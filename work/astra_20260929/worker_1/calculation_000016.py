from pathlib import Path
import hashlib
import json

candidate = Path('[private local path removed]redacted_historical_name.md')
expected_content = '627b84db31ceb70a32d19d4ed78056281b5ae9e2bcc79510cfc396a8bc76364c'
expected_file = '4f7f387cd5206834a7e6c8e7c011016bce45c7cb33c06c0f2d62cc275f70c55c'
# Use the actual whole-file digest recorded in the reading ledger.
expected_file = '4f7c387cd5206834a5cf590a2469dc2d227dd95a93cbef8fcaecdc10a42be446'
raw = candidate.read_bytes()
marker = b'\n\nSTATUS AND SCOPE\n'
assert raw.count(marker) == 1, 'Candidate body boundary is missing or ambiguous'
body_offset = raw.index(marker) + 2
header = raw[:body_offset].decode('utf-8')
assert 'Content SHA256: ' + expected_content in header
body = raw[body_offset:]
variants = {
    'body_exact': body,
    'body_without_terminal_newlines': body.rstrip(b'\r\n'),
    'body_with_one_terminal_newline': body.rstrip(b'\r\n') + b'\n',
}
checks = {}
for name, data in variants.items():
    digest = hashlib.sha256(data).hexdigest()
    checks[name] = {'bytes': len(data), 'sha256': digest, 'matches_expected_content': digest == expected_content}
file_digest = hashlib.sha256(raw).hexdigest()
# Print the digest directly for comparison with the supplied ledger.
print(json.dumps({
    'path': str(candidate),
    'whole_file_bytes': len(raw),
    'whole_file_sha256': file_digest,
    'body_byte_offset': body_offset,
    'expected_content_sha256': expected_content,
    'body_checks': checks,
    'matching_representations': [name for name, result in checks.items() if result['matches_expected_content']],
}, indent=2))