"""New fixed polynomial amplitude endpoint and carry checks."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb,gcd
import json,hashlib
S=Path('work/session_20261002_codex_continuation')
raw=(S/'main/EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json').read_bytes()
ks=json.loads(raw)['endpoint_basis_integers'];P=[Q(0)]*82;P[1]=Q(1)
for j,v in enumerate(ks,1):P[j]+=Q(v,factorial(j));P[j+1]-=Q(v,factorial(j))
pj=[int(v*factorial(j)) for j,v in enumerate(P)];d=len(pj)-1;M=420
qq=[2]+[sum(comb(j,a)*pj[a]*pj[j-a] for a in range(max(0,j-d),min(d,j)+1))-(2*pj[j] if j<=d else 0) for j in range(1,2*d+1)]
G,u,D,B,CC=[0],[0],[1],[1],[0]
for n in range(1,M+1):
 val=(4*pj[n] if n<=d else 0)-sum(comb(n-1,a)*qq[a]*G[n-a] for a in range(1,min(2*d,n-1)+1))
 assert val%4==0;G.append(val//2)
 u.append(sum(comb(n,j)*(-1)**(n-j)*G[j] for j in range(n+1)))
 D.append(n*D[-1]+(-1)**n);B.append(n*B[-1]+u[-1]);CC.append(-n*CC[-1]+(-1)**n*G[-1])
def vp(n,p):
 if n==0:return 1000000
 k=0
 while n%p==0:n//=p;k+=1
 return k
def fl(n,p):
 k=0
 while n>=p:n//=p;k+=1
 return k
def cutoff(p,k,loss):
 j=0;s=0
 while True:
  j+=1;s+=vp(j,p)
  if s-(fl(j,p) if loss else 0)>=k:return j
def falling(x,j):
 f=1
 for t in range(j):f*=x-t
 return f
rows=[]
for name,aa in [('linear_1minus2z',[1,-2]),('quadratic_1plusz2',[1,0,1]),('quadratic_1minus2zplus2z2',[1,-2,2])]:
 m=len(aa)-1;alpha=[a*factorial(j) for j,a in enumerate(aa)];A1=sum(aa);assert A1!=0
 da=[alpha[0]];ba=[A1]
 for n in range(1,141):
  hn=sum(comb(n,j)*alpha[j]*(-1)**(n-j) for j in range(min(m,n)+1))
  vn=sum(comb(n,j)*alpha[j]*u[n-j] for j in range(min(m,n)+1))
  da.append(n*da[-1]+hn);ba.append(n*ba[-1]+vn)
  if n>=m:
   assert da[n]==sum(comb(n,j)*alpha[j]*D[n-j] for j in range(m+1))
   assert ba[n]==sum(comb(n,j)*alpha[j]*B[n-j] for j in range(m+1))
 records=[{'N':n,'D_A':str(da[n]),'B_A':str(ba[n]),'actual_q':str(abs(da[n])//gcd(da[n],ba[n]))} for n in (10,50,140)]
 p=83;chi=-1;depths=[]
 for k in range(1,4):
  mod=p**k;JC=cutoff(p,k,True);JD=cutoff(p,k,False)
  def cv(x):return sum(comb(x,j)*(CC[j]%mod) for j in range(1,min(x,JC-1)+1))%mod
  def dv(x):
   f,s=1,1
   for j in range(1,min(x,JD-1)+1):f=f*(x-j+1)%mod;s=(s+(-1)**j*f)%mod
   return s
  def weighted(x,fun):return sum((-1)**j*aa[j]*(falling(x,j)%mod)*fun(x-j) for j in range(m+1))%mod
  witnesses=[3,4,5,8,20,50,83,84,85,159,166,169,10**20+3,10**20+84]
  for x in witnesses:
   v=weighted(x,cv);den=weighted(x,dv)
   assert (weighted(x+p**k,cv)-v-p**(k-1)*chi*G[1]*den)%mod==0
   if x<=140:
    assert weighted(x,dv)==(-1)**x*da[x]%mod
    assert weighted(x,cv)==(-1)**x*(ba[x]-factorial(x)*A1)%mod
  depths.append({'p':p,'depth':k,'new_shift_checks':len(witnesses),'uniform_C_cutoff':JC})
 rows.append({'case':name,'ordinary_A_coefficients':aa,'A_one':A1,'original_jet_product_endpoint_checks_to':140,'actual_endpoint_records':records,'carry_depths':depths})
out={'status':'PASS_EXACT_NEW_FIXED_POLYNOMIAL_GAUGE_ENDPOINT_AND_CARRY','source_sha256':hashlib.sha256(raw).hexdigest(),'rows':rows,'scope':'New complete polynomial-weighted endpoint and three-depth carry checks; no favorable primitive gcd growth or main proof.'}
(S/'main/POLYNOMIAL_GAUGED_ENDPOINT_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
