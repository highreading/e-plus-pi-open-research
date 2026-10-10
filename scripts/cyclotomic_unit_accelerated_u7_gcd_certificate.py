#!/usr/bin/env python3
"""Exact algebraic certificate for the accelerated u_7 moving-gcd theorem.

The companion source applies Grieve--Wang's moving-target theorem.  This
script checks the field/unit/support/isogeny and coefficient-structure
claims which enter that application.  It is not a numerical gcd scan.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import algebraic_unit_two_log_n5_ideal_content as base
import cyclotomic_unit_trace_probe as prior
import cyclotomic_unit_rational_ray_tropical as tropical


Pair = base.Pair
TRACE_GRAM = sp.Matrix(
    [
        [4, -2, 0, 0],
        [-2, 6, 0, 0],
        [0, 0, 10, 0],
        [0, 0, 0, 10],
    ]
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/cyclotomic_unit_accelerated_u7_gcd_certificate.json"
        ),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/cyclotomic_unit_accelerated_u7_gcd.md"),
    )
    args = parser.parse_args()

    w: Pair = (base.ZERO, base.kpow(base.ZETA, 4))
    units = [prior.cyclotomic_unit(w, a) for a in (3, 7, 9)]
    u3, u7, u9 = units
    if [base.plus_coordinates(u) for u in units] != [
        (1, 0, -1, 0),
        (2, 1, -1, -1),
        (2, 2, -1, -1),
    ]:
        raise AssertionError("cyclotomic-unit coordinates changed")

    action = {
        1: sp.eye(3),
        3: sp.Matrix([[-1, -1, -1], [0, 0, 1], [1, 0, 0]]),
        7: sp.Matrix([[0, 0, 1], [-1, -1, -1], [0, 1, 0]]),
        9: sp.Matrix([[0, 1, 0], [1, 0, 0], [-1, -1, -1]]),
    }
    sign_columns = {
        1: (1, 1, 1),
        3: (1, -1, -1),
        7: (-1, 1, -1),
        9: (-1, -1, 1),
    }
    for k in (1, 3, 7, 9):
        actual = tropical.sigma(u7, k)
        exponents = tuple(int(action[k][row, 1]) for row in range(3))
        expected = tropical.product_of_powers(units, exponents)
        if sign_columns[k][1] == -1:
            expected = prior.pneg(expected)
        if actual != expected:
            raise AssertionError(f"signed u_7 conjugate failed at embedding {k}")

    u7_exponent_columns = sp.Matrix.hstack(
        action[1][:, 1], action[3][:, 1], action[7][:, 1]
    )
    if u7_exponent_columns.det() != 1:
        raise AssertionError("three conjugates were not multiplicatively independent")

    multiplication = base.plus_multiplication_matrix(u7)
    if multiplication.det() != 1:
        raise AssertionError("u_7 was not a global unit")
    characteristic = sp.Poly(
        multiplication.charpoly().as_expr(), multiplication.charpoly().gen
    )
    root_intervals = sp.intervals(characteristic.as_expr(), eps=sp.Rational(1, 1000))
    intervals = [(sp.Rational(a), sp.Rational(b)) for (a, b), mult in root_intervals if mult == 1]
    if len(intervals) != 4 or not (
        -sp.Rational(1, 2) < intervals[0][0] < intervals[0][1] < 0
        and -sp.Rational(1, 2) < intervals[1][0] < intervals[1][1] < 0
        and 1 < intervals[2][0] < intervals[2][1] < sp.Rational(6, 5)
        and 5 < intervals[3][0] < intervals[3][1]
    ):
        raise AssertionError("exact conjugate separation failed")

    support_columns = sp.Matrix(
        [
            [2, 1, 1],
            [1, 2, 1],
            [1, 1, 2],
        ]
    )
    if support_columns.det() != 4:
        raise AssertionError("support map was not the claimed finite isogeny")

    # Exact fixed/anti-fixed checks at representative degrees.  The accepted
    # endpoint-asymptotic dependency proves that the anti-fixed component is
    # nonzero for all sufficiently large d; these finite records are only
    # independent structural checks, not the proof of that eventual claim.
    eta: base.Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    coefficient_structure_records = []
    for d in (2, 3, 7, 20, 50):
        edge = base.edge_integer_data(d, eta, eta_bar)
        u = edge["u_plus"]
        v = edge["v_plus"]
        tau_u = prior.tau(u)
        tau_v = prior.tau(v)
        u_fixed = tau_u == u
        v_anti_nonzero = tau_v != v
        if not u_fixed or not v_anti_nonzero:
            raise AssertionError("fixed/anti-fixed coefficient structure failed")
        coefficient_structure_records.append(
            {
                "d": d,
                "u_tau_fixed": u_fixed,
                "v_has_nonzero_tau_anti_part": v_anti_nonzero,
                "safe_denominator_digits": len(str(edge["safe_denominator"])),
                "least_clearing_digits": len(str(edge["q_min"])),
            }
        )

    if TRACE_GRAM.det() != 2000:
        raise AssertionError("trace Gram determinant changed")

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependency_paths = [
        Path(base.__file__).resolve(),
        Path(prior.__file__).resolve(),
        Path(tropical.__file__).resolve(),
        Path("sources/cyclotomic_unit_rational_ray_tropical.md").resolve(),
        Path("sources/arbitrary_integer_trace_lattice.md").resolve(),
        Path("sources/cyclotomic_unit_cone_selected_gcd.md").resolve(),
    ]
    if not source_path.exists() or not all(path.exists() for path in dependency_paths):
        raise FileNotFoundError("source or theorem dependency missing")
    result = {
        "description": (
            "Exact unit-independence, finite-isogeny support, trace, and "
            "coefficient-structure certificate for the accelerated u_7 ray."
        ),
        "scope_warning": (
            "The moving-target gcd estimate is a theorem application proved "
            "in the source note, not a consequence of finite diagnostics."
        ),
        "external_theorem": {
            "authors": "Nathan Grieve and Julie Tzu-Yueh Wang",
            "title": (
                "Greatest common divisors with moving targets and consequences "
                "for linear recurrence sequences"
            ),
            "theorem": "Theorem 1.2 via its proof through Theorems 3.1 and 3.2",
            "arxiv": "1902.09109v2",
            "doi": "10.1090/tran/8220",
            "hypothesis_audit": {
                "fixed_number_field": "K=Q(zeta_20)^+",
                "fixed_S": "the four archimedean places; all moving points are global units",
                "fixed_positive_degree": 4,
                "nonzero_constant_terms": (
                    "sigma_9(U_d), and eventually sigma_9(V_d); the theorem "
                    "is applied after deleting finitely many degrees"
                ),
                "slow_height": "O(d*log(d))=o(t_d)",
                "projective_scalar_normalization": (
                    "apply the theorem to F_d/sigma_9(U_d) and "
                    "G_d/sigma_9(V_d), each with constant coefficient 1"
                ),
                "coprime": "finite-isogeny pullbacks of nonproportional linear forms",
                "exceptional_character_branches": (
                    "Theorem 3.1's (ii') relation (3.36)-(3.37) and "
                    "Theorem 3.2's distinct-monomial ratio are both excluded "
                    "by multiplicative independence: every nontrivial "
                    "character has height exactly t_d times a positive constant"
                ),
                "only_infinite_subset": (
                    "on a hypothetical bad set, first take the infinite "
                    "outside-S-small subset from Theorem 3.1, then the nested "
                    "S-small subset from Theorem 3.2"
                ),
            },
        },
        "field": {
            "trace_gram": [[int(x) for x in row] for row in TRACE_GRAM.tolist()],
            "trace_discriminant": int(TRACE_GRAM.det()),
            "degree": 4,
        },
        "u7": {
            "coordinates": list(base.plus_coordinates(u7)),
            "multiplication_matrix": [
                [int(x) for x in row] for row in multiplication.tolist()
            ],
            "norm": int(multiplication.det()),
            "characteristic_polynomial": str(characteristic.as_expr()),
            "exact_root_intervals": [[str(a), str(b)] for a, b in intervals],
            "conjugate_exponent_columns_in_u3_u7_u9_basis": [
                [int(x) for x in row] for row in u7_exponent_columns.tolist()
            ],
            "conjugate_exponent_determinant": int(u7_exponent_columns.det()),
        },
        "polynomial_support": {
            "exponents": [[0, 0, 0], [2, 1, 1], [1, 2, 1], [1, 1, 2]],
            "nonconstant_exponent_matrix": [
                [int(x) for x in row] for row in support_columns.tolist()
            ],
            "isogeny_degree": abs(int(support_columns.det())),
        },
        "coefficient_structure_exact_records": coefficient_structure_records,
        "safe_height_ingredients": {
            "P": "P_d=d!*A_d has coefficients bounded by d!",
            "R": "R_d=d!*lcm(1,...,d)*B_d has coefficients bounded by d*d!*lcm",
            "conclusion": "h(U_d),h(V_d),h(F_d),h(G_d)=O(d*log(d))",
        },
        "ordinary_gcd_normalization": (
            "For Delta_d the generalized gcd after independent constant-term "
            "normalization: 4*log(gcd_Z(A_d,B_d)) <= Delta_d + "
            "h(sigma_9(U_d))+h(sigma_9(V_d)); this is the primewise "
            "valuation transfer, and the two added heights are O(d*log(d))."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependency_paths
        ],
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
