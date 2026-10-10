from pathlib import Path
import hashlib
root = Path('[private local path removed]')
checks = [
 ('work/astra_review_registry/candidates/w3-b2-five-residue-three-loss-v1.md', '4c6782bac2e4b40307b358ad9cb7dd30d0caaa7b00bad5bb0c608c52a001f142'),
 ('work/astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md', '66273b26045bf283eff8b3b503e2c51141e05c2c3f0bf128a8412e1fdec6817f')
]
for rel, expected in checks:
    data = (root / rel).read_bytes()
    offsets = [i for i in range(min(2048, len(data))) if hashlib.sha256(data[i:]).hexdigest() == expected]
    print({'path': rel, 'bytes': len(data), 'whole_sha256': hashlib.sha256(data).hexdigest(), 'expected_payload': expected, 'matching_payload_offsets': offsets})
rel = 'work/astra_20260929/worker_3/note_000102.md'
data = (root / rel).read_bytes()
print({'path': rel, 'bytes': len(data), 'whole_sha256': hashlib.sha256(data).hexdigest()})