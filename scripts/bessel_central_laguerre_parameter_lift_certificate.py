#!/usr/bin/env python3
"""Exact certificate for the central Bessel--Laguerre parameter lift.

The all-prime proofs are in
``sources/bessel_central_laguerre_parameter_lift.md``.  This program:

* checks the exact finite polynomial, Laguerre-connection, derivative, and
  Padé-Wronskian identities over the integers/rationals;
* scans the single central class for every odd prime through a requested
  cutoff with an exact accumulating remainder tree; and
* checks every central root found modulo p^2 by independent scalar
  recurrences.

The scan is finite evidence only.  No finite cutoff is used as an all-prime
nonvanishing theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


Matrix = tuple[int, int, int, int]


def matrix_product(left: Matrix, right: Matrix) -> Matrix:
    """Return left*right for row-major 2 by 2 matrices."""
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def matrix_vector_mod(matrix: Matrix, vector: tuple[int, int], modulus: int) -> tuple[int, int]:
    a, b, c, d = matrix
    x, y = vector
    return ((a * x + b * y) % modulus, (c * x + d * y) % modulus)


def polynomial_add(left: list[int], right: list[int], scale: int = 1) -> list[int]:
    size = max(len(left), len(right))
    answer = [0] * size
    for index in range(size):
        answer[index] = (
            (left[index] if index < len(left) else 0)
            + scale * (right[index] if index < len(right) else 0)
        )
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def polynomial_product(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def polynomial_derivative(poly: list[int]) -> list[int]:
    if len(poly) == 1:
        return [0]
    return [index * poly[index] for index in range(1, len(poly))]


def q_polynomial(n: int) -> list[int]:
    return [
        (-1) ** k * factorial(2 * n - k) // (factorial(k) * factorial(n - k))
        for k in range(n + 1)
    ]


def a_values(limit: int) -> list[int]:
    values = [1]
    if limit == 0:
        return values
    values.append(2)
    for n in range(2, limit + 1):
        values.append(2 * n * values[-1] - (n - 1) ** 2 * values[-2])
    return values


def c_from_a(m: int, values: list[int]) -> int:
    falling = 1
    answer = 0
    for r in range(1, m + 1):
        falling *= m - r + 1
        assert falling % r == 0
        answer += (falling // r) * values[m - r]
    return answer


def exact_identity_checks(limit: int) -> dict[str, int]:
    values = a_values(limit)
    q_nm2 = 1
    q_nm1 = 1

    for m in range(limit + 1):
        poly = q_polynomial(m)
        q_value = sum(poly)
        if m == 0:
            recurrence_value = 1
        elif m == 1:
            recurrence_value = 1
        else:
            recurrence_value = (4 * m - 2) * q_nm1 + q_nm2
            q_nm2, q_nm1 = q_nm1, recurrence_value
        if m == 1:
            q_nm2, q_nm1 = 1, 1
        assert q_value == recurrence_value

        partial_permutations = sum(factorial(j) * comb(m, j) ** 2 for j in range(m + 1))
        assert values[m] == partial_permutations

        c_integer = c_from_a(m, values)
        harmonic = [Fraction(0)]
        for j in range(1, m + 1):
            harmonic.append(harmonic[-1] + Fraction(1, j))
        c_harmonic = sum(
            Fraction(factorial(j) * comb(m, j) ** 2)
            * (harmonic[m] - harmonic[m - j])
            for j in range(m + 1)
        )
        assert c_harmonic.denominator == 1
        assert c_harmonic.numerator == c_integer

        # Exact Laguerre connection formula at alpha=-(2m+1), multiplied
        # through by (-1)^m m!.
        p_symbol = 2 * m + 1
        connection = values[m]
        falling = 1
        for r in range(1, m + 1):
            falling *= m - r + 1
            connection += (-1) ** r * comb(p_symbol, r) * falling * values[m - r]
        assert q_value == (-1) ** m * connection

    # Polynomial recurrence and exact Wronskian.  This smaller cap keeps the
    # purely symbolic coefficient arithmetic quick while covering many degrees.
    polynomial_limit = min(limit, 24)
    q_polys = [q_polynomial(n) for n in range(polynomial_limit + 1)]
    for m, q_poly in enumerate(q_polys):
        if m >= 2:
            predicted = polynomial_add(
                [2 * (2 * m - 1) * coefficient for coefficient in q_polys[m - 1]],
                [0, 0] + q_polys[m - 2],
            )
            assert q_poly == predicted

        p_poly = [(-1) ** index * coefficient for index, coefficient in enumerate(q_poly)]
        wronskian = polynomial_add(
            polynomial_product(polynomial_derivative(p_poly), q_poly),
            polynomial_product(p_poly, polynomial_derivative(q_poly)),
            scale=-1,
        )
        wronskian = polynomial_add(wronskian, polynomial_product(p_poly, q_poly), scale=-1)
        expected = [0] * (2 * m) + [(-1) ** (m + 1)]
        assert wronskian == expected

    return {
        "integer_degree_limit": limit,
        "polynomial_degree_limit": polynomial_limit,
    }


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


def central_residues(primes: list[int]) -> list[int]:
    """Compute A_((p-1)/2) modulo p for every p by a remainder tree.

    The recurrence state is

        [A_n, A_(n-1)]^T = T_n [A_(n-1), A_(n-2)]^T,
        T_n = [[2n, -(n-1)^2], [1, 0]].

    Segment matrices end at consecutive prime-derived indices.  At product
    level l>=1, a node product is retained only modulo the product of all
    later node moduli.  This is sufficient because that product is used only
    to advance prefixes into a right sibling.  Level-zero segment products
    remain exact because they are also applied at their own leaves.
    """
    if not primes:
        return []
    indices = [(prime - 1) // 2 for prime in primes]
    segments: list[Matrix] = []
    previous = 1
    for index in indices:
        segment: Matrix = (1, 0, 0, 1)
        for n in range(previous + 1, index + 1):
            transition: Matrix = (2 * n, -(n - 1) ** 2, 1, 0)
            segment = matrix_product(transition, segment)
        segments.append(segment)
        previous = index

    product_levels: list[list[Matrix]] = [segments]
    modulus_levels: list[list[int]] = [primes]
    while len(product_levels[-1]) > 1:
        old_products = product_levels[-1]
        old_moduli = modulus_levels[-1]
        new_products: list[Matrix] = []
        new_moduli: list[int] = []
        for offset in range(0, len(old_products), 2):
            if offset + 1 < len(old_products):
                new_products.append(
                    matrix_product(old_products[offset + 1], old_products[offset])
                )
                new_moduli.append(old_moduli[offset] * old_moduli[offset + 1])
            else:
                new_products.append(old_products[offset])
                new_moduli.append(old_moduli[offset])

        # Establish the suffix-modulus invariant described in the docstring.
        suffix = 1
        for offset in range(len(new_products) - 1, -1, -1):
            if suffix == 1:
                new_products[offset] = (0, 0, 0, 0)
            elif max(abs(entry).bit_length() for entry in new_products[offset]) > suffix.bit_length():
                new_products[offset] = tuple(entry % suffix for entry in new_products[offset])  # type: ignore[assignment]
            suffix *= new_moduli[offset]

        product_levels.append(new_products)
        modulus_levels.append(new_moduli)

    residues = [0] * len(primes)

    def descend(level: int, node: int, prefix: tuple[int, int]) -> None:
        if level == 0:
            residues[node] = matrix_vector_mod(
                product_levels[0][node], prefix, primes[node]
            )[0]
            return

        left = 2 * node
        right = left + 1
        left_modulus = modulus_levels[level - 1][left]
        descend(level - 1, left, (prefix[0] % left_modulus, prefix[1] % left_modulus))

        if right < len(product_levels[level - 1]):
            right_modulus = modulus_levels[level - 1][right]
            left_product = tuple(
                entry % right_modulus for entry in product_levels[level - 1][left]
            )
            right_prefix = matrix_vector_mod(
                left_product,  # type: ignore[arg-type]
                (prefix[0] % right_modulus, prefix[1] % right_modulus),
                right_modulus,
            )
            descend(level - 1, right, right_prefix)

    descend(len(product_levels) - 1, 0, (2, 1))
    return residues


def direct_root_record(prime: int) -> dict[str, int]:
    m = (prime - 1) // 2
    modulus = prime * prime

    a_mod = [1]
    if m >= 1:
        a_mod.append(2)
    for n in range(2, m + 1):
        a_mod.append((2 * n * a_mod[-1] - (n - 1) ** 2 * a_mod[-2]) % modulus)
    a_value = a_mod[m] % modulus
    assert a_value % prime == 0

    falling = 1
    c_value = 0
    for r in range(1, m + 1):
        falling = falling * (m - r + 1) % prime
        c_value = (c_value + falling * pow(r, -1, prime) * (a_mod[m - r] % prime)) % prime

    q_nm2 = q_nm1 = 1
    derivative_nm2 = 0
    derivative_nm1 = -1 % prime
    p_nm2 = 1
    p_nm1 = 3 % prime
    if m == 0:
        q_value = 1
        derivative = 0
        p_value = 1
    elif m == 1:
        q_value = 1
        derivative = derivative_nm1
        p_value = p_nm1
    else:
        for n in range(2, m + 1):
            q_value = ((4 * n - 2) * q_nm1 + q_nm2) % modulus
            derivative = (
                (4 * n - 2) * derivative_nm1 + 2 * (q_nm2 % prime) + derivative_nm2
            ) % prime
            p_value = ((4 * n - 2) * p_nm1 + p_nm2) % prime
            q_nm2, q_nm1 = q_nm1, q_value
            derivative_nm2, derivative_nm1 = derivative_nm1, derivative
            p_nm2, p_nm1 = p_nm1, p_value

    q_value %= modulus
    predicted_q = ((-1) ** m * (a_value - prime * c_value)) % modulus
    assert q_value == predicted_q
    assert q_value % prime == 0
    q_quotient = (q_value // prime) % prime
    sign = (-1) ** (m + 1) % prime
    assert (-p_value * derivative) % prime == sign
    hensel_shift = (-q_quotient * pow(derivative, -1, prime)) % prime

    return {
        "p": prime,
        "m": m,
        "A_m_mod_p_squared": a_value,
        "A_m_over_p_mod_p": (a_value // prime) % prime,
        "C_m_mod_p": c_value,
        "q_m_mod_p_squared": q_value,
        "q_m_over_p_mod_p": q_quotient,
        "Q_m_prime_at_1_mod_p": derivative,
        "P_m_at_1_mod_p": p_value,
        "hensel_shift_t_for_x_equals_1_plus_p_t": hensel_shift,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=2_000_001)
    parser.add_argument("--identity-limit", type=int, default=80)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/bessel_central_laguerre_parameter_lift_certificate.json"),
    )
    arguments = parser.parse_args()
    if arguments.prime_limit < 3:
        raise SystemExit("prime limit must be at least 3")
    if arguments.identity_limit < 1:
        raise SystemExit("identity limit must be positive")

    identity_checks = exact_identity_checks(arguments.identity_limit)
    primes = odd_primes_up_to(arguments.prime_limit)
    residues = central_residues(primes)

    digest = hashlib.sha256()
    for prime, residue in zip(primes, residues):
        digest.update(f"{prime}:{residue}\n".encode("ascii"))

    root_primes = [prime for prime, residue in zip(primes, residues) if residue == 0]
    root_records = [direct_root_record(prime) for prime in root_primes]
    all_branching = [record for record in root_records if record["q_m_mod_p_squared"] == 0]

    result = {
        "description": (
            "Exact Laguerre/parameter-derivative identity checks and an exact finite "
            "central-class remainder-tree scan; the scan is not an all-prime proof."
        ),
        "identity_checks": identity_checks,
        "prime_limit": arguments.prime_limit,
        "odd_primes_scanned": len(primes),
        "central_residue_stream_sha256": digest.hexdigest(),
        "central_root_primes": root_primes,
        "central_root_records": root_records,
        "all_branching_central_roots": all_branching,
        "logical_status": (
            "The identities are exact.  The bounded scan is finite evidence only; "
            "it does not exclude a later prime with p^2 dividing q_((p-1)/2)."
        ),
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

