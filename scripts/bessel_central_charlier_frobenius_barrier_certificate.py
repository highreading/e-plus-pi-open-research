#!/usr/bin/env python3
"""Exact/finite certificate for the central Charlier--Frobenius barrier.

The accompanying source note proves the identities for every admissible
degree and prime.  This script checks representative exact polynomial and
formal-series identities, coefficientwise Wilson congruences at a finite
prime cutoff, the known central root in that cutoff, and one explicitly
reported noncentral repeated Charlier root.

Nothing in the finite checks is asserted as an all-prime nonvanishing
theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


def poly_add(left: list[Fraction], right: list[Fraction], scale: Fraction = Fraction(1)) -> list[Fraction]:
    size = max(len(left), len(right))
    answer = [Fraction(0) for _ in range(size)]
    for index in range(size):
        if index < len(left):
            answer[index] += left[index]
        if index < len(right):
            answer[index] += scale * right[index]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def poly_product(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * coefficient for coefficient in poly]


def poly_derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) <= 1:
        return [Fraction(0)]
    return [index * poly[index] for index in range(1, len(poly))]


def poly_evaluate(poly: list[Fraction], value: int) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def falling_polynomial(order: int) -> list[Fraction]:
    answer = [Fraction(1)]
    for shift in range(order):
        answer = poly_product(answer, [Fraction(-shift), Fraction(1)])
    return answer


def charlier_polynomial(degree: int) -> list[Fraction]:
    answer = [Fraction(0)]
    for order in range(degree + 1):
        answer = poly_add(
            answer,
            poly_scale(falling_polynomial(order), Fraction(comb(degree, order))),
        )
    return answer


def charlier_value_direct(degree: int, parameter: int) -> int:
    falling = 1
    answer = 1
    for order in range(1, degree + 1):
        falling *= parameter - order + 1
        answer += comb(degree, order) * falling
    return answer


def charlier_value_and_derivative_mod(degree: int, parameter: int, modulus: int) -> tuple[int, int]:
    """Evaluate F_degree and its ordinary parameter derivative by recurrence."""
    f_previous, d_previous = 1, 0
    if degree == 0:
        return f_previous, d_previous
    f_current, d_current = (parameter + 1) % modulus, 1
    for n in range(1, degree):
        f_next = ((parameter - n + 1) * f_current + n * f_previous) % modulus
        d_next = (
            f_current
            + (parameter - n + 1) * d_current
            + n * d_previous
        ) % modulus
        f_previous, f_current = f_current, f_next
        d_previous, d_current = d_current, d_next
    return f_current, d_current


def a_and_c_values(limit: int) -> tuple[list[int], list[int]]:
    a_values = [1]
    c_values = [0]
    if limit == 0:
        return a_values, c_values
    a_values.append(2)
    c_values.append(1)
    for n in range(1, limit):
        a_next = 2 * (n + 1) * a_values[n] - n * n * a_values[n - 1]
        c_next = (
            2 * (n + 1) * c_values[n]
            - n * n * c_values[n - 1]
            + a_values[n]
            - n * a_values[n - 1]
        )
        a_values.append(a_next)
        c_values.append(c_next)
    return a_values, c_values


def series_product(left: list[Fraction], right: list[Fraction], limit: int) -> list[Fraction]:
    answer = [Fraction(0) for _ in range(limit + 1)]
    for i, a in enumerate(left[: limit + 1]):
        for j, b in enumerate(right[: limit + 1 - i]):
            answer[i + j] += a * b
    return answer


def harmonic_numbers(limit: int) -> list[Fraction]:
    values = [Fraction(0)]
    for n in range(1, limit + 1):
        values.append(values[-1] + Fraction(1, n))
    return values


def fraction_mod(value: Fraction, modulus: int) -> int:
    denominator = value.denominator % modulus
    return value.numerator % modulus * pow(denominator, -1, modulus) % modulus


def odd_primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (((limit - start) // prime) + 1)
    return [prime for prime in range(3, limit + 1, 2) if sieve[prime]]


def exact_charlier_checks(limit: int) -> dict[str, int]:
    a_values, c_values = a_and_c_values(limit)
    harmonics = harmonic_numbers(limit)

    polynomials = [charlier_polynomial(n) for n in range(limit + 1)]
    for n, polynomial in enumerate(polynomials):
        # Three distinguished values/derivative.
        assert poly_evaluate(polynomial, n) == a_values[n]
        q_value = charlier_value_direct(n, -n - 1)
        assert poly_evaluate(polynomial, -n - 1) == q_value
        assert poly_evaluate(poly_derivative(polynomial), n) == c_values[n]

        # Sum of squarefree coefficients in (1+X)^a, using
        # lambda(X^j)=j! binomial(n,j), is exactly F_n(a).
        for parameter in (-n - 1, -2, 0, n, n + 3):
            falling = 1
            nilpotent_value = Fraction(1)
            for j in range(1, n + 1):
                falling *= parameter - j + 1
                nilpotent_value += comb(n, j) * falling
            assert nilpotent_value == poly_evaluate(polynomial, parameter)

        if n >= 1:
            # Delta_a F_n = n F_{n-1}.
            shifted = poly_evaluate(polynomial, n + 1) - poly_evaluate(polynomial, n)
            assert shifted == n * poly_evaluate(polynomials[n - 1], n)
            # Check the degree-n polynomial identity at n+1 distinct points.
            for parameter in range(-1, n + 1):
                assert (
                    poly_evaluate(polynomial, parameter + 1)
                    - poly_evaluate(polynomial, parameter)
                    == n * poly_evaluate(polynomials[n - 1], parameter)
                )

        if n >= 2:
            predicted = poly_add(
                poly_product([Fraction(1 - (n - 1)), Fraction(1)], polynomials[n - 1]),
                poly_scale(polynomials[n - 2], Fraction(n - 1)),
            )
            assert predicted == polynomial

        # log(1+Delta) and its square recover the first two ordinary
        # derivatives exactly for every polynomial of degree n.
        first_from_differences = [Fraction(0)]
        second_from_differences = [Fraction(0)]
        falling_degree = 1
        for r in range(1, n + 1):
            falling_degree *= n - r + 1
            delta_power = poly_scale(polynomials[n - r], Fraction(falling_degree))
            first_from_differences = poly_add(
                first_from_differences,
                delta_power,
                scale=Fraction((-1) ** (r - 1), r),
            )
            if r >= 2:
                second_from_differences = poly_add(
                    second_from_differences,
                    delta_power,
                    scale=Fraction((-1) ** r, r) * harmonics[r - 1],
                )
        assert first_from_differences == poly_derivative(polynomial)
        assert second_from_differences == poly_scale(
            poly_derivative(poly_derivative(polynomial)), Fraction(1, 2)
        )

        # Exact p-step Newton translation, with p specialized to 2n+1.
        p_symbol = 2 * n + 1
        newton_translation = 0
        falling_degree = 1
        for r in range(n + 1):
            if r >= 1:
                falling_degree *= n - r + 1
            delta_value = falling_degree * charlier_value_direct(n - r, n)
            generalized_binomial = (-1) ** r * comb(p_symbol + r - 1, r)
            newton_translation += generalized_binomial * delta_value
        assert newton_translation == charlier_value_direct(n, n - p_symbol)

    return {"exact_charlier_degree_limit": limit}


def exact_frobenius_checks(limit: int) -> dict[str, int]:
    a_values, c_values = a_and_c_values(limit)
    g = [Fraction(a_values[n], factorial(n)) for n in range(limit + 1)]
    u = g[:]
    u[0] = Fraction(0)
    harmonics = harmonic_numbers(limit)

    for m in range(1, limit + 1):
        powers: dict[int, Fraction] = {}
        current = [Fraction(1)] + [Fraction(0) for _ in range(limit)]
        for r in range(1, m + 1):
            current = series_product(current, u, limit)
            powers[r] = current[m]

        ell_m = Fraction(1) + Fraction(1, m)
        logarithm_coefficient = sum(
            Fraction((-1) ** (r - 1), r) * powers[r]
            for r in range(1, m + 1)
        )
        assert logarithm_coefficient == ell_m

        ell_square_half = Fraction(1, 2) * sum(
            (Fraction(1) + Fraction(1, j))
            * (Fraction(1) + Fraction(1, m - j))
            for j in range(1, m)
        )
        second_binomial_derivative = sum(
            Fraction((-1) ** r, r) * harmonics[r - 1] * powers[r]
            for r in range(2, m + 1)
        )
        assert second_binomial_derivative == ell_square_half

        # The lower-coefficient quotient formula is exact whenever a prime
        # p=2m+1 divides A_m.  Its numerator is the logarithm identity with
        # the r=1 term isolated.
        lower_expression = ell_m - sum(
            Fraction((-1) ** (r - 1), r) * powers[r]
            for r in range(2, m + 1)
        )
        assert lower_expression == g[m]
        h_m = sum(g[m - r] * Fraction(1, r) for r in range(1, m + 1))
        assert h_m == Fraction(c_values[m], factorial(m))

    return {"exact_frobenius_degree_limit": limit}


def finite_prime_checks(prime_limit: int) -> dict[str, object]:
    primes = odd_primes_up_to(prime_limit)
    max_m = (prime_limit - 1) // 2
    a_values, c_values = a_and_c_values(max_m)
    central_roots: list[dict[str, int]] = []

    for p in primes:
        m = (p - 1) // 2
        modulus = p * p
        wilson_quotient = ((factorial(p - 1) + 1) // p) % p
        factorials = [1]
        for n in range(1, p):
            factorials.append(factorials[-1] * n % modulus)
        harmonic = 0
        q_sum = 0
        r_sum = 0
        t_sum_mod_p = 0
        for k in range(m + 1):
            if k >= 1:
                harmonic = (harmonic + pow(k, -1, p)) % p
            denominator = factorials[k] * factorials[m - k] % modulus
            q_coefficient = (
                (-1 if k % 2 else 1)
                * factorials[p - 1 - k]
                * pow(denominator, -1, modulus)
            ) % modulus
            r_denominator = factorials[k] * factorials[k] * factorials[m - k] % modulus
            r_coefficient = pow(r_denominator, -1, modulus)
            transformed = (
                -r_coefficient
                + p * (wilson_quotient - harmonic) * r_coefficient
            ) % modulus
            assert q_coefficient == transformed
            q_sum = (q_sum + q_coefficient) % modulus
            r_sum = (r_sum + r_coefficient) % modulus
            t_sum_mod_p = (
                t_sum_mod_p
                + harmonic * (r_coefficient % p)
            ) % p

        assert r_sum == (
            a_values[m] * pow(factorials[m] * factorials[m] % modulus, -1, modulus)
        ) % modulus
        if a_values[m] % p == 0:
            assert q_sum % p == 0
            assert r_sum % p == 0
            q_quotient = q_sum // p % p
            r_quotient = r_sum // p % p
            assert q_quotient == (-r_quotient - t_sum_mod_p) % p
            target = (a_values[m] // p - c_values[m]) % p
            assert q_quotient == ((-1) ** m * target) % p

            # Exact lower-degree logarithm formula for A_m/p-C_m.
            g = [Fraction(a_values[n], factorial(n)) for n in range(m + 1)]
            u = g[:]
            u[0] = Fraction(0)
            current = [Fraction(1)] + [Fraction(0) for _ in range(m)]
            convolution_sum = Fraction(0)
            for r in range(1, m + 1):
                current = series_product(current, u, m)
                if r >= 2:
                    convolution_sum += Fraction((-1) ** (r - 1), r) * current[m]
            g_m_from_lower = Fraction(1) + Fraction(1, m) - convolution_sum
            assert g_m_from_lower == g[m]
            lower_target = factorial(m) * (
                g_m_from_lower / p
                - sum(g[m - r] * Fraction(1, r) for r in range(1, m + 1))
            )
            assert lower_target.denominator == 1
            assert lower_target.numerator % p == target

            central_roots.append(
                {
                    "p": p,
                    "m": m,
                    "A_over_p_mod_p": (a_values[m] // p) % p,
                    "C_mod_p": c_values[m] % p,
                    "target_mod_p": target,
                    "q_over_p_mod_p": q_quotient,
                }
            )

    return {
        "finite_prime_limit": prime_limit,
        "odd_prime_count": len(primes),
        "central_roots": central_roots,
    }


def repeated_root_diagnostic() -> dict[str, int]:
    p = 577
    degree = 288
    parameter = 186
    value, derivative = charlier_value_and_derivative_mod(degree, parameter, p)
    central_value, central_derivative = charlier_value_and_derivative_mod(degree, degree, p)
    assert value == 0 and derivative == 0
    assert central_value == 8 and central_derivative == 211
    return {
        "p": p,
        "degree": degree,
        "repeated_root_parameter": parameter,
        "value_mod_p": value,
        "derivative_mod_p": derivative,
        "central_value_mod_p": central_value,
        "central_derivative_mod_p": central_derivative,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-degree", type=int, default=18)
    parser.add_argument("--frobenius-degree", type=int, default=40)
    parser.add_argument("--prime-limit", type=int, default=1000)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    report: dict[str, object] = {
        "scope": (
            "All-prime identities are proved in the source note; all cutoffs "
            "in this JSON are finite certificate checks only."
        ),
        "charlier": exact_charlier_checks(arguments.exact_degree),
        "frobenius": exact_frobenius_checks(arguments.frobenius_degree),
        "wilson": finite_prime_checks(arguments.prime_limit),
        "ordinary_derivative_failure": repeated_root_diagnostic(),
    }
    canonical = json.dumps(report, sort_keys=True, separators=(",", ":"))
    report["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output is not None:
        arguments.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
