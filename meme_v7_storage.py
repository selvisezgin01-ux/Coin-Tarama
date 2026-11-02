"""Lossless, checksummed state transport. Financial state is never pruned or repriced."""
import base64, gzip, hashlib, io, json, re
from pathlib import Path

FORMAT='meme-v7-storage-v1'
PART_BYTES=6*1024*1024
MAX_FILE_BYTES=16*1024*1024
MAX_STATE_BYTES=512*1024*1024

def digest(raw):return hashlib.sha256(raw).hexdigest()
def pack(value):return json.dumps(value,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode('utf-8')

def prepare(state,directory,part_bytes=PART_BYTES):
    if state.get('version')!='meme-v7':raise ValueError('Unexpected state version')
    if not 0<part_bytes<=PART_BYTES:raise ValueError('Invalid part budget')
    raw=pack(state)
    if len(raw)>MAX_STATE_BYTES:raise ValueError('State capacity budget exceeded; refusing silent truncation')
    compressed=gzip.compress(raw,compresslevel=6,mtime=0);parts=[];files=[];directory=Path(directory)
    for index,start in enumerate(range(0,len(compressed),part_bytes)):
        chunk=compressed[start:start+part_bytes];name=f'state-part-{index:05d}.json'
        data=pack({'encoding':'base64','data':base64.b64encode(chunk).decode('ascii')})
        if len(data)>MAX_FILE_BYTES:raise ValueError('State part exceeds publication budget')
        path=directory/name;path.write_bytes(data);files.append((path,name))
        parts.append({'name':name,'bytes':len(data),'sha256':digest(data)})
    manifest={'version':FORMAT,'state_version':state['version'],'rules_fingerprint':state['rules_fingerprint'],
        'encoding':'gzip+base64-json','state_bytes':len(raw),'state_sha256':digest(raw),
        'compressed_bytes':len(compressed),'compressed_sha256':digest(compressed),'parts':parts,
        'summary':{'events':len(state.get('events',{})),'cases':len(state.get('cases',{})),
            'receipts':len(state.get('receipts',{})),'runs':len(state.get('runs',[])),
            'last_run':state.get('runs',[])[-1] if state.get('runs') else None},
        'note':'Lossless transport manifest. Load and verify every part before scanning; this is not an empty financial state.'}
    path=directory/'state_manifest.json';path.write_bytes(pack(manifest))
    return [(path,'state.json')]+files

def load(manifest,read_bytes):
    if manifest.get('version')!=FORMAT:
        if manifest.get('version')!='meme-v7':raise ValueError('Unexpected stored state format')
        return manifest # Legacy full JSON migration preserves every field.
    if manifest.get('state_version')!='meme-v7' or manifest.get('encoding')!='gzip+base64-json':raise ValueError('Invalid storage schema')
    size=manifest.get('state_bytes')
    if type(size) is not int or not 0<size<=MAX_STATE_BYTES:raise ValueError('Invalid state byte budget')
    parts=manifest.get('parts')
    if not isinstance(parts,list) or not 0<len(parts)<=128:raise ValueError('Invalid part count')
    chunks=[]
    for index,part in enumerate(parts):
        name=f'state-part-{index:05d}.json'
        if part.get('name')!=name:raise ValueError('Unexpected state part identity/order')
        data=read_bytes(name)
        if not isinstance(data,bytes) or len(data)>MAX_FILE_BYTES or len(data)!=part.get('bytes') or digest(data)!=part.get('sha256'):
            raise ValueError('State part checksum or size mismatch')
        payload=json.loads(data)
        if payload.get('encoding')!='base64':raise ValueError('Unexpected part encoding')
        chunks.append(base64.b64decode(payload['data'],validate=True))
    compressed=b''.join(chunks)
    if len(compressed)!=manifest.get('compressed_bytes') or digest(compressed)!=manifest.get('compressed_sha256'):
        raise ValueError('Compressed state checksum mismatch')
    with gzip.GzipFile(fileobj=io.BytesIO(compressed)) as stream:raw=stream.read(size+1)
    if len(raw)!=size or digest(raw)!=manifest.get('state_sha256'):raise ValueError('Restored state checksum or length mismatch')
    state=json.loads(raw)
    if state.get('version')!='meme-v7' or state.get('rules_fingerprint')!=manifest['rules_fingerprint']:raise ValueError('Restored state identity mismatch')
    return state
