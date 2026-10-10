#!/usr/bin/env python3
"""Deterministic certificate for Item 403.

The all-DVR theorem and the uniform perturbation theorem are proved in the
report.  This standard-library program checks exact normalization rows and
transparent Smith-valuation test vectors.  No finite scan is used as
evidence for an all-parameter assertion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def vp_integer(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def vp_fraction(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    return vp_integer(value.numerator, prime) - vp_integer(value.denominator, prime)


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def strip_two_three(value: int) -> int:
    value = abs(value)
    for prime in (2, 3):
        while value and value % prime == 0:
            value //= prime
    return value


def h_power_coefficients(parameter: int, degree: int) -> list[Fraction]:
    exponent = Fraction(parameter, 3)
    polynomial = (Fraction(1), Fraction(2), Fraction(3, 2), Fraction(1, 2))
    coefficients = [Fraction(1)]
    for target in range(1, degree + 1):
        total = Fraction(0)
        for index in range(1, min(3, target) + 1):
            total += (
                ((exponent + 1) * index - target)
                * polynomial[index]
                * coefficients[target - index]
            )
        coefficients.append(total / target)
    return coefficients


def negative_power_with_polynomial(q_value: int, degree: int, shift: int) -> int:
    polynomial_degree = 1 + 3 * shift
    return sum(
        math.comb(polynomial_degree, index)
        * math.comb(q_value + degree - index - 1, degree - index)
        for index in range(min(polynomial_degree, degree) + 1)
    )


def actual_fixed_gap_coefficients(q_value: int) -> tuple[Fraction, ...]:
    n_value = q_value - 1
    half_n = n_value // 2
    parameter = 2 * q_value - 3

    full_zero = h_power_coefficients(parameter, n_value)
    c_zero = 2 * full_zero[n_value]
    if n_value:
        c_zero += full_zero[n_value - 1]

    full_one = h_power_coefficients(parameter - 3, n_value)
    c_one = Fraction(0)
    for index in range(min(4, n_value) + 1):
        c_one += (
            Fraction(math.comb(4, index) * 2 ** (4 - index), 2)
            * full_one[n_value - index]
        )

    exponent_zero = Fraction(parameter, 3)
    exponent_one = exponent_zero - 1
    binomial_zero = Fraction(1)
    binomial_one = Fraction(1)
    t_zero = Fraction(0)
    t_one = Fraction(0)
    for index in range(half_n + 1):
        remaining = n_value - 2 * index
        t_zero += binomial_zero * negative_power_with_polynomial(
            q_value, remaining, 0
        )
        t_one += binomial_one * negative_power_with_polynomial(
            q_value, remaining, 1
        )
        binomial_zero *= (exponent_zero - index) / (index + 1)
        binomial_one *= (exponent_one - index) / (index + 1)
    return c_zero, t_zero, c_one, t_one


def matrix_for(
    c_zero: int, t_zero: int, c_one: int, t_one: int, k_value: int
) -> tuple[tuple[int, ...], ...]:
    return (
        (-t_zero, 0, k_value * c_zero, -t_one, 0, k_value * c_one),
        (c_zero, -t_zero, 0, c_one, -t_one, 0),
        (0, c_zero, -t_zero, 0, c_one, -t_one),
    )


def determinant_three(
    matrix: tuple[tuple[int, ...], ...], columns: tuple[int, int, int]
) -> int:
    a, b, c = columns
    return (
        matrix[0][a] * (matrix[1][b] * matrix[2][c] - matrix[1][c] * matrix[2][b])
        - matrix[0][b]
        * (matrix[1][a] * matrix[2][c] - matrix[1][c] * matrix[2][a])
        + matrix[0][c]
        * (matrix[1][a] * matrix[2][b] - matrix[1][b] * matrix[2][a])
    )


def determinant_divisors(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, int, int]:
    delta_one = math.gcd(*(abs(value) for row in matrix for value in row))
    minors_two = []
    for rows in combinations(range(3), 2):
        for columns in combinations(range(6), 2):
            minors_two.append(
                matrix[rows[0]][columns[0]] * matrix[rows[1]][columns[1]]
                - matrix[rows[0]][columns[1]] * matrix[rows[1]][columns[0]]
            )
    delta_two = math.gcd(*(abs(value) for value in minors_two))
    minors_three = [
        determinant_three(matrix, columns) for columns in combinations(range(6), 3)
    ]
    delta_three = math.gcd(*(abs(value) for value in minors_three))
    assert delta_two % delta_one == 0
    assert delta_three % delta_two == 0
    return delta_one, delta_two, delta_three


def smith_invariants(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, int, int]:
    delta_one, delta_two, delta_three = determinant_divisors(matrix)
    return delta_one, delta_two // delta_one, delta_three // delta_two


def predicted_local_valuations(
    values: tuple[int, int, int, int], k_value: int, prime: int
) -> tuple[int, int, int]:
    h_value = min(vp_integer(value, prime) for value in values)
    scale = prime**h_value
    c_zero, t_zero, c_one, t_one = (value // scale for value in values)
    resultant = c_zero * t_one - c_one * t_zero
    cube_zero = t_zero**3 - k_value * c_zero**3
    cube_one = t_one**3 - k_value * c_one**3
    gamma = min(
        vp_integer(resultant, prime),
        vp_integer(cube_zero, prime),
        vp_integer(cube_one, prime),
    )
    return h_value, h_value, h_value + gamma


def local_smith_checks() -> list[dict[str, object]]:
    test_rows = [
        (5, (1, 2, 3, 4), 7),
        (5, (7, 14, 21, 35), 7),
        (6, (1, 3, 2, 6), 7),
        (6, (49, 147, 98, 294), 7),
        (11, (25, 10, 15, 20), 5),
        (17, (121, 22, 33, 44), 11),
        (19, (13, 26, 39, 65), 13),
    ]
    rows = []
    for k_value, values, prime in test_rows:
        matrix = matrix_for(*values, k_value)
        invariants = smith_invariants(matrix)
        observed = tuple(vp_integer(value, prime) for value in invariants)
        predicted = predicted_local_valuations(values, k_value, prime)
        assert observed == predicted
        rows.append(
            {
                "K": k_value,
                "coefficients": list(values),
                "prime": prime,
                "smith_invariants": [str(value) for value in invariants],
                "observed_valuations": list(observed),
                "predicted_valuations": list(predicted),
            }
        )
    return rows


def falling_product(q_value: int) -> int:
    return math.prod(2 * q_value - 3 - 3 * index for index in range(q_value - 1))


def factorial_vp(value: int, prime: int) -> int:
    total = 0
    while value:
        value //= prime
        total += value
    return total


def countermodel(q_value: int, p_value: int, requested_digits: int) -> dict[str, object]:
    assert p_value > q_value
    assert (p_value - q_value) % 6 == 0
    assert q_value % 2 == 1 and q_value % 3 != 0
    m_value = (p_value - q_value) // 6
    exponent = 2 * m_value + q_value - 1
    x_value = pow(2, exponent, p_value)
    k_value = 4 ** (q_value - 1)
    assert pow(x_value, 3, p_value) == k_value % p_value

    anchor = actual_fixed_gap_coefficients(q_value)
    c_zero, t_zero, c_one, t_one = anchor
    anchor_resultant = c_zero * t_one - c_one * t_zero
    expected_resultant_v3 = (
        1
        - (q_value - 1)
        - factorial_vp(q_value - 1, 3)
        - (q_value - 1) // 2
        - factorial_vp((q_value - 1) // 2, 3)
    )
    assert vp_fraction(anchor_resultant, 3) == expected_resultant_v3

    # A deliberately high absolute 3-adic precision.  The proof shows that
    # such a level exists for every requested finite precision.
    perturbation_level = requested_digits + 80
    epsilon = 3**perturbation_level
    perturbed: list[Fraction] = []
    choices = []
    for c_value, t_value in ((c_zero, t_zero), (c_one, t_one)):
        c_residue = fraction_mod(c_value, p_value)
        epsilon_residue = epsilon % p_value
        forbidden = (-c_residue * pow(epsilon_residue, -1, p_value)) % p_value
        a_value = 0 if forbidden != 0 else 1
        c_prime = c_value + epsilon * a_value
        assert fraction_mod(c_prime, p_value) != 0
        b_value = (
            (x_value * fraction_mod(c_prime, p_value) - fraction_mod(t_value, p_value))
            * pow(epsilon_residue, -1, p_value)
        ) % p_value
        t_prime = t_value + epsilon * b_value
        assert fraction_mod(t_prime - x_value * c_prime, p_value) == 0
        perturbed.extend((c_prime, t_prime))
        choices.append({"a": a_value, "b": b_value})

    c_zero_p, t_zero_p, c_one_p, t_one_p = perturbed
    perturbed_resultant = c_zero_p * t_one_p - c_one_p * t_zero_p

    assert [vp_fraction(value, 3) for value in anchor] == [
        vp_fraction(value, 3) for value in perturbed
    ]
    assert vp_fraction(perturbed_resultant, 3) == expected_resultant_v3

    anchor_c_ratio = c_one / c_zero
    anchor_t_ratio = t_one / t_zero
    perturbed_c_ratio = c_one_p / c_zero_p
    perturbed_t_ratio = t_one_p / t_zero_p
    c_ratio_precision = vp_fraction(perturbed_c_ratio - anchor_c_ratio, 3)
    t_ratio_precision = vp_fraction(perturbed_t_ratio - anchor_t_ratio, 3)
    assert c_ratio_precision >= requested_digits
    assert t_ratio_precision >= requested_digits
    assert vp_fraction(anchor_t_ratio - anchor_c_ratio, 3) == 1
    assert vp_fraction(perturbed_t_ratio - perturbed_c_ratio, 3) == 1

    resultant_mod = fraction_mod(perturbed_resultant, p_value)
    cube_zero_mod = fraction_mod(t_zero_p**3 - k_value * c_zero_p**3, p_value)
    cube_one_mod = fraction_mod(t_one_p**3 - k_value * c_one_p**3, p_value)
    assert resultant_mod == cube_zero_mod == cube_one_mod == 0

    common_denominator = math.lcm(*(value.denominator for value in perturbed))
    assert strip_two_three(common_denominator) == 1
    integers = tuple(
        value.numerator * (common_denominator // value.denominator)
        for value in perturbed
    )
    invariants = smith_invariants(matrix_for(*integers, k_value))
    localized_invariants = tuple(strip_two_three(value) for value in invariants)
    invariant_p_valuations = tuple(vp_integer(value, p_value) for value in invariants)
    assert invariant_p_valuations[0] == 0
    assert invariant_p_valuations[1] == 0
    assert invariant_p_valuations[2] >= 1
    assert falling_product(q_value) % p_value != 0

    branch = "bijective_cube_U0_U1" if q_value % 6 == 5 else "branched_rho_U0_U1"
    return {
        "q": q_value,
        "p": p_value,
        "m": m_value,
        "q_mod_6": q_value % 6,
        "minimal_carrier_branch": branch,
        "requested_3adic_ratio_digits": requested_digits,
        "perturbation_level": perturbation_level,
        "perturbation_choices": choices,
        "coefficient_v3_anchor": [vp_fraction(value, 3) for value in anchor],
        "coefficient_v3_perturbed": [vp_fraction(value, 3) for value in perturbed],
        "determinant_v3_formula": expected_resultant_v3,
        "determinant_v3_perturbed": vp_fraction(perturbed_resultant, 3),
        "C_ratio_preserved_precision": c_ratio_precision,
        "T_ratio_preserved_precision": t_ratio_precision,
        "ratio_separation_v3_anchor": vp_fraction(anchor_t_ratio - anchor_c_ratio, 3),
        "ratio_separation_v3_perturbed": vp_fraction(
            perturbed_t_ratio - perturbed_c_ratio, 3
        ),
        "X_mod_p": x_value,
        "K_mod_p": k_value % p_value,
        "carrier_residues_mod_p": {
            "rho": resultant_mod,
            "U0": cube_zero_mod,
            "U1": cube_one_mod,
        },
        "localized_smith_invariants": [str(value) for value in localized_invariants],
        "smith_p_valuations": list(invariant_p_valuations),
        "p_divides_P_q": False,
        "ambient_countermodel_only": True,
    }


def run() -> dict[str, object]:
    smith_rows = local_smith_checks()
    # One normalization row in each exact Item-396 carrier branch.
    countermodels = [countermodel(5, 11, 18), countermodel(7, 13, 18)]
    witness = json.dumps(
        {"smith_rows": smith_rows, "countermodels": countermodels},
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return {
        "schema": "item403-exact-smith-and-finite-local-data-no-go-v1",
        "status": "work-only theorem normalization; no finite extrapolation",
        "uniform_theorems_proved_in_report": [
            "over every DVR with K a unit, the local Smith valuations are (h,h,h+gamma)",
            "globally away from 6, d1=d2=H and d3=H*G_primitive",
            "for every admissible q, compatible p, and finite 3-adic precision, ambient perturbations preserve that local data while forcing p|d3 and p not dividing P_q",
        ],
        "scope_boundary": (
            "the perturbations are not actual mixed-cubic coefficient rows and do not "
            "refute the actual support conjecture"
        ),
        "local_smith_normalization_rows": smith_rows,
        "carrier_split_normalization_rows": countermodels,
        "assertions": {
            "exact_local_smith_formula_normalized": True,
            "both_q_mod_6_carrier_branches_checked": True,
            "coefficient_and_resultant_v3_preserved": True,
            "finite_ratio_digits_preserved": True,
            "minimal_carriers_vanish_mod_compatible_prime": True,
            "matrix_rank_is_two_mod_compatible_prime": True,
            "compatible_prime_does_not_divide_P_q": True,
            "no_actual_support_theorem_claimed": True,
            "booking_delta": 0,
        },
        "witness_sha256": hashlib.sha256(witness).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    payload = run()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    print(hashlib.sha256(rendered).hexdigest())
    if arguments.output:
        arguments.output.write_bytes(rendered)


if __name__ == "__main__":
    main()
