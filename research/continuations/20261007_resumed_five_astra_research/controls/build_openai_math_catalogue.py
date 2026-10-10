"""Inventory every official family/abstract without executing downloaded source."""
from pathlib import Path
import re,json,hashlib
P=Path(__file__).resolve().parents[1]/'literature/openai_math_20261006'
s=(P/'CONTENTS.md').read_text();ov=(P/'overview.tex').read_text()
heads=list(re.finditer(r'\*\*(\d{3})\. ([^\n]+?)\*\*',s))
assert len(heads)==372
subjects=[(m.start(),m.group(1)) for m in
          re.finditer(r'\\cataloguesection\{([^}]+)\}\{\d+\}',ov)]
mapping={m.group(1):[z[1] for z in subjects if z[0]<m.start()][-1]
         for m in re.finditer(r'\\resultentry\{(\d{3})\}',ov)}
rows=[];dest=P/'catalogue_shards';dest.mkdir(exist_ok=True)
for i,h in enumerate(heads):
    body=s[h.start():heads[i+1].start() if i+1<len(heads) else len(s)]
    body=re.sub(r'</?(?:table|thead|tbody|tr|td|th)[^>]*>','',body)
    body=body.replace('&emsp;','');body=re.sub(r'\n{3,}','\n\n',body)
    # Whole-line matching retains parentheses in the CAT(0) manuscript path.
    links=re.findall(r'(?m)^[ \t]*\[(.+)\]\((preprints/.+\.pdf)\)[^\n]*$',body)
    rows.append({'family':h.group(1),'title':h.group(2).rstrip('.'),
                 'subject':mapping[h.group(1)],
                 'papers':[{'title':a,'path':b} for a,b in links],'body':body})
assert sum(len(x['papers']) for x in rows)==722
manifest=[]
for k in range(5):
    selected=rows[k::5]
    content=('# Official manuscript catalogue shard '+str(k+1)+' of 5\n\n'
             'Every abstract is a CLAIM in an official release, not a verified '
             'theorem. This shard includes the complete listed abstracts.\n\n'
             +'\n'.join('Subject: '+x['subject']+'\n'+x['body'] for x in selected))
    path=dest/('shard_'+str(k+1)+'.md');path.write_text(content)
    manifest.append({'shard':k+1,'families':[x['family'] for x in selected],
                     'paper_count':sum(len(x['papers']) for x in selected),
                     'bytes':len(content.encode()),
                     'sha256':hashlib.sha256(content.encode()).hexdigest()})
(P/'CATALOGUE_INVENTORY.json').write_text(json.dumps({
    'families':372,'manuscripts':722,
    'entries':[{a:b for a,b in x.items() if a!='body'} for x in rows],
    'shards':manifest,'scope':'Complete metadata and abstract inventory; '
                           'not full-paper reading.'},indent=2)+'\n')
for family in ('005','017','022'):
    x=next(x for x in rows if x['family']==family)
    (P/('FAMILY_'+family+'_CATALOGUE.md')).write_text(x['body'])
print(json.dumps({'families':372,'manuscripts':722,
                  'shards':[{'shard':x['shard'],'families':len(x['families']),
                             'papers':x['paper_count'],'bytes':x['bytes']}
                            for x in manifest]},indent=2))
