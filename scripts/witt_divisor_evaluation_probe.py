#!/usr/bin/env python3
"""Finite divisor-evaluation probe for the item-162 Bockstein route.

For every e=1 item-149 rank-one row in the extended Hasse census, construct
P0, P1, gamma0, gamma1, Theta, and T modulo p, then evaluate T at
0, 1, -1, i, -i.  Zero patterns and affine-line searches are diagnostics.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
from typing import Any


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiply_small(poly: list[int], base: list[int], p: int) -> list[int]:
    out = [0] * (len(poly) + len(base) - 1)
    for i, value in enumerate(poly):
        if value:
            for j, coefficient in enumerate(base):
                if coefficient:
                    out[i + j] = (out[i + j] + value * coefficient) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def sparse_power(base: list[int], exponent: int, p: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = multiply_small(out, base, p)
    return out


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    # Choose the shorter factor for the inner loop.
    if len(left) < len(right):
        right, left = left, right
    out = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        if value:
            for j, coefficient in enumerate(right):
                if coefficient:
                    out[i + j] = (out[i + j] + value * coefficient) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def evaluate_scalar(poly: list[int], value: int, p: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % p
    return out


def gmul(x: tuple[int, int], y: tuple[int, int], p: int) -> tuple[int, int]:
    return (x[0] * y[0] - x[1] * y[1]) % p, (
        x[0] * y[1] + x[1] * y[0]
    ) % p


def evaluate_gaussian(poly: list[int], value: tuple[int, int], p: int) -> tuple[int, int]:
    out = (0, 0)
    for coefficient in reversed(poly):
        out = gmul(out, value, p)
        out = ((out[0] + coefficient) % p, out[1])
    return out


def bockstein_row(m: int, p: int) -> dict[str, Any]:
    n, k0 = 6 * m, 4 * m + 1
    a, r = divmod(n, p)
    b, t = divmod(k0, p)
    if t == 0:
        raise AssertionError(("rank-one t=0", m, p))
    u_power = sparse_power([0, 1, -1], r, p)
    q_power_1 = sparse_power([1, 1, 1, 1], p - t - 1, p)
    p1 = multiply(u_power, q_power_1, p)
    p0 = multiply_small(p1, [1, 1, 1, 1], p)
    d0 = len(p0) - 1
    d1 = len(p1) - 1
    if d0 > 2 * p - 2 or d1 > 2 * p - 2:
        raise AssertionError(("not rank one", m, p, d0, d1))
    gamma0 = p0[p - 1] if p - 1 < len(p0) else 0
    gamma1 = p1[p - 1] if p - 1 < len(p1) else 0
    degree = max(len(p0), len(p1), p)
    theta = [0] * degree
    for j in range(degree):
        theta[j] = (
            gamma1 * (p0[j] if j < len(p0) else 0)
            - gamma0 * (p1[j] if j < len(p1) else 0)
        ) % p
    if theta[p - 1] != 0:
        raise AssertionError(("Theta coefficient", m, p, theta[p - 1]))
    primitive_t = [0] * (len(theta) + 1)
    for j, coefficient in enumerate(theta):
        if j == p - 1:
            if coefficient:
                raise AssertionError((m, p, j, coefficient))
            continue
        primitive_t[j + 1] = coefficient * pow(j + 1, -1, p) % p
    values = {
        "0": 0,
        "1": evaluate_scalar(primitive_t, 1, p),
        "-1": evaluate_scalar(primitive_t, -1, p),
        "i": list(evaluate_gaussian(primitive_t, (0, 1), p)),
        "-i": list(evaluate_gaussian(primitive_t, (0, -1), p)),
    }
    all_zero = (
        values["1"] == 0
        and values["-1"] == 0
        and values["i"] == [0, 0]
        and values["-i"] == [0, 0]
    )
    return {
        "a": a, "b": b, "r": r, "t": t, "h": b + 1,
        "degree_P0": d0, "degree_P1": d1,
        "gamma0": gamma0, "gamma1": gamma1,
        "T_values": values,
        "all_five_divisor_values_zero": all_zero,
        "bockstein_integrality_safe": b + 1 <= p - 1,
    }


def line_search(rows: list[dict[str, Any]], field: str, minimum: int = 3) -> list[dict[str, Any]]:
    candidates = []
    for denominator in range(1, 13):
        for numerator in range(1, 2 * denominator):
            if math.gcd(numerator, denominator) != 1:
                continue
            groups: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
            for row in rows:
                groups[denominator * row["p"] - numerator * row["m"]].append(row)
            for intercept, group in groups.items():
                if len(group) >= minimum and all(bool(row[field]) for row in group):
                    candidates.append({
                        "equation": f"{denominator}*p={numerator}*m+({intercept})",
                        "point_count": len(group),
                        "points": sorted([row["m"], row["p"]] for row in group),
                    })
    candidates.sort(key=lambda row: (-row["point_count"], row["equation"]))
    return candidates


def in_proved_congruence_slab(row: dict[str, Any]) -> bool:
    """The support-zero family proved in the item-162 companion note."""
    m, p = int(row["m"]), int(row["p"])
    return (
        p % 20 == 19
        and (10 * m + 1) % p == 0
        and int(row["e"]) == 1
        and int(row["delta"]) == 0
        and p <= 4 * m + 1 < p * p
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--census",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "lifted_endpoint_hasse_extended_census_m100.json",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    census = json.loads(args.census.read_text(encoding="utf-8"))
    rows = []
    implications_fail = []
    for source_row in census["rows"]:
        if (
            source_row["e"] != 1
            or source_row["delta"] != 0
            or "rank_one" not in source_row["source"]
        ):
            continue
        row = {**source_row, **bockstein_row(source_row["m"], source_row["p"])}
        # When the sufficient integrality condition holds, vanishing at all
        # divisor points forces the determinant wedge to vanish.
        if (
            row["bockstein_integrality_safe"]
            and row["all_five_divisor_values_zero"]
            and row["eta"] != 0
        ):
            implications_fail.append([row["m"], row["p"], row["eta"]])
        rows.append(row)
    if implications_fail:
        raise AssertionError(("Bockstein/Hasse mismatch", implications_fail[:5]))

    safe = [row for row in rows if row["bockstein_integrality_safe"]]
    all_t_zero = [row for row in safe if row["all_five_divisor_values_zero"]]
    eta_zero = [row for row in safe if row["eta"] == 0]
    proved_slab = [row for row in safe if in_proved_congruence_slab(row)]
    slab_failures = [
        row for row in proved_slab
        if not row["all_five_divisor_values_zero"]
        or row["gamma0"] != 0
        or row["gamma1"] != 0
        or row["eta"] != 0
    ]
    if slab_failures:
        raise AssertionError(("proved congruence-slab mismatch", slab_failures[:5]))
    output = {
        "schema": "mixed-cubic-witt-divisor-evaluation-probe-v1",
        "status": {
            "Bockstein_formula": "PROVED_IN_COMPANION_NOTE",
            "finite_evaluation_census": "EXPERIMENTAL_EXACT_FINITE_ONLY",
            "congruence_slab_family": "PROVED_IN_ITEM_162_COMPANION_NOTE",
            "unrefined_affine_line_search": "EXPERIMENTAL_NO_UNIFORM_LINE_FOUND",
        },
        "inputs": {args.census.name: sha256(args.census)},
        "summary": {
            "e1_non_rank_zero_rank_one_rows_evaluated": len(rows),
            "integrality_safe_rows": len(safe),
            "safe_rows_with_eta_zero": len(eta_zero),
            "safe_rows_with_all_T_divisor_values_zero": len(all_t_zero),
            "all_T_zero_but_eta_nonzero_mismatches": len(implications_fail),
            "eta_zero_rows_not_explained_by_all_T_zero": len(
                [row for row in eta_zero if not row["all_five_divisor_values_zero"]]
            ),
            "proved_congruence_slab_rows": len(proved_slab),
            "proved_congruence_slab_failures": len(slab_failures),
            "all_T_zero_rows_outside_proved_slab": len(
                [row for row in all_t_zero if not in_proved_congruence_slab(row)]
            ),
        },
        "all_T_zero_rows": all_t_zero,
        "proved_congruence_slab_rows": proved_slab,
        "all_T_zero_affine_line_search": {
            "status": "EXPERIMENTAL_FINITE_SEARCH_ONLY",
            "candidates": line_search(safe, "all_five_divisor_values_zero"),
        },
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output["summary"], indent=2, sort_keys=True))
    print(json.dumps({
        "all_T_zero_affine_candidate_count": len(output["all_T_zero_affine_line_search"]["candidates"])
    }))


if __name__ == "__main__":
    main()
