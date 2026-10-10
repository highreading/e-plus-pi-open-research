#!/usr/bin/env python3
"""Finite exact regression checks for the local zero-run no-go theorem."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def valuation_nonzero(value: int, prime: int) -> int:
    assert value
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def check_case(
    prime: int, residue: int, positions: list[int], precision: int
) -> dict[str, object]:
    assert (2 * residue + 1) % prime
    assert positions == sorted(set(positions))
    assert positions and positions[0] >= 1 and positions[-1] < precision
    modulus = prime**precision
    rho = (residue + sum(prime**position for position in positions)) % modulus

    def function(x: int) -> int:
        return (x * (x + 1) - rho * (rho + 1)) % modulus

    prefix_records = []
    for j in range(len(positions) - 1):
        prefix = residue + sum(
            prime**position for position in positions[: j + 1]
        )
        value = function(prefix)
        valuation = valuation_nonzero(value, prime)
        assert valuation == positions[j + 1]
        prefix_records.append(
            {
                "prefix_number": prefix,
                "last_nonzero_digit_position": positions[j],
                "next_nonzero_digit_position": positions[j + 1],
                "terminal_zero_run_length": (
                    positions[j + 1] - positions[j] - 1
                ),
                "function_valuation": valuation,
            }
        )

    # Exact reflection and translation checks modulo p^precision.
    reflection_checks = 0
    translation_checks = 0
    for x in [0, 1, residue, prime + residue, prime**2 + 3]:
        assert function(-x - 1) == function(x)
        reflection_checks += 1
        for exponent in range(1, min(5, precision // 2) + 1):
            step = prime**exponent
            for multiplier in [1, 2, prime - 1]:
                translated = function(x + multiplier * step)
                affine = (
                    function(x)
                    + multiplier * step * (2 * x + 1)
                    + multiplier**2 * step**2
                ) % modulus
                assert translated == affine
                assert (
                    function(x + 2 * step)
                    - 2 * function(x + step)
                    + function(x)
                    - 2 * step**2
                ) % modulus == 0
                translation_checks += 1

    derivative_at_root = (2 * rho + 1) % prime
    assert derivative_at_root == (2 * residue + 1) % prime
    assert derivative_at_root
    return {
        "prime": prime,
        "base_residue": residue,
        "nonzero_digit_positions": positions,
        "precision": precision,
        "root_residue_mod_precision": rho,
        "derivative_at_root_mod_p": derivative_at_root,
        "prefix_records": prefix_records,
        "reflection_checks": reflection_checks,
        "translation_checks": translation_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/bessel_padic_local_zero_run_no_go_certificate.json"
        ),
    )
    args = parser.parse_args()
    records = [
        check_case(3, 0, [2, 9, 31], 40),
        check_case(5, 1, [1, 8, 43], 50),
        check_case(7, 2, [3, 17, 61], 70),
        check_case(11, 3, [2, 13, 57], 65),
    ]
    result = {
        "theorem_scope": (
            "local analytic/reflection/affine-lift properties only"
        ),
        "cases": records,
        "warning": (
            "These comparison functions do not satisfy the Bessel "
            "difference equation and do not have rational global "
            "coefficient height."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
