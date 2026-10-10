#!/usr/bin/env python3
"""Portable exact certificate for Item 275.

All calculations use rational arithmetic in the Python standard library.
The declared small witnesses are exact identities, not density evidence.
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
    HERE / "item275_j1_grassmannian_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item275_j1_grassmannian_certificate.json"
)
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def identity(size: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def mmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((x * y for x, y in zip(row, column)), Fraction()) for column in zip(*right)]
        for row in left
    ]


def madd(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[x + y for x, y in zip(row, other)] for row, other in zip(left, right)]


def matrix_vector(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((x * y for x, y in zip(row, vector)), Fraction()) for row in matrix]


def inverse(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(matrix)
    rows = [list(map(Fraction, row)) + identity(size)[index] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(index for index in range(column, size) if rows[index][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        divisor = rows[column][column]
        rows[column] = [entry / divisor for entry in rows[column]]
        for index in range(size):
            if index != column and rows[index][column]:
                multiplier = rows[index][column]
                rows[index] = [
                    entry - multiplier * pivot_entry
                    for entry, pivot_entry in zip(rows[index], rows[column])
                ]
    return [row[size:] for row in rows]


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    rows = [list(map(Fraction, row)) for row in matrix]
    value = Fraction(1)
    sign = 1
    for column in range(len(rows)):
        pivot = next(index for index in range(column, len(rows)) if rows[index][column])
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            sign = -sign
        pivot_value = rows[column][column]
        value *= pivot_value
        for index in range(column + 1, len(rows)):
            multiplier = rows[index][column] / pivot_value
            for j in range(column + 1, len(rows)):
                rows[index][j] -= multiplier * rows[column][j]
    return sign * value


def rank(matrix: list[list[Fraction]]) -> int:
    rows = [list(map(Fraction, row)) for row in matrix]
    result = 0
    for column in range(len(rows[0])):
        pivot = next((index for index in range(result, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[result], rows[pivot] = rows[pivot], rows[result]
        divisor = rows[result][column]
        rows[result] = [entry / divisor for entry in rows[result]]
        for index in range(len(rows)):
            if index != result and rows[index][column]:
                multiplier = rows[index][column]
                rows[index] = [
                    entry - multiplier * pivot_entry
                    for entry, pivot_entry in zip(rows[index], rows[result])
                ]
        result += 1
    return result


def tail_step(index: int, h_value: int, s_value: int) -> list[list[Fraction]]:
    denominator = Fraction(index + 2)
    return [
        [
            Fraction(1 - 2 * h_value, denominator),
            Fraction(-2 * h_value - 1 + 4 * s_value, denominator),
            Fraction(1 - 2 * h_value, denominator),
            Fraction(index - 2 * h_value - 4 * s_value - 3, denominator),
        ],
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
    ]


def endpoint_transfer(h_value: int, s_value: int) -> list[list[Fraction]]:
    T = 2 * h_value + 6 * s_value + 2
    E = 4 * h_value + 4 * s_value + 3
    out = identity(4)
    if E >= T:
        for index in range(T, E):
            out = mmul(tail_step(index, h_value, s_value), out)
        return out
    for index in range(E, T):
        out = mmul(tail_step(index, h_value, s_value), out)
    return inverse(out)


def reduced_gate(h_value: int, s_value: int) -> list[list[Fraction]]:
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
    return madd(
        [list(map(Fraction, row)) for row in left],
        mmul([list(map(Fraction, row)) for row in right], endpoint_transfer(h_value, s_value)),
    )


def parameter_shift(h_value: int, s_value: int, kind: str) -> list[list[Fraction]]:
    T = 2 * h_value + 6 * s_value + 2
    if kind == "h":
        endpoint_shift, multiplier = 2, {0: 1, 1: -2, 2: 1}
    elif kind == "s":
        endpoint_shift, multiplier = 6, {0: 1, 2: 2, 4: 1}
    else:
        raise ValueError(kind)
    basis = identity(4)
    vectors = {1: basis[0], 0: basis[1], -1: basis[2], -2: basis[3]}
    for offset in range(2, endpoint_shift + 2):
        vectors[offset] = [
            (
                (1 - 2 * h_value) * vectors[offset - 1][column]
                + (-2 * h_value - 1 + 4 * s_value) * vectors[offset - 2][column]
                + (1 - 2 * h_value) * vectors[offset - 3][column]
                + (T + offset - 2 * h_value - 4 * s_value - 5)
                * vectors[offset - 4][column]
            )
            / Fraction(T + offset)
            for column in range(4)
        ]
    return [
        [
            sum(
                (
                    Fraction(coefficient) * vectors[output_offset - input_offset][column]
                    for input_offset, coefficient in multiplier.items()
                ),
                Fraction(),
            )
            for column in range(4)
        ]
        for output_offset in (
            endpoint_shift + 1,
            endpoint_shift,
            endpoint_shift - 1,
            endpoint_shift - 2,
        )
    ]


def fixed_M_shift(h_value: int, s_value: int) -> list[list[Fraction]]:
    if h_value < 5:
        raise ValueError("the (-4,+3) chart requires h>=5")
    out = identity(4)
    for h_base in (h_value - 1, h_value - 2, h_value - 3, h_value - 4):
        out = mmul(inverse(parameter_shift(h_base, s_value, "h")), out)
    for s_base in (s_value, s_value + 1, s_value + 2):
        out = mmul(parameter_shift(h_value - 4, s_base, "s"), out)
    return out


def row_plucker(gate: list[list[Fraction]]) -> list[Fraction]:
    return [
        gate[0][i] * gate[1][j] - gate[0][j] * gate[1][i]
        for i, j in PAIRS
    ]


def kernel_plucker(gate: list[list[Fraction]]) -> list[Fraction]:
    delta12, delta13, delta14, delta23, delta24, delta34 = row_plucker(gate)
    return [delta34, -delta24, delta23, delta14, -delta13, delta12]


def wedge_square(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [
            matrix[i][a] * matrix[j][b] - matrix[i][b] * matrix[j][a]
            for a, b in PAIRS
        ]
        for i, j in PAIRS
    ]


def plucker_relation(values: list[Fraction]) -> Fraction:
    k12, k13, k14, k23, k24, k34 = values
    return k12 * k34 - k13 * k24 + k14 * k23


def incidence(vector: list[Fraction], values: list[Fraction]) -> list[Fraction]:
    x1, x2, x3, x4 = vector
    k12, k13, k14, k23, k24, k34 = values
    return [
        x1 * k23 - x2 * k13 + x3 * k12,
        x1 * k24 - x2 * k14 + x4 * k12,
        x1 * k34 - x3 * k14 + x4 * k13,
        x2 * k34 - x3 * k24 + x4 * k23,
    ]


def normalize(values: list[Fraction]) -> list[int]:
    denominator = 1
    for value in values:
        denominator = math.lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in values]
    common = 0
    for value in integers:
        common = math.gcd(common, abs(value))
    if not common:
        return integers
    integers = [value // common for value in integers]
    first = next(value for value in integers if value)
    return integers if first > 0 else [-value for value in integers]


def proportional(left: list[Fraction], right: list[Fraction]) -> bool:
    ratio: Fraction | None = None
    for x, y in zip(left, right):
        if y:
            if ratio is None:
                ratio = x / y
            elif x != ratio * y:
                return False
        elif x:
            return False
    return ratio is not None


def diagonal_family_check() -> str:
    digest = hashlib.sha256()
    for value in range(1, 13):
        gate = reduced_gate(value, value)
        expected_gate = [
            [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
            [
                Fraction(4 * value + 3),
                Fraction(22 * value + 5),
                Fraction(12 * value - 3),
                Fraction(-6 * value + 3),
            ],
        ]
        expected_plucker = [
            0,
            6 * value - 3,
            12 * value - 3,
            0,
            0,
            -4 * value - 3,
        ]
        if gate != expected_gate or kernel_plucker(gate) != list(map(Fraction, expected_plucker)):
            raise AssertionError((value, gate, kernel_plucker(gate)))
        if plucker_relation(kernel_plucker(gate)):
            raise AssertionError("diagonal Plucker relation")
        digest.update((repr((value, gate, expected_plucker)) + "\n").encode("ascii"))
    return digest.hexdigest()


def local_transport_witnesses() -> dict[str, Any]:
    old_gate = reduced_gate(1, 1)
    old_plucker = kernel_plucker(old_gate)
    if old_gate != [[0, 1, 0, 0], [7, 27, 9, -3]]:
        raise AssertionError(old_gate)
    if normalize(old_plucker) != [0, 3, 9, 0, 0, -7]:
        raise AssertionError(old_plucker)
    if any(any(incidence(vector, old_plucker)) for vector in (
        [Fraction(-9), Fraction(0), Fraction(7), Fraction(0)],
        [Fraction(3), Fraction(0), Fraction(0), Fraction(7)],
    )):
        raise AssertionError("flag incidence basis")
    if not any(incidence([Fraction(0), Fraction(1), Fraction(0), Fraction(0)], old_plucker)):
        raise AssertionError("outside incidence")

    expected = {
        "h": {
            "target_h_s": [2, 1],
            "pulled_kernel_plucker": [1565, -5870, -17959, -12915, -42296, 10439],
            "stack_determinant": "604/1365",
        },
        "s": {
            "target_h_s": [1, 2],
            "pulled_kernel_plucker": [595, -427, 1090, 812, -1475, -429],
            "stack_determinant": "-7568/1365",
        },
    }
    out: dict[str, Any] = {}
    for kind, target in (("h", (2, 1)), ("s", (1, 2))):
        shift = parameter_shift(1, 1, kind)
        pulled_gate = mmul(reduced_gate(*target), shift)
        pulled_plucker = kernel_plucker(pulled_gate)
        stack_determinant = determinant(old_gate + pulled_gate)
        data = {
            "target_h_s": list(target),
            "pulled_kernel_plucker": normalize(pulled_plucker),
            "stack_determinant": str(stack_determinant),
        }
        if data != expected[kind] or not stack_determinant:
            raise AssertionError((kind, data))
        if proportional(old_plucker, pulled_plucker):
            raise AssertionError("false horizontality")

        # The exterior-square law itself is exact: transporting the old
        # plane agrees with the kernel of the transported old covectors.
        transported = matrix_vector(wedge_square(shift), old_plucker)
        image_gate = mmul(old_gate, inverse(shift))
        if not proportional(transported, kernel_plucker(image_gate)):
            raise AssertionError("exterior-square transport law")
        if determinant(wedge_square(shift)) != determinant(shift) ** 3:
            raise AssertionError("exterior determinant")
        out[kind] = data
    return out


def fixed_M_witness() -> dict[str, Any]:
    old_h, old_s = 5, 1
    new_h, new_s = 1, 4
    if 3 * old_h + 4 * old_s + 2 != 21 or 3 * new_h + 4 * new_s + 2 != 21:
        raise AssertionError("fixed M")
    if 4 * old_h + 6 * old_s + 3 != 29 or 4 * new_h + 6 * new_s + 3 != 31:
        raise AssertionError("actual adjacent primes")
    shift = fixed_M_shift(old_h, old_s)
    old_gate = reduced_gate(old_h, old_s)
    pulled_gate = mmul(reduced_gate(new_h, new_s), shift)
    data = {
        "old_h_s_p_M": [5, 1, 29, 21],
        "new_h_s_p_M": [1, 4, 31, 21],
        "old_kernel_plucker": normalize(kernel_plucker(old_gate)),
        "pulled_kernel_plucker": normalize(kernel_plucker(pulled_gate)),
        "stack_determinant": str(determinant(old_gate + pulled_gate)),
    }
    expected = {
        "old_h_s_p_M": [5, 1, 29, 21],
        "new_h_s_p_M": [1, 4, 31, 21],
        "old_kernel_plucker": [966875, -83743035, -928364750, 8571696, 84169225, 940218807],
        "pulled_kernel_plucker": [1162220187, 411657489, -1265521434, -8518535856, 9022899625, -6079782117],
        "stack_determinant": "-585482135072/1165539375",
    }
    if data != expected or not determinant(old_gate + pulled_gate):
        raise AssertionError(data)
    if plucker_relation(kernel_plucker(old_gate)) or plucker_relation(kernel_plucker(pulled_gate)):
        raise AssertionError("fixed-M Plucker relation")
    if determinant(wedge_square(shift)) != determinant(shift) ** 3:
        raise AssertionError("fixed-M exterior determinant")
    return data


def rank_strata_check() -> dict[str, Any]:
    rank_one = [[Fraction(1), Fraction(2), Fraction(3), Fraction(4)],
                [Fraction(2), Fraction(4), Fraction(6), Fraction(8)]]
    rank_zero = [[Fraction(0)] * 4, [Fraction(0)] * 4]
    if rank(rank_one) != 1 or rank(rank_zero) != 0:
        raise AssertionError("rank examples")
    if any(kernel_plucker(rank_one)) or any(kernel_plucker(rank_zero)):
        raise AssertionError("Plucker collapse")
    return {
        "rank_2": "nonzero decomposable Plucker line encoding a two-plane kernel",
        "rank_1": "all six maximal minors vanish; the three-plane kernel is not encoded by K=0",
        "rank_0": "the same K=0 apex; the four-plane kernel is not distinguished",
        "state_zero": "x=0 lies in the affine incidence but has no projective state point",
    }


def certificate() -> dict[str, Any]:
    diagonal_hash = diagonal_family_check()
    local = local_transport_witnesses()
    fixed_M = fixed_M_witness()
    strata = rank_strata_check()
    body: dict[str, Any] = {
        "schema": "item275-j1-grassmannian-certificate-v1",
        "labels": {
            "fixed_flag_incidence": "PROVED on the rank-two, nonzero-state chart",
            "exterior_square_module": "PROVED rank 6 with inherited fixed singular support",
            "natural_plucker_line_horizontal": False,
            "lisse_or_frobenius_nonexistence": "NOT CLAIMED",
            "new_weighted_zero_theorem": 0,
            "new_route1_rate": 0,
        },
        "plucker": {
            "coordinate_order": ["12", "13", "14", "23", "24", "34"],
            "kernel_from_row_minors": "(Delta34,-Delta24,Delta23,Delta14,-Delta13,Delta12)",
            "quadric": "K12*K34-K13*K24+K14*K23=0",
            "incidence": [
                "x1*K23-x2*K13+x3*K12",
                "x1*K24-x2*K14+x4*K12",
                "x1*K34-x3*K14+x4*K13",
                "x2*K34-x3*K24+x4*K23",
            ],
            "independent_incidence_codimension": 2,
            "diagonal_family": {
                "G_t_t": "[[0,1,0,0],[4t+3,22t+5,12t-3,-6t+3]]",
                "K_t_t": "(0,6t-3,12t-3,0,0,-4t-3)",
                "exact_replay_sha256": diagonal_hash,
            },
        },
        "exterior_transport": {
            "rank": 6,
            "coordinate_formula": "(wedge^2 U)_(ij,ab)=U_ia U_jb-U_ib U_ja",
            "determinant": "det(wedge^2 U)=det(U)^3",
            "singular_support": "exactly the Item273 support, with multiplicities tripled",
            "local_nonhorizontal_witnesses": local,
            "fixed_M_prime_tied_witness": fixed_M,
        },
        "rank_strata": strata,
        "scope": {
            "proved_no_go": "the natural Plucker line is not a horizontal rank-one subobject of the exact Item273 exterior-square transports",
            "not_proved": "nonexistence of an enlarged sheaf, a different connection, or a finite-field-specific incidence theorem",
            "prime_tied_issue": "the fixed-M step changes p from 29 to 31 in the exact witness, so it is not an orbit inside one finite field",
        },
        "capacity": {
            "raw_j1_capacity_per_6M": "1/36",
            "item149_first_post_cartier_copy_already_booked": True,
            "fixed_window_exceptional_weight": "O_L(log M), inherited from Item273",
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
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "payload_sha256": result["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
