import unittest,json
from copy import deepcopy
from unittest.mock import patch
import coin5_v3_model as m
import coin5_v3_sources as s
import coin5_v3_scan as run
import coin5_v3_measure as study
from test_coin5 import candles,STAMP
C=m.config();EX={'stable':[],'equity':{},'plates':[]}
def quote(sym='TESTUSDT',venue='MEXC',kind='SPOT',stamp=STAMP,last=101.8):
    contract=sym if kind=='SPOT' and venue=='MEXC' else sym[:-4]+'_USDT' if venue=='MEXC' else sym[:-4]+'-USDT'+('-SWAP' if kind=='PERP' else '')
    return {'symbol':sym,'venue':venue,'kind':kind,'contract':contract,'key':venue+':'+kind+':'+sym,
        'bid':last-.01,'ask':last+.01,'price':last,'last':last,'spread_pct':.1,'volume24':1000000,'return24_pct':0.,
        'observed_ms':stamp,'provider_ms':stamp,'oi_contracts':None,'funding_raw':None}
def series():return {'15m':candles(64),'1h':candles(64,3600000),'4h':candles(64,14400000)}
def radar_row():
    bs=series();bs['15m'][-1].update(o=100,h=102,l=100,c=101.8,v=400)
    q=quote();return {'key':q['key'],'group':'MEXC:SPOT','symbol':q['symbol'],'exchange':'MEXC','kind':'SPOT','quote':q,
        'series':bs,'radar':m.radar(bs['15m'],C),'context':{'atr':2.,'btc_hour_pct':0.,'support_warnings':['4s zayıf']},'btc_quote':quote('BTCUSDT',last=1000),'book_reasons':[]}
def entry_asset():
    return {'id':'a','key':'MEXC:SPOT:TESTUSDT','group':'MEXC:SPOT','symbol':'TESTUSDT','exchange':'MEXC','kind':'SPOT',
        'contract':'TESTUSDT','phase':'radar','created_ms':STAMP-1800000+1000,'level':101.,'base_invalid':98.,'invalid':98.,
        'atr':2.,'break_close_ms':STAMP-1800000,'break_volume':400,'radar':{'bar_close_ms':STAMP-1800000}}
def entry_row():
    r=radar_row();r['series']['15m'][-2].update(o=101.1,h=101.5,l=100.9,c=101.3,v=90)
    r['series']['15m'][-1].update(o=101.3,h=102.2,l=101.2,c=102.,v=140)
    r['quote']['price']=102.1;return r

class MarketData(unittest.TestCase):
    def test_spot_listing_needs_no_perpetual(self):
        raw={'symbols':[{'symbol':'LSKUSDT','baseAsset':'LSK','quoteAsset':'USDT','status':'1'}]}
        self.assertIn('LSKUSDT',s.metadata(raw,'MEXC','SPOT',EX))
    def test_okx_spot_stands_alone(self):
        raw=[{'instId':'LSK-USDT','baseCcy':'LSK','quoteCcy':'USDT','state':'live'}]
        self.assertIn('LSKUSDT',s.metadata(raw,'OKX','SPOT',EX))
    def test_perp_stands_alone(self):
        raw=[{'symbol':'LSK_USDT','baseCoin':'LSK','quoteCoin':'USDT','settleCoin':'USDT','state':0,'futureType':1,'contractSize':1}]
        self.assertIn('LSKUSDT',s.metadata(raw,'MEXC','PERP',EX))
    def test_tradfi_perpetual_excluded_by_type(self):
        raw=[{'symbol':'SQQQ_USDT','baseCoin':'SQQQ','quoteCoin':'USDT','settleCoin':'USDT','state':0,'futureType':1,'contractSize':.1,'type':2}]
        self.assertFalse(s.metadata(raw,'MEXC','PERP',EX))
    def test_tradfi_tag_excluded_without_type(self):
        raw=[{'symbol':'SQQQ_USDT','baseCoin':'SQQQ','quoteCoin':'USDT','settleCoin':'USDT','state':0,'futureType':1,'contractSize':.1,'conceptPlate':['mc-trade-zone-ETF']}]
        self.assertFalse(s.metadata(raw,'MEXC','PERP',EX))
    def test_identity_mismatch_rejected(self):
        with self.assertRaises(ValueError):s.ticker({'symbol':'OTHERUSDT'},quote(),'MEXC','SPOT',STAMP)
    def test_future_provider_time_rejected(self):
        raw={'instId':'TEST-USDT','bidPx':100,'askPx':101,'last':100,'ts':STAMP+1,'volCcy24h':1000}
        with self.assertRaises(ValueError):s.ticker(raw,quote(venue='OKX'),'OKX','SPOT',STAMP)
    def test_no_oi_needed_for_spot_ticker(self):
        raw={'symbol':'TESTUSDT','bidPrice':100,'askPrice':100.1,'lastPrice':100,'quoteVolume':2e6,'priceChangePercent':5}
        q=s.ticker(raw,{'contract':'TESTUSDT','symbol':'TESTUSDT'},'MEXC','SPOT',STAMP)
        self.assertEqual(q['volume24'],2e6);self.assertIsNone(q['oi_contracts'])
    def test_okx_quote_turnover_not_multiplied_again(self):
        raw={'instId':'TEST-USDT','bidPx':100,'askPx':101,'last':100,'ts':STAMP,'volCcy24h':1000}
        q=s.ticker(raw,{'contract':'TEST-USDT','symbol':'TESTUSDT'},'OKX','SPOT',STAMP)
        self.assertEqual(q['volume24'],1000)
    def test_candles_preserve_quote_volume(self):
        raw=[[b['t'],b['o'],b['h'],b['l'],b['c'],2,0,123] for b in candles(4)]
        self.assertEqual(s.candles(raw,'MEXC','SPOT','15m',STAMP,4)[-1]['v'],123)
    def test_open_bar_not_used(self):
        raw=[[b['t'],b['o'],b['h'],b['l'],b['c'],2,0,123] for b in candles(4)]+[[STAMP,1,1000,1,900,10,0,1e9]]
        self.assertEqual(s.candles(raw,'MEXC','SPOT','15m',STAMP,4)[-1]['c'],100)
    def test_okx_unconfirmed_bar_ignored(self):
        raw=[[b['t'],b['o'],b['h'],b['l'],b['c'],2,3,4,'1'] for b in candles(4)]
        raw.append([STAMP,1,1000,1,900,2,3,4,'0'])
        self.assertEqual(len(s.candles(raw,'OKX','SPOT','15m',STAMP,4)),4)
    def test_gap_rejected(self):
        raw=[[b['t'],100,101,99,100,2,0,123] for b in candles(4)];raw.pop(1)
        with self.assertRaises(ValueError):s.candles(raw,'MEXC','SPOT','15m',STAMP,3)
    def test_mexc_contract_array_amount_is_used(self):
        bs=candles(4);raw={'time':[b['t']//1000 for b in bs],'open':[100]*4,'high':[101]*4,'low':[99]*4,'close':[100]*4,'amount':[456]*4,'vol':[999]*4}
        self.assertEqual(s.candles(raw,'MEXC','PERP','15m',STAMP,4)[-1]['v'],456)
    def test_contract_array_length_mismatch_rejected(self):
        with self.assertRaises(ValueError):s.candles({'time':[0],'open':[]},'MEXC','PERP','15m',STAMP,1)
    def test_private_endpoint_forbidden(self):
        with self.assertRaises(ValueError):s.Public('MEXC','PERP').get('order')

class Discovery(unittest.TestCase):
    def test_low_daily_volume_rank_can_win_real_short_momentum(self):
        st=m.new_state();qs={}
        for i in range(100):
            q=quote('X'+str(i)+'USDT');q['last']=100.;q['volume24']=1e8;qs[q['key']]=q
        q=quote('NEWUSDT',last=104);q['volume24']=100001;qs[q['key']]=q
        st['quote_history'][q['key']]=[{'observed_ms':STAMP-300000,'last':100,'volume24':100001}]
        self.assertIn(q['key'],m.select(qs,st,'MEXC:SPOT',C,STAMP))
    def test_no_baseline_is_unknown_not_fake_five_minute_return(self):
        self.assertIsNone(m.priority(quote(),[],STAMP)['change5m_pct'])
    def test_rolling_turnover_not_named_buy_volume(self):
        p=m.priority(quote(),[],STAMP);self.assertIn('not five-minute',p['turnover_note'])
    def test_rotation_reaches_non_priority_symbols(self):
        st=m.new_state();qs={q['key']:q for q in [quote('X'+str(i)+'USDT') for i in range(80)]}
        one=set(m.select(qs,st,'MEXC:SPOT',C,STAMP));two=set(m.select(qs,st,'MEXC:SPOT',C,STAMP))
        self.assertTrue(two-one)
    def test_quote_history_keeps_actual_market_identity(self):
        st=m.new_state();a=quote();b=quote(kind='PERP');m.remember_quotes(st,{a['key']:a,b['key']:b},STAMP)
        self.assertEqual(len(st['quote_history']),2)
    def test_missing_oi_does_not_create_support(self):
        self.assertEqual(m.oi_support(quote(),[])['status'],'unknown_or_not_applicable')
    def test_oi_change_only_same_contract_size(self):
        q=quote(kind='PERP');q.update(oi_contracts=110,contract_size=1)
        old={'provider_ms':STAMP-3600000,'oi_contracts':100,'contract':q['contract'],'contract_size':10}
        self.assertEqual(m.oi_support(q,[old])['status'],'warming')

class RadarAndEntry(unittest.TestCase):
    def test_volume_breakout_gives_radar_not_entry(self):self.assertTrue(radar_row()['radar']['valid'])
    def test_early_turn_can_precede_old_range_top(self):
        r=radar_row();r['series']['15m'][-8]['h']=108
        self.assertTrue(m.radar(r['series']['15m'],C)['valid'])
    def test_weak_4h_is_warning_not_radar_veto(self):
        r=radar_row();self.assertTrue(r['radar']['valid']);self.assertIn('4s zayıf',r['context']['support_warnings'])
    def test_late_pump_not_relabelled_early(self):
        bs=radar_row()['series']['15m'];bs[-1].update(h=132,c=130)
        self.assertIn('already_extended',m.radar(bs,C)['reasons'])
    def test_future_retest_reclaim_enters_even_without_oi(self):
        a=entry_asset();r=entry_row();self.assertEqual(m.transition(a,r,STAMP,C),'triggered')
        self.assertEqual(a['trigger_price'],102.1)
    def test_unknown_resistance_is_explicit_projection(self):
        a=entry_asset();m.transition(a,entry_row(),STAMP,C)
        self.assertEqual(a['entry_plan']['target_kind'],'projected_2R_resistance_unknown')
    def test_known_nearby_resistance_blocks_entry(self):
        r=entry_row();r['series']['4h'][30]['h']=103;a=entry_asset()
        self.assertIsNone(m.transition(a,r,STAMP,C));self.assertIn('known_resistance_blocks_target',a['entry_check']['reasons'])
    def test_first_closed_breakout_never_claimed_entry(self):
        a=entry_asset();a['created_ms']=STAMP
        self.assertIsNone(m.transition(a,entry_row(),STAMP,C))
    def test_btc_shock_blocks_entry(self):
        r=entry_row();r['context']['btc_hour_pct']=-3
        self.assertIsNone(m.transition(entry_asset(),r,STAMP,C))
    def test_btc_unknown_blocks_entry_not_radar(self):
        r=entry_row();r['context']['btc_hour_pct']=None
        self.assertIsNone(m.transition(entry_asset(),r,STAMP,C));self.assertTrue(r['radar']['valid'])
    def test_entry_risk_limit(self):
        r=entry_row();a=entry_asset();a.update(retest_close_ms=STAMP-900000,retest_low=95,retest_high=101.5)
        self.assertIsNone(m.transition(a,r,STAMP,C))
    def test_extended_live_quote_rejected(self):
        r=entry_row();r['quote']['price']=110
        self.assertIsNone(m.transition(entry_asset(),r,STAMP,C))
    def test_later_support_loss_cancels(self):
        r=entry_row();r['quote']['price']=97
        self.assertEqual(m.transition(entry_asset(),r,STAMP,C),'cancelled')

class StateNotificationsAndMeasurement(unittest.TestCase):
    def test_actual_observation_reference_not_candle_close(self):
        st=m.new_state();r=radar_row();r['quote']['price']=101.9
        run.apply_records(st,{'x':{'rows':[r]}},C,STAMP)
        self.assertEqual(st['measurements']['cases']['TESTUSDT:radar']['entry_price'],101.9)
        self.assertEqual(st['pending'][0]['phase'],'radar')
    def test_same_symbol_not_repeated_across_markets(self):
        st=m.new_state();r=radar_row();run.apply_records(st,{'x':{'rows':[r]}},C,STAMP)
        other=deepcopy(r);other['key']='OKX:PERP:TESTUSDT';other['group']='OKX:PERP';other['exchange']='OKX';other['kind']='PERP'
        run.apply_records(st,{'x':{'rows':[other]}},C,STAMP)
        self.assertEqual(len(st['assets']),1);self.assertEqual(len(st['pending']),1)
    def test_dump_after_signal_candle_does_not_create_new_radar(self):
        st=m.new_state();r=radar_row();r['quote']['price']=98
        run.apply_records(st,{'x':{'rows':[r]}},C,STAMP)
        self.assertFalse(st['assets']);self.assertFalse(st['pending'])
    def test_lost_breakout_after_close_is_not_new_radar(self):
        st=m.new_state();r=radar_row();r['quote']['price']=100.1
        run.apply_records(st,{'x':{'rows':[r]}},C,STAMP)
        self.assertFalse(st['pending'])
    def test_old_reference_never_repriced(self):
        st=m.new_state();r=radar_row();run.apply_records(st,{'x':{'rows':[r]}},C,STAMP)
        a=next(iter(st['assets'].values()));r['quote']['price']=110;run.register(st,a,'radar',r,STAMP+1000)
        self.assertEqual(st['measurements']['cases']['TESTUSDT:radar']['entry_price'],101.8)
    def test_hourly_notification_budget(self):
        st=m.new_state();st['delivery']=[{'phase':'radar','observed_ms':STAMP-i} for i in range(6)]
        run.apply_records(st,{'x':{'rows':[radar_row()]}},C,STAMP);self.assertFalse(st['pending'])
    def test_migration_archives_all_old_trade_records(self):
        old={'version':'coin-tarama-5-v2','rules_fingerprint':m.previous_fingerprint(),'assets':{'a':{'price':123}},'measurements':{'cases':{'x':{}}},'delivery':[],'pending':[]}
        st=m.migrate(old,'sha',STAMP);self.assertEqual(st['archive']['old_records']['assets'],old['assets']);self.assertFalse(st['assets'])
    def test_wrong_source_version_rejected(self):
        with self.assertRaises(ValueError):m.migrate({'version':'bad'},'sha',STAMP)
    def test_radar_message_explicitly_not_entry(self):
        st=m.new_state();r=radar_row();run.apply_records(st,{'x':{'rows':[r]}},C,STAMP)
        self.assertIn('giriş teyidi henüz yok',run.describe(st['pending'][0]))
    def test_spot_and_perp_outcomes_use_own_source(self):
        calls=[]
        def fake(client,contract,start,end,stamp):
            calls.append((client.kind,contract));return {t:{'t':t,'o':100,'h':101,'l':99,'c':100,'v':1} for t in range(start,end,60000)}
        st=m.new_state();r=radar_row();r['kind']='PERP';r['quote'].update(kind='PERP',contract='TEST_USDT');r['key']='MEXC:PERP:TESTUSDT';r['group']='MEXC:PERP'
        run.apply_records(st,{'x':{'rows':[r]}},C,STAMP)
        study.measure(st,C,STAMP+3600000,fake)
        self.assertTrue(any(k=='PERP' and c=='TEST_USDT' for k,c in calls));self.assertTrue(all(k=='PERP' for k,c in calls))
        self.assertEqual(st['measurements']['cases']['TESTUSDT:radar']['outcomes']['1']['barriers']['status'],'not_a_trade_entry')
    def test_no_network_for_not_yet_due_measurement(self):
        st=m.new_state();r=radar_row();run.apply_records(st,{'x':{'rows':[r]}},C,STAMP)
        with patch.object(study,'fetch_range',side_effect=AssertionError('network')):
            study.measure(st,C,STAMP+1000,lambda *args:(_ for _ in ()).throw(AssertionError('network')))
        self.assertFalse(st['measurements']['errors'])

if __name__=='__main__':unittest.main()
