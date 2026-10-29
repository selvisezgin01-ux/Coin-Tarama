import unittest,json
from copy import deepcopy
from unittest.mock import patch
import coin5_v2_model as m
import coin5_v2_scan as run
import coin5_v2_measure as measure
import coin5_v2_worker as worker
from test_coin5 import candles,series,market,point,STAMP

C=m.config()
def asset():
    return {'id':'a','symbol':'TESTUSDT','exchange':'MEXC','phase':'preparation','created_ms':STAMP-2700000,
        'level':101.,'invalid':98.,'base_invalid':98.,'atr':2.}
def sample():
    bs=series()
    bs['15m'][-3].update(o=100,h=102,l=100,c=101.8,v=200)
    bs['15m'][-2].update(o=101.1,h=101.5,l=100.9,c=101.3,v=90)
    bs['15m'][-1].update(o=101.3,h=102,l=101.2,c=101.7,v=120)
    bs['4h'][40]['h']=120
    return {'symbol':'TESTUSDT','exchange':'MEXC','quote':{'price':101.8,'spread_pct':.1,'observed_ms':STAMP},
        'series':bs,'context':{'reasons':[],'atr':2.,'btc_long_blocked':False},
        'derivatives':{'ready':True,'reasons':[],'profiles':{},'score':0,'strict_short_confirmed':False,'short_information':'unknown'},
        'preparation':{'valid':False},'book_reasons':[],'btc_quote':{'price':1000},'volume24':2e6,'observed_ms':STAMP}

class Sequence(unittest.TestCase):
    def test_three_distinct_closed_bars_trigger_current_quote(self):
        a=asset();r=sample();self.assertEqual(m.transition(a,r,STAMP,C),'triggered')
        self.assertEqual(a['trigger_price'],101.8);self.assertLess(a['break_close_ms'],a['retest_close_ms'])
        self.assertLess(a['retest_close_ms'],a['trigger_bar_close_ms'])
    def test_breakout_alone_never_triggers(self):
        r=sample();r['series']['15m']=r['series']['15m'][:-2];a=asset()
        self.assertIsNone(m.transition(a,r,STAMP-1800000,C));self.assertIn('break_close_ms',a)
    def test_retest_alone_never_triggers(self):
        r=sample();r['series']['15m']=r['series']['15m'][:-1]
        self.assertIsNone(m.transition(asset(),r,STAMP-900000,C))
    def test_open_reclaim_not_used(self):
        r=sample();self.assertIsNone(m.transition(asset(),r,STAMP-1,C))
    def test_bars_before_creation_cannot_create_historical_signal(self):
        a=asset();a['created_ms']=STAMP
        self.assertIsNone(m.transition(a,sample(),STAMP,C))
    def test_oi_missing_holds_pattern_then_can_confirm_same_closed_bar(self):
        a=asset();r=sample();r['derivatives'].update(ready=False,reasons=['oi_baseline_warming'])
        self.assertIsNone(m.transition(a,r,STAMP,C));r['derivatives'].update(ready=True,reasons=[])
        self.assertEqual(m.transition(a,r,STAMP+1000,C),'triggered')
    def test_btc_downtrend_blocks_entry_but_keeps_watch(self):
        a=asset();r=sample();r['context']['btc_long_blocked']=True
        self.assertIsNone(m.transition(a,r,STAMP,C));self.assertIn('btc_downtrend',a['entry_check']['reasons'])
    def test_unknown_overhead_is_not_two_r(self):
        r=sample();r['series']['4h'][40]['h']=101
        a=asset();self.assertIsNone(m.transition(a,r,STAMP,C));self.assertIn('overhead_unknown',a['entry_check']['reasons'])
    def test_future_unconfirmed_pivot_is_not_resistance(self):
        r=sample();r['series']['4h'][40]['h']=101;r['series']['4h'][-1]['h']=120
        self.assertIsNone(m.transition(asset(),r,STAMP,C))
    def test_costs_can_remove_apparent_two_r_room(self):
        r=sample();r['series']['4h'][40]['h']=104.3;a=asset()
        self.assertIsNone(m.transition(a,r,STAMP,C));self.assertIn('net_overhead_room_insufficient',a['entry_check']['reasons'])
    def test_extended_quote_does_not_trigger(self):
        r=sample();r['quote']['price']=103;self.assertIsNone(m.transition(asset(),r,STAMP,C))
    def test_missing_candles_still_allows_verified_support_loss(self):
        r=sample();r['series']={};r['quote']['price']=97
        self.assertEqual(m.transition(asset(),r,STAMP,C),'cancelled')
    def test_false_breakout_cancelled(self):
        r=sample();r['series']['15m'][-2]['c']=100
        self.assertEqual(m.transition(asset(),r,STAMP,C),'cancelled')
    def test_late_old_reclaim_not_triggered(self):
        self.assertIsNone(m.transition(asset(),sample(),STAMP+900001,C))
    def test_trigger_never_repeated(self):
        a=asset();r=sample();m.transition(a,r,STAMP,C)
        self.assertIsNone(m.transition(a,r,STAMP+1000,C))

class DataAndState(unittest.TestCase):
    def derivative(self,points=None,oi=None):
        return m.derivatives(market(),None,[market(STAMP-3600000,100)] if oi is None else oi,
            {} if points is None else points,{},C,STAMP)
    def test_short_unknown_is_explicit_not_required(self):
        d=self.derivative();self.assertTrue(d['ready']);self.assertEqual(d['short_information'],'unknown');self.assertFalse(d['strict_short_confirmed'])
    def test_oi_still_required(self):self.assertFalse(self.derivative(oi=[])['ready'])
    def test_negative_funding_not_fabricated(self):self.assertIsNone(self.derivative()['negative_funding'])
    def test_migration_preserves_entire_old_snapshot(self):
        old=__import__('coin5_model').new_state();old['pending']=[{'price':123,'observed_ms':456}]
        s=m.migrate(old,'sha',STAMP);self.assertEqual(s['previous_v1'],old)
        self.assertFalse(s['pending']);self.assertFalse(s['measurements']['cases'])
    def test_migration_rejects_unknown_rules(self):
        with self.assertRaises(ValueError):m.migrate({'rules_fingerprint':'bad'},'sha',STAMP)
    def test_silent_watch_created_before_oi_or_ratio_baseline(self):
        s=m.new_state();r=sample();r['quote']['price']=100;r['derivatives']['ready']=False
        r['preparation']={'valid':True,'level':101,'invalid':98,'atr':2}
        run.apply_records(s,{'MEXC':{'records':[r]}},C,STAMP)
        self.assertEqual(len(s['assets']),1);self.assertFalse(s['pending']);self.assertFalse(s['measurements']['cases'])
    def test_cross_venue_symbol_not_two_watches(self):
        s=m.new_state();r=sample();r['quote']['price']=100;r['preparation']={'valid':True,'level':101,'invalid':98,'atr':2}
        other=deepcopy(r);other['exchange']='OKX'
        run.apply_records(s,{'MEXC':{'records':[r]},'OKX':{'records':[other]}},C,STAMP)
        self.assertEqual(len(s['assets']),1)
    def test_stale_quote_cannot_cancel_or_create(self):
        s=m.new_state();s['assets']['a']=asset();r=sample();r['quote'].update(price=97,observed_ms=STAMP-180000)
        run.apply_records(s,{'MEXC':{'records':[r]}},C,STAMP);self.assertEqual(s['assets']['a']['phase'],'preparation')
    def test_duplicate_measurements_preserve_entry(self):
        s=m.new_state();a=asset();r=sample();m.transition(a,r,STAMP,C);m.register(s,a,r,STAMP)
        r['quote']['price']=111;m.register(s,a,r,STAMP+1000)
        self.assertEqual(s['measurements']['cases']['TESTUSDT']['entry_price'],101.8)
    def test_preparation_event_is_never_enqueued(self):
        s=m.new_state();m.enqueue(s,asset(),'preparation',sample(),STAMP);self.assertFalse(s['pending'])
    def test_notification_deduplicates_bot_receipt(self):
        s=m.new_state();a=asset();r=sample();m.transition(a,r,STAMP,C);s['assets']['a']=a;e=m.enqueue(s,a,'triggered',r,STAMP)
        with patch.object(run.oldrun,'settings',return_value=('https://api.github.com/repos/x/y/issues',{},'x')),patch.object(run.cloud,'http_json',return_value=[{'body':run.marker(e),'user':{'login':'github-actions[bot]'}}]):
            run.reconcile(s,'github_issue')
        self.assertFalse(s['pending']);self.assertEqual(len(s['delivery']),1)
    def test_notify_old_event_rejected(self):
        s=m.new_state();a=asset();r=sample();m.transition(a,r,STAMP,C);s['assets']['a']=a;e=m.enqueue(s,a,'triggered',r,STAMP)
        self.assertFalse(run.current(e,s,STAMP+120001,C))
    def test_cadence_distinguishes_session_gap(self):
        x=worker.cadence([{'started_ms':0,'session_id':'a'},{'started_ms':300000,'session_id':'a'},{'started_ms':1200000,'session_id':'b'}],C)
        self.assertEqual(x['within_session']['longest_minutes'],5);self.assertEqual(x['between_sessions']['over_10_minutes'],1)
    def test_full_universe_config_replaces_rotation(self):self.assertEqual(C['rotate_per_venue'],C['universe_per_venue'])

class Collection(unittest.TestCase):
    def collect(self,count=20):
        symbols=['X'+str(i)+'USDT' for i in range(count)]
        class Spot:
            blocked=False;calls=0
            def book(self,symbol,stamp):return {'price':100.,'spread_pct':.1,'observed_ms':STAMP}
        class Client:
            calls=0;blocked=False
            def read(self,*a):return {'status':'unknown','scope':'test','reason':'no data'}
        with patch.object(run.source,'Spot',return_value=Spot()),patch.object(run.futures,'Public',return_value=Client()),\
             patch.object(run.futures,'markets',return_value={k:market() for k in symbols}) as fresh,\
             patch.object(run.source,'universe',return_value=([{'symbol':k,'volume24':2e6} for k in symbols],{'bounded_universe':count})),\
             patch.object(run.source,'bars',side_effect=lambda client,sym,interval,*args:series()[interval]),\
             patch.object(run.futures,'funding',return_value=None),patch.object(run.ratios,'Client',return_value=Client()),\
             patch.object(run,'now_ms',return_value=STAMP):
            result=run.collect('MEXC',m.new_state(),C)
        return result,fresh.call_count
    def test_all_chart_symbols_examined_not_twelve_rotation(self):
        r,_=self.collect();self.assertEqual(r['coverage']['chart_evaluated'],20)
    def test_final_quotes_bounded_by_watch_slots(self):
        r,_=self.collect();self.assertEqual(len(r['records']),12)
    def test_oi_refreshed_after_candles_and_all_symbols_remembered(self):
        r,n=self.collect();self.assertEqual(n,2);self.assertEqual(len(r['oi_history']),20)
    def test_missing_ratios_do_not_fabricate_short_confirmation(self):
        r,_=self.collect();self.assertTrue(all(not x['derivatives']['strict_short_confirmed'] for x in r['records']))
    def test_first_real_oi_point_does_not_pass_growth(self):
        r,_=self.collect();self.assertTrue(all(not x['derivatives']['ready'] for x in r['records']))

class Barriers(unittest.TestCase):
    case={'observed_ms':60000,'entry_price':100,'stop':98,'target':105,'risk_pct':2}
    def rows(self,low=99,high=101):return {60000:{'open':100,'low':low,'high':high,'close':100}}
    def test_stop_first(self):self.assertEqual(measure.first_touch(self.case,self.rows(low=97),60000,120000)['status'],'stop_first')
    def test_target_first(self):self.assertEqual(measure.first_touch(self.case,self.rows(high=106),60000,120000)['status'],'target_first')
    def test_both_same_minute_ambiguous(self):self.assertEqual(measure.first_touch(self.case,self.rows(97,106),60000,120000)['status'],'ambiguous_same_minute')
    def test_gap_before_touch_unknown(self):self.assertEqual(measure.first_touch(self.case,{},60000,120000)['status'],'unknown_gap')
    def test_partial_entry_minute_is_not_counted_as_success(self):
        c={**self.case,'observed_ms':61000};self.assertEqual(measure.first_touch(c,self.rows(high=106),120000,120000)['status'],'unknown_entry_fragment')
    def test_gap_stop_uses_worse_open(self):
        rows=self.rows(low=96);rows[60000]['open']=97
        self.assertEqual(measure.first_touch(self.case,rows,60000,120000)['exit_price'],97)
    def test_neither_is_terminal_mark_not_target_hit(self):self.assertEqual(measure.first_touch(self.case,self.rows(),60000,120000)['status'],'neither')
    def test_hit_before_later_gap_keeps_known_order(self):
        self.assertEqual(measure.first_touch(self.case,self.rows(high=106),60000,180000)['status'],'target_first')

if __name__=='__main__':unittest.main()
