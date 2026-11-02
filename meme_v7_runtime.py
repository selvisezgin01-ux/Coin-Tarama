"""Operational entry point: restore legacy or verified partitioned V7 state."""
import argparse, json, os, sys
import meme_v7 as scanner
from meme_v7_storage import load
from meme_v7_persistence import PublicationError

def pull_state():
    cloud=scanner.cloud
    if cloud.state_branch()!=scanner.BRANCH:raise RuntimeError('Refuse unexpected state branch')
    found=cloud.git('ls-remote','--exit-code','--heads','origin','refs/heads/'+scanner.BRANCH,allowed=(0,2))
    scanner.OUT.mkdir(parents=True,exist_ok=True)
    if found.returncode==2:raise RuntimeError('Expected existing V7 history is missing; refusing reset')
    cloud.git('fetch','--depth=1','--no-tags','origin','refs/heads/'+scanner.BRANCH)
    parent=cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
    manifest=json.loads(cloud.git('show',parent+':state.json').stdout)
    state=load(manifest,lambda name:cloud.git('show',parent+':'+name).stdout.encode('utf-8'))
    if state.get('rules_fingerprint')!=scanner.fingerprint():raise RuntimeError('Stored V7 financial rules differ; refusing migration')
    cloud.save(scanner.STATE,state);(scanner.OUT/'parent.txt').write_text(parent,encoding='ascii')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['worker']);parser.add_argument('--minutes',type=int,default=110);args=parser.parse_args()
    # Only the V7 process restore hook changes. Shared scanners and financial source stay untouched.
    scanner.cloud.pull_state=pull_state
    try:scanner.worker(args.minutes)
    except PublicationError as exc:
        print(json.dumps({'publication_error':exc.category,'detail':exc.detail}),flush=True)
        raise SystemExit(75 if exc.restart_allowed else 78)

if __name__=='__main__':main()
