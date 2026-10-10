from fractions import Fraction as F
from math import factorial, gcd
import json

p, q = 9252196933, 1579037328
assert gcd(p, q) == 1
K, M5, M239 = 30, 24, 7

def atan_bounds(x, M):
    partial = sum(((-1)**j * x**(2*j+1) / (2*j+1) for j in range(M+1)), F(0))
    next_term = x**(2*M+3) / (2*M+3)
    return (partial-next_term, partial) if M % 2 == 0 else (partial, partial+next_term)

x, y = F(1,5), F(1,239)
t2 = 2*x/(1-x*x)
t4 = 2*t2/(1-t2*t2)
assert t4 == F(120,119)
assert (t4-y)/(1+t4*y) == 1
assert 4*(x-x**3/3)-y > 0
assert 4*x < 1

e_lo = sum((F(1,factorial(j)) for j in range(K+1)), F(0))
e_hi = e_lo + F(K+2, (K+1)*factorial(K+1))
a_lo, a_hi = atan_bounds(x, M5)
b_lo, b_hi = atan_bounds(y, M239)
pi_lo, pi_hi = 16*a_lo-4*b_hi, 16*a_hi-4*b_lo
target_lo, target_hi = e_lo+pi_lo, e_hi+pi_hi
error_lo, error_hi = target_lo-F(p,q), target_hi-F(p,q)
form_lo, form_hi = q*target_lo-p, q*target_hi-p
assert error_lo > 0
assert 0 < form_hi-form_lo < F(1,10**24)

def exact_decimal(j, places):
    sign = '-' if j < 0 else ''
    j = abs(j)
    scale = 10**places
    return sign + str(j//scale) + '.' + str(j%scale).zfill(places)

def enclosure(lo, hi, places):
    scale = 10**places
    lower = lo.numerator*scale//lo.denominator
    upper = -((-hi.numerator*scale)//hi.denominator)
    return {'strict_lower': exact_decimal(lower,places), 'strict_upper': exact_decimal(upper,places), 'endpoints_are_exact_decimals': True}

print(json.dumps({'scope':'Supplementary author check; independent registry review remains pending', 'n':4, 'p':p, 'q':q, 'series_indices':{'e_K':K,'atan_1_over_5_M':M5,'atan_1_over_239_M':M239}, 'machin_tangent_identity_checked':True, 'error_e_plus_pi_minus_p_over_q':enclosure(error_lo,error_hi,24), 'linear_form_q_times_e_plus_pi_minus_p':enclosure(form_lo,form_hi,12), 'linear_form_is_positive':True, 'unrounded_linear_form_interval_width_below_10_to_minus_24':True}, indent=2))