from fractions import Fraction as Q
from math import factorial, comb
import json

def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

def power(p, m):
    out = [1]
    for _ in range(m):
        out = mul(out, p)
    return out

def legendre_scaled(m):
    coeff = power([1, -2, 2], m)
    return [comb(m+d, m)*coeff[m+d] for d in range(m+1)]

def moment(d):
    x, y = 1, 0
    for _ in range(d+1):
        x, y = x-y, x+y
    return Q(2*y, 2**d*(d+1))

def h_derivative(m, j):
    if j > m:
        return 0
    coeff = power([Q(1), Q(-1), Q(1, 2)], m)
    value = factorial(m)*sum((coeff[s]/factorial(m-j-s) for s in range(m-j+1)), Q(0))
    assert value.denominator == 1
    return value.numerator

def vp_int(a):
    a = abs(a)
    if a == 0:
        return float('inf')
    v = 0
    while a % 3 == 0:
        a //= 3
        v += 1
    return v

def vp(x):
    x = Q(x)
    return vp_int(x.numerator)-vp_int(x.denominator) if x else float('inf')

def residue(x):
    x = Q(x)
    assert x.denominator % 3 != 0
    return (x.numerator * pow(x.denominator, -1, 3)) % 3

def content_v(poly):
    return min(vp(c) for c in poly)

rows = []
for n in [3, 6, 9, 12]:
    polys = [legendre_scaled(m) for m in range(n+2)]
    P, U = polys[n], polys[n+1]
    a, b = sum(P), sum(U)
    mu = [moment(d) for d in range(2*n+2)]
    Fcoef = [Q(0)] + mu
    kernel = [[Q(0) for _ in range(n+1)] for _ in range(n+1)]
    for m in range(n+1):
        weight = Q((-1)**m*(2*m+1), 2**(2*m+1))
        for d in range(m+1):
            for e in range(m+1):
                kernel[d][e] += weight*polys[m][d]*polys[m][e]
    projections = []
    for j in range(3):
        projections.append([sum((kernel[d][e]/factorial(n+e+1-j) for e in range(n+1)), Q(0)) for d in range(n+1)])
    ar = [sum((Q(U[d], factorial(n+d+1-j)) for d in range(n+2)), Q(0)) for j in range(3)]
    tr = [sum(row) for row in projections]
    br = [1+t for t in tr]
    B = [ar[1]*br[2]-ar[2]*br[1], ar[2]*br[0]-ar[0]*br[2], ar[0]*br[1]-ar[1]*br[0]]
    Cstar = [-sum((B[j]*projections[j][d] for j in range(3)), Q(0)) for d in range(n+1)]
    Cpoly = Cstar[::-1]
    def exp_coefficient(k):
        return sum((B[j]/factorial(k-j) for j in range(min(k, 2)+1)), Q(0))
    def logarithmic_coefficient(k):
        return sum((Cpoly[d]*Fcoef[k-d] for d in range(min(k, n)+1)), Q(0))
    Apoly = [-exp_coefficient(k)-logarithmic_coefficient(k) for k in range(n+1)]
    for k0 in range(2*n+3):
        assert (Apoly[k0] if k0 <= n else 0)+exp_coefficient(k0)+logarithmic_coefficient(k0) == 0
    rawX, rawY = sum(Apoly), sum(B)
    assert sum(Cpoly) == rawY
    assert rawY != 0

    h = h_derivative(n, 0)
    Jn = n*h+h_derivative(n, 1)
    eta = h_derivative(n+1, 0)
    J = (n+1)*eta+h_derivative(n+1, 1)
    K = n*(n+1)*eta+2*(n+1)*h_derivative(n+1, 1)+h_derivative(n+1, 2)
    S = J*J-eta*K
    Cscalar = (J-eta)*Jn-(K-J)*h
    W = J*Jn-K*h
    k = (n+1)**2
    f = Q(2**n, factorial(n)**2)
    gamma = Q((-1)**n, 4*(n+1)**3*factorial(n)**4)
    E = [Q(1)]
    for j in range(1, 2*n+2):
        E.append(E[-1]+Q(1, factorial(j)))
    def T(poly):
        return sum((c*E[n+d] for d, c in enumerate(poly)), Q(0))
    def w(poly):
        return sum((poly[d]*sum(mu[:d], Q(0)) for d in range(1, len(poly))), Q(0))
    TP, TU, wP, wU = T(P), T(U), w(P), w(U)
    D = k*b*Cscalar-2*a*S
    X = 2*(wP+TP)*S-k*(wU+TU)*Cscalar-2*f*eta*W
    theta = X/f
    assert rawY == gamma*D
    assert rawX == gamma*X
    assert [residue(h), residue(Jn), residue(eta), residue(J), residue(K)] == [1, 0, 0, 1, 2]
    assert [residue(TP/f), residue(TU/f), residue(wP/f), residue(wU/f), residue(theta)] == [1, 0, 0, 0, 2]
    assert residue(b) == 2*residue(a) % 3
    assert residue(D) == 2*residue(a) % 3 != 0
    r = vp_int(factorial(n))
    L, z = 0, n
    while z >= 3:
        z //= 3
        L += 1
    nuA, nuB, nuC = content_v(Apoly), content_v(B), content_v(Cpoly)
    nu = min(nuA, nuB, nuC)
    c = -6*r-nu
    q = (rawX/rawY).denominator
    assert vp(D) == 0 and vp(X) == -2*r
    assert vp(rawY) == -4*r and vp(rawX) == -6*r
    assert nuB == -4*r and nuC >= -6*r
    assert -6*r-L <= nu <= -6*r
    assert 0 <= c <= L
    assert vp_int(q) == 2*r
    rows.append({'n': n, 'v3_n_factorial': r, 'v3_D': vp(D), 'v3_X': vp(X), 'v3_raw_Y': vp(rawY), 'v3_raw_X': vp(rawX), 'nu_A': nuA, 'nu_B': nuB, 'nu_C': nuC, 'nu_full': nu, 'primitive_endpoint_gcd_v3': c, 'v3_q': vp_int(q), 'q_decimal_digits': len(str(q)), 'scaled_TP_TU_theta_mod3': [residue(TP/f), residue(TU/f), residue(theta)], 'full_order_and_endpoint_checks': True})
print(json.dumps({'status': 'all bounded exact checks passed', 'rows': rows}, indent=2))