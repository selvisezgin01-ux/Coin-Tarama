from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd

import strength_v4 as previous
import strength_v5 as model
import strength_v5_watch as watch
import paper_watch
from study_dataset import STEP,read_json

CONFIG=read_json(Path(__file__).with_name('strength_v5_config.json'))


def base():
    close=100+np.arange(240)*.015+np.sin(np.arange(240))*.15
    return pd.DataFrame({'open':close-.05,'high':close+.5,'low':close-.5,'close':close,
        'volume':1000.,'quote_volume':100000.},index=np.arange(240)*STEP)


def retest_fixture():
    f=base();level=f.high.iloc[190:210].max()
    f.iloc[210]=[level-.3,level+3.1,level-.4,level+2.9,5000.,500000.]
    f.iloc[211]=[level+2.9,level+4,level+2,level+3,1000.,100000.]
    for i in (212,213):f.iloc[i]=[level+.35,level+.6,level-.05,level+.4,1000.,100000.]
    return f


def enrich(frame,btc=None):
    if btc is None:btc=pd.Series(0.,index=frame.index);btc.attrs['return8']=btc.copy()
    return model.features(frame,btc,CONFIG)


class AddedGroups(unittest.TestCase):
    def test_prefix_and_future_changes_cannot_repaint_signals(self):
        f=retest_fixture();original=enrich(f);changed=f.copy()
        changed.iloc[220:,:4]*=3;changed.iloc[220:,4:]*=7
        pd.testing.assert_frame_equal(original.iloc[:220],enrich(changed).iloc[:220])
        pd.testing.assert_frame_equal(original.iloc[:214],enrich(f.iloc[:214]))

    def test_original_paths_remain_exactly_the_same(self):
        f=retest_fixture();btc=pd.Series(0.,index=f.index);btc.attrs['return8']=btc.copy()
        old=previous.features(f,btc,CONFIG);new=model.features(f,btc,CONFIG)
        pd.testing.assert_series_equal(new.group_new_breakout,old.new_breakout,check_names=False)
        pd.testing.assert_series_equal(new.group_continuation,old.continuation,check_names=False)

    def test_early_reversal_does_not_require_old_peak_or_rising_ema20(self):
        f=base()
        for i in range(200,210):
            price=99-(i-200)*.1;f.iloc[i]=[price+.1,price+.3,price-.2,price,1000.,100000.]
        f.iloc[210]=[98.2,100.8,98.0,100.6,2000.,200000.]
        row=enrich(f).iloc[210]
        self.assertTrue(row.group_early_reversal);self.assertFalse(row.gate_anchor)
        self.assertFalse(row.gate_trend);self.assertTrue(row.qualified)
        self.assertIn('early_reversal',row.matched_groups)

    def test_upper_wick_and_lack_of_volume_do_not_create_early_reversal(self):
        f=base()
        for i in range(200,210):
            p=99-(i-200)*.1;f.iloc[i]=[p+.1,p+.3,p-.2,p,1000.,100000.]
        f.iloc[210]=[98.2,110,98,100.6,2000.,200000.]
        self.assertFalse(enrich(f).iloc[210].group_early_reversal)
        f.iloc[210]=[98.2,100.8,98,100.6,1000.,100000.]
        self.assertFalse(enrich(f).iloc[210].group_early_reversal)

    def test_flat_price_volume_path_is_not_an_all_conditions_conjunction(self):
        f=base();p=f.close.iloc[209]
        for i in (207,208,209):f.iloc[i]=[p,p+.4,p-.4,p,1000.,100000.]
        f.iloc[210]=[p,p+.4,p-.35,p+.1,2000.,200000.]
        row=enrich(f).iloc[210]
        self.assertTrue(row.group_sideways_volume);self.assertFalse(row.group_early_reversal)
        self.assertFalse(row.group_retest);self.assertTrue(row.qualified)
        f.iloc[210]=[p,p+4,p-.35,p+3,2000.,200000.]
        self.assertFalse(enrich(f).iloc[210].group_sideways_volume)

    def test_true_retest_needs_excursion_support_base_and_sar(self):
        rows=enrich(retest_fixture())
        self.assertTrue(rows.iloc[210].new_breakout)
        self.assertFalse(rows.iloc[210].group_retest)
        self.assertFalse(rows.iloc[211].group_retest)
        self.assertTrue(rows.iloc[213].retest_touched_support)
        self.assertTrue(rows.iloc[213].sar_below)
        self.assertTrue(rows.iloc[213].group_retest)

    def test_broken_support_is_not_resurrected_by_returning_to_the_level(self):
        f=retest_fixture();f.iloc[211,f.columns.get_loc('low')]=95
        self.assertFalse(enrich(f).iloc[213].group_retest)

    def test_quiet_bars_without_a_real_return_are_not_a_retest(self):
        f=retest_fixture();level=f.high.iloc[190:210].max()
        for i in (212,213):f.iloc[i]=[level+2,level+2.3,level+1.8,level+2.1,1000.,100000.]
        self.assertFalse(enrich(f).iloc[213].group_retest)

    def test_retest_requires_sar_and_lower_base_volume(self):
        f=retest_fixture()
        with patch.object(previous,'parabolic_sar',return_value={'sar_below':pd.Series(False,index=f.index)}):
            self.assertFalse(enrich(f).iloc[213].group_retest)
        f.iloc[212:214,f.columns.get_loc('quote_volume')]=600000
        self.assertFalse(enrich(f).iloc[213].group_retest)

    def test_raw_weak_breakout_does_not_seed_a_confirmed_retest(self):
        f=retest_fixture();f.iloc[210,f.columns.get_loc('high')]=150
        rows=enrich(f)
        self.assertTrue(rows.iloc[210].breakout_now);self.assertFalse(rows.iloc[210].new_breakout)
        self.assertFalse(rows.iloc[213].group_retest)

    def test_zero_liquidity_or_missing_btc_never_qualifies(self):
        f=retest_fixture();f.quote_volume=0
        self.assertFalse(enrich(f).qualified.any())
        f=retest_fixture();btc=pd.Series(np.nan,index=f.index);btc.attrs['return8']=btc.copy()
        self.assertFalse(enrich(f,btc).qualified.any())

    def test_price_scale_does_not_change_group_membership(self):
        f=retest_fixture();original=enrich(f);f[['open','high','low','close']]*=.000001
        changed=enrich(f)
        for group in model.ORDER:
            pd.testing.assert_series_equal(original['group_'+group],changed['group_'+group])


class StateAndMeasurements(unittest.TestCase):
    def row(self,stamp=1000,price=1,groups=None):
        return {'symbol':'TESTUSDT','exchange':'MEXC','observed_ms':stamp,'mid_price':price,'paper_btc_price':100.,
            'paper_controls':[],'stage':'early_reversal','matched_groups':groups or ['early_reversal'],'breakout_open_ms':None}

    def test_group_transition_uses_its_own_actual_price_without_changing_primary(self):
        state={};watch.register_measurements(state,{'MEXC':{'candidates':[self.row()]}})
        watch.register_measurements(state,{'MEXC':{'candidates':[self.row(2000,1.2,['early_reversal','retest'])]}})
        primary=state['paper']['entries']['MEXC:TESTUSDT']
        later=state['group_measurements']['retest']['paper']['entries']['MEXC:TESTUSDT']
        self.assertEqual(primary['entry_price'],1);self.assertEqual(primary['observed_ms'],1000)
        self.assertEqual(later['entry_price'],1.2);self.assertEqual(later['observed_ms'],2000)
        self.assertEqual(len(state['paper']['entries']),1)

    def test_overlapping_cohorts_share_fetches_and_unknown_stays_unknown(self):
        state={};watch.register_measurements(state,{'MEXC':{'candidates':[self.row(groups=['early_reversal','sideways_volume'])]}})
        calls=[]
        def fetch(venue,symbol,endpoint):calls.append((venue,symbol,endpoint));return None
        watch.refresh_measurements(state,1000+13*3600000,fetcher=fetch)
        self.assertEqual(len(calls),len(set(calls)));self.assertEqual(len(calls),2)
        entry=state['paper']['entries']['MEXC:TESTUSDT']
        self.assertIsNone(entry['outcomes']['12']['return_pct'])

    def test_original_branches_cannot_be_written(self):
        for branch in ('scanner-state','scanner-state-v4','scanner-state-meme-v3'):
            with patch.dict(os.environ,{'SCANNER_STATE_BRANCH':branch}):
                with self.assertRaises(ValueError):watch.configure()

    def test_labels_do_not_turn_non_breakout_groups_into_breakout_signals(self):
        row={**self.row(),'return24_pct':1.,'signal_volume_ratio':2.,'spread_pct':.1,'warnings':[]}
        text=watch.row_text(row)
        self.assertIn('Erken dönüş',text);self.assertNotIn('yeni kırılım',text.lower())

    def test_migration_keeps_actual_prices_cooldowns_and_does_not_backdate_v5(self):
        previous={'rules_fingerprint':'dec8ec5333c785f60a104f211aafb2d0b3a6343581c89e2ee198890de649be78',
            'pending':[],'venues':{'MEXC':{'active':['TESTUSDT'],'last_alert':{'TESTUSDT':1000},'ever_seen':['TESTUSDT'],'latest':{'old':True}}},
            'paper':{'version':paper_watch.VERSION,'entries':{'MEXC:TESTUSDT':{'entry_price':1,'observed_ms':1000}},'measurement_errors':[]}}
        state=watch.migrate(previous,'scanner-state-v4','commit')
        self.assertEqual(state['previous_v4']['paper'],previous['paper'])
        self.assertEqual(state['venues']['MEXC']['last_alert'],{'TESTUSDT':1000})
        self.assertNotIn('paper',state);self.assertNotIn('latest',state['venues']['MEXC'])
        previous['paper']['entries']['MEXC:TESTUSDT']['entry_price']=99
        self.assertEqual(state['previous_v4']['paper']['entries']['MEXC:TESTUSDT']['entry_price'],1)
        previous['pending']=[{'id':'unsent'}]
        with self.assertRaises(ValueError):watch.migrate(previous,'scanner-state-v4','commit')

    def test_notify_preserves_dedup_and_uses_group_labels(self):
        row={**self.row(),'return24_pct':1.,'signal_volume_ratio':2.,'spread_pct':.1,'warnings':[]}
        state={'pending':[{'id':'batch','created_ms':1000,'candidates':[row]}]};sent=[]
        def http(url,payload=None,headers=None,label=None):
            if payload is None:return []
            sent.append(payload);return {'number':1}
        with TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            path=Path(tmp)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(watch.cloud,'STATE',path),patch.object(watch.cloud,'http_json',side_effect=http),patch.dict(os.environ,
                    {'SCANNER_STATE_BRANCH':'scanner-state-v5','GITHUB_REPOSITORY':'example/test','GH_TOKEN':'unit-test-only','COIN_SCAN_LABEL':'Coin Tarama 3'}):
                watch.notify('github_issue');watch.notify('github_issue')
        self.assertEqual(len(sent),1);self.assertIn('Erken dönüş',sent[0]['body'])
        self.assertIn('coin-scanner:scanner-state-v5:batch',sent[0]['body'])

    def test_one_exchange_failure_does_not_drop_the_other_or_existing_references(self):
        with TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            folder=Path(tmp)
            (folder/'state.json').write_text(json.dumps({**watch.new_state(),'initialization_complete':True}),encoding='utf-8')
            def snapshot(venue,config):
                if venue=='OKX':raise RuntimeError('exchange unavailable')
                return Path('fixture')
            result={'candidates':[],'exchange':'MEXC','observed_ms':1,'feature_cutoff_ms':0,'universe_count':10,'prefilter_count':4,'analyzed_count':3}
            def report(scans,archive):(folder/'report.md').write_text('# fixture',encoding='utf-8')
            with patch.object(watch.cloud,'OUT',folder),patch.object(watch.cloud,'STATE',folder/'state.json'),\
                 patch.object(watch.scanner,'OUT',folder),patch.object(watch.scanner,'snapshot',side_effect=snapshot),\
                 patch.object(watch.scanner,'evaluate',return_value=result),patch.object(watch.scanner,'write_report',side_effect=report),\
                 patch.object(watch,'refresh_measurements'):
                watch.scan()
            state=read_json(folder/'state.json')
            self.assertIn('MEXC',state['venues']);self.assertNotIn('OKX',state['venues'])
            self.assertIn('error',read_json(folder/'scan.json')['scans']['OKX'])

    def test_incomplete_migration_cannot_be_published_by_always_checkpoint_step(self):
        with TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            path=Path(tmp)/'state.json';path.write_text(json.dumps(watch.new_state()),encoding='utf-8')
            with patch.object(watch.cloud,'STATE',path),patch.object(watch.cloud,'push_state') as push:
                with self.assertRaises(ValueError):watch.push_state()
                push.assert_not_called()


if __name__=='__main__':unittest.main()
