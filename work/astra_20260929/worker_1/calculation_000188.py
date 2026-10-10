import json

def digit_sum(n, b):
    total = 0
    while n:
        n, digit = divmod(n, b)
        total += digit
    return total

def is_base_power(n, b):
    if n < 1:
        return False
    while n % b == 0:
        n //= b
    return n == 1

def factorial_valuation(n, p):
    total = 0
    while n:
        n //= p
        total += n
    return total

integer_checks = 0
minimum_checks = 0
extremizer_checks = 0
for b in range(2, 12):
    first = {}
    for n in range(4097):
        s = digit_sum(n, b)
        first.setdefault(s, n)
        k, r = divmod(s, b - 1)
        minimum = (r + 1) * b**k - 1
        assert minimum <= n
        assert digit_sum(minimum, b) == s
        left = b**s
        right = (n + 1)**(b - 1)
        assert left <= right
        assert (left == right) == is_base_power(n + 1, b)
        j, a = divmod(n, b)
        suffix_right = b**a * (j + 1)**(b - 1)
        assert left <= suffix_right
        assert (left == suffix_right) == is_base_power(j + 1, b)
        integer_checks += 1
    for s, observed_minimum in first.items():
        k, r = divmod(s, b - 1)
        assert observed_minimum == (r + 1) * b**k - 1
        minimum_checks += 1
    for k in range(33):
        for a in range(b):
            n = b**(k + 1) - b + a
            j = n // b
            assert b**digit_sum(n, b) == b**a * (j + 1)**(b - 1)
            extremizer_checks += 1

indices = sorted(set(range(6, 1002, 5)) | {5**k - 4 for k in range(2, 6)} | {26, 2186})
for n in indices:
    assert n >= 6 and n % 5 == 1
    exponent_3 = 2 * factorial_valuation(n, 3)
    exponent_5 = 2 * factorial_valuation(n, 5)
    assert exponent_3 == n - digit_sum(n, 3)
    assert 2 * exponent_5 == n - digit_sum(n, 5)
    forced_divisor = 3**exponent_3 * 5**exponent_5
    # Squaring removes every radical; both sides of the original bound are positive.
    assert forced_divisor**2 * (n + 1)**4 * (n + 4)**4 >= 125 * 45**n

print(json.dumps({
    'integer_digit_checks': integer_checks,
    'exact_minimum_checks': minimum_checks,
    'structured_equality_checks': extremizer_checks,
    'conditional_denominator_checks': len(indices),
    'largest_denominator_test_index': max(indices),
    'all_assertions_passed': True
}, sort_keys=True))