"""Main-only full-interval derivative certificate for the fixed exterior arc.

The archived leaves supply rational domains, never accepted numerical signs.
All derivative, branch and overlap enclosures are independently reconstructed.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import re

BASE = Path(__file__).resolve().parent
module_path = BASE / 'fixed_interval_main.py'
assert hashlib.sha256(module_path.read_bytes()).hexdigest() == 'b48f4ed029b5fe334b5861b52702cebef9f9e945ada99a08e97dc3d13e52a276'
spec = importlib.util.spec_from_file_location('main_fixed_interval', module_path)
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
I, C, SCALE = iv.I, iv.C, iv.SCALE
source = Path('work/session_20260913/exterior_phase_monotonicity_certificate.json')
raw = source.read_bytes()
SOURCE_SHA = '9a242800023b7f173553d2d829bb52374bdc1014803f3ceb0025a128c4e9bc69'
assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA
old = json.loads(raw)
assert old['leaf_count'] == len(old['leaves']) == 128
pi = iv.pi_interval()
assert pi.lo > 3 * SCALE and pi.hi < 4 * SCALE


def rational(q):
    q = Fraction(q)
    return I.rational(q.numerator, q.denominator)


def square(value):
    lower = 0 if value.lo <= 0 <= value.hi else min(value.lo ** 2, value.hi ** 2)
    return I(lower // SCALE, iv.ceildiv(max(value.lo ** 2, value.hi ** 2), SCALE))


def divide(a, b):
    denominator = square(b.real) + square(b.imag)
    assert denominator.lo > 0
    return C((a.real * b.real + a.imag * b.imag) / denominator,
             (a.imag * b.real - a.real * b.imag) / denominator)


def power(value, n):
    result = C(1)
    for _ in range(n):
        result = result * value
    return result


def sine_point(angle):
    assert angle.lo >= 0 and angle.hi < 4 * SCALE
    term, result = angle, angle
    for j in range(1, 64):
        term = -term * (angle * angle) / ((2 * j) * (2 * j + 1))
        result = result + term
    # Degree128 has a zero sine coefficient; Lagrange remainder has order129.
    return result.widen(I.rational(4 ** 129, math.factorial(129)))


def trigonometric_range(lo, hi):
    left, right = rational(lo), rational(hi)
    assert 0 <= left.lo <= right.hi < pi.lo
    lc, rc = iv.cosine_small(left), iv.cosine_small(right)
    ls, rs = sine_point(left), sine_point(right)
    cosine = I(rc.lo, lc.hi)  # cosine decreases throughout [0,pi].
    if 2 * right.hi <= pi.lo:
        sine_hi = rs.hi
    elif 2 * left.lo >= pi.hi:
        sine_hi = ls.hi
    else:
        sine_hi = SCALE
    sine = I(min(ls.lo, rs.lo), sine_hi)
    return cosine, sine


def sqrt_positive_real(value):
    modulus = (square(value.real) + square(value.imag)).sqrt()
    radicand = (modulus + value.real) / 2
    assert radicand.lo > 0
    real = radicand.sqrt()
    return C(real, value.imag / (2 * real))


def derivatives(lo, hi):
    cosine, sine = trigonometric_range(lo, hi)
    radius = I.integer(5).sqrt() / 2
    z = C(-I.rational(1, 2) - radius * cosine, radius * sine)
    z2 = power(z, 2)
    d = C(1) + z2
    w = divide(C(-1), z2)
    s = sqrt_positive_real(C(1) - w + w * w)
    r = divide(C(1), C(1) + s)
    rp = divide(C(1) - 2 * w, 2 * s * power(C(1) + s, 2))
    hp = divide(2 * z, d) - divide(C(1), z) - divide(C(1), z - C(1)) + divide(r, power(z, 3))
    hpp = (divide(2 * (C(1) - z2), power(d, 2)) + divide(C(1), z2) +
           divide(C(1), power(z - C(1), 2)) - divide(3 * r, power(z, 4)) +
           divide(2 * rp, power(z, 6)))
    zp, zpp = C(0, -1) * (z + C(I.rational(1, 2))), -(z + C(I.rational(1, 2)))
    return (hp * zp).real, (hpp * zp * zp + hp * zpp).real


leaves = []


def cover(lo, hi, order, upper, original_index, depth=0):
    passed = False
    try:
        enclosure = derivatives(lo, hi)[order - 1]
        passed = Fraction(enclosure.hi, SCALE) < upper
    except AssertionError:
        pass  # Refine an unresolved denominator/branch box; no sign is guessed.
    if passed:
        leaves.append({'lo': str(lo), 'hi': str(hi), 'derivative_order': order,
                       'strict_upper_bound': str(upper), 'enclosure': enclosure.exact_json(),
                       'source_leaf_index': original_index, 'additional_bisection_depth': depth})
        return
    assert depth < 18, ('Uncertified interval', lo, hi, order)
    middle = (lo + hi) / 2
    cover(lo, middle, order, upper, original_index, depth + 1)
    cover(middle, hi, order, upper, original_index, depth + 1)


domains = {1: [], 2: []}
for index, row in enumerate(old['leaves']):
    lo, hi = Fraction(row['lo']), Fraction(row['hi'])
    order, upper = row['derivative_order'], Fraction(row['strict_upper_bound'])
    assert order in (1, 2) and lo < hi
    assert upper == (Fraction(-1, 10) if order == 2 else 0)
    match = re.fullmatch(r'\[([^,\]]+),\s*([^\]]+)\]', row['enclosure'])
    assert match and Fraction(match.group(1)) < Fraction(match.group(2)) < upper
    domains[order].append((lo, hi))
    cover(lo, hi, order, upper, index)
for order, endpoints in [(2, (Fraction(0), Fraction(1, 100))),
                         (1, (Fraction(1, 100), Fraction(1913, 1000)))]:
    intervals = sorted(domains[order])
    assert intervals[0][0] == endpoints[0] and intervals[-1][1] == endpoints[1]
    assert all(left[1] == right[0] for left, right in zip(intervals, intervals[1:]))
    fresh = sorted((Fraction(row['lo']), Fraction(row['hi'])) for row in leaves if row['derivative_order'] == order)
    assert fresh[0][0] == endpoints[0] and fresh[-1][1] == endpoints[1]
    assert all(left[1] == right[0] for left, right in zip(fresh, fresh[1:]))
cosine = iv.cosine_small(rational(Fraction(1913, 1000)))
endpoint_a = I.rational(1, 2) + I.integer(5).sqrt() * cosine / 2
assert Fraction(endpoint_a.lo, SCALE) > Fraction('0.12482826182419')
assert Fraction(endpoint_a.hi, SCALE) < Fraction('0.12482826182420')
assert 0 < endpoint_a.lo and Fraction(endpoint_a.hi, SCALE) < Fraction(1, 8)
result = {'reviewer': 'main Codex', 'all_controls_passed': True,
          'all_enclosures_integer_outward_arithmetic': True,
          'original_program_or_library_executed': False, 'source_leaf_count': 128,
          'independent_cover_leaf_count': len(leaves),
          'whole_rational_domain_covered_without_gaps': True,
          'source_SHA256': SOURCE_SHA, 'interval_module_SHA256': hashlib.sha256(module_path.read_bytes()).hexdigest(),
          'own_verifier_SHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'endpoint_minus_real_z': endpoint_a.exact_json(), 'leaves': leaves,
          'source_printed_derivative_enclosures_not_authenticating_historical_execution': True,
          'analytic_branch_and_exact_saddle_identity_require_separate_main_proof': True,
          'full_endpoint_remainder_bound_proved_here': False,
          'whole_archive_audit_complete': False, 'e_plus_pi_proof': False}
target = BASE / 'RAW_EXTERIOR_PHASE_INTEGER_MAIN_CONTROL.json'
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'leaves'}, ensure_ascii=False))
