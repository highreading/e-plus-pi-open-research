#!/usr/bin/env python3
"""Deterministic exact replay for Item 381.

Checks predeclared binary discriminant/norm cases, the exact ternary
reciprocal coefficient table, the normalized Newton stability identity,
singleton separation controls, definite matrices, and live conic examples.
No actual target or prime census is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "results/item316_beta_intermediate_ostrowski_no_go_certificate.json": (
        "5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "manifests/item316_beta_intermediate_ostrowski_no_go_manifest.json": (
        "aac741658430fb661de078adfeafdbc3a9d20312a8fd8725cb4244d406d9bcf6"
    ),
    "sources/item358_beta_actual_low_incidence_saturation_barrier_report.md": (
        "681c9f9cbe926978c78f632084c8be83439c2ac3f5e50f2c2697a49f2f0da68d"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_certificate.json": (
        "4da88e55dec36f3c130def549007c8ae1509ff0a029dfed9ff25f67a78c2ffa3"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_root_audit.json": (
        "a1a48f7d7080834ebf3be56b47d8056733e88e1913e8f6ea784f97a5eb2d9172"
    ),
    "manifests/item358_beta_actual_low_incidence_saturation_barrier_manifest.json": (
        "4ba799fe2fc8cb6063034d844f91bcaec6c3fc84d043b1f46c675fce400acfb1"
    ),
    "sources/item373_beta_symmetric_singleton_first_quotient_report.md": (
        "daa16600359a52501fcbe303359e39696c1f0b0acfdb62b944b19be77784d6c5"
    ),
    "scripts/item373_beta_symmetric_singleton_first_quotient_certificate.py": (
        "8158fd3e100c1a7abb5efa0048a979a6e368e7328ae67743731041b756944bcf"
    ),
    "results/item373_beta_symmetric_singleton_first_quotient_certificate.json": (
        "335be8c519597bc1fd1a6e21cb9bbbbe37b1785a2468e4f0a7d6c205a9cb2cc5"
    ),
    "results/item373_beta_symmetric_singleton_first_quotient_ledger_delta.json": (
        "6d2193aecb20165fd44082c5e0a2959756e7f62bbac7e35efd6ac5be76b28a39"
    ),
    "results/item373_beta_symmetric_singleton_first_quotient_root_audit.json": (
        "3b5d6b13fdd327e27b518744edd2666cc58895fb401f7050ad52046810bb1128"
    ),
    "manifests/item373_beta_symmetric_singleton_first_quotient_manifest.json": (
        "a42cd4b5e306b5fe864e4832e11726380d9bf4197868884f1879dc98b91aeacf"
    ),
    "sources/item375_beta_symmetric_content_primitive_no_go_report.md": (
        "4acda264afe6fa40431d041fbbbc3634eeb0ec1395a35b682611764f5c92fb12"
    ),
    "scripts/item375_beta_symmetric_content_primitive_no_go_certificate.py": (
        "ab42775d9d854c1b62fe25e5aa929b00f7c8f07b1c04331a56b111c5b3d996b9"
    ),
    "results/item375_beta_symmetric_content_primitive_no_go_certificate.json": (
        "e96a358a761bf3f83ae791ebcc83756feb17725fd68ba58d611b00800f3ff6d3"
    ),
    "results/item375_beta_symmetric_content_primitive_no_go_ledger_delta.json": (
        "d0cc6de271dcf31adb0ec605d824410f0320b89a9ddcfd4f722a22d3d19adbf5"
    ),
    "results/item375_beta_symmetric_content_primitive_no_go_root_audit.json": (
        "8e0a605818fd7779552c9c196fb00584c9a8d58937d6b40063f9e6b6cad7e5d9"
    ),
    "manifests/item375_beta_symmetric_content_primitive_no_go_manifest.json": (
        "79db075b1c5cab090fa942c8bacb4dd0e7ea80eace9cc26c7f4e4cf91ce42621"
    ),
    "sources/item378_beta_top_symmetric_multivariate_cancellation_report.md": (
        "2b3ccd3123e2be2964c50cbcc5a4efae373a1831ba8adc821e3b328bcc4a35fc"
    ),
    "scripts/item378_beta_top_symmetric_multivariate_cancellation_certificate.py": (
        "59e18be6f61e7b9a1a25565f8794ea0e8fca3aa522979b8891dd4b54467a639e"
    ),
    "results/item378_beta_top_symmetric_multivariate_cancellation_certificate.json": (
        "a894df120ed27c83c589dfd0a4c48a7ce66b8c6521772b861e3c264fd75107c8"
    ),
    "results/item378_beta_top_symmetric_multivariate_cancellation_ledger_delta.json": (
        "79d2b0ad602ef827f623739b5330b91379d750acbdf8c595fe4d80e0d4392d90"
    ),
    "results/item378_beta_top_symmetric_multivariate_cancellation_root_audit.json": (
        "37e706b6e096aef885fafeafe1594a8c00f8c15d6eb3dbf85d7c2f152bfc2d60"
    ),
    "manifests/item378_beta_top_symmetric_multivariate_cancellation_manifest.json": (
        "4a574ac75c61fd1eae7f0539f11fcee07a6713e834bba095f2e26b4148f548aa"
    ),
}


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    root = Path(__file__).resolve().parent.parent
    rows = []
    for relative_path, expected in DEPENDENCY_HASHES.items():
        payload = (root / relative_path).read_bytes()
        actual = hashlib.sha256(payload).hexdigest()
        assert actual == expected, (relative_path, actual, expected)
        rows.append(
            {"path": relative_path, "bytes": len(payload), "sha256": actual}
        )
    return {"count": len(rows), "rows": rows, "rows_digest": digest(rows)}


def clean(poly: Polynomial) -> Polynomial:
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + coefficient
    return clean(result)


def scale(poly: Polynomial, scalar: int) -> Polynomial:
    return clean({exponent: scalar * coefficient for exponent, coefficient in poly.items()})


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    assert left and right
    result: Polynomial = {}
    for left_exp, left_coefficient in left.items():
        for right_exp, right_coefficient in right.items():
            exponent = tuple(a + b for a, b in zip(left_exp, right_exp))
            result[exponent] = result.get(exponent, 0) + left_coefficient * right_coefficient
    return clean(result)


def evaluate(poly: Polynomial, values: list[Any]) -> Any:
    return sum(
        coefficient * math.prod(value**power for value, power in zip(values, exponent))
        for exponent, coefficient in poly.items()
    )


def elementary(values: list[Any], degree: int) -> Any:
    if degree == 0:
        return 1
    return sum(
        (math.prod(values[index] for index in subset) for subset in itertools.combinations(range(len(values)), degree)),
        start=0,
    )


def elementary_polynomial(variable_count: int, degree: int) -> Polynomial:
    if degree == 0:
        return {(0,) * variable_count: 1}
    return {
        tuple(int(index in subset) for index in range(variable_count)): 1
        for subset in itertools.combinations(range(variable_count), degree)
    }


def top_coordinates(loads: list[int], count: int) -> list[int]:
    size = len(loads)
    return [elementary(loads, size - s_value) for s_value in range(1, count + 1)]


def partition_type(exponent: Exponent) -> tuple[int, ...]:
    return tuple(sorted((value for value in exponent if value), reverse=True))


def determinant_3(matrix: list[list[int]]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def binary_quadratic(a: int, b: int, c: int, x_value: int, y_value: int) -> int:
    return a * x_value**2 + b * x_value * y_value + c * y_value**2


def binary_controls() -> dict[str, Any]:
    rows = []
    definite_forms = [(2, 1, 3), (-3, -2, -5)]
    for a, b, c in definite_forms:
        discriminant = b * b - 4 * a * c
        assert discriminant < 0
        sign = 1 if a > 0 else -1
        aa, bb, cc = sign * a, sign * b, sign * c
        for x_value, y_value in [(13, 11), (101, 73), (1009, 997)]:
            q_value = binary_quadratic(aa, bb, cc, x_value, y_value)
            identity = (2 * aa * x_value + bb * y_value) ** 2 + (4 * aa * cc - bb * bb) * y_value**2
            assert 4 * aa * q_value == identity
            assert q_value * 4 * aa >= y_value**2
        rows.append(
            {
                "class": "definite",
                "coefficients": [a, b, c],
                "discriminant": discriminant,
            }
        )

    split = (1, 0, -4)
    split_discriminant = split[1] ** 2 - 4 * split[0] * split[2]
    assert split_discriminant == 16
    for x_value, y_value in [(2, 1), (10, 5), (22, 11)]:
        assert binary_quadratic(*split, x_value, y_value) == 0
    rows.append(
        {
            "class": "rational_split_positive_line",
            "coefficients": list(split),
            "discriminant": split_discriminant,
            "positive_line": "X=2Y",
        }
    )

    pell_pairs = [(3, 2), (17, 12), (99, 70), (577, 408)]
    pell_rows = []
    for q_value, r_value in pell_pairs:
        assert math.gcd(q_value, r_value) == 1
        norm = q_value**2 - 2 * r_value**2
        assert norm == 1
        for scalar in [1, 7, 23]:
            scaled = binary_quadratic(1, 0, -2, scalar * q_value, scalar * r_value)
            assert scaled == scalar**2
        pell_rows.append(
            {"q": q_value, "r": r_value, "primitive_norm": norm}
        )
    rows.append(
        {
            "class": "irreducible_indefinite_Pell_small",
            "coefficients": [1, 0, -2],
            "discriminant": 8,
            "pell_rows": pell_rows,
        }
    )
    return {"rows": rows, "rows_digest": digest(rows)}


def reciprocal_coefficient_table_controls() -> dict[str, Any]:
    variable_count = 4
    e1 = elementary_polynomial(variable_count, 1)
    e2 = elementary_polynomial(variable_count, 2)
    e3 = elementary_polynomial(variable_count, 3)
    e1e3 = multiply(e1, e3)
    e2sq = multiply(e2, e2)

    def type_coefficients(poly: Polynomial) -> dict[str, int]:
        grouped: dict[tuple[int, ...], set[int]] = {}
        for exponent, coefficient in poly.items():
            grouped.setdefault(partition_type(exponent), set()).add(coefficient)
        assert all(len(values) == 1 for values in grouped.values())
        return {str(key): next(iter(values)) for key, values in sorted(grouped.items())}

    e1e3_table = type_coefficients(e1e3)
    e2sq_table = type_coefficients(e2sq)
    assert e1e3_table == {"(1, 1, 1, 1)": 4, "(2, 1, 1)": 1}
    assert e2sq_table == {"(1, 1, 1, 1)": 6, "(2, 1, 1)": 2, "(2, 2)": 1}

    cd_rows = []
    for c_value in range(-6, 7):
        for d_value in range(-6, 7):
            combined = add(scale(e1e3, c_value), scale(e2sq, d_value))
            coefficients = list(combined.values())
            nonnegative = bool(combined) and all(value >= 0 for value in coefficients)
            predicted = d_value >= 0 and 2 * c_value + 3 * d_value >= 0 and (c_value != 0 or d_value != 0)
            assert nonnegative == predicted
            nonpositive = bool(combined) and all(value <= 0 for value in coefficients)
            predicted_negative = d_value <= 0 and 2 * c_value + 3 * d_value <= 0 and (c_value != 0 or d_value != 0)
            assert nonpositive == predicted_negative
            cd_rows.append(
                {
                    "c": c_value,
                    "d": d_value,
                    "nonnegative": nonnegative,
                    "nonpositive": nonpositive,
                }
            )
    return {
        "e1e3_type_coefficients": e1e3_table,
        "e2_squared_type_coefficients": e2sq_table,
        "cd_rows_checked": len(cd_rows),
        "cd_rows_digest": digest(cd_rows),
    }


def newton_stability_controls() -> dict[str, Any]:
    identity_rows = []
    for variable_count in range(3, 8):
        e1 = elementary_polynomial(variable_count, 1)
        e2 = elementary_polynomial(variable_count, 2)
        e3 = elementary_polynomial(variable_count, 3)
        left = add(
            scale(multiply(e2, e2), 2 * (variable_count - 2)),
            scale(multiply(e1, e3), -3 * (variable_count - 1)),
        )
        right: Polynomial = {}
        for i_value in range(variable_count):
            for j_value in range(i_value + 1, variable_count):
                difference: Polynomial = {
                    tuple(int(index == i_value) for index in range(variable_count)): 1,
                    tuple(int(index == j_value) for index in range(variable_count)): -1,
                }
                difference_squared = multiply(difference, difference)
                outside = [index for index in range(variable_count) if index not in (i_value, j_value)]
                outside_e1: Polynomial = {
                    tuple(int(index == outside_index) for index in range(variable_count)): 1
                    for outside_index in outside
                }
                outside_e2: Polynomial = {
                    tuple(int(index in subset) for index in range(variable_count)): 1
                    for subset in itertools.combinations(outside, 2)
                }
                kernel = add(multiply(outside_e1, outside_e1), scale(outside_e2, -1))
                right = add(right, multiply(difference_squared, kernel))
        assert left == right
        identity_rows.append(
            {
                "N": variable_count,
                "terms": len(left),
                "identity_digest": digest(sorted((list(key), value) for key, value in left.items())),
            }
        )

    capital_A = 20
    loads = [46, 87, 217, 74, 5, 11]
    reciprocals = [Fraction(1, load) for load in loads]
    count = len(loads)
    e1_value = elementary(reciprocals, 1)
    e2_value = elementary(reciprocals, 2)
    e3_value = elementary(reciprocals, 3)
    left_value = 2 * (count - 2) * e2_value**2 - 3 * (count - 1) * e1_value * e3_value
    right_value = Fraction(0, 1)
    for i_value in range(count):
        for j_value in range(i_value + 1, count):
            outside_values = [
                reciprocals[index]
                for index in range(count)
                if index not in (i_value, j_value)
            ]
            kernel_value = elementary(outside_values, 1) ** 2 - elementary(outside_values, 2)
            right_value += (reciprocals[i_value] - reciprocals[j_value]) ** 2 * kernel_value
    assert left_value == right_value
    assert left_value > Fraction(1, capital_A**12)

    product = math.prod(loads)
    coordinates = top_coordinates(loads, 3)
    gap_value = 2 * (count - 2) * coordinates[1] ** 2 - 3 * (count - 1) * coordinates[0] * coordinates[2]
    assert Fraction(gap_value, product**2) == left_value
    normalized = Fraction(gap_value, coordinates[0] ** 2)
    assert normalized > Fraction(1, capital_A**12 * count**2)
    return {
        "identity_rows": identity_rows,
        "identity_rows_digest": digest(identity_rows),
        "actual_algebra_control": {
            "capital_A": capital_A,
            "loads": loads,
            "coordinates": coordinates,
            "gap_value": gap_value,
            "normalized_gap": str(normalized),
            "declared_lower": str(Fraction(1, capital_A**12 * count**2)),
        },
    }


def definite_and_live_ternary_controls() -> dict[str, Any]:
    definite_rows = []
    matrices = [
        [[4, 1, 0], [1, 6, 1], [0, 1, 8]],
        [[6, -1, 1], [-1, 8, 0], [1, 0, 10]],
    ]
    for matrix in matrices:
        determinant = determinant_3(matrix)
        minor_1 = matrix[0][0]
        minor_2 = matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2
        assert minor_1 > 0 and minor_2 > 0 and determinant > 0
        definite_rows.append(
            {
                "matrix": matrix,
                "principal_minors": [minor_1, minor_2, determinant],
            }
        )

    loads = [1, 1, 2, 2]
    coordinates = top_coordinates(loads, 3)
    assert coordinates == [12, 13, 6]
    T1, T2, T3 = coordinates
    conic_value = 169 * T1 * T3 - 72 * T2**2
    assert conic_value == 0
    conic_matrix = [[0, 0, 169], [0, -144, 0], [169, 0, 0]]
    conic_determinant = determinant_3(conic_matrix)
    assert conic_determinant != 0
    newton_gap = 2 * (len(loads) - 2) * T2**2 - 3 * (len(loads) - 1) * T1 * T3
    assert newton_gap == 28

    norm_rows = []
    for m_value, z_value in [(1, 1), (5, 7), (29, 41), (169, 239)]:
        assert math.gcd(m_value, z_value) == 1
        norm = m_value**2 + m_value**2 - z_value**2
        assert norm == 1
        norm_rows.append(
            {"primitive_point": [m_value, m_value, z_value], "indefinite_norm": norm}
        )
    return {
        "definite_rows": definite_rows,
        "live_irreducible_conic": {
            "loads": loads,
            "coordinates": coordinates,
            "equation": "169*T1*T3-72*T2^2",
            "value": conic_value,
            "doubled_matrix_determinant": conic_determinant,
            "strict_newton_gap": newton_gap,
            "actual_singleton_mass_claimed": False,
        },
        "bounded_primitive_indefinite_norm_rows": norm_rows,
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    binary = binary_controls()
    reciprocal_table = reciprocal_coefficient_table_controls()
    newton = newton_stability_controls()
    ternary = definite_and_live_ternary_controls()
    core = {
        "schema": "item381-beta-low-degree-symmetric-cancellation-classification-v1",
        "item": 381,
        "checked_date_beijing": "2026-09-01",
        "classification": "PROVED_LOW_DEGREE_CLASSIFICATION_AND_NEWTON_STABILITY",
        "dependencies": dependencies,
        "controls": {
            "binary": binary,
            "ternary_reciprocal_coefficient_table": reciprocal_table,
            "newton_stability": newton,
            "definite_and_live_ternary": ternary,
        },
        "claims": {
            "binary_definite": "Delta<0 gives beta-scale separation by completing the square",
            "binary_split": "square Delta reduces exact zeros to rational positive lines",
            "binary_irreducible": "nonsquare indefinite forms cannot vanish and satisfy |Q(T)|>=gcd(T1,T2)^2, but Pell-small norms exist",
            "ternary_reciprocal_cone": "nonnegative iff a,b,d,e,f>=0 and 2c+3d>=0, or all inequalities reversed",
            "newton_identity": "2(N-2)e2^2-3(N-1)e1e3=sum_(i<j)(xi-xj)^2*((e1^(ij))^2-e2^(ij))",
            "singleton_newton_separation": "normalized Newton gap exceeds A^-12*N^-2",
            "ternary_definite": "integral definite doubled matrix gives beta-scale eigenvalue separation",
            "live_conics": "irreducible indefinite conics may vanish strictly inside the positive Newton cone",
        },
        "declared_symbolic_controls_only": True,
        "actual_prime_or_target_census_performed": False,
        "constructed_actual_sub_beta_carrier": False,
        "strict_labels": {
            "PROVED": [
                "complete binary discriminant classification",
                "ternary reciprocal coefficient cone",
                "normalized Newton stability and singleton separation",
                "definite ternary bound",
                "primitive gcd/norm factorizations",
                "zero booking",
            ],
            "PROVED_SCOPED_NO_GO": [
                "definite binary and ternary quadratics",
                "reciprocal-positive and Newton-certified ternary quadratics",
                "split lines separated from the actual interval",
                "sub-beta denominators and content escapes",
            ],
            "EXACT_FINITE_ONLY": [
                "predeclared discriminants, Pell pairs, coefficient tables, Newton identities, and ambient conics"
            ],
            "OPEN": [
                "actual rational split-line correlation",
                "binary primitive Pell norms and gcd",
                "ternary actual isotropy, primitive norms, and gcd",
                "higher mixed-sign varieties and U_11 weighted bound",
            ],
        },
        "capacity_booking": {
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "new_booking": 0,
        },
    }
    core["certificate_digest"] = digest(core)
    return core


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item381_beta_low_degree_symmetric_cancellation_classification_certificate.json",
    )
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(output),
                "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                "digest": payload["certificate_digest"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
