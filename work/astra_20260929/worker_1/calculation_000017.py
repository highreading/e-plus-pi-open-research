from pathlib import Path
import hashlib
import json

folder = Path('work/astra_review_registry/candidates')
paths = sorted(p for p in folder.iterdir() if p.is_file() and p.name.startswith('b2-ternary-zero-') and p.suffix == '.md')
if len(paths) != 1:
    raise RuntimeError('Expected one matching candidate; found ' + str(len(paths)))
raw = paths[0].read_bytes()
expected_file = '4f7f387cd5206834a5cf590a2469dc2d227dd95a93cbef8fcaecdc10a42be446'
expected_content = '627b84db31ceb70a32d19d4ed78056281b5ae9e2bcc79510cfc396a8bc76364c'
file_hash = hashlib.sha256(raw).hexdigest()
print(json.dumps({'bytes': len(raw), 'file_sha256': file_hash, 'matches_reading_ledger': file_hash == expected_file}))

# Identify a body beginning at a line boundary, checking terminal-newline conventions explicitly.
starts = [0] + [i + 1 for i, value in enumerate(raw) if value == 10 and i + 1 < len(raw)]
matches = []
for start in starts:
    suffix = raw[start:]
    variants = {'exact_suffix': suffix, 'without_terminal_newlines': suffix.rstrip(b'\r\n'), 'one_terminal_lf': suffix.rstrip(b'\r\n') + b'\n'}
    for convention, body in variants.items():
        if hashlib.sha256(body).hexdigest() == expected_content:
            matches.append({'start_byte': start, 'convention': convention, 'body_bytes': len(body), 'opening': body[:200].decode('utf-8', errors='replace')})
print(json.dumps({'content_sha256': expected_content, 'matches': matches}, ensure_ascii=False))
if not matches:
    lines = raw.decode('utf-8').splitlines()
    print('Content boundary unresolved; header and footer follow:')
    print('\n'.join(lines[:16]))
    print('\n'.join(lines[-8:]))
