from copy import deepcopy
import json,os,unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock,patch
from urllib.error import HTTPError
import short_squeeze_positions as data
import short_squeeze_monitor as monitor

CFG=monitor.cfg();BASE=57600000;NOW=BASE+60000


def point(short,ts=BASE,provider='OKX'):
    return {'status':'observed','provider':provider,'scope':data.SCOPES[provider],'symbol':'AAAUSDT',
        'contract':'AAA-USDT-SWAP' if provider=='OKX' else 'AAAUSDT','period':'5m',
        'ratio_long_over_short':100/short-1 if short else 1e300,'long_pct':100-short,'short_pct':short,
        'provider_ms':ts,'observed_ms':ts+60000,'is_market_wide':False,'is_account_count':False}


def ref():
    return {'id':'reference','symbol':'AAAUSDT','origin_venue':'MEXC','reference_ms':BASE,'reference_price':100,
        'notified_ms':NOW,'expires_ms':NOW+24*3600000}


def source_state():
    return {'last_sent':{'AAAUSDT':NOW},'latest':{'selected':[{'symbol':'AAAUSDT','exchange':'MEXC',
        'row':{'observed_ms':BASE,'mid_price':100}}]},'paper':{'entries':{}}}


class RatioChecks(unittest.TestCase):
    def test_positions_ratio_converts_to_short_and_long_not_account_count(self):
        parsed=data.parse('OKX','AAAUSDT',{'code':'0','data':[[str(BASE),str(2/3)]]},NOW,CFG)
        self.assertAlmostEqual(parsed['short_pct'],60);self.assertAlmostEqual(parsed['long_pct'],40)
        self.assertFalse(parsed['is_market_wide']);self.assertFalse(parsed['is_account_count'])

    def test_binance_uses_position_endpoint_semantics_and_validates_legacy_field_names(self):
        rows=[{'symbol':'AAAUSDT','longShortRatio':'1.5','longAccount':'.6','shortAccount':'.4','timestamp':BASE}]
        parsed=data.parse('BINANCE','AAAUSDT',rows,NOW,CFG)
        self.assertEqual(parsed['short_pct'],40);self.assertIn('%20',parsed['scope'])
        rows[0]['longAccount']='.9'
        with self.assertRaises(ValueError):data.parse('BINANCE','AAAUSDT',rows,NOW,CFG)

    def test_provider_rows_are_sorted_and_future_points_do_not_repaint_a_previous_value(self):
        rows=[[BASE,'1.5'],[BASE+300000,'.5'],[BASE-300000,'2']]
        result=data.parse('OKX','AAAUSDT',{'code':'0','data':rows},NOW,CFG)
        self.assertEqual(result['provider_ms'],BASE);self.assertEqual(result['short_pct'],40)

    def test_conflicting_timestamp_missing_negative_or_nonfinite_ratio_are_unknown(self):
        for rows in ([[BASE,'1'],[BASE,'2']],[[BASE,None]],[[BASE,'NaN']],[[BASE,'-1']]):
            with self.assertRaises(ValueError):data.parse('OKX','AAAUSDT',{'code':'0','data':rows},NOW,CFG)
        with self.assertRaises(ValueError):data.parse('OKX','AAAUSDT',{'code':'0','data':[]},NOW,CFG)

    def test_stale_time_or_wrong_contract_cannot_be_presented_as_current(self):
        with self.assertRaises(ValueError):data.parse('OKX','AAAUSDT',{'code':'0','data':[[BASE-20*60000,'1']]},NOW,CFG)
        with self.assertRaises(ValueError):data.parse('BINANCE','AAAUSDT',[{'symbol':'BBBUSDT'}],NOW,CFG)

    def test_percentage_points_and_relative_change_are_distinct(self):
        result=data.change(point(60),point(65,BASE+300000))
        self.assertEqual(result['short_change_pp'],5);self.assertAlmostEqual(result['short_relative_change_pct'],8.3333333)
        self.assertEqual(result['elapsed_minutes'],5)
        result=data.change(point(60),point(54,BASE+600000))
        self.assertEqual(result['short_change_pp'],-6);self.assertEqual(result['short_relative_change_pct'],-10)

    def test_zero_previous_short_share_has_no_invented_relative_percentage(self):
        result=data.change(point(0),point(3,BASE+300000))
        self.assertIsNone(result['short_relative_change_pct']);self.assertEqual(result['short_change_pp'],3)

    def test_different_provider_populations_or_same_timestamp_cannot_be_compared(self):
        with self.assertRaises(ValueError):data.change(point(60),point(65,BASE+300000,'BINANCE'))
        with self.assertRaises(ValueError):data.change(point(60),point(65))

    def test_only_meaningful_changes_or_crossing_fifty_trigger(self):
        self.assertFalse(data.meaningful(data.change(point(60),point(61.5,BASE+300000)),CFG))
        self.assertTrue(data.meaningful(data.change(point(60),point(62,BASE+300000)),CFG))
        self.assertTrue(data.meaningful(data.change(point(49.8),point(50.1,BASE+300000)),CFG))


class TargetAndStateChecks(unittest.TestCase):
    def test_only_actually_delivered_candidates_start_monitoring(self):
        source=source_state();source['last_sent']={}
        self.assertEqual(monitor.targets(source,monitor.new_state(),NOW,CFG)[0],[])
        source=source_state();targets,stats=monitor.targets(source,monitor.new_state(),NOW,CFG)
        self.assertEqual(len(targets),1);self.assertEqual(targets[0]['origin_venue'],'MEXC')

    def test_cached_original_alert_is_retained_when_latest_production_list_moves_on(self):
        state=monitor.new_state();r=ref();state['assets'][r['id']]={'ref':r,'profiles':{}}
        source=source_state();source['latest']['selected']=[]
        targets,_=monitor.targets(source,state,NOW+4*3600000,CFG)
        self.assertEqual(targets[0]['reference_ms'],BASE)
        self.assertEqual(monitor.targets(source,state,NOW+25*3600000,CFG)[0],[])

    def test_reentry_never_uses_an_old_paper_price_as_new_delivery_reference(self):
        source=source_state();source['last_sent']['AAAUSDT']=NOW+48*3600000
        source['paper']['entries']={'MEXC:AAAUSDT':{'symbol':'AAAUSDT','exchange':'MEXC','observed_ms':BASE,'entry_price':1}}
        targets,stats=monitor.targets(source,monitor.new_state(),NOW+48*3600000,CFG)
        self.assertEqual(targets,[]);self.assertEqual(stats['unresolved_references'],1)

    def test_reentry_uses_matching_cached_delivery_even_if_old_asset_sorts_later(self):
        source=source_state();source['latest']['selected']=[];newtime=NOW+48*3600000;source['last_sent']['AAAUSDT']=newtime
        newref={**ref(),'id':'new','notified_ms':newtime,'reference_ms':newtime,'expires_ms':newtime+24*3600000}
        state=monitor.new_state();state['assets']={'new':{'ref':newref},'old':{'ref':ref()}}
        targets,_=monitor.targets(source,state,newtime,CFG)
        self.assertEqual(targets[0]['notified_ms'],newtime)

    def test_first_live_point_establishes_baseline_without_backfilled_notification(self):
        state=monitor.new_state();monitor.update(state,ref(),'OKX',point(60),NOW,CFG)
        self.assertEqual(state['pending'],[]);self.assertEqual(state['assets']['reference']['profiles']['OKX']['anchor']['short_pct'],60)

    def test_small_changes_accumulate_from_last_notified_anchor(self):
        state=monitor.new_state();r=ref()
        monitor.update(state,r,'OKX',point(60),NOW,CFG)
        monitor.update(state,r,'OKX',point(61,BASE+300000),NOW+300000,CFG)
        self.assertEqual(state['pending'],[])
        monitor.update(state,r,'OKX',point(62.5,BASE+600000),NOW+600000,CFG)
        self.assertAlmostEqual(state['pending'][0]['delta']['short_change_pp'],2.5)

    def test_same_period_revision_or_unknown_data_does_not_reset_baseline_or_alert(self):
        state=monitor.new_state();r=ref()
        monitor.update(state,r,'OKX',point(60),NOW,CFG)
        monitor.update(state,r,'OKX',point(65),NOW+10000,CFG)
        monitor.update(state,r,'OKX',{'status':'unknown','reason':'stale'},NOW+20000,CFG)
        p=state['assets']['reference']['profiles']['OKX']
        self.assertEqual(state['pending'],[]);self.assertEqual(p['anchor']['short_pct'],60);self.assertEqual(p['revisions'],1)

    def test_not_delivered_change_is_retried_at_same_fresh_provider_point(self):
        state=monitor.new_state();r=ref();monitor.update(state,r,'OKX',point(60),NOW,CFG)
        newer=point(65,BASE+300000);monitor.update(state,r,'OKX',newer,NOW+300000,CFG)
        identifier=state['pending'][0]['id'];state['pending']=[]
        monitor.update(state,r,'OKX',newer,NOW+310000,CFG)
        self.assertEqual(state['pending'][0]['id'],identifier)

    def test_sources_are_kept_separate_and_never_average_percentages(self):
        state=monitor.new_state();r=ref()
        monitor.update(state,r,'OKX',point(60),NOW,CFG)
        monitor.update(state,r,'BINANCE',point(30,provider='BINANCE'),NOW,CFG)
        monitor.update(state,r,'OKX',point(65,BASE+300000),NOW+300000,CFG)
        self.assertEqual(state['pending'][0]['provider'],'OKX')
        self.assertEqual(state['assets']['reference']['profiles']['BINANCE']['anchor']['short_pct'],30)

    def test_provider_timestamp_gaps_are_reported_as_real_elapsed_time(self):
        state=monitor.new_state();r=ref()
        monitor.update(state,r,'OKX',point(60),NOW,CFG)
        monitor.update(state,r,'OKX',point(65,BASE+1800000),NOW+1800000,CFG)
        self.assertEqual(state['pending'][0]['delta']['elapsed_minutes'],30)


class PublicClientChecks(unittest.TestCase):
    def test_private_endpoints_and_malformed_symbols_are_rejected_before_network(self):
        for provider in data.SCOPES:
            client=data.Client(provider);client.opener=Mock()
            with self.assertRaises(ValueError):client.get('account')
            with self.assertRaises(ValueError):client.get('ratio','../orders')
            client.opener.open.assert_not_called()

    def test_access_rate_and_region_rejections_stop_requests_without_fallback_hosts(self):
        for status in (401,403,429,451):
            client=data.Client('BINANCE');client.opener=Mock()
            client.opener.open.side_effect=HTTPError('https://fapi.binance.com',status,'unavailable',{},None)
            with self.assertRaises(RuntimeError):client.get('catalog')
            with self.assertRaises(RuntimeError):client.get('catalog')
            self.assertEqual(client.opener.open.call_count,1)

    def test_unsupported_scaled_symbol_is_not_mapped_to_unscaled_coin(self):
        client=data.Client('BINANCE');client.catalog={'1000AAAUSDT':'1000AAAUSDT'}
        client.get=Mock()
        result=client.read('AAAUSDT',lambda:NOW,CFG)
        self.assertEqual(result['status'],'unsupported');client.get.assert_not_called()


class NotificationChecks(unittest.TestCase):
    def setup_event(self):
        state=monitor.new_state();r=ref();state['active']=['reference']
        monitor.update(state,r,'OKX',point(60),NOW,CFG)
        monitor.update(state,r,'OKX',point(65,BASE+300000),NOW+300000,CFG)
        return state

    def test_message_contains_actual_percentage_delta_scope_and_both_times(self):
        text=monitor.event_text(self.setup_event()['pending'][0])
        for expected in ('%60.00','%65.00','+5.00 yüzde puan','+8.33','Son long payı: %35.00','%5','Veri:','Kontrol:'):
            self.assertIn(expected,text)
        self.assertIn('MEXC toplamının oranı değildir',text)

    def test_bot_issue_is_distinct_and_confirmed_delivery_moves_only_monitor_anchor(self):
        state=self.setup_event();sent=[]
        def http(url,payload=None,headers=None,label=None):
            if payload is None:return []
            sent.append(payload);return {'number':1}
        with TemporaryDirectory() as directory:
            out=Path(directory);path=out/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            state['latest']={'observed_ms':NOW+300000,'active_symbols':1,'coverage':{},'errors':[]}
            path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(monitor,'OUT',out),patch.object(monitor,'STATE',path),patch.object(monitor,'now_ms',return_value=NOW+300000),\
                patch.object(monitor.cloud,'http_json',side_effect=http),patch.dict(os.environ,{'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'fake-test','COIN_NOTIFY_USER':'recipient'}):
                monitor.notify('github_issue');monitor.notify('github_issue')
            final=json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(len(sent),1);self.assertIn('@recipient',sent[0]['body']);self.assertIn('Pozisyon oranı değişimi',sent[0]['title'])
        self.assertEqual(final['assets']['reference']['profiles']['OKX']['anchor']['short_pct'],65)

    def test_reconciliation_of_accepted_post_happens_before_next_delta(self):
        state=self.setup_event();event=state['pending'][0]
        existing=[{'body':'<!-- shortcu-position-event:'+event['id']+' -->','user':{'login':'github-actions[bot]'}}]
        with patch.object(monitor.cloud,'http_json',return_value=existing),patch.dict(os.environ,{'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'fake-test'}):monitor.reconcile(state,'github_issue')
        self.assertEqual(state['pending'],[])
        monitor.update(state,ref(),'OKX',point(66,BASE+600000),NOW+600000,CFG)
        self.assertEqual(state['pending'],[])

    def test_first_empty_live_scan_never_contacts_provider_or_posts_a_message(self):
        with TemporaryDirectory() as directory:
            out=Path(directory);path=out/'state.json';path.write_text(json.dumps(monitor.new_state()),encoding='utf-8')
            source={'commit':'read-only','data':{'last_sent':{},'latest':{'selected':[]},'paper':{'entries':{}}}}
            (out/'source.json').write_text(json.dumps(source),encoding='utf-8')
            with patch.object(monitor,'OUT',out),patch.object(monitor,'STATE',path),patch.object(monitor,'now_ms',return_value=NOW),\
                patch.object(monitor.positions.Client,'read') as read,patch.object(monitor.cloud,'http_json') as post:
                monitor.observe('github_issue');monitor.notify('github_issue');read.assert_not_called();post.assert_not_called()
            self.assertEqual(json.loads((out/'source.json').read_text(encoding='utf-8')),source)
            self.assertEqual(json.loads(path.read_text(encoding='utf-8'))['pending'],[])

    def test_original_scanner_state_branch_is_refused(self):
        with patch.dict(os.environ,{'SCANNER_STATE_BRANCH':'scanner-state-shortcu-kistir'}):
            with self.assertRaises(ValueError):monitor.configure()

if __name__=='__main__':unittest.main()
