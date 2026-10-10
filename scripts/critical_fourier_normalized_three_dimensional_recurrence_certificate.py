"""Exact certificate for the normalized three-dimensional Fourier recurrence.

The all-parameter proof, including the endpoint audit, is in
sources/critical_fourier_normalized_three_dimensional_recurrence.md.
All arithmetic in this certificate is exact integer arithmetic in the Gaussian
residue ring (Z/pZ)[i].
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


Gaussian = tuple[int, int]


def gadd(left: Gaussian, right: Gaussian, prime: int) -> Gaussian:
    return (
        (left[0] + right[0]) % prime,
        (left[1] + right[1]) % prime,
    )


def gscale(scale: int, value: Gaussian, prime: int) -> Gaussian:
    return scale * value[0] % prime, scale * value[1] % prime


def gmul(left: Gaussian, right: Gaussian, prime: int) -> Gaussian:
    return (
        (left[0] * right[0] - left[1] * right[1]) % prime,
        (left[0] * right[1] + left[1] * right[0]) % prime,
    )


def gpow(base: Gaussian, exponent: int, prime: int) -> Gaussian:
    value = (1, 0)
    while exponent:
        if exponent & 1:
            value = gmul(value, base, prime)
        base = gmul(base, base, prime)
        exponent //= 2
    return value


def ginv(value: Gaussian, prime: int) -> Gaussian:
    norm = (value[0] * value[0] + value[1] * value[1]) % prime
    assert norm != 0
    inverse_norm = pow(norm, -1, prime)
    return value[0] * inverse_norm % prime, -value[1] * inverse_norm % prime


def gdiv(left: Gaussian, right: Gaussian, prime: int) -> Gaussian:
    return gmul(left, ginv(right, prime), prime)


def polynomial_multiply(
    left: list[Gaussian], right: list[Gaussian], prime: int
) -> list[Gaussian]:
    value = [(0, 0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            index = left_index + right_index
            value[index] = gadd(
                value[index], gmul(left_value, right_value, prime), prime
            )
    return value


def base_polynomial_mod(n: int, prime: int) -> list[Gaussian]:
    """Return (1-i)^n (z-1)^n (z-i)^n in F_p[i][z]."""
    first = [
        (math.comb(n, index) * ((-1) ** (n - index)) % prime, 0)
        for index in range(n + 1)
    ]
    second = [
        gscale(
            math.comb(n, index),
            gpow((0, -1), n - index, prime),
            prime,
        )
        for index in range(n + 1)
    ]
    phase = gpow((1, -1), n, prime)
    return [
        gmul(phase, coefficient, prime)
        for coefficient in polynomial_multiply(first, second, prime)
    ]


def multiply_one_plus_z_squared(
    polynomial: list[Gaussian], prime: int
) -> list[Gaussian]:
    value: list[Gaussian] = []
    for index in range(len(polynomial) + 2):
        coefficient = (0, 0)
        if index < len(polynomial):
            coefficient = gadd(coefficient, polynomial[index], prime)
        if 0 <= index - 1 < len(polynomial):
            coefficient = gadd(
                coefficient,
                gscale(2, polynomial[index - 1], prime),
                prime,
            )
        if 0 <= index - 2 < len(polynomial):
            coefficient = gadd(
                coefficient, polynomial[index - 2], prime
            )
        value.append(coefficient)
    return value


def initial_r_polynomial(n: int, prime: int) -> list[Gaussian]:
    return polynomial_multiply(
        base_polynomial_mod(n, prime), [(1, 0), (1, 0)], prime
    )


def endpoint_integral(
    polynomial: list[Gaussian], u: int, extra_z: int, prime: int
) -> Gaussian:
    """Integrate z^(u-1+extra_z) R(z) formally from 1 to i."""
    value = (0, 0)
    for index, coefficient in enumerate(polynomial):
        denominator = u + index + extra_z
        assert 1 <= denominator < prime
        endpoint_difference = gadd(
            gpow((0, 1), denominator, prime), (-1, 0), prime
        )
        term = gscale(
            pow(denominator, -1, prime),
            gmul(coefficient, endpoint_difference, prime),
            prime,
        )
        value = gadd(value, term, prime)
    return value


def A_coefficient(n: int, h: int) -> int:
    numerator = (
        math.comb(n, 2 * h)
        * math.factorial(2 * n - 2 * h)
        * math.factorial(n)
    )
    denominator = math.factorial(n - h)
    assert numerator % denominator == 0
    return numerator // denominator


def phi_mod(n: int, argument: int, prime: int) -> int:
    value = 0
    product = 1
    for h in range(n // 2 + 1):
        if h:
            product = product * (argument + 2 * h - 1) % prime
        value += (
            A_coefficient(n, h)
            * pow(2, h, prime)
            * product
        )
        value %= prime
    return value


def exponential_pair(n: int) -> tuple[int, int]:
    p_previous, p_current = 1, 3
    q_previous, q_current = 1, 1
    if n == 0:
        return p_previous, q_previous
    if n == 1:
        return p_current, q_current
    for index in range(2, n + 1):
        multiplier = 4 * index - 2
        p_previous, p_current = (
            p_current,
            multiplier * p_current + p_previous,
        )
        q_previous, q_current = (
            q_current,
            multiplier * q_current + q_previous,
        )
    return p_current, q_current


def valuation(value: int, prime: int) -> int:
    assert value != 0
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def coefficient_digit(
    polynomial: list[Gaussian], K: int, prime: int
) -> Gaussian:
    value = (0, 0)
    for index, coefficient in enumerate(polynomial):
        denominator = K - index
        assert 1 <= denominator < prime
        sign = 1 if (denominator - 1) % 2 == 0 else -1
        value = gadd(
            value,
            gscale(
                sign * pow(denominator, -1, prime),
                coefficient,
                prime,
            ),
            prime,
        )
    return value


def recurrence_coefficients(
    n: int, c: int, v: int, prime: int
) -> dict[str, Gaussian]:
    return {
        "a0": (
            -(2 * c + 3 * n + 3) % prime,
            (-2 * c - n + 4 * v + 3) % prime,
        ),
        "a1": (0, (c - v - 1) % prime),
        "b0": (
            -(2 * c + 3 * n + 4 * v + 7) % prime,
            (-2 * c - n - 1) % prime,
        ),
        "b1": ((c + 2 * n + v + 3) % prime, 0),
        "g0": (
            (2 * c + 3 * n - 4 * v - 3) % prime,
            (2 * c + n - 8 * v - 9) % prime,
        ),
        "g1": (
            (-c - n + v + 1) % prime,
            (-4 * c - n + 6 * v + 9) % prime,
        ),
        "g2": (0, (c - v - 2) % prime),
        "d0": (
            (2 * c + 3 * n + 1) % prime,
            (2 * c + n - 4 * v - 5) % prime,
        ),
        "d1": (0, (-c + v + 2) % prime),
    }


def relation_sum(
    terms: list[tuple[Gaussian, Gaussian]], prime: int
) -> Gaussian:
    value = (0, 0)
    for coefficient, variable in terms:
        value = gadd(value, gmul(coefficient, variable, prime), prime)
    return value


def kappa_value(
    n: int,
    v: int,
    ell: int,
    K: int,
    factorial: list[int],
    prime: int,
) -> int:
    denominator = factorial[n] * factorial[ell] % prime
    denominator = denominator * factorial[K] % prime
    return -factorial[2 * v + 1] * pow(denominator, -1, prime) % prime


def verify_case(n: int, prime: int) -> dict[str, object]:
    assert n > 0 and n % 2 == 0 and prime > 2 * n + 1
    c = (prime - 2 * n - 1) // 2
    assert 2 * c == prime - 2 * n - 1
    factorial = [1] * prime
    for index in range(1, prime):
        factorial[index] = factorial[index - 1] * index % prime

    p_value, q_value = exponential_pair(n)
    q_valuation = valuation(q_value, prime)
    q_quotient = (
        (q_value // prime) % prime if q_valuation >= 1 else None
    )
    R = initial_r_polynomial(n, prime)
    I_values: list[Gaussian] = []
    J_values: list[Gaussian] = []
    kappas: list[int] = []
    phis: list[int] = []
    D_values: list[int] = []
    U_values: list[int] = []
    normalized_I: list[Gaussian] = []
    normalized_J: list[Gaussian] = []
    target_records: list[dict[str, int]] = []
    target_values: list[int] = []
    transcript: list[str] = []

    for v in range(c):
        s = 2 * v + 1
        ell = (prime + s) // 2
        K = n + ell
        u = c - v
        assert K < prime <= 2 * (K - n)
        assert len(R) == 2 * n + s + 1

        I_value = endpoint_integral(R, u, 0, prime)
        I_values.append(I_value)
        U_value = I_value[1]
        U_values.append(U_value)
        if v <= c - 2:
            J_values.append(endpoint_integral(R, u, 1, prime))

        D_pair = coefficient_digit(R, K, prime)
        assert D_pair[1] == 0
        D_value = D_pair[0]
        D_values.append(D_value)
        phi_value = phi_mod(n, s, prime)
        phis.append(phi_value)
        kappa = kappa_value(n, v, ell, K, factorial, prime)
        assert kappa != 0
        kappas.append(kappa)
        assert D_value == kappa * phi_value % prime
        normalized_I.append(gscale(pow(kappa, -1, prime), I_value, prime))
        if v <= c - 2:
            normalized_J.append(
                gscale(pow(kappa, -1, prime), J_values[v], prime)
            )

        target = None
        if q_quotient is not None:
            original_target = (
                4 * q_quotient * U_value - p_value * D_value
            ) % prime
            normalized_target = (
                4 * q_quotient * normalized_I[v][1]
                - p_value * phi_value
            ) % prime
            assert normalized_target == original_target * pow(kappa, -1, prime) % prime
            target = original_target
            target_values.append(target)
            if D_value != 0 and U_value != 0 and target == 0:
                left = 4 * q_quotient * U_value % prime
                right = p_value * D_value % prime
                normalized_left = (
                    4 * q_quotient * normalized_I[v][1] % prime
                )
                normalized_right = p_value * phi_value % prime
                target_records.append(
                    {
                        "v": v,
                        "s": s,
                        "K": K,
                        "D": D_value,
                        "U": U_value,
                        "kappa": kappa,
                        "Phi": phi_value,
                        "normalized_U": normalized_I[v][1],
                        "left_side_mod_prime": left,
                        "right_side_mod_prime": right,
                        "normalized_left_side_mod_prime": normalized_left,
                        "normalized_right_side_mod_prime": normalized_right,
                    }
                )
        transcript.append(
            (
                f"v={v};s={s};K={K};u={u};"
                f"I={I_value[0]},{I_value[1]};"
                f"D={D_value};U={U_value};Phi={phi_value};"
                f"kappa={kappa};target={target}"
            )
        )
        if v + 1 < c:
            R = multiply_one_plus_z_squared(R, prime)

    relation_checks = 0
    transition_checks = 0
    normalized_relation_checks = 0
    pivot_b1_values: list[int] = []
    pivot_g2_scalar_values: list[int] = []
    for v in range(max(0, c - 2)):
        coefficients = recurrence_coefficients(n, c, v, prime)
        b1_integer = c + 2 * n + v + 3
        g2_scalar_integer = c - v - 2
        assert coefficients["b1"] == (b1_integer % prime, 0)
        assert coefficients["g2"] == (0, g2_scalar_integer % prime)
        assert c + 2 * n + 3 <= b1_integer <= 2 * c + 2 * n
        assert 1 <= g2_scalar_integer <= c - 2
        assert b1_integer <= prime - 1
        assert coefficients["b1"] != (0, 0)
        assert coefficients["g2"] != (0, 0)
        pivot_b1_values.append(b1_integer)
        pivot_g2_scalar_values.append(g2_scalar_integer)

        first_relation = relation_sum(
            [
                (coefficients["a0"], I_values[v]),
                (coefficients["a1"], I_values[v + 1]),
                (coefficients["b0"], J_values[v]),
                (coefficients["b1"], J_values[v + 1]),
            ],
            prime,
        )
        second_relation = relation_sum(
            [
                (coefficients["g0"], I_values[v]),
                (coefficients["g1"], I_values[v + 1]),
                (coefficients["g2"], I_values[v + 2]),
                (coefficients["d0"], J_values[v]),
                (coefficients["d1"], J_values[v + 1]),
            ],
            prime,
        )
        assert first_relation == second_relation == (0, 0)
        relation_checks += 2

        predicted_J_next = gscale(
            -1,
            gdiv(
                relation_sum(
                    [
                        (coefficients["a0"], I_values[v]),
                        (coefficients["a1"], I_values[v + 1]),
                        (coefficients["b0"], J_values[v]),
                    ],
                    prime,
                ),
                coefficients["b1"],
                prime,
            ),
            prime,
        )
        assert predicted_J_next == J_values[v + 1]
        predicted_I_next_next = gscale(
            -1,
            gdiv(
                relation_sum(
                    [
                        (coefficients["g0"], I_values[v]),
                        (coefficients["g1"], I_values[v + 1]),
                        (coefficients["d0"], J_values[v]),
                        (coefficients["d1"], J_values[v + 1]),
                    ],
                    prime,
                ),
                coefficients["g2"],
                prime,
            ),
            prime,
        )
        assert predicted_I_next_next == I_values[v + 2]
        transition_checks += 2

        lambda_value = kappas[v + 1] * pow(kappas[v], -1, prime) % prime
        lambda_formula = (
            (2 * v + 2)
            * (2 * v + 3)
            * pow(((prime + 2 * v + 1) // 2 + 1), -1, prime)
            * pow((n + (prime + 2 * v + 1) // 2 + 1), -1, prime)
        ) % prime
        assert lambda_value == lambda_formula != 0
        mu_value = kappas[v + 2] * pow(kappas[v], -1, prime) % prime
        first_normalized_relation = relation_sum(
            [
                (coefficients["a0"], normalized_I[v]),
                (
                    gscale(lambda_value, coefficients["a1"], prime),
                    normalized_I[v + 1],
                ),
                (coefficients["b0"], normalized_J[v]),
                (
                    gscale(lambda_value, coefficients["b1"], prime),
                    normalized_J[v + 1],
                ),
            ],
            prime,
        )
        second_normalized_relation = relation_sum(
            [
                (coefficients["g0"], normalized_I[v]),
                (
                    gscale(lambda_value, coefficients["g1"], prime),
                    normalized_I[v + 1],
                ),
                (
                    gscale(mu_value, coefficients["g2"], prime),
                    normalized_I[v + 2],
                ),
                (coefficients["d0"], normalized_J[v]),
                (
                    gscale(lambda_value, coefficients["d1"], prime),
                    normalized_J[v + 1],
                ),
            ],
            prime,
        )
        assert first_normalized_relation == second_normalized_relation == (0, 0)
        normalized_relation_checks += 2

    return {
        "n": n,
        "prime": prime,
        "c": c,
        "admissible_v_count": c,
        "recurrence_step_count": max(0, c - 2),
        "unnormalized_relation_checks": relation_checks,
        "transition_reconstruction_checks": transition_checks,
        "normalized_relation_checks": normalized_relation_checks,
        "b1_integer_range": (
            [min(pivot_b1_values), max(pivot_b1_values)]
            if pivot_b1_values
            else []
        ),
        "g2_scalar_integer_range": (
            [min(pivot_g2_scalar_values), max(pivot_g2_scalar_values)]
            if pivot_g2_scalar_values
            else []
        ),
        "v_prime_q_n": q_valuation,
        "q_n_over_prime_mod_prime": q_quotient,
        "q_n_mod_prime_squared": q_value % (prime * prime),
        "p_n_mod_prime": p_value % prime,
        "generic_target_zero_records": target_records,
        "all_target_zero_v": (
            [index for index, value in enumerate(target_values) if value == 0]
            if q_quotient is not None
            else []
        ),
        "target_sequence_sha256": (
            hashlib.sha256(
                ",".join(str(value) for value in target_values).encode("ascii")
            ).hexdigest()
            if q_quotient is not None
            else None
        ),
        "state_transcript_sha256": hashlib.sha256(
            "\n".join(transcript).encode("ascii")
        ).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "critical_fourier_normalized_three_dimensional_recurrence_"
            "certificate.json"
        ),
    )
    arguments = parser.parse_args()
    cases = [
        verify_case(4, 43),
        verify_case(64, 937),
        verify_case(82, 953),
    ]
    assert cases[1]["generic_target_zero_records"] == [
        {
            "v": 264,
            "s": 529,
            "K": 797,
            "D": 257,
            "U": 463,
            "kappa": 586,
            "Phi": 373,
            "normalized_U": 610,
            "left_side_mod_prime": 833,
            "right_side_mod_prime": 833,
            "normalized_left_side_mod_prime": 35,
            "normalized_right_side_mod_prime": 35,
        }
    ]
    assert cases[2]["v_prime_q_n"] == 1
    assert cases[2]["q_n_over_prime_mod_prime"] == 149
    assert cases[2]["q_n_mod_prime_squared"] == 141997
    assert cases[2]["p_n_mod_prime"] == 662
    assert cases[2]["all_target_zero_v"] == [55, 281]
    assert cases[2]["generic_target_zero_records"] == [
        {
            "v": 55,
            "s": 111,
            "K": 614,
            "D": 405,
            "U": 210,
            "kappa": 49,
            "Phi": 300,
            "normalized_U": 685,
            "left_side_mod_prime": 317,
            "right_side_mod_prime": 317,
            "normalized_left_side_mod_prime": 376,
            "normalized_right_side_mod_prime": 376,
        },
        {
            "v": 281,
            "s": 563,
            "K": 840,
            "D": 402,
            "U": 632,
            "kappa": 819,
            "Phi": 950,
            "normalized_U": 422,
            "left_side_mod_prime": 237,
            "right_side_mod_prime": 237,
            "normalized_left_side_mod_prime": 873,
            "normalized_right_side_mod_prime": 873,
        },
    ]
    output = {
        "description": (
            "Exact Gaussian-residue-ring certificate for the normalized "
            "three-dimensional endpoint-integral recurrence"
        ),
        "proof_status": (
            "The finite checks are diagnostic; the all-parameter proof "
            "is in the companion source note."
        ),
        "cases": cases,
        "two_return_counterexample": cases[2],
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
