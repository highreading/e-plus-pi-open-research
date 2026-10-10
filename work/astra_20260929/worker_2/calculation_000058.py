from pathlib import Path
import hashlib
import re

root = Path('[private local path removed]')
paths = {
    'transfer': 'work/astra_review_registry/candidates/worker2-fixed-b-projection-and-error-transfer-v1.md',
    'ordinary': 'work/astra_review_registry/candidates/worker3-ordinary-pade-prefactor-v1.md',
}
records = {}
for label, relative in paths.items():
    data = (root / relative).read_bytes()
    marker = data.index(b'Content SHA256: ')
    header_hash = data[marker:].splitlines()[0].split(b': ', 1)[1].decode()
    payload_start = data.index(b'\n\n', marker) + 2
    payload_hash = hashlib.sha256(data[payload_start:]).hexdigest()
    records[label] = {'path': relative, 'whole_file_sha256': hashlib.sha256(data).hexdigest(), 'payload_start': payload_start, 'payload_sha256': payload_hash, 'header_sha256': header_hash, 'header_matches_payload': header_hash == payload_hash}
    if label == 'transfer':
        dependency_hashes = re.findall(r'payload SHA-256 ([0-9a-f]+)', data.decode())

print(records)
print({'dependency_identifiers': [{'value': value, 'length': len(value), 'matches_ordinary_payload': value == records['ordinary']['payload_sha256']} for value in dependency_hashes]})
assert all(record['header_matches_payload'] for record in records.values())
assert records['transfer']['payload_sha256'] == 'f6eff74e903d1c74cc6373fce1df4256f87c392e028a7a3bdc59698aec4d7850'
assert records['ordinary']['payload_sha256'] == 'e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3'
