"""Corrected jet evaluation truncates modulo z^k before finite lookup.
One exact k=3 return identity test; the original script is preserved.
"""
import json
from pathlib import Path
import sympy as sp

k = 3
z, x = sp.symbols('z x')
gamma = sp.Rational(4**(k-1), sp.binomial(2*k-2, k-1))
c = 4*gamma
maxn = 3*k-2
Dnums = [sp.Integer(1)]
for r in range(1, 2*maxn+1):
    Dnums.append(r*Dnums[-1]+(-1)**r)
mu_m = [sum(sp.binomial(n,r)*Dnums[2*r] for r in range(n+1)) for n in range(maxn+1)]
f_m = [sum(sp.binomial(n,r)*sp.factorial(2*r) for r in range(n+1)) for n in range(maxn+1)]
i_m = [sum(sp.binomial(n,r)/sp.Integer(2*r+1) for r in range(n+1)) for n in range(maxn+1)]
nu_m = [gamma*sp.binomial(2*(k-1-n), k-1-n)/4**(k-1-n) if n<k else sp.Integer(0) for n in range(maxn+1)]
# Independent exact integration retains both rational and pi endpoints.
compact_integrals = [sp.integrate((1+x*x)**(n-k), (x,0,1)) for n in range(maxn+1)]
R_m = [sp.simplify(c*compact_integrals[n]-sp.pi*nu_m[n]-f_m[n]) for n in range(maxn+1)]
assert all(value.is_Rational for value in R_m)

def apply(moments, P):
    P = sp.Poly(sp.expand(P), z)
    return sp.expand(sum(coef*moments[n[0]] for n,coef in P.terms()))

def rem(P):
    return sp.rem(sp.expand(P), z**k, z)

def quo(P):
    return sp.div(sp.expand(P), z**k, z)[0]

def poly(v):
    return sum(v[j]*z**j for j in range(k))

def vec(P):
    P = sp.expand(P)
    return sp.Matrix([P.coeff(z,j) for j in range(k)])

mu = lambda P: apply(mu_m,P)
f = lambda P: apply(f_m,P)
integ = lambda P: apply(i_m,P)
nu = lambda P: apply(nu_m,rem(P))
R = lambda P: apply(R_m,P)
Cfun = lambda P: mu(P)-nu(P)
tau = sum(sp.Rational(1,n)*sum(sp.Rational(1,2**b)*sp.binomial(2*(n-1-b),n-1-b)/4**(n-1-b) for b in range(n))*z**n for n in range(1,k))
assert tau == z+z*z/2
for n in range(maxn+1):
    assert R(z**n) == -f(z**n)+c*integ(quo(z**n))+nu(tau*z**n)

J = sp.Matrix(k,k,lambda i,j: nu(z**(i+j)))
G = sp.Matrix(k,k,lambda i,j: mu(z**(k+i+j)))
C = sp.Matrix(k,k,lambda i,j: Cfun(z**(i+j)))
B = sp.Matrix(k,k,lambda i,j: R(z**(i+j)))
D = sp.Matrix(k,k,lambda i,j: R(z**(k+i+j)))
nu_inverse_symbol = sp.series(sp.sqrt(1-z)/gamma,z,0,k).removeO()
for j in range(k):
    rhs = sp.eye(k)[:,j]
    q = rem(nu_inverse_symbol*sum(rhs[i]*z**(k-1-i) for i in range(k)))
    assert J*vec(q) == rhs

# Exact rational Schur split of the ACTUAL G, without prime factorization.
# This tests the algebra, not occurrence of the one-positive-depth branch.
Ablock = G[:k-1,:k-1]
b = G[:k-1,k-1]
schur = sp.cancel(G[k-1,k-1]-(b.T*Ablock.inv()*b)[0])
G0 = sp.diag(Ablock.inv(),sp.zeros(1))
xx = (-Ablock.inv()*b).col_join(sp.ones(1,1))
yy = xx
assert G.inv() == G0+xx*yy.T/schur
H0 = J.inv()*(D*G0*C-B)
U = J.inv()*D*xx
Z = J.inv()*C*yy
N = sp.zeros(k)
for j in range(k-1):
    N[j+1,j] = 1
tauN = N+N**2/2
F_low = sp.Matrix(k,k,lambda i,j: f(z**(i+j)))
Kplus = sp.Matrix(k,k,lambda i,j: integ(z**(i+j-k)) if i+j>=k else 0)
Aop = J.inv()*(D*G0*C+F_low-c*Kplus)
assert H0 == Aop-tauN
assert B == -F_low+c*Kplus+J*tauN

# Check r_j and r_(j+1) from the new scalar first-return identity,
# retaining the complete B inside H0. Normalizations e_u,e_v are not tested.
Zp = poly(Z)
current = U
return_checks = []
for j in range(2):
    Up = poly(current)
    Qp = poly(G0*C*current)
    Pj = rem(Zp*Up)
    Tj = sp.expand(Zp*Qp-quo(Zp*Up))
    rj = (Z.T*J*current)[0]
    rnext = (Z.T*J*H0*current)[0]
    explicit = f(Pj)-f(z**k*Tj)+c*integ(Tj)-nu(tau*Pj)
    assert rj == nu(Pj)
    assert sp.cancel(rnext-explicit) == 0
    return_checks.append({'j':j,'r_j':str(rj),'r_next':str(rnext),
        'P_j':str(Pj),'T_j':str(Tj),'identity':True})
    current = H0*current
assert sp.cancel((yy.T*C*U)[0]-R(z**k*poly(xx)*Zp)) == 0

# The pure endpoint observation transform is p-unimodular when J is.
S = sp.Matrix.hstack(*[vec(rem(tau**j)) for j in range(k)])
assert S.det() == 1
obs = sp.Matrix(k,k,lambda j,i: nu(tau**j*z**i))
assert obs == S.T*J
assert obs.det() == J.det()

receipt = {
    'purpose':'Single k=3 actual-moment check of complete remainder decomposition and first/second return identities; no primes, scans, or branch-occurrence claim.',
    'k':k,'gamma':str(gamma),'tau':str(tau),
    'complete_R_moments':[str(a) for a in R_m],
    'J':[[str(a) for a in J.row(i)] for i in range(k)],
    'rational_schur_scalar':str(schur),
    'return_checks':return_checks,
    'checks':{'independent_compact_integrals':True,'complete_remainder_identity':True,
        'explicit_inverse_jet_symbol':True,'complete_B_split':True,
        'H0_endpoint_split':True,'first_and_second_return':True,
        'endpoint_observation_determinant':True},
    'limitations':'Exact rational algebra on one actual size; no p-adic Smith branch selected, no contraction depths numerically tested, no uniform return-depth bound or independent verification.'
}
Path('ACTUAL_RETURN_REDUCTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'all assertions passed','k':k,'moment_identities':maxn+1,'return_steps':len(return_checks),'receipt':'ACTUAL_RETURN_REDUCTION_RECEIPT.json'},indent=2))
