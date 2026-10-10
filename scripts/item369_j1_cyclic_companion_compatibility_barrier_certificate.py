#!/usr/bin/env python3
"""Deterministic exact replay for Item 369.

The checker compresses the actual selected Hasse/transverse pair into one
rank-two cyclic companion moment over F_(p^2).  It verifies the exact
characteristic polynomial, uniform cyclic vector, and the conjugacy-class
obstruction for the unframed rank-five Item 366 matrix.  It also rechecks
the growing singular support of literal full-order finite-log Kummerization.
Only predeclared control rows are evaluated; no collision scan is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item369_j1_cyclic_companion_compatibility_barrier_certificate.json"

DEPENDENCIES = {
    "sources/item342_j1_finite_field_fourier_weil_barrier_report.md":
        "843bb85381c98adf0a5b64801ce099e4c3c9119d5933704d97bbd492f1b8029b",
    "scripts/item342_j1_finite_field_fourier_weil_barrier_certificate.py":
        "130cfd5d2ac7c31546ef177c3f751abcc236ca92dc253a59914d487187c1fbac",
    "results/item342_j1_finite_field_fourier_weil_barrier_certificate.json":
        "4cf10e1d035dcd18a134e5f1b00e54a34ae1b3833a2863b54212da9fcccf49d9",
    "results/item342_j1_finite_field_fourier_weil_barrier_certificate_replay.json":
        "4cf10e1d035dcd18a134e5f1b00e54a34ae1b3833a2863b54212da9fcccf49d9",
    "results/item342_j1_finite_field_fourier_weil_barrier_root_replay.json":
        "4cf10e1d035dcd18a134e5f1b00e54a34ae1b3833a2863b54212da9fcccf49d9",
    "results/item342_j1_finite_field_fourier_weil_barrier_ledger_delta.json":
        "f60d0976d860c0860cb2c044ccde0ce53b6ab18d65f4e32ec648ec114d143df2",
    "results/item342_j1_finite_field_fourier_weil_barrier_root_audit.json":
        "aa6b260f78ae094b20a1b6b041c75131514b5ded51f016e6950671c472280835",
    "manifests/item342_j1_finite_field_fourier_weil_barrier_manifest.json":
        "85ca4a73d9009acc3dc8d7102325f74156a11bf13e618dc1a88c06fd352b8a54",
    "sources/item360_j1_full_gate_transverse_period_report.md":
        "4468412fb8631924952dc7f70fc4e75433a7524954b89525de508e55feefc8c4",
    "scripts/item360_j1_full_gate_transverse_period_certificate.py":
        "84cabfb296a0892e620f252a1c413648c30664c8667245bd6fe444095bcad7e0",
    "results/item360_j1_full_gate_transverse_period_certificate.json":
        "a3f9e5b8e55b0a36bf7aef18fd1b81010eef0e8b9c8ade05995e2c4a25f9084d",
    "results/item360_j1_full_gate_transverse_period_certificate_replay.json":
        "a3f9e5b8e55b0a36bf7aef18fd1b81010eef0e8b9c8ade05995e2c4a25f9084d",
    "results/item360_j1_full_gate_transverse_period_root_replay.json":
        "a3f9e5b8e55b0a36bf7aef18fd1b81010eef0e8b9c8ade05995e2c4a25f9084d",
    "results/item360_j1_full_gate_transverse_period_ledger_delta.json":
        "20a7676bd6c14bc24d3cd9623e64ef7836afae8ad9bb1536f357fccfd050e11e",
    "results/item360_j1_full_gate_transverse_period_self_audit.json":
        "79677ecf502683a38de56c134a48bba21cf352ca3374e74253c9aa0f8cee95df",
    "results/item360_j1_full_gate_transverse_period_root_audit.json":
        "7a23e487b4d70d63f9785339344bdc00ae0e8350bcf1d8b1fcf6228c230e5138",
    "manifests/item360_j1_full_gate_transverse_period_manifest.json":
        "92f88a56162f3803b8699922da921333f5225c41a32d14c87641dd53c3f8b55b",
    "sources/item366_j1_joint_frobenius_extension_obstruction_report.md":
        "50c678cadf4650a68eab772da297021190f06492928ee32bf9ea3c2215b9ea74",
    "scripts/item366_j1_joint_frobenius_extension_obstruction_certificate.py":
        "7157c1a3e1e7c63820d5bf9c29d080c632b6461e9ec9ad803d44c667479c3a3e",
    "results/item366_j1_joint_frobenius_extension_obstruction_certificate.json":
        "d6ac566800b010538ebad2b17648a49107f3d3e5ee93cd4b3af377fe851e486c",
    "results/item366_j1_joint_frobenius_extension_obstruction_certificate_replay.json":
        "d6ac566800b010538ebad2b17648a49107f3d3e5ee93cd4b3af377fe851e486c",
    "results/item366_j1_joint_frobenius_extension_obstruction_root_replay.json":
        "d6ac566800b010538ebad2b17648a49107f3d3e5ee93cd4b3af377fe851e486c",
    "results/item366_j1_joint_frobenius_extension_obstruction_ledger_delta.json":
        "d62cf99fc0da6425c383a277b1f86af3ce134f4e11ec36efc446f604c162011d",
    "results/item366_j1_joint_frobenius_extension_obstruction_root_audit.json":
        "8d787c37bf513d89cd461a84a77713386bf9c17b9f27d018dd8c3d90c94cbe50",
    "manifests/item366_j1_joint_frobenius_extension_obstruction_manifest.json":
        "91106677a853790eb511fc4efc0da8a5b29976107a17adfb2367b40d916a526e",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def multiply_polynomials(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = (output[i + j] + a * b) % prime
    return output


def power_polynomial(base: list[int], exponent: int, prime: int) -> list[int]:
    output = [1]
    while exponent:
        if exponent & 1:
            output = multiply_polynomials(output, base, prime)
        base = multiply_polynomials(base, base, prime)
        exponent //= 2
    return output


def p0_polynomial(h: int, s: int, prime: int) -> list[int]:
    return multiply_polynomials(
        multiply_polynomials(
            power_polynomial([1, -1], 2 * h, prime), [1, 1], prime
        ),
        power_polynomial([1, 0, 1], 2 * s, prime),
        prime,
    )


def finite_log(prime: int) -> list[int]:
    output = [0] * prime
    for k in range(1, prime):
        coefficient = (comb(prime, k) // prime) % prime
        if coefficient != ((-1) ** (k - 1) * pow(k, -1, prime)) % prime:
            raise AssertionError("finite-log quotient")
        output[k] = coefficient
    return output


def transverse_polynomial(h: int, s: int, prime: int) -> tuple[list[int], int, int]:
    log_z2 = [0] * (2 * prime - 1)
    for k, coefficient in enumerate(finite_log(prime)):
        log_z2[2 * k] = coefficient
    coefficients = multiply_polynomials(p0_polynomial(h, s, prime), log_z2, prime)
    return coefficients, 2 * h + 6 * s + 2, 4 * h + 4 * s + 2


def selected_hasse(h: int, s: int) -> int:
    n = 2 * h
    r = 2 * s + 1
    return sum(
        comb(r + k - 1, k) * comb(4 * r + n - 1, n - 4 * k)
        for k in range(n // 4 + 1)
    )


def least_nonsquare(prime: int) -> int:
    for value in range(2, prime):
        if pow(value, (prime - 1) // 2, prime) == prime - 1:
            return value
    raise AssertionError("nonsquare")


def fp2_operations(prime: int):
    nonsquare = least_nonsquare(prime)

    def add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        return ((left[0] + right[0]) % prime, (left[1] + right[1]) % prime)

    def multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        return (
            (left[0] * right[0] + nonsquare * left[1] * right[1]) % prime,
            (left[0] * right[1] + left[1] * right[0]) % prime,
        )

    def power(value: tuple[int, int], exponent: int) -> tuple[int, int]:
        output = (1, 0)
        while exponent:
            if exponent & 1:
                output = multiply(output, value)
            value = multiply(value, value)
            exponent //= 2
        return output

    return nonsquare, add, multiply, power


def polynomial_value(
    coefficients: list[int], value: tuple[int, int], add, multiply
) -> tuple[int, int]:
    output = (0, 0)
    for coefficient in reversed(coefficients):
        output = add(multiply(output, value), (coefficient, 0))
    return output


def companion_moment(h: int, s: int, prime: int) -> dict[str, Any]:
    n = 2 * h
    r = 2 * s + 1
    E = prime - r
    q_minus_one = prime * prime - 1
    p0 = p0_polynomial(h, s, prime)
    log_coefficients = finite_log(prime)
    T = 2 * h + 6 * s + 2
    L = 4 * h + 4 * s + 2
    nonsquare, add, multiply, power = fp2_operations(prime)
    total_hasse = (0, 0)
    total_transverse = (0, 0)
    total_frame = (0, 0)
    for first in range(prime):
        for second in range(prime):
            x = (first, second)
            if x == (0, 0):
                continue
            x2 = multiply(x, x)
            x3 = multiply(x2, x)
            g = add(
                add(
                    add((1, 0), ((-4 * first) % prime, (-4 * second) % prime)),
                    ((6 * x2[0]) % prime, (6 * x2[1]) % prime),
                ),
                ((-4 * x3[0]) % prime, (-4 * x3[1]) % prime),
            )
            hasse_integrand = multiply(
                power(x, q_minus_one - n), power(g, E)
            )
            p0_value = polynomial_value(p0, x, add, multiply)
            log_value = polynomial_value(log_coefficients, x2, add, multiply)
            finite_log_value = multiply(p0_value, log_value)
            frequency = add(
                ((2 * power(x, q_minus_one - T)[0]) % prime,
                 (2 * power(x, q_minus_one - T)[1]) % prime),
                ((-power(x, q_minus_one - L)[0]) % prime,
                 (-power(x, q_minus_one - L)[1]) % prime),
            )
            total_hasse = add(total_hasse, hasse_integrand)
            total_transverse = add(
                total_transverse, multiply(frequency, finite_log_value)
            )
            total_frame = add(total_frame, (prime - 1, 0))
    return {
        "nonsquare": nonsquare,
        "matrix": [
            [list(total_hasse), list(total_transverse)],
            [list(total_frame), [0, 0]],
        ],
    }


def finite_log_roots(prime: int) -> dict[str, int]:
    w = S.symbols("w")
    coefficients = finite_log(prime)
    polynomial = S.Poly(
        sum(coefficient * w**degree for degree, coefficient in enumerate(coefficients)),
        w,
        modulus=prime,
    )
    derivative = polynomial.diff()
    expected = S.Poly(sum((-1) ** j * w**j for j in range(prime - 1)), w, modulus=prime)
    if derivative != expected:
        raise AssertionError("finite-log derivative")
    gcd_degree = S.gcd(polynomial, derivative).degree()
    distinct = polynomial.degree() - gcd_degree
    if distinct < (prime - 1) // 2:
        raise AssertionError("root bound")
    return {
        "degree": polynomial.degree(),
        "gcd_derivative_degree": gcd_degree,
        "distinct_roots_Lp": distinct,
        "distinct_roots_Lp_z2": 2 * distinct - 1,
        "proved_lower_bound_Lp_z2": prime - 2,
    }


def symbolic_companion() -> dict[str, Any]:
    a, q0, X = S.symbols("a q0 X")
    companion = S.Matrix([[-a, -q0], [1, 0]])
    characteristic = S.expand(companion.charpoly(X).as_expr())
    if characteristic != X**2 + a * X + q0:
        raise AssertionError("companion characteristic polynomial")
    e1 = S.Matrix([1, 0])
    krylov = S.Matrix.hstack(e1, companion * e1)
    if S.expand(krylov.det()) != 1:
        raise AssertionError("uniform cyclic vector")
    if companion**2 + a * companion + q0 * S.eye(2) != S.zeros(2):
        raise AssertionError("Cayley-Hamilton recurrence")
    coefficient_map = S.Matrix([-companion.trace(), companion.det()])
    jacobian = coefficient_map.jacobian(S.Matrix([a, q0]))
    if jacobian.det() != 1:
        raise AssertionError("coordinate recovery")
    return {
        "matrix": "[[-a,-Q0],[1,0]]",
        "characteristic_polynomial": "X^2+a*X+Q0",
        "trace": "-a",
        "determinant": "Q0",
        "cyclic_vector": "e1",
        "Krylov_basis_determinant": "det[e1,C*e1]=1",
        "recurrence": "C^2+a*C+Q0*I=0",
        "coordinate_map_Jacobian_determinant": 1,
        "rank_minimality": "rank one has only one characteristic coefficient and cannot recover the transcendence-degree-two coordinate ring Z[a,Q0]",
    }


def symbolic_unframed_obstruction() -> dict[str, Any]:
    a = S.symbols("a")
    u, v = S.symbols("u v", nonzero=True)
    zero = S.Integer(0)
    matrix = S.Matrix([
        [-a, zero, zero, zero, zero],
        [zero, zero, u, zero, zero],
        [zero, zero, zero, zero, zero],
        [zero, zero, zero, zero, v],
        [zero, zero, zero, zero, zero],
    ])
    conjugator = S.diag(1, u, 1, v, 1)
    standard = S.simplify(conjugator.inv() * matrix * conjugator)
    expected = S.Matrix([
        [-a, zero, zero, zero, zero],
        [zero, zero, 1, zero, zero],
        [zero, zero, zero, zero, zero],
        [zero, zero, zero, zero, 1],
        [zero, zero, zero, zero, zero],
    ])
    if standard != expected:
        raise AssertionError("nilpotent block conjugacy")
    return {
        "rank_five_coordinates": "u=-2c_T, v=c_L, so u+v=-Q0",
        "open_stratum": "u*v != 0",
        "conjugator": "diag(1,u,1,v,1)",
        "normal_form": "diag(-a,N(1),N(1))",
        "counterpair": "(u,v)=(1,-1) has Q0=0 while (1,1) has Q0=-2; the matrices are conjugate in odd characteristic",
        "conclusion": "no invariant depending only on the unframed conjugacy class of the rank-five matrix can recover the transverse linear relation on the open stratum",
        "actual_orbit_caveat": "this is a universal functorial no-go; a new relation special to the tied orbit is not ruled out",
    }


# All four rows were predeclared before Item 369; no scan is made.
DECLARED_ROWS = [
    (1, 1, 13, 0, 9),
    (2, 1, 17, 8, 14),
    (8, 2, 47, 0, 30),
    (10, 11, 109, 70, 0),
]


def direct_controls() -> list[dict[str, Any]]:
    output = []
    for h, s, prime, expected_a, expected_q0 in DECLARED_ROWS:
        if prime != 4 * h + 6 * s + 3:
            raise AssertionError("actual selector")
        coefficients, T, L = transverse_polynomial(h, s, prime)
        cT = coefficients[T] % prime
        cL = coefficients[L] % prime
        q0 = (2 * cT - cL) % prime
        a = selected_hasse(h, s) % prime
        if (a, q0) != (expected_a, expected_q0):
            raise AssertionError("declared control")
        moment = companion_moment(h, s, prime)
        expected_matrix = [
            [[(-a) % prime, 0], [(-q0) % prime, 0]],
            [[1, 0], [0, 0]],
        ]
        if moment["matrix"] != expected_matrix:
            raise AssertionError(("companion moment", h, s, moment, expected_matrix))
        u = (-2 * cT) % prime
        v = cL % prime
        roots = finite_log_roots(prime)
        output.append({
            "classification": "PREDECLARED EXACT CONTROL; NOT A PRIME SCAN",
            "h": h,
            "s": s,
            "p": prime,
            "M": 3 * h + 4 * s + 2,
            "selected_Hasse": a,
            "transverse_Q0": q0,
            "c_T": cT,
            "c_L": cL,
            "rank_five_nilpotent_coordinates": {"u": u, "v": v, "u_plus_v": (u + v) % prime},
            "open_nilpotent_stratum": u != 0 and v != 0,
            "companion_moment": moment,
            "characteristic_polynomial": [1, a, q0],
            "finite_log_roots": roots,
        })
    return output


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item369-j1-cyclic-companion-compatibility-barrier-certificate-v1",
        "item": 369,
        "date": "2026-09-01",
        "status": "PROVED_MINIMAL_CYCLIC_COMPANION_AND_SCOPED_COMPATIBILITY_BARRIERS",
        "dependencies": DEPENDENCIES,
        "actual_family": "p=4h+6s+3, M=3h+4s+2, n=2h, r=2s+1",
        "companion_theorem": symbolic_companion(),
        "unframed_obstruction": symbolic_unframed_obstruction(),
        "finite_field_moment": {
            "field": "F_(p^2)",
            "local_matrix": "[[x^(-n)G(x)^(p-r), 2x^(-T)F_Q(x)-x^(-L)F_Q(x)],[-1,0]]",
            "summed_matrix": "[[-a,-Q0],[1,0]]",
            "lower_left_identity": "sum_(x in F_(p^2)^*) -1 = 1 in F_p",
            "target_aware_framing_used": True,
            "compatible_system_claimed": False,
            "why_not_yet_compatible": "an additive complete-moment companionization is not a Frobenius representation; no prime-independent local system, multiplicativity, or compatible characteristic-zero lift is constructed",
        },
        "literal_bounded_support_no_go": {
            "finite_log_root_bound": "L_p(z^2) has at least p-2 distinct roots",
            "full_order_Kummer_ramification": "root multiplicities are one or two, hence nonzero modulo both p-1 and p^2-1 for every actual p>=13",
            "conductor_conclusion": "literal full-order Kummer pullback along the finite-log factor has at least p-2 finite ramification points",
            "scope": "does not rule out a different unipotent F-crystal, Artin-Schreier compression, cancellation of apparent singularities, or target-specific compatible system",
        },
        "capacity": {
            "actual_support": "all fixed-j1 selector rows",
            "raw_log_mass": "M/6+o(M)",
            "raw_ceiling_per_6M": "1/36",
            "potential_if_joint_nonconcentration_proved": "remove the full 1/36 ceiling",
            "weighted_joint_zero_theorem_proved": False,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
            "route_1_status": "ACTIVE",
        },
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "exact all-row rank-two cyclic companion moment",
                "trace and determinant recover the two exact collision-forced coordinates",
                "rank-two minimality for universal exact characteristic-coordinate recovery",
                "unframed conjugacy-class no-go for the original rank-five moment",
                "literal full-order finite-log Kummer bounded-support no-go",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "four predeclared controls; no collision scan or density inference",
            ],
            "OPEN": [
                "a genuine prime-independent bounded-conductor compatible system realizing the companion polynomial",
                "a special relation on the actual tied orbit escaping the universal conjugacy obstruction",
                "framed or determinant-trace horizontal nonconcentration",
                "weighted joint-zero density, any fixed-j1 ceiling reduction, Route 1, and every conclusion about e+pi",
            ],
        },
        "canonical_files_modified": False,
        "collision_scans": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    pin_dependencies()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "item": 369,
        "cyclic_rank": 2,
        "trace_recovers_Hasse": True,
        "determinant_recovers_transverse": True,
        "compatible_system_proved": False,
        "booking": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
