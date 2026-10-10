from exact_local_probe import adj,det,mm,mv,dot,transpose
from math import factorial,log
import sys
from pathlib import Path
import json

def primes(m):
 return [p for p in range(3,m+1) if all(p%d for d in range(2,int(p**.5)+1))]
def coeffs(n):
 b=[2**n]
 for s in range(2*n):
  num=2*(s-n)*b[-1]+(2*n-s+1)*(b[-2] if s else 0)
  assert num%(2*(s+1))==0
  b.append(num//(2*(s+1)))
 return b

def pm(A,p):return [[x%p for x in row] for row in A]
def state(r,p,P,b=None):
 inv2=pow(2,-1,p);b=coeffs(r) if b is None else b;a=[x*pow(inv2,r,p)%p for x in b]
 falls=[]
 for i in range(3):
  f=[1]
  for k in range(r+i):f.append(f[-1]*(r+i-k)%p)
  falls.append(f)
 Dc=[1]
 for k in range(1,2*r+3):Dc.append((k*Dc[-1]+1)%p)
 N=[[sum(a[s]*falls[i][j+s] for s in range(min(2*r,r+i-j)+1))%p for j in range(3)] for i in range(3)]
 A=[sum(a[s]*falls[i][s]*Dc[2*r+i-s] for s in range(min(2*r,r+i)+1))%p for i in range(3)]
 K=[[-1,r,-r*(r+1)],[1,-r-1,r*(r+3)],[0,1,-2*r-1],[0,0,1]]
 om=[1,(r+2)**2,((r+2)*(r+1))**2,((r+2)*(r+1)*r)**2]
 H=pm(mm(transpose(K),[[w*x for x in row] for w,row in zip(om,K)]),p)
 J=[P[r]%p,(P[r]*inv2+P[r+1]*inv2**2)%p,(P[r+2]*inv2**3)%p]
 d0J=[J[0],(r+1)*J[1],(r+1)*(r+2)*J[2]]
 Y=[x%p for x in mv(adj(N),d0J)]
 W=[(x+det(N)*y)%p for x,y in zip(mv(H,mv(adj(N),A)),K[0])]
 V=dot(Y,W)%p;D=dot(Y,mv(H,Y))%p
 return dict(r=r,N=N,A=A,J=J,Y=Y,W=W,V=V,D=D)
if __name__=='__main__':
 lo=int(sys.argv[1]) if len(sys.argv)>1 else 3
 hi=int(sys.argv[2]) if len(sys.argv)>2 else 199
 P=[1,2]
 for k in range(1,hi+4):P.append((2*(2*k+1)*P[-1]+4*k*P[-2])//(k+1))
 out=[];selected=[];rate=0
 cache=[coeffs(r) for r in range(hi)]
 for p in primes(hi):
  if p<lo:continue
  states=[state(r,p,P,cache[r]) for r in range(p)]
  zerosP=[r for r in range(p) if P[r]%p==0]
  zerosV=[d['r'] for d in states if d['V']==0]
  C=sum((-1)**j*factorial(j) for j in range(p))%p
  good=not zerosP and zerosV==[0] and (3*C+4)%p!=0
  row=dict(p=p,endpoint_zeros=zerosP,V_zeros=zerosV,C=C,origin_coefficient=(16*(3*C+4))%p,good=good,states=states)
  out.append(row)
  if good:
   selected.append(p);rate+=2*log(p)/(p-1);print(p,'good',rate)
 Path(__file__).with_name('residue_atlas_'+str(lo)+'_'+str(hi)+'.json').write_text(json.dumps(out,indent=2))
 print('selected',selected,'rate',rate,'threshold',2*log(1+2**.5))
