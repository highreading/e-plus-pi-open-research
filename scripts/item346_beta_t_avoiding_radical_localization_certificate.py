#!/usr/bin/env python3
"""Exact deterministic replay for Item 346.

The asymptotic and ideal-contraction proofs are in the report.  This replay
checks declared coordinate and carrier identities using exact integers only.
It performs no prime census, target search, or half-bound scan.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item333_beta_nonlinear_state_saturation_no_go_report.md": (
        "8f4bc0a6f93cbd4882392ade311d68e25be1ceb282db71cc5e1ef2f70aee75d6"
    ),
    "results/item333_beta_nonlinear_state_saturation_no_go_root_audit.json": (
        "6ddd4949f5d7f91fdc160634da06079661ebf373ac0f061495a7b41135924ecc"
    ),
    "sources/item335_beta_first_canonical_cofactor_zero_rate_report.md": (
        "15bd02042bf8a11e774faeed48e21e3de9d89087e04e88df06d0db664041693c"
    ),
    "results/item335_beta_first_canonical_cofactor_zero_rate_root_audit.json": (
        "bbadf11f929237aa89f2891ecb770af03b68fe5fbe5cd233fd86f0c4b78c5bd6"
    ),
    "sources/item340_beta_full_complement_loop_correlation_report.md": (
        "4f3ddc5e09544e7c4d8077413b968f5b8a61694b8872dfdccf89d18dc03018b6"
    ),
    "results/item340_beta_full_complement_loop_correlation_certificate.json": (
        "4be0540e6835c3621482ab42bf5218420d76d7091a827386b1f6978146f6bfd0"
    ),
    "results/item340_beta_full_complement_loop_correlation_root_audit.json": (
        "1b0a53ab7a2c99a5be681a233c1a4c55ff8e6addb702ff287996cab3eb3e1900"
    ),
    "manifests/item340_beta_full_complement_loop_correlation_manifest.json": (
        "3197f620428af855b016842f156f69894f704de2d71846a675860d1a6b679366"
    ),
    "sources/item343_beta_quotient_radical_excess_capacity_report.md": (
        "0fb48e3bbf30d05bcf40d2e4dc9b04e2e80893e6c4fee925d9c6b99b25126c66"
    ),
    "results/item343_beta_quotient_radical_excess_capacity_certificate.json": (
        "c700ffaa6898bd50e4d6b790dea307ec883ecab6374e07a7c62622eb5ba7d57b"
    ),
    "results/item343_beta_quotient_radical_excess_capacity_root_audit.json": (
        "1788b3f5247b132c8ea8f8133d64d9fadcd716013b041964be46b7c71c9747e4"
    ),
    "manifests/item343_beta_quotient_radical_excess_capacity_manifest.json": (
        "eddaff62ba519ece9bac2c881b04b0a0ec3f5dc5d06d780ac03a4b0b7dc69439"
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


def factorization(value: int) -> dict[int, int]:
    if value <= 0:
        raise ValueError("factorization input must be positive")
    remaining = value
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            factors[prime] = exponent
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors[remaining] = 1
    assert math.prod(p**e for p, e in factors.items()) == value
    return factors


def radical_small(value: int) -> int:
    return math.prod(factorization(value))


def continuant(entries: list[int]) -> int:
    previous_previous, previous = 0, 1
    for entry in entries:
        previous_previous, previous = previous, entry * previous + previous_previous
    return previous


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def weight_data(n: int) -> tuple[int, int, list[int]]:
    m = n - 2
    A = 4 * n - 2
    weights = [0] * (m + 2)
    weights[1] = 7
    for index in range(2, m + 1):
        weights[index] = 4 * index + 2
    weights[m + 1] = A
    return A, m, weights


def basis_denominators(weights: list[int], m: int) -> list[int]:
    values = [1]
    previous_previous, previous = 0, 1
    for index in range(1, m + 1):
        current = weights[index] * previous + previous_previous
        values.append(current)
        previous_previous, previous = previous, current
    return values


def canonical_digits(value: int, weights: list[int], m: int) -> list[int]:
    basis = basis_denominators(weights, m)
    if not 0 <= value < basis[m]:
        raise ValueError("canonical value must lie in [0,Q_m)")
    digits = [0] * (m + 1)
    remainder = value
    for index in range(m, 0, -1):
        digits[index], remainder = divmod(remainder, basis[index - 1])
    assert remainder == 0
    assert 0 <= digits[1] <= 6
    for index in range(2, m + 1):
        assert 0 <= digits[index] <= weights[index]
        if digits[index] == weights[index]:
            assert digits[index - 1] == 0
    reconstructed = sum(digits[i] * basis[i - 1] for i in range(1, m + 1))
    assert reconstructed == value
    return digits


def cofactor_rows(
    digits: list[int], weights: list[int], m: int, epsilon: int
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for index in range(3, m + 1):
        raw = digits[index] - weights[index] * digits[index - 1]
        value = epsilon * raw
        if value:
            assert abs(value) <= weights[index] * weights[index - 1]
        rows.append(
            {
                "j": index,
                "delta_previous": digits[index - 1],
                "delta": digits[index],
                "raw": raw,
                "z": value,
            }
        )
    return rows


def carrier_control(
    target: int,
    quotient: int,
    A: int,
    cofactor_data: list[dict[str, Any]],
) -> dict[str, Any]:
    if target <= 0 or quotient <= 0:
        raise ValueError("carrier inputs must be positive")
    saturation_exponent = (A * A - 1).bit_length()
    assert 2 ** (saturation_exponent - 1) < A * A <= 2**saturation_exponent

    primitive_lcm = 1
    away_radical_lcm = 1
    prepared: list[dict[str, Any]] = []
    for row in cofactor_data:
        value = abs(row["z"])
        if not value:
            prepared.append({**row, "omitted_exact_zero": True})
            continue
        primitive_lcm = math.lcm(primitive_lcm, value)
        quotient_power_mod_value = pow(quotient, saturation_exponent, value)
        away = value // math.gcd(value, quotient_power_mod_value)
        away_radical = radical_small(away)
        away_radical_lcm = math.lcm(away_radical_lcm, away_radical)
        prepared.append(
            {
                **row,
                "omitted_exact_zero": False,
                "away": away,
                "away_radical": away_radical,
            }
        )

    global_carrier = math.gcd(target, away_radical_lcm)
    captured = math.gcd(target, primitive_lcm)
    target_exponent = 0 if target == 1 else (target - 1).bit_length()
    if captured == 1:
        item343_perpendicular = 1
    else:
        quotient_power_mod_captured = pow(quotient, target_exponent, captured)
        supported = math.gcd(captured, quotient_power_mod_captured)
        perpendicular = captured // supported
        item343_perpendicular = math.gcd(perpendicular, away_radical_lcm)
    assert item343_perpendicular == global_carrier

    accumulated = 1
    first_hits: list[dict[str, Any]] = []
    high_primes_seen: set[int] = set()
    for row in prepared:
        if row["omitted_exact_zero"]:
            B = 1
        else:
            B = math.gcd(target, row["away_radical"])
        D = B // math.gcd(B, accumulated)
        accumulated = math.lcm(accumulated, B)
        factors = factorization(D)
        low_primes = [prime for prime in factors if prime <= A]
        high_primes = [prime for prime in factors if prime > A]
        assert len(high_primes) <= 1
        high_shape: dict[str, Any] | None = None
        if high_primes:
            prime = high_primes[0]
            assert prime not in high_primes_seen
            high_primes_seen.add(prime)
            assert A < prime < A * A
            assert quotient % prime
            assert row["raw"] < 0
            assert row["delta_previous"] >= 2
            h_value = abs(row["z"]) // prime
            assert 1 <= h_value < A
            high_shape = {"p": prime, "h": h_value}
        first_hits.append(
            {
                "j": row["j"],
                "B": B,
                "D": D,
                "low_primes": low_primes,
                "high_primes": high_primes,
                "high_shape": high_shape,
            }
        )
    assert accumulated == global_carrier
    assert math.prod(row["D"] for row in first_hits) == global_carrier
    for left_index, left in enumerate(first_hits):
        for right in first_hits[left_index + 1 :]:
            assert math.gcd(left["D"], right["D"]) == 1

    return {
        "target": str(target),
        "quotient": str(quotient),
        "M_A": saturation_exponent,
        "primitive_lcm": str(primitive_lcm),
        "away_radical_lcm": str(away_radical_lcm),
        "R_perpendicular": str(global_carrier),
        "item343_R_perpendicular": str(item343_perpendicular),
        "prepared_rows": prepared,
        "first_hits": first_hits,
        "first_hits_digest": digest(first_hits),
        "high_prime_count": len(high_primes_seen),
    }


def seed_row(n: int) -> dict[str, Any]:
    q_values = beta_q(n)
    a, b, c = q_values[n - 1], q_values[n], q_values[n - 2]
    A, m, weights = weight_data(n)
    basis = basis_denominators(weights, m)
    assert basis[m] == a and basis[m - 1] == c
    kappa = (2 * a * a + b) // (2 * b)
    signed_remainder = a * a - kappa * b
    assert signed_remainder
    epsilon = 1 if signed_remainder > 0 else -1
    R = abs(signed_remainder)
    quotient = c - kappa
    assert quotient > 0
    reduced_R = R % a
    digits = canonical_digits(reduced_R, weights, m)
    cofactors = cofactor_rows(digits, weights, m, epsilon)
    carrier = carrier_control(b, quotient, A, cofactors)
    return {
        "n": n,
        "A": A,
        "m": m,
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "kappa": str(kappa),
        "epsilon": epsilon,
        "R": str(R),
        "R_mod_a": str(reduced_R),
        "R_less_than_a": R < a,
        "t": str(quotient),
        "digits": digits[1:],
        "digits_digest": digest(digits[1:]),
        "carrier": carrier,
        "actual_item316_target_claim": False,
        "finite_only": True,
    }


def seed_controls() -> dict[str, Any]:
    declared_n_values = [5, 12, 24, 56]
    rows = [seed_row(n) for n in declared_n_values]
    return {
        "declared_n_values": declared_n_values,
        "row_count": len(rows),
        "rows": rows,
        "rows_digest": digest(rows),
        "prime_census_performed": False,
        "target_search_performed": False,
        "half_bound_census_performed": False,
    }


def e_coefficient_vectors(n: int) -> tuple[list[int], list[int]]:
    A, m, weights = weight_data(n)
    zero = [0] * m
    E_previous = zero[:]
    E_current = zero[:]
    E_current[0] = 1
    vectors = [E_previous, E_current]
    for index in range(1, m + 1):
        following = [
            weights[index + 1] * E_current[column] + E_previous[column]
            for column in range(m)
        ]
        if index + 1 <= m:
            following[index] += (-1) ** index
        vectors.append(following)
        E_previous, E_current = E_current, following
    assert len(vectors) == m + 2
    return vectors[m], vectors[m + 1]


def coordinate_row(n: int, sigma: int) -> dict[str, Any]:
    q_values = beta_q(n)
    a, b, c = q_values[n - 1], q_values[n], q_values[n - 2]
    A, m, weights = weight_data(n)
    E_m, E_next = e_coefficient_vectors(n)
    epsilon = sigma * ((-1) ** m)
    assert E_m[m - 2] == ((-1) ** m) * weights[m]
    assert E_m[m - 1] == (-1) ** (m - 1)
    assert sigma * E_m[m - 2] == epsilon * weights[m]
    assert sigma * E_m[m - 1] == -epsilon

    lower_values = [((-1) ** index) * (index + 2) for index in range(m - 2)]
    lower_target_coefficients = [sigma * E_next[index] for index in range(m - 2)]
    lower_kappa_coefficients = [sigma * E_m[index] for index in range(m - 2)]
    L_value = sum(
        coefficient * value
        for coefficient, value in zip(lower_target_coefficients, lower_values)
    )
    kappa_lower = sum(
        coefficient * value
        for coefficient, value in zip(lower_kappa_coefficients, lower_values)
    )

    target_coordinate = n - 3
    z_coordinate = 2 * sigma - 1
    s = epsilon
    u = s * (A * weights[m] + 1)
    v = -s * A
    alpha = s
    beta = s * weights[m]
    assert alpha * u + beta * v == 1
    d_previous = alpha * (target_coordinate - L_value + a) - v * z_coordinate
    d_top = beta * (target_coordinate - L_value + a) + u * z_coordinate
    digits = lower_values + [d_previous, d_top]

    computed_delta = sigma * sum(
        coefficient * value for coefficient, value in zip(E_next, digits)
    ) - a
    computed_z = epsilon * (d_top - weights[m] * d_previous)
    kappa = sigma * sum(
        coefficient * value for coefficient, value in zip(E_m, digits)
    )
    quotient = c - kappa
    assert computed_delta == target_coordinate
    assert computed_z == z_coordinate
    assert kappa == kappa_lower - z_coordinate
    assert quotient == c - kappa_lower + z_coordinate

    content = math.gcd(c, *[abs(value) for value in lower_kappa_coefficients])
    assert content == 1
    if m == 3:
        assert c == 71
        assert abs(lower_kappa_coefficients[0]) == 141
    else:
        suffix_values = [
            continuant(weights[index + 2 : m + 1])
            for index in range(m)
        ]
        assert math.gcd(suffix_values[m - 4], suffix_values[m - 3]) == 1

    return {
        "n": n,
        "sigma": sigma,
        "epsilon": epsilon,
        "A": A,
        "m": m,
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "target_coordinate": target_coordinate,
        "z_coordinate": z_coordinate,
        "computed_target_coordinate": computed_delta,
        "computed_z_coordinate": computed_z,
        "kappa": str(kappa),
        "kappa_lower": str(kappa_lower),
        "t": str(quotient),
        "lower_t_polynomial_content": content,
        "unimodular_determinant": alpha * u + beta * v,
        "formal_noncanonical_control": True,
        "finite_only": True,
    }


def coordinate_controls() -> dict[str, Any]:
    declared = [(5, 1), (6, -1), (12, 1), (30, -1)]
    rows = [coordinate_row(n, sigma) for n, sigma in declared]
    return {
        "declared_rows": declared,
        "row_count": len(rows),
        "rows": rows,
        "rows_digest": digest(rows),
        "actual_family_claim": False,
        "finite_rows_promoted": False,
    }


def proof_object() -> dict[str, Any]:
    return {
        "actual_carrier": (
            "After exact-zero rows are omitted, saturating each nonzero "
            "z_j by t^ceil(log_2 A^2) removes exactly the t-supported "
            "primary parts. The radical lcm, intersected with rad(Q), is "
            "R_perp_Q."
        ),
        "first_hit": (
            "Successive squarefree novelty quotients D_j are pairwise "
            "coprime and multiply exactly to R_perp_Q; Xi_Q=sum log D_j."
        ),
        "mesoscopic": (
            "The union of p<=A has Chebyshev mass O(A)=o(log b). Since "
            "|z_j|<A^2, the >A part of each D_j is one or a single prime."
        ),
        "density": (
            "Any o(n)-depth portfolio is zero rate. Xi_Q>=eta log b "
            "requires at least (eta/2+o(1))n distinct active depths."
        ),
        "quotient_coordinate": (
            "In the target coordinate ring z=z_m is free and "
            "kappa=kappa_lower-z, t=c-kappa_lower+z."
        ),
        "resultant_barrier": (
            "The lower t-polynomial is primitive. Gauss content gives "
            "((b,Delta,z):t^infinity) intersect Z=(b); the raw union "
            "product ideal is contained in this component and has the "
            "same constant contraction."
        ),
        "scope": (
            "The raw product has exact-zero components; the theorem does "
            "not bound the specialization-first growing first-hit average. "
            "H_Q, squarefull excess, Gamma_Q, and the half-bound stay open."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    coordinates = coordinate_controls()
    seeds = seed_controls()
    proof = proof_object()
    return {
        "schema": "item346-beta-t-avoiding-radical-localization-certificate-v1",
        "item": 346,
        "date": "2026-09-01",
        "status": "PROVED_XI_FIRST_HIT_MESOSCOPIC_LOCALIZATION_SCOPED_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "actual_t_away_carrier": "PROVED",
            "pairwise_coprime_first_hit_factorization": "PROVED",
            "small_prime_zero_rate": "PROVED",
            "one_mesoscopic_prime_per_active_depth": "PROVED",
            "sublinear_depth_zero_rate": "PROVED",
            "positive_mass_density_necessity": "PROVED",
            "localized_raw_resultant_contraction": "PROVED",
            "actual_Xi_Q_zero_rate": "OPEN",
            "actual_Gamma_Q": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "coordinate_controls": coordinates,
        "seed_controls": seeds,
        "strict_scope": {
            "actual_target_claim_from_finite_rows": False,
            "finite_rows_promoted": False,
            "closes": [
                "p<=A support as positive beta-scale Xi_Q mass",
                "every o(n)-depth Xi_Q portfolio as a positive-rate reservoir",
                "an unstratified target/cofactor/t-unit resultant as a carrier smaller than b",
            ],
            "isolates": [
                "a positive-density matching of distinct A<p<A^2 first-hit primes",
                "the specialization-first average of the D_j factors",
            ],
            "does_not_close": [
                "Xi_Q, H_Q, K_Q, or Gamma_Q on the actual target",
                "the Item 265 squarefull branch",
                "the centered half-bound, beta capacity, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_Xi_Q_maximum": "log Q<=log b",
            "small_prime_rate": 0,
            "sublinear_depth_rate": 0,
            "remaining_branch": "positive-density distinct mesoscopic first-hit matching",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item346_beta_t_avoiding_radical_localization_certificate.json",
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
                "actual_Gamma_Q": "OPEN",
                "actual_Xi_Q": "OPEN",
                "booking": 0,
                "item": 346,
                "remaining_branch": "MESOSCOPIC_FIRST_HIT_AVERAGE",
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
