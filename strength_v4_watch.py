"""Coin Tarama 3: durable independent GitHub experiment using V4 rules."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
import argparse
import hashlib
import os
from pathlib import Path

import github_scan as cloud
import paper_watch
import strength_v4_scan as scanner
from study_dataset import read_json

ROOT = Path(__file__).resolve().parent


def fingerprint():
    digest = hashlib.sha256()
    for name in ['strength_v4_config.json','strength_v4.py','support_indicators.py','momentum_scan.py','okx_scan.py',
                 'study_config.json','study_dataset.py','parabolic_sar.py']:
        digest.update(name.encode())
        digest.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return digest.hexdigest()


def configure():
    branch = os.environ.setdefault('SCANNER_STATE_BRANCH','scanner-state-v4')
    if not branch.startswith('scanner-state-v4'):
        raise ValueError('Coin Tarama 3 requires its own scanner-state-v4 version branch.')
    os.environ.setdefault('COIN_SCAN_LABEL','Coin Tarama 3')
    cloud.OUT = ROOT/'cloud_output_v4'
    cloud.STATE = cloud.OUT/'state.json'
    cloud.fingerprint = fingerprint


def scan():
    config = read_json(ROOT/'strength_v4_config.json')
    state = read_json(cloud.STATE) if cloud.STATE.exists() else cloud.new_state()
    if state['rules_fingerprint']!=fingerprint():
        raise RuntimeError('V4 rules changed; use an explicitly new experiment branch.')
    scans = {}
    def collect(venue):
        directory = scanner.snapshot(venue,config)
        return scanner.evaluate(venue,directory,config,False)
    with ThreadPoolExecutor(max_workers=2) as executor:
        jobs = {executor.submit(collect,e):e for e in ['MEXC','OKX']}
        for job in as_completed(jobs):
            try: scans[jobs[job]] = job.result()
            except Exception as exc: scans[jobs[job]] = {'error':str(exc)}
    now = int(datetime.now(timezone.utc).timestamp()*1000)
    fresh = cloud.update_state(state,scans,now)
    paper_watch.register(state,scans)
    paper_watch.refresh(state,now)
    cloud.save(cloud.STATE,state)
    cloud.save(cloud.OUT/'scan.json',{'scans':scans,'new_candidates':fresh,'replay':False})
    cloud.save(cloud.OUT/'paper_summary.json',paper_watch.summary(state))
    scanner.write_report(scans,False)
    text = (scanner.OUT/'report.md').read_text(encoding='utf-8')
    text = text.replace('# Deneysel V4 — yeni kırılım ve tutunma','# Coin Tarama 3 — yeni kırılım ve tutunma',1)
    text = text.replace('Bu komut bildirim göndermez ve ileri dönem pilot kayıtlarını değiştirmez.',
                        'Yeni adaylar bu sürümün kendi bildirim başlığıyla gönderilir; yerel pilot kayıtları ayrıdır.')
    text += '\n## Bu döngüde yeni gelenler\n\n'
    text += '\n\n'.join(cloud.row_text(row) for row in fresh) if fresh else 'Yeni aday yok.'
    text += '\n'+paper_watch.render(state)
    (cloud.OUT/'report.md').write_text(text,encoding='utf-8')
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary_path:
        with open(summary_path,'a',encoding='utf-8') as stream: stream.write(text)
    print(f'Coin Tarama 3: {len(fresh)} new venue candidates; {paper_watch.summary(state)["venue_records"]} actual observations.')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('phase',choices=['pull-state','scan','push-state','notify','check-status'])
    parser.add_argument('--channel',choices=['report','github_issue','telegram'],default='report')
    args = parser.parse_args()
    configure()
    if args.phase=='pull-state': cloud.pull_state()
    elif args.phase=='push-state': cloud.push_state()
    elif args.phase=='scan': scan()
    elif args.phase=='notify': cloud.notify(args.channel)
    else:
        result = read_json(cloud.OUT/'scan.json')
        raise SystemExit(1 if any('error' in r for r in result['scans'].values()) else 0)
