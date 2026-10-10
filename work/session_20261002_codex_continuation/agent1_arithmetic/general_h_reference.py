from pathlib import Path
import json
from b4_finite_criterion import state,plus_coeffs
from residue_atlas import coeffs
BASE=Path(__file__).parent
p,b,m,h=13,7,2,3;n=p*p-h;mod=p**7
s=state(n,mod,b,m,coeffs(n),plus_coeffs(n));P=s['J'][0]%p
assert P and s['D']%p**4==0 and s['V']%p**4==0
delta=(s['D']//p**4)*pow(P,-2,p)%p;nu=(s['V']//p**4)*pow(P,-1,p)%p
out=dict(status='single new bounded reference, not infinite proof',p=p,b=b,m=m,h=h,n=n,modulus=str(mod),P=P,delta=delta,nu=nu,state=s)
(BASE/'general_h_reference.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:out[k] for k in ['p','b','m','h','n','P','delta','nu']},indent=2))
