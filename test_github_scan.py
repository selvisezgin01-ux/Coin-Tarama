"""Cloud-watch deduplication, failures, opt-in notifications and durable state."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

import github_scan as cloud


def candidate(symbol='TESTUSDT'):
    return {'symbol':symbol,'exchange':'MEXC','breakout_open_ms':0,'mid_price':1.,
            'return24_pct':5.,'breakout_volume_ratio':2.,'spread_pct':.1,
            'liquidity_band':'main','breakout_level':.99,'breakout_age_bars':0}


class CloudChecks(unittest.TestCase):
    def test_new_then_unchanged_then_reentry_cooldown(self):
        state=cloud.new_state();row=candidate()
        scan={'MEXC':{'candidates':[row]}}
        self.assertEqual(len(cloud.update_state(state,scan,0)),1)
        self.assertEqual(cloud.update_state(state,scan,4*3600000),[])
        cloud.update_state(state,{'MEXC':{'candidates':[]}},8*3600000)
        self.assertEqual(cloud.update_state(state,scan,12*3600000),[])
        cloud.update_state(state,{'MEXC':{'candidates':[]}},50*3600000)
        fresh=cloud.update_state(state,scan,52*3600000)
        self.assertEqual(fresh[0]['arrival'],'reentry')

    def test_exchange_failure_preserves_active_state_and_other_exchange(self):
        state=cloud.new_state()
        cloud.update_state(state,{'MEXC':{'candidates':[candidate()]}},0)
        previous=deepcopy(state['venues']['MEXC'])
        fresh=cloud.update_state(state,{'MEXC':{'error':'unavailable'},'OKX':{'candidates':[candidate('NEWUSDT')]}},4*3600000)
        self.assertEqual(state['venues']['MEXC'],previous)
        self.assertEqual(len(fresh),1)
        self.assertEqual(fresh[0]['symbol'],'NEWUSDT')

    def test_report_mode_never_sends_external_messages(self):
        with TemporaryDirectory() as tmp,patch.object(cloud,'STATE',Path(tmp)/'state.json'):
            state=cloud.new_state()
            cloud.update_state(state,{'MEXC':{'candidates':[candidate()]}},0)
            cloud.save(cloud.STATE,state)
            with patch.object(cloud,'http_json',side_effect=AssertionError('Unexpected external send')):
                cloud.notify('report')
            self.assertEqual(json.loads(cloud.STATE.read_text(encoding='utf-8'))['pending'],[])

    def test_failed_delivery_preserves_pending_and_does_not_log_token(self):
        token='synthetic-secret-never-use'
        with patch.object(cloud,'urlopen',side_effect=HTTPError('https://example/'+token,401,'unauthorized',None,None)):
            with self.assertRaises(RuntimeError) as caught:cloud.http_json('https://example/'+token,label='Telegram')
        self.assertNotIn(token,str(caught.exception))
        with TemporaryDirectory() as tmp,patch.object(cloud,'STATE',Path(tmp)/'state.json'):
            state=cloud.new_state();cloud.update_state(state,{'MEXC':{'candidates':[candidate()]}},0)
            cloud.save(cloud.STATE,state)
            with patch.dict('os.environ',{'TELEGRAM_BOT_TOKEN':token,'TELEGRAM_CHAT_ID':'123'}),\
                 patch.object(cloud,'http_json',side_effect=RuntimeError('delivery failed')):
                with self.assertRaises(RuntimeError):cloud.notify('telegram')
            self.assertEqual(len(json.loads(cloud.STATE.read_text(encoding='utf-8'))['pending']),1)

    def test_state_branch_roundtrip_without_touching_code_or_network(self):
        with TemporaryDirectory() as tmp:
            base=Path(tmp);remote=base/'remote.git';work=base/'work'
            remote.mkdir();work.mkdir()
            subprocess.run(['git','init','--bare',str(remote)],check=True,capture_output=True)
            subprocess.run(['git','init',str(work)],check=True,capture_output=True)
            subprocess.run(['git','-C',str(work),'remote','add','origin',str(remote)],check=True,capture_output=True)
            out=work/'cloud_output';state=out/'state.json'
            (work/'code.py').write_text('original code',encoding='utf-8')
            with patch.object(cloud,'ROOT',work),patch.object(cloud,'OUT',out),patch.object(cloud,'STATE',state),\
                 patch.object(cloud,'fingerprint',return_value='fixture'),\
                 patch.dict('os.environ',{'SCANNER_STATE_BRANCH':'scanner-state'}):
                cloud.pull_state()
                stored=json.loads(state.read_text(encoding='utf-8'));stored['sentinel']='persisted'
                cloud.save(state,stored);(out/'report.md').write_text('report',encoding='utf-8')
                cloud.push_state()
                cloud.save(state,{'damaged_local_copy':True})
                cloud.pull_state()
                self.assertEqual(json.loads(state.read_text(encoding='utf-8'))['sentinel'],'persisted')
                tree=cloud.git('ls-tree','--name-only',(out/'parent.txt').read_text(encoding='ascii')).stdout.splitlines()
                self.assertEqual(sorted(tree),['report.md','state.json'])
            self.assertEqual((work/'code.py').read_text(encoding='utf-8'),'original code')


if __name__=='__main__':unittest.main()
