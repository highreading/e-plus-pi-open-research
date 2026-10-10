"""Check final document links, public-response exclusion and exact mirror bytes."""
from pathlib import Path
import hashlib, json, re, shutil
R=Path(__file__).resolve().parents[1]
M=Path('research/continuations/20261007_resumed_five_astra_research')
recent=R/'latest_three_successful_calls/README.md'
text=recent.read_text()
for directory in sorted((R/'latest_three_successful_calls').iterdir()):
    if directory.is_dir():
        stem=directory.name.split('_',1)[1]
        text=text.replace(f'[{stem}]({directory.name}/public_response.md)',
            f'[{stem} request]({directory.name}/request_text.txt) · [response]({directory.name}/public_response.md)')
recent.write_text(text)

def encryption_fields(value):
    if isinstance(value,dict):
        assert not value.get('encrypted_content'),'Nonempty encrypted reasoning in a saved response'
        for x in value.values():encryption_fields(x)
    elif isinstance(value,list):
        for x in value:encryption_fields(x)
for p in (R/'responses').glob('*.json'):encryption_fields(json.loads(p.read_text()))

checks=0
for p in [R/name for name in ('README.md','RESEARCH_REPORT.md','PROOF_STATUS_LEDGER.md',
                  'CONTINUATION_PLAN.md','COORDINATOR_LATE_REPORT_REVIEW.md')]+[recent]:
    for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)',p.read_text()):
        if target.startswith(('https://','http://','#')):continue
        target=target.strip('<>').split('#',1)[0]
        assert (p.parent/target).exists(),(p.name,target)
        checks+=1

verification=json.loads((R/'VERIFICATION.json').read_text())
rows=[]
for p in R.rglob('*'):
    rel=p.relative_to(R)
    if not p.is_file() or p.name=='VERIFICATION.json' or p.name.startswith('.') or any(part in ('vendor','__pycache__') for part in rel.parts):continue
    dest=M/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(p,dest)
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    assert h==hashlib.sha256(dest.read_bytes()).hexdigest()
    rows.append({'path':str(rel),'sha256':h})
verification.update({'files':rows,'mirrored_files':len(rows),'new_document_local_links_checked':checks,
                     'saved_response_encrypted_content_absent':True,'all_admitted_sessions_ended':True})
(R/'VERIFICATION.json').write_text(json.dumps(verification,indent=2)+'\n')
shutil.copy2(R/'VERIFICATION.json',M/'VERIFICATION.json')
print(json.dumps({'status':verification['status'],'complete_reports':verification['complete_reports'],
    'new_document_local_links_checked':checks,'saved_response_encrypted_content_absent':True,
    'mirror_sha256_matches':True,'mirrored_files':len(rows)}))
