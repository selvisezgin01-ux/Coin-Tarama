"""Active Coin Tarama 3 V5. Preserve the previous cohort; never change Coin Tarama 2."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor,as_completed,Future
from copy import deepcopy
from datetime import datetime,timezone
import hashlib
import os
from pathlib import Path
import threading

import github_scan as cloud
import paper_watch
import strength_v5 as model
import strength_v5_scan as scanner
from study_dataset import read_json

ROOT=Path(__file__).resolve().parent


def fingerprint():
    digest=hashlib.sha256()
    for name in ['strength_v5_config.json','strength_v5.py','strength_v5_scan.py','strength_v5_watch.py',
                 'strength_v4.py','support_indicators.py','momentum_scan.py','okx_scan.py','paper_watch.py','github_scan.py',
                 'study_config.json','study_dataset.py','parabolic_sar.py']:
        digest.update(name.encode());digest.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return digest.hexdigest()


def new_state():
    return {'version':5,'rules_fingerprint':fingerprint(),'initialization_complete':False,
            'venues':{},'pending':[],'group_measurements':{}}


def configure():
    branch=os.environ.setdefault('SCANNER_STATE_BRANCH','scanner-state-v5')
    if not branch.startswith('scanner-state-v5'):raise ValueError('Coin Tarama 3 V5 requires its own scanner-state-v5 branch')
    os.environ.setdefault('COIN_SCAN_LABEL','Coin Tarama 3')
    cloud.OUT=ROOT/'cloud_output_v5';cloud.STATE=cloud.OUT/'state.json'
    cloud.fingerprint=fingerprint;cloud.new_state=new_state


def migrate(previous,source_branch,source_commit):
    if source_branch!='scanner-state-v4':raise ValueError('Unexpected migration source')
    # Compare against the original unchanged V4 source set, not a hand-edited fingerprint.
    digest=hashlib.sha256()
    for name in ['strength_v4_config.json','strength_v4.py','support_indicators.py','momentum_scan.py','okx_scan.py',
                 'study_config.json','study_dataset.py','parabolic_sar.py']:
        digest.update(name.encode());digest.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    if previous.get('rules_fingerprint')!=digest.hexdigest():raise ValueError('Unexpected V4 experiment fingerprint')
    if previous.get('pending'):raise ValueError('Previous notifications pending: refusing to discard or replay under a different namespace')
    result=new_state()
    for venue,value in previous.get('venues',{}).items():
        result['venues'][venue]={k:deepcopy(value[k]) for k in ('active','last_alert','ever_seen') if k in value}
    result['previous_v4']={'rules_fingerprint':previous['rules_fingerprint'],
        'paper':deepcopy(previous.get('paper',{'version':paper_watch.VERSION,'entries':{},'measurement_errors':[]}))}
    result['migration']={'source_branch':source_branch,'source_commit':source_commit,
        'source_updated_ms':previous.get('updated_ms'),'migrated_ms':int(datetime.now(timezone.utc).timestamp()*1000),
        'reason':'Three added alternative groups; previous real reference prices retained in separate cohort and continue measuring. Notification cooldowns retained; no backdated new-version entries.'}
    result['initialization_complete']=True
    return result


def pull_state():
    cloud.pull_state()
    if (cloud.OUT/'parent.txt').read_text(encoding='ascii').strip():
        if not read_json(cloud.STATE).get('initialization_complete'):raise ValueError('Incomplete experiment initialization')
        return
    source=os.environ.get('STRENGTH_MIGRATE_FROM_BRANCH')
    if not source:
        state=read_json(cloud.STATE);state['initialization_complete']=True;cloud.save(cloud.STATE,state)
        return
    if source!='scanner-state-v4':raise ValueError('Only archived V4 can seed this version')
    cloud.git('fetch','--no-tags','origin','refs/heads/'+source)
    commit=cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
    import json
    previous=json.loads(cloud.git('show',commit+':state.json').stdout)
    cloud.save(cloud.STATE,migrate(previous,source,commit))


def push_state():
    if not read_json(cloud.STATE).get('initialization_complete'):
        raise ValueError('Refusing to publish an empty/incomplete migration checkpoint')
    cloud.push_state()


def register_measurements(state,scans):
    paper_watch.register(state,scans)
    for group in model.ORDER:
        subset={venue:{**scan,'candidates':[{**row,'stage':group} for row in scan.get('candidates',[]) if group in row['matched_groups']]}
                for venue,scan in scans.items() if 'error' not in scan}
        paper_watch.register(state.setdefault('group_measurements',{}).setdefault(group,{}),subset)


def refresh_measurements(state,asof,fetcher=paper_watch.endpoint_price):
    # One provider read per venue/symbol/endpoint even if it belongs to overlapping cohorts.
    cache={};lock=threading.Lock()
    def shared(venue,symbol,endpoint):
        key=(venue,symbol,endpoint)
        with lock:
            owner=key not in cache
            if owner:cache[key]=Future()
            future=cache[key]
        if owner:
            try:future.set_result(fetcher(venue,symbol,endpoint))
            except Exception as exc:future.set_exception(exc)
        return future.result()
    for cohort in [state,*state.get('group_measurements',{}).values(),state.get('previous_v4',{})]:
        paper_watch.refresh(cohort,asof,fetcher=shared)


def row_text(row):
    def number(value,digits=5):return 'bilinmiyor' if value is None else f'{value:.{digits}g}'
    groups=', '.join(model.LABELS[g] for g in row['matched_groups'])
    volume=row.get('signal_volume_ratio');spread=row.get('spread_pct')
    text=f"{row['symbol']} · {row['exchange']}\nGruplar: {groups}\nGözlem {cloud.time_label(row['observed_ms'])} TR; fiyat {number(row.get('mid_price'))}"
    text+=f"\n24s %{row['return24_pct']:.2f}; ilgili hacim {number(volume)}x; makas "+('bilinmiyor' if spread is None else f'%{spread:.2f}')
    text+='\n'+('; '.join(row.get('warnings',[])) or 'Ek eşik uyarısı yok')
    if row.get('pu_active'):text+='; teyitli RSI pozitif uyumsuzluk desteği'
    return text


def render_measurements(state):
    def pct(value):return '—' if value is None else f'{value:.2f}'
    lines=['','## V5 gerçek gözlemden sonraki sonuçlar','',
        'Her borsa/token için ilk gerçek fiyat bir ana kayıttır. Gruplar örtüşebilir; grup sayıları bağımsız başarı gibi toplanmaz. Bir gruba sonradan ilk giriş, o andaki gerçek fiyatla ayrıca ölçülür. Getiriler ücret/kayma dahil değildir; eksik ölçüm boş kalır.','',
        '| Coin | Borsa | İlk grup | Gerçek gözlem TR | Fiyat | 12s % | 24s % | 48s % |',
        '|---|---|---|---|---:|---:|---:|---:|']
    entries=state.get('paper',{}).get('entries',{})
    for entry in entries.values():
        values=[pct(entry['outcomes'].get(str(h),{}).get('return_pct')) for h in paper_watch.HOURS]
        lines.append(f"| {entry['symbol']} | {entry['exchange']} | {model.LABELS[entry['initial_stage']]} | {cloud.time_label(entry['observed_ms'])} | {entry['entry_price']:.8g} | {' | '.join(values)} |")
    lines+=['','### Grupların ayrı ölçümleri','',
            '| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |',
            '|---|---|---:|---:|---:|---:|---:|']
    for group,cohort in state.get('group_measurements',{}).items():
        for venue,stats in paper_watch.summary(cohort)['by_exchange'].items():
            for hours,item in stats['horizons'].items():
                lines.append(f"| {model.LABELS[group]} | {venue} | {hours}s | {item['available']}/{stats['entries']} | {pct(item['median_return_pct'])} | {pct(item['median_btc_excess_pct_points'])} | {pct(item['median_control_excess_pct_points'])} |")
    if state.get('previous_v4'):
        lines+=['','## Önceki V4 kayıtları — yeni kayıt alınmıyor','',
                'Eski gerçek giriş fiyatları korunur; bunlar yeni grupların geçmişte yakaladığı örnekler değildir. 12/24/48s ölçümleri ayrı sürdürülür.',
                paper_watch.render(state['previous_v4'])]
    return '\n'.join(lines)+'\n'


def scan():
    config=read_json(ROOT/'strength_v5_config.json')
    state=read_json(cloud.STATE) if cloud.STATE.exists() else new_state()
    if not state.get('initialization_complete'):raise ValueError('Pull and initialize state before scanning')
    if state['rules_fingerprint']!=fingerprint():raise ValueError('V5 rules changed; use a new experiment branch')
    scans={}
    def collect(venue):
        directory=scanner.snapshot(venue,config)
        return scanner.evaluate(venue,directory,config,False)
    with ThreadPoolExecutor(max_workers=2) as executor:
        jobs={executor.submit(collect,venue):venue for venue in ('MEXC','OKX')}
        for job in as_completed(jobs):
            try:scans[jobs[job]]=job.result()
            except Exception as exc:scans[jobs[job]]={'error':str(exc)}
    now=int(datetime.now(timezone.utc).timestamp()*1000)
    fresh=cloud.update_state(state,scans,now)
    register_measurements(state,scans);refresh_measurements(state,now)
    cloud.save(cloud.STATE,state)
    cloud.save(cloud.OUT/'scan.json',{'scans':scans,'new_candidates':fresh,'replay':False})
    summary={'unique':paper_watch.summary(state),'groups':{k:paper_watch.summary(v) for k,v in state['group_measurements'].items()},
             'previous_v4':paper_watch.summary(state.get('previous_v4',{}))}
    cloud.save(cloud.OUT/'paper_summary.json',summary)
    scanner.write_report(scans,False)
    text=(scanner.OUT/'report.md').read_text(encoding='utf-8')
    text=text.replace('Bu komut bildirim göndermez ve ileri dönem pilot kayıtlarını değiştirmez.',
                      'Yeni adaylar Coin Tarama 3 başlığıyla bildirilir; yerel 50 coinlik pilot kayıtları ayrıdır.')
    text+='\n## Bu döngüde yeni gelenler\n\n'+('\n\n'.join(row_text(row) for row in fresh) or 'Yeni aday yok.')+'\n'
    text+=render_measurements(state)
    (cloud.OUT/'report.md').write_text(text,encoding='utf-8')
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'],'a',encoding='utf-8') as stream:stream.write(text)
    print(f'Coin Tarama 3 V5: {len(fresh)} new venue candidates; {summary["unique"]["venue_records"]} actual observations.')


def notify(channel):
    old=cloud.row_text;cloud.row_text=row_text
    try:cloud.notify(channel)
    finally:cloud.row_text=old


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['pull-state','scan','push-state','notify','check-status'])
    parser.add_argument('--channel',choices=['report','github_issue','telegram'],default='report');args=parser.parse_args();configure()
    if args.phase=='pull-state':pull_state()
    elif args.phase=='scan':scan()
    elif args.phase=='push-state':push_state()
    elif args.phase=='notify':notify(args.channel)
    else:
        result=read_json(cloud.OUT/'scan.json')
        raise SystemExit(1 if any('error' in row for row in result['scans'].values()) else 0)
