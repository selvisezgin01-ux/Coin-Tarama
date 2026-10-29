"""Prospective V2: frozen base -> breakout -> retest -> later reclaim. No orders."""
import hashlib,json
from pathlib import Path
from copy import deepcopy
from statistics import median
import coin5_model as v1

ROOT=Path(__file__).parent

def config():return json.loads((ROOT/'coin5_v2_config.json').read_text(encoding='utf-8'))

def fingerprint():
    h=hashlib.sha256(v1.fingerprint().encode())
    for name in ('coin5_v2_config.json','coin5_v2_model.py','coin5_v2_scan.py','coin5_v2_measure.py','coin5_v2_worker.py'):
        h.update(name.encode());h.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return h.hexdigest()

def new_state():
    s=v1.new_state();s.update(version='coin-tarama-5-v2',rules_fingerprint=fingerprint(),runs=[],review_candidates={})
    return s

def migrate(old,sha,stamp):
    if old['rules_fingerprint']!=v1.fingerprint():raise ValueError('Unexpected V1 rules; cannot silently migrate')
    s=new_state();s['previous_v1']=deepcopy(old)
    s['migration']={'source':'scanner-state-coin-tarama-5','source_sha':sha,'observed_ms':stamp,'old_entries_replayed':False}
    for field in ('oi_history','ratio_history'):s[field]=deepcopy(old.get(field,{}))
    # Old fills and pending messages remain only in their unmodified archive.
    s['last_closed']=deepcopy(old.get('last_closed',{}))
    for a in old.get('assets',{}).values():
        if a['phase'] in ('preparation','triggered'):s['last_closed'][a['symbol']]=stamp
    return s

def context(series,btc,cfg):
    c=v1.context(series,btc,cfg);be=v1.ema([b['c'] for b in btc])
    c['btc_long_blocked']=btc[-1]['c']<be[-1] and be[-1]<be[-4]
    c['btc_close_ms']=btc[-1]['t']+3600000
    return c

def derivatives(market,funding,oi,points,history,cfg,stamp):
    d=v1.derivative_context(market,funding,oi,points,history,cfg,stamp)
    d['strict_short_confirmed']=bool(d.get('supporting_sources'))
    d['short_information']=('confirmed' if d['strict_short_confirmed'] else
        'observed_without_confirmation' if any(p.get('change_pp') is not None for p in d['profiles'].values()) else 'unknown')
    # Short confirmation is a predeclared nested comparison, not a market-wide claim.
    d['reasons']=[x for x in d['reasons'] if x!='short_increase_unconfirmed']
    d['ready']=not d['reasons'];return d

def pivots(bars):
    return [bars[i]['h'] for i in range(2,len(bars)-2)
            if bars[i]['h']>max(bars[i-1]['h'],bars[i-2]['h']) and
               bars[i]['h']>=max(bars[i+1]['h'],bars[i+2]['h'])]

def entry_plan(asset,row,cfg):
    price=row['quote']['price'];a=row['context']['atr'];level=asset['level']
    stop=max(asset['base_invalid'],asset['retest_low']-.15*asset['atr'])
    levels=[h for h in pivots(row['series']['4h']) if h>price]
    reasons=[];resistance=min(levels) if levels else None
    if row['context'].get('btc_long_blocked'):reasons.append('btc_downtrend')
    if row['context']['reasons']:reasons.extend(row['context']['reasons'])
    if not row['derivatives']['ready']:reasons.extend(row['derivatives']['reasons'])
    if row.get('book_reasons'):reasons.extend(row['book_reasons'])
    if not stop<price or price<level:reasons.append('entry_below_level_or_stop')
    if price-level>cfg['maximum_trigger_extension_atr']*a:reasons.append('entry_extended')
    if abs(price-row['series']['15m'][-1]['c'])>a:reasons.append('quote_detached_from_close')
    risk=(price-stop)/price*100
    if not 0<risk<=cfg['maximum_risk_pct']:reasons.append('risk_outside_limit')
    if resistance is None:reasons.append('overhead_unknown')
    cost=cfg['planning_cost_pct'];gross_room=None if resistance is None else (resistance/price-1)*100
    net_r=None if gross_room is None or risk<=0 else (gross_room-cost)/(risk+cost)
    if net_r is not None and net_r<cfg['minimum_overhead_room_r']:reasons.append('net_overhead_room_insufficient')
    target=price*(1+(cfg['minimum_overhead_room_r']*(risk+cost)+cost)/100)
    return {'reasons':list(dict.fromkeys(reasons)),'stop':stop,'target':target,'resistance':resistance,
            'risk_pct':risk,'net_room_r':net_r,'planning_cost_pct':cost,
            'entry_zone_low':level,'entry_zone_high':level+cfg['maximum_trigger_extension_atr']*a}

def transition(asset,row,stamp,cfg):
    if asset['phase'] in ('cancelled','expired'):return None
    price=row['quote']['price'];bars=row.get('series',{}).get('15m',[])
    if price<=asset['invalid']:
        asset.update(phase='cancelled',reason='korunması gereken destek kaybedildi');return 'cancelled'
    expiry=(asset['created_ms']+cfg['setup_hours']*3600000 if asset['phase']=='preparation' else
            asset['triggered_ms']+cfg['trigger_watch_hours']*3600000)
    if stamp>=expiry:asset.update(phase='expired',reason='izleme süresi doldu');return 'expired'
    if asset['phase']=='triggered' or not bars:return None
    for i,b in enumerate(bars):
        close=b['t']+900000
        if close>stamp or close<=max(asset['created_ms'],asset.get('last_evaluated_close_ms',0)):continue
        asset['last_evaluated_close_ms']=close
        if b['c']<=asset['invalid']:
            asset.update(phase='cancelled',reason='kapalı mum desteği kaybetti');return 'cancelled'
        a=asset['atr'];level=asset['level'];prior=bars[max(0,i-20):i]
        med=median(x['v'] for x in prior) if len(prior)==20 else 0
        rvol=b['v']/med if med>0 else 0
        if not asset.get('break_close_ms'):
            if b['c']>level and rvol>=cfg['trigger_volume_ratio'] and (b['c']-b['l'])/max(b['h']-b['l'],1e-20)>=.65:
                asset.update(break_close_ms=close,break_volume=b['v'])
            continue
        if b['c']<level-.2*a:
            asset.update(phase='cancelled',reason='kırılan direnç üzerinde tutunamadı');return 'cancelled'
        if not asset.get('retest_close_ms'):
            if close>asset['break_close_ms'] and level-.2*a<=b['l']<=level+.25*a and b['c']>=level and b['c']>=b['o'] and b['v']<=asset['break_volume']:
                asset.update(retest_close_ms=close,retest_low=b['l'],retest_high=b['h'])
            continue
        if b['l']<asset['retest_low']-.15*a:
            asset.update(phase='cancelled',reason='geri test desteği kaybedildi');return 'cancelled'
        if close-asset['retest_close_ms']>cfg['maximum_reclaim_bars']*900000:
            asset.update(phase='expired',reason='geri test sonrası teyit süresi doldu');return 'expired'
        if close>asset['retest_close_ms'] and b['c']>asset['retest_high'] and b['c']>b['o']:
            asset['reclaim_close_ms']=close
    latest=bars[-1]['t']+900000
    if not asset.get('reclaim_close_ms') or asset['reclaim_close_ms']!=latest:return None
    if not 0<=stamp-latest<=cfg['max_confirmation_age_minutes']*60000:return None
    plan=entry_plan(asset,row,cfg);asset['entry_check']=plan
    if plan['reasons']:return None
    asset.update(phase='triggered',triggered_ms=stamp,trigger_price=price,invalid=plan['stop'],
        target=plan['target'],risk_pct=plan['risk_pct'],overhead_room_r=plan['net_room_r'],
        trigger_kind='kırılım + geri test + sonraki kapalı mumda güçlenme',trigger_bar_close_ms=latest,
        entry_plan=plan,strict_short_confirmed=row['derivatives']['strict_short_confirmed'])
    return 'triggered'

def register(state,asset,row,stamp):
    key=asset['symbol']
    if key in state['measurements']['cases'] or row.get('btc_quote') is None:return
    state['measurements']['cases'][key]={'symbol':key,'exchange':asset['exchange'],'phase':'triggered',
        'asset_id':asset['id'],'observed_ms':stamp,'entry_price':row['quote']['price'],
        'btc_entry_price':row['btc_quote']['price'],'controls':[],'outcomes':{},'stop':asset['invalid'],
        'target':asset['target'],'risk_pct':asset['risk_pct'],'strict_short_confirmed':asset['strict_short_confirmed'],
        'short_information':row['derivatives']['short_information'],
        'source_close_ms':asset['trigger_bar_close_ms'],'observation_lag_ms':stamp-asset['trigger_bar_close_ms']}

def enqueue(state,asset,phase,row,stamp):
    if phase=='preparation':return None
    e=v1.enqueue(state,asset,phase,row,stamp)
    e.update(version='coin-tarama-5-v2',target=asset.get('target'),entry_plan=asset.get('entry_plan'),
             source_close_ms=asset.get('trigger_bar_close_ms'),strict_short_confirmed=asset.get('strict_short_confirmed'))
    return e
