"""Coin Tarama 3 V5 snapshot adapter. Unchanged V3/V4 source files are dependencies only."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

import numpy as np

import momentum_scan as mexc
import okx_scan as okx
import paper_watch
import strength_v5 as model
import support_indicators
from study_dataset import STEP, load_history, read_json

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results'/'strength_v5'


def normalized(row):
    result = {}
    for key, value in row.items():
        if isinstance(value, (float, np.floating)) and not np.isfinite(value): value = None
        elif hasattr(value, 'item'): value = value.item()
        result[key] = value
    return result


def last_segment(frame):
    gaps = np.flatnonzero(np.diff(frame.index.to_numpy()) != STEP)
    return frame.iloc[int(gaps[-1])+1:] if len(gaps) else frame


def snapshot(exchange, config):
    adapter = mexc if exchange == 'MEXC' else okx
    end = adapter.public_get('time')['serverTime']
    run_id = datetime.fromtimestamp(end/1000, timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    directory = ROOT/'data'/'strength_v5'/exchange/run_id
    if exchange == 'MEXC':
        info, raw_tickers = mexc.public_get('exchangeInfo'), mexc.public_get('ticker/24hr')
        sampling = read_json(ROOT/'study_config.json')['sampling']
        universe = [x['symbol'] for x in info['symbols'] if x['quoteAsset']=='USDT'
                    and str(x['status']) in ('1','ENABLED','TRADING')
                    and x['baseAsset'] not in sampling['stable_bases']
                    and not re.search(r'[235][LS]$', x['baseAsset'])
                    and not set(x.get('conceptPlates',[])) & set(sampling['excluded_concept_plates'])
                    and re.fullmatch(r'[A-Z0-9]+USDT',x['symbol'])]
        tickers = {x['symbol']:(x['lastPrice'],x['openPrice'],x['quoteVolume']) for x in raw_tickers}
    else:
        info = okx.request('public/instruments?instType=SPOT')
        raw_tickers = okx.request('market/tickers?instType=SPOT')
        sampling = read_json(ROOT/'study_config.json')['sampling']
        universe = [x['instId'].replace('-','') for x in info['data'] if x['state']=='live'
                    and x['quoteCcy']=='USDT' and x['baseCcy'] not in sampling['stable_bases']
                    and not re.search(r'[235][LS]$',x['baseCcy'])
                    and re.fullmatch(r'[A-Z0-9]+-USDT',x['instId'])]
        tickers = {x['instId'].replace('-',''):(x['last'],x['open24h'],x['volCcy24h']) for x in raw_tickers['data']}
    chosen = []
    for symbol in sorted(set(universe)):
        try:
            last, opening, volume = map(float, tickers[symbol])
            gain = (last/opening-1)*100
            if not np.isfinite([gain,volume]).all(): continue
            if gain >= config['prefilter']['ticker_return24_min_pct'] and volume >= config['prefilter']['ticker_quote_volume24_min_usdt']:
                chosen.append(symbol)
        except (KeyError, ValueError, TypeError, ZeroDivisionError): continue
    mexc.save(directory/'design_frozen.json', {'config':config,
              'source_sha256':hashlib.sha256((ROOT/'strength_v5.py').read_bytes()).hexdigest()})
    mexc.save(directory/'universe_raw.json',{'fetched_server_time_ms':end,'data':info})
    mexc.save(directory/'tickers_raw.json',{'fetched_server_time_ms':end,'data':raw_tickers})
    mexc.save(directory/'selection.json',{'exchange':exchange,'run_id':run_id,'snapshot_server_time_ms':end,
              'closed_decision_ms':end//STEP*STEP,'crypto_usdt_universe':len(set(universe)),
              'prefilter_passed':len(chosen),'symbols':list(dict.fromkeys(['BTCUSDT']+chosen)),
              'rank_symbols':[s for s in chosen if s!='BTCUSDT']})
    adapter.download(directory)
    books = adapter.public_get('ticker/bookTicker')
    observed = adapter.public_get('time')['serverTime']
    mexc.save(directory/'book_tickers_raw.json',{'fetched_server_time_ms':observed,'data':books})
    return directory


def evaluate(exchange, directory, config, archive):
    selection = read_json(directory/'selection.json')
    decision = selection['closed_decision_ms']
    btc, audit = load_history(directory/'history'/'BTCUSDT.json')
    if audit['gaps'] or len(btc)<config['minimum_history_bars'] or int(btc.index[-1])+STEP != decision:
        raise ValueError('BTC history incomplete or stale')
    btc_return = (btc.close/btc.close.shift(6)-1)*100
    btc_return.attrs['return8'] = (btc.close/btc.close.shift(2)-1)*100
    book = read_json(directory/'book_tickers_raw.json')
    quotes = {x['symbol']:x for x in book['data']}
    rows, audits = [], []
    for symbol in selection['rank_symbols']:
        try:
            frame, audit = load_history(directory/'history'/f'{symbol}.json')
            segment = last_segment(frame)
            if len(segment)<config['minimum_history_bars'] or int(segment.index[-1])+STEP != decision:
                raise ValueError('insufficient contiguous history or stale last candle')
            row = normalized(model.features(segment,btc_return,config).iloc[-1])
            row.update(normalized(support_indicators.features(segment).iloc[-1]))
            row.update({'symbol':symbol,'exchange':exchange,'observed_ms':book['fetched_server_time_ms']})
            row['liquidity_band'] = 'main' if row['quote_volume24']>=config['rules']['main_liquidity_band_usdt24'] else 'thin'
            raw = quotes.get(symbol,{})
            try:
                bid, ask = float(raw['bidPrice']), float(raw['askPrice'])
                if not np.isfinite([bid,ask]).all() or not 0<bid<=ask: raise ValueError('invalid quote')
                mid = (bid+ask)/2
                row.update({'mid_price':mid,'spread_pct':(ask-bid)/mid*100})
            except (KeyError, ValueError, TypeError): row.update({'mid_price':None,'spread_pct':None})
            row['warnings'] = model.warnings(row,config)
            if any(group in row['matched_groups'] for group in ('early_reversal','sideways_volume','retest')):
                row['warnings'].append('deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi')
            if row['spread_pct'] is None: row['warnings'].append('alış/satış fiyatı doğrulanamadı')
            elif row['spread_pct']>config['warnings']['spread_above_pct']: row['warnings'].append('makas geniş')
            if row['mid_price'] is not None:
                if row['signal_reference_level'] is not None and row['mid_price']<row['signal_reference_level']:
                    row['warnings'].append('gözlem fiyatı grubun izlediği seviyenin altında')
                if row['atr'] and abs(row['mid_price']-row['close'])/row['atr']>config['warnings']['quote_drift_above_atr']:
                    row['warnings'].append('gözlem fiyatı kapanıştan uzaklaştı')
            row['failed_legacy_gates'] = [k[5:] for k,v in row.items() if k.startswith('gate_') and not v]
            rows.append(row);audits.append({'symbol':symbol,**audit,'contiguous_rows':len(segment)})
        except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
            audits.append({'symbol':symbol,'error':str(exc)})
    candidates = sorted([x for x in rows if x['qualified']], key=lambda r:(r['stage'],-r['strength_score'],r['symbol']))
    paper_watch.attach_context(candidates,rows,quotes)
    result = {'exchange':exchange,'archive':archive,'feature_cutoff_ms':decision,
              'observed_ms':book['fetched_server_time_ms'],'universe_count':selection['crypto_usdt_universe'],
              'prefilter_count':selection['prefilter_passed'],'analyzed_count':len(rows),'candidates':candidates,
              'limitation':'Archive uses v3-selected saved histories; v4-expanded live prefilter was NOT applied.' if archive else 'V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.'}
    folder = OUT/exchange/selection['run_id']
    mexc.save(folder/'all_snapshots.json',rows);mexc.save(folder/'audit.json',audits);mexc.save(folder/'summary.json',result)
    return result


def write_report(scans,archive):
    lines = ['# Coin Tarama 3 — erken dönüş / hacim / geri test','',
             '**Arşiv incelemesi; güncel canlı fiyat veya geçmişte gönderilmiş sinyal değildir.**' if archive else '**Deneysel canlı tarama; başarı üstünlüğü doğrulanmadı.**','',
             'V3 otomasyonu ve bildirimleri ayrı çalışır. Bu komut bildirim göndermez ve ileri dönem pilot kayıtlarını değiştirmez. Puan başarı olasılığı değildir.','']
    labels = model.LABELS
    lines+=['Üç ek grup birbirinin alternatifi: erken dönüş, yatay fiyat/hacim artışı, geri testte tutunma/SAR. Önceki yeni kırılım ve tutunma yolları da korunur. Bir token birden çok gruba uyabilir; bağımsız başarı gibi toplanmaz.','',
            '246 coinlik geçmiş kontrolünde bilinen tasarım örnekleri hariç yeni birleşim 1423, eski V4 724 olay üretti. Ölçülen 12s kapanış medyanı sırasıyla -%0,33 ve -%0,50; yeni birleşimin kontrol üstü medyan farkı -0,29 puan. Bu, kazanç veya üstünlük kanıtı değildir. Eski arşiv, canlı ön eleme ve işlem maliyetlerini tam temsil etmez.','',
            'Erken dönüşte önceki mum EMA20 altındayken üç mumluk yakın tepenin hacimle geri alınması aranır; yükselen EMA20 veya eski 20 mum tepesini aşması zorunlu değildir. Yatay hacim yükseliş onayı veya kesin toplama değildir. Geri testte sabit kırılım seviyesi, gerçek dönüş, dar taban, azalan hacim ve SAR alt konumu aranır.','']
    unique = set()
    for exchange,result in sorted(scans.items()):
        if 'error' in result:
            lines += [f"{exchange}: HATA — {result['error']}",''];continue
        lines += [f"{exchange}: incelenen {result['analyzed_count']}, aday {len(result['candidates'])}; kapanış {mexc.local_time(result['feature_cutoff_ms'])} TR; fiyat gözlemi {mexc.local_time(result['observed_ms'])} TR.",
                  result['limitation'],'', '| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |', '|---|---|---:|---:|---|---|']
        for row in result['candidates']:
            unique.add(row['symbol'])
            pu='RSI PU teyitli' if row.get('pu_active') else 'Yok'
            groups=', '.join(labels[name] for name in row['matched_groups'])
            lines.append(f"| {row['symbol']} | {groups} | {row['return24_pct']:.2f} | {row['signal_volume_ratio']:.2f} | {pu} | {'; '.join(row['warnings']) or 'Ek eşik uyarısı yok'} |")
        lines += ['']
    lines += [f'İki borsada toplam {len(unique)} farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.','',
              'Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.','']
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'report.md').write_text('\n'.join(lines),encoding='utf-8')
    mexc.save(OUT/'summary.json',{'archive':archive,'scans':scans,'unique_symbols':len(unique)})


def run(archive):
    config = read_json(ROOT/'strength_v5_config.json')
    def collect(exchange):
        adapter = mexc if exchange=='MEXC' else okx
        directory = adapter.selected_directory(None) if archive else snapshot(exchange,config)
        return evaluate(exchange,directory,config,archive)
    scans = {}
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs = {pool.submit(collect,e):e for e in ['MEXC','OKX']}
        for job in as_completed(jobs):
            try: scans[jobs[job]] = job.result()
            except Exception as exc: scans[jobs[job]] = {'error':str(exc)}
    write_report(scans,archive)
    print(json.dumps({'archive':archive,'exchanges':{e:({'error':r['error']} if 'error' in r else {'analyzed':r['analyzed_count'],'candidates':len(r['candidates'])}) for e,r in scans.items()}},ensure_ascii=False))
    return any('error' in result for result in scans.values())


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive',action='store_true',help='Use saved v3 histories; no network or alerts.')
    parser.add_argument('--live',action='store_true',help='Read public exchange data into separate v4 files; no alerts.')
    args = parser.parse_args()
    if args.archive == args.live: parser.error('Choose exactly one of --archive or --live.')
    raise SystemExit(1 if run(args.archive) else 0)
