from pathlib import Path
import hashlib
import json

relative = Path('work/astra_review_registry/candidates/b2-ternary-endpoint-denominator-and-content-v1.md')
locations = [ancestor / relative for ancestor in (Path.cwd(), *Path.cwd().parents)]
matches = [location for location in locations if location.is_file()]
assert len(matches) == 1, 'Expected exactly one project candidate path'
path = matches[0]
data = path.read_bytes()
file_digest = hashlib.sha256(data).hexdigest()
assert file_digest == 'c7ef06d12e84f62443ad86ded779a5d7521c36563176ba8960821417e63ee38b', 'Whole-file digest differs from reading ledger'
marker = b'UNVERIFIED CANDIDATE. Author: worker_4.'
assert data.count(marker) == 1
start = data.index(marker)
body = data[start:]
expected = '6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe'
variants = {'exact_remaining_bytes': body, 'without_terminal_newlines': body.rstrip(b'\n'), 'one_terminal_newline': body.rstrip(b'\n') + b'\n'}
verified = []
for representation, payload in variants.items():
    digest = hashlib.sha256(payload).hexdigest()
    if digest == expected:
        verified.append({'representation': representation, 'payload_bytes': len(payload), 'sha256': digest})
assert verified, 'No payload representation matches the assigned immutable hash'
print(json.dumps({'candidate_path': str(path), 'whole_file_bytes': len(data), 'whole_file_sha256': file_digest, 'payload_start_byte': start, 'verified_payload_representations': verified, 'scope': 'Read-only provenance verification; no endpoint computation repeated'}, indent=2))