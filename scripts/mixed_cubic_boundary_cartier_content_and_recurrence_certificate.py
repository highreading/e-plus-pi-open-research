#!/usr/bin/env python3
"""Exact replay for the mixed-cubic boundary Cartier/content theorem.

All theorem checks use symbolic or exact rational arithmetic.  The final saddle
numbers are explicitly labelled diagnostics and are not used as a proof of an
asymptotic.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY = ROOT / "scripts" / "cubic_and_mixed_cubic_kernel_certificate.py"


def load_parent_module():
    spec = importlib.util.spec_from_file_location("mixed_parent_certificate", DEPENDENCY)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load parent certificate")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = load_parent_module()


def valuation(integer: int, prime: int) -> int:
    if integer == 0:
        return 10**9
    integer = abs(integer)
    output = 0
    while integer % prime == 0:
        integer //= prime
        output += 1
    return output


def rational_valuation(value: Fraction, prime: int) -> int:
    return valuation(value.numerator, prime) - valuation(value.denominator, prime)


def lcm_upto(bound: int) -> int:
    output = 1
    for value in range(1, bound + 1):
        output = lcm(output, value)
    return output


def d_value(n_value: int, power: int, prime: int) -> int:
    remainder_n = n_value % prime
    remainder_k = power % prime
    if remainder_k == 0:
        return 2 * remainder_n
    return 2 * remainder_n + 3 * (prime - remainder_k)


def good_primes(m_value: int) -> list[int]:
    n_value = 6 * m_value
    power = 4 * m_value + 1
    return [
        int(prime)
        for prime in sp.primerange(3, n_value + 1)
        if d_value(n_value, power, int(prime)) <= prime - 2
        and d_value(n_value, power + 1, int(prime)) <= prime - 2
    ]


def symbolic_checks() -> dict[str, bool]:
    x, y, m, v = sp.symbols("x y m v")
    i = sp.I
    u = x * (1 - x)
    q = (1 + x) * (1 + x**2)
    transform = (1 - y) / (1 + y)
    transformed_q = sp.factor(q.subs(x, transform))

    n_value = 6 * m
    power = 4 * m + 1
    a_value = (10 * m + 2) * (10 * m + 3)
    b_value = -(10 * m + 3) * (20 * m + 5)
    c_value = 8 * (2 * m + 1) * (4 * m + 1)
    s_value = -(6 * m + 1) - (10 * m + 3) * (x + x**2 + x**3) - x**4
    recurrence_bracket = sp.expand(
        (n_value + 1) * sp.diff(u, x) * s_value * q
        + u * sp.diff(s_value, x) * q
        - (power + 1) * u * s_value * sp.diff(q, x)
        - (a_value * q**2 + b_value * q + c_value)
    )

    psi = (1 + 2 * v) ** 6 * (1 + (1 - i) * v) ** 6 / (
        v**4 * (1 + v) ** 4
    )
    b0 = (1 + (1 + i) * v) / (1 + v)
    ratio = (1 - i) * (1 + (1 + i) * v) ** 3 / (8 * v * (1 + v))
    saddle_poly = 4 * v**3 + (6 - i) * v**2 - i * v - 1 - i
    h_value = (-1 + i) * (1 + 2 * v) * (1 + (1 - i) * v) / 32
    b2 = (1 - i) * (4 * v**4 + 8 * v**3 + 2 * v**2 - 2 * v - 1) / (
        32 * v * (1 + v) ** 2
    )

    return {
        "mobius_Q_identity": sp.simplify(
            transformed_q - 4 * (1 + y**2) / (1 + y) ** 3
        )
        == 0,
        "three_adjacent_derivative_bracket": recurrence_bracket == 0,
        "psi_log_derivative": sp.simplify(
            sp.diff(psi, v) / psi
            - (2 - 2 * i)
            * saddle_poly
            / (v * (1 + v) * (1 + 2 * v) * (1 + (1 - i) * v))
        )
        == 0,
        "five_eighths_factorization": sp.simplify(
            ratio - sp.Rational(5, 8) - i * saddle_poly / (8 * v * (1 + v))
        )
        == 0,
        "h_times_log_derivative": sp.simplify(
            ratio - sp.Rational(5, 8) - h_value * sp.diff(psi, v) / psi
        )
        == 0,
        "integration_by_parts_amplitude": sp.simplify(
            b2 + v * sp.diff(b0 * h_value / v, v)
        )
        == 0,
    }


def gaussian_residue(m_value: int, shift: int) -> sp.Expr:
    """Simple residue at y=i of the transformed integrand (7)."""
    t = sp.symbols("t")
    i = sp.I
    n_value = 6 * m_value
    power = 4 * m_value + 1 + shift
    degree = power - 1
    extra = 1 + 3 * shift
    numerator = sp.Poly(
        sp.expand(
            (i + t) ** n_value
            * (1 - i - t) ** n_value
            * (1 + i + t) ** extra
        ),
        t,
    )
    answer = sp.S.Zero
    for exponent in range(min(degree, numerator.degree()) + 1):
        coefficient = numerator.coeff_monomial(t**exponent)
        tail = degree - exponent
        answer += (
            coefficient
            * (-1) ** tail
            * sp.binomial(power + tail - 1, tail)
            / (2 * i) ** (power + tail)
        )
    answer *= sp.Rational(1, 2 ** (2 * m_value + 1 + 2 * shift))
    return sp.simplify(answer)


def coefficient_over_one_plus_power(
    numerator: sp.Poly, denominator_power: int, degree: int
) -> sp.Expr:
    """[v^degree] numerator(v)/(1+v)^denominator_power, exactly."""
    v = numerator.gens[0]
    answer = sp.S.Zero
    for exponent in range(min(degree, numerator.degree()) + 1):
        tail = degree - exponent
        answer += (
            numerator.coeff_monomial(v**exponent)
            * (-1) ** tail
            * sp.binomial(denominator_power + tail - 1, tail)
        )
    return sp.simplify(answer)


def contour_integrals(m_value: int) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return C_m,I_0,I_1 in the exact contour formula (39)."""
    v = sp.symbols("v")
    i = sp.I
    common = (1 + 2 * v) ** (6 * m_value) * (1 + (1 - i) * v) ** (
        6 * m_value
    )
    numerator0 = sp.Poly(sp.expand(common * (1 + (1 + i) * v)), v)
    i0 = coefficient_over_one_plus_power(numerator0, 4 * m_value + 1, 4 * m_value)
    numerator1 = sp.Poly(sp.expand(common * (1 + (1 + i) * v) ** 4), v)
    i1 = (1 - i) * coefficient_over_one_plus_power(
        numerator1, 4 * m_value + 2, 4 * m_value + 1
    ) / 8
    c_value = sp.Rational(1, 2 ** (7 * m_value + 2)) * (-1) ** m_value * i**m_value * (
        1 - i
    )
    return sp.simplify(c_value), sp.simplify(i0), sp.simplify(i1)


def exact_row(m_value: int) -> dict[str, object]:
    n_value = 6 * m_value
    power = 4 * m_value + 1
    coordinates = [PARENT.mixed_coordinates(n_value, power + shift) for shift in range(3)]
    r0, l0, e0 = coordinates[0]
    r1, l1, e1 = coordinates[1]
    a_form = l1 * r0 - l0 * r1
    b_form = (l1 * e0 - l0 * e1) / 8
    common = 2 ** (9 * m_value + 5) * lcm_upto(power)
    x_value = a_form * common
    y_value = b_form * common
    if x_value.denominator != 1 or y_value.denominator != 1:
        raise AssertionError((m_value, x_value, y_value))

    individual_clearings = {
        "L0": (l0 * 2 ** (2 * m_value)).denominator == 1,
        "L1": (l1 * 2 ** (2 * m_value + 2)).denominator == 1,
        "E0": (e0 * 2 ** (7 * m_value)).denominator == 1,
        "E1": (e1 * 2 ** (7 * m_value + 2)).denominator == 1,
        "R0": (r0 * 2 ** (7 * m_value + 2) * lcm_upto(4 * m_value)).denominator
        == 1,
        "R1": (r1 * 2 ** (7 * m_value + 4) * lcm_upto(4 * m_value + 1)).denominator
        == 1,
    }
    if not all(individual_clearings.values()):
        raise AssertionError((m_value, individual_clearings))

    coefficient_a = (10 * m_value + 2) * (10 * m_value + 3)
    coefficient_b = -(10 * m_value + 3) * (20 * m_value + 5)
    coefficient_c = 8 * (2 * m_value + 1) * (4 * m_value + 1)
    for coordinate_index in range(3):
        relation = (
            coefficient_a * coordinates[0][coordinate_index]
            + coefficient_b * coordinates[1][coordinate_index]
            + coefficient_c * coordinates[2][coordinate_index]
        )
        if relation != 0:
            raise AssertionError((m_value, coordinate_index, relation))

    next_a = coordinates[2][1] * coordinates[1][0] - coordinates[1][1] * coordinates[2][0]
    next_b = (
        coordinates[2][1] * coordinates[1][2]
        - coordinates[1][1] * coordinates[2][2]
    ) / 8
    if next_a * coefficient_c != a_form * coefficient_a:
        raise AssertionError((m_value, "next A"))
    if next_b * coefficient_c != b_form * coefficient_a:
        raise AssertionError((m_value, "next B"))

    primes = good_primes(m_value)
    product = 1
    local_rows = []
    for prime in primes:
        product *= prime
        valuations = [
            rational_valuation(value, prime)
            for triple in coordinates[:2]
            for value in triple[1:]
        ]
        if min(valuations) < 1:
            raise AssertionError((m_value, prime, valuations))
        if x_value.numerator % prime or y_value.numerator % prime:
            raise AssertionError((m_value, prime, x_value, y_value))
        local_rows.append(
            {
                "p": prime,
                "d0": d_value(n_value, power, prime),
                "d1": d_value(n_value, power + 1, prime),
                "minimum_LE_valuation": min(valuations),
            }
        )
    if gcd(abs(x_value.numerator), abs(y_value.numerator)) % product:
        raise AssertionError((m_value, product))

    band = [int(p) for p in sp.primerange(power + 1, n_value + 1)]
    if not set(band).issubset(primes):
        raise AssertionError((m_value, band, primes))

    middle_band = [int(p) for p in sp.primerange(2 * m_value + 1, 3 * m_value)]
    middle_product = math.prod(middle_band)
    if common % middle_product:
        raise AssertionError((m_value, common, middle_product))
    sharp_common = common // middle_product
    sharp_x = a_form * sharp_common
    sharp_y = b_form * sharp_common
    if sharp_x.denominator != 1 or sharp_y.denominator != 1:
        raise AssertionError((m_value, sharp_x, sharp_y))
    if set(middle_band) & set(primes):
        raise AssertionError((m_value, middle_band, primes))
    middle_rows = []
    for prime in middle_band:
        vector0 = (prime * r0, l0, e0)
        vector1 = (prime * r1, l1, e1)
        minors = (
            vector1[1] * vector0[0] - vector0[1] * vector1[0],
            vector1[2] * vector0[0] - vector0[2] * vector1[0],
            vector1[1] * vector0[2] - vector0[1] * vector1[2],
        )
        if min(rational_valuation(value, prime) for value in minors) < 1:
            raise AssertionError((m_value, prime, minors))
        if rational_valuation(a_form, prime) < 0 or rational_valuation(b_form, prime) < 0:
            raise AssertionError((m_value, prime, a_form, b_form))
        middle_rows.append(
            {
                "p": prime,
                "minimum_relative_Cartier_minor_valuation": min(
                    rational_valuation(value, prime) for value in minors
                ),
                "v_p_A": rational_valuation(a_form, prime),
                "v_p_B": rational_valuation(b_form, prime),
            }
        )
    if gcd(abs(sharp_x.numerator), abs(sharp_y.numerator)) % product:
        raise AssertionError((m_value, "sharp content", product))

    residue_checks = None
    if m_value <= 6:
        c0 = gaussian_residue(m_value, 0)
        c1 = gaussian_residue(m_value, 1)
        contour_c, contour_i0, contour_i1 = contour_integrals(m_value)
        residue_checks = {
            "L0": sp.simplify(4 * sp.re(c0)) == sp.Rational(l0.numerator, l0.denominator),
            "E0": sp.simplify(-4 * sp.im(c0)) == sp.Rational(e0.numerator, e0.denominator),
            "L1": sp.simplify(4 * sp.re(c1)) == sp.Rational(l1.numerator, l1.denominator),
            "E1": sp.simplify(-4 * sp.im(c1)) == sp.Rational(e1.numerator, e1.denominator),
            "B_from_residues": sp.simplify(2 * sp.im(c1 * sp.conjugate(c0)))
            == sp.Rational(b_form.numerator, b_form.denominator),
            "contour_formula_c0": sp.simplify(contour_c * contour_i0 - c0) == 0,
            "contour_formula_c1": sp.simplify(contour_c * contour_i1 - c1) == 0,
        }
        if not all(residue_checks.values()):
            raise AssertionError((m_value, residue_checks, c0, c1))

    return {
        "m": m_value,
        "n": n_value,
        "k": power,
        "all_individual_clearings_pass": all(individual_clearings.values()),
        "common_clearing_A_integral": x_value.denominator == 1,
        "common_clearing_B_integral": y_value.denominator == 1,
        "good_primes": primes,
        "band_primes": band,
        "good_prime_product_divides_content": True,
        "local_exactness_rows": local_rows,
        "middle_band_primes": middle_band,
        "relative_Cartier_middle_band_rows": middle_rows,
        "sharp_common_clearing_A_integral": sharp_x.denominator == 1,
        "sharp_common_clearing_B_integral": sharp_y.denominator == 1,
        "good_prime_product_divides_sharp_content": True,
        "three_adjacent_coordinate_relation": True,
        "next_adjacent_form_is_A_over_C_multiple": True,
        "transformed_residue_checks": residue_checks,
    }


def saddle_diagnostics() -> dict[str, str]:
    mp.mp.dps = 80
    polynomial = lambda value: (
        4 * value**3 + (6 - 1j) * value**2 - 1j * value - 1 - 1j
    )
    tau = mp.findroot(polynomial, mp.mpc("0.39", "0.23"))
    psi = lambda value: (
        (1 + 2 * value) ** 6
        * (1 + (1 - 1j) * value) ** 6
        / (value**4 * (1 + value) ** 4)
    )
    b0 = lambda value: (1 + (1 + 1j) * value) / (1 + value)
    b2 = lambda value: (
        (1 - 1j)
        * (4 * value**4 + 8 * value**3 + 2 * value**2 - 2 * value - 1)
        / (32 * value * (1 + value) ** 2)
    )
    ell = (mp.log(abs(psi(tau))) - 7 * mp.log(2)) / 6

    q = lambda value: (1 + value) * (1 + value**2)
    phase = lambda value: mp.log(value) + mp.log(1 - value) - mp.mpf(2) / 3 * mp.log(q(value))
    derivative = lambda value: 1 / value - 1 / (1 - value) - mp.mpf(2) / 3 * (
        1 + 2 * value + 3 * value**2
    ) / q(value)
    head = mp.findroot(
        derivative,
        (mp.mpf("0.2"), mp.mpf("0.6")),
        solver="bisect",
        tol=mp.mpf("1e-55"),
    )
    phi = phase(head)
    content_constant = -4 * mp.log(2) + mp.pi / mp.sqrt(3) + 3 * mp.log(3)
    height = 2 * ell + mp.mpf(3) / 2 * mp.log(2) + mp.mpf(1) / 2 - content_constant / 6
    decay = ell - phi
    return {
        "warning": "These saddle values are diagnostics and a conditional ledger, not a proved coefficient asymptotic.",
        "tau": mp.nstr(tau, 50),
        "Im_b2_over_b0_at_tau": mp.nstr(mp.im(b2(tau) / b0(tau)), 50),
        "candidate_single_residue_rate_per_n": mp.nstr(ell, 50),
        "rigorous_positive_integral_Laplace_rate_per_n": mp.nstr(phi, 50),
        "conditional_normalized_decay_exponent": mp.nstr(decay, 50),
        "proved_content_PNT_constant_per_m": mp.nstr(content_constant, 50),
        "conditional_height_upper_using_only_proved_arithmetic": mp.nstr(height, 50),
        "conditional_decay_over_height": mp.nstr(decay / height, 50),
        "conditional_positive_margin_per_n": mp.nstr(decay - height, 50),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results" / "mixed_cubic_boundary_cartier_content_and_recurrence_certificate.json",
    )
    parser.add_argument("--max-m", type=int, default=36)
    args = parser.parse_args()

    mp.mp.dps = 80
    symbolic = symbolic_checks()
    if not all(symbolic.values()):
        raise AssertionError(symbolic)
    rows = [exact_row(m_value) for m_value in range(1, args.max_m + 1)]
    source_constant = sum(
        (mp.mpf(2) / ((2 * index + 1) * (3 * index + 1)) for index in range(200000)),
        mp.mpf(0),
    )
    closed_constant = -4 * mp.log(2) + mp.pi / mp.sqrt(3) + 3 * mp.log(3)
    if abs(source_constant - closed_constant) > mp.mpf("1e-5"):
        raise AssertionError((source_constant, closed_constant))

    payload_object = {
        "schema": "mixed-cubic-boundary-cartier-content-v1",
        "dependency": str(DEPENDENCY.relative_to(ROOT)),
        "dependency_sha256": hashlib.sha256(DEPENDENCY.read_bytes()).hexdigest(),
        "symbolic_checks": symbolic,
        "exact_rows": rows,
        "interval_length_constant": {
            "closed_form": "-4*log(2)+pi/sqrt(3)+3*log(3)",
            "decimal": mp.nstr(closed_constant, 50),
            "partial_sum_200000": mp.nstr(source_constant, 50),
        },
        "saddle_diagnostics_and_conditional_ledger": saddle_diagnostics(),
        "warnings": [
            "The dyadic/lcm clearing, exactness criterion, content divisibility, prime-density constant, recurrence, and contour integration-by-parts identity are exact theorems.",
            "Finite exact rows certify the implementation but are not used to extrapolate an all-parameter theorem.",
            "The selected complex saddle has not been proved uniquely accessible/dominant; all residue-rate and normalized-exponent values are explicitly conditional.",
            "The sharpened proved arithmetic plus the conditional saddle rate gives a ratio slightly above one; the required accessible-saddle theorem remains unproved.",
            "Nothing in this package proves or disproves that e+pi is transcendental.",
        ],
    }
    payload = json.dumps(payload_object, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(hashlib.sha256(payload.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
