"""Portable collector service. Optional fixed-repository feed publication, no trading."""
from pathlib import Path
import argparse,contextlib,json,os,time
from meme_v7_collector import run
from meme_v7_feed_publisher import Publisher

@contextlib.contextmanager
def single_instance(directory):
    path=Path(directory)/'collector.lock';path.parent.mkdir(exist_ok=True,parents=True)
    handle=path.open('a+b');handle.seek(0)
    if path.stat().st_size==0:handle.write(b'1');handle.flush();handle.seek(0)
    try:
        if os.name=='nt':
            import msvcrt;msvcrt.locking(handle.fileno(),msvcrt.LK_NBLCK,1)
        else:
            import fcntl;fcntl.flock(handle.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
    except OSError:
        handle.close();raise RuntimeError('Collector already running; refusing duplicate publisher') from None
    try:yield
    finally:handle.close()

def serve(directory,publish=None):
    directory=Path(directory);directory.mkdir(exist_ok=True,parents=True)
    cfg=json.loads((Path(__file__).parent/'meme_v7_config.json').read_text(encoding='utf-8'))
    with single_instance(directory):
        while True:
            try:run(directory/'discovery.sqlite',cfg,directory/'feed.json',publish=publish)
            except KeyboardInterrupt:raise
            except Exception as exc:
                (directory/'service_health.json').write_text(json.dumps({'observed_ms':int(time.time()*1000),'status':'restarting_after_error','error':str(exc)}),encoding='utf-8')
                time.sleep(30)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data-dir',default='collector_data');p.add_argument('--publish',action='store_true');a=p.parse_args()
    directory=Path(a.data_dir).resolve();publisher=Publisher(directory) if a.publish else None
    serve(directory,publisher.publish if publisher else None)
