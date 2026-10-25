"""Shared prospective measurements for independent GitHub scanner versions.

First actual quote per venue/symbol/version; no retrospective entries or orders.
The first closed minute at/after each exact 12/24/48h target is the endpoint.
"""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
import math

import numpy as np

import momentum_scan as mexc
import okx_scan as okx

VERSION = 'github-paper-v1'
HOURS = (12, 24, 48)
MINUTE = 60000


def midpoint(raw):
    try:
        bid, ask = float(raw['bidPrice']), float(raw['askPrice'])
        return (bid+ask)/2 if np.isfinite([bid,ask]).all() and 0<bid<=ask else None
    except (KeyError, TypeError, ValueError): return None


def attach_context(candidates, snapshots, quotes):
    pool = [r for r in snapshots if not r['qualified'] and r.get('gate_liquidity')
            and r['symbol']!='BTCUSDT' and r.get('atr',0)>0 and r.get('close',0)>0
            and midpoint(quotes.get(r['symbol'],{})) is not None]
    for row in candidates:
        candidates_for_control = [r for r in pool if r['symbol']!=row['symbol']]
        def distance(other):
            return (abs(math.log(other['quote_volume24']/row['quote_volume24'])) +
                    abs(math.log((other['atr']/other['close'])/(row['atr']/row['close']))),other['symbol'])
        controls = sorted(candidates_for_control,key=distance)[:3]
        row['paper_controls'] = [{'symbol':r['symbol'],'entry_price':midpoint(quotes[r['symbol']])} for r in controls]
        row['paper_btc_price'] = midpoint(quotes.get('BTCUSDT',{}))


def register(state, scans):
    paper = state.setdefault('paper',{'version':VERSION,'entries':{},'measurement_errors':[]})
    if paper['version']!=VERSION: raise ValueError('Paper measurement design changed; use a new version branch.')
    for venue,scan in scans.items():
        if 'error' in scan: continue
        for row in scan['candidates']:
            key = venue+':'+row['symbol']
            stage = row.get('stage','new_breakout')
            if key in paper['entries']:
                entry = paper['entries'][key]
                if stage!=entry['stages'][-1]['stage']:
                    entry['stages'].append({'stage':stage,'observed_ms':row['observed_ms'],'price':row.get('mid_price')})
                continue
            price, btc = row.get('mid_price'), row.get('paper_btc_price')
            if price is None or btc is None or not np.isfinite([price,btc]).all() or min(price,btc)<=0:
                continue # Retry only at a future real observation; never backdate a missing quote.
            paper['entries'][key] = {'symbol':row['symbol'],'exchange':venue,'observed_ms':row['observed_ms'],
                  'entry_price':price,'btc_entry_price':btc,'controls':row.get('paper_controls',[]),
                  'pu_at_entry':bool(row.get('pu_active',False)),'rsi14_at_entry':row.get('rsi14'),
                  'initial_stage':stage,'stages':[{'stage':stage,'observed_ms':row['observed_ms'],'price':price}],
                  'outcomes':{}}
    return paper


def endpoint_price(venue,symbol,endpoint):
    start = endpoint-MINUTE
    if venue=='MEXC':
        rows = mexc.public_get(f'klines?symbol={symbol}&interval=1m&startTime={start}&endTime={endpoint-1}&limit=1')
    else:
        rows,_ = okx.fetch_rows(symbol,'1m',start,endpoint-1)
    for row in rows:
        if int(row[0])==start:
            value = float(row[4])
            if np.isfinite(value) and value>0: return value
    return None


def refresh(state, asof, fetcher=endpoint_price):
    paper = state.get('paper')
    if not paper: return
    def update_venue(venue):
        cache, errors = {}, []
        def price(symbol,endpoint):
            key = (symbol,endpoint)
            if key not in cache:
                try: cache[key] = fetcher(venue,symbol,endpoint)
                except Exception as exc:
                    cache[key] = None
                    errors.append({'exchange':venue,'symbol':symbol,'endpoint_ms':endpoint,'error':str(exc)})
            return cache[key]
        for entry in paper['entries'].values():
            if entry['exchange']!=venue: continue
            for hours in HOURS:
                target = entry['observed_ms']+hours*3600000
                endpoint = int(math.ceil(target/MINUTE)*MINUTE)
                previous = entry['outcomes'].get(str(hours),{})
                if asof<endpoint or previous.get('complete'): continue
                coin_price = price(entry['symbol'],endpoint)
                btc_price = price('BTCUSDT',endpoint)
                controls = [price(c['symbol'],endpoint) for c in entry['controls']]
                ret = None if coin_price is None else (coin_price/entry['entry_price']-1)*100
                btc_ret = None if btc_price is None else (btc_price/entry['btc_entry_price']-1)*100
                all_controls = len(controls)==3 and all(p is not None for p in controls)
                control_ret = float(np.median([(p/c['entry_price']-1)*100 for p,c in zip(controls,entry['controls'])])) if all_controls else None
                entry['outcomes'][str(hours)] = {'target_ms':target,'endpoint_ms':endpoint,
                    'endpoint_delay_ms':endpoint-target,'endpoint_price':coin_price,'return_pct':ret,
                    'btc_excess_pct_points':None if ret is None or btc_ret is None else ret-btc_ret,
                    'control_excess_pct_points':None if ret is None or control_ret is None else ret-control_ret,
                    'complete':coin_price is not None and btc_price is not None and all(p is not None for p in controls),
                    'controls_count':len(controls)}
        return errors
    venues = sorted({e['exchange'] for e in paper['entries'].values()})
    with ThreadPoolExecutor(max_workers=2) as executor:
        errors = list(executor.map(update_venue,venues))
    paper['measurement_errors'] = [item for group in errors for item in group]
    paper['asof_ms'] = asof


def summary(state):
    entries = list(state.get('paper',{}).get('entries',{}).values())
    result = {'unique_symbols':len({e['symbol'] for e in entries}),'venue_records':len(entries),'by_exchange':{}}
    for venue in sorted({e['exchange'] for e in entries}):
        subset = [e for e in entries if e['exchange']==venue]
        stats = {}
        for hours in HOURS:
            outcomes = [e['outcomes'].get(str(hours),{}) for e in subset]
            def median(field):
                values = [o[field] for o in outcomes if o.get(field) is not None]
                return float(np.median(values)) if values else None
            stats[str(hours)] = {'available':sum(o.get('return_pct') is not None for o in outcomes),
                  'btc_available':sum(o.get('btc_excess_pct_points') is not None for o in outcomes),
                  'controls_available':sum(o.get('control_excess_pct_points') is not None for o in outcomes),
                  'median_return_pct':median('return_pct'),'median_btc_excess_pct_points':median('btc_excess_pct_points'),
                  'median_control_excess_pct_points':median('control_excess_pct_points')}
        result['by_exchange'][venue] = {'entries':len(subset),'horizons':stats}
    return result


def render(state):
    from momentum_scan import local_time
    stats = summary(state)
    entries = state.get('paper',{}).get('entries',{})
    def number(value): return '—' if value is None else f'{value:.2f}'
    lines = ['','## Gerçek gözlemden sonraki ölçümler','',
             'Her sürüm ve borsanın ilk gerçek alış/satış orta fiyatı ayrı kaydedilir. Aynı coin grup değiştirse de yeni bağımsız örnek sayılmaz. Hedef saatten sonraki ilk dakika kapanışı kullanılır; gecikme 60 saniyeden küçüktür. Ücret/kayma dahil net kâr değildir. Henüz oluşmamış veya eksik ölçümler boş kalır.','',
             f"{stats['venue_records']} borsa kaydı, {stats['unique_symbols']} farklı sembol. Ortak semboller iki bağımsız başarı gibi toplanmaz.",'',
             '| Borsa | Süre | Ölçülen | Medyan % | BTC üstü puan | Kontrol üstü puan | Kontrol ölçülen |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for venue,item in stats['by_exchange'].items():
        for hours,h in item['horizons'].items():
            lines.append(f"| {venue} | {hours}s | {h['available']}/{item['entries']} | {number(h['median_return_pct'])} | {number(h['median_btc_excess_pct_points'])} | {number(h['median_control_excess_pct_points'])} | {h['controls_available']} |")
    lines += ['', '| Coin | Borsa | İlk grup | Gerçek gözlem TR | Referans fiyat | 12s % | 24s % | 48s % |',
              '|---|---|---|---|---:|---:|---:|---:|']
    for key,entry in sorted(entries.items()):
        values = [number(entry['outcomes'].get(str(h),{}).get('return_pct')) for h in HOURS]
        stage = 'Tutunma' if entry['initial_stage']=='continuation' else 'Yeni kırılım'
        lines.append(f"| {entry['symbol']} | {entry['exchange']} | {stage} | {local_time(entry['observed_ms'])} | {entry['entry_price']:.8g} | {' | '.join(values)} |")
    errors = state.get('paper',{}).get('measurement_errors',[])
    if errors: lines += ['',f"Bu döngüde {len(errors)} ölçüm isteğinde erişim/veri hatası oluştu; eksikler sonraki çalışmada yeniden denenir."]
    lines += ['', 'Karşılaştırma için en az 1–2 haftalık gerçek kayıt beklenir. Gruplar, borsalar ve ortak coinler dikkate alınmadan bir kazanma oranı iddia edilmez.','']
    return '\n'.join(lines)
