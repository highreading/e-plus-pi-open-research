#!/usr/bin/env python3
"""Deterministic exact replay for Item 418.

The companion report proves the sharp exponential constant obtainable from
centered circular Cauchy bounds for the two Item-415 normalized residue
coordinates.  This checker uses only the Python standard library.  It
verifies the dependency hashes, the polynomial identities controlling the
minimax problem, an algebraic isolation of the optimum, and an independent
rational Sturm certificate at a nearby radius.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STEM = "item418_normalized_large_carrier"

DEPENDENCIES = {
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "results/item200_common_log_gcd_certificate.json":
        "5fd9f62b82d92dde6755919ef0e44d5d42a3c9452acfc3bbe3d3ee96f7326f82",
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "results/item390_mixed_cubic_fresh_primitive_saturation_certificate.json":
        "45b61f683a29305e4fcfd8810f146068f950070496e8e88a2a6b800f9dc1ada6",
    "results/item390_mixed_cubic_fresh_primitive_saturation_root_audit.json":
        "8287cf78f5af6e4824c2034bd9af2aa5c7669afc0eb555c926ef59ab74914813",
    "sources/item415_marked_selector_compulsory_strip_report.md":
        "da79ea786471a6abb35288f242a0b0b2307a695bd9352eaa3c4e2033fc701777",
    "results/item415_marked_selector_compulsory_strip_certificate.json":
        "af731cf70e9a6d40cab380d38d5b404786cefef196eb42f743634b8d390cb29e",
    "manifests/item415_marked_selector_compulsory_strip_manifest.json":
        "8ae673cec3d739af76f3e73eaeb9266868431a77ab9bcaffd72a42cf522780b1",
    "results/item415_marked_selector_compulsory_strip_root_audit.json":
        "123576c914528abdc1e3ffa3993e5161c56f92ac21e4ec33b9c6f450edfa653c",
    "results/item415_marked_selector_compulsory_strip_hashes.sha256":
        "d347509c3bca23d8b723dfa14015a67e836cc616434d906ae9f2dae9a521f343",
}


Poly = list[Fraction]  # ascending coefficients


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def verify_dependencies() -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        digest = sha256_bytes((ROOT / relative).read_bytes())
        assert digest == expected, (relative, expected, digest)
        observed[relative] = digest
    return observed


def trim(poly: Poly) -> Poly:
    answer = poly[:]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def add(left: Poly, right: Poly) -> Poly:
    answer = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    return trim(answer)


def scale(poly: Poly, scalar: Fraction | int) -> Poly:
    return trim([Fraction(scalar) * value for value in poly])


def multiply(left: Poly, right: Poly) -> Poly:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return trim(answer)


def power(poly: Poly, exponent: int) -> Poly:
    answer: Poly = [Fraction(1)]
    base = poly
    value = exponent
    while value:
        if value & 1:
            answer = multiply(answer, base)
        base = multiply(base, base)
        value //= 2
    return answer


def derivative(poly: Poly) -> Poly:
    if len(poly) == 1:
        return [Fraction(0)]
    return trim([index * poly[index] for index in range(1, len(poly))])


def divide_with_remainder(dividend: Poly, divisor: Poly) -> tuple[Poly, Poly]:
    numerator = trim(dividend)
    denominator = trim(divisor)
    assert denominator != [0]
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0)] * (len(numerator) - len(denominator) + 1)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] / denominator[-1]
        quotient[shift] += coefficient
        for index, value in enumerate(denominator):
            numerator[index + shift] -= coefficient * value
        numerator = trim(numerator)
    return trim(quotient), trim(numerator)


def evaluate(poly: Poly, point: Fraction) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(poly):
        answer = answer * point + coefficient
    return answer


def sturm_sequence(poly: Poly) -> list[Poly]:
    sequence = [trim(poly), derivative(poly)]
    while sequence[-1] != [0]:
        _, remainder = divide_with_remainder(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append(scale(remainder, -1))
    return sequence


def sign(value: Fraction | Decimal) -> int:
    return (value > 0) - (value < 0)


def signs_and_variations(sequence: list[Poly], point: Fraction) -> tuple[list[int], int]:
    signs = [sign(evaluate(poly, point)) for poly in sequence]
    nonzero = [value for value in signs if value]
    variations = sum(left != right for left, right in zip(nonzero, nonzero[1:]))
    return signs, variations


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def exact_minimax_identities() -> dict[str, object]:
    # x=r^2.  The unique positive stationary radius is defined by h(x)=0.
    h: Poly = [Fraction(-4), Fraction(12), Fraction(3), Fraction(9)]
    x_left = Fraction(2_930_043, 10_000_000)
    x_right = Fraction(2_930_044, 10_000_000)
    assert evaluate(h, x_left) < 0 < evaluate(h, x_right)
    # h'(x)=12+6x+27x^2 is positive for every x>=0.
    assert derivative(h) == [Fraction(12), Fraction(6), Fraction(27)]

    # On the interior angular maximum, with
    # S^2=7x^2+2x+7, the radial derivative numerator is
    # 8(aS-b).  Its sign is controlled by the following exact identity.
    a = [Fraction(4), Fraction(5), Fraction(6)]
    b = [Fraction(10), Fraction(18), Fraction(17), Fraction(15)]
    s_squared = [Fraction(7), Fraction(2), Fraction(7)]
    left = add(multiply(power(a, 2), s_squared), scale(power(b, 2), -1))
    right = scale(
        multiply(multiply([Fraction(-1), Fraction(1)], [Fraction(1), Fraction(0), Fraction(1)]), h),
        3,
    )
    assert left == right

    # At h(x)=0, rho=N(x)/D(x).  Verify that its algebraic polynomial
    # vanishes modulo h exactly, without a floating-point resultant.
    q = [Fraction(2), Fraction(3), Fraction(3)]
    n_poly = scale(power(q, 3), 2)
    w = [Fraction(4), Fraction(-8), Fraction(5), Fraction(6), Fraction(9)]
    d_poly = multiply([Fraction(0), Fraction(0), Fraction(1)], power(w, 2))
    rho_relation = add(
        add(
            scale(power(n_poly, 3), 262_144),
            scale(multiply(power(n_poly, 2), d_poly), -35_555_328),
        ),
        add(
            scale(multiply(n_poly, power(d_poly, 2)), 1_259_712),
            scale(power(d_poly, 3), -531_441),
        ),
    )
    _, remainder = divide_with_remainder(rho_relation, h)
    assert remainder == [Fraction(0)]

    rho_polynomial: Poly = [
        Fraction(-531_441),
        Fraction(1_259_712),
        Fraction(-35_555_328),
        Fraction(262_144),
    ]
    rho_left = Fraction(13_559_748, 100_000)
    rho_right = Fraction(13_559_749, 100_000)
    assert evaluate(rho_polynomial, rho_left) < 0 < evaluate(rho_polynomial, rho_right)
    # Both cubics have negative discriminant and hence exactly one real root.
    h_discriminant = -118_800
    rho_discriminant = -93_433_860_167_497_364_275_200_000_000
    assert h_discriminant < 0 and rho_discriminant < 0

    # The optimum radius lies below 271/500, enough for the fixed
    # prefactor bounds used in the report.
    radius_upper = Fraction(271, 500)
    assert evaluate(h, radius_upper * radius_upper) > 0
    prefactor_zero_at_upper = 1 / (1 - radius_upper)
    prefactor_one_at_upper = (
        (1 + radius_upper) ** 2
        / (radius_upper * (1 - radius_upper) ** 2)
    )
    assert prefactor_zero_at_upper < 3
    assert prefactor_one_at_upper < 21

    return {
        "h_coefficients_ascending": [fraction_text(value) for value in h],
        "h_derivative_coefficients_ascending": [
            fraction_text(value) for value in derivative(h)
        ],
        "x_star_isolation": [fraction_text(x_left), fraction_text(x_right)],
        "radial_sign_identity": (
            "(6x^2+5x+4)^2(7x^2+2x+7)-"
            "(15x^3+17x^2+18x+10)^2="
            "3(x-1)(x^2+1)(9x^3+3x^2+12x-4)"
        ),
        "rho_polynomial_coefficients_ascending": [
            fraction_text(value) for value in rho_polynomial
        ],
        "rho_star_isolation": [fraction_text(rho_left), fraction_text(rho_right)],
        "h_discriminant": h_discriminant,
        "rho_polynomial_discriminant": rho_discriminant,
        "rho_relation_remainder_mod_h": [fraction_text(value) for value in remainder],
        "radius_upper": fraction_text(radius_upper),
        "prefactor_zero_upper": fraction_text(prefactor_zero_at_upper),
        "prefactor_one_upper": fraction_text(prefactor_one_at_upper),
    }


def rational_sturm_witness() -> dict[str, object]:
    radius = Fraction(5_413, 10_000)
    height_base = Fraction(678, 5)
    variable_a = [1 + radius * radius, -2 * radius]
    variable_b = [(1 - radius * radius) ** 2, Fraction(0), 4 * radius * radius]
    positivity = add(
        scale(power(variable_b, 2), height_base * radius**4),
        scale(power(variable_a, 3), -1),
    )
    sequence = sturm_sequence(positivity)
    left_signs, left_variations = signs_and_variations(sequence, Fraction(-1))
    right_signs, right_variations = signs_and_variations(sequence, Fraction(1))
    assert left_variations == right_variations
    witnesses = {
        point: evaluate(positivity, point)
        for point in (Fraction(-1), Fraction(0), Fraction(1))
    }
    assert all(value > 0 for value in witnesses.values())
    prefactor_zero = (1 + radius) / (1 - radius * radius)
    prefactor_one = (1 / radius) * (1 + radius) ** 4 / (1 - radius * radius) ** 2
    assert prefactor_zero < 3 and prefactor_one < 21
    return {
        "radius": fraction_text(radius),
        "height_base": fraction_text(height_base),
        "polynomial_coefficients_ascending": [fraction_text(value) for value in positivity],
        "sturm_degrees": [len(poly) - 1 for poly in sequence],
        "left_endpoint_signs": left_signs,
        "right_endpoint_signs": right_signs,
        "left_variations": left_variations,
        "right_variations": right_variations,
        "real_roots_in_closed_interval": 0,
        "values": {fraction_text(point): fraction_text(value) for point, value in witnesses.items()},
        "prefactor_zero": fraction_text(prefactor_zero),
        "prefactor_one": fraction_text(prefactor_one),
        "conclusion": (
            "max_{|z|=5413/10000} r^(-4)|1-z|^6/|1+z^2|^4 < 678/5"
        ),
    }


def decimal_root_of_rho_polynomial() -> Decimal:
    getcontext().prec = 80
    value = Decimal("135.5974839")
    for _ in range(20):
        polynomial = (
            Decimal(262_144) * value**3
            - Decimal(35_555_328) * value**2
            + Decimal(1_259_712) * value
            - Decimal(531_441)
        )
        derivative_value = (
            Decimal(786_432) * value**2
            - Decimal(71_110_656) * value
            + Decimal(1_259_712)
        )
        value -= polynomial / derivative_value
    return value


def capacity_record() -> dict[str, object]:
    getcontext().prec = 70
    rho = decimal_root_of_rho_polynomial()
    pi_value = Decimal(
        "3.1415926535897932384626433832795028841971693993751058209749445923"
    )
    forced_rate = (
        -Decimal(4) * Decimal(2).ln()
        + pi_value / Decimal(3).sqrt()
        + Decimal(3) * Decimal(3).ln()
    )
    old_ceiling = (Decimal(136).ln() - forced_rate) / Decimal(6)
    new_ceiling = (rho.ln() - forced_rate) / Decimal(6)
    improvement = old_ceiling - new_ceiling
    rational_ceiling = ((Decimal(678) / Decimal(5)).ln() - forced_rate) / Decimal(6)
    frozen_deficit = Decimal("1.0196329836694317938803064012")
    outside_large_component_residual = frozen_deficit - new_ceiling
    return {
        "rho_star_decimal": str(rho),
        "forced_Item200_rate_per_m": str(forced_rate),
        "Item415_component_ceiling": str(old_ceiling),
        "Item418_sharp_circular_component_ceiling": str(new_ceiling),
        "component_ceiling_decrease": str(improvement),
        "nearby_fully_rational_678_over_5_ceiling": str(rational_ceiling),
        "gap_between_rational_and_sharp_circular_ceiling": str(rational_ceiling - new_ceiling),
        "frozen_deficit": str(frozen_deficit),
        "deficit_minus_maximal_strictly_large_component": str(outside_large_component_residual),
        "residual_interpretation": (
            "admission comparison only; not a global ceiling reduction and not an additive de-overlap theorem"
        ),
        "booked_lower_bound_delta": "0",
        "global_total_content_ceiling_delta": "0",
        "frozen_deficit_delta": "0",
    }


def build_certificate() -> dict[str, object]:
    dependencies = verify_dependencies()
    minimax = exact_minimax_identities()
    sturm = rational_sturm_witness()
    capacity = capacity_record()
    witness = json.dumps(
        {"minimax": minimax, "sturm": sturm, "capacity": capacity},
        sort_keys=True,
        separators=(",", ":"),
    ).encode("ascii")
    return {
        "schema": "item418-normalized-large-carrier-v1",
        "item": 418,
        "status": "CANONICAL_ROOT_AUDITED_COMPONENT_CEILING_REDUCED_NO_BOOKING",
        "dependency_sha256": dependencies,
        "exact_circular_minimax": minimax,
        "independent_rational_sturm_witness": sturm,
        "capacity": capacity,
        "strict_claims": {
            "PROVED": [
                "exact global minimizer of the centered circular Cauchy kernel",
                "sharp circular exponential base rho_star",
                "strictly-large component ceiling reduction relative to Item415",
                "rational Sturm witness at radius 5413/10000 and base 678/5",
                "zero booking and no global total-ceiling subtraction",
            ],
            "SCOPED_NO_GO": [
                "changing only the centered circular radius cannot lower the exponential base below rho_star",
            ],
            "OPEN": [
                "valuation-weighted o(m) for the normalized carrier",
                "noncircular or cancellation-aware global bounds",
                "uniform noncollision c_m^>=1",
                "Route 1 and irrationality of e+pi",
            ],
        },
        "witness_sha256": sha256_bytes(witness),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / f"{STEM}_certificate.json")
    parser.add_argument("--replay", type=Path)
    arguments = parser.parse_args()
    payload = (json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n").encode("utf-8")
    if arguments.replay is not None:
        assert arguments.replay.read_bytes() == payload
    arguments.output.write_bytes(payload)


if __name__ == "__main__":
    main()
