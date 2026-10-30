"""Meme V7: continuous discovery feed, explicit queues, radar/entry/exit separation."""
from copy import deepcopy
from collections import Counter
from pathlib import Path
import argparse,hashlib,json,os,sys,time,traceback
from concurrent.futures import ThreadPoolExecutor,as_completed
import meme_sources as source
import meme_security as security
import meme_rules as rules
import meme_base_volume as base_volume
import meme_large_buyers as large_buyers
import meme_scan as legacy
import github_scan as cloud
import meme_v7_model as model
import meme_v7_discovery as discovery
import meme_v7_routes as routes
from meme_v7_persistence import SafePublisher,PublicationError,clean

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'cloud_output_meme_v7';STATE=OUT/'state.json'
BRANCH='scanner-state-meme-v7';ARCHIVE_BRANCH='scanner-state-meme-v6';OLD_FP='6125b19ab15e06089dabf2bf29605e95c0211c75678f202917710aec4cc63c82'
def now_ms():return int(time.time()*1000)
def config():return json.loads((ROOT/'meme_v7_config.json').read_text(encoding='utf-8'))
def fingerprint():
    h=hashlib.sha256()
    for n in ('meme_v7.py','meme_v7_model.py','meme_v7_discovery.py','meme_v7_routes.py','meme_v7_config.json',
              'meme_sources.py','meme_security.py','meme_rules.py','meme_base_volume.py','meme_hybrid.py','meme_large_buyers.py','meme_followup_watch.py'):
        h.update(n.encode());h.update((ROOT/n).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return h.hexdigest()
def new_state():return {'version':'meme-v7','rules_fingerprint':fingerprint(),'ledger':{},'assets':{},'entries':{},'events':{},'receipts':{},'cases':{},'runs':[]}
def seed(old,sha):
    if old.get('version')!='meme-v6-pipeline' or old.get('rules_fingerprint')!=OLD_FP:raise ValueError('Unexpected V6 archive identity')
    s=new_state();s['archive']={'branch':ARCHIVE_BRANCH,'sha':sha,'fingerprint':OLD_FP,'entries':len(old['entries']),
        'receipts':len(old['delivery_receipts']),'note':'Immutable V6 SHA; old references are not V7 signals.'}
    s['legacy_v6']={k:deepcopy(old.get(k)) for k in ('entries','paper_v5','delivery_receipts','previous_v5')}
    for r in old['assets'].values():
        a=r['latest'];discovery.remember_identity(s,a['chain'],a['mint'],a['pool'],a.get('pool_created_ms'),r['first_seen_ms'])
    return s
def bind():
    if os.environ.setdefault('SCANNER_STATE_BRANCH',BRANCH)!=BRANCH:raise ValueError('Independent V7 branch required')
    cloud.OUT=OUT;cloud.STATE=STATE;cloud.fingerprint=fingerprint;cloud.new_state=new_state
def restore():
    bind();cloud.pull_state();s=json.loads(STATE.read_text(encoding='utf-8'))
    if not (OUT/'parent.txt').read_text(encoding='ascii').strip():
        cloud.git('fetch','--no-tags','origin','refs/heads/'+ARCHIVE_BRANCH);sha=cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
        s=seed(json.loads(cloud.git('show',sha+':state.json').stdout),sha)
    return s

class Client(base_volume.Client):
    def __init__(self,cfg,backoff_until=0):
        super().__init__(cfg,backoff_until);self.deadline=time.monotonic()+150
    def request(self,*args,**kwargs):
        if time.monotonic()>self.deadline:raise RuntimeError('cycle_data_budget_deferred_not_complete_coverage')
        return super().request(*args,**kwargs)

def save(s):cloud.save(STATE,s)
def checkpoint(s,publisher):
    render(s);save(s);commit=publisher.publish()
    health=json.loads(publisher.health.read_text(encoding='utf-8'))
    s['publication']={'commit':commit,'success_ms':health['time_ms'],'attempts':health['attempts']}

def archive_cold_identities(s,stamp):
    # Only after a real successful snapshot. Full old rows remain in its immutable ancestor SHA.
    sha=s.get('publication',{}).get('commit')
    if not sha:return
    cold=[]
    for k,r in s['ledger'].items():
        newest=max(p['created_ms'] for p in r['pools'].values())
        e=s.get('entries',{}).get(k,{}).get('references',{}).get('entry_5m')
        if stamp-newest>26*3600000 and (not e or stamp-e['observed_ms']>25*3600000):cold.append(k)
    if not cold:return
    s.setdefault('cold_archives',[]).append({'source_state_sha':sha,'archived_ms':stamp,'keys':cold,'count':len(cold),
        'note':'Full identity/decision history retained in immutable ancestor state.json and local collector SQLite.'})
    for k in cold:s['ledger'].pop(k);s['assets'].pop(k,None)

def remember(s,a,cfg,stamp):
    k=model.key(a);discovery.remember_identity(s,a['chain'],a['mint'],a['pool'],a.get('pool_created_ms'),stamp)
    rec=s['assets'].setdefault(k,{'first_seen_ms':stamp,'observations':[]})
    # A selected pool change cannot reset a first base or an entry's original identity.
    rec['latest']=a;rec['observations'].append({'ms':a['price_observed_ms'],'price':a['price_usd'],'liquidity':a.get('liquidity_usd')})
    rec['observations']=rec['observations'][-360:]
    gate=model.market(a,cfg,stamp);rec['market']=gate;act=model.activity(a,cfg);rec['activity']=act
    if gate['passed'] and 'eligible_since_ms' not in rec:rec['eligible_since_ms']=a['price_observed_ms'];rec['eligible_pool']=a['pool']
    if rec.get('eligible_pool') and rec['eligible_pool']!=a['pool']:rec['identity_warning']='eligible_pool_changed_not_new_independent_token'
    return rec

def reference(s,a,phase,details):
    k=model.key(a);e=s['entries'].setdefault(k,{'chain':a['chain'],'mint':a['mint'],'symbol':a['symbol'],'first_pool':a['pool'],
        'references':{},'highest_observed_price':a['price_usd']})
    ref=e['references'].setdefault(phase,{'observed_ms':a['price_observed_ms'],'price':a['price_usd'],'pool':a['pool'],
        'stage':phase,'outcomes':{},'experiment':'meme-v7','details':deepcopy(details)})
    return ref

def handle_market(s,a,rec,cfg,stamp):
    k=model.key(a);gate=rec['market'];act=rec['activity'];sec=rec.get('security',{})
    if not gate['passed']:
        discovery.decision(s,a,stamp,'market_rejected_or_unknown',gate['failed']+gate['unknown']);return
    if sec.get('blocked') or rec.get('developer',{}).get('status')=='outgoing_transfer_detected':
        discovery.decision(s,a,stamp,'risk_blocked',['known_risk_block']);return
    if act['passed'] and not rec.get('dump_disqualified'):
        new_this_cycle=s.setdefault('_radars_this_cycle',0)
        if new_this_cycle<cfg['v7']['radar_per_cycle_limit']:
            ev=model.event(s,a,'early_radar',a['price_observed_ms'],{'activity':act,'security_status':'not_entry_security_may_be_pending',
                'manual_wallet_map':'required','buy_volume_verified':False},cfg['v7']['radar_hourly_limit'])
            if ev:reference(s,a,'early_radar',ev['details']);s['_radars_this_cycle']=new_this_cycle+1
    discovery.decision(s,a,stamp,'candle_queue',['waiting_closed_candles_and_security'])

def evaluate(s,rec,client,cfg,stamp):
    a=rec['latest'];k=model.key(a);net=cfg['networks'][a['chain']];rec['last_candle_attempt_ms']=stamp
    raw=source.candles(client,net,a,stamp);setup=model.first_base(raw,a,rec,now_ms(),cfg);rec['setup']=setup
    if setup.get('first_base'):rec.setdefault('first_base',setup['first_base'])
    if setup.get('latch_dump'):rec.setdefault('dump_disqualified',{'observed_ms':stamp,'reason':setup['reason']})
    if 'entry_5m' in s.get('entries',{}).get(k,{}).get('references',{}):
        entry=s['entries'][k]['references']['entry_5m']
        if k in s['receipts'].get('entry_keys',[]) and model.strengthened(raw,entry['details'],now_ms()):
            model.event(s,a,'confirmed_15m',a['price_observed_ms'],{'entry_observed_ms':entry['observed_ms'],'same_entry_cohort':True})
        return
    if setup['stage'] is None:
        discovery.decision(s,a,stamp,'setup_wait_or_reject',[setup['reason']]);return
    sec=security.fetch_security(client,net,a);rec['security']=sec;rec['security_checked_ms']=now_ms()
    maps=security.fetch_map(client,a,sec,now_ms(),net);rec['maps']=maps
    dev=security.developer_check(client,net,a,sec,now_ms()) if not sec.get('blocked') else {'status':'unknown','reason':'security_blocked'}
    rec['developer']=dev
    gate=model.market(a,cfg,now_ms());risk_tier=rules.tier(gate,setup,sec,dev,maps,cfg['risk']['wallet_map_mode'])
    pressure={'status':'unknown','reasons':['security_or_developer_not_complete']};route={'status':'unknown','reason':'buy_flow_not_verified'}
    if risk_tier=='qualified':
        payload=client.gecko(f"networks/{net['gecko']}/pools/{a['pool']}/trades?token={a['mint']}&include_anomalous=true")
        pressure=base_volume.pressure(payload,a,sec,setup,now_ms(),cfg)
        rec['large_buyers']=large_buyers.assess(payload,a,sec,now_ms(),cfg)
        if pressure['status']=='passed':route=routes.roundtrip(client,net,a,sec,cfg)
    rec.update(buy_pressure=pressure,roundtrip=route)
    # New actual exact-pool price and cap after all checks, never the older candle close.
    if pressure['status']=='passed':
        fresh=discovery.dex_quotes(client,a['chain'],net,[a['mint']],now_ms(),{a['mint']:a['pool']})
        if len(fresh)!=1:raise ValueError('Fresh candidate exact pool unavailable')
        a=fresh[0];rec['latest']=a
    guard=model.entry_guard(a,setup,pressure,sec,dev,maps,route,cfg,now_ms());rec['entry_guard']=guard
    discovery.decision(s,a,now_ms(),'entry_ready' if guard['passed'] else 'entry_rejected_or_unknown',guard['failed']+guard['unknown'])
    if not guard['passed']:return
    details={'observed_ms':a['price_observed_ms'],'base':setup['first_base'],'setup':setup,'risk':guard,'buy_pressure':pressure,
        'security':sec,'developer':dev,'maps':maps,'roundtrip':route,'large_buyers':rec.get('large_buyers'),
        'manual_checks':['wallet_map','official_contract_identity'],'route':'base_pressure' if setup['stage']=='accumulation' else 'first_base_breakout'}
    ev=model.event(s,a,'entry_5m',a['price_observed_ms'],details)
    if ev:
        reference(s,a,'entry_5m',details)
        s['cases'][k]={'chain':a['chain'],'mint':a['mint'],'pool':a['pool'],'symbol':a['symbol'],'observed_ms':a['price_observed_ms'],
            'entry_price':a['price_usd'],'token_output_raw':route['token_output_raw'],'entry_input_usd':route['entry_input_usd'],
            'entry_quote':deepcopy(route),'risk':guard,'base':setup['first_base'],'marks':[],'outcomes':{},'status':'open_indicative',
            'entry_event_id':ev['id'],'actual_fill_verified':False,'net_realized_pnl_usd':None}

def follow(s,rec,client,cfg,stamp):
    a=rec['latest'];k=model.key(a);case=s['cases'].get(k)
    if not case:return
    delivered=k in s['receipts'].get('entry_keys',[])
    try:q=routes.exit_fixed(client,a,case)
    except Exception as exc:q={'observed_ms':stamp,'status':'unknown','reason':str(exc),'net_realized_pnl_usd':None}
    case['marks']=(case['marks']+[q])[-360:]
    if q.get('gross_quote_return_pct') is not None:
        value=q['gross_quote_return_pct'];case['min_observed_quote_return_pct']=min(case.get('min_observed_quote_return_pct',0),value)
        case['max_observed_quote_return_pct']=max(case.get('max_observed_quote_return_pct',0),value)
    for h in cfg['measurement']['horizons_minutes']:
        if str(h) in case['outcomes'] or stamp<case['observed_ms']+h*60000:continue
        lag=stamp-case['observed_ms']-h*60000
        case['outcomes'][str(h)]={'observed_ms':stamp,'delay_ms':lag,'quote':deepcopy(q) if lag<=7*60000 else None,
            'status':'observed_indicative' if lag<=7*60000 and 'gross_quote_return_pct' in q else 'unknown_or_late','net_realized_pnl_usd':None}
    reason=None
    gross=q.get('gross_quote_return_pct')
    if gross is not None and gross>=2*case['risk']['risk_pct']+cfg['v7']['additional_cost_assumption_pct']:reason='target_observed'
    if a['price_usd']<case['risk']['stop_reference']:reason='structure_lost'
    if gross is not None and gross<=-case['risk']['risk_pct']:reason='structure_lost'
    recent=[o['liquidity'] for o in rec['observations'] if o.get('liquidity') and 0<=stamp-o['ms']<=3600000]
    if recent and a.get('liquidity_usd') is not None and a['liquidity_usd']<max(recent)*.8:reason='liquidity_loss'
    if rec.get('security',{}).get('blocked') or rec.get('developer',{}).get('status')=='outgoing_transfer_detected':reason='risk_detected'
    if case['status']=='open_indicative' and stamp-case['observed_ms']>=cfg['pipeline']['exit_timeout_minutes']*60000:reason=reason or 'exit_timeout'
    if reason and delivered:
        model.event(s,a,reason,a['price_observed_ms'],{'entry_observed_ms':case['observed_ms'],'exit_quote':q,'same_entry_cohort':True})
        case['status']='closed_indicative';case.setdefault('exit_reference',{'reason':reason,'observed_ms':stamp,'quote':deepcopy(q)})
    if delivered and case['status']=='open_indicative' and rec['activity']['buys5'] is not None and rec['activity']['sells5'] is not None:
        buys=rec['activity']['buys5'];sells=rec['activity']['sells5']
        if buys+sells>=12 and buys/(buys+sells)<.4:model.event(s,a,'buy_pressure_weakening',a['price_observed_ms'],
            {'entry_observed_ms':case['observed_ms'],'scope':'buy_count_share_not_buy_volume','activity':rec['activity']})

def scan(s,cfg):
    if s['rules_fingerprint']!=fingerprint():raise ValueError('V7 fingerprint mismatch')
    started=now_ms();client=Client(cfg,s.get('provider_backoff_until_ms',0));s['_radars_this_cycle']=0
    coverage=discovery.discover(s,client,cfg,started);errors=[];groups={};quotes=[]
    for chain,net in cfg['networks'].items():
        requested=discovery.quote_plan(s,chain,cfg,now_ms());pinned={r['mint']:r['pool'] for r in s['cases'].values() if r['chain']==chain}
        try:
            rows=discovery.dex_quotes(client,chain,net,requested,now_ms(),pinned) if requested else []
            quotes+=rows;groups[chain]={'requested_quotes':len(requested),'fresh_quotes':len(rows),'quote_unknown':len(set(requested)-{a['mint'] for a in rows})}
            for mint in set(requested)-{a['mint'] for a in rows}:
                s['ledger'][chain+':'+mint].update(status='quote_unknown',reasons=['no_exact_token_pool_quote'])
        except Exception as exc:errors.append(chain+': '+str(exc));groups[chain]={'requested_quotes':len(requested),'error':str(exc)}
    for a in quotes:
        rec=remember(s,a,cfg,now_ms());legacy.measure_entries(s,rec,cfg);handle_market(s,a,rec,cfg,now_ms())
    targets=[r for r in s['assets'].values() if r.get('market',{}).get('passed') and 0<=now_ms()-r['latest']['price_observed_ms']<=120000 and not r.get('dump_disqualified')]
    targets.sort(key=lambda r:(0 if model.key(r['latest']) in s['receipts'].get('entry_keys',[]) else 1,r.get('last_candle_attempt_ms',0),r['first_seen_ms']))
    evaluated=0
    for rec in targets[:cfg['v7']['candles_per_cycle']]:
        try:evaluate(s,rec,client,cfg,now_ms());evaluated+=1
        except Exception as exc:
            errors.append(model.key(rec['latest'])+': '+str(exc));discovery.decision(s,rec['latest'],now_ms(),'data_unknown',[str(exc)])
    # Quote actual fixed hypothetical quantities and recheck known risks for delivered entries.
    follow_targets=[s['assets'][k] for k in s['cases'] if k in s['assets'] and 0<=now_ms()-s['assets'][k]['latest']['price_observed_ms']<=120000]
    follow_targets.sort(key=lambda r:r.get('last_follow_ms',0))
    for rec in follow_targets[:2]:
        rec['last_follow_ms']=now_ms();a=rec['latest']
        if now_ms()-rec.get('security_checked_ms',0)>=cfg['risk']['security_cache_max_minutes']*60000:
            try:
                rec['security']=security.fetch_security(client,cfg['networks'][a['chain']],a);rec['security_checked_ms']=now_ms()
                rec['developer']=security.developer_check(client,cfg['networks'][a['chain']],a,rec['security'],now_ms())
            except Exception as exc:rec['risk_refresh_error']={'observed_ms':now_ms(),'reason':str(exc)}
        follow(s,rec,client,cfg,now_ms())
    if client.rate_limited:s['provider_backoff_until_ms']=now_ms()+900000
    finished=now_ms();s.pop('_radars_this_cycle',None)
    run={'started_ms':started,'scan_finished_ms':finished,'session_id':os.environ.get('GITHUB_RUN_ID','local'),
         'errors':errors,'discovery_mode':coverage['mode'],'candles_evaluated':evaluated,'selected_for_candles':min(len(targets),cfg['v7']['candles_per_cycle']),
         'candles_budget_waiting':max(0,len(targets)-cfg['v7']['candles_per_cycle']),'groups':groups,'requests':dict(client.stats)}
    s['runs'].append(run);s['runs']=s['runs'][-2000:];s['last_scan']={'discovery':coverage,**run};s['updated_ms']=finished
    return client

def event_body(e):
    phase=e['phase'];d=e['details'];head=model.LABELS[phase]+' · '+legacy.safe_symbol(e['symbol'])+' · '+e['chain']
    lines=[head,'','Ağ: '+e['chain'],'','Kontrat / token adresi (kopyala):','```text',e['mint'],'```','',
        'Gerçek gözlem: '+legacy.time_label(e['observed_ms'])+' TR',f"Fiyat ${e['price']:.8g}; MCAP ${e['market_cap_usd']:.0f}; likidite ${e['liquidity_usd']:.0f}.",'']
    if phase=='early_radar':lines+=['**İZLEME UYARISI. Giriş teyidi değildir. Güvenlik ve geliştirici denetimleri tamamlanmamış olabilir.**',
        'Son 5dk işlem adedi/hacim faaliyeti: '+json.dumps(d['activity'],ensure_ascii=False),
        'Alım adedi payı alım hacmi, balina veya bağımsız yatırımcı kanıtı değildir.']
    elif phase=='entry_5m':
        risk=d['risk'];lines+=['**Otomatik giriş ölçütleri sağlandı; manuel cüzdan haritası ve resmî kontrat kimliği kontrolü bekler.**',
            f"Stop referansı ${risk['stop_reference']:.8g}; risk mesafesi %{risk['risk_pct']:.2f}; 2R senaryo hedefi ${risk['target_projection']:.8g}.",
            'Hedef doğrulanmış direnç alanı veya gerçekleşme sözü değildir; ilave maliyet varsayımı %'+str(risk['additional_cost_assumption_pct'])+'.',
            base_volume.text(d['buy_pressure']),large_buyers.text(d.get('large_buyers')),
            'Alış/satış gösterge kotasyon kaybı: %'+str(round(d['roundtrip']['roundtrip_loss_pct'],2))+'. Gerçek alış/satış, tüm maliyetler ve net kâr doğrulanmadı.',
            'Dev kontrolü yalnız bildirilen oluşturucu ve tam taranabilen son45dk penceresi; bağlı tüm cüzdanlar veya ömür boyu satış geçmişi değildir.']
    else:lines+=['Önceden bildirilen aynı girişin devam/çıkış izlemesidir; yeni bağımsız işlem değildir.',json.dumps(d,ensure_ascii=False)]
    net=config()['networks'][e['chain']]
    lines+=['','Bubblemaps: https://app.bubblemaps.io/'+{'solana':'sol','ethereum':'eth','bnb':'bsc','robinhood':'robinhood','hyperevm':'hyperevm'}[e['chain']]+'/token/'+e['mint'],
        'DexScreener: https://dexscreener.com/'+net['dex']+'/'+e['pool'],'','GMGN kullanılmaz. Gösterge kotasyonları satış veya getiri garantisi değildir.',
        '<!-- coin-tarama-meme-v7:'+e['id']+' -->']
    return head,'\n'.join(lines)

def notify(s,cfg):
    pending=[e for i,e in s['events'].items() if i not in s['receipts'] and not e.get('notification_expired_ms')]
    if not pending:return
    repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN');user=os.environ.get('COIN_NOTIFY_USER','')
    if repo!='selvisezgin01-ux/Coin-Tarama' or not token:raise ValueError('Fixed repository notification credentials unavailable')
    url='https://api.github.com/repos/'+repo+'/issues';headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'}
    existing=cloud.http_json(url+'?state=all&sort=created&direction=desc&per_page=100',headers=headers,label='Meme V7 notifications')
    for e in pending:
        marker='<!-- coin-tarama-meme-v7:'+e['id']+' -->';found=next((i for i in existing if marker in (i.get('body') or '') and i.get('user',{}).get('login')=='github-actions[bot]'),None)
        if not found:
            if not 0<=now_ms()-e['observed_ms']<=cfg['pipeline']['notification_max_age_minutes']*60000:e['notification_expired_ms']=now_ms();continue
            rec=s['assets'].get(e['key'],{})
            if e['phase'] in ('early_radar','entry_5m') and (rec.get('dump_disqualified') or rec.get('security',{}).get('blocked') or rec.get('developer',{}).get('status')=='outgoing_transfer_detected'):
                e['notification_expired_ms']=now_ms();e['notification_expiry_reason']='new_risk_before_delivery';continue
            if e['phase']=='entry_5m':
                validator=source.Client(cfg);net=cfg['networks'][e['chain']]
                fresh=discovery.dex_quotes(validator,e['chain'],net,[e['mint']],now_ms(),{e['mint']:e['pool']})
                d=e['details']
                validation=model.entry_guard(fresh[0],d['setup'],d['buy_pressure'],d['security'],d['developer'],d['maps'],d['roundtrip'],cfg,now_ms()) if len(fresh)==1 else {'passed':False}
                if not validation['passed'] or fresh[0]['price_usd']>e['price']*1.02:
                    e['notification_expired_ms']=now_ms();e['notification_expiry_reason']='fresh_delivery_revalidation_failed';continue
                e['delivery_validation']={'checked_ms':now_ms(),'price':fresh[0]['price_usd'],'original_reference_preserved':True}
            title,body=event_body(e)
            if user:
                if not __import__('re').fullmatch('[A-Za-z0-9-]{1,39}',user):raise ValueError('Invalid notification recipient')
                body='@'+user+'\n\n'+body
            found=cloud.http_json(url,{'title':'Coin Tarama Meme V7 · '+title,'body':body},headers,label='Meme V7 notifications')
            existing.insert(0,found)
        s['receipts'][e['id']]={'event_id':e['id'],'key':e['key'],'phase':e['phase'],'observed_ms':e['observed_ms'],
            'issue_number':found['number'],'issue_url':found['html_url'],'issue_created_at':found.get('created_at'),'recorded_ms':now_ms()}
        if e['phase']=='entry_5m' and e['key'] not in s['receipts'].setdefault('entry_keys',[]):s['receipts']['entry_keys'].append(e['key'])
        save(s) # Same event marker reconciles a lost response/checkpoint; never new observation prices.

def render(s):
    lines=['# Coin Tarama Meme — V7','', 'Son gözlem: '+legacy.time_label(s.get('updated_ms',now_ms()))+' TR','',
        '🟡 Erken radar: giriş değildir. 🟢🎯 Otomatik giriş ölçütleri: manuel harita/kontrat kontrolü bekler. 🔵 15dk güçlenme: aynı girişin devamı.',
        'Beş ağ korunur: Solana, Ethereum, BNB Chain, Robinhood ve HyperEVM. Yeni havuz yaşı tokenin tüm yaşamı değildir.',
        'MCAP 50–500bin USD; FDV yerine geçmez. İlk gerçek V7 uygunluk gözleminden sonraki 2tam5dk taban ve ayrı kapalı5dk hacim mumu aranır. İlk haber için bu mumlar beklenmez.',
        'İlk fiyattan %25 yükseliş yasağı V7 koşulu değildir. Seçilen havuzun erişilen geçmişindeki sert düşüş, ilk taban kaybı, tabandan uzama ve güvenlik engelleri ayrı değerlendirilir. Başlangıç/ara geçmiş eksikse giriş teyitsizdir.',
        'İlk likit taban geçmiş MCAP varsayımıyla geriye taşınmaz. Bilinmeyen risk/akış/kotasyon yeşil giriş olmaz. Eski V6 kayıtları yeni V7 başarısı sayılmaz.','',
        '## Keşif ve kapsam','',json.dumps(s.get('last_scan',{}),ensure_ascii=False,indent=2),'',
        'Sürekli keşif toplayıcısı ayrı yerel süreçtir; bilgisayar uyursa/kapanırsa kesilir. Bayat/yok feed halinde sınırlı GitHub keşfi açıkça fallback sayılır. Tam zincir kapsamı veya kesintisiz1dk sözü yoktur.',
        'Kimlik defteri: '+str(len(s['ledger']))+' token; ayrıntılı fiyat/mum okumaları bütçelidir. Kota nedeniyle bekleyen kimlikler sessizce silinmez.','',
        '## Bildirim evreleri','', '| Evre | Token | Ağ | Gözlem TR | MCAP USD | Bildirim |','|---|---|---|---|---:|---|']
    for e in sorted(s['events'].values(),key=lambda e:e['observed_ms'],reverse=True):
        rec=s['receipts'].get(e['id']);receipt='Bekliyor' if not rec else '[Issue #'+str(rec['issue_number'])+']('+rec['issue_url']+')'
        if e.get('notification_expired_ms'):receipt='Bayat/iptal — gönderilmedi'
        lines.append(f"| {model.LABELS[e['phase']]} | {legacy.safe_symbol(e['symbol'])} `{e['mint']}` | {e['chain']} | {legacy.time_label(e['observed_ms'])} | {e.get('market_cap_usd')} | {receipt} |")
    lines+=['','## Kontrat başına son karar','', '| Kontrat | Durum | Neden |','|---|---|---|']
    for k,r in sorted(s['ledger'].items()):lines.append('| `'+k+'` | '+r['status']+' | '+', '.join(r.get('reasons',[])).replace('|','/')+' |')
    lines+=['','## Gerçek gözlem ve varsayımsal sabit miktar ölçümleri','',
        'Aynı ağ+kontrat bütün evre/havuzlarda aynı bağımlı örnektir. Radar, giriş ve güçlenme ayrı bağımsız kazanç sayılmaz.',
        'Kotasyonda alınabileceği varsayılan token miktarı sabitlenir; gerçek alım yoktur. Sonraki satış kotasyonları ve %0.2/%0.5/%1 ilave maliyet senaryoları kaydedilir. Gas/tax/fill bilinmiyorsa gerçekleşmiş net kâr bilinmiyor kalır. Ara yol/stop-hedef sırası tam bilinmez.','']
    for k,c in s['cases'].items():lines+=['### '+k,json.dumps(c,ensure_ascii=False,indent=2)]
    lines+=['','V6 arşivi: '+json.dumps(s.get('archive',{}),ensure_ascii=False),'',
        'İlk değerlendirme 50–100farklı kontratta ileriye dönük örnek hedefler; bu sayı kârlılık kanıtı veya sabit bitiş tarihi değildir.']
    OUT.mkdir(exist_ok=True,parents=True);(OUT/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    cloud.save(OUT/'summary.json',{'version':s['version'],'rules_fingerprint':s['rules_fingerprint'],'last_scan':s.get('last_scan'),
        'identities':len(s['ledger']),'events':dict(Counter(e['phase'] for e in s['events'].values())),
        'entry_unique_contracts':len(s['cases']),'archive':s.get('archive'),'publication':s.get('publication')})

def worker(minutes):
    if not 1<=minutes<=110:raise ValueError('Bounded session required')
    cfg=config();s=restore();pub=SafePublisher(ROOT,OUT,fingerprint(),os.environ.get('GITHUB_RUN_ID','local'))
    parent=(OUT/'parent.txt').read_text(encoding='ascii').strip();s=pub.recover_local(s,parent)
    deadline=time.monotonic()+minutes*60;completed=0
    checkpoint(s,pub)
    while time.monotonic()<deadline:
        started=time.monotonic();scan(s,cfg);checkpoint(s,pub);archive_cold_identities(s,now_ms())
        try:notify(s,cfg)
        finally:
            s['runs'][-1]['finished_ms']=now_ms();checkpoint(s,pub)
        completed+=1;print(json.dumps({'completed_cycles':completed,'last_scan':s['last_scan']},ensure_ascii=True),flush=True)
        wait=max(0,cfg['pipeline']['worker_interval_seconds']-(time.monotonic()-started))
        if time.monotonic()+wait>=deadline:break
        time.sleep(wait)
    if completed==0:raise RuntimeError('No completed V7 cycle')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['worker']);p.add_argument('--minutes',type=int,default=110);a=p.parse_args()
    try:worker(a.minutes)
    except PublicationError as exc:print(clean(exc),flush=True);sys.exit(75 if exc.restart_allowed else 78)
