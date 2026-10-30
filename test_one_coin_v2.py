import copy,unittest
import one_coin_v2 as w
import one_coin_analytics as a
M=w.config()['tokens'][0]['mint'];W=w.config()['watched_wallets'][0]['address'];OTHER=w.config()['tokens'][1]['mint']
class Tests(unittest.TestCase):
    def token(self):return {'mint':M,'market':{'liquidity':100000,'price':1,'pool':W},'seen_trades':{},'history':[]}
    def row(self,n,usd=60,side='buy',ms=1500000):return {'tx':str(n)*80,'wallet':W,'usd':usd,'side':side,'block_ms':ms}
    def baseline(self):
        s=w.new_state();t=self.token();w.ingest_trades(s,t,[],[],1000000,w.config());return s,t
    def quiet_token(self):
        t=self.token();stamp=3600000;t['last_trade_check_ms']=stamp
        t['history']=[{'observed_ms':x,'price':1,'pool':W} for x in range(stamp-1200000,stamp+1,300000)]
        t['seen_trades']={str(i):self.row(i,usd=60,ms=stamp-600000+i*60000) for i in range(3)}
        t['flow15_sample']={'coverage':[{'possibly_truncated':False,'invalid':0}]}
        return t,stamp
    def test_floor_relative_to_liquidity(self):
        t=self.token();self.assertEqual(a.threshold(t,w.config()),100);t['market']['liquidity']=200000;self.assertEqual(a.threshold(t,w.config()),200)
    def test_unknown_liquidity_has_no_positive_threshold(self):
        t=self.token();t['market']['liquidity']=None;self.assertIsNone(a.threshold(t,w.config()))
    def test_small_swap_kept_but_not_notified(self):
        s,t=self.baseline();w.ingest_trades(s,t,[self.row(1,.1)],[],2000000,w.config());self.assertEqual(s['pending'],[]);self.assertEqual(len(t['seen_trades']),1);self.assertEqual(t['notification_filter']['small_trades_logged'],1)
    def test_meaningful_buy_and_sell_notified(self):
        s,t=self.baseline();w.ingest_trades(s,t,[self.row(1,150),self.row(2,180,'sell')],[],2000000,w.config());self.assertEqual([e['kind'] for e in s['pending']],['ALIM','SATIŞ'])
    def test_routed_swap_dedup_does_not_cross_floor_by_summing(self):
        s,t=self.baseline();r=self.row(1,60);w.ingest_trades(s,t,[r,dict(r)],[],2000000,w.config());self.assertEqual(s['pending'],[])
    def test_quiet_small_buys_are_detectable_in_aggregate(self):
        t,stamp=self.quiet_token();q=a.quiet(t,stamp,w.config());self.assertEqual(len(q),1);self.assertEqual(q[0]['net_usd'],180)
    def test_sell_churn_is_net_not_gross_accumulation(self):
        t,stamp=self.quiet_token();t['seen_trades']['sell']=self.row(4,170,'sell',stamp-1000);self.assertEqual(a.quiet(t,stamp,w.config()),[])
    def test_already_rising_price_is_not_quiet(self):
        t,stamp=self.quiet_token();t['history'][-1]['price']=1.1;self.assertEqual(a.quiet(t,stamp,w.config()),[])
    def test_price_observation_gap_blocks_quiet(self):
        t,stamp=self.quiet_token();t['history']=t['history'][:1]+t['history'][-2:];self.assertEqual(a.quiet(t,stamp,w.config()),[])
    def test_missing_or_truncated_trades_block_quiet(self):
        t,stamp=self.quiet_token();t['flow15_sample']['coverage'][0]['possibly_truncated']=True;self.assertEqual(a.quiet(t,stamp,w.config()),[])
    def test_unchanged_quiet_does_not_notify_each_cycle(self):
        prev={'stamp':1000,'net_usd':200};self.assertFalse(a.should_repeat(prev,220,2000,w.config()));self.assertTrue(a.should_repeat(prev,310,2000,w.config()))
    def test_holder_accounts_need_exact_mint_owner(self):
        v={'data':{'parsed':{'info':{'owner':W,'mint':M,'tokenAmount':{'amount':'100','decimals':0}}}}}
        r=a.holders([v],[M],M,set(),1000,1,{});self.assertEqual(r['owners'][W]['amount'],100)
        self.assertEqual(a.holders([v],[M],OTHER,set(),1000,1,{})['owners'],{})
    def test_infrastructure_excluded(self):
        v={'data':{'parsed':{'info':{'owner':W,'mint':M,'tokenAmount':{'amount':'100','decimals':0}}}}};self.assertEqual(a.holders([v],[M],M,{W},1000,1,{})['owners'],{})
    def test_missing_holder_not_zero_or_sell(self):
        previous={'accounts':{M:{'owner':W,'amount':100}}};r=a.holders([None],[M],M,set(),1000,1,previous);self.assertEqual(r['owners'],{});self.assertEqual(r['missing'],[M])
    def test_connections_require_explicit_mint_specific_transfer(self):
        changes={W:{'change_tokens':10},OTHER:{'change_tokens':5}};e={'mint':M,'source_owner':W,'destination_owner':OTHER,'evidence':'explicit_token_transfer'}
        self.assertEqual(a.groups([e],changes,M)[0]['change_tokens'],15);self.assertEqual(a.groups([dict(e,evidence='rumor')],changes,M),[]);self.assertEqual(a.groups([e],changes,OTHER),[])
    def test_migration_preserves_quotes_wallets_and_seen_swaps(self):
        old=w.new_state();old.update(version='1-coin-v1',rules_fingerprint='778ab62a65e684bb326ffc593f092d340bd76c14bd8ed0be25a56dc446f931b6');old['tokens'][M]=self.token();old['tokens'][M]['seen_trades']['abc']=self.row(1);before=copy.deepcopy(old)
        s=w.migrate(old,'sha');self.assertEqual(s['tokens'],old['tokens']);self.assertEqual(s['wallets'],old['wallets']);self.assertEqual(s['pending'],[]);self.assertEqual(old,before);self.assertEqual(s['archive']['source_sha'],'sha')
    def test_no_trading_rpc_and_no_largest_account_retry(self):
        p=w.Public(w.new_state(),w.config())
        for method in ('sendTransaction','getTokenLargestAccounts'):
            with self.assertRaises(ValueError):p.rpc(method,[])
if __name__=='__main__':unittest.main()
