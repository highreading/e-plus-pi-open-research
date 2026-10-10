#!/usr/bin/env python3
"""Exact Schur--Cohn certificate for a sparse integral-Hurwitz pullback.

The certified polynomial is

    phi(z) = z + 46*z^7*(1-z)/7! + 213*z^9*(1-z)/9!
                 - 763*z^10*(1-z)/10! + 20078*z^11*(1-z)/11!.

For q(z)=phi(z)-(1+i), exact arithmetic in Q(i) proves that all roots of
q lie outside |z|=1747/1000.  Conjugation gives the same conclusion for
phi(z)=1-i.  The program also performs an exact 3^4 neighboring-lattice
classification at the same radius.  Decimal roots are diagnostics only.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


QComplex = tuple[Fraction, Fraction]

SUPPORT = (7, 9, 10, 11)
PARAMETERS = (46, 213, -763, 20078)
CERTIFIED_RADIUS = Fraction(1747, 1000)


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


def phi_coefficients(parameters: tuple[int, ...]) -> list[Fraction]:
    """Ascending ordinary-power coefficients of the endpoint-fixed phi."""
    assert len(parameters) == len(SUPPORT)
    degree = max(SUPPORT) + 1
    coefficients = [Fraction(0) for _ in range(degree + 1)]
    coefficients[1] = Fraction(1)
    for m, a in zip(SUPPORT, parameters):
        coefficient = Fraction(a, math.factorial(m))
        coefficients[m] += coefficient
        coefficients[m + 1] -= coefficient
    return coefficients


def reciprocal_coefficients(
    parameters: tuple[int, ...], radius: Fraction
) -> list[QComplex]:
    """Leading-to-constant coefficients of w^D q(radius/w)."""
    phi = phi_coefficients(parameters)
    coefficients: list[QComplex] = []
    for k, value in enumerate(phi):
        if k == 0:
            coefficients.append((Fraction(-1), Fraction(-1)))
        else:
            coefficients.append((value * radius**k, Fraction(0)))
    assert coefficients[-1] != (Fraction(0), Fraction(0))
    return coefficients


def normalized_schur_certificate(
    parameters: tuple[int, ...], radius: Fraction, include_records: bool
) -> tuple[bool, list[dict], int | None]:
    """Apply exact normalized Schur reduction to the reciprocal polynomial."""
    coefficients = reciprocal_coefficients(parameters, radius)
    records: list[dict] = []
    while len(coefficients) > 1:
        degree = len(coefficients) - 1
        leading = coefficients[0]
        coefficients = [qdiv(value, leading) for value in coefficients]
        assert coefficients[0] == (Fraction(1), Fraction(0))
        constant = coefficients[-1]
        gap = Fraction(1) - qnorm(constant)
        if include_records:
            records.append(
                {
                    "degree": degree,
                    "normalized_constant": complex_record(constant),
                    "one_minus_constant_modulus_squared": fraction_record(gap),
                    "gap_is_strictly_positive": gap > 0,
                }
            )
        if gap <= 0:
            return False, records, degree

        reciprocal = [qconj(value) for value in reversed(coefficients)]
        numerator = [
            qsub(value, qmul(constant, star))
            for value, star in zip(coefficients, reciprocal)
        ]
        assert numerator[-1] == (Fraction(0), Fraction(0))
        coefficients = numerator[:-1]

    assert coefficients[0] != (Fraction(0), Fraction(0))
    return True, records, None


def neighboring_lattice_classification() -> dict:
    """Classify the exact +/-1 box at the certified radius."""
    passing: list[dict] = []
    failure_degree_counts: dict[str, int] = {}
    tested = 0
    for offsets in itertools.product((-1, 0, 1), repeat=len(PARAMETERS)):
        parameters = tuple(a + delta for a, delta in zip(PARAMETERS, offsets))
        passed, _, failed_degree = normalized_schur_certificate(
            parameters, CERTIFIED_RADIUS, include_records=False
        )
        tested += 1
        if passed:
            passing.append(
                {
                    "offsets": list(offsets),
                    "parameters": list(parameters),
                }
            )
        else:
            assert failed_degree is not None
            key = str(failed_degree)
            failure_degree_counts[key] = failure_degree_counts.get(key, 0) + 1
    assert tested == 3 ** len(PARAMETERS)
    assert passing == [{"offsets": [0, 0, 0, 0], "parameters": list(PARAMETERS)}]
    return {
        "parameter_order": list(SUPPORT),
        "offset_set_for_each_parameter": [-1, 0, 1],
        "number_tested": tested,
        "number_passing_strict_radius_test": len(passing),
        "passing_records": passing,
        "first_nonpositive_schur_gap_degree_counts": failure_degree_counts,
        "classification_is_exact": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-digits", type=int, default=90)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    passed, schur_records, failed_degree = normalized_schur_certificate(
        PARAMETERS, CERTIFIED_RADIUS, include_records=True
    )
    assert passed and failed_degree is None
    assert [item["degree"] for item in schur_records] == list(range(12, 0, -1))

    phi_coeff = phi_coefficients(PARAMETERS)
    derivative_jets = [
        phi_coeff[k] * math.factorial(k) for k in range(1, len(phi_coeff))
    ]
    assert all(value.denominator == 1 for value in derivative_jets)
    assert sum(phi_coeff) == 1

    z = sp.symbols("z")
    phi = sum(
        sp.Rational(value.numerator, value.denominator) * z**k
        for k, value in enumerate(phi_coeff)
    )
    roots = sp.nroots(phi - (1 + sp.I), n=args.root_digits, maxsteps=1000)
    root_records = sorted(
        [
            {
                "real": str(sp.re(root).evalf(65)),
                "imag": str(sp.im(root).evalf(65)),
                "modulus": str(sp.Abs(root).evalf(70)),
            }
            for root in roots
        ],
        key=lambda item: sp.Float(item["modulus"], 75),
    )

    result = {
        "support_indices": list(SUPPORT),
        "integer_endpoint_jet_parameters": list(PARAMETERS),
        "phi_sparse_formula": (
            "z+46*z^7*(1-z)/7!+213*z^9*(1-z)/9!"
            "-763*z^10*(1-z)/10!+20078*z^11*(1-z)/11!"
        ),
        "phi_expanded_formula": str(sp.expand(phi)),
        "phi_at_zero": str(phi.subs(z, 0)),
        "phi_at_one": str(phi.subs(z, 1)),
        "phi_derivative_jets_1_through_12": [
            value.numerator for value in derivative_jets
        ],
        "reciprocal_polynomial_definition": (
            "P(w)=w^12*(phi((1747/1000)/w)-(1+i))"
        ),
        "normalized_schur_cohn_records": schur_records,
        "all_12_schur_gaps_strictly_positive": True,
        "strict_radius_lower_bound": "1747/1000",
        "exact_neighboring_lattice_classification": (
            neighboring_lattice_classification()
        ),
        "roots_of_phi_equals_1_plus_i_high_precision_diagnostic": root_records,
        "nearest_root_modulus_high_precision_diagnostic": root_records[0]["modulus"],
        "warning": (
            "The Schur--Cohn inequalities and the 3^4 neighboring-lattice "
            "classification are exact. Decimal roots are diagnostics only."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
