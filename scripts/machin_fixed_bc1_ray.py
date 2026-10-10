#!/usr/bin/env python3
"""Exact checks for the non-diagonal ray (a,b,c)=(N-1,1,1), N odd.

The closed formulas and their asymptotic/p-adic proof are in
``sources/machin_endpoint_asymptotics.md``.  Small N are cross-checked
against the general exact linear solver.  N=479=1+2*239 is an exact first
nontrivial check of the subsequence used in the divergence theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

from machin_nondiagonal_probe import primitive_solution
from mixed_hermite_pade_probe import f_coefficient

sys.set_int_max_str_digits(0)

P = 239


def valuation_int(value: int, prime: int) -> int | None:
    if value == 0:
        return None
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def valuation_positive(value: int, prime: int) -> int:
    answer = valuation_int(value, prime)
    if answer is None:
        raise ValueError("valuation of zero is undefined")
    return answer


def alternating_sign(index: int) -> int:
    """Return (-1)^((index-1)/2) for a positive odd index."""
    if index < 1 or index % 2 == 0:
        raise ValueError("index must be positive and odd")
    return 1 if ((index - 1) // 2) % 2 == 0 else -1


def floor_log_positive(value: int, base: int) -> int:
    if value < 1 or base < 2:
        raise ValueError("invalid integer logarithm arguments")
    answer = 0
    power = base
    while power <= value:
        answer += 1
        power *= base
    return answer


def largest_odd_exact_valuation_below(N: int, exponent: int) -> int | None:
    """Largest positive odd r<N with v_P(r)=exponent, if it exists."""
    base = P**exponent
    quotient = (N - 1) // base
    if quotient % 2 == 0:
        quotient -= 1
    while quotient > 0 and quotient % P == 0:
        quotient -= 2
    if quotient <= 0:
        return None
    result = base * quotient
    if result >= N or result % 2 == 0:
        raise RuntimeError("internal largest-candidate error")
    if valuation_positive(result, P) != exponent:
        raise RuntimeError("internal exact-valuation error")
    return result


def leading_residue_record(N: int) -> dict:
    """Exact first 239-adic residue test from Proposition 6.1."""
    if N < 1 or N % 2 == 0:
        raise ValueError("N must be positive and odd")
    D = N * N + N - 1
    a_N = valuation_positive(N + 1, P)
    d_N = valuation_positive(D, P)
    star_exponent = N - a_N + d_N

    earlier_candidates = []
    exponent = 0
    while P**exponent < N:
        r = largest_odd_exact_valuation_below(N, exponent)
        if r is not None:
            earlier_candidates.append(
                {
                    "r": r,
                    "v239_r": exponent,
                    "denominator_exponent": r + exponent,
                }
            )
        exponent += 1

    W_N = max(
        [star_exponent]
        + [item["denominator_exponent"] for item in earlier_candidates]
    )
    dominant_terms = []
    residue = 0
    for item in earlier_candidates:
        if item["denominator_exponent"] != W_N:
            continue
        r = item["r"]
        unit = r // (P ** item["v239_r"])
        term_residue = (
            alternating_sign(r) * pow(unit % P, -1, P)
        ) % P
        residue = (residue + term_residue) % P
        dominant_terms.append(
            {
                "kind": "earlier_minus_g_r",
                **item,
                "residue_without_common_factor_4": term_residue,
            }
        )

    if star_exponent == W_N:
        N_plus_1_unit = (N + 1) // (P**a_N)
        D_unit = D // (P**d_N)
        term_residue = (
            alternating_sign(N)
            * (N_plus_1_unit % P)
            * pow(D_unit % P, -1, P)
        ) % P
        residue = (residue + term_residue) % P
        dominant_terms.append(
            {
                "kind": "combined_final_g_N",
                "denominator_exponent": star_exponent,
                "residue_without_common_factor_4": term_residue,
            }
        )

    return {
        "N": N,
        "a_v239_N_plus_1": a_N,
        "d_v239_D": d_N,
        "star_denominator_exponent": star_exponent,
        "W_N": W_N,
        "lower_bound_N_minus_floor_log239_N_plus_1": (
            N - floor_log_positive(N + 1, P)
        ),
        "dominant_terms": dominant_terms,
        "C_N_mod_239_without_common_factor_4": residue,
        "valuation_conclusion_available": residue != 0,
    }


def rational_sha256(value: sp.Rational) -> str:
    return hashlib.sha256(
        f"{int(value.p)}/{int(value.q)}".encode()
    ).hexdigest()


def closed_bc(N: int) -> list[sp.Rational]:
    if N < 1 or N % 2 == 0:
        raise ValueError("N must be positive and odd")
    g_N = f_coefficient("machin", N)
    X = sp.factorial(N) * g_N
    D = N * N + N - 1
    b_0 = X * (N + 1) * (X + N + 1)
    b_1 = -X * X * (N + 1) - X * (N + 2)
    c_0 = X * (N * N - 1) - 1
    c_1 = X * N + 1
    return [b_0, b_1, c_0, c_1]


def endpoint_ratio(N: int) -> sp.Rational:
    """Return A(1)/B(1) from the proved closed formula."""
    g_N = f_coefficient("machin", N)
    D = N * N + N - 1
    e_partial = sum(
        (sp.Rational(1, math.factorial(r)) for r in range(N + 2)),
        sp.Rational(0),
    )
    g_partial = sum(
        (f_coefficient("machin", r) for r in range(N + 2)),
        sp.Rational(0),
    )
    return (
        -e_partial
        - g_partial
        - g_N / D
        - sp.Rational(N + 2, D * math.factorial(N + 1))
    )


def small_crosscheck(N: int) -> dict:
    nullity, vector = primitive_solution(N - 1, 1, 1)
    if nullity != 1 or vector is None:
        raise RuntimeError(f"N={N}: expected a canonical line")
    bc = [sp.Rational(x) for x in vector[N:]]
    closed = closed_bc(N)
    scale = bc[0] / closed[0]
    if any(x != scale * y for x, y in zip(bc, closed)):
        raise RuntimeError(f"N={N}: closed B,C formula mismatch")
    raw_a = sum(vector[:N])
    raw_b = sum(vector[N : N + 2])
    ratio = endpoint_ratio(N)
    if sp.Rational(raw_a, raw_b) != ratio:
        raise RuntimeError(f"N={N}: endpoint-ratio formula mismatch")
    ratio_v = (
        valuation_positive(int(ratio.p), P)
        - valuation_positive(int(ratio.q), P)
    )
    leading = leading_residue_record(N)
    if leading["valuation_conclusion_available"]:
        if ratio_v != -leading["W_N"]:
            raise RuntimeError(f"N={N}: leading-residue theorem mismatch")
    return {
        "N": N,
        "degrees": [N - 1, 1, 1],
        "nullity": 1,
        "closed_BC_formula_verified": True,
        "endpoint_ratio_formula_verified": True,
        "endpoint_ratio_v239": ratio_v,
        "leading_residue_test": leading,
        "endpoint_ratio_sha256": rational_sha256(ratio),
    }


def N1_edge_record() -> dict:
    nullity, vector = primitive_solution(0, 1, 1)
    expected = [47123952, -47123952, 42578172, 1428025, -5973805]
    if nullity != 1 or vector != expected:
        raise RuntimeError("N=1 primitive polynomial vector mismatch")
    raw_a = vector[0]
    raw_b = vector[1] + vector[2]
    raw_c = vector[3] + vector[4]
    endpoint_gcd = math.gcd(abs(raw_a), abs(raw_b))
    alpha = raw_a // endpoint_gcd
    beta = raw_b // endpoint_gcd
    if raw_b != raw_c or (alpha, beta) != (12388, -1195):
        raise RuntimeError("N=1 endpoint normalization mismatch")
    ratio = sp.Rational(raw_a, raw_b)
    if ratio != sp.Rational(-12388, 1195):
        raise RuntimeError("N=1 endpoint ratio mismatch")
    return {
        "N": 1,
        "primitive_polynomial_vector_A_B0_B1_C0_C1": vector,
        "raw_endpoint_A": raw_a,
        "raw_endpoint_B_equals_C": raw_b,
        "endpoint_gcd": endpoint_gcd,
        "primitive_endpoint_pair_alpha_beta": [alpha, beta],
        "endpoint_ratio": "-12388/1195",
        "endpoint_ratio_v239": -1,
        "primitive_beta_v239": valuation_positive(beta, P),
    }


def exact_leading_residue_crosscheck(N: int) -> dict:
    """Compare Proposition 6.1 with the exact closed endpoint ratio."""
    ratio = endpoint_ratio(N)
    exact_v = (
        valuation_positive(int(ratio.p), P)
        - valuation_positive(int(ratio.q), P)
    )
    leading = leading_residue_record(N)
    if not leading["valuation_conclusion_available"]:
        raise RuntimeError(f"N={N}: selected cross-check is exceptional")
    if exact_v != -leading["W_N"]:
        raise RuntimeError(f"N={N}: exact leading-residue mismatch")
    return {
        "N": N,
        "reason_selected": {
            15: "D is divisible by 239",
            239: "N is divisible by 239",
            477: "N+1 is divisible by 239",
        }[N],
        "exact_endpoint_ratio_v239": exact_v,
        "endpoint_ratio_sha256": rational_sha256(ratio),
        "leading_residue_test": leading,
    }


def exceptional_leading_residue_record() -> dict:
    u = 161
    r = P * P * u
    N = r + 2
    record = leading_residue_record(N)
    residues = [
        item["residue_without_common_factor_4"]
        for item in record["dominant_terms"]
    ]
    if N != 9196483 or r != 9196481 or N >= P**3:
        raise RuntimeError("exceptional example arithmetic mismatch")
    if record["W_N"] != N or record["star_denominator_exponent"] != N:
        raise RuntimeError("exceptional example exponent mismatch")
    if residues != [144, 95] or record[
        "C_N_mod_239_without_common_factor_4"
    ] != 0:
        raise RuntimeError("exceptional leading-residue cancellation failed")
    return {
        "scope_warning": (
            "This certifies cancellation of the first 239-adic residue only; "
            "it does not determine the exact endpoint valuation at this N."
        ),
        "construction": "N=239^2*161+2",
        "r_equals_N_minus_2": r,
        "u_inverse_mod_239": pow(u, -1, P),
        "N_plus_1_over_D_mod_239": (
            ((N + 1) % P) * pow((N * N + N - 1) % P, -1, P)
        ) % P,
        "leading_residue_record": record,
    }


def p_adic_record(N: int) -> dict:
    ratio = endpoint_ratio(N)
    numerator_v = valuation_int(int(ratio.p), P)
    denominator_v = valuation_int(int(ratio.q), P)
    value_v = numerator_v - denominator_v
    if value_v != -N or numerator_v != 0 or denominator_v != N:
        raise RuntimeError(f"N={N}: predicted 239-adic valuation failed")
    leading = leading_residue_record(N)
    if (
        not leading["valuation_conclusion_available"]
        or leading["W_N"] != N
    ):
        raise RuntimeError(f"N={N}: leading-residue certificate mismatch")
    return {
        "N": N,
        "degrees": [N - 1, 1, 1],
        "N_representation": "1+2*239" if N == 479 else None,
        "endpoint_ratio_numerator_decimal_digits": len(str(abs(int(ratio.p)))),
        "endpoint_ratio_denominator_decimal_digits": len(str(int(ratio.q))),
        "endpoint_ratio_v239": value_v,
        "primitive_endpoint_A_v239": numerator_v,
        "primitive_endpoint_B_v239": denominator_v,
        "leading_residue_test": leading,
        "endpoint_ratio_sha256": rational_sha256(ratio),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--small-max-N", type=int, default=13)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.small_max_N < 1:
        raise ValueError("small-max-N must be positive")
    result = {
        "ray": "(a,b,c)=(N-1,1,1), N odd",
        "finite_scope_warning": (
            "The small cross-checks and N=479 calculation verify instances; "
            "the all-degree closed formulas and divergent-subsequence claim "
            "depend on the proof in the accompanying source note."
        ),
        "small_crosschecks": [
            small_crosscheck(N)
            for N in range(1, args.small_max_N + 1, 2)
        ],
        "N_equals_1_edge_normalization": N1_edge_record(),
        "targeted_exact_leading_residue_crosschecks": [
            exact_leading_residue_crosscheck(N) for N in (15, 239, 477)
        ],
        "first_nontrivial_divergence_subsequence_check": p_adic_record(479),
        "leading_residue_exception_certificate": (
            exceptional_leading_residue_record()
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
