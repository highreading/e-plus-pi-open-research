import sys, json
from fractions import Fraction as Q
from math import comb, factorial
sys.path.insert(0, '[private local path removed]')
import mpmath as mp
mp.mp.dps = 260
indices = [4, 5, 8, 16, 32, 64]
M = max(indices)

# Construct the monic orthogonal polynomials over Q.
p = [[Q(1)], [Q(-1, 2), Q(1)]]
for k in range(1, M + 1):
    cur = [Q(0)] * (len(p[k]) + 1)
    for j, c in enumerate(p[k]):
        cur[j] -= c / 2
        cur[j + 1] += c
    beta = Q(k*k, 4*(4*k*k - 1))
    for j, c in enumerate(p[k-1]):
        cur[j] += beta*c
    p.append(cur)
a = [sum(row, Q(0)) for row in p]
h = [Q(2*(-1)**k, (2*k+1)*comb(2*k, k)**2) for k in range(M+2)]

# Exact moments: L(t^j)=4 Im(((1+i)/2)^(j+1))/(j+1).
mu = []
re, im = Q(1), Q(0)
for j in range(M+1):
    re, im = (re-im)/2, (re+im)/2
    mu.append(4*im/(j+1))
prefix = [Q(0)]
for x in mu:
    prefix.append(prefix[-1] + x)
r = [sum((c*prefix[j] for j, c in enumerate(row)), Q(0)) for row in p]

facts = [factorial(j) for j in range(2*M+4)]
E = []
partial = Q(0)
for fct in facts:
    partial += Q(1, fct)
    E.append(partial)

def ell(row, j, n):
    return sum((c/facts[n+k+1-j] for k, c in enumerate(row)), Q(0))

def resolvent_pair(row, j, n):
    # Coefficients in ascending powers of the formal variable e.
    return [-sum((c*E[n+k-j] for k, c in enumerate(row)), Q(0)), sum(row, Q(0))]

def product_pair(x, y):
    return [x[0]*y[0], x[0]*y[1]+x[1]*y[0], x[1]*y[1]]

def to_mp(x):
    return mp.mpf(x.numerator)/x.denominator

target = -mp.exp(-mp.sqrt(2))
rows = []
for n in indices:
    V, Z = [Q(0)]*(n+1), [Q(0)]*(n+1)
    for k in range(n+1):
        for j, c in enumerate(p[k]):
            V[j] += a[k]*c/h[k]
            Z[j] += r[k]*c/h[k]
    v0, v1 = ell(V, 0, n), ell(V, 1, n)
    z0, z1 = ell(Z, 0, n), ell(Z, 1, n)
    D = v1-v0
    C = v1*E[n]-v0*E[n-1]+v0*z1-v1*z0
    left = product_pair(resolvent_pair(p[n], 0, n), resolvent_pair(p[n+1], 1, n))
    right = product_pair(resolvent_pair(p[n], 1, n), resolvent_pair(p[n+1], 0, n))
    det_coeff = [(x-y)/h[n] for x, y in zip(left, right)]
    scalar_ok = det_coeff == [C, -D, Q(0)]
    wronskian_ok = a[n]*r[n+1]-a[n+1]*r[n] == h[n]
    assert scalar_ok and wronskian_ok
    record = {'n': n, 'scalar_identity_exact': scalar_ok, 'wronskian_exact': wronskian_ok, 'D_nonzero': D != 0}
    if D:
        W0 = 1-mp.pi*to_mp(V[0])+to_mp(Z[0])
        N = to_mp(C)-to_mp(D)*mp.e
        normalized = mp.mpf(facts[n])*n**3*N/(to_mp(D)*W0)
        record['W0'] = mp.nstr(W0, 24)
        record['normalized_cofactor'] = mp.nstr(normalized, 30)
        record['ratio_to_predicted_limit'] = mp.nstr(normalized/target, 24)
    rows.append(record)
print(json.dumps({'precision_decimal_digits': mp.mp.dps, 'predicted_limit': mp.nstr(target, 40), 'exact_identity_checks': 2*len(indices), 'results': rows, 'scope': 'Exact finite algebra and numerical asymptotic checks only; no denominator-growth conclusion.'}, indent=2))