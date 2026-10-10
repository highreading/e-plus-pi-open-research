"""Minimal source-complete bounded packet writer for ongoing external work."""
import hashlib,json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent
ARC=Path('[private local path removed]')
def write_packets(turn,tasks,common,selected=None):
    selected=selected or list(tasks)
    manifest_path=HERE/f'turn{turn}_packet_manifest.json'
    old=json.loads(manifest_path.read_text()) if manifest_path.exists() else []
    manifests={v['agent']:v for v in old}
    for agent in selected:
        title,task,files,reports,controls=tasks[agent]
        parts=[common,'\nASSIGNMENT '+agent+': '+title+'\n'+task];docs=[]
        groups=[(ARC,files,'PRIOR ARCHIVE'),(HERE,[f'responses/{r}.md' for r in reports]+[f'controls/{r}' for r in controls],'CURRENT UNTRUSTED')]
        for source_root,rels,label in groups:
            for rel in rels:
                data=(source_root/rel).read_bytes();sha=hashlib.sha256(data).hexdigest()
                parts.append('\nBEGIN COMPLETE '+label+' SOURCE '+rel+'\nSHA256 '+sha+'\n'+data.decode()+'\nEND SOURCE\n')
                docs.append({'path':str(source_root/rel),'sha256':sha,'bytes':len(data)})
        prompt='\n'.join(parts);size=len(prompt.encode())
        assert size<230000,(agent,size)
        assert not re.search(r'sk-[A-Za-z0-9_-]{16,}',prompt)
        (HERE/'prompts'/f'{agent}_turn{turn}.txt').write_text(prompt)
        manifests[agent]={'agent':agent,'title':title,'bytes':size,'sources':docs}
        print(json.dumps({'agent':agent,'turn':turn,'bytes':size,'documents':len(docs)}))
    manifest_path.write_text(json.dumps([manifests[a] for a in sorted(manifests)],indent=2)+'\n')
