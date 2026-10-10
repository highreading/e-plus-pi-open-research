from fractions import Fraction as F
from math import factorial, gcd
import json

# Exact rational arithmetic only. No source files are executed or modified.
def valuation(x, p=3):
    x = F(x)
    if not x:
        return 'inf'
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v

def residue(x, modulus=3):
    x = F(x)
    assert gcd(x.denominator, modulus) == 1
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus

def base_power(m):
    u = [1]
    for _ in range(m):
        nxt = [0] * (len(u) + 2)
        for j, c in enumerate(u):
            nxt[j] += c
            nxt[j+1] -= 2*c
            nxt[j+2] += 2*c
        u = nxt
    return u

def legendre(m, u):
    return [factorial(m+d)//(factorial(m)*factorial(d))*u[m+d]
            for d in range(m+1)]

def h_derivative(m, derivative, u):
    # H_m(x)=m![s^m] exp(xs)(1-s+s^2/2)^m.
    value = sum((F(factorial(m)*u[j],
                   factorial(m-j-derivative)*2**j)
                 for j in range(m-derivative+1)), F(0))
    assert value.denominator == 1
    return value.numerator

def content(coeffs):
    vals = [valuation(c) for c in coeffs if c]
    return min(vals) if vals else 'inf'

results = []
for n in (4, 7, 10, 28):
    top = 2*n+4
    fac = [factorial(j) for j in range(top+2)]
    E = []
    running = F(0)
    for j in range(top+1):
        running += F(1, fac[j])
        E.append(running)
    # Original rational moment formula, evaluated using integer complex powers.
    mu = []
    real, imag = 1, 0
    for j in range(top+1):
        real, imag = real-imag, real+imag
        mu.append(F(2*imag, 2**j*(j+1)))
    moment_prefix = [F(0)]
    for value in mu:
        moment_prefix.append(moment_prefix[-1]+value)
    powers = [base_power(m) for m in range(n+2)]
    polys = [legendre(m, powers[m]) for m in range(n+2)]
    P, U = polys[n], polys[n+1]
    a, b = sum(P), sum(U)
    k = (n+1)**2
    f = F(2**n, fac[n]**2)
    G = F((-1)**n*2**(2*n+3), n+1)
    gamma = F((-1)**n, 4*(n+1)**3*fac[n]**4)
    def ell(poly, j):
        return sum((F(c, fac[n+d+1-j]) for d,c in enumerate(poly)), F(0))
    def T(poly, j):
        return sum((c*E[n+d-j] for d,c in enumerate(poly)), F(0))
    def w(poly):
        return sum((poly[d]*moment_prefix[d] for d in range(1,len(poly))), F(0))
    alpha = [ell(U,j) for j in range(3)]
    matching = [1+(a*T(U,j)-b*T(P,j))/G for j in range(3)]
    beta = [alpha[1]*matching[2]-alpha[2]*matching[1],
            alpha[2]*matching[0]-alpha[0]*matching[2],
            alpha[0]*matching[1]-alpha[1]*matching[0]]
    # Independent reconstruction from the orthogonal-polynomial kernel sum.
    Q = [F(0)]*(n+1)
    for m in range(n+1):
        contraction = sum((beta[j]*ell(polys[m],j) for j in range(3)), F(0))
        multiplier = -F((-1)**m*(2*m+1), 2**(2*m+1))*contraction
        for d,c in enumerate(polys[m]):
            Q[d] += multiplier*c
    Cpoly = Q[::-1]
    def unfixed_coefficient(degree):
        exponential = sum((beta[j]/fac[degree-j]
                           for j in range(3) if degree >= j), F(0))
        moment = sum((Cpoly[j]*mu[degree-j-1]
                      for j in range(n+1) if degree-j >= 1), F(0))
        return exponential+moment
    Apoly = [-unfixed_coefficient(d) for d in range(n+1)]
    for degree in range(2*n+3):
        assert unfixed_coefficient(degree)+(Apoly[degree] if degree <= n else 0) == 0
    Aend, Bend, Cend = sum(Apoly), sum(beta), sum(Cpoly)
    assert Bend == Cend
    h = h_derivative(n,0,powers[n])
    hp = h_derivative(n,1,powers[n])
    eta = h_derivative(n+1,0,powers[n+1])
    etap = h_derivative(n+1,1,powers[n+1])
    etapp = h_derivative(n+1,2,powers[n+1])
    Jn = n*h+hp
    Jm = (n+1)*eta+etap
    Km = (n+1)*n*eta+2*(n+1)*etap+etapp
    S = Jm*Jm-eta*Km
    Cscalar = (Jm-eta)*Jn-(Km-Jm)*h
    W = Jm*Jn-Km*h
    wp, wu, tp, tu = w(P), w(U), T(P,0), T(U,0)
    D = k*b*Cscalar-2*a*S
    normalized_terms = [2*(wp+tp)*S/f, -k*(wu+tu)*Cscalar/f, F(-2*eta*W)]
    N = sum(normalized_terms,F(0))
    X = f*N
    assert Aend == gamma*X
    assert Bend == gamma*D
    assert X != 0 and D != 0
    ratio = X/D
    assert ratio == Aend/Bend
    assert residue(tp/f) == 0 and residue(tu/f) == 1
    assert residue(N) == 1
    r = valuation(fac[n])
    assert valuation(ratio.denominator) == 2*r+valuation(D)
    results.append({
        'n':n, 'v3_n_minus_1':valuation(n-1), 'r':r,
        'complete_reduced_ratio':str(ratio),
        'D':str(D), 'X_over_f':str(N),
        'v3_D':valuation(D), 'v3_X':valuation(X),
        'v3_reduced_denominator':valuation(ratio.denominator),
        'v3_raw_A_endpoint':valuation(Aend),
        'v3_raw_B_endpoint':valuation(Bend),
        'raw_coefficient_contents_A_B_C':[content(Apoly),content(beta),content(Cpoly)],
        'v3_normalized_numerator_terms':[valuation(z) for z in normalized_terms],
        'v3_moments_divided_by_f':[valuation(wp/f),valuation(wu/f)],
        'normalized_partial_exponentials_mod3':[residue(tp/f),residue(tu/f)],
        'v3_S_C_W_eta':[valuation(S),valuation(Cscalar),valuation(W),valuation(eta)],
        'v3_denominator_terms':[valuation(k*b*Cscalar),valuation(2*a*S)],
        'v3_b_minus_a':valuation(b-a),
        'v3_kC_minus_2S':valuation(k*Cscalar-2*S),
        'v3_split_denominator_terms':[valuation(k*Cscalar*(b-a)),valuation(a*(k*Cscalar-2*S))],
        'order_conditions_through':2*n+2,
        'endpoint_and_order_checks':'passed'
    })
print(json.dumps(results, indent=2))