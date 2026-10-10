#!/usr/bin/env python3
"""Deterministic replay for Item 310.

This checker verifies the exact all-s constant-term decomposition data,
the D-finite/P-recursive closure graph, the actual-prime splitting table,
and the fixed-K hypergeometric comparison.  Bounded coefficient and
recurrence rows are replay controls only.  No primes are scanned and no
integer is factored.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = ROOT / "results" / "item310_j1_container_holonomy_no_go_certificate.json"
Q = Fraction

DEPENDENCIES = {
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
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pin_dependencies()
item308 = load(
    "item310_item308",
    ROOT / "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py",
)


def encode_fraction(value: Q) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


N_ZERO = [
    Q(4),
    Q(-4, 3),
    Q(-8, 3),
    Q(16, 3),
    Q(-3),
    Q(1),
]
N_ONE = [
    Q(0),
    Q(80, 3),
    Q(-224, 3),
    Q(256, 3),
    Q(-46),
    Q(10),
]


def affine_numerator_audit() -> dict[str, Any]:
    expected_pairs = list(zip(N_ZERO, N_ONE))
    symbolic_pairs = [
        (Q(4), Q(0)),
        (Q(-4, 3), Q(80, 3)),
        (Q(-8, 3), Q(-224, 3)),
        (Q(16, 3), Q(256, 3)),
        (Q(-3), Q(-46)),
        (Q(1), Q(10)),
    ]
    if expected_pairs != symbolic_pairs:
        raise AssertionError("affine numerator")

    controls = []
    for s_value in (1, 2, 3, 4, 6, 8):
        reconstructed = [
            constant + s_value * slope
            for constant, slope in expected_pairs
        ]
        actual = item308.base.rational_source(s_value)[0]
        if reconstructed != actual:
            raise AssertionError(("N_s control", s_value))
        controls.append(
            {
                "s": s_value,
                "N_s_low_to_high": [
                    encode_fraction(value) for value in actual
                ],
                "classification": "BOUNDED EXACT REPLAY ONLY",
            }
        )

    return {
        "identity": "N_s(t)=N_0(t)+s*N_1(t) in Q[s,t]",
        "N_0_low_to_high": [
            encode_fraction(value) for value in N_ZERO
        ],
        "N_1_low_to_high": [
            encode_fraction(value) for value in N_ONE
        ],
        "symbolic": True,
        "bounded_controls": controls,
    }


def qseries_multiply(
    left: list[Q], right: list[Q], maximum: int
) -> list[Q]:
    out = [Q(0)] * (maximum + 1)
    for j, x_value in enumerate(left[: maximum + 1]):
        for k, y_value in enumerate(right[: maximum + 1 - j]):
            out[j + k] += x_value * y_value
    return out


def integer_binomial_series(exponent: int, maximum: int) -> list[Q]:
    return [
        Q(math.comb(exponent, degree))
        if degree <= exponent
        else Q(0)
        for degree in range(maximum + 1)
    ]


def constant_term_controls() -> list[dict[str, Any]]:
    """Replay the base/ratio decomposition on a fixed bounded list."""
    answer = []
    f_constant = item308.gscale(
        item308.ginv((Q(1), Q(1))), Q(-1, 2)
    )
    r_constant = (Q(0), Q(1, 8))

    for s_value in (1, 2, 3, 4, 6, 8):
        maximum_a = 2 * s_value + 5
        split_half = qseries_multiply(
            item308.half_binomial_series(Q(1, 2), maximum_a),
            integer_binomial_series(3 * s_value, maximum_a),
            maximum_a,
        )
        direct_half = item308.half_binomial_series(
            Q(6 * s_value + 1, 2), maximum_a
        )
        if split_half != direct_half:
            raise AssertionError(("A base/ratio", s_value))

        q_value = 2 * s_value + 1
        r_value = 2 * s_value + 6
        original_constant = item308.ginv(
            item308.gmul(
                item308.gscale(
                    item308.gpow((Q(0), Q(1)), r_value),
                    2**q_value,
                ),
                item308.gpow((Q(1), Q(1)), q_value),
            )
        )
        split_constant = item308.gmul(
            f_constant, item308.gpow(r_constant, s_value)
        )
        if split_constant != original_constant:
            raise AssertionError(("B constant", s_value))

        alpha = item308.alpha_coefficient(s_value)
        real, imaginary = item308.beta_coefficient(s_value)
        answer.append(
            {
                "s": s_value,
                "A_s": encode_fraction(alpha),
                "B_s_real": encode_fraction(real),
                "B_s_imaginary": encode_fraction(imaginary),
                "A_identity": (
                    "F_A*R_A^s=(1+x)^(3s+1/2)/(1+x^2)^(2s+1)"
                ),
                "B_constant_identity": (
                    "1/(2^(2s+1)i^(2s+6)(1+i)^(2s+1))="
                    "-1/(2(1+i))*(i/8)^s"
                ),
                "classification": (
                    "FIXED BOUNDED REPLAY OF SYMBOLIC IDENTITIES"
                ),
            }
        )
    return answer


def constant_term_theorem() -> dict[str, Any]:
    return {
        "A_generating_function": (
            "-CT_x x^(-5) F_A(x)[N_0(1+x)u_A/(1-u_A)"
            "+N_1(1+x)u_A/(1-u_A)^2]"
        ),
        "F_A": "(1+x)^(1/2)/(1+x^2)",
        "R_A": "(1+x)^3/(1+x^2)^2",
        "u_A": "z*R_A/x^2",
        "B_generating_function": (
            "CT_x F_B(x)[N_0((1-i)(1+x))u_B/(1-u_B)"
            "+N_1((1-i)(1+x))u_B/(1-u_B)^2]"
        ),
        "F_B": (
            "-(1+x)^(1/2)/(2(1+i)(1+(1+i)x)^6"
            "(1+((1+i)/2)x))"
        ),
        "R_B": (
            "i(1+x)^3/(8(1+(1+i)x)^2"
            "(1+((1+i)/2)x)^2)"
        ),
        "u_B": "z*R_B/x^2",
        "summation_identities": [
            "sum_(s>=1)u^s=u/(1-u)",
            "sum_(s>=1)s*u^s=u/(1-u)^2",
        ],
        "proof_type": (
            "SYMBOLIC BASE/RATIO EXPONENT SPLIT FOR EVERY INTEGER s>=1"
        ),
        "bounded_replay": constant_term_controls(),
    }


def closure_graph() -> dict[str, Any]:
    return {
        "theorem_hypotheses": {
            "coefficient_field": "characteristic-zero Q(i)",
            "integrands": (
                "algebraic Laurent series in x,z; only algebraic branch "
                "is (1+x)^(1/2) with constant term one"
            ),
            "formal_expansion": (
                "power series in z; every z^s coefficient has a "
                "well-defined displayed x constant term"
            ),
            "positive_power_series_reformulation": (
                "equivalently extract coefficient rays (2s+5,s) and "
                "(2s,s) from F*N0/(1-zR) and "
                "F*N1*zR/(1-zR)^2, algebraic at (x,z)=(0,0)"
            ),
            "closure": (
                "generalized diagonals/constant terms of multivariate "
                "D-finite series are D-finite"
            ),
            "equivalence": (
                "univariate D-finite generating function iff "
                "coefficient sequence is P-recursive"
            ),
        },
        "nodes": [
            {
                "sequence": "A_s",
                "input": "A constant-term identity",
                "class": "P-recursive over Q",
            },
            {
                "sequence": "B_s",
                "input": "B constant-term identity",
                "class": "P-recursive over Q(i)",
            },
            {
                "sequence": "U_s,V_s",
                "input": "rational combinations of B_s and conjugate(B_s)",
                "class": "P-recursive over Q",
            },
            {
                "sequence": "a_s,b_s,0,b_s,1",
                "input": (
                    "Hadamard products with exponential and period-four "
                    "C-finite sequences"
                ),
                "class": "P-recursive integer sequences",
            },
            {
                "sequence": "D_s,0,D_s,1",
                "input": (
                    "Hadamard squares, exponential scaling, periodic "
                    "scaling, and subtraction"
                ),
                "class": "P-recursive integer sequences",
            },
        ],
        "conclusion": (
            "For epsilon=0,1 there exist nonzero polynomials q_j(s) "
            "with sum_j q_j(s)D_(s+j,epsilon)=0 on a regular tail."
        ),
        "minimal_operator_or_algebraicity": "OPEN / NOT CLAIMED",
    }


def small_legendre_symbol(discriminant: int, p_mod_8: int) -> int:
    if discriminant == 1:
        return 1
    symbol_two = 1 if p_mod_8 in (1, 7) else -1
    symbol_minus_one = 1 if p_mod_8 in (1, 5) else -1
    if discriminant == -1:
        return symbol_minus_one
    if discriminant == 2:
        return symbol_two
    if discriminant == -2:
        return symbol_minus_one * symbol_two
    raise ValueError(discriminant)


def splitting_table() -> list[dict[str, int]]:
    representative = {0: 4, 1: 1, 2: 2, 3: 3}
    answer = []
    for residue in range(4):
        s_value = representative[residue]
        for parity in (0, 1):
            p_mod_8 = (4 * parity + 6 * s_value + 3) % 8
            sign = item308.delta(s_value, parity)
            eta_value = item308.eta(s_value)
            discriminant = sign * eta_value
            symbol = small_legendre_symbol(discriminant, p_mod_8)
            if symbol != 1:
                raise AssertionError(
                    ("nonsplit actual class", residue, parity)
                )
            answer.append(
                {
                    "s_mod_4": residue,
                    "h_parity": parity,
                    "p_mod_8": p_mod_8,
                    "delta": sign,
                    "eta": eta_value,
                    "quadratic_parameter_delta_times_eta": discriminant,
                    "Legendre_symbol": symbol,
                }
            )
    return answer


def comparison_term(k_max: int, s_value: int) -> int:
    if k_max < 7 or s_value < 1:
        raise ValueError((k_max, s_value))
    return math.prod(
        math.comb(k_value * s_value, s_value)
        for k_value in range(7, k_max + 1)
    )


def recurrence_ratio(k_max: int, s_value: int) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for k_value in range(7, k_max + 1):
        numerator *= math.prod(
            k_value * s_value + j_value
            for j_value in range(1, k_value + 1)
        )
        denominator *= s_value + 1
        denominator *= math.prod(
            (k_value - 1) * s_value + j_value
            for j_value in range(1, k_value)
        )
    return numerator, denominator


def telescoping_height_symbols(k_max: int) -> dict[int, int]:
    coefficients: dict[int, int] = {}
    for k_value in range(7, k_max + 1):
        coefficients[k_value] = coefficients.get(k_value, 0) + 1
        coefficients[k_value - 1] = (
            coefficients.get(k_value - 1, 0) - 1
        )
    return {
        index: coefficient
        for index, coefficient in coefficients.items()
        if coefficient
    }


def comparison_controls() -> list[dict[str, Any]]:
    answer = []
    for k_max in (7, 8, 12):
        if telescoping_height_symbols(k_max) != {6: -1, k_max: 1}:
            raise AssertionError(("height telescope", k_max))
        degree = k_max * (k_max + 1) // 2 - 21
        rows = []
        for s_value in range(1, 6):
            current = comparison_term(k_max, s_value)
            following = comparison_term(k_max, s_value + 1)
            numerator, denominator = recurrence_ratio(
                k_max, s_value
            )
            if denominator * following != numerator * current:
                raise AssertionError(
                    ("hypergeometric recurrence", k_max, s_value)
                )
            rows.append(
                {
                    "s": s_value,
                    "P_s": current,
                    "P_s_plus_1": following,
                    "recurrence_verified": True,
                }
            )
        answer.append(
            {
                "K": k_max,
                "recurrence_order": 1,
                "numerator_and_denominator_degree": degree,
                "height_rate": f"{k_max}*log({k_max})-6*log(6)",
                "rows": rows,
                "classification": "BOUNDED EXACT RECURRENCE REPLAY ONLY",
            }
        )
    return answer


def mass_row(k_max: int) -> dict[str, Any]:
    lower_endpoint = Q(4 * k_max, 3 * k_max - 2)
    mass = Q(3, 2) - lower_endpoint
    expected = Q(k_max - 6, 2 * (3 * k_max - 2))
    if mass != expected:
        raise AssertionError(("mass normalization", k_max))
    return {
        "K": k_max,
        "s_slice": f"s>=(4M+1)/({3*k_max-2})",
        "prime_interval_lower_coefficient": encode_fraction(lower_endpoint),
        "prime_interval_upper_coefficient": "3/2",
        "log_mass_per_M": encode_fraction(mass),
        "log_mass_per_6M": encode_fraction(mass / 6),
    }


def comparison_theorem() -> dict[str, Any]:
    return {
        "sequence": "P_s^(K)=product_(k=7..K) binomial(k*s,s), K>=7",
        "nonzero": "P_s^(K)>0 for every s>=1",
        "first_order_recurrence": (
            "S_K(s)P_(s+1)-R_K(s)P_s=0, with the exact products "
            "R_K,S_K in the report"
        ),
        "recurrence_degree": "K(K+1)/2-21",
        "height": (
            "log P_s^(K)=s(K log K-6 log 6)+O_K(log s)"
        ),
        "prime_localization": (
            "If 6s<p<=Ks is prime, k=ceil(p/s) lies in [7,K] "
            "and v_p binomial(ks,s)=1, so p divides P_s^(K)."
        ),
        "norm_comparison": (
            "a_tilde=b_tilde=P_s^(K); "
            "D_tilde=(P_s^(K))^2(2^(3s+1)-delta)"
        ),
        "norm_comparison_properties": (
            "nonzero, integer, P-recursive, exponential height, "
            "same eta*z^2-delta*b^2 shape, denominator one"
        ),
        "fixed_M_logic": [
            "Every actual candidate has p_s-6s>=7.",
            "p_s<=Ks iff s>=(4M+1)/(3K-2).",
            "The slice maps to [4K/(3K-2) M, 3M/2] up to O(1).",
        ],
        "mass_rows": [
            mass_row(k_max) for k_max in (7, 8, 12, 30, 100)
        ],
        "limit": "(K-6)/(2(3K-2)) -> 1/6 per M",
        "normalized_limit": "(K-6)/(12(3K-2)) -> 1/36 per 6M",
        "scope": (
            "NO-GO FOR QUALITATIVE P-RECURSIVENESS, EXPONENTIAL "
            "HEIGHT, NONVANISHING, AND NORM SHAPE ONLY"
        ),
        "not_ruled_out": (
            "a theorem using the exact Item308 operator coefficients, "
            "a separately bounded operator class, an actual moving-prime "
            "gcd bound, or exact factor localization"
        ),
        "bounded_controls": comparison_controls(),
    }


def build_result() -> dict[str, Any]:
    upstream = item308.upstream_admission()
    return {
        "schema": "item310-j1-container-holonomy-no-go-v1",
        "item": 310,
        "title": (
            "P-recursive structure of the all-s j=1 containers "
            "and its arithmetic limit"
        ),
        "dependencies": DEPENDENCIES,
        "upstream_admission": upstream,
        "affine_numerator": affine_numerator_audit(),
        "constant_term_generating_functions": constant_term_theorem(),
        "D_finite_P_recursive_closure": closure_graph(),
        "actual_prime_norm_splitting": {
            "theorem": (
                "(delta_s_epsilon*eta_s/p)=1 on every actual prime class"
            ),
            "table": splitting_table(),
            "capacity_consequence": (
                "quadratic norm splitting excludes zero actual candidates"
            ),
        },
        "hypergeometric_comparison_no_go": comparison_theorem(),
        "fixed_M_capacity": {
            "raw_log_mass": "M/6+o(M)=1/36 per 6M",
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
        },
        "smallest_remaining_lemma": (
            "Use the exact Item308 annihilator/diagonal to prove W_D(M)=o(M), "
            "or localize the exact D_s_epsilon prime factors away from the "
            "tied interval on all but weighted-o(M) actual indices."
        ),
        "strict_labels": {
            "constant_term_identities_all_s": "PROVED",
            "actual_D_sequences_P_recursive": "PROVED",
            "actual_norm_splitting_automatic": "PROVED",
            "qualitative_P_recursive_height_norm_no_go": "PROVED",
            "bounded_rows": "EXACT FINITE ONLY / REPLAY ONLY",
            "minimal_or_arithmetically_useful_actual_operator": "OPEN",
            "actual_generating_function_algebraicity": "OPEN",
            "actual_factor_localization_or_W_D_o_M": "OPEN",
            "prime_scan_or_factorization": "NONE",
            "capacity_booking": "ZERO",
            "Route_1_and_any_conclusion_about_e_plus_pi": "OPEN",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "item": result["item"],
                "constant_term_identities": "PROVED_ALL_s",
                "actual_container_structure": "P_RECURSIVE",
                "actual_norm_splitting_exclusions": 0,
                "comparison_family": "NONZERO_FIRST_ORDER_HYPERGEOMETRIC",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

