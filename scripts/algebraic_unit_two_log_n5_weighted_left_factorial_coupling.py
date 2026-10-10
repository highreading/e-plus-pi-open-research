#!/usr/bin/env python3
"""Exact checks for the two weighted left-factorial coupling identities.

The finite prime scan is diagnostic only.  All identities claimed for every
eligible prime are proved in the companion Markdown source.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import algebraic_unit_two_log_n5_p_boundary_obstruction as base


Pair = base.Pair
Elt = base.Elt
Vector = tuple[Pair, Pair]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def embed_pair(value: Pair, prime: int) -> Elt:
    """Embed a+b*A, A=1-zeta^2-zeta^3, in the cyclotomic power basis."""

    a, b = value
    return ((a + b) % prime, 0, (-b) % prime, (-b) % prime)


def vector_add(x: Vector, y: Vector, prime: int) -> Vector:
    return (
        base.paddm(x[0], y[0], prime),
        base.paddm(x[1], y[1], prime),
    )


def vector_scale(coefficient: int, x: Vector, prime: int) -> Vector:
    return (
        base.pscalem(coefficient, x[0], prime),
        base.pscalem(coefficient, x[1], prime),
    )


def matrix_m(x: Vector, prime: int) -> Vector:
    """Multiplication by Z modulo Z^2-AZ+A."""

    return (
        base.pscalem(-1, base.pmulm(base.A, x[1], prime), prime),
        base.paddm(x[0], base.pmulm(base.A, x[1], prime), prime),
    )


def matrix_m_exact(x: Vector) -> Vector:
    return (
        base.pneg(base.pmul(base.A, x[1])),
        base.padd(x[0], base.pmul(base.A, x[1])),
    )


def norm_pair(value: Pair, prime: int) -> int:
    a, b = value
    return (a * a + 3 * a * b + b * b) % prime


def exact_matrix_check() -> None:
    basis_0: Vector = (base.PONE, base.PZERO)
    basis_1: Vector = (base.PZERO, base.PONE)
    image_0 = basis_0
    image_1 = basis_1
    for _ in range(5):
        image_0 = matrix_m_exact(image_0)
        image_1 = matrix_m_exact(image_1)
    expected_0 = (base.pneg(base.KAPPA), base.PZERO)
    expected_1 = (base.PZERO, base.pneg(base.KAPPA))
    if image_0 != expected_0 or image_1 != expected_1:
        raise AssertionError(f"M^5 identity failed: {image_0}, {image_1}")


def prime_check(prime: int) -> tuple[list[dict[str, int]], list[dict[str, int]]]:
    factorial = [1]
    for n in range(1, prime):
        factorial.append(factorial[-1] * n % prime)

    # All remainders, computed backward from W_p=0.
    a_values: list[Pair] = [base.PZERO for _ in range(prime + 1)]
    b_values: list[Pair] = [base.PZERO for _ in range(prime + 1)]
    for m in range(prime - 1, -1, -1):
        a_values[m] = base.paddm(
            (factorial[m], 0),
            base.pscalem(-1, base.pmulm(base.A, b_values[m + 1], prime), prime),
            prime,
        )
        b_values[m] = base.paddm(
            a_values[m + 1],
            base.pmulm(base.A, b_values[m + 1], prime),
            prime,
        )

    # Direct values and derivatives, independently propagated from
    # W_m=m!+Z*W_(m+1) and its derivative.
    wu_values: list[Elt] = [base.EZERO for _ in range(prime + 1)]
    wv_values: list[Elt] = [base.EZERO for _ in range(prime + 1)]
    wpu_values: list[Elt] = [base.EZERO for _ in range(prime + 1)]
    wpv_values: list[Elt] = [base.EZERO for _ in range(prime + 1)]
    for m in range(prime - 1, -1, -1):
        constant = (factorial[m], 0, 0, 0)
        wu_values[m] = base.eaddm(
            constant, base.emulm(base.U, wu_values[m + 1], prime), prime
        )
        wv_values[m] = base.eaddm(
            constant, base.emulm(base.V, wv_values[m + 1], prime), prime
        )
        wpu_values[m] = base.eaddm(
            wu_values[m + 1],
            base.emulm(base.U, wpu_values[m + 1], prime),
            prime,
        )
        wpv_values[m] = base.eaddm(
            wv_values[m + 1],
            base.emulm(base.V, wpv_values[m + 1], prime),
            prime,
        )

    zeta_inverse = base.epowm(base.ZETA, 4, prime)
    zeta_minus_one = base.eaddm(
        base.ZETA, base.escalem(-1, base.EONE, prime), prime
    )

    common_hits: list[dict[str, int]] = []
    resultant_only: list[dict[str, int]] = []
    for m in range(prime):
        d = prime - 1 - m
        a_value = a_values[m]
        b_value = b_values[m]

        # Direct remainder evaluation at the two roots u,v.
        wu = wu_values[m]
        wv = wv_values[m]
        remainder_u = base.eaddm(
            embed_pair(a_value, prime),
            base.emulm(embed_pair(b_value, prime), base.U, prime),
            prime,
        )
        remainder_v = base.eaddm(
            embed_pair(a_value, prime),
            base.emulm(embed_pair(b_value, prime), base.V, prime),
            prime,
        )
        if wu != remainder_u or wv != remainder_v:
            raise AssertionError(f"linear remainder failed at p={prime}, m={m}")

        # Resultant/product formula.
        resultant = base.paddm(
            base.pmulm(a_value, a_value, prime),
            base.paddm(
                base.pmulm(base.A, base.pmulm(a_value, b_value, prime), prime),
                base.pmulm(base.A, base.pmulm(b_value, b_value, prime), prime),
                prime,
            ),
            prime,
        )
        if embed_pair(resultant, prime) != base.emulm(wu, wv, prime):
            raise AssertionError(f"resultant product failed at p={prime}, m={m}")
        # R-a^2=A*b*(a+b), proving (b,R)=(b,a^2).
        difference = base.paddm(
            resultant,
            base.pscalem(-1, base.pmulm(a_value, a_value, prime), prime),
            prime,
        )
        expected_difference = base.pmulm(
            base.A,
            base.pmulm(b_value, base.paddm(a_value, b_value, prime), prime),
            prime,
        )
        if difference != expected_difference:
            raise AssertionError(f"resultant ideal identity failed at p={prime}, m={m}")

        # Coefficientwise differential equation.
        coefficients = [factorial[m + j] for j in range(d + 1)]
        if -coefficients[0] % prime != -factorial[m] % prime:
            raise AssertionError("constant differential coefficient failed")
        for k in range(1, d + 1):
            coefficient = ((m + k) * coefficients[k - 1] - coefficients[k]) % prime
            if coefficient:
                raise AssertionError(f"differential equation failed at p={prime}, m={m}, k={k}")
        if ((m + d + 1) * coefficients[d]) % prime:
            raise AssertionError(f"terminal differential coefficient failed at p={prime}, m={m}")

        # H(u), H'(u), the lacuna, and the exact coupling identity.
        w_prime_u = wpu_values[m]
        w_prime_v = wpv_values[m]
        h_u = base.eaddm(wv, base.escalem(-1, base.emulm(base.ZETA, wu, prime), prime), prime)
        h_prime_u = base.eaddm(
            base.emulm(zeta_inverse, w_prime_v, prime),
            base.escalem(-1, base.emulm(base.ZETA, w_prime_u, prime), prime),
            prime,
        )
        h_coefficients: list[Elt] = []
        zeta_inverse_power = base.EONE
        for j in range(d + 1):
            h_coefficients.append(
                base.escalem(
                    factorial[m + j],
                    base.eaddm(
                        zeta_inverse_power,
                        base.escalem(-1, base.ZETA, prime),
                        prime,
                    ),
                    prime,
                )
            )
            zeta_inverse_power = base.emulm(
                zeta_inverse_power, zeta_inverse, prime
            )
        for j in range(4, d + 1, 5):
            if h_coefficients[j] != base.EZERO:
                raise AssertionError(f"H lacuna failed at p={prime}, m={m}, j={j}")
        zeta_zeta_minus_one = base.emulm(base.ZETA, zeta_minus_one, prime)
        for k in range(d + 2):
            lhs_coefficient = (
                base.escalem(k - 1, h_coefficients[k - 1], prime)
                if 2 <= k <= d + 1
                else base.EZERO
            )
            rhs_coefficient = base.EZERO
            if k <= d:
                rhs_coefficient = base.eaddm(
                    rhs_coefficient,
                    base.emulm(base.ZETA, h_coefficients[k], prime),
                    prime,
                )
                rhs_coefficient = base.eaddm(
                    rhs_coefficient,
                    base.escalem(
                        factorial[m + k], zeta_zeta_minus_one, prime
                    ),
                    prime,
                )
            if 1 <= k <= d + 1:
                rhs_coefficient = base.eaddm(
                    rhs_coefficient,
                    base.escalem(
                        -(m + 1), h_coefficients[k - 1], prime
                    ),
                    prime,
                )
            if lhs_coefficient != rhs_coefficient:
                raise AssertionError(
                    f"H polynomial identity failed at p={prime}, m={m}, k={k}"
                )
        left = base.emulm(base.emulm(base.U, base.U, prime), h_prime_u, prime)
        zeta_minus_m_u = base.eaddm(
            base.ZETA, base.escalem(-(m + 1), base.U, prime), prime
        )
        right = base.eaddm(
            base.emulm(zeta_minus_m_u, h_u, prime),
            base.emulm(
                base.emulm(base.ZETA, zeta_minus_one, prime),
                wu,
                prime,
            ),
            prime,
        )
        if left != right:
            raise AssertionError(f"H differential coupling failed at p={prime}, m={m}")
        if h_u != base.eaddm(wv, base.escalem(-1, base.emulm(base.ZETA, wu, prime), prime), prime):
            raise AssertionError("H value formula failed")

        proper = base.h_pair_is_proper_mod_p(a_value, b_value, prime)
        if proper:
            common_hits.append({"p": prime, "d": d, "m": m})
        if norm_pair(resultant, prime) == 0 and not proper and len(resultant_only) < 20:
            resultant_only.append({"p": prime, "d": d, "m": m})

    # Five-block vector recurrence.
    for m in range(prime - 4):
        forcing: Vector = (base.PZERO, base.PZERO)
        image: Vector = (base.PONE, base.PZERO)
        for j in range(5):
            forcing = vector_add(
                forcing,
                vector_scale(factorial[m + j], image, prime),
                prime,
            )
            image = matrix_m(image, prime)
        rhs = vector_add(
            forcing,
            (
                base.pscalem(-1, base.pmulm(base.KAPPA, a_values[m + 5], prime), prime),
                base.pscalem(-1, base.pmulm(base.KAPPA, b_values[m + 5], prime), prime),
            ),
            prime,
        )
        if rhs != (a_values[m], b_values[m]):
            raise AssertionError(f"five-block remainder recurrence failed at p={prime}, m={m}")

    return common_hits, resultant_only


def explicit_p11_check() -> dict[str, object]:
    prime = 11
    d = 4
    m = 6
    zeta = 4
    u = 5
    v = 4
    x = 9
    y = 3

    def w_scalar(argument: int) -> int:
        return sum(
            sp.factorial(m + j) * pow(argument, j, prime)
            for j in range(d + 1)
        ) % prime

    def p4(argument: int) -> int:
        return (
            argument**4
            - 4 * argument**3
            + 12 * argument**2
            - 24 * argument
            + 24
        ) % prime

    values = {
        "p": prime,
        "d": d,
        "m": m,
        "zeta": zeta,
        "u": u,
        "v": v,
        "x": x,
        "y": y,
        "W_u": int(w_scalar(u)),
        "W_v": int(w_scalar(v)),
        "P4_x": p4(x),
        "P4_y": p4(y),
        "remainder_a": 10,
        "remainder_b": 3,
    }
    expected = {
        "p": 11,
        "d": 4,
        "m": 6,
        "zeta": 4,
        "u": 5,
        "v": 4,
        "x": 9,
        "y": 3,
        "W_u": 3,
        "W_v": 0,
        "P4_x": 3,
        "P4_y": 0,
        "remainder_a": 10,
        "remainder_b": 3,
    }
    if values != expected:
        raise AssertionError(f"p=11 counterexample changed: {values}")
    if (values["remainder_a"] + values["remainder_b"] * u) % prime != values["W_u"]:
        raise AssertionError("p=11 u remainder failed")
    if (values["remainder_a"] + values["remainder_b"] * v) % prime != values["W_v"]:
        raise AssertionError("p=11 v remainder failed")
    return values


def run(max_prime: int) -> dict[str, object]:
    if max_prime < 19:
        raise ValueError("max-prime must be at least 19")
    exact_matrix_check()
    hits: list[dict[str, int]] = []
    resultant_only: list[dict[str, int]] = []
    prime_count = 0
    for prime_value in sp.primerange(3, max_prime + 1):
        prime = int(prime_value)
        if prime == 5:
            continue
        prime_count += 1
        prime_hits, prime_resultant_only = prime_check(prime)
        hits.extend(prime_hits)
        for item in prime_resultant_only:
            if len(resultant_only) < 20:
                resultant_only.append(item)

    return {
        "description": "Exact linear-remainder, resultant, and lacunary H coupling checks.",
        "bounds": {
            "odd_primes_other_than_5_max": max_prime,
            "prime_count": prime_count,
            "all_complementary_indices": "0<=m<=p-1 (equivalently 0<=d<p)",
        },
        "identity_checks": {
            "W_differential_equation": True,
            "linear_remainder_at_u_and_v": True,
            "resultant_product_and_radical_data": True,
            "M_fifth_power_and_five_block_recurrence": True,
            "lacunary_H_and_derivative_coupling": True,
        },
        "exact_product_only_counterexample": explicit_p11_check(),
        "finite_diagnostics": {
            "true_common_ideal_hits": hits,
            "first_resultant_zero_but_common_ideal_unit_cases": resultant_only,
        },
        "scope_warning": (
            "The finite scan does not prove that 19 is the only common support prime.  "
            "The p=11 example refutes use of the product/resultant alone, not the true "
            "two-generator support conjecture or any statement about e+pi."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/algebraic_unit_two_log_n5_weighted_left_factorial_coupling.json"
        ),
    )
    args = parser.parse_args()
    result = run(args.max_prime)
    script = Path(__file__).resolve()
    project = script.parent.parent
    source = (
        project
        / "sources"
        / "algebraic_unit_two_log_n5_weighted_left_factorial_coupling.md"
    )
    dependency = (
        project
        / "scripts"
        / "algebraic_unit_two_log_n5_p_boundary_obstruction.py"
    )
    result["script_sha256"] = file_sha256(script)
    result["source_sha256"] = file_sha256(source)
    result["dependency_sha256"] = file_sha256(dependency)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
