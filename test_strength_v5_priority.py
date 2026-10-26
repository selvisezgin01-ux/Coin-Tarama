from copy import deepcopy
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
import strength_v5_priority as priority
import strength_v5_watch as watch
from study_dataset import STEP,read_json

CFG=read_json(Path(__file__).with_name('strength_v5_priority_config.json'))
ASOF=4*STEP+60000


def row(symbol='AAAUSDT',venue='MEXC',ratio=2):
    return {'symbol':symbol,'exchange':venue,'matched_groups':['early_reversal'],'stage':'early_reversal',
      'observed_ms':ASOF,'mid_price':100.,'close':100.,'atr':2.,'ema20':99.,'signal_reference_level':99.,
      'signal_invalidation_level':95.,'quote_volume24':200000.,'spread_pct':.1,'signal_volume_ratio':ratio,
      'close_position':.8,'return24_pct':3.,'paper_btc_price':80000.,'paper_controls':[],
      'breakout_open_ms':None,'warnings':[]}


def scans(rows):
    return {venue:{'feature_cutoff_ms':4*STEP,'candidates':[r for r in rows if r['exchange']==venue]}
            for venue in sorted({r['exchange'] for r in rows})}


class SelectionChecks(unittest.TestCase):
    def test_five_unique_symbols_maximum_without_filling_an_empty_list(self):
        result=priority.select(scans([row('A'+str(i)+'USDT') for i in range(8)]),CFG,ASOF)
        self.assertEqual(len(result['selected']),5);self.assertEqual(result['eligible_unique'],8)
        self.assertEqual(len(result['ranked_but_not_selected']),3)
        self.assertEqual(priority.select(scans([]),CFG,ASOF)['selected'],[])

    def test_duplicate_venues_do_not_add_volume_or_claim_a_failing_venue_passed(self):
        a=row();b=row(venue='OKX');b['quote_volume24']=99999
        result=priority.select(scans([a,b]),CFG,ASOF)
        self.assertEqual(result['raw_rows'],2);self.assertEqual(result['raw_unique'],1)
        self.assertEqual(result['selected'][0]['passing_venues'],['MEXC'])
        b['quote_volume24']=300000
        result=priority.select(scans([a,b]),CFG,ASOF)
        self.assertEqual(len(result['selected']),1)
        self.assertEqual(result['selected'][0]['quote_volume24'],300000)
        self.assertEqual(result['selected'][0]['passing_venues'],['MEXC','OKX'])

    def test_each_material_risk_excludes_priority_but_preserves_reasons(self):
        examples=[('quote_volume24',90000,'volume'),('spread_pct',.51,'spread'),
          ('signal_reference_level',101,'structure_lost'),('close',96,'quote_drift'),
          ('ema20',90,'extension'),('signal_invalidation_level',80,'risk_distance')]
        for field,value,reason in examples:
            r=row();r[field]=value;result=priority.select(scans([r]),CFG,ASOF)
            self.assertEqual(result['selected'],[]);self.assertIn(reason,result['excluded'][0]['reasons'])

    def test_actual_price_instead_of_old_close_sets_risk_and_ema_extension(self):
        r=row();r['mid_price']=103;r['ema20']=98
        result=priority.select(scans([r]),CFG,ASOF)
        self.assertIn('quote_drift',result['excluded'][0]['reasons'])
        r=row();r['signal_invalidation_level']=88.1;r['mid_price']=101
        self.assertIn('risk_distance',priority.select(scans([r]),CFG,ASOF)['excluded'][0]['reasons'])

    def test_preparation_remains_available_but_never_automatically_notifies(self):
        r=row();r['matched_groups']=['sideways_volume']
        self.assertIn('preparation_only',priority.select(scans([r]),CFG,ASOF)['excluded'][0]['reasons'])
        r['matched_groups'].append('early_reversal')
        self.assertEqual(len(priority.select(scans([r]),CFG,ASOF)['selected']),1)

    def test_equity_exclusion_is_exact_and_venue_specific_not_all_x_tokens(self):
        for symbol in ('XLITEUSDT','XASMLUSDT'):
            self.assertIn('known_equity',priority.select(scans([row(symbol,'OKX')]),CFG,ASOF)['excluded'][0]['reasons'])
        for symbol in ('XRPUSDT','XLMUSDT','XMRUSDT'):
            self.assertEqual(len(priority.select(scans([row(symbol,'OKX')]),CFG,ASOF)['selected']),1)
        self.assertEqual(len(priority.select(scans([row('XLITEUSDT','MEXC')]),CFG,ASOF)['selected']),1)

    def test_no_new_return_cap_but_extreme_volume_is_manual_review(self):
        r=row();r['return24_pct']=80
        self.assertEqual(len(priority.select(scans([r]),CFG,ASOF)['selected']),1)
        r['signal_volume_ratio']=684
        self.assertIn('extreme_volume',priority.select(scans([r]),CFG,ASOF)['excluded'][0]['reasons'])

    def test_old_quotes_and_old_decision_cannot_masquerade_as_current(self):
        r=row();r['observed_ms']=ASOF-16*60000
        self.assertIn('quote_age',priority.select(scans([r]),CFG,ASOF)['excluded'][0]['reasons'])
        s=scans([row()]);s['MEXC']['feature_cutoff_ms']=3*STEP
        self.assertIn('decision_stale',priority.select(s,CFG,ASOF)['excluded'][0]['reasons'])

    def test_missing_or_nonfinite_fields_are_not_clean_values(self):
        for field in ('mid_price','atr','ema20','spread_pct','quote_volume24','signal_invalidation_level'):
            for value in (None,float('nan')):
                r=row();r[field]=value
                self.assertFalse(priority.select(scans([r]),CFG,ASOF)['selected'])

    def test_future_outcome_or_raw_score_does_not_change_priority_rank(self):
        original=scans([row('AAAUSDT',ratio=3),row('BBBUSDT',ratio=2)])
        expected=priority.select(original,CFG,ASOF)
        changed=deepcopy(original)
        for r in changed['MEXC']['candidates']:r.update({'future_return_pct':999,'strength_score':10000})
        actual=priority.select(changed,CFG,ASOF)
        self.assertEqual([r['symbol'] for r in expected['selected']],[r['symbol'] for r in actual['selected']])


class PersistenceAndDelivery(unittest.TestCase):
    def observe(self,state,data,stamp=ASOF):
        with patch.object(priority.paper_watch,'refresh'):return priority.observe(state,data,CFG,stamp)

    def test_raw_pool_and_original_references_remain_unchanged(self):
        data=scans([row(),{**row('BBBUSDT'),'spread_pct':2}]);before=deepcopy(data)
        state={'pending':[{'id':'raw','created_ms':ASOF,'candidates':data['MEXC']['candidates']}],
            'venues':deepcopy(data),'paper':{'version':'github-paper-v1','entries':{'old':{'entry_price':90}},'measurement_errors':[]}}
        p=self.observe(state,data)
        self.assertEqual(data,before);self.assertEqual(state['venues'],before)
        self.assertEqual(state['paper']['entries']['old']['entry_price'],90);self.assertEqual(state['pending'],[])
        self.assertEqual(p['paper']['entries']['MEXC:AAAUSDT']['entry_price'],100)
        self.assertEqual(len(p['pending'][0]['candidates']),1)

    def test_filtered_coin_can_later_enter_priority_despite_raw_engine_cooldown(self):
        state={'pending':[],'venues':{'MEXC':{'last_alert':{'AAAUSDT':ASOF}}}}
        bad={**row(),'spread_pct':2};self.observe(state,scans([bad]))
        p=self.observe(state,scans([row()]))
        self.assertEqual(p['pending'][-1]['candidates'][0]['symbol'],'AAAUSDT')

    def test_failure_preserves_prior_active_without_claiming_current_pass(self):
        state={'pending':[]};p=self.observe(state,scans([row()]))
        p['last_sent']['AAAUSDT']=ASOF;p['pending']=[]
        p=self.observe(state,{'MEXC':{'error':'unavailable'}},ASOF+60000)
        self.assertEqual(p['active'],['AAAUSDT']);self.assertEqual(p['latest']['selected'],[])
        self.assertIn('MEXC',p['latest']['source_errors'])

    def test_quote_refresh_is_a_copy_and_never_rewrites_core_entry_prices(self):
        data=scans([row()]);before=deepcopy(data)
        def public(endpoint):
            if endpoint=='ticker/bookTicker':return [{'symbol':'AAAUSDT','bidPrice':'101','askPrice':'101.2'}]
            if endpoint=='time':return {'serverTime':ASOF+1000}
            raise AssertionError(endpoint)
        with patch.object(priority.watch.scanner.mexc,'public_get',side_effect=public):fresh=priority.refresh_quotes(data)
        self.assertEqual(data,before);self.assertAlmostEqual(fresh['MEXC']['candidates'][0]['mid_price'],101.1)
        self.assertEqual(fresh['MEXC']['candidates'][0]['observed_ms'],ASOF+1000)

    def test_fresh_coin_reference_uses_same_book_btc_and_control_prices(self):
        r=row();r['paper_controls']=[{'symbol':'CTRLUSDT','entry_price':1}]
        def public(endpoint):
            if endpoint=='time':return {'serverTime':ASOF+1000}
            return [{'symbol':s,'bidPrice':str(p),'askPrice':str(p)} for s,p in [('AAAUSDT',101),('BTCUSDT',81000),('CTRLUSDT',2)]]
        with patch.object(priority.watch.scanner.mexc,'public_get',side_effect=public):fresh=priority.refresh_quotes(scans([r]))
        saved=fresh['MEXC']['candidates'][0]
        self.assertEqual(saved['paper_btc_price'],81000)
        self.assertEqual(saved['paper_controls'],[{'symbol':'CTRLUSDT','entry_price':2}])

    def test_refresh_failure_retains_known_raw_count_but_cannot_select_stale_quotes(self):
        with patch.object(priority.watch.scanner.mexc,'public_get',side_effect=RuntimeError('provider unavailable')):
            fresh=priority.refresh_quotes(scans([row()]))
        result=priority.select(fresh,CFG,ASOF)
        self.assertEqual(result['raw_rows'],1);self.assertEqual(result['raw_unique'],1)
        self.assertEqual(result['selected'],[]);self.assertIn('MEXC',result['source_errors'])

    def test_message_retries_reconcile_old_delivery_without_duplicate_issue(self):
        state={'pending':[]};p=self.observe(state,scans([row()]));old=p['pending'][0]['id']
        newer={**row(),'observed_ms':ASOF+1000};p=self.observe(state,scans([newer]),ASOF+1000)
        sent=[]
        def http(url,payload=None,headers=None,label=None):
            if payload is None:return [{'body':'<!-- coin-priority-v5:'+old+' -->'}]
            sent.append(payload);return {'number':1}
        with TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            path=Path(tmp)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(watch.cloud,'STATE',path),patch.object(watch.cloud,'http_json',side_effect=http),\
                 patch.object(priority,'now_ms',return_value=ASOF+1000),patch.dict(os.environ,
                 {'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'unit-test-only','COIN_NOTIFY_USER':'test-user'}):priority.notify('github_issue',CFG)
            result=read_json(path)
        self.assertEqual(sent,[]);self.assertEqual(result['priority_watch']['pending'],[])
        self.assertIn('AAAUSDT',result['priority_watch']['last_sent'])

    def test_failed_delivery_keeps_pending_and_retry_sends_once(self):
        state={'pending':[]};self.observe(state,scans([row()]));sent=[];fail=[True]
        def http(url,payload=None,headers=None,label=None):
            if payload is None:return []
            if fail[0]:raise RuntimeError('test failure')
            sent.append(payload);return {'number':1}
        with TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            path=Path(tmp)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(watch.cloud,'STATE',path),patch.object(watch.cloud,'http_json',side_effect=http),\
                 patch.object(priority,'now_ms',return_value=ASOF),patch.dict(os.environ,
                 {'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'unit-test-only','COIN_NOTIFY_USER':'test-user'}):
                with self.assertRaises(RuntimeError):priority.notify('github_issue',CFG)
                self.assertEqual(len(read_json(path)['priority_watch']['pending']),1)
                fail[0]=False;priority.notify('github_issue',CFG);priority.notify('github_issue',CFG)
        self.assertEqual(len(sent),1);self.assertIn('1 coin',sent[0]['title']);self.assertIn('@test-user',sent[0]['body'])

    def test_obsolete_unsent_batch_is_replaced_with_current_price_only(self):
        state={'pending':[]};self.observe(state,scans([row()]))
        self.observe(state,scans([{**row(),'mid_price':101,'observed_ms':ASOF+1000}]),ASOF+1000)
        sent=[]
        def http(url,payload=None,headers=None,label=None):
            if payload is None:return []
            sent.append(payload);return {'number':1}
        with TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            path=Path(tmp)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(watch.cloud,'STATE',path),patch.object(watch.cloud,'http_json',side_effect=http),\
                 patch.object(priority,'now_ms',return_value=ASOF+1000),patch.dict(os.environ,
                 {'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'unit-test-only'}):priority.notify('github_issue',CFG)
        self.assertEqual(len(sent),1);self.assertIn('101',sent[0]['body'])

    def test_wide_report_is_collapsed_and_repeated_render_does_not_nest_it(self):
        state={'pending':[]};self.observe(state,scans([row()]))
        with TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            path=Path(tmp)/'report.md';path.write_text('# broad raw report',encoding='utf-8')
            with patch.object(watch.cloud,'OUT',Path(tmp)):
                priority.render(state,CFG);priority.render(state,CFG)
            text=path.read_text(encoding='utf-8')
        self.assertEqual(text.count(priority.RAW_START),1);self.assertIn('<details>',text)
        self.assertIn('AAAUSDT',text);self.assertIn('broad raw report',text)


if __name__=='__main__':unittest.main()
