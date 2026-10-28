"""Bounded new-pool discovery and explicit data-only inspection funnel."""
from collections import Counter
import time
import meme_sources as source
import meme_rules as rules

class BudgetClient(source.Client):
    """Shared scan/followup budget; access rejection never triggers alternate hosts."""
    def __init__(self,cfg,backoff_until=0):
        super().__init__(cfg);self.gecko_remaining=cfg['pipeline']['global_gecko_requests_per_cycle'];self.rate_limited=False
        if int(time.time()*1000)<backoff_until:self.blocked.add('api.geckoterminal.com')
    def gecko(self,path):
        with self.lock:
            if self.gecko_remaining<=0:
                self.stats['gecko:budget_deferred']+=1;raise RuntimeError('gecko_request_budget_deferred')
            self.gecko_remaining-=1
        try:return super().gecko(path)
        except RuntimeError as e:
            if 'HTTP 429' in str(e):self.rate_limited=True
            raise

def discover(client,chain,network,state,stamp):
    rows=[];errors=[];pages=[];prior=state.get('discovery_checkpoints',{}).get(chain)
    overlap=client.config['pipeline']['discovery_gap_overlap_minutes']*60000
    boundary=prior-overlap if prior is not None else stamp-120*60000
    reached=False;last_stamp=None;valid_page=False
    for page in range(1,client.config['discovery']['new_pool_pages_per_network']+1):
        path=f"networks/{network['gecko']}/new_pools?page={page}&include=base_token,quote_token"
        try:
            payload=client.gecko(path);data=payload.get('data');assert isinstance(data,list),'Malformed discovery list'
            included={x['id']:x.get('attributes',{}) for x in payload.get('included',[])}
            times=[source.ms_iso(p.get('attributes',{}).get('pool_created_at')) for p in data]
            times=[t for t in times if t is not None];valid_page=True
            if times:last_stamp=min(times)
            pages.append({'page':page,'returned':len(data),'oldest_created_ms':last_stamp})
            for pool in data:
                try:rows.append(source.normalize_pool(chain,pool,included))
                except (ValueError,TypeError,KeyError):continue
            if not data or (times and min(times)<=boundary):reached=True;break
        except Exception as e:errors.append(str(e));break
    # An uncovered interval remains unresolved on subsequent runs, rather than disappearing.
    checkpoint=stamp if reached and not errors else prior
    return rows,errors,{'pages':pages,'covered_to_previous_checkpoint':reached,'gap_or_initial_window_uncovered':not reached,
        'previous_checkpoint_ms':prior,'next_checkpoint_ms':checkpoint,'oldest_returned_ms':last_stamp,'valid_page':valid_page}

def age(record,stamp):
    created=record.get('earliest_pool_created_ms')
    return None if created is None else (stamp-created)/60000

def priority(record,stamp,cfg):
    a=age(record,stamp);asset=record['latest'];gate=record.get('market',{})
    # Approaching minimum age must be refreshed BEFORE eligibility, not retained behind old liquid pools.
    due=a is not None and cfg['market']['min_pool_age_minutes']<=a<=cfg['pipeline']['priority_age_minutes']
    approaching=a is not None and 0<=a<cfg['market']['min_pool_age_minutes']
    activity=(rules.number(asset.get('volume15_usd')) or 0)+100*(rules.number(asset.get('buys15')) or 0)
    return (0 if due else 1 if approaching else 2,0 if gate.get('passed') else 1,
            record.get('last_evaluated_ms',0),-activity,record['latest'].get('observed_ms',0))

def refresh_targets(records,state,chain,stamp,cfg):
    active=set(state.get('entries',{}))
    records=sorted(records,key=lambda r:(0 if chain+':'+r['latest']['mint'] in active else 1,priority(r,stamp,cfg)))
    pools=[]
    for r in records:
        if stamp-r['latest'].get('observed_ms',0)<120000:continue
        if age(r,stamp) is None or age(r,stamp)>cfg['market']['max_pool_age_hours']*60:continue
        if r['latest']['pool'] not in pools:pools.append(r['latest']['pool'])
    return pools[:cfg['pipeline']['refresh_pool_budget_per_network']]

def inspectable(record,cfg,stamp):
    a=age(record,stamp);asset=record['latest'];liq=rules.number(asset.get('liquidity_usd'))
    if record.get('first_formation_disqualified'):return False
    if a is None or not cfg['market']['min_pool_age_minutes']<=a<=cfg['market']['max_pool_age_hours']*60:return False
    if liq is None or liq<cfg['pipeline']['minimum_observe_liquidity_usd']:return False
    if record.get('security',{}).get('blocked') or record.get('developer',{}).get('status')=='outgoing_transfer_detected':return False
    # This permits candle READING only. It does not waive a positive alert market/security gate.
    return True

def funnel(records,stamp,cfg):
    return {'records':len(records),'waiting_min_age':sum(age(r,stamp) is not None and 0<=age(r,stamp)<cfg['market']['min_pool_age_minutes'] for r in records),
        'market_pass':sum(r.get('market',{}).get('passed',False) for r in records),
        'market_failed':dict(Counter(k for r in records for k in r.get('market',{}).get('failed',[]))),
        'market_unknown':dict(Counter(k for r in records for k in r.get('market',{}).get('unknown',[]))),
        'data_inspection_possible':sum(inspectable(r,cfg,stamp) for r in records)}

def cadence(runs,stamp):
    times=sorted({r['ms'] for r in runs if 0<=stamp-r['ms']<=86400000});intervals=sorted((b-a)/60000 for a,b in zip(times,times[1:]))
    return {'interval_count':len(intervals),'p95_minutes':intervals[min(len(intervals)-1,max(0,__import__('math').ceil(.95*len(intervals))-1))] if intervals else None,
            'max_minutes':max(intervals) if intervals else None,'meets_7m_target':bool(intervals and intervals[min(len(intervals)-1,max(0,__import__('math').ceil(.95*len(intervals))-1))]<=7),
            'full_24h_observed':bool(times and times[-1]-times[0]>=23*3600000)}
