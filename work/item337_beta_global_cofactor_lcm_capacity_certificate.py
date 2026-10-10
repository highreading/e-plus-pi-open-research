#!/usr/bin/env python3
"""Exact deterministic replay for Item 337.

The all-depth lcm upper bound and the asymptotic quadratic-lcm lower bound
are proved in the report.  This replay checks their exact algebraic inputs on
a declared set of canonical witness rows.  It performs no actual-target scan
and does not re-prove Cilleruelo's published asymptotic theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item265_beta_squarefull_capacity_report.md": (
        "c41d8d2c813d4952ce5a038f291b932817c28ae5b0b1512df0a6bf0ba92a8daa"
    ),
    "results/item265_root_audit.json": (
        "72e5f43c554e326d101d1b2c55de76f277a5a817eaa6b0fc2837dd8f6bbee24a"
    ),
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "sources/item323_beta_all_depth_dual_transducer_no_go_report.md": (
        "e0b5e7279079a17556a0b287ea18a40e461b6fdb8e45d8ef5a357434b8e6d9ef"
    ),
    "results/item323_beta_all_depth_dual_transducer_no_go_root_audit.json": (
        "2455ebbc739cc235bea44e0d220dae6d29be73eac5a9e8a846465366562ca6c2"
    ),
    "sources/item335_beta_first_canonical_cofactor_zero_rate_report.md": (
        "15bd02042bf8a11e774faeed48e21e3de9d89087e04e88df06d0db664041693c"
    ),
}


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    archive_root = Path(__file__).resolve().parent.parent
    rows: list[dict[str, Any]] = []
    for relative_path, expected_hash in DEPENDENCY_HASHES.items():
        path = archive_root / relative_path
        payload = path.read_bytes()
        actual_hash = hashlib.sha256(payload).hexdigest()
        assert actual_hash == expected_hash, (
            relative_path,
            actual_hash,
            expected_hash,
        )
        rows.append(
            {
                "path": relative_path,
                "bytes": len(payload),
                "sha256": actual_hash,
            }
        )
    return {"count": len(rows), "rows": rows, "digest": digest(rows)}


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def lcm_pair(left: int, right: int) -> int:
    if left == 0 or right == 0:
        return 0
    return abs(left // math.gcd(left, right) * right)


def lcm_nonzero(values: list[int]) -> int:
    result = 1
    for value in values:
        if value:
            result = lcm_pair(result, abs(value))
    return result


def small_factorization(value: int) -> dict[int, int]:
    remaining = abs(value)
    if remaining == 0:
        raise ValueError("zero has no finite prime factorization")
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            exponent += 1
            remaining //= prime
        if exponent:
            factors[prime] = exponent
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors[remaining] = 1
    reconstructed = 1
    for factor, exponent in factors.items():
        reconstructed *= factor**exponent
    assert reconstructed == abs(value)
    return factors


def coordinates(n: int) -> dict[str, Any]:
    if n < 5:
        raise ValueError("Item 337 uses n>=5")
    m = n - 2
    q_values = beta_q(n)
    word = [0] + [7] + [4 * index + 2 for index in range(2, m + 1)]
    assert len(word) == m + 1

    continuants = [1]
    previous_previous = 0
    previous = 1
    for index in range(1, m + 1):
        current = word[index] * previous + previous_previous
        continuants.append(current)
        previous_previous, previous = previous, current
    assert continuants == q_values[1 : m + 2]

    return {
        "n": n,
        "m": m,
        "word": word,
        "Q": continuants,
        "q": q_values,
        "A": 4 * n - 2,
        "a": q_values[n - 1],
        "b": q_values[n],
        "c": q_values[n - 2],
    }


def witness_digits(data: dict[str, Any]) -> list[int]:
    m = data["m"]
    digits = [0] * (m + 1)
    digits[1] = 3
    for index in range(2, m + 1):
        digits[index] = 1 if index % 2 == 0 else data["word"][index] // 2
    if m % 2 == 1:
        digits[m] = data["word"][m] // 2 - 1
    return digits


def validate_canonical(digits: list[int], data: dict[str, Any]) -> None:
    m = data["m"]
    assert len(digits) == m + 1
    assert digits[0] == 0
    assert 0 <= digits[1] <= 6
    for index in range(2, m + 1):
        assert 0 <= digits[index] <= data["word"][index]
        if digits[index] == data["word"][index]:
            assert digits[index - 1] == 0


def target_capture_from_max_valuations(
    target: int, maximum_valuations: dict[int, int]
) -> int:
    result = 1
    for prime, maximum in maximum_valuations.items():
        remaining = target
        target_valuation = 0
        while remaining % prime == 0:
            target_valuation += 1
            remaining //= prime
        result *= prime ** min(target_valuation, maximum)
    return result


def finite_row(n: int) -> dict[str, Any]:
    data = coordinates(n)
    m = data["m"]
    digits = witness_digits(data)
    validate_canonical(digits, data)
    assert all(
        digits[index] < data["word"][index]
        for index in range(2, m + 1)
    )

    value = sum(
        digits[index] * data["q"][index]
        for index in range(1, m + 1)
    )
    assert data["q"][m] == data["c"]
    assert digits[m] >= 1
    assert value >= data["c"]
    assert 2 * value < data["a"]
    assert 2 * data["c"] * value > data["a"]
    assert 2 * data["c"] > data["A"]
    assert data["a"] < data["A"] * data["c"]

    z_values = {
        index: digits[index] - data["word"][index] * digits[index - 1]
        for index in range(3, m + 1)
    }
    assert all(z_values.values())
    for index, z_value in z_values.items():
        assert abs(z_value) <= (
            data["word"][index] * data["word"][index - 1]
        )

    even_values: list[int] = []
    for index in range(4, m + 1, 2):
        r_index = index // 2
        expected = 32 * r_index * r_index - 3
        assert abs(z_values[index]) == expected
        even_values.append(expected)

    tower_lcm = lcm_nonzero(list(z_values.values()))
    quadratic_lcm = lcm_nonzero(even_values)
    assert tower_lcm % quadratic_lcm == 0

    cofactor_product = math.prod(abs(value) for value in z_values.values())
    assert cofactor_product % tower_lcm == 0
    word_product = math.prod(data["word"][1 : m + 1])
    universal_product_bound = math.prod(
        data["word"][index] * data["word"][index - 1]
        for index in range(3, m + 1)
    )
    exact_product_formula = (
        word_product * word_product
        // (
            data["word"][1] ** 2
            * data["word"][2]
            * data["word"][m]
        )
    )
    assert universal_product_bound == exact_product_formula
    assert cofactor_product <= universal_product_bound
    assert word_product <= data["a"]

    maximum_valuations: dict[int, int] = {}
    for z_value in z_values.values():
        for prime, exponent in small_factorization(z_value).items():
            maximum_valuations[prime] = max(
                exponent, maximum_valuations.get(prime, 0)
            )
    reconstructed_lcm = math.prod(
        prime**exponent
        for prime, exponent in maximum_valuations.items()
    )
    assert reconstructed_lcm == tower_lcm

    declared_old_reservoir = data["A"] * data["a"]
    deoverlapped_target = data["b"] // math.gcd(
        data["b"], declared_old_reservoir
    )
    target_rows: list[dict[str, Any]] = []
    for label, target in (
        ("full_b", data["b"]),
        ("remove_declared_Aa_overlap", deoverlapped_target),
    ):
        captured = math.gcd(target, tower_lcm)
        from_valuations = target_capture_from_max_valuations(
            target, maximum_valuations
        )
        assert captured == from_valuations
        assert target % captured == 0
        target_rows.append(
            {
                "label": label,
                "target": str(target),
                "captured_gcd": str(captured),
                "captured_bit_length": captured.bit_length(),
                "target_bit_length": target.bit_length(),
                "maximum_valuation_identity": True,
            }
        )

    return {
        "n": n,
        "m": m,
        "A": data["A"],
        "a": str(data["a"]),
        "b": str(data["b"]),
        "c": str(data["c"]),
        "R": str(value),
        "digits": digits[1:],
        "digits_digest": digest(digits),
        "canonical": True,
        "strict_intermediate_R_window": True,
        "z_rows": [[index, z_values[index]] for index in sorted(z_values)],
        "z_digest": digest(z_values),
        "quadratic_values": even_values,
        "quadratic_values_digest": digest(even_values),
        "quadratic_lcm": str(quadratic_lcm),
        "tower_lcm": str(tower_lcm),
        "tower_lcm_bit_length": tower_lcm.bit_length(),
        "cofactor_product_bit_length": cofactor_product.bit_length(),
        "universal_product_bound_bit_length": universal_product_bound.bit_length(),
        "word_product_bit_length": word_product.bit_length(),
        "continuant_bit_length": data["a"].bit_length(),
        "quadratic_lcm_divides_tower_lcm": True,
        "tower_lcm_divides_cofactor_product": True,
        "universal_product_formula": True,
        "continuant_dominates_word_product": True,
        "maximum_valuations_digest": digest(maximum_valuations),
        "target_rows": target_rows,
        "finite_tower_lcm_bits_over_b_bits": (
            f"{tower_lcm.bit_length()}/{data['b'].bit_length()}"
        ),
        "finite_quadratic_lcm_bits_over_b_bits": (
            f"{quadratic_lcm.bit_length()}/{data['b'].bit_length()}"
        ),
        "actual_item316_target_claim": False,
        "finite_only": True,
    }


def exact_controls() -> dict[str, Any]:
    declared_n_values = [5, 6, 8, 12, 20, 32, 48, 64]
    rows = [finite_row(n) for n in declared_n_values]
    return {
        "declared_n_values": declared_n_values,
        "row_count": len(rows),
        "rows": rows,
        "rows_digest": digest(rows),
        "target_census_performed": False,
        "bounded_rows_promoted": False,
        "external_asymptotic_reproved": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "actual_family_implication": (
            "An Item-316 target supplies a canonical digit word and the exact "
            "cofactors z_j=epsilon(delta_j-w_j delta_(j-1)); Item 335 proves "
            "that at least one z_j is nonzero."
        ),
        "primitive_tower": (
            "Lambda=lcm_{z_j nonzero}|z_j|. For Q|b, log gcd(Q,Lambda) "
            "equals sum_p min(v_p(Q),max_j v_p(z_j)) log p."
        ),
        "universal_upper": (
            "Lambda<=product_{j=3}^m w_j w_(j-1)="
            "W_m^2/(w_1^2 w_2 w_m), while W_m<=a<exp(1/8)W_m; "
            "therefore log Lambda<=2 log b-3 log A+O(1)."
        ),
        "one_target_ceiling": (
            "For every de-overlapped Q|b, gcd(Q,Lambda)|Q, so the tower "
            "can supply at most log Q<=log b, never two target copies."
        ),
        "canonical_witness": (
            "Set delta_1=3, delta_j=1 at even j and w_j/2 at odd j; "
            "when m is odd lower delta_m by one. This is canonical and lies "
            "strictly between a/(2c) and a/2."
        ),
        "quadratic_subsequence": (
            "For every even j=2r>=4, |z_j|=32r^2-3, whose discriminant "
            "384 is nonsquare; gcd(|f(0)|,|f(1)|)=gcd(3,29)=1."
        ),
        "external_published_input": {
            "author": "Javier Cilleruelo",
            "title": "The least common multiple of a quadratic sequence",
            "url": "https://arxiv.org/abs/1001.3438",
            "theorem": (
                "For irreducible quadratic f in Z[x], "
                "log lcm(f(1),...,f(N))=N log N+O_f(N)."
            ),
            "reproved_by_replay": False,
        },
        "capacity_decision": (
            "The canonical intermediate-window class admits "
            "log Lambda>=(1/2+o(1))log b. Hence fixed-complexity closure "
            "does not extend to the full tower; Lambda is a bulk invariant."
        ),
        "strict_scope": (
            "The witness is not asserted to satisfy Item 316's small-error "
            "or Delta=0 target equation. Actual target overlap with Q remains "
            "open and no capacity is booked."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    controls = exact_controls()
    proof = proof_object()
    return {
        "schema": "item337-beta-global-cofactor-lcm-capacity-certificate-v1",
        "item": 337,
        "date": "2026-09-01",
        "status": "PROVED_GLOBAL_LCM_CAPACITY_DECISION_FIRST_BULK_INVARIANT",
        "dependencies": dependencies,
        "theorem": {
            "actual_target_to_nonempty_cofactor_tower": "PROVED",
            "exact_cross_depth_overlap_normalization": "PROVED",
            "universal_lcm_upper_rate_at_most_two": "PROVED",
            "one_deoverlapped_target_rate_at_most_one": "PROVED",
            "canonical_intermediate_window_witness": "PROVED",
            "quadratic_subsequence": "PROVED",
            "ambient_primitive_lcm_rate_at_least_one_half": (
                "PROVED USING PUBLISHED QUADRATIC-LCM THEOREM"
            ),
            "full_tower_zero_rate_from_canonical_window_data": "DISPROVED",
            "actual_target_shared_mass": "OPEN",
            "centered_half_bound": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "exact_controls": controls,
        "strict_scope": {
            "actual_target_claim_from_witness": False,
            "finite_rows_promoted": False,
            "closes": [
                "product booking across cofactor depths",
                "the claim that every growing-depth canonical cofactor tower is zero rate",
                "extension of Item 335's fixed-complexity no-go to the full lcm tower",
            ],
            "isolates": [
                "Lambda as the first overlap-normalized bulk cofactor invariant",
                "Gamma_Q=log gcd(Q,Lambda) as the exact actual-family capacity question",
            ],
            "does_not_close": [
                "the original Item-316 target or centered half-bound",
                "target-specific shared prime mass Gamma_Q",
                "removal of every old denominator reservoir",
                "beta capacity, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_lcm_universal_upper_rate": 2,
            "raw_lcm_ambient_lower_rate": "at least 1/2+o(1)",
            "one_target_universal_upper_rate": 1,
            "actual_target_rate": "OPEN",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "work/item337_beta_global_cofactor_lcm_capacity_"
            "certificate.json"
        ),
    )
    args = parser.parse_args()
    result = build_certificate()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = Path(__file__).resolve().parent.parent / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "actual_target_mass": "OPEN",
                "ambient_lcm_lower_rate": "AT_LEAST_ONE_HALF",
                "booking": 0,
                "centered_half_bound": "OPEN",
                "item": 337,
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
