#!/usr/bin/env python3
"""Exact diagonal HP diagnostic for the nonpolynomial integral-Hurwitz map.

The G jets are generated independently of the rational-derivative recurrence
used by earlier pullback probes:

1. compute every phi derivative jet from the closed integer formula for
   z^m(z-1)exp(a z)/m!;
2. convert to the ordinary Taylor series of phi;
3. generate the ordinary Taylor series of F from
   (2-2w+w^2)F'(w)=4; and
4. compose the two series by exact rational convolution.

The generic exact endpoint-matched HP record routine is then used for
1<=n<=15.  This is a finite diagnostic, not an all-degree theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

from composed_integral_pullback_hp_probe import record
from mobius_arctan_hp_probe import e_plus_pi_interval


sys.set_int_max_str_digits(0)


BASE_TERMS = [(7, 46), (9, 213), (10, -762), (11, 20073)]
EXPONENTIAL_TERMS = [
    (15, -1, 1215540),
    (26, -1, 65574371633155024),
    (40, 1, 40126919362525583214229456433446912),
]


def vector_sha256(values: list[int]) -> str:
    return hashlib.sha256(
        json.dumps(values, separators=(",", ":")).encode()
    ).hexdigest()


def phi_jets(maximum: int) -> list[int]:
    jets = [0] * (maximum + 1)
    if maximum >= 1:
        jets[1] = 1
    for m, coefficient in BASE_TERMS:
        if m <= maximum:
            jets[m] += coefficient
        if m + 1 <= maximum:
            jets[m + 1] -= (m + 1) * coefficient
    for m, a, k in EXPONENTIAL_TERMS:
        if m <= maximum:
            jets[m] -= k
        for n in range(m + 1, maximum + 1):
            r = n - m
            jets[n] += k * math.comb(n, m) * (
                r * a ** (r - 1) - a**r
            )
    return jets


def multiply_truncated(
    left: list[Fraction], right: list[Fraction], maximum: int
) -> list[Fraction]:
    result = [Fraction(0)] * (maximum + 1)
    for j, x in enumerate(left):
        if not x:
            continue
        for k, y in enumerate(right):
            if j + k > maximum:
                break
            if y:
                result[j + k] += x * y
    return result


def f_ordinary_coefficients(maximum: int) -> list[Fraction]:
    derivative: list[Fraction] = []
    for n in range(maximum):
        rhs = Fraction(4 if n == 0 else 0)
        if n >= 1:
            rhs += 2 * derivative[n - 1]
        if n >= 2:
            rhs -= derivative[n - 2]
        derivative.append(rhs / 2)
    return [Fraction(0)] + [
        derivative[n] / (n + 1) for n in range(maximum)
    ]


def composed_g_jets(maximum: int) -> tuple[list[int], list[int]]:
    p_jets = phi_jets(maximum)
    phi = [
        Fraction(p_jets[n], math.factorial(n)) for n in range(maximum + 1)
    ]
    f = f_ordinary_coefficients(maximum)
    composition = [Fraction(0)] * (maximum + 1)
    power = [Fraction(0)] * (maximum + 1)
    power[0] = Fraction(1)
    for k in range(1, maximum + 1):
        power = multiply_truncated(power, phi, maximum)
        if f[k]:
            for n in range(maximum + 1):
                composition[n] += f[k] * power[n]
    jets: list[int] = []
    for n, coefficient in enumerate(composition):
        value = coefficient * math.factorial(n)
        assert value.denominator == 1
        jets.append(value.numerator)
    return p_jets, jets


def derivative_equation_g_jets(
    p_jets: list[int], maximum: int
) -> list[int]:
    """Independent exact reconstruction from

        (phi**2 - 2*phi + 2) G' = 4 phi'.

    This does not use the F-series or series-composition route above.
    """
    phi = [
        Fraction(p_jets[n], math.factorial(n))
        for n in range(maximum + 1)
    ]
    denominator = multiply_truncated(phi, phi, maximum)
    denominator[0] += 2
    for n in range(maximum + 1):
        denominator[n] -= 2 * phi[n]
    assert denominator[0] == 2

    derivative: list[Fraction] = []
    for n in range(maximum):
        rhs = 4 * (n + 1) * phi[n + 1]
        for j in range(1, n + 1):
            rhs -= denominator[j] * derivative[n - j]
        derivative.append(rhs / denominator[0])

    ordinary = [Fraction(0)] + [
        derivative[n] / (n + 1) for n in range(maximum)
    ]
    jets: list[int] = []
    for n, coefficient in enumerate(ordinary):
        value = coefficient * math.factorial(n)
        assert value.denominator == 1
        jets.append(value.numerator)
    return jets


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=15)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    maximum_jet = 3 * args.max_n + 1
    p_jets, g_jets = composed_g_jets(maximum_jet)
    independent_g_jets = derivative_equation_g_jets(
        p_jets, maximum_jet
    )
    assert independent_g_jets == g_jets
    interval = e_plus_pi_interval()
    records = [
        record(n, g_jets, interval) for n in range(1, args.max_n + 1)
    ]
    result = {
        "candidate": (
            "phi from sources/nonpolynomial_integral_hurwitz_pullback.md; "
            "G=4*atan(phi/(2-phi))"
        ),
        "maximum_computed_jet": maximum_jet,
        "phi_jets_sha256": vector_sha256(p_jets),
        "G_jets_sha256": vector_sha256(g_jets),
        "independent_derivative_equation_G_jets_sha256": vector_sha256(
            independent_g_jets
        ),
        "independent_G_jet_vectors_agree": independent_g_jets == g_jets,
        "all_computed_phi_and_G_jets_integral": True,
        "jet_generation": (
            "closed integer phi-jet formula plus exact ordinary-series "
            "composition with F"
        ),
        "records": records,
        "endpoint_decades": [
            item.get("endpoint_interval_certificate", {}).get(
                "single_certified_base10_decade"
            )
            for item in records
        ],
        "warning": (
            "Finite exact diagnostic only; no all-degree rank, height, "
            "content, nonvanishing, or asymptotic conclusion."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
