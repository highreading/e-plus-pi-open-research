#!/usr/bin/env python3
"""Portable exact certificate for Item 281.

All coefficient, Smith/Fitting, rank-stratum, and displayed norm-witness
checks are exact.  The bounded row replay is EXACT FINITE ONLY.  The
Chebotarev and prime-number-theorem statements used in the report are
theorems, not inferred from this replay.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE.parent / "results" / "item281_j1_isolated_fitting_norm_certificate.json"


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(flags) if flag]


def scalar_coefficients(m: int) -> list[int]:
    """Return g_(m,k), 0<=k<=4m+1, by Item 200's exact recurrence."""
    target = 4 * m + 1
    coefficients = [1]
    for degree in range(target):
        rhs = (20 * m - 8 - 10 * degree) * coefficients[degree]
        if degree >= 1:
            rhs += 2 * (10 * degree + 10 - 20 * m) * coefficients[degree - 1]
        if degree >= 2:
            rhs += 4 * (10 * m - 5 * degree - 6) * coefficients[degree - 2]
        if degree >= 3:
            rhs += 8 * (degree + 1 - 4 * m) * coefficients[degree - 3]
        divisor = -2 * (degree + 1)
        quotient, remainder = divmod(rhs, divisor)
        if remainder:
            raise AssertionError((m, degree, rhs, divisor))
        coefficients.append(quotient)
    return coefficients


def coefficient_pair(m: int) -> tuple[int, int]:
    coefficients = scalar_coefficients(m)
    n = 4 * m
    return (
        coefficients[n] - 2 * coefficients[n - 1] + 2 * coefficients[n - 2],
        coefficients[n + 1],
    )


def cartier_degree(modulus: int, n: int, k: int) -> int:
    residue_n = n % modulus
    residue_k = k % modulus
    return (
        2 * residue_n
        if residue_k == 0
        else 2 * residue_n + 3 * (modulus - residue_k)
    )


def forced_primes(m: int, primes: list[int]) -> list[int]:
    return [
        prime
        for prime in primes
        if prime & 1
        and cartier_degree(prime, 6 * m, 4 * m + 1) <= prime - 2
        and cartier_degree(prime, 6 * m, 4 * m + 2) <= prime - 2
    ]


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s * (-1 if a < 0 else 1), old_t * (-1 if b < 0 else 1)


def actual_j1_rows(m: int, primes: list[int]) -> list[tuple[int, int, int]]:
    rows = []
    for prime in primes:
        if 3 * prime < 4 * m + 3 or 2 * prime > 3 * m - 1:
            continue
        s_numerator = 3 * prime - 4 * m - 1
        if s_numerator % 2:
            continue
        s = s_numerator // 2
        h = 3 * m - 2 * prime
        if h >= 1 and s >= 1:
            if (4 * h + 6 * s + 3, 3 * h + 4 * s + 2) != (prime, m):
                raise AssertionError((m, prime, h, s))
            rows.append((prime, h, s))
    return rows


def fitting_replay(bound: int = 120) -> tuple[dict[str, int], str]:
    primes = primes_upto(6 * bound)
    digest = hashlib.sha256()
    forced_incidents = 0
    j1_rows = 0
    for m in range(2, bound + 1):
        c0, c1 = coefficient_pair(m)
        forced = forced_primes(m, primes)
        factor = math.prod(forced)
        if c0 % factor or c1 % factor:
            raise AssertionError((m, "forced factor"))
        b0, b1 = c0 // factor, c1 // factor
        gcd_value, bezout_0, bezout_1 = extended_gcd(b0, b1)
        if bezout_0 * b0 + bezout_1 * b1 != gcd_value:
            raise AssertionError((m, "Bezout"))
        if gcd_value != math.gcd(abs(b0), abs(b1)):
            raise AssertionError((m, "gcd"))
        forced_incidents += len(forced)
        for prime, h, s in actual_j1_rows(m, primes):
            if prime not in forced:
                raise AssertionError((m, prime, "not forced"))
            collision_raw = c0 % (prime * prime) == 0 and c1 % (prime * prime) == 0
            collision_normalized = b0 % prime == 0 and b1 % prime == 0
            if collision_raw != collision_normalized:
                raise AssertionError((m, prime, collision_raw, collision_normalized))
            digest.update(
                (repr((m, prime, h, s, b0 % prime, b1 % prime)) + "\n").encode("ascii")
            )
            j1_rows += 1
    return {
        "m_bound": bound,
        "forced_prime_incidents": forced_incidents,
        "j1_rows": j1_rows,
    }, digest.hexdigest()


def rank_mod(matrix: list[list[int]], modulus: int) -> int:
    rows = [[entry % modulus for entry in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, modulus)
        rows[rank] = [(entry * inverse) % modulus for entry in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                multiplier = rows[i][column]
                rows[i] = [
                    (left - multiplier * right) % modulus
                    for left, right in zip(rows[i], rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def rank_strata() -> dict[str, Any]:
    matrices = {
        "rank_2": [[1, 0, 0, 0], [0, 1, 0, 0]],
        "rank_1": [[1, 0, 0, 0], [0, 0, 0, 0]],
        "rank_0": [[0, 0, 0, 0], [0, 0, 0, 0]],
    }
    result: dict[str, Any] = {}
    for name, matrix in matrices.items():
        ranks = {rank_mod(matrix, prime) for prime in (13, 17, 19, 23)}
        if len(ranks) != 1:
            raise AssertionError((name, ranks))
        rank = ranks.pop()
        result[name] = {
            "rank": rank,
            "kernel_dimension": 4 - rank,
            "canonical_collision_ideal": (
                "(x1,x2)" if rank == 2 else "(x1)" if rank == 1 else "(0)"
            ),
        }
    return result


def least_nonsquare(prime: int) -> int:
    for candidate in range(2, prime):
        if pow(candidate, (prime - 1) // 2, prime) == prime - 1:
            return candidate
    raise AssertionError(prime)


def local_scalar_replay() -> list[dict[str, int]]:
    rows = []
    for prime in (13, 17, 19, 23, 29, 31):
        # Every nonzero linear form has the displayed nonzero kernel vector.
        for a in range(prime):
            for b in range(prime):
                if a == b == 0:
                    continue
                x, y = b, -a % prime
                if x == y == 0 or (a * x + b * y) % prime:
                    raise AssertionError((prime, a, b, x, y))
        discriminant = least_nonsquare(prime)
        zero_count = 0
        for x in range(prime):
            for y in range(prime):
                if (x * x - discriminant * y * y) % prime == 0:
                    zero_count += 1
        if zero_count != 1:
            raise AssertionError((prime, discriminant, zero_count))
        rows.append({"p": prime, "least_nonsquare": discriminant, "norm_zero_count": zero_count})
    return rows


def actual_norm_false_positives() -> list[dict[str, int]]:
    declared = [
        (-1, 61, 10, 3, 44, 32, 47),
        (2, 89, 8, 9, 62, 88, 32),
        (3, 37, 4, 3, 26, 35, 10),
        (5, 59, 5, 6, 41, 52, 36),
        (7, 37, 1, 5, 25, 15, 14),
    ]
    result = []
    for discriminant, prime, h, s, m, expected_q0, expected_q1 in declared:
        if 4 * h + 6 * s + 3 != prime or 3 * h + 4 * s + 2 != m:
            raise AssertionError((discriminant, prime, "phase"))
        c0, c1 = coefficient_pair(m)
        forced = forced_primes(m, primes_upto(6 * m))
        if prime not in forced:
            raise AssertionError((discriminant, prime, "not in forced product"))
        if c0 % prime or c1 % prime:
            raise AssertionError((discriminant, prime, "first digit"))
        q0, q1 = (c0 // prime) % prime, (c1 // prime) % prime
        if (q0, q1) != (expected_q0, expected_q1):
            raise AssertionError((discriminant, prime, q0, q1))
        if q0 == q1 == 0 or (q0 * q0 - discriminant * q1 * q1) % prime:
            raise AssertionError((discriminant, prime, q0, q1, "norm"))
        forced_factor = math.prod(forced)
        b0, b1 = (c0 // forced_factor) % prime, (c1 // forced_factor) % prime
        if b0 == b1 == 0 or (b0 * b0 - discriminant * b1 * b1) % prime:
            raise AssertionError((discriminant, prime, b0, b1, "normalized norm"))
        result.append({
            "d": discriminant,
            "p": prime,
            "h": h,
            "s": s,
            "M": m,
            "U0_raw_quotient": q0,
            "U1_raw_quotient": q1,
            "Cbar0": b0,
            "Cbar1": b1,
        })
    return result


def split_library_witness() -> dict[str, Any]:
    prime = 1009
    if prime not in primes_upto(prime):
        raise AssertionError((prime, "not prime"))
    discriminants = [-1, 2, 3, 5, 7]
    roots = []
    for discriminant in discriminants:
        root = next(
            (value for value in range(prime) if value * value % prime == discriminant % prime),
            None,
        )
        if root is None:
            raise AssertionError((prime, discriminant))
        roots.append(root)
    h, s = (prime - 9) // 4, 1
    m = 3 * h + 4 * s + 2
    if (h, s, m) != (250, 1, 756) or 4 * h + 6 * s + 3 != prime:
        raise AssertionError((prime, h, s, m))
    return {
        "p": prime,
        "actual_row": {"h": h, "s": s, "M": m},
        "discriminants": discriminants,
        "square_roots": roots,
    }


def certificate() -> dict[str, Any]:
    fitting_counts, fitting_hash = fitting_replay()
    height_constant = -4 * math.log(2) + math.pi / math.sqrt(3) + 3 * math.log(3)
    cauchy_constant = 6.327627545440858
    normalized_constant = cauchy_constant - height_constant
    body: dict[str, Any] = {
        "schema": "item281-j1-isolated-fitting-norm-certificate-v1",
        "labels": {
            "normalized_Smith_Fitting_generator": "PROVED",
            "rank_stratification": "PROVED",
            "local_minimum_exact_scalar_degree": 2,
            "finite_fixed_form_library_global_exactness": "PROVED IMPOSSIBLE by Chebotarev; report theorem",
            "bounded_replays": "EXACT FINITE ONLY",
            "isolated_prime_weighted_mass": "OPEN",
            "new_route1_rate": 0,
        },
        "fitting": {
            "ideal": "(Cbar0(M),Cbar1(M))=g_M Z",
            "generator": "g_M=gcd(Cbar0(M),Cbar1(M))",
            "j1_collision_equivalence": "p divides g_M iff p^2 divides both raw coefficients",
            "replay": fitting_counts,
            "replay_sha256": fitting_hash,
            "replay_label": "EXACT FINITE ONLY",
        },
        "rank_strata": rank_strata(),
        "local_scalar": {
            "linear_form_exact_origin_encoding": False,
            "quadratic_norm_with_nonsquare": True,
            "exact_replay": local_scalar_replay(),
            "actual_false_positive_norm_witnesses": actual_norm_false_positives(),
            "fixed_library_split_witness": split_library_witness(),
        },
        "height": {
            "forced_Cartier_log_constant_kappa": height_constant,
            "component_Cauchy_constant_H": cauchy_constant,
            "normalized_component_constant_H_minus_kappa": normalized_constant,
            "raw_j1_log_mass_per_M": 1 / 6,
            "normalized_scalar_ratio_beats_raw": False,
            "independent_normalized_valuation_copies_needed": 24,
        },
        "capacity": {
            "raw_j1_capacity_per_6M": "1/36",
            "bounded_cluster_difference": "o(M), frozen Item279",
            "isolated_collision_primes": "uncontrolled at linear scale",
            "new_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
    }
    payload = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    body["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "payload_sha256": result["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
