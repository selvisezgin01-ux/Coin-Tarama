import json,os,subprocess,tempfile,unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch
import coin5_v4_persistence as p
import coin5_v4_reliable_worker as supervisor

P=Path(__file__).resolve().parent
OLD='e'*40;COMMIT='d'*40
def silent(*args,**kwargs):pass
class Clock:
    def __init__(self):self.t=0;self.pauses=[]
    def now(self):return self.t
    def sleep(self,seconds):self.pauses.append(seconds);self.t+=seconds
class FakeGit:
    def __init__(self,results=None):self.remote=OLD;self.results=list(results or []);self.calls=[];self.pushes=[]
    def __call__(self,*args,input=None,timeout=30):
        self.calls.append(args);text=''
        if args[0]=='hash-object':text='a'*40
        if args[0]=='mktree':text='c'*40
        if args[0]=='commit-tree':text=COMMIT
        if args[0]=='ls-remote':text=self.remote+'\trefs/heads/'+p.BRANCH+'\n' if self.remote else ''
        if args[0]=='push':
            self.pushes.append(args)
            code,message,accepted=self.results.pop(0) if self.results else (0,'',True)
            if accepted:self.remote=COMMIT
            return subprocess.CompletedProcess(args,code,'',message)
        return subprocess.CompletedProcess(args,0,text,'')

class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=P);self.root=Path(self.tmp.name);self.out=self.root/'out';self.out.mkdir()
        self.state={'version':'coin-tarama-5-v4','rules_fingerprint':'rules','assets':{'a':{'initial_price':.0013615,'created_ms':12345}},
            'pending':[{'id':'same-event','observed_ms':12345}], 'delivery':[{'id':'already-sent'}]}
        p.write_json(self.out/'state.json',self.state);p.atomic(self.out/'parent.txt',OLD);p.atomic(self.out/'report.md','Report')
        self.clock=Clock()
    def tearDown(self):self.tmp.cleanup()
    def writer(self,git):return p.SafePublisher(self.root,self.out,'rules','run1',runner=git,clock=self.clock.now,sleep=self.clock.sleep,log=silent)
    def test_normal_publication_preserves_quote_and_receipt_ids(self):
        git=FakeGit();self.writer(git).publish()
        self.assertEqual((self.out/'parent.txt').read_text(),COMMIT)
        self.assertEqual(json.loads((self.out/'state.json').read_text()),self.state);self.assertEqual(len(git.pushes),1)
    def test_network_timeout_budget_is_finite_even_before_push(self):
        git=FakeGit()
        def timeout(*args,**kwargs):
            if args[0]=='ls-remote':
                self.clock.t+=kwargs['timeout'];return subprocess.CompletedProcess(args,124,'','command timed out')
            return git(*args,**kwargs)
        with self.assertRaises(p.PublicationError):self.writer(timeout).publish()
        self.assertLessEqual(self.clock.t,120);self.assertFalse(git.pushes)
        self.assertEqual(json.loads((self.out/'recovery_state.json').read_text()),self.state)
    def test_preparation_timeout_keeps_snapshot_for_same_job_recovery(self):
        def fail(*args,**kwargs):return subprocess.CompletedProcess(args,124,'','command timed out')
        writer=self.writer(fail)
        with self.assertRaises(p.PublicationError):writer.publish()
        self.assertEqual(json.loads((self.out/'publication_journal.json').read_text())['status'],'preparing')
        restored=writer.recover_local({'rules_fingerprint':'rules'},OLD)
        self.assertEqual(restored['assets'],self.state['assets']);self.assertEqual(restored['pending'],self.state['pending'])
    def test_transient_push_is_retried_with_same_commit(self):
        git=FakeGit([(128,'RPC failed; HTTP 503 Service Unavailable',False),(0,'',True)])
        self.writer(git).publish();self.assertEqual(self.clock.pauses,[5]);self.assertEqual(git.pushes[0],git.pushes[1])
        self.assertFalse(any('--force' in arg for args in git.calls for arg in args))
    def test_accepted_push_with_lost_response_is_not_pushed_twice(self):
        git=FakeGit([(124,'command timed out',True)])
        self.writer(git).publish();self.assertEqual(len(git.pushes),1)
        self.assertTrue(json.loads((self.out/'publication_journal.json').read_text())['verified_prior_acceptance'])
    def test_permission_error_stops_without_retry(self):
        git=FakeGit([(128,'remote: Permission to repo denied. The requested URL returned error: 403',False)])
        with self.assertRaises(p.PublicationError) as raised:self.writer(git).publish()
        self.assertEqual(raised.exception.category,'permission');self.assertFalse(self.clock.pauses)
    def test_other_writer_is_never_overwritten(self):
        git=FakeGit();git.remote='f'*40
        with self.assertRaises(p.PublicationError) as raised:self.writer(git).publish()
        self.assertEqual(raised.exception.category,'conflict');self.assertFalse(git.pushes)
    def test_non_fast_forward_is_not_rebased_or_forced(self):
        git=FakeGit([(1,'[rejected] non-fast-forward',False)])
        with self.assertRaises(p.PublicationError) as raised:self.writer(git).publish()
        self.assertEqual(raised.exception.category,'conflict');self.assertEqual(len(git.pushes),1);self.assertFalse(self.clock.pauses)
    def test_bounded_attempts_leave_recoverable_snapshot(self):
        git=FakeGit([(128,'Could not resolve host: github.com',False)]*4)
        with self.assertRaises(p.PublicationError) as raised:self.writer(git).publish()
        self.assertTrue(raised.exception.restart_allowed);self.assertEqual(len(git.pushes),4);self.assertEqual(self.clock.pauses,[5,15,30])
        self.assertEqual(json.loads((self.out/'recovery_state.json').read_text()),self.state)
    def test_unclassified_git_error_is_not_blindly_retried(self):
        git=FakeGit([(128,'unclassified failure',False)])
        with self.assertRaises(p.PublicationError) as raised:self.writer(git).publish()
        self.assertEqual(raised.exception.category,'unknown');self.assertFalse(self.clock.pauses)
    def fail_prepared(self):
        git=FakeGit([(128,'Could not resolve host: github.com',False)]*4);writer=self.writer(git)
        with self.assertRaises(p.PublicationError):writer.publish()
        return writer
    def test_same_job_recovery_keeps_original_prices_times_pending_and_receipts(self):
        writer=self.fail_prepared();remote={'version':'coin-tarama-5-v4','rules_fingerprint':'rules','assets':{},'pending':[]}
        restored=writer.recover_local(remote,OLD)
        for key in ('assets','pending','delivery'):self.assertEqual(restored[key],self.state[key])
        self.assertFalse(restored['operational_recoveries'][0]['references_repriced'])
    def test_recovery_of_accepted_snapshot_uses_remote_without_replay(self):
        writer=self.fail_prepared();remote=deepcopy(self.state)
        self.assertIs(writer.recover_local(remote,COMMIT),remote)
    def test_recovery_refuses_changed_remote_parent(self):
        writer=self.fail_prepared()
        with self.assertRaises(p.PublicationError):writer.recover_local(self.state,'f'*40)
    def test_recovery_refuses_other_job_or_modified_snapshot(self):
        writer=self.fail_prepared();writer.run_id='another-job'
        with self.assertRaises(p.PublicationError):writer.recover_local(self.state,OLD)
        writer.run_id='run1';p.write_json(self.out/'recovery_state.json',{**self.state,'pending':[]})
        with self.assertRaises(p.PublicationError):writer.recover_local(self.state,OLD)
    def test_wrong_rules_never_publish(self):
        bad={**self.state,'rules_fingerprint':'changed'};p.write_json(self.out/'state.json',bad);git=FakeGit()
        with self.assertRaises(p.PublicationError):self.writer(git).publish()
        self.assertFalse(git.calls)
    def test_long_diagnostic_is_redacted_without_corrupting_journal(self):
        token='ghs_'+'z'*40;git=FakeGit([(128,'Permission denied '+token+' '+'x'*8000,False)])
        with patch.dict(os.environ,{'GH_TOKEN':token}):
            with self.assertRaises(p.PublicationError):self.writer(git).publish()
        data=json.loads((self.out/'publication_health.json').read_text());self.assertNotIn(token,json.dumps(data))
    def test_credential_forms_are_masked(self):
        text='Authorization: Basic abc123 https://user:password@github.com/path ghs_'+'z'*40
        cleaned=p.clean(text);self.assertNotIn('abc123',cleaned);self.assertNotIn('password',cleaned);self.assertNotIn('ghs_',cleaned)

class SupervisorTests(unittest.TestCase):
    def test_hard_session_timeout_does_not_start_another_child(self):
        clock=Clock()
        def timeout(args):raise subprocess.TimeoutExpired(args,120)
        self.assertEqual(supervisor.supervise(1,'report',timeout,clock.now,clock.sleep,silent),124)
        self.assertFalse(clock.pauses)
    def test_child_lifecycle_keeps_checkpoint_before_notification_and_restores_hooks(self):
        import contextlib,io
        import coin5_v4_worker as worker
        import coin5_v4_model as model
        with tempfile.TemporaryDirectory(dir=P) as directory:
            root=Path(directory);out=root/'out';out.mkdir();s=model.new_state()
            s['assets']={'fixture':{'initial_price':.0013615,'created_ms':12345}}
            calls=[];git=FakeGit();real_checkpoint=worker.checkpoint
            def restore():p.atomic(out/'parent.txt',OLD);p.write_json(out/'state.json',s);return s
            def factory(repo,output,fp,run_id):return p.SafePublisher(repo,output,fp,run_id,runner=git,sleep=lambda _:None,log=silent)
            def fake_worker(minutes,channel):
                restored=worker.restore();worker.checkpoint(restored)
                calls.append('notification_allowed_after_checkpoint')
                self.assertEqual(json.loads((out/'publication_journal.json').read_text())['status'],'published')
                self.assertEqual(restored['assets'],s['assets'])
            with patch.object(worker.scan,'ROOT',root),patch.object(worker.scan,'OUT',out),patch.object(worker.scan,'STATE',out/'state.json'),patch.object(worker.scan,'render',side_effect=lambda _:p.atomic(out/'report.md','fixture')),patch.object(worker,'restore',side_effect=restore) as original_restore,patch.object(worker,'worker',side_effect=fake_worker),patch.object(supervisor,'SafePublisher',side_effect=factory),patch.dict(os.environ,{'GITHUB_RUN_ID':'fixture-run','GITHUB_REPOSITORY':'selvisezgin01-ux/Coin-Tarama'}),contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(supervisor.child(1,'report'),0)
                self.assertIs(worker.restore,original_restore);self.assertIs(worker.checkpoint,real_checkpoint)
            self.assertEqual(calls,['notification_allowed_after_checkpoint'])
    def test_fixed_repository_rejection_does_not_restart(self):
        with patch.dict(os.environ,{'GITHUB_RUN_ID':'test','GITHUB_REPOSITORY':'other/repo'}),patch('builtins.print'):
            self.assertEqual(supervisor.child(1,'report'),78)
    def test_restart_is_once_and_uses_remaining_session_budget(self):
        clock=Clock();calls=[]
        def launch(args):
            calls.append(args);clock.t+=120
            return 75 if len(calls)==1 else 0
        self.assertEqual(supervisor.supervise(10,'report',launch,clock.now,clock.sleep,silent),0)
        self.assertEqual([args[args.index('--minutes')+1] for args in calls],['10','7']);self.assertEqual(clock.pauses,[20])
    def test_persistent_failure_does_not_create_restart_loop(self):
        clock=Clock();calls=[]
        def launch(args):calls.append(args);return 75
        self.assertEqual(supervisor.supervise(10,'report',launch,clock.now,clock.sleep,silent),75);self.assertEqual(len(calls),2)
    def test_permission_and_manual_cancellation_do_not_restart(self):
        for code in (78,-15,-2):
            clock=Clock();calls=[]
            def launch(args):calls.append(args);return code
            self.assertEqual(supervisor.supervise(10,'report',launch,clock.now,clock.sleep,silent),code);self.assertEqual(len(calls),1)
    def test_unexpected_crash_gets_only_one_controlled_restart(self):
        clock=Clock();codes=iter((1,0));self.assertEqual(supervisor.supervise(10,'report',lambda _:next(codes),clock.now,clock.sleep,silent),0)
    def test_no_restart_beyond_original_deadline(self):
        clock=Clock();calls=[]
        def launch(args):calls.append(args);clock.t+=50;return 75
        self.assertEqual(supervisor.supervise(1,'report',launch,clock.now,clock.sleep,silent),75);self.assertEqual(len(calls),1)
    def test_frozen_signal_fingerprint_is_still_original_v4(self):
        import coin5_v4_model as model
        self.assertEqual(model.fingerprint(),'a037f92f3df635673a8f8a00f16adf14d5f7957088fdc5e046a7043f7251d685')

if __name__=='__main__':unittest.main()
