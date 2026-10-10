#!/usr/bin/env python3
"""Reproducible numerical search diagnostics for sparse endpoint pullbacks.

For a finite integer tuple (a_m), search polynomials

    phi(z)=z+sum_m a_m*z^m*(1-z)/m!.

The script performs three deliberately separate diagnostics:

1. a one-term scan for 1 <= m <= M, using a fixed real-coefficient grid,
   deterministic scalar refinement, and nearby integer lattice points;
2. recomputation of a fixed catalog of multi-jet candidates found during
   pair/triple/four-term exploratory searches;
3. exhaustive floating-point root computation in the displayed 13^3 local
   integer box around the final four-jet candidate (a_7 is fixed at 46).

No numerical comparison in this file is a proof.  The companion exact
Schur--Cohn script certifies the final candidate and a small lattice box.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import minimize_scalar


FINAL_SUPPORT = (7, 9, 10, 11)
FINAL_PARAMETERS = (46, 213, -763, 20078)


def singular_radius(support: tuple[int, ...], parameters: tuple[float, ...]) -> float:
    """Double-precision minimum root modulus for phi(z)=1+i."""
    degree = max(support) + 1 if support else 1
    coefficients = np.zeros(degree + 1, dtype=np.complex128)
    coefficients[0] = -(1 + 1j)
    coefficients[1] = 1
    for m, a in zip(support, parameters):
        coefficient = a / math.factorial(m)
        coefficients[m] += coefficient
        coefficients[m + 1] -= coefficient
    while len(coefficients) > 1 and abs(coefficients[-1]) < 1e-18:
        coefficients = coefficients[:-1]
    return float(np.min(np.abs(np.roots(coefficients[::-1]))))


def singular_radius_normalized_one_term(m: int, coefficient: float) -> float:
    """Use coefficient b=a/m! directly during the continuous scan."""
    degree = m + 1
    coefficients = np.zeros(degree + 1, dtype=np.complex128)
    coefficients[0] = -(1 + 1j)
    coefficients[1] = 1
    coefficients[m] += coefficient
    coefficients[m + 1] -= coefficient
    while len(coefficients) > 1 and abs(coefficients[-1]) < 1e-18:
        coefficients = coefficients[:-1]
    return float(np.min(np.abs(np.roots(coefficients[::-1]))))


def one_term_scan(maximum_m: int, grid_size: int, local_span: int) -> list[dict]:
    grid = np.linspace(-0.25, 0.25, grid_size)
    records: list[dict] = []
    for m in range(1, maximum_m + 1):
        values = np.array(
            [singular_radius_normalized_one_term(m, float(b)) for b in grid]
        )
        top_count = min(8, grid_size)
        top_indices = np.argpartition(values, -top_count)[-top_count:]
        continuous_candidates: list[tuple[float, float]] = [
            (singular_radius_normalized_one_term(m, 0.0), 0.0)
        ]
        for index in top_indices:
            lower = float(grid[max(0, int(index) - 1)])
            upper = float(grid[min(grid_size - 1, int(index) + 1)])
            if lower == upper:
                continue
            optimum = minimize_scalar(
                lambda b: -singular_radius_normalized_one_term(m, float(b)),
                bounds=(lower, upper),
                method="bounded",
                options={"xatol": 1e-13, "maxiter": 300},
            )
            continuous_candidates.append((-float(optimum.fun), float(optimum.x)))
        continuous_radius, normalized_coefficient = max(continuous_candidates)
        if abs(continuous_radius - math.sqrt(2)) <= 1e-11:
            continuous_radius = singular_radius_normalized_one_term(m, 0.0)
            normalized_coefficient = 0.0

        factorial = math.factorial(m)
        center = round(normalized_coefficient * factorial)
        integer_candidates = set(range(center - local_span, center + local_span + 1))
        integer_candidates.add(0)
        best_radius = -1.0
        best_a = 0
        for a in sorted(integer_candidates):
            radius = singular_radius((m,), (a,))
            if radius > best_radius + 1e-12:
                best_radius, best_a = radius, a
            elif abs(radius - best_radius) <= 1e-12 and abs(a) < abs(best_a):
                best_radius, best_a = radius, a
        records.append(
            {
                "m": m,
                "continuous_normalized_coefficient": normalized_coefficient,
                "continuous_radius_diagnostic": continuous_radius,
                "nearby_integer_a": best_a,
                "nearby_integer_radius_diagnostic": best_radius,
            }
        )
    return records


def candidate_catalog() -> list[dict]:
    candidates = [
        ((7,), (36,), "one-term benchmark"),
        ((7, 8), (27, 26), "two-term"),
        ((7, 10), (35, 933), "two-term"),
        ((7, 11), (60, 30422), "two-term"),
        ((7, 14), (35, -3191864), "two-term"),
        ((7, 18), (34, 31469398607), "two-term"),
        ((7, 8, 11), (43, 32, 17835), "three-term"),
        ((7, 10, 11), (52, 897, 18070), "three-term"),
        (FINAL_SUPPORT, FINAL_PARAMETERS, "four-term final"),
    ]
    records = [
        {
            "support": list(support),
            "parameters": list(parameters),
            "stage": stage,
            "radius_diagnostic": singular_radius(support, parameters),
        }
        for support, parameters, stage in candidates
    ]
    records.sort(key=lambda item: item["radius_diagnostic"], reverse=True)
    return records


def local_integer_box() -> dict:
    records: list[dict] = []
    tested = 0
    for a9 in range(FINAL_PARAMETERS[1] - 6, FINAL_PARAMETERS[1] + 7):
        for a10 in range(FINAL_PARAMETERS[2] - 6, FINAL_PARAMETERS[2] + 7):
            for a11 in range(FINAL_PARAMETERS[3] - 6, FINAL_PARAMETERS[3] + 7):
                parameters = (FINAL_PARAMETERS[0], a9, a10, a11)
                radius = singular_radius(FINAL_SUPPORT, parameters)
                records.append(
                    {"parameters": list(parameters), "radius_diagnostic": radius}
                )
                tested += 1
    records.sort(key=lambda item: item["radius_diagnostic"], reverse=True)
    assert records[0]["parameters"] == list(FINAL_PARAMETERS)
    return {
        "support": list(FINAL_SUPPORT),
        "fixed_a7": FINAL_PARAMETERS[0],
        "a9_range_inclusive": [FINAL_PARAMETERS[1] - 6, FINAL_PARAMETERS[1] + 6],
        "a10_range_inclusive": [FINAL_PARAMETERS[2] - 6, FINAL_PARAMETERS[2] + 6],
        "a11_range_inclusive": [FINAL_PARAMETERS[3] - 6, FINAL_PARAMETERS[3] + 6],
        "number_tested": tested,
        "best_record": records[0],
        "top_25_records": records[:25],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-one-term-m", type=int, default=30)
    parser.add_argument("--grid-size", type=int, default=501)
    parser.add_argument("--integer-local-span", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.grid_size < 17:
        raise ValueError("grid size must be at least 17")

    one_term = one_term_scan(
        args.max_one_term_m, args.grid_size, args.integer_local_span
    )
    best_one_term = max(
        one_term, key=lambda item: item["nearby_integer_radius_diagnostic"]
    )
    result = {
        "family": "phi(z)=z+sum_m a_m*z^m*(1-z)/m!",
        "sign_and_jet_convention": (
            "The m-term contributes +a_m to phi^(m)(0) and "
            "-(m+1)*a_m to phi^(m+1)(0)."
        ),
        "software": {"numpy": np.__version__, "scipy": scipy.__version__},
        "one_term_scan_parameters": {
            "m_range_inclusive": [1, args.max_one_term_m],
            "normalized_coefficient_interval": [-0.25, 0.25],
            "grid_size": args.grid_size,
            "integer_local_span": args.integer_local_span,
        },
        "one_term_records": one_term,
        "best_one_term_record": best_one_term,
        "selected_multijet_candidate_catalog": candidate_catalog(),
        "final_candidate_local_integer_box": local_integer_box(),
        "warning": (
            "Every radius and ordering in this file is a floating-point "
            "diagnostic. The continuous scan is not a global optimization "
            "proof. The companion exact Schur--Cohn artifact certifies only "
            "the stated final candidate and its exact 3^4 neighbor test."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
