"""Exact certificate for the generic large-prime degree and CRT note."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from critical_fourier_generalized_odd_prime_bands_certificate import (
    fourier_content,
    fourier_polynomial,
)
from critical_fourier_large_prime_matching_filter_certificate import (
    base_polynomial,
    exponential_pair,
)


Gaussian = tuple[int, int]


def valuation(value: int, prime: int) -> int:
    assert value != 0
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def A_coefficient(n: int, h: int) -> int:
    return (
        math.comb(n, 2 * h)
        * math.factorial(2 * n - 2 * h)
        * math.factorial(n)
        // math.factorial(n - h)
    )


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


def multiply_one_plus_y_squared(
    polynomial: list[Gaussian], prime: int
) -> list[Gaussian]:
    value: list[Gaussian] = []
    for index in range(len(polynomial) + 2):
        real = 0
        imaginary = 0
        if index < len(polynomial):
            real += polynomial[index][0]
            imaginary += polynomial[index][1]
        if 0 <= index - 1 < len(polynomial):
            real += 2 * polynomial[index - 1][0]
            imaginary += 2 * polynomial[index - 1][1]
        if 0 <= index - 2 < len(polynomial):
            real += polynomial[index - 2][0]
            imaginary += polynomial[index - 2][1]
        value.append((real % prime, imaginary % prime))
    return value


def initial_r_polynomial(n: int, prime: int) -> list[Gaussian]:
    base = [
        (real % prime, imaginary % prime)
        for real, imaginary in base_polynomial(n)
    ]
    value: list[Gaussian] = []
    for index in range(len(base) + 1):
        real = 0
        imaginary = 0
        if index < len(base):
            real += base[index][0]
            imaginary += base[index][1]
        if index > 0:
            real += base[index - 1][0]
            imaginary += base[index - 1][1]
        value.append((real % prime, imaginary % prime))
    return value


def interpolation_counterexample() -> dict[str, object]:
    n = 64
    prime = 937
    p_value, q_value = exponential_pair(n)
    assert valuation(q_value, prime) == 1
    q_quotient = (q_value // prime) % prime

    inverse = [0] * prime
    inverse[1] = 1
    for index in range(2, prime):
        inverse[index] = (
            -(prime // index) * inverse[prime % index]
        ) % prime
    factorial = [1] * prime
    for index in range(1, prime):
        factorial[index] = factorial[index - 1] * index % prime

    sine_values = (0, 1, 0, -1)
    cosine_values = (1, 0, -1, 0)
    R = initial_r_polynomial(n, prime)
    residues: list[int] = []
    records: list[dict[str, int]] = []

    for s in range(1, prime - 2 * n - 1, 2):
        K = (prime + s + 2 * n) // 2
        u = prime - K
        assert len(R) == 2 * n + s + 1
        U = 0
        for index, (real, imaginary) in enumerate(R):
            m_value = u + index
            N_value = (
                real * sine_values[m_value % 4]
                - imaginary * (1 - cosine_values[m_value % 4])
            )
            U = (U + N_value * inverse[m_value]) % prime

        ell = (prime + s) // 2
        denominator = (
            factorial[n] * factorial[ell] % prime
        ) * factorial[K] % prime
        D = (
            -factorial[s]
            * phi_mod(n, s, prime)
            * pow(denominator, -1, prime)
        ) % prime
        F = (
            4 * q_quotient * U - p_value * D
        ) % prime
        residues.append(F)
        if F == 0 or K == 797:
            records.append(
                {"s": s, "K": K, "D": D, "U": U, "F": F}
            )
        R = multiply_one_plus_y_squared(R, prime)

    assert len(residues) == 404
    differences = residues[:]
    interpolation_degree = -1
    for order in range(len(residues)):
        if any(differences):
            interpolation_degree = order
        if len(differences) > 1:
            differences = [
                (differences[index + 1] - differences[index]) % prime
                for index in range(len(differences) - 1)
            ]
    assert len(differences) == 1
    assert interpolation_degree == 403
    assert differences[0] == 513
    assert records == [{"s": 529, "K": 797, "D": 257, "U": 463, "F": 0}]
    sequence_text = ",".join(str(value) for value in residues)
    sequence_hash = hashlib.sha256(sequence_text.encode("ascii")).hexdigest()
    assert (
        sequence_hash
        == "de44c4cdb29ed59fdaf1823d9ba69aa637f9fa56325fb49b8ca474f200853d9f"
    )
    return {
        "n": n,
        "prime": prime,
        "v_q": 1,
        "q_over_prime_mod_prime": q_quotient,
        "p_n_mod_prime": p_value % prime,
        "admissible_parameter_count": len(residues),
        "interpolation_degree": interpolation_degree,
        "top_finite_difference": differences[0],
        "sequence_sha256": sequence_hash,
        "zero_records": records,
        "residues": residues,
    }


def lcm_to(K: int) -> int:
    value = 1
    for index in range(1, K + 1):
        value = math.lcm(value, index)
    return value


def crt_examples() -> list[dict[str, object]]:
    specifications = [
        (72, 189, 227),
        (92, 442, 647),
        (64, 797, 937),
    ]
    records: list[dict[str, object]] = []
    for n, K, prime in specifications:
        coefficients = fourier_polynomial(n, K)
        c0, t_value, _ = fourier_content(coefficients, K)
        lcm_value = lcm_to(K)
        p_value, q_value = exponential_pair(n)
        Z = 4 * q_value * t_value - p_value * lcm_value * c0
        assert Z != 0
        assert valuation(Z, prime) >= 2
        norm_bound = 2 ** (2 * K + n // 2)
        upper_bound = 15 * q_value * lcm_value * norm_bound
        assert abs(Z) <= upper_bound
        records.append(
            {
                "n": n,
                "K": K,
                "prime": prime,
                "v_prime_Z": valuation(Z, prime),
                "Z_sign": 1 if Z > 0 else -1,
                "Z_decimal_digits": len(str(abs(Z))),
                "Z_decimal_sha256": hashlib.sha256(
                    str(Z).encode("ascii")
                ).hexdigest(),
                "size_bound_verified": True,
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "critical_fourier_generic_large_prime_degree_and_crt_"
            "certificate.json"
        ),
    )
    arguments = parser.parse_args()
    output = {
        "description": (
            "Exact interpolation counterexample and CRT checks for "
            "generic large-prime critical-Fourier matching"
        ),
        "interpolation_counterexample": interpolation_counterexample(),
        "crt_examples": crt_examples(),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
