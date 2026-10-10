#!/usr/bin/env python3
"""Exact deterministic replay for Item 265.

This checker uses only the Python standard library.  Its bounded loops verify
universal identities on explicit finite rectangles; they do not search for
exceptional primes and are labelled EXACT FINITE ONLY in the output.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def beta_sequences(limit: int) -> tuple[list[int], list[int]]:
    q = [1, 1]
    p = [1, 3]
    for n in range(2, limit + 1):
        a = 4 * n - 2
        q.append(a * q[-1] + q[-2])
        p.append(a * p[-1] + p[-2])
    return p[: limit + 1], q[: limit + 1]


def poly_add(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(a: list[int], scalar: int) -> list[int]:
    return [scalar * value for value in a]


def poly_shift(a: list[int], places: int) -> list[int]:
    return [0] * places + a


def poly_derivative(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return [0]
    return [i * a[i] for i in range(1, len(a))]


def poly_eval(a: list[int], x: int) -> int:
    value = 0
    for coefficient in reversed(a):
        value = value * x + coefficient
    return value


def reverse_bessel_closed(n: int) -> list[int]:
    return [
        math.factorial(2 * n - k)
        // (math.factorial(k) * math.factorial(n - k))
        for k in range(n + 1)
    ]


def reverse_bessel_recurrence(limit: int) -> list[list[int]]:
    polys = [[1]]
    if limit == 0:
        return polys
    polys.append([2, 1])
    for n in range(2, limit + 1):
        polys.append(
            poly_add(
                poly_scale(polys[n - 1], 4 * n - 2),
                poly_shift(polys[n - 2], 2),
            )
        )
    return polys


def continuant_value(d: int, x: int) -> int:
    if d == 0:
        return 0
    if d == 1:
        return 1
    p0, p1 = 0, 1
    for j in range(d - 1):
        p0, p1 = p1, (4 * x + 4 * j + 6) * p1 + p0
    return p1


def check_fixed_seed(limit: int) -> dict[str, object]:
    p, q = beta_sequences(limit)
    checked = 0
    product_rows = 0
    for n in range(1, limit + 1):
        assert p[n] % 2 == 1
        assert q[n] % 2 == 1
        assert math.gcd(q[n], q[n - 1]) == 1
        assert p[n] * q[n - 1] - p[n - 1] * q[n] == 2 * (-1) ** (n - 1)
        assert math.gcd(p[n], q[n]) == 1
        checked += 1
        if n >= 2:
            lower_product = math.prod(4 * j - 2 for j in range(2, n + 1))
            lower_closed = math.factorial(2 * n) // (2 * math.factorial(n))
            upper = 4 ** (n - 1) * math.factorial(n)
            assert lower_product == lower_closed
            assert lower_product < q[n] < upper
            product_rows += 1
    return {
        "range": [1, limit],
        "fixed_seed_rows": checked,
        "product_bound_rows": product_rows,
        "q_endpoint_digits": len(str(q[limit])),
        "labels": "EXACT FINITE ONLY",
    }


def check_reverse_bessel(limit: int) -> dict[str, object]:
    _, q = beta_sequences(limit)
    polys = reverse_bessel_recurrence(limit)
    coefficient_identity_rows = 0
    derivative_identity_rows = 0
    specialization_rows = 0
    for n in range(limit + 1):
        closed = reverse_bessel_closed(n)
        assert polys[n] == closed
        coefficient_identity_rows += len(closed)
        assert poly_eval(closed, -1) == q[n]
        specialization_rows += 1
        if n >= 1:
            lhs = poly_scale(poly_derivative(closed), 2)
            rhs = poly_add(closed, poly_scale(poly_shift(polys[n - 1], 1), -1))
            assert lhs == rhs
            assert 2 * poly_eval(poly_derivative(closed), -1) == q[n] + q[n - 1]
            derivative_identity_rows += len(lhs)
    return {
        "degree_range": [0, limit],
        "coefficient_equalities": coefficient_identity_rows,
        "specialization_equalities": specialization_rows,
        "derivative_coefficient_equalities": derivative_identity_rows,
        "labels": "EXACT FINITE ONLY",
    }


def check_transfer(n_limit: int, d_limit: int) -> dict[str, object]:
    _, q = beta_sequences(n_limit + d_limit)
    transfer_rows = 0
    gcd_rows = 0
    for n in range(n_limit + 1):
        for d in range(1, d_limit + 1):
            rhs = continuant_value(d, n) * q[n + 1]
            rhs += continuant_value(d - 1, n + 1) * q[n]
            assert q[n + d] == rhs
            assert math.gcd(q[n], q[n + d]) == math.gcd(
                q[n], continuant_value(d, n)
            )
            transfer_rows += 1
            gcd_rows += 1
    return {
        "n_range": [0, n_limit],
        "d_range": [1, d_limit],
        "transfer_equalities": transfer_rows,
        "gcd_equalities": gcd_rows,
        "labels": "EXACT FINITE ONLY",
    }


def check_primewise_box(bound: int) -> dict[str, object]:
    sequential_rows = 0
    reservoir_rows = 0
    squarefull_rows = 0

    for exponent in range(bound + 1):
        excess = max(exponent - 1, 0)
        sqfull = exponent if exponent >= 2 else 0
        assert excess <= sqfull <= 2 * excess
        squarefull_rows += 1

    for k in range(bound + 1):
        for kappa in range(bound + 1):
            residual = max(k - kappa, 0)
            assert min(k, kappa) + 2 * residual <= 2 * k
            reservoir_rows += 1

            for beta in range(bound + 1):
                if k > kappa + beta:
                    continue
                assert residual <= beta
                for t in range(bound + 1):
                    d = min(beta, t)
                    for pstar in range(bound + 1):
                        gamma = min(beta, pstar) if beta == t and beta > 0 else 0
                        matching = d + gamma
                        assert matching <= 2 * t
                        overlap_quotient = max(matching - 2 * residual, 0)
                        normalized_q_square = 2 * max(t - residual, 0)
                        assert overlap_quotient <= normalized_q_square
                        sequential_rows += 1

    return {
        "exponent_box": [0, bound],
        "squarefull_exponent_rows": squarefull_rows,
        "reservoir_ceiling_rows": reservoir_rows,
        "sequential_overlap_rows": sequential_rows,
        "labels": "EXACT FINITE ONLY",
    }


def build_result() -> dict[str, object]:
    return {
        "schema": "item265-beta-squarefull-capacity-certificate-v1",
        "scope": (
            "bounded exact identity replay only; no search for exceptional primes "
            "and no finite-to-asymptotic inference"
        ),
        "checks": {
            "fixed_seed": check_fixed_seed(80),
            "reverse_bessel": check_reverse_bessel(14),
            "transfer": check_transfer(36, 12),
            "primewise": check_primewise_box(8),
        },
        "general_claims_location": (
            "item265_beta_squarefull_capacity_report.md; general claims are "
            "proved algebraically or inherited from sealed dependencies"
        ),
        "booking": {
            "positive_linear_capacity_admission": "FAIL",
            "new_route1_rate": "0",
            "new_capacity_reduction": "0",
        },
        "strict_labels": {
            "bounded_checks": "EXACT FINITE ONLY",
            "exceptional_prime_search": "NOT PERFORMED",
            "all_prime_squarefull_bound": "OPEN",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    payload = build_result()
    output = Path(args.output)
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

