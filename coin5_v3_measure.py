"""Exact market price-path study; no spot substitution for perpetual outcomes."""
import math
from statistics import median
import coin5_v3_sources as src
from coin5_v2_measure import first_touch

def fetch_range(client,contract,start,end,stamp):
    result={};cursor=end if client.venue=='OKX' else start;pages=0
    while (cursor>start if client.venue=='OKX' else cursor<end):
        pages+=1
        if pages>20:raise ValueError('Minute range exceeds bounded page budget')
        raw=client.get('candles',contract,'1m',start=start if client.venue=='OKX' else cursor,end=cursor if client.venue=='OKX' else end)
        rows=src.normalized(raw,client.venue,client.kind,'1m',stamp)
        in_range={k:v for k,v in rows.items() if start<=k<end}
        for k,v in in_range.items():
            if k in result and result[k]!=v:raise ValueError('Conflicting historical minute')
            result[k]=v
        if not rows:break
        new=min(rows) if client.venue=='OKX' else max(rows)+60000
        if client.venue=='OKX' and new>=cursor or client.venue!='OKX' and new<=cursor:raise ValueError('Historical pagination made no progress')
        cursor=new
    return result

def measure(state,cfg,stamp,fetcher=fetch_range):
    cases=state['measurements']['cases'];due=[]
    for c in cases.values():
        if any(stamp>=math.ceil((c['observed_ms']+h*3600000)/60000)*60000 and not c['outcomes'].get(str(h),{}).get('complete') for h in cfg['horizons_hours']):due.append(c)
    due.sort(key=lambda c:(c.get('last_measure_attempt_ms',0),c['observed_ms']))
    errors=[];clients={};cache={}
    def read(c,contract,start,end):
        group=c['exchange']+':'+c['kind'];key=(group,contract,start,end)
        if group not in clients:clients[group]=src.Public(c['exchange'],c['kind'])
        if key not in cache:cache[key]=fetcher(clients[group],contract,start,end,stamp)
        return cache[key]
    for c in due[:cfg['max_cases_measured_per_run']]:
        c['last_measure_attempt_ms']=stamp
        try:
            horizons=[(h,math.ceil((c['observed_ms']+h*3600000)/60000)*60000) for h in cfg['horizons_hours']
                      if stamp>=math.ceil((c['observed_ms']+h*3600000)/60000)*60000 and not c['outcomes'].get(str(h),{}).get('complete')]
            start=c['observed_ms']//60000*60000;end=max(t for _,t in horizons)
            rows=read(c,c['contract'],start,end)
            btc='BTCUSDT' if c['kind']=='SPOT' and c['exchange']=='MEXC' else 'BTC_USDT' if c['exchange']=='MEXC' else 'BTC-USDT'+('-SWAP' if c['kind']=='PERP' else '')
            for h,t in horizons:
                price=rows.get(t-60000,{}).get('c');ret=None if price is None else (price/c['entry_price']-1)*100
                fullstart=math.ceil(c['observed_ms']/60000)*60000
                path=[rows[k] for k in range(fullstart,t,60000) if k in rows]
                full=bool(path) and len(path)==(t-fullstart)//60000
                b=None
                if c['btc_entry_price'] is not None:
                    b=read(c,btc,t-60000,t).get(t-60000,{}).get('c')
                br=None if b is None or c['btc_entry_price'] is None else (b/c['btc_entry_price']-1)*100
                o={'target_ms':c['observed_ms']+h*3600000,'endpoint_ms':t,'endpoint_price':price,'return_pct':ret,
                    'btc_excess_pct_points':None if br is None or ret is None else ret-br,
                    'mae_pct':min(0,(min(b['l'] for b in path)/c['entry_price']-1)*100) if full else None,
                    'mfe_pct':max(0,(max(b['h'] for b in path)/c['entry_price']-1)*100) if full else None,
                    'path_complete':full,'complete':ret is not None and full,'minute_bars':len(path),
                    'ignored_entry_fragment_ms':fullstart-c['observed_ms'],'measured_ms':stamp,
                    'cost_scenarios_pct':{str(cost):None if ret is None else ret-cost for cost in cfg['round_trip_cost_scenarios_pct']}}
                if c['phase']=='triggered':
                    oldshape={k:{'open':v['o'],'high':v['h'],'low':v['l'],'close':v['c']} for k,v in rows.items() if k<t}
                    outcome=first_touch(c,oldshape,start,t)
                    if outcome.get('exit_price') is not None:
                        gross=(outcome['exit_price']/c['entry_price']-1)*100
                        outcome['net_r_scenarios']={str(cost):(gross-cost)/c['risk_pct'] for cost in cfg['round_trip_cost_scenarios_pct']}
                    outcome['hypothetical_not_fill']=True;o['barriers']=outcome
                else:o['barriers']={'status':'not_a_trade_entry'}
                c['outcomes'][str(h)]=o
        except Exception as e:errors.append({'key':c['key'],'phase':c['phase'],'error':str(e)})
    state['measurements']['errors']=errors
    state['measurements']['queue']={'due':len(due),'attempted':min(len(due),cfg['max_cases_measured_per_run']),'observed_ms':stamp,'unique_reads':len(cache)}
    summary={}
    for phase in ('radar','triggered'):
        items=[c for c in cases.values() if c['phase']==phase];summary[phase]={'unique_symbol_labels':len(items),'hours':{}}
        for h in cfg['horizons_hours']:
            vals=[c['outcomes'][str(h)]['return_pct'] for c in items if c['outcomes'].get(str(h),{}).get('complete')]
            summary[phase]['hours'][str(h)]={'known':len(vals),'median_pct':median(vals) if vals else None}
    state['measurements']['summary']=summary
