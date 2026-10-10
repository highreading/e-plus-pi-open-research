from pathlib import Path
import hashlib
import json

root = Path('[private local path removed]')
relative_path = 'work/astra_review_registry/candidates/w3-b2-eventual-d-nonzero-v1.md'
expected_payload = '66273b26045bf283eff8b3b503e2c51141e05c2c3f0bf128a8412e1fdec6817f'
expected_file = '449f948c3de2fa52f5fe582b17205cdeb01db7d287667ad71100722661096404'
data = (root / relative_path).read_bytes()
starts = [0] + [index + 1 for index, byte in enumerate(data) if byte == 10]
matches = [offset for offset in starts if hashlib.sha256(data[offset:]).hexdigest() == expected_payload]
file_digest = hashlib.sha256(data).hexdigest()
print(json.dumps({'path': relative_path, 'file_bytes': len(data), 'file_sha256': file_digest, 'matches_reading_ledger': file_digest == expected_file, 'payload_offsets': matches, 'expected_payload_sha256': expected_payload}, sort_keys=True))
assert len(matches) == 1, 'The exact registered payload was not uniquely identified.'
offset = matches[0]
print(json.dumps({'payload_bytes': len(data) - offset, 'payload_sha256': hashlib.sha256(data[offset:]).hexdigest()}, sort_keys=True))
print(data[offset:].decode('utf-8'))