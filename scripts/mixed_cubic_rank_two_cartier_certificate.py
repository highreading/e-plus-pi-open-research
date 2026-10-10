#!/usr/bin/env python3
"""Deterministic finite audit for the mixed-cubic rank-two Cartier divisor.

The companion note proves the uniform determinant and divisibility statements.
This program checks normalizations against frozen exact coordinates and audits
the displayed determinant identities on a finite, explicitly recorded range.
No asymptotic assertion is inferred from this computation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


ARCHIVE = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def valuation(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        raise ValueError("the frozen coordinates are nonzero")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def top_prime_power(prime: int, limit: int) -> tuple[int, int]:
    exponent = 1
    layer = prime
    while layer * prime <= limit:
        layer *= prime
        exponent += 1
    return exponent, layer


def d_value(n_value: int, k_value: int, modulus: int) -> int:
    remainder_n = n_value % modulus
    remainder_k = k_value % modulus
    if remainder_k == 0:
        return 2 * remainder_n
    return 2 * remainder_n + 3 * (modulus - remainder_k)


def multiply(
    left: tuple[int, ...],
    right: tuple[int, ...],
    modulus: int,
    cutoff: int,
) -> tuple[int, ...]:
    result = [0] * min(cutoff + 1, len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        if left_value == 0:
            continue
        upper = min(len(right), len(result) - left_index)
        for right_index in range(upper):
            result[left_index + right_index] = (
                result[left_index + right_index]
                + left_value * right[right_index]
            ) % modulus
    return tuple(result)


def power(
    base: tuple[int, ...],
    exponent: int,
    modulus: int,
    cutoff: int,
) -> tuple[int, ...]:
    result = (1,)
    while exponent:
        if exponent & 1:
            result = multiply(result, base, modulus, cutoff)
        exponent >>= 1
        if exponent:
            base = multiply(base, base, modulus, cutoff)
    return result


@lru_cache(maxsize=None)
def determinant_coefficients(
    prime: int, layer: int, residual_index: int
) -> tuple[int, int, int, int, int]:
    """Return (a0,b0,a1,b1,Delta) for a delta-zero top layer."""

    h_value = layer - 2 * residual_index - 2
    if h_value < 0:
        raise ValueError((prime, layer, residual_index, h_value))
    cutoff = 2 * layer - 1
    u_power = power((0, 1, -1), 3 * residual_index, prime, cutoff)
    q_power = power((1, 1, 1, 1), h_value, prime, cutoff)
    coefficients = list(multiply(u_power, q_power, prime, cutoff))
    coefficients += [0] * (cutoff + 1 - len(coefficients))
    a1 = coefficients[layer - 1]
    b1 = coefficients[2 * layer - 1]
    a0 = sum(coefficients[layer - 1 - index] for index in range(4)) % prime
    b0 = sum(
        coefficients[2 * layer - 1 - index] for index in range(4)
    ) % prime
    determinant = (a0 * b1 - b0 * a1) % prime
    return a0, b0, a1, b1, determinant


def rank_two_row(m_value: int, prime: int) -> dict[str, int | bool] | None:
    exponent, layer = top_prime_power(prime, 4 * m_value + 1)
    if layer < 5:
        return None
    a_value, remainder = divmod(6 * m_value, layer)
    b_value, t_value = divmod(4 * m_value + 1, layer)
    delta = 2 * a_value - 3 * b_value
    if delta != 0:
        return None
    if not (t_value > 0 and 2 * remainder == 3 * (t_value - 1)):
        raise AssertionError((m_value, prime, layer, remainder, t_value))
    if remainder % 3:
        raise AssertionError((m_value, prime, layer, remainder))
    residual_index = remainder // 3
    if t_value != 2 * residual_index + 1:
        raise AssertionError((m_value, prime, layer, residual_index, t_value))
    a0, b0, a1, b1, determinant = determinant_coefficients(
        prime, layer, residual_index
    )
    return {
        "p": prime,
        "denominator_exponent": exponent,
        "top_prime_power_layer": layer,
        "floor_a": a_value,
        "floor_b": b_value,
        "residual_index": residual_index,
        "a0": a0,
        "b0": b0,
        "a1": a1,
        "b1": b1,
        "determinant": determinant,
        "vanishes": determinant == 0,
        "rank_zero_at_first_cartier": (
            d_value(6 * m_value, 4 * m_value + 1, prime) <= prime - 2
            and d_value(6 * m_value, 4 * m_value + 2, prime) <= prime - 2
        ),
    }


def degree_classification_check(m_value: int, prime: int) -> bool:
    _, layer = top_prime_power(prime, 4 * m_value + 1)
    if layer < 5:
        return True
    a_value = (6 * m_value) // layer
    b_value, t_value = divmod(4 * m_value + 1, layer)
    delta = 2 * a_value - 3 * b_value
    d0 = d_value(6 * m_value, 4 * m_value + 1, layer)
    d1 = d_value(6 * m_value, 4 * m_value + 2, layer)
    rank_two_equivalence = (
        d0 <= 3 * layer - 2 and d1 <= 3 * layer - 2
    ) == (t_value > 0 and delta >= 0)
    rank_one_equivalence = (
        d0 <= 2 * layer - 2 and d1 <= 2 * layer - 2
    ) == (t_value > 0 and delta >= 1)
    return rank_two_equivalence and rank_one_equivalence


def ray_labels(prime: int, residual_index: int) -> list[str]:
    labels = []
    if prime == 3 * residual_index + 4:
        labels.append("p=3s+4")
    if prime == 5 * residual_index + 2 and residual_index % 4 == 1:
        labels.append("p=5s+2,s=1(mod4)")
    if prime == 5 * residual_index + 1 and residual_index % 4 == 2:
        labels.append("p=5s+1,s=2(mod4)")
    return labels


def fixed_s_zero_integer(prime: int, residual_index: int) -> int:
    if residual_index == 0:
        if prime % 4 == 1:
            return -(3 * prime + 1) // 4
        return (prime + 1) // 4
    if residual_index == 1:
        if prime % 4 == 1:
            value = Fraction(
                -7
                * (prime - 1) ** 2
                * (2 * prime**3 + 2 * prime**2 + 15 * prime + 9),
                192,
            )
        else:
            value = Fraction(
                -(prime - 3)
                * (prime - 1)
                * (prime + 1)
                * (34 * prime**2 - 20 * prime - 21),
                192,
            )
    elif residual_index == 2:
        if prime % 4 == 1:
            value = Fraction(
                -11
                * (prime - 5)
                * (prime - 3)
                * (prime - 1) ** 2
                * (
                    99 * prime**5
                    - 665 * prime**4
                    - 1203 * prime**3
                    + 7853 * prime**2
                    + 9552 * prime
                    + 1980
                ),
                92160,
            )
        else:
            value = Fraction(
                -(prime - 3) ** 2
                * (prime - 1)
                * (prime + 1)
                * (
                    1023 * prime**5
                    - 8233 * prime**4
                    + 3493 * prime**3
                    + 22297 * prime**2
                    + 51680 * prime
                    + 36300
                ),
                92160,
            )
    else:
        raise ValueError(residual_index)
    if value.denominator != 1:
        raise AssertionError((prime, residual_index, value))
    return value.numerator


def load_records(
    scan: Path, probes: list[Path]
) -> tuple[dict[int, dict[str, object]], list[dict[str, str]]]:
    records: dict[int, dict[str, object]] = {}
    dependencies = []
    scan_data = json.loads(scan.read_text(encoding="utf-8"))
    for row in scan_data["rows"]:
        records[int(row["m"])] = {
            "content": int(row["extra_content"]),
            "u": int(row["U"]["value"]),
            "v": int(row["V"]["value"]),
        }
    dependencies.append({"filename": scan.name, "sha256": sha256(scan)})
    for probe in probes:
        probe_data = json.loads(probe.read_text(encoding="utf-8"))
        for row in probe_data["rows"]:
            records[int(row["m"])] = {
                "content": int(row["content"]),
                "vp_map": row["vp_u_minus_vp_cartier_for_small_primes"],
            }
        dependencies.append({"filename": probe.name, "sha256": sha256(probe)})
    return records, dependencies


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scan",
        type=Path,
        default=ARCHIVE
        / "results"
        / "mixed_cubic_positive_match_exact_scan_m100_N6m.json",
    )
    parser.add_argument(
        "--probe",
        type=Path,
        action="append",
        default=None,
        help="Optional exact factor-probe JSON; may be repeated.",
    )
    parser.add_argument(
        "--identity-prime-limit",
        type=int,
        default=401,
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ARCHIVE
        / "results"
        / "mixed_cubic_rank_two_cartier_certificate.json",
    )
    args = parser.parse_args()
    probes = args.probe or [
        ARCHIVE / "results" / "mixed_cubic_content_factor_m150.json",
        ARCHIVE / "results" / "mixed_cubic_content_factor_m200.json",
    ]
    records, dependencies = load_records(args.scan, probes)

    index_rows = []
    total_delta_zero = 0
    total_vanishing = 0
    total_vanishing_rank_zero = 0
    all_divisibility_checks_pass = True
    all_valuation_checks_pass = True
    all_degree_classification_checks_pass = True
    for m_value in sorted(records):
        record = records[m_value]
        content = int(record["content"])
        delta_zero_rows = []
        for prime in primes_upto(2 * m_value - 1):
            if prime == 2:
                continue
            all_degree_classification_checks_pass &= degree_classification_check(
                m_value, prime
            )
            row = rank_two_row(m_value, prime)
            if row is None:
                continue
            total_delta_zero += 1
            if not bool(row["vanishes"]):
                continue
            total_vanishing += 1
            total_vanishing_rank_zero += bool(row["rank_zero_at_first_cartier"])
            exponent = int(row["denominator_exponent"])
            if "u" in record:
                vp_u = valuation(int(record["u"]), prime)
                vp_v = valuation(int(record["v"]), prime)
            else:
                vp_u, vp_v = map(int, record["vp_map"][str(prime)])
            divides = content % prime == 0
            valuation_check = vp_u >= 1 and vp_v >= exponent + 1
            all_divisibility_checks_pass &= divides
            all_valuation_checks_pass &= valuation_check
            row["ray_labels"] = ray_labels(prime, int(row["residual_index"]))
            row["divides_post_G_content"] = divides
            row["vp_u"] = vp_u
            row["vp_v"] = vp_v
            row["proved_lower_bounds_hold"] = valuation_check
            delta_zero_rows.append(row)
        index_rows.append(
            {
                "m": m_value,
                "vanishing_rank_two_rows": delta_zero_rows,
            }
        )

    identity_rows = []
    all_fixed_s_checks_pass = True
    all_ray_checks_pass = True
    for prime in primes_upto(args.identity_prime_limit):
        if prime < 5:
            continue
        for residual_index in (0, 1, 2):
            if residual_index > (prime - 1) // 3:
                continue
            coefficients = determinant_coefficients(prime, prime, residual_index)
            predicted = fixed_s_zero_integer(prime, residual_index)
            agrees = coefficients[-1] == predicted % prime
            expected_nonzero = (
                residual_index == 0
                or (residual_index == 1 and prime != 7)
                or (residual_index == 2 and prime != 11)
            )
            nonzero_check = (coefficients[-1] != 0) == expected_nonzero
            all_fixed_s_checks_pass &= agrees and nonzero_check
            identity_rows.append(
                {
                    "p": prime,
                    "s": residual_index,
                    "determinant_mod_p": coefficients[-1],
                    "predicted_integer_determinant": predicted,
                    "formula_agrees_mod_p": agrees,
                    "expected_nonzero_check": nonzero_check,
                }
            )

        possible_ray_indices = {
            (prime - 4) // 3 if (prime - 4) % 3 == 0 else -1,
            (prime - 2) // 5 if (prime - 2) % 5 == 0 else -1,
            (prime - 1) // 5 if (prime - 1) % 5 == 0 else -1,
        }
        for residual_index in sorted(possible_ray_indices):
            if not (0 <= residual_index <= (prime - 1) // 3):
                continue
            labels = ray_labels(prime, residual_index)
            if not labels:
                continue
            a0, b0, a1, b1, determinant = determinant_coefficients(
                prime, prime, residual_index
            )
            vanishing_check = determinant == 0
            structural_checks = []
            if "p=5s+2,s=1(mod4)" in labels:
                structural_checks.append(a1 == 0 and b1 == 0)
            if "p=5s+1,s=2(mod4)" in labels:
                structural_checks.append(b0 == 0 and b1 == 0)
            structural_check = all(structural_checks)
            all_ray_checks_pass &= vanishing_check and structural_check
            identity_rows.append(
                {
                    "p": prime,
                    "s": residual_index,
                    "ray_labels": labels,
                    "coefficients": [a0, b0, a1, b1],
                    "ray_vanishing_check": vanishing_check,
                    "ray_structural_check": structural_check,
                }
            )

    payload = {
        "schema": "mixed-cubic-rank-two-cartier-certificate-v1",
        "scope": {
            "exact_coordinate_indices": sorted(records),
            "identity_prime_limit": args.identity_prime_limit,
            "finite_audit_only": True,
        },
        "dependencies": dependencies,
        "summary": {
            "exact_coordinate_index_count": len(records),
            "delta_zero_row_count": total_delta_zero,
            "vanishing_rank_two_row_count": total_vanishing,
            "vanishing_rows_already_rank_zero_at_first_cartier": (
                total_vanishing_rank_zero
            ),
            "all_divisibility_checks_pass": all_divisibility_checks_pass,
            "all_valuation_checks_pass": all_valuation_checks_pass,
            "all_degree_classification_checks_pass": (
                all_degree_classification_checks_pass
            ),
            "all_fixed_s_formula_checks_pass": all_fixed_s_checks_pass,
            "all_explicit_ray_checks_pass": all_ray_checks_pass,
            "failure_count": sum(
                not check
                for check in (
                    all_divisibility_checks_pass,
                    all_valuation_checks_pass,
                    all_degree_classification_checks_pass,
                    all_fixed_s_checks_pass,
                    all_ray_checks_pass,
                )
            ),
        },
        "index_rows": index_rows,
        "identity_rows": identity_rows,
    }
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
