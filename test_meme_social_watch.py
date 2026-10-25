import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock,patch

import meme_scan as meme
import meme_social_watch as social


class SocialChecks(unittest.TestCase):
    def setUp(self):
        self.asset={'chain':'ethereum','mint':'0x'+'1'*40,'pool':'0x'+'2'*40,'symbol':'TEST'}
        self.watch={'tokens':{},'pending':[]}

    def test_only_valid_x_targets_are_normalized_without_following_links(self):
        self.assertEqual(social.canonical_x('https://twitter.com/NAME/status/123?ref=abc'),'https://x.com/name')
        self.assertEqual(social.canonical_x('https://x.com/i/communities/123'),'https://x.com/i/communities/123')
        for url in ['https://x.com.attacker.test/name','https://x.com@attacker.test/name','https://x.com:999/name',
                    'javascript:alert(1)','https://x.com/intent/follow','https://x.com/i/lists/123','https://x.com/name/other']:
            self.assertIsNone(social.canonical_x(url))

    def test_missing_metadata_is_not_social_account_removal(self):
        self.assertIsNone(social.x_links({}))
        self.assertIsNone(social.x_links({'info':{'socials':[{'type':'twitter','url':'invalid'}]}}))
        self.assertEqual(social.x_links({'info':{'socials':[]}}),[])
        social.update_links(self.watch,self.asset,['https://x.com/first'],100)
        social.update_links(self.watch,self.asset,None,200,True)
        row=self.watch['tokens'][meme.key_of(self.asset)]
        self.assertEqual(row['current_links'],['https://x.com/first']);self.assertEqual(row['observed_link_changes'],0)
        self.assertEqual(self.watch['pending'],[])

    def test_initial_baseline_and_url_spelling_never_become_historical_rename_counts(self):
        links=social.x_links({'info':{'socials':[{'type':'twitter','url':'https://twitter.com/NAME'}]}})
        social.update_links(self.watch,self.asset,links,100,True)
        social.update_links(self.watch,self.asset,['https://x.com/name'],200,True)
        row=self.watch['tokens'][meme.key_of(self.asset)]
        self.assertIsNone(row['historical_username_change_count']);self.assertFalse(row['x_account_identity_verified'])
        self.assertEqual(row['observed_link_changes'],0);self.assertEqual(self.watch['pending'],[])

    def test_link_change_is_counted_once_and_only_prior_candidates_are_notified(self):
        social.update_links(self.watch,self.asset,['https://x.com/old'],100)
        social.update_links(self.watch,self.asset,['https://x.com/new'],200,True)
        social.update_links(self.watch,self.asset,['https://x.com/new'],300,True)
        row=self.watch['tokens'][meme.key_of(self.asset)]
        self.assertEqual(row['observed_link_changes'],1);self.assertEqual(len(self.watch['pending']),1)
        self.assertEqual(self.watch['pending'][0]['before'],['https://x.com/old'])
        social.update_links(self.watch,self.asset,[],400,False)
        self.assertEqual(row['observed_link_changes'],2);self.assertEqual(len(self.watch['pending']),1)

    def test_cto_claim_is_an_additional_warning_not_developer_sale_proof(self):
        social.update_links(self.watch,self.asset,[],100)
        claim={'claimDate':'2026-10-25T20:00:00Z'};stamp=1792960000000
        social.update_cto(self.watch,self.asset,claim,stamp,True)
        social.update_cto(self.watch,self.asset,claim,stamp+1000,True)
        row=self.watch['tokens'][meme.key_of(self.asset)]
        self.assertEqual(len(self.watch['pending']),1)
        self.assertIn('not_developer_sale_proof',row['cto']['status'])
        self.assertIn('kanıtlanmış sayılmaz',social.text_for(row))
        social.update_cto(self.watch,self.asset,None,stamp+2000,True)
        self.assertIn('cto',row)

    def test_another_pool_or_contract_does_not_modify_this_tokens_social_baseline(self):
        key=meme.key_of(self.asset);state={'assets':{key:{'latest':self.asset}},'entries':{},'pending':[]}
        config={'networks':{'ethereum':{'name':'Ethereum','dex':'ethereum'}}}
        client=Mock();client.dex.side_effect=[[{'chainId':'ethereum','pairAddress':'0x'+'3'*40,
                    'baseToken':{'address':self.asset['mint']},'info':{'socials':[{'type':'twitter','url':'https://x.com/wrong'}]}}],[]]
        social.annotate(state,config,client)
        row=state['social_watch']['tokens'][key]
        self.assertNotIn('current_links',row);self.assertEqual(state['social_watch']['last_run']['usable_x_observations'],0)

    def test_additive_social_rules_cannot_silently_reset_their_history(self):
        state={'social_watch':{'fingerprint':'another-version','tokens':{},'pending':[]}}
        with self.assertRaises(ValueError):social.social_state(state)

    def test_first_queued_candidate_is_not_treated_as_a_previously_delivered_alert(self):
        key=meme.key_of(self.asset);row={**self.asset,'stage':'accumulation'}
        state={'entries':{key:{'alerted_stages':['accumulation']}},'pending':[{'candidates':[row]}]}
        self.assertFalse(social.previously_notified(state,key))
        state['pending']=[];self.assertTrue(social.previously_notified(state,key))

    def test_retry_of_existing_social_warning_does_not_create_a_duplicate_issue(self):
        state={'pending':[]};watch=social.social_state(state)
        social.update_links(watch,self.asset,['https://x.com/old'],100)
        social.update_links(watch,self.asset,['https://x.com/new'],200,True)
        event=watch['pending'][0];marker='<!-- meme-social-watch:'+event['id']+' -->'
        sent=[]
        def http(url,body=None,headers=None,label=None):
            if body is None:return [{'body':marker}]
            sent.append(body);return {'number':123}
        with TemporaryDirectory() as directory:
            path=Path(directory)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(meme,'STATE',path),patch.object(meme.cloud,'http_json',side_effect=http),patch.dict('os.environ',
                    {'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'unit-test-only','COIN_NOTIFY_USER':'test-user'}):social.notify()
            self.assertEqual(json.loads(path.read_text(encoding='utf-8'))['social_watch']['pending'],[])
        self.assertEqual(sent,[])

    def test_candidate_notification_keeps_manual_map_warning_and_adds_social_uncertainty(self):
        row={**self.asset,'stage':'accumulation','observed_ms':1000,'price_usd':1.}
        state={'pending':[{'id':'testbatch','created_ms':1000,'candidates':[row]}]}
        watch=social.social_state(state);social.update_links(watch,self.asset,['https://x.com/current'],1000)
        sent=[]
        def http(url,body=None,headers=None,label=None):
            if body is None:return []
            sent.append(body);return {'number':123}
        with TemporaryDirectory() as directory:
            path=Path(directory)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(meme,'STATE',path),patch.object(meme.cloud,'http_json',side_effect=http),patch.dict('os.environ',
                    {'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'unit-test-only','COIN_NOTIFY_USER':'test-user'}):
                social.notify()
        self.assertEqual(len(sent),1)
        self.assertIn('MANUEL KONTROL EDİLMELİ',sent[0]['body'])
        self.assertIn('https://x.com/current',sent[0]['body'])
        self.assertIn('Geçmiş kullanıcı adı değişikliği sayısı: bilinmiyor',sent[0]['body'])

    def test_failed_social_delivery_keeps_pending_event_and_retry_uses_explicit_warning(self):
        state={'pending':[]};watch=social.social_state(state)
        social.update_links(watch,self.asset,['https://x.com/old'],100)
        social.update_links(watch,self.asset,['https://x.com/new'],200,True)
        sent=[];fail=[True]
        def http(url,body=None,headers=None,label=None):
            if body is None:return []
            if fail[0]:raise RuntimeError('Test delivery failure')
            sent.append(body);return {'number':123}
        with TemporaryDirectory() as directory:
            path=Path(directory)/'state.json';path.write_text(json.dumps(state),encoding='utf-8')
            with patch.object(meme,'STATE',path),patch.object(meme.cloud,'http_json',side_effect=http),patch.dict('os.environ',
                    {'GITHUB_REPOSITORY':'example/test','GH_TOKEN':'unit-test-only','COIN_NOTIFY_USER':'test-user'}):
                with self.assertRaises(RuntimeError):social.notify()
                self.assertEqual(len(json.loads(path.read_text(encoding='utf-8'))['social_watch']['pending']),1)
                fail[0]=False;social.notify()
            self.assertEqual(json.loads(path.read_text(encoding='utf-8'))['social_watch']['pending'],[])
        self.assertEqual(len(sent),1);self.assertIn('X bağlantısı değişti',sent[0]['title'])
        self.assertIn('Önce: https://x.com/old',sent[0]['body']);self.assertIn('Sonra: https://x.com/new',sent[0]['body'])
        self.assertIn('kesin satış/dump',sent[0]['body'])


if __name__=='__main__':unittest.main()
