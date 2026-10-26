"""Causal additional paths for Coin Tarama 3; original V3/V4 algorithms stay intact."""
from __future__ import annotations
import numpy as np
import pandas as pd
import strength_v4 as previous

LABELS={'early_reversal':'Erken dönüş','sideways_volume':'Yatay fiyat / hacim artışı',
        'retest':'Geri testte tutunma / SAR','new_breakout':'Yeni kırılım','continuation':'Tutunma'}
ORDER=('retest','early_reversal','sideways_volume','new_breakout','continuation')


def features(frame,btc_return,config):
    out=previous.features(frame,btc_return,config)
    atr=out.atr;prior_atr=atr.shift(1)
    out['volume_ratio_now']=out.quote_volume/out.quote_volume.shift(1).rolling(20).median().replace(0,np.nan)
    out['relative8_pct_points']=(out.close/out.close.shift(2)-1)*100-btc_return.attrs['return8'].reindex(out.index)
    # These are independent alternatives, not extra requirements on the original two paths.
    common=out.gate_history & out.gate_liquidity & ((out.relative24_pct_points>0)|(out.relative8_pct_points>0))
    e=config['groups']['early_reversal'];n=e['short_resistance_bars']
    out['early_level']=out.high.shift(1).rolling(n).max()
    out['early_ema']=out.close.ewm(span=e['short_ema_length'],adjust=False,min_periods=e['short_ema_length']).mean()
    out['early_prior_below_ema20']=out.close.shift(1)<out.ema20.shift(1)
    out['group_early_reversal']=(common & out.early_prior_below_ema20 & (out.close>out.early_level) &
        (out.close>out.early_ema) & (out.close>out.close.shift(1)) &
        (out.low>=out.low.shift(1)-e['low_tolerance_atr']*prior_atr) &
        (out.volume_ratio_now>=e['volume_ratio_min']) & (out.close_position>=e['close_position_min']))
    s=config['groups']['sideways_volume'];n=s['box_bars']
    out['box_high']=out.high.shift(1).rolling(n).max();out['box_low']=out.low.shift(1).rolling(n).min()
    out['box_range_atr']=(out.box_high-out.box_low)/prior_atr
    out['box_net_change_atr']=(out.close.shift(1)-out.open.shift(n)).abs()/prior_atr
    out['group_sideways_volume']=(common & (out.box_range_atr<=s['box_range_max_atr']) &
        (out.box_net_change_atr<=s['box_net_change_max_atr']) &
        ((out.close-out.close.shift(1)).abs()<=s['current_move_max_atr']*prior_atr) &
        (out.low>=out.box_low-s['box_tolerance_atr']*prior_atr) &
        (out.close>=out.box_low) & (out.close<=out.box_high+s['box_tolerance_atr']*prior_atr) &
        (out.low.shift(1)>=out.low.shift(n)-s['box_tolerance_atr']*prior_atr) &
        (out.volume_ratio_now>=s['volume_ratio_min']) & (out.close_position>=s['close_position_min']))
    r=config['groups']['retest'];flags=np.zeros(len(out),dtype=bool)
    touch=np.zeros(len(out),dtype=bool);base_range=np.full(len(out),np.nan)
    last=None
    for i in range(len(out)):
        if bool(out.breakout_now.iloc[i]):
            last=i if bool(out.new_breakout.iloc[i]) else None
            continue
        if last is None:continue
        age=i-last
        if not r['minimum_age_bars']<=age<=r['maximum_age_bars']:continue
        first=i-r['base_bars']+1
        if first<=last:continue
        level=out.breakout_level.iloc[i];anchor_atr=out.anchor_atr.iloc[i]
        if not np.isfinite([level,anchor_atr]).all() or anchor_atr<=0:continue
        base=out.iloc[first:i+1];past=out.iloc[last+1:first]
        # A genuine excursion BEFORE the base prevents flat bars at breakout from being called a retest.
        excursion=(past.high.max()-level)/anchor_atr if len(past) else np.nan
        touched=base.low.between(level-r['touch_tolerance_anchor_atr']*anchor_atr,
                                 level+r['touch_tolerance_anchor_atr']*anchor_atr).any()
        span=(base.high.max()-base.low.min())/anchor_atr
        touch[i]=bool(touched);base_range[i]=span
        flags[i]=bool(common.iloc[i] and touched and excursion>=r['minimum_excursion_anchor_atr'] and
            out.hold_low.iloc[i]>=level-r['touch_tolerance_anchor_atr']*anchor_atr and
            (base.close>=level).all() and span<=r['base_range_max_anchor_atr'] and
            out.close.iloc[i]<=level+r['close_extension_max_anchor_atr']*anchor_atr and
            base.quote_volume.mean()<=out.quote_volume.iloc[last]*r['base_breakout_volume_max_ratio'] and
            (not r['sar_below_required'] or out.sar_below.iloc[i]))
    out['retest_touched_support']=touch;out['retest_base_range_anchor_atr']=base_range
    out['group_retest']=flags
    out['group_new_breakout']=out.new_breakout;out['group_continuation']=out.continuation
    out['matched_groups']=[[name for name in ORDER if bool(out['group_'+name].iloc[i])] for i in range(len(out))]
    out['qualified']=out[['group_'+name for name in ORDER]].any(axis=1)
    out['stage']=[groups[0] if groups else '' for groups in out.matched_groups]
    # Group-specific structure references; never relabel a quiet box as an 80h breakout.
    out['signal_reference_level']=out.breakout_level
    early=out.stage.eq('early_reversal');box=out.stage.eq('sideways_volume')
    out.loc[early,'signal_reference_level']=out.loc[early,'early_level']
    out.loc[box,'signal_reference_level']=out.loc[box,'box_low']
    out['signal_invalidation_level']=out.invalidation_level
    out.loc[early,'signal_invalidation_level']=out.loc[early,'low']-config['rules']['invalidation_buffer_anchor_atr']*atr[early]
    out.loc[box,'signal_invalidation_level']=out.loc[box,'box_low']-config['rules']['invalidation_buffer_anchor_atr']*atr[box]
    out['signal_invalidation_distance_pct']=(1-out.signal_invalidation_level/out.close)*100
    out['signal_volume_ratio']=out.breakout_volume_ratio
    new=early|box;out.loc[new,'signal_volume_ratio']=out.loc[new,'volume_ratio_now']
    out['strength_score']=((out.ema20>out.ema50).astype(int)*25+out.higher_lows.astype(int)*25+
        out.sar_below.astype(int)*10+(out.relative8_pct_points>0).astype(int)*20+(out.signal_volume_ratio>=2).astype(int)*20)
    return out


def warnings(row,config):
    # Existing generic risk warnings remain; group-dependent references are explicit.
    adapted={**row,'invalidation_distance_pct':row.get('signal_invalidation_distance_pct')}
    if row.get('stage') not in ('new_breakout','continuation','retest'):adapted['breakout_age_bars']=None
    result=previous.warnings(adapted,config)
    if row.get('stage')=='early_reversal':result.append('erken dönüş; uzun trend teyidi henüz aranmadı')
    if row.get('stage')=='sideways_volume':result.append('yatay hacim; toplama veya yükseliş teyidi değildir')
    if row.get('stage')=='retest':result.append('geri testte SAR desteği; devam garantisi değildir')
    return result
