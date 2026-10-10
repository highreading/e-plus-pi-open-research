import math
import json


def vp_integer(n, p):
    n = abs(n)
    if n == 0:
        return math.inf
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp_factorial(k, p):
    total = 0
    while k:
        k //= p
        total += k
    return total


def digit_sum(k, p):
    total = 0
    while k:
        k, digit = divmod(k, p)
        total += digit
    return total


rows = []
for p in (3, 5, 7, 11):
    for d in range(1, 129):
        K = max(1, ((p - 1) * (d - 1) + p - 3) // (p - 2))
        for k in range(0, 4 * K + 20):
            f = k - vp_factorial(k, p)
            assert (p - 1) * f == (p - 2) * k + digit_sum(k, p)
            if k >= K:
                assert f >= d
        # The proved uniform bound excludes every k >= K.
        # Exhaustive search below K therefore finds the exact cutoff
        # supplied by f_p alone, not an optimal cutoff for actual terms.
        exact_bound_cutoff = 1 + max(k for k in range(K) if k - vp_factorial(k, p) < d)
        if p == 3 and d <= 12:
            rows.append({'d': d, 'uniform_K': K, 'exact_K_from_bound': exact_bound_cutoff})


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def falling_on_disk(a, p, length):
    out = [1]
    for j in range(length):
        out = multiply(out, [a - j, p])
    return out


# Independently test the summands newly omitted when the mod-9
# cutoff is lowered from b+2c < 9 to b+2c < 6.
# T_(b,c,r)(X)=(-1)^b (X)_(b+2c+r)(X)_(b+c)/(2^c b! c!).
checked = 0
minimum = math.inf
for a in range(3):
    for r in range(3):
        for m in (6, 7, 8):
            for c in range(m // 2 + 1):
                b = m - 2 * c
                numerator = multiply(falling_on_disk(a, 3, m + r), falling_on_disk(a, 3, b + c))
                denominator = 2**c * math.factorial(b) * math.factorial(c)
                gauss_valuation = min(vp_integer(x, 3) for x in numerator) - vp_integer(denominator, 3)
                assert gauss_valuation >= 2, (a, r, b, c, gauss_valuation)
                minimum = min(minimum, gauss_valuation)
                checked += 1

print(json.dumps({'finite_bound_checks_passed': True, 'primes': [3, 5, 7, 11], 'precision_range': [1, 128], 'ternary_cutoff_table': rows, 'newly_omitted_summands_checked': checked, 'minimum_coefficient_valuation': minimum, 'scope': 'Auxiliary truncation only; no denominator-growth conclusion.'}, indent=2))