"""Independent Coin Tarama 5 workflow: public data only, own state and Issue lifecycle."""
import argparse,json,os,re,time
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
from collections import Counter
import github_scan as cloud
import coin5_model as model
import coin5_sources as source
import short_squeeze_sources as futures
import short_squeeze_positions as ratios
import short_squeeze_lab as measurement

ROOT=Path(__file__).parent;OUT=ROOT/'cloud_output_coin5';STATE=OUT/'state.json'
LABELS={'preparation':'HAZIRLIK','triggered':'TETİKLENDİ','cancelled':'İPTAL','expired':'SÜRE DOLDU'}
def now_ms():return int(time.time()*1000)
def configure():
    expected=model.config()['state_branch']
    if os.environ.setdefault('SCANNER_STATE_BRANCH',expected)!=expected:raise ValueError('Coin Tarama 5 must use its independent state branch')
    cloud.OUT=OUT;cloud.STATE=STATE;cloud.fingerprint=model.fingerprint;cloud.new_state=model.new_state
def settings():
    repo=os.environ.get('GITHUB_REPOSITORY','');token=os.environ.get('GH_TOKEN','');user=os.environ.get('COIN_NOTIFY_USER','').strip()
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo) or not token:raise ValueError('GitHub Issue notification configuration missing')
    if user and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',user):raise ValueError('Invalid recipient')
    return 'https://api.github.com/repos/'+repo+'/issues',{'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'},user
def marker(event):return '<!-- coin-tarama-5:'+event['id']+' -->'
def delivered(state,event):
    if not any(d['id']==event['id'] for d in state['delivery']):state['delivery'].append({'id':event['id'],'asset_id':event['asset_id'],'phase':event['phase'],'observed_ms':event['observed_ms']})
    state['delivery']=state['delivery'][-2000:]

def reconcile(state,channel):
    if channel!='github_issue' or not state['pending']:return
    url,headers,_=settings();issues=cloud.http_json(url+'?state=all&sort=created&direction=desc&per_page=100',headers=headers,label='GitHub Issues')
    remaining=[]
    for event in state['pending']:
        if any(marker(event) in (i.get('body') or '') and i.get('user',{}).get('login')=='github-actions[bot]' for i in issues):delivered(state,event)
        else:remaining.append(event)
    state['pending']=remaining

def collect(venue,state,cfg):
    spot=source.Spot(venue);client=futures.Public(venue);errors=[];records=[];cache={k:v for k,v in state['cache'].items() if k.startswith(venue+':')}
    oi_history={k:deepcopy(v) for k,v in state['oi_history'].items() if k.startswith(venue+':')}
    rhistory={k:deepcopy(v) for k,v in state['ratio_history'].items() if k.startswith(venue+':')}
    active=[a for a in state['assets'].values() if a['exchange']==venue and a['phase'] in ('preparation','triggered')]
    for attempt in range(2):
        try:markets=futures.markets(client,now_ms);break
        except Exception as e:
            markets={}
            if client.blocked or attempt or 'connection' not in str(e):errors.append('futures: '+str(e));break
            time.sleep(1)
    policy=json.loads((ROOT/'strength_v5_priority_config.json').read_text(encoding='utf-8'))
    sampling=json.loads((ROOT/'study_config.json').read_text(encoding='utf-8'))['sampling']
    excludes={'stable':sampling['stable_bases'],'plates':sampling['excluded_concept_plates'],'equity':policy['excluded_equity_bases']}
    try:universe,coverage=source.universe(spot,markets,cfg,excludes)
    except Exception as e:universe=[];coverage={};errors.append('spot universe: '+str(e))
    cursor=state['venues'].get(venue,{}).get('cursor',0);n=len(universe)
    rotating=[universe[(cursor+i)%n]['symbol'] for i in range(min(n,cfg['rotate_per_venue']))] if n else []
    symbols=list(dict.fromkeys([a['symbol'] for a in active]+rotating));volumes={u['symbol']:u['volume24'] for u in universe}
    positions={p:ratios.Client(p) for p in ratios.SCOPES}
    try:btc=source.bars(spot,'BTCUSDT','1h',now_ms(),cfg,cache);btc_quote=spot.book('BTCUSDT',now_ms())
    except Exception as e:btc=None;btc_quote=None;errors.append('BTC context: '+str(e))
    for symbol in symbols:
        if spot.blocked:break
        try:
            stamp=now_ms();series={interval:source.bars(spot,symbol,interval,stamp,cfg,cache) for interval in source.STEPS}
            if btc is None:raise ValueError('BTC context unavailable')
            if series['1h'][-1]['t']!=btc[-1]['t']:raise ValueError('BTC and symbol hour cutoffs differ')
            ctx=model.context(series,btc,cfg);prep=model.preparation(series,ctx,cfg)
            market=markets.get(symbol);key=venue+':'+symbol;profiles={}
            # Price preparation is evaluated BEFORE derivative requests; active setups always stay under observation.
            is_active=any(a['symbol']==symbol for a in active)
            if prep['valid'] or is_active:
                profiles={p:c.read(symbol,now_ms,cfg) for p,c in positions.items()}
            history_by_provider={p:rhistory.get(key+':'+p,[]) for p in profiles}
            funding=None
            if market and (prep['valid'] or is_active):
                try:funding=futures.funding(client,market,now_ms)
                except Exception as e:errors.append(symbol+' funding support unknown: '+str(e))
            der=model.derivative_context(market,funding,oi_history.get(key,[]),profiles,history_by_provider,cfg,now_ms())
            for provider,p in profiles.items():
                if p['status']=='observed':model.remember(rhistory.setdefault(key+':'+provider,[]),p,'provider_ms',now_ms())
                elif p['status']=='unknown':errors.append(symbol+' '+provider+': '+p.get('reason','ratio unknown'))
            quote=spot.book(symbol,now_ms());stamp=now_ms()
            entry_btc=btc_quote
            if prep['valid'] or is_active:
                try:entry_btc=spot.book('BTCUSDT',now_ms())
                except Exception as e:entry_btc=None;errors.append(symbol+' fresh BTC reference: '+str(e))
            book_reasons=[]
            if quote['spread_pct']>cfg['maximum_spread_pct']:book_reasons.append('spot_spread')
            if market is None:book_reasons.append('futures_unknown')
            else:
                if stamp-market['observed_ms']>300000:book_reasons.append('futures_stale')
                if market['oi_notional']<cfg['minimum_oi_notional']:book_reasons.append('oi_liquidity')
                if market['spread_pct']>cfg['maximum_spread_pct']:book_reasons.append('futures_spread')
                if abs(market['mid_price']/quote['price']-1)*100>cfg['maximum_basis_pct']:book_reasons.append('spot_futures_basis')
            if series['15m'][-1]['t']+900000!=stamp//900000*900000:book_reasons.append('closed_15m_stale')
            if series['1h'][-1]['t']+3600000!=stamp//3600000*3600000:book_reasons.append('closed_1h_stale')
            if series['4h'][-1]['t']+14400000!=stamp//14400000*14400000:book_reasons.append('closed_4h_stale')
            # Return current liquid volume from ticker universe. Excluded active entries cannot retrigger.
            if symbol not in volumes:book_reasons.append('not_in_current_liquid_universe')
            row={'symbol':symbol,'exchange':venue,'quote':quote,'series':series,'context':ctx,'preparation':prep,
                 'derivatives':der,'btc_quote':entry_btc,'volume24':volumes.get(symbol),'book_reasons':book_reasons,'observed_ms':quote['observed_ms']}
            records.append(row)
        except Exception as e:
            errors.append(symbol+': '+str(e))
            if any(a['symbol']==symbol for a in active) and not spot.blocked:
                try:
                    quote=spot.book(symbol,now_ms())
                    records.append({'symbol':symbol,'exchange':venue,'quote':quote,'series':{},
                        'context':{'reasons':['technical_data_unknown']},'preparation':{'valid':False},
                        'derivatives':{'ready':False,'reasons':['data_unknown'],'profiles':{}},
                        'btc_quote':None,'volume24':None,'book_reasons':['data_unknown'],'observed_ms':quote['observed_ms']})
                except Exception:pass
    # Record current universe snapshots only AFTER comparison; no backfilled OI.
    keep=set(symbols)|{u['symbol'] for u in universe}
    for symbol in keep:
        market=markets.get(symbol)
        if market:model.remember(oi_history.setdefault(venue+':'+symbol,[]),market,'observed_ms',now_ms())
    # Prune cache/history to the current bounded universe plus active references.
    cache={k:v for k,v in cache.items() if k.split(':')[1] in keep|{'BTCUSDT'}}
    oi_history={k:v for k,v in oi_history.items() if k.split(':')[1] in keep}
    rhistory={k:v for k,v in rhistory.items() if k.split(':')[1] in keep}
    return {'records':records,'cache':cache,'oi_history':oi_history,'ratio_history':rhistory,'errors':errors,
            'coverage':{**coverage,'requested':len(symbols),'evaluated':len(records),'rotated':len(rotating),'active':len(active)},
            'cursor':(cursor+len(rotating))%n if n else cursor,'calls':{'spot':spot.calls,'futures':client.calls,'ratios':{p:c.calls for p,c in positions.items()}}}

def apply_records(state,results,cfg,stamp):
    records=[r for result in results.values() for r in result['records'] if 0<=stamp-r['quote']['observed_ms']<=cfg['max_quote_age_minutes']*60000]
    bykey={(r['exchange'],r['symbol']):r for r in records}
    for asset in state['assets'].values():
        if asset['phase'] not in ('preparation','triggered'):continue
        row=bykey.get((asset['exchange'],asset['symbol']))
        if row is None:continue # An API gap is not evidence of support loss.
        asset['latest_price']=row['quote']['price'];asset['last_observed_ms']=row['observed_ms'];asset['latest_derivatives']=row['derivatives']
        # A fresh quote can invalidate a setup even when technical/ratio data are unavailable.
        evaluate=deepcopy(row)
        if row['book_reasons']:evaluate['derivatives']['ready']=False
        phase=model.transition(asset,evaluate,row['observed_ms'],cfg)
        if phase:
            model.enqueue(state,asset,phase,row,row['observed_ms'])
            if phase=='triggered':model.register_measurement(state,asset,phase,row,row['observed_ms'])
            else:state['last_closed'][asset['symbol']]=row['observed_ms']
        if asset['phase'] in ('preparation','triggered') and not row['book_reasons']:
            model.register_measurement(state,asset,asset['phase'],row,row['observed_ms'])
    active={a['symbol'] for a in state['assets'].values() if a['phase'] in ('preparation','triggered')}
    ready=[r for r in records if not r['book_reasons'] and r['preparation']['valid'] and r['derivatives']['ready'] and
           r['quote']['price']<=r['preparation']['level'] and r['quote']['price']>r['preparation']['invalid'] and
           (r['quote']['price']-r['preparation']['invalid'])/r['quote']['price']*100<=cfg['maximum_risk_pct']]
    ready.sort(key=lambda r:(-r['derivatives']['score'],r['quote']['spread_pct'],-r['volume24'],r['symbol'],r['exchange']))
    new=[]
    for row in ready:
        symbol=row['symbol']
        if symbol in active or len(active)>=cfg['max_active_symbols']:continue
        if stamp-state['last_closed'].get(symbol,0)<cfg['cooldown_hours']*3600000:continue
        p=row['preparation'];uid=__import__('hashlib').sha256(json.dumps([symbol,row['exchange'],row['observed_ms']]).encode()).hexdigest()[:24]
        asset={'id':uid,'symbol':symbol,'exchange':row['exchange'],'phase':'preparation','created_ms':row['observed_ms'],
               'level':p['level'],'invalid':p['invalid'],'atr':p['atr'],'initial_price':row['quote']['price'],
               'latest_price':row['quote']['price'],'last_observed_ms':row['observed_ms'],'latest_derivatives':row['derivatives']}
        state['assets'][uid]=asset;active.add(symbol);new.append(symbol)
        model.enqueue(state,asset,'preparation',row,row['observed_ms']);model.register_measurement(state,asset,'preparation',row,row['observed_ms'])
    # Refresh a not-yet-delivered preparation from an actual fresh observation.
    # Its original signal time stays visible; never reprice a registered paper entry.
    for event in state['pending']:
        asset=state['assets'].get(event['asset_id']);row=bykey.get((event['exchange'],event['symbol']))
        if asset and row and asset['phase']==event['phase']=='preparation' and not row['book_reasons'] and row['derivatives']['ready']:
            event.update(observed_ms=row['observed_ms'],price=row['quote']['price'],derivatives=deepcopy(row['derivatives']),context=deepcopy(row['context']))
    return new

def scan(channel):
    cfg=model.config();state=json.loads(STATE.read_text(encoding='utf-8'));reconcile(state,channel)
    if state['rules_fingerprint']!=model.fingerprint():raise ValueError('New strategy version required before changing rules')
    results={}
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs={pool.submit(collect,v,state,cfg):v for v in ('MEXC','OKX')}
        for job in as_completed(jobs):
            venue=jobs[job]
            try:results[venue]=job.result()
            except Exception as e:results[venue]={'records':[],'coverage':{},'errors':[str(e)],'cursor':state['venues'].get(venue,{}).get('cursor',0),'calls':{}}
    for venue,r in results.items():
        state['venues'][venue]={'cursor':r['cursor'],'coverage':r['coverage'],'errors':r['errors'],'calls':r['calls']}
        for field in ('cache','oi_history','ratio_history'):
            if field in r:
                state[field]={**{k:v for k,v in state[field].items() if not k.startswith(venue+':')},**r[field]}
    stamp=now_ms();new=apply_records(state,results,cfg,stamp)
    counts=Counter(reason for r in results.values() for row in r['records'] for reason in row['book_reasons']+row['context']['reasons']+row['derivatives']['reasons'])
    counts['price_preparation_not_ready']=sum(not row['preparation']['valid'] for r in results.values() for row in r['records'])
    # Never serialize full duplicate row candle histories into report state.
    state['latest']={'observed_ms':stamp,'new_preparations':new,'reasons':dict(counts),
        'evaluated':sum(len(r['records']) for r in results.values()),'pending':len(state['pending']),
        'errors':{v:r['errors'] for v,r in results.items()},'failed_venues':[v for v,r in results.items() if not r['records']]}
    cloud.save(STATE,state);render(state);(OUT/'ready.txt').write_text('complete',encoding='ascii');print(json.dumps(state['latest']))

def describe(e):
    d=e['derivatives'];a=e['context'];num=lambda x:'bilinmiyor' if x is None else f'{x:+.2f}'
    lines=[f"**{LABELS[e['phase']]} · {e['symbol']} · {e['exchange']}**",f"Gerçek gözlem: {cloud.time_label(e['observed_ms'])} TR; spot {e['price']:.8g}",
           f"Sabit direnç {e['level']:.8g}; geçersizlik {e['invalid']:.8g}",
           f"OI değişimi %{num(d.get('oi_change_pct'))}; aynı aralıkta vadeli fiyat %{num(d.get('price_change_pct'))}"]
    if e.get('signal_ms')!=e['observed_ms']:lines.append('İlk hazırlık tespiti: '+cloud.time_label(e['signal_ms'])+' TR; bu mesajın fiyatı son gerçek gözlemdir.')
    if d.get('oi_old_ms'):lines.append(f"OI veri aralığı: {cloud.time_label(d['oi_old_ms'])} → {cloud.time_label(d['oi_ms'])} TR")
    for provider,p in d.get('profiles',{}).items():
        if p.get('change_pp') is not None:
            delta=p['change_pp'];old=p['previous_short_pct'];relative='tanımsız' if old==0 else f'%{delta/old*100:+.2f}'
            lines.append(f"{p['scope']}: short %{old:.2f} → %{p['short_pct']:.2f} ({delta:+.2f} yüzde puan; göreli {relative}); long %{p['long_pct']:.2f}. Veri {cloud.time_label(p['old_ms'])} → {cloud.time_label(p['provider_ms'])} TR")
        else:lines.append(provider+': '+p['status']+'; eksik veri olumlu sayılmadı.')
    lines.append('8 saate ölçekli fonlama %'+num(d.get('funding_8h_pct'))+'; negatif olması ek destek, zorunlu değil.')
    if d.get('opposing_sources'):lines.append('Kaynaklar ayrışıyor: '+', '.join(d['opposing_sources'])+' short payı azalıyor; oranlar ortalanmaz.')
    if e['phase']=='preparation':lines.append('Hazırlık gözlemidir; kırılım henüz teyit edilmedi.')
    if e.get('trigger_kind'):lines.append('Teyit: '+e['trigger_kind'])
    if e.get('reason'):lines.append('Neden: '+e['reason'])
    lines.append('Grup pozisyon dağılımı tüm piyasanın short toplamı veya gerçekleşmiş likidasyon değildir. Deneysel takip; emir gönderilmez.')
    return '\n\n'.join(lines)

def render(state):
    cfg=model.config();latest=state.get('latest',{});assets=[a for a in state['assets'].values() if a['phase'] in ('preparation','triggered')]
    lines=['# Coin Tarama 5','',f"Son gözlem: {cloud.time_label(latest.get('observed_ms',now_ms()))} TR.",'',
        'Bağımsız fiyat + pozisyon davranışı deneyi. 4s genel yapı, 1s hazırlık bağlamı, kapalı 15dk mumla kırılım/geri test; yaklaşık 5dk kamu veri kontrolü. GitHub gecikebilir/atlayabilir. Fiyat düşmezken OI ve kaynak grubun short payı artışı aranır; negatif fonlama yalnız ek destek.','',
        f"Aktif {len(assets)} farklı coin; sınır {cfg['max_active_symbols']}. Hazırlık/tetik aynı coin için iki bağımsız başarı sayılmaz. Eski taramaların hiçbir state dalı okunmaz/yazılmaz.",'',
        '| Coin | Borsa | Durum | İlk gerçek gözlem TR | Son spot | Sabit direnç | Geçersizlik | Son kontrol TR |',
        '|---|---|---|---|---:|---:|---:|---|']
    for a in assets:lines.append(f"| {a['symbol']} | {a['exchange']} | {LABELS[a['phase']]} | {cloud.time_label(a['created_ms'])} | {a['latest_price']:.8g} | {a['level']:.8g} | {a['invalid']:.8g} | {cloud.time_label(a['last_observed_ms'])} |")
    if not assets:lines+=['','Şu an doğrulanmış hazırlık/tetik yok. İlk OI ve oran bazları yaklaşık 45–75dk aralığında gerçek gözlemler biriktirir; kapsam rotasyonu/sağlayıcı/GitHub gecikmesi bunu uzatabilir.']
    for venue,v in state['venues'].items():lines+=['',venue+': '+json.dumps(v,ensure_ascii=False)]
    lines+=['','## Eleme ve veri durumu','',json.dumps(latest.get('reasons',{}),ensure_ascii=False),
        '',f"Bekleyen mesaj: {len(state['pending'])}. Deneysel eşikler başarı olasılığı değildir; yalnız sinyal sayısını artırmak için değiştirilmez.",'',
        'Evren her borsada en likit en çok60 spot+USDT perpetual paritesi; her döngüde12 dönüşümlü parite ve aktif adaylar. Tüm piyasa veya her coin her5dk inceleniyor iddiası yok. Tokenleştirilmiş hisseler/stable/leveraged metadata ile elenir. Evren sıralamasında dönüş yapmış coinleri zorunlu kılan 24s pozitif getiri koşulu yok.','',
        'Oranlar OKX en büyük %5 pozisyon grubu ve Binance en büyük %20 teminat grubunun pozisyon ağırlıklarıdır. Kaynaklar ayrı kalır, birinde onay yeterlidir; diğeri ters yöndeyse ayrışma açıkça yazılır. Farklı borsa oranı MEXC oranı sayılmaz. Bir saatlik short payı artışı yeni short tutarını kanıtlamaz; grup değişimi/hedge/long azalması etkili olabilir.','',
        'Eksik oran/OI pozitif kabul edilmez. Kaynak veya mum hatası destek kaybı sayılmaz; aktif aday son gerçek gözlemiyle kalır. İptal yalnız yeni doğrulanmış fiyat/seviye kaybında; süre dolması ayrı etiketlenir. Açık mum olumlu sinyal üretmez. Destek ve direnç hazırlık anında dondurulur. Tetik hazırlıktan sonraki kapalı15dk mumda değerlendirilir; geçmiş kırılıma yeni tetik yazılmaz.','',
        'Öngörülen risk mesafesi en çok%6; tetiğe 1ATR fazla uzamış fiyat takip edilmez. Son24 kapalı4s mumdaki en yakın yukarı tepe biliniyorsa en az2R mesafe aranır; gözlenen yukarı tepe yoksa alan bilinmiyor olarak kalır ve2R kazanç vaat edilmez.','',
        '## Gerçek gözlem sonuçları','',
        'İlk gerçek hazırlık ve ilk gerçek tetik fiyatları ayrı saklanır; sembol/evre tekrarları yeni bağımsız başarı değildir. Sonuçlar1/4/12/24 saat; BTC farkı, tam sonraki1dk mum yolunda MAE/MFE ve %0.2/%0.5/%1 maliyet senaryoları. Gerçek net kâr veya stop emri gerçekleşmesi değildir; eşlenmiş kontrol coinleri bu sürümde yoktur. Eksik veri bilinmiyor.','',
        '| Coin | Evre | Borsa | Gerçek giriş TR | Referans | 1s % | 4s % | 12s % | 24s % |','|---|---|---|---|---:|---:|---:|---:|---:|']
    for c in state['measurements']['cases'].values():
        vals=['—' if c['outcomes'].get(str(h),{}).get('return_pct') is None else f"{c['outcomes'][str(h)]['return_pct']:+.2f}" for h in cfg['horizons_hours']]
        lines.append(f"| {c['symbol']} | {LABELS[c['phase']]} | {c['exchange']} | {cloud.time_label(c['observed_ms'])} | {c['entry_price']:.8g} | {' | '.join(vals)} |")
    lines+=['',f"Ölçüm hataları: {len(state['measurements'].get('errors',[]))}. Ölçüm için döngüde en çok2 kayıt; eksik/ara mumlar sıfır veya başarı sayılmaz. Girişten sonraki ilk tam dakika öncesi parça MAE/MFE dışındadır.",'',
        '## Son olaylar','']
    recent=list(state['assets'].values())[-15:]
    for a in recent:lines.append(f"- {a['symbol']} {a['exchange']}: {LABELS[a['phase']]} · son {cloud.time_label(a['last_observed_ms'])} TR")
    (OUT/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

def event_current(event,state,stamp,cfg):
    asset=state['assets'].get(event['asset_id'])
    if asset is None or asset['phase']!=event['phase']:return False
    if not 0<=stamp-event['observed_ms']<=cfg['max_notification_age_minutes']*60000:return False
    if event['phase'] in ('cancelled','expired') and not any(d['asset_id']==event['asset_id'] for d in state['delivery']):return False
    return True

def notify(channel):
    state=json.loads(STATE.read_text(encoding='utf-8'));cfg=model.config();reconcile(state,channel)
    if channel=='report':state['pending']=[];cloud.save(STATE,state);render(state);return
    valid=[e for e in state['pending'] if event_current(e,state,now_ms(),cfg)]
    if valid:
        url,headers,user=settings()
        body=('@'+user+'\n\n' if user else '')+'Coin Tarama 5 — hazırlık / tetik / iptal\n\n'+'\n\n---\n\n'.join(describe(e) for e in valid)
        body+='\n\nRapor: https://github.com/'+os.environ['GITHUB_REPOSITORY']+'/blob/'+cfg['state_branch']+'/report.md\n\n'+'\n'.join(marker(e) for e in valid)
        title='Coin Tarama 5 · '+', '.join(sorted({LABELS[e['phase']] for e in valid}))+' · '+cloud.time_label(now_ms())
        cloud.http_json(url,{'title':title,'body':body},headers,label='GitHub Issues')
        for e in valid:delivered(state,e)
    state['pending']=[];cloud.save(STATE,state);render(state)

def measure():
    state=json.loads(STATE.read_text(encoding='utf-8'));measurement.measure(state['measurements'],model.config(),now_ms())
    cloud.save(STATE,state);render(state)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['pull-state','scan','notify','measure','push-state','check-status']);p.add_argument('--channel',choices=['github_issue','report'],default='github_issue');args=p.parse_args();configure()
    if args.phase=='pull-state':cloud.pull_state()
    elif args.phase=='scan':scan(args.channel)
    elif args.phase=='notify':notify(args.channel)
    elif args.phase=='measure':measure()
    elif args.phase=='push-state':
        if not (OUT/'ready.txt').exists():raise RuntimeError('No complete observation checkpoint')
        cloud.push_state()
    else:
        s=json.loads(STATE.read_text(encoding='utf-8'));raise SystemExit(1 if s['latest']['failed_venues'] or any(s['latest']['errors'].values()) or s['measurements'].get('errors') else 0)
