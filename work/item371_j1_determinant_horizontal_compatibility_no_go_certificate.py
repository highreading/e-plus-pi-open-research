#!/usr/bin/env python3
"""Deterministic exact replay for Item 371.

The checker tests whether Item 369's cyclic companion determinant can be
promoted from an additive coefficient moment to a pointwise multiplicative
Frobenius determinant.  It verifies determinant multiplicativity, the
universal additive-versus-separable-product obstruction, the mixed
zero/nonzero determinant controls on the actual selector, and the growing
finite-log Kummer support.  No collision scan or density inference is made.
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
DEFAULT_OUTPUT = HERE / "item371_j1_determinant_horizontal_compatibility_no_go_certificate.json"

DEPENDENCIES = {
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
    "sources/item369_j1_cyclic_companion_compatibility_barrier_report.md":
        "676b7f68b3602c1ebbd743779845fd4fe3f511484a3f2e7033ac5ff27d0544b9",
    "scripts/item369_j1_cyclic_companion_compatibility_barrier_certificate.py":
        "cd9ef9480809552083b667ea7fcc2c4657ffb104f1558a5f0b5920e6bf7171ea",
    "results/item369_j1_cyclic_companion_compatibility_barrier_certificate.json":
        "24ce6c7dae148763699358971170e7cfae6a72a4313b4344c4fb3e4244133d83",
    "results/item369_j1_cyclic_companion_compatibility_barrier_certificate_replay.json":
        "24ce6c7dae148763699358971170e7cfae6a72a4313b4344c4fb3e4244133d83",
    "results/item369_j1_cyclic_companion_compatibility_barrier_root_replay.json":
        "24ce6c7dae148763699358971170e7cfae6a72a4313b4344c4fb3e4244133d83",
    "results/item369_j1_cyclic_companion_compatibility_barrier_ledger_delta.json":
        "87175da5ed0b16419d4d463e02fe96f7b7c3f30c8cf5b876a24b6d8f6702a468",
    "results/item369_j1_cyclic_companion_compatibility_barrier_root_audit.json":
        "a8e84b3ad547c41deb6b4eac2066ae097cef88cf6943ec3aead9da1d3d357b59",
    "manifests/item369_j1_cyclic_companion_compatibility_barrier_manifest.json":
        "dd602f42797fe29bef053373eff93ef7ddd13422bd93ad914a31195be64f9b1d",
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


def finite_log(prime: int) -> list[int]:
    output = [0] * prime
    for k in range(1, prime):
        coefficient = (comb(prime, k) // prime) % prime
        if coefficient != ((-1) ** (k - 1) * pow(k, -1, prime)) % prime:
            raise AssertionError("finite-log quotient")
        output[k] = coefficient
    return output


def p0_polynomial(h: int, s: int, prime: int) -> list[int]:
    return multiply_polynomials(
        multiply_polynomials(
            power_polynomial([1, -1], 2 * h, prime),
            [1, 1],
            prime,
        ),
        power_polynomial([1, 0, 1], 2 * s, prime),
        prime,
    )


def transverse_data(h: int, s: int, prime: int) -> dict[str, int]:
    log_z2 = [0] * (2 * prime - 1)
    for k, coefficient in enumerate(finite_log(prime)):
        log_z2[2 * k] = coefficient
    product = multiply_polynomials(p0_polynomial(h, s, prime), log_z2, prime)
    T = 2 * h + 6 * s + 2
    L = 4 * h + 4 * s + 2
    cT = product[T] % prime
    cL = product[L] % prime
    return {"T": T, "L": L, "c_T": cT, "c_L": cL, "Q0": (2 * cT - cL) % prime}


def selected_hasse(h: int, s: int) -> int:
    n = 2 * h
    r = 2 * s + 1
    return sum(
        comb(r + k - 1, k) * comb(4 * r + n - 1, n - 4 * k)
        for k in range(n // 4 + 1)
    )


def finite_log_roots(prime: int) -> dict[str, int]:
    w = S.symbols("w")
    coefficients = finite_log(prime)
    polynomial = S.Poly(
        sum(value * w**degree for degree, value in enumerate(coefficients)),
        w,
        modulus=prime,
    )
    derivative = polynomial.diff()
    expected = S.Poly(
        sum((-1) ** j * w**j for j in range(prime - 1)),
        w,
        modulus=prime,
    )
    if derivative != expected:
        raise AssertionError("finite-log derivative")
    gcd_degree = S.gcd(polynomial, derivative).degree()
    distinct = polynomial.degree() - gcd_degree
    if distinct < (prime - 1) // 2:
        raise AssertionError("finite-log root bound")
    return {
        "degree": polynomial.degree(),
        "gcd_derivative_degree": gcd_degree,
        "distinct_roots_Lp": distinct,
        "distinct_roots_Lp_z2": 2 * distinct - 1,
        "proved_lower_bound_Lp_z2": prime - 2,
    }


def symbolic_companion_and_product() -> dict[str, Any]:
    a, q0, X = S.symbols("a q0 X")
    companion = S.Matrix([[-a, -q0], [1, 0]])
    if companion.det() != q0:
        raise AssertionError("companion determinant")
    if S.expand(companion.charpoly(X).as_expr()) != X**2 + a * X + q0:
        raise AssertionError("companion characteristic")

    entries = S.symbols("a11 a12 a21 a22 b11 b12 b21 b22")
    A = S.Matrix([[entries[0], entries[1]], [entries[2], entries[3]]])
    B = S.Matrix([[entries[4], entries[5]], [entries[6], entries[7]]])
    multiplicativity = S.expand((A * B).det() - A.det() * B.det())
    if multiplicativity != 0:
        raise AssertionError("determinant multiplicativity")

    x, y = S.symbols("x y")
    additive = x + y
    mixed_obstruction = S.expand(
        additive * S.diff(additive, x, y)
        - S.diff(additive, x) * S.diff(additive, y)
    )
    if mixed_obstruction != -1:
        raise AssertionError("mixed separability obstruction")
    f = S.Function("f")
    g = S.Function("g")
    separable = f(x) * g(y)
    separable_identity = S.simplify(
        separable * S.diff(separable, x, y)
        - S.diff(separable, x) * S.diff(separable, y)
    )
    if separable_identity != 0:
        raise AssertionError("separable product identity")

    return {
        "companion": "[[-a,-Q0],[1,0]]",
        "characteristic_polynomial": "X^2+a*X+Q0",
        "determinant": "Q0",
        "generic_local_matrices": "A and B",
        "determinant_product_identity": "det(A*B)=det(A)*det(B)",
        "additive_selector_model": "x+y",
        "multiplicatively_separable_model": "f(x)*g(y)",
        "mixed_operator": "F*F_xy-F_x*F_y",
        "mixed_operator_on_additive_selector": -1,
        "mixed_operator_on_separable_product": 0,
        "conclusion": "a universal pointwise product of local determinant factors cannot equal the additive transverse selector once two local contributions vary independently",
    }


# Predeclared before Item 371; no search is performed.
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
            raise AssertionError("actual family")
        data = transverse_data(h, s, prime)
        a = selected_hasse(h, s) % prime
        q0 = data["Q0"]
        if (a, q0) != (expected_a, expected_q0):
            raise AssertionError("declared control")
        roots = finite_log_roots(prime)
        companion = S.Matrix([[-a, -q0], [1, 0]])
        if int(companion.det()) % prime != q0:
            raise AssertionError("control determinant")
        output.append({
            "classification": "PREDECLARED EXACT CONTROL; NOT A PRIME SCAN",
            "h": h,
            "s": s,
            "p": prime,
            "M": 3 * h + 4 * s + 2,
            "selected_Hasse": a,
            "transverse_Q0": q0,
            "c_T": data["c_T"],
            "c_L": data["c_L"],
            "companion_mod_p": [[(-a) % prime, (-q0) % prime], [1, 0]],
            "companion_determinant": q0,
            "companion_invertible": q0 != 0,
            "finite_log_roots": roots,
        })
    if not any(row["companion_determinant"] == 0 for row in output):
        raise AssertionError("zero determinant witness")
    if not any(row["companion_determinant"] != 0 for row in output):
        raise AssertionError("nonzero determinant witness")
    return output


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item371-j1-determinant-horizontal-compatibility-no-go-certificate-v1",
        "item": 371,
        "date": "2026-09-01",
        "status": "PROVED_SCOPED_LISSE_CRYSTALLINE_AND_LOCAL_PRODUCT_DETERMINANT_NO_GO",
        "dependencies": DEPENDENCIES,
        "actual_family": "p=4h+6s+3, M=3h+4s+2, n=2h, r=2s+1",
        "symbolic_theorem": symbolic_companion_and_product(),
        "exact_determinant_divisor": {
            "equation": "Q0=2c_T-c_L=0 mod p",
            "classification": "the already forced Item360 transverse divisor, not a new independent Frobenius divisor",
            "full_collision_implication": "full ordinary collision implies trace(C)=det(C)=0",
            "joint_converse_to_full_collision_claimed": False,
        },
        "lisse_obstruction": {
            "statement": "Frobenius on a lisse rank-two mod-p fiber lies in GL_2, so its determinant is nonzero at every unramified point",
            "actual_witness": "(h,s,p)=(10,11,109) has Q0=0, hence the literal companion is singular",
            "conclusion": "the literal companion cannot be Frobenius of a lisse mod-p system on a good locus containing all actual rows",
            "removing_zero_divisor_issue": "deleting Q0=0 from the lisse locus removes exactly the rows whose density must be bounded",
        },
        "crystalline_obstruction": {
            "scope": "integral bounded-conductor rank-two F-crystals with one fixed Tate normalization and unit normalized full determinant on a connected good locus",
            "dichotomy": "after undoing a fixed Tate twist p^w, the full determinant mod p is everywhere a unit when w=0 and identically zero when w>0",
            "control_pattern": "Q0 is nonzero on three declared rows and zero on one declared row",
            "conclusion": "Q0 cannot be the full Frobenius determinant in this fixed-normalization class",
            "not_ruled_out": "Hasse subdeterminants, varying lattices or slopes, singular extensions across Q0=0, and a different target-specific F-crystal",
        },
        "pointwise_product_obstruction": {
            "determinant_law": "det(product_x A_x)=product_x det(A_x)",
            "zero_locus": "a product determinant vanishes through at least one local factor, whereas Q0 is a selected additive cancellation",
            "universal_separability_test": "(x+y)(x+y)_xy-(x+y)_x(x+y)_y=-1, but the same operator is zero on f(x)g(y)",
            "scope": "pointwise local factors whose determinants depend separately on local contributions; target-global factors evade the theorem only by abandoning locality",
        },
        "literal_support_obstruction": {
            "finite_log": "L_p(z^2) has at least p-2 distinct roots",
            "ramification": "multiplicities one or two are nonzero modulo p-1 and p^2-1 for p>=13",
            "Kummer_conclusion": "literal full-order Kummer realization has linearly growing conductor support",
            "Artin_Schreier_degree": "deg L_p(z^2)=2(p-1), which is not divisible by p",
            "Artin_Schreier_conclusion": "the literal reduced polynomial pullback has Swan conductor 2(p-1) at infinity",
            "not_ruled_out": "a different unipotent, Artin-Schreier-Witt, or cohomological compression with proved bounded conductor",
        },
        "capacity": {
            "actual_support": "all fixed-j1 selector rows",
            "raw_log_mass": "M/6+o(M)",
            "raw_ceiling_per_6M": "1/36",
            "desired_theorem": "sum_(prime rows with tr(C)=det(C)=0) log p=o(M)",
            "desired_theorem_proved": False,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
            "route_1_status": "ACTIVE",
        },
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "exact determinant divisor is the existing additive transverse coordinate",
                "lisse mod-p invertibility obstruction for a literal all-row companion realization",
                "fixed-normalization full crystalline determinant dichotomy",
                "universal pointwise local-product separability obstruction",
                "literal finite-log Kummer and Artin-Schreier conductor-growth obstructions",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "four predeclared determinant controls, including both zero and nonzero values; no prime scan",
            ],
            "OPEN": [
                "a Hasse subdeterminant or non-unit varying-slope F-crystal realization",
                "a target-specific nonlocal identity or bounded-conductor compression",
                "horizontal determinant/trace nonconcentration or an average-gcd theorem",
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
        "item": 371,
        "exact_determinant_divisor": "Q0",
        "genuine_all_row_lisse_companion": False,
        "pointwise_product_realization": False,
        "booking": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
