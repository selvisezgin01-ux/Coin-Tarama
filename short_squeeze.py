"""Independent prospective short-squeeze research using frozen Coin Tarama 3 features."""
from copy import deepcopy
import hashlib,json
from pathlib import Path
import strength_v5_watch as base
import strength_v5_priority as priority
from short_squeeze_sources import num,recent
from study_dataset import STEP

ROOT=Path(__file__).parent
CONFIG=ROOT/'short_squeeze_config.json'
REASONS={'technical':'Coin Tarama 3 işlem koşulu ön elemesini geçmedi',
 'not_listed':'aynı borsada eşleşen aktif USDT sürekli vadeli kontrat yok',
 'market_data_unknown':'vadeli veri eksik/eski', 'funding_unknown':'fonlama verisi eksik/eski',
 'funding':'yeterince negatif fonlama yok','warming':'uygun aralıkta önceki gerçek OI gözlemi birikiyor',
 'oi_growth':'toplam açık pozisyon artışı yetersiz','price_weak':'vadeli fiyat önceki gözlemin altında',
 'extended':'fiyat gözlem aralığında fazla yükselmiş','futures_spread':'vadeli makas geniş',
 'oi_liquidity':'açık pozisyon büyüklüğü yetersiz','basis':'spot-vadeli fiyat farkı yüksek veya fiyat eksik'}


def fingerprint():
    digest=hashlib.sha256()
    for name in ['short_squeeze.py','short_squeeze_sources.py','short_squeeze_scan.py','short_squeeze_config.json']:
        digest.update(name.encode());digest.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    digest.update(base.fingerprint().encode());digest.update(priority.fingerprint().encode())
    return digest.hexdigest()


def new_state():
    return {'version':'shortcu-kistir-v1','rules_fingerprint':fingerprint(),'source_fingerprint':base.fingerprint(),
        'history':{},'active':[],'active_venues':{},'last_sent':{},'pending':[],'delivery_audit':[]}


def technical_rows(scans,policy,stamp):
    eligible=[];rejected=[];errors={}
    for venue,result in scans.items():
        if 'error' in result:errors[venue]=result['error'];continue
        if result.get('feature_cutoff_ms')!=stamp//STEP*STEP:
            errors[venue]='Coin Tarama 3 closed 4h source is stale/missing';continue
        for original in result.get('candidates',[]):
            row=deepcopy(original);row['exchange']=venue;row['feature_cutoff_ms']=result['feature_cutoff_ms']
            reasons,metrics=priority.reasons_for(row,policy,stamp)
            if reasons:rejected.append({'exchange':venue,'symbol':row['symbol'],'reasons':reasons})
            else:row['priority_metrics']=metrics;eligible.append(row)
    eligible.sort(key=lambda r:priority.rank_key(r,policy))
    return eligible,rejected,errors


def baseline(history,current,config):
    target=config['baseline_hours']*3600000;tolerance=config['baseline_tolerance_minutes']*60000
    valid=[]
    for point in history:
        if point.get('contract')!=current['contract'] or point.get('contract_size')!=current['contract_size']:continue
        elapsed=current['observed_ms']-point['observed_ms']
        if target-tolerance<=elapsed<=target+tolerance and num(point.get('oi_contracts')) is not None and point['oi_contracts']>0:
            if num(point.get('mid_price')) is None or point['mid_price']<=0:continue
            if abs(point.get('price_ms',0)-point['observed_ms'])>5*60000:continue
            valid.append(point)
    return min(valid,key=lambda p:abs(current['observed_ms']-p['observed_ms']-target)) if valid else None


def decide(row,market,funding,history,config,stamp):
    result={'symbol':row['symbol'],'exchange':row['exchange'],'reasons':[],'status':'watch','metrics':{}}
    if market is None:return {**result,'reasons':['not_listed']}
    if not recent(market.get('observed_ms'),stamp,config['max_data_age_minutes']) or not recent(market.get('price_ms'),stamp,config['max_data_age_minutes']):
        return {**result,'status':'unknown','reasons':['market_data_unknown']}
    metrics={'oi_contracts':market['oi_contracts'],'oi_notional':market['oi_notional'],
        'oi_notional_kind':market['notional_kind'],'contract':market['contract'],'futures_observed_ms':market['observed_ms'],
        'futures_mid':market['mid_price'],'futures_spread_pct':market['spread_pct']}
    reasons=[]
    if market['spread_pct']>config['maximum_futures_spread_pct']:reasons.append('futures_spread')
    if market['oi_notional']<config['minimum_oi_notional']:reasons.append('oi_liquidity')
    spot=num(row.get('mid_price'));future=market['mid_price']
    basis=abs(future/spot-1)*100 if spot is not None and spot>0 else None
    metrics['basis_pct']=basis
    if basis is None or basis>config['maximum_spot_futures_basis_pct']:reasons.append('basis')
    if not funding or not recent(funding.get('observed_ms'),stamp,config['max_data_age_minutes']):reasons.append('funding_unknown')
    else:
        metrics.update({'funding_rate':funding['rate'],'funding_hours':funding['interval_hours'],
            'funding_scaled_8h':funding['scaled_8h_rate'],'funding_observed_ms':funding['observed_ms']})
        if funding['scaled_8h_rate']>config['funding_scaled_8h_max']:reasons.append('funding')
    old=baseline(history,market,config)
    if old is None:reasons.append('warming')
    else:
        oi_change=(market['oi_contracts']/old['oi_contracts']-1)*100
        price_change=(future/old['mid_price']-1)*100
        metrics.update(oi_change_pct=oi_change,futures_price_change_pct=price_change,
            elapsed_hours=(market['observed_ms']-old['observed_ms'])/3600000,baseline_ms=old['observed_ms'])
        if oi_change<config['oi_change_min_pct']:reasons.append('oi_growth')
        if price_change<config['futures_price_change_min_pct']:reasons.append('price_weak')
        if price_change>config['futures_price_change_max_pct']:reasons.append('extended')
    status='candidate' if not reasons else ('unknown' if 'funding_unknown' in reasons else ('warming' if 'warming' in reasons else 'watch'))
    return {**result,'status':status,'reasons':reasons,'metrics':metrics}


def record_history(state,venue,markets,config,stamp):
    fields=['contract','contract_size','observed_ms','price_ms','oi_contracts','mid_price']
    for market in markets.values():
        key=venue+':'+market['contract'];history=state['history'].setdefault(key,[])
        point={k:market[k] for k in fields}
        # A second run of one provider snapshot cannot manufacture another observation.
        same=[p for p in history if p['observed_ms']==point['observed_ms']]
        if same and any(p!=point for p in same):continue
        if not same:history.append(point)
    minimum=stamp-config['history_days']*86400000
    state['history']={key:[p for p in history if p['observed_ms']>=minimum][-100:]
        for key,history in state['history'].items() if history and history[-1]['observed_ms']>=minimum}


def select(decisions,config):
    candidates=[deepcopy(d) for d in decisions if d['status']=='candidate']
    candidates.sort(key=lambda d:(d['metrics']['funding_scaled_8h'],-d['metrics']['oi_change_pct'],
        d['metrics']['futures_spread_pct'],d['symbol'],d['exchange']))
    unique={}
    for d in candidates:
        if d['symbol'] not in unique:unique[d['symbol']]=d
    return list(unique.values())[:config['max_unique_symbols']]


def queue(state,selected,failed,config,stamp):
    for batch in state['pending']:batch['obsolete']=True
    active=set(state['active']);fresh=[]
    for row in selected:
        last=state['last_sent'].get(row['symbol'])
        if last is None or (row['symbol'] not in active and stamp-last>=config['cooldown_hours']*3600000):fresh.append(row)
    if fresh:
        identifier=hashlib.sha256(json.dumps([[r['symbol'],r['exchange'],r['row']['observed_ms']] for r in fresh],sort_keys=True).encode()).hexdigest()[:24]
        state['pending'].append({'id':identifier,'created_ms':stamp,'candidates':fresh,'obsolete':False})
    preserved={s:v for s,v in state['active_venues'].items() if v in failed}
    state['active_venues']={**preserved,**{r['symbol']:r['exchange'] for r in selected}}
    state['active']=sorted(state['active_venues'])
