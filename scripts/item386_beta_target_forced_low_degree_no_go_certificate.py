#!/usr/bin/env python3
"""Deterministic controls for Item 386.

The output is EXACT FINITE ONLY.  General theorems are proved in the report.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def beta_q(n_max: int) -> list[int]:
    q = [1, 1]
    for n in range(2, n_max + 1):
        q.append((4 * n - 2) * q[-1] + q[-2])
    return q


def weights(n: int) -> tuple[int, int, dict[int, int]]:
    m = n - 2
    A = 4 * n - 2
    w = {1: 7}
    for j in range(2, m + 1):
        w[j] = 4 * j + 2
    w[m + 1] = A
    return m, A, w


def endpoint_coefficient(n: int) -> int:
    m, _, w = weights(n)
    c_prev = 1
    c_cur = w[2]
    if m + 1 == 2:
        return c_cur
    for j in range(2, m + 1):
        c_prev, c_cur = c_cur, w[j + 1] * c_cur + c_prev
    return c_cur


def endpoint_value(n: int, digits: dict[int, int]) -> int:
    m, _, w = weights(n)
    e_prev = 0
    e_cur = digits[1]
    for j in range(1, m + 1):
        d_next = digits.get(j + 1, 0)
        e_prev, e_cur = (
            e_cur,
            w[j + 1] * e_cur + e_prev + ((-1) ** j) * d_next,
        )
    return e_cur


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    d = 3
    while d * d <= p:
        if p % d == 0:
            return False
        d += 2
    return True


def elementary(values: list[int], modulus: int | None = None) -> list[int]:
    e = [1] + [0] * len(values)
    for value in values:
        for j in range(len(values), 0, -1):
            e[j] += value * e[j - 1]
            if modulus is not None:
                e[j] %= modulus
    return e


def reconstruct_target_point(
    n: int,
    p: int,
    sigma: int,
    d2: int,
    loads: dict[int, int],
) -> dict[str, object]:
    q = beta_q(n)
    a = q[n - 1]
    b = q[n]
    m, A, w = weights(n)
    assert b % p == 0 and p > A and is_prime(p)
    digits = {2: d2 % p, m + 1: 0}
    for j in range(3, m + 1):
        digits[j] = (w[j] * digits[j - 1] - loads[j]) % p
    digits[1] = 0
    rest = endpoint_value(n, digits) % p
    coeff = endpoint_coefficient(n) % p
    assert coeff != 0
    digits[1] = ((sigma * a - rest) * pow(coeff, -1, p)) % p
    endpoint = endpoint_value(n, digits) % p
    recovered = {
        j: (w[j] * digits[j - 1] - digits[j]) % p
        for j in range(3, m + 1)
    }
    assert endpoint == (sigma * a) % p
    assert recovered == {j: value % p for j, value in loads.items()}
    return {
        "n": n,
        "p": p,
        "A": A,
        "b_divisible": b % p == 0,
        "endpoint_unit": coeff,
        "sigma": sigma,
        "d2": d2,
        "digits_mod_p": [digits[j] for j in range(1, m + 1)],
        "loads_mod_p": [recovered[j] for j in range(3, m + 1)],
        "endpoint_mod_p": endpoint,
        "target_mod_p": (sigma * a) % p,
    }


def symmetric_chart(loads: list[int], hit: int, p: int) -> dict[str, object]:
    z = [value % p for value in loads]
    assert z[hit] == 0
    outside = [value for i, value in enumerate(z) if i != hit]
    assert all(value != 0 for value in outside)
    n_loads = len(z)
    ez = elementary(z, p)
    top = {s: ez[n_loads - s] for s in range(1, min(3, n_loads) + 1)}
    assert top[1] != 0
    inv = [pow(value, -1, p) for value in outside]
    einv = elementary(inv, p)
    ratios = {}
    for s, value in top.items():
        ratios[s] = value * pow(top[1], -1, p) % p
        assert ratios[s] == einv[s - 1] % p
    g_control_values = [p] + outside
    integer_e = elementary(g_control_values)
    integer_top = [integer_e[n_loads - s] for s in range(1, min(3, n_loads) + 1)]
    gcd_top = 0
    for value in integer_top:
        gcd_top = math.gcd(gcd_top, value)
    assert integer_top[0] % p != 0
    assert gcd_top % p != 0
    return {
        "p": p,
        "hit_index": hit,
        "outside_mod_p": outside,
        "top_symmetric_mod_p": top,
        "normalized_ratios_mod_p": ratios,
        "outside_reciprocal_elementaries_mod_p": einv[:3],
        "integer_top_gcd_control": gcd_top,
        "p_divides_integer_top_gcd": gcd_top % p == 0,
    }


def split_line_control(length: int, p: int) -> dict[str, object]:
    assert length >= 2
    y0 = [1] * length
    y1 = [1] * (length - 1) + [pow(2, -1, p)]
    # Use outside loads z, not reciprocals, for the exact T2-L*T1 example.
    z0 = [1] * length
    z1 = [1] * (length - 1) + [2]
    e0 = elementary(z0, p)
    e1 = elementary(z1, p)
    t10, t20 = e0[length], e0[length - 1]
    t11, t21 = e1[length], e1[length - 1]
    f0 = (t20 - length * t10) % p
    f1 = (t21 - length * t11) % p
    assert f0 == 0 and f1 == p - 1
    assert elementary(y0, p)[1] == length % p
    assert elementary(y1, p)[1] == (length - 1 + pow(2, -1, p)) % p
    return {
        "outside_count": length,
        "prime": p,
        "line": f"T2-{length}*T1",
        "all_one_value_mod_p": f0,
        "one_two_value_mod_p": f1,
        "conclusion": "the displayed split line can hold and fail on the same formal singleton torus",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    q = beta_q(25)
    bridge_rows = []
    for n in range(5, 13):
        a, b = q[n - 1], q[n]
        coeff = endpoint_coefficient(n)
        numerator = a * coeff - ((-1) ** n)
        assert numerator % b == 0
        s = numerator // b
        assert a * coeff == b * s + ((-1) ** n)
        assert math.gcd(coeff, b) == 1
        bridge_rows.append(
            {
                "n": n,
                "a": a,
                "b": b,
                "endpoint_coefficient": coeff,
                "bridge_S": s,
                "gcd_coefficient_b": 1,
            }
        )

    declared = [
        (5, 18089),
        (6, 36269),
        (7, 10391023),
        (8, 1846921),
        (9, 1913),
        (10, 6151),
        (15, 691),
    ]
    prime_rows = []
    for n, p in declared:
        m, A, _ = weights(n)
        coeff = endpoint_coefficient(n)
        assert is_prime(p) and q[n] % p == 0 and p > A and coeff % p != 0
        prime_rows.append(
            {
                "n": n,
                "p": p,
                "A": A,
                "active_load_count": m - 2,
                "p_divides_b": True,
                "endpoint_coefficient_is_unit": True,
                "mesoscopic": p < A * A,
            }
        )

    n = 15
    p = 691
    m, _, _ = weights(n)
    loads = {j: (3 * j + 5) % p or 1 for j in range(3, m + 1)}
    hit_j = 8
    loads[hit_j] = 0
    target_points = [
        reconstruct_target_point(n, p, 1, 17, loads),
        reconstruct_target_point(n, p, -1, 29, loads),
    ]
    load_vector = [loads[j] for j in range(3, m + 1)]
    chart = symmetric_chart(load_vector, hit_j - 3, p)
    split = split_line_control(len(load_vector) - 1, p)

    payload = {
        "artifact": "item386_beta_target_forced_low_degree_no_go_certificate",
        "classification": "EXACT FINITE ONLY",
        "general_claims_from_finite_data": False,
        "bridge_rows": bridge_rows,
        "declared_prime_rows": prime_rows,
        "formal_target_singleton_points": target_points,
        "symmetric_chart_control": chart,
        "split_line_variation_control": split,
        "proved_by_report_not_by_scan": [
            "all-power endpoint load-coordinate freedom",
            "top-symmetric projective algebraic independence",
            "torus nonvanishing when d(k-1)<p-1",
            "exact actual coprimality of U_1,1 with every coordinate gcd",
            "zero incremental capacity of target-forced low-degree forms",
        ],
        "searches_performed": {
            "actual_target_search": False,
            "prime_census": False,
            "factor_search": False,
            "half_bound_scan": False,
        },
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    Path(args.output).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

