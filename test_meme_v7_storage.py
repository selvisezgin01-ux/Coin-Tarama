import base64, copy, json, os, subprocess, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import meme_v7_storage as storage
import meme_v7_persistence as persistence

def state():
    return {'version':'meme-v7','rules_fingerprint':'frozen-financial-fingerprint',
        'entries':{'solana:CA':{'references':{'entry_5m':{'price':0.00000123456789,'observed_ms':1234567890123,'pool':'original'}}}},
        'receipts':{'original-event':{'issue_number':99,'observed_ms':1234567890123}},
        'events':{'original-event':{'price':0.00000123456789,'phase':'entry_5m'}},'cases':{},
        'legacy_v6':{'original':{'price':17.25}},'cold_archives':[{'keys':['solana:CA'],'source_state_sha':'a'*40}],
        'ledger':{},'assets':{},'runs':[]}

class StorageTests(unittest.TestCase):
    def test_collector_package_includes_new_transitive_storage_dependency(self):
        root=Path(__file__).resolve().parent
        copy_line=next(line for line in (root/'Dockerfile.meme-v7').read_text(encoding='utf-8').splitlines() if line.startswith('COPY '))
        files=copy_line.split()[1:-1]
        self.assertIn('meme_v7_storage.py',files)
        with tempfile.TemporaryDirectory() as td:
            import shutil,sys
            for name in files:shutil.copyfile(root/name,Path(td)/name)
            result=subprocess.run([sys.executable,'-c','import meme_v7_service'],cwd=td,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr.decode(errors='replace'))
    def roundtrip(self,s,**kw):
        with tempfile.TemporaryDirectory() as td:
            files=storage.prepare(s,td,**kw);manifest=json.loads(files[0][0].read_bytes())
            self.assertTrue(all(p.stat().st_size<=storage.MAX_FILE_BYTES for p,_ in files))
            return storage.load(manifest,lambda n:(Path(td)/n).read_bytes()),manifest
    def test_exact_roundtrip_preserves_original_prices_times_receipts_and_archive(self):
        original=state();out,_=self.roundtrip(original);self.assertEqual(original,out)
    def test_legacy_state_is_not_pruned_or_repriced(self):
        original=state();self.assertEqual(original,storage.load(original,lambda _:self.fail('legacy needs no part')))
    def test_many_parts_roundtrip(self):
        original=state();original['payload']=base64.b64encode(os.urandom(200000)).decode()
        out,manifest=self.roundtrip(original,part_bytes=65536);self.assertEqual(out,original);self.assertGreater(len(manifest['parts']),1)
    def test_truncated_tampered_missing_or_reordered_part_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            original=state();original['payload']=base64.b64encode(os.urandom(200000)).decode()
            files=storage.prepare(original,td,part_bytes=65536);m=json.loads(files[0][0].read_bytes());read=lambda n:(Path(td)/n).read_bytes()
            with self.assertRaises(ValueError):storage.load(m,lambda n:read(n)[:-1])
            with self.assertRaises(ValueError):storage.load(m,lambda n:b'!'+read(n)[1:])
            with self.assertRaises(FileNotFoundError):storage.load(m,lambda n:(Path(td)/'missing').read_bytes())
            bad=copy.deepcopy(m);bad['parts'].reverse()
            with self.assertRaises(ValueError):storage.load(bad,read)
    def test_no_path_traversal_or_mismatched_rules(self):
        with tempfile.TemporaryDirectory() as td:
            files=storage.prepare(state(),td);m=json.loads(files[0][0].read_bytes());read=lambda n:(Path(td)/n).read_bytes()
            bad=copy.deepcopy(m);bad['parts'][0]['name']='../../state.json'
            with self.assertRaises(ValueError):storage.load(bad,read)
            bad=copy.deepcopy(m);bad['rules_fingerprint']='changed'
            with self.assertRaises(ValueError):storage.load(bad,read)
    def test_decompression_length_and_capacity_are_enforced(self):
        with tempfile.TemporaryDirectory() as td:
            files=storage.prepare(state(),td);m=json.loads(files[0][0].read_bytes());m['state_bytes']-=1
            with self.assertRaises(ValueError):storage.load(m,lambda n:(Path(td)/n).read_bytes())
            with patch.object(storage,'MAX_STATE_BYTES',10):
                with self.assertRaises(ValueError):storage.prepare(state(),td)
    def test_github_large_blob_error_has_specific_non_retryable_category(self):
        error=subprocess.CompletedProcess([],1,'','GH001: file exceeds GitHub size limit')
        self.assertEqual(persistence.category(error),'capacity');self.assertFalse(persistence.PublicationError('capacity','limit').restart_allowed)

class PublicationIntegrationTests(unittest.TestCase):
    def test_real_git_publish_restore_next_checkpoint_and_old_commit_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'work';root.mkdir();remote=Path(td)/'remote.git'
            def git(*args,cwd=root):return subprocess.run(['git',*args],cwd=cwd,capture_output=True,check=True).stdout
            git('init','--bare',str(remote));git('init');git('remote','add','origin',str(remote));git('config','user.name','fixture');git('config','user.email','fixture@example.invalid')
            out=root/'output';out.mkdir();original=state();(out/'state.json').write_text(json.dumps(original),encoding='utf-8');(out/'report.md').write_text('fixture',encoding='utf-8');(out/'parent.txt').write_text('',encoding='ascii')
            pub=persistence.SafePublisher(root,out,original['rules_fingerprint'],'fixture',log=lambda *a,**k:None)
            first=pub.publish()
            def restored(sha):
                manifest=json.loads(git('show',sha+':state.json'));return storage.load(manifest,lambda n:git('show',sha+':'+n))
            self.assertEqual(restored(first),original)
            next_state=copy.deepcopy(original);next_state['runs'].append({'started_ms':1234,'session_id':'new'})
            (out/'state.json').write_text(json.dumps(next_state),encoding='utf-8');second=pub.publish()
            self.assertNotEqual(first,second);self.assertEqual(restored(first),original);self.assertEqual(restored(second),next_state)
            self.assertEqual(git('rev-parse',second+'^').decode().strip(),first)
            self.assertEqual(git('rev-parse','refs/heads/'+persistence.BRANCH,cwd=remote).decode().strip(),second)

if __name__=='__main__':unittest.main()
