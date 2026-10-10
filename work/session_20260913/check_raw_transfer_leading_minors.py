"""Symbolic leading minors and checks against frozen n=1,2 transfer rows.

No new degree is sampled or constructed.
"""
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s

x,n=s.symbols('x n')
a,a1,a2,b,b1,b2,c,c1,c2,d,d1,e,e1,f,f1=s.symbols(
    'a a1 a2 b b1 b2 c c1 c2 d d1 e e1 f f1')
H=a+(a1-c)*x+(a2-c1)*x*x
B=b+b1*x+b2*x*x
C=c+c1*x+c2*x*x
Hp=d+(d1-f)*x
Bp=e+e1*x
Cp=f+f1*x
def fall_on(g,degree,r):
    for j in range(r):
        g=s.expand((degree-j)*g-x*s.diff(g,x))
    return g
rows=[]
for r in range(3):
    rows.append([x**r*fall_on(H,n,r),
        sum(s.binomial(r,j)*x**j*fall_on(B,n,j) for j in range(r+1)),
        x**r*fall_on(C,n,r)])
W=s.Poly(s.expand(s.det(s.Matrix(rows))),x)
Xi=a*c1-a1*c+c*c
D0=a*f-c*d
D1=a*f1+a1*f-c*d1-c1*d
assert W.nth(0)==W.nth(1)==0
assert s.expand(W.nth(2)-b*Xi)==0
mix=s.Poly(s.expand(s.det(s.Matrix([rows[0],rows[1],[Hp,Bp,Cp]]))),x)
assert s.expand(mix.nth(0)-b*D0)==0
assert s.expand(mix.nth(1)-(b*D1+b1*D0))==0

z=s.symbols('z');D=1+z*z
def kmat(A,B,C):
    return s.Matrix([[D*D*A,B,C],
      [D*D*s.diff(A,z)+D*C,B+s.diff(B,z),s.diff(C,z)],
      [D*D*s.diff(A,z,2)+2*D*s.diff(C,z)-s.diff(D,z)*C,
       B+2*s.diff(B,z)+s.diff(B,z,2),s.diff(C,z,2)]])

saved=json.loads((HERE/'raw_rational_transfer_checks.json').read_text())
old=(7-s.Rational(19,2)*z,-7+8*z,s.Rational(17,2)-s.Rational(9,2)*z)
controls=[]
for case in saved['steps']:
    k=case['from_n']
    nxt=tuple(s.sympify(t) for t in case['next_triple'])
    AA,BB,CC=map(lambda p:s.Poly(p,z),old)
    AP,BP,CP=map(lambda p:s.Poly(p,z),nxt)
    aa,ac,bb=AA.nth(k),CC.nth(k),BB.nth(k)
    xi=aa*CC.nth(k-1)-AA.nth(k-1)*ac+ac*ac
    d0=aa*CP.nth(k+1)-ac*AP.nth(k+1)
    d1=aa*CP.nth(k)+AA.nth(k-1)*CP.nth(k+1)-ac*AP.nth(k)-CC.nth(k-1)*AP.nth(k+1)
    q=s.Poly(s.sympify(case['Q']),z)
    assert q.nth(3)==bb*xi
    K=kmat(*old);Kmix=K.copy();Kmix[2,:]=kmat(*nxt)[0,:]
    numer=s.Poly(s.cancel(Kmix.det()/z**(3*k-1)),z)
    assert numer.nth(6)==bb*d0
    assert numer.nth(5)==bb*d1+BB.nth(k-1)*d0
    controls.append({'n':k,'frozen_polynomials_only':True,
       'Q3':str(q.nth(3)),'Xi':str(xi),
       'gamma_N26_over_Q3':str(s.factor(d0/xi)),
       'delta_N25_over_Q3':str(s.factor((d1+BB.nth(k-1)/bb*d0)/xi))})
    old=nxt
out={'status':'passed','new_degree_samples':0,
     'symbolic_Q3':str(s.factor(W.nth(2))),
     'symbolic_N26':str(s.factor(mix.nth(0))),
     'symbolic_N25':str(s.factor(mix.nth(1))),
     'frozen_controls':controls}
(HERE/'raw_transfer_leading_minors_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
