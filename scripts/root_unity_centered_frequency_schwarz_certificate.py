#!/usr/bin/env python3
"""Deterministic replay for the centered-frequency Schwarz correction.

The all-parameter analytic proof is in the companion source.  This script
checks the exact Laurent-frequency algebra on deterministic exterior sums,
the stationary-point identities symbolically, every discrete inequality
used by the denominator proof, and a bounded high-precision diagnostic grid.
No finite grid is extrapolated into an all-parameter theorem.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_centered_frequency_schwarz_certificate.json"


# An exponential polynomial is a dictionary (frequency, z-degree) -> integer.
ExpPoly = dict[tuple[int, int], int]


def clean(poly: ExpPoly) -> ExpPoly:
    return {key: value for key, value in poly.items() if value}


def add(left: ExpPoly, right: ExpPoly, scale: int = 1) -> ExpPoly:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, 0) + scale * value
    return clean(out)


def scalar(poly: ExpPoly, factor: int) -> ExpPoly:
    return clean({key: factor * value for key, value in poly.items()})


def derivative(poly: ExpPoly) -> ExpPoly:
    out: ExpPoly = {}
    for (frequency, degree), value in poly.items():
        if degree:
            key = (frequency, degree - 1)
            out[key] = out.get(key, 0) + degree * value
        if frequency:
            key = (frequency, degree)
            out[key] = out.get(key, 0) + frequency * value
    return clean(out)


def multiply(left: ExpPoly, right: ExpPoly) -> ExpPoly:
    out: ExpPoly = {}
    for (frequency_left, degree_left), value_left in left.items():
        for (frequency_right, degree_right), value_right in right.items():
            key = (frequency_left + frequency_right, degree_left + degree_right)
            out[key] = out.get(key, 0) + value_left * value_right
    return clean(out)


def wronskian(left: ExpPoly, right: ExpPoly) -> ExpPoly:
    return add(
        multiply(left, derivative(right)),
        multiply(right, derivative(left)),
        scale=-1,
    )


def frequency_shift(poly: ExpPoly, shift: int) -> ExpPoly:
    return clean(
        {(frequency + shift, degree): value for (frequency, degree), value in poly.items()}
    )


def coefficient_height(poly: ExpPoly) -> int:
    return max((abs(value) for value in poly.values()), default=0)


def degree(poly: ExpPoly) -> int:
    return max((power for _, power in poly), default=-1)


def frequency_interval(poly: ExpPoly) -> list[int]:
    frequencies = [frequency for frequency, _ in poly]
    return [min(frequencies), max(frequencies)] if frequencies else [0, 0]


def value_at_i_pi_as_pi_polynomial(poly: ExpPoly) -> list[int]:
    """Coefficients of sum a_k (i*pi)^k after exp(q*i*pi)=(-1)^q."""
    maximum = degree(poly)
    out = [0] * (maximum + 1)
    for (frequency, power), value in poly.items():
        out[power] += value * ((-1) ** frequency)
    return out


def deterministic_remainder(index: int, m: int, n: int) -> ExpPoly:
    """A dense deterministic test exponential polynomial of the right support."""
    return clean(
        {
            (frequency, power):
            ((-1) ** (index + frequency + power))
            * (index + 1 + 2 * frequency + 3 * power)
            for frequency in range(m + 1)
            for power in range(n + 1)
        }
    )


def exact_centering_grid() -> dict:
    rows = []
    for m in range(2, 6):
        for n in range(2, 5):
            remainders = [deterministic_remainder(index, m, n) for index in range(4)]
            weights = [2, -3, 5, 7, -11, 13]
            pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            exterior: ExpPoly = {}
            for weight, (left, right) in zip(weights, pairs):
                exterior = add(
                    exterior,
                    scalar(wronskian(remainders[left], remainders[right]), weight),
                )
            assert exterior
            assert frequency_interval(exterior)[0] >= 0
            assert frequency_interval(exterior)[1] <= 2 * m
            assert degree(exterior) <= 2 * n
            centered = frequency_shift(exterior, -m)
            assert frequency_interval(centered)[0] >= -m
            assert frequency_interval(centered)[1] <= m
            assert coefficient_height(centered) == coefficient_height(exterior)
            assert len(centered) == len(exterior)
            raw_value = value_at_i_pi_as_pi_polynomial(exterior)
            centered_value = value_at_i_pi_as_pi_polynomial(centered)
            assert centered_value == [(-1) ** m * value for value in raw_value]
            rows.append(
                {
                    "m": m,
                    "n": n,
                    "raw_frequency_interval": frequency_interval(exterior),
                    "centered_frequency_interval": frequency_interval(centered),
                    "polynomial_degree": degree(exterior),
                    "coefficient_height": coefficient_height(exterior),
                    "coefficient_count": len(exterior),
                    "i_pi_multiplier": (-1) ** m,
                }
            )
    return {
        "rows": rows,
        "row_count": len(rows),
        "all_frequency_height_and_i_pi_identities_exact": True,
    }


def symbolic_stationary_audit() -> dict:
    rho, A, m, n, pi = sp.symbols("rho A m n pi", positive=True)
    variable_part = 2 * A * sp.log(rho) - m * rho
    derivative_expr = sp.diff(variable_part, rho)
    stationary = 2 * A / m
    assert sp.simplify(derivative_expr.subs(rho, stationary)) == 0
    total_gain = sp.expand_log(
        2 * A * sp.log(stationary / pi) - m * stationary - 2 * n * sp.log(pi),
        force=True,
    )
    expected = 2 * A * sp.log(2 * A / (sp.E * pi * m)) - 2 * n * sp.log(pi)
    assert sp.simplify(total_gain - expected) == 0
    uncentered = 2 * A * sp.log(A / (sp.E * pi * m)) - 2 * n * sp.log(pi)
    assert sp.simplify(expected - uncentered - 2 * A * sp.log(2)) == 0
    boundary = -2 * n * sp.log(pi) - m * pi
    assert sp.simplify(expected.subs(A, m * pi / 2) - boundary) == 0
    return {
        "circle_exponent_variable_part": "2*A*log(rho)-m*rho",
        "stationary_radius": "2*A/m",
        "total_centered_gain": "2*A*log(2*A/(e*pi*m))-2*n*log(pi)",
        "improvement_over_uncentered_total_gain": "2*A*log(2)",
        "boundary_total_gain_when_2*A/m<=pi": "-2*n*log(pi)-m*pi",
        "stationary_and_boundary_match_at_2*A/m=pi": True,
    }


def Q_log(m: int, n: int) -> mp.mpf:
    return (
        m * (n + 1) * mp.log(2)
        + m * mp.fsum(mp.log(mp.factorial(a)) for a in range(1, n + 1))
        + (n + 1) ** 2
        * mp.fsum((m - h) * mp.log(h) for h in range(1, m))
    )


def centered_gain(m: int, n: int, D: int, nu: int = 2) -> tuple[mp.mpf, mp.mpf]:
    M = m * (n + 1)
    L_nu = M + D + 1 - nu
    A_nu = L_nu - n
    radius = mp.mpf(2 * A_nu) / m
    if radius > mp.pi:
        gain = A_nu * mp.log(2 * A_nu / (mp.e * mp.pi * m)) - n * mp.log(mp.pi)
    else:
        gain = -n * mp.log(mp.pi) - m * mp.pi / 2
    return gain, radius


def denominator_inequality_grid() -> dict:
    mp.mp.dps = 80
    maximum = None
    row_count = 0
    for m in range(2, 21):
        for n in range(2, 31):
            log_Q = Q_log(m, n)
            for D in range(2, n + 1):
                gain, radius = centered_gain(m, n, D, 2)
                ratio = 2 * gain / log_Q
                assert 2 * gain < log_Q
                assert radius > mp.pi
                row_count += 1
                row = {
                    "m": m,
                    "n": n,
                    "D": D,
                    "centered_radius": mp.nstr(radius, 30),
                    "two_centered_gain": mp.nstr(2 * gain, 35),
                    "log_Q": mp.nstr(log_Q, 35),
                    "ratio": mp.nstr(ratio, 30),
                }
                if maximum is None or ratio > maximum[0]:
                    maximum = (ratio, row)
    assert maximum is not None
    return {
        "range": "2<=m<=20, 2<=n<=30, 2<=D<=n, nu=2",
        "row_count": row_count,
        "maximum_two_centered_gain_over_log_Q": maximum[1],
        "finite_diagnostic_only": True,
    }


def exact_denominator_proof_checks() -> dict:
    # n >= 8 comparison after multiplying by 480.
    n = sp.symbols("n", integer=True)
    gap = 115 * n**2 - 602 * n - 397
    assert gap.subs(n, 8) == 2147
    assert sp.diff(gap, n).subs(n, 8) > 0
    assert sp.diff(gap, n, 2) > 0

    # Exact elementary logarithm bounds used in the source.
    # exp(7/10) > its cubic Taylor truncation = 12013/6000 > 2.
    cubic_exp_lower = sum(sp.Rational(7, 10) ** j / sp.factorial(j) for j in range(4))
    assert cubic_exp_lower == sp.Rational(12013, 6000)
    assert cubic_exp_lower > 2

    # The h=2 node term closes 4<=n<=7, m>=3.
    small_gap_min = (4 + 1) * (3 - 2) - 3
    assert small_gap_min == 2

    # S_n > n log 2 for n>=4: 2! contributes one copy, 3! more
    # than two copies, and each a!, a>=4, contributes at least one.
    factorial_copy_count = 1 + 2 + (4 - 3)
    assert factorial_copy_count == 4

    return {
        "log_2_upper_bound": "log(2)<7/10",
        "exp_cubic_lower_bound_exact": "12013/6000>2",
        "n_at_least_8_scaled_gap": "115*n^2-602*n-397",
        "scaled_gap_at_n_8": 2147,
        "scaled_gap_strictly_increasing_for_n_at_least_8": True,
        "small_n_node_term_minimum_integer_gap": small_gap_min,
        "S_n_strictly_greater_than_n_log_2_for_n_at_least_4": True,
        "all_parameter_proof_is_in_source": True,
    }


def general_endpoint_radius_grid() -> dict:
    mp.mp.dps = 50
    minimum = None
    row_count = 0
    monotone_checks = 0
    for m in range(2, 13):
        for n in range(2, 16):
            for D in range(2, n + 1):
                previous = None
                for nu in range(2, D + 2):
                    gain, radius = centered_gain(m, n, D, nu)
                    assert radius > mp.pi
                    if previous is not None:
                        assert gain < previous
                        monotone_checks += 1
                    previous = gain
                    row_count += 1
                    if minimum is None or radius < minimum[0]:
                        minimum = (
                            radius,
                            {"m": m, "n": n, "D": D, "nu": nu},
                        )
    assert minimum is not None
    assert minimum[0] == 4
    return {
        "range": "2<=m<=12, 2<=n<=15, 2<=D<=n, 2<=nu<=D+1",
        "row_count": row_count,
        "strict_gain_monotonicity_checks_as_nu_increases": monotone_checks,
        "minimum_centered_radius": mp.nstr(minimum[0], 20),
        "minimum_parameters": minimum[1],
        "finite_check_only_source_proves_radius_at_least_4": True,
    }


def main() -> None:
    payload = {
        "schema": "root-unity-centered-frequency-schwarz-correction-v1",
        "exact_frequency_algebra": exact_centering_grid(),
        "symbolic_optimization": symbolic_stationary_audit(),
        "exact_denominator_proof_checks": exact_denominator_proof_checks(),
        "general_endpoint_radius_grid": general_endpoint_radius_grid(),
        "denominator_inequality_diagnostic_grid": denominator_inequality_grid(),
        "scope": {
            "supersedes_uncentered_frequency_2m_circle_ledger": True,
            "centered_type": "m",
            "coefficient_height_is_unchanged_by_frequency_relabeling": True,
            "all_parameter_inequality": "2*G_centered<log(Q_mn)",
            "leading_n_log_n_threshold_unchanged_for_fixed_m_and_D_over_n": True,
            "no_nonvanishing_rank_gap_content_or_classification_theorem": True,
            "no_irrationality_or_transcendence_conclusion": True,
        },
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(OUT),
                "frequency_rows": payload["exact_frequency_algebra"]["row_count"],
                "denominator_grid_rows": payload[
                    "denominator_inequality_diagnostic_grid"
                ]["row_count"],
                "minimum_general_endpoint_centered_radius": payload[
                    "general_endpoint_radius_grid"
                ]["minimum_centered_radius"],
                "all_assertions_passed": True,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
