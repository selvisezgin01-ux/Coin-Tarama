"""First closed base, early volume and token-oriented sampled buy pressure."""
from copy import deepcopy
from statistics import median
import time
import meme_rules as rules
import meme_hybrid as hybrid
import meme_pipeline as pipeline
import meme_sources as source

STEP=300000

class Client(pipeline.BudgetClient):
    """Keep one global request available for a qualified setup's trade check."""
    def __init__(self,cfg,backoff_until=0):
        super().__init__(cfg,backoff_until);self.flow_reserve=cfg['base_volume']['reserved_trade_requests']
    def gecko(self,path):
        is_flow='/trades' in path
        with self.lock:
            if is_flow:self.flow_reserve=0
            elif self.gecko_remaining<=self.flow_reserve:
                self.stats['gecko:reserved_for_buy_pressure']+=1
                raise RuntimeError('gecko_request_reserved_for_buy_pressure')
        return super().gecko(path)

def evaluate(rows,asset,earliest,stamp,cfg,anchor=None):
    formation=rules.first_formation(rows,asset,earliest,stamp,cfg,step_ms=STEP)
    bars=rules.available_candles(rows,stamp,step_ms=STEP)
    created=asset.get('pool_created_ms')
    bars=[b for b in bars if created is not None and b['open_ms']>=created]
    setup={'stage':None,'reason':'first_base_not_observed','metrics':{}}
    out={'formation':formation,'phase':'early_5m','setup':setup,'cutoff_ms':None,'last_close':None,'first_base':deepcopy(anchor)}
    count=cfg['base_volume']['base_bars'];market=cfg['market']
    if len(bars)<count+1:
        setup['reason']='need_three_base_bars_and_one_volume_bar';return out
    if any(b['open_ms']-a['open_ms']!=STEP for a,b in zip(bars,bars[1:])):
        setup['reason']='first_base_history_gap';return out
    if anchor is not None and anchor.get('pool')!=asset['pool']:
        setup['reason']='first_base_pool_changed';return out
    if anchor is None:
        # Find the earliest qualifying base using only bars already closed before the signal bar.
        for i in range(len(bars)-count):
            group=bars[i:i+count];high=max(b['high'] for b in group);low=min(b['low'] for b in group)
            width=(high/low-1)*100;net=(group[-1]['close']/group[0]['open']-1)*100
            if width<=market['accumulation_range_max_pct'] and abs(net)<=market['accumulation_net_change_max_pct'] and group[-1]['low']>=group[0]['low']*.98 and all(b['volume']>0 for b in group):
                anchor={'pool':asset['pool'],'start_ms':group[0]['open_ms'],'end_ms':group[-1]['open_ms']+STEP,
                    'high':high,'low':low,'volume_median_usd':median(b['volume'] for b in group),'width_pct':width,'net_change_pct':net}
                out['first_base']=anchor;break
    if anchor is None:return out
    last=bars[-1];cutoff=last['open_ms']+STEP;out.update(cutoff_ms=cutoff,last_close=last['close'])
    metrics={'setup_high':anchor['high'],'setup_low':anchor['low'],'resistance':anchor['high'],
        'base_start_ms':anchor['start_ms'],'base_end_ms':anchor['end_ms'],'volume_baseline_usd':anchor['volume_median_usd'],
        'latest_volume_usd':last['volume'],'volume_multiple':last['volume']/anchor['volume_median_usd'],
        'window_start_ms':last['open_ms'],'window_end_ms':cutoff,'latest_high':last['high']}
    setup['metrics']=metrics
    if last['open_ms']<anchor['end_ms']:setup['reason']='volume_bar_overlaps_base';return out
    if cutoff-anchor['end_ms']>cfg['base_volume']['base_valid_minutes']*60000:setup['reason']='first_base_expired';return out
    if stamp-cutoff>cfg['timeframes']['max_closed_lag_minutes']*60000:setup['reason']='closed_volume_bar_stale';return out
    if last['low']<anchor['low']*.98 or last['close']<anchor['low']:setup['reason']='first_base_lost';return out
    if metrics['volume_multiple']<cfg['base_volume']['volume_multiple_min'] or last['volume']<cfg['base_volume']['burst_volume_min_usd']:
        setup['reason']='early_volume_not_expanded';return out
    position=(last['close']-last['low'])/(last['high']-last['low']) if last['high']>last['low'] else 0
    if position<market['accumulation_close_position_min']:setup['reason']='volume_bar_close_weak';return out
    if last['close']>anchor['high']:
        extension=(last['close']/anchor['high']-1)*100
        if extension>market['breakout_extension_max_pct']:setup['reason']='first_base_breakout_extended';return out
        setup.update(stage='first_breakout',reason='first_base_breakout_requires_prior_delivered_preparation')
    else:setup.update(stage='accumulation',reason='first_base_early_volume_waiting_buy_pressure')
    fifteen=hybrid.aggregate_15m(rows,stamp)
    full15=[b for b in rules.available_candles(fifteen,stamp,step_ms=900000) if b['open_ms']>=created]
    if len(full15)>=3 and full15[-1]['low']>=anchor['low']*.98 and full15[-1]['close']>=anchor['low']:
        out['phase']='confirmed_15m'
    return out

def pressure(payload,asset,security,setup,stamp,cfg):
    r=cfg['base_volume'];m=setup['metrics'];start=m['window_start_ms'];end=m['window_end_ms']
    result={'status':'unknown','reasons':[],'window_start_ms':start,'window_end_ms':end,'checked_ms':stamp,
        'scope':'selected_pool_provider_sample_swap_direction_not_capital_inflow','independent_investors_verified':False,
        'complete_onchain_coverage':False,'buy_usd':None,'sell_usd':None,'net_buy_usd':None}
    rows=payload.get('data')
    if not isinstance(rows,list):result['reasons']=['trade_payload_missing'];return result
    unique={};bad=[];oldest=None;gross_all=0.;buy=sell=0.;buys=sells=0;accounts={};flags=[]
    excluded={rules.address_key(asset['chain'],str(x)) for x in security.get('excluded_known_accounts',[])}
    creator=rules.address_key(asset['chain'],str(security.get('creator') or ''))
    excluded|={creator,asset['pool'],'0x0000000000000000000000000000000000000000','0x000000000000000000000000000000000000dead','11111111111111111111111111111111'}
    for row in rows:
        if not isinstance(row,dict) or not isinstance(row.get('attributes'),dict):bad.append('malformed_trade');continue
        identity=row.get('id');data=row['attributes']
        if not isinstance(identity,str) or not identity:bad.append('trade_identity_missing');continue
        if identity in unique:
            if unique[identity]!=data:bad.append('conflicting_trade_identity')
            continue
        unique[identity]=data
        date=source.ms_iso(data.get('block_timestamp'))
        if date is None or date>stamp:bad.append('invalid_trade_time');continue
        oldest=date if oldest is None else min(oldest,date)
        if not start<=date<end:continue
        origin=rules.address_key(asset['chain'],str(data.get('from_token_address','')))
        target=rules.address_key(asset['chain'],str(data.get('to_token_address','')))
        if (origin==asset['mint'])==(target==asset['mint']):bad.append('trade_token_orientation_unknown');continue
        buying=target==asset['mint'];value=rules.number(data.get('volume_in_usd'));wallet=data.get('tx_from_address')
        if value is None or value<=0 or not source.valid_address(asset['chain'],wallet):bad.append('trade_amount_or_initiator_missing');continue
        if data.get('is_anomalous') is not False:bad.append('anomalous_or_unclassified_trade');continue
        if data.get('kind') not in (None,'buy' if buying else 'sell'):bad.append('trade_direction_conflict');continue
        gross_all+=value;wallet=rules.address_key(asset['chain'],wallet)
        if wallet==creator and not buying:flags.append('creator_selling_in_signal_window')
        if wallet in excluded:continue
        account=accounts.setdefault(wallet,{'buy':0.,'sell':0.});account['buy' if buying else 'sell']+=value
        if buying:buy+=value;buys+=1
        else:sell+=value;sells+=1
    expected=m['latest_volume_usd'];coverage=abs(gross_all/expected-1) if expected>0 else None
    if len(rows)>=300 and (oldest is None or oldest>start):bad.append('trade_window_truncated')
    if payload.get('meta',{}).get('next_cursor') and (oldest is None or oldest>start):bad.append('trade_window_more_pages')
    if coverage is None or coverage>r['trade_volume_reconciliation_tolerance']:bad.append('trade_ohlcv_volume_not_reconciled')
    if bad:result.update(reasons=sorted(set(bad)),sample_rows=len(rows),volume_reconciliation_error=coverage);return result
    total=buy+sell;fraction=buy/total if total else 0.;count_fraction=buys/(buys+sells) if buys+sells else 0.
    top=max((a['buy'] for a in accounts.values()),default=0.)/buy if buy else 0.
    net_buyers=sum(a['buy']>a['sell'] for a in accounts.values());net=buy-sell
    if fraction<r['buy_volume_fraction_min']:flags.append('buy_volume_not_dominant')
    if count_fraction<r['buy_count_fraction_min']:flags.append('buy_count_not_dominant')
    if net<r['net_buy_min_usd']:flags.append('net_buy_value_insufficient')
    if buys+sells<r['minimum_trades']:flags.append('trade_count_insufficient')
    if net_buyers<r['minimum_net_buy_initiators']:flags.append('too_few_net_buy_initiators')
    if top>r['top_buyer_fraction_max']:flags.append('buy_volume_single_initiator_dominated')
    result.update(status='failed' if flags else 'passed',reasons=sorted(set(flags)),buy_usd=buy,sell_usd=sell,net_buy_usd=net,
        buy_volume_fraction=fraction,buy_count_fraction=count_fraction,buy_trades=buys,sell_trades=sells,
        net_buy_initiators=net_buyers,top_buyer_fraction=top,volume_reconciliation_error=coverage,sample_rows=len(rows))
    return result

def fresh_observation(client,network,asset):
    payload=client.dex('latest/dex/pairs/'+network['dex']+'/'+asset['pool']);stamp=int(time.time()*1000)
    for row in payload.get('pairs') or []:
        if row.get('chainId')!=network['dex']:continue
        if rules.address_key(asset['chain'],str(row.get('pairAddress') or ''))!=asset['pool']:continue
        if rules.address_key(asset['chain'],str((row.get('baseToken') or {}).get('address') or ''))!=asset['mint']:continue
        price=rules.number(row.get('priceUsd'));cap=rules.number(row.get('marketCap'));liq=rules.number((row.get('liquidity') or {}).get('usd'))
        if price is None or price<=0:raise ValueError('Fresh exact-pool price missing')
        return {'price_usd':price,'price_observed_ms':stamp,'market_cap_usd':cap if cap and cap>0 else None,
            'market_cap_observed_ms':stamp,'liquidity_usd':liq,'fdv_usd':rules.number(row.get('fdv')),'price_source':'dexscreener_matched_pool'}
    raise ValueError('Fresh exact token and pool identity not matched')

def text(result):
    if not result or result.get('status')!='passed':return 'Alım yönlü hacim: doğrulanamadı; olumlu teyit değildir.'
    return (f"Kapalı 5dk işlem örneği: alım ${result['buy_usd']:.0f}, satım ${result['sell_usd']:.0f}, fark +${result['net_buy_usd']:.0f}; "
        f"alım hacim payı %{100*result['buy_volume_fraction']:.1f}, net alıcı işlem başlatıcı {result['net_buy_initiators']}. "
        'Bağımsız yatırımcı, balina veya toplam sermaye girişi kanıtı değildir.')
