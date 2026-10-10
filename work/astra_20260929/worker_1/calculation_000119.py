from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb, inf
import json

root = Path('[private local path removed]')
path = root / 'work/astra_review_registry/candidates/worker4-b2-five-adic-residue-two-exact-denominator-v1.md'
data = path.read_bytes()
marker = b'UNVERIFIED CANDIDATE. Author: worker_4.'
start = data.index(marker)
body = data[start:]
expected = 'bd96cc2e3fcd4f97c84f74f4c4967a0c79dbae9337bb055a00c6ab693e682c86'
variants = {body, body.rstrip(b'\n'), body + b'\n'}
matched = [v for v in variants if sha256(v).hexdigest() == expected]
assert len(matched) == 1, 'Candidate payload mismatch'
print(json.dumps({'provenance': {'path': str(path), 'file_sha256': sha256(data).hexdigest(), 'payload_start': start, 'payload_bytes': len(matched[0]), 'payload_sha256': expected}}))

samples = [7, 12, 27, 127]
limit = 2 * max(samples) + 3
fac = [1]
for j in range(1, limit + 1):
    fac.append(fac[-1] * j)
e = [1]
for j in range(1, limit + 1):
    e.append(j * e[-1] + 1)
E = [Q(e[j], fac[j]) for j in range(limit + 1)]
assert all(e[j] % 5 == (1, 2, 0, 1, 0)[j % 5] for j in range(limit + 1))

# Expand the original Rodrigues base polynomial by integer convolution.
powers = [[1]]
for m in range(1, max(samples) + 2):
    previous = powers[-1]
    out = [0] * (len(previous) + 2)
    for j, value in enumerate(previous):
        out[j] += value
        out[j + 1] -= 2 * value
        out[j + 2] += 2 * value
    powers.append(out)
Lpoly = [[comb(m + d, m) * powers[m][m + d] for d in range(m + 1)] for m in range(len(powers))]

# Moments from exact Gaussian integer powers, without analytic approximation.
mu = []
gaussian_re, gaussian_im = 1, 0
for j in range(limit):
    gaussian_re, gaussian_im = gaussian_re - gaussian_im, gaussian_re + gaussian_im
    mu.append(Q(2 * gaussian_im, 2**j * (j + 1)))

def valuation(value):
    value = Q(value)
    if not value:
        return inf
    num, den = abs(value.numerator), value.denominator
    result = 0
    while num % 5 == 0:
        num //= 5
        result += 1
    while den % 5 == 0:
        den //= 5
        result -= 1
    return result

def residue(value):
    value = Q(value)
    assert value.denominator % 5
    return value.numerator * pow(value.denominator % 5, -1, 5) % 5

def transform_h(m, derivative):
    # Direct coefficient extraction from exp(xs)(1-s+s^2/2)^m.
    value = sum((Q(fac[m] * powers[m][j], 2**j * fac[m-j-derivative]) for j in range(m-derivative+1)), Q(0))
    assert value.denominator == 1
    return value.numerator

def moments_of_quotient(poly):
    running = 0
    answer = Q(0)
    for j in range(len(poly) - 2, -1, -1):
        running += poly[j + 1]
        answer += running * mu[j]
    assert -running == poly[0] - sum(poly)
    return answer

def T(poly, n, shift=0):
    return sum((coefficient * E[n+d-shift] for d, coefficient in enumerate(poly)), Q(0))

def ell(poly, n, shift):
    return sum((Q(coefficient, fac[n+d+1-shift]) for d, coefficient in enumerate(poly)), Q(0))

def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def convolution_coefficient(B, C, degree):
    exp_part = sum((B[j] / fac[degree-j] for j in range(min(2, degree)+1)), Q(0))
    f_part = sum((C[j] * mu[degree-j-1] for j in range(min(len(C)-1, degree-1)+1)), Q(0))
    return exp_part + f_part

def raw_reconstruction(n, P, U, a, b, X, D, gamma):
    G = Q((-1)**n * 2**(2*n+3), n+1)
    alpha = [ell(U, n, j) for j in range(3)]
    tau = [(a*T(U,n,j)-b*T(P,n,j))/G for j in range(3)]
    beta = cross(alpha, [1+x for x in tau])
    # Reconstruct the projection from its orthogonal-basis kernel expansion.
    qpoly = [Q(0) for _ in range(n+1)]
    for j in range(n+1):
        basis = Lpoly[j]
        norm = Q((-1)**j * 2**(2*j+1), 2*j+1)
        contraction = sum((beta[s]*ell(basis,n,s) for s in range(3)), Q(0))
        for d, coefficient in enumerate(basis):
            qpoly[d] -= coefficient * contraction / norm
    Cpoly = list(reversed(qpoly))
    Apoly = [-convolution_coefficient(beta,Cpoly,d) for d in range(n+1)]
    for degree in range(2*n+3):
        value = convolution_coefficient(beta,Cpoly,degree)
        if degree <= n:
            value += Apoly[degree]
        assert value == 0, ('order',n,degree)
    assert sum(beta) == sum(Cpoly) == gamma*D
    assert sum(Apoly) == gamma*X
    assert sum(Apoly)/sum(beta) == X/D
    return {'n': n, 'order_through': 2*n+2, 'raw_scaling_and_matching': True}

def solve_linear(matrix, rhs):
    size = len(rhs)
    assert all(len(row) == size for row in matrix)
    rows = [[Q(x) for x in row] + [Q(y)] for row,y in zip(matrix,rhs)]
    for column in range(size):
        pivot = next(j for j in range(column,size) if rows[j][column])
        rows[column],rows[pivot] = rows[pivot],rows[column]
        scale = rows[column][column]
        rows[column] = [x/scale for x in rows[column]]
        for j in range(size):
            if j == column or not rows[j][column]:
                continue
            multiplier = rows[j][column]
            rows[j] = [x-multiplier*y for x,y in zip(rows[j],rows[column])]
    return [row[-1] for row in rows]

def direct_system(n, expected_ratio):
    # Eliminate A using its degree cap; solve directly for B and C.
    matrix, rhs = [], []
    for degree in range(n+1,2*n+3):
        matrix.append([Q(1,fac[degree-j]) for j in range(3)] + [mu[degree-j-1] for j in range(n+1)])
        rhs.append(0)
    matrix.append([-1]*3+[1]*(n+1))
    rhs.append(0)
    matrix.append([1]*3+[0]*(n+1))
    rhs.append(1)
    solution = solve_linear(matrix,rhs)
    B,C = solution[:3],solution[3:]
    assert sum(B) == sum(C) == 1
    A = [-convolution_coefficient(B,C,d) for d in range(n+1)]
    assert sum(A) == expected_ratio
    return {'n':n,'independent_normalized_system':True,'ratio_numerator':str(expected_ratio.numerator),'ratio_denominator':str(expected_ratio.denominator)}

rows = []
raw_checks = []
low_checks = 0
for n in samples:
    P,U = Lpoly[n],Lpoly[n+1]
    a,b = sum(P),sum(U)
    f = Q(2**n,fac[n]**2)
    k = (n+1)**2
    h,dh,ddh = [transform_h(n,j) for j in range(3)]
    eta,deta,ddeta = [transform_h(n+1,j) for j in range(3)]
    J = n*h+dh
    Ju = (n+1)*eta+deta
    Ku = n*(n+1)*eta+2*(n+1)*deta+ddeta
    S = Ju*Ju-eta*Ku
    C = (Ju-eta)*J-(Ku-Ju)*h
    W = Ju*J-Ku*h
    assert tuple(x%5 for x in (h,J,eta,Ju,Ku,S,C,W,k)) == (1,0,0,2,0,4,2,0,4)
    assert ell(P,n,1) == f*h and ell(P,n,2) == f*J
    g = 2*f/k
    assert [ell(U,n,j) for j in range(3)] == [g*eta,g*Ju,g*Ku]
    wP,wU = moments_of_quotient(P),moments_of_quotient(U)
    G = Q((-1)**n * 2**(2*n+3),n+1)
    assert a*wU-b*wP == G
    TP,TU = T(P,n),T(U,n)
    pterms = [Q(fac[n],fac[d]*2**n)*powers[n][n+d]*e[n+d] for d in range(n+1)]
    uterms = [Q(fac[n],fac[d]*2**n*(n+1))*(n+1+d)*powers[n+1][n+1+d]*e[n+d] for d in range(n+2)]
    assert sum(pterms) == TP/f and sum(uterms) == TU/f
    depth = valuation(n-2)
    for term in pterms[:n-2]+uterms[:n-2]:
        assert valuation(term) >= depth
        low_checks += 1
    pexpected = [Q(n**3*(n-1),2)*e[2*n-2], -n*n*e[2*n-1], e[2*n]]
    uexpected = [-Q(n*n*(n-1)*(n+2)*(2*n-1),3)*e[2*n-2], 2*n*n*(n+1)*e[2*n-1], -2*(2*n+1)*e[2*n], Q(4,n+1)*e[2*n+1]]
    assert pterms[n-2:] == pexpected
    assert uterms[n-2:] == uexpected
    assert [residue(x) for x in pexpected] == [0,1,0]
    assert [residue(x) for x in uexpected] == [0,4,0,3]
    for m in (n,n+1):
        expected_high = [2**m,-m*2**m,m*m*2**(m-1),-Q(m*(m-1)*(m+1)*2**(m-1),3)]
        assert [powers[m][2*m-j] for j in range(4)] == expected_high
    r = valuation(fac[n])
    L = 0
    power = 5
    while power <= n:
        L += 1
        power *= 5
    assert valuation(wP/f) >= 2*r-L >= 1
    assert valuation(wU/f) >= 2*r-L
    D = Q(k*b*C-2*a*S)
    X = 2*(wP+TP)*S-k*(wU+TU)*C-2*f*eta*W
    assert residue(a) != 0 and residue(D/a) == 4
    assert (residue(TP/f),residue(TU/f),residue(X/f)) == (1,2,2)
    ratio = X/D
    assert (valuation(D),valuation(X),valuation(ratio.denominator)) == (0,-2*r,2*r)
    gamma = Q((-1)**n,4*(n+1)**3*fac[n]**4)
    assert (valuation(gamma*X),valuation(gamma*D)) == (-6*r,-4*r)
    rows.append({'n':n,'v5_n_minus_2':depth,'r':r,'L':L,'v5_D':valuation(D),'v5_X':valuation(X),'v5_q':valuation(ratio.denominator),'D_over_a_mod5':residue(D/a),'TP_TU_X_over_f_mod5':[residue(TP/f),residue(TU/f),residue(X/f)],'U_contributions_mod5':[residue(x) for x in uexpected]})
    if n in (7,27):
        raw_checks.append(raw_reconstruction(n,P,U,a,b,X,D,gamma))
    if n == 7:
        system_check = direct_system(n,ratio)
print(json.dumps({'samples':rows,'individual_omitted_term_checks':low_checks,'raw_reconstruction_checks':raw_checks,'independent_system':system_check,'all_assertions_passed':True}))