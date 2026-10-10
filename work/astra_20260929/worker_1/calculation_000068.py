from pathlib import Path
from hashlib import sha256
import json

root = Path('[private local path removed]')
candidate = root / 'work/astra_review_registry/candidates/worker1-b2-four-ternary-endpoint-certificates-v1.md'
data = candidate.read_bytes()
marker = b'Verification status: author-checked finite exact-computation claim'
assert data.count(marker) == 1
start = data.index(marker)
payload_hash = sha256(data[start:]).hexdigest()
expected_payload = '52ab9bfa20ec804c2701c0c3adbee0c980eeda0a2f3db474b2c1183e912b7bed'
assert payload_hash == expected_payload, (payload_hash, expected_payload)
assert sha256(data).hexdigest() == 'c6821c703a748218bf164165ecf43b31af094b601a7d9c1464a139c40662dded'

expected_evidence = {
    'work/astra_20260929/worker_1/calculation_000061.py': '23a70be94192346b554bdd6f5606d155e7e0ddb34aeb17e2be651891334386d3',
    'work/astra_20260929/worker_1/calculation_000063.py': 'fca29b8c2e462cde7bb185679a0d082601c3f8fbfe60d3abeedd65377181e8a0',
    'work/astra_20260929/worker_1/note_000064.md': 'dc5188332deea7da39f0526fea6731d94ed9bfd6a0e84472843a14861499a183'
}
verified = {}
for relative, expected in expected_evidence.items():
    actual = sha256((root / relative).read_bytes()).hexdigest()
    assert actual == expected, (relative, actual, expected)
    verified[relative] = actual

print(json.dumps({'payload_offset': start, 'payload_bytes': len(data)-start, 'payload_sha256': payload_hash, 'evidence_sha256': verified, 'scope': 'Publication provenance only; reconstruction scripts were not executed and independent mathematical review remains outstanding.'}, indent=2))