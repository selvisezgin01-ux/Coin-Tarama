"""Persistent identity ledger, young-token capacity and honest discovery coverage."""
from copy import deepcopy
from collections import Counter
import hashlib,json,time,os,base64
import meme_sources as source
import meme_v7_model as model

def remember_identity(state,chain,mint,pool,created,seen):
    if not source.valid_address(chain,mint) or not source.valid_address(chain,pool,True):return False
    created=source.ms_iso(created) if isinstance(created,str) else created
    if not isinstance(created,(int,float)) or not 0<created<=seen:return False
    mint=model.rules.address_key(chain,mint);pool=model.rules.address_key(chain,pool);k=chain+':'+mint
    ledger=state.setdefault('ledger',{})
    row=ledger.setdefault(k,{'chain':chain,'mint':mint,'first_seen_ms':seen,'pools':{},'status':'discovered_waiting_quote','reasons':[]})
    row['first_seen_ms']=min(row['first_seen_ms'],seen)
    row['pools'].setdefault(pool,{'created_ms':int(created),'first_seen_ms':seen})
    return True

def merge_feed(state,feed,cfg,now):
    if not isinstance(feed,dict) or feed.get('version')!='meme-v7-discovery-feed':raise ValueError('Feed identity/schema mismatch')
    stamp=feed.get('observed_ms')
    if not isinstance(stamp,int) or stamp>now+60000:raise ValueError('Feed clock invalid')
    rows=feed.get('identities')
    if not isinstance(rows,list) or len(rows)>30000:raise ValueError('Feed size/schema invalid')
    added=0
    for r in rows:
        if not isinstance(r,dict) or r.get('chain') not in cfg['networks']:continue
        seen=r.get('first_seen_ms')
        if not isinstance(seen,int) or not 0<seen<=now:continue
        added+=remember_identity(state,r['chain'],r.get('mint'),r.get('pool'),r.get('created_ms'),seen)
    heartbeat_fresh=0<=now-stamp<=cfg['v7']['feed_max_age_seconds']*1000;health={}
    for chain in cfg['networks']:
        p=feed.get('networks',{}).get(chain,{})
        last=p.get('last_observed_ms');age=None if not isinstance(last,int) else (now-last)/1000
        target=cfg['v7']['collector_network_intervals_seconds'][chain]
        ok=age is not None and 0<=age<=max(180,2*target) and not p.get('last_error')
        health[chain]={'last_data_age_seconds':age,'data_recent':ok,'last_error':p.get('last_error'),
            'unresolved_gap_count':p.get('unresolved_gap_count',len(p.get('gaps',[])))}
        if any(code in str(p.get('last_error','')) for code in ('429','403','401','418')):
            state['provider_backoff_until_ms']=max(state.get('provider_backoff_until_ms',0),p.get('due_ms',now+900000))
    state['collector_feed']={'observed_ms':stamp,'age_seconds':(now-stamp)/1000,'heartbeat_fresh':heartbeat_fresh,
        'fresh':heartbeat_fresh and all(v['data_recent'] for v in health.values()),'network_health':health,'ingested_identities':added,
        'network_coverage':deepcopy(feed.get('networks',{})),'collector_run_id':feed.get('run_id'),
        'note':'Discovery identity is not a fresh price, security check or complete chain coverage.'}
    return state['collector_feed']['fresh']

def discover(state,client,cfg,now):
    errors=[];fresh=False
    try:
        token=os.environ.get('GH_TOKEN')
        if token and os.environ.get('GITHUB_REPOSITORY')=='selvisezgin01-ux/Coin-Tarama':
            # Read the branch through authenticated Contents API, not the 5min raw CDN cache.
            payload=client.request('https://api.github.com/repos/selvisezgin01-ux/Coin-Tarama/contents/feed.json?ref=scanner-feed-meme-v7',
                headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github.raw+json','Cache-Control':'no-cache'})
            if payload.get('encoding')=='base64':payload=json.loads(base64.b64decode(payload['content']).decode('utf-8'))
        else:payload=client.request(cfg['v7']['feed_url']+'?minute='+str(now//60000))
        fresh=merge_feed(state,payload,cfg,now)
    except Exception as exc:errors.append('collector_feed: '+str(exc));state['collector_feed']={'fresh':False,'error':str(exc)}
    if fresh:return {'mode':'continuous_collector_feed','errors':errors,'coverage':state['collector_feed']}
    if now<state.get('provider_backoff_until_ms',0):
        client.blocked.add('api.geckoterminal.com')
        return {'mode':'collector_or_provider_backoff_no_new_pool_coverage','errors':errors+['provider_backoff_active'],
                'coverage':state.get('collector_feed'),'complete':False}
    # Bounded fallback is labelled as partial; a stale collector never becomes a healthy minute feed.
    chains=list(cfg['networks']);offset=state.get('fallback_rotation',0)%len(chains);chains=chains[offset:]+chains[:offset]
    pages=[]
    for chain in chains[:cfg['v7']['max_fallback_pages']]:
        try:
            data=client.gecko(f"networks/{cfg['networks'][chain]['gecko']}/new_pools?page=1&include=base_token,quote_token")
            rows=data.get('data');assert isinstance(rows,list),'Malformed new-pool response'
            for p in rows:
                try:
                    a=source.normalize_pool(chain,p,{r['id']:r['attributes'] for r in data.get('included',[])})
                    remember_identity(state,chain,a['mint'],a['pool'],a.get('pool_created_ms'),now)
                except (ValueError,KeyError,TypeError):continue
            pages.append({'chain':chain,'page':1,'returned':len(rows),'complete':False})
        except Exception as exc:errors.append(chain+': '+str(exc))
    state['fallback_rotation']=offset+1
    return {'mode':'bounded_fallback_collector_unavailable_or_stale','errors':errors,'pages':pages,'complete':False}

def quote_plan(state,chain,cfg,now):
    rows=[];active=[]
    for k,r in state.get('ledger',{}).items():
        if r['chain']!=chain:continue
        created=min(p['created_ms'] for p in r['pools'].values());age=(now-created)/60000
        entry=state.get('entries',{}).get(k,{}).get('references',{}).get('entry_5m')
        if entry and 0<=now-entry['observed_ms']<=25*3600000:
            active.append((k,r,age));continue
        if not 0<=age<=cfg['market']['max_pool_age_hours']*60:
            r.update(status='archived_age',reasons=['pool_age_over_24h_identity_preserved']);continue
        rows.append((k,r,age))
    rows.sort(key=lambda item:(item[1].get('last_quote_attempt_ms',0),item[1]['first_seen_ms'],item[0]))
    young=[r for r in rows if r[2]<=cfg['v7']['young_minutes']];older=[r for r in rows if r[2]>cfg['v7']['young_minutes']]
    cap=cfg['v7']['quote_per_chain'];selected=active[:cap];remaining=cap-len(selected)
    picked=young[:(remaining+1)//2]+older[:remaining//2]
    ids={x[0] for x in picked+selected}
    picked += [x for x in rows if x[0] not in ids][:remaining-len(picked)]
    selected+=picked
    for _,r,_ in selected:r['last_quote_attempt_ms']=now
    for k,r,_ in rows:
        if k not in {x[0] for x in selected}:r['status']='quote_budget_waiting';r['reasons']=['explicit_quote_queue_no_identity_eviction']
    return [r['mint'] for _,r,_ in selected]

def dex_quotes(client,chain,network,mints,now,pinned=None):
    result=[];pinned=pinned or {}
    for start in range(0,len(mints),30):
        data=client.dex('tokens/v1/'+network['dex']+'/'+','.join(mints[start:start+30]))
        if not isinstance(data,list):raise ValueError('Malformed DexScreener quote response')
        by={}
        for p in data:
            mint=model.rules.address_key(chain,str((p.get('baseToken') or {}).get('address','')))
            if p.get('chainId')!=network['dex'] or mint not in mints[start:start+30]:continue
            pool=model.rules.address_key(chain,str(p.get('pairAddress','')))
            if not source.valid_address(chain,pool,True):continue
            if mint in pinned and pool!=pinned[mint]:continue
            liq=model.rules.number((p.get('liquidity') or {}).get('usd'))
            old=by.get(mint)
            if old is None or (liq or 0)>(old.get('liquidity_usd') or 0):
                tx=(p.get('txns') or {}).get('m5') or {};volume=p.get('volume') or {}
                by[mint]={'chain':chain,'mint':mint,'pool':pool,'symbol':str((p.get('baseToken') or {}).get('symbol','?'))[:40],
                    'dex':p.get('dexId'),'price_usd':model.rules.number(p.get('priceUsd')),'price_observed_ms':int(time.time()*1000),
                    'observed_ms':int(time.time()*1000),'liquidity_usd':liq,'market_cap_usd':model.rules.number(p.get('marketCap')),
                    'fdv_usd':model.rules.number(p.get('fdv')),'pool_created_ms':model.rules.number(p.get('pairCreatedAt')),
                    'volume5_usd':model.rules.number(volume.get('m5')),'buys5':model.rules.number(tx.get('buys')),'sells5':model.rules.number(tx.get('sells')),
                    'source':'dexscreener_exact_chain_mint_pool','pool_age_is_token_age':False}
        result+=list(by.values())
    return result

def decision(state,a,now,stage,reasons):
    row=state['ledger'][model.key(a)];old=row.get('decision')
    value={'at_ms':now,'stage':stage,'reasons':list(reasons),'pool':a['pool']}
    row['decision']=value;row['status']=stage;row['reasons']=list(reasons)
    # Append only transitions, retaining the original timestamps; no silent eviction.
    if old is None or (old['stage'],old['reasons'],old['pool'])!=(stage,list(reasons),a['pool']):
        row.setdefault('decision_history',[]).append(value)
