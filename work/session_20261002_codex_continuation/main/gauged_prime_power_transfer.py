"""New exact finite prime-power transfer checks; no old analytic certificate replay."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb
import json
SESSION=Path('work/session_20261002_codex_continuation')
cases=[('linear',[Q(0),Q(1)],(3,11),4),('cubic',[Q(0),Q(1),Q(-1,2),Q(1,2)],(3,11),4)]
ks=json.loads((SESSION/'main/EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json').read_text())['endpoint_basis_integers'];P=[Q(0)]*(len(ks)+2);P[1]=Q(1)
for k,v in enumerate(ks,1):P[k]+=Q(v,factorial(k));P[k+1]-=Q(v,factorial(k))
cases.append(('degree81',P,(83,),2))
def vp(n,p):
 if n==0:return 1000000
 s=0
 while n%p==0:n//=p;s+=1
 return s
def floorlog(n,p):
 s=0
 while n>=p:n//=p;s+=1
 return s
def cutoff(p,k,logloss):
 j=0;s=0
 while True:
  j+=1;s+=vp(j,p)
  if s-(floorlog(j,p) if logloss else 0)>=k:return j
rows=[]
for name,P,ps,Kmax in cases:
 d=len(P)-1;pj=[int(v*factorial(k)) for k,v in enumerate(P)]
 maxJ=max(cutoff(p,Kmax,True) for p in ps)
 qq=[2]+[sum(comb(j,k)*pj[k]*pj[j-k] for k in range(max(0,j-d),min(d,j)+1))-(2*pj[j] if j<=d else 0) for j in range(1,2*d+1)]
 G=[0];CC=[0]
 for n in range(1,maxJ):
  val=(4*pj[n] if n<=d else 0)-sum(comb(n-1,k)*qq[k]*G[n-k] for k in range(1,min(2*d,n-1)+1))
  assert val%2==0;G.append(val//2);CC.append(-n*CC[-1]+(-1)**n*G[-1])
 for p in ps:
  assert all(v.denominator%p for v in P)
  chi=1 if p%4==1 else -1;pr=[]
  for k in range(1,Kmax+1):
   mod=p**k;J=cutoff(p,k,True);JD=cutoff(p,k,False)
   assert J<=2*p*(k+1)
   for j in range(1,J):assert vp(CC[j],p)>=vp(factorial(j),p)-floorlog(j,p)
   def Dvalue(N):
    f=1;s=1
    for j in range(1,min(N,JD-1)+1):f=f*(N-j+1)%mod;s=(s+(-1)**j*f)%mod
    return s
   def Cvalue(N):return sum(comb(N,j)*(CC[j]%mod) for j in range(min(N,J-1)+1))%mod
   def original_convolution(N):return sum((-1)**j*(comb(N,j)%mod)*(G[j]%mod)*Dvalue(N-j) for j in range(1,min(N,JD)+1))%mod
   witnesses=list(range(0,2*p+3))+[10**20+J,10**20+J+p,p**(k+2)+1]
   for N in witnesses:
    c=Cvalue(N);dv=Dvalue(N)
    assert (Cvalue(N+p**k)-c-p**(k-1)*chi*G[1]*dv)%mod==0
    assert (Cvalue(N+p**(k+1))-c)%mod==0
    if dv%p==0:assert (Cvalue(N+p**k)-c)%mod==0
   for N in [0,1,J,J+1,2*J+3,10**20+J,p**(k+2)+1]:assert Cvalue(N)==original_convolution(N)
   pr.append({'depth':k,'modulus':mod,'C_degree_bound':J-1,'D_degree_bound':JD-1,'C_global_period_bound':p**(k+1),'C_on_denominator_root_period_bound':p**k,'new_shift_checks':len(witnesses),'independent_original_convolution_checks':7,'C_at_p_power':Cvalue(p**k),'expected_C_at_p_power':p**(k-1)*chi*G[1]%mod})
  rows.append({'case':name,'p':p,'chi':chi,'g1':G[1],'depths':pr})
out={'status':'PASS_EXACT_NEW_ALL_DEPTH_CARRY_TRANSFER_RECEIPT','scope':'Author all-depth theorem proved separately; finite checks at indicated depths using an independent original binomial-convolution interface. No global prime-supply or e+pi proof.','rows':rows}
(SESSION/'main/GAUGED_PRIME_POWER_TRANSFER_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],[(r['case'],r['p'],len(r['depths'])) for r in rows])
