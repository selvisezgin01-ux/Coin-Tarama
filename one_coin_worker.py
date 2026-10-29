"""Independent bounded GitHub session. No exchange or wallet signing credentials."""
import argparse,json,os,re,time
from pathlib import Path
import one_coin as watch

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'cloud_output_1_coin'

def batches(events,limit=45000):
    chunks=[];current=[];size=0
    for e in events:
        text=event_text(e);length=len(text)
        if current and size+length>limit:chunks.append(current);current=[];size=0
        current.append(e);size+=length
    if current:chunks.append(current)
    return chunks
def event_text(e):
    lines=['**'+e['kind']+'** · '+watch.stamp(e['observed_ms']),e['text']]
    if e.get('mint'):lines+=['CA (Solana):','```text\n'+e['mint']+'\n```']
    d=e.get('details') or {};signature=d.get('tx') or d.get('signature')
    if signature and re.fullmatch(r'[1-9A-HJ-NP-Za-km-z]{64,90}',signature):lines+=['[Zincir işlemi](https://solscan.io/tx/'+signature+')']
    if d.get('block_ms'):lines+=['Zincir zamanı: '+watch.stamp(d['block_ms'])]
    return '\n\n'.join(lines)
def notify(s,cloud,checkpoint):
    repo=os.environ['GITHUB_REPOSITORY']
    if repo!='selvisezgin01-ux/Coin-Tarama':raise ValueError('Fixed authorized repository required')
    token=os.environ.get('GH_TOKEN')
    if not token:raise RuntimeError('Missing GitHub token')
    headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
    base='https://api.github.com/repos/'+repo
    recent=cloud.http_json(base+'/issues?state=all&sort=created&direction=desc&per_page=100',headers=headers,label='1 coin issue lookup') if s['pending'] else []
    receipts={r['id'] for r in s['delivery']}
    # At-least-once publication with markers: recover a posted Issue after a lost checkpoint.
    for chunk in batches(s['pending'])[:6]:
        unsent=[e for e in chunk if e['id'] not in receipts]
        if not unsent:continue
        for e in list(unsent):
            marker='<!-- 1-coin:'+e['id']+' -->'
            found=next((i for i in recent if not i.get('pull_request') and i.get('user',{}).get('login')=='github-actions[bot]' and marker in (i.get('body') or '')),None)
            if found:
                s['delivery'].append({'id':e['id'],'issue':found['number'],'url':found['html_url'],'delivered_ms':watch.now(),'recovered':True});receipts.add(e['id']);unsent.remove(e)
        if unsent:
            recipient=os.environ.get('COIN_NOTIFY_USER') or 'selvisezgin01-ux'
            if not re.fullmatch(r'[A-Za-z0-9-]{1,39}',recipient):raise ValueError('Invalid notification recipient')
            body='@'+recipient+'\n\n# 1 coin\n\n'+'\n\n---\n\n'.join(event_text(e) for e in unsent)
            body+='\n\n[Rapor](https://github.com/'+repo+'/blob/scanner-state-1-coin/report.md)\n\nİşlem örneği ve izlenen adresler sınırlıdır. Transfer alım değildir; cüzdan bağlantısı aynı sahiplik kanıtı değildir. Veri eksikliği raporda gösterilir.\n\n'+'\n'.join('<!-- 1-coin:'+e['id']+' -->' for e in unsent)
            answer=cloud.http_json(base+'/issues',{'title':'1 coin · '+str(len(unsent))+' yeni hareket · '+watch.stamp(watch.now()),'body':body},headers=headers,label='1 coin notification')
            for e in unsent:
                s['delivery'].append({'id':e['id'],'issue':answer['number'],'url':answer['html_url'],'delivered_ms':watch.now()});receipts.add(e['id'])
        s['pending']=[e for e in s['pending'] if e['id'] not in receipts];checkpoint(s)

def worker(minutes,channel):
    if not 1<=minutes<=110:raise ValueError('Bounded1-110min required')
    import github_scan as cloud
    cfg=watch.config()
    if os.environ.setdefault('SCANNER_STATE_BRANCH',cfg['state_branch'])!=cfg['state_branch']:raise ValueError('Separate state required')
    cloud.ROOT=ROOT;cloud.OUT=OUT;cloud.STATE=OUT/'state.json';cloud.fingerprint=watch.fingerprint;cloud.new_state=watch.new_state
    cloud.pull_state();s=json.loads(cloud.STATE.read_text(encoding='utf-8'))
    if s['rules_fingerprint']!=watch.fingerprint():raise ValueError('Unexpected rules fingerprint')
    def checkpoint(s):
        cloud.save(cloud.STATE,s);(OUT/'report.md').write_text(watch.render(s),encoding='utf-8');cloud.push_state()
    deadline=time.monotonic()+minutes*60;session=os.environ.get('GITHUB_RUN_ID','local')
    while time.monotonic()<deadline:
        tick=time.monotonic();start=watch.now();r={'started_ms':start,'session_id':session}
        if s['runs'] and start-s['runs'][-1]['started_ms']>600000:
            watch.event(s,'gap:'+str(start),None,'KAPSAM BOŞLUĞU',f"Son döngü başlangıcından {(start-s['runs'][-1]['started_ms'])/60000:.1f}dk geçti. Bu aralıkta bütün hareketlerin görüldüğü iddia edilmiyor.")
        try:watch.observe(s,cfg)
        except Exception as e:r['error']=str(e);watch.health(s,'cycle',str(e))
        r['finished_ms']=watch.now();s['runs'].append(r);s['runs']=s['runs'][-2016:]
        intervals=sorted((b['started_ms']-a['started_ms'])/60000 for a,b in zip(s['runs'],s['runs'][1:]))
        s['timing']={'intervals':len(intervals),'p95_minutes':intervals[__import__('math').ceil(.95*len(intervals))-1] if intervals else None,'max_minutes':max(intervals) if intervals else None,'over10_minutes':sum(v>10 for v in intervals),'full_chain_coverage':False}
        checkpoint(s)
        if channel=='github_issue':
            try:notify(s,cloud,checkpoint)
            except Exception as e:r['notification_error']=str(e)
        checkpoint(s)
        print(json.dumps({'cycle':r,'pending':len(s['pending']),'delivery_events':len(s['delivery']),'coverage':s['coverage'],'requests':s.get('last_api_requests')},ensure_ascii=True),flush=True)
        pause=min(max(0,cfg['interval_seconds']-(time.monotonic()-tick)),max(0,deadline-time.monotonic()))
        if pause:time.sleep(pause)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--minutes',type=int,default=110);p.add_argument('--channel',choices=['github_issue','report'],default='report');a=p.parse_args();worker(a.minutes,a.channel)
