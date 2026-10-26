"""Causal 5m discovery / 15m confirmation from the same observed pool history."""
from copy import deepcopy
import meme_rules as rules

EARLY = 5 * 60000
CONFIRM = 15 * 60000
LABELS = {'early_5m': '5 dk erken aday', 'confirmed_15m': '15 dk teknik teyit'}


def aggregate_15m(rows, asof_ms):
    bars = rules.available_candles(rows, asof_ms, step_ms=EARLY)
    grouped = {}
    for bar in bars:
        grouped.setdefault(bar['open_ms'] // CONFIRM * CONFIRM, []).append(bar)
    result = []
    for opening, group in sorted(grouped.items()):
        # A launch fragment, gap or open sub-candle never creates a complete 15m bar.
        if [b['open_ms'] for b in group] != [opening + i * EARLY for i in range(3)]:
            continue
        result.append([opening // 1000, group[0]['open'], max(b['high'] for b in group),
                       min(b['low'] for b in group), group[-1]['close'], sum(b['volume'] for b in group)])
    return result


def evaluate(rows, asset, earliest, stamp, config):
    formation = rules.first_formation(rows, asset, earliest, stamp, config, step_ms=EARLY)
    stages = {}
    created = asset.get('pool_created_ms')
    for phase, step, raw in [('early_5m', EARLY, rows), ('confirmed_15m', CONFIRM, aggregate_15m(rows, stamp))]:
        bars = rules.closed_candles(raw, stamp, step_ms=step)
        # Only full intervals after pool creation contribute to a positive setup.
        bars = [b for b in bars if created is not None and b['open_ms'] >= created]
        setup = rules.pattern(bars, config)
        if not bars or stamp // step * step - (bars[-1]['open_ms'] + step) > config['timeframes']['max_closed_lag_minutes'] * 60000:
            setup = {'stage': None, 'reason': 'closed_candles_missing_or_stale', 'metrics': {}}
        stages[phase] = {'setup': setup, 'closed_count': len(bars),
                         'cutoff_ms': bars[-1]['open_ms'] + step if bars else None,
                         'last_close': bars[-1]['close'] if bars else None}
    # First encounter in a 5m breakout cannot be disguised by a still-quiet 15m bar.
    phase = 'confirmed_15m' if stages['confirmed_15m']['setup']['stage'] else 'early_5m'
    if stages['early_5m']['setup']['stage'] == 'first_breakout':
        phase = 'early_5m'
    chosen = stages[phase]
    return {'formation': formation, 'phases': stages, 'phase': phase, **deepcopy(chosen)}


def seed(previous, branch, commit, fingerprint, stamp):
    if branch != 'scanner-state-meme-v3' or previous.get('version') != 'meme-v3':
        raise ValueError('Hybrid migration only accepts the archived meme-v3 experiment')
    if previous.get('rules_fingerprint') != 'b3c031ccb7d7142c8f54981df790673fdb670ef391a4e5e3716c268f6f249d1f':
        raise ValueError('Unexpected source Meme fingerprint')
    state = deepcopy(previous)
    state.update(version='meme-v4-hybrid', rules_fingerprint=fingerprint, runs=[])
    state['legacy_pending_v3'] = state.pop('pending', [])
    state['pending'] = []  # Never replay stale candidates at their earlier prices.
    for entry in state.get('entries', {}).values():
        entry['origin_experiment'] = 'meme-v3'
    for record in state.get('assets', {}).values():
        record.pop('setup', None)
        record.pop('timeframe_assessment', None)
        record['tier'] = 'watch'
    state['migration'] = {'from_branch': branch, 'from_commit': commit,
                          'from_fingerprint': previous['rules_fingerprint'], 'migrated_ms': stamp,
                          'reason': 'User approved 5m early discovery + independent 15m confirmation and optional large-buyer support. Prior prices/outcomes/latches preserved; no backfilled early signals.'}
    return state
