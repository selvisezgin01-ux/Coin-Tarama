import copy,json,unittest
from unittest.mock import patch
import one_coin as w
import one_coin_worker as worker
M=w.config()['tokens'][0]['mint'];OTHER=w.config()['tokens'][1]['mint'];W='2LoNg8b8wYneseTQ4FYEVQxSJWp12tsLE799oUdYPDHB';A='2x6Uhxmaot1cpiRisNwUcaQFPJCryGE4aTdpTYhYLENS'
class Tests(unittest.TestCase):
    def state(self):return w.new_state()
    def token(self):return {'mint':M,'market':{'liquidity':100000},'seen_trades':{}}
    def row(self,tx='a',usd=600,ms=100,side='buy'):return {'tx':tx*88,'wallet':W,'usd':usd,'block_ms':ms,'side':side}
    def test_exact_mint_chain_and_orientation(self):
        r={'chainId':'solana','baseToken':{'address':M},'pairAddress':A,'priceUsd':'1','liquidity':{'usd':100}}
        self.assertEqual(len(w.market([r],M)),1)
        for wrong in [{**r,'chainId':'eth'},{**r,'baseToken':{'address':OTHER}},{**r,'priceUsd':'nan'}]:self.assertEqual(w.market([wrong],M),[])
    def test_historical_baseline_is_never_notified(self):
        s=self.state();t=self.token();w.ingest_trades(s,t,[self.row()],[],1000,w.config());self.assertEqual(s['events'],[])
        w.ingest_trades(s,t,[self.row('b',ms=500)],[],2000,w.config());self.assertEqual(s['events'],[])
    def test_live_swaps_and_retry_dedup(self):
        s=self.state();t=self.token();w.ingest_trades(s,t,[],[],1000,w.config())
        r=self.row(ms=1500);w.ingest_trades(s,t,[r,r],[],2000,w.config());w.ingest_trades(s,t,[r],[],3000,w.config())
        self.assertEqual(len(s['events']),1);self.assertEqual(s['events'][0]['kind'],'BÜYÜK ALIM')
    def test_routed_signature_not_summed_across_pools(self):
        s=self.state();t=self.token();w.ingest_trades(s,t,[],[],1000,w.config())
        w.ingest_trades(s,t,[self.row(usd=600,ms=1500),self.row(usd=800,ms=1500)],[],2000,w.config())
        self.assertEqual(t['flow15_sample']['buy_usd'],800);self.assertEqual(len(s['events']),1)
    def test_sell_not_buy(self):
        s=self.state();t=self.token();w.ingest_trades(s,t,[],[],1000,w.config());w.ingest_trades(s,t,[self.row(ms=1500,side='sell')],[],2000,w.config())
        self.assertEqual(s['events'][0]['kind'],'SATIŞ');self.assertEqual(t['flow15_sample']['net_usd'],-600)
    def test_old_buyer_not_called_new_wallet(self):
        s=self.state();t=self.token();w.ingest_trades(s,t,[self.row(ms=500)],[],1000,w.config());w.ingest_trades(s,t,[self.row('b',ms=1500)],[],2000,w.config())
        self.assertFalse(s['events'][0]['details']['first_buyer_seen_by_this_watch'])
    def test_changes_require_tracked_mint_and_owner(self):
        tx={'meta':{'preTokenBalances':[{'mint':M,'owner':W,'accountIndex':0,'uiTokenAmount':{'amount':'100','decimals':1}}],'postTokenBalances':[{'mint':M,'owner':W,'accountIndex':0,'uiTokenAmount':{'amount':'150','decimals':1}}]}}
        result,owners=w.token_balances(tx,{M});self.assertEqual(result[0]['change_tokens'],5)
        self.assertEqual(w.token_balances(tx,{OTHER})[0],[])
    def test_explicit_transfer_not_same_ownership_or_purchase(self):
        tx={'transaction':{'message':{'accountKeys':[M,OTHER],'instructions':[{'parsed':{'type':'transfer','info':{'source':M,'destination':OTHER}}}]}}}
        e=w.explicit_edges(tx,{0:W,1:A});self.assertEqual(len(e),1);self.assertIn('not proof',e[0]['interpretation'])
        self.assertEqual(w.explicit_edges(tx,{0:W}),[])
    def test_wallet_initial_history_is_baseline(self):
        s=self.state();wallet=s['wallets'][W]
        class Client:
            def rpc(self,*args):return [{'signature':'first','blockTime':1,'err':None}]
        w.watch_wallet(s,wallet,Client(),w.config());self.assertEqual(wallet['cursor'],'first');self.assertEqual(s['events'],[])
        w.watch_wallet(s,wallet,Client(),w.config());self.assertEqual(s['events'],[])
    def test_pagination_retains_old_watermark_until_covered(self):
        s=self.state();wallet=s['wallets'][W];wallet['cursor']='old';cfg={**w.config(),'signatures_per_page':1,'signature_pages_per_wallet':1}
        class Client:
            def __init__(self,signature):self.signature=signature
            def rpc(self,*args):return [{'signature':self.signature,'blockTime':2,'err':None}]
        w.watch_wallet(s,wallet,Client('new'),cfg);self.assertEqual(wallet['cursor'],'old');self.assertEqual(wallet['before'],'new');self.assertEqual(wallet['pending_head'],'new')
        w.watch_wallet(s,wallet,Client('old'),cfg);self.assertEqual(wallet['cursor'],'new');self.assertIsNone(wallet['before'])
    def test_first_activity_after_empty_wallet_baseline_is_not_lost(self):
        s=self.state();wallet=s['wallets'][W]
        class Client:
            rows=[]
            def rpc(self,*args):return self.rows
        client=Client();w.watch_wallet(s,wallet,client,w.config())
        client.rows=[{'signature':'later','blockTime':w.now()//1000+1,'err':None}]
        w.watch_wallet(s,wallet,client,w.config());self.assertEqual(len(s['events']),1)
    def test_no_trading_or_signing_rpc(self):
        client=w.Public(self.state(),w.config())
        with self.assertRaises(ValueError):client.rpc('sendTransaction',[])
        with self.assertRaises(ValueError):client.get('https://evil.example/token')
    def test_failed_reads_do_not_become_empty_wallet_activity(self):
        s=self.state()
        class Client:
            def rpc(self,*args):raise RuntimeError('provider: HTTP429')
        w.rpc_watch(s,Client(),w.config());self.assertTrue(s['coverage']['wallets']['errors']);self.assertNotIn('last_checked_ms',s['wallets'][W])
    def test_receipt_recovery_does_not_duplicate_issue(self):
        s=self.state();w.event(s,'test',M,'ALIM','test');e=s['pending'][0]
        class Cloud:
            def http_json(self,url,payload=None,**kwargs):
                self_case.assertIsNone(payload)
                return [{'number':99,'html_url':'https://github.com/selvisezgin01-ux/Coin-Tarama/issues/99','body':'<!-- 1-coin:'+e['id']+' -->','user':{'login':'github-actions[bot]'}}]
        self_case=self
        with patch.dict('os.environ',{'GITHUB_REPOSITORY':'selvisezgin01-ux/Coin-Tarama','GH_TOKEN':'test-local-value'}):worker.notify(s,Cloud(),lambda s:None)
        self.assertEqual(s['pending'],[]);self.assertEqual(s['delivery'][0]['issue'],99)
    def test_notification_contains_copyable_exact_contract_and_tx(self):
        s=self.state();w.event(s,'test',M,'ALIM','test',self.row());txt=worker.event_text(s['pending'][0]);self.assertIn('```text\n'+M+'\n```',txt);self.assertIn('https://solscan.io/tx/',txt)
    def test_report_explicitly_exposes_unknown_coverage(self):
        txt=w.render(self.state());self.assertIn('bütün zincir/bütün cüzdanlar izlenmiyor',txt);self.assertIn('BİLİNMİYOR',txt)
    def test_holder_dropping_out_of_top20_is_not_a_zero_balance(self):
        s=self.state();t=self.token();t['holder_snapshot']={'owners':{W:100}}
        w.holder_changes(s,t,[],99,w.config());self.assertEqual(s['events'],[]);self.assertEqual(t['holder_snapshot']['dropped_from_sample'],[W])
    def test_known_lp_owner_not_counted_as_whale(self):
        s=self.state();t=self.token();t['excluded_infrastructure']=[W]
        row={'data':{'parsed':{'info':{'owner':W,'mint':M,'tokenAmount':{'amount':'100000000','decimals':6}}}}}
        w.holder_changes(s,t,[row],99,w.config());self.assertEqual(t['holder_snapshot']['owners'],{})
    def test_sample_membership_change_does_not_fake_a_wallet_outflow(self):
        s=self.state();t=self.token();t['holder_snapshot']={'owners':{W:200},'accounts':{M:{'owner':W,'amount':100},OTHER:{'owner':W,'amount':100}}}
        row={'_account':M,'data':{'parsed':{'info':{'owner':W,'mint':M,'tokenAmount':{'amount':'100','decimals':0}}}}}
        w.holder_changes(s,t,[row],100,w.config());self.assertEqual(s['events'],[])
if __name__=='__main__':unittest.main()
