from math import comb,factorial,log,isqrt
from pathlib import Path
import json
from exact_local_probe import mm,mv,dot,transpose
from residue_atlas import coeffs,primes
BASE=Path(__file__).parent

def det(A,p):
 if len(A)==1:return A[0][0]%p
 return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]],p) for j in range(len(A)))%p
def adj(A,p):
 b=len(A)
 return [[(-1)**(i+j)*det([row[:i]+row[i+1:] for k,row in enumerate(A) if k!=j],p)%p for j in range(b)] for i in range(b)]
def plus_coeffs(n):
 c=[1]
 for k in range(2*n):
  t=2*(n-k)*c[-1]+2*(2*n-k+1)*(c[-2] if k else 0)
  assert t%(k+1)==0
  c.append(t//(k+1))
 return c

def state(n,p,b,m,bc,pc):
 aa=[a*pow(pow(2,-1,p),n,p)%p for a in bc]
 falls=[]
 for i in range(b):
  f=[1]
  for k in range(n+i):f.append(f[-1]*(n+i-k)%p)
  falls.append(f)
 N=[[sum(aa[s]*falls[i][j+s] for s in range(min(2*n,n+i-j)+1))%p for j in range(b)] for i in range(b)]
 Dc=[1]
 for k in range(1,2*n+b):Dc.append((k*Dc[-1]+1)%p)
 A=[sum(aa[s]*falls[i][s]*Dc[2*n+i-s] for s in range(min(2*n,n+i)+1))%p for i in range(b)]
 J=[sum(comb(i,k)*pc[n-k] for k in range(min(i,n)+1))%p for i in range(b)]
 U=[[0]*b for _ in range(b)]
 for i in range(b):
  U[i][i]=1
  for j in range(i+1,b):
   k=j-i
   U[i][j]=(-1)**k*(comb(n+k-1,k) if n else 0)*factorial(j)//factorial(i)
 Z=[[0]*b for _ in range(b+1)]
 for i in range(b):Z[i][i]=-1;Z[i+1][i]=1
 K=mm(Z,U)
 omega=[];f=1
 for j in range(b+1):
  if j:f*=n+m+2-j
  omega.append(f*f)
 H=mm(transpose(K),[[w*x for x in r] for w,r in zip(omega,K)])
 adjN=adj(N,p);detN=det(N,p)
 D0J=[factorial(n+i)//factorial(n)*J[i]%p for i in range(b)]
 Y=[v%p for v in mv(adjN,D0J)]
 W=[(x+detN*k)%p for x,k in zip(mv(H,mv(adjN,A)),K[0])]
 V=dot(Y,W)%p;D=dot(Y,mv(H,Y))%p
 return dict(n=n,N=N,A=A,J=J,Y=Y,W=W,V=V,D=D)
if __name__=='__main__':
 b,m=4,1;hi=199
 cache=[(coeffs(n),plus_coeffs(n)) for n in range(hi)]
 out=[];goods=[];rate=0
 for p in primes(hi):
  if p<=b:continue
  states=[state(n,p,b,m,*cache[n]) for n in range(p)]
  pz=[n for n,s in enumerate(states) if s['J'][0]==0];vz=[n for n,s in enumerate(states) if s['V']==0]
  C=sum((-1)**j*factorial(j) for j in range(p))%p
  origin=(576*(3*C-13))%p
  good=not pz and vz==[0] and 864%p!=0 and origin!=0
  out.append(dict(p=p,endpoint_zeros=pz,V_zeros=vz,C=C,origin_coefficient=origin,good=good,states=states))
  if good:goods.append(p);rate+=2*log(p)/(p-1);print(p,'good',rate)
 (BASE/'b4_finite_criterion.json').write_text(json.dumps(dict(b=b,m=m,prime_bound=hi,good_primes=goods,rate_display=rate,rows=out),indent=2))
 print('good primes',goods,'rate',rate)
