#!/usr/bin/env python3
"""Independent exact audit of the softened-singularity finite scan.

This program deliberately does not import the original probe.  It computes
the jets of e^{-z}F(z) by direct binomial convolution from the closed formula
for F^{(j)}(0), forms D(z)^n by ordinary polynomial multiplication, and then
uses the direct product formula for the jets of D^n e^{-z}F.  Its enclosure
of e+pi uses exact Fraction partial sums and rigorous remainders, rather than
the fixed-point interval implementation in the original probe.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


sys.set_int_max_str_digits(0)


def f_jet(k: int) -> int:
    """Return F^(k)(0) for F(z)=4 atan(z/(2-z))."""
    if k == 0:
        return 0
    q, residue = divmod(k - 1, 4)
    if residue == 0:
        numerator = 2 * math.factorial(4 * q)
    elif residue == 1:
        numerator = 2 * math.factorial(4 * q + 1)
    elif residue == 2:
        numerator = math.factorial(4 * q + 2)
    else:
        return 0
    assert numerator % (4**q) == 0
    return ((-1) ** q) * numerator // (4**q)


def eta_zero_direct(max_k: int) -> list[int]:
    """Jets of e^{-z}F from the direct Leibniz convolution."""
    return [
        sum(
            math.comb(k, j) * ((-1) ** (k - j)) * f_jet(j)
            for j in range(k + 1)
        )
        for k in range(max_k + 1)
    ]


def multiply_ordinary(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def jets_after_polynomial_product(
    eta_zero: list[int], polynomial: list[int], max_k: int
) -> list[int]:
    """Jets of polynomial(z)*sum eta_k z^k/k!, by direct convolution."""
    factorial = [math.factorial(k) for k in range(max_k + 1)]
    answer = []
    for k in range(max_k + 1):
        value = 0
        for ell in range(min(k, len(polynomial) - 1) + 1):
            falling = factorial[k] // factorial[k - ell]
            value += polynomial[ell] * falling * eta_zero[k - ell]
        answer.append(value)
    return answer


def e_interval(last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum((Fraction(1, math.factorial(k)) for k in range(last_index + 1)), Fraction())
    # For M=last_index >= 1, sum_{k>M}1/k! < 1/(M*M!).
    return partial, partial + Fraction(1, last_index * math.factorial(last_index))


def atan_reciprocal_interval(q: int, last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            ((-1) ** k) * Fraction(1, (2 * k + 1) * q ** (2 * k + 1))
            for k in range(last_index + 1)
        ),
        Fraction(),
    )
    next_size = Fraction(
        1, (2 * last_index + 3) * q ** (2 * last_index + 3)
    )
    if last_index % 2 == 0:
        return partial - next_size, partial
    return partial, partial + next_size


def e_plus_pi_interval() -> tuple[Fraction, Fraction, dict[str, int]]:
    e_lo, e_hi = e_interval(450)
    a5_lo, a5_hi = atan_reciprocal_interval(5, 560)
    a239_lo, a239_hi = atan_reciprocal_interval(239, 175)
    return (
        e_lo + 16 * a5_lo - 4 * a239_hi,
        e_hi + 16 * a5_hi - 4 * a239_lo,
        {"e_last_index": 450, "atan_1_5_last_index": 560, "atan_1_239_last_index": 175},
    )


def abs_numerator_interval(
    u: int, v: int, s_lo_num: int, s_hi_num: int, denominator: int
) -> tuple[int, int]:
    assert u >= 0
    lo = u * s_lo_num - v * denominator
    hi = u * s_hi_num - v * denominator
    assert lo <= hi
    if lo > 0:
        return lo, hi
    if hi < 0:
        return -hi, -lo
    return 0, max(-lo, hi)


def direct_coordinates(eta: list[int], b: int) -> tuple[int, int, int, int]:
    factorial_b = math.factorial(b)
    u = sum(((-1) ** k) * factorial_b // math.factorial(k) for k in range(b + 1))
    v = factorial_b + sum(
        eta[k] * factorial_b // math.factorial(k) for k in range(b + 1)
    )
    common = math.gcd(abs(u), abs(v))
    return u, v, u // common, v // common


def certify_minimum(entries: list[dict]) -> tuple[dict, bool, int]:
    candidate = min(entries, key=lambda item: item["abs_lo"] + item["abs_hi"])
    competing_lowers = [
        item["abs_lo"] for item in entries if item["b"] != candidate["b"]
    ]
    gap = min(competing_lowers) - candidate["abs_hi"] if competing_lowers else 0
    return candidate, gap > 0, gap


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=60)
    parser.add_argument("--b-multiple", type=int, default=4)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reference", type=Path)
    args = parser.parse_args()
    max_b = args.n_max * args.b_multiple

    s_lo, s_hi, interval_parameters = e_plus_pi_interval()
    denominator = math.lcm(s_lo.denominator, s_hi.denominator)
    s_lo_num = s_lo.numerator * (denominator // s_lo.denominator)
    s_hi_num = s_hi.numerator * (denominator // s_hi.denominator)
    assert s_lo_num < s_hi_num

    eta_zero = eta_zero_direct(max_b)
    # Independent verification of the differential recurrence for eta_0.
    for k in range(max_b):
        em1 = eta_zero[k - 1] if k >= 1 else 0
        em2 = eta_zero[k - 2] if k >= 2 else 0
        assert (
            2 * (eta_zero[k + 1] + eta_zero[k])
            - 2 * k * (eta_zero[k] + em1)
            + k * (k - 1) * (em1 + em2)
            == 4 * ((-1) ** k)
        )

    polynomial = [1]
    records = []
    coordinate_digest = hashlib.sha256()
    reference_records = {}
    if args.reference:
        reference = json.loads(args.reference.read_text())
        reference_records = {int(record["n"]): record for record in reference["records"]}

    for n in range(1, args.n_max + 1):
        polynomial = multiply_ordinary(polynomial, [2, -2, 1])
        eta = jets_after_polynomial_product(eta_zero, polynomial, args.b_multiple * n)
        entries = []
        for b in range(2, args.b_multiple * n + 1):
            u, v, up, vp = direct_coordinates(eta, b)
            assert u > 0
            g = math.gcd(abs(u), abs(v))
            alo, ahi = abs_numerator_interval(
                up, vp, s_lo_num, s_hi_num, denominator
            )
            coordinate_digest.update(f"{n},{b},{u},{v},{g}\n".encode())
            entries.append(
                {"b": b, "gcd": g, "u_primitive": up, "v_primitive": vp, "abs_lo": alo, "abs_hi": ahi}
            )

        candidate, certified, gap = certify_minimum(entries)
        lower_b = max(2, math.ceil(n / 2))
        restricted = [item for item in entries if item["b"] >= lower_b]
        rcandidate, rcertified, rgap = certify_minimum(restricted)

        # Closed b=2 check, independently from the original recurrence.
        assert entries[0]["u_primitive"] == 1
        expected_v2 = 2 + (2 ** (n + 1)) * (1 - 2 * n)
        assert entries[0]["v_primitive"] == expected_v2

        if n in reference_records:
            old = reference_records[n]
            assert candidate["b"] == old["global_min_b"]
            assert certified == old["global_min_certified"]
            assert rcandidate["b"] == old["restricted_min_b"]
            assert rcertified == old["restricted_min_certified"]

        records.append(
            {
                "n": n,
                "global_min_b": candidate["b"],
                "global_min_gcd": candidate["gcd"],
                "global_min_certified": certified,
                "global_certificate_gap_numerator_decimal_digits": len(str(gap)),
                "restricted_b_minimum": lower_b,
                "restricted_min_b": rcandidate["b"],
                "restricted_min_gcd": rcandidate["gcd"],
                "restricted_min_certified": rcertified,
                "restricted_certificate_gap_numerator_decimal_digits": len(str(rgap)),
            }
        )

    payload = {
        "description": "Independent direct-convolution audit of the softened-singularity finite scan",
        "parameters": {"n_min": 1, "n_max": args.n_max, "b_max_for_n": f"{args.b_multiple}*n"},
        "independent_interval": {
            **interval_parameters,
            "common_denominator_decimal_digits": len(str(denominator)),
            "width_numerator": s_hi_num - s_lo_num,
            "method": "exact Fraction partial sums and rigorous analytic remainder bounds",
        },
        "all_n_2_through_nmax_have_certified_global_minimum_b2": all(
            record["global_min_certified"] and record["global_min_b"] == 2
            for record in records
            if record["n"] >= 2
        ),
        "all_reference_minimizers_and_certification_flags_match": bool(args.reference),
        "all_coordinate_tuples_sha256": coordinate_digest.hexdigest(),
        "records": records,
        "warning": "Finite exact certificate only; no asymptotic claim is inferred.",
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
