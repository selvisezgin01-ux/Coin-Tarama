"""Bounded durable V4 loop. Successful loop is not evidence of healthy data."""
import argparse,json,os,time
import coin5_v4_scan as scan
import coin5_v4_model as model
import coin5_v4_measure as study
import coin5_v3_measure as legacy_study
import coin5_v3_model as legacy_model
from coin5_v2_worker import cadence
def restore():
    # The generic cloud reader rejects any different fingerprint before a caller
    # can run its explicit migration. Validate the one approved V4 predecessor here.
    branch=scan.cloud.state_branch()
    if branch!=model.config()['state_branch']:raise ValueError('V4 branch isolation required')
    found=scan.cloud.git('ls-remote','--exit-code','--heads','origin','refs/heads/'+branch,allowed=(0,2))
    if found.returncode==2:
        scan.cloud.pull_state();s=json.loads(scan.STATE.read_text(encoding='utf-8'))
    else:
        scan.cloud.git('fetch','--no-tags','origin','refs/heads/'+branch)
        parent=scan.cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
        s=validate_state(json.loads(scan.cloud.git('show',parent+':state.json').stdout))
        scan.OUT.mkdir(parents=True,exist_ok=True);scan.cloud.save(scan.STATE,s)
        (scan.OUT/'parent.txt').write_text(parent,encoding='ascii')
    if not s.get('archive'):
        scan.cloud.git('fetch','--no-tags','origin','refs/heads/scanner-state-coin-tarama-5-v3')
        sha=scan.cloud.git('rev-parse','FETCH_HEAD').stdout.strip()
        old=json.loads(scan.cloud.git('show',sha+':state.json').stdout);s=model.migrate(old,sha,scan.now_ms())
    return validate_state(s)
def validate_state(s):
    current=model.fingerprint()
    previous='9827746f05ad8df4bb7eaaebdfc768271ebd9fa18381eeaf5d93cc564abef469'
    if s.get('version')=='coin-tarama-5-v4' and s.get('rules_fingerprint')==previous:
        s.setdefault('presentation_migrations',[]).append({'from_fingerprint':previous,'to_fingerprint':current,
            'observed_ms':scan.now_ms(),'reason':'Authorized Turkish display-text encoding correction; conditions unchanged',
            'references_repriced':False})
        s['rules_fingerprint']=current
    if s.get('version')!='coin-tarama-5-v4' or s['rules_fingerprint']!=current:raise ValueError('Unapproved V4 rules/state change')
    return s

def checkpoint(s):
    scan.render(s);scan.cloud.save(scan.STATE,s);scan.cloud.push_state()
def worker(minutes,channel):
    if not 1<=minutes<=110:raise ValueError('Bounded1-110min session required')
    scan.configure();cfg=model.config();s=restore();deadline=time.monotonic()+60*minutes
    session=os.environ.get('GITHUB_RUN_ID','local-'+str(scan.now_ms()))
    while time.monotonic()<deadline:
        tick=time.monotonic();start=scan.now_ms();r={'started_ms':start,'session_id':session,'scan_complete':False}
        try:scan.observe(s,cfg);r['scan_complete']=True
        except Exception as e:r['error']=str(e)
        r['scan_finished_ms']=scan.now_ms();r['errors']=s.get('latest',{}).get('errors',{})
        r['coverage']={g:{k:v.get(k) for k in ('active_catalog','valid_liquid_tickers','candles_evaluated','selected_for_candles','fresh_candidate_quotes')} for g,v in s['venues'].items()}
        s['runs'].append(r);s['runs']=s['runs'][-1000:]
        s['timing']=cadence(s['runs'],{'coverage_gap_minutes':10});checkpoint(s)
        try:scan.notify(s,channel,cfg)
        except Exception as e:r['notification_error']=str(e)
        # Save receipt promptly; expensive outcome reads never hide a successful send.
        checkpoint(s)
        try:
            legacy=s.get('legacy_v3');share=bool(legacy) and len(s['runs'])%3==0
            study.measure(s,{**cfg,'max_cases_measured_per_run':1 if share else cfg['max_cases_measured_per_run']},scan.now_ms())
            if share:legacy_study.measure(legacy,{**legacy_model.config(),'max_cases_measured_per_run':1},scan.now_ms())
        except Exception as e:r['measurement_error']=str(e)
        r['finished_ms']=scan.now_ms();r['duration_ms']=r['finished_ms']-start;checkpoint(s)
        print(json.dumps({'run':r,'latest':s.get('latest'),'deliveries':len(s['delivery'])},ensure_ascii=True),flush=True)
        pause=min(max(0,300-(time.monotonic()-tick)),max(0,deadline-time.monotonic()))
        if pause:time.sleep(pause)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--minutes',type=int,default=110);p.add_argument('--channel',choices=['github_issue','report'],default='report')
    a=p.parse_args();worker(a.minutes,a.channel)
