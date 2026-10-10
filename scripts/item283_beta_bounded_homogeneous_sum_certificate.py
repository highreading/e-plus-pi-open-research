#!/usr/bin/env python3
"""Deterministic certificate for Item 283's bounded homogeneous-sum theorem.

All rows use exact integer arithmetic.  The bounded replay illustrates and
checks identities only; it is not a prime census or asymptotic experiment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


def q_values(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def continuant(n: int, h: int) -> int:
    if h == 0:
        return 0
    previous, current = 0, 1
    for d in range(h - 1):
        previous, current = current, (4 * n + 4 * d + 6) * current + previous
    return current


def casoratian(q: list[int], n: int, h: int) -> int:
    return q[n] * q[n + h + 1] - q[n + 1] * q[n + h]


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("zero valuation excluded")
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def product(values: list[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def digest(rows: list[Any]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def moving_gap_sets(n: int) -> tuple[tuple[int, ...], ...]:
    """Three homogeneous degree-three monomials with moving bounded gaps."""
    return (
        (2 + n % 3, 4 + n % 2, 6 + n % 4),
        (3 + n % 2, 5 + n % 3, 7 + n % 2),
        (2 + n % 2, 6 + n % 3, 8 + n % 2),
    )


def coefficient_sets(n: int) -> tuple[tuple[int, ...], ...]:
    """Prime-independent integer-polynomial coefficient evaluations."""
    return (
        (1, 1, -1),
        (n + 1, -2, 1),
        (2 * n + 3, n - 1, -3),
        (n * n + 1, -(n + 2), 2),
        (3, -2 * n - 1, n + 4),
    )


def build_result() -> dict[str, Any]:
    q = q_values(100)
    check_primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    clearing_samples = (1, 3, 5, 7, 9, 11, 15, 25, 49, 77, 121)

    sum_rows: list[dict[str, Any]] = []
    valuation_rows: list[dict[str, Any]] = []
    cancellation_rows: list[dict[str, Any]] = []
    target_divisibility_rows: list[dict[str, Any]] = []
    for n in range(1, 41):
        gap_sets = moving_gap_sets(n)
        degree = len(gap_sets[0])
        assert all(len(gaps) == degree for gaps in gap_sets)
        residual_monomials: list[int] = []
        scalar_monomials: list[int] = []
        gap_budgets: list[int] = []
        for gaps in gap_sets:
            residual = product([continuant(n, h) for h in gaps])
            scalar = product([casoratian(q, n, h) for h in gaps])
            budget = sum(h - 1 for h in gaps)
            lower = (4 * n + 6) ** budget
            upper = (4 * (n + budget + 1)) ** budget
            assert lower <= residual <= upper
            residual_monomials.append(residual)
            scalar_monomials.append(scalar)
            gap_budgets.append(budget)

        common_boundary_unit = (-q[n + 1] ** 2) ** degree
        for coefficients in coefficient_sets(n):
            terms = [
                coefficient * monomial
                for coefficient, monomial in zip(coefficients, residual_monomials)
                if coefficient
            ]
            scalar_terms = [
                coefficient * monomial
                for coefficient, monomial in zip(coefficients, scalar_monomials)
                if coefficient
            ]
            residual_sum = sum(terms)
            scalar_sum = sum(scalar_terms)
            if residual_sum == 0 or scalar_sum == 0:
                continue
            common_term = 0
            for term in terms:
                common_term = math.gcd(common_term, abs(term))
            assert common_term > 0
            normalized_residual = residual_sum // common_term
            assert residual_sum % common_term == 0
            l1_height_integer = sum(abs(term) for term in terms)
            normalized_l1_integer = l1_height_integer // common_term
            assert l1_height_integer % common_term == 0
            assert abs(normalized_residual) <= normalized_l1_integer

            for clearing in clearing_samples:
                target = q[n] // math.gcd(q[n], clearing)
                assert (scalar_sum - common_boundary_unit * residual_sum) % target == 0
                residual_capture = math.gcd(target, abs(residual_sum))
                scalar_capture = math.gcd(target, abs(scalar_sum))
                assert residual_capture == scalar_capture
                baseline = math.gcd(target, common_term)
                assert residual_capture % baseline == 0
                cancellation_quotient = residual_capture // baseline
                assert normalized_residual % cancellation_quotient == 0
                assert normalized_l1_integer >= cancellation_quotient
                if residual_sum % target == 0:
                    leftover_target = target // baseline
                    assert normalized_residual % leftover_target == 0
                    target_divisibility_rows.append(
                        {
                            "n": n,
                            "D": clearing,
                            "target": target,
                            "baseline": baseline,
                            "leftover_target": leftover_target,
                        }
                    )
                sum_rows.append(
                    {
                        "n": n,
                        "D": clearing,
                        "degree": degree,
                        "coefficients": coefficients,
                        "gaps": gap_sets,
                        "gap_budgets": gap_budgets,
                        "target": target,
                        "baseline": baseline,
                        "captured": residual_capture,
                        "cancellation_quotient": cancellation_quotient,
                        "normalized_residual": normalized_residual,
                        "normalized_l1": normalized_l1_integer,
                    }
                )

            for prime in check_primes:
                if q[n] % prime:
                    continue
                term_orders = [valuation(term, prime) for term in terms]
                minimum = min(term_orders)
                minimum_count = sum(order == minimum for order in term_orders)
                result_order = valuation(residual_sum, prime)
                if minimum_count == 1:
                    assert result_order == minimum
                elif result_order > minimum:
                    cancellation_rows.append(
                        {
                            "n": n,
                            "p": prime,
                            "coefficients": coefficients,
                            "term_orders": term_orders,
                            "sum_order": result_order,
                        }
                    )
                valuation_rows.append(
                    {
                        "n": n,
                        "p": prime,
                        "coefficients": coefficients,
                        "term_orders": term_orders,
                        "minimum_count": minimum_count,
                        "sum_order": result_order,
                    }
                )

    # The zero-identity branch: duplicate monomials with opposite coefficients.
    zero_identity_rows: list[dict[str, Any]] = []
    for n in range(1, 31):
        gaps = (2 + n % 3, 4 + n % 2, 6 + n % 4)
        residual = product([continuant(n, h) for h in gaps])
        scalar = product([casoratian(q, n, h) for h in gaps])
        residual_identity = residual - residual
        scalar_identity = scalar - scalar
        assert residual_identity == 0
        assert scalar_identity == 0
        zero_identity_rows.append({"n": n, "gaps": gaps, "degree": len(gaps)})

    assert cancellation_rows

    return {
        "schema": "item283-beta-bounded-homogeneous-sum-certificate-v1",
        "description": (
            "Exact bounded-complexity homogeneous sum reduction, normalized "
            "cancellation divisor, unique-minimum split, and zero-identity branch"
        ),
        "declared_class": {
            "sparsity": "fixed T",
            "homogeneous_degree": "fixed K",
            "coefficients": (
                "prime-independent integer values of fixed bounded-degree "
                "polynomials, or more generally coefficient log-height O(log n)"
            ),
            "gaps": (
                "may move with n, independently of target factorization, with "
                "each monomial gap budget O(n/log n)"
            ),
            "residual_height": (
                "H_sum=log(sum_j |c_j| A_j), conservatively before "
                "archimedean cancellation"
            ),
            "exclusions": (
                "nonhomogeneous sums, unbounded sparsity/degree, target-dependent "
                "coefficients, and the identically zero residual as a height certificate"
            ),
        },
        "theorem": {
            "homogeneous_reduction": (
                "gcd(Q,sum c_j D_j)=gcd(Q,R), "
                "R=sum c_j A_j, for every Q|q_n"
            ),
            "cancellation_invariant": (
                "with B=gcd_j |c_j A_j|, G0=gcd(Q,B), "
                "G=gcd(Q,R), X=G/G0, one has X|R/B"
            ),
            "height": (
                "fixed T,K, coefficient log-height O(log n), and monomial "
                "gap budget O(n/log n) imply log|R/B|<=O(n)"
            ),
            "actual_target_implication": (
                "if Q|R then Q/G0 divides R/B and has logarithmic height O(n)"
            ),
            "unique_minimum": (
                "a unique least term valuation gives v_p(R) equal to that "
                "minimum; only tied minima contribute to X"
            ),
            "full_qn_identity": (
                "a nonzero O(n)-height residual cannot be divisible by q_n "
                "for all large n because log q_n=n log n+O(n)"
            ),
            "zero_identity": (
                "R=0 can force homogeneous scalar divisibility modulo q_n, "
                "but supplies no nonzero residual height bound"
            ),
            "deoverlap": "all statements hold for every Q|q_n/gcd(q_n,D_m)",
            "capacity": (
                "the sum-only quotient has O(n)=o(n log n) log height; "
                "the common product baseline remains the Item282 channel"
            ),
        },
        "bounded_exact_checks": {
            "label": "EXACT FINITE ONLY",
            "sum_rows": len(sum_rows),
            "sum_digest": digest(sum_rows),
            "valuation_rows": len(valuation_rows),
            "valuation_digest": digest(valuation_rows),
            "tied_cancellation_rows": len(cancellation_rows),
            "tied_cancellation_digest": digest(cancellation_rows),
            "first_tied_cancellation_row": cancellation_rows[0],
            "target_divisibility_rows": len(target_divisibility_rows),
            "target_divisibility_digest": digest(target_divisibility_rows),
            "zero_identity_rows": len(zero_identity_rows),
            "zero_identity_digest": digest(zero_identity_rows),
            "exceptional_singleton_search": False,
            "asymptotic_extrapolation": False,
        },
        "admission": {
            "sum_only_superlinear_capacity": False,
            "actual_positive_linear_route1_mass": False,
            "uniform_prime_power_height_O_n": False,
            "little_o_squarefull": False,
            "positive_linear_capacity_admission": "FAIL",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
        "open": [
            "the common product baseline and Item282 weighted-return cover",
            "nonhomogeneous sums with different boundary-unit degrees",
            "unbounded sparsity or total degree and arbitrary block/Hankel determinants",
            "a nontrivial prime-independent identity controlling the product baseline",
            "the uniform prime-power-height or little-oh squarefull theorem",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_result(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
