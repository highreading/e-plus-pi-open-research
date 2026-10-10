"""Compare complete report ledgers against pinned catalogue, not narrative totals."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parents[1]
P=R/'literature/openai_math_20261006'
inv=json.loads((P/'CATALOGUE_INVENTORY.json').read_text())
entries={x['family']:x for x in inv['entries']}
targets={1:'A1_turn15',2:'A2_turn12',3:'A3_turn9',4:'A4_turn14',5:'A5_turn9'}
receipts=[]
for shard,stem in targets.items():
    source=R/'responses'/f'{stem}.md'
    expected=next(x for x in inv['shards'] if x['shard']==shard)
    if not source.exists():
        receipts.append({'shard':shard,'report':stem,'status':'pending','papers':expected['paper_count']})
        continue
    text=source.read_text().replace('**','')
    rows=re.findall(r'(?m)^\|\s*(\d{3})\s*\|\s*(\d+)\s*\|',text)
    parsed={f:int(n) for f,n in rows}
    assert len(rows)==len(parsed)==len(expected['families'])
    assert set(parsed)==set(expected['families'])
    assert all(parsed[f]==len(entries[f]['papers']) for f in parsed)
    assert sum(parsed.values())==expected['paper_count']
    receipts.append({'shard':shard,'report':stem,'status':'ledger_exactly_matches',
                     'families':len(parsed),'papers':sum(parsed.values()),
                     'report_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                     'shard_sha256':expected['sha256'],
                     'scope':'Complete abstract screen; not full mathematical proof review.'})
data={'catalogue_families':372,'catalogue_papers':722,'receipts':receipts,
      'screened_families':sum(x.get('families',0) for x in receipts),
      'screened_papers':sum(x['papers'] for x in receipts if x['status']!='pending'),
      'parent_errata':[{'report':'A5_turn9','narrative_total':139,'actual_ledger_total':141,
                       'consequence':'Narrative addition error only; all 74 families and 141 paper counts match. Raw response retained.'}]}
(R/'controls/CATALOGUE_SCREEN_COVERAGE_CERTIFICATE.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'screened_families':data['screened_families'],'screened_papers':data['screened_papers'],
                  'pending_reports':[x['report'] for x in receipts if x['status']=='pending']}))
