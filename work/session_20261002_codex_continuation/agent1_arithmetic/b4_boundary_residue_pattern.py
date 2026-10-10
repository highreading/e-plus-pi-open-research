from b4_finite_criterion import state,coeffs,plus_coeffs
from pathlib import Path
import json
out=[]
for p in [5,7]:
 for k in [1,2,3]:
  for a in range(1,p):
   n=a*p**k-1;mod=p**16;u=p**k*a
   d=state(n,mod,4,1,coeffs(n),plus_coeffs(n))
   assert d['D']%p**(2*k)==d['V']%p**(2*k)==0
   pn=d['J'][0]%p;inv=pow(pn,-1,p);sign=1 if p%4==1 else p-1
   theta=sign*(4*d['J'][1]-2*pn)*inv%p
   vn=(d['V']//p**(2*k))*pow(a*a,-1,p)*inv%p
   dn=(d['D']//p**(2*k))*pow(a*a,-1,p)*inv*inv%p
   row=dict(p=p,k=k,a=a,n=n,P=pn,theta=theta,V_boundary_norm=vn,D_boundary_norm=dn)
   out.append(row);print(row)
Path(__file__).with_name('b4_boundary_residue_pattern.json').write_text(json.dumps(out,indent=2))
