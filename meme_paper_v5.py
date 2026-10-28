"""Frozen token quantities, read-only indicative exits. Unknown execution costs remain unknown."""
from copy import deepcopy
from urllib.parse import urlencode
import meme_followup_watch as routes
import meme_rules as rules

def register(state,record,phase,stamp):
    asset=record['latest'];key=asset['chain']+':'+asset['mint']+':'+phase
    cases=state.setdefault('paper_v5',{'cases':{},'errors':[]})['cases']
    if key in cases:return
    cases[key]={'chain':asset['chain'],'mint':asset['mint'],'pool':asset['pool'],'symbol':asset['symbol'],'phase':phase,
        'observed_ms':asset['observed_ms'],'provider_entry_price':asset['price_usd'],'entry_kind':'observed_provider_price_not_buy_fill',
        'outcomes':{},'sizes':{},'marks':[],'max_observed_return_pct':0.,'min_observed_return_pct':0.,
        'structural_invalid_price':record.get('setup',{}).get('metrics',{}).get('setup_low')}

def quote_fixed(client,network,asset,security,case,size,stamp):
    item=case['sizes'].get(str(size))
    if not item:
        decimals=routes.read_decimals(client,network,asset,security)
        item={'input_raw':routes.decimal_units(size,case['provider_entry_price'],decimals),'token_decimals':decimals,
              'reference_usd':size,'quantity_basis':'assumed_at_first_observed_provider_price','status':'open','quotes':[]}
        case['sizes'][str(size)]=item
    amount=item['input_raw']
    if asset['chain']=='solana':
        query=urlencode({'inputMint':asset['mint'],'outputMint':routes.USDC_SOL,'amount':amount,'slippageBps':50,'txVersion':'V0'})
        data=client.request('https://transaction-v1.raydium.io/compute/swap-base-in?'+query)
    else:
        query=urlencode({'tokenIn':asset['mint'],'tokenOut':routes.NATIVE,'amountIn':amount,'excludeRFQSources':'true','gasInclude':'true'})
        data=client.request('https://aggregator-api.kyberswap.com/'+routes.KYBER_CHAINS[asset['chain']]+'/api/v1/routes?'+query,headers={'X-Client-Id':'CoinTaramaMeme'})
    q=routes.parse_route(data,asset,amount,stamp)
    usd=rules.number(q.get('output_usd'));q.update({'reference_usd':size,'input_raw':amount,
        'net_realized_pnl_usd':None,'all_costs_known':False,'buy_execution_unknown':True})
    q['indicative_gross_return_pct']=None if usd is None else (usd/size-1)*100
    item['latest']=q;item['quotes']=(item['quotes']+[q])[-60:]
    return q

def update(case,asset,stamp,cfg,quotes):
    ret=(asset['price_usd']/case['provider_entry_price']-1)*100
    case['max_observed_return_pct']=max(case['max_observed_return_pct'],ret);case['min_observed_return_pct']=min(case['min_observed_return_pct'],ret)
    case['marks']=(case['marks']+[{'observed_ms':stamp,'return_pct':ret}])[-100:]
    for h in cfg['pipeline']['measurement_horizons_minutes']:
        if str(h) in case['outcomes'] or stamp<case['observed_ms']+h*60000:continue
        delay=stamp-case['observed_ms']-h*60000;valid=delay<=cfg['pipeline']['measurement_max_delay_minutes']*60000
        case['outcomes'][str(h)]={'observed_ms':stamp,'delay_ms':delay,'provider_return_pct':ret if valid else None,
            'status':'observed_provider_mark' if valid else 'missed_window','indicative_exit_quotes':deepcopy(quotes) if valid else [],
            'net_realized_pnl_usd':None,'full_path_mae_mfe':None}
    for size,item in case['sizes'].items():
        if item['status']!='open':continue
        q=item.get('latest',{});gross=q.get('indicative_gross_return_pct');reason=None
        if q.get('observed_ms')!=stamp:gross=None
        invalid=case.get('structural_invalid_price')
        if gross is not None and invalid is not None and asset['price_usd']<invalid:reason='structure_lost_with_observed_sell_quote'
        elif gross is not None and gross<=-cfg['pipeline']['exit_stop_pct']:reason='observed_sell_quote_stop'
        elif gross is not None and gross>=cfg['pipeline']['exit_target_pct']:reason='observed_sell_quote_target'
        elif stamp-case['observed_ms']>=cfg['pipeline']['exit_timeout_minutes']*60000:reason='timeout'
        if reason:item.update({'status':'closed_indicative','exit_reason':reason,'exit_observed_ms':stamp,'exit_quote':deepcopy(q) if q.get('observed_ms')==stamp else None,
                              'net_realized_pnl_usd':None,'intraperiod_stop_target_order':'unknown'})

def path_metrics(case,raw,stamp):
    step=300000;start=math_ceil(case['observed_ms'],step);end=stamp//step*step
    bars=rules.available_candles(raw,stamp,step_ms=step)
    selected={b['open_ms']:b for b in bars if start<=b['open_ms']<end}
    full=end>start and all(t in selected for t in range(start,end,step))
    return {'status':'complete_closed_5m_subwindow' if full else 'unknown_or_gapped','start_ms':start,'end_ms':end,
        'entry_fragment_omitted_ms':start-case['observed_ms'],'current_fragment_omitted_ms':stamp-end,
        'mae_pct':min(0,(min(b['low'] for b in selected.values())/case['provider_entry_price']-1)*100) if full else None,
        'mfe_pct':max(0,(max(b['high'] for b in selected.values())/case['provider_entry_price']-1)*100) if full else None,
        'full_trade_path':False}
def math_ceil(value,step):return (value+step-1)//step*step

def observe(state,cfg,client,stamp):
    paper=state.setdefault('paper_v5',{'cases':{},'errors':[]});paper['errors']=[]
    cases=[c for c in paper['cases'].values() if len(c['outcomes'])<len(cfg['pipeline']['measurement_horizons_minutes']) or any(s['status']=='open' for s in c['sizes'].values())]
    cases.sort(key=lambda c:(c.get('last_attempt_ms',0),c['observed_ms']))
    for case in cases[:2]:
        case['last_attempt_ms']=stamp;key=case['chain']+':'+case['mint'];record=state['assets'].get(key)
        if not record:continue
        asset=record['latest'];network=cfg['networks'][case['chain']]
        if asset['pool']!=case['pool']:paper['errors'].append(key+': original pool changed');continue
        quotes=[]
        try:asset={**asset,**__import__('meme_sources').quote(client,network,asset)}
        except Exception as e:paper['errors'].append(key+': '+str(e));continue
        stamp=asset['price_observed_ms']
        try:case['closed_5m_path']=path_metrics(case,__import__('meme_sources').candles(client,network,asset,stamp),stamp)
        except Exception as e:case['closed_5m_path']={'status':'unknown','reason':str(e),'mae_pct':None,'mfe_pct':None}
        for size in (100,500):
            try:quotes.append(quote_fixed(client,network,asset,record.get('security',{}),case,size,stamp))
            except Exception as e:quotes.append({'reference_usd':size,'status':'unknown','reason':str(e),'observed_ms':stamp,'net_realized_pnl_usd':None})
        update(case,asset,stamp,cfg,quotes)
