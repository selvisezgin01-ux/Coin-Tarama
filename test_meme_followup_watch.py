from copy import deepcopy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock,patch
import os

import meme_followup_watch as watch
import meme_scan as meme
import meme_social_watch as social
from test_meme_scan import CONFIG


class FollowupChecks(unittest.TestCase):
    def setUp(self):
        self.asset={'chain':'ethereum','mint':'0x'+'1'*40,'pool':'0x'+'2'*40,'symbol':'TEST','price_usd':.01,'price_observed_ms':1000}

    def trade(self,identity,kind,wallet='0x'+'3'*40,volume='10',date='1970-01-01T00:30:00Z'):
        return {'id':identity,'attributes':{'block_timestamp':date,'tx_hash':'same-transaction','tx_from_address':wallet,
            'from_token_address':self.asset['mint'] if kind=='sell' else '0x'+'4'*40,
            'to_token_address':self.asset['mint'] if kind=='buy' else '0x'+'4'*40,'volume_in_usd':volume}}

    def test_multiple_trades_in_one_transaction_are_preserved_and_ids_deduplicated(self):
        rows=[self.trade('a','buy'),self.trade('b','buy'),self.trade('a','buy'),self.trade('c','sell')]
        sample=watch.trade_sample({'data':rows},self.asset,30*60000)['windows']['15']
        self.assertEqual(sample['observed_buy_trades'],2);self.assertEqual(sample['observed_sell_trades'],1)
        self.assertEqual(sample['net_buy_volume_usd'],10);self.assertEqual(sample['unique_observed_buyers'],1)
        self.assertEqual(sample['both_sides_initiators'],1);self.assertFalse(sample['complete_onchain_coverage'])

    def test_missing_dollar_volume_does_not_become_zero_net_flow(self):
        sample=watch.trade_sample({'data':[self.trade('a','buy',volume=None)]},self.asset,30*60000)
        self.assertIsNone(sample['windows']['15']['net_buy_volume_usd'])
        self.assertFalse(sample['windows']['15']['returned_span_reaches_window_start'])
        self.assertEqual(watch.trade_sample({'data':[]},self.asset,30*60000)['status'],'unknown')

    def test_truncated_sample_does_not_claim_complete_coverage_or_independent_people(self):
        sample=watch.trade_sample({'data':[self.trade(str(i),'buy') for i in range(300)]},self.asset,30*60000)
        self.assertTrue(sample['row_limit_reached']);self.assertFalse(sample['windows']['30']['complete_onchain_coverage'])
        self.assertEqual(sample['windows']['30']['unique_observed_buyers'],1)

    def test_holder_changes_require_same_provider_actual_times_and_do_not_invent_missing_data(self):
        record={};watch.holder_observation(record,{'source':'A','holder_count':100},0)
        result=watch.holder_observation(record,{'source':'B','holder_count':500},15*60000)
        self.assertEqual(result['comparisons'],{})
        result=watch.holder_observation(record,{'source':'A','holder_count':105},17*60000)
        self.assertEqual(result['comparisons']['15']['change'],5)
        self.assertEqual(result['comparisons']['15']['elapsed_minutes'],17)
        self.assertIsNone(watch.holder_observation(record,{},18*60000)['count'])

    def test_raw_amount_uses_decimal_floor_and_rejects_invalid_units(self):
        self.assertEqual(watch.decimal_units(100,.003,6),'33333333333')
        for decimals in [None,True,37,-1]:
            with self.assertRaises(ValueError):watch.decimal_units(100,1,decimals)
        with self.assertRaises(ValueError):watch.decimal_units(100,0,6)

    def test_wrong_token_amount_or_stale_quote_does_not_become_a_valid_exit(self):
        route={'tokenIn':self.asset['mint'],'tokenOut':watch.NATIVE,'amountIn':'100','amountOut':'1000',
               'amountOutUsd':'0','gasUsd':'0','timestamp':1000,'route':[[{'pool':'pool'}]]}
        data={'code':0,'data':{'routeSummary':route}}
        result=watch.parse_route(data,self.asset,'100',1000000)
        self.assertIsNone(result['output_usd']);self.assertIsNone(result['gas_usd'])
        self.assertFalse(result['tax_inclusion_verified'])
        with self.assertRaises(ValueError):watch.parse_route(data,self.asset,'101',1000000)
        with self.assertRaises(ValueError):watch.parse_route(data,self.asset,'100',1200001)
        route['tokenIn']='0x'+'7'*40
        with self.assertRaises(ValueError):watch.parse_route(data,self.asset,'100',1000000)

    def test_solana_usdc_is_not_silently_dollar_priced_and_gas_is_unknown(self):
        asset={'chain':'solana','mint':'SolMint'}
        data={'success':True,'data':{'swapType':'BaseIn','inputMint':'SolMint','inputAmount':'10',
             'outputMint':watch.USDC_SOL,'outputAmount':'1234567','priceImpactPct':.1,'routePlan':[{'poolId':'pool'}]}}
        result=watch.parse_route(data,asset,'10',1000)
        self.assertEqual(result['output_units'],'1.234567');self.assertIsNone(result['output_usd'])
        self.assertIsNone(result['gas_usd']);self.assertFalse(result['price_impact_unit_verified'])

    def test_missing_rpc_metadata_does_not_create_fabricated_quotes(self):
        client=Mock();client.rpc.return_value='0x38'
        result=watch.exit_quotes(client,CONFIG['networks']['ethereum'],self.asset,{})
        self.assertEqual([r['status'] for r in result],['unknown','unknown']);client.request.assert_not_called()

    def test_repeated_warning_and_unknown_observation_do_not_spam_or_clear_risk(self):
        state={'pending':[]};record={**self.asset}
        watch.risk_event(state,record,'developer_outflow',True,1000,True,'Transfer, not sale proof')
        watch.risk_event(state,record,'developer_outflow',None,2000,True,'unknown')
        watch.risk_event(state,record,'developer_outflow',True,3000,True,'repeat')
        self.assertEqual(len(state['pending']),1);self.assertTrue(record['flags']['developer_outflow'])
        watch.risk_event(state,record,'developer_outflow',False,4000,True,'known window clear')
        watch.risk_event(state,record,'developer_outflow',True,5000,True,'new episode')
        self.assertEqual(len(state['pending']),2);self.assertNotEqual(state['pending'][0]['id'],state['pending'][1]['id'])

    def test_no_qualified_entries_means_no_network_calls_or_unfiltered_tokens_in_report(self):
        state={'entries':{},'assets':{}};client=Mock()
        result=watch.annotate(state,CONFIG,client)
        self.assertEqual(result['last_run']['checked'],0);self.assertEqual(client.mock_calls,[])
        with TemporaryDirectory() as directory,patch.object(meme,'OUT',Path(directory)):
            (meme.OUT/'report.md').write_text('# Report\n',encoding='utf-8');watch.append_report(state)
            self.assertIn('Henüz ön eleme adayı yok',(meme.OUT/'report.md').read_text(encoding='utf-8'))

    def test_queued_first_alert_gets_warning_in_message_without_second_issue(self):
        pending={'pending':[]};record={**self.asset}
        watch.risk_event(pending,record,'liquidity_withdrawal',True,1000,False,'loss')
        self.assertEqual(pending['pending'],[]);self.assertEqual(len(record['events']),1)

    def test_zero_creator_balance_is_still_checked_and_original_pool_is_preserved(self):
        key=meme.key_of(self.asset);creator='0x'+'6'*40
        entry={'chain':'ethereum','mint':self.asset['mint'],'symbol':'TEST','first_pool':self.asset['pool'],
               'references':{'qualified':{'observed_ms':1000,'price':.01,'stage':'accumulation'}},'alerted_stages':['accumulation']}
        state={'entries':{key:entry},'assets':{key:{'latest':{**self.asset,'pool':'0x'+'9'*40},'security':{'creator':creator}}},'pending':[]}
        before=deepcopy(entry);fresh={**self.asset,'liquidity_usd':20000}
        sec={'creator':creator,'creator_pct':0,'source':'GoPlus','complete':True,'blocked':False,'holder_count':100}
        client=Mock();client.gecko.return_value={'data':[]}
        with patch.object(meme,'now_ms',return_value=2000),patch.object(meme.source,'refresh_pools',return_value=[fresh]) as refresh,\
             patch.object(meme.security_api,'fetch_security',return_value=sec),\
             patch.object(meme.security_api,'developer_evm',return_value={'status':'outgoing_transfer_detected'}) as dev,\
             patch.object(watch,'exit_quotes',return_value=[]):
            result=watch.annotate(state,CONFIG,client)
        self.assertEqual(refresh.call_args.args[-1],[self.asset['pool']])
        self.assertEqual(dev.call_args.args[3],creator)
        self.assertEqual(result['pending'][0]['kind'],'developer_outflow')
        self.assertEqual(state['entries'][key],before)

    def test_quote_collection_only_reads_routes_and_never_builds_or_sends_transactions(self):
        client=Mock();client.request.return_value={'code':0,'data':{'routeSummary':{'tokenIn':self.asset['mint'],
            'tokenOut':watch.NATIVE,'amountIn':'10000000000','amountOut':'1000','amountOutUsd':'99','gasUsd':'1',
            'timestamp':1000,'route':[[{'pool':'test'}]]}}}
        with patch.object(watch,'read_decimals',return_value=6),patch.object(meme,'now_ms',return_value=1000000):
            rows=watch.exit_quotes(client,CONFIG['networks']['ethereum'],self.asset,{})
        self.assertEqual(rows[0]['status'],'indicative_route')
        self.assertEqual(rows[1]['status'],'unknown') # Deliberately wrong amount in second provider response.
        for call in client.request.call_args_list:
            self.assertEqual(len(call.args),1);self.assertIn('/api/v1/routes?',call.args[0])
            self.assertNotIn('payload',call.kwargs);self.assertNotIn('wallet',call.args[0])

    def test_notification_wrappers_preserve_manual_map_social_notes_and_clear_pending_once(self):
        row={**self.asset,'stage':'accumulation','observed_ms':1000}
        state={'entries':{},'pending':[{'id':'testbatch','created_ms':1000,'candidates':[row]}]}
        social.social_state(state);followup=watch.followup_state(state)
        followup['tokens'][meme.key_of(row)]={**self.asset,'latest':{'holders':{'count':100},'exit_quotes':[]}}
        sent=[]
        def http(url,body=None,headers=None,label=None):
            if body is None:return []
            sent.append(body);return {'number':123}
        with TemporaryDirectory() as directory:
            path=Path(directory)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(meme,'STATE',path),patch.object(meme.cloud,'http_json',side_effect=http),patch.dict(os.environ,
                {'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'unit-test-only','COIN_NOTIFY_USER':'test-user'}):watch.notify()
            self.assertEqual(json.loads(path.read_text(encoding='utf-8'))['pending'],[])
        self.assertEqual(len(sent),1);self.assertIn('MANUEL KONTROL EDİLMELİ',sent[0]['body'])
        self.assertIn('Sosyal hesap gözlemleri',sent[0]['body']);self.assertIn('Ek ölçümler',sent[0]['body'])


if __name__=='__main__':unittest.main()
