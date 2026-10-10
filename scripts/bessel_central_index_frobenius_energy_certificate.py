#!/usr/bin/env python3
"""Certificate for the central index-Frobenius/energy note.

The source note contains the all-degree proofs.  This program performs exact
polynomial checks, modular adversarial checks, and one explicitly finite gcd
scan.  The scan is evidence only and is not promoted to a theorem.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial, gcd
from pathlib import Path


Poly = list[Fraction]


def trim(poly: Poly) -> Poly:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: Poly, right: Poly, scale: Fraction = Fraction(1)) -> Poly:
    out = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += scale * value
    return trim(out)


def poly_scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim([scalar * value for value in poly])


def poly_product(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            out[i + j] += first * second
    return trim(out)


def poly_derivative(poly: Poly) -> Poly:
    if len(poly) == 1:
        return [Fraction(0)]
    return trim([index * poly[index] for index in range(1, len(poly))])


def poly_shift(poly: Poly, delta: int) -> Poly:
    """Return f(x+delta)."""
    out = [Fraction(0) for _ in range(len(poly))]
    for degree, value in enumerate(poly):
        for exponent in range(degree + 1):
            out[exponent] += value * comb(degree, exponent) * delta ** (degree - exponent)
    return trim(out)


def falling_poly(order: int) -> Poly:
    out = [Fraction(1)]
    for shift in range(order):
        out = poly_product(out, [Fraction(-shift), Fraction(1)])
    return out


def charlier_poly(degree: int) -> Poly:
    out = [Fraction(0)]
    for order in range(degree + 1):
        out = poly_add(out, poly_scale(falling_poly(order), Fraction(comb(degree, order))))
    return out


def rational_mod(value: Fraction, modulus: int) -> int:
    numerator = value.numerator % modulus
    denominator = value.denominator % modulus
    if gcd(denominator, modulus) != 1:
        raise AssertionError(f"nonunit denominator {value.denominator} modulo {modulus}")
    return numerator * pow(denominator, -1, modulus) % modulus


def poly_mod(poly: Poly, prime: int) -> tuple[int, ...]:
    values = [rational_mod(value, prime) for value in poly]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def correction_poly(prime: int, degree: int) -> Poly:
    f = charlier_poly(degree)
    out = poly_scale(poly_product(falling_poly(prime), poly_derivative(f)), Fraction(-1))
    for order in range(1, prime):
        difference = poly_add(poly_shift(f, -order), f, Fraction(-1))
        term = poly_product(falling_poly(order), difference)
        scalar = Fraction((-1) ** (order - 1), order)
        out = poly_add(out, poly_scale(term, scalar))
    return trim(out)


def check_index_identities() -> dict[str, object]:
    cases = []
    for prime in (3, 5, 7):
        fp = charlier_poly(prime)
        for degree in range(prime):
            fn = charlier_poly(degree)
            left = charlier_poly(prime + degree)

            addition = [Fraction(0)]
            for order in range(prime + 1):
                term = poly_product(falling_poly(order), poly_shift(fn, -order))
                addition = poly_add(
                    addition,
                    poly_scale(term, Fraction(comb(prime, order))),
                )
            assert left == addition

            exact_difference = poly_add(left, poly_product(fp, fn), Fraction(-1))
            rhs_difference = poly_product(
                falling_poly(prime),
                poly_add(poly_shift(fn, -prime), fn, Fraction(-1)),
            )
            for order in range(1, prime):
                translated = poly_add(poly_shift(fn, -order), fn, Fraction(-1))
                term = poly_product(falling_poly(order), translated)
                rhs_difference = poly_add(
                    rhs_difference,
                    poly_scale(term, Fraction(comb(prime, order))),
                )
            assert exact_difference == rhs_difference

            quotient = poly_scale(exact_difference, Fraction(1, prime))
            correction = correction_poly(prime, degree)
            assert poly_mod(quotient, prime) == poly_mod(correction, prime)
            cases.append([prime, degree])
    return {"case_count": len(cases), "cases": cases}


def uw_mod(limit: int, modulus: int) -> tuple[list[int], list[int]]:
    u = [1, 1]
    w = [0, 1]
    for n in range(1, limit):
        u.append(((1 - 2 * n) * u[n] + 4 * n * u[n - 1]) % modulus)
        w.append((u[n] + (1 - 2 * n) * w[n] + 4 * n * w[n - 1]) % modulus)
    return u, w


def check_401_counterexample() -> dict[str, object]:
    prime = 401
    base_index = 317
    propagated_index = base_index + prime

    u_exact_previous, u_exact = 1, 1
    w_exact_previous, w_exact = 0, 1
    for n in range(1, base_index):
        u_next = (1 - 2 * n) * u_exact + 4 * n * u_exact_previous
        w_next = u_exact + (1 - 2 * n) * w_exact + 4 * n * w_exact_previous
        u_exact_previous, u_exact = u_exact, u_next
        w_exact_previous, w_exact = w_exact, w_next
    exact_gcd = gcd(abs(u_exact), abs(w_exact))
    assert exact_gcd == 1203

    u_prime, w_prime = uw_mod(318, prime)
    expected_table = {
        313: [179, 223],
        314: [204, 385],
        315: [275, 0],
        316: [256, 165],
        317: [0, 0],
        318: [199, 299],
    }
    actual_table = {index: [u_prime[index], w_prime[index]] for index in expected_table}
    assert actual_table == expected_table

    modulus = prime * prime
    u_lift, w_lift = uw_mod(propagated_index, modulus)
    base_digits = [u_lift[base_index] // prime % prime, w_lift[base_index] // prime % prime]
    propagated_digits = [
        u_lift[propagated_index] // prime % prime,
        w_lift[propagated_index] // prime % prime,
    ]
    assert base_digits == [188, 361]
    assert propagated_digits == [233, 111]
    corrections = [
        (propagated_digits[0] - 2 * base_digits[0]) % prime,
        (propagated_digits[1] + base_digits[0] - 2 * base_digits[1]) % prime,
    ]
    assert corrections == [258, 379]

    return {
        "prime": prime,
        "base_index": base_index,
        "propagated_index": propagated_index,
        "exact_gcd_at_base": exact_gcd,
        "mod_prime_table": actual_table,
        "base_lift_digits": base_digits,
        "propagated_lift_digits": propagated_digits,
        "index_correction_digits": corrections,
    }


def universal_b_mod(prime: int) -> list[int]:
    m = (prime - 1) // 2
    values = [0, 1]
    for r in range(1, m):
        numerator = (2 * r - 1) * (2 * values[r] - values[r - 1])
        values.append(numerator * pow(2 * r + 1, -1, prime) % prime)
    return values


def energy_form(coefficients: list[int], prime: int) -> int:
    answer = 0
    for i, first in enumerate(coefficients):
        for j, second in enumerate(coefficients):
            answer += first * second * pow(i + j + 2, -1, prime)
    return answer % prime


def check_resonance_and_energy() -> dict[str, object]:
    prime = 79
    m = (prime - 1) // 2
    b = universal_b_mod(prime)
    defect = (b[m - 1] - 2 * b[m]) % prime
    beta = sum(b[r] * pow(r, -1, prime) for r in range(1, m + 1)) % prime
    assert defect == 0

    # K(z)=sum_{i=0}^{m-1} b_{i+1} z^i.  Check (28) coefficientwise.
    k = b[1:]
    derivative = [(index + 1) * k[index + 1] % prime for index in range(len(k) - 1)]
    # Build 2z(1-z)^2 K' + (1-2z+3z^2)K.
    def mul_mod(left: list[int], right: list[int], modulus: int) -> list[int]:
        out = [0] * (len(left) + len(right) - 1)
        for i, first in enumerate(left):
            for j, second in enumerate(right):
                out[i + j] = (out[i + j] + first * second) % modulus
        return out

    first = mul_mod([0, 2, -4, 2], derivative, prime)
    second = mul_mod([1, -2, 3], k, prime)
    size = max(len(first), len(second))
    ode = [0] * size
    for index in range(size):
        ode[index] = (
            (first[index] if index < len(first) else 0)
            + (second[index] if index < len(second) else 0)
        ) % prime
    while len(ode) > 1 and ode[-1] == 0:
        ode.pop()
    assert ode == [1]

    residual_checks = {}
    for test_prime in (5, 7, 11, 13, 79):
        test_m = (test_prime - 1) // 2
        test_b = universal_b_mod(test_prime)
        test_defect = (test_b[test_m - 1] - 2 * test_b[test_m]) % test_prime
        b_poly = test_b[:]
        b_derivative = [
            index * b_poly[index] % test_prime for index in range(1, len(b_poly))
        ]
        first_b = mul_mod([0, 2, -4, 2], b_derivative, test_prime)
        second_b = mul_mod([-1, 2, 1], b_poly, test_prime)
        residual_size = max(len(first_b), len(second_b), 2)
        residual = [0] * residual_size
        for index in range(residual_size):
            residual[index] = (
                (first_b[index] if index < len(first_b) else 0)
                + (second_b[index] if index < len(second_b) else 0)
                - (1 if index == 1 else 0)
            ) % test_prime
        expected = [0] * (test_m + 2)
        expected[test_m + 1] = (2 * test_m - 1) * test_defect % test_prime
        while len(residual) > 1 and residual[-1] == 0:
            residual.pop()
        while len(expected) > 1 and expected[-1] == 0:
            expected.pop()
        assert residual == expected
        residual_checks[str(test_prime)] = {
            "m": test_m,
            "D_m": test_defect,
            "residual_coefficient": expected[-1] if len(expected) > 1 else 0,
        }

    quadratic = energy_form(k, prime)
    anomaly = b[m] * b[m] % prime
    assert beta == (2 * quadratic - anomaly) % prime
    assert [beta, quadratic, b[m], anomaly] == [16, 5, 51, 73]

    isotropic_prime = 11
    isotropic = [1, 0, 1, 3, 1]
    assert sum(isotropic) % isotropic_prime == pow(2, -1, isotropic_prime)
    isotropic_energy = energy_form(isotropic, isotropic_prime)
    isotropic_r = (2 * isotropic_energy - isotropic[-1] ** 2) % isotropic_prime
    assert [isotropic_energy, isotropic_r] == [6, 0]

    return {
        "prime": prime,
        "m": m,
        "defect_D_m": defect,
        "beta_m": beta,
        "energy_Q_K": quadratic,
        "frobenius_top_coefficient_anomaly_B_m_squared": anomaly,
        "corrected_energy_2Q_minus_B_m_squared": (2 * quadratic - anomaly) % prime,
        "ode_degree": len(k) - 1,
        "resonant_residual_checks": residual_checks,
        "unrestricted_isotropic_example": {
            "prime": isotropic_prime,
            "coefficients_low_to_high": isotropic,
            "f_at_0": isotropic[0],
            "f_at_1": sum(isotropic) % isotropic_prime,
            "energy_Q": isotropic_energy,
            "corrected_form_R": isotropic_r,
        },
    }


def harmonic_data(k: int, prime: int) -> tuple[int, int]:
    harmonic = 0
    odd_harmonic = 0
    for r in range(1, k + 1):
        harmonic = (harmonic + pow(r, -1, prime)) % prime
        odd_harmonic = (odd_harmonic + pow(2 * r - 1, -1, prime)) % prime
    return harmonic, odd_harmonic


def a_low_mod(k: int, modulus: int) -> int:
    value = 1
    for r in range(1, k + 1):
        value = value * (2 * r - 1) ** 2 % modulus
        value = value * pow(4 * r, -1, modulus) % modulus
    return value


def ratio_r_exact(prime: int, k: int) -> Fraction:
    central = Fraction(comb(2 * prime, prime) ** 2 * factorial(prime - 1), 16**prime)
    shift = Fraction(1)
    for r in range(k):
        shift *= Fraction(2 * prime + 2 * r + 1, 2 * r + 1) ** 2
        shift *= Fraction(r + 1, prime + r + 1)
    return central * shift


def a_fraction(k: int) -> Fraction:
    value = Fraction(1)
    for r in range(1, k + 1):
        value *= Fraction((2 * r - 1) ** 2, 4 * r)
    return value


def check_dwork_blocks() -> dict[str, object]:
    checked_primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 79]
    checked_pairs = 0
    for prime in checked_primes:
        m = (prime - 1) // 2
        modulus = prime * prime
        wilson = (factorial(prime - 1) + 1) // prime % prime
        fermat16 = (pow(16, prime - 1, prime * prime) - 1) // prime % prime
        inverse_four = pow(4, -1, modulus)
        for k in range(m + 1):
            harmonic, odd_harmonic = harmonic_data(k, prime)
            correction = (4 * odd_harmonic - harmonic - wilson - fermat16) % prime
            predicted = (-inverse_four * (1 + prime * correction)) % modulus
            actual = rational_mod(ratio_r_exact(prime, k), modulus)
            assert actual == predicted
            checked_pairs += 1

    prime = 79
    m = (prime - 1) // 2
    modulus = prime * prime
    low_values = [a_low_mod(k, modulus) for k in range(m + 1)]
    total = sum(low_values) % modulus
    assert total % prime == 0
    lift_digit = total // prime % prime
    weighted = 0
    for k, value in enumerate(low_values):
        harmonic, odd_harmonic = harmonic_data(k, prime)
        weighted += (value % prime) * (4 * odd_harmonic - harmonic)
    weighted %= prime

    block = sum((a_fraction(prime + k) for k in range(m + 1)), Fraction(0))
    block_digit = rational_mod(block / (prime * prime), prime)
    predicted_block = -pow(4, -1, prime) * (lift_digit + weighted) % prime
    assert [lift_digit, weighted, block_digit, predicted_block] == [67, 7, 21, 21]

    return {
        "checked_primes": checked_primes,
        "checked_prime_k_pairs": checked_pairs,
        "p79": {
            "m": m,
            "T_m_over_p": lift_digit,
            "weighted_harmonic_sum": weighted,
            "next_block_over_p_squared": block_digit,
            "predicted_next_block": predicted_block,
        },
    }


def finite_gcd_scan(limit: int = 3000) -> dict[str, object]:
    u_previous, u_current = 1, 1
    w_previous, w_current = 0, 1
    non_three = []
    count_nontrivial = 0
    largest_gap = -10**18
    largest_gap_pair = None

    for index in range(1, limit + 1):
        if index > 1:
            n = index - 1
            u_next = (1 - 2 * n) * u_current + 4 * n * u_previous
            w_next = u_current + (1 - 2 * n) * w_current + 4 * n * w_previous
            u_previous, u_current = u_current, u_next
            w_previous, w_current = w_current, w_next

        common = gcd(abs(u_current), abs(w_current))
        if common == 1:
            continue
        count_nontrivial += 1
        residual = common
        factors = []
        for prime in (3, 401):
            exponent = 0
            while residual % prime == 0:
                residual //= prime
                exponent += 1
            if exponent:
                factors.append([prime, exponent])
                gap = prime - 2 * index
                if gap > largest_gap:
                    largest_gap = gap
                    largest_gap_pair = [index, prime]
        assert residual == 1
        if any(prime != 3 for prime, _ in factors):
            non_three.append([index, common, factors])

    expected_indices = list(range(317, limit + 1, 401))
    assert [record[0] for record in non_three] == expected_indices
    assert largest_gap == -1 and largest_gap_pair == [2, 3]
    return {
        "finite_evidence_only": True,
        "limit": limit,
        "nontrivial_gcd_count": count_nontrivial,
        "non_three_records": non_three,
        "largest_prime_minus_2n": largest_gap,
        "largest_gap_pair_n_prime": largest_gap_pair,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--skip-gcd-scan", action="store_true")
    args = parser.parse_args()

    result = {
        "certificate": "bessel_central_index_frobenius_energy",
        "theorem_checks": {
            "index_identities": check_index_identities(),
            "counterexample_401": check_401_counterexample(),
            "resonance_and_energy": check_resonance_and_energy(),
            "dwork_blocks": check_dwork_blocks(),
        },
        "finite_gcd_scan": None if args.skip_gcd_scan else finite_gcd_scan(),
        "claim_boundary": (
            "All symbolic identities are proved in the source note.  The gcd scan is finite "
            "evidence only and does not prove q <= 2n or central nonvanishing."
        ),
    }

    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
