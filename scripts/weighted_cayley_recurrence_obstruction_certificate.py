#!/usr/bin/env python3
"""Exact audit of the corrected weighted-residue s-recurrence.

This is a no-go/structure certificate.  It verifies the exact telescoper,
the short cohomological relation B_2 in terms of B_0,B_1, the failure of a
symmetric-cube explanation, and surviving terminal modes at old resultant
primes.  It does not prove fresh-prime nonvanishing.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


z, q, s = sp.symbols("z q s")
P = 1 + z + z**2 + z**3
alpha = (2 * q - 3) / 3


def expected_recurrence() -> list[sp.Expr]:
    return [
        -81 * (s + 1) * (s + 2) * (3 * s + 2) * (3 * s + 4)
        * (3 * s + 7) * (3 * s + 10),
        -5 * (s + 2) * (3 * s + 7) * (3 * s + 10)
        * (5 * q - 21 * s - 27)
        * (5 * q**2 - 24 * q * s - 33 * q + 45 * s**2 + 117 * s + 72),
        4 * (3 * s + 10) * (2 * q - 3 * s - 6)
        * (
            225 * q**2 * s**2 + 750 * q**2 * s + 650 * q**2
            - 1350 * q * s**3 - 6975 * q * s**2 - 11550 * q * s
            - 6150 * q + 2187 * s**4 + 15255 * s**3 + 38286 * s**2
            + 40770 * s + 15552
        ),
        -80 * (3 * s + 4) * (2 * q - 3 * s - 9) * (2 * q - 3 * s - 6)
        * (
            9 * q * s**2 + 39 * q * s + 37 * q - 27 * s**3
            - 180 * s**2 - 360 * s - 207
        ),
        64 * (s + 1) * (3 * s + 4) * (3 * s + 7)
        * (2 * q - 3 * s - 12) * (2 * q - 3 * s - 9)
        * (2 * q - 3 * s - 6),
    ]


def derive_telescoper() -> tuple[list[sp.Expr], bool]:
    """Re-derive sum a_i/P^i = H' + H(log J_s)' exactly."""
    degree = 10
    order = 4
    u_coefficients = sp.symbols(f"u0:{degree + 1}")
    recurrence_coefficients = sp.symbols(f"a0:{order + 1}")
    U = sum(value * z**index for index, value in enumerate(u_coefficients))
    # This is the parameter choice z_power=one_power=-1, p_power=3.
    H = U * z * (1 - z) / P**3
    log_derivative = -q / z + q / (1 - z) + (alpha - s) * sp.diff(P, z) / P
    recurrence = sum(
        value / P**index for index, value in enumerate(recurrence_coefficients)
    )
    numerator = sp.Poly(
        sp.together(sp.diff(H, z) + H * log_derivative - recurrence)
        .as_numer_denom()[0],
        z,
    )
    solution_set = sp.linsolve(
        numerator.all_coeffs(), (*u_coefficients, *recurrence_coefficients)
    )
    row = next(iter(solution_set))
    raw = row[-len(recurrence_coefficients):]
    common_denominator = sp.lcm([sp.denom(value) for value in raw])
    scaled = [sp.factor(value * common_denominator) for value in raw]
    content = sp.gcd_list(scaled)
    scaled = [sp.factor(value / content) for value in scaled]
    pivot = next(index for index, value in enumerate(raw) if value != 0)
    scale = sp.cancel(scaled[pivot] / raw[pivot])
    scaled_U = sp.expand(sum(
        sp.cancel(scale * row[index]) * z**index
        for index in range(len(u_coefficients))
    ))
    identity = sp.factor(sp.together(
        sp.diff(scaled_U * z * (1 - z) / P**3, z)
        + scaled_U * z * (1 - z) / P**3 * log_derivative
        - sum(scaled[index] / P**index for index in range(len(scaled)))
    ))
    expected = expected_recurrence()
    assert all(sp.expand(scaled[i] - expected[i]) == 0 for i in range(5))
    assert identity == 0
    return scaled, True


def verify_short_relation() -> dict[str, str | bool]:
    """Verify J_2+a J_1+b J_0 is an exact derivative."""
    a_value = -5 * (5 * q - 9) / (8 * (q - 3))
    b_value = (5 * q - 9) * (5 * q - 6) / (
        8 * (q - 3) * (2 * q - 3)
    )
    S = -3 * (
        -5 * q * z**3 - 5 * q * z**2 - 5 * q * z - 3 * q
        + 3 * z**4 + 9 * z**3 + 9 * z**2 + 9 * z + 3
    ) / (8 * (q - 3) * (2 * q - 3))
    H = z * (1 - z) * P * S
    log_j2 = -q / z + q / (1 - z) + (alpha - 2) * sp.diff(P, z) / P
    identity = sp.factor(sp.cancel(
        sp.diff(H, z) + H * log_j2
        - (1 + a_value * P + b_value * P**2)
    ))
    assert identity == 0
    return {
        "identity_zero": True,
        "a_in_B2_plus_aB1_plus_bB0": str(sp.factor(a_value)),
        "b_in_B2_plus_aB1_plus_bB0": str(sp.factor(b_value)),
        "certificate_S": str(sp.factor(S)),
    }


def recurrence_coefficients_integer(index: int, gap: int) -> list[int]:
    values = expected_recurrence()
    return [int(value.subs({s: index, q: gap})) for value in values]


def terminal_trace(gap: int, prime: int) -> dict[str, object]:
    exponent = (prime + 2 * gap - 3) // 3
    state = [0, 0, 0, 1]
    singular_rows: list[dict[str, object]] = []
    first_failure = None
    for index in range(exponent):
        coefficients = [
            value % prime for value in recurrence_coefficients_integer(index, gap)
        ]
        if coefficients[4] != 0:
            next_value = -sum(
                coefficients[offset] * state[index + offset]
                for offset in range(4)
            ) * pow(coefficients[4], -1, prime)
            state.append(next_value % prime)
        else:
            residual = sum(
                coefficients[offset] * state[index + offset]
                for offset in range(4)
            ) % prime
            singular_rows.append({
                "s": index,
                "coefficients_mod_p": coefficients,
                "state_window": state[index:index + 4],
                "residual": residual,
            })
            if residual != 0 and first_failure is None:
                first_failure = {"s": index, "residual": residual}
                break
            # At a consistent right-singular row the recurrence leaves the
            # next value free.  Zero is a deterministic witness choice.
            state.append(0)
    pochhammer = math.prod(2 * gap - 3 - 3 * j for j in range(gap - 1))
    return {
        "q": gap,
        "p": prime,
        "E": exponent,
        "pochhammer_mod_p": pochhammer % prime,
        "singular_rows": singular_rows,
        "first_failure": first_failure,
        "mode_survives_checked_rows": first_failure is None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    recurrence, identity_zero = derive_telescoper()
    leading = [sp.LC(sp.Poly(value, s)) for value in recurrence]
    x = sp.symbols("x")
    characteristic = sp.factor(sum(leading[i] * x**i for i in range(5)))
    expected_characteristic = -243 * (x - 1) * (4 * x - 1) * (
        16 * x**2 - 40 * x + 27
    )
    assert sp.expand(characteristic - expected_characteristic) == 0

    result = {
        "scope": "structure/no-go audit; not a fresh-prime nonvanishing proof",
        "telescoper_identity_zero": identity_zero,
        "recurrence_coefficients": [str(sp.factor(value)) for value in recurrence],
        "short_relation": verify_short_relation(),
        "asymptotic": {
            "leading_coefficients": [int(value) for value in leading],
            "characteristic_factorization": str(characteristic),
            "roots": ["1", "1/4", "(5+sqrt(-2))/4", "(5-sqrt(-2))/4"],
            "symmetric_cube_possible": False,
            "reason": (
                "A symmetric-cube root multiset has a pairing with equal "
                "products; none of the three pairings of these four roots does."
            ),
        },
        "terminal_traces": [
            terminal_trace(5, 11),
            terminal_trace(11, 659),
            terminal_trace(5, 17),
            terminal_trace(13, 97),
        ],
    }
    serialized = json.dumps(result, indent=2, sort_keys=True) + "\n"
    arguments.output.write_bytes(serialized.encode("utf-8"))


if __name__ == "__main__":
    main()
