"""Main-only mechanical preflight. No mathematical judgment or archive mutation."""
from pathlib import Path
import datetime
import gzip
import hashlib
import json
import re
import sqlite3

BASE = Path(__file__).resolve().parent
ROOT = Path('[private local path removed]')
CAND = BASE / 'assistant3_organization/graph_refresh_20261004_main181_candidate'
TREE = CAND / 'staged_tree/reviews/provenance_graph'
sha = lambda data: hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def pointer(value, text):
    assert text == '' or text.startswith('/')
    for token in text.split('/')[1:]:
        token = token.replace('~1', '/').replace('~0', '~')
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value


def readonly(path):
    con = sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True)
    con.row_factory = sqlite3.Row
    return con


def runtime(path):
    assert isinstance(path, str) and not re.search(r'[\x00-\x1f]', path)
    assert not re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', path)
    p = Path(path) if path.startswith('/') else ROOT / path
    assert p.is_absolute() and p.is_relative_to(ROOT)
    assert not any(x in ('.', '..') for x in path.split('/'))
    assert p.exists(), path
    return p


manifest = [json.loads(line) for line in (CAND / 'SEALED_MANIFEST.jsonl').read_text().splitlines()]
assert len(manifest) == 85
for row in manifest:
    p = CAND / row['path']
    assert p.resolve().is_relative_to(CAND.resolve())
    raw = p.read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256'], row['path']
plan = load(CAND / 'candidate_refresh_plan.json')
assert len(plan['operations']) == 4 and plan['not_installed'] is True
for op in plan['operations']:
    old = (ROOT / op['formal_archive_path']).read_bytes()
    new = Path(op['candidate_source_path']).read_bytes()
    assert len(old) == op['original_bytes'] and sha(old) == op['original_sha256']
    assert len(new) == op['candidate_bytes'] and sha(new) == op['candidate_sha256']

old_graph = json.loads(gzip.decompress((ROOT / plan['operations'][0]['formal_archive_path']).read_bytes()))
graph = json.loads(gzip.decompress((TREE / 'PROVENANCE_GRAPH.json.gz').read_bytes()))
snapshot = load(TREE / 'MAIN_REGISTER_REFERENCE_SNAPSHOT.json')
assert old_graph['main_reviewed_count'] == 107
assert graph['main_reviewed_count'] == snapshot['main_reviewed_count'] == 181
assert graph['pending_count'] == snapshot['pending_count'] == 2597
assert graph['main_reviewed_embedded_count'] == snapshot['main_reviewed_embedded_count'] == 7
assert graph['embedded_prose_count'] == snapshot['embedded_prose_count'] == 13344
assert graph['pending_embedded_count'] == snapshot['pending_embedded_count'] == 13337
assert graph['main_audit_complete'] is snapshot['main_audit_complete'] is False
assert graph['full_archive_mathematical_review_complete'] is False
assert snapshot['full_archive_math_review_complete'] is False
assert graph['edges'] == old_graph['edges'] and len(graph['edges']) == 16758
assert len(graph['nodes']) == len(old_graph['nodes']) == 13680
audit_keys = {'main_label_source', 'main_document_status', 'main_registration_key', 'main_register_ref', 'main_registered'}
changed_counts = {k: 0 for k in audit_keys}
for before, after in zip(old_graph['nodes'], graph['nodes']):
    assert {k: v for k, v in before.items() if k not in audit_keys} == {
        k: v for k, v in after.items() if k not in audit_keys}, after['id']
    for key in audit_keys:
        changed_counts[key] += (before.get(key) != after.get(key))
    runtime(after['view_path'])
for key in ['historical_version_records', 'entry_version_ledger', 'unresolved_edge_count',
            'runtime_open_root', 'runtime_open_targets_are_formal_archive_paths']:
    assert graph[key] == old_graph[key], key
assert graph['main_audit_records'] == {'rows': snapshot['rows'], 'embedded_rows': snapshot['embedded_rows']}

contract = load(CAND / 'html_projection_contract.json')
projection = {k: graph[k] for k in contract['projection_top_level_keys']}
html = (TREE / 'PROVENANCE_SEARCH.html').read_text(encoding='utf-8')
start = '<script id="data" type="application/json">'
assert html.count(start) == 1
head, rest = html.split(start)
data, tail = rest.split('</script>', 1)
assert json.loads(data) == projection
assert '<' not in data and '>' not in data and '\u2028' not in data and '\u2029' not in data
template = head + start + '@@SAFE_JSON_DATA@@</script>' + tail
assert template == (CAND / 'association_viewer_without_data.html').read_text(encoding='utf-8')
css = re.search(r'<style>(.*?)</style>', template, re.S).group(1)
js = tail.split('<script>', 1)[1].split('</script>', 1)[0]
assert css == (CAND / 'association_viewer_complete_css.css').read_text(encoding='utf-8')
assert js == (CAND / 'association_viewer_complete_js.js').read_text(encoding='utf-8')
assert not re.search(r'\b(fetch|XMLHttpRequest|eval)\s*\(|innerHTML\s*=|document\.write', js)
assert "connect-src 'none'" in template and "default-src 'none'" in template
for target in re.findall(r'href="([^"]+)"', template):
    runtime(target)

frozen_path = CAND / 'inputs/main181.sqlite3'
assert sha(frozen_path.read_bytes()) == '52a1e653fabd69a1cd8f89d8b43d760bb1f19b752453454fa51ca8efead15518'
frozen = readonly(frozen_path)
live = readonly(BASE / 'audit.sqlite3')
assert frozen.execute("SELECT count(*) FROM documents WHERE status='audited'").fetchone()[0] == 181
versions = {r['original_path']: r for r in load(ROOT / 'reviews/ENTRY_VERSION_CHANGES.json')}
baseline_count = 0
for row in live.execute('SELECT * FROM files WHERE sha256 IS NOT NULL'):
    p = ROOT / (versions[row['path']]['preserved_path'] if row['path'] in versions else row['path'])
    raw = p.read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256'], row['path']
    baseline_count += 1
assert baseline_count == 13619


def batches(record):
    assert record['exact_batch_coordinates']
    for coord in record['exact_batch_coordinates']:
        p = Path(coord['source_read_path'])
        assert p.parent == BASE and re.fullmatch(r'main_(?:embedded_)?reviews_\d{4}\.json', p.name)
        assert sha(p.read_bytes()) == coord['source_sha256']
        value = pointer(load(p), coord['json_pointer'])
        for key in ['reviewer', 'read_in_full', 'verdict', 'scope', 'reason']:
            assert value[key] == record[key], (record['record_key'], key)
        if record['source_kind'] == 'standalone_document':
            assert value['path'] == record['path']
        else:
            for key in ['source_json_path', 'json_pointer', 'source_json_raw_sha256', 'decoded_field_raw_sha256']:
                assert value[key] == record[key]


records = {}
for index, record in enumerate(snapshot['rows']):
    assert record['read_in_full'] is True and record['reviewer'] == 'main Codex'
    ident = record['document_id']
    review_id = record['db_coordinate']['reviews_id']
    for con in [frozen, live]:
        doc = con.execute('SELECT * FROM documents WHERE id=?', (ident,)).fetchone()
        rev = con.execute('SELECT * FROM reviews WHERE id=?', (review_id,)).fetchone()
        assert doc['status'] == 'audited' and doc['sha256'] == record['sha256']
        assert doc['representative'] == record['baseline_representative']
        assert rev['document_id'] == ident and rev['created_at'] == record['reviewed_at']
        assert sorted(record['all_baseline_paths']) == [r[0] for r in con.execute(
            'SELECT path FROM document_paths WHERE document_id=? ORDER BY path', (ident,))]
        for key in ['reviewer', 'verdict', 'scope', 'reason']:
            assert rev[key] == record[key]
        notes = json.loads(doc['review_notes'])
        for key in ['path', 'reviewer', 'read_in_full', 'verdict', 'scope', 'reason']:
            assert notes[key] == record[key]
    batches(record)
    assert record['runtime_snapshot_pointer'] == f'/rows/{index}'
    runtime(record['runtime_snapshot_path']); runtime(record['runtime_latest_main_register_path'])
    records[record['record_key']] = record

for index, record in enumerate(snapshot['embedded_rows']):
    for con in [frozen, live]:
        rev = con.execute('SELECT * FROM embedded_reviews WHERE id=?', (record['embedded_review_id'],)).fetchone()
        assert rev['file_path'] == record['source_json_path'] and rev['json_pointer'] == record['json_pointer']
        assert rev['source_file_sha256'] == record['source_json_raw_sha256']
        assert rev['body_sha256'] == record['decoded_field_raw_sha256']
        assert rev['created_at'] == record['reviewed_at'] and rev['read_in_full'] == 1
        for key in ['reviewer', 'verdict', 'scope', 'reason']:
            assert rev[key] == record[key]
    raw = (ROOT / record['source_json_path']).read_bytes()
    assert sha(raw) == record['source_json_raw_sha256']
    body = pointer(json.loads(raw), record['json_pointer'])
    assert isinstance(body, str) and sha(body.encode('utf-8')) == record['decoded_field_raw_sha256']
    batches(record)
    assert record['runtime_snapshot_pointer'] == f'/embedded_rows/{index}'
    runtime(record['runtime_snapshot_path']); runtime(record['runtime_latest_main_register_path'])
    records[record['record_key']] = record

registered_path_nodes = 0
native_nodes = 0
for node in graph['nodes']:
    if not node.get('main_registered'):
        continue
    record = records[node['main_registration_key']]
    ref = node['main_register_ref']
    assert pointer(snapshot, ref['json_pointer']) == record
    runtime(ref['path'])
    if record['source_kind'] == 'standalone_document':
        assert node['sha256'] == record['sha256'] and node['path'] in record['all_baseline_paths']
        registered_path_nodes += 1
    else:
        assert node['sha256'] == record['decoded_field_raw_sha256']
        assert node['content_epoch'] == 'original_embedded_field'
        native_nodes += 1
assert registered_path_nodes == 205 and native_nodes == 7
result = {'at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'main_own_mechanical_verification': True, 'sealed_files_verified': 85,
          'baseline_original_files_SHA_verified': baseline_count,
          'old_nodes_and_non_audit_fields_preserved': 13680, 'old_edges_preserved': 16758,
          'audit_label_field_change_counts': changed_counts,
          'exact_frozen_standalone_reviews': 181, 'exact_native_reviews': 7,
          'live_standalone_reviews': live.execute("SELECT count(*) FROM documents WHERE status='audited'").fetchone()[0],
          'registered_path_nodes': registered_path_nodes, 'registered_native_field_nodes': native_nodes,
          'HTML_uncropped_projection_and_whole_authored_template_match': True,
          'all_runtime_targets_exist': True, 'all_verdict_scope_reason_match_main_DB_and_batches': True,
          'no_new_math_judgment_or_scope_change': True, 'main_audit_complete': False, 'passed': True}
(BASE / 'MAIN_GRAPH_181_PREFLIGHT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False))
