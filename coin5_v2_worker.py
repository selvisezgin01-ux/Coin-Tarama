"""Bounded checkpointed public-data worker; nominal cadence is not a guarantee."""
import argparse,json,os,time,math
import coin5_v2_scan as scan
import coin5_v2_model as model
import coin5_v2_measure as study

def cadence(runs,cfg):
    pairs=list(zip(runs,runs[1:]))
    def stats(p):
        gaps=sorted((b['started_ms']-a['started_ms'])/60000 for a,b in p)
        return {'intervals':len(gaps),'p95_minutes':gaps[math.ceil(.95*len(gaps))-1] if gaps else None,
            'longest_minutes':max(gaps) if gaps else None,'over_10_minutes':sum(g>cfg['coverage_gap_minutes'] for g in gaps)}
    return {'all_starts':stats(pairs),'within_session':stats([(a,b) for a,b in pairs if a['session_id']==b['session_id']]),
        'between_sessions':stats([(a,b) for a,b in pairs if a['session_id']!=b['session_id']]),
        'note':'Loop starts are not evidence of complete provider data.'}

def restore():
    scan.cloud.pull_state();state=json.loads(scan.STATE.read_text(encoding='utf-8'))
    if not state.get('migration'):
        scan.cloud.git('fetch','--no-tags','origin','refs/heads/scanner-state-coin-tarama-5')
        sha=scan.cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
        old=json.loads(scan.cloud.git('show',sha+':state.json').stdout)
        state=model.migrate(old,sha,scan.now_ms())
    if state['rules_fingerprint']!=model.fingerprint():raise ValueError('Unversioned rule change')
    return state

def checkpoint(state):
    scan.render(state);scan.cloud.save(scan.STATE,state);scan.cloud.push_state()

def worker(minutes,channel):
    if not 1<=minutes<=110:raise ValueError('Session must be 1-110 minutes')
    scan.configure();cfg=model.config();state=restore();deadline=time.monotonic()+minutes*60
    session=os.environ.get('GITHUB_RUN_ID','local-'+str(scan.now_ms()))
    while time.monotonic()<deadline:
        tick=time.monotonic();start=scan.now_ms();row={'started_ms':start,'session_id':session,'scan_complete':False}
        try:
            scan.observe(state,cfg);row['scan_complete']=True
        except Exception as e:row['error']='observation: '+str(e)
        row['scan_finished_ms']=scan.now_ms();row['coverage']={v:x.get('coverage',{}) for v,x in state['venues'].items()}
        row['errors']=state.get('latest',{}).get('errors',{})
        state['runs'].append(row);state['runs']=state['runs'][-1000:];state['timing']=cadence(state['runs'],cfg)
        # Persist evidence and pending IDs before any external notification.
        checkpoint(state)
        try:scan.notify(state,channel,cfg)
        except Exception as e:row['notification_error']=str(e)
        try:study.measure(state,cfg,scan.now_ms())
        except Exception as e:row['measurement_error']=str(e)
        row['finished_ms']=scan.now_ms();row['duration_ms']=row['finished_ms']-start
        checkpoint(state)
        print(json.dumps({'started_ms':start,'finished_ms':row['finished_ms'],'scan_complete':row['scan_complete'],
            'latest':state.get('latest'),'pending':len(state['pending']),'delivered':len(state['delivery']),
            'timing':state['timing']},ensure_ascii=True),flush=True)
        remaining=deadline-time.monotonic()
        if remaining<=0:break
        pause=min(max(0,cfg['cycle_seconds']-(time.monotonic()-tick)),remaining)
        if pause:time.sleep(pause)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--minutes',type=int,default=110)
    p.add_argument('--channel',choices=['report','github_issue'],default='report');a=p.parse_args();worker(a.minutes,a.channel)
