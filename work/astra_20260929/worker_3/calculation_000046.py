from pathlib import Path
import hashlib
import json

path = Path('work/astra_review_registry/candidates/worker2-dyadic-linear-depth-residual-null-v1.md')
expected = 'a8be775b6a40b05145fc2a8e8938d43d4fb744325d57e97575d6d5fec033dd4b'
data = path.read_bytes()
marker = b'Status: unverified author submission; independent review required.'
assert data.count(marker) == 1
start = data.index(marker)
payload = data[start:]
declared = data.split(b'Content SHA256: ', 1)[1].splitlines()[0].decode('ascii')
actual = hashlib.sha256(payload).hexdigest()
report = {
    'file_bytes': len(data),
    'file_sha256': hashlib.sha256(data).hexdigest(),
    'payload_byte_offset': start,
    'payload_bytes': len(payload),
    'payload_sha256': actual,
    'declared_sha256': declared,
    'matches_assignment': actual == expected == declared
}
print(json.dumps(report, indent=2))
assert actual == expected == declared
