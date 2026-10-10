#!/usr/bin/env python3
"""Deterministic replay for Item 382.

The checker constructs the unique order-three operator candidates in a
declared polynomial ansatz for the four unreduced carrier subsequences,
verifies exact holdout identities, records modular rank minimality within
the declared search box, and checks the fixed-M shift/modulus alignment
barrier.  The operators remain finite certificates, not all-n theorems.

There is no prime scan, collision census, or operator extrapolation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item382_j1_explicit_operator_alignment_barrier_certificate.json"

DEPENDENCIES = {
    "sources/item379_j1_primitive_gcd_local_height_report.md":
        "478b630ba1f982982da35fc54e247aaa5624ecd8158eaf7f8c54e60d29c1d612",
    "scripts/item379_j1_primitive_gcd_local_height_certificate.py":
        "91ff429d4d1a19d17f30e9db0ce5d99c86be0544e929253dbe8360b2893c1ac3",
    "results/item379_j1_primitive_gcd_local_height_certificate.json":
        "697d5517f8b53d6c839e69bb4a41028e0f92bee20dbb34dca48f167366f7c5b4",
    "results/item379_j1_primitive_gcd_local_height_ledger_delta.json":
        "53f23a9baf27622bcecec8360b37095394d3bcc9790e0ebc1bc24140c9042a61",
    "results/item379_j1_primitive_gcd_local_height_root_audit.json":
        "8a6980357b6416f9d7254cf9a938bd06674f3eaa3c09e30debafecdba75f02fd",
    "manifests/item379_j1_primitive_gcd_local_height_manifest.json":
        "0b88be1406949605bc8d1f7e063c53a5eed49b131f95540cbef71337967cacca",
}

SPECS = (
    ("x", 1, 19),
    ("x", 2, 19),
    ("u", 1, 23),
    ("u", 2, 23),
)
ORDER = 3
FIT_SLACK = 8
HOLDOUT = 12
RANK_PRIME = 1_000_000_007
RECONSTRUCTION_PRIMES = (
    1_000_000_103,
    1_000_000_207,
    1_000_000_321,
    1_000_000_427,
    1_000_000_531,
    1_000_000_637,
    1_000_000_753,
    1_000_000_861,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify_dependencies()
ITEM379 = load_module(
    "item382_pinned_item379",
    ROOT / "scripts/item379_j1_primitive_gcd_local_height_certificate.py",
)
ITEM376 = ITEM379.ITEM376


def carrier_sequence(family: str, residue: int, length: int) -> list[int]:
    answer = []
    for index in range(length):
        h_value = 3 * index + residue
        if family == "x":
            kernel = ITEM376.ITEM364.ITEM218.kernel_integer(h_value, 1)
            numerator, _ = ITEM376.cleared_pair(kernel, h_value, h_value, 3)
        elif family == "u":
            kernel = ITEM376.ITEM364.ITEM218.kernel_integer(h_value, 4)
            numerator, _ = ITEM376.cleared_pair(
                kernel, h_value, h_value + 2, -3
            )
        else:
            raise ValueError(family)
        answer.append(numerator)
    return answer


def recurrence_matrix(
    sequence: list[int], order: int, degree: int, rows: int, prime: int
) -> list[list[int]]:
    matrix = []
    for index in range(rows):
        powers = [1]
        for _ in range(degree):
            powers.append(powers[-1] * index % prime)
        matrix.append(
            [
                sequence[index + shift] % prime * powers[power] % prime
                for shift in range(order + 1)
                for power in range(degree + 1)
            ]
        )
    return matrix


def rref_rank(matrix: list[list[int]], prime: int) -> int:
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], prime - 2, prime)
        for position in range(column, column_count):
            rows[pivot_row][position] = (
                rows[pivot_row][position] * inverse % prime
            )
        for row in range(pivot_row + 1, row_count):
            multiplier = rows[row][column]
            if multiplier:
                for position in range(column, column_count):
                    rows[row][position] = (
                        rows[row][position]
                        - multiplier * rows[pivot_row][position]
                    ) % prime
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def null_vector(matrix: list[list[int]], prime: int) -> tuple[list[int], int]:
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    pivots: list[int] = []
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], prime - 2, prime)
        for position in range(column, column_count):
            rows[pivot_row][position] = (
                rows[pivot_row][position] * inverse % prime
            )
        for row in range(row_count):
            if row == pivot_row:
                continue
            multiplier = rows[row][column]
            if multiplier:
                for position in range(column, column_count):
                    rows[row][position] = (
                        rows[row][position]
                        - multiplier * rows[pivot_row][position]
                    ) % prime
        pivots.append(column)
        pivot_row += 1
    free = [column for column in range(column_count) if column not in pivots]
    if len(free) != 1:
        raise AssertionError((prime, len(free), "nullity"))
    free_column = free[0]
    vector = [0] * column_count
    vector[free_column] = 1
    for row in range(len(pivots) - 1, -1, -1):
        column = pivots[row]
        vector[column] = -sum(
            rows[row][position] * vector[position]
            for position in range(column + 1, column_count)
        ) % prime
    return vector, free_column


def crt_pair(left: int, modulus: int, right: int, prime: int) -> int:
    multiplier = (right - left) % prime * pow(modulus % prime, prime - 2, prime)
    return (left + modulus * (multiplier % prime)) % (modulus * prime)


def rational_reconstruct(residue: int, modulus: int) -> tuple[int, int] | None:
    residue %= modulus
    bound = math.isqrt(modulus // 2)
    r0, s0 = modulus, 0
    r1, s1 = residue, 1
    while r1 >= bound:
        quotient = r0 // r1
        r0, r1 = r1, r0 - quotient * r1
        s0, s1 = s1, s0 - quotient * s1
    if not s1 or abs(s1) >= bound:
        return None
    numerator, denominator = (r1, s1) if s1 > 0 else (-r1, -s1)
    divisor = math.gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def reconstruct_operator(
    sequence: list[int], degree: int, fit_rows: int
) -> list[int]:
    residues: list[int] | None = None
    modulus = 1
    normalization_column: int | None = None
    for prime in RECONSTRUCTION_PRIMES:
        matrix = recurrence_matrix(sequence, ORDER, degree, fit_rows, prime)
        vector, free_column = null_vector(matrix, prime)
        if normalization_column is None:
            normalization_column = free_column
        if vector[normalization_column] == 0:
            raise AssertionError((prime, "normalization vanished"))
        inverse = pow(vector[normalization_column], prime - 2, prime)
        vector = [entry * inverse % prime for entry in vector]
        if residues is None:
            residues = vector
            modulus = prime
        else:
            residues = [
                crt_pair(left, modulus, right, prime)
                for left, right in zip(residues, vector)
            ]
            modulus *= prime
    if residues is None:
        raise AssertionError("no residues")
    rationals = [rational_reconstruct(entry, modulus) for entry in residues]
    if any(entry is None for entry in rationals):
        raise AssertionError("rational reconstruction failed")
    denominator_lcm = 1
    for entry in rationals:
        assert entry is not None
        denominator_lcm = math.lcm(denominator_lcm, entry[1])
    integers = [
        entry[0] * (denominator_lcm // entry[1])  # type: ignore[index]
        for entry in rationals
    ]
    common = math.gcd(*map(abs, integers))
    integers = [entry // common for entry in integers]
    first_nonzero = next(entry for entry in integers if entry)
    if first_nonzero < 0:
        integers = [-entry for entry in integers]
    return integers


def evaluate_operator(
    coefficients: list[int], degree: int, sequence: list[int], index: int
) -> int:
    return sum(
        coefficients[shift * (degree + 1) + power]
        * (index**power)
        * sequence[index + shift]
        for shift in range(ORDER + 1)
        for power in range(degree + 1)
    )


def operator_record(family: str, residue: int, degree: int) -> dict[str, Any]:
    unknowns = (ORDER + 1) * (degree + 1)
    fit_rows = unknowns + FIT_SLACK
    length = fit_rows + ORDER + HOLDOUT
    sequence = carrier_sequence(family, residue, length)
    coefficients = reconstruct_operator(sequence, degree, fit_rows)
    for index in range(fit_rows, fit_rows + HOLDOUT):
        if evaluate_operator(coefficients, degree, sequence, index):
            raise AssertionError((family, residue, index, "holdout"))

    candidate_matrix = recurrence_matrix(
        sequence, ORDER, degree, fit_rows, RANK_PRIME
    )
    candidate_rank = rref_rank(candidate_matrix, RANK_PRIME)
    if candidate_rank != unknowns - 1:
        raise AssertionError((family, residue, "candidate nullity"))

    lower_degree = degree - 1
    lower_degree_unknowns = (ORDER + 1) * (lower_degree + 1)
    lower_degree_rank = rref_rank(
        recurrence_matrix(
            sequence,
            ORDER,
            lower_degree,
            lower_degree_unknowns + 3,
            RANK_PRIME,
        ),
        RANK_PRIME,
    )
    if lower_degree_rank != lower_degree_unknowns:
        raise AssertionError((family, residue, "lower degree rank"))

    lower_order_witnesses = []
    for order in (1, 2):
        witness_degree = 30
        witness_unknowns = (order + 1) * (witness_degree + 1)
        rank = rref_rank(
            recurrence_matrix(
                sequence,
                order,
                witness_degree,
                witness_unknowns + 3,
                RANK_PRIME,
            ),
            RANK_PRIME,
        )
        if rank != witness_unknowns:
            raise AssertionError((family, residue, order, "lower order rank"))
        lower_order_witnesses.append(
            {"order": order, "degree_bound": witness_degree, "full_rank": rank}
        )

    coefficient_payload = json.dumps(coefficients, separators=(",", ":"))
    return {
        "family": family,
        "residue_h_mod_3": residue,
        "indexing": f"a_n=A_{family}(3n+{residue})",
        "candidate_order": ORDER,
        "candidate_degree": degree,
        "coefficient_layout": (
            "blocks P_0,...,P_3; within each block coefficients are in "
            "ascending powers of n"
        ),
        "coefficient_sha256": hashlib.sha256(
            coefficient_payload.encode("utf-8")
        ).hexdigest(),
        "coefficients": coefficients,
        "fit_rows": fit_rows,
        "exact_holdout_rows": HOLDOUT,
        "candidate_modular_nullity": unknowns - candidate_rank,
        "order_3_lower_degree_full_rank": lower_degree_rank,
        "lower_order_witnesses": lower_order_witnesses,
        "classification": (
            "EXACT FINITE OPERATOR CANDIDATE; NO ALL-n TELESCOPING CERTIFICATE"
        ),
    }


def operator_replay() -> dict[str, Any]:
    return {
        "classification": "EXACT FINITE ONLY; NO OPERATOR PROMOTION",
        "operators": [operator_record(*spec) for spec in SPECS],
        "search_box": (
            "full modular rank excludes orders 1 and 2 through degree 30, and "
            "order 3 below degree 19 for x or 23 for u, on the declared rows"
        ),
        "scope": (
            "the coefficient tables and holdouts are exact, but without a symbolic "
            "creative-telescoping certificate they are not all-n recurrence theorems"
        ),
    }


def alignment_replay() -> dict[str, Any]:
    rows = []
    for shift_index in range(1, 9):
        delta_h = 3 * shift_index
        numerator_delta_s = -9 * shift_index
        fixed_m_integral = numerator_delta_s % 4 == 0
        row = {
            "recurrence_shift_index": shift_index,
            "delta_h": delta_h,
            "delta_s": (
                numerator_delta_s // 4 if fixed_m_integral else f"{numerator_delta_s}/4"
            ),
            "same_fixed_M_integral_parameter_row": fixed_m_integral,
        }
        if fixed_m_integral:
            row["delta_p"] = -(3 * shift_index) // 2
        rows.append(row)
    if any(row["same_fixed_M_integral_parameter_row"] for row in rows[:3]):
        raise AssertionError("order-three window unexpectedly meets fixed-M row")
    if rows[3]["delta_h"] != 12 or rows[3]["delta_p"] != -6:
        raise AssertionError("first fixed-M return")
    return {
        "classification": "PROVED SYMBOLIC ALIGNMENT BARRIER",
        "rows": rows,
        "identity": (
            "under h->h+3j at fixed M, s->s-9j/4; this is an integral parameter "
            "row iff 4|j, and is actual iff also s-9j/4>=1; then p->p-3j/2"
        ),
        "order_three_consequence": (
            "a single order-three h-mod-3 recurrence window contains no second "
            "actual fixed-M row"
        ),
        "first_return": (
            "iteration first reaches another integral parameter row at h->h+12; it "
            "is actual when s>=10, and its selected prime is p-6. Reduction of the "
            "recurrence modulo p gives no congruence modulo p-6"
        ),
        "scope": (
            "same-ray rational recurrences alone cannot transfer selected divisibility; "
            "a genuinely cross-prime reciprocity or common carrier is required"
        ),
    }


def capacity_replay() -> dict[str, Any]:
    return {
        "unreduced_individual_height": "O(h log(h+2))",
        "primitive_individual_height_from_item379": "O(h)",
        "direct_aggregate_unreduced": "O(M^2 log M)",
        "direct_aggregate_primitive": "O(M^2)",
        "required_exceptional_mass": "o(M)",
        "shared_full_fixed_j1_ceiling_per_6M": "1/36",
        "new_booking": 0,
        "new_capacity_reduction": 0,
    }


def build_result() -> dict[str, Any]:
    return {
        "item": 382,
        "schema": "item382-j1-explicit-operator-alignment-barrier-v1",
        "classification": "FINITE_EXPLICIT_OPERATORS_AND_PROVED_MOVING_MODULUS_ALIGNMENT_BARRIER",
        "dependencies": DEPENDENCIES,
        "dependency_hashes_verified": True,
        "operator_replay": operator_replay(),
        "alignment_replay": alignment_replay(),
        "capacity_replay": capacity_replay(),
        "strict_labels": {
            "proved": [
                "fixed-M alignment identity for every same-ray recurrence shift",
                "an order-three same-ray window contains no second actual row",
                "the first possible integral same-ray fixed-M return changes p to p-6 and is actual when s>=10",
                "same-ray recurrence identities alone provide no cross-prime transfer",
                "zero booking and zero capacity reduction",
            ],
            "finite_only": [
                "four exact order-three operator coefficient tables",
                "exact fitting and holdout identities",
                "modular rank minimality only inside the declared finite search box",
                "no all-n operator promotion, prime scan, or extrapolation",
            ],
            "open": [
                "symbolic creative-telescoping certificates for the four candidates",
                "true all-n minimality of the recurrence operators",
                "a cross-prime reciprocity between p and p-6 or a common fixed-M carrier",
                "selector-aware weighted zero density and any capacity reduction",
            ],
        },
        "smallest_missing_arithmetic_lemma": (
            "a target-retaining cross-prime identity comparing the h and h+12 carrier "
            "states, where the returned row exists, at their different selected primes p and p-6"
        ),
        "verdict": (
            "The explicit finite operators are order three on each h mod 3 ray, but "
            "their window does not contain two actual fixed-M rows.  The first possible "
            "integral return is actual only away from the positivity boundary and has a "
            "different modulus, so no moving-modulus bridge or capacity gain follows "
            "from recurrence data alone."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "classification": result["classification"],
                "new_booking": result["capacity_replay"]["new_booking"],
                "new_capacity_reduction": result["capacity_replay"][
                    "new_capacity_reduction"
                ],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
