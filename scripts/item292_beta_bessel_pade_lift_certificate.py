#!/usr/bin/env python3
"""Deterministic exact checker for Item 292.

The bounded loops below verify Bessel coefficients, the every-third regular
continued-fraction convergents of e, the fixed-RHS Padé determinant, centered
solution families, and proper-target reductions.  They are EXACT FINITE ONLY
and are not used as asymptotic evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def digest(rows: list[dict[str, Any]]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def beta_sequences(limit: int) -> tuple[list[int], list[int]]:
    q = [1, 1]
    p = [1, 3]
    for n in range(2, limit + 1):
        coefficient = 4 * n - 2
        q.append(coefficient * q[-1] + q[-2])
        p.append(coefficient * p[-1] + p[-2])
    return p, q


def poly_add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * value for value in poly]


def poly_shift(poly: list[int], places: int) -> list[int]:
    return [0] * places + poly


def poly_eval(poly: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def bessel_closed(n: int) -> list[int]:
    """A_n(X)=sum_(k=0)^n (2n-k)!/[k!(n-k)!] X^k."""
    return [
        math.factorial(2 * n - k)
        // (math.factorial(k) * math.factorial(n - k))
        for k in range(n + 1)
    ]


def y_at_signed_two(n: int, sign: int) -> int:
    """Classical y_n(2*sign), with sign in {-1,+1}."""
    assert sign in (-1, 1)
    return sum(
        sign**j
        * math.factorial(n + j)
        // (math.factorial(j) * math.factorial(n - j))
        for j in range(n + 1)
    )


def e_partial_quotient(index: int) -> int:
    """Euler's e=[a_0;a_1,...], using zero-based index."""
    if index == 0:
        return 2
    if index % 3 == 2:
        return 2 * ((index + 1) // 3)
    return 1


def e_convergents(last_index: int) -> tuple[list[int], list[int]]:
    p_minus_two, p_minus_one = 0, 1
    q_minus_two, q_minus_one = 1, 0
    numerators: list[int] = []
    denominators: list[int] = []
    for index in range(last_index + 1):
        partial = e_partial_quotient(index)
        p_current = partial * p_minus_one + p_minus_two
        q_current = partial * q_minus_one + q_minus_two
        numerators.append(p_current)
        denominators.append(q_current)
        p_minus_two, p_minus_one = p_minus_one, p_current
        q_minus_two, q_minus_one = q_minus_one, q_current
    return numerators, denominators


def centered(value: int, odd_modulus: int) -> int:
    assert odd_modulus > 0 and odd_modulus % 2 == 1
    residue = value % odd_modulus
    if 2 * residue > odd_modulus:
        residue -= odd_modulus
    return residue


def check_bessel(limit: int) -> dict[str, Any]:
    p, q = beta_sequences(limit)
    recurrence_polys = [[1], [2, 1]]
    rows: list[dict[str, Any]] = []
    for n in range(limit + 1):
        closed = bessel_closed(n)
        if n >= 2:
            recurrence_polys.append(
                poly_add(
                    poly_scale(recurrence_polys[n - 1], 4 * n - 2),
                    poly_shift(recurrence_polys[n - 2], 2),
                )
            )
        assert recurrence_polys[n] == closed
        assert poly_eval(closed, -1) == q[n]
        assert poly_eval(closed, 1) == p[n]
        assert y_at_signed_two(n, 1) == p[n]
        assert (-1) ** n * y_at_signed_two(n, -1) == q[n]
        rows.append(
            {
                "n": n,
                "degree": len(closed) - 1,
                "q_digits": len(str(q[n])),
                "p_digits": len(str(p[n])),
            }
        )
    return {
        "range": [0, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "label": "EXACT FINITE ONLY",
    }


def check_pade_and_lifts(limit: int) -> dict[str, Any]:
    p, q = beta_sequences(limit)
    last_cf_index = 3 * limit - 1
    convergent_p, convergent_q = e_convergents(last_cf_index)
    rows: list[dict[str, Any]] = []
    family_rows = 0
    for n in range(2, limit + 1):
        index = 3 * n - 2
        assert p[n] == convergent_p[index]
        assert q[n] == convergent_q[index]
        assert (
            p[n] * q[n - 1] - p[n - 1] * q[n]
            == 2 * (-1) ** (n - 1)
        )

        a = q[n - 1]
        b = q[n]
        signed_r = centered(a * a, b)
        rho = abs(signed_r)
        sign = (-1) ** (n - 1)
        numerator = p[n] * signed_r - 2 * sign * a
        assert numerator % b == 0
        j_value = numerator // b
        assert p[n] * signed_r - j_value * b == 2 * sign * a
        assert signed_r != 0

        for ell in range(-4, 5):
            beta = signed_r + ell * b
            shifted_j = j_value + ell * p[n]
            assert p[n] * beta - shifted_j * b == 2 * sign * a
            assert abs(beta) >= rho
            family_rows += 1

        previous_regular_denominator = convergent_q[index - 1]
        next_regular_denominator = convergent_q[index + 1]
        assert 2 * previous_regular_denominator == b + a
        assert (
            next_regular_denominator
            == 2 * n * b + previous_regular_denominator
        )
        if n == 2:
            assert Fraction(2, 4 * n - 1) == Fraction(2 * a, b)
        else:
            assert Fraction(2, 4 * n - 1) < Fraction(2 * a, b)
        assert Fraction(2 * a, b) < Fraction(2, 4 * n - 2)

        rows.append(
            {
                "n": n,
                "regular_cf_index": index,
                "signed_r_sign": (signed_r > 0) - (signed_r < 0),
                "rho_digits": len(str(rho)),
                "q_previous_digits": len(str(a)),
                "next_denominator_digits": len(str(next_regular_denominator)),
                "relative_eta_correction_upper_denominator":
                    4 * next_regular_denominator,
            }
        )
    return {
        "range": [2, limit],
        "rows": len(rows),
        "solution_family_rows": family_rows,
        "digest": digest(rows),
        "label": "EXACT FINITE ONLY",
    }


def check_proper_targets(limit: int) -> dict[str, Any]:
    p, q = beta_sequences(limit)
    rows: list[dict[str, Any]] = []
    fixed_clearing_values = (1, 3, 5, 7, 11, 35, 77)
    for n in range(2, limit + 1):
        a = q[n - 1]
        b = q[n]
        sign = (-1) ** (n - 1)
        full_r = centered(a * a, b)
        for clearing in fixed_clearing_values:
            target = b // math.gcd(b, clearing)
            if target == 1:
                continue
            target_r = centered(full_r, target)
            assert target_r == centered(a * a, target)
            assert math.gcd(p[n], target) == 1
            numerator = p[n] * target_r - 2 * sign * a
            assert numerator % target == 0
            target_j = numerator // target
            assert (
                p[n] * target_r - target_j * target
                == 2 * sign * a
            )
            assert abs(target_r) <= abs(full_r)
            assert abs(target_r) <= (target - 1) // 2
            rows.append(
                {
                    "n": n,
                    "clearing": clearing,
                    "target_digits": len(str(target)),
                    "target_r_sign": (target_r > 0) - (target_r < 0),
                }
            )
    return {
        "fixed_clearing_values": list(fixed_clearing_values),
        "rows": len(rows),
        "digest": digest(rows),
        "exceptional_prime_search": False,
        "label": "EXACT FINITE ONLY",
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item292-beta-bessel-pade-lift-certificate-v1",
        "description": (
            "Exact reverse-Bessel companion, every-third e-convergent, "
            "fixed-RHS Padé determinant, centered lift family, eta-bound "
            "bookkeeping, and proper-target checker"
        ),
        "theorem": {
            "bessel_seed": (
                "with A_n(X)=sum_k (2n-k)!/[k!(n-k)!] X^k, "
                "q_n=A_n(-1)=(-1)^n y_n(-2) and "
                "p_n=A_n(1)=y_n(2)"
            ),
            "e_convergent": (
                "p_n/q_n is Euler's regular continued-fraction "
                "convergent of zero-based index 3n-2"
            ),
            "wronskian": (
                "p_n*q_(n-1)-p_(n-1)*q_n=2*(-1)^(n-1)"
            ),
            "minimum_equivalence": (
                "rho_n=min |beta| over beta,J with "
                "p_n*beta-J*q_n=2*(-1)^(n-1)*q_(n-1)"
            ),
            "eta_identity": (
                "for eta_n=(-1)^n(e-p_n/q_n)>0, "
                "(-1)^(n-1)(beta*e-J)=2*q_(n-1)/q_n-beta*eta_n"
            ),
            "eta_bound": (
                "eta_n<1/[q_n*Q_(3n-1)], with "
                "Q_(3n-1)=2n*q_n+Q_(3n-3)"
            ),
            "homogeneous_measure_barrier": (
                "a fixed-power homogeneous lower bound for |beta*e-J|, "
                "combined only with the O(1/n) target size, forces at "
                "most a polynomial lower scale for |beta|"
            ),
            "proper_target": (
                "for Q|q_n, the centered beta is centered(r_n mod Q) "
                "and solves p_n*beta-J*Q=2*(-1)^(n-1)*q_(n-1)"
            ),
            "scope": (
                "no all-n half-bound, factorial lower bound, or O(n)-height "
                "lift construction is proved"
            ),
        },
        "bounded_exact_checks": {
            "bessel": check_bessel(32),
            "pade_and_lifts": check_pade_and_lifts(160),
            "proper_targets": check_proper_targets(80),
            "asymptotic_extrapolation": False,
            "exceptional_prime_search": False,
            "label": "EXACT FINITE ONLY",
        },
        "admission": {
            "full_target_degree_one_exclusion": "OPEN",
            "full_target_O_n_lift": "OPEN",
            "proper_target_large_factor_bound": "OPEN",
            "homogeneous_measure_route": "SCOPED FAIL",
            "inhomogeneous_ostrowski_route": "OPEN",
            "item282_product_baseline": "OPEN AND SEPARATE",
            "new_route1_rate": 0,
            "new_beta_capacity_reduction": 0,
            "positive_linear_capacity_admission": "FAIL",
        },
        "open": [
            "the all-n inequality 2*rho_n>=q_(n-1)",
            "any lower bound log rho_n>=n log n-O(n)",
            "any construction log rho_n=O(n)",
            "an inhomogeneous shrinking-target or Ostrowski theorem using the exact endpoint",
            "a large proper de-overlapped target residue theorem",
            "the Item282 common product baseline and weighted-return cover",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
