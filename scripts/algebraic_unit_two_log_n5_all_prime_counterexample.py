#!/usr/bin/env python3
"""Exact certificate for the new n=5 prescribed-first-jet prime.

This script proves the single unconditional assertion

    109321 | N_{F/Q}(J_6219),

where F=Q(t), t^2+t-1=0, and in fact computes
N_{F/Q}(J_6219)=109321 in characteristic zero.  It also checks the
equivalent P-value, h-recurrence, weighted-factorial, and prescribed-first-
jet formulations.  The separate finite scan through p=200000 is reported
as diagnostic metadata only and is deliberately not used in the proof.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path


sys.set_int_max_str_digits(1_000_000)

EElement = tuple[int, int, int, int]
FElement = tuple[int, int]

P = 109_321
D = 6_219
M = P - 1 - D
T0 = 53_267
A0 = T0 + 2
T1 = (-1 - T0) % P
A1 = (T1 + 2) % P
ZETA0 = 85_986
ZETA0_INV = 76_602
X0 = 70_927
Y0 = 38_395
U0 = 85_987
V0 = 76_603

E_ZERO: EElement = (0, 0, 0, 0)
E_ONE: EElement = (1, 0, 0, 0)
E_ZETA: EElement = (0, 1, 0, 0)
E_ZETA_INV: EElement = (-1, -1, -1, -1)
E_T: EElement = (-1, 0, -1, -1)
E_ETA: EElement = (0, -1, 0, -1)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prime_certificate() -> dict[str, object]:
    """Lucas certificate, including an elementary proof that 911 is prime."""

    prime_divisors = (2, 3, 5, 911)
    trial_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    if math.prod((2**3, 3, 5, 911)) != P - 1:
        raise AssertionError("incorrect factorization of p-1")
    trial_remainders = {str(q): 911 % q for q in trial_primes}
    if any(value == 0 for value in trial_remainders.values()):
        raise AssertionError("911 failed trial division")

    witness = 19
    full_power = pow(witness, P - 1, P)
    quotient_powers = {
        str(q): pow(witness, (P - 1) // q, P) for q in prime_divisors
    }
    quotient_gcds = {
        q: math.gcd(value - 1, P) for q, value in quotient_powers.items()
    }
    if full_power != 1 or any(value != 1 for value in quotient_gcds.values()):
        raise AssertionError("Lucas primality certificate failed")
    return {
        "factorization_p_minus_1": "2^3 * 3 * 5 * 911",
        "prime_911_trial_division_remainders": trial_remainders,
        "lucas_witness": witness,
        "witness_power_p_minus_1_mod_p": full_power,
        "witness_quotient_powers_mod_p": quotient_powers,
        "gcd_power_minus_1_with_p": quotient_gcds,
        "conclusion": "p is prime by the Lucas primality criterion",
    }


def p_value_mod(argument: int) -> dict[str, object]:
    """Advance P_n(r)=r^n-nP_(n-1)(r) modulo P."""

    power = 1
    value = 1
    tail: dict[str, dict[str, int]] = {}
    for n in range(1, D + 1):
        power = power * argument % P
        value = (power - n * value) % P
        if n >= D - 2:
            tail[str(n)] = {"power": power, "P_value": value}

    # Independent evaluation of (-1)^d d! E_d(-r).
    factorial = 1
    term = 1
    truncated = 1
    for n in range(1, D + 1):
        factorial = factorial * n % P
        term = term * (-argument) * pow(n, -1, P) % P
        truncated = (truncated + term) % P
    direct = pow(-1, D, P) * factorial * truncated % P
    if value != 0 or direct != value:
        raise AssertionError("P-value check failed")
    return {
        "argument": argument,
        "tail": tail,
        "P_d_by_recurrence": value,
        "P_d_by_truncated_exponential": direct,
    }


def h_modular_data() -> dict[str, object]:
    """Check the real-quadratic scalar recurrence at A=A0."""

    previous_previous = 1
    previous = (1 - A0) % P
    tail = {"0": previous_previous, "1": previous}
    for n in range(2, D + 1):
        current = (
            1
            - A0 * n * previous
            - A0 * n * (n - 1) * previous_previous
        ) % P
        previous_previous, previous = previous, current
        if n >= D - 4:
            tail[str(n)] = current
    if (previous_previous, previous) != (0, 0):
        raise AssertionError("the modular h first jet did not vanish")
    return {
        "recurrence": "h_n=1-A*n*h_(n-1)-A*n*(n-1)*h_(n-2)",
        "tail": tail,
        "h_d_minus_1": previous_previous,
        "h_d": previous,
    }


def a_times_t_multiply(value: FElement) -> FElement:
    """Multiply r+s*A by A, where A^2=3A-1."""

    r, s = value
    return -s, r + 3 * s


def ideal_index_A(generators: tuple[FElement, FElement]) -> tuple[int, list[int]]:
    """Index of a two-generator ideal in Z[A], A^2=3A-1."""

    columns: list[FElement] = []
    for value in generators:
        columns.extend((value, a_times_t_multiply(value)))
    minors = [
        columns[j][0] * columns[k][1] - columns[j][1] * columns[k][0]
        for k in range(4)
        for j in range(k)
    ]
    index = 0
    for value in minors:
        index = math.gcd(index, abs(value))
    return index, minors


def h_characteristic_zero_data() -> dict[str, object]:
    """Advance h exactly in Z[A] and compute its first-jet ideal index."""

    previous_previous: FElement = (1, 0)
    previous: FElement = (1, -1)
    for n in range(2, D + 1):
        a0, b0 = a_times_t_multiply(previous_previous)
        a1, b1 = a_times_t_multiply(previous)
        current = (
            1 - n * a1 - n * (n - 1) * a0,
            -n * b1 - n * (n - 1) * b0,
        )
        previous_previous, previous = previous, current

    index, minors = ideal_index_A((previous_previous, previous))
    if index != P:
        raise AssertionError("unexpected characteristic-zero h-jet ideal index")
    coordinate_residues = [
        [value[0] % P, value[1] % P]
        for value in (previous_previous, previous)
    ]
    evaluations_at_A0 = [
        (value[0] + A0 * value[1]) % P
        for value in (previous_previous, previous)
    ]
    evaluations_at_A1 = [
        (value[0] + A1 * value[1]) % P
        for value in (previous_previous, previous)
    ]
    if evaluations_at_A0 != [0, 0] or 0 in evaluations_at_A1:
        raise AssertionError("incorrect prime selection in the h-jet ideal")
    return {
        "coordinate_residues_mod_p": coordinate_residues,
        "evaluations_at_A0": evaluations_at_A0,
        "evaluations_at_conjugate_A1": evaluations_at_A1,
        "coordinate_digit_counts": [
            [len(str(abs(value[0]))), len(str(abs(value[1])))]
            for value in (previous_previous, previous)
        ],
        "six_minor_gcd": str(index),
        "minor_digit_counts": [len(str(abs(value))) for value in minors],
    }


def weighted_first_jet_data() -> dict[str, object]:
    """Check W_m(u)=W_m(v)=0 and H(u)=H'(u)=0."""

    factorial_m = 1
    for n in range(1, M + 1):
        factorial_m = factorial_m * n % P

    def value_and_derivative(argument: int) -> tuple[int, int]:
        coefficient = factorial_m
        power = 1
        previous_power = 1
        value = coefficient
        derivative = 0
        for j in range(1, D + 1):
            coefficient = coefficient * (M + j) % P
            previous_power = power
            power = power * argument % P
            value = (value + coefficient * power) % P
            derivative = (
                derivative + j * coefficient * previous_power
            ) % P
        return value, derivative

    w_u, wp_u = value_and_derivative(U0)
    w_v, wp_v = value_and_derivative(V0)
    h_value = (w_v - ZETA0 * w_u) % P
    h_derivative = (ZETA0_INV * wp_v - ZETA0 * wp_u) % P
    expected_wp_u = -factorial_m * pow(U0, -2, P) % P
    expected_wp_v = -factorial_m * pow(V0, -2, P) % P
    if (w_u, w_v, h_value, h_derivative) != (0, 0, 0, 0):
        raise AssertionError("weighted prescribed first jet did not vanish")
    if (wp_u, wp_v) != (expected_wp_u, expected_wp_v):
        raise AssertionError("weighted differential equation check failed")
    return {
        "m": M,
        "factorial_m_mod_p": factorial_m,
        "W_m_u": w_u,
        "W_m_v": w_v,
        "W_m_prime_u": wp_u,
        "W_m_prime_v": wp_v,
        "H_m_u": h_value,
        "H_m_prime_u": h_derivative,
        "W_roots_are_simple": wp_u != 0 and wp_v != 0,
        "H_has_the_prescribed_double_root": True,
    }


def e_add(a: EElement, b: EElement) -> EElement:
    return tuple(a[j] + b[j] for j in range(4))  # type: ignore[return-value]


def e_scale(scalar: int, value: EElement) -> EElement:
    return tuple(scalar * value[j] for j in range(4))  # type: ignore[return-value]


def e_multiply(a: EElement, b: EElement) -> EElement:
    raw = [0] * 7
    for j, aj in enumerate(a):
        for k, bk in enumerate(b):
            raw[j + k] += aj * bk
    # zeta^4=-(1+zeta+zeta^2+zeta^3).
    for degree in range(6, 3, -1):
        value = raw[degree]
        if value:
            for target in range(degree - 4, degree):
                raw[target] -= value
            raw[degree] = 0
    return tuple(raw[:4])  # type: ignore[return-value]


def f_coordinates(value: EElement) -> FElement:
    """Coordinates a+b*t of a conjugation-fixed E element."""

    if value[1] != 0 or value[2] != value[3]:
        raise AssertionError("element was not in F")
    return value[0] - value[2], -value[2]


def divide_by_zeta_minus_inverse(value: EElement) -> FElement:
    """Divide an anti-invariant integral element by zeta-zeta^-1."""

    delta = e_add(E_ZETA, e_scale(-1, E_ZETA_INV))
    delta_t = e_multiply(delta, E_T)
    if value[1] % 2:
        raise AssertionError("anti-invariant coordinate was not divisible by 2")
    a = value[1] // 2
    b = value[2] - a
    if e_add(e_scale(a, delta), e_scale(b, delta_t)) != value:
        raise AssertionError("division by zeta-zeta^-1 failed")
    return a, b


def ideal_index_t(
    first: FElement, second: FElement
) -> tuple[int, list[int], list[int]]:
    """Index of (first,second) in Z[t], t^2+t-1=0."""

    a, b = first
    c, d = second
    # Columns are first, t*first, second, t*second.
    columns = [(a, b), (b, a - b), (c, d), (d, c - d)]
    minors = [
        columns[j][0] * columns[k][1] - columns[j][1] * columns[k][0]
        for k in range(4)
        for j in range(k)
    ]
    entry_gcd = 0
    for column in columns:
        entry_gcd = math.gcd(entry_gcd, abs(column[0]))
        entry_gcd = math.gcd(entry_gcd, abs(column[1]))
    index = 0
    for value in minors:
        index = math.gcd(index, abs(value))
    if entry_gcd == 0 or index % entry_gcd:
        raise AssertionError("invalid Smith data")
    return index, [entry_gcd, index // entry_gcd], minors


def characteristic_zero_J_data() -> dict[str, object]:
    """Reconstruct N_d and a_d*T_d exactly and compute the ideal norm."""

    eta_bar = e_add(E_ONE, e_scale(-1, E_ETA))
    x_power = E_ONE
    y_power = E_ONE
    p_x = E_ONE
    p_y = E_ONE
    c_x = E_ZERO
    c_y = E_ZERO
    a_value = 1
    top_c = 0

    for n in range(1, D + 1):
        x_power = e_multiply(x_power, E_ETA)
        y_power = e_multiply(y_power, eta_bar)
        p_x = e_add(x_power, e_scale(-n, p_x))
        p_y = e_add(y_power, e_scale(-n, p_y))
        top_c += a_value
        a_value = 1 - n * a_value
        c_x = e_add(e_scale(-n, c_x), e_scale(top_c, x_power))
        c_y = e_add(e_scale(-n, c_y), e_scale(top_c, y_power))

    n_value = f_coordinates(e_multiply(p_x, p_y))
    determinant = e_add(
        e_multiply(p_x, c_y), e_scale(-1, e_multiply(p_y, c_x))
    )
    t_value = divide_by_zeta_minus_inverse(determinant)
    a_times_t = (a_value * t_value[0], a_value * t_value[1])
    index, smith_diagonal, minors = ideal_index_t(n_value, a_times_t)
    if index != P or smith_diagonal != [1, P]:
        raise AssertionError("unexpected characteristic-zero J ideal norm")

    n_mod_p = [n_value[0] % P, n_value[1] % P]
    at_mod_p = [a_times_t[0] % P, a_times_t[1] % P]
    expected_n_mod_p = [41_140, 3_246]
    expected_at_mod_p = [938, 103_634]
    if n_mod_p != expected_n_mod_p or at_mod_p != expected_at_mod_p:
        raise AssertionError("unexpected F-coordinate residues")
    at_t0 = [
        (n_mod_p[0] + T0 * n_mod_p[1]) % P,
        (at_mod_p[0] + T0 * at_mod_p[1]) % P,
    ]
    at_t1 = [
        (n_mod_p[0] + T1 * n_mod_p[1]) % P,
        (at_mod_p[0] + T1 * at_mod_p[1]) % P,
    ]
    if at_t0 != [0, 0] or 0 in at_t1:
        raise AssertionError("J selected the wrong prime over p")

    full_payload = json.dumps(
        {
            "d": D,
            "N": [str(value) for value in n_value],
            "aT": [str(value) for value in a_times_t],
            "minors": [str(value) for value in minors],
        },
        separators=(",", ":"),
    )
    payload_hash = hashlib.sha256(full_payload.encode()).hexdigest()
    expected_hash = "ea79ca6c41ed1580a41327f405b9bf1805fcf70a1ec4998538a6bdfffc5abb2a"
    if payload_hash != expected_hash:
        raise AssertionError("characteristic-zero payload hash changed")
    return {
        "N_coordinates_mod_p": n_mod_p,
        "a_d_T_d_coordinates_mod_p": at_mod_p,
        "values_at_t0": at_t0,
        "values_at_conjugate_t1": at_t1,
        "N_mod_p_factorization": "3246*(t-53267)",
        "a_d_T_d_mod_p_factorization": "103634*(t-53267)",
        "a_d_mod_p": a_value % P,
        "coordinate_digit_counts": [
            len(str(abs(value))) for value in n_value + a_times_t
        ],
        "coordinate_signs": [
            1 if value >= 0 else -1 for value in n_value + a_times_t
        ],
        "six_minor_digit_counts": [len(str(abs(value))) for value in minors],
        "six_minor_signs": [1 if value >= 0 else -1 for value in minors],
        "smith_diagonal": [str(value) for value in smith_diagonal],
        "six_minor_gcd_and_ideal_norm": str(index),
        "full_integer_payload_sha256": payload_hash,
        "full_integer_payload_bytes": len(full_payload),
    }


def main() -> None:
    if (T0 * T0 + T0 - 1) % P or (A0 * A0 - 3 * A0 + 1) % P:
        raise AssertionError("incorrect real-quadratic residue")
    if (T1 * T1 + T1 - 1) % P or A0 * A1 % P != 1:
        raise AssertionError("incorrect conjugate real-quadratic residue")
    if sum(pow(ZETA0, j, P) for j in range(5)) % P or ZETA0 == 1:
        raise AssertionError("zeta residue is not a primitive fifth root")
    if ZETA0 * ZETA0_INV % P != 1:
        raise AssertionError("incorrect inverse fifth root")
    if (ZETA0 + ZETA0_INV) % P != T0:
        raise AssertionError("zeta residue has the wrong trace")
    if pow(1 + ZETA0, -1, P) != X0 or (1 - X0) % P != Y0:
        raise AssertionError("incorrect eta residues")
    if (X0 + Y0) % P != 1 or X0 * Y0 % P != A1:
        raise AssertionError("incorrect eta sum or product")
    if (U0, V0) != ((1 + ZETA0) % P, (1 + ZETA0_INV) % P):
        raise AssertionError("incorrect cyclotomic units")
    if ZETA0_INV * U0 % P != V0:
        raise AssertionError("incorrect scaling in the first-jet polynomial")

    archive_root = Path(__file__).resolve().parent.parent
    source_path = archive_root / "sources/algebraic_unit_two_log_n5_all_prime_counterexample.md"
    result = {
        "schema_version": 1,
        "checked_utc": "2026-08-27",
        "unconditional_conclusion": {
            "statement": "109321 divides Norm_F/Q(J_6219)",
            "stronger_exact_statement": "Norm_F/Q(J_6219)=109321",
            "prime_ideal": "(109321,t-53267)",
            "consequence": "The proposed all-prime classification by (19,15) and the containment 361 in J_d are false.",
        },
        "parameters": {
            "p": P,
            "d": D,
            "m": M,
            "t0": T0,
            "A0": A0,
            "conjugate_t1": T1,
            "conjugate_A1": A1,
            "zeta": ZETA0,
            "zeta_inverse": ZETA0_INV,
            "x": X0,
            "y": Y0,
            "u": U0,
            "v": V0,
        },
        "primality_certificate": prime_certificate(),
        "P_value_checks": {
            "at_x": p_value_mod(X0),
            "at_y": p_value_mod(Y0),
        },
        "h_modular_first_jet": h_modular_data(),
        "h_characteristic_zero_first_jet_ideal": h_characteristic_zero_data(),
        "weighted_prescribed_first_jet": weighted_first_jet_data(),
        "characteristic_zero_J_ideal": characteristic_zero_J_data(),
        "finite_scans_not_used_in_proof": {
            "branch_1_scope": "Every odd prime p<=200000, p!=5, every 0<=d<p, both roots of A^2-3A+1 in the split cases and exact quadratic-pair arithmetic in the inert cases.",
            "branch_1_hits": [[19, 15], [109321, 6219]],
            "full_three_branch_scope": "Every odd prime p<=30000, p!=5, every 0<=d<p.",
            "full_three_branch_hits": [[19, 15]],
            "logical_status": "finite diagnostic only; neither scan is used to prove the displayed counterexample or to exclude later primes",
        },
        "file_sha256": {
            "source": file_sha256(source_path),
            "script": file_sha256(Path(__file__).resolve()),
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
