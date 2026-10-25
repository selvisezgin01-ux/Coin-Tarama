"""Retrospective sanity check on one common archived MEXC cohort, not a backtest of execution."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

import momentum_scan as v3
import strength_v4 as v4
from study_dataset import STEP, load_history, read_json

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results'/'strength_v4_comparison'


def clean(value):
    if isinstance(value, dict): return {k:clean(v) for k,v in value.items()}
    if isinstance(value, list): return [clean(v) for v in value]
    if isinstance(value, (np.integer, np.bool_)): return value.item()
    if isinstance(value, (float, np.floating)): return float(value) if np.isfinite(value) else None
    return value


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(clean(value), ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')


def last_segment(frame):
    gaps = np.flatnonzero(np.diff(frame.index.to_numpy()) != STEP)
    return frame.iloc[int(gaps[-1])+1:] if len(gaps) else frame


def summarize(events, horizon):
    valid = [e for e in events if e['outcomes'][str(horizon)]['return_pct'] is not None]
    def median(key):
        values = [e['outcomes'][str(horizon)][key] for e in valid if e['outcomes'][str(horizon)][key] is not None]
        return float(np.median(values)) if values else None
    return {'measured':len(valid), 'pending_or_missing':len(events)-len(valid),
            'median_return_pct':median('return_pct'), 'median_btc_excess_pct_points':median('btc_excess_pct_points'),
            'median_control_excess_pct_points':median('control_excess_pct_points'),
            'negative_close_fraction':float(np.mean([e['outcomes'][str(horizon)]['return_pct'] <= 0 for e in valid])) if valid else None,
            'median_mae_pct':median('mae_pct')}


def run():
    cfg = read_json(ROOT/'strength_v4_config.json')
    old = read_json(ROOT/'momentum_config.json')
    # Persist rules before computing aggregate outcomes. The archived data are already known;
    # this is a design freeze, never a claim of a prospective preregistered trial.
    freeze = {'config':cfg, 'sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
               for name in ['strength_v4_config.json','strength_v4.py','compare_strength_v4.py']}}
    frozen = OUT/'design_frozen.json'
    if frozen.exists() and read_json(frozen) != freeze:
        raise RuntimeError('Comparison design changed; use a new comparison directory.')
    save(frozen, freeze)
    directory = ROOT/'data'/'study'/'history'
    btc, _ = load_history(directory/'BTCUSDT.json')
    btc = last_segment(btc)
    btc_return = (btc.close/btc.close.shift(6)-1)*100
    btc_return.attrs['return8'] = (btc.close/btc.close.shift(2)-1)*100
    frames, models, audit = {}, {'v3':{},'v4':{}}, []
    for path in sorted(directory.glob('*.json')):
        symbol = path.stem
        if symbol == 'BTCUSDT': continue
        try:
            frame, info = load_history(path)
            frame = last_segment(frame)
            if len(frame) < cfg['minimum_history_bars']:
                raise ValueError('insufficient contiguous history')
            frames[symbol] = frame
            models['v3'][symbol] = v3.features(frame, btc_return, old)
            models['v4'][symbol] = v4.features(frame, btc_return, cfg)
            audit.append({'symbol':symbol, 'rows':len(frame), 'original_gaps':info['gaps']})
        except (ValueError, KeyError, FileNotFoundError) as exc:
            audit.append({'symbol':symbol, 'error':str(exc)})
    known = set(cfg['comparison']['known_design_symbols'])
    # Controls share decision time and archive membership; only causal liquidity/ATR is used.
    pool_parts = []
    for symbol, rows in models['v4'].items():
        eligible = rows[rows.gate_history & rows.gate_liquidity & (rows.atr > 0)]
        part = eligible[['close','atr','quote_volume24']].copy()
        part['symbol'] = symbol
        pool_parts.append(part)
    pool = pd.concat(pool_parts).reset_index(names='open_ms')
    by_time = {stamp:group for stamp,group in pool.groupby('open_ms')}
    events = []
    for model, series in models.items():
        for symbol, rows in series.items():
            previous = -10**20
            for stamp, row in rows[rows.qualified].iterrows():
                if stamp - previous < cfg['comparison']['cooldown_hours_per_symbol']*3600000: continue
                previous = stamp
                frame = frames[symbol]
                controls = by_time.get(stamp, pool.iloc[:0])
                controls = controls[(controls.symbol != symbol) & ~controls.symbol.isin(known)].copy()
                if len(controls):
                    controls['distance'] = (np.abs(np.log(controls.quote_volume24/row.quote_volume24)) +
                                            np.abs(np.log((controls.atr/controls.close)/(row.atr/row.close))))
                    controls = controls.sort_values(['distance','symbol']).head(cfg['comparison']['controls_per_event'])
                control_symbols = list(controls.symbol)
                event = {'model':model, 'symbol':symbol, 'decision_ms':int(stamp+STEP),
                         'reference_closed_price':float(row.close), 'known_design_example':symbol in known,
                         'stage':row.get('stage','new_breakout'), 'controls':control_symbols, 'outcomes':{}}
                for hours in cfg['comparison']['return_horizons_hours']:
                    endpoint = stamp + hours//4*STEP
                    value = {'return_pct':None,'btc_excess_pct_points':None,'control_excess_pct_points':None,'mae_pct':None}
                    expected = np.arange(stamp, endpoint+1, STEP)
                    if endpoint in frame.index and frame.index.isin(expected).sum() == len(expected):
                        ret = (frame.loc[endpoint,'close']/row.close-1)*100
                        value['return_pct'] = float(ret)
                        value['mae_pct'] = float((frame.loc[(frame.index>stamp)&(frame.index<=endpoint),'low'].min()/row.close-1)*100)
                        if stamp in btc.index and endpoint in btc.index:
                            value['btc_excess_pct_points'] = float(ret-(btc.loc[endpoint,'close']/btc.loc[stamp,'close']-1)*100)
                        control_returns = []
                        for control in control_symbols:
                            other = frames[control]
                            if stamp in other.index and endpoint in other.index:
                                control_returns.append((other.loc[endpoint,'close']/other.loc[stamp,'close']-1)*100)
                        if len(control_returns) == len(control_symbols) and control_returns:
                            value['control_excess_pct_points'] = float(ret-np.median(control_returns))
                    event['outcomes'][str(hours)] = value
                events.append(event)
    summary = {'status':'retrospective_sanity_check_not_prospective_validation',
               'cohort':'archived data/study/history; no ticker prefilter applied retrospectively',
               'limitations':['Archive and current-listing selection bias; no market-wide success rate.',
                              'Known examples excluded from headline aggregates; remaining data are still retrospective.',
                              'Closed-price references, no bid/ask, fees or executable profit.',
                              '48h cooldown per symbol within each model; events can still share market exposure.',
                              'Matched controls are descriptive and can be reused; no independent significance claim.'],
               'symbols_analyzed':len(frames), 'excluded_design_symbols':sorted(known), 'models':{}}
    for model in models:
        subset = [e for e in events if e['model']==model and not e['known_design_example']]
        summary['models'][model] = {'events':len(subset),'unique_symbols':len({e['symbol'] for e in subset}),
              'stages':{stage:sum(e['stage']==stage for e in subset) for stage in ['new_breakout','continuation']},
              'horizons':{str(h):summarize(subset,h) for h in cfg['comparison']['return_horizons_hours']}}
    save(OUT/'events.json',events);save(OUT/'audit.json',audit);save(OUT/'summary.json',summary)
    lines = ['# V3 / deneysel V4 — arşiv karşılaştırması','',
             'Bu geriye dönük bir sağlamlık kontrolüdür; ileriye dönük doğrulama veya gerçekleşebilir net kâr testi değildir.',
             f"Ortak veri kümesi: {len(frames)} MEXC sembolü. Bilinen tasarım örnekleri aşağıdaki toplamlardan çıkarıldı.",'',
             '| Sürüm | Bildirim olayı | Farklı coin | 48s ölçülen | Medyan 48s % | BTC üstü medyan puan | Kontrol üstü medyan puan | 48s ≤0 oranı |',
             '|---|---:|---:|---:|---:|---:|---:|---:|']
    def number(value): return '—' if value is None else f'{value:.2f}'
    for model,item in summary['models'].items():
        h = item['horizons']['48']
        lines.append(f"| {model} | {item['events']} | {item['unique_symbols']} | {h['measured']} | {number(h['median_return_pct'])} | {number(h['median_btc_excess_pct_points'])} | {number(h['median_control_excess_pct_points'])} | {number(None if h['negative_close_fraction'] is None else h['negative_close_fraction']*100)}% |")
    lines += ['', '## Sınırlar',''] + ['- '+item for item in summary['limitations']]
    lines += ['', '12/24/48 saatlik ayrıntılar summary.json, olaylar events.json dosyasındadır. Örneklerdeki artışlar eşik seçmek için tekrar optimize edilmez.', '']
    (OUT/'report.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps(clean(summary),ensure_ascii=False))


if __name__ == '__main__': run()
