#!/usr/bin/env python3
"""Exact ideal-content certificate for the n=5, c=f=0 two-log edge.

The companion source note proves the analytic statements.  This script uses
only integer arithmetic (apart from SymPy's exact Smith normal form) to:

* reconstruct the least rationally cleared coefficient pair in the real
  subfield of Q(zeta_5,i);
* compute its full coordinate-content ideal by a 4-by-8 Smith matrix;
* check degrees 1..D (D=200 by default);
* verify selected records independently in the degree-eight ambient field;
* compare the observed content norm with phi^d by an exact Fibonacci bound.

The finite scan is a certificate for the displayed range, not an all-degree
content theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


Kelt = tuple[int, int, int, int]
Pair = tuple[Kelt, Kelt]  # r+i*t, with r,t in Q(zeta_5)
ZERO: Kelt = (0, 0, 0, 0)
ONE: Kelt = (1, 0, 0, 0)
ZETA: Kelt = (0, 1, 0, 0)


def kadd(a: Kelt, b: Kelt) -> Kelt:
    return tuple(a[j] + b[j] for j in range(4))  # type: ignore[return-value]


def kneg(a: Kelt) -> Kelt:
    return tuple(-x for x in a)  # type: ignore[return-value]


def ksub(a: Kelt, b: Kelt) -> Kelt:
    return kadd(a, kneg(b))


def kscale(m: int, a: Kelt) -> Kelt:
    return tuple(m * x for x in a)  # type: ignore[return-value]


def kmul(a: Kelt, b: Kelt) -> Kelt:
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


def kpow(a: Kelt, exponent: int) -> Kelt:
    answer = ONE
    base = a
    while exponent:
        if exponent & 1:
            answer = kmul(answer, base)
        base = kmul(base, base)
        exponent //= 2
    return answer


def keval(coefficients: list[int], x: Kelt) -> Kelt:
    answer = ZERO
    for coefficient in reversed(coefficients):
        answer = kadd(kmul(answer, x), kscale(coefficient, ONE))
    return answer


def pmul(a: Pair, b: Pair) -> Pair:
    return (
        ksub(kmul(a[0], b[0]), kmul(a[1], b[1])),
        kadd(kmul(a[0], b[1]), kmul(a[1], b[0])),
    )


# Integral basis of the fixed field L^+=Q(zeta_5,i)^+:
# 1, zeta+zeta^-1, i(zeta-zeta^-1), i(zeta^2-zeta^-2).
ANTI1: Kelt = (1, 2, 1, 1)
ANTI2: Kelt = (0, 0, 1, -1)
BPLUS: tuple[Pair, Pair, Pair, Pair] = (
    (ONE, ZERO),
    ((-1, 0, -1, -1), ZERO),
    (ZERO, ANTI1),
    (ZERO, ANTI2),
)


def plus_coordinates(a: Pair) -> tuple[int, int, int, int]:
    """Coordinates in BPLUS, with exact fixed-field membership checks."""
    r, t = a
    if r[1] != 0 or r[2] != r[3]:
        raise AssertionError(f"real K component is not fixed: {r}")
    if t[1] != 2 * t[0] or t[2] + t[3] != 2 * t[0]:
        raise AssertionError(f"imaginary K component is not anti-fixed: {t}")
    return (r[0] - r[2], -r[2], t[0], t[2] - t[0])


def plus_multiplication_matrix(a: Pair) -> sp.Matrix:
    return sp.Matrix.hstack(
        *(sp.Matrix(plus_coordinates(pmul(a, basis))) for basis in BPLUS)
    )


def full_multiplication_matrix(a: Pair) -> sp.Matrix:
    basis: list[Pair] = []
    for j in range(4):
        basis.append((kpow(ZETA, j), ZERO))
    for j in range(4):
        basis.append((ZERO, kpow(ZETA, j)))
    columns = []
    for element in basis:
        product = pmul(a, element)
        columns.append(sp.Matrix(tuple(product[0]) + tuple(product[1])))
    return sp.Matrix.hstack(*columns)


def smith_diagonal(matrix: sp.Matrix, rank: int) -> list[int]:
    smith = smith_normal_form(matrix, domain=sp.ZZ)
    diagonal = [abs(int(smith[j, j])) for j in range(rank)]
    if any(value == 0 for value in diagonal):
        raise AssertionError("Smith matrix did not have full row rank")
    return diagonal


def lcm_through(n: int) -> int:
    answer = 1
    for value in range(1, n + 1):
        answer = math.lcm(answer, value)
    return answer


def edge_integer_data(d: int, eta: Kelt, eta_bar: Kelt) -> dict:
    """Return the minimally rational-cleared coefficient pair.

    P=d! A and Q=d! lcm(1..d) B are reconstructed integrally.  Multiplying
    Lambda by D=d!^3*lcm(1..d) gives the three K-coordinate blocks below.
    Their gcd with D determines the least positive rational multiplier.
    """
    h = math.factorial(d)
    ell = lcm_through(d)
    p_coefficients = [(-1) ** (d - j) * h // math.factorial(j) for j in range(d + 1)]
    q_coefficients = [0] * (d + 1)
    for degree in range(d + 1):
        q_coefficients[degree] = -sum(
            p_coefficients[j] * (ell // (degree - j)) for j in range(degree)
        )

    a = sum(p_coefficients)
    p_eta = keval(p_coefficients, eta)
    p_bar = keval(p_coefficients, eta_bar)
    q_eta = keval(q_coefficients, eta)
    q_bar = keval(q_coefficients, eta_bar)
    p_product = kmul(p_eta, p_bar)

    safe_u_imag = kscale(2 * ell * a, p_product)
    safe_v_imag = kscale(-2 * ((-1) ** d) * h * ell, p_product)
    safe_v_real = kadd(
        kscale(-5 * a, kmul(p_bar, q_eta)),
        kscale(5 * a, kmul(p_eta, q_bar)),
    )
    safe_denominator = h**3 * ell
    common = safe_denominator
    for coordinate in safe_u_imag + safe_v_imag + safe_v_real:
        common = math.gcd(common, abs(coordinate))

    u_imag = tuple(value // common for value in safe_u_imag)
    v_imag = tuple(value // common for value in safe_v_imag)
    v_real = tuple(value // common for value in safe_v_real)
    rational_content = 0
    for coordinate in u_imag + v_imag + v_real:
        rational_content = math.gcd(rational_content, abs(coordinate))

    # -i(q Lambda)=u*s+v is in L^+; u=U_imag and v=V_imag-i*V_real.
    u_plus: Pair = (u_imag, ZERO)
    v_plus: Pair = (v_imag, kneg(v_real))
    plus_coordinates(u_plus)
    plus_coordinates(v_plus)
    return {
        "p_coefficients": p_coefficients,
        "p_eta": p_eta,
        "p_bar": p_bar,
        "u_plus": u_plus,
        "v_plus": v_plus,
        "q_min": safe_denominator // common,
        "safe_denominator": safe_denominator,
        "safe_coordinate_gcd": common,
        "rational_content": rational_content,
    }


def fibonacci_pair(d: int) -> tuple[int, int]:
    previous, current = 0, 1
    for _ in range(d):
        previous, current = current, previous + current
    return previous, current  # F_d,F_{d+1}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/algebraic_unit_two_log_n5_ideal_content_d200.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/algebraic_unit_global_norm_rivoal.md"),
    )
    args = parser.parse_args()
    if args.max_d < 3:
        raise ValueError("max-d must be at least 3")

    eta: Kelt = (0, -1, 0, -1)  # (1+zeta_5)^-1
    eta_bar: Kelt = ksub(ONE, eta)
    records = []
    exception_records = []
    selected_full_degrees = {1, 2, 3, 7, 15, 72, 167, args.max_d}
    full_verifications = []
    all_threshold_checks = True

    for d in range(1, args.max_d + 1):
        data = edge_integer_data(d, eta, eta_bar)
        u_plus = data["u_plus"]
        v_plus = data["v_plus"]
        ideal_matrix = plus_multiplication_matrix(u_plus).row_join(
            plus_multiplication_matrix(v_plus)
        )
        diagonal = smith_diagonal(ideal_matrix, 4)
        norm = math.prod(diagonal)

        # phi^d=F_d*phi+F_(d-1) and phi>3/2.  This is an exact sufficient
        # comparison; it succeeds for every tested d>=3.
        f_d, f_next = fibonacci_pair(d)
        f_previous = f_next - f_d
        norm_below_phi_d = 2 * norm < 3 * f_d + 2 * f_previous
        if d >= 3:
            all_threshold_checks &= norm_below_phi_d

        record = {
            "d": d,
            "smith_diagonal_Lplus": diagonal,
            "content_ideal_norm_Lplus": str(norm),
            "rational_integer_coordinate_content": data["rational_content"],
            "q_min_digits": len(str(data["q_min"])),
            "norm_below_phi_power_d_by_phi_gt_3_over_2": norm_below_phi_d,
        }
        records.append(record)
        if norm != 1:
            exception_records.append(record)

        if d in selected_full_degrees:
            full_matrix = full_multiplication_matrix(u_plus).row_join(
                full_multiplication_matrix(v_plus)
            )
            full_diagonal = smith_diagonal(full_matrix, 8)
            full_norm = math.prod(full_diagonal)
            if full_norm != norm**2:
                raise AssertionError("ambient-field ideal norm is not the square")
            full_verifications.append(
                {
                    "d": d,
                    "smith_diagonal_L": full_diagonal,
                    "content_ideal_norm_L": str(full_norm),
                    "equals_Lplus_norm_squared": True,
                }
            )

    if not all_threshold_checks:
        raise AssertionError("an exact content threshold comparison failed")

    # State and verify the simple finite pattern without promoting it to a
    # theorem beyond the scanned range.
    def predicted_norm(d: int) -> int:
        if d == 1:
            return 16
        factor = 1
        if d % 5 == 2:
            factor *= 5
        if d % 19 == 15:
            factor *= 19
        return factor**2

    finite_pattern_matches = all(
        int(record["content_ideal_norm_Lplus"]) == predicted_norm(record["d"])
        for record in records
    )
    if not finite_pattern_matches:
        raise AssertionError("finite residue-class pattern failed")

    compact_rows = [
        (
            record["d"],
            tuple(record["smith_diagonal_Lplus"]),
            record["content_ideal_norm_Lplus"],
            record["rational_integer_coordinate_content"],
        )
        for record in records
    ]
    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    result = {
        "description": (
            "Exact finite Smith-normal-form certificate for the full algebraic "
            "coordinate-content ideal on the n=5,c=f=0 two-log edge."
        ),
        "scope_warning": "All residue-class and threshold claims are finite for 1<=d<=max_d; no all-degree content theorem is asserted.",
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "max_d": args.max_d,
        "field": {
            "ambient": "L=Q(zeta_5,i)=Q(zeta_20), degree 8",
            "real_subfield": "Lplus, degree 4",
            "integral_basis_Lplus": [
                "1",
                "zeta_5+zeta_5^-1",
                "i*(zeta_5-zeta_5^-1)",
                "i*(zeta_5^2-zeta_5^-2)",
            ],
        },
        "exact_reconstruction": {
            "P_recurrence": "P_0(X)=1; P_d(X)=X^d-d*P_(d-1)(X)=d!*A_d(X)",
            "safe_denominator": "d!^3*lcm(1,...,d)",
            "content_matrix": "4x8 matrix [M_u | M_v] in the displayed Lplus integral basis",
        },
        "finite_pattern": {
            "matches_all_records": finite_pattern_matches,
            "formula": "N(c_d)=16 for d=1; otherwise (5^[d=2 mod 5]*19^[d=15 mod 19])^2",
            "exception_records": exception_records,
        },
        "exact_threshold": {
            "range": f"3<=d<={args.max_d}",
            "all_content_norms_strictly_below_phi_power_d": all_threshold_checks,
            "proof_check": "2*N(c_d)<3*F_d+2*F_(d-1)<2*phi^d, using phi>3/2",
        },
        "selected_ambient_degree_8_verifications": full_verifications,
        "all_record_sha256": hashlib.sha256(repr(compact_rows).encode()).hexdigest(),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
