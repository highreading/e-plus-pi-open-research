#!/usr/bin/env python3
"""Portable exact certificate for Item 284.

The CRT norm construction and all displayed witnesses are exact.  The
bounded least-simultaneous-nonresidue replay is EXACT FINITE ONLY.  No
asymptotic least-nonresidue inference is made from it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Callable


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE.parent / "results" / "item284_j1_parameter_norm_certificate.json"


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


def coefficient_pair(m: int) -> tuple[int, int]:
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
    n = 4 * m
    return (
        coefficients[n] - 2 * coefficients[n - 1] + 2 * coefficients[n - 2],
        coefficients[n + 1],
    )


def cartier_degree(modulus: int, n: int, k: int) -> int:
    residue_n = n % modulus
    residue_k = k % modulus
    return 2 * residue_n if residue_k == 0 else 2 * residue_n + 3 * (modulus - residue_k)


def forced_primes(m: int, primes: list[int]) -> list[int]:
    return [
        prime
        for prime in primes
        if prime & 1
        and cartier_degree(prime, 6 * m, 4 * m + 1) <= prime - 2
        and cartier_degree(prime, 6 * m, 4 * m + 2) <= prime - 2
    ]


def candidate_primes(m: int, primes: list[int]) -> list[int]:
    return [
        prime
        for prime in primes
        if 3 * prime >= 4 * m + 3 and 2 * prime <= 3 * m - 1
    ]


def least_nonsquare(prime: int) -> int:
    for candidate in range(2, prime):
        if pow(candidate, (prime - 1) // 2, prime) == prime - 1:
            return candidate
    raise AssertionError(prime)


def crt_simultaneous_nonsquare(primes: list[int]) -> tuple[int, int, list[int]]:
    if not primes:
        return 2, 1, []
    modulus = math.prod(primes)
    local_values = [least_nonsquare(prime) for prime in primes]
    coefficient = 0
    for prime, local in zip(primes, local_values):
        complement = modulus // prime
        idempotent = complement * pow(complement, -1, prime)
        coefficient = (coefficient + local * idempotent) % modulus
    if not (1 <= coefficient < modulus):
        raise AssertionError((primes, coefficient, modulus))
    for prime in primes:
        if pow(coefficient % prime, (prime - 1) // 2, prime) != prime - 1:
            raise AssertionError((prime, coefficient))
    return coefficient, modulus, local_values


def least_simultaneous_nonsquare(primes: list[int]) -> int:
    if not primes:
        return 2
    candidate = 2
    while True:
        if all(pow(candidate % prime, (prime - 1) // 2, prime) == prime - 1 for prime in primes):
            return candidate
        candidate += 1


def crt_norm_replay(bound: int = 220) -> tuple[dict[str, Any], str]:
    primes = primes_upto(6 * bound)
    digest = hashlib.sha256()
    rows = 0
    maximum_coefficient_bits = 0
    declared_example: dict[str, Any] = {}
    for m in range(9, bound + 1):
        candidates = candidate_primes(m, primes)
        if not candidates:
            continue
        coefficient, modulus, local_values = crt_simultaneous_nonsquare(candidates)
        if modulus != math.prod(candidates) or coefficient >= modulus:
            raise AssertionError((m, coefficient, modulus))
        c0, c1 = coefficient_pair(m)
        forced = forced_primes(m, primes)
        if any(prime not in forced for prime in candidates):
            raise AssertionError((m, "candidate not forced"))
        forced_factor = math.prod(forced)
        if c0 % forced_factor or c1 % forced_factor:
            raise AssertionError((m, "forced divisibility"))
        b0, b1 = c0 // forced_factor, c1 // forced_factor
        raw_norm = c0 * c0 - coefficient * c1 * c1
        normalized_norm = b0 * b0 - coefficient * b1 * b1
        if raw_norm == 0 and (c0 != 0 or c1 != 0):
            raise AssertionError((m, "raw norm unexpectedly zero"))
        for prime in candidates:
            collision = c0 % (prime * prime) == 0 and c1 % (prime * prime) == 0
            if (raw_norm % (prime**4) == 0) != collision:
                raise AssertionError((m, prime, "raw norm equivalence"))
            if (normalized_norm % prime == 0) != collision:
                raise AssertionError((m, prime, "normalized norm equivalence"))
            if collision and normalized_norm % (prime * prime):
                raise AssertionError((m, prime, "normalized square valuation"))
            digest.update(
                (repr((m, prime, coefficient % prime, collision)) + "\n").encode("ascii")
            )
            rows += 1
        maximum_coefficient_bits = max(maximum_coefficient_bits, coefficient.bit_length())
        if m == 100:
            declared_example = {
                "M": m,
                "candidate_primes": candidates,
                "B_M": modulus,
                "least_local_nonsquares": local_values,
                "CRT_coefficient": coefficient,
            }
    return {
        "M_bound": bound,
        "candidate_rows": rows,
        "maximum_CRT_coefficient_bits": maximum_coefficient_bits,
        "declared_M100_example": declared_example,
    }, digest.hexdigest()


def least_coefficient_replay(bound: int = 300) -> tuple[dict[str, Any], str]:
    primes = primes_upto(2 * bound)
    digest = hashlib.sha256()
    maximum = (0, 0, 0)
    nonempty = 0
    for m in range(9, bound + 1):
        candidates = candidate_primes(m, primes)
        if not candidates:
            continue
        coefficient = least_simultaneous_nonsquare(candidates)
        if not all(pow(coefficient % prime, (prime - 1) // 2, prime) == prime - 1 for prime in candidates):
            raise AssertionError((m, coefficient))
        digest.update((repr((m, tuple(candidates), coefficient)) + "\n").encode("ascii"))
        nonempty += 1
        maximum = max(maximum, (coefficient, m, len(candidates)))
    return {
        "M_bound": bound,
        "nonempty_prime_intervals": nonempty,
        "maximum_least_coefficient": maximum[0],
        "maximum_at_M": maximum[1],
        "candidate_count_there": maximum[2],
    }, digest.hexdigest()


def simple_rule_false_positives() -> list[dict[str, Any]]:
    rules: list[tuple[str, Callable[[int, int, int], int], tuple[int, ...]]] = [
        ("h", lambda h, s, m: h, (13, 1, 1, 9, 2, 11, 1)),
        ("s", lambda h, s, m: s, (13, 1, 1, 9, 2, 11, 1)),
        ("h+s", lambda h, s, m: h + s, (139, 7, 18, 95, 107, 62, 25)),
        ("2h+3s", lambda h, s, m: 2 * h + 3 * s, (31, 1, 4, 21, 13, 1, 14)),
        ("M", lambda h, s, m: m, (71, 8, 6, 50, 46, 30, 50)),
        ("M-1", lambda h, s, m: m - 1, (283, 34, 24, 200, 154, 100, 199)),
        ("M+1", lambda h, s, m: m + 1, (443, 74, 24, 320, 195, 44, 321)),
    ]
    result = []
    for name, rule, row in rules:
        prime, h, s, m, expected_u0, expected_u1, expected_d = row
        if prime not in primes_upto(prime):
            raise AssertionError((name, prime, "not prime"))
        if (4 * h + 6 * s + 3, 3 * h + 4 * s + 2) != (prime, m):
            raise AssertionError((name, "phase"))
        c0, c1 = coefficient_pair(m)
        if c0 % prime or c1 % prime:
            raise AssertionError((name, "first digit"))
        u0, u1 = (c0 // prime) % prime, (c1 // prime) % prime
        discriminant = rule(h, s, m) % prime
        if (u0, u1, discriminant) != (expected_u0, expected_u1, expected_d):
            raise AssertionError((name, u0, u1, discriminant))
        if u0 == u1 == 0 or discriminant == 0:
            raise AssertionError((name, "degenerate witness"))
        if (u0 * u0 - discriminant * u1 * u1) % prime:
            raise AssertionError((name, "not a norm zero"))
        result.append({
            "rule": name,
            "p": prime,
            "h": h,
            "s": s,
            "M": m,
            "U0": u0,
            "U1": u1,
            "d_mod_p": discriminant,
        })
    return result


def certificate() -> dict[str, Any]:
    crt_counts, crt_hash = crt_norm_replay()
    least_counts, least_hash = least_coefficient_replay()
    h_constant = 6.327627545440858
    kappa = -4 * math.log(2) + math.pi / math.sqrt(3) + 3 * math.log(3)
    body: dict[str, Any] = {
        "schema": "item284-j1-parameter-norm-certificate-v1",
        "labels": {
            "all_candidate_prime_CRT_norm": "PROVED exact construction",
            "construction_uses_unknown_collision_set": False,
            "bounded_height_norm_size_method": "PROVED insufficient",
            "least_simultaneous_nonsquare_replay": "EXACT FINITE ONLY",
            "isolated_prime_weighted_mass": "OPEN",
            "new_route1_rate": 0,
        },
        "CRT_norm": {
            "candidate_set": "all primes (4M+3)/3 <= p <= (3M-1)/2",
            "coefficient": "d_M is the least positive CRT representative of least local nonsquares",
            "coefficient_bound": "1 <= d_M < B_M=product(candidate primes)",
            "raw_equivalence": "p^4 divides C0^2-d_M C1^2 iff the full gate collides",
            "normalized_equivalence": "p divides Cbar0^2-d_M Cbar1^2 iff the full gate collides",
            "replay": crt_counts,
            "replay_sha256": crt_hash,
        },
        "least_coefficient": {
            "status": "asymptotic height OPEN",
            "replay": least_counts,
            "replay_sha256": least_hash,
            "replay_label": "EXACT FINITE ONLY",
        },
        "simple_parameter_rules": {
            "actual_false_positive_witnesses": simple_rule_false_positives(),
            "inference": "witnesses only; no universal rational-function no-go",
        },
        "height": {
            "H": h_constant,
            "kappa": kappa,
            "CRT_delta_upper_bound": 1 / 6,
            "raw_norm_ratio_CRT": h_constant / 2 + 1 / 24,
            "normalized_norm_ratio_CRT": h_constant - kappa + 1 / 12,
            "raw_norm_ratio_if_subexponential_coefficient": h_constant / 2,
            "raw_j1_log_mass_per_M": 1 / 6,
            "height_admission_passed": False,
        },
        "capacity": {
            "raw_j1_capacity_per_6M": "1/36",
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
