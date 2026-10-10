from pathlib import Path
import json,hashlib
BASE=Path(__file__).parent
probe=BASE/'h2_boundary_probe.json'
sources=[BASE/'b4_finite_criterion.json',BASE/'residue_atlas.json']
probe_rows=json.loads(probe.read_text())
seed_rows={r['p']:r for r in json.loads(sources[0].read_text())['rows']}
seed_rows.update({r['p']:r for r in json.loads(sources[1].read_text())})
out=[]
for p in [7,13]:
 row=next(r for r in probe_rows if r['p']==p and r['k']==2 and r['a']==1)
 seeds=seed_rows[p]['states'];Ps=[s['J'][0] for s in seeds]
 assert len(Ps)==p and all(Ps)
 modulus=p**5;D=row['state']['D']%modulus;V=row['state']['V']%modulus;P=row['P_residue']
 assert D%p**4==0 and V%p**4==0
 delta=D//p**4*pow(P,-2,p)%p;nu=V//p**4*pow(P,-1,p)%p
 assert delta==row['delta'] and nu==row['nu'] and nu
 out.append(dict(p=p,b=5,m=1,h=2,reference_n=p*p-2,modulus=str(modulus),D=D,V=V,P=P,delta=delta,nu=nu,P_digit_residues=Ps))
cert=dict(status='author finite inputs to the separately written all-depth h2 chart; no whole b5 criterion',references=out,sources=[dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in [probe]+sources])
(BASE/'H2_BOUNDARY_REFERENCE_CERTIFICATE.json').write_text(json.dumps(cert,indent=2))
print(json.dumps(out,indent=2))
