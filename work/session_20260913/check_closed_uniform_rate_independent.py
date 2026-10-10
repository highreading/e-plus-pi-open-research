"""Independent rational rate check for the fixed ten-prime set only.

Use log x=sum_{j>=1}(1-1/x)^j/j, not the source's atanh series.
No finite seed classification is performed here.
"""
import json
from fractions import Fraction as F
from math import prod
from pathlib import Path

BASE = Path(__file__).resolve().parent
PRIMES = (3, 7, 23, 43, 71, 83, 101, 109, 127, 151)
TERMS = 72


def base_log(x):
    assert F(1) <= x <= F(2)
    u = 1 - 1/x
    low = sum((u**j / j for j in range(1, TERMS + 1)), F(0))
    tail = u**(TERMS + 1) / ((TERMS + 1) * (1 - u))
    return low, low + tail


LOG2 = base_log(F(2))


def logarithm(x):
    power = 0
    while x >= 2:
        x /= 2
        power += 1
    low, high = base_log(x)
    return low + power * LOG2[0], high + power * LOG2[1]


Llo = F(3, 2) * LOG2[0]
Lhi = F(3, 2) * LOG2[1]
for p in PRIMES:
    lo, hi = logarithm(F(p))
    Llo += lo / (p - 1)
    Lhi += hi / (p - 1)
root_lo = F(22360679774997896964, 10**19)
root_hi = root_lo + F(1, 10**19)
assert root_lo**2 < 5 < root_hi**2
Tlo = 5 * logarithm((1 + root_lo)/2)[0]
Thi = 5 * logarithm((1 + root_hi)/2)[1]
Glo, Ghi = Llo - Thi, Lhi - Tlo
source = json.loads((BASE / 'raw_closed_uniform_seed_rate_certificate.json').read_text())
assert tuple(source['uniform_odd_primes']) == PRIMES
checks = {}
for label, (lo, hi) in {
    'rate_interval': (Llo, Lhi),
    'threshold_interval': (Tlo, Thi),
    'rate_minus_threshold_interval': (Glo, Ghi),
}.items():
    claimed = source[label]
    lower = F(claimed['lower_numerator'], claimed['denominator'])
    upper = F(claimed['upper_numerator'], claimed['denominator'])
    assert lower < lo <= hi < upper
    checks[label] = dict(**claimed, strictly_contains_independent_bounds=True)
assert Glo > F(15, 1000)
out = dict(status='PASS', fixed_primes=list(PRIMES),
           method='72-term positive -log(1-u) series; independent rational sqrt(5) bracket.',
           certified_gap_above= '3/200', prime_product=prod(PRIMES),
           source_intervals_independently_verified=checks,
           scope='Rate and denominator assembly only; each finite seed certificate retains its own review.')
target = BASE / 'closed_uniform_rate_independent_certificate.json'
target.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
