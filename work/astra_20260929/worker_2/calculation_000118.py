import json
from math import gcd, isqrt
from fractions import Fraction

def factorial_valuation(n, prime):
    result = 0
    while n:
        n //= prime
        result += n
    return result

def valuation(value, prime):
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result

def digit_sum(n, base):
    result = 0
    while n:
        n, digit = divmod(n, base)
        result += digit
    return result

def pell_pair(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = 3*a + 4*b, 2*a + 3*b
    return a, b

rows = []
for n in (1, 3, 5, 10, 20, 40, 80, 160):
    f3 = factorial_valuation(n, 3)
    f5 = factorial_valuation(n, 5)
    s3 = digit_sum(n, 3)
    s5 = digit_sum(n, 5)
    q = 3**(2*f3) * 7**n
    a, b = pell_pair(n)
    assert a*a - 2*b*b == 1
    square = 2*(q*b)**2
    root_floor = isqrt(square)
    assert root_floor**2 < square < (root_floor + 1)**2
    # Exact floor of x = q*(a-b*sqrt(2)); x is irrational.
    x_floor = q*a - root_floor - 1
    assert x_floor > 0
    k = 1 + 21*((x_floor + 20)//21)
    numerator = -k
    assert k % 21 == 1
    assert 1 <= k - x_floor <= 21
    # Since x_floor < x < x_floor+1, this proves 0 < k-x < 21.
    assert gcd(numerator, q) == 1
    assert valuation(q, 3) == 2*f3
    assert valuation(q, 5) == 0
    assert valuation(q, 7) == n
    assert 2*f3 == n-s3
    assert 4*f5 == n-s5
    loss = 2*f5
    residual_factor = 7**n
    assert q == 3**(2*f3) * 5**(2*f5-loss) * residual_factor
    assert q == 21**n // 3**s3
    rows.append({
        'n': n,
        'v3_q': 2*f3,
        'v5_q': 0,
        'five_adic_loss': loss,
        'absolute_linear_form': str(k),
        'relative_error_upper_bound': str(Fraction(21, x_floor))
    })

print(json.dumps({
    'status': 'all exact checks passed',
    'cases': len(rows),
    'scope': 'constructed approximants to zero with C=1; no endpoint-family computation',
    'rows': rows
}, indent=2))