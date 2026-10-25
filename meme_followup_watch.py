"""Bounded post-alert observations and indicative read-only exit routes. Never sends trades."""
from __future__ import annotations
import argparse
from decimal import Decimal,ROUND_DOWN
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import urlencode

import meme_scan as meme
import meme_social_watch as social
from meme_sources import Client,valid_address,ms_iso

SECTION='## Bildirim sonrası ek ölçümler'
SIZES=(100,500)
MAX_TARGETS=2
WINDOW_MS=24*3600000
NATIVE='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
USDC_SOL='EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
KYBER_CHAINS={'ethereum':'ethereum','bnb':'bsc','robinhood':'robinhood','hyperevm':'hyperevm'}
WARNING_LABELS={'liquidity_withdrawal':'likidite kaybı','developer_outflow':'geliştirici cüzdanından çıkış',
                'security_deterioration':'kontrat risk işareti','sample_selling_pressure':'örnekte satış baskısı'}


def fingerprint():
    return hashlib.sha256(Path(__file__).read_text(encoding='utf-8-sig').replace('\r\n','\n').encode()).hexdigest()


def followup_state(state):
    value=state.setdefault('followup_watch',{'version':1,'fingerprint':fingerprint(),'tokens':{},'pending':[]})
    if value['fingerprint']!=fingerprint():raise ValueError('Follow-up rules changed; explicit migration required')
    return value


def trade_sample(payload,asset,stamp):
    rows=payload.get('data')
    if not isinstance(rows,list):raise ValueError('Unexpected trades response')
    unique={};invalid=0
    for row in rows:
        a=row.get('attributes') or {};identity=row.get('id');date=ms_iso(a.get('block_timestamp'))
        if not identity or date is None or date>stamp+60000:invalid+=1;continue
        if identity in unique and unique[identity]!=a:raise ValueError('Conflicting trade ID')
        unique[identity]=a
    result={'source':'GeckoTerminal last at most 300 trades / 24h','observed_ms':stamp,'returned':len(rows),
            'row_limit_reached':len(rows)>=300,'invalid_rows':invalid,'scope':'observed transaction initiators, not independent people',
            'status':'provider_limited_sample' if rows else 'unknown','windows':{}}
    dates=[ms_iso(a.get('block_timestamp')) for a in unique.values()]
    earliest=min(dates) if dates else None
    result['earliest_trade_ms']=earliest
    for minutes in (15,30):
        buys={};sells={};buy_count=sell_count=0;buy_usd=sell_usd=0.;unknown_volume=0;missing_wallet=0
        for a in unique.values():
            date=ms_iso(a.get('block_timestamp'))
            if not stamp-minutes*60000<=date<=stamp:continue
            if a.get('is_anomalous') is True:invalid+=1;continue
            start=meme.rules.address_key(asset['chain'],str(a.get('from_token_address','')))
            end=meme.rules.address_key(asset['chain'],str(a.get('to_token_address','')))
            if (start==asset['mint'])==(end==asset['mint']):continue
            buying=end==asset['mint'];volume=meme.rules.number(a.get('volume_in_usd'))
            if volume is None or volume<0:unknown_volume+=1
            elif buying:buy_usd+=volume
            else:sell_usd+=volume
            if buying:buy_count+=1
            else:sell_count+=1
            wallet=a.get('tx_from_address')
            if not valid_address(asset['chain'],wallet):missing_wallet+=1;continue
            wallet=meme.rules.address_key(asset['chain'],wallet)
            target=buys if buying else sells
            target[wallet]=target.get(wallet,0.)+(volume if volume is not None and volume>=0 else 0.)
        valid_volume=unknown_volume==0 and buy_count+sell_count>0
        result['windows'][str(minutes)]={'observed_buy_trades':buy_count,'observed_sell_trades':sell_count,
            'unique_observed_buyers':len(buys),'unique_observed_sellers':len(sells),'both_sides_initiators':len(set(buys)&set(sells)),
            'buy_volume_usd':buy_usd if valid_volume else None,'sell_volume_usd':sell_usd if valid_volume else None,
            'net_buy_volume_usd':buy_usd-sell_usd if valid_volume else None,
            'top_buyer_volume_fraction':max(buys.values())/buy_usd if valid_volume and buy_usd>0 and not missing_wallet else None,
            'missing_wallet_rows':missing_wallet,'unknown_volume_rows':unknown_volume,
            'returned_span_reaches_window_start':bool(earliest is not None and earliest<=stamp-minutes*60000),
            'complete_onchain_coverage':False}
    return result


def holder_observation(record,security,stamp):
    count=meme.rules.number(security.get('holder_count'));provider=security.get('source')
    if count is None or count<0 or count!=int(count):return {'status':'unknown','count':None,'observed_ms':stamp}
    history=record.setdefault('holder_history',[])
    observation={'count':int(count),'source':provider,'observed_ms':stamp,'provider_cache_age_known':False}
    comparisons={}
    for minutes in (15,30):
        choices=[x for x in history if x['source']==provider and minutes*60000<=stamp-x['observed_ms']<=(minutes+10)*60000]
        if choices:
            prior=max(choices,key=lambda x:x['observed_ms'])
            comparisons[str(minutes)]={'change':int(count)-prior['count'],'elapsed_minutes':(stamp-prior['observed_ms'])/60000,
                'prior_observed_ms':prior['observed_ms']}
    history.append(observation);record['holder_history']=[x for x in history if stamp-x['observed_ms']<=2*3600000][-60:]
    return {**observation,'status':'provider_reported','comparisons':comparisons}


def decimal_units(dollars,price,decimals):
    if not isinstance(decimals,int) or isinstance(decimals,bool) or not 0<=decimals<=36:raise ValueError('Token decimals unknown')
    p=Decimal(str(price))
    if not p.is_finite() or p<=0:raise ValueError('Reference price invalid')
    value=int((Decimal(str(dollars))/p*10**decimals).to_integral_value(rounding=ROUND_DOWN))
    if value<=0:raise ValueError('Quote amount rounds to zero')
    return str(value)


def read_decimals(client,network,asset,security):
    if asset['chain']=='solana':
        decimals=security.get('token_decimals')
        if isinstance(decimals,int) and not isinstance(decimals,bool) and 0<=decimals<=36:return decimals
        # Public mint metadata, not a wallet/account read or transaction construction.
        url=os.environ.get('MEME_RPC_SOLANA') or 'https://api.mainnet-beta.solana.com'
        data=client.request(url,{'jsonrpc':'2.0','id':1,'method':'getTokenSupply','params':[asset['mint'],{'commitment':'confirmed'}]})
        decimals=((data.get('result') or {}).get('value') or {}).get('decimals')
    else:
        url=os.environ.get('MEME_RPC_'+asset['chain'].upper()) or network['rpc']
        if int(client.rpc(url,'eth_chainId',[]),16)!=int(network['chain_id']):raise ValueError('Wrong metadata RPC chain')
        data=client.request(url,{'jsonrpc':'2.0','id':1,'method':'eth_call',
             'params':[{'to':asset['mint'],'data':'0x313ce567'},'latest']})
        raw=data.get('result')
        if not isinstance(raw,str) or not re.fullmatch(r'0x[0-9a-fA-F]{64}',raw):raise ValueError('Invalid token decimals response')
        decimals=int(raw,16)
    if not isinstance(decimals,int) or isinstance(decimals,bool) or not 0<=decimals<=36:raise ValueError('Token decimals unknown')
    return decimals


def parse_route(data,asset,amount,stamp):
    if asset['chain']=='solana':
        route=data.get('data') or {}
        if data.get('success') is not True or route.get('swapType')!='BaseIn':raise ValueError('No indicative Raydium route')
        if route.get('inputMint')!=asset['mint'] or route.get('outputMint')!=USDC_SOL or str(route.get('inputAmount'))!=amount:
            raise ValueError('Quote does not match requested token/amount')
        raw=route.get('outputAmount')
        if not isinstance(raw,str) or not raw.isdigit() or int(raw)<=0:raise ValueError('No output quote')
        if not route.get('routePlan'):raise ValueError('Missing route')
        return {'status':'indicative_route','provider':'Raydium','observed_ms':stamp,'output_token':'USDC',
                'output_units':str(Decimal(raw)/10**6),'output_usd':None,'gas_usd':None,
                'provider_price_impact_pct_raw':meme.rules.number(route.get('priceImpactPct')),
                'price_impact_unit_verified':False,'tax_inclusion_verified':False}
    route=(data.get('data') or {}).get('routeSummary') or {}
    if data.get('code')!=0 or not route.get('route'):raise ValueError('No indicative KyberSwap route')
    if str(route.get('tokenIn','')).lower()!=asset['mint'].lower() or str(route.get('tokenOut','')).lower()!=NATIVE or str(route.get('amountIn'))!=amount:
        raise ValueError('Quote does not match requested token/amount')
    provider_stamp=meme.rules.number(route.get('timestamp'))
    if provider_stamp is None or not -60000<=stamp-provider_stamp*1000<=120000:raise ValueError('Quote timestamp stale or missing')
    raw=route.get('amountOut')
    if not isinstance(raw,str) or not raw.isdigit() or int(raw)<=0:raise ValueError('No output quote')
    usd=meme.rules.number(route.get('amountOutUsd'));gas=meme.rules.number(route.get('gasUsd'))
    return {'status':'indicative_route','provider':'KyberSwap','observed_ms':stamp,'provider_ms':provider_stamp*1000,
            'output_token':{'ethereum':'ETH','bnb':'BNB','robinhood':'ETH','hyperevm':'HYPE'}[asset['chain']],
            'output_units':str(Decimal(raw)/10**18),'output_usd':usd if usd is not None and usd>0 else None,
            'gas_usd':gas if gas is not None and gas>0 else None,'l1_fee_usd':meme.rules.number(route.get('l1FeeUsd')),
            'tax_inclusion_verified':False}


def exit_quotes(client,network,asset,security):
    result=[]
    try:decimals=read_decimals(client,network,asset,security)
    except Exception as exc:return [{'reference_usd':size,'status':'unknown','reason':str(exc)} for size in SIZES]
    for size in SIZES:
        try:
            amount=decimal_units(size,asset['price_usd'],decimals)
            if asset['chain']=='solana':
                query=urlencode({'inputMint':asset['mint'],'outputMint':USDC_SOL,'amount':amount,'slippageBps':50,'txVersion':'V0'})
                data=client.request('https://transaction-v1.raydium.io/compute/swap-base-in?'+query)
            else:
                chain=KYBER_CHAINS[asset['chain']]
                query=urlencode({'tokenIn':asset['mint'],'tokenOut':NATIVE,'amountIn':amount,'excludeRFQSources':'true','gasInclude':'true'})
                data=client.request('https://aggregator-api.kyberswap.com/'+chain+'/api/v1/routes?'+query,headers={'X-Client-Id':'CoinTaramaMeme'})
            item=parse_route(data,asset,amount,meme.now_ms())
            item.update({'reference_usd':size,'input_raw':amount,'token_decimals':decimals,'reference_price_usd':asset['price_usd'],
                         'reference_observed_ms':asset['price_observed_ms'],'buy_tax_fraction':security.get('buy_tax_fraction'),
                         'sell_tax_fraction':security.get('sell_tax_fraction')})
            if item.get('output_usd') is not None:item['difference_from_reference_pct']=(item['output_usd']/size-1)*100
            result.append(item)
        except Exception as exc:result.append({'reference_usd':size,'status':'unknown','reason':str(exc)})
    return result


def risk_event(watch,record,kind,value,stamp,notified,detail):
    if value is None:return # Unknown never clears a previous warning or creates a recovery claim.
    flags=record.setdefault('flags',{});old=flags.get(kind)
    flags[kind]=value
    if not value or old is True:return
    episode=record.setdefault('episodes',{});episode[kind]=episode.get(kind,0)+1
    event={'kind':kind,'chain':record['chain'],'mint':record['mint'],'symbol':record['symbol'],
           'observed_ms':stamp,'detail':detail}
    event['id']=hashlib.sha256((meme.key_of(record)+'|'+kind+'|'+str(episode[kind])).encode()).hexdigest()[:24]
    record.setdefault('events',[]).append(event)
    if notified:watch['pending'].append(event)


def annotate(state,config,client):
    watch=followup_state(state);stamp=meme.now_ms();targets=[];errors=[]
    for key,entry in state['entries'].items():
        reference=entry.get('references',{}).get('qualified')
        if not reference or not 0<=stamp-reference['observed_ms']<=WINDOW_MS:continue
        base=state['assets'].get(key,{});asset=base.get('latest')
        if not asset:continue
        record=watch['tokens'].setdefault(key,{'chain':entry['chain'],'mint':entry['mint'],'symbol':entry['symbol'],
            'pool':entry['first_pool'],'started_ms':reference['observed_ms'],'creator':base.get('security',{}).get('creator')})
        targets.append((record.get('last_attempt_ms',0),key,record,asset))
    targets.sort(key=lambda x:(x[0],x[1]))
    for _,key,record,oldasset in targets[:MAX_TARGETS]:
        record['last_attempt_ms']=meme.now_ms();chain=record['chain'];network=config['networks'][chain];notified=social.previously_notified(state,key)
        asset={**oldasset,'pool':record['pool']};latest={'observed_ms':meme.now_ms(),'errors':[]}
        try:
            rows=meme.source.refresh_pools(client,chain,network,[record['pool']])
            exact=[r for r in rows if meme.key_of(r)==key and r['pool']==record['pool']]
            if len(exact)!=1:raise ValueError('Original pool could not be matched; migration not treated as liquidity withdrawal')
            asset=exact[0];latest['market']=asset;stamp=meme.now_ms()
            history=record.setdefault('liquidity_history',[]);liq=meme.rules.number(asset.get('liquidity_usd'))
            previous=[p['liquidity_usd'] for p in history if 0<=stamp-p['observed_ms']<=3600000 and p['liquidity_usd']>0]
            loss=(1-liq/max(previous))*100 if previous and liq is not None else None
            latest['liquidity_loss_from_observed_hour_peak_pct']=loss
            risk_event(watch,record,'liquidity_withdrawal',None if loss is None else loss>20,stamp,notified,
                       'Aynı havuzda gözlenen son saat tepesine göre likidite düşüşü: '+str(loss)+'%.')
            if liq is not None:history.append({'observed_ms':stamp,'liquidity_usd':liq})
            record['liquidity_history']=[p for p in history if stamp-p['observed_ms']<=3600000][-60:]
        except Exception as exc:latest['errors'].append(str(exc));asset=None
        sec={}
        try:
            sec=meme.security_api.fetch_security(client,network,{**oldasset,'pool':record['pool']});latest['security']=sec
            latest['holders']=holder_observation(record,sec,meme.now_ms())
            risk_event(watch,record,'security_deterioration',True if sec.get('blocked') else (False if sec.get('complete') else None),
                       meme.now_ms(),notified,'Yeni güvenlik raporu: '+', '.join(sec.get('risks',[])))
        except Exception as exc:latest['errors'].append(str(exc));latest['holders']={'status':'unknown','count':None}
        creator=record.get('creator')
        if not creator and valid_address(chain,sec.get('creator')):creator=sec['creator'];record['creator']=creator
        try:
            if not valid_address(chain,creator):raise ValueError('Known original creator unavailable')
            if sec.get('creator') and meme.rules.address_key(chain,sec['creator'])!=meme.rules.address_key(chain,creator):
                raise ValueError('Creator identity conflict; original creator not replaced')
            # Recheck the known creator even after its reported balance reaches zero.
            dev=meme.security_api.developer_solana(client,oldasset,creator,meme.now_ms()) if chain=='solana' else meme.security_api.developer_evm(client,network,oldasset,creator,meme.now_ms())
            latest['developer']=dev
            risk_event(watch,record,'developer_outflow',True if dev.get('status')=='outgoing_transfer_detected' else (False if dev.get('status')=='no_outgoing_transfers_in_complete_window' else None),
                       meme.now_ms(),notified,'Raporlanan geliştirici cüzdanından son 45 dakikada çıkış var; satış olduğu kanıtlanmadı.')
        except Exception as exc:latest['developer']={'status':'unknown','reason':str(exc)}
        try:
            query=urlencode({'token':oldasset['mint'],'include_anomalous':'true'})
            payload=client.gecko(f"networks/{network['gecko']}/pools/{record['pool']}/trades?"+query)
            sample=trade_sample(payload,oldasset,meme.now_ms());latest['participation']=sample;win=sample['windows']['15']
            b=win['buy_volume_usd'];s=win['sell_volume_usd']
            pressure=None if b is None or s is None or b+s<=0 or not win['returned_span_reaches_window_start'] else (win['observed_sell_trades']>=12 and s/(b+s)>=.75)
            risk_event(watch,record,'sample_selling_pressure',pressure,meme.now_ms(),notified,
                       'Sınırlı işlem örneğinde 15dk satış hacmi payı en az %75 ve en az 12 satış; tam zincir kapsamı değil.')
        except Exception as exc:latest['participation']={'status':'unknown','reason':str(exc)}
        latest['exit_quotes']=exit_quotes(client,network,asset,sec) if asset else [{'reference_usd':s,'status':'unknown','reason':'Original pool reference unavailable'} for s in SIZES]
        latest['active_warnings']=[k for k,v in record.get('flags',{}).items() if v]
        record['latest']=latest;errors.extend([record['symbol']+': '+e for e in latest['errors']])
    watch['last_run']={'observed_ms':meme.now_ms(),'active_targets':len(targets),'checked':min(MAX_TARGETS,len(targets)),
                       'errors':errors,'max_targets_per_run':MAX_TARGETS,'monitor_hours':24}
    return watch


def text_for(record):
    if not record or not record.get('latest'):return 'Ek ölçümler henüz tamamlanmadı; eksik veri temiz sonuç sayılmaz.'
    latest=record['latest'];lines=[]
    if latest.get('active_warnings'):lines.append('DİKKAT (son bilinen durum): '+', '.join(WARNING_LABELS.get(k,k) for k in latest['active_warnings']))
    h=latest.get('holders',{});lines.append('Holder: '+str(h.get('count') if h.get('count') is not None else 'bilinmiyor')+'; değişim: '+json.dumps(h.get('comparisons',{}),ensure_ascii=False))
    participation=latest.get('participation',{})
    if not participation.get('windows'):lines.append('Katılım örneği: bilinmiyor.')
    for minutes,win in participation.get('windows',{}).items():
        top=win.get('top_buyer_volume_fraction');top_text='bilinmiyor' if top is None else f'%{top*100:.1f}'
        net=win['net_buy_volume_usd'];net_text='bilinmiyor' if net is None else f'{net:.2f}'
        lines.append(minutes+'dk gözlenen alıcı/satıcı işlem başlatıcısı: '+str(win['unique_observed_buyers'])+'/'+str(win['unique_observed_sellers'])+
            '; net alım USD: '+net_text+'; en büyük alıcı hacim payı: '+top_text+' (sınırlı örnek, kişi sayısı değil).')
    for quote in latest.get('exit_quotes',[]):
        label='$'+str(quote['reference_usd'])+' referanslı satış: '
        if quote['status']!='indicative_route':lines.append(label+'bilinmiyor — '+quote.get('reason','veri yok'));continue
        text=label+quote['output_units']+' '+quote['output_token']
        if quote.get('output_usd') is not None:text+=f" (~${quote['output_usd']:.2f})"
        if quote.get('difference_from_reference_pct') is not None:text+=f"; referansa fark %{quote['difference_from_reference_pct']:.2f} (saf fiyat etkisi değil)"
        text+='; gaz USD: '+str(quote.get('gas_usd') if quote.get('gas_usd') is not None else 'bilinmiyor')
        tax=quote.get('sell_tax_fraction');text+='; sağlayıcı satış vergisi: '+('bilinmiyor' if tax is None else f'%{tax*100:.2f}')
        text+='; gözlem '+meme.time_label(quote['observed_ms'])+' TR'
        lines.append(text)
    lines.append('Kotasyon gözlem anına aittir, hızla eskir; gerçekleşme/honeypot veya bütün vergilerin dahil olduğu teyidi değildir. USDC otomatik $1 sayılmaz. Likidite, işlem hacmi ve holder verisi organik talebi kanıtlamaz.')
    if latest.get('errors'):lines.append('Eksikler: '+'; '.join(latest['errors']))
    return '\n'.join(lines)


def append_report(state):
    watch=state['followup_watch'];path=meme.OUT/'report.md'
    prefix=path.read_text(encoding='utf-8').split('\n'+SECTION,1)[0]
    lines=['',SECTION,'','Yalnız ön elemeden geçen tokenler; ilk bildirimden sonra 24 saat, döngü başına en çok 2 token sırayla kontrol edilir. Her token her döngüde kontrol edilmiş sayılmaz. Ek ölçümler seçim eşiklerini veya geçmiş referans fiyatını değiştirmez.','']
    if not watch['tokens']:lines+=['Henüz ön eleme adayı yok; ek ölçüm listesi boş.','']
    for record in watch['tokens'].values():
        lines+=['### '+record['symbol']+' / '+record['chain']+' `'+record['mint']+'`','',text_for(record).replace('\n','  \n'),'']
    lines+=['Alıcı sayısı, net alım ve yoğunlaşma son en çok 300 işlemin 15/30dk örneğinden hesaplanır; tam pencere veya bağımsız kişi sayısı değildir. Ayrıntı state.json içindedir. Holder değişimi yalnız aynı sağlayıcının iki gerçek gözlemi arasında ölçülür; önbellek yaşı bilinmez. Developer takibi yalnız bilinen oluşturucu ve sınırlı 45dk pencereyi kapsar; boşluklar kalabilir.','',
            'Satış rotaları yalnız GET fiyat sorgusudur; işlem oluşturulmaz, imzalanmaz ve gönderilmez. Rota bulunamaması tek başına satış engeli değildir. Kendi havuzumuz dışındaki rotalar da kullanılabilir. Raydium fiyat etkisinin birimi ayrıca doğrulanmadığından yüzdelik iddia yapılmaz; ham sağlayıcı alanı kaydedilir. Gaz ve verginin eksik olduğu yerde net kazanç hesaplanmaz.','']
    path.write_text(prefix.rstrip()+'\n'+'\n'.join(lines),encoding='utf-8')
    summary=meme.OUT/'summary.json'
    if summary.exists():
        data=json.loads(summary.read_text(encoding='utf-8'));data['followup_watch']=watch['last_run'];meme.cloud.save(summary,data)


def notify():
    state=json.loads(meme.STATE.read_text(encoding='utf-8'));watch=followup_state(state)
    notes={b['id']:'\n\nEk ölçümler:\n\n'+'\n\n'.join(r['symbol']+'\n'+text_for(watch['tokens'].get(meme.key_of(r))) for r in b['candidates']) for b in state['pending']}
    original=meme.cloud.http_json
    def enriched(url,payload=None,headers=None,label='Notification'):
        if isinstance(payload,dict) and isinstance(payload.get('body'),str):
            match=re.search(r'<!-- coin-tarama-meme:([a-z0-9]+) -->',payload['body'])
            if match and match[1] in notes:payload={**payload,'body':payload['body']+notes[match[1]]}
        return original(url,payload,headers,label)
    meme.cloud.http_json=enriched
    try:social.notify()
    finally:meme.cloud.http_json=original
    state=json.loads(meme.STATE.read_text(encoding='utf-8'));watch=followup_state(state)
    if not watch['pending']:return
    repo=os.environ.get('GITHUB_REPOSITORY');token=os.environ.get('GH_TOKEN');user=os.environ.get('COIN_NOTIFY_USER','').strip()
    if not repo or not token:raise RuntimeError('Follow-up issue notification configuration missing')
    if user and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',user):raise ValueError('Invalid recipient')
    url='https://api.github.com/repos/'+repo+'/issues';headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'}
    existing=original(url+'?state=all&per_page=100',headers=headers,label='GitHub Issues')
    for event in list(watch['pending']):
        marker='<!-- meme-followup:'+event['id']+' -->'
        if not any(marker in (row.get('body') or '') for row in existing):
            body=('@'+user+'\n\n' if user else '')+event['detail']+'\nKontrat: `'+event['mint']+'` / '+event['chain']+'\nGözlem: '+meme.time_label(event['observed_ms'])+' TR\n\n'+text_for(watch['tokens'].get(meme.key_of(event)))+'\n\n'+marker
            original(url,{'title':'Coin Tarama Meme · Risk değişimi · '+event['symbol'],'body':body},headers,label='GitHub Issues')
        watch['pending']=[e for e in watch['pending'] if e['id']!=event['id']];meme.cloud.save(meme.STATE,state)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['observe','notify']);args=parser.parse_args();meme.configure()
    if args.phase=='notify':notify()
    else:
        state=json.loads(meme.STATE.read_text(encoding='utf-8'));config=json.loads((meme.ROOT/'meme_config.json').read_text(encoding='utf-8'))
        if state['rules_fingerprint']!=meme.fingerprint():raise ValueError('Core scanner rules do not match stored state')
        annotate(state,config,Client(config));meme.cloud.save(meme.STATE,state);append_report(state)
        print(json.dumps(state['followup_watch']['last_run']))
