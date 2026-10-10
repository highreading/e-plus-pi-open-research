import sympy as s
from math import factorial
from pathlib import Path
import json
X,T,C=s.symbols('X T C')

def falling(x,j):
 a=s.Integer(1)
 for k in range(j):a*=x-k
 return s.expand(a)
def general(b,m):
 q=1-T+T*T/2
 logs=[s.expand(s.log(q).series(T,0,b).removeO()).coeff(T,k) for k in range(b)]
 N0=s.Matrix(b,b,lambda i,j:falling(i,j))
 N1=s.zeros(b)
 for i in range(b):
  for j in range(b):
   f=falling(X+i,j)
   N1[i,j]=s.diff(f,X).subs(X,0)+sum(logs[k]*falling(i,j+k) for k in range(1,b))
 Dc=[s.Integer(1)]
 for i in range(1,b):Dc.append(i*Dc[-1]+1)
 deriv=[2*C]
 for i in range(1,b):deriv.append(i*deriv[-1]+2*Dc[i-1])
 A1=s.Matrix([deriv[i]+sum(logs[k]*falling(i,k)*Dc[i-k] for k in range(1,i+1)) for i in range(b)])
 A0=s.Matrix(Dc)
 Dpol=s.zeros(b)
 for i in range(b-1):Dpol[i,i+1]=i+1
 L=s.zeros(b)
 for k in range(1,b):L+=s.Rational((-1)**(k+1),k)*Dpol**k
 Z=s.zeros(b+1,b)
 for i in range(b):Z[i,i]=-1;Z[i+1,i]=1
 Om=s.diag(*[falling(m+1,j)**2 for j in range(b+1)])
 H0=Z.T*Om*Z
 t0=N0.det();u0=N0.inv()*s.Matrix([factorial(i) for i in range(b)]);Y0=t0*u0
 ones=s.ones(b,1)
 assert N0*ones==A0
 assert H0*ones==s.Matrix([1]+[0]*(b-1))
 W1=t0*H0*(N0.inv()*(A1-N1*ones)-L*ones)
 V1=s.factor((Y0.T*W1)[0]);D0=s.factor((Y0.T*H0*Y0)[0])
 assert s.expand(V1).coeff(C)==2*D0
 return dict(b=b,m=m,det_N0=str(t0),D_origin=str(D0),V_over_n=str(V1),beta_coefficient=str(V1.subs(C,0)),ratio_beta_to_D=str(s.cancel(V1.subs(C,0)/D0)),Y_origin=[str(a) for a in Y0],W_derivative=[str(a) for a in W1])
if __name__=='__main__':
 rows=[general(b,m) for b in range(3,11) for m in range(1,(b-1)//2+1)]
 Path(__file__).with_name('general_origin_coefficient.json').write_text(json.dumps(rows,indent=2))
 for a in rows:print(a['b'],a['m'],'D0=',a['D_origin'],'V/n=',a['V_over_n'],'beta/D=',a['ratio_beta_to_D'])
