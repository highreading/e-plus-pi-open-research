"""Small exact controls for identities proved in raw_borel_legendre_literature.md."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'math_packages'))
import sympy as s

x,z=s.symbols('x z')
N=8
Q={k:s.expand(s.factorial(k)/s.factorial(2*k)*s.diff((1+x*x)**k,x,k)) for k in range(N+1)}
F={k:s.Add(*[Q[k].coeff(x,d)*x**d/s.factorial(d) for d in range(k+1)]) for k in Q}
def L(f):
    return s.diff(x*x*s.diff(f,x,2),x,2)+s.diff(x*x*s.diff(f,x),x)
def boundary(f,g):
    return (f*s.diff(x*x*s.diff(g,x,2),x)-s.diff(f,x)*x*x*s.diff(g,x,2)
            -g*s.diff(x*x*s.diff(f,x,2),x)+s.diff(g,x)*x*x*s.diff(f,x,2)
            +x*x*(f*s.diff(g,x)-s.diff(f,x)*g))
for k in Q:
    assert s.expand(L(F[k])-k*(k+1)*F[k])==0
    m=k//2
    h=s.Rational(1,2) if k%2==0 else s.Rational(3,2)
    series=sum(s.rf(-m,j)*s.rf(m+h,j)/
               (s.rf(h,j)**2*s.rf(1,j)*s.factorial(j))*(-x*x/4)**j
               for j in range(m+1))
    expected=Q[k].coeff(x,k%2)*x**(k%2)*series
    assert s.expand(expected-F[k])==0
for k in Q:
    for l in Q:
        b=boundary(F[k],F[l])
        assert s.expand(s.diff(b,x)-F[k]*L(F[l])+F[l]*L(F[k]))==0
        assert b.subs(x,0)==0
u=x*z/(1-z*z)
# Truncate elementary series before expansion; all operations are exact.
prod=(1-z*z)**s.Rational(-1,2)
exp_u=sum(u**j/s.factorial(j) for j in range(N+1))
i0_u=sum((u*u/4)**j/s.factorial(j)**2 for j in range(N//2+1))
rhs=s.series(prod*exp_u*i0_u,z,0,N+1).removeO().expand()
for k in Q:
    assert s.expand(rhs.coeff(z,k)-s.binomial(2*k,k)/2**k*F[k])==0
out={'degree_range':[0,N], 'hypergeometric_and_operator_checks':True,
     'green_identity_pairs':(N+1)**2,'generating_function_checks':True,
     'first_monic_polynomials':{k:str(s.factorial(k)*F[k]) for k in range(5)},
     'scope':'Exact finite controls; the all-degree statements are proved in the accompanying note.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
