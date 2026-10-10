#!/usr/bin/env python3
"""Exact certificate for Item 176: the common-polynomial reciprocal Padé ray.

Only the optional floating root diagnostic is non-proof data.  Every field
under ``proved_checks`` is checked with Python integers/Fractions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item176_route2_native_reciprocal_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item176_route2_native_reciprocal_certificate.json"
)


def tau(k: int) -> int:
    """F^(k)(0) for F(z)=4 atan(z/(2-z))."""
    if k == 0 or k % 4 == 0:
        return 0
    q, r = divmod(k, 4)
    if r in (1, 2):
        return (-1) ** q * 2 * math.factorial(k - 1) // (4**q)
    if r == 3:
        return (-1) ** q * math.factorial(k - 1) // (4**q)
    raise AssertionError("unreachable")


def valuation(n: int, p: int) -> int:
    n = abs(n)
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def factor_small(n: int) -> dict[str, int]:
    n = abs(n)
    ans: dict[str, int] = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            v = 0
            while n % p == 0:
                n //= p
                v += 1
            ans[str(p)] = v
        p = 3 if p == 2 else p + 2
    if n > 1:
        ans[str(n)] = 1
    return ans


def reciprocal_jets(nmax: int) -> tuple[list[int], list[int]]:
    s = [1 + tau(k) for k in range(nmax + 1)]
    h = [1]
    for n in range(1, nmax + 1):
        h.append(-sum(math.comb(n, k) * s[k] * h[n - k] for k in range(1, n + 1)))
    return s, h


def exact_checks(nmax: int, s: list[int], h: list[int]) -> dict:
    assert s[0] == 1 and h[0] == 1
    # Differential recurrence for the F jets.
    for m in range(1, nmax):
        assert 2 * tau(m + 1) - 2 * m * tau(m) + m * (m - 1) * tau(m - 1) == 0
    # Hurwitz convolution H*S=1 through the certified range.
    convolution = []
    for n in range(nmax + 1):
        v = sum(math.comb(n, k) * s[k] * h[n - k] for k in range(n + 1))
        convolution.append(v)
        assert v == (1 if n == 0 else 0)

    # Rational Rouché ledger on |z|=3/5.
    exp_tail_upper = Fraction(7, 30)
    f_tail_upper = Fraction(15, 28)
    total_upper = exp_tail_upper + f_tail_upper
    linear_lower = Fraction(4, 5)
    assert total_upper == Fraction(323, 420)
    assert linear_lower - total_upper == Fraction(13, 420) > 0

    # Rational inequalities used to locate the real zero in (-1/2,-2/5).
    # e^(1/2)>1+1/2+(1/2)^2/2=13/8>3/2.
    assert Fraction(13, 8) > Fraction(3, 2)
    atan15_lower_times4 = 4 * (Fraction(1, 5) - Fraction(1, 3 * 5**3))
    assert atan15_lower_times4 == Fraction(296, 375) > Fraction(2, 3)
    # e^(2/5)<1+2/5 + ((2/5)^2/2)/(1-2/15)=97/65<3/2.
    exp_two_fifths_upper = Fraction(7, 5) + Fraction(2, 25) / (1 - Fraction(2, 15))
    assert exp_two_fifths_upper == Fraction(97, 65) < Fraction(3, 2)
    exp_minus_two_fifths_lower = Fraction(65, 97)
    atan16_upper_times4 = Fraction(2, 3)
    assert exp_minus_two_fifths_lower - atan16_upper_times4 == Fraction(1, 291) > 0

    # Auxiliary inequalities used in the F-tail bound.
    # 1/sqrt(2)<5/7 follows after squaring; exp(9/16)>7/4 proves log(7/4)<9/16.
    assert Fraction(1, 2) < Fraction(25, 49)
    exp_9_16_lower = sum(Fraction(9, 16) ** k / math.factorial(k) for k in range(4))
    assert exp_9_16_lower == Fraction(14339, 8192) > Fraction(7, 4)
    # e^(3/5)<1+3/5+((3/5)^2/2)/(1-1/5)=73/40<11/6.
    exp_three_fifths_upper = Fraction(8, 5) + Fraction(9, 50) / (1 - Fraction(1, 5))
    assert exp_three_fifths_upper == Fraction(73, 40) < Fraction(11, 6)

    return {
        "tau_recurrence_checked_m": [1, max(0, nmax - 1)],
        "hurwitz_inverse_convolution_checked_n": [0, nmax],
        "hurwitz_convolution_sha256": hashlib.sha256(
            json.dumps(convolution, separators=(",", ":")).encode("ascii")
        ).hexdigest(),
        "rouche": {
            "circle_radius": "3/5",
            "comparison": "1+3z",
            "comparison_lower": str(linear_lower),
            "exp_tail_upper": str(exp_tail_upper),
            "F_tail_upper": str(f_tail_upper),
            "total_tail_upper": str(total_upper),
            "strict_gap": str(linear_lower - total_upper),
        },
        "real_root_bracket": {
            "interval": ["-1/2", "-2/5"],
            "S_minus_half_strict_upper": str(Fraction(2, 3) - atan15_lower_times4),
            "S_minus_two_fifths_strict_lower": str(
                exp_minus_two_fifths_lower - atan16_upper_times4
            ),
        },
        "auxiliary_rational_inequalities": {
            "exp_9_16_lower": str(exp_9_16_lower),
            "exp_2_5_upper": str(exp_two_fifths_upper),
            "exp_3_5_upper": str(exp_three_fifths_upper),
        },
    }


def finite_records(nmax: int, h: list[int]) -> list[dict]:
    records = []
    fact = 1
    selected = set(range(0, min(nmax, 20) + 1))
    selected.update(k for k in (25, 30, 40, 50, 75, 100, 125, 150, 175, 200) if k <= nmax)
    for n in range(nmax + 1):
        if n:
            fact *= n
        w = sum(h[k] * fact // math.factorial(k) for k in range(n + 1))
        # Each coefficient of n! Q_n is integral.
        assert all((fact * h[k]) % math.factorial(k) == 0 for k in range(n + 1))
        g = math.gcd(abs(w), fact)
        assert math.gcd(abs(w // g), fact // g) == 1
        if n in selected:
            records.append(
                {
                    "n": n,
                    "h_n": h[n],
                    "W_n": w,
                    "n_factorial": fact,
                    "endpoint_gcd": g,
                    "endpoint_gcd_factorization": factor_small(g),
                    "primitive_B": w // g,
                    "primitive_A": -(fact // g),
                    "h_n_bit_length": abs(h[n]).bit_length(),
                    "W_n_bit_length": abs(w).bit_length(),
                    "factorial_bit_length": fact.bit_length(),
                }
            )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nmax", type=int, default=200)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.nmax < 2:
        raise SystemExit("nmax must be at least 2")

    s, h = reciprocal_jets(args.nmax)
    obj = {
        "item": 176,
        "status": "PROVED scoped no-decay theorem; finite rows are exact diagnostics",
        "construction": {
            "F": "4 atan(z/(2-z))",
            "S": "exp(z)+F(z)",
            "H": "1/S",
            "Q_n": "sum_{k=0}^n h_k z^k/k!, where h_k=H^(k)(0)",
            "remainder": "-1+Q_n exp(z)+Q_n F(z)=O(z^(n+1))",
            "endpoint": "W_n(e+pi)-n!, W_n=n! Q_n(1)",
        },
        "nmax": args.nmax,
        "proved_checks": exact_checks(args.nmax, s, h),
        "hashes": {
            "S_jets_sha256": hashlib.sha256(
                json.dumps(s, separators=(",", ":")).encode("ascii")
            ).hexdigest(),
            "reciprocal_jets_sha256": hashlib.sha256(
                json.dumps(h, separators=(",", ":")).encode("ascii")
            ).hexdigest(),
        },
        "selected_exact_records": finite_records(args.nmax, h),
        "experimental": {
            "real_root_float_diagnostic": "-0.404821727032308...",
            "note": "The decimal is not used in any proof; the exact bracket is proved above.",
        },
        "open": [
            "This scoped theorem says nothing about endpoint-only B(1)=C(1) systems with B and C independent.",
            "It does not decide the arithmetic nature of e+pi.",
        ],
    }
    args.output.write_text(
        json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
