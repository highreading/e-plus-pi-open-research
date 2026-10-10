from pathlib import Path
import hashlib

root = Path('[private local path removed]')
path = root / 'work/astra_review_registry/candidates/b2-ternary-zero-diredacted_historical_name.md'
raw = path.read_bytes()
expected = '627b84db31ceb70a32d19d4ed78056281b5ae9e2bcc79510cfc396a8bc76364c'
marker = b'\n\nSTATUS AND SCOPE\n'
position = raw.find(marker)
assert position >= 0, 'Expected candidate-body boundary not found'
body = raw[position + 2:]
variants = {
    'body_exact': body,
    'body_without_terminal_newlines': body.rstrip(b'\r\n'),
    'body_with_one_terminal_newline': body.rstrip(b'\r\n') + b'\n',
}
print('whole_file_bytes:', len(raw))
print('whole_file_sha256:', hashlib.sha256(raw).hexdigest())
print('expected_content_sha256:', expected)
print('body_byte_offset:', position + 2)
matched = []
for name, value in variants.items():
    digest = hashlib.sha256(value).hexdigest()
    print(name, 'bytes=', len(value), 'sha256=', digest, 'matches=', digest == expected)
    if digest == expected:
        matched.append(name)
print('matching_representations:', matched)
if not matched:
    print('UNRESOLVED: content representation must be supplied before a hash-bound registry review.')