from fractions import Fraction
import json


def digit_sum(n, p):
    total = 0
    while n:
        n, r = divmod(n, p)
        total += r
    return total


def factorial_valuation(n, p):
    total = 0
    while n:
        n //= p
        total += n
    return total


def check_new_bound(n):
    assert n >= 6 and n % 5 == 1
    m = (n - 1) // 5
    a = digit_sum(n, 3)
    b = digit_sum(n, 5)
    c = digit_sum(m, 5)
    assert b == c + 1
    assert a % 2 == n % 2
    assert c % 2 == m % 2
    T = (n + 1)**2 * (n + 4)**2
    F_squared = 3**(2*a) * 5**b
    if n % 2:
        assert 4 * 3**a <= 3 * (n + 1)**2
        assert 5**c <= (m + 1)**4
        lhs, rhs = 2000 * F_squared, 9 * T**2
    else:
        assert 3**a <= (n + 1)**2
        assert 256 * 5**c <= 125 * (m + 1)**4
        lhs, rhs = 256 * F_squared, T**2
    assert lhs < rhs, (n, a, b, c)
    return Fraction(lhs, rhs)


indices = set(range(6, 10002, 5))
structured = set()
for k in range(1, 129):
    for n in (3**k - 1, 2 * 3**k - 1, 5**k - 4, 4 * 5**k - 4):
        if n >= 6 and n % 5 == 1:
            structured.add(n)
indices.update(structured)
maxima = {}
for n in sorted(indices):
    ratio = check_new_bound(n)
    parity = 'odd' if n % 2 else 'even'
    if parity not in maxima or ratio > maxima[parity][1]:
        maxima[parity] = (n, ratio)

forced_denominator_checks = 0
for n in range(6, 1007, 5):
    a = digit_sum(n, 3)
    b = digit_sum(n, 5)
    q0 = 3**(2 * factorial_valuation(n, 3)) * 5**(2 * factorial_valuation(n, 5))
    T = (n + 1)**2 * (n + 4)**2
    assert q0**2 * 3**(2*a) * 5**b == 45**n
    if n % 2:
        assert 9 * q0**2 * T**2 > 2000 * 45**n
    else:
        assert q0**2 * T**2 > 256 * 45**n
    forced_denominator_checks += 1

print(json.dumps({
    'status': 'PASS',
    'new_digit_bound_checks': len(indices),
    'structured_indices': len(structured),
    'largest_index_decimal_digits': len(str(max(indices))),
    'conditional_forced_denominator_checks': forced_denominator_checks,
    'largest_denominator_test_index': 1006,
    'largest_tested_squared_ratios': {
        parity: {'n': n, 'ratio': str(ratio)}
        for parity, (n, ratio) in maxima.items()
    },
    'scope': 'Finite corroboration of the new parity refinement; endpoint valuation hypotheses were not tested.'
}, sort_keys=True))