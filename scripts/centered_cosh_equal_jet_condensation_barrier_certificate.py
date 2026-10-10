#!/usr/bin/env python3
"""Exact replay for the equal-jet condensation/contiguous-transfer barrier.

The all-parameter statements replayed here are algebraic identities proved in
the companion source.  The M <= 120 determinant scan is explicitly finite.
All scan arithmetic is over the prime field with p = 2^61 - 1; a nonzero
modular determinant certifies nonvanishing of the corresponding rational one.
"""

from __future__ import annotations

import hashlib
import json
import math
import resource
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp
from flint import __version__ as flint_version
from flint import fmpq, fmpq_mat, fmpz, nmod_mat


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/centered_cosh_equal_jet_condensation_barrier.md"
OUTPUT = ROOT / "results/centered_cosh_equal_jet_condensation_barrier_certificate.json"
OLD_SOURCE = ROOT / "sources/centered_cosh_unbalanced_coupled_parity_obstruction.md"
OLD_MANIFEST = ROOT / "results/centered_cosh_unbalanced_coupled_parity_hashes.sha256"

OLD_SOURCE_SHA256 = "3aea77c0901bcf1d1209ee57c18dec01cc2c15c37c454249a8bb45af9b91d52d"
OLD_MANIFEST_SHA256 = "985a4a111319321868b17e526f0ecf6e41896708a92fc1db2256402188b7580a"

PRIME = 2**61 - 1
GRID_MAX_M = 120
RSS_GUARD_KIB = 8 * 1024 * 1024


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def fraction_record(value: Fraction) -> dict[str, object]:
    encoded = f"{value.numerator}/{value.denominator}".encode()
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "sha256": sha256_bytes(encoded),
    }


def peak_rss_kib() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def secant_f_mod(limit: int, modulus: int) -> list[int]:
    """F(x)=1/(2 cosh(sqrt(x))) modulo modulus."""
    factorial = 1
    cosh_coefficients = [1]
    for degree in range(1, limit + 1):
        factorial = factorial * (2 * degree - 1) % modulus
        factorial = factorial * (2 * degree) % modulus
        cosh_coefficients.append(pow(factorial, -1, modulus))
    coefficients = [pow(2, -1, modulus)]
    for degree in range(1, limit + 1):
        coefficients.append(
            -sum(
                cosh_coefficients[index] * coefficients[degree - index]
                for index in range(1, degree + 1)
            )
            % modulus
        )
    return coefficients


def secant_f_fraction(limit: int) -> list[Fraction]:
    coefficients = [Fraction(1, 2)]
    for degree in range(1, limit + 1):
        coefficients.append(
            -sum(
                Fraction(1, math.factorial(2 * index))
                * coefficients[degree - index]
                for index in range(1, degree + 1)
            )
        )
    return coefficients


def pade_mod(
    numerator_degree: int,
    denominator_degree: int,
    coefficients: list[int],
    modulus: int,
) -> list[int]:
    if denominator_degree == 0:
        return [1]
    left = nmod_mat(
        [
            [
                coefficients[row_degree - column] % modulus
                for column in range(1, denominator_degree + 1)
            ]
            for row_degree in range(
                numerator_degree + 1,
                numerator_degree + denominator_degree + 1,
            )
        ],
        modulus,
    )
    right = nmod_mat(
        [
            [(-coefficients[row_degree]) % modulus]
            for row_degree in range(
                numerator_degree + 1,
                numerator_degree + denominator_degree + 1,
            )
        ],
        modulus,
    )
    assert int(left.det()) != 0
    solution = left.solve(right)
    answer = [1] + [int(solution[index, 0]) for index in range(denominator_degree)]
    assert answer[-1] != 0
    for row_degree in range(
        numerator_degree + 1,
        numerator_degree + denominator_degree + 1,
    ):
        assert sum(
            answer[column] * coefficients[row_degree - column]
            for column in range(denominator_degree + 1)
        ) % modulus == 0
    return answer


def pade_fraction(
    numerator_degree: int,
    denominator_degree: int,
    coefficients: list[Fraction],
) -> list[Fraction]:
    if denominator_degree == 0:
        return [Fraction(1)]
    left = fmpq_mat(
        [
            [
                fmpq(
                    coefficients[row_degree - column].numerator,
                    coefficients[row_degree - column].denominator,
                )
                for column in range(1, denominator_degree + 1)
            ]
            for row_degree in range(
                numerator_degree + 1,
                numerator_degree + denominator_degree + 1,
            )
        ]
    )
    right = fmpq_mat(
        [
            [
                fmpq(
                    -coefficients[row_degree].numerator,
                    coefficients[row_degree].denominator,
                )
            ]
            for row_degree in range(
                numerator_degree + 1,
                numerator_degree + denominator_degree + 1,
            )
        ]
    )
    solution = left.solve(right)
    answer = [Fraction(1)]
    for index in range(denominator_degree):
        entry = solution[index, 0]
        answer.append(Fraction(int(entry.numerator), int(entry.denominator)))
    assert answer[-1] != 0
    return answer


def poly_multiply_mod(left: list[int], right: list[int], modulus: int) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] = (
                answer[left_index + right_index] + left_value * right_value
            ) % modulus
    return answer


def poly_multiply_fraction(
    left: list[Fraction], right: list[Fraction]
) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return answer


def poly_series_inverse(values: list[Fraction], limit: int) -> list[Fraction]:
    assert values[0] != 0
    answer = [Fraction(0)] * limit
    answer[0] = 1 / values[0]
    for degree in range(1, limit):
        answer[degree] = -sum(
            values[index] * answer[degree - index]
            for index in range(1, min(degree, len(values) - 1) + 1)
        ) / values[0]
    return answer


def poly_series_quotient(
    numerator: list[Fraction], denominator: list[Fraction], limit: int
) -> list[Fraction]:
    inverse = poly_series_inverse(denominator, limit)
    product = poly_multiply_fraction(numerator, inverse)
    return (product + [Fraction(0)] * limit)[:limit]


def jet_det_mod(
    polynomials: list[list[int]], counts: tuple[int, int, int], modulus: int
) -> int:
    size = sum(counts)
    matrix = nmod_mat(size, size, modulus)
    column = 0
    for polynomial, count in zip(polynomials, counts):
        for shift in range(count):
            last_row = min(size, shift + len(polynomial))
            for row in range(shift, last_row):
                matrix[row, column] = polynomial[row - shift]
            column += 1
    assert column == size
    return int(matrix.det())


def scan_equal_jets() -> dict[str, object]:
    assert fmpz(PRIME).is_prime()
    coefficients = secant_f_mod(2 * GRID_MAX_M + 2, PRIME)
    diagonal: dict[int, list[int]] = {}
    upper: dict[int, list[int]] = {}
    for degree in range(GRID_MAX_M + 1):
        diagonal[degree] = pade_mod(degree, degree, coefficients, PRIME)
        upper[degree] = pade_mod(degree + 1, degree, coefficients, PRIME)

    digest = hashlib.sha256()
    sigma_one_count = 0
    sigma_zero_count = 0
    per_m: list[dict[str, object]] = []
    transfer_checks = 0

    for degree in range(1, GRID_MAX_M + 1):
        c_value = diagonal[degree]
        b_value = upper[degree]
        b_previous = upper[degree - 1]
        c_previous = diagonal[degree - 1]
        beta = (b_value[1] - c_value[1]) % PRIME
        alpha = (c_value[1] - (b_previous[1] if degree > 1 else 0)) % PRIME
        assert alpha != 0 and beta != 0
        for index in range(degree + 1):
            assert (
                b_value[index]
                - c_value[index]
                - (beta * b_previous[index - 1] if index >= 1 else 0)
            ) % PRIME == 0
            assert (
                c_value[index]
                - (b_previous[index] if index < len(b_previous) else 0)
                - (alpha * c_previous[index - 1] if index >= 1 else 0)
            ) % PRIME == 0
        transfer_checks += 2

        x_value = list(reversed(c_value))
        y_value = [0] + list(reversed(b_value))
        y_previous = [0] + list(reversed(b_previous))

        equal_polynomials = [
            poly_multiply_mod(x_value, x_value, PRIME),
            poly_multiply_mod(x_value, y_value, PRIME),
            poly_multiply_mod(y_value, y_value, PRIME),
        ]
        flagged_polynomials = [
            poly_multiply_mod(x_value, x_value, PRIME),
            poly_multiply_mod(x_value, y_previous, PRIME),
            poly_multiply_mod(y_previous, y_previous, PRIME),
        ]

        row_sigma_one = 0
        row_sigma_zero = 0
        for multiplier_count in range(2, degree + 1, 2):
            residue = jet_det_mod(
                equal_polynomials,
                (multiplier_count, multiplier_count, multiplier_count),
                PRIME,
            )
            assert residue != 0
            digest.update(
                f"1,{degree},{multiplier_count},{residue}\n".encode()
            )
            sigma_one_count += 1
            row_sigma_one += 1
        for multiplier_count in range(2, degree - 1, 2):
            residue = jet_det_mod(
                flagged_polynomials,
                (
                    multiplier_count + 2,
                    multiplier_count + 1,
                    multiplier_count,
                ),
                PRIME,
            )
            assert residue != 0
            digest.update(
                f"0,{degree},{multiplier_count},{residue}\n".encode()
            )
            sigma_zero_count += 1
            row_sigma_zero += 1
        per_m.append(
            {
                "M": degree,
                "sigma_1_count": row_sigma_one,
                "sigma_0_count": row_sigma_zero,
            }
        )

    assert sigma_one_count == 3600
    assert sigma_zero_count == 3481
    assert sigma_one_count + sigma_zero_count == 7081
    return {
        "field_prime": str(PRIME),
        "M_max": GRID_MAX_M,
        "sigma_1_nonzero_count": sigma_one_count,
        "sigma_0_nonzero_count": sigma_zero_count,
        "total_nonzero_count": sigma_one_count + sigma_zero_count,
        "all_determinants_nonzero_mod_prime": True,
        "determinant_stream_sha256": digest.hexdigest(),
        "transfer_polynomial_checks": transfer_checks,
        "per_M_counts": per_m,
        "scope": "finite exact certificate only; no all-M extrapolation",
    }


def exact_contiguous_checks() -> dict[str, object]:
    coefficients = secant_f_fraction(20)
    rows = []
    for degree in range(2, 9):
        a_poly = pade_fraction(degree, degree + 1, coefficients)
        b_poly = pade_fraction(degree + 1, degree, coefficients)
        c_poly = pade_fraction(degree, degree, coefficients)
        b_previous = pade_fraction(degree, degree - 1, coefficients)
        c_previous = pade_fraction(degree - 1, degree - 1, coefficients)
        r_poly = pade_fraction(degree + 1, degree - 1, coefficients)
        c_scalar = a_poly[1] - b_poly[1]
        b_scalar = b_poly[1] - c_poly[1]
        a_scalar = c_poly[1] - (
            b_previous[1] if len(b_previous) > 1 else Fraction(0)
        )
        d_scalar = c_poly[1] - (
            r_poly[1] if len(r_poly) > 1 else Fraction(0)
        )
        assert all(value != 0 for value in (a_scalar, b_scalar, c_scalar, d_scalar))

        def coefficient(values: list[Fraction], index: int) -> Fraction:
            return values[index] if index < len(values) else Fraction(0)

        for index in range(degree + 2):
            assert coefficient(a_poly, index) - coefficient(b_poly, index) == (
                c_scalar * coefficient(c_poly, index - 1)
                if index >= 1
                else 0
            )
        for index in range(degree + 1):
            assert coefficient(b_poly, index) - coefficient(c_poly, index) == (
                b_scalar * coefficient(b_previous, index - 1)
                if index >= 1
                else 0
            )
            assert coefficient(c_poly, index) - coefficient(b_previous, index) == (
                a_scalar * coefficient(c_previous, index - 1)
                if index >= 1
                else 0
            )
            assert coefficient(c_poly, index) - coefficient(r_poly, index) == (
                d_scalar * coefficient(b_previous, index - 1)
                if index >= 1
                else 0
            )
        rows.append(
            {
                "M": degree,
                "a_M": fraction_record(a_scalar),
                "b_M": fraction_record(b_scalar),
                "c_M": fraction_record(c_scalar),
                "d_M": fraction_record(d_scalar),
                "four_identities_verified": True,
                "transfer_determinant_nonzero": a_scalar * b_scalar != 0,
            }
        )
    return {"rows": rows, "all_exact": True}


def coefficient_det_fraction(columns: list[list[Fraction]], size: int) -> Fraction:
    matrix = fmpq_mat(
        [
            [
                fmpq(
                    (column[row] if row < len(column) else Fraction(0)).numerator,
                    (column[row] if row < len(column) else Fraction(0)).denominator,
                )
                for column in columns
            ]
            for row in range(size)
        ]
    )
    determinant = matrix.det()
    return Fraction(int(determinant.numerator), int(determinant.denominator))


def two_block_minor(
    k_values: list[Fraction],
    ell_values: list[Fraction],
    p_count: int,
    q_count: int,
    shift: int,
) -> Fraction:
    size = p_count + q_count
    columns: list[list[Fraction]] = []
    for values, count in ((k_values, p_count), (ell_values, q_count)):
        for column_shift in range(count):
            column = []
            for row in range(size):
                index = shift + row - column_shift
                column.append(values[index] if 0 <= index < len(values) else Fraction(0))
            columns.append(column)
    return coefficient_det_fraction(columns, size)


def desnanot_and_sign_checks() -> dict[str, object]:
    k_symbols = sp.symbols("k1:7")
    k_values = [sp.Integer(0)] + list(k_symbols)
    ell_values = [sp.Integer(0)] * 7
    for degree in range(2, 7):
        ell_values[degree] = sum(
            k_values[index] * k_values[degree - index]
            for index in range(1, degree)
        )

    def symbolic_minor(p_count: int, q_count: int, shift: int) -> sp.Expr:
        size = p_count + q_count
        matrix = []
        for row in range(size):
            matrix.append(
                [
                    k_values[shift + row - column]
                    if 0 <= shift + row - column < len(k_values)
                    else 0
                    for column in range(p_count)
                ]
                + [
                    ell_values[shift + row - column]
                    if 0 <= shift + row - column < len(ell_values)
                    else 0
                    for column in range(q_count)
                ]
            )
        return sp.expand(sp.Matrix(matrix).det())

    symbolic_terms = {
        "D_2_2_shift_2": symbolic_minor(2, 2, 2),
        "D_1_1_shift_3": symbolic_minor(1, 1, 3),
        "D_1_2_shift_3": symbolic_minor(1, 2, 3),
        "D_2_1_shift_2": symbolic_minor(2, 1, 2),
        "D_2_1_shift_3": symbolic_minor(2, 1, 3),
        "D_1_2_shift_2": symbolic_minor(1, 2, 2),
    }
    assert sp.expand(
        symbolic_terms["D_2_2_shift_2"] * symbolic_terms["D_1_1_shift_3"]
        - symbolic_terms["D_1_2_shift_3"] * symbolic_terms["D_2_1_shift_2"]
        + symbolic_terms["D_2_1_shift_3"] * symbolic_terms["D_1_2_shift_2"]
    ) == 0

    coefficients = secant_f_fraction(20)
    sign_rows = []
    keys = [(2, 2, 2), (1, 1, 3), (1, 2, 3), (2, 1, 2), (2, 1, 3), (1, 2, 2)]
    for degree in (2, 5):
        # Use the actual sigma=1 quotient y*rev(Q_[M+1/M]) /
        # rev(Q_[M/M+1]); off-diagonal minors are not invariant under the
        # constant projective change to the canonical (X_M,Y_M) pair.
        x_value = list(
            reversed(pade_fraction(degree, degree + 1, coefficients))
        )
        y_value = [Fraction(0)] + list(
            reversed(pade_fraction(degree + 1, degree, coefficients))
        )
        k_series = poly_series_quotient(y_value, x_value, 8)
        ell_series = (poly_multiply_fraction(k_series, k_series) + [Fraction(0)] * 8)[:8]
        values = [two_block_minor(k_series, ell_series, *key) for key in keys]
        signs = "".join("+" if value > 0 else "-" if value < 0 else "0" for value in values)
        sign_rows.append(
            {
                "M": degree,
                "ordered_keys": [list(key) for key in keys],
                "signs": signs,
                "value_sha256": sha256_bytes(
                    "\n".join(
                        f"{value.numerator}/{value.denominator}" for value in values
                    ).encode()
                ),
            }
        )
    assert sign_rows[0]["signs"] == "++++--"
    assert sign_rows[1]["signs"] == "+++-+-"
    return {
        "m_equals_2_symbolic_desnanot_verified": True,
        "symbolic_term_sha256": {
            key: sha256_bytes(str(sp.factor(value)).encode())
            for key, value in symbolic_terms.items()
        },
        "genuine_secant_off_diagonal_sign_rows": sign_rows,
        "sign_change_present": True,
    }


def flagged_basis_change_checks() -> dict[str, object]:
    b_symbol = sp.symbols("b")
    rows = []
    for multiplier_count in range(1, 7):
        m_value = multiplier_count
        standard_labels = (
            [(0, shift) for shift in range(m_value + 2)]
            + [(1, shift) for shift in range(m_value + 1)]
            + [(2, shift) for shift in range(m_value)]
        )
        index = {label: position for position, label in enumerate(standard_labels)}
        size = 3 * m_value + 3
        matrix = sp.zeros(size, size)
        column = 0
        for shift in range(m_value):
            matrix[index[(0, shift)], column] = 1
            column += 1
        for shift in range(m_value):
            matrix[index[(0, shift + 1)], column] = 1
            matrix[index[(1, shift)], column] = b_symbol
            column += 1
        for shift in range(m_value):
            matrix[index[(0, shift + 2)], column] = 1
            matrix[index[(1, shift + 1)], column] = 2 * b_symbol
            matrix[index[(2, shift)], column] = b_symbol**2
            column += 1
        for label in ((0, m_value), (0, m_value + 1), (1, m_value)):
            matrix[index[label], column] = 1
            column += 1
        assert column == size
        determinant = sp.factor(matrix.det())
        assert determinant in (b_symbol ** (3 * m_value), -b_symbol ** (3 * m_value))
        rows.append(
            {
                "m": m_value,
                "determinant": str(determinant),
                "absolute_formula_verified": True,
            }
        )
    return {"rows": rows, "all_exact": True}


def positive_node_counterexample() -> dict[str, object]:
    y_symbol, t_symbol = sp.symbols("y t")
    k_rational = y_symbol * (
        1 / (1 - y_symbol)
        + 1 / (1 - 2 * y_symbol)
        + t_symbol / (1 - 3 * y_symbol)
    )
    k_truncated = sp.series(k_rational, y_symbol, 0, 7).removeO().expand()
    columns = [
        sp.expand(y_symbol**shift * value)
        for value in (sp.Integer(1), k_truncated, sp.expand(k_truncated**2))
        for shift in range(2)
    ]
    matrix = sp.Matrix(
        [
            [column.coeff(y_symbol, row) for column in columns]
            for row in range(6)
        ]
    )
    determinant = sp.factor(matrix.det())
    expected = (4 * t_symbol - 1) * (
        t_symbol**3 - 25 * t_symbol**2 - 13 * t_symbol + 1
    )
    assert sp.expand(determinant - expected) == 0

    special = sp.factor(k_rational.subs(t_symbol, sp.Rational(1, 4)))
    combination = sp.factor(
        -sp.Rational(729, 16) * y_symbol
        + (sp.Rational(81, 4) - 27 * y_symbol) * special
        + (y_symbol - 3) * special**2
    )
    expected_combination = -y_symbol**6 * (11 * y_symbol - 3) / (
        (y_symbol - 1) ** 2
        * (2 * y_symbol - 1) ** 2
        * (3 * y_symbol - 1) ** 2
    )
    assert sp.factor(combination - expected_combination) == 0
    numerator = -y_symbol * (38 * y_symbol**2 - 39 * y_symbol + 9)
    denominator = 4 * (y_symbol - 1) * (2 * y_symbol - 1) * (3 * y_symbol - 1)
    assert sp.factor(special - numerator / denominator) == 0
    assert sp.gcd(numerator, denominator) == 1
    resultant = sp.resultant(numerator, denominator, y_symbol)
    assert resultant == -4096
    return {
        "parameter_determinant": str(determinant),
        "rational_zero_parameter": "1/4",
        "explicit_order_six_relation_verified": True,
        "coprime_numerator_denominator": True,
        "ordinary_resultant": str(resultant),
        "positive_nodes": [1, 2, 3],
        "positive_weights": ["1", "1", "1/4"],
        "logical_scope": "generic barrier; not a secant counterexample",
    }


def source_control_audit() -> dict[str, object]:
    source_text = SOURCE.read_text()
    required = [
        "finite grid",
        "not extrapolated",
        "still needed",
        "No conclusion about \\(e+\\pi\\) follows",
    ]
    for phrase in required:
        assert phrase in source_text
    return {"required_scope_phrases_present": required}


def main() -> None:
    started = time.perf_counter()
    assert sha256_file(OLD_SOURCE) == OLD_SOURCE_SHA256
    assert sha256_file(OLD_MANIFEST) == OLD_MANIFEST_SHA256
    dependency_checks = {
        str(OLD_SOURCE.relative_to(ROOT)): OLD_SOURCE_SHA256,
        str(OLD_MANIFEST.relative_to(ROOT)): OLD_MANIFEST_SHA256,
    }

    payload = {
        "schema": "centered-cosh-equal-jet-condensation-barrier-v1",
        "assertions": {
            "cleared_equal_and_flagged_jet_formulas": True,
            "four_contiguous_pade_identities": True,
            "degree_one_transfer_has_constant_nonzero_determinant": True,
            "full_step_leaves_six_boundary_dimensions": True,
            "equal_jet_is_codimension_three_in_flagged_jet": True,
            "desnanot_lattice_does_not_close_on_equal_diagonal": True,
            "positive_node_coprime_counterexample_at_m_2": True,
            "all_parameter_secant_nonvanishing_proved": False,
        },
        "finite_scan": scan_equal_jets(),
        "exact_contiguous_checks": exact_contiguous_checks(),
        "desnanot_and_sign_checks": desnanot_and_sign_checks(),
        "flagged_basis_change": flagged_basis_change_checks(),
        "positive_node_counterexample": positive_node_counterexample(),
        "dependency_checks": dependency_checks,
        "source_sha256": sha256_file(SOURCE),
        "source_control_audit": source_control_audit(),
        "logical_scope": {
            "proved": (
                "the algebraic transfer, nesting, condensation identities, "
                "and the explicit generic positive-node counterexample"
            ),
            "finite_only": "both secant equal-jet grids through M=120",
            "not_proved": (
                "all-parameter nonvanishing of either special secant jet, "
                "or any arithmetic conclusion about e+pi"
            ),
        },
        "software": {
            "python_flint": flint_version,
            "sympy": sp.__version__,
        },
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "failure guard only; it does not allocate or cap the roughly "
                "50 GiB available Colab RAM"
            ),
            "hardware_accelerator": (
                "not used: exact finite-field and rational determinants use "
                "CPU integer arithmetic rather than floating-point GPU kernels"
            ),
        },
    }

    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_GUARD_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUTPUT}")
    print(f"sha256 {sha256_bytes(encoded)}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
