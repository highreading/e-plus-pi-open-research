from pathlib import Path
import hashlib, json
root = Path('[private local path removed]')
expected = {
 'work/astra_review_registry/candidates/worker3-dyadic-finite-coefficient-verification-v1.md': 'c9b0d6fe13dd17745137498d1cbd64488573c210150e4f592c94c1eec842eacd',
 'work/session_20260927/hp_b1_odd_dyadic_germs_independent_review.md': '43a17e421a90ec2b0b2a664fa4f62bbde15371bf51b26f15432afd1db2843f64',
 'work/session_20260927/check_hp_b1_odd_dyadic_germs.py': 'e82d30312ca6dd2eda7ab75d533fc6c9b3c8d2a3cfc9276f32864edefe697b78',
 'work/session_20260927/hp_b1_odd_dyadic_germs_checks.json': 'f8efc553dbad4713c088bddfe7c60d45d6f8caf87d868ddb4c2b85d1124f77fb'
}
results = []
for relative, wanted in expected.items():
    data = (root / relative).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    results.append({'path': relative, 'bytes': len(data), 'sha256': actual, 'matches_reading_ledger': actual == wanted})
candidate = (root / next(iter(expected))).read_bytes()
payload_hash = '95120d1360a13ef505aae42ed923cca030f0b44ceb99489e17c245501c410269'
starts = [0] + [i + 1 for i, value in enumerate(candidate) if value == 10]
ends = sorted(set([len(candidate), len(candidate.rstrip(b'\n')), len(candidate.rstrip(b'\r\n'))]))
matches = []
for start in starts:
    for end in ends:
        if end >= start and hashlib.sha256(candidate[start:end]).hexdigest() == payload_hash:
            matches.append({'start_byte': start, 'end_byte': end, 'payload_bytes': end-start})
print(json.dumps({'files': results, 'all_files_unchanged': all(r['matches_reading_ledger'] for r in results), 'assigned_payload_sha256': payload_hash, 'exact_payload_matches': matches}, indent=2))