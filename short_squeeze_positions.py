"""Position-weighted public ratios, with explicit provider populations. No accounts/orders."""
import json,math,re,time
from urllib.parse import urlencode
from urllib.request import Request,build_opener,HTTPRedirectHandler
from urllib.error import HTTPError

SCOPES={
 'OKX': 'OKX: açık pozisyon değeri en büyük %5 yatırımcı, pozisyon büyüklüğü oranı',
 'BINANCE': 'Binance: teminat bakiyesi en büyük %20 yatırımcı, pozisyon büyüklüğü oranı'}


def num(v):
    if isinstance(v,bool):return None
    try:
        v=float(v);return v if math.isfinite(v) else None
    except (ValueError,TypeError):return None


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None


class Client:
    def __init__(self,provider):
        if provider not in SCOPES:raise ValueError('Unknown position provider')
        self.provider=provider;self.blocked=False;self.last=0.;self.catalog=None;self.calls=0
        self.opener=build_opener(NoRedirect())

    def get(self,kind,symbol=None):
        if self.blocked:raise RuntimeError(self.provider+': public requests stopped after access/rate error')
        if kind not in ('catalog','ratio'):raise ValueError('Only public catalog/position ratio reads allowed')
        if kind=='ratio' and (not isinstance(symbol,str) or not re.fullmatch(r'[A-Z0-9]+USDT',symbol)):raise ValueError('Invalid exact symbol')
        if self.provider=='OKX':
            url='https://www.okx.com/api/v5/'
            url+=('public/instruments?instType=SWAP' if kind=='catalog' else
                'rubik/stat/contracts/long-short-position-ratio-contract-top-trader?'+urlencode({'instId':symbol[:-4]+'-USDT-SWAP','period':'5m','limit':3}))
        else:
            url='https://fapi.binance.com/'
            url+=('fapi/v1/exchangeInfo' if kind=='catalog' else 'futures/data/topLongShortPositionRatio?'+urlencode({'symbol':symbol,'period':'5m','limit':3}))
        delay=max(0.,self.last+.5-time.monotonic())
        if delay:time.sleep(delay)
        self.last=time.monotonic();self.calls+=1
        try:
            with self.opener.open(Request(url,headers={'User-Agent':'Shortcu-position-monitor/1','Accept':'application/json'}),timeout=15) as r:data=json.load(r)
        except HTTPError as e:
            if e.code in (401,403,418,429,451):self.blocked=True
            raise RuntimeError(self.provider+': public HTTP '+str(e.code)) from None
        except Exception:raise RuntimeError(self.provider+': public connection/response error') from None
        if isinstance(data,dict) and self.provider=='BINANCE' and positions_error(data):
            if data.get('code') in (-2014,-2015,-1003):self.blocked=True
            raise RuntimeError('Binance public data rejected; no auth or regional workaround attempted')
        if isinstance(data,dict) and self.provider=='OKX' and data.get('code') not in (None,'0'):
            if data.get('code') in ('50011','50040','50111','50113','50114'):self.blocked=True
            raise RuntimeError('OKX public data rejected')
        return data

    def instruments(self):
        if self.catalog is not None:return self.catalog
        data=self.get('catalog');result={}
        if self.provider=='OKX':
            if not isinstance(data,dict) or data.get('code')!='0' or not isinstance(data.get('data'),list):raise ValueError('Unexpected OKX catalog')
            for r in data['data']:
                identifier=r.get('instId','')
                if r.get('state')!='live' or r.get('ctType')!='linear' or r.get('settleCcy')!='USDT' or not re.fullmatch(r'[A-Z0-9]+-USDT-SWAP',identifier):continue
                base=identifier.split('-')[0]
                if r.get('ctValCcy')!=base:continue
                result[base+'USDT']=identifier
        else:
            if not isinstance(data,dict) or not isinstance(data.get('symbols'),list):raise ValueError('Unexpected Binance catalog')
            for r in data['symbols']:
                base=r.get('baseAsset');symbol=r.get('symbol')
                if r.get('status')!='TRADING' or r.get('contractType')!='PERPETUAL' or r.get('quoteAsset')!='USDT' or r.get('marginAsset')!='USDT':continue
                if not isinstance(base,str) or symbol!=base+'USDT' or not re.fullmatch(r'[A-Z0-9]+USDT',symbol):continue
                result[symbol]=symbol
        self.catalog=result;return result

    def read(self,symbol,stamp,cfg):
        try:
            if symbol not in self.instruments():return {'status':'unsupported','reason':'exact active USDT perpetual unavailable','provider':self.provider,'scope':SCOPES[self.provider]}
            return parse(self.provider,symbol,self.get('ratio',symbol),stamp(),cfg)
        except Exception as e:return {'status':'unknown','reason':str(e),'provider':self.provider,'scope':SCOPES[self.provider]}


def parse(provider,symbol,payload,stamp,cfg):
    if provider not in SCOPES:raise ValueError('Unknown provider scope')
    if provider=='OKX':
        if not isinstance(payload,dict) or payload.get('code')!='0':raise ValueError('OKX ratio response rejected')
        rows=payload.get('data')
    else:rows=payload
    if not isinstance(rows,list) or not rows:raise ValueError('Position data missing')
    output={}
    for raw in rows:
        if provider=='OKX':
            if not isinstance(raw,list) or len(raw)!=2:raise ValueError('Unexpected position ratio row')
            ts,ratio=map(num,raw)
        else:
            if not isinstance(raw,dict) or raw.get('symbol')!=symbol:raise ValueError('Position symbol mismatch')
            ts=num(raw.get('timestamp'));ratio=num(raw.get('longShortRatio'))
        if ts is None or ts!=int(ts) or int(ts)%300000 or ratio is None or ratio<0:raise ValueError('Invalid position ratio/time')
        ts=int(ts)
        if ts>stamp:continue
        short=100/(1+ratio);long=100-short
        if provider=='BINANCE':
            # The API keeps historical field names longAccount/shortAccount even
            # on the POSITIONS endpoint. Endpoint semantics, not names, set scope.
            lp=num(raw.get('longAccount'));sp=num(raw.get('shortAccount'))
            if lp is None or sp is None or not 0<=lp<=1 or not 0<=sp<=1 or abs(lp+sp-1)>.001:
                raise ValueError('Invalid position share fields')
            if abs(long-lp*100)>.1 or abs(short-sp*100)>.1:raise ValueError('Position ratio/share inconsistency')
        point={'status':'observed','provider':provider,'scope':SCOPES[provider],'symbol':symbol,
            'contract':symbol[:-4]+'-USDT-SWAP' if provider=='OKX' else symbol,'period':'5m',
            'ratio_long_over_short':ratio,'long_pct':long,'short_pct':short,'provider_ms':ts,'observed_ms':stamp,
            'is_market_wide':False,'is_account_count':False}
        if ts in output and output[ts]['ratio_long_over_short']!=ratio:raise ValueError('Conflicting ratio timestamp')
        output[ts]=point
    if not output:raise ValueError('No nonfuture ratio observation')
    point=output[max(output)]
    if stamp-point['provider_ms']>cfg['max_provider_age_minutes']*60000:raise ValueError('Position ratio is stale')
    return point


def change(previous,current):
    if (previous['provider'],previous['symbol'],previous['scope'],previous['period'])!=(current['provider'],current['symbol'],current['scope'],current['period']):raise ValueError('Cannot compare different position populations')
    if current['provider_ms']<=previous['provider_ms']:raise ValueError('No new provider period')
    points=current['short_pct']-previous['short_pct']
    relative=points/previous['short_pct']*100 if previous['short_pct']>0 else None
    if relative is not None and not math.isfinite(relative):relative=None
    crossing=(previous['short_pct']<50<=current['short_pct']) or (previous['short_pct']>50>=current['short_pct'])
    return {'short_change_pp':points,'short_relative_change_pct':relative,
            'elapsed_minutes':(current['provider_ms']-previous['provider_ms'])/60000,'crosses_50':crossing}


def meaningful(delta,cfg):
    return abs(delta['short_change_pp'])+1e-9>=cfg['minimum_short_change_percentage_points'] or (cfg['notify_crossing_50_percent'] and delta['crosses_50'])


def positions_error(data):
    value=data.get('code')
    return isinstance(value,(int,float)) and value<0
