"""Causal RSI(14) regular bullish divergence, context only (no gate or score).

Two left/two right closed candles confirm a price pivot. A signal is emitted
at confirmation time, never backdated to the pivot candle.
"""
import numpy as np
import pandas as pd
from study_dataset import STEP


def rsi_wilder(close,length=14):
    values = close.to_numpy(dtype=float)
    result = np.full(len(values),np.nan)
    if len(values)<=length: return pd.Series(result,index=close.index)
    changes = np.diff(values)
    gains, losses = np.maximum(changes,0), np.maximum(-changes,0)
    up, down = gains[:length].mean(), losses[:length].mean()
    for i in range(length,len(values)):
        if i>length:
            up = ((length-1)*up+gains[i-1])/length
            down = ((length-1)*down+losses[i-1])/length
        result[i] = 50. if up==down==0 else (100. if down==0 else 100-100/(1+up/down))
    return pd.Series(result,index=close.index)


def divergence(frame,rsi):
    count = len(frame)
    event = np.zeros(count,dtype=bool)
    active = np.zeros(count,dtype=bool)
    confirmation = np.full(count,np.nan)
    age = np.full(count,np.nan)
    previous_pivot = None
    last_signal = None
    lows = frame.low.to_numpy()
    for i in range(count):
        pivot = i-2
        if pivot>=2 and np.isfinite(rsi.iloc[pivot]):
            is_pivot = lows[pivot]<np.min(lows[pivot-2:pivot]) and lows[pivot]<=np.min(lows[pivot+1:i+1])
            if is_pivot:
                if previous_pivot is not None and 3<=pivot-previous_pivot<=30:
                    if lows[pivot]<lows[previous_pivot] and rsi.iloc[pivot]>rsi.iloc[previous_pivot]:
                        event[i]=True
                        last_signal=(i,pivot)
                previous_pivot=pivot
        if last_signal is not None:
            detected,pivot = last_signal
            if lows[i]<lows[pivot]: last_signal=None
            elif i-detected<6:
                active[i]=True
                confirmation[i]=frame.index[detected]+STEP
                age[i]=i-detected
    return pd.DataFrame({'rsi14':rsi,'pu_confirmed_now':event,'pu_active':active,
                         'pu_confirmation_ms':confirmation,'pu_age_bars':age},index=frame.index)


def features(frame):
    return divergence(frame,rsi_wilder(frame.close))
