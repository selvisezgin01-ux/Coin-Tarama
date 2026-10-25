"""Closed 15-minute meme setup rules and explicit unknown-data gates."""
from __future__ import annotations
import math

STEP_MS = 15*60000


def number(value):
    try:
        value=float(value)
        return value if math.isfinite(value) else None
    except (TypeError,ValueError): return None


def address_key(chain,address):
    return address if chain=='solana' else address.lower()


def available_candles(rows,asof_ms,include_open=False):
    output={}
    for raw in rows:
        if not isinstance(raw,list) or len(raw)!=6:raise ValueError('Unexpected OHLCV schema')
        stamp=int(raw[0])*1000
        values=[number(v) for v in raw[1:]]
        if any(v is None for v in values):raise ValueError('Invalid OHLCV numbers')
        opening,high,low,close,volume=values
        if stamp%STEP_MS or min(opening,high,low,close)<=0 or volume<0 or high<max(opening,low,close) or low>min(opening,high,close):
            raise ValueError('Invalid or misaligned OHLCV')
        if stamp>asof_ms or (not include_open and stamp+STEP_MS>asof_ms):continue
        row={'open_ms':stamp,'open':opening,'high':high,'low':low,'close':close,'volume':volume}
        if stamp in output and output[stamp]!=row:raise ValueError('Conflicting duplicate candle')
        output[stamp]=row
    return [output[k] for k in sorted(output)]


def closed_candles(rows,asof_ms):
    ordered=available_candles(rows,asof_ms)
    # Indicators restart after a gap; missing intervals are not manufactured.
    for i in range(len(ordered)-1,0,-1):
        if ordered[i]['open_ms']-ordered[i-1]['open_ms']!=STEP_MS:return ordered[i:]
    return ordered


def first_formation(rows,asset,earliest_pool_ms,asof_ms,config):
    """Negative history checks include wicks/open bars; never create a positive candle signal."""
    bars=available_candles(rows,asof_ms,include_open=True)
    result={'status':'unknown','reason':'initial_pool_history_missing','metrics':{}}
    created=number(asset.get('pool_created_ms'));earliest=number(earliest_pool_ms)
    if not bars or created is None or earliest is None:return result
    if earliest<created:
        result['reason']='earlier_pool_history_not_covered';return result
    start=int(created)//STEP_MS*STEP_MS
    initial=bars[0]['open'];floor=initial;runup=0.;peak=initial
    for bar in bars:
        # Include possible within-bar low-to-high rises conservatively: ordering is unknown.
        floor=min(floor,bar['low']);peak=max(peak,bar['high'])
        runup=max(runup,(bar['high']/floor-1)*100)
    last=bars[-1]['close'];r=config['first_formation']
    metrics={'available_bars':len(bars),'first_open_ms':bars[0]['open_ms'],'initial_open':initial,
             'max_observed_runup_pct':runup,'latest_from_initial_pct':(last/initial-1)*100,
             'drawdown_from_available_peak_pct':(1-last/peak)*100,
             'scope':'selected_pool_available_OHLCV_not_token_lifetime'}
    result['metrics']=metrics
    failures=[]
    if runup>r['max_observed_runup_pct']:failures.append('first_rise_already_observed')
    if metrics['latest_from_initial_pct']>r['max_current_gain_from_initial_pct']:failures.append('already_extended_from_initial_price')
    if metrics['drawdown_from_available_peak_pct']>r['max_drawdown_from_peak_pct']:failures.append('post_peak_rebound_excluded')
    if failures:return {**result,'status':'rejected','reason':','.join(failures)}
    # A quiet tail after a missing launch/gap is not evidence of no previous pump.
    if bars[0]['open_ms']!=start:return result
    if any(b['open_ms']-a['open_ms']!=STEP_MS for a,b in zip(bars,bars[1:])):
        return {**result,'reason':'initial_history_has_gaps'}
    if bars[-1]['open_ms']!=asof_ms//STEP_MS*STEP_MS:
        return {**result,'reason':'current_interval_history_missing'}
    return {**result,'status':'passed','reason':'no_threshold_crossing_in_available_pool_history'}


def pattern(candles,config):
    r=config['market'];count=r['setup_bars']
    result={'stage':None,'reason':'insufficient_closed_candles','metrics':{}}
    if len(candles)<count:return result
    latest=candles[-1]
    def setup(rows):
        high=max(x['high'] for x in rows);low=min(x['low'] for x in rows)
        net=(rows[-1]['close']/rows[0]['open']-1)*100
        width=(high/low-1)*100
        # Prevent calling a rebound after a large first pump a quiet accumulation.
        return (width<=r['accumulation_range_max_pct'] and abs(net)<=r['accumulation_net_change_max_pct']
                and rows[-1]['low']>=rows[0]['low']*.98 and all(x['volume']>0 for x in rows)
                and rows[-1]['volume']<=rows[0]['volume']*r['accumulation_last_first_volume_max_ratio']),high,low,width,net
    position=(latest['close']-latest['low'])/(latest['high']-latest['low']) if latest['high']>latest['low'] else 0.
    result['metrics']['close_position']=position
    if any((x['close']/x['open']-1)*100>r['max_previous_one_bar_gain_pct'] for x in candles):
        result['reason']='large_pump_already_in_available_history';return result
    peak=max(x['high'] for x in candles)
    drawdown=(1-latest['close']/peak)*100
    result['metrics']['observed_history_peak_drawdown_pct']=drawdown
    if drawdown>r['max_pool_peak_drawdown_pct']:
        result['reason']='large_drawdown_after_previous_peak';return result
    if len(candles)>=count+1:
        prior=candles[-count-1:-1]
        valid,resistance,low,width,net=setup(prior)
        average=sum(x['volume'] for x in prior)/count
        volume_ratio=latest['volume']/average if average>0 else 0.
        extension=(latest['close']/resistance-1)*100
        result['metrics'].update({'resistance':resistance,'breakout_volume_ratio':volume_ratio,'breakout_extension_pct':extension})
        if valid and latest['close']>resistance and volume_ratio>=r['breakout_volume_ratio_min'] and position>=r['breakout_close_position_min'] and extension<=r['breakout_extension_max_pct']:
            result.update({'stage':'first_breakout','reason':'closed_first_breakout'});return result
    valid,high,low,width,net=setup(candles[-count:])
    result['metrics'].update({'setup_range_pct':width,'setup_net_change_pct':net,'setup_high':high,'setup_low':low})
    if valid and position>=r['accumulation_close_position_min']:
        result.update({'stage':'accumulation','reason':'closed_accumulation_setup'})
    else:result['reason']='no_qualifying_setup'
    return result


def current_price_holds(price,setup,last_close,config):
    if price is None or price<=0 or last_close<=0:return False
    if abs(price/last_close-1)*100>config['market']['live_price_drift_max_pct']:return False
    if setup['stage']=='first_breakout':return price>=setup['metrics']['resistance']
    return price>=setup['metrics'].get('setup_low',last_close)*.98


def market_gates(asset,config,asof_ms,observations):
    r=config['market'];failures=[];unknown=[]
    created=number(asset.get('pool_created_ms'))
    age=None if created is None else (asof_ms-created)/60000
    if age is None:unknown.append('pool_age')
    elif not r['min_pool_age_minutes']<=age<=r['max_pool_age_hours']*60:failures.append('pool_age')
    liquidity=number(asset.get('liquidity_usd'))
    if liquidity is None:unknown.append('liquidity')
    elif liquidity<r['liquidity_min_usd']:failures.append('liquidity')
    cap=number(asset.get('market_cap_usd'));fdv=number(asset.get('fdv_usd'))
    # FDV is shown as a labelled proxy but never relabelled as circulating cap.
    valuation=cap if cap is not None and cap>0 else fdv
    if valuation is None or valuation<=0:unknown.append('valuation')
    elif not r['valuation_min_usd']<=valuation<=r['valuation_max_usd']:failures.append('valuation')
    if liquidity is not None and valuation is not None and valuation>0 and liquidity/valuation<r['liquidity_valuation_min_ratio']:
        failures.append('liquidity_to_valuation')
    vol=number(asset.get('volume15_usd'));buys=number(asset.get('buys15'));sells=number(asset.get('sells15'))
    if vol is None:unknown.append('volume15')
    elif vol<r['volume15_min_usd']:failures.append('volume15')
    if buys is None or sells is None:unknown.append('transactions15')
    elif buys+sells<r['trades15_min'] or buys/max(buys+sells,1)<r['buy_count_fraction_min']:failures.append('transaction_flow15')
    previous=[x for x in observations if asof_ms-60*60000<=x['ms']<asof_ms and number(x.get('liquidity')) is not None]
    if previous and liquidity is not None:
        prior=max(x['liquidity'] for x in previous)
        if prior>0 and (1-liquidity/prior)*100>r['liquidity_loss_max_pct']:failures.append('liquidity_withdrawal')
    return {'passed':not failures and not unknown,'failed':failures,'unknown':unknown,
            'pool_age_minutes':age,'valuation_usd':valuation,'valuation_kind':'market_cap_provider_reported' if cap is not None and cap>0 else 'fdv_proxy'}


def tier(market,setup,security,developer,maps,map_mode='automatic'):
    if map_mode not in ('automatic','manual'):raise ValueError('Unknown wallet-map policy')
    if market['failed'] or security.get('blocked') or maps.get('blocked') or developer.get('status')=='outgoing_transfer_detected':return 'rejected'
    if not market['passed'] or setup['stage'] is None:return 'watch'
    risk_complete=security.get('complete') or (not security.get('blocked') and set(security.get('unknown',[]))<={'complete_top10_non_pool_owners'} and maps.get('complete'))
    if risk_complete and developer.get('status')=='no_outgoing_transfers_in_complete_window' and (maps.get('complete') or map_mode=='manual') and market.get('valuation_kind')=='market_cap_provider_reported':
        return 'qualified'
    return 'review'
