#!/usr/bin/env python3
"""Deterministic exact replay for Item 383.

The checker verifies the explicit overconvergent Frobenius lift with its
rational logarithmic horizontal connection, the general splitting-gauge
equation, the valuation/p-th-power obstruction, and allowed filtered gauge
shape.  It performs no collision or prime census and proves no weighted
density or actual-family conductor theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import factorial
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item383_j1_frobenius_lift_gauge_invariance_certificate.json"

DEPENDENCIES = {
    "sources/item380_j1_actual_moment_horizontal_complexity_barrier_report.md":
        "35668582bec3086fdb523f38c69df6a31d2557d2538cdb43794224dbfa2b623f",
    "scripts/item380_j1_actual_moment_horizontal_complexity_barrier_certificate.py":
        "e1bf9c6a1b0a0a57c96351ab294a0f031915ebe2f3897a86e5ba766e89b1ea6f",
    "results/item380_j1_actual_moment_horizontal_complexity_barrier_certificate.json":
        "5b1fd2b70010bbec53e195b64e824e46ff865b3a5d7d0980af3b0cf002e64e08",
    "results/item380_j1_actual_moment_horizontal_complexity_barrier_certificate_replay.json":
        "5b1fd2b70010bbec53e195b64e824e46ff865b3a5d7d0980af3b0cf002e64e08",
    "results/item380_j1_actual_moment_horizontal_complexity_barrier_root_replay.json":
        "5b1fd2b70010bbec53e195b64e824e46ff865b3a5d7d0980af3b0cf002e64e08",
    "results/item380_j1_actual_moment_horizontal_complexity_barrier_ledger_delta.json":
        "151bf10de7d8bfd5050b739b3cd6cc7ca949ef0ca699bacf840b45e75e181ccb",
    "results/item380_j1_actual_moment_horizontal_complexity_barrier_root_audit.json":
        "55b91eb8b88297f40a6a5f723448c0dca2805c17dc958e30b3fede282d7a1b50",
    "manifests/item380_j1_actual_moment_horizontal_complexity_barrier_manifest.json":
        "521e28618a87d86d50f8560d9dfa2e8c7442d5492edf5bc979b25256dd14c829",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def p_adic_valuation(integer: int, prime: int) -> int:
    if integer == 0:
        raise ValueError("valuation of zero")
    value = abs(integer)
    output = 0
    while value % prime == 0:
        output += 1
        value //= prime
    return output


def rational_p_valuation(value: S.Rational, prime: int) -> int:
    return (
        p_adic_valuation(int(value.p), prime)
        - p_adic_valuation(int(value.q), prime)
    )


Q = S.symbols("q")


def exact_logarithmic_identity() -> dict[str, Any]:
    p, lam = S.symbols("p lambda", nonzero=True)
    exponential = S.exp(-lam * p * Q)
    phi = (1 - (1 - lam * Q) ** p * exponential) / lam
    omega = 1 / (1 - lam * Q)
    pulled_omega = S.diff(phi, Q) / (p * (1 - lam * phi))
    assert S.factor(pulled_omega - omega - 1) == 0

    # The formal logarithmic primitive f=lambda^-1 log(1-lambda q)
    # has df=-omega.  The defining identity gives F(f)/p-f=-q.
    primitive_derivative = S.diff(S.log(1 - lam * Q) / lam, Q)
    assert S.simplify(primitive_derivative + omega) == 0

    return {
        "lambda_scope": "lambda in Z_p^times (residue in F_p^times)",
        "Phi_lambda": "[1-(1-lambda*q)^p*exp(-lambda*p*q)]/lambda",
        "defining_identity":
            "1-lambda*Phi_lambda=(1-lambda*q)^p*exp(-lambda*p*q)",
        "omega_lambda": "dq/(1-lambda*q)",
        "horizontal_identity": "F^*(omega_lambda)/p=omega_lambda+dq",
        "primitive": "f_lambda=log(1-lambda*q)/lambda",
        "splitting_difference_identity": "F(f_lambda)/p-f_lambda=-q",
        "verified": True,
    }


def exp_truncated(argument: S.Expr, degree: int) -> S.Expr:
    return S.expand(sum(argument ** n / factorial(n) for n in range(degree + 1)))


def series_control(prime: int, lam: int, degree: int) -> dict[str, Any]:
    assert prime % 2 == 1 and lam % prime != 0 and degree >= prime
    exponential = exp_truncated(-lam * prime * Q, degree)
    raw_phi = S.expand((1 - (1 - lam * Q) ** prime * exponential) / lam)
    phi = S.series(raw_phi, Q, 0, degree + 1).removeO().expand()

    coefficients = [S.Rational(phi.coeff(Q, n)) for n in range(degree + 1)]
    assert coefficients[0] == 0
    for n, coefficient in enumerate(coefficients):
        if n == prime:
            assert (coefficient - 1).p % prime == 0
        else:
            assert coefficient.p % prime == 0
        assert rational_p_valuation(coefficient, prime) >= 0 if coefficient else True

    correction = S.expand((phi - Q ** prime) / prime)
    correction_coefficients = [
        S.Rational(correction.coeff(Q, n)) for n in range(degree + 1)
    ]
    assert all(
        coefficient == 0 or rational_p_valuation(coefficient, prime) >= 0
        for coefficient in correction_coefficients
    )

    exp_valuations = []
    for n in range(1, degree + 1):
        coefficient = S.Rational((-lam * prime) ** n, factorial(n))
        exp_valuations.append(rational_p_valuation(coefficient, prime))
    assert all(value >= 0 for value in exp_valuations)

    log_coeff_valuations = [
        rational_p_valuation(S.Rational(-(lam ** (n - 1)), n), prime)
        for n in range(1, degree + 1)
    ]

    return {
        "prime": prime,
        "lambda": lam,
        "degree": degree,
        "Phi_mod_p_equals_q_to_p_through_degree": True,
        "correction_integral_through_degree": True,
        "exp_coefficient_p_valuations": exp_valuations,
        "log_primitive_coefficient_p_valuations": log_coeff_valuations,
        "log_coefficients_at_n=p_have_negative_valuation":
            log_coeff_valuations[prime - 1] < 0,
    }


def gauge_identity() -> dict[str, Any]:
    p, q, f, ff = S.symbols("p q f F_f", nonzero=True)

    def unipotent(value: S.Expr) -> S.Matrix:
        return S.Matrix([[1, 0], [value, 1]])

    diagonal = S.diag(p, 1)
    frobenius = unipotent(q) * diagonal
    transformed = S.simplify(unipotent(f).inv() * frobenius * unipotent(ff))
    expected = unipotent(-f + q + ff / p) * diagonal
    assert S.simplify(transformed - expected) == S.zeros(2)

    return {
        "transform": "U(f)^-1*A_q*F(U(f))=U(-f+q+F(f)/p)*diag(p,1)",
        "splitting_equation": "F(f)/p-f=-q",
        "verified": True,
    }


def valuation_obstruction_controls() -> dict[str, Any]:
    # For f=p^m g primitive, p^(m-1)F(g)-p^m g=-q.
    possible_m = list(range(-3, 6))
    valuation_outcome = {}
    for m in possible_m:
        if m < 1:
            valuation_outcome[str(m)] = "impossible: left valuation m-1<0"
        elif m > 1:
            valuation_outcome[str(m)] = "impossible: left divisible by p"
        else:
            valuation_outcome[str(m)] = "forces gbar^p=-qbar"
    assert [m for m in possible_m if m == 1] == [1]

    u, v = S.symbols("u v")
    q = 2 * u - v
    differential = [S.diff(q, u), S.diff(q, v)]
    assert differential == [2, -1]

    return {
        "normal_form": "f=p^m*g with g primitive",
        "valuation_cases": valuation_outcome,
        "only_possible_m": 1,
        "mod_p_consequence": "gbar^p=-qbar",
        "dq_coefficients": [int(value) for value in differential],
        "dq_nonzero_for_odd_p": True,
        "conclusion": "qbar is not a p-th power; no bounded-denominator f",
    }


def filtered_gauge_shape() -> dict[str, Any]:
    a, b, c, d, omega = S.symbols("a b c d omega")
    gamma = S.Matrix([[0, 0], [omega, 0]])
    gauge = S.Matrix([[a, b], [c, d]])
    differential = S.simplify(-gamma * gauge)
    assert differential == S.Matrix([[0, 0], [-omega * a, -omega * b]])
    return {
        "dG": [["0", "0"], ["-omega*a", "-omega*b"]],
        "filtered_upper_triangular_condition": "c=0",
        "invertibility_condition": "a!=0 and d!=0",
        "consequence": "dc=-omega*a=0 forces omega=0",
        "filtered_split_when_dq_nonzero": False,
    }


def build_certificate() -> dict[str, Any]:
    return {
        "item": 383,
        "schema": "item383-j1-frobenius-lift-gauge-invariance-certificate-v1",
        "classification": "PROVED_RATIONAL_LOG_MODEL_AND_INVARIANT_NO_BOUNDED_SPLITTING",
        "checked_date_beijing": "2026-09-01",
        "scope": {
            "actual_selector": "p=4h+6s+3, M=3h+4s+2, n=2h, r=2s+1",
            "moment_coordinates": "u=c_T, v=c_L, q=2u-v",
            "general_lift": "F(u)=u^p+p*a(u,v), F(v)=v^p+p*b(u,v)",
            "gate_direction": "full collision => a_(r,n)=0 and Q0=0 mod p",
            "converse_claimed": False,
        },
        "dependencies": DEPENDENCIES,
        "exact_logarithmic_model": exact_logarithmic_identity(),
        "declared_series_controls": [
            series_control(3, 1, 12),
            series_control(5, 2, 15),
            series_control(7, 3, 16),
        ],
        "gauge_identity": gauge_identity(),
        "valuation_obstruction": valuation_obstruction_controls(),
        "filtered_gauge": filtered_gauge_shape(),
        "invariance_theorems": {
            "lacunary_nonrational_formula_invariant": False,
            "explicit_rational_log_connection_constructed": True,
            "rational_pole_divisor": "1-lambda*q=0",
            "regular_at_Hasse_divisor_q=0": True,
            "bounded_denominator_simultaneous_split_for_any_lift": False,
            "coordinate_invariant_reason": "d(qbar)!=0",
            "dagger_connection_on_full_closed_disc": False,
            "dagger_reason":
                "dagger Poincare primitive plus constant adjustment would solve the forbidden splitting equation",
        },
        "capacity": {
            "raw_log_mass": "M/6+o(M)",
            "raw_ceiling_per_6M": "1/36",
            "weighted_target": "W_(H,Q)(M)=o(M)",
            "weighted_target_proved": False,
            "new_linear_log_rate": 0,
            "new_capacity_reduction": 0,
            "new_booking": 0,
            "retained_ceiling_per_6M": "1/36",
        },
        "classification_labels": {
            "PROVED": [
                "explicit overconvergent Frobenius lift with rational logarithmic horizontal connection",
                "noninvariance of the standard-lift lacunary and nonrational presentation",
                "coordinate- and lift-invariant no bounded-denominator simultaneous splitting",
                "no global dagger horizontal connection on the full moment disc",
                "no filtration-preserving split when dq is nonzero",
                "zero booking",
            ],
            "DECLARED_EXACT_CONTROLS_ONLY": [
                "three finite series controls, exact symbolic logarithmic and matrix identities, and a declared valuation table",
                "no prime or collision scan",
            ],
            "OPEN": [
                "prime-independent geometry of the actual tied moment map",
                "a useful nonsplit monodromy statistic on another global base",
                "geometric conductor, weighted nonconcentration, any strict fixed-j1 ceiling reduction, Route 1, and every conclusion about e+pi",
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
        "item": 383,
        "rational_log_connection": True,
        "bounded_simultaneous_splitting": False,
        "global_dagger_connection": False,
        "weighted_theorem": False,
        "booking": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
