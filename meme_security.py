"""Provider risk reports, holder concentration and bounded read-only creator checks."""
from __future__ import annotations
import os
import time

from meme_rules import address_key,number
from meme_sources import valid_address

TRANSFER='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
BURN={'0x0000000000000000000000000000000000000000','0x000000000000000000000000000000000000dead','11111111111111111111111111111111'}


def concentration(holders,excluded,chain,config):
    owners={}
    for holder in holders:
        owner=holder.get('owner') or holder.get('address')
        pct=number(holder.get('pct'))
        if not owner or pct is None or pct<0:continue
        owner=address_key(chain,owner)
        if owner in excluded or owner in BURN:continue
        owners[owner]=owners.get(owner,0.)+pct
    shares=sorted(owners.values(),reverse=True)
    largest=shares[0] if shares else None
    top10=sum(shares[:10]) if len(shares)>=10 else None
    r=config['risk']
    blocked=bool(largest is not None and largest>r['single_unexcluded_owner_max_pct_total_supply'])
    blocked=blocked or bool(top10 is not None and top10>r['top10_unexcluded_owner_max_pct_total_supply'])
    return {'largest_owner_pct':largest,'top10_owner_pct':top10,'owners_observed':len(shares),
            'holder_concentration_blocked':blocked,'holder_concentration_complete':top10 is not None,
            'excluded_known_accounts':sorted(excluded),'percentage_denominator':'provider total supply, not inferred circulating supply'}


def parse_rug(report,asset,config):
    unknown=[];risks=[];token=report.get('token') or {}
    for field in ['mintAuthority','freezeAuthority']:
        if field not in token and field not in report:unknown.append(field)
        elif token.get(field,report.get(field)) is not None:risks.append(field+'_active')
    if report.get('rugged') is True:risks.append('provider_reports_rugged')
    for risk in report.get('risks') or []:
        if str(risk.get('level','')).lower()=='danger':risks.append(str(risk.get('name','danger'))[:100])
    extensions=report.get('token_extensions')
    warnings=[]
    if extensions:
        if not isinstance(extensions,dict):unknown.append('token_extensions_need_review')
        else:
            metadata={'metadataPointer','tokenMetadata','groupPointer','groupMemberPointer','tokenGroup','tokenGroupMember'}
            if extensions.get('nonTransferable') is True:risks.append('non_transferable')
            for field,value in extensions.items():
                if field not in metadata|{'nonTransferable'} and value not in (None,False):unknown.append('extension_'+field)
            if (extensions.get('tokenMetadata') or {}).get('authority'):warnings.append('metadata_can_change_not_originality_proof')
    excluded=set(BURN)
    for market in report.get('markets') or []:
        for field in ['pubkey','liquidityA','liquidityB']:
            if market.get(field):excluded.add(market[field])
        for field in ['liquidityAAccount','liquidityBAccount']:
            if (market.get(field) or {}).get('owner'):excluded.add(market[field]['owner'])
    holders=report.get('topHolders') or []
    owner=report.get('creator');raw_supply=number(token.get('supply'))
    decimals=token.get('decimals');supply=raw_supply/10**decimals if raw_supply and isinstance(decimals,int) else None
    creator_pct=None
    if owner and raw_supply:
        amounts=[number(h.get('amount')) for h in holders if h.get('owner')==owner]
        if amounts and all(x is not None for x in amounts):creator_pct=sum(amounts)/raw_supply*100
        elif number(report.get('creatorBalance'))==0:creator_pct=0.
    if creator_pct is not None and creator_pct>config['risk']['developer_holdings_max_pct']:risks.append('creator_concentration')
    count=number(report.get('totalHolders'))
    if count is None:unknown.append('holder_count')
    elif count<config['risk']['holder_count_min']:risks.append('too_few_holders')
    holder_info=concentration(holders,excluded,asset['chain'],config)
    if holder_info['holder_concentration_blocked']:risks.append('holder_concentration')
    if not holder_info['holder_concentration_complete']:unknown.append('complete_top10_non_pool_owners')
    if not report.get('markets'):unknown.append('pool_security_and_liquidity_lock')
    lock={'status':'unknown','locked_pct':None,'scope':'exact_selected_pool'}
    for market in report.get('markets') or []:
        if market.get('pubkey')!=asset['pool']:continue
        pct=number((market.get('lp') or {}).get('lpLockedPct'))
        if pct is not None and 0<=pct<=100:
            kind=market.get('marketType','unknown')
            lock={'status':'provider_reported','locked_pct':pct,'scope':'exact_selected_pool','market_type':kind,
                  'note':'Bonding curve/launch inventory is not automatically equivalent to a classic withdrawable LP token lock.'}
    return {'source':'RugCheck','creator':owner,'creator_pct':creator_pct,'supply_normalized':supply,'liquidity_lock':lock,
            'holder_count':count,'token_decimals':decimals,'buy_tax_fraction':None,'sell_tax_fraction':None,
            'warnings':warnings,'reported_insider_networks':len(report.get('insiderNetworks') or []),
            'blocked':bool(risks),'risks':risks,'unknown':unknown,'complete':not risks and not unknown,
            'report_fetch_age_is_not_report_cache_age':True,**holder_info}


def parse_goplus(report,asset,config):
    risks=[];unknown=[]
    required={'is_honeypot':'0','cannot_buy':'0','is_mintable':'0','hidden_owner':'0',
              'can_take_back_ownership':'0','transfer_pausable':'0','selfdestruct':'0',
              'slippage_modifiable':'0','is_open_source':'1','is_proxy':'0','owner_change_balance':'0',
              'is_blacklisted':'0','is_whitelisted':'0','cannot_sell_all':'0'}
    for key,safe in required.items():
        if key not in report or str(report[key]) not in ('0','1'):unknown.append(key)
        elif str(report[key])!=safe:risks.append(key)
    for key in ['buy_tax','sell_tax']:
        value=number(report.get(key))
        if value is None:unknown.append(key)
        elif value<0 or value>config['risk']['evm_tax_max_fraction']:risks.append(key)
    counterfeit=report.get('fake_token')
    if isinstance(counterfeit,dict) and str(counterfeit.get('value'))=='1':risks.append('provider_reports_counterfeit')
    excluded=set(BURN)
    for pool in report.get('dex') or []:
        for key in ['pair','pool_manager']:
            address=pool.get(key)
            if address and valid_address(asset['chain'],address):excluded.add(address.lower())
    holders=[{'address':h.get('address'),'pct':None if number(h.get('percent')) is None else float(h['percent'])*100} for h in report.get('holders') or []]
    holder_info=concentration(holders,excluded,asset['chain'],config)
    if holder_info['holder_concentration_blocked']:risks.append('holder_concentration')
    if not holder_info['holder_concentration_complete']:unknown.append('complete_top10_non_pool_owners')
    creator_pct=number(report.get('creator_percent'))
    if creator_pct is not None:creator_pct*=100
    if creator_pct is not None and creator_pct>config['risk']['developer_holdings_max_pct']:risks.append('creator_concentration')
    count=number(report.get('holder_count'))
    if count is None:unknown.append('holder_count')
    elif count<config['risk']['holder_count_min']:risks.append('too_few_holders')
    # GoPlus LP holders can aggregate several pools. Do not assign an aggregate
    # locked share to the particular pool being scanned, especially V3/V4 NFTs.
    lock={'status':'unknown','locked_pct':None,'scope':'exact_selected_pool',
          'note':'Aggregated LP-holder data does not prove this selected pool or position is locked.'}
    return {'source':'GoPlus','creator':report.get('creator_address'),'creator_pct':creator_pct,'liquidity_lock':lock,
            'holder_count':count,'token_decimals':None,'buy_tax_fraction':number(report.get('buy_tax')),'sell_tax_fraction':number(report.get('sell_tax')),
            'supply_normalized':number(report.get('total_supply')),'blocked':bool(risks),'risks':risks,
            'unknown':unknown,'complete':not risks and not unknown,
            'report_fetch_age_is_not_report_cache_age':True,**holder_info}


def solana_crosscheck(report,rug_report,parsed,asset,config):
    """Require independently returned authority/transfer fields; missing is unknown."""
    risks=list(parsed['risks']);unknown=list(parsed['unknown']);warnings=list(parsed.get('warnings',[]))
    for field in ['mintable','freezable','closable','balance_mutable_authority','transfer_fee_upgradable',
                  'default_account_state_upgradable','transfer_hook_upgradable']:
        value=(report.get(field) or {}).get('status')
        if str(value) not in ('0','1'):unknown.append('goplus_'+field)
        elif str(value)=='1':risks.append('goplus_'+field)
    if str(report.get('non_transferable')) not in ('0','1'):unknown.append('goplus_non_transferable')
    elif str(report['non_transferable'])=='1':risks.append('goplus_non_transferable')
    if str(report.get('default_account_state'))!='1':
        (risks if str(report.get('default_account_state'))=='2' else unknown).append('goplus_default_account_state')
    hooks=report.get('transfer_hook')
    if hooks is None:unknown.append('goplus_transfer_hook')
    elif hooks:unknown.append('goplus_transfer_hook_requires_review')
    fee=report.get('transfer_fee')
    if fee is None:unknown.append('goplus_transfer_fee')
    elif fee:unknown.append('goplus_transfer_fee_requires_review')
    else:
        # An empty GoPlus fee object is not itself proof of zero fees.
        ext=rug_report.get('token_extensions') or {}
        if ext.get('transferFeeConfig') is not None:unknown.append('transfer_fee_not_resolved')
    creators=report.get('creators') or report.get('creator') or []
    if isinstance(creators,dict):creators=[creators]
    reported={address_key('solana',r['address']) for r in creators if isinstance(r,dict) and r.get('address')}
    if any(str(r.get('malicious_address'))=='1' for r in creators if isinstance(r,dict)):risks.append('goplus_malicious_creator')
    if reported and parsed.get('creator') not in reported:unknown.append('creator_identity_conflict')
    if not reported:warnings.append('goplus_creator_identity_not_available')
    supplied=number(report.get('total_supply'));rug_supply=parsed.get('supply_normalized')
    if supplied and rug_supply and abs(supplied/rug_supply-1)>.01:unknown.append('provider_supply_conflict')
    return {**parsed,'source':'RugCheck + GoPlus Solana','risks':sorted(set(risks)),'unknown':sorted(set(unknown)),
            'warnings':sorted(set(warnings)),'blocked':bool(risks),'complete':not risks and not unknown,
            'goplus_solana_crosscheck':True}


def fetch_security(client,network,asset):
    if network['security']=='rugcheck':
        report=client.request('https://api.rugcheck.xyz/v1/tokens/'+asset['mint']+'/report')
        if report.get('mint')!=asset['mint']:raise ValueError('RugCheck returned another mint')
        parsed=parse_rug(report,asset,client.config)
        try:cross=client.request('https://api.gopluslabs.io/api/v1/solana/token_security?contract_addresses='+asset['mint'])
        except Exception:
            return {**parsed,'complete':False,'unknown':parsed['unknown']+['goplus_solana_unavailable']}
        data=(cross.get('result') or {}).get(asset['mint']) if cross.get('code')==1 else None
        if not data:
            return {**parsed,'complete':False,'unknown':parsed['unknown']+['goplus_solana_report_missing']}
        return solana_crosscheck(data,report,parsed,asset,client.config)
    # Supported chains are checked at runtime; unsupported is unknown, never safe.
    if not hasattr(client,'goplus_chains'):
        response=client.request('https://api.gopluslabs.io/api/v1/supported_chains')
        client.goplus_chains={str(c['id']) for c in response.get('result',[])} if response.get('code')==1 else set()
    if network['chain_id'] not in client.goplus_chains:
        return {'source':'GoPlus','blocked':False,'complete':False,'unknown':['network_not_supported'],'risks':[]}
    data=client.request('https://api.gopluslabs.io/api/v1/token_security/'+network['chain_id']+'?contract_addresses='+asset['mint'])
    report=data.get('result',{}).get(asset['mint'].lower()) if data.get('code')==1 else None
    if not report:raise ValueError('No token security report')
    return parse_goplus(report,asset,client.config)


def parse_map(payload,security,asof_ms,config):
    unknown={'complete':False,'blocked':False,'status':'unknown','largest_cluster_pct':None}
    stamp=number((payload.get('metadata') or {}).get('ts_update'))
    if stamp is None or asof_ms-stamp*1000>config['risk']['map_max_age_minutes']*60000 or stamp*1000>asof_ms+60000:
        return {**unknown,'reason':'map_timestamp_missing_or_stale'}
    supply=security.get('supply_normalized');nodes=(payload.get('nodes') or {}).get('top_holders') or []
    if not supply or supply<=0 or not nodes:return {**unknown,'reason':'cannot_verify_map_share_units'}
    # The schema omits units for `share`; verify with amounts and independent supply.
    checks=[]
    for node in nodes:
        holder=node.get('holder_data') or {};amount=number(holder.get('amount'));share=number(holder.get('share'))
        if amount is not None and share is not None and amount>0 and share>0:checks.append((amount/supply*100,share))
    possible=[factor for factor in (1.,100.) if len(checks)>=2 and all(abs(p-s*factor)<=max(.001,p*.02) for p,s in checks)]
    if len(possible)!=1:return {**unknown,'reason':'map_share_units_not_uniquely_verified'}
    factor=possible[0];excluded=set(security.get('excluded_known_accounts',[]));holders=[]
    normalized=lambda value:address_key('solana' if not str(value).startswith('0x') else 'evm',value)
    for node in nodes:
        details=node.get('address_details') or {};address=node.get('address')
        if not address:continue
        if details.get('is_dex') or details.get('is_cex'):excluded.add(normalized(address));continue
        share=number((node.get('holder_data') or {}).get('share'))
        if share is not None:holders.append({'address':address,'pct':share*factor})
    largest=0.;found=False
    returned={h['address'] for h in holders}|{node.get('address') for node in nodes}
    for cluster in payload.get('clusters') or []:
        members=cluster.get('holders') or []
        if any(member not in returned for member in members):return {**unknown,'reason':'cluster_contains_unreturned_holders'}
        shares=[h['pct'] for h in holders if h['address'] in members and normalized(h['address']) not in excluded]
        if shares:largest=max(largest,sum(shares));found=True
    if payload.get('clusters') is None:return {**unknown,'reason':'clusters_not_returned'}
    concentration_info=concentration(holders,excluded,'solana' if not str(nodes[0].get('address','')).startswith('0x') else 'evm',config)
    blocked=largest>config['risk']['largest_connected_cluster_max_pct'] or concentration_info['holder_concentration_blocked']
    return {'complete':concentration_info['holder_concentration_complete'],'blocked':blocked,
        'status':'provider_connected_wallet_map','largest_cluster_pct':largest if found else 0.,
        'source':'Bubblemaps','asof_ms':int(stamp*1000),'share_unit_crosschecked':True,
        'note':'Transfer connections do not prove common ownership.',**concentration_info}


def fetch_map(client,asset,security,asof_ms,network):
    if client.config['risk'].get('wallet_map_mode')=='manual':
        return {'complete':False,'blocked':False,'status':'manual_review_required',
                'reason':'User performs wallet-map review; no automatic approval inferred.'}
    key=os.environ.get('BUBBLEMAPS_API_KEY')
    if not key:return {'complete':False,'blocked':False,'status':'unknown','reason':'BUBBLEMAPS_API_KEY_not_configured'}
    chain='eth' if asset['chain']=='ethereum' else ('bsc' if asset['chain']=='bnb' else asset['chain'])
    payload=client.request('https://api.bubblemaps.io/v0/tokens/map/'+chain+'/'+asset['mint']+'?limit=80&return_nodes=true&return_clusters=true',headers={'X-ApiKey':key})
    return parse_map(payload,security,asof_ms,client.config)


def developer_evm(client,network,asset,creator,asof_ms):
    url=os.environ.get('MEME_RPC_'+asset['chain'].upper()) or network['rpc']
    if int(client.rpc(url,'eth_chainId',[]),16)!=int(network['chain_id']):raise ValueError('Wrong RPC network')
    if client.rpc(url,'eth_getCode',[creator,'latest']) not in ('0x','0x0'):
        return {'status':'unknown','reason':'reported_creator_is_a_contract_not_verified_developer'}
    tip=int(client.rpc(url,'eth_blockNumber',[]),16)
    block=client.rpc(url,'eth_getBlockByNumber',[hex(tip),False]);end=int(block['timestamp'],16)*1000
    if end>asof_ms+60000 or asof_ms-end>120000:raise ValueError('RPC block is stale')
    start=end-client.config['risk']['developer_transfer_window_minutes']*60000
    size=client.config['risk']['rpc_log_page_blocks'];maximum=client.config['risk']['rpc_log_max_pages']
    lower=tip
    for _ in range(maximum):
        lower=max(0,lower-size)
        older=client.rpc(url,'eth_getBlockByNumber',[hex(lower),False])
        if int(older['timestamp'],16)*1000<=start:break
    else:return {'status':'unknown','reason':'developer_history_range_budget_exceeded'}
    creator_topic='0x'+creator.lower().removeprefix('0x').zfill(64)
    for first in range(lower,tip+1,size):
        logs=client.rpc(url,'eth_getLogs',[{'address':asset['mint'],'fromBlock':hex(first),'toBlock':hex(min(tip,first+size-1)),
                           'topics':[TRANSFER,creator_topic]}])
        if not isinstance(logs,list):raise ValueError('Invalid log result')
        for log in logs:
            if log.get('removed'):return {'status':'unknown','reason':'removed_chain_log'}
            if log.get('address','').lower()!=asset['mint'].lower() or len(log.get('topics',[]))<3:raise ValueError('Unexpected transfer log')
            if int(log.get('data','0x0'),16)<=0:continue
            stamp=int(client.rpc(url,'eth_getBlockByNumber',[log['blockNumber'],False])['timestamp'],16)*1000
            if stamp>=start:
                return {'status':'outgoing_transfer_detected','window_start_ms':start,'window_end_ms':end,
                        'transaction':log.get('transactionHash'),'note':'Transfer detected; not automatically classified as a sale.'}
    return {'status':'no_outgoing_transfers_in_complete_window','window_start_ms':start,'window_end_ms':end,
            'note':'Reported creator only; not lifetime no-sale proof or coverage of related wallets.'}


def developer_solana(client,asset,creator,asof_ms):
    url=os.environ.get('MEME_RPC_SOLANA') or 'https://api.mainnet-beta.solana.com'
    start=asof_ms-client.config['risk']['developer_transfer_window_minutes']*60000
    cap=client.config['risk']['solana_signature_limit']
    accounts=client.rpc(url,'getTokenAccountsByOwner',[creator,{'mint':asset['mint']},{'encoding':'jsonParsed','commitment':'confirmed'}])
    values=accounts.get('value',[])
    if len(values)>4:return {'status':'unknown','reason':'too_many_creator_token_accounts_for_complete_check'}
    addresses=[creator]
    for account in values:
        info=account['account']['data']['parsed']['info']
        if info.get('delegate'):return {'status':'unknown','reason':'delegated_token_account'}
        addresses.append(account['pubkey'])
    signatures={}
    for address in addresses:
        rows=client.rpc(url,'getSignaturesForAddress',[address,{'limit':cap,'commitment':'confirmed'}])
        if any(r.get('blockTime') is None for r in rows):return {'status':'unknown','reason':'transaction_time_missing'}
        if len(rows)==cap and rows[-1]['blockTime']*1000>=start:return {'status':'unknown','reason':'developer_history_truncated'}
        for record in rows:
            if record['blockTime']*1000>=start and record.get('err') is None:signatures[record['signature']]=record
    if len(signatures)>cap:return {'status':'unknown','reason':'developer_transaction_budget_exceeded'}
    for signature in signatures:
        tx=client.rpc(url,'getTransaction',[signature,{'encoding':'jsonParsed','maxSupportedTransactionVersion':0,'commitment':'confirmed'}])
        if not tx or tx.get('meta') is None:return {'status':'unknown','reason':'transaction_body_missing'}
        meta=tx['meta']
        if meta.get('err') is not None:continue
        if 'preTokenBalances' not in meta or 'postTokenBalances' not in meta:return {'status':'unknown','reason':'token_balances_missing'}
        before={r['accountIndex']:r for r in meta['preTokenBalances'] if r.get('mint')==asset['mint'] and r.get('owner')==creator}
        after={r['accountIndex']:r for r in meta['postTokenBalances'] if r.get('mint')==asset['mint'] and r.get('owner')==creator}
        for index,balance in before.items():
            old=int(balance['uiTokenAmount']['amount']);new=int(after.get(index,{}).get('uiTokenAmount',{}).get('amount','0'))
            if new<old:
                return {'status':'outgoing_transfer_detected','window_start_ms':start,'window_end_ms':asof_ms,
                    'transaction':signature,'note':'Account decrease or closure, including possible transfers; not asserted to be a sale.'}
    return {'status':'no_outgoing_transfers_in_complete_window','window_start_ms':start,'window_end_ms':asof_ms,
            'note':'Reported creator and current token accounts; not lifetime no-sale proof or linked-wallet coverage.'}


def developer_check(client,network,asset,security,asof_ms):
    creator=security.get('creator')
    if not valid_address(asset['chain'],creator) or address_key(asset['chain'],creator) in BURN:
        return {'status':'unknown','reason':'creator_identity_not_available'}
    percentage=security.get('creator_pct')
    if percentage is None or percentage<=0:return {'status':'unknown','reason':'creator_positive_holdings_not_verified'}
    result=developer_solana(client,asset,creator,asof_ms) if asset['chain']=='solana' else developer_evm(client,network,asset,creator,asof_ms)
    return {**result,'creator':creator,'identity_source':'provider_reported_creator','creator_pct':percentage}
