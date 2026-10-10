from fractions import Fraction as F
from math import factorial, comb
import json


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    c = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def pscale(a, s):
    return trim([F(s) * x for x in a])


def psub(a, b):
    return padd(a, pscale(b, -1))


def pmul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def ppow(a, n):
    out = [F(1)]
    for _ in range(n):
        out = pmul(out, a)
    return out


def vp(x, p=5):
    x = F(x)
    if x == 0:
        return None
    num, den = abs(x.numerator), x.denominator
    value = 0
    while num % p == 0:
        value += 1
        num //= p
    while den % p == 0:
        value -= 1
        den //= p
    return value


def mod5(x):
    x = F(x)
    assert x.denominator % 5 != 0, ('nonintegral residue', str(x))
    return (x.numerator * pow(x.denominator, -1, 5)) % 5


def poly_mod5(a):
    return trim([mod5(x) for x in a])


def legendre_transform(m):
    u = ppow([F(1), F(-2), F(2)], m)
    out = [comb(m+d, m) * u[m+d] for d in range(m+1)]
    assert all(x.denominator == 1 for x in out)
    return out


def h_derivatives(m):
    u = ppow([F(1), F(-1), F(1, 2)], m)
    out = []
    for j in range(3):
        value = F(0)
        if j <= m:
            value = factorial(m) * sum((u[s] / factorial(m-s-j) for s in range(m-j+1)), F(0))
        assert value.denominator == 1
        out.append(value)
    return out


def moment(j):
    re, im = 1, 0
    for _ in range(j+1):
        re, im = re-im, re+im
    return F(2*im, 2**j * (j+1))


def solve_exact(matrix, rhs):
    size = len(rhs)
    rows = [[F(x) for x in matrix[i]] + [F(rhs[i])] for i in range(size)]
    for col in range(size):
        pivot = next(i for i in range(col, size) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [x/scale for x in rows[col]]
        for i in range(size):
            if i != col and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [x-scale*y for x, y in zip(rows[i], rows[col])]
    return [row[-1] for row in rows]


def coefficient_minimum(poly):
    return min(vp(x) for x in poly if x)


examples = []
for n in (5, 10):
    P, U = legendre_transform(n), legendre_transform(n+1)
    a, b = sum(P), sum(U)
    hn, hp, hpp = h_derivatives(n)
    eta, ep, epp = h_derivatives(n+1)
    Jn = n*hn + hp
    Jnext = (n+1)*eta + ep
    Knext = n*(n+1)*eta + 2*(n+1)*ep + epp
    S = Jnext**2 - eta*Knext
    C = (Jnext-eta)*Jn - (Knext-Jnext)*hn
    W = Jnext*Jn - Knext*hn
    k = (n+1)**2
    f = F(2**n, factorial(n)**2)
    G = F((-1)**n * 2**(2*n+3), n+1)
    gamma = F((-1)**n, 4*(n+1)**3*factorial(n)**4)
    E = [F(1)]
    for j in range(1, 2*n+3):
        E.append(E[-1] + F(1, factorial(j)))

    def T(poly, j=0):
        return sum((coef*E[n+d-j] for d, coef in enumerate(poly)), F(0))

    def w(poly):
        return sum((moment(j)*sum(poly[j+1:]) for j in range(len(poly)-1)), F(0))

    TP, TU, wP, wU = T(P), T(U), w(P), w(U)
    Pstar, Ustar = wP+TP, wU+TU
    D = k*b*C - 2*a*S
    X = 2*Pstar*S - k*Ustar*C - 2*f*eta*W
    assert D.denominator == 1 and D != 0
    ratio = X/D

    # Reconstruct the specified raw B, then solve the rational moment equations
    # for Q independently of the Christoffel-Darboux reconstruction formula.
    alpha = [sum((coef/F(factorial(n+d+1-j)) for d, coef in enumerate(U)), F(0)) for j in range(3)]
    t = [(a*T(U, j)-b*T(P, j))/G for j in range(3)]
    second = [1+x for x in t]
    Braw = [alpha[1]*second[2]-alpha[2]*second[1],
            alpha[2]*second[0]-alpha[0]*second[2],
            alpha[0]*second[1]-alpha[1]*second[0]]
    mat = [[moment(s+d) for d in range(n+1)] for s in range(n+1)]
    rhs = [-sum((Braw[j]/factorial(n+s+1-j) for j in range(3)), F(0)) for s in range(n+1)]
    Qraw = solve_exact(mat, rhs)
    Craw = Qraw[::-1]

    def exp_coefficient(degree):
        return sum((Braw[j]/factorial(degree-j) for j in range(min(2, degree)+1)), F(0))

    def cf_coefficient(degree):
        return sum((Craw[j]*moment(degree-j-1) for j in range(min(n, degree-1)+1)), F(0))

    Araw = [-exp_coefficient(degree)-cf_coefficient(degree) for degree in range(n+1)]
    for degree in range(2*n+3):
        remainder = (Araw[degree] if degree <= n else F(0)) + exp_coefficient(degree) + cf_coefficient(degree)
        assert remainder == 0, ('order condition', n, degree, str(remainder))
    A1, B1, C1 = sum(Araw), sum(Braw), sum(Craw)
    assert B1 == C1 == gamma*D
    assert A1 == gamma*X
    assert A1/B1 == ratio

    r = vp(factorial(n))
    normalized = {'TP_over_f': mod5(TP/f), 'TU_over_f': mod5(TU/f),
                  'wP_over_f': mod5(wP/f), 'wU_over_f': mod5(wU/f),
                  'Pstar_over_f': mod5(Pstar/f), 'Ustar_over_f': mod5(Ustar/f),
                  'X_over_f': mod5(X/f)}
    assert normalized == {'TP_over_f': 1, 'TU_over_f': 1, 'wP_over_f': 0,
                          'wU_over_f': 0, 'Pstar_over_f': 1, 'Ustar_over_f': 1,
                          'X_over_f': 3}
    assert (vp(D), vp(X), vp(ratio.denominator)) == (0, -2*r, 2*r)
    assert (vp(gamma), vp(A1), vp(B1)) == (-4*r, -6*r, -4*r)
    assert mod5(D) == mod5(a) != 0
    examples.append({'n': n, 'v5_factorial': r, 'a': str(a), 'b': str(b),
                     'auxiliary_values': {name: str(value) for name, value in
                         [('h_n', hn), ('J_n', Jn), ('eta', eta), ('J_next', Jnext),
                          ('K_next', Knext), ('S', S), ('C', C), ('W', W)]},
                     'D': str(D), 'X': str(X), 'X_over_f': str(X/f),
                     'reduced_numerator': str(ratio.numerator),
                     'reduced_denominator': str(ratio.denominator),
                     'normalized_residues_mod5': normalized,
                     'valuations': {'D': vp(D), 'X': vp(X), 'q': vp(ratio.denominator),
                                    'gamma': vp(gamma), 'A_raw_at_1': vp(A1), 'B_raw_at_1': vp(B1)},
                     'raw_endpoints': {'A': str(A1), 'B': str(B1)},
                     'raw_coefficient_minima': {'A': coefficient_minimum(Araw),
                                               'B': coefficient_minimum(Braw),
                                               'C': coefficient_minimum(Craw)},
                     'order_verified_through_degree': 2*n+2,
                     'endpoint_reconstruction_passed': True})


# A bounded coefficientwise calculation on X=5Y and X=1+5Y.
def falling_on_disk(a, length):
    out = [F(1)]
    for j in range(length):
        out = pmul(out, [F(a-j), F(5)])
    return out


def interpolation(a, derivative, cutoff):
    out = [F(0)]
    for c in range((cutoff-1)//2+1):
        for b in range(cutoff-2*c):
            s = b+2*c
            term = pmul(falling_on_disk(a, s+derivative), falling_on_disk(a, b+c))
            out = padd(out, pscale(term, F((-1)**b, 2**c*factorial(b)*factorial(c))))
    return out


derivatives = {}
for a in (0, 1):
    for derivative in range(3):
        short = interpolation(a, derivative, 5)
        extended = interpolation(a, derivative, 10)
        assert poly_mod5(short) == poly_mod5(extended)
        derivatives[a, derivative] = short
expected = {(0, 0): [1], (0, 1): [0], (0, 2): [0],
            (1, 0): [0], (1, 1): [1], (1, 2): [0]}
assert {key: poly_mod5(value) for key, value in derivatives.items()} == expected

N, N1 = [F(0), F(5)], [F(1), F(5)]
h = derivatives[0, 0]
j = padd(pmul(N, h), derivatives[0, 1])
eta_poly = derivatives[1, 0]
j1 = padd(pmul(N1, eta_poly), derivatives[1, 1])
k1 = padd(padd(pmul(pmul(N, N1), eta_poly), pscale(pmul(N1, derivatives[1, 1]), 2)), derivatives[1, 2])
s_poly = psub(pmul(j1, j1), pmul(eta_poly, k1))
c_poly = psub(pmul(psub(j1, eta_poly), j), pmul(psub(k1, j1), h))
w_poly = psub(pmul(j1, j), pmul(k1, h))
auxiliary_disk = {name: poly_mod5(value) for name, value in
                  [('h_n', h), ('J_n', j), ('eta', eta_poly), ('J_next', j1),
                   ('K_next', k1), ('S', s_poly), ('C', c_poly), ('W', w_poly)]}
assert auxiliary_disk == {'h_n': [1], 'J_n': [0], 'eta': [0], 'J_next': [1],
                          'K_next': [2], 'S': [1], 'C': [4], 'W': [3]}
digit_polynomial = poly_mod5(ppow([F(1), F(-4), F(-4)], 2))
endpoint_digits = [mod5(sum(legendre_transform(j))) for j in range(5)]
assert digit_polynomial == endpoint_digits == [1, 2, 3, 2, 1]

print(json.dumps({'status': 'PASS', 'examples': examples,
                  'symbolic_disk': {'prime': 5, 'index_disk': '5Z_5', 'precision': 1,
                                    'cutoffs_compared': [5, 10],
                                    'derivative_polynomials_mod5': {str(key): poly_mod5(value) for key, value in derivatives.items()},
                                    'auxiliary_contractions_mod5': auxiliary_disk,
                                    'legendre_digit_polynomial': digit_polynomial},
                  'scope': 'Two exact integer examples and a bounded symbolic disk check; independent review remains required.'}, indent=2))