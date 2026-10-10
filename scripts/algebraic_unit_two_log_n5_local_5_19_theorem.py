#!/usr/bin/env python3
"""Finite-state exact certificate for the 5- and 19-parts of c_d.

The companion proof explains why the checked states are periodic for every
degree.  This script deliberately makes no claim about primes other than
5 and 19.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


Pair = tuple[int, int]
Truncated = tuple[int, int, int, int]


def pair_add(a: Pair, b: Pair, modulus: int) -> Pair:
    return (a[0] + b[0]) % modulus, (a[1] + b[1]) % modulus


def pair_scale(scalar: int, a: Pair, modulus: int) -> Pair:
    return scalar * a[0] % modulus, scalar * a[1] % modulus


def pair_multiply(a: Pair, b: Pair, s: int, modulus: int) -> Pair:
    """Multiply in (Z/modulus)[X]/(X^2-X+s)."""

    a0, a1 = a
    b0, b1 = b
    return (
        (a0 * b0 - s * a1 * b1) % modulus,
        (a0 * b1 + a1 * b0 + a1 * b1) % modulus,
    )


def pair_multiply_x(a: Pair, s: int, modulus: int) -> Pair:
    return -s * a[1] % modulus, (a[0] + a[1]) % modulus


def pair_multiply_one_minus_x(a: Pair, s: int, modulus: int) -> Pair:
    return (a[0] + s * a[1]) % modulus, -a[0] % modulus


def pair_order_of_x(s: int, modulus: int) -> int:
    value = (1, 0)
    for exponent in range(1, 100000):
        value = pair_multiply_x(value, s, modulus)
        if value == (1, 0):
            return exponent
    raise AssertionError("order search bound was too small")


def pair_order_of_one_minus_x(s: int, modulus: int) -> int:
    value = (1, 0)
    for exponent in range(1, 100000):
        value = pair_multiply_one_minus_x(value, s, modulus)
        if value == (1, 0):
            return exponent
    raise AssertionError("order search bound was too small")


def scan_19() -> dict:
    p = 19
    modulus = p * p

    # The Hensel lift of t=4 mod 19 satisfying t^2+t-1=0 is t=42 mod 361.
    t = 42
    if (t * t + t - 1) % modulus:
        raise AssertionError("incorrect Hensel lift of t")
    s = pow(t + 2, -1, modulus)
    if s != 320 or (s * s - 3 * s + 1) % modulus:
        raise AssertionError("incorrect value of eta*(1-eta)")

    order_x = pair_order_of_x(s, modulus)
    order_y = pair_order_of_one_minus_x(s, modulus)
    if (order_x, order_y) != (1710, 1710):
        raise AssertionError("unexpected local unit orders")
    period = math.lcm(modulus, order_x, order_y)
    if period != 32490:
        raise AssertionError("unexpected period")

    one = (1, 0)
    x_power = y_power = one
    p_x = p_y = one
    c_x = c_y = (0, 0)
    a_value = 1  # a_0=P_0(1)
    top_c = 0
    p_hits: list[int] = []
    d_lifts: list[int] = []

    for d in range(1, period + 1):
        x_power = pair_multiply_x(x_power, s, modulus)
        y_power = pair_multiply_one_minus_x(y_power, s, modulus)
        p_x = pair_add(x_power, pair_scale(-d, p_x, modulus), modulus)
        p_y = pair_add(y_power, pair_scale(-d, p_y, modulus), modulus)

        # If C_d=d! B_d and c_d=[X^d]C_d, then
        # c_d=c_(d-1)+P_(d-1)(1) and
        # C_d(X)=-d C_(d-1)(X)+c_d X^d.
        top_c = (top_c + a_value) % modulus
        a_value = (1 - d * a_value) % modulus
        c_x = pair_add(
            pair_scale(-d, c_x, modulus),
            pair_scale(top_c, x_power, modulus),
            modulus,
        )
        c_y = pair_add(
            pair_scale(-d, c_y, modulus),
            pair_scale(top_c, y_power, modulus),
            modulus,
        )

        p_x_divisible = p_x[0] % p == 0 and p_x[1] % p == 0
        p_y_divisible = p_y[0] % p == 0 and p_y[1] % p == 0
        if p_x_divisible != p_y_divisible:
            raise AssertionError("the two conjugate P-values disagree")
        if p_x_divisible:
            p_hits.append(d)
            if p_x == (0, 0) or p_y == (0, 0):
                raise AssertionError("a P-value acquired 19-adic valuation >1")
            if a_value % p != 4:
                raise AssertionError("P_d(1) was not a 19-adic unit")
            determinant = pair_add(
                pair_multiply(p_x, c_y, s, modulus),
                pair_scale(-1, pair_multiply(p_y, c_x, s, modulus), modulus),
                modulus,
            )
            if determinant == (0, 0):
                d_lifts.append(d)

    if len(p_hits) != period // p or {d % p for d in p_hits} != {15}:
        raise AssertionError("incorrect mod-19 zero class for P_d")
    if len(d_lifts) != period // modulus or {
        d % modulus for d in d_lifts
    } != {205}:
        raise AssertionError("incorrect mod-361 lift class for the determinant")

    # The P-state and the powers return exactly.  C and its leading
    # coefficient return shifted by 95*P.  This shift leaves
    # P(x)C(y)-P(y)C(x) unchanged, proving periodicity beyond the scan.
    endpoint = {
        "x_power": x_power,
        "y_power": y_power,
        "P_x": p_x,
        "P_y": p_y,
        "C_x": c_x,
        "C_y": c_y,
        "P_at_1": a_value,
        "top_C_coefficient": top_c,
    }
    expected_endpoint = {
        "x_power": one,
        "y_power": one,
        "P_x": one,
        "P_y": one,
        "C_x": (95, 0),
        "C_y": (95, 0),
        "P_at_1": 1,
        "top_C_coefficient": 95,
    }
    if endpoint != expected_endpoint:
        raise AssertionError(f"period endpoint mismatch: {endpoint}")

    # At the conjugate prime t=14 mod 19 (the second root of
    # t^2+t-1), P_d(eta) is never zero.  Its complete period is 855.
    conjugate_s = pow(14 + 2, -1, p)
    if conjugate_s != 6:
        raise AssertionError("incorrect conjugate value of s")
    conjugate_period = math.lcm(
        p,
        pair_order_of_x(conjugate_s, p),
        pair_order_of_one_minus_x(conjugate_s, p),
    )
    if conjugate_period != 855:
        raise AssertionError("unexpected conjugate-prime period")
    power = value = one
    for d in range(1, conjugate_period + 1):
        power = pair_multiply_x(power, conjugate_s, p)
        value = pair_add(power, pair_scale(-d, value, p), p)
        if value == (0, 0):
            raise AssertionError("P_d vanished at the conjugate prime")
    if power != one or value != one:
        raise AssertionError("conjugate-prime state did not return")

    return {
        "hensel_t_mod_19_squared": t,
        "s_mod_19_squared": s,
        "period": period,
        "orders_of_eta_and_one_minus_eta": [order_x, order_y],
        "P_zero_class_mod_19": 15,
        "P_values_have_exact_local_valuation_one": True,
        "determinant_second_order_class_mod_19_squared": 205,
        "period_hit_counts": {
            "P_zero_degrees": len(p_hits),
            "second_order_determinant_degrees": len(d_lifts),
        },
        "endpoint_shift_C_by_multiple_of_P": 95,
        "conjugate_prime_period": conjugate_period,
        "conjugate_prime_has_no_P_zeros": True,
        "content_exponent": (
            "[d=15 mod 19]+[d=205 mod 361] for the principal ideal "
            "(4-t) O_K"
        ),
    }


def truncated_add(a: Truncated, b: Truncated) -> Truncated:
    return tuple((a[j] + b[j]) % 5 for j in range(4))  # type: ignore[return-value]


def truncated_scale(scalar: int, a: Truncated) -> Truncated:
    return tuple(scalar * value % 5 for value in a)  # type: ignore[return-value]


def truncated_multiply(a: Truncated, b: Truncated) -> Truncated:
    answer = [0] * 4
    for j, aj in enumerate(a):
        for k, bk in enumerate(b):
            if j + k < 4:
                answer[j + k] = (answer[j + k] + aj * bk) % 5
    return tuple(answer)  # type: ignore[return-value]


def truncated_inverse(a: Truncated) -> Truncated:
    if a[0] % 5 == 0:
        raise ValueError("constant coefficient is not a unit")
    answer = [0] * 4
    answer[0] = pow(a[0], -1, 5)
    for degree in range(1, 4):
        answer[degree] = (
            -answer[0]
            * sum(a[j] * answer[degree - j] for j in range(1, degree + 1))
        ) % 5
    return tuple(answer)  # type: ignore[return-value]


def truncated_valuation(a: Truncated) -> int:
    return next((j for j, value in enumerate(a) if value), 4)


def truncated_order(a: Truncated) -> int:
    one: Truncated = (1, 0, 0, 0)
    value = one
    for exponent in range(1, 101):
        value = truncated_multiply(value, a)
        if value == one:
            return exponent
    raise AssertionError("truncated unit order was too large")


def scan_5() -> dict:
    # Work in F_5[pi]/(pi^4), pi=zeta_5-1.  Since
    # eta=(2+pi)^-1, all operations are explicit truncated convolutions.
    one: Truncated = (1, 0, 0, 0)
    eta = truncated_inverse((2, 1, 0, 0))
    eta_bar = truncated_add(one, truncated_scale(-1, eta))
    if eta != (3, 1, 2, 4) or eta_bar != (3, 4, 3, 1):
        raise AssertionError("incorrect local expansions of eta")
    if (truncated_order(eta), truncated_order(eta_bar)) != (20, 20):
        raise AssertionError("unexpected local unit orders at 5")

    period = 20
    x_power = y_power = one
    p_x = p_y = one
    c_x = c_y = (0, 0, 0, 0)
    a_value = 1
    top_c = 0
    hits: list[int] = []
    for d in range(1, period + 1):
        x_power = truncated_multiply(x_power, eta)
        y_power = truncated_multiply(y_power, eta_bar)
        p_x = truncated_add(x_power, truncated_scale(-d, p_x))
        p_y = truncated_add(y_power, truncated_scale(-d, p_y))
        top_c = (top_c + a_value) % 5
        a_value = (1 - d * a_value) % 5
        c_x = truncated_add(
            truncated_scale(-d, c_x), truncated_scale(top_c, x_power)
        )
        c_y = truncated_add(
            truncated_scale(-d, c_y), truncated_scale(top_c, y_power)
        )
        if truncated_valuation(p_x) > 0:
            hits.append(d)
            if (
                truncated_valuation(p_x),
                truncated_valuation(p_y),
                a_value,
            ) != (1, 1, 1):
                raise AssertionError("incorrect simple zero at 5")
            determinant = truncated_add(
                truncated_multiply(p_x, c_y),
                truncated_scale(-1, truncated_multiply(p_y, c_x)),
            )
            if truncated_valuation(determinant) != 1:
                raise AssertionError("incorrect determinant valuation at 5")
        elif truncated_valuation(p_y) > 0:
            raise AssertionError("the conjugate P-values disagree at 5")

    if hits != [2, 7, 12, 17]:
        raise AssertionError(f"incorrect mod-5 zero degrees: {hits}")
    endpoint = (x_power, y_power, p_x, p_y, c_x, c_y, a_value, top_c)
    expected = (one, one, one, one, one, one, 1, 1)
    if endpoint != expected:
        raise AssertionError(f"period endpoint mismatch at 5: {endpoint}")

    return {
        "local_ring": "F_5[pi]/(pi^4), pi=zeta_5-1",
        "period": period,
        "orders_of_eta_and_one_minus_eta": [20, 20],
        "P_zero_class_mod_5": 2,
        "P_values_have_exact_pi_valuation_one": True,
        "determinant_has_exact_pi_valuation_one": True,
        "endpoint_shift_C_by_multiple_of_P": 1,
        "content_exponent": "[d=2 mod 5] for the principal ideal (2-t) O_K",
    }


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    script = Path(__file__).resolve()
    result = {
        "description": (
            "Exact finite-state all-degree classification of the local 5- and "
            "19-parts of the n=5 two-log content ideal."
        ),
        "prime_5": scan_5(),
        "prime_19": scan_19(),
        "combined_local_formula": (
            "(2-t)^[d=2 mod 5] and "
            "(4-t)^([d=15 mod 19]+[d=205 mod 361]); "
            "no assertion is made at any other prime"
        ),
        "script_sha256": file_sha256(script),
        "scope_warning": (
            "This theorem is local at 5 and 19.  It neither excludes content "
            "at later primes nor proves a global subexponential content bound."
        ),
    }
    output = Path("results/algebraic_unit_two_log_n5_local_5_19_theorem.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
