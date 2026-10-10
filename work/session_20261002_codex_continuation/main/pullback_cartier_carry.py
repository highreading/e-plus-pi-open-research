"""New finite exact checks of the twisted Cartier coefficient and universal carry law."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb,lcm
import json,hashlib
SESSION=Path('work/session_20261002_codex_continuation')
cases=[('linear',[Q(0),Q(1)],None),('cubic',[Q(0),Q(1),Q(-1,2),Q(1,2)],None)]
for degree,filename in [(61,'EXPLICIT_DEGREE61_RADIUS198_CERTIFICATE.json'),(81,'EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json')]:
 raw=(SESSION/'main'/filename).read_bytes();ks=json.loads(raw)['endpoint_basis_integers'];P=[Q(0)]*(len(ks)+2);P[1]=Q(1)
 for k,v in enumerate(ks,1):P[k]+=Q(v,factorial(k));P[k+1]-=Q(v,factorial(k))
 cases.append(('degree'+str(degree),P,hashlib.sha256(raw).hexdigest()))
primes=[p for p in range(3,200,2) if all(p%q for q in range(2,int(p**.5)+1))]
rows=[]
for name,P,sha in cases:
 den=lcm(*(v.denominator for v in P));d=len(P)-1;rr=[]
 for p in primes:
  if den%p==0:continue
  pp=[v.numerator*pow(v.denominator,-1,p)%p for v in P]
  qq=[0]*(2*d+1);qq[0]=2
  for j in range(1,2*d+1):qq[j]=(sum(pp[k]*pp[j-k] for k in range(max(0,j-d),min(d,j)+1))-(2*pp[j] if j<=d else 0))%p
  M=max(8*p,p*p if len(rr)<2 else 0);aa=[];inv2=pow(2,-1,p)
  for n in range(M):aa.append(((4*(n+1)*pp[n+1] if n+1<=d else 0)-sum(qq[j]*aa[n-j] for j in range(1,min(2*d,n)+1)))*inv2%p)
  chi=1 if p%4==1 else -1
  for k in range(8):assert aa[p*(k+1)-1]==chi*aa[k]%p
  gg=[0];ff=1
  for n in range(1,M+1):
   if n>1:ff=ff*(n-1)%p
   gg.append(ff*aa[n-1]%p)
  assert gg[p]==-chi*gg[1]%p
  D=[1];B=[1];fac=[1];pascal=[1]+[0]*p
  if len(rr)<2:assert aa[p*p-1]==gg[1]%p
  for n in range(1,5*p+1):
   for j in range(min(n,p),0,-1):pascal[j]=(pascal[j]+pascal[j-1])%p
   u=sum(pascal[j]*(-1)**(n-j)*gg[j] for j in range(min(n,p)+1))%p
   D.append((n*D[-1]+(-1)**n)%p);B.append((n*B[-1]+u)%p);fac.append(n*fac[-1]%p)
   if n>=p:
    a,r=divmod(n,p)
    assert D[n]==(-1)**a*D[r]%p
    assert B[n]==(-1)**a*(B[r]-fac[r]+a*chi*gg[1]*D[r])%p
  rr.append({'p':p,'chi':chi,'p_jet':gg[p],'g1':gg[1],'cartier_rows_k':[0,7],'carry_check_to_n':5*p,'p_squared_normalized_jet_checked':len(rr)<2})
 rows.append({'case':name,'degree':d,'source_sha256':sha,'good_primes':rr})
out={'status':'PASS_EXACT_NEW_TWISTED_CARTIER_AND_UNIVERSAL_GAUGED_CARRY','scope':'Finite exact characteristic-p checks only; all-prime/all-index theorem is the root proof in PULLBACK_TWISTED_CARTIER_AND_CARRY.md. No p^2 or favorable-global-gcd claim.','cases':rows}
(SESSION/'main/PULLBACK_CARTIER_CARRY_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],[(x['case'],len(x['good_primes'])) for x in rows])
