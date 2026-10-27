"""Silent, frozen, prospective comparison. Never changes production selections or messages."""
from __future__ import annotations
import argparse,hashlib,json,math,time
from copy import deepcopy
from pathlib import Path
from statistics import median
import short_squeeze as production
import short_squeeze_scan as scanner
import strength_v5_priority as priority
import momentum_scan as mexc
import okx_scan as okx
from short_squeeze_sources import num,recent

ROOT=Path(__file__).parent
CONFIG=ROOT/'short_squeeze_lab_config.json'
SECTION='<!-- shortcu-comparison:start -->'
MINUTE=60000
ARMS={'A':'Teknik temel + ortak vadeli işlem koşulları',
      'B':'A + negatif fonlama', 'C':'A + OI artışı ve fiyat tutunması',
      'D':'A + fonlama + OI/fiyat birlikte'}
UNKNOWN={'warming','funding_unknown','market_data_unknown','btc_context_unknown','not_listed'}
COMMON_FAILURES={'futures_spread','oi_liquidity','basis'}


def now_ms():return int(time.time()*1000)
def load_config():return json.loads(CONFIG.read_text(encoding='utf-8'))
def fingerprint():
    h=hashlib.sha256()
    for path in (Path(__file__),CONFIG):
        h.update(path.name.encode());h.update(path.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    h.update(production.fingerprint().encode())
    return h.hexdigest()
def protected(state):return hashlib.sha256(json.dumps({k:v for k,v in state.items() if k!='comparison_lab'},sort_keys=True,allow_nan=False).encode()).hexdigest()


def lab_state(state):
    lab=state.setdefault('comparison_lab',{'version':'shortcu-comparison-v1','fingerprint':fingerprint(),'cases':{},'errors':[]})
    if lab['fingerprint']!=fingerprint():raise ValueError('Comparison rules changed; explicit new cohort required')
    return lab


def copied_quotes(decisions):
    grouped={}
    for d in decisions:
        row=deepcopy(d['row']);v=row['exchange']
        grouped.setdefault(v,{'feature_cutoff_ms':row['feature_cutoff_ms'],'candidates':[]})['candidates'].append(row)
    return priority.refresh_quotes(grouped)


def membership(decision,stamp,cfg):
    reasons=set(decision.get('reasons',[]));metrics=decision.get('metrics',{})
    if reasons & UNKNOWN or reasons & COMMON_FAILURES:return None
    required=('funding_scaled_8h','oi_change_pct','futures_price_change_pct','elapsed_hours','baseline_ms','futures_mid')
    if any(num(metrics.get(k)) is None for k in required):return None
    if not isinstance(metrics.get('contract'),str) or metrics['futures_mid']<=0:return None
    for name in ('futures_observed_ms','funding_observed_ms'):
        if not recent(metrics.get(name),stamp,cfg['maximum_derivative_age_minutes']):return None
    # All factor states must be known BEFORE entering the shared cohort.
    p=json.loads(production.CONFIG.read_text(encoding='utf-8'))
    negative=metrics['funding_scaled_8h']<=p['funding_scaled_8h_max']
    oi=metrics['oi_change_pct']>=p['oi_change_min_pct']
    held=p['futures_price_change_min_pct']<=metrics['futures_price_change_pct']<=p['futures_price_change_max_pct']
    return {'A':True,'B':negative,'C':oi and held,'D':negative and oi and held}


def register(lab,decisions,fresh,cfg,stamp):
    policy=json.loads(priority.CONFIG.read_text(encoding='utf-8'));lookup={}
    for venue,result in fresh.items():
        if 'error' in result:continue
        for row in result.get('candidates',[]):
            row=deepcopy(row);row['feature_cutoff_ms']=result['feature_cutoff_ms'];row['exchange']=venue
            reasons,_=priority.reasons_for(row,policy,stamp)
            if not reasons:lookup[(venue,row['symbol'])]=row
    eligible=[];skipped={}
    for decision in decisions:
        label=decision['symbol']
        if label in lab['cases']:continue
        arms=membership(decision,stamp,cfg)
        row=lookup.get((decision['exchange'],label))
        if arms is None:skipped['factor_unknown_or_common_failure']=skipped.get('factor_unknown_or_common_failure',0)+1;continue
        if row is None:skipped['fresh_technical_quote_missing']=skipped.get('fresh_technical_quote_missing',0)+1;continue
        btc=num(row.get('paper_btc_price'))
        if btc is None or btc<=0:skipped['btc_reference_missing']=skipped.get('btc_reference_missing',0)+1;continue
        # Cross-source observations must still be reasonably simultaneous.
        if abs(row['observed_ms']-decision['metrics']['futures_observed_ms'])>cfg['maximum_derivative_age_minutes']*MINUTE:
            skipped['source_time_mismatch']=skipped.get('source_time_mismatch',0)+1;continue
        basis=abs(decision['metrics']['futures_mid']/row['mid_price']-1)*100
        p=json.loads(production.CONFIG.read_text(encoding='utf-8'))
        if basis>p['maximum_spot_futures_basis_pct']:skipped['current_basis_widened']=skipped.get('current_basis_widened',0)+1;continue
        eligible.append((row,decision,arms))
    # Venue selection does not depend on the factor verdict or future returns.
    eligible.sort(key=lambda x:(x[0]['spread_pct'],-x[0]['quote_volume24'],x[0]['exchange'],x[0]['symbol']))
    added=[]
    for row,decision,arms in eligible:
        if row['symbol'] in lab['cases']:continue
        if len(lab['cases'])>=cfg['max_unique_cases'] or len(added)>=cfg['max_new_cases_per_run']:break
        controls=[];seen=set()
        for control in row.get('paper_controls',[]):
            value=num(control.get('entry_price'));symbol=control.get('symbol')
            if symbol in seen or symbol==row['symbol'] or value is None or value<=0:continue
            controls.append({'symbol':symbol,'entry_price':value});seen.add(symbol)
        index=len(lab['cases'])+1
        case={'symbol':row['symbol'],'exchange':row['exchange'],'contract':decision['metrics']['contract'],
            'observed_ms':row['observed_ms'],'entry_price':row['mid_price'],'btc_entry_price':row['paper_btc_price'],
            'controls':controls[:3],'arms':arms,'factor_metrics':deepcopy(decision['metrics']),
            'cohort_index':index,'split':'first25' if index<=cfg['discovery_first_cases'] else 'next25',
            'feature_cutoff_ms':row['feature_cutoff_ms'],
            'source_lag_minutes':(row['observed_ms']-row['feature_cutoff_ms'])/MINUTE,
            'entry_spread_pct':row['spread_pct'],'outcomes':{}}
        lab['cases'][row['symbol']]=case;added.append(row['symbol'])
    lab['registration']={'observed_ms':stamp,'added':added,'skipped':skipped,
        'quote_errors':{v:r['error'] for v,r in fresh.items() if 'error' in r}}
    return added


def fetch_minutes(venue,symbol,start,end):
    """Documented public historical candles, [start,end); at most 48h per case."""
    if end<=start or end-start>48*3600000:raise ValueError('Minute window outside comparison budget')
    if venue=='OKX':
        rows,_=okx.fetch_rows(symbol,'1m',start,end-1)
        # The existing adapter already filters confirm=1 and normalizes 9 raw
        # fields into the research 8-field format. Do not filter it as raw data.
        if any(len(r)!=8 for r in rows):raise ValueError('Unexpected normalized OKX minute schema')
        return rows
    if venue!='MEXC':raise ValueError('Unknown venue')
    result=[];cursor=start
    for _ in range(4):
        rows=mexc.public_get(f'klines?symbol={symbol}&interval=1m&startTime={cursor}&endTime={end-1}&limit=1000')
        if not isinstance(rows,list):raise ValueError('Unexpected minute response')
        if not rows:break
        result+=rows;latest=max(int(r[0]) for r in rows)
        if latest<cursor:raise ValueError('Minute pagination did not advance')
        cursor=latest+MINUTE
        if cursor>=end:break
    return result


def candles(rows,start,end,stamp):
    result={}
    for raw in rows:
        if not isinstance(raw,list) or len(raw)<6:raise ValueError('Unexpected minute schema')
        opening=num(raw[0]);values=[num(v) for v in raw[1:6]]
        if opening is None or opening!=int(opening) or int(opening)%MINUTE or any(v is None for v in values):raise ValueError('Invalid minute values')
        opening=int(opening);o,h,l,c,v=values
        if min(o,h,l,c)<=0 or v<0 or h<max(o,l,c) or l>min(o,h,c):raise ValueError('Invalid minute OHLCV')
        if not start<=opening<end or opening+MINUTE>stamp:continue
        row={'open_ms':opening,'open':o,'high':h,'low':l,'close':c}
        if opening in result and result[opening]!=row:raise ValueError('Conflicting duplicate minute')
        result[opening]=row
    return result


def update_case(case,cfg,stamp,fetcher):
    due=[]
    for h in cfg['horizons_hours']:
        endpoint=int(math.ceil((case['observed_ms']+h*3600000)/MINUTE)*MINUTE)
        if stamp>=endpoint and not case['outcomes'].get(str(h),{}).get('complete'):due.append((h,endpoint))
    if not due:return False
    start=int(math.ceil(case['observed_ms']/MINUTE)*MINUTE);end=max(t for _,t in due)
    series=candles(fetcher(case['exchange'],case['symbol'],start,end),start,end,stamp)
    def endpoint_price(symbol,endpoint):
        bars=candles(fetcher(case['exchange'],symbol,endpoint-MINUTE,endpoint),endpoint-MINUTE,endpoint,stamp)
        return bars.get(endpoint-MINUTE,{}).get('close')
    for hours,endpoint in due:
        target=case['observed_ms']+hours*3600000
        price=series.get(endpoint-MINUTE,{}).get('close')
        ret=None if price is None else (price/case['entry_price']-1)*100
        path=[series[t] for t in range(start,endpoint,MINUTE) if t in series]
        full=len(path)==(endpoint-start)//MINUTE and bool(path)
        btc=endpoint_price('BTCUSDT',endpoint)
        btc_ret=None if btc is None else (btc/case['btc_entry_price']-1)*100
        controls=[endpoint_price(c['symbol'],endpoint) for c in case['controls']]
        control_ret=median([(p/c['entry_price']-1)*100 for p,c in zip(controls,case['controls'])]) if len(controls)==3 and all(p is not None for p in controls) else None
        complete=ret is not None and btc_ret is not None and full and (len(case['controls'])!=3 or control_ret is not None)
        case['outcomes'][str(hours)]={'target_ms':target,'endpoint_ms':endpoint,'endpoint_delay_ms':endpoint-target,
            'endpoint_price':price,'return_pct':ret,'btc_excess_pct_points':None if ret is None or btc_ret is None else ret-btc_ret,
            'control_excess_pct_points':None if ret is None or control_ret is None else ret-control_ret,
            'mae_pct':min(0.,(min(b['low'] for b in path)/case['entry_price']-1)*100) if full else None,
            'mfe_pct':max(0.,(max(b['high'] for b in path)/case['entry_price']-1)*100) if full else None,
            'path_complete':full,'minute_bars':len(path),'range_start_ms':start,
            'ignored_entry_fragment_ms':start-case['observed_ms'],'complete':complete,
            'cost_scenarios_pct':{str(cost):None if ret is None else ret-cost for cost in cfg['round_trip_cost_scenarios_pct']},
            'measured_ms':stamp}
    return True


def measure(lab,cfg,stamp,fetcher=fetch_minutes):
    cache={};errors=[]
    def cached(venue,symbol,start,end):
        key=(venue,symbol,start,end)
        if key not in cache:cache[key]=fetcher(venue,symbol,start,end)
        return cache[key]
    pending=[]
    for case in lab['cases'].values():
        if any(stamp>=math.ceil((case['observed_ms']+h*3600000)/MINUTE)*MINUTE and not case['outcomes'].get(str(h),{}).get('complete') for h in cfg['horizons_hours']):
            pending.append(case)
    pending.sort(key=lambda c:(c.get('last_measure_attempt_ms',0),c['observed_ms']))
    for case in pending[:cfg['max_cases_measured_per_run']]:
        case['last_measure_attempt_ms']=stamp
        try:update_case(case,cfg,stamp,cached)
        except Exception as exc:errors.append({'symbol':case['symbol'],'exchange':case['exchange'],'error':str(exc)})
    lab['errors']=errors;lab['measurement']={'observed_ms':stamp,'pending':len(pending),'attempted':min(len(pending),cfg['max_cases_measured_per_run']),'unique_reads':len(cache)}


def summarize(lab,cfg,hours=None,split=None):
    h=str(hours or cfg['primary_horizon_hours']);result={}
    for arm in ARMS:
        cases=[c for c in lab['cases'].values() if c['arms'].get(arm) and (split is None or c['split']==split)]
        outcomes=[c['outcomes'][h] for c in cases if c['outcomes'].get(h,{}).get('complete')]
        def med(field):
            values=[o[field] for o in outcomes if num(o.get(field)) is not None]
            return median(values) if values else None
        result[arm]={'cases':len(cases),'measured':len(outcomes),'median_return_pct':med('return_pct'),
            'median_btc_excess_pct_points':med('btc_excess_pct_points'),'median_controls_excess_pct_points':med('control_excess_pct_points'),
            'control_comparisons':sum(o.get('control_excess_pct_points') is not None for o in outcomes),
            'median_mae_pct':med('mae_pct'),'median_mfe_pct':med('mfe_pct'),
            'positive_after_cost_fraction':{str(cost):sum(o['return_pct']>cost for o in outcomes)/len(outcomes) if outcomes else None for cost in cfg['round_trip_cost_scenarios_pct']},
            'enough_for_initial_review':len(outcomes)>=cfg['minimum_arm_complete_for_review']}
    return result


def append_report(state,cfg):
    lab=state['comparison_lab'];path=scanner.OUT/'report.md'
    original=path.read_text(encoding='utf-8').split(SECTION,1)[0].rstrip()
    stats=summarize(lab,cfg)
    def val(value):return '—' if value is None else f'{value:+.2f}'
    lines=[SECTION,'','## Ücretsiz karşılaştırmalı deney — sessiz ölçüm','',
        f"Aynı ilk uygun gözlemde en çok {cfg['max_unique_cases']} farklı sembol. Şu an {len(lab['cases'])} kayıt. Bildirim eklenmez; mevcut Shortçu Kıstır kuralları ve eski fiyatlar korunur.",'',
        'Aynı anda tüm faktörler biliniyorsa kayda alınır. Eksik OI geçmişi, fonlama veya fiyat bilinmiyor kalır; olumsuz koşula veya 0 puana dönüştürülmez. Aynı sembol iki borsada iki bağımsız örnek sayılmaz.','',
        '| Grup | Koşul | Kayıt | Ölçülen 12s | Medyan % | BTC üstü puan | Kontrol üstü puan | Girişe göre dip % | Girişe göre tepe % |',
        '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for arm,label in ARMS.items():
        s=stats[arm];lines.append(f"| {arm} | {label} | {s['cases']} | {s['measured']} | {val(s['median_return_pct'])} | {val(s['median_btc_excess_pct_points'])} | {val(s['median_controls_excess_pct_points'])} | {val(s['median_mae_pct'])} | {val(s['median_mfe_pct'])} |")
    lines+=['','**Henüz üstünlük/başarı iddiası yok.** Ana karşılaştırma 12 saat; 6/24/48 saat ikincildir. Gruplar örtüşür, grup sayıları toplanarak bağımsız başarı hesaplanmaz. A da aynı borsada geçerli perpetual/likidite/makas/fiyat farkı şartlarına tabidir; bütün spot piyasanın kontrol grubu değildir.','',
        'Aynı başlangıç fiyatındaki koşullu karşılaştırmadır; bir coin saatler sonra yeni bir şartı sağladığında geriye dönük grup değiştirilmez. Bu nedenle D, mevcut üretim sinyallerinin tümünün birebir kopyası değildir; ilk ortak uygun gözlemde birlikte sağlanan koşulları ölçer. Üretimin kendi gerçek sinyal ölçümleri yukarıda ayrıca sürer.','',
        f"Her grupta en az {cfg['minimum_arm_complete_for_review']} tamamlanmış gözlem olmadan ilk değerlendirme yapılmaz. İlk 25 / sonraki 25 kayıt ayrı tutulur; dönem arasında sonuçlara bakıp eşik değiştirilmez. Bunlar istatistiksel kesinlik veya bağımsız piyasa rejimleri anlamına gelmez.",'',
        'Maliyet duyarlılığı (gerçek gerçekleşme/net kâr değildir): gidiş-dönüş %0.2 / %0.5 / %1 toplam maliyet varsayımı getiriden ayrı düşülür. Sabit maliyet senaryosu gerçek hesap komisyonu, kayma, vergi veya vadeli fonlamanın ölçüldüğü anlamına gelmez.','',
        '| Grup | Ölçülen | %0.2 maliyet sonrası pozitif | %0.5 sonrası | %1 sonrası |','|---|---:|---:|---:|---:|']
    for arm,s in stats.items():
        values=['—' if s['positive_after_cost_fraction'][str(cost)] is None else f"%{s['positive_after_cost_fraction'][str(cost)]*100:.1f}" for cost in cfg['round_trip_cost_scenarios_pct']]
        lines.append(f"| {arm} | {s['measured']} | {' | '.join(values)} |")
    lines+=['','Ölçüm: girişten sonraki ilk TAM 1dk mumdan hedefin ilk dakika kapanışına kadar. Giriş mumunun kalan <1 dakikası dip/tepe hesabına dahil edilmez; tam işlem aralığının mutlak tepe/dibi olduğu iddia edilmez. Eksik ara mum varsa dip/tepe bilinmiyor; eksik sonuçlar sıfır getiri sayılmaz.','',
        '## Deneyin gerçek gözlem kayıtları','',
        '| No | Coin | Borsa | Grup üyelikleri | Gerçek gözlem TR | Spot referans | Kaynak kapanışından gecikme dk |','|---:|---|---|---|---|---:|---:|']
    for c in lab['cases'].values():lines.append(f"| {c['cohort_index']} | {c['symbol']} | {c['exchange']} | {','.join(k for k,v in c['arms'].items() if v)} | {scanner.cloud.time_label(c['observed_ms'])} | {c['entry_price']:.8g} | {c['source_lag_minutes']:.1f} |")
    lines+=['','Dış likidasyon haritası / büyük yatırımcı pozisyon oranı API bağlantısı yok; bu alanlar hesaplanmış veya doğrulanmış kabul edilmez. Ücretsiz deney mevcut kamu verisinin katkısını sınar. Dört saatlik teknik kaynak ve GitHub gecikmesi hızlı squeeze hareketlerini kaçırabilir; gecikme yukarıda kayıtlıdır.','',
        'Son kayıt elemesi: '+json.dumps(lab.get('registration',{}).get('skipped',{}),ensure_ascii=False),
        'Fiyat kaynağı hataları: '+json.dumps(lab.get('registration',{}).get('quote_errors',{}),ensure_ascii=False),
        f"Ölçüm erişim/veri hatası: {len(lab['errors'])}.",'']
    path.write_text(original+'\n\n'+'\n'.join(lines),encoding='utf-8')


def observe():
    cfg=load_config();state=json.loads(scanner.STATE.read_text(encoding='utf-8'))
    if state['rules_fingerprint']!=production.fingerprint():raise ValueError('Production design mismatch')
    before=protected(state);lab=lab_state(state);decisions=state['latest']['decisions']
    fresh=copied_quotes(decisions);stamp=now_ms();added=register(lab,decisions,fresh,cfg,stamp)
    measure(lab,cfg,stamp);lab['updated_ms']=stamp
    lab['summaries']={str(h):summarize(lab,cfg,h) for h in cfg['horizons_hours']}
    lab['split_summaries']={s:summarize(lab,cfg,split=s) for s in ('first25','next25')}
    assert protected(state)==before,'Original production fields must remain unchanged'
    scanner.cloud.save(scanner.STATE,state);append_report(state,cfg)
    scanner.cloud.save(scanner.OUT/'comparison_summary.json',{'cases':len(lab['cases']),'added':added,'summaries':lab['summaries'],
        'registration':lab['registration'],'measurement':lab['measurement'],'errors':lab['errors']})
    print(json.dumps({'comparison_cases':len(lab['cases']),'new_cases':len(added),'production_fields_preserved':True,
        'measurement_errors':len(lab['errors']),'quote_errors':lab['registration']['quote_errors']}))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['observe','check-status']);args=parser.parse_args();scanner.configure()
    if args.phase=='observe':observe()
    else:
        state=json.loads(scanner.STATE.read_text(encoding='utf-8'));lab=lab_state(state)
        raise SystemExit(1 if lab['errors'] or lab.get('registration',{}).get('quote_errors') else 0)
