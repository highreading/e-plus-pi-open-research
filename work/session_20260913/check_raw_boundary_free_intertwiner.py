"""Selected exact controls for the new boundary-free moment intertwiner.

No canonical HP triple or increasing-degree diagnostic is constructed.
The closed moment-pair set is stated below before any computation.
"""
import sys,json
from pathlib import Path
from math import factorial,comb
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
x=s.symbols('x'); f=s.Function('f')(x)
def J(p): return x*s.diff(p,x,2)+s.diff(p,x)+x*p
def LL(p): return s.diff(x*x*s.diff(p,x,2),x,2)+s.diff(x*x*s.diff(p,x),x)
def TT(p): return s.diff(x*(x-1)*s.diff(p,x),x)+(x*x-x+1)*p
assert s.expand(J(J(f))-J(f)-LL(f)-TT(f))==0
def beta(k): return s.Rational(k*k,4*k*k-1) if k else s.S.Zero
def moment(k,l):
    if k<0 or l<0: return s.S.Zero
    return s.Rational(factorial(k),factorial(2*k))*sum(
        s.Rational(comb(k,(k+d)//2)*factorial(k+d),factorial(d-l)*factorial(d+l+1))
        for d in range(l,k+1) if d%2==k%2)
def row_terms(k):
    return {k+2:(k+1)*(k+2), k+1:-(k+1),
        k:(k+1)**2*beta(k+1)+k*k*beta(k)-k*(k+1),
        k-1:-k*beta(k),k-2:k*(k-1)*beta(k)*beta(k-1) if k>=2 else 0}
def xp(l): return s.Rational(l+1,2*(2*l+1))
def xm(l): return s.Rational(l,2*(2*l+1)) if l>=0 else s.S.Zero
def col_terms(l):
    return {l+2:xp(l)*xp(l+1),
        l:l*(l+1)+s.Rational(3,4)+xp(l)*xm(l+1)+(xm(l)*xp(l-1) if l else 0),
        l-2:xm(l)*xm(l-1) if l>=2 else 0}
pairs=((0,0),(1,2),(4,3),(5,4),(7,5))
checks=[]
for k,l in pairs:
    left=sum(c*moment(j,l) for j,c in row_terms(k).items() if c)
    right=sum(c*moment(k,j) for j,c in col_terms(l).items() if c)
    assert left==right
    checks.append({'k':k,'l':l,'common_exact_value':str(left),'pass':True})
u=s.symbols('u')
assert s.expand((1+s.Rational(2,3)*u)**2*(1-u)-1-u*(s.Rational(1,3)-s.Rational(8,9)*u-s.Rational(4,9)*u*u))==0
constant=s.Rational(3,4)+s.Rational(1,6)+s.Rational(5,2)/24+s.Rational(25,12)/24+s.Rational(17,18)/144
assert constant==s.Rational(361,324)<s.Rational(9,8)
out={'scope':'Only the five predeclared moment pairs, a formal differential-operator identity, and exact arithmetic in the uniform row-sum proof; no canonical degree solve.',
     'formal_operator_identity':True,'moment_pairs':checks,
     'row_sum_bound_for_k_ge_2':str(constant),'status':'pass'}
(HERE/'raw_boundary_free_intertwiner_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
