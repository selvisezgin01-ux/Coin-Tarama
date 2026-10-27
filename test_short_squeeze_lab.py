from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch,Mock
import json,unittest
import short_squeeze_lab as lab
import short_squeeze as prod
import short_squeeze_scan as scanner
from test_short_squeeze import market,funding,CFG as PROD_CFG
from test_strength_v5_priority import row,scans,ASOF

CFG=lab.load_config()


def decision(symbol='AAAUSDT',venue='MEXC',rate=-.0002,oi=110.,price=100.):
    r=row(symbol,venue);r['feature_cutoff_ms']=ASOF//(4*3600000)*(4*3600000)
    current=market(venue,oi=oi,price=price);old=market(venue,stamp=ASOF-4*3600000,oi=100.)
    d=prod.decide(r,current,funding(rate=rate),[old],PROD_CFG,ASOF);d['row']=r
    return d


def case(symbol='AAAUSDT',venue='MEXC',stamp=ASOF+30000):
    return {'symbol':symbol,'exchange':venue,'observed_ms':stamp,'entry_price':100.,'btc_entry_price':80000.,
        'controls':[],'arms':dict.fromkeys(lab.ARMS,True),'split':'first25','outcomes':{},'cohort_index':1,
        'source_lag_minutes':1,'factor_metrics':{},'contract':'AAA_USDT'}


def minute_rows(start,end,price=110.):
    return [[t,100.,max(111.,price),95.,price,10] for t in range(start,end,60000)]


def fetcher(venue,symbol,start,end):
    if symbol=='BTCUSDT':return [[t,80000.,80000.,80000.,80000.,10] for t in range(start,end,60000)]
    return minute_rows(start,end)


class CohortChecks(unittest.TestCase):
    def test_factor_arms_are_separate_and_same_observation_not_four_new_coins(self):
        d=decision();members=lab.membership(d,ASOF,CFG)
        self.assertEqual(members,{'A':True,'B':True,'C':True,'D':True})
        self.assertEqual(lab.membership(decision(rate=.0001),ASOF,CFG),{'A':True,'B':False,'C':True,'D':False})
        self.assertEqual(lab.membership(decision(oi=100.),ASOF,CFG),{'A':True,'B':True,'C':False,'D':False})

    def test_unknown_warmup_and_common_failure_never_become_negative_factor_samples(self):
        for reason in ('warming','funding_unknown','market_data_unknown','not_listed','oi_liquidity','futures_spread','basis'):
            d=decision();d['reasons']=[reason]
            self.assertIsNone(lab.membership(d,ASOF,CFG))
        d=decision();d['metrics'].pop('oi_change_pct')
        self.assertIsNone(lab.membership(d,ASOF,CFG))

    def test_stale_and_future_derivative_observations_do_not_classify_current_entry(self):
        self.assertIsNone(lab.membership(decision(),ASOF+6*60000,CFG))
        d=decision();d['metrics']['funding_observed_ms']=ASOF+2*60000
        self.assertIsNone(lab.membership(d,ASOF,CFG))

    def test_duplicate_venues_choose_quote_quality_not_future_returns_or_arm_passes(self):
        d=decision(rate=.0001);o=decision(venue='OKX')
        r=deepcopy(d['row']);r['spread_pct']=.05;r['future_return']=999
        q=deepcopy(o['row']);q['spread_pct']=.1
        registry={'cases':{}}
        lab.register(registry,[d,o],scans([r,q]),CFG,ASOF)
        self.assertEqual(len(registry['cases']),1)
        self.assertEqual(registry['cases']['AAAUSDT']['exchange'],'MEXC')
        self.assertFalse(registry['cases']['AAAUSDT']['arms']['D'])

    def test_actual_new_quote_becomes_reference_not_original_production_price(self):
        d=decision();fresh=deepcopy(d['row']);fresh.update(mid_price=101.,observed_ms=ASOF+60000)
        registry={'cases':{}};before=deepcopy(d)
        lab.register(registry,[d],scans([fresh]),CFG,ASOF+60000)
        c=registry['cases']['AAAUSDT'];self.assertEqual(c['entry_price'],101.)
        self.assertEqual(c['observed_ms'],ASOF+60000);self.assertEqual(d,before)

    def test_later_factor_changes_cannot_rewrite_first_membership_or_price(self):
        d=decision();registry={'cases':{}}
        lab.register(registry,[d],scans([d['row']]),CFG,ASOF);first=deepcopy(registry['cases'])
        later=decision(rate=.0001);later['row']['mid_price']=101.
        lab.register(registry,[later],scans([later['row']]),CFG,ASOF)
        self.assertEqual(registry['cases'],first)

    def test_per_run_and_global_caps_do_not_fill_with_unknown_cases(self):
        cfg={**CFG,'max_unique_cases':2,'max_new_cases_per_run':1};registry={'cases':{}}
        data=[decision('A'+str(i)+'USDT') for i in range(5)]
        fresh=scans([d['row'] for d in data])
        self.assertEqual(len(lab.register(registry,data,fresh,cfg,ASOF)),1)
        self.assertEqual(len(lab.register(registry,data,fresh,cfg,ASOF)),1)
        self.assertEqual(lab.register(registry,data,fresh,cfg,ASOF),[])
        self.assertEqual(len(registry['cases']),2)

    def test_incomplete_btc_or_a_new_basis_gap_does_not_create_unmeasurable_case(self):
        d=decision();fresh=deepcopy(d['row']);fresh['paper_btc_price']=None
        registry={'cases':{}};lab.register(registry,[d],scans([fresh]),CFG,ASOF)
        self.assertEqual(registry['cases'],{})
        d['metrics']['futures_mid']=103.
        lab.register(registry,[d],scans([d['row']]),CFG,ASOF)
        self.assertEqual(registry['cases'],{})

    def test_policy_mismatch_refuses_to_relabel_an_existing_cohort(self):
        state={'comparison_lab':{'fingerprint':'different','cases':{'AAA':{'price':1}}}}
        old=deepcopy(state)
        with self.assertRaises(ValueError):lab.lab_state(state)
        self.assertEqual(state,old)


class MeasurementChecks(unittest.TestCase):
    def test_okx_adapter_already_returns_confirmed_normalized_eight_field_candles(self):
        normalized=[[60000,100.,111.,95.,110.,10,120000,1000.]]
        with patch.object(lab.okx,'fetch_rows',return_value=(normalized,[])) as fetch:
            result=lab.fetch_minutes('OKX','AAAUSDT',60000,120000)
        self.assertEqual(result,normalized);self.assertEqual(len(result),1)
        fetch.assert_called_once_with('AAAUSDT','1m',60000,119999)

    def test_no_future_reads_before_horizon_and_open_bars_never_count(self):
        c=case();fake=Mock()
        self.assertFalse(lab.update_case(c,CFG,c['observed_ms']+3600000,fake));fake.assert_not_called()
        start=60000;end=180000
        bars=lab.candles(minute_rows(start,end),start,end,120000)
        self.assertEqual(set(bars),{60000})

    def test_targets_use_real_first_minute_close_after_signal_horizon_and_correct_path(self):
        c=case();stamp=c['observed_ms']+6*3600000+60000
        self.assertTrue(lab.update_case(c,CFG,stamp,fetcher));o=c['outcomes']['6']
        self.assertEqual(o['endpoint_delay_ms'],30000)
        self.assertEqual(o['ignored_entry_fragment_ms'],30000)
        self.assertAlmostEqual(o['return_pct'],10)
        self.assertAlmostEqual(o['mae_pct'],-5);self.assertAlmostEqual(o['mfe_pct'],11)
        self.assertAlmostEqual(o['cost_scenarios_pct']['0.2'],9.8)
        self.assertTrue(o['complete']);self.assertIsNone(o['control_excess_pct_points'])

    def test_pre_entry_spike_is_not_used_for_mae_mfe(self):
        c=case();stamp=c['observed_ms']+6*3600000+60000
        def fake(v,s,start,end):
            result=fetcher(v,s,start,end)
            if s=='AAAUSDT':result.insert(0,[start-60000,100.,999.,1.,100.,10])
            return result
        lab.update_case(c,CFG,stamp,fake)
        self.assertAlmostEqual(c['outcomes']['6']['mfe_pct'],11)
        self.assertAlmostEqual(c['outcomes']['6']['mae_pct'],-5)

    def test_missing_intermediate_minute_keeps_path_unknown_without_inventing_return_zero(self):
        c=case();stamp=c['observed_ms']+6*3600000+60000
        def fake(v,s,start,end):
            result=fetcher(v,s,start,end)
            return result[:2]+result[3:] if s=='AAAUSDT' else result
        lab.update_case(c,CFG,stamp,fake);o=c['outcomes']['6']
        self.assertAlmostEqual(o['return_pct'],10);self.assertIsNone(o['mae_pct']);self.assertFalse(o['complete'])

    def test_missing_endpoint_or_btc_cannot_count_as_completed_success(self):
        for missing in ('AAAUSDT','BTCUSDT'):
            c=case();stamp=c['observed_ms']+6*3600000+60000
            def fake(v,s,start,end):return [] if s==missing else fetcher(v,s,start,end)
            lab.update_case(c,CFG,stamp,fake);self.assertFalse(c['outcomes']['6']['complete'])

    def test_missing_controls_are_not_a_fabricated_zero_benchmark(self):
        c=case();c['controls']=[{'symbol':'C'+str(i)+'USDT','entry_price':100.} for i in range(3)]
        stamp=c['observed_ms']+6*3600000+60000
        def fake(v,s,start,end):return [] if s=='C1USDT' else fetcher(v,s,start,end)
        lab.update_case(c,CFG,stamp,fake);o=c['outcomes']['6']
        self.assertIsNone(o['control_excess_pct_points']);self.assertFalse(o['complete'])

    def test_completed_windows_are_not_refetched_without_new_due_measurements(self):
        c=case();stamp=c['observed_ms']+6*3600000+60000
        lab.update_case(c,CFG,stamp,fetcher);fake=Mock()
        self.assertFalse(lab.update_case(c,CFG,stamp,fake));fake.assert_not_called()

    def test_conflicting_duplicate_and_nan_candles_are_rejected(self):
        first=[60000,100.,111.,95.,110.,10];other=[60000,100.,111.,95.,109.,10]
        with self.assertRaises(ValueError):lab.candles([first,other],60000,120000,120000)
        first[4]=float('nan')
        with self.assertRaises(ValueError):lab.candles([first],60000,120000,120000)

    def test_measurement_budget_rotates_and_one_venue_failure_does_not_stop_the_other(self):
        a=case('AAAUSDT','MEXC');b=case('BBBUSDT','OKX')
        registry={'cases':{'AAAUSDT':a,'BBBUSDT':b}};stamp=a['observed_ms']+6*3600000+60000
        def fake(v,s,start,end):
            if v=='MEXC':raise RuntimeError('MEXC unavailable')
            return fetcher(v,s,start,end)
        lab.measure(registry,{**CFG,'max_cases_measured_per_run':2},stamp,fake)
        self.assertEqual(len(registry['errors']),1);self.assertTrue(b['outcomes']['6']['complete'])
        self.assertNotIn('6',a['outcomes'])

    def test_summary_denominators_use_completed_cases_and_keep_unknowns_visible(self):
        a=case();b=case('BBBUSDT');a['outcomes']['12']={'complete':True,'return_pct':.1,'btc_excess_pct_points':.2,
            'control_excess_pct_points':None,'mae_pct':-1,'mfe_pct':2}
        registry={'cases':{'AAA':a,'BBB':b}}
        stats=lab.summarize(registry,CFG)
        self.assertEqual(stats['A']['cases'],2);self.assertEqual(stats['A']['measured'],1)
        self.assertEqual(stats['A']['positive_after_cost_fraction']['0.2'],0)
        self.assertFalse(stats['A']['enough_for_initial_review'])
        self.assertIsNone(stats['A']['median_controls_excess_pct_points'])


class PreservationChecks(unittest.TestCase):
    def test_full_shadow_observe_preserves_all_production_fields_and_does_not_notify(self):
        with TemporaryDirectory() as directory:
            out=Path(directory);path=out/'state.json';d=decision()
            state=prod.new_state();state['latest']={'decisions':[d]}
            state['pending']=[{'id':'production-pending','candidates':[]}]
            state['paper']={'entries':{'old':{'price':123}}};original=deepcopy(state)
            path.write_text(json.dumps(state),encoding='utf-8');(out/'report.md').write_text('# Production report\n',encoding='utf-8')
            with patch.object(scanner,'OUT',out),patch.object(scanner,'STATE',path),patch.object(lab,'now_ms',return_value=ASOF),\
                patch.object(lab,'copied_quotes',return_value=scans([d['row']])),patch.object(scanner.cloud,'http_json') as notify:
                lab.observe();notify.assert_not_called()
            final=json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual({k:v for k,v in final.items() if k!='comparison_lab'},original)
            self.assertEqual(len(final['comparison_lab']['cases']),1)
            text=(out/'report.md').read_text(encoding='utf-8');self.assertTrue(text.startswith('# Production report'))
            self.assertIn('Ücretsiz karşılaştırmalı deney',text)

    def test_empty_or_cold_inputs_do_not_fill_cohort_or_request_historical_returns(self):
        with TemporaryDirectory() as directory:
            out=Path(directory);path=out/'state.json';state=prod.new_state();d=decision();d['reasons']=['warming'];state['latest']={'decisions':[d]}
            path.write_text(json.dumps(state),encoding='utf-8');(out/'report.md').write_text('# Original\n',encoding='utf-8')
            with patch.object(scanner,'OUT',out),patch.object(scanner,'STATE',path),patch.object(lab,'now_ms',return_value=ASOF),\
                patch.object(lab,'copied_quotes',return_value=scans([d['row']])):lab.observe()
            final=json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(final['comparison_lab']['cases'],{})
            self.assertEqual(final['comparison_lab']['measurement']['attempted'],0)

if __name__=='__main__':unittest.main()
