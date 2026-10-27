"""Separate 5m position-share update monitor. Source scanner is strictly read-only."""
from __future__ import annotations
import argparse,hashlib,json,os,re,time
from copy import deepcopy
from pathlib import Path
import github_scan as cloud
import short_squeeze as production
import short_squeeze_positions as positions

ROOT=Path(__file__).parent;OUT=ROOT/'cloud_output_shortcu_positions';STATE=OUT/'state.json'
CONFIG=ROOT/'short_squeeze_monitor_config.json'
def now_ms():return int(time.time()*1000)
def cfg():return json.loads(CONFIG.read_text(encoding='utf-8'))
def fingerprint():
    h=hashlib.sha256()
    for name in ('short_squeeze_monitor.py','short_squeeze_positions.py','short_squeeze_monitor_config.json'):
        h.update(name.encode());h.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return h.hexdigest()
def new_state():return {'version':'shortcu-position-monitor-v1','rules_fingerprint':fingerprint(),'assets':{},'active':[],'pending':[],'audit':[]}
def configure():
    expected=cfg()['state_branch'];branch=os.environ.setdefault('SCANNER_STATE_BRANCH',expected)
    if branch!=expected:raise ValueError('Position monitor must use its separate state branch')
    cloud.OUT=OUT;cloud.STATE=STATE;cloud.fingerprint=fingerprint;cloud.new_state=new_state


def pull():
    cloud.pull_state();branch=cfg()['source_branch']
    if branch!='scanner-state-shortcu-kistir':raise ValueError('Unexpected original scanner branch')
    cloud.git('fetch','--no-tags','origin','refs/heads/'+branch)
    commit=cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
    source=json.loads(cloud.git('show',commit+':state.json').stdout)
    if source.get('rules_fingerprint')!=production.fingerprint():raise ValueError('Original scanner version mismatch')
    # Keep only public alert references; no OI arrays or unrelated cohorts needed.
    subset={'last_sent':source.get('last_sent',{}),'latest':{'selected':source.get('latest',{}).get('selected',[])},
        'paper':{'entries':source.get('paper',{}).get('entries',{})}}
    cloud.save(OUT/'source.json',{'branch':branch,'commit':commit,'data':subset})


def targets(source,state,stamp,config):
    known={(a['ref']['symbol'],a['ref']['notified_ms']):a['ref'] for a in state['assets'].values()}
    result=[];unresolved=0;eligible=0
    for symbol,notified in source.get('last_sent',{}).items():
        if not re.fullmatch(r'[A-Z0-9]+USDT',symbol) or positions.num(notified) is None:continue
        if not -60000<=stamp-notified<=config['watch_hours_after_alert']*3600000:continue
        eligible+=1;choices=[]
        for d in source.get('latest',{}).get('selected',[]):
            if d.get('symbol')!=symbol:continue
            r=d.get('row',{});t=positions.num(r.get('observed_ms'));price=positions.num(r.get('mid_price'))
            if t is not None and price is not None and price>0 and abs(t-notified)<=config['source_reference_tolerance_minutes']*60000:
                choices.append({'symbol':symbol,'origin_venue':d['exchange'],'reference_ms':t,'reference_price':price,'notified_ms':notified})
        for e in source.get('paper',{}).get('entries',{}).values():
            t=positions.num(e.get('observed_ms'));price=positions.num(e.get('entry_price'))
            if e.get('symbol')==symbol and t is not None and price is not None and price>0 and abs(t-notified)<=config['source_reference_tolerance_minutes']*60000:
                choices.append({'symbol':symbol,'origin_venue':e['exchange'],'reference_ms':t,'reference_price':price,'notified_ms':notified})
        cached=known.get((symbol,notified))
        if cached and cached['notified_ms']==notified:choices.append(deepcopy(cached))
        if not choices:unresolved+=1;continue
        choice=min(choices,key=lambda r:(abs(r['reference_ms']-notified),r['origin_venue']))
        choice['id']=hashlib.sha256(json.dumps([symbol,notified,choice['origin_venue']]).encode()).hexdigest()[:24]
        choice['expires_ms']=notified+config['watch_hours_after_alert']*3600000;result.append(choice)
    result.sort(key=lambda r:(-r['notified_ms'],r['symbol']))
    return result[:config['max_symbols_per_run']],{'delivered_candidates_in_window':eligible,'unresolved_references':unresolved,
        'outside_request_budget':max(0,len(result)-config['max_symbols_per_run'])}


def issue_settings():
    repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN');user=os.environ.get('COIN_NOTIFY_USER','').strip()
    if not repo or not token:raise RuntimeError('GitHub update notification configuration missing')
    if user and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',user):raise ValueError('Invalid notification recipient')
    return 'https://api.github.com/repos/'+repo+'/issues',{'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'},user


def mark_delivered(state,event):
    profile=state['assets'][event['asset_id']]['profiles'][event['provider']]
    profile['anchor']=deepcopy(event['new']);profile['last_delivered_ms']=event['created_ms']
    state['audit'].append({'id':event['id'],'status':'delivered','provider_ms':event['new']['provider_ms']})


def reconcile(state,channel):
    if not state['pending']:return
    if channel=='github_issue':
        url,headers,_=issue_settings()
        issues=cloud.http_json(url+'?state=all&per_page=100',headers=headers,label='GitHub Issues')
        for event in state['pending']:
            marker='<!-- shortcu-position-event:'+event['id']+' -->'
            if any(marker in (i.get('body') or '') and i.get('user',{}).get('login')=='github-actions[bot]' for i in issues):mark_delivered(state,event)
            else:state['audit'].append({'id':event['id'],'status':'superseded_for_fresh_observation'})
    else:
        for event in state['pending']:state['audit'].append({'id':event['id'],'status':'superseded_for_fresh_observation'})
    state['pending']=[];state['audit']=state['audit'][-500:]


def enqueue_change(state,ref,provider,profile,point,stamp,config):
    delta=positions.change(profile['anchor'],point)
    if not positions.meaningful(delta,config):return
    event={'asset_id':ref['id'],'provider':provider,'symbol':ref['symbol'],'origin_venue':ref['origin_venue'],
        'created_ms':stamp,'old':deepcopy(profile['anchor']),'new':deepcopy(point),'delta':delta}
    event['id']=hashlib.sha256(json.dumps([ref['id'],provider,event['old']['provider_ms'],point['provider_ms'],point['ratio_long_over_short']]).encode()).hexdigest()[:24]
    state['pending'].append(event)


def update(state,ref,provider,point,stamp,config):
    asset=state['assets'].setdefault(ref['id'],{'ref':deepcopy(ref),'profiles':{}})
    profile=asset['profiles'].setdefault(provider,{'anchor':None,'latest':None,'history':[],'revisions':0})
    profile['last_status']=point['status'];profile['last_check_ms']=stamp
    if point['status']!='observed':profile['reason']=point.get('reason','data unavailable');return
    profile.pop('reason',None);previous=profile['latest']
    if previous and point['provider_ms']<previous['provider_ms']:
        profile['last_status']='unknown';profile['reason']='out_of_order_provider_timestamp';return
    if previous and point['provider_ms']==previous['provider_ms']:
        if point['ratio_long_over_short']!=previous['ratio_long_over_short']:profile['revisions']+=1
        profile['latest']=deepcopy(point)
        # An accepted delivery is reconciled BEFORE this function. If an older
        # period's change was never delivered, retry its current, fresh value.
        if profile['anchor'] and profile['anchor']['provider_ms']<point['provider_ms']:
            enqueue_change(state,ref,provider,profile,point,stamp,config)
        return
    profile['latest']=deepcopy(point);profile['history'].append(deepcopy(point));profile['history']=profile['history'][-288:]
    if profile['anchor'] is None:profile['anchor']=deepcopy(point);return # Live baseline, no backfilled event.
    enqueue_change(state,ref,provider,profile,point,stamp,config)


def event_text(event):
    old=event['old'];new=event['new'];d=event['delta'];direction='yükseliyor' if d['short_change_pp']>0 else 'düşüyor'
    relative='tanımsız (önceki pay sıfır veya sayısal karşılaştırma yok)' if d['short_relative_change_pct'] is None else f"%{d['short_relative_change_pct']:+.2f}"
    return (f"{event['symbol']} · aday fiyat borsası {event['origin_venue']}\n{new['scope']}\n"
        f"Short payı {direction}: %{old['short_pct']:.2f} → %{new['short_pct']:.2f}\n"
        f"Değişim: {d['short_change_pp']:+.2f} yüzde puan; göreli değişim {relative}\n"
        f"Son long payı: %{new['long_pct']:.2f}\n"
        f"Veri: {cloud.time_label(old['provider_ms'])} → {cloud.time_label(new['provider_ms'])} TR ({d['elapsed_minutes']:.0f} dk)\n"
        f"Kontrol: {cloud.time_label(new['observed_ms'])} TR\n"
        'Bu grubun pozisyon dağılımıdır; tüm piyasanın veya MEXC toplamının oranı değildir. Yeni alım/satım sinyali değildir.')


def observe(channel):
    config=cfg();state=json.loads(STATE.read_text(encoding='utf-8'))
    if state['rules_fingerprint']!=fingerprint():raise ValueError('Monitor rules changed; explicit new monitor version required')
    source=json.loads((OUT/'source.json').read_text(encoding='utf-8'));before=deepcopy(source)
    reconcile(state,channel);stamp=now_ms();refs,coverage=targets(source['data'],state,stamp,config)
    state['active']=[r['id'] for r in refs];clients={p:positions.Client(p) for p in positions.SCOPES};errors=[]
    for ref in refs:
        for provider,client in clients.items():
            point=client.read(ref['symbol'],now_ms,config);update(state,ref,provider,point,now_ms(),config)
            profile=state['assets'][ref['id']]['profiles'][provider]
            if profile['last_status']=='unknown':errors.append({'symbol':ref['symbol'],'provider':provider,'reason':profile.get('reason','data unknown')})
    assert source==before,'Original scanner source must remain read-only'
    observed=sum(p.get('last_status')=='observed' for k in state['active'] for p in state['assets'][k]['profiles'].values())
    state['latest']={'observed_ms':now_ms(),'source_commit':source['commit'],'coverage':coverage,'active_symbols':len(refs),
        'queued_changes':len(state['pending']),'api_calls':{p:c.calls for p,c in clients.items()},'errors':errors,
        'observed_profiles':observed,'critical_data_failure':bool(refs and observed==0 and errors)}
    cloud.save(STATE,state);report(state);(OUT/'ready.txt').write_text('complete',encoding='ascii')
    print(json.dumps(state['latest']))


def report(state):
    r=state['latest'];config=cfg()
    lines=['# Shortçu Kıstır — dinamik pozisyon oranı takibi','',f"Son kontrol: {cloud.time_label(r['observed_ms'])} TR.",'',
        '**Yalnız gerçekten bildirilmiş Shortçu Kıstır adayları. Yeni aday seçimi veya alım/satım sinyali değildir.**','',
        'OKX: pozisyon değeri en büyük %5 grubunun pozisyon oranı. Binance: teminat bakiyesi en büyük %20 grubunun pozisyon oranı. Hesap sayısı veya tüm piyasanın toplam short yüzdesi değildir; iki kaynak ortalanmaz. Aday MEXC fiyatından seçilmiş olsa da OKX/Binance oranı MEXC oranı olarak adlandırılmaz.','',
        f"{r['active_symbols']} aktif sembol; son aday bildiriminin ardından {config['watch_hours_after_alert']} saat, çalışmada en çok {config['max_symbols_per_run']} sembol. İlk canlı gözlem yalnız başlangıç oluşturur; geçmişe bildirim yazılmaz.",'',
        '| Coin | Aday borsası | Oran kaynağı | Son geçerli short % | Long % | Veri TR | Kontrol durumu |','|---|---|---|---:|---:|---|---|']
    for key in state['active']:
        asset=state['assets'][key]
        for provider,p in asset['profiles'].items():
            point=p.get('latest');status=p.get('last_status','unknown')
            short='—' if not point else f"{point['short_pct']:.2f}"
            long='—' if not point else f"{point['long_pct']:.2f}"
            date='—' if not point else cloud.time_label(point['provider_ms'])
            lines.append(f"| {asset['ref']['symbol']} | {asset['ref']['origin_venue']} | {provider} | {short} | {long} | {date} | {status} {p.get('reason','')} |")
    if not state['active']:lines+=['','Henüz son 24 saatte bildirilmiş, referansı doğrulanabilen aday yok; oran izleme listesi boş.']
    lines+=['',f"Anlamlı değişim: son bildirilen/ilk gözlenen short payına göre en az {config['minimum_short_change_percentage_points']} yüzde puan veya %50 seviyesinin geçilmesi. Küçük değişimler birikerek eşiğe ulaşabilir. Aynı zaman damgalı revizyon yeni dönem gibi bildirilmez.",'',
        'Örnek (gerçek aday değildir): short %60 → %65 = +5 yüzde puan, göreli +%8.33; long %35. Önceki short %0 ise göreli değişim tanımsızdır; uydurulmaz.','',
        'API verisinin en kısa istenen aralığı 5dk. GitHub yaklaşık 5dk kontrol için planlanır; gecikme/atlama olabilir. Mesaj iki gerçek sağlayıcı zaman damgasını ve kontrol saatini gösterir; her değişimin oluştuğu anı veya kesintisiz her 5dk gözlemi bildiği iddia edilmez.','',
        'Eksik, eski, desteklenmeyen veya erişimi engellenen veri bilinmiyor kalır. Binance anonim erişimi değişebilir; API anahtarı/erişim istendiğinde durulur, kısıt aşılmaz. Özel hesap/emir veya ücretli veri erişimi yoktur. Sembol eşleşmesi token kontrat kimliğinin bağımsız doğrulaması değildir.','',
        'Kapsam: '+json.dumps(r['coverage'],ensure_ascii=False),f"Bekleyen anlamlı değişim: {len(state['pending'])}; erişim/veri sorunu: {len(r['errors'])}.",'',
        '[OKX kapsam](https://www.okx.com/en-us/help/how-do-i-use-the-top-position-long-short-ratio-indicator) · [Binance pozisyon oranı](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio)','']
    OUT.mkdir(exist_ok=True);(OUT/'report.md').write_text('\n'.join(lines),encoding='utf-8')


def notify(channel):
    config=cfg();state=json.loads(STATE.read_text(encoding='utf-8'))
    if state['rules_fingerprint']!=fingerprint():raise ValueError('Monitor design mismatch')
    if not state['pending']:return
    if channel=='report':state['pending']=[];cloud.save(STATE,state);return
    if channel!='github_issue':raise ValueError('This update monitor currently uses GitHub Issue notifications')
    url,headers,user=issue_settings();stamp=now_ms()
    valid=[e for e in state['pending'] if e['asset_id'] in state['active'] and
        -60000<=stamp-e['created_ms']<=config['max_notification_age_minutes']*60000 and
        stamp<=state['assets'][e['asset_id']]['ref']['expires_ms']]
    if valid:
        # Reconcile a previously accepted POST whose checkpoint failed, even on a retry.
        existing=cloud.http_json(url+'?state=all&per_page=100',headers=headers,label='GitHub Issues')
        fresh=[]
        for e in valid:
            marker='<!-- shortcu-position-event:'+e['id']+' -->'
            if any(marker in (i.get('body') or '') and i.get('user',{}).get('login')=='github-actions[bot]' for i in existing):mark_delivered(state,e)
            else:fresh.append(e)
        if fresh:
            body=('@'+user+'\n\n' if user else '')+'Shortçu Kıstır — short payı değişimi\n\n'+'\n\n'.join(event_text(e) for e in fresh)
            body+='\n\n'+'\n'.join('<!-- shortcu-position-event:'+e['id']+' -->' for e in fresh)
            cloud.http_json(url,{'title':'Shortçu Kıstır · Pozisyon oranı değişimi · '+cloud.time_label(stamp),'body':body},headers,label='GitHub Issues')
            for e in fresh:mark_delivered(state,e)
    for e in state['pending']:
        if e not in valid:state['audit'].append({'id':e['id'],'status':'expired_not_delivered'})
    state['pending']=[];state['audit']=state['audit'][-500:]
    cloud.save(STATE,state);report(state)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['pull-state','observe','notify','push-state','check-status'])
    p.add_argument('--channel',choices=['report','github_issue'],default='github_issue');a=p.parse_args();configure()
    if a.phase=='pull-state':pull()
    elif a.phase=='observe':observe(a.channel)
    elif a.phase=='notify':notify(a.channel)
    elif a.phase=='push-state':
        if not (OUT/'ready.txt').exists():raise RuntimeError('Monitor observation not complete')
        cloud.push_state()
    else:
        state=json.loads(STATE.read_text(encoding='utf-8'));raise SystemExit(1 if state['latest'].get('critical_data_failure') else 0)
