#!/usr/bin/env python3
"""Exact finite replay for the post-Cartier rank-one small-prime divisor.

The theorem proved in the companion note is uniform.  This script only
checks its exact divisor against frozen coordinate data; it does not infer
the theorem or its asymptotic from the finite table.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
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


def d_value(n_value: int, power: int, prime: int) -> int:
    remainder_n = n_value % prime
    remainder_k = power % prime
    if remainder_k == 0:
        return 2 * remainder_n
    return 2 * remainder_n + 3 * (prime - remainder_k)


def forced_primes(m_value: int) -> list[dict[str, int | bool]]:
    n_value = 6 * m_value
    power = 4 * m_value + 1
    rows = []
    for prime in primes_upto(2 * m_value - 1):
        if prime == 2:
            continue
        exponent = 1
        layer = prime
        while layer * prime <= power:
            layer *= prime
            exponent += 1
        d0 = d_value(n_value, power, layer)
        d1 = d_value(n_value, power + 1, layer)
        if d0 <= 2 * layer - 2 and d1 <= 2 * layer - 2:
            first_d0 = d_value(n_value, power, prime)
            first_d1 = d_value(n_value, power + 1, prime)
            rows.append(
                {
                    "p": prime,
                    "denominator_exponent": exponent,
                    "top_prime_power_layer": layer,
                    "d0": d0,
                    "d1": d1,
                    "rank_zero_certified": (
                        first_d0 <= prime - 2 and first_d1 <= prime - 2
                    ),
                    "top_layer_zero_by_degree": (
                        d0 <= layer - 2 and d1 <= layer - 2
                    ),
                }
            )
    return rows


def integer_digest(value: int) -> dict[str, int | str]:
    encoded = str(value).encode("ascii")
    return {
        "decimal_digits": len(encoded),
        "bit_length": value.bit_length(),
        "sha256_decimal": hashlib.sha256(encoded).hexdigest(),
    }


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def load_contents(
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
        data = json.loads(probe.read_text(encoding="utf-8"))
        for row in data["rows"]:
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
        "--output",
        type=Path,
        default=ARCHIVE
        / "results"
        / "mixed_cubic_small_prime_rank_one_cartier_certificate.json",
    )
    args = parser.parse_args()
    probes = args.probe or [
        ARCHIVE / "results" / "mixed_cubic_content_factor_m150.json",
        ARCHIVE / "results" / "mixed_cubic_content_factor_m200.json",
    ]
    records, dependencies = load_contents(args.scan, probes)
    rows = []
    for m_value in sorted(records):
        record = records[m_value]
        content = int(record["content"])
        local_rows = forced_primes(m_value)
        divisor = math.prod(int(row["p"]) for row in local_rows)
        quotient, remainder = divmod(content, divisor)
        valuation_checks = []
        for local in local_rows:
            prime = int(local["p"])
            exponent = int(local["denominator_exponent"])
            if "u" in record:
                vp_u = valuation(abs(int(record["u"])), prime)
                vp_v = valuation(abs(int(record["v"])), prime)
            else:
                vp_u, vp_v = map(int, record["vp_map"][str(prime)])
            valuation_checks.append(
                {
                    "p": prime,
                    "vp_u": vp_u,
                    "vp_v": vp_v,
                    "proved_lower_bounds_hold": vp_u >= 1 and vp_v >= exponent + 1,
                }
            )
        rows.append(
            {
                "m": m_value,
                "forced_primes": local_rows,
                "forced_prime_count": len(local_rows),
                "forced_divisor": str(divisor),
                "forced_divisor_digest": integer_digest(divisor),
                "content_digest": integer_digest(content),
                "content_divided_by_forced_divisor_digest": (
                    integer_digest(quotient) if remainder == 0 else None
                ),
                "divides_exact_content": remainder == 0,
                "sharp_normalized_valuation_checks": valuation_checks,
                "all_sharp_normalized_valuation_bounds_hold": all(
                    bool(check["proved_lower_bounds_hold"])
                    for check in valuation_checks
                ),
                "log_forced_divisor_per_m": (
                    math.log(divisor) / m_value if divisor > 1 else 0.0
                ),
                "log_forced_divisor_per_6m": (
                    math.log(divisor) / (6 * m_value) if divisor > 1 else 0.0
                ),
            }
        )
    constant_per_m = -4 * math.log(2) + 6 * math.log(3) - 3
    threshold = 1.1561471519642446
    payload = {
        "schema": "mixed-cubic-small-prime-rank-one-cartier-v1",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": sha256(Path(__file__)),
        },
        "dependencies": dependencies,
        "exact_checked_indices": sorted(records),
        "all_forced_divisors_divide_exact_content": all(
            bool(row["divides_exact_content"]) for row in rows
        ),
        "all_sharp_normalized_valuation_bounds_hold": all(
            bool(row["all_sharp_normalized_valuation_bounds_hold"])
            for row in rows
        ),
        "theorem_constants": {
            "symbolic_per_m": "-4*log(2)+6*log(3)-3",
            "per_m": constant_per_m,
            "per_6m": constant_per_m / 6,
            "matching_threshold_per_6m": threshold,
            "remaining_deficit_per_6m": threshold - constant_per_m / 6,
        },
        "warning": (
            "Finite exact replay only. The all-m divisor and PNT limit are "
            "proved in the companion note, not extrapolated from these rows."
        ),
        "rows": rows,
    }
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded).hexdigest(),
                "checked_count": len(rows),
                "all_divide": payload["all_forced_divisors_divide_exact_content"],
                "constants": payload["theorem_constants"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
