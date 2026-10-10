from fractions import Fraction as F
from math import factorial, comb
import json

# Exactly three endpoint reconstructions: boundary, opposite parity, and 25 | n-2.
indices = (7, 12, 27)
max_n = max(indices)
facts = [factorial(j) for j in range(2 * max_n + 4)]

# Original Rodrigues polynomials, computed with integer coefficient arithmetic.
powers = [[1]]
legendre = [[1]]
for m in range(1, max_n + 2):
    previous = powers[-1]
    current = [0] * (len(previous) + 2)
    for j, coefficient in enumerate(previous):
        current[j] += coefficient
        current[j + 1] -= 2 * coefficient
        current[j + 2] += 2 * coefficient
    powers.append(current)
    legendre.append([comb(m + d, m) * current[m + d] for d in range(m + 1)])

# Exact moments from powers of 1+i; no floating point or complex approximation.
mu = []
real_part, imag_part = 1, 0
for j in range(2 * max_n + 2):
    real_part, imag_part = real_part - imag_part, real_part + imag_part
    mu.append(F(2 * imag_part, 2**j * (j + 1)))
moment_prefix = [F(0)]
for value in mu:
    moment_prefix.append(moment_prefix[-1] + value)

E = [F(1)]
e_integer = [1]
for j in range(1, len(facts)):
    E.append(E[-1] + F(1, facts[j]))
    e_integer.append(j * e_integer[-1] + 1)
    assert facts[j] * E[j] == e_integer[j]

def v5(value):
    value = F(value)
    if value == 0:
        return float('inf')
    numerator = abs(value.numerator)
    denominator = value.denominator
    answer = 0
    while numerator % 5 == 0:
        numerator //= 5
        answer += 1
    while denominator % 5 == 0:
        denominator //= 5
        answer -= 1
    return answer

def residue(value):
    value = F(value)
    assert value.denominator % 5 != 0
    return (value.numerator % 5) * pow(value.denominator % 5, -1, 5) % 5

def report_valuation(value):
    answer = v5(value)
    return 'infinity' if answer == float('inf') else answer

def h_derivatives(m):
    answer = []
    for order in range(3):
        value = sum((F(facts[m] * powers[m][j], 2**j * facts[m - j - order])
                     for j in range(m - order + 1)), F(0))
        assert value.denominator == 1
        answer.append(value.numerator)
    return answer

assert h_derivatives(2) == [1, -2, 2]
assert h_derivatives(3) == [-5, 12, -12]
results = []
for n in indices:
    P, U = legendre[n], legendre[n + 1]
    a, b = sum(P), sum(U)
    k = (n + 1)**2
    f = F(2**n, facts[n]**2)
    G = F((-1)**n * 2**(2*n + 3), n + 1)

    def ell(poly, j):
        return sum((F(coefficient, facts[n + d + 1 - j])
                    for d, coefficient in enumerate(poly)), F(0))

    def T(poly, j):
        return sum((coefficient * E[n + d - j]
                    for d, coefficient in enumerate(poly)), F(0))

    def w(poly):
        return sum((coefficient * moment_prefix[d]
                    for d, coefficient in enumerate(poly) if d), F(0))

    wP, wU = w(P), w(U)
    assert a * wU - b * wP == G
    TP = [T(P, j) for j in range(3)]
    TU = [T(U, j) for j in range(3)]
    hn, hn1, hn2 = h_derivatives(n)
    eta, hm1, hm2 = h_derivatives(n + 1)
    Jn = n * hn + hn1
    Jm = (n + 1) * eta + hm1
    Km = n * (n + 1) * eta + 2 * (n + 1) * hm1 + hm2
    S = Jm**2 - eta * Km
    Cscalar = (Jm - eta) * Jn - (Km - Jm) * hn
    W = Jm * Jn - Km * hn
    D = k * b * Cscalar - 2 * a * S
    X = 2 * (wP + TP[0]) * S - k * (wU + TU[0]) * Cscalar - 2 * f * eta * W

    assert [residue(t) for t in (hn, Jn, eta, Jm, Km)] == [1, 0, 0, 2, 0]
    assert [residue(t) for t in (S, Cscalar, W, k)] == [4, 2, 0, 4]
    assert residue(a) != 0 and residue(F(b, a)) == 4
    assert residue(F(D, a)) == 4

    p_terms = [F(facts[n], 2**n * facts[d]) * powers[n][n + d] * e_integer[n + d]
               for d in range(n + 1)]
    u_terms = [F(facts[n] * (n + 1 + d), 2**n * (n + 1) * facts[d])
               * powers[n + 1][n + 1 + d] * e_integer[n + d]
               for d in range(n + 2)]
    assert sum(p_terms, F(0)) == TP[0] / f
    assert sum(u_terms, F(0)) == TU[0] / f
    assert all(v5(term) >= 1 for term in p_terms[:n - 2])
    assert all(v5(term) >= 1 for term in u_terms[:n - 2])
    p_kept = [residue(term) for term in p_terms[n - 2:]]
    u_kept = [residue(term) for term in u_terms[n - 2:]]
    assert p_kept == [0, 1, 0]
    assert u_kept == [0, 4, 0, 3]
    assert [residue(TP[0] / f), residue(TU[0] / f), residue(X / f)] == [1, 2, 2]

    r = v5(facts[n])
    logarithm = 0
    quotient = n
    while quotient >= 5:
        quotient //= 5
        logarithm += 1
    assert 2 * r - logarithm >= 1
    assert v5(wP / f) >= 2 * r - logarithm
    assert v5(wU / f) >= 2 * r - logarithm
    assert v5(D) == 0 and v5(X) == -2 * r

    # Reconstruct all raw coefficients without using the scalar D or X.
    alpha = [ell(U, j) for j in range(3)]
    tau = [(a * TU[j] - b * TP[j]) / G for j in range(3)]
    second_row = [1 + value for value in tau]
    beta = [alpha[1] * second_row[2] - alpha[2] * second_row[1],
            alpha[2] * second_row[0] - alpha[0] * second_row[2],
            alpha[0] * second_row[1] - alpha[1] * second_row[0]]

    # Orthogonal expansion of the reproducing kernel:
    # K_n(t,s) = sum_m L_m(t)L_m(s) / integral(L_m^2).
    q_coefficients = [F(0) for _ in range(n + 1)]
    for m in range(n + 1):
        poly = legendre[m]
        contraction = sum((beta[j] * ell(poly, j) for j in range(3)), F(0))
        inverse_norm = F((-1)**m * (2*m + 1), 2**(2*m + 1))
        multiplier = -inverse_norm * contraction
        for d, coefficient in enumerate(poly):
            q_coefficients[d] += multiplier * coefficient
    Craw = list(reversed(q_coefficients))
    Braw = beta

    complete_series = []
    for degree in range(2 * n + 3):
        value = sum((Braw[j] / facts[degree - j]
                     for j in range(min(2, degree) + 1)), F(0))
        value += sum((Craw[d] * mu[degree - d - 1]
                      for d in range(min(n, degree - 1) + 1)), F(0))
        complete_series.append(value)
    Araw = [-complete_series[d] for d in range(n + 1)]
    assert all(value == 0 for value in complete_series[n + 1:])

    Aendpoint = sum(Araw, F(0))
    Bendpoint = sum(Braw, F(0))
    Cendpoint = sum(Craw, F(0))
    gamma = F((-1)**n, 4 * (n + 1)**3 * facts[n]**4)
    assert Bendpoint == Cendpoint == gamma * D
    assert Aendpoint == gamma * X
    actual_ratio = Aendpoint / Bendpoint
    assert actual_ratio == X / D
    assert v5(actual_ratio.denominator) == 2 * r
    assert [v5(Aendpoint), v5(Bendpoint)] == [-6 * r, -4 * r]

    results.append({
        'n': n,
        'v5_n_minus_2': v5(n - 2),
        'v5_factorial': r,
        'v5_D_X_q': [v5(D), v5(X), v5(actual_ratio.denominator)],
        'D_over_a_mod5': residue(F(D, a)),
        'P_U_N_mod5': [residue(TP[0] / f), residue(TU[0] / f), residue(X / f)],
        'retained_P_term_residues': p_kept,
        'retained_U_term_residues': u_kept,
        'normalized_moment_lower_bound': 2 * r - logarithm,
        'normalized_moment_valuations': [report_valuation(wP / f), report_valuation(wU / f)],
        'raw_endpoint_valuations': [v5(Aendpoint), v5(Bendpoint)],
        'full_order_checked_through_degree': 2 * n + 2,
        'endpoint_scaling_verified': True,
        'ratio_numerator': str(actual_ratio.numerator),
        'ratio_denominator': str(actual_ratio.denominator)
    })
print(json.dumps({'status': 'all exact assertions passed', 'reconstruction_count': len(results), 'results': results}, indent=2))