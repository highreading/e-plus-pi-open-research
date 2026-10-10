from pathlib import Path
import hashlib
import json

root = Path('[private local path removed]')
specs = [
    ('work/astra_review_registry/candidates/worker4-b2-ternary-residue-one-conditional-denominator-v1.md', '1f472a9749015949582d20d18e818cc79d1fdc0bef0bd1f41c150eca8b1ef209', '5268f1e9d2b38f15e4b00b9918dd6c98f6f57dcac0b6a75fc046e5bbb7738082'),
    ('work/astra_20260929/worker_2/note_000073.md', '1a1005b7bb29e1c347c818d92cd47fd9052009809a4e48f6b4a437d696f4c14c', None),
    ('work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md', '64b85a398142f1d6234352f890967787ef4dd5ac64844446c521f349fe726412', 'ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d')
]
reports = []
for relative_path, ledger_hash, payload_hash in specs:
    raw = (root / relative_path).read_bytes()
    whole_hash = hashlib.sha256(raw).hexdigest()
    report = {
        'path': relative_path,
        'bytes': len(raw),
        'whole_file_sha256': whole_hash,
        'matches_reading_ledger': whole_hash == ledger_hash
    }
    if payload_hash is not None:
        marker = ('Content SHA256: ' + payload_hash + '\n').encode('ascii')
        assert raw.count(marker) == 1, 'Missing or ambiguous registry hash header'
        marker_start = raw.index(marker)
        payload_start = raw.index(b'\n\n', marker_start) + 2
        actual_payload_hash = hashlib.sha256(raw[payload_start:]).hexdigest()
        report.update({
            'payload_start_byte': payload_start,
            'payload_sha256': actual_payload_hash,
            'matches_registry_payload': actual_payload_hash == payload_hash
        })
    reports.append(report)
print(json.dumps(reports, indent=2))
assert all(item['matches_reading_ledger'] for item in reports)
assert all(item.get('matches_registry_payload', True) for item in reports)
print('Integrity checks passed; no endpoint reconstruction repeated and no files written.')