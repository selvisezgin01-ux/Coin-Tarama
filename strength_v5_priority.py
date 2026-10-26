"""At most five unique priority symbols; preserve the underlying broad experiment."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import time
from concurrent.futures import ThreadPoolExecutor
import strength_v5_watch as watch
import strength_v5 as model
import paper_watch
from study_dataset import STEP,read_json

ROOT=Path(__file__).resolve().parent
CONFIG=ROOT/'strength_v5_priority_config.json'
RAW_START='<!-- coin-priority-raw:start -->'
RAW_END='<!-- coin-priority-raw:end -->'
REASONS={'volume':'hacim 100.000 USDT altında','spread':'makas geniş veya bilinmiyor',
 'structure_lost':'izlenen seviye kaybedilmiş veya bilinmiyor','quote_drift':'güncel fiyat kapanıştan uzak veya veri eksik',
 'extension':'EMA20 uzaklığı fazla veya bilinmiyor','risk_distance':'yapı bozulma mesafesi geniş veya bilinmiyor',
 'preparation_only':'yalnız hazırlık; ek teknik teyit yok','known_equity':'tanınan tokenleştirilmiş hisse',
 'extreme_volume':'olağandışı hacim katsayısı; ayrıca inceleme','quote_age':'güncel fiyat gözlemi eski veya bilinmiyor',
 'decision_stale':'son kapalı 4s kararına ait değil','invalid_data':'geçersiz fiyat/oynaklık verisi'}


def now_ms():return int(time.time()*1000)
def num(value):
    if isinstance(value,bool):return None
    try:
        value=float(value);return value if math.isfinite(value) else None
    except (TypeError,ValueError):return None


def fingerprint():
    h=hashlib.sha256()
    for path in (Path(__file__),CONFIG):
        h.update(path.name.encode());h.update(path.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return h.hexdigest()


def priority_state(state):
    p=state.setdefault('priority_watch',{'version':1,'fingerprint':fingerprint(),'active':[],
        'active_venues':{},'last_sent':{},'pending':[],'suppressed_raw_batches':[]})
    if p['fingerprint']!=fingerprint():raise ValueError('Priority policy changed; explicit migration required')
    return p


def reasons_for(row,config,asof):
    reasons=[];price=num(row.get('mid_price'));atr=num(row.get('atr'));close=num(row.get('close'))
    level=num(row.get('signal_reference_level'));invalid=num(row.get('signal_invalidation_level'));ema=num(row.get('ema20'))
    volume=num(row.get('quote_volume24'));spread=num(row.get('spread_pct'));ratio=num(row.get('signal_volume_ratio'))
    observed=num(row.get('observed_ms'));cutoff=num(row.get('feature_cutoff_ms'))
    if not all(x is not None and x>0 for x in (price,atr,close,ema)):reasons.append('invalid_data')
    if volume is None or volume<config['minimum_quote_volume24_usdt']:reasons.append('volume')
    if spread is None or not 0<=spread<=config['maximum_spread_pct']:reasons.append('spread')
    if price is None or level is None or level<=0 or price<level:reasons.append('structure_lost')
    if price is None or close is None or atr is None or atr<=0 or abs(price-close)/atr>config['maximum_quote_drift_atr']:reasons.append('quote_drift')
    if price is None or ema is None or atr is None or atr<=0 or (price-ema)/atr>config['maximum_current_ema20_extension_atr']:reasons.append('extension')
    risk=(1-invalid/price)*100 if price is not None and price>0 and invalid is not None else None
    if risk is None or not 0<risk<=config['maximum_current_structure_distance_pct']:reasons.append('risk_distance')
    if observed is None or not -60000<=asof-observed<=config['maximum_quote_age_minutes']*60000:reasons.append('quote_age')
    if cutoff is None or cutoff!=asof//STEP*STEP:reasons.append('decision_stale')
    groups=set(row.get('matched_groups') or [])
    if not groups or not groups-set(config['preparation_only_groups']):reasons.append('preparation_only')
    base=row['symbol'][:-4] if row.get('symbol','').endswith('USDT') else ''
    if base in config['excluded_equity_bases'].get(row.get('exchange'),[]):reasons.append('known_equity')
    if ratio is None or ratio>config['extreme_volume_ratio_review_above']:reasons.append('extreme_volume')
    return reasons,{'current_structure_distance_pct':risk,
        'current_ema20_extension_atr':None if price is None or ema is None or atr is None or atr<=0 else (price-ema)/atr,
        'current_quote_drift_atr':None if price is None or close is None or atr is None or atr<=0 else abs(price-close)/atr}


def rank_key(row,config):
    return (-min(num(row['signal_volume_ratio']),config['volume_ratio_rank_cap']),
        -(num(row.get('close_position')) or 0),num(row['spread_pct']),-num(row['quote_volume24']),row['symbol'],row['exchange'])


def select(scans,config,asof):
    eligible=[];excluded=[];errors={};raw_count=0;symbols=set()
    for venue,result in scans.items():
        raw_count+=len(result.get('candidates',[]));symbols.update(r['symbol'] for r in result.get('candidates',[]))
        if 'error' in result:errors[venue]=result['error'];continue
        for original in result.get('candidates',[]):
            row=deepcopy(original);row['exchange']=venue
            row['feature_cutoff_ms']=result['feature_cutoff_ms']
            reasons,metrics=reasons_for(row,config,asof);row['priority_metrics']=metrics
            if reasons:excluded.append({'symbol':row['symbol'],'exchange':venue,'reasons':reasons})
            else:eligible.append(row)
    eligible.sort(key=lambda r:rank_key(r,config));unique={}
    for row in eligible:
        symbol=row['symbol']
        if symbol not in unique:unique[symbol]={'best':row,'passing_venues':[]}
        unique[symbol]['passing_venues'].append(row['exchange'])
    selected=[]
    for value in list(unique.values())[:config['max_unique_symbols']]:
        selected.append({**value['best'],'passing_venues':sorted(value['passing_venues'])})
    chosen={r['symbol'] for r in selected}
    return {'selected':selected,'eligible_rows':len(eligible),'eligible_unique':len(unique),'raw_rows':raw_count,
        'raw_unique':len(symbols),'excluded':excluded,'source_errors':errors,
        'ranked_but_not_selected':[s for s in unique if s not in chosen],'observed_ms':asof}


def refresh_quotes(scans):
    """Read public books afresh; never overwrite original core prices or references."""
    def refresh(item):
        venue,result=item
        if 'error' in result or not result.get('candidates'):return venue,deepcopy(result)
        try:
            adapter=watch.scanner.mexc if venue=='MEXC' else watch.scanner.okx
            books=adapter.public_get('ticker/bookTicker');stamp=int(adapter.public_get('time')['serverTime'])
            quotes={r['symbol']:r for r in books};copy=deepcopy(result)
            for row in copy['candidates']:
                quote=quotes.get(row['symbol'],{});price=paper_watch.midpoint(quote)
                bid=num(quote.get('bidPrice'));ask=num(quote.get('askPrice'))
                if bid is None or ask is None:price=None
                row['source_feature_observed_ms']=row['observed_ms'];row['observed_ms']=stamp;row['mid_price']=price
                row['spread_pct']=None if price is None else (ask-bid)/price*100
                row['paper_btc_price']=paper_watch.midpoint(quotes.get('BTCUSDT',{}))
                controls=[]
                for old in row.get('paper_controls',[]):
                    observed=paper_watch.midpoint(quotes.get(old['symbol'],{}))
                    if observed is not None:controls.append({'symbol':old['symbol'],'entry_price':observed})
                row['paper_controls']=controls
            copy['priority_quote_observed_ms']=stamp
            return venue,copy
        except Exception as exc:return venue,{**deepcopy(result),'error':str(exc),'priority_quote_refresh_failed':True}
    with ThreadPoolExecutor(max_workers=2) as executor:return dict(executor.map(refresh,scans.items()))


def observe(state,scans,config,asof):
    p=priority_state(state);result=select(scans,config,asof)
    old_active=set(p['active']);failed=set(result['source_errors'])
    preserved={s for s,v in p.get('active_venues',{}).items() if v in failed}
    # Unsent prior messages remain immutable for delivery reconciliation, not for stale delivery.
    for batch in p['pending']:batch['obsolete']=True
    fresh=[r for r in result['selected'] if r['symbol'] not in p['last_sent'] or
           (r['symbol'] not in old_active and asof-p['last_sent'][r['symbol']]>=config['notification_cooldown_hours']*3600000)]
    if fresh:
        identifier=hashlib.sha256(json.dumps([[r['symbol'],r['exchange'],r['observed_ms']] for r in fresh],sort_keys=True).encode()).hexdigest()[:24]
        p['pending'].append({'id':identifier,'created_ms':asof,'candidates':fresh,'obsolete':False})
    p['active']=sorted({r['symbol'] for r in result['selected']}|preserved)
    p['active_venues']={**{s:p['active_venues'][s] for s in preserved},**{r['symbol']:r['exchange'] for r in result['selected']}}
    for batch in state['pending']:
        p['suppressed_raw_batches'].append({'id':batch['id'],'created_ms':batch['created_ms'],
            'raw_candidates':len(batch['candidates']),'reason':'Priority-only notifications; full candidates and paper measurements retained'})
    p['suppressed_raw_batches']=p['suppressed_raw_batches'][-300:];state['pending']=[]
    p['latest']=result
    selected_scans={venue:{'candidates':[r for r in result['selected'] if r['exchange']==venue]} for venue in scans if venue not in failed}
    paper_watch.register(p,selected_scans);paper_watch.refresh(p,asof)
    return p


def describe(row):
    groups=', '.join(model.LABELS[g] for g in row['matched_groups'])
    risk=row['priority_metrics']['current_structure_distance_pct']
    return (f"{row['symbol']} · {row['exchange']}\nGruplar: {groups}\n"
        f"Gerçek fiyat gözlemi {watch.cloud.time_label(row['observed_ms'])} TR: {row['mid_price']:.8g}\n"
        f"24s kapalı mum hacmi {row['quote_volume24']:,.0f} USDT; hacim katsayısı {row['signal_volume_ratio']:.2f}x; makas %{row['spread_pct']:.2f}\n"
        f"Yapı bozulma referansına mesafe %{risk:.2f}. Piyasa koşulu ön elemesidir; bağımsız derinlik veya gerçekleşebilir zarar sınırı değildir.")


def render(state,config):
    p=state['priority_watch'];r=p['latest'];path=watch.cloud.OUT/'report.md';raw=path.read_text(encoding='utf-8')
    if RAW_START in raw:raw=raw.split(RAW_START,1)[1].split(RAW_END,1)[0].strip()
    lines=['# Coin Tarama 3 — kısa öncelik listesi','',f"Son kontrol: {watch.cloud.time_label(r['observed_ms'])} TR.",'',
        f"Geniş havuz: {r['raw_rows']} borsa kaydı / {r['raw_unique']} sembol. İşlem koşulu elemesini geçen: {r['eligible_unique']} farklı sembol. Bildirim ve üst liste: en fazla {config['max_unique_symbols']} farklı coin.",'',
        '**Öncelik, kârlılık veya güvenli işlem garantisi değildir.** Hacim/makas, güncel fiyat, yapı ve uzama kontrollerinden geçenler sıralanır. Yalnız yatay hacim hazırlığı bildirilmez. Aday yoksa liste doldurulmaz.','',
        '| Coin | Fiyat borsası | Geçen borsalar | Grup | Gerçek gözlem TR | Fiyat | Makas % | Yapı mesafesi % |',
        '|---|---|---|---|---|---:|---:|---:|']
    for row in r['selected']:
        lines.append(f"| {row['symbol']} | {row['exchange']} | {', '.join(row['passing_venues'])} | {', '.join(model.LABELS[g] for g in row['matched_groups'])} | {watch.cloud.time_label(row['observed_ms'])} | {row['mid_price']:.8g} | {row['spread_pct']:.2f} | {row['priority_metrics']['current_structure_distance_pct']:.2f} |")
    if not r['selected']:
        lines+=['','Veri eksikleri nedeniyle güncel öncelik listesi tam doğrulanamadı; bu, aday olmadığı anlamına gelmez.' if r['source_errors'] else 'Şu an öncelik koşullarını sağlayan aday yok.']
    lines+=['','Sıralama: en çok 4x sayılan göreli hacim, kapanış konumu, dar makas ve aynı borsanın hacmi. Farklı borsaların hacimleri toplanmaz. Bu sıra başarı olasılığı değildir.','',
        'Başlangıç elemesi: en az 100.000 USDT kapalı 24s hacim, en çok %0,5 makas, izlenen seviyeyi koruyan güncel fiyat, kapanıştan en çok 1 ATR uzaklık, EMA20 üstüne en çok 2,5 ATR uzama ve yapı referansına en çok %12 mesafe. 20x üzeri hacim ayrıca incelemede kalır. Bunlar daha iyi sonuç verdiği kanıtlanmış yeni strateji eşikleri değildir.','',
        'Aynı sembol tek satırda gösterilir; yalnız elemeden geçen borsalar listelenir. Sembol eşleşmesi bağımsız kontrat kimliği teyidi değildir. Geniş havuz ve eski ölçümler korunur. [Tanınan OKX hisse tokenlerinin kaynağı]('+config['equity_source']+'). Liste '+config['equity_source_checked_date']+' tarihinde kontrol edildi; yeni hisse tokenlerinin eklenmesi gerekebilir.','',
        '## Eleme özeti','']
    counts={}
    for item in r['excluded']:
        for reason in item['reasons']:counts[reason]=counts.get(reason,0)+1
    for reason,count in sorted(counts.items()):lines.append('- '+str(count)+' borsa kaydı: '+REASONS[reason])
    lines+=['','Bir kayıtta birden fazla neden olabilir; sayılar bağımsız coinler gibi toplanmaz.',
        f"Sıralama sınırı dışında kalan uygun sembol: {len(r['ranked_but_not_selected'])}.",'']
    for venue,error in r['source_errors'].items():lines.append('- '+venue+': güncel fiyat teyidi alınamadı — '+error)
    lines+=['','## Öncelik listesinin ayrı gerçek gözlem ölçümleri','',
        'Referans, bu kısa listeye ilk girişte gerçekten okunan fiyat ve saattir; eski geniş listedeki daha erken fiyat kullanılmaz. 12/24/48s ölçümleri state.json içinde ayrı tutulur. Aynı sembolün iki borsa kaydı bağımsız iki coin sayılmaz.','',
        '<details>','<summary>Öncelik listesinin 12/24/48 saat sonuçlarını aç</summary>','',
        '| Coin | Borsa | İlk gerçek gözlem TR | Referans | 12s % | 24s % | 48s % |',
        '|---|---|---|---:|---:|---:|---:|']
    for entry in p.get('paper',{}).get('entries',{}).values():
        values=[]
        for h in (12,24,48):
            value=entry['outcomes'].get(str(h),{}).get('return_pct');values.append('—' if value is None else f'{value:.2f}')
        lines.append(f"| {entry['symbol']} | {entry['exchange']} | {watch.cloud.time_label(entry['observed_ms'])} | {entry['entry_price']:.8g} | {' | '.join(values)} |")
    lines+=['','</details>','','<details>','<summary>Geniş tarama, hazırlık adayları ve önceki tüm ölçümler</summary>','',RAW_START,raw,RAW_END,'','</details>','']
    path.write_text('\n'.join(lines),encoding='utf-8')


def notify(channel,config):
    state=read_json(watch.cloud.STATE);p=priority_state(state)
    if not p['pending']:return
    if channel=='report':
        p['pending']=[];watch.cloud.save(watch.cloud.STATE,state);return
    if channel=='telegram':
        token=os.environ.get('TELEGRAM_BOT_TOKEN');chat=os.environ.get('TELEGRAM_CHAT_ID')
        if not token or not chat:raise RuntimeError('Telegram configuration missing')
        for batch in list(p['pending']):
            now=now_ms()
            rows=[] if batch['obsolete'] else [r for r in batch['candidates'] if
                (r['symbol'] not in p['last_sent'] or now-p['last_sent'][r['symbol']]>=config['notification_cooldown_hours']*3600000)
                and -60000<=now-r['observed_ms']<=config['maximum_quote_age_minutes']*60000]
            if rows:
                body='Coin Tarama 3 — kısa öncelik listesi\nDeneysel işlem koşulu elemesi; kârlılık üstünlüğü doğrulanmadı.\n\n'+'\n\n'.join(describe(r) for r in rows)
                chunks=[];current=''
                for line in body.splitlines(keepends=True):
                    if len(current)+len(line)>3500:chunks.append(current);current=''
                    current+=line
                if current:chunks.append(current)
                for chunk in chunks:
                    result=watch.cloud.http_json('https://api.telegram.org/bot'+token+'/sendMessage',{'chat_id':chat,'text':chunk},label='Telegram')
                    if not result.get('ok'):raise RuntimeError('Telegram rejected priority message')
                for row in rows:p['last_sent'][row['symbol']]=batch['created_ms']
            p['pending']=[b for b in p['pending'] if b['id']!=batch['id']];watch.cloud.save(watch.cloud.STATE,state)
        return
    if channel!='github_issue':raise ValueError('Unknown priority notification channel')
    repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN');user=os.environ.get('COIN_NOTIFY_USER','').strip()
    if not repo or not token:raise RuntimeError('Priority notification configuration missing')
    if user and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',user):raise ValueError('Invalid recipient')
    url='https://api.github.com/repos/'+repo+'/issues';headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'}
    existing=watch.cloud.http_json(url+'?state=all&per_page=100',headers=headers,label='GitHub Issues')
    for batch in list(p['pending']):
        marker='<!-- coin-priority-v5:'+batch['id']+' -->'
        delivered=any(marker in (row.get('body') or '') for row in existing)
        if not delivered and not batch['obsolete']:
            now=now_ms()
            rows=[row for row in batch['candidates'] if row['symbol'] not in p['last_sent'] or
                now-p['last_sent'][row['symbol']]>=config['notification_cooldown_hours']*3600000]
            rows=[row for row in rows if -60000<=now-row['observed_ms']<=config['maximum_quote_age_minutes']*60000]
            if rows:
                body=('@'+user+'\n\n' if user else '')+'Coin Tarama 3 — kısa öncelik listesi\n\n'
                body+='Geniş taramaya ek işlem koşulu elemesi uygulanmıştır; seçilenlerin daha kârlı olacağı doğrulanmadı.\n\n'
                body+='\n\n'.join(describe(row) for row in rows)
                body+='\n\nTam havuz, hazırlık kayıtları ve elenme nedenleri: https://github.com/'+repo+'/blob/scanner-state-v5/report.md\n\n'+marker
                watch.cloud.http_json(url,{'title':'Coin Tarama 3 · Öncelik listesi · '+str(len(rows))+' coin · '+watch.cloud.time_label(batch['created_ms']),'body':body},headers,label='GitHub Issues')
                batch['delivered_symbols']=[row['symbol'] for row in rows];delivered=True
        if delivered:
            for symbol in batch.get('delivered_symbols',[r['symbol'] for r in batch['candidates']]):p['last_sent'][symbol]=batch['created_ms']
        p['pending']=[b for b in p['pending'] if b['id']!=batch['id']];watch.cloud.save(watch.cloud.STATE,state)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['observe','notify','check-status'])
    parser.add_argument('--channel',choices=['report','github_issue','telegram'],default='github_issue');args=parser.parse_args();watch.configure()
    config=read_json(CONFIG)
    if args.phase=='notify':notify(args.channel,config)
    else:
        state=read_json(watch.cloud.STATE)
        if state['rules_fingerprint']!=watch.fingerprint():raise ValueError('Core rules do not match state')
        if args.phase=='check-status':raise SystemExit(1 if state.get('priority_watch',{}).get('latest',{}).get('source_errors') else 0)
        scans=read_json(watch.cloud.OUT/'scan.json')['scans'];fresh=refresh_quotes(scans)
        observe(state,fresh,config,now_ms());watch.cloud.save(watch.cloud.STATE,state);render(state,config)
        watch.cloud.save(watch.cloud.OUT/'priority_summary.json',state['priority_watch']['latest'])
        print(json.dumps({k:state['priority_watch']['latest'][k] for k in ['raw_rows','raw_unique','eligible_unique','source_errors']}))
