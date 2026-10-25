"""Actual observation integrity, stage deduplication and minute endpoint semantics."""
from copy import deepcopy
import unittest

import paper_watch as paper


def row(stage='new_breakout',price=10.,observed=1000123):
    return {'symbol':'TESTUSDT','stage':stage,'observed_ms':observed,'mid_price':price,'paper_btc_price':100.,
            'paper_controls':[{'symbol':f'C{i}USDT','entry_price':10.} for i in range(3)]}


class PaperChecks(unittest.TestCase):
    def test_first_actual_observation_stays_immutable_when_stage_changes(self):
        state = {}
        paper.register(state,{'MEXC':{'candidates':[row()]}})
        original = deepcopy(state['paper']['entries']['MEXC:TESTUSDT'])
        paper.register(state,{'MEXC':{'candidates':[row('continuation',12.,2000123)]}})
        entry = state['paper']['entries']['MEXC:TESTUSDT']
        self.assertEqual(len(state['paper']['entries']),1)
        self.assertEqual(entry['entry_price'],original['entry_price'])
        self.assertEqual(entry['observed_ms'],original['observed_ms'])
        self.assertEqual(len(entry['stages']),2)

    def test_missing_quote_waits_for_future_real_observation(self):
        state = {}
        paper.register(state,{'MEXC':{'candidates':[row(price=None)]}})
        self.assertEqual(state['paper']['entries'],{})
        paper.register(state,{'MEXC':{'candidates':[row(price=11.,observed=2000123)]}})
        self.assertEqual(state['paper']['entries']['MEXC:TESTUSDT']['observed_ms'],2000123)

    def test_target_is_first_closed_minute_after_exact_horizon(self):
        state = {}
        paper.register(state,{'MEXC':{'candidates':[row()]}})
        entry = state['paper']['entries']['MEXC:TESTUSDT']
        target = entry['observed_ms']+12*3600000
        endpoint = ((target+59999)//60000)*60000
        calls = []
        def fetch(venue,symbol,end):
            calls.append((venue,symbol,end))
            return 105. if symbol=='BTCUSDT' else 11.
        paper.refresh(state,endpoint-1,fetch)
        self.assertEqual(calls,[])
        paper.refresh(state,endpoint,fetch)
        result = entry['outcomes']['12']
        self.assertEqual(result['endpoint_ms'],endpoint)
        self.assertLess(result['endpoint_delay_ms'],60000)
        self.assertAlmostEqual(result['return_pct'],10.)
        self.assertAlmostEqual(result['btc_excess_pct_points'],5.)
        self.assertAlmostEqual(result['control_excess_pct_points'],0.)
        self.assertNotIn('24',entry['outcomes'])

    def test_missing_endpoint_is_unknown_and_retried_after_disappearance(self):
        state = {}
        paper.register(state,{'MEXC':{'candidates':[row()]}})
        paper.register(state,{'MEXC':{'candidates':[]}})
        now = 1000123+12*3600000+60000
        paper.refresh(state,now,lambda *args:None)
        entry = state['paper']['entries']['MEXC:TESTUSDT']
        self.assertIsNone(entry['outcomes']['12']['return_pct'])
        paper.refresh(state,now,lambda venue,symbol,end:100. if symbol=='BTCUSDT' else 12.)
        self.assertAlmostEqual(entry['outcomes']['12']['return_pct'],20.)

    def test_exchange_error_does_not_stop_other_and_shared_coin_is_not_two_symbols(self):
        state = {}
        paper.register(state,{v:{'candidates':[row()]} for v in ['MEXC','OKX']})
        def fetch(venue,symbol,end):
            if venue=='MEXC':raise RuntimeError('unavailable')
            return 100. if symbol=='BTCUSDT' else 11.
        paper.refresh(state,1000123+12*3600000+60000,fetch)
        stats = paper.summary(state)
        self.assertEqual(stats['unique_symbols'],1)
        self.assertEqual(stats['venue_records'],2)
        self.assertEqual(stats['by_exchange']['MEXC']['horizons']['12']['available'],0)
        self.assertEqual(stats['by_exchange']['OKX']['horizons']['12']['available'],1)


if __name__=='__main__':unittest.main()
