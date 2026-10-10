#!/usr/bin/env python3
"""Exact checks for Item 175's fixed-band five-divisor analysis.

The all-j nonidentity theorem is proved symbolically in the companion report.
This standard-library checker supplies three independent finite audits:

* exact rational/Gaussian partial-fraction coordinates for F_j and F_j/(x-a);
* the polynomial exactness obstruction obtained after the Cayley transform;
* the exact-coefficient versus reduced-Cartier-scalar convention at (p,s)=(107,15).

Finite scans in this file are diagnostics, not substitutes for the all-j proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item175_fixed_band_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item175_fixed_band_certificate.json"
)

G = tuple[Fraction, Fraction]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))
I: G = (Fraction(0), Fraction(1))
ROOTS: tuple[G, G, G] = ((Fraction(-1), Fraction(0)), I, (Fraction(0), Fraction(-1)))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def g(value: int | Fraction) -> G:
    return Fraction(value), Fraction(0)


def gadd(left: G, right: G) -> G:
    return left[0] + right[0], left[1] + right[1]


def gneg(value: G) -> G:
    return -value[0], -value[1]


def gsub(left: G, right: G) -> G:
    return gadd(left, gneg(right))


def gmul(left: G, right: G) -> G:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gscale(value: G, scalar: int | Fraction) -> G:
    scalar = Fraction(scalar)
    return value[0] * scalar, value[1] * scalar


def ginv(value: G) -> G:
    norm = value[0] * value[0] + value[1] * value[1]
    if not norm:
        raise ZeroDivisionError(value)
    return value[0] / norm, -value[1] / norm


def gpow(value: G, exponent: int) -> G:
    if exponent < 0:
        return gpow(ginv(value), -exponent)
    answer = ONE
    while exponent:
        if exponent & 1:
            answer = gmul(answer, value)
        value = gmul(value, value)
        exponent >>= 1
    return answer


def polynomial_multiply(left: list[G], right: list[G], degree: int) -> list[G]:
    answer = [ZERO] * (degree + 1)
    for first, left_value in enumerate(left[: degree + 1]):
        for second, right_value in enumerate(right[: degree - first + 1]):
            answer[first + second] = gadd(
                answer[first + second], gmul(left_value, right_value)
            )
    return answer


def polynomial_power(base: list[G], exponent: int, degree: int) -> list[G]:
    answer = [ONE] + [ZERO] * degree
    while exponent:
        if exponent & 1:
            answer = polynomial_multiply(answer, base, degree)
        exponent >>= 1
        if exponent:
            base = polynomial_multiply(base, base, degree)
    return answer


def series_inverse(base: list[G], degree: int) -> list[G]:
    inverse_constant = ginv(base[0])
    answer = [inverse_constant] + [ZERO] * degree
    for n in range(1, degree + 1):
        total = ZERO
        for k in range(1, min(n, len(base) - 1) + 1):
            total = gadd(total, gmul(base[k], answer[n - k]))
        answer[n] = gneg(gmul(inverse_constant, total))
    return answer


def linear_factor_at(alpha: G, beta: G) -> list[G]:
    """Series of x-beta at x=alpha+y."""
    return [gsub(alpha, beta), ONE]


def coordinates(j: int, extra_divisor: G | None = None) -> tuple[G, G, G]:
    """Return exact (R,L,E) of F_j/(x-a) dx over Q(i).

    ``extra_divisor=None`` means F_j itself.  Otherwise it means division by
    x-a.  Principal parts at -1,i,-i give every coordinate.  All rational
    parts come from pole orders at least two; the input is proper at infinity.
    """
    if j < 1:
        raise ValueError(j)
    numerator_exponent = 3 * j + 2
    pole_order = 2 * j + 2
    residues: list[G] = []
    rational_coordinate = ZERO

    for alpha in ROOTS:
        order = pole_order + int(extra_divisor == alpha)
        degree = order - 1

        # u(alpha+y)=(alpha+y)(1-alpha-y).
        numerator_base = polynomial_multiply(
            [alpha, ONE], [gsub(ONE, alpha), g(-1)], degree
        )
        numerator = polynomial_power(numerator_base, numerator_exponent, degree)

        regular_denominator = [ONE] + [ZERO] * degree
        for beta in ROOTS:
            exponent = pole_order + int(extra_divisor == beta)
            if beta == alpha:
                continue
            regular_denominator = polynomial_multiply(
                regular_denominator,
                polynomial_power(linear_factor_at(alpha, beta), exponent, degree),
                degree,
            )
        if extra_divisor is not None and extra_divisor not in ROOTS:
            regular_denominator = polynomial_multiply(
                regular_denominator,
                linear_factor_at(alpha, extra_divisor),
                degree,
            )

        regular_series = polynomial_multiply(
            numerator, series_inverse(regular_denominator, degree), degree
        )
        principal = {
            n: regular_series[order - n] for n in range(1, order + 1)
        }
        residues.append(principal[1])

        for n, coefficient in principal.items():
            if n == 1:
                continue
            endpoint_factor = gsub(
                gpow(gneg(alpha), 1 - n),
                gpow(gsub(ONE, alpha), 1 - n),
            )
            rational_coordinate = gadd(
                rational_coordinate,
                gscale(gmul(coefficient, endpoint_factor), Fraction(1, n - 1)),
            )

    residue_minus_one, residue_i, residue_minus_i = residues
    logarithmic_coordinate = gadd(
        gscale(residue_minus_one, 4),
        gscale(gadd(residue_i, residue_minus_i), 2),
    )
    circular_coordinate = gmul(
        (Fraction(0), Fraction(2)), gsub(residue_i, residue_minus_i)
    )
    return rational_coordinate, logarithmic_coordinate, circular_coordinate


def wedge(left: tuple[G, G, G], right: tuple[G, G, G], first: int, second: int) -> G:
    return gsub(gmul(left[first], right[second]), gmul(left[second], right[first]))


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rational(value: G) -> Fraction:
    if value[1]:
        raise AssertionError(("expected rational Gaussian value", value))
    return value[0]


def coordinate_checks(max_full_j: int, max_divisor_j: int) -> dict[str, Any]:
    rows = []
    full_nonzero_failures = []
    for j in range(1, max_divisor_j + 1):
        base = coordinates(j)
        zero_divisor = coordinates(j, g(0))
        one_divisor = coordinates(j, g(1))
        weight_a0 = rational(wedge(base, zero_divisor, 0, 1))
        weight_b0 = rational(wedge(base, zero_divisor, 2, 1))
        weight_a1 = rational(wedge(base, one_divisor, 0, 1))
        weight_b1 = rational(wedge(base, one_divisor, 2, 1))
        if not weight_a0 or not weight_b0 or not weight_a1 or not weight_b1:
            raise AssertionError(
                ("zero/one-divisor weight", j, weight_a0, weight_b0, weight_a1, weight_b1)
            )
        row: dict[str, Any] = {
            "j": j,
            "v_j": [fraction_text(rational(value)) for value in base],
            "weight_A_at_0": fraction_text(weight_a0),
            "weight_B_at_0": fraction_text(weight_b0),
            "weight_A_at_1": fraction_text(weight_a1),
            "weight_B_at_1": fraction_text(weight_b1),
        }
        if j <= max_full_j:
            weights = {}
            for name, divisor in (
                ("0", g(0)),
                ("1", g(1)),
                ("-1", g(-1)),
                ("i", I),
                ("-i", gneg(I)),
            ):
                target = coordinates(j, divisor)
                weight_a = wedge(base, target, 0, 1)
                weight_b = wedge(base, target, 2, 1)
                if weight_a == ZERO or weight_b == ZERO:
                    full_nonzero_failures.append((j, name, weight_a, weight_b))
                weights[name] = {
                    "A": [fraction_text(weight_a[0]), fraction_text(weight_a[1])],
                    "B": [fraction_text(weight_b[0]), fraction_text(weight_b[1])],
                }
            row["all_five_weights_over_Q_i"] = weights
        rows.append(row)
    if full_nonzero_failures:
        raise AssertionError(full_nonzero_failures[:3])
    return {
        "full_five_divisor_range": [1, max_full_j],
        "zero_and_one_divisor_range": [1, max_divisor_j],
        "all_A_and_B_weights_nonzero_on_full_range": True,
        "A_and_B_at_0_and_1_nonzero_on_extended_range": True,
        "rows": rows,
    }


def obstruction_resultant(j: int) -> dict[str, Any]:
    """Finite recurrence audit for exactness of (F_j/(x-1)-lambda F_j)dx.

    After y=(x+1)/(1-x), exactness would require

      D R'-(K-1)D'R=N_lambda,

    with D=y(1+y^2), deg R<=3j.  Coefficients are stored as affine forms
    constant + lambda*L + free*T.  Two T-free obstruction rows result.
    """
    a_value = 3 * j + 2
    k_value = 2 * j + 2
    degree = a_value - 1

    numerator: list[tuple[Fraction, Fraction, Fraction]] = []
    for n in range(degree + 3):
        def coefficient(index: int) -> int:
            if 0 <= index <= a_value:
                return (-1) ** index * math.comb(a_value, index)
            return 0

        # Twice the transformed numerator:
        # (1-y)^A * (-(1+y) - 2*lambda).
        numerator.append(
            (
                Fraction(-coefficient(n) - coefficient(n - 1)),
                Fraction(-2 * coefficient(n)),
                Fraction(0),
            )
        )

    solution: dict[int, tuple[Fraction, Fraction, Fraction]] = {}
    t_free_obstructions: list[tuple[Fraction, Fraction, Fraction]] = []
    all_obstructions = []
    for n in range(degree + 3):
        previous = solution.get(n - 2, (Fraction(0),) * 3)
        off_diagonal = n - 2 - 3 * (k_value - 1)
        rhs = tuple(
            numerator[n][index] - off_diagonal * previous[index]
            for index in range(3)
        )
        diagonal = n - (k_value - 1)
        if n <= degree and diagonal:
            solution[n] = tuple(value / diagonal for value in rhs)
        elif n <= degree:
            all_obstructions.append(("resonance", rhs))
            if rhs[2] == 0:
                t_free_obstructions.append(rhs)
            solution[n] = (Fraction(0), Fraction(0), Fraction(1))
        else:
            all_obstructions.append(("top", rhs))
            if rhs[2] == 0:
                t_free_obstructions.append(rhs)

    if len(t_free_obstructions) != 2:
        raise AssertionError((j, t_free_obstructions, all_obstructions))
    first, second = t_free_obstructions
    resultant = first[1] * second[0] - second[1] * first[0]
    return {
        "j": j,
        "first_obstruction": [fraction_text(first[0]), fraction_text(first[1])],
        "second_obstruction": [fraction_text(second[0]), fraction_text(second[1])],
        "resultant": fraction_text(resultant),
        "resultant_positive": resultant > 0,
    }


def polynomial_obstruction_checks(max_j: int) -> dict[str, Any]:
    rows = [obstruction_resultant(j) for j in range(1, max_j + 1)]
    if not all(row["resultant_positive"] for row in rows):
        raise AssertionError("nonpositive finite obstruction resultant")

    # D(1+t)=2+4t+3t^2+t^3 has strictly positive coefficients.  The
    # coefficient used in the all-j proof is therefore positive.  These
    # finite exact coefficients are only a replay of that symbolic fact.
    positivity = []
    for j in range(1, max_j + 1):
        exponent = 2 * j + 1
        target = 3 * j + 1
        polynomial = [1]
        base = [2, 4, 3, 1]
        for _ in range(exponent):
            next_polynomial = [0] * (len(polynomial) + 3)
            for left_index, left_value in enumerate(polynomial):
                for right_index, right_value in enumerate(base):
                    next_polynomial[left_index + right_index] += left_value * right_value
            polynomial = next_polynomial
        coefficient = polynomial[target]
        if coefficient <= 0:
            raise AssertionError((j, coefficient))
        positivity.append({"j": j, "coefficient": str(coefficient)})
    return {
        "range": [1, max_j],
        "all_recurrence_resultants_positive": True,
        "all_D_power_coefficients_positive": True,
        "rows": rows,
        "D_power_coefficients": positivity,
    }


def generalized_binomial(integer: int, degree: int) -> int:
    if degree < 0:
        return 0
    if integer >= 0:
        return math.comb(integer, degree) if degree <= integer else 0
    return (-1) ** degree * math.comb(-integer + degree - 1, degree)


def four_section_exact(linear_exponent: int, four_exponent: int, degree: int) -> int:
    total = 0
    for v in range(four_exponent + 1):
        linear_degree = degree - 4 * v
        if linear_degree < 0:
            break
        total += (
            (-1) ** (v + linear_degree)
            * math.comb(four_exponent, v)
            * generalized_binomial(linear_exponent, linear_degree)
        )
    return total


def exact_scalar_convention_witness() -> dict[str, Any]:
    p, s = 107, 15
    r_value = p - 3 * s - 3
    h_value = 2 * s + 1
    degree = 3 * s + 2
    exact_gamma0 = four_section_exact(r_value - h_value, h_value, degree)
    exact_gamma1 = four_section_exact(r_value - h_value + 1, h_value - 1, degree)
    reduced_gamma0 = exact_gamma0 % p
    reduced_gamma1 = exact_gamma1 % p
    resonant_coefficient_for_reduced_lifts = (
        reduced_gamma1 * exact_gamma0 - reduced_gamma0 * exact_gamma1
    )
    if resonant_coefficient_for_reduced_lifts % p:
        raise AssertionError("Cartier-lift resonance is not p-divisible")
    omitted_xp_coefficient = resonant_coefficient_for_reduced_lifts // p
    if omitted_xp_coefficient % p != 61:
        raise AssertionError(omitted_xp_coefficient)
    return {
        "p": p,
        "s": s,
        "exact_integer_coefficients": [exact_gamma0, exact_gamma1],
        "Cartier_reductions": [reduced_gamma0, reduced_gamma1],
        "exact_lift_resonant_coefficient": 0,
        "reduced_representative_resonant_coefficient": resonant_coefficient_for_reduced_lifts,
        "reduced_representative_resonant_coefficient_divided_by_p": omitted_xp_coefficient,
        "omitted_xp_coefficient_mod_p": omitted_xp_coefficient % p,
        "interpretation": (
            "Exact integer coefficients make the x^(p-1) coefficient vanish "
            "exactly. Canonical reduced representatives require the displayed "
            "nonzero x^p primitive term."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--full-five-divisor-j", type=int, default=12)
    parser.add_argument("--coordinate-j", type=int, default=24)
    parser.add_argument("--obstruction-j", type=int, default=200)
    args = parser.parse_args()

    output = {
        "schema": "item175-fixed-band-five-divisor-v1",
        "status": {
            "exact_scalar_convention": "PROVED_IN_COMPANION_REPORT_AND_EXACTLY_REPLAYED",
            "B_weight_at_one_nonzero_for_every_fixed_j": "PROVED_IN_COMPANION_REPORT",
            "A_weight_at_one_all_j": "OPEN; FINITE_EXACT_REPLAY_ONLY",
            "actual_moving_T_value_nonvanishing": "OPEN",
        },
        "exact_scalar_convention_witness": exact_scalar_convention_witness(),
        "exact_coordinate_checks": coordinate_checks(
            args.full_five_divisor_j, args.coordinate_j
        ),
        "polynomial_exactness_obstruction": polynomial_obstruction_checks(
            args.obstruction_j
        ),
        "scope": {
            "all_j_theorem": (
                "For every j>=1, w_B(j,1)=E(F_j)L(F_j/(x-1))-L(F_j)E(F_j/(x-1)) "
                "is a nonzero rational number. Hence its formal five-divisor "
                "coefficient is nonzero modulo every prime outside a finite "
                "j-dependent exceptional set."
            ),
            "not_proved": (
                "The constrained values T(a) coming from P0,P1 need not realize "
                "an arbitrary five-tuple; no actual-prime nonvanishing or density "
                "statement follows."
            ),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "coordinate_j": args.coordinate_j,
                "full_five_divisor_j": args.full_five_divisor_j,
                "obstruction_j": args.obstruction_j,
                "output_sha256": sha256(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
