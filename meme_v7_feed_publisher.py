"""Single-writer CAS publisher for the public identity feed, separate from scanner state."""
import base64,json,os,time
from pathlib import Path
from urllib.request import Request,urlopen
from meme_v7_persistence import atomic,clean

REPO='selvisezgin01-ux/Coin-Tarama';BRANCH='scanner-feed-meme-v7'

def api(path,body=None,method=None):
    token=os.environ.get('GH_TOKEN')
    if not token:raise ValueError('Feed publisher credential missing')
    req=Request('https://api.github.com/repos/'+REPO+path,
        data=None if body is None else json.dumps(body).encode(),method=method,
        headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','Content-Type':'application/json','User-Agent':'CoinTaramaMemeV7Feed'})
    # This fixed repository has no redirects; reject before credentials could leave GitHub.
    import meme_sources
    try:
        with meme_sources.build_opener(meme_sources.NoRedirect()).open(req,timeout=25) as response:
            data=response.read();return json.loads(data) if data else {}
    except Exception as exc:raise RuntimeError(clean(type(exc).__name__+': '+str(exc))) from None

class Publisher:
    def __init__(self,directory,request=api):
        self.directory=Path(directory);self.directory.mkdir(exist_ok=True,parents=True);self.request=request
        self.journal=self.directory/'feed_publication.json';self.health=self.directory/'feed_publication_health.json'
    def publish(self,feed):
        if feed.get('version')!='meme-v7-discovery-feed':raise ValueError('Feed schema mismatch')
        branches=self.request('/branches?per_page=100');branch=next((b for b in branches if b['name']==BRANCH),None)
        current=branch['commit']['sha'] if branch else ''
        journal=json.loads(self.journal.read_text(encoding='utf-8')) if self.journal.exists() else {}
        expected=journal.get('accepted_parent',current)
        if current==journal.get('candidate_commit'):
            expected=current # Prior push accepted, response lost.
        if current!=expected:raise RuntimeError('Feed branch changed by another writer; refused overwrite')
        blob=self.request('/git/blobs',{'content':json.dumps(feed,ensure_ascii=False,separators=(',',':')),'encoding':'utf-8'},'POST')['sha']
        tree=self.request('/git/trees',{'tree':[{'path':'feed.json','mode':'100644','type':'blob','sha':blob}]},'POST')['sha']
        commit=self.request('/git/commits',{'message':'Meme V7 public discovery feed','tree':tree,'parents':[current] if current else []},'POST')['sha']
        atomic(self.journal,json.dumps({'accepted_parent':current,'candidate_commit':commit,'feed_observed_ms':feed['observed_ms']}))
        if current:self.request('/git/refs/heads/'+BRANCH,{'sha':commit,'force':False},'PATCH')
        else:self.request('/git/refs',{'ref':'refs/heads/'+BRANCH,'sha':commit},'POST')
        atomic(self.journal,json.dumps({'accepted_parent':commit,'candidate_commit':commit,'feed_observed_ms':feed['observed_ms']}))
        atomic(self.health,json.dumps({'status':'published','commit':commit,'feed_observed_ms':feed['observed_ms'],'published_ms':int(time.time()*1000)}))
        return commit
