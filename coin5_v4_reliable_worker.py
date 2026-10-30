"""Operational supervisor only. Frozen Coin5 V4 signal modules are unchanged."""
import argparse,json,math,os,subprocess,sys,time,traceback
from pathlib import Path
from coin5_v4_persistence import SafePublisher,PublicationError,clean

MAX_RESTARTS=1
RESTART_DELAY=20

def supervise(minutes,channel,launch=None,clock=time.monotonic,sleep=time.sleep,log=print):
    if not 1<=minutes<=110:raise ValueError('Bounded 1-110 minute session required')
    deadline=clock()+minutes*60;attempt=0
    launch=launch or (lambda args:subprocess.run(args,timeout=max(1,deadline-clock()+120)).returncode)
    while True:
        remaining=minutes if attempt==0 else min(110,math.floor((deadline-clock())/60))
        if remaining<1:return 75
        args=[sys.executable,'-u',str(Path(__file__).resolve()),'--child','--minutes',str(remaining),'--channel',channel,'--restart-index',str(attempt)]
        try:code=launch(args)
        except subprocess.TimeoutExpired:
            log(json.dumps({'supervisor':{'status':'original_session_budget_plus_checkpoint_grace_exhausted'}}),flush=True)
            return 124
        log(json.dumps({'supervisor':{'child_exit':code,'restart_index':attempt,'remaining_seconds':max(0,deadline-clock())}}),flush=True)
        if code==0:return 0
        if code not in (1,75) or attempt>=MAX_RESTARTS or deadline-clock()<RESTART_DELAY+60:return code
        sleep(RESTART_DELAY);attempt+=1

def child(minutes,channel,restart_index=0):
    import coin5_v4_worker as worker
    scan=worker.scan
    if os.environ.get('GITHUB_RUN_ID') and os.environ.get('GITHUB_REPOSITORY')!='selvisezgin01-ux/Coin-Tarama':
        print('Fixed repository runtime required',flush=True);return 78
    original_restore=worker.restore;original_checkpoint=worker.checkpoint;publisher=None
    def get_publisher():
        nonlocal publisher
        if publisher is None:publisher=SafePublisher(scan.ROOT,scan.OUT,worker.model.fingerprint(),os.environ.get('GITHUB_RUN_ID','local'))
        return publisher
    def checkpoint(state):
        scan.render(state);scan.cloud.save(scan.STATE,state);commit=get_publisher().publish()
        health=json.loads(get_publisher().health.read_text(encoding='utf-8'))
        state['operational_publication']={'previous_commit':commit,'previous_success_ms':health['time_ms'],
            'attempts':health['attempts'],'verified_prior_acceptance':health['verified_prior_acceptance']}
    def restore():
        state=original_restore();parent=(scan.OUT/'parent.txt').read_text(encoding='ascii').strip()
        recovered=get_publisher().recover_local(state,parent)
        recovered['runtime_policy']={'version':'v4-publication-recovery-v1','push_attempts':4,'push_budget_seconds':120,
            'retry_delays_seconds':[5,15,30],'maximum_child_restarts':1,'restart_delay_seconds':20,'original_session_deadline_preserved':True}
        if restart_index:
            restored=recovered.setdefault('operational_process_restarts',[])
            identity=(os.environ.get('GITHUB_RUN_ID','local'),restart_index)
            if not any((r['run_id'],r['restart_index'])==identity for r in restored):
                restored.append({'run_id':identity[0],'restart_index':restart_index,'observed_ms':scan.now_ms(),'references_repriced':False})
        checkpoint(recovered)
        return recovered
    worker.checkpoint=checkpoint;worker.restore=restore
    try:worker.worker(minutes,channel);return 0
    except PublicationError as error:
        print(json.dumps({'runtime_failure':{'category':error.category,'detail':error.detail,'restart_allowed':error.restart_allowed}},ensure_ascii=True),flush=True)
        return 75 if error.restart_allowed else 78
    except ValueError as error:
        print(json.dumps({'runtime_failure':{'category':'configuration','detail':clean(error),'restart_allowed':False}}),flush=True);return 78
    except Exception:
        print(clean(traceback.format_exc()),flush=True);return 1
    finally:
        worker.restore=original_restore;worker.checkpoint=original_checkpoint

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--child',action='store_true');p.add_argument('--minutes',type=int,default=110)
    p.add_argument('--restart-index',type=int,choices=[0,1],default=0)
    p.add_argument('--channel',choices=['github_issue','report'],default='report');args=p.parse_args()
    sys.exit(child(args.minutes,args.channel,args.restart_index) if args.child else supervise(args.minutes,args.channel))
