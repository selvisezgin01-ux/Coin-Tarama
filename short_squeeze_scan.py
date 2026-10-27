"""Separate workflow, state and messages; original Coin Tarama 3 state is read-only."""
import argparse,json,os,re,time
from concurrent.futures import ThreadPoolExecutor,as_completed
from copy import deepcopy
from pathlib import Path
import github_scan as cloud
import paper_watch
import strength_v5_watch as base
import strength_v5_priority as priority
import short_squeeze as model
import short_squeeze_sources as source

ROOT=Path(__file__).parent;OUT=ROOT/'cloud_output_shortcu';STATE=OUT/'state.json'
SECTION='<!-- shortcu-kistir:v1 -->'
def now_ms():return int(time.time()*1000)
def config():return json.loads(model.CONFIG.read_text(encoding='utf-8'))
def configure():
    expected=config()['state_branch'];branch=os.environ.setdefault('SCANNER_STATE_BRANCH',expected)
    if branch!=expected:raise ValueError('Shortçu Kıstır requires its independent state branch')
    cloud.OUT=OUT;cloud.STATE=STATE;cloud.new_state=model.new_state;cloud.fingerprint=model.fingerprint


def pull():
    cloud.pull_state()
    # Never migrate old CEX signals into this new experiment as past squeeze signals.
    branch=config()['source_branch']
    if branch!='scanner-state-v5':raise ValueError('Unexpected technical source branch')
    cloud.git('fetch','--no-tags','origin','refs/heads/'+branch)
    commit=cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
    old=json.loads(cloud.git('show',commit+':state.json').stdout)
    if old.get('rules_fingerprint')!=base.fingerprint() or not old.get('initialization_complete'):
        raise ValueError('Source Coin Tarama 3 design is incomplete or incompatible')
    scans={venue:deepcopy(old.get('venues',{}).get(venue,{}).get('latest',{'error':'Technical source venue missing'})) for venue in ('MEXC','OKX')}
    cloud.save(OUT/'source.json',{'branch':branch,'commit':commit,'source_updated_ms':old.get('updated_ms'),
        'rules_fingerprint':old['rules_fingerprint'],'scans':scans})


def collect(venue,rows,cfg):
    client=source.Public(venue);errors=[];markets={};funding={}
    try:markets=source.markets(client,now_ms)
    except Exception as exc:return {'markets':{},'funding':{},'listed_contracts':list(getattr(client,'instruments',{})),'errors':[str(exc)],'calls':client.calls}
    checked=0
    for row in rows:
        current=markets.get(row['symbol'])
        if current is None or checked>=cfg['max_funding_checks_per_venue']:continue
        checked+=1
        try:funding[row['symbol']]=source.funding(client,current,now_ms)
        except Exception as exc:
            errors.append(row['symbol']+': '+str(exc))
            if client.blocked:break
    return {'markets':markets,'funding':funding,'listed_contracts':list(client.instruments),'errors':errors,'calls':client.calls,'funding_checked':checked}


def scan():
    cfg=config();state=json.loads(STATE.read_text(encoding='utf-8'))
    if state['rules_fingerprint']!=model.fingerprint():raise ValueError('Squeeze design changed; explicit new version required')
    saved=json.loads((OUT/'source.json').read_text(encoding='utf-8'));original=deepcopy(saved)
    # Source technical features remain as observed; only copied spot quotes/context refresh.
    scans=priority.refresh_quotes(saved['scans']);stamp=now_ms()
    policy=json.loads(priority.CONFIG.read_text(encoding='utf-8'))
    eligible,rejected,source_errors=model.technical_rows(scans,policy,stamp)
    venues={};decisions=[]
    with ThreadPoolExecutor(max_workers=2) as executor:
        jobs={executor.submit(collect,v,[r for r in eligible if r['exchange']==v],cfg):v for v in ('MEXC','OKX')}
        for job in as_completed(jobs):
            v=jobs[job]
            try:venues[v]=job.result()
            except Exception as exc:venues[v]={'markets':{},'funding':{},'errors':[str(exc)],'calls':0}
    # Fresh final spot reads ensure newly registered references are not inherited old prices.
    final=priority.refresh_quotes(scans);stamp=now_ms()
    eligible,rejected,late_errors=model.technical_rows(final,policy,stamp);source_errors.update(late_errors)
    for venue,result in venues.items():
        considered=0
        for row in [r for r in eligible if r['exchange']==venue]:
            current=result['markets'].get(row['symbol']);contract=None if current is None else current['contract']
            history=state['history'].get(venue+':'+str(contract),[])
            decision=model.decide(row,current,result['funding'].get(row['symbol']),history,cfg,stamp)
            if current is None and (row['symbol'] in result.get('listed_contracts',[]) or result['errors']):
                decision.update(status='unknown',reasons=['market_data_unknown'])
            decision['row']=row;decisions.append(decision);considered+=1
        # Compare before adding the current snapshot, so reruns cannot fake 4h growth.
        model.record_history(state,venue,result['markets'],cfg,stamp)
        result['considered']=considered
    failed=set(source_errors)|{v for v,r in venues.items() if r['errors']}
    selected=model.select(decisions,cfg);model.queue(state,selected,failed,cfg,stamp)
    selected_scans={v:{'candidates':[r['row'] for r in selected if r['exchange']==v]} for v in ('MEXC','OKX')}
    paper_watch.register(state,selected_scans);paper_watch.refresh(state,stamp)
    state['latest']={'observed_ms':stamp,'source_branch':saved['branch'],'source_commit':saved['commit'],
        'source_updated_ms':saved.get('source_updated_ms'),'source_errors':source_errors,
        'technical_eligible':len(eligible),'technical_rejected':rejected,'decisions':decisions,'selected':selected,
        'venues':{v:{'market_records':len(r['markets']),'funding_checked':r.get('funding_checked',0),'calls':r['calls'],'errors':r['errors']} for v,r in venues.items()}}
    assert saved==original,'Technical source mutated'
    cloud.save(STATE,state);render(state,cfg)
    (OUT/'ready.txt').write_text('scan complete',encoding='ascii')
    cloud.save(OUT/'summary.json',state['latest'])
    print(json.dumps({'technical_eligible':len(eligible),'selected':len(selected),
        'status_counts':{s:sum(d['status']==s for d in decisions) for s in ['candidate','warming','watch','unknown']},
        'venues':state['latest']['venues'],'source_errors':source_errors}))


def describe(d):
    row=d['row'];m=d['metrics']
    return (f"{d['symbol']} · {d['exchange']} · {m['contract']}\n"
        f"Spot gözlemi {cloud.time_label(row['observed_ms'])} TR; fiyat {row['mid_price']:.8g}\n"
        f"Fonlama %{m['funding_rate']*100:.4f} / {m['funding_hours']:g} saat; 8 saate ölçekli %{m['funding_scaled_8h']*100:.4f}\n"
        f"OI %{m['oi_change_pct']:+.2f}; vadeli fiyat %{m['futures_price_change_pct']:+.2f}; gerçek aralık {m['elapsed_hours']:.2f} saat\n"
        f"OI gözlemi {cloud.time_label(m['futures_observed_ms'])} TR; vadeli makas %{m['futures_spread_pct']:.3f}; spot/vadeli fark %{m['basis_pct']:.2f}\n"
        'Olası short sıkışması için deneysel adaydır; toplam OI short miktarını veya likidasyonu doğrulamaz.')


def measurements(state):
    stats=paper_watch.summary(state)
    lines=[f"{stats['venue_records']} borsa kaydı / {stats['unique_symbols']} farklı sembol. Aynı coin ayrı bağımsız başarı sayılmaz.",'',
        '| Coin | Borsa | Teknik grup | Yeni deneyin ilk gerçek gözlemi TR | Spot referans | 12s % | 24s % | 48s % |',
        '|---|---|---|---|---:|---:|---:|---:|']
    for entry in state.get('paper',{}).get('entries',{}).values():
        values=[entry['outcomes'].get(str(h),{}).get('return_pct') for h in (12,24,48)]
        cells=['—' if v is None else f'{v:+.2f}' for v in values]
        label=base.model.LABELS.get(entry['initial_stage'],entry['initial_stage'])
        lines.append(f"| {entry['symbol']} | {entry['exchange']} | {label} | {cloud.time_label(entry['observed_ms'])} | {entry['entry_price']:.8g} | {' | '.join(cells)} |")
    if state.get('paper',{}).get('measurement_errors'):lines.append('Bazı ölçüm uçları eksik; sonradan yeniden denenecek. Eksik sonuçlar sıfır getiri sayılmaz.')
    return '\n'.join(lines)


def render(state,cfg):
    r=state['latest'];lines=['# Shortçu Kıstır','',f"Son çalışma: {cloud.time_label(r['observed_ms'])} TR.",'',
        '**Coin Tarama 3 teknik temelinden beslenen bağımsız deney. Short pozisyon açılmaz; yükseliş yönlü olası short sıkışması aranır. Başarı garantisi yoktur.**','',
        f"Teknik işlem koşullarından geçen {r['technical_eligible']} borsa kaydı; squeeze koşullarını sağlayan en çok {cfg['max_unique_symbols']} farklı sembol; güncel liste {len(r['selected'])}.",'',
        'Kaynak: Coin Tarama 3 tamamlandığında scanner-state-v5 dalından okunur. Kaynak adaylar, eski ölçümler ve beşli öncelik listesi değiştirilmez. Eski fiyatlar yeni sinyalin referansı değildir.','',
        '| Coin | Borsa | Gerçek spot gözlemi TR | Spot fiyat | Fonlama / dönem | OI değişimi | Gerçek aralık |',
        '|---|---|---|---:|---|---:|---|']
    for d in r['selected']:
        row=d['row'];m=d['metrics'];lines.append(f"| {d['symbol']} | {d['exchange']} | {cloud.time_label(row['observed_ms'])} | {row['mid_price']:.8g} | %{m['funding_rate']*100:.4f} / {m['funding_hours']:g}s | %{m['oi_change_pct']:+.2f} | {m['elapsed_hours']:.2f}s |")
    if not r['selected']:lines+=['','Şu an tüm koşulları doğrulanan aday yok. Veri birikimi/erişim eksikliği ile koşul sağlanmaması aşağıda ayrılır.']
    counts={}
    for d in r['decisions']:
        for reason in d['reasons']:counts[reason]=counts.get(reason,0)+1
    lines+=['','## Veri birikimi ve eleme nedenleri','']
    for reason,count in sorted(counts.items()):lines.append(f"- {count} borsa kaydı: {model.REASONS.get(reason,reason)}")
    lines+=['','Bir kayıtta birden çok neden olabilir. Şu anki fonlama ve OI, başarısız teknik filtreleri geçersiz kılmaz.','']
    for venue,result in r['venues'].items():
        lines.append(f"- {venue}: {result['market_records']} güncel vadeli OI kaydı; {result['funding_checked']} fonlama incelemesi; {len(result['errors'])} erişim/veri hatası.")
        lines+=['  - '+e for e in result['errors'][:5]]
    lines+=['- '+v+': teknik kaynak/güncel spot fiyat eksik — '+e for v,e in r['source_errors'].items()]
    lines+=['','## Dondurulmuş başlangıç kuralları','',
        'Coin Tarama 3 geniş aday havuzuna mevcut işlem koşulu elemesi uygulanır; eski beşli sınırı öncesindeki uygun adaylar değerlendirilir. Yalnız hazırlık grubu tek başına bildirilmez. Aynı borsada tam baz koduyla eşleşen aktif USDT perpetual kontrat gerekir; 1000x isimler veya başka borsanın verisi eşlenmez.','',
        'Güncel fonlama: 8 saate oransal ölçeklendiğinde en çok -%0.01. OI kontrat sayısı en az %5 artmış olmalı; önceki GERÇEK gözlem yaklaşık 4 saat önce (3–5 saat aralığı) olmalı. Fiyat aynı aralıkta %0–12 yükselmiş, vadeli makas en çok %0.5, OI büyüklüğü en az yaklaşık 1 milyon USD/USDT, spot-vadeli fiyat farkı en çok %2 olmalı. İlk çalışmada eski OI yoksa veri birikiyor; geriye sinyal yazılmaz.','',
        'OI değişimi fiyat etkisinden arındırılmış aynı kontrat sayılarıyla ölçülür; kontrat büyüklüğü değiştiyse eski baz kullanılmaz. MEXC OI parasal büyüklüğü güncel fiyatla tahmini USDT, OKX oiUsd sağlayıcı USD değeridir; eşdeğer nakit veya fiyat etkisinden arınmış büyüme değillerdir. Fonlama dönemleri ayrı gösterilir; 8 saat ölçeği gelecek ödeme tahmini değildir.','',
        'Negatif fonlama ve artan toplam OI, shortların çoğunlukta olduğunu veya fiyat yükseldiğinde kesin likidasyon olacağını kanıtlamaz. Likidasyon haritası, hesapların kaldıraçları ve bağımsız short-only OI verisi kullanılmaz. Bu bir araştırma filtresidir.','',
        'Aynı sembol küresel listede bir kez seçilir; farklı borsaların OI/hacimleri toplanmaz. Sembol eşleşmesi kontrat kimliğinin bağımsız doğrulaması değildir. Yeni girişler yalnız o andaki gerçek spot fiyatından 12/24/48 saat ölçülür; ücret, kayma ve vadeli fonlama dahil net getiri değildir.','',
        '## Bu deneyin ayrı gerçek gözlem ölçümleri','',measurements(state),'',
        '[MEXC kontrat verileri](https://www.mexc.com/api-docs/futures/market-endpoints/get-ticker-contract-market-data) · [MEXC fonlama](https://www.mexc.com/api-docs/futures/market-endpoints/get-funding-rate) · [OKX kamu verileri](https://www.okx.com/docs-v5/en/#public-data-rest-api-get-open-interest)','',SECTION]
    OUT.mkdir(exist_ok=True);(OUT/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')


def notify(channel):
    cfg=config();state=json.loads(STATE.read_text(encoding='utf-8'))
    if state['rules_fingerprint']!=model.fingerprint():raise ValueError('Squeeze state incompatible')
    if not state['pending']:return
    if channel=='report':state['pending']=[];cloud.save(STATE,state);return
    repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN');user=os.environ.get('COIN_NOTIFY_USER','').strip()
    if channel=='github_issue' and (not repo or not token):raise RuntimeError('GitHub notification configuration missing')
    if user and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',user):raise ValueError('Invalid recipient')
    if channel=='github_issue':
        url='https://api.github.com/repos/'+repo+'/issues';headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'}
        existing=cloud.http_json(url+'?state=all&per_page=100',headers=headers,label='GitHub Issues')
    for batch in list(state['pending']):
        marker='<!-- shortcu-kistir:'+batch['id']+' -->'
        delivered=channel=='github_issue' and any(marker in (i.get('body') or '') for i in existing)
        stamp=now_ms()
        rows=[] if batch['obsolete'] else [d for d in batch['candidates'] if
            -60000<=stamp-d['row']['observed_ms']<=cfg['max_notification_age_minutes']*60000 and
            (d['symbol'] not in state['last_sent'] or stamp-state['last_sent'][d['symbol']]>=cfg['cooldown_hours']*3600000)]
        if not delivered and rows:
            body=('@'+user+'\n\n' if user else '')+'Shortçu Kıstır — olası short sıkışması adayları\n\n'+'\n\n'.join(describe(d) for d in rows)
            body+='\n\nAyrı deney; eski Coin Tarama 3 fiyatları giriş olarak kullanılmaz. Rapor: https://github.com/'+str(repo)+'/blob/'+cfg['state_branch']+'/report.md\n\n'+marker
            if channel=='github_issue':cloud.http_json(url,{'title':'Shortçu Kıstır · '+str(len(rows))+' aday · '+cloud.time_label(batch['created_ms']),'body':body},headers,label='GitHub Issues')
            elif channel=='telegram':
                bot=os.environ.get('TELEGRAM_BOT_TOKEN');chat=os.environ.get('TELEGRAM_CHAT_ID')
                if not bot or not chat:raise RuntimeError('Telegram configuration missing')
                if len(body)>4000:raise RuntimeError('Message exceeds Telegram limit; keep pending for review')
                result=cloud.http_json('https://api.telegram.org/bot'+bot+'/sendMessage',{'chat_id':chat,'text':body},label='Telegram')
                if not result.get('ok'):raise RuntimeError('Telegram notification rejected')
            else:raise ValueError('Unknown channel')
            batch['delivered_symbols']=[d['symbol'] for d in rows];delivered=True
        if delivered:
            for symbol in batch.get('delivered_symbols',[d['symbol'] for d in batch['candidates']]):state['last_sent'][symbol]=batch['created_ms']
        state['delivery_audit'].append({'id':batch['id'],'delivered':bool(delivered),'obsolete':batch['obsolete'],'checked_ms':stamp})
        state['delivery_audit']=state['delivery_audit'][-300:]
        state['pending']=[b for b in state['pending'] if b['id']!=batch['id']];cloud.save(STATE,state)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['pull-state','scan','push-state','notify','check-status'])
    parser.add_argument('--channel',choices=['report','github_issue','telegram'],default='github_issue');args=parser.parse_args();configure()
    if args.phase=='pull-state':pull()
    elif args.phase=='scan':scan()
    elif args.phase=='push-state':
        if not (OUT/'ready.txt').exists():raise RuntimeError('Cannot publish incomplete Shortçu Kıstır initialization')
        cloud.push_state()
    elif args.phase=='notify':notify(args.channel)
    else:
        state=json.loads(STATE.read_text(encoding='utf-8'));r=state['latest']
        raise SystemExit(1 if r['source_errors'] or any(v['errors'] for v in r['venues'].values()) else 0)
