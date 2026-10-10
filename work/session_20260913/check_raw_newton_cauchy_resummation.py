"""Symbolic adjacent ratios and one existing n4 moment control; no HP solve."""
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
n=s.symbols('n',integer=True,positive=True)
for even in (True,False):
    d=n-4 if even else n-3
    spectral=(n*n-(4 if even else 1))*(2*n-1)/2
    vd=(d+1)*(d+2)/(6 if even else 2)
    dr=(d+1)*(d+2)/((d+n)*(d+n+1))
    ratio=s.factor(-spectral*vd*dr/((d+1)*(d+2))**2)
    expected=-(n+(2 if even else 1))*(2*n-1)/((24 if even else 8)*(2*n-3))
    assert s.cancel(ratio-expected)==0

x=s.symbols('x')
Q=[s.Integer(1),x]
for k in range(1,7):Q.append(s.expand(x*Q[k]+s.Rational(k*k,4*k*k-1)*Q[k-1]))
F=[s.Poly(sum(s.expand(q).coeff(x,j)*x**j/s.factorial(j) for j in range(k+1)),x)
   for k,q in enumerate(Q)]
C=s.Matrix([[F[k].nth(d) for d in range(8)] for k in (5,6,7)])
I=[0,1,3];E=[2,4,5,6,7];r=3
C0=C[:,I]
H0=s.Matrix([[s.Rational(1,i+j+1) for j in range(r)] for i in I])
HE=s.Matrix([[s.Rational(1,i+j+1) for j in range(r)] for i in E])
R=C0.inv()*C[:,E];W=HE*H0.inv();K=R*W
for a,D in enumerate(E):
    for j,b in enumerate(I):
        w=s.rf(b+1,r)/s.rf(D+1,r)*s.prod(s.Rational(D-i,b-i) for i in I if i!=b)
        assert w==W[a,j]
Hall=s.Matrix([[s.Rational(1,d+j+1) for j in range(r)] for d in range(8)])
A=C*Hall
assert A==C0*(s.eye(r)+K)*H0
assert A.det()==C0.det()*H0.det()*(s.eye(r)+K).det()
assert R.rank()==W.rank()==r and K.rank()>=r-2
adj=R[0,E.index(2)]*W[E.index(2),0]
assert adj==-s.Rational(7,20)
one=s.zeros(r);one[0,0]=1
assert (s.eye(r)+one*K).det()==1+K[0,0]
Phi=(C0.inv()*s.Matrix([f.as_expr() for f in (F[5],F[6],F[7])]))[0]
assert s.expand(Phi-F[6].as_expr()/F[6].nth(0))==0
psi=sum(H0.inv()[j,0]*x**j for j in range(r))
assert s.integrate(Phi*psi,(x,0,1))==1+K[0,0]
out={'status':'passed','scope':'All-n symbolic ratios plus the already studied n4 moment matrix only',
     'new_HP_degrees_solved':0,'n4_adjacent_ratio':str(adj),
     'n4_resummed_one_column_family':str(1+K[0,0]),
     'n4_full_determinant_correction':str((s.eye(r)+K).det()),
     'n4_correction_rank':K.rank(),'explicit_cardinal_weights_verified':True,
     'coherent_factorization_verified':True,'scalar_integral_resummation_verified':True}
(HERE/'raw_newton_cauchy_resummation_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
