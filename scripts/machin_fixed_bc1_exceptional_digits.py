#!/usr/bin/env python3
"""Exact 239-adic follow-up for the exceptional fixed-(b,c) endpoint ray.

This script supplements Proposition 6.1 of
``sources/machin_endpoint_asymptotics.md``.  It never constructs the
astronomically large endpoint rational number.  Instead it works with the
exact p-singular part of equation (67), modulo a requested power of p, and
with rigorous lower bounds for the valuation of every omitted regular term.

The default run also exhausts every positive odd N < 239^3.  Use
``--skip-exhaustive`` for the much faster certificate-only run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


P = 239


def valuation_positive(value: int, prime: int = P) -> int:
    if value == 0:
        raise ValueError("valuation of zero is undefined")
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def alternating_sign(index: int) -> int:
    """Return (-1)^((index-1)/2) for a positive odd index."""
    if index < 1 or index % 2 == 0:
        raise ValueError("index must be positive and odd")
    return 1 if ((index - 1) // 2) % 2 == 0 else -1


def floor_log_positive(value: int, base: int = P) -> int:
    if value < 1:
        raise ValueError("value must be positive")
    answer = 0
    power = base
    while power <= value:
        answer += 1
        power *= base
    return answer


def factorial_valuation(n: int, prime: int = P) -> int:
    """Legendre's exact valuation v_prime(n!)."""
    answer = 0
    while n:
        n //= prime
        answer += n
    return answer


def largest_odd_exact_valuation_below(
    N: int, exponent: int, prime: int = P
) -> int | None:
    """Largest positive odd r<N having v_prime(r)=exponent."""
    base = prime**exponent
    quotient = (N - 1) // base
    if quotient % 2 == 0:
        quotient -= 1
    while quotient > 0 and quotient % prime == 0:
        quotient -= 2
    if quotient <= 0:
        return None
    r = base * quotient
    if r >= N or r % 2 == 0 or valuation_positive(r, prime) != exponent:
        raise RuntimeError("internal largest-candidate error")
    return r


def leading_data(N: int, prime: int = P) -> dict:
    """Return W_N and the exact leading residue C_N from (73)--(75)."""
    if N < 1 or N % 2 == 0:
        raise ValueError("N must be positive and odd")
    D = N * N + N - 1
    a = valuation_positive(N + 1, prime)
    d = valuation_positive(D, prime)
    star_exponent = N - a + d

    candidates: list[tuple[int, int, int]] = []
    exponent = 0
    while prime**exponent < N:
        r = largest_odd_exact_valuation_below(N, exponent, prime)
        if r is not None:
            candidates.append((r + exponent, r, exponent))
        exponent += 1
    W = max([star_exponent] + [item[0] for item in candidates])

    residue = 0
    dominant_terms = []
    for denominator_exponent, r, exponent in candidates:
        if denominator_exponent != W:
            continue
        unit = r // prime**exponent
        term = alternating_sign(r) * pow(unit % prime, -1, prime) % prime
        residue = (residue + term) % prime
        dominant_terms.append(
            {
                "kind": "earlier_p_singular_term",
                "r": r,
                "v239_r": exponent,
                "denominator_exponent": denominator_exponent,
                "residue_without_common_factor_4": term,
            }
        )

    if star_exponent == W:
        U = (N + 1) // prime**a
        V = D // prime**d
        term = alternating_sign(N) * (U % prime) * pow(V % prime, -1, prime)
        term %= prime
        residue = (residue + term) % prime
        dominant_terms.append(
            {
                "kind": "combined_final_p_singular_term",
                "denominator_exponent": star_exponent,
                "residue_without_common_factor_4": term,
            }
        )

    return {
        "N": N,
        "D": D,
        "a_v239_N_plus_1": a,
        "d_v239_D": d,
        "star_denominator_exponent": star_exponent,
        "W_N": W,
        "dominant_terms": dominant_terms,
        "C_N_mod_239_without_common_factor_4": residue,
    }


def normalized_singular_mod(N: int, W: int, precision: int, prime: int = P) -> dict:
    r"""Compute p^W h_N modulo p^precision, where

        h_N = sum_{odd r<N} s_r/(r p^r) + s_N(N+1)/(D p^N).

    Terms whose scaled valuation is at least ``precision`` vanish modulo the
    modulus.  The lower cutoff below is rigorous because v_p(r) <=
    floor(log_p(N-1)).
    """
    if precision < 1:
        raise ValueError("precision must be positive")
    modulus = prime**precision
    D = N * N + N - 1
    a = valuation_positive(N + 1, prime)
    d = valuation_positive(D, prime)
    star_exponent = N - a + d
    max_earlier_exponent = floor_log_positive(N - 1, prime) if N > 1 else 0
    start = max(1, W - precision + 1 - max_earlier_exponent)
    if start % 2 == 0:
        start += 1

    residue = 0
    included_terms = []
    for r in range(start, N, 2):
        exponent = valuation_positive(r, prime)
        gap = W - r - exponent
        if gap < 0:
            raise RuntimeError("W failed to dominate an earlier term")
        if gap >= precision:
            continue
        unit = r // prime**exponent
        term = (
            alternating_sign(r)
            * prime**gap
            * pow(unit % modulus, -1, modulus)
        ) % modulus
        residue = (residue + term) % modulus
        included_terms.append(
            {
                "kind": "earlier_p_singular_term",
                "r": r,
                "v239_r": exponent,
                "gap_from_W": gap,
                "residue_mod_239_power_without_common_factor_4": term,
            }
        )

    star_gap = W - star_exponent
    if star_gap < 0:
        raise RuntimeError("W failed to dominate the combined final term")
    if star_gap < precision:
        U = (N + 1) // prime**a
        V = D // prime**d
        term = (
            alternating_sign(N)
            * prime**star_gap
            * (U % modulus)
            * pow(V % modulus, -1, modulus)
        ) % modulus
        residue = (residue + term) % modulus
        included_terms.append(
            {
                "kind": "combined_final_p_singular_term",
                "gap_from_W": star_gap,
                "residue_mod_239_power_without_common_factor_4": term,
            }
        )

    valuation_if_detected = None
    first_unit_if_detected = None
    if residue:
        valuation_if_detected = valuation_positive(residue, prime)
        first_unit_if_detected = (
            residue // prime**valuation_if_detected
        ) % prime
    return {
        "precision": precision,
        "modulus": modulus,
        "normalized_singular_without_common_factor_4_modulus": residue,
        "normalized_full_p_singular_with_factor_4_modulus": (4 * residue) % modulus,
        "valuation_if_less_than_precision": valuation_if_detected,
        "first_unit_without_factor_4_mod_239_if_detected": first_unit_if_detected,
        "first_unit_with_factor_4_mod_239_if_detected": (
            None if first_unit_if_detected is None else 4 * first_unit_if_detected % prime
        ),
        "included_terms": included_terms,
    }


def regular_gap_data(N: int, W: int, prime: int = P) -> dict:
    """Lower bounds after scaling every non-p-singular term by p^W."""
    D = N * N + N - 1
    a = valuation_positive(N + 1, prime)
    d = valuation_positive(D, prime)
    L = floor_log_positive(N, prime)
    F = factorial_valuation(N + 1, prime)
    v_N_plus_2 = valuation_positive(N + 2, prime)
    gaps = {
        "earlier_5_power_arctan_terms": W - L,
        "combined_final_5_power_arctan_term": W + a - d,
        "exponential_partial_sum": W - F,
        "last_D_factorial_term": W - F - d + v_N_plus_2,
    }
    return {
        "floor_log239_N": L,
        "v239_factorial_N_plus_1": F,
        "v239_N_plus_2": v_N_plus_2,
        "individual_scaled_valuation_lower_bounds": gaps,
        "Gamma_N_minimum_regular_gap": min(gaps.values()),
    }


def exceptional_certificate(N: int, precision: int = 3, prime: int = P) -> dict:
    lead = leading_data(N, prime)
    W = lead["W_N"]
    singular = normalized_singular_mod(N, W, precision, prime)
    regular = regular_gap_data(N, W, prime)
    t = singular["valuation_if_less_than_precision"]
    gamma = regular["Gamma_N_minimum_regular_gap"]
    exact_conclusion = None
    if t is not None and t < gamma:
        endpoint_v = -W + t
        exact_conclusion = {
            "hypothesis_t_less_than_Gamma_verified": True,
            "endpoint_ratio_v239": endpoint_v,
            "primitive_endpoint_beta_v239": max(0, -endpoint_v),
        }
    return {
        "leading_data": lead,
        "normalized_singular_calculation": singular,
        "regular_term_separation": regular,
        "exact_valuation_conclusion": exact_conclusion,
    }


def fast_leading_residue_below_p_cubed(N: int, prime: int = P) -> tuple:
    """Specialized exact leading calculation for 1 <= N < p^3."""
    D = N * N + N - 1
    if (N + 1) % (prime * prime) == 0:
        a = 2
    elif (N + 1) % prime == 0:
        a = 1
    else:
        a = 0
    d = 0
    D_unit = D
    while D_unit % prime == 0:
        d += 1
        D_unit //= prime
    star_exponent = N - a + d

    candidates = []
    for exponent in range(3):
        r = largest_odd_exact_valuation_below(N, exponent, prime)
        if r is not None:
            candidates.append((r + exponent, r, exponent))
    W = max([star_exponent] + [item[0] for item in candidates])
    residue = 0
    kinds = []
    for denominator_exponent, r, exponent in candidates:
        if denominator_exponent == W:
            unit = r // prime**exponent
            residue += alternating_sign(r) * pow(unit % prime, -1, prime)
            kinds.append(f"r_exact_v{exponent}")
    if star_exponent == W:
        U = (N + 1) // prime**a
        residue += alternating_sign(N) * (U % prime) * pow(
            D_unit % prime, -1, prime
        )
        kinds.append("star")
    return W, residue % prime, tuple(sorted(kinds))


def exhaustive_below_p_cubed(prime: int = P) -> dict:
    upper = prime**3
    odd_count = (upper - 1) // 2
    tie_shape_counts: dict[str, int] = {}
    exceptional = []
    tie_count = 0
    for N in range(1, upper, 2):
        W, residue, kinds = fast_leading_residue_below_p_cubed(N, prime)
        if len(kinds) > 1:
            tie_count += 1
            key = "+".join(kinds)
            tie_shape_counts[key] = tie_shape_counts.get(key, 0) + 1
        if residue == 0:
            exceptional.append({"N": N, "W_N": W, "dominant_kinds": list(kinds)})
    expected = [prime * prime * 80 - 1, prime * prime * 161 + 2]
    if [item["N"] for item in exceptional] != expected:
        raise RuntimeError("unexpected exhaustive exceptional set below p^3")
    return {
        "range": f"positive odd N < {prime}^3",
        "exclusive_upper_bound": upper,
        "odd_indices_tested": odd_count,
        "leading_ties": tie_count,
        "tie_shape_counts": tie_shape_counts,
        "C_N_zero_count": len(exceptional),
        "C_N_zero_records": exceptional,
    }


def D_value(N: int) -> int:
    return N * N + N - 1


def H_value(N: int, prime: int = P) -> Fraction:
    numerator = prime * prime * D_value(N + 2) + N * (N + 3) * D_value(N)
    denominator = N * D_value(N) * D_value(N + 2)
    return Fraction(numerator, denominator)


def F_value(N: int, prime: int = P) -> Fraction:
    """Exact small-N value of F_N used only for recurrence checks."""
    S = sum(
        (
            Fraction(alternating_sign(r) * prime ** (N - r), r)
            for r in range(1, N, 2)
        ),
        Fraction(0),
    )
    return S + Fraction(alternating_sign(N) * (N + 1), D_value(N))


def recurrence_certificate(prime: int = P) -> dict:
    checked = []
    for N in range(1, 42, 2):
        left = F_value(N + 2, prime)
        right = prime * prime * F_value(N, prime) - alternating_sign(N) * H_value(
            N, prime
        )
        if left != right:
            raise RuntimeError(f"recurrence failed at N={N}")
        checked.append(N)
    # P_N is the positive numerator of H_N in expanded form.
    return {
        "identity": "F_(N+2) = 239^2 F_N - s_N H_N",
        "H_N": (
            "[239^2 D_(N+2) + N(N+3)D_N] / "
            "[N D_N D_(N+2)]"
        ),
        "expanded_positive_numerator_P_N": (
            "N^4+4N^3+(239^2+2)N^2+(5*239^2-3)N+5*239^2"
        ),
        "exact_fraction_checks_at_odd_N": checked,
        "checks_passed": True,
    }


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/machin_fixed_bc1_exceptional_digits.json"),
    )
    parser.add_argument("--skip-exhaustive", action="store_true")
    args = parser.parse_args()

    N_low = P * P * 80 - 1
    N_high = P * P * 161 + 2
    N_e4 = P**4 * 283 + 4
    records = {
        "prime": P,
        "normalization": (
            "The modular singular sum suppresses the common p-adic unit 4, "
            "exactly as C_N in equation (75)."
        ),
        "next_digit_certificates": {
            "N_equals_p2_times_80_minus_1": exceptional_certificate(N_low, 2),
            "N_equals_p2_times_161_plus_2": exceptional_certificate(N_high, 2),
            "N_equals_p4_times_283_plus_4": exceptional_certificate(N_e4, 2),
        },
        "third_certificate_construction": {
            "N": N_e4,
            "representation": "239^4*283+4",
            "283_mod_239": 283 % P,
            "cancellation_congruence": "283 == -19/5 (mod 239)",
        },
        "recurrence_certificate": recurrence_certificate(),
        "exhaustive_scan_below_p_cubed": (
            None if args.skip_exhaustive else exhaustive_below_p_cubed()
        ),
        "scope_warning": (
            "Finite scans certify only their stated ranges.  The recurrence "
            "gives an adjacent-pair O(log N) result, not the unresolved "
            "pointwise bound at every exceptional index."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(records, indent=2, sort_keys=True) + "\n"
    args.output.write_text(rendered, encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "output_sha256": sha256_file(args.output),
        "exceptional_N": [N_low, N_high, N_e4],
        "exhaustive_scan_run": not args.skip_exhaustive,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
