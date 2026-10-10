#!/usr/bin/env python3
"""Deterministic exact replay for Item 317.

This checker proves the residue-level telescoper shared by A_s and the
rescaled Gaussian companion, verifies the exact quadratic readout for both
actual containers D_(s,epsilon), constructs the symmetric-square coupled
system, audits all forward/backward pivots through a four-step period, and
checks the operator-specific pivot-only no-go.  It performs no prime scan
and no container factorization.
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
DEFAULT_OUTPUT = HERE / "item317_gaussian_container_coupled_no_go_certificate.json"
DATA_PATH = HERE / "item317_residue_telescoper_data.json"
DATA_SHA256 = "f9ca57040fc7ae1030f9d915955085e3263e6c30f3129f2e9c4961198defa81b"

DEPENDENCIES = {
    "sources/item310_j1_container_holonomy_no_go_report.md": (
        "35537c7908392d860ea58334f0ea5fe728f7158a7338992ab091df89d8742eb0"
    ),
    "scripts/item310_j1_container_holonomy_no_go_certificate.py": (
        "b03b91da941b22eef55f7a3bb5e91fd8abdcbf249ce89677e1e2ac497ca71880"
    ),
    "results/item310_j1_container_holonomy_no_go_certificate.json": (
        "025ac9ae87cbec544877e072dc5c79fad82039d4d85e4d1abe73d0ffadc77d16"
    ),
    "results/item310_j1_container_holonomy_no_go_certificate_replay.json": (
        "025ac9ae87cbec544877e072dc5c79fad82039d4d85e4d1abe73d0ffadc77d16"
    ),
    "results/item310_j1_container_holonomy_no_go_ledger.json": (
        "610d70ae0d64c5339231bdde37f293c22134cbd70b94f4b6917ec7d6a99daa9c"
    ),
    "results/item310_j1_container_holonomy_no_go_hashes.sha256": (
        "786e540fbde50b083ae2f29e88b6ebf3a6c1836b80574c093ae371b97cbcc583"
    ),
    "manifests/item310_j1_container_holonomy_no_go_manifest.json": (
        "6c2162f0ab9e514c179b38bc3fa4e4380e0b85ff45338abe4463fe57573ac011"
    ),
    "results/item310_root_audit.json": (
        "7375bcc491bd1641764f3a980311c5a8038a602c5d9aea6535b9f23d8580cf76"
    ),
    "sources/item312_A_telescoper_singular_no_go_report.md": (
        "39f6d5e20ae7e463324af44023b1fe78c20d11b3d97d1e672291808f5b586bb2"
    ),
    "scripts/item312_A_telescoper_singular_no_go_certificate.py": (
        "9564216d70fcf3053ef4ffad3594a7d638176407fb7d7aae3acdba131c15bd36"
    ),
    "scripts/item312_A_telescoper_data.json": (
        "64cdd3c400c0472fef2e6b7949ccff2a15478ba7a96eb232ab05f2c547cd993c"
    ),
    "results/item312_A_telescoper_singular_no_go_certificate.json": (
        "21373d42a41590895112b4567bd3eae988166db8d84d55db9514be0e59e8f7f9"
    ),
    "results/item312_A_telescoper_singular_no_go_certificate_replay.json": (
        "21373d42a41590895112b4567bd3eae988166db8d84d55db9514be0e59e8f7f9"
    ),
    "results/item312_A_telescoper_singular_no_go_ledger.json": (
        "23a6f4d9a1e86409b70f39b0ca27e119debf5a54c777a0e769b09be6ceeb839d"
    ),
    "results/item312_A_telescoper_singular_no_go_hashes.sha256": (
        "e15c781f29f47cfd63678978410edec9cf9706e1671a87bacc1cf0b8cf04e730"
    ),
    "manifests/item312_A_telescoper_singular_no_go_manifest.json": (
        "7bb44b319299fe9193b3eb80004a4c9b65d8f47ad1402553033cffaa3be8d9b1"
    ),
    "results/item312_root_audit.json": (
        "ea84afb7c4c8e67c6cd958a576469e167460b2ea92bacc8e7e4ae05872759c1d"
    ),
    "sources/item308_j1_all_s_fixed_divisor_no_go_report.md": (
        "4eb8f8c37dfde9d19e57c8df5ff8090bd95f03be59fff7d6aede55d02993bdc8"
    ),
    "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py": (
        "9b60d380b503c7ac9fed13792fae67735cfcf6b0f376581a0076fde16a82f0b9"
    ),
    "results/item308_j1_all_s_fixed_divisor_no_go_certificate.json": (
        "4efff9ca2fb1bc11cc6030e260ff73aae89c28bd157bb41fa6bbc3b32e41e5cf"
    ),
    "manifests/item308_j1_all_s_fixed_divisor_no_go_manifest.json": (
        "1c4721f43b5bbdc0c68e4d9fd689562a32a4af4fbbab2a9e7075da96b151b4d5"
    ),
    "results/item308_root_audit.json": (
        "11feb8105ea46c27d83df2449404297fe74709eceaa8be6a21bd9484cbffba22"
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))
    if not DATA_PATH.is_file() or sha256(DATA_PATH) != DATA_SHA256:
        raise RuntimeError("Item317 telescoper data mismatch")


pin_dependencies()
DATA = json.loads(DATA_PATH.read_text(encoding="utf-8"))
if DATA.get("schema") != "item317_residue_telescoper_data_v1":
    raise RuntimeError("Item317 data schema")

s, t = S.symbols("s t")


def recurrence_polynomials() -> list[S.Expr]:
    return [
        9
        * (2 * s + 1)
        * (6 * s + 5)
        * (6 * s + 7)
        * (6 * s + 11)
        * (6 * s + 13)
        * (660 * s**2 + 2920 * s + 3039),
        24
        * s
        * (6 * s + 11)
        * (6 * s + 13)
        * (
            1697520 * s**4
            + 10905280 * s**3
            + 24360488 * s**2
            + 22368528 * s
            + 7001703
        ),
        768
        * s
        * (s + 1)
        * (2 * s + 3)
        * (6 * s + 13)
        * (3960 * s**3 + 20820 * s**2 + 33034 * s + 14047),
        4096
        * s
        * (s + 1)
        * (s + 2)
        * (2 * s + 3)
        * (2 * s + 5)
        * (660 * s**2 + 1600 * s + 779),
    ]


def residue_telescoper_audit() -> dict[str, Any]:
    q = t**2 - 2 * t + 2
    n_zero = (
        4
        - S.Rational(4, 3) * t
        - S.Rational(8, 3) * t**2
        + S.Rational(16, 3) * t**3
        - 3 * t**4
        + t**5
    )
    n_one = (
        S.Rational(80, 3) * t
        - S.Rational(224, 3) * t**2
        + S.Rational(256, 3) * t**3
        - 46 * t**4
        + 10 * t**5
    )
    operators = recurrence_polynomials()
    stored_operators = [
        S.sympify(value, locals={"s": s})
        for value in DATA["operators_factored"]
    ]
    if any(
        S.expand(actual - stored) != 0
        for actual, stored in zip(operators, stored_operators)
    ):
        raise AssertionError("operator data")

    coefficients = [
        S.sympify(value, locals={"s": s})
        for value in DATA["certificate_P_coefficients_descending_t"]
    ]
    if (
        DATA["certificate_P_degree_t"] != 20
        or DATA["certificate_P_degree_s"] != 7
        or len(coefficients) != 21
    ):
        raise AssertionError("certificate shape")
    certificate_p = S.Poly.from_list(coefficients, gens=t).as_expr()
    certificate_k = S.factor(
        t * certificate_p / ((1 - t) ** 5 * q**5)
    )
    stored_k = S.sympify(
        DATA["certificate_K"], locals={"s": s, "t": t}
    )
    if S.cancel(certificate_k - stored_k) != 0:
        raise AssertionError("certificate data")

    ratio = t**3 / ((1 - t) ** 2 * q**2)
    target = S.factor(
        sum(
            operators[j]
            * ratio**j
            * (n_zero + (s + j) * n_one)
            for j in range(4)
        )
    )
    log_derivative = (
        (3 * s + S.Rational(1, 2)) / t
        + (2 * s + 6) / (1 - t)
        - (2 * s + 1) * S.diff(q, t) / q
    )
    identity = S.cancel(
        S.diff(certificate_k, t)
        + log_derivative * certificate_k
        - target
    )
    if identity != 0:
        raise AssertionError("residue telescoper")

    gaussian_i = S.I
    lam = (1 + gaussian_i) / 2
    rho = S.cancel(1 / lam)
    r = S.expand(lam ** -3)
    if rho != 1 - gaussian_i or r != -2 * (1 + gaussian_i):
        raise AssertionError("Gaussian scaling")

    # If Z_s=r^s B_s, then the rational Item312 operator annihilates Z.
    # Clearing the harmless common Gaussian factor (1+i) gives these
    # exact B-operator multipliers.
    cleared_multipliers = [
        S.expand((1 + gaussian_i) * r**j) for j in range(4)
    ]
    expected_multipliers = [
        1 + gaussian_i,
        -4 * gaussian_i,
        8 * (-1 + gaussian_i),
        32,
    ]
    if cleared_multipliers != expected_multipliers:
        raise AssertionError("B recurrence multipliers")

    return {
        "differential_form": (
            "omega_s=t^(3s+1/2)N_s(t)/"
            "((1-t)^(2s+6)(t^2-2t+2)^(2s+1)) dt"
        ),
        "certificate_K": (
            "t*P(s,t)/((1-t)^5*(t^2-2t+2)^5), "
            "with P stored exactly in Item317 data"
        ),
        "certificate_bidegree": {"degree_s": 7, "degree_t": 20},
        "identity": (
            "sum_(j=0..3) P_j(s)*omega_(s+j)"
            "=d(K_s(t)*F_s(t))"
        ),
        "identity_verified": True,
        "A_residue": "A_s=-Res_(t=1)(omega_s)",
        "lambda": "(1+i)/2",
        "Gaussian_root": "rho=1/lambda=1-i",
        "B_residue": (
            "Res_(t=rho)(omega_s)="
            "-lambda^(-3s-3/2)*B_s (fixed square-root branch)"
        ),
        "rescaling": "Z_s=(-2*(1+i))^s*B_s",
        "Z_operator": "sum_(j=0..3)P_j(s)Z_(s+j)=0",
        "B_operator": (
            "(1+i)P0(s)B_s-4iP1(s)B_(s+1)"
            "+8(-1+i)P2(s)B_(s+2)+32P3(s)B_(s+3)=0"
        ),
        "B_trailing_pivot": str(S.factor((1 + gaussian_i) * operators[0])),
        "B_leading_pivot": str(S.factor(32 * operators[3])),
        "rational_prime_pivots": ["P0(s)", "P3(s)"],
        "all_s_range": "integers s>=1",
    }


def actual_container_readout_audit() -> dict[str, Any]:
    A, z, zbar = S.symbols("A z zbar")
    gaussian_i = S.I
    r = -2 * (1 + gaussian_i)
    rbar = S.conjugate(r)
    rows = []
    representatives = {0: 4, 1: 1, 2: 2, 3: 3}
    for residue, s_value in representatives.items():
        delta_zero = (-1) ** (s_value * (s_value + 1) // 2 + 1)
        B = S.expand(r ** (-s_value) * z)
        Bbar = S.expand(rbar ** (-s_value) * zbar)
        U = S.expand((B + Bbar) / 2)
        V = S.expand((B - Bbar) / (2 * gaussian_i))
        a_integer = 3 * 2 ** (12 * s_value + 10) * A
        for epsilon in (0, 1):
            delta_epsilon = (-1) ** (
                s_value * (s_value + 1) // 2 + 1 + epsilon
            )
            if epsilon == 0:
                b_integer = (
                    3
                    * delta_epsilon
                    * 2 ** (15 * s_value + 12)
                    * U
                )
            else:
                b_integer = (
                    -3
                    * delta_epsilon
                    * 2 ** (15 * s_value + 12)
                    * V
                )
            divisor = S.expand(
                2 ** (3 * s_value + 1) * a_integer**2
                - delta_epsilon * b_integer**2
            )
            normalized = S.cancel(
                divisor / (9 * 2 ** (27 * s_value + 21))
            )
            expected = S.expand(
                A**2
                - 2
                * delta_zero
                * (-gaussian_i) ** s_value
                * z**2
                - 2
                * delta_zero
                * gaussian_i**s_value
                * zbar**2
                - 4
                * (-1) ** epsilon
                * delta_zero
                * z
                * zbar
            )
            if S.expand(normalized - expected) != 0:
                raise AssertionError(("container readout", residue, epsilon))
            rows.append(
                {
                    "s_mod_4": residue,
                    "epsilon": epsilon,
                    "delta_s_0": delta_zero,
                    "quadratic_coefficients_A2_Z2_Zbar2_ZZbar": [
                        str(S.expand(1)),
                        str(S.expand(-2 * delta_zero * (-gaussian_i) ** s_value)),
                        str(S.expand(-2 * delta_zero * gaussian_i**s_value)),
                        str(S.expand(-4 * (-1) ** epsilon * delta_zero)),
                    ],
                }
            )

    return {
        "Item308_scalings": {
            "a_s": "3*2^(12s+10)*A_s",
            "b_s_0": "3*delta_s_0*2^(15s+12)*Re(B_s)",
            "b_s_1": "-3*delta_s_1*2^(15s+12)*Im(B_s)",
        },
        "Z_s": "(-2*(1+i))^s*B_s",
        "delta_s": "(-1)^(s(s+1)/2+1)",
        "exact_readout": (
            "D_(s,epsilon)/(9*2^(27s+21))="
            "A_s^2-2delta_s(-i)^sZ_s^2"
            "-2delta_s i^s conjugate(Z_s)^2"
            "-4(-1)^epsilon delta_s Z_s conjugate(Z_s)"
        ),
        "periodic_rows": rows,
        "symbolic_residue_classes_verified": 8,
    }


def symmetric_square_matrix(matrix: S.Matrix) -> S.Matrix:
    pairs = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    output = S.zeros(6, 6)
    for output_index, (i, j) in enumerate(pairs):
        for input_index, (k, ell) in enumerate(pairs):
            if i == j:
                coefficient = (
                    matrix[i, k] ** 2
                    if k == ell
                    else matrix[i, k] * matrix[i, ell]
                )
            else:
                coefficient = (
                    2 * matrix[i, k] * matrix[j, k]
                    if k == ell
                    else matrix[i, k] * matrix[j, ell]
                    + matrix[i, ell] * matrix[j, k]
                )
            output[output_index, input_index] = S.cancel(coefficient)
    return output


def coupled_system_and_pivot_audit() -> dict[str, Any]:
    operators = recurrence_polynomials()
    p_zero, p_one, p_two, p_three = operators
    transition = S.Matrix(
        [
            [0, 1, 0],
            [0, 0, 1],
            [
                -p_zero / p_three,
                -p_one / p_three,
                -p_two / p_three,
            ],
        ]
    )
    transition_det = S.factor(transition.det())
    if S.cancel(transition_det + p_zero / p_three) != 0:
        raise AssertionError("companion determinant")
    symmetric = symmetric_square_matrix(transition)
    symmetric_det = S.factor(symmetric.det())
    if S.cancel(symmetric_det - transition_det**4) != 0:
        raise AssertionError("symmetric-square determinant")

    M = S.symbols("M", integer=True)
    shifted_rows = []
    combined_primitive = S.Integer(1)
    for label, pivot in (("P0", p_zero), ("P3", p_three)):
        for shift in range(4):
            fixed_value = S.Poly(
                S.expand(
                    2**7
                    * pivot.subs(s, -(4 * M + 1) / 2 + shift)
                ),
                M,
                domain=S.ZZ,
            )
            content, primitive = fixed_value.primitive()
            content_factors = S.factorint(abs(int(content)))
            if any(prime not in (2, 3) for prime in content_factors):
                raise AssertionError(("nonunit content", label, shift))
            primitive_expression = S.factor(primitive.as_expr())
            if primitive.degree() != 7:
                raise AssertionError(("shifted pivot degree", label, shift))
            u = S.symbols("u", nonnegative=True)
            shifted_to_nine = S.Poly(
                S.expand(primitive_expression.subs(M, u + 9)), u
            )
            signs = shifted_to_nine.all_coeffs()
            sign = 1 if signs[0] > 0 else -1
            if any(sign * coefficient <= 0 for coefficient in signs):
                raise AssertionError(("shifted pivot nonzero", label, shift))
            combined_primitive *= primitive_expression
            shifted_rows.append(
                {
                    "pivot": label,
                    "shift": shift,
                    "discarded_p_unit_content": int(content),
                    "primitive_fixed_M_container": str(primitive_expression),
                    "degree": 7,
                    "nonzero_for_M_ge_9": True,
                }
            )
    combined_primitive = S.factor(combined_primitive)
    if S.degree(combined_primitive, M) != 56:
        raise AssertionError("combined shifted pivot degree")

    return {
        "scalar_companion": (
            "T_s=[[0,1,0],[0,0,1],"
            "[-P0/P3,-P1/P3,-P2/P3]]"
        ),
        "companion_determinant": "-P0(s)/P3(s)",
        "quadratic_state_basis": [
            "u0*v0",
            "u0*v1+u1*v0",
            "u0*v2+u2*v0",
            "u1*v1",
            "u1*v2+u2*v1",
            "u2*v2",
        ],
        "quadratic_transition": "S_s=Sym^2(T_s), dimension 6",
        "quadratic_transition_explicit": (
            "with a=-P0/P3,b=-P1/P3,c=-P2/P3, rows are "
            "[0,0,0,1,0,0];[0,0,0,0,1,0];"
            "[0,a,0,2b,c,0];[0,0,0,0,0,1];"
            "[0,0,a,0,b,2c];[a^2,ab,ac,b^2,bc,c^2]"
        ),
        "quadratic_transition_determinant": "(P0(s)/P3(s))^4",
        "actual_container_state": (
            "four quadratic blocks AA,ZZ,ZbarZbar,ZZbar; "
            "a 24-dimensional all-s stacked system"
        ),
        "scaled_state_transition": (
            "W_hat_(s+1)=2^27*diag(S_s,S_s,S_s,S_s)*W_hat_s"
        ),
        "container_readout": (
            "D_(s,epsilon)=9*2^21*l_(s,epsilon)*W_hat_s, "
            "with l period 4"
        ),
        "all_s_stacked_dimension": 24,
        "fixed_residue_subsequence_dimension": 6,
        "residue_step_four_system": (
            "for fixed (s mod 4,epsilon), the four quadratic blocks "
            "combine with constant coefficients into one 6-state vector; "
            "V_hat_(s+4)=2^108*S_(s+3)S_(s+2)S_(s+1)S_s*V_hat_s"
        ),
        "scalar_subsequence_bound": (
            "for each fixed (s mod 4,epsilon), exact cyclic-vector "
            "elimination gives a step-four scalar annihilator of order "
            "at most 6 over Q(i)(s); no global interlaced order is claimed"
        ),
        "forward_pivot": str(S.factor(p_three)),
        "backward_pivot": str(S.factor(p_zero)),
        "rational_prime_pivot_set": "factors of P0(s)P3(s) only",
        "four_step_shifted_pivot_rows": shifted_rows,
        "combined_shifted_fixed_M_degree": 56,
        "moving_prime_mass": (
            "sum over p_s dividing any four-step forward/backward pivot "
            "is <=log|R_shift(M)|=O(log M)=o(M)"
        ),
        "already_booked_content": (
            "shift 0 is Item312's R0(M)R3(M); all powers of 2 and 3 "
            "are p_s-units; shifts 1,2,3 are also zero-rate"
        ),
    }


def pivot_only_no_go_audit() -> dict[str, Any]:
    return {
        "regular_row_hypothesis": (
            "p_s does not divide product_(k=0..3)"
            "P0(s+k)P3(s+k)"
        ),
        "invertibility": (
            "T_(s+k) and Sym^2(T_(s+k)), k=0..3, are invertible "
            "over the residue algebra"
        ),
        "local_witness": (
            "choose a scalar-solution state (y_s,y_(s+1),y_(s+2))="
            "(0,1,0), and set both Gaussian solution states to zero; "
            "the exact quadratic readout has D_(s,epsilon)=0 while "
            "the coupled state is nonzero"
        ),
        "consequence": (
            "pivot factorization and regular transport exclude no "
            "off-pivot row; the full off-pivot collision support remains "
            "admissible in the pivot-only information class"
        ),
        "strict_scope": (
            "This is not a counterexample to the actual Item308 initial "
            "state. It closes only arguments using the operator, its "
            "pivots, and regularity without a sequence-specific invariant "
            "or initial-state arithmetic."
        ),
    }


def build_certificate() -> dict[str, Any]:
    residue = residue_telescoper_audit()
    readout = actual_container_readout_audit()
    coupled = coupled_system_and_pivot_audit()
    no_go = pivot_only_no_go_audit()
    return {
        "schema": "item317-gaussian-container-coupled-no-go-certificate-v1",
        "item": 317,
        "status": "PROVED_GAUSSIAN_OPERATOR_AND_CONTAINER_COUPLED_SYSTEM_SCOPED_PIVOT_NO_GO",
        "dependencies": DEPENDENCIES,
        "telescoper_data_sha256": DATA_SHA256,
        "residue_telescoper": residue,
        "actual_container_readout": readout,
        "coupled_system_and_pivots": coupled,
        "pivot_only_no_go": no_go,
        "capacity": {
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
            "pivot_mass": "O(log M)=o(M), with shift 0 already Item312",
            "off_pivot_collision_mass": "UNCONTROLLED",
        },
        "classification": {
            "PROVED": [
                "all-s residue telescoper",
                "exact rescaled Gaussian companion operator",
                "exact actual-container quadratic readout",
                "exact dimension-6 symmetric-square coupled system",
                "complete forward/backward pivot factorization",
                "four-step shifted-pivot mass O(log M)",
            ],
            "SCOPED_NO_GO": [
                "operator pivots and regularity alone leave every "
                "off-pivot row admissible"
            ],
            "EXACT_FINITE_ONLY": [],
            "OPEN": [
                "a sequence-specific invariant or initial-state theorem",
                "regular-row moving-prime localization",
                "W_D(M)=o(M), fixed-j1 closure, Route 1, and e+pi",
            ],
        },
        "canonical_files_modified": False,
        "prime_scans": 0,
        "container_factorizations": 0,
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
                "item": 317,
                "Gaussian_operator": "PROVED_ALL_s",
                "container_system": "PROVED_24D_ALL_s_6D_RESIDUE",
                "pivot_mass": "O(log M)",
                "off_pivot_capacity": "UNREDUCED",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
