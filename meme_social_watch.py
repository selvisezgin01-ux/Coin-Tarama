"""Additive metadata observations; never claims X rename history or changes trade gates."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import urlsplit

import meme_scan as meme
from meme_sources import Client,valid_address

SECTION='## X bağlantıları ve topluluk devri — ek gözlem'
LIMIT_PER_NETWORK=20
LEGACY_FINGERPRINT='5dc9665062f18d0f3f623620c84cfc5481fb85d30ceb062d89420ff4e9eed303'


def fingerprint():
    return hashlib.sha256(Path(__file__).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode()).hexdigest()


def social_state(state):
    value=state.setdefault('social_watch',{'version':1,'fingerprint':fingerprint(),'tokens':{},'pending':[]})
    if value.get('fingerprint')!=fingerprint():
        if value.get('version')==1 and value.get('fingerprint')==LEGACY_FINGERPRINT:
            value['migration']={'from_fingerprint':value['fingerprint'],'observed_ms':meme.now_ms(),
                                'reason':'Presentation only: hide raw discovery records; preserve all X/CTO baselines and events.'}
            value['version']=2;value['fingerprint']=fingerprint()
        else:raise ValueError('Social observation rules changed; explicit migration required')
    return value


def canonical_x(url):
    if not isinstance(url,str):return None
    try:
        parsed=urlsplit(url)
        if parsed.scheme not in ('http','https') or parsed.hostname not in ('x.com','www.x.com','twitter.com','www.twitter.com'):return None
        if parsed.username or parsed.password or parsed.port not in (None,80,443):return None
    except ValueError:return None
    parts=parsed.path.strip('/').split('/')
    if len(parts)==3 and parts[:2]==['i','communities'] and parts[2].isdigit():
        return 'https://x.com/i/communities/'+parts[2]
    reserved={'i','intent','search','home','explore','settings','share','messages','notifications','compose','login','signup'}
    if not parts or not re.fullmatch(r'[A-Za-z0-9_]{1,15}',parts[0]) or parts[0].lower() in reserved:return None
    if len(parts)>1 and not (len(parts)>=3 and parts[1]=='status' and parts[2].isdigit()):return None
    return 'https://x.com/'+parts[0].lower()


def x_links(pair):
    """None = no usable provider observation; [] = explicit social list with no X link."""
    info=pair.get('info')
    if not isinstance(info,dict) or not isinstance(info.get('socials'),list):return None
    result=[]
    for row in info['socials']:
        if not isinstance(row,dict):return None
        value=canonical_x(row.get('url'))
        if value:result.append(value)
        elif str(row.get('type','')).lower() in ('twitter','x'):return None
    return sorted(set(result))


def update_links(watch,asset,links,stamp,previously_alerted=False):
    key=meme.key_of(asset);record=watch['tokens'].setdefault(key,{'chain':asset['chain'],'mint':asset['mint'],
                'symbol':meme.safe_symbol(asset['symbol']),'observed_link_changes':0,'events':[],
                'historical_username_change_count':None,'x_account_identity_verified':False})
    if links is None:
        record['last_attempt_ms']=stamp;record['latest_observation_status']='unavailable';return
    if 'current_links' not in record:
        record.update({'first_links':links,'current_links':links,'first_observed_ms':stamp,'last_observed_ms':stamp,
                       'source_pool':asset['pool'],'latest_observation_status':'provider_observed'})
        return
    if stamp<=record['last_observed_ms']:return
    if record['current_links']!=links:
        event={'kind':'x_link_change','chain':asset['chain'],'mint':asset['mint'],'symbol':record['symbol'],
               'before':record['current_links'],'after':links,'observed_ms':stamp,'previous_observed_ms':record['last_observed_ms'],
               'source_pool_before':record.get('source_pool'),'source_pool_after':asset['pool']}
        event['id']=hashlib.sha256(json.dumps(event,sort_keys=True).encode()).hexdigest()[:24]
        record['observed_link_changes']+=1;record['events']=(record['events']+[event])[-100:]
        if previously_alerted:watch['pending'].append(event)
    record.update({'current_links':links,'last_observed_ms':stamp,'source_pool':asset['pool'],'latest_observation_status':'provider_observed'})


def update_cto(watch,asset,claim,stamp,previously_alerted=False):
    # A DexScreener community claim is not proof the developer sold or ownership changed on-chain.
    record=watch['tokens'][meme.key_of(asset)]
    if claim is None:return
    date=claim.get('claimDate')
    if not isinstance(date,str) or len(date)>64:return
    try:
        parsed=datetime.fromisoformat(date.replace('Z','+00:00'))
        if parsed.tzinfo is None or not 0<parsed.timestamp()*1000<=stamp+60000:return
        date=str(int(parsed.timestamp()*1000))
    except (ValueError,OverflowError):return
    identity=hashlib.sha256((meme.key_of(asset)+'|'+date).encode()).hexdigest()[:24]
    if identity in record.setdefault('cto_seen_ids',[]):return
    record['cto_seen_ids'].append(identity)
    event={'kind':'community_claim','id':identity,'chain':asset['chain'],'mint':asset['mint'],
           'symbol':record['symbol'],'observed_ms':stamp,'provider_claim_date_ms':int(date)}
    record['cto']={**event,'status':'dexscreener_reported_claim_not_developer_sale_proof'}
    if previously_alerted:watch['pending'].append(event)


def text_for(record):
    if not record:return 'X bağlantısı: veri yok. Geçmiş kullanıcı adı değişikliği sayısı: bilinmiyor.'
    current=record.get('current_links')
    links='; '.join(current) if current else ('Sağlayıcı listesinde X bağlantısı yok' if current==[] else 'Veri yok')
    text='X: '+links+'\nTakipte gözlenen bağlantı değişikliği: '+str(record['observed_link_changes'])
    if record.get('latest_observation_status')=='unavailable':text+='; son yenileme doğrulanamadı'
    text+='\nGeçmiş kullanıcı adı değişikliği sayısı: bilinmiyor. Bağlantı değişimi, aynı X hesabının ad değiştirdiği veya el değiştirdiği kanıtı değildir.'
    if record.get('cto'):text+='\nDİKKAT: DexScreener topluluk devri/CTO kaydı var; geliştiricinin sattığı veya fiyatın düşeceği kanıtlanmış sayılmaz.'
    return text


def previously_notified(state,key):
    waiting={r['stage'] for batch in state['pending'] for r in batch['candidates'] if meme.key_of(r)==key}
    return bool(set(state['entries'].get(key,{}).get('alerted_stages',[]))-waiting)


def annotate(state,config,client):
    watch=social_state(state);stamp=meme.now_ms();errors=[];selected=[];observed=0
    for chain,network in config['networks'].items():
        rows=[r['latest'] for r in state['assets'].values() if r['latest']['chain']==chain]
        rows.sort(key=lambda a:(0 if meme.key_of(a) in state['entries'] else 1,
                               watch['tokens'].get(meme.key_of(a),{}).get('last_attempt_ms',0),-(a.get('liquidity_usd') or 0)))
        rows=rows[:LIMIT_PER_NETWORK];selected+=rows
        if not rows:continue
        try:
            pairs=client.dex('tokens/v1/'+network['dex']+'/'+','.join(a['mint'] for a in rows))
            if not isinstance(pairs,list):raise ValueError('Unexpected social metadata response')
            for asset in rows:
                key=meme.key_of(asset)
                matching=[p for p in pairs if p.get('chainId')==network['dex']
                          and meme.rules.address_key(chain,(p.get('baseToken') or {}).get('address',''))==asset['mint']
                          and meme.rules.address_key(chain,p.get('pairAddress',''))==asset['pool']]
                links=x_links(matching[0]) if len(matching)==1 else None
                update_links(watch,asset,links,meme.now_ms(),previously_notified(state,key))
                watch['tokens'][key]['last_attempt_ms']=stamp
                observed+=links is not None
        except Exception as exc:
            errors.append(network['name']+': '+str(exc))
            for asset in rows:update_links(watch,asset,None,stamp)
    try:
        claims=client.dex('community-takeovers/latest/v1')
        if not isinstance(claims,list):raise ValueError('Unexpected community-claim response')
        by_key={}
        for claim in claims:
            for chain,network in config['networks'].items():
                mint=claim.get('tokenAddress')
                if claim.get('chainId')==network['dex'] and valid_address(chain,mint):
                    by_key[chain+':'+meme.rules.address_key(chain,mint)]=claim
        for asset in selected:
            key=meme.key_of(asset)
            update_cto(watch,asset,by_key.get(key),meme.now_ms(),previously_notified(state,key))
    except Exception as exc:errors.append('CTO: '+str(exc))
    protected=set(state['assets'])|set(state['entries'])|{meme.key_of(e) for e in watch['pending']}
    others=sorted([(k,r) for k,r in watch['tokens'].items() if k not in protected and stamp-r.get('last_attempt_ms',0)<=48*3600000],
                  key=lambda item:-item[1].get('last_attempt_ms',0))[:3000]
    watch['tokens']={**dict(others),**{k:r for k,r in watch['tokens'].items() if k in protected}}
    # Retain previous sightings rather than deleting unavailable metadata or rewriting history.
    watch['last_run']={'observed_ms':meme.now_ms(),'requested_tokens':len(selected),'usable_x_observations':observed,
                       'errors':errors,'cto_absence_is_not_no_takeover_proof':True}
    return watch


def append_report(state):
    watch=state['social_watch'];path=meme.OUT/'report.md'
    prefix=path.read_text(encoding='utf-8').split('\n'+SECTION,1)[0] if path.exists() else '# Coin Tarama Meme\n'
    lines=['',SECTION,'','Kaynak: DexScreener token metadata ve sınırlı son topluluk devri akışı. Geçmiş tüm X isim değişiklikleri, aynı hesabın kimliği ve hesabın sahibinin değişmesi doğrulanmaz. İlk gözlemden önceki geçmiş bilinmiyor; sayaç yalnız takip sırasında görülen bağlantı değişimlerini sayar. CTO kaydı satış veya dump kanıtı değildir.','',
           '| Token / ağ | İlk X gözlemi TR | İlk bağlantı | Güncel bağlantı | Gözlenen değişiklik | CTO kaydı |',
           '|---|---|---|---|---:|---|']
    records=sorted([r for k,r in watch['tokens'].items() if k in state['entries']],key=lambda r:(-bool(r.get('cto') or r['observed_link_changes']),-r.get('last_observed_ms',0)))
    if not records:lines+=['','Henüz aday yok; ham sosyal gözlem tokenleri aday olarak gösterilmez.','']
    for record in records[:40]:
        def links(value):return '<br>'.join(value) if value else ('Listede yok' if value==[] else 'Bilinmiyor')
        date=meme.time_label(record['first_observed_ms']) if record.get('first_observed_ms') else '—'
        lines.append(f"| {record['symbol']} / {record['chain']} `{record['mint']}` | {date} | {links(record.get('first_links'))} | {links(record.get('current_links'))} | {record['observed_link_changes']} | {'Sağlayıcı kaydı var' if record.get('cto') else 'Gözlenmedi; yokluğu kanıtlanmadı'} |")
    lines+=['','Her döngüde ağ başına en çok 20 tokenin metadatası okunur; bütün tokenler aynı anda kapsanmaz. X bağlantıları yalnız metin olarak doğrulanır; hesap varlığı veya resmî proje hesabı olduğu onaylanmaz. Daha önce bildirilen adayda sonradan bağlantı değişimi/CTO kaydı gözlenirse ayrı uyarı Issue’su oluşur.','']
    lines+=['- '+err for err in watch['last_run']['errors']]
    path.write_text(prefix.rstrip()+'\n'+'\n'.join(lines),encoding='utf-8')
    summary=meme.OUT/'summary.json'
    if summary.exists():
        data=json.loads(summary.read_text(encoding='utf-8'));data['social_watch']=watch['last_run'];meme.cloud.save(summary,data)


def notify():
    state=json.loads(meme.STATE.read_text(encoding='utf-8'));watch=social_state(state)
    notes={batch['id']:'\n\nSosyal hesap gözlemleri:\n\n'+'\n\n'.join(meme.safe_symbol(row['symbol'])+'\n'+text_for(watch['tokens'].get(meme.key_of(row))) for row in batch['candidates']) for batch in state['pending']}
    original=meme.cloud.http_json
    def enriched(url,payload=None,headers=None,label='Notification'):
        if isinstance(payload,dict) and isinstance(payload.get('body'),str):
            match=re.search(r'<!-- coin-tarama-meme:([a-z0-9]+) -->',payload['body'])
            if match and match[1] in notes:payload={**payload,'body':payload['body']+notes[match[1]]}
        return original(url,payload,headers,label)
    meme.cloud.http_json=enriched
    try:meme.notify()
    finally:meme.cloud.http_json=original
    state=json.loads(meme.STATE.read_text(encoding='utf-8'));watch=social_state(state)
    if not watch['pending']:return
    repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN');user=os.environ.get('COIN_NOTIFY_USER','').strip()
    if not repo or not token:raise RuntimeError('Social-warning notification configuration missing')
    if user and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',user):raise ValueError('Invalid notification recipient')
    url='https://api.github.com/repos/'+repo+'/issues';headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'}
    existing=original(url+'?state=all&per_page=100',headers=headers,label='GitHub Issues')
    for event in list(watch['pending']):
        marker='<!-- meme-social-watch:'+event['id']+' -->'
        label='X bağlantısı değişti' if event['kind']=='x_link_change' else 'Topluluk devri kaydı'
        if not any(marker in (r.get('body') or '') for r in existing):
            body=('@'+user+'\n\n' if user else '')+label+' — '+event['symbol']+' / '+event['chain']+'\nKontrat: `'+event['mint']+'`\nGözlem: '+meme.time_label(event['observed_ms'])+' TR\n\n'
            if event['kind']=='x_link_change':body+='Önce: '+('; '.join(event['before']) or 'Listede yok')+'\nSonra: '+('; '.join(event['after']) or 'Listede yok')+'\n\n'
            body+=text_for(watch['tokens'].get(meme.key_of(event)))+'\n\nEk inceleme uyarısıdır; kesin satış/dump veya hesap sahipliği değişimi iddiası değildir.\n\n'+marker
            original(url,{'title':'Coin Tarama Meme · '+label+' · '+event['symbol'],'body':body},headers,label='GitHub Issues')
        watch['pending']=[e for e in watch['pending'] if e['id']!=event['id']];meme.cloud.save(meme.STATE,state)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['observe','notify']);args=parser.parse_args();meme.configure()
    if args.phase=='notify':notify()
    else:
        state=json.loads(meme.STATE.read_text(encoding='utf-8'));config=json.loads((meme.ROOT/'meme_config.json').read_text(encoding='utf-8'))
        if state['rules_fingerprint']!=meme.fingerprint():raise ValueError('Core scanner rules do not match stored observations')
        annotate(state,config,Client(config));meme.cloud.save(meme.STATE,state);append_report(state)
        print(json.dumps(state['social_watch']['last_run']))
