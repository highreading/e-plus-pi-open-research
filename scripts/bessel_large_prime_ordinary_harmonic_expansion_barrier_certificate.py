#!/usr/bin/env python3
"""Exact replay for the ordinary large-prime Bessel harmonic expansion."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import resource
import time
from fractions import Fraction
from pathlib import Path


DEPENDENCIES = {
    "sources/bessel_large_prime_four_point_exclusivity.md": (
        "1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41"
    ),
    "sources/bessel_all_even_antiperiod_higher_threshold_exclusivity.md": (
        "c0c834ca8851ddc8dba9edbc9ec74461c0d3aa1b553f79c2320b3d083a0c37de"
    ),
    "sources/bessel_large_prime_unit_cancellation_frontier.md": (
        "baa384012e6f56f3437de42eb7614e0475763a883529fbfda97120497c97b11d"
    ),
}

FOUR_PARAMETERS = (0, -1, 1, -2)


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
    if limit <= 2:
        return []
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            count = (limit - 1 - start) // candidate + 1
            sieve[start:limit:candidate] = b"\x00" * count
    return [index for index, flag in enumerate(sieve) if flag]


def q_exact(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values[: limit + 1]


def valuation(value: int, prime: int) -> int:
    assert value != 0
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return trim([scalar * value for value in poly])


def poly_multiply(
    left: list[Fraction], right: list[Fraction]
) -> list[Fraction]:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return trim(result)


def poly_shift(poly: list[Fraction], degree: int) -> list[Fraction]:
    return [Fraction(0)] * degree + poly


def poly_evaluate(poly: list[Fraction], value: int) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def fraction_mod(value: Fraction, prime: int) -> int:
    assert value.denominator % prime != 0
    return value.numerator * pow(value.denominator, -1, prime) % prime


def elementary_reciprocals(arguments: list[int]) -> list[Fraction]:
    coefficients = [Fraction(1)]
    for argument in arguments:
        coefficients.append(Fraction(0))
        reciprocal = Fraction(1, argument)
        for degree in range(len(coefficients) - 1, 0, -1):
            coefficients[degree] += coefficients[degree - 1] * reciprocal
    return coefficients


def expected_multiple_set(prime: int, root: int, k: int) -> list[int]:
    if k <= root:
        return []
    if k < prime - root:
        return [0]
    if k <= prime + root:
        return [0, 1]
    return [-1, 0, 1]


def harmonic_layers(
    prime: int, root: int
) -> tuple[dict[int, list[Fraction]], dict[str, int]]:
    last = 2 * prime - root - 1
    layers: dict[int, list[Fraction]] = {}
    termwise_polynomial_checks = 0
    denominator_checks = 0
    range_checks = 0

    for k in range(last + 1):
        interval = list(range(root - k + 1, root + k + 1)) if k else []
        multiples = [m for m in (-1, 0, 1) if m * prime in interval]
        assert multiples == expected_multiple_set(prime, root, k)
        epsilon = k // prime
        nu = len(multiples) - epsilon
        assert epsilon in (0, 1) and nu >= 0
        range_checks += 1

        arguments = [value for value in interval if value % prime != 0]
        denominator_without_prime = math.factorial(k) // prime**epsilon
        numerator_unit = math.prod(arguments)
        unit = Fraction(numerator_unit, denominator_without_prime)
        assert unit.numerator % prime != 0
        assert unit.denominator % prime != 0

        phi = [Fraction(1)]
        for multiple in multiples:
            phi = poly_multiply(phi, [Fraction(multiple), Fraction(1)])
        harmonics = elementary_reciprocals(arguments)
        for coefficient in harmonics:
            assert coefficient.denominator % prime != 0
            denominator_checks += 1

        harmonic_poly = [
            Fraction(prime**degree) * coefficient
            for degree, coefficient in enumerate(harmonics)
        ]
        factored = poly_scale(
            poly_multiply(phi, harmonic_poly),
            Fraction(prime**nu) * unit,
        )

        direct = [Fraction(1)]
        for argument in interval:
            direct = poly_multiply(
                direct, [Fraction(argument), Fraction(prime)]
            )
        direct = poly_scale(direct, Fraction(1, math.factorial(k)))
        assert direct == factored
        termwise_polynomial_checks += 1

        sign_unit = Fraction((-1) ** (root + k)) * unit
        for ell, harmonic in enumerate(harmonics):
            layer_index = nu + ell
            summand = poly_scale(
                poly_shift(phi, ell), sign_unit * harmonic
            )
            layers[layer_index] = poly_add(
                layers.get(layer_index, [Fraction(0)]), summand
            )

    for index, polynomial in layers.items():
        assert len(polynomial) - 1 <= index + 1
        for coefficient in polynomial:
            assert coefficient.denominator % prime != 0
            denominator_checks += 1

    return layers, {
        "range_checks": range_checks,
        "termwise_polynomial_checks": termwise_polynomial_checks,
        "p_integral_denominator_checks": denominator_checks,
        "maximum_layer_index": max(layers),
    }


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def expansion_checks(prime_bound: int) -> dict:
    primes = [prime for prime in primes_below(prime_bound) if prime >= 5]
    maximum = 2 * max(primes) - 1
    values = q_exact(maximum)
    root_records: list[dict] = []
    aggregate = {
        "base_orbit_expansions": 0,
        "range_checks": 0,
        "termwise_polynomial_checks": 0,
        "p_integral_denominator_checks": 0,
        "four_value_reconstructions": 0,
        "first_layer_polynomial_checks": 0,
    }

    for prime in primes:
        for root in range((prime - 1) // 2 + 1):
            layers, counts = harmonic_layers(prime, root)
            aggregate["base_orbit_expansions"] += 1
            for key in (
                "range_checks",
                "termwise_polynomial_checks",
                "p_integral_denominator_checks",
            ):
                aggregate[key] += counts[key]

            assert layers[0] == [Fraction(values[root])]
            reflection = prime - 1 - root
            expected = {
                0: values[root],
                -1: values[reflection],
                1: -values[root + prime],
                -2: -values[reflection + prime],
            }
            for parameter in FOUR_PARAMETERS:
                reconstructed = sum(
                    Fraction(prime**index)
                    * poly_evaluate(polynomial, parameter)
                    for index, polynomial in layers.items()
                )
                assert reconstructed.denominator == 1
                assert reconstructed.numerator == expected[parameter]
                aggregate["four_value_reconstructions"] += 1

            if values[root] % prime:
                continue
            assert (-values[root + prime] - values[root]) % prime == 0
            delta = (-values[root + prime] - values[root]) // prime % prime
            c_value = values[root] // prime % prime
            for parameter in FOUR_PARAMETERS:
                assert expected[parameter] % prime == 0
                assert expected[parameter] // prime % prime == (
                    c_value + parameter * delta
                ) % prime

            first = layers[1]
            assert len(first) <= 3
            first_mod = [fraction_mod(value, prime) for value in first]
            first_mod += [0] * (3 - len(first_mod))
            assert first_mod == [0, delta, 0]
            aggregate["first_layer_polynomial_checks"] += 1

            ordinary = delta != 0
            square_parameters = [
                parameter
                for parameter in FOUR_PARAMETERS
                if expected[parameter] % (prime * prime) == 0
            ]
            if ordinary:
                assert len(square_parameters) <= 1

            second = layers.get(2, [Fraction(0)])
            root_records.append(
                {
                    "prime": prime,
                    "root": root,
                    "reflection": reflection,
                    "ordinary": ordinary,
                    "c_mod_p": c_value,
                    "delta_mod_p": delta,
                    "square_parameters": square_parameters,
                    "layer_count": len(layers),
                    "maximum_layer_index": counts["maximum_layer_index"],
                    "first_layer_exact": [
                        fraction_record(value) for value in first
                    ],
                    "second_layer_mod_p": [
                        fraction_mod(value, prime) for value in second
                    ],
                }
            )

    assert root_records
    assert all(record["ordinary"] for record in root_records)
    return {
        "prime_bound_exclusive": prime_bound,
        "ordinary_root_count": len(root_records),
        "roots": root_records,
        **aggregate,
        "scope_note": (
            "This finite grid checks the symbolic expansion; it is not used "
            "to infer a valuation bound. All roots in the default grid are "
            "ordinary."
        ),
    }


def finite_difference(function, argument: int, order: int) -> int:
    return sum(
        (-1) ** (order - index)
        * math.comb(order, index)
        * function(argument + index)
        for index in range(order + 1)
    )


def countermodel_checks(prime_bound: int, hierarchy_k_max: int) -> dict:
    instance_count = 0
    valuation_checks = 0
    hierarchy_checks = 0
    odd_difference_checks = 0
    reflection_checks = 0
    layer_checks = 0
    height_checks = 0
    product_checks = 0
    examples: list[dict[str, int]] = []

    for prime in primes_below(prime_bound):
        if prime < 5:
            continue
        exponents = sorted({2, max(2, prime // 2)})
        for exponent in exponents:
            for exceptional in FOUR_PARAMETERS:
                def model(argument: int) -> int:
                    return prime * (
                        argument - exceptional - prime ** (exponent - 1)
                    )

                instance_count += 1
                assert model(0) + prime * exceptional == -prime**exponent
                assert model(1) - model(0) == prime
                layer_checks += 2

                four_values = [model(parameter) for parameter in FOUR_PARAMETERS]
                four_valuations = [
                    valuation(value, prime) for value in four_values
                ]
                for parameter, value_exponent in zip(
                    FOUR_PARAMETERS, four_valuations
                ):
                    assert value_exponent == (
                        exponent if parameter == exceptional else 1
                    )
                    assert model(parameter) // prime % prime == (
                        parameter - exceptional
                    ) % prime
                    valuation_checks += 2

                for k in range(1, hierarchy_k_max + 1):
                    constant = math.factorial(2 * k) // math.factorial(k)
                    for argument in FOUR_PARAMETERS:
                        left = finite_difference(model, argument, 2 * k)
                        right = constant * prime**k * model(argument)
                        assert (left - right) % prime ** (k + 1) == 0
                        hierarchy_checks += 1
                    assert finite_difference(model, 0, 1) % prime == 0
                    odd_difference_checks += 1
                    if 2 * k - 1 >= 3:
                        assert finite_difference(model, 0, 2 * k - 1) == 0
                        odd_difference_checks += 1

                companion = lambda argument: model(-1 - argument)
                for argument in range(-3, 4):
                    assert companion(argument) == model(-1 - argument)
                    reflection_checks += 1

                coefficient_height = max(prime, abs(model(0)))
                assert prime**exponent - 2 * prime <= coefficient_height
                assert coefficient_height <= prime**exponent + 2 * prime
                assert coefficient_height <= 2 * prime**exponent
                height_checks += 1
                product = math.prod(four_values)
                assert valuation(product, prime) == exponent + 3
                product_checks += 1

                if (
                    prime in (5, 11, 23)
                    and exponent == max(2, prime // 2)
                    and exceptional == -1
                ):
                    examples.append(
                        {
                            "prime": prime,
                            "A": exponent,
                            "exceptional_parameter": exceptional,
                            "coefficient_height": coefficient_height,
                            "exceptional_valuation": valuation(
                                model(exceptional), prime
                            ),
                            "four_value_product_valuation": valuation(
                                product, prime
                            ),
                        }
                    )

    return {
        "prime_bound_exclusive": prime_bound,
        "hierarchy_k_max": hierarchy_k_max,
        "model_instance_count": instance_count,
        "valuation_and_slope_checks": valuation_checks,
        "hierarchy_checks": hierarchy_checks,
        "odd_difference_checks": odd_difference_checks,
        "reflection_checks": reflection_checks,
        "permitted_layer_checks": layer_checks,
        "height_checks": height_checks,
        "four_value_product_checks": product_checks,
        "examples": examples,
        "scope_note": (
            "Finite checks illustrate the symbolic linear-polynomial proof. "
            "The countermodel is not a Bessel-recurrence solution and does "
            "not constrain the exact harmonic coefficients."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expansion-prime-bound", type=int, default=14)
    parser.add_argument("--countermodel-prime-bound", type=int, default=44)
    parser.add_argument("--hierarchy-k-max", type=int, default=7)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.json"
        ),
    )
    args = parser.parse_args()
    started = time.perf_counter()

    repo = Path(__file__).resolve().parents[1]
    dependencies = check_dependencies(repo)
    expansion = expansion_checks(args.expansion_prime_bound)
    countermodel = countermodel_checks(
        args.countermodel_prime_bound, args.hierarchy_k_max
    )
    result = {
        "description": (
            "Deterministic exact replay of the finite symmetric-harmonic "
            "large-prime Bessel expansion and the ordinary-path countermodel."
        ),
        "frozen_dependencies": dependencies,
        "harmonic_expansion_grid": expansion,
        "countermodel_grid": countermodel,
        "scope_warning": (
            "The expansion is an exact all-prime identity. The finite grid "
            "only replays it. The countermodel proves that the listed local "
            "hierarchy and height inputs alone cannot yield a sublinear "
            "ordinary exponent; it does not satisfy the Bessel recurrence."
        ),
    }

    output = args.output
    if not output.is_absolute():
        output = repo / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    elapsed = time.perf_counter() - started
    rss_mib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    print(f"live_metrics: elapsed_seconds={elapsed:.3f}, peak_rss_mib={rss_mib:.2f}")


if __name__ == "__main__":
    main()
