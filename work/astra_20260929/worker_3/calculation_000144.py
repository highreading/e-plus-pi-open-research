from fractions import Fraction
from math import gcd
import json

# Preserved outputs of the completed n=9 endpoint reconstruction.
x_num = 30686517292378474786419257881060
x_den = 321489
D = -16288952758072398513390080
f = Fraction(1, 257191200)
X = Fraction(x_num, x_den)
assert gcd(x_num, x_den) == 1

# Reduce -X/D by integer arithmetic before comparing with Fraction.
raw_num = x_num
raw_den = -x_den * D
common = gcd(raw_num, raw_den)
p = raw_num // common
q = raw_den // common
assert q > 0
assert p * raw_den == q * raw_num

# Extended Euclidean algorithm supplies a standalone coprimality witness.
r0, r1 = p, q
s0, s1 = 1, 0
t0, t1 = 0, 1
while r1:
    quotient = r0 // r1
    r0, r1 = r1, r0 - quotient * r1
    s0, s1 = s1, s0 - quotient * s1
    t0, t1 = t1, t0 - quotient * t1
assert r0 == 1
assert s0 * p + t0 * q == 1
assert Fraction(p, q) == -X / D
assert p == 1534325864618923739320962894053
assert q == 261835956661996866283563171456

Z = X / (10 * f)
unit = Z / 25
assert Z == 2454921383390277982913540630484800
assert unit == 98196855335611119316541625219392

def v5_integer(value):
    value = abs(value)
    assert value
    exponent = 0
    while value % 5 == 0:
        value //= 5
        exponent += 1
    return exponent

def v5(value):
    value = Fraction(value)
    return v5_integer(value.numerator) - v5_integer(value.denominator)

def residue(value, modulus):
    value = Fraction(value)
    assert gcd(value.denominator, modulus) == 1
    return value.numerator * pow(value.denominator, -1, modulus) % modulus

assert v5(Z) == 2
assert residue(unit, 5) == 2
assert residue(unit, 625) == 17
assert v5(D) == 1 and v5(X) == 1 and v5(f) == -2
assert v5(q) == 0 and q % 5 == 1
assert v5(q) == max(0, v5(D) - v5(X))

print(json.dumps({
    'index': 9,
    'raw_approximant_numerator': str(raw_num),
    'raw_approximant_denominator': str(raw_den),
    'integer_gcd': str(common),
    'reduced_numerator': str(p),
    'positive_reduced_denominator': str(q),
    'bezout_coefficient_p': str(s0),
    'bezout_coefficient_q': str(t0),
    'bezout_value': str(s0*p+t0*q),
    'Z': str(Z),
    'Z_over_25': str(unit),
    'Z_mod_125': residue(Z, 125),
    'leading_unit_mod_5': residue(unit, 5),
    'leading_unit_mod_625': residue(unit, 625),
    'valuations': {'f': v5(f), 'D': v5(D), 'X': v5(X), 'Z': v5(Z), 'q': v5(q)},
    'q_mod_5': q % 5,
    'checks': 'All exact normalization, integer reduction, Bezout, and valuation assertions passed.'
}, indent=2))