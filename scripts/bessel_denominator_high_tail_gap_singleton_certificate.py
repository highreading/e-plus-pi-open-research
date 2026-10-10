#!/usr/bin/env python3
"""Exact certificate for the Bessel high-tail gap/singleton reduction.

The sequence is
    q_0=q_1=1, q_n=(4n-2)q_{n-1}+q_{n-2}.

All calculations are integer or modular-integer calculations.  The finite
checks support (but are not substitutes for) the algebraic proofs in the
companion note.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path


def q_values_exact(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values[: limit + 1]


def q_values_mod(limit: int, modulus: int) -> list[int]:
    values = [1 % modulus, 1 % modulus]
    for n in range(2, limit + 1):
        values.append(((4 * n - 2) * values[-1] + values[-2]) % modulus)
    return values[: limit + 1]


def gap_value(n: int, d: int) -> int:
    """Evaluate P_d(n), with P_0=0, P_1=1."""
    if d == 0:
        return 0
    previous, current = 0, 1
    for j in range(d - 1):
        previous, current = current, (4 * n + 4 * j + 6) * current + previous
    return current


def valuation_from_modular_recurrence(n: int, prime: int, max_exponent: int) -> int:
    modulus = prime ** max_exponent
    residue = q_values_mod(n, modulus)[n]
    exponent = 0
    while residue % prime == 0:
        residue //= prime
        exponent += 1
    return exponent


def lift_record(prime: int, root_index: int, exponent: int) -> dict[str, object]:
    modulus = prime**exponent
    child_modulus = modulus * prime
    representative = root_index % modulus
    largest_index = representative + (prime - 1) * modulus
    values = q_values_mod(largest_index, child_modulus)
    child_residues = [
        values[representative + digit * modulus] for digit in range(prime)
    ]
    root_digits = [digit for digit, value in enumerate(child_residues) if value == 0]
    return {
        "level_exponent": exponent,
        "modulus": modulus,
        "representative": representative,
        "child_modulus": child_modulus,
        "child_residues_mod_child_modulus": child_residues,
        "root_digits": root_digits,
        "number_of_children": len(root_digits),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/bessel_denominator_high_tail_gap_singleton_certificate.json"),
    )
    args = parser.parse_args()

    # Exact finite audit of the continuant identity and gcd identity.
    exact_limit = 90
    q_exact = q_values_exact(exact_limit)
    continuant_checks = 0
    gcd_checks = 0
    bound_checks = 0
    for n in range(0, 46):
        for d in range(1, 46 - n):
            p_d = gap_value(n, d)
            p_previous_shifted = gap_value(n + 1, d - 1)
            assert q_exact[n + d] == p_d * q_exact[n + 1] + p_previous_shifted * q_exact[n]
            continuant_checks += 1
            assert gcd(q_exact[n], q_exact[n + d]) == gcd(q_exact[n], p_d)
            gcd_checks += 1
            assert p_d <= (4 * (n + d)) ** (d - 1)
            bound_checks += 1

    for n in range(exact_limit):
        assert gcd(q_exact[n], q_exact[n + 1]) == 1

    # The ordinary high-tail chain at p=11, n=1359.
    prime = 11
    index = 1359
    valuation = valuation_from_modular_recurrence(index, prime, 6)
    assert valuation == 5
    residue_mod_p6 = q_values_mod(index, prime**6)[index]
    assert residue_mod_p6 == 3 * prime**5

    lift_records = [lift_record(prime, index, exponent) for exponent in range(1, 6)]
    expected_digits = [2, 0, 1, 0, 8]
    for record, expected_digit in zip(lift_records, expected_digits):
        assert record["number_of_children"] == 1
        assert record["root_digits"] == [expected_digit]

    # First-level slope is nonzero, independently checking that this is not
    # an all-p branch already at the first lift.
    p2_values = q_values_mod(6 + prime, prime**2)
    q_6_mod_p2 = p2_values[6]
    q_17_mod_p2 = p2_values[17]
    delta = ((-q_17_mod_p2 - q_6_mod_p2) // prime) % prime
    assert q_6_mod_p2 == 22
    assert q_17_mod_p2 == 110
    assert delta == 10

    averaging_start = 1359
    threshold_exponent = 2
    while prime**threshold_exponent <= averaging_start:
        threshold_exponent += 1
    tail_levels = valuation - threshold_exponent + 1
    assert threshold_exponent == 4
    assert tail_levels == 2

    # At the first high level, this prime occurs at exactly one index of the
    # selected interval.  Thus its entire high-tail contribution is in the
    # singleton-max term, not in any pairwise gap term.
    first_high_modulus = prime**threshold_exponent
    interval_values = q_values_mod(2 * averaging_start - 1, first_high_modulus)
    high_level_indices = [
        n
        for n in range(averaging_start, 2 * averaging_start)
        if interval_values[n] == 0
    ]
    assert high_level_indices == [index]

    # A second, very small ordinary-square representative.
    prime_13 = 13
    q_8 = q_values_exact(8)[8]
    assert q_8 == 312129649
    assert q_8 % (prime_13**2) == 0
    assert q_8 % (prime_13**3) != 0
    p13_values = q_values_mod(8 + prime_13, prime_13**2)
    delta_13 = ((-p13_values[21] - p13_values[8]) // prime_13) % prime_13
    assert delta_13 == 1

    data: dict[str, object] = {
        "description": "Exact finite checks for the Bessel high-tail gap/singleton reduction",
        "finite_identity_audit": {
            "exact_q_limit": exact_limit,
            "continuant_identity_checks": continuant_checks,
            "gcd_identity_checks": gcd_checks,
            "gap_upper_bound_checks": bound_checks,
            "consecutive_gcd_checks": exact_limit,
        },
        "ordinary_high_tail_example": {
            "averaging_interval": [averaging_start, 2 * averaging_start - 1],
            "prime": prime,
            "index": index,
            "valuation": valuation,
            "q_index_mod_prime_to_6": residue_mod_p6,
            "first_tail_exponent": threshold_exponent,
            "tail_level_count": tail_levels,
            "indices_divisible_at_first_tail_level": high_level_indices,
            "first_level_delta_mod_prime": delta,
            "lift_records": lift_records,
        },
        "ordinary_square_example": {
            "prime": prime_13,
            "index": 8,
            "q_index": q_8,
            "valuation": 2,
            "first_level_delta_mod_prime": delta_13,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, indent=2, sort_keys=True) + "\n"
    args.output.write_text(payload, encoding="utf-8")
    print(hashlib.sha256(payload.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
