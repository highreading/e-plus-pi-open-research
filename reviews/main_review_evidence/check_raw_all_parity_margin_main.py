"""Main-authored rational verification of the fixed rate constant only."""
from fractions import Fraction as F
from math import isqrt, prod
from pathlib import Path
import datetime
import json

BASE = Path(__file__).resolve().parent
PRIMES = (3, 7, 23, 43, 71, 83, 101, 109, 127, 151)
TERMS = 80


def small_log_interval(q):
    # log(q)=2 sum z^(2j+1)/(2j+1), 0<=z<=1/3.
    assert F(1) <= q <= F(2)
    z = (q-1)/(q+1)
    s = F(0)
    power = z
    for j in range(TERMS):
        s += 2*power/F(2*j+1)
        power *= z*z
    tail = 2*power/(F(2*TERMS+1)*(1-z*z))
    return s, s+tail


LOG_TWO = small_log_interval(F(2))


def log_interval(q):
    assert q >= 1
    k = 0
    while q >= 2:
        q /= 2
        k += 1
    lo, hi = small_log_interval(q)
    return lo+k*LOG_TWO[0], hi+k*LOG_TWO[1]


def rounded_outward(interval, digits=30):
    scale = 10**digits
    lo, hi = interval
    a = lo.numerator*scale//lo.denominator
    b = -((-hi.numerator*scale)//hi.denominator)
    return {"denominator": str(scale), "lower_numerator": str(a),
            "upper_numerator": str(b)}


sqrt_scale = 10**35
sqrt_floor = isqrt(5*sqrt_scale*sqrt_scale)
assert sqrt_floor*sqrt_floor <= 5*sqrt_scale*sqrt_scale < (sqrt_floor+1)**2
phi_lo = (1+F(sqrt_floor, sqrt_scale))/2
phi_hi = (1+F(sqrt_floor+1, sqrt_scale))/2
log_phi = (log_interval(phi_lo)[0], log_interval(phi_hi)[1])
rate_lo, rate_hi = (F(3, 2)*v for v in LOG_TWO)
prime_logs = {}
for p in PRIMES:
    lo, hi = log_interval(F(p))
    prime_logs[str(p)] = rounded_outward((lo, hi))
    rate_lo += lo/F(p-1)
    rate_hi += hi/F(p-1)
margin = (rate_lo-5*log_phi[1], rate_hi-5*log_phi[0])
assert margin[0] > F(15628796017, 10**12)
assert margin[0] > F(3, 200)
assert prod(PRIMES) == 25839289479611181
result = {
    "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "reviewer": "main Codex", "method": "exact Fraction arithmetic; positive atanh series with explicit geometric tail; integer square-root enclosure",
    "atanh_terms": TERMS, "prime_set": list(PRIMES), "prime_product": prod(PRIMES),
    "prime_log_intervals": prime_logs, "log_phi_interval": rounded_outward(log_phi),
    "L_interval": rounded_outward((rate_lo, rate_hi)),
    "L_minus_5_log_phi_interval": rounded_outward(margin),
    "lower_exceeds_0_015628796017": True, "lower_exceeds_3_over_200": True,
    "scope": "Fixed numerical rate margin only. This does not certify any prime divisor of the actual reduced denominator, any amplitude, or the all-parity exclusion theorem."
}
(BASE/'RAW_ALL_PARITY_RATE_MARGIN_MAIN_CONTROL.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k: result[k] for k in ('prime_product','L_minus_5_log_phi_interval','lower_exceeds_3_over_200','scope')}, ensure_ascii=False))
