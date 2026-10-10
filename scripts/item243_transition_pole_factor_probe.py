#!/usr/bin/env python3
"""Exact factorization of Item 243 primitive transition denominators."""

from __future__ import annotations

import json
from pathlib import Path

from sympy import Poly, Rational, factor_list, symbols


HERE = Path(__file__).resolve().parent
n = symbols("n")


def polynomial(coefficients):
    return Poly(
        sum(Rational(a, b) * n**degree for degree, (a, b) in enumerate(coefficients)),
        n,
        domain="QQ",
    )


def recurrence_block(data, residue, name, order, degree, shift):
    flat = data["recurrences"][f"r{residue}_{name}"]
    return polynomial(flat[shift * (degree + 1) : (shift + 1) * (degree + 1)])


def relation_blocks(data, residue, key, orders, degree):
    flat = data["relations"][f"r{residue}_{key}"]
    answer = []
    cursor = 0
    for order in orders:
        part = []
        for _ in range(order + 1):
            part.append(polynomial(flat[cursor : cursor + degree + 1]))
            cursor += degree + 1
        answer.append(part)
    return answer


def encode_factorization(poly):
    scalar, factors = factor_list(poly.as_expr(), n)
    factor_entries = []
    for factor, multiplicity in factors:
        current = Poly(factor, n, domain="QQ")
        coefficients = current.all_coeffs()
        if current.LC() < 0:
            coefficients = [-value for value in coefficients]
        positive_coefficients = all(value > 0 for value in coefficients)
        if not positive_coefficients:
            raise AssertionError((str(factor), "not coefficient-positive"))
        factor_entries.append(
            {
                "factor": str(factor),
                "degree": current.degree(),
                "multiplicity": multiplicity,
                "all_coefficients_strictly_positive_after_sign_normalization": True,
            }
        )
    return {
        "degree": poly.degree(),
        "scalar": str(scalar),
        "factors": factor_entries,
        "nonzero_for_every_integer_n_ge_0": True,
    }


def main():
    recurrences = json.loads((HERE / "item243_univariate_recurrence_probe.json").read_text())
    relations = json.loads((HERE / "item243_cross_reconstruct.json").read_text())
    result = {
        "classification": "PROVED_EXACT_NO_NONNEGATIVE_TRANSITION_POLES",
        "logic": (
            "Every irreducible factor, after normalizing its sign, has all "
            "coefficients strictly positive. Therefore it is positive for "
            "every real n>=0. The displayed nonzero rational scalar fixes "
            "the sign but cannot create a zero. The same conclusion holds "
            "after every transition shift n->n+s, s>=0."
        ),
        "remaining_structural_denominators": (
            "rho has denominator 864(h+1)(h+2)(2h+1)^2(2h+3)"
            "(2h+5)^2(4h+3), and scalar/y factors use 4h+3; all are "
            "strictly positive for h=3n+r>=1."
        ),
        "residues": [],
    }
    for residue in (1, 2):
        xu_x, xu_u = relation_blocks(relations, residue, "xu", (1, 1), 7)
        yv_y, yv_v = relation_blocks(relations, residue, "yv", (0, 2), 12)
        entries = {
            "x_companion_leading": recurrence_block(recurrences, residue, "x", 4, 15, 4),
            "v_companion_leading": recurrence_block(recurrences, residue, "v", 3, 16, 3),
            "xu_u_shift_leading": xu_u[1],
            "yv_y_coefficient": yv_y[0],
        }
        result["residues"].append(
            {
                "residue": residue,
                "primitive_transition_denominators": {
                    name: encode_factorization(value) for name, value in entries.items()
                },
                "all_transition_denominators_nonzero_for_n_ge_0": True,
            }
        )
    output = HERE / "item243_transition_pole_factor_probe.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
