"""Exact diagnostics for the beta Bessel-period congruence.

The all-degree proof is in
sources/exponential_beta_bessel_period_congruence.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def pairs(maximum: int) -> tuple[list[int], list[int]]:
    p_values = [1, 3]
    q_values = [1, 1]
    for n in range(2, maximum + 1):
        multiplier = 2 * (2 * n - 1)
        p_values.append(multiplier * p_values[-1] + p_values[-2])
        q_values.append(multiplier * q_values[-1] + q_values[-2])
    return p_values, q_values


def sha256_records(records: list[tuple[int, ...]]) -> str:
    text = "\n".join(",".join(str(value) for value in row) for row in records)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def pair_residues(maximum: int, modulus: int) -> tuple[list[int], list[int]]:
    p_values = [1 % modulus, 3 % modulus]
    q_values = [1 % modulus, 1 % modulus]
    for n in range(2, maximum + 1):
        multiplier = 2 * (2 * n - 1)
        p_values.append(
            (multiplier * p_values[-1] + p_values[-2]) % modulus
        )
        q_values.append(
            (multiplier * q_values[-1] + q_values[-2]) % modulus
        )
    return p_values, q_values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/exponential_beta_bessel_period_congruence.json"
        ),
    )
    arguments = parser.parse_args()

    maximum_modulus = 160
    maximum_shift = 320
    p_values, q_values = pairs(maximum_modulus + maximum_shift)
    records: list[tuple[int, ...]] = []
    for modulus in range(1, maximum_modulus + 1):
        sign = -1 if modulus % 2 else 1
        assert p_values[modulus] % modulus == 1 % modulus
        assert p_values[modulus + 1] % modulus == 3 % modulus
        assert q_values[modulus] % modulus == sign % modulus
        assert q_values[modulus + 1] % modulus == sign % modulus
        for n in range(maximum_shift + 1):
            p_residue = (p_values[n + modulus] - p_values[n]) % modulus
            q_residue = (
                q_values[n + modulus] - sign * q_values[n]
            ) % modulus
            assert p_residue == 0 and q_residue == 0
            records.append(
                (modulus, n, p_residue, q_residue)
            )

    prime_power_examples: list[dict[str, int]] = []
    for prime, exponent, n in (
        (7, 1, 2),
        (13, 2, 8),
        (7, 3, 18),
        (7, 4, 361),
        (11, 5, 1359),
    ):
        modulus = prime**exponent
        needed = n + modulus
        p_extended, q_extended = pair_residues(needed, modulus)
        assert q_extended[n] % modulus == 0
        assert q_extended[n + modulus] % modulus == 0
        assert (
            p_extended[n + modulus] - p_extended[n]
        ) % modulus == 0
        prime_power_examples.append(
            {
                "prime": prime,
                "exponent": exponent,
                "modulus": modulus,
                "root_index": n,
                "shifted_root_index": n + modulus,
            }
        )

    output = {
        "description": (
            "Exact finite diagnostics for p_(n+m)=p_n and "
            "q_(n+m)=(-1)^m q_n modulo m"
        ),
        "maximum_modulus": maximum_modulus,
        "maximum_shift": maximum_shift,
        "checked_pair_count": len(records),
        "record_sha256": sha256_records(records),
        "prime_power_examples": prime_power_examples,
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
