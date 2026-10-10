#!/usr/bin/env python3
"""Exact replay for Item 326.

The checker constructs the true Item-317 scalar companion, eliminates its
four step-12 readouts to an order-three determinant recurrence, verifies
that all four recurrence coefficients are nonzero for every positive
integer index, and checks the recurrence on the actual Item-308/321
factor solutions with their exact initial values.  It also replays one
declared p=47 selected-factor control.  It performs no prime scan.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as S
from sympy.polys.domains import QQ


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item326_j1_selected_factor_step12_no_go_certificate.json"

DEPENDENCIES = {
    "sources/item308_j1_all_s_fixed_divisor_no_go_report.md":
        "4eb8f8c37dfde9d19e57c8df5ff8090bd95f03be59fff7d6aede55d02993bdc8",
    "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py":
        "9b60d380b503c7ac9fed13792fae67735cfcf6b0f376581a0076fde16a82f0b9",
    "results/item308_j1_all_s_fixed_divisor_no_go_certificate.json":
        "4efff9ca2fb1bc11cc6030e260ff73aae89c28bd157bb41fa6bbc3b32e41e5cf",
    "results/item308_root_audit.json":
        "11feb8105ea46c27d83df2449404297fe74709eceaa8be6a21bd9484cbffba22",
    "manifests/item308_j1_all_s_fixed_divisor_no_go_manifest.json":
        "1c4721f43b5bbdc0c68e4d9fd689562a32a4af4fbbab2a9e7075da96b151b4d5",
    "sources/item317_gaussian_container_coupled_no_go_report.md":
        "3e8a885b790965edf225b0fb9efd91142ffcdd7d1c13e9b65e43b9bb6d3023b5",
    "scripts/item317_gaussian_container_coupled_no_go_certificate.py":
        "a07f6157648bbbfec0a9c9de8d899c81523f5e2cb63c997aedc7dc37c2213e71",
    "scripts/item317_residue_telescoper_data.json":
        "f9ca57040fc7ae1030f9d915955085e3263e6c30f3129f2e9c4961198defa81b",
    "results/item317_gaussian_container_coupled_no_go_certificate.json":
        "334165a7e3a40f043aedd3ea2d221786569aa91262481c2347c436cf10890e44",
    "results/item317_root_audit.json":
        "6c22e387ee90b82d1f14f05cf949733d6fbbf825db2c1c8a0d74fc5b2ae95931",
    "manifests/item317_gaussian_container_coupled_no_go_manifest.json":
        "045aff4b05ef79a664e6dba30d9d7002f8e337ac066048e022c3509171e000f3",
    "sources/item321_fundamental_basis_operator_elimination_no_go_report.md":
        "bb41380371b6e591c4670aeb85d41520b0fb2b7f5f4d377e44bd531b5fa1b5c1",
    "scripts/item321_fundamental_basis_operator_elimination_no_go_certificate.py":
        "d5352d1bbcb77f875dc7e8eadc36c5f43d23f9dd3ccee06449c8fa7834577b1e",
    "results/item321_fundamental_basis_operator_elimination_no_go_certificate.json":
        "c196625c48a6e1f154cbbed29bc938eff53a318f172bb7679ade099aa5da3c35",
    "results/item321_fundamental_basis_operator_elimination_no_go_root_audit.json":
        "9759809da8c264f9d4975491f5520c44bf78905471272bd688bfe3ce3773eed6",
    "manifests/item321_fundamental_basis_operator_elimination_no_go_manifest.json":
        "3555ca387f7b20366a4874fc161c9c048500486ec4126e94c1f07b97dcc7237f",
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
ITEM308 = load_module(
    "item326_pinned_item308",
    ROOT / "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py",
)


K, x = S.polys.fields.field("x", QQ)


def recurrence_polynomials(value):
    return [
        9 * (2 * value + 1) * (6 * value + 5) * (6 * value + 7)
        * (6 * value + 11) * (6 * value + 13)
        * (660 * value**2 + 2920 * value + 3039),
        24 * value * (6 * value + 11) * (6 * value + 13)
        * (1697520 * value**4 + 10905280 * value**3
           + 24360488 * value**2 + 22368528 * value + 7001703),
        768 * value * (value + 1) * (2 * value + 3)
        * (6 * value + 13)
        * (3960 * value**3 + 20820 * value**2
           + 33034 * value + 14047),
        4096 * value * (value + 1) * (value + 2)
        * (2 * value + 3) * (2 * value + 5)
        * (660 * value**2 + 1600 * value + 779),
    ]


def companion(value):
    p0, p1, p2, p3 = recurrence_polynomials(value)
    return [
        [K.zero, K.one, K.zero],
        [K.zero, K.zero, K.one],
        [-p0 / p3, -p1 / p3, -p2 / p3],
    ]


def matrix_multiply(left, right):
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(3)), K.zero)
            for j in range(3)
        ]
        for i in range(3)
    ]


def determinant_three(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2]
                        - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2]
                          - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1]
                          - matrix[1][1] * matrix[2][0])
    )


def primitive_integer_coefficients(poly) -> list[int]:
    degree = poly.degree()
    data = poly.to_dict()
    denominator_lcm = 1
    for coefficient in data.values():
        denominator_lcm = math.lcm(denominator_lcm, coefficient.denominator)
    coefficients = []
    for exponent in range(degree, -1, -1):
        coefficient = data.get((exponent,), QQ.zero)
        coefficients.append(
            int(coefficient.numerator * (denominator_lcm // coefficient.denominator))
        )
    content = 0
    for coefficient in coefficients:
        content = math.gcd(content, abs(coefficient))
    if content == 0:
        raise AssertionError("zero polynomial")
    return [coefficient // content for coefficient in coefficients]


def coefficient_metrics(coefficients: list[int]) -> dict[str, Any]:
    signs = sorted({(value > 0) - (value < 0) for value in coefficients})
    canonical = json.dumps(coefficients, separators=(",", ":"))
    return {
        "degree": len(coefficients) - 1,
        "coefficient_count": len(coefficients),
        "coefficient_signs": signs,
        "zero_coefficients": coefficients.count(0),
        "coefficient_list_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
        "total_decimal_digits": sum(len(str(abs(value))) for value in coefficients),
        "maximum_decimal_digits": max(len(str(abs(value))) for value in coefficients),
    }


def evaluate_fraction_field(value, integer: int) -> S.Rational:
    numerator = value.numer.evaluate(0, integer)
    denominator = value.denom.evaluate(0, integer)
    quotient = numerator / denominator
    return S.Rational(quotient.numerator, quotient.denominator)


def step_twelve_recurrence_audit() -> tuple[dict[str, Any], list[Any]]:
    identity = [
        [K.one, K.zero, K.zero],
        [K.zero, K.one, K.zero],
        [K.zero, K.zero, K.one],
    ]
    transfer = identity
    rows = [[K.one, K.zero, K.zero]]
    for shift in range(36):
        transfer = matrix_multiply(companion(x + shift), transfer)
        if (shift + 1) % 12 == 0:
            rows.append(transfer[0])

    minors = []
    for omitted in range(4):
        minor = determinant_three(
            [rows[index] for index in range(4) if index != omitted]
        )
        minors.append(minor)
    deltas = [minor if index % 2 == 0 else -minor
              for index, minor in enumerate(minors)]

    relation = [
        sum((deltas[index] * rows[index][coordinate]
             for index in range(4)), K.zero)
        for coordinate in range(3)
    ]
    if relation != [K.zero, K.zero, K.zero]:
        raise AssertionError("Laplace recurrence")

    expected_degrees = [(117, 117), (116, 116), (92, 92), (68, 68)]
    expected_numerator_signs = [[1], [-1], [-1], [-1]]
    coefficient_rows = []
    for index, delta in enumerate(deltas):
        numerator_coefficients = primitive_integer_coefficients(delta.numer)
        denominator_coefficients = primitive_integer_coefficients(delta.denom)
        numerator_metrics = coefficient_metrics(numerator_coefficients)
        denominator_metrics = coefficient_metrics(denominator_coefficients)
        if (
            (numerator_metrics["degree"], denominator_metrics["degree"])
            != expected_degrees[index]
            or numerator_metrics["coefficient_signs"]
            != expected_numerator_signs[index]
            or numerator_metrics["zero_coefficients"] != 0
            or not set(denominator_metrics["coefficient_signs"]).issubset({0, 1})
            or 1 not in denominator_metrics["coefficient_signs"]
        ):
            raise AssertionError(("coefficient audit", index))
        coefficient_rows.append(
            {
                "j": index,
                "Delta_j_definition":
                    f"(-1)^{index} det(rows R_k with k!={index})",
                "numerator": numerator_metrics,
                "denominator": denominator_metrics,
                "nonzero_for_every_integer_s_at_least_1": True,
            }
        )

    return {
        "scalar_companion":
            "T_s=[[0,1,0],[0,0,1],[-P0/P3,-P1/P3,-P2/P3]]",
        "row_definition":
            "R_j(s)=e0^T T_(s+12j-1)...T_s for j=1,2,3; R_0=e0^T",
        "coefficient_definition":
            "Delta_j(s)=(-1)^j det of the 3x3 matrix obtained by omitting R_j",
        "exact_recurrence":
            "sum_(j=0..3) Delta_j(s)y_(s+12j)=0 for every scalar solution y",
        "Laplace_vector_identity": "sum_j Delta_j(s)R_j(s)=0 in Q(s)^3",
        "coefficient_rows": coefficient_rows,
        "order_exact_over_Q_of_s": 3,
        "all_positive_integer_coefficients_nonzero": True,
        "finite_fit_used": False,
    }, deltas


I = S.I
ROOT_TWO = S.Symbol("sqrt2")

FACTOR_TABLE = {
    (0, 0): (ROOT_TWO, ROOT_TWO),
    (0, 1): (ROOT_TWO, -ROOT_TWO),
    (1, 0): (1 + I, -1 + I),
    (1, 1): (1 + I, 1 - I),
    (2, 0): (ROOT_TWO, -ROOT_TWO),
    (2, 1): (ROOT_TWO, ROOT_TWO),
    (3, 0): (1 + I, 1 - I),
    (3, 1): (1 + I, -1 + I),
}


def factorization_audit() -> dict[str, Any]:
    a_symbol, z_symbol, zbar_symbol = S.symbols("A Z Zbar")
    rows = []
    representatives = {0: 4, 1: 1, 2: 2, 3: 3}
    for residue in range(4):
        representative = representatives[residue]
        delta_zero = (-1) ** (
            representative * (representative + 1) // 2 + 1
        )
        for parity in (0, 1):
            alpha, beta = FACTOR_TABLE[(residue, parity)]
            ell = alpha * z_symbol + beta * zbar_symbol
            product = S.expand((a_symbol + I * ell) * (a_symbol - I * ell))
            expected = S.expand(
                a_symbol**2
                - 2 * delta_zero * (-I) ** representative * z_symbol**2
                - 2 * delta_zero * I**representative * zbar_symbol**2
                - 4 * (-1) ** parity * delta_zero * z_symbol * zbar_symbol
            )
            difference = S.Poly(
                S.expand(product - expected), ROOT_TWO, domain="EX"
            ).rem(S.Poly(ROOT_TWO**2 - 2, ROOT_TWO, domain="EX"))
            if difference.as_expr() != 0:
                raise AssertionError(("factorization", residue, parity))
            rows.append({"s_mod_4": residue, "epsilon": parity})
    return {
        "normalized_container":
            "q_(s,epsilon)=D_(s,epsilon)/(9*2^(27s+21))",
        "exact_factorization_on_matching_phase":
            "q_(s,epsilon)=Y_plus_(r,epsilon)(s)*Y_minus_(r,epsilon)(s)",
        "coefficient_field": "Q(i,sqrt(2))",
        "actual_prime_unit_audit":
            "all actual p>=13 are unramified and all discarded scalings/denominators are p-units",
        "symbolic_rows_verified": len(rows),
    }


@functools.cache
def exact_residue_row(index: int) -> tuple[S.Expr, S.Expr, S.Expr]:
    alpha = ITEM308.alpha_coefficient(index)
    beta_real, beta_imaginary = ITEM308.beta_coefficient(index)
    a_value = S.Rational(alpha.numerator, alpha.denominator)
    b_value = (
        S.Rational(beta_real.numerator, beta_real.denominator)
        + I * S.Rational(beta_imaginary.numerator, beta_imaginary.denominator)
    )
    z_value = S.expand((-2 * (1 + I)) ** index * b_value)
    return a_value, z_value, S.conjugate(z_value)


def selected_factor(index: int, residue: int, parity: int, sign: int) -> S.Expr:
    a_value, z_value, zbar_value = exact_residue_row(index)
    alpha, beta = FACTOR_TABLE[(residue, parity)]
    return S.expand(
        a_value + sign * I * (alpha * z_value + beta * zbar_value)
    )


def actual_initial_value_audit(deltas: list[Any]) -> dict[str, Any]:
    initial_strings = []
    recurrence_checks = 0
    representatives = {0: 4, 1: 1, 2: 2, 3: 3}
    for residue in range(4):
        for parity in (0, 1):
            for sign in (-1, 1):
                initial_triple = [
                    S.sstr(selected_factor(index, residue, parity, sign))
                    for index in (1, 2, 3)
                ]
                initial_strings.append(
                    {
                        "residue": residue,
                        "parity": parity,
                        "sign": sign,
                        "values_at_1_2_3": initial_triple,
                    }
                )

                start = representatives[residue]
                coefficients = [evaluate_fraction_field(value, start)
                                for value in deltas]
                relation = S.expand(
                    sum(
                        coefficients[j]
                        * selected_factor(start + 12 * j, residue, parity, sign)
                        for j in range(4)
                    )
                )
                if relation != 0:
                    raise AssertionError(
                        ("actual factor recurrence", residue, parity, sign)
                    )
                recurrence_checks += 1

    canonical = json.dumps(initial_strings, sort_keys=True, separators=(",", ":"))
    return {
        "factor_definition":
            "Y_(r,epsilon)^sign(n)=A_n+sign*i*(alpha_(r,epsilon)Z_n+beta_(r,epsilon)Zbar_n)",
        "factor_table": {
            f"r={residue},epsilon={parity}": [str(alpha), str(beta)]
            for (residue, parity), (alpha, beta) in FACTOR_TABLE.items()
        },
        "initial_values_source":
            "actual Item-308 coefficient formulas at n=1,2,3; no free state",
        "number_of_actual_factor_initial_triples": len(initial_strings),
        "actual_initial_triples_sha256":
            hashlib.sha256(canonical.encode()).hexdigest(),
        "direct_exact_step12_checks": recurrence_checks,
        "checked_phase_starts": [1, 2, 3, 4],
        "largest_direct_coefficient_index": 40,
    }


def rational_mod(value: S.Expr, prime: int) -> int:
    value = S.Rational(value)
    return int(value.p % prime) * pow(int(value.q % prime), -1, prime) % prime


def selected_p47_control() -> dict[str, Any]:
    prime = 47
    root_two = 7
    plus_values = []
    minus_values = []
    for index in (2, 14, 26, 38):
        a_value, z_value, _ = exact_residue_row(index)
        a_mod = rational_mod(a_value, prime)
        y_mod = rational_mod(S.im(z_value), prime)
        plus_values.append((a_mod - 2 * root_two * y_mod) % prime)
        minus_values.append((a_mod + 2 * root_two * y_mod) % prime)
    if plus_values != [43, 0, 44, 13] or minus_values != [0, 0, 35, 44]:
        raise AssertionError("p=47 selected-factor control")

    aggregate = (
        ITEM308.alpha_coefficient(2),
        *ITEM308.beta_coefficient(2),
    )
    integer_form = ITEM308.integer_form(2, 0, aggregate)
    if integer_form["D_s_epsilon"] % prime != 0:
        raise AssertionError("p=47 selected container")

    return {
        "classification": "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN",
        "actual_index": {"M": 34, "s": 2, "h": 8, "p": 47, "epsilon": 0},
        "embedding": "sqrt(2)=7 modulo 47",
        "Y_plus_at_s_2_14_26_38": plus_values,
        "Y_minus_at_s_2_14_26_38": minus_values,
        "selected_container_D_2_0_mod_47": 0,
        "next_fixed_M_candidate_at_s_plus_3": 49,
        "next_candidate_is_composite": True,
        "scope":
            "Item-308 selected eliminant/container control only; not a full Item-264 collision",
    }


def fixed_M_and_capacity_audit() -> dict[str, Any]:
    M, s_value, j = S.symbols("M s j", integer=True)
    p_value = (4 * M + 2 * s_value + 1) / 3
    h_value = (M - 4 * s_value - 2) / 3
    if (
        S.expand(p_value.subs(s_value, s_value + 3 * j) - p_value) != 2 * j
        or S.expand(h_value.subs(s_value, s_value + 3 * j) - h_value) != -4 * j
    ):
        raise AssertionError("fixed-M shifts")
    return {
        "fixed_M_indexing": {
            "S_M": "s>=1, 4s<=M-5, s=M+1 mod 3",
            "p_s": "(4M+2s+1)/3",
            "h_s": "(M-4s-2)/3",
            "s_to_s_plus_3j": "p to p+2j, h to h-4j",
            "epsilon_constant": True,
            "four_phase_step12_prime_gaps": [0, 8, 16, 24],
        },
        "analytic_input":
            "standard Brun/Selberg two-dimensional upper-bound sieve: for fixed nonzero d, #{n<=X:n and n+2d prime}=O_d(X/log^2 X)",
        "weighted_consequence":
            "sum log p over fixed-M rows with both p_s and p_(s+3d) prime is O_d(M/log M)=o(M)",
        "finite_window_consequence":
            "the union over any fixed finite set of nonzero row offsets also has o(M) logarithmic mass",
        "raw_candidate_mass_after_removing_bounded_gap_pairs":
            "M/6+o(M); isolated candidate primes retain the full raw first-order mass",
        "scoped_no_go":
            "a cross-row gcd/resultant whose hypotheses require selected collisions at two bounded-offset actual rows can control only zero-rate overlap; it does not control isolated one-row collisions",
        "not_closed":
            "a theorem forcing every selected collision to propagate, or a one-row prime-factor localization using the actual initial values",
    }


def build_certificate() -> dict[str, Any]:
    recurrence, deltas = step_twelve_recurrence_audit()
    factorization = factorization_audit()
    actual = actual_initial_value_audit(deltas)
    p47 = selected_p47_control()
    capacity = fixed_M_and_capacity_audit()
    return {
        "schema": "item326-j1-selected-factor-step12-no-go-certificate-v1",
        "item": 326,
        "date": "2026-09-01",
        "status":
            "PROVED_ACTUAL_SELECTED_FACTOR_STEP12_RECURRENCE_AND_SCOPED_BOUNDED_GAP_NO_GO",
        "dependencies": DEPENDENCIES,
        "actual_factorization": factorization,
        "step12_scalar_recurrence": recurrence,
        "actual_initial_values": actual,
        "selected_p47_control": p47,
        "fixed_M_capacity_audit": capacity,
        "capacity": {
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "bounded_gap_cross_row_overlap_mass": "o(M)",
            "isolated_selected_collision_mass": "UNCONTROLLED",
            "retained_ceiling_per_6M": "1/36",
        },
        "classification": {
            "PROVED": [
                "exact determinant-form order-three step-12 recurrence for every actual selected factor",
                "all four recurrence coefficients nonzero over Q at every positive integer index",
                "all factor sequences initialized by the true Item-308/321 values rather than a free state",
                "fixed-M four-phase indexing and bounded-gap prime-pair weighted mass o(M)",
            ],
            "SCOPED_NO_GO": [
                "bounded-window cross-row mechanisms requiring two actual candidate-prime collision rows touch only o(M) overlap and do not control isolated rows"
            ],
            "EXACT_FINITE_ONLY": [
                "one preselected p=47 selected-eliminant factor replay; no scan or asymptotic inference",
                "16 direct actual-value substitutions through index 40; the all-index theorem comes from the Laplace identity",
            ],
            "OPEN": [
                "a single-row theorem for the actual selected factor values",
                "a bridge forcing propagation from every original collision",
                "W_D(M)=o(M), W_off(M)=o(M), fixed-j1 closure, Route 1, and e+pi",
            ],
        },
        "prime_scans": 0,
        "canonical_files_modified": False,
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
                "item": 326,
                "step12_recurrence": "PROVED_ORDER_3_ACTUAL_INITIAL_VALUES",
                "bounded_gap_overlap": "o(M)",
                "isolated_rows": "UNCONTROLLED",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
