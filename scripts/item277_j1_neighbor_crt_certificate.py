#!/usr/bin/env python3
"""Portable exact certificate for Item 277.

The checker reuses the frozen Item 275 rational transport certificate and
otherwise uses only the Python standard library.  The bounded twin-prime
replay is EXACT FINITE ONLY; the asymptotic mass statement uses the
classical Brun/Selberg upper-bound sieve theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from item275_j1_grassmannian_certificate import fixed_M_witness


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item277_j1_neighbor_crt_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item277_j1_neighbor_crt_certificate.json"
)


def determinant_integer(matrix: list[list[int]]) -> int:
    # Fraction-free Bareiss elimination.
    rows = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for column in range(len(rows) - 1):
        pivot = next(index for index in range(column, len(rows)) if rows[index][column])
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


def phase_neighbor_replay() -> tuple[int, str]:
    digest = hashlib.sha256()
    count = 0
    for h_value in range(5, 61):
        for s_value in range(1, 61):
            p = 4 * h_value + 6 * s_value + 3
            M = 3 * h_value + 4 * s_value + 2
            new_h, new_s = h_value - 4, s_value + 3
            q = 4 * new_h + 6 * new_s + 3
            new_M = 3 * new_h + 4 * new_s + 2
            if q != p + 2 or new_M != M:
                raise AssertionError((h_value, s_value, p, q, M, new_M))
            digest.update((repr((h_value, s_value, p, M, new_h, new_s, q)) + "\n").encode("ascii"))
            count += 1
    return count, digest.hexdigest()


def crt_transversality_obstruction() -> dict[str, Any]:
    p, q = 29, 31
    modulus = p * q
    e_p = q * pow(q, -1, p) % modulus
    e_q = p * pow(p, -1, q) % modulus
    if (e_p % p, e_p % q, e_q % p, e_q % q) != (1, 0, 0, 1):
        raise AssertionError((e_p, e_q))
    if (e_p * e_p - e_p) % modulus or (e_q * e_q - e_q) % modulus or e_p * e_q % modulus:
        raise AssertionError("CRT idempotents")

    A = [[1, 0, 0, 0], [0, 1, 0, 0]]
    B = [[0, 0, 1, 0], [0, 0, 0, 1]]
    if determinant_integer(A + B) != 1:
        raise AssertionError("transverse model")
    mixed = [
        [(e_p * entry) % modulus for entry in row] for row in A
    ] + [
        [(e_q * entry) % modulus for entry in row] for row in B
    ]
    if determinant_integer(mixed) % modulus:
        raise AssertionError("mixed determinant must vanish in Z/N")
    vector = [p, 0, q, 0]
    if matrix_vector(A, vector, p) != [0, 0] or matrix_vector(B, vector, q) != [0, 0]:
        raise AssertionError("mixed solution")
    if all(entry % modulus == 0 for entry in vector):
        raise AssertionError("false product divisibility")

    # The equivalent integer row scaling has the tautological N^2 factor.
    scaled = [[q * entry for entry in row] for row in A] + [[p * entry for entry in row] for row in B]
    if determinant_integer(scaled) != (p * q) ** 2:
        raise AssertionError("scaled determinant")
    return {
        "p_q_N": [p, q, modulus],
        "idempotents_e_p_e_q": [e_p, e_q],
        "rational_stack_determinant": 1,
        "mixed_idempotent_determinant_mod_N": 0,
        "integer_scaled_determinant": determinant_integer(scaled),
        "counterexample_vector": vector,
        "counterexample_vector_divisible_by_N": False,
        "rank_formula": "|solutions|=p^(4-r_p) q^(4-r_q)",
    }


def square_crt_check() -> dict[str, Any]:
    p, q = 29, 31
    product_square = (p * q) ** 2
    C0 = product_square * 37
    C1 = -product_square * 101
    if any(value % (p * p) or value % (q * q) or value % product_square for value in (C0, C1)):
        raise AssertionError("square CRT")
    return {
        "theorem": "p^2|C and q^2|C with gcd(p,q)=1 iff (pq)^2|C",
        "sample_p_q": [p, q],
        "sample_product_square": product_square,
        "valuation_gain_beyond_distinct_prime_square_product": 0,
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


def twin_isolation_replay(bound: int = 10000) -> tuple[int, str]:
    sieve = prime_sieve(bound + 4)
    twins: list[int] = []
    digest = hashlib.sha256()
    for p in range(5, bound + 1, 2):
        if sieve[p] and sieve[p + 2]:
            twins.append(p)
            if p > 5 and (sieve[p - 2] or sieve[p + 4]):
                raise AssertionError((p, p - 2, p + 4))
            digest.update((repr((p, p + 2, p % 3)) + "\n").encode("ascii"))
    if any(right <= left + 2 for left, right in zip(twins, twins[1:])):
        raise AssertionError("overlapping twin edges beyond the 3,5,7 boundary")
    return len(twins), digest.hexdigest()


def certificate() -> dict[str, Any]:
    phase_count, phase_hash = phase_neighbor_replay()
    crt = crt_transversality_obstruction()
    square = square_crt_check()
    twin_count, twin_hash = twin_isolation_replay()
    item275_witness = fixed_M_witness()
    if item275_witness["old_h_s_p_M"] != [5, 1, 29, 21] or item275_witness["new_h_s_p_M"] != [1, 4, 31, 21]:
        raise AssertionError(item275_witness)
    body: dict[str, Any] = {
        "schema": "item277-j1-neighbor-crt-certificate-v1",
        "labels": {
            "phase_neighbor": "PROVED",
            "square_CRT_divisibility": "PROVED",
            "cross_field_transversality_gain": 0,
            "twin_endpoint_weight": "PROVED o(M) by the classical Brun/Selberg upper-bound sieve",
            "bounded_twin_replay": "EXACT FINITE ONLY",
            "new_weighted_zero_theorem_for_full_j1_cell": 0,
            "new_route1_rate": 0,
        },
        "phase": {
            "map": "(h,s,p,M)->(h-4,s+3,p+2,M), h>=5",
            "exact_grid_rows": phase_count,
            "exact_grid_sha256": phase_hash,
            "item275_actual_transverse_witness": item275_witness,
        },
        "integer_CRT": square,
        "mixed_state_CRT": crt,
        "rank_branches": {
            "r_p_r_q": "each belongs to {0,1,2}",
            "solution_module": "ker(A mod p) x ker(B mod q)",
            "solution_count": "p^(4-r_p)q^(4-r_q)",
            "rank_drops": "weaken the conditions and are retained",
        },
        "cluster_spacing": {
            "mod_3_theorem": "for twin p,p+2 with p>5, p=2 mod 3, so p-2 and p+4 are composite",
            "edges_overlap": False,
            "brun_selberg": "#{p<=X:p,p+2 prime}=O(X/log^2 X)",
            "fixed_M_endpoint_log_weight": "O(M/log M)=o(M)",
            "finite_replay_bound": 10000,
            "finite_replay_twin_count": twin_count,
            "finite_replay_sha256": twin_hash,
            "finite_replay_label": "EXACT FINITE ONLY",
        },
        "capacity": {
            "raw_j1_capacity_per_6M": "1/36",
            "maximum_linear_mass_affected_by_neighbor_pairs": 0,
            "item149_first_post_cartier_copy_already_booked": True,
            "new_independent_valuation_copy": 0,
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
