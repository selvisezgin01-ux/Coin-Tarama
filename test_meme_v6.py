import unittest,json,tempfile
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch
import meme_v6 as v
import meme_base_volume as b
import meme_sources as source
from collections import defaultdict

CFG=v.config();STAMP=21*60000
def address(i):return '0x'+format(i,'040x')
def asset():return {'chain':'ethereum','mint':address(101),'pool':address(202),'symbol':'TEST','pool_created_ms':0,
    'price_usd':1.015,'price_observed_ms':STAMP,'observed_ms':STAMP,'liquidity_usd':20000,'market_cap_usd':100000,'fdv_usd':100000,
    'volume15_usd':5000,'buys15':20,'sells15':2}
def bars():return [[i*300,1,1.02,.99,1,1000] for i in range(3)]+[[900,1,1.02,.99,1.015,2000],[1200,1.015,1.015,1.015,1.015,1]]
def payload():
    rows=[]
    for i in range(8):
        buy=i<6
        rows.append({'id':str(i),'attributes':{'block_timestamp':'1970-01-01T00:'+('16' if i<4 else '17')+':00Z',
            'from_token_address':address(303) if buy else address(101),'to_token_address':address(101) if buy else address(303),
            'tx_from_address':address(1000+i),'volume_in_usd':'250','is_anomalous':False,'kind':'buy' if buy else 'sell'}})
    return {'data':rows}
def setup():return b.evaluate(bars(),asset(),0,STAMP,CFG)['setup']
def security():return {'complete':True,'blocked':False,'unknown':[],'creator':address(999),'creator_pct':1,'excluded_known_accounts':[]}

class PriceBase(unittest.TestCase):
    def test_first_base_then_closed_volume(self):
        a=b.evaluate(bars(),asset(),0,STAMP,CFG)
        self.assertEqual(a['setup']['stage'],'accumulation');self.assertEqual(a['setup']['metrics']['volume_multiple'],2)
        self.assertEqual(a['first_base']['end_ms'],900000);self.assertEqual(a['cutoff_ms'],1200000)
    def test_open_volume_does_not_create_signal(self):
        raw=bars();raw[3][5]=1000;raw[-1][5]=1000000
        self.assertIsNone(b.evaluate(raw,asset(),0,STAMP,CFG)['setup']['stage'])
    def test_three_bars_alone_insufficient(self):self.assertIsNone(b.evaluate(bars()[:3],asset(),0,900000,CFG)['setup']['stage'])
    def test_launch_fragment_excluded_from_base(self):
        a=asset();a['pool_created_ms']=60000
        self.assertIsNone(b.evaluate(bars(),a,60000,STAMP,CFG)['setup']['stage'])
    def test_base_anchor_not_rolled_forward(self):
        first=b.evaluate(bars(),asset(),0,STAMP,CFG)['first_base'];raw=bars()+[[1500,1,1.02,.99,1.015,2000]]
        a=b.evaluate(raw,asset(),0,1800000,CFG,first);self.assertEqual(a['first_base'],first)
    def test_expired_base_not_reset(self):
        anchor=b.evaluate(bars(),asset(),0,STAMP,CFG)['first_base']
        raw=bars()[:4]+[[i*300,1,1.02,.99,1.015,2000] for i in range(4,20)]
        self.assertEqual(b.evaluate(raw,asset(),0,6000000,CFG,anchor)['setup']['reason'],'first_base_expired')
    def test_base_loss(self):
        raw=bars();raw[3][3]=.9
        self.assertEqual(b.evaluate(raw,asset(),0,STAMP,CFG)['setup']['reason'],'first_base_lost')
    def test_gap_is_unknown(self):
        raw=bars();raw.pop(1)
        self.assertIsNone(b.evaluate(raw,asset(),0,STAMP,CFG)['setup']['stage'])
    def test_first_formation_pump_gate_preserved(self):
        raw=bars();raw[0][2]=1.5
        self.assertEqual(b.evaluate(raw,asset(),0,STAMP,CFG)['formation']['status'],'rejected')
    def test_breakout_is_distinct(self):
        raw=bars();raw[3][2]=1.04;raw[3][4]=1.03
        self.assertEqual(b.evaluate(raw,asset(),0,STAMP,CFG)['setup']['stage'],'first_breakout')

class BuyPressure(unittest.TestCase):
    def assess(self,p=None,sec=None):return b.pressure(payload() if p is None else p,asset(),security() if sec is None else sec,setup(),STAMP,CFG)
    def test_buy_dominance_requires_money_and_counts(self):
        x=self.assess();self.assertEqual(x['status'],'passed');self.assertEqual(x['buy_volume_fraction'],.75);self.assertEqual(x['net_buy_usd'],1000)
    def test_sell_dominance_fails(self):
        p=payload()
        for d in p['data']:d['attributes']['from_token_address'],d['attributes']['to_token_address']=d['attributes']['to_token_address'],d['attributes']['from_token_address'];d['attributes']['kind']='sell' if d['attributes']['kind']=='buy' else 'buy'
        self.assertEqual(self.assess(p)['status'],'failed')
    def test_many_small_buys_do_not_override_sell_value(self):
        p=payload()
        for i,r in enumerate(p['data']):r['attributes']['volume_in_usd']='100' if i<6 else '700'
        self.assertIn('buy_volume_not_dominant',self.assess(p)['reasons'])
    def test_single_initiator_dominates(self):
        p=payload()
        for row in p['data'][:6]:row['attributes']['tx_from_address']=address(1001)
        self.assertIn('buy_volume_single_initiator_dominated',self.assess(p)['reasons'])
    def test_unknown_wallet_not_safe(self):
        p=payload();p['data'][0]['attributes'].pop('tx_from_address')
        self.assertEqual(self.assess(p)['status'],'unknown')
    def test_duplicates_do_not_inflate(self):
        p=payload();p['data']+=deepcopy(p['data']);x=self.assess(p)
        self.assertEqual(x['status'],'passed');self.assertEqual(x['net_buy_usd'],1000)
    def test_conflicting_duplicate_unknown(self):
        p=payload();d=deepcopy(p['data'][0]);d['attributes']['volume_in_usd']='500';p['data'].append(d)
        self.assertEqual(self.assess(p)['status'],'unknown')
    def test_token_orientation_conflict_unknown(self):
        p=payload();p['data'][0]['attributes']['to_token_address']=address(555)
        self.assertEqual(self.assess(p)['status'],'unknown')
    def test_open_bar_trades_do_not_confirm_closed_window(self):
        p=payload()
        for row in p['data']:row['attributes']['block_timestamp']='1970-01-01T00:20:30Z'
        self.assertEqual(self.assess(p)['status'],'unknown')
    def test_capped_trade_window_unknown(self):
        p=payload();p['data']=[{**deepcopy(p['data'][i%8]),'id':str(i)} for i in range(300)]
        self.assertIn('trade_window_truncated',self.assess(p)['reasons'])
    def test_volume_mismatch_unknown(self):
        p=payload();p['data']=p['data'][:-1];self.assertNotEqual(self.assess(p)['status'],'unknown')
        p['data']=p['data'][:2];self.assertEqual(self.assess(p)['status'],'unknown')
    def test_creator_outflow_fails(self):
        p=payload();p['data'][-1]['attributes']['tx_from_address']=address(999)
        self.assertIn('creator_selling_in_signal_window',self.assess(p)['reasons'])
    def test_anomalous_trade_not_positive(self):
        p=payload();p['data'][0]['attributes']['is_anomalous']=True
        self.assertEqual(self.assess(p)['status'],'unknown')

class Integration(unittest.TestCase):
    def network(self,cap=100000,sec=None,flow=None,now=STAMP,raw=None):
        st=v.new_state();a=asset();events=[]
        class Client:
            config=CFG
            def gecko(self,path):events.append('flow');return payload() if flow is None else flow
        def fetch(*args):events.append('security');return security() if sec is None else sec
        fresh={'price_usd':1.015,'price_observed_ms':now,'market_cap_usd':cap,'liquidity_usd':20000,'fdv_usd':100000}
        with patch.object(v.pipeline,'discover',return_value=([a],[],{'next_checkpoint_ms':STAMP})),patch.object(v.source,'refresh_pools',return_value=[]),patch.object(v.source,'dex_enrich'),patch.object(v.source,'candles',return_value=bars() if raw is None else raw),patch.object(v.security_api,'fetch_security',side_effect=fetch),patch.object(v.security_api,'fetch_map',return_value={'blocked':False,'complete':False}),patch.object(v.security_api,'developer_check',return_value={'status':'no_outgoing_transfers_in_complete_window'}),patch.object(v.base_volume,'fresh_observation',return_value=fresh),patch.object(v,'now_ms',return_value=now):
            result=v.scan_network('ethereum',CFG['networks']['ethereum'],st,CFG,Client())
        return result,st,events
    def test_security_precedes_flow_and_valid_signal(self):
        r,s,e=self.network();self.assertEqual(e,['security','flow']);self.assertEqual(len(r['qualified']),1)
        self.assertEqual(r['qualified'][0]['buy_pressure']['status'],'passed');self.assertEqual(len(s['paper_v5']['cases']),1)
    def test_missing_security_never_queries_positive_flow(self):
        r,s,e=self.network(sec={'blocked':False,'complete':False,'unknown':['mint_authority']})
        self.assertNotIn('flow',e);self.assertFalse(r['qualified']);self.assertFalse(s['paper_v5']['cases'])
    def test_security_rejection_blocks(self):self.assertFalse(self.network(sec={'blocked':True,'complete':False,'unknown':[]})[0]['qualified'])
    def test_fresh_marketcap_too_high_blocks(self):self.assertFalse(self.network(cap=500001)[0]['qualified'])
    def test_fresh_marketcap_too_low_blocks(self):self.assertFalse(self.network(cap=49999)[0]['qualified'])
    def test_fdv_not_marketcap(self):self.assertFalse(self.network(cap=None)[0]['qualified'])
    def test_marketcap_endpoints_inclusive(self):
        self.assertTrue(self.network(cap=50000)[0]['qualified']);self.assertTrue(self.network(cap=500000)[0]['qualified'])
    def test_unknown_flow_never_qualifies(self):self.assertFalse(self.network(flow={'data':[]})[0]['qualified'])
    def test_first_encounter_already_breaking_out_not_preparation(self):
        raw=bars();raw[3][2]=1.04;raw[3][4]=1.03
        result,_,events=self.network(raw=raw)
        self.assertFalse(result['qualified']);self.assertFalse(events)
    def test_old_archive_keeps_prices_latches_and_no_retro_signals(self):
        old={'version':'meme-v5-pipeline','rules_fingerprint':'a067c337285dc7c4c914d4e30c21efe5575eb62de6c189c2adfc3b6df52c2faa',
            'assets':{'k':{'latest':asset(),'first_formation_disqualified':{'reason':'pump'}}},'entries':{'k':{'references':{'qualified':{'price':12,'observed_ms':99}}}},'pending':[{'id':'old'}],
            'provider_backoff_until_ms':STAMP+900000}
        original=deepcopy(old);new=v.seed(old,'scanner-state-meme-v5','sha',STAMP)
        self.assertEqual(old,original);self.assertEqual(new['previous_v5']['entries'],old['entries']);self.assertEqual(new['entries'],{});self.assertEqual(new['pending'],[])
        self.assertEqual(new['assets']['k']['first_formation_disqualified'],{'reason':'pump'});self.assertEqual(new['provider_backoff_until_ms'],old['provider_backoff_until_ms'])
    def test_reserve_keeps_trade_request(self):
        c=b.Client(CFG);c.gecko_remaining=1
        with patch.object(source.Client,'gecko',return_value={}):
            with self.assertRaises(RuntimeError):c.gecko('x/ohlcv/minute')
            c.gecko('x/trades');self.assertEqual(c.gecko_remaining,0)
    def test_fresh_quote_requires_exact_contract_not_symbol(self):
        class C:
            def dex(self,path):return {'pairs':[{'chainId':'ethereum','pairAddress':address(202),'baseToken':{'address':address(888)},'priceUsd':'1','marketCap':100000}]}
        with self.assertRaises(ValueError):b.fresh_observation(C(),CFG['networks']['ethereum'],asset())
    def test_actual_notification_contains_buy_pressure_cap_and_copy_contract(self):
        result,state,_=self.network();row=result['qualified'][0]
        state['pending']=[{'id':'example','created_ms':STAMP,'candidates':[row]}];posted=[]
        def http(url,payload=None,*args,**kwargs):
            if payload:posted.append(payload);return {'number':1}
            return []
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(v,'STATE',path),patch.object(v.cloud,'http_json',side_effect=http),patch.dict('os.environ',{'GITHUB_REPOSITORY':'test/repo','GH_TOKEN':'test-only'}):v.send_candidate_notifications()
        body=posted[0]['body'];self.assertIn('MCAP $100000',body);self.assertIn('2.00x',body);self.assertIn('alım $1500',body)
        self.assertIn('```text\n'+asset()['mint']+'\n```',body)
    def test_report_missing_fresh_marketcap_is_unknown_not_fdv_or_old_cap(self):
        result,state,_=self.network(cap=None)
        class C:stats=defaultdict(int)
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(v,'OUT',Path(folder)):
                v.render_core(state,{'ethereum':result},C(),CFG);v.render_extra(state)
                text=(Path(folder)/'report.md').read_text(encoding='utf-8')
            self.assertIn('MCAP bilinmiyor',text);self.assertNotIn('15–20 dk',text)

if __name__=='__main__':unittest.main()
