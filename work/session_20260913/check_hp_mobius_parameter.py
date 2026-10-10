"""Bounded symbolic checks for the Möbius parameter; no parameter scan."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "math_packages"))
import sympy as S

b, t, s, z = S.symbols("b t s z", real=True)
a = 1+b
n = 2
def monic(k, x, bb=b):
    aa=1+bb
    return S.expand((2*S.I/aa)**k*S.legendre(k,-S.I*(aa*x-bb))/S.binomial(2*k,k))
def norm(k, bb=b):
    aa=1+bb
    return 4*(-4)**k/(aa**(2*k+1)*(2*k+1)*S.binomial(2*k,k)**2)
def kernel(nn, x, y, bb=b):
    return S.cancel(sum(monic(k,x,bb)*monic(k,y,bb)/norm(k,bb) for k in range(nn+1)))
def ell(poly, j, variable=s):
    pp=S.Poly(S.expand(poly),variable)
    return S.cancel(sum(c/S.factorial(n+k+1-j) for (k,),c in pp.terms()))
def trunc(expr, nn=n):
    return S.series(expr,z,0,nn+1).removeO().expand()

K=kernel(n,t,s)
affine=lambda x:(a*x-b+1)/2
assert S.cancel(K-a*kernel(n,affine(t),affine(s),S.Integer(1))/2)==0
for k in range(n+1):
    assert S.cancel(monic(k,t)-(2/a)**k*monic(k,affine(t),S.Integer(1)))==0
    assert S.cancel(norm(k)-(2/a)**(2*k+1)*norm(k,S.Integer(1)))==0
for k in (1,2):
    mu_previous=-monic(k,0)/monic(k-1,0)
    lhs=S.diff(monic(k,t),t).subs(t,0)/(k*monic(k,0))
    rhs=-a/(1+b*b)*(b+k/(a*(2*k-1)*mu_previous))
    assert S.cancel(lhs-rhs)==0

# Moments obtained directly by integrating monomials on the vertical segment.
u=S.symbols('u',real=True)
moments=[S.cancel(2/a*S.integrate(((b+S.I*u)/a)**k,(u,-1,1))) for k in range(2*n+1)]
F=sum(moments[k]*z**(k+1) for k in range(2*n+1))
derivative=4*a/((a-b*z)**2+z*z)
assert S.cancel(trunc(S.diff(F,z)-derivative,2*n))==0

tj=[ell(K.subs(t,1),j) for j in (0,1)]
Cstar=[-ell(K,j) for j in (0,1)]
C=[S.cancel(z**n*cs.subs(t,1/z)) for cs in Cstar]
aj=[S.cancel(-trunc(z**j*sum(z**k/S.factorial(k) for k in range(n+1))+C[j]*F).subs(z,1)) for j in (0,1)]
B0=1+tj[1]; B1=-1-tj[0]
YY=S.cancel(B0+B1)
XX=S.cancel(B0*aj[0]+B1*aj[1])
xx=S.factor(XX/YY)
claimed=-(13*b**5+b**4+2562*b**3-382*b**2-191*b+3277)/(32*(b+1)*(14*b*b-17*b+17))
assert S.cancel(xx-claimed)==0
assert S.cancel(YY-(b+1)*(14*b*b-17*b+17)/32)==0
H=4**(n+1)*S.factorial(2*n+1)
L=S.ilcm(*range(1,n+1))
assert S.Poly(XX,b).degree()<=2*n+1
assert S.Poly(YY,b).degree()<=n+1
for elem in tj:
    assert all(S.denom(c)==1 for c in S.Poly(S.cancel(H*elem),b).all_coeffs())
for elem in aj:
    assert S.Poly(elem,b).degree()<=n+1
    assert all(S.denom(c)==1 for c in S.Poly(S.cancel(H*L*elem),b).all_coeffs())
CC=S.cancel(B0*C[0]+B1*C[1])
AA=-trunc((B0+B1*z)*sum(z**k/S.factorial(k) for k in range(n+1))+CC*F)
RR=AA+(B0+B1*z)*sum(z**k/S.factorial(k) for k in range(2*n+2))+CC*F
assert S.cancel(trunc(RR,2*n+1))==0
assert S.cancel(CC.subs(z,1)-YY)==0
assert S.cancel(AA.subs(z,1)-XX)==0

# Canonical diagonal pi Pade endpoint invariance, as a rational-function identity.
Db=S.cancel(z**n*monic(n,1/z))
Nb=trunc(Db*F)
D0=S.cancel(Db.subs(b,0)); N0=S.cancel(Nb.subs(b,0))
w=z/(a-b*z)
assert S.cancel(Db-(a-b*z)**n/a**n*D0.subs(z,w))==0
assert S.cancel(Nb-(a-b*z)**n/a**n*N0.subs(z,w))==0
assert S.cancel(Nb.subs(z,1)/Db.subs(z,1)-N0.subs(z,1)/D0.subs(z,1))==0

checks={"status":"all exact symbolic checks passed", "degree":n,
 "kernel_affine_conjugacy":True,"moment_derivative":True,
 "Legendre_logarithmic_derivative_identity":True,
 "endpoint_ratio":str(xx),"nonzero_canonical_endpoint":str(S.factor(YY)),
 "polynomial_endpoint_degrees_and_integer_ledger":True,
 "all_HP_jet_and_endpoint_constraints":True,
 "pure_pi_Pade_endpoint_invariance":True,
 "three_algebraic_specializations":[{"b":bb,"x":str(xx.subs(b,bb)),"q":int(S.denom(xx.subs(b,bb)))} for bb in (0,1,2)]}
out=Path(__file__).with_name("hp_mobius_parameter_checks.json")
out.write_text(json.dumps(checks,indent=2)+"\n")
print(json.dumps(checks,indent=2))
