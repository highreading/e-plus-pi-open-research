#!/usr/bin/env python3
"""Exact certificate for four-power cofactor content and endpoint Smith data."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from math import comb, factorial, gcd, lcm
from pathlib import Path

import sympy as sp


def integer_content(values) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(int(value)))
    return result


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0)")
    value = abs(value)
    return (value & -value).bit_length() - 1


def determinant(matrix: list[list[int]]) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    if size == 1:
        return matrix[0][0]
    return sum(
        (-1) ** column
        * matrix[0][column]
        * determinant(
            [
                row[:column] + row[column + 1 :]
                for row in matrix[1:]
            ]
        )
        for column in range(size)
    )


def determinantal_divisor(matrix: list[list[int]], size: int) -> int:
    minors = []
    for rows in itertools.combinations(range(len(matrix)), size):
        for columns in itertools.combinations(range(len(matrix[0])), size):
            minors.append(
                determinant(
                    [
                        [matrix[row][column] for column in columns]
                        for row in rows
                    ]
                )
            )
    return integer_content(minors)


def primitive_integer_row(values: list[Fraction]) -> tuple[list[int], Fraction]:
    denominator = 1
    for value in values:
        denominator = lcm(denominator, value.denominator)
    integers = [
        value.numerator * (denominator // value.denominator)
        for value in values
    ]
    content = integer_content(integers)
    if content == 0:
        raise ValueError("zero rational row")
    return [value // content for value in integers], Fraction(
        denominator, content
    )


def common_integer_clearing(rows: list[list[Fraction]]) -> tuple[list[list[int]], int]:
    denominator = 1
    for row in rows:
        for value in row:
            denominator = lcm(denominator, value.denominator)
    return [
        [
            value.numerator * (denominator // value.denominator)
            for value in row
        ]
        for row in rows
    ], denominator


def primitive_rational_pair(
    values: list[Fraction],
) -> tuple[list[int], int, int]:
    denominator = 1
    for value in values:
        denominator = lcm(denominator, value.denominator)
    integers = [
        value.numerator * (denominator // value.denominator)
        for value in values
    ]
    content = integer_content(integers)
    return [value // content for value in integers], denominator, content


def phase_vector_data(
    logarithmic: list[int], positive: list[int]
) -> dict[str, object]:
    q = [
        logarithmic[1] * logarithmic[3] - logarithmic[2] ** 2,
        logarithmic[1] * logarithmic[2]
        - logarithmic[0] * logarithmic[3],
        logarithmic[0] * logarithmic[2] - logarithmic[1] ** 2,
    ]
    e = [
        sum(q[j] * positive[j + shift] for j in range(3))
        for shift in range(2)
    ]
    vector = [
        e[1] * q[0],
        e[1] * q[1] - e[0] * q[0],
        e[1] * q[2] - e[0] * q[1],
        -e[0] * q[2],
    ]
    q_content = integer_content(q)
    e_content = integer_content(e)
    vector_content = integer_content(vector)
    if q_content == 0 or e_content == 0 or vector_content == 0:
        raise ValueError("degenerate phase vector")
    q_primitive = [value // q_content for value in q]
    compressed_e = [
        sum(q_primitive[j] * positive[j + shift] for j in range(3))
        for shift in range(2)
    ]
    compressed_content = integer_content(compressed_e)
    eta = [value // compressed_content for value in compressed_e]
    primitive = [value // vector_content for value in vector]
    reconstructed = [
        eta[1] * q_primitive[0],
        eta[1] * q_primitive[1] - eta[0] * q_primitive[0],
        eta[1] * q_primitive[2] - eta[0] * q_primitive[1],
        -eta[0] * q_primitive[2],
    ]
    if reconstructed != primitive:
        raise AssertionError((reconstructed, primitive))
    return {
        "q": q,
        "e": e,
        "vector": vector,
        "q_content": q_content,
        "e_content": e_content,
        "vector_content": vector_content,
        "q_primitive": q_primitive,
        "compressed_e": compressed_e,
        "compressed_content": compressed_content,
        "eta": eta,
        "primitive": primitive,
    }


def compressed_value(q_primitive: list[int], eta: list[int], row: list[int]) -> int:
    moments = [
        sum(q_primitive[j] * row[j + shift] for j in range(3))
        for shift in range(2)
    ]
    return eta[1] * moments[0] - eta[0] * moments[1]


def lattice_invariants(
    a_matrix: list[list[int]], endpoint: list[list[int]]
) -> dict[str, int]:
    matrix = [*a_matrix, *endpoint]
    delta2 = determinantal_divisor(a_matrix, 2)
    delta4 = abs(determinant(matrix))
    if delta2 == 0 or delta4 == 0:
        raise ValueError("rank-deficient lattice matrix")
    n_rho = [*a_matrix, endpoint[0]]
    n_beta = [*a_matrix, endpoint[1]]
    delta3_rho = determinantal_divisor(n_rho, 3)
    delta3_beta = determinantal_divisor(n_beta, 3)
    if delta3_rho % delta2 or delta3_beta % delta2:
        raise AssertionError("delta_2 does not divide delta_3")
    coordinate_ideal_rho = delta3_rho // delta2
    coordinate_ideal_beta = delta3_beta // delta2
    s1 = gcd(coordinate_ideal_rho, coordinate_ideal_beta)
    if delta4 % delta2:
        raise AssertionError("delta_2 does not divide delta_4")
    quotient_index = delta4 // delta2
    if quotient_index % s1:
        raise AssertionError("first Smith invariant does not divide index")
    s2 = quotient_index // s1
    if s2 % s1:
        raise AssertionError("invalid Smith invariant ordering")
    return {
        "delta2": delta2,
        "delta3_rho": delta3_rho,
        "delta3_beta": delta3_beta,
        "delta4": delta4,
        "coordinate_ideal_rho": coordinate_ideal_rho,
        "coordinate_ideal_beta": coordinate_ideal_beta,
        "s1": s1,
        "s2": s2,
        "smith_ratio": s2 // s1,
        "quotient_index": quotient_index,
    }


def symbolic_checks() -> dict[str, bool]:
    logarithmic = sp.symbols("l0:4")
    positive = sp.symbols("e0:4")
    endpoint = sp.symbols("x0:4")
    t, scale_l, scale_e = sp.symbols("t scale_l scale_e")

    q = [
        logarithmic[1] * logarithmic[3] - logarithmic[2] ** 2,
        logarithmic[1] * logarithmic[2]
        - logarithmic[0] * logarithmic[3],
        logarithmic[0] * logarithmic[2] - logarithmic[1] ** 2,
    ]
    e = [
        sum(q[j] * positive[j + shift] for j in range(3))
        for shift in range(2)
    ]
    vector = [
        e[1] * q[0],
        e[1] * q[1] - e[0] * q[0],
        e[1] * q[2] - e[0] * q[1],
        -e[0] * q[2],
    ]
    polynomial = sum(vector[j] * t**j for j in range(4))
    expected_polynomial = (e[1] - e[0] * t) * sum(
        q[j] * t**j for j in range(3)
    )

    p = {
        (i, j): logarithmic[i] * positive[j]
        - logarithmic[j] * positive[i]
        for i in range(4)
        for j in range(i + 1, 4)
    }
    expected_e0 = (
        -logarithmic[3] * p[0, 1]
        + logarithmic[2] * p[0, 2]
        - logarithmic[1] * p[1, 2]
    )
    expected_e1 = (
        logarithmic[0] * p[2, 3]
        - logarithmic[1] * p[1, 3]
        + logarithmic[2] * p[1, 2]
    )

    q_symbol = sp.symbols("q0:3")
    eta_symbol = sp.symbols("eta0:2")
    compressed = [
        sum(q_symbol[j] * endpoint[j + shift] for j in range(3))
        for shift in range(2)
    ]
    primitive_symbol = [
        eta_symbol[1] * q_symbol[0],
        eta_symbol[1] * q_symbol[1]
        - eta_symbol[0] * q_symbol[0],
        eta_symbol[1] * q_symbol[2]
        - eta_symbol[0] * q_symbol[1],
        -eta_symbol[0] * q_symbol[2],
    ]
    compressed_identity = sp.expand(
        sum(primitive_symbol[j] * endpoint[j] for j in range(4))
        - (
            eta_symbol[1] * compressed[0]
            - eta_symbol[0] * compressed[1]
        )
    )

    scaled_q = [
        value.subs(
            {
                logarithmic[j]: scale_l * logarithmic[j]
                for j in range(4)
            },
            simultaneous=True,
        )
        for value in q
    ]
    scaled_e = [
        sum(
            scaled_q[j] * scale_e * positive[j + shift]
            for j in range(3)
        )
        for shift in range(2)
    ]
    scaled_vector = [
        scaled_e[1] * scaled_q[0],
        scaled_e[1] * scaled_q[1] - scaled_e[0] * scaled_q[0],
        scaled_e[1] * scaled_q[2] - scaled_e[0] * scaled_q[1],
        -scaled_e[0] * scaled_q[2],
    ]

    return {
        "hankel_identity_first_window": sp.expand(
            sum(q[j] * logarithmic[j] for j in range(3))
        )
        == 0,
        "hankel_identity_second_window": sp.expand(
            sum(q[j] * logarithmic[j + 1] for j in range(3))
        )
        == 0,
        "cubic_product_identity": sp.expand(
            polynomial - expected_polynomial
        )
        == 0,
        "phase_vector_kills_logarithmic_row": sp.expand(
            sum(vector[j] * logarithmic[j] for j in range(4))
        )
        == 0,
        "phase_vector_kills_positive_row": sp.expand(
            sum(vector[j] * positive[j] for j in range(4))
        )
        == 0,
        "e0_pluecker_identity": sp.expand(e[0] - expected_e0) == 0,
        "e1_pluecker_identity": sp.expand(e[1] - expected_e1) == 0,
        "compressed_endpoint_identity": compressed_identity == 0,
        "row_scaling_degree_4_1": all(
            sp.expand(
                scaled_vector[j]
                - scale_l**4 * scale_e * vector[j]
            )
            == 0
            for j in range(4)
        ),
    }


def deterministic_integer_checks(target: int = 240) -> dict[str, int]:
    checked = 0
    attempted = 0
    for seed in range(1, 5000):
        attempted += 1
        logarithmic = [
            ((seed + 3) * (j + 2) ** 3 + 7 * seed * j + 11) % 43 - 21
            for j in range(4)
        ]
        positive = [
            ((seed + 5) * (j + 1) ** 4 + 9 * seed * (j + 2) + 3) % 47 - 23
            for j in range(4)
        ]
        rho = [
            ((seed + 7) * (j + 3) ** 2 + 5 * seed * j + 1) % 53 - 26
            for j in range(4)
        ]
        beta = [
            ((seed + 11) * (j + 4) ** 3 + 3 * seed * j + 17) % 59 - 29
            for j in range(4)
        ]
        a_matrix = [logarithmic, positive]
        if determinantal_divisor(a_matrix, 2) == 0:
            continue
        try:
            phase = phase_vector_data(logarithmic, positive)
            invariants = lattice_invariants(a_matrix, [rho, beta])
        except ValueError:
            continue

        q_content = int(phase["q_content"])
        e_content = int(phase["e_content"])
        vector_content = int(phase["vector_content"])
        compressed_content = int(phase["compressed_content"])
        if vector_content != q_content * e_content:
            raise AssertionError("Gauss content identity failed")
        if e_content != q_content * compressed_content:
            raise AssertionError("normalized e content identity failed")
        delta2 = invariants["delta2"]
        if e_content % delta2:
            raise AssertionError("delta_2 does not divide e content")

        primitive = phase["primitive"]
        if integer_content(primitive) != 1:
            raise AssertionError("phase vector is not primitive")
        if sum(primitive[j] * logarithmic[j] for j in range(4)):
            raise AssertionError("primitive vector lost L kernel")
        if sum(primitive[j] * positive[j] for j in range(4)):
            raise AssertionError("primitive vector lost E kernel")

        endpoint_pair = [
            sum(primitive[j] * row[j] for j in range(4))
            for row in (rho, beta)
        ]
        endpoint_content = integer_content(endpoint_pair)
        s1 = invariants["s1"]
        s2 = invariants["s2"]
        if endpoint_content % s1 or s2 % endpoint_content:
            raise AssertionError("selected Smith divisibility failed")
        if endpoint_pair[0] != compressed_value(
            phase["q_primitive"], phase["eta"], rho
        ):
            raise AssertionError("compressed rho identity failed")
        if endpoint_pair[1] != compressed_value(
            phase["q_primitive"], phase["eta"], beta
        ):
            raise AssertionError("compressed beta identity failed")
        checked += 1
        if checked == target:
            break
    if checked != target:
        raise AssertionError((checked, attempted))
    return {"matrices_checked": checked, "seeds_attempted": attempted}


def raw_coordinate_numerators(n: int, k: int) -> tuple[int, int, int, int]:
    output = [0, 0, 0, 0]
    products = [1] * (n + 1)
    for j in range(n + 1):
        monomial = n + j
        for step in range(1, k):
            products[j] *= 4 * step - monomial - 1
        residue = monomial % 4
        output[residue] += (
            (-1) ** (j + (monomial - residue) // 4)
            * comb(n, j)
            * products[j]
        )
    return tuple(output)


def coordinates(n: int, k: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    denominator = 4 ** (k - 1) * factorial(k - 1)
    return tuple(
        Fraction(value, denominator)
        for value in raw_coordinate_numerators(n, k)
    )


def monomial_reduction(monomial: int, k: int) -> tuple[Fraction, Fraction]:
    scale = Fraction(1)
    endpoint = Fraction(0)
    for step in range(k, 1, -1):
        endpoint += scale * Fraction(
            1, 4 * (step - 1) * 2 ** (step - 1)
        )
        scale *= Fraction(4 * step - monomial - 5, 4 * (step - 1))
    return scale, endpoint


def polynomial_integral(monomial: int) -> Fraction:
    quotient, residue = divmod(monomial, 4)
    return sum(
        (
            Fraction(
                (-1) ** index,
                residue + 4 * (quotient - 1 - index) + 1,
            )
            for index in range(quotient)
        ),
        Fraction(0),
    )


def rational_and_coordinates(
    n: int, k: int
) -> tuple[Fraction, tuple[Fraction, Fraction, Fraction, Fraction]]:
    rational = Fraction(0)
    output = [Fraction(0) for _ in range(4)]
    for j in range(n + 1):
        monomial = n + j
        coefficient = (-1) ** j * comb(n, j)
        scale, endpoint = monomial_reduction(monomial, k)
        quotient, residue = divmod(monomial, 4)
        output[residue] += coefficient * scale * (-1) ** quotient
        rational += coefficient * (
            endpoint + scale * polynomial_integral(monomial)
        )
    return rational, tuple(output)


def quartic_record(n: int) -> dict[str, object]:
    k = round(n * math.log(n))
    data = [rational_and_coordinates(n, k + shift) for shift in range(4)]
    rational = [entry[0] for entry in data]
    coordinate_rows = [entry[1] for entry in data]
    logarithmic_q = [row[0] - row[2] for row in coordinate_rows]
    positive_q = [row[0] + row[2] for row in coordinate_rows]
    odd_q = [row[1] for row in coordinate_rows]

    logarithmic, logarithmic_scale = primitive_integer_row(logarithmic_q)
    positive, positive_scale = primitive_integer_row(positive_q)
    phase = phase_vector_data(logarithmic, positive)
    primitive = phase["primitive"]
    a_matrix = [logarithmic, positive]
    delta2 = determinantal_divisor(a_matrix, 2)
    if phase["e_content"] % delta2:
        raise AssertionError("quartic forced delta_2 divisor failed")

    endpoint_q = [
        [8 * value for value in rational],
        odd_q,
    ]
    endpoint, endpoint_delta = common_integer_clearing(endpoint_q)
    invariants = lattice_invariants(a_matrix, endpoint)
    block_pair = [
        sum(primitive[j] * row[j] for j in range(4))
        for row in endpoint
    ]
    block_content = integer_content(block_pair)
    if block_content % invariants["s1"]:
        raise AssertionError("quartic block content misses s1")
    if invariants["s2"] % block_content:
        raise AssertionError("quartic block content does not divide s2")

    rational_pair = [
        sum(primitive[j] * 8 * rational[j] for j in range(4)),
        sum(primitive[j] * odd_q[j] for j in range(4)),
    ]
    primitive_pair, selected_delta, selected_content = primitive_rational_pair(
        rational_pair
    )
    if endpoint_delta % selected_delta:
        raise AssertionError("selected denominator does not divide block clearing")
    clearing_factor = endpoint_delta // selected_delta
    if block_content != clearing_factor * selected_content:
        raise AssertionError("block/selected content identity failed")

    for row, observed in zip(endpoint, block_pair):
        expected = compressed_value(
            phase["q_primitive"], phase["eta"], row
        )
        if observed != expected:
            raise AssertionError("quartic compressed endpoint identity failed")

    smith_extra = block_content // invariants["s1"]
    if invariants["smith_ratio"] % smith_extra:
        raise AssertionError("quartic selected Smith gcd failed")

    return {
        "n": n,
        "k": k,
        "logarithmic_row_scale": str(logarithmic_scale),
        "positive_row_scale": str(positive_scale),
        "endpoint_common_clearing_bits": endpoint_delta.bit_length(),
        "selected_pair_clearing_bits": selected_delta.bit_length(),
        "coefficient_content_bits": phase["vector_content"].bit_length(),
        "forced_delta2_bits": delta2.bit_length(),
        "coefficient_content_over_delta2_bits": (
            phase["vector_content"] // delta2
        ).bit_length(),
        "primitive_coefficient_max_bits": max(
            abs(value).bit_length() for value in primitive
        ),
        "quotient_index_bits": invariants["quotient_index"].bit_length(),
        "smith_s1_bits": invariants["s1"].bit_length(),
        "smith_s2_bits": invariants["s2"].bit_length(),
        "smith_ratio_bits": invariants["smith_ratio"].bit_length(),
        "block_phase_content_bits": block_content.bit_length(),
        "block_phase_extra_content": str(smith_extra),
        "intrinsic_selected_content": str(selected_content),
        "intrinsic_selected_content_bits": selected_content.bit_length(),
        "primitive_endpoint_pair_max_bits": max(
            abs(value).bit_length() for value in primitive_pair
        ),
        "quotient_index_v2": v2(invariants["quotient_index"]),
        "block_phase_content_v2": v2(block_content),
    }


def sharpness_family_check(maximum_n: int = 64) -> dict[str, object]:
    records = []
    for exponent in (1, 2, 4, 8, 16, 32, maximum_n):
        a_matrix = [[1, 0, 0, 0], [0, 1, 0, 0]]
        endpoint = [
            [0, 0, 1, 0],
            [0, 0, 0, 2 ** (2 * exponent)],
        ]
        invariants = lattice_invariants(a_matrix, endpoint)
        if invariants["s1"] != 1 or invariants["s2"] != 2 ** (
            2 * exponent
        ):
            raise AssertionError("sharpness Smith factors failed")
        contents = [
            integer_content([endpoint[row][column] for row in range(2)])
            for column in (2, 3)
        ]
        if contents != [1, 2 ** (2 * exponent)]:
            raise AssertionError("sharpness direction contents failed")
        records.append(
            {
                "exponent": exponent,
                "s1": str(invariants["s1"]),
                "s2_bits": invariants["s2"].bit_length(),
                "direction_content_bits": [
                    value.bit_length() for value in contents
                ],
            }
        )
    return {
        "family": "diag(1, 2^(2N)) on the saturated rank-two kernel",
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/quartic_four_power_primitive_content_smith_certificate.json"
        ),
    )
    args = parser.parse_args()

    symbolic = symbolic_checks()
    if not all(symbolic.values()):
        raise AssertionError(symbolic)
    integer_checks = deterministic_integer_checks()
    sharpness = sharpness_family_check()
    quartic = [quartic_record(n) for n in range(4, 41, 4)]

    result = {
        "schema": "quartic-four-power-primitive-content-smith-v1",
        "symbolic_identities": symbolic,
        "deterministic_exact_integer_checks": integer_checks,
        "smith_sharpness_family": sharpness,
        "critical_quartic_diagnostics": quartic,
        "warnings": [
            "The coefficient-content, determinantal-divisor, and selected-Smith formulas are exact theorems.",
            "The sharpness family is an abstract lattice example, not a quartic-coordinate family.",
            "The bounded critical quartic records are diagnostics and imply no asymptotic content law.",
            "No subexponential bound for the intrinsic selected quartic endpoint content is proved.",
            "Nothing here classifies e+pi.",
        ],
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(hashlib.sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    main()
