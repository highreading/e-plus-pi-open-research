import json

N, D, M, c, precision = 1, 5, 3, 1, 640
prefix = [-1, 1, 2, -2, 0, 0]
modulus = 1 << precision


def evaluate(coefficients, x, mod):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % mod
    return value


def valuation(nonzero):
    assert nonzero != 0
    return (nonzero & -nonzero).bit_length() - 1


# Include only increments visible at the selected precision.
n, j = 1, 1
visible_indices = []
while True:
    depth = n * n + j + N
    if depth >= precision:
        break
    visible_indices.append((n, depth))
    n += M * (1 << depth)
    j += 1
beta = n % modulus
assert visible_indices == [(1, 3), (25, 628)]
assert beta == 25 + 3 * (1 << 628)
assert beta % 2 == 1
assert evaluate(prefix, beta, 1 << N) == 0

# Construct the correction digits using modular residuals.
coefficients = list(prefix)
residual = evaluate(prefix, beta, modulus)
power = pow(beta, D + 1, modulus)
digits = []
for t in range(precision - N):
    exponent = N + t
    assert residual % (1 << exponent) == 0
    digit = (residual >> exponent) & 1
    coefficient = digit * (1 << exponent)
    assert len(coefficients) == D + 1 + t
    coefficients.append(coefficient)
    digits.append(digit)
    residual = (residual + coefficient * power) % modulus
    assert residual % (1 << (exponent + 1)) == 0
    power = power * beta % modulus

assert residual == 0
assert evaluate(coefficients, beta, modulus) == 0
assert coefficients[:D + 1] == prefix
assert all(a % (1 << N) == 0 for a in coefficients[D + 1:])
for degree, coefficient in enumerate(coefficients[D + 1:], D + 1):
    bound = 1 << (N + degree - D - 1)
    assert coefficient in (0, bound)
    assert abs(coefficient) <= bound

last_degree = len(coefficients) - 1
for cutoff in range(D, last_degree + 1):
    retained_tail_valuation = min(
        (valuation(a) for a in coefficients[cutoff + 1:] if a),
        default=precision,
    )
    assert retained_tail_valuation >= N + cutoff - D

# Independently evaluate the polynomial at the two ordinary integers.
approximation_checks = []
for integer, expected_depth in visible_indices:
    difference_depth = valuation((beta - integer) % modulus)
    value_depth = valuation(evaluate(coefficients, integer, modulus))
    assert difference_depth == value_depth == expected_depth
    assert integer % M == c
    approximation_checks.append({
        'integer': integer,
        'expected_depth': expected_depth,
        'difference_depth': difference_depth,
        'polynomial_value_depth': value_depth,
    })

# Synthetic division independently checks the unit quotient modulo 2^K.
quotient = [0] * last_degree
quotient[-1] = coefficients[-1] % modulus
for degree in range(last_degree - 1, 0, -1):
    quotient[degree - 1] = (
        coefficients[degree] + beta * quotient[degree]
    ) % modulus
assert (coefficients[0] + beta * quotient[0]) % modulus == 0
assert quotient[0] % 2 == 1
assert all(a % 2 == 0 for a in quotient[1:])
for degree in range(len(coefficients)):
    reconstructed = 0
    if degree >= 1:
        reconstructed += quotient[degree - 1]
    if degree < last_degree:
        reconstructed -= beta * quotient[degree]
    assert (reconstructed - coefficients[degree]) % modulus == 0

derivative = [degree * coefficients[degree]
              for degree in range(1, len(coefficients))]
assert derivative[0] % 2 == 1
assert all(a % 2 == 0 for a in derivative[1:])

# Recover the root by Newton lifting, independently of correction digits.
root, bits = 1, 1
while bits < precision:
    next_bits = min(2 * bits, precision)
    next_modulus = 1 << next_bits
    value = evaluate(coefficients, root, next_modulus)
    slope = evaluate(derivative, root, next_modulus)
    assert slope % 2 == 1
    root = (root - value * pow(slope, -1, next_modulus)) % next_modulus
    assert evaluate(coefficients, root, next_modulus) == 0
    bits = next_bits
assert root == beta

# Exhaustively check uniqueness at a small modulus.
small_modulus = 1024
small_coefficients = [a % small_modulus for a in coefficients]
while small_coefficients and small_coefficients[-1] == 0:
    small_coefficients.pop()
small_roots = [x for x in range(small_modulus)
               if evaluate(small_coefficients, x, small_modulus) == 0]
assert small_roots == [beta % small_modulus]

print(json.dumps({
    'status': 'finite author self-check only',
    'parameters': {'N': N, 'D': D, 'M': M, 'c': c},
    'precision_bits': precision,
    'retained_degree': last_degree,
    'correction_digits': len(digits),
    'nonzero_correction_digits': sum(digits),
    'exact_prefix_preserved_through_degree': D,
    'retained_tail_bounds_checked_for_cutoffs': [D, last_degree],
    'approximation_checks': approximation_checks,
    'quotient_congruent_to_one_modulo_two': True,
    'newton_root_matches': True,
    'all_roots_modulo_1024': small_roots,
    'all_assertions_passed': True,
    'scope': 'Finite modular validation; the infinite theorem still requires independent review.'
}, indent=2))