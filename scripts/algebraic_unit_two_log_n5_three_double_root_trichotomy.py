#!/usr/bin/env python3
"""Exact checks for the three prescribed-double-root formulations.

The all-parameter proofs are in the companion Markdown source.  Prime scans
here are finite diagnostics and are never promoted to classification theorems.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import algebraic_unit_two_log_n5_p_boundary_obstruction as base


Elt = base.Elt


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def esub(x: Elt, y: Elt, prime: int) -> Elt:
    return base.eaddm(x, base.escalem(-1, y, prime), prime)


def polynomial_value(coefficients: list[Elt], argument: Elt, prime: int) -> Elt:
    answer = base.EZERO
    for coefficient in reversed(coefficients):
        answer = base.eaddm(
            base.emulm(answer, argument, prime), coefficient, prime
        )
    return answer


def polynomial_derivative_value(
    coefficients: list[Elt], argument: Elt, prime: int
) -> Elt:
    answer = base.EZERO
    for j in range(len(coefficients) - 1, 0, -1):
        answer = base.eaddm(
            base.emulm(answer, argument, prime),
            base.escalem(j, coefficients[j], prime),
            prime,
        )
    return answer


def w_coefficients(m: int, d: int, factorial: list[int]) -> list[Elt]:
    return [(factorial[m + j], 0, 0, 0) for j in range(d + 1)]


def h_coefficients(
    w_coeffs: list[Elt],
    c: Elt,
    c_inverse: Elt,
    prime: int,
) -> list[Elt]:
    answer: list[Elt] = []
    c_power = base.EONE
    for coefficient in w_coeffs:
        answer.append(
            base.emulm(
                coefficient,
                esub(c_power, c_inverse, prime),
                prime,
            )
        )
        c_power = base.emulm(c_power, c, prime)
    return answer


def verify_general_h(
    p: int,
    m: int,
    d: int,
    factorial: list[int],
    c: Elt,
    c_inverse: Elt,
    r: Elt,
    cr: Elt,
) -> None:
    w_coeffs = w_coefficients(m, d, factorial)
    h_coeffs = h_coefficients(w_coeffs, c, c_inverse, p)
    c_inverse_minus_one = esub(c_inverse, base.EONE, p)
    w_multiplier = base.emulm(c_inverse, c_inverse_minus_one, p)

    # Full coefficientwise identity (7).
    for k in range(d + 2):
        lhs = (
            base.escalem(k - 1, h_coeffs[k - 1], p)
            if 2 <= k <= d + 1
            else base.EZERO
        )
        rhs = base.EZERO
        if k <= d:
            rhs = base.eaddm(
                rhs, base.emulm(c_inverse, h_coeffs[k], p), p
            )
            rhs = base.eaddm(
                rhs, base.emulm(w_multiplier, w_coeffs[k], p), p
            )
        if 1 <= k <= d + 1:
            rhs = base.eaddm(
                rhs, base.escalem(-(m + 1), h_coeffs[k - 1], p), p
            )
        if lhs != rhs:
            raise AssertionError(
                f"general H identity failed at p={p}, m={m}, d={d}, k={k}"
            )

    w_r = polynomial_value(w_coeffs, r, p)
    w_cr = polynomial_value(w_coeffs, cr, p)
    h_r = polynomial_value(h_coeffs, r, p)
    h_prime_r = polynomial_derivative_value(h_coeffs, r, p)

    if h_r != esub(w_cr, base.emulm(c_inverse, w_r, p), p):
        raise AssertionError(f"H value recovery failed at p={p}, m={m}")

    left = base.emulm(c_inverse_minus_one, w_r, p)
    cr2 = base.emulm(c, base.emulm(r, r, p), p)
    one_minus_factor = esub(
        base.EONE,
        base.escalem(m + 1, base.emulm(c, r, p), p),
        p,
    )
    right = esub(
        base.emulm(cr2, h_prime_r, p),
        base.emulm(one_minus_factor, h_r, p),
        p,
    )
    if left != right:
        raise AssertionError(f"W reverse recovery failed at p={p}, m={m}")


def elt_ideal_is_proper_mod_p(x: Elt, y: Elt, prime: int) -> bool:
    """Whether x,y share a prime in F_p[zeta_5]."""

    variable = sp.symbols("z")
    cyclotomic = sp.Poly(
        variable**4 + variable**3 + variable**2 + variable + 1,
        variable,
        modulus=prime,
    )
    poly_x = sp.Poly(sum(x[j] * variable**j for j in range(4)), variable, modulus=prime)
    poly_y = sp.Poly(sum(y[j] * variable**j for j in range(4)), variable, modulus=prime)
    common = sp.gcd(cyclotomic, sp.gcd(poly_x, poly_y))
    return common.degree() > 0


def prime_checks(prime: int) -> tuple[list[dict[str, int]], list[dict[str, int]]]:
    factorial = [1]
    for n in range(1, prime):
        factorial.append(factorial[-1] * n % prime)
    inverse_factorial = [pow(value, -1, prime) for value in factorial]

    zeta_inverse = base.epowm(base.ZETA, 4, prime)
    if base.emulm(base.U, base.ETA, prime) != base.EONE:
        raise AssertionError("u inverse was not eta")

    # P_d(1), P_d(x), C_d(x), and the F_d constant/linear coefficients.
    p_one_values = [1]
    p_x_values = [base.EONE]
    c_x_values = [base.EZERO]
    f_constant_values = [base.EONE]
    f_linear_values = [base.EZERO]
    x_powers = [base.EONE]
    u_powers = [base.EONE]
    a_previous = 1
    top_c_previous = 0
    a_p_hits: list[dict[str, int]] = []
    pc_hits: list[dict[str, int]] = []

    for d in range(1, prime):
        x_powers.append(base.emulm(x_powers[-1], base.ETA, prime))
        u_powers.append(base.emulm(u_powers[-1], base.U, prime))
        top_c = (top_c_previous + a_previous) % prime
        a_current = (1 - d * a_previous) % prime
        p_x_current = base.eaddm(
            x_powers[d], base.escalem(-d, p_x_values[-1], prime), prime
        )
        c_x_current = base.eaddm(
            base.escalem(-d, c_x_values[-1], prime),
            base.escalem(top_c, x_powers[d], prime),
            prime,
        )
        f_constant = base.eaddm(
            base.EONE,
            base.escalem(
                -d, base.emulm(base.U, f_constant_values[-1], prime), prime
            ),
            prime,
        )
        f_linear = base.eaddm(
            (top_c, 0, 0, 0),
            base.escalem(
                -d, base.emulm(base.U, f_linear_values[-1], prime), prime
            ),
            prime,
        )
        if f_constant != base.emulm(u_powers[d], p_x_current, prime):
            raise AssertionError(f"F constant identity failed at p={prime}, d={d}")
        if f_linear != base.emulm(u_powers[d], c_x_current, prime):
            raise AssertionError(f"F linear identity failed at p={prime}, d={d}")

        p_one_values.append(a_current)
        p_x_values.append(p_x_current)
        c_x_values.append(c_x_current)
        f_constant_values.append(f_constant)
        f_linear_values.append(f_linear)
        if a_current == 0 and elt_ideal_is_proper_mod_p(p_x_current, base.EZERO, prime):
            a_p_hits.append({"p": prime, "d": d})
        if elt_ideal_is_proper_mod_p(p_x_current, c_x_current, prime):
            pc_hits.append({"p": prime, "d": d})
        a_previous = a_current
        top_c_previous = top_c

    # d=0 is included in the H and complementary identities.
    for d in range(prime):
        m = prime - 1 - d
        verify_general_h(
            prime,
            m,
            d,
            factorial,
            zeta_inverse,
            base.ZETA,
            base.U,
            base.V,
        )
        verify_general_h(
            prime,
            m,
            d,
            factorial,
            base.U,
            base.ETA,
            base.EONE,
            base.U,
        )

        coeffs = w_coefficients(m, d, factorial)
        w_one = polynomial_value(coeffs, base.EONE, prime)
        w_u = polynomial_value(coeffs, base.U, prime)
        expected_one = (p_one_values[d] * factorial[m]) % prime
        expected_u = base.escalem(
            factorial[m],
            base.emulm(base.epowm(base.U, d, prime), p_x_values[d], prime),
            prime,
        )
        if w_one != (expected_one, 0, 0, 0):
            raise AssertionError(f"P(1) complementary factor failed at p={prime}, d={d}")
        if w_u != expected_u:
            raise AssertionError(f"P(x) complementary factor failed at p={prime}, d={d}")
        # Also check the displayed inverse-factor form directly.
        recovered_x = base.emulm(
            base.epowm(base.ETA, d, prime),
            base.escalem(inverse_factorial[m], w_u, prime),
            prime,
        )
        if recovered_x != p_x_values[d]:
            raise AssertionError(f"inverse complementary factor failed at p={prime}, d={d}")

    return a_p_hits, pc_hits


def full_discriminant_false_positives() -> dict[str, object]:
    variable = sp.symbols("Z")

    # PP and a/P branches at p=31,d=18,m=12.
    prime = 31
    d = 18
    m = 12
    zeta = 16
    u = 17
    zeta_inverse = pow(zeta, -1, prime)
    u_inverse = pow(u, -1, prime)
    factorial = [1]
    for n in range(1, prime):
        factorial.append(factorial[-1] * n % prime)

    h_poly = sp.Poly(
        sum(
            factorial[m + j]
            * (pow(zeta_inverse, j, prime) - zeta)
            * variable**j
            for j in range(d + 1)
        ),
        variable,
        modulus=prime,
    )
    g_poly = sp.Poly(
        sum(
            factorial[m + j]
            * (pow(u, j, prime) - u_inverse)
            * variable**j
            for j in range(d + 1)
        ),
        variable,
        modulus=prime,
    )
    expected_gcd = sp.Poly(variable - 8, variable, modulus=prime)
    if sp.gcd(h_poly, h_poly.diff()).monic() != expected_gcd:
        raise AssertionError("PP full-discriminant false positive changed")
    if sp.gcd(g_poly, g_poly.diff()).monic() != expected_gcd:
        raise AssertionError("aP full-discriminant false positive changed")
    h_jet = (int(h_poly.eval(u)) % prime, int(h_poly.diff().eval(u)) % prime)
    g_jet = (int(g_poly.eval(1)) % prime, int(g_poly.diff().eval(1)) % prime)
    if h_jet != (26, 19) or g_jet != (1, 1):
        raise AssertionError(f"wrong prescribed jets: H={h_jet}, G={g_jet}")

    # Parameter branch at p=11,d=4,u=5, constructed from its EGF recurrence.
    lambda_variable = sp.symbols("lambda")
    parameter_prime = 11
    parameter_u = 5
    parameter_f = sp.Poly(1, lambda_variable, modulus=parameter_prime)
    for degree in range(1, 5):
        ch = sp.Poly(0, lambda_variable, modulus=parameter_prime)
        falling_poly = sp.Poly(1, lambda_variable, modulus=parameter_prime)
        falling_degree = 1
        for k in range(degree + 1):
            if k:
                falling_poly *= sp.Poly(
                    lambda_variable - (k - 1),
                    lambda_variable,
                    modulus=parameter_prime,
                )
                falling_degree = falling_degree * (degree - k + 1) % parameter_prime
            coefficient = (
                falling_degree
                * pow(int(sp.factorial(k)) % parameter_prime, -1, parameter_prime)
            ) % parameter_prime
            ch += falling_poly.mul_ground(coefficient)
        parameter_f = ch - parameter_f.mul_ground(
            parameter_u * degree % parameter_prime
        )
    expected_f = sp.Poly(
        lambda_variable**4
        - 3 * lambda_variable**2
        - lambda_variable
        + 5,
        lambda_variable,
        modulus=parameter_prime,
    )
    if parameter_f != expected_f:
        raise AssertionError(f"parameter false-positive polynomial changed: {parameter_f}")
    parameter_gcd = sp.gcd(parameter_f, parameter_f.diff()).monic()
    if parameter_gcd != sp.Poly(
        lambda_variable - 4, lambda_variable, modulus=parameter_prime
    ):
        raise AssertionError(f"parameter gcd changed: {parameter_gcd}")
    parameter_jet = (
        int(parameter_f.eval(0)) % parameter_prime,
        int(parameter_f.diff().eval(0)) % parameter_prime,
    )
    if parameter_jet != (5, 10):
        raise AssertionError(f"parameter prescribed jet changed: {parameter_jet}")

    return {
        "PP": {
            "p": 31,
            "d": 18,
            "m": 12,
            "zeta": 16,
            "prescribed_point": 17,
            "unrelated_double_root": 8,
            "prescribed_jet": list(h_jet),
        },
        "aP": {
            "p": 31,
            "d": 18,
            "m": 12,
            "u": 17,
            "prescribed_point": 1,
            "unrelated_double_root": 8,
            "prescribed_jet": list(g_jet),
        },
        "PC": {
            "p": 11,
            "d": 4,
            "u": 5,
            "prescribed_point": 0,
            "unrelated_double_root": 4,
            "prescribed_jet": list(parameter_jet),
        },
    }


def run(max_prime: int) -> dict[str, object]:
    if max_prime < 19:
        raise ValueError("max-prime must be at least 19")
    ap_hits: list[dict[str, int]] = []
    pc_hits: list[dict[str, int]] = []
    prime_count = 0
    for prime_value in sp.primerange(3, max_prime + 1):
        prime = int(prime_value)
        if prime == 5:
            continue
        prime_count += 1
        prime_ap, prime_pc = prime_checks(prime)
        ap_hits.extend(prime_ap)
        pc_hits.extend(prime_pc)

    return {
        "description": "Exact general-H and three prescribed-double-root trichotomy checks.",
        "bounds": {
            "odd_primes_other_than_5_max": max_prime,
            "prime_count": prime_count,
            "all_base_degrees": "0<=d<p",
        },
        "identity_checks": {
            "general_H_polynomial_differential_identity": True,
            "general_H_value_and_reverse_recovery": True,
            "PP_specialization_r_u_c_zeta_inverse": True,
            "aP_specialization_r_1_c_u": True,
            "complementary_unit_factors": True,
            "F_lambda_constant_and_linear_coefficients": True,
            "shared_prescribed_first_jet_data": True,
        },
        "finite_diagnostics": {
            "aP_common_prime_hits": ap_hits,
            "PC_common_prime_hits": pc_hits,
        },
        "exact_full_discriminant_false_positives": (
            full_discriminant_false_positives()
        ),
        "scope_warning": (
            "Finite scans are diagnostic only.  The proved identities compress all three "
            "branches but do not classify their prime support or prove anything about e+pi."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=100)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/algebraic_unit_two_log_n5_three_double_root_trichotomy.json"
        ),
    )
    args = parser.parse_args()
    result = run(args.max_prime)
    script = Path(__file__).resolve()
    project = script.parent.parent
    source = (
        project
        / "sources"
        / "algebraic_unit_two_log_n5_three_double_root_trichotomy.md"
    )
    boundary_dependency = (
        project
        / "scripts"
        / "algebraic_unit_two_log_n5_p_boundary_obstruction.py"
    )
    weighted_precursor_source = (
        project
        / "sources"
        / "algebraic_unit_two_log_n5_weighted_left_factorial_coupling.md"
    )
    result["script_sha256"] = file_sha256(script)
    result["source_sha256"] = file_sha256(source)
    result["boundary_dependency_sha256"] = file_sha256(boundary_dependency)
    result["weighted_precursor_source_sha256"] = file_sha256(
        weighted_precursor_source
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
