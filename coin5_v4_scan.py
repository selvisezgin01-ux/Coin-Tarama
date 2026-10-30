"""Independent V4 market state, causal entries, entry-only trend notifications."""
import os,json,time,hashlib
from pathlib import Path
from copy import deepcopy
from collections import Counter
from concurrent.futures import ThreadPoolExecutor,as_completed
import github_scan as cloud
import coin5_scan as oldrun
import coin5_v3_sources as src
import coin5_v4_model as model
ROOT=Path(__file__).parent;OUT=ROOT/'cloud_output_coin5_v4';STATE=OUT/'state.json'
LABELS={'radar':'ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL','triggered':'GİRİŞ TEYİDİ','cancelled':'İPTAL','expired':'SÜRE DOLDU','trend_continuing':'🔵📈 TREND SÜRÜYOR / GÜÇLENİYOR','trend_weakening':'🟠⚠️ TREND ZAYIFLIYOR','trend_broken':'🔴🧱 TREND YAPISI BOZULDU'}
def now_ms():return int(time.time()*1000)
def configure():
    if os.environ.setdefault('SCANNER_STATE_BRANCH',model.config()['state_branch'])!=model.config()['state_branch']:raise ValueError('V4 state isolation required')
    cloud.ROOT=ROOT;cloud.OUT=OUT;cloud.STATE=STATE;cloud.fingerprint=model.fingerprint;cloud.new_state=model.new_state

def snapshot(client,excludes,cfg,state,group):
    catalog=client.get('catalog');categories={}
    if client.venue=='OKX':
        categories=dict(Counter(str(r.get('instCategory','unknown')) for r in catalog))
        # Official OKX asset category 1 is crypto; 3+ are tokenized traditional assets.
        # No X-prefix heuristic: XRP and XNO remain eligible crypto.
        catalog=[r for r in catalog if str(r.get('instCategory',''))=='1']
    meta=src.metadata(catalog,client.venue,client.kind,excludes)
    raw=client.get('tickers');stamp=now_ms();quotes={};excluded={};byid={m['contract']:m for m in meta.values()}
    if not isinstance(raw,list):raise ValueError('Invalid bulk tickers')
    active={a['key'] for a in state['assets'].values() if a['group']==group and a['phase'] in ('radar','triggered')}
    retained=0;liquid=0
    for item in raw:
        cid=item.get('symbol' if client.venue=='MEXC' else 'instId')
        if cid not in byid:continue
        try:
            q=src.ticker(item,byid[cid],client.venue,client.kind,stamp)
            reason='low_turnover' if q['volume24']<cfg['minimum_volume24'] else 'wide_spread' if q['spread_pct']>cfg['maximum_radar_spread_pct'] else None
            if reason:
                excluded[q['symbol']]=reason
                if q['key'] not in active:continue
                retained+=1
            else:liquid+=1
            quotes[q['key']]=q
        except ValueError as e:excluded[byid[cid]['symbol']]=str(e)
    return quotes,{'active_catalog':len(meta),'instrument_categories':categories,'valid_liquid_tickers':liquid,'active_quotes_retained_outside_discovery':retained,
        'excluded':excluded,'observed_ms':stamp}

def collect(venue,kind,state,cfg):
    group=venue+':'+kind;client=src.Public(venue,kind);errors=[];rows=[];counts=Counter();cache={k:v for k,v in state['cache'].items() if k.startswith(group+':')}
    sampling=json.loads((ROOT/'study_config.json').read_text())['sampling'];policy=json.loads((ROOT/'strength_v5_priority_config.json').read_text())
    excludes={'stable':sampling['stable_bases'],'plates':sampling['excluded_concept_plates'],'equity':policy['excluded_equity_bases']}
    quotes,coverage=snapshot(client,excludes,cfg,state,group)
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
        if q['price']<=radar.get('base_invalid',0):reasons.append('fresh_support_lost')
        if radar.get('breakout') and q['price']<radar['level']-.2*ctx['atr']:reasons.append('fresh_breakout_lost')
        decisions[key].update(fresh_book_reasons=list(reasons),fresh_quote_ms=q['observed_ms'],fresh_quote_price=q['price'])
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

def source_close(a,phase):
    return a.get('trend_event_close_ms') if phase.startswith('trend_') else a.get('trigger_bar_close_ms',a['radar']['bar_close_ms'])

def event_id(a,phase):
    return hashlib.sha256((a['id']+':'+phase+':'+str(a.get('entry_seq',0))+':'+str(source_close(a,phase))).encode()).hexdigest()[:24]

def enqueue(state,a,phase,row,stamp):
    uid=event_id(a,phase)
    if any(e['id']==uid for e in state['pending']+state['delivery']+state['suppressed']):return
    state['pending'].append({'id':uid,'asset_id':a['id'],'key':a['key'],'symbol':a['symbol'],'exchange':a['exchange'],
        'kind':a['kind'],'phase':phase,'observed_ms':stamp,'price':row['quote']['price'],'level':a['level'],
        'invalid':a['invalid'],'target':a.get('target'),'radar':deepcopy(a['radar']),'context':deepcopy(row['context']),
        'entry_plan':deepcopy(a.get('entry_plan')),'reason':a.get('reason'),'source_close_ms':source_close(a,phase),
        'entry_route':a.get('entry_route'),'entry_seq':a.get('entry_seq',0),'cohort':a['symbol'],
        'trend_detail':deepcopy(a.get('trend_detail')),'was_triggered':any(d['asset_id']==a['id'] and d['phase']=='triggered' for d in state['delivery'])})

def register(state,a,phase,row,stamp):
    key=a['id']+':'+phase+(':'+str(a.get('entry_seq',0)) if phase=='triggered' else '')
    if key in state['measurements']['cases']:return
    btc=row.get('btc_quote')
    state['measurements']['cases'][key]={'symbol':a['symbol'],'exchange':a['exchange'],'kind':a['kind'],'key':a['key'],
        'phase':phase,'asset_id':a['id'],'contract':row['quote']['contract'],'observed_ms':stamp,'entry_price':row['quote']['price'],
        'btc_entry_price':btc['price'] if btc else None,'stop':a['invalid'] if phase=='triggered' else None,
        'target':a.get('target'),'risk_pct':a.get('risk_pct'),'outcomes':{},'source_close_ms':source_close(a,phase),
        'entry_route':a.get('entry_route') if phase=='triggered' else None,'entry_seq':a.get('entry_seq',0),'cohort':a['symbol'],
        'observation_lag_ms':stamp-source_close(a,phase),
        'interpretation':'early radar reference, not a trade entry' if phase=='radar' else 'hypothetical confirmed entry, not an order fill'}

def apply_records(state,results,cfg,stamp):
    rows=[r for result in results.values() for r in result['rows'] if 0<=stamp-r['quote']['observed_ms']<=120000]
    lookup={r['key']:r for r in rows};triggered={a['symbol'] for a in state['assets'].values() if a['phase']=='triggered'}
    for a in list(state['assets'].values()):
        if a['phase'] not in ('radar','triggered'):continue
        row=lookup.get(a['key'])
        if row is None:
            deadline=a.get('first_triggered_ms',a['created_ms'])+(cfg['trigger_watch_hours'] if a['phase']=='triggered' else cfg['setup_hours'])*3600000
            if stamp>=deadline:
                a.update(phase='expired',reason='süre doldu; güncel fiyat bilinmiyor')
                state['last_closed'][a['key']]={'observed_ms':stamp,'source_close_ms':a.get('last_evaluated_close_ms',a['radar']['bar_close_ms'])}
            continue
        a.update(latest_price=row['quote']['price'],last_observed_ms=row['quote']['observed_ms'])
        triggered={x['symbol'] for x in state['assets'].values() if x['phase']=='triggered'}
        evalrow=deepcopy(row)
        if a['symbol'] not in triggered and len(triggered)>=cfg['maximum_triggered']:evalrow['book_reasons'].append('active_entry_limit')
        phase=model.transition(a,evalrow,row['quote']['observed_ms'],cfg)
        if phase:
            enqueue(state,a,phase,row,row['quote']['observed_ms'])
            if phase=='triggered':triggered.add(a['symbol']);register(state,a,phase,row,row['quote']['observed_ms'])
            else:state['last_closed'][a['key']]={'observed_ms':row['quote']['observed_ms'],'source_close_ms':a.get('last_evaluated_close_ms',a['radar']['bar_close_ms'])}
        if any(d['asset_id']==a['id'] and d['phase']=='triggered' for d in state['delivery']):
            trend=model.trend_event(a,row,row['quote']['observed_ms'],cfg)
            if trend:enqueue(state,a,trend,row,row['quote']['observed_ms'])
    active={a['key'] for a in state['assets'].values() if a['phase'] in ('radar','triggered')}
    active_symbols={a['symbol'] for a in state['assets'].values() if a['phase'] in ('radar','triggered')}
    ranked=sorted([r for r in rows if r['radar']['valid'] and not r['book_reasons']],
        key=lambda r:(-r['radar']['score'],r['quote']['spread_pct'],r['key']))
    recent={e['symbol'] for e in state['radar_admissions'] if 0<=stamp-e['observed_ms']<3600000}
    new_symbols=set();added=[];rejections={}
    for r in ranked:
        key=r['key'];q=r['quote'];p=r['radar'];sym=r['symbol'];why=None
        if q['price']<=p['base_invalid'] or q['price']<r['series']['15m'][-1]['c']-.5*p['atr'] or (p['breakout'] and q['price']<p['level']-.2*p['atr']):why='live_quote_lost_setup'
        elif key in active:why='market_already_active'
        elif len(active)>=cfg['maximum_active_markets']:why='active_market_limit'
        elif sym not in active_symbols and len(active_symbols)>=cfg['maximum_active_assets']:why='active_symbol_limit'
        elif sym not in recent and sym not in new_symbols and len(new_symbols)>=cfg['maximum_new_symbols_per_cycle']:why='cycle_symbol_budget'
        elif sym not in recent and len(recent)>=cfg['maximum_radar_symbols_per_hour']:why='hourly_symbol_budget'
        elif p['bar_close_ms'] in state['prior_signal_bars'].get(key,[]):why='archived_signal_bar'
        elif any(a['key']==key and a['radar']['bar_close_ms']==p['bar_close_ms'] for a in state['assets'].values()):why='same_signal_bar'
        else:why=model.rearm_reason(state,r,stamp,cfg)
        if why:rejections[key]=why;continue
        uid=hashlib.sha256((key+':'+str(p['bar_close_ms'])).encode()).hexdigest()[:24]
        a={'id':uid,'key':key,'group':r['group'],'symbol':sym,'exchange':r['exchange'],'kind':r['kind'],'contract':q['contract'],
            'phase':'radar','created_ms':q['observed_ms'],'level':p['level'],'base_invalid':p['base_invalid'],'invalid':p['base_invalid'],
            'atr':p['atr'],'initial_price':q['price'],'latest_price':q['price'],'last_observed_ms':q['observed_ms'],'radar':deepcopy(p)}
        if p['breakout']:a.update(break_close_ms=p['bar_close_ms'],break_volume=r['series']['15m'][-1]['v'])
        state['assets'][uid]=a;active.add(key);active_symbols.add(sym);added.append(key)
        if sym not in recent:
            state['radar_admissions'].append({'symbol':sym,'observed_ms':stamp});recent.add(sym);new_symbols.add(sym)
        # All markets are tracked; only repeated early notifications are suppressed.
        sent=any(e.get('symbol')==sym and e['phase']=='radar' and 0<=stamp-e['observed_ms']<3600000 for e in state['delivery'])
        if sent:state['suppressed'].append({'id':event_id(a,'radar'),'asset_id':uid,'phase':'radar','observed_ms':stamp,'reason':'same_symbol_radar_already_notified','symbol':sym})
        else:enqueue(state,a,'radar',r,q['observed_ms'])
        register(state,a,'radar',r,q['observed_ms'])
    state['registration_decisions']={'observed_ms':stamp,'rejected':rejections,'added_markets':added}
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

def marker(e):return '<!-- coin-tarama-5-v4:'+e['id']+' -->'
def delivered(state,e,stamp):
    if not any(x['id']==e['id'] for x in state['delivery']):
        state['delivery'].append({k:e.get(k) for k in ('id','asset_id','key','symbol','phase','observed_ms','entry_seq','entry_route')}|{'delivered_ms':stamp})
    for c in state['measurements']['cases'].values():
        if c['asset_id']==e['asset_id'] and c['phase']==e['phase'] and c.get('entry_seq',0)==e.get('entry_seq',0):c['notification_lag_ms']=stamp-e['observed_ms']

def reconcile(state,channel):
    if channel!='github_issue' or not state['pending']:return
    url,headers,_=oldrun.settings();issues=cloud.http_json(url+'?state=all&sort=created&direction=desc&per_page=100',headers=headers,label='GitHub Issues')
    for e in list(state['pending']):
        if any(marker(e) in (i.get('body') or '') and i.get('user',{}).get('login')=='github-actions[bot]' for i in issues):delivered(state,e,now_ms());state['pending'].remove(e)
def describe(e):
    r=e['radar'];ctx=e['context'];label=LABELS[e['phase']]
    if e['phase']=='cancelled' and e.get('was_triggered'):label='🔴🧱 YAPI BOZULDU — GİRİŞ GEÇERSİZLİĞİ'
    lines=[f"**{label} · {e['symbol']} · {e['exchange']} {e['kind']}**",
        f"Gerçek gözlem: {cloud.time_label(e['observed_ms'])} TR · fiyat {e['price']:.8g}",
        f"Kapalı15dk hacim {r['rvol']:.2f}x · {r['kind']} · kırılım seviyesi {e['level']:.8g}",
        f"Kaynak kapanışı: {cloud.time_label(e['source_close_ms'])} TR · gözlem gecikmesi {(e['observed_ms']-e['source_close_ms'])/60000:.1f}dk"]
    if e['phase']=='radar':lines+=['**Erken izleme uyarısıdır. Geri test ve giriş teyidi henüz yok.**']
    if e['phase']=='triggered' and e.get('entry_plan'):
        p=e['entry_plan'];lines+=[f"Giriş izleme bölgesi {p['entry_zone_low']:.8g}–{p['entry_zone_high']:.8g}; geçersizlik {p['stop']:.8g}; varsayımsal hedef {p['target']:.8g}; risk mesafesi %{p['risk_pct']:.2f}.",
            'Hedef alanı: '+('gözlenen direnç hedefin üzerinde' if p['resistance'] else 'direnç bilinmiyor; hedef yalnız maliyet dahil2R projeksiyonudur')]
    if e['phase']=='triggered':lines+=['Giriş türü: '+('yukarıda yeni taban kırılımı' if e.get('entry_route')=='continuation' else 'kırılan seviyede geri test ve güçlenme')+' · giriş sıra no '+str(e.get('entry_seq',1))+'. Aynı coin içindeki ilişkili girişlerdir.']
    if e['phase'].startswith('trend_'):
        lines+=['**Bu bir trend durum güncellemesidir; yeni giriş teyidi değildir.**',json.dumps(e.get('trend_detail'),ensure_ascii=False)]
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
        if not a or not 0<=now_ms()-e['observed_ms']<=cfg['notification_age_ms']:continue
        if e['phase'].startswith('trend_'):
            if a['phase']!='triggered' or not a.get('entry_history'):continue
        elif a['phase']!=e['phase']:continue
        if e['phase'] in ('cancelled','expired') and not any(x['asset_id']==a['id'] for x in state['delivery']):continue
        valid.append(e)
    if channel=='github_issue' and valid:
        url,headers,user=oldrun.settings();body=('@'+user+'\n\n' if user else '')+'Coin Tarama5 V4\n\n'+'\n\n---\n\n'.join(describe(e) for e in valid)
        body+='\n\nRapor: https://github.com/'+os.environ['GITHUB_REPOSITORY']+'/blob/'+cfg['state_branch']+'/report.md\n\n'+'\n'.join(marker(e) for e in valid)
        cloud.http_json(url,{'title':'Coin Tarama5 V4 · '+', '.join(sorted({LABELS[e['phase']] for e in valid}))+' · '+cloud.time_label(now_ms()),'body':body},headers,label='GitHub Issues')
        for e in valid:delivered(state,e,now_ms())
    elif channel not in ('github_issue','report'):raise ValueError('Unsupported channel')
    state['pending']=[]

def render(state):
    lines=['# Coin Tarama5 — V4','',
        'Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.','',
        'Son gözlem: '+cloud.time_label(state.get('latest',{}).get('observed_ms',now_ms()))+' TR.','',
        'Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.','',
        'Hedef5dk, gerçek başlangıç aralıkları: '+json.dumps(state.get('timing',{}),ensure_ascii=False),'',
        '## Aktif izleme','',
        '| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |',
        '|---|---|---|---|---:|---:|---:|']
    for a in state['assets'].values():
        if a['phase'] in ('radar','triggered'):lines.append(f"| {a['symbol']} | {a['exchange']} {a['kind']} | {('🟢🎯 '+LABELS[a['phase']] if a['phase']=='triggered' else LABELS[a['phase']])} | {cloud.time_label(a['created_ms'])} | {a['latest_price']:.8g} | {a['level']:.8g} | {a['invalid']:.8g} |")
    lines+=['','## Kapsam ve eleme','',json.dumps(state.get('latest',{}),ensure_ascii=False)]
    for group,c in state['venues'].items():lines+=['',group+': '+json.dumps({k:v for k,v in c.items() if k not in ('eligible_keys','selected_keys','excluded','decisions')},ensure_ascii=False)]
    lines+=['','Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni sembol/döngü,6yeni sembol/saat,20aktif sembol/80pazar sınırı vardır. Aynı sembol her borsada kendi fiyatıyla izlenir; yalnız tekrar eden erken bildirimler bastırılır; kota dışı fırsatlar kaçabilir.','',
        '## İlk gerçek gözlem ölçümleri','',
        'Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Her pazar/evre/giriş türünün gerçek referansı korunur; aynı sembol ve tekrar girişler bağımsız örnek sayılmaz; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V3 kayıtları değişmeyen arşiv commitinde korunur; eski ölçümler ayrı legacy_v3 alanında sürer.','',
        '| Coin | Pazar | Evre / giriş türü | Gözlem TR | Referans | 1s | 4s | 12s | 24s |',
        '|---|---|---|---|---:|---|---|---|---|']
    for c in state['measurements']['cases'].values():
        vals=['—' if c['outcomes'].get(str(h),{}).get('return_pct') is None else f"%{c['outcomes'][str(h)]['return_pct']:+.2f}" for h in model.config()['horizons_hours']]
        lines.append(f"| {c['symbol']} | {c['exchange']} {c['kind']} | {c['phase']} / {c.get('entry_route') or 'radar'} #{c.get('entry_seq',0)} | {cloud.time_label(c['observed_ms'])} | {c['entry_price']:.8g} | {' | '.join(vals)} |")
    lines+=['','Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.','',
        '1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.','',
        'Ölçüm: '+json.dumps({k:v for k,v in state['measurements'].items() if k!='cases'},ensure_ascii=False),'']
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'report.md').write_text('\n'.join(lines),encoding='utf-8')
