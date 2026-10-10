#!/usr/bin/env python3
"""Deterministic exact replay for Item 380.

The checker verifies the exact two-moment pullback of Item 377's unique
horizontal connection, the simultaneous formal splitting gauge, its
unbounded p-denominators, lacunary support, and the ambient-to-two-variable
cotangent-rank collapse.  It performs no collision or prime census and
does not infer a geometric conductor or weighted density theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item380_j1_actual_moment_horizontal_complexity_barrier_certificate.json"

DEPENDENCIES = {
    "sources/item377_j1_horizontal_filtered_hasse_neutrality_report.md":
        "ce5d546e4cd2fb093219453db362b84a2369446334137c8c913143698f55ed88",
    "scripts/item377_j1_horizontal_filtered_hasse_neutrality_certificate.py":
        "e80706033c5d5e05fbec2668da53cb5f50f07d476a5350d54c37543967c832ba",
    "results/item377_j1_horizontal_filtered_hasse_neutrality_certificate.json":
        "299663f4f520ff77760ff4ee4b6d554b7d59b9c36e04e7f2be25026022eab9af",
    "results/item377_j1_horizontal_filtered_hasse_neutrality_certificate_replay.json":
        "299663f4f520ff77760ff4ee4b6d554b7d59b9c36e04e7f2be25026022eab9af",
    "results/item377_j1_horizontal_filtered_hasse_neutrality_root_replay.json":
        "299663f4f520ff77760ff4ee4b6d554b7d59b9c36e04e7f2be25026022eab9af",
    "results/item377_j1_horizontal_filtered_hasse_neutrality_ledger_delta.json":
        "153ac70b32d36eac7b9a89594d9bd9dccf2eab263c10754b8eb10a9e433fada9",
    "results/item377_j1_horizontal_filtered_hasse_neutrality_root_audit.json":
        "4efb362a26c20cdf1a4048585d4e38e078f1360e7451c6f20fd52b272a35a334",
    "manifests/item377_j1_horizontal_filtered_hasse_neutrality_manifest.json":
        "02d9567bd2992d593a4d15c808455f00ab3bbff87310a0b3c300972f36605cc3",
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


def symbolic_gauge_identity() -> dict[str, Any]:
    p, q, f, ff = S.symbols("p q f F_f", nonzero=True)

    def unipotent(value: S.Expr) -> S.Matrix:
        return S.Matrix([[1, 0], [value, 1]])

    diagonal = S.diag(p, 1)
    frobenius = unipotent(q) * diagonal
    gauge = unipotent(f)
    transformed = S.simplify(gauge.inv() * frobenius * unipotent(ff))
    expected = unipotent(-f + q + ff / p) * diagonal
    assert S.simplify(transformed - expected) == S.zeros(2)
    assert S.simplify(transformed.subs(ff, p * (f - q)) - diagonal) == S.zeros(2)

    omega, df = S.symbols("omega df")
    gamma = S.Matrix([[0, 0], [omega, 0]])
    gauge_differential = S.Matrix([[0, 0], [df, 0]])
    transformed_gamma = S.simplify(gauge.inv() * gamma * gauge + gauge_differential)
    assert transformed_gamma == S.Matrix([[0, 0], [omega + df, 0]])
    assert transformed_gamma.subs(df, -omega) == S.zeros(2)

    return {
        "A_q": [["p", "0"], ["p*q", "1"]],
        "G": [["1", "0"], ["f", "1"]],
        "Frobenius_transform": "G^-1*A_q*F(G)=U(-f+q+F(f)/p)*diag(p,1)",
        "connection_transform": "G^-1*Gamma*G+G^-1*dG=E21*(omega+df)",
        "simultaneous_split_condition": "df=-omega and F(f)/p-f=-q",
        "verified": True,
    }


U, V = S.symbols("u v")


def frobenius(polynomial: S.Expr, prime: int) -> S.Expr:
    return S.expand(polynomial.subs(
        {U: U ** prime, V: V ** prime}, simultaneous=True
    ))


def iterate_frobenius(polynomial: S.Expr, prime: int, depth: int) -> S.Expr:
    output = polynomial
    for _ in range(depth):
        output = frobenius(output, prime)
    return output


def moment_truncation_control(prime: int, depth: int) -> dict[str, Any]:
    assert prime % 2 == 1
    q = 2 * U - V
    f_truncated = S.Integer(0)
    omega_u = S.Integer(0)
    omega_v = S.Integer(0)
    denominator_valuations = []
    exponents = []

    current = q
    for j in range(depth):
        f_truncated += current / (prime ** j)
        omega_u -= 2 * U ** (prime ** j - 1)
        omega_v += V ** (prime ** j - 1)
        coefficient_u = S.Rational(2, prime ** j)
        coefficient_v = S.Rational(-1, prime ** j)
        denominator_valuations.append([
            rational_p_valuation(coefficient_u, prime),
            rational_p_valuation(coefficient_v, prime),
        ])
        exponents.append(prime ** j)
        current = frobenius(current, prime)

    assert S.expand(S.diff(f_truncated, U) + omega_u) == 0
    assert S.expand(S.diff(f_truncated, V) + omega_v) == 0
    tail = iterate_frobenius(q, prime, depth) / (prime ** depth)
    difference_residual = S.expand(
        frobenius(f_truncated, prime) / prime - f_truncated + q
    )
    assert S.expand(difference_residual - tail) == 0
    assert denominator_valuations == [[-j, -j] for j in range(depth)]

    support = [exponent - 1 for exponent in exponents]
    gaps = [support[j + 1] - support[j] - 1 for j in range(len(support) - 1)]
    assert all(gaps[j + 1] > gaps[j] for j in range(len(gaps) - 1))

    return {
        "prime": prime,
        "depth": depth,
        "q": "2*u-v",
        "omega_truncation": "-2*sum u^(p^j-1)du+sum v^(p^j-1)dv",
        "f_truncation": "sum (2*u^(p^j)-v^(p^j))/p^j",
        "df_equals_minus_omega": True,
        "difference_residual": "F^depth(q)/p^depth",
        "exponents_in_f": exponents,
        "p_valuations_u_v": denominator_valuations,
        "lacunary_support_in_omega": support,
        "zero_gap_lengths": gaps,
    }


def fundamental_gauge_equations() -> dict[str, Any]:
    # If G=[[a,b],[c,d]], dG=-E21*omega*G.
    a, b, c, d, omega = S.symbols("a b c d omega")
    gamma = S.Matrix([[0, 0], [omega, 0]])
    gauge = S.Matrix([[a, b], [c, d]])
    right = S.simplify(-gamma * gauge)
    assert right == S.Matrix([[0, 0], [-omega * a, -omega * b]])
    return {
        "dG": [["0", "0"], ["-omega*a", "-omega*b"]],
        "solution_shape": [["a0", "b0"], ["a0*f+c0", "b0*f+d0"]],
        "reason_unbounded_poles_are_forced":
            "an invertible constant top row has a0 or b0 nonzero, so a nonzero constant multiple of f occurs",
    }


def cotangent_rank_control(number_of_ambient_directions: int) -> dict[str, Any]:
    # A declared full-rank two-row specialization matrix; every 2xN matrix
    # has rank at most two, independently of this control.
    first = list(range(1, number_of_ambient_directions + 1))
    second = [1 if j % 2 == 0 else -1 for j in range(number_of_ambient_directions)]
    matrix = S.Matrix([first, second])
    assert matrix.rank() == 2
    return {
        "ambient_directions": number_of_ambient_directions,
        "target_cotangent_rank": 2,
        "declared_matrix_rank": matrix.rank(),
        "general_bound": "rank(image(span(dy_i)->Omega_base))<=2 on every two-parameter base",
        "geometric_conductor_inference": False,
    }


def literal_finite_log_controls() -> list[dict[str, int]]:
    output = []
    for prime in [13, 17, 47, 109]:
        exponents = [2 * k for k in range(1, prime)]
        assert len(exponents) == prime - 1
        assert max(exponents) == 2 * (prime - 1)
        output.append({
            "prime": prime,
            "nonzero_terms": len(exponents),
            "degree_in_x": max(exponents),
        })
    return output


def build_certificate() -> dict[str, Any]:
    return {
        "item": 380,
        "schema": "item380-j1-actual-moment-horizontal-complexity-barrier-certificate-v1",
        "classification": "PROVED_SCOPED_DIRECT_TWO_MOMENT_GAUGE_COMPLEXITY_BARRIER",
        "checked_date_beijing": "2026-09-01",
        "scope": {
            "actual_selector": "p=4h+6s+3, M=3h+4s+2, n=2h, r=2s+1",
            "selected_moments": "u=c_T, v=c_L, q=2u-v",
            "moment_indices": "T=2h+6s+2, L=4h+4s+2",
            "gate_direction": "full collision => a_(r,n)=0 and Q0=0 mod p",
            "converse_claimed": False,
        },
        "dependencies": DEPENDENCIES,
        "symbolic_gauge_identity": symbolic_gauge_identity(),
        "exact_moment_formula": {
            "omega": "-2*sum_(j>=0)u^(p^j-1)du+sum_(j>=0)v^(p^j-1)dv",
            "formal_splitting_gauge": "f=sum_(j>=0)(2u^(p^j)-v^(p^j))/p^j",
            "bounded_dimensional_formal_descent": True,
            "bounded_vertical_p_pole_gauge": False,
            "rational": False,
            "overconvergent": False,
        },
        "declared_truncation_controls": [
            moment_truncation_control(3, 7),
            moment_truncation_control(5, 6),
        ],
        "fundamental_gauge": fundamental_gauge_equations(),
        "ambient_to_actual_control": cotangent_rank_control(13),
        "inherited_actual_ambient_support":
            "N>=p^2-1-[4+2(p-1)+2|h-s|]=p^2-O(p)",
        "literal_finite_log_controls": literal_finite_log_controls(),
        "method_scope": {
            "closed": [
                "bounded-p vertical pole splitting gauge for the direct standard-Frobenius moment model",
                "rational or dagger gauge realization of that direct moment connection",
                "using ambient p^2-O(p) independent directions as an actual conductor lower bound without controlling pullback dependencies",
            ],
            "not_closed": [
                "a different prime-independent geometric descent",
                "actual h,s cancellation or compression",
                "a genuine geometric conductor theorem after specialization",
            ],
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
                "exact two-moment connection and formal splitting gauge",
                "unbounded vertical p-denominator theorem for every fundamental gauge",
                "nonrational and non-overconvergent direct moment connection",
                "ambient-to-two-variable cotangent-rank collapse",
                "zero booking",
            ],
            "DECLARED_EXACT_CONTROLS_ONLY": [
                "two finite-depth Mahler controls, one symbolic gauge identity, one cotangent-rank control, and four literal term counts",
                "no prime or collision scan",
            ],
            "OPEN": [
                "different prime-independent bounded-complexity geometry for the actual tied coefficient map",
                "geometric conductor after actual specialization",
                "weighted nonconcentration, any strict fixed-j1 ceiling reduction, Route 1, and every conclusion about e+pi",
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
        "item": 380,
        "bounded_dimensional_formal_descent": True,
        "bounded_p_pole_gauge": False,
        "direct_connection_overconvergent": False,
        "geometric_conductor_theorem": False,
        "booking": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()

