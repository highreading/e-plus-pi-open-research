#!/usr/bin/env python3
"""Deterministic exact checker for Item 305.

The checker replays bounded instances of the universal continuant identities
and the two symbolically proved counterfamilies. Bounded rows are EXACT FINITE
ONLY and are not the proof of infinitude.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path
from typing import Any


def continuant(values: list[int]) -> int:
    before_previous = 0
    previous = 1
    for value in values:
        before_previous, previous = previous, value * previous + before_previous
    return previous


def coefficients(m: int) -> list[int]:
    return [7] + [4 * j + 2 for j in range(2, m + 1)]


def digest(rows: list[dict[str, Any]]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def prefix_denominators(limit: int) -> list[int]:
    result = [1]
    for k in range(1, limit + 1):
        result.append(continuant(coefficients(k)))
    return result


def check_euler_identity(max_n: int) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for n in range(5, max_n + 1):
        m = n - 2
        word = coefficients(m)
        a_value = continuant(word)
        s_value = continuant(word[1:])
        for k in range(1, m):
            q_value = continuant(word[:k])
            p_value = continuant(word[1:k])
            d_value = continuant(word[k + 1 :])
            assert q_value * s_value - p_value * a_value == (-1) ** k * d_value
            rows.append({"n": n, "k": k, "euler_identity": True})
    return {
        "range": [5, max_n],
        "rows": len(rows),
        "digest": digest(rows),
        "label": "EXACT FINITE ONLY",
    }


def check_dual_window(max_n: int) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for n in range(5, max_n + 1):
        m = n - 2
        word = coefficients(m)
        a_value = continuant(word)
        c_value = continuant(word[:-1])
        s_value = continuant(word[1:])
        assert gcd(a_value, s_value) == 1
        assert s_value > c_value

        predicted: set[tuple[int, int, int]] = set()
        for k in range(1, m):
            q_value = continuant(word[:k])
            d_value = continuant(word[k + 1 :])
            multiplier = 1
            while 2 * multiplier * q_value * c_value < a_value:
                if multiplier * d_value < c_value:
                    predicted.add((multiplier * q_value, (-1) ** k, multiplier * d_value))
                multiplier += 1

        observed: set[tuple[int, int, int]] = set()
        r_value = 1
        while 2 * r_value * c_value < a_value:
            for sign in (-1, 1):
                residue = (sign * r_value * s_value) % a_value
                if 0 < residue < c_value:
                    observed.add((r_value, sign, residue))
            r_value += 1
        assert observed == predicted
        rows.append(
            {
                "n": n,
                "admissible_triples": len(observed),
                "classification_exact": True,
            }
        )
    return {
        "range": [5, max_n],
        "rows": len(rows),
        "digest": digest(rows),
        "legendre_extrapolation": False,
        "label": "EXACT FINITE ONLY",
    }


def family_values(k: int, family: str) -> dict[str, int]:
    q_values = prefix_denominators(k + 1)
    q_value = q_values[k]
    if family == "multiplier":
        n = q_value + 2
    elif family == "tail":
        n = (q_value + 3) // 2
    else:
        raise ValueError(family)
    m = n - 2
    word = coefficients(m)
    a_value = continuant(word)
    c_value = continuant(word[:-1])
    d_value = continuant(word[k + 1 :])
    return {
        "k": k,
        "q": q_value,
        "n": n,
        "m": m,
        "a": a_value,
        "c": c_value,
        "d": d_value,
    }


def check_counterfamilies(max_k: int) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for k in range(1, max_k + 1):
        first = family_values(k, "multiplier")
        q_value = first["q"]
        r_value = 2 * q_value
        kappa = 2 * first["d"]
        assert 2 * r_value * first["c"] < first["a"]
        assert kappa < first["c"]
        all_prefix = prefix_denominators(first["m"])
        assert all(value % 2 == 1 for value in all_prefix)
        assert r_value not in set(all_prefix)
        rows.append(
            {
                "family": "multiplier",
                "k": k,
                "n": first["n"],
                "R_equals_2Qk": True,
                "R_below_threshold": True,
                "two_D_below_c": True,
                "R_not_prefix_denominator": True,
            }
        )

        second = family_values(k, "tail")
        assert 2 * q_value * second["c"] < second["a"]
        assert second["d"] < second["c"]
        rows.append(
            {
                "family": "tail",
                "k": k,
                "n": second["n"],
                "Qk_below_threshold": True,
                "Dk_below_c": True,
            }
        )
    return {
        "range": [1, max_k],
        "rows": len(rows),
        "digest": digest(rows),
        "infinite_claim_source": "symbolic inequalities in report Sections 4-5",
        "label": "EXACT FINITE ONLY",
    }


def concrete_example() -> dict[str, Any]:
    values = family_values(1, "multiplier")
    assert values == {
        "k": 1,
        "q": 7,
        "n": 9,
        "m": 7,
        "a": 312129649,
        "c": 10391023,
        "d": 4365570,
    }
    assert 2 * 14 * values["c"] < values["a"]
    assert 2 * values["d"] < values["c"]
    return {
        "k": 1,
        "n": 9,
        "a": values["a"],
        "c": values["c"],
        "D": values["d"],
        "R": 14,
        "kappa": 2 * values["d"],
        "checks": True,
        "label": "EXACT FINITE ONLY",
    }


def symbolic_proof_data() -> dict[str, Any]:
    return {
        "euler_identity": "Q_k S-P_k a=(-1)^k D_k",
        "classification": "R=g Q_k, kappa=g D_k, sign=(-1)^k",
        "multiplier_family": "n=Q_k+2, R=2Q_k, kappa=2D_k",
        "tail_family": "n=(Q_k+3)/2, Q_k<a/(2c), D_k<c",
        "bounded_rows_prove_infinitude": False,
        "actual_half_bound": "OPEN",
        "proper_target_transfer": "OPEN",
        "booking": "zero new Route-1 rate and zero new beta capacity reduction",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--max-n", type=int, default=32)
    parser.add_argument("--max-k", type=int, default=3)
    args = parser.parse_args()

    result = {
        "schema": "item305-beta-continuant-multiplier-certificate-v1",
        "symbolic_proof_data": symbolic_proof_data(),
        "euler_identity_replay": check_euler_identity(args.max_n),
        "dual_window_replay": check_dual_window(args.max_n),
        "counterfamily_replay": check_counterfamilies(args.max_k),
        "concrete_example": concrete_example(),
        "strict_labels": {
            "classification": "PROVED",
            "infinite_counterfamilies": "PROVED SYMBOLICALLY",
            "bounded_checks": "EXACT FINITE ONLY",
            "actual_half_bound": "OPEN",
            "positive_linear_capacity_admission": "FAIL",
        },
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
