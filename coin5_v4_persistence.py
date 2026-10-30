"""Bounded, idempotent Coin5 V4 publication; never force-push or reprice data."""
import hashlib,json,os,re,subprocess,time
from pathlib import Path

BRANCH='scanner-state-coin-tarama-5-v4'
ATTEMPTS=4
DELAYS=(5,15,30)
BUDGET_SECONDS=120

def clean(text):
    text=str(text)
    for key in ('GH_TOKEN','GITHUB_TOKEN'):
        value=os.environ.get(key)
        if value and len(value)>3:text=text.replace(value,'[REDACTED]')
    text=re.sub(r'https?://[^\s/@]+:[^\s/@]+@', 'https://[REDACTED]@',text)
    text=re.sub(r'(?i)(authorization\s*[:=]\s*)(?:basic|bearer)\s+[^\s]+',r'\1[REDACTED]',text)
    text=re.sub(r'(?:gh[pousr]_[A-Za-z0-9_]{15,}|github_pat_[A-Za-z0-9_]{15,})','[REDACTED]',text)
    return text[-6000:]

def canonical(value):return hashlib.sha256(json.dumps(value,sort_keys=True,allow_nan=False).encode()).hexdigest()

def atomic(path,text):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+'.tmp');temp.write_text(text,encoding='utf-8');temp.replace(path)

def write_json(path,value):atomic(path,json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False))

class PublicationError(RuntimeError):
    def __init__(self,category,detail):
        self.category=category;self.detail=clean(detail)
        super().__init__(category+': '+self.detail)
    @property
    def restart_allowed(self):return self.category=='transient'

def category(result):
    text=(result.stderr+'\n'+result.stdout).lower()
    if re.search(r'authentication failed|could not read username|permission denied|permission to .+ denied|http[^\n]*(?:401|403)|protected branch|gh006|gh013|repository not found',text):return 'permission'
    if re.search(r'non-fast-forward|fetch first|\[rejected\]|cannot lock ref|stale info',text):return 'conflict'
    if result.returncode==124 or re.search(r'could not resolve host|failed to connect|connection (?:reset|closed|timed out)|timed out|timeout|tls|ssl|http[^\n]*(?:408|429|500|502|503|504)|remote end hung up|recv failure|send failure|temporarily unavailable|broken pipe',text):return 'transient'
    return 'unknown'

class GitRunner:
    def __init__(self,root):self.root=Path(root)
    def __call__(self,*args,input=None,timeout=30):
        command=['git','-c','credential.interactive=never','-c','http.lowSpeedLimit=1024','-c','http.lowSpeedTime=15',*args]
        try:
            r=subprocess.run(command,cwd=self.root,input=None if input is None else input.encode('utf-8'),capture_output=True,timeout=timeout)
            return subprocess.CompletedProcess(args,r.returncode,r.stdout.decode('utf-8',errors='replace'),r.stderr.decode('utf-8',errors='replace'))
        except subprocess.TimeoutExpired:
            return subprocess.CompletedProcess(args,124,'','Git command timed out; remote acceptance must be verified')

class SafePublisher:
    def __init__(self,root,out,fingerprint,run_id,runner=None,clock=time.monotonic,sleep=time.sleep,log=print):
        self.root=Path(root).resolve();self.out=Path(out).resolve()
        if not self.out.is_relative_to(self.root):raise ValueError('Output must be inside scanner workspace')
        self.out.mkdir(parents=True,exist_ok=True);self.fingerprint=fingerprint;self.run_id=str(run_id)
        self.git=runner or GitRunner(self.root);self.clock=clock;self.sleep=sleep;self.log=log
        self.journal=self.out/'publication_journal.json';self.snapshot=self.out/'recovery_state.json'
        self.health=self.out/'publication_health.json'

    def _run(self,args,deadline,input=None):
        remaining=deadline-self.clock()
        if remaining<=0:raise PublicationError('transient','Publication time budget exhausted')
        r=self.git(*args,input=input,timeout=min(30,remaining))
        if r.returncode:
            raise PublicationError(category(r),json.dumps({'operation':args[0],'exit_code':r.returncode,'stderr':clean(r.stderr),'stdout':clean(r.stdout)}))
        return r.stdout.strip()

    def _remote(self,deadline):
        text=self._run(('ls-remote','--heads','origin','refs/heads/'+BRANCH),deadline)
        if not text:return ''
        lines=text.splitlines()
        if len(lines)!=1 or len(lines[0].split())!=2:raise PublicationError('conflict','Unexpected remote branch response')
        sha,ref=lines[0].split()
        if ref!='refs/heads/'+BRANCH or not re.fullmatch('[0-9a-f]{40,64}',sha):raise PublicationError('conflict','Remote branch identity mismatch')
        return sha

    def _event(self,value):
        # Detail strings are already individually redacted; never truncate JSON.
        write_json(self.health,value);self.log(json.dumps({'publication':value},ensure_ascii=True),flush=True)

    def publish(self):
        deadline=self.clock()+BUDGET_SECONDS
        state_path=self.out/'state.json';parent_path=self.out/'parent.txt'
        if not parent_path.exists():raise PublicationError('local','No validated publication parent; restore first')
        parent=parent_path.read_text(encoding='ascii').strip()
        if parent and not re.fullmatch('[0-9a-f]{40,64}',parent):raise PublicationError('local','Invalid saved publication parent')
        state=json.loads(state_path.read_text(encoding='utf-8'))
        if state.get('version')!='coin-tarama-5-v4' or state.get('rules_fingerprint')!=self.fingerprint:
            raise PublicationError('configuration','Refuse publication of unexpected rules/state')
        write_json(self.snapshot,state)
        j={'version':1,'status':'preparing','run_id':self.run_id,'branch':BRANCH,'fingerprint':self.fingerprint,
            'expected_parent':parent,'candidate_commit':None,'canonical_state_sha256':canonical(state),'prepared_ms':int(time.time()*1000)}
        write_json(self.journal,j)
        self._run(('config','user.name','github-actions[bot]'),deadline)
        self._run(('config','user.email','41898282+github-actions[bot]@users.noreply.github.com'),deadline)
        records=[]
        for name in ('state.json','report.md'):
            path=self.out/name
            if path.exists():records.append('100644 blob '+self._run(('hash-object','-w',str(path)),deadline)+'\t'+name+'\n')
        tree=self._run(('mktree',),deadline,input=''.join(records))
        args=('commit-tree',tree)+ (('-p',parent) if parent else ())
        commit=self._run(args,deadline,input='Scanner checkpoint '+self.run_id+'\n')
        if not re.fullmatch('[0-9a-f]{40,64}',commit):raise PublicationError('local','Invalid prepared commit identity')
        j.update(status='prepared',candidate_commit=commit)
        write_json(self.journal,j)
        last=None
        for attempt in range(1,ATTEMPTS+1):
            try:
                remote=self._remote(deadline)
                acknowledged=remote==commit
                if remote not in (parent,commit):raise PublicationError('conflict','Remote state changed; no overwrite or force-push was attempted')
                if not acknowledged:self._run(('push','origin',commit+':refs/heads/'+BRANCH),deadline)
                atomic(parent_path,commit)
                j.update(status='published',published_ms=int(time.time()*1000),attempts=attempt,verified_prior_acceptance=acknowledged)
                write_json(self.journal,j);self._event({'status':'published','attempts':attempt,'commit':commit,'verified_prior_acceptance':acknowledged,'time_ms':j['published_ms']})
                return commit
            except PublicationError as error:
                last=error;j.update(status='failed',category=error.category,detail=error.detail,attempts=attempt,failed_ms=int(time.time()*1000))
                write_json(self.journal,j);self._event({'status':'failed_attempt','attempt':attempt,'category':error.category,'detail':error.detail,'time_ms':j['failed_ms']})
                if not error.restart_allowed or attempt>=ATTEMPTS:raise
                pause=DELAYS[attempt-1]
                if self.clock()+pause>=deadline:raise PublicationError('transient','Publication retry budget exhausted') from None
                self.sleep(pause)
        raise last

    def recover_local(self,remote_state,remote_parent):
        if not self.journal.exists():return remote_state
        j=json.loads(self.journal.read_text(encoding='utf-8'))
        if j.get('status')=='published':return remote_state
        if j.get('run_id')!=self.run_id or j.get('branch')!=BRANCH or j.get('fingerprint')!=self.fingerprint:
            raise PublicationError('configuration','Recovery journal identity mismatch')
        if remote_state.get('rules_fingerprint')!=self.fingerprint:raise PublicationError('configuration','Remote rules changed during recovery')
        if remote_parent==j['candidate_commit']:
            if canonical(remote_state)!=j['canonical_state_sha256']:raise PublicationError('conflict','Accepted remote snapshot differs from prepared state')
            return remote_state
        if remote_parent!=j['expected_parent']:raise PublicationError('conflict','Another writer changed remote state; local snapshot not replayed')
        local=json.loads(self.snapshot.read_text(encoding='utf-8'))
        if canonical(local)!=j['canonical_state_sha256']:raise PublicationError('local','Recovery snapshot checksum mismatch')
        # Original observation prices, timestamps, pending IDs and receipts stay exact.
        local.setdefault('operational_recoveries',[]).append({'observed_ms':int(time.time()*1000),'source':'same_job_prepared_snapshot',
            'run_id':self.run_id,'original_prepared_ms':j['prepared_ms'],'references_repriced':False})
        return local
