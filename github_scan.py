"""Independent GitHub live watch, sharing the existing MEXC/OKX scan rules.

No 50-coin pilot limit, retrospective entries or local heartbeat dependency.
State is checkpointed in a separate Git branch; notifications are optional.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.error import HTTPError,URLError
from urllib.request import Request,urlopen

import momentum_scan
import okx_scan
from research import LOCAL
from study_dataset import read_json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'cloud_output'
STATE=OUT/'state.json'


def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
    temporary.replace(path)


def fingerprint():
    digest=hashlib.sha256()
    for name in ['momentum_config.json','study_config.json','momentum_scan.py','okx_scan.py','study_dataset.py','parabolic_sar.py']:
        # Hash canonical text so Git CRLF/LF checkout does not change the rules.
        digest.update(name.encode());digest.update((ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode())
    return digest.hexdigest()


def new_state():
    return {'version':1,'rules_fingerprint':fingerprint(),'venues':{},'pending':[]}


def collect(exchange,replay=False):
    adapter=momentum_scan if exchange=='MEXC' else okx_scan
    if replay:
        directory=adapter.selected_directory(None)
    else:
        directory=adapter.snapshot()
        adapter.download(directory);adapter.evaluate(directory);adapter.quotes(directory)
    selection=read_json(directory/'selection.json')
    result_root=ROOT/'results'/('momentum_v3' if exchange=='MEXC' else 'okx_momentum_v3')/selection['run_id']
    candidates=read_json(result_root/'candidates.json')
    book=read_json(directory/'book_tickers_raw.json')
    quotes={x['symbol']:x for x in book['data']}
    rows=[]
    for c in candidates:
        raw=quotes.get(c['symbol'],{})
        try:
            bid,ask=float(raw['bidPrice']),float(raw['askPrice'])
            if not 0<bid<=ask:raise ValueError('Invalid quote')
            mid=(bid+ask)/2;spread=(ask-bid)/mid*100
        except (KeyError,ValueError,TypeError):mid=None;spread=None
        rows.append({'exchange':exchange,'symbol':c['symbol'],'observed_ms':book['fetched_server_time_ms'],
             'feature_cutoff_ms':selection['closed_decision_ms'],'mid_price':mid,'spread_pct':spread,
             'return24_pct':c['return24_pct'],'relative24_pct_points':c['relative24_pct_points'],
             'quote_volume24':c['quote_volume24'],'liquidity_band':c['liquidity_band'],
             'breakout_level':c['breakout_level'],'breakout_open_ms':c['breakout_open_ms'],
             'breakout_volume_ratio':c['breakout_volume_ratio'],'strength_score':c['strength_score'],
             'breakout_age_bars':c['breakout_age_bars'],'invalidation_level':c['invalidation_level']})
    return {'exchange':exchange,'observed_ms':book['fetched_server_time_ms'],
            'feature_cutoff_ms':selection['closed_decision_ms'],
            'universe_count':selection['crypto_usdt_universe'],'prefilter_count':selection['prefilter_passed'],
            'analyzed_count':read_json(result_root/'summary.json')['analyzed_symbols'],
            'candidates':rows}


def update_state(state,scans,now_ms):
    fresh=[]
    for exchange,result in scans.items():
        if 'error' in result:continue # A failed exchange is not an empty candidate list.
        old=state['venues'].get(exchange,{'active':[],'last_alert':{},'ever_seen':[]})
        previous=set(old['active']);ever=set(old['ever_seen']);last=old['last_alert']
        for row in result['candidates']:
            symbol=row['symbol']
            if symbol not in previous and (symbol not in last or now_ms-last[symbol]>=48*3600000):
                fresh.append({**row,'arrival':'reentry' if symbol in ever else 'new'})
                last[symbol]=now_ms
            ever.add(symbol)
        state['venues'][exchange]={'active':[r['symbol'] for r in result['candidates']],
            'last_alert':last,'ever_seen':sorted(ever),'latest':result}
    if fresh:
        batch_id=hashlib.sha256(json.dumps([now_ms,[(r['exchange'],r['symbol'],r['breakout_open_ms']) for r in fresh]],sort_keys=True).encode()).hexdigest()[:24]
        state['pending'].append({'id':batch_id,'created_ms':now_ms,'candidates':fresh})
    state['updated_ms']=now_ms
    return fresh


def time_label(ms):return datetime.fromtimestamp(ms/1000,LOCAL).strftime('%d.%m.%Y %H:%M')


def row_text(row):
    price='doğrulanamadı' if row['mid_price'] is None else f"{row['mid_price']:.8g}"
    spread='—' if row['spread_pct'] is None else f"%{row['spread_pct']:.2f}"
    flags=[]
    if row['liquidity_band']=='thin':flags.append('düşük hacim')
    if row['spread_pct'] is None or row['spread_pct']>.5:flags.append('makas teyidi gerekli')
    if row['mid_price'] is not None and row['mid_price']<row['breakout_level']:flags.append('güncel fiyat kırılan seviyenin altında')
    if row['breakout_age_bars']==0:flags.append('ilk kırılım kapanışı; sonraki mum teyidi yok')
    return f"{row['symbol']} · {row['exchange']}\nFiyat {price} | 24s %{row['return24_pct']:.2f} | hacim {row['breakout_volume_ratio']:.2f}x | makas {spread}\n"+('; '.join(flags) if flags else 'Kapalı mum tarama koşulları sağlandı')


def report(scans,fresh,replay):
    lines=['# MEXC + OKX — GitHub taraması','',
           'Bağımsız canlı izleme; yerel 50 coinlik araştırma pilotundan ayrıdır. Yalnız ön elemeden geçen spot/USDT pariteleri incelenir. Puan başarı olasılığı değildir.', '']
    if replay:lines+=['**Çevrimdışı deneme: arşiv verisi kullanıldı; bu güncel canlı tarama değildir.**','']
    for exchange,result in scans.items():
        if 'error' in result:lines += [f"{exchange}: **HATA — {result['error']}**. Önceki aktif liste korunur.",''];continue
        lines += [f"{exchange}: evren {result['universe_count']}, ön eleme {result['prefilter_count']}, incelenen {result['analyzed_count']}, aday {len(result['candidates'])}. Gözlem {time_label(result['observed_ms'])} TR; mum kesimi {time_label(result['feature_cutoff_ms'])} TR.",'']
    lines+=['## Bu döngüde yeni gelenler','']
    if not fresh:lines+=['Yeni aday yok.','']
    for row in fresh:lines += [row_text(row).replace('\n','  \n'),'']
    lines+=['## Güncel aday listesi','','| Coin | Borsa | 24s % | Hacim USDT | Hacim katı | Makas % |', '|---|---|---:|---:|---:|---:|']
    for result in scans.values():
        for row in result.get('candidates',[]):
            spread='—' if row['spread_pct'] is None else f"{row['spread_pct']:.3f}"
            lines.append(f"| {row['symbol']} | {row['exchange']} | {row['return24_pct']:.2f} | {row['quote_volume24']:.0f} | {row['breakout_volume_ratio']:.2f} | {spread} |")
    lines+=['','Her borsa kendi fiyatı ve hacmiyle değerlendirilir. Aynı coin iki borsada görünürse borsa etiketi korunur. Bildirimler önceki başarılı taramaya göre yeni girişlerde oluşur; tekrar girişler için 48 saat bildirim beklemesi vardır. Sürekli listede kalan coin her dört saatte tekrar bildirilmez. Bu döngüdeki yokluk yalnız başarılı bir taramadan sonra değerlendirilir.','']
    OUT.mkdir(parents=True,exist_ok=True)
    text='\n'.join(lines)
    (OUT/'report.md').write_text(text,encoding='utf-8')
    summary=os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary,'a',encoding='utf-8') as stream:stream.write(text)


def scan(replay=False):
    state=read_json(STATE) if STATE.exists() else new_state()
    if state['rules_fingerprint']!=fingerprint():raise RuntimeError('Rules changed. Start an explicitly versioned state branch before continuing.')
    scans={}
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs={pool.submit(collect,e,replay):e for e in ['MEXC','OKX']}
        for job in as_completed(jobs):
            try:scans[jobs[job]]=job.result()
            except Exception as exc:scans[jobs[job]]={'error':str(exc)}
    now=int(datetime.now(timezone.utc).timestamp()*1000)
    fresh=update_state(state,scans,now)
    save(STATE,state);save(OUT/'scan.json',{'scans':scans,'new_candidates':fresh,'replay':replay})
    report(scans,fresh,replay)
    print(f'New exchange candidates: {len(fresh)}; failed exchanges: {sum("error" in v for v in scans.values())}')


def git(*args,input=None,allowed=(0,)):
    # Git tree records need literal LF on Windows too; text stdin would add CR.
    result=subprocess.run(['git',*args],cwd=ROOT,input=None if input is None else input.encode('utf-8'),capture_output=True)
    result=subprocess.CompletedProcess(result.args,result.returncode,
                                       result.stdout.decode('utf-8'),result.stderr.decode('utf-8',errors='replace'))
    if result.returncode not in allowed:raise RuntimeError(f'Git state operation failed ({args[0]}). Check branch permissions and Actions logs.')
    return result


def state_branch():
    branch=os.environ.get('SCANNER_STATE_BRANCH','scanner-state')
    git('check-ref-format','--branch',branch)
    return branch


def pull_state():
    branch=state_branch()
    found=git('ls-remote','--exit-code','--heads','origin',f'refs/heads/{branch}',allowed=(0,2))
    OUT.mkdir(parents=True,exist_ok=True)
    if found.returncode==2:
        save(STATE,new_state());(OUT/'parent.txt').write_text('',encoding='ascii')
        return
    git('fetch','--no-tags','origin',f'refs/heads/{branch}')
    parent=git('rev-parse','FETCH_HEAD').stdout.strip()
    contents=git('show',f'{parent}:state.json').stdout
    parsed=json.loads(contents) # Corrupt/missing state must fail, not silently reset deduplication.
    if parsed['rules_fingerprint']!=fingerprint():raise RuntimeError('Stored state uses different rules; choose a new state branch.')
    save(STATE,parsed);(OUT/'parent.txt').write_text(parent,encoding='ascii')


def push_state():
    branch=state_branch()
    if not (OUT/'parent.txt').exists():raise RuntimeError('Pull state before pushing it.')
    git('config','user.name','github-actions[bot]')
    git('config','user.email','41898282+github-actions[bot]@users.noreply.github.com')
    records=[]
    for path,name in [(STATE,'state.json'),(OUT/'report.md','report.md')]:
        if path.exists():records.append(f"100644 blob {git('hash-object','-w',str(path)).stdout.strip()}\t{name}\n")
    tree=git('mktree',input=''.join(records)).stdout.strip()
    parent=(OUT/'parent.txt').read_text(encoding='ascii').strip()
    args=['commit-tree',tree]+(['-p',parent] if parent else [])
    commit=git(*args,input=f"Scanner checkpoint {os.environ.get('GITHUB_RUN_ID','manual')}\n").stdout.strip()
    git('push','origin',f'{commit}:refs/heads/{branch}')
    (OUT/'parent.txt').write_text(commit,encoding='ascii')


def http_json(url,payload=None,headers=None,label='Notification'):
    data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
    request=Request(url,data=data,headers={'Content-Type':'application/json',**(headers or {})})
    try:
        with urlopen(request,timeout=25) as response:return json.load(response)
    except HTTPError as exc:raise RuntimeError(f'{label} HTTP {exc.code}; check configured permissions/recipient.') from None
    except (URLError,OSError):raise RuntimeError(f'{label} connection failed; credentials were not logged.') from None


def notify(channel):
    state=read_json(STATE)
    pending=list(state['pending'])
    for batch in pending:
        body='Yeni tarama adayları · '+time_label(batch['created_ms'])+' TR\n\n'+'\n\n'.join(row_text(r) for r in batch['candidates'])
        body+='\n\nTeknik izleme listesidir; doğrulanmış getiri vaadi içermez.'
        if channel=='telegram':
            token=os.environ.get('TELEGRAM_BOT_TOKEN');chat=os.environ.get('TELEGRAM_CHAT_ID')
            if not token or not chat:raise RuntimeError('Telegram secrets are missing. Add them in repository Actions secrets.')
            # Split by line below Telegram's text size; never print the token URL.
            chunks=[];current=''
            for line in body.splitlines(keepends=True):
                if len(current)+len(line)>3500:chunks.append(current);current=''
                current+=line
            if current:chunks.append(current)
            for chunk in chunks:
                answer=http_json(f'https://api.telegram.org/bot{token}/sendMessage',{'chat_id':chat,'text':chunk},label='Telegram')
                if not answer.get('ok'):raise RuntimeError('Telegram rejected the message.')
        elif channel=='github_issue':
            repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN')
            if not repo or not token:raise RuntimeError('GitHub repository/token is missing.')
            recipient=os.environ.get('GITHUB_NOTIFY_USER','').strip()
            if recipient and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',recipient):
                raise ValueError('GITHUB_NOTIFY_USER must be a GitHub username without @.')
            if recipient:body=f'@{recipient}\n\n'+body
            headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json'}
            url=f'https://api.github.com/repos/{repo}/issues'
            marker=f"<!-- coin-scanner:{batch['id']} -->"
            existing=http_json(url+'?state=all&per_page=100',headers=headers,label='GitHub Issues')
            if not any(marker in (issue.get('body') or '') for issue in existing):
                http_json(url,{'title':f"Yeni coin adayları · {time_label(batch['created_ms'])}",
                              'body':body+'\n\n'+marker},headers,label='GitHub Issues')
        elif channel!='report':raise ValueError('Unknown notification channel')
        state['pending']=[x for x in state['pending'] if x['id']!=batch['id']]
        save(STATE,state)
    print(f'Processed notification batches: {len(pending)}; channel: {channel}')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('phase',choices=['scan','pull-state','push-state','notify','check-status'])
    parser.add_argument('--replay',action='store_true')
    parser.add_argument('--channel',choices=['report','telegram','github_issue'],default='report')
    args=parser.parse_args()
    if args.phase=='scan':scan(args.replay)
    elif args.phase=='pull-state':pull_state()
    elif args.phase=='push-state':push_state()
    elif args.phase=='notify':notify(args.channel)
    else:
        result=read_json(OUT/'scan.json')
        raise SystemExit(1 if any('error' in v for v in result['scans'].values()) else 0)
