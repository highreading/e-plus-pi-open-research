#!/usr/bin/env python3
"""Exact radius-3/2 certificate for a high-radius integral-jet pi pullback.

For

    phi(z)=z+(z^7-z^8)/140,
    G(z)=4*atan(phi(z)/(2-phi(z))),

this script uses rational complex arithmetic and the Schur--Cohn recursion
to prove that every solution of phi(z)=1+i is outside |z|=3/2.  Real
coefficients give the same result for 1-i.  Decimal roots and a finite jet
scan are included only as diagnostics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from high_radius_composed_pullback_hp_probe import PHI, composed_jets


QComplex = tuple[Fraction, Fraction]


def qadd(left: QComplex, right: QComplex) -> QComplex:
    return left[0] + right[0], left[1] + right[1]


def qsub(left: QComplex, right: QComplex) -> QComplex:
    return left[0] - right[0], left[1] - right[1]


def qmul(left: QComplex, right: QComplex) -> QComplex:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def qconj(value: QComplex) -> QComplex:
    return value[0], -value[1]


def qnorm(value: QComplex) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def qdiv(left: QComplex, right: QComplex) -> QComplex:
    denominator = qnorm(right)
    assert denominator
    numerator = qmul(left, qconj(right))
    return numerator[0] / denominator, numerator[1] / denominator


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def complex_record(value: QComplex) -> dict[str, dict[str, int]]:
    return {
        "real": fraction_record(value[0]),
        "imag": fraction_record(value[1]),
    }


def normalized_schur_certificate() -> list[dict]:
    """Return exact normalized Schur data for w^8 q((3/2)/w)."""
    radius = Fraction(3, 2)
    # Leading-to-constant coefficients of
    # w^8(phi((3/2)/w)-(1+i)).
    coefficients: list[QComplex] = [
        (Fraction(-1), Fraction(-1)),
        (radius, Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (radius**7 / 140, Fraction(0)),
        (-radius**8 / 140, Fraction(0)),
    ]
    records: list[dict] = []
    while len(coefficients) > 1:
        leading = coefficients[0]
        coefficients = [qdiv(value, leading) for value in coefficients]
        assert coefficients[0] == (Fraction(1), Fraction(0))
        constant = coefficients[-1]
        gap = Fraction(1) - qnorm(constant)
        assert gap > 0
        degree = len(coefficients) - 1
        records.append(
            {
                "degree": degree,
                "normalized_constant": complex_record(constant),
                "one_minus_constant_modulus_squared": fraction_record(gap),
            }
        )

        reciprocal = [qconj(value) for value in reversed(coefficients)]
        numerator = [
            qsub(value, qmul(constant, star))
            for value, star in zip(coefficients, reciprocal)
        ]
        assert numerator[-1] == (Fraction(0), Fraction(0))
        coefficients = numerator[:-1]

    assert coefficients[0] != (Fraction(0), Fraction(0))
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jet-order", type=int, default=120)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    schur_records = normalized_schur_certificate()
    assert [item["degree"] for item in schur_records] == list(range(8, 0, -1))
    jets = composed_jets(args.jet_order)

    z = sp.symbols("z")
    phi = sum(
        sp.Rational(value.numerator, value.denominator) * z**k
        for k, value in enumerate(PHI)
    )
    roots = sp.nroots(phi - (1 + sp.I), n=70, maxsteps=500)
    root_records = sorted(
        [
            {
                "real": str(sp.re(root).evalf(55)),
                "imag": str(sp.im(root).evalf(55)),
                "modulus": str(sp.Abs(root).evalf(55)),
            }
            for root in roots
        ],
        key=lambda item: sp.Float(item["modulus"], 60),
    )

    result = {
        "phi": "z+(z^7-z^8)/140",
        "phi_at_zero": str(phi.subs(z, 0)),
        "phi_at_one": str(phi.subs(z, 1)),
        "phi_derivative_jets_1_through_8": [
            int(sp.diff(phi, z, k).subs(z, 0)) for k in range(1, 9)
        ],
        "reciprocal_polynomial_at_radius_3_over_2": (
            "-(1+i)w^8+(3/2)w^7+(3/2)^7*w/140-(3/2)^8/140"
        ),
        "normalized_schur_cohn_records": schur_records,
        "all_schur_gaps_strictly_positive": True,
        "strict_radius_lower_bound": "3/2",
        "roots_of_phi_equals_1_plus_i_high_precision_diagnostic": root_records,
        "computed_composite_jet_order": args.jet_order,
        "all_computed_composite_jets_integral": all(
            isinstance(value, int) for value in jets
        ),
        "computed_composite_jets_sha256": hashlib.sha256(
            json.dumps(jets, separators=(",", ":")).encode()
        ).hexdigest(),
        "warning": (
            "The Schur--Cohn radius inequality is exact. Decimal roots and "
            "the finite jet recomputation are diagnostics; all-order jet "
            "integrality follows from Faa di Bruno and the integral jets of phi."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
