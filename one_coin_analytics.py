"""Bounded observed accumulation, not bot classification or ownership attribution."""
import math

def threshold(t,cfg,kind='swap'):
    liq=t.get('market',{}).get('liquidity')
    if not isinstance(liq,(int,float)) or not math.isfinite(liq) or liq<=0:return None
    if kind=='holder':return max(cfg['holder_notify_min_usd'],liq*cfg['holder_notify_liquidity_fraction'])
    return max(cfg['minimum_notify_swap_usd'],liq*cfg['minimum_notify_swap_liquidity_fraction'])

def quiet(t,stamp,cfg):
    out=[];last=t.get('last_trade_check_ms',0);coverage=t.get('flow15_sample',{}).get('coverage',[])
    safe=bool(last and stamp-last<=420000 and coverage and all(not c.get('possibly_truncated') and not c.get('invalid') for c in coverage))
    if not safe:return []
    for minutes in cfg['quiet_windows_minutes']:
        start=stamp-minutes*60000
        prices=[p for p in t.get('history',[]) if start-300000<=p['observed_ms']<=stamp and p['pool']==t['market']['pool']]
        if len(prices)<3 or prices[0]['observed_ms']>start+300000:continue
        if any(b['observed_ms']-a['observed_ms']>450000 for a,b in zip(prices,prices[1:])):continue
        band=(max(p['price'] for p in prices)/min(p['price'] for p in prices)-1)*100
        if band>cfg['quiet_price_band_pct']:continue
        rows=[r for r in t.get('seen_trades',{}).values() if start<=r['block_ms']<=stamp]
        buys=[r for r in rows if r['side']=='buy'];buy=sum(r['usd'] for r in buys);sell=sum(r['usd'] for r in rows if r['side']=='sell')
        net=buy-sell;fraction=buy/(buy+sell) if buy+sell else None
        floor=max(cfg['quiet_min_net_usd'],t['market']['liquidity']*cfg['quiet_net_liquidity_fraction'])*(1 if minutes==15 else 1.5)
        if len(buys)<cfg['quiet_min_trades'] or fraction is None or fraction<cfg['quiet_buy_fraction'] or net<floor:continue
        accounts={}
        for r in rows:
            a=accounts.setdefault(r['wallet'],{'buy_usd':0.,'sell_usd':0.,'buys':0})
            a[r['side']+'_usd']+=r['usd'];a['buys']+=r['side']=='buy'
        for a in accounts.values():a['net_usd']=a['buy_usd']-a['sell_usd']
        out.append({'minutes':minutes,'buy_usd':buy,'sell_usd':sell,'net_usd':net,'buy_fraction':fraction,'buy_trades':len(buys),'price_band_pct':band,
                    'initiators':len({r['wallet'] for r in buys}),'accounts':accounts,'source':'observed selected-pool swap sample','complete_chain_coverage':False})
    return out

def should_repeat(previous,current,stamp,cfg):
    if not previous:return True
    return stamp-previous['stamp']>=cfg['quiet_cooldown_minutes']*60000 or current>=previous['net_usd']*(1+cfg['quiet_repeat_growth_fraction'])

def holders(values,candidates,mint,excluded,stamp,slot,previous):
    accounts={};owners={};missing=[]
    for address,v in zip(candidates,values):
        if not isinstance(v,dict):missing.append(address);continue
        info=v.get('data',{}).get('parsed',{}).get('info',{})
        amount=info.get('tokenAmount',{});raw=amount.get('amount');dec=amount.get('decimals');owner=info.get('owner')
        if info.get('mint')!=mint or not isinstance(owner,str) or not isinstance(raw,str) or not raw.isdigit() or not isinstance(dec,int):missing.append(address);continue
        if owner in excluded:continue
        n=int(raw)/10**dec;accounts[address]={'owner':owner,'amount':n}
        o=owners.setdefault(owner,{'amount':0.,'change_tokens':0.,'same_accounts_compared':0});o['amount']+=n
        old=previous.get('accounts',{}).get(address)
        if old and old['owner']==owner:o['change_tokens']+=n-old['amount'];o['same_accounts_compared']+=1
    return {'accounts':accounts,'owners':owners,'missing':missing,'observed_ms':stamp,'slot':slot,'complete_owner_balances':False,
            'coverage':'known token-account cohort; not a live global top20 ranking'}

def groups(edges,owner_changes,mint):
    graph={}
    for e in edges:
        if e.get('mint')!=mint or e.get('evidence')!='explicit_token_transfer':continue
        a,b=e['source_owner'],e['destination_owner']
        graph.setdefault(a,set()).add(b);graph.setdefault(b,set()).add(a)
    seen=set();out=[]
    for root in graph:
        if root in seen:continue
        todo=[root];members=set()
        while todo:
            a=todo.pop()
            if a in members:continue
            members.add(a);todo+=list(graph.get(a,[])-members)
        seen|=members
        sampled=[a for a in members if a in owner_changes]
        if len(sampled)>=2:out.append({'members':sorted(members),'observed_members':sampled,'change_tokens':sum(owner_changes[a]['change_tokens'] for a in sampled),
            'evidence':'direct transfer edges only; shared ownership not verified'})
    return out
