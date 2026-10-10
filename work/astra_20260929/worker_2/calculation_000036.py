from pathlib import Path
import hashlib
import json

root = Path('[private local path removed]')
relative = 'work/astra_review_registry/candidates/worker3-finite-data-dyadic-depth-counterexample-v1.md'
raw = (root / relative).read_bytes()
expected_file = '7fe449bb834d7c1127328897eecc3e2849831d7cbb43004c5068b03ee7f673a5'
expected_payload = '27d6f36815f7b3e87c21e6b1367375d8fa6666ae1d391fe867d02dd887bb27a6'
file_hash = hashlib.sha256(raw).hexdigest()
assert file_hash == expected_file, ('Candidate changed from reading ledger', file_hash)
starts = [0] + [i + 1 for i, value in enumerate(raw) if value == 10]
matches = [start for start in starts if hashlib.sha256(raw[start:]).hexdigest() == expected_payload]
assert len(matches) == 1, ('Expected one exact payload suffix', matches)
start = matches[0]
print(json.dumps({'candidate_path': relative, 'file_bytes': len(raw), 'whole_file_sha256': file_hash, 'payload_byte_start': start, 'payload_byte_end': len(raw), 'payload_sha256': expected_payload, 'payload_hash_verified': True}))
print(raw[start:].decode('utf-8'))

sources = {
    'work/astra_20260929/worker_3/note_000018.md': '80bdc94f3eeb2ae439f0efe791a14278c899a80397e5bc857de656e5dbfdb72c',
    'work/astra_20260929/worker_3/note_000021.md': '09b602f48f7735e954624e05c96fa162f3ddeddd63b3f7600da9987be6efa6b8',
}
for path, expected in sources.items():
    data = (root / path).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    assert actual == expected, ('Source changed from reading ledger', path, actual)
    print(json.dumps({'source_path': path, 'bytes': len(data), 'sha256': actual, 'unchanged': True}))