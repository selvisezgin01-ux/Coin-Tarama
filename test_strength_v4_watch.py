from pathlib import Path
from tempfile import TemporaryDirectory
import os
import unittest
from unittest.mock import patch

import strength_v4_watch as watch
from study_dataset import read_json


class VersionIsolationChecks(unittest.TestCase):
    def test_experiment_cannot_write_the_original_branch(self):
        with patch.dict(os.environ,{'SCANNER_STATE_BRANCH':'scanner-state'}):
            with self.assertRaises(ValueError):watch.configure()

    def test_default_experiment_state_and_fingerprint_are_separate(self):
        with patch.dict(os.environ,{},clear=True),\
             patch.object(watch.cloud,'OUT',watch.cloud.OUT),\
             patch.object(watch.cloud,'STATE',watch.cloud.STATE),\
             patch.object(watch.cloud,'fingerprint',watch.cloud.fingerprint):
            original = watch.cloud.fingerprint()
            watch.configure()
            self.assertEqual(os.environ['SCANNER_STATE_BRANCH'],'scanner-state-v4')
            self.assertEqual(watch.cloud.OUT.name,'cloud_output_v4')
            self.assertNotEqual(watch.cloud.fingerprint(),original)

    def test_partial_failure_still_checkpoints_healthy_venue_without_network(self):
        with TemporaryDirectory() as tmp:
            folder=Path(tmp)
            def snapshot(venue,config):
                if venue=='OKX':raise RuntimeError('exchange unavailable')
                return Path('fixture')
            result={'candidates':[],'exchange':'MEXC','observed_ms':1,'feature_cutoff_ms':0,
                    'universe_count':100,'prefilter_count':40,'analyzed_count':30}
            def report(scans,archive):
                (folder/'report.md').write_text('# fixture',encoding='utf-8')
            with patch.object(watch.cloud,'OUT',folder),patch.object(watch.cloud,'STATE',folder/'state.json'),\
                 patch.object(watch.cloud,'fingerprint',return_value='fixture'),\
                 patch.object(watch,'fingerprint',return_value='fixture'),\
                 patch.object(watch.scanner,'OUT',folder),\
                 patch.object(watch.scanner,'snapshot',side_effect=snapshot),\
                 patch.object(watch.scanner,'evaluate',return_value=result),\
                 patch.object(watch.scanner,'write_report',side_effect=report),\
                 patch.object(watch.paper_watch,'refresh'):
                watch.scan()
            state=read_json(folder/'state.json')
            self.assertIn('MEXC',state['venues'])
            self.assertNotIn('OKX',state['venues'])
            self.assertIn('error',read_json(folder/'scan.json')['scans']['OKX'])


if __name__=='__main__':unittest.main()
