"""New finite-depth construction in a radius-preserving endpoint-fixed family.
Uses rational definition coefficients modulo p^L, not a prior carry receipt.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb
import json, hashlib
S=Path('work/session_20261002_codex_continuation')
raw=(S/'main/EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json').read_bytes()
ks=json.loads(raw)['endpoint_basis_integers']
p,r=163,159
P0=[Q(0)]*(r+2);P0[1]=Q(1)
for j,v in enumerate(ks,1):
 P0[j]+=Q(v,factorial(j));P0[j+1]-=Q(v,factorial(j))

def vp(a):
 if a==0:return 10**6
 k=0
 while a%p==0:a//=p;k+=1
 return k
def fl(j):
 k=0
 while j>=p:j//=p;k+=1
 return k
def cutoff(k):
 j=0;s=0
 while True:
  j+=1;s+=vp(j)
  if s-fl(j)>=k:return j
def dv(x,k,derivative=False):
 m=p**k;f,df,total,dtotal=1,0,1,0
 for j in range(1,p*(k+2)):
  df,f=(df*(x-j+1)+f)%m,f*(x-j+1)%m
  total=(total+(-1)**j*f)%m
  dtotal=(dtotal+(-1)**j*df)%m
 return dtotal if derivative else total

def cv(x,K,k):
 J=cutoff(k)
 # T_j involves division by j. Keep floor(log_p J) extra digits.
 L=k+fl(J);m=p**L
 pp=[a.numerator*pow(a.denominator,-1,m)%m for a in P0]
 invfac=pow(factorial(r),-1,m)
 pp[r]=(pp[r]+K*invfac)%m;pp[r+1]=(pp[r+1]-K*invfac)%m
 d=len(pp)-1
 qq=[2]+[(sum(pp[a]*pp[j-a] for a in range(max(0,j-d),min(d,j)+1))-(2*pp[j] if j<=d else 0))%m for j in range(1,min(2*d,J-1)+1)]
 aa=[];inv2=pow(2,-1,m)
 for n in range(J-1):
  aa.append(((4*(n+1)*pp[n+1] if n+1<=d else 0)-sum(qq[a]*aa[n-a] for a in range(1,min(len(qq)-1,n)+1)))*inv2%m)
 mod=p**k;f=1;num=0
 # Accumulate T_j at the uniform fixed denominator p^fl(J).
 ell=fl(J);den=p**ell;T=0
 for j in range(1,J):
  v=vp(j);unit=j//p**v
  T=(T+aa[j-1]*p**(ell-v)*pow(unit,-1,m))%m
  f=f*(x-j+1)%m
  term=(-1)**j*T*f%m
  assert term%den==0
  num=(num+term//den)%mod
 return num

assert dv(r,1)==0 and dv(r,1,True)==62
x=r;K=-31;rows=[]
maxsafe=0
while (p**(maxsafe+1)//2)*3*2**r*401**81<factorial(r):maxsafe+=1
for k in range(1,maxsafe+1):
 m=p**k
 if k>1:
  step=p**(k-1)
  f=dv(x,k)
  assert f%step==0
  x=(x+step*((-(f//step)*pow(62,-1,p))%p))%m
  value=cv(x,K,k)
  assert value%step==0
  # C*_K is -2 mod p because r is odd.
  K=(K+step*((-(value//step)*pow(-2,-1,p))%p))%m
  if K>m//2:K-=m
 assert dv(x,k)==cv(x,K,k)==0
 assert abs(K)*3*2**r*401**81<factorial(r)
 # Pick an actual large nonnegative index with factorial vanished at depth k.
 J=cutoff(k);N=x
 if N<J:N+=((J-N+m-1)//m)*m
 assert dv(N,k)==cv(N,K,k)==0 and vp(factorial(J))>=k
 rows.append({'depth':k,'modulus':m,'index_residue_x':str(x),'centered_integer_K':str(K),'actual_large_index':str(N),'uniform_cutoff':J,'Dstar_modulus_residue':0,'Cstar_modulus_residue':0,'strict_radius_lower':2})
 print('depth',k,'K',K,'x',x,flush=True)
out={'status':'PASS_EXACT_NEW_PARAMETER_HENSEL_FINITE_RADIUS_DEPTHS','prime':p,'cell_r':r,'Dstar_derivative_mod_p':62,'Cstar_parameter_derivative_mod_p':161,'source_sha256':hashlib.sha256(raw).hexdigest(),'uniform_safe_depth_count':maxsafe,'rows':rows,'scope':'Finite distinct rational pullbacks; the p-adic parameter limit need not be rational or archimedean-bounded. No one fixed rational P with unbounded depth, no global q-error bound.'}
# An independent original binomial endpoint convolution at the largest depth.
# This uses only integral derivative jets and the exponential product rule.
row=rows[-1];k=row['depth'];mod=p**k;N=int(row['actual_large_index']);K=int(row['centered_integer_K'])
P=P0[:];P[r]+=Q(K,factorial(r));P[r+1]-=Q(K,factorial(r))
pj=[int(v*factorial(j))%mod for j,v in enumerate(P)];d=len(pj)-1
qq=[2]+[(sum(comb(j,a)*pj[a]*pj[j-a] for a in range(max(0,j-d),min(d,j)+1))-(2*pj[j] if j<=d else 0))%mod for j in range(1,2*d+1)]
M=p*(k+1);G=[0];pascal=[1]+[0]*M
for n in range(1,M+1):
 val=(4*pj[n] if n<=d else 0)-sum(pascal[a]*qq[a]*G[n-a] for a in range(1,min(2*d,n-1)+1))
 G.append(val*pow(2,-1,mod)%mod)
 for a in range(n,0,-1):pascal[a]=(pascal[a]+pascal[a-1])%mod
assert all(G[j]==0 for j in range(p*(k+1),len(G)))
original=sum((-1)**j*(comb(N,j)%mod)*G[j]*dv(N-j,k) for j in range(1,M+1))%mod
assert original==0
out['independent_original_endpoint_convolution']={'depth':k,'N':str(N),'G_max_order':M,'residue':original}
(S/'main/PRIME_PARAMETER_HENSEL_RADIUS_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
