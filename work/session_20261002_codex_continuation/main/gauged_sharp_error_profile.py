"""New exact endpoint arrays and numerical asymptotic profiles. Not a proof by data."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb
import json,mpmath as mp
mp.mp.dps=190
SESSION=Path('work/session_20261002_codex_continuation')
cases=[('linear',[Q(0),Q(1)]),('cubic',[Q(0),Q(1),Q(-1,2),Q(1,2)])]
records=[]
for name,P in cases:
 d=len(P)-1;pj=[int(v*factorial(k)) for k,v in enumerate(P)]
 assert sum(P)==1 and all(P[k]*factorial(k)==pj[k] for k in range(d+1))
 Qjets=[2]+[sum(comb(j,k)*pj[k]*pj[j-k] for k in range(max(0,j-d),min(d,j)+1))-(2*pj[j] if j<=d else 0) for j in range(1,2*d+1)]
 G=[0];D=[1];B=[1]
 N=360
 for n in range(1,N+1):
  z=(4*pj[n] if n<=d else 0)-sum(comb(n-1,k)*Qjets[k]*G[n-k] for k in range(1,min(2*d,n-1)+1))
  assert z%2==0;G.append(z//2);assert G[-1]%2==0
  u=sum(comb(n,j)*(-1)**(n-j)*G[j] for j in range(n+1))
  D.append(n*D[-1]+(-1)**n);B.append(n*B[-1]+u)
  assert B[-1]==factorial(n)+sum(comb(n,j)*G[j]*D[n-j] for j in range(n+1))
 roots=[]
 for sign in (1,-1):
  cc=[mp.mpf(v.numerator)/v.denominator for v in P];cc[0]-=1+sign*1j
  rs=mp.polyroots(list(reversed(cc)),maxsteps=100)
  roots.extend((r,-sign*2j) for r in rs)
 R=min(abs(r) for r,L in roots)
 rows=[]
 for n in (40,80,120,180,240,360):
  err=mp.mpf(B[n])/D[n]-mp.e-mp.pi
  lead=sum(L*mp.exp(1-r)/(r-1)*r**(-n)/n for r,L in roots)
  second=sum(L*mp.exp(1-r)/(r-1)*r**(-n)/n*(1-r*r/((r-1)*n)) for r,L in roots)
  rows.append({'n':n,'complete_error':mp.nstr(err,24),'normalized_first_order_residual':mp.nstr(abs(err-lead)*R**n*n*n,18),'normalized_second_order_residual':mp.nstr(abs(err-second)*R**n*n**3,18)})
 records.append({'name':name,'P':[str(v) for v in P],'N_exact_endpoint_identity_checks':N,'diagnostic_R0':mp.nstr(R,24),'profile':rows})
out={'status':'PASS_NEW_EXACT_ENDPOINT_IDENTITIES_PLUS_NUMERICAL_PROFILE','scope':'Exact rational identities n1..360; floating root/asymptotic profiles are diagnostics only. General theorem is proved in GAUGED_FIXED_PULLBACK_SHARP_BLOCK_ERROR.md.','cases':records}
(SESSION/'main/GAUGED_SHARP_ERROR_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n')
for x in records:print(x['name'],'R0',x['diagnostic_R0'],'last profile',x['profile'][-1])
