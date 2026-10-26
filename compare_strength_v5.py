"""Frozen retrospective smoke check, including losers, not an executable-profit backtest."""
from __future__ import annotations
import hashlib
import json
import math
import os
from pathlib import Path
import numpy as np
import pandas as pd
import strength_v4 as baseline
import strength_v5 as extended
from strength_v4_scan import last_segment
from study_dataset import STEP,read_json,load_history

ROOT=Path(__file__).resolve().parent
PROJECT=Path(os.environ.get('COIN_ARCHIVE_ROOT',str(ROOT)))
OUT=ROOT/'comparison'


def clean(value):
    if isinstance(value,dict):return {k:clean(v) for k,v in value.items()}
    if isinstance(value,list):return [clean(v) for v in value]
    if isinstance(value,(np.bool_,np.integer)):return value.item()
    if isinstance(value,(np.floating,float)):return float(value) if np.isfinite(value) else None
    return value


def save(name,value):
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/name).write_text(json.dumps(clean(value),ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')


def run():
    cfg=read_json(ROOT/'strength_v5_config.json');old=read_json(ROOT/'strength_v4_config.json')
    freeze={'config':cfg,'hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            for name in ('strength_v5.py','strength_v5_config.json','compare_strength_v5.py')}}
    if (OUT/'design_frozen.json').exists() and read_json(OUT/'design_frozen.json')!=freeze:raise ValueError('Do not tune after reading this comparison')
    save('design_frozen.json',freeze)
    btc,_=load_history(PROJECT/'data/study/history/BTCUSDT.json');btc=last_segment(btc)
    br=(btc.close/btc.close.shift(6)-1)*100;br.attrs['return8']=(btc.close/btc.close.shift(2)-1)*100
    models={name:{} for name in ['original_v4','extended_v5','early_reversal','sideways_volume','retest']}
    frames={};pool=[];audits=[]
    paths=sorted((PROJECT/'data/study/history').glob('*.json'))
    for path in paths:
        symbol=path.stem
        if symbol=='BTCUSDT':continue
        try:
            frame,audit=load_history(path);frame=last_segment(frame)
            if len(frame)<cfg['minimum_history_bars']:raise ValueError('Insufficient contiguous history')
            frames[symbol]=frame
            old_rows=baseline.features(frame,br,old);new=extended.features(frame,br,cfg)
            models['original_v4'][symbol]=old_rows.qualified
            models['extended_v5'][symbol]=new.qualified
            for group in ('early_reversal','sideways_volume','retest'):models[group][symbol]=new['group_'+group]
            eligible=new[new.gate_history & new.gate_liquidity & (new.atr>0)][['close','atr','quote_volume24']].copy()
            eligible['symbol']=symbol;pool.append(eligible)
            audits.append({'symbol':symbol,'rows':len(frame),'source_gaps':audit['gaps']})
        except (ValueError,KeyError,FileNotFoundError,TypeError) as exc:audits.append({'symbol':symbol,'error':str(exc)})
        if len(audits)%40==0:print('Comparison histories '+str(len(audits))+'/'+str(len(paths)-1),flush=True)
    all_pool=pd.concat(pool).reset_index(names='stamp');by_time={stamp:g for stamp,g in all_pool.groupby('stamp')}
    known=set(cfg['design_examples']);events=[]
    for name,tokens in models.items():
        for symbol,signals in tokens.items():
            previous=-10**20;frame=frames[symbol]
            for stamp in signals[signals].index:
                if stamp-previous<48*3600000:continue
                previous=stamp;cohort=by_time[stamp]
                subject=cohort[cohort.symbol==symbol].iloc[0]
                controls=cohort[(cohort.symbol!=symbol)&~cohort.symbol.isin(known)].copy()
                controls['distance']=(np.abs(np.log(controls.quote_volume24/subject.quote_volume24))+
                    np.abs(np.log((controls.atr/controls.close)/(subject.atr/subject.close))))
                choices=list(controls.sort_values(['distance','symbol']).head(3).symbol)
                event={'model':name,'symbol':symbol,'known_design_example':symbol in known,'decision_ms':int(stamp+STEP),
                       'reference_closed_price':float(frame.loc[stamp,'close']),'controls':choices,'outcomes':{}}
                for hours in (12,24,48):
                    endpoint=stamp+hours//4*STEP;value={'return_pct':None,'btc_excess_pct_points':None,'control_excess_pct_points':None,'mae_pct':None}
                    expected=np.arange(stamp,endpoint+1,STEP)
                    if endpoint in frame.index and frame.index.isin(expected).sum()==len(expected):
                        ret=(frame.loc[endpoint,'close']/frame.loc[stamp,'close']-1)*100;value['return_pct']=float(ret)
                        value['mae_pct']=float((frame.loc[(frame.index>stamp)&(frame.index<=endpoint),'low'].min()/frame.loc[stamp,'close']-1)*100)
                        if stamp in btc.index and endpoint in btc.index:value['btc_excess_pct_points']=float(ret-(btc.loc[endpoint,'close']/btc.loc[stamp,'close']-1)*100)
                        cr=[]
                        for control in choices:
                            other=frames[control]
                            if stamp in other.index and endpoint in other.index:cr.append((other.loc[endpoint,'close']/other.loc[stamp,'close']-1)*100)
                        if len(choices)==3 and len(cr)==3:value['control_excess_pct_points']=float(ret-np.median(cr))
                    event['outcomes'][str(hours)]=value
                events.append(event)
    def stats(rows,hours):
        measured=[r['outcomes'][str(hours)] for r in rows if r['outcomes'][str(hours)]['return_pct'] is not None]
        def median(field):
            values=[r[field] for r in measured if r[field] is not None]
            return float(np.median(values)) if values else None
        return {'measured':len(measured),'missing':len(rows)-len(measured),
                'negative_fraction':float(np.mean([r['return_pct']<=0 for r in measured])) if measured else None,
                **{'median_'+k:median(k) for k in ('return_pct','btc_excess_pct_points','control_excess_pct_points','mae_pct')}}
    summary={'status':'retrospective_sanity_check_only','symbols_analyzed':len(frames),'audit_errors':sum('error' in a for a in audits),
        'known_design_symbols_excluded':sorted(known),'limitations':['Current listing and archive selection bias.',
        'No historical live ticker prefilter reconstructed. Closed-price references, no execution/fees.',
        '48h cooldown per symbol/model; different symbols/times/groups still share market exposure.',
        'All archived periods have been available during earlier research; no independent out-of-sample claim.',
        'Groups overlap: do not sum their sample sizes as independent coins.'],'models':{}}
    for name in models:
        rows=[r for r in events if r['model']==name and not r['known_design_example']]
        summary['models'][name]={'events':len(rows),'horizons':{str(h):stats(rows,h) for h in (12,24,48)}}
    save('audit.json',audits);save('events.json',events);save('summary.json',summary)
    losers=sorted([r for r in events if not r['known_design_example'] and r['outcomes']['12']['return_pct'] is not None],
                  key=lambda r:r['outcomes']['12']['return_pct'])[:20]
    save('failure_examples.json',losers)
    print(json.dumps(clean(summary),ensure_ascii=True),flush=True)


if __name__=='__main__':run()
