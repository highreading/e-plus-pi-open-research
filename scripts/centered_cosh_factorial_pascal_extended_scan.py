#!/usr/bin/env python3
"""Extended exact diagnostic for the factorial-Pascal endpoint model.

The frozen theorem/certificate covers q <= 12.  This resumable diagnostic
starts at q=13 and records raw Pascal-kernel size, endpoint content, final
primitive height, and the rational approximation error.  Its finite rows
are evidence only and are never promoted to an asymptotic theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import resource
import sys
from pathlib import Path

import mpmath as mp
from flint import fmpz, fmpz_mat


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/centered_cosh_factorial_pascal_extended_scan.json"
SCHEMA = "centered_cosh_factorial_pascal_extended_scan/v1"
MIN_Q = 13
RSS_GUARD_KIB = 12 * 1024 * 1024

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def vector_sha256(values: list[int]) -> str:
    payload = ",".join(str(value) for value in values).encode()
    return hashlib.sha256(payload).hexdigest()


def load_rows() -> list[dict[str, object]]:
    if not OUTPUT.exists():
        return []
    data = json.loads(OUTPUT.read_text())
    assert data["schema"] == SCHEMA
    rows = data["rows"]
    assert [row["q"] for row in rows] == sorted(
        {row["q"] for row in rows}
    )
    return rows


def save_rows(rows: list[dict[str, object]], requested_end: int) -> None:
    payload = {
        "schema": SCHEMA,
        "logical_scope": (
            "Finite exact diagnostic beyond the frozen q<=12 grid.  "
            "No asymptotic content, height, or e+pi claim is inferred."
        ),
        "certified_grid_not_recomputed": "q <= 12",
        "requested_q_min": MIN_Q,
        "requested_q_max": requested_end,
        "rss_guard_kib": RSS_GUARD_KIB,
        "guard_is_not_an_allocation_or_colab_ram_cap": True,
        "rows": rows,
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def pascal_kernel(q: int) -> list[int]:
    matrix = fmpz_mat([
        [
            (-1 if i % 2 else 1) * math.comb(2 * (q + r), 2 * i)
            for i in range(q + 1)
        ]
        for r in range(1, q + 1)
    ])
    basis, nullity = matrix.nullspace()
    assert nullity == 1
    values = [int(basis[i, 0]) for i in range(q + 1)]
    if values[0] < 0:
        values = [-value for value in values]
    assert all(value > 0 for value in values)
    assert all(
        sum(
            (-1 if i % 2 else 1)
            * math.comb(2 * (q + r), 2 * i)
            * values[i]
            for i in range(q + 1)
        )
        == 0
        for r in range(1, q + 1)
    )
    return values


def endpoint_row(
    q: int,
    euler: list[int],
    square_euler: list[int],
) -> dict[str, object]:
    d = pascal_kernel(q)
    d_content = math.gcd(*d)
    e = [
        sum(
            (-1 if (k - i) % 2 else 1)
            * math.comb(2 * k, 2 * i)
            * d[i]
            for i in range(k + 1)
        )
        for k in range(q + 1)
    ]
    assert all(
        (value > 0 if k % 2 == 0 else value < 0)
        for k, value in enumerate(e)
    )

    def w(m: int) -> int:
        first = 2 * sum(
            math.comb(2 * m, 2 * i) * d[i] * euler[m - i]
            for i in range(q + 1)
        )
        second = sum(
            math.comb(2 * m, 2 * k) * e[k] * square_euler[m - k]
            for k in range(q + 1)
        )
        return first - second

    w_even = w(4 * q)
    w_odd = w(4 * q + 1)
    assert w_even > 0 and w_odd > 0
    raw_even = (8 * q + 2) * (8 * q + 1) * w_even
    raw_odd = w_odd
    endpoint_content = math.gcd(raw_even, raw_odd)
    primitive_even = raw_even // endpoint_content
    primitive_odd = raw_odd // endpoint_content
    assert math.gcd(primitive_even, primitive_odd) == 1

    height = max(primitive_even, primitive_odd)
    raw_height = max(raw_even, raw_odd)
    rational = mp.mpf(primitive_odd) / primitive_even
    target = 4 / (mp.pi * mp.pi)
    error = abs(rational - target)
    assert error > 0

    return {
        "q": q,
        "pascal_kernel_sha256": vector_sha256(d),
        "binomial_transform_sha256": vector_sha256(e),
        "pascal_kernel_content": str(d_content),
        "pascal_kernel_content_bits": d_content.bit_length(),
        "max_pascal_cofactor_bits": max(d).bit_length(),
        "raw_endpoint_height_bits": raw_height.bit_length(),
        "endpoint_content_bits": endpoint_content.bit_length(),
        "primitive_height_bits": height.bit_length(),
        "log_max_pascal_cofactor_over_q_squared": mp.nstr(
            mp.log(max(d)) / (q * q), 30
        ),
        "log_raw_endpoint_height_over_q_squared": mp.nstr(
            mp.log(raw_height) / (q * q), 30
        ),
        "log_endpoint_content_over_q_log_q": mp.nstr(
            mp.log(endpoint_content) / (q * mp.log(q)), 30
        ),
        "log_primitive_height_over_q_squared": mp.nstr(
            mp.log(height) / (q * q), 30
        ),
        "minus_log_ratio_error_over_q": mp.nstr(
            -mp.log(error) / q, 30
        ),
        "primitive_even_sha256": hashlib.sha256(
            str(primitive_even).encode()
        ).hexdigest(),
        "primitive_odd_sha256": hashlib.sha256(
            str(primitive_odd).encode()
        ).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--end", type=int, default=100)
    args = parser.parse_args()
    assert args.end >= MIN_Q

    mp.mp.dps = max(100, 5 * args.end + 100)
    top = 4 * args.end + 1
    euler = [abs(int(fmpz.euler_number(2 * j))) for j in range(top + 1)]
    square_euler = [
        sum(
            math.comb(2 * j, 2 * a) * euler[a] * euler[j - a]
            for a in range(j + 1)
        )
        for j in range(top + 1)
    ]

    rows = load_rows()
    completed = {int(row["q"]) for row in rows}
    for q in range(MIN_Q, args.end + 1):
        if q in completed:
            continue
        row = endpoint_row(q, euler, square_euler)
        rows.append(row)
        rows.sort(key=lambda item: int(item["q"]))
        save_rows(rows, args.end)
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        assert rss < RSS_GUARD_KIB, rss
        print(
            f"q={q} primitive_bits={row['primitive_height_bits']} "
            f"content_bits={row['endpoint_content_bits']} "
            f"peak_rss_kib={rss}",
            flush=True,
        )

    save_rows(rows, args.end)


if __name__ == "__main__":
    main()
