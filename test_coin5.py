import unittest,json,tempfile
from pathlib import Path
from copy import deepcopy
from unittest.mock import patch
from urllib.error import HTTPError
import coin5_model as m
import coin5_sources as s
import coin5_scan as run
from short_squeeze_positions import SCOPES

CFG=m.config();STAMP=900000*2000

def candles(count=80,step=900000):
    end=STAMP//step*step
    return [{'t':end-(count-i)*step,'o':100.,'h':101.,'l':99.,'c':100.,'v':100.} for i in range(count)]
def series():return {k:candles(step=v) for k,v in s.STEPS.items()}
def market(stamp=STAMP,oi=110):return {'observed_ms':stamp,'contract':'TEST_USDT','contract_size':1,'oi_contracts':oi,'mid_price':100.,'oi_notional':2e6,'spread_pct':.1}
def point(provider='OKX',stamp=STAMP,short=60):
    return {'status':'observed','scope':SCOPES[provider],'symbol':'TESTUSDT','provider_ms':stamp,'short_pct':short,'long_pct':100-short,'provider':provider}
def asset():return {'id':'a','symbol':'TESTUSDT','exchange':'MEXC','phase':'preparation','created_ms':STAMP-900000,'level':101.,'invalid':98.,'atr':2.}
def row():
    bars=series();bars['15m'][-1].update(o=100.,h=102.,l=100.,c=101.8,v=200.)
    return {'symbol':'TESTUSDT','exchange':'MEXC','quote':{'price':101.9,'spread_pct':.1,'observed_ms':STAMP},
            'series':bars,'context':{'reasons':[],'atr':2.},'derivatives':{'ready':True,'reasons':[],'profiles':{},'score':2},
            'preparation':{'valid':False},'book_reasons':[],'btc_quote':{'price':1000.},'observed_ms':STAMP,'volume24':2e6}

class Bars(unittest.TestCase):
    def raw(self,venue='MEXC'):
        return [[b['t'],b['o'],b['h'],b['l'],b['c'],2,b['t']+900000,123]+(['1'] if venue=='OKX' else []) for b in candles(5)]
    def test_open_candle_never_positive(self):
        raw=self.raw();raw.append([STAMP,100,1000,1,900,10,STAMP+900000,100])
        self.assertEqual(s.closed_bars(raw,'MEXC','15m',STAMP,5)[-1]['c'],100)
    def test_okx_confirmation_and_quote_volume(self):
        raw=self.raw('OKX');raw.append([STAMP,100,110,90,105,2,3,4,'0'])
        self.assertEqual(s.closed_bars(raw,'OKX','15m',STAMP,5)[-1]['v'],123)
    def test_gap_rejected(self):
        raw=self.raw();raw.pop(2)
        with self.assertRaises(ValueError):s.closed_bars(raw,'MEXC','15m',STAMP,4)
    def test_stale_rejected(self):
        with self.assertRaises(ValueError):s.closed_bars(self.raw(),'MEXC','15m',STAMP+900000,5)
    def test_conflicting_duplicate_rejected(self):
        raw=self.raw();x=deepcopy(raw[0]);x[4]=100.5;raw.append(x)
        with self.assertRaises(ValueError):s.closed_bars(raw,'MEXC','15m',STAMP,5)
    def test_cache_only_same_closed_cutoff(self):
        c=s.Spot('MEXC');cache={};cfg={**CFG,'bars_per_timeframe':5}
        with patch.object(c,'get',return_value=self.raw()) as get:
            s.bars(c,'TESTUSDT','15m',STAMP,cfg,cache);s.bars(c,'TESTUSDT','15m',STAMP+1000,cfg,cache)
            self.assertEqual(get.call_count,1)
    def test_no_private_endpoints(self):
        with self.assertRaises(ValueError):s.Spot('MEXC').get('order')
    def test_access_rejection_stops_requests(self):
        c=s.Spot('MEXC')
        with patch.object(c.opener,'open',side_effect=HTTPError('',451,'blocked',{},None)) as op:
            with self.assertRaises(RuntimeError):c.get('catalog')
            with self.assertRaises(RuntimeError):c.get('catalog')
            self.assertEqual(op.call_count,1)
    def test_mexc_hour_wire_code(self):
        c=s.Spot('MEXC')
        response=__import__('io').BytesIO(b'[]')
        with patch.object(c.opener,'open',return_value=response) as op:
            c.get('candles','TESTUSDT','1h');self.assertIn('interval=60m',op.call_args.args[0].full_url)

class Factors(unittest.TestCase):
    def evaluate(self,**kw):
        return m.derivative_context(kw.get('market',market()),kw.get('funding',{'scaled_8h_rate':.001,'observed_ms':STAMP}),
            kw.get('oi',[market(STAMP-3600000,100)]),kw.get('points',{'OKX':point()}),
            kw.get('history',{'OKX':[point(stamp=STAMP-3600000,short=55)]}),CFG,STAMP)
    def test_positive_funding_not_gate(self):
        d=self.evaluate();self.assertTrue(d['ready']);self.assertFalse(d['negative_funding'])
    def test_funding_unknown_does_not_become_negative(self):
        d=self.evaluate(funding=None);self.assertTrue(d['ready']);self.assertIsNone(d['negative_funding'])
    def test_missing_ratio_not_pass(self):self.assertFalse(self.evaluate(points={})['ready'])
    def test_future_ratio_not_pass(self):self.assertFalse(self.evaluate(points={'OKX':point(stamp=STAMP+300000)})['ready'])
    def test_old_ratio_not_pass(self):self.assertFalse(self.evaluate(points={'OKX':point(stamp=STAMP-1200000)})['ready'])
    def test_oi_only_same_identity(self):
        old=market(STAMP-3600000,100);old['contract_size']=1000
        self.assertIn('oi_identity_changed',self.evaluate(oi=[old])['reasons'])
    def test_no_historical_baseline_fabricated(self):self.assertIn('oi_baseline_warming',self.evaluate(oi=[])['reasons'])
    def test_short_must_increase_not_just_large(self):
        self.assertFalse(self.evaluate(history={'OKX':[point(stamp=STAMP-3600000,short=62)]})['ready'])
    def test_population_conflict_is_visible_not_averaged(self):
        d=self.evaluate(points={'OKX':point(),'BINANCE':point('BINANCE',short=40)},history={
            'OKX':[point(stamp=STAMP-3600000,short=55)],'BINANCE':[point('BINANCE',STAMP-3600000,45)]})
        self.assertTrue(d['ready']);self.assertEqual(d['supporting_sources'],['OKX']);self.assertEqual(d['opposing_sources'],['BINANCE'])
    def test_revisions_cannot_rewrite_old_ratio(self):
        h=[];m.remember(h,point(),'provider_ms',STAMP);m.remember(h,point(short=90),'provider_ms',STAMP)
        self.assertEqual(len(h),1);self.assertEqual(h[0]['short_pct'],60)
    def test_context_and_setup_with_closed_series(self):
        x=series();c=m.context(x,x['1h'],CFG);p=m.preparation(x,c,CFG)
        self.assertTrue(p['valid']);self.assertEqual(p['level'],101)

class Lifecycle(unittest.TestCase):
    def test_preparation_cannot_backdate_trigger(self):
        a=asset();a['created_ms']=STAMP
        self.assertIsNone(m.transition(a,row(),STAMP,CFG))
    def test_breakout_trigger_uses_current_quote(self):
        a=asset();r=row();self.assertEqual(m.transition(a,r,STAMP,CFG),'triggered');self.assertEqual(a['trigger_price'],101.9)
    def test_missing_derivative_holds_preparation(self):
        a=asset();r=row();r['derivatives']['ready']=False
        self.assertIsNone(m.transition(a,r,STAMP,CFG));self.assertEqual(a['phase'],'preparation')
    def test_quote_below_invalid_cancels_with_missing_candles(self):
        a=asset();r=row();r['series']={};r['quote']['price']=97
        self.assertEqual(m.transition(a,r,STAMP,CFG),'cancelled')
    def test_no_repeat_same_closed_bar(self):
        a=asset();r=row();r['derivatives']['ready']=False;m.transition(a,r,STAMP,CFG);r['derivatives']['ready']=True
        self.assertIsNone(m.transition(a,r,STAMP+1000,CFG))
    def test_known_close_overhead_rejects_trigger(self):
        a=asset();r=row();r['series']['4h'][-1]['h']=102
        self.assertIsNone(m.transition(a,r,STAMP,CFG))
    def test_frozen_level_never_moves(self):
        a=asset();r=row();r['derivatives']['ready']=False;m.transition(a,r,STAMP,CFG)
        self.assertEqual((a['level'],a['invalid']),(101,98))
    def test_extended_current_quote_rejects(self):
        a=asset();r=row();r['quote']['price']=110
        self.assertIsNone(m.transition(a,r,STAMP,CFG))
    def test_expiry_not_called_support_loss(self):
        a=asset();r=row();a['created_ms']=STAMP-7*3600000
        self.assertEqual(m.transition(a,r,STAMP,CFG),'expired')
    def test_successful_retest_uses_later_closed_bar(self):
        a=asset();a.update(break_close_ms=STAMP-900000,break_volume=300)
        r=row();r['series']['15m'][-1].update(l=101,c=101.4,h=101.8,o=101.1,v=90);r['quote']['price']=101.5
        self.assertEqual(m.transition(a,r,STAMP,CFG),'triggered');self.assertEqual(a['trigger_kind'],'geri test')

class StateAndMessages(unittest.TestCase):
    def test_new_state_isolated(self):self.assertEqual(m.new_state()['assets'],{})
    def test_single_global_coin_and_actual_measurement(self):
        state=m.new_state();r=row();r['quote']['price']=100.;r['preparation']={'valid':True,'level':101,'invalid':98,'atr':2}
        other=deepcopy(r);other['exchange']='OKX';other['quote']['spread_pct']=.2
        run.apply_records(state,{'MEXC':{'records':[r]},'OKX':{'records':[other]}},CFG,STAMP)
        self.assertEqual(len(state['assets']),1);self.assertEqual(len(state['pending']),1)
        case=state['measurements']['cases']['TESTUSDT:preparation'];self.assertEqual(case['entry_price'],100);self.assertEqual(case['observed_ms'],STAMP)
    def test_phase_measurements_do_not_reprice(self):
        state=m.new_state();r=row();a=asset();m.register_measurement(state,a,'preparation',r,STAMP)
        r['quote']['price']=110;m.register_measurement(state,a,'preparation',r,STAMP+10000)
        self.assertEqual(state['measurements']['cases']['TESTUSDT:preparation']['entry_price'],101.9)
    def test_stale_quote_does_not_create_or_invalidate(self):
        state=m.new_state();a=asset();state['assets']['a']=a;r=row();r['quote']['price']=90;r['quote']['observed_ms']=STAMP-180000
        run.apply_records(state,{'MEXC':{'records':[r]}},CFG,STAMP)
        self.assertEqual(a['phase'],'preparation');self.assertFalse(state['pending'])
    def test_event_deduplication(self):
        state=m.new_state();a=asset();r=row();m.enqueue(state,a,'preparation',r,STAMP);m.enqueue(state,a,'preparation',r,STAMP)
        self.assertEqual(len(state['pending']),1)
    def test_obsolete_preparation_not_sent_after_trigger(self):
        state=m.new_state();a=asset();state['assets']['a']=a;e=m.enqueue(state,a,'preparation',row(),STAMP);a['phase']='triggered'
        self.assertFalse(run.event_current(e,state,STAMP,CFG))
    def test_cancellation_only_if_candidate_was_delivered(self):
        state=m.new_state();a=asset();a['phase']='cancelled';state['assets']['a']=a;e=m.enqueue(state,a,'cancelled',row(),STAMP)
        self.assertFalse(run.event_current(e,state,STAMP,CFG));state['delivery']=[{'id':'old','asset_id':'a','phase':'preparation'}]
        self.assertTrue(run.event_current(e,state,STAMP,CFG))
    def test_retry_marker_reconciles_without_sending(self):
        state=m.new_state();e=m.enqueue(state,asset(),'preparation',row(),STAMP)
        with patch.object(run,'settings',return_value=('https://api.github.com/repos/test/repo/issues',{},'test')),patch.object(run.cloud,'http_json',return_value=[{'body':run.marker(e),'user':{'login':'github-actions[bot]'}}]):
            run.reconcile(state,'github_issue')
        self.assertFalse(state['pending']);self.assertEqual(len(state['delivery']),1)
    def test_old_state_branch_forbidden(self):
        with patch.dict('os.environ',{'SCANNER_STATE_BRANCH':'scanner-state-shortcu-kistir'}):
            with self.assertRaises(ValueError):run.configure()

if __name__=='__main__':unittest.main()
