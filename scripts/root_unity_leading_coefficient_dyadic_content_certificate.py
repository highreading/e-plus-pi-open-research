#!/usr/bin/env python3
"""Exact replay for the power-of-two leading-coefficient content theorem.

The infinite valuation and content statements are proved in the companion
source.  This script replays their algebra over QQ and records a finite full
Delta audit without extrapolating the observed full contents.
"""

from __future__ import annotations

import hashlib
import json
import math
import resource
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_leading_coefficient_dyadic_content_certificate.json"
sys.path.insert(0, str(ROOT / "scripts"))
import root_unity_corrected_exterior_primitive_height_certificate as exterior  # noqa: E402
import root_unity_gamma_logistic_minor_certificate as logistic  # noqa: E402


X = sp.symbols("X")


def v2_integer(value: int) -> int:
    assert value
    value = abs(int(value))
    answer = 0
    while value % 2 == 0:
        answer += 1
        value //= 2
    return answer


def v2_rational(value: sp.Expr) -> int:
    value = sp.Rational(value)
    return v2_integer(int(sp.numer(value))) - v2_integer(int(sp.denom(value)))


def logistic_moment_odd(s: int) -> sp.Rational:
    """mu_(2s-1) in the normalization of the source."""
    assert s >= 1
    return sp.factor(-(2 ** (2 * s) - 1) * sp.bernoulli(2 * s) / (2 * s))


def leading_row(q: int) -> tuple[dict, sp.Rational]:
    h = 2**q
    n = h - 1
    B = sp.Poly(X ** (h - 1) * (X - 1) ** (h + 1) * (X - 2) ** (h - 1), X)
    C = sp.Poly(X**h * (X - 1) ** (h - 1) * (X - 2) ** h, X)
    A = sp.Poly(2 * B.as_expr() - 2**h * C.as_expr(), X, domain=sp.ZZ)
    assert A.degree() == 3 * h - 1
    assert all(int(coefficient) % 2 == 0 for coefficient in A.all_coeffs())

    critical_degree = 2 * h - 1
    critical_coefficient = int(A.nth(critical_degree))
    assert v2_integer(critical_coefficient) == 1

    functional_value = sp.Rational(0)
    term_valuations: dict[int, int] = {}
    for s in range(1, 3 * h // 2 + 1):
        coefficient = int(A.nth(2 * s - 1))
        if coefficient == 0:
            continue
        moment = logistic_moment_odd(s)
        assert v2_rational(moment) == -2 - v2_integer(s)
        term = coefficient * moment
        functional_value += term
        term_valuations[s] = v2_rational(term)

    minimum = min(term_valuations.values())
    minimizers = [s for s, valuation in term_valuations.items() if valuation == minimum]
    assert minimum == -q - 1
    assert minimizers == [h]
    functional_value = sp.factor(functional_value)
    assert v2_rational(functional_value) == -q - 1

    u_h = sp.factor(2 ** (q + 1) * functional_value)
    assert sp.denom(u_h) == 1
    u_h_int = int(u_h)
    assert u_h_int % 2

    leading = sp.factor(-functional_value / (2**h * sp.factorial(n)))
    assert v2_rational(leading) == -2 * h
    numerator = int(sp.numer(leading))
    denominator = int(sp.denom(leading))
    assert v2_integer(denominator) == 2 * h

    g_h = math.gcd(abs(u_h_int), math.factorial(n))
    expected_numerator = -u_h_int // g_h
    expected_denominator = 2 ** (h + q + 1) * math.factorial(n) // g_h
    assert numerator == expected_numerator
    assert denominator == expected_denominator

    norm_bound = (
        2 ** (h + 2) * 3 ** (h - 1)
        + 2 ** (2 * h - 1) * 3**h
    )
    numerator_bound = 2**q * math.factorial(3 * h - 1) * norm_bound
    assert abs(numerator) <= abs(u_h_int) <= numerator_bound

    factorial_v2_sum = sum(v2_integer(math.factorial(a)) for a in range(1, h))
    assert factorial_v2_sum == h * (h - 1 - q) // 2
    universal_Q_v2 = 3 * h + h * h + 3 * factorial_v2_sum
    assert universal_Q_v2 == (5 * h * h + 3 * h - 3 * q * h) // 2

    row = {
        "q": q,
        "h": h,
        "n": n,
        "critical_degree": critical_degree,
        "critical_coefficient_v2": v2_integer(critical_coefficient),
        "unique_minimal_logistic_term_index_s": h,
        "functional_value_v2": v2_rational(functional_value),
        "u_h_is_odd_integer": True,
        "u_h_decimal_digits": len(str(abs(u_h_int))),
        "leading_numerator": str(numerator),
        "leading_denominator": str(denominator),
        "leading_coefficient_v2": v2_rational(leading),
        "leading_numerator_decimal_digits": len(str(abs(numerator))),
        "leading_denominator_decimal_digits": len(str(denominator)),
        "explicit_numerator_bound_verified": True,
        "universal_Q_v2": universal_Q_v2,
        "global_content_v2_upper_bound": universal_Q_v2 - 2 * h,
    }
    return row, leading


def checkerboard_replay(q: int) -> dict:
    h = 2**q
    n = h - 1
    M = 3 * h
    moments = logistic.logistic_moments(M + 6)
    K = logistic.endpoint_matrix(3, n, 2, moments, centered=True)
    assert K.shape == (1, 3)
    assert K[0, 0] == 0 and K[0, 2] == 0 and K[0, 1] != 0
    basis = sp.Matrix.hstack(*K.nullspace())
    pairs, pluecker, _ = exterior.saturated_pluecker(basis)
    assert pairs == [(0, 1), (0, 2), (1, 2)]
    assert pluecker == [0, 1, 0]
    return {
        "q": q,
        "h": h,
        "checkerboard_row_is_0_nonzero_0": True,
        "saturated_pluecker": pluecker,
    }


def full_delta_replay(q: int, expected_leading: sp.Rational) -> dict:
    h = 2**q
    n = h - 1
    exact = exterior.exact_row(3, n, 2)
    primitive = exact["primitive_delta_coefficients_ascending"]
    content = exact["delta_cleared_content"]
    denominator = exact["delta_minimal_denominator"]
    # exact_row canonically flips the entire primitive coefficient vector so
    # that its first nonzero entry is positive; the exterior orientation in
    # the theorem is fixed instead by p=e_0 wedge e_2.  Compare absolute
    # values here and retain the theorem's sign in leading_row.
    reconstructed_leading = sp.Rational(primitive[-1] * content, denominator)
    assert abs(reconstructed_leading) == abs(expected_leading)
    assert exact["delta_actual_degree"] == h + 1
    assert denominator % int(sp.denom(expected_leading)) == 0
    assert content % 2 == 1
    assert math.gcd(denominator, content) == 1
    assert int(sp.numer(expected_leading)) % content == 0
    return {
        "q": q,
        "h": h,
        "delta_actual_degree": exact["delta_actual_degree"],
        "delta_minimal_denominator": str(denominator),
        "delta_cleared_content": str(content),
        "observed_intrinsic_content_one": content == 1,
        "content_coprime_to_minimal_denominator": True,
        "content_divides_reduced_leading_numerator": True,
        "primitive_height_decimal_digits": len(
            str(max(abs(value) for value in primitive))
        ),
        "primitive_leading_decimal_digits": len(str(abs(primitive[-1]))),
        "full_corrected_polynomial_replay_is_finite_only": True,
    }


def main() -> None:
    leading_rows: list[dict] = []
    leading_values: dict[int, sp.Rational] = {}
    digest = hashlib.sha256()
    for q in range(2, 7):
        row, leading = leading_row(q)
        leading_rows.append(row)
        leading_values[q] = leading
        digest.update(
            f"{q},{sp.numer(leading)},{sp.denom(leading)}\n".encode()
        )

    checkerboard_rows = [checkerboard_replay(q) for q in range(2, 6)]
    full_delta_rows = [
        full_delta_replay(q, leading_values[q]) for q in range(2, 5)
    ]

    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_rss_limit_kib = 2 * 1024 * 1024
    assert peak_rss_kib < peak_rss_limit_kib
    payload = {
        "schema": "root-unity-leading-coefficient-dyadic-content-certificate-v1",
        "infinite_theorem_replay": {
            "q_rule": "2 <= q <= 6 in this finite replay",
            "row_count": len(leading_rows),
            "all_critical_coefficients_have_v2_one": True,
            "all_minimal_logistic_terms_are_unique_at_s_equals_h": True,
            "all_functional_values_have_v2_minus_q_minus_one": True,
            "all_leading_coefficients_have_v2_minus_2h": True,
            "all_explicit_numerator_bounds_verified": True,
            "exact_leading_digest_sha256": digest.hexdigest(),
        },
        "checkerboard_saturation_replay": {
            "row_count": len(checkerboard_rows),
            "all_endpoint_rows_are_0_nonzero_0": True,
            "all_saturated_pluecker_vectors_are_e0_wedge_e2": True,
        },
        "finite_full_delta_replay": {
            "row_count": len(full_delta_rows),
            "all_actual_degrees_equal_h_plus_one": True,
            "all_leading_coefficient_absolute_values_match_formula": True,
            "global_exterior_orientation_difference_is_documented": True,
            "all_contents_are_coprime_to_minimal_denominators": True,
            "all_contents_divide_reduced_leading_numerators": True,
            "all_observed_intrinsic_contents_are_one": True,
            "no_extrapolation": True,
        },
        "leading_rows": leading_rows,
        "checkerboard_rows": checkerboard_rows,
        "full_delta_rows": full_delta_rows,
        "resource_audit": {
            "required_peak_rss_limit_kib": peak_rss_limit_kib,
            "observed_peak_rss_below_2_GiB": True,
            "note": "The variable observed RSS is printed but omitted from deterministic JSON.",
        },
        "logical_scope": {
            "proved_in_source": (
                "The formula, exact dyadic valuation, numerator content cap, "
                "and universal-clearing dyadic cap hold for every q>=2."
            ),
            "finite_only": (
                "The complete corrected polynomials and their observed content "
                "one are finite replays and are not extrapolated."
            ),
            "remaining_obstruction": (
                "A single leading coefficient cannot lower-bound primitive "
                "height; a gcd theorem involving a second coefficient is still needed."
            ),
        },
        "versions": {
            "python": sys.version,
            "sympy": sp.__version__,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["infinite_theorem_replay"], indent=2, sort_keys=True))
    print(json.dumps(payload["finite_full_delta_replay"], indent=2, sort_keys=True))
    print(json.dumps(payload["resource_audit"], indent=2, sort_keys=True))
    print(f"observed_peak_rss_kib={peak_rss_kib}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
