import json
from decimal import Decimal, localcontext

def digit_sum(n, p):
    total = 0
    while n:
        n, digit = divmod(n, p)
        total += digit
    return total

def factorial_valuation(n, p):
    total = 0
    power = p
    while power <= n:
        total += n // power
        power *= p
    return total

limit = 20000
class_counts = {0: 0, 5: 0, 10: 0}
class_minima = {}
for n in range(1, limit + 1):
    s3 = digit_sum(n, 3)
    s5 = digit_sum(n, 5)
    v3 = factorial_valuation(n, 3)
    v5 = factorial_valuation(n, 5)
    assert 2*v3 == n-s3
    assert 4*v5 == n-s5
    # Square the digit factor to keep this check entirely integral.
    digit_factor_squared = 3**(2*s3) * 5**s5
    assert digit_factor_squared <= (225*n**4)**2
    if n % 5 == 0:
        assert s5 == digit_sum(n//5, 5)
        assert digit_factor_squared <= (9*n**4)**2
        residue = n % 15
        assert residue in class_counts
        class_counts[residue] += 1
        class_minima.setdefault(residue, n)
        if residue == 0:
            assert n % 3 == 0 and n >= 3
        elif residue == 5:
            assert n % 3 == 2 and n >= 5
        else:
            assert n % 3 == 1 and n >= 4

with localcontext() as ctx:
    ctx.prec = 70
    rho = Decimal(1) + Decimal(2).sqrt()
    exponential_base = Decimal(3)*Decimal(5).sqrt()/(rho*rho)
    margin = exponential_base.ln()
    base_text = str(exponential_base)
    margin_text = str(margin)

print(json.dumps({
    'checked_n': [1, limit],
    'legendre_identity_checks': 2*limit,
    'general_digit_bound_checks': limit,
    'five_multiple_sharpened_bound_checks': limit//5,
    'progression_class_counts': class_counts,
    'progression_class_minima': class_minima,
    'exponential_base_approximation': base_text,
    'logarithmic_margin_approximation': margin_text,
    'scope': 'Finite bookkeeping checks only. Positivity and the universal bounds are proved in the note; pending endpoint congruences were not tested or approved.'
}, indent=2))