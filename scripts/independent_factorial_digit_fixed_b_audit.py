#!/usr/bin/env python3
"""Independent audit of the canonical-factorial-digit fixed-b theorem.

Independence from the source finite probe:

* pi is enclosed with
      pi = 4*(atan(1/2) + atan(1/3)),
  rather than Machin's 16*atan(1/5)-4*atan(1/239);
* forward differences are formed by repeated differencing, rather than the
  binomial sum used by the source;
* finite minima are selected and separated using Fraction comparisons only;
* selected complete HP matrices in A, B, gamma are solved over QQ and their
  fully primitive endpoint pairs are reconstructed.

The script verifies the entire 15094-point a<=500, b<=30 archive.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from math import factorial, gcd
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy.polys.matrices import DomainMatrix


sys.set_int_max_str_digits(0)

BASE = Path("/content/drive/MyDrive/e_pi_research_20260826")
SOURCE = BASE / "sources/factorial_digit_entire_fixed_b_rays.md"
SCRIPT = BASE / "scripts/factorial_digit_entire_nondiagonal_probe.py"
RESULT = BASE / "results/factorial_digit_entire_nondiagonal_a500_b30.json"

EXPECTED_HASHES = {
    str(SOURCE): "66e5e2f46ad10db1bd60ce5a93e7a85a9cb3e02d933b3da78bf09a2815b30f7d",
    str(SCRIPT): "997127083235cafcef7d815feef587db3d4c6c02d56e4d62d749614a3b145c93",
    str(RESULT): "84cb3eaafeba0887c8291883a0acb0e727217d0c3df509bab9ef9fe808522741",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def fraction_sha256(value: Fraction) -> str:
    return sha256_bytes(
        f"{value.numerator}/{value.denominator}".encode()
    )


def integer_sha256(value: int) -> str:
    return sha256_bytes(str(value).encode())


def vector_sha256(values: list[int]) -> str:
    return sha256_bytes(
        json.dumps(values, separators=(",", ":")).encode()
    )


def decimal_fraction(value: Fraction, digits: int = 45) -> str:
    mp.mp.dps = digits + 20
    return mp.nstr(
        mp.mpf(value.numerator) / mp.mpf(value.denominator), digits
    )


def alternating_atan_interval(
    inverse: int, last_index: int
) -> tuple[Fraction, Fraction]:
    """Directed alternating-series enclosure of atan(1/inverse)."""
    partial = Fraction()
    power = inverse
    square = inverse * inverse
    for k in range(last_index + 1):
        term = Fraction(1, (2 * k + 1) * power)
        partial += -term if k & 1 else term
        power *= square
    omitted = Fraction(1, (2 * last_index + 3) * power)
    if last_index & 1:
        lower, upper = partial, partial + omitted
    else:
        lower, upper = partial - omitted, partial
    assert lower < upper
    return lower, upper


def independent_pi_interval() -> tuple[Fraction, Fraction]:
    """Use tan(atan(1/2)+atan(1/3))=1, hence the sum is pi/4."""
    a_lower, a_upper = alternating_atan_interval(2, 2400)
    b_lower, b_upper = alternating_atan_interval(3, 1600)
    return 4 * (a_lower + b_lower), 4 * (a_upper + b_upper)


def independent_e_interval(last_index: int = 700) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, factorial(k)) for k in range(last_index + 1)),
        Fraction(),
    )
    # For N>=1, sum_{k>N} 1/k! < 1/(N*N!).
    return partial, partial + Fraction(
        1, last_index * factorial(last_index)
    )


def rational_floor(value: Fraction) -> int:
    return value.numerator // value.denominator


def repeated_forward_difference(
    values: list[int], start: int, order: int
) -> int:
    row = values[start : start + order + 1]
    for _ in range(order):
        row = [row[j + 1] - row[j] for j in range(len(row) - 1)]
    assert len(row) == 1
    return row[0]


def absolute_box(lower: Fraction, upper: Fraction) -> tuple[Fraction, Fraction]:
    assert lower <= upper and not (lower <= 0 <= upper)
    if lower > 0:
        return lower, upper
    return -upper, -lower


def primitive_integer_vector(vector: sp.Matrix) -> list[int]:
    denominator = sp.ilcm(*[entry.q for entry in vector])
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(value) for value in integers if value))
    integers = [value // common for value in integers]
    first = next(value for value in integers if value)
    return integers if first > 0 else [-value for value in integers]


def falling(k: int, j: int) -> int:
    if j > k:
        return 0
    return factorial(k) // factorial(k - j)


def complete_hp_endpoint_check(
    a: int,
    b: int,
    digits: list[int],
    factorials: list[int],
    combined: list[int],
) -> dict:
    """Solve the full A,B,gamma HP matrix over QQ."""
    g_jets = [3, 0] + digits[2:]
    rows: list[list[int]] = []
    for k in range(a + b + 1):
        a_columns = [
            factorial(k) if j == k else 0 for j in range(a + 1)
        ]
        b_columns = [falling(k, j) for j in range(b + 1)]
        rows.append(a_columns + b_columns + [g_jets[k]])
    rows.append(
        [0] * (a + 1) + [1] * (b + 1) + [-1]
    )
    matrix = sp.Matrix(rows)
    domain = DomainMatrix.from_Matrix(matrix).to_field()
    rank = domain.rank()
    kernel = domain.nullspace()
    assert rank == matrix.cols - 1
    assert kernel.shape[0] == 1
    vector = primitive_integer_vector(kernel.to_Matrix().row(0).T)
    a_values = vector[: a + 1]
    gamma = vector[-1]
    assert gamma != 0
    endpoint_a = sum(a_values)
    common = gcd(abs(endpoint_a), abs(gamma))
    alpha, beta = endpoint_a // common, gamma // common
    if beta < 0:
        alpha, beta = -alpha, -beta

    w = repeated_forward_difference(factorials, a, b)
    z = repeated_forward_difference(combined, a, b)
    h = gcd(w, z)
    expected = [-z // h, w // h]
    assert [alpha, beta] == expected
    return {
        "a": a,
        "b": b,
        "matrix_shape": list(matrix.shape),
        "rank": rank,
        "nullity": 1,
        "primitive_full_vector_sha256": vector_sha256(vector),
        "reduced_endpoint_pair_sha256": vector_sha256([alpha, beta]),
        "endpoint_pair_matches_Delta_formula": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    actual_hashes = {
        path: file_sha256(Path(path)) for path in EXPECTED_HASHES
    }
    assert actual_hashes == EXPECTED_HASHES
    archived = json.loads(RESULT.read_text())

    maximum = 530
    factorials = [factorial(n) for n in range(maximum + 1)]
    pi_lower, pi_upper = independent_pi_interval()
    e_lower, e_upper = independent_e_interval()
    s_lower, s_upper = e_lower + pi_lower, e_upper + pi_upper

    pi_floors: list[int] = []
    e_floors: list[int] = []
    combined: list[int] = []
    for n, n_factorial in enumerate(factorials):
        lower_floor = rational_floor(n_factorial * pi_lower)
        upper_floor = rational_floor(n_factorial * pi_upper)
        assert lower_floor == upper_floor
        pi_floors.append(lower_floor)

        # This is the integral numerator of the e Taylor truncation.  At
        # n=0 it is B_0=1 by convention; for n>=1 it is floor(n!*e).
        e_floor = sum(
            n_factorial // factorials[k] for k in range(n + 1)
        )
        e_floors.append(e_floor)
        combined.append(e_floor + lower_floor)

    digits = [0, 0]
    for n in range(2, maximum + 1):
        digit = pi_floors[n] - n * pi_floors[n - 1]
        assert 0 <= digit <= n - 1
        digits.append(digit)
        assert combined[n] == n * combined[n - 1] + digit + 1

    records: list[dict] = []
    per_b: dict[int, list[dict]] = {}
    stream = hashlib.sha256()
    threshold_counts = {
        str(threshold): [0] * 31
        for threshold in (
            Fraction(1),
            Fraction(1, 10**4),
            Fraction(1, 10**8),
            Fraction(1, 10**12),
        )
    }

    for b in range(31):
        items: list[dict] = []
        for a in range(max(1, b - 1), 501):
            w = repeated_forward_difference(factorials, a, b)
            z = repeated_forward_difference(combined, a, b)
            assert w > 0
            h = gcd(w, z)
            delta_lower = w * s_lower - z
            delta_upper = w * s_upper - z
            assert not (delta_lower <= 0 <= delta_upper)
            delta_abs_lower, delta_abs_upper = absolute_box(
                delta_lower, delta_upper
            )
            value_abs_lower = delta_abs_lower / h
            value_abs_upper = delta_abs_upper / h
            sign = 1 if delta_lower > 0 else -1
            item = {
                "a": a,
                "b": b,
                "W": w,
                "Z": z,
                "H": h,
                "sign": sign,
                "delta_abs_lower": delta_abs_lower,
                "delta_abs_upper": delta_abs_upper,
                "value_abs_lower": value_abs_lower,
                "value_abs_upper": value_abs_upper,
            }
            items.append(item)
            records.append(item)
            stream.update(f"{a},{b},{w},{z},{h};".encode())
            for threshold_text, counts in threshold_counts.items():
                if value_abs_upper < Fraction(threshold_text):
                    counts[b] += 1
        per_b[b] = items

    assert len(records) == 15094

    def exact_unique_minimum(items: list[dict]) -> tuple[dict, Fraction]:
        winner = min(items, key=lambda item: item["value_abs_upper"])
        competing_lower = min(
            item["value_abs_lower"]
            for item in items
            if item is not winner
        )
        assert winner["value_abs_upper"] < competing_lower
        return winner, competing_lower

    minima = [exact_unique_minimum(per_b[b])[0] for b in range(31)]
    global_winner, global_competing_lower = exact_unique_minimum(records)

    # Check D_{a,b}=Delta^b(a!)/a! independently through the whole box.
    determinant_recurrence_checks = 0
    for a in range(1, 501):
        previous_two = 1
        previous_one = a
        assert (
            repeated_forward_difference(factorials, a, 1)
            == factorials[a] * previous_one
        )
        determinant_recurrence_checks += 1
        for b in range(2, 31):
            value = (
                (a + b - 1) * previous_one
                + (b - 1) * previous_two
            )
            assert (
                repeated_forward_difference(factorials, a, b)
                == factorials[a] * value
            )
            previous_two, previous_one = previous_one, value
            determinant_recurrence_checks += 1

    # Compare every archived structural field that is independent of the
    # source interval endpoints.
    comparisons: dict[str, bool] = {}
    comparisons["record_count"] = (
        archived["scan_box"]["number_of_endpoint_records"] == len(records)
    )
    comparisons["digit_vector"] = (
        archived["canonical_digit_certificate"]["digit_vector_sha256"]
        == vector_sha256(digits)
    )
    comparisons["pi_floor_vector"] = (
        archived["canonical_digit_certificate"][
            "pi_factorial_floor_vector_sha256"
        ]
        == vector_sha256(pi_floors)
    )
    comparisons["combined_vector"] = (
        archived["canonical_digit_certificate"]["combined_C_vector_sha256"]
        == vector_sha256(combined)
    )
    comparisons["record_stream"] = (
        archived["record_stream_a_b_W_Z_H_sha256"]
        == stream.hexdigest()
    )
    comparisons["threshold_counts"] = (
        archived["certified_counts_strictly_below_threshold_by_b"]
        == threshold_counts
    )

    for b, source_minimum in enumerate(
        archived["all_b_minimum_summaries"]
    ):
        winner = minima[b]
        assert (winner["a"], winner["b"]) == (
            source_minimum["a"],
            source_minimum["b"],
        )
        assert winner["H"] == source_minimum["H_gcd_W_Z"]["value"]
        assert winner["sign"] == source_minimum[
            "primitive_endpoint_interval"
        ]["certified_sign"]
    comparisons["all_31_minimizers_and_signs"] = True

    source_global = archived["global_minimum_in_scan_box"]
    assert (global_winner["a"], global_winner["b"]) == (
        source_global["a"],
        source_global["b"],
    )
    for source_key, independent_key in (
        ("W_Delta_b_factorial", "W"),
        ("Z_Delta_b_combined_numerator", "Z"),
        ("H_gcd_W_Z", "H"),
    ):
        assert source_global[source_key]["value"] == global_winner[
            independent_key
        ]
    assert source_global["reduced_endpoint_pair_alpha_beta"] == [
        -global_winner["Z"] // global_winner["H"],
        global_winner["W"] // global_winner["H"],
    ]
    comparisons["global_minimum_exact_data"] = True
    assert all(comparisons.values())

    full_hp_parameters = [
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (5, 6),
        (8, 2),
        (12, 10),
        (29, 30),
    ]
    full_hp_checks = [
        complete_hp_endpoint_check(
            a, b, digits, factorials, combined
        )
        for a, b in full_hp_parameters
    ]

    def minimum_summary(item: dict) -> dict:
        return {
            "a": item["a"],
            "b": item["b"],
            "H": item["H"],
            "H_sha256": integer_sha256(item["H"]),
            "absolute_Delta_b_x_lower_sha256": fraction_sha256(
                item["delta_abs_lower"]
            ),
            "absolute_Delta_b_x_upper_sha256": fraction_sha256(
                item["delta_abs_upper"]
            ),
            "absolute_L_lower_sha256": fraction_sha256(
                item["value_abs_lower"]
            ),
            "absolute_L_upper_sha256": fraction_sha256(
                item["value_abs_upper"]
            ),
            "absolute_Delta_b_x_decimal_diagnostic": decimal_fraction(
                (item["delta_abs_lower"] + item["delta_abs_upper"]) / 2
            ),
            "absolute_L_decimal_diagnostic": decimal_fraction(
                (item["value_abs_lower"] + item["value_abs_upper"]) / 2
            ),
        }

    result = {
        "verdict": "accept",
        "frozen_input_sha256": actual_hashes,
        "independent_pi_identity": (
            "pi=4*(atan(1/2)+atan(1/3)); tangent addition gives "
            "tan(sum)=1 and 0<sum<pi/2"
        ),
        "independent_interval_parameters": {
            "atan_1_over_2_last_index": 2400,
            "atan_1_over_3_last_index": 1600,
            "e_taylor_last_index": 700,
            "pi_width_sha256": fraction_sha256(pi_upper - pi_lower),
            "e_plus_pi_width_sha256": fraction_sha256(
                s_upper - s_lower
            ),
        },
        "independent_vector_sha256": {
            "canonical_digits_through_530": vector_sha256(digits),
            "pi_factorial_floors_through_530": vector_sha256(pi_floors),
            "combined_C_through_530": vector_sha256(combined),
        },
        "full_HP_matrix_endpoint_checks": full_hp_checks,
        "determinant_recurrence_checks": determinant_recurrence_checks,
        "finite_box": {
            "a_maximum": 500,
            "b_maximum": 30,
            "record_count": len(records),
            "all_endpoint_intervals_exclude_zero": True,
            "all_31_fixed_b_minima_have_disjoint_exact_intervals": True,
            "record_stream_a_b_W_Z_H_sha256": stream.hexdigest(),
            "small_b_minima": [
                minimum_summary(minima[b]) for b in range(7)
            ],
            "global_minimum": minimum_summary(global_winner),
            "global_smallest_competing_L_lower_sha256": fraction_sha256(
                global_competing_lower
            ),
            "global_smallest_competing_L_lower_decimal_diagnostic": (
                decimal_fraction(global_competing_lower)
            ),
            "threshold_counts": threshold_counts,
        },
        "archived_structural_comparisons": comparisons,
        "all_archived_structural_comparisons_pass": True,
        "theorem_checks": {
            "Delta_endpoint_identity_rederived_in_audit_note": True,
            "rational_case_equivalence_rederived_in_audit_note": True,
            "Roth_inequality_orientation_rederived_in_audit_note": True,
        },
        "warning": (
            "The finite scan certifies only the stated box.  It supplies "
            "no asymptotic nonvanishing, gcd-growth, irrationality, or "
            "transcendence theorem."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
