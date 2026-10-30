import unittest,json
from copy import deepcopy
from unittest.mock import patch
import coin5_v4_model as m
import coin5_v4_scan as run
import coin5_v4_measure as study
import coin5_v3_model as previous
import notification_style
from test_coin5_v3 import radar_row,entry_row,entry_asset,quote
from test_coin5 import candles,STAMP
C=m.config()

def market(row,venue,kind):
    r=deepcopy(row);q=quote(venue=venue,kind=kind,stamp=r['quote']['observed_ms'],last=r['quote']['price'])
    r.update(key=q['key'],group=venue+':'+kind,exchange=venue,kind=kind,quote=q)
    return r

def continuation_fixture():
    a=entry_asset();r=entry_row();bs=r['series']['15m']
    bs[-5].update(o=99.5,h=102.,l=99.4,c=101.8,v=400.)
    for b in bs[-4:-1]:b.update(o=102.1,h=102.7,l=102.,c=102.2,v=80.)
    bs[-1].update(o=102.6,h=103.1,l=102.5,c=103.,v=400.)
    r['quote']['price']=103.;r['context']['atr']=1.
    a.update(created_ms=STAMP-3600000+1000,level=100.,atr=1.,base_invalid=98.,invalid=98.,
        break_close_ms=STAMP-3600000,break_volume=400.)
    return a,r

def triggered():
    a,r=continuation_fixture();p=m.continuation(a,r,STAMP,C);m.enter(a,r,STAMP,'continuation',p,STAMP)
    a['radar']=deepcopy(r['radar']);a['initial_price']=100.;a['latest_price']=103.
    return a,r

def trend_fixture():
    a,r=triggered();a['first_triggered_ms']=STAMP-7200000;a['triggered_ms']=STAMP-7200000
    a['entry_history'][0]['observed_ms']=STAMP-7200000
    bs=r['series']['1h'];bs[-3].update(o=100,h=102,l=100,c=101)
    bs[-2].update(o=101,h=103,l=101,c=102)
    bs[-1].update(o=102,h=105,l=102,c=104)
    a['trend_floor']=99.;r['quote']['price']=104.
    return a,r

class IndependentMarkets(unittest.TestCase):
    def test_official_crypto_category_excludes_etfs_without_excluding_xrp(self):
        class Client:
            venue='OKX';kind='SPOT'
            def get(self,endpoint):
                if endpoint=='catalog':return [{'instId':b+'-USDT','baseCcy':b,'quoteCcy':'USDT','state':'live','instCategory':cat} for b,cat in [('XRP','1'),('XUVXY','3'),('XSOXS','3'),('UNKNOWN','')]]
                return [{'instId':b+'-USDT','bidPx':100.,'askPx':100.1,'last':100.,'ts':STAMP,'volCcy24h':1e6} for b in ('XRP','XUVXY','XSOXS','UNKNOWN')]
        with patch.object(run,'now_ms',return_value=STAMP):
            quotes,cov=run.snapshot(Client(),{'stable':[],'equity':{},'plates':[]},C,m.new_state(),'OKX:SPOT')
        self.assertEqual(list(quotes),['OKX:SPOT:XRPUSDT']);self.assertEqual(cov['instrument_categories']['3'],2)
    def test_active_quote_is_retained_when_discovery_liquidity_deteriorates(self):
        class Client:
            venue='OKX';kind='SPOT'
            def get(self,endpoint):
                if endpoint=='catalog':return [{'instId':'TEST-USDT','baseCcy':'TEST','quoteCcy':'USDT','state':'live','instCategory':'1'}]
                return [{'instId':'TEST-USDT','bidPx':100.,'askPx':101.,'last':100.,'ts':STAMP,'volCcy24h':1.}]
        s=m.new_state();s['assets']['a']={'key':'OKX:SPOT:TESTUSDT','group':'OKX:SPOT','phase':'triggered'}
        with patch.object(run,'now_ms',return_value=STAMP):q,cov=run.snapshot(Client(),{'stable':[],'equity':{},'plates':[]},C,s,'OKX:SPOT')
        self.assertIn('OKX:SPOT:TESTUSDT',q);self.assertEqual(cov['valid_liquid_tickers'],0);self.assertEqual(cov['active_quotes_retained_outside_discovery'],1)
    def test_four_markets_tracked_with_distinct_quotes_and_cases(self):
        s=m.new_state();rs=[market(radar_row(),v,k) for v in ('MEXC','OKX') for k in ('SPOT','PERP')]
        for i,r in enumerate(rs):r['quote']['price']+=i*.01
        run.apply_records(s,{'all':{'rows':rs}},C,STAMP)
        self.assertEqual(len(s['assets']),4);self.assertEqual(len(s['measurements']['cases']),4)
        self.assertEqual(len(s['radar_admissions']),1)
        self.assertEqual(len({c['entry_price'] for c in s['measurements']['cases'].values()}),4)
    def test_prior_venue_notification_does_not_block_okx_tracking(self):
        s=m.new_state();r=radar_row();run.apply_records(s,{'x':{'rows':[r]}},C,STAMP)
        for e in s['pending']:run.delivered(s,e,STAMP)
        s['pending']=[];other=market(r,'OKX','SPOT')
        run.apply_records(s,{'x':{'rows':[other]}},C,STAMP)
        self.assertEqual(len(s['assets']),2);self.assertFalse(s['pending']);self.assertEqual(len(s['suppressed']),1)
        self.assertEqual(len(s['delivery']),1) # Suppression is not a delivery receipt.
    def test_another_market_entry_is_not_suppressed_by_same_symbol(self):
        s=m.new_state();a=entry_asset();a.update(radar=deepcopy(radar_row()['radar']),initial_price=100,latest_price=100)
        a['id']='first';b=deepcopy(a);b.update(id='second',key='OKX:SPOT:TESTUSDT',group='OKX:SPOT',exchange='OKX')
        s['assets']={'first':a,'second':b};r=entry_row();other=market(r,'OKX','SPOT')
        run.apply_records(s,{'x':{'rows':[r,other]}},C,STAMP)
        self.assertEqual(sum(e['phase']=='triggered' for e in s['pending']),2)
    def test_duplicate_bar_still_idempotent(self):
        s=m.new_state();r=radar_row();run.apply_records(s,{'x':{'rows':[r]}},C,STAMP)
        run.apply_records(s,{'x':{'rows':[r]}},C,STAMP)
        self.assertEqual(len(s['assets']),1);self.assertEqual(len(s['pending']),1)
    def test_hourly_budget_counts_symbols_not_market_rows(self):
        s=m.new_state();s['radar_admissions']=[{'symbol':'X'+str(i),'observed_ms':STAMP} for i in range(6)]
        run.apply_records(s,{'x':{'rows':[radar_row()]}},C,STAMP)
        self.assertFalse(s['assets']);self.assertIn('hourly_symbol_budget',s['registration_decisions']['rejected'].values())
    def test_fresh_decisions_preserve_rejection_evidence(self):
        s=m.new_state();r=radar_row();r['quote']['price']=98
        run.apply_records(s,{'x':{'rows':[r]}},C,STAMP)
        self.assertEqual(s['registration_decisions']['rejected'][r['key']],'live_quote_lost_setup')

class StructuralRearm(unittest.TestCase):
    def state_row(self):
        s=m.new_state();r=radar_row();closed=STAMP-7200000
        s['last_closed'][r['key']]={'observed_ms':closed,'source_close_ms':closed-300000}
        return s,r
    def test_new_base_and_breakout_can_rearm_before_six_hours(self):
        s,r=self.state_row();self.assertIsNone(m.rearm_reason(s,r,STAMP,C))
        run.apply_records(s,{'x':{'rows':[r]}},C,STAMP);self.assertEqual(len(s['assets']),1)
    def test_base_must_start_after_actual_invalidation(self):
        s,r=self.state_row();s['last_closed'][r['key']]['observed_ms']=STAMP-2700000
        self.assertEqual(m.rearm_reason(s,r,STAMP,C),'rearm_base_not_fully_after_invalidation')
    def test_waiting_without_new_structure_is_not_enough(self):
        s,r=self.state_row();r['radar']['breakout']=False
        self.assertEqual(m.rearm_reason(s,r,STAMP,C),'rearm_new_breakout_missing')
    def test_wide_base_is_not_rearm(self):
        s,r=self.state_row();r['series']['15m'][-2]['h']=120
        self.assertEqual(m.rearm_reason(s,r,STAMP,C),'rearm_base_too_wide')

class EntryRoutes(unittest.TestCase):
    def test_original_retest_still_enters(self):
        a=entry_asset();self.assertEqual(m.transition(a,entry_row(),STAMP,C),'triggered')
        self.assertEqual(a['entry_route'],'retest');self.assertEqual(a['entry_seq'],1)
    def test_higher_base_can_enter_without_old_level_retest(self):
        a,r=continuation_fixture();self.assertEqual(m.transition(a,r,STAMP,C),'triggered')
        self.assertEqual(a['entry_route'],'continuation');self.assertEqual(a['trigger_price'],103.)
        self.assertNotIn('retest_close_ms',a)
    def test_only_two_base_candles_do_not_enter(self):
        a,r=continuation_fixture();r['series']['15m'][-4]['l']=99.4
        self.assertIsNone(m.continuation(a,r,STAMP,C))
    def test_open_future_breakout_is_not_confirmation(self):
        a,r=continuation_fixture();r['series']['15m'][-1]['t']=STAMP
        self.assertIsNone(m.continuation(a,r,STAMP,C))
    def test_weak_breakout_volume_is_not_confirmation(self):
        a,r=continuation_fixture();r['series']['15m'][-1]['v']=100
        self.assertIsNone(m.continuation(a,r,STAMP,C))
    def test_old_level_touch_belongs_to_retest_route(self):
        a,r=continuation_fixture();r['series']['15m'][-3]['l']=100.1
        self.assertIsNone(m.continuation(a,r,STAMP,C))
    def test_continuation_cannot_evade_btc_or_spread_or_price_guard(self):
        for what in ('btc','spread','extension','resistance','risk'):
            with self.subTest(what=what):
                a,r=continuation_fixture()
                if what=='btc':r['context']['btc_hour_pct']=-3.
                if what=='spread':r['quote']['spread_pct']=1.
                if what=='extension':r['quote']['price']=110.
                if what=='resistance':r['series']['4h'][30]['h']=103.5
                if what=='risk':r['quote']['price']=108.
                p=m.continuation(a,r,STAMP,C);self.assertTrue(p['reasons']);self.assertNotEqual(m.transition(a,r,STAMP,C),'triggered')
    def test_later_new_base_gives_distinct_related_entry(self):
        a,r=continuation_fixture();a['phase']='triggered';a['triggered_ms']=STAMP-7200000;a['first_triggered_ms']=STAMP-7200000
        a['entry_history']=[{'observed_ms':STAMP-7200000,'price':100.,'stop':98.,'source_close_ms':STAMP-7200000}]
        a['trigger_bar_close_ms']=STAMP-7200000;a['entry_seq']=1
        self.assertEqual(m.transition(a,r,STAMP,C),'triggered');self.assertEqual(a['entry_seq'],2)
        self.assertEqual(a['entry_history'][0]['price'],100.)
    def test_same_candle_never_creates_second_entry(self):
        a,r=triggered();self.assertIsNone(m.transition(a,r,STAMP+300000,C));self.assertEqual(a['entry_seq'],1)
    def test_new_entry_has_unique_event_and_frozen_old_case(self):
        s=m.new_state();a,r=triggered();run.register(s,a,'triggered',r,STAMP)
        old=deepcopy(s['measurements']['cases']);run.enqueue(s,a,'triggered',r,STAMP)
        p=deepcopy(a['entry_plan']);r['quote']['price']=104.
        m.enter(a,r,STAMP+3600000,'continuation',p,STAMP+3600000)
        run.register(s,a,'triggered',r,STAMP+3600000);run.enqueue(s,a,'triggered',r,STAMP+3600000)
        self.assertEqual(len(s['pending']),2);self.assertEqual(len(s['measurements']['cases']),2)
        self.assertTrue(all(s['measurements']['cases'][k]==v for k,v in old.items()))

class TrendAndNotification(unittest.TestCase):
    def test_unsent_entry_never_gets_trend_notifications_or_advanced_trend_state(self):
        s=m.new_state();a,r=trend_fixture();a['triggered_ms']=STAMP-1800000
        s['assets'][a['id']]=a;run.apply_records(s,{'x':{'rows':[r]}},C,STAMP)
        self.assertFalse(any(e['phase'].startswith('trend_') for e in s['pending']))
        self.assertNotIn('trend_evaluated_close_ms',a)
    def test_delivered_entry_receives_trend_update_without_new_entry(self):
        s=m.new_state();a,r=trend_fixture();a['triggered_ms']=STAMP-1800000
        s['assets'][a['id']]=a;s['delivery']=[{'id':'sent','asset_id':a['id'],'phase':'triggered','observed_ms':STAMP-7200000}]
        run.apply_records(s,{'x':{'rows':[r]}},C,STAMP)
        self.assertEqual([e['phase'] for e in s['pending']],['trend_continuing'])
        self.assertEqual(a['entry_seq'],1)
    def test_drop_in_entry_quote_generates_structure_loss_only_after_entry_receipt(self):
        s=m.new_state();a,r=triggered();s['assets'][a['id']]=a
        s['delivery']=[{'id':'sent','asset_id':a['id'],'phase':'triggered','observed_ms':STAMP}]
        r['quote']['price']=90.;run.apply_records(s,{'x':{'rows':[r]}},C,STAMP)
        self.assertTrue(s['pending'][0]['was_triggered']);self.assertIn('YAPI BOZULDU',run.describe(s['pending'][0]))
    def test_radar_only_never_has_trend_status(self):
        a,r=trend_fixture();a['phase']='radar';self.assertIsNone(m.trend_event(a,r,STAMP,C))
    def test_entry_then_later_hourly_strengthening(self):
        a,r=trend_fixture();self.assertEqual(m.trend_event(a,r,STAMP,C),'trend_continuing')
        self.assertEqual(a['trend_floor'],101.);self.assertIsNone(m.trend_event(a,r,STAMP+300000,C))
    def test_hourly_weakening_and_structure_break_are_separate(self):
        a,r=trend_fixture();r['series']['1h'][-1].update(o=101,h=102,l=98,c=99.5)
        self.assertEqual(m.trend_event(a,r,STAMP,C),'trend_weakening')
        a,r=trend_fixture();a['trend_floor']=102.;r['series']['1h'][-1].update(o=101,h=102,l=98,c=99.)
        self.assertEqual(m.trend_event(a,r,STAMP,C),'trend_broken')
    def test_bars_closing_before_entry_cannot_confirm_holding_trend(self):
        a,r=trend_fixture();a['first_triggered_ms']=STAMP+1;self.assertIsNone(m.trend_event(a,r,STAMP,C))
    def test_missing_or_stale_hourly_data_remains_unknown(self):
        a,r=trend_fixture();r['series']['1h']=[];self.assertIsNone(m.trend_event(a,r,STAMP,C))
        a,r=trend_fixture();self.assertIsNone(m.trend_event(a,r,STAMP+3600000,C))
    def test_trend_does_not_rewrite_original_entry_measurement(self):
        s=m.new_state();a,r=trend_fixture();run.register(s,a,'triggered',r,STAMP-7200000)
        old=deepcopy(s['measurements']['cases']);m.trend_event(a,r,STAMP,C)
        self.assertEqual(old,s['measurements']['cases'])
    def test_both_entry_routes_keep_green_confirmation_icon(self):
        for route in ('retest','continuation'):
            s=m.new_state();a,r=triggered();a['entry_route']=route;run.enqueue(s,a,'triggered',r,STAMP)
            p=notification_style.style({'title':'Coin Tarama5 V4','body':run.describe(s['pending'][0])})
            self.assertTrue(p['title'].startswith('🟢🎯'));self.assertIn('GİRİŞ TEYİDİ',p['body'])
    def test_trend_notification_is_never_promoted_to_entry(self):
        s=m.new_state();a,r=trend_fixture();phase=m.trend_event(a,r,STAMP,C);run.enqueue(s,a,phase,r,STAMP)
        p=notification_style.style({'title':'Coin Tarama5 V4','body':run.describe(s['pending'][0])})
        self.assertFalse(p['title'].startswith('🟢🎯'));self.assertIn('yeni giriş teyidi değildir',p['body'])

class PreservationAndStudy(unittest.TestCase):
    def test_approved_text_fix_retains_all_live_references(self):
        import coin5_v4_worker as worker
        s=m.new_state();s['rules_fingerprint']='9827746f05ad8df4bb7eaaebdfc768271ebd9fa18381eeaf5d93cc564abef469'
        s['assets']={'a':{'initial_price':.0013615,'created_ms':STAMP}}
        s['measurements']['cases']={'x':{'entry_price':123.,'stop':120.,'outcomes':{}}}
        s['delivery']=[{'id':'already-sent'}];old=deepcopy(s)
        worker.validate_state(s)
        for k in ('assets','measurements','delivery','pending','runs'):self.assertEqual(old[k],s[k])
        self.assertEqual(s['rules_fingerprint'],m.fingerprint());self.assertEqual(len(s['presentation_migrations']),1)
        worker.validate_state(s);self.assertEqual(len(s['presentation_migrations']),1)
    def test_unapproved_changed_state_is_not_migrated(self):
        import coin5_v4_worker as worker
        s=m.new_state();s['rules_fingerprint']='unapproved'
        with self.assertRaises(ValueError):worker.validate_state(s)
    def test_migration_preserves_legacy_and_does_not_replay_messages(self):
        old=previous.new_state();old['assets']={'a':{'key':'OKX:SPOT:SOPHUSDT','radar':{'bar_close_ms':STAMP}}}
        old['measurements']['cases']={'x':{'entry_price':.00123}};old['delivery']=[{'id':'sent'}];old['pending']=[{'id':'unsent'}]
        before=deepcopy(old);s=m.migrate(old,'sha',STAMP)
        self.assertEqual(s['legacy_v3']['measurements'],old['measurements']);self.assertEqual(s['legacy_v3']['pending'],old['pending'])
        self.assertFalse(s['assets']);self.assertFalse(s['delivery']);self.assertFalse(s['pending']);self.assertEqual(before,old)
        self.assertEqual(s['prior_signal_bars']['OKX:SPOT:SOPHUSDT'],[STAMP])
    def test_wrong_archive_rules_fail_closed(self):
        old=previous.new_state();old['rules_fingerprint']='wrong'
        with self.assertRaises(ValueError):m.migrate(old,'sha',STAMP)
    def test_measurements_summary_does_not_count_four_markets_as_four_coins(self):
        s=m.new_state();rs=[market(radar_row(),v,k) for v in ('MEXC','OKX') for k in ('SPOT','PERP')]
        run.apply_records(s,{'x':{'rows':rs}},C,STAMP);study.measure(s,C,STAMP+1000)
        self.assertEqual(s['measurements']['summary']['radar']['unique_symbol_labels'],1)
        self.assertEqual(s['measurements']['summary']['radar']['market_event_references'],4)
        self.assertEqual(len(s['measurements']['summary']['radar']['groups']),4)

if __name__=='__main__':unittest.main()
