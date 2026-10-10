from pathlib import Path
import hashlib, difflib
base = Path('work/astra_review_registry/candidates')
texts = []
for version in (1, 2):
    path = base / f'worker2-fixed-b-projection-and-error-transfer-v{version}.md'
    raw = path.read_bytes()
    texts.append(raw.decode('utf-8'))
    print(path.name, 'bytes', len(raw), 'whole_file_sha256', hashlib.sha256(raw).hexdigest())
diff = list(difflib.unified_diff(texts[0].splitlines(), texts[1].splitlines(), fromfile='v1', tofile='v2', n=2))
print('\n'.join(diff))
correct = 'e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3'
print('correct_dependency_occurrences_in_v2', texts[1].count(correct))