#!/usr/bin/env python3
"""Exact replay for the actual-secant equal-jet sign barrier.

The script independently reconstructs F=1/(2 cosh(sqrt(x))), solves the
required Pade systems over Q, clears each denominator to a primitive integer
polynomial, builds the full integer equal-jet matrices, and computes their
determinants.  No floating-point arithmetic or stored sign oracle is used.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

from flint import __version__ as flint_version
from flint import fmpq, fmpq_mat, fmpz_mat


sys.set_int_max_str_digits(1_000_000)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/centered_cosh_equal_jet_actual_sign_barrier.md"
OUTPUT = ROOT / "results/centered_cosh_equal_jet_actual_sign_barrier_certificate.json"

# Filled after the source is frozen; the replay refuses a silent source edit.
SOURCE_SHA256 = "45bfb6497840dc9f9e0a997091c56d104d66157a992c57f598c31bd1001da218"

WITNESS_M = (6, 7, 14, 15)
EXPECTED_THETA6_SIGNS = {6: 1, 7: -1, 14: -1, 15: 1}
MAX_SERIES_DEGREE = 31
RSS_GUARD_KIB = 4 * 1024 * 1024


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte != 10
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def to_fmpq(value: Fraction | int) -> fmpq:
    value = Fraction(value)
    return fmpq(value.numerator, value.denominator)


def from_fmpq(value: fmpq) -> Fraction:
    return Fraction(int(value.numerator), int(value.denominator))


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def integer_list_digest(values: list[int]) -> str:
    return sha256_bytes("".join(f"{value}\n" for value in values).encode())


def secant_f_coefficients(limit: int) -> list[Fraction]:
    """Coefficients of F(x)=1/(2 cosh(sqrt(x))) from its exact recurrence."""
    coefficients = [Fraction(1, 2)]
    for degree in range(1, limit + 1):
        coefficients.append(
            -sum(
                Fraction(1, math.factorial(2 * index))
                * coefficients[degree - index]
                for index in range(1, degree + 1)
            )
        )
    # Independent convolution check of 2 F cosh(sqrt(x)) = 1.
    for degree in range(limit + 1):
        convolution = 2 * sum(
            coefficients[degree - index]
            * Fraction(1, math.factorial(2 * index))
            for index in range(degree + 1)
        )
        assert convolution == (1 if degree == 0 else 0)
    return coefficients


F_COEFFICIENTS = secant_f_coefficients(MAX_SERIES_DEGREE)


@lru_cache(maxsize=None)
def pade_denominator(numerator_degree: int, denominator_degree: int) -> tuple[Fraction, ...]:
    """Normal [L/D] denominator with constant coefficient one, solved over Q."""
    L = numerator_degree
    D = denominator_degree
    assert L >= 0 and D >= 0 and L + D <= MAX_SERIES_DEGREE
    if D == 0:
        return (Fraction(1),)
    matrix = fmpq_mat(
        [
            [
                to_fmpq(F_COEFFICIENTS[row_degree - column])
                for column in range(1, D + 1)
            ]
            for row_degree in range(L + 1, L + D + 1)
        ]
    )
    target = fmpq_mat(
        [
            [to_fmpq(-F_COEFFICIENTS[row_degree])]
            for row_degree in range(L + 1, L + D + 1)
        ]
    )
    # ``solve`` is exact and raises if the square coefficient matrix is
    # singular.  Computing its rational determinant separately is redundant
    # and creates much larger intermediates at M=15.
    solution = matrix.solve(target)
    denominator = [Fraction(1)] + [
        from_fmpq(solution[index, 0]) for index in range(D)
    ]
    assert denominator[-1] != 0
    for row_degree in range(L + 1, L + D + 1):
        assert sum(
            denominator[column] * F_COEFFICIENTS[row_degree - column]
            for column in range(D + 1)
        ) == 0
    return tuple(denominator)


def primitive_integer_polynomial(values: tuple[Fraction, ...]) -> list[int]:
    denominator_lcm = 1
    for value in values:
        denominator_lcm = math.lcm(denominator_lcm, value.denominator)
    integers = [
        value.numerator * (denominator_lcm // value.denominator)
        for value in values
    ]
    content = 0
    for value in integers:
        content = math.gcd(content, abs(value))
    assert content > 0
    integers = [value // content for value in integers]
    if integers[0] < 0:
        integers = [-value for value in integers]
    assert integers[0] > 0
    assert math.gcd(*[abs(value) for value in integers]) == 1
    # Division by the positive constant reconstructs the q_0=1 vector.
    assert [Fraction(value, integers[0]) for value in integers] == list(values)
    return integers


def poly_multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return answer


def jet_matrix(diagonal: list[int], upper: list[int], block_size: int) -> fmpz_mat:
    """Matrix (4), using X=rev(diagonal), Y=y rev(upper)."""
    X = list(reversed(diagonal))
    Y = [0] + list(reversed(upper))
    polynomials = [
        poly_multiply(X, X),
        poly_multiply(X, Y),
        poly_multiply(Y, Y),
    ]
    size = 3 * block_size
    matrix = fmpz_mat(size, size)
    column = 0
    for polynomial in polynomials:
        for shift in range(block_size):
            for degree, coefficient in enumerate(polynomial):
                row = shift + degree
                if row < size:
                    matrix[row, column] = coefficient
            column += 1
    assert column == size
    return matrix


def integer_matrix_digest(matrix: fmpz_mat) -> str:
    row_count = matrix.nrows()
    column_count = matrix.ncols()
    digest = hashlib.sha256(f"{row_count},{column_count}\n".encode())
    for row in range(row_count):
        for column in range(column_count):
            digest.update(f"{int(matrix[row, column])}\n".encode())
    return digest.hexdigest()


def determinant_record(diagonal: list[int], upper: list[int], block_size: int) -> dict[str, object]:
    matrix = jet_matrix(diagonal, upper, block_size)
    determinant = int(matrix.det())
    assert determinant != 0
    determinant_text = str(determinant)
    return {
        "block_size": block_size,
        "matrix_dimension": matrix.nrows(),
        "matrix_sha256": integer_matrix_digest(matrix),
        "determinant": determinant_text,
        "determinant_sha256": sha256_bytes(determinant_text.encode()),
        "absolute_bit_length": abs(determinant).bit_length(),
        "sign": 1 if determinant > 0 else -1,
    }


def polynomial_record(L: int, D: int) -> tuple[list[int], dict[str, object]]:
    rational = pade_denominator(L, D)
    primitive = primitive_integer_polynomial(rational)
    return primitive, {
        "type": [L, D],
        "normalization": "primitive integer coefficients, constant coefficient positive",
        "primitive_coefficients_low_to_high": [str(value) for value in primitive],
        "primitive_coefficients_sha256": integer_list_digest(primitive),
        "normalized_rational_coefficients_low_to_high": [
            fraction_text(value) for value in rational
        ],
        "primitive_constant": str(primitive[0]),
        "degree_exact": len(primitive) - 1,
    }


def main() -> None:
    started = time.monotonic()
    assert SOURCE.exists()
    assert sha256_file(SOURCE) == SOURCE_SHA256
    source_audit = control_audit(SOURCE)
    script_audit = control_audit(Path(__file__))
    assert source_audit["clean"] and script_audit["clean"]

    needed_indices = sorted(set(WITNESS_M) | {value - 1 for value in WITNESS_M})
    primitive_pairs: dict[int, tuple[list[int], list[int]]] = {}
    polynomial_records: dict[str, object] = {}
    for M in needed_indices:
        diagonal, diagonal_record = polynomial_record(M, M)
        upper, upper_record = polynomial_record(M + 1, M)
        primitive_pairs[M] = (diagonal, upper)
        polynomial_records[str(M)] = {
            "diagonal": diagonal_record,
            "upper_adjacent": upper_record,
        }

    witnesses: list[dict[str, object]] = []
    observed_theta6_signs: list[int] = []
    quotient_signs: list[int] = []
    for M in WITNESS_M:
        theta6 = determinant_record(*primitive_pairs[M], 6)
        theta4_previous = determinant_record(*primitive_pairs[M - 1], 4)
        assert theta6["sign"] == EXPECTED_THETA6_SIGNS[M]
        assert theta4_previous["sign"] == 1

        theta6_integer = int(theta6["determinant"])
        theta4_integer = int(theta4_previous["determinant"])
        common = math.gcd(abs(theta6_integer), abs(theta4_integer))
        reduced_numerator = theta6_integer // common
        reduced_denominator = theta4_integer // common
        assert reduced_denominator > 0
        quotient_sign = 1 if reduced_numerator > 0 else -1
        assert quotient_sign == theta6["sign"]

        observed_theta6_signs.append(int(theta6["sign"]))
        quotient_signs.append(quotient_sign)
        witnesses.append(
            {
                "M": M,
                "theta6_at_M": theta6,
                "theta4_at_M_minus_1": theta4_previous,
                "reduced_condensation_quotient": {
                    "numerator": str(reduced_numerator),
                    "denominator": str(reduced_denominator),
                    "numerator_bit_length": abs(reduced_numerator).bit_length(),
                    "denominator_bit_length": reduced_denominator.bit_length(),
                    "sign": quotient_sign,
                    "sha256": sha256_bytes(
                        f"{reduced_numerator}/{reduced_denominator}".encode()
                    ),
                },
            }
        )

    assert observed_theta6_signs == [1, -1, -1, 1]
    assert quotient_signs == [1, -1, -1, 1]
    assert peak_rss_kib() < RSS_GUARD_KIB

    output = {
        "claim": {
            "kernel": "F(x)=1/(2*cosh(sqrt(x)))",
            "normalization": "Q_[L/D](0)=1, then independent positive primitive integer clearing",
            "witness_M": list(WITNESS_M),
            "theta6_signs": observed_theta6_signs,
            "theta4_previous_all_positive": True,
            "condensation_quotient_signs": quotient_signs,
            "fixed_sign_actual_kernel_representation_excluded": True,
            "sign_changing_prefactor_excluded": False,
            "all_parameter_nonvanishing_claimed": False,
            "e_plus_pi_implication_claimed": False,
        },
        "exact_reconstruction": {
            "series_max_degree": MAX_SERIES_DEGREE,
            "F_coefficients": [fraction_text(value) for value in F_COEFFICIENTS],
            "F_coefficients_sha256": sha256_bytes(
                "".join(f"{fraction_text(value)}\n" for value in F_COEFFICIENTS).encode()
            ),
            "pade_polynomials": polynomial_records,
            "witnesses": witnesses,
        },
        "reproducibility": {
            "arithmetic": "Python Fraction plus python-flint exact fmpq/fmpz matrices",
            "flint_version": flint_version,
            "python_version": sys.version.split()[0],
            "source_sha256": SOURCE_SHA256,
            "source_control_audit": source_audit,
            "script_control_audit": script_audit,
            "rss_guard_kib": RSS_GUARD_KIB,
            "floating_point_used": False,
            "stored_sign_oracle_used": False,
        },
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    elapsed = time.monotonic() - started
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(f"elapsed_seconds={elapsed:.6f}")
    print(f"peak_rss_kib={peak_rss_kib()}")


if __name__ == "__main__":
    main()
