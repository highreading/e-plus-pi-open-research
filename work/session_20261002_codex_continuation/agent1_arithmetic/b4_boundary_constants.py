from pathlib import Path
from b4_finite_criterion import state,coeffs,plus_coeffs
import json
rows=[]
for p in [5,7,43,67,71]:
 n=p*p-1;prec=p**5
 d=state(n,prec,4,1,coeffs(n),plus_coeffs(n))
 assert d['D']%p**4==d['V']%p**4==0
 pn=d['J'][0]%p;assert pn
 inv=pow(pn,-1,p)
 row=dict(p=p,reference_n=n,modulus=str(prec),D_residue=d['D'],V_residue=d['V'],P_residue=pn,delta=(d['D']//p**4)*inv*inv%p,nu=(d['V']//p**4)*inv%p,state=d)
 assert row['nu']!=0
 rows.append(row);print({k:v for k,v in row.items() if k!='state'})
Path(__file__).with_name('b4_boundary_constants.json').write_text(json.dumps(rows,indent=2))
