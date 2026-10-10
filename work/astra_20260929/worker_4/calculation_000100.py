from fractions import Fraction as F
from math import comb
import json

indices = [9, 14, 19, 24, 29, 49, 124]
unit_modulus = 625
max_n = max(indices)
fac = [1]
for j in range(1, 2 * max_n + 5):
    fac.append(fac[-1] * j)
E = []
partial = F(0)
for j in range(len(fac)):
    partial += F(1, fac[j])
    E.append(partial)

# Exact Gaussian-integer evaluation of the original rational moments.
mu = []
ga, gb = 1, 0
for j in range(2 * max_n + 3):
    ga, gb = ga - gb, ga + gb
    mu.append(F(2 * gb, 2**j * (j + 1)))

def v5(value):
    value = F(value)
    if not value:
        return None
    numerator, denominator = abs(value.numerator), value.denominator
    result = 0
    while numerator % 5 == 0:
        numerator //= 5
        result += 1
    while denominator % 5 == 0:
        denominator //= 5
        result -= 1
    return result

def unit_residue(value):
    value = F(value)
    if not value:
        return None
    numerator, denominator = value.numerator, value.denominator
    while numerator % 5 == 0:
        numerator //= 5
    while denominator % 5 == 0:
        denominator //= 5
    return numerator * pow(denominator, -1, unit_modulus) % unit_modulus

def trinomial_power(base, exponent):
    result = [1]
    for unused in range(exponent):
        updated = [0] * (len(result) + 2)
        for i, coefficient in enumerate(result):
            for j, factor in enumerate(base):
                updated[i + j] += coefficient * factor
        result = updated
    return result

def legendre_coefficients(m):
    # Rodrigues: L_m[d] = binom(m+d,m) [t^(m+d)](1-2t+2t^2)^m.
    u = trinomial_power([1, -2, 2], m)
    return [comb(m + d, m) * u[m + d] for d in range(m + 1)]

def auxiliary_derivatives(m):
    # Independent expansion of H_m, using (2-2s+s^2)^m to keep integers.
    u = trinomial_power([2, -2, 1], m)
    result = []
    for derivative in range(3):
        total = sum(u[a] * (fac[m] // fac[m - derivative - a])
                    for a in range(m - derivative + 1))
        value = F(total, 2**m)
        assert value.denominator == 1
        result.append(value.numerator)
    return result

def moment_quotient(poly):
    # Coefficient of t^j in (poly(t)-poly(1))/(t-1) is sum_{d>j} poly[d].
    tail = 0
    result = F(0)
    for j in range(len(poly) - 2, -1, -1):
        tail += poly[j + 1]
        result += tail * mu[j]
    return result

def cross(left, right):
    return [left[1] * right[2] - left[2] * right[1],
            left[2] * right[0] - left[0] * right[2],
            left[0] * right[1] - left[1] * right[0]]

def coefficient_content(poly):
    return min((v5(c) for c in poly if c), default=None)

def degree(poly):
    return max((j for j, c in enumerate(poly) if c), default=-1)

def reconstruct_polynomials(n, P, U, beta, G, gamma, X, D):
    # Divide U(t)P(s)-P(t)U(s) by t-s directly in Z[t,s].
    padded_P = P + [0]
    quotient = [None] * (n + 1)
    carry = [0] * (n + 2)
    for i in range(n, -1, -1):
        row = [U[i + 1] * padded_P[j] - padded_P[i + 1] * U[j]
               + (carry[j - 1] if j else 0)
               for j in range(n + 2)]
        assert row[-1] == 0, ('kernel degree', n, i)
        quotient[i] = row[:-1]
        carry = row
    remainder = [U[0] * padded_P[j] - padded_P[0] * U[j]
                 + (carry[j - 1] if j else 0)
                 for j in range(n + 2)]
    assert not any(remainder), ('kernel division', n)
    assert all(quotient[i][j] == quotient[j][i]
               for i in range(n + 1) for j in range(n + 1))

    functional = [sum(beta[j] / fac[n + s + 1 - j] for j in range(3))
                  for s in range(n + 1)]
    Qraw = [-sum(quotient[i][s] * functional[s] for s in range(n + 1)) / G
            for i in range(n + 1)]
    Craw = Qraw[::-1]

    def other_remainder_coefficient(t):
        exponential = sum(beta[j] / fac[t - j] for j in range(min(2, t) + 1))
        moment = sum(Craw[j] * mu[t - j - 1]
                     for j in range(min(n, t - 1) + 1))
        return exponential + moment

    Araw = [-other_remainder_coefficient(t) for t in range(n + 1)]
    remainder_coefficients = [other_remainder_coefficient(t)
                              + (Araw[t] if t <= n else F(0))
                              for t in range(2 * n + 3)]
    Aend, Bend, Cend = sum(Araw), sum(beta), sum(Craw)
    checks = {
        'all_order_conditions': not any(remainder_coefficients),
        'A_endpoint_scaling': Aend == gamma * X,
        'B_endpoint_scaling': Bend == gamma * D,
        'C_endpoint_scaling': Cend == gamma * D,
        'matched_endpoints': Bend == Cend
    }
    return {
        'n': n,
        'gamma': str(gamma),
        'actual_degrees_A_B_C': [degree(Araw), degree(beta), degree(Craw)],
        'vanishing_coefficient_degrees_checked': [0, 2 * n + 2],
        'raw_A_endpoint': str(Aend),
        'raw_B_endpoint': str(Bend),
        'raw_C_endpoint': str(Cend),
        'v5_raw_endpoints_A_B_C': [v5(Aend), v5(Bend), v5(Cend)],
        'v5_coefficient_contents_A_B_C': [coefficient_content(Araw),
                                         coefficient_content(beta),
                                         coefficient_content(Craw)],
        'checks': checks
    }

rows = []
scalar_checks = []
full_reconstructions = []
counterexamples = []

for n in indices:
    P, U = legendre_coefficients(n), legendre_coefficients(n + 1)
    a, b = sum(P), sum(U)
    h, hp, hpp = auxiliary_derivatives(n)
    eta, etap, etapp = auxiliary_derivatives(n + 1)
    Jn = n * h + hp
    Jnext = (n + 1) * eta + etap
    Knext = n * (n + 1) * eta + 2 * (n + 1) * etap + etapp
    S = Jnext**2 - eta * Knext
    Cscalar = (Jnext - eta) * Jn - (Knext - Jnext) * h
    W = Jnext * Jn - Knext * h
    k = (n + 1)**2
    f = F(2**n, fac[n]**2)
    g = F(2**(n + 1), fac[n + 1]**2)
    G = F((-1)**n * 2**(2 * n + 3), n + 1)
    gamma = F((-1)**n, 4 * (n + 1)**3 * fac[n]**4)
    wP, wU = moment_quotient(P), moment_quotient(U)
    TP = [sum(c * E[n + d - j] for d, c in enumerate(P)) for j in range(3)]
    TU = [sum(c * E[n + d - j] for d, c in enumerate(U)) for j in range(3)]
    Pstar, Ustar = wP + TP[0], wU + TU[0]
    D = k * b * Cscalar - 2 * a * S
    X = 2 * Pstar * S - k * Ustar * Cscalar - 2 * f * eta * W
    N = X / f
    Z = N / (n + 1)

    # Reconstruct both scalar endpoints from the raw cross product.
    alpha = [sum(F(c, fac[n + d + 1 - j]) for d, c in enumerate(U))
             for j in range(3)]
    rho = [sum(F(c, fac[n + d + 1 - j]) for d, c in enumerate(P))
           for j in range(3)]
    tau = [(a * TU[j] - b * TP[j]) / G for j in range(3)]
    beta = cross(alpha, [1 + t for t in tau])
    xj = [(wP * TU[j] - wU * TP[j]) / G for j in range(3)]
    Bdet = sum(beta)
    Adet = sum(beta[j] * xj[j] for j in range(3))

    r, s = v5(fac[n]), v5(n + 1)
    dv, xv, nv, zv = v5(D), v5(X), v5(N), v5(Z)
    ratio = X / D if D else None
    qv = v5(ratio.denominator) if ratio is not None else None
    expected_qv = None if not D else (0 if not X else max(0, 2 * r + dv - s - zv))
    expected_raw_Av = None if not X else -6 * r - 2 * s + zv
    expected_raw_Bv = None if not D else -4 * r - 3 * s + dv
    checks = {
        'factorial_rows_match_auxiliary_definition':
            alpha == [g * eta, g * Jnext, g * Knext]
            and rho[1:] == [f * h, f * Jn],
        'moment_wronskian': a * wU - b * wP == G,
        'common_gamma_identity': gamma == g * f / (G * k),
        'raw_cross_product_constraints':
            sum(beta[j] * alpha[j] for j in range(3)) == 0
            and sum(beta[j] * (1 + tau[j]) for j in range(3)) == 0,
        'scalar_B_endpoint_scaling': Bdet == gamma * D,
        'scalar_A_endpoint_scaling': Adet == gamma * X,
        'raw_endpoint_valuation_scaling':
            v5(Adet) == expected_raw_Av and v5(Bdet) == expected_raw_Bv,
        'actual_reduced_denominator_identity': qv == expected_qv
    }
    row = {
        'n': n, 'r': r, 's': s,
        'v5_D': dv, 'v5_X_over_f': nv, 'v5_q_n': qv,
        'v5_Z': zv, 'unit_Z_mod_625': unit_residue(Z),
        'unit_D_mod_625': unit_residue(D),
        'v5_gamma': v5(gamma),
        'v5_raw_A_endpoint': v5(Adet),
        'v5_raw_B_endpoint': v5(Bdet),
        'D_nonzero': bool(D), 'X_nonzero': bool(X),
        'prediction_D_valuation_equals_s': dv == s,
        'prediction_Z_in_5Z5': not Z or zv >= 1
    }
    rows.append(row)
    scalar_checks.append({'n': n, 'checks': checks})
    if dv != s:
        counterexamples.append({'n': n, 'prediction': 'v5(D)=s', 'actual': dv, 's': s})
    if Z and zv < 1:
        counterexamples.append({'n': n, 'prediction': 'v5(Z)>=1', 'actual': zv})
    if n in (9, 24):
        full_reconstructions.append(reconstruct_polynomials(n, P, U, beta, G, gamma, X, D))

all_checks_pass = all(all(item['checks'].values()) for item in scalar_checks + full_reconstructions)
report = {
    'scope': 'Exactly seven scalar reconstructions; full raw polynomials only at n=9 and n=24.',
    'valuation_zero_convention': 'null denotes v5(0)=infinity; q_n is undefined when D=0.',
    'unit_residue_definition': 'unit_Z_mod_625 is 5^(-v5(Z))*Z modulo 625; similarly for D.',
    'table': rows,
    'scalar_checks': scalar_checks,
    'full_raw_reconstructions': full_reconstructions,
    'prediction_counterexamples': counterexamples,
    'all_normalization_and_order_checks_pass': all_checks_pass,
    'limitation': 'Finite exact calculations only; no uniform bound on v5(Z) follows.'
}
print(json.dumps(report, indent=2))
assert all_checks_pass, 'At least one exact normalization or polynomial order check failed.'