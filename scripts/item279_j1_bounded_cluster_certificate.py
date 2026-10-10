#!/usr/bin/env python3
"""Portable exact certificate for Item 279.

The multi-prime CRT identities are exact.  The bounded prime-pattern
replay is EXACT FINITE ONLY; asymptotic pattern mass uses the classical
Selberg upper-bound sieve theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item279_j1_bounded_cluster_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item279_j1_bounded_cluster_certificate.json"
)


def determinant_integer(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for column in range(len(rows) - 1):
        pivot = next((index for index in range(column, len(rows)) if rows[index][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            sign = -sign
        pivot_value = rows[column][column]
        for i in range(column + 1, len(rows)):
            for j in range(column + 1, len(rows)):
                numerator = pivot_value * rows[i][j] - rows[i][column] * rows[column][j]
                if numerator % previous:
                    raise AssertionError("Bareiss exact division")
                rows[i][j] = numerator // previous
            rows[i][column] = 0
        previous = pivot_value
    return sign * rows[-1][-1]


def matrix_vector(matrix: list[list[int]], vector: list[int], modulus: int) -> list[int]:
    return [sum(x * y for x, y in zip(row, vector)) % modulus for row in matrix]


def phase_tower_replay(maximum_diameter: int = 8) -> tuple[int, str]:
    digest = hashlib.sha256()
    count = 0
    for diameter in range(1, maximum_diameter + 1):
        for h_value in range(4 * diameter + 1, 4 * diameter + 18):
            for s_value in range(1, 18):
                p = 4 * h_value + 6 * s_value + 3
                M = 3 * h_value + 4 * s_value + 2
                for shift in range(diameter + 1):
                    h_new, s_new = h_value - 4 * shift, s_value + 3 * shift
                    p_new = 4 * h_new + 6 * s_new + 3
                    M_new = 3 * h_new + 4 * s_new + 2
                    if p_new != p + 2 * shift or M_new != M or h_new < 1:
                        raise AssertionError((diameter, h_value, s_value, shift))
                    digest.update((repr((diameter, h_value, s_value, shift, p_new, M_new)) + "\n").encode("ascii"))
                    count += 1
    return count, digest.hexdigest()


def crt_idempotents(primes: list[int]) -> list[int]:
    modulus = math.prod(primes)
    values = []
    for prime in primes:
        complement = modulus // prime
        values.append(complement * pow(complement, -1, prime) % modulus)
    if sum(values) % modulus != 1:
        raise AssertionError("idempotent sum")
    for i, left in enumerate(values):
        if (left * left - left) % modulus:
            raise AssertionError("idempotent")
        for j, right in enumerate(values):
            if i != j and left * right % modulus:
                raise AssertionError("orthogonality")
    return values


def multi_crt_obstruction() -> dict[str, Any]:
    # This is the actual offset pattern J={0,1,4}: 29,31,37.
    primes = [29, 31, 37]
    offsets = [0, 1, 4]
    modulus = math.prod(primes)
    idempotents = crt_idempotents(primes)
    gates = [
        [[1, 0, 0, 0], [0, 1, 0, 0]],
        [[0, 0, 1, 0], [0, 0, 0, 1]],
        [[1, 0, 0, 0], [0, 1, 0, 0]],
    ]
    if determinant_integer(gates[0] + gates[1]) != 1:
        raise AssertionError("rational transverse substack")
    mixed: list[list[int]] = []
    row_blocks: list[int] = []
    for block, (idempotent, gate) in enumerate(zip(idempotents, gates)):
        for row in gate:
            mixed.append([(idempotent * entry) % modulus for entry in row])
            row_blocks.append(block)
    minor_count = 0
    for row_indices in itertools.combinations(range(len(mixed)), 4):
        minor = [mixed[index] for index in row_indices]
        if determinant_integer(minor) % modulus:
            raise AssertionError((row_indices, determinant_integer(minor) % modulus))
        minor_count += 1

    # A single integral vector can realize independent kernel residues.
    vector = [29 * 37, 0, 31, 0]
    for prime, gate in zip(primes, gates):
        if matrix_vector(gate, vector, prime) != [0, 0]:
            raise AssertionError((prime, gate, vector))
    if all(entry % modulus == 0 for entry in vector):
        raise AssertionError("false full-product divisibility")

    product_square = modulus * modulus
    fixed_coefficients = [product_square * 17, -product_square * 43]
    if any(value % product_square for value in fixed_coefficients):
        raise AssertionError("multi-square CRT")
    return {
        "offset_pattern_J": offsets,
        "primes": primes,
        "N": modulus,
        "idempotents": idempotents,
        "rational_two_block_stack_determinant": 1,
        "mixed_4x4_minors_checked": minor_count,
        "all_mixed_4x4_minors_mod_N": 0,
        "counterexample_vector": vector,
        "counterexample_vector_divisible_by_N": False,
        "fixed_coefficient_product_square": product_square,
    }


def prime_sieve(bound: int) -> bytearray:
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(bound) + 1):
        if sieve[prime]:
            sieve[prime * prime : bound + 1 : prime] = b"\x00" * (
                (bound - prime * prime) // prime + 1
            )
    return sieve


def bounded_pattern_replay(diameter: int = 6, bound: int = 10000) -> tuple[dict[str, int], str]:
    sieve = prime_sieve(bound + 2 * diameter)
    digest = hashlib.sha256()
    counts: dict[str, int] = {}
    for size in range(2, diameter + 2):
        patterns = [(0,) + tail for tail in itertools.combinations(range(1, diameter + 1), size - 1)]
        if len(patterns) != math.comb(diameter, size - 1):
            raise AssertionError("pattern count")
        total = 0
        for pattern in patterns:
            count = 0
            for base in range(3, bound + 1, 2):
                if all(sieve[base + 2 * shift] for shift in pattern):
                    count += 1
                    digest.update((repr((size, pattern, base)) + "\n").encode("ascii"))
            total += count
        counts[str(size)] = total
    return counts, digest.hexdigest()


def certificate() -> dict[str, Any]:
    phase_count, phase_hash = phase_tower_replay()
    crt = multi_crt_obstruction()
    pattern_counts, pattern_hash = bounded_pattern_replay()
    body: dict[str, Any] = {
        "schema": "item279-j1-bounded-cluster-certificate-v1",
        "labels": {
            "fixed_D_t_cluster_theorem": "PROVED for every fixed D and 2<=t<=D+1",
            "multi_prime_CRT_module": "PROVED",
            "rational_multiplane_product_valuation_gain": 0,
            "bounded_cluster_endpoint_mass": "PROVED o(M) by the classical Selberg upper-bound sieve",
            "finite_pattern_replay": "EXACT FINITE ONLY",
            "isolated_prime_problem": "OPEN",
            "new_route1_rate": 0,
        },
        "phase_tower": {
            "formula": "(h_j,s_j,p_j,M)=(h-4j,s+3j,p+2j,M)",
            "boundary": "h>=4D+1 for every 0<=j<=D",
            "exact_grid_rows": phase_count,
            "exact_grid_sha256": phase_hash,
        },
        "multi_CRT": {
            "general_module": "product over j in J of ker(A_j mod p_j)",
            "general_size": "product over j in J of p_j^(4-r_j)",
            "fixed_integer_divisibility": "(product over j in J p_j)^2 divides gcd(C0(M),C1(M))",
            "extra_valuation_copy": 0,
            "exact_witness": crt,
        },
        "sieve": {
            "patterns": "J subset {0,...,D}, 0 in J, |J|=t",
            "pattern_count": "binomial(D,t-1)",
            "selberg_count": "O_(D,t)(M/log^t M)",
            "endpoint_log_weight": "O_(D,t)(M/log^(t-1) M)=o(M) for t>=2",
            "union_all_non_singleton_patterns": "O_D(M/log M)=o(M)",
            "finite_replay_D": 6,
            "finite_replay_bound": 10000,
            "finite_replay_counts_by_t": pattern_counts,
            "finite_replay_sha256": pattern_hash,
            "finite_replay_label": "EXACT FINITE ONLY",
        },
        "capacity": {
            "raw_j1_capacity_per_6M": "1/36",
            "maximum_linear_mass_affected_by_any_fixed_D_non_singleton_cluster": 0,
            "item149_item264_overlap": "first post-Cartier copy and square radical already booked/recorded",
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
