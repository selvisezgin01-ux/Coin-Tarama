"""Causal Wilder Parabolic SAR with close-based initial direction.

Defaults and initialization follow TradingView's documented convention.
No assertion of bit-for-bit parity with a live TradingView feed is made.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def parabolic_sar(frame, start=.02, increment=.02, maximum=.20):
    if not (0 < start <= maximum and 0 < increment <= maximum):
        raise ValueError('Invalid SAR acceleration settings')
    high = frame['high'].to_numpy(dtype=float)
    low = frame['low'].to_numpy(dtype=float)
    close = frame['close'].to_numpy(dtype=float)
    if not (np.isfinite(high).all() and np.isfinite(low).all() and np.isfinite(close).all()):
        raise ValueError('SAR requires finite OHLC data')
    n = len(frame)
    values = np.full(n, np.nan)
    below = np.zeros(n, dtype=bool)
    flip_up, flip_down = np.zeros(n, dtype=bool), np.zeros(n, dtype=bool)
    bull_run = np.zeros(n, dtype=int)
    extreme = sar = acceleration = np.nan
    bullish = False
    for i in range(1, n):
        new_trend = False
        if i == 1:
            bullish = close[i] > close[i-1]
            extreme = high[i] if bullish else low[i]
            sar = low[i-1] if bullish else high[i-1]
            acceleration = start
            new_trend = True
        sar += acceleration * (extreme-sar)
        if bullish and sar > low[i]:
            bullish = False
            sar = max(high[i], extreme)
            extreme = low[i]
            acceleration = start
            new_trend = True
            flip_down[i] = True
        elif not bullish and sar < high[i]:
            bullish = True
            sar = min(low[i], extreme)
            extreme = high[i]
            acceleration = start
            new_trend = True
            flip_up[i] = True
        if not new_trend:
            if bullish and high[i] > extreme:
                extreme = high[i]
                acceleration = min(acceleration+increment, maximum)
            elif not bullish and low[i] < extreme:
                extreme = low[i]
                acceleration = min(acceleration+increment, maximum)
        if bullish:
            sar = min(sar, low[i-1])
            if i > 1:
                sar = min(sar, low[i-2])
        else:
            sar = max(sar, high[i-1])
            if i > 1:
                sar = max(sar, high[i-2])
        values[i] = sar
        below[i] = bullish
        bull_run[i] = bull_run[i-1]+1 if bullish else 0
    return pd.DataFrame({
        'sar': values, 'sar_below': below, 'sar_flip_up': flip_up,
        'sar_flip_down': flip_down, 'sar_bull_run_bars': bull_run,
        'sar_signed_distance_pct': (close-values)/close*100,
    }, index=frame.index)


def self_check():
    fixture = pd.DataFrame({
        'high': [11,12,13,14,13,12,15],
        'low': [9,10,11,12,8,7,9],
        'close': [10,11,12,13,9,8,14],
    })
    expected = [np.nan,9,9,9.16,14,14,7]
    got = parabolic_sar(fixture)
    np.testing.assert_allclose(got['sar'], expected, equal_nan=True)
    assert list(got['sar_flip_up']) == [False,False,False,False,False,False,True]
    assert list(got['sar_flip_down']) == [False,False,False,False,True,False,False]
    changed = fixture.copy()
    changed.iloc[5:] *= 10
    pd.testing.assert_frame_equal(got.iloc[:5], parabolic_sar(changed).iloc[:5])
    scaled = parabolic_sar(fixture*7)
    np.testing.assert_allclose(scaled['sar'], got['sar']*7, equal_nan=True)
    np.testing.assert_allclose(scaled['sar_signed_distance_pct'], got['sar_signed_distance_pct'], equal_nan=True)


if __name__ == '__main__':
    self_check()
    print('SAR fixture, future independence, and scale invariance checks passed.')
