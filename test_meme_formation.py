"""Regression cases for post-pump tails accidentally presented as first formations."""
from copy import deepcopy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from contextlib import ExitStack

import meme_rules as rules
import meme_scan as meme
import meme_social_watch as social
from test_meme_scan import candle,CONFIG


class FormationChecks(unittest.TestCase):
    def setUp(self):
        self.asset={'chain':'solana','mint':'mint','pool':'pool','pool_created_ms':0}
        self.rows=[candle(0,volume=4000),candle(1,volume=3000),candle(2,volume=2000),candle(3)]
        self.stamp=3*rules.STEP_MS+60000

    def check(self,rows=None,earliest=0,asset=None):
        return rules.first_formation(rows if rows is not None else self.rows,asset or self.asset,earliest,self.stamp,CONFIG)

    def test_quiet_launch_requires_launch_and_current_interval_coverage(self):
        self.assertEqual(self.check()['status'],'passed')
        self.assertEqual(self.check(self.rows[1:])['status'],'unknown')
        self.assertEqual(self.check(self.rows[:-1])['reason'],'current_interval_history_missing')

    def test_multiple_small_rises_cannot_hide_behind_small_individual_bodies(self):
        rows=[candle(0,high=1.16,close=1.15),candle(1,opening=1.15,high=1.32,low=1.14,close=1.3),
              candle(2,opening=1.30,high=1.31,low=1.01,close=1.02),candle(3)]
        self.assertEqual(self.check(rows)['status'],'rejected')
        self.assertIn('first_rise_already_observed',self.check(rows)['reason'])

    def test_upper_wick_in_open_candle_blocks_but_never_generates_a_positive_setup(self):
        rows=deepcopy(self.rows);rows[-1]=candle(3,high=1.8,close=1.02)
        self.assertEqual(self.check(rows)['status'],'rejected')
        self.assertEqual(rules.closed_candles(rows,self.stamp),rules.closed_candles(self.rows,self.stamp))

    def test_pump_before_gap_is_still_examined_and_gap_without_pump_is_unknown(self):
        rows=[candle(0,high=2,close=1.01),candle(2),candle(3)]
        self.assertEqual(len(rules.closed_candles(rows,self.stamp)),1)
        self.assertEqual(self.check(rows)['status'],'rejected')
        self.assertEqual(self.check([self.rows[0],self.rows[2],self.rows[3]])['reason'],'initial_history_has_gaps')

    def test_new_pool_does_not_reset_previously_observed_age(self):
        asset={**self.asset,'pool_created_ms':rules.STEP_MS}
        self.assertEqual(self.check(asset=asset)['reason'],'earlier_pool_history_not_covered')

    def test_future_candle_cannot_disqualify_a_past_observation(self):
        self.assertEqual(self.check(self.rows+[candle(4,high=99,close=50)]),self.check())

    def test_new_experiment_keeps_real_age_and_social_baselines_without_backdated_signals(self):
        previous={'version':'meme-v2','rules_fingerprint':'7cd0a36fdb87a00b75afb7ef6d96d24f11ccde772445318eee9380ecb6e0d80e',
            'assets':{'solana:mint':{'latest':self.asset,'first_seen_ms':1,'earliest_pool_created_ms':0,'tier':'qualified'}},
            'entries':{},'pending':[],'social_watch':{'tokens':{'solana:mint':{'observed_link_changes':2}}}}
        state=meme.seed_first_formation(previous,'scanner-state-meme-v2','commit')
        self.assertEqual(state['entries'],{});self.assertNotIn('tier',state['assets']['solana:mint'])
        self.assertEqual(state['social_watch'],previous['social_watch'])
        previous['entries']={'real_measurement':{}}
        with self.assertRaises(ValueError):meme.seed_first_formation(previous,'scanner-state-meme-v2','commit')

    def test_social_report_hides_unfiltered_discovery_tokens_and_preserves_baseline(self):
        state={'entries':{},'social_watch':{'tokens':{'solana:mint':{'chain':'solana','mint':'mint','symbol':'RAW_TOKEN',
              'observed_link_changes':0,'last_observed_ms':1}},'last_run':{'errors':[]}}}
        with TemporaryDirectory() as directory,patch.object(meme,'OUT',Path(directory)):
            (meme.OUT/'report.md').write_text('# Report\n',encoding='utf-8')
            social.append_report(state);report=(meme.OUT/'report.md').read_text(encoding='utf-8')
            self.assertNotIn('RAW_TOKEN',report);self.assertIn('Henüz aday yok',report)
        self.assertIn('solana:mint',state['social_watch']['tokens'])

    def test_social_render_migration_preserves_events_and_observations(self):
        old={'version':1,'fingerprint':social.LEGACY_FINGERPRINT,'tokens':{'token':{'changes':2}},'pending':[{'event':1}]}
        state={'social_watch':deepcopy(old)};result=social.social_state(state)
        self.assertEqual(result['tokens'],old['tokens']);self.assertEqual(result['pending'],old['pending'])
        self.assertEqual(result['migration']['from_fingerprint'],social.LEGACY_FINGERPRINT)

    def test_breakout_followup_requires_a_previously_delivered_accumulation(self):
        key='solana:mint';state={'entries':{},'pending':[]}
        self.assertFalse(meme.previously_alerted_accumulation(state,key))
        state['entries'][key]={'references':{'qualified':{'stage':'accumulation'}},'alerted_stages':['accumulation']}
        self.assertTrue(meme.previously_alerted_accumulation(state,key))
        state['pending']=[{'candidates':[{'chain':'solana','mint':'mint','stage':'accumulation'}]}]
        self.assertFalse(meme.previously_alerted_accumulation(state,key))

    def network_scan(self,rows,state,stamp):
        asset={**self.asset,'symbol':'TEST','price_usd':1.02,'price_observed_ms':stamp,'liquidity_usd':20000,
               'market_cap_usd':200000,'volume15_usd':2000,'buys15':18,'sells15':10}
        with ExitStack() as stack:
            stack.enter_context(patch.object(meme,'now_ms',return_value=stamp))
            stack.enter_context(patch.object(meme.source,'discover',return_value=([asset],[],[])))
            stack.enter_context(patch.object(meme.source,'refresh_pools',return_value=[]))
            stack.enter_context(patch.object(meme.source,'dex_enrich',return_value=[asset]))
            stack.enter_context(patch.object(meme.source,'candles',return_value=rows))
            check=stack.enter_context(patch.object(meme.security_api,'fetch_security',return_value={'complete':True,'blocked':False}))
            stack.enter_context(patch.object(meme.security_api,'fetch_map',return_value={'complete':False}))
            stack.enter_context(patch.object(meme.security_api,'developer_check',return_value={'status':'no_outgoing_transfers_in_complete_window'}))
            stack.enter_context(patch.object(meme.source,'quote',return_value={'price_usd':1.02,'price_observed_ms':stamp}))
            result=meme.scan_network('solana',CONFIG['networks']['solana'],state,CONFIG,None)
            return result,check.call_count

    def test_actual_orchestration_rejects_pump_before_security_and_preserves_latch(self):
        state={'entries':{},'assets':{},'pending':[]}
        rows=deepcopy(self.rows);rows[0]=candle(0,high=1.8,close=1.02,volume=4000)
        result,calls=self.network_scan(rows,state,self.stamp)
        self.assertEqual(calls,0);self.assertEqual(result['qualified'],[])
        self.assertIn('first_formation_disqualified',state['assets']['solana:mint'])
        # Even if the provider later returns a quiet history, the recorded pump is retained.
        result,calls=self.network_scan(self.rows,state,self.stamp)
        self.assertEqual(calls,0);self.assertEqual(result['qualified'],[])

    def test_actual_orchestration_can_qualify_quiet_launch_but_not_first_seen_breakout(self):
        state={'entries':{},'assets':{},'pending':[]}
        result,_=self.network_scan(self.rows,state,self.stamp)
        self.assertEqual(len(result['qualified']),1)
        self.assertEqual(result['qualified'][0]['stage'],'accumulation')
        rows=self.rows[:3]+[candle(3,opening=1.02,high=1.1,low=1.01,close=1.09,volume=6000),candle(4)]
        result,calls=self.network_scan(rows,{'entries':{},'assets':{},'pending':[]},4*rules.STEP_MS+60000)
        self.assertEqual(calls,0);self.assertEqual(result['qualified'],[])
        self.assertEqual(result['evaluated'][0]['reason'],'first_encounter_after_breakout_excluded')


if __name__=='__main__':unittest.main()
