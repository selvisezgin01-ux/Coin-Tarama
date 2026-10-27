"""Fixed public GET endpoints only. Venue failures stay separate; no accounts/orders."""
import json, math, re, time
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError


def num(value):
    if isinstance(value,bool):return None
    try:
        value=float(value)
        return value if math.isfinite(value) else None
    except (ValueError,TypeError):return None


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None


class Public:
    def __init__(self,venue):
        if venue not in ('MEXC','OKX'):raise ValueError('Unknown venue')
        self.venue=venue;self.last=0.;self.blocked=False;self.calls=0
        self.opener=build_opener(NoRedirect())

    def get(self,kind,symbol=None):
        if self.blocked:raise RuntimeError(self.venue+': public requests stopped after rate/access error')
        if self.venue=='MEXC':
            root='https://contract.mexc.com/api/v1/contract/'
            paths={'catalog':'detail/country','ticker':'ticker','funding':'funding_rate/'+(symbol or '')}
            if symbol is not None and not re.fullmatch(r'[A-Z0-9]+_USDT',symbol):raise ValueError('Invalid contract ID')
            if kind not in paths:raise ValueError('Not a public endpoint')
            url=root+paths[kind]
        else:
            root='https://www.okx.com/api/v5/'
            paths={'catalog':'public/instruments','ticker':'market/tickers','oi':'public/open-interest','funding':'public/funding-rate'}
            if symbol is not None and not re.fullmatch(r'[A-Z0-9]+-USDT-SWAP',symbol):raise ValueError('Invalid swap ID')
            if kind not in paths:raise ValueError('Not a public endpoint')
            url=root+paths[kind]+'?'+urlencode({'instId':symbol} if kind=='funding' else {'instType':'SWAP'})
        delay=max(0.,self.last+.25-time.monotonic())
        if delay:time.sleep(delay)
        self.last=time.monotonic();self.calls+=1
        try:
            with self.opener.open(Request(url,headers={'User-Agent':'Shortcu-Kistir/1','Accept':'application/json'}),timeout=18) as response:data=json.load(response)
        except HTTPError as exc:
            if exc.code in (401,403,418,429):self.blocked=True
            raise RuntimeError(self.venue+': public HTTP '+str(exc.code)) from None
        except Exception:raise RuntimeError(self.venue+': public connection/response error') from None
        if self.venue=='MEXC':
            if data.get('success') is not True or data.get('code')!=0:raise ValueError('MEXC public response rejected')
        elif data.get('code')!='0':raise ValueError('OKX public response rejected')
        return data['data']


def catalog(rows,venue):
    if not isinstance(rows,list):raise ValueError('Unexpected contract catalog')
    result={}
    for row in rows:
        if venue=='MEXC':
            if row.get('state')!=0 or row.get('futureType')!=1 or row.get('quoteCoin')!='USDT' or row.get('settleCoin')!='USDT':continue
            base=row.get('baseCoin');identifier=row.get('symbol');size=num(row.get('contractSize'))
            if not isinstance(base,str) or identifier!=base+'_USDT' or not re.fullmatch(r'[A-Z0-9]+',base):continue
        else:
            if row.get('state')!='live' or row.get('instType')!='SWAP' or row.get('ctType')!='linear' or row.get('settleCcy')!='USDT':continue
            identifier=row.get('instId','')
            if not re.fullmatch(r'[A-Z0-9]+-USDT-SWAP',identifier):continue
            base=identifier.split('-')[0]
            if row.get('ctValCcy')!=base:continue
            value=num(row.get('ctVal'));mult=num(row.get('ctMult'))
            size=value*mult if value is not None and mult is not None else None
        if size is None or size<=0:continue
        symbol=base+'USDT'
        if symbol in result:raise ValueError('Ambiguous contract identity')
        result[symbol]={'symbol':symbol,'contract':identifier,'base':base,'contract_size':size,
                        'identity_scope':'exact exchange base ID; cross-venue contract authenticity not independently verified'}
    return result


def recent(stamp,asof,minutes=5):
    value=num(stamp)
    return value is not None and -60000<=asof-value<=minutes*60000


def markets(client,asof):
    venue=client.venue;instruments=catalog(client.get('catalog'),venue)
    client.instruments=instruments
    if not instruments:raise ValueError('No verified active perpetual metadata available')
    ticks=client.get('ticker')
    if not isinstance(ticks,list):raise ValueError('Unexpected futures tickers')
    ticker_map={r.get('symbol' if venue=='MEXC' else 'instId'):r for r in ticks}
    interests={} if venue=='MEXC' else client.get('oi')
    if venue=='OKX' and not isinstance(interests,list):raise ValueError('Unexpected open interest')
    oi_map={} if venue=='MEXC' else {r.get('instId'):r for r in interests}
    result={}
    for symbol,meta in instruments.items():
        try:
            tick=ticker_map[meta['contract']]
            bid=num(tick.get('bid1' if venue=='MEXC' else 'bidPx'));ask=num(tick.get('ask1' if venue=='MEXC' else 'askPx'))
            if bid is None or ask is None or not 0<bid<=ask:continue
            price=(bid+ask)/2;tick_stamp=num(tick.get('timestamp' if venue=='MEXC' else 'ts'))
            interest=tick if venue=='MEXC' else oi_map[meta['contract']]
            oi=num(interest.get('holdVol' if venue=='MEXC' else 'oi'))
            stamp=num(interest.get('timestamp' if venue=='MEXC' else 'ts'))
            if oi is None or oi<=0 or not recent(stamp,asof()) or not recent(tick_stamp,asof()):continue
            notional=num(interest.get('oiUsd')) if venue=='OKX' else oi*meta['contract_size']*price
            if notional is None or notional<=0:continue
            result[symbol]={**meta,'venue':venue,'observed_ms':int(stamp),'retrieved_ms':asof(),
                'price_ms':int(tick_stamp),'mid_price':price,'spread_pct':(ask-bid)/price*100,
                'oi_contracts':oi,'oi_notional':notional,
                'notional_kind':'provider_USD' if venue=='OKX' else 'estimated_USDT_at_current_mid'}
        except (KeyError,ValueError,TypeError):continue
    return result


def funding(client,market,asof):
    rows=client.get('funding',market['contract'])
    if client.venue=='OKX':
        if not isinstance(rows,list) or len(rows)!=1:raise ValueError('Unexpected funding response')
        row=rows[0]
        if row.get('instId')!=market['contract']:raise ValueError('Funding contract mismatch')
        end=num(row.get('fundingTime'));start=num(row.get('prevFundingTime'));stamp=num(row.get('ts'))
        hours=(end-start)/3600000 if end is not None and start is not None else None
    else:
        row=rows
        if not isinstance(row,dict) or row.get('symbol')!=market['contract']:raise ValueError('Funding contract mismatch')
        hours=num(row.get('collectCycle'));end=num(row.get('nextSettleTime'));stamp=num(row.get('timestamp'))
    rate=num(row.get('fundingRate'))
    if rate is None or not -1<rate<1 or hours is None or not 0<hours<=24 or end is None or not recent(stamp,asof()):raise ValueError('Funding data missing/stale/invalid')
    if not -60000<=end-asof()<=hours*3600000+60000:raise ValueError('Funding settlement interval inconsistent')
    return {'rate':rate,'interval_hours':hours,'scaled_8h_rate':rate*8/hours,'observed_ms':int(stamp),
            'settlement_ms':int(end),'meaning':'current indicative rate, not a settled payment or future funding guarantee'}
