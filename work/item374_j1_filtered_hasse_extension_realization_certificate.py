#!/usr/bin/env python3
"""Deterministic exact replay for Item 374.

The checker constructs a rank-two Fontaine--Laffaille-type filtered
Frobenius module whose graded Hasse coordinate is the actual transverse
Q0 while full Frobenius remains an isogeny.  It verifies the unipotent
local-product law, fixed Hodge data, characteristic-polynomial blindness,
and the first Witt/Teichmueller lift carry on predeclared actual rows.
No collision scan or horizontal density inference is performed.
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
DEFAULT_OUTPUT = HERE / "item374_j1_filtered_hasse_extension_realization_certificate.json"

DEPENDENCIES = {
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
    "sources/item371_j1_determinant_horizontal_compatibility_no_go_report.md":
        "9d4ece939ce2d644058f9d8da27f2c2d9697e6674d3c2bb8543d42f87a1713d9",
    "scripts/item371_j1_determinant_horizontal_compatibility_no_go_certificate.py":
        "2105cf70cd15b3f272f99e76605aa4fec661037e839172c93b6faeb755bcd83f",
    "results/item371_j1_determinant_horizontal_compatibility_no_go_certificate.json":
        "e0eb9298d30cd3938d3be409d90444700c4f03b312269100d756ac62d9e0b8fb",
    "results/item371_j1_determinant_horizontal_compatibility_no_go_certificate_replay.json":
        "e0eb9298d30cd3938d3be409d90444700c4f03b312269100d756ac62d9e0b8fb",
    "results/item371_j1_determinant_horizontal_compatibility_no_go_root_replay.json":
        "e0eb9298d30cd3938d3be409d90444700c4f03b312269100d756ac62d9e0b8fb",
    "results/item371_j1_determinant_horizontal_compatibility_no_go_ledger_delta.json":
        "1892db2b67ab145ca24eadde59af314267a4afd78e22047df271c73a4ee12309",
    "results/item371_j1_determinant_horizontal_compatibility_no_go_root_audit.json":
        "7aa4a6f8199c6046ac50616de523fb50b68d8c2837522ba557522072e66df13f",
    "manifests/item371_j1_determinant_horizontal_compatibility_no_go_manifest.json":
        "c55bd136dac9c8bc8be84d8f1bd0049256880814c1297f257918c3612c741af8",
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
        expected = ((-1) ** (k - 1) * pow(k, -1, prime)) % prime
        if coefficient != expected:
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


def unipotent(value) -> S.Matrix:
    return S.Matrix([[1, 0], [value, 1]])


def symbolic_filtered_module() -> dict[str, Any]:
    q, x, y, P, X = S.symbols("q x y P X")
    Uq = unipotent(q)
    if Uq.det() != 1:
        raise AssertionError("unipotent determinant")
    if unipotent(x) * unipotent(y) != unipotent(x + y):
        raise AssertionError("unipotent product")

    diagonal_hodge = S.diag(P, 1)
    phi0 = Uq * diagonal_hodge
    if phi0 != S.Matrix([[P, 0], [P * q, 1]]):
        raise AssertionError("full Frobenius")
    if S.expand(phi0.det() - P) != 0:
        raise AssertionError("full Frobenius determinant")
    characteristic = S.factor(phi0.charpoly(X).as_expr())
    if S.expand(characteristic - (X - P) * (X - 1)) != 0:
        raise AssertionError("full characteristic")

    e1 = S.Matrix([1, 0])
    e2 = S.Matrix([0, 1])
    phi1_e1 = S.simplify(phi0 * e1 / P)
    phi0_e2 = phi0 * e2
    generation = S.Matrix.hstack(phi1_e1, phi0_e2)
    if phi1_e1 != S.Matrix([1, q]):
        raise AssertionError("divided Frobenius")
    if generation.det() != 1:
        raise AssertionError("strong generation")
    hasse_coordinate = phi1_e1[1]
    if hasse_coordinate != q:
        raise AssertionError("graded Hasse coordinate")

    principal = S.Matrix([[q, -1], [1, 0]])
    if principal.det() != 1 or principal[0, 0] != q:
        raise AssertionError("principal-minor packaging")

    diagonalizing_parameter = S.simplify(P * q / (P - 1))
    basis = unipotent(diagonalizing_parameter)
    diagonalized = S.simplify(basis.inv() * phi0 * basis)
    if diagonalized != diagonal_hodge:
        raise AssertionError("unfiltered diagonalization")

    return {
        "base": "W(F_p)=Z_p; Witt Frobenius is the identity",
        "residue_unipotent": "U(q)=[[1,0],[q,1]]",
        "local_product_law": "U(x)U(y)=U(x+y)",
        "residue_full_determinant": 1,
        "filtration": "Fil^0=M, Fil^1=W*e1, Fil^2=0",
        "Hodge_weights": [0, 1],
        "phi0": "[[p,0],[p*q_tilde,1]]",
        "phi1_e1": "e1+q_tilde*e2",
        "Fontaine_Laffaille_relation": "phi0|Fil^1=p*phi1",
        "strong_generation_determinant": 1,
        "full_Frobenius_determinant": "p",
        "full_Frobenius_characteristic_polynomial": "(X-p)(X-1)",
        "graded_Hasse_coordinate": "q mod p",
        "principal_minor_alternative": "[[q,-1],[1,0]] has determinant one and principal 1x1 minor q",
        "unfiltered_diagonalization": "U(p*q/(p-1))^(-1)*phi0*U(p*q/(p-1))=diag(p,1)",
        "conclusion": "q lives in filtered/divided-Frobenius extension data and is invisible to the full isocrystal characteristic polynomial",
        "rank_minimality": "rank one cannot have both nonzero Fil^1 and nonzero M/Fil^1, so rank two is minimal for this graded Hasse map",
    }


def teichmueller_lift(residue: int, prime: int) -> int:
    if residue % prime == 0:
        return 0
    return pow(residue % prime, prime, prime * prime)


def pointwise_support_bound(h: int, s: int, prime: int) -> dict[str, int]:
    exponent_difference = 2 * abs(h - s)
    zero_upper_bound = 4 + 2 * (prime - 1) + exponent_difference
    nonidentity_lower_bound = prime * prime - 1 - zero_upper_bound
    if exponent_difference >= prime:
        raise AssertionError("frequency zero bound")
    if nonidentity_lower_bound <= 0:
        raise AssertionError("pointwise support lower bound")
    return {
        "P0_distinct_zero_upper_bound": 4,
        "finite_log_z2_zero_upper_bound": 2 * (prime - 1),
        "frequency_factor_zero_upper_bound": exponent_difference,
        "total_zero_upper_bound": zero_upper_bound,
        "nonidentity_factor_lower_bound_over_Fp2": nonidentity_lower_bound,
    }


# Predeclared before Item 374; no search is performed.
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

        tT = (2 * data["c_T"]) % prime
        tL = (-data["c_L"]) % prime
        if (tT + tL) % prime != q0:
            raise AssertionError("grouped transverse sum")
        grouped_product = unipotent(tT) * unipotent(tL)
        expected_product = unipotent(q0)
        grouped_product = grouped_product.applyfunc(lambda value: int(value) % prime)
        expected_product = expected_product.applyfunc(lambda value: int(value) % prime)
        if grouped_product != expected_product:
            raise AssertionError("grouped unipotent product")

        modulus = prime * prime
        lifted_sum = (
            teichmueller_lift(tT, prime)
            + teichmueller_lift(tL, prime)
        ) % modulus
        lifted_target = teichmueller_lift(q0, prime)
        lift_difference = (lifted_sum - lifted_target) % modulus
        if lift_difference % prime != 0:
            raise AssertionError("Witt carry divisibility")
        carry_digit = (lift_difference // prime) % prime

        phi0 = [[prime, 0], [prime * q0, 1]]
        phi1_e1 = [1, q0]
        if phi0[0][0] * phi0[1][1] - phi0[0][1] * phi0[1][0] != prime:
            raise AssertionError("control full determinant")
        if S.Matrix.hstack(S.Matrix(phi1_e1), S.Matrix([0, 1])).det() != 1:
            raise AssertionError("control strong generation")

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
            "grouped_extension_entries": {"2c_T": tT, "-c_L": tL},
            "unipotent_product_mod_p": [[int(value) for value in row] for row in grouped_product.tolist()],
            "pointwise_support_bound": pointwise_support_bound(h, s, prime),
            "filtered_module": {
                "phi0_integer_lift": phi0,
                "phi1_e1_residue": phi1_e1,
                "full_determinant": prime,
                "graded_Hasse": q0,
            },
            "naive_Teichmueller_lift": {
                "lift_2c_T_mod_p2": teichmueller_lift(tT, prime),
                "lift_minus_c_L_mod_p2": teichmueller_lift(tL, prime),
                "lift_Q0_mod_p2": lifted_target,
                "sum_minus_target_mod_p2": lift_difference,
                "carry_digit_mod_p": carry_digit,
                "additive_without_carry": lift_difference == 0,
            },
        })
    if not any(
        row["naive_Teichmueller_lift"]["carry_digit_mod_p"] != 0
        for row in output
    ):
        raise AssertionError("nontrivial actual Witt carry control")
    return output


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item374-j1-filtered-hasse-extension-realization-certificate-v1",
        "item": 374,
        "date": "2026-09-01",
        "status": "PROVED_EXACT_RANK_TWO_FILTERED_HASSE_REALIZATION_AND_HORIZONTAL_INFORMATION_NEUTRALITY",
        "dependencies": DEPENDENCIES,
        "actual_family": "p=4h+6s+3, M=3h+4s+2, n=2h, r=2s+1",
        "filtered_module_theorem": symbolic_filtered_module(),
        "actual_target_bridge": {
            "choice": "q=Q0=2c_T-c_L in F_p",
            "full_collision_implication": "full ordinary collision implies selected Hasse a=0 and graded Hasse q=0",
            "joint_converse_to_full_collision_claimed": False,
            "new_independent_condition": 0,
        },
        "local_extension_product": {
            "Item369_local_entry": "R(x)=2x^(-T)F_Q(x)-x^(-L)F_Q(x), with sum_x R(x)=-Q0",
            "factor": "U(-R(x))",
            "product": "product_x U(-R(x))=U(Q0)",
            "full_determinant": 1,
            "order_independent": True,
            "support_theorem": "R(x)=x^(-L)P0(x)L_p(x^2)(2x^(L-T)-1), so at most 4+2(p-1)+2|h-s| points vanish and at least p^2-1-[that] factors are nonidentity",
            "classification": "exact residue-field unipotent extension product, not a characteristic-zero compatible lift",
        },
        "compatibility_barrier": {
            "full_characteristic_polynomial": "(X-p)(X-1), independent of Q0",
            "semisimplification": "the same split slopes 1 and p for every Q0",
            "standard_compatible_data": "trace and determinant do not see the filtered extension coordinate",
            "moduli_flexibility": "the fixed rank-two Hodge type admits every residue q, so rank and Hodge polygon alone impose no horizontal zero restriction",
            "selector_map": "the tied row is sent to the affine Hasse coordinate q=Q0; bounding the pullback of q=0 is exactly the original open problem",
            "compatible_extension_target": "a bounded-conductor nonsemisimple extension of the Tate-type graded factors with local Fontaine--Laffaille class Q0",
            "density_translation": "Q0=0 is local splitting of that extension; semisimple Chebotarev data are constant and cannot count the splitting primes",
            "naive_local_lift": "Teichmueller representatives are not additive; actual controls exhibit a nonzero first Witt carry",
            "not_proved": "one prime-independent geometric filtered F-crystal, connection, compatible lattice, or horizontal monodromy law",
        },
        "literal_cases": {
            "classification": "SEPARATE INHERITED CLOSURES; NOT REPROVED HERE",
            "Kummer": "literal full-order Kummer support grows at least p-2",
            "Artin_Schreier": "literal polynomial pullback has Swan conductor 2(p-1)",
            "live_nonliteral_route": "a different bounded-conductor unipotent/cohomological extension with an exact selector bridge",
        },
        "capacity": {
            "actual_support": "all fixed-j1 selector rows",
            "raw_log_mass": "M/6+o(M)",
            "raw_ceiling_per_6M": "1/36",
            "desired_theorem": "weighted joint vanishing of selected Hasse a and graded Hasse Q0 is o(M)",
            "desired_theorem_proved": False,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
            "route_1_status": "ACTIVE",
        },
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "exact rank-two strongly generated filtered Frobenius module with graded Hasse Q0",
                "full Frobenius isogeny determinant p and fixed Hodge weights 0,1",
                "exact residue-level unipotent local-product realization of the additive transverse coordinate",
                "quadratic lower bound for the number of nonidentity pointwise unipotent factors",
                "full characteristic-polynomial and semisimplification blindness to Q0",
                "fixed-rank/fixed-Hodge information-neutrality",
                "nontrivial naive Teichmueller lift carry on declared actual controls",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "four predeclared filtered-module and Witt-carry controls; no prime scan",
            ],
            "OPEN": [
                "a prime-independent geometric filtered/crystalline compatible extension realizing Q0",
                "a nonliteral bounded-conductor unipotent or cohomological compression",
                "horizontal distribution of the filtered extension/Hasse coordinate",
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
        "item": 374,
        "filtered_rank": 2,
        "fixed_Hodge_weights": [0, 1],
        "graded_Hasse_equals_Q0": True,
        "horizontal_theorem": False,
        "booking": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
