#!/usr/bin/env python3
"""Exact Schur--Cohn certificate for an improved integral-jet pi pullback.

The polynomial

    phi(z)=z-z^3/6+5z^4/24-z^5/24

has integral derivative jets and fixes 0 and 1.  Composing the established
integral-jet function 4*atan(w/(2-w)) with phi therefore preserves integral
jets.  This script exactly certifies that every solution of
phi(z)=1+i (and hence also phi(z)=1-i) lies outside |z|=sqrt(2).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

from composed_integral_pullback_hp_probe import PHI, composed_jets


def schur_cohn_gaps() -> tuple[list[sp.Rational], sp.Expr]:
    z, w = sp.symbols("z w")
    radius = sp.sqrt(2)
    phi = sum(
        sp.Rational(value.numerator, value.denominator) * z**k
        for k, value in enumerate(PHI)
    )
    q = sp.Poly(phi - (1 + sp.I), z)
    degree = q.degree()
    polynomial = sp.Poly(
        sp.expand(w**degree * q.as_expr().subs(z, radius / w)),
        w,
        extension=[sp.I, radius],
    )
    initial = polynomial.as_expr()
    gaps: list[sp.Rational] = []
    while polynomial.degree() > 0:
        coefficients = polynomial.all_coeffs()
        n = polynomial.degree()
        leading = coefficients[0]
        constant = coefficients[-1]
        gap = sp.simplify(sp.conjugate(leading) * leading - sp.conjugate(constant) * constant)
        assert gap.is_Rational and gap > 0
        gaps.append(sp.Rational(gap))
        reciprocal = sum(
            sp.conjugate(coefficients[n - j]) * w ** (n - j)
            for j in range(n + 1)
        )
        transformed = sp.Poly(
            sp.expand(sp.conjugate(leading) * polynomial.as_expr() - constant * reciprocal),
            w,
            extension=[sp.I, radius],
        )
        assert transformed.nth(0) == 0
        polynomial = sp.Poly(
            sp.cancel(transformed.as_expr() / w),
            w,
            extension=[sp.I, radius],
        )
    return gaps, initial


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jet-order", type=int, default=100)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    gaps, initial = schur_cohn_gaps()
    jets = composed_jets(args.jet_order)

    z = sp.symbols("z")
    phi = sum(
        sp.Rational(value.numerator, value.denominator) * z**k
        for k, value in enumerate(PHI)
    )
    roots = sp.nroots(phi - (1 + sp.I), n=60, maxsteps=300)
    root_records = [
        {
            "real": str(sp.re(root).evalf(50)),
            "imag": str(sp.im(root).evalf(50)),
            "modulus": str(sp.Abs(root).evalf(50)),
        }
        for root in roots
    ]
    result = {
        "phi": "z-z^3/6+5*z^4/24-z^5/24",
        "phi_at_zero": str(phi.subs(z, 0)),
        "phi_at_one": str(phi.subs(z, 1)),
        "phi_derivative_jets": [
            int(sp.diff(phi, z, k).subs(z, 0)) for k in range(1, 6)
        ],
        "reciprocal_polynomial_at_radius_sqrt2": str(initial),
        "schur_cohn_positive_gaps": [
            {"numerator": int(gap.p), "denominator": int(gap.q)}
            for gap in gaps
        ],
        "strict_radius_lower_bound": "sqrt(2)",
        "roots_of_phi_equals_1_plus_i_high_precision_diagnostic": root_records,
        "computed_composite_jet_order": args.jet_order,
        "all_computed_composite_jets_integral": all(
            isinstance(value, int) for value in jets
        ),
        "computed_composite_jets_sha256": hashlib.sha256(
            json.dumps(jets, separators=(",", ":")).encode()
        ).hexdigest(),
        "warning": (
            "The Schur--Cohn radius inequality is exact. Decimal root values "
            "and the finite jet recomputation are diagnostics; all-order jet "
            "integrality follows separately from Faa di Bruno."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
