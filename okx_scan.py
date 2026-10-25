"""OKX spot adapter using the unchanged v3 feature/selection rules.

Public market-data GETs only. OKX newest-first, 9-field candles are normalized
to the research schema; incomplete candles and other quote currencies excluded.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import threading
import time
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request,urlopen

import numpy as np
import pandas as pd

import momentum_scan as rules
from study_dataset import STEP,load_history,read_json

ROOT=Path(__file__).resolve().parent
API='https://www.okx.com/api/v5/'
DATA=ROOT/'data'/'okx_momentum_v3'
RESULTS=ROOT/'results'/'okx_momentum_v3'
LOCK=threading.Lock()
LAST=0.
STOP=threading.Event()
local_time=rules.local_time
save=rules.save


def request(endpoint):
    global LAST
    for attempt in range(3):
        with LOCK:
            if STOP.is_set():raise RuntimeError('OKX stopped on access/rate limit')
            time.sleep(max(0.,.3-(time.monotonic()-LAST)))
            LAST=time.monotonic()
        try:
            with urlopen(Request(API+endpoint,headers={'User-Agent':'Public-strength-research/1'}),timeout=25) as response:
                payload=json.load(response)
            if str(payload.get('code'))!='0':
                if str(payload.get('code')) in ('50011','50040'):STOP.set()
                raise ValueError(f"OKX {payload.get('code')}: {payload.get('msg')}")
            return payload
        except HTTPError as exc:
            if exc.code in (403,418,429):STOP.set();raise
            if exc.code<500 or attempt==2:raise
        except (OSError,TimeoutError):
            if attempt==2:raise
        time.sleep(1+attempt)
    raise RuntimeError('Unreachable')


def instrument(symbol):
    if not re.fullmatch(r'[A-Z0-9]+USDT',symbol):raise ValueError('Invalid OKX symbol')
    return symbol[:-4]+'-USDT'


def book_rows(payload):
    return [{'symbol':x['instId'].replace('-',''),'bidPrice':x.get('bidPx'),
             'askPrice':x.get('askPx'),'source_ts':x.get('ts')}
            for x in payload['data'] if re.fullmatch(r'[A-Z0-9]+-USDT',x['instId'])]


def public_get(endpoint):
    """Only the two compatibility endpoints needed by the generic ledger."""
    if endpoint=='time':return {'serverTime':int(request('public/time')['data'][0]['ts'])}
    if endpoint=='ticker/bookTicker':return book_rows(request('market/tickers?instType=SPOT'))
    raise ValueError('Unsupported compatibility endpoint; use OKX request/fetch_rows')


def normalize_candles(rows,step,start,end):
    normalized={}
    for x in rows:
        if len(x)!=9:raise ValueError('Unexpected OKX candle schema')
        stamp=int(x[0])
        if str(x[8])!='1' or not start<=stamp<=end:continue
        if stamp%step:raise ValueError('OKX candle off time grid')
        # volCcyQuote is quote volume, never the base-token count.
        row=[stamp,*x[1:6],stamp+step,x[7]]
        if stamp in normalized and normalized[stamp]!=row:raise ValueError('Conflicting OKX candle')
        normalized[stamp]=row
    return [normalized[k] for k in sorted(normalized)]


def fetch_rows(symbol,interval,start,end,recent=False):
    step=60000 if interval=='1m' else STEP
    if interval not in ('1m','4h'):raise ValueError('Unsupported candle interval')
    bar='1m' if interval=='1m' else '4H'
    cursor=int(end)+1
    all_rows=[];urls=[]
    while cursor>start:
        endpoint=('market/candles' if recent else 'market/history-candles')+'?'+urlencode({
            'instId':instrument(symbol),'bar':bar,'after':cursor,'before':int(start)-1,'limit':300})
        payload=request(endpoint)
        page=payload['data'];urls.append(API+endpoint)
        if not page:break
        stamps=[int(x[0]) for x in page]
        oldest=min(stamps)
        if oldest>=cursor:raise ValueError('OKX backward pagination did not advance')
        all_rows.extend(page)
        cursor=oldest
        if oldest<=start or len(page)<300:break
    return normalize_candles(all_rows,step,start,end),urls


def selected_directory(value=None):
    return Path(value).resolve() if value else Path(read_json(DATA/'latest_run.json')['directory'])


def snapshot():
    config=read_json(ROOT/'momentum_config.json')
    freeze={'config':config,'frozen_at_utc':datetime.now(timezone.utc).isoformat(),
            'adapter_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'rules_sha256':hashlib.sha256((ROOT/'momentum_scan.py').read_bytes()).hexdigest(),
            'config_sha256':hashlib.sha256((ROOT/'momentum_config.json').read_bytes()).hexdigest()}
    end=public_get('time')['serverTime']
    run_id=datetime.fromtimestamp(end/1000,timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    directory=DATA/run_id
    save(directory/'design_frozen.json',freeze)
    info=request('public/instruments?instType=SPOT')
    tickers=request('market/tickers?instType=SPOT')
    save(directory/'universe_raw.json',{'fetched_server_time_ms':end,'data':info})
    save(directory/'tickers_raw.json',{'fetched_server_time_ms':end,'data':tickers})
    sampling=read_json(ROOT/'study_config.json')['sampling']
    universe=[]
    for x in info['data']:
        if (x['state']!='live' or x['quoteCcy']!='USDT' or x['baseCcy'] in sampling['stable_bases']
                or re.search(r'[235][LS]$',x['baseCcy']) or not re.fullmatch(r'[A-Z0-9]+-USDT',x['instId'])):continue
        universe.append(x['instId'].replace('-',''))
    index={x['instId'].replace('-',''):x for x in tickers['data']}
    chosen=[];excluded={'missing_or_invalid':0,'return_band':0,'low_volume':0}
    p=config['prefilter']
    for symbol in sorted(set(universe)):
        try:
            t=index[symbol]
            gain=(float(t['last'])/float(t['open24h'])-1)*100
            volume=float(t['volCcy24h'])
            if not np.isfinite([gain,volume]).all():raise ValueError('Nonfinite')
        except (KeyError,TypeError,ValueError,ZeroDivisionError):excluded['missing_or_invalid']+=1;continue
        if not p['ticker_return24_min_pct']<=gain<=p['ticker_return24_max_pct']:excluded['return_band']+=1
        elif volume<p['ticker_quote_volume24_min_usdt']:excluded['low_volume']+=1
        else:chosen.append(symbol)
    save(directory/'selection.json',{'exchange':'OKX','run_id':run_id,'snapshot_server_time_ms':end,
         'closed_decision_ms':end//STEP*STEP,'api_pairs':len(info['data']),
         'crypto_usdt_universe':len(set(universe)),'universe_symbols':sorted(set(universe)),
         'prefilter_passed':len(chosen),'prefilter_exclusions':excluded,
         'symbols':list(dict.fromkeys(['BTCUSDT']+chosen)),
         'rank_symbols':[x for x in chosen if x!='BTCUSDT'],
         'limitation':'Active API spot USDT only. Same 0-35% live return / 10k USDT volume prefilter as MEXC. Exchange listing and observation times differ.'})
    save(DATA/'latest_run.json',{'directory':str(directory)})
    print(f'OKX snapshot {run_id}: universe {len(set(universe))}, prefilter {len(chosen)}',flush=True)
    return directory


def download(directory):
    s=read_json(directory/'selection.json');cfg=read_json(directory/'design_frozen.json')['config']
    start=s['closed_decision_ms']-cfg['history_bars']*STEP;end=s['closed_decision_ms']-1
    def fetch(symbol):
        path=directory/'history'/f'{symbol}.json'
        if path.exists():return {'symbol':symbol,'cached':True}
        rows,urls=fetch_rows(symbol,'4h',start,end,recent=True)
        save(path,{'source':'OKX public spot REST','symbol':symbol,'interval':'4h','urls':urls,
             'fetched_server_time_ms':s['snapshot_server_time_ms'],'rows':rows})
        return {'symbol':symbol,'rows':len(rows)}
    audit=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        jobs={pool.submit(fetch,symbol):symbol for symbol in s['symbols']}
        for job in as_completed(jobs):
            try:audit.append(job.result())
            except Exception as exc:audit.append({'symbol':jobs[job],'error':str(exc)})
            if len(audit)%25==0 or len(audit)==len(jobs):print(f'OKX history {len(audit)}/{len(jobs)}',flush=True)
    save(directory/'download_audit.json',audit)
    if STOP.is_set():raise RuntimeError('OKX access/rate-limit stop')


def evaluate(directory):
    s=read_json(directory/'selection.json');cfg=read_json(directory/'design_frozen.json')['config']
    btc,audit=load_history(directory/'history'/'BTCUSDT.json')
    if audit['gaps'] or len(btc)<cfg['minimum_history_bars'] or int(btc.index[-1])+STEP!=s['closed_decision_ms']:
        raise ValueError('OKX BTC stale/incomplete')
    btc_return=(btc['close']/btc['close'].shift(6)-1)*100
    btc_return.attrs['return8']=(btc['close']/btc['close'].shift(2)-1)*100
    snapshots=[];audits=[]
    for symbol in s['rank_symbols']:
        try:
            f,audit=load_history(directory/'history'/f'{symbol}.json')
            if f.empty:raise ValueError('No candles')
            gaps=np.flatnonzero(np.diff(f.index.to_numpy())!=STEP)
            f=f.iloc[int(gaps[-1])+1:] if len(gaps) else f
            if len(f)<cfg['minimum_history_bars']:raise ValueError('Insufficient contiguous history')
            if int(f.index[-1])+STEP!=s['closed_decision_ms']:raise ValueError('Stale last candle')
            row=rules.features(f,btc_return,cfg).iloc[-1]
            result={'symbol':symbol,'exchange':'OKX'}
            for k,v in row.items():result[k]=None if pd.isna(v) else (v.item() if hasattr(v,'item') else v)
            result['liquidity_band']='main' if row['quote_volume24']>=cfg['rules']['main_liquidity_band_usdt24'] else 'thin'
            result['failed_gates']=[k[5:] for k,v in row.items() if k.startswith('gate_') and not v]
            snapshots.append(result);audits.append({'symbol':symbol,**audit})
        except (FileNotFoundError,ValueError,TypeError,KeyError) as exc:audits.append({'symbol':symbol,'error':str(exc)})
    candidates=sorted([x for x in snapshots if x['qualified']],key=lambda x:(-x['strength_score'],-x['relative24_pct_points'],x['symbol']))
    result_dir=RESULTS/s['run_id']
    save(result_dir/'all_snapshots.json',snapshots);save(result_dir/'candidates.json',candidates)
    save(result_dir/'data_audit.json',audits)
    summary={k:v for k,v in s.items() if k not in ('symbols','rank_symbols','universe_symbols')}
    summary.update(analyzed_symbols=len(snapshots),unusable_symbols=sum('error' in a for a in audits),candidates=len(candidates),
                   btc_return24_pct=float(btc_return.iloc[-1]),main_candidates=sum(x['liquidity_band']=='main' for x in candidates))
    save(result_dir/'summary.json',summary)
    print(json.dumps(summary,ensure_ascii=False),flush=True)
    return result_dir


def quotes(directory):
    s=read_json(directory/'selection.json')
    raw=request('market/tickers?instType=SPOT')
    end=public_get('time')['serverTime']
    save(directory/'book_tickers_source.json',{'fetched_server_time_ms':end,'data':raw})
    save(directory/'book_tickers_raw.json',{'fetched_server_time_ms':end,'data':book_rows(raw)})

