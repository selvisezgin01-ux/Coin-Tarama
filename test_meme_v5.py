import unittest,json,tempfile
from pathlib import Path
from copy import deepcopy
from unittest.mock import patch
import meme_v5 as v
import meme_pipeline as p
import meme_paper_v5 as paper
import meme_sources as source
from test_meme_hybrid import bar
CFG=v.config();STAMP=16*60000
def asset(age=16):return {'chain':'ethereum','mint':'0x'+'1'*40,'pool':'0x'+'2'*40,'symbol':'TEST','pool_created_ms':STAMP-age*60000,
    'price_usd':1.02,'price_observed_ms':STAMP,'observed_ms':STAMP,'liquidity_usd':20000,'market_cap_usd':200000,'fdv_usd':200000,
    'volume15_usd':0,'buys15':0,'sells15':0}
def record(age=16):
    a=asset(age);return {'latest':a,'earliest_pool_created_ms':a['pool_created_ms'],'first_seen_ms':1,'observations':[],
        'market':{'passed':False,'failed':['volume15','transaction_flow15'],'unknown':[]}}
class Pipeline(unittest.TestCase):
    def test_actual_rate_limit_is_marked_for_next_cycle(self):
        c=p.BudgetClient(CFG)
        with patch.object(source.Client,'gecko',side_effect=RuntimeError('api.geckoterminal.com: HTTP 429')):
            with self.assertRaises(RuntimeError):c.gecko('a')
        self.assertTrue(c.rate_limited)
    def test_shared_request_budget_stops_before_network(self):
        cfg=deepcopy(CFG);cfg['pipeline']['global_gecko_requests_per_cycle']=2;c=p.BudgetClient(cfg)
        with patch.object(source.Client,'gecko',return_value={}) as net:
            c.gecko('a');c.gecko('b')
            with self.assertRaises(RuntimeError):c.gecko('c')
            self.assertEqual(net.call_count,2)
    def test_before_age_only_observation(self):self.assertFalse(p.inspectable(record(10),CFG,STAMP))
    def test_market_gate_not_required_for_candle_read(self):self.assertTrue(p.inspectable(record(),CFG,STAMP))
    def test_missing_liquidity_not_inspected(self):
        r=record();r['latest']['liquidity_usd']=None;self.assertFalse(p.inspectable(r,CFG,STAMP))
    def test_known_security_risk_not_inspected(self):
        r=record();r['security']={'blocked':True};self.assertFalse(p.inspectable(r,CFG,STAMP))
    def test_pump_latch_never_revisited_as_fresh(self):
        r=record();r['first_formation_disqualified']={'reason':'pump'};self.assertFalse(p.inspectable(r,CFG,STAMP))
    def test_just_eligible_young_pool_beats_old_liquid_pool(self):
        a,b=record(16),record(1200);b['latest']['liquidity_usd']=1e7
        self.assertLess(p.priority(a,STAMP,CFG),p.priority(b,STAMP,CFG))
    def test_approaching_age_kept_ahead_of_old_pool(self):self.assertLess(p.priority(record(10),STAMP,CFG),p.priority(record(1200),STAMP,CFG))
    def test_refresh_budget(self):
        rows=[]
        for i in range(45):r=record();r['latest']['pool']='0x'+format(i,'040x');r['latest']['observed_ms']=STAMP-180000;rows.append(r)
        self.assertEqual(len(p.refresh_targets(rows,{'entries':{}},'ethereum',STAMP,CFG)),30)
    def test_missing_vs_failed_fields(self):
        r=record();r['market']['unknown']=['valuation'];f=p.funnel([r],STAMP,CFG)
        self.assertEqual(f['market_failed']['volume15'],1);self.assertEqual(f['market_unknown']['valuation'],1)
    def test_discovery_pages_until_coverage(self):
        class Client:
            config=CFG
            def __init__(self):self.calls=0
            def gecko(self,path):
                self.calls+=1;return {'data':[{'attributes':{'pool_created_at':'1970-01-01T00:01:00Z'}}]}
        c=Client()
        with patch.object(source,'normalize_pool',return_value=asset()):rows,err,cov=p.discover(c,'ethereum',CFG['networks']['ethereum'],{'discovery_checkpoints':{'ethereum':600000}},STAMP)
        self.assertTrue(cov['covered_to_previous_checkpoint']);self.assertEqual(c.calls,1)
    def test_uncovered_gap_keeps_previous_checkpoint(self):
        class Client:
            config=CFG
            def gecko(self,path):return {'data':[{'attributes':{'pool_created_at':'1970-01-01T00:15:00Z'}}]}
        with patch.object(source,'normalize_pool',return_value=asset()):_,_,cov=p.discover(Client(),'ethereum',CFG['networks']['ethereum'],{'discovery_checkpoints':{'ethereum':400000}},STAMP)
        self.assertTrue(cov['gap_or_initial_window_uncovered']);self.assertEqual(cov['next_checkpoint_ms'],400000)
    def test_no_false_five_minute_claim(self):
        a=p.cadence([{'ms':1000},{'ms':3601000}],3601000)
        self.assertFalse(a['meets_7m_target']);self.assertFalse(a['full_24h_observed'])
    def test_five_minute_cycles_measured(self):self.assertTrue(p.cadence([{'ms':1},{'ms':300001}],300001)['meets_7m_target'])
class MigrationAndSignals(unittest.TestCase):
    def test_seed_preserves_old_refs_and_pump_latch(self):
        old={'version':'meme-v4-hybrid','rules_fingerprint':v.V4_FP,'assets':{'ethereum:a':{**record(),'first_formation_disqualified':{'reason':'pump'}}},'entries':{'x':{'price':17.3}},'pending':[]}
        before=deepcopy(old);s=v.seed(old,'scanner-state-meme-v4','commit',STAMP)
        self.assertEqual(old,before);self.assertEqual(s['previous_v4']['entries'],old['entries']);self.assertEqual(s['entries'],{})
        self.assertEqual(s['assets']['ethereum:a']['first_formation_disqualified'],{'reason':'pump'})
    def test_wrong_archive_refused(self):
        with self.assertRaises(ValueError):v.seed({},'scanner-state','commit',STAMP)
    def test_market_rejected_can_read_candles_but_cannot_notify(self):
        st=v.new_state();a=asset();cfg=deepcopy(CFG)
        class Client:config=cfg
        with patch.object(v.pipeline,'discover',return_value=([a],[],{'next_checkpoint_ms':STAMP})),patch.object(v.source,'refresh_pools',return_value=[]),patch.object(v.source,'dex_enrich'),patch.object(v.source,'candles',return_value=[bar(0,3000),bar(1,2000),bar(2,1000),bar(3)]),patch.object(v.security_api,'fetch_security') as sec,patch.object(v,'now_ms',return_value=STAMP):
            result=v.scan_network('ethereum',cfg['networks']['ethereum'],st,cfg,Client())
        self.assertEqual(result['funnel']['ohlcv_read'],1);self.assertEqual(result['qualified'],[]);self.assertEqual(st['assets'][v.key_of(a)]['tier'],'watch');sec.assert_not_called()
    def test_first_pump_is_still_excluded(self):
        st=v.new_state();a=asset()
        class Client:config=CFG
        with patch.object(v.pipeline,'discover',return_value=([a],[],{'next_checkpoint_ms':STAMP})),patch.object(v.source,'refresh_pools',return_value=[]),patch.object(v.source,'dex_enrich'),patch.object(v.source,'candles',return_value=[bar(0,high=1.5),bar(1),bar(2),bar(3)]),patch.object(v.security_api,'fetch_security') as sec,patch.object(v,'now_ms',return_value=STAMP):
            result=v.scan_network('ethereum',CFG['networks']['ethereum'],st,CFG,Client())
        self.assertFalse(result['qualified']);self.assertTrue(st['assets'][v.key_of(a)].get('first_formation_disqualified'));sec.assert_not_called()
    def test_pending_does_not_count_as_delivered_accumulation(self):
        st=v.new_state();st['entries']['k']={'alerted_stages':['accumulation']}
        self.assertFalse(v.previously_alerted_accumulation(st,'k'))
        st['delivery_receipts']=[{'key':'k','stage':'accumulation'}];self.assertTrue(v.previously_alerted_accumulation(st,'k'))
    def test_no_qualified_no_pending(self):
        st=v.new_state();v.enqueue_v5(st,{'eth':{'qualified':[]}},CFG);self.assertEqual(st['pending'],[])
class Paper(unittest.TestCase):
    def case(self):
        st=v.new_state();paper.register(st,record(),'early_5m',STAMP);return next(iter(st['paper_v5']['cases'].values()))
    def test_quantity_frozen_at_initial_price(self):
        c=self.case();client=object();a=asset()
        route={'status':'indicative_route','output_usd':100.,'observed_ms':STAMP,'gas_usd':None}
        with patch.object(paper.routes,'read_decimals',return_value=6),patch.object(paper.routes,'parse_route',return_value=route),patch.object(paper.routes,'decimal_units',wraps=paper.routes.decimal_units),patch.object(paper,'urlencode',return_value='x'):
            class C:
                def request(self,*a,**k):return {}
            q=paper.quote_fixed(C(),CFG['networks']['ethereum'],a,{},c,100,STAMP);amount=q['input_raw'];a['price_usd']=10
            q2=paper.quote_fixed(C(),CFG['networks']['ethereum'],a,{},c,100,STAMP)
        self.assertEqual(q2['input_raw'],amount);self.assertIsNone(q2['net_realized_pnl_usd'])
    def test_late_endpoint_unknown_not_zero(self):
        c=self.case();paper.update(c,asset(),STAMP+18*60000,CFG,[])
        self.assertIsNone(c['outcomes']['10']['provider_return_pct']);self.assertEqual(c['outcomes']['10']['status'],'missed_window')
    def test_usdc_not_assumed_one_dollar(self):
        c=self.case();c['sizes']['100']={'status':'open','latest':{'observed_ms':STAMP,'output_units':'200','output_usd':None}}
        paper.update(c,asset(),STAMP,CFG,[]);self.assertEqual(c['sizes']['100']['status'],'open')
    def test_observed_exit_not_realized_profit(self):
        c=self.case();c['sizes']['100']={'status':'open','latest':{'observed_ms':STAMP,'indicative_gross_return_pct':30}}
        paper.update(c,asset(),STAMP,CFG,[]);self.assertEqual(c['sizes']['100']['exit_reason'],'observed_sell_quote_target');self.assertIsNone(c['sizes']['100']['net_realized_pnl_usd'])
    def test_no_future_or_intrabar_fill_claim(self):
        c=self.case();paper.update(c,asset(),STAMP+10*60000,CFG,[])
        self.assertIsNone(c['outcomes']['10']['full_path_mae_mfe']);self.assertEqual(c['max_observed_return_pct'],0)
    def test_reference_not_repriced(self):
        st=v.new_state();r=record();paper.register(st,r,'early_5m',STAMP);r['latest']['price_usd']=2;paper.register(st,r,'early_5m',STAMP)
        self.assertEqual(next(iter(st['paper_v5']['cases'].values()))['provider_entry_price'],1.02)
    def test_path_gaps_are_unknown(self):
        c=self.case();c['observed_ms']=0
        result=paper.path_metrics(c,[bar(0),bar(2)],900000)
        self.assertIsNone(result['mae_pct']);self.assertFalse(result['full_trade_path'])
    def test_entry_fragment_excluded_from_path(self):
        c=self.case();c['observed_ms']=60000
        result=paper.path_metrics(c,[bar(0,high=99),bar(1),bar(2)],900000)
        self.assertEqual(result['entry_fragment_omitted_ms'],240000);self.assertLess(result['mfe_pct'],5)
class NotificationIntegrity(unittest.TestCase):
    def test_token_contract_copy_block_in_actual_issue_payload(self):
        st,_,batch=self.fixture();row=batch['candidates'][0];row['developer']={'status':'unknown'}
        posted=[]
        def http(url,payload=None,*args,**kwargs):
            if payload:posted.append(payload);return {'number':1}
            return []
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'state.json';path.write_text(json.dumps(st),encoding='utf-8')
            with patch.object(v,'STATE',path),patch.dict('os.environ',{'GITHUB_REPOSITORY':'test/repo','GH_TOKEN':'mock'}),patch.object(v.cloud,'http_json',side_effect=http):v.send_candidate_notifications()
        body=posted[0]['body']
        self.assertIn('```text\n'+row['mint']+'\n```',body)
        self.assertIn('Ağ: '+CFG['networks']['ethereum']['name'],body)
        self.assertNotIn('```text\n'+row['pool']+'\n```',body)
        self.assertIn('Resmî/orijinal kontrat eşleşmesi ayrıca doğrulanmalıdır',body)
    def test_malformed_contract_refused(self):
        row=asset();row['mint']='bad-address\n```'
        with self.assertRaises(ValueError):v.contract_block(row)
    def fixture(self):
        st=v.new_state();a=asset();key=v.key_of(a);st['assets'][key]={'latest':a,'tier':'qualified'};st['entries'][key]={'references':{}}
        row={**a,'signal_phase':'early_5m','stage':'accumulation'};batch={'id':'testevent','created_ms':STAMP,'candidates':[row]};st['pending']=[batch]
        return st,key,batch
    def perform(self,state,existing,send):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(v,'STATE',path),patch.object(v,'now_ms',return_value=STAMP),patch.dict('os.environ',{'GITHUB_REPOSITORY':'test/repo','GH_TOKEN':'mock'}),patch.object(v.cloud,'http_json',return_value=existing),patch.object(v,'BASE_NOTIFY',side_effect=send):
                try:v.notify()
                except RuntimeError:pass
            return json.loads(path.read_text(encoding='utf-8'))
    def test_stale_candidate_not_sent(self):
        st,_,_=self.fixture();st['pending'][0]['candidates'][0]['observed_ms']=STAMP-11*60000
        def forbidden():raise AssertionError('Stale message must not be sent')
        out=self.perform(st,[],forbidden);self.assertFalse(out['pending']);self.assertFalse(out['delivery_receipts'])
    def test_accepted_post_is_reconciled_before_retry(self):
        st,key,_=self.fixture();existing=[{'body':'<!-- coin-tarama-meme:testevent -->','user':{'login':'github-actions[bot]'}}]
        def forbidden():raise AssertionError('Already accepted message must not repeat')
        out=self.perform(st,existing,forbidden);self.assertFalse(out['pending']);self.assertTrue(v.previously_alerted_accumulation(out,key))
    def test_failed_post_keeps_pending_no_delivered_mark(self):
        st,_,_=self.fixture()
        def failure():raise RuntimeError('mock POST unavailable')
        out=self.perform(st,[],failure);self.assertEqual(len(out['pending']),1);self.assertFalse(out['delivery_receipts'])
    def test_risk_change_blocks_positive_alert(self):
        st,key,_=self.fixture();st['followup_watch']={'tokens':{key:{'flags':{'security_deterioration':True}}}}
        def forbidden():raise AssertionError('Known risk must block message')
        out=self.perform(st,[],forbidden);self.assertFalse(out['pending'])

if __name__=='__main__':unittest.main()
