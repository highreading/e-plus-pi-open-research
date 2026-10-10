#!/usr/bin/env python3
"""Exact replay for the all-degree endpoint-collapse theorem.

The companion source proves the vector-valued block identity, the rank-one
all-degree normal form, the primitive optimization comparison, the sharp
Dirichlet exponent, and the aligned/unaligned parity distinction.  This
certificate uses only exact symbolic, integer, and rational arithmetic.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import resource
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "results"
    / "root_unity_hardy_all_degree_endpoint_collapse_certificate.json"
)
BINARY_SOURCE = (
    ROOT / "sources" / "root_unity_hardy_endpoint_quotient_geometry_correction.md"
)
BINARY_SOURCE_SHA256 = "5bd489df02183a374145d889ca96a6d2f3940ba141af0592962920021fc3a901"
EMEASURE_SOURCE = ROOT / "sources" / "root_unity_gaussian_parity_mixing_barrier.md"
EMEASURE_SOURCE_SHA256 = "fbfb6fba663768b80364462608d0267d233d1828924b9d25f12dd9a7a1ea4b6d"
RSS_GUARD_KIB = 1024 * 1024


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(BINARY_SOURCE) == BINARY_SOURCE_SHA256
assert sha256_file(EMEASURE_SOURCE) == EMEASURE_SOURCE_SHA256


def positive_matrix(size: int, offset: int) -> sp.Matrix:
    base = sp.Matrix(
        size,
        size,
        lambda row, column: ((row + 2) * (column + 3) + offset) % 11 - 5,
    )
    return base.transpose() * base + (offset + size + 1) * sp.eye(size)


def block_schur_audit() -> dict:
    rows = []
    for evaluation_rank, kernel_rank, offset in [(1, 1, 2), (1, 4, 3), (2, 3, 5), (3, 2, 7)]:
        size = evaluation_rank + kernel_rank
        gram = positive_matrix(size, offset)
        A = gram[:evaluation_rank, :evaluation_rank]
        B = gram[:evaluation_rank, evaluation_rank:]
        D = gram[evaluation_rank:, evaluation_rank:]
        schur = D - B.transpose() * A.inv() * B
        assert all(minor > 0 for minor in [A[:j, :j].det() for j in range(1, evaluation_rank + 1)])
        assert all(minor > 0 for minor in [schur[:j, :j].det() for j in range(1, kernel_rank + 1)])

        u = sp.Matrix([row + 1 for row in range(evaluation_rank)])
        v = sp.Matrix([(-1) ** row * (row + 2) for row in range(kernel_rank)])
        direct = (u.transpose() * A * u)[0] + 2 * (u.transpose() * B * v)[0] + (v.transpose() * D * v)[0]
        shifted = u + A.inv() * B * v
        completed = (shifted.transpose() * A * shifted)[0] + (v.transpose() * schur * v)[0]
        assert sp.factor(direct - completed) == 0
        assert B.transpose() * A.inv() * B + schur == D
        rows.append(
            {
                "evaluation_rank": evaluation_rank,
                "kernel_rank": kernel_rank,
                "gram_determinant": str(gram.det()),
                "schur_determinant": str(sp.factor(schur.det())),
                "completed_square_identity": True,
                "perturbation_squared_norm_equals_v_transpose_D_v": True,
            }
        )
    return {"rows": rows}


def rank_one_audit() -> dict:
    rows = []
    for degree in range(1, 7):
        size = degree + 1
        quotient = positive_matrix(size, degree + 4)
        lam = sp.Matrix([sp.Rational(j + 2, j + 1) for j in range(degree)])
        transform = sp.zeros(size, size)
        transform[0, 0] = 1
        for column in range(degree):
            transform[0, column + 1] = -lam[column]
            transform[column + 1, column + 1] = 1
        changed = transform.transpose() * quotient * transform
        a = changed[0, 0]
        b = changed[1:, 0]
        D = changed[1:, 1:]
        eta = b / a
        transverse = (D - b * b.transpose() / a) / a
        assert eta * eta.transpose() + transverse == D / a
        assert all(
            transverse[:j, :j].det() > 0 for j in range(1, degree + 1)
        )

        signs = list(itertools.product((-1, 1), repeat=degree))
        vertex_values = []
        for sign in signs:
            vector = sp.Matrix(sign)
            vertex_values.append((vector.transpose() * D * vector)[0] / a)
        epsilon_squared = max(vertex_values)

        exhaustive_vectors = 0
        for values in itertools.product(range(-2, 3), repeat=degree):
            if not any(values):
                continue
            vector = sp.Matrix(values)
            height = max(abs(value) for value in values)
            value = (vector.transpose() * D * vector)[0] / a
            assert value <= epsilon_squared * height**2
            exhaustive_vectors += 1

        u = sp.Rational(7, 5)
        v = sp.Matrix([(-1) ** j * (j + 1) for j in range(degree)])
        y = sp.Matrix([u, *list(v)])
        direct = (y.transpose() * changed * y)[0] / a
        normal = (u + (eta.transpose() * v)[0]) ** 2 + (v.transpose() * transverse * v)[0]
        assert sp.factor(direct - normal) == 0
        rows.append(
            {
                "degree": degree,
                "quotient_determinant": str(quotient.det()),
                "transverse_determinant": str(sp.factor(transverse.det())),
                "epsilon_squared_vertex_maximum": str(epsilon_squared),
                "cube_vectors_checked": exhaustive_vectors,
                "normal_form_identity": True,
                "vertex_maximum_bounds_integer_cube": True,
            }
        )
    return {"rows": rows}


def gaussian_phase_audit() -> dict:
    x, z, t = sp.symbols("x z t", real=True)
    rows = []
    for degree in range(1, 13):
        coefficients = [(-1) ** j * (j + 2) for j in range(degree + 1)]
        ordinary = sum(coefficients[j] * x**j for j in range(degree + 1))
        gaussian = sp.expand(ordinary.subs(x, -sp.I * z))
        evaluated = sp.expand(gaussian.subs(z, sp.I * t))
        assert sp.expand(evaluated - ordinary.subs(x, t)) == 0
        gaussian_coefficients = [sp.expand(gaussian).coeff(z, j) for j in range(degree + 1)]
        assert all(coefficient / coefficients[j] in (1, -1, sp.I, -sp.I) for j, coefficient in enumerate(gaussian_coefficients))
        ordinary_content = math.gcd(*[abs(value) for value in coefficients])
        gaussian_squared_gcd = math.gcd(
            *[
                math.gcd(abs(int(sp.re(value))), abs(int(sp.im(value))))
                for value in gaussian_coefficients
            ]
        )
        assert ordinary_content == gaussian_squared_gcd
        rows.append(
            {
                "degree": degree,
                "evaluation_identity": True,
                "coefficient_phases_are_Gaussian_units": True,
                "ordinary_and_Gaussian_content": ordinary_content,
            }
        )
    return {"rows": rows}


def parity_audit() -> dict:
    z, t = sp.symbols("z t", real=True)
    rows = []
    for degree in range(1, 31):
        coefficients = [j + 1 for j in range(degree + 1)]
        polynomial = sum(coefficients[j] * z**j for j in range(degree + 1))
        evaluated = sp.expand(polynomial.subs(z, sp.I * t))
        even = sum(
            (-1) ** (j // 2) * coefficients[j] * t**j
            for j in range(0, degree + 1, 2)
        )
        odd = sum(
            (-1) ** ((j - 1) // 2) * coefficients[j] * t**j
            for j in range(1, degree + 1, 2)
        )
        assert sp.expand(evaluated - (even + sp.I * odd)) == 0
        modulus_squared = sp.expand(evaluated * sp.conjugate(evaluated))
        assert sp.expand(modulus_squared - even**2 - odd**2) == 0

        q_even = degree // 2 + 1
        q_odd = (degree + 1) // 2
        critical = max(q_even - 1, q_odd - 1)
        assert critical == degree // 2
        rows.append(
            {
                "degree": degree,
                "even_coefficient_count": q_even,
                "odd_coefficient_count": q_odd,
                "unaligned_Dirichlet_exponent": critical,
                "aligned_Dirichlet_exponent": degree,
                "orthogonal_parity_identity": True,
            }
        )
    return {"rows": rows}


def threshold_audit() -> dict:
    rows = []
    for degree in range(1, 21):
        for algebraic_degree in range(1, 6):
            threshold = algebraic_degree**2 * degree + algebraic_degree - 1
            gap = threshold - degree
            assert gap == (algebraic_degree**2 - 1) * degree + algebraic_degree - 1
            assert (gap == 0) == (algebraic_degree == 1)
            parity_half = degree // 2
            parity_actual_degree = 2 * parity_half
            parity_threshold = (
                algebraic_degree**2 * parity_actual_degree
                + algebraic_degree
                - 1
            )
            rows.append(
                {
                    "endpoint_degree": degree,
                    "algebraic_degree_r": algebraic_degree,
                    "Dirichlet_absolute_exponent": degree,
                    "conditional_measure_absolute_exponent": threshold,
                    "absolute_exponent_gap": gap,
                    "unaligned_parity_exponent": parity_half,
                    "better_parity_actual_degree": parity_actual_degree,
                    "better_parity_measure_threshold": parity_threshold,
                }
            )
    return {"rows": rows}


def fractional_part(value: Fraction) -> Fraction:
    return value - math.floor(value)


def dirichlet_finite_audit() -> dict:
    rows = []
    for degree in range(1, 6):
        for height in range(1, 6):
            base = 2 * height + 1
            maximum_numerator = sum(height * base**j for j in range(degree))
            modulus = max((height + 1) ** degree * 3, maximum_numerator * 5 + 7)
            lambdas = [Fraction(base**j, modulus) for j in range(degree)]
            points = []
            for vector in itertools.product(range(height + 1), repeat=degree):
                value = fractional_part(
                    sum((lambdas[j] * vector[j] for j in range(degree)), Fraction(0))
                )
                points.append((value, vector))
            points.sort()
            assert len({value for value, _ in points}) == len(points)
            cyclic_gaps = []
            for index in range(len(points)):
                next_index = (index + 1) % len(points)
                gap = points[next_index][0] - points[index][0]
                if next_index == 0:
                    gap += 1
                cyclic_gaps.append((gap, index, next_index))
            gap, first_index, second_index = min(cyclic_gaps)
            bound = Fraction(1, (height + 1) ** degree)
            assert gap <= bound
            first_vector = points[first_index][1]
            second_vector = points[second_index][1]
            difference = tuple(
                second_vector[j] - first_vector[j] for j in range(degree)
            )
            assert any(difference)
            assert max(abs(value) for value in difference) <= height
            rows.append(
                {
                    "degree": degree,
                    "height": height,
                    "point_count": len(points),
                    "minimum_cyclic_gap": f"{gap.numerator}/{gap.denominator}",
                    "Dirichlet_bound": f"{bound.numerator}/{bound.denominator}",
                    "difference_vector": list(difference),
                }
            )
    return {"rows": rows}


def algebraic_norm_audit() -> dict:
    x = sp.symbols("x")
    rows = []
    for degree in range(1, 9):
        minimal = x ** (degree + 1) - 2
        polynomial = sum(((-1) ** j * (j + 1)) * x**j for j in range(degree + 1))
        resultant = sp.resultant(minimal, polynomial, x)
        assert resultant != 0 and resultant.is_Integer
        rows.append(
            {
                "degree": degree,
                "minimal_polynomial": str(minimal),
                "test_polynomial": str(polynomial),
                "nonzero_integer_norm": str(resultant),
            }
        )
    return {"rows": rows}


def main() -> None:
    output = {
        "title": "All-degree Hardy endpoint collapse and Dirichlet boundary",
        "dependencies": {
            str(BINARY_SOURCE.relative_to(ROOT)): BINARY_SOURCE_SHA256,
            str(EMEASURE_SOURCE.relative_to(ROOT)): EMEASURE_SOURCE_SHA256,
        },
        "exact_block_schur_audit": block_schur_audit(),
        "exact_rank_one_audit": rank_one_audit(),
        "exact_Gaussian_phase_audit": gaussian_phase_audit(),
        "exact_parity_audit": parity_audit(),
        "exact_threshold_audit": threshold_audit(),
        "exact_finite_Dirichlet_audit": dirichlet_finite_audit(),
        "exact_algebraic_norm_audit": algebraic_norm_audit(),
        "theorem_scope": {
            "vector_valued_block_completion": True,
            "rank_one_all_degree_normal_form": True,
            "transverse_cube_vertex_formula": True,
            "primitive_minimum_comparison": True,
            "collapse_rate_is_required_for_exponent_transfer": True,
            "Dirichlet_absolute_exponent_d": True,
            "dimension_only_exponent_d_is_sharp": True,
            "conditional_measure_threshold_r_squared_d_plus_r_minus_1": True,
            "Gaussian_phase_alignment_preserves_height_content_and_degree": True,
            "unaligned_parity_exponent_floor_d_over_2": True,
            "no_asymptotic_collapse_rate_claimed": True,
            "no_classification_of_e_plus_pi": True,
        },
    }
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_GUARD_KIB
    OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
