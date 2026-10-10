#!/usr/bin/env python3
"""Deterministic exact replay for Item 366.

The checker realizes the actual selected Hasse coefficient and transverse
Q0 as two framed matrix coefficients of one rank-five F_(p^2) moment built
from a scalar Hasse block and two logarithmic divided-Frobenius blocks.  It
verifies that the characteristic polynomial and every trace power ignore
the transverse extension entries.  It also checks the base-field two-alias
formula and the growing-root obstruction for literal Kummerization of the
finite logarithm.  No collision scan or density inference is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item366_j1_joint_frobenius_extension_obstruction_certificate.json"

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
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def polynomial_multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] = (output[i + j] + left_value * right_value) % prime
    return output


def polynomial_power(base: list[int], exponent: int, prime: int) -> list[int]:
    output = [1]
    while exponent:
        if exponent & 1:
            output = polynomial_multiply(output, base, prime)
        base = polynomial_multiply(base, base, prime)
        exponent //= 2
    return output


def polynomial_value(
    coefficients: list[int], value: tuple[int, int],
    add, multiply
) -> tuple[int, int]:
    output = (0, 0)
    for coefficient in reversed(coefficients):
        output = add(multiply(output, value), (coefficient, 0))
    return output


def integer_polynomial_power(base: list[int], exponent: int) -> list[int]:
    output = [1]
    while exponent:
        if exponent & 1:
            new = [0] * (len(output) + len(base) - 1)
            for i, a in enumerate(output):
                for j, b in enumerate(base):
                    new[i + j] += a * b
            output = new
        new_base = [0] * (2 * len(base) - 1)
        for i, a in enumerate(base):
            for j, b in enumerate(base):
                new_base[i + j] += a * b
        base = new_base
        exponent //= 2
    return output


def integer_polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return output


def p0_integer(h: int, s: int) -> list[int]:
    return integer_polynomial_multiply(
        integer_polynomial_multiply(
            integer_polynomial_power([1, -1], 2 * h), [1, 1]
        ),
        integer_polynomial_power([1, 0, 1], 2 * s),
    )


def finite_log_coefficients(prime: int) -> list[int]:
    output = [0] * prime
    for k in range(1, prime):
        quotient = comb(prime, k) // prime
        expected = ((-1) ** (k - 1) * pow(k, -1, prime)) % prime
        if quotient % prime != expected:
            raise AssertionError("finite-log binomial quotient")
        output[k] = quotient % prime
    return output


def finite_log_convolution(h: int, s: int, prime: int) -> tuple[list[int], int, int]:
    p0 = [value % prime for value in p0_integer(h, s)]
    log_z2 = [0] * (2 * prime - 1)
    for k, value in enumerate(finite_log_coefficients(prime)):
        log_z2[2 * k] = value
    product = polynomial_multiply(p0, log_z2, prime)
    T = 2 * h + 6 * s + 2
    L = 4 * h + 4 * s + 2
    return product, T, L


def selected_hasse(h: int, s: int) -> int:
    r = 2 * s + 1
    n = 2 * h
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

    def negate(value: tuple[int, int]) -> tuple[int, int]:
        return ((-value[0]) % prime, (-value[1]) % prime)

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

    return nonsquare, add, negate, multiply, power


def extension_joint_moment(h: int, s: int, prime: int) -> dict[str, Any]:
    n = 2 * h
    r = 2 * s + 1
    E = prime - r
    q_minus_one = prime * prime - 1
    p0 = [value % prime for value in p0_integer(h, s)]
    finite_log = finite_log_coefficients(prime)
    T = 2 * h + 6 * s + 2
    L = 4 * h + 4 * s + 2
    nonsquare, add, negate, multiply, power = fp2_operations(prime)
    totals = {
        "hasse": (0, 0),
        "T_diagonal": (0, 0),
        "T_extension": (0, 0),
        "L_diagonal": (0, 0),
        "L_extension": (0, 0),
    }
    for first in range(prime):
        for second in range(prime):
            x = (first, second)
            if x == (0, 0):
                continue
            square = multiply(x, x)
            cube = multiply(square, x)
            g_value = add(
                add(
                    add((1, 0), ((-4 * first) % prime, (-4 * second) % prime)),
                    ((6 * square[0]) % prime, (6 * square[1]) % prime),
                ),
                ((-4 * cube[0]) % prime, (-4 * cube[1]) % prime),
            )
            hasse_term = multiply(
                power(x, q_minus_one - n), power(g_value, E)
            )
            p0_value = polynomial_value(p0, x, add, multiply)
            log_value = polynomial_value(finite_log, square, add, multiply)
            T_weight = multiply((2, 0), multiply(power(x, q_minus_one - T), p0_value))
            L_weight = negate(multiply(power(x, q_minus_one - L), p0_value))
            totals["hasse"] = add(totals["hasse"], hasse_term)
            totals["T_diagonal"] = add(totals["T_diagonal"], T_weight)
            totals["T_extension"] = add(
                totals["T_extension"], multiply(T_weight, log_value)
            )
            totals["L_diagonal"] = add(totals["L_diagonal"], L_weight)
            totals["L_extension"] = add(
                totals["L_extension"], multiply(L_weight, log_value)
            )
    return {"nonsquare": nonsquare, **totals}


def base_field_two_alias(coefficients: list[int], index: int, prime: int) -> dict[str, int]:
    S0 = 0
    S1 = 0
    for x in range(1, prime):
        value = 0
        theta_value = 0
        for degree, coefficient in enumerate(coefficients):
            power_value = pow(x, degree, prime)
            value += coefficient * power_value
            theta_value += degree * coefficient * power_value
        frequency = pow(x, prime - 1 - index, prime)
        S0 = (S0 + frequency * value) % prime
        S1 = (S1 + frequency * theta_value) % prime
    recovered = ((index - 1) * S0 - S1) % prime
    return {"S0": S0, "S1": S1, "recovered": recovered}


def distinct_root_lower_bound(prime: int) -> dict[str, int]:
    w = S.symbols("w")
    coefficients = finite_log_coefficients(prime)
    polynomial = S.Poly(
        sum(value * w**degree for degree, value in enumerate(coefficients)),
        w,
        modulus=prime,
    )
    derivative = polynomial.diff()
    expected_derivative = S.Poly(
        sum(((-1) ** j) * w**j for j in range(prime - 1)),
        w,
        modulus=prime,
    )
    if derivative != expected_derivative:
        raise AssertionError("finite-log derivative")
    gcd_degree = S.gcd(polynomial, derivative).degree()
    distinct = polynomial.degree() - gcd_degree
    if distinct < (prime - 1) // 2:
        raise AssertionError("distinct root lower bound")
    return {
        "degree": polynomial.degree(),
        "gcd_with_derivative_degree": gcd_degree,
        "distinct_roots_over_algebraic_closure": distinct,
        "z_squared_distinct_roots": 2 * distinct - 1,
        "proved_lower_bound_for_z_squared": prime - 2,
    }


def symbolic_theorem() -> dict[str, Any]:
    h, s, p = S.symbols("h s p", integer=True, positive=True)
    d = 2 * h + 4 * s + 1
    T = 2 * h + 6 * s + 2
    L = 4 * h + 4 * s + 2
    Dq = d + 2 * (p - 1)
    actual_p = 4 * h + 6 * s + 3
    identities = {
        "T_minus_degree": T - d - (2 * s + 1),
        "L_minus_degree": L - d - (2 * h + 1),
        "T_second_alias_absent": Dq - (T + 2 * (p - 1)) - (d - T),
        "L_second_alias_absent": Dq - (L + 2 * (p - 1)) - (d - L),
    }
    if any(S.expand(value) != 0 for value in identities.values()):
        raise AssertionError("degree identities")
    if S.expand((p - 1 + d - T).subs(p, actual_p) - (4 * h + 4 * s + 1)) != 0:
        raise AssertionError("T first alias")
    if S.expand((p - 1 + d - L).subs(p, actual_p) - (2 * h + 6 * s + 1)) != 0:
        raise AssertionError("L first alias")

    a, cT, cL, X = S.symbols("a c_T c_L X")
    moment_matrix = S.Matrix([
        [-a, 0, 0, 0, 0],
        [0, 0, -2 * cT, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, cL],
        [0, 0, 0, 0, 0],
    ])
    characteristic = S.factor(moment_matrix.charpoly(X).as_expr())
    if S.expand(characteristic - X**4 * (X + a)) != 0:
        raise AssertionError("characteristic polynomial")
    traces = []
    for exponent in range(1, 6):
        trace = S.factor((moment_matrix**exponent).trace())
        if S.expand(trace - (-a) ** exponent) != 0:
            raise AssertionError("trace power")
        traces.append(str(trace))
    return {
        "actual_family": "p=4h+6s+3, M=3h+4s+2",
        "Q_polynomial_degree": "deg(P0*L_p(z^2))=2h+4s+1+2(p-1)<3p<p^2-1",
        "two_aliases_over_Fp": "for N=T,L, only N and N+p-1 occur",
        "coefficient_recovery": "c_N=(N-1)S_(N,0)-S_(N,1)",
        "rank_five_global_matrix": "diag(-a, [[0,-2c_T],[0,0]], [[0,c_L],[0,0]])",
        "transverse_functional": "-Q0=(-2c_T)+c_L",
        "characteristic_polynomial": str(characteristic),
        "trace_powers_1_to_5": traces,
        "determinant": "0",
        "conclusion": "all characteristic-polynomial and trace-power data ignore Q0",
    }


# Predeclared in Items 342, 360, and 218; no row was discovered by Item 366.
DECLARED_ROWS = [
    (1, 1, 13, 0, 9),
    (2, 1, 17, 8, 14),
    (8, 2, 47, 0, 30),
    (10, 11, 109, 70, 0),
]


def direct_controls() -> list[dict[str, Any]]:
    output = []
    for h, s, prime, expected_hasse, expected_q0 in DECLARED_ROWS:
        if prime != 4 * h + 6 * s + 3:
            raise AssertionError("actual row")
        coefficients, T, L = finite_log_convolution(h, s, prime)
        cT = coefficients[T] % prime
        cL = coefficients[L] % prime
        q0 = (2 * cT - cL) % prime
        hasse = selected_hasse(h, s) % prime
        if (hasse, q0) != (expected_hasse, expected_q0):
            raise AssertionError((h, s, prime, hasse, q0))
        Dq = len(coefficients) - 1
        if not Dq < prime * prime - 1:
            raise AssertionError("extension isolation degree")
        T_alias = base_field_two_alias(coefficients, T, prime)
        L_alias = base_field_two_alias(coefficients, L, prime)
        if T_alias["recovered"] != cT or L_alias["recovered"] != cL:
            raise AssertionError("two-alias de-aliasing")
        moment = extension_joint_moment(h, s, prime)
        expected = {
            "hasse": ((-hasse) % prime, 0),
            "T_diagonal": (0, 0),
            "T_extension": ((-2 * cT) % prime, 0),
            "L_diagonal": (0, 0),
            "L_extension": (cL % prime, 0),
        }
        for key, value in expected.items():
            if moment[key] != value:
                raise AssertionError(("extension moment", key, moment[key], value))
        transverse_matrix_coefficient = (
            moment["T_extension"][0] + moment["L_extension"][0]
        ) % prime
        if transverse_matrix_coefficient != (-q0) % prime:
            raise AssertionError("transverse functional")
        root_data = distinct_root_lower_bound(prime)
        output.append({
            "classification": "PREDECLARED EXACT CONTROL; NOT A PRIME SCAN",
            "h": h,
            "s": s,
            "p": prime,
            "M": 3 * h + 4 * s + 2,
            "n": 2 * h,
            "r": 2 * s + 1,
            "selected_Hasse": hasse,
            "transverse_Q0": q0,
            "finite_log_coefficients": {"c_T": cT, "c_L": cL},
            "base_field_T_two_alias": T_alias,
            "base_field_L_two_alias": L_alias,
            "extension_joint_moment": moment,
            "extension_expected_blocks": expected,
            "finite_log_root_data": root_data,
            "Hasse_zero_transverse_nonzero": hasse == 0 and q0 != 0,
            "transverse_zero_Hasse_nonzero": q0 == 0 and hasse != 0,
            "joint_zero": hasse == 0 and q0 == 0,
        })
    return output


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item366-j1-joint-frobenius-extension-obstruction-certificate-v1",
        "item": 366,
        "date": "2026-09-01",
        "status": "PROVED_EXACT_FRAMED_JOINT_MOMENT_AND_TRACE_DETERMINANT_NO_GO",
        "dependencies": DEPENDENCIES,
        "symbolic_theorem": symbolic_theorem(),
        "representation": {
            "finite_log": "L_p(w)=((1+w)^p-1-w^p)/p mod p",
            "divided_Frobenius_identity": "(1+z^2)^p=(1+z^(2p))+p*L_p(z^2)",
            "unipotent_frame": "U_p(z)=[[1,L_p(z^2)],[0,1]]",
            "Hasse_block": "z^(-n)G(z)^(p-r)",
            "T_block": "2*z^(-T)*P0(z)*U_p(z)",
            "L_block": "-z^(-L)*P0(z)*U_p(z)",
            "joint_rank": 5,
            "field": "F_(p^2)",
            "Hasse_matrix_coefficient": "-a_(2s+1,2h)",
            "transverse_matrix_coefficient": "-Q0",
            "ambient_zero_conditions_imposed": False,
            "genuine_lisse_or_compatible_system_claimed": False,
        },
        "trace_determinant_obstruction": {
            "semisimple_slot": "selected Hasse diagonal block",
            "nilpotent_slot": "transverse divided-Frobenius extension functional",
            "characteristic_polynomial": "X^4*(X+a)",
            "all_trace_powers": "tr(S^k)=(-a)^k",
            "determinant": 0,
            "joint_event": "two specified framed matrix coefficients vanish; no other block entry is required to vanish",
            "conclusion": "ordinary trace/determinant data cannot see the transverse selector",
        },
        "literal_Kummer_obstruction": {
            "derivative": "L_p'(w)=(1-w^(p-1))/(1+w)",
            "root_multiplicity": "every root has multiplicity at most two",
            "distinct_roots_Lp": "at least (p-1)/2 over the algebraic closure",
            "distinct_roots_Lp_z2": "at least p-2",
            "scope": "literal full-order Kummerization of the finite-log factor has linearly growing singular support; this does not rule out a different unipotent F-crystal compression",
        },
        "capacity": {
            "actual_support": "all p=4h+6s+3, M=3h+4s+2 rows",
            "raw_log_mass": "M/6+o(M)",
            "raw_ceiling_per_6M": "1/36",
            "potential_if_weighted_nonconcentration_proved": "remove the full 1/36 ceiling",
            "selector_aware_weighted_theorem_proved": False,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
            "route_1_status": "ACTIVE",
        },
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "exact F_(p^2) rank-five framed divided-Frobenius moment for the actual pair",
                "exact two matrix coefficients equal to the selected Hasse and transverse coordinates",
                "base-field two-alias and two-Euler-moment theorem for each transverse coefficient",
                "trace, determinant, characteristic-polynomial blindness to the transverse extension slot",
                "linear distinct-root lower bound for literal finite-log Kummerization",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "four predeclared rows, including separation controls in both directions; no prime scan",
            ],
            "OPEN": [
                "a genuine bounded-conductor lisse or crystalline joint system",
                "framed extension-class equidistribution or horizontal chosen-prime nonconcentration",
                "a trace replacement sensitive to the nilpotent selector without imposing ambient zeros",
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
        "item": 366,
        "joint_rank": 5,
        "exact_pair_matrix_coefficients": True,
        "trace_determinant_sees_transverse": False,
        "booking": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
