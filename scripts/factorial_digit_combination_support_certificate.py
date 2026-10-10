#!/usr/bin/env python3
"""Exact certificate for two factorial-digit support barriers.

The companion source note proves two universal statements.

1.  If V_n=(C_n,n!) and C_n=n*C_{n-1}+c_n, then the lattice generated
    by V_a,...,V_{a+B} (equivalently by their forward differences at a)
    is <V_a,(g,0)>, where g=gcd(c_{a+1},...,c_{a+B}).  Its Smith
    invariants are r=gcd(C_a,a!,g) and g*a!/r.  Its projective saturation
    is therefore every primitive pair in Z^2.

2.  If q_n is the reduced denominator of C_n/n!, then for n<m,

        m! | K_{n,m} q_n q_m,

    where K_{n,m}=C_m-(m!/n!)*C_n is positive and is less than
    (m!/n!)*(1+1/n).

This program independently constructs the canonical factorial digits of
pi, verifies the lattice/Hermite/Smith statements on finite blocks, checks
the explicit two-form universal-combination identity, and verifies the
gap divisibility and outside-support inequality on a finite triangle.
Finite checks are diagnostics; the source proofs are all-degree.
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
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form


sys.set_int_max_str_digits(0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vector_sha256(values: list[int]) -> str:
    payload = json.dumps(values, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def matrix_payload(matrix: sp.Matrix) -> str:
    return f"{matrix.rows}x{matrix.cols}:" + ",".join(
        str(int(value)) for value in matrix
    )


def matrix_sha256(matrix: sp.Matrix) -> str:
    return hashlib.sha256(matrix_payload(matrix).encode()).hexdigest()


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
    half = atan_inverse_interval(2, 420)
    third = atan_inverse_interval(3, 300)
    return (
        4 * (half[0] + third[0]),
        4 * (half[1] + third[1]),
    )


def canonical_data(
    maximum: int, pi_box: tuple[Fraction, Fraction]
) -> tuple[list[int], list[int], list[int], list[int]]:
    factorials = [math.factorial(index) for index in range(maximum + 1)]
    pi_floors: list[int] = []
    for index, factorial in enumerate(factorials):
        lower = factorial * pi_box[0]
        upper = factorial * pi_box[1]
        floor_lower = lower.numerator // lower.denominator
        floor_upper = upper.numerator // upper.denominator
        if floor_lower != floor_upper:
            raise AssertionError(f"uncertified floor({index}! pi)")
        pi_floors.append(floor_lower)

    digits = [0, 0]
    for index in range(2, maximum + 1):
        digit = pi_floors[index] - index * pi_floors[index - 1]
        if not 0 <= digit <= index - 1:
            raise AssertionError("canonical digit outside its exact range")
        digits.append(digit)

    c_digits = [4, 1] + [digits[index] + 1 for index in range(2, maximum + 1)]
    combined = [4]
    for index in range(1, maximum + 1):
        combined.append(index * combined[index - 1] + c_digits[index])

    for index in range(1, maximum + 1):
        e_floor = sum(
            factorials[index] // factorials[k] for k in range(index + 1)
        )
        if combined[index] != e_floor + pi_floors[index]:
            raise AssertionError("combined numerator identity failed")
    return factorials, digits, c_digits, combined


def forward_difference_columns(
    vectors: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    first: list[tuple[int, int]] = []
    row = vectors[:]
    while row:
        first.append(row[0])
        row = [
            (row[index + 1][0] - row[index][0],
             row[index + 1][1] - row[index][1])
            for index in range(len(row) - 1)
        ]
    return first


def column_matrix(vectors: list[tuple[int, int]]) -> sp.Matrix:
    return sp.Matrix(
        [
            [vector[0] for vector in vectors],
            [vector[1] for vector in vectors],
        ]
    )


def outside_part(value: int, primes: tuple[int, ...]) -> int:
    result = abs(value)
    for prime in primes:
        while result % prime == 0:
            result //= prime
    return result


def compact_integer(value: int) -> dict[str, object]:
    rendered = str(value)
    return {
        "decimal_digits": len(rendered.lstrip("-")),
        "sha256": hashlib.sha256(rendered.encode()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-index", type=int, default=100)
    parser.add_argument("--maximum-block-width", type=int, default=12)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "sources/factorial_digit_integer_combination_support_barrier.md"
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/factorial_digit_combination_support_certificate.json"
        ),
    )
    args = parser.parse_args()
    if args.maximum_index < 20:
        raise ValueError("maximum-index must be at least 20")
    if not 1 <= args.maximum_block_width < args.maximum_index:
        raise ValueError("invalid maximum-block-width")

    pi_box = pi_interval()
    factorials, digits, c_digits, combined = canonical_data(
        args.maximum_index, pi_box
    )

    block_count = 0
    block_stream = hashlib.sha256()
    selected_blocks: list[dict[str, object]] = []
    selected_block_keys = {
        (1, 1),
        (3, 1),
        (5, 1),
        (5, 4),
        (12, 8),
        (35, 1),
        (37, 12),
        (80, 12),
    }

    for a in range(1, args.maximum_index):
        maximum_width = min(
            args.maximum_block_width, args.maximum_index - a
        )
        vectors = [
            (combined[index], factorials[index])
            for index in range(a, a + maximum_width + 1)
        ]
        differences = forward_difference_columns(vectors)
        for width in range(1, maximum_width + 1):
            g_value = 0
            for digit in c_digits[a + 1 : a + width + 1]:
                g_value = math.gcd(g_value, digit)
            predicted = sp.Matrix(
                [[combined[a], g_value], [factorials[a], 0]]
            )
            value_matrix = column_matrix(vectors[: width + 1])
            difference_matrix = column_matrix(differences[: width + 1])
            hnf_predicted = hermite_normal_form(predicted)
            if hermite_normal_form(value_matrix) != hnf_predicted:
                raise AssertionError("value-block lattice mismatch")
            if hermite_normal_form(difference_matrix) != hnf_predicted:
                raise AssertionError("difference-block lattice mismatch")

            r_value = math.gcd(combined[a], factorials[a], g_value)
            conductor = g_value * factorials[a] // r_value
            smith = smith_normal_form(predicted, domain=sp.ZZ)
            smith_diagonal = sorted(
                abs(int(smith[index, index])) for index in range(2)
            )
            if smith_diagonal != [r_value, conductor]:
                raise AssertionError("Smith invariant formula mismatch")

            payload = (
                f"{a},{width},{g_value},{r_value},{conductor},"
                f"{matrix_sha256(hnf_predicted)};"
            )
            block_stream.update(payload.encode())
            block_count += 1
            if (a, width) in selected_block_keys:
                selected_blocks.append(
                    {
                        "a": a,
                        "width": width,
                        "gcd_future_digits": g_value,
                        "first_Smith_invariant": r_value,
                        "lattice_conductor": compact_integer(conductor),
                        "Hermite_normal_form": [
                            [str(int(hnf_predicted[row, column]))
                             for column in range(hnf_predicted.cols)]
                            for row in range(hnf_predicted.rows)
                        ],
                    }
                )

    primitive_pairs = [(1, 1), (5, 7), (-3, 11), (97, 64), (1234, 4321)]
    combination_checks = 0
    combination_stream = hashlib.sha256()
    for a in range(1, args.maximum_index):
        c_value = c_digits[a + 1]
        f0 = (combined[a], factorials[a])
        f1 = (
            combined[a + 1] - combined[a],
            factorials[a + 1] - factorials[a],
        )
        for p_value, q_value in primitive_pairs:
            if math.gcd(abs(p_value), q_value) != 1:
                raise AssertionError("test pair is not primitive")
            t_value = factorials[a] * p_value - q_value * combined[a]
            coefficient_0 = c_value * q_value - a * t_value
            coefficient_1 = t_value
            obtained = (
                coefficient_0 * f0[0] + coefficient_1 * f1[0],
                coefficient_0 * f0[1] + coefficient_1 * f1[1],
            )
            expected = (
                c_value * factorials[a] * p_value,
                c_value * factorials[a] * q_value,
            )
            if obtained != expected:
                raise AssertionError("explicit universal combination failed")
            if math.gcd(abs(obtained[0]), abs(obtained[1])) != (
                c_value * factorials[a]
            ):
                raise AssertionError("endpoint content is not the exact scale")
            combination_stream.update(
                (
                    f"{a},{p_value},{q_value},{coefficient_0},"
                    f"{coefficient_1};"
                ).encode()
            )
            combination_checks += 1

    support_sets = {
        "empty": (),
        "2_3": (2, 3),
        "2_3_5_7": (2, 3, 5, 7),
    }
    q_values = [0] * (args.maximum_index + 1)
    for index in range(1, args.maximum_index + 1):
        q_values[index] = factorials[index] // math.gcd(
            factorials[index], combined[index]
        )

    gap_count = 0
    gap_stream = hashlib.sha256()
    support_checks = {name: 0 for name in support_sets}
    selected_gaps: list[dict[str, object]] = []
    selected_gap_keys = {(1, 2), (5, 11), (20, 40), (50, 100)}
    minimum_outside_ratio: dict[str, tuple[Fraction, int, int] | None] = {
        name: None for name in support_sets
    }

    for n in range(1, args.maximum_index):
        for m in range(n + 1, args.maximum_index + 1):
            ratio = factorials[m] // factorials[n]
            k_value = combined[m] - ratio * combined[n]
            if k_value <= 0:
                raise AssertionError("K is not positive")
            if not n * k_value < (n + 1) * ratio:
                raise AssertionError("strict K upper bound failed")
            product = k_value * q_values[n] * q_values[m]
            if product % factorials[m]:
                raise AssertionError("m! does not divide K q_n q_m")
            primitive_determinant = product // factorials[m]
            if primitive_determinant <= 0:
                raise AssertionError("primitive determinant is not positive")

            support_record: dict[str, object] = {}
            for name, primes in support_sets.items():
                n_out = outside_part(q_values[n], primes)
                m_out = outside_part(q_values[m], primes)
                factorial_out = outside_part(factorials[m], primes)
                k_out = outside_part(k_value, primes)
                if (k_out * n_out * m_out) % factorial_out:
                    raise AssertionError("outside-support divisibility failed")
                left = n_out * m_out
                right = Fraction(factorial_out, k_out)
                if left < right:
                    raise AssertionError("outside-support lower bound failed")
                lower_from_size = Fraction(
                    factorials[n],
                    1,
                ) * Fraction(n, n + 1) / (
                    factorials[m] // factorial_out
                )
                if not Fraction(left, 1) > lower_from_size:
                    raise AssertionError("strict support-dispersion bound failed")
                ratio_to_lower = Fraction(left, 1) / lower_from_size
                current = minimum_outside_ratio[name]
                if current is None or ratio_to_lower < current[0]:
                    minimum_outside_ratio[name] = (ratio_to_lower, n, m)
                support_checks[name] += 1
                if (n, m) in selected_gap_keys:
                    support_record[name] = {
                        "q_n_outside": compact_integer(n_out),
                        "q_m_outside": compact_integer(m_out),
                        "factorial_outside_over_K_outside": {
                            "numerator": compact_integer(right.numerator),
                            "denominator": compact_integer(right.denominator),
                        },
                    }

            gap_stream.update(
                (
                    f"{n},{m},{k_value},{q_values[n]},{q_values[m]},"
                    f"{primitive_determinant};"
                ).encode()
            )
            gap_count += 1
            if (n, m) in selected_gap_keys:
                selected_gaps.append(
                    {
                        "n": n,
                        "m": m,
                        "K_n_m": compact_integer(k_value),
                        "q_n": compact_integer(q_values[n]),
                        "q_m": compact_integer(q_values[m]),
                        "primitive_cross_determinant": compact_integer(
                            primitive_determinant
                        ),
                        "support_records": support_record,
                    }
                )

    rendered_minima: dict[str, object] = {}
    for name, item in minimum_outside_ratio.items():
        if item is None:
            raise AssertionError("missing support minimum")
        ratio_value, n, m = item
        rendered_minima[name] = {
            "n": n,
            "m": m,
            "ratio_numerator": str(ratio_value.numerator),
            "ratio_denominator": str(ratio_value.denominator),
        }

    source_path = args.source.resolve()
    script_path = Path(__file__).resolve()
    result = {
        "description": (
            "Exact finite certificate for the factorial-digit integer-"
            "combination lattice saturation and denominator-support gap"
        ),
        "status": (
            "finite checks of all-degree symbolic theorems; no conclusion "
            "about the arithmetic nature of e+pi"
        ),
        "parameters": {
            "maximum_index": args.maximum_index,
            "maximum_block_width": args.maximum_block_width,
            "block_count": block_count,
            "universal_combination_checks": combination_checks,
            "gap_pair_count": gap_count,
        },
        "artifact_hashes": {
            "source_sha256": sha256(source_path),
            "script_sha256": sha256(script_path),
        },
        "canonical_data": {
            "pi_identity": "pi=4*(atan(1/2)+atan(1/3))",
            "atan_last_indices": {"inverse_2": 420, "inverse_3": 300},
            "digit_vector_sha256": vector_sha256(digits),
            "combined_digit_vector_sha256": vector_sha256(c_digits),
            "combined_numerator_vector_sha256": vector_sha256(combined),
        },
        "lattice_checks": {
            "all_value_and_difference_HNFs_match_predicted_lattice": True,
            "all_Smith_invariants_match": True,
            "block_stream_sha256": block_stream.hexdigest(),
            "selected_blocks": selected_blocks,
        },
        "universal_combination_checks": {
            "all_explicit_identities_and_exact_contents_match": True,
            "primitive_test_pairs": [list(pair) for pair in primitive_pairs],
            "combination_stream_sha256": combination_stream.hexdigest(),
        },
        "gap_checks": {
            "all_K_positivity_and_strict_upper_bounds_match": True,
            "all_m_factorial_divisibilities_match": True,
            "all_outside_support_bounds_match": True,
            "support_check_counts": support_checks,
            "gap_stream_sha256": gap_stream.hexdigest(),
            "minimum_ratio_to_strict_size_lower_bound": rendered_minima,
            "selected_gaps": selected_gaps,
        },
        "warning": (
            "The checks are finite diagnostics.  The source note proves the "
            "identities in all degrees.  The surviving possibility is an "
            "infinite lacunary sequence with exceptional support/content."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result["parameters"], indent=2, sort_keys=True))
    print(json.dumps(result["lattice_checks"], indent=2, sort_keys=True))
    print(json.dumps(result["gap_checks"]["support_check_counts"], indent=2, sort_keys=True))
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
