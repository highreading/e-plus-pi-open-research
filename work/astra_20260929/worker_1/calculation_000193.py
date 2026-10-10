from pathlib import Path
import hashlib
import json

path = Path('work/astra_review_registry/candidates/worker1-digit-minima-and-conditional-denominator-bound-v1.md')
raw = path.read_bytes()
expected_file = '95cf08ba7b72ddcf26dff26b0e149d82eb242a2c98aef647678763d3078f7d68'
expected_payload = '067ec2594e6d23d28cc4342397f71d62fed7517b3e4e86fa3d71191af3addc0a'
file_digest = hashlib.sha256(raw).hexdigest()
assert file_digest == expected_file, 'Whole-file digest differs from the reading ledger'
starts = [0] + [i + 1 for i, value in enumerate(raw) if value == 10 and i + 1 < len(raw)]
matches = [offset for offset in starts if hashlib.sha256(raw[offset:]).hexdigest() == expected_payload]
assert len(matches) == 1, {'payload_boundary_matches': matches}
offset = matches[0]
assert expected_payload.encode('ascii') in raw[:offset]
print(json.dumps({'file_sha256': file_digest, 'payload_sha256': expected_payload, 'payload_byte_offset': offset, 'payload_bytes': len(raw) - offset, 'provenance_check': 'passed', 'mathematical_review_status': 'awaiting independent review'}, indent=2))