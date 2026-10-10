#!/usr/bin/env python3
"""Exact certificate for the Euler-transfer exponent-two barrier.

The script uses only rational arithmetic to certify the continued-fraction
bounds for a finite prefix of e.  It also prints the explicit x=2
Nesterenko--Waldschmidt exponents from equation (26) of the companion note.
The transcendence theorems themselves are cited and applied in the note; the
script certifies the algebraic/numerical layer, not those published theorems.
"""

from __future__ import annotations

from fractions import Fraction
from math import e, factorial, log, pi
import json
from pathlib import Path


N_CONVERGENTS = 60
TAIL_CUTOFF = 500


def partial_quotient(j: int) -> int:
    if j == 0:
        return 2
    if j % 3 == 2:
        return 2 * ((j + 1) // 3)
    return 1


def rational_e_interval(cutoff: int) -> tuple[Fraction, Fraction]:
    """Return rigorous lower/upper bounds for e.

    After the term 1/cutoff!, the remaining tail is strictly smaller than
    1/(cutoff*cutoff!), by comparison with a geometric series of ratio
    1/(cutoff+1).
    """

    lower = sum((Fraction(1, factorial(k)) for k in range(cutoff + 1)), Fraction())
    upper = lower + Fraction(1, cutoff * factorial(cutoff))
    return lower, upper


def convergents(n: int) -> list[tuple[int, int, int]]:
    p_minus_2, p_minus_1 = 0, 1
    q_minus_2, q_minus_1 = 1, 0
    out: list[tuple[int, int, int]] = []
    for m in range(n + 1):
        a = partial_quotient(m)
        p = a * p_minus_1 + p_minus_2
        q = a * q_minus_1 + q_minus_2
        out.append((m, p, q))
        p_minus_2, p_minus_1 = p_minus_1, p
        q_minus_2, q_minus_1 = q_minus_1, q
    return out


def absolute_error_interval(
    p: int, q: int, e_lower: Fraction, e_upper: Fraction
) -> tuple[Fraction, Fraction]:
    r = Fraction(p, q)
    if r < e_lower:
        return e_lower - r, e_upper - r
    if r > e_upper:
        return r - e_upper, r - e_lower
    raise AssertionError("e interval is not fine enough to separate the convergent")


def nw_x2_exponent(d: int) -> float:
    d0 = 2 * d
    return (
        211.0
        * d0
        / 4.0
        * (13.0 + 2.0 * e**2 * (pi + 1.0))
        * (3.3 * d0 * log(d0 + 2.0) + 2.0)
    )


def main() -> None:
    e_lower, e_upper = rational_e_interval(TAIL_CUTOFF)
    conv = convergents(N_CONVERGENTS + 1)

    checked = 0
    special = []
    for m, p, q in conv[:-1]:
        err_lower, err_upper = absolute_error_interval(p, q, e_lower, e_upper)
        a_next = partial_quotient(m + 1)
        cf_lower = Fraction(1, (a_next + 2) * q * q)
        cf_upper = Fraction(1, a_next * q * q)
        assert err_lower > cf_lower
        assert err_upper < cf_upper
        checked += 1

        if m >= 1 and (m + 2) % 3 == 0:
            k = (m + 2) // 3
            assert m == 3 * k - 2
            assert a_next == 2 * k
            scaled_upper = err_upper * q * q
            assert scaled_upper < Fraction(1, 2 * k)
            special.append(
                {
                    "k": k,
                    "m": m,
                    "p": str(p),
                    "q": str(q),
                    "a_next": a_next,
                    "q2_error_upper_decimal": format(float(scaled_upper), ".18g"),
                    "exact_comparison_certified": True,
                    "target_upper": f"1/{2*k}",
                }
            )

    assert special
    output = {
        "status": "PASS",
        "exact_checks": {
            "continued_fraction_pattern": "a_0=2; a_(3k-2)=1, a_(3k-1)=2k, a_(3k)=1",
            "convergents_checked": checked,
            "rigorous_e_interval_cutoff": TAIL_CUTOFF,
            "bounds_checked": "1/((a_next+2)q^2) < |e-p/q| < 1/(a_next q^2)",
            "special_subsequence": "m=3k-2, so q_m^2|e-p_m/q_m|<1/(2k)",
            "last_special_record": special[-1],
        },
        "height_reduction": {
            "degree": "D_r=[Q(i(s-p/q)):Q] <= 2d, d=[Q(s):Q]",
            "height": "log(q)-h(s)-log(2) <= h(i(s-p/q)) <= log(q)+h(s)+log(6)",
        },
        "nw_theorem1_x_equals_2": {
            "formula": "211*(2d)/4*(13+2*e^2*(pi+1))*(3.3*(2d)*log(2d+2)+2)",
            "sample_exponents": {
                str(d): format(nw_x2_exponent(d), ".12f") for d in range(1, 11)
            },
            "optimized_coefficient_elementary_floor": ">1266*D > 2",
        },
        "verdict": (
            "The explicit e-convergents reach height exponent 2 and beat every "
            "positive constant at exponent 2; the cited uniform quantitative "
            "Lindemann theorem remains strictly above exponent 2."
        ),
    }

    result_path = Path(__file__).resolve().parents[1] / "results" / (
        "euler_transfer_quantitative_lindemann_certificate.json"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    print(f"RESULT_PATH={result_path}")


if __name__ == "__main__":
    main()
