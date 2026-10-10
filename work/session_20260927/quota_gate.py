"""Coordinate the active worker and app heartbeat without duplicate quota reads."""
from pathlib import Path
import argparse, json, os, time
from datetime import datetime, timezone

root=Path(__file__).resolve().parent
state_path=root/'quota_state.json'
lock_path=root/'quota_gate.lock'
parser=argparse.ArgumentParser()
parser.add_argument('action',choices=['initialize','claim','record','stop'])
parser.add_argument('--data')
args=parser.parse_args()
now=time.time()
try:
    fd=os.open(lock_path,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
except FileExistsError:
    print(json.dumps({'claimed':False,'reason':'another_worker_holds_gate'}))
    raise SystemExit(0)
try:
    os.close(fd)
    state=json.loads(state_path.read_text()) if state_path.exists() else {}
    if args.action=='initialize':
        if not state:
            state={'active':True,'interval_seconds':300,'stop_threshold_percent':40,
                   'last_attempt_epoch':now,'next_due_epoch':now+300,
                   'last_remaining_percent':94,'initial_read':'supported_tool_at_session_start',
                   'resets_permitted':False}
        result=state
    elif args.action=='claim':
        due=state.get('next_due_epoch',0)
        claimed=state.get('active',False) and now>=due
        if claimed:
            state.update(last_attempt_epoch=now,next_due_epoch=now+300)
        result={'claimed':claimed,'active':state.get('active',False),
                'next_due_epoch':state.get('next_due_epoch',0),
                'seconds_until_due':max(0,state.get('next_due_epoch',0)-now)}
    elif args.action=='record':
        row=json.loads(args.data)
        row['logged_at']=datetime.now(timezone.utc).isoformat()
        with (root/'quota_log.jsonl').open('a') as f:
            f.write(json.dumps(row)+'\n')
        remaining=row.get('core_remaining_percent')
        if remaining is not None:
            state['last_remaining_percent']=remaining
            if remaining<=40:
                state.update(active=False,stop_reason='quota_at_or_below_40',
                             termination_observed_at=row['logged_at'])
        result=state
    else:
        state.update(active=False,stop_reason=args.data or 'verified_main_proof')
        result=state
    temp=state_path.with_suffix('.tmp')
    temp.write_text(json.dumps(state,indent=2)+'\n')
    temp.replace(state_path)
    print(json.dumps(result))
finally:
    lock_path.unlink(missing_ok=True)
