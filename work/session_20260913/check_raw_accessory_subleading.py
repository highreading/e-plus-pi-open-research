"""Symbolic coefficient identities, without new Hermite--Pade degree samples."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'math_packages'))
import sympy as s

x,n,alpha,beta,gamma,h2,b2,v2,q2,q1,q0,u4,u3,u2,u1,u0,v3,v_2,v1,v0=s.symbols(
    'x n alpha beta gamma h2 b2 v2 q2 q1 q0 u4 u3 u2 u1 u0 v3 v_2 v1 v0')

def fall_on(f, degree, order):
    for j in range(order):
        f=s.expand((degree-j)*f-x*s.diff(f,x))
    return f

H=1+alpha*x+h2*x*x
B=1+beta*x+b2*x*x
V=1+gamma*x+v2*x*x
rows=[]
for r in range(3):
    rows.append([x**r*fall_on(H,n,r),
        sum(s.binomial(r,j)*x**j*fall_on(B,n,j) for j in range(r+1)),
        x**r*fall_on(V,n-1,r)])
wr=s.Poly(s.expand(s.det(s.Matrix(rows))),x)
assert wr.nth(1)==1
assert s.expand(wr.nth(2)-(beta+2*gamma+2))==0

# Reverse each A_j with enough explicit symbolic coefficients to retain the
# first equations. A_j(z)=z^(6-jbound) times the displayed reversed polynomial.
z=s.symbols('z')
D=1+z*z
Q=z**3+q2*z*z+q1*z+q0
A3=z*D*Q
A2=-(((z+3*n-1)*D-2*z*s.diff(D,z))*Q+z*D*s.diff(Q,z))
A1=(2*n-2)*z**5+u4*z**4+u3*z**3+u2*z*z+u1*z+u0
A0=-n*(n-1)*z**4+v3*z**3+v_2*z*z+v1*z+v0
Aj=(A0,A1,A2,A3)
alg=s.expand(sum(Aj[j].subs(z,1/x)*x**j*fall_on(H,n,j) for j in range(4)))
exp=s.expand(sum(Aj[j].subs(z,1/x)*
    sum(s.binomial(j,k)*x**k*fall_on(B,n,k) for k in range(j+1)) for j in range(4)))
e1=s.expand(exp).coeff(x,-4)
a1=s.expand(alg).coeff(x,-3)
assert s.expand(e1-(-beta-3*n*n-2*n*q2+n+3*q2+u4))==0
assert s.expand(a1-(-2*n**3-n*n*q2+2*n*n+n*q2+n*u4+v3))==0
u_expected=beta+3*n*n-n+(2*n-3)*q2
v_expected=-n*beta-n**3-n*n-n*(n-2)*q2
assert s.expand(a1.subs({u4:u_expected,v3:v_expected}))==0

p,t=s.symbols('p t')
curve=t*t*p**3-t*(t+3)*p*p+(2*t+2)*p-1
factor=(t*p-1)*(t*p*p-(t+2)*p+1)
assert s.expand(curve-factor)==0

out={'status':'passed','new_numeric_degree_samples':0,
     'Wr_first_coefficient':str(wr.nth(1)),
     'Wr_second_coefficient':str(s.factor(wr.nth(2))),
     'exponential_next_equation':str(s.factor(e1)),
     'high_Laurent_resonance_equation':str(s.factor(a1)),
     'conditional_curve_factorization':str(s.factor(curve))}
(HERE/'raw_accessory_subleading_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
