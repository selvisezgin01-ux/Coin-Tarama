"""Meme V6: bounded discovery, young-pool revisit, data-only candles and observed exits."""
from meme_scan import *
from copy import deepcopy
from collections import Counter
import argparse,subprocess,math
import meme_scan as core
import meme_pipeline as pipeline
import meme_base_volume as base_volume
import meme_paper_v5 as paper
import meme_followup_watch as followup
import meme_social_watch as social
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'cloud_output_meme_v6';STATE=OUT/'state.json'
CONFIG=ROOT/'meme_v6_config.json'
BASE_OBSERVE=core.observe_entry
V4_FP='06ac5cc225f7b765bed5958110f8a96819ac628cc143389dfa23243407b9976a'

PHASE_LABELS={'early_5m':'5 dk ilk taban + alım yönlü hacim','confirmed_15m':'15 dk fiyat teyidi + 5 dk alım akışı'}

def config():return json.loads(CONFIG.read_text(encoding='utf-8'))

def contract_block(row):
    chain=row['chain'];address=row['mint']
    if chain not in config()['networks'] or not source.valid_address(chain,address):raise ValueError('Invalid token contract identity')
    return 'Ağ: '+config()['networks'][chain]['name']+'\n\nKontrat / token adresi (kopyala):\n```text\n'+address+'\n```\n'
def fingerprint():
    h=hashlib.sha256()
    for name in ('meme_base_volume.py','meme_v6.py','meme_v6_config.json','meme_pipeline.py','meme_paper_v5.py','meme_scan.py','meme_rules.py','meme_sources.py','meme_security.py','meme_hybrid.py','meme_large_buyers.py','meme_followup_watch.py','meme_social_watch.py'):
        h.update(name.encode());h.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return h.hexdigest()
def new_state():
    return {'version':'meme-v6-pipeline','rules_fingerprint':fingerprint(),'assets':{},'entries':{},'pending':[],
            'runs':[],'discovery_checkpoints':{},'delivery_receipts':[],'paper_v5':{'cases':{},'errors':[]}}
def bind():
    if os.environ.setdefault('SCANNER_STATE_BRANCH','scanner-state-meme-v6')!='scanner-state-meme-v6':raise ValueError('Independent V6 branch required')
    core.OUT=OUT;core.STATE=STATE;core.fingerprint=fingerprint;core.new_state=new_state
    core.notify=notify;core.previously_alerted_accumulation=previously_alerted_accumulation
    cloud.OUT=OUT;cloud.STATE=STATE;cloud.fingerprint=fingerprint;cloud.new_state=new_state
def seed(previous,branch,commit,stamp):
    expected='a067c337285dc7c4c914d4e30c21efe5575eb62de6c189c2adfc3b6df52c2faa'
    if branch!='scanner-state-meme-v5' or previous.get('version')!='meme-v5-pipeline' or previous.get('rules_fingerprint')!=expected:raise ValueError('Unexpected V5 archive')
    state=new_state();state['previous_v5']={k:deepcopy(v) for k,v in previous.items() if k!='assets'}
    state['assets']=deepcopy(previous['assets']);state['discovery_checkpoints']=deepcopy(previous.get('discovery_checkpoints',{}))
    if 'provider_backoff_until_ms' in previous:state['provider_backoff_until_ms']=previous['provider_backoff_until_ms']
    for r in state['assets'].values():
        for key in ('setup','timeframe_assessment','signal_phase','security','maps','developer','market','buy_pressure'):r.pop(key,None)
        r['tier']='watch'
    state['migration']={'from_branch':branch,'commit':commit,'source_fingerprint':expected,'migrated_ms':stamp,
        'old_reference_prices_preserved':True,'no_backfilled_v6_entries':True,'old_pump_latches_preserved':True}
    return state

def pull():
    cloud.pull_state()
    if (OUT/'parent.txt').read_text(encoding='ascii').strip():return
    branch='scanner-state-meme-v5';cloud.git('fetch','--no-tags','origin','refs/heads/'+branch)
    commit=cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
    previous=json.loads(cloud.git('show',commit+':state.json').stdout);cloud.save(STATE,seed(previous,branch,commit,now_ms()))

def previously_alerted_accumulation(state,key):
    return any(r['key']==key and r['stage']=='accumulation' for r in state.get('delivery_receipts',[]))
def observe_entry_v6(state,record,tier,setup,cfg):
    BASE_OBSERVE(state,record,tier,setup,cfg)
    for ref in state['entries'][key_of(record['latest'])]['references'].values():ref['experiment']='meme-v6-pipeline'
    if tier=='qualified':paper.register(state,record,record['signal_phase'],now_ms())


def send_candidate_notifications():
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
            body=('@'+user+'\n\n' if user else '')+'Coin Tarama Meme — ilk oluşum ön elemesi — ilk taban + alım yönlü erken hacim\n\nİlk aday birikim evresinde aranır; başlangıç dahil erişilen havuz geçmişinde eşikleri aşan yükseliş/düşüş görülmemiştir. Tokenin tüm yaşamı doğrulanmış veya yükseliş garanti edilmiş değildir.\n\n**Bubblemaps cüzdan haritası MANUEL KONTROL EDİLMELİ; harita onayı verilmedi.**\nGMGN kullanılmaz; tüm sniper/bundler etiketleri ve tam geliştirici geçmişi kapsanmaz. Resmî/orijinal kontrat eşleşmesi ayrıca doğrulanmalıdır.\n\n'
            for row in batch['candidates']:
                body+=f"{row['symbol']} · {row['chain']} · {PHASE_LABELS.get(row.get('signal_phase'),row['stage'])} · {row['stage']}\n{large_buyers.text(row.get('large_buyers'))}\n{contract_block(row)}\nİlk taban + hacim: {row['volume_metrics']['volume_multiple']:.2f}x; MCAP ${row['market_cap_usd']:.0f} (gözlem anı).\n{base_volume.text(row.get('buy_pressure'))}\nGözlem: {time_label(row['observed_ms'])} TR; fiyat ${row['price_usd']:.8g}\nGeliştirici: yalnız son 45 dakikalık taranan işlem penceresi; bağlantılı tüm cüzdanlar veya geçmişin tamamı için satış yapmadı iddiası değildir.\nBubblemaps: {bubble_link(row)}\nhttps://dexscreener.com/{json.loads((ROOT/'meme_config.json').read_text(encoding='utf-8'))['networks'][row['chain']]['dex']}/{row['pool']}\n\n"
            body+='Filtreleri sağlayan izleme kaydıdır; güvenli token veya getiri garantisi değildir.\n\n'+marker
            cloud.http_json(url,{'title':'Coin Tarama Meme · Ön eleme / manuel harita · '+time_label(batch['created_ms']),'body':body},headers,label='GitHub Issues')
        state['pending']=[b for b in state['pending'] if b['id']!=batch['id']];cloud.save(STATE,state)


BASE_NOTIFY=send_candidate_notifications

def scan_network(chain,network,state,config,client):
    result={'network':network['name'],'errors':[],'discovery':[],'evaluated':[],'qualified':[],'review':[],'refreshed':0}
    rows,errors,coverage=pipeline.discover(client,chain,network,state,now_ms())
    result['errors']+=errors;result['discovery']=coverage
    state.setdefault('discovery_checkpoints',{})[chain]=coverage['next_checkpoint_ms']
    # Refresh retained pools, including expired candidates whose measurements are unfinished.
    old=[r for k,r in state['assets'].items() if r['latest']['chain']==chain]
    pools=pipeline.refresh_targets(old,state,chain,now_ms(),config)
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
    eligible=[];refreshed_records=[];security_count=0;ohlcv_success=0
    for asset in fresh:
        stamp=now_ms();record=remember(state,asset,stamp,config);result['refreshed']+=1
        measure_entries(state,record,config)
        # Earliest observed pool, not a replacement pool's reset age.
        market_asset={**asset,'pool_created_ms':record['earliest_pool_created_ms']}
        gate=rules.market_gates(market_asset,config,stamp,record['observations'])
        record['market']=gate;record['tier']='watch';record['buy_pressure']={'status':'not_checked','reasons':['not_evaluated_this_cycle']};refreshed_records.append(record)
        if pipeline.inspectable(record,config,stamp):eligible.append(record)
    # Rotating bounded requests: prefer least-recently evaluated valid market setups.
    eligible.sort(key=lambda r:(0 if r['market']['passed'] else 1,pipeline.priority(r,now_ms(),config)))
    limit=config['discovery']['max_ohlcv_per_network_per_run'];rpc_count=0
    for record in eligible[:limit]:
        asset=record['latest'];stamp=now_ms();record['last_evaluated_ms']=stamp
        try:
            raw=source.candles(client,network,asset,stamp);ohlcv_success+=1
            assessment=base_volume.evaluate(raw,asset,record['earliest_pool_created_ms'],stamp,config,record.get('first_base'))
            if assessment.get('first_base'):record.setdefault('first_base',assessment['first_base'])
            record['timeframe_assessment']=assessment
            setup=assessment['setup'];phase=assessment['phase']
            record['signal_phase']=phase
            record['setup']=setup
            formation=assessment['formation']
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
            if not record['market']['passed']:
                result['evaluated'].append({'mint':asset['mint'],'stage':None,'reason':'data_observation_market_not_ready'});continue
            if security_count>=config['discovery']['max_security_checks_per_network_per_run']:
                result['evaluated'].append({'mint':asset['mint'],'stage':None,'reason':'security_budget_waiting'});continue
            security_count+=1
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
            # Security/dev eligibility is required before positive directional-flow evidence.
            participation={'status':'unknown','windows':{}}
            pressure={'status':'not_checked','reasons':['security_or_developer_eligibility_incomplete']}
            if classified=='qualified':
                try:
                    payload=client.gecko(f"networks/{network['gecko']}/pools/{asset['pool']}/trades?token={asset['mint']}&include_anomalous=true")
                    pressure=base_volume.pressure(payload,asset,sec,setup,now_ms(),config)
                    participation=large_buyers.assess(payload,asset,sec,now_ms(),config)
                except Exception as exc:pressure={'status':'unknown','reasons':[str(exc)]}
                if pressure['status']!='passed':classified='review' if pressure['status']=='unknown' else 'watch'
            record['buy_pressure']=pressure;record['large_buyers']=participation
            if classified in ('qualified','review'):
                # Alert/review references use an actual new read after the checks,
                # never the older candle close or a fabricated execution quote.
                asset.update(base_volume.fresh_observation(client,network,asset));asset['observed_ms']=asset['price_observed_ms']
                cap=rules.number(asset.get('market_cap_usd'));liquidity=rules.number(asset.get('liquidity_usd'))
                if cap is None:
                    classified='review';record['quote_rejection']='fresh_market_cap_unknown_no_fdv_substitution'
                elif not config['market']['valuation_min_usd']<=cap<=config['market']['valuation_max_usd']:
                    classified='rejected';record['quote_rejection']='fresh_market_cap_out_of_50k_500k_band'
                if liquidity is None:
                    classified='review' if classified!='rejected' else classified;record['quote_rejection']='fresh_liquidity_unknown'
                elif liquidity<config['market']['liquidity_min_usd'] or (cap and liquidity/cap<config['market']['liquidity_valuation_min_ratio']):
                    classified='rejected';record['quote_rejection']='fresh_liquidity_gate_failed'
                if now_ms()-assessment['cutoff_ms']>config['timeframes']['max_closed_lag_minutes']*60000:
                    classified='watch';record['quote_rejection']='buy_pressure_feature_cutoff_expired'
                record['market']['valuation_usd']=cap
                record['market']['valuation_kind']='market_cap_provider_reported' if cap is not None else 'current_market_cap_unknown'
                record['buy_pressure']['market_cap_observed_usd']=cap
                record['buy_pressure']['market_cap_observed_ms']=asset['price_observed_ms']
                if not rules.current_price_holds(asset['price_usd'],setup,assessment['last_close'],config):
                    classified='rejected';record['quote_rejection']='current_price_lost_setup_or_moved_too_far'
                if (asset['price_usd']/formation['metrics']['initial_open']-1)*100>config['first_formation']['max_current_gain_from_initial_pct']:
                    classified='rejected';record['quote_rejection']='live_price_already_extended_from_initial'
                if sec.get('liquidity_lock') is None:sec['liquidity_lock']={'status':'unknown','locked_pct':None}
            record['tier']=classified
            item={'chain':chain,'mint':asset['mint'],'symbol':safe_symbol(asset['symbol']),'stage':setup['stage'],'tier':classified,
                  'price_usd':asset['price_usd'],'observed_ms':asset['observed_ms'],'pool':asset['pool'],
                  'market':record['market'],'security':sec,'developer':dev,'maps':maps}
            item['first_formation']=formation
            item['signal_phase']=phase;item['large_buyers']=participation
            item['feature_cutoff_ms']=assessment['cutoff_ms'];item['buy_pressure']=pressure;item['first_base']=record.get('first_base');item['volume_metrics']=setup['metrics'];item['market_cap_usd']=asset.get('market_cap_usd')
            item['manual_checks_required']=['wallet_map','official_contract_identity']
            result['evaluated'].append(item)
            if classified in ('qualified','review'):
                observe_entry_v6(state,record,classified,setup,config)
                result[classified].append(item)
        except Exception as exc:
            record['tier']='unknown';result['errors'].append(safe_symbol(asset['symbol'])+': '+str(exc))
    result['funnel']=pipeline.funnel(refreshed_records,now_ms(),config)
    result['funnel'].update(ohlcv_read=ohlcv_success,ohlcv_attempted=min(len(eligible),limit),ohlcv_budget_waiting=max(0,len(eligible)-limit),security_checked=security_count)
    result['funnel']['buy_pressure_status']=dict(Counter(r.get('buy_pressure',{}).get('status','not_checked') for r in refreshed_records))
    result['funnel']['buy_pressure_reasons']=dict(Counter(reason for r in refreshed_records for reason in r.get('buy_pressure',{}).get('reasons',[])))
    result['eligible_market_count']=result['funnel']['market_pass'];result['ohlcv_budget']=limit
    result['watch_retained']=sum(r['latest']['chain']==chain for r in state['assets'].values())
    return result


def enqueue_v6(state,scans,cfg):
    fresh=[];pending={(key_of(r),r.get('signal_phase'),r['stage']) for b in state['pending'] for r in b['candidates']}
    delivered={(r['key'],r['phase'],r['stage']) for r in state['delivery_receipts']}
    for result in scans.values():
        for row in result['qualified']:
            key=key_of(row);ident=(key,row['signal_phase'],row['stage'])
            if ident in pending or ident in delivered:continue
            if row['signal_phase']=='early_5m' and any(k==key and phase=='confirmed_15m' for k,phase,_ in delivered):continue
            if row['stage']=='first_breakout' and not previously_alerted_accumulation(state,key):continue
            fresh.append(row);pending.add(ident)
    fresh.sort(key=lambda r:(-state['assets'][key_of(r)]['latest'].get('liquidity_usd',0),r['chain'],r['mint']))
    fresh=fresh[:cfg['pipeline']['max_candidates_per_run']]
    if fresh:
        uid=hashlib.sha256(json.dumps(['meme-v6',[(r['chain'],r['mint'],r['observed_ms'],r['signal_phase'],r['stage']) for r in fresh]]).encode()).hexdigest()[:24]
        state['pending'].append({'id':uid,'created_ms':now_ms(),'candidates':fresh})
    return fresh

def scan():
    cfg=config();state=json.loads(STATE.read_text(encoding='utf-8'))
    if state['rules_fingerprint']!=fingerprint():raise ValueError('V6 rules changed; new version required')
    start=now_ms();client=base_volume.Client(cfg,state.get('provider_backoff_until_ms',0));scans={}
    global CYCLE_CLIENT
    CYCLE_CLIENT=client
    substates={chain:{**state,'assets':{k:deepcopy(v) for k,v in state['assets'].items() if v['latest']['chain']==chain},
        'entries':{k:deepcopy(v) for k,v in state['entries'].items() if v['chain']==chain},
        'discovery_checkpoints':deepcopy(state['discovery_checkpoints']),'paper_v5':{'cases':{},'errors':[]}} for chain in cfg['networks']}
    with ThreadPoolExecutor(max_workers=5) as pool:
        jobs={pool.submit(scan_network,c,n,substates[c],cfg,client):c for c,n in cfg['networks'].items()}
        for job in as_completed(jobs):
            chain=jobs[job]
            try:scans[chain]=job.result()
            except Exception as e:scans[chain]={'network':cfg['networks'][chain]['name'],'errors':[str(e)],'qualified':[],'review':[],'evaluated':[]}
    stamp=now_ms()
    for chain,sub in substates.items():
        state['discovery_checkpoints'][chain]=sub['discovery_checkpoints'].get(chain)
        values=list(sub['assets'].items());active=set(sub['entries'])
        values.sort(key=lambda kv:(0 if kv[0] in active else 1,pipeline.priority(kv[1],stamp,cfg)))
        protected={k:v for k,v in values if k in active and pending_measurements(sub['entries'][k],cfg)}
        keep={k:v for k,v in values if k not in protected and pipeline.age(v,stamp) is not None and 0<=pipeline.age(v,stamp)<=cfg['market']['max_pool_age_hours']*60}
        keep={**dict(list(keep.items())[:cfg['discovery']['max_watch_per_network']]),**protected}
        state['assets']={**{k:v for k,v in state['assets'].items() if v['latest']['chain']!=chain},**keep}
        state['entries'].update(sub['entries']);state['paper_v5']['cases'].update({k:v for k,v in sub['paper_v5']['cases'].items() if k not in state['paper_v5']['cases']})
    expire_missed_endpoints(state,cfg,stamp);fresh=enqueue_v6(state,scans,cfg)
    # Existing cohorts stay isolated and their next actual observations can still mature.
    old=state.get('previous_v5',{}).get('entries',{})
    for record in state['assets'].values():
        measure_entries({'entries':old},record,cfg)
    state['updated_ms']=stamp;state['runs']=(state['runs']+[{'ms':stamp,'started_ms':start,'networks':{c:len(s['qualified']) for c,s in scans.items()}}])[-1000:]
    state['last_scan_summary']={c:{'refreshed':s.get('refreshed',0),'eligible':s.get('eligible_market_count',0),'evaluated':len(s['evaluated']),
        'qualified':len(s['qualified']),'review':len(s['review']),'errors':s['errors'],'funnel':s.get('funnel',{}),'discovery':s.get('discovery',{}),
        'reasons':dict(Counter(i.get('reason','risk_or_quote_assessment') for i in s['evaluated']))} for c,s in scans.items()}
    state['timing']={'started_ms':start,'finished_ms':stamp,'duration_seconds':(stamp-start)/1000,'github_run_created_at':os.environ.get('GH_RUN_CREATED_AT'),
        'worker_started_ms':os.environ.get('MEME_WORKER_STARTED_MS'),'github_job_started_at':os.environ.get('GH_JOB_STARTED_AT'),
        'cadence':pipeline.cadence(state['runs'],stamp)}
    state['last_api_requests']=dict(client.stats);cloud.save(STATE,state)
    if client.rate_limited:
        state['provider_backoff_until_ms']=stamp+15*60000
        cloud.save(STATE,state)
    render_core(state,scans,client,cfg)
    render_extra(state)
    (OUT/'ready.txt').write_text('complete',encoding='ascii');print(json.dumps({'updated_ms':stamp,'new_alerts':len(fresh),'summary':state['last_scan_summary'],'timing':state['timing']},ensure_ascii=True),flush=True)

def render_extra(state):
    path=OUT/'report.md';txt=path.read_text(encoding='utf-8').split('<!-- meme-v6-pipeline -->',1)[0]
    txt=txt.replace('# Coin Tarama Meme\n','# Coin Tarama Meme — V6\n',1)
    txt+='\n\n<!-- meme-v6-pipeline -->\n\n## V6 keşif, aşamalar ve gerçek zamanlama\n\n'
    txt+='Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.\n\n'
    txt+='Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.\n\n'
    for chain,v in state.get('last_scan_summary',{}).items():txt+='- '+chain+': '+json.dumps(v,ensure_ascii=False)+'\n'
    txt+='\nZamanlama: '+json.dumps(state.get('timing',{}),ensure_ascii=False)+'\n\n'
    txt+='İstek durumu: '+json.dumps(state.get('last_api_requests',{}),ensure_ascii=False)+'; sağlayıcı429bekleme bitişi: '+str(state.get('provider_backoff_until_ms'))+'\n\n'
    txt+='GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.\n\n'
    txt+='## Sabit miktarlı gösterge satış deneyi\n\n100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.\n\n'
    for c in state.get('paper_v5',{}).get('cases',{}).values():
        txt+='- '+safe_symbol(c['symbol'])+' / '+c['chain']+' / '+c['phase']+': '+json.dumps({'references':c['observed_ms'],'sizes':c['sizes'],'outcomes':c['outcomes'],
            'observed_min_pct':c['min_observed_return_pct'],'observed_max_pct':c['max_observed_return_pct'],'closed_5m_path':c.get('closed_5m_path'),'full_path_mae_mfe':None},ensure_ascii=False)+'\n'
    txt+='\nÖlçüm hataları: '+json.dumps(state.get('paper_v5',{}).get('errors',[]),ensure_ascii=False)+'\n'
    txt+='\n## İlk taban ve alım yönlü erken hacim\n\nMCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.\n\n'
    for k,rec in state.get('assets',{}).items():
        if rec.get('first_base') or rec.get('buy_pressure',{}).get('status') in ('passed','failed','unknown'):
            txt+='- '+k+': '+json.dumps({'tier':rec.get('tier'),'first_base':rec.get('first_base'),'buy_pressure':rec.get('buy_pressure'),'quote_rejection':rec.get('quote_rejection')},ensure_ascii=False)+'\n'
    path.write_text(txt,encoding='utf-8')

def mark_receipts(state,batch):
    for r in batch['candidates']:
        key=key_of(r);receipt={'id':batch['id'],'key':key,'phase':r['signal_phase'],'stage':r['stage'],'observed_ms':r['observed_ms']}
        if receipt not in state['delivery_receipts']:state['delivery_receipts'].append(receipt)
        entry=state['entries'][key]
        for field,value in (('alerted_phases',r['signal_phase']),('alerted_stages',r['stage'])):
            if value not in entry.setdefault(field,[]):entry[field].append(value)

def notify():
    state=json.loads(STATE.read_text(encoding='utf-8'));cfg=config()
    if not state['pending']:return
    repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN')
    if not repo or not token:raise ValueError('GitHub notification configuration missing')
    existing=cloud.http_json('https://api.github.com/repos/'+repo+'/issues?state=all&sort=created&direction=desc&per_page=100',headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'},label='GitHub Issues')
    valid=[]
    for b in state['pending']:
        marker='<!-- coin-tarama-meme:'+b['id']+' -->'
        if any(marker in (i.get('body') or '') and i.get('user',{}).get('login')=='github-actions[bot]' for i in existing):mark_receipts(state,b);continue
        rows=[]
        for r in b['candidates']:
            rec=state['assets'].get(key_of(r),{});flags=state.get('followup_watch',{}).get('tokens',{}).get(key_of(r),{}).get('flags',{})
            critical=any(flags.get(k) for k in ('security_deterioration','developer_outflow','liquidity_withdrawal'))
            if 0<=now_ms()-r['observed_ms']<=cfg['pipeline']['notification_max_age_minutes']*60000 and rec.get('tier')=='qualified' and not critical:rows.append(r)
        if rows:valid.append({**b,'candidates':rows})
    state['pending']=valid;cloud.save(STATE,state)
    # Existing formatter, exact security disclosures and GitHub marker protocol stay intact.
    for batch in valid:
        state=json.loads(STATE.read_text(encoding='utf-8'));others=[b for b in state['pending'] if b['id']!=batch['id']]
        state['pending']=[batch];cloud.save(STATE,state)
        try:BASE_NOTIFY()
        except Exception:
            current=json.loads(STATE.read_text(encoding='utf-8'));current['pending']+=others;cloud.save(STATE,current);raise
        current=json.loads(STATE.read_text(encoding='utf-8'));mark_receipts(current,batch);current['pending']+=others;cloud.save(STATE,current)

def enrich():
    state=json.loads(STATE.read_text(encoding='utf-8'));cfg=config();client=globals().get('CYCLE_CLIENT') or pipeline.BudgetClient(cfg,state.get('provider_backoff_until_ms',0))
    followup.annotate(state,cfg,client);social.annotate(state,cfg,client);paper.observe(state,cfg,client,now_ms())
    state['last_api_requests']=dict(client.stats)
    if client.rate_limited:state['provider_backoff_until_ms']=now_ms()+15*60000
    cloud.save(STATE,state);followup.append_report(state);social.append_report(state);render_extra(state)

def cycle():
    pull();scan();cloud.push_state()
    try:enrich();followup.notify()
    finally:
        state=json.loads(STATE.read_text(encoding='utf-8'));render_extra(state);cloud.push_state()

def worker(minutes):
    cfg=config();started=now_ms();os.environ['MEME_WORKER_STARTED_MS']=str(started);deadline=time.monotonic()+minutes*60
    repo=os.environ.get('GITHUB_REPOSITORY');runid=os.environ.get('GITHUB_RUN_ID');token=os.environ.get('GH_TOKEN')
    if repo and runid and token:
        try:
            url='https://api.github.com/repos/'+repo+'/actions/runs/'+runid;headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'}
            metadata=cloud.http_json(url,headers=headers,label='GitHub run metadata');jobs=cloud.http_json(url+'/jobs',headers=headers,label='GitHub job metadata')
            os.environ['GH_RUN_CREATED_AT']=metadata['created_at']
            active=next((j for j in jobs['jobs'] if j['status']=='in_progress'),None)
            if active:os.environ['GH_JOB_STARTED_AT']=active['started_at']
        except Exception as e:print('Timing metadata unknown: '+str(e),flush=True)
    cycles=0
    while True:
        tick=time.monotonic()
        try:cycle();cycles+=1
        except Exception as e:print(json.dumps({'worker_error':str(e),'observed_ms':now_ms()}),flush=True)
        # A bounded hosted session does not assert a durable always-on service.
        wait=max(0,cfg['pipeline']['worker_interval_seconds']-(time.monotonic()-tick))
        if time.monotonic()+wait>=deadline:break
        time.sleep(wait)
    if cycles==0:raise RuntimeError('No complete scan cycle')
    print(json.dumps({'completed_cycles':cycles,'worker_started_ms':started,'worker_finished_ms':now_ms()}),flush=True)

def render_core(state,scans,client,config):
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
        lines+=['','## '+label,'','| Token / adres | Ağ | Grup | Piyasa değeri / FDV USD | Geliştirici | Harita | Likidite kilidi | Büyük alıcı desteği | Eksik otomatik kontroller |','|---|---|---|---:|---|---|---|---|---|']
        if not any(r.get(tier) for r in scans.values()):
            lines+=['','**Henüz koşulları sağlayan aday yok.**' if tier=='qualified' else 'Bu çalışmada inceleme kaydı yok.','']
        for chain,r in scans.items():
            for row in r.get(tier,[]):
                label_stage=PHASE_LABELS.get(row.get('signal_phase'),'Birikim')+(' / ilk kırılım' if row['stage']=='first_breakout' else '')
                cap=row['market'].get('valuation_usd');kind='MC' if row['market']['valuation_kind']=='market_cap_provider_reported' else 'MCAP bilinmiyor'
                url='https://dexscreener.com/'+config['networks'][chain]['dex']+'/'+row['pool']
                lock=row['security'].get('liquidity_lock') or {};locked=lock.get('locked_pct')
                locked_text='Bilinmiyor' if locked is None else f'%{locked:.1f} (sağlayıcı bildirimi)'
                missing=list(row['security'].get('unknown',[]))
                if row['developer']['status']=='unknown':missing.append('developer: '+row['developer'].get('reason','unknown'))
                lines.append(f"| [{row['symbol']}]({url}) `{row['mint']}` | {r['network']} | {label_stage} | {kind} {str(round(cap)) if isinstance(cap,(int,float)) else '—'} | {row['developer']['status']} | [Manuel kontrol]({bubble_link(row)}) | {locked_text} | {large_buyers.text(row.get('large_buyers'))} | {', '.join(missing) or '—'} |")
    lines+=['','## Gerçek gözlem kayıtları','',
            'Fiyatlar sağlayıcının gözlenen fiyatıdır; emir, alış/satış kotasyonu veya gerçekleşebilir net getiri değildir. İnceleme ve daha sonraki teyitli bildirim fiyatları ayrı tutulur. Aynı token havuz/grup değiştirse de yeni bağımsız coin sayılmaz.','',
            '| Token | Ağ | Referans türü | Gerçek gözlem TR | Fiyat | 15dk % | 30dk % | 1s % | 3s % | 6s % | 24s % |',
            '|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
    def pct(value):return '—' if value is None else f'{value:.2f}'
    for entry in state['entries'].values():
        for kind,reference in entry['references'].items():
            if reference.get('alias_of'):continue
            returns=[]
            for m in config['measurement']['horizons_minutes']:
                outcome=reference['outcomes'].get(str(m),{})
                value=outcome.get('return_pct')
                returns.append('—' if value is None else pct(value)+f" (+{outcome['delay_ms']/60000:.1f}dk)")
            kind_label={'early_5m':'5 dk erken aday','confirmed_15m':'15 dk teknik teyit','qualified':'Ön eleme / manuel harita bekliyor','review':'Eksik otomatik teyit','first_breakout':'İlk kırılım / manuel harita bekliyor'}.get(kind,kind)
            if entry.get('origin_experiment')=='meme-v3' and kind not in PHASE_LABELS:kind_label+=' (arşiv V3)'
            lines.append(f"| {entry['symbol']} | {entry['chain']} | {kind_label} | {time_label(reference['observed_ms'])} | {reference['price']:.8g} | {' | '.join(returns)} |")
    lines+=['','## Veri kapsamı ve eksikler','',
            'Getiri sütunları hedef sürelerdir. Parantezdeki +dakika gerçek fiyat gözleminin hedefe gecikmesidir; tam 15/30/60 dakikalık mum getirisi olduğu iddia edilmez. Geçerli gözlem penceresi kaçırılırsa sonuç boş kalır.','',
            'Her ağda yalnız yeni havuz akışı sınırlı sayfalarla okunur. Önceki izlenen havuzlar kalıcı kayıttan yenilenir. Ham keşif ve sosyal gözlem tokenleri aday listesinde gösterilmez. Ücretli profil/boost olumlu sinyal sayılmaz. Aynı simge farklı kontratlarda birleştirilmez.','',
            '5 dk erken aday: üç tam kapalı5dk taban mumu ve sonraki kapalı5dk hacim mumu gerekir (yaklaşık20–25dk + veri/çalışma gecikmesi). 15 dk fiyat teyidi ve ayrıca5dk alım akışı: üç tam kapalı15dk mum gerekir (yaklaşık 45–60 dk + gecikme); erken bildirim için beklenmez. İki aşama kendi gerçek gözlem fiyatıyla ayrı ölçülür, aynı token iki bağımsız başarı sayılmaz. 15 dk teyit daha yüksek başarı veya kontrat güvenliği kanıtı değildir. Başlangıç havuz verisi tokenin tüm geçmişini kapsamaz.','',
            'Bubblemaps haritasını kullanıcı manuel inceler; API anahtarı gerekmez. Hiçbir kayıt otomatik veya manuel harita onayı almış sayılmaz. Robinhood/HyperEVM harita desteği bu sürümde doğrulanmadığından genel uygulama bağlantısı verilir; uygun ağ/harita bulunamazsa bu kontrol eksik kalır. RPC veya güvenlik kaynağının ağ desteği yoksa o ağda fiyat/havuz takibi sürer; eksik otomatik teyitle aday bildirilmez.','',
            'Büyük alıcı desteği zorunlu filtre değildir: 15/30 dk işlem örneğinde adres başına net alım en az max(500 USD, havuz likiditesi × 0.005). Deneysel 0–10 puan olasılık/servet/akıllı para kanıtı değildir. Tek adres >%50 alım hacmi veya büyük alıcıda >=%50 geri satış puanı sıfırlar; eksik/kesilmiş veri bilinmiyor. Bilinen dev/havuz/vault/yakım adresleri çıkarılır; diğer adreslerin bağlantısı doğrulanmaz.','',
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


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['worker','cycle']);p.add_argument('--minutes',type=int,default=110);args=p.parse_args();bind()
    if not 1<=args.minutes<=110:raise ValueError('Bounded worker duration1..110 minutes')
    if args.phase=='cycle':cycle()
    else:worker(args.minutes)
