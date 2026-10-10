#!/usr/bin/env python3
"""Replay the corrected exterior asymptotic-capacity ledger.

The all-parameter proofs are in the companion source file.  This script
performs exact integer evaluation of the universal denominator and height
majorants on representative parity rows, checks every discrete inequality
used by the proof, and records diagnostic logarithmic ratios.  It does not
extrapolate the finite rows.
"""

from __future__ import annotations

import json
import math
import resource
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results/root_unity_corrected_asymptotic_capacity_certificate.json"


def log_integer(value: int) -> float:
    """Return log(value) without converting a large integer to float."""
    if value <= 0:
        raise ValueError("log_integer requires a positive integer")
    bits = value.bit_length()
    if bits <= 52:
        return math.log(value)
    shift = bits - 52
    return math.log(value >> shift) + shift * math.log(2.0)


def degree_regime(m: int, n: int, D: int) -> tuple[str, int | None]:
    """Return exactly the degree information proved in the frozen sources."""
    if (n + D) % 2 == 0 or (m % 2 == 1 and n % 2 == 1 and D % 2 == 0):
        return "top_exact", n + D
    if m % 2 == 1 and n % 2 == 0 and D % 2 == 1:
        return "odd_m_next_exact", n + D - 1
    if m % 2 == 0:
        return "even_m_forced_nonzero_degree_unknown", None
    raise AssertionError("parity classifier missed a regime")


def exact_ledger(m: int, n: int, D: int) -> dict[str, object]:
    if not (m >= 2 and n >= D >= 2):
        raise ValueError("need m >= 2 and n >= D >= 2")

    M = m * (n + 1)
    L = M + D - 1
    analytic_order = L - n

    factorial_product = math.prod(math.factorial(a) for a in range(n + 1))
    node_product = math.prod(
        h ** ((m - h) * (n + 1) ** 2) for h in range(1, m)
    )
    vandermonde = factorial_product**m * node_product
    Q = 2**M * vandermonde

    B0 = (M - 1) ** n * (m - 1) ** (M - 1)
    C_B = (
        2 ** (M - 1)
        * (D + 1)
        * math.factorial(M)
        * math.factorial(M - 1)
        * B0 ** (M - 1)
    )

    N0 = M + D - 2
    B_K = (
        2**N0
        * math.factorial(N0)
        * N0**D
        * math.factorial(m) ** (n + 1)
    )
    P0 = math.factorial(D - 1) * B_K ** (D - 1)
    omega = (D + 1) ** 2 // 4
    exterior_rank = D * (D + 1) // 2

    H_N_hat = P0 * (Q * omega + D * (D + 1) * m * C_B)
    H_W_hat = (
        2
        * exterior_rank
        * (m + 1)
        * (n + 1)
        * (n + m)
        * P0
        * (Q + 2 * C_B) ** 2
    )
    C0 = (2 * m + 1) * (2 * n + 1)

    gain = analytic_order * math.log(
        analytic_order / (math.e * math.pi * m)
    ) - n * math.log(math.pi)
    log_Q = log_integer(Q)
    log_H_N_hat = log_integer(H_N_hat)
    log_H_W_hat = log_integer(H_W_hat)
    universal_absolute_exponent = (
        2 * gain + log_Q - math.log(C0) - log_H_W_hat
    )

    regime, exact_degree = degree_regime(m, n, D)
    test_degree = exact_degree if exact_degree is not None else n + D
    kappa_r1 = test_degree
    chi_required_r1 = (
        kappa_r1 * log_H_N_hat
        + math.log(C0)
        + log_H_W_hat
        - 2 * gain
        - log_Q
    ) / (kappa_r1 + 1)

    # Exact inequalities used in Sections 3--5 of the source.
    assert B0 ** (M - 1) >= vandermonde
    assert H_W_hat >= Q * Q
    assert 2 * gain < log_Q
    assert universal_absolute_exponent < 0
    assert 23 * n * n + 14 * n + 55 > 0

    return {
        "parameters": {"m": m, "n": n, "D": D},
        "degree_regime": regime,
        "proved_exact_degree": exact_degree,
        "unknown_degree_test_uses_upper_bound": (
            test_degree if exact_degree is None else None
        ),
        "stationary_radius": analytic_order / m,
        "stationary_radius_admissible": analytic_order / m > math.pi,
        "bit_lengths": {
            "Q": Q.bit_length(),
            "C_B": C_B.bit_length(),
            "P0": P0.bit_length(),
            "H_N_hat": H_N_hat.bit_length(),
            "H_W_hat": H_W_hat.bit_length(),
        },
        "diagnostic_logs": {
            "G1": gain,
            "log_Q": log_Q,
            "two_G1_over_log_Q": 2 * gain / log_Q,
            "log_H_N_hat": log_H_N_hat,
            "log_H_W_hat": log_H_W_hat,
            "universal_absolute_exponent_chi_0": universal_absolute_exponent,
            "chi_required_leading_r1": chi_required_r1,
            "chi_required_fraction_of_log_H_N_hat_r1": (
                chi_required_r1 / log_H_N_hat
            ),
        },
        "exact_checks": {
            "B0_power_covers_vandermonde": True,
            "H_W_hat_at_least_Q_squared": True,
            "two_G1_less_than_log_Q": True,
            "universal_absolute_exponent_negative": True,
            "section_4_polynomial_gap_positive": True,
        },
    }


def fraction_string(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    sample_parameters = [
        (2, 2, 2),   # parity-allowed top degree
        (2, 4, 3),   # even-m forced family A
        (2, 5, 2),   # even-m forced family B
        (3, 4, 3),   # odd-m forced next coefficient
        (3, 5, 2),   # odd m,n with even D
        (4, 5, 3),   # parity-allowed top degree
        (5, 8, 7),   # larger odd-m forced next coefficient
    ]
    rows = [exact_ledger(*parameters) for parameters in sample_parameters]

    fixed_m_constants: list[dict[str, object]] = []
    for m in (2, 3, 5):
        for delta in (Fraction(0), Fraction(1)):
            gain_ratio_coefficient = Fraction(2) * (m - 1 + delta) / m
            r1_amplification_coefficient = (
                Fraction(m) * (1 + delta) / (2 * (m - 1 + delta))
            )
            fixed_m_constants.append(
                {
                    "m": m,
                    "delta": fraction_string(delta),
                    "G1_over_logQ_coefficient_of_1_over_n": fraction_string(
                        gain_ratio_coefficient
                    ),
                    "r1_analytic_amplification_coefficient_of_n_squared": (
                        fraction_string(r1_amplification_coefficient)
                    ),
                }
            )

    parity_pair_thresholds: list[dict[str, object]] = []
    for m in (2, 3, 5):
        for r in (1, 2, 3):
            threshold = Fraction(m - 1, 2 * r * r + r)
            parity_pair_thresholds.append(
                {
                    "m": m,
                    "hypothetical_algebraic_degree_r": r,
                    "required_lambda_strictly_below": fraction_string(threshold),
                }
            )

    observed_eliminant_splits = {4: [1, 2], 6: [4, 6], 8: [15, 20]}
    parity_segre_rows: list[dict[str, object]] = []
    for n, split in observed_eliminant_splits.items():
        s = n // 2
        segre_degree = math.comb(n - 1, s - 1)
        assert sum(split) == segre_degree
        parity_segre_rows.append(
            {
                "n": n,
                "s": s,
                "segre_dimension": n - 1,
                "segre_degree": segre_degree,
                "observed_eliminant_component_degrees": split,
                "has_degree_one_component": 1 in split,
            }
        )

    exterior_sum_dimensions: list[dict[str, object]] = []
    for n in (20, 100, 500):
        # Linear endpoint degree D=n.
        D = n
        target_degree = 2
        high_constraints = n + D - target_degree
        target_variables = 2 * high_constraints
        nu = 2
        while nu * (nu - 1) // 2 < target_variables:
            nu += 1
        exterior_variables = nu * (nu - 1) // 2
        assert exterior_variables > high_constraints
        assert nu <= D + 1
        siegel_exponent = Fraction(
            high_constraints, exterior_variables - high_constraints
        )
        exterior_sum_dimensions.append(
            {
                "endpoint_space_mode": "D_equals_n",
                "n": n,
                "D": D,
                "target_degree": target_degree,
                "high_coefficient_constraints_S": high_constraints,
                "endpoint_dimension_nu": nu,
                "exterior_variables_N": exterior_variables,
                "origin_order_loss_versus_E2": nu - 2,
                "siegel_exponent_S_over_N_minus_S": fraction_string(
                    siegel_exponent
                ),
            }
        )

        # Full endpoint space D=nu-1; solve the self-consistent dimension
        # inequality N >= 2S.
        nu_full = 2
        while True:
            D_full = nu_full - 1
            S_full = n + D_full - target_degree
            N_full = nu_full * (nu_full - 1) // 2
            if N_full >= 2 * S_full:
                break
            nu_full += 1
        assert N_full > S_full
        siegel_full = Fraction(S_full, N_full - S_full)
        exterior_sum_dimensions.append(
            {
                "endpoint_space_mode": "full_D_equals_nu_minus_1",
                "n": n,
                "D": D_full,
                "target_degree": target_degree,
                "high_coefficient_constraints_S": S_full,
                "endpoint_dimension_nu": nu_full,
                "exterior_variables_N": N_full,
                "origin_order_loss_versus_E2": nu_full - 2,
                "remainder_origin_order": "M",
                "saturated_monomial_basis_height": 1,
                "siegel_exponent_S_over_N_minus_S": fraction_string(
                    siegel_full
                ),
            }
        )

    exterior_sum_thresholds: list[dict[str, object]] = []
    for m in (2, 3, 5):
        for r in (1, 2, 3):
            for delta in (0, 1):
                target_degree = 2
                threshold = Fraction(
                    m - 1 + delta, r * r * target_degree + r
                )
                exterior_sum_thresholds.append(
                    {
                        "m": m,
                        "D_over_n_limit": f"{delta}/1",
                        "target_degree_d": target_degree,
                        "hypothetical_algebraic_degree_r": r,
                        "matched_height_lambda_strictly_below": fraction_string(
                            threshold
                        ),
                    }
                )

    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    output = {
        "scope": (
            "Finite exact-integer replay of universal majorants; "
            "all-parameter proofs are in the companion source."
        ),
        "global_symbolic_checks": {
            "section_4_gap_identity": (
                "32(n^2+n+2)-9(n+1)^2=23n^2+14n+55"
            ),
            "gap_polynomial_has_positive_coefficients": True,
            "proved_content_lower_bound_used": "log(c_Q) >= 0 only",
            "even_m_forced_degree_policy": (
                "Delta nonzero and d <= n+D only; no exact degree assumed"
            ),
            "conditional_parity_pair_policy": (
                "degree two and all-even-n existence are hypotheses, "
                "not inferred from n=4"
            ),
        },
        "representative_rows": rows,
        "fixed_m_asymptotic_constants": fixed_m_constants,
        "conditional_degree_two_parity_pair_lambda_thresholds": (
            parity_pair_thresholds
        ),
        "conditional_parity_pair_segre_diagnostics": parity_segre_rows,
        "conditional_nondecomposable_exterior_sum_dimensions": (
            exterior_sum_dimensions
        ),
        "conditional_nondecomposable_exterior_sum_thresholds": (
            exterior_sum_thresholds
        ),
        "resource_audit": {
            "peak_rss_kib": peak_rss_kib,
            "peak_rss_below_2_GiB": peak_rss_kib < 2 * 1024 * 1024,
        },
    }

    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {RESULT}")
    print(f"checked {len(rows)} representative rows")


if __name__ == "__main__":
    main()
