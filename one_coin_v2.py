"""Exact-mint public watch; swaps are not transfers, snapshots are not a complete ledger."""
import hashlib,json,math,re,time,statistics
from copy import deepcopy
import one_coin_analytics as analytics
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.request import Request,build_opener,HTTPRedirectHandler
from urllib.parse import urlsplit
from urllib.error import HTTPError

ROOT=Path(__file__).resolve().parent
def config():return json.loads((ROOT/'one_coin_v2_config.json').read_text(encoding='utf-8'))
def now():return int(time.time()*1000)
def stamp(ms):return datetime.fromtimestamp(ms/1000,ZoneInfo('Europe/Istanbul')).strftime('%d.%m.%Y %H:%M:%S')+' TR'
def number(v):
    try:
        n=float(v)
        return n if math.isfinite(n) else None
    except (ValueError,TypeError):return None
def address(x):return isinstance(x,str) and re.fullmatch(r'[1-9A-HJ-NP-Za-km-z]{32,44}',x) is not None
def fingerprint():
    return hashlib.sha256(b''.join((ROOT/n).read_text(encoding='utf-8').replace('\r\n','\n').encode() for n in ['one_coin_v2_config.json','one_coin_v2.py','one_coin_v2_worker.py','one_coin_analytics.py'])).hexdigest()
def new_state():
    cfg=config()
    return {'version':cfg['version'],'rules_fingerprint':fingerprint(),'created_ms':now(),'tokens':{},'wallets':{w['address']:{**w,'cursor':None,'before':None,'pending_head':None,'seen_signatures':[]} for w in cfg['watched_wallets']},
        'runs':[],'events':[],'pending':[],'delivery':[],'provider_backoff':{},'alerts':{},'transaction_queue':[],
        'coverage':{'full_chain_coverage':False,'wlfi_entire_entity_coverage':False,'related_ownership_verified':False}}

def migrate(old,source_sha):
    if old.get('version')!='1-coin-v1' or old.get('rules_fingerprint')!='778ab62a65e684bb326ffc593f092d340bd76c14bd8ed0be25a56dc446f931b6':raise ValueError('Unexpected V1 archive')
    s=deepcopy(old)
    s['archive']={'source_branch':'scanner-state-1-coin','source_sha':source_sha,'canonical_sha256':hashlib.sha256(json.dumps(old,sort_keys=True,allow_nan=False).encode()).hexdigest(),
        'old_events':deepcopy(old['events']),'old_delivery':deepcopy(old['delivery']),'old_pending':deepcopy(old['pending']),'old_created_ms':old['created_ms']}
    s.update(version=config()['version'],rules_fingerprint=fingerprint(),created_ms=now(),notification_start_ms=now(),runs=[],events=[],pending=[],delivery=[],alerts={},startup_recorded=False,quiet_alerts={})
    s.pop('timing',None)
    return s

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*a,**k):return None
class Public:
    def __init__(self,s,cfg):self.s=s;self.cfg=cfg;self.last={};self.requests={};self.opener=build_opener(NoRedirect());self.rpc_deadline=time.monotonic()+150
    def get(self,url,payload=None):
        host=urlsplit(url).hostname
        method=payload.get('method') if isinstance(payload,dict) else None
        scoped=host+':'+method if method else host
        if urlsplit(url).scheme!='https' or host not in {'api.dexscreener.com','api.geckoterminal.com','api.rugcheck.xyz','api.mainnet.solana.com'}:raise ValueError('Unapproved public provider')
        if self.s['provider_backoff'].get(host,0)>now():raise RuntimeError(host+': erişim beklemesi sürüyor')
        if self.s['provider_backoff'].get(scoped,0)>now():raise RuntimeError(scoped+': yöntem erişimi kapalı; diğer izinli okumalar bağımsız sürer')
        delay={'api.geckoterminal.com':13,'api.mainnet.solana.com':2}.get(host,.4)
        time.sleep(max(0,self.last.get(host,0)+delay-time.monotonic()))
        self.last[host]=time.monotonic()
        req=Request(url,data=None if payload is None else json.dumps(payload).encode(),headers={'User-Agent':'Coin-1-watch/1','Accept':'application/json','Content-Type':'application/json'})
        try:
            with self.opener.open(req,timeout=self.cfg['http_timeout_seconds']) as r:data=json.load(r)
            self.requests[host]=self.requests.get(host,0)+1
            if isinstance(data,dict) and data.get('error'):
                code=data['error'].get('code') if isinstance(data['error'],dict) else None
                if code in (429,-32429):self.s['provider_backoff'][host]=now()+self.cfg['provider_backoff_seconds']*1000
                if method and code in (-32010,-32601):self.s['provider_backoff'][scoped]=now()+86400000
                raise RuntimeError(host+': RPC error '+str(code))
            return data
        except HTTPError as e:
            # PublicNode serves wallet signatures but denies expensive largest-account
            # reads on its public tier. Respect that denial without blocking other
            # independently permitted RPC methods. Global429 still stops all calls.
            if e.code==403 and method:self.s['provider_backoff'][scoped]=now()+86400000
            elif e.code in (401,403,418,429):self.s['provider_backoff'][host]=now()+self.cfg['provider_backoff_seconds']*1000
            raise RuntimeError(host+': HTTP '+str(e.code)) from None
    def rpc(self,method,params):
        if method not in {'getTokenAccountsByOwner','getMultipleAccounts','getSignaturesForAddress','getTransaction'}:raise ValueError('Only read-only wallet RPC permitted')
        if time.monotonic()>self.rpc_deadline:raise RuntimeError('Wallet read time budget exhausted; remaining data unknown')
        d=self.get(self.cfg['wallet_rpc_url'],{'jsonrpc':'2.0','id':1,'method':method,'params':params})
        if 'result' not in d:raise ValueError('Missing RPC result')
        return d['result']

def event(s,key,mint,kind,text,details=None,observed_ms=None):
    eid=hashlib.sha256(key.encode()).hexdigest()[:28]
    if any(e['id']==eid for e in s['events']):return
    e={'id':eid,'mint':mint,'kind':kind,'observed_ms':observed_ms or now(),'text':text,'details':details or {}}
    s['events'].append(e);s['pending'].append(e)
def health(s,scope,message):
    key=scope+':'+message
    if s['alerts'].get(scope)!=key:
        event(s,'health:'+key+':'+str(now()//86400000),None,'VERİ ERİŞİMİ',scope+': '+message)
    s['alerts'][scope]=key
def recover(s,scope):
    if s['alerts'].pop(scope,None):event(s,'recover:'+scope+':'+str(now()),None,'ERİŞİM DÜZELDİ',scope+' yeniden okunabildi; aradaki boşluk kapanmış sayılmaz.')

def market(rows,mint):
    if not isinstance(rows,list):raise ValueError('Unexpected DexScreener response')
    out=[]
    for r in rows:
        if r.get('chainId')!='solana' or r.get('baseToken',{}).get('address')!=mint or not address(r.get('pairAddress')):continue
        price=number(r.get('priceUsd'));liq=number(r.get('liquidity',{}).get('usd'))
        if price is None or price<=0 or liq is None or liq<=0:continue
        out.append({'pool':r['pairAddress'],'price':price,'liquidity':liq,'market_cap':number(r.get('marketCap')),
            'volume':r.get('volume',{}),'price_change':r.get('priceChange',{}),'txns':r.get('txns',{}),
            'dex':r.get('dexId'),'quote_mint':r.get('quoteToken',{}).get('address')})
    return sorted(out,key=lambda x:-x['liquidity'])

def parse_trades(payload,mint,observed_ms):
    rows=payload.get('data')
    if not isinstance(rows,list):raise ValueError('Unexpected trade sample')
    parsed={};invalid=0;oldest=None
    for r in rows:
        a=r.get('attributes',{});tx=a.get('tx_hash');wallet=a.get('tx_from_address')
        try:t=int(datetime.fromisoformat(a['block_timestamp'].replace('Z','+00:00')).timestamp()*1000)
        except (KeyError,TypeError,ValueError):invalid+=1;continue
        if t>observed_ms+60000 or a.get('is_anomalous') is True:invalid+=1;continue
        oldest=t if oldest is None else min(oldest,t)
        source=a.get('from_token_address');target=a.get('to_token_address');usd=number(a.get('volume_in_usd'))
        if (source==mint)==(target==mint):continue
        if not address(wallet) or not isinstance(tx,str) or not re.fullmatch(r'[1-9A-HJ-NP-Za-km-z]{64,90}',tx) or usd is None or usd<=0:invalid+=1;continue
        side='buy' if target==mint else 'sell'
        key=tx+':'+side
        v={'tx':tx,'wallet':wallet,'side':side,'usd':usd,'block_ms':t,'provider_row_id':r.get('id')}
        # Same signature seen through multiple pools is one sampled swap per direction;
        # retain the largest leg, do not sum routed legs as independent demand.
        if key not in parsed or parsed[key]['usd']<usd:parsed[key]=v
    return list(parsed.values()),{'returned':len(rows),'oldest_ms':oldest,'invalid':invalid,
        'possibly_truncated':len(rows)>=300,'full_chain_coverage':False}

def ingest_trades(s,t,rows,coverage,observed_ms,cfg):
    initial='trade_baseline_ms' not in t
    if initial:t['trade_baseline_ms']=observed_ms
    seen=t.setdefault('seen_trades',{});fresh=[]
    threshold=max(cfg['large_trade_min_usd'],t['market']['liquidity']*cfg['large_trade_liquidity_fraction'])
    merged={}
    for row in rows:
        k=row['tx']+':'+row['side']
        if k not in merged or merged[k]['usd']<row['usd']:merged[k]=row
    for row in sorted(merged.values(),key=lambda x:x['block_ms']):
        key=row['tx']+':'+row['side']
        if key in seen:continue
        seen[key]=row
        # First sample is a baseline, never retroactive alerts from old transactions.
        first=t.setdefault('buyer_first_seen',{})
        first_time=row['wallet'] not in first
        if row['side']=='buy':first.setdefault(row['wallet'],observed_ms)
        if initial or row['block_ms']<max(t['trade_baseline_ms'],s.get('notification_start_ms',0)):continue
        fresh.append(row)
        row['first_buyer_seen_by_this_watch']=row['side']=='buy' and first_time
        kind='BÜYÜK ALIM' if row['side']=='buy' and row['usd']>=threshold else ('ALIM' if row['side']=='buy' else 'SATIŞ')
        notify_floor=analytics.threshold(t,cfg)
        counts=t.setdefault('notification_filter',{'small_trades_logged':0,'meaningful_trades':0})
        if notify_floor is not None and row['usd']>=notify_floor:
            counts['meaningful_trades']+=1
            event(s,t['mint']+':trade:'+key,t['mint'],kind,f"{kind}: ${row['usd']:.2f} · işlem başlatıcı `{row['wallet']}` · bildirim eşiği ${notify_floor:.0f}",row,observed_ms)
        else:counts['small_trades_logged']+=1
        if row['usd']>=threshold and row['wallet'] not in s['wallets']:
            dynamic=sum(w.get('dynamic',False) for w in s['wallets'].values())
            if dynamic<cfg['maximum_dynamic_wallets']:
                s['wallets'][row['wallet']]={'address':row['wallet'],'label':'Büyük örnek işlemin başlatıcısı; servet/kimlik bilinmiyor','dynamic':True,'identity_verified':False,'source':'sampled swap','cursor':None,'before':None,'pending_head':None,'seen_signatures':[]}
            else:health(s,'dynamic_wallet_capacity','Dinamik cüzdan sınırı doldu; bütün yeni alıcı cüzdanları işlem geçmişiyle izlenmiyor.')
    # New means newly observed by this watch; never means a newly created wallet.
    start=observed_ms-900000
    recent=[x for x in seen.values() if x['block_ms']>=start]
    buys=sum(x['usd'] for x in recent if x['side']=='buy');sells=sum(x['usd'] for x in recent if x['side']=='sell')
    t['flow15_sample']={'observed_ms':observed_ms,'buy_usd':buys,'sell_usd':sells,'net_usd':buys-sells,'buy_fraction':buys/(buys+sells) if buys+sells else None,
        'initiators':len({x['wallet'] for x in recent}),'scope':'bounded selected-pool swap sample','coverage':coverage,'new_trades':len(fresh)}
    t['seen_trades']=dict(sorted(seen.items(),key=lambda x:-x[1]['block_ms'])[:20000])

def token_balances(tx,mints):
    meta=tx.get('meta') or {};delta={};maps={}
    for field,sign in [('preTokenBalances',-1),('postTokenBalances',1)]:
        for r in meta.get(field,[]) or []:
            if r.get('mint') not in mints or not address(r.get('owner')):continue
            a=r.get('uiTokenAmount',{});raw=a.get('amount');dec=a.get('decimals')
            if not isinstance(raw,str) or not raw.isdigit() or not isinstance(dec,int):continue
            key=(r['mint'],r['owner']);delta[key]=delta.get(key,0)+sign*int(raw)/10**dec
            maps[r['accountIndex']]=r['owner']
    return [{'mint':m,'owner':o,'change_tokens':v} for (m,o),v in delta.items() if abs(v)>1e-9],maps

def explicit_edges(tx,owners):
    keys=tx.get('transaction',{}).get('message',{}).get('accountKeys',[])
    keys=[x.get('pubkey') if isinstance(x,dict) else x for x in keys]
    by_account={keys[i]:o for i,o in owners.items() if i<len(keys)}
    groups=[tx.get('transaction',{}).get('message',{}).get('instructions',[])]+[x.get('instructions',[]) for x in (tx.get('meta') or {}).get('innerInstructions',[]) or []]
    edges=[]
    for group in groups:
        for ins in group:
            p=ins.get('parsed')
            if not isinstance(p,dict) or p.get('type') not in ('transfer','transferChecked'):continue
            info=p.get('info',{});a=info.get('source');b=info.get('destination')
            if a in by_account and b in by_account:
                edges.append({'source_owner':by_account[a],'destination_owner':by_account[b],'source_token_account':a,'destination_token_account':b,'interpretation':'explicit token transfer; not proof of same ownership or a purchase'})
    return edges

def holder_changes(s,t,values,slot,cfg):
    current={};accounts={};deltas={}
    excluded=set(t.get('excluded_infrastructure',[]))
    for v in values:
        if not isinstance(v,dict):continue
        info=v.get('data',{}).get('parsed',{}).get('info',{})
        owner=info.get('owner');amount=info.get('tokenAmount',{})
        if info.get('mint')!=t['mint'] or not address(owner) or owner in excluded:continue
        raw=amount.get('amount');dec=amount.get('decimals')
        if not isinstance(raw,str) or not raw.isdigit() or not isinstance(dec,int):continue
        amount=int(raw)/10**dec;current[owner]=current.get(owner,0)+amount
        ata=v.get('_account')
        if address(ata):accounts[ata]={'owner':owner,'amount':amount}
    old=t.get('holder_snapshot',{}).get('owners',{})
    old_accounts=t.get('holder_snapshot',{}).get('accounts',{})
    for ata in accounts.keys() & old_accounts.keys():
        a,b=old_accounts[ata],accounts[ata]
        if a['owner']==b['owner']:deltas[b['owner']]=deltas.get(b['owner'],0)+b['amount']-a['amount']
    for owner,delta in deltas.items():
        if abs(delta)<.000001:continue
        text=f"`{owner}` · gözlenen üst token hesaplarında {delta:+.6f} token değişim. Transfer veya alım/satım olabilir; işlem nedeni henüz doğrulanmadı."
        event(s,'holding:'+t['mint']+':'+owner+':'+str(slot),t['mint'],'BÜYÜK HESAP BAKİYESİ',text,{'wallet':owner,'change_tokens':delta,'slot':slot})
    t['holder_snapshot']={'owners':current,'accounts':accounts,'slot':slot,'observed_ms':now(),'coverage':'top20 token accounts; changes compare identical account addresses only, not complete owner balances','new_to_sample':sorted(current.keys()-old.keys()),'dropped_from_sample':sorted(old.keys()-current.keys())}

def legacy_holders(s,client,cfg):
    for t in s['tokens'].values():
        if now()-t.get('holder_attempt_ms',0)<cfg['holder_interval_seconds']*1000:continue
        t['holder_attempt_ms']=now()
        try:
            r=client.rpc('getTokenLargestAccounts',[t['mint'],{'commitment':'finalized'}])
            accounts=[x['address'] for x in r.get('value',[]) if address(x.get('address'))]
            if not accounts:raise ValueError('No largest-account sample returned')
            values=client.rpc('getMultipleAccounts',[accounts,{'encoding':'jsonParsed','commitment':'finalized'}])
            if not isinstance(values.get('value'),list) or not values.get('context',{}).get('slot'):raise ValueError('Missing holder sample or slot')
            annotated=[{**v,'_account':a} if isinstance(v,dict) else None for a,v in zip(accounts,values['value'])]
            holder_changes(s,t,annotated,values['context']['slot'],cfg);recover(s,'holders:'+t['mint'])
        except Exception as e:health(s,'holders:'+t['mint'],str(e))

def watch_wallet(s,w,client,cfg):
    options={'limit':cfg['signatures_per_page'],'commitment':'finalized'}
    if w.get('before'):options['before']=w['before']
    initial=not w.get('baseline_ready',False) and w.get('cursor') is None;found=False;rows=[]
    if initial:w['baseline_ms']=now()
    for page in range(cfg['signature_pages_per_wallet']):
        batch=client.rpc('getSignaturesForAddress',[w['address'],options])
        if not isinstance(batch,list):raise ValueError('Invalid signature response')
        if batch and not w.get('pending_head'):w['pending_head']=batch[0]['signature']
        for r in batch:
            if r['signature']==w.get('cursor'):found=True;break
            if not initial and w.get('cursor') is None and r.get('blockTime') and r['blockTime']*1000<max(w.get('baseline_ms',0),s.get('notification_start_ms',0)):found=True;break
            rows.append(r)
        if found or initial or len(batch)<cfg['signatures_per_page']:found=True;break
        options['before']=batch[-1]['signature']
    known=set(w.get('seen_signatures',[]))
    for r in rows:
        sig=r.get('signature')
        if sig in known:continue
        known.add(sig)
        if initial or (r.get('blockTime') and r['blockTime']*1000<w.get('baseline_ms',0)):continue
        activity={'signature':sig,'wallet':w['address'],'block_ms':r['blockTime']*1000 if isinstance(r.get('blockTime'),(int,float)) else None,'failed':r.get('err') is not None,'label':w['label'],'identity_verified':w.get('identity_verified',False)}
        activity['monitored_owner']=w.get('monitored_owner',w['address'])
        s.setdefault('wallet_activity_log',{})[w['address']+':'+sig]=activity
        if activity['block_ms'] is None or activity['block_ms']<s.get('notification_start_ms',0):continue
        if not activity['failed'] and not any(x['signature']==sig for x in s['transaction_queue']):s['transaction_queue'].append(activity)
    w['seen_signatures']=sorted(known)[-10000:]
    if found:
        w['cursor']=w.get('pending_head') or w.get('cursor');w['before']=None;w['pending_head']=None
    elif rows:
        w['before']=rows[-1]['signature'];health(s,'wallet_pages:'+w['address'],'İşlem sayfalama sınırı; eski kontrol noktasına erişilmedi, sonraki döngüde devam edilecek.')
    w['last_checked_ms']=now();w['baseline_ready']=True

def rpc_watch(s,client,cfg):
    seeds=sorted([w for w in s['wallets'].values() if not w.get('dynamic')],key=lambda w:not w.get('token_account',False))
    dyn=[w for w in s['wallets'].values() if w.get('dynamic')]
    offset=s.get('wallet_rotation',0)
    selected=seeds+[dyn[(offset+i)%len(dyn)] for i in range(min(len(dyn),cfg['dynamic_wallets_per_cycle']))] if dyn else seeds
    s['wallet_rotation']=offset+cfg['dynamic_wallets_per_cycle']
    errors=[]
    for w in selected:
        try:watch_wallet(s,w,client,cfg);recover(s,'rpc_wallets')
        except Exception as e:
            errors.append(w['address']+': '+str(e))
            if s.get('provider_backoff',{}).get(urlsplit(cfg['wallet_rpc_url']).hostname,0)>now():break
    mints={x['mint'] for x in cfg['tokens']};remaining=[]
    for i,a in enumerate(s['transaction_queue']):
        if errors or i>=cfg['transaction_details_per_cycle']:remaining.append(a);continue
        try:
            tx=client.rpc('getTransaction',[a['signature'],{'encoding':'jsonParsed','commitment':'finalized','maxSupportedTransactionVersion':0}])
            if tx is None:remaining.append(a);continue
            if (tx.get('meta') or {}).get('err') is not None:continue
            changes,owners=token_balances(tx,mints);edges=explicit_edges(tx,owners)
            result={**a,'changes':changes,'explicit_transfer_edges':edges,'observed_ms':now()}
            s.setdefault('wallet_transaction_details',{})[a['signature']]=result
            relevant=[v for v in changes if v['owner']==a.get('monitored_owner',a['wallet'])]
            for v in relevant:
                t=s['tokens'][v['mint']];approx=abs(v['change_tokens'])*t['market']['price'];floor=analytics.threshold(t,cfg,'holder')
                if floor is not None and approx>=floor:
                    text='İzlenen adreste anlamlı token bakiye değişimi · `'+v['owner']+'`\n'+f"{v['change_tokens']:+.6f} token; güncel fiyatla yaklaşık ${approx:.0f}."
                    event(s,'details:'+a['signature']+':'+v['mint']+':'+v['owner'],v['mint'],'ANLAMLI TOKEN HAREKETİ',text+'\nTransfer olabilir; tek başına alım/satım değildir.',result)
            for edge in edges:
                recipient=edge['destination_owner']
                excluded={a for t in s['tokens'].values() for a in t.get('excluded_infrastructure',[])}
                # An observed parsed transfer links addresses, not identities.
                if edge['source_owner']!=recipient and edge['source_owner'] not in excluded and recipient not in excluded:
                    for mint in mints:
                        if any(v['mint']==mint and v['owner']==edge['source_owner'] for v in changes) and any(v['mint']==mint and v['owner']==recipient for v in changes):
                            record={**edge,'mint':mint,'tx':a['signature'],'observed_ms':now(),'evidence':'explicit_token_transfer'}
                            identity=hashlib.sha256(json.dumps([mint,a['signature'],edge['source_owner'],recipient]).encode()).hexdigest()
                            s.setdefault('transfer_edges',{})[identity]=record
                # Follow outgoing recipients only from a watched owner; no cluster ownership claim.
                if edge['source_owner'] in s['wallets'] and recipient not in s['wallets'] and recipient not in excluded and sum(w.get('dynamic',False) for w in s['wallets'].values())<cfg['maximum_dynamic_wallets']:
                    s['wallets'][recipient]={'address':recipient,'label':'Açık transferdeki alıcı adres; ortak sahiplik bilinmiyor','dynamic':True,'identity_verified':False,'source':a['signature'],'cursor':None,'before':None,'pending_head':None,'seen_signatures':[]}
        except Exception as e:remaining.append(a);errors.append(str(e))
    s['transaction_queue']=remaining
    s['coverage']['wallets']={'selected':len(selected),'total_tracked':len(s['wallets']),'errors':errors,'detail_queue':len(remaining),'full_chain_coverage':False,'checked_ms':now()}
    if errors:health(s,'rpc_wallets',errors[0])

def observe(s,cfg,client=None):
    client=client or Public(s,cfg);started=now();latest={'observed_ms':started,'tokens':{},'errors':[]}
    try:bulk=client.get('https://api.dexscreener.com/tokens/v1/solana/'+','.join(t['mint'] for t in cfg['tokens']))
    except Exception as e:bulk=None;health(s,'dex',str(e));latest['errors'].append(str(e))
    for identity in cfg['tokens']:
        mint=identity['mint'];t=s['tokens'].setdefault(mint,{**identity,'history':[],'seen_trades':{}});local={}
        try:
            if bulk is None:raise ValueError('DexScreener unavailable; no fresh quote')
            pools=market(bulk,mint)
            if not pools:raise ValueError('No exact mint/liquid base-oriented pool')
            old=t.get('market');current={**pools[0],'observed_ms':now()};same=old and old['pool']==current['pool']
            t['pools']=pools;t['market']=current;t['history'].append(current);t['history']=t['history'][-2016:]
            if old and not same:event(s,mint+':pool:'+str(started),mint,'HAVUZ DEĞİŞTİ','Ana havuz değişti; iki havuzun fiyat/hacim serileri birbirine eklenmedi.')
            if same:
                change=(current['price']/old['price']-1)*100;liq=(current['liquidity']/old['liquidity']-1)*100
                if abs(change)>=cfg['price_alert_change_pct']:event(s,mint+':price:'+str(started),mint,'FİYAT',f"Son kontrol %{change:+.2f}; fiyat ${current['price']:.9g}. Gözlem aralığı {(current['observed_ms']-old['observed_ms'])/60000:.1f}dk.")
                if abs(liq)>=cfg['liquidity_alert_change_pct']:event(s,mint+':liq:'+str(started),mint,'LİKİDİTE',f"Likidite %{liq:+.2f}, ${current['liquidity']:.0f}; fiyat etkisi de içerebilir, tek başına LP çekimi kanıtı değil.")
            recover(s,'market:'+mint);local['market']='observed';allrows=[];coverage=[]
            for p in pools[:cfg['maximum_pools_per_token']]:
                payload=client.get('https://api.geckoterminal.com/api/v2/networks/solana/pools/'+p['pool']+'/trades')
                rows,cov=parse_trades(payload,mint,now());allrows.extend(rows);coverage.append({'pool':p['pool'],**cov})
            ingest_trades(s,t,allrows,coverage,now(),cfg);recover(s,'trades:'+mint)
            local['trades']=len(allrows);local['trade_coverage']=coverage
            if any(x['possibly_truncated'] or x['invalid'] for x in coverage):health(s,'sample:'+mint,'İşlem örneği sınırına veya geçersiz kayda ulaşıldı; tam hareket kapsamı yok.')
            previous=t.get('last_trade_check_ms')
            if previous and any(x['possibly_truncated'] and x['oldest_ms'] and x['oldest_ms']>previous for x in coverage):health(s,'trade_gap:'+mint,'Önceki kontrole kadar işlem geçmişi kapsanamadı; arada işlemler eksik olabilir.')
            t['last_trade_check_ms']=now()
        except Exception as e:
            local['error']=str(e);health(s,'token:'+mint,str(e))
        if now()-t.get('rugcheck_observed_ms',0)>=cfg['rugcheck_interval_seconds']*1000:
            try:
                report=client.get('https://api.rugcheck.xyz/v1/tokens/'+mint+'/report')
                if report.get('mint')!=mint:raise ValueError('Rugcheck mint mismatch')
                t['security_snapshot']={k:report.get(k) for k in ('mint','token','mintAuthority','freezeAuthority','risks','score_normalised','totalHolders','topHolders','insiderNetworks','graphInsidersDetected','detectedAt')}
                t['security_snapshot']['source_updated_ms']=None
                t['security_snapshot']['freshness']='unknown; detectedAt is not a freshness guarantee'
                t['security_snapshot']['ownership_clusters_verified']=False
                t['excluded_infrastructure']=[a for a,v in report.get('knownAccounts',{}).items() if v.get('type') in ('AMM','LOCKER')]
                t['rugcheck_observed_ms']=now()
            except Exception as e:local['rugcheck_error']=str(e)
        latest['tokens'][mint]=local
    holders(s,client,cfg)
    rpc_watch(s,client,cfg)
    for t in s['tokens'].values():
        t['quiet_accumulation']=analytics.quiet(t,now(),cfg) if not latest['tokens'][t['mint']].get('error') and t.get('last_trade_check_ms',0)>=started else []
        if not t['quiet_accumulation']:continue
        q=max(t['quiet_accumulation'],key=lambda x:x['net_usd']);previous=s.setdefault('quiet_alerts',{}).get(t['mint'])
        if analytics.should_repeat(previous,q['net_usd'],now(),cfg):
            event(s,'quiet:'+t['mint']+':'+str(now()),t['mint'],'SESSİZ BİRİKİM',f"{q['minutes']}dk örneğinde net alım ${q['net_usd']:.0f}; alım payı %{q['buy_fraction']*100:.1f}; {q['buy_trades']}alım/{q['initiators']}başlatıcı. Gözlenen fiyat bandı %{q['price_band_pct']:.2f}. Bağımsız kişi/gerçek balina veya yükseliş garantisi değil.",q)
            s['quiet_alerts'][t['mint']]={'stamp':now(),'net_usd':q['net_usd']}
    if not s.get('startup_recorded'):
        event(s,'startup:'+s['rules_fingerprint'],None,'V2 GÜNCELLEME — İŞLEM SİNYALİ DEĞİL','1 coin V2: küçük swaplar kayıtta kalır, tek tek bildirilmez. Tek işlem eşiği max100USD/likiditenin%0.1i.15/60dk net alım ve yatay fiyatla sessiz birikim ayrıca aranır. Bilinen holder token hesapları ve doğrudan transfer bağlantıları ayrı gösterilir; kimlik/sahiplik kesinliği veya tüm zincir kapsamı yok.')
        s['startup_recorded']=True
    s['updated_ms']=now();s['latest']=latest;s['last_api_requests']=client.requests
    s['events']=s['events'][-10000:]
    s['wallet_transaction_details']=dict(list(s.get('wallet_transaction_details',{}).items())[-5000:])

def legacy_render(s):
    lines=['# 1 coin — iki token için bağımsız radar','',
        'Solana: 1 ve SPSC. Yaş/mcap/yeni token filtresi yok. Alım önerisi değildir. İşlemler sınırlı havuz örneğidir; bütün zincir/bütün cüzdanlar izlenmiyor.',
        'Kontrol hedefi 5 dakika; GitHub oturumları ve kaynaklar gecikebilir. Sayım oranı USD alım hacmi değildir. Transfer alım değildir. İlişki aynı sahiplik değildir.','',
        'Son gözlem: '+(stamp(s['updated_ms']) if s.get('updated_ms') else 'başlatılıyor'),
        'Döngü: '+str(len(s['runs']))+' · doğrulanmış Issue gönderimi: '+str(len(s['delivery'])),'']
    for t in s['tokens'].values():
        m=t.get('market',{});f=t.get('flow15_sample',{})
        lines+=['## '+t['symbol']+' — '+t['name'],'','CA:','```text',t['mint'],'```',
            f"Fiyat: ${m.get('price','bilinmiyor')} · likidite: ${m.get('liquidity','bilinmiyor')} · gözlem: "+(stamp(m['observed_ms']) if m.get('observed_ms') else 'bilinmiyor'),
            f"15dk örneği: alım ${f.get('buy_usd','bilinmiyor')}, satış ${f.get('sell_usd','bilinmiyor')}, net ${f.get('net_usd','bilinmiyor')}. Örnek gözlemi: "+(stamp(f['observed_ms']) if f.get('observed_ms') else 'bilinmiyor')+'. Kaynak: seçili havuzlardaki sınırlı swap örneği.',
            '[Solscan](https://solscan.io/token/'+t['mint']+') · [DexScreener](https://dexscreener.com/solana/'+m.get('pool',t['mint'])+')','']
        hs=t.get('holder_snapshot',{})
        lines+=['Üst token hesapları: '+str(len(hs.get('owners',{})))+' altyapı dışı örnek sahip adresi; son zincir okuması '+(stamp(hs['observed_ms']) if hs.get('observed_ms') else 'BİLİNMİYOR / ERİŞİLEMEDİ')+'. Her sahibin bütün token hesapları kapsanmış sayılmaz.','']
    lines+=['## Cüzdan kapsamı','','WLFI’nin bütün adreslerini veya ana cüzdanını kapsama iddiası yok. Aşağıdaki etiketler kaynak iddiasıdır; kesin kurum sahipliği doğrulanmadı.','']
    for w in s['wallets'].values():
        lines+=['- '+w['label']+' · ['+w['address']+'](https://solscan.io/account/'+w['address']+') · son okuma '+(stamp(w['last_checked_ms']) if w.get('last_checked_ms') else 'BİLİNMİYOR / ERİŞİLEMEDİ')]
    lines+=['','## Erişim ve boşluklar','', '```json',json.dumps({'wallets':s['coverage'].get('wallets'),'errors':s.get('latest',{}).get('errors'),'alerts':s['alerts'],'provider_backoff':s['provider_backoff'],'last_api_requests':s.get('last_api_requests'),'cadence':s.get('timing')},ensure_ascii=False,indent=2),'```',
        '', 'Rugcheck holder/ilişki verisinin kaynak güncelliği bilinmiyor; bu snapshotlar canlı balina girişi veya ortak sahiplik kanıtı sayılmaz.','', '## Son kayıtlar','']
    for e in reversed(s['events'][-40:]):
        lines+=[stamp(e['observed_ms'])+' · **'+e['kind']+'** · '+e['text'],'']
    return '\n'.join(lines)+'\n'

def holders(s,client,cfg):
    seeds=[w for w in s['wallets'].values() if not w.get('dynamic') and not w.get('token_account')]
    cohort={};issues=[]
    for mint,t in s['tokens'].items():
        t.setdefault('owner_discovery',{})
        addresses={r['address'] for r in t.get('security_snapshot',{}).get('topHolders',[])[:cfg['holder_accounts_per_token']] if address(r.get('address'))}
        for w in seeds:
            record=t['owner_discovery'].get(w['address'],{})
            if now()-record.get('attempted_ms',0)>=900000:
                record={'attempted_ms':now(),'accounts':record.get('accounts',[])}
                try:
                    response=client.rpc('getTokenAccountsByOwner',[w['address'],{'mint':mint},{'encoding':'jsonParsed','commitment':'finalized'}])
                    found=[]
                    for r in response.get('value',[]):
                        info=r.get('account',{}).get('data',{}).get('parsed',{}).get('info',{})
                        if info.get('mint')!=mint or info.get('owner')!=w['address'] or not address(r.get('pubkey')):continue
                        found.append(r['pubkey'])
                    record.update(accounts=found[:4],observed_ms=now(),slot=response.get('context',{}).get('slot'),error=None)
                except Exception as e:record['error']=str(e);issues.append(str(e))
                t['owner_discovery'][w['address']]=record
            addresses.update(record.get('accounts',[]))
            for ata in record.get('accounts',[]):
                if ata not in s['wallets']:
                    s['wallets'][ata]={'address':ata,'label':w['label']+' / token hesabı','monitored_owner':w['address'],'monitored_mint':mint,
                        'identity_verified':False,'token_account':True,'dynamic':False,'source':'getTokenAccountsByOwner','cursor':None,'before':None,'pending_head':None,'seen_signatures':[]}
        # A previously reported exact ATA is also a candidate until it is revalidated.
        # This is a known account cohort, never a claim to the live global top20.
        for r in t.get('security_snapshot',{}).get('topHolders',[]):
            if r.get('owner') in {w['address'] for w in seeds} and address(r.get('address')):
                addresses.add(r['address'])
        cohort[mint]=sorted(addresses)
    requested=sorted({a for values in cohort.values() for a in values})[:100]
    try:
        if not requested:raise ValueError('No known token-account cohort available')
        response=client.rpc('getMultipleAccounts',[requested,{'encoding':'jsonParsed','commitment':'finalized'}])
        values=response.get('value');slot=response.get('context',{}).get('slot')
        if not isinstance(values,list) or len(values)!=len(requested) or not slot:raise ValueError('Invalid holder account response')
        byaddress=dict(zip(requested,values))
        for mint,t in s['tokens'].items():
            selected=[a for a in cohort[mint] if a in byaddress];previous=t.get('live_holder_cohort',{})
            current=analytics.holders([byaddress[a] for a in selected],selected,mint,set(t.get('excluded_infrastructure',[])),now(),slot,previous)
            t['live_holder_cohort']=current
            for owner,row in current['owners'].items():
                # Activate exact token-account monitoring for seed wallet owners,
                # including ATAs discovered by the holder report and validated now.
                if owner in {w['address'] for w in seeds}:
                    parent=s['wallets'][owner]
                    for ata,v in current['accounts'].items():
                        if v['owner']==owner and ata not in s['wallets']:
                            s['wallets'][ata]={'address':ata,'label':parent['label']+' / doğrulanmış token hesabı','monitored_owner':owner,'monitored_mint':mint,'identity_verified':False,'token_account':True,'dynamic':False,'source':'getMultipleAccounts exact mint/owner validation','cursor':None,'before':None,'pending_head':None,'seen_signatures':[]}
                approximate=abs(row['change_tokens'])*t['market']['price'];floor=analytics.threshold(t,cfg,'holder')
                if row['same_accounts_compared'] and floor is not None and approximate>=floor:
                    event(s,'holder:'+mint+':'+owner+':'+str(slot),mint,'HOLDER BAKİYE ARTIŞI' if row['change_tokens']>0 else 'HOLDER BAKİYE AZALIŞI',
                        f"`{owner}` · aynı izlenen token hesaplarında {row['change_tokens']:+.6f}token; güncel fiyatla yaklaşık ${approximate:.0f}. Token transferi olabilir; otomatik alım/satım yorumu yok.",{'owner':owner,**row,'slot':slot})
            t['linked_groups']=analytics.groups(list(s.get('transfer_edges',{}).values()),current['owners'],mint)
            recover(s,'holder_cohort:'+mint)
    except Exception as e:
        issues.append(str(e));health(s,'holder_cohort','Doğrulanmış holder bakiyesi okunamadı: '+str(e))
    s['coverage']['holder_cohort']={'requested_token_accounts':len(requested),'issues':issues,'observed_ms':now(),'global_top20_complete':False,'all_holders_complete':False}

def render(s):
    cfg=config();lines=['# 1 coin — V2 anlamlı hareket ve sessiz birikim','',
        'Solana1 veSPSC; yalnız genel veriler. Bildirim gürültüsü filtresi küçük işlemleri gizler; bot tespiti yapıldığı anlamına gelmez.',
        'Yaklaşık5dk kontrol.1coin V1 kayıtları arşivlenir; eski mesajlar yeni sinyal diye tekrar gönderilmez.','',
        'Son gözlem: '+(stamp(s['updated_ms']) if s.get('updated_ms') else 'başlatılıyor')+' · V2 döngüsü '+str(len(s['runs'])),'',
        '## Bildirim kuralları','', 'Tek swap: en az max(100USD, likidite×%0.1). Küçük swaplar sessiz kayda alınır.15/60dk net alım, en az3alım ve en az%65USD alım payı ile gözlenen fiyat bandı en çok%2 ise sessiz birikim incelenir. Bu yükseliş veya bağımsız kişiler kanıtı değildir.','']
    for t in s['tokens'].values():
        m=t.get('market',{});floor=analytics.threshold(t,cfg);f=t.get('notification_filter',{})
        lines+=['## '+t['symbol']+' — '+t['name'],'','CA:','```text',t['mint'],'```',
            f"Fiyat ${m.get('price','bilinmiyor')}; likidite ${m.get('liquidity','bilinmiyor')}; tek swap bildirim eşiği ${floor:.0f}." if floor is not None else 'Güncel fiyat/likidite bilinmiyor.',
            f"V2de sessiz kaydedilen küçük işlem {f.get('small_trades_logged',0)}, anlamlı tek işlem {f.get('meaningful_trades',0)}.",
            '[Solscan](https://solscan.io/token/'+t['mint']+') · [DexScreener](https://dexscreener.com/solana/'+m.get('pool',t['mint'])+')','', '### Sessiz birikim','']
        for q in t.get('quiet_accumulation',[]):lines+=[f"{q['minutes']}dk: örnek alım ${q['buy_usd']:.0f}, satış ${q['sell_usd']:.0f}, net ${q['net_usd']:.0f}, fiyat bandı %{q['price_band_pct']:.2f}; {q['initiators']}başlatıcı adres."]
        if not t.get('quiet_accumulation'):lines+=['Güncel örnekte koşullar sağlanmadı veya yeterli kesintisiz veri yok.']
        holder=t.get('live_holder_cohort',{})
        lines+=['','### İzlenen holderlar','',
            'Bilinen token hesaplarının zincir üzerinde doğrulanmış örneği; bütün holderlar veya güncel en büyük20sıralaması değildir. Eksik hesaplar sıfır bakiye sayılmaz.',
            'Son zincir okuması: '+(stamp(holder['observed_ms']) if holder.get('observed_ms') else 'BİLİNMİYOR'),
            '', '| Adres | Gözlenen token bakiyesi | Aynı hesaplardaki son değişim |', '|---|---:|---:|']
        for owner,h in sorted(holder.get('owners',{}).items(),key=lambda x:-x[1]['amount'])[:12]:
            delta=f"{h['change_tokens']:+.6f}" if h['same_accounts_compared'] else 'ilk baz / bilinmiyor'
            lines+=['|['+owner+'](https://solscan.io/account/'+owner+')|'+f"{h['amount']:.6f}"+'|'+delta+'|']
        lines+=['','### Cüzdan bağlantıları','', 'Yalnız açık kaynakta gözlenen doğrudan token transferleri bağlantı sayılır; aynı sahiplik kanıtı değildir.']
        for group in t.get('linked_groups',[]):lines+=['- '+', '.join('`'+a+'`' for a in group['members'])+f" · aynı örnek hesaplarda toplam {group['change_tokens']:+.6f}token değişim."]
        if not t.get('linked_groups'):lines+=['Henüz yeterli doğrulanmış bağlantı yok. Sağlayıcının insider-network etiketleri kimlik teyidi sayılmadı.']
    lines+=['', '## Veri kapsamı','', '```json',json.dumps({'coverage':s.get('coverage'),'alerts':s.get('alerts'),'provider_backoff':s.get('provider_backoff'),'timing':s.get('timing'),'detail_queue':len(s.get('transaction_queue',[]))},ensure_ascii=False,indent=2),'```',
        'WLFI etiketleri kaynak iddiasıdır; tüm WLFI adreslerini veya ana cüzdanı doğruladığımız iddiası yok. Cüzdan sahip adresi ve bilinen token hesapları birlikte izlenir. Aradaki veri boşlukları gizlenmez.', '', '## Son anlamlı kayıtlar','']
    for e in reversed(s['events'][-40:]):lines+=[stamp(e['observed_ms'])+' · **'+e['kind']+'** · '+e['text'],'']
    return '\n'.join(lines)+'\n'
