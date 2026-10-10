"""Exact audit of the relative-endpoint first-lift identity.

The theorem is algebraic.  This script only replays the sharp mixed-cubic
row (m,p)=(6,7) over Q and modulo 7, using an independent Hermite reduction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


P = 7


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(
    left: list[Fraction],
    right: list[Fraction],
    scale: Fraction = Fraction(1),
) -> list[Fraction]:
    out = [Fraction()] * max(len(left), len(right))
    for j, value in enumerate(left):
        out[j] += value
    for j, value in enumerate(right):
        out[j] += scale * value
    return trim(out)


def mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction()] * (len(left) + len(right) - 1)
    for j, a in enumerate(left):
        for k, b in enumerate(right):
            out[j + k] += a * b
    return trim(out)


def power(poly: list[Fraction], exponent: int) -> list[Fraction]:
    out = [Fraction(1)]
    base = poly[:]
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        exponent >>= 1
        if exponent:
            base = mul(base, base)
    return out


def derivative(poly: list[Fraction]) -> list[Fraction]:
    return [Fraction(j) * poly[j] for j in range(1, len(poly))] or [Fraction()]


def integral_without_constant(poly: list[Fraction]) -> list[Fraction]:
    return [Fraction()] + [value / Fraction(j + 1) for j, value in enumerate(poly)]


def evaluate(poly: list[Fraction], value: Fraction) -> Fraction:
    out = Fraction()
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


Q = [Fraction(1), Fraction(1), Fraction(1), Fraction(1)]
Q_PRIME = derivative(Q)
Q_PRIME_INVERSE_MOD_Q = [Fraction(), Fraction(-1, 4), Fraction(1, 4)]
U = [Fraction(), Fraction(1), Fraction(-1)]


def divmod_q(poly: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    remainder = poly[:]
    quotient = [Fraction()] * max(1, len(remainder) - 3)
    while len(remainder) >= 4:
        shift = len(remainder) - 4
        leading = remainder[-1]
        quotient[shift] = leading
        for j in range(4):
            remainder[shift + j] -= leading
        trim(remainder)
    return trim(quotient), trim(remainder)


def remainder_mod_q(poly: list[Fraction]) -> list[Fraction]:
    return divmod_q(poly)[1]


def mixed_coordinates(
    numerator: list[Fraction], denominator_power: int
) -> tuple[Fraction, Fraction, Fraction]:
    """Coordinates of numerator/Q**denominator_power dx."""
    current = numerator[:]
    rational = Fraction()
    for level in range(denominator_power, 1, -1):
        reduced = remainder_mod_q(current)
        primitive = remainder_mod_q(mul(reduced, Q_PRIME_INVERSE_MOD_Q))
        primitive = [-value / Fraction(level - 1) for value in primitive]
        lowered = add(current, mul(derivative(primitive), Q), Fraction(-1))
        lowered = add(lowered, mul(primitive, Q_PRIME), Fraction(level - 1))
        current, remainder = divmod_q(lowered)
        assert remainder == [0]
        rational += evaluate(primitive, Fraction(1)) / 4 ** (level - 1)
        rational -= evaluate(primitive, Fraction())

    polynomial_part, remainder = divmod_q(current)
    rational += sum(
        (
            coefficient / Fraction(j + 1)
            for j, coefficient in enumerate(polynomial_part)
        ),
        Fraction(),
    )
    remainder += [Fraction()] * (3 - len(remainder))
    a, b, c = remainder[:3]
    return rational, a - b + 3 * c, a + b - c


def mod_fraction(value: Fraction, prime: int = P) -> int:
    assert value.denominator % prime
    return (value.numerator % prime) * pow(value.denominator, -1, prime) % prime


def valuation(value: Fraction, prime: int = P) -> int:
    def integer_valuation(integer: int) -> int:
        if integer == 0:
            return 10**9
        count = 0
        integer = abs(integer)
        while integer % prime == 0:
            integer //= prime
            count += 1
        return count

    return integer_valuation(value.numerator) - integer_valuation(value.denominator)


def primes_through(bound: int) -> list[int]:
    out: list[int] = []
    for candidate in range(2, bound + 1):
        if all(candidate % divisor for divisor in range(2, math.isqrt(candidate) + 1)):
            out.append(candidate)
    return out


def lcm_through(bound: int) -> int:
    out = 1
    for value in range(2, bound + 1):
        out = math.lcm(out, value)
    return out


def cartier_degree(n_value: int, k_value: int, prime: int) -> int:
    r_value = n_value % prime
    t_value = k_value % prime
    return 2 * r_value if t_value == 0 else 2 * r_value + 3 * (prime - t_value)


def run() -> dict[str, object]:
    m = 6
    n = 6 * m
    k0 = 4 * m + 1
    k1 = k0 + 1
    a = n // P
    r = n % P
    h = k0 // P + 1
    t = k0 % P

    p0 = mul(power(U, r), power(Q, P - t))
    p1 = mul(power(U, r), power(Q, P - t - 1))
    gamma0 = p0[P - 1]
    gamma1 = p1[P - 1] if len(p1) > P - 1 else Fraction()
    assert gamma0.denominator == gamma1.denominator == 1

    theta = add(
        [gamma1 * value for value in p0],
        [gamma0 * value for value in p1],
        Fraction(-1),
    )
    theta += [Fraction()] * max(0, P - len(theta))
    assert theta[P - 1] == 0
    primitive_t = integral_without_constant(theta)
    assert derivative(primitive_t) == trim(theta[:])

    omega0 = mixed_coordinates(power(U, n), k0)
    omega1 = mixed_coordinates(power(U, n), k1)
    f_coordinates = mixed_coordinates(power(U, a), h)

    # eta = F^(p-1) F' T dx
    #     = u^(ap-1) (a u'Q-huQ') T / Q^(hp+1) dx.
    logarithmic_numerator = add(
        mul(derivative(U), Q),
        mul(U, Q_PRIME),
        Fraction(-h, a),
    )
    logarithmic_numerator = [Fraction(a) * value for value in logarithmic_numerator]
    eta_numerator = mul(
        mul(power(U, a * P - 1), logarithmic_numerator), primitive_t
    )
    eta_coordinates = mixed_coordinates(eta_numerator, h * P + 1)

    r0, l0, e0 = omega0
    r1, l1, e1 = omega1
    a_form = l1 * r0 - l0 * r1
    b_form = (l1 * e0 - l0 * e1) / 8
    determinant = l1 * (P * r0) - l0 * (P * r1)
    assert determinant == P * a_form
    assert valuation(determinant) == 1
    assert valuation(a_form) == 0

    middle_product = math.prod(
        prime
        for prime in primes_through(3 * m - 1)
        if 2 * m < prime < 3 * m
    )
    clearing = 2 ** (9 * m + 5) * lcm_through(k0) // middle_product
    cartier_product = math.prod(
        prime
        for prime in primes_through(n)
        if prime != 2
        and cartier_degree(n, k0, prime) <= prime - 2
        and cartier_degree(n, k1, prime) <= prime - 2
    )
    u_value = clearing * a_form / cartier_product
    v_value = clearing * b_form / cartier_product
    assert u_value.denominator == v_value.denominator == 1
    content = math.gcd(abs(u_value.numerator), abs(v_value.numerator))
    assert valuation(u_value) == 1
    assert valuation(v_value) >= 2
    assert valuation(Fraction(content)) == 1

    v_x = mod_fraction(f_coordinates[0])
    v_l = mod_fraction(f_coordinates[1])
    x0 = mod_fraction(P * r0)
    x1 = mod_fraction(P * r1)
    ell0 = mod_fraction(l0)
    ell1 = mod_fraction(l1)
    assert x0 == mod_fraction(gamma0) * v_x % P
    assert x1 == mod_fraction(gamma1) * v_x % P
    assert ell0 == mod_fraction(gamma0) * v_l % P
    assert ell1 == mod_fraction(gamma1) * v_l % P

    eta_x = mod_fraction(P * eta_coordinates[0])
    eta_l = mod_fraction(eta_coordinates[1])
    boundary = evaluate(power(U, a * P), Fraction(1)) * evaluate(
        primitive_t, Fraction(1)
    ) - evaluate(power(U, a * P), Fraction()) * evaluate(
        primitive_t, Fraction()
    )
    assert boundary == 0

    predicted_digit = (-v_l * eta_x + v_x * eta_l) % P
    actual_digit = mod_fraction(determinant / P)
    assert predicted_digit == actual_digit
    assert actual_digit != 0

    return {
        "scope": "exact audit only; theorem is proved in the companion note",
        "row": {"m": m, "p": P, "N": n, "K0": k0, "K1": k1},
        "factorization": {
            "a": a,
            "r": r,
            "h": h,
            "t": t,
            "degree_P0": len(trim(p0[:])) - 1,
            "degree_P1": len(trim(p1[:])) - 1,
            "gamma0": int(gamma0),
            "gamma1": int(gamma1),
        },
        "mod_p": {
            "leading_F_vector_X_L": [v_x, v_l],
            "omega0_vector_X_L": [x0, ell0],
            "omega1_vector_X_L": [x1, ell1],
            "eta_vector_pR_L": [eta_x, eta_l],
            "boundary": int(boundary),
            "predicted_A_mod_p": predicted_digit,
            "actual_A_mod_p": actual_digit,
        },
        "valuations": {
            "v_p_pA": valuation(determinant),
            "v_p_A": valuation(a_form),
            "v_p_U": valuation(u_value),
            "v_p_V": valuation(v_value),
            "v_p_content": valuation(Fraction(content)),
        },
        "checks": {
            "P0_equals_Q_times_P1": p0 == mul(Q, p1),
            "theta_x_p_minus_1_coefficient_zero": theta[P - 1] == 0,
            "theta_equals_T_prime": derivative(primitive_t) == trim(theta[:]),
            "rank_one_relative_endpoint": True,
            "first_lift_identity": True,
            "sharp_obstruction_nonzero": actual_digit != 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "witt_endpoint_first_lift_checker.json",
    )
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_bytes(payload.encode("utf-8"))
    print(payload, end="")
    print("sha256", hashlib.sha256(payload.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
