"""Public spot candles/books + existing audited futures and scoped ratio readers."""
import json,re,time
from urllib.request import Request,build_opener
from urllib.error import HTTPError
from urllib.parse import urlencode
from short_squeeze_positions import NoRedirect,num
from short_squeeze_sources import recent

STEPS={'15m':900000,'1h':3600000,'4h':14400000}

class Spot:
    def __init__(self,venue):
        if venue not in ('MEXC','OKX'):raise ValueError('Unsupported spot venue')
        self.venue=venue;self.calls=0;self.blocked=False;self.last=0
        self.opener=build_opener(NoRedirect())

    def get(self,kind,symbol=None,interval=None):
        if self.blocked:raise RuntimeError(self.venue+': stopped after public access/rate error')
        if kind not in ('catalog','tickers','book','candles'):raise ValueError('Public market endpoints only')
        if symbol is not None and not re.fullmatch(r'[A-Z0-9]+USDT',symbol):raise ValueError('Invalid spot symbol')
        if kind=='candles' and interval not in STEPS:raise ValueError('Unsupported timeframe')
        if self.venue=='MEXC':
            query={'catalog':'exchangeInfo','tickers':'ticker/24hr','book':'ticker/bookTicker',
                   'candles':'klines'}.get(kind)
            params={} if symbol is None else {'symbol':symbol}
            if kind=='candles':params.update(interval='60m' if interval=='1h' else interval,limit=100)
            url='https://api.mexc.com/api/v3/'+query+('?' + urlencode(params) if params else '')
        else:
            paths={'catalog':'public/instruments','tickers':'market/tickers','book':'market/ticker','candles':'market/candles'}
            params={'instType':'SPOT'} if kind in ('catalog','tickers') else {'instId':symbol[:-4]+'-USDT'}
            if kind=='candles':params.update(bar={'15m':'15m','1h':'1H','4h':'4H'}[interval],limit=100)
            url='https://www.okx.com/api/v5/'+paths[kind]+'?'+urlencode(params)
        time.sleep(max(0,self.last+.3-time.monotonic()));self.last=time.monotonic();self.calls+=1
        for attempt in range(2):
            try:
                with self.opener.open(Request(url,headers={'User-Agent':'Coin-Tarama-5/1','Accept':'application/json'}),timeout=15) as r:data=json.load(r)
                break
            except HTTPError as e:
                if e.code in (401,403,418,429,451):self.blocked=True
                raise RuntimeError(self.venue+': public HTTP '+str(e.code)) from None
            except OSError:
                if attempt:raise RuntimeError(self.venue+': public connection unavailable') from None
                time.sleep(1)
        if self.venue=='OKX':
            if data.get('code')!='0':
                if data.get('code') in ('50011','50040'):self.blocked=True
                raise ValueError('OKX public response rejected')
            return data['data']
        return data

    def book(self,symbol,now):
        raw=self.get('book',symbol)
        now=int(time.time()*1000)
        if self.venue=='OKX':
            if not isinstance(raw,list) or len(raw)!=1 or raw[0].get('instId')!=symbol[:-4]+'-USDT':raise ValueError('Spot identity mismatch')
            raw=raw[0];bid=num(raw.get('bidPx'));ask=num(raw.get('askPx'));ts=num(raw.get('ts'))
        else:
            if not isinstance(raw,dict) or raw.get('symbol')!=symbol:raise ValueError('Spot identity mismatch')
            bid=num(raw.get('bidPrice'));ask=num(raw.get('askPrice'));ts=now
        if bid is None or ask is None or not 0<bid<=ask or not recent(ts,now,2):raise ValueError('Invalid or stale spot book')
        price=(bid+ask)/2
        return {'price':price,'spread_pct':(ask-bid)/price*100,'observed_ms':now,'provider_ms':int(ts),
                'timestamp_kind':'provider' if self.venue=='OKX' else 'local_public_response_observation'}

def universe(client,futures,cfg,exclusions):
    catalog=client.get('catalog');ticks=client.get('tickers');allowed=set()
    items=catalog.get('symbols',[]) if client.venue=='MEXC' else catalog
    for r in items:
        if client.venue=='MEXC':
            symbol=r.get('symbol','');base=r.get('baseAsset','')
            if r.get('quoteAsset')!='USDT' or str(r.get('status')) not in ('1','ENABLED','TRADING'):continue
            if set(r.get('conceptPlates',[])) & set(exclusions['plates']):continue
        else:
            identity=r.get('instId','')
            if not re.fullmatch(r'[A-Z0-9]+-USDT',identity) or r.get('state')!='live':continue
            symbol=identity.replace('-','');base=r.get('baseCcy','')
        if not re.fullmatch(r'[A-Z0-9]+USDT',symbol) or re.search(r'[235][LS]$',base):continue
        if base in exclusions['stable'] or base in exclusions['equity'].get(client.venue,[]):continue
        allowed.add(symbol)
    ranked=[]
    for r in ticks:
        symbol=r.get('symbol','') if client.venue=='MEXC' else r.get('instId','').replace('-','')
        vol=num(r.get('quoteVolume' if client.venue=='MEXC' else 'volCcy24h'))
        # OKX SPOT volCcy24h is quote currency; future tick volume is not used here.
        if symbol in allowed and symbol in futures and vol is not None and vol>=cfg['minimum_spot_volume24']:
            m=futures[symbol]
            if m['oi_notional']>=cfg['minimum_oi_notional'] and m['spread_pct']<=cfg['maximum_spread_pct']:
                ranked.append({'symbol':symbol,'volume24':vol})
    ranked.sort(key=lambda r:(-r['volume24'],r['symbol']))
    return ranked[:cfg['universe_per_venue']],{'active_spot':len(allowed),'liquid_spot_perpetual':len(ranked),'bounded_universe':min(len(ranked),cfg['universe_per_venue'])}

def closed_bars(raw,venue,interval,stamp,count):
    step=STEPS[interval];rows={}
    if not isinstance(raw,list):raise ValueError('Invalid candle response')
    for r in raw:
        if len(r)<8 or (venue=='OKX' and (len(r)!=9 or str(r[8])!='1')):continue
        ts=num(r[0])
        if ts is None or ts!=int(ts) or int(ts)%step:raise ValueError('Candle off grid')
        ts=int(ts)
        if ts+step>stamp:continue
        o,h,l,c,v,q=[num(r[i]) for i in (1,2,3,4,5,7)]
        if any(x is None for x in (o,h,l,c,v,q)) or min(o,h,l,c)<=0 or min(v,q)<0 or h<max(o,l,c) or l>min(o,h,c):raise ValueError('Invalid OHLCV')
        bar={'t':ts,'o':o,'h':h,'l':l,'c':c,'v':q}
        if ts in rows and rows[ts]!=bar:raise ValueError('Conflicting candle')
        rows[ts]=bar
    expected=stamp//step*step-step;series=[rows[k] for k in sorted(rows)][-count:]
    if len(series)<count or series[-1]['t']!=expected:raise ValueError('Insufficient or stale closed candle history')
    if any(b['t']-a['t']!=step for a,b in zip(series,series[1:])):raise ValueError('Candle history gap')
    return series

def bars(client,symbol,interval,stamp,cfg,cache):
    key=client.venue+':'+symbol+':'+interval;cutoff=stamp//STEPS[interval]*STEPS[interval]
    old=cache.get(key)
    if old and old['cutoff']==cutoff:return old['bars']
    series=closed_bars(client.get('candles',symbol,interval),client.venue,interval,stamp,cfg['bars_per_timeframe'])
    cache[key]={'cutoff':cutoff,'bars':series};return series
