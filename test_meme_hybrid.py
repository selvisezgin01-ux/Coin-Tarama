from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch, Mock
import json
import unittest
import meme_hybrid as hybrid
import meme_large_buyers as large
import meme_scan as scan
import meme_rules as rules
from test_meme_scan import CONFIG


def bar(i, volume=1000, high=1.04):
    return [i*300,1.,high,.99,1.02,volume]


class HybridTests(unittest.TestCase):
    def setUp(self):
        self.asset={'chain':'ethereum','mint':'0x'+'1'*40,'pool':'0x'+'2'*40,'symbol':'TEST',
            'pool_created_ms':0,'price_usd':1.02,'liquidity_usd':20000,'market_cap_usd':200000,
            'volume15_usd':3000,'buys15':20,'sells15':10}

    def test_15_minute_early_setup_never_waits_for_45_minutes(self):
        rows=[bar(0,3000),bar(1,2000),bar(2,1000),bar(3)]
        result=hybrid.evaluate(rows,self.asset,0,16*60000,CONFIG)
        self.assertEqual(result['phase'],'early_5m')
        self.assertEqual(result['setup']['stage'],'accumulation')
        self.assertEqual(result['formation']['status'],'passed')
        self.assertEqual(result['phases']['confirmed_15m']['closed_count'],1)

    def test_open_candle_never_generates_early_positive_and_future_does_not_repaint(self):
        rows=[bar(0,3000),bar(1,2000),bar(2,1000)]
        self.assertIsNone(hybrid.evaluate(rows,self.asset,0,14*60000,CONFIG)['setup']['stage'])
        early=hybrid.evaluate(rows+[bar(3)],self.asset,0,16*60000,CONFIG)
        later=hybrid.evaluate(rows+[bar(3),bar(4,high=3)],self.asset,0,16*60000,CONFIG)
        self.assertEqual(early,later)

    def test_launch_fragment_is_not_counted_as_a_full_positive_candle(self):
        asset={**self.asset,'pool_created_ms':60000}
        result=hybrid.evaluate([bar(0,4000),bar(1,3000),bar(2,2000),bar(3,1000)],asset,60000,16*60000,CONFIG)
        self.assertEqual(result['phases']['early_5m']['closed_count'],2)
        self.assertIsNone(result['setup']['stage'])

    def test_15m_confirmation_requires_all_three_full_5m_rows_and_closed_intervals(self):
        rows=[bar(i,3000-i*150) for i in range(10)]
        result=hybrid.evaluate(rows,self.asset,0,46*60000,CONFIG)
        self.assertEqual(result['phase'],'confirmed_15m')
        self.assertEqual(result['setup']['stage'],'accumulation')
        self.assertEqual(result['cutoff_ms'],45*60000)
        self.assertEqual(len(hybrid.aggregate_15m(rows,44*60000)),2)
        self.assertEqual(len(hybrid.aggregate_15m(rows[:4]+rows[5:],46*60000)),2)

    def test_past_or_open_pump_still_blocks_early_candidate(self):
        for index in (0,3):
            rows=[bar(0,3000),bar(1,2000),bar(2,1000),bar(3)]
            rows[index][2]=2
            self.assertEqual(hybrid.evaluate(rows,self.asset,0,16*60000,CONFIG)['formation']['status'],'rejected')

    def test_15m_close_remains_current_until_next_15m_boundary(self):
        rows=[bar(i,3000-i*150) for i in range(12)]
        result=hybrid.evaluate(rows,self.asset,0,59*60000,CONFIG)
        self.assertEqual(result['phase'],'confirmed_15m')
        self.assertEqual(result['cutoff_ms'],45*60000)
        self.assertEqual(result['setup']['stage'],'accumulation')

    def test_missing_subbar_does_not_create_15m_confirmation(self):
        rows=[bar(i,3000-i*150) for i in range(10) if i!=4]
        result=hybrid.evaluate(rows,self.asset,0,46*60000,CONFIG)
        self.assertIsNone(result['phases']['confirmed_15m']['setup']['stage'])
        self.assertEqual(result['formation']['status'],'unknown')

    def test_5m_and_15m_use_separate_actual_reference_prices_without_new_token(self):
        state={'entries':{}};asset={**self.asset,'observed_ms':16*60000}
        record={'latest':asset,'signal_phase':'early_5m'}
        scan.observe_entry(state,record,'qualified',{'stage':'accumulation'},CONFIG)
        original=deepcopy(state['entries'][scan.key_of(asset)]['references']['early_5m'])
        asset.update(observed_ms=46*60000,price_usd=1.03);record['signal_phase']='confirmed_15m'
        scan.observe_entry(state,record,'qualified',{'stage':'accumulation'},CONFIG)
        refs=state['entries'][scan.key_of(asset)]['references']
        self.assertEqual(refs['early_5m'],original)
        self.assertEqual(refs['confirmed_15m']['price'],1.03)
        self.assertEqual(refs['qualified']['price'],1.02)
        self.assertEqual(len(state['entries']),1)

    def test_confirmation_can_notify_once_and_never_downgrades_to_early(self):
        row={**self.asset,'observed_ms':1,'stage':'accumulation','signal_phase':'early_5m'}
        state={'entries':{scan.key_of(row):{}},'pending':[]}
        def enqueue(r):return scan.enqueue(state,{'ethereum':{'qualified':[r]}},CONFIG)
        self.assertEqual(len(enqueue(row)),1)
        self.assertEqual(enqueue(row),[])
        self.assertEqual(len(enqueue({**row,'signal_phase':'confirmed_15m','observed_ms':2})),1)
        self.assertEqual(enqueue(row),[])
        state={'entries':{scan.key_of(row):{}},'pending':[]}
        self.assertEqual(len(scan.enqueue(state,{'e':{'qualified':[{**row,'signal_phase':'confirmed_15m'}]}},CONFIG)),1)
        self.assertEqual(scan.enqueue(state,{'e':{'qualified':[row]}},CONFIG),[])

    def test_migration_preserves_prices_pump_latch_and_pending_as_audit_only(self):
        old={'version':'meme-v3','rules_fingerprint':'b3c031ccb7d7142c8f54981df790673fdb670ef391a4e5e3716c268f6f249d1f',
            'assets':{'a':{'setup':{},'first_formation_disqualified':{'reason':'pump'}}},
            'entries':{'a':{'references':{'qualified':{'price':1,'observed_ms':1,'outcomes':{'15':{'return_pct':-10}}}}}},
            'pending':[{'old':'stale'}],'social_watch':{'baseline':1}}
        state=hybrid.seed(old,'scanner-state-meme-v3','sha','new',2)
        self.assertEqual(state['entries']['a']['references'],old['entries']['a']['references'])
        self.assertEqual(state['pending'],[]);self.assertEqual(state['legacy_pending_v3'],old['pending'])
        self.assertEqual(state['assets']['a']['first_formation_disqualified'],{'reason':'pump'})
        self.assertNotIn('early_5m',state['entries']['a']['references'])
        self.assertEqual(state['social_watch'],old['social_watch'])
        old['rules_fingerprint']='wrong'
        with self.assertRaises(ValueError):hybrid.seed(old,'scanner-state-meme-v3','sha','new',2)

    def trade(self, identity, wallet, buy, volume):
        return {'id':identity,'attributes':{'block_timestamp':'1970-01-01T00:15:00Z','tx_from_address':wallet,
            'from_token_address':'0x'+'4'*40 if buy else self.asset['mint'],
            'to_token_address':self.asset['mint'] if buy else '0x'+'4'*40,'volume_in_usd':volume}}

    def assess(self, rows, security=None):
        return large.assess({'data':rows},self.asset,security or {},16*60000,CONFIG)

    def test_same_address_aggregates_buys_minus_sells_and_duplicates_do_not_inflate(self):
        a='0x'+'3'*40;b='0x'+'5'*40
        rows=[self.trade('a',a,True,400),self.trade('b',a,True,400),self.trade('c',a,False,200),self.trade('d',b,True,700),
              self.trade('e','0x'+'6'*40,True,300)]
        result=self.assess(rows+[rows[0]])
        self.assertEqual(result['windows']['15']['large_buyer_count'],2)
        self.assertEqual(result['support_points'],8)
        self.assertEqual(result['windows']['15']['large_buyers'][1]['net_buy_usd'],600)
        self.assertFalse(result['independent_ownership_verified'])

    def test_large_threshold_scales_with_liquidity(self):
        self.asset['liquidity_usd']=1_000_000
        result=self.assess([self.trade('a','0x'+'3'*40,True,600)])
        self.assertEqual(result['threshold_usd'],5000)
        self.assertEqual(result['windows']['15']['large_buyer_count'],0)

    def test_developer_pool_and_known_vault_are_not_large_investors(self):
        wallets=['0x'+'3'*40,self.asset['pool'],'0x'+'5'*40]
        result=self.assess([self.trade(str(i),w,True,1000) for i,w in enumerate(wallets)],
            {'creator':wallets[0],'excluded_known_accounts':[wallets[2]]})
        self.assertEqual(result['status'],'unknown')
        self.assertIsNone(result['support_points'])

    def test_concentrated_or_fast_resale_flow_cannot_earn_support(self):
        a='0x'+'3'*40;b='0x'+'5'*40
        result=self.assess([self.trade('a',a,True,5000),self.trade('b',b,True,500)])
        self.assertEqual(result['support_points'],0)
        rows=[self.trade('a',a,True,2000),self.trade('b',a,False,1200),self.trade('c',b,True,2000)]
        self.assertEqual(self.assess(rows)['support_points'],0)

    def test_missing_empty_or_truncated_data_is_unknown_and_future_trades_not_positive(self):
        self.assertIsNone(self.assess([])['support_points'])
        row=self.trade('a','0x'+'3'*40,True,None)
        self.assertIsNone(self.assess([row])['support_points'])
        rows=[self.trade(str(i),'0x'+'3'*40,True,1000) for i in range(300)]
        self.assertEqual(self.assess(rows)['status'],'unknown')
        row=self.trade('a','0x'+'3'*40,True,1000);row['attributes']['block_timestamp']='1970-01-01T00:17:00Z'
        self.assertEqual(self.assess([row])['status'],'unknown')

    def test_provider_failure_returns_unknown_instead_of_blocking_or_positive_points(self):
        client=Mock();client.gecko.side_effect=RuntimeError('HTTP 429')
        result=large.observe(client,CONFIG['networks']['ethereum'],self.asset,{},lambda:16*60000,CONFIG)
        self.assertEqual(result['status'],'unknown');self.assertIsNone(result['support_points'])

    def test_early_orchestration_keeps_security_gates_and_optional_data_failure(self):
        stamp=16*60000;asset={**self.asset,'price_observed_ms':stamp}
        rows=[bar(0,3000),bar(1,2000),bar(2,1000),bar(3)]
        state={'entries':{},'assets':{},'pending':[]}
        with patch.object(scan,'now_ms',return_value=stamp),patch.object(scan.source,'discover',return_value=([asset],[],[])),\
             patch.object(scan.source,'refresh_pools',return_value=[]),patch.object(scan.source,'dex_enrich'),\
             patch.object(scan.source,'candles',return_value=rows),\
             patch.object(scan.security_api,'fetch_security',return_value={'complete':True}),\
             patch.object(scan.security_api,'fetch_map',return_value={'complete':False}),\
             patch.object(scan.security_api,'developer_check',return_value={'status':'no_outgoing_transfers_in_complete_window'}),\
             patch.object(scan.source,'quote',return_value={'price_usd':1.02,'price_observed_ms':stamp}),\
             patch.object(scan.large_buyers,'observe',return_value={'status':'unknown','support_points':None}):
            result=scan.scan_network('ethereum',CONFIG['networks']['ethereum'],state,CONFIG,None)
            self.assertEqual(result['qualified'][0]['signal_phase'],'early_5m')
            with patch.object(scan.security_api,'fetch_security',return_value={'complete':False,'unknown':['honeypot']}):
                result=scan.scan_network('ethereum',CONFIG['networks']['ethereum'],state,CONFIG,None)
                self.assertEqual(result['qualified'],[]);self.assertEqual(len(result['review']),1)

if __name__=='__main__':unittest.main()
