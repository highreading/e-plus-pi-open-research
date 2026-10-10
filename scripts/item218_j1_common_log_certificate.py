#!/usr/bin/env python3
"""Deterministic exact certificate for Item 218.

This standard-library checker verifies the j=1 tail reduction, the fixed-h
rational eliminants and resultants through h=8, and a declared finite scan.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item218_j1_common_log_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item218_j1_common_log_certificate.json"
)


def primes_upto(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value, flag in enumerate(flags) if flag]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def factorial_tables(prime: int) -> tuple[list[int], list[int], list[int]]:
    factorial = [1] * prime
    for value in range(1, prime):
        factorial[value] = factorial[value - 1] * value % prime
    inverse_factorial = [1] * prime
    inverse_factorial[-1] = pow(factorial[-1], -1, prime)
    for value in range(prime - 1, 0, -1):
        inverse_factorial[value - 1] = inverse_factorial[value] * value % prime
    inverse = [0] * prime
    for value in range(1, prime):
        inverse[value] = factorial[value - 1] * inverse_factorial[value] % prime
    return factorial, inverse_factorial, inverse


def kernel_coefficients(
    h_value: int,
    extra: int,
    prime: int,
    factorial: list[int],
    inverse_factorial: list[int],
) -> list[int]:
    """Coefficients of (1-z)^(2h)(1+z)^extra modulo p."""
    answer = []
    factorial_2h = factorial[2 * h_value]
    for degree in range(2 * h_value + extra + 1):
        value = 0
        for right_degree in range(extra + 1):
            left_degree = degree - right_degree
            if 0 <= left_degree <= 2 * h_value:
                choose = (
                    factorial_2h
                    * inverse_factorial[left_degree]
                    * inverse_factorial[2 * h_value - left_degree]
                ) % prime
                if left_degree % 2:
                    choose = -choose
                value += math.comb(extra, right_degree) * choose
        answer.append(value % prime)
    return answer


def normalized_sum_mod(
    kernel: list[int],
    a_value: int,
    q_value: int,
    odd: bool,
    prime: int,
    inverse: list[int],
) -> int:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    ratio = 1
    answer = 0
    for t_value in range(maximum_t + 1):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        answer = (answer + ratio * kernel[degree]) % prime
        if t_value == maximum_t:
            break
        numerator = a_value + t_value + 1 if odd else a_value + t_value
        denominator = (
            q_value + a_value + t_value + 2
            if odd
            else q_value + a_value + t_value + 1
        )
        if not (0 < denominator < prime):
            raise AssertionError((prime, a_value, q_value, t_value, denominator))
        ratio = -ratio * numerator * inverse[denominator] % prime
    return answer


def divided_conditions_mod(
    prime: int,
    h_value: int,
    s_value: int,
    factorial: list[int],
    inverse_factorial: list[int],
    inverse: list[int],
) -> tuple[int, int, int, tuple[int, ...]]:
    """Return Q0,Q1,E and normalized data; C_nu/p=6*Q_nu mod p."""
    if prime != 4 * h_value + 6 * s_value + 3:
        raise ValueError((prime, h_value, s_value))
    kernel_0 = kernel_coefficients(h_value, 1, prime, factorial, inverse_factorial)
    kernel_1 = kernel_coefficients(h_value, 4, prime, factorial, inverse_factorial)
    x_value = normalized_sum_mod(kernel_0, s_value, 2 * s_value, True, prime, inverse)
    y_value = normalized_sum_mod(kernel_0, h_value, 2 * s_value, True, prime, inverse)
    u_value = normalized_sum_mod(kernel_1, s_value, 2 * s_value - 1, False, prime, inverse)
    v_value = normalized_sum_mod(kernel_1, h_value, 2 * s_value - 1, True, prime, inverse)

    sign_s = -1 if s_value % 2 else 1
    sign_h = -1 if h_value % 2 else 1
    a_base = (
        sign_s
        * factorial[2 * s_value]
        * factorial[s_value]
        * inverse_factorial[3 * s_value + 1]
    ) % prime
    b_base = (
        sign_h
        * factorial[2 * s_value]
        * factorial[h_value]
        * inverse_factorial[2 * s_value + h_value + 1]
    ) % prime
    c_base = (
        -sign_s
        * factorial[2 * s_value - 1]
        * factorial[s_value - 1]
        * inverse_factorial[3 * s_value - 1]
    ) % prime
    d_base = (
        sign_h
        * factorial[2 * s_value - 1]
        * factorial[h_value]
        * inverse_factorial[2 * s_value + h_value]
    ) % prime
    q0 = (2 * a_base * x_value - b_base * y_value) % prime
    q1 = (2 * c_base * u_value - d_base * v_value) % prime
    eliminant = (
        ((2 * s_value + h_value + 1) * x_value * v_value)
        + 3 * (3 * s_value + 1) * u_value * y_value
    ) * inverse[2 * s_value] % prime
    if q0 == q1 == 0 and eliminant:
        raise AssertionError((prime, h_value, s_value, "necessary eliminant"))
    return q0, q1, eliminant, (
        x_value,
        y_value,
        u_value,
        v_value,
        a_base,
        b_base,
        c_base,
        d_base,
    )


def residue_numerator(m_value: int, nu: int) -> int:
    index = 4 * m_value + nu
    extra = 1 + 3 * nu
    denominator_power = 4 * m_value + 1 + nu
    answer = 0
    for even_index in range(index // 2 + 1):
        remaining = index - 2 * even_index
        numerator_coefficient = 0
        for right_degree in range(extra + 1):
            left_degree = remaining - right_degree
            if 0 <= left_degree <= 6 * m_value:
                numerator_coefficient += (
                    (-1) ** left_degree
                    * math.comb(6 * m_value, left_degree)
                    * math.comb(extra, right_degree)
                )
        answer += (
            (-1) ** even_index
            * math.comb(denominator_power + even_index - 1, even_index)
            * numerator_coefficient
        )
    return answer


# Sparse-free low-to-high polynomial arithmetic over Q.
Poly = tuple[Fraction, ...]
Rat = tuple[Poly, Poly]


def ptrim(poly: list[Fraction] | tuple[Fraction, ...]) -> Poly:
    answer = list(poly)
    while len(answer) > 1 and not answer[-1]:
        answer.pop()
    return tuple(answer or [Fraction(0)])


def padd(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return ptrim(
        [
            (left[index] if index < len(left) else Fraction(0))
            + (right[index] if index < len(right) else Fraction(0))
            for index in range(size)
        ]
    )


def pscale(poly: Poly, scalar: int | Fraction) -> Poly:
    return ptrim([coefficient * Fraction(scalar) for coefficient in poly])


def pmul(left: Poly, right: Poly) -> Poly:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            answer[left_degree + right_degree] += left_coefficient * right_coefficient
    return ptrim(answer)


def pdivmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    if denominator == (Fraction(0),):
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(1, len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    while len(remainder) >= len(denominator) and any(remainder):
        degree = len(remainder) - len(denominator)
        scalar = remainder[-1] / denominator[-1]
        quotient[degree] += scalar
        for index, coefficient in enumerate(denominator):
            remainder[index + degree] -= scalar * coefficient
        remainder = list(ptrim(remainder))
    return ptrim(quotient), ptrim(remainder)


def pgcd(left: Poly, right: Poly) -> Poly:
    while right != (Fraction(0),):
        _, remainder = pdivmod(left, right)
        left, right = right, remainder
    if left == (Fraction(0),):
        return left
    return pscale(left, 1 / left[-1])


def pexact(numerator: Poly, denominator: Poly) -> Poly:
    quotient, remainder = pdivmod(numerator, denominator)
    if remainder != (Fraction(0),):
        raise AssertionError((numerator, denominator, remainder))
    return quotient


def peval(poly: Poly, value: Fraction | int) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def linear(s_coefficient: int, constant: int) -> Poly:
    return ptrim([Fraction(constant), Fraction(s_coefficient)])


def rising_linear(s_coefficient: int, constant: int, length: int) -> Poly:
    answer: Poly = (Fraction(1),)
    for offset in range(length):
        answer = pmul(answer, linear(s_coefficient, constant + offset))
    return answer


def rnormalize(numerator: Poly, denominator: Poly) -> Rat:
    common = pgcd(numerator, denominator)
    numerator = pexact(numerator, common)
    denominator = pexact(denominator, common)
    if denominator[-1] < 0:
        numerator = pscale(numerator, -1)
        denominator = pscale(denominator, -1)
    return numerator, denominator


def radd(left: Rat, right: Rat) -> Rat:
    return rnormalize(
        padd(pmul(left[0], right[1]), pmul(right[0], left[1])),
        pmul(left[1], right[1]),
    )


def rmul(left: Rat, right: Rat) -> Rat:
    return rnormalize(pmul(left[0], right[0]), pmul(left[1], right[1]))


def rscale(value: Rat, scalar: int | Fraction) -> Rat:
    return rnormalize(pscale(value[0], scalar), value[1])


def kernel_integer(h_value: int, extra: int) -> list[int]:
    answer = []
    for degree in range(2 * h_value + extra + 1):
        value = 0
        for right_degree in range(extra + 1):
            left_degree = degree - right_degree
            if 0 <= left_degree <= 2 * h_value:
                value += (
                    math.comb(extra, right_degree)
                    * (-1) ** left_degree
                    * math.comb(2 * h_value, left_degree)
                )
        answer.append(value)
    return answer


def normalized_sum_symbolic(
    kernel: list[int],
    a_s: int,
    a_constant: int,
    q_s: int,
    q_constant: int,
    odd: bool,
) -> Rat:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    answer: Rat = ((Fraction(0),), (Fraction(1),))
    for t_value in range(maximum_t + 1):
        numerator_constant = a_constant + (1 if odd else 0)
        denominator_constant = q_constant + a_constant + (2 if odd else 1)
        numerator = rising_linear(a_s, numerator_constant, t_value)
        denominator = rising_linear(q_s + a_s, denominator_constant, t_value)
        degree = 2 * t_value + 1 if odd else 2 * t_value
        term = rscale(rnormalize(numerator, denominator), (-1) ** t_value * kernel[degree])
        answer = radd(answer, term)
    return answer


def fixed_h_eliminant(h_value: int) -> Rat:
    kernel_0 = kernel_integer(h_value, 1)
    kernel_1 = kernel_integer(h_value, 4)
    x_value = normalized_sum_symbolic(kernel_0, 1, 0, 2, 0, True)
    y_value = normalized_sum_symbolic(kernel_0, 0, h_value, 2, 0, True)
    u_value = normalized_sum_symbolic(kernel_1, 1, 0, 2, -1, False)
    v_value = normalized_sum_symbolic(kernel_1, 0, h_value, 2, -1, True)
    first = rmul(rnormalize(linear(2, h_value + 1), linear(2, 0)), rmul(x_value, v_value))
    second = rmul(rnormalize(linear(9, 3), linear(2, 0)), rmul(u_value, y_value))
    return radd(first, second)


def primitive_integer(poly: Poly) -> tuple[int, ...]:
    lcm = 1
    for coefficient in poly:
        lcm = math.lcm(lcm, coefficient.denominator)
    values = [coefficient.numerator * (lcm // coefficient.denominator) for coefficient in poly]
    common = 0
    for value in values:
        common = math.gcd(common, abs(value))
    values = [value // common for value in values]
    if values[-1] < 0:
        values = [-value for value in values]
    return tuple(values)


def polynomial_digest(coefficients: tuple[int, ...]) -> str:
    return hashlib.sha256((",".join(map(str, coefficients)) + "\n").encode("ascii")).hexdigest()


def resultant_linear(coefficients: tuple[int, ...], h_value: int) -> int:
    degree = len(coefficients) - 1
    constant = 4 * h_value + 3
    return sum(
        coefficient * (-constant) ** index * 6 ** (degree - index)
        for index, coefficient in enumerate(coefficients)
    )


def mod_trim(poly: list[int], prime: int) -> list[int]:
    answer = [value % prime for value in poly]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def mod_divmod(numerator: list[int], denominator: list[int], prime: int) -> tuple[list[int], list[int]]:
    numerator = mod_trim(numerator, prime)
    denominator = mod_trim(denominator, prime)
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, prime)
    while len(numerator) >= len(denominator) and numerator != [0]:
        degree = len(numerator) - len(denominator)
        scalar = numerator[-1] * inverse_lead % prime
        quotient[degree] = scalar
        for index, coefficient in enumerate(denominator):
            numerator[index + degree] = (numerator[index + degree] - scalar * coefficient) % prime
        numerator = mod_trim(numerator, prime)
    return mod_trim(quotient, prime), numerator


def mod_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    while mod_trim(right, prime) != [0]:
        _, remainder = mod_divmod(left, right, prime)
        left, right = right, remainder
    left = mod_trim(left, prime)
    inverse_lead = pow(left[-1], -1, prime)
    return [(value * inverse_lead) % prime for value in left]


def mod_mul_reduce(left: list[int], right: list[int], modulus: list[int], prime: int) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i_value, left_value in enumerate(left):
        for j_value, right_value in enumerate(right):
            product[i_value + j_value] = (product[i_value + j_value] + left_value * right_value) % prime
    _, remainder = mod_divmod(product, modulus, prime)
    return remainder


def mod_pow_x(exponent: int, modulus: list[int], prime: int) -> list[int]:
    answer = [1]
    factor = [0, 1]
    while exponent:
        if exponent & 1:
            answer = mod_mul_reduce(answer, factor, modulus, prime)
        exponent >>= 1
        if exponent:
            factor = mod_mul_reduce(factor, factor, modulus, prime)
    return mod_trim(answer, prime)


def distinct_prime_divisors(value: int) -> list[int]:
    answer = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            answer.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        answer.append(value)
    return answer


def irreducible_mod(coefficients: tuple[int, ...], prime: int) -> bool:
    modulus = mod_trim(list(coefficients), prime)
    degree = len(modulus) - 1
    if degree != len(coefficients) - 1:
        return False
    x_poly = [0, 1]
    for divisor in distinct_prime_divisors(degree):
        powered = mod_pow_x(prime ** (degree // divisor), modulus, prime)
        difference = powered + [0] * max(0, 2 - len(powered))
        difference[1] = (difference[1] - 1) % prime
        if len(mod_gcd(modulus, difference, prime)) > 1:
            return False
    powered = mod_pow_x(prime**degree, modulus, prime)
    powered += [0] * max(0, 2 - len(powered))
    powered[1] = (powered[1] - 1) % prime
    return mod_trim(powered, prime) == [0]


RESULTANT_FACTORS = {
    1: {2: 4, 3: 1, 13: 1},
    2: {2: 6, 859: 1},
    4: {2: 10, 3: 1, 5: 1, 7: 1, 13: 1, 1219909: 1},
    5: {2: 11, 5: 2, 7: 2, 53: 1, 1033: 1, 3463: 1},
    7: {2: 16, 3: 1, 5: 2, 7: 2, 11: 1, 13: 1, 73: 1, 1103: 1, 1409: 1, 32533: 1},
    8: {2: 18, 5: 3, 7: 2, 11: 1, 13: 1, 47: 1, 1314127: 1, 8383391: 1},
}
EXPECTED_RESULTANTS = {
    1: 624,
    2: -54976,
    4: 1705140003840,
    5: -475657910425600,
    7: 127117923618801750835200,
    8: -118887712469320504213504000,
}
IRREDUCIBILITY_WITNESSES = {1: 5, 4: 11, 5: 11, 7: 67, 8: 113}
EXPECTED_ELIMINANT_SCALARS = {
    1: Fraction(-2),
    2: Fraction(-2),
    4: Fraction(4, 3),
    5: Fraction(8, 3),
    7: Fraction(-32, 9),
    8: Fraction(-16, 9),
}
# Primitive denominator factorizations, represented by a*s+b.
EXPECTED_DENOMINATOR_FACTORS = {
    1: [(1, 0), (2, 3), (3, 2)],
    2: [(1, 0), (1, 2), (2, 5), (3, 2)],
    4: [(1, 0), (1, 3), (1, 4), (2, 7), (2, 9), (3, 2), (3, 4), (3, 5)],
    5: [(1, 0), (1, 4), (1, 5), (2, 7), (2, 9), (2, 11), (3, 2), (3, 4), (3, 5)],
    7: [
        (1, 0), (1, 5), (1, 6), (1, 7),
        (2, 9), (2, 11), (2, 13), (2, 15),
        (3, 2), (3, 4), (3, 5), (3, 7), (3, 8),
    ],
    8: [
        (1, 0), (1, 5), (1, 6), (1, 7), (1, 8),
        (2, 11), (2, 13), (2, 15), (2, 17),
        (3, 2), (3, 4), (3, 5), (3, 7), (3, 8),
    ],
}
EXPECTED_CANDIDATES = {
    1: [(13, 1, 9, 4)],
    2: [],
    4: [(1219909, 203315, 833864, 86967)],
    5: [(53, 5, 36, 14)],
    7: [(73, 7, 32, 58), (32533, 5417, 20350, 11902)],
    8: [(47, 2, 30, 41), (8383391, 1397226, 6424621, 1596119)],
}


def selective_factorials(prime: int, indices: set[int]) -> dict[int, int]:
    values = {0: 1}
    factorial = 1
    for index in range(1, max(indices) + 1):
        factorial = factorial * index % prime
        if index in indices:
            values[index] = factorial
    return values


def candidate_conditions(prime: int, h_value: int, s_value: int) -> tuple[int, int]:
    indices = {
        h_value,
        s_value - 1,
        s_value,
        2 * s_value - 1,
        2 * s_value,
        3 * s_value - 1,
        3 * s_value + 1,
        2 * s_value + h_value,
        2 * s_value + h_value + 1,
    }
    factorial = selective_factorials(prime, indices)

    def fact(index: int) -> int:
        return factorial[index]

    sign_s = prime - 1 if s_value % 2 else 1
    sign_h = prime - 1 if h_value % 2 else 1
    a_base = sign_s * fact(2 * s_value) * fact(s_value) * pow(fact(3 * s_value + 1), -1, prime) % prime
    b_base = sign_h * fact(2 * s_value) * fact(h_value) * pow(fact(2 * s_value + h_value + 1), -1, prime) % prime
    c_base = (-sign_s) * fact(2 * s_value - 1) * fact(s_value - 1) * pow(fact(3 * s_value - 1), -1, prime) % prime
    d_base = sign_h * fact(2 * s_value - 1) * fact(h_value) * pow(fact(2 * s_value + h_value), -1, prime) % prime
    kernel_0 = kernel_integer(h_value, 1)
    kernel_1 = kernel_integer(h_value, 4)

    def norm(kernel: list[int], a_value: int, q_value: int, odd: bool) -> int:
        maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
        ratio = 1
        answer = 0
        for t_value in range(maximum_t + 1):
            degree = 2 * t_value + 1 if odd else 2 * t_value
            answer = (answer + ratio * kernel[degree]) % prime
            if t_value < maximum_t:
                numerator = a_value + t_value + 1 if odd else a_value + t_value
                denominator = q_value + a_value + t_value + 2 if odd else q_value + a_value + t_value + 1
                ratio = -ratio * numerator * pow(denominator, -1, prime) % prime
        return answer

    x_value = norm(kernel_0, s_value, 2 * s_value, True)
    y_value = norm(kernel_0, h_value, 2 * s_value, True)
    u_value = norm(kernel_1, s_value, 2 * s_value - 1, False)
    v_value = norm(kernel_1, h_value, 2 * s_value - 1, True)
    return (
        (2 * a_base * x_value - b_base * y_value) % prime,
        (2 * c_base * u_value - d_base * v_value) % prime,
    )


def certificate(prime_max: int, integer_bridge_prime_max: int) -> dict[str, Any]:
    if prime_max < 2000 or integer_bridge_prime_max < 31:
        raise ValueError("canonical run requires prime_max>=2000 and bridge prime max>=31")

    # Fixed cell coefficients in both frozen normalizations.
    a_value, c_value = 4, 3
    # A(y)=1-3y+2y^2, D(y)=1-2y+2y^2.  Only degree two is needed.
    def ratio_coefficients(a_exponent: int, d_exponent: int) -> list[int]:
        numerator = [1]
        for _ in range(a_exponent):
            next_values = [0] * min(3, len(numerator) + 2)
            for i_value, left in enumerate(numerator):
                for j_value, right in enumerate((1, -3, 2)):
                    if i_value + j_value < 3:
                        next_values[i_value + j_value] += left * right
            numerator = next_values
        inverse_d = [1, 2, 2]
        denominator = [1]
        for _ in range(d_exponent):
            next_values = [0] * min(3, len(denominator) + 2)
            for i_value, left in enumerate(denominator):
                for j_value, right in enumerate(inverse_d):
                    if i_value + j_value < 3:
                        next_values[i_value + j_value] += left * right
            denominator = next_values
        result = [0, 0, 0]
        for i_value, left in enumerate(numerator):
            for j_value, right in enumerate(denominator):
                if i_value + j_value < 3:
                    result[i_value + j_value] += left * right
        return result

    u_series = ratio_coefficients(3, 3)
    v_series = ratio_coefficients(4, 4)
    j_vector = (a_value * u_series[2], a_value * u_series[1], -c_value * v_series[2], -c_value * v_series[1])
    if j_vector != (-12, -12, 6, 12):
        raise AssertionError(j_vector)

    # FINITE p<=prime_max scan of every admissible j=1 row.
    rows = []
    zero_rows = []
    eliminant_zero_rows = []
    integer_bridge_rows = 0
    for prime in primes_upto(prime_max):
        if prime <= 5:
            continue
        factorial, inverse_factorial, inverse = factorial_tables(prime)
        for s_value in range(1, (prime - 3) // 6 + 1):
            residual = prime - 6 * s_value - 3
            if residual < 0 or residual % 4:
                continue
            h_value = residual // 4
            if h_value < 1:
                continue
            q0, q1, eliminant, _ = divided_conditions_mod(
                prime, h_value, s_value, factorial, inverse_factorial, inverse
            )
            row = (prime, h_value, s_value, q0, q1, eliminant)
            rows.append(row)
            if q0 == 0 or q1 == 0:
                zero_rows.append(row)
            if eliminant == 0:
                eliminant_zero_rows.append(row)
            if q0 == q1 == 0:
                raise AssertionError((row, "finite common row"))

            if prime <= integer_bridge_prime_max:
                m_value = 3 * h_value + 4 * s_value + 2
                for nu, q_value in enumerate((q0, q1)):
                    coefficient = residue_numerator(m_value, nu)
                    if coefficient % prime or coefficient // prime % prime != 6 * q_value % prime:
                        raise AssertionError((prime, h_value, s_value, m_value, nu, q_value))
                integer_bridge_rows += 1

    row_payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    zero_payload = "".join(",".join(map(str, row)) + "\n" for row in zero_rows).encode("ascii")
    if (
        len(rows),
        sum(row[3] == 0 for row in rows),
        sum(row[4] == 0 for row in rows),
        len(zero_rows),
        len(eliminant_zero_rows),
        hashlib.sha256(row_payload).hexdigest(),
    ) != (
        22934,
        20,
        26,
        46,
        58,
        "b641131ccb68bea399df3bc40429916f639da72546ef7c2da61d890158d778b6",
    ):
        raise AssertionError("canonical finite scan changed")

    # Exact all-s classification on h<=8 by rational eliminants.
    fixed_h_rows = []
    for h_value in (1, 2, 4, 5, 7, 8):
        eliminant = fixed_h_eliminant(h_value)
        numerator = primitive_integer(eliminant[0])
        denominator = primitive_integer(eliminant[1])

        denominator_product: Poly = (Fraction(1),)
        for s_coefficient, constant in EXPECTED_DENOMINATOR_FACTORS[h_value]:
            denominator_product = pmul(denominator_product, linear(s_coefficient, constant))
            # For every s>=1 this factor lies strictly between 0 and
            # p=6s+4h+3, hence is a p-unit on an admissible row.
            if s_coefficient + constant >= 4 * h_value + 9:
                raise AssertionError((h_value, s_coefficient, constant, "unit bound"))
        if denominator_product != tuple(map(Fraction, denominator)):
            raise AssertionError((h_value, "denominator factorization"))

        def scale_against_primitive(poly: Poly, primitive: tuple[int, ...]) -> Fraction:
            for coefficient, primitive_coefficient in zip(poly, primitive):
                if primitive_coefficient:
                    return coefficient / primitive_coefficient
            raise AssertionError("zero primitive polynomial")

        eliminant_scalar = scale_against_primitive(eliminant[0], numerator) / scale_against_primitive(
            eliminant[1], denominator
        )
        if eliminant_scalar != EXPECTED_ELIMINANT_SCALARS[h_value]:
            raise AssertionError((h_value, eliminant_scalar, "eliminant scalar"))
        if any(
            prime_factor not in (2, 3)
            for prime_factor in distinct_prime_divisors(
                abs(eliminant_scalar.numerator * eliminant_scalar.denominator)
            )
        ):
            raise AssertionError((h_value, eliminant_scalar, "scalar unit audit"))

        resultant = resultant_linear(numerator, h_value)
        if resultant != EXPECTED_RESULTANTS[h_value]:
            raise AssertionError((h_value, resultant))
        reconstructed = 1
        for factor, exponent in RESULTANT_FACTORS[h_value].items():
            if not is_prime(factor):
                raise AssertionError((h_value, factor, "nonprime listed factor"))
            reconstructed *= factor**exponent
        if reconstructed != abs(resultant):
            raise AssertionError((h_value, reconstructed, resultant))

        if h_value == 2:
            first_factor = (13, 11, 2)
            second_factor = (27, 80, 64)
            if pmul(tuple(map(Fraction, first_factor)), tuple(map(Fraction, second_factor))) != tuple(
                map(Fraction, numerator)
            ):
                raise AssertionError((h_value, "quadratic factorization"))
            factorization = ["2*s^2+11*s+13", "64*s^2+80*s+27"]
            irreducibility = "both quadratic discriminants (17 and -512) are nonsquares"
        else:
            witness = IRREDUCIBILITY_WITNESSES[h_value]
            if not irreducible_mod(numerator, witness):
                raise AssertionError((h_value, witness, "irreducibility witness"))
            factorization = [f"irreducible degree {len(numerator)-1} over Z (mod {witness} witness)"]
            irreducibility = f"Rabin irreducibility certificate modulo {witness}"

        candidates = []
        for factor in RESULTANT_FACTORS[h_value]:
            if factor >= 4 * h_value + 9 and (factor - (4 * h_value + 3)) % 6 == 0:
                s_value = (factor - (4 * h_value + 3)) // 6
                q0, q1 = candidate_conditions(factor, h_value, s_value)
                candidates.append((factor, s_value, q0, q1))
        if candidates != EXPECTED_CANDIDATES[h_value]:
            raise AssertionError((h_value, candidates))
        if any(q0 == q1 == 0 for _, _, q0, q1 in candidates):
            raise AssertionError((h_value, "candidate survived"))
        fixed_h_rows.append(
            {
                "h": h_value,
                "eliminant_numerator_degree": len(numerator) - 1,
                "eliminant_numerator_coefficients_low_to_high": list(numerator),
                "eliminant_numerator_sha256": polynomial_digest(numerator),
                "eliminant_numerator_factorization": factorization,
                "irreducibility_certificate": irreducibility,
                "exact_eliminant_scalar_times_primitive_ratio": str(eliminant_scalar),
                "eliminant_denominator_coefficients_low_to_high_up_to_scalar": list(denominator),
                "eliminant_denominator_factorization": [
                    {"s_coefficient": s_coefficient, "constant": constant}
                    for s_coefficient, constant in EXPECTED_DENOMINATOR_FACTORS[h_value]
                ],
                "denominator_unit_audit": (
                    "every a*s+b factor is positive and <p=6s+4h+3 for s>=1; "
                    "the remaining scalar uses only 2 and 3, while admissible p is odd and p!=3"
                ),
                "resultant": resultant,
                "resultant_factorization": [[factor, exponent] for factor, exponent in RESULTANT_FACTORS[h_value].items()],
                "phase_compatible_candidate_checks": [
                    {"p": prime, "s": s_value, "Q0": q0, "Q1": q1}
                    for prime, s_value, q0, q1 in candidates
                ],
            }
        )

    return {
        "item": 218,
        "arithmetic": "exact integers, fractions, finite-field polynomials, and fully factored declared resultants; standard library only",
        "proved_j1_reduction": {
            "parameters": "h=(p-6s-3)/4; p=4h+6s+3; r=2h; m=3h+4s+2",
            "admissibility": "h>=1, s>=1, p prime; h=0 mod 3 is impossible because then 3 divides p>3",
            "a_c": [a_value, c_value],
            "J1": list(j_vector),
            "item197_fixed_coefficients": {"U1": 0, "V1": 2, "W1": -4},
            "divided_conditions": "C_nu/p = 6*Q_nu (mod p), Q_nu=2*H_nu(T)-H_nu(L_nu)",
            "targets": {
                "T": "2h+6s+2",
                "L0": "4h+4s+2",
                "L1": "4h+4s+3",
            },
            "tail_kernel": "H_nu(N)=[z^N]P_nu(z)*log(1+z^2) over Q; every denominator is a p-unit",
            "normalized_equations": "Q0=2*A*x-B*y; Q1=2*C*u-D*v",
            "bases": {
                "A": "(-1)^s*(2s)!*s!/(3s+1)!",
                "B": "(-1)^h*(2s)!*h!/(2s+h+1)!",
                "C": "(-1)^(s-1)*(2s-1)!*(s-1)!/(3s-1)!",
                "D": "(-1)^h*(2s-1)!*h!/(2s+h)!",
            },
            "necessary_eliminant": "E_h(s)=((2s+h+1)/(2s))*x*v+(3(3s+1)/(2s))*u*y",
            "remaining_binomial_residue": "B/A=(-1)^(h-s)*h!*C(3s+1,s)/(2s+2)_h (mod p)",
        },
        "proved_twisted_derivative_reduction": {
            "identity": "P1=alpha*P0+beta*P0'",
            "alpha": "(2h+4s-1)/(4s)+(h+2s)z/s+(2h+4s+1)z^2/(4s)",
            "beta": "(1-z^2)(1+z)/(4s)",
            "boundary": "beta*P0*d(log(1+z^2))/dz is a polynomial of degree deg(P0)+2 and has zero coefficient at both nu=1 targets",
            "all_index_tail_identity": (
                "4s*H1(N)=(N+1)H0(N+1)+(N+2h+4s-1)H0(N)"
                "+(4h+8s+1-N)H0(N-1)+(2h+4s+3-N)H0(N-2), "
                "valid for N>deg(P0)+2"
            ),
            "uniqueness_domain": "unique with deg(alpha)<=2 and deg(beta)<=3",
            "consequence": "the finite-log symbol is removed locally, but a tail transfer over |L0-T|=2|h-s| remains",
        },
        "proved_all_s_residual_strip": {
            "scope": "every admissible j=1 row with 0<=h<=8",
            "automatic_composite_h": [0, 3, 6],
            "factored_eliminants": fixed_h_rows,
            "verdict": "no simultaneous divided-coordinate zero for any prime on these residual lines",
        },
        "finite_scan": {
            "label": "FINITE exact scan only; no extrapolation",
            "prime_max": prime_max,
            "rows": len(rows),
            "Q0_zero": sum(row[3] == 0 for row in rows),
            "Q1_zero": sum(row[4] == 0 for row in rows),
            "separate_zero_rows": len(zero_rows),
            "common_zero_rows": 0,
            "necessary_eliminant_zero_rows": len(eliminant_zero_rows),
            "row_sha256": hashlib.sha256(row_payload).hexdigest(),
            "zero_row_sha256": hashlib.sha256(zero_payload).hexdigest(),
            "first_three_separate_zero_rows": [list(row) for row in zero_rows[:3]],
            "integer_bridge_prime_max": integer_bridge_prime_max,
            "integer_bridge_rows": integer_bridge_rows,
        },
        "rate_ledger": {
            "actual_new_usable_coefficient": 0,
            "reason": "the proved h<=8 strip is thin and the full j=1 cell remains open",
            "j1_cell_per_m": "1/6",
            "j1_cell_per_6m": "1/36",
            "conditional_after_full_j1_exclusion_per_6m": "0.0283968068886832...",
            "j2_cell_per_m": "2/35",
            "conditional_after_full_j1_and_j2_exclusion_per_m": "C0-47/210=0.1132379841892420...",
            "conditional_after_full_j1_and_j2_exclusion_per_6m": "0.0188729973648737...",
            "gap_below_G_if_both_excluded_per_6m": "0.0007599863045581...",
        },
        "labels": {
            "PROVED": [
                "exact p,s,h parameterization and both divided-coordinate conditions",
                "palindromic reduction to rational low tails with p-unit denominators",
                "twisted derivative identity and vanishing local boundary",
                "necessary rational eliminant and residual binomial congruence",
                "complete all-s exclusion on 0<=h<=8",
            ],
            "FINITE": ["all 22,934 admissible rows through p<=2000; 46 separate zeros and no common zero"],
            "OPEN": [
                "all-prime exclusion for unbounded h",
                "uniform control of the moving binomial/hypergeometric residue B/A",
                "any positive Route-1 rate consequence from the j=1 cell",
                "the j=2 classification",
            ],
        },
        "verdict": (
            "PROVED an exact rational-tail and Hermite reduction and excluded every j=1 row on h<=8; "
            "FINITE p<=2000 finds no common zero. Unbounded h remains OPEN, so the actual rate gain is zero."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=2000)
    parser.add_argument("--integer-bridge-prime-max", type=int, default=31)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.prime_max, args.integer_bridge_prime_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "rows": result["finite_scan"]["rows"],
                "common_zero_rows": result["finite_scan"]["common_zero_rows"],
                "row_sha256": result["finite_scan"]["row_sha256"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
