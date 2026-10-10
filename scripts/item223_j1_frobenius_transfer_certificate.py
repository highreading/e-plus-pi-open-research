#!/usr/bin/env python3
"""Deterministic checks for Item 223's j=1 Frobenius transfer.

The companion report contains the all-row derivation.  This checker verifies
the Pearson recurrence, common initial line, both resonance sources, closed
coefficient formulas, transfer determinant, diagonal exclusion, and a
finite actual-row replay.  Output contains no clock or host-dependent path.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item223_j1_frobenius_transfer_certificate.json"

DEPENDENCIES = {
    "scripts/item218_j1_common_log_certificate.py":
        "a238c5ca37263f2553da47bf3f21253aedf1c34f8c57458a4a274fc6cdc9029a",
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "scripts/item220_twisted_derham_fixed_cells_certificate.py":
        "3e65aea853529c616398518f6e1c9fa6c8493fc5004d6171f01c926bbbb6cbbe",
    "sources/item220_twisted_derham_fixed_cells_report.md":
        "3ddc253eedb4453370d41953b1b050341e6ec59028059e459b82249d84f340b9",
}


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load_item218():
    path = resolve("item218_j1_common_log_certificate.py")
    spec = importlib.util.spec_from_file_location("item223_item218", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


item218 = load_item218()


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def convolution(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            answer[i + j] += a_value * b_value
    return answer


def polynomial_power(base: list[int], exponent: int) -> list[int]:
    answer = [1]
    factor = base[:]
    while exponent:
        if exponent & 1:
            answer = convolution(answer, factor)
        exponent >>= 1
        if exponent:
            factor = convolution(factor, factor)
    return answer


def derivative(poly: list[int]) -> list[int]:
    return [(index + 1) * poly[index + 1] for index in range(len(poly) - 1)]


def add_polynomials(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return [
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ]


def pearson_check(limit: int = 8) -> dict:
    sigma = [1, -1, 1, -1]  # (1-z)(1+z^2)
    rows = []
    for r_value in range(2, 2 * limit + 1, 2):
        for s_value in range(1, limit + 1):
            weight = convolution(
                polynomial_power([1, -1], r_value),
                polynomial_power([1, 0, 1], 2 * s_value - 1),
            )
            tau = [
                -r_value - 1,
                4 * s_value,
                -r_value - 4 * s_value - 1,
            ]
            left = derivative(convolution(sigma, weight))
            right = convolution(tau, weight)
            if left != right:
                raise AssertionError((r_value, s_value, "Pearson identity"))
            rows.append((r_value, s_value, len(weight) - 1))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "identity": "((1-z)(1+z^2)W)'=(-r-1+4sz-(r+4s+1)z^2)W",
        "formal_rows": len(rows),
        "r_even_max": 2 * limit,
        "s_max": limit,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def i_power(exponent: int) -> tuple[int, int]:
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[exponent % 4]


def gaussian_multiply(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def ell_numerator(exponent: int, epsilon: int) -> int:
    minus_i_power = i_power(3 * (exponent + 1))
    plus_i_power = i_power(exponent + 1)
    first = gaussian_multiply((2 * epsilon, -1), minus_i_power)
    second = gaussian_multiply((2 * epsilon, 1), plus_i_power)
    total = (first[0] + second[0], first[1] + second[1])
    if total[1]:
        raise AssertionError((exponent, epsilon, total))
    return total[0]


def fraction_mod(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise AssertionError((value, prime, "nonintegral residue"))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def boundary_moment(
    prime: int, r_value: int, s_value: int, epsilon: int, shift: int
) -> Fraction:
    weight = convolution(
        polynomial_power([1, -1], r_value),
        polynomial_power([1, 0, 1], 2 * s_value - 1),
    )
    exponent = prime + r_value + shift
    return sum(
        Fraction(coefficient * ell_numerator(exponent + degree, epsilon),
                 exponent + degree + 1)
        for degree, coefficient in enumerate(weight)
    )


def source_and_phase_check(prime_max: int = 251) -> dict:
    rows = []
    for prime in item218.primes_upto(prime_max):
        if prime < 13:
            continue
        for s_value in range(1, (prime - 7) // 6 + 1):
            numerator = prime - 6 * s_value - 3
            if numerator % 4:
                continue
            h_value = numerator // 4
            if h_value < 1:
                continue
            r_value = 2 * h_value
            epsilon = -1 if (s_value + 1) & 1 else 1
            n_value = prime + r_value
            n0 = 2 * prime - 2 * s_value - 1
            n1 = n0 + 1
            if i_power(n0) != (0, -epsilon):
                raise AssertionError((prime, r_value, s_value, n0, "i^N0"))
            if i_power(3 * n0) != (0, epsilon):
                raise AssertionError((prime, r_value, s_value, n0, "(-i)^N0"))
            if i_power(n1) != (epsilon, 0) or i_power(3 * n1) != (epsilon, 0):
                raise AssertionError((prime, r_value, s_value, n1, "N1 phase"))
            lower = ell_numerator(prime - 1, epsilon)
            upper = ell_numerator(2 * prime - 1, epsilon)
            if lower != -2 * epsilon or upper != -4 * epsilon:
                raise AssertionError((prime, epsilon, lower, upper))
            terminal = 2 * s_value + 1
            lower_exact_multiplier = n_value + (-r_value - 1) + 1
            upper_exact_multiplier = (
                n_value + terminal + 1 + r_value + 4 * s_value + 1
            )
            if lower_exact_multiplier != prime or upper_exact_multiplier != 2 * prime:
                raise AssertionError(
                    (
                        prime,
                        r_value,
                        s_value,
                        lower_exact_multiplier,
                        upper_exact_multiplier,
                    )
                )
            lower_moment = boundary_moment(
                prime, r_value, s_value, epsilon, -r_value - 1
            )
            upper_moment = boundary_moment(
                prime, r_value, s_value, epsilon, terminal + 3
            )
            lower_source = fraction_mod(prime * lower_moment, prime)
            upper_half_residue = fraction_mod(prime * upper_moment, prime)
            upper_source = fraction_mod(2 * prime * upper_moment, prime)
            expected_lower = (-2 * epsilon) % prime
            expected_upper = (-4 * epsilon) % prime
            if (
                lower_source != expected_lower
                or upper_half_residue != expected_lower
                or upper_source != expected_upper
            ):
                raise AssertionError(
                    (
                        prime,
                        r_value,
                        s_value,
                        lower_source,
                        upper_half_residue,
                        upper_source,
                    )
                )
            for shift in (-r_value - 1, terminal):
                exact_lead = prime + 2 * r_value + 4 * s_value + shift + 2
                exact_right = (
                    (prime + r_value + shift + 1)
                    * boundary_moment(prime, r_value, s_value, epsilon, shift)
                    - (prime + 2 * r_value + shift + 2)
                    * boundary_moment(prime, r_value, s_value, epsilon, shift + 1)
                    + (prime + r_value + 4 * s_value + shift + 1)
                    * boundary_moment(prime, r_value, s_value, epsilon, shift + 2)
                )
                exact_left = exact_lead * boundary_moment(
                    prime, r_value, s_value, epsilon, shift + 3
                )
                if exact_left != exact_right:
                    raise AssertionError(
                        (prime, r_value, s_value, shift, exact_left, exact_right)
                    )
            rows.append(
                (
                    prime,
                    r_value,
                    s_value,
                    n_value,
                    epsilon,
                    lower,
                    upper,
                    lower_exact_multiplier,
                    upper_exact_multiplier,
                    lower_source,
                    upper_source,
                )
            )
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "prime_max": prime_max,
        "actual_rows": len(rows),
        "common_boundary_functional": (
            "L_e(f)=(2e-i)int_0^(-i)f(z)dz+(2e+i)int_0^i f(z)dz"
        ),
        "lower_residue": "p*L_e(z^(p-1)W)=-2e mod p",
        "upper_residue": "p*L_e(z^(p+r+2s+4)W)=-2e mod p",
        "exact_recurrence_multipliers": "p at the lower pole and 2p at the upper pole",
        "terminal_sources": "Delta_minus=-2e and Delta_plus=-4e mod p",
        "direct_exact_recurrence_checks": "both terminal shifts on every replayed row",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def initial_line_check(prime_max: int = 251) -> dict:
    rows = []
    for prime in item218.primes_upto(prime_max):
        if prime < 13:
            continue
        for s_value in range(1, (prime - 7) // 6 + 1):
            numerator = prime - 6 * s_value - 3
            if numerator % 4:
                continue
            r_value = numerator // 2
            if r_value < 2 or r_value % 2:
                continue
            row_0 = (
                3 * r_value + 4 * s_value + 3,
                4 * s_value,
                3 * r_value + 8 * s_value + 3,
            )
            row_1 = (
                7 * r_value + 16 * s_value + 11,
                4 * s_value,
                -r_value - 4 * s_value - 1,
            )
            vector = (1, 1, -1)
            if any(
                sum(left * right for left, right in zip(row, vector)) % prime
                for row in (row_0, row_1)
            ):
                raise AssertionError((prime, r_value, s_value, row_0, row_1))
            minor = (row_0[0] * row_1[1] - row_0[1] * row_1[0]) % prime
            if not minor:
                raise AssertionError((prime, r_value, s_value, "rank minor"))
            rows.append((prime, r_value, s_value, minor))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "prime_max": prime_max,
        "actual_rows": len(rows),
        "equivalent_rows": [
            ["3r+4s+3", "4s", "3r+8s+3"],
            ["7r+16s+11", "4s", "-r-4s-1"],
        ],
        "rank_minor": "-16s(r+3s+2)=-8s mod p, hence nonzero",
        "common_kernel_line": "<(1,1,-1)>",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def transfer_mod(r_value: int, s_value: int, prime: int) -> tuple[int, int]:
    """Return (Delta_plus, Delta_minus) for the normalized initial line."""
    u0, u1, u2 = 1, 1, prime - 1
    terminal = 2 * s_value + 1
    for t_value in range(terminal):
        denominator = 2 * r_value + 4 * s_value + t_value + 2
        if not 0 < denominator < prime:
            raise AssertionError((prime, r_value, s_value, t_value, denominator))
        next_value = (
            (r_value + t_value + 1) * u0
            - (2 * r_value + t_value + 2) * u1
            + (r_value + 4 * s_value + t_value + 1) * u2
        ) * pow(denominator, -1, prime) % prime
        u0, u1, u2 = u1, u2, next_value
    delta_plus = (
        (r_value + terminal + 1) * u0
        - (2 * r_value + terminal + 2) * u1
        + (r_value + 4 * s_value + terminal + 1) * u2
    ) % prime

    u0, u1, u2 = 1, 1, prime - 1
    for t_value in range(-1, -r_value - 1, -1):
        denominator = r_value + t_value + 1
        if not 0 < denominator < prime:
            raise AssertionError((prime, r_value, s_value, t_value, denominator))
        previous = (
            (2 * r_value + 4 * s_value + t_value + 2) * u2
            + (2 * r_value + t_value + 2) * u0
            - (r_value + 4 * s_value + t_value + 1) * u1
        ) * pow(denominator, -1, prime) % prime
        u2, u1, u0 = u1, u0, previous
    delta_minus = (
        (r_value + 1) * u0
        - 4 * s_value * u1
        + (r_value + 4 * s_value + 1) * u2
    ) % prime
    return delta_plus, delta_minus


def transfer_fraction(r_value: int, s_value: int) -> tuple[Fraction, Fraction]:
    values = {0: Fraction(1), 1: Fraction(1), 2: Fraction(-1)}
    terminal = 2 * s_value + 1
    for t_value in range(terminal):
        values[t_value + 3] = (
            (r_value + t_value + 1) * values[t_value]
            - (2 * r_value + t_value + 2) * values[t_value + 1]
            + (r_value + 4 * s_value + t_value + 1) * values[t_value + 2]
        ) / (2 * r_value + 4 * s_value + t_value + 2)
    delta_plus = (
        (r_value + terminal + 1) * values[terminal]
        - (2 * r_value + terminal + 2) * values[terminal + 1]
        + (r_value + 4 * s_value + terminal + 1) * values[terminal + 2]
    )
    for t_value in range(-1, -r_value - 1, -1):
        values[t_value] = (
            (2 * r_value + 4 * s_value + t_value + 2) * values[t_value + 3]
            + (2 * r_value + t_value + 2) * values[t_value + 1]
            - (r_value + 4 * s_value + t_value + 1) * values[t_value + 2]
        ) / (r_value + t_value + 1)
    delta_minus = (
        (r_value + 1) * values[-r_value]
        - 4 * s_value * values[-r_value + 1]
        + (r_value + 4 * s_value + 1) * values[-r_value + 2]
    )
    return delta_plus, delta_minus


def base_coefficient(r_value: int, s_value: int, degree: int) -> int:
    """[x^degree](1-x)^(-r-1)(1+x^2)^(-2s)."""
    return sum(
        (-1) ** index
        * comb(2 * s_value + index - 1, index)
        * comb(r_value + degree - 2 * index, degree - 2 * index)
        for index in range(degree // 2 + 1)
    )


def closed_delta_plus(r_value: int, s_value: int) -> int:
    degree = 2 * s_value + 4
    return (
        (2 * r_value + 4 * s_value - 1)
        * base_coefficient(r_value, s_value, degree)
        + (r_value + 1) * base_coefficient(r_value, s_value, degree - 1)
        - (r_value + 8 * s_value)
        * base_coefficient(r_value, s_value, degree - 2)
    )


def closed_delta_minus(r_value: int, s_value: int) -> int:
    degree = r_value + 3
    coefficient = (
        (r_value + 3) * base_coefficient(r_value, s_value, degree)
        - (3 * r_value + 5) * base_coefficient(r_value, s_value, degree - 1)
        + (2 * r_value + 4 * s_value + 2)
        * base_coefficient(r_value, s_value, degree - 2)
    )
    return -coefficient


def closed_formula_check(prime_max: int = 251) -> dict:
    rows = []
    for prime in item218.primes_upto(prime_max):
        if prime < 13:
            continue
        for s_value in range(1, (prime - 7) // 6 + 1):
            numerator = prime - 6 * s_value - 3
            if numerator % 4:
                continue
            r_value = numerator // 2
            if r_value < 2 or r_value % 2:
                continue
            plus, minus = transfer_mod(r_value, s_value, prime)
            plus_closed = closed_delta_plus(r_value, s_value) % prime
            minus_closed = closed_delta_minus(r_value, s_value) % prime
            if (plus, minus) != (plus_closed, minus_closed):
                raise AssertionError(
                    (prime, r_value, s_value, plus, minus, plus_closed, minus_closed)
                )
            rows.append((prime, r_value, s_value, plus, minus))
    for r_value in range(2, 14, 2):
        for s_value in range(1, 7):
            _, minus = transfer_fraction(r_value, s_value)
            if minus.denominator != 1 or minus.numerator != closed_delta_minus(
                r_value, s_value
            ):
                raise AssertionError((r_value, s_value, minus, "exact minus formula"))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "prime_max": prime_max,
        "actual_rows": len(rows),
        "D_n": (
            "sum_{j=0}^{floor(n/2)} (-1)^j binom(2s+j-1,j) "
            "binom(r+n-2j,n-2j)"
        ),
        "delta_plus_mod_p": (
            "(2r+4s-1)D_(2s+4)+(r+1)D_(2s+3)-(r+8s)D_(2s+2)"
        ),
        "delta_minus_exact": (
            "-(r+3)D_(r+3)+(3r+5)D_(r+2)-(2r+4s+2)D_(r+1)"
        ),
        "exact_minus_formal_grid": "2<=r<=12 even, 1<=s<=6",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def diagonal_check(prime_max: int) -> dict:
    rows = []
    for prime in item218.primes_upto(prime_max):
        if prime < 13 or prime % 10 != 3:
            continue
        s_value = (prime - 3) // 10
        r_value = 2 * s_value
        plus, minus = transfer_mod(r_value, s_value, prime)
        if plus != minus:
            raise AssertionError((prime, r_value, s_value, plus, minus))
        rows.append((prime, r_value, s_value, plus))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "PROVED_ALL_PRIME_DIAGONAL_EXCLUSION",
        "family": "r=2s, p=10s+3 prime",
        "involution": "v_t=-v_(3-t) mod p",
        "transfer_identity": "Delta_plus=Delta_minus identically on this actual family",
        "collision_requirement": "Delta_plus=2*Delta_minus!=0 mod p",
        "conclusion": "the actual paired common-log collision is impossible on every diagonal row",
        "finite_prime_max": prime_max,
        "finite_rows": len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def finite_actual_replay(prime_max: int) -> dict:
    counts = {
        "rows": 0,
        "delta_plus_zero": 0,
        "delta_minus_zero": 0,
        "Theta_zero": 0,
        "Theta_zero_diagonal": 0,
        "transfer_necessary_survivors": 0,
        "direct_paired_zero_among_survivors": 0,
    }
    theta_rows = []
    plus_zero_examples = []
    off_diagonal_examples = []
    for prime in item218.primes_upto(prime_max):
        if prime < 13:
            continue
        for s_value in range(1, (prime - 7) // 6 + 1):
            numerator = prime - 6 * s_value - 3
            if numerator % 4:
                continue
            h_value = numerator // 4
            if h_value < 1:
                continue
            r_value = 2 * h_value
            plus, minus = transfer_mod(r_value, s_value, prime)
            theta = (plus - 2 * minus) % prime
            counts["rows"] += 1
            counts["delta_plus_zero"] += plus == 0
            counts["delta_minus_zero"] += minus == 0
            counts["Theta_zero"] += theta == 0
            counts["Theta_zero_diagonal"] += theta == 0 and r_value == 2 * s_value
            if plus == 0 and len(plus_zero_examples) < 6:
                q0, q1 = item218.candidate_conditions(prime, h_value, s_value)
                plus_zero_examples.append((prime, r_value, s_value, minus, q0, q1))
            if theta:
                continue
            if not plus:
                raise AssertionError((prime, r_value, s_value, "necessary transfer is zero"))
            counts["transfer_necessary_survivors"] += 1
            q0, q1 = item218.candidate_conditions(prime, h_value, s_value)
            counts["direct_paired_zero_among_survivors"] += q0 == q1 == 0
            row = (prime, r_value, s_value, plus, q0, q1)
            theta_rows.append(row)
            if r_value != 2 * s_value and len(off_diagonal_examples) < 8:
                off_diagonal_examples.append(row)
    expected = {
        "rows": 22934,
        "delta_plus_zero": 29,
        "delta_minus_zero": 22,
        "Theta_zero": 22,
        "Theta_zero_diagonal": 0,
        "transfer_necessary_survivors": 22,
        "direct_paired_zero_among_survivors": 0,
    }
    if prime_max == 2000 and counts != expected:
        raise AssertionError((counts, expected))
    stream = json.dumps(theta_rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_ONLY",
        "prime_max": prime_max,
        **counts,
        "first_delta_plus_zero_rows": plus_zero_examples,
        "first_off_diagonal_Theta_zero_rows": off_diagonal_examples,
        "Theta_survivor_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "scope_warning": "finite survivor counts imply no all-prime density or rate bound",
    }


def certificate(prime_max: int) -> dict:
    return {
        "item": 223,
        "classification": {
            "PROVED": [
                "the Item220 j=1 pair uses one common boundary functional after reciprocity",
                "the gcd weight has the stated exact order-three Pearson moment recurrence",
                "the two collision equations reduce to the initial line <(1,1,-1)>",
                "the lower and upper Frobenius sources are -2epsilon and -4epsilon",
                "every collision satisfies Delta_plus=2*Delta_minus!=0",
                "the closed binomial coefficient formulas for both transfer scalars",
                "the transfer determinant excludes every actual diagonal row r=2s",
            ],
            "EXACT_FINITE_ONLY": [
                f"transfer survivor replay and direct noncollision through p<={prime_max}"
            ],
            "OPEN": [
                "all-prime noncollision on the remaining off-diagonal transfer survivors",
                "an independent higher resonance or arithmetic invariant",
                "any positive Route-1 linear log-rate or radical saving",
            ],
        },
        "parameters": {
            "prime": "p=2r+6s+3=4h+6s+3",
            "j1": "r=2h even, h,s>=1",
            "epsilon": "(-1)^((p-1)/2)=(-1)^(s+1)",
            "common_exponent": "n*=p+r",
            "gcd_weight": "W=(1-z)^r(1+z^2)^(2s-1)",
        },
        "boundary_bridge": source_and_phase_check(),
        "pearson_recurrence": {
            "formula": (
                "(2r+4s+t+2)u_(t+3)=(r+t+1)u_t-(2r+t+2)u_(t+1)"
                "+(r+4s+t+1)u_(t+2)"
            ),
            "regression": pearson_check(),
        },
        "initial_line": initial_line_check(),
        "frobenius_transfer": {
            "upper_resonance_shift": "T=2s+1",
            "lower_resonance_shift": "-r-1",
            "lower_source": "-2epsilon",
            "upper_source": "-4epsilon",
            "collision_implication": "Delta_plus=2*Delta_minus!=0 mod p",
            "transfer_matrix_determinant": (
                "product_(t=0)^(T-1) (r+t+1)/(2r+4s+t+2), a p-unit"
            ),
            "closed_formulas": closed_formula_check(),
        },
        "diagonal_exclusion": diagonal_check(prime_max),
        "finite_actual_replay": finite_actual_replay(prime_max),
        "rate_ledger": {
            "j1_cell_mass_per_m_if_fully_excluded": "1/6",
            "full_cell_exclusion": "OPEN",
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "reason": "the diagonal is excluded, but no uniform bound is proved for all off-diagonal survivors",
        },
        "dependency_sha256": DEPENDENCIES,
        "runtime": {"external_numeric_backend": None},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=2000)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    result = certificate(args.prime_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    replay = result["finite_actual_replay"]
    print(json.dumps({
        "output": str(args.output),
        "prime_max": args.prime_max,
        "rows": replay["rows"],
        "transfer_survivors": replay["transfer_necessary_survivors"],
        "paired_zeros_among_survivors": replay[
            "direct_paired_zero_among_survivors"
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
