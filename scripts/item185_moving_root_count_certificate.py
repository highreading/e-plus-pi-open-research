#!/usr/bin/env python3
"""Exact diagnostics for the Item185 moving-root-count problem."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULT_NAME = "item185_moving_root_count_certificate.json"


def default_output() -> Path:
    return HERE / RESULT_NAME if HERE.name.lower() == "work" else HERE.parent / "results" / RESULT_NAME


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * ((limit - q * q) // q + 1)
    return [p for p in range(7, limit + 1) if sieve[p]]


def coefficients_mod_p(p: int, s: int) -> list[int]:
    a = [0] * p
    a[0] = 1
    for n in range(p - 1):
        rhs = (n - 5 * s - 2) * a[n]
        if n >= 3:
            rhs += (n + 8 * s + 5) * a[n - 3]
        if n >= 4:
            rhs -= (n + 3 * s + 2) * a[n - 4]
        a[n + 1] = rhs * pow(n + 1, -1, p) % p
    return a


def data_from_coefficients(p: int, s: int, a: list[int]) -> dict:
    d = p - 3 * s
    sign = p - 1 if s & 1 else 1
    low_sum = sum(a[d - j] if d - j >= 0 else 0 for j in (2, 3, 4)) % p
    high_sum = sum(a[p - j] for j in (4, 3, 2)) % p
    determinant = sign * (low_sum * a[p - 5] - high_sum * a[d - 1]) % p
    return {
        "determinant": determinant,
        "low_sum": low_sum,
        "low_pivot": a[d - 1],
        "high_sum": high_sum,
        "high_pivot": a[p - 5],
    }


def known_ray_labels(p: int, s: int) -> list[str]:
    labels = []
    if p == 3 * s + 4:
        labels.append("p=3s+4")
    if p == 5 * s + 2 and s % 4 == 1:
        labels.append("p=5s+2,s=1(mod4)")
    if p == 5 * s + 1 and s % 4 == 2:
        labels.append("p=5s+1,s=2(mod4)")
    return labels


def interpolation_degree(values: list[int], p: int) -> int:
    row = values[:]
    for order in range(len(values)):
        if all(x % p == 0 for x in row):
            return order - 1
        row = [(row[j + 1] - row[j]) % p for j in range(len(row) - 1)]
    return len(values) - 1


def matrix_rank_mod_p(matrix: list[list[int]], p: int) -> int:
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col] % p, -1, p)
        a[rank][col:] = [x * inv % p for x in a[rank][col:]]
        for r in range(rank + 1, rows):
            if a[r][col]:
                factor = a[r][col]
                a[r][col:] = [(x - factor * y) % p for x, y in zip(a[r][col:], a[rank][col:])]
        rank += 1
        if rank == rows:
            break
    return rank


def normalization_record(p: int) -> dict:
    count = (p - 1) // 3 + 1
    raw: list[int] = []
    gamma_mul: list[int] = []
    gamma_div: list[int] = []
    ratio_data: list[tuple[int, int]] = []
    roots = []
    structural = []
    factorial = 1
    for s in range(count):
        if s:
            factorial = factorial * (2 * s) * (2 * s + 1) % p
        a = coefficients_mod_p(p, s)
        datum = data_from_coefficients(p, s, a)
        value = datum["determinant"]
        raw.append(value)
        gamma_mul.append(value * factorial * factorial % p)
        gamma_div.append(value * pow(factorial, -2, p) % p)
        if value == 0:
            roots.append(s)
            labels = known_ray_labels(p, s)
            if labels:
                structural.append({"s": s, "labels": labels})
        lp, hp = datum["low_pivot"], datum["high_pivot"]
        if lp and hp:
            normalized = (
                datum["low_sum"] * pow(lp, -1, p)
                - datum["high_sum"] * pow(hp, -1, p)
            ) % p
            ratio_data.append((s, normalized))

    raw_degree = interpolation_degree(raw, p)
    gamma_mul_degree = interpolation_degree(gamma_mul, p)
    gamma_div_degree = interpolation_degree(gamma_div, p)
    # If the interpolation polynomial vanishes at q distinct structural nodes,
    # exact division by their linear factors lowers its degree by exactly q.
    residual_degree = raw_degree - len(structural)

    excluded_degree = len(ratio_data) // 2 - 1
    columns = 2 * (excluded_degree + 1)
    rational_matrix = []
    for s, value in ratio_data:
        powers = [1]
        for _ in range(excluded_degree):
            powers.append(powers[-1] * s % p)
        rational_matrix.append(powers + [(-value * x) % p for x in powers])
    rational_rank = matrix_rank_mod_p(rational_matrix, p)
    assert rational_rank == columns

    return {
        "p": p,
        "admissible_point_count": count,
        "roots": roots,
        "structural_roots": structural,
        "raw_interpolation_degree": raw_degree,
        "degree_after_exact_structural_linear_factor_removal": residual_degree,
        "factorial_squared_multiply_interpolation_degree": gamma_mul_degree,
        "factorial_squared_divide_interpolation_degree": gamma_div_degree,
        "endpoint_ratio_normalization": "low_sum/low_pivot-high_sum/high_pivot",
        "endpoint_ratio_defined_point_count": len(ratio_data),
        "balanced_rational_degree_excluded_through": excluded_degree,
        "rational_interpolation_matrix_rank": rational_rank,
        "rational_interpolation_matrix_column_count": columns,
    }


def positive_coefficients(p: int, s: int) -> list[int]:
    b, c = p - 5 * s - 2, 2 * s + 2
    assert b >= 0
    g = [0] * p
    g[0] = 1
    for n in range(p - 1):
        rhs = (n + b) * g[n]
        if n >= 3:
            rhs += (n - 3 + 4 * c) * g[n - 3]
        if n >= 4:
            rhs -= (n - 4 + b + 4 * c) * g[n - 4]
        assert rhs % (n + 1) == 0
        g[n + 1] = rhs // (n + 1)
    return g


def sign_check(limit: int) -> dict:
    transcript = []
    for p in primes_upto(limit):
        for s in range((p - 2) // 5 + 1):
            b = p - 5 * s - 2
            if b < 0:
                continue
            g = positive_coefficients(p, s)
            d = p - 3 * s
            value = (
                (g[d - 2] + g[d - 3] + g[d - 4]) * g[p - 5]
                - (g[p - 4] + g[p - 3] + g[p - 2]) * g[d - 1]
            )
            sign = (value > 0) - (value < 0)
            expected = -1 if b >= 1 else (0 if s % 4 == 1 else 1)
            assert sign == expected
            transcript.append([p, s, b, sign])
    return {
        "prime_limit": limit,
        "pairs_checked": len(transcript),
        "all_match_proved_sign_classification": True,
        "transcript_sha256": hashlib.sha256(json.dumps(transcript, separators=(",", ":")).encode()).hexdigest(),
    }


def finite_scan(limit: int) -> dict:
    primes = primes_upto(limit)
    roots: list[list[int]] = []
    off_ray = []
    per_prime = {}
    histogram = Counter()
    candidates = 0
    classification = Counter()
    for p in primes:
        local = []
        for s in range((p - 1) // 3 + 1):
            candidates += 1
            a = coefficients_mod_p(p, s)
            if data_from_coefficients(p, s, a)["determinant"]:
                continue
            roots.append([p, s])
            local.append(s)
            labels = known_ray_labels(p, s)
            if labels:
                classification[" + ".join(labels)] += 1
            else:
                classification["off_known_rays"] += 1
                off_ray.append([p, s])
        histogram[len(local)] += 1
        if local:
            per_prime[str(p)] = len(local)
    maximum = max(histogram) if histogram else 0
    encoded = json.dumps(roots, separators=(",", ":")).encode("ascii")
    return {
        "scope": [7, limit],
        "prime_count": len(primes),
        "candidate_pair_count": candidates,
        "zero_pair_count": len(roots),
        "primes_with_roots": len(per_prime),
        "root_count_histogram": {str(k): histogram[k] for k in sorted(histogram)},
        "maximum_roots_for_one_prime": maximum,
        "primes_attaining_maximum": [int(p) for p, value in per_prime.items() if value == maximum],
        "classification_counts": dict(sorted(classification.items())),
        "off_known_ray_count": len(off_ray),
        "zero_pairs_sha256": hashlib.sha256(encoded).hexdigest(),
        "zero_pairs": roots,
        "warning": "finite exact census only; no uniform or density conclusion",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-limit", type=int, default=2000)
    parser.add_argument("--sign-limit", type=int, default=251)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    selected = [p for p in (101, 211, 337, 503, 997) if p <= args.scan_limit]
    obj = {
        "item": 185,
        "status": "PROVED generating-function and positive-lift sign theorems; exact normalization obstruction and finite census; sublinear root count OPEN",
        "proved_definitions": {
            "A0": "(1-x)^2/(1-x^4)^2",
            "H": "(1-x)^5/(1-x^4)^2",
            "K": "x^3 H",
            "coefficient_maps": "a[p-r](s)=[x^(p-r)]A0 H^s and a[p-3s-r](s)=[x^(p-r)]A0 K^s",
            "positive_lift_sign": "For b=p-5s-2: E<0 if b>=1; if b=0 then E=0 for s=1 mod 4 and E>0 for s=3 mod 4.",
        },
        "positive_lift_sign_finite_check": sign_check(args.sign_limit),
        "normalization_diagnostics": [normalization_record(p) for p in selected],
        "finite_census": finite_scan(args.scan_limit),
        "open": [
            "Prove r_p=o(p), or produce a counterexample with linearly many moving roots.",
            "Find a bounded-conductor trace-function or fixed-order recurrence controlling zeros of the coefficient determinant.",
            "The exact structural, factorial/gamma, and endpoint-pivot normalizations tested here retain linearly growing interpolation complexity.",
            "Nothing here decides the arithmetic nature of e+pi.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
