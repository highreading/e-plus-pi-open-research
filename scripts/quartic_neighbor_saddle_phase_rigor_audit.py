#!/usr/bin/env python3
"""Adversarial certificate for the quartic saddle rigor audit."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from quartic_neighbor_saddle_phase_certificate import (  # noqa: E402
    positive_kernel_from_log_vector,
    primitive_integer_log_vector,
)
from quartic_power_kernel_hermite_certificate import (  # noqa: E402
    raw_coordinate_rows,
)


def symbolic_checks() -> dict[str, bool | str]:
    u, r, kappa, theta, eta, rho, magnitude = sp.symbols(
        "u r kappa theta eta rho magnitude", positive=True, real=True
    )
    h = (
        sp.log(u)
        + sp.log(1 + r**2 * u**2) / 2
        - sp.log(1 + r**4 * u**4) / (4 * r**4)
    )
    scaled_derivative = sp.factor(u * sp.diff(h, u))
    expected_derivative = (
        1
        + r**2 * u**2 / (1 + r**2 * u**2)
        - u**4 / (1 + r**4 * u**4)
    )

    y, t = sp.symbols("y t", positive=True, real=True)
    amplitude_derivative = (
        1 / y
        + y / (1 + y**2)
        - 4 * kappa * y**3 / (1 + y**4)
    )
    cleared = sp.factor(
        amplitude_derivative * y * (1 + y**2) * (1 + y**4)
    )
    expected_polynomial = 1 + 2 * t + (1 - 4 * kappa) * t**2 + (2 - 4 * kappa) * t**3

    y_phase = (
        sp.log(y)
        + sp.log(1 + y**2) / 2
        - kappa * sp.log(1 + y**4)
    )
    scaled_y_derivative = sp.factor(y * sp.diff(y_phase, y))
    expected_y_derivative = (
        1 + y**2 / (1 + y**2) - 4 * kappa * y**4 / (1 + y**4)
    )

    hankel = sp.trigsimp(
        (magnitude * rho * sp.cos(theta + eta)) ** 2
        - magnitude
        * sp.cos(theta)
        * magnitude
        * rho**2
        * sp.cos(theta + 2 * eta)
        - magnitude**2 * rho**2 * sp.sin(eta) ** 2
    )

    a, b, c, uu, vv, q = sp.symbols("a b c uu vv q", real=True)
    c0, c1, c2 = c * vv, -2 * c * uu, -a * vv + 2 * b * uu
    kernel_dot = sp.expand(a * c0 + b * c1 + c * c2)
    f_t = a - 2 * b * (uu / vv) + c * (uu / vv) ** 2
    square_identity = sp.expand(
        c0 * q**2 + c1 * q + c2 - vv * (c * (q - uu / vv) ** 2 - f_t)
    )

    return {
        "scaled_tail_derivative_identity": sp.simplify(
            scaled_derivative - expected_derivative
        )
        == 0,
        "unique_maximum_polynomial_identity": sp.expand(
            cleared.subs(y**2, t) - expected_polynomial
        )
        == 0,
        "complex_tail_scaled_log_derivative_identity": sp.simplify(
            scaled_y_derivative - expected_y_derivative
        )
        == 0,
        "phase_independent_hankel_identity": hankel == 0,
        "integer_kernel_dot_identity": kernel_dot == 0,
        "positive_square_identity": square_identity == 0,
        "left_boundary_gap": str(sp.N(-sp.Rational(1, 4) - (sp.log(sp.Rational(1, 2)) - sp.Rational(1, 64)), 30)),
        "right_boundary_gap": str(sp.N(-sp.Rational(1, 4) - (sp.log(2) - 4), 30)),
    }


def stable_root_grid() -> dict[str, object]:
    worst_ratio = 0.0
    failures = []
    samples = 0
    for eta in (1e-3, 3e-3, 1e-2, 3e-2, 1e-1):
        rho = 0.9
        for j in range(4001):
            theta = -math.pi + 2 * math.pi * j / 4000
            aa = math.cos(theta)
            bb = rho * math.cos(theta + eta)
            cc = rho**2 * math.cos(theta + 2 * eta)
            delta = bb * bb - aa * cc
            if delta < -1e-12:
                failures.append([eta, theta, "negative-discriminant"])
                continue
            if abs(cc) < 1e-12:
                roots = [aa / (2 * bb)]
            else:
                root_delta = math.sqrt(max(delta, 0.0))
                roots = [(bb + root_delta) / cc, (bb - root_delta) / cc]
            distance = min(abs(rho * root - 1) for root in roots)
            ratio = distance / eta
            worst_ratio = max(worst_ratio, ratio)
            if ratio > 2.00001:
                failures.append([eta, theta, ratio])
            samples += 1
    return {
        "samples": samples,
        "worst_distance_over_eta": worst_ratio,
        "failures": failures,
    }


def hankel_sign(n: int, k: int) -> int:
    rows = raw_coordinate_rows(n, k + 2)
    numerators = [rows[k + s - 1][0] - rows[k + s - 1][2] for s in range(3)]
    # d_0 d_2 / d_1^2=(k+1)/k for the raw coordinate denominators.
    determinant_numerator = (
        (k + 1) * numerators[1] ** 2 - k * numerators[0] * numerators[2]
    )
    return (determinant_numerator > 0) - (determinant_numerator < 0)


def selected_ray_scan() -> dict[str, object]:
    records = []
    for slope in (0.25, 0.5, 1.0, 2.0):
        signs = []
        for n in (20, 32, 48, 64, 80, 100, 120):
            k = max(n // 2 + 1, int(round(slope * n * math.log(n))))
            signs.append([n, k, hankel_sign(n, k)])
        records.append({"slope": slope, "records": signs})
    return {"critical_ray_diagnostics": records}


def exact_kernel_records() -> list[dict[str, object]]:
    mp.mp.dps = 100
    output = []
    for n, slope in ((20, 1.0), (40, 0.5), (80, 1.0), (100, 2.0)):
        k = int(round(slope * n * math.log(n)))
        vector, values = primitive_integer_log_vector(n, k)
        delta = values[1] * values[1] - values[0] * values[2]
        if delta <= 0:
            output.append({"n": n, "k": k, "positive_hankel": False})
            continue
        r = (mp.mpf(n) / (4 * k)) ** (mp.mpf(1) / 4)
        eta = r**5
        coeffs, metadata = positive_kernel_from_log_vector(vector, eta)
        dot = sum(vector[j] * coeffs[j] for j in range(3))
        polynomial_discriminant = coeffs[1] ** 2 - 4 * coeffs[0] * coeffs[2]
        tail_exponent = (
            -(k - n) * math.log(2)
            + n * math.log(4 * k / n) / 4
            + 2 * math.log(1 / float(eta))
        )
        output.append(
            {
                "n": n,
                "k": k,
                "positive_hankel": True,
                "kernel_dot": dot,
                "leading_coefficient_positive": coeffs[0] > 0,
                "polynomial_discriminant_negative": polynomial_discriminant < 0,
                "coefficient_digit_counts": [len(str(abs(z))) for z in coeffs],
                "tail_log_upper_exponent": tail_exponent,
                **metadata,
            }
        )
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "quartic_neighbor_saddle_phase_rigor_audit.json",
    )
    args = parser.parse_args()

    symbolic = symbolic_checks()
    stable = stable_root_grid()
    rays = selected_ray_scan()
    kernels = exact_kernel_records()

    boolean_symbolic = [value for value in symbolic.values() if isinstance(value, bool)]
    if not all(boolean_symbolic):
        raise AssertionError(symbolic)
    if stable["failures"]:
        raise AssertionError(stable)
    for record in kernels:
        if record.get("positive_hankel") and (
            record["kernel_dot"] != 0
            or not record["leading_coefficient_positive"]
            or not record["polynomial_discriminant_negative"]
        ):
            raise AssertionError(record)

    result = {
        "schema": "quartic-neighbor-saddle-phase-rigor-audit-v1",
        "symbolic_checks": symbolic,
        "stable_root_grid_diagnostic": stable,
        "selected_ray_scan": rays,
        "exact_positive_kernel_records": kernels,
        "verdict": "Two proof-presentation gaps were repaired; no counterexample or missing asymptotic hypothesis was found.",
        "repairs": [
            "The y>=1 logarithmic-derivative bound retains the endpoint factor 2^(-k), unlike the formerly cited crude power bound.",
            "The central contour now uses O(r)-length vertical connectors in a pole-free rectangle.",
            "The bounded stable root and adjacent inner interval are separated explicitly before applying the rational grid.",
            "The tail proof now treats separately the permitted degenerate kernel case c=0, P(Q)=1.",
        ],
        "warnings": [
            "Finite grids and selected-ray scans are diagnostics only.",
            "The analytic symmetric-form ratio is not a quadratic-field primitive-content theorem.",
            "Nothing in this audit classifies e+pi.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
