#!/usr/bin/env python3
"""Deterministic checks for Item 168's e=1 forced-cell analysis.

The companion report supplies the symbolic proofs.  This checker verifies:

* the three complete floor-cell parameterizations for rank at most two;
* the corresponding PNT interval sums and closed-form constants;
* the universal small-support inequality for the second-Cartier exact tail;
* the balanced four-section scalar-zero ray;
* a finite census of simultaneous rank-one Cartier-scalar zeros; and
* the frozen scalar-free p^3 gates from Item 163.

Finite scalar-zero and p^3 counts are diagnostics only.  They are never
promoted to density or non-density theorems.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ARCHIVE_ROOT = HERE.parent
DEFAULT_ITEM163 = (
    HERE / "item163_deeper_digits_certificate.json"
    if (HERE / "item163_deeper_digits_certificate.json").exists()
    else ARCHIVE_ROOT / "results" / "item163_deeper_digits_certificate.json"
)
DEFAULT_OUTPUT = (
    HERE / "item168_positive_mass_certificate.json"
    if HERE.name == "work"
    else ARCHIVE_ROOT / "results" / "item168_positive_mass_certificate.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n, flag in enumerate(sieve) if flag]


def generalized_binomial_row(exponent: int, degree: int, p: int) -> list[int]:
    """Return binom(exponent,k) mod p for 0<=k<=degree<p.

    The exponent may be negative.  Since every denominator k is below p,
    the usual multiplicative recurrence is valid in F_p.
    """
    if not (0 <= degree < p):
        raise ValueError((exponent, degree, p))
    row = [1]
    value = 1
    for k in range(1, degree + 1):
        value = value * (exponent - k + 1) % p
        value = value * pow(k, -1, p) % p
        row.append(value)
    return row


def four_section_coefficient(
    linear_exponent: int, four_exponent: int, degree: int, p: int
) -> int:
    """[x^degree](1-x)^linear_exponent*(1-x^4)^four_exponent mod p."""
    linear = generalized_binomial_row(linear_exponent, degree, p)
    four = generalized_binomial_row(four_exponent, min(four_exponent, degree // 4), p)
    total = 0
    for v, choose_four in enumerate(four):
        k = degree - 4 * v
        total += (-1 if (v + k) & 1 else 1) * choose_four * linear[k]
    return total % p


def rank_one_scalars(p: int, s: int) -> tuple[int, int]:
    """The two Cartier scalars in the d=1 cell.

    Here r=p-3s-3, h=p-t=2s+1, and the selected offset after x^r is
    n=p-1-r=3s+2.  The factorizations are

      P0/x^r=(1-x)^(r-h)   (1-x^4)^h,
      P1/x^r=(1-x)^(r-h+1) (1-x^4)^(h-1).
    """
    if not (0 <= s <= (p - 3) // 3):
        raise ValueError((p, s))
    r = p - 3 * s - 3
    h = 2 * s + 1
    degree = 3 * s + 2
    gamma0 = four_section_coefficient(r - h, h, degree, p)
    gamma1 = four_section_coefficient(r - h + 1, h - 1, degree, p)
    return gamma0, gamma1


def classify_cell(m: int, p: int) -> dict[str, int]:
    a, r = divmod(6 * m, p)
    b, t = divmod(4 * m + 1, p)
    d = 2 * a - 3 * b
    return {"a": a, "b": b, "r": r, "t": t, "d": d}


def verify_cell_parameterizations(bound: int) -> dict[str, int]:
    counts = {"rank_two_d0": 0, "rank_one_d1": 0, "rank_zero_d2": 0}
    for p in primes_upto(bound):
        if p < 5:
            continue

        # d=0: (a,b)=(3j,2j), r=3s, t=2s+1, 2m=jp+s.
        for s in range((p - 1) // 3 + 1):
            for j in range(1, (p - 1) // 2 + 1):
                if (s - j) & 1 or (j == 1 and s == 0):
                    continue
                numerator = j * p + s
                if numerator & 1:
                    raise AssertionError(("d0 parity", p, j, s))
                m = numerator // 2
                row = classify_cell(m, p)
                expected = {"a": 3 * j, "b": 2 * j, "r": 3 * s, "t": 2 * s + 1, "d": 0}
                if row != expected or not (p < 2 * m and p <= 4 * m + 1 < p * p):
                    raise AssertionError(("d0", p, j, s, m, row, expected))
                counts["rank_two_d0"] += 1

        # d=1: (a,b)=(3j+2,2j+1), h=2s+1, r=p-3s-3.
        for s in range((p - 3) // 3 + 1):
            for j in range(1, (p - 3) // 2 + 1):
                if (s - j) & 1:
                    continue
                odd_value = (j + 1) * p - s
                if odd_value % 2 != 1:
                    raise AssertionError(("d1 parity", p, j, s))
                m = (odd_value - 1) // 2
                row = classify_cell(m, p)
                expected = {
                    "a": 3 * j + 2,
                    "b": 2 * j + 1,
                    "r": p - 3 * s - 3,
                    "t": p - 2 * s - 1,
                    "d": 1,
                }
                if row != expected or not (p < 2 * m and p <= 4 * m + 1 < p * p):
                    raise AssertionError(("d1", p, j, s, m, row, expected))
                if 3 * j + 1 >= p:
                    # This is the theorem's universal support inequality.
                    if not (6 * m >= p * (p + 1)):
                        raise AssertionError(("tail support", p, j, s, m))
                    if 2 * j + 3 > p:
                        raise AssertionError(("tail denominator", p, j, s))
                    for degree_h in range(1, 6):
                        residual_degree = p - 7 + degree_h
                        if residual_degree > p - 2:
                            raise AssertionError(("tail degree", p, j, degree_h))
                counts["rank_one_d1"] += 1

        # d=2: (a,b)=(3j+1,2j), h=2s, r=(p-6s-3)/2.
        for s in range(1, (p - 3) // 6 + 1):
            for j in range(1, (p - 1) // 2 + 1):
                numerator = (2 * j + 1) * p - 2 * s - 1
                if numerator % 4:
                    continue
                m = numerator // 4
                row = classify_cell(m, p)
                expected = {
                    "a": 3 * j + 1,
                    "b": 2 * j,
                    "r": (p - 6 * s - 3) // 2,
                    "t": p - 2 * s,
                    "d": 2,
                }
                if row != expected or not (p < 2 * m and p <= 4 * m + 1 < p * p):
                    raise AssertionError(("d2", p, j, s, m, row, expected))
                counts["rank_zero_d2"] += 1
    return counts


def interval_constants(truncation: int) -> dict[str, float]:
    rank_zero_sum = sum(
        6.0 / (3 * j + 1) - 4.0 / (2 * j + 1)
        for j in range(1, truncation + 1)
    )
    rank_one_sum = sum(
        6.0 / (3 * j + 2) - 2.0 / (j + 1)
        for j in range(1, truncation + 1)
    )
    rank_two_sum = sum(
        2.0 / j - 6.0 / (3 * j + 1)
        for j in range(1, truncation + 1)
    )
    root3 = math.sqrt(3.0)
    closed_rank_zero = -4 * math.log(2) + math.pi / root3 + 3 * math.log(3) - 2
    closed_rank_one = -1 - math.pi / root3 + 3 * math.log(3)
    closed_rank_two = 6 - math.pi / root3 - 3 * math.log(3)
    # All tails are O(1/truncation); this tolerance is intentionally loose.
    tolerance = 10.0 / truncation
    for partial, closed in (
        (rank_zero_sum, closed_rank_zero),
        (rank_one_sum, closed_rank_one),
        (rank_two_sum, closed_rank_two),
    ):
        if not (0 <= closed - partial < tolerance):
            raise AssertionError((partial, closed, tolerance))
    total = closed_rank_zero + closed_rank_one + closed_rank_two
    threshold = 1.1561471519642446123307302239
    return {
        "truncation": truncation,
        "rank_zero_partial": rank_zero_sum,
        "rank_zero_closed": closed_rank_zero,
        "rank_one_partial": rank_one_sum,
        "rank_one_closed": closed_rank_one,
        "rank_two_partial": rank_two_sum,
        "rank_two_closed_ceiling": closed_rank_two,
        "rank_at_most_two_radical_ceiling_per_m": total,
        "one_layer_ceiling_per_6m": total / 6,
        "three_complete_layers_ceiling_per_6m": total / 2,
        "three_layer_deficit_to_threshold_per_6m": threshold - total / 2,
        "threshold_per_6m": threshold,
    }


def scalar_zero_census(bound: int) -> dict[str, Any]:
    zeros = []
    balanced_rows = []
    for p in primes_upto(bound):
        if p < 5:
            continue
        for s in range((p - 3) // 3 + 1):
            gamma0, gamma1 = rank_one_scalars(p, s)
            balanced = p == 5 * s + 4
            balanced_forced_zero = balanced and s % 4 == 3
            if balanced:
                expected = gamma0 == 0 and ((gamma1 == 0) == (s % 4 == 3))
                if not expected:
                    raise AssertionError(("balanced four-section", p, s, gamma0, gamma1))
                balanced_rows.append(
                    {
                        "p": p,
                        "s": s,
                        "s_mod_4": s % 4,
                        "gamma0": gamma0,
                        "gamma1": gamma1,
                        "simultaneous_zero": gamma0 == gamma1 == 0,
                    }
                )
            if gamma0 == 0 and gamma1 == 0:
                zeros.append(
                    {
                        "p": p,
                        "s": s,
                        "balanced_four_section_ray": balanced_forced_zero,
                    }
                )
    return {
        "prime_bound": bound,
        "simultaneous_zero_count": len(zeros),
        "balanced_rows": balanced_rows,
        "simultaneous_zeros": zeros,
        "off_balanced_simultaneous_zeros": [
            row for row in zeros if not row["balanced_four_section_ray"]
        ],
        "interpretation": "EXACT_FINITE_CENSUS_ONLY",
    }


def square_ray_classification(bound: int) -> dict[str, Any]:
    """Check the four p mod 20 classes on 10m+1=p^2.

    The symbolic proof in the report uses only four-section support and
    nonvanishing of binomial coefficients whose arguments are below p.
    """
    rows = []
    for p in primes_upto(bound):
        if p in (2, 5) or p % 10 not in (1, 9):
            continue
        m = (p * p - 1) // 10
        if 10 * m + 1 != p * p:
            raise AssertionError(("square ray integrality", p, m))
        cell = classify_cell(m, p)
        residue = p % 20
        if residue in (9, 19):
            s = (p - 4) // 5
            j = s
            gamma0, gamma1 = rank_one_scalars(p, s)
            expected_both_zero = residue == 19
            if cell["d"] != 1 or gamma0 != 0 or ((gamma1 == 0) != expected_both_zero):
                raise AssertionError(("square d1", p, m, cell, gamma0, gamma1))
            status = (
                "PROVED_EXACT_V3_BY_ITEM167"
                if residue == 19
                else "RANK_ONE_BUT_NO_AUTOMATIC_SCALAR_ZERO"
            )
            rows.append(
                {
                    "p": p,
                    "p_mod_20": residue,
                    "m": m,
                    "d": 1,
                    "j": j,
                    "s": s,
                    "gamma0": gamma0,
                    "gamma1": gamma1,
                    "classification": status,
                }
            )
            continue

        if residue not in (1, 11):
            raise AssertionError(("unexpected prime residue", p, residue))
        s = (p - 1) // 5
        j = s
        if cell["d"] != 0:
            raise AssertionError(("square d0", p, m, cell))
        if residue == 11:
            # P0=x^(3s)(1-x^4)^(3s) and
            # P1=x^(3s)(1-x)(1-x^4)^(3s-1); at 2p-1 the
            # selected offset is 7s+1=3 (mod 4).
            determinant_zero = True
            status = "PROVED_RANK_TWO_DETERMINANT_ZERO_ONLY"
        else:
            # For s=0 mod 4, Delta=a0*b1 with the two displayed
            # nonzero binomial coefficients.
            a0 = pow(-1, s // 2, p) * math.comb(3 * s, s // 2) % p
            b1 = (
                -pow(-1, 7 * s // 4, p)
                * math.comb(3 * s - 1, 7 * s // 4)
            ) % p
            determinant_zero = (a0 * b1) % p == 0
            if determinant_zero:
                raise AssertionError(("square d0 nonzero", p, s, a0, b1))
            status = "PROVED_RANK_TWO_DETERMINANT_NONZERO"
        rows.append(
            {
                "p": p,
                "p_mod_20": residue,
                "m": m,
                "d": 0,
                "j": j,
                "s": s,
                "rank_two_determinant_zero": determinant_zero,
                "classification": status,
            }
        )
    counts: dict[str, int] = {}
    for row in rows:
        key = str(row["p_mod_20"])
        counts[key] = counts.get(key, 0) + 1
    return {
        "prime_bound": bound,
        "counts_by_p_mod_20": counts,
        "rows": rows,
        "scope_warning": (
            "Only p=19 mod 20 has a theorem-level exact content valuation; "
            "uniform deeper valuations in the 9 and 11 classes remain open."
        ),
    }


def frozen_cubic_census(item163_path: Path) -> dict[str, Any]:
    payload = json.loads(item163_path.read_text(encoding="utf-8"))
    survivors = []
    by_cell = {"d0_rank_two": 0, "d1_rank_one": 0, "d2_rank_zero": 0}
    rank_one_exact_tail_rows = []
    rank_zero_exact_tail_rows = []
    for row in payload["rows"]:
        m = int(row["m"])
        p = int(row["p"])
        cell = classify_cell(m, p)
        d = cell["d"]
        if d == 1:
            s1 = (p - cell["t"] - 1) // 2
            j1 = (cell["b"] - 1) // 2
            gamma0, gamma1 = rank_one_scalars(p, s1)
            if gamma0 == gamma1 == 0 and 3 * j1 + 1 >= p:
                if not bool(row["gates"]["p^3"]):
                    raise AssertionError(("frozen d1 exact tail", m, p, j1, s1))
                rank_one_exact_tail_rows.append(
                    {"m": m, "p": p, "j": j1, "s": s1, "p3_gate": True}
                )
        elif d == 2:
            j2 = cell["b"] // 2
            s2 = (p - cell["t"]) // 2
            if 3 * j2 >= p and 2 * j2 + 2 <= p:
                if not bool(row["gates"]["p^2"]):
                    raise AssertionError(("frozen d2 exact tail", m, p, j2, s2))
                rank_zero_exact_tail_rows.append(
                    {
                        "m": m,
                        "p": p,
                        "j": j2,
                        "s": s2,
                        "p2_gate": True,
                        "p3_gate": bool(row["gates"]["p^3"]),
                    }
                )

        if not bool(row["gates"]["p^3"]):
            continue
        if d == 0:
            label = "d0_rank_two"
            s = (cell["t"] - 1) // 2
            j = cell["b"] // 2
        elif d == 1:
            label = "d1_rank_one"
            s = (p - cell["t"] - 1) // 2
            j = (cell["b"] - 1) // 2
        elif d == 2:
            label = "d2_rank_zero"
            s = (p - cell["t"]) // 2
            j = cell["b"] // 2
        else:
            raise AssertionError((m, p, cell))
        by_cell[label] += 1
        structural_ray = d == 1 and p == 5 * s + 4 and s % 4 == 3
        exact_tail = structural_ray and 3 * j + 1 >= p
        square_ray = 10 * m + 1 == p * p
        survivors.append(
            {
                "m": m,
                "p": p,
                "d": d,
                "j": j,
                "s": s,
                "structural_p_divides_10m_plus_1_ray": structural_ray,
                "item164_exact_tail": exact_tail,
                "item167_prime_square_ray": square_ray,
                "other_finite_cancellation": not (exact_tail or square_ray),
            }
        )
    return {
        "input": str(item163_path.name),
        "input_sha256": sha256(item163_path),
        "scope": payload["scope"],
        "p3_survivor_count": len(survivors),
        "p3_survivors_by_cell": by_cell,
        "p3_survivors": survivors,
        "rank_one_exact_tail_rows": rank_one_exact_tail_rows,
        "rank_zero_exact_tail_rows": rank_zero_exact_tail_rows,
        "rank_zero_exact_tail_p3_survivors": sum(
            bool(row["p3_gate"]) for row in rank_zero_exact_tail_rows
        ),
        "interpretation": "FROZEN_EXACT_FINITE_REPLAY_ONLY",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell-prime-bound", type=int, default=149)
    parser.add_argument("--scalar-prime-bound", type=int, default=2000)
    parser.add_argument("--interval-truncation", type=int, default=200000)
    parser.add_argument("--item163", type=Path, default=DEFAULT_ITEM163)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    cell_counts = verify_cell_parameterizations(args.cell_prime_bound)
    constants = interval_constants(args.interval_truncation)
    scalar_census = scalar_zero_census(args.scalar_prime_bound)
    square_census = square_ray_classification(args.scalar_prime_bound)
    cubic_census = frozen_cubic_census(args.item163)

    output = {
        "schema": "item168-e1-forced-cell-third-layer-v1",
        "status": {
            "complete_e1_cell_parameterization": "PROVED_IN_COMPANION_REPORT",
            "automatic_second_Cartier_tail_small_support": "PROVED_IN_COMPANION_REPORT",
            "known_ray_thinness": "PROVED_IN_COMPANION_REPORT",
            "three_layer_capacity_no_go": "PROVED_IN_COMPANION_REPORT",
            "positive_mass_p3_family": "OPEN_NOT_FOUND",
            "finite_censuses": "EXACT_FINITE_DIAGNOSTICS_ONLY",
        },
        "parameters": {
            "cell_prime_bound": args.cell_prime_bound,
            "scalar_prime_bound": args.scalar_prime_bound,
            "interval_truncation": args.interval_truncation,
        },
        "cell_parameterization_replay_counts": cell_counts,
        "interval_mass_constants": constants,
        "rank_one_scalar_zero_census": scalar_census,
        "prime_square_ray_classification": square_census,
        "frozen_cubic_census": cubic_census,
        "proved_support_statements": {
            "automatic_tail": "d=1, gamma0=gamma1=0, 3j+1>=p implies p^3|c_m and p(p+1)<=6m",
            "rank_zero_tail": "d=2, 3j>=p, 2j+2<=p implies p^2|c_m and p(p+1)<=6m; p^3 does not follow from degree exactness alone",
            "mechanism_level_no_go": "factoring a new (u/Q)^p requires a-1>=p, hence p(p+1)<=6m and zero weighted radical mass",
            "balanced_four_section_ray": "p=5s+4 and s=3 mod 4 implies p|(10m+1)",
            "rank_two_known_rays": [
                "p=3s+4 implies p|(6m+4)",
                "p=5s+2 implies p|(10m+2)",
                "p=5s+1 implies p|(10m+1)",
            ],
            "scope_warning": "non-scalar lifted cancellations in all three cells remain open",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
