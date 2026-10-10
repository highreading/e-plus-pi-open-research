#!/usr/bin/env python3
"""Exact certificate for Item 234: the first j=1 p^2/Witt lift.

Only the Python standard library is used.  Symbolic identities are proved in
the companion report; this checker replays their coefficient, rational-moment,
terminal-multiplicity, and finite-census consequences deterministically.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item234_j1_first_witt_certificate.json"

DEPENDENCIES = {
    "sources/item197_common_log_locus_report.md":
        "2241656ac9c47e81b5026449a97c15bed7d35290bf2b6a91cdfed4bb3fe3683c",
    "scripts/item197_common_log_locus_certificate.py":
        "f85c36169c7eb0aee3fb73f8030d3ddb2296b00077370012be84479eea9aeeb9",
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "scripts/item218_j1_common_log_certificate.py":
        "a238c5ca37263f2553da47bf3f21253aedf1c34f8c57458a4a274fc6cdc9029a",
    "sources/item223_j1_frobenius_transfer_report.md":
        "d1102c3efec35e9b08d1a8bcdf46f1b00b33b18f20391016a4e17632b0c4a2e0",
    "scripts/item223_j1_frobenius_transfer_certificate.py":
        "928ddc876ed70939fd4a39fccd0e91d8c59d8aa2a8a694967d8fc7f737512d4a",
    "sources/item228_j1_second_frobenius_report.md":
        "a2c9c474e24ff7eedddc5abdc48569022f4707119be36fe06146673eb250cc99",
    "scripts/item228_j1_second_frobenius_certificate.py":
        "4264f7df929a269633fe71865d9b47910e4d6d1bf0a91bdb9ceb2e3774171220",
    "sources/item230_j1_phase_closure_report.md":
        "d5172233ca5dcdd3ba49ea7fd870de582d625975d8ca0b55d2ae10f94204fa72",
    "scripts/item230_j1_phase_closure_certificate.py":
        "0722964a47817ca2dcd93cc9013339f16d2d6a6271893938c7d473cc6115fe0b",
}


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def resolve_dependency(relative_name: str) -> Path:
    candidates = (HERE.parent / relative_name, HERE / Path(relative_name).name)
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(relative_name)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


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


def rows_upto(limit: int):
    for prime in primes_upto(limit):
        if prime < 13:
            continue
        for s_value in range(1, (prime - 7) // 6 + 1):
            remainder = prime - 6 * s_value - 3
            if remainder > 0 and remainder % 4 == 0:
                h_value = remainder // 4
                if h_value >= 1:
                    yield prime, h_value, s_value


def convolution(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i_value, left_value in enumerate(left):
        if left_value:
            for j_value, right_value in enumerate(right):
                if right_value:
                    answer[i_value + j_value] += left_value * right_value
    return answer


def convolution_mod(
    left: list[int], right: list[int], modulus: int, limit: int | None = None
) -> list[int]:
    maximum = len(left) + len(right) - 2
    if limit is not None:
        maximum = min(maximum, limit)
    answer = [0] * (maximum + 1)
    for i_value, left_value in enumerate(left):
        if not left_value or i_value > maximum:
            continue
        last = min(len(right) - 1, maximum - i_value)
        for j_value in range(last + 1):
            right_value = right[j_value]
            if right_value:
                answer[i_value + j_value] = (
                    answer[i_value + j_value] + left_value * right_value
                ) % modulus
    return answer


def coefficient_product(left: list[int], right: list[int], degree: int, modulus: int) -> int:
    if degree < 0:
        return 0
    lower = max(0, degree - len(right) + 1)
    upper = min(len(left) - 1, degree)
    return sum(
        left[index] * right[degree - index] for index in range(lower, upper + 1)
    ) % modulus


def p_polynomial(prime: int, h_value: int, s_value: int, nu: int) -> list[int]:
    r_value = 2 * h_value
    q_value = 2 * s_value - nu
    left = [(-1) ** degree * math.comb(r_value, degree) for degree in range(r_value + 1)]
    middle = [math.comb(1 + 3 * nu, degree) for degree in range(2 + 3 * nu)]
    even = [0] * (2 * q_value + 1)
    for degree in range(q_value + 1):
        even[2 * degree] = math.comb(q_value, degree)
    return convolution(convolution(left, middle), even)


def w_polynomial(h_value: int, s_value: int) -> list[int]:
    r_value = 2 * h_value
    left = [(-1) ** degree * math.comb(r_value, degree) for degree in range(r_value + 1)]
    even = [0] * (4 * s_value - 1)
    for degree in range(2 * s_value):
        even[2 * degree] = math.comb(2 * s_value - 1, degree)
    return convolution(left, even)


def log_coefficient(poly: list[int], degree: int) -> Fraction:
    answer = Fraction(0)
    for index in range(1, degree // 2 + 1):
        source = degree - 2 * index
        if source < len(poly):
            answer += Fraction(((-1) ** (index - 1)) * poly[source], index)
    return answer


def finite_b_coefficient(poly: list[int], degree: int, prime: int) -> Fraction:
    answer = Fraction(0)
    for index in range(1, prime):
        source = degree - 2 * index
        if 0 <= source < len(poly):
            answer += Fraction(((-1) ** (index - 1)) * poly[source], index)
    return answer


def ell_value(exponent: int, epsilon: int) -> int:
    # ell_q=(2e-i)(-i)^(q+1)+(2e+i)i^(q+1), evaluated in Z.
    residue = exponent % 4
    return (-2, -4 * epsilon, 2, 4 * epsilon)[residue]


def exact_moment(poly: list[int], exponent_shift: int, epsilon: int) -> Fraction:
    return sum(
        (
            Fraction(coefficient * ell_value(exponent_shift + degree, epsilon),
                     exponent_shift + degree + 1)
            for degree, coefficient in enumerate(poly)
        ),
        Fraction(0),
    )


def q_r_m_j(
    prime: int, h_value: int, s_value: int, nu: int
) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    r_value = 2 * h_value
    q_value = 2 * s_value - nu
    poly = p_polynomial(prime, h_value, s_value, nu)
    low = prime - q_value - 1
    high = 2 * prime - q_value - 1
    target = r_value + 6 * s_value + 2
    y_value = finite_b_coefficient(poly, low, prime)
    y_prime = finite_b_coefficient(poly, high, prime)
    h_one = 2 * y_prime - y_value
    q_exact = 2 * log_coefficient(poly, target) - log_coefficient(poly, low)
    reflection_carry = sum(
        (
            Fraction(((-1) ** index) * poly[target - 2 * index], index * (prime - index))
            for index in range(1, prime)
            if 0 <= target - 2 * index < len(poly)
        ),
        Fraction(0),
    )
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    moment = exact_moment(poly, prime + r_value, epsilon)

    # Reindex M using palindromicity. D_a=N-a lies strictly in (p,2p).
    n_value = 2 * prime - q_value - 1
    hermite_carry = Fraction(0)
    for degree, coefficient in enumerate(poly):
        denominator = n_value - degree
        if not (prime < denominator < 2 * prime):
            raise AssertionError((prime, h_value, s_value, nu, degree, denominator))
        if denominator % 2:
            other = denominator - prime
            if not (0 < other < prime):
                raise AssertionError((prime, denominator, other))
            hermite_carry += Fraction(
                coefficient
                * 2
                * epsilon
                * ((-1) ** ((denominator - 1) // 2)),
                denominator * other,
            )

    if h_one != q_exact + 2 * prime * reflection_carry:
        raise AssertionError((prime, h_value, s_value, nu, "reflection carry"))
    if h_one != -epsilon * moment + prime * hermite_carry:
        raise AssertionError((prime, h_value, s_value, nu, "Hermite carry"))
    return q_exact, reflection_carry, moment, hermite_carry, h_one


def fraction_mod(value: Fraction, modulus: int) -> int:
    if math.gcd(value.denominator, modulus) != 1:
        raise AssertionError((value, modulus, "nonunit denominator"))
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def divided_fraction_mod(value: Fraction, prime: int) -> int:
    if value.numerator % prime:
        raise AssertionError((value, prime, "not divisible by p"))
    if value.denominator % prime == 0:
        raise AssertionError((value, prime, "nonunit denominator"))
    return (value.numerator // prime) * pow(value.denominator, -1, prime) % prime


def original_coefficient(m_value: int, nu: int) -> int:
    target = 4 * m_value + nu
    extra = 1 + 3 * nu
    numerator = [0] * (target + 1)
    for degree in range(target + 1):
        numerator[degree] = sum(
            (
                (-1) ** (degree - right)
                * math.comb(6 * m_value, degree - right)
                * math.comb(extra, right)
                for right in range(extra + 1)
                if 0 <= degree - right <= 6 * m_value
            ),
            0,
        )
    denominator_power = 4 * m_value + 1 + nu
    answer = 0
    for index in range(target // 2 + 1):
        answer += (
            (-1) ** index
            * math.comb(denominator_power + index - 1, index)
            * numerator[target - 2 * index]
        )
    return answer


def harmonic_digits(prime: int) -> tuple[list[int], list[int], list[int], list[int]]:
    a_zero = [0] * prime
    a_one = [0] * prime
    b_zero = [0] * (2 * prime - 1)
    b_one = [0] * (2 * prime - 1)
    harmonic = 0
    for index in range(1, prime):
        inverse = pow(index, -1, prime)
        a_zero[index] = -inverse % prime
        a_one[index] = harmonic * inverse % prime
        sign = 1 if index % 2 else -1
        b_zero[2 * index] = sign * inverse % prime
        b_one[2 * index] = -sign * harmonic * inverse % prime
        harmonic = (harmonic + inverse) % prime
    return a_zero, a_one, b_zero, b_one


def frobenius_sections(a_power: int, b_power: int, prime: int, maximum: int, modulus: int) -> dict[int, int]:
    answer: dict[int, int] = {}
    for left_index in range(a_power + 1):
        for right_index in range(maximum // (2 * prime) + 1):
            degree = (left_index + 2 * right_index) * prime
            if degree > maximum:
                continue
            coefficient = (
                (-1) ** (left_index + right_index)
                * math.comb(a_power, left_index)
                * math.comb(b_power + right_index - 1, right_index)
            )
            answer[degree] = (answer.get(degree, 0) + coefficient) % modulus
    return answer


def sectioned_coefficient(
    a_power: int,
    b_power: int,
    kernel: list[int],
    poly: list[int],
    target: int,
    prime: int,
) -> int:
    sections = frobenius_sections(a_power, b_power, prime, target, prime)
    return sum(
        coefficient * coefficient_product(kernel, poly, target - shift, prime)
        for shift, coefficient in sections.items()
    ) % prime


def e_digit(prime: int, h_value: int, s_value: int, nu: int) -> int:
    poly = [value % prime for value in p_polynomial(prime, h_value, s_value, nu)]
    q_value = 2 * s_value - nu
    target = 3 * prime - q_value - 1
    a_zero, a_one, b_zero, b_one = harmonic_digits(prime)
    aa = convolution_mod(a_zero, a_zero, prime, target)
    ab = convolution_mod(a_zero, b_zero, prime, target)
    bb = convolution_mod(b_zero, b_zero, prime, target)
    value = (
        4 * sectioned_coefficient(3, 3, a_one, poly, target, prime)
        - 3 * sectioned_coefficient(4, 4, b_one, poly, target, prime)
        + 6 * sectioned_coefficient(2, 3, aa, poly, target, prime)
        - 12 * sectioned_coefficient(3, 4, ab, poly, target, prime)
        + 6 * sectioned_coefficient(4, 5, bb, poly, target, prime)
    ) % prime
    return value


def q_mod_direct(prime: int, h_value: int, s_value: int, nu: int, modulus: int) -> int:
    poly = p_polynomial(prime, h_value, s_value, nu)
    q_value = 2 * s_value - nu
    target = 2 * h_value + 6 * s_value + 2
    low = prime - q_value - 1

    def h_value_at(degree: int) -> int:
        answer = 0
        for index in range(1, degree // 2 + 1):
            source = degree - 2 * index
            if source < len(poly):
                answer += (
                    (-1) ** (index - 1)
                    * poly[source]
                    * pow(index, -1, modulus)
                )
        return answer % modulus

    return (2 * h_value_at(target) - h_value_at(low)) % modulus


def r_mod_direct(prime: int, h_value: int, s_value: int, nu: int) -> int:
    poly = p_polynomial(prime, h_value, s_value, nu)
    target = 2 * h_value + 6 * s_value + 2
    answer = 0
    for index in range(1, prime):
        source = target - 2 * index
        if 0 <= source < len(poly):
            answer += (
                (-1) ** index
                * poly[source]
                * pow(index * (prime - index), -1, prime)
            )
    return answer % prime


def moment_j_mod(
    prime: int, h_value: int, s_value: int, nu: int
) -> tuple[int, int]:
    """Return M modulo p^2 and the explicit Hermite carry J modulo p."""
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    q_value = 2 * s_value - nu
    n_value = 2 * prime - q_value - 1
    poly = p_polynomial(prime, h_value, s_value, nu)
    moment = 0
    carry = 0
    for degree, coefficient in enumerate(poly):
        denominator = n_value - degree
        if not (prime < denominator < 2 * prime):
            raise AssertionError((prime, h_value, s_value, nu, degree, denominator))
        moment += (
            coefficient
            * ell_value(denominator - 1, epsilon)
            * pow(denominator, -1, prime * prime)
        )
        if denominator % 2:
            carry += (
                coefficient
                * 2
                * epsilon
                * ((-1) ** ((denominator - 1) // 2))
                * pow(denominator * (denominator - prime), -1, prime)
            )
    return moment % (prime * prime), carry % prime


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
        ratio = -ratio * numerator * inverse[denominator] % prime
    return answer


def q_pair_fast(prime: int, h_value: int, s_value: int) -> tuple[int, int]:
    factorial, inverse_factorial, inverse = factorial_tables(prime)
    kernel_0 = kernel_coefficients(h_value, 1, prime, factorial, inverse_factorial)
    kernel_1 = kernel_coefficients(h_value, 4, prime, factorial, inverse_factorial)
    x_value = normalized_sum_mod(kernel_0, s_value, 2 * s_value, True, prime, inverse)
    y_value = normalized_sum_mod(kernel_0, h_value, 2 * s_value, True, prime, inverse)
    u_value = normalized_sum_mod(kernel_1, s_value, 2 * s_value - 1, False, prime, inverse)
    v_value = normalized_sum_mod(kernel_1, h_value, 2 * s_value - 1, True, prime, inverse)
    sign_s = -1 if s_value % 2 else 1
    sign_h = -1 if h_value % 2 else 1
    a_base = sign_s * factorial[2 * s_value] * factorial[s_value] * inverse_factorial[3 * s_value + 1] % prime
    b_base = sign_h * factorial[2 * s_value] * factorial[h_value] * inverse_factorial[2 * s_value + h_value + 1] % prime
    c_base = -sign_s * factorial[2 * s_value - 1] * factorial[s_value - 1] * inverse_factorial[3 * s_value - 1] % prime
    d_base = sign_h * factorial[2 * s_value - 1] * factorial[h_value] * inverse_factorial[2 * s_value + h_value] % prime
    return (
        (2 * a_base * x_value - b_base * y_value) % prime,
        (2 * c_base * u_value - d_base * v_value) % prime,
    )


def uhat(
    prime: int, h_value: int, s_value: int, t_value: int
) -> Fraction:
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    r_value = 2 * h_value
    answer = Fraction(0)
    for degree, coefficient in enumerate(w_polynomial(h_value, s_value)):
        denominator = prime + r_value + t_value + degree + 1
        if denominator % prime:
            answer += Fraction(
                coefficient * ell_value(denominator - 1, epsilon), denominator
            )
    return answer


def full_u(
    prime: int, h_value: int, s_value: int, t_value: int
) -> Fraction:
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    r_value = 2 * h_value
    return sum(
        (
            Fraction(
                coefficient
                * ell_value(prime + r_value + t_value + degree, epsilon),
                prime + r_value + t_value + degree + 1,
            )
            for degree, coefficient in enumerate(w_polynomial(h_value, s_value))
        ),
        Fraction(0),
    )


def v_digit(prime: int, h_value: int, s_value: int, t_value: int) -> int:
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    r_value = 2 * h_value
    answer = 0
    for degree, coefficient in enumerate(w_polynomial(h_value, s_value)):
        denominator = prime + r_value + t_value + degree + 1
        if denominator % prime:
            answer += (
                coefficient
                * ell_value(denominator - 1, epsilon)
                * pow(denominator, -2, prime)
            )
    return answer % prime


def terminal_replay(prime: int, h_value: int, s_value: int) -> dict:
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    r_value = 2 * h_value
    checked = 0
    multiplicities = []
    for a_value in range(2, 6):
        t_value = 2 * s_value + 1 + (a_value - 2) * prime
        a_coefficient = prime + 2 * r_value + 4 * s_value + t_value + 2
        b_coefficient = prime + r_value + t_value + 1
        c_coefficient = prime + 2 * r_value + t_value + 2
        d_coefficient = prime + r_value + 4 * s_value + t_value + 1
        if a_coefficient != a_value * prime:
            raise AssertionError((prime, a_value, a_coefficient))
        lhs = (
            b_coefficient * uhat(prime, h_value, s_value, t_value)
            - c_coefficient * uhat(prime, h_value, s_value, t_value + 1)
            + d_coefficient * uhat(prime, h_value, s_value, t_value + 2)
            - a_coefficient * uhat(prime, h_value, s_value, t_value + 3)
        )
        source = ell_value(a_value * prime - 1, epsilon)
        if lhs != source:
            raise AssertionError((prime, h_value, s_value, a_value, lhs, source))
        quotient = (
            b_coefficient * uhat(prime, h_value, s_value, t_value)
            - c_coefficient * uhat(prime, h_value, s_value, t_value + 1)
            + d_coefficient * uhat(prime, h_value, s_value, t_value + 2)
            - source
        ) / prime
        if quotient != a_value * uhat(prime, h_value, s_value, t_value + 3):
            raise AssertionError((prime, h_value, s_value, a_value, "quotient"))
        pole_digit = fraction_mod(prime * full_u(prime, h_value, s_value, t_value + 3), prime)
        if pole_digit != source * pow(a_value, -1, prime) % prime:
            raise AssertionError((prime, a_value, pole_digit, source))
        multiplicities.append([a_value, source, pole_digit])
        checked += 1

    antiperiod_checks = 0
    for t_value in range(0, 2 * s_value + 7):
        value = (
            uhat(prime, h_value, s_value, t_value + 2 * prime)
            + uhat(prime, h_value, s_value, t_value)
            - 2 * prime * v_digit(prime, h_value, s_value, t_value)
        )
        if fraction_mod(value, prime * prime):
            raise AssertionError((prime, h_value, s_value, t_value, "2p carry"))
        value = (
            uhat(prime, h_value, s_value, t_value + 4 * prime)
            - uhat(prime, h_value, s_value, t_value)
            + 4 * prime * v_digit(prime, h_value, s_value, t_value)
        )
        if fraction_mod(value, prime * prime):
            raise AssertionError((prime, h_value, s_value, t_value, "4p carry"))
        antiperiod_checks += 2

    # The exact initial endpoint moments are the displayed combinations.
    poly_zero = p_polynomial(prime, h_value, s_value, 0)
    poly_one = p_polynomial(prime, h_value, s_value, 1)
    moment_zero = exact_moment(poly_zero, prime + r_value, epsilon)
    moment_one = exact_moment(poly_one, prime + r_value, epsilon)
    initial = [uhat(prime, h_value, s_value, index) for index in range(5)]
    if moment_zero != initial[0] + initial[1] + initial[2] + initial[3]:
        raise AssertionError((prime, "initial M0"))
    if moment_one != initial[0] + 4 * initial[1] + 6 * initial[2] + 4 * initial[3] + initial[4]:
        raise AssertionError((prime, "initial M1"))
    return {
        "row": [prime, h_value, s_value],
        "terminal_multiplicities": multiplicities,
        "terminal_checks": checked,
        "antiperiod_checks": antiperiod_checks,
    }


def row_digest(rows: list[list[int]]) -> str:
    payload = "".join(
        ",".join(str(value) for value in row) + "\n" for row in rows
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def build_certificate(direct_limit: int, census_limit: int) -> dict:
    dependency_hashes = {
        name: sha256_file(resolve_dependency(name)) for name in DEPENDENCIES
    }
    if dependency_hashes != DEPENDENCIES:
        raise AssertionError((dependency_hashes, DEPENDENCIES))

    direct_rows = 0
    direct_coordinates = 0
    direct_gate_records: list[list[int]] = []
    for prime, h_value, s_value in rows_upto(direct_limit):
        q_pair = q_pair_fast(prime, h_value, s_value)
        for nu in (0, 1):
            q_exact, reflection, moment, hermite, h_one = q_r_m_j(
                prime, h_value, s_value, nu
            )
            if fraction_mod(q_exact, prime) != q_pair[nu]:
                raise AssertionError((prime, h_value, s_value, nu, "Q replay"))
            e_value = e_digit(prime, h_value, s_value, nu)
            m_value = 3 * h_value + 4 * s_value + 2
            coefficient = original_coefficient(m_value, nu)
            if coefficient % prime:
                raise AssertionError((prime, h_value, s_value, nu, "rank zero"))
            rhs = 6 * q_exact + prime * (12 * reflection + e_value)
            if coefficient // prime % (prime * prime) != fraction_mod(rhs, prime * prime):
                raise AssertionError((prime, h_value, s_value, nu, "Witt quotient"))
            if q_pair[nu] == 0:
                if fraction_mod(moment, prime):
                    raise AssertionError((prime, h_value, s_value, nu, "M gate"))
                omega = (
                    6 * divided_fraction_mod(q_exact, prime)
                    + 12 * fraction_mod(reflection, prime)
                    + e_value
                ) % prime
                endpoint_omega = (
                    -6
                    * (-1 if ((prime - 1) // 2) % 2 else 1)
                    * divided_fraction_mod(moment, prime)
                    + 6 * fraction_mod(hermite, prime)
                    + e_value
                ) % prime
                if omega != endpoint_omega:
                    raise AssertionError((prime, h_value, s_value, nu, "Omega forms"))
                if coefficient % (prime * prime):
                    raise AssertionError((prime, h_value, s_value, nu, "first gate"))
                if coefficient // (prime * prime) % prime != omega:
                    raise AssertionError((prime, h_value, s_value, nu, "Omega direct"))
                direct_gate_records.append(
                    [prime, h_value, s_value, nu, omega, divided_fraction_mod(moment, prime)]
                )
            direct_coordinates += 1
        direct_rows += 1

    gate_records: list[list[int]] = []
    row_count = 0
    zero_counts = [0, 0]
    joint_count = 0
    for prime, h_value, s_value in rows_upto(census_limit):
        q_pair = q_pair_fast(prime, h_value, s_value)
        row_count += 1
        if q_pair == (0, 0):
            joint_count += 1
        for nu in (0, 1):
            if q_pair[nu]:
                continue
            zero_counts[nu] += 1
            q_mod_p2 = q_mod_direct(prime, h_value, s_value, nu, prime * prime)
            if q_mod_p2 % prime:
                raise AssertionError((prime, h_value, s_value, nu, "gate mod p2"))
            reflection = r_mod_direct(prime, h_value, s_value, nu)
            e_value = e_digit(prime, h_value, s_value, nu)
            omega = (6 * (q_mod_p2 // prime) + 12 * reflection + e_value) % prime
            moment_mod_p2, hermite = moment_j_mod(prime, h_value, s_value, nu)
            if moment_mod_p2 % prime:
                raise AssertionError((prime, h_value, s_value, nu, "endpoint gate"))
            moment_digit = moment_mod_p2 // prime
            endpoint_omega = (
                -6
                * (-1 if ((prime - 1) // 2) % 2 else 1)
                * moment_digit
                + 6 * hermite
                + e_value
            ) % prime
            if endpoint_omega != omega:
                raise AssertionError((prime, h_value, s_value, nu, "endpoint Omega census"))
            xi_value = (6 * hermite + e_value) % prime
            gate_records.append(
                [prime, h_value, s_value, nu, omega, moment_digit, xi_value]
            )

    # Omega is coordinate 4; the last coordinate is Xi, not the second digit.
    second_zero_count = sum(row[4] == 0 for row in gate_records)
    endpoint_extra_count = sum(row[5] == 0 for row in gate_records)
    endpoint_and_coefficient_extra_count = sum(
        row[4] == 0 and row[5] == 0 for row in gate_records
    )
    if direct_limit == 151:
        if direct_rows != 184 or direct_coordinates != 368:
            raise AssertionError((direct_rows, direct_coordinates))
    if census_limit == 2000:
        if (row_count, zero_counts, joint_count, len(gate_records), second_zero_count) != (
            22934,
            [20, 26],
            0,
            46,
            0,
        ):
            raise AssertionError((row_count, zero_counts, joint_count, len(gate_records), second_zero_count))

    terminal_rows = [
        terminal_replay(13, 1, 1),
        terminal_replay(29, 5, 1),
        terminal_replay(109, 10, 11),
    ]

    return {
        "item": 234,
        "title": "first p^2/Witt lift of the corrected j=1 common-log terminal system",
        "parameters": {
            "row": "p=4h+6s+3=2r+6s+3, r=2h, h,s>=1",
            "direct_integer_rational_limit": direct_limit,
            "finite_census_limit": census_limit,
        },
        "proved": {
            "witt_expansion": (
                "C_nu/p = [z^N](L(A,B)+pK(A,B))P_nu mod p^2, "
                "K=6U^2V^-5(VA-UB)^2"
            ),
            "harmonic_digits": (
                "A=A0+pA1 and B=B0+pB1 mod p^2 with the stated harmonic coefficients"
            ),
            "reflection_carry": "H1_nu=Q_nu+2pR_nu exactly",
            "unreduced_moment_carry": "H1_nu=-epsilon*M_nu+pJ_nu exactly",
            "second_digit": (
                "on Q_nu=0 mod p, Omega_nu=C_nu/p^2="
                "6(Q_nu/p)+12R_nu+E_nu="
                "-6epsilon(M_nu/p)+6J_nu+E_nu mod p"
            ),
            "terminal_multiplicity": (
                "at t_a=2s+1+(a-2)p, A_t=a p and the retained source is ell_(ap-1)"
            ),
            "squared_denominator_carry": (
                "uhat_(t+2p)+uhat_t=2p v_t mod p^2 and "
                "uhat_(t+4p)-uhat_t=-4p v_t mod p^2"
            ),
            "scoped_terminal_no_go": (
                "after first-digit terminal compatibility, division by p gives "
                "a*uhat_(t+3); since a is a unit, one lifted terminal determines "
                "the free post-terminal digit and supplies no new compatibility"
            ),
        },
        "exact_replay": {
            "direct_rows": direct_rows,
            "direct_coordinates": direct_coordinates,
            "direct_gate_records": direct_gate_records,
            "terminal_rows": terminal_rows,
        },
        "exact_finite_only": {
            "rows": row_count,
            "coordinate_zero_counts": zero_counts,
            "joint_first_digit_zeros": joint_count,
            "individual_first_digit_zero_records": len(gate_records),
            "individual_second_digit_zeros": second_zero_count,
            "individual_endpoint_moment_extra_digit_zeros": endpoint_extra_count,
            "endpoint_and_coefficient_extra_digit_zeros": endpoint_and_coefficient_extra_count,
            "gate_record_schema": [
                "p", "h", "s", "nu", "Omega", "M_over_p", "Xi=6J+E"
            ],
            "gate_record_stream_sha256": row_digest(gate_records),
            "gate_records": gate_records,
        },
        "open": [
            "existence or exclusion of a simultaneous first-digit common-log row in all rows",
            "all-row nonvanishing of the two Omega coordinates on a hypothetical common row",
            "closure or arithmetic control of the squared-denominator v_t coordinate",
            "any positive Route-1 mass/rate consequence",
        ],
        "scope": (
            "Omega is a necessary per-coordinate second-digit invariant and is not claimed "
            "to prove an all-row common-log exclusion; finite nonoccurrence is evidence only"
        ),
        "dependencies": dependency_hashes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--direct-limit", type=int, default=151)
    parser.add_argument("--census-limit", type=int, default=2000)
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.direct_limit, arguments.census_limit)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "output": str(arguments.output),
        "direct_rows": certificate["exact_replay"]["direct_rows"],
        "census_rows": certificate["exact_finite_only"]["rows"],
        "gate_records": certificate["exact_finite_only"]["individual_first_digit_zero_records"],
        "second_digit_zeros": certificate["exact_finite_only"]["individual_second_digit_zeros"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
