from copy import deepcopy
from pathlib import Path
import unittest
from unittest.mock import patch
import os

import meme_rules as rules
import meme_security as security
import meme_scan as scan
import meme_sources as sources

CONFIG=__import__('json').loads(Path(__file__).with_name('meme_config.json').read_text(encoding='utf-8'))


def candle(i,opening=1.,high=1.05,low=.98,close=1.02,volume=2000.):
    return [i*900,opening,high,low,close,volume]


class MemeChecks(unittest.TestCase):
    def test_open_candle_is_not_a_signal_and_future_does_not_repaint_past(self):
        rows=[candle(0,volume=4000),candle(1,volume=3000),candle(2,volume=2000),candle(3,close=1.04,volume=999999)]
        first=rules.closed_candles(rows,3*rules.STEP_MS)
        self.assertEqual(len(first),3)
        changed=deepcopy(rows);changed[3]=candle(3,high=10,close=9,volume=1000000)
        self.assertEqual(first,rules.closed_candles(changed,3*rules.STEP_MS))

    def test_gap_restarts_features_instead_of_filling_missing_trades(self):
        rows=[candle(0),candle(1),candle(3)]
        self.assertEqual(len(rules.closed_candles(rows,4*rules.STEP_MS)),1)
        with self.assertRaises(ValueError):rules.closed_candles([candle(0),candle(0,volume=999)],rules.STEP_MS)

    def test_accumulation_requires_declining_volume_and_tight_price(self):
        rows=[candle(0,volume=4000),candle(1,volume=3000),candle(2,volume=2000)]
        bars=rules.closed_candles(rows,3*rules.STEP_MS)
        self.assertEqual(rules.pattern(bars,CONFIG)['stage'],'accumulation')
        bars[-1]['volume']=5000
        self.assertIsNone(rules.pattern(bars,CONFIG)['stage'])

    def test_first_breakout_requires_volume_and_strong_close(self):
        rows=[candle(0,volume=4000),candle(1,volume=3000),candle(2,volume=2000),candle(3,opening=1.02,high=1.10,low=1.01,close=1.09,volume=6000)]
        bars=rules.closed_candles(rows,4*rules.STEP_MS)
        self.assertEqual(rules.pattern(bars,CONFIG)['stage'],'first_breakout')
        bars[-1]['high']=1.5
        self.assertNotEqual(rules.pattern(bars,CONFIG)['stage'],'first_breakout')

    def test_zero_volume_and_previous_big_pump_do_not_create_setup(self):
        rows=[candle(0,volume=0),candle(1,volume=0),candle(2,volume=0),candle(3)]
        self.assertIsNone(rules.pattern(rules.closed_candles(rows,4*rules.STEP_MS),CONFIG)['stage'])
        rows=[candle(0,high=2,close=1.8),candle(1,volume=4000),candle(2,volume=3000),candle(3,volume=2000)]
        self.assertEqual(rules.pattern(rules.closed_candles(rows,4*rules.STEP_MS),CONFIG)['reason'],'large_pump_already_in_available_history')

    def test_missing_security_or_map_never_becomes_qualified(self):
        market={'failed':[],'passed':True,'valuation_kind':'market_cap_provider_reported'}
        setup={'stage':'accumulation'}
        dev={'status':'no_outgoing_transfers_in_complete_window'}
        self.assertEqual(rules.tier(market,setup,{'complete':True},dev,{'complete':False}),'review')
        self.assertEqual(rules.tier(market,setup,{'complete':False,'unknown':['is_honeypot']},dev,{'complete':True}),'review')
        self.assertEqual(rules.tier(market,setup,{'complete':True},dev,{'complete':True}),'qualified')
        self.assertEqual(rules.tier(market,setup,{'complete':True},{'status':'outgoing_transfer_detected'},{'complete':True}),'rejected')
        market['valuation_kind']='fdv_proxy'
        self.assertEqual(rules.tier(market,setup,{'complete':True},dev,{'complete':True}),'review')

    def test_market_cap_and_fdv_are_separate_and_missing_volume_not_zero(self):
        asset={'pool_created_ms':0,'liquidity_usd':20000,'market_cap_usd':None,'fdv_usd':200000,
               'volume15_usd':2000,'buys15':18,'sells15':10}
        gate=rules.market_gates(asset,CONFIG,2*3600000,[])
        self.assertTrue(gate['passed']);self.assertEqual(gate['valuation_kind'],'fdv_proxy')
        asset.pop('volume15_usd');self.assertIn('volume15',rules.market_gates(asset,CONFIG,2*3600000,[])['unknown'])

    def test_liquidity_withdrawal_and_weak_buy_flow_are_rejected(self):
        asset={'pool_created_ms':0,'liquidity_usd':20000,'market_cap_usd':200000,'volume15_usd':2000,'buys15':18,'sells15':10}
        old=[{'ms':2*3600000-60000,'liquidity':40000}]
        self.assertIn('liquidity_withdrawal',rules.market_gates(asset,CONFIG,2*3600000,old)['failed'])
        asset['buys15']=10
        self.assertIn('transaction_flow15',rules.market_gates(asset,CONFIG,2*3600000,[])['failed'])

    def test_pool_owner_is_excluded_but_unknown_contract_is_not(self):
        holders=[{'owner':'pool','pct':70.}]+[{'owner':'owner'+str(i),'pct':2.} for i in range(10)]
        parsed=security.concentration(holders,{'pool'},'solana',CONFIG)
        self.assertFalse(parsed['holder_concentration_blocked']);self.assertEqual(parsed['top10_owner_pct'],20.)
        holders.append({'owner':'unidentified_contract','pct':11.})
        self.assertTrue(security.concentration(holders,{'pool'},'solana',CONFIG)['holder_concentration_blocked'])

    def test_multiple_accounts_of_one_owner_are_aggregated(self):
        parsed=security.concentration([{'owner':'same','pct':6.},{'owner':'same','pct':6.}],set(),'solana',CONFIG)
        self.assertTrue(parsed['holder_concentration_blocked']);self.assertEqual(parsed['largest_owner_pct'],12.)

    def test_map_units_and_timestamp_must_be_verified(self):
        nodes=[{'address':'holder'+str(i),'holder_data':{'amount':30.,'share':.03},'address_details':{}} for i in range(12)]
        data={'metadata':{'ts_update':1000},'nodes':{'top_holders':nodes},'clusters':[{'holders':['holder0','holder1']}]}
        parsed=security.parse_map(data,{'supply_normalized':1000.},1000000,CONFIG)
        self.assertTrue(parsed['complete']);self.assertEqual(parsed['largest_cluster_pct'],6.)
        self.assertFalse(security.parse_map(data,{},1000000,CONFIG)['complete'])
        self.assertFalse(security.parse_map(data,{'supply_normalized':1000.},1000000+16*60000,CONFIG)['complete'])
        data['clusters'][0]['holders']=[n['address'] for n in nodes]
        self.assertTrue(security.parse_map(data,{'supply_normalized':1000.},1000000,CONFIG)['blocked'])

    def test_absent_api_key_does_not_call_map_provider(self):
        with patch.dict(os.environ,{},clear=True):
            client=unittest.mock.Mock()
            result=security.fetch_map(client,{'chain':'solana','mint':'test'}, {},0,{})
            self.assertFalse(result['complete']);client.request.assert_not_called()

    def test_goplus_fraction_is_percent_and_lp_is_not_inferred_from_aggregate(self):
        report={'holders':[{'address':'0x'+'2'*40,'percent':'0.15'}],'lp_holders':[{'is_locked':1,'percent':'1'}]}
        result=security.parse_goplus(report,{'chain':'ethereum','pool':'0x'+'1'*40},CONFIG)
        self.assertEqual(result['largest_owner_pct'],15.)
        self.assertTrue(result['blocked']);self.assertIsNone(result['liquidity_lock']['locked_pct'])

    def test_chain_mint_identity_never_uses_symbol(self):
        self.assertNotEqual(scan.key_of({'chain':'solana','mint':'Abc'}),scan.key_of({'chain':'solana','mint':'abc'}))
        self.assertEqual(scan.key_of({'chain':'ethereum','mint':'0xAB'}),scan.key_of({'chain':'ethereum','mint':'0xab'}))
        self.assertNotEqual(scan.key_of({'chain':'bnb','mint':'0xab'}),scan.key_of({'chain':'ethereum','mint':'0xab'}))

    def test_review_price_is_not_reused_as_later_alert_price(self):
        state={'entries':{}}
        asset={'chain':'ethereum','mint':'0x'+'1'*40,'symbol':'T','pool':'0x'+'2'*40,'price_usd':1.,'observed_ms':1000}
        record={'latest':asset};setup={'stage':'accumulation'}
        scan.observe_entry(state,record,'review',setup,CONFIG)
        asset.update({'price_usd':2.,'observed_ms':2000})
        scan.observe_entry(state,record,'qualified',setup,CONFIG)
        entry=state['entries'][scan.key_of(asset)]
        self.assertEqual(len(state['entries']),1)
        self.assertEqual(entry['references']['review']['price'],1.)
        self.assertEqual(entry['references']['qualified']['price'],2.)

    def test_missing_or_late_endpoint_does_not_invent_return(self):
        state={'entries':{}};asset={'chain':'ethereum','mint':'a','symbol':'A','pool':'p','price_usd':1.,'observed_ms':1000}
        record={'latest':asset};scan.observe_entry(state,record,'review',{'stage':'accumulation'},CONFIG)
        asset['observed_ms']=1000+40*60000;asset['price_usd']=5.
        scan.measure_entries(state,record,CONFIG)
        result=state['entries'][scan.key_of(asset)]['references']['review']['outcomes']['15']
        self.assertIsNone(result['return_pct']);self.assertEqual(result['status'],'missed_target_window')

    def test_meme_state_cannot_target_the_other_versions(self):
        with patch.dict(os.environ,{'SCANNER_STATE_BRANCH':'scanner-state-v4'}):
            with self.assertRaises(ValueError):scan.configure()

    def test_zero_creator_balance_does_not_prove_burn_or_no_sales(self):
        client=unittest.mock.Mock();client.config=CONFIG
        result=security.developer_check(client,{'rpc':'https://example.test'},{'chain':'ethereum','mint':'0x'+'1'*40},
             {'creator':'0x'+'2'*40,'creator_pct':0.},1000000)
        self.assertEqual(result['status'],'unknown');client.rpc.assert_not_called()

    def test_rpc_cannot_submit_transactions(self):
        client=sources.Client(CONFIG)
        for method in ['eth_sendRawTransaction','sendTransaction','signMessage']:
            with self.assertRaises(ValueError):client.rpc('https://example.test',method,[])

    def test_wrong_rpc_network_cannot_prove_no_developer_sales(self):
        client=unittest.mock.Mock();client.config=CONFIG;client.rpc.return_value='0x38'
        with self.assertRaises(ValueError):security.developer_evm(client,{'rpc':'https://example.test','chain_id':'1'},
            {'chain':'ethereum','mint':'0x'+'1'*40},'0x'+'2'*40,1000000)

    def test_current_quote_cannot_alert_on_lost_or_already_run_breakout(self):
        setup={'stage':'first_breakout','metrics':{'resistance':1.05}}
        self.assertTrue(rules.current_price_holds(1.08,setup,1.07,CONFIG))
        self.assertFalse(rules.current_price_holds(1.04,setup,1.07,CONFIG))
        self.assertFalse(rules.current_price_holds(1.6,setup,1.07,CONFIG))

    def test_evm_developer_window_distinguishes_outflow_and_incomplete_history(self):
        client=unittest.mock.Mock();client.config=deepcopy(CONFIG)
        asset={'chain':'ethereum','mint':'0x'+'1'*40};creator='0x'+'2'*40
        end=10000;tip=5000;logs=[]
        def rpc(url,method,params):
            if method=='eth_chainId':return '0x1'
            if method=='eth_getCode':return '0x'
            if method=='eth_blockNumber':return hex(tip)
            if method=='eth_getBlockByNumber':
                return {'timestamp':hex(end-(tip-int(params[0],16))*12)}
            if method=='eth_getLogs':return logs
            raise AssertionError(method)
        client.rpc.side_effect=rpc
        network={'rpc':'https://example.test','chain_id':'1'}
        with patch.dict(os.environ,{},clear=True):
            result=security.developer_evm(client,network,asset,creator,end*1000)
            self.assertEqual(result['status'],'no_outgoing_transfers_in_complete_window')
            self.assertEqual(result['window_end_ms']-result['window_start_ms'],45*60000)
            logs.append({'address':asset['mint'],'topics':[security.TRANSFER,'0x'+creator[2:].zfill(64),'0x'+'0'*64],
                         'data':'0x1','blockNumber':hex(tip),'transactionHash':'transfer'})
            self.assertEqual(security.developer_evm(client,network,asset,creator,end*1000)['status'],'outgoing_transfer_detected')
            client.config['risk'].update({'rpc_log_page_blocks':1,'rpc_log_max_pages':1})
            self.assertEqual(security.developer_evm(client,network,asset,creator,end*1000)['status'],'unknown')

    def test_solana_developer_missing_transactions_cannot_prove_no_outflow(self):
        client=unittest.mock.Mock();client.config=CONFIG
        asset={'chain':'solana','mint':'mint'};creator='creator';body=None
        rows=[{'signature':'tx','blockTime':10000,'err':None}]
        def rpc(url,method,params):
            if method=='getTokenAccountsByOwner':return {'value':[]}
            if method=='getSignaturesForAddress':return rows
            if method=='getTransaction':return body
            raise AssertionError(method)
        client.rpc.side_effect=rpc
        with patch.dict(os.environ,{},clear=True):
            self.assertEqual(security.developer_solana(client,asset,creator,10000000)['status'],'unknown')
            body={'meta':{'err':None,'preTokenBalances':[{'accountIndex':0,'mint':'mint','owner':creator,
                          'uiTokenAmount':{'amount':'10'}}],'postTokenBalances':[]}}
            self.assertEqual(security.developer_solana(client,asset,creator,10000000)['status'],'outgoing_transfer_detected')
            rows[:]=[{'signature':str(i),'blockTime':10000,'err':None} for i in range(CONFIG['risk']['solana_signature_limit'])]
            result=security.developer_solana(client,asset,creator,10000000)
            self.assertEqual(result['status'],'unknown');self.assertEqual(result['reason'],'developer_history_truncated')

    def test_missing_measurements_remain_in_cohort_when_window_expires(self):
        asset={'chain':'solana','mint':'A','symbol':'A','pool':'P','price_usd':1.,'observed_ms':1000}
        state={'entries':{}};scan.observe_entry(state,{'latest':asset},'review',{'stage':'accumulation'},CONFIG)
        scan.expire_missed_endpoints(state,CONFIG,1000+26*3600000)
        self.assertEqual(len(state['entries']),1)
        self.assertFalse(scan.pending_measurements(state['entries'][scan.key_of(asset)],CONFIG))
        self.assertTrue(all(v['return_pct'] is None for v in state['entries'][scan.key_of(asset)]['references']['review']['outcomes'].values()))


if __name__=='__main__':unittest.main()
