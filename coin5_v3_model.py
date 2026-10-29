"""Broad discovery, causal early radar and separate risk-controlled retest entry."""
import json,hashlib,math
from pathlib import Path
from copy import deepcopy
from statistics import median
import coin5_model as core
from coin5_v2_model import pivots,fingerprint as previous_fingerprint
ROOT=Path(__file__).parent
def config():return json.loads((ROOT/'coin5_v3_config.json').read_text(encoding='utf-8'))
def fingerprint():
    h=hashlib.sha256()
    for n in ('coin5_v3_model.py','coin5_v3_sources.py','coin5_v3_scan.py','coin5_v3_measure.py','coin5_v3_worker.py','coin5_v3_config.json',
              'coin5_model.py','coin5_v2_model.py','coin5_v2_measure.py','coin5_v2_worker.py','coin5_scan.py',
              'short_squeeze_positions.py','short_squeeze_sources.py','parabolic_sar.py','support_indicators.py','study_config.json','strength_v5_priority_config.json'):
        h.update(n.encode());h.update((ROOT/n).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return h.hexdigest()
def new_state():return {'version':'coin-tarama-5-v3','rules_fingerprint':fingerprint(),'venues':{},'cache':{},'quote_history':{},
    'cursor':{},'oi_history':{},'ratio_history':{},'provider_backoff':{},'assets':{},'last_closed':{},'pending':[],
    'delivery':[],'runs':[],'measurements':{'cases':{},'errors':[]}}
def migrate(old,sha,stamp):
    if old.get('version')!='coin-tarama-5-v2':raise ValueError('Expected explicit V2 archive')
    if old.get('rules_fingerprint')!=previous_fingerprint():raise ValueError('Unexpected V2 fingerprint')
    s=new_state();s['archive']={'source_branch':'scanner-state-coin-tarama-5-v2','source_sha':sha,
        'source_state_sha256':hashlib.sha256(json.dumps(old,sort_keys=True,allow_nan=False).encode()).hexdigest(),
        'observed_ms':stamp,'old_entries_replayed':False,'old_records':deepcopy({k:old[k] for k in ('assets','measurements','delivery','pending','migration') if k in old})}
    return s

def priority(q,history,stamp):
    candidates=[p for p in history if 240000<=stamp-p['observed_ms']<=600000]
    old=min(candidates,key=lambda p:abs(stamp-p['observed_ms']-300000)) if candidates else None
    change=(q['last']/old['last']-1)*100 if old else None
    rolling=(q['volume24']/old['volume24']-1)*100 if old and old['volume24']>0 else None
    score=max(change or 0,0)*5+min(max(q.get('return24_pct') or 0,0),20)*.04+math.log10(max(q['volume24'],1))*.02+min(max(rolling or 0,0),20)*.15
    return {'score':score,'change5m_pct':change,'rolling24h_turnover_change_pct':rolling,
        'baseline_ms':old['observed_ms'] if old else None,'turnover_note':'rolling24h change is ranking only, not five-minute buy volume'}
def remember_quotes(state,quotes,stamp):
    for key,q in quotes.items():
        hist=state['quote_history'].setdefault(key,[])
        if not any(p['observed_ms']==q['observed_ms'] for p in hist):hist.append({k:q[k] for k in ('observed_ms','last','volume24')})
        state['quote_history'][key]=[p for p in hist if 0<=stamp-p['observed_ms']<=3600000][-16:]
    state['quote_history']={k:v for k,v in state['quote_history'].items() if v and stamp-v[-1]['observed_ms']<=3600000}
def select(quotes,state,group,cfg,stamp):
    ranked=sorted(quotes,key=lambda k:(-priority(quotes[k],state['quote_history'].get(k,[]),stamp)['score'],k))
    active=[a['key'] for a in state['assets'].values() if a['group']==group and a['phase'] in ('radar','triggered') and a['key'] in quotes]
    chosen=list(dict.fromkeys(active+ranked[:cfg['dynamic_per_group']]))
    remaining=sorted(set(ranked)-set(chosen));cursor=state['cursor'].get(group,0)
    rotate=[remaining[(cursor+i)%len(remaining)] for i in range(min(len(remaining),cfg['rotate_per_group']))] if remaining else []
    state['cursor'][group]=(cursor+len(rotate))%max(1,len(remaining))
    return list(dict.fromkeys(chosen+rotate))[:cfg['maximum_charts_per_group']]

def radar(bs,cfg):
    if len(bs)<41:return {'valid':False,'reasons':['insufficient_history']}
    a=core.atr(bs);b=bs[-1];prior=bs[-21:-1];med=median(x['v'] for x in prior)
    if a<=0 or med<=0:return {'valid':False,'reasons':['flat_price_or_volume']}
    level=max(x['h'] for x in bs[-9:-1]);rvol=b['v']/med;where=(b['c']-b['l'])/max(b['h']-b['l'],1e-20)
    ema=core.ema([x['c'] for x in bs]);breakout=b['c']>level
    turning=b['c']>bs[-2]['h'] and b['c']>=ema[-1]
    box=bs[-5:-1];flat=(max(x['h'] for x in box)-min(x['l'] for x in box))<=3*a and abs(box[-1]['c']-box[0]['o'])<=1.5*a
    reasons=[]
    if rvol<cfg['radar_volume_ratio']:reasons.append('volume_not_accelerating')
    if b['c']<=b['o'] or where<.6:reasons.append('close_not_strong')
    if not (breakout or turning or (flat and b['c']>=level-.5*a)):reasons.append('price_structure_not_ready')
    hour=(b['c']/bs[-5]['c']-1)*100
    if b['c']-ema[-1]>cfg['maximum_radar_ema_extension_atr']*a or hour>cfg['maximum_recent_gain_pct']:reasons.append('already_extended')
    return {'valid':not reasons,'reasons':reasons,'level':level,'base_invalid':min(x['l'] for x in bs[-9:-1])-.15*a,
        'atr':a,'rvol':rvol,'close_position':where,'breakout':breakout,'bar_close_ms':b['t']+900000,
        'kind':'hacimli kırılım' if breakout else 'erken dönüş / hacimlenme','recent_hour_pct':hour,
        'score':min(rvol,6)+where+(1 if breakout else .5)}

def context(series,btc):
    m,h,f=series['15m'],series.get('1h'),series.get('4h');c={'atr':core.atr(m),'reasons':[],'support_warnings':[]}
    if h and btc:
        rel=(h[-1]['c']/h[-2]['c']-1)*100-(btc[-1]['c']/btc[-2]['c']-1)*100
        c.update(relative1h_pp=rel,btc_hour_pct=(btc[-1]['c']/btc[-2]['c']-1)*100)
    else:c.update(relative1h_pp=None,btc_hour_pct=None)
    if f:
        e=core.ema([b['c'] for b in f]);c['trend4h_support']=f[-1]['c']>=e[-1]
    else:c['trend4h_support']=None
    if c['trend4h_support'] is False:c['support_warnings'].append('4s trend henüz teyitsiz')
    return c

def oi_support(q,history):
    if q['kind']!='PERP' or not q.get('oi_contracts') or q['oi_contracts']<=0:return {'status':'unknown_or_not_applicable','market':q['key']}
    old=[p for p in history if p.get('oi_contracts',0)>0 and 2700000<=q['provider_ms']-p['provider_ms']<=4500000 and p['contract']==q['contract'] and p.get('contract_size')==q.get('contract_size')]
    if not old:return {'status':'warming','market':q['key']}
    p=min(old,key=lambda p:abs(q['provider_ms']-p['provider_ms']-3600000))
    return {'status':'observed','market':q['key'],'change_pct':(q['oi_contracts']/p['oi_contracts']-1)*100,
        'old_ms':p['provider_ms'],'current_ms':q['provider_ms'],'new_short_opening_proven':False}

def plan(a,row,cfg):
    q=row['quote'];price=q['price'];atr=row['context']['atr'];stop=max(a['base_invalid'],a['retest_low']-.15*a['atr'])
    risk=(price-stop)/price*100;cost=cfg['planning_cost_pct'];target=price*(1+(2*(risk+cost)+cost)/100)
    levels=[h for k in ('1h','4h') for h in pivots(row['series'].get(k,[])) if h>price]
    resistance=min(levels) if levels else None;why=[]
    if not 0<risk<=cfg['maximum_risk_pct']:why.append('risk_outside_limit')
    if q['spread_pct']>cfg['maximum_entry_spread_pct']:why.append('entry_spread')
    if price<a['retest_high'] or price>a['retest_high']+.5*atr:why.append('entry_outside_retest_zone')
    if price-a['level']>2*atr:why.append('too_far_from_breakout')
    if resistance is not None and resistance<target:why.append('known_resistance_blocks_target')
    shock=row['context'].get('btc_hour_pct')
    if shock is None:why.append('btc_context_unknown')
    elif shock<=-2:why.append('btc_shock')
    if row.get('book_reasons'):why.extend(row['book_reasons'])
    return {'reasons':why,'stop':stop,'target':target,'risk_pct':risk,'planning_cost_pct':cost,
        'resistance':resistance,'target_kind':'known_overhead_room' if resistance else 'projected_2R_resistance_unknown',
        'entry_zone_low':a['retest_high'],'entry_zone_high':a['retest_high']+.5*atr}

def transition(a,row,stamp,cfg):
    if a['phase'] in ('cancelled','expired'):return None
    if row['quote']['price']<=a['invalid']:
        a.update(phase='cancelled',reason='destek kaybedildi');return 'cancelled'
    deadline=a.get('triggered_ms',a['created_ms'])+(cfg['trigger_watch_hours'] if a['phase']=='triggered' else cfg['setup_hours'])*3600000
    if stamp>=deadline:a.update(phase='expired',reason='izleme süresi doldu');return 'expired'
    if a['phase']=='triggered':return None
    bs=row['series']['15m'];level=a['level'];atr=a['atr']
    for i,b in enumerate(bs):
        close=b['t']+900000
        if close>stamp or close<=max(a['created_ms'],a.get('last_evaluated_close_ms',0)):continue
        a['last_evaluated_close_ms']=close
        if b['l']<=a['invalid']:a.update(phase='cancelled',reason='sonraki kapalı mum desteğe dokundu');return 'cancelled'
        if not a.get('break_close_ms'):
            med=median(x['v'] for x in bs[max(0,i-20):i]) if i>=20 else 0
            if med>0 and b['c']>level and b['v']>=cfg['radar_volume_ratio']*med and b['c']>b['o']:
                a.update(break_close_ms=close,break_volume=b['v'])
            continue
        if b['c']<level-.3*atr:a.update(phase='cancelled',reason='kırılım tutunamadı');return 'cancelled'
        if not a.get('retest_close_ms'):
            if close>a['break_close_ms'] and level-.3*atr<=b['l']<=level+.5*atr and b['c']>=level and b['v']<=a['break_volume']:
                a.update(retest_close_ms=close,retest_low=b['l'],retest_high=b['h'])
            continue
        if b['l']<a['retest_low']-.15*atr:a.update(phase='cancelled',reason='geri test dibi kaybedildi');return 'cancelled'
        if close-a['retest_close_ms']>3600000:a.update(phase='expired',reason='geri test teyidi gecikti');return 'expired'
        if close>a['retest_close_ms'] and b['c']>a['retest_high'] and b['c']>b['o']:a['reclaim_close_ms']=close
    latest=bs[-1]['t']+900000
    if a.get('reclaim_close_ms')!=latest or not 0<=stamp-latest<=900000:return None
    p=plan(a,row,cfg);a['entry_check']=p
    if p['reasons']:return None
    a.update(phase='triggered',triggered_ms=stamp,trigger_price=row['quote']['price'],invalid=p['stop'],
        target=p['target'],risk_pct=p['risk_pct'],entry_plan=p,trigger_bar_close_ms=latest)
    return 'triggered'
