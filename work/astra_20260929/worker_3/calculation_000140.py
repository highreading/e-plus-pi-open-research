from fractions import Fraction as F
from math import factorial, comb
import json

n = 9
m = n + 1

def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def poly_power(a, exponent):
    out = [F(1)]
    for _ in range(exponent):
        out = poly_mul(out, a)
    return out

def rodrigues(j):
    base = poly_power([1, -2, 2], j)
    coefficients = [comb(j+d, j)*base[j+d] for d in range(j+1)]
    assert all(x.denominator == 1 for x in coefficients)
    return coefficients, base

def falling(j, k):
    return factorial(j)//factorial(j-k) if 0 <= k <= j else 0

def auxiliary(j):
    coefficients = poly_power([1, -1, F(1, 2)], j)
    derivatives = []
    for h in range(3):
        direct = sum((F(factorial(j), factorial(j-h-t))*coefficients[t]
                      for t in range(j-h+1)), F(0))
        expanded = F(0)
        for u in range(j+1):
            for w in range((j-u)//2+1):
                expanded += F((-1)**u * falling(j, u+2*w+h) * falling(j, u+w),
                              2**w * factorial(u) * factorial(w))
        assert direct == expanded
        assert direct.denominator == 1
        derivatives.append(direct)
    h0, h1, h2 = derivatives
    J = j*h0 + h1
    K = j*(j-1)*h0 + 2*j*h1 + h2
    return derivatives, J, K, coefficients

def moment(k):
    integral_expansion = F(2, 2**k) * sum(
        (F((-1)**j * comb(k, 2*j), 2*j+1) for j in range(k//2+1)), F(0))
    real, imag = 1, 0
    for _ in range(k+1):
        real, imag = real-imag, real+imag
    endpoint_expression = F(2*imag, 2**k*(k+1))
    assert integral_expansion == endpoint_expression
    return integral_expansion

def moment_contraction(coefficients):
    degree = len(coefficients)-1
    quotient = [sum(coefficients[k+1:], F(0)) for k in range(degree)]
    reconstructed = poly_mul(quotient, [-1, 1])
    expected = list(coefficients)
    expected[0] -= sum(coefficients, F(0))
    assert reconstructed == expected
    return sum((quotient[k]*moment(k) for k in range(degree)), F(0))

P, base_n = rodrigues(n)
U, base_m = rodrigues(m)
a, b = sum(P, F(0)), sum(U, F(0))
wP, wU = moment_contraction(P), moment_contraction(U)
E = []
e = []
running = F(0)
for j in range(n+m+1):
    running += F(1, factorial(j))
    E.append(running)
    e.append(factorial(j)*running)
    assert e[-1].denominator == 1
    if j:
        assert e[j] == j*e[j-1] + 1
TP = sum((coefficient*E[n+d] for d, coefficient in enumerate(P)), F(0))
TU = sum((coefficient*E[n+d] for d, coefficient in enumerate(U)), F(0))
f = F(2**n, factorial(n)**2)

hn_derivatives, Jn, Kn, cn = auxiliary(n)
hm_derivatives, Jm, Km, cm = auxiliary(m)
hn, hm = hn_derivatives[0], hm_derivatives[0]
S = Jm**2 - hm*Km
C = (Jm-hm)*Jn - (Km-Jm)*hn
W = Jm*Jn - Km*hn
D = m*m*b*C - 2*a*S
Pstar, Ustar = wP+TP, wU+TU
X = 2*Pstar*S - m*m*Ustar*C - 2*f*hm*W
Z = X/(f*m)

# Check both exponential contractions using different coefficient formulas.
TP_reversed = sum((falling(n, t)*cn[t]*e[2*n-t] for t in range(n+1)), F(0))
assert TP/f == TP_reversed
U_terms = [F(1, 2**(m-1))*F(factorial(m-1), factorial(d))
           *(m+d)*base_m[m+d]*e[m-1+d] for d in range(m+1)]
assert m*TU/f == sum(U_terms, F(0))
assert U_terms[-1] == 4*e[2*m-1]

components = {
    'exponential_P': 2*(TP/f)*(S/m),
    'exponential_U': -(m*TU/f)*C,
    'auxiliary_correction': -2*hm*(W/m),
    'moment_P': 2*(wP/f)*(S/m),
    'moment_U': -(m*wU/f)*C,
}
Z_exponential = sum((components[key] for key in
    ['exponential_P', 'exponential_U', 'auxiliary_correction']), F(0))
Z_moment = components['moment_P'] + components['moment_U']
assert sum(components.values(), F(0)) == Z
assert Z_exponential + Z_moment == Z
assert D != 0
approximant = -X/D
q = approximant.denominator

# All valuation and modular calculations below use reduced exact fractions.
def integer_v5(value):
    value = abs(value)
    assert value != 0
    result = 0
    while value % 5 == 0:
        value //= 5
        result += 1
    return result

def v5(value):
    value = F(value)
    if not value:
        return None
    return integer_v5(value.numerator) - integer_v5(value.denominator)

def residue(value, modulus):
    value = F(value)
    assert value.denominator % 5 != 0
    return (value.numerator * pow(value.denominator, -1, modulus)) % modulus

def describe(value):
    value = F(value)
    valuation = v5(value)
    result = {'fraction': str(value), 'v5': valuation}
    if value.denominator % 5:
        result['mod_15625'] = residue(value, 15625)
    if value:
        normalized = value/(F(5)**valuation)
        result['unit_mod_625'] = residue(normalized, 625)
    return result

scalars = {
    'f': f, 'a': a, 'b': b,
    'h_n': hn, 'Hprime_n': hn_derivatives[1], 'Hsecond_n': hn_derivatives[2],
    'h_m': hm, 'Hprime_m': hm_derivatives[1], 'Hsecond_m': hm_derivatives[2],
    'J_n': Jn, 'K_n': Kn, 'J_m': Jm, 'K_m': Km,
    'S': S, 'C': C, 'W': W,
    'T_P': TP, 'T_U': TU, 'w_P': wP, 'w_U': wU,
    'P_star': Pstar, 'U_star': Ustar,
    'T_P_over_f': TP/f, 'm_T_U_over_f': m*TU/f,
    'U_boundary_term': U_terms[-1],
    'Z_exponential': Z_exponential, 'Z_moment': Z_moment,
    'D': D, 'X': X, 'Z': Z, 'Z_over_25': Z/25,
    'approximant': approximant, 'reduced_denominator': F(q),
}
quotient = Z/25
certificate = {
    'Z_over_25_numerator': str(quotient.numerator),
    'Z_over_25_denominator': str(quotient.denominator),
    'numerator_mod_5': quotient.numerator % 5,
    'denominator_mod_5': quotient.denominator % 5,
    'is_five_adic_unit': bool(quotient) and quotient.numerator % 5 != 0 and quotient.denominator % 5 != 0,
    'reported_v5_Z_equals_2': v5(Z) == 2,
    'reported_unit_mod_625_equals_17': residue(quotient, 625) == 17 if quotient.denominator % 5 else False,
    'reported_v5_q_equals_0': v5(q) == 0,
}
print(json.dumps({
    'index': n,
    'scalars': {key: describe(value) for key, value in scalars.items()},
    'complete_Z_components': {key: describe(value) for key, value in components.items()},
    'certificate': certificate,
    'identity_checks': 'All exact reconstruction assertions passed.',
}, indent=2))