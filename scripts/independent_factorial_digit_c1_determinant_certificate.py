#!/usr/bin/env python3
"""Exact c=1 determinant theorem and finite canonical-digit diagnostic.

For the full polynomial-C endpoint-matched Hermite-Pade family, this script
audits the first new ray deg(C)<=1.  It checks three independent formulas:

  * the normalized determinant recurrence in b;
  * the alternating v-cofactor expansion;
  * the alternating factorial-digit expansion.

It then scans all a+b<=530 with a>=max(1,b-1), using a rational enclosure
from pi=4*(atan(1/2)+atan(1/3)).  Every rank/determinant/content statement
and every minimum comparison is exact.  Decimal strings are diagnostics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp


sys.set_int_max_str_digits(0)


EXPECTED_DIGIT_HASH_THROUGH_530 = (
    "9823adbf8b8ee2e45695284428ae465af2247354bf889979e8ddceb6139326b4"
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def vector_sha256(values: list[int]) -> str:
    return sha256_text(json.dumps(values, separators=(",", ":")))


def fraction_sha256(value: Fraction) -> str:
    return sha256_text(f"{value.numerator}/{value.denominator}")


def decimal_fraction(value: Fraction, digits: int = 40) -> str:
    mp.mp.dps = digits + 20
    return mp.nstr(mp.mpf(value.numerator) / value.denominator, digits)


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
    half = atan_inverse_interval(2, 2100)
    third = atan_inverse_interval(3, 1400)
    return (
        4 * (half[0] + third[0]),
        4 * (half[1] + third[1]),
    )


def canonical_digits(
    maximum_index: int, pi_box: tuple[Fraction, Fraction]
) -> tuple[list[int], list[int]]:
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
    digits = [0, 0]
    for index in range(2, maximum_index + 1):
        digit = floors[index] - index * floors[index - 1]
        if not 0 <= digit <= index - 1:
            raise AssertionError("factorial digit outside its exact bounds")
        digits.append(digit)
    return floors, digits


def d_sequence(a: int, maximum_b: int) -> list[int]:
    values = [1]
    if maximum_b:
        values.append(a)
    for b in range(2, maximum_b + 1):
        values.append(
            (a + b - 1) * values[b - 1] + (b - 1) * values[b - 2]
        )
    return values


def cofactor_update(
    a: int,
    b: int,
    d_values: list[int],
    previous: list[int],
) -> list[int]:
    if b == 0:
        return [1]
    return [
        *(
            b * previous[r] + math.comb(b, r) * d_values[b]
            for r in range(b)
        ),
        d_values[b],
    ]


def digit_coefficient_magnitudes(
    a: int, b: int, cofactors: list[int]
) -> list[int]:
    return [
        (a + 1) * cofactors[0],
        *(
            cofactors[s - 1] + (a + s + 1) * cofactors[s]
            for s in range(1, b + 1)
        ),
        cofactors[b],
    ]


def pair_data(
    a: int,
    b: int,
    g_jets: list[int],
) -> dict[str, object]:
    d_values = d_sequence(a, b)
    v_values = [
        (a + 1 + r) * g_jets[a + r] - g_jets[a + 1 + r]
        for r in range(b + 1)
    ]
    differences = v_values[:]
    cofactors = [1]
    normalized = v_values[0]
    for order in range(1, b + 1):
        differences = [
            differences[index + 1] - differences[index]
            for index in range(len(differences) - 1)
        ]
        cofactors = cofactor_update(a, order, d_values, cofactors)
        normalized = (
            order * normalized
            + (-1) ** order * d_values[order] * differences[0]
        )

    by_v = sum(
        (-1) ** r * cofactors[r] * v_values[r] for r in range(b + 1)
    )
    if normalized != by_v:
        raise AssertionError("recurrence and v-cofactor formulas disagree")

    magnitudes = digit_coefficient_magnitudes(a, b, cofactors)
    by_digits = sum(
        (-1) ** s * magnitudes[s] * g_jets[a + s]
        for s in range(b + 2)
    )
    if normalized != by_digits:
        raise AssertionError("v and factorial-digit formulas disagree")

    content = 0
    for magnitude in magnitudes:
        content = math.gcd(content, magnitude)
    if content != 1:
        raise AssertionError("normalized digit coefficient vector is not primitive")

    capacity = sum(
        magnitudes[s] * max(0, a + s - 1) for s in range(b + 2)
    )
    return {
        "a": a,
        "b": b,
        "D": d_values[b],
        "normalized_determinant_F": normalized,
        "v_values": v_values,
        "cofactor_magnitudes": cofactors,
        "digit_coefficient_magnitudes": magnitudes,
        "digit_coefficient_content": content,
        "digit_bound_l1_capacity": capacity,
        "digit_block": g_jets[a : a + b + 2],
    }


def falling(value: int, order: int) -> int:
    if order > value:
        return 0
    return math.factorial(value) // math.factorial(value - order)


def c1_matrix(a: int, b: int, g_jets: list[int]) -> list[list[int]]:
    rows: list[list[int]] = []
    for k in range(a + 1, a + b + 2):
        row = [falling(k, j) * (k - j - 1) for j in range(b)]
        row.append(k * g_jets[k - 1] - g_jets[k])
        rows.append(row)
    return rows


def bareiss_determinant(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    work = [row[:] for row in matrix]
    sign = 1
    previous_pivot = 1
    for k in range(n - 1):
        pivot_row = next(
            (row for row in range(k, n) if work[row][k] != 0), None
        )
        if pivot_row is None:
            return 0
        if pivot_row != k:
            work[k], work[pivot_row] = work[pivot_row], work[k]
            sign = -sign
        pivot = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = work[i][j] * pivot - work[i][k] * work[k][j]
                if numerator % previous_pivot:
                    raise AssertionError("Bareiss division was not exact")
                work[i][j] = numerator // previous_pivot
            work[i][k] = 0
        previous_pivot = pivot
    return sign * work[n - 1][n - 1]


def kappa_b(b: int) -> int:
    return math.prod(math.factorial(j) for j in range(b))


def exact_record_json(data: dict[str, object]) -> dict[str, object]:
    F = int(data["normalized_determinant_F"])
    D = int(data["D"])
    capacity = int(data["digit_bound_l1_capacity"])
    result: dict[str, object] = {
        "a": data["a"],
        "b": data["b"],
        "D": str(D),
        "normalized_determinant_F": str(F),
        "normalized_determinant_sign": (F > 0) - (F < 0),
        "digit_coefficient_content": data["digit_coefficient_content"],
        "digit_bound_l1_capacity": str(capacity),
        "digit_block": data["digit_block"],
        "v_values": [str(value) for value in data["v_values"]],
        "cofactor_magnitudes": [
            str(value) for value in data["cofactor_magnitudes"]
        ],
        "digit_coefficient_magnitudes": [
            str(value) for value in data["digit_coefficient_magnitudes"]
        ],
    }
    if F:
        schur = Fraction(abs(F), D)
        relative = Fraction(abs(F), capacity)
        result["absolute_schur_residual"] = {
            "numerator": str(schur.numerator),
            "denominator": str(schur.denominator),
            "decimal_diagnostic": decimal_fraction(schur),
        }
        result["absolute_digit_box_ratio"] = {
            "numerator": str(relative.numerator),
            "denominator": str(relative.denominator),
            "decimal_diagnostic": decimal_fraction(relative),
        }
    else:
        result["absolute_schur_residual"] = None
        result["absolute_digit_box_ratio"] = None
    return result


def is_better_ratio(
    numerator: int,
    denominator: int,
    current: tuple[int, int, int, int] | None,
) -> bool:
    if current is None:
        return True
    return numerator * current[1] < current[0] * denominator


def jacobi_moment(a: int, order: int) -> int:
    size = order + 1
    vector = [1] + [0] * order
    for _ in range(order):
        new = [0] * size
        for index, value in enumerate(vector):
            if not value:
                continue
            new[index] += (a + 2 * index) * value
            if index + 1 < size:
                new[index + 1] += value
            if index:
                new[index - 1] += index * (index + a) * value
        vector = new
    return vector[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-total", type=int, default=530)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/independent_factorial_digit_c1_determinant_a_plus_b_530.json"
        ),
    )
    args = parser.parse_args()
    if args.max_total < 18:
        raise ValueError("max-total must be at least 18")

    pi_box = pi_interval()
    floors, digits = canonical_digits(args.max_total + 1, pi_box)
    if args.max_total == 530:
        digit_hash_530 = vector_sha256(digits[:531])
        if digit_hash_530 != EXPECTED_DIGIT_HASH_THROUGH_530:
            raise AssertionError("independent digits disagree with the prior certificate")
    else:
        digit_hash_530 = None
    g_jets = digits[:]
    g_jets[0] = 3

    record_stream = hashlib.sha256()
    pair_count = 0
    zero_pairs: list[tuple[int, int]] = []
    sign_counts_F = {"negative": 0, "zero": 0, "positive": 0}
    sign_counts_determinant = {"negative": 0, "zero": 0, "positive": 0}
    min_abs_F: tuple[int, int, int] | None = None
    all_abs_F_one: list[tuple[int, int]] = []
    min_schur: tuple[int, int, int, int] | None = None
    min_relative: tuple[int, int, int, int] | None = None
    max_F_digits: tuple[int, int, int] = (0, 0, 0)
    per_total: dict[int, dict[str, object]] = {}
    fixed_b: dict[int, dict[str, object]] = {
        b: {"count": 0, "zeros": [], "min_abs_F": None}
        for b in range(31)
    }
    diagonal_records: list[tuple[int, int, int]] = []

    selected_pairs = {
        (1, 0),
        (1, 1),
        (2, 0),
        (5, 0),
        (8, 3),
        (18, 1),
        (50, 10),
        (100, 50),
        (200, 100),
        (264, 265),
        (318, 212),
        (500, 30),
        (529, 1),
        (530, 0),
    }
    selected_data: dict[tuple[int, int], dict[str, object]] = {}

    for a in range(1, args.max_total + 1):
        maximum_b = min(args.max_total - a, a + 1)
        if maximum_b < 0:
            continue
        d_values = d_sequence(a, maximum_b)
        v_values = [
            (a + 1 + r) * g_jets[a + r] - g_jets[a + 1 + r]
            for r in range(maximum_b + 1)
        ]
        differences = v_values[:]
        cofactors = [1]
        previous_F = 0

        for b in range(maximum_b + 1):
            if b == 0:
                F = v_values[0]
            else:
                cofactors = cofactor_update(a, b, d_values, cofactors)
                F = (
                    b * previous_F
                    + (-1) ** b * d_values[b] * differences[0]
                )

            by_v = sum(
                (-1) ** r * cofactors[r] * v_values[r]
                for r in range(b + 1)
            )
            if F != by_v:
                raise AssertionError("scan recurrence/v formula mismatch")

            magnitudes = digit_coefficient_magnitudes(a, b, cofactors)
            by_digits = sum(
                (-1) ** s * magnitudes[s] * g_jets[a + s]
                for s in range(b + 2)
            )
            if F != by_digits:
                raise AssertionError("scan v/digit formula mismatch")

            content = 0
            for magnitude in magnitudes:
                content = math.gcd(content, magnitude)
            if content != 1:
                raise AssertionError("unexpected digit-coefficient content")

            capacity = sum(
                magnitudes[s] * max(0, a + s - 1)
                for s in range(b + 2)
            )
            D = d_values[b]
            pair_count += 1
            payload = [a, b, str(F), str(D), str(capacity)]
            record_stream.update(
                (json.dumps(payload, separators=(",", ":")) + "\n").encode()
            )

            total_summary = per_total.setdefault(
                a + b,
                {
                    "count": 0,
                    "negative_F": 0,
                    "zero_F": 0,
                    "positive_F": 0,
                    "minimum_nonzero_abs_F": None,
                },
            )
            total_summary["count"] = int(total_summary["count"]) + 1

            if F < 0:
                sign_counts_F["negative"] += 1
                total_summary["negative_F"] = int(total_summary["negative_F"]) + 1
            elif F > 0:
                sign_counts_F["positive"] += 1
                total_summary["positive_F"] = int(total_summary["positive_F"]) + 1
            else:
                sign_counts_F["zero"] += 1
                total_summary["zero_F"] = int(total_summary["zero_F"]) + 1
                zero_pairs.append((a, b))

            determinant_sign = ((-1) ** b) * ((F > 0) - (F < 0))
            if determinant_sign < 0:
                sign_counts_determinant["negative"] += 1
            elif determinant_sign > 0:
                sign_counts_determinant["positive"] += 1
            else:
                sign_counts_determinant["zero"] += 1

            if F:
                absolute_F = abs(F)
                current_total_min = total_summary["minimum_nonzero_abs_F"]
                if current_total_min is None or absolute_F < int(
                    current_total_min["absolute_F"]
                ):
                    total_summary["minimum_nonzero_abs_F"] = {
                        "a": a,
                        "b": b,
                        "absolute_F": str(absolute_F),
                    }
                candidate_F = (absolute_F, a, b)
                if min_abs_F is None or candidate_F < min_abs_F:
                    min_abs_F = candidate_F
                if absolute_F == 1:
                    all_abs_F_one.append((a, b))
                if is_better_ratio(absolute_F, D, min_schur):
                    min_schur = (absolute_F, D, a, b)
                if is_better_ratio(absolute_F, capacity, min_relative):
                    min_relative = (absolute_F, capacity, a, b)

            f_digits = len(str(abs(F))) if F else 1
            if f_digits > max_F_digits[0]:
                max_F_digits = (f_digits, a, b)

            if b <= 30:
                fixed = fixed_b[b]
                fixed["count"] = int(fixed["count"]) + 1
                if not F:
                    fixed["zeros"].append([a, b])
                elif fixed["min_abs_F"] is None or abs(F) < int(
                    fixed["min_abs_F"]["absolute_F"]
                ):
                    fixed["min_abs_F"] = {
                        "a": a,
                        "b": b,
                        "absolute_F": str(abs(F)),
                    }

            if a == b:
                diagonal_records.append((a, b, F))

            if (a, b) in selected_pairs:
                selected_data[(a, b)] = {
                    "a": a,
                    "b": b,
                    "D": D,
                    "normalized_determinant_F": F,
                    "v_values": v_values[: b + 1],
                    "cofactor_magnitudes": cofactors[:],
                    "digit_coefficient_magnitudes": magnitudes,
                    "digit_coefficient_content": content,
                    "digit_bound_l1_capacity": capacity,
                    "digit_block": g_jets[a : a + b + 2],
                }

            previous_F = F
            differences = [
                differences[index + 1] - differences[index]
                for index in range(len(differences) - 1)
            ]

    if min_abs_F is None or min_schur is None or min_relative is None:
        raise AssertionError("empty nonzero scan")

    # Direct fraction-free determinant checks in the complete small box.
    direct_checks = 0
    for a in range(1, 19):
        for b in range(min(18 - a, a + 1) + 1):
            data = pair_data(a, b, g_jets)
            direct = bareiss_determinant(c1_matrix(a, b, g_jets))
            predicted = (
                (-1) ** b
                * kappa_b(b)
                * int(data["normalized_determinant_F"])
            )
            if direct != predicted:
                raise AssertionError("direct Bareiss determinant mismatch")
            direct_checks += 1

    # The Jacobi matrix for shifted Gamma/Laguerre moments reproduces D.
    jacobi_checks = 0
    for a in (1, 2, 7, 19):
        expected = d_sequence(a, 14)
        for order in range(15):
            if jacobi_moment(a, order) != expected[order]:
                raise AssertionError("Jacobi continued-fraction moment mismatch")
            jacobi_checks += 1

    # Exact adversarial checks: constant-one digits make v(k)=k-1 and
    # annihilate every b>=1 determinant; zero pairs annihilate b=0.
    adversarial_checks = 0
    for a, b in ((2, 0), (5, 1), (20, 2), (100, 7), (200, 100)):
        data = pair_data(a, b, g_jets)
        magnitudes = [int(value) for value in data["digit_coefficient_magnitudes"]]
        if b == 0:
            adversarial_value = 0
        else:
            adversarial_value = sum(
                (-1) ** s * magnitudes[s] for s in range(b + 2)
            )
        if adversarial_value != 0:
            raise AssertionError("adversarial zero pattern failed")
        adversarial_checks += 1

    selected_keys = set(selected_data)
    selected_keys.update(zero_pairs)
    selected_keys.add((min_abs_F[1], min_abs_F[2]))
    selected_keys.add((min_schur[2], min_schur[3]))
    selected_keys.add((min_relative[2], min_relative[3]))
    for pair in sorted(selected_keys):
        if pair not in selected_data:
            selected_data[pair] = pair_data(pair[0], pair[1], g_jets)

    result = {
        "description": (
            "Independent exact c=1 determinant theorem checks and canonical "
            "factorial-digit scan"
        ),
        "status": (
            "all determinant/content identities are all-degree; canonical "
            "digit zero/minimum facts are finite diagnostics"
        ),
        "parameters": {
            "max_a_plus_b": args.max_total,
            "admissibility": "a>=max(1,b-1)",
            "pair_count": pair_count,
            "maximum_digit_index": args.max_total + 1,
        },
        "pi_and_digit_certificate": {
            "identity": "pi=4*(atan(1/2)+atan(1/3))",
            "atan_half_last_index": 2100,
            "atan_third_last_index": 1400,
            "pi_lower_sha256": fraction_sha256(pi_box[0]),
            "pi_upper_sha256": fraction_sha256(pi_box[1]),
            "floor_531_factorial_pi": str(floors[531])
            if args.max_total >= 530
            else None,
            "digits_through_530_sha256": digit_hash_530,
            "digits_through_max_plus_1_sha256": vector_sha256(digits),
            "new_digit_d_531": digits[531] if args.max_total >= 530 else None,
        },
        "all_degree_identity_checks": {
            "all_recurrence_v_digit_formulas_agree": True,
            "all_normalized_digit_coefficient_contents_equal_one": True,
            "complete_small_box_direct_Bareiss_checks": direct_checks,
            "shifted_gamma_J_fraction_moment_checks": jacobi_checks,
            "adversarial_zero_checks": adversarial_checks,
        },
        "finite_scan": {
            "record_stream_sha256": record_stream.hexdigest(),
            "sign_counts_normalized_F": sign_counts_F,
            "sign_counts_full_determinant": sign_counts_determinant,
            "zero_count": len(zero_pairs),
            "zero_pairs": [list(pair) for pair in zero_pairs],
            "minimum_nonzero_absolute_F": {
                "absolute_F": str(min_abs_F[0]),
                "a": min_abs_F[1],
                "b": min_abs_F[2],
                "all_pairs_with_absolute_F_one": [
                    list(pair) for pair in all_abs_F_one
                ],
            },
            "minimum_absolute_schur_residual_F_over_D": {
                "numerator": str(Fraction(min_schur[0], min_schur[1]).numerator),
                "denominator": str(
                    Fraction(min_schur[0], min_schur[1]).denominator
                ),
                "a": min_schur[2],
                "b": min_schur[3],
                "decimal_diagnostic": decimal_fraction(
                    Fraction(min_schur[0], min_schur[1])
                ),
            },
            "minimum_nonzero_digit_box_ratio": {
                "numerator": str(
                    Fraction(min_relative[0], min_relative[1]).numerator
                ),
                "denominator": str(
                    Fraction(min_relative[0], min_relative[1]).denominator
                ),
                "a": min_relative[2],
                "b": min_relative[3],
                "decimal_diagnostic": decimal_fraction(
                    Fraction(min_relative[0], min_relative[1])
                ),
            },
            "maximum_F_decimal_digits": {
                "digits": max_F_digits[0],
                "a": max_F_digits[1],
                "b": max_F_digits[2],
            },
            "fixed_b_0_through_30": {
                str(key): value for key, value in fixed_b.items()
            },
            "diagonal_b_equals_a": [
                {
                    "a": a,
                    "b": b,
                    "sign_F": (F > 0) - (F < 0),
                    "absolute_F_decimal_digits": len(str(abs(F))) if F else 1,
                    "F_sha256": sha256_text(str(F)),
                }
                for a, b, F in diagonal_records
            ],
            "per_total": {
                str(key): value for key, value in sorted(per_total.items())
            },
        },
        "selected_exact_records": [
            exact_record_json(selected_data[key]) for key in sorted(selected_data)
        ],
        "warning": (
            "The 71,019 canonical-pi records are finite.  Digit bounds alone "
            "force neither sign nor nonvanishing; the theorem note gives "
            "explicit adversarial digit blocks."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result["all_degree_identity_checks"], indent=2, sort_keys=True))
    print(
        json.dumps(
            {
                "parameters": result["parameters"],
                "finite_scan_core": {
                    key: result["finite_scan"][key]
                    for key in (
                        "record_stream_sha256",
                        "sign_counts_normalized_F",
                        "zero_count",
                        "zero_pairs",
                        "minimum_nonzero_absolute_F",
                        "minimum_absolute_schur_residual_F_over_D",
                        "minimum_nonzero_digit_box_ratio",
                        "maximum_F_decimal_digits",
                    )
                },
            },
            indent=2,
            sort_keys=True,
        )
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
