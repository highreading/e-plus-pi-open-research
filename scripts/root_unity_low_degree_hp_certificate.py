#!/usr/bin/env python3
"""Exact certificate for the root-of-unity low-degree HP audit.

All rank, null-vector, content, and tangent-number calculations are exact.
Decimal endpoint values are diagnostics and are emitted as fixed precision
strings; no numerical observation is used as a proof of a rank statement.
"""

from __future__ import annotations

import hashlib
import json
import math
from functools import lru_cache, reduce
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_low_degree_hp_certificate.json"


def gcd_many(values: list[int]) -> int:
    nonzero = [abs(x) for x in values if x]
    return reduce(math.gcd, nonzero) if nonzero else 0


def primitive_integer_vector(v: sp.Matrix) -> list[int]:
    den = 1
    for x in v:
        den = sp.ilcm(den, int(x.q))
    out = [int(x * den) for x in v]
    content = gcd_many(out)
    out = [x // content for x in out]
    first = next(x for x in out if x)
    if first < 0:
        out = [-x for x in out]
    return out


def constrained_matrix(m: int, n: int, d: int, jet_rows: int) -> sp.Matrix:
    """Rows for jets R^(k)(0), followed by the high S coefficients."""
    variables = [(j, r) for j in range(m + 1) for r in range(n + 1)]
    rows: list[list[int]] = []
    for k in range(jet_rows):
        row = []
        for j, r in variables:
            if r > k:
                row.append(0)
            else:
                row.append(math.factorial(r) * math.comb(k, r) * j ** (k - r))
        rows.append(row)
    for r0 in range(d + 1, n + 1):
        rows.append([(-1) ** j if r == r0 else 0 for j, r in variables])
    return sp.Matrix(rows)


@lru_cache(maxsize=None)
def exact_form(m: int, n: int, d: int) -> dict:
    u = (m + 1) * (n + 1)
    dimension = m * (n + 1) + d + 1
    expected_order = dimension - 1
    matrix = constrained_matrix(m, n, d, expected_order)
    kernel = matrix.nullspace()
    rank = u - len(kernel)
    if len(kernel) != 1:
        return {
            "m": m,
            "n": n,
            "D": d,
            "ambient_dimension": u,
            "constrained_dimension": dimension,
            "expected_order": expected_order,
            "full_constraint_rank": rank,
            "restricted_jet_rank": rank - (n - d),
            "nullity": len(kernel),
        }
    coeff = primitive_integer_vector(kernel[0])
    s_coeff = []
    for r in range(d + 1):
        s_coeff.append(sum((-1) ** j * coeff[j * (n + 1) + r] for j in range(m + 1)))
    s_content = gcd_many(s_coeff)
    s_primitive = [x // s_content for x in s_coeff]
    if next(x for x in s_primitive if x) < 0:
        s_primitive = [-x for x in s_primitive]
    variables = [(j, r) for j in range(m + 1) for r in range(n + 1)]
    def jet(k: int) -> int:
        return sum(
            coeff[index] * math.factorial(r) * math.comb(k, r) * j ** (k - r)
            for index, (j, r) in enumerate(variables)
            if r <= k
        )

    next_jet = jet(expected_order)
    bonus = next_jet == 0
    next_rank = rank if bonus else rank + 1
    actual_order = next(k for k in range(expected_order, u + 1) if jet(k) != 0)
    return {
        "m": m,
        "n": n,
        "D": d,
        "ambient_dimension": u,
        "constrained_dimension": dimension,
        "expected_order": expected_order,
        "full_constraint_rank": rank,
        "restricted_jet_rank": rank - (n - d),
        "nullity": 1,
        "full_rank_with_next_jet": next_rank,
        "one_order_bonus": bonus,
        "predicted_bonus": bool(m % 2 and n % 2 and d % 2 == 0),
        "actual_order": actual_order,
        "predicted_actual_order": expected_order + int(bool(m % 2 and n % 2 and d % 2 == 0)),
        "full_vector_height": max(abs(x) for x in coeff),
        "S_content_inside_full_vector": s_content,
        "S_primitive": s_primitive,
        "S_primitive_height": max(abs(x) for x in s_primitive),
    }


def tangent_number(r: int) -> int:
    # tau_r is the positive coefficient in tan(z):
    # tan(z)=sum_{r>=1} tau_r*z^(2r-1)/(2r-1)!.
    b = sp.bernoulli(2 * r)
    value = (-1) ** (r - 1) * 2 ** (2 * r) * (2 ** (2 * r) - 1) * b / (2 * r)
    assert value.q == 1 and value > 0
    return int(value)


def d2_tangent_row(r: int) -> dict:
    t0 = tangent_number(r)
    t1 = tangent_number(r + 1)
    raw_p = 8 * r * (2 * r + 1) * t0
    raw_q = t1
    common = math.gcd(raw_p, raw_q)
    p = raw_p // common
    q = raw_q // common
    mp.mp.dps = 100
    endpoint = abs(mp.mpf(p) - mp.mpf(q) * mp.pi**2)
    scaled_ratio = endpoint / (mp.mpf(q) * mp.power(9, -r))
    consecutive_gcd = math.gcd(t0, t1)
    odd_gcd = consecutive_gcd
    while odd_gcd % 2 == 0:
        odd_gcd //= 2
    return {
        "r": r,
        "tau_r": t0,
        "tau_r_plus_1": t1,
        "raw_gcd": common,
        "P": p,
        "Q": q,
        "primitive_endpoint_abs": mp.nstr(endpoint, 45),
        "endpoint_over_Q_times_9_to_minus_r": mp.nstr(scaled_ratio, 35),
        "odd_part_gcd_consecutive_tangent_numbers": odd_gcd,
    }


def m1_hankel_checks(max_size: int = 5, max_shift: int = 8) -> list[dict]:
    # Remove harmless positive powers of pi from u_r.  The rational signed
    # coefficients themselves suffice: u_r=tau_r/(2^(2r)(2r-1)!).
    def u(r: int) -> sp.Rational:
        return sp.Rational(tangent_number(r), 2 ** (2 * r) * math.factorial(2 * r - 1))

    rows = []
    for size in range(1, max_size + 1):
        for shift in range(1, max_shift + 1):
            h = sp.Matrix([[u(shift + i + j) for j in range(size)] for i in range(size)])
            det = sp.factor(h.det())
            assert det > 0
            rows.append(
                {
                    "size": size,
                    "shift": shift,
                    "det_numerator": int(det.p),
                    "det_denominator": int(det.q),
                    "positive": True,
                }
            )
    return rows


def endpoint_diagnostic(m: int, n: int, d: int) -> dict:
    row = exact_form(m, n, d)
    coeff = row["S_primitive"]
    mp.mp.dps = 140
    value = abs(sum(mp.mpf(a) * (1j * mp.pi) ** r for r, a in enumerate(coeff)))
    height = row["S_primitive_height"]
    return {
        "m": m,
        "n": n,
        "D": d,
        "S_primitive": coeff,
        "height": height,
        "endpoint_abs": mp.nstr(value, 50),
        "log_endpoint_over_height": mp.nstr(mp.log(value / height), 35),
    }


def diagonal_lambert_row(n: int) -> dict:
    b = [
        math.factorial(2 * n - 2 * j)
        // (math.factorial(2 * j) * math.factorial(n - 2 * j))
        for j in range(n // 2 + 1)
    ]
    content = gcd_many(b)
    predicted_content = 1 if n % 2 == 0 else n * (n + 1)
    assert content == predicted_content
    primitive = [x // content for x in b]
    assert primitive[0] == max(primitive)
    mp.mp.dps = 120
    endpoint = abs(sum(mp.mpf(a) * (-mp.pi**2) ** j for j, a in enumerate(primitive)))
    return {
        "n": n,
        "even_part_coefficients_before_content": b,
        "content": content,
        "predicted_content": predicted_content,
        "primitive_coefficients_in_z_squared": primitive,
        "height": primitive[0],
        "endpoint_abs": mp.nstr(endpoint, 45),
        "log_height_over_n_log_n": mp.nstr(
            mp.log(primitive[0]) / (n * mp.log(n)) if n > 1 else mp.mpf(0), 30
        ),
        "log_endpoint_over_n_log_n": mp.nstr(
            mp.log(endpoint) / (n * mp.log(n)) if n > 1 else mp.mpf(0), 30
        ),
    }


def main() -> None:
    grid = []
    failures = []
    for m in range(1, 5):
        for n in range(1, 9):
            for d in range(0, min(4, n) + 1):
                row = exact_form(m, n, d)
                grid.append(row)
                ok = (
                    row["full_constraint_rank"] == row["ambient_dimension"] - 1
                    and row["restricted_jet_rank"] == row["expected_order"]
                    and row["nullity"] == 1
                    and row["one_order_bonus"] == row["predicted_bonus"]
                    and row["actual_order"] == row["predicted_actual_order"]
                )
                if not ok:
                    failures.append({"m": m, "n": n, "D": d})

    d1_failures = []
    for row in grid:
        if row["D"] != 1:
            continue
        s = row["S_primitive"]
        expected = [1, 0] if (row["m"] % 2 and row["n"] % 2) else [0, 1]
        if s != expected:
            d1_failures.append({"m": row["m"], "n": row["n"], "actual": s})

    tangent_rows = [d2_tangent_row(r) for r in range(1, 181)]
    odd_common = [
        {"r": row["r"], "odd_part": row["odd_part_gcd_consecutive_tangent_numbers"]}
        for row in tangent_rows
        if row["odd_part_gcd_consecutive_tangent_numbers"] != 1
    ]

    diagnostics = []
    for m in range(1, 5):
        for d in (2, 4):
            for n in (max(d, 4), 8, 12):
                diagnostics.append(endpoint_diagnostic(m, n, d))

    payload = {
        "schema": "root-unity-low-degree-hp-certificate-v1",
        "all_exact_rank_checks_passed": not failures,
        "rank_failures": failures,
        "rank_grid": grid,
        "all_D1_monomial_checks_passed": not d1_failures,
        "D1_failures": d1_failures,
        "m1_hankel_positive_determinants": m1_hankel_checks(),
        "D2_tangent_rows": tangent_rows,
        "nontrivial_odd_gcds_through_r_180": odd_common,
        "endpoint_diagnostics": diagnostics,
        "diagonal_Lambert_rows": [diagonal_lambert_row(n) for n in range(1, 31)],
        "claims": {
            "rank_grid": "exact over Q",
            "D1_grid": "exact over Q",
            "hankel_grid": "exact rational positivity",
            "D2_P_Q_and_gcd": "exact integers",
            "endpoint_decimals": "diagnostic only",
        },
    }
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUT.write_bytes(encoded)
    print(f"wrote {OUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"rank rows {len(grid)}; failures {len(failures)}")
    print(f"odd consecutive-tangent gcd exceptions {odd_common}")


if __name__ == "__main__":
    main()
