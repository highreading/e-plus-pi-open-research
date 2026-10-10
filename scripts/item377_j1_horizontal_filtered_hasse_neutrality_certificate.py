#!/usr/bin/env python3
"""Deterministic exact replay for Item 377.

This checker verifies the general Frobenius-horizontality equations for
the Item 374 rank-two filtered Hasse extension and exact polynomial
truncations of the normalized-Frobenius resolvent connection.  It also
checks flatness and the dense cotangent support on an independent
coefficient-moment base.  It performs no collision or prime census and
makes no horizontal density inference.
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
DEFAULT_OUTPUT = HERE / "item377_j1_horizontal_filtered_hasse_neutrality_certificate.json"

DEPENDENCIES = {
    "sources/item374_j1_filtered_hasse_extension_realization_report.md":
        "ac04f52132e3355692b1744d625f765dd6b0d1e74f90b123ebd599c135b009d2",
    "scripts/item374_j1_filtered_hasse_extension_realization_certificate.py":
        "45802992e5347d83660a520db3cebd72681908bf80b3406795a594fb514fdfbe",
    "results/item374_j1_filtered_hasse_extension_realization_certificate.json":
        "609f378221a2aafa823947dd967fe0c626df3c74ff726681e406d9b1d4a4fcaf",
    "results/item374_j1_filtered_hasse_extension_realization_certificate_replay.json":
        "609f378221a2aafa823947dd967fe0c626df3c74ff726681e406d9b1d4a4fcaf",
    "results/item374_j1_filtered_hasse_extension_realization_root_replay.json":
        "609f378221a2aafa823947dd967fe0c626df3c74ff726681e406d9b1d4a4fcaf",
    "results/item374_j1_filtered_hasse_extension_realization_ledger_delta.json":
        "3f7fbd0dc0801d84f324fc5f2f426fd00567cb7d79cff895c1c7e09abe5dcfd1",
    "results/item374_j1_filtered_hasse_extension_realization_root_audit.json":
        "c66909a9599e760addcbcc79239646d36889cf7eb6118b97800e5474bf871b6a",
    "manifests/item374_j1_filtered_hasse_extension_realization_manifest.json":
        "5963968673fdb77e53ab4acdce5c1eb5e323491c79ef27a45f5f6ee39d73fcd5",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def symbolic_horizontality() -> dict[str, Any]:
    p, q, dq = S.symbols("p q dq", nonzero=True)
    a, b, c, d = S.symbols("a b c d")
    fa, fb, fc, fd = S.symbols("F_a F_b F_c F_d")

    frobenius = S.Matrix([[p, 0], [p * q, 1]])
    connection = S.Matrix([[a, b], [c, d]])
    pulled_connection = S.Matrix([[fa, fb], [fc, fd]])
    differential = S.Matrix([[0, 0], [p * dq, 0]])
    residual = S.simplify(
        differential + connection * frobenius - frobenius * pulled_connection
    )
    expected = S.Matrix([
        [p * (a + q * b - fa), b - p * fb],
        [p * dq + p * c + p * q * d - p * q * fa - fc,
         d - p * q * fb - fd],
    ])
    assert residual == expected

    omega, c_omega = S.symbols("omega C_omega")
    lower_connection = S.Matrix([[0, 0], [omega, 0]])
    lower_pullback = S.Matrix([[0, 0], [p * c_omega, 0]])
    lower_residual = S.simplify(
        differential + lower_connection * frobenius
        - frobenius * lower_pullback
    )
    expected_lower = S.Matrix([[0, 0], [p * (dq + omega - c_omega), 0]])
    assert lower_residual == expected_lower

    return {
        "full_matrix": [["p", "0"], ["p*q", "1"]],
        "matrix_residual": [
            ["p*(a+q*b-F*a)", "b-p*F*b"],
            ["p*dq+p*c+p*q*d-p*q*F*a-F*c", "d-p*q*F*b-F*d"],
        ],
        "forced_under_p_adic_separation": {
            "b": 0,
            "a": 0,
            "d": 0,
            "remaining_equation": "C(c)-c=dq",
        },
        "lower_residual": "p*(dq+omega-C(omega))*E21",
    }


H, T = S.symbols("H S")


def normalized_frobenius_one_form(
    form: tuple[S.Expr, S.Expr], prime: int
) -> tuple[S.Expr, S.Expr]:
    """C(P dH+Q dS) for F(H)=H^p and F(S)=S^p."""
    left, right = form
    substitution = {H: H ** prime, T: T ** prime}
    return (
        S.expand(left.subs(substitution, simultaneous=True) * H ** (prime - 1)),
        S.expand(right.subs(substitution, simultaneous=True) * T ** (prime - 1)),
    )


def add_forms(
    left: tuple[S.Expr, S.Expr], right: tuple[S.Expr, S.Expr]
) -> tuple[S.Expr, S.Expr]:
    return S.expand(left[0] + right[0]), S.expand(left[1] + right[1])


def scale_form(form: tuple[S.Expr, S.Expr], scalar: int) -> tuple[S.Expr, S.Expr]:
    return S.expand(scalar * form[0]), S.expand(scalar * form[1])


def differential(polynomial: S.Expr) -> tuple[S.Expr, S.Expr]:
    return S.diff(polynomial, H), S.diff(polynomial, T)


def exterior_derivative(form: tuple[S.Expr, S.Expr]) -> S.Expr:
    # d(P dH+Q dS)=(d_H Q-d_S P)dH wedge dS.
    return S.expand(S.diff(form[1], H) - S.diff(form[0], T))


def polynomial_resolvent_control(
    prime: int, polynomial: S.Expr, depth: int
) -> dict[str, Any]:
    dq = differential(polynomial)
    current = dq
    omega = (S.Integer(0), S.Integer(0))
    for _ in range(depth):
        omega = add_forms(omega, scale_form(current, -1))
        current = normalized_frobenius_one_form(current, prime)

    telescoping = add_forms(
        add_forms(normalized_frobenius_one_form(omega, prime), scale_form(omega, -1)),
        scale_form(dq, -1),
    )
    expected = scale_form(current, -1)
    assert tuple(map(S.expand, telescoping)) == tuple(map(S.expand, expected))
    assert exterior_derivative(omega) == 0

    initial_orders: list[int] = []
    probe = dq
    for _ in range(depth + 1):
        monomials = []
        for coefficient in probe:
            poly = S.Poly(coefficient, H, T)
            for (u, v), value in poly.terms():
                if value:
                    monomials.append(u + v)
        initial_orders.append(min(monomials) if monomials else -1)
        probe = normalized_frobenius_one_form(probe, prime)

    return {
        "prime": prime,
        "q": str(S.expand(polynomial)),
        "depth": depth,
        "telescoping_identity": "C(omega_N)-omega_N-dq=-C^N(dq)",
        "telescoping_verified": True,
        "flatness_verified": True,
        "orders_of_Cj_dq": initial_orders,
    }


def dense_cotangent_control(number_of_coordinates: int) -> dict[str, Any]:
    variables = S.symbols(f"y0:{number_of_coordinates}")
    q = sum(variables)
    gradient = [S.diff(q, variable) for variable in variables]
    omega_mod_maximal = [-value for value in gradient]
    assert omega_mod_maximal == [-1] * number_of_coordinates
    return {
        "independent_coordinates": number_of_coordinates,
        "q": "+".join(str(variable) for variable in variables),
        "omega_mod_maximal_coefficients": [int(value) for value in omega_mod_maximal],
        "cotangent_support": number_of_coordinates,
        "general_identity": "omega_q mod m*Omega=-sum_i dy_i",
    }


def build_certificate() -> dict[str, Any]:
    controls = [
        polynomial_resolvent_control(3, H + T, 4),
        polynomial_resolvent_control(3, H + 2 * T + H * T + H ** 2 * T, 3),
        polynomial_resolvent_control(5, 2 * H + 3 * T + H * T ** 2 + H ** 3, 3),
    ]
    return {
        "item": 377,
        "schema": "item377-j1-horizontal-filtered-hasse-neutrality-certificate-v1",
        "classification": "PROVED_SCOPED_HORIZONTALITY_INFORMATION_NEUTRAL_NO_GO",
        "checked_date_beijing": "2026-09-01",
        "scope": {
            "actual_selector": "p=4h+6s+3, M=3h+4s+2, n=2h, r=2s+1",
            "base": "W(k)[[H,S]] with F(H)=H^p and F(S)=S^p",
            "gate_direction": "full collision => a_(r,n)=0 and Q0=0 mod p",
            "converse_claimed": False,
        },
        "dependencies": DEPENDENCIES,
        "symbolic_horizontality": symbolic_horizontality(),
        "horizontal_neutrality_theorem": {
            "general_connection": "Gamma=[[a,b],[c,d]]",
            "unique_connection": "Gamma_q=E21*omega_q",
            "omega_q": "-sum_(j>=0) C^j(dq)",
            "C": "F_Omega^*/p",
            "convergence": "(H,S)-adic",
            "integrable": True,
            "Griffiths_transverse": True,
            "divided_Frobenius_horizontal": True,
            "all_q_allowed": True,
            "new_differential_constraint_on_q": False,
        },
        "exact_polynomial_controls": controls,
        "dense_coefficient_moment_control": dense_cotangent_control(11),
        "inherited_actual_support": {
            "nonidentity_factors_lower_bound": "p^2-1-[4+2(p-1)+2|h-s|]",
            "asymptotic": "p^2-O(p)",
            "claim_type": "coefficient-support, not geometric conductor after pullback",
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
                "general matrix horizontality equations",
                "unique integral flat Griffiths-transverse connection for every q",
                "fixed-rank fixed-Hodge horizontality-information-neutral no-go",
                "dense cotangent support on the universal coefficient-moment base",
                "zero booking",
            ],
            "DECLARED_EXACT_CONTROLS_ONLY": [
                "three polynomial normalized-Frobenius resolvent controls",
                "one eleven-coordinate dense-cotangent control",
                "no prime or collision scan",
            ],
            "OPEN": [
                "prime-independent bounded-complexity geometry realizing the actual cross-prime Q0",
                "bounded conductor after pullback to the tied selector",
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
        "item": 377,
        "all_q_allowed": True,
        "horizontal_connection_unique": True,
        "new_differential_constraint": False,
        "weighted_theorem": False,
        "booking": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
