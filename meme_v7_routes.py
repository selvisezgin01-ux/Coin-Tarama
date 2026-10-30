"""Indicative buy+sell quotes only. Never builds, signs or sends a transaction."""
from decimal import Decimal,ROUND_DOWN
from urllib.parse import urlencode
import time
import meme_rules as rules
import meme_followup_watch as prior

def raw_amount(value):
    if not isinstance(value,str) or not value.isdigit() or not 0<int(value)<10**60:raise ValueError('Invalid quote amount')
    return value

def stable_usd(client):
    pairs=client.dex('tokens/v1/solana/'+prior.USDC_SOL)
    rows=[p for p in pairs if p.get('chainId')=='solana' and (p.get('baseToken') or {}).get('address')==prior.USDC_SOL
          and rules.number(p.get('priceUsd')) and rules.number((p.get('liquidity') or {}).get('usd'))]
    if not rows:raise ValueError('USDC USD reference unavailable; never assume parity')
    row=max(rows,key=lambda p:float(p['liquidity']['usd']));value=float(row['priceUsd'])
    if not .5<value<1.5:raise ValueError('USDC USD reference outside diagnostic band')
    return value

def ray(client,origin,target,amount):
    data=client.request('https://transaction-v1.raydium.io/compute/swap-base-in?'+urlencode(
        {'inputMint':origin,'outputMint':target,'amount':amount,'slippageBps':50,'txVersion':'V0'}))
    r=data.get('data') or {}
    if data.get('success') is not True or r.get('swapType')!='BaseIn' or not r.get('routePlan'):raise ValueError('No Raydium route')
    if (r.get('inputMint'),r.get('outputMint'),str(r.get('inputAmount')))!=(origin,target,amount):raise ValueError('Raydium quote identity mismatch')
    raw_amount(r.get('outputAmount'));return r

def kyber(client,chain,origin,target,amount):
    path=prior.KYBER_CHAINS[chain]
    d=client.request('https://aggregator-api.kyberswap.com/'+path+'/api/v1/routes?'+urlencode(
        {'tokenIn':origin,'tokenOut':target,'amountIn':amount,'excludeRFQSources':'true','gasInclude':'true'}),headers={'X-Client-Id':'CoinTaramaMemeV7'})
    r=(d.get('data') or {}).get('routeSummary') or {};now=int(time.time()*1000)
    if d.get('code')!=0 or not r.get('route'):raise ValueError('No Kyber route')
    if (str(r.get('tokenIn','')).lower(),str(r.get('tokenOut','')).lower(),str(r.get('amountIn')))!=(origin.lower(),target.lower(),amount):raise ValueError('Kyber quote identity mismatch')
    stamp=rules.number(r.get('timestamp'))
    if stamp is None or not -60000<=now-stamp*1000<=120000:raise ValueError('Kyber quote stale or timestamp unknown')
    raw_amount(r.get('amountOut'));return r

def roundtrip(client,network,a,sec,cfg):
    stamp=int(time.time()*1000);base={'status':'unknown','observed_ms':stamp,'scope':'indicative_quote_to_quote_not_actual_execution',
        'actual_fill_verified':False,'all_costs_known':False,'net_realized_pnl_usd':None}
    try:
        decimals=prior.read_decimals(client,network,a,sec);size=cfg['v7']['quote_notional_usd']
        if a['chain']=='solana':
            usd=stable_usd(client);amount=str(int(Decimal(str(size))/Decimal(str(usd))*10**6))
            buy=ray(client,prior.USDC_SOL,a['mint'],amount);quantity=raw_amount(buy['outputAmount'])
            sell=ray(client,a['mint'],prior.USDC_SOL,quantity)
            input_usd=int(amount)/10**6*usd;output_usd=int(sell['outputAmount'])/10**6*usd
            gas=None;provider='Raydium';reference=usd
        else:
            ref=kyber(client,a['chain'],prior.NATIVE,a['mint'],str(10**16));ref_usd=rules.number(ref.get('amountInUsd'))
            if ref_usd is None or ref_usd<=0:raise ValueError('Native USD reference unavailable')
            amount=str(int(Decimal(10**16)*Decimal(str(size))/Decimal(str(ref_usd))))
            buy=kyber(client,a['chain'],prior.NATIVE,a['mint'],amount);quantity=raw_amount(buy['amountOut'])
            sell=kyber(client,a['chain'],a['mint'],prior.NATIVE,quantity)
            input_usd=rules.number(buy.get('amountInUsd'));output_usd=rules.number(sell.get('amountOutUsd'))
            if not input_usd or not output_usd:raise ValueError('Quote USD amounts unknown')
            gas_values=[rules.number(x.get('gasUsd')) for x in (buy,sell)]
            gas=sum(gas_values) if all(x is not None and x>=0 for x in gas_values) else None
            provider='KyberSwap';reference=None
        if not .9*size<=input_usd<=1.1*size:raise ValueError('Quote notional changed too far')
        loss=(1-output_usd/input_usd)*100
        # Implausible immediate positive roundtrips are not an arbitrage or fill claim.
        passed=-1<=loss<=cfg['v7']['roundtrip_loss_max_pct']
        return {**base,'status':'passed' if passed else 'failed','provider':provider,'token_decimals':decimals,
            'buy_input_raw':amount,'token_output_raw':quantity,'entry_input_usd':input_usd,'roundtrip_output_usd':output_usd,
            'roundtrip_loss_pct':loss,'gas_usd':gas,'stable_usd_reference':reference,
            'reason':'quote_roundtrip_within_experimental_budget' if passed else 'roundtrip_loss_or_cross_quote_inconsistency'}
    except Exception as exc:return {**base,'reason':str(exc)}

def exit_fixed(client,a,case):
    quantity=raw_amount(case['token_output_raw']);stamp=int(time.time()*1000)
    if a['chain']=='solana':
        usd=stable_usd(client);sell=ray(client,a['mint'],prior.USDC_SOL,quantity);output=int(sell['outputAmount'])/10**6*usd
    else:
        sell=kyber(client,a['chain'],a['mint'],prior.NATIVE,quantity);output=rules.number(sell.get('amountOutUsd'))
        if output is None or output<=0:raise ValueError('Exit USD value unknown')
    gross=(output/case['entry_input_usd']-1)*100
    return {'observed_ms':stamp,'output_usd':output,'quantity_raw':quantity,'gross_quote_return_pct':gross,
        'cost_scenarios_return_pct':{str(cost):gross-cost for cost in (.2,.5,1)},
        'all_costs_known':False,'actual_fill_verified':False,'net_realized_pnl_usd':None}
