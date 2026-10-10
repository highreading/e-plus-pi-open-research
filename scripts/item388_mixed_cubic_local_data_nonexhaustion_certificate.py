#!/usr/bin/env python3
"""Deterministic exact controls for Item 388.

All instantiated rows are EXACT FINITE ONLY.  The general countermodel
theorems are proved algebraically in the report.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path


def valuation(n: int, p: int) -> int:
    result = 0
    while n and n % p == 0:
        n //= p
        result += 1
    return result


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def primes_after(start: int, count: int) -> list[int]:
    out: list[int] = []
    n = max(3, start | 1)
    while len(out) < count:
        if is_prime(n):
            out.append(n)
        n += 2
    return out


def lcm_many(values: list[int]) -> int:
    result = 1
    for value in values:
        result = math.lcm(result, value)
    return result


def fresh_scalar_controls() -> list[dict[str, object]]:
    cases = [
        ({3: 2, 5: 3, 7: 1}, 1, 37, 91),
        ({3: 4, 11: 2, 17: 2}, 5, 143, 221),
        ({5: 5, 7: 3, 13: 2, 19: 1}, 17, 323, 437),
    ]
    rows = []
    for exponents, t, u, v in cases:
        modulus = math.prod(p**e for p, e in exponents.items())
        scalar = 1 + t * modulus
        u2, v2 = scalar * u, scalar * v
        assert u2 % modulus == u % modulus
        assert v2 % modulus == v % modulus
        assert math.gcd(scalar, modulus) == 1
        assert math.gcd(u2, v2) == scalar * math.gcd(u, v)
        for p, e in exponents.items():
            assert u2 % (p**e) == u % (p**e)
            assert v2 % (p**e) == v % (p**e)
            assert valuation(u2, p) == valuation(u, p)
            assert valuation(v2, p) == valuation(v, p)
        bound = 2 * (1 + modulus)
        pair_a = (1, 2)
        pair_b = (1 + modulus, 2 * (1 + modulus))
        assert max(pair_b) <= bound
        assert pair_a[0] % modulus == pair_b[0] % modulus
        assert pair_a[1] % modulus == pair_b[1] % modulus
        rows.append(
            {
                "support_exponents": {str(p): e for p, e in exponents.items()},
                "modulus": modulus,
                "t": t,
                "scalar": scalar,
                "base_pair": [u, v],
                "scaled_pair": [u2, v2],
                "same_complete_residue_package": True,
                "base_gcd": math.gcd(u, v),
                "scaled_gcd": math.gcd(u2, v2),
                "fresh_support_disjoint": True,
                "height_box_control": {
                    "bound": bound,
                    "content_one_pair": list(pair_a),
                    "content_1_plus_M_pair": list(pair_b),
                },
            }
        )
    return rows


def multiparent_control(r: int, start: int) -> dict[str, object]:
    edges = list(itertools.combinations(range(r), 2))
    labels = primes_after(start, len(edges))
    edge_label = dict(zip(edges, labels, strict=True))
    parents = []
    for i in range(r):
        value = 1
        for j in range(r):
            if i == j:
                continue
            edge = (i, j) if i < j else (j, i)
            value *= edge_label[edge]
        parents.append(value)
    for i, j in edges:
        assert math.gcd(parents[i], parents[j]) == edge_label[(i, j)]
    for i, j, k in itertools.combinations(range(r), 3):
        assert math.gcd(math.gcd(parents[i], parents[j]), parents[k]) == 1
        triangle = [edge_label[(i, j)], edge_label[(i, k)], edge_label[(j, k)]]
        assert math.gcd(triangle[0], triangle[1]) == 1
        assert math.gcd(triangle[0], triangle[2]) == 1
        assert math.gcd(triangle[1], triangle[2]) == 1
        assert lcm_many(triangle) == math.prod(triangle)
    product_parents = math.prod(parents)
    unique_modulus = lcm_many(parents)
    reuse = product_parents // unique_modulus
    product_edges = math.prod(labels)
    assert product_parents == product_edges * product_edges
    assert unique_modulus == product_edges
    assert reuse == product_edges == unique_modulus
    star_edges = [(0, j) for j in range(1, r)]
    star_product = math.prod(edge_label[edge] for edge in star_edges)
    assert len(star_edges) == r - 1
    assert product_edges % star_product == 0
    return {
        "vertices": r,
        "edge_count": len(edges),
        "labels": labels,
        "parents": parents,
        "all_triple_gcds_one": True,
        "pair_gcds_equal_edge_labels": True,
        "product_parents": product_parents,
        "unique_crt_modulus": unique_modulus,
        "reuse_credit": reuse,
        "reuse_equals_crt_modulus": True,
        "one_parent_star_edge_count": len(star_edges),
        "one_parent_star_product": star_product,
        "unseen_edge_factor": product_edges // star_product,
    }


def capacity_rows() -> dict[str, object]:
    getcontext().prec = 60
    c_rad = Decimal("0.28490812992172166432")
    target = Decimal("1.1561471519642446123307302239")
    content_height = Decimal("1.99566316016")
    layers = {str(k): str(c_rad * k) for k in range(1, 9)}
    assert c_rad * 4 < target < c_rad * 5
    assert c_rad * 7 < content_height < c_rad * 8
    return {
        "C_rad": str(c_rad),
        "target_T": str(target),
        "frozen_content_height_ceiling": str(content_height),
        "layer_ceilings": layers,
        "four_below_target_five_above": True,
        "seven_below_height_eight_above": True,
        "height_minus_seven_layers": str(content_height - c_rad * 7),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    multiparent = [
        multiparent_control(3, 101),
        multiparent_control(4, 211),
        multiparent_control(6, 401),
        multiparent_control(8, 809),
    ]
    payload = {
        "artifact": "item388_mixed_cubic_local_data_nonexhaustion_certificate",
        "classification": "EXACT FINITE ONLY",
        "general_claims_from_finite_data": False,
        "fresh_scalar_controls": fresh_scalar_controls(),
        "multiparent_controls": multiparent,
        "capacity_controls": capacity_rows(),
        "proved_by_report_not_by_scan": [
            "arbitrary finite-precision fresh-scalar blindness",
            "height-compatible two-realization theorem",
            "complete-graph pair-specific multi-parent construction for every r",
            "sharpness of R<=L and asymptotically vanishing forest fraction",
            "nonexhaustion of finite local digits plus current matching incidence axioms",
        ],
        "searches_performed": {
            "actual_mixed_cubic_rows": False,
            "actual_beta_rows": False,
            "exceptional_prime_search": False,
            "factor_census": False,
            "asymptotic_extrapolation": False,
        },
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    Path(args.output).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

