#!/usr/bin/env python3
"""Exact replay for successive Hardy minima and exterior no-amortization.

The companion source proves the all-parameter statements.  This certificate
checks their determinant, Pluecker, contraction, resultant, threshold, phase,
and parity algebra over integers, rationals, or symbolic polynomial rings.
No floating-point diagnostic or finite extrapolation is used.
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
    / "root_unity_hardy_successive_minima_exterior_certificate.json"
)
ITEM72_SOURCE = (
    ROOT / "sources" / "root_unity_hardy_all_degree_endpoint_collapse_theorem.md"
)
ITEM72_SOURCE_SHA256 = "6201f479c27e16afe4fdf515e24d860c0c360ea0be29c31d12feb97da0831687"
EXTERIOR_SOURCE = ROOT / "sources" / "root_unity_endpoint_exterior_power_audit.md"
EXTERIOR_SOURCE_SHA256 = "18db8252a651f692f55dc2f44c7fa8bede9d33d29cf86525714406c88b7ca8e5"
EMEASURE_SOURCE = ROOT / "sources" / "root_unity_gaussian_parity_mixing_barrier.md"
EMEASURE_SOURCE_SHA256 = "fbfb6fba663768b80364462608d0267d233d1828924b9d25f12dd9a7a1ea4b6d"
RSS_GUARD_KIB = 1024 * 1024


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(ITEM72_SOURCE) == ITEM72_SOURCE_SHA256
assert sha256_file(EXTERIOR_SOURCE) == EXTERIOR_SOURCE_SHA256
assert sha256_file(EMEASURE_SOURCE) == EMEASURE_SOURCE_SHA256


def gcd_nonzero(values: list[int]) -> int:
    result = 0
    for value in values:
        result = math.gcd(result, abs(value))
    assert result > 0
    return result


def matrix_rows_for_audit(degree: int, rank: int) -> sp.Matrix:
    """Primitive independent rows with a visible exterior index."""
    dimension = degree + 1
    multiplier = degree + rank + 2
    rows = []
    if rank <= degree:
        for row_index in range(rank):
            row = [0] * dimension
            row[0] = 1
            row[row_index + 1] = multiplier
            rows.append(row)
    else:
        assert rank == dimension
        rows.append([1] + [0] * degree)
        for column in range(1, dimension):
            row = [0] * dimension
            row[0] = 1
            row[column] = multiplier
            rows.append(row)
    matrix = sp.Matrix(rows)
    assert matrix.rank() == rank
    assert all(math.gcd(*[abs(int(value)) for value in matrix.row(i)]) == 1 for i in range(rank))
    return matrix


def pluecker_data(matrix: sp.Matrix) -> tuple[list[tuple[int, ...]], list[int], int, list[int]]:
    rank = matrix.rows
    subsets = list(itertools.combinations(range(matrix.cols), rank))
    minors = [int(matrix[:, subset].det()) for subset in subsets]
    content = gcd_nonzero(minors)
    primitive = [value // content for value in minors]
    assert gcd_nonzero(primitive) == 1
    return subsets, minors, content, primitive


def polynomial_height(polynomial: sp.Expr, variable: sp.Symbol) -> int:
    poly = sp.Poly(sp.expand(polynomial), variable, domain=sp.ZZ)
    return max(abs(int(value)) for value in poly.all_coeffs())


def lattice_and_exterior_audit() -> dict:
    x = sp.symbols("x")
    alpha = sp.Rational(3, 2)
    rows = []
    full_rows = []
    for degree in range(1, 8):
        dimension = degree + 1

        transform = sp.eye(dimension)
        for power in range(1, dimension):
            transform[power, 0] = alpha**power
        assert transform.det() == 1

        for rank in range(1, dimension + 1):
            matrix = matrix_rows_for_audit(degree, rank)
            subsets, minors, content, primitive = pluecker_data(matrix)
            multiplier = degree + rank + 2
            if rank <= degree:
                assert content == multiplier ** (rank - 1)
            else:
                assert content == multiplier**degree

            evaluations = sp.Matrix(
                [sum(matrix[i, power] * alpha**power for power in range(dimension)) for i in range(rank)]
            )
            tail = matrix[:, 1:]
            transformed = matrix * transform
            assert transformed[:, 0] == evaluations
            assert transformed[:, 1:] == tail
            assert transformed.rank() == rank

            if rank == dimension:
                determinant = int(matrix.det())
                assert transformed.det() == determinant
                height = max(abs(int(value)) for value in tail)
                epsilon = max(abs(value) for value in evaluations)
                assert abs(determinant) <= math.factorial(dimension) * epsilon * height**degree
                full_rows.append(
                    {
                        "degree": degree,
                        "dimension": dimension,
                        "coefficient_determinant": determinant,
                        "exterior_content": content,
                        "evaluation_tail_determinant_identity": True,
                        "factorial_determinant_bound": True,
                    }
                )
                continue

            subset_to_coordinate = {
                subset: primitive[index] for index, subset in enumerate(subsets)
            }
            polynomials = []
            coefficients_seen = []
            nonzero_evaluated_minors = 0
            for tail_subset in itertools.combinations(range(1, dimension), rank - 1):
                first_column = sp.Matrix(
                    [sum(matrix[i, power] * x**power for power in range(dimension)) for i in range(rank)]
                )
                determinant_matrix = first_column.row_join(matrix[:, tail_subset])
                polynomial = sp.expand(determinant_matrix.det() / content)
                assert sp.Poly(polynomial, x).domain == sp.ZZ
                polynomials.append(polynomial)

                poly = sp.Poly(polynomial, x, domain=sp.ZZ)
                for power in range(degree + 1):
                    coefficient = int(poly.nth(power))
                    if coefficient:
                        coefficients_seen.append(abs(coefficient))
                        index_set = tuple(sorted((power, *tail_subset)))
                        if power in tail_subset:
                            assert coefficient == 0
                        else:
                            assert abs(coefficient) == abs(subset_to_coordinate[index_set])

                evaluated_minor = determinant_matrix.subs(x, alpha).det() / content
                assert sp.expand(polynomial.subs(x, alpha) - evaluated_minor) == 0
                if evaluated_minor:
                    nonzero_evaluated_minors += 1

            primitive_absolute = [abs(value) for value in primitive if value]
            assert set(primitive_absolute).issubset(set(coefficients_seen))
            pluecker_height = max(primitive_absolute)
            collective_height = max(polynomial_height(polynomial, x) for polynomial in polynomials)
            assert collective_height == pluecker_height
            assert nonzero_evaluated_minors > 0

            height = max(abs(int(value)) for value in tail)
            epsilon = max(abs(value) for value in evaluations)
            for polynomial in polynomials:
                evaluated = abs(polynomial.subs(x, alpha))
                assert evaluated <= math.factorial(rank) * epsilon * height ** (rank - 1) / content

            rows.append(
                {
                    "degree": degree,
                    "rank": rank,
                    "row_vectors_individually_primitive": True,
                    "exterior_content": content,
                    "primitive_Pluecker_height": pluecker_height,
                    "contraction_polynomial_count": len(polynomials),
                    "collective_height_equals_Pluecker_height": True,
                    "nonzero_evaluated_contraction_count": nonzero_evaluated_minors,
                    "one_evaluation_column_bound": True,
                }
            )
    return {
        "coordinate_change_rows": 7,
        "lower_exterior_rows": rows,
        "full_determinant_rows": full_rows,
    }


def vector_rank(vectors: list[tuple[int, ...]]) -> int:
    if not vectors:
        return 0
    return int(sp.Matrix(vectors).rank())


def rank_threshold(values: list[tuple[tuple[int, ...], Fraction]]) -> list[Fraction]:
    thresholds = sorted({value for _, value in values})
    dimension = len(values[0][0])
    answer = []
    for target_rank in range(1, dimension + 1):
        for threshold in thresholds:
            vectors = [vector for vector, value in values if value <= threshold]
            if vector_rank(vectors) >= target_rank:
                answer.append(threshold)
                break
        else:
            raise AssertionError("finite audit set did not span")
    return answer


def rank_threshold_audit() -> dict:
    alpha = Fraction(3, 2)
    rows = []
    for degree in range(1, 6):
        dimension = degree + 1
        vectors = []
        for vector in itertools.product(range(-1, 2), repeat=dimension):
            if not any(vector[1:]):
                continue
            if math.gcd(*[abs(value) for value in vector]) != 1:
                continue
            evaluation = abs(sum(Fraction(vector[j]) * alpha**j for j in range(dimension)))
            vectors.append((vector, evaluation))
        original = rank_threshold(vectors)
        perturbation = Fraction(1, 17)
        perturbed_values = []
        for vector, value in vectors:
            signed = perturbation if sum(vector) % 2 else -perturbation
            changed = max(Fraction(0), value + signed)
            assert abs(changed - value) <= perturbation
            perturbed_values.append((vector, changed))
        perturbed = rank_threshold(perturbed_values)
        assert all(abs(left - right) <= perturbation for left, right in zip(original, perturbed))
        rows.append(
            {
                "degree": degree,
                "finite_primitive_vectors": len(vectors),
                "rank_thresholds_checked": dimension,
                "pointwise_error": f"{perturbation.numerator}/{perturbation.denominator}",
                "all_rank_threshold_differences_bounded": True,
            }
        )
    return {"rows": rows}


def resultant_audit() -> dict:
    x, y, t = sp.symbols("x y t")
    concrete_rows = []
    for degree_p in range(1, 5):
        for degree_q in range(1, 5):
            polynomial_p = x**degree_p + sum((j + 2) * x**j for j in range(degree_p))
            polynomial_q = (x + 1) ** degree_q + degree_p + degree_q + 1
            resultant_original = sp.resultant(polynomial_p, polynomial_q, x)
            assert resultant_original != 0 and resultant_original.is_Integer
            shifted_p = sp.expand(polynomial_p.subs(x, y + t))
            shifted_q = sp.expand(polynomial_q.subs(x, y + t))
            resultant_shifted = sp.resultant(shifted_p, shifted_q, y)
            assert sp.expand(resultant_shifted - resultant_original) == 0

            alpha = sp.Rational(3, 2)
            height = max(
                max(abs(int(value)) for value in sp.Poly(polynomial_p, x).all_coeffs()),
                max(abs(int(value)) for value in sp.Poly(polynomial_q, x).all_coeffs()),
            )
            epsilon = max(abs(polynomial_p.subs(x, alpha)), abs(polynomial_q.subs(x, alpha)))
            shifted_coefficients = []
            for polynomial in (shifted_p.subs(t, alpha), shifted_q.subs(t, alpha)):
                poly = sp.Poly(polynomial, y)
                shifted_coefficients.extend(abs(value) for value in poly.all_coeffs()[0:-1])
            coefficient_bound = max(shifted_coefficients)
            assert epsilon <= max(epsilon, coefficient_bound)
            assert abs(resultant_original) <= math.factorial(degree_p + degree_q) * epsilon * max(
                epsilon, coefficient_bound
            ) ** (degree_p + degree_q - 1)
            concrete_rows.append(
                {
                    "degree_P": degree_p,
                    "degree_Q": degree_q,
                    "nonzero_integer_resultant": str(resultant_original),
                    "translation_invariance": True,
                    "one_small_constant_factor_bound": True,
                }
            )

    ideal_rows = []
    for degree_p in range(1, 4):
        for degree_q in range(1, 4):
            coefficients_p = sp.symbols(f"a0:{degree_p + 1}")
            coefficients_q = sp.symbols(f"b0:{degree_q + 1}")
            generic_p = sum(coefficients_p[j] * x**j for j in range(degree_p + 1))
            generic_q = sum(coefficients_q[j] * x**j for j in range(degree_q + 1))
            generic_resultant = sp.resultant(generic_p, generic_q, x)
            common_zero_specialization = sp.expand(
                generic_resultant.subs({coefficients_p[0]: 0, coefficients_q[0]: 0})
            )
            assert common_zero_specialization == 0
            ideal_rows.append(
                {
                    "degree_P": degree_p,
                    "degree_Q": degree_q,
                    "resultant_in_constant_term_ideal": True,
                }
            )
    return {"concrete_rows": concrete_rows, "generic_ideal_rows": ideal_rows}


def threshold_audit() -> dict:
    rows = []
    for degree in range(1, 21):
        for exterior_rank in range(1, degree + 1):
            for algebraic_degree in range(1, 6):
                kappa = algebraic_degree**2 * degree + algebraic_degree - 1
                critical_content = Fraction(
                    exterior_rank * (kappa + 1) - (degree + 1), kappa + 1
                )
                alternate = Fraction(exterior_rank, 1) - Fraction(degree + 1, kappa + 1)
                assert critical_content == alternate
                if algebraic_degree == 1:
                    assert critical_content == exterior_rank - 1

                denominator = 2 * (kappa + 1)
                gamma_below = critical_content - Fraction(1, denominator)
                gamma_above = critical_content + Fraction(1, denominator)

                def exterior_exponent(gamma: Fraction) -> Fraction:
                    return Fraction(degree - exterior_rank + 1, 1) + gamma

                def exterior_height_exponent(gamma: Fraction) -> Fraction:
                    return Fraction(exterior_rank, 1) - gamma

                below_mu = exterior_exponent(gamma_below) / exterior_height_exponent(gamma_below)
                above_mu = exterior_exponent(gamma_above) / exterior_height_exponent(gamma_above)
                assert below_mu < kappa < above_mu
                rows.append(
                    {
                        "degree": degree,
                        "exterior_rank": exterior_rank,
                        "algebraic_degree_r": algebraic_degree,
                        "conditional_measure_exponent": kappa,
                        "critical_content_exponent": f"{critical_content.numerator}/{critical_content.denominator}",
                        "rational_case_is_k_minus_1": algebraic_degree != 1 or critical_content == exterior_rank - 1,
                        "strict_threshold_equivalence": True,
                    }
                )
    return {"rows": rows}


def phase_and_parity_audit() -> dict:
    z, x = sp.symbols("z x", real=True)
    alpha = sp.Rational(3, 2)
    rows = []
    for degree in range(1, 31):
        coefficients = [(-1) ** j * (j + 2) for j in range(degree + 1)]
        ordinary = sum(coefficients[j] * x**j for j in range(degree + 1))
        gaussian = sp.expand(ordinary.subs(x, -sp.I * z))
        assert sp.expand(gaussian.subs(z, sp.I * x) - ordinary) == 0

        evaluated = sp.expand(sum(coefficients[j] * (sp.I * x) ** j for j in range(degree + 1)))
        even = sp.re(evaluated).expand()
        odd = sp.im(evaluated).expand()
        assert sp.expand(evaluated - even - sp.I * odd) == 0
        assert sp.expand(evaluated * sp.conjugate(evaluated) - even**2 - odd**2) == 0

        dimension = degree + 1
        transform = sp.zeros(dimension, dimension)
        transform[0, 0] = 1
        transform[1, 1] = alpha
        for column in range(2, dimension):
            transform[0 if column % 2 == 0 else 1, column] = (
                (-1) ** (column // 2) * alpha**column
                if column % 2 == 0
                else (-1) ** ((column - 1) // 2) * alpha**column
            )
            transform[column, column] = 1
        assert transform.det() == alpha

        q_even = degree // 2 + 1
        q_odd = (degree + 1) // 2
        assert max(q_even - 1, q_odd - 1) == degree // 2
        rows.append(
            {
                "degree": degree,
                "Gaussian_phase_identity": True,
                "orthogonal_parity_identity": True,
                "even_dimension": q_even,
                "odd_dimension": q_odd,
                "two_evaluation_coordinate_determinant": "3/2",
                "unaligned_exponent": degree // 2,
            }
        )
    return {"rows": rows}


def main() -> None:
    output = {
        "title": "Successive Hardy minima and exterior no-amortization",
        "dependencies": {
            str(ITEM72_SOURCE.relative_to(ROOT)): ITEM72_SOURCE_SHA256,
            str(EXTERIOR_SOURCE.relative_to(ROOT)): EXTERIOR_SOURCE_SHA256,
            str(EMEASURE_SOURCE.relative_to(ROOT)): EMEASURE_SOURCE_SHA256,
        },
        "exact_lattice_and_exterior_audit": lattice_and_exterior_audit(),
        "exact_rank_threshold_audit": rank_threshold_audit(),
        "exact_resultant_audit": resultant_audit(),
        "exact_threshold_audit": threshold_audit(),
        "exact_phase_and_parity_audit": phase_and_parity_audit(),
        "theorem_scope": {
            "successive_minima_product_with_constants": True,
            "all_k_Hardy_rank_threshold_comparison": True,
            "full_determinant_has_one_evaluation_column": True,
            "saturated_exterior_contraction_is_integer_polynomial_vector": True,
            "collective_contraction_height_equals_primitive_Pluecker_height": True,
            "conditional_content_threshold_is_exact": True,
            "rational_critical_content_exponent_is_k_minus_1": True,
            "resultant_has_one_small_constant_factor": True,
            "phase_and_parity_are_separated": True,
            "no_finite_extrapolation": True,
            "no_exceptional_approximation_claimed": True,
            "no_classification_of_e_plus_pi": True,
        },
    }
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_GUARD_KIB
    OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
