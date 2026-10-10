"""Rational interval check of the rate from the three CLOSED certificates.

This verifies the numerical inequality only. The certificate arithmetic
and the all-index theorems retain their separate independent-review gates.
"""
import json
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
TERMS = 24
SCALE = 10**12


def series_log(x):
    """Bounds log(x) for rational 1<=x<=2, using an explicit positive tail."""
    assert 1 <= x <= 2
    r = (x-1)/(x+1)
    lower = 2*sum((r**(2*j+1)/F(2*j+1) for j in range(TERMS)), F(0))
    tail = 2*r**(2*TERMS+1)/(F(2*TERMS+1)*(1-r*r))
    return lower, lower+tail


LOG2 = series_log(F(2))


def rational_log(x):
    power = 0
    while x >= 2:
        x /= 2
        power += 1
    lo, hi = series_log(x)
    return power*LOG2[0]+lo, power*LOG2[1]+hi


def displayed_interval(lower, upper):
    lo = (lower*SCALE).numerator//(lower*SCALE).denominator
    hi_scaled = upper*SCALE
    hi = -((-hi_scaled.numerator)//hi_scaled.denominator)
    return {"denominator": SCALE, "lower_numerator": lo, "upper_numerator": hi}


first = json.loads((BASE/"raw_predeclared_residue_seed_atlas.json").read_text())
second = json.loads((BASE/"raw_second_predeclared_uniform_seed_certificate.json").read_text())
third = json.loads((BASE/"raw_third_predeclared_uniform_seed_certificate.json").read_text())
uniform = {3, 7}
uniform.update(row["p"] for row in first["atlas"] if row["all_residues_good"])
for certificate in (second, third):
    uniform.update(row["p"] for row in certificate["results"] if row["all_residues_good"])
uniform = sorted(uniform)
lo, hi = F(3, 2)*LOG2[0], F(3, 2)*LOG2[1]
for p in uniform:
    lp = rational_log(F(p))
    lo += lp[0]/(p-1)
    hi += lp[1]/(p-1)

sqrt5lo = F(2236067977499789696, 10**18)
sqrt5hi = sqrt5lo+F(1, 10**18)
assert sqrt5lo**2 < 5 < sqrt5hi**2
phi_lo, phi_hi = (1+sqrt5lo)/2, (1+sqrt5hi)/2
threshold_lo = 5*rational_log(phi_lo)[0]
threshold_hi = 5*rational_log(phi_hi)[1]
gap_lo, gap_hi = lo-threshold_hi, hi-threshold_lo
payload = {
    "scope": "Exact rational rate inequality, conditional on the separately reviewed finite seed certificates.",
    "uniform_odd_primes": uniform,
    "atanh_series_terms": TERMS,
    "range_reduction": "Each integer prime is divided by a power of two into [1,2).",
    "tail_bound": "2*r^(2*TERMS+1)/((2*TERMS+1)*(1-r^2)), r=(x-1)/(x+1)",
    "sqrt5_bracket_checked_by_squares": True,
    "rate_interval": displayed_interval(lo, hi),
    "threshold_interval": displayed_interval(threshold_lo, threshold_hi),
    "rate_minus_threshold_interval": displayed_interval(gap_lo, gap_hi),
    "strictly_above_threshold": gap_lo > 0,
    "strictly_below_threshold": gap_hi < 0,
}
(BASE/"raw_closed_uniform_seed_rate_certificate.json").write_text(
    json.dumps(payload, indent=2)+"\n"
)
print(json.dumps(payload, indent=2))
