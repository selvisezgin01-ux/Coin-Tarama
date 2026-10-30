"""Continuously scheduled PUBLIC discovery only. No wallet keys, trading, or notifications.

The local launcher may publish feed.json to the user's fixed repository. SQLite is
the durable identity/audit store. Sleep/network failures remain recorded gaps.
"""
import argparse,datetime,hashlib,json,sqlite3,time,uuid
from pathlib import Path
import meme_sources as source

class Collector:
    def __init__(self,path,cfg,clock=lambda:int(time.time()*1000)):
        self.path=Path(path);self.path.parent.mkdir(parents=True,exist_ok=True);self.cfg=cfg;self.clock=clock;self.run_id=uuid.uuid4().hex
        self.db=sqlite3.connect(self.path);self.db.execute('PRAGMA journal_mode=WAL')
        self.db.executescript('CREATE TABLE IF NOT EXISTS identities(chain TEXT,mint TEXT,pool TEXT,created_ms INTEGER,first_seen_ms INTEGER,last_seen_ms INTEGER,PRIMARY KEY(chain,pool)); CREATE TABLE IF NOT EXISTS pages(id INTEGER PRIMARY KEY,ms INTEGER,chain TEXT,page INTEGER,returned INTEGER,oldest_ms INTEGER,error TEXT,identity_json TEXT); CREATE TABLE IF NOT EXISTS progress(chain TEXT PRIMARY KEY,json TEXT);')
        self.progress={chain:json.loads(text) for chain,text in self.db.execute('SELECT chain,json FROM progress')}
        for chain in cfg['networks']:self.progress.setdefault(chain,{'page':1,'due_ms':0,'cursor_ms':None,'covered_until_ms':None,'gaps':[]})
        if any('429' in str(p.get('last_error','')) for p in self.progress.values()):
            cfg['discovery']['gecko_minimum_request_interval_seconds']=max(25,cfg['discovery']['gecko_minimum_request_interval_seconds'])
    def next_chain(self):
        return min(self.progress,key=lambda c:(self.progress[c]['due_ms'],0 if c=='solana' else 1,c))
    def consume(self,chain,payload,now,error=None):
        p=self.progress[chain];page=p['page'];rows=[];times=[];invalid=0
        if p.get('cycle_started_ms') is None:p['cycle_started_ms']=now;p['boundary_ms']=(p['cursor_ms'] or now)-self.cfg['v7']['collector_overlap_seconds']*1000
        if error is None:
            data=payload.get('data')
            if not isinstance(data,list):raise ValueError('Malformed discovery page')
            included={r['id']:r.get('attributes',{}) for r in payload.get('included',[])}
            for raw in data:
                created=source.ms_iso((raw.get('attributes') or {}).get('pool_created_at'))
                if created is not None:times.append(created)
                try:
                    a=source.normalize_pool(chain,raw,included)
                    if a['pool_created_ms'] is None or not 0<a['pool_created_ms']<=now:raise ValueError('Future/missing creation')
                    self.db.execute('INSERT INTO identities VALUES(?,?,?,?,?,?) ON CONFLICT(chain,pool) DO UPDATE SET last_seen_ms=excluded.last_seen_ms',
                        (chain,a['mint'],a['pool'],a['pool_created_ms'],now,now))
                    rows.append({'mint':a['mint'],'pool':a['pool'],'created_ms':a['pool_created_ms']})
                except (ValueError,KeyError,TypeError):invalid+=1
        else:data=[]
        self.db.execute('INSERT INTO pages(ms,chain,page,returned,oldest_ms,error,identity_json) VALUES(?,?,?,?,?,?,?)',
            (now,chain,page,len(data),min(times) if times else None,error,json.dumps(rows)))
        reached=not error and (not data or bool(times and min(times)<=p['boundary_ms']))
        exhausted=page>=self.cfg['v7']['collector_max_pages']
        if reached or exhausted or error:
            if reached:p['covered_until_ms']=p['cycle_started_ms']
            else:p['gaps'].append({'from_ms':p['boundary_ms'],'to_ms':now,'oldest_returned_ms':min(times) if times else None,
                                   'reason':error or 'page_budget_exhausted','complete':False})
            # Progress head and unresolved gaps are separate. An old hole never silently vanishes.
            p['cursor_ms']=p['cycle_started_ms'];p['cycle_started_ms']=None;p['page']=1
            p['due_ms']=now+(900000 if error and any(x in error for x in ('429','403','401','418')) else self.cfg['v7']['collector_network_intervals_seconds'][chain]*1000)
        else:p['page']+=1;p['due_ms']=now
        p.update(last_observed_ms=now,last_error=error,last_page=page,invalid_rows=invalid)
        self.db.execute('INSERT INTO progress VALUES(?,?) ON CONFLICT(chain) DO UPDATE SET json=excluded.json',(chain,json.dumps(p)));self.db.commit()
    def feed(self,now=None):
        now=self.clock() if now is None else now;start=now-self.cfg['v7']['collector_feed_window_minutes']*60000
        identities=[dict(zip(('chain','mint','pool','created_ms','first_seen_ms'),r)) for r in self.db.execute(
            'SELECT chain,mint,pool,created_ms,first_seen_ms FROM identities WHERE created_ms>=? ORDER BY chain,mint,pool',(start,))]
        coverage={c:{**p,'gaps':p['gaps'][-20:],'unresolved_gap_count':len(p['gaps'])} for c,p in self.progress.items()}
        return {'version':'meme-v7-discovery-feed','observed_ms':now,'run_id':self.run_id,'networks':coverage,
                'identities':identities,'total_identities_durable':self.db.execute('SELECT COUNT(*) FROM identities').fetchone()[0],
                'minimum_request_interval_seconds':self.cfg['discovery']['gecko_minimum_request_interval_seconds'],
                'scope':'provider-indexed-new-pools-not-complete-onchain-discovery','complete_onchain_coverage':False}
    def step(self,client):
        now=self.clock();chain=self.next_chain();p=self.progress[chain]
        if p['due_ms']>now:return (p['due_ms']-now)/1000
        path=f"networks/{self.cfg['networks'][chain]['gecko']}/new_pools?page={p['page']}&include=base_token,quote_token"
        try:self.consume(chain,client.gecko(path),self.clock())
        except Exception as exc:self.consume(chain,{},self.clock(),str(exc))
        return 0

def run(dbpath,cfg,export,publish=None,stop=None):
    collector=Collector(dbpath,cfg);client=source.Client(cfg);last_export=0;last_activity=0
    while not (stop and stop()):
        now=int(time.time()*1000)
        if last_activity and now-last_activity>180000:
            for c,p in collector.progress.items():p['gaps'].append({'from_ms':last_activity,'to_ms':now,'reason':'local_process_sleep_or_pause','complete':False})
        delay=collector.step(client);last_activity=int(time.time()*1000)
        # A rejection remains a 15-minute provider-wide cooldown, never host rotation.
        if client.blocked:
            pause=last_activity+900000
            if any('429' in str(p.get('last_error','')) for p in collector.progress.values()):
                cfg['discovery']['gecko_minimum_request_interval_seconds']=min(60,max(25,2*cfg['discovery']['gecko_minimum_request_interval_seconds']))
            for chain,p in collector.progress.items():
                p['due_ms']=max(p['due_ms'],pause)
                collector.db.execute('INSERT INTO progress VALUES(?,?) ON CONFLICT(chain) DO UPDATE SET json=excluded.json',(chain,json.dumps(p)))
            collector.db.commit()
            client=source.Client(cfg)
        if last_activity-last_export>=60000:
            feed=collector.feed();temp=Path(export).with_suffix('.tmp');temp.write_text(json.dumps(feed,ensure_ascii=False),encoding='utf-8');temp.replace(export)
            if publish:
                try:publish(feed)
                except Exception as exc:
                    Path(export).with_name('publish_health.json').write_text(json.dumps({'observed_ms':last_activity,'status':'failed','error':str(exc)}),encoding='utf-8')
            last_export=last_activity
        time.sleep(min(5,max(.2,delay)))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--database',required=True);p.add_argument('--export',required=True);a=p.parse_args()
    cfg=json.loads((Path(__file__).parent/'meme_v7_config.json').read_text(encoding='utf-8'));run(a.database,cfg,Path(a.export))
