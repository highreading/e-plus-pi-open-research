#!/usr/bin/env python3
"""Exact finite replay for centered exterior reflection and reciprocity.

The companion source contains the all-parameter proofs.  This script builds
the actual full-endpoint Hermite--Pade remainders in small exact cases and
checks the reflection law, centered coefficient reciprocity, refined origin
orders, nondecomposable parity-homogeneous sums, and nonzero extreme
frequencies.  The finite rows are diagnostics for sharpness, not an
all-parameter extrapolation.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_centered_exterior_reflection_certificate.json"

# Dictionary key = (integer exponential frequency, polynomial degree).
ExpPoly = dict[tuple[int, int], sp.Rational]


def logistic_moments(max_degree: int) -> list[sp.Rational]:
    moments = [sp.Rational(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(sp.binomial(k, j) * moments[j] for j in range(k)) / 2
        )
    return moments


def jet_interpolation_map(m: int, n: int) -> tuple[sp.Matrix, list[tuple[int, int]]]:
    """Map C coefficients to T_C coefficients for the full endpoint space."""
    M = m * (n + 1)
    moments = logistic_moments(M + n + 3)
    columns = [(frequency, degree) for frequency in range(m) for degree in range(n + 1)]
    jet = sp.Matrix(
        [
            [
                sp.factorial(k) / sp.factorial(k - degree)
                * frequency ** (k - degree)
                if degree <= k
                else 0
                for frequency, degree in columns
            ]
            for k in range(M)
        ]
    )
    target = sp.Matrix(
        [
            [
                -sp.factorial(k) / sp.factorial(k - degree)
                * moments[k - degree]
                if degree <= k
                else 0
                for degree in range(n + 1)
            ]
            for k in range(M)
        ]
    )
    assert jet.det() != 0
    return jet.inv() * target, columns


def clean(poly: ExpPoly) -> ExpPoly:
    return {key: sp.cancel(value) for key, value in poly.items() if value}


def add(left: ExpPoly, right: ExpPoly, scale: sp.Rational = sp.Rational(1)) -> ExpPoly:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, sp.Rational(0)) + scale * value
    return clean(out)


def scalar(poly: ExpPoly, factor: sp.Rational) -> ExpPoly:
    return clean({key: factor * value for key, value in poly.items()})


def derivative(poly: ExpPoly) -> ExpPoly:
    out: ExpPoly = {}
    for (frequency, degree), value in poly.items():
        if degree:
            key = (frequency, degree - 1)
            out[key] = out.get(key, sp.Rational(0)) + degree * value
        if frequency:
            key = (frequency, degree)
            out[key] = out.get(key, sp.Rational(0)) + frequency * value
    return clean(out)


def multiply(left: ExpPoly, right: ExpPoly) -> ExpPoly:
    out: ExpPoly = {}
    for (q, k), a in left.items():
        for (r, ell), b in right.items():
            key = (q + r, k + ell)
            out[key] = out.get(key, sp.Rational(0)) + a * b
    return clean(out)


def wronskian(left: ExpPoly, right: ExpPoly) -> ExpPoly:
    return add(multiply(left, derivative(right)), multiply(right, derivative(left)), -1)


def frequency_shift(poly: ExpPoly, shift: int) -> ExpPoly:
    return clean({(q + shift, k): value for (q, k), value in poly.items()})


def reflected_raw(poly: ExpPoly, m: int) -> ExpPoly:
    """The transform exp(mz) F(-z)."""
    return clean({(m - q, k): (-1) ** k * value for (q, k), value in poly.items()})


def centered_reflection(poly: ExpPoly) -> ExpPoly:
    """The transform G(-z)."""
    return clean({(-q, k): (-1) ** k * value for (q, k), value in poly.items()})


def full_remainder(m: int, n: int, endpoint_degree: int, interpolation: sp.Matrix,
                   columns: list[tuple[int, int]]) -> ExpPoly:
    remainder: ExpPoly = {(0, endpoint_degree): sp.Rational(1)}
    for index, (frequency, degree) in enumerate(columns):
        value = interpolation[index, endpoint_degree]
        if not value:
            continue
        remainder[(frequency, degree)] = remainder.get(
            (frequency, degree), sp.Rational(0)
        ) + value
        remainder[(frequency + 1, degree)] = remainder.get(
            (frequency + 1, degree), sp.Rational(0)
        ) + value
    return clean(remainder)


def taylor_coefficient(poly: ExpPoly, order: int) -> sp.Rational:
    value = sp.Rational(0)
    for (frequency, degree), coefficient in poly.items():
        if degree <= order:
            value += coefficient * sp.Rational(
                frequency ** (order - degree), math.factorial(order - degree)
            )
    return sp.cancel(value)


def vanishing_order(poly: ExpPoly, limit: int) -> int:
    for order in range(limit + 1):
        if taylor_coefficient(poly, order) != 0:
            return order
    raise AssertionError("vanishing order exceeded audit limit")


def coefficient_digest(poly: ExpPoly) -> str:
    data = [
        [q, k, int(sp.numer(value)), int(sp.denom(value))]
        for (q, k), value in sorted(poly.items())
    ]
    return hashlib.sha256(json.dumps(data, separators=(",", ":")).encode()).hexdigest()


def verify_reciprocity(centered: ExpPoly, epsilon: int) -> None:
    assert centered_reflection(centered) == scalar(centered, epsilon)
    maximum_degree = max(k for _, k in centered)
    for r in range(1, max(abs(q) for q, _ in centered) + 1):
        for k in range(maximum_degree + 1):
            positive = centered.get((r, k), sp.Rational(0))
            negative = centered.get((-r, k), sp.Rational(0))
            assert negative == epsilon * (-1) ** k * positive
    for k in range(maximum_degree + 1):
        middle = centered.get((0, k), sp.Rational(0))
        if (-1) ** k != epsilon:
            assert middle == 0


def exact_pair_grid() -> dict:
    rows = []
    type_m_count = 0
    exact_lower_order_count = 0
    for m in (2, 3):
        for n in (2, 3, 4):
            M = m * (n + 1)
            interpolation, columns = jet_interpolation_map(m, n)
            remainders = [
                full_remainder(m, n, degree, interpolation, columns)
                for degree in range(n + 1)
            ]
            for degree, remainder in enumerate(remainders):
                sigma = (-1) ** degree
                assert reflected_raw(remainder, m) == scalar(
                    remainder, (-1) ** m * sigma
                )
                assert vanishing_order(remainder, M + 3) >= M

            for a in range(n + 1):
                for b in range(a + 1, n + 1):
                    sigma_a = (-1) ** a
                    sigma_b = (-1) ** b
                    tau = sigma_a * sigma_b
                    epsilon = -tau
                    centered = frequency_shift(wronskian(remainders[a], remainders[b]), -m)
                    verify_reciprocity(centered, epsilon)
                    order = vanishing_order(centered, 2 * M + 8)
                    if tau == -1:
                        lower_bound = 2 * M
                        block_delta = None
                    else:
                        centered_parity = (-1) ** m * sigma_a
                        delta = 0 if centered_parity == (-1) ** M else 1
                        block_delta = delta
                        lower_bound = 2 * (M + delta) + 1
                    assert order >= lower_bound
                    if order == lower_bound:
                        exact_lower_order_count += 1
                    has_both_extremes = any(q == m for q, _ in centered) and any(
                        q == -m for q, _ in centered
                    )
                    assert has_both_extremes
                    type_m_count += 1
                    rows.append(
                        {
                            "m": m,
                            "n": n,
                            "endpoint_monomial_degrees": [a, b],
                            "exterior_parity_tau": tau,
                            "centered_function_parity_epsilon": epsilon,
                            "same_parity_block_delta": block_delta,
                            "proved_order_lower_bound": lower_bound,
                            "actual_vanishing_order": order,
                            "lower_bound_attained": order == lower_bound,
                            "centered_frequency_interval": [-m, m],
                            "both_extreme_frequencies_nonzero": has_both_extremes,
                            "coefficient_sha256": coefficient_digest(centered),
                        }
                    )
    assert type_m_count == len(rows)
    assert exact_lower_order_count == len(rows)
    return {
        "rows": rows,
        "row_count": len(rows),
        "all_raw_remainder_reflections_exact": True,
        "all_centered_reciprocities_exact": True,
        "all_refined_order_lower_bounds_attained": True,
        "all_rows_have_nonzero_plus_and_minus_m_frequencies": True,
    }


def nondecomposable_parity_sums() -> dict:
    rows = []
    for m, n in ((2, 4), (3, 4)):
        interpolation, columns = jet_interpolation_map(m, n)
        remainders = [
            full_remainder(m, n, degree, interpolation, columns)
            for degree in range(n + 1)
        ]
        for tau in (-1, 1):
            total: ExpPoly = {}
            used_pairs = []
            skew = sp.zeros(n + 1)
            for a in range(n + 1):
                for b in range(a + 1, n + 1):
                    if (-1) ** (a + b) != tau:
                        continue
                    weight = (-1) ** (a + 2 * b) * (a + 2) * (b + 3)
                    total = add(total, scalar(wronskian(remainders[a], remainders[b]), weight))
                    used_pairs.append([a, b, weight])
                    skew[a, b] = weight
                    skew[b, a] = -weight
            skew_rank = skew.rank()
            # A nonzero decomposable bivector has skew-matrix rank exactly 2.
            # Rank 4 therefore certifies that this diagnostic exterior vector
            # is genuinely nondecomposable.
            assert skew_rank == 4
            centered = frequency_shift(total, -m)
            assert centered
            epsilon = -tau
            verify_reciprocity(centered, epsilon)
            rows.append(
                {
                    "m": m,
                    "n": n,
                    "exterior_parity_tau": tau,
                    "centered_function_parity_epsilon": epsilon,
                    "used_pair_count": len(used_pairs),
                    "used_pairs": used_pairs,
                    "skew_rank": skew_rank,
                    "genuinely_nondecomposable": True,
                    "actual_vanishing_order": vanishing_order(centered, 2 * m * (n + 1) + 10),
                    "both_extreme_frequencies_nonzero": (
                        any(q == m for q, _ in centered)
                        and any(q == -m for q, _ in centered)
                    ),
                    "coefficient_sha256": coefficient_digest(centered),
                }
            )
    assert all(row["both_extreme_frequencies_nonzero"] for row in rows)
    return {"rows": rows, "all_parity_sum_reciprocities_exact": True}


def hyperbolic_majorant_audit() -> dict:
    q = sp.symbols("q")
    identities = []
    for m in range(1, 11):
        geometric = sum(q**j for j in range(2 * m + 1))
        closed = (1 - q ** (2 * m + 1)) / (1 - q)
        assert sp.cancel(geometric - closed) == 0
        identities.append(
            {
                "m": m,
                "geometric_coefficient_count": 2 * m + 1,
                "strictly_less_than_count_for_0<q<1": True,
            }
        )

    mp.mp.dps = 60
    diagnostics = []
    for m in (2, 3, 5, 10):
        R = mp.mpf(4)
        correction = (1 - mp.e ** (-(2 * m + 1) * R)) / (1 - mp.e ** (-R))
        ratio_to_old_coarse = correction / (2 * m + 1)
        diagnostics.append(
            {
                "m": m,
                "R": "4",
                "D_m_over_exp_mR": mp.nstr(correction, 35),
                "ratio_to_(2m+1)_exp_mR": mp.nstr(ratio_to_old_coarse, 35),
                "log_prefactor_gain": mp.nstr(-mp.log(ratio_to_old_coarse), 35),
            }
        )
    return {
        "identity": (
            "1+2*sum_{r=1}^m cosh(rR)="
            "sinh((m+1/2)R)/sinh(R/2)="
            "exp(mR)*(1-exp(-(2m+1)R))/(1-exp(-R))"
        ),
        "geometric_checks": identities,
        "R_equals_4_diagnostics": diagnostics,
        "paired_coefficient_bound_strict_if_a_noncentral_coefficient_is_nonzero": True,
        "no_uniform_relative_gain_when_only_the_middle_frequency_is_present": True,
    }


def main() -> None:
    payload = {
        "schema": "root-unity-centered-exterior-reflection-reciprocity-v1",
        "exact_actual_pair_grid": exact_pair_grid(),
        "nondecomposable_parity_homogeneous_sums": nondecomposable_parity_sums(),
        "hyperbolic_circle_majorant": hyperbolic_majorant_audit(),
        "proved_in_source": {
            "raw_remainder_reflection": (
                "exp(mz) R_C(-z)=(-1)^m sigma_C R_C(z)"
            ),
            "centered_exterior_reflection": "G_p(-z)=-tau G_p(z)",
            "coefficient_reciprocity": "a_(-r,k)=(-tau)*(-1)^k*a_(r,k)",
            "mixed_parity_uniform_order": "at least 2L",
            "same_parity_uniform_order": "at least 2L+1",
            "same_block_refinement": "at least 2(L+delta_sigma)+1",
            "circle_type_remains_m": True,
        },
        "limitations": {
            "reflection_does_not_force_extreme_frequency_vanishing": True,
            "no_exponential_type_below_m": True,
            "circle_improvement_is_prefactor_level": True,
            "extra_origin_order_is_O(1)": True,
            "no_change_to_leading_n_log_n_gain": True,
            "no_rank_gap_content_classification_or_transcendence_result": True,
            "finite_exact_cases_are_diagnostics_only": True,
        },
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(OUT),
                "exact_pair_rows": payload["exact_actual_pair_grid"]["row_count"],
                "parity_sum_rows": len(
                    payload["nondecomposable_parity_homogeneous_sums"]["rows"]
                ),
                "all_assertions_passed": True,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
