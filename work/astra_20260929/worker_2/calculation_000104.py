from pathlib import Path
import hashlib
root = Path('[private local path removed]')
rel = 'work/astra_review_registry/candidates/w3-b2-five-multiples-obstruction-v1.md'
data = (root / rel).read_bytes()
expected = '997d4e294246e29dbb36126bced5fc1507e46540ae607b48d2eb9f86cb447f7e'
starts = [0] + [i + 1 for i, c in enumerate(data) if c == 10]
matches = [i for i in starts if hashlib.sha256(data[i:]).hexdigest() == expected]
print({'path': rel, 'byte_length': len(data), 'whole_file_sha256': hashlib.sha256(data).hexdigest(), 'expected_payload_sha256': expected, 'matching_payload_start_offsets': matches, 'payload_match': len(matches) == 1})