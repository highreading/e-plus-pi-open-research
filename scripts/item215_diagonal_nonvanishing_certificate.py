#!/usr/bin/env python3
"""Deterministic certificate for Item 215's diagonal nonvanishing branch.

The proof-bearing assertions are elementary identities recorded in the JSON:

* an exact 2-adic expansion of ell_j and its unique-minimum criterion;
* the mod-4/Kummer carry-one theorem;
* an algebraic ordinary generating function checked as a formal series; and
* the no-three-consecutive-zeros capacity bound from the proved Item 210
  recurrence.

Finite scans are explicitly labelled FINITE and are not promoted to all-j
claims.  The script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(1_000_000)


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item215_diagonal_nonvanishing_certificate.json"
    if (HERE / "item215_diagonal_nonvanishing_certificate.py").exists()
    else HERE.parent / "results" / "item215_diagonal_nonvanishing_certificate.json"
)


P_COEFFICIENTS = (
    (-11753280, -46086408, -75353094, -66698343, -34568046, -10504404, -1735020, -120285),
    (1621956672, 5897336856, 9019719984, 7528419750, 3706107054, 1076695974, 171005850, 11458260),
    (-52220160, -183220704, -269869776, -216686448, -102607824, -28701648, -4397760, -285120),
    (17579520, 61204608, 89232320, 70702080, 32916800, 9013632, 1345280, 84480),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def polynomial_value(coefficients: tuple[int, ...], value: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = answer * value + coefficient
    return answer


def recurrence_coefficients(n_value: int) -> tuple[int, int, int, int]:
    return tuple(polynomial_value(coefficients, n_value) for coefficients in P_COEFFICIENTS)


def ell_direct(j_value: int) -> int:
    return sum(
        (-1) ** (j_value + 1 + t_value)
        * math.comb(3 * j_value + 2, 2 * j_value + 1 - 2 * t_value)
        * math.comb(2 * j_value + 1 + t_value, t_value)
        for t_value in range(j_value + 1)
    )


def ell_two_adic_expansion(j_value: int) -> int:
    n_value = 2 * j_value + 1
    return (-1) ** j_value * sum(
        (-1) ** k_value
        * (1 << k_value)
        * math.comb(2 * j_value + 1 + k_value, k_value)
        * math.comb(3 * j_value + 2 + k_value, n_value - k_value)
        for k_value in range(n_value + 1)
    )


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0) is infinite")
    absolute = abs(value)
    return (absolute & -absolute).bit_length() - 1


def v2_binomial(n_value: int, k_value: int) -> int:
    if not 0 <= k_value <= n_value:
        raise ValueError((n_value, k_value))
    return k_value.bit_count() + (n_value - k_value).bit_count() - n_value.bit_count()


def term_valuation(j_value: int, k_value: int) -> int:
    return (
        k_value
        + v2_binomial(2 * j_value + 1 + k_value, k_value)
        + v2_binomial(3 * j_value + 2 + k_value, 2 * j_value + 1 - k_value)
    )


def minimum_profile(j_value: int) -> tuple[int, tuple[int, ...]]:
    # nu_j(k) >= k, so a minimizer cannot lie beyond nu_j(0).
    nu_zero = term_valuation(j_value, 0)
    values = [term_valuation(j_value, k_value) for k_value in range(nu_zero + 1)]
    minimum = min(values)
    minimizers = tuple(index for index, value in enumerate(values) if value == minimum)
    return minimum, minimizers


def sequence_scan(limit: int, direct_check: int) -> tuple[list[int], dict[str, Any]]:
    if limit < 3:
        raise ValueError("limit must be at least 3")
    values = [ell_direct(0), ell_direct(1), ell_direct(2), ell_direct(3)]
    digest = hashlib.sha256()
    for value in values[1:]:
        digest.update(f"{value}\n".encode("ascii"))
    zeros = []
    for n_value in range(1, limit - 2):
        p0, p1, p2, p3 = recurrence_coefficients(n_value)
        numerator = -(p0 * values[n_value] + p1 * values[n_value + 1] + p2 * values[n_value + 2])
        quotient, remainder = divmod(numerator, p3)
        if remainder:
            raise AssertionError((n_value, remainder))
        values.append(quotient)
        digest.update(f"{quotient}\n".encode("ascii"))
        if quotient == 0:
            zeros.append(n_value + 3)
    for j_value in range(min(limit, direct_check) + 1):
        direct = ell_direct(j_value)
        expanded = ell_two_adic_expansion(j_value)
        if values[j_value] != direct or direct != expanded:
            raise AssertionError((j_value, values[j_value], direct, expanded))
    return values, {
        "label": "FINITE",
        "range": [1, limit],
        "zeros": zeros,
        "direct_and_two_adic_expansion_cross_check_through": min(limit, direct_check),
        "sequence_sha256_newline_decimal": digest.hexdigest(),
        "last_decimal_digits": len(str(abs(values[limit]))),
        "last_mod_2^64": values[limit] % (1 << 64),
    }


def two_adic_audit(values: list[int], limit: int) -> dict[str, Any]:
    unique_count = 0
    collisions = []
    minimizer_histogram: Counter[str] = Counter()
    carry_one_count = 0
    maximum_v2 = -1
    maximum_v2_indices = []
    maximum_collision_uplift = -1
    maximum_collision_uplift_indices = []
    for j_value in range(1, limit + 1):
        minimum, minimizers = minimum_profile(j_value)
        actual_v2 = v2(values[j_value])
        if len(minimizers) == 1:
            unique_count += 1
            if actual_v2 != minimum:
                raise AssertionError((j_value, minimum, minimizers, actual_v2))
            minimizer_histogram[str(minimizers[0])] += 1
        else:
            uplift = actual_v2 - minimum
            if uplift < 0:
                raise AssertionError((j_value, minimum, minimizers, actual_v2))
            if len(collisions) < 20:
                collisions.append(
                    {
                        "j": j_value,
                        "minimum_term_valuation": minimum,
                        "minimizers": list(minimizers),
                        "actual_v2_ell": actual_v2,
                        "cancellation_uplift": uplift,
                    }
                )
            if uplift > maximum_collision_uplift:
                maximum_collision_uplift = uplift
                maximum_collision_uplift_indices = [j_value]
            elif uplift == maximum_collision_uplift:
                maximum_collision_uplift_indices.append(j_value)
        carry_count = v2_binomial(3 * j_value + 2, j_value + 1)
        if carry_count < 1:
            raise AssertionError((j_value, carry_count))
        if carry_count == 1:
            carry_one_count += 1
            if actual_v2 != 1:
                raise AssertionError((j_value, carry_count, actual_v2))
        if actual_v2 > maximum_v2:
            maximum_v2 = actual_v2
            maximum_v2_indices = [j_value]
        elif actual_v2 == maximum_v2:
            maximum_v2_indices.append(j_value)
    return {
        "label": "FINITE_PROFILE_SUPPORTING_AN_ALL_J_CRITERION",
        "range": [1, limit],
        "unique_minimum_count": unique_count,
        "tied_minimum_candidate_count": limit - unique_count,
        "unique_minimum_fraction": f"{unique_count}/{limit}",
        "unique_minimizer_histogram": dict(sorted(minimizer_histogram.items(), key=lambda pair: int(pair[0]))),
        "first_tied_minimum_records": collisions,
        "maximum_collision_uplift": maximum_collision_uplift,
        "maximum_collision_uplift_indices": maximum_collision_uplift_indices,
        "carry_one_count": carry_one_count,
        "maximum_v2_ell": maximum_v2,
        "maximum_v2_indices": maximum_v2_indices,
    }


def prime_cover_diagnostic(values: list[int], limit: int) -> dict[str, Any]:
    primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    common = list(range(1, limit + 1))
    counts = []
    for prime in primes:
        common = [index for index in common if values[index] % prime == 0]
        counts.append({"through_prime": prime, "common_divisibility_count": len(common)})
    return {
        "label": "FINITE_DIAGNOSTIC_ONLY",
        "range": [1, limit],
        "primes": list(primes),
        "successive_common_zero_counts": counts,
        "indices_divisible_by_every_listed_prime": common,
        "warning": "Different prime automata read different bases; this finite cover is not an all-j product-automaton proof.",
    }


def s_trim(series: list[int], order: int) -> list[int]:
    return (series + [0] * (order - len(series)))[:order]


def s_add(left: list[int], right: list[int], order: int) -> list[int]:
    return [(left[index] if index < len(left) else 0) + (right[index] if index < len(right) else 0) for index in range(order)]


def s_scale(series: list[int], scalar: int, order: int) -> list[int]:
    return [(series[index] if index < len(series) else 0) * scalar for index in range(order)]


def s_mul(left: list[int], right: list[int], order: int) -> list[int]:
    answer = [0] * order
    for left_index, left_value in enumerate(left[:order]):
        if not left_value:
            continue
        for right_index, right_value in enumerate(right[: order - left_index]):
            if right_value:
                answer[left_index + right_index] += left_value * right_value
    return answer


def s_pow(series: list[int], exponent: int, order: int) -> list[int]:
    answer = [1] + [0] * (order - 1)
    base = s_trim(series, order)
    while exponent:
        if exponent & 1:
            answer = s_mul(answer, base, order)
        exponent >>= 1
        if exponent:
            base = s_mul(base, base, order)
    return answer


def s_constant(value: int, order: int) -> list[int]:
    return [value] + [0] * (order - 1)


def s_shift(series: list[int], amount: int, order: int) -> list[int]:
    return [0] * amount + series[: max(0, order - amount)]


def algebraic_ogf_check(values: list[int], order: int) -> dict[str, Any]:
    # H'/H=A, A=sum ell_j z^j, H(0)=1.
    h_values = [1]
    for n_value in range(1, order):
        numerator = sum(values[k_value] * h_values[n_value - 1 - k_value] for k_value in range(n_value))
        quotient, remainder = divmod(numerator, n_value)
        if remainder:
            raise AssertionError((n_value, remainder))
        h_values.append(quotient)

    h = h_values
    h_minus_two = s_add(h, s_constant(-2, order), order)
    h_minus_one = s_add(h, s_constant(-1, order), order)
    h2 = s_pow(h, 2, order)
    h3 = s_pow(h, 3, order)
    h2_plus_four = s_add(h2, s_constant(4, order), order)
    h2_minus_2h_plus_2 = s_add(s_add(h2, s_scale(h, -2, order), order), s_constant(2, order), order)

    g0 = s_scale(
        s_mul(
            s_mul(s_pow(h_minus_two, 4, order), h_minus_one, order),
            s_mul(h2_plus_four, s_pow(h2_minus_2h_plus_2, 4, order), order),
            order,
        ),
        -1,
        order,
    )
    quintic = s_add(
        s_add(
            s_add(s_scale(s_pow(h, 5, order), 3, order), s_scale(s_pow(h, 4, order), -4, order), order),
            s_add(s_scale(h3, -24, order), s_scale(h2, 36, order), order),
            order,
        ),
        s_add(s_scale(h, 16, order), s_constant(-32, order), order),
        order,
    )
    g1_unshifted = s_scale(
        s_mul(
            s_mul(h2, s_pow(h_minus_two, 2, order), order),
            s_mul(s_pow(h2_minus_2h_plus_2, 2, order), quintic, order),
            order,
        ),
        2,
        order,
    )
    h3_minus_four = s_add(h3, s_constant(-4, order), order)
    g2_unshifted = s_mul(h3, s_pow(h3_minus_four, 3, order), order)
    defect = s_add(s_add(g0, s_shift(g1_unshifted, 1, order), order), s_shift(g2_unshifted, 2, order), order)
    nonzero_defect = [(index, value) for index, value in enumerate(defect) if value]
    if nonzero_defect:
        raise AssertionError(nonzero_defect[:5])
    return {
        "label": "EXACT_FORMAL_SERIES_REPLAY",
        "order_exclusive": order,
        "H_initial_coefficients": h_values[:16],
        "G_series_defect_nonzero_terms": 0,
        "G": (
            "-(H-2)^4(H-1)(H^2+4)(H^2-2H+2)^4"
            "+2zH^2(H-2)^2(H^2-2H+2)^2(3H^5-4H^4-24H^3+36H^2+16H-32)"
            "+z^2H^3(H^3-4)^3"
        ),
        "A_relation": "A(z)=sum_{j>=0}ell_j z^j=H'(z)/H(z), H(0)=1",
        "critical_value_polynomial": "729z^3-69444z^2+1728z-512",
    }


def decimal_text(value: Decimal, places: int = 32) -> str:
    return format(value, f".{places}f")


def capacity_bound(j_prefix: int) -> dict[str, Any]:
    getcontext().prec = 80
    a = Decimal(j_prefix + 1)

    def f(value: Decimal) -> Decimal:
        return Decimal(1) / (value * (value + 1))

    bound = (
        Decimal(2) / Decimal(3) * (f(a) + f(a + 1))
        + Decimal(2) / Decimal(9) * ((Decimal(1) + Decimal(1) / a).ln() + (Decimal(1) + Decimal(1) / (a + 1)).ln())
    )
    old_bound = Decimal(2) / (Decimal(3) * a)
    return {
        "label": "PROVED",
        "prefix_J": j_prefix,
        "weight": "w_j=2/((3j+2)(j+1))",
        "zero_spacing": "no three consecutive ell_j can vanish",
        "block_partition": "{J+1+3q,J+2+3q,J+3+3q}, q>=0",
        "symbolic_upper_bound": (
            "(2/3)(1/(a(a+1))+1/((a+1)(a+2)))"
            "+(2/9)(log(1+1/a)+log(1+1/(a+1))), a=J+1"
        ),
        "per_m_upper_bound_decimal": decimal_text(bound),
        "per_6m_upper_bound_decimal": decimal_text(bound / 6),
        "item210_full_tail_bound_decimal": decimal_text(old_bound),
        "ratio_to_item210_full_tail_bound": decimal_text(bound / old_bound),
        "required_gap_per_m": "0.1177979020165907632818384072",
        "required_G_per_6m": "0.0196329836694317938803064012",
    }


def certificate(limit: int, direct_check: int, ogf_order: int) -> dict[str, Any]:
    values, finite_scan = sequence_scan(limit, direct_check)
    checker_path = Path(__file__).resolve()
    return {
        "item": 215,
        "title": "2-adic candidate classification and algebraic structure of the diagonal anchor",
        "status": {
            "proved": [
                "exact 2-adic expansion and unique-minimum nonvanishing criterion for every j",
                "ell_j congruent to (-1)^j binomial(3j+2,j+1) modulo 4",
                "carry-one indices have exact v2(ell_j)=1 and are nonzero",
                "algebraic OGF A=H'/H with the displayed exact polynomial G(z,H)",
                "no-three-consecutive-zero spacing improves the unresolved rank-one ceiling",
            ],
            "experimental_finite": [
                f"no zero through j={limit}",
                "unique-minimum and mixed-prime diagnostics on the declared prefix",
            ],
            "open": [
                "all-j nonvanishing on the tied-minimum candidate class",
                "a uniform-in-modulus 2-adic automaton or a same-base congruence cover",
            ],
        },
        "source_sha256": sha256(checker_path),
        "definitions": {
            "ell_j": "[y^(2j+1)](y-1)^(3j+2)/(1+y^2)^(2j+2)",
            "two_adic_expansion": (
                "(-1)^j sum_{k=0}^{2j+1}(-1)^k 2^k "
                "C(2j+1+k,k)C(3j+2+k,2j+1-k)"
            ),
            "term_valuation": (
                "nu_j(k)=k+v2(C(2j+1+k,k))+v2(C(3j+2+k,2j+1-k))"
            ),
            "candidate_theorem": (
                "ell_j=0 implies the minimum of nu_j(k) is attained at least twice; "
                "a unique minimizer gives v2(ell_j)=min_k nu_j(k)"
            ),
            "mod4_theorem": "ell_j=(-1)^j C(3j+2,j+1) mod 4",
            "carry_count": "v2(C(N,K))=s_2(K)+s_2(N-K)-s_2(N)",
        },
        "experimental_finite_scan": finite_scan,
        "two_adic_profile": two_adic_audit(values, limit),
        "mixed_prime_diagnostic": prime_cover_diagnostic(values, limit),
        "algebraic_ogf": algebraic_ogf_check(values, ogf_order),
        "capacity": capacity_bound(limit),
        "verdict": (
            "No all-j nonvanishing proof is claimed. Exact zeros are confined to the tied-minimum "
            "2-adic class. Independently, the proved order-three recurrence forbids three consecutive "
            "zeros and lowers the worst-case unresolved rank-one ceiling, but the branch still cannot "
            "supply the Route-1 gap alone."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20_000)
    parser.add_argument("--direct-check", type=int, default=80)
    parser.add_argument("--ogf-order", type=int, default=96)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.limit, args.direct_check, args.ogf_order)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["status"], sort_keys=True))
    print(args.output)


if __name__ == "__main__":
    main()
