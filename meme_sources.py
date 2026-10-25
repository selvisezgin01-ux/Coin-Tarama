"""Documented public market-data adapters. Never follows token-provided URLs."""
from __future__ import annotations
from collections import defaultdict
from datetime import datetime
import json
import re
import threading
import time
from urllib.error import HTTPError,URLError
from urllib.parse import urlencode,urlsplit
from urllib.request import Request,build_opener,HTTPRedirectHandler

from meme_rules import address_key,number


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None


class Client:
    def __init__(self,config):
        self.config=config;self.lock=threading.Lock();self.last={};self.blocked=set();self.stats=defaultdict(int)
        self.opener=build_opener(NoRedirect())

    def request(self,url,payload=None,headers=None):
        host=urlsplit(url).hostname
        if urlsplit(url).scheme!='https':raise ValueError('Only HTTPS data endpoints are allowed')
        interval=6.5 if host=='api.geckoterminal.com' else (.35 if host=='api.dexscreener.com' else .5)
        if host=='api.geckoterminal.com':interval=self.config['discovery']['gecko_minimum_request_interval_seconds']
        with self.lock:
            if host in self.blocked:raise RuntimeError(f'{host}: provider stopped after access/rate error')
            delay=max(0.,self.last.get(host,0.)+interval-time.monotonic())
            self.last[host]=time.monotonic()+delay
        if delay:time.sleep(delay)
        with self.lock:
            if host in self.blocked:raise RuntimeError(f'{host}: queued request stopped after access/rate error')
        request=Request(url,data=None if payload is None else json.dumps(payload).encode(),
                        headers={'User-Agent':'Coin-Tarama-Meme/1','Accept':'application/json','Content-Type':'application/json',**(headers or {})})
        try:
            with self.opener.open(request,timeout=self.config['discovery']['api_timeout_seconds']) as response:
                result=json.load(response)
            self.stats[host+':ok']+=1
            return result
        except HTTPError as error:
            self.stats[host+':error']+=1
            if error.code in (401,403,418,429):self.blocked.add(host)
            raise RuntimeError(f'{host}: HTTP {error.code}') from None
        except (URLError,OSError,ValueError):
            self.stats[host+':error']+=1
            raise RuntimeError(f'{host}: data connection or response error') from None

    def gecko(self,path):return self.request('https://api.geckoterminal.com/api/v2/'+path)
    def dex(self,path):return self.request('https://api.dexscreener.com/'+path)

    def rpc(self,url,method,params):
        allowed={'eth_chainId','eth_blockNumber','eth_getBlockByNumber','eth_getLogs','eth_getCode',
                 'getSignaturesForAddress','getTransaction','getTokenAccountsByOwner'}
        if method not in allowed:raise ValueError('RPC method is not a permitted public read')
        result=self.request(url,{'jsonrpc':'2.0','id':1,'method':method,'params':params})
        if result.get('error'):raise RuntimeError('Read-only RPC method unavailable or limited')
        if 'result' not in result:raise ValueError('Invalid RPC response')
        return result['result']


def valid_address(chain,value,pool=False):
    if not isinstance(value,str):return False
    if chain=='solana':return re.fullmatch(r'[1-9A-HJ-NP-Za-km-z]{32,44}',value) is not None
    return re.fullmatch(r'0x[0-9a-fA-F]{40}'+(r'(?:[0-9a-fA-F]{24})?' if pool else ''),value) is not None


def ms_iso(value):
    if not isinstance(value,str):return None
    try:return int(datetime.fromisoformat(value.replace('Z','+00:00')).timestamp()*1000)
    except ValueError:return None


def normalize_pool(chain,pool,included=None):
    a=pool['attributes'];relations=pool['relationships']
    mint=relations['base_token']['data']['id'].split('_',1)[1]
    pair=a['address']
    if not valid_address(chain,mint) or not valid_address(chain,pair,True):raise ValueError('Invalid provider address')
    meta=(included or {}).get(relations['base_token']['data']['id'],{})
    symbol=meta.get('symbol',a.get('name','?').split(' / ')[0])
    # A base quote asset is not interpreted as the meme on the opposite side.
    if str(symbol).upper() in {'WETH','ETH','WSOL','SOL','USDC','USDT','WBNB','BNB','WHYPE','HYPE','USDG','DAI','WBTC','CBBTC'}:
        raise ValueError('Base token is a quote asset; orientation not supported')
    transactions=a.get('transactions',{}).get('m15',{})
    return {'chain':chain,'mint':address_key(chain,mint),'pool':address_key(chain,pair),
        'price_observed_ms':int(time.time()*1000),
        'symbol':str(symbol)[:40],'dex':relations.get('dex',{}).get('data',{}).get('id','unknown'),
        'price_usd':number(a.get('base_token_price_usd')),'liquidity_usd':number(a.get('reserve_in_usd')),
        'market_cap_usd':number(a.get('market_cap_usd')),'fdv_usd':number(a.get('fdv_usd')),
        'pool_created_ms':ms_iso(a.get('pool_created_at')),'volume15_usd':number(a.get('volume_usd',{}).get('m15')),
        'buys15':number(transactions.get('buys')),'sells15':number(transactions.get('sells')),
        'source':'geckoterminal','pool_age_is_token_age':False}


def discover(client,chain,network):
    rows=[];errors=[];coverage=[]
    paths=[f"networks/{network['gecko']}/new_pools?page={p}&include=base_token,quote_token" for p in range(1,client.config['discovery']['new_pool_pages_per_network']+1)]
    if client.config['discovery']['trending_pools_per_network']:
        paths.append(f"networks/{network['gecko']}/trending_pools?include=base_token,quote_token")
    for path in paths:
        try:
            payload=client.gecko(path)
            included={x['id']:x.get('attributes',{}) for x in payload.get('included',[])}
            coverage.append({'endpoint':path.split('?')[0],'returned':len(payload.get('data',[]))})
            for pool in payload.get('data',[]):
                try:rows.append(normalize_pool(chain,pool,included))
                except (ValueError,KeyError,TypeError):continue
        except Exception as exc:errors.append(str(exc))
    return rows,errors,coverage


def refresh_pools(client,chain,network,pools):
    if not pools:return []
    # The provider documents at most 30 pool addresses in a multi lookup.
    result=[]
    for start in range(0,len(pools),30):
        path=f"networks/{network['gecko']}/pools/multi/"+','.join(pools[start:start+30])+'?include=base_token,quote_token'
        data=client.gecko(path)
        included={x['id']:x.get('attributes',{}) for x in data.get('included',[])}
        for row in data.get('data',[]):
            try:result.append(normalize_pool(chain,row,included))
            except (ValueError,KeyError,TypeError):continue
    return result


def dex_enrich(client,chain,network,rows):
    by_mint={r['mint']:r for r in rows}
    addresses=list(by_mint)
    for start in range(0,len(addresses),30):
        payload=client.dex('tokens/v1/'+network['dex']+'/'+','.join(addresses[start:start+30]))
        if not isinstance(payload,list):raise ValueError('Unexpected DexScreener token response')
        for pair in payload:
            if pair.get('chainId')!=network['dex']:continue
            mint=address_key(chain,pair.get('baseToken',{}).get('address',''))
            if mint not in by_mint:continue
            row=by_mint[mint]
            if address_key(chain,pair.get('pairAddress',''))!=row['pool']:continue
            cap=number(pair.get('marketCap'));fdv=number(pair.get('fdv'))
            if cap is not None and cap>0:row['market_cap_usd']=cap
            if fdv is not None and fdv>0:row['fdv_usd']=fdv
            row['dexscreener_matched']=True
    return rows


def candles(client,network,asset,asof_ms):
    query=urlencode({'aggregate':15,'limit':100,'currency':'usd','token':asset['mint'],
                     'before_timestamp':asof_ms//1000,'include_empty_intervals':'false'})
    payload=client.gecko(f"networks/{network['gecko']}/pools/{asset['pool']}/ohlcv/minute?"+query)
    return payload['data']['attributes']['ohlcv_list']


def quote(client,network,asset):
    payload=client.dex('latest/dex/pairs/'+network['dex']+'/'+asset['pool'])
    observed=int(time.time()*1000)
    for row in payload.get('pairs') or []:
        if row.get('chainId')!=network['dex']:continue
        mint=address_key(asset['chain'],row.get('baseToken',{}).get('address',''))
        pair=address_key(asset['chain'],row.get('pairAddress',''))
        price=number(row.get('priceUsd'))
        if mint==asset['mint'] and pair==asset['pool'] and price is not None and price>0:
            return {'price_usd':price,'price_observed_ms':observed,'price_source':'dexscreener_matched_pool'}
    raise ValueError('Fresh token price could not be matched to exact chain, mint and pool')
