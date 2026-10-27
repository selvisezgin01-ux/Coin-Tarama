from copy import deepcopy
import json,os,tempfile,unittest
from pathlib import Path
from unittest.mock import Mock,patch
from urllib.error import HTTPError
import short_squeeze as model
import short_squeeze_sources as sources
import short_squeeze_scan as scan
import paper_watch
from test_strength_v5_priority import row,CFG as POLICY,ASOF,scans

CFG=json.loads(model.CONFIG.read_text(encoding='utf-8'))


def market(venue='MEXC',stamp=ASOF,oi=110.,price=100.):
    return {'symbol':'AAAUSDT','venue':venue,'contract':'AAA_USDT' if venue=='MEXC' else 'AAA-USDT-SWAP',
        'contract_size':1.,'observed_ms':stamp,'price_ms':stamp,'oi_contracts':oi,'mid_price':price,
        'spread_pct':.1,'oi_notional':2000000,'notional_kind':'estimated_USDT_at_current_mid'}


def funding(stamp=ASOF,rate=-.0002,hours=8):
    return {'observed_ms':stamp,'rate':rate,'interval_hours':hours,'scaled_8h_rate':rate*8/hours}


class RulesTests(unittest.TestCase):
    def setUp(self):
        self.current=market();self.old=market(stamp=ASOF-4*3600000,oi=100.)
        self.r=row()

    def decide(self,**kw):
        return model.decide(kw.get('row',self.r),kw.get('current',self.current),kw.get('funding',funding()),kw.get('history',[self.old]),CFG,ASOF)

    def test_negative_funding_growing_contract_oi_and_held_price_can_qualify(self):
        result=self.decide();self.assertEqual(result['status'],'candidate')
        self.assertAlmostEqual(result['metrics']['oi_change_pct'],10)
        self.assertEqual(result['metrics']['elapsed_hours'],4)

    def test_no_past_observation_is_warmup_not_a_backfilled_signal(self):
        result=self.decide(history=[])
        self.assertEqual(result['status'],'warming');self.assertNotIn('oi_change_pct',result['metrics'])
        self.assertIsNone(model.baseline([self.current],self.current,CFG))

    def test_funding_alone_or_growing_oi_alone_is_not_enough(self):
        current={**self.current,'oi_contracts':100.}
        self.assertIn('oi_growth',self.decide(current=current)['reasons'])
        self.assertIn('funding',self.decide(funding=funding(rate=.0001))['reasons'])

    def test_nominal_oi_growth_caused_by_price_does_not_fake_contract_oi_growth(self):
        current={**self.current,'oi_contracts':100.,'oi_notional':4000000}
        self.assertIn('oi_growth',self.decide(current=current)['reasons'])

    def test_price_dropping_or_already_running_away_is_excluded(self):
        self.assertIn('price_weak',self.decide(current={**self.current,'mid_price':99.})['reasons'])
        self.assertIn('extended',self.decide(current={**self.current,'mid_price':113.})['reasons'])

    def test_stale_or_future_data_is_unknown_not_a_clean_negative(self):
        self.assertEqual(self.decide(current={**self.current,'observed_ms':ASOF-6*60000})['status'],'unknown')
        self.assertEqual(self.decide(current={**self.current,'price_ms':ASOF+2*60000})['status'],'unknown')
        self.assertIn('funding_unknown',self.decide(funding=None)['reasons'])

    def test_wide_futures_spread_small_oi_and_basis_are_separate_rejections(self):
        for changed,reason in [({'spread_pct':.6},'futures_spread'),({'oi_notional':999999},'oi_liquidity'),({'mid_price':103},'basis')]:
            self.assertIn(reason,self.decide(current={**self.current,**changed})['reasons'])

    def test_different_contract_size_or_venue_id_cannot_supply_a_baseline(self):
        for changed in ({'contract_size':1000.},{'contract':'AAA-USDT-SWAP'}):
            self.assertEqual(self.decide(history=[{**self.old,**changed}])['status'],'warming')

    def test_elapsed_window_is_real_and_no_interpolation_outside_3_to_5_hours(self):
        prior={**self.old,'observed_ms':ASOF-int(4.5*3600000),'price_ms':ASOF-int(4.5*3600000)}
        self.assertEqual(self.decide(history=[prior])['metrics']['elapsed_hours'],4.5)
        prior.update(observed_ms=ASOF-6*3600000,price_ms=ASOF-6*3600000)
        self.assertEqual(self.decide(history=[prior])['status'],'warming')

    def test_snapshot_repeats_are_not_extra_observations_and_source_input_is_unchanged(self):
        state=model.new_state();data={'AAAUSDT':self.current};before=deepcopy(data)
        model.record_history(state,'MEXC',data,CFG,ASOF);model.record_history(state,'MEXC',data,CFG,ASOF)
        self.assertEqual(len(state['history']['MEXC:AAA_USDT']),1);self.assertEqual(data,before)
        changed={'AAAUSDT':{**self.current,'oi_contracts':9999}}
        model.record_history(state,'MEXC',changed,CFG,ASOF)
        self.assertEqual(state['history']['MEXC:AAA_USDT'][0]['oi_contracts'],110)

    def test_old_history_is_pruned_but_current_references_are_not_touched(self):
        state=model.new_state();state['paper']={'fixed':'old reference'}
        model.record_history(state,'MEXC',{'AAAUSDT':self.old},CFG,ASOF+8*86400000)
        self.assertEqual(state['history'],{});self.assertEqual(state['paper'],{'fixed':'old reference'})

    def test_all_technical_eligible_rows_before_the_old_five_cap_are_available(self):
        data=scans([row('A'+str(i)+'USDT') for i in range(8)]);before=deepcopy(data)
        eligible,rejected,errors=model.technical_rows(data,POLICY,ASOF)
        self.assertEqual(len(eligible),8);self.assertEqual(rejected,[]);self.assertEqual(errors,{})
        self.assertEqual(data,before)

    def test_stale_empty_source_is_error_not_no_candidates(self):
        eligible,_,errors=model.technical_rows({'MEXC':{'feature_cutoff_ms':0,'candidates':[]}},POLICY,ASOF)
        self.assertEqual(eligible,[]);self.assertIn('MEXC',errors)

    def test_preparation_only_and_old_risk_failures_are_not_overridden(self):
        r=row();r['matched_groups']=['sideways_volume']
        eligible,rejected,_=model.technical_rows(scans([r]),POLICY,ASOF)
        self.assertEqual(eligible,[]);self.assertIn('preparation_only',rejected[0]['reasons'])

    def test_selection_is_at_most_five_symbols_never_sums_venues(self):
        decisions=[]
        for n in range(8):
            for venue in ('MEXC','OKX'):
                d=self.decide();d.update(symbol='A'+str(n)+'USDT',exchange=venue)
                decisions.append(d)
        chosen=model.select(decisions,CFG)
        self.assertEqual(len(chosen),5);self.assertEqual(len({x['symbol'] for x in chosen}),5)
        self.assertEqual(model.select([],CFG),[])

    def test_own_delivery_queue_does_not_modify_source_priority_or_old_prices(self):
        state=model.new_state();state['priority_watch']={'immutable':123};state['paper']={'reference':100}
        d={**self.decide(),'row':row()}
        model.queue(state,[d],set(),CFG,ASOF)
        self.assertEqual(state['priority_watch'],{'immutable':123});self.assertEqual(state['paper'],{'reference':100})
        self.assertEqual(len(state['pending']),1)
        model.queue(state,[],{'MEXC'},CFG,ASOF+1)
        self.assertTrue(state['pending'][0]['obsolete']);self.assertIn('AAAUSDT',state['active'])

    def test_new_paper_reference_is_current_not_a_price_inherited_from_coin_3(self):
        state=model.new_state();current=row();current.update(mid_price=101.,observed_ms=ASOF+60000)
        paper_watch.register(state,{'MEXC':{'candidates':[current]}})
        entry=state['paper']['entries']['MEXC:AAAUSDT']
        self.assertEqual(entry['entry_price'],101.);self.assertEqual(entry['observed_ms'],ASOF+60000)


class SourceTests(unittest.TestCase):
    def test_exact_catalog_mapping_does_not_alias_scaled_or_inactive_contracts(self):
        sample={'symbol':'AAA_USDT','baseCoin':'AAA','quoteCoin':'USDT','settleCoin':'USDT','futureType':1,'state':0,'contractSize':1}
        self.assertIn('AAAUSDT',sources.catalog([sample],'MEXC'))
        for change in ({'symbol':'1000AAA_USDT'},{'futureType':2},{'state':4},{'settleCoin':'BTC'}):
            self.assertEqual(sources.catalog([{**sample,**change}],'MEXC'),{})
        with self.assertRaises(ValueError):sources.catalog([sample,sample],'MEXC')

    def test_okx_requires_linear_usdt_and_correct_contract_value_currency(self):
        r={'instId':'AAA-USDT-SWAP','state':'live','instType':'SWAP','ctType':'linear','settleCcy':'USDT','ctVal':'10','ctMult':'1','ctValCcy':'AAA'}
        self.assertEqual(sources.catalog([r],'OKX')['AAAUSDT']['contract_size'],10)
        self.assertEqual(sources.catalog([{**r,'ctValCcy':'USDT'}],'OKX'),{})

    def test_only_public_gets_and_exact_contract_ids_are_allowed(self):
        for venue in ('MEXC','OKX'):
            client=sources.Public(venue);client.opener=Mock()
            with self.assertRaises(ValueError):client.get('account')
            with self.assertRaises(ValueError):client.get('funding','../../orders')
            client.opener.open.assert_not_called()

    def test_http_access_or_rate_failure_stops_that_client_not_another_venue(self):
        mexc=sources.Public('MEXC');mexc.opener=Mock()
        mexc.opener.open.side_effect=HTTPError('https://contract.mexc.com',429,'rate',{},None)
        with self.assertRaises(RuntimeError):mexc.get('ticker')
        with self.assertRaises(RuntimeError):mexc.get('ticker')
        self.assertEqual(mexc.opener.open.call_count,1);self.assertFalse(sources.Public('OKX').blocked)

    def test_funding_different_periods_are_scaled_and_missing_time_is_not_assumed_eight_hours(self):
        client=Mock();client.venue='MEXC'
        client.get.return_value={'symbol':'AAA_USDT','fundingRate':-.00005,'collectCycle':2,'nextSettleTime':ASOF+3600000,'timestamp':ASOF}
        result=sources.funding(client,market(),lambda:ASOF)
        self.assertAlmostEqual(result['scaled_8h_rate'],-.0002);self.assertEqual(result['interval_hours'],2)
        client.get.return_value.pop('collectCycle')
        with self.assertRaises(ValueError):sources.funding(client,market(),lambda:ASOF)

    def test_okx_period_uses_previous_and_current_funding_times_and_identity(self):
        client=Mock();client.venue='OKX'
        client.get.return_value=[{'instId':'AAA-USDT-SWAP','fundingRate':'-.0001','fundingTime':ASOF+3600000,'prevFundingTime':ASOF-3600000,'ts':ASOF}]
        result=sources.funding(client,market('OKX'),lambda:ASOF);self.assertEqual(result['interval_hours'],2)
        client.get.return_value[0]['instId']='BBB-USDT-SWAP'
        with self.assertRaises(ValueError):sources.funding(client,market('OKX'),lambda:ASOF)

    def test_stale_funding_timestamp_or_wrong_settlement_interval_cannot_pass(self):
        client=Mock();client.venue='MEXC'
        client.get.return_value={'symbol':'AAA_USDT','fundingRate':-.001,'collectCycle':8,'nextSettleTime':ASOF+3600000,'timestamp':ASOF-6*60000}
        with self.assertRaises(ValueError):sources.funding(client,market(),lambda:ASOF)
        client.get.return_value.update(timestamp=ASOF,nextSettleTime=ASOF+20*3600000)
        with self.assertRaises(ValueError):sources.funding(client,market(),lambda:ASOF)


class IntegrationTests(unittest.TestCase):
    def test_first_run_warms_then_four_hours_later_can_register_one_new_squeeze_price(self):
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory);statefile=out/'state.json'
            state=model.new_state();statefile.write_text(json.dumps(state),encoding='utf-8')
            source={'branch':'scanner-state-v5','commit':'unchanged-source','source_updated_ms':ASOF,'scans':scans([row()])}
            (out/'source.json').write_text(json.dumps(source),encoding='utf-8')
            def collect(venue,rows,cfg):
                return {'markets':{'AAAUSDT':market(stamp=scan.now_ms(),oi=100 if scan.now_ms()==ASOF else 110)} if venue=='MEXC' else {},
                    'funding':{'AAAUSDT':funding(stamp=scan.now_ms())},'listed_contracts':['AAAUSDT'],'errors':[],'calls':3,'funding_checked':1}
            with patch.object(scan,'OUT',out),patch.object(scan,'STATE',statefile),patch.object(scan.priority,'refresh_quotes',side_effect=deepcopy),\
                 patch.object(scan,'collect',side_effect=collect),patch.object(scan,'now_ms',return_value=ASOF):
                scan.scan();first=json.loads(statefile.read_text(encoding='utf-8'))
                self.assertEqual(first['latest']['selected'],[]);self.assertEqual(first['paper']['entries'],{})
                self.assertEqual(first['latest']['decisions'][0]['status'],'warming')
                later=ASOF+4*3600000;source['scans']['MEXC']['feature_cutoff_ms']+=4*3600000
                source['scans']['MEXC']['candidates'][0]['observed_ms']=later
                (out/'source.json').write_text(json.dumps(source),encoding='utf-8')
                with patch.object(scan,'now_ms',return_value=later):scan.scan()
                second=json.loads(statefile.read_text(encoding='utf-8'))
                self.assertEqual(len(second['latest']['selected']),1)
                self.assertEqual(second['paper']['entries']['MEXC:AAAUSDT']['observed_ms'],later)
                self.assertEqual(json.loads((out/'source.json').read_text(encoding='utf-8')),source)
                self.assertIn('erken',scan.measurements(second).casefold())

    def test_notification_is_distinct_mentions_user_and_reconciles_duplicate_delivery(self):
        current=market();prior=market(stamp=ASOF-4*3600000,oi=100)
        d=model.decide(row(),current,funding(),[prior],CFG,ASOF);d['row']=row()
        state=model.new_state();model.queue(state,[d],set(),CFG,ASOF)
        sent=[]
        def http(url,payload=None,headers=None,label=None):
            if payload is None:return []
            sent.append(payload);return {'number':1}
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(scan,'STATE',path),patch.object(scan,'now_ms',return_value=ASOF),patch.object(scan.cloud,'http_json',side_effect=http),\
                patch.dict(os.environ,{'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'fake-test-only','COIN_NOTIFY_USER':'recipient'}):
                scan.notify('github_issue');scan.notify('github_issue')
            self.assertEqual(len(sent),1);self.assertIn('Shortçu Kıstır',sent[0]['title'])
            self.assertIn('@recipient',sent[0]['body']);self.assertIn('toplam OI',sent[0]['body'])
            self.assertIn('scanner-state-shortcu-kistir',sent[0]['body'])

    def test_old_pending_issues_reconcile_before_new_delivery_and_never_send_stale_prices(self):
        state=model.new_state();d={'symbol':'AAAUSDT','row':row()}
        state['pending']=[{'id':'delivered','created_ms':ASOF,'candidates':[d],'obsolete':True}]
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(scan,'STATE',path),patch.object(scan,'now_ms',return_value=ASOF),\
                patch.object(scan.cloud,'http_json',return_value=[{'body':'<!-- shortcu-kistir:delivered -->'}]) as http,\
                patch.dict(os.environ,{'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'fake-test-only'}):scan.notify('github_issue')
            final=json.loads(path.read_text(encoding='utf-8'));self.assertEqual(final['pending'],[])
            self.assertEqual(final['last_sent']['AAAUSDT'],ASOF);self.assertEqual(http.call_count,1)

    def test_existing_scanner_branch_is_refused(self):
        with patch.dict(os.environ,{'SCANNER_STATE_BRANCH':'scanner-state-v5'}):
            with self.assertRaises(ValueError):scan.configure()

if __name__=='__main__':unittest.main()
