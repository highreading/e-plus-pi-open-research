import math, json, hashlib
from fractions import Fraction

p = 3
precision = 6
modulus = p ** precision

def valuation(a):
    a = abs(a)
    if a == 0:
        return 10**9
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v

facts = [math.factorial(k) for k in range(64)]

def multiply_linear(poly, constant, linear):
    out = [0] * (len(poly) + 1)
    for i, a in enumerate(poly):
        out[i] = (out[i] + constant * a) % modulus
        out[i + 1] = (out[i + 1] + linear * a) % modulus
    return out

# F[j][m] is (3Y+j) falling m, divided by its exact Gauss content.
F = {}
normalized_content = {}
for j in range(3):
    F[j] = [[1]]
    normalized_content[j] = [0]
    for i in range(40):
        constant = j - i
        if constant % 3 == 0:
            F[j].append(multiply_linear(F[j][-1], constant // 3, 1))
            normalized_content[j].append(normalized_content[j][-1] + 1)
        else:
            F[j].append(multiply_linear(F[j][-1], constant, 3))
            normalized_content[j].append(normalized_content[j][-1])
        assert any(a % 3 for a in F[j][-1])


def truncated_series(j, r, cutoff):
    out = [0] * (2 * cutoff + r + 1)
    for c in range((cutoff - 1) // 2 + 1):
        for b in range(cutoff - 2 * c):
            t, s = b + 2 * c, b + c
            vb, vc = valuation(facts[b]), valuation(facts[c])
            v = normalized_content[j][t + r] + normalized_content[j][s] - vb - vc
            assert v >= 0
            if v >= precision:
                continue
            denominator_unit = (pow(2, c, modulus) * (facts[b] // 3**vb) * (facts[c] // 3**vc)) % modulus
            scalar = ((-1 if b % 2 else 1) * 3**v * pow(denominator_unit, -1, modulus)) % modulus
            for a_index, a in enumerate(F[j][t + r]):
                if a == 0:
                    continue
                for d_index, d in enumerate(F[j][s]):
                    out[a_index + d_index] = (out[a_index + d_index] + scalar * a * d) % modulus
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def falling_integer(n, m):
    if m > n:
        return 0
    return facts[n] // facts[n - m]


def exact_defining_sum(n, r):
    total = Fraction(0)
    for c in range(n // 2 + 1):
        for b in range(n - 2 * c + 1):
            t, s = b + 2 * c, b + c
            numerator = (-1)**b * falling_integer(n, t + r) * falling_integer(n, s)
            total += Fraction(numerator, 2**c * facts[b] * facts[c])
    assert total.denominator == 1
    return total.numerator


def evaluate(poly, y):
    result = 0
    for a in reversed(poly):
        result = (result * y + a) % modulus
    return result

coefficients = {}
mod3_constants = []
checks = 0
for j in range(3):
    constants = []
    for r in range(4):
        a = truncated_series(j, r, 30)
        b = truncated_series(j, r, 36)
        assert a == b, (j, r, 'cutoff mismatch')
        assert all(x % 3 == 0 for x in a[1:]), (j, r, 'nonconstant reduction')
        constants.append(a[0] % 3)
        for y in range(13):
            n = 3*y + j
            actual = exact_defining_sum(n, r) % modulus
            assert evaluate(a, y) == actual, (j, r, n)
            checks += 1
        coefficients[str((j, r))] = a
    mod3_constants.append(constants)

assert mod3_constants == [[1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 2, 0]]
assert 10 - valuation(facts[10]) == 6
sharp_term_valuation = 2 * normalized_content[2][29] - valuation(facts[29])
assert sharp_term_valuation == 5
encoded = json.dumps(coefficients, sort_keys=True, separators=(',', ':')).encode()
print(json.dumps({'status': 'passed', 'modulus': modulus, 'cutoffs_compared': [30, 36], 'coefficientwise_series_comparisons': 12, 'exact_integer_evaluation_checks': checks, 'derivative_reductions_mod3_by_shift': mod3_constants, 'discarded_term_cutoff29_counterexample_valuation': sharp_term_valuation, 'coefficient_arrays_sha256': hashlib.sha256(encoded).hexdigest(), 'scope': 'Author computation; independent review remains pending. No actual denominator bound.'}, indent=2))