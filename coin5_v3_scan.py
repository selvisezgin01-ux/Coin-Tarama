"""Independent V3 state and notifications; all public tickers, bounded dynamic candles."""
import os,json,time,hashlib
from pathlib import Path
from copy import deepcopy
from collections import Counter
from concurrent.futures import ThreadPoolExecutor,as_completed
import github_scan as cloud
import coin5_scan as oldrun
import coin5_v3_sources as src
import coin5_v3_model as model
ROOT=Path(__file__).parent;OUT=ROOT/'cloud_output_coin5_v3';STATE=OUT/'state.json'
LABELS={'radar':'ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL','triggered':'GERİ TEST — GİRİŞ TEYİDİ','cancelled':'İPTAL','expired':'SÜRE DOLDU'}
def now_ms():return int(time.time()*1000)
def configure():
    if os.environ.setdefault('SCANNER_STATE_BRANCH',model.config()['state_branch'])!=model.config()['state_branch']:raise ValueError('V3 state isolation required')
    cloud.ROOT=ROOT;cloud.OUT=OUT;cloud.STATE=STATE;cloud.fingerprint=model.fingerprint;cloud.new_state=model.new_state

def collect(venue,kind,state,cfg):
    group=venue+':'+kind;client=src.Public(venue,kind);errors=[];rows=[];counts=Counter();cache={k:v for k,v in state['cache'].items() if k.startswith(group+':')}
    sampling=json.loads((ROOT/'study_config.json').read_text())['sampling'];policy=json.loads((ROOT/'strength_v5_priority_config.json').read_text())
    excludes={'stable':sampling['stable_bases'],'plates':sampling['excluded_concept_plates'],'equity':policy['excluded_equity_bases']}
    quotes,coverage=src.snapshot(client,excludes,cfg)
    local={**state,'cursor':state['cursor'].copy()};selected=model.select(quotes,local,group,cfg,now_ms())
    staged=[];started=time.monotonic();btc_bars=None;decisions={}
    btc=next((q for q in quotes.values() if q['symbol']=='BTCUSDT'),None)
    if btc:
        try:btc_bars=src.bars(client,btc,'1h',now_ms(),64,cache)
        except Exception as e:errors.append('BTC context: '+str(e))
    active={a['key'] for a in state['assets'].values() if a['phase'] in ('radar','triggered')}
    for key in selected:
        if client.blocked:break
        if time.monotonic()-started>cfg['maximum_chart_seconds']:
            errors.append('candle_time_budget: remaining symbols unknown');break
        q=quotes[key]
        try:
            bs=src.bars(client,q,'15m',now_ms(),cfg['history_bars'],cache);r=model.radar(bs,cfg);counts['candles_evaluated']+=1
            decisions[key]={**r,'ticker_observed_ms':q['observed_ms'],'priority':model.priority(q,state['quote_history'].get(key,[]),q['observed_ms'])}
            counts.update(r['reasons'])
            if not r['valid'] and key not in active:continue
            series={'15m':bs}
            for interval in ('1h','4h'):
                try:series[interval]=src.bars(client,q,interval,now_ms(),64,cache)
                except Exception as e:errors.append(q['symbol']+' '+interval+' optional context: '+str(e))
            ctx=model.context(series,btc_bars)
            if btc_bars:ctx['btc_hour_pct']=(btc_bars[-1]['c']/btc_bars[-2]['c']-1)*100
            staged.append((key,series,r,ctx))
        except Exception as e:errors.append(q['symbol']+': '+str(e));decisions[key]={'status':'read_error','reason':str(e)}
    # Refresh bulk quotes after chart reads. No old candle close becomes a live price.
    latest={};stamp=now_ms()
    try:
        raw=client.get('tickers');stamp=now_ms();byid={q['contract']:q for q in quotes.values()}
        for item in raw:
            cid=item.get('symbol' if venue=='MEXC' else 'instId')
            if cid in byid:
                try:
                    q=src.ticker(item,byid[cid],venue,kind,stamp);latest[q['key']]=q
                except ValueError:pass
    except Exception as e:errors.append('fresh quotes: '+str(e))
    btc_quote=next((q for q in latest.values() if q['symbol']=='BTCUSDT'),None)
    for key,series,radar,ctx in staged:
        q=latest.get(key)
        if not q:counts['fresh_quote_unknown']+=1;continue
        reasons=[]
        if q['spread_pct']>cfg['maximum_radar_spread_pct'] or q['volume24']<cfg['minimum_volume24']:reasons.append('fresh_liquidity_failed')
        if series['15m'][-1]['t']+900000!=q['observed_ms']//900000*900000:reasons.append('closed_15m_stale')
        if q['price']-series['15m'][-1]['c']>model.core.atr(series['15m']):reasons.append('fresh_price_outran_signal')
        if series['15m'][-1]['c']-q['price']>.5*ctx['atr']:reasons.append('fresh_pullback_advanced')
        if q['price']<=radar['base_invalid']:reasons.append('fresh_support_lost')
        if radar['breakout'] and q['price']<radar['level']-.2*ctx['atr']:reasons.append('fresh_breakout_lost')
        ctx['oi_support']=model.oi_support(q,state['oi_history'].get(key,[]))
        ctx['funding_raw_pct']=q['funding_raw']*100 if q.get('funding_raw') is not None else None
        ctx['funding_note']='raw indicative rate; interval/scaling unknown, not a paid funding amount'
        rows.append({'key':key,'group':group,'symbol':q['symbol'],'exchange':venue,'kind':kind,'quote':q,'series':series,
            'radar':radar,'context':ctx,'btc_quote':btc_quote,'book_reasons':reasons,
            'priority':model.priority(q,state['quote_history'].get(key,[]),q['observed_ms'])})
    keep=set(quotes)|{a['key'] for a in state['assets'].values() if a['group']==group and a['phase'] in ('radar','triggered')}
    for key in selected:
        if key not in decisions:decisions[key]={'status':'not_observed_budget_or_access'}
    coverage.update(selected_for_candles=len(selected),candles_evaluated=counts['candles_evaluated'],fresh_candidate_quotes=len(rows),
        selected_keys=selected,eligible_keys=sorted(quotes),decisions=decisions,funnel=dict(counts),calls=client.calls,errors=errors)
    return {'rows':rows,'quotes':quotes,'cache':{k:v for k,v in cache.items() if ':'.join(k.split(':')[:3]) in keep},
        'coverage':coverage,'cursor':local['cursor'].get(group,0)}

def enqueue(state,a,phase,row,stamp):
    uid=hashlib.sha256((a['id']+':'+phase).encode()).hexdigest()[:24]
    if any(e['id']==uid for e in state['pending']+state['delivery']):return
    state['pending'].append({'id':uid,'asset_id':a['id'],'key':a['key'],'symbol':a['symbol'],'exchange':a['exchange'],
        'kind':a['kind'],'phase':phase,'observed_ms':stamp,'price':row['quote']['price'],'level':a['level'],
        'invalid':a['invalid'],'target':a.get('target'),'radar':a['radar'],'context':row['context'],
        'entry_plan':a.get('entry_plan'),'reason':a.get('reason'),'source_close_ms':a.get('trigger_bar_close_ms',a['radar']['bar_close_ms'])})

def register(state,a,phase,row,stamp):
    key=a['symbol']+':'+phase
    if key in state['measurements']['cases']:return
    btc=row.get('btc_quote')
    state['measurements']['cases'][key]={'symbol':a['symbol'],'exchange':a['exchange'],'kind':a['kind'],'key':a['key'],
        'phase':phase,'asset_id':a['id'],'contract':row['quote']['contract'],'observed_ms':stamp,'entry_price':row['quote']['price'],
        'btc_entry_price':btc['price'] if btc else None,'stop':a['invalid'] if phase=='triggered' else None,
        'target':a.get('target'),'risk_pct':a.get('risk_pct'),'outcomes':{},'source_close_ms':a.get('trigger_bar_close_ms',a['radar']['bar_close_ms']),
        'observation_lag_ms':stamp-a.get('trigger_bar_close_ms',a['radar']['bar_close_ms']),
        'interpretation':'early radar reference, not a trade entry' if phase=='radar' else 'hypothetical confirmed entry, not an order fill'}

def apply_records(state,results,cfg,stamp):
    rows=[r for result in results.values() for r in result['rows'] if 0<=stamp-r['quote']['observed_ms']<=120000]
    lookup={r['key']:r for r in rows};triggered={a['symbol'] for a in state['assets'].values() if a['phase']=='triggered'}
    for a in state['assets'].values():
        if a['phase'] not in ('radar','triggered'):continue
        row=lookup.get(a['key'])
        if row is None:
            if stamp>=a.get('triggered_ms',a['created_ms'])+(cfg['trigger_watch_hours'] if a['phase']=='triggered' else cfg['setup_hours'])*3600000:
                a.update(phase='expired',reason='süre doldu; güncel fiyat bilinmiyor');state['last_closed'][a['key']]=stamp
            continue
        a.update(latest_price=row['quote']['price'],last_observed_ms=row['quote']['observed_ms'])
        evalrow=deepcopy(row)
        if len(triggered)>=cfg['maximum_triggered']:evalrow['book_reasons'].append('active_entry_limit')
        phase=model.transition(a,evalrow,row['quote']['observed_ms'],cfg)
        if phase:
            enqueue(state,a,phase,row,row['quote']['observed_ms'])
            if phase=='triggered':triggered.add(a['symbol']);register(state,a,phase,row,row['quote']['observed_ms'])
            else:triggered.discard(a['symbol']);state['last_closed'][a['key']]=row['quote']['observed_ms']
    active={a['key'] for a in state['assets'].values() if a['phase'] in ('radar','triggered')}
    ranked=sorted([r for r in rows if r['radar']['valid'] and not r['book_reasons']],
        key=lambda r:(-r['radar']['score'],r['quote']['spread_pct'],r['key']))
    added=[];new_symbols=set()
    sent_recent=sum(e['phase']=='radar' and 0<=stamp-e['observed_ms']<3600000 for e in state['delivery'])
    available=max(0,min(cfg['maximum_new_radars_per_cycle'],cfg['maximum_radars_per_hour']-sent_recent))
    for r in ranked:
        key=r['key'];q=r['quote'];p=r['radar']
        if q['price']<=p['base_invalid'] or q['price']<r['series']['15m'][-1]['c']-.5*p['atr'] or (p['breakout'] and q['price']<p['level']-.2*p['atr']):continue
        if key in active or r['symbol'] in new_symbols or any(a['symbol']==r['symbol'] and a['phase'] in ('radar','triggered') for a in state['assets'].values()) or len(active)>=cfg['maximum_active_assets'] or len(added)>=available:continue
        if stamp-state['last_closed'].get(key,0)<cfg['cooldown_hours']*3600000:continue
        # Repeated recognition of the same old candle never makes a new event.
        if any(a['key']==key and a['radar']['bar_close_ms']==p['bar_close_ms'] for a in state['assets'].values()):continue
        uid=hashlib.sha256((key+':'+str(p['bar_close_ms'])).encode()).hexdigest()[:24]
        a={'id':uid,'key':key,'group':r['group'],'symbol':r['symbol'],'exchange':r['exchange'],'kind':r['kind'],'contract':q['contract'],'phase':'radar',
            'created_ms':q['observed_ms'],'level':p['level'],'base_invalid':p['base_invalid'],'invalid':p['base_invalid'],
            'atr':p['atr'],'initial_price':q['price'],'latest_price':q['price'],'last_observed_ms':q['observed_ms'],'radar':p}
        if p['breakout']:a.update(break_close_ms=p['bar_close_ms'],break_volume=r['series']['15m'][-1]['v'])
        state['assets'][uid]=a;active.add(key);new_symbols.add(a['symbol']);added.append(key)
        enqueue(state,a,'radar',r,q['observed_ms']);register(state,a,'radar',r,q['observed_ms'])
    return added

def observe(state,cfg):
    results={}
    with ThreadPoolExecutor(max_workers=4) as pool:
        jobs={pool.submit(collect,v,k,state,cfg):v+':'+k for v in ('MEXC','OKX') for k in ('SPOT','PERP')}
        for j in as_completed(jobs):
            group=jobs[j]
            try:results[group]=j.result()
            except Exception as e:results[group]={'rows':[],'quotes':{},'cache':{},'coverage':{'errors':[str(e)]},'cursor':state['cursor'].get(group,0)}
    for group,r in results.items():
        state['venues'][group]=r['coverage'];state['cursor'][group]=r['cursor']
        state['cache']={**{k:v for k,v in state['cache'].items() if not k.startswith(group+':')},**r['cache']}
        model.remember_quotes(state,r['quotes'],now_ms())
        for key,q in r['quotes'].items():
            if q['kind']!='PERP' or q.get('oi_contracts') is None:continue
            hist=state['oi_history'].setdefault(key,[])
            if not any(p['provider_ms']==q['provider_ms'] for p in hist):hist.append({k:q.get(k) for k in ('provider_ms','oi_contracts','contract','contract_size')})
            state['oi_history'][key]=[p for p in hist if 0<=now_ms()-p['provider_ms']<=14400000][-60:]
    stamp=now_ms();new=apply_records(state,results,cfg,stamp)
    state['latest']={'observed_ms':stamp,'new_radars':new,'liquid_tickers':sum(len(r['quotes']) for r in results.values()),
        'candles_evaluated':sum(r['coverage'].get('candles_evaluated',0) for r in results.values()),
        'errors':{g:r['coverage'].get('errors',[]) for g,r in results.items()},'failed_groups':[g for g,r in results.items() if not r['quotes']]}

def marker(e):return '<!-- coin-tarama-5-v3:'+e['id']+' -->'
def delivered(state,e,stamp):
    if not any(x['id']==e['id'] for x in state['delivery']):state['delivery'].append({'id':e['id'],'asset_id':e['asset_id'],'phase':e['phase'],'observed_ms':e['observed_ms'],'delivered_ms':stamp})
    c=state['measurements']['cases'].get(e['symbol']+':'+e['phase'])
    if c and c['asset_id']==e['asset_id']:c['notification_lag_ms']=stamp-e['observed_ms']
def reconcile(state,channel):
    if channel!='github_issue' or not state['pending']:return
    url,headers,_=oldrun.settings();issues=cloud.http_json(url+'?state=all&sort=created&direction=desc&per_page=100',headers=headers,label='GitHub Issues')
    for e in list(state['pending']):
        if any(marker(e) in (i.get('body') or '') and i.get('user',{}).get('login')=='github-actions[bot]' for i in issues):delivered(state,e,now_ms());state['pending'].remove(e)
def describe(e):
    r=e['radar'];ctx=e['context'];lines=[f"**{LABELS[e['phase']]} · {e['symbol']} · {e['exchange']} {e['kind']}**",
        f"Gerçek gözlem: {cloud.time_label(e['observed_ms'])} TR · fiyat {e['price']:.8g}",
        f"Kapalı15dk hacim {r['rvol']:.2f}x · {r['kind']} · kırılım seviyesi {e['level']:.8g}",
        f"Kaynak kapanışı: {cloud.time_label(e['source_close_ms'])} TR · gözlem gecikmesi {(e['observed_ms']-e['source_close_ms'])/60000:.1f}dk"]
    if e['phase']=='radar':lines+=['**Erken izleme uyarısıdır. Geri test ve giriş teyidi henüz yok.**']
    if e.get('entry_plan'):
        p=e['entry_plan'];lines+=[f"Giriş izleme bölgesi {p['entry_zone_low']:.8g}–{p['entry_zone_high']:.8g}; geçersizlik {p['stop']:.8g}; varsayımsal hedef {p['target']:.8g}; risk mesafesi %{p['risk_pct']:.2f}.",
            'Hedef alanı: '+('gözlenen direnç hedefin üzerinde' if p['resistance'] else 'direnç bilinmiyor; hedef yalnız maliyet dahil2R projeksiyonudur')]
    if ctx.get('support_warnings'):lines+=['Destek verileri: '+', '.join(ctx['support_warnings'])]
    oi=ctx.get('oi_support',{})
    lines+=['OI desteği: '+(f"%{oi['change_pct']:+.2f}" if oi.get('status')=='observed' else 'bilinmiyor / uygulanamaz / geçmiş birikiyor')+'; yeni short açılışı kanıtı değildir.']
    if e.get('reason'):lines+=['Neden: '+e['reason']]
    lines+=['Spot ve vadeli fiyatları ayrı pazarlardır. Hacim artışı gerçek net alıcı/bağımsız balina girişi kanıtı değildir. Bu deney emir göndermez, kâr veya gerçekleşme garantisi vermez.']
    return '\n\n'.join(lines)
def notify(state,channel,cfg):
    reconcile(state,channel);valid=[]
    for e in state['pending']:
        a=state['assets'].get(e['asset_id'])
        if not a or a['phase']!=e['phase'] or not 0<=now_ms()-e['observed_ms']<=cfg['notification_age_ms']:continue
        if e['phase'] in ('cancelled','expired') and not any(x['asset_id']==a['id'] for x in state['delivery']):continue
        valid.append(e)
    if channel=='github_issue' and valid:
        url,headers,user=oldrun.settings();body=('@'+user+'\n\n' if user else '')+'Coin Tarama5 V3\n\n'+'\n\n---\n\n'.join(describe(e) for e in valid)
        body+='\n\nRapor: https://github.com/'+os.environ['GITHUB_REPOSITORY']+'/blob/'+cfg['state_branch']+'/report.md\n\n'+'\n'.join(marker(e) for e in valid)
        cloud.http_json(url,{'title':'Coin Tarama5 V3 · '+', '.join(sorted({LABELS[e['phase']] for e in valid}))+' · '+cloud.time_label(now_ms()),'body':body},headers,label='GitHub Issues')
        for e in valid:delivered(state,e,now_ms())
    elif channel not in ('github_issue','report'):raise ValueError('Unsupported channel')
    state['pending']=[]

def render(state):
    lines=['# Coin Tarama5 — V3','',
        'Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.','',
        'Son gözlem: '+cloud.time_label(state.get('latest',{}).get('observed_ms',now_ms()))+' TR.','',
        'Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.','',
        'Hedef5dk, gerçek başlangıç aralıkları: '+json.dumps(state.get('timing',{}),ensure_ascii=False),'',
        '## Aktif izleme','',
        '| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |',
        '|---|---|---|---|---:|---:|---:|']
    for a in state['assets'].values():
        if a['phase'] in ('radar','triggered'):lines.append(f"| {a['symbol']} | {a['exchange']} {a['kind']} | {LABELS[a['phase']]} | {cloud.time_label(a['created_ms'])} | {a['latest_price']:.8g} | {a['level']:.8g} | {a['invalid']:.8g} |")
    lines+=['','## Kapsam ve eleme','',json.dumps(state.get('latest',{}),ensure_ascii=False)]
    for group,c in state['venues'].items():lines+=['',group+': '+json.dumps({k:v for k,v in c.items() if k not in ('eligible_keys','selected_keys','excluded','decisions')},ensure_ascii=False)]
    lines+=['','Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni radar/döngü,6radar/saat ve20aktif izleme sınırı vardır; kota dışı fırsatlar kaçabilir.','',
        '## İlk gerçek gözlem ölçümleri','',
        'Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Aynı sembolün ilk evre referansı korunur; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V2 kayıtları değişmeyen arşiv commitinde korunur.','',
        '| Coin | Pazar | Evre | Gözlem TR | Referans | 1s | 4s | 12s | 24s |',
        '|---|---|---|---|---:|---|---|---|---|']
    for c in state['measurements']['cases'].values():
        vals=['—' if c['outcomes'].get(str(h),{}).get('return_pct') is None else f"%{c['outcomes'][str(h)]['return_pct']:+.2f}" for h in model.config()['horizons_hours']]
        lines.append(f"| {c['symbol']} | {c['exchange']} {c['kind']} | {c['phase']} | {cloud.time_label(c['observed_ms'])} | {c['entry_price']:.8g} | {' | '.join(vals)} |")
    lines+=['','Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.','',
        '1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.','',
        'Ölçüm: '+json.dumps({k:v for k,v in state['measurements'].items() if k!='cases'},ensure_ascii=False),'']
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'report.md').write_text('\n'.join(lines),encoding='utf-8')
