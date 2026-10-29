"""Exact public SPOT/PERP identities and candles. No private endpoints or orders."""
import json,re,time,math
from urllib.request import Request,build_opener
from urllib.parse import urlencode
from urllib.error import HTTPError
from pathlib import Path
from short_squeeze_positions import NoRedirect,num
from short_squeeze_sources import catalog
STEPS={'15m':900000,'1h':3600000,'4h':14400000,'1m':60000}
ROOT=Path(__file__).parent

class Public:
    def __init__(self,venue,kind):
        if venue not in ('MEXC','OKX') or kind not in ('SPOT','PERP'):raise ValueError('Unknown market')
        self.venue=venue;self.kind=kind;self.calls=0;self.blocked=False;self.last=0
        self.opener=build_opener(NoRedirect())
    def get(self,which,contract=None,interval=None,start=None,end=None):
        if self.blocked:raise RuntimeError('Provider blocked for this cycle')
        if which not in ('catalog','tickers','candles'):raise ValueError('Public reads only')
        if which=='candles' and (interval not in STEPS or not re.fullmatch(r'[A-Z0-9]+(?:_USDT|-USDT(?:-SWAP)?|USDT)',contract or '')):raise ValueError('Invalid exact candle identity')
        if self.venue=='OKX':
            path={'catalog':'public/instruments','tickers':'market/tickers','candles':'market/history-candles' if end is not None else 'market/candles'}[which]
            params={'instType':'SPOT' if self.kind=='SPOT' else 'SWAP'} if which!='candles' else {
                'instId':contract,'bar':{'15m':'15m','1h':'1H','4h':'4H','1m':'1m'}[interval],'limit':100}
            if which=='candles' and end is not None:params['after']=int(end)
            url='https://www.okx.com/api/v5/'+path+'?'+urlencode(params)
        elif self.kind=='SPOT':
            path={'catalog':'exchangeInfo','tickers':'ticker/24hr','candles':'klines'}[which]
            params={} if which!='candles' else {'symbol':contract,'interval':'60m' if interval=='1h' else interval,'limit':100}
            if which=='candles' and start is not None:params.update(startTime=int(start),endTime=int(end)-1,limit=1000)
            url='https://api.mexc.com/api/v3/'+path+('?' +urlencode(params) if params else '')
        else:
            path={'catalog':'detail/country','tickers':'ticker','candles':'kline/'+(contract or '')}[which]
            params={}
            if which=='candles':
                step=STEPS[interval];stamp=int(time.time()*1000)
                params={'interval':{'15m':'Min15','1h':'Min60','4h':'Hour4','1m':'Min1'}[interval],
                    'start':int((start if start is not None else stamp-100*step)/1000),
                    'end':int((end if end is not None else stamp)/1000)}
            url='https://contract.mexc.com/api/v1/contract/'+path+('?' +urlencode(params) if params else '')
        time.sleep(max(0,self.last+.34-time.monotonic()));self.last=time.monotonic();self.calls+=1
        try:
            with self.opener.open(Request(url,headers={'User-Agent':'Coin-Tarama-5-V3/1','Accept':'application/json'}),timeout=12) as r:data=json.load(r)
        except HTTPError as e:
            if e.code in (401,403,418,429,451):self.blocked=True
            raise RuntimeError(self.venue+' '+self.kind+' public HTTP '+str(e.code)) from None
        except Exception:raise RuntimeError(self.venue+' '+self.kind+' public connection/response error') from None
        if self.venue=='OKX':
            if not isinstance(data,dict) or data.get('code')!='0':raise ValueError('OKX rejected public response')
            return data['data']
        if self.kind=='PERP':
            if not isinstance(data,dict) or data.get('success') is not True or data.get('code')!=0:raise ValueError('MEXC rejected public response')
            return data['data']
        return data

def metadata(raw,venue,kind,excludes):
    if kind=='PERP':
        if venue=='MEXC':
            raw=[r for r in raw if r.get('type')!=2 and not any(re.search(r'(?:stock|tradfi|etf|forex|commodity|commodities)',str(t),re.I) for t in r.get('conceptPlate',[]))]
        return {k:v for k,v in catalog(raw,venue).items() if v['base'] not in excludes['stable'] and v['base'] not in excludes['equity'].get(venue,[]) and not re.search(r'[235][LS]$',v['base'])}
    rows=raw.get('symbols',[]) if venue=='MEXC' else raw;result={}
    for r in rows:
        if venue=='MEXC':
            symbol=r.get('symbol','');base=r.get('baseAsset','')
            if r.get('quoteAsset')!='USDT' or str(r.get('status')) not in ('1','ENABLED','TRADING') or set(r.get('conceptPlates',[]))&set(excludes['plates']):continue
            contract=symbol
        else:
            contract=r.get('instId','');base=r.get('baseCcy','');symbol=base+'USDT'
            if contract!=base+'-USDT' or r.get('state')!='live' or r.get('quoteCcy')!='USDT':continue
        if not re.fullmatch(r'[A-Z0-9]+USDT',symbol) or base in excludes['stable'] or base in excludes['equity'].get(venue,[]) or re.search(r'[235][LS]$',base):continue
        result[symbol]={'symbol':symbol,'contract':contract,'base':base}
    return result

def ticker(raw,meta,venue,kind,stamp):
    cid=raw.get('symbol' if venue=='MEXC' else 'instId')
    if cid!=meta['contract']:raise ValueError('Ticker identity mismatch')
    bid=num(raw.get(('bidPrice' if kind=='SPOT' else 'bid1') if venue=='MEXC' else 'bidPx'))
    ask=num(raw.get(('askPrice' if kind=='SPOT' else 'ask1') if venue=='MEXC' else 'askPx'))
    last=num(raw.get('lastPrice' if venue=='MEXC' else 'last'))
    ts=stamp if venue=='MEXC' and kind=='SPOT' else num(raw.get('timestamp' if venue=='MEXC' else 'ts'))
    if any(v is None for v in (bid,ask,last,ts)) or not 0<bid<=ask or last<=0 or not 0<=stamp-ts<=120000:raise ValueError('Invalid/stale ticker')
    if venue=='MEXC':vol=num(raw.get('quoteVolume' if kind=='SPOT' else 'amount24'));basis='reported quote turnover'
    elif kind=='SPOT':vol=num(raw.get('volCcy24h'));basis='reported quote turnover'
    else:
        base=num(raw.get('volCcy24h'));vol=base*last if base is not None else None;basis='base turnover times current last, approximate USDT'
    if vol is None or vol<0:raise ValueError('Turnover missing')
    op=num(raw.get('openPrice' if venue=='MEXC' and kind=='SPOT' else 'open24h'))
    day=(last/op-1)*100 if op and op>0 else num(raw.get('priceChangePercent')) if kind=='SPOT' else None
    if venue=='MEXC' and kind=='PERP':
        change=num(raw.get('riseFallRate'));day=change*100 if change is not None else None
    oi=num(raw.get('holdVol')) if venue=='MEXC' and kind=='PERP' else None
    return {**meta,'venue':venue,'kind':kind,'key':venue+':'+kind+':'+meta['symbol'],
        'bid':bid,'ask':ask,'price':(bid+ask)/2,'last':last,'spread_pct':(ask-bid)/((bid+ask)/2)*100,
        'volume24':vol,'volume_kind':basis,'return24_pct':day,'observed_ms':stamp,'provider_ms':int(ts),
        'oi_contracts':oi,'funding_raw':num(raw.get('fundingRate')) if kind=='PERP' else None,
        'timestamp_kind':'public_response_observation' if venue=='MEXC' and kind=='SPOT' else 'provider'}

def snapshot(client,excludes,cfg):
    meta=metadata(client.get('catalog'),client.venue,client.kind,excludes)
    rows=client.get('tickers');stamp=int(time.time()*1000);quotes={};reject={}
    if not isinstance(rows,list):raise ValueError('Invalid bulk tickers')
    bycontract={v['contract']:v for v in meta.values()}
    for raw in rows:
        cid=raw.get('symbol' if client.venue=='MEXC' else 'instId')
        if cid not in bycontract:continue
        try:
            q=ticker(raw,bycontract[cid],client.venue,client.kind,stamp)
            if q['volume24']<cfg['minimum_volume24']:reject[q['symbol']]='low_turnover';continue
            if q['spread_pct']>cfg['maximum_radar_spread_pct']:reject[q['symbol']]='wide_spread';continue
            quotes[q['key']]=q
        except ValueError as e:reject[bycontract[cid]['symbol']]=str(e)
    return quotes,{'active_catalog':len(meta),'valid_liquid_tickers':len(quotes),'excluded':reject,'observed_ms':stamp}

def normalized(raw,venue,kind,interval,stamp):
    step=STEPS[interval];rows={}
    if venue=='MEXC' and kind=='PERP':
        names=('time','open','high','low','close','amount')
        if not isinstance(raw,dict) or any(not isinstance(raw.get(n),list) for n in names) or len({len(raw[n]) for n in names})!=1:raise ValueError('Contract candle arrays invalid')
        source=[]
        for t,o,h,l,c,q in zip(*(raw[n] for n in names)):
            sec=num(t)
            if sec is None or sec!=int(sec):raise ValueError('Contract candle time invalid')
            source.append([int(sec)*1000,o,h,l,c,q])
    else:
        if not isinstance(raw,list):raise ValueError('Candle response invalid')
        source=[]
        for r in raw:
            if len(r)<8 or (venue=='OKX' and (len(r)!=9 or str(r[8])!='1')):continue
            source.append([r[0],r[1],r[2],r[3],r[4],r[7]])
    for r in source:
        ts=num(r[0]);values=[num(x) for x in r[1:]]
        if ts is None or ts!=int(ts) or int(ts)%step or any(x is None for x in values):raise ValueError('Candle values/grid invalid')
        ts=int(ts);o,h,l,c,v=values
        if ts+step>stamp:continue
        if min(o,h,l,c)<=0 or v<0 or h<max(o,l,c) or l>min(o,h,c):raise ValueError('Invalid OHLCV')
        b={'t':ts,'o':o,'h':h,'l':l,'c':c,'v':v}
        if ts in rows and rows[ts]!=b:raise ValueError('Conflicting duplicate candle')
        rows[ts]=b
    return rows

def candles(raw,venue,kind,interval,stamp,count):
    step=STEPS[interval];rows=normalized(raw,venue,kind,interval,stamp)
    bs=[rows[k] for k in sorted(rows)][-count:]
    if len(bs)!=count or bs[-1]['t']+step!=stamp//step*step or any(b['t']-a['t']!=step for a,b in zip(bs,bs[1:])):raise ValueError('Missing/stale closed history')
    return bs

def bars(client,quote,interval,stamp,count,cache):
    key=quote['key']+':'+interval;cutoff=stamp//STEPS[interval]*STEPS[interval];old=cache.get(key)
    if old and old['cutoff']==cutoff and len(old['bars'])>=count:return old['bars'][-count:]
    bs=candles(client.get('candles',quote['contract'],interval),client.venue,client.kind,interval,stamp,count)
    cache[key]={'cutoff':cutoff,'bars':bs};return bs
