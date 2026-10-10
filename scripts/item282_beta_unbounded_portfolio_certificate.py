#!/usr/bin/env python3
"""Deterministic certificate for Item 282's unbounded-portfolio dichotomy.

This is an exact, standard-library-only replay.  Bounded computations verify
algebraic identities and do not constitute a prime census or asymptotic
experiment.
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
        raise ValueError("valuation of zero is excluded")
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def product_from_spec(n: int, specification: tuple[tuple[int, int], ...]) -> int:
    result = 1
    for h, weight in specification:
        result *= continuant(n, h) ** weight
    return result


def scalar_product_from_spec(
    q: list[int], n: int, specification: tuple[tuple[int, int], ...]
) -> int:
    result = 1
    for h, weight in specification:
        result *= casoratian(q, n, h) ** weight
    return result


def gap_budget(specification: tuple[tuple[int, int], ...]) -> int:
    return sum(weight * (h - 1) for h, weight in specification)


def factor_degree(specification: tuple[tuple[int, int], ...]) -> int:
    return sum(weight for _, weight in specification)


def digest(rows: list[Any]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def canonical_unbounded_cost(prime: int, depth: int) -> int:
    """Dynamic optimizer over any number of certified anti-period factors."""
    costs = [0] + [10**100] * depth
    for target in range(1, depth + 1):
        costs[target] = min(
            costs[target - part] + prime**part - 1
            for part in range(1, target + 1)
        )
    return costs[depth]


def build_result() -> dict[str, Any]:
    q = q_values(190)
    check_primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    clearing_samples = (1, 3, 5, 7, 9, 11, 15, 25, 49, 77, 121)
    product_specs: list[tuple[tuple[int, int], ...]] = [
        ((2, 1),),
        ((2, 4),),
        ((3, 2), (5, 1)),
        ((2, 7), (4, 3)),
        ((4, 1), (6, 5), (8, 2)),
        ((2, 12), (5, 4), (9, 1)),
    ]

    product_rows: list[dict[str, Any]] = []
    layer_rows: list[dict[str, Any]] = []
    for n in range(1, 31):
        for clearing in clearing_samples:
            target = q[n] // math.gcd(q[n], clearing)
            for specification in product_specs:
                residual = product_from_spec(n, specification)
                scalar = scalar_product_from_spec(q, n, specification)
                captured = math.gcd(target, residual)
                scalar_captured = math.gcd(target, abs(scalar))
                assert captured == scalar_captured
                overlap_majorant = 1
                for h, weight in specification:
                    overlap_majorant *= math.gcd(target, continuant(n, h)) ** weight
                assert overlap_majorant % captured == 0
                budget = gap_budget(specification)
                lower = (4 * n + 6) ** budget
                upper = (4 * (n + budget + 1)) ** budget
                assert lower <= residual <= upper
                assert factor_degree(specification) <= budget
                product_rows.append(
                    {
                        "n": n,
                        "D": clearing,
                        "target": target,
                        "portfolio": specification,
                        "K": factor_degree(specification),
                        "L": budget,
                        "captured": captured,
                        "overlap_majorant": overlap_majorant,
                        "residual": residual,
                    }
                )

            for h in range(2, 10):
                primitive = continuant(n, h)
                previous_gcd = 1
                previous_layer = None
                for power in range(1, 9):
                    current_gcd = math.gcd(target, primitive**power)
                    assert current_gcd % previous_gcd == 0
                    layer = current_gcd // previous_gcd
                    if previous_layer is not None:
                        assert previous_layer % layer == 0
                    layer_rows.append(
                        {
                            "n": n,
                            "D": clearing,
                            "h": h,
                            "power": power,
                            "gcd": current_gcd,
                            "new_layer": layer,
                        }
                    )
                    previous_gcd = current_gcd
                    previous_layer = layer

    optimizer_rows: list[dict[str, Any]] = []
    for prime in (3, 5, 7, 11, 13):
        for depth in range(1, 21):
            optimum = canonical_unbounded_cost(prime, depth)
            expected = depth * (prime - 1)
            assert optimum == expected
            for certified_part in range(1, depth + 1):
                assert prime**certified_part - 1 >= certified_part * (prime - 1)
            optimizer_rows.append(
                {"p": prime, "s": depth, "optimum": optimum}
            )

    # Homogeneous degree-two residual and scalar-Casoratian sums.
    monomial_specs: tuple[tuple[tuple[int, int], ...], ...] = (
        ((2, 1), (4, 1)),
        ((3, 2),),
        ((5, 1), (6, 1)),
    )
    coefficient_rows = (
        (1, 1, 1),
        (1, -1, 0),
        (1, 1, -1),
        (2, -1, 1),
        (1, -2, 1),
        (3, 1, -2),
    )
    sum_rows: list[dict[str, Any]] = []
    cancellation_witnesses: list[dict[str, Any]] = []
    for n in range(1, 31):
        residual_monomials = [
            product_from_spec(n, specification)
            for specification in monomial_specs
        ]
        scalar_monomials = [
            scalar_product_from_spec(q, n, specification)
            for specification in monomial_specs
        ]
        assert all(factor_degree(specification) == 2 for specification in monomial_specs)
        common_unit = (-q[n + 1] ** 2) ** 2
        for coefficients in coefficient_rows:
            residual_sum = sum(
                coefficient * monomial
                for coefficient, monomial in zip(coefficients, residual_monomials)
            )
            scalar_sum = sum(
                coefficient * monomial
                for coefficient, monomial in zip(coefficients, scalar_monomials)
            )
            if residual_sum == 0 or scalar_sum == 0:
                continue
            for clearing in clearing_samples:
                target = q[n] // math.gcd(q[n], clearing)
                assert (scalar_sum - common_unit * residual_sum) % target == 0
                residual_capture = math.gcd(target, abs(residual_sum))
                scalar_capture = math.gcd(target, abs(scalar_sum))
                assert residual_capture == scalar_capture
                term_values = [
                    coefficient * monomial
                    for coefficient, monomial in zip(coefficients, residual_monomials)
                    if coefficient
                ]
                common_term_gcd = 0
                for value in term_values:
                    common_term_gcd = math.gcd(common_term_gcd, abs(value))
                baseline = math.gcd(target, common_term_gcd)
                assert residual_capture % baseline == 0
                sum_rows.append(
                    {
                        "n": n,
                        "D": clearing,
                        "coefficients": coefficients,
                        "target": target,
                        "baseline": baseline,
                        "captured": residual_capture,
                        "cancellation_quotient": residual_capture // baseline,
                    }
                )

            for prime in check_primes:
                if q[n] % prime:
                    continue
                nonzero_terms = [
                    coefficient * monomial
                    for coefficient, monomial in zip(coefficients, residual_monomials)
                    if coefficient
                ]
                orders = [valuation(term, prime) for term in nonzero_terms]
                minimum = min(orders)
                result_order = valuation(residual_sum, prime)
                minimum_count = sum(order == minimum for order in orders)
                if minimum_count == 1:
                    assert result_order == minimum
                elif result_order > minimum:
                    cancellation_witnesses.append(
                        {
                            "n": n,
                            "p": prime,
                            "coefficients": coefficients,
                            "term_orders": orders,
                            "sum_order": result_order,
                        }
                    )

    assert cancellation_witnesses

    return {
        "schema": "item282-beta-unbounded-portfolio-certificate-v1",
        "description": (
            "Exact product-efficiency, diminishing-power, unbounded canonical, "
            "and homogeneous-sum cancellation dichotomy"
        ),
        "exact_quantifiers": {
            "target": (
                "every positive divisor Q of q_n, including every Item265 "
                "de-overlapped surviving target Q|qbar_(m,n)"
            ),
            "products": (
                "every finite weighted product of P_h(n) or scalar C_h(n), "
                "with h>=2 and arbitrary K=K(n)"
            ),
            "sums": (
                "every nonzero homogeneous integer-coefficient sum of "
                "primitive product monomials; coefficients and gaps must be "
                "specified independently of target factorization for admission"
            ),
        },
        "theorem": {
            "height_and_multiplicity": (
                "H=O(n) implies L=O(n/log n) and K<=L=O(n/log n)"
            ),
            "product_overlap_majorant": (
                "gcd(Q,product P_h^w_h) divides "
                "product gcd(Q,P_h)^w_h"
            ),
            "efficiency_dichotomy": (
                "captured_log/H is at most the largest primitive overlap "
                "efficiency log gcd(Q,P_h)/log P_h"
            ),
            "power_layers": (
                "for G_t=gcd(Q,P_h^t), the new layers G_t/G_(t-1) form "
                "a divisibility-decreasing chain"
            ),
            "canonical_unbounded_optimum": (
                "minimum anti-period certified gap cost for depth s is "
                "s(p-1), attained by s repeated depth-one factors"
            ),
            "canonical_capacity": (
                "an O(n)-height canonical portfolio has only O(n/log n) "
                "certified log depth, uniformly over odd primes"
            ),
            "sum_dichotomy": (
                "a unique least term valuation gives no cancellation depth; "
                "only tied minima can create a new sum-only factor"
            ),
            "deoverlap": (
                "all target statements apply after choosing "
                "Q|q_n/gcd(q_n,D_m)"
            ),
            "scope_limit": (
                "actual high-efficiency short returns and tied-minimum "
                "cancellation are not excluded"
            ),
        },
        "bounded_exact_checks": {
            "label": "EXACT FINITE ONLY",
            "product_rows": len(product_rows),
            "product_digest": digest(product_rows),
            "power_layer_rows": len(layer_rows),
            "power_layer_digest": digest(layer_rows),
            "canonical_optimizer_rows": len(optimizer_rows),
            "canonical_optimizer_digest": digest(optimizer_rows),
            "homogeneous_sum_rows": len(sum_rows),
            "homogeneous_sum_digest": digest(sum_rows),
            "tied_cancellation_witness_count": len(cancellation_witnesses),
            "tied_cancellation_witness_digest": digest(cancellation_witnesses),
            "first_tied_cancellation_witness": cancellation_witnesses[0],
            "exceptional_singleton_search": False,
            "asymptotic_extrapolation": False,
        },
        "admission": {
            "actual_high_efficiency_return_mass_theorem": False,
            "actual_sum_cancellation_divisibility_theorem": False,
            "uniform_prime_power_height_O_n": False,
            "little_o_squarefull": False,
            "positive_linear_capacity_admission": "FAIL",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
        "open": [
            "an actual-family high-efficiency or weighted return-cover theorem",
            "a prime-independent homogeneous sum with proved target cancellation divisibility",
            "nonhomogeneous sums and arbitrary growing block/Hankel determinants",
            "the uniform v_p(q_n) log p=O(n) theorem or sufficient little-oh aggregate",
            "the clearing-divisor and transverse matching correlation",
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
