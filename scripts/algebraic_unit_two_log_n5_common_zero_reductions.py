#!/usr/bin/env python3
"""Exact identities and finite diagnostics for the n=5 common-zero reductions.

The identities are proved in the companion Markdown source.  The scans here are
finite certificates only; no bounded scan is promoted to an all-degree theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp


Elt = tuple[int, int, int, int]
Pair = tuple[int, int]

ZERO: Elt = (0, 0, 0, 0)
ONE: Elt = (1, 0, 0, 0)
ZETA: Elt = (0, 1, 0, 0)
ETA: Elt = (0, -1, 0, -1)
U: Elt = (1, 1, 0, 0)  # 1+zeta=eta^{-1}
A_IN_E: Elt = (1, 0, -1, -1)  # A=2+zeta+zeta^{-1}


def add(a: Elt, b: Elt) -> Elt:
    return tuple(a[j] + b[j] for j in range(4))  # type: ignore[return-value]


def scale(n: int, a: Elt) -> Elt:
    return tuple(n * value for value in a)  # type: ignore[return-value]


def multiply(a: Elt, b: Elt) -> Elt:
    raw = [0] * 7
    for j, aj in enumerate(a):
        for k, bk in enumerate(b):
            raw[j + k] += aj * bk
    # zeta^4=-(1+zeta+zeta^2+zeta^3).
    for degree in range(6, 3, -1):
        value = raw[degree]
        for target in range(degree - 4, degree):
            raw[target] -= value
    return tuple(raw[:4])  # type: ignore[return-value]


def power(a: Elt, exponent: int) -> Elt:
    answer = ONE
    base = a
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        base = multiply(base, base)
        exponent //= 2
    return answer


def embed_a_pair(a: Pair) -> Elt:
    """Embed a[0]+a[1]*A, A=2+zeta+zeta^-1, into Z[zeta]."""

    return (a[0] + a[1], 0, -a[1], -a[1])


def multiply_by_a(a: Pair) -> Pair:
    """Multiply by A in Z[A], A^2=3A-1."""

    return (-a[1], a[0] + 3 * a[1])


def add_pair(a: Pair, b: Pair) -> Pair:
    return (a[0] + b[0], a[1] + b[1])


def scale_pair(n: int, a: Pair) -> Pair:
    return (n * a[0], n * a[1])


def multiply_pair(a: Pair, b: Pair) -> Pair:
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + 3 * a[1] * b[1])


def ideal_norm_a(a: Pair, b: Pair) -> int:
    """Norm of (a,b) in Z[A], using its 2 by 4 multiplication matrix."""

    columns = (a, multiply_by_a(a), b, multiply_by_a(b))
    divisor = 0
    for j, k in itertools.combinations(range(4), 2):
        minor = columns[j][0] * columns[k][1] - columns[k][0] * columns[j][1]
        divisor = math.gcd(divisor, abs(minor))
    return divisor


def multiply_by_t(a: Pair) -> Pair:
    """Multiply by t in Z[t], t^2+t-1=0."""

    return (a[1], a[0] - a[1])


def ideal_norm_t(a: Pair, b: Pair) -> int:
    columns = (a, multiply_by_t(a), b, multiply_by_t(b))
    divisor = 0
    for j, k in itertools.combinations(range(4), 2):
        minor = columns[j][0] * columns[k][1] - columns[k][0] * columns[j][1]
        divisor = math.gcd(divisor, abs(minor))
    return divisor


def determinant(columns: tuple[Elt, Elt, Elt, Elt]) -> int:
    """Fraction-free determinant of four integer columns."""

    matrix = [[columns[column][row] for column in range(4)] for row in range(4)]
    sign = 1
    denominator = 1
    for pivot_index in range(3):
        pivot_row = next(
            (row for row in range(pivot_index, 4) if matrix[row][pivot_index]),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            matrix[pivot_index], matrix[pivot_row] = matrix[pivot_row], matrix[pivot_index]
            sign = -sign
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, 4):
            for column in range(pivot_index + 1, 4):
                numerator = (
                    matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column]
                )
                if numerator % denominator:
                    raise AssertionError("Bareiss division was not exact")
                matrix[row][column] = numerator // denominator
        denominator = pivot
    return sign * matrix[3][3]


BASIS: tuple[Elt, Elt, Elt, Elt] = tuple(
    tuple(int(j == k) for j in range(4)) for k in range(4)
)  # type: ignore[assignment]


def ideal_norm_e(a: Elt, b: Elt) -> int:
    """Norm of (a,b) in Z[zeta_5], by exact determinantal divisors."""

    columns = tuple(multiply(a, basis) for basis in BASIS) + tuple(
        multiply(b, basis) for basis in BASIS
    )
    divisor = 0
    for indices in itertools.combinations(range(8), 4):
        chosen = tuple(columns[index] for index in indices)
        value = determinant(chosen)  # type: ignore[arg-type]
        divisor = math.gcd(divisor, abs(value))
        if divisor == 1:
            break
    return divisor


def h_ideal_is_proper_mod_p(current: Pair, previous: Pair, p: int) -> bool:
    """Properness of (current,previous) in F_p[A]/(A^2-3A+1)."""

    u, v = current
    r, s = previous
    norm_current = (u * u + 3 * u * v + v * v) % p
    norm_previous = (r * r + 3 * r * s + s * s) % p
    cross = (u * s - v * r) % p
    return norm_current == norm_previous == cross == 0


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(max_degree: int, pc_max_degree: int, max_prime: int) -> dict[str, object]:
    if max_degree < 205:
        raise ValueError("max-degree must be at least 205")
    if not 1 <= pc_max_degree <= max_degree:
        raise ValueError("pc-max-degree must lie between 1 and max-degree")
    if max_prime < 19:
        raise ValueError("max-prime must be at least 19")

    eta_bar = add(ONE, scale(-1, ETA))
    one_minus_zeta = add(ONE, scale(-1, ZETA))
    one_minus_u = add(ONE, scale(-1, U))
    one_plus_u = add(ONE, U)

    x_power = y_power = ONE
    p_x = p_y = ONE
    c_x = c_y = ZERO
    a_value = 1
    top_c = 0

    # h_0,h_1 and g_0,g_1 from their exact quadratic-denominator recurrences.
    h_previous_previous: Pair = (1, 0)
    h_previous: Pair = (1, -1)
    h_values: list[Pair] = [h_previous_previous, h_previous]
    g_previous_previous = ONE
    g_previous = scale(-1, U)
    g_values: list[Elt] = [g_previous_previous, g_previous]

    # Normalized constant and linear coefficients of F_d(lambda,u).
    r_previous = ONE
    s_previous = ZERO

    p_x_previous = p_y_previous = ONE
    k_previous = one_minus_zeta

    h_deviations: list[dict[str, int]] = []
    h_nontrivial_count = 0
    j_deviations: list[dict[str, int]] = []
    j_nontrivial_count = 0
    ap_deviations: list[dict[str, int]] = []
    pc_deviations: list[dict[str, int]] = []

    for d in range(1, max_degree + 1):
        x_power = multiply(x_power, ETA)
        y_power = multiply(y_power, eta_bar)
        p_x = add(x_power, scale(-d, p_x))
        p_y = add(y_power, scale(-d, p_y))
        top_c += a_value
        a_value = 1 - d * a_value
        c_x = add(scale(-d, c_x), scale(top_c, x_power))
        c_y = add(scale(-d, c_y), scale(top_c, y_power))

        if d >= 2:
            ah1 = multiply_by_a(h_previous)
            ah2 = multiply_by_a(h_previous_previous)
            h_current = add_pair(
                (1, 0),
                add_pair(scale_pair(-d, ah1), scale_pair(-d * (d - 1), ah2)),
            )
            h_values.append(h_current)
            h_previous_previous, h_previous = h_previous, h_current

            g_current = add(
                ONE,
                add(
                    scale(-d, multiply(one_plus_u, g_previous)),
                    scale(-d * (d - 1), multiply(U, g_previous_previous)),
                ),
            )
            g_values.append(g_current)
            g_previous_previous, g_previous = g_previous, g_current

        h_current = h_values[d]
        h_norm = ideal_norm_a(h_current, h_values[d - 1])
        h_expected = 19 if d % 19 == 15 else 1
        if h_norm != 1:
            h_nontrivial_count += 1
        if h_norm != h_expected:
            h_deviations.append({"d": d, "actual": h_norm, "expected": h_expected})

        # K_d(eta)=(1-zeta)*etabar^d*h_d.
        k_value = add(p_y, scale(-1, multiply(power(ZETA, d + 1), p_x)))
        h_value_in_e = embed_a_pair(h_current)
        k_expected = multiply(
            multiply(one_minus_zeta, y_power),
            h_value_in_e,
        )
        if k_value != k_expected:
            raise AssertionError(f"simultaneous-P normalization failed at d={d}")
        k_derivative = add(
            scale(d, multiply(ZETA, p_y_previous)),
            scale(-d, multiply(power(ZETA, d + 1), p_x_previous)),
        )
        k_derivative_expected = scale(d, multiply(ZETA, k_previous))
        if k_derivative != k_derivative_expected:
            raise AssertionError(f"K derivative identity failed at d={d}")

        # L_d(eta)=(1-u)*g_d for the a/P alternative.
        l_value = add((a_value, 0, 0, 0), scale(-1, multiply(power(U, d + 1), p_x)))
        if l_value != multiply(one_minus_u, g_values[d]):
            raise AssertionError(f"a/P normalization failed at d={d}")

        # Constant and linear lambda-coefficients in (21).
        r_current = add(ONE, scale(-d, multiply(U, r_previous)))
        s_current = add((top_c, 0, 0, 0), scale(-d, multiply(U, s_previous)))
        u_power = power(U, d)
        if r_current != multiply(u_power, p_x):
            raise AssertionError(f"F_d constant coefficient failed at d={d}")
        if s_current != multiply(u_power, c_x):
            raise AssertionError(f"F_d linear coefficient failed at d={d}")
        r_previous, s_previous = r_current, s_current

        # Five-step scalar recurrence (15).
        if d >= 5:
            kappa: Pair = (-2, 5)
            left = add_pair(
                h_current,
                scale_pair(-math.prod(range(d - 4, d + 1)), multiply_pair(kappa, h_values[d - 5])),
            )
            right = add_pair(
                (1, 0),
                add_pair(
                    scale_pair(-d, (0, 1)),
                    add_pair(
                        scale_pair(d * (d - 1), (-1, 2)),
                        scale_pair(d * (d - 1) * (d - 2), (1, -2)),
                    ),
                ),
            )
            if left != right:
                raise AssertionError(f"five-step recurrence failed at d={d}")

        # J_d=(N_d,a_d*T_d) in Z[t], t^2+t-1=0.
        n_raw = multiply(p_x, p_y)
        d_raw = add(multiply(p_x, c_y), scale(-1, multiply(p_y, c_x)))
        if n_raw[1] or n_raw[2] != n_raw[3]:
            raise AssertionError("N_d was not fixed by conjugation")
        if d_raw[1] != 2 * d_raw[0] or d_raw[2] + d_raw[3] != 2 * d_raw[0]:
            raise AssertionError("D_d was not anti-fixed")
        n_coordinates = (n_raw[0] - n_raw[2], -n_raw[2])
        at_coordinates = (
            a_value * d_raw[0],
            a_value * (d_raw[2] - d_raw[0]),
        )
        j_norm = ideal_norm_t(n_coordinates, at_coordinates)
        j_expected = 361 if d % 361 == 205 else (19 if d % 19 == 15 else 1)
        if j_norm != 1:
            j_nontrivial_count += 1
        if j_norm != j_expected:
            j_deviations.append({"d": d, "actual": j_norm, "expected": j_expected})

        # The rational norm detects any prime in (a_d,P_d(eta)).
        norm_p_x = n_coordinates[0] ** 2 - n_coordinates[0] * n_coordinates[1] - n_coordinates[1] ** 2
        ap_gcd = math.gcd(abs(a_value), abs(norm_p_x))
        if ap_gcd != 1:
            ap_deviations.append({"d": d, "gcd": ap_gcd})

        if d <= pc_max_degree:
            pc_norm = ideal_norm_e(p_x, c_x)
            if pc_norm != 1:
                pc_deviations.append({"d": d, "ideal_norm": pc_norm})

        p_x_previous, p_y_previous, k_previous = p_x, p_y, k_value

    modular_hits: list[dict[str, int]] = []
    for p in sp.primerange(3, max_prime + 1):
        if p == 5:
            continue
        h0: Pair = (1, 0)
        h1: Pair = (1, p - 1)
        for d in range(2, p):
            ah1 = (-h1[1] % p, (h1[0] + 3 * h1[1]) % p)
            ah0 = (-h0[1] % p, (h0[0] + 3 * h0[1]) % p)
            h2 = (
                (1 - d * ah1[0] - d * (d - 1) * ah0[0]) % p,
                (-d * ah1[1] - d * (d - 1) * ah0[1]) % p,
            )
            if h_ideal_is_proper_mod_p(h2, h1, p):
                modular_hits.append({"p": int(p), "d": d})
            h0, h1 = h1, h2

    expected_modular_hits = [{"p": 19, "d": 15}]
    if h_deviations or j_deviations or ap_deviations or pc_deviations:
        raise AssertionError(
            "finite exact scan deviated: "
            f"h={h_deviations}, J={j_deviations}, aP={ap_deviations}, PC={pc_deviations}"
        )
    if modular_hits != expected_modular_hits:
        raise AssertionError(f"unexpected modular hits: {modular_hits}")

    return {
        "description": "Exact common-zero identities and finite diagnostics on the n=5 two-log edge.",
        "bounds": {
            "exact_h_J_aP_max_degree": max_degree,
            "exact_PC_ideal_max_degree": pc_max_degree,
            "modular_h_max_prime": max_prime,
            "modular_h_degrees": "2<=d<p",
        },
        "identity_checks": {
            "K_and_h_normalization": True,
            "K_derivative_identity": True,
            "aP_and_g_normalization": True,
            "F_constant_and_linear_coefficients": True,
            "h_five_step_recurrence": True,
        },
        "finite_diagnostics": {
            "h_ideal_pattern": "norm 19 iff d == 15 (mod 19), otherwise norm 1",
            "h_nontrivial_count": h_nontrivial_count,
            "h_deviations": h_deviations,
            "J_ideal_pattern": "norm 361 iff d == 205 (mod 361), norm 19 at other d == 15 (mod 19), otherwise norm 1",
            "J_nontrivial_count": j_nontrivial_count,
            "J_deviations": j_deviations,
            "aP_rational_norm_gcd_deviations_from_1": ap_deviations,
            "PC_ideal_norm_deviations_from_1": pc_deviations,
            "modular_h_hits": modular_hits,
        },
        "scope_warning": (
            "All scans are finite diagnostics. They do not prove that 19 is the only possible "
            "prime, that 361 belongs to J_d for every d, or any statement about e+pi."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=1000)
    parser.add_argument("--pc-max-degree", type=int, default=300)
    parser.add_argument("--max-prime", type=int, default=5000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/algebraic_unit_two_log_n5_common_zero_reductions.json"),
    )
    args = parser.parse_args()
    result = run(args.max_degree, args.pc_max_degree, args.max_prime)
    script = Path(__file__).resolve()
    source = script.parent.parent / "sources" / "algebraic_unit_two_log_n5_common_zero_reductions.md"
    result["script_sha256"] = file_sha256(script)
    result["source_sha256"] = file_sha256(source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
