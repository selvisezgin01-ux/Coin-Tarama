"""Coin Tarama Meme: independent DEX discovery, closed 15m patterns and evidence gates."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import re
import time
from urllib.parse import urlencode

import github_scan as cloud
import meme_rules as rules
import meme_security as security_api
import meme_sources as source
from research import LOCAL

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'cloud_output_meme'
STATE=OUT/'state.json'


def fingerprint():
    digest=hashlib.sha256()
    for name in ['meme_config.json','meme_scan.py','meme_rules.py','meme_sources.py','meme_security.py']:
        digest.update(name.encode());digest.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return digest.hexdigest()


def new_state():
    return {'version':'meme-v3','rules_fingerprint':fingerprint(),'assets':{},'entries':{},'pending':[],'runs':[]}


def configure():
    branch=os.environ.setdefault('SCANNER_STATE_BRANCH','scanner-state-meme-v3')
    if not branch.startswith('scanner-state-meme'):raise ValueError('Meme scanner must use its own state branch')
    cloud.OUT=OUT;cloud.STATE=STATE;cloud.fingerprint=fingerprint;cloud.new_state=new_state


def now_ms():return int(time.time()*1000)
def key_of(asset):return asset['chain']+':'+rules.address_key(asset['chain'],asset['mint'])
def time_label(ms):return datetime.fromtimestamp(ms/1000,LOCAL).strftime('%d.%m.%Y %H:%M')
def safe_symbol(value):return re.sub(r'[^A-Za-z0-9_-]','',str(value))[:24] or 'TOKEN'


def bubble_link(asset):
    chain={'solana':'solana','ethereum':'eth','bnb':'bsc'}.get(asset['chain'])
    if chain:return 'https://v2.bubblemaps.io/map?'+urlencode({'chain':chain,'address':asset['mint']})
    return 'https://v2.bubblemaps.io/' # Do not invent a working map route for unverified networks.


def seed_from_v1(previous,branch,commit):
    if previous.get('version')!='meme-v1':raise ValueError('Migration only accepts the archived meme-v1 state')
    if previous.get('entries') or previous.get('pending'):
        raise ValueError('Existing observations/alerts require a separate measurement migration; refusing to reset them')
    state=new_state()
    for key,record in previous.get('assets',{}).items():
        state['assets'][key]={k:record[k] for k in ['latest','first_seen_ms','earliest_pool_created_ms','observations'] if k in record}
    state['migration']={'from_branch':branch,'from_commit':commit,'from_fingerprint':previous['rules_fingerprint'],
                        'source_updated_ms':previous.get('updated_ms'),'migrated_ms':now_ms(),
                        'reason':'User performs wallet-map review; strengthened public security checks. Historical setups are re-evaluated prospectively.'}
    return state


def pull_state():
    cloud.pull_state()
    if (OUT/'parent.txt').read_text(encoding='ascii').strip():return
    branch=os.environ.get('MEME_MIGRATE_FROM_BRANCH')
    if not branch:return
    if branch!='scanner-state-meme-v2':raise ValueError('Only the archived meme-v2 branch may seed this experiment')
    cloud.git('fetch','--no-tags','origin','refs/heads/'+branch)
    commit=cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
    previous=json.loads(cloud.git('show',commit+':state.json').stdout)
    cloud.save(STATE,seed_first_formation(previous,branch,commit))


def seed_first_formation(previous,branch,commit):
    if previous.get('version')!='meme-v2' or previous.get('rules_fingerprint')!='7cd0a36fdb87a00b75afb7ef6d96d24f11ccde772445318eee9380ecb6e0d80e':
        raise ValueError('Unexpected source experiment for first-formation migration')
    if previous.get('entries') or previous.get('pending'):
        raise ValueError('Source has observations/alerts; refusing to reset or mix its measured cohort')
    state=new_state()
    for key,record in previous.get('assets',{}).items():
        state['assets'][key]={k:record[k] for k in ['latest','first_seen_ms','earliest_pool_created_ms','observations'] if k in record}
    if 'social_watch' in previous:state['social_watch']=previous['social_watch']
    state['migration']={'from_branch':branch,'from_commit':commit,'from_fingerprint':previous['rules_fingerprint'],
                        'source_updated_ms':previous.get('updated_ms'),'migrated_ms':now_ms(),
                        'reason':'First formation only; full available launch history and wick/runup exclusions. Previous branch archived; no historical signals backfilled.'}
    return state


def pending_measurements(entry,config):
    return any(any(str(m) not in ref['outcomes'] for m in config['measurement']['horizons_minutes']) for ref in entry['references'].values())


def expire_missed_endpoints(state,config,asof):
    for entry in state['entries'].values():
        for ref in entry['references'].values():
            for minutes in config['measurement']['horizons_minutes']:
                target=ref['observed_ms']+minutes*60000
                if str(minutes) not in ref['outcomes'] and asof>target+config['measurement']['max_endpoint_observation_delay_minutes']*60000:
                    ref['outcomes'][str(minutes)]={'target_ms':target,'observed_ms':None,'delay_ms':None,
                        'return_pct':None,'status':'no_observation_within_target_window'}


def remember(state,asset,observed_ms,config):
    key=key_of(asset)
    old=state['assets'].get(key,{})
    earlier=[v for v in [old.get('earliest_pool_created_ms'),asset.get('pool_created_ms')] if v is not None]
    asset['observed_ms']=asset.get('price_observed_ms',observed_ms)
    observations=old.get('observations',[])
    observations.append({'ms':asset['observed_ms'],'price':asset.get('price_usd'),'liquidity':asset.get('liquidity_usd')})
    observations=[o for o in observations if observed_ms-o['ms']<=24*3600000][-300:]
    record={**old,'latest':asset,'first_seen_ms':old.get('first_seen_ms',observed_ms),
            'earliest_pool_created_ms':min(earlier) if earlier else None,'observations':observations}
    state['assets'][key]=record
    return record


def observe_entry(state,record,tier,setup,config):
    asset=record['latest'];key=key_of(asset)
    price=rules.number(asset.get('price_usd'))
    if price is None or price<=0:return
    entry=state['entries'].setdefault(key,{'chain':asset['chain'],'mint':asset['mint'],'symbol':safe_symbol(asset['symbol']),
                  'first_pool':asset['pool'],'references':{},'highest_observed_price':price,'latest_tier':tier})
    entry['latest_tier']=tier
    label='qualified' if tier=='qualified' else 'review'
    # A later actual alert has its own price; the earlier unverified observation cannot be used as its entry.
    if label not in entry['references']:
        entry['references'][label]={'observed_ms':asset['observed_ms'],'price':price,'stage':setup['stage'],
                                  'tier':tier,'outcomes':{},'wallet_map':'manual_review_pending' if config['risk'].get('wallet_map_mode')=='manual' else 'automatic'}
    if tier=='qualified' and setup['stage']=='first_breakout' and 'first_breakout' not in entry['references']:
        entry['references']['first_breakout']={'observed_ms':asset['observed_ms'],'price':price,'stage':'first_breakout','tier':tier,'outcomes':{}}
    entry['highest_observed_price']=max(price,entry['highest_observed_price'])


def measure_entries(state,record,config):
    asset=record['latest'];entry=state['entries'].get(key_of(asset))
    price=rules.number(asset.get('price_usd'));stamp=asset['observed_ms']
    if not entry or price is None or price<=0:return
    entry['highest_observed_price']=max(price,entry['highest_observed_price'])
    for reference in entry['references'].values():
        for minutes in config['measurement']['horizons_minutes']:
            target=reference['observed_ms']+minutes*60000
            if str(minutes) in reference['outcomes'] or stamp<target:continue
            delay=stamp-target
            late=delay>config['measurement']['max_endpoint_observation_delay_minutes']*60000
            reference['outcomes'][str(minutes)]={'target_ms':target,'observed_ms':stamp,'delay_ms':delay,
                 'return_pct':None if late else (price/reference['price']-1)*100,
                 'liquidity_usd':asset.get('liquidity_usd'),'status':'missed_target_window' if late else 'actual_observed_price'}


def previously_alerted_accumulation(state,key):
    entry=state['entries'].get(key,{})
    if entry.get('references',{}).get('qualified',{}).get('stage')!='accumulation':return False
    if 'accumulation' not in entry.get('alerted_stages',[]):return False
    return not any(key_of(row)==key and row['stage']=='accumulation' for batch in state['pending'] for row in batch['candidates'])


def scan_network(chain,network,state,config,client):
    result={'network':network['name'],'errors':[],'discovery':[],'evaluated':[],'qualified':[],'review':[],'refreshed':0}
    rows,errors,coverage=source.discover(client,chain,network)
    result['errors']+=errors;result['discovery']=coverage
    # Refresh retained pools, including expired candidates whose measurements are unfinished.
    old=[r for k,r in state['assets'].items() if r['latest']['chain']==chain]
    old.sort(key=lambda r:(0 if key_of(r['latest']) in state['entries'] and pending_measurements(state['entries'][key_of(r['latest'])],config) else 1,r['latest'].get('observed_ms',0)))
    pools=list(dict.fromkeys(r['latest']['pool'] for r in old if now_ms()-r['latest'].get('observed_ms',0)>120000))[:15]
    try:rows+=source.refresh_pools(client,chain,network,pools)
    except Exception as exc:result['errors'].append(str(exc))
    # One pool per canonical chain+mint; never merge symbols or mix token orientations.
    by_mint={}
    for asset in rows:
        previous=by_mint.get(asset['mint'])
        if previous is None or (asset.get('liquidity_usd') or 0)>(previous.get('liquidity_usd') or 0):by_mint[asset['mint']]=asset
    fresh=list(by_mint.values())
    try:source.dex_enrich(client,chain,network,fresh)
    except Exception as exc:result['errors'].append(str(exc))
    eligible=[]
    for asset in fresh:
        stamp=now_ms();record=remember(state,asset,stamp,config);result['refreshed']+=1
        measure_entries(state,record,config)
        # Earliest observed pool, not a replacement pool's reset age.
        market_asset={**asset,'pool_created_ms':record['earliest_pool_created_ms']}
        gate=rules.market_gates(market_asset,config,stamp,record['observations'])
        record['market']=gate
        if gate['passed']:eligible.append(record)
    # Rotating bounded requests: prefer least-recently evaluated valid market setups.
    eligible.sort(key=lambda r:(r.get('last_evaluated_ms',0),-(r['latest'].get('liquidity_usd') or 0)))
    limit=config['discovery']['max_ohlcv_per_network_per_run'];rpc_count=0
    for record in eligible[:limit]:
        asset=record['latest'];stamp=now_ms();record['last_evaluated_ms']=stamp
        try:
            raw=source.candles(client,network,asset,stamp)
            candles=rules.closed_candles(raw,stamp)
            if not candles or stamp-(candles[-1]['open_ms']+rules.STEP_MS)>config['market']['ohlcv_staleness_max_minutes']*60000:
                raise ValueError('Closed 15m candles missing or stale')
            setup=rules.pattern(candles,config)
            record['setup']=setup
            formation=rules.first_formation(raw,asset,record['earliest_pool_created_ms'],stamp,config)
            record['first_formation']=formation
            if formation['status']=='rejected':
                record.setdefault('first_formation_disqualified',{'observed_ms':stamp,'pool':asset['pool'],**formation})
            if formation['status']!='passed' or record.get('first_formation_disqualified'):
                record['tier']='watch';result['evaluated'].append({'mint':asset['mint'],'stage':None,
                    'reason':(record.get('first_formation_disqualified') or formation)['reason']});continue
            # A first encounter during a breakout is already late for this experiment.
            if setup['stage']=='first_breakout' and not previously_alerted_accumulation(state,key_of(asset)):
                setup={**setup,'stage':None,'reason':'first_encounter_after_breakout_excluded'};record['setup']=setup
            if setup['stage'] is None:
                record['tier']='watch';result['evaluated'].append({'mint':asset['mint'],'stage':None,'reason':setup['reason']});continue
            # Re-fetch price after OHLCV/risk work before publishing an observation.
            sec={'blocked':False,'complete':False,'unknown':['not_fetched']}
            try:sec=security_api.fetch_security(client,network,asset)
            except Exception as exc:sec={'blocked':False,'complete':False,'unknown':[str(exc)]}
            maps={'blocked':False,'complete':False,'status':'unknown','reason':'not_fetched'}
            try:maps=security_api.fetch_map(client,asset,sec,now_ms(),network)
            except Exception as exc:maps={'blocked':False,'complete':False,'status':'unknown','reason':str(exc)}
            dev={'status':'unknown','reason':'developer_RPC_budget_or_risk_block'}
            if not sec.get('blocked') and rpc_count<config['risk']['max_developer_rpc_checks_per_network_per_run']:
                rpc_count+=1
                try:dev=security_api.developer_check(client,network,asset,sec,now_ms())
                except Exception as exc:dev={'status':'unknown','reason':str(exc)}
            record.update({'security':sec,'developer':dev,'maps':maps})
            classified=rules.tier(record['market'],setup,sec,dev,maps,config['risk']['wallet_map_mode'])
            if classified in ('qualified','review'):
                # Alert/review references use an actual new read after the checks,
                # never the older candle close or a fabricated execution quote.
                asset.update(source.quote(client,network,asset));asset['observed_ms']=asset['price_observed_ms']
                if not rules.current_price_holds(asset['price_usd'],setup,candles[-1]['close'],config):
                    classified='rejected';record['quote_rejection']='current_price_lost_setup_or_moved_too_far'
                if (asset['price_usd']/formation['metrics']['initial_open']-1)*100>config['first_formation']['max_current_gain_from_initial_pct']:
                    classified='rejected';record['quote_rejection']='live_price_already_extended_from_initial'
                if sec.get('liquidity_lock') is None:sec['liquidity_lock']={'status':'unknown','locked_pct':None}
            record['tier']=classified
            item={'chain':chain,'mint':asset['mint'],'symbol':safe_symbol(asset['symbol']),'stage':setup['stage'],'tier':classified,
                  'price_usd':asset['price_usd'],'observed_ms':asset['observed_ms'],'pool':asset['pool'],
                  'market':record['market'],'security':sec,'developer':dev,'maps':maps}
            item['first_formation']=formation
            item['manual_checks_required']=['wallet_map','official_contract_identity']
            result['evaluated'].append(item)
            if classified in ('qualified','review'):
                observe_entry(state,record,classified,setup,config)
                result[classified].append(item)
        except Exception as exc:
            record['tier']='unknown';result['errors'].append(safe_symbol(asset['symbol'])+': '+str(exc))
    result['eligible_market_count']=len(eligible);result['ohlcv_budget']=limit
    result['watch_retained']=sum(r['latest']['chain']==chain for r in state['assets'].values())
    return result


def enqueue(state,scans,config):
    fresh=[]
    for result in scans.values():
        for row in result.get('qualified',[]):
            entry=state['entries'][key_of(row)]
            stage=row['stage'];sent=entry.setdefault('alerted_stages',[])
            should=not sent or (stage=='first_breakout' and stage not in sent and config['alerts']['notify_first_breakout_after_accumulation'])
            if should:
                fresh.append(row);sent.append(stage)
    if fresh:
        identifier=hashlib.sha256(json.dumps([[r['chain'],r['mint'],r['stage'],r['observed_ms']] for r in fresh],sort_keys=True).encode()).hexdigest()[:24]
        state['pending'].append({'id':identifier,'created_ms':now_ms(),'candidates':fresh})
    return fresh


def report(state,scans,client,config):
    lines=['# Coin Tarama Meme','',f"Son çalışma: {time_label(now_ms())} Türkiye saati.",'',
        '**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**','',
        'Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.','',
        '**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.','',
        'Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.','',
        'GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.','',
        'Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.','',
        '| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for chain,r in scans.items():
        lines.append(f"| {r['network']} | {r.get('refreshed',0)} | {r.get('eligible_market_count',0)} | {len(r.get('evaluated',[]))} | {len(r.get('qualified',[]))} | {len(r.get('review',[]))} | {len(r.get('errors',[]))} |")
    reasons={}
    for r in scans.values():
        for item in r.get('evaluated',[]):
            if item.get('reason'):reasons[item['reason']]=reasons.get(item['reason'],0)+1
    if reasons:
        lines+=['','Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):']
        descriptions={'initial_pool_history_missing':'Havuz başlangıç mumları eksik',
            'initial_history_has_gaps':'Başlangıç geçmişinde veri boşluğu var',
            'current_interval_history_missing':'Güncel mumun yüksek/düşük verisi eksik',
            'earlier_pool_history_not_covered':'Daha eski havuz geçmişi kapsam dışı',
            'first_rise_already_observed':'Önceden yükseliş / uzun fitil görülmüş',
            'already_extended_from_initial_price':'Başlangıç fiyatından fazla uzaklaşmış',
            'post_peak_rebound_excluded':'Tepeden düşüş sonrası yapı elenmiş',
            'first_encounter_after_breakout_excluded':'İlk karşılaşmada kırılım zaten başlamış',
            'no_qualifying_setup':'Birikim yapısı yok'}
        for reason,count in sorted(reasons.items()):
            lines.append('- '+str(count)+': '+'; '.join(descriptions.get(x,x) for x in reason.split(',')))
    for label,tier in [('Otomatik ön eleme geçti — manuel harita kontrolü bekliyor','qualified'),('İnceleme — eksik otomatik teyitler','review')]:
        lines+=['','## '+label,'','| Token / adres | Ağ | Grup | Piyasa değeri / FDV USD | Geliştirici | Harita | Likidite kilidi | Eksik otomatik kontroller |','|---|---|---|---:|---|---|---|---|']
        if not any(r.get(tier) for r in scans.values()):
            lines+=['','**Henüz koşulları sağlayan aday yok.**' if tier=='qualified' else 'Bu çalışmada inceleme kaydı yok.','']
        for chain,r in scans.items():
            for row in r.get(tier,[]):
                label_stage='Birikim' if row['stage']=='accumulation' else 'İlk kırılım'
                cap=row['market'].get('valuation_usd');kind='MC' if row['market']['valuation_kind']=='market_cap_provider_reported' else 'FDV (MC değil)'
                url='https://dexscreener.com/'+config['networks'][chain]['dex']+'/'+row['pool']
                lock=row['security'].get('liquidity_lock') or {};locked=lock.get('locked_pct')
                locked_text='Bilinmiyor' if locked is None else f'%{locked:.1f} (sağlayıcı bildirimi)'
                missing=list(row['security'].get('unknown',[]))
                if row['developer']['status']=='unknown':missing.append('developer: '+row['developer'].get('reason','unknown'))
                lines.append(f"| [{row['symbol']}]({url}) `{row['mint']}` | {r['network']} | {label_stage} | {kind} {cap:.0f} | {row['developer']['status']} | [Manuel kontrol]({bubble_link(row)}) | {locked_text} | {', '.join(missing) or '—'} |")
    lines+=['','## Gerçek gözlem kayıtları','',
            'Fiyatlar sağlayıcının gözlenen fiyatıdır; emir, alış/satış kotasyonu veya gerçekleşebilir net getiri değildir. İnceleme ve daha sonraki teyitli bildirim fiyatları ayrı tutulur. Aynı token havuz/grup değiştirse de yeni bağımsız coin sayılmaz.','',
            '| Token | Ağ | Referans türü | Gerçek gözlem TR | Fiyat | 15dk % | 30dk % | 1s % | 3s % | 6s % | 24s % |',
            '|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
    def pct(value):return '—' if value is None else f'{value:.2f}'
    for entry in state['entries'].values():
        for kind,reference in entry['references'].items():
            returns=[]
            for m in config['measurement']['horizons_minutes']:
                outcome=reference['outcomes'].get(str(m),{})
                value=outcome.get('return_pct')
                returns.append('—' if value is None else pct(value)+f" (+{outcome['delay_ms']/60000:.1f}dk)")
            kind_label={'qualified':'Ön eleme / manuel harita bekliyor','review':'Eksik otomatik teyit','first_breakout':'İlk kırılım / manuel harita bekliyor'}.get(kind,kind)
            lines.append(f"| {entry['symbol']} | {entry['chain']} | {kind_label} | {time_label(reference['observed_ms'])} | {reference['price']:.8g} | {' | '.join(returns)} |")
    lines+=['','## Veri kapsamı ve eksikler','',
            'Getiri sütunları hedef sürelerdir. Parantezdeki +dakika gerçek fiyat gözleminin hedefe gecikmesidir; tam 15/30/60 dakikalık mum getirisi olduğu iddia edilmez. Geçerli gözlem penceresi kaçırılırsa sonuç boş kalır.','',
            'Her ağda yalnız yeni havuz akışı sınırlı sayfalarla okunur. Önceki izlenen havuzlar kalıcı kayıttan yenilenir. Ham keşif ve sosyal gözlem tokenleri aday listesinde gösterilmez. Ücretli profil/boost olumlu sinyal sayılmaz. Aynı simge farklı kontratlarda birleştirilmez.','',
            'Üç kapalı 15 dakikalık birikim mumu ve en az 45 dakikalık havuz yaşı gerekir. Bu süreden önce pump yapan tokenleri bu yöntem önceden yakalayamaz. Başlangıç havuz verisi tokenin tüm zincir geçmişi veya eski havuzları kapsadığı anlamına gelmez.','',
            'Bubblemaps haritasını kullanıcı manuel inceler; API anahtarı gerekmez. Hiçbir kayıt otomatik veya manuel harita onayı almış sayılmaz. Robinhood/HyperEVM harita desteği bu sürümde doğrulanmadığından genel uygulama bağlantısı verilir; uygun ağ/harita bulunamazsa bu kontrol eksik kalır. RPC veya güvenlik kaynağının ağ desteği yoksa o ağda fiyat/havuz takibi sürer; eksik otomatik teyitle aday bildirilmez.','',
            'GitHub planı yaklaşık 5 dakikada birdir; zamanlayıcı gecikebilir. Birkaç saniyede oluşan ilk pump yakalanamayabilir. Mum/istek bütçesi nedeniyle aynı anda bütün havuzlara bakıldığı iddia edilmez.','']
    for chain,r in scans.items():
        if r.get('errors'):lines+=['- '+r['network']+': '+'; '.join(r['errors'][:6])]
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    cloud.save(OUT/'summary.json',{'version':config['version'],'updated_ms':now_ms(),'networks':scans,
             'unique_chain_tokens_observed':len(state['entries']),'api_requests':dict(client.stats),
             'wallet_map_mode':config['risk']['wallet_map_mode'],
             'qualification_scope':'automated_risk_prefilter_manual_map_pending',
             'bubblemaps_configured':bool(os.environ.get('BUBBLEMAPS_API_KEY'))})


def scan():
    config=json.loads((ROOT/'meme_config.json').read_text(encoding='utf-8'))
    state=json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else new_state()
    if state['rules_fingerprint']!=fingerprint():raise RuntimeError('Meme rules changed; use an explicitly new experiment branch')
    client=source.Client(config);scans={}
    # Each worker owns its network's existing records. Add new records only under that prefix.
    network_states={chain:{**state,'assets':{k:v for k,v in state['assets'].items() if v['latest']['chain']==chain},
                    'entries':{k:v for k,v in state['entries'].items() if v['chain']==chain}} for chain in config['networks']}
    with ThreadPoolExecutor(max_workers=5) as executor:
        jobs={executor.submit(scan_network,c,n,network_states[c],config,client):c for c,n in config['networks'].items()}
        for job in as_completed(jobs):
            chain=jobs[job]
            try:scans[chain]=job.result()
            except Exception as exc:scans[chain]={'network':config['networks'][chain]['name'],'errors':[str(exc)],'qualified':[],'review':[],'evaluated':[]}
    expire_missed_endpoints(state,config,now_ms())
    for chain,substate in network_states.items():
        expire_missed_endpoints(substate,config,now_ms())
        candidates=list(substate['assets'].items())
        # Keep outcome-bearing tokens until measurements finish, otherwise rank recent/real liquidity.
        candidates.sort(key=lambda kv:(0 if kv[0] in substate['entries'] and pending_measurements(substate['entries'][kv[0]],config) else 1,
                         -(kv[1]['latest'].get('liquidity_usd') or 0),-kv[1]['latest']['observed_ms']))
        protected={k:v for k,v in candidates if k in substate['entries'] and pending_measurements(substate['entries'][k],config)}
        recent=[(k,v) for k,v in candidates if k not in protected and v.get('earliest_pool_created_ms') is not None
                and now_ms()-v['earliest_pool_created_ms']<=config['market']['max_pool_age_hours']*3600000]
        keep={**dict(recent[:config['discovery']['max_watch_per_network']]),**protected}
        for key in [k for k,v in state['assets'].items() if v['latest']['chain']==chain]:state['assets'].pop(key)
        state['assets'].update(keep);state['entries'].update(substate['entries'])
    fresh=enqueue(state,scans,config)
    state['updated_ms']=now_ms();state['runs']=(state['runs']+[{'ms':state['updated_ms'],'networks':{c:len(r.get('qualified',[])) for c,r in scans.items()}}])[-1000:]
    cloud.save(STATE,state);report(state,scans,client,config)
    print(json.dumps({'new_alerts':len(fresh),'networks':{c:{'refreshed':r.get('refreshed',0),'review':len(r.get('review',[])),'qualified':len(r.get('qualified',[])),'errors':len(r.get('errors',[]))} for c,r in scans.items()}}))


def notify():
    state=json.loads(STATE.read_text(encoding='utf-8'))
    user=os.environ.get('COIN_NOTIFY_USER','').strip();repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN')
    if user and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',user):raise ValueError('Invalid GitHub notification recipient')
    if not state['pending']:print('Meme: no verified new candidates to notify.');return
    if not repo or not token:raise RuntimeError('GitHub issue notification configuration missing')
    url='https://api.github.com/repos/'+repo+'/issues';headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'}
    for batch in list(state['pending']):
        marker='<!-- coin-tarama-meme:'+batch['id']+' -->'
        existing=cloud.http_json(url+'?state=all&per_page=100',headers=headers,label='GitHub Issues')
        if not any(marker in (i.get('body') or '') for i in existing):
            body=('@'+user+'\n\n' if user else '')+'Coin Tarama Meme — ilk oluşum ön elemesi\n\nİlk aday birikim evresinde aranır; başlangıç dahil erişilen havuz geçmişinde eşikleri aşan yükseliş/düşüş görülmemiştir. Tokenin tüm yaşamı doğrulanmış veya yükseliş garanti edilmiş değildir.\n\n**Bubblemaps cüzdan haritası MANUEL KONTROL EDİLMELİ; harita onayı verilmedi.**\nGMGN kullanılmaz; tüm sniper/bundler etiketleri ve tam geliştirici geçmişi kapsanmaz. Resmî/orijinal kontrat eşleşmesi ayrıca doğrulanmalıdır.\n\n'
            for row in batch['candidates']:
                body+=f"{row['symbol']} · {row['chain']} · {row['stage']}\nKontrat: `{row['mint']}`\nGözlem: {time_label(row['observed_ms'])} TR; fiyat ${row['price_usd']:.8g}\nGeliştirici: yalnız son 45 dakikalık taranan işlem penceresi; bağlantılı tüm cüzdanlar veya geçmişin tamamı için satış yapmadı iddiası değildir.\nBubblemaps: {bubble_link(row)}\nhttps://dexscreener.com/{json.loads((ROOT/'meme_config.json').read_text(encoding='utf-8'))['networks'][row['chain']]['dex']}/{row['pool']}\n\n"
            body+='Filtreleri sağlayan izleme kaydıdır; güvenli token veya getiri garantisi değildir.\n\n'+marker
            cloud.http_json(url,{'title':'Coin Tarama Meme · Ön eleme / manuel harita · '+time_label(batch['created_ms']),'body':body},headers,label='GitHub Issues')
        state['pending']=[b for b in state['pending'] if b['id']!=batch['id']];cloud.save(STATE,state)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['pull-state','scan','push-state','notify','check-status'])
    args=parser.parse_args();configure()
    if args.phase=='pull-state':pull_state()
    elif args.phase=='scan':scan()
    elif args.phase=='push-state':cloud.push_state()
    elif args.phase=='notify':notify()
    else:
        summary=json.loads((OUT/'summary.json').read_text(encoding='utf-8'))
        raise SystemExit(1 if any(r.get('errors') for r in summary['networks'].values()) else 0)
