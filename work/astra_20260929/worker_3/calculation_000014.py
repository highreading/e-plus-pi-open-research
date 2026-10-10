from pathlib import Path
import hashlib
p=Path('work/astra_review_registry/candidates/conditional-dyadic-depth-and-index-gaps.md')
b=p.read_bytes()
target='29db0d226d2991d949f69ee25fe70b23795e8c56ff01ad7459c5dacae39f7ba8'
print('file_bytes',len(b),'file_sha256',hashlib.sha256(b).hexdigest())
print('header_preview',repr(b[:1200].decode('utf-8')))
lines=b.splitlines(keepends=True)
matches=[]
for start in range(len(lines)):
    suffix=b''.join(lines[start:])
    variants={'exact':suffix,'rstrip_newlines':suffix.rstrip(b'\r\n'),'strip_whitespace':suffix.strip(),'strip_plus_newline':suffix.strip()+b'\n'}
    for normalization,data in variants.items():
        if hashlib.sha256(data).hexdigest()==target:
            matches.append({'body_start_line':start+1,'normalization':normalization,'bytes':len(data)})
print('registry_hash_body_matches',matches)
print('No file was modified; identity checks alone do not constitute mathematical approval.')