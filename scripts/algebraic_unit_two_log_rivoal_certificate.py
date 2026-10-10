#!/usr/bin/env python3
"""Exact certificate and sharply targeted diagnostics for the two-log unit family.

The theorem in sources/algebraic_unit_global_norm_rivoal.md is proved there.
This script independently checks the Q(zeta_5) algebra, exact coefficient
clearing for c=f=0, and a few numerical values testing the stated asymptotic
norm exponent.  Numerical records are explicitly diagnostics, not proofs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import mpmath as mp
import sympy as sp


Kelt = tuple[Fraction, Fraction, Fraction, Fraction]
ZERO: Kelt = (Fraction(0),) * 4
ONE: Kelt = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
ZETA: Kelt = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))


def kadd(a: Kelt, b: Kelt) -> Kelt:
    return tuple(a[j] + b[j] for j in range(4))  # type: ignore[return-value]


def kneg(a: Kelt) -> Kelt:
    return tuple(-x for x in a)  # type: ignore[return-value]


def ksub(a: Kelt, b: Kelt) -> Kelt:
    return kadd(a, kneg(b))


def kscale(q: Fraction | int, a: Kelt) -> Kelt:
    q = Fraction(q)
    return tuple(q * x for x in a)  # type: ignore[return-value]


def kmul(a: Kelt, b: Kelt) -> Kelt:
    raw = [Fraction(0) for _ in range(7)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            raw[i + j] += ai * bj
    # zeta^4=-(1+zeta+zeta^2+zeta^3).
    for degree in range(6, 3, -1):
        value = raw[degree]
        if value:
            for target in range(degree - 4, degree):
                raw[target] -= value
            raw[degree] = Fraction(0)
    return tuple(raw[:4])  # type: ignore[return-value]


def kpow(a: Kelt, exponent: int) -> Kelt:
    if exponent < 0:
        raise ValueError("negative powers are not used")
    answer = ONE
    base = a
    while exponent:
        if exponent & 1:
            answer = kmul(answer, base)
        base = kmul(base, base)
        exponent //= 2
    return answer


def kconj(a: Kelt) -> Kelt:
    # Complex conjugation is zeta -> zeta^{-1}=zeta^4.
    zeta_bar = kpow(ZETA, 4)
    answer = ZERO
    power = ONE
    for coefficient in a:
        answer = kadd(answer, kscale(coefficient, power))
        power = kmul(power, zeta_bar)
    return answer


def kevaluate(coefficients: Iterable[Fraction], x: Kelt) -> Kelt:
    answer = ZERO
    for coefficient in reversed(tuple(coefficients)):
        answer = kadd(kmul(answer, x), kscale(coefficient, ONE))
    return answer


def multiplication_matrix(a: Kelt) -> sp.Matrix:
    columns = []
    for j in range(4):
        columns.append([sp.Rational(x.numerator, x.denominator) for x in kmul(a, kpow(ZETA, j))])
    return sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))


def coordinate_denominator(values: Iterable[Fraction]) -> int:
    answer = 1
    for value in values:
        answer = math.lcm(answer, value.denominator)
    return answer


def lcm_through(n: int) -> int:
    answer = 1
    for value in range(1, n + 1):
        answer = math.lcm(answer, value)
    return answer


def edge_polynomials(d: int) -> tuple[list[Fraction], list[Fraction], list[Fraction]]:
    """Return A,B,E for c=f=0 from the defining coefficient convolutions."""
    A = [Fraction((-1) ** (d - j), math.factorial(j)) for j in range(d + 1)]
    B = [Fraction(0) for _ in range(d + 1)]
    for n in range(d + 1):
        B[n] = -sum((A[m] / (n - m) for m in range(n)), Fraction(0))
    E = [A[0]]
    return A, B, E


def exact_edge_record(d: int, eta: Kelt, eta_bar: Kelt) -> dict:
    A, B, E = edge_polynomials(d)
    A_one = sum(A, Fraction(0))
    E_one = E[0]
    A_eta = kevaluate(A, eta)
    A_bar = kevaluate(A, eta_bar)
    B_eta = kevaluate(B, eta)
    B_bar = kevaluate(B, eta_bar)

    # Lambda=U*s+V in Q(zeta_5,i), represented as real and i coordinates.
    U_imag = kscale(2 * A_one, kmul(A_eta, A_bar))
    V_imag = kscale(-2 * E_one, kmul(A_eta, A_bar))
    V_real = kadd(
        kscale(-5 * A_one, kmul(A_bar, B_eta)),
        kscale(5 * A_one, kmul(A_eta, B_bar)),
    )
    coordinates = tuple(U_imag) + tuple(V_imag) + tuple(V_real)
    q_min = coordinate_denominator(coordinates)
    safe = math.factorial(d) ** 3 * lcm_through(d)
    cleared = [q_min * value for value in coordinates]
    if any(value.denominator != 1 for value in cleared):
        raise AssertionError("minimal coordinate denominator failed")
    if safe % q_min:
        raise AssertionError("safe denominator is not a multiple of q_min")
    rational_content = 0
    for value in cleared:
        rational_content = math.gcd(rational_content, abs(int(value)))
    return {
        "d": d,
        "q_min": str(q_min),
        "q_min_digits": len(str(q_min)),
        "safe_denominator_digits": len(str(safe)),
        "safe_over_q_min": str(safe // q_min),
        "rational_integer_coordinate_content": str(rational_content),
        "effective_multiplier_after_rational_content": str(
            Fraction(q_min, rational_content)
        ),
        "nonzero_U": any(U_imag),
        "coordinate_sha256": hashlib.sha256(
            repr(tuple((x.numerator, x.denominator) for x in coordinates)).encode()
        ).hexdigest(),
    }


def eval_fraction_poly(coefficients: Iterable[Fraction], x: mp.mpc) -> mp.mpc:
    answer = mp.mpc(0)
    for coefficient in reversed(tuple(coefficients)):
        answer = answer * x + mp.mpf(coefficient.numerator) / coefficient.denominator
    return answer


def numerical_embedding_values(d: int) -> tuple[list[mp.mpf], mp.mpf, mp.mpf]:
    A, B, E = edge_polynomials(d)
    zeta = mp.e ** (2j * mp.pi / 5)
    s = mp.e + mp.pi
    A_one = eval_fraction_poly(A, mp.mpc(1))
    E_one = eval_fraction_poly(E, mp.mpc(1))
    values: list[mp.mpf] = []
    for k in (1, 2, -2, -1):
        x = 1 / (1 + zeta**k)
        y = 1 / (1 + zeta ** (-k))
        A_x = eval_fraction_poly(A, x)
        A_y = eval_fraction_poly(A, y)
        B_x = eval_fraction_poly(B, x)
        B_y = eval_fraction_poly(B, y)
        for epsilon in (1, -1):
            U = 2 * epsilon * 1j * A_one * A_x * A_y
            V = (
                -2 * epsilon * 1j * A_x * A_y * E_one
                - 5 * A_one * A_y * B_x
                + 5 * A_one * A_x * B_y
            )
            values.append(abs(U * s + V))
    product = mp.fprod(values)
    golden = (1 + mp.sqrt(5)) / 2
    rho = 1 / golden
    scaled_product = product * d**6 * rho ** (2 * d)
    return values, product, scaled_product


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/algebraic_unit_two_log_rivoal_certificate.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/algebraic_unit_global_norm_rivoal.md"),
    )
    args = parser.parse_args()
    mp.mp.dps = 100

    # eta=(1+zeta_5)^(-1)=-zeta-zeta^3.
    eta: Kelt = (Fraction(0), Fraction(-1), Fraction(0), Fraction(-1))
    eta_bar = kconj(eta)
    algebra_checks = {
        "eta_times_one_plus_zeta": kmul(eta, kadd(ONE, ZETA)),
        "eta_plus_conjugate": kadd(eta, eta_bar),
        "conjugate_equals_one_minus_eta": eta_bar == ksub(ONE, eta),
        "conjugate_equals_zeta_times_eta": eta_bar == kmul(ZETA, eta),
        "eta_norm": int(multiplication_matrix(eta).det()),
        "cyclotomic_5_at_minus_one": int(sp.cyclotomic_poly(5, sp.Symbol("x")).subs(sp.Symbol("x"), -1)),
    }
    if algebra_checks["eta_times_one_plus_zeta"] != ONE:
        raise AssertionError("eta inverse identity failed")
    if algebra_checks["eta_plus_conjugate"] != ONE:
        raise AssertionError("complement identity failed")
    if algebra_checks["eta_norm"] not in (-1, 1):
        raise AssertionError("eta is not a unit")

    odd_cyclotomic_checks = {}
    x_symbol = sp.Symbol("x")
    for n in range(5, 32, 2):
        value = int(sp.cyclotomic_poly(n, x_symbol).subs(x_symbol, -1))
        odd_cyclotomic_checks[str(n)] = value
        if value != 1:
            raise AssertionError(f"Phi_{n}(-1) != 1")

    edge_records = [exact_edge_record(d, eta, eta_bar) for d in range(1, 26)]

    mismatch_table = []
    for k in (1, 2, -2, -1):
        rho_type = "small" if abs(k) == 1 else "large"
        for epsilon in (1, -1):
            mismatch_table.append(
                {
                    "k": k,
                    "epsilon": epsilon,
                    "branch_numerator": 2 * k,
                    "algebraic_target_numerator": 2 * epsilon,
                    "matched": epsilon == k,
                    "rho_type": rho_type,
                }
            )

    numerical = []
    for d in (10, 20, 40, 80):
        values, product, scaled = numerical_embedding_values(d)
        numerical.append(
            {
                "d": d,
                "embedding_abs_values": [mp.nstr(value, 30) for value in values],
                "raw_product": mp.nstr(product, 40),
                "product_times_d6_rho_2d": mp.nstr(scaled, 40),
            }
        )

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    result = {
        "description": "Exact Q(zeta_5) and clearing certificate for the algebraic-unit two-log Rivoal family; numerical asymptotic records are diagnostics only.",
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "field_basis": ["1", "zeta_5", "zeta_5^2", "zeta_5^3"],
        "algebra_checks": {
            key: ([str(x) for x in value] if isinstance(value, tuple) else value)
            for key, value in algebra_checks.items()
        },
        "odd_Phi_n_minus_one": odd_cyclotomic_checks,
        "n5_exact_base": {
            "B5": "phi^2=(3+sqrt(5))/2",
            "minimal_polynomial": "X^2-3*X+1",
            "relative_product_order": "B5^d*d^(-6)",
        },
        "embedding_mismatch_table": mismatch_table,
        "edge_exact_clearing_records": edge_records,
        "numerical_diagnostics_not_used_in_proof": numerical,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
