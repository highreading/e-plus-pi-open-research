from pathlib import Path
import json
from b4_finite_criterion import state,plus_coeffs
from residue_atlas import coeffs
BASE=Path(__file__).parent

def vp(a,p,maxprec):
 if not a:return maxprec
 v=0
 while a%p==0:v+=1;a//=p
 return v

out=[]
for p in [7,13]:
 precision=10;mod=p**precision
 for k,a in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)]+([(3,1)] if p==7 else []):
  n=a*p**k-2;u=n+2
  s=state(n,mod,5,1,coeffs(n),plus_coeffs(n));P=s['J'][0]%p
  assert P
  vd=vp(s['D'],p,precision);vv=vp(s['V'],p,precision)
  assert vd>=2*k and vv>=2*k
  delta=s['D']//p**(2*k)*pow((u//p**k)*P,-2,p)%p
  nu=s['V']//p**(2*k)*pow((u//p**k)**2*P,-1,p)%p
  out.append(dict(p=p,b=5,m=1,h=2,a=a,k=k,n=n,modulus=str(mod),D_depth=vd,V_depth=vv,P_residue=P,delta=delta,nu=nu,state=s))
  print(p,a,k,n,vd,vv,delta,nu,flush=True)
(BASE/'h2_boundary_probe.json').write_text(json.dumps(out,indent=2))
