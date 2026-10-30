import unittest,json,tempfile,copy
from pathlib import Path
from unittest.mock import patch
import meme_v7 as v
import meme_v7_model as m
import meme_v7_discovery as d
import meme_v7_collector as c
import meme_v7_routes as r
from meme_v7_feed_publisher import Publisher,BRANCH as FEED_BRANCH
from meme_v7_service import single_instance

CFG=v.config();START=1800000000000;NOW=START+900000
MINT='B'*40;POOL='D'*40
def asset(**changes):
    return {'chain':'solana','mint':MINT,'pool':POOL,'symbol':'FIXTURE_NOT_LIVE','price_usd':102.,'price_observed_ms':NOW,
        'observed_ms':NOW,'pool_created_ms':START,'liquidity_usd':20000.,'market_cap_usd':100000.,
        'volume5_usd':1000.,'buys5':20,'sells5':5,**changes}
def bars():return [[START//1000,100,101,99,100,100],[(START+300000)//1000,100,101,99.5,100.5,100],[(START+600000)//1000,100.5,102.3,100,102,1000]]
def setup():return m.first_base(bars(),asset(),{'eligible_since_ms':START},NOW,CFG)
def sec():return {'complete':True,'blocked':False,'creator':'C'*40}
def dev():return {'status':'no_outgoing_transfers_in_complete_window'}
def maps():return {'blocked':False,'complete':False,'status':'manual'}
def route():return {'status':'passed','roundtrip_loss_pct':1,'entry_input_usd':100,'token_output_raw':'12345'}
def old_state():return {'version':'meme-v6-pipeline','rules_fingerprint':v.OLD_FP,'entries':{'x':{'references':{'qualified':{'price':17,'observed_ms':99}}}},'delivery_receipts':[{'id':'old'}],
    'assets':{'x':{'latest':asset(),'first_seen_ms':START}},'paper_v5':{'cases':{'x':{'price':17}}},'previous_v5':{'entries':{'y':{'price':10}}}}
def pool_payload(created,chain='solana',mint=MINT,pool=POOL):
    date=__import__('datetime').datetime.fromtimestamp(created/1000,__import__('datetime').timezone.utc).isoformat()
    return {'data':[{'attributes':{'address':pool,'pool_created_at':date,'name':'FIXTURE / SOL','base_token_price_usd':'1','reserve_in_usd':'20000'},
        'relationships':{'base_token':{'data':{'id':chain+'_'+mint}},'quote_token':{'data':{'id':chain+'_So11111111111111111111111111111111111111112'}}}}]}

class ModelTests(unittest.TestCase):
    def test_three_closed_bars_form_entry_not_four(self):
        s=setup();self.assertEqual(s['stage'],'first_breakout');self.assertEqual(s['first_base']['end_ms'],START+600000)
    def test_open_signal_bar_is_not_entry(self):self.assertIsNone(m.first_base(bars(),asset(),{'eligible_since_ms':START},NOW-1,CFG)['stage'])
    def test_future_real_eligibility_does_not_backfill(self):self.assertIsNone(m.first_base(bars(),asset(),{'eligible_since_ms':NOW},NOW,CFG)['stage'])
    def test_missing_first_eligible_bar_unknown(self):
        result=m.first_base(bars()[1:],asset(),{'eligible_since_ms':START},NOW,CFG)
        self.assertIsNone(result['stage']);self.assertIn(result['reason'],('first_eligible_interval_history_missing','selected_pool_initial_history_unknown'))
    def test_gap_unknown(self):self.assertIsNone(m.first_base([bars()[0],bars()[2]],asset(),{'eligible_since_ms':START},NOW,CFG)['stage'])
    def test_no_lifetime_25pct_ban(self):
        a=asset(pool_created_ms=START-3600000)
        history=[[(START-3600000+i*300000)//1000,20+i*6.5,21+i*6.5,19+i*6.5,20.5+i*6.5,100] for i in range(12)]
        s=m.first_base(history+bars(),a,{'eligible_since_ms':START,'previous_launch_gain_pct':500},NOW,CFG)
        self.assertIsNotNone(s['stage'])
    def test_known_earlier_dump_cannot_be_reset_by_later_quiet_base(self):
        a=asset(pool_created_ms=START-600000)
        old=[[(START-600000)//1000,150,200,140,180,100],[(START-300000)//1000,180,181,90,100,100]]
        out=m.first_base(old+bars(),a,{'eligible_since_ms':START},NOW,CFG)
        self.assertTrue(out['latch_dump']);self.assertEqual(out['reason'],'severe_dump_in_available_pool_history')
    def test_missing_launch_history_not_certified_clean(self):
        self.assertEqual(m.first_base(bars(),asset(pool_created_ms=START-300000),{'eligible_since_ms':START},NOW,CFG)['reason'],'selected_pool_initial_history_unknown')
    def test_dump_latches(self):
        raw=bars();raw[0][2]=200;self.assertTrue(m.first_base(raw,asset(),{'eligible_since_ms':START},NOW,CFG)['latch_dump'])
    def test_base_never_switches_pool(self):
        s=setup();a=asset(pool='E'*40);self.assertEqual(m.first_base(bars(),a,{'eligible_since_ms':START,'first_base':s['first_base']},NOW,CFG)['reason'],'first_base_pool_changed')
    def test_no_fdv_substitution(self):self.assertFalse(m.market(asset(market_cap_usd=None,fdv_usd=100000),CFG,NOW)['passed'])
    def test_quote_stale_and_future(self):
        for stamp in (NOW-121000,NOW+1):self.assertFalse(m.market(asset(price_observed_ms=stamp),CFG,NOW)['passed'])
    def test_activity_never_claims_buy_volume(self):self.assertFalse(m.activity(asset(),CFG)['buy_volume_verified'])
    def test_full_criteria_pass(self):self.assertTrue(m.entry_guard(asset(),setup(),{'status':'passed'},sec(),dev(),maps(),route(),CFG,NOW)['passed'])
    def test_unknown_is_never_green(self):
        defaults=[asset(),setup(),{'status':'passed'},sec(),dev(),maps(),route(),CFG,NOW]
        for index,value in ((2,{'status':'unknown'}),(3,{'blocked':False,'complete':False,'unknown':['authority']}),(4,{'status':'unknown'}),(6,{'status':'unknown'})):
            args=copy.deepcopy(defaults);args[index]=value;self.assertFalse(m.entry_guard(*args)['passed'])
    def test_known_risk_is_never_green(self):
        for a,b in (({'blocked':True,'complete':True},dev()),(sec(),{'status':'outgoing_transfer_detected'})):
            self.assertFalse(m.entry_guard(asset(),setup(),{'status':'passed'},a,b,maps(),route(),CFG,NOW)['passed'])
    def test_entry_stop_and_projected_target(self):
        g=m.entry_guard(asset(),setup(),{'status':'passed'},sec(),dev(),maps(),route(),CFG,NOW)
        self.assertAlmostEqual(g['stop_reference'],97.02);self.assertGreater(g['target_projection'],asset()['price_usd']);self.assertFalse(g['actual_execution_or_net_profit_verified'])
    def test_one_event_per_contract_phase_and_pool(self):
        s=v.new_state();e=m.event(s,asset(),'early_radar',NOW,{});self.assertIsNone(m.event(s,asset(pool='E'*40),'early_radar',NOW+1,{}));self.assertEqual(len(s['events']),1)
    def test_no_historical_15m_strengthening(self):
        self.assertFalse(m.strengthened(bars(),{'observed_ms':NOW,'base':setup()['first_base']},NOW))

class DiscoveryTests(unittest.TestCase):
    def test_young_identities_not_evicted_by_180_older(self):
        s=v.new_state()
        for i in range(220):s['ledger']['solana:'+str(i)]={'chain':'solana','mint':str(i),'pools':{POOL:{'created_ms':START-3600000}},'first_seen_ms':START-3600000,'status':'queued','reasons':[]}
        d.remember_identity(s,'solana',MINT,POOL,START-60000,START)
        selected=d.quote_plan(s,'solana',CFG,START);self.assertIn(MINT,selected);self.assertEqual(len(s['ledger']),221)
    def test_feed_staleness_not_fresh_price(self):
        s=v.new_state();feed={'version':'meme-v7-discovery-feed','observed_ms':START-181000,'identities':[{'chain':'solana','mint':MINT,'pool':POOL,'created_ms':START-300000,'first_seen_ms':START-180000}]}
        self.assertFalse(d.merge_feed(s,feed,CFG,START));self.assertEqual(len(s['ledger']),1);self.assertFalse(s['assets'])
    def test_future_feed_rejected(self):
        with self.assertRaises(ValueError):d.merge_feed(v.new_state(),{'version':'meme-v7-discovery-feed','observed_ms':NOW+60001,'identities':[]},CFG,NOW)
    def test_fresh_heartbeat_never_hides_network_429(self):
        s=v.new_state();feed={'version':'meme-v7-discovery-feed','observed_ms':NOW,'identities':[],
            'networks':{chain:{'last_observed_ms':NOW,'last_error':None} for chain in CFG['networks']}}
        feed['networks']['solana'].update(last_error='HTTP 429',due_ms=NOW+900000)
        self.assertFalse(d.merge_feed(s,feed,CFG,NOW));self.assertEqual(s['provider_backoff_until_ms'],NOW+900000)
    def test_ledger_first_seen_immutable(self):
        s=v.new_state();d.remember_identity(s,'solana',MINT,POOL,START-1000,START);d.remember_identity(s,'solana',MINT,POOL,START-1000,NOW)
        self.assertEqual(s['ledger']['solana:'+MINT]['first_seen_ms'],START)
    def test_queue_defer_explicit(self):
        s=v.new_state()
        for i in range(100):s['ledger']['solana:'+str(i)]={'chain':'solana','mint':str(i),'pools':{POOL:{'created_ms':START}},'first_seen_ms':START,'status':'queued','reasons':[]}
        self.assertEqual(len(d.quote_plan(s,'solana',CFG,NOW)),60);self.assertEqual(sum(r['status']=='quote_budget_waiting' for r in s['ledger'].values()),40)
    def test_ledger_decision_transition_history(self):
        s=v.new_state();d.remember_identity(s,'solana',MINT,POOL,START-1,START)
        for t,reason in ((START,'x'),(START+1,'x'),(START+2,'y')):d.decision(s,asset(),t,'wait',[reason])
        self.assertEqual(len(s['ledger']['solana:'+MINT]['decision_history']),2)
    def test_collector_durable_identity_and_catchup(self):
        with tempfile.TemporaryDirectory() as td:
            x=c.Collector(Path(td)/'a.db',CFG,lambda:START);x.consume('solana',pool_payload(START-120000),START)
            self.assertEqual(x.progress['solana']['covered_until_ms'],START);self.assertEqual(x.feed(START)['total_identities_durable'],1)
            x.db.close();y=c.Collector(Path(td)/'a.db',CFG,lambda:NOW);self.assertEqual(y.feed(NOW)['total_identities_durable'],1);y.db.close()
    def test_collector_page_cap_preserves_gap(self):
        cfg=copy.deepcopy(CFG);cfg['v7']['collector_max_pages']=1
        with tempfile.TemporaryDirectory() as td:
            x=c.Collector(Path(td)/'a.db',cfg,lambda:START);x.consume('solana',pool_payload(START-1000),START)
            self.assertEqual(x.progress['solana']['gaps'][0]['reason'],'page_budget_exhausted');self.assertIsNone(x.progress['solana']['covered_until_ms']);x.db.close()
    def test_collector_429_is_gap_not_healthy(self):
        with tempfile.TemporaryDirectory() as td:
            x=c.Collector(Path(td)/'a.db',CFG,lambda:START);x.consume('solana',{},START,'HTTP 429')
            self.assertEqual(x.progress['solana']['due_ms'],START+900000);self.assertTrue(x.progress['solana']['gaps']);x.db.close()

class DeliveryTests(unittest.TestCase):
    def test_v6_references_preserved_and_no_v7_backfill(self):
        old=old_state();s=v.seed(old,'a'*40);self.assertEqual(s['legacy_v6']['entries'],old['entries']);self.assertFalse(s['entries']);self.assertFalse(s['events']);self.assertFalse(s['cases'])
    def test_unexpected_archive_rejected(self):
        old=old_state();old['rules_fingerprint']='other'
        with self.assertRaises(ValueError):v.seed(old,'a'*40)
    def test_phase_headers_and_copyable_contract(self):
        s=v.new_state()
        for phase in ('early_radar','entry_5m','confirmed_15m'):
            details={'activity':m.activity(asset(),CFG)}
            if phase=='entry_5m':details={'risk':m.entry_guard(asset(),setup(),{'status':'passed'},sec(),dev(),maps(),route(),CFG,NOW),'buy_pressure':{'status':'unknown'},'roundtrip':route()}
            e=m.event(s,asset(),phase,NOW,details);title,body=v.event_body(e)
            self.assertIn(MINT,body);self.assertIn('```text',body);self.assertIn(m.LABELS[phase],title);self.assertIn('coin-tarama-meme-v7:'+e['id'],body)
    def test_actual_reference_price_is_not_candle_close(self):
        s=v.new_state();a=asset(price_usd=102.25);v.reference(s,a,'entry_5m',{});v.reference(s,asset(price_usd=200),'entry_5m',{})
        self.assertEqual(s['entries'][m.key(a)]['references']['entry_5m']['price'],102.25)
    def test_bad_quote_identity_rejected(self):
        class Client:
            def request(self,*args,**kwargs):return {'success':True,'data':{'swapType':'BaseIn','routePlan':[{}],'inputMint':'wrong','outputMint':MINT,'inputAmount':'100','outputAmount':'5'}}
        with self.assertRaises(ValueError):r.ray(Client(),'A',MINT,'100')
    def test_unknown_route_never_turns_into_zero_cost(self):
        class Client:
            def dex(self,*args):return []
        with patch.object(r.prior,'read_decimals',return_value=6):out=r.roundtrip(Client(),{},asset(),sec(),CFG)
        self.assertEqual(out['status'],'unknown');self.assertIsNone(out['net_realized_pnl_usd'])

class OperationalTests(unittest.TestCase):
    def test_active_entry_kept_for_24h_even_if_pool_age_exceeds24h(self):
        s=v.new_state();d.remember_identity(s,'solana',MINT,POOL,START-24*3600000,START)
        s['entries'][m.key(asset())]={'references':{'entry_5m':{'observed_ms':START}}}
        self.assertIn(MINT,d.quote_plan(s,'solana',CFG,START+3600000))
    def test_cold_archive_requires_published_snapshot_and_preserves_refs(self):
        s=v.new_state();d.remember_identity(s,'solana',MINT,POOL,START-28*3600000,START)
        v.archive_cold_identities(s,START);self.assertEqual(len(s['ledger']),1)
        s['publication']={'commit':'a'*40};v.archive_cold_identities(s,START)
        self.assertFalse(s['ledger']);self.assertEqual(s['cold_archives'][0]['source_state_sha'],'a'*40)
    def test_no_strengthening_without_real_entry_receipt(self):
        s=v.new_state();a=asset();ref=v.reference(s,a,'entry_5m',{'observed_ms':NOW,'base':setup()['first_base']})
        rec={'latest':a,'eligible_since_ms':START};s['assets'][m.key(a)]=rec
        with patch.object(v.source,'candles',return_value=bars()),patch.object(v.model,'strengthened',return_value=True) as strength,patch.object(v,'now_ms',return_value=NOW):
            v.evaluate(s,rec,object(),CFG,NOW);strength.assert_not_called();self.assertFalse(s['events'])
    def test_green_notification_lost_response_reconciles_without_duplicate(self):
        s=v.new_state();a=asset();pressure={'status':'passed','buy_usd':1000,'sell_usd':100,'net_buy_usd':900,'buy_volume_fraction':.9,'net_buy_initiators':3}
        risk=m.entry_guard(a,setup(),pressure,sec(),dev(),maps(),route(),CFG,NOW)
        details={'setup':setup(),'risk':risk,'buy_pressure':pressure,'security':sec(),'developer':dev(),'maps':maps(),'roundtrip':route()}
        ev=m.event(s,a,'entry_5m',NOW,details);s['assets'][m.key(a)]={'latest':a};accepted=[];posts=[]
        def http(url,payload=None,*args,**kwargs):
            if payload is None:return accepted
            posts.append(payload);accepted.append({'number':123,'html_url':'https://example.invalid/fixture','user':{'login':'github-actions[bot]'},'body':payload['body'],'created_at':'fixture'})
            raise RuntimeError('Synthetic response lost after acceptance')
        with tempfile.TemporaryDirectory() as td,patch.object(v,'STATE',Path(td)/'state.json'),patch.object(v,'now_ms',return_value=NOW),patch.dict(v.os.environ,{'GITHUB_REPOSITORY':'selvisezgin01-ux/Coin-Tarama','GH_TOKEN':'fixture','COIN_NOTIFY_USER':''}),patch.object(v.cloud,'http_json',side_effect=http),patch.object(v.discovery,'dex_quotes',return_value=[a]):
            with self.assertRaises(RuntimeError):v.notify(s,CFG)
            v.notify(s,CFG)
        self.assertEqual(len(posts),1);self.assertEqual(s['events'][ev['id']]['price'],102);self.assertEqual(s['receipts'][ev['id']]['issue_number'],123)
    def test_known_block_cancels_yellow_before_delivery(self):
        s=v.new_state();a=asset();ev=m.event(s,a,'early_radar',NOW,{'activity':{}});s['assets'][m.key(a)]={'security':{'blocked':True}}
        with tempfile.TemporaryDirectory() as td,patch.object(v,'STATE',Path(td)/'state.json'),patch.object(v,'now_ms',return_value=NOW),patch.dict(v.os.environ,{'GITHUB_REPOSITORY':'selvisezgin01-ux/Coin-Tarama','GH_TOKEN':'fixture'}),patch.object(v.cloud,'http_json',return_value=[]) as http:
            v.notify(s,CFG)
        self.assertEqual(http.call_count,1);self.assertIn('notification_expired_ms',ev)
    def test_feed_publisher_refuses_other_writer(self):
        with tempfile.TemporaryDirectory() as td:
            p=Publisher(td,request=lambda *args:[{'name':FEED_BRANCH,'commit':{'sha':'b'*40}}]);p.journal.write_text(json.dumps({'accepted_parent':'a'*40}),encoding='utf-8')
            with self.assertRaises(RuntimeError):p.publish({'version':'meme-v7-discovery-feed'})
    def test_single_collector_instance(self):
        with tempfile.TemporaryDirectory() as td,single_instance(td):
            with self.assertRaises(RuntimeError):
                with single_instance(td):pass
    def test_meme_publication_cannot_target_coin5(self):
        import meme_v7_persistence as persistence
        self.assertEqual(persistence.BRANCH,'scanner-state-meme-v7')

if __name__=='__main__':unittest.main()
