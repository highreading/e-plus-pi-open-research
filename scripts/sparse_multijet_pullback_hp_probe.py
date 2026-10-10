#!/usr/bin/env python3
"""Finite exact diagonal Hermite--Pade probe for the four-jet pullback.

This is a diagnostic companion to the exact radius certificate.  It proves
the displayed ranks, contents, and endpoint intervals only for n <= max_n;
it supplies no all-degree rank, nonvanishing, height, or decay theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

from composed_integral_pullback_hp_probe import (
    convolution,
    e_plus_pi_interval,
    record,
)


SUPPORT = (7, 9, 10, 11)
PARAMETERS = (46, 213, -763, 20078)


def phi_coefficients() -> list[Fraction]:
    coefficients = [Fraction(0) for _ in range(max(SUPPORT) + 2)]
    coefficients[1] = Fraction(1)
    for m, a in zip(SUPPORT, PARAMETERS):
        value = Fraction(a, math.factorial(m))
        coefficients[m] += value
        coefficients[m + 1] -= value
    return coefficients


PHI = phi_coefficients()


def composed_jets(maximum: int) -> list[int]:
    """Return G^(k)(0), 0 <= k <= maximum, by exact division of G'."""
    phi_prime = [k * PHI[k] for k in range(1, len(PHI))]
    numerator = [4 * value for value in phi_prime]
    square = convolution(PHI, PHI)
    denominator = square + [Fraction(0)] * max(0, len(PHI) - len(square))
    for k, value in enumerate(PHI):
        denominator[k] -= 2 * value
    denominator[0] += 2

    coefficients: list[Fraction] = []
    for r in range(maximum):
        rhs = numerator[r] if r < len(numerator) else Fraction(0)
        for j in range(1, min(r, len(denominator) - 1) + 1):
            rhs -= denominator[j] * coefficients[r - j]
        coefficients.append(rhs / denominator[0])

    jets = [0]
    for k in range(1, maximum + 1):
        value = coefficients[k - 1] * math.factorial(k - 1)
        assert value.denominator == 1
        jets.append(value.numerator)
    return jets


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=15)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    jets = composed_jets(3 * args.max_n + 1)
    s_interval = e_plus_pi_interval()
    records = [record(n, jets, s_interval) for n in range(1, args.max_n + 1)]
    result = {
        "function": (
            "G(z)=4*atan(phi(z)/(2-phi(z))), "
            "phi=z+46*z^7*(1-z)/7!+213*z^9*(1-z)/9!"
            "-763*z^10*(1-z)/10!+20078*z^11*(1-z)/11!"
        ),
        "support_indices": list(SUPPORT),
        "integer_endpoint_jet_parameters": list(PARAMETERS),
        "phi_derivative_jets_1_through_12": [
            int(PHI[k] * math.factorial(k)) for k in range(1, len(PHI))
        ],
        "all_computed_G_jets_integral": True,
        "computed_G_jet_sha256": hashlib.sha256(
            json.dumps(jets, separators=(",", ":")).encode()
        ).hexdigest(),
        "records": records,
        "endpoint_decades": [
            item.get("endpoint_interval_certificate", {}).get(
                "single_certified_base10_decade"
            )
            for item in records
        ],
        "warning": (
            "Finite exact diagnostic only; no all-degree rank, nonvanishing, "
            "height, content, or asymptotic conclusion."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
