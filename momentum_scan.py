"""Read-only MEXC 4h strength scanner. Ranking is descriptive, not probability.

snapshot freezes rules before market data; download is bounded to that prefilter;
evaluate replays saved closed candles; quotes adds explicitly separate live checks.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import threading
import time
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import numpy as np
import pandas as pd

from parabolic_sar import parabolic_sar
from research import LOCAL
from study_dataset import STEP, atr_wilder, load_history, read_json

ROOT = Path(__file__).resolve().parent
API = 'https://api.mexc.com/api/v3/'
NETWORK_LOCK = threading.Lock()
LAST_REQUEST = 0.
STOP = threading.Event()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')


def public_get(endpoint):
    global LAST_REQUEST
    with NETWORK_LOCK:
        if STOP.is_set():
            raise RuntimeError('Stopped after access/rate-limit error')
        time.sleep(max(0., .3-(time.monotonic()-LAST_REQUEST)))
        LAST_REQUEST = time.monotonic()
    req = Request(API+endpoint, headers={'User-Agent': 'MEXC-public-research/3'})
    try:
        with urlopen(req, timeout=25) as response:
            return json.load(response)
    except HTTPError as exc:
        if exc.code in (403, 418, 429):
            STOP.set()
        raise


def local_time(ms):
    return datetime.fromtimestamp(int(ms)/1000, LOCAL).strftime('%d.%m.%Y %H:%M')


def snapshot():
    config = read_json(ROOT/'momentum_config.json')
    # Freeze source/config before reading the candidate market snapshot.
    freeze = {
        'frozen_at_utc': datetime.now(timezone.utc).isoformat(),
        'config': config,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'config_sha256': hashlib.sha256((ROOT/'momentum_config.json').read_bytes()).hexdigest(),
    }
    provisional = ROOT/'data'/'momentum_v3'/'design_frozen.json'
    if not provisional.exists():
        save(provisional, freeze)
    clock = public_get('time')
    end = int(clock['serverTime'])
    run_id = datetime.fromtimestamp(end/1000, timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    directory = ROOT/'data'/'momentum_v3'/run_id
    save(directory/'design_frozen.json', freeze)
    info = public_get('exchangeInfo')
    tickers = public_get('ticker/24hr')
    save(directory/'universe_raw.json', {'fetched_server_time_ms':end, 'data':info})
    save(directory/'tickers_raw.json', {'fetched_server_time_ms':end, 'data':tickers})
    sampling = read_json(ROOT/'study_config.json')['sampling']
    universe = []
    for item in info['symbols']:
        base, symbol = item['baseAsset'], item['symbol']
        if (item['quoteAsset'] != 'USDT' or str(item['status']) not in ('1','ENABLED','TRADING')
                or base in sampling['stable_bases'] or re.search(r'[235][LS]$', base)
                or set(item.get('conceptPlates', [])) & set(sampling['excluded_concept_plates'])
                or not re.fullmatch(r'[A-Z0-9]+USDT', symbol)):
            continue
        universe.append(symbol)
    ticker_map = {x['symbol']: x for x in tickers}
    chosen, exclusions = [], {'ticker_missing_or_invalid':0, 'return_band':0, 'low_volume':0}
    pre = config['prefilter']
    for symbol in sorted(set(universe)):
        try:
            t = ticker_map[symbol]
            # Calculate directly to avoid exchange-specific percent units.
            gain = (float(t['lastPrice'])/float(t['openPrice'])-1)*100
            volume = float(t['quoteVolume'])
            if not np.isfinite([gain,volume]).all():
                raise ValueError('nonfinite ticker')
        except (KeyError, ValueError, TypeError, ZeroDivisionError):
            exclusions['ticker_missing_or_invalid'] += 1
            continue
        if not pre['ticker_return24_min_pct'] <= gain <= pre['ticker_return24_max_pct']:
            exclusions['return_band'] += 1
        elif volume < pre['ticker_quote_volume24_min_usdt']:
            exclusions['low_volume'] += 1
        else:
            chosen.append(symbol)
    save(directory/'selection.json', {
        'run_id':run_id, 'snapshot_server_time_ms':end,
        'closed_decision_ms':end//STEP*STEP,
        'api_pairs':len(info['symbols']), 'crypto_usdt_universe':len(set(universe)),
        'prefilter_passed':len(chosen), 'prefilter_exclusions':exclusions,
        'symbols':list(dict.fromkeys(['BTCUSDT']+chosen)),
        'rank_symbols':[s for s in chosen if s != 'BTCUSDT'],
        'limitation':'24h ticker >=0% and <=35%, >=10k USDT prefilter. Negative 24h turnarounds, illiquid assets and larger pumps not scanned. Active API spot universe only.',
    })
    save(ROOT/'data'/'momentum_v3'/'latest_run.json', {'directory':str(directory)})
    print(f'Snapshot {run_id}: crypto universe {len(universe)}, prefilter passed {len(chosen)}, closed decision {local_time(end//STEP*STEP)} TR', flush=True)
    return directory


def selected_directory(value):
    return Path(value).resolve() if value else Path(read_json(ROOT/'data'/'momentum_v3'/'latest_run.json')['directory'])


def download(directory):
    selection = read_json(directory/'selection.json')
    config = read_json(directory/'design_frozen.json')['config']
    end = selection['closed_decision_ms']-1
    start = selection['closed_decision_ms']-config['history_bars']*STEP
    def fetch(symbol):
        path = directory/'history'/f'{symbol}.json'
        if path.exists():
            return {'symbol':symbol, 'cached':True}
        if not re.fullmatch(r'[A-Z0-9]+USDT',symbol):
            raise ValueError('Invalid symbol')
        endpoint = f'klines?symbol={symbol}&interval=4h&startTime={start}&endTime={end}&limit=500'
        rows = public_get(endpoint)
        if not isinstance(rows,list):
            raise ValueError(f'Non-array klines: {symbol}')
        save(path, {'source':'MEXC Spot REST API','symbol':symbol,'interval':'4h',
                    'url':API+endpoint,'fetched_server_time_ms':selection['snapshot_server_time_ms'],
                    'requested_start_ms':start,'requested_end_ms':end,'rows':rows})
        return {'symbol':symbol,'rows':len(rows)}
    audits = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        jobs = {pool.submit(fetch,s):s for s in selection['symbols']}
        for job in as_completed(jobs):
            try:
                audits.append(job.result())
            except Exception as exc:
                audits.append({'symbol':jobs[job],'error':str(exc)})
            if len(audits)%25==0 or len(audits)==len(jobs):
                print(f'History {len(audits)}/{len(jobs)}; errors {sum("error" in a for a in audits)}',flush=True)
    save(directory/'download_audit.json',audits)
    if STOP.is_set():
        raise RuntimeError('Stopped on access/rate limit; completed files retained')


def features(frame, btc_return, config):
    """Causal strength features. Call on one contiguous closed-candle segment."""
    out = frame.copy()
    r = config['rules']
    atr = atr_wilder(out).replace(0,np.nan)
    out['atr'] = atr
    out['ema20'] = out['close'].ewm(span=20,adjust=False,min_periods=20).mean()
    out['ema50'] = out['close'].ewm(span=50,adjust=False,min_periods=50).mean()
    out['return24_pct'] = (out['close']/out['close'].shift(6)-1)*100
    out['return72_pct'] = (out['close']/out['close'].shift(18)-1)*100
    out['relative24_pct_points'] = out['return24_pct']-btc_return.reindex(out.index)
    out['relative_strength8h_positive'] = ((out['close']/out['close'].shift(2)-1)*100 >
                                          btc_return.attrs['return8'].reindex(out.index))
    resistance = out['high'].shift(1).rolling(r['resistance_lookback_bars']).max()
    volume_ratio = out['quote_volume']/out['quote_volume'].shift(1).rolling(20).median().replace(0,np.nan)
    # First close above rolling resistance, with observed breakout volume.
    breakout = ((out['close']>resistance)&(out['close'].shift(1)<=resistance.shift(1))&
                (volume_ratio>=r['breakout_volume_median_ratio_min']))
    out['breakout_now'] = breakout
    limit = r['fresh_breakout_bars']-1
    out['breakout_level'] = resistance.where(breakout).ffill(limit=limit)
    out['breakout_volume_ratio'] = volume_ratio.where(breakout).ffill(limit=limit)
    positions = pd.Series(np.arange(len(out)),index=out.index,dtype=float)
    out['breakout_age_bars'] = positions-positions.where(breakout).ffill(limit=limit)
    out['breakout_open_ms'] = pd.Series(out.index.astype(float),index=out.index).where(breakout).ffill(limit=limit)
    out['breakout_low'] = out['low'].where(breakout).ffill(limit=limit)
    hold_low = pd.Series(np.nan,index=out.index,dtype=float)
    last = -100000
    for i in range(len(out)):
        if breakout.iloc[i]: last=i
        if i-last<=limit:
            hold_low.iloc[i] = out['low'].iloc[last+1:i+1].min() if i>last else out['close'].iloc[i]
    out['hold_low'] = hold_low
    out['ema20_extension_atr'] = (out['close']-out['ema20'])/atr
    out['breakout_extension_atr'] = (out['close']-out['breakout_level'])/atr
    out['pullback_high3_atr'] = (out['high'].rolling(3).max()-out['close'])/atr
    spread = (out['high']-out['low']).replace(0,np.nan)
    out['close_position'] = (out['close']-out['low'])/spread
    out['higher_lows'] = out['low'].rolling(3).median()>out['low'].shift(3).rolling(3).median()
    out['ema20_above_ema50'] = out['ema20']>out['ema50']
    out['sar_below'] = parabolic_sar(out)['sar_below']
    out['quote_volume24'] = out['quote_volume'].rolling(6).sum()
    out['nonzero24'] = (out['quote_volume']>0).rolling(6).sum()
    out['invalidation_level'] = np.minimum(out['breakout_low'],out['low'].rolling(3).min())-r['invalidation_buffer_atr']*atr
    out['invalidation_distance_pct'] = (1-out['invalidation_level']/out['close'])*100
    gates = {
        'history':pd.Series(np.arange(len(out))>=config['minimum_history_bars']-1,index=out.index),
        'fresh_breakout':out['breakout_level'].notna(),
        'trend':(out['close']>out['ema20'])&(out['close']>out['ema50'])&(out['ema20']>out['ema20'].shift(3)),
        'holds_breakout':(out['close']>=out['breakout_level'])&(out['hold_low']>=out['breakout_level']-r['breakout_hold_tolerance_atr']*atr),
        'gain_band':out['return24_pct'].between(r['return24_min_pct'],r['return24_max_pct'])&(out['return72_pct']<=r['return72_max_pct']),
        'relative_strength':out['relative24_pct_points']>0,
        'not_extended':out['ema20_extension_atr'].between(0,r['ema20_extension_atr_max'])&out['breakout_extension_atr'].between(0,r['breakout_extension_atr_max']),
        'holds_gains':(out['pullback_high3_atr']<=r['pullback_from_high3_atr_max'])&(out['close_position']>=r['close_position_min']),
        'invalidation':out['invalidation_distance_pct'].between(0,r['invalidation_distance_max_pct'],inclusive='neither'),
        'liquidity':(out['quote_volume24']>=r['quote_volume24_min_usdt'])&(out['nonzero24']==6),
    }
    for name,mask in gates.items(): out['gate_'+name] = mask.fillna(False)
    out['qualified'] = out[['gate_'+name for name in gates]].all(axis=1)
    out['breakout_volume_ratio_at_least_2'] = out['breakout_volume_ratio']>=2
    out['strength_score'] = sum(out[name].astype(int)*weight for name,weight in r['score_weights'].items())
    out['decision_ms'] = out.index+STEP
    return out


def evaluate(directory):
    selection = read_json(directory/'selection.json')
    config = read_json(directory/'design_frozen.json')['config']
    decision = selection['closed_decision_ms']
    btc,audit = load_history(directory/'history'/'BTCUSDT.json')
    if audit['gaps'] or len(btc)<config['minimum_history_bars'] or int(btc.index[-1])+STEP != decision:
        raise ValueError('BTC history stale/incomplete')
    btc_return = (btc['close']/btc['close'].shift(6)-1)*100
    btc_return.attrs['return8'] = (btc['close']/btc['close'].shift(2)-1)*100
    rows, audits = [], []
    for symbol in selection['rank_symbols']:
        try:
            f,audit = load_history(directory/'history'/f'{symbol}.json')
            if f.empty: raise ValueError('empty history')
            # Restart all rolling features after the last gap.
            gaps = np.flatnonzero(np.diff(f.index.to_numpy()) != STEP)
            segment = f.iloc[int(gaps[-1])+1:] if len(gaps) else f
            if len(segment)<config['minimum_history_bars']: raise ValueError('insufficient contiguous history')
            if int(segment.index[-1])+STEP != decision: raise ValueError('stale last candle')
            enriched = features(segment,btc_return,config)
            row = enriched.iloc[-1]
            result = {'symbol':symbol}
            for key,value in row.items():
                result[key] = None if pd.isna(value) else (value.item() if hasattr(value,'item') else value)
            result['liquidity_band'] = 'main' if row['quote_volume24']>=config['rules']['main_liquidity_band_usdt24'] else 'thin'
            result['failed_gates'] = [key[5:] for key,value in row.items() if key.startswith('gate_') and not value]
            rows.append(result)
            audits.append({'symbol':symbol, **audit,'contiguous_rows':len(segment)})
        except (ValueError,KeyError,TypeError,FileNotFoundError) as exc:
            audits.append({'symbol':symbol,'error':str(exc)})
    candidates = sorted([x for x in rows if x['qualified']], key=lambda x:(-x['strength_score'],-x['relative24_pct_points'],x['symbol']))
    result_dir = ROOT/'results'/'momentum_v3'/selection['run_id']
    result_dir.mkdir(parents=True,exist_ok=True)
    save(result_dir/'all_snapshots.json',rows)
    save(result_dir/'data_audit.json',audits)
    summary = {
        **{k:v for k,v in selection.items() if k not in ('symbols','rank_symbols')},
        'analyzed_symbols':len(rows),'unusable_symbols':sum('error' in a for a in audits),
        'candidates':len(candidates),'main_candidates':sum(x['liquidity_band']=='main' for x in candidates),
        'thin_candidates':sum(x['liquidity_band']=='thin' for x in candidates),
        'btc_return24_pct':float(btc_return.iloc[-1]),
        'gate_fail_counts':{key:sum(not x[key] for x in rows) for key in (rows[0] if rows else {}) if key.startswith('gate_')},
        'validation_status':config['evaluation_plan']['validation_status'],
        'data_directory':str(directory),
    }
    save(result_dir/'summary.json',summary)
    save(result_dir/'candidates.json',candidates)
    report(result_dir,config)
    print(json.dumps(summary,ensure_ascii=False),flush=True)
    return result_dir


def report(result_dir,config):
    summary = read_json(result_dir/'summary.json')
    candidates = read_json(result_dir/'candidates.json')
    lines = ['# Başlamış ve gücünü koruyan yükselişler — 4 saat', '',
             f"Karar kesimi: **{local_time(summary['closed_decision_ms'])} Türkiye saati**. Yalnız bu saatte kapanmış mumlar kullanıldı.", '',
             f"MEXC aktif kripto/USDT evreni: {summary['crypto_usdt_universe']}; 24 saatlik ön elemeden geçen {summary['prefilter_passed']}; değerlendirilen {summary['analyzed_symbols']}; kullanılamayan {summary['unusable_symbols']}. BTC son 24 saat: %{summary['btc_return24_pct']:.2f}.", '',
             f"Kuralları sağlayan {summary['candidates']} aday: {summary['main_candidates']} normal hacim grubunda, {summary['thin_candidates']} düşük hacim grubunda.", '',
             '## Ne arıyoruz?', '',
             'Son üç kapalı mum içinde (en çok 12 saatlik pencere) önceki 20 mumun tepesinin hacimle aşılması; fiyatın kırılan seviyede tutunması; yükselen EMA20 ve fiyatın EMA20/50 üzerinde olması; BTC’ye göre pozitif 24 saatlik güç; %2–30 kapalı 24 saat getirisi; sınırlı geri çekilme ve ATR ile sınırlı uzama. Kırılım mumunun hacmi önceki 20 mum medyanının en az 1,3 katı. Geçmişte sert mum görülmesi otomatik eleme sebebi değil.', '',
             'SAR yalnız destekleyici puan. Sıkışma zorunlu değil; dolaşımdaki arz adedi bir alım filtresi değil. Aday yoksa liste zorla doldurulmaz.', '',
             'Puan, beş ek niteliğin sabit ağırlıklı toplamıdır; getiri veya başarı olasılığı değildir. Kurallar bu sürümün güncel listesi görülmeden kaydedildi; sayısal eşikler yeni hipotezlerdir ve ileri dönem doğrulaması bekler.', '',
             '## Adaylar', '']
    for band,label in [('main','Normal hacim: en az 100.000 USDT / 24 saat'),('thin','Düşük hacim: 10.000–100.000 USDT / 24 saat')]:
        lines += [f'### {label}', '', '| Coin | Puan | 24s % | BTC farkı (puan) | Kırılım yaşı | Hacim katı | EMA20 uzaklık (ATR) | 24s hacim USDT | Kapanış | Yapı bozulma referansı |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
        selected = [x for x in candidates if x['liquidity_band']==band]
        for x in selected:
            lines.append(f"| {x['symbol']} | {x['strength_score']} | {x['return24_pct']:.2f} | {x['relative24_pct_points']:.2f} | {int(x['breakout_age_bars'])*4} saat | {x['breakout_volume_ratio']:.2f} | {x['ema20_extension_atr']:.2f} | {x['quote_volume24']:,.0f} | {x['close']:.8g} | {x['invalidation_level']:.8g} |")
        if not selected: lines += ['| Uygun aday yok | | | | | | | | | |']
        lines.append('')
    quotes_path = result_dir/'current_quotes.json'
    if quotes_path.exists():
        quotes = read_json(quotes_path)
        lines += ['## Sonraki fiyat kontrolü', '',
                  f"Kontrol: {local_time(quotes['fetched_server_time_ms'])} Türkiye saati. Bu değerler karar mumundan sonradır; yukarıdaki kapalı mum sıralamasına eklenmedi. Alış/satış orta fiyatı kullanıldı; son işlem veya gerçekleşebilir emir fiyatı değildir.", '',
                  '| Coin | Alış/satış orta fiyatı | Makas % | Kapanıştan fark (ATR) | Durum |',
                  '|---|---:|---:|---:|---|']
        for q in quotes['checks']:
            if q.get('mid_price') is None:
                lines.append(f"| {q['symbol']} | — | — | — | Fiyat doğrulanamadı |")
            else:
                lines.append(f"| {q['symbol']} | {q['mid_price']:.8g} | {q['spread_pct']:.3f} | {q['drift_atr']:.2f} | {q['status']} |")
        lines.append('')
    lines += ['## Sınırlar ve bir sonraki ölçüm', '',
              'Bu sürüm, eski deneylerin doğrulanmış devamı değildir. Eski sonuçlar yalnız tasarım tercihlerini yönlendirdi. Yalnız aktif API spot pariteleri ve 24 saat getirisi %0–35, hacmi en az 10.000 USDT olan ön eleme incelendi. Negatif 24 saat getirisine rağmen yeni dönen coinler kapsam dışında. Düşük hacim ayrı gösterildi; o grupta emir derinliği henüz doğrulanmadı.', '',
              'Güncel makas kontrolü emir defteri derinliği veya kayma testi değildir. Kapanış ile güncel fiyat farklı zamanlara aittir. Yapı bozulma seviyesi gözlenebilir bir teknik referanstır; bu fiyattan çıkılacağı varsayılmaz.', '',
              'Başarıyı bundan sonra 12/24/48 saatlik kapanış getirisi, BTC’ye göre getiri, ters hareket ve yapı bozulma oranıyla değerlendireceğiz. Rastgele kontroller aynı zamanda ve benzer hacim/oynaklık grubunda seçilmeli. Henüz bu yeni sürüm için başarı oranı veya pozitif beklenen getiri hesaplanmadı.', '',
              'Kaynak: [MEXC resmi genel piyasa verisi API belgeleri](https://mexcdevelop.github.io/apidocs/spot_v3_en/). SAR bağlamı: [TradingView resmi açıklaması](https://www.tradingview.com/support/solutions/43000502597-parabolic-sar-sar/).', '']
    (result_dir/'guclu_baslangiclar.md').write_text('\n'.join(lines),encoding='utf-8')


def quotes(directory):
    selection = read_json(directory/'selection.json')
    result_dir = ROOT/'results'/'momentum_v3'/selection['run_id']
    config = read_json(directory/'design_frozen.json')['config']
    candidates = read_json(result_dir/'candidates.json')
    book = public_get('ticker/bookTicker')
    clock = public_get('time')
    save(directory/'book_tickers_raw.json',{'fetched_server_time_ms':int(clock['serverTime']),'data':book})
    index = {x['symbol']:x for x in book}
    checks = []
    for row in candidates:
        q = {'symbol':row['symbol']}
        try:
            entry = index[row['symbol']]
            bid,ask = float(entry['bidPrice']),float(entry['askPrice'])
            if not 0<bid<=ask: raise ValueError('Invalid quote')
            mid = (bid+ask)/2
            spread = (ask-bid)/mid*100
            drift = (mid-row['close'])/row['atr']
            flags = []
            if mid<row['invalidation_level']: flags.append('Yapı bozulma referansı altında')
            elif mid<row['breakout_level']: flags.append('Kırılan seviye altında')
            if spread>config['current_quote_checks']['spread_max_pct']: flags.append('Geniş makas')
            if abs(drift)>config['current_quote_checks']['closed_price_drift_max_atr']: flags.append('Kapanıştan uzaklaştı; yeniden teyit gerekli')
            q.update(mid_price=mid,spread_pct=spread,drift_atr=drift,status='; '.join(flags) if flags else 'Anlık kontrolde eşikler korunuyor')
        except (KeyError,ValueError,TypeError):
            q.update(mid_price=None,status='Fiyat doğrulanamadı')
        checks.append(q)
    save(result_dir/'current_quotes.json',{'fetched_server_time_ms':int(clock['serverTime']),'checks':checks})
    report(result_dir,config)
    print(json.dumps(checks,ensure_ascii=False),flush=True)


def self_check():
    config = read_json(ROOT/'momentum_config.json')
    n = 240
    index = pd.Index(np.arange(n)*STEP,name='open_ms')
    p = np.full(n,10.)
    frame = pd.DataFrame({'open':p,'close':p,'high':p+.04,'low':p-.04,'volume':10000.,'quote_volume':100000.},index=index)
    # Hand-built positive: modest new breakout on double volume, closes near high.
    frame.loc[index[-1],['open','close','high','low','quote_volume']] = [10.,10.22,10.23,9.99,200000.]
    btc = pd.Series(0.,index=index)
    btc.attrs['return8'] = pd.Series(0.,index=index)
    got = features(frame,btc,config)
    assert got.iloc[-1]['qualified'],got.iloc[-1].filter(like='gate_').to_dict()
    assert got.iloc[-1]['breakout_age_bars']==0
    # Repaint prevention: mutating later observations cannot change earlier values.
    changed = frame.copy()
    changed.iloc[210:,:4] *= 3
    pd.testing.assert_frame_equal(got.iloc[:210],features(changed,btc,config).iloc[:210])
    scaled = frame.copy()
    scaled[['open','close','high','low']] *= 7
    check = features(scaled,btc,config)
    pd.testing.assert_series_equal(got['qualified'],check['qualified'])
    np.testing.assert_allclose(got['invalidation_distance_pct'],check['invalidation_distance_pct'],equal_nan=True,atol=1e-10)
    weak = frame.copy()
    weak.loc[index[-1],['open','close','high','low']] = [10.,9.8,10.23,9.7]
    assert not features(weak,btc,config).iloc[-1]['qualified']
    # Labels/future prices are never inputs to this module.
    assert not any('mfe' in k or 'label' in k for k in got.columns)
    print('Checks passed: positive breakout fixture, rejected failed breakout, no future dependency, price-scale invariance.')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('phase',choices=['check','snapshot','download','evaluate','quotes'])
    parser.add_argument('--directory')
    args = parser.parse_args()
    if args.phase=='check': self_check()
    elif args.phase=='snapshot': snapshot()
    else:
        directory = selected_directory(args.directory)
        {'download':download,'evaluate':evaluate,'quotes':quotes}[args.phase](directory)
