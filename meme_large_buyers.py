"""Optional evidence from sampled transaction initiators; never labels smart money."""
from meme_rules import address_key, number
from meme_sources import valid_address, ms_iso


def assess(payload, asset, security, stamp, config):
    rows = payload.get('data')
    if not isinstance(rows, list):
        raise ValueError('Unexpected pool trades schema')
    unique = {}
    invalid = 0
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get('attributes'), dict):
            invalid += 1
            continue
        identity = row.get('id'); data = row['attributes']
        if not isinstance(identity, str) or not identity:
            invalid += 1
            continue
        if identity in unique and unique[identity] != data:
            raise ValueError('Conflicting trade identity')
        unique[identity] = data
    excluded = set(security.get('excluded_known_accounts', []))
    excluded.update([asset['pool'], security.get('creator', ''),
                     '0x0000000000000000000000000000000000000000',
                     '0x000000000000000000000000000000000000dead', '11111111111111111111111111111111'])
    excluded = {address_key(asset['chain'], str(x)) for x in excluded if x}
    liquidity = number(asset.get('liquidity_usd'))
    r = config['large_buyers']
    threshold = max(r['net_buy_min_usd'], liquidity * r['net_buy_min_liquidity_fraction']) if liquidity and liquidity > 0 else None
    result = {'source': 'GeckoTerminal pool trades, bounded sample', 'observed_ms': stamp,
              'threshold_usd': threshold, 'windows': {}, 'wallet_wealth_verified': False,
              'independent_ownership_verified': False, 'complete_onchain_coverage': False,
              'scope': 'sampled initiator addresses, not verified holders, people or smart money',
              'support_only': True, 'status': 'unknown', 'support_points': None, 'support_max': 10}
    for minutes in (15, 30):
        start = stamp - minutes * 60000
        accounts = {}; bad = invalid; oldest = None; count = 0; gross_buy = 0.; gross_sell = 0.
        for data in unique.values():
            date = ms_iso(data.get('block_timestamp'))
            if date is None or date > stamp:
                bad += 1
                continue
            oldest = date if oldest is None else min(oldest, date)
            if date < start:
                continue
            if data.get('is_anomalous') is True:
                continue
            source = address_key(asset['chain'], str(data.get('from_token_address', '')))
            target = address_key(asset['chain'], str(data.get('to_token_address', '')))
            if (source == asset['mint']) == (target == asset['mint']):
                continue
            wallet = data.get('tx_from_address'); amount = number(data.get('volume_in_usd'))
            if not valid_address(asset['chain'], wallet) or amount is None or amount <= 0:
                bad += 1
                continue
            wallet = address_key(asset['chain'], wallet)
            if wallet in excluded:
                continue
            buying = target == asset['mint']
            side = 'buy_usd' if buying else 'sell_usd'
            account = accounts.setdefault(wallet, {'address': wallet, 'buy_usd': 0., 'sell_usd': 0., 'buy_trades': 0})
            account[side] += amount
            if buying:
                account['buy_trades'] += 1; gross_buy += amount
            else:
                gross_sell += amount
            count += 1
        warnings = []
        truncated = len(rows) >= 300 and (oldest is None or oldest > start)
        if truncated: warnings.append('window_truncated_by_trade_limit')
        if bad: warnings.append('invalid_or_missing_trade_fields')
        top_share = max((x['buy_usd'] for x in accounts.values()), default=0) / gross_buy if gross_buy else None
        if top_share is not None and top_share > r['top_buyer_fraction_warning']:
            warnings.append('single_initiator_dominates_buy_volume')
        large = []
        for account in accounts.values():
            account['net_buy_usd'] = account['buy_usd'] - account['sell_usd']
            if threshold is not None and account['buy_usd'] >= threshold and account['sell_usd'] / account['buy_usd'] >= r['resale_fraction_warning']:
                warnings.append('large_buyer_also_selling')
            if threshold is not None and account['net_buy_usd'] >= threshold:
                large.append(account)
        known = bool(count and threshold is not None and not bad and not truncated)
        points = min(8, len(large) * 3) + (2 if gross_buy > gross_sell and len(large) >= 2 else 0) if known else None
        if known and warnings: points = 0
        result['windows'][str(minutes)] = {'status': ('observed' if large else 'not_observed_in_sample') if known else 'unknown',
            'large_buyer_count': len(large) if known else None, 'observed_initiators': len(accounts),
            'sample_net_buy_usd': gross_buy - gross_sell if count else None, 'top_buyer_fraction': top_share,
            'large_buyers': sorted(large, key=lambda x: -x['net_buy_usd'])[:10],
            'warnings': sorted(set(warnings)), 'support_points': points,
            'returned_span_reaches_window_start': oldest is not None and oldest <= start,
            'complete_onchain_coverage': False}
    window = result['windows']['15']
    result['status'] = window['status']; result['support_points'] = window['support_points']
    return result


def observe(client, network, asset, security, stamp, config):
    try:
        payload = client.gecko(f"networks/{network['gecko']}/pools/{asset['pool']}/trades")
        return assess(payload, asset, security, stamp(), config)
    except Exception as exc:
        return {'status': 'unknown', 'support_only': True, 'support_points': None, 'support_max': 10,
                'observed_ms': stamp(), 'windows': {}, 'reason': str(exc)}


def text(result):
    if not result or result.get('status') == 'unknown':
        return 'Büyük alıcı katılımı: veri yetersiz; destek puanı bilinmiyor.'
    parts = []
    for minutes, window in result.get('windows', {}).items():
        n = window.get('large_buyer_count')
        parts.append(f"{minutes} dk: " + ('veri yetersiz' if n is None else f'{n} farklı işlem başlatıcı adres'))
    points = result.get('support_points')
    warnings = sorted({x for w in result.get('windows', {}).values() for x in w.get('warnings', [])})
    return ('Büyük alıcı katılımı: ' + '; '.join(parts) +
            f". Net alım eşiği ${result['threshold_usd']:.0f}; destek {points}/10 (deneysel). " +
            ('Uyarı: ' + ', '.join(warnings) + '. ' if warnings else '') +
            'Sınırlı işlem örneği; adreslerin serveti, bağımsızlığı ve başarısı doğrulanmadı.')
