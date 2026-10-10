#!/usr/bin/env python3
"""Deterministic exact replay for Item 360.

This checker reconstructs the two original Item 218 divided common-log
coordinates before the factorial-ratio elimination.  It verifies the exact
principal elimination ideal obtained when that ratio is forgotten, the
prime codimension-two ideal on the actual tied fiber, its two primary chart
decompositions, and the original first coordinate as a transverse parameter-
derivative period.  No prime scan or density inference is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item360_j1_full_gate_transverse_period_certificate.json"

DEPENDENCIES = {
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "scripts/item218_j1_common_log_certificate.py":
        "a238c5ca37263f2553da47bf3f21253aedf1c34f8c57458a4a274fc6cdc9029a",
    "results/item218_j1_common_log_certificate.json":
        "963bbb8a9758e55ede72f965693d21fc41aa70d44e2d981d5873685c3f08ea0f",
    "results/item218_j1_common_log_certificate.replay.json":
        "963bbb8a9758e55ede72f965693d21fc41aa70d44e2d981d5873685c3f08ea0f",
    "results/item218_j1_common_log_manifest.json":
        "e1c6c3d713670c819b5f27b1005db26f9b804ec8ee0766671928fc30c1ff6d8d",
    "sources/item357_j1_gross_koblitz_unit_face_obstruction_report.md":
        "637c5faa455e894a70a3c5963f89f3db51c06651ed591f8714d28fd67e2e398e",
    "scripts/item357_j1_gross_koblitz_unit_face_obstruction_certificate.py":
        "4991e2a4412b6b9094d70f1724062ddcf5eadc19a24bedaf7a1837072ba6c6b1",
    "results/item357_j1_gross_koblitz_unit_face_obstruction_certificate.json":
        "8dd11773d7744fd364402406e88f5d4fcb6dedd7b449000bb11b83996dce3e51",
    "results/item357_j1_gross_koblitz_unit_face_obstruction_certificate_replay.json":
        "8dd11773d7744fd364402406e88f5d4fcb6dedd7b449000bb11b83996dce3e51",
    "results/item357_j1_gross_koblitz_unit_face_obstruction_root_replay.json":
        "8dd11773d7744fd364402406e88f5d4fcb6dedd7b449000bb11b83996dce3e51",
    "results/item357_j1_gross_koblitz_unit_face_obstruction_ledger_delta.json":
        "e258e7d9280e465553efaa37eb133a4bbbe91ac43432bc771c98b4022c917661",
    "results/item357_j1_gross_koblitz_unit_face_obstruction_self_audit.json":
        "281a70d3187def827dea0ec89d46d15a5d3653d65d7255f2c9a335cab67ac695",
    "results/item357_j1_gross_koblitz_unit_face_obstruction_root_audit.json":
        "8cda5a1377862d780c5501ea8f0c796ac5eba0140b97158bef998468c5e86f94",
    "manifests/item357_j1_gross_koblitz_unit_face_obstruction_manifest.json":
        "c46800cdfd12db0a72c81e04f8a7f24856f8d5097f4915233d06681fa873526d",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pin_dependencies()
ITEM218 = load_module(
    "item360_pinned_item218",
    ROOT / "scripts/item218_j1_common_log_certificate.py",
)


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return output


def polynomial_power(base: list[int], exponent: int) -> list[int]:
    output = [1]
    while exponent:
        if exponent & 1:
            output = polynomial_multiply(output, base)
        base = polynomial_multiply(base, base)
        exponent //= 2
    return output


def h0_log_coefficient(polynomial: list[int], index: int) -> Fraction:
    """[z^index] P(z) log(1+z^2), exactly over Q."""
    output = Fraction(0)
    for k in range(1, index // 2 + 1):
        degree = index - 2 * k
        if degree < len(polynomial):
            output += Fraction(((-1) ** (k - 1)) * polynomial[degree], k)
    return output


def transverse_period_rational(h: int, s: int) -> Fraction:
    p0 = polynomial_multiply(
        polynomial_multiply(
            polynomial_power([1, -1], 2 * h),
            [1, 1],
        ),
        polynomial_power([1, 0, 1], 2 * s),
    )
    target = 2 * h + 6 * s + 2
    left = 4 * h + 4 * s + 2
    return 2 * h0_log_coefficient(p0, target) - h0_log_coefficient(p0, left)


def reduce_fraction(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise AssertionError("nonunit period denominator")
    return value.numerator * pow(value.denominator, -1, prime) % prime


def positive_prefix(r: int, n: int) -> int:
    return sum(
        comb(r + k - 1, k) * comb(4 * r + n - 1, n - 4 * k)
        for k in range(n // 4 + 1)
    )


def rising(start: int, length: int) -> int:
    output = 1
    for offset in range(length):
        output *= start + offset
    return output


def ideal_contains(groebner: S.GroebnerBasis, polynomials: list[S.Expr]) -> bool:
    return all(S.expand(groebner.reduce(polynomial)[1]) == 0 for polynomial in polynomials)


def symbolic_elimination() -> dict[str, Any]:
    x, y, u, v, lam, alpha, beta, w = S.symbols(
        "x y u v lambda alpha beta w"
    )
    f0 = 2 * x - lam * y
    f1 = 2 * alpha * u - beta * lam * v
    hasse = beta * x * v - alpha * u * y

    if S.expand(beta * v * f0 - y * f1 - 2 * hasse) != 0:
        raise AssertionError("gate syzygy")
    resultant = S.factor(S.resultant(f0, f1, lam))
    if S.expand(resultant - 2 * hasse) != 0:
        raise AssertionError(("lambda resultant", resultant))

    universal_domain = S.QQ.frac_field(alpha, beta)
    universal = S.groebner(
        [f0, f1], lam, x, y, u, v, order="lex", domain=universal_domain
    )
    eliminated = [
        polynomial.as_expr()
        for polynomial in universal.polys
        if not polynomial.as_expr().has(lam)
    ]
    principal = S.groebner(
        [hasse], x, y, u, v, order="lex", domain=universal_domain
    )
    if not eliminated or not ideal_contains(principal, eliminated):
        raise AssertionError("principal universal elimination")
    eliminated_basis = S.groebner(
        eliminated, x, y, u, v, order="lex", domain=universal_domain
    )
    if not ideal_contains(eliminated_basis, [hasse]):
        raise AssertionError("elimination misses Hasse generator")

    ell = S.symbols("ell")
    actual_domain = S.QQ.frac_field(alpha, beta, ell)
    actual_f0 = S.expand(f0.subs(lam, ell))
    actual_f1 = S.expand(f1.subs(lam, ell))
    actual_hasse = hasse
    actual_gate = S.groebner(
        [actual_f0, actual_f1],
        x,
        y,
        u,
        v,
        order="lex",
        domain=actual_domain,
    )
    if not ideal_contains(actual_gate, [actual_hasse]):
        raise AssertionError("Hasse not in actual gate")
    if S.expand(actual_gate.reduce(actual_f0)[1]) != 0:
        raise AssertionError("actual f0")
    actual_principal = S.groebner(
        [actual_hasse],
        x,
        y,
        u,
        v,
        order="lex",
        domain=actual_domain,
    )
    if S.expand(actual_principal.reduce(actual_f0)[1]) == 0:
        raise AssertionError("transverse form incorrectly principal")

    # Intersection I_actual intersect <x,y> by the standard w-elimination.
    intersection_xy_full = S.groebner(
        [
            w * actual_f0,
            w * actual_f1,
            (1 - w) * x,
            (1 - w) * y,
        ],
        w,
        x,
        y,
        u,
        v,
        order="lex",
        domain=actual_domain,
    )
    intersection_xy = [
        polynomial.as_expr()
        for polynomial in intersection_xy_full.polys
        if not polynomial.as_expr().has(w)
    ]
    expected_xy = S.groebner(
        [actual_f0, actual_hasse],
        x,
        y,
        u,
        v,
        order="lex",
        domain=actual_domain,
    )
    intersection_xy_basis = S.groebner(
        intersection_xy,
        x,
        y,
        u,
        v,
        order="lex",
        domain=actual_domain,
    )
    if not ideal_contains(expected_xy, intersection_xy):
        raise AssertionError("xy intersection upper inclusion")
    if not ideal_contains(intersection_xy_basis, [actual_f0, actual_hasse]):
        raise AssertionError("xy intersection lower inclusion")

    # Symmetric intersection I_actual intersect <u,v>.
    intersection_uv_full = S.groebner(
        [
            w * actual_f0,
            w * actual_f1,
            (1 - w) * u,
            (1 - w) * v,
        ],
        w,
        x,
        y,
        u,
        v,
        order="lex",
        domain=actual_domain,
    )
    intersection_uv = [
        polynomial.as_expr()
        for polynomial in intersection_uv_full.polys
        if not polynomial.as_expr().has(w)
    ]
    expected_uv = S.groebner(
        [actual_f1, actual_hasse],
        x,
        y,
        u,
        v,
        order="lex",
        domain=actual_domain,
    )
    intersection_uv_basis = S.groebner(
        intersection_uv,
        x,
        y,
        u,
        v,
        order="lex",
        domain=actual_domain,
    )
    if not ideal_contains(expected_uv, intersection_uv):
        raise AssertionError("uv intersection upper inclusion")
    if not ideal_contains(intersection_uv_basis, [actual_f1, actual_hasse]):
        raise AssertionError("uv intersection lower inclusion")

    # A concrete Hasse-zero point with nonzero transverse coordinate proves
    # strictness without relying only on degree/codimension language.
    witness = {x: 1, y: 0, u: 0, v: 0}
    if S.expand(actual_hasse.subs(witness)) != 0:
        raise AssertionError("principal witness")
    if S.expand(actual_f0.subs(witness)) == 0:
        raise AssertionError("transverse witness")

    return {
        "normalized_gate": {
            "f0": "2x-lambda*y",
            "f1": "2alpha*u-beta*lambda*v",
            "alpha": "-3(3s+1)/(2s)",
            "beta": "(2s+h+1)/(2s)",
        },
        "syzygy": "beta*v*f0-y*f1=2H",
        "H": "beta*x*v-alpha*u*y",
        "forget_lambda_elimination_ideal": "<H>",
        "forget_lambda_codimension": 1,
        "actual_lambda_fiber_ideal": "<f0,f1>",
        "actual_lambda_fiber_prime": True,
        "actual_lambda_fiber_codimension": 2,
        "first_chart_primary_decomposition": "<f0,H>=<f0,f1> intersect <x,y>",
        "second_chart_primary_decomposition": "<f1,H>=<f0,f1> intersect <u,v>",
        "saturations": [
            "<f0,f1>=<f0,H>:y^infinity",
            "<f0,f1>=<f1,H>:v^infinity",
        ],
        "strict_principal_witness": "(x,y,u,v)=(1,0,0,0) has H=0 but f0=2",
        "Groebner_checks": {
            "universal_elimination": True,
            "xy_primary_decomposition": True,
            "uv_primary_decomposition": True,
        },
    }


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        (1, 1, 13, (9, 4, 0), 0),
        (2, 1, 17, (14, 14, 11), 8),
        (8, 2, 47, (30, 41, 0), 0),
        (4, 4, 43, (25, 27, 34), 2),
        (2, 6, 47, (17, 23, 42), 36),
    ]
    output = []
    for h, s, prime, expected_coordinates, expected_hasse in declared:
        factorial_table, inverse_factorial, inverse = ITEM218.factorial_tables(prime)
        q0, q1, eliminant, data = ITEM218.divided_conditions_mod(
            prime,
            h,
            s,
            factorial_table,
            inverse_factorial,
            inverse,
        )
        if (q0, q1, eliminant) != expected_coordinates:
            raise AssertionError("declared Item218 coordinates")
        x, y, u, v, a_base, b_base, c_base, d_base = data
        lam = b_base * pow(a_base, -1, prime) % prime
        alpha = c_base * pow(a_base, -1, prime) % prime
        beta = d_base * pow(b_base, -1, prime) % prime
        alpha_formula = -3 * (3 * s + 1) * pow(2 * s, -1, prime) % prime
        beta_formula = (2 * s + h + 1) * pow(2 * s, -1, prime) % prime
        lambda_formula = (
            (-1 if (h - s) % 2 else 1)
            * factorial(h)
            * comb(3 * s + 1, s)
            * pow(rising(2 * s + 2, h), -1, prime)
        ) % prime
        if (alpha, beta, lam) != (alpha_formula, beta_formula, lambda_formula):
            raise AssertionError("actual scalar ratios")

        f0 = (2 * x - lam * y) % prime
        f1 = (2 * alpha * u - beta * lam * v) % prime
        hasse = (beta * x * v - alpha * u * y) % prime
        if f0 != q0 * pow(a_base, -1, prime) % prime:
            raise AssertionError("Q0 normalization")
        if f1 != q1 * pow(a_base, -1, prime) % prime:
            raise AssertionError("Q1 normalization")
        if hasse != eliminant:
            raise AssertionError("Hasse eliminant normalization")
        if (beta * v * f0 - y * f1 - 2 * hasse) % prime:
            raise AssertionError("finite syzygy")

        transverse_rational = transverse_period_rational(h, s)
        transverse_residue = reduce_fraction(transverse_rational, prime)
        if transverse_residue != q0:
            raise AssertionError("parameter-derivative period")

        n = 2 * h
        r = 2 * s + 1
        selected_hasse = positive_prefix(r, n) % prime
        if selected_hasse != expected_hasse:
            raise AssertionError("selected Hasse coefficient")
        if (selected_hasse == 0) != (eliminant == 0):
            raise AssertionError("pinned Hasse/eliminant zero bridge")

        output.append(
            {
                "classification": "PREDECLARED EXACT CONTROL; NOT A PRIME SCAN",
                "M": 3 * h + 4 * s + 2,
                "h": h,
                "s": s,
                "p": prime,
                "n": n,
                "r": r,
                "period_data": {"x": x, "y": y, "u": u, "v": v},
                "scalar_data": {
                    "A": a_base,
                    "B": b_base,
                    "C": c_base,
                    "D": d_base,
                    "lambda": lam,
                    "alpha": alpha,
                    "beta": beta,
                },
                "original_coordinates": {"Q0": q0, "Q1": q1},
                "normalized_coordinates": {"f0": f0, "f1": f1},
                "eliminated_Hasse_period": eliminant,
                "selected_Hasse_coefficient": selected_hasse,
                "transverse_parameter_derivative_period": {
                    "numerator": transverse_rational.numerator,
                    "denominator": transverse_rational.denominator,
                    "residue": transverse_residue,
                },
                "selected_Hasse_zero_but_transverse_nonzero":
                    selected_hasse == 0 and q0 != 0,
                "full_original_collision": q0 == 0 and q1 == 0,
                "full_collision_claimed_from_selected_zero": False,
            }
        )
    return output


def capacity_and_scope() -> dict[str, Any]:
    return {
        "admission": {
            "actual_family": "p=4h+6s+3, M=3h+4s+2",
            "raw_support": "all actual fixed-j1 rows",
            "raw_prime_mass": "M/6+o(M)",
            "maximum_possible_saving_per_6M": "1/36",
            "new_algebraic_codimension": 1,
            "meaning": "restoring the fixed factorial ratio changes the forgotten-ratio principal Hasse ideal into the actual prime codimension-two gate ideal",
        },
        "transverse_period": {
            "exact": "Q0=2H0(2h+6s+2)-H0(4h+4s+2)",
            "parameter_derivative":
                "H0(N)=d/dtau [z^N](1-z)^(2h)(1+z)(1+z^2)^(2s+tau) at tau=0",
            "normalization": "f0=Q0/A, with A a p-unit on every actual row",
            "forced_by_full_collision": True,
            "forced_by_selected_Hasse_zero": False,
        },
        "scope": {
            "proved": [
                "exact full-gate reconstruction and ideal",
                "principal elimination after forgetting lambda",
                "actual codimension-two fiber and transverse period",
                "two chart decompositions and boundary components",
            ],
            "not_proved": [
                "weighted nonconcentration for the joint Hasse/transverse zero set",
                "zero-rate mass for either boundary component",
                "a fixed-M sublinear-height common target",
                "any full collision in the declared controls",
            ],
        },
        "ledger": {
            "new_forced_independent_algebraic_condition": 1,
            "new_proved_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
            "retained_ceiling_per_6M": "1/36",
            "route_1_status": "ACTIVE",
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item360-j1-full-gate-transverse-period-certificate-v1",
        "item": 360,
        "date": "2026-09-01",
        "status": "PROVED_ACTUAL_CODIMENSION_TWO_FULL_GATE_AND_TRANSVERSE_PERIOD",
        "dependencies": DEPENDENCIES,
        "symbolic_elimination": symbolic_elimination(),
        "capacity_and_scope": capacity_and_scope(),
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "exact reconstruction of the full two-coordinate Item218 gate",
                "principal Hasse elimination ideal when the factorial ratio is forgotten",
                "prime codimension-two ideal on the actual tied factorial-ratio fiber",
                "the original Q0 coordinate as an exact transverse parameter-derivative period",
                "two primary chart decompositions and saturation formulas",
                "one new collision-forced algebraic codimension but zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "five predeclared rows, including two selected-Hasse zeros with nonzero transverse period; no prime scan"
            ],
            "OPEN": [
                "weighted zero density for the joint Hasse/transverse gate",
                "weighted control of the two boundary components",
                "a global arithmetic transform or fixed-M common target for Q0",
                "any strict fixed-j1 ceiling reduction, Route 1, and every conclusion about e+pi",
            ],
        },
        "canonical_files_modified": False,
        "prime_scans": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "item": 360,
                "forgotten_ratio_codimension": 1,
                "actual_full_gate_codimension": 2,
                "independent_transverse_period": True,
                "booking": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
