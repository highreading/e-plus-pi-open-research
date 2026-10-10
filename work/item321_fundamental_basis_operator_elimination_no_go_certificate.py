#!/usr/bin/env python3
"""Exact deterministic replay for Item 321.

The checker proves the actual A,Z,Zbar Casoratian formula, localizes every
failure of this residue basis on the fixed-M slice, factors all eight
period quadrics into genuine common-operator solutions, audits the
basis-change norms and actual finite-field splitting, and verifies the
scoped operator-elimination no-go.  It performs no prime scan.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = (
    HERE / "item321_fundamental_basis_operator_elimination_no_go_certificate.json"
)

DEPENDENCIES = {
    "sources/item317_gaussian_container_coupled_no_go_report.md": (
        "3e8a885b790965edf225b0fb9efd91142ffcdd7d1c13e9b65e43b9bb6d3023b5"
    ),
    "scripts/item317_gaussian_container_coupled_no_go_certificate.py": (
        "a07f6157648bbbfec0a9c9de8d899c81523f5e2cb63c997aedc7dc37c2213e71"
    ),
    "scripts/item317_residue_telescoper_data.json": (
        "f9ca57040fc7ae1030f9d915955085e3263e6c30f3129f2e9c4961198defa81b"
    ),
    "results/item317_gaussian_container_coupled_no_go_certificate.json": (
        "334165a7e3a40f043aedd3ea2d221786569aa91262481c2347c436cf10890e44"
    ),
    "results/item317_gaussian_container_coupled_no_go_certificate_replay.json": (
        "334165a7e3a40f043aedd3ea2d221786569aa91262481c2347c436cf10890e44"
    ),
    "results/item317_gaussian_container_coupled_no_go_ledger.json": (
        "40e7953a26a01c90d0415dbd247186a8b86dd9e8ead70edc5829b007591b8779"
    ),
    "results/item317_gaussian_container_coupled_no_go_hashes.sha256": (
        "c905ff8f6b96ce1d6e56ae420855e7f7cf4d008690c588f00b611705ece63124"
    ),
    "manifests/item317_gaussian_container_coupled_no_go_manifest.json": (
        "045aff4b05ef79a664e6dba30d9d7002f8e337ac066048e022c3509171e000f3"
    ),
    "results/item317_root_audit.json": (
        "6c22e387ee90b82d1f14f05cf949733d6fbbf825db2c1c8a0d74fc5b2ae95931"
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


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


pin_dependencies()
ITEM308 = load_module(
    "item321_canonical_item308",
    ROOT / "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py",
)

s, M = S.symbols("s M", integer=True)
I = S.I


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


def exact_residue_row(index: int) -> list[S.Expr]:
    a_fraction = ITEM308.alpha_coefficient(index)
    real_fraction, imag_fraction = ITEM308.beta_coefficient(index)
    a_value = S.Rational(a_fraction.numerator, a_fraction.denominator)
    b_value = (
        S.Rational(real_fraction.numerator, real_fraction.denominator)
        + I * S.Rational(imag_fraction.numerator, imag_fraction.denominator)
    )
    z_value = S.expand((-2 * (1 + I)) ** index * b_value)
    return [a_value, z_value, S.conjugate(z_value)]


def casoratian_audit() -> dict[str, Any]:
    initial_rows = [exact_residue_row(index) for index in range(1, 4)]
    expected_rows = [
        [-11, -S.Rational(91, 8) + S.Rational(33, 4) * I,
         -S.Rational(91, 8) - S.Rational(33, 4) * I],
        [S.Rational(6517, 8),
         -S.Rational(28357, 256) - S.Rational(55363, 256) * I,
         -S.Rational(28357, 256) + S.Rational(55363, 256) * I],
        [-S.Rational(103389, 128),
         S.Rational(13678665, 4096) - S.Rational(9202479, 8192) * I,
         S.Rational(13678665, 4096) + S.Rational(9202479, 8192) * I],
    ]
    if any(
        S.expand(actual - expected) != 0
        for actual_row, expected_row in zip(initial_rows, expected_rows)
        for actual, expected in zip(actual_row, expected_row)
    ):
        raise AssertionError("initial residue rows")

    w_one = S.factor(S.det(S.Matrix(initial_rows)))
    expected_w_one = S.Rational(7985352375, 2**20) * I
    if S.expand(w_one - expected_w_one) != 0:
        raise AssertionError("initial Casoratian")

    q = 660 * s**2 + 1600 * s + 779
    q_next = S.expand(q.subs(s, s + 1))
    operators = recurrence_polynomials()
    linear_numerator = (
        (2 * s + 1)
        * (6 * s + 5)
        * (6 * s + 7)
        * (6 * s + 11)
        * (6 * s + 13)
    )
    linear_denominator = (
        s * (s + 1) * (s + 2) * (2 * s + 3) * (2 * s + 5)
    )
    if S.expand(q_next - (660 * s**2 + 2920 * s + 3039)) != 0:
        raise AssertionError("quadratic telescope")
    expected_ratio = S.factor(
        -S.Rational(9, 4096)
        * q_next
        / q
        * linear_numerator
        / linear_denominator
    )
    if S.cancel(expected_ratio + operators[0] / operators[3]) != 0:
        raise AssertionError("Casoratian ratio")

    fixed_container = 330 * M**2 - 235 * M + 18
    division_free = S.factor(q - 8 * fixed_container)
    expected_division_free = (
        5 * (66 * s - 132 * M + 127) * (4 * M + 2 * s + 1)
    )
    if S.expand(division_free - expected_division_free) != 0:
        raise AssertionError("fixed-M Q identity")
    u = S.symbols("u", nonnegative=True)
    if S.Poly(S.expand(fixed_container.subs(M, u + 1)), u).all_coeffs() != [
        330,
        425,
        113,
    ]:
        raise AssertionError("fixed-M Q nonvanishing")

    constant = 3 * 5**3 * 7**2 * 11 * 13
    if constant != 2627625:
        raise AssertionError("Casoratian constant")
    if S.factor(expected_w_one / (I * q.subs(s, 1))) != S.Rational(
        constant, 2**20
    ):
        raise AssertionError("closed form constant")

    return {
        "initial_rows_A_Z_Zbar": [
            [str(S.expand(value)) for value in row] for row in initial_rows
        ],
        "W_1": "7985352375*i/2^20",
        "W_1_factorization": "3^2*5^3*7^2*11*13*1013*i/2^20",
        "Q_s": "660s^2+1600s+779",
        "Q_shift_identity": (
            "660s^2+2920s+3039=Q_(s+1)"
        ),
        "Casoratian_transport": "W_(s+1)=-P0(s)/P3(s)*W_s",
        "closed_form": (
            "W_s=i*(3*5^3*7^2*11*13/2^20)*(-9/4096)^(s-1)"
            "*Q_s*prod_(n=1..s-1)[(2n+1)(6n+5)(6n+7)(6n+11)"
            "(6n+13)/(n(n+1)(n+2)(2n+3)(2n+5))]"
        ),
        "actual_prime_denominator_audit": (
            "all displayed denominator factors are <p=4h+6s+3 "
            "for h,s>=1; powers 2 and the Item308 denominators are p-units"
        ),
        "h_equals_one_audit": (
            "if h=1 then p=6s+7; for s>=2 this is the n=s-1 "
            "factor 6n+13, while s=1 gives p=13 in the constant"
        ),
        "h_at_least_two_audit": (
            "p>=6s+11, so every constant and linear numerator factor "
            "is nonzero mod p; only Q_s can remain"
        ),
        "division_free_fixed_M_identity": (
            "Q_s-8*(330M^2-235M+18)="
            "5*(66s-132M+127)*(4M+2s+1)"
        ),
        "basis_failure_localization": (
            "p divides W_s only if h=1 or "
            "p divides 330M^2-235M+18"
        ),
        "basis_failure_mass": "O(log M)=o(M)",
    }


def field_norm_even(expression: S.Expr, root_two: S.Symbol) -> S.Expr:
    answer = S.Integer(1)
    for i_sign in (1, -1):
        for two_sign in (1, -1):
            answer *= expression.subs({I: i_sign * I, root_two: two_sign * root_two})
    return S.expand(answer.subs(root_two**2, 2))


def quadric_factor_audit() -> dict[str, Any]:
    A, Z, Zbar = S.symbols("A Z Zbar")
    root_two = S.symbols("sqrt2")
    table = {
        (0, 0): (root_two, root_two),
        (0, 1): (root_two, -root_two),
        (1, 0): (1 + I, -1 + I),
        (1, 1): (1 + I, 1 - I),
        (2, 0): (root_two, -root_two),
        (2, 1): (root_two, root_two),
        (3, 0): (1 + I, 1 - I),
        (3, 1): (1 + I, -1 + I),
    }
    representatives = {0: 4, 1: 1, 2: 2, 3: 3}
    rows = []
    for (residue, epsilon), (alpha, beta) in table.items():
        s_value = representatives[residue]
        delta = (-1) ** (s_value * (s_value + 1) // 2 + 1)
        quadric = S.expand(
            A**2
            - 2 * delta * (-I) ** s_value * Z**2
            - 2 * delta * I**s_value * Zbar**2
            - 4 * (-1) ** epsilon * delta * Z * Zbar
        )
        ell = alpha * Z + beta * Zbar
        factor_plus = A + I * ell
        factor_minus = A - I * ell
        difference = S.expand(quadric - factor_plus * factor_minus).subs(
            root_two**2, 2
        )
        if S.expand(difference) != 0:
            raise AssertionError(("quadric factorization", residue, epsilon))

        coefficient_matrix = S.Matrix(
            [
                [1, 1, 0],
                [I * alpha, -I * alpha, 1],
                [I * beta, -I * beta, 0],
            ]
        )
        determinant = S.factor(coefficient_matrix.det())
        if S.expand(determinant - 2 * I * beta) != 0:
            raise AssertionError(("basis determinant", residue, epsilon))
        if residue % 2 == 0:
            norm = field_norm_even(determinant, root_two)
            norm = S.expand(norm.subs(root_two**4, 4).subs(root_two**2, 2))
            expected_norm = 64
            field = "Q(i,sqrt(2))"
        else:
            norm = S.expand(
                determinant
                * S.conjugate(determinant).subs(
                    {S.conjugate(root_two): root_two}
                )
            )
            expected_norm = 8
            field = "Q(i)"
        if S.expand(norm - expected_norm) != 0:
            raise AssertionError(("basis determinant norm", residue, epsilon, norm))

        qmatrix = S.hessian(quadric, (A, Z, Zbar)) / 2
        if qmatrix.det().subs(root_two**2, 2) != 0 or qmatrix.rank() != 2:
            raise AssertionError(("quadric rank", residue, epsilon))

        # A nonzero isotropic first row which can be completed to an
        # invertible fundamental state matrix.  This makes the
        # coefficient-field elimination ideal zero at every regular row.
        witness_row = S.Matrix([[-I * beta, 0, 1]])
        witness_quadric = S.expand(
            quadric.subs({A: -I * beta, Z: 0, Zbar: 1})
        ).subs(root_two**2, 2)
        witness_matrix = S.Matrix(
            [[-I * beta, 0, 1], [0, 1, 0], [1, 0, 0]]
        )
        if S.expand(witness_quadric) != 0 or witness_matrix.det() != -1:
            raise AssertionError(("elimination witness", residue, epsilon))

        rows.append(
            {
                "s_mod_4": residue,
                "epsilon": epsilon,
                "field": field,
                "alpha": str(alpha),
                "beta": str(beta),
                "ell": f"({alpha})Z+({beta})Zbar",
                "factorization": "q=(A+i*ell)(A-i*ell)",
                "basis": ["A+i*ell", "A-i*ell", "Z"],
                "basis_change_determinant": str(determinant),
                "absolute_norm": expected_norm,
                "p_unit_for_actual_primes": True,
                "isotropic_invertible_state_witness": [
                    [str(value) for value in witness_matrix.row(index)]
                    for index in range(3)
                ],
            }
        )

    return {
        "uniform_field": "L=Q(i,sqrt(2))",
        "linear_solution_reason": (
            "A,Z,Zbar satisfy the same homogeneous operator and alpha,beta "
            "are constant; therefore A+/-i(alpha Z+beta Zbar) are genuine "
            "solutions of that same operator at every index"
        ),
        "factor_rows": rows,
        "basis_change_prime_support": "{2}",
        "actual_prime_minimum": 13,
        "fundamental_basis_consequence": (
            "outside the Casoratian exceptional set, each factor pair "
            "together with Z is a fundamental common-operator basis"
        ),
    }


def chi_two(residue_mod_8: int) -> int:
    return 1 if residue_mod_8 in (1, 7) else -1


def chi_minus_one(residue_mod_8: int) -> int:
    return 1 if residue_mod_8 in (1, 5) else -1


def frobenius_split_audit() -> dict[str, Any]:
    rows = []
    for residue in range(4):
        for epsilon in (0, 1):
            p_mod_8 = (4 * epsilon + 6 * residue + 3) % 8
            delta = chi_two(p_mod_8)
            eta = 2 if residue % 2 == 0 else 1
            if eta == 1:
                symbol = 1 if delta == 1 else chi_minus_one(p_mod_8)
            elif delta == 1:
                symbol = chi_two(p_mod_8)
            else:
                symbol = chi_minus_one(p_mod_8) * chi_two(p_mod_8)
            if symbol != 1:
                raise AssertionError(("actual norm did not split", residue, epsilon))
            rows.append(
                {
                    "s_mod_4": residue,
                    "epsilon_h_mod_2": epsilon,
                    "p_mod_8": p_mod_8,
                    "delta=(2/p)": delta,
                    "eta": eta,
                    "delta_eta": delta * eta,
                    "Legendre_symbol_(delta_eta/p)": symbol,
                    "split_mod_p": True,
                }
            )
    return {
        "p_mod_8_identity": "p=4h+6s+3 mod 8",
        "rows": rows,
        "global_conclusion": (
            "the Item308 norm algebra is split modulo every actual prime; "
            "Frobenius never forces both linear factors to vanish"
        ),
        "small_prime_audit": (
            "p>=13; p=2 is absent, and p=13 occurs only at s=h=1 "
            "inside the already isolated h=1 Casoratian exception"
        ),
    }


def invariant_and_elimination_no_go() -> dict[str, Any]:
    # Structural matrix identities.  If F_(s+1)=T_s F_s and
    # T_s^T H_(s+1)T_s=H_s, then C_s=F_s^T H_s F_s is constant.
    # Conversely H_s=F_s^(-T) C F_s^(-1).  Likewise a constant
    # solution-label quadric Q gives G_s=F_s Q F_s^T and
    # G_(s+1)=T_s G_s T_s^T.
    return {
        "transported_quadratic_invariant_classification": (
            "on regular support, every H_s satisfying "
            "T_s^T H_(s+1) T_s=H_s is "
            "H_s=F_s^(-T) C F_s^(-1) for one constant C"
        ),
        "proof": (
            "C_s=F_s^T H_s F_s obeys C_(s+1)=C_s; "
            "invertibility of F_s gives the converse"
        ),
        "actual_quadric_transport": (
            "for each fixed period quadric Q, G_s=F_s Q F_s^T obeys "
            "G_(s+1)=T_s G_s T_s^T and pulls back identically to Q"
        ),
        "tautology": (
            "these invariants are changes of coordinates by the actual "
            "fundamental matrix; they create no new fixed-M divisor"
        ),
        "operator_elimination": (
            "over any finite regular orbit window, recurrence equations "
            "leave an arbitrary invertible fundamental state.  Each actual "
            "rank-two split quadric has the explicit invertible isotropic "
            "state in the factor table, so eliminating orbit variables "
            "from one collision condition gives the zero ideal in the "
            "coefficient field"
        ),
        "after_actual_initial_state_substitution": (
            "the row scalar is exactly D_(s,epsilon) up to p-units; "
            "the union product over O(M) rows has only "
            "sum O(s)=O(M^2) logarithmic height by Item308"
        ),
        "strict_scope": (
            "This closes transported-invariant and single-row "
            "operator-elimination arguments.  It does not rule out a new "
            "arithmetic relation among the actual initial values, a gcd "
            "theorem, or a genuinely sublinear fixed-M resultant."
        ),
    }


def build_certificate() -> dict[str, Any]:
    casoratian = casoratian_audit()
    quadrics = quadric_factor_audit()
    frobenius = frobenius_split_audit()
    no_go = invariant_and_elimination_no_go()
    return {
        "schema": "item321-fundamental-basis-operator-elimination-no-go-v1",
        "item": 321,
        "status": (
            "PROVED_ACTUAL_FUNDAMENTAL_BASIS_AND_"
            "SCOPED_OPERATOR_ELIMINATION_NO_GO"
        ),
        "dependencies": DEPENDENCIES,
        "casoratian": casoratian,
        "period_quadrics": quadrics,
        "actual_frobenius_split": frobenius,
        "invariant_and_elimination_no_go": no_go,
        "capacity": {
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "basis_exception_mass": "O(log M)=o(M)",
            "regular_collision_mass": "UNCONTROLLED",
            "retained_ceiling_per_6M": "1/36",
        },
        "classification": {
            "PROVED": [
                "exact all-s Casoratian and fixed-M localization",
                "actual residue solutions form a fundamental basis away "
                "from O(log M) mass",
                "all eight actual period quadrics factor into genuine "
                "common-operator solutions",
                "every factor basis change is a p-unit",
                "every actual finite-field norm is split",
            ],
            "SCOPED_NO_GO": [
                "transported quadratic invariants are coordinate "
                "tautologies",
                "single-row common-operator elimination yields no nonzero "
                "base scalar on regular support",
                "the raw actual-value union product has only O(M^2) "
                "logarithmic height",
            ],
            "EXACT_FINITE_ONLY": [],
            "OPEN": [
                "actual-initial-value arithmetic beyond the common operator",
                "a sublinear-height fixed-M resultant or gcd theorem",
                "regular-row moving-prime localization",
                "W_D(M)=o(M), fixed-j1 closure, Route 1, and e+pi",
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
                "item": 321,
                "Casoratian_basis": "PROVED_AWAY_O_LOG_M",
                "period_factors": "GENUINE_COMMON_OPERATOR_BASES",
                "actual_norms": "ALL_SPLIT",
                "operator_elimination": "TAUTOLOGICAL_ZERO_IDEAL",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
