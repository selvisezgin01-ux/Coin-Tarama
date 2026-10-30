"""Causal first-liquid-base experiment. Radar is not an entry or a profit claim."""
from copy import deepcopy
from statistics import median
import hashlib,json,math
import meme_rules as rules
import meme_hybrid as hybrid

STEP=300000
LABELS={'early_radar':'🟡 ERKEN RADAR','entry_5m':'🟢🎯 GİRİŞ TEYİDİ',
        'confirmed_15m':'🔵 GÜÇLENME — 15dk mum','structure_lost':'🔴 YAPI KAYBI',
        'liquidity_loss':'🔴 LİKİDİTE KAYBI','risk_detected':'🔴 GÜVENLİK UYARISI',
        'buy_pressure_weakening':'🟠 ALIM BASKISI ZAYIFLIYOR','exit_timeout':'🟠 İZLEME SÜRESİ DOLDU',
        'target_observed':'🟣🎯 GÖSTERGE HEDEF GÖRÜLDÜ'}

def key(a):return a['chain']+':'+rules.address_key(a['chain'],a['mint'])

def market(a,cfg,now):
    r=cfg['market'];failed=[];unknown=[]
    values={name:rules.number(a.get(name)) for name in ('price_usd','liquidity_usd','market_cap_usd','pool_created_ms','price_observed_ms')}
    for name,v in values.items():
        if v is None or (name!='pool_created_ms' and v<=0):unknown.append(name)
    price=values['price_usd'];liq=values['liquidity_usd'];cap=values['market_cap_usd'];created=values['pool_created_ms'];stamp=values['price_observed_ms']
    if stamp is not None and not 0<=now-stamp<=cfg['v7']['quote_max_age_seconds']*1000:failed.append('quote_stale_or_future')
    if created is not None and not 0<=now-created<=r['max_pool_age_hours']*3600000:failed.append('pool_age')
    if liq is not None and liq<r['liquidity_min_usd']:failed.append('liquidity')
    if cap is not None and not r['valuation_min_usd']<=cap<=r['valuation_max_usd']:failed.append('market_cap_not_50k_500k')
    if liq is not None and cap is not None and cap>0 and liq/cap<r['liquidity_valuation_min_ratio']:failed.append('liquidity_to_cap')
    return {'passed':not failed and not unknown,'failed':failed,'unknown':unknown,
            'valuation_kind':'market_cap_provider_reported' if cap is not None else 'market_cap_unknown',
            'valuation_usd':cap,'pool_age_minutes':None if created is None else (now-created)/60000}

def activity(a,cfg):
    r=cfg['v7'];vol=rules.number(a.get('volume5_usd'));buys=rules.number(a.get('buys5'));sells=rules.number(a.get('sells5'))
    failed=[]
    if vol is None or vol<r['radar_volume5_min_usd']:failed.append('activity_volume5_insufficient_or_unknown')
    if buys is None or sells is None or buys+sells<r['radar_trades5_min']:failed.append('activity_trades5_insufficient_or_unknown')
    elif buys/(buys+sells)<r['radar_buy_count_min_fraction']:failed.append('buy_count_not_dominant')
    return {'passed':not failed,'reasons':failed,'volume5_usd':vol,'buys5':buys,'sells5':sells,
            'buy_count_fraction':None if buys is None or sells is None or buys+sells<=0 else buys/(buys+sells),
            'buy_volume_verified':False,'independent_buyers_verified':False}

def first_base(raw,a,record,now,cfg):
    """Anchor only after a REAL V7 eligible observation; do not infer historical MCAP."""
    r=cfg['v7'];start=record.get('eligible_since_ms');anchor=deepcopy(record.get('first_base'))
    out={'stage':None,'reason':'awaiting_actual_eligible_observation','metrics':{},'first_base':anchor,
         'scope':'selected_pool_since_real_v7_eligibility_not_token_lifetime','cutoff_ms':None,'last_close':None}
    if start is None:return out
    bars=rules.available_candles(raw,now,step_ms=STEP)
    bars=[b for b in bars if b['open_ms']>=start]
    if not bars:out['reason']='no_closed_bar_after_actual_eligibility';return out
    expected=((start+STEP-1)//STEP)*STEP
    if bars[0]['open_ms']!=expected:out['reason']='first_eligible_interval_history_missing';return out
    if any(b['open_ms']-a0['open_ms']!=STEP for a0,b in zip(bars,bars[1:])):
        out['reason']='eligible_history_gap';return out
    if now-(bars[-1]['open_ms']+STEP)>cfg['timeframes']['max_closed_lag_minutes']*60000:
        out['reason']='closed_candles_stale';return out
    peak=max(b['high'] for b in bars);drawdown=(1-bars[-1]['close']/peak)*100
    out['metrics']['drawdown_from_available_peak_pct']=drawdown
    if record.get('dump_disqualified') or drawdown>r['severe_drawdown_pct']:
        out['reason']='severe_dump_after_observed_eligibility';out['latch_dump']=True;return out
    if anchor and anchor['pool']!=a['pool']:out['reason']='first_base_pool_changed';return out
    n=r['base_bars']
    if anchor is None:
        for i in range(max(0,len(bars)-n)):
            group=bars[i:i+n];hi=max(b['high'] for b in group);lo=min(b['low'] for b in group)
            width=(hi/lo-1)*100;net=(group[-1]['close']/group[0]['open']-1)*100
            if width<=r['base_range_max_pct'] and abs(net)<=r['base_net_max_pct'] and group[-1]['low']>=group[0]['low']*.98 and all(b['volume']>0 for b in group):
                anchor={'pool':a['pool'],'start_ms':group[0]['open_ms'],'end_ms':group[-1]['open_ms']+STEP,
                        'high':hi,'low':lo,'volume_median_usd':median(b['volume'] for b in group),
                        'width_pct':width,'net_change_pct':net,'eligibility_observed_ms':start}
                out['first_base']=anchor;break
    if anchor is None:out['reason']='need_two_quiet_base_bars_and_separate_volume_bar';return out
    latest=bars[-1];cutoff=latest['open_ms']+STEP
    out.update(cutoff_ms=cutoff,last_close=latest['close'])
    out['metrics'].update(setup_low=anchor['low'],setup_high=anchor['high'],resistance=anchor['high'],
        base_start_ms=anchor['start_ms'],base_end_ms=anchor['end_ms'],window_start_ms=latest['open_ms'],window_end_ms=cutoff,
        latest_volume_usd=latest['volume'],volume_multiple=latest['volume']/anchor['volume_median_usd'],
        latest_high=latest['high'],volume_baseline_usd=anchor['volume_median_usd'])
    if latest['open_ms']<anchor['end_ms']:out['reason']='volume_bar_overlaps_base';return out
    if cutoff-anchor['end_ms']>r['base_valid_minutes']*60000:out['reason']='first_liquid_base_expired';return out
    if latest['close']<anchor['low']*.98:out['reason']='first_liquid_base_lost';out['latch_dump']=True;return out
    extension=(latest['close']/anchor['high']-1)*100
    if extension>r['entry_extension_max_pct']:out['reason']='too_far_from_first_liquid_base';return out
    pos=(latest['close']-latest['low'])/(latest['high']-latest['low']) if latest['high']>latest['low'] else 0
    if latest['close']<=latest['open'] or pos<r['volume_bar_close_position_min']:out['reason']='volume_bar_close_weak';return out
    if out['metrics']['volume_multiple']<cfg['base_volume']['volume_multiple_min'] or latest['volume']<cfg['base_volume']['burst_volume_min_usd']:
        out['reason']='volume_not_accelerating';return out
    out.update(stage='first_breakout' if latest['close']>anchor['high'] else 'accumulation',
               reason='first_liquid_base_price_volume_ready')
    return out

def entry_guard(a,setup,pressure,sec,dev,maps,route,cfg,now):
    failed=[];unknown=[];gate=market(a,cfg,now)
    failed+=gate['failed'];unknown+=gate['unknown']
    if setup.get('stage') is None:failed.append(setup.get('reason','price_structure_missing'))
    tier=rules.tier(gate,{'stage':setup.get('stage')},sec,dev,maps,cfg['risk']['wallet_map_mode'])
    if sec.get('blocked') or maps.get('blocked') or dev.get('status')=='outgoing_transfer_detected':failed.append('risk_blocked')
    elif tier!='qualified':unknown.append('security_or_developer_not_complete')
    if pressure.get('status')!='passed':(failed if pressure.get('status')=='failed' else unknown).append('buy_volume_not_verified')
    if route.get('status')!='passed':(failed if route.get('status')=='failed' else unknown).append('buy_sell_roundtrip_not_verified')
    price=rules.number(a.get('price_usd'));anchor=setup.get('first_base') or {};low=rules.number(anchor.get('low'));high=rules.number(anchor.get('high'))
    stop=None if low is None else low*.98
    risk=None if not price or stop is None else (price-stop)/price*100
    if risk is None:unknown.append('risk_distance_unknown')
    elif not cfg['v7']['risk_min_pct']<=risk<=cfg['v7']['risk_max_pct']:failed.append('risk_distance_out_of_band')
    if price and high and price>high*(1+cfg['v7']['entry_extension_max_pct']/100):failed.append('live_price_extended_from_base')
    if price and stop and price<=stop:failed.append('live_price_lost_base')
    cutoff=setup.get('cutoff_ms')
    if cutoff is None or not 0<=now-cutoff<=cfg['timeframes']['max_closed_lag_minutes']*60000:unknown.append('feature_cutoff_stale_or_unknown')
    # 2R is a scenario projection, never known resistance room or an execution promise.
    cost=cfg['v7']['additional_cost_assumption_pct'];target=None if risk is None or not price else price*(1+(2*risk+cost)/100)
    return {'passed':not failed and not unknown,'failed':sorted(set(failed)),'unknown':sorted(set(unknown)),
        'stop_reference':stop,'risk_pct':risk,'target_projection':target,'target_kind':'2R_scenario_not_verified_resistance',
        'additional_cost_assumption_pct':cost,'actual_execution_or_net_profit_verified':False}

def strengthened(raw,entry,now):
    bars=rules.available_candles(hybrid.aggregate_15m(raw,now),now,step_ms=900000)
    bars=[b for b in bars if b['open_ms']>=entry['observed_ms']]
    if not bars:return False
    b=bars[-1];base=entry['base']
    return b['close']>base['high'] and b['low']>=base['low']*.98 and b['close']>b['open']

def event(state,a,phase,now,details,limit=None):
    identity=hashlib.sha256((key(a)+'|'+phase).encode()).hexdigest()[:24]
    if identity in state.setdefault('events',{}):return None
    if limit is not None:
        recent=sum(e['phase']==phase and 0<=now-e['observed_ms']<3600000 for e in state['events'].values())
        if recent>=limit:return None
    row={'id':identity,'key':key(a),'chain':a['chain'],'mint':a['mint'],'pool':a['pool'],
         'symbol':str(a.get('symbol','?'))[:40],'phase':phase,'observed_ms':now,'price':a['price_usd'],
         'market_cap_usd':a.get('market_cap_usd'),'liquidity_usd':a.get('liquidity_usd'),'details':deepcopy(details)}
    state['events'][identity]=row;return row
