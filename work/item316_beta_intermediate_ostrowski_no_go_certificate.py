#!/usr/bin/env python3
"""Exact deterministic replay for Item 316.

The universal Ostrowski and fixed-precision statements are proved by the
symbolic arguments recorded in the report and certificate.  Declared rows
below are algebra controls only, not a half-bound scan or finite promotion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def continuant(values: list[int]) -> int:
    before_previous = 0
    previous = 1
    for value in values:
        before_previous, previous = previous, value * previous + before_previous
    return previous


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def centered(value: int, odd_modulus: int) -> int:
    residue = value % odd_modulus
    if 2 * residue > odd_modulus:
        residue -= odd_modulus
    return residue


def sign(value: int) -> int:
    if value == 0:
        raise ValueError("zero has no sign in the target theorem")
    return 1 if value > 0 else -1


def coordinates(n: int) -> dict[str, Any]:
    if n < 5:
        raise ValueError("Item 316 coordinates use n>=5")
    m = n - 2
    word = [7] + [4 * index + 2 for index in range(2, m + 1)]
    coefficient_a = 4 * n - 2
    terminal_b = word[-1]

    q_prefix = [1]
    before_previous, previous = 0, 1
    for value in word:
        before_previous, previous = previous, value * previous + before_previous
        q_prefix.append(previous)

    p_prefix = [0]
    before_previous, previous = 1, 0
    for value in word:
        before_previous, previous = previous, value * previous + before_previous
        p_prefix.append(previous)

    delta = [continuant(word[index + 1 :]) for index in range(m)]
    delta_hat = [
        continuant(word[index + 1 :] + [coefficient_a]) for index in range(m)
    ]

    a_value = q_prefix[m]
    b_value = continuant(word + [coefficient_a])
    c_value = q_prefix[m - 1]
    d_value = q_prefix[m - 2]
    s_value = p_prefix[m]
    s_appended = continuant(word[1:] + [coefficient_a])

    assert a_value == continuant(word)
    assert b_value == coefficient_a * a_value + c_value
    assert a_value == terminal_b * c_value + d_value
    assert s_value == continuant(word[1:]) == delta[0]
    assert s_value > c_value
    assert a_value > c_value + s_value

    for index in range(m):
        assert (
            q_prefix[index] * s_value - p_prefix[index] * a_value
            == (-1) ** index * delta[index]
        )
        assert (
            b_value * delta[index]
            + (-1) ** (n + index) * q_prefix[index]
            == a_value * delta_hat[index]
        )

    return {
        "n": n,
        "m": m,
        "word": word,
        "A": coefficient_a,
        "B": terminal_b,
        "Q": q_prefix,
        "P": p_prefix,
        "Delta": delta,
        "Delta_hat": delta_hat,
        "a": a_value,
        "b": b_value,
        "c": c_value,
        "d": d_value,
        "S": s_value,
        "S_appended": s_appended,
    }


def ostrowski_digits(value: int, data: dict[str, Any]) -> list[int]:
    if not 0 <= value < data["a"]:
        raise ValueError("Ostrowski input must lie in [0,a)")
    digits = [0] * data["m"]
    remainder = value
    for index in range(data["m"] - 1, -1, -1):
        digits[index], remainder = divmod(remainder, data["Q"][index])
    assert remainder == 0
    validate_digits(digits, data)
    return digits


def validate_digits(digits: list[int], data: dict[str, Any]) -> None:
    assert len(digits) == data["m"]
    assert 0 <= digits[0] <= 6
    for index in range(1, data["m"]):
        assert 0 <= digits[index] <= data["word"][index]
        if digits[index] == data["word"][index]:
            assert digits[index - 1] == 0


def digit_coordinates(digits: list[int], data: dict[str, Any]) -> dict[str, int]:
    validate_digits(digits, data)
    r_value = sum(
        digits[index] * data["Q"][index] for index in range(data["m"])
    )
    p_value = sum(
        digits[index] * data["P"][index] for index in range(data["m"])
    )
    e_value = sum(
        digits[index] * (-1) ** index * data["Delta"][index]
        for index in range(data["m"])
    )
    u_value = sum(
        digits[index] * (-1) ** (data["n"] + index) * data["Delta_hat"][index]
        for index in range(data["m"])
    )
    appended_error = sum(
        digits[index] * (-1) ** index * data["Delta_hat"][index]
        for index in range(data["m"])
    )
    assert e_value == r_value * data["S"] - p_value * data["a"]
    assert (
        appended_error
        == r_value * data["S_appended"] - p_value * data["b"]
    )
    assert u_value == (-1) ** data["n"] * appended_error
    assert (
        data["a"] * u_value
        == (-1) ** data["n"] * data["b"] * e_value + r_value
    )
    return {"R": r_value, "P": p_value, "E": e_value, "U": u_value}


def half_digits(data: dict[str, Any]) -> list[int]:
    digits: list[int] = []
    for one_based in range(1, data["m"] + 1):
        if one_based % 2 != data["m"] % 2:
            digits.append(0)
        elif one_based == 1:
            digits.append(3)
        else:
            digits.append(data["word"][one_based - 1] // 2)
    validate_digits(digits, data)
    assert digit_coordinates(digits, data)["R"] == (data["a"] - 1) // 2
    assert ostrowski_digits((data["a"] - 1) // 2, data) == digits
    return digits


def telescoping_proof_object() -> dict[str, Any]:
    return {
        "tail_recurrence": "Delta_(i-1)=w_(i+1)Delta_i+Delta_(i+1)",
        "positive_bound": (
            "(w_1-1)Delta_0+sum_(even i>=2)w_(i+1)Delta_i <= a-Delta_0"
        ),
        "negative_bound": (
            "-sum_(odd i>=1)w_(i+1)Delta_i >= -Delta_0"
        ),
        "endpoint_exclusion": (
            "E=-S or E=a-S implies (R+1)S=0 mod a; gcd(S,a)=1 gives "
            "R=a-1, impossible when R<a/2"
        ),
        "strict_conclusion": "-S<E<a-S",
        "carry_consequence": (
            "S>c and a>c+S force E=sigma*kappa, with no +/-a carry, "
            "whenever 0<kappa<c and E=sigma*kappa mod a"
        ),
        "status": "PROVED SYMBOLICALLY",
    }


def declared_digit_controls() -> dict[str, Any]:
    declarations = [
        (5, [1, 70, 500]),
        (6, [7, 1000, 9044]),
        (7, [35, 18088, 199479]),
        (8, [71, 398958, 5195511]),
        (9, [1001, 10391022, 156064824]),
    ]
    rows: list[dict[str, Any]] = []
    for n, values in declarations:
        data = coordinates(n)
        half = half_digits(data)
        for value in values:
            assert 0 <= value < data["a"] / 2
            digits = ostrowski_digits(value, data)
            coords = digit_coordinates(digits, data)
            assert -data["S"] < coords["E"] < data["a"] - data["S"]
            assert abs(coords["U"]) < data["b"]
            rows.append(
                {
                    "n": n,
                    "R": value,
                    "digits": digits,
                    "E_bound": True,
                    "U_bound": True,
                    "half_digits": half,
                }
            )
    return {
        "declared_rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_all_digit_lemma": False,
    }


def fixed_precision_witness(s: int) -> dict[str, Any]:
    if s < 1:
        raise ValueError("s must be positive")
    modulus_reduced = 1 << (s - 1)
    n = max(6, modulus_reduced + 2)
    data = coordinates(n)
    assert data["B"] // 2 >= 2 * modulus_reduced

    if modulus_reduced == 1:
        residue = 0
    else:
        residue = (
            ((data["a"] - 1) // 2)
            * pow(data["A"] // 2, -1, modulus_reduced)
        ) % modulus_reduced

    lower = data["B"] // 2 + 1
    first = lower + (residue - lower) % modulus_reduced
    second = first + modulus_reduced
    assert second <= data["B"]
    exact_value = (
        (data["a"] - 1) // data["A"]
        if (data["a"] - 1) % data["A"] == 0
        else None
    )
    kappa = first if first != exact_value else second
    assert lower <= kappa <= data["B"]
    assert kappa != exact_value

    g_value = data["B"] - kappa
    digits = [0] * data["m"]
    digits[data["m"] - 2] = 1
    digits[data["m"] - 1] = g_value
    coords = digit_coordinates(digits, data)

    assert 0 <= g_value < data["B"] // 2
    assert coords["R"] == g_value * data["c"] + data["d"]
    assert coords["E"] == (-1) ** n * kappa
    assert coords["U"] == data["A"] * kappa + 1
    assert 2 * data["c"] * coords["R"] > data["a"]
    assert 2 * coords["R"] < data["a"]
    assert 0 < kappa < data["c"]
    assert (-1) ** n * sign(coords["E"]) == 1
    assert data["b"] * kappa + coords["R"] == data["a"] * coords["U"]
    assert (coords["U"] - data["a"]) % (1 << s) == 0
    assert (
        data["a"] * data["a"] - data["b"] * kappa - coords["R"]
    ) % (1 << s) == 0
    assert coords["U"] != data["a"]
    assert data["a"] * data["a"] != data["b"] * kappa + coords["R"]

    return {
        "s": s,
        "n": n,
        "modulus": 1 << s,
        "kappa": kappa,
        "g": g_value,
        "digits_top_two": [1, g_value],
        "intermediate_window": True,
        "small_dual_error": True,
        "positive_square_sign": True,
        "U_congruent_a": True,
        "U_equal_a": False,
        "exact_square_equality": False,
    }


def fixed_precision_controls() -> dict[str, Any]:
    rows = [fixed_precision_witness(s) for s in range(1, 7)]
    return {
        "declared_rows": rows,
        "row_digest": digest(rows),
        "label": "EXACT FINITE ONLY",
        "finite_rows_prove_global_witness_theorem": False,
        "symbolic_quantifier": (
            "for fixed s, every n>=max(6,2^(s-1)+2) has an interval of "
            "at least two representatives of the required class modulo 2^(s-1)"
        ),
    }


def small_index_audit() -> dict[str, Any]:
    q_values = beta_q(4)
    expected = {
        2: (1, 1, 1),
        3: (7, 1, 22),
        4: (71, 7, 36),
    }
    rows: list[dict[str, int]] = []
    for n, (a_value, c_value, remainder_size) in expected.items():
        b_value = q_values[n]
        assert (q_values[n - 1], q_values[n - 2]) == (a_value, c_value)
        signed = centered(a_value * a_value, b_value)
        assert abs(signed) == remainder_size
        assert 2 * remainder_size >= a_value
        rows.append(
            {"n": n, "a": a_value, "c": c_value, "R_actual": remainder_size}
        )
    return {"rows": rows, "status": "EXACT BASES; NO HALF-BOUND FAILURE"}


def proof_object() -> dict[str, Any]:
    return {
        "canonical_digits": (
            "R=sum_(i=0)^(m-1) delta_(i+1)Q_i, 0<=delta_1<=6, "
            "0<=delta_i<=w_i, and delta_i=w_i implies delta_(i-1)=0"
        ),
        "half_language": (
            "R<a/2 iff the reversed digit word is lexicographically at most "
            "the alternating digits of (Q_m-1)/2"
        ),
        "dual_coordinates": (
            "E=sum delta_(i+1)(-1)^i Delta_i and "
            "U=sum delta_(i+1)(-1)^(n+i)Dhat_i"
        ),
        "master_identity": "aU=(-1)^n bE+R",
        "strict_dual_error": "-S<E<a-S for R<a/2",
        "endpoint_carry": "EXCLUDED EXACTLY because S>c and a>c+S",
        "actual_kappa_bound": (
            "for n>=5, b<a^2 and bc-a^2=a(4c-d)+c^2>b/2; hence "
            "1<a^2/b<c-1/2 and 1<=kappa<=c-1"
        ),
        "actual_equivalence": (
            "a/(2c)<=R<a/2 is an actual failure iff 0<|E|<c and "
            "U=(-1)^n sign(E)a; then kappa=|E|"
        ),
        "fixed_precision_no_go": (
            "for every fixed s, top-two-digit witnesses satisfy all exact "
            "CF/window/sign data and U=target mod 2^s but not U=target"
        ),
        "not_ruled_out": [
            "precision growing with n",
            "the full 2-adic or integer equality",
            "odd-modulus or global modular-square invariants",
            "the centered half-bound",
        ],
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item316-beta-intermediate-ostrowski-no-go-certificate-v1",
        "item": 316,
        "date_beijing": "2026-08-31",
        "status": "PROVED_EXACT_CLASSIFICATION_AND_SCOPED_FIXED_2ADIC_NO_GO",
        "proof": proof_object(),
        "symbolic_dual_error_proof": telescoping_proof_object(),
        "exact_replay_controls": {
            "digits_and_dual_errors": declared_digit_controls(),
            "fixed_precision_witnesses": fixed_precision_controls(),
            "small_indices": small_index_audit(),
            "label": "EXACT FINITE ONLY",
            "finite_promotion": False,
            "half_bound_scan": False,
            "actual_counterexample_search": False,
        },
        "strict_labels": {
            "canonical_half_language": "PROVED",
            "dual_error_and_no_endpoint_carry": "PROVED",
            "actual_target_equivalence": "PROVED",
            "fixed_precision_2adic_information_class": "PROVED SCOPED NO-GO",
            "centered_half_bound": "OPEN",
            "growing_or_full_2adic_target": "OPEN",
            "odd_modular_square_invariant": "OPEN",
            "bounded_controls": "EXACT FINITE ONLY",
            "capacity_reduction": "ZERO",
            "booking": "ZERO",
        },
        "scope": {
            "item313_role": (
                "retained only for the weaker lower bound and its single-support "
                "small-window theorem; not applied termwise to the all-digit sum"
            ),
            "proper_target": "not constructed or bounded",
            "item282_product_baseline": "preserved and separate",
            "canonical_files_modified": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    certificate = build_certificate()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "item": 316,
                "status": certificate["status"],
                "actual_target_equivalence": "PROVED",
                "fixed_precision_2adic_no_go": "PROVED_SCOPED",
                "centered_half_bound": "OPEN",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
