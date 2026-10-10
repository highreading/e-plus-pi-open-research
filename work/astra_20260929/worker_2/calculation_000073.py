from pathlib import Path
import json
root = Path('[private local path removed]')
folders = ['work/session_20260913', 'work/session_20260927', 'work/astra_20260929/worker_1', 'work/astra_20260929/worker_4']
results = {}
for folder in folders:
    directory = root / folder
    if not directory.is_dir():
        results[folder] = {'missing': True}
        continue
    matches = []
    for item in directory.iterdir():
        if not item.is_file():
            continue
        name = item.name.lower()
        if 'b2' in name or 'endpoint' in name or (folder.startswith('work/astra_20260929/') and item.suffix.lower() == '.json'):
            matches.append({'path': str(item.relative_to(root)), 'bytes': item.stat().st_size})
    matches.sort(key=lambda x: x['path'])
    results[folder] = {'count': len(matches), 'files': matches[:100], 'truncated': len(matches) > 100}
print(json.dumps(results, indent=2))