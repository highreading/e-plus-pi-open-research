#!/usr/bin/env python3
"""Deterministic certificate for Item 235's j=2 p^2 terminal lift.

The checker works over Z/(p^2), retaining the exact q*p terminal
multiplicity.  It verifies the lifted finite-part recurrence, the harmonic
4p carry, the lifted affine terminal rows, and the exact redundancy of the
corrected four-phase closure.  It also reconstructs an integer common-log
coefficient showing that the frozen mod-p beta-period bridge does not lift
naively to p^2.  All finite censuses are labelled as such in the output.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item235_j2_witt_terminal_certificate.json"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM227_PATH = resolve("item227_j2_phase_control_certificate.py")
item227 = load("item235_item227", ITEM227_PATH)
item226 = item227.item226
item225 = item227.item225
item224 = item227.item224
item219 = item227.item219


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def exact_convolution(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return tuple(result)


def exact_power(base: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    result = (1,)
    power = base
    while exponent:
        if exponent & 1:
            result = exact_convolution(result, power)
        exponent //= 2
        if exponent:
            power = exact_convolution(power, power)
    return result


@functools.lru_cache(maxsize=None)
def exact_g(p: int, s: int) -> tuple[int, tuple[int, ...]]:
    """Return r and the exact integer coefficients of g."""
    r = (p - 6 * s - 3) // 2
    polynomial = exact_convolution(exact_power((1, -1), r), (1, 1))
    polynomial = exact_convolution(polynomial, exact_power((1, 0, 1), 2 * s))
    return r, polynomial


def phase_weight(p: int, n: int) -> int:
    chi = 1 if p % 4 == 1 else -1
    return item219.residue_weight(n, chi)


def recurrence_coefficients(k: int, r: int, s: int) -> tuple[int, ...]:
    return (
        k + r + 1,
        1 - r,
        4 * s - r - 1,
        1 - r,
        -(k + 2 * r + 4 * s + 6),
    )


@functools.lru_cache(maxsize=None)
def finite_period(p: int, s: int, k: int, modulus: int) -> int:
    """Canonical finite part in Z/(p^2), or in a requested p-power ring."""
    r, polynomial = exact_g(p, s)
    total = 0
    for ell, coefficient in enumerate(polynomial):
        denominator = r + ell + k + 1
        if denominator % p:
            total += (
                coefficient
                * phase_weight(p, denominator)
                * pow(denominator % modulus, -1, modulus)
            )
    return total % modulus


@functools.lru_cache(maxsize=None)
def h_coefficient(p: int, s: int, exponent: int) -> int:
    """Coefficient of z^exponent in (1-z^4) z^r g(z), over Z."""
    r, polynomial = exact_g(p, s)

    def f_coefficient(degree: int) -> int:
        index = degree - r
        return polynomial[index] if 0 <= index < len(polynomial) else 0

    return f_coefficient(exponent) - f_coefficient(exponent - 4)


@functools.lru_cache(maxsize=None)
def regularized_rhs(p: int, s: int, k: int, modulus: int) -> int:
    """The exact positive-Cartier-source side, reduced modulo modulus."""
    _, polynomial = exact_g(p, s)
    r = (p - 6 * s - 3) // 2
    degree_h = r + len(polynomial) - 1 + 4
    top = k + 1 + degree_h
    total = 0
    for multiple in range(p, top + 1, p):
        coefficient = h_coefficient(p, s, multiple - k - 1)
        total -= coefficient * phase_weight(p, multiple)
    return total % modulus


def add_vectors(left: tuple[int, ...], right: tuple[int, ...], modulus: int) -> tuple[int, ...]:
    return tuple((left[j] + right[j]) % modulus for j in range(len(left)))


def scale_vector(value: tuple[int, ...], scalar: int, modulus: int) -> tuple[int, ...]:
    return tuple(scalar * x % modulus for x in value)


def dot(left: list[int] | tuple[int, ...], right: list[int] | tuple[int, ...], modulus: int) -> int:
    return sum(x * y for x, y in zip(left, right)) % modulus


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def matrix_multiply(left: list[list[int]], right: list[list[int]], modulus: int) -> list[list[int]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right))) % modulus
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def matrix_vector(matrix: list[list[int]], vector: list[int], modulus: int) -> list[int]:
    return [dot(row, vector, modulus) for row in matrix]


def row_matrix(row: list[int], matrix: list[list[int]], modulus: int) -> list[int]:
    return [
        sum(row[k] * matrix[k][j] for k in range(len(row))) % modulus
        for j in range(len(matrix[0]))
    ]


def inverse_matrix(matrix: list[list[int]], modulus: int) -> list[list[int]]:
    size = len(matrix)
    work = [
        [matrix[i][j] % modulus for j in range(size)]
        + [int(i == j) for j in range(size)]
        for i in range(size)
    ]
    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if math.gcd(work[row][column], modulus) == 1
            ),
            None,
        )
        if pivot is None:
            raise ZeroDivisionError("matrix is not invertible over the local ring")
        work[column], work[pivot] = work[pivot], work[column]
        unit = pow(work[column][column], -1, modulus)
        work[column] = [entry * unit % modulus for entry in work[column]]
        for row in range(size):
            if row == column:
                continue
            factor = work[row][column]
            work[row] = [
                (work[row][j] - factor * work[column][j]) % modulus
                for j in range(2 * size)
            ]
    return [row[size:] for row in work]


def initial_line(p: int, s: int, modulus: int) -> dict[int, int]:
    if s < 2:
        raise ValueError("Item 235's z^3 line assumes s>=2")
    denominator = 4 * (s - 1)
    if math.gcd(denominator, p) != 1:
        raise AssertionError((p, s, "initial-line denominator"))
    return {
        0: 0,
        1: (4 * s - 2) % modulus,
        2: (2 * s - 5) % modulus,
        3: (
            -(52 * s * s - 36 * s - 27)
            * pow(denominator % modulus, -1, modulus)
        )
        % modulus,
    }


def canonical_line(p: int, s: int) -> dict[str, Any]:
    """Lift Item 224's rational common line and propagate it to both terminals."""
    modulus = p * p
    r = (p - 6 * s - 3) // 2
    first = 2 * s - 3
    values = initial_line(p, s, modulus)

    for k in range(0, first):
        coefficients = recurrence_coefficients(k, r, s)
        pivot = coefficients[4]
        if math.gcd(pivot, p) != 1:
            raise AssertionError((p, s, k, "forward pivot"))
        numerator = regularized_rhs(p, s, k, modulus)
        numerator -= sum(coefficients[j] * values[k + j] for j in range(4))
        values[k + 4] = numerator * pow(pivot % modulus, -1, modulus) % modulus

    tail = [values[first + j] for j in range(4)]
    backward = dict(values)
    for k in range(-1, -r - 1, -1):
        coefficients = recurrence_coefficients(k, r, s)
        pivot = coefficients[0]
        if math.gcd(pivot, p) != 1:
            raise AssertionError((p, s, k, "backward pivot"))
        numerator = regularized_rhs(p, s, k, modulus)
        numerator -= sum(coefficients[j] * backward[k + j] for j in range(1, 5))
        backward[k] = numerator * pow(pivot % modulus, -1, modulus) % modulus

    bottom_k = -r - 1
    bottom_coefficients = recurrence_coefficients(bottom_k, r, s)
    if bottom_coefficients[0] != 0:
        raise AssertionError((p, s, "bottom coefficient"))
    beta = sum(
        bottom_coefficients[j] * backward[bottom_k + j] for j in range(1, 5)
    ) % modulus
    return {"r": r, "first": first, "tail": tail, "beta": beta}


def homogeneous_phase_transfer(p: int, s: int, phase: int) -> list[list[int]]:
    """Difference transfer with the resonant coordinate reset to zero."""
    modulus = p * p
    r = (p - 6 * s - 3) // 2
    first = 2 * s - 3
    terminal = first + (phase - 1) * p
    dimension = 4
    values: dict[int, tuple[int, ...]] = {
        terminal + j: tuple(int(i == j) for i in range(dimension))
        for j in range(dimension)
    }
    values[terminal + 4] = (0, 0, 0, 0)

    for k in range(terminal + 1, terminal + p):
        coefficients = recurrence_coefficients(k, r, s)
        pivot = coefficients[4]
        if math.gcd(pivot, p) != 1:
            raise AssertionError((p, s, phase, k, "interphase pivot"))
        lower = (0, 0, 0, 0)
        for j in range(4):
            lower = add_vectors(
                lower, scale_vector(values[k + j], coefficients[j], modulus), modulus
            )
        values[k + 4] = scale_vector(
            lower, -pow(pivot % modulus, -1, modulus), modulus
        )
    return [list(values[terminal + p + j]) for j in range(4)]


def lifted_affine_system(p: int, s: int) -> dict[str, Any]:
    modulus = p * p
    base = canonical_line(p, s)
    r = int(base["r"])
    first = int(base["first"])
    candidate_tail: list[int] = base["tail"]
    beta = int(base["beta"])
    epsilon = (-1) ** r

    # Each entry is (constant term, coefficient of lambda).
    values: dict[int, tuple[int, int]] = {
        first + j: (0, candidate_tail[j]) for j in range(4)
    }
    rows: list[tuple[str, int, int]] = [("bottom", beta, 11 % modulus)]
    transfers: list[list[list[int]]] = []
    terminal_x: list[int] = []
    terminal_covectors: list[list[int]] = []

    for phase in range(1, 5):
        terminal = first + (phase - 1) * p
        coefficients = recurrence_coefficients(terminal, r, s)
        if coefficients[4] != -phase * p:
            raise AssertionError((p, s, phase, coefficients[4]))
        covector = list(coefficients[:4])
        x_value = finite_period(p, s, terminal + 4, modulus)
        constants = [values[terminal + j][0] for j in range(4)]
        lambdas = [values[terminal + j][1] for j in range(4)]
        coefficient = dot(covector, lambdas, modulus)
        rhs = (
            epsilon * phase_weight(p, phase * p)
            + phase * p * x_value
            - dot(covector, constants, modulus)
        ) % modulus
        rows.append((f"terminal_{phase}", coefficient, rhs))
        terminal_x.append(x_value)
        terminal_covectors.append(covector)

        values[terminal + 4] = (x_value, 0)
        transfer = homogeneous_phase_transfer(p, s, phase)
        transfers.append(transfer)
        for k in range(terminal + 1, terminal + p):
            coefficients_k = recurrence_coefficients(k, r, s)
            pivot = coefficients_k[4]
            lower = (0, 0)
            for j in range(4):
                lower = add_vectors(
                    lower,
                    scale_vector(values[k + j], coefficients_k[j], modulus),
                    modulus,
                )
            source = (regularized_rhs(p, s, k, modulus), 0)
            values[k + 4] = scale_vector(
                add_vectors(source, scale_vector(lower, -1, modulus), modulus),
                pow(pivot % modulus, -1, modulus),
                modulus,
            )

    fifth = first + 4 * p
    fifth_constants = [values[fifth + j][0] for j in range(4)]
    fifth_lambdas = [values[fifth + j][1] for j in range(4)]
    carry = [
        (finite_period(p, s, fifth + j, modulus) - finite_period(p, s, first + j, modulus))
        % modulus
        for j in range(4)
    ]
    for j in range(4):
        rows.append(
            (
                f"corrected_closure_{j}",
                (fifth_lambdas[j] - candidate_tail[j]) % modulus,
                (carry[j] - fifth_constants[j]) % modulus,
            )
        )

    product = identity(4)
    observability: list[list[int]] = []
    for phase in range(4):
        observability.append(
            row_matrix(terminal_covectors[phase], product, modulus)
        )
        product = matrix_multiply(transfers[phase], product, modulus)

    reduced_observability = [[entry % p for entry in row] for row in observability]
    determinant = item226.determinant_mod(reduced_observability, p)
    if determinant == 0:
        raise AssertionError((p, s, "lifted observability"))

    closure_operator = [
        [(product[i][j] - int(i == j)) % modulus for j in range(4)]
        for i in range(4)
    ]
    combination = matrix_multiply(
        closure_operator, inverse_matrix(observability, modulus), modulus
    )

    terminal_rows = rows[1:5]
    closure_rows = rows[5:9]
    terminal_coefficients = [row[1] for row in terminal_rows]
    terminal_rhs = [row[2] for row in terminal_rows]
    for j, row in enumerate(closure_rows):
        if row[1] != dot(combination[j], terminal_coefficients, modulus):
            raise AssertionError((p, s, j, "closure coefficient combination"))
        if row[2] != dot(combination[j], terminal_rhs, modulus):
            raise AssertionError((p, s, j, "closure rhs combination"))

    return {
        "r": r,
        "rows": rows,
        "transfers": transfers,
        "carry": carry,
        "observability": observability,
        "observability_det_mod_p": determinant,
        "combination": combination,
        "terminal_x": terminal_x,
    }


def verify_row(p: int, s: int) -> tuple[int, ...]:
    modulus = p * p
    r = (p - 6 * s - 3) // 2
    first = 2 * s - 3
    fifth = first + 4 * p
    if r <= 0 or r % 2 != 1:
        raise AssertionError((p, s, r, "admissible r must be positive and odd"))

    recurrence_checks = 0
    for k in range(-r, fifth + 1):
        coefficients = recurrence_coefficients(k, r, s)
        lhs = sum(
            coefficients[j] * finite_period(p, s, k + j, modulus)
            for j in range(5)
        ) % modulus
        rhs = regularized_rhs(p, s, k, modulus)
        if lhs != rhs:
            raise AssertionError((p, s, k, "lifted recurrence", lhs, rhs))
        recurrence_checks += 1

    pole_audit: list[int] = []
    epsilon = (-1) ** r
    for phase in range(1, 5):
        terminal = first + (phase - 1) * p
        pivot = recurrence_coefficients(terminal, r, s)[4]
        primitive = Fraction(epsilon, phase * p)
        if pivot != -phase * p or pivot * primitive != -epsilon:
            raise AssertionError((p, s, phase, "rational pole audit"))
        coefficient_k = h_coefficient(p, s, phase * p - terminal - 1)
        if coefficient_k != -epsilon:
            raise AssertionError((p, s, phase, "Cartier coefficient", coefficient_k))
        if regularized_rhs(p, s, terminal, modulus) != (
            epsilon * phase_weight(p, phase * p)
        ) % modulus:
            raise AssertionError((p, s, phase, "terminal source"))
        pole_audit.append(phase)

    carry_digits: list[int] = []
    _, polynomial = exact_g(p, s)
    for offset in range(4):
        k = first + offset
        left = (
            finite_period(p, s, k + 4 * p, modulus)
            - finite_period(p, s, k, modulus)
        ) % modulus
        harmonic = 0
        for ell, coefficient in enumerate(polynomial):
            denominator = r + ell + k + 1
            if denominator % p:
                harmonic += (
                    coefficient
                    * phase_weight(p, denominator)
                    * pow(denominator % p, -2, p)
                )
        harmonic %= p
        if left != (-4 * p * harmonic) % modulus:
            raise AssertionError((p, s, offset, "4p carry", left, harmonic))
        carry_digits.append(left // p)

    lifted = lifted_affine_system(p, s)
    old = item226.phase_system(p, s)
    lifted_rows: list[tuple[str, int, int]] = lifted["rows"]
    reduced_rows = [(row[1] % p, row[2] % p) for row in lifted_rows]
    old_rows = list(zip(old["coefficient_column"], old["rhs_column"]))
    # Item 226 writes closure as initial-final, whereas the corrected
    # p^2 residual below is final-initial.  The four equations differ by
    # one harmless common sign.
    expected_rows = old_rows[:5] + [((-c) % p, (-d) % p) for c, d in old_rows[5:]]
    if reduced_rows != expected_rows:
        raise AssertionError((p, s, "reduction to Item 226"))
    old_matrix: list[list[int]] = old["M"]
    for transfer in lifted["transfers"]:
        if [[entry % p for entry in row] for row in transfer] != old_matrix:
            raise AssertionError((p, s, "phase transfer reduction"))

    return (
        p,
        s,
        r,
        recurrence_checks,
        *pole_audit,
        *carry_digits,
        int(lifted["observability_det_mod_p"]),
        *[entry for row in lifted_rows for entry in row[1:]],
    )


def common_log_coefficient(p: int, s: int, nu: int) -> int:
    """Reconstruct C_nu as an exact integer binomial coefficient sum."""
    m = (5 * p - 2 * s - 1) // 4
    target = 4 * m + nu
    numerator_power = 6 * m
    plus_power = 1 + 3 * nu
    denominator_power = 4 * m + 1 + nu
    numerator = [0] * (numerator_power + plus_power + 1)
    for a in range(numerator_power + 1):
        for b in range(plus_power + 1):
            numerator[a + b] += (
                (-1) ** a
                * math.comb(numerator_power, a)
                * math.comb(plus_power, b)
            )
    total = 0
    for degree, coefficient in enumerate(numerator[: target + 1]):
        remainder = target - degree
        if remainder % 2 == 0:
            half = remainder // 2
            total += (
                coefficient
                * (-1) ** half
                * math.comb(denominator_power + half - 1, half)
            )
    return total


def naive_bridge_counterexample() -> dict[str, int]:
    p, s, nu = 17, 2, 0
    modulus = p * p
    r = (p - 6 * s - 3) // 2
    coefficient = common_log_coefficient(p, s, nu)
    if coefficient % p:
        raise AssertionError("rank-zero divisibility failed")
    actual = (coefficient // p) % modulus
    canonical = (
        -35
        * ((-1) ** (r + 1))
        * finite_period(p, s, 0, modulus)
    ) % modulus
    if actual % p != canonical % p:
        raise AssertionError((actual, canonical, "frozen mod-p bridge"))
    difference = (actual - canonical) % modulus
    if difference != 3 * p:
        raise AssertionError((actual, canonical, difference))
    return {
        "p": p,
        "s": s,
        "nu": nu,
        "r": r,
        "C_nu_mod_p_cubed": coefficient % (p**3),
        "actual_C_nu_over_p_mod_p_squared": actual,
        "naive_beta_lift_mod_p_squared": canonical,
        "difference": difference,
        "difference_over_p_mod_p": difference // p,
    }


def admissible_rows(bound: int):
    for p in item219.primes_upto(bound):
        if p < 17:
            continue
        for s in range(2, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4 == 0:
                yield p, s


def finite_omega_census(bound: int) -> dict[str, Any]:
    rows = 0
    omega_zero: list[dict[str, int]] = []
    digest_rows: list[tuple[int, ...]] = []
    for p, s in admissible_rows(bound):
        rows += 1
        beta, tau, omega, r = item224.compatibility_mod(p, s)
        digest_rows.append((p, s, r, beta, tau, omega))
        if omega:
            continue
        lifted = lifted_affine_system(p, s)
        lifted_rows: list[tuple[str, int, int]] = lifted["rows"]
        bottom = lifted_rows[0]
        top = lifted_rows[1]
        modulus = p * p
        omega_lift = (bottom[1] * top[2] - top[1] * bottom[2]) % modulus
        if omega_lift % p:
            raise AssertionError((p, s, "lifted Omega does not reduce to zero"))
        psi = int(item225.second_phase_components(p, s)["psi"])
        omega_zero.append(
            {
                "p": p,
                "s": s,
                "r": r,
                "Psi_mod_p": psi,
                "canonical_Omega_second_digit": omega_lift // p,
            }
        )
    return {
        "row_count": rows,
        "row_digest_sha256": row_digest(digest_rows),
        "Omega_zero_count": len(omega_zero),
        "Omega_zero_rows": omega_zero,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proof-prime-max", type=int, default=101)
    parser.add_argument("--finite-prime-max", type=int, default=401)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if not (17 <= args.proof_prime_max <= args.finite_prime_max):
        raise ValueError("require 17 <= proof-prime-max <= finite-prime-max")

    proof_rows = [verify_row(p, s) for p, s in admissible_rows(args.proof_prime_max)]
    finite = finite_omega_census(args.finite_prime_max)
    counterexample = naive_bridge_counterexample()

    result = {
        "schema": "item235-j2-witt-terminal-v1",
        "item": 235,
        "route": "Route 1A",
        "cell": {
            "j": 2,
            "range": "p prime, s>=2, 4m+1=5p-2s, 1<=s<=(p-3)/6",
            "r": "(p-6s-3)/2, necessarily positive and odd",
            "ring": "Z/(p^2)",
        },
        "proved": {
            "finite_part": "T2_k=sum_(p does not divide d) g_l W(d)/d in Z/(p^2), d=r+l+k+1",
            "exact_recurrence": "sum_(j=0)^4 A_j(k) T2_(k+j)=-sum_(a>=1) [z^(ap)]K_k W(ap) mod p^2",
            "terminal": "a_q Y_q-q*p*x_q=(-1)^r W(qp), q=1,2,3,4",
            "terminal_weights": [7, 29, 11, -11],
            "rational_pole_audit": "A_4(k_q)=-q*p and the pole is (-1)^r*z^(q*p)/(q*p) before reduction",
            "four_p_carry": "T2_(k+4p)-T2_k=-4p*sum g_l W(d)/d^2 mod p^2",
            "witt_rows": "inside the canonical lift, if lambda0 solves c_i lambda=d_i mod p, then lambda0+p lambda1 solves mod p^2 iff cbar_i lambda1=(d_i-c_i lambda0)/p for every row",
            "closure_no_go": "the corrected four-phase closure residual is (P-I)*K^(-1) times the four terminal residuals over Z/(p^2); it gives no additional invariant",
            "actual_defect_expansion": "with X=((1-z)^p-(1-z^p))/(p(1-z^p)) and Y=((1+z^2)^p-(1+z^(2p)))/(p(1+z^(2p))), Delta_p G=G(z^p)*(7X-5Y+p*(21X^2+15Y^2-35XY)) mod p^2",
        },
        "proof_replay": {
            "prime_max_inclusive": args.proof_prime_max,
            "row_count": len(proof_rows),
            "row_digest_sha256": row_digest(proof_rows),
            "checks": [
                "all exact finite-part recurrences from the lower regular range through four phases",
                "all four q*p pole multiplicities and sources",
                "four required 4p carry coordinates",
                "reduction of every lifted affine row and transfer to frozen Item 226",
                "p-unit lifted observability and exact closure-row combinations",
            ],
        },
        "exact_finite": {
            "status": "EXACT FINITE ONLY",
            "prime_max_inclusive": args.finite_prime_max,
            **finite,
            "naive_bridge_counterexample": counterexample,
        },
        "scope_barrier": {
            "status": "PROVED OBSTRUCTION TO THE NAIVE LIFT; ACTUAL BRIDGE OPEN",
            "frozen_input": "Item 219 identifies C_nu/p with the beta period only modulo p, and Item 224 fixes the displayed common line only after reducing r modulo p",
            "counterexample": "at (p,s,nu)=(17,2,0), the two natural p^2 lifts differ by 3p",
            "consequence": "an ordinary collision does not force the canonical p^2 rows, and they are not yet proved necessary even under an extra-digit p^3-divisibility hypothesis",
        },
        "status_ledger": {
            "PROVED": [
                "the exact localized p^2 finite-part recurrence and every q*p terminal multiplicity",
                "the nonzero harmonic 4p carry replacing mod-p periodicity",
                "the canonical bottom-plus-terminal Witt/Hensel row criterion",
                "the exact redundancy of corrected order-four closure over Z/(p^2)",
                "the quadratic Frobenius-defect expansion showing the missing Witt correction",
                "a concrete exact counterexample to the naive p^2 beta-period bridge",
            ],
            "EXACT_FINITE": [
                "the proof replay through the stated proof bound",
                "the canonical Omega second digits on the seven frozen Omega-zero rows through p<=401",
            ],
            "OPEN": [
                "translate the actual second digit C_nu/p mod p^2 into a corrected terminal functional",
                "derive the true p-carry in the common initial line",
                "prove that any terminal Witt minor is necessary for an actual extra common-log digit",
                "classify simultaneous zeros of the corrected second-digit conditions",
                "obtain any all-prime j=2 exclusion, zero-rate theorem, or Route-1 gain",
            ],
        },
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "none",
        },
        "dependencies": {
            "item227_checker": ITEM227_PATH.name,
            "item227_checker_sha256": sha256(ITEM227_PATH),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
