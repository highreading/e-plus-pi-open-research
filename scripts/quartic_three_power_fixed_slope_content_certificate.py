#!/usr/bin/env python3
"""Exact and diagnostic certificate for the fixed-slope L cross E branch."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from math import comb, factorial, gcd, lcm
from pathlib import Path

import mpmath as mp
import sympy as sp

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from quartic_multi_power_kernel_lattice_certificate import (  # noqa: E402
    primitive_integer_vector,
    raw_coordinate_numerators,
    rational_and_coordinates,
    triple_vector,
)


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0)")
    value = abs(value)
    return (value & -value).bit_length() - 1


def det3(rows: list[list[int]]) -> int:
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def coordinate_data(n: int, k: int) -> dict[str, list[Fraction]]:
    data = [rational_and_coordinates(n, k + s) for s in range(3)]
    rational = [entry[0] for entry in data]
    rows = [entry[1] for entry in data]
    logarithmic = [row[0] - row[2] for row in rows]
    positive = [row[0] + row[2] for row in rows]
    odd = [row[1] for row in rows]
    return {"R": rational, "L": logarithmic, "E": positive, "b": odd}


def primitive_cross_and_pair(n: int, k: int) -> tuple[list[int], Fraction, Fraction, list[int]]:
    data = coordinate_data(n, k)
    cross = primitive_integer_vector(triple_vector(data["L"], data["E"]))
    rational = sum((cross[s] * data["R"][s] for s in range(3)), Fraction())
    pi_coefficient = sum(
        (cross[s] * data["b"][s] / 8 for s in range(3)), Fraction()
    )
    pair = primitive_integer_vector([rational, pi_coefficient])
    return cross, rational, pi_coefficient, pair


def universal_delta(n: int, k: int) -> int:
    odd_lcm_k = 1
    for value in range(1, k):
        odd_lcm_k = lcm(odd_lcm_k, value)
    endpoint_lcm = 1
    for value in range(1, 2 * n + 2):
        endpoint_lcm = lcm(endpoint_lcm, value)
    exponent = 3 * (k - 1) - (k - 1).bit_count() + k
    return 2**exponent * odd_lcm_k * endpoint_lcm


def cleared_determinant_pair(n: int, k: int) -> tuple[int, int, int]:
    data = coordinate_data(n, k)
    columns = []
    for s in range(3):
        delta = universal_delta(n, k + s)
        values = [data[name][s] for name in ("L", "E", "R", "b")]
        if any((value * delta).denominator != 1 for value in values):
            raise AssertionError((n, k, s, values, delta))
        columns.append([int(value * delta) for value in values])
    rows = [[columns[s][row] for s in range(3)] for row in range(4)]
    u_value = det3([rows[0], rows[1], rows[2]])
    v_value = det3([rows[0], rows[1], rows[3]])
    content = gcd(abs(8 * u_value), abs(v_value))
    return 8 * u_value, v_value, content


def symbolic_checks() -> dict[str, bool]:
    u, v, x, y, p, m = sp.symbols("u v x y p m", real=True)
    z = u + sp.I * v
    g = x + sp.I * y
    real_row = sp.Matrix([[sp.re(sp.expand(z * g**j)) for j in range(3)]])
    imag_row = sp.Matrix([[sp.im(sp.expand(z * g**j)) for j in range(3)]])
    p_row = sp.Matrix([[p**j for j in range(3)]])
    m_row = sp.Matrix([[m**j for j in range(3)]])
    quadrature = sp.expand(sp.Matrix.vstack(real_row, p_row, imag_row).det())
    real_value = sp.expand(sp.Matrix.vstack(real_row, p_row, m_row).det())

    a, b = sp.symbols("a b", real=True)
    transition_real = sp.expand(
        sp.re((a + sp.I * b) ** 4 - 2 * sp.I * (a + sp.I * b) - 1)
    )
    transition_imag = sp.expand(
        sp.im((a + sp.I * b) ** 4 - 2 * sp.I * (a + sp.I * b) - 1)
    )
    substituted = sp.factor(
        transition_real.subs(a**2, b**2 + 1 / (2 * b))
    )

    return {
        "quadrature_determinant": sp.expand(
            quadrature - (-y) * (u**2 + v**2) * ((p - x) ** 2 + y**2)
        )
        == 0,
        "real_value_determinant": sp.expand(
            real_value - sp.re(sp.expand(z * (p - g) * (m - g) * (m - p)))
        )
        == 0,
        "transition_real_equation": transition_real
        == a**4 - 6 * a**2 * b**2 + b**4 + 2 * b - 1,
        "transition_imag_equation": transition_imag
        == 4 * a**3 * b - 4 * a * b**3 - 2 * a,
        "transition_b_elimination": sp.factor(
            substituted + (16 * b**6 + 4 * b**2 - 1) / (4 * b**2)
        )
        == 0,
    }


def boundary_b_formula(m: int) -> Fraction:
    total = Fraction()
    for h in range(m):
        total += Fraction(
            comb(4 * m, 4 * h + 1)
            * factorial(2 * m - 2 * h)
            * factorial(2 * m + 2 * h),
            factorial(m - h)
            * factorial(m + h)
            * factorial(2 * m),
        )
    return -total / 4 ** (2 * m)


def raw_even_pair(m: int, K: int) -> tuple[int, int]:
    """Raw (L,E) pair for P_K(D)F_m, before division by 4^K K!."""
    a_value, _, c_value, _ = raw_coordinate_numerators(4 * m, K + 1)
    return a_value - c_value, a_value + c_value


def raw_even_moment_pair(m: int, K: int, power: int) -> tuple[int, int]:
    """Raw even pair after inserting D^power before P_K(D)."""
    n = 4 * m
    out = [0, 0, 0, 0]
    for j in range(n + 1):
        exponent = n + j
        product = math.prod(4 * s - exponent - 1 for s in range(1, K + 1))
        quotient, residue = divmod(exponent, 4)
        out[residue] += (
            (-1) ** (j + quotient)
            * comb(n, j)
            * product
            * exponent**power
        )
    return out[0] - out[2], out[0] + out[2]


def quartic_refinement_table_audit() -> dict[str, object]:
    expected = {
        (1, 0): ((3, 5), (1, 3)), (1, 1): ((7, 5), (3, 1)),
        (1, 2): ((7, 1), (1, 3)), (1, 3): ((3, 1), (3, 1)),
        (2, 0): ((7, 7), (3, 3)), (2, 1): ((7, 7), (5, 1)),
        (2, 2): ((7, 7), (7, 7)), (2, 3): ((7, 7), (1, 5)),
        (3, 0): ((5, 3), (3, 1)), (3, 1): ((1, 3), (1, 3)),
        (3, 2): ((1, 7), (3, 1)), (3, 3): ((5, 7), (1, 3)),
        (0, 0): ((1, 1), (1, 1)), (0, 1): ((1, 1), (7, 3)),
        (0, 2): ((1, 1), (5, 5)), (0, 3): ((1, 1), (3, 7)),
    }
    def ring_mul(left: tuple[int, ...], right: tuple[int, ...], modulus: int) -> tuple[int, ...]:
        product = [0] * 7
        for i, left_value in enumerate(left):
            for j, right_value in enumerate(right):
                product[i + j] += left_value * right_value
        for degree in range(6, 3, -1):
            product[degree - 4] -= product[degree]
        return tuple(value % modulus for value in product[:4])

    def ring_power(value: tuple[int, ...], exponent: int, modulus: int) -> tuple[int, ...]:
        result = (1, 0, 0, 0)
        base = tuple(entry % modulus for entry in value)
        while exponent:
            if exponent & 1:
                result = ring_mul(result, base, modulus)
            base = ring_mul(base, base, modulus)
            exponent //= 2
        return result

    def h_derivative(order: int, modulus: int) -> tuple[int, ...]:
        if order == 0:
            return (0, 2 % modulus, -3 % modulus, 2 % modulus)
        return (
            ((8**order - 4**order) // 2) % modulus,
            (2 * 5**order) % modulus,
            (-3 * 6**order) % modulus,
            (2 * 7**order) % modulus,
        )

    failures = []
    for m in range(1, 9):
        for K in range(8):
            constant = math.prod(4 * s - 1 for s in range(1, K + 1))
            inverse = pow(constant, -1, 8)
            pair_0 = raw_even_moment_pair(m, K, 0)
            pair_2 = raw_even_moment_pair(m, K, 2)
            a_pair = tuple((value // 2**m * inverse) % 8 for value in pair_0)
            b_pair = tuple(
                (value // (4 * m * 2**m) * inverse) % 8 for value in pair_2
            )
            observed = (a_pair, b_pair)
            target = expected[(m % 4, K % 4)]
            determinant = (a_pair[0] * b_pair[1] - a_pair[1] * b_pair[0]) % 8
            if observed != target or determinant != 4 * ((m + K) % 2):
                failures.append(
                    {
                        "m": m,
                        "K": K,
                        "observed": observed,
                        "expected": target,
                        "determinant_mod_8": determinant,
                    }
                )
    h_zero = h_derivative(0, 32)
    h_zero_fourth = ring_power(h_zero, 4, 32)
    expected_h_zero_fourth = tuple(
        value % 32 for value in (577, -408, 0, 408)
    )
    special_rho_failures = []
    h_fourth_minus_one = tuple(
        (h_zero_fourth[index] - (1 if index == 0 else 0)) % 32
        for index in range(4)
    )
    # Modulo 32 the proof reduces a to its parity and s to s=1 or s>=2.
    for exponent in range(2):
        for order in (1, 2):
            product = ring_mul(
                ring_mul(ring_power(h_zero, exponent, 32), h_fourth_minus_one, 32),
                h_derivative(order, 32),
                32,
            )
            rho_value = ((product[0] - product[2]) % 32, (product[0] + product[2]) % 32)
            if rho_value != (0, 0):
                special_rho_failures.append((exponent, order, rho_value))

    four_block_failures = []
    for k_mod in range(4):
        for even_lambda in range(0, 16, 2):
            ratio = 1
            for offset in range(1, 5):
                denominator = 4 * (k_mod + offset) - 1
                ratio = (
                    ratio
                    * (1 - even_lambda * pow(denominator, -1, 16))
                ) % 16
            if ratio != 1:
                four_block_failures.append((k_mod, even_lambda, ratio))

    return {
        "component_table": {
            f"m{m_mod}_K{K_mod}": [list(pair[0]), list(pair[1])]
            for (m_mod, K_mod), pair in sorted(expected.items())
        },
        "failures_for_1_le_m_le_8_0_le_K_le_7": failures,
        "determinant_formula": "det(A_mK,B_mK) == 4*(m+K) mod 8",
        "proof_modulus_before_division_by_4m": 32,
        "h0_fourth_mod_32": list(h_zero_fourth),
        "h0_fourth_exact_residue_expected": list(expected_h_zero_fourth),
        "h0_fourth_identity_holds": h_zero_fourth == expected_h_zero_fourth,
        "special_rho_mod_32_failures": special_rho_failures,
        "four_successive_Q_factors_mod_16_failures": four_block_failures,
    }


def raw_wronskian_theorem_scan(m_max: int) -> dict[str, object]:
    """Finite audit of Lemma 7.1; the proof itself is in the source note."""
    failures = []
    selected = []
    for m in range(1, m_max + 1):
        expected_adjacent = 2 * m + 2 + v2(m)
        expected_skip = expected_adjacent + 1
        for K in range(0, 2 * m + 3):
            pair_0 = raw_even_pair(m, K)
            pair_1 = raw_even_pair(m, K + 1)
            pair_2 = raw_even_pair(m, K + 2)
            determinant_01 = pair_0[0] * pair_1[1] - pair_0[1] * pair_1[0]
            determinant_02 = pair_0[0] * pair_2[1] - pair_0[1] * pair_2[0]
            observed = {
                "pair_v2": [v2(pair_0[0]), v2(pair_0[1])],
                "adjacent_minor_v2": v2(determinant_01),
                "skip_minor_v2": v2(determinant_02),
            }
            expected = {
                "pair_v2": [m, m],
                "adjacent_minor_v2": expected_adjacent,
                "skip_minor_v2": expected_skip,
            }
            if observed != expected:
                failures.append(
                    {"m": m, "K": K, "observed": observed, "expected": expected}
                )
        if m in (1, 2, 4, 8, 16, m_max):
            selected.append(
                {
                    "m": m,
                    "K_range": [0, 2 * m + 2],
                    "pair_v2": [m, m],
                    "adjacent_minor_v2": expected_adjacent,
                    "skip_minor_v2": expected_skip,
                }
            )
    return {
        "m_max": m_max,
        "failures": failures,
        "selected_records": selected,
        "status": (
            "Finite audit of the all-m raw Wronskian theorem proved in the source."
        ),
    }


def boundary_exact_scan(m_max: int) -> dict[str, object]:
    endpoint_pattern_failures: list[dict[str, object]] = []
    cross_theorem_failures: list[dict[str, object]] = []
    formula_failures = []
    records = []
    for m in range(1, m_max + 1):
        n, k = 4 * m, 2 * m + 1
        cross, rational, pi_coefficient, pair = primitive_cross_and_pair(n, k)
        b0 = coordinate_data(n, k)["b"][0]
        if m <= 16 and b0 != boundary_b_formula(m):
            formula_failures.append(m)
        observed = {
            "cross_v2": [v2(value) for value in cross],
            "rational_denominator_v2": v2(rational.denominator),
            "pi_denominator_v2": v2(pi_coefficient.denominator),
        }
        expected = {
            "cross_v2": [0, 3, 5 + v2(m + 1)],
            "rational_denominator_v2": m + 1 + m.bit_count(),
            "pi_denominator_v2": 3 * m - m.bit_count() + 2 - v2(m),
        }
        if observed["cross_v2"] != expected["cross_v2"]:
            cross_theorem_failures.append(
                {"m": m, "observed": observed["cross_v2"], "expected": expected["cross_v2"]}
            )
        endpoint_observed = {
            key: observed[key]
            for key in ("rational_denominator_v2", "pi_denominator_v2")
        }
        endpoint_expected = {
            key: expected[key]
            for key in ("rational_denominator_v2", "pi_denominator_v2")
        }
        if endpoint_observed != endpoint_expected:
            endpoint_pattern_failures.append(
                {"m": m, "observed": endpoint_observed, "expected": endpoint_expected}
            )
        if m in (1, 2, 4, 8, 16, m_max):
            records.append(
                {
                    "m": m,
                    "n": n,
                    **observed,
                    "primitive_cross_max_bits": max(abs(value).bit_length() for value in cross),
                    "primitive_pair_max_bits": max(abs(value).bit_length() for value in pair),
                }
            )
    return {
        "m_max": m_max,
        "boundary_formula_failures_through_m16": formula_failures,
        "proved_cross_theorem_failures": cross_theorem_failures,
        "conjectural_endpoint_pattern_failures": endpoint_pattern_failures,
        "selected_records": records,
        "status": (
            "The cross-vector law is proved in the source; the terminating formula is exact; "
            "the endpoint A,B valuation laws remain conjectural."
        ),
    }


def saddle_record(kappa: float) -> dict[str, str | float]:
    mp.mp.dps = 80
    kap = mp.mpf(str(kappa))
    x_minus = mp.findroot(
        lambda x: 1 / x - 1 / (1 - x) - 4 * kap * x**3 / (1 + x**4),
        mp.mpf("0.47") if kap < 0.7 else (4 * kap) ** (-mp.mpf(1) / 4) * mp.mpf("0.8"),
    )
    y_plus = mp.findroot(
        lambda y: 1 / y + 1 / (1 + y) - 4 * kap * y**3 / (1 + y**4),
        mp.mpf("1.4") if kap < 0.7 else (4 * kap) ** (-mp.mpf(1) / 4) * mp.mpf("1.2"),
    )
    z_complex = mp.findroot(
        lambda z: 1 / z + mp.j / (1 + mp.j * z) - 4 * kap * z**3 / (1 + z**4),
        (4 * kap) ** (-mp.mpf(1) / 4) * (1 + mp.mpf("0.3") * mp.j),
    )
    j_rate = mp.log(x_minus) + mp.log(1 - x_minus) - kap * mp.log(1 + x_minus**4)
    e_rate = mp.log(y_plus) + mp.log(1 + y_plus) - kap * mp.log(1 + y_plus**4)
    ell_rate = mp.re(
        mp.log(z_complex)
        + mp.log(1 + mp.j * z_complex)
        - kap * mp.log(1 + z_complex**4)
    )
    delta = 4 * kap * mp.log(2) + kap + 2
    full_rate = 3 * delta + e_rate + ell_rate + j_rate
    return {
        "kappa": kappa,
        "x_minus": mp.nstr(x_minus, 25),
        "y_plus": mp.nstr(y_plus, 25),
        "z_complex": mp.nstr(z_complex, 25),
        "j_rate": mp.nstr(j_rate, 25),
        "e_rate": mp.nstr(e_rate, 25),
        "ell_rate": mp.nstr(ell_rate, 25),
        "approximation_exponent_ell_minus_j": mp.nstr(ell_rate - j_rate, 25),
        "universal_fully_cleared_rate": mp.nstr(full_rate, 25),
    }


def exact_diagnostics() -> list[dict[str, object]]:
    mp.mp.dps = 220
    output = []
    for n, k in ((20, 11), (40, 21), (60, 31), (40, 30), (40, 40), (40, 80)):
        cross, rational, pi_coefficient, pair = primitive_cross_and_pair(n, k)
        error = abs(
            mp.pi
            + (mp.mpf(rational.numerator) / rational.denominator)
            / (mp.mpf(pi_coefficient.numerator) / pi_coefficient.denominator)
        )
        value = mp.mpf(pair[0]) + mp.mpf(pair[1]) * mp.pi
        output.append(
            {
                "n": n,
                "k": k,
                "kappa": k / n,
                "normalized_error_log_over_n": mp.nstr(mp.log(error) / n, 18),
                "primitive_value_log_over_n": mp.nstr(mp.log(abs(value)) / n, 18),
                "primitive_pi_height_log_over_n": mp.nstr(mp.log(abs(pair[1])) / n, 18),
                "primitive_cross_max_bits": max(abs(value).bit_length() for value in cross),
            }
        )
    return output


def clearing_checks() -> list[dict[str, object]]:
    records = []
    for n, k in ((4, 3), (8, 5), (12, 7), (12, 10), (16, 16)):
        p_full, q_full, content = cleared_determinant_pair(n, k)
        _, _, _, direct_pair = primitive_cross_and_pair(n, k)
        matrix_pair = [p_full // content, q_full // content]
        same = matrix_pair == direct_pair or matrix_pair == [-value for value in direct_pair]
        records.append(
            {
                "n": n,
                "k": k,
                "integer_pair_identity": same,
                "full_pair_content_bits": content.bit_length(),
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "quartic_three_power_fixed_slope_content_certificate.json",
    )
    parser.add_argument("--boundary-m-max", type=int, default=30)
    args = parser.parse_args()

    symbolic = symbolic_checks()
    boundary = boundary_exact_scan(args.boundary_m_max)
    raw_wronskian = raw_wronskian_theorem_scan(args.boundary_m_max)
    refinement_table = quartic_refinement_table_audit()
    clearing = clearing_checks()
    if not all(symbolic.values()):
        raise AssertionError(symbolic)
    if boundary["boundary_formula_failures_through_m16"]:
        raise AssertionError(boundary)
    if boundary["proved_cross_theorem_failures"] or raw_wronskian["failures"]:
        raise AssertionError((boundary, raw_wronskian))
    if refinement_table["failures_for_1_le_m_le_8_0_le_K_le_7"]:
        raise AssertionError(refinement_table)
    if (
        not refinement_table["h0_fourth_identity_holds"]
        or refinement_table["special_rho_mod_32_failures"]
        or refinement_table["four_successive_Q_factors_mod_16_failures"]
    ):
        raise AssertionError(refinement_table)
    if any(not record["integer_pair_identity"] for record in clearing):
        raise AssertionError(clearing)

    result = {
        "schema": "quartic-three-power-fixed-slope-content-v1",
        "symbolic_checks": symbolic,
        "transition_and_fixed_slope_saddles": [
            saddle_record(value) for value in (0.5, 0.55, 0.75, 1.0, 2.0, 4.0)
        ],
        "exact_clearing_checks": clearing,
        "boundary_exact_and_dyadic_diagnostic": boundary,
        "raw_wronskian_theorem_finite_audit": raw_wronskian,
        "quartic_refinement_mod_8_table_audit": refinement_table,
        "exact_primitive_diagnostics": exact_diagnostics(),
        "warnings": [
            "The raw Wronskian and primitive cross-vector dyadic laws are proved in the source; their finite audit is not the proof.",
            "The boundary hypergeometric formula is exact, but the endpoint A,B valuation laws remain finite diagnostics.",
            "The saddle numbers certify algebraic stationary equations numerically; the theorem in the source retains its projected-contour hypothesis.",
            "Universal full clearing is not primitive clearing; the determinant gcd may remove an exponential factor.",
            "Nothing in this certificate classifies e+pi.",
        ],
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(hashlib.sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    main()
