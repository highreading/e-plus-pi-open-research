from pathlib import Path
import hashlib
import json

path = Path('work/astra_review_registry/candidates/worker1-parity-digit-denominator-bound-v1.md')
data = path.read_bytes()
expected_file = '1bd51e8d84f503372c5c1eca1cc145d699a8e82b72c5e01d038e7f2138324fc5'
expected_payload = '9677b1b1c9a80f4d833dd2ebdd9a2612ae352036e7625ac1fdb87821d3537150'
marker = b'Status: author-checked conditional arithmetic claim; independent review required.'
assert data.count(marker) == 1
start = data.index(marker)
suffix = data[start:]
representations = [('exact file suffix', suffix)]
if suffix.endswith(b'\n'):
    representations.append(('file suffix excluding one final LF', suffix[:-1]))
checks = [{'representation': name, 'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()} for name, body in representations]
matches = [item for item in checks if item['sha256'] == expected_payload]
file_digest = hashlib.sha256(data).hexdigest()
print(json.dumps({'file_bytes': len(data), 'file_sha256': file_digest, 'payload_byte_offset': start, 'payload_checks': checks, 'matching_payloads': matches}, indent=2))
assert file_digest == expected_file, 'Whole-file digest differs from the reading ledger'
assert len(matches) == 1, 'Registered payload digest was not uniquely recovered'
print('Provenance verified; independent mathematical review remains outstanding.')