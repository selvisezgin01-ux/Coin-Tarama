"""Price-path barrier study. Hypothetical observations, never exchange executions."""
import math
from statistics import median
import short_squeeze_lab as lab

def first_touch(case,rows,start,end):
    stop=case['stop'];target=case['target'];entry=case['entry_price'];minute=60000
    opening=case['observed_ms']//minute*minute
    partial=opening!=case['observed_ms']
    for t in range(opening,end,minute):
        b=rows.get(t)
        if b is None:return {'status':'unknown_gap','at_ms':t}
        low=b['low']<=stop;high=b['high']>=target
        if t==opening and partial and (low or high):return {'status':'unknown_entry_fragment','at_ms':t}
        if t==opening and partial:continue
        if low and high:return {'status':'ambiguous_same_minute','at_ms':t}
        if low:return {'status':'stop_first','at_ms':t,'exit_price':min(stop,b['open'])}
        if high:return {'status':'target_first','at_ms':t,'exit_price':target}
    return {'status':'neither','at_ms':end,'exit_price':rows[end-minute]['close']} if rows else {'status':'unknown_gap'}

def measure(state,cfg,stamp,fetcher=lab.fetch_minutes):
    cache={}
    def cached(venue,symbol,start,end):
        key=(venue,symbol,start,end)
        if key not in cache:cache[key]=fetcher(venue,symbol,start,end)
        return cache[key]
    # Preserve the existing endpoint returns/BTC/MAE/MFE measurements.
    lab.measure(state['measurements'],cfg,stamp,cached)
    errors=state['measurements']['errors']
    selected=[c for c in state['measurements']['cases'].values() if c.get('last_measure_attempt_ms')==stamp]
    retries=[c for c in state['measurements']['cases'].values() if c not in selected and any(
        not o.get('barriers') or o['barriers'].get('status')=='unknown_gap' for o in c['outcomes'].values())]
    retries.sort(key=lambda c:c.get('last_barrier_attempt_ms',0))
    selected+=retries[:max(0,cfg['max_cases_measured_per_run']-len(selected))]
    for case in selected:
        case['last_barrier_attempt_ms']=stamp
        for key,o in case['outcomes'].items():
            try:
                start=case['observed_ms']//60000*60000;end=o['endpoint_ms']
                rows=lab.candles(cached(case['exchange'],case['symbol'],start,end),start,end,stamp)
                result=first_touch(case,rows,start,end)
                if result.get('exit_price') is not None:
                    gross=(result['exit_price']/case['entry_price']-1)*100
                    result['net_r_scenarios']={str(c):(gross-c)/case['risk_pct'] for c in cfg['round_trip_cost_scenarios_pct']}
                result['hypothetical_not_fill']=True;o['barriers']=result
            except Exception as e:errors.append({'symbol':case['symbol'],'exchange':case['exchange'],'error':'barriers: '+str(e)})
    state['measurements']['comparison']={
        'all_retest_entries':len(state['measurements']['cases']),
        'nested_short_confirmed':sum(c['strict_short_confirmed'] for c in state['measurements']['cases'].values()),
        'short_information_unknown':sum(c['short_information']=='unknown' for c in state['measurements']['cases'].values()),
        'note':'Nested observational subsets at the same entries; not randomized independent trials.',
        'by_horizon':{}}
    for h in cfg['horizons_hours']:
        groups={}
        for group in ('all_retests','short_confirmed','observed_without_short_confirmation','short_unknown'):
            cases=[c for c in state['measurements']['cases'].values() if group=='all_retests' or
                (group=='short_confirmed' and c['strict_short_confirmed']) or
                (group=='observed_without_short_confirmation' and c['short_information']=='observed_without_confirmation') or
                (group=='short_unknown' and c['short_information']=='unknown')]
            outcomes=[c['outcomes'].get(str(h),{}).get('barriers',{}) for c in cases]
            values=[o['net_r_scenarios'][str(cfg['planning_cost_pct'])] for o in outcomes if o.get('net_r_scenarios')]
            groups[group]={'unique_symbols':len(cases),'known_path_results':len(values),
                'median_net_r':median(values) if values else None,
                'target_first':sum(o.get('status')=='target_first' for o in outcomes),
                'stop_first':sum(o.get('status')=='stop_first' for o in outcomes),
                'ambiguous_or_missing':sum(o.get('status','').startswith(('unknown','ambiguous')) for o in outcomes)}
        state['measurements']['comparison']['by_horizon'][str(h)]=groups
