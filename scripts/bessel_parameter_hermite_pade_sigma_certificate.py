#!/usr/bin/env python3
"""Exact checks for the Bessel shift-Pade and Sigma-operator barrier."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


Polynomial = tuple[int, ...]


def normalize(values: list[int] | tuple[int, ...]) -> Polynomial:
    answer = list(values)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return tuple(answer)


def poly_add(first: Polynomial, second: Polynomial) -> Polynomial:
    length = max(len(first), len(second))
    return normalize(
        [
            (first[index] if index < len(first) else 0)
            + (second[index] if index < len(second) else 0)
            for index in range(length)
        ]
    )


def poly_scale(value: int, polynomial: Polynomial) -> Polynomial:
    return normalize([value * coefficient for coefficient in polynomial])


def poly_sub(first: Polynomial, second: Polynomial) -> Polynomial:
    return poly_add(first, poly_scale(-1, second))


def poly_mul(first: Polynomial, second: Polynomial) -> Polynomial:
    answer = [0] * (len(first) + len(second) - 1)
    for first_index, first_value in enumerate(first):
        for second_index, second_value in enumerate(second):
            answer[first_index + second_index] += first_value * second_value
    return normalize(answer)


def poly_eval(polynomial: Polynomial, value: int) -> int:
    answer = 0
    for coefficient in reversed(polynomial):
        answer = answer * value + coefficient
    return answer


def affine_times(polynomial: Polynomial, constant: int) -> Polynomial:
    """Return (4*x + constant) * polynomial."""
    return poly_mul((constant, 4), polynomial)


def shift_coefficients(
    minimum_index: int, maximum_index: int
) -> tuple[dict[int, Polynomial], dict[int, Polynomial]]:
    assert minimum_index <= 0 and maximum_index >= 1
    u_values: dict[int, Polynomial] = {0: (1,), 1: (0,)}
    v_values: dict[int, Polynomial] = {0: (0,), 1: (1,)}

    for index in range(1, maximum_index):
        coefficient = 4 * index + 2
        u_values[index + 1] = poly_add(
            poly_scale(-1, affine_times(u_values[index], coefficient)),
            u_values[index - 1],
        )
        v_values[index + 1] = poly_add(
            poly_scale(-1, affine_times(v_values[index], coefficient)),
            v_values[index - 1],
        )

    for index in range(0, minimum_index, -1):
        coefficient = 4 * index + 2
        u_values[index - 1] = poly_add(
            u_values[index + 1],
            affine_times(u_values[index], coefficient),
        )
        v_values[index - 1] = poly_add(
            v_values[index + 1],
            affine_times(v_values[index], coefficient),
        )

    return u_values, v_values


def bessel_denominators(maximum_index: int) -> list[int]:
    values = [1, 1]
    for index in range(2, maximum_index + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def normalized_value(index: int, denominators: list[int]) -> int:
    return (-1) ** index * denominators[index]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def valuation(value: int, prime: int) -> int | None:
    if value == 0:
        return None
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def shift_module_checks() -> dict[str, object]:
    minimum_index = -14
    maximum_index = 18
    u_values, v_values = shift_coefficients(minimum_index, maximum_index)
    determinant_checks = 0
    for index in range(minimum_index, maximum_index):
        determinant = poly_sub(
            poly_mul(u_values[index], v_values[index + 1]),
            poly_mul(u_values[index + 1], v_values[index]),
        )
        expected_sign = -1 if index % 2 else 1
        assert determinant == (expected_sign,)
        determinant_checks += 1

    denominators = bessel_denominators(100)
    shift_checks = 0
    linear_form_checks = 0
    for base_index in range(20, 61):
        base_value = normalized_value(base_index, denominators)
        next_value = normalized_value(base_index + 1, denominators)
        for shift in range(minimum_index, maximum_index + 1):
            predicted = (
                poly_eval(u_values[shift], base_index) * base_value
                + poly_eval(v_values[shift], base_index) * next_value
            )
            assert predicted == normalized_value(
                base_index + shift, denominators
            )
            shift_checks += 1

        # A deterministic nontrivial integral-polynomial shift form.
        selected_shifts = [-7, -2, 0, 1, 5, 11]
        polynomials = {
            shift: normalize(
                [
                    3 * shift - 1,
                    shift * shift + 2,
                    -1 if shift % 2 else 1,
                ]
            )
            for shift in selected_shifts
        }
        a_polynomial = (0,)
        b_polynomial = (0,)
        direct_value = 0
        for shift, polynomial in polynomials.items():
            a_polynomial = poly_add(
                a_polynomial, poly_mul(polynomial, u_values[shift])
            )
            b_polynomial = poly_add(
                b_polynomial, poly_mul(polynomial, v_values[shift])
            )
            direct_value += (
                poly_eval(polynomial, base_index)
                * normalized_value(base_index + shift, denominators)
            )
        reduced_value = (
            poly_eval(a_polynomial, base_index) * base_value
            + poly_eval(b_polynomial, base_index) * next_value
        )
        assert direct_value == reduced_value
        linear_form_checks += 1

    return {
        "index_range": [minimum_index, maximum_index],
        "unimodular_determinant_checks": determinant_checks,
        "integer_shift_identity_checks": shift_checks,
        "linear_shift_form_checks": linear_form_checks,
        "representative_coefficients": {
            str(index): {
                "U_ascending_coefficients": list(u_values[index]),
                "V_ascending_coefficients": list(v_values[index]),
            }
            for index in [-3, -1, 0, 1, 2, 5]
        },
    }


def root_boundary_checks() -> dict[str, object]:
    maximum_prime = 127
    primes = [
        value for value in range(3, maximum_prime + 1) if is_prime(value)
    ]
    denominators = bessel_denominators(maximum_prime + 2)
    root_classes = 0
    hankel_checks = 0
    representatives: list[dict[str, int]] = []
    for prime in primes:
        for residue in range(prime):
            if denominators[residue] % prime != 0:
                continue
            root_classes += 1
            assert denominators[residue + 1] % prime != 0
            f_zero = normalized_value(residue, denominators)
            f_one = normalized_value(residue + 1, denominators)
            f_two = normalized_value(residue + 2, denominators)
            hankel = f_zero * f_two - f_one * f_one
            assert hankel % prime == (-f_one * f_one) % prime
            assert hankel % prime != 0
            hankel_checks += 1
            if len(representatives) < 12:
                representatives.append(
                    {
                        "p": prime,
                        "r": residue,
                        "q_r_mod_p": denominators[residue] % prime,
                        "q_r_plus_1_mod_p": (
                            denominators[residue + 1] % prime
                        ),
                        "Hankel_mod_p": hankel % prime,
                    }
                )
    assert root_classes > 0
    return {
        "prime_range": [3, maximum_prime],
        "root_classes": root_classes,
        "boundary_unit_checks": root_classes,
        "Hankel_unit_checks": hankel_checks,
        "representative_records": representatives,
    }


def growth_and_irregularity_checks() -> dict[str, object]:
    maximum_index = 160
    denominators = bessel_denominators(maximum_index)
    product = 1
    growth_checks = 0
    ratios: list[dict[str, int]] = []
    for index in range(2, maximum_index + 1):
        product *= 4 * index - 2
        assert denominators[index] > product
        growth_checks += 1
        if index in [2, 5, 20, 80, 160]:
            ratios.append(
                {
                    "n": index,
                    "q_n": denominators[index],
                    "lower_product": product,
                }
            )

    # If y'/y = 1/4 - 1/(2z) - 1/(4z^2), then
    # 4z^2*y'/y + 1 + 2z - z^2 is identically zero.
    logarithmic_derivative_after_multiplication = {
        "z^2": 1,
        "z": -2,
        "constant": -1,
    }
    operator_lower_terms = {
        "z^2": -1,
        "z": 2,
        "constant": 1,
    }
    assert all(
        logarithmic_derivative_after_multiplication[key]
        + operator_lower_terms[key]
        == 0
        for key in logarithmic_derivative_after_multiplication
    )

    return {
        "factorial_growth_checks": growth_checks,
        "representative_growth_records": ratios,
        "M_of_R": "4*z^2*d/dz + 1 + 2*z - z^2",
        "coefficient_quotient_pole_order_at_zero": 2,
        "homogeneous_solution": "z^(-1/2)*exp(z/4 + 1/(4z))",
        "homogeneous_solution_identity_checked": True,
    }


def residual_polynomial_checks() -> dict[str, object]:
    polynomials: list[Polynomial] = [
        (3, -2, 5),
        (-7, 0, 1, 4),
        (11, -9, 3, 0, -2),
        (1, 1),
    ]
    checks = 0
    for prime in [3, 5, 7, 11]:
        for rho_integer in range(0, 40):
            for exponent in range(1, 5):
                n_value = rho_integer + prime**exponent
                for polynomial in polynomials:
                    rho_value = poly_eval(polynomial, rho_integer)
                    n_polynomial_value = poly_eval(polynomial, n_value)
                    difference = n_polynomial_value - rho_value
                    difference_valuation = valuation(difference, prime)
                    assert difference_valuation is None or (
                        difference_valuation >= exponent
                    )

                    rho_valuation = valuation(rho_value, prime)
                    n_valuation = valuation(n_polynomial_value, prime)
                    if n_polynomial_value != 0:
                        lower_exponent = exponent
                        if rho_valuation is not None:
                            lower_exponent = min(
                                lower_exponent, rho_valuation
                            )
                        assert n_valuation is not None
                        assert n_valuation >= lower_exponent
                        degree = len(polynomial) - 1
                        height = max(abs(value) for value in polynomial)
                        size_upper = (
                            (degree + 1)
                            * height
                            * max(1, n_value) ** degree
                        )
                        assert prime**lower_exponent <= abs(
                            n_polynomial_value
                        )
                        assert abs(n_polynomial_value) <= size_upper
                    checks += 1
    return {
        "integer_Lipschitz_and_height_checks": checks,
        "polynomials_ascending_coefficients": [
            list(polynomial) for polynomial in polynomials
        ],
    }


def derivative_tail_checks() -> dict[str, object]:
    checks = 0
    representatives: list[dict[str, int]] = []
    for integer_index in range(0, 16):
        for term_index in range(integer_index + 1, 41):
            product_without_zero = math.prod(
                integer_index + offset
                for offset in range(-term_index + 1, term_index + 1)
                if offset != -integer_index
            )
            signed_numerator = (-1 if term_index % 2 else 1) * (
                product_without_zero
            )
            assert signed_numerator % math.factorial(term_index) == 0
            direct_derivative = signed_numerator // math.factorial(
                term_index
            )
            predicted_derivative = (
                (-1 if (integer_index + 1) % 2 else 1)
                * math.factorial(term_index - integer_index - 1)
                * math.factorial(integer_index + term_index)
                // math.factorial(term_index)
            )
            assert direct_derivative == predicted_derivative
            if integer_index == 0:
                assert direct_derivative == -math.factorial(term_index - 1)
            checks += 1
            if (integer_index, term_index) in [
                (0, 1),
                (0, 12),
                (4, 9),
                (15, 40),
            ]:
                representatives.append(
                    {
                        "n": integer_index,
                        "k": term_index,
                        "T_k_prime_at_n": direct_derivative,
                    }
                )
    return {
        "nonterminating_derivative_checks": checks,
        "representative_records": representatives,
        "n_equals_zero_identity": "T_k'(0)=-(k-1)! for k>=1",
        "consequence": "f_p'(0)=-sum_{m>=0} m!",
    }


def determinant_branch_checks() -> dict[str, object]:
    u_values, v_values = shift_coefficients(-2, 4)

    # Canonical Hankel matrix [[f_0,f_1],[f_1,f_2]].
    hankel_b_determinant = poly_sub(
        poly_mul(v_values[0], v_values[2]),
        poly_mul(v_values[1], v_values[1]),
    )
    assert hankel_b_determinant == (-1,)

    # Matrix [[f_0,f_1],[2f_0,f_2]] has identically singular B-matrix,
    # so its formal determinant has an F factor.
    zero_preserving_b_determinant = poly_sub(
        poly_mul(v_values[0], v_values[2]),
        poly_mul(v_values[1], poly_scale(2, v_values[0])),
    )
    assert zero_preserving_b_determinant == (0,)
    quotient_f_coefficient = poly_sub(
        u_values[2], poly_scale(2, u_values[1])
    )
    quotient_g_coefficient = poly_sub(
        v_values[2], poly_scale(2, v_values[1])
    )

    denominators = bessel_denominators(50)
    integer_factor_checks = 0
    for index in range(0, 49):
        f_zero = normalized_value(index, denominators)
        f_one = normalized_value(index + 1, denominators)
        f_two = (
            poly_eval(u_values[2], index) * f_zero
            + poly_eval(v_values[2], index) * f_one
        )
        determinant = f_zero * f_two - f_one * (2 * f_zero)
        quotient = (
            poly_eval(quotient_f_coefficient, index) * f_zero
            + poly_eval(quotient_g_coefficient, index) * f_one
        )
        assert determinant == f_zero * quotient
        if determinant != 0:
            assert abs(determinant) >= denominators[index]
        integer_factor_checks += 1

    return {
        "Hankel_B_determinant": list(hankel_b_determinant),
        "zero_preserving_B_determinant": list(
            zero_preserving_b_determinant
        ),
        "zero_preserving_quotient_F_coefficient": list(
            quotient_f_coefficient
        ),
        "zero_preserving_quotient_G_coefficient": list(
            quotient_g_coefficient
        ),
        "integer_q_factor_checks": integer_factor_checks,
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for the Bessel parameter shift "
            "Hermite-Pade determinant and Sigma-operator barrier"
        ),
        "shift_module": shift_module_checks(),
        "ordinary_root_boundary": root_boundary_checks(),
        "growth_and_irregularity": growth_and_irregularity_checks(),
        "determinant_dichotomy": determinant_branch_checks(),
        "derivative_tail": derivative_tail_checks(),
        "residual_polynomial_bound": residual_polynomial_checks(),
        "status": (
            "finite diagnostic; the all-index shift reduction, Sigma "
            "exclusion, determinant dichotomy, and asymptotic conclusions "
            "are proved symbolically in the companion source; no digit-"
            "depth bound or algebraicity of a Bessel zero is claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_parameter_hermite_pade_sigma_certificate.json"
    )
    parser.add_argument("--output", type=Path, default=default_output)
    arguments = parser.parse_args()
    payload = build_payload()
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_bytes(encoded)
    print(f"wrote {arguments.output}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")


if __name__ == "__main__":
    main()
