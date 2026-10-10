from pathlib import Path
import hashlib
import json

root = Path('[private local path removed]')
candidate = root / 'work/astra_review_registry/candidates/worker2-b2-n4-exact-boundary-certificate-v1.md'
saved_note = root / 'work/astra_20260929/worker_2/note_000167.md'
data = candidate.read_bytes()
expected_payload = 'dae657eacb7c17dc22444fd0485bcf57a9465236d3f8d5fadaeb3051f701a513'
expected_file = '6fd4d21d8e08187c6a1f865b2ebabe3abc91ae18947d2f79ce90f0c42ca7ed21'
expected_note = 'e4ee220746a308fd2713299cefd3dba34ec72ba1f33af196eca4b81018ad5977'
starts = [0] + [i + 1 for i, byte in enumerate(data) if byte == 10]
matches = [offset for offset in starts if hashlib.sha256(data[offset:]).hexdigest() == expected_payload]
file_hash = hashlib.sha256(data).hexdigest()
note_hash = hashlib.sha256(saved_note.read_bytes()).hexdigest()
assert file_hash == expected_file
assert note_hash == expected_note
assert len(matches) == 1
print(json.dumps({'candidate_file_sha256': file_hash, 'payload_sha256': expected_payload, 'payload_start_byte': matches[0], 'candidate_end_byte': len(data), 'saved_calculation_sha256': note_hash, 'integrity_checks_passed': True, 'independent_review': False}, indent=2))