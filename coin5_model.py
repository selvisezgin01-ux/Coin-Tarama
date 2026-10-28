"""Causal setup/trigger/invalidation rules, separate version and real observation entries."""
import hashlib,json,math
from copy import deepcopy
from pathlib import Path
from statistics import median
import pandas as pd
from parabolic_sar import parabolic_sar
from support_indicators import rsi_wilder
from short_squeeze_positions import num

ROOT=Path(__file__).parent
def config():return json.loads((ROOT/'coin5_config.json').read_text(encoding='utf-8'))
def fingerprint():
    digest=hashlib.sha256()
    for name in ('coin5_config.json','coin5_model.py','coin5_sources.py','coin5_scan.py','short_squeeze_sources.py',
                 'short_squeeze_positions.py','short_squeeze_lab.py','parabolic_sar.py','support_indicators.py',
                 'study_config.json','strength_v5_priority_config.json'):
        digest.update(name.encode());digest.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return digest.hexdigest()
def new_state():
    return {'version':'coin-tarama-5-v1','rules_fingerprint':fingerprint(),'venues':{},'cache':{},'oi_history':{},
            'ratio_history':{},'assets':{},'last_closed':{},'pending':[],'delivery':[],
            'measurements':{'cases':{},'errors':[]}}

def ema(values,n=20):
    result=[];x=values[0]
    for v in values:x=x+(v-x)*2/(n+1);result.append(x)
    return result
def atr(rows):
    tr=[max(b['h']-b['l'],abs(b['h']-a['c']),abs(b['l']-a['c'])) for a,b in zip(rows,rows[1:])]
    x=sum(tr[:14])/14
    for v in tr[14:]:x=(13*x+v)/14
    return x
def context(series,btc,cfg):
    m,h,f=series['15m'],series['1h'],series['4h'];a=atr(m);ha=atr(h);fa=atr(f)
    if min(a,ha,fa)<=0:raise ValueError('Flat ATR cannot define risk')
    he=ema([x['c'] for x in h]);fe=ema([x['c'] for x in f]);reasons=[]
    if f[-1]['c']<fe[-1]-fa:reasons.append('4h_structure_weak')
    if h[-1]['c']<he[-1]-.5*ha or he[-1]<he[-4]-.2*ha:reasons.append('1h_structure_weak')
    relative=(h[-1]['c']/h[-2]['c']-1)*100-(btc[-1]['c']/btc[-2]['c']-1)*100
    if relative<0:reasons.append('btc_relative_weak')
    frame=pd.DataFrame({'high':[b['h'] for b in m],'low':[b['l'] for b in m],'close':[b['c'] for b in m]})
    sar=parabolic_sar(frame)
    return {'reasons':reasons,'atr':a,'relative1h_pp':relative,'rsi14':float(rsi_wilder(frame['close']).iloc[-1]),
            'sar_below':bool(sar['sar_below'].iloc[-1]) if 'sar_below' in sar else bool(sar['sar'].iloc[-1]<m[-1]['c']),
            'ema4h':fe[-1],'ema1h':he[-1]}

def preparation(series,ctx,cfg):
    m=series['15m'];box=m[-cfg['box_bars']:];a=ctx['atr'];high=max(b['h'] for b in box);low=min(b['l'] for b in box)
    width=(high-low)/a;net=abs(box[-1]['c']-box[0]['o'])/a
    defended=min(b['l'] for b in box[-2:])>=min(b['l'] for b in box[:2])-.2*a
    down_old=[b['v'] for b in m[-12:-4] if b['c']<b['o']];down_new=[b['v'] for b in box if b['c']<b['o']]
    selling_fades=not down_new or bool(down_old and median(down_new)<=median(down_old))
    valid=not ctx['reasons'] and width<=cfg['maximum_box_atr'] and net<=cfg['maximum_box_net_atr'] and (high/low-1)*100<=cfg['maximum_box_range_pct'] and defended and selling_fades
    return {'valid':valid,'level':high,'invalid':low-.15*a,'atr':a,'box_atr':width,
            'box_net_atr':net,'selling_fades':selling_fades,'bar_close_ms':m[-1]['t']+900000}

def baseline(history,stamp,cfg,field='observed_ms'):
    target=cfg['baseline_minutes'];tol=cfg['baseline_tolerance_minutes'];choices=[]
    for p in history:
        age=(stamp-p[field])/60000
        if target-tol<=age<=target+tol:choices.append(p)
    return min(choices,key=lambda p:abs((stamp-p[field])/60000-target)) if choices else None

def derivative_context(market,funding,oi_history,points,ratio_history,cfg,stamp):
    result={'ready':False,'reasons':[],'profiles':{},'negative_funding':None,'score':0}
    if market is None:return {**result,'reasons':['futures_unknown']}
    if stamp-market['observed_ms']>300000 or market['observed_ms']>stamp+60000:return {**result,'reasons':['futures_stale']}
    old=baseline(oi_history,market['observed_ms'],cfg)
    if old is None:result['reasons'].append('oi_baseline_warming')
    elif old['contract']!=market['contract'] or old['contract_size']!=market['contract_size']:result['reasons'].append('oi_identity_changed')
    else:
        growth=(market['oi_contracts']/old['oi_contracts']-1)*100;price=(market['mid_price']/old['mid_price']-1)*100
        result.update(oi_change_pct=growth,price_change_pct=price,oi_old_ms=old['observed_ms'],oi_ms=market['observed_ms'])
        if growth<cfg['minimum_oi_growth_pct']:result['reasons'].append('oi_growth_insufficient')
        if not cfg['minimum_baseline_price_change_pct']<=price<=cfg['maximum_baseline_price_change_pct']:result['reasons'].append('price_not_holding_or_extended')
    supports=[]
    for provider,p in points.items():
        detail={'status':p['status'],'scope':p['scope']}
        if p['status']=='observed' and 0<=stamp-p['provider_ms']<=cfg['max_provider_age_minutes']*60000:
            prev=baseline(ratio_history.get(provider,[]),p['provider_ms'],cfg,field='provider_ms')
            detail.update(short_pct=p['short_pct'],long_pct=p['long_pct'],provider_ms=p['provider_ms'])
            if prev and (prev['scope'],prev['symbol'])==(p['scope'],p['symbol']):
                detail.update(change_pp=p['short_pct']-prev['short_pct'],previous_short_pct=prev['short_pct'],old_ms=prev['provider_ms'])
                detail['supports']=detail['change_pp']>=cfg['minimum_short_increase_pp']
                if detail['supports']:supports.append(provider)
            else:detail['status']='baseline_warming'
        result['profiles'][provider]=detail
    if not supports:result['reasons'].append('short_increase_unconfirmed')
    # Different populations remain separate. One source can support, conflict is visible.
    result['supporting_sources']=supports
    result['opposing_sources']=[p for p,d in result['profiles'].items() if d.get('change_pp',0)<=-cfg['minimum_short_increase_pp']]
    if funding and 0<=stamp-funding['observed_ms']<=300000:
        result['negative_funding']=funding['scaled_8h_rate']<0;result['funding_8h_pct']=funding['scaled_8h_rate']*100
    result['ready']=not result['reasons'];result['score']=len(supports)*2+(1 if result['negative_funding'] else 0)
    return result

def remember(history,point,field,stamp,max_hours=4):
    # First observation at a provider timestamp is immutable; revisions don't fake changes.
    if not any(p[field]==point[field] for p in history):history.append(deepcopy(point))
    history[:]=sorted([p for p in history if 0<=stamp-p[field]<=max_hours*3600000],key=lambda p:p[field])[-60:]

def transition(asset,row,stamp,cfg):
    """Missing positive evidence holds state; verified loss or expiry closes it."""
    phase=asset['phase'];quote=row['quote'];series=row['series'];bar=series.get('15m',[None])[-1];a=asset['atr']
    if phase in ('cancelled','expired'):return None
    expiry=asset['created_ms']+cfg['setup_hours']*3600000 if phase=='preparation' else asset['triggered_ms']+cfg['trigger_watch_hours']*3600000
    if quote['price']<=asset['invalid'] or (bar and bar['t']+900000>asset['created_ms'] and bar['c']<=asset['invalid']):
        asset['phase']='cancelled';asset['reason']='korunması gereken destek kaybedildi';return 'cancelled'
    if stamp>=expiry:asset['phase']='expired';asset['reason']='izleme süresi doldu';return 'expired'
    if phase=='triggered':return None
    if bar is None:return None
    closed=bar['t']+900000
    if closed<=asset['created_ms'] or closed<=asset.get('last_evaluated_close_ms',0):return None
    asset['last_evaluated_close_ms']=closed
    level=asset['level'];current_a=row['context']['atr'];prior=series['15m'][-21:-1];v=median(b['v'] for b in prior)
    rvol=bar['v']/v if v>0 else 0
    breakout=bar['c']>level and rvol>=cfg['trigger_volume_ratio'] and (bar['c']-bar['l'])/max(bar['h']-bar['l'],1e-20)>=.65
    if breakout and not asset.get('break_close_ms'):
        asset['break_close_ms']=closed;asset['break_volume']=bar['v']
    retest=bool(asset.get('break_close_ms') and closed>asset['break_close_ms'] and level-.2*a<=bar['l']<=level+.25*a and
                bar['c']>=level and bar['v']<=asset['break_volume'] and bar['c']>=bar['o'])
    risk=(quote['price']-asset['invalid'])/quote['price']*100
    overhead=[b['h'] for b in series['4h'][-24:] if b['h']>quote['price']]
    room=None if not overhead else (min(overhead)-quote['price'])/(quote['price']-asset['invalid']) if quote['price']>asset['invalid'] else 0
    good=(not row['context']['reasons'] and row['derivatives']['ready'] and quote['price']>=level and
          quote['price']-level<=cfg['maximum_trigger_extension_atr']*current_a and abs(quote['price']-bar['c'])<=current_a and
          0<risk<=cfg['maximum_risk_pct'] and (room is None or room>=cfg['minimum_overhead_room_r']))
    if (breakout or retest) and good:
        asset.update(phase='triggered',triggered_ms=stamp,trigger_price=quote['price'],trigger_kind='geri test' if retest else 'hacimli kırılım',
                     risk_pct=risk,overhead_room_r=room,trigger_bar_close_ms=closed)
        return 'triggered'
    return None

def enqueue(state,asset,phase,row,stamp):
    event={'id':hashlib.sha256((asset['id']+':'+phase).encode()).hexdigest()[:24],'asset_id':asset['id'],
           'symbol':asset['symbol'],'exchange':asset['exchange'],'phase':phase,'observed_ms':stamp,
           'signal_ms':stamp,
           'price':row['quote']['price'],'level':asset['level'],'invalid':asset['invalid'],'reason':asset.get('reason'),
           'derivatives':deepcopy(row['derivatives']),'context':deepcopy(row['context']),
           'trigger_kind':asset.get('trigger_kind'),'overhead_room_r':asset.get('overhead_room_r')}
    if not any(e['id']==event['id'] for e in state['pending']) and not any(e['id']==event['id'] for e in state['delivery']):state['pending'].append(event)
    return event

def register_measurement(state,asset,phase,row,stamp):
    key=asset['symbol']+':'+phase
    if key in state['measurements']['cases']:return
    if row.get('btc_quote') is None:return # Retry only at a later real observation.
    state['measurements']['cases'][key]={'symbol':asset['symbol'],'exchange':asset['exchange'],'phase':phase,
         'asset_id':asset['id'],'observed_ms':stamp,'entry_price':row['quote']['price'],
         'btc_entry_price':row['btc_quote']['price'],'controls':[], 'outcomes':{}}
