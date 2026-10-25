"""Build causal features and explicitly separated forward labels for MEXC study."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from parabolic_sar import parabolic_sar

ROOT = Path(__file__).resolve().parent
STEP = 14400000
FEATURES = ['body_atr','low_lift_atr','sar_distance_atr','sar_recent_up',
            'log_volume_change','relative_log_return24','log_quote_volume24']


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def load_history(path):
    raw = read_json(path)
    if not raw['rows']:
        return pd.DataFrame(), {'rows': 0, 'gaps': 0, 'reason': 'no_history'}
    frame = pd.DataFrame(raw['rows'], columns=[
        'open_ms','open','high','low','close','volume','close_ms','quote_volume'
    ]).apply(pd.to_numeric, errors='raise').sort_values('open_ms').set_index('open_ms')
    if frame.index.duplicated().any():
        raise ValueError('duplicate candle timestamps')
    if (frame.index.to_numpy()%STEP != 0).any():
        raise ValueError('candles not on UTC 4h grid')
    valid = ((frame[['open','high','low','close']] > 0).all(axis=1) &
             (frame['high'] >= frame[['open','close','low']].max(axis=1)) &
             (frame['low'] <= frame[['open','close']].min(axis=1)) &
             (frame[['volume','quote_volume']] >= 0).all(axis=1))
    if not valid.all():
        raise ValueError(f'invalid OHLCV on {int((~valid).sum())} bars')
    frame = frame[(frame.index+STEP) <= raw['fetched_server_time_ms']].copy()
    gaps = int((np.diff(frame.index.to_numpy()) != STEP).sum())
    return frame, {'rows':len(frame), 'gaps':gaps, 'reason':None}


def atr_wilder(frame, length=14):
    previous = frame['close'].shift(1)
    tr = pd.concat([frame['high']-frame['low'], (frame['high']-previous).abs(),
                    (frame['low']-previous).abs()], axis=1).max(axis=1).to_numpy()
    result = np.full(len(frame), np.nan)
    if len(frame) >= length:
        result[length-1] = np.mean(tr[:length])
        for i in range(length, len(frame)):
            result[i] = ((length-1)*result[i-1]+tr[i])/length
    return pd.Series(result, index=frame.index)


def segment_features(segment, btc_log_return24, config):
    out = segment.copy()
    atr = atr_wilder(out).replace(0,np.nan)
    sar = parabolic_sar(out)
    out['body_atr'] = (out['close']-out['open'])/atr
    out['low_lift_atr'] = (out['low']-out['low'].shift(1).rolling(6).min())/atr
    out['sar_distance_atr'] = (out['close']-sar['sar'])/atr
    out['sar_recent_up'] = sar['sar_flip_up'].rolling(3).max().fillna(0).astype(float)
    volume_ratio = (out['quote_volume'].rolling(6).mean()/
                    out['quote_volume'].shift(6).rolling(30).mean().replace(0,np.nan))
    out['log_volume_change'] = np.log(volume_ratio.replace(0,np.nan))
    out['relative_log_return24'] = np.log(out['close']/out['close'].shift(6))-btc_log_return24.reindex(out.index)
    out['quote_volume24'] = out['quote_volume'].rolling(6).sum()
    out['log_quote_volume24'] = np.log(out['quote_volume24'].replace(0,np.nan))
    out['atr_pct'] = atr/out['close']*100
    out['nonzero24'] = (out['quote_volume']>0).rolling(6).sum()
    out['body_pct'] = (out['close']/out['open']-1)*100
    strong = out['body_pct'] >= config['event']['primary_closed_bar_body_gain_pct']
    lookback = config['event']['no_equal_or_larger_body_in_previous_bars']
    prior_strong = strong.shift(1).rolling(lookback, min_periods=lookback).sum()
    out['primary_event'] = strong & (prior_strong==0)
    out['past_strong48'] = strong.rolling(lookback).max().fillna(0).astype(bool)
    warmup = np.arange(len(out)) >= config['model']['minimum_contiguous_history_bars']-1
    out['feature_ready'] = warmup & np.isfinite(out[FEATURES]).all(axis=1)
    out['eligible'] = (out['feature_ready'] & ~out['past_strong48'] &
                       (out['quote_volume24'] >= config['model']['liquidity_floor_usdt24']) &
                       (out['nonzero24'] >= config['model']['minimum_nonzero_volume_bars24']))
    out['sar_below'] = sar['sar_below']
    out['sar_value'] = sar['sar']
    out['decision_ms'] = out.index+STEP
    return out


def add_labels(features, config):
    out = features.copy()
    # A row's close is at open_ms+4h. Target at row i+2 therefore opens 4h later.
    minimum = config['event']['alert_minimum_lead_hours']//4 + 1
    maximum = config['event']['alert_maximum_lead_hours']//4 + 1
    next_events = pd.concat([out['primary_event'].shift(-j) for j in range(minimum,maximum+1)], axis=1)
    any_next = pd.concat([out['primary_event'].shift(-j) for j in range(1,maximum+1)], axis=1)
    highs = pd.concat([out['high'].shift(-j) for j in range(1,13)], axis=1)
    lows = pd.concat([out['low'].shift(-j) for j in range(1,13)], axis=1)
    closes = pd.concat([out['close'].shift(-j) for j in range(1,13)], axis=1)
    complete = highs.notna().all(axis=1) & lows.notna().all(axis=1) & closes.notna().all(axis=1)
    out['label'] = next_events.eq(True).any(axis=1).astype(float).where(complete)
    out['any_event_next24'] = any_next.eq(True).any(axis=1).where(complete)
    out['next_event_ms'] = np.nan
    for j in range(maximum,minimum-1,-1):
        mask = out['primary_event'].shift(-j).eq(True) & complete
        out.loc[mask,'next_event_ms'] = out.index[mask]+j*STEP
    out['mfe24_pct'] = ((highs.iloc[:,:6].max(axis=1)/out['close']-1)*100).where(complete)
    out['mfe48_pct'] = ((highs.max(axis=1)/out['close']-1)*100).where(complete)
    out['mae48_pct'] = ((lows.min(axis=1)/out['close']-1)*100).where(complete)
    out['max_close48_multiple'] = (closes.max(axis=1)/out['close']).where(complete)
    out['return48_close_pct'] = ((out['close'].shift(-12)/out['close']-1)*100).where(complete)
    return out


def build(config=None):
    config = config or read_json(ROOT/'study_config.json')
    selection = read_json(ROOT/'data'/'study'/'selection.json')
    directory = ROOT/'data'/'study'/'history'
    btc, _ = load_history(directory/'BTCUSDT.json')
    if btc.empty or (np.diff(btc.index.to_numpy()) != STEP).any():
        raise ValueError('BTC history must be nonempty and contiguous')
    btc_return = np.log(btc['close']/btc['close'].shift(6))
    frames, event_rows, audits = [], [], []
    for symbol in selection['symbols']:
        path = directory/f'{symbol}.json'
        if not path.exists():
            audits.append({'symbol':symbol, 'rows':0, 'gaps':0, 'reason':'missing_download'})
            continue
        try:
            frame, audit = load_history(path)
            audit['symbol'] = symbol
            audit['eligible_rows'] = 0
            audits.append(audit)
            if frame.empty:
                continue
            segments = pd.Series(np.r_[True,np.diff(frame.index.to_numpy()) != STEP], index=frame.index).cumsum()
            for _, segment in frame.groupby(segments):
                if len(segment) < config['model']['minimum_contiguous_history_bars']:
                    continue
                f = add_labels(segment_features(segment,btc_return,config),config)
                f['symbol'] = symbol
                audit['eligible_rows'] += int(f['eligible'].sum())
                frames.append(f)
                for ms, row in f[f['primary_event'] & f['feature_ready']].iterrows():
                    event_rows.append({'symbol':symbol, 'event_open_ms':int(ms),
                                       'body_pct':float(row['body_pct']), 'open':float(row['open']),
                                       'close':float(row['close'])})
        except (ValueError, KeyError, TypeError) as exc:
            audits.append({'symbol':symbol, 'reason':str(exc), 'rows':0, 'gaps':None})
    if not frames:
        raise ValueError('No usable study history')
    data = pd.concat(frames).reset_index().sort_values(['decision_ms','symbol']).reset_index(drop=True)
    events = pd.DataFrame(event_rows).sort_values(['event_open_ms','symbol']).reset_index(drop=True)
    return data, events, audits, selection


def self_check():
    from parabolic_sar import self_check as sar_check
    sar_check()
    config = read_json(ROOT/'study_config.json')
    count = 240
    times = np.arange(count)*STEP
    price = 10+np.sin(np.arange(count)/8)
    frame = pd.DataFrame({'open':price,'high':price+.2,'low':price-.2,'close':price+.02,
                          'volume':10000.,'quote_volume':100000.},index=times)
    btc = pd.Series(0.,index=times)
    first = segment_features(frame,btc,config)
    changed = frame.copy()
    changed.iloc[200:,:4] *= 3
    second = segment_features(changed,btc,config)
    pd.testing.assert_frame_equal(first.iloc[:200],second.iloc[:200])
    # A forced event on bar 210 cannot label bar 209 positive (zero warning).
    first['primary_event'] = False
    first.loc[times[210],'primary_event'] = True
    labelled = add_labels(first,config)
    assert labelled.loc[times[208],'label'] == 1 # closes at 209, event opens 210: 4h
    assert labelled.loc[times[209],'label'] == 0 # closes at 210: no advance warning
    assert labelled.loc[times[203],'label'] == 1 # 24h warning
    assert labelled.loc[times[202],'label'] == 0 # 28h warning, outside horizon
    assert labelled.iloc[-1]['label'] != labelled.iloc[-1]['label'] # incomplete future is NA
    assert (labelled.loc[labelled['label']==1,'next_event_ms']-labelled.loc[labelled['label']==1,'decision_ms']).min() == STEP


if __name__ == '__main__':
    self_check()
    print('Dataset checks passed: causal features, label lead, future censoring, SAR fixture.')
