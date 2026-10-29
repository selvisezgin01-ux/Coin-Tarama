"""V2 orchestration; bounded public reads, full top-60 coverage and internal watch pool."""
import json,os,time,hashlib
from copy import deepcopy
from collections import Counter
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import coin5_scan as oldrun
import coin5_model as v1
import coin5_v2_model as model
import coin5_sources as source
import coin5_v2_measure as study
import short_squeeze_sources as futures
import short_squeeze_positions as ratios
import github_scan as cloud
ROOT=Path(__file__).parent;OUT=ROOT/'cloud_output_coin5_v2';STATE=OUT/'state.json'
LABELS=oldrun.LABELS
def now_ms():return int(time.time()*1000)
def configure():
    expected=model.config()['state_branch']
    if os.environ.setdefault('SCANNER_STATE_BRANCH',expected)!=expected:raise ValueError('V2 state isolation required')
    cloud.ROOT=ROOT;cloud.OUT=OUT;cloud.STATE=STATE;cloud.fingerprint=model.fingerprint;cloud.new_state=model.new_state

def collect(venue,state,cfg):
    spot=source.Spot(venue);client=futures.Public(venue);errors=[];records=[]
    cache={k:v for k,v in state['cache'].items() if k.startswith(venue+':')}
    oi_history={k:deepcopy(v) for k,v in state['oi_history'].items() if k.startswith(venue+':')}
    rhistory={k:deepcopy(v) for k,v in state['ratio_history'].items() if k.startswith(venue+':')}
    active=[a for a in state['assets'].values() if a['exchange']==venue and a['phase'] in ('preparation','triggered')]
    active_symbols={a['symbol'] for a in active}
    try:markets=futures.markets(client,now_ms)
    except Exception as e:markets={};errors.append('futures: '+str(e));client.blocked=True
    policy=json.loads((ROOT/'strength_v5_priority_config.json').read_text(encoding='utf-8'))
    sampling=json.loads((ROOT/'study_config.json').read_text(encoding='utf-8'))['sampling']
    excludes={'stable':sampling['stable_bases'],'plates':sampling['excluded_concept_plates'],'equity':policy['excluded_equity_bases']}
    try:universe,coverage=source.universe(spot,markets,cfg,excludes)
    except Exception as e:universe=[];coverage={};errors.append('spot universe: '+str(e))
    volumes={u['symbol']:u['volume24'] for u in universe}
    symbols=list(dict.fromkeys([a['symbol'] for a in active]+[u['symbol'] for u in universe]))
    start=time.monotonic();prepared=[];diagnostics=Counter();chart_count=0;attempted=0
    try:btc=source.bars(spot,'BTCUSDT','1h',now_ms(),cfg,cache)
    except Exception as e:btc=None;errors.append('BTC context: '+str(e))
    for symbol in symbols:
        if spot.blocked:break
        if time.monotonic()-start>=cfg['maximum_chart_seconds']:
            errors.append('chart_time_budget: remaining '+str(len(symbols)-attempted)+' symbols not observed');break
        attempted+=1
        try:
            stamp=now_ms();series={interval:source.bars(spot,symbol,interval,stamp,cfg,cache) for interval in source.STEPS}
            if btc is None:raise ValueError('BTC context unavailable')
            if series['1h'][-1]['t']!=btc[-1]['t']:raise ValueError('BTC and symbol hour cutoffs differ')
            ctx=model.context(series,btc,cfg);prep=v1.preparation(series,ctx,cfg);chart_count+=1
            diagnostics.update(ctx['reasons'])
            if not prep['valid']:diagnostics['price_preparation_not_ready']+=1
            if prep['valid'] or symbol in active_symbols:prepared.append((symbol,series,ctx,prep))
        except Exception as e:
            errors.append(symbol+': '+str(e))
            if symbol in active_symbols:prepared.append((symbol,{}, {'reasons':['technical_data_unknown']},{'valid':False}))
    # Candle reads precede the fresh bulk OI snapshot and final watched quotes.
    # Slow universe reads cannot silently turn an old OI ticker into current evidence.
    if not client.blocked:
        try:markets=futures.markets(client,now_ms)
        except Exception as e:markets={};errors.append('fresh futures: '+str(e));client.blocked=True
    keep=set(symbols)
    for symbol in keep:
        if symbol in markets:v1.remember(oi_history.setdefault(venue+':'+symbol,[]),markets[symbol],'observed_ms',now_ms())
    positions={p:ratios.Client(p) for p in ratios.SCOPES}
    active_preps=sum(a['phase']=='preparation' for a in active)
    slots=max(0,cfg['max_preparations_per_venue']-active_preps)
    selected=[p for p in prepared if p[0] in active_symbols]+[p for p in prepared if p[0] not in active_symbols][:slots]
    staged=[]
    for symbol,series,ctx,prep in selected:
        key=venue+':'+symbol;market=markets.get(symbol);profiles={}
        if series:
            profiles={p:c.read(symbol,now_ms,cfg) for p,c in positions.items()}
            for provider,p in profiles.items():
                if p['status']=='unknown':
                    errors.append(symbol+' '+provider+': '+p.get('reason','unknown'))
                    # A connection outage is not retried for every watched symbol.
                    if 'connection' in p.get('reason',''):positions[provider].blocked=True
        funding=None
        if market and not client.blocked:
            try:funding=futures.funding(client,market,now_ms)
            except Exception as e:errors.append(symbol+' funding support unknown: '+str(e))
        old=oi_history.get(key,[])
        history_by_provider={p:rhistory.get(key+':'+p,[]) for p in profiles}
        der=model.derivatives(market,funding,old,profiles,history_by_provider,cfg,now_ms())
        for provider,p in profiles.items():
            if p['status']=='observed':v1.remember(rhistory.setdefault(key+':'+provider,[]),p,'provider_ms',now_ms())
        staged.append((symbol,series,ctx,prep,der,market))
    # Final quote pass after all candle/ratio reads, including fresh BTC reference.
    try:btc_quote=spot.book('BTCUSDT',now_ms())
    except Exception as e:btc_quote=None;errors.append('fresh BTC quote: '+str(e))
    for symbol,series,ctx,prep,der,market in staged:
        try:
            quote=spot.book(symbol,now_ms());stamp=now_ms();reasons=[]
            if quote['spread_pct']>cfg['maximum_spread_pct']:reasons.append('spot_spread')
            if market is None:reasons.append('futures_unknown')
            else:
                if stamp-market['observed_ms']>300000:reasons.append('futures_stale')
                if market['oi_notional']<cfg['minimum_oi_notional']:reasons.append('oi_liquidity')
                if market['spread_pct']>cfg['maximum_spread_pct']:reasons.append('futures_spread')
                if abs(market['mid_price']/quote['price']-1)*100>cfg['maximum_basis_pct']:reasons.append('spot_futures_basis')
            for interval,step in source.STEPS.items():
                if not series.get(interval) or series[interval][-1]['t']+step!=stamp//step*step:reasons.append('closed_'+interval+'_stale')
            if symbol not in volumes:reasons.append('not_in_current_liquid_universe')
            if btc_quote is None or not 0<=stamp-btc_quote['observed_ms']<=cfg['max_quote_age_minutes']*60000:reasons.append('btc_quote_unknown_or_stale')
            # Also ensure ratio evidence did not age out while other symbols were read.
            if market is None or stamp-market['observed_ms']>300000:der['ready']=False
            records.append({'symbol':symbol,'exchange':venue,'quote':quote,'series':series,'context':ctx,
                'preparation':prep,'derivatives':der,'btc_quote':btc_quote,'volume24':volumes.get(symbol),
                'book_reasons':reasons,'observed_ms':quote['observed_ms']})
        except Exception as e:errors.append(symbol+' quote: '+str(e))
    coverage.update(requested=len(symbols),attempted=attempted,chart_evaluated=chart_count,
        evaluated=len(records),candidate_quotes=len(records),active=len(active),chart_budget_seconds=cfg['maximum_chart_seconds'])
    return {'records':records,'cache':{k:v for k,v in cache.items() if k.split(':')[1] in keep|{'BTCUSDT'}},
        'oi_history':{k:v for k,v in oi_history.items() if k.split(':')[1] in keep},
        'ratio_history':{k:v for k,v in rhistory.items() if k.split(':')[1] in keep},
        'errors':errors,'coverage':coverage,'cursor':0,'diagnostics':dict(diagnostics),
        'calls':{'spot':spot.calls,'futures':client.calls,'ratios':{p:c.calls for p,c in positions.items()}}}

def apply_records(state,results,cfg,stamp):
    raw=[r for x in results.values() for r in x['records']]
    rows=[r for r in raw if 0<=stamp-r['quote']['observed_ms']<=cfg['max_quote_age_minutes']*60000]
    bykey={(r['exchange'],r['symbol']):r for r in rows}
    triggered={a['symbol'] for a in state['assets'].values() if a['phase']=='triggered'}
    ranked=sorted(rows,key=lambda r:(-r['derivatives'].get('score',0),r['quote']['spread_pct'],-(r['volume24'] or 0),r['symbol'],r['exchange']))
    # Existing assets always receive verified invalidation before new entries.
    for a in state['assets'].values():
        if a['phase'] not in ('preparation','triggered'):continue
        r=bykey.get((a['exchange'],a['symbol']))
        if r is None:continue
        a.update(latest_price=r['quote']['price'],last_observed_ms=r['observed_ms'],latest_derivatives=r['derivatives'])
        evaluate=deepcopy(r)
        if r['book_reasons'] or (a['phase']=='preparation' and len(triggered)>=cfg['max_active_symbols']):
            evaluate['derivatives']['ready']=False;evaluate['derivatives']['reasons'].append('book_or_active_limit')
        phase=model.transition(a,evaluate,r['observed_ms'],cfg)
        if phase:
            model.enqueue(state,a,phase,r,r['observed_ms'])
            if phase=='triggered':
                triggered.add(a['symbol']);model.register(state,a,r,r['observed_ms'])
            else:triggered.discard(a['symbol']);state['last_closed'][a['symbol']]=r['observed_ms']
    active={a['symbol'] for a in state['assets'].values() if a['phase'] in ('preparation','triggered')}
    added=[]
    for r in ranked:
        symbol=r['symbol'];p=r['preparation']
        if symbol in active or r['book_reasons'] or not p['valid']:continue
        count=sum(a['exchange']==r['exchange'] and a['phase']=='preparation' for a in state['assets'].values())
        if count>=cfg['max_preparations_per_venue']:continue
        if stamp-state['last_closed'].get(symbol,0)<cfg['cooldown_hours']*3600000:continue
        if not p['invalid']<r['quote']['price']<=p['level']:continue
        if (r['quote']['price']-p['invalid'])/r['quote']['price']*100>cfg['maximum_risk_pct']:continue
        uid=hashlib.sha256(json.dumps([symbol,r['exchange'],r['observed_ms']]).encode()).hexdigest()[:24]
        state['assets'][uid]={'id':uid,'symbol':symbol,'exchange':r['exchange'],'phase':'preparation',
            'created_ms':r['observed_ms'],'level':p['level'],'base_invalid':p['invalid'],'invalid':p['invalid'],
            'atr':p['atr'],'initial_price':r['quote']['price'],'latest_price':r['quote']['price'],
            'last_observed_ms':r['observed_ms'],'latest_derivatives':r['derivatives']}
        active.add(symbol);added.append(symbol)
    return added,len(raw)-len(rows)

def observe(state,cfg):
    results={}
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs={pool.submit(collect,v,state,cfg):v for v in ('MEXC','OKX')}
        for job in as_completed(jobs):
            v=jobs[job]
            try:results[v]=job.result()
            except Exception as e:results[v]={'records':[],'errors':[str(e)],'coverage':{},'calls':{},'cursor':0}
    for v,r in results.items():
        state['venues'][v]={k:r[k] for k in ('coverage','errors','calls','cursor')}
        for field in ('cache','oi_history','ratio_history'):
            if field in r:state[field]={**{k:x for k,x in state[field].items() if not k.startswith(v+':')},**r[field]}
    stamp=now_ms();added,stale=apply_records(state,results,cfg,stamp)
    counts=Counter(reason for r in results.values() for row in r['records'] for reason in row['book_reasons']+row['context']['reasons']+row['derivatives']['reasons'])
    for r in results.values():counts.update(r.get('diagnostics',{}))
    counts['stale_quotes_excluded']=stale
    state['latest']={'observed_ms':stamp,'new_preparations':added,'reasons':dict(counts),
        'evaluated':sum(r['coverage'].get('chart_evaluated',0) for r in results.values()),
        'candidate_quotes':sum(len(r['records']) for r in results.values()),'errors':{v:r['errors'] for v,r in results.items()},
        'failed_venues':[v for v,r in results.items() if not r['coverage'].get('chart_evaluated')]}

def marker(e):return '<!-- coin-tarama-5-v2:'+e['id']+' -->'
def delivered(state,e,stamp):
    if not any(x['id']==e['id'] for x in state['delivery']):
        state['delivery'].append({'id':e['id'],'asset_id':e['asset_id'],'phase':e['phase'],
            'observed_ms':e['observed_ms'],'delivered_ms':stamp,'notification_lag_ms':stamp-e['observed_ms']})
    c=state['measurements']['cases'].get(e['symbol'])
    if c and c['asset_id']==e['asset_id'] and e['phase']=='triggered':c['notification_lag_ms']=stamp-e['observed_ms']

def reconcile(state,channel):
    if channel!='github_issue' or not state['pending']:return
    url,headers,_=oldrun.settings()
    issues=cloud.http_json(url+'?state=all&sort=created&direction=desc&per_page=100',headers=headers,label='GitHub Issues')
    for e in list(state['pending']):
        if any(marker(e) in (i.get('body') or '') and i.get('user',{}).get('login')=='github-actions[bot]' for i in issues):
            delivered(state,e,now_ms());state['pending'].remove(e)

def current(e,state,stamp,cfg):
    a=state['assets'].get(e['asset_id'])
    if not a or a['phase']!=e['phase']:return False
    if not 0<=stamp-e['observed_ms']<=cfg['max_notification_age_minutes']*60000:return False
    if e['phase'] in ('cancelled','expired') and not any(x['asset_id']==a['id'] for x in state['delivery']):return False
    return True

def describe(e):
    text=oldrun.describe(e)
    if e.get('entry_plan'):
        p=e['entry_plan']
        text+=f"\n\nGiriş izleme bölgesi {p['entry_zone_low']:.8g}–{p['entry_zone_high']:.8g}; geçersizlik {p['stop']:.8g}; varsayımsal hedef {p['target']:.8g}. Gözlenen direnç {p['resistance']:.8g}. %{p['planning_cost_pct']:.2f} toplam maliyet varsayımıyla alan {p['net_room_r']:.2f}R."
    if e['phase']=='triggered':
        text+='\n\nShort artışı teyidi: '+('VAR' if e['strict_short_confirmed'] else 'YOK / bilinmeyen kaynak ayrıntısı yukarıda')
        text+='\n\nSinyal kapanışından gözleme gecikme: '+f"{(e['observed_ms']-e['source_close_ms'])/60000:.1f} dk."
    return text

def notify(state,channel,cfg):
    reconcile(state,channel)
    valid=[e for e in state['pending'] if current(e,state,now_ms(),cfg)]
    if channel=='github_issue' and valid:
        url,headers,user=oldrun.settings()
        body=('@'+user+'\n\n' if user else '')+'Coin Tarama 5 V2 — geri test sonrası teyit\n\n'+'\n\n---\n\n'.join(describe(e) for e in valid)
        body+='\n\nRapor: https://github.com/'+os.environ['GITHUB_REPOSITORY']+'/blob/'+cfg['state_branch']+'/report.md\n\n'+'\n'.join(marker(e) for e in valid)
        cloud.http_json(url,{'title':'Coin Tarama 5 V2 · '+', '.join(sorted({LABELS[e['phase']] for e in valid}))+' · '+cloud.time_label(now_ms()),'body':body},headers,label='GitHub Issues')
        for e in valid:delivered(state,e,now_ms())
    elif channel not in ('report','github_issue'):raise ValueError('Unsupported notification channel')
    state['pending']=[]

def render(state):
    cfg=model.config();active=[a for a in state['assets'].values() if a['phase'] in ('preparation','triggered')]
    lines=['# Coin Tarama 5 — V2','',
        'Kapalı 15dk: hazırlık → hacimli kırılım → düşük hacimli geri test → sonraki mumda güçlenme. Hazırlıklar sessiz izlenir; yalnız tetik ve daha önce bildirilmiş adayın iptal/süre olayı bildirilir. Emir gönderilmez.','',
        'Son tamamlanmış tarama: '+cloud.time_label(state.get('latest',{}).get('observed_ms',now_ms()))+' TR.','',
        'Her borsanın mevcut likit spot+perpetual evrenindeki en çok60 coin her döngüde incelenir; daha önceki 12li rotasyon kaldırıldı. Teknik adaylar borsa başına en çok12lik sessiz havuzda oran geçmişi biriktirir. Aktif tetik üst sınırı küresel5 farklı sembol.','',
        'Hedef döngü5dk; gerçek başlangıç aralıkları (veri erişimi anlamına gelmez): '+json.dumps(state.get('timing',{}),ensure_ascii=False),'',
        '| Coin | Borsa | Aşama | Son spot | Direnç | Geçersizlik | Hedef | Son gözlem TR |',
        '|---|---|---|---:|---:|---:|---:|---|']
    for a in active:
        phase=LABELS[a['phase']] if a['phase']=='triggered' else ('GERİ TEST' if a.get('retest_close_ms') else 'KIRILIM İZLEME' if a.get('break_close_ms') else 'SESSİZ HAZIRLIK')
        lines.append(f"| {a['symbol']} | {a['exchange']} | {phase} | {a['latest_price']:.8g} | {a['level']:.8g} | {a['invalid']:.8g} | {a.get('target','—')} | {cloud.time_label(a['last_observed_ms'])} |")
    lines+=['','## Eleme ve veri kapsamı','',json.dumps(state.get('latest',{}),ensure_ascii=False),'',json.dumps(state['venues'],ensure_ascii=False),'',
        'OI kontrat adedinde gerçek45–75dk bazına göre en az%3 artış ve aynı aralıkta vadeli fiyat -%0.5/+%6 zorunlu. Baz yoksa bilinmiyor. Short payı+2yüzde puan şartı destek puanıdır; zorunlu değildir. OKX ve Binance grupları ayrı kalır; eksik oran verisi short açıldığı/azaldığı sayılmaz. Negatif fonlama ek destektir.','',
        'BTC son kapalı1s EMA20 altında ve EMA20 son3s düşüyorsa yeni long teyidi yok. Coinin1s/4s yapısı ve BTC göreli güç kontrolleri korunur. RSI/SAR açıklayıcıdır.','',
        'Giriş kırılan seviyeden en çok0.5ATR uzaklıkta; stop geri test dibi-0.15ATR ile ilk taban geçersizliğinin yüksek olanı. Risk en çok%6. En az iki sağ/sol kapalı4s mumla doğrulanmış yukarı tepe gerekir; bilinmeyen direnç2R alan sayılmaz. %0.5 toplam maliyet varsayımı dahil en az2R alan aranır.','',
        '## Gerçek gözlem ölçümleri','',
        'İlk farklı sembolün ilk gerçek tetik fiyatı değişmez. Önceki V1 kayıtları previous_v1 içinde aynen arşivlenir; yeni başarı sayılmaz. Saat getirileri1/4/12/24, BTC farkı, MAE/MFE yanında stop/hedef sırası ve maliyet sonrası R tutulur. Bunlar varsayımsal fiyat yolu ölçümüdür, gerçekleşmiş emir/net kâr değildir.','',
        '| Coin | Borsa | İlk tetik TR | Referans | Short teyidi | 1s | 4s | 12s | 24s |',
        '|---|---|---|---:|---|---|---|---|---|']
    for c in state['measurements']['cases'].values():
        vals=[]
        for h in cfg['horizons_hours']:
            o=c['outcomes'].get(str(h),{});b=o.get('barriers',{})
            vals.append(b.get('status','bekliyor')+' / '+('—' if o.get('return_pct') is None else f"%{o['return_pct']:+.2f}"))
        lines.append(f"| {c['symbol']} | {c['exchange']} | {cloud.time_label(c['observed_ms'])} | {c['entry_price']:.8g} | {c['short_information']} | {' | '.join(vals)} |")
    lines+=['','Short teyitli alt küme aynı girişlerin içindedir; iki bağımsız başarı gibi toplanmaz. Unknown kaynaklar ayrıca sayılır. Bu gözlemsel karşılaştırma tek başına short filtresinin nedensel katkısını kanıtlamaz.','',
        'Aynı1dk mumunda stop ve hedef varsa sıra belirsizdir. Giriş dakikasının zaman sırası bilinmiyorsa veya ilk dokunuştan önce eksik mum varsa sonuç bilinmiyor. Fiyat boşluğunda stop için daha kötü açılış kullanılır; bu fill garantisi değildir.','',
        'Maliyet senaryoları toplam%0.2/%0.5/%1; R ve saat getirileri farklı ölçümlerdir. Gerçek komisyon/kayma/fonlama ölçülmüş sayılmaz.','',
        'Ölçüm durumu: '+json.dumps({k:v for k,v in state['measurements'].items() if k!='cases'},ensure_ascii=False),'']
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'report.md').write_text('\n'.join(lines),encoding='utf-8')
