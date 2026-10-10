#!/usr/bin/env python3
"""Exact diagnostics for the p-adic parameter-hypergeometric Bessel zero.

This is a finite certificate for the identities and inequalities proved in
``sources/bessel_padic_hypergeometric_zero_pade_barrier.md``.  The source,
not this finite computation, contains the all-prime and all-index proofs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def valuation_nonzero(value: int, prime: int) -> int:
    """Return v_prime(value), requiring value to be nonzero."""
    if value == 0:
        raise ValueError("valuation_nonzero requires a nonzero integer")
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def factorial_valuation(index: int, prime: int) -> int:
    """Return v_prime(index!) by Legendre's formula."""
    answer = 0
    while index:
        index //= prime
        answer += index
    return answer


def floor_log(index: int, prime: int) -> int:
    """Return floor(log_prime(index)) for positive index."""
    if index <= 0:
        raise ValueError("floor_log requires a positive integer")
    answer = 0
    while index >= prime:
        index //= prime
        answer += 1
    return answer


def lambda_value(index: int, prime: int) -> int:
    """Return Lambda_prime(index)=v((2 index)!)-v(index!)."""
    return factorial_valuation(2 * index, prime) - factorial_valuation(
        index, prime
    )


def q_values(limit: int, modulus: int | None = None) -> list[int]:
    """Return q_0,...,q_limit for q_0=q_1=1."""
    if limit == 0:
        return [1]
    values = [1, 1]
    for index in range(2, limit + 1):
        value = (4 * index - 2) * values[-1] + values[-2]
        if modulus is not None:
            value %= modulus
        values.append(value)
    if modulus is not None:
        values[0] %= modulus
        values[1] %= modulus
    return values


def q_at_index(index: int, modulus: int) -> int:
    """Evaluate q_index modulo modulus without constructing huge integers."""
    if index <= 1:
        return 1 % modulus
    previous, current = 1 % modulus, 1 % modulus
    for step in range(2, index + 1):
        previous, current = (
            current,
            ((4 * step - 2) * current + previous) % modulus,
        )
    return current


def terms_at_integer(value: int, limit: int) -> list[int]:
    """Return T_k(value)=(-value)_k(value+1)_k/k! exactly."""
    terms = [1]
    term = 1
    for index in range(limit):
        numerator = -(value - index) * (value + index + 1)
        product = term * numerator
        denominator = index + 1
        assert product % denominator == 0
        term = product // denominator
        terms.append(term)
    return terms


def direct_term(value: int, index: int) -> int:
    """Evaluate T_index(value) from its consecutive-factor product."""
    numerator = (-1) ** index
    for shift in range(-index + 1, index + 1):
        numerator *= value + shift
    denominator = math.factorial(index)
    assert numerator % denominator == 0
    return numerator // denominator


def terminating_identity_checks() -> dict[str, object]:
    """Check H_n(n)=(-1)^n q_n and the quadratic Newton form."""
    limit = 90
    q_exact = q_values(limit)
    samples = []
    for n in range(limit + 1):
        terms = terms_at_integer(n, n + 10)
        partial = sum(terms[: n + 1])
        assert partial == (-1) ** n * q_exact[n]
        assert all(term == 0 for term in terms[n + 1 :])
        for k in range(n, n + 11):
            assert sum(terms[: k + 1]) == partial
        quadratic_parameter = n * (n + 1)
        newton_product = 1
        for k in range(n + 1):
            if k:
                j = k - 1
                newton_product *= quadratic_parameter - j * (j + 1)
            quadratic_term = (-1) ** k * newton_product // math.factorial(k)
            assert quadratic_term == terms[k]
        if n in {0, 1, 2, 3, 5, 10, 20, 40, 90}:
            samples.append(
                {
                    "n": n,
                    "signed_q": partial,
                    "decimal_digits_abs_q": len(str(abs(partial))),
                    "first_zero_term": n + 1,
                }
            )
    return {
        "checked_n_through": limit,
        "identity_checks": limit + 1,
        "quadratic_newton_checks": sum(range(1, limit + 2)),
        "samples": samples,
    }


def uniform_valuation_checks() -> list[dict[str, object]]:
    """Check v_p(T_k(x)) >= Lambda_p(k) on finite residue systems."""
    records = []
    for prime, exponent, limit in [
        (2, 6, 70),
        (3, 5, 70),
        (5, 4, 70),
        (7, 3, 70),
        (11, 3, 60),
        (13, 3, 60),
    ]:
        modulus = prime**exponent
        minimum_gap: int | None = None
        nonzero_checks = 0
        zero_terms = 0
        half_depth_checks = 0
        for k in range(limit + 1):
            lower_bound = lambda_value(k, prime)
            depth_visibility_cap = factorial_valuation(
                k, prime
            ) + lambda_value(k + 1, prime)
            assert depth_visibility_cap == factorial_valuation(
                2 * k + 2, prime
            ) - valuation_nonzero(k + 1, prime)
            assert (prime - 1) * depth_visibility_cap <= 2 * k + 2
            factorial_loss = factorial_valuation(k, prime)
            lambda_next = lambda_value(k + 1, prime)
            imbalance = lambda_next - factorial_loss
            assert imbalance == valuation_nonzero(
                (k + 1) * math.comb(2 * k + 2, k + 1), prime
            )
            assert imbalance >= 0
            assert imbalance <= 1 + 2 * floor_log(k + 1, prime)
            for depth in range(0, 3 * limit + 1):
                certified = min(lambda_next, depth - factorial_loss)
                assert 2 * certified <= depth + imbalance
                half_depth_checks += 1
            if k < limit:
                increment = lambda_value(k + 1, prime) - lower_bound
                assert increment == valuation_nonzero(2 * (2 * k + 1), prime)
                assert increment >= 0
            for residue in range(modulus):
                term = direct_term(residue, k)
                if term == 0:
                    zero_terms += 1
                    continue
                gap = valuation_nonzero(term, prime) - lower_bound
                assert gap >= 0
                minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
                nonzero_checks += 1
        assert minimum_gap == 0
        records.append(
            {
                "prime": prime,
                "residue_exponent": exponent,
                "residue_count": modulus,
                "terms_checked_through": limit,
                "nonzero_valuation_checks": nonzero_checks,
                "zero_terms_skipped": zero_terms,
                "minimum_valuation_gap": minimum_gap,
                "last_lambda": lambda_value(limit, prime),
                "exact_depth_visibility_cap_checks": limit + 1,
                "half_depth_ceiling_checks": half_depth_checks,
            }
        )
    return records


def dominance_checks() -> dict[str, object]:
    """Check term growth, sign, nonvanishing, and the height bound."""
    checked_partial_sums = 0
    checked_ratios = 0
    samples = []
    for n in range(1, 81):
        terms = terms_at_integer(n, n)
        running = 0
        for k, term in enumerate(terms):
            running += term
            assert running != 0
            assert (1 if running > 0 else -1) == (-1) ** k
            assert abs(running) < 2 * abs(term)
            assert abs(term) <= (n + k) ** (2 * k)
            assert abs(running) < 2 * (n + k) ** (2 * k)
            checked_partial_sums += 1
            if k < n:
                ratio_numerator = (n - k) * (n + k + 1)
                ratio_denominator = k + 1
                assert ratio_numerator >= 2 * ratio_denominator
                assert abs(terms[k + 1]) * ratio_denominator == (
                    abs(term) * ratio_numerator
                )
                checked_ratios += 1
        if n in {1, 2, 5, 10, 20, 40, 80}:
            samples.append(
                {
                    "n": n,
                    "H_floor_n_over_2": sum(terms[: n // 2 + 1]),
                    "H_n_decimal_digits": len(str(abs(sum(terms)))),
                }
            )
    return {
        "n_checked_through": 80,
        "partial_sum_checks": checked_partial_sums,
        "successive_ratio_checks": checked_ratios,
        "samples": samples,
    }


def polynomial_difference_checks() -> list[dict[str, int]]:
    """Check v_p(T_k(x)-T_k(y)) >= v_p(x-y)-v_p(k!)."""
    records = []
    for prime in [2, 3, 5, 7, 11, 13]:
        checks = 0
        sharp = 0
        for exponent in range(1, 6):
            displacement = prime**exponent
            for base in range(-13, 18):
                for multiplier in [1, 2, prime + 1]:
                    other = base + multiplier * displacement
                    actual_distance = valuation_nonzero(other - base, prime)
                    for k in range(0, 24):
                        difference = direct_term(other, k) - direct_term(base, k)
                        lower_bound = actual_distance - factorial_valuation(k, prime)
                        if difference:
                            actual = valuation_nonzero(difference, prime)
                            assert actual >= lower_bound
                            if actual == lower_bound:
                                sharp += 1
                        checks += 1
        records.append(
            {
                "prime": prime,
                "checks": checks,
                "equalities": sharp,
            }
        )
    return records


def branch_auxiliary_checks() -> list[dict[str, object]]:
    """Check the natural auxiliary inequality at deep ordinary representatives."""
    branch_data = [
        (7, 576601, 7),
        (11, 1289767, 6),
        (13, 206864, 5),
        (41, 2644525, 4),
    ]
    records = []
    for prime, n, expected_minimum in branch_data:
        modulus = prime ** (expected_minimum + 8)
        residue = q_at_index(n, modulus)
        assert residue != 0
        valuation = valuation_nonzero(residue, prime)
        assert valuation >= expected_minimum
        k_values = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        terms = terms_at_integer(n, max(k_values))
        cases = []
        for k in k_values:
            auxiliary = sum(terms[: k + 1])
            assert auxiliary != 0
            auxiliary_valuation = valuation_nonzero(auxiliary, prime)
            lower_bound = min(
                lambda_value(k + 1, prime),
                valuation - factorial_valuation(k, prime),
            )
            assert auxiliary_valuation >= lower_bound
            assert abs(auxiliary) < 2 * (n + k) ** (2 * k)
            if lower_bound >= 0:
                assert prime**lower_bound <= abs(auxiliary)
            cases.append(
                {
                    "K": k,
                    "lambda_K_plus_1": lambda_value(k + 1, prime),
                    "v_K_factorial": factorial_valuation(k, prime),
                    "claimed_lower_bound": lower_bound,
                    "actual_v_H_K_n": auxiliary_valuation,
                    "decimal_digits_abs_H_K_n": len(str(abs(auxiliary))),
                }
            )
        records.append(
            {
                "prime": prime,
                "n": n,
                "v_q_n": valuation,
                "q_mod_p_power_exponent": expected_minimum + 8,
                "cases": cases,
            }
        )
    return records


def visibility_checks() -> dict[str, object]:
    """Check that the offset -n first belongs to [-k+1,k] at k=n+1."""
    checks = 0
    for n in range(0, 501):
        containing = [
            k
            for k in range(0, n + 4)
            if -k + 1 <= -n <= k
        ]
        assert containing
        assert containing[0] == n + 1
        checks += 1
    return {
        "n_checked_through": 500,
        "checks": checks,
        "first_visible_term_formula": "k=n+1",
    }


def build_payload() -> dict[str, object]:
    return {
        "description": (
            "Exact finite diagnostics for the p-adic _2F_0 parameter "
            "representation and its raw-truncation height barrier"
        ),
        "terminating_and_quadratic_newton": terminating_identity_checks(),
        "uniform_term_valuation": uniform_valuation_checks(),
        "dominance_and_height": dominance_checks(),
        "polynomial_difference": polynomial_difference_checks(),
        "ordinary_branch_auxiliaries": branch_auxiliary_checks(),
        "visibility_threshold": visibility_checks(),
        "status": (
            "finite diagnostic; the uniform convergence and inequalities are "
            "proved in the companion source; no uniform digit-depth bound is "
            "claimed"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    default_output = Path(__file__).resolve().parents[1] / "results" / (
        "bessel_padic_hypergeometric_zero_pade_certificate.json"
    )
    parser.add_argument("--output", type=Path, default=default_output)
    arguments = parser.parse_args()
    payload = build_payload()
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_bytes(encoded)
    print(f"wrote {arguments.output}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")


if __name__ == "__main__":
    main()
