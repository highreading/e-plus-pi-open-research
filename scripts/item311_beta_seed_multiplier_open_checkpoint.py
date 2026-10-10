#!/usr/bin/env python3
"""Deterministic exact replay for the Item 311 OPEN checkpoint.

The bounded rows replay universal recurrence and continuant identities only.
They do not scan for a counterexample, prove the open divisibility exclusion,
or promote any finite observation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def digest(rows: list[dict[str, Any]]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def continuant(values: list[int]) -> int:
    before_previous = 0
    previous = 1
    for value in values:
        before_previous, previous = previous, value * previous + before_previous
    return previous


def beta_sequences(limit: int) -> tuple[list[int], list[int]]:
    q_values = [1, 1]
    p_values = [1, 3]
    for n in range(2, limit + 1):
        coefficient = 4 * n - 2
        q_values.append(coefficient * q_values[-1] + q_values[-2])
        p_values.append(coefficient * p_values[-1] + p_values[-2])
    return p_values, q_values


def coefficients(m: int) -> list[int]:
    assert m >= 1
    return [7] + [4 * j + 2 for j in range(2, m + 1)]


def centered(value: int, odd_modulus: int) -> int:
    assert odd_modulus > 0 and odd_modulus % 2 == 1
    residue = value % odd_modulus
    if 2 * residue > odd_modulus:
        residue -= odd_modulus
    return residue


def check_companion_tail(limit: int) -> dict[str, Any]:
    p_values, q_values = beta_sequences(limit)
    rows: list[dict[str, Any]] = []
    previous_tail = 1
    current_tail = 10
    for n in range(2, limit + 1):
        word = list(range(10, 4 * n - 1, 4))
        tail = continuant(word)
        companion = (3 * q_values[n] - p_values[n]) // 2
        assert 3 * q_values[n] - p_values[n] == 2 * companion
        assert tail == companion
        if n == 2:
            assert tail == 1
        elif n == 3:
            assert tail == 10
        else:
            next_tail = (4 * n - 2) * current_tail + previous_tail
            assert tail == next_tail
            previous_tail, current_tail = current_tail, next_tail
        if n >= 3:
            previous_companion = (3 * q_values[n - 1] - p_values[n - 1]) // 2
            assert (
                q_values[n - 1] * companion
                - q_values[n] * previous_companion
                == (-1) ** n
            )
        rows.append(
            {
                "n": n,
                "tail_equals_(3q-p)/2": True,
                "adjacent_tail_determinant": n >= 3,
            }
        )
    return {
        "range": [2, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_all_n_identity": False,
    }


def check_appended_tail_identities(limit: int) -> dict[str, Any]:
    p_values, q_values = beta_sequences(limit)
    rows: list[dict[str, Any]] = []
    for n in range(5, limit + 1):
        m = n - 2
        coefficient = 4 * n - 2
        word = coefficients(m)
        extended_word = word + [coefficient]
        a_value = continuant(word)
        b_value = continuant(extended_word)
        c_value = continuant(word[:-1])
        assert (a_value, b_value, c_value) == (
            q_values[n - 1],
            q_values[n],
            q_values[n - 2],
        )
        assert b_value == coefficient * a_value + c_value

        s_previous = continuant(word[1:])
        s_current = continuant(extended_word[1:])
        assert s_previous == (3 * a_value - p_values[n - 1]) // 2
        assert s_current == (3 * b_value - p_values[n]) // 2

        for k in range(1, m):
            q_prefix = continuant(word[:k])
            p_prefix = continuant(word[1:k])
            d_tail = continuant(word[k + 1 :])
            appended_tail = continuant(word[k + 1 :] + [coefficient])
            epsilon = (-1) ** (n + k)

            assert q_prefix == q_values[k + 1]
            assert p_prefix == (3 * q_prefix - p_values[k + 1]) // 2
            assert q_prefix * s_previous - p_prefix * a_value == (
                (-1) ** k * d_tail
            )
            assert q_prefix * s_current - p_prefix * b_value == (
                (-1) ** k * appended_tail
            )
            assert (
                p_values[k + 1] * b_value - q_prefix * p_values[n]
                == 2 * (-1) ** k * appended_tail
            )
            assert b_value * d_tail + epsilon * q_prefix == (
                a_value * appended_tail
            )

            tail_length = m - k
            if tail_length % 2 == 0:
                assert appended_tail % 2 == 1
                assert d_tail % 2 == 0
                assert epsilon == 1
            else:
                assert appended_tail % 2 == 0

            rows.append(
                {
                    "n": n,
                    "k": k,
                    "pade_cross_determinant": True,
                    "appended_tail_bridge": True,
                    "parity_orientation": True,
                }
            )
    return {
        "range": [5, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "divisibility_search": False,
        "actual_half_bound_scan": False,
    }


def check_actual_centering_identities(limit: int) -> dict[str, Any]:
    p_values, q_values = beta_sequences(limit)
    rows: list[dict[str, Any]] = []
    for n in range(3, limit + 1):
        a_value = q_values[n - 1]
        b_value = q_values[n]
        c_value = q_values[n - 2]
        signed_r = centered(a_value * a_value, b_value)
        assert signed_r != 0
        kappa = (a_value * a_value - signed_r) // b_value
        assert a_value * a_value == kappa * b_value + signed_r
        assert kappa > 0
        if n == 3:
            assert kappa == c_value
        else:
            assert kappa < c_value
        s_previous = (3 * a_value - p_values[n - 1]) // 2
        assert (
            (signed_r * s_previous - (-1) ** n * kappa) % a_value == 0
        )
        rows.append(
            {
                "n": n,
                "actual_square_decomposition": True,
                "actual_kappa_range": True,
                "seed_congruence": True,
            }
        )
    return {
        "range": [3, limit],
        "rows": len(rows),
        "digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "counterexample_search": False,
    }


def exact_small_bases() -> dict[str, Any]:
    p_values, q_values = beta_sequences(4)
    rows: list[dict[str, Any]] = []
    expected = {
        2: (1, 7, 1, 0, 1),
        3: (7, 71, 1, 1, -22),
        4: (71, 1001, 7, 5, 36),
    }
    for n, values in expected.items():
        a_value, b_value, c_value, kappa, signed_r = values
        assert (q_values[n - 1], q_values[n], q_values[n - 2]) == (
            a_value,
            b_value,
            c_value,
        )
        assert centered(a_value * a_value, b_value) == signed_r
        assert a_value * a_value == kappa * b_value + signed_r
        rows.append(
            {
                "n": n,
                "a": a_value,
                "b": b_value,
                "c": c_value,
                "kappa": kappa,
                "signed_r": signed_r,
                "label": "EXACT BASE",
            }
        )
    return {"rows": rows, "p_values_used": p_values[2:5]}


def false_split_quarantine() -> dict[str, Any]:
    n = 9
    m = n - 2
    coefficient = 4 * n - 2
    word = coefficients(m)
    k = 1
    a_value = continuant(word)
    q_k = continuant(word[:k])
    q_next = continuant(word[: k + 1])
    d_tail = continuant(word[k + 1 :])
    appended_tail = continuant(word[k + 1 :] + [coefficient])
    left = a_value - q_k * appended_tail
    false_right = (q_next - coefficient * q_k) * d_tail
    assert left == -727893342
    assert false_right == -729050190
    assert left != false_right
    return {
        "n": n,
        "k": k,
        "a": a_value,
        "Q_k": q_k,
        "Q_(k+1)": q_next,
        "D_k": d_tail,
        "Dhat_k": appended_tail,
        "left": left,
        "false_right": false_right,
        "identity_is_false": True,
        "label": "EXACT COUNTEREXAMPLE TO QUARANTINED IDENTITY",
    }


def symbolic_proof_data() -> dict[str, Any]:
    return {
        "companion_tail": (
            "S_n=K(10,14,...,4n-2)=(3q_n-p_n)/2 for n>=2; "
            "proved by the common recurrence and bases S_2=1,S_3=10"
        ),
        "pade_bridge": (
            "p_(k+1)q_n-q_(k+1)p_n=2(-1)^k Dhat_k"
        ),
        "appended_tail_bridge": (
            "q_n D_k+(-1)^(n+k)Q_k=q_(n-1)Dhat_k"
        ),
        "exact_open_reduction": (
            "R<q_(n-1)/(2q_(n-2)) iff some k has "
            "Dhat_k|q_(n-1) and Dhat_k>2q_(n-2)Q_k"
        ),
        "parity_consequence": (
            "a hypothetical divisor branch has n+k even, positive signed "
            "remainder, odd R, and even kappa"
        ),
        "remaining_divisibility_lemma": (
            "Dhat_k>2q_(n-2)Q_k => Dhat_k does not divide q_(n-1)"
        ),
        "remaining_divisibility_lemma_status": "OPEN",
        "actual_half_bound": "OPEN",
        "intermediate_gap": (
            "q_(n-1)/(2q_(n-2)) <= R < q_(n-1)/2"
        ),
        "booking": "zero new Route-1 rate and zero new beta capacity reduction",
    }


def build_certificate(limit: int) -> dict[str, Any]:
    return {
        "schema": "item311-beta-seed-multiplier-open-checkpoint-v1",
        "status": "OPEN",
        "description": (
            "Exact Padé/continuant bridge and reduction of the actual "
            "Item305 small window to one unresolved divisibility implication"
        ),
        "symbolic_proof_data": symbolic_proof_data(),
        "bounded_exact_replay": {
            "companion_tail": check_companion_tail(limit),
            "appended_tail_identities": check_appended_tail_identities(limit),
            "actual_centering_identities": check_actual_centering_identities(limit),
            "small_bases": exact_small_bases(),
            "false_split_quarantine": false_split_quarantine(),
            "label": "EXACT FINITE ONLY",
            "finite_promotion": False,
            "actual_half_bound_scan": False,
            "divisibility_search": False,
        },
        "strict_labels": {
            "companion_tail_identity": "PROVED",
            "pade_cross_determinant": "PROVED",
            "appended_tail_bridge": "PROVED",
            "small_window_divisor_equivalence": "PROVED EXACT REDUCTION",
            "false_split_identity": "FALSE AND QUARANTINED",
            "divisibility_exclusion": "OPEN",
            "actual_half_bound": "OPEN",
            "bounded_rows": "EXACT FINITE ONLY",
            "positive_linear_capacity_admission": "FAIL",
            "booking": "ZERO",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=32)
    args = parser.parse_args()
    if args.limit < 9:
        raise ValueError("--limit must be at least 9")
    result = build_certificate(args.limit)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
