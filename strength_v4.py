"""Experimental closed-bar start/continuation rules; does not alter frozen v3."""
from __future__ import annotations

import numpy as np
import pandas as pd

from parabolic_sar import parabolic_sar
from study_dataset import STEP, atr_wilder


def features(frame, btc_return, config):
    out = frame.copy()
    r = config['rules']
    atr = atr_wilder(out).replace(0, np.nan)
    out['atr'] = atr
    out['ema20'] = out.close.ewm(span=20, adjust=False, min_periods=20).mean()
    out['ema50'] = out.close.ewm(span=50, adjust=False, min_periods=50).mean()
    out['return24_pct'] = (out.close / out.close.shift(6) - 1) * 100
    out['return72_pct'] = (out.close / out.close.shift(18) - 1) * 100
    out['relative24_pct_points'] = out.return24_pct - btc_return.reindex(out.index)
    out['ema20_extension_atr'] = (out.close - out.ema20) / atr
    out['close_position'] = (out.close - out.low) / (out.high - out.low).replace(0, np.nan)
    out['quote_volume24'] = out.quote_volume.rolling(6).sum()
    out['nonzero24'] = (out.quote_volume > 0).rolling(6).sum()
    out['higher_lows'] = out.low.rolling(3).median() > out.low.shift(3).rolling(3).median()
    resistance = out.high.shift(1).rolling(r['resistance_lookback_bars']).max()
    ratio = out.quote_volume / out.quote_volume.shift(1).rolling(20).median().replace(0, np.nan)
    breakout = ((out.close > resistance) & (out.close.shift(1) <= resistance.shift(1)) &
                (ratio >= r['breakout_volume_median_ratio_min']))
    out['breakout_now'] = breakout
    limit = r['continuation_max_age_bars']
    positions = pd.Series(np.arange(len(out)), index=out.index, dtype=float)
    out['breakout_age_bars'] = positions - positions.where(breakout).ffill(limit=limit)
    for name, values in [('breakout_level', resistance), ('breakout_volume_ratio', ratio),
                         ('breakout_low', out.low), ('anchor_atr', atr),
                         ('breakout_open_ms', pd.Series(out.index, index=out.index, dtype=float))]:
        out[name] = values.where(breakout).ffill(limit=limit)
    hold_low, peak = np.full(len(out), np.nan), np.full(len(out), np.nan)
    last = -limit - 1
    lows, highs, closes = out.low.to_numpy(), out.high.to_numpy(), out.close.to_numpy()
    for i, is_breakout in enumerate(breakout.to_numpy()):
        if is_breakout:
            last = i
        if i - last <= limit:
            # The wide breakout bar's own low is not a post-breakout retest.
            hold_low[i] = np.min(lows[last+1:i+1]) if i > last else closes[i]
            peak[i] = np.max(highs[last:i+1])
    out['hold_low'] = hold_low
    out['peak_since_breakout'] = peak
    out['peak_drawdown_pct'] = (1 - out.close / out.peak_since_breakout) * 100
    out['peak_drawdown_atr'] = (out.peak_since_breakout - out.close) / atr
    out['invalidation_level'] = (np.minimum(out.breakout_low, out.low.rolling(3).min()) -
                                 r['invalidation_buffer_anchor_atr'] * out.anchor_atr)
    out['invalidation_distance_pct'] = (1 - out.invalidation_level / out.close) * 100
    fresh = out.breakout_age_bars.between(0, r['fresh_max_age_bars'])
    continuation = out.breakout_age_bars.between(r['fresh_max_age_bars']+1, limit)
    gates = {
        'history': pd.Series(np.arange(len(out)) >= config['minimum_history_bars']-1, index=out.index),
        'anchor': out.breakout_level.notna(),
        'trend': ((out.close > out.ema20) & (out.close > out.ema50) &
                  (out.ema20 > out.ema20.shift(3))),
        'holds_breakout': ((out.close >= out.breakout_level) &
                          (out.hold_low >= out.breakout_level - r['hold_tolerance_anchor_atr'] * out.anchor_atr)),
        'relative_strength': out.relative24_pct_points > 0,
        'liquidity': ((out.quote_volume24 >= r['quote_volume24_min_usdt']) & (out.nonzero24 == 6)),
    }
    for name, value in gates.items():
        out['gate_'+name] = value.fillna(False)
    common = out[['gate_'+name for name in gates]].all(axis=1)
    out['new_breakout'] = (common & fresh &
                          (out.return24_pct >= r['fresh_return24_min_pct']) &
                          (out.close_position >= r['fresh_close_position_min']) &
                          (out.peak_drawdown_pct <= r['fresh_peak_drawdown_max_pct']) &
                          (out.peak_drawdown_atr <= r['fresh_peak_drawdown_max_atr']))
    out['continuation'] = (common & continuation & out.higher_lows &
                          (out.return24_pct >= r['continuation_return24_min_pct']) & (out.return72_pct > 0) &
                          (out.close_position >= r['continuation_close_position_min']) &
                          (out.peak_drawdown_pct <= r['continuation_peak_drawdown_max_pct']) &
                          (out.peak_drawdown_atr <= r['continuation_peak_drawdown_max_atr']))
    out['qualified'] = out.new_breakout | out.continuation
    out['stage'] = np.select([out.new_breakout, out.continuation], ['new_breakout', 'continuation'], default='')
    out['sar_below'] = parabolic_sar(out)['sar_below']
    out['strength_score'] = ((out.ema20 > out.ema50).astype(int)*25 + out.higher_lows.astype(int)*25 +
                              out.sar_below.astype(int)*10 +
                              (((out.close / out.close.shift(2)-1)*100) >
                               btc_return.attrs['return8'].reindex(out.index)).astype(int)*20 +
                              (out.breakout_volume_ratio >= 2).astype(int)*20)
    out['decision_ms'] = out.index + STEP
    return out


def warnings(row, config):
    w = config['warnings']
    result = []
    for field, threshold, label in [
        ('return24_pct', w['return24_above_pct'], '24 saatlik yükseliş yüksek'),
        ('return72_pct', w['return72_above_pct'], '72 saatlik yükseliş yüksek'),
        ('ema20_extension_atr', w['ema20_extension_above_atr'], 'ortalamadan uzak'),
        ('invalidation_distance_pct', w['invalidation_distance_above_pct'], 'yapı bozulma mesafesi geniş'),
    ]:
        if row.get(field) is not None and row[field] > threshold:
            result.append(label)
    if row.get('quote_volume24', 0) < config['rules']['main_liquidity_band_usdt24']:
        result.append('düşük hacim')
    if row.get('breakout_age_bars') == 0:
        result.append('ilk kapanış; sonraki mumda tutunma henüz gözlenmedi')
    return result
