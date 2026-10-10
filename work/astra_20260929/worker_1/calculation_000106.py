from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib
import json
import time

started = time.process_time()
root = Path('[private local path removed]')
path = root / 'work/astra_review_registry/candidates/worker4-b2-five-adic-residue-one-exact-denominator-v1.md'
raw = path.read_bytes()
expected = 'cbf4838dfb7531fb17145053d4180baeed90ce8d9214d4f57197b1022eb790d3'
whole_hash = hashlib.sha256(raw).hexdigest()
assert whole_hash == '6c5e172e3b2fba497bd42e6c0fca3a780dba94980ee581fe8933a8b71b666c43'
start = raw.index(b'UNVERIFIED CANDIDATE. Author: worker_4.')
tail = raw[start:]
variants = {tail, tail.rstrip(b'\n'), tail.rstrip(b'\n') + b'\n'}
matches = [x for x in variants if hashlib.sha256(x).hexdigest() == expected]
assert len(matches) == 1
provenance = {'payload_sha256': expected, 'payload_offset': start, 'payload_bytes': len(matches[0]), 'whole_file_sha256': whole_hash}

indices = (6, 11, 26, 126)
limit = 2 * max(indices) + 4
facts = [1]
eints = [1]
for j in range(1, limit + 1):
    facts.append(facts[-1] * j)
    eints.append(j * eints[-1] + 1)
E = [F(eints[j], facts[j]) for j in range(limit + 1)]
moments = []
real, imag = 1, 0
for j in range(limit):
    real, imag = real - imag, real + imag
    moments.append(F(2 * imag, (1 << j) * (j + 1)))

def valuation(x):
    x = F(x)
    if not x:
        return None
    def integer_v(a):
        a = abs(a)
        result = 0
        while a % 5 == 0:
            a //= 5
            result += 1
        return result
    return integer_v(x.numerator) - integer_v(x.denominator)

def at_least(x, bound):
    return not x or valuation(x) >= bound

def residue(x):
    x = F(x)
    assert x.denominator % 5
    return (x.numerator % 5) * pow(x.denominator % 5, -1, 5) % 5

def trinomial_power(c0, c1, c2, m):
    result = [1]
    for unused in range(m):
        nxt = [0] * (len(result) + 2)
        for j, coefficient in enumerate(result):
            nxt[j] += c0 * coefficient
            nxt[j + 1] += c1 * coefficient
            nxt[j + 2] += c2 * coefficient
        result = nxt
    return result

def legendre_coefficients(m):
    power = trinomial_power(1, -2, 2, m)
    return [comb(m + d, d) * power[m + d] for d in range(m + 1)], power

def h_derivatives(m):
    power = trinomial_power(2, -2, 1, m)
    result = []
    for derivative in range(3):
        numerator = sum(power[j] * (facts[m] // facts[m - derivative - j]) for j in range(m - derivative + 1))
        quotient, remainder = divmod(numerator, 1 << m)
        assert remainder == 0
        result.append(quotient)
    return result

def exponential_contraction(coefficients, n, j=0):
    return sum((coefficient * E[n + d - j] for d, coefficient in enumerate(coefficients)), F(0))

def moment_contraction(coefficients):
    tail_sum = 0
    result = F(0)
    for d in range(len(coefficients) - 1, 0, -1):
        tail_sum += coefficients[d]
        result += tail_sum * moments[d - 1]
    return result

def a_endpoint(beta, q_coefficients, n):
    cumulative = [F(0)]
    for j in range(n):
        cumulative.append(cumulative[-1] + moments[j])
    return -sum((beta[j] * E[n - j] for j in range(3)), F(0)) - sum((q_coefficients[d] * cumulative[d] for d in range(1, n + 1)), F(0))

def verify_raw(n, p_coefficients, u_coefficients, a, b, D, X):
    G = F((-1) ** n * (1 << (2 * n + 3)), n + 1)
    gamma = F((-1) ** n, 4 * (n + 1) ** 3 * facts[n] ** 4)
    alpha = [sum((F(coefficient, facts[n + d + 1 - j]) for d, coefficient in enumerate(u_coefficients)), F(0)) for j in range(3)]
    tau = [(a * exponential_contraction(u_coefficients, n, j) - b * exponential_contraction(p_coefficients, n, j)) / G for j in range(3)]
    second = [1 + x for x in tau]
    beta = [alpha[1] * second[2] - alpha[2] * second[1], alpha[2] * second[0] - alpha[0] * second[2], alpha[0] * second[1] - alpha[1] * second[0]]
    kernel_numerator = [[0] * (n + 1) for unused in range(n + 1)]
    padded_p = p_coefficients + [0]
    for upper in range(1, n + 2):
        for lower in range(upper):
            coefficient = u_coefficients[upper] * padded_p[lower] - padded_p[upper] * u_coefficients[lower]
            for shift in range(upper - lower):
                kernel_numerator[upper - 1 - shift][lower + shift] += coefficient
    assert all(kernel_numerator[i][j] == kernel_numerator[j][i] for i in range(n + 1) for j in range(n + 1))
    contracted = [sum((beta[j] / facts[n + d + 1 - j] for j in range(3)), F(0)) for d in range(n + 1)]
    q_coefficients = [-sum((kernel_numerator[i][d] * contracted[d] for d in range(n + 1)), F(0)) / G for i in range(n + 1)]
    assert sum(beta) == gamma * D
    assert sum(q_coefficients) == gamma * D
    assert a_endpoint(beta, q_coefficients, n) == gamma * X
    for r_index in range(n + 2):
        coefficient = sum((q_coefficients[d] * moments[r_index + d] for d in range(n + 1)), F(0))
        coefficient += sum((beta[j] / facts[n + r_index + 1 - j] for j in range(3)), F(0))
        assert coefficient == 0
    return {'n': n, 'tail_coefficients_checked': n + 2, 'order_at_least': 2 * n + 3, 'endpoint_scaling_passed': True, 'raw_A_valuation': valuation(gamma * X), 'raw_B_valuation': valuation(gamma * D)}

def independently_solve_normalized(n):
    dimension = n + 4
    matrix = []
    for r_index in range(n + 2):
        row = [F(1, facts[n + r_index + 1 - j]) for j in range(3)]
        row += [moments[r_index + d] for d in range(n + 1)]
        matrix.append(row + [F(0)])
    matrix.append([F(1)] * 3 + [F(-1)] * (n + 1) + [F(0)])
    matrix.append([F(1)] * 3 + [F(0)] * (n + 1) + [F(1)])
    for column in range(dimension):
        pivot = next(row for row in range(column, dimension) if matrix[row][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        divisor = matrix[column][column]
        matrix[column] = [x / divisor for x in matrix[column]]
        for row in range(dimension):
            if row == column or not matrix[row][column]:
                continue
            multiplier = matrix[row][column]
            for j in range(column, dimension + 1):
                matrix[row][j] -= multiplier * matrix[column][j]
    solution = [matrix[j][-1] for j in range(dimension)]
    beta, q_coefficients = solution[:3], solution[3:]
    assert sum(beta) == sum(q_coefficients) == 1
    return a_endpoint(beta, q_coefficients, n)

rows = []
raw_checks = []
lower_term_checks = 0
system_check = None
for n in indices:
    p_coefficients, p_power = legendre_coefficients(n)
    u_coefficients, u_power = legendre_coefficients(n + 1)
    a, b = sum(p_coefficients), sum(u_coefficients)
    h, hp, hpp = h_derivatives(n)
    eta, etap, etapp = h_derivatives(n + 1)
    J = n * h + hp
    Jnext = (n + 1) * eta + etap
    Knext = (n + 1) * n * eta + 2 * (n + 1) * etap + etapp
    S = Jnext * Jnext - eta * Knext
    scalar_c = (Jnext - eta) * J - (Knext - Jnext) * h
    W = Jnext * J - Knext * h
    k = (n + 1) ** 2
    f = F(1 << n, facts[n] ** 2)
    tp = exponential_contraction(p_coefficients, n)
    tu = exponential_contraction(u_coefficients, n)
    wp = moment_contraction(p_coefficients)
    wu = moment_contraction(u_coefficients)
    D = k * b * scalar_c - 2 * a * S
    X = 2 * (wp + tp) * S - k * (wu + tu) * scalar_c - 2 * f * eta * W
    r = valuation(facts[n])
    L, power_of_five = 0, 5
    while power_of_five <= n:
        L += 1
        power_of_five *= 5
    assert [residue(z) for z in (h, hp, hpp)] == [0, 1, 0]
    assert [residue(z) for z in (eta, etap, etapp)] == [1, 3, 2]
    assert [residue(z) for z in (S, scalar_c, W, k)] == [4, 4, 0, 4]
    assert residue(a) != 0 and residue(b) == 4 * residue(a) % 5
    assert residue(D) == residue(a) and valuation(D) == 0
    p_terms = [F(facts[n] * p_power[n + d] * eints[n + d], (1 << n) * facts[d]) for d in range(n + 1)]
    u_terms = [F(facts[n] * (n + 1 + d) * u_power[n + 1 + d] * eints[n + d], (1 << n) * (n + 1) * facts[d]) for d in range(n + 2)]
    assert sum(p_terms) == tp / f and sum(u_terms) == tu / f
    for d in range(n - 1):
        assert at_least(p_terms[d], 1) and at_least(u_terms[d], 1)
        lower_term_checks += 2
    assert p_terms[-2:] == [-n * n * eints[2 * n - 1], eints[2 * n]]
    assert u_terms[-3:] == [2 * n * n * (n + 1) * eints[2 * n - 1], -2 * (2 * n + 1) * eints[2 * n], F(4 * eints[2 * n + 1], n + 1)]
    assert [residue(z) for z in u_terms[-3:]] == [3, 0, 2]
    assert at_least(wp, -L) and at_least(wu, -L)
    assert at_least(wp / f, 2 * r - L) and at_least(wu / f, 2 * r - L)
    assert 2 * r - L >= 1
    assert [residue(tp / f), residue(tu / f), residue(X / f)] == [3, 0, 4]
    assert valuation(X) == -2 * r
    reduced = X / D
    assert valuation(reduced.denominator) == 2 * r
    if n in (11, 26):
        raw_checks.append(verify_raw(n, p_coefficients, u_coefficients, a, b, D, X))
    if n == 11:
        solved = independently_solve_normalized(n)
        assert solved == reduced
        system_check = {'n': n, 'unknowns': n + 4, 'exact_ratio_agreement': True, 'denominator_valuation': valuation(solved.denominator)}
    rows.append({'n': n, 'v5_n_minus_one': valuation(n - 1), 'r': r, 'L': L, 'v5_D': valuation(D), 'v5_X': valuation(X), 'v5_q': valuation(reduced.denominator), 'a_mod5': residue(a), 'normalized_contractions_mod5': [residue(tp / f), residue(tu / f), residue(X / f)], 'normalized_moment_valuations': [valuation(wp / f), valuation(wu / f)], 'denominator_digits': len(str(reduced.denominator))})

print(json.dumps({'provenance': provenance, 'endpoint_checks': rows, 'lower_summands_checked': lower_term_checks, 'raw_reconstruction_checks': raw_checks, 'independent_system_check': system_check, 'cpu_seconds': round(time.process_time() - started, 3)}, indent=2))