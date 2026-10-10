"""New two-prime radius-budget CRT specialization, definition-level computations."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,hashlib
S=Path('work/session_20261002_codex_continuation')
raw=(S/'main/EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json').read_bytes()
ks=json.loads(raw)['endpoint_basis_integers'];P0=[Q(0)]*161;P0[1]=Q(1)
for j,v in enumerate(ks,1):P0[j]+=Q(v,factorial(j));P0[j+1]-=Q(v,factorial(j))
def vp(n,p):
 if n==0:return 10**6
 k=0
 while n%p==0:n//=p;k+=1
 return k
def fl(j,p):
 k=0
 while j>=p:j//=p;k+=1
 return k
def cutoff(p,k):
 j=0;s=0
 while True:
  j+=1;s+=vp(j,p)
  if s-fl(j,p)>=k:return j
def D(x,p,k,derivative=False):
 mod=p**k;f,df,total,dtotal=1,0,1,0
 for j in range(1,p*(k+2)):
  df,f=(df*(x-j+1)+f)%mod,f*(x-j+1)%mod
  total=(total+(-1)**j*f)%mod;dtotal=(dtotal+(-1)**j*df)%mod
 return dtotal if derivative else total
def C(x,poly,p,k):
 J=cutoff(p,k);ell=fl(J,p);mod=p**(k+ell);den=p**ell
 pp=[v.numerator*pow(v.denominator,-1,mod)%mod for v in poly];d=len(pp)-1
 qq=[2]+[(sum(pp[a]*pp[j-a] for a in range(max(0,j-d),min(d,j)+1))-(2*pp[j] if j<=d else 0))%mod for j in range(1,min(2*d,J-1)+1)]
 aa=[];inv2=pow(2,-1,mod)
 for n in range(J-1):
  aa.append(((4*(n+1)*pp[n+1] if n+1<=d else 0)-sum(qq[a]*aa[n-a] for a in range(1,min(len(qq)-1,n)+1)))*inv2%mod)
 T=0;f=1;total=0
 for j in range(1,J):
  v=vp(j,p);unit=j//p**v
  T=(T+aa[j-1]*p**(ell-v)*pow(unit,-1,mod))%mod
  f=f*(x-j+1)%mod;term=(-1)**j*T*f%mod
  assert term%den==0
  total=(total+term//den)%p**k
 return total
def family(r,K):
 pp=P0[:];pp[r]+=Q(K,factorial(r));pp[r+1]-=Q(K,factorial(r));return pp
def crt(a,m,b,n):return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n)
locals={}
for p,r in [(163,159),(347,157)]:
 der=D(r,p,1,True);assert D(r,p,1)==0 and der!=0
 x=r;K=0;vals=[]
 for k in range(1,5):
  step=p**(k-1);mod=p**k
  if k>1:x=(x+step*((-(D(x,p,k)//step)*pow(der,-1,p))%p))%mod
  value=C(x,family(r,K),p,k);assert value%step==0
  K=(K+step*((-(value//step)*pow(-2,-1,p))%p))%mod
  assert D(x,p,k)==C(x,family(r,K),p,k)==0
  vals.append({'k':k,'index':x,'parameter':K,'derivative':der})
 locals[p]=vals
rows=[]
for k in range(1,5):
 a,b=163**k,347**k;mod=a*b
 K157=crt(0,a,locals[347][k-1]['parameter'],b)
 K159=crt(locals[163][k-1]['parameter'],a,0,b)
 if K157>mod//2:K157-=mod
 if K159>mod//2:K159-=mod
 pp=family(157,K157);pp[159]+=Q(K159,factorial(159));pp[160]-=Q(K159,factorial(159))
 assert pp[0]==0 and sum(pp)==1 and pp[1]==1
 left=3*(mod//2)*(2**157*159*158+2**159)*401**81
 assert left<factorial(159)
 N=crt(locals[163][k-1]['index'],a,locals[347][k-1]['index'],b)
 J=max(cutoff(163,k),cutoff(347,k))
 if N<J:N+=((J-N+mod-1)//mod)*mod
 for p in (163,347):assert D(N,p,k)==C(N,pp,p,k)==0
 rows.append({'depth_at_each_prime':k,'guaranteed_actual_gcd_divisor':str(mod),'centered_K157':str(K157),'centered_K159':str(K159),'joint_actual_index_N':str(N),'factorial_cutoff':J,'strict_radius_lower':2,'uniform_integer_bound_left':str(left),'uniform_integer_bound_right':str(factorial(159))})
 print('both primes depth',k,'N',N,'K157',K157,'K159',K159,flush=True)
out={'status':'PASS_EXACT_NEW_TWO_PRIME_COMMON_CONTENT_WITH_RADIUS_BUDGET','source_sha256':hashlib.sha256(raw).hexdigest(),'polynomial':'P81+K157*z^157*(1-z)/157!+K159*z^159*(1-z)/159!','degree':160,'good_primes':[163,347],'local_cells':locals,'rows':rows,'scope':'Four distinct rational polynomials and actual large-index cells with joint prime-power content, certified radius>2. No infinite-prime supply, fixed-polynomial arbitrary-depth content, or global q-error bound.'}
(S/'main/MULTILOCAL_RADIUS_BUDGET_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
