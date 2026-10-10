from b4_finite_criterion import state,coeffs,plus_coeffs
from exact_local_probe import v
from pathlib import Path
import json
out=[]
for p,ks in [(5,[1,2,3]),(7,[1,2,3]),(13,[1,2]),(43,[1,2])]:
 for k in ks:
  for a in [1,2]:
   n=a*p**k-1;mod=p**24
   s=state(n,mod,4,1,coeffs(n),plus_coeffs(n))
   dv=v(s['D'],p);vv=v(s['V'],p)
   row=dict(p=p,k=k,a=a,n=n,precision=24,D_depth=dv,V_depth=vv,ratio_depth=(dv-vv) if dv is not None and vv is not None else None)
   out.append(row);print(row)
Path(__file__).with_name('b4_boundary_probe.json').write_text(json.dumps(out,indent=2))
