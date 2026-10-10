"""Exact ladder/Green/jet identities; no fitting and no degree scan of HP solutions."""
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
x=s.symbols('x')
Q=[s.Integer(1),x]
for k in range(1,10):
    Q.append(s.expand(x*Q[-1]+s.Rational(k*k,4*k*k-1)*Q[-2]))
F=[sum(a*x**j/s.factorial(j) for (j,),a in s.Poly(q,x).terms()) for q in Q]
def J(f): return x*s.diff(f,x,2)+s.diff(f,x)+x*f
out={'scope':'Exact symbolic identity controls, no recurrence fitting','ladder':[],'moment_transfer':[],'green':[]}
assert J(F[0])==F[1]
for k in (1,2,4,7,9):
    rhs=(k+1)*F[k+1]+k*s.Rational(k*k,4*k*k-1)*F[k-1]
    assert s.expand(J(F[k])-rhs)==0
    out['ladder'].append(k)
for P,k in [(1+2*x-x*x,3),((1-x)**7+3*x,5)]:
    mu=lambda f:s.integrate(P*f,(x,0,1))
    rhs=(k+1)*mu(F[k+1])+k*s.Rational(k*k,4*k*k-1)*mu(F[k-1])
    rhs-=P.subs(x,1)*s.diff(F[k],x).subs(x,1)-s.diff(P,x).subs(x,1)*F[k].subs(x,1)
    lhs=s.integrate(J(P)*F[k],(x,0,1))
    assert s.simplify(lhs-rhs)==0
    for r in range(5):
        jet=lambda j:s.diff(P,x,j).subs(x,1) if j>=0 else 0
        assert s.expand(s.diff(J(P),x,r).subs(x,1)
                         -jet(r+2)-(r+1)*jet(r+1)-jet(r)-r*jet(r-1))==0
    out['moment_transfer'].append({'polynomial':str(P),'k':k,'common_value':str(lhs)})
Omega=s.Matrix([[0,1,2,1],[-1,0,-1,0],[-2,1,0,0],[-1,0,0,0]])
assert Omega.det()==1
for j,k in [(0,3),(2,5),(3,8)]:
    vec=lambda f:s.Matrix([s.diff(f,x,r).subs(x,1) for r in range(4)])
    lhs=(k*(k+1)-j*(j+1))*s.integrate(F[j]*F[k],(x,0,1))
    rhs=(vec(F[j]).T*Omega*vec(F[k]))[0]
    assert s.simplify(lhs-rhs)==0
    out['green'].append([j,k])
out['status']='passed'
(HERE/'raw_balanced_ladder_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact second-order ladder, moment transfer, endpoint jets, and four-jet Green controls passed.')
