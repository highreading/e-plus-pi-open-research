#!/usr/bin/env python3
"""Finite exact checks for the central singular zero-run dichotomy."""

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


def digits_base(number: int, prime: int) -> list[int]:
    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(number % prime)
        number //= prime
    return digits


def model_record(prime: int, multiplicity: int, unit_power: int) -> dict:
    assert prime % 2 and multiplicity >= 2 and multiplicity % 2 == 0
    rows = []
    digit = (prime - 1) // 2
    for exponent in range(1, 13):
        n = (prime**exponent - 1) // 2
        digits = digits_base(n, prime)
        assert digits == [digit] * exponent

        # Clear the harmless denominator 2^multiplicity.  The local model
        # is p^unit_power*(x+1/2)^multiplicity.
        cleared_value = (
            prime**unit_power * (2 * n + 1) ** multiplicity
        )
        valuation = valuation_nonzero(cleared_value, prime)
        expected = multiplicity * exponent + unit_power
        assert valuation == expected
        rows.append(
            {
                "digit_depth": exponent,
                "integer_truncation": n,
                "valuation": valuation,
                "terminal_zero_run_length": valuation - exponent,
            }
        )
    return {
        "prime": prime,
        "even_multiplicity": multiplicity,
        "unit_valuation": unit_power,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/"
            "bessel_padic_central_singular_zero_run_dichotomy_certificate.json"
        ),
    )
    args = parser.parse_args()
    result = {
        "description": (
            "Exact synthetic regression checks for the valuation law at "
            "an even-multiplicity central p-adic zero."
        ),
        "models": [
            model_record(3, 2, 0),
            model_record(5, 4, 1),
            model_record(7, 6, 0),
            model_record(11, 2, 3),
        ],
        "scope_warning": (
            "These are local analytic models. They do not assert that "
            "the Bessel interpolation vanishes at -1/2 for any prime."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
