from pathlib import Path
import hashlib
import json

# Read-only provenance check. Do not execute the reconstruction source.
project_root = Path('[private local path removed]')
artifacts = [
    ('work/astra_20260929/worker_4/calculation_000100.py', '3d153b7ea4a1b6b6006eaf0a44b3227fffeaadb38f2d30008e9f7fa12827eeb3'),
    ('work/astra_20260929/worker_4/note_000101.md', '62481c6468d84f44c41099130f2bef1a0bb14a619437de7d386d1dadbef8f0b0'),
    ('work/astra_20260929/worker_4/note_000105.md', 'cf3d9cb8c0476fe3b415394dc3050247d1e494e6572ec6d6ef09c23f654314a8'),
]
records = []
source_text = None
for relative_path, recorded_digest in artifacts:
    artifact_bytes = (project_root / relative_path).read_bytes()
    actual_digest = hashlib.sha256(artifact_bytes).hexdigest()
    records.append({
        'path': relative_path,
        'bytes': len(artifact_bytes),
        'sha256': actual_digest,
        'matches_supplied_reading_ledger': actual_digest == recorded_digest,
    })
    if relative_path.endswith('calculation_000100.py'):
        source_text = artifact_bytes.decode('utf-8')
print(json.dumps({
    'artifacts': records,
    'reconstruction_executed': False,
    'source_text': source_text,
}, ensure_ascii=False, indent=2))