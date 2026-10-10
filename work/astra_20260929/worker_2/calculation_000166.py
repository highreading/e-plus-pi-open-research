from fractions import Fraction as F
from math import factorial, comb, gcd
import json

n = 4
m = n + 1

def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out

def poly_power(p, exponent):
    out = [F(1)]
    for _ in range(exponent):
        out = mul(out, p)
    return out

def integral_coefficients(p):
    assert all(F(x).denominator == 1 for x in p)
    return [int(x) for x in p]

def rodrigues(j):
    coeff = poly_power([F(1), F(-2), F(2)], j)
    return integral_coefficients([
        coeff[j + d] * F(factorial(j + d), factorial(j) * factorial(d))
        for d in range(j + 1)
    ])

def auxiliary(j):
    coeff = poly_power([F(1), F(-1), F(1, 2)], j)
    hp = [F(0)] * (j + 1)
    for t in range(j + 1):
        hp[j - t] = coeff[t] * F(factorial(j), factorial(j - t))
    hp = integral_coefficients(hp)
    h = sum(hp)
    d1 = sum(d * x for d, x in enumerate(hp))
    d2 = sum(d * (d - 1) * x for d, x in enumerate(hp))
    J = j * h + d1
    K = j * (j - 1) * h + 2 * j * d1 + d2
    return hp, h, d1, d2, J, K

def moment(d):
    return sum((F(2 * comb(d, 2 * k) * (-1)**k,
                  2**d * (2 * k + 1))
                for k in range(d // 2 + 1)), F(0))

def endpoint_quotient(p):
    quotient = [sum(p[j + 1:]) for j in range(len(p) - 1)]
    rebuilt = mul([F(-1), F(1)], quotient)
    rebuilt[0] += sum(p)
    assert rebuilt == p
    return quotient

def moment_contraction(p):
    quotient = endpoint_quotient(p)
    return sum((x * moment(d) for d, x in enumerate(quotient)), F(0))

P, U = rodrigues(n), rodrigues(m)
a, b = sum(P), sum(U)
Hn, hn, Hn1, Hn2, Jn, Kn = auxiliary(n)
Hm, hm, Hm1, Hm2, Jm, Km = auxiliary(m)
S = Jm**2 - hm * Km
C = (Jm - hm) * Jn - (Km - Jm) * hn
W = Jm * Jn - Km * hn
f = F(2**n, factorial(n)**2)
k = m**2
g = 2 * f / k
G = F((-1)**n * 2**(2*n + 3), m)

E = [F(1)]
for j in range(1, 2*n + 2):
    E.append(E[-1] + F(1, factorial(j)))

def T(p, j=0):
    return sum((x * E[n + d - j] for d, x in enumerate(p)), F(0))

def ell(p, j):
    return sum((F(x, factorial(n + d + 1 - j))
                for d, x in enumerate(p)), F(0))

wP, wU = moment_contraction(P), moment_contraction(U)
TP, TU = T(P), T(U)
Pstar, Ustar = wP + TP, wU + TU
D = k * b * C - 2 * a * S
exp_parts = [2 * TP * S, -k * TU * C, -2 * f * hm * W]
moment_parts = [2 * wP * S, -k * wU * C]
XE = sum(exp_parts, F(0))
XM = sum(moment_parts, F(0))
X = XE + XM
ZE, ZM = XE / (f*m), XM / (f*m)
Z = X / (f*m)
ratio = X / D
q = ratio.denominator

# Independently reconstruct the raw scalar endpoints from the published cross product.
raw_a = [ell(U, j) for j in range(3)]
raw_t = [(a*T(U, j) - b*T(P, j)) / G for j in range(3)]
raw_x = [(wP*T(U, j) - wU*T(P, j)) / G for j in range(3)]
raw_rhs = [1 + t for t in raw_t]
beta = [raw_a[1]*raw_rhs[2] - raw_a[2]*raw_rhs[1],
        raw_a[2]*raw_rhs[0] - raw_a[0]*raw_rhs[2],
        raw_a[0]*raw_rhs[1] - raw_a[1]*raw_rhs[0]]
Yraw = sum(beta, F(0))
Xraw = sum((beta[j]*raw_x[j] for j in range(3)), F(0))
gamma = F((-1)**n, 4*m**3*factorial(n)**4)
assert gamma == g*f/(G*k)
assert raw_a == [g*hm, g*Jm, g*Km]
assert ell(P, 1) == f*hn and ell(P, 2) == f*Jn
assert Xraw == gamma*X and Yraw == gamma*D
assert Xraw/Yraw == ratio
assert a*wU - b*wP == G
V = b*Pstar - a*Ustar
assert V == b*TP - a*TU - G
assert b*X + Ustar*D == 2*(V*S - b*f*hm*W)
assert a*X + Pstar*D == k*V*C - 2*a*f*hm*W

# Compare fresh reconstruction with the hand derivation and the saved n=4 ratio.
assert P == [136, -800, 1920, -2240, 1120]
assert U == [-592, 4320, -13440, 22400, -20160, 8064]
assert (hn, Hn1, Hn2, Jn, Kn) == (45, -92, 108, 88, -88)
assert (hm, Hm1, Hm2, Jm, Km) == (-494, 955, -1180, -1515, -1510)
assert (S, C, W) == (1549285, -90073, -65370)
assert (wP, wU, TP, TU) == (F(1280, 3), F(27904, 15), F(1477, 4), F(28991, 18))
assert (Pstar, Ustar) == (F(9551, 12), F(312379, 90))
assert f == F(1, 36) and D == -1754485920
assert XE == F(42922505650, 9) and XM == 5511051520
assert X == F(92521969330, 9)
assert (ZE, ZM, Z) == (34338004520, 39679570944, 74017575464)
assert ratio == F(-9252196933, 1579037328)
assert gcd(abs(ratio.numerator), ratio.denominator) == 1
reduction_gcd = gcd(abs(X.numerator), abs(X.denominator*D))
assert reduction_gcd == 10
assert q == abs(X.denominator*D) // reduction_gcd

# Each certificate expresses the rational as 5^v times an explicit unit.
def strip_five(integer):
    assert integer != 0
    exponent = 0
    while integer % 5 == 0:
        integer //= 5
        exponent += 1
    return exponent, integer

def certificate(value):
    value = F(value)
    assert value != 0
    nv, un = strip_five(value.numerator)
    dv, ud = strip_five(value.denominator)
    valuation = nv - dv
    assert value == F(5)**valuation * F(un, ud)
    assert un % 5 and ud % 5
    return {'value': str(value), 'v5': valuation,
            'unit_numerator': un, 'unit_denominator': ud,
            'unit_mod5': (un % 5) * pow(ud % 5, -1, 5) % 5}

core = {'f': f, 'D': D, 'X_exponential': XE, 'X_moment': XM,
        'X': X, 'X_over_f': X/f, 'Z_exponential': ZE,
        'Z_moment': ZM, 'Z': Z, 'ratio_X_over_D': ratio, 'q': q}
certificates = {name: certificate(value) for name, value in core.items()}
assert [certificates[name]['v5'] for name in ['X', 'D', 'f', 'Z', 'q']] == [1, 1, 0, 0, 0]
assert certificates['Z_exponential']['v5'] == 1
assert certificates['Z_moment']['v5'] == 0
assert certificates['q']['v5'] == max(0, certificates['D']['v5'] - certificates['X']['v5'])
assert [int(x) % 25 for x in (ZE, ZM, Z)] == [20, 19, 14]

result = {
    'scope': 'Exact n=4 author computation; independent registry review pending.',
    'all_assertions_passed': True,
    'polynomials_ascending': {'P': P, 'U': U, 'H4': Hn, 'H5': Hm},
    'auxiliary_states': {'n4': [hn, Hn1, Hn2, Jn, Kn], 'm5': [hm, Hm1, Hm2, Jm, Km]},
    'integer_contractions': {'a': a, 'b': b, 'S': S, 'C': C, 'W': W},
    'moments_degree_0_through_4': [str(moment(d)) for d in range(5)],
    'endpoint_quotients_ascending': {'P': endpoint_quotient(P), 'U': endpoint_quotient(U)},
    'scalar_contractions': {name: str(value) for name, value in
        [('wP', wP), ('wU', wU), ('TP', TP), ('TU', TU), ('Pstar', Pstar), ('Ustar', Ustar)]},
    'exponential_terms_P_U_auxiliary': [certificate(x) for x in exp_parts],
    'moment_terms_P_U': [certificate(x) for x in moment_parts],
    'normalized_exponential_terms': [str(x/(f*m)) for x in exp_parts],
    'normalized_moment_terms': [str(x/(f*m)) for x in moment_parts],
    'valuation_certificates': certificates,
    'normalized_residues_mod25': {'exponential': int(ZE) % 25, 'moment': int(ZM) % 25, 'complete': int(Z) % 25},
    'reduction_certificate': {'numerator_X': X.numerator, 'denominator_X': X.denominator,
        'signed_unreduced_denominator': X.denominator*D, 'gcd': reduction_gcd,
        'reduced_numerator': ratio.numerator, 'positive_reduced_denominator': q},
    'raw_endpoint_check': {'gamma': str(gamma), 'Xraw': str(Xraw), 'Yraw': str(Yraw),
        'common_scaling_and_both_chart_identities': True}
}
print(json.dumps(result, indent=2, sort_keys=True))