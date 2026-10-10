#!/usr/bin/env python3
"""Portable exact certificate for Item 273.

The structural identities are exact.  The bounded prime-row probes are
explicitly labelled EXACT FINITE ONLY and are not used for asymptotics.
Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item273_j1_fixed_incidence_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item273_j1_fixed_incidence_certificate.json"
)


def primes(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(bound) + 1):
        if sieve[prime]:
            sieve[prime * prime : bound + 1 : prime] = b"\x00" * (
                (bound - prime * prime) // prime + 1
            )
    return [value for value, flag in enumerate(sieve) if flag]


def actual_rows(bound: int):
    for prime in primes(bound):
        for s_value in range(1, (prime - 7) // 6 + 1):
            remainder = prime - 6 * s_value - 3
            if remainder > 0 and remainder % 4 == 0:
                yield prime, remainder // 4, s_value


def conv(left: list[int], right: list[int], modulus: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] = (out[i + j] + left_value * right_value) % modulus
    return out


def polynomial_power(base: list[int], exponent: int, modulus: int) -> list[int]:
    out = [1]
    value = [entry % modulus for entry in base]
    while exponent:
        if exponent & 1:
            out = conv(out, value, modulus)
        exponent //= 2
        if exponent:
            value = conv(value, value, modulus)
    return out


def coefficient_vectors(h_value: int, s_value: int, prime: int) -> tuple[list[int], list[int]]:
    T = 2 * h_value + 6 * s_value + 2
    L1 = 4 * h_value + 4 * s_value + 3
    maximum = max(T + 1, L1 + 1)
    p0 = conv(
        conv(
            polynomial_power([1, -1], 2 * h_value, prime),
            [1, 1],
            prime,
        ),
        polynomial_power([1, 0, 1], 2 * s_value, prime),
        prime,
    )
    p1 = conv(
        conv(
            polynomial_power([1, -1], 2 * h_value, prime),
            polynomial_power([1, 1], 4, prime),
            prime,
        ),
        polynomial_power([1, 0, 1], 2 * s_value - 1, prime),
        prime,
    )
    logarithm = [0] * (maximum + 1)
    for index in range(1, maximum // 2 + 1):
        logarithm[2 * index] = (
            (1 if index & 1 else -1) * pow(index, -1, prime)
        ) % prime
    return conv(p0, logarithm, prime), conv(p1, logarithm, prime)


def mmul(left: list[list[int]], right: list[list[int]], prime: int) -> list[list[int]]:
    return [
        [sum(x * y for x, y in zip(row, column)) % prime for column in zip(*right)]
        for row in left
    ]


def madd(left: list[list[int]], right: list[list[int]], prime: int) -> list[list[int]]:
    return [
        [(x + y) % prime for x, y in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def matrix_inverse(matrix: list[list[int]], prime: int) -> list[list[int]]:
    size = len(matrix)
    rows = [
        [entry % prime for entry in row] + identity(size)[index]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(index for index in range(column, size) if rows[index][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        inverse = pow(rows[column][column], -1, prime)
        rows[column] = [(entry * inverse) % prime for entry in rows[column]]
        for index in range(size):
            if index != column and rows[index][column]:
                multiplier = rows[index][column]
                rows[index] = [
                    (entry - multiplier * pivot_entry) % prime
                    for entry, pivot_entry in zip(rows[index], rows[column])
                ]
    return [row[size:] for row in rows]


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (index for index in range(rank, len(rows)) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(entry * inverse) % prime for entry in rows[rank]]
        for index in range(len(rows)):
            if index != rank and rows[index][column]:
                multiplier = rows[index][column]
                rows[index] = [
                    (entry - multiplier * pivot_entry) % prime
                    for entry, pivot_entry in zip(rows[index], rows[rank])
                ]
        rank += 1
    return rank


def tail_step(index: int, h_value: int, s_value: int, prime: int) -> list[list[int]]:
    denominator = pow(index + 2, -1, prime)
    first_row = [
        1 - 2 * h_value,
        -2 * h_value - 1 + 4 * s_value,
        1 - 2 * h_value,
        index - 2 * h_value - 4 * s_value - 3,
    ]
    return [
        [(entry * denominator) % prime for entry in first_row],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ]


def endpoint_transfer(h_value: int, s_value: int, prime: int) -> list[list[int]]:
    T = 2 * h_value + 6 * s_value + 2
    E = 4 * h_value + 4 * s_value + 3
    if E >= T:
        out = identity(4)
        for index in range(T, E):
            out = mmul(tail_step(index, h_value, s_value, prime), out, prime)
        return out
    out = identity(4)
    for index in range(E, T):
        out = mmul(tail_step(index, h_value, s_value, prime), out, prime)
    return matrix_inverse(out, prime)


def gate_blocks(h_value: int, s_value: int) -> tuple[list[list[int]], list[list[int]]]:
    left = [
        [0, 2, 0, 0],
        [
            4 * h_value + 12 * s_value + 6,
            8 * h_value + 20 * s_value + 2,
            4 * h_value + 4 * s_value - 2,
            2 - 4 * s_value,
        ],
    ]
    right = [
        [0, 0, -1, 0],
        [
            -4 * h_value - 4 * s_value - 4,
            -6 * h_value - 8 * s_value - 2,
            2 - 4 * s_value,
            2 * h_value,
        ],
    ]
    return left, right


def reduced_gate(h_value: int, s_value: int, prime: int) -> list[list[int]]:
    left, right = gate_blocks(h_value, s_value)
    return madd(left, mmul(right, endpoint_transfer(h_value, s_value, prime), prime), prime)


def direct_gate_replay(bound: int = 200) -> tuple[int, str, dict[str, Any]]:
    digest = hashlib.sha256()
    count = 0
    norm_witness: dict[str, Any] | None = None
    for prime, h_value, s_value in actual_rows(bound):
        f0, f1 = coefficient_vectors(h_value, s_value, prime)
        T = 2 * h_value + 6 * s_value + 2
        L0 = 4 * h_value + 4 * s_value + 2
        E = L0 + 1
        state_T = [[f0[T + 1]], [f0[T]], [f0[T - 1]], [f0[T - 2]]]
        state_E = [[f0[E + 1]], [f0[E]], [f0[E - 1]], [f0[E - 2]]]
        transfer_state = mmul(endpoint_transfer(h_value, s_value, prime), state_T, prime)
        if transfer_state != state_E:
            raise AssertionError((prime, h_value, s_value, transfer_state, state_E))
        q0 = (2 * f0[T] - f0[L0]) % prime
        q1 = (2 * f1[T] - f1[E]) % prime
        left, right = gate_blocks(h_value, s_value)
        incidence = madd(mmul(left, state_T, prime), mmul(right, state_E, prime), prime)
        if incidence != [[q0], [(4 * s_value * q1) % prime]]:
            raise AssertionError((prime, h_value, s_value, incidence, q0, q1))
        reduced = mmul(reduced_gate(h_value, s_value, prime), state_T, prime)
        if reduced != incidence:
            raise AssertionError((prime, h_value, s_value, reduced, incidence))
        if matrix_rank([left[0] + right[0], left[1] + right[1]], prime) != 2:
            raise AssertionError("ambient rank")
        if (
            prime % 4 == 1
            and (q0, q1) != (0, 0)
            and (q0 * q0 + q1 * q1) % prime == 0
            and norm_witness is None
        ):
            norm_witness = {
                "p_h_s": [prime, h_value, s_value],
                "Q0_Q1": [q0, q1],
                "sqrt_minus_one_ratio_Q1_over_Q0": q1 * pow(q0, -1, prime) % prime,
            }
        digest.update((repr((prime, h_value, s_value, q0, q1)) + "\n").encode("ascii"))
        count += 1
    expected = {
        "p_h_s": [61, 10, 3],
        "Q0_Q1": [46, 18],
        "sqrt_minus_one_ratio_Q1_over_Q0": 11,
    }
    if norm_witness != expected:
        raise AssertionError(norm_witness)
    return count, digest.hexdigest(), expected


def rank_probe(bound: int = 1000) -> tuple[list[int], str]:
    counts = [0, 0, 0]
    digest = hashlib.sha256()
    for prime, h_value, s_value in actual_rows(bound):
        gate = reduced_gate(h_value, s_value, prime)
        rank = matrix_rank(gate, prime)
        counts[rank] += 1
        digest.update((repr((prime, h_value, s_value, rank, gate)) + "\n").encode("ascii"))
    if counts != [0, 0, 6258]:
        raise AssertionError(counts)
    return counts, digest.hexdigest()


def fraction_determinant(matrix: list[list[Fraction]]) -> Fraction:
    rows = [list(map(Fraction, row)) for row in matrix]
    sign = 1
    value = Fraction(1)
    for column in range(len(rows)):
        pivot = next(index for index in range(column, len(rows)) if rows[index][column])
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            sign = -sign
        pivot_value = rows[column][column]
        value *= pivot_value
        for index in range(column + 1, len(rows)):
            if rows[index][column]:
                multiplier = rows[index][column] / pivot_value
                for j in range(column + 1, len(rows)):
                    rows[index][j] -= multiplier * rows[column][j]
    return sign * value


def fraction_vectors(h_value: int, s_value: int, endpoint: int, maximum: int) -> dict[int, list[Fraction]]:
    vectors: dict[int, list[Fraction]] = {
        1: [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        0: [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        -1: [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        -2: [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    }
    a0 = 1 - 2 * h_value
    a1 = -2 * h_value - 1 + 4 * s_value
    a2 = 1 - 2 * h_value
    for offset in range(2, maximum + 1):
        denominator = endpoint + offset
        vectors[offset] = [
            (
                a0 * vectors[offset - 1][column]
                + a1 * vectors[offset - 2][column]
                + a2 * vectors[offset - 3][column]
                + (endpoint + offset - 2 * h_value - 4 * s_value - 5)
                * vectors[offset - 4][column]
            )
            / denominator
            for column in range(4)
        ]
    return vectors


def parameter_shift_matrix(
    h_value: int,
    s_value: int,
    endpoint: int,
    endpoint_shift: int,
    multiplier: dict[int, int],
) -> list[list[Fraction]]:
    vectors = fraction_vectors(h_value, s_value, endpoint, endpoint_shift + 1)
    rows: list[list[Fraction]] = []
    for output_offset in (
        endpoint_shift + 1,
        endpoint_shift,
        endpoint_shift - 1,
        endpoint_shift - 2,
    ):
        rows.append(
            [
                sum(
                    coefficient * vectors[output_offset - input_offset][column]
                    for input_offset, coefficient in multiplier.items()
                )
                for column in range(4)
            ]
        )
    return rows


def claimed_parameter_determinant(name: str, h_value: int, s_value: int) -> Fraction:
    h, s = h_value, s_value
    values = {
        "hT": Fraction(16 * (h + 1) * (2 * h + 1), (h + 3 * s + 2) * (2 * h + 6 * s + 5)),
        "hE": Fraction(
            8 * h * (h + 1) * (2 * h + 1) ** 2,
            (h + s + 2) * (2 * h + 2 * s + 3) * (4 * h + 4 * s + 5) * (4 * h + 4 * s + 7),
        ),
        "sT": Fraction(
            256 * s * (s + 1) ** 2 * (2 * s - 1) * (2 * s + 1) ** 2,
            (h + 3 * s + 2)
            * (h + 3 * s + 3)
            * (h + 3 * s + 4)
            * (2 * h + 6 * s + 5)
            * (2 * h + 6 * s + 7)
            * (2 * h + 6 * s + 9),
        ),
        "sE": Fraction(
            128 * (s + 1) ** 2 * (2 * s + 1) ** 2,
            (h + s + 2) * (2 * h + 2 * s + 3) * (4 * h + 4 * s + 5) * (4 * h + 4 * s + 7),
        ),
    }
    return values[name]


def parameter_module_grid() -> tuple[dict[str, int], str]:
    cases = {
        "hT": (lambda h, s: 2 * h + 6 * s + 2, 2, {0: 1, 1: -2, 2: 1}),
        "hE": (lambda h, s: 4 * h + 4 * s + 3, 4, {0: 1, 1: -2, 2: 1}),
        "sT": (lambda h, s: 2 * h + 6 * s + 2, 6, {0: 1, 2: 2, 4: 1}),
        "sE": (lambda h, s: 4 * h + 4 * s + 3, 4, {0: 1, 2: 2, 4: 1}),
    }
    counts: dict[str, int] = {}
    digest = hashlib.sha256()
    # After the row denominators are cleared, each determinant identity has
    # bidegree at most 24.  A 25 by 25 rational grid is therefore a complete
    # polynomial-identity certificate, not a numerical fit.
    for name, (endpoint_function, shift, multiplier) in cases.items():
        count = 0
        for h_value in range(1, 26):
            for s_value in range(1, 26):
                endpoint = endpoint_function(h_value, s_value)
                matrix = parameter_shift_matrix(
                    h_value, s_value, endpoint, shift, multiplier
                )
                determinant = fraction_determinant(matrix)
                expected = claimed_parameter_determinant(name, h_value, s_value)
                if determinant != expected:
                    raise AssertionError((name, h_value, s_value, determinant, expected))
                digest.update((repr((name, h_value, s_value, determinant)) + "\n").encode("ascii"))
                count += 1
        counts[name] = count
    return counts, digest.hexdigest()


def singular_support_audit(bound: int = 1000) -> dict[str, Any]:
    denominator_factors = {
        "h+3s+2": lambda h, s: h + 3 * s + 2,
        "h+3s+3": lambda h, s: h + 3 * s + 3,
        "h+3s+4": lambda h, s: h + 3 * s + 4,
        "2h+6s+5": lambda h, s: 2 * h + 6 * s + 5,
        "2h+6s+7": lambda h, s: 2 * h + 6 * s + 7,
        "2h+6s+9": lambda h, s: 2 * h + 6 * s + 9,
        "h+s+2": lambda h, s: h + s + 2,
        "2h+2s+3": lambda h, s: 2 * h + 2 * s + 3,
        "4h+4s+5": lambda h, s: 4 * h + 4 * s + 5,
        "4h+4s+7": lambda h, s: 4 * h + 4 * s + 7,
    }
    expected_conditions = {
        "2h+6s+5": "h=1",
        "2h+6s+7": "h=2",
        "2h+6s+9": "h=3",
        "4h+4s+5": "s=1",
        "4h+4s+7": "s=2",
    }
    observed: dict[str, set[tuple[int, int]]] = {name: set() for name in denominator_factors}
    numerator_factors = [
        lambda h, s: h,
        lambda h, s: h + 1,
        lambda h, s: 2 * h + 1,
        lambda h, s: s,
        lambda h, s: s + 1,
        lambda h, s: 2 * s - 1,
        lambda h, s: 2 * s + 1,
    ]
    for prime, h_value, s_value in actual_rows(bound):
        for name, factor in denominator_factors.items():
            if factor(h_value, s_value) % prime == 0:
                observed[name].add((h_value, s_value))
        if any(factor(h_value, s_value) % prime == 0 for factor in numerator_factors):
            raise AssertionError("numerator singular factor")
    for name, pairs in observed.items():
        if name not in expected_conditions and pairs:
            raise AssertionError((name, pairs))
        if name == "2h+6s+5" and any(h != 1 for h, _ in pairs):
            raise AssertionError((name, pairs))
        if name == "2h+6s+7" and any(h != 2 for h, _ in pairs):
            raise AssertionError((name, pairs))
        if name == "2h+6s+9" and any(h != 3 for h, _ in pairs):
            raise AssertionError((name, pairs))
        if name == "4h+4s+5" and any(s != 1 for _, s in pairs):
            raise AssertionError((name, pairs))
        if name == "4h+4s+7" and any(s != 2 for _, s in pairs):
            raise AssertionError((name, pairs))
    return {
        "actual_pole_edges": expected_conditions,
        "all_determinant_numerator_factors_are_actual_units_through_bound": bound,
        "fixed_M_container": "2(alpha h+beta s+gamma) == (6alpha-4beta)M+(2gamma-beta) mod p",
    }


def certificate() -> dict[str, Any]:
    direct_count, direct_hash, norm_witness = direct_gate_replay()
    rank_counts, rank_hash = rank_probe()
    grid_counts, grid_hash = parameter_module_grid()
    singular = singular_support_audit()
    body: dict[str, Any] = {
        "schema": "item273-j1-fixed-incidence-certificate-v1",
        "labels": {
            "tail_module_and_incidence": "PROVED",
            "parameter_difference_realization": "PROVED rank at most 8 with fixed singular support",
            "scalar_divisor_obstruction": "PROVED on the generic rank-two graph chart",
            "bounded_prime_replays": "EXACT FINITE ONLY",
            "new_weighted_zero_theorem": 0,
            "new_route1_rate": 0,
        },
        "actual_family": {
            "phase": "p=4h+6s+3, h,s>=1",
            "global_index": "M=3h+4s+2; 4M+1=3p-2s",
            "prime_interval": "(4M+3)/3 <= p <= (3M-1)/2",
            "raw_log_weight": "M/6+o(M)",
            "raw_normalized_capacity_per_6M": "1/36",
        },
        "incidence": {
            "state": "Y=(S_T,S_(L+1)), S_n=(f_(n+1),f_n,f_(n-1),f_(n-2))",
            "row_Q0": [0, 2, 0, 0, 0, 0, -1, 0],
            "row_4sQ1": [
                "4h+12s+6", "8h+20s+2", "4h+4s-2", "2-4s",
                "-4h-4s-4", "-6h-8s-2", "2-4s", "2h",
            ],
            "ambient_rank_on_actual_rows": 2,
            "ambient_rank_witness_unit": "4h+12s+6 == 6s+3 mod p, with 0<6s+3<p",
            "reduced_rank_branches_retained": [0, 1, 2],
        },
        "tail_module": {
            "ode": "(1-z^4)F'-a(z)F=2z(1-z^2)P0",
            "a_coefficients_low_to_high": ["1-2h", "-2h-1+4s", "1-2h", "-2h-1-4s"],
            "rank": 4,
            "step_determinant": "(2h+4s+3-n)/(n+2)",
            "actual_transfer": "homogeneous and invertible; affine forcing branch empty on the actual endpoint corridor",
        },
        "parameter_module": {
            "rank_upper_bound": 8,
            "h_multiplier": "(1-z)^2",
            "s_multiplier": "(1+z^2)^2",
            "determinants": {
                "hT": "16(h+1)(2h+1)/((h+3s+2)(2h+6s+5))",
                "hE": "8h(h+1)(2h+1)^2/((h+s+2)(2h+2s+3)(4h+4s+5)(4h+4s+7))",
                "sT": "256s(s+1)^2(2s-1)(2s+1)^2/((h+3s+2)(h+3s+3)(h+3s+4)(2h+6s+5)(2h+6s+7)(2h+6s+9))",
                "sE": "128(s+1)^2(2s+1)^2/((h+s+2)(2h+2s+3)(4h+4s+5)(4h+4s+7))",
            },
            "identity_grid": {
                "method": "25x25 exact rational grid after a proved bidegree-at-most-24 clearing bound",
                "counts": grid_counts,
                "sha256": grid_hash,
            },
            "singular_support": singular,
        },
        "scalar_divisor": {
            "generic_gate_ideal": "two independent linear forms in four graph-state variables; height 2 and nonprincipal",
            "scope": "no single polynomial has exactly the collision zero set on the generic algebraically closed graph chart",
            "not_excluded": "finite-field-specific compression, sheaf/determinantal encoding, or a theorem for a necessary larger divisor",
            "split_norm_extra_branch_witness": norm_witness,
        },
        "finite_replay": {
            "label": "EXACT FINITE ONLY",
            "direct_gate_rows_p_le_200": direct_count,
            "direct_gate_sha256": direct_hash,
            "reduced_rank_rows_p_le_1000_by_rank_0_1_2": rank_counts,
            "reduced_rank_sha256": rank_hash,
            "asymptotic_inference": False,
        },
        "booking": {
            "item149_first_post_cartier_copy_already_booked": True,
            "exceptional_factor_weight_for_fixed_window": "O_L(log M)",
            "j1_raw_ceiling_after_item273": "unchanged at 1/36 per 6M",
            "new_weighted_zero_theorem": 0,
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
    print(
        json.dumps(
            {
                "status": "PASS",
                "output": str(args.output),
                "payload_sha256": result["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
