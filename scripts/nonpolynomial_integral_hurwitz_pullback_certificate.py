#!/usr/bin/env python3
"""Exact zero-free-disk certificate for an entire integral-Hurwitz pullback.

The endpoint map is a polynomial integral-Hurwitz base plus three terms

    (k/m!) z^m (z-1) exp(a z),  a in {-1, 1}, k,m integers.

Each term fixes 0 and 1 and has integer derivative jets at zero.  To prove
that phi(z) avoids 1+i in |z| <= 707/400, this program:

1. truncates each exponential after degree 20, obtaining an exact degree-61
   Gaussian-rational polynomial q_N;
2. applies a fraction-free Schur--Cohn recursion to
   w^61 q_N((707/400)/w), proving that q_N has no zeros in the disk;
3. derives an exact boundary lower bound from rational dyadic upper bounds
   for every Schur reflection coefficient; and
4. proves that this lower bound exceeds an exact exponential-tail bound.

Rouche's theorem then proves that the original entire q=phi-(1+i) is
zero-free in the closed disk.  Real coefficients give the same result for
1-i.  Decimal roots and argument-principle samples are diagnostics only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from math import factorial, gcd, isqrt, lcm
from pathlib import Path

import mpmath as mp
import numpy as np


sys.set_int_max_str_digits(0)


BASE_TERMS = [
    # (m, K) means (K/m!) z^m (1-z).
    (7, 46),
    (9, 213),
    (10, -762),
    (11, 20073),
]

EXPONENTIAL_TERMS = [
    # (m, a, k) means (k/m!) z^m (z-1) exp(a z).
    (15, -1, 1215540),
    (26, -1, 65574371633155024),
    (40, 1, 40126919362525583214229456433446912),
]

RADIUS = Fraction(707, 400)
EXPONENTIAL_TRUNCATION_DEGREE = 20
DYADIC_BITS = 128


GaussianInteger = tuple[int, int]


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def integer_sha256(value: int) -> str:
    return hashlib.sha256(str(value).encode()).hexdigest()


def vector_sha256(values: list[int]) -> str:
    rendered = json.dumps(values, separators=(",", ":")).encode()
    return hashlib.sha256(rendered).hexdigest()


def gaussian_state_sha256(values: list[GaussianInteger]) -> str:
    digest = hashlib.sha256()
    for real, imag in values:
        for value in (real, imag):
            sign = b"-" if value < 0 else b"+"
            magnitude = abs(value)
            length = max(1, (magnitude.bit_length() + 7) // 8)
            digest.update(sign)
            digest.update(length.to_bytes(8, "big"))
            digest.update(magnitude.to_bytes(length, "big"))
    return digest.hexdigest()


def gmul(left: GaussianInteger, right: GaussianInteger) -> GaussianInteger:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gconj(value: GaussianInteger) -> GaussianInteger:
    return value[0], -value[1]


def gsub(left: GaussianInteger, right: GaussianInteger) -> GaussianInteger:
    return left[0] - right[0], left[1] - right[1]


def gnorm(value: GaussianInteger) -> int:
    return value[0] * value[0] + value[1] * value[1]


def primitive_gaussian(values: list[GaussianInteger]) -> tuple[list[GaussianInteger], int]:
    content = 0
    for real, imag in values:
        content = gcd(content, abs(real))
        content = gcd(content, abs(imag))
    assert content > 0
    if content > 1:
        values = [(real // content, imag // content) for real, imag in values]
    return values, content


def ceil_sqrt_ratio_scaled(numerator: int, denominator: int, bits: int) -> int:
    """Smallest u with (u/2^bits)^2 >= numerator/denominator."""
    assert 0 <= numerator < denominator
    scale = 1 << bits
    scaled_numerator = numerator * scale * scale
    quotient = scaled_numerator // denominator
    upper = isqrt(quotient)
    if upper * upper * denominator < scaled_numerator:
        upper += 1
    assert upper * upper * denominator >= scaled_numerator
    assert 0 <= upper < scale
    return upper


def integral_hurwitz_jets(maximum: int) -> list[int]:
    """Compute derivative jets from the closed integer formulas."""
    jets = [0] * (maximum + 1)
    if maximum >= 1:
        jets[1] = 1
    for m, coefficient in BASE_TERMS:
        if m <= maximum:
            jets[m] += coefficient
        if m + 1 <= maximum:
            jets[m + 1] -= coefficient * (m + 1)
    for m, a, k in EXPONENTIAL_TERMS:
        if m <= maximum:
            jets[m] -= k
        for n in range(m + 1, maximum + 1):
            r = n - m
            jets[n] += k * math.comb(n, m) * (
                r * a ** (r - 1) - a**r
            )
    assert all(isinstance(value, int) for value in jets)
    return jets


def truncated_q_coefficients(
    truncation_degree: int,
) -> tuple[list[Fraction], list[Fraction]]:
    """Ascending real/imaginary coefficients of q_N=phi_N-(1+i)."""
    maximum = max(
        12,
        max(m + truncation_degree + 1 for m, _a, _k in EXPONENTIAL_TERMS),
    )
    real = [Fraction(0)] * (maximum + 1)
    imag = [Fraction(0)] * (maximum + 1)
    real[0] = Fraction(-1)
    imag[0] = Fraction(-1)
    real[1] = Fraction(1)
    for m, coefficient in BASE_TERMS:
        value = Fraction(coefficient, factorial(m))
        real[m] += value
        real[m + 1] -= value
    for m, a, k in EXPONENTIAL_TERMS:
        value = Fraction(k, factorial(m))
        for n in range(truncation_degree + 1):
            exponential_coefficient = Fraction(a**n, factorial(n))
            contribution = value * exponential_coefficient
            real[m + n] -= contribution
            real[m + n + 1] += contribution
    while real[-1] == 0 and imag[-1] == 0:
        real.pop()
        imag.pop()
    return real, imag


def initial_reversed_gaussian_integer_polynomial(
    real: list[Fraction], imag: list[Fraction], radius: Fraction
) -> tuple[list[GaussianInteger], int]:
    """Clear denominators in w^d q_N(radius/w), leading first."""
    rational_coefficients = [
        (real[j] * radius**j, imag[j] * radius**j)
        for j in range(len(real))
    ]
    common_denominator = 1
    for x, y in rational_coefficients:
        common_denominator = lcm(
            common_denominator, x.denominator, y.denominator
        )
    integers = [
        (int(x * common_denominator), int(y * common_denominator))
        for x, y in rational_coefficients
    ]
    integers, content = primitive_gaussian(integers)
    common_denominator //= gcd(common_denominator, content)
    return integers, common_denominator


def fraction_free_schur_certificate(
    coefficients: list[GaussianInteger], dyadic_bits: int
) -> tuple[list[dict], Fraction, GaussianInteger]:
    """Run exact Schur reductions and return a boundary product lower bound."""
    polynomial = coefficients
    scale = 1 << dyadic_bits
    factor_product_numerator = 1
    records: list[dict] = []

    while len(polynomial) > 1:
        degree = len(polynomial) - 1
        leading = polynomial[0]
        constant = polynomial[-1]
        leading_norm = gnorm(leading)
        constant_norm = gnorm(constant)
        gap = leading_norm - constant_norm
        assert gap > 0

        modulus_upper_scaled = ceil_sqrt_ratio_scaled(
            constant_norm, leading_norm, dyadic_bits
        )
        factor_numerator = scale - modulus_upper_scaled
        assert factor_numerator > 0
        factor_product_numerator *= factor_numerator

        transformed = [
            gsub(
                gmul(gconj(leading), polynomial[j]),
                gmul(constant, gconj(polynomial[-1 - j])),
            )
            for j in range(len(polynomial))
        ]
        assert transformed[-1] == (0, 0)
        transformed = transformed[:-1]
        transformed, removed_content = primitive_gaussian(transformed)

        records.append(
            {
                "degree": degree,
                "state_sha256": gaussian_state_sha256(polynomial),
                "leading_norm_bit_length": leading_norm.bit_length(),
                "constant_norm_bit_length": constant_norm.bit_length(),
                "gap_positive": True,
                "gap_bit_length": gap.bit_length(),
                "gap_sha256": integer_sha256(gap),
                "dyadic_modulus_upper_scaled": modulus_upper_scaled,
                "dyadic_factor_numerator": factor_numerator,
                "removed_integer_content_bit_length": removed_content.bit_length(),
                "next_state_sha256": gaussian_state_sha256(transformed),
            }
        )
        polynomial = transformed

    assert polynomial[0] != (0, 0)
    factor_product = Fraction(
        factor_product_numerator, scale ** len(records)
    )
    return records, factor_product, polynomial[0]


def exponential_tail_bound(radius: Fraction, truncation_degree: int) -> Fraction:
    """Exact common tail bound, using exp(radius)<exp(2)<9."""
    exponential_remainder = (
        Fraction(9)
        * radius ** (truncation_degree + 1)
        / factorial(truncation_degree + 1)
    )
    total = Fraction(0)
    for m, a, k in EXPONENTIAL_TERMS:
        assert abs(a) == 1
        total += (
            Fraction(abs(k), factorial(m))
            * radius**m
            * (1 + radius)
            * exponential_remainder
        )
    return total


def numerical_q(z: complex | mp.mpc) -> complex | mp.mpc:
    value = z - (1 + 1j)
    for m, coefficient in BASE_TERMS:
        value += mp.mpf(coefficient) / factorial(m) * z**m * (1 - z)
    for m, a, k in EXPONENTIAL_TERMS:
        value += (
            mp.mpf(k)
            / factorial(m)
            * z**m
            * (z - 1)
            * mp.exp(a * z)
        )
    return value


def numerical_q_derivative(z: mp.mpc) -> mp.mpc:
    value = mp.mpc(1)
    for m, coefficient in BASE_TERMS:
        c = mp.mpf(coefficient) / factorial(m)
        value += c * (m * z ** (m - 1) * (1 - z) - z**m)
    for m, a, k in EXPONENTIAL_TERMS:
        c = mp.mpf(k) / factorial(m)
        h = z**m * (z - 1)
        value += c * mp.exp(a * z) * (
            m * z ** (m - 1) * (z - 1) + z**m + a * h
        )
    return value


def root_diagnostics() -> list[dict[str, str]]:
    mp.mp.dps = 90
    starts = [
        mp.mpc("1.2800742259", "1.2193981398"),
        mp.mpc("1.2097050148", "1.2892348916"),
        mp.mpc("1.2096733383", "1.2892715756"),
    ]
    records = []
    for start in starts:
        root = mp.findroot(
            numerical_q,
            start,
            solver="newton",
            df=numerical_q_derivative,
            tol=mp.mpf("1e-80"),
            maxsteps=200,
        )
        records.append(
            {
                "real": mp.nstr(root.real, 70),
                "imag": mp.nstr(root.imag, 70),
                "modulus": mp.nstr(abs(root), 70),
                "absolute_residual": mp.nstr(abs(numerical_q(root)), 12),
                "derivative_modulus": mp.nstr(
                    abs(numerical_q_derivative(root)), 40
                ),
            }
        )
    records.sort(key=lambda item: mp.mpf(item["modulus"]))
    return records


def numpy_q(values: np.ndarray) -> np.ndarray:
    result = values - (1 + 1j)
    for m, coefficient in BASE_TERMS:
        result += coefficient / factorial(m) * values**m * (1 - values)
    for m, a, k in EXPONENTIAL_TERMS:
        result += (
            k
            / factorial(m)
            * values**m
            * (values - 1)
            * np.exp(a * values)
        )
    return result


def adaptive_winding_diagnostic(radius: float) -> dict:
    previous_winding: int | None = None
    for power in range(14, 21):
        sample_count = 1 << power
        angles = 2 * np.pi * np.arange(sample_count) / sample_count
        values = numpy_q(radius * np.exp(1j * angles))
        argument_steps = np.angle(np.roll(values, -1) / values)
        winding = round(float(argument_steps.sum() / (2 * np.pi)))
        maximum_step = float(np.max(np.abs(argument_steps)))
        minimum_modulus = float(np.min(np.abs(values)))
        if (
            previous_winding == winding
            and maximum_step < 0.25
            and minimum_modulus > 0
        ):
            return {
                "radius": repr(radius),
                "sample_count": sample_count,
                "winding_number": winding,
                "maximum_principal_argument_step": repr(maximum_step),
                "minimum_sampled_modulus": repr(minimum_modulus),
                "diagnostic_stability_criterion_met": True,
            }
        previous_winding = winding
    return {
        "radius": repr(radius),
        "sample_count": sample_count,
        "winding_number": winding,
        "maximum_principal_argument_step": repr(maximum_step),
        "minimum_sampled_modulus": repr(minimum_modulus),
        "diagnostic_stability_criterion_met": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    jets = integral_hurwitz_jets(120)
    real, imag = truncated_q_coefficients(EXPONENTIAL_TRUNCATION_DEGREE)
    initial, cleared_denominator = initial_reversed_gaussian_integer_polynomial(
        real, imag, RADIUS
    )
    schur_records, reflection_product_lower, final_constant = (
        fraction_free_schur_certificate(initial, DYADIC_BITS)
    )
    degree = len(real) - 1
    assert degree == 61
    assert len(schur_records) == degree
    assert all(record["gap_positive"] for record in schur_records)

    # On |w|=1, the original reversed polynomial has leading modulus sqrt(2).
    # Hence |q_N|^2 >= 2*reflection_product_lower^2.
    boundary_modulus_squared_lower = 2 * reflection_product_lower**2
    tail = exponential_tail_bound(RADIUS, EXPONENTIAL_TRUNCATION_DEGREE)
    tail_squared = tail**2
    assert boundary_modulus_squared_lower > tail_squared

    root_records = root_diagnostics()
    winding_records = [
        adaptive_winding_diagnostic(float(RADIUS)),
        adaptive_winding_diagnostic(1.768),
        adaptive_winding_diagnostic(1.77),
    ]

    result = {
        "verdict": "exact zero-free disk certified",
        "candidate": {
            "base_terms_K_over_m_factorial_times_zm_1_minus_z": [
                {"m": m, "K": coefficient} for m, coefficient in BASE_TERMS
            ],
            "exponential_terms_k_over_m_factorial_times_zm_z_minus_1_exp_az": [
                {"m": m, "a": a, "k": k}
                for m, a, k in EXPONENTIAL_TERMS
            ],
            "phi_at_zero": "0",
            "phi_at_one": "1",
            "real_entire_coefficients": True,
        },
        "all_order_integral_hurwitz_jet_formula": (
            "For H=(k/m!)*z^m*(z-1)*exp(a*z): H^(m)(0)=-k; "
            "for n=m+r>=m+1, H^(n)(0)=k*binom(n,m)*(r*a^(r-1)-a^r)."
        ),
        "computed_integral_jet_order": 120,
        "computed_integral_jets_sha256": vector_sha256(jets),
        "certified_zero_free_closed_disk_radius": fraction_record(RADIUS),
        "strict_Taylor_radius_lower_bound": "707/400",
        "exponential_truncation_degree": EXPONENTIAL_TRUNCATION_DEGREE,
        "truncated_q_degree": degree,
        "truncated_q_real_coefficients_sha256": hashlib.sha256(
            json.dumps(
                [fraction_record(value) for value in real],
                separators=(",", ":"),
                sort_keys=True,
            ).encode()
        ).hexdigest(),
        "initial_reversed_primitive_gaussian_state_sha256": gaussian_state_sha256(
            initial
        ),
        "initial_cleared_denominator": cleared_denominator,
        "dyadic_reflection_modulus_bits": DYADIC_BITS,
        "fraction_free_schur_records": schur_records,
        "all_61_schur_gaps_strictly_positive": True,
        "final_fraction_free_constant": list(final_constant),
        "reflection_factor_product_rational_lower": fraction_record(
            reflection_product_lower
        ),
        "boundary_modulus_squared_rational_lower": fraction_record(
            boundary_modulus_squared_lower
        ),
        "exponential_tail_rational_upper": fraction_record(tail),
        "exponential_tail_squared_rational_upper": fraction_record(tail_squared),
        "exact_boundary_lower_exceeds_tail": True,
        "rouche_conclusion": (
            "q=phi-(1+i) has zero zeros in |z|<=707/400; real "
            "coefficients give the same for phi-(1-i)."
        ),
        "nearest_roots_of_phi_equals_1_plus_i_diagnostic": root_records,
        "adaptive_argument_principle_diagnostics": winding_records,
        "singularity_statement": (
            "phi is entire, so it adds no finite poles or essential "
            "singularities. Every preimage of 1+i or 1-i is a genuine "
            "logarithmic singularity of F composed with phi."
        ),
        "warning": (
            "The Schur, dyadic boundary, tail, and Rouche comparisons use "
            "exact integer/rational arithmetic. Decimal roots and sampled "
            "argument-principle counts are diagnostics only."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
