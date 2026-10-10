#!/usr/bin/env python3
"""Exact replay for the first three ordinary Bessel harmonic layers."""

from __future__ import annotations

import hashlib
import json
import math
import resource
import time
from pathlib import Path


DEPENDENCIES = {
    "sources/bessel_large_prime_ordinary_harmonic_expansion_barrier.md": (
        "28a91596edafac946448ea68f4c95dfdcd94e63bcf7586394c464a69d6a76e3d"
    ),
    "sources/bessel_large_prime_four_point_exclusivity.md": (
        "1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41"
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def check_dependencies(repo: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(repo / relative)
        assert actual == expected, (relative, expected, actual)
        observed[relative] = actual
    return observed


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    if limit:
        sieve[0] = 0
    if limit > 1:
        sieve[1] = 0
    for candidate in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            count = (limit - 1 - start) // candidate + 1
            sieve[start:limit:candidate] = b"\x00" * count
    return [index for index, flag in enumerate(sieve) if flag]


def trim(poly: list[int], prime: int) -> list[int]:
    poly = [coefficient % prime for coefficient in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * max(len(left), len(right))
    for index, coefficient in enumerate(left):
        result[index] += coefficient
    for index, coefficient in enumerate(right):
        result[index] += coefficient
    return trim(result, prime)


def poly_multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_coefficient in enumerate(left):
        for j, right_coefficient in enumerate(right):
            result[i + j] += left_coefficient * right_coefficient
    return trim(result, prime)


def poly_scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([scalar * coefficient for coefficient in poly], prime)


def poly_shift(poly: list[int], degree: int) -> list[int]:
    return [0] * degree + poly


def elementary_from_arguments(
    arguments: list[int], maximum_degree: int, prime: int
) -> list[int]:
    elementary = [1] + [0] * maximum_degree
    for argument in arguments:
        reciprocal = pow(argument % prime, -1, prime)
        for degree in range(maximum_degree, 0, -1):
            elementary[degree] += elementary[degree - 1] * reciprocal
            elementary[degree] %= prime
    return elementary


def direct_layers(prime: int, root: int) -> dict[int, list[int]]:
    last = 2 * prime - root - 1
    layers = {1: [0], 2: [0], 3: [0]}
    for k in range(last + 1):
        interval = list(range(root - k + 1, root + k + 1)) if k else []
        multiples = [m for m in (-1, 0, 1) if m * prime in interval]
        epsilon = k // prime
        nu = len(multiples) - epsilon
        arguments = [value for value in interval if value % prime]
        denominator = math.factorial(k) // prime**epsilon
        unit = math.prod(arguments) % prime
        unit *= pow(denominator % prime, -1, prime)
        unit %= prime
        phi = [1]
        for multiple in multiples:
            phi = poly_multiply(phi, [multiple, 1], prime)
        elementary = elementary_from_arguments(arguments, 3, prime)
        sign_unit = unit if (root + k) % 2 == 0 else -unit
        for layer in (1, 2, 3):
            if nu > layer:
                continue
            ell = layer - nu
            summand = poly_scale(
                poly_shift(phi, ell), sign_unit * elementary[ell], prime
            )
            layers[layer] = poly_add(layers[layer], summand, prime)
    return layers


def factorial_tables(prime: int, modulus: int) -> tuple[list[int], list[int]]:
    factorial = [1] * prime
    for value in range(1, prime):
        factorial[value] = factorial[value - 1] * value % modulus
    inverse_factorial = [1] * prime
    inverse_factorial[-1] = pow(factorial[-1], -1, modulus)
    for value in range(prime - 1, 0, -1):
        inverse_factorial[value - 1] = (
            inverse_factorial[value] * value % modulus
        )
    return factorial, inverse_factorial


def harmonic_tables(prime: int) -> dict[int, list[int]]:
    tables = {degree: [0] * prime for degree in (1, 2, 3)}
    for value in range(1, prime):
        inverse = pow(value, -1, prime)
        power = 1
        for degree in (1, 2, 3):
            power = power * inverse % prime
            tables[degree][value] = (
                tables[degree][value - 1] + power
            ) % prime
    return tables


def elementary_from_powers(powers: dict[int, int], degree: int, prime: int) -> int:
    if degree == 0:
        return 1
    if degree == 1:
        return powers[1]
    if degree == 2:
        return (
            (powers[1] * powers[1] - powers[2]) * pow(2, -1, prime)
        ) % prime
    assert degree == 3
    return (
        (
            powers[1] ** 3
            - 3 * powers[1] * powers[2]
            + 2 * powers[3]
        )
        * pow(6, -1, prime)
    ) % prime


def reduced_blocks(
    prime: int,
    root: int,
    factorial: list[int],
    inverse_factorial: list[int],
    harmonics: dict[int, list[int]],
) -> tuple[list[int], list[int], list[int]]:
    blocks_a = [0] * 4
    blocks_b = [0] * 3
    blocks_g = [0] * 2

    for h in range(root + 1):
        weight = factorial[root + h]
        weight *= inverse_factorial[h] * inverse_factorial[root - h]
        weight %= prime
        if (root + h) % 2:
            weight = -weight
        powers = {
            degree: (
                harmonics[degree][root + h]
                - harmonics[degree][root - h]
            )
            % prime
            for degree in (1, 2, 3)
        }
        for degree in range(4):
            blocks_a[degree] += weight * elementary_from_powers(
                powers, degree, prime
            )
            blocks_a[degree] %= prime

    for h in range(prime - 2 * root - 1):
        weight = -factorial[h] * factorial[2 * root + 1 + h]
        weight *= inverse_factorial[root + 1 + h]
        weight %= prime
        powers = {
            degree: (
                (-1) ** degree * harmonics[degree][h]
                + harmonics[degree][2 * root + 1 + h]
            )
            % prime
            for degree in (1, 2, 3)
        }
        for degree in range(3):
            blocks_b[degree] += weight * elementary_from_powers(
                powers, degree, prime
            )
            blocks_b[degree] %= prime

    for h in range(root):
        weight = factorial[h] * factorial[root - h - 1]
        weight *= inverse_factorial[2 * root - h]
        weight %= prime
        if (root + 1) % 2:
            weight = -weight
        powers = {
            degree: (
                harmonics[degree][h]
                - harmonics[degree][2 * root - h]
            )
            % prime
            for degree in (1, 2, 3)
        }
        for degree in range(2):
            blocks_g[degree] += weight * elementary_from_powers(
                powers, degree, prime
            )
            blocks_g[degree] %= prime

    return blocks_a, blocks_b, blocks_g


def predicted_layers(
    prime: int, blocks_a: list[int], blocks_b: list[int], blocks_g: list[int]
) -> dict[int, list[int]]:
    z = [0, 1]
    z_plus_one = [1, 1]
    z2 = poly_multiply(z, z, prime)
    z3 = poly_multiply(z2, z, prime)
    z2_minus_one = [-1, 0, 1]

    first = poly_add(
        poly_scale(z, blocks_a[1] + blocks_b[0], prime),
        poly_scale(
            poly_multiply(z, z_plus_one, prime), blocks_a[0], prime
        ),
        prime,
    )
    second = [0]
    for polynomial, scalar in (
        (z2, blocks_a[2] + blocks_b[1]),
        (poly_multiply(z, z_plus_one, prime), blocks_g[0]),
        (poly_multiply(z2, z_plus_one, prime), blocks_a[1]),
        (poly_multiply(z, z2_minus_one, prime), blocks_b[0]),
    ):
        second = poly_add(second, poly_scale(polynomial, scalar, prime), prime)
    third = [0]
    for polynomial, scalar in (
        (z3, blocks_a[3] + blocks_b[2]),
        (poly_multiply(z2, z_plus_one, prime), blocks_g[1]),
        (poly_multiply(z3, z_plus_one, prime), blocks_a[2]),
        (poly_multiply(z2, z2_minus_one, prime), blocks_b[1]),
    ):
        third = poly_add(third, poly_scale(polynomial, scalar, prime), prime)
    return {1: first, 2: second, 3: third}


def finite_field_grid(prime_bound: int) -> dict:
    orbit_count = 0
    direct_polynomial_checks = 0
    endpoint_checks = 0
    zero_endpoint_checks = 0
    left_factorial_checks = 0
    root_slope_checks = 0
    root_records: list[dict[str, int]] = []
    for prime in primes_below(prime_bound):
        if prime < 5:
            continue
        factorial, inverse_factorial = factorial_tables(prime, prime)
        harmonics = harmonic_tables(prime)
        q_values = [1, 1]
        for n in range(2, prime):
            q_values.append(
                ((4 * n - 2) * q_values[-1] + q_values[-2]) % prime
            )
        for root in range((prime - 1) // 2 + 1):
            orbit_count += 1
            direct = direct_layers(prime, root)
            blocks_a, blocks_b, blocks_g = reduced_blocks(
                prime, root, factorial, inverse_factorial, harmonics
            )
            predicted = predicted_layers(prime, blocks_a, blocks_b, blocks_g)
            for layer in (1, 2, 3):
                assert trim(direct[layer], prime) == trim(
                    predicted[layer], prime
                )
                direct_polynomial_checks += 1
                assert direct[layer][0] % prime == 0
                zero_endpoint_checks += 1
                for endpoint in (0, -1, 1, -2):
                    direct_value = sum(
                        coefficient * pow(endpoint, degree)
                        for degree, coefficient in enumerate(direct[layer])
                    ) % prime
                    predicted_value = sum(
                        coefficient * pow(endpoint, degree)
                        for degree, coefficient in enumerate(predicted[layer])
                    ) % prime
                    assert direct_value == predicted_value
                    endpoint_checks += 1
            assert blocks_a[0] == q_values[root]
            if q_values[root] == 0:
                slope = (blocks_a[1] + blocks_b[0]) % prime
                assert predicted[1] == trim([0, slope], prime)
                root_slope_checks += 1
                root_records.append(
                    {"prime": prime, "root": root, "delta_mod_p": slope}
                )

        _, blocks_b_zero, _ = reduced_blocks(
            prime, 0, factorial, inverse_factorial, harmonics
        )
        left_factorial = sum(factorial) % prime
        assert (1 + blocks_b_zero[0]) % prime == -left_factorial % prime
        left_factorial_checks += 1

    return {
        "prime_bound_exclusive": prime_bound,
        "base_orbit_count": orbit_count,
        "direct_layer_polynomial_checks": direct_polynomial_checks,
        "endpoint_evaluation_checks": endpoint_checks,
        "exact_zero_endpoint_checks": zero_endpoint_checks,
        "root_slope_checks": root_slope_checks,
        "left_factorial_specialization_checks": left_factorial_checks,
        "root_records": root_records,
    }


def wilson_lift_grid(prime_bound: int) -> dict:
    term_checks = 0
    root_sum_checks = 0
    for prime in primes_below(prime_bound):
        if prime < 5:
            continue
        modulus = prime * prime
        factorial, inverse_factorial = factorial_tables(prime, modulus)
        harmonics = harmonic_tables(prime)[1]
        wilson = ((factorial[-1] + 1) % modulus) // prime % prime
        q_values = [1, 1]
        for n in range(2, (prime - 1) // 2 + 1):
            q_values.append(
                ((4 * n - 2) * q_values[-1] + q_values[-2]) % modulus
            )
        for root in range((prime - 1) // 2 + 1):
            prefix = [1] * (2 * root + 1)
            for index in range(1, 2 * root + 1):
                prefix[index] = prefix[index - 1] * (prime + index) % modulus
            inverse_prefix = [1] * (2 * root + 1)
            inverse_prefix[-1] = pow(prefix[-1], -1, modulus)
            for index in range(2 * root, 0, -1):
                inverse_prefix[index - 1] = (
                    inverse_prefix[index] * (prime + index) % modulus
                )

            high_sum = 0
            base_sum = 0
            reduced_correction = 0
            for h in range(root + 1):
                high = -factorial[prime - root + h - 1]
                high *= prefix[h + root] * inverse_prefix[h]
                high %= modulus
                base = factorial[root + h]
                base *= inverse_factorial[h] * inverse_factorial[root - h]
                base %= modulus
                if (root + h) % 2:
                    base = -base
                correction = (
                    harmonics[root + h]
                    - harmonics[h]
                    + harmonics[root - h]
                    - wilson
                ) % prime
                predicted = base * (1 + prime * correction) % modulus
                assert high == predicted
                term_checks += 1
                high_sum = (high_sum + high) % modulus
                base_sum = (base_sum + base) % modulus
                reduced_correction += (
                    (base % prime)
                    * (
                        harmonics[root + h]
                        - harmonics[h]
                        + harmonics[root - h]
                    )
                )
                reduced_correction %= prime

            if q_values[root] % prime == 0:
                assert base_sum == q_values[root]
                quotient = (high_sum - base_sum) % modulus
                assert quotient % prime == 0
                assert quotient // prime == reduced_correction
                root_sum_checks += 1
    return {
        "prime_bound_exclusive": prime_bound,
        "termwise_wilson_lift_checks": term_checks,
        "root_wilson_cancellation_checks": root_sum_checks,
    }


def witness(prime: int, root: int, endpoint: int, index: int, f_sign: int) -> dict:
    modulus = prime * prime
    factorial, inverse_factorial = factorial_tables(prime, prime)
    factorial2, inverse_factorial2 = factorial_tables(prime, modulus)
    harmonics = harmonic_tables(prime)
    harmonic2 = [0] * prime
    for value in range(1, prime):
        harmonic2[value] = (
            harmonic2[value - 1] + pow(value, -1, modulus)
        ) % modulus

    blocks_a, blocks_b, blocks_g = reduced_blocks(
        prime, root, factorial, inverse_factorial, harmonics
    )
    a1_exact = 0
    b0_exact = 0
    correction = 0
    for h in range(root + 1):
        weight = factorial2[root + h]
        weight *= inverse_factorial2[h] * inverse_factorial2[root - h]
        weight %= modulus
        if (root + h) % 2:
            weight = -weight
        e1 = (harmonic2[root + h] - harmonic2[root - h]) % modulus
        a1_exact = (a1_exact + weight * e1) % modulus
        correction += (
            (weight % prime)
            * (
                harmonics[1][root + h]
                - harmonics[1][h]
                + harmonics[1][root - h]
            )
        )
        correction %= prime
    for h in range(prime - 2 * root - 1):
        weight = -factorial2[h] * factorial2[2 * root + 1 + h]
        weight *= inverse_factorial2[root + 1 + h]
        b0_exact = (b0_exact + weight) % modulus
    low_exact = (a1_exact + b0_exact) % modulus

    q_modulus = prime**3
    previous, current = 1, 1
    q_root = 1 if root <= 1 else None
    q_index = 1 if index <= 1 else None
    for n in range(2, index + 1):
        previous, current = current, (
            (4 * n - 2) * current + previous
        ) % q_modulus
        if n == root:
            q_root = current
        if n == index:
            q_index = current
    assert q_root is not None and q_index is not None
    assert q_root % prime == 0

    base_numerator = (
        q_root // prime
        + endpoint * low_exact
        + endpoint * (endpoint + 1) * q_root
    ) % modulus
    assert base_numerator % prime == 0
    kappa = (
        base_numerator // prime
        + endpoint * (endpoint + 1) * correction
    ) % prime
    second_layer = (
        endpoint**2 * (blocks_a[2] + blocks_b[1])
        + endpoint * (endpoint + 1) * blocks_g[0]
        + endpoint**2 * (endpoint + 1) * blocks_a[1]
        + endpoint * (endpoint**2 - 1) * blocks_b[0]
    ) % prime
    third_layer = (
        endpoint**3 * (blocks_a[3] + blocks_b[2])
        + endpoint**2 * (endpoint + 1) * blocks_g[1]
        + endpoint**3 * (endpoint + 1) * blocks_a[2]
        + endpoint**2 * (endpoint**2 - 1) * blocks_b[1]
    ) % prime
    carried_digit = (kappa + second_layer) % prime
    assert q_index % (prime * prime) == 0
    assert q_index % (prime**3) != 0
    direct_digit = f_sign * (q_index // (prime * prime)) % prime
    assert carried_digit == direct_digit

    return {
        "prime": prime,
        "root": root,
        "endpoint": endpoint,
        "index": index,
        "blocks_A": blocks_a,
        "blocks_B": blocks_b,
        "blocks_G": blocks_g,
        "R": correction,
        "unreduced_low_P_mod_p2": low_exact,
        "kappa_2": kappa,
        "second_layer": second_layer,
        "third_layer": third_layer,
        "carried_F_over_p2_mod_p": carried_digit,
        "q_over_p2_mod_p": q_index // (prime * prime) % prime,
        "valuation": 2,
    }


def main() -> None:
    started = time.perf_counter()
    repo = Path(__file__).resolve().parents[1]
    result = {
        "description": (
            "Deterministic exact replay for the first three ordinary "
            "Bessel harmonic layers and their Wilson carry."
        ),
        "frozen_dependencies": check_dependencies(repo),
        "finite_field_grid": finite_field_grid(32),
        "wilson_lift_grid": wilson_lift_grid(50),
        "square_witnesses": [
            witness(13, 4, -1, 8, 1),
            witness(52453, 14378, 1, 66831, -1),
        ],
        "scope_warning": (
            "The layer and Wilson-carry formulas are symbolic all-prime "
            "theorems. Finite grids and the two square witnesses do not "
            "imply a uniform valuation bound. Every positive raw layer "
            "vanishes at endpoint Z=0, and raw layers do not include carries."
        ),
    }
    output = (
        repo
        / "results/bessel_ordinary_first_three_layer_wilson_carry_certificate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    elapsed = time.perf_counter() - started
    rss_mib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    print(f"live_metrics: elapsed_seconds={elapsed:.3f}, peak_rss_mib={rss_mib:.2f}")


if __name__ == "__main__":
    main()
