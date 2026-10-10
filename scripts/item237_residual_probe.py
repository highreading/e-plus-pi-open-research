#!/usr/bin/env python3
"""Exploratory modular recurrence probe for the Item 237 phase residual."""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


def residual_mod(h: int, prime: int) -> int:
    """c_h(s*) from the Item 229 coefficient, in O(h) field operations."""
    inv2 = pow(2, -1, prime)
    inv3 = pow(3, -1, prime)
    alpha = (4 * h + 3) * inv3 % prime
    beta = (-2 * h - 1) % prime
    # D=(1+y+y^2/2)(1+y), and D F'=N F for
    # F=(1+y)^beta(1+y+y^2/2)^alpha.
    d_coefficients = [1, 2, 3 * inv2 % prime, inv2]
    n_coefficients = [
        (alpha + beta) % prime,
        (2 * alpha + beta) % prime,
        (alpha + beta * inv2) % prime,
    ]
    coefficients = [1]
    for degree in range(2 * h):
        right = sum(
            n_coefficients[index] * coefficients[degree - index]
            for index in range(min(2, degree) + 1)
        )
        left_tail = sum(
            d_coefficients[index]
            * (degree - index + 1)
            * coefficients[degree - index + 1]
            for index in range(1, min(3, degree + 1) + 1)
        )
        coefficients.append(
            (right - left_tail) * pow(degree + 1, -1, prime) % prime
        )
    first = (4 * h - 9) * inv3 % prime
    middle = (2 * h + 1) % prime
    last = (10 * h + 12) * inv3 % prime
    boundary = [
        (first + middle + last) % prime,
        (2 * first + middle) % prime,
        first,
    ]
    return sum(
        boundary[index] * coefficients[2 * h - index]
        for index in range(3)
    ) % prime


def convolve_truncated(left, right, maximum, prime):
    answer = [0] * (maximum + 1)
    for left_index, left_value in enumerate(left):
        if left_index > maximum:
            break
        for right_index, right_value in enumerate(right):
            if left_index + right_index > maximum:
                break
            answer[left_index + right_index] = (
                answer[left_index + right_index] + left_value * right_value
            ) % prime
    return answer


def inverse_series(poly, maximum, prime):
    answer = [pow(poly[0] % prime, -1, prime)]
    for degree in range(1, maximum + 1):
        answer.append(
            -answer[0]
            * sum(
                poly[index] * answer[degree - index]
                for index in range(1, min(degree, len(poly) - 1) + 1)
            )
            % prime
        )
    return answer


def polynomial_power_series(base, exponent, maximum, prime):
    answer = [1] + [0] * maximum
    factor = list(base) + [0] * (maximum + 1 - len(base))
    while exponent:
        if exponent & 1:
            answer = convolve_truncated(answer, factor, maximum, prime)
        exponent >>= 1
        if exponent:
            factor = convolve_truncated(factor, factor, maximum, prime)
    return answer


def q_power_series(exponent, maximum, prime):
    """(1+y+y^2/2)^exponent through y^maximum."""
    inv2 = pow(2, -1, prime)
    answer = [1]
    for degree in range(maximum):
        previous = answer[degree]
        previous_two = answer[degree - 1] if degree else 0
        next_value = (
            (exponent - degree) * previous
            + (exponent - (degree - 1) * inv2) * previous_two
        ) * pow(degree + 1, -1, prime) % prime
        answer.append(next_value)
    return answer


def full_algebraic_coefficient_mod(index: int, prime: int) -> int:
    """[x^index] C(x), using the exact Lagrange coefficient formula."""
    if index == 0:
        return 2
    maximum = index - 1
    # C=N/D^3; C'=(N'D-3ND')/D^4.
    n_poly = [432, 2064, 4440, 5376, 4044, 1860, 486, 48]
    d_poly = [6, 14, 7, 2]
    n_derivative = [degree * n_poly[degree] for degree in range(1, len(n_poly))]
    d_derivative = [degree * d_poly[degree] for degree in range(1, len(d_poly))]
    first = [0] * (len(n_derivative) + len(d_poly) - 1)
    second = [0] * (len(n_poly) + len(d_derivative) - 1)
    for left_index, left_value in enumerate(n_derivative):
        for right_index, right_value in enumerate(d_poly):
            first[left_index + right_index] += left_value * right_value
    for left_index, left_value in enumerate(n_poly):
        for right_index, right_value in enumerate(d_derivative):
            second[left_index + right_index] += 3 * left_value * right_value
    numerator = [
        ((first[degree] if degree < len(first) else 0)
         - (second[degree] if degree < len(second) else 0)) % prime
        for degree in range(max(len(first), len(second)))
    ]
    d_inverse = inverse_series(d_poly, maximum, prime)
    d_minus_four = polynomial_power_series(d_inverse, 4, maximum, prime)
    q_factor = q_power_series(2 * index * pow(3, -1, prime) % prime, maximum, prime)
    one_plus = [1]
    for degree in range(1, maximum + 1):
        one_plus.append(
            one_plus[-1] * (-index - degree + 1) * pow(degree, -1, prime) % prime
        )
    product = convolve_truncated(numerator, d_minus_four, maximum, prime)
    product = convolve_truncated(product, q_factor, maximum, prime)
    product = convolve_truncated(product, one_plus, maximum, prime)
    return product[maximum] * pow(index, -1, prime) % prime


def null_vector(matrix: list[list[int]], prime: int) -> list[int] | None:
    if not matrix:
        return None
    rows = len(matrix)
    columns = len(matrix[0])
    work = [row[:] for row in matrix]
    pivots: list[int] = []
    pivot_row = 0
    for column in range(columns):
        selected = next(
            (row for row in range(pivot_row, rows) if work[row][column]),
            None,
        )
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [value * inverse % prime for value in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][column]:
                multiplier = work[row][column]
                work[row] = [
                    (left - multiplier * right) % prime
                    for left, right in zip(work[row], work[pivot_row])
                ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    if len(pivots) == columns:
        return None
    free = next(column for column in range(columns) if column not in pivots)
    answer = [0] * columns
    answer[free] = 1
    for row in range(len(pivots) - 1, -1, -1):
        column = pivots[row]
        answer[column] = -sum(
            work[row][index] * answer[index]
            for index in range(column + 1, columns)
        ) % prime
    return answer


def recurrence_matrix(
    values: list[int], order: int, degree: int, rows: int, prime: int
) -> list[list[int]]:
    return [
        [
            pow(index, power, prime) * values[index + shift] % prime
            for shift in range(order + 1)
            for power in range(degree + 1)
        ]
        for index in range(rows)
    ]


def verify(
    vector: list[int], values: list[int], order: int, degree: int, prime: int
) -> bool:
    return all(
        sum(
            vector[shift * (degree + 1) + power]
            * pow(index, power, prime)
            * values[index + shift]
            for shift in range(order + 1)
            for power in range(degree + 1)
        )
        % prime
        == 0
        for index in range(len(values) - order)
    )


def search(residue: int, count: int, prime: int, max_order: int, max_degree: int):
    values = [residual_mod(3 * index + residue, prime) for index in range(count)]
    for order in range(1, max_order + 1):
        for degree in range(max_degree + 1):
            columns = (order + 1) * (degree + 1)
            if columns + order + 8 > count:
                continue
            vector = null_vector(
                recurrence_matrix(values, order, degree, columns + 3, prime),
                prime,
            )
            if vector is not None and verify(vector, values, order, degree, prime):
                return order, degree, vector
    return None


def polynomial_value(coefficients: list[int], value: int, prime: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = (answer * value + coefficient) % prime
    return answer


def divide_linear(coefficients: list[int], root: int, prime: int) -> list[int]:
    quotient = [0] * (len(coefficients) - 1)
    carry = coefficients[-1]
    quotient[-1] = carry
    for index in range(len(coefficients) - 2, 0, -1):
        carry = (coefficients[index] + root * carry) % prime
        quotient[index - 1] = carry
    if (coefficients[0] + root * carry) % prime:
        raise ValueError("not a root")
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return quotient


def rational_linear_factors(coefficients: list[int], prime: int):
    remaining = coefficients[:]
    factors = []
    candidates = []
    for denominator in range(1, 25):
        for numerator in range(-120, 121):
            if math.gcd(abs(numerator), denominator) == 1:
                candidates.append((numerator, denominator))
    candidates.sort(key=lambda pair: (abs(pair[0]) + pair[1], pair[1], pair[0]))
    for numerator, denominator in candidates:
        root = numerator * pow(denominator, -1, prime) % prime
        multiplicity = 0
        while len(remaining) > 1 and polynomial_value(remaining, root, prime) == 0:
            remaining = divide_linear(remaining, root, prime)
            multiplicity += 1
        if multiplicity:
            factors.append((numerator, denominator, multiplicity))
    return factors, remaining


def rational_reconstruct(value: int, modulus: int) -> Fraction | None:
    bound = math.isqrt(modulus // 2)
    old_remainder, remainder = modulus, value % modulus
    old_coefficient, coefficient = 0, 1
    while remainder > bound:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_coefficient, coefficient = (
            coefficient,
            old_coefficient - quotient * coefficient,
        )
    if coefficient == 0 or abs(coefficient) > bound:
        return None
    if math.gcd(remainder, coefficient) != 1:
        return None
    if remainder * pow(coefficient, -1, modulus) % modulus != value % modulus:
        return None
    return Fraction(remainder, coefficient)


def universal_recurrence(count: int, prime: int, order: int, degree: int):
    values = {h: residual_mod(h, prime) for h in range(1, count + 3 * order + 1)}
    columns = (order + 1) * (degree + 1)
    matrix = [
        [
            pow(h, power, prime) * values[h + 3 * shift] % prime
            for shift in range(order + 1)
            for power in range(degree + 1)
        ]
        for h in range(1, columns + 5)
    ]
    vector = null_vector(matrix, prime)
    if vector is None:
        return None
    if not all(
        sum(
            vector[shift * (degree + 1) + power]
            * pow(h, power, prime)
            * values[h + 3 * shift]
            for shift in range(order + 1)
            for power in range(degree + 1)
        )
        % prime
        == 0
        for h in range(1, count + 1)
    ):
        return None
    blocks = [
        vector[shift * (degree + 1) : (shift + 1) * (degree + 1)]
        for shift in range(order + 1)
    ]
    factorizations = [rational_linear_factors(block, prime) for block in blocks]
    return {
        "vector": vector,
        "factors": factorizations,
        "reconstructed_remainders": [
            [rational_reconstruct(value, prime) for value in remainder]
            for _, remainder in factorizations
        ],
    }


def crt_pair(left: int, left_modulus: int, right: int, right_modulus: int):
    multiplier = (
        (right - left) % right_modulus
        * pow(left_modulus % right_modulus, -1, right_modulus)
        % right_modulus
    )
    return left + left_modulus * multiplier, left_modulus * right_modulus


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for small in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % small == 0:
            return value == small
    odd_part = value - 1
    twos = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        twos += 1
    for base in (2, 3, 5, 7, 11):
        witness = pow(base, odd_part, value)
        if witness in (1, value - 1):
            continue
        for _ in range(twos - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def reconstruction_primes(count: int) -> list[int]:
    answer = []
    candidate = 1_010_000_001
    while len(answer) < count:
        if is_prime(candidate):
            answer.append(candidate)
        candidate -= 2
    return answer


def reconstruct_universal(count: int, prime_count: int = 10):
    primes = reconstruction_primes(prime_count)
    vectors = [
        universal_recurrence(count, prime, order=3, degree=16)["vector"]
        for prime in primes
    ]
    reconstructed = []
    for coordinate in range(len(vectors[0])):
        value = vectors[0][coordinate]
        modulus = primes[0]
        for index in range(1, len(primes)):
            value, modulus = crt_pair(
                value, modulus, vectors[index][coordinate], primes[index]
            )
        reconstructed.append(rational_reconstruct(value, modulus))
    return {"primes": primes, "coefficients": reconstructed}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=180)
    parser.add_argument("--max-order", type=int, default=14)
    parser.add_argument("--max-degree", type=int, default=18)
    parser.add_argument("--prime", type=int, default=1_000_000_007)
    parser.add_argument("--crt", action="store_true")
    args = parser.parse_args()
    for residue in (1, 2):
        result = search(
            residue,
            args.count,
            args.prime,
            args.max_order,
            args.max_degree,
        )
        print({"residue": residue, "result": result})
    universal = universal_recurrence(
        args.count, args.prime, order=3, degree=16
    )
    print({"universal_step3_order3_degree16": universal})
    if args.crt:
        print({"crt_reconstruction": reconstruct_universal(args.count)})


if __name__ == "__main__":
    main()
