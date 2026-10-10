#!/usr/bin/env python3
"""Deterministic certificate for Item 278's Casoratian-portfolio theorem.

All calculations are exact and standard-library only.  Bounded rows replay
identities; no distributional inference or exceptional-prime search occurs.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any, Iterable


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


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("zero valuation is not used")
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def weak_compositions(total: int, slots: int) -> Iterable[tuple[int, ...]]:
    if slots == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, slots - 1):
            yield (first,) + tail


def balanced_depths(depth: int, slots: int) -> tuple[int, ...]:
    quotient, remainder = divmod(depth, slots)
    return (quotient + 1,) * remainder + (quotient,) * (slots - remainder)


def canonical_cost(prime: int, depth: int, slots: int) -> int:
    return sum(prime**part - 1 for part in balanced_depths(depth, slots))


def digest(rows: list[Any]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def scalar_casoratian(q: list[int], n: int, h: int) -> int:
    return q[n] * q[n + h + 1] - q[n + 1] * q[n + h]


def build_result() -> dict[str, Any]:
    q = q_values(180)
    check_primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

    portfolio_specs: list[tuple[tuple[int, int], ...]] = [
        ((2, 1),),
        ((3, 2),),
        ((2, 1), (4, 1)),
        ((2, 2), (5, 1)),
        ((3, 1), (4, 2)),
        ((2, 1), (3, 1), (6, 1)),
        ((2, 2), (4, 1), (7, 2)),
        ((5, 3), (8, 1)),
    ]

    valuation_rows: list[dict[str, Any]] = []
    deoverlap_rows: list[dict[str, Any]] = []
    clearing_samples = (1, 3, 5, 7, 9, 11, 15, 25, 49, 77, 121)
    for n in range(1, 31):
        divisors = [
            prime for prime in check_primes
            if q[n] % prime == 0
        ]
        for specification in portfolio_specs:
            residual_product = 1
            casoratian_product = 1
            gap_budget = 0
            for h, weight in specification:
                residual_product *= continuant(n, h) ** weight
                casoratian_product *= scalar_casoratian(q, n, h) ** weight
                gap_budget += weight * (h - 1)
            for prime in divisors:
                a = valuation(q[n], prime)
                residual_order = valuation(residual_product, prime)
                casoratian_order = valuation(casoratian_product, prime)
                return_sum = sum(
                    weight * min(a, valuation(q[n + h], prime))
                    for h, weight in specification
                )
                assert min(a, residual_order) == min(a, return_sum)
                assert min(a, casoratian_order) == min(a, return_sum)
                valuation_rows.append(
                    {
                        "n": n,
                        "p": prime,
                        "a": a,
                        "portfolio": specification,
                        "gap_budget": gap_budget,
                        "v_residual": residual_order,
                        "v_casoratian": casoratian_order,
                        "return_sum": return_sum,
                    }
                )
            for clearing in clearing_samples:
                qbar = q[n] // math.gcd(q[n], clearing)
                for prime in divisors:
                    surviving = max(
                        valuation(q[n], prime) - valuation(clearing, prime),
                        0,
                    )
                    if surviving == 0:
                        continue
                    residual_order = valuation(residual_product, prime)
                    casoratian_order = valuation(casoratian_product, prime)
                    return_sum = sum(
                        weight * min(surviving, valuation(q[n + h], prime))
                        for h, weight in specification
                    )
                    assert min(surviving, residual_order) == min(
                        surviving, return_sum
                    )
                    assert min(surviving, casoratian_order) == min(
                        surviving, return_sum
                    )
                    deoverlap_rows.append(
                        {
                            "n": n,
                            "D": clearing,
                            "qbar": qbar,
                            "p": prime,
                            "surviving_depth": surviving,
                            "portfolio": specification,
                            "return_sum": return_sum,
                        }
                    )

    height_rows: list[dict[str, Any]] = []
    for n in range(1, 41):
        for specification in portfolio_specs:
            residual_product = 1
            gap_budget = 0
            for h, weight in specification:
                residual_product *= continuant(n, h) ** weight
                gap_budget += weight * (h - 1)
            lower = (4 * n + 6) ** gap_budget
            upper = (4 * (n + gap_budget + 1)) ** gap_budget
            assert lower <= residual_product <= upper
            height_rows.append(
                {
                    "n": n,
                    "portfolio": specification,
                    "gap_budget": gap_budget,
                    "lower": lower,
                    "residual_product": residual_product,
                    "upper": upper,
                }
            )

    optimizer_rows: list[dict[str, Any]] = []
    for prime in (3, 5, 7, 11):
        for slots in range(1, 7):
            for depth in range(1, 17):
                formula = canonical_cost(prime, depth, slots)
                brute = min(
                    sum(prime**part - 1 for part in composition)
                    for composition in weak_compositions(depth, slots)
                )
                assert formula == brute
                balanced = balanced_depths(depth, slots)
                assert sum(balanced) == depth
                assert max(balanced) - min(balanced) <= 1
                assert (formula + slots) ** slots >= (
                    slots**slots * prime**depth
                )
                optimizer_rows.append(
                    {
                        "p": prime,
                        "K": slots,
                        "s": depth,
                        "balanced": balanced,
                        "cost": formula,
                    }
                )

    antiperiod_portfolio_rows: list[dict[str, Any]] = []
    for n in range(1, 31):
        for prime in check_primes:
            if q[n] % prime:
                continue
            available_depth = valuation(q[n], prime)
            for slots in range(1, 5):
                for target_depth in range(1, available_depth + 1):
                    parts = balanced_depths(target_depth, slots)
                    product = 1
                    gap_budget = 0
                    for part in parts:
                        if part == 0:
                            continue
                        gap = prime**part
                        assert q[n] % gap == 0
                        assert continuant(n, gap) % gap == 0
                        product *= continuant(n, gap)
                        gap_budget += gap - 1
                    assert valuation(product, prime) >= target_depth
                    assert gap_budget == canonical_cost(prime, target_depth, slots)
                    antiperiod_portfolio_rows.append(
                        {
                            "n": n,
                            "p": prime,
                            "available_depth": available_depth,
                            "K": slots,
                            "target_depth": target_depth,
                            "balanced_depths": parts,
                            "gap_budget": gap_budget,
                        }
                    )

    return {
        "schema": "item278-beta-casoratian-portfolio-certificate-v1",
        "description": (
            "Exact residual-height and p-adic-depth accounting for weighted "
            "products of primitive growing beta Casoratians"
        ),
        "exact_class": {
            "portfolio": (
                "A=product_i P_(h_i)(n)^(w_i), "
                "D=product_i C_(h_i)(n)^(w_i), h_i>=2, w_i>=1"
            ),
            "multiplicity": "K=sum_i w_i",
            "gap_budget": "L=sum_i w_i(h_i-1)",
            "residual_height": "H=log A=sum_i w_i log P_(h_i)(n)",
            "exclusions": (
                "sums with cancellation, arbitrary block/Hankel determinants, "
                "and coefficients not generated by primitive transfer minors"
            ),
        },
        "theorem": {
            "height_gap_tradeoff": (
                "L log(4n+6)<=H<=L log(4(n+L+1)); "
                "therefore H=O(n) iff L=O(n/log n)"
            ),
            "depth_accounting": (
                "for p^s|q_n, min(s,v_p(A))=min(s,v_p(D))="
                "min(s,sum_i w_i min(s,v_p(q_(n+h_i))))"
            ),
            "bounded_K_consequence": (
                "if K is fixed and the portfolio reaches depth s with "
                "H=O(n), then some h_i=O(n/log n) satisfies "
                "p^ceil(s/K)|q_(n+h_i)"
            ),
            "canonical_antiperiod_optimum": (
                "for K slots and s=Kq+r, the minimum guaranteed gap cost "
                "is (K-r)(p^q-1)+r(p^(q+1)-1)"
            ),
            "canonical_fixed_K_barrier": (
                "O(n) residual height in the canonical anti-period class "
                "forces s log p=O_K(log n)"
            ),
            "deoverlap": (
                "all formulas hold with s=(v_p(q_n)-v_p(D_m))_+, "
                "the surviving Item265 exponent"
            ),
            "scope_limit": (
                "a new uniform short-return theorem could beat the canonical "
                "anti-period portfolio and is not excluded"
            ),
        },
        "bounded_exact_checks": {
            "label": "EXACT FINITE ONLY",
            "portfolio_valuation_rows": len(valuation_rows),
            "portfolio_valuation_digest": digest(valuation_rows),
            "deoverlap_rows": len(deoverlap_rows),
            "deoverlap_digest": digest(deoverlap_rows),
            "height_rows": len(height_rows),
            "height_digest": digest(height_rows),
            "balanced_optimizer_rows": len(optimizer_rows),
            "balanced_optimizer_digest": digest(optimizer_rows),
            "antiperiod_portfolio_rows": len(antiperiod_portfolio_rows),
            "antiperiod_portfolio_digest": digest(antiperiod_portfolio_rows),
            "exceptional_singleton_search": False,
            "asymptotic_extrapolation": False,
        },
        "admission": {
            "uniform_prime_power_height_O_n": False,
            "little_o_squarefull": False,
            "positive_linear_capacity_admission": "FAIL",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
        "open": [
            "a uniform short-return lower bound or construction for the actual high levels",
            "growing sums with cancellation or arbitrary growing block/Hankel determinants",
            "unbounded portfolio multiplicity with genuinely independent arithmetic input",
            "the uniform v_p(q_n) log p=O(n) theorem or a sufficient little-oh aggregate",
            "the actual clearing-divisor and transverse matching correlation",
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
