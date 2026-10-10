from fractions import Fraction as F
from math import factorial
import json

p = 1534325864618923739320962894053
q = 261835956661996866283563171456
N = 30
e_lo = sum((F(1, factorial(k)) for k in range(N + 1)), F(0))
e_hi = e_lo + F(N + 2, (N + 1) * factorial(N + 1))

def atan_bounds(d, terms):
    assert d > 1 and terms % 2 == 0
    lo = sum((F((-1)**k, (2*k + 1) * d**(2*k + 1)) for k in range(terms)), F(0))
    hi = lo + F(1, (2*terms + 1) * d**(2*terms + 1))
    return lo, hi

a_lo, a_hi = atan_bounds(5, 30)
b_lo, b_hi = atan_bounds(239, 8)
pi_lo = 16*a_lo - 4*b_hi
pi_hi = 16*a_hi - 4*b_lo
s_lo, s_hi = e_lo + pi_lo, e_hi + pi_hi
r = F(p, q)
err_lo, err_hi = s_lo - r, s_hi - r
form_lo, form_hi = q*s_lo - p, q*s_hi - p
assert err_lo < err_hi
assert form_lo == q*err_lo and form_hi == q*err_hi

def outward_interval(lo, hi, scale):
    lower = (lo*scale).numerator // (lo*scale).denominator
    upper = -((-((hi*scale).numerator)) // (hi*scale).denominator)
    assert F(lower, scale) <= lo < hi <= F(upper, scale)
    return {'lower_numerator': str(lower), 'upper_numerator': str(upper), 'common_denominator': str(scale)}

sign = -1 if err_hi < 0 else (1 if err_lo > 0 else 0)
print(json.dumps({
    'method': 'Exact rational series bounds with proved remainder estimates',
    'index': 9,
    'target_enclosure': outward_interval(s_lo, s_hi, 10**30),
    'signed_error_enclosure': outward_interval(err_lo, err_hi, 10**30),
    'integer_form_enclosure': outward_interval(form_lo, form_hi, 10**3),
    'certified_error_sign': sign,
    'agrees_with_eventual_sign_at_this_index': sign == (-1)**9,
    'target_interval_width_less_than_1e_minus_33': s_hi-s_lo < F(1, 10**33),
    'scope': 'Finite analytic author check; endpoint identification awaits independent review.'
}, indent=2))