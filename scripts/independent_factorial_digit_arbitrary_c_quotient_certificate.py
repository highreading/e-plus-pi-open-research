#!/usr/bin/env python3
"""Exact certificate for the arbitrary-c Poisson quotient determinant.

For c>0, the full high block H=[U,V] has b polynomial e-columns and c
factorial-digit G-columns.  This script independently checks

    det(H) = (-1)^b * kappa_b * det(Q),

where Q is the c-by-c integral Poisson/Newton quotient matrix.  It also
checks the stronger rank reductions for H and for the augmented high matrix
[H y], and compares them with the complete bordered HP matrix.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


sys.set_int_max_str_digits(0)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def vector_sha256(values: list[int]) -> str:
    return sha256_text(json.dumps(values, separators=(",", ":")))


def matrix_sha256(matrix: sp.Matrix) -> str:
    payload = f"{matrix.rows}x{matrix.cols}:" + ",".join(
        str(int(value)) for value in matrix
    )
    return sha256_text(payload)


def atan_inverse_interval(
    inverse: int, last_index: int
) -> tuple[Fraction, Fraction]:
    term = Fraction(1, inverse)
    partial = term
    for index in range(last_index):
        term *= Fraction(
            -(2 * index + 1),
            (2 * index + 3) * inverse * inverse,
        )
        partial += term
    first_omitted = abs(term) * Fraction(
        2 * last_index + 1,
        (2 * last_index + 3) * inverse * inverse,
    )
    if last_index & 1:
        return partial, partial + first_omitted
    return partial - first_omitted, partial


def pi_interval() -> tuple[Fraction, Fraction]:
    half = atan_inverse_interval(2, 100)
    third = atan_inverse_interval(3, 70)
    return (
        4 * (half[0] + third[0]),
        4 * (half[1] + third[1]),
    )


def canonical_g_jets(
    maximum_index: int, pi_box: tuple[Fraction, Fraction]
) -> list[int]:
    factorial = 1
    floors: list[int] = []
    for index in range(maximum_index + 1):
        if index:
            factorial *= index
        lower = factorial * pi_box[0]
        upper = factorial * pi_box[1]
        floor_lower = lower.numerator // lower.denominator
        floor_upper = upper.numerator // upper.denominator
        if floor_lower != floor_upper:
            raise AssertionError(f"uncertified floor({index}! pi)")
        floors.append(floor_lower)
    jets = [3, 0]
    for index in range(2, maximum_index + 1):
        digit = floors[index] - index * floors[index - 1]
        if not 0 <= digit <= index - 1:
            raise AssertionError("invalid canonical factorial digit")
        jets.append(digit)
    return jets


def falling(value: int, order: int) -> int:
    if order > value:
        return 0
    return math.factorial(value) // math.factorial(value - order)


def d_sequence(a: int, maximum_order: int) -> list[int]:
    values = [1]
    if maximum_order:
        values.append(a)
    for order in range(2, maximum_order + 1):
        values.append(
            (a + order - 1) * values[order - 1]
            + (order - 1) * values[order - 2]
        )
    return values


def forward_differences(values: list[int]) -> list[int]:
    first_values: list[int] = []
    row = values[:]
    while row:
        first_values.append(row[0])
        row = [row[index + 1] - row[index] for index in range(len(row) - 1)]
    return first_values


def u_value(k: int, j: int) -> int:
    return falling(k, j) * (k - j - 1)


def v_value(k: int, j: int, g_jets: list[int]) -> int:
    if j > k:
        return 0
    n = k - j
    previous = 0 if n == 0 else g_jets[n - 1]
    return falling(k, j) * (n * previous - g_jets[n])


def high_matrix(a: int, b: int, c: int, g_jets: list[int]) -> sp.Matrix:
    rows: list[list[int]] = []
    for k in range(a + 1, a + b + c + 1):
        rows.append(
            [u_value(k, j) for j in range(b)]
            + [v_value(k, j, g_jets) for j in range(c)]
        )
    return sp.Matrix(rows)


def quotient_column(
    a: int,
    b: int,
    c: int,
    samples: list[int],
) -> list[int]:
    if len(samples) != b + c:
        raise AssertionError("quotient sample length mismatch")
    differences = forward_differences(samples)
    d_values = d_sequence(a, b)
    first = sum(
        (-1) ** order
        * (math.factorial(b) // math.factorial(order))
        * d_values[order]
        * differences[order]
        for order in range(b + 1)
    )
    return [first] + [
        differences[b + row] for row in range(1, c)
    ]


def quotient_matrix(
    a: int, b: int, c: int, g_jets: list[int]
) -> sp.Matrix:
    node_count = b + c
    columns = []
    for j in range(c):
        samples = [
            v_value(k, j, g_jets)
            for k in range(a + 1, a + node_count + 1)
        ]
        columns.append(sp.Matrix(quotient_column(a, b, c, samples)))
    return sp.Matrix.hstack(*columns)


def combined_high_column(
    a: int, b: int, c: int, g_jets: list[int]
) -> sp.Matrix:
    return sp.Matrix(
        [
            1 + g_jets[k]
            for k in range(a + 1, a + b + c + 1)
        ]
    )


def quotient_combined_column(
    a: int, b: int, c: int, g_jets: list[int]
) -> sp.Matrix:
    samples = [
        1 + g_jets[k]
        for k in range(a + 1, a + b + c + 1)
    ]
    return sp.Matrix(quotient_column(a, b, c, samples))


def kappa_b(b: int) -> int:
    return math.prod(math.factorial(j) for j in range(b))


def full_bordered_matrix(
    a: int, b: int, c: int, g_jets: list[int]
) -> sp.Matrix:
    order = a + b + c + 1
    column_count = a + b + c + 3
    rows: list[list[int]] = []
    for k in range(order):
        row = [0] * column_count
        if k <= a:
            row[k] = math.factorial(k)
        b_offset = a + 1
        for j in range(min(b, k) + 1):
            row[b_offset + j] = falling(k, j)
        c_offset = b_offset + b + 1
        for j in range(min(c, k) + 1):
            row[c_offset + j] = falling(k, j) * g_jets[k - j]
        rows.append(row)
    endpoint = [0] * column_count
    b_offset = a + 1
    for j in range(b + 1):
        endpoint[b_offset + j] = 1
    c_offset = b_offset + b + 1
    for j in range(c + 1):
        endpoint[c_offset + j] = -1
    rows.append(endpoint)
    return sp.Matrix(rows)


def primitive_kernel(matrix: sp.Matrix) -> list[int]:
    nullspace = matrix.nullspace()
    if len(nullspace) != 1:
        return []
    vector = nullspace[0]
    denominator = 1
    for entry in vector:
        denominator = math.lcm(
            denominator, int(entry.as_numer_denom()[1])
        )
    values = [int(entry * denominator) for entry in vector]
    content = 0
    for value in values:
        content = math.gcd(content, abs(value))
    values = [value // content for value in values]
    for value in values:
        if value:
            if value < 0:
                values = [-entry for entry in values]
            break
    return values


def direct_record(
    a: int, b: int, c: int, g_jets: list[int]
) -> dict[str, object]:
    high = high_matrix(a, b, c, g_jets)
    quotient = quotient_matrix(a, b, c, g_jets)
    y = combined_high_column(a, b, c, g_jets)
    quotient_y = quotient_combined_column(a, b, c, g_jets)
    augmented_high = high.row_join(y)
    augmented_quotient = quotient.row_join(quotient_y)
    determinant_high = int(high.det())
    determinant_quotient = int(quotient.det())
    predicted = (-1) ** b * kappa_b(b) * determinant_quotient
    if determinant_high != predicted:
        raise AssertionError("arbitrary-c determinant formula mismatch")

    rank_high = high.rank()
    rank_quotient = quotient.rank()
    rank_augmented_high = augmented_high.rank()
    rank_augmented_quotient = augmented_quotient.rank()
    if rank_high != b + rank_quotient:
        raise AssertionError("high rank quotient formula mismatch")
    if rank_augmented_high != b + rank_augmented_quotient:
        raise AssertionError("augmented rank quotient formula mismatch")

    full = full_bordered_matrix(a, b, c, g_jets)
    rank_full = full.rank()
    nullity_full = full.cols - rank_full
    predicted_nullity = c + 1 - rank_augmented_quotient
    if nullity_full != predicted_nullity:
        raise AssertionError("full bordered nullity quotient formula mismatch")

    kernel = primitive_kernel(full)
    if nullity_full == 1:
        if not kernel:
            raise AssertionError("missing primitive kernel")
        b_offset = a + 1
        c_offset = b_offset + b + 1
        alpha = sum(kernel[:b_offset])
        beta = sum(kernel[b_offset:c_offset])
        gamma = sum(kernel[c_offset:])
        if beta != gamma:
            raise AssertionError("endpoint equality failed")
    else:
        alpha = None
        beta = None

    return {
        "a": a,
        "b": b,
        "c": c,
        "determinant_high": determinant_high,
        "determinant_quotient": determinant_quotient,
        "rank_high": rank_high,
        "rank_quotient": rank_quotient,
        "rank_augmented_high": rank_augmented_high,
        "rank_augmented_quotient": rank_augmented_quotient,
        "rank_full": rank_full,
        "nullity_full": nullity_full,
        "endpoint_alpha": alpha,
        "endpoint_beta": beta,
        "high_matrix": high,
        "quotient_matrix": quotient,
        "quotient_y": quotient_y,
    }


def synthetic_jets(maximum_index: int) -> list[int]:
    # A deterministic integral sequence unrelated to the canonical digits.
    return [
        ((index**4 + 7 * index**2 + 11 * index + 5) % 97) - 48
        for index in range(maximum_index + 1)
    ]


def selected_json(record: dict[str, object]) -> dict[str, object]:
    high = record["high_matrix"]
    quotient = record["quotient_matrix"]
    quotient_y = record["quotient_y"]
    return {
        "a": record["a"],
        "b": record["b"],
        "c": record["c"],
        "determinant_high": str(record["determinant_high"]),
        "determinant_quotient": str(record["determinant_quotient"]),
        "rank_high": record["rank_high"],
        "rank_quotient": record["rank_quotient"],
        "rank_augmented_high": record["rank_augmented_high"],
        "rank_augmented_quotient": record["rank_augmented_quotient"],
        "rank_full": record["rank_full"],
        "nullity_full": record["nullity_full"],
        "endpoint_alpha": (
            str(record["endpoint_alpha"])
            if record["endpoint_alpha"] is not None
            else None
        ),
        "endpoint_beta": (
            str(record["endpoint_beta"])
            if record["endpoint_beta"] is not None
            else None
        ),
        "high_matrix_sha256": matrix_sha256(high),
        "quotient_matrix": [
            [str(int(quotient[row, column])) for column in range(quotient.cols)]
            for row in range(quotient.rows)
        ],
        "quotient_y": [str(int(value)) for value in quotient_y],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-total", type=int, default=18)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/independent_factorial_digit_arbitrary_c_quotient_T18.json"
        ),
    )
    args = parser.parse_args()
    if args.max_total < 4:
        raise ValueError("max-total must be at least 4")

    pi_box = pi_interval()
    g_jets = canonical_g_jets(args.max_total, pi_box)
    combined_jets = [1 + value for value in g_jets]

    record_stream = hashlib.sha256()
    total_records = 0
    c1_records = 0
    determinant_nonzero = 0
    determinant_zero = 0
    all_full_row_rank = True
    singular_records: list[dict[str, object]] = []
    selected_triples = {
        (0, 0, 1),
        (1, 0, 1),
        (1, 0, 2),
        (1, 1, 1),
        (2, 0, 2),
        (4, 2, 3),
        (5, 4, 2),
        (8, 3, 1),
        (0, 0, args.max_total),
    }
    selected_records: list[dict[str, object]] = []

    for total in range(1, args.max_total + 1):
        for a in range(total + 1):
            for b in range(total - a + 1):
                c = total - a - b
                if c <= 0:
                    continue
                record = direct_record(a, b, c, g_jets)
                total_records += 1
                if c == 1:
                    c1_records += 1
                    samples = [
                        v_value(k, 0, g_jets)
                        for k in range(a + 1, a + b + 2)
                    ]
                    differences = forward_differences(samples)
                    d_values = d_sequence(a, b)
                    recurrence_value = samples[0]
                    for order in range(1, b + 1):
                        recurrence_value = (
                            order * recurrence_value
                            + (-1) ** order
                            * d_values[order]
                            * differences[order]
                        )
                    if recurrence_value != record["determinant_quotient"]:
                        raise AssertionError("c=1 recurrence was not recovered")

                if record["determinant_high"]:
                    determinant_nonzero += 1
                else:
                    determinant_zero += 1
                    singular_records.append(selected_json(record))
                if record["rank_full"] != (
                    a + b + c + 2
                ):
                    all_full_row_rank = False

                payload = [
                    a,
                    b,
                    c,
                    str(record["determinant_high"]),
                    str(record["determinant_quotient"]),
                    record["rank_high"],
                    record["rank_quotient"],
                    record["rank_augmented_high"],
                    record["rank_augmented_quotient"],
                    record["rank_full"],
                    record["nullity_full"],
                    (
                        str(record["endpoint_alpha"])
                        if record["endpoint_alpha"] is not None
                        else None
                    ),
                    (
                        str(record["endpoint_beta"])
                        if record["endpoint_beta"] is not None
                        else None
                    ),
                ]
                record_stream.update(
                    (json.dumps(payload, separators=(",", ":")) + "\n").encode()
                )
                if (a, b, c) in selected_triples:
                    selected_records.append(selected_json(record))

    expected = math.comb(args.max_total + 3, 3) - math.comb(
        args.max_total + 2, 2
    )
    if total_records != expected:
        raise AssertionError("positive-c triple count mismatch")

    # Universal synthetic-sequence checks show that the identity is not a
    # special numerical property of pi's digits.
    synthetic = synthetic_jets(12)
    synthetic_checks = 0
    for total in range(1, 11):
        for a in range(total + 1):
            for b in range(total - a + 1):
                c = total - a - b
                if c <= 0:
                    continue
                high = high_matrix(a, b, c, synthetic)
                quotient = quotient_matrix(a, b, c, synthetic)
                if int(high.det()) != (
                    (-1) ** b * kappa_b(b) * int(quotient.det())
                ):
                    raise AssertionError("synthetic determinant check failed")
                if high.rank() != b + quotient.rank():
                    raise AssertionError("synthetic rank check failed")
                synthetic_checks += 1

    result = {
        "description": (
            "Independent exact arbitrary-c Poisson/Newton quotient "
            "determinant and rank certificate"
        ),
        "status": (
            "all-degree algebraic identity; T<=18 canonical-digit and "
            "T<=10 synthetic checks are finite"
        ),
        "parameters": {
            "max_total": args.max_total,
            "positive_c_triple_count": total_records,
            "c1_record_count": c1_records,
            "synthetic_sequence_check_count": synthetic_checks,
        },
        "canonical_jet_certificate": {
            "G_jets_0_through_T": g_jets,
            "combined_jets_0_through_T": combined_jets,
            "G_jet_vector_sha256": vector_sha256(g_jets),
            "combined_jet_vector_sha256": vector_sha256(combined_jets),
            "pi_identity": "pi=4*(atan(1/2)+atan(1/3))",
            "atan_last_indices": {"inverse_2": 100, "inverse_3": 70},
            "pi_lower": f"{pi_box[0].numerator}/{pi_box[0].denominator}",
            "pi_upper": f"{pi_box[1].numerator}/{pi_box[1].denominator}",
            "pi_interval_width": (
                f"{(pi_box[1] - pi_box[0]).numerator}/"
                f"{(pi_box[1] - pi_box[0]).denominator}"
            ),
        },
        "identity_checks": {
            "all_direct_determinants_match_quotient_formula": True,
            "all_high_ranks_match_b_plus_quotient_rank": True,
            "all_augmented_ranks_match_b_plus_augmented_quotient_rank": True,
            "all_full_nullities_match_c_plus_1_minus_augmented_quotient_rank": True,
            "all_c1_records_recover_normalized_recurrence": True,
            "all_synthetic_integral_sequence_checks_pass": True,
        },
        "finite_canonical_scan": {
            "record_stream_sha256": record_stream.hexdigest(),
            "high_determinant_nonzero_count": determinant_nonzero,
            "high_determinant_zero_count": determinant_zero,
            "all_full_bordered_matrices_have_full_row_rank": all_full_row_rank,
            "singular_high_records": singular_records,
        },
        "selected_exact_records": sorted(
            selected_records,
            key=lambda record: (record["a"], record["b"], record["c"]),
        ),
        "warning": (
            "The quotient identity and rank equivalences are all-degree.  "
            "The observed determinant zeros and full ranks through total "
            "degree 18 are finite facts only."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result["parameters"], indent=2, sort_keys=True))
    print(json.dumps(result["identity_checks"], indent=2, sort_keys=True))
    print(
        json.dumps(
            {
                "high_determinant_nonzero_count": determinant_nonzero,
                "high_determinant_zero_count": determinant_zero,
                "all_full_bordered_matrices_have_full_row_rank": (
                    all_full_row_rank
                ),
                "singular_triples": [
                    [record["a"], record["b"], record["c"]]
                    for record in singular_records
                ],
                "record_stream_sha256": record_stream.hexdigest(),
            },
            indent=2,
            sort_keys=True,
        )
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
