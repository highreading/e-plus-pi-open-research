#!/usr/bin/env python3
"""Deterministic exact diagnostics for the two-pole fresh-prime reduction.

This is a finite probe, not a proof that the fixed-gap determinant is
nonzero for every gap.  It uses only the Python standard library and the
frozen width-49 certificate module.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from types import ModuleType


DEPENDENCY_NAME = "mixed_cubic_large_prime_log_residue_fixed_gap_certificate.py"
DEPENDENCY_SHA256 = (
    "272913d09c4a2f7d7d844f78dee9a900d47f0793c89d4f76b32da59273054769"
)
RECURRENCE_MODULUS = 1_000_000_007
RESULTANT_LIMIT = 180
HEIGHT_AUDIT_LIMIT = 80
RECURRENCE_TERMS = 28
RECURRENCE_MAX_ORDER = 6
RECURRENCE_MAX_DEGREE = 5


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_dependency(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("fixed_gap_certificate", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            answer[first + second] += left_value * right_value
    return answer


def polynomial_power(base: list[int], exponent: int) -> list[int]:
    answer = [1]
    factor = base
    while exponent:
        if exponent & 1:
            answer = polynomial_multiply(answer, factor)
        factor = polynomial_multiply(factor, factor)
        exponent //= 2
    return answer


def rational_series(
    numerator: list[int], denominator: list[int], degree: int
) -> list[Fraction]:
    answer: list[Fraction] = []
    for target in range(degree + 1):
        value = Fraction(numerator[target] if target < len(numerator) else 0)
        for lag in range(1, min(target, len(denominator) - 1) + 1):
            value -= denominator[lag] * answer[target - lag]
        answer.append(value / denominator[0])
    return answer


def fraction_mod(value: Fraction, prime: int) -> int:
    denominator = value.denominator % prime
    assert denominator
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def verify_two_pole_formulas() -> list[dict[str, int]]:
    # A=-2+3t-t^2 and R=2-2t+t^2.
    a_polynomial = [-2, 3, -1]
    r_polynomial = [2, -2, 1]
    samples = [(1, 11), (3, 31), (4, 41), (7, 71)]
    records = []
    for m_value, prime in samples:
        delta = prime - 6 * m_value
        exponent = 2 * m_value + delta - 2
        target = 4 * m_value
        polynomial_degree = 4 * m_value - 4

        h_coefficients = rational_series(
            polynomial_power(r_polynomial, exponent),
            polynomial_power(a_polynomial, delta),
            target + 1,
        )
        c_coefficients = rational_series(
            polynomial_power([1, 0, 1], exponent),
            polynomial_power([1, 1], delta),
            delta - 1,
        )
        principal = {
            ell: -c_coefficients[delta - ell] for ell in range(1, delta + 1)
        }

        for index in (target, target + 1):
            first_pole = sum(
                principal[ell] * math.comb(index + ell - 1, ell - 1)
                for ell in principal
            )
            second_pole = Fraction(2) ** (2 * m_value - 2 - index) * sum(
                (-1) ** ell
                * principal[ell]
                * math.comb(index - polynomial_degree - 1, ell - 1)
                for ell in principal
                if ell - 1 <= index - polynomial_degree - 1
            )
            assert h_coefficients[index] == first_pole + second_pole

            hahn_coefficient = -sum(
                c_coefficients[power]
                * math.comb(
                    index + delta - 1 - power,
                    delta - 1 - power,
                )
                for power in range(delta)
            )
            assert first_pole == hahn_coefficient

        f_coefficients = rational_series(
            polynomial_power(a_polynomial, 6 * m_value),
            polynomial_power(r_polynomial, 4 * m_value + 2),
            target + 1,
        )
        for index, (f_value, h_value) in enumerate(
            zip(f_coefficients, h_coefficients)
        ):
            assert fraction_mod(f_value + h_value, prime) == 0, (
                m_value,
                prime,
                index,
            )

        records.append(
            {
                "m": m_value,
                "p": prime,
                "delta": delta,
                "checked_through_coefficient": target + 1,
            }
        )
    return records


def matrix_rank_mod(matrix: list[list[int]], prime: int) -> int:
    if not matrix:
        return 0
    answer = [row[:] for row in matrix]
    row_count = len(answer)
    column_count = len(answer[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if answer[row][column] % prime
            ),
            None,
        )
        if pivot is None:
            continue
        answer[pivot_row], answer[pivot] = answer[pivot], answer[pivot_row]
        inverse = pow(answer[pivot_row][column] % prime, -1, prime)
        answer[pivot_row] = [
            value * inverse % prime for value in answer[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row:
                continue
            multiplier = answer[row][column] % prime
            if multiplier:
                answer[row] = [
                    (value - multiplier * pivot_value) % prime
                    for value, pivot_value in zip(
                        answer[row], answer[pivot_row]
                    )
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def recurrence_diagnostic(
    values: list[Fraction], prime: int
) -> tuple[int, list[dict[str, int]]]:
    modular_values = [fraction_mod(value, prime) for value in values]
    tested = 0
    deficient = []
    for order in range(1, RECURRENCE_MAX_ORDER + 1):
        for degree in range(RECURRENCE_MAX_DEGREE + 1):
            columns = (order + 1) * (degree + 1)
            rows = len(values) - order
            if rows < columns:
                continue
            matrix = [
                [
                    modular_values[index + shift]
                    * pow(index, power, prime)
                    % prime
                    for shift in range(order + 1)
                    for power in range(degree + 1)
                ]
                for index in range(rows)
            ]
            rank = matrix_rank_mod(matrix, prime)
            tested += 1
            if rank < columns:
                deficient.append(
                    {
                        "order": order,
                        "degree": degree,
                        "rank": rank,
                        "columns": columns,
                    }
                )
    return tested, deficient


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_suffix(".json"),
    )
    arguments = parser.parse_args()

    script_path = Path(__file__).resolve()
    dependency_path = script_path.parent / DEPENDENCY_NAME
    dependency_hash = sha256_file(dependency_path)
    assert dependency_hash == DEPENDENCY_SHA256
    certificate = load_dependency(dependency_path)
    assert certificate.is_prime(RECURRENCE_MODULUS)

    exact_values: dict[int, Fraction] = {}
    fixed_data: dict[
        int, tuple[Fraction, Fraction, Fraction, Fraction]
    ] = {}
    resultant_rows = []
    canonical_values = []
    for q_value in range(1, RESULTANT_LIMIT, 2):
        if q_value % 3 == 0:
            continue
        c0, t0 = certificate.full_and_tail(q_value, 0)
        c1, t1 = certificate.full_and_tail(q_value, 1)
        resultant = c0 * t1 - c1 * t0
        assert resultant
        exact_values[q_value] = resultant
        fixed_data[q_value] = (c0, t0, c1, t1)
        canonical = f"{resultant.numerator}/{resultant.denominator}"
        canonical_values.append(f"{q_value}:{canonical}")
        resultant_rows.append(
            {
                "q": q_value,
                "sign": 1 if resultant > 0 else -1,
                "numerator_digits": len(str(abs(resultant.numerator))),
                "denominator_digits": len(str(resultant.denominator)),
                "exact_value_sha256": sha256_bytes(canonical.encode("ascii")),
            }
        )

    height_rows = []
    for q_value in sorted(fixed_data):
        if q_value < 5 or q_value >= HEIGHT_AUDIT_LIMIT:
            continue
        c0, t0, c1, t1 = fixed_data[q_value]
        degree = q_value - 1
        assert (2**degree * 3 ** (2 * degree)) % c0.denominator == 0
        assert (2 ** (degree + 1) * 3 ** (2 * degree)) % c1.denominator == 0
        assert 3 ** (2 * degree) % t0.denominator == 0
        assert 3 ** (2 * degree) % t1.denominator == 0
        assert abs(c0) <= 3 * q_value**2 * 24**q_value
        assert abs(c1) <= Fraction(81, 2) * q_value**2 * 24**q_value
        assert abs(t0) <= 2 * q_value * 16**q_value
        assert abs(t1) <= 16 * q_value * 16**q_value
        resultant = exact_values[q_value]
        assert (
            abs(resultant.numerator)
            <= 129 * q_value**3 * 62208**q_value
        )
        height_rows.append(q_value)

    recurrence_records = []
    for residue in (1, 5):
        values = [
            exact_values[6 * index + residue]
            for index in range(RECURRENCE_TERMS)
        ]
        tested, deficient = recurrence_diagnostic(
            values, RECURRENCE_MODULUS
        )
        assert not deficient
        recurrence_records.append(
            {
                "q_form": f"6r+{residue}",
                "terms": RECURRENCE_TERMS,
                "r_range": [0, RECURRENCE_TERMS - 1],
                "maximum_order": RECURRENCE_MAX_ORDER,
                "maximum_polynomial_degree": RECURRENCE_MAX_DEGREE,
                "modulus": RECURRENCE_MODULUS,
                "full_column_rank_for_tested_ansatzes": True,
                "tested_ansatz_count": tested,
            }
        )

    signs = {row["q"]: row["sign"] for row in resultant_rows}
    assert [signs[q] for q in (1, 5, 7, 11, 13)] == [-1, 1, -1, -1, 1]

    output = {
        "schema_version": 1,
        "scope_warning": (
            "All resultant and recurrence statements in this file are finite "
            "diagnostics, not an all-q theorem."
        ),
        "generator": {
            "path": script_path.name,
            "sha256": sha256_file(script_path),
        },
        "dependency": {
            "path": dependency_path.name,
            "sha256": dependency_hash,
        },
        "two_pole_formula_audit": {
            "status": "passed",
            "samples": verify_two_pole_formulas(),
        },
        "exact_resultant_probe": {
            "admissible_q_condition": (
                "1 <= q < 180, q odd, and q not divisible by 3"
            ),
            "count": len(resultant_rows),
            "all_nonzero": True,
            "aggregate_exact_values_sha256": sha256_bytes(
                "\n".join(canonical_values).encode("ascii")
            ),
            "rows": resultant_rows,
        },
        "fixed_sign_hypothesis": {
            "status": "refuted",
            "exact_signs": {
                str(q): signs[q] for q in (1, 5, 7, 11, 13)
            },
        },
        "height_bound_finite_audit": {
            "universal_bound_proved_separately": (
                "|num(R_q)| <= 129*q^3*62208^q"
            ),
            "audited_admissible_q": height_rows,
            "status": "passed",
        },
        "polynomial_recurrence_search": {
            "status": "no_relation_in_bounded_ansatz",
            "records": recurrence_records,
        },
    }
    serialized = json.dumps(
        output, indent=2, sort_keys=True, ensure_ascii=True
    ) + "\n"
    arguments.output.write_text(serialized, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

