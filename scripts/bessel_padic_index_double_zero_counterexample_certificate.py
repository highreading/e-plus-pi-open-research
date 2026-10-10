#!/usr/bin/env python3
"""Exact certificate for a double-zero Bessel index-Hensel lift.

The sequence is
    q_0=q_1=1, q_n=(4n-2)q_{n-1}+q_{n-2}.

For f(n)=(-1)^n q_n, let A_j=Delta^j f(0).  The Newton series
f(x)=sum_j A_j binom(x,j) permits exact evaluation at a very large
integer modulo 7^60, because all A_j past an explicit cutoff vanish
modulo 7^60.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import resource
import sys
import time
from pathlib import Path


PRIME = 7
EXPONENT = 60
CUTOFF = 2 * PRIME * (EXPONENT + 2)
INDEX = 464838342618219576262104570205987685961890202821


def q_values(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values[: limit + 1]


def mahler_recurrence(limit: int) -> list[int]:
    values = [1, -2]
    for j in range(limit - 1):
        previous = values[j - 1] if j else 0
        values.append(
            -4 * (j + 2) * values[j + 1]
            - (8 * j + 6) * values[j]
            - 4 * j * previous
        )
    return values[: limit + 1]


def mahler_closed(limit: int) -> list[int]:
    factorials = [math.factorial(j) for j in range(limit + 1)]
    values: list[int] = []
    for j in range(limit + 1):
        inner = sum(
            (-1) ** m
            * (factorials[j] // factorials[m])
            * math.comb(2 * j - 2 * m, j)
            for m in range(j // 2 + 1)
        )
        values.append((-1) ** j * inner)
    return values


def newton_value_direct(
    x: int, coefficients: list[int], modulus: int
) -> int:
    return sum(
        (coefficient % modulus) * (math.comb(x, j) % modulus)
        for j, coefficient in enumerate(coefficients)
    ) % modulus


def newton_value_padic_binomial(
    x: int,
    coefficients: list[int],
    prime: int,
    exponent: int,
) -> int:
    """Evaluate with a p-unit/valuation recurrence for binom(x,j)."""
    modulus = prime**exponent
    total = coefficients[0] % modulus
    unit = 1
    valuation = 0
    powers = [1]
    for _ in range(exponent):
        powers.append(powers[-1] * prime)

    for j in range(1, len(coefficients)):
        numerator = x - j + 1
        denominator = j
        if numerator == 0:
            break
        while numerator % prime == 0:
            valuation += 1
            numerator //= prime
        while denominator % prime == 0:
            valuation -= 1
            denominator //= prime
        assert valuation >= 0
        unit *= numerator % modulus
        unit %= modulus
        unit *= pow(denominator, -1, modulus)
        unit %= modulus
        binomial = 0 if valuation >= exponent else unit * powers[valuation] % modulus
        total += (coefficients[j] % modulus) * binomial
        total %= modulus
    return total


def base_digits(value: int, base: int) -> list[int]:
    digits = []
    while value:
        digits.append(value % base)
        value //= base
    return digits or [0]


def sha256_integer_vector(values: list[int]) -> str:
    payload = "".join(f"{value}\n" for value in values).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/bessel_padic_index_double_zero_counterexample_certificate.json"
        ),
    )
    args = parser.parse_args()
    started = time.perf_counter()

    p = PRIME
    k = EXPONENT
    modulus = p**k

    # Two independent constructions of every Mahler coefficient used in
    # the modular evaluation.
    recurrence_coefficients = mahler_recurrence(CUTOFF)
    closed_coefficients = mahler_closed(CUTOFF)
    assert recurrence_coefficients == closed_coefficients

    # Check the finite-difference definition against ordinary recurrence
    # values at a nontrivial initial range.
    check_limit = 80
    q_initial = q_values(check_limit)
    for j in range(check_limit + 1):
        finite_difference = sum(
            (-1) ** (j - n)
            * math.comb(j, n)
            * (-1) ** n
            * q_initial[n]
            for n in range(j + 1)
        )
        assert finite_difference == recurrence_coefficients[j]

    # Divisibility certificate used to discard the infinite tail.  The
    # exact closed formula gives (j!/floor(j/2)!) | A_j.  At the first
    # omitted index, already the multiples of 7 in the upper half supply
    # more than k factors of 7; the elementary lower bound increases
    # thereafter.
    first_omitted = CUTOFF + 1
    first_level_lower_bound = (
        first_omitted // p - (first_omitted // 2) // p
    )
    assert first_level_lower_bound >= k
    assert first_omitted / (2 * p) - 1 > k

    # Evaluate f(INDEX) modulo 7^60 in two arithmetically distinct ways.
    f_direct = newton_value_direct(INDEX, recurrence_coefficients, modulus)
    f_padic = newton_value_padic_binomial(
        INDEX, recurrence_coefficients, p, k
    )
    assert f_direct == f_padic == 5 * p ** (k - 1)

    # INDEX is odd, so f(INDEX)=-q_INDEX.  Hence q_INDEX/7^59 == 2 mod 7.
    assert INDEX % 2 == 1
    q_residue = (-f_direct) % modulus
    assert q_residue == 2 * p ** (k - 1)

    # The next ordinary Hensel digit is 6.  It kills the nonzero quotient
    # at level 60.  This also checks the digit orientation independently.
    next_digit = 6
    next_representative = INDEX + next_digit * p ** (k - 1)
    f_next_direct = newton_value_direct(
        next_representative, recurrence_coefficients, modulus
    )
    f_next_padic = newton_value_padic_binomial(
        next_representative, recurrence_coefficients, p, k
    )
    assert f_next_direct == f_next_padic == 0

    digits = base_digits(INDEX, p)
    assert len(digits) == 57
    assert digits[0] == 2 and digits[-1] == 2
    assert p**56 < INDEX < p**57
    # Appending the level-57 and level-58 lift digits 0 leaves the same
    # least representative modulo 7^58 and 7^59.
    lifted_digits = digits + [0, 0, next_digit]
    assert sum(d * p**j for j, d in enumerate(lifted_digits)) == next_representative

    # The base root is ordinary in the exact anti-period normalization.
    q_small = q_values(9)
    delta_7_at_2 = ((-q_small[9] - q_small[2]) // p) % p
    assert q_small[2] == p
    assert delta_7_at_2 == 5

    elapsed = time.perf_counter() - started
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result = {
        "sequence": {
            "q_0": 1,
            "q_1": 1,
            "recurrence": "q_n=(4*n-2)*q_(n-1)+q_(n-2)",
            "newton_function": "f(n)=(-1)^n*q_n",
        },
        "counterexample": {
            "prime": p,
            "index": INDEX,
            "index_base_7_digits_least_significant_first": digits,
            "index_between_powers": [56, 57],
            "ceil_log_p_index": 57,
            "valuation_q_index": 59,
            "claimed_upper_bound_1_plus_ceil_log": 58,
            "ordinary_base_root": 2,
            "ordinary_delta_mod_p": delta_7_at_2,
            "zero_lift_digit_positions": [57, 58],
            "next_lift_digit_position": 59,
            "next_lift_digit": next_digit,
            "next_representative_mod_p60": next_representative,
        },
        "exact_modular_evaluation": {
            "modulus_exponent": k,
            "modulus": modulus,
            "f_index_residue": f_direct,
            "f_index_quotient_mod_p": 5,
            "q_index_residue": q_residue,
            "q_index_quotient_mod_p": 2,
            "f_next_representative_residue": f_next_direct,
        },
        "mahler_certificate": {
            "cutoff_inclusive": CUTOFF,
            "first_omitted_index": first_omitted,
            "first_level_valuation_lower_bound_at_first_omitted": first_level_lower_bound,
            "coefficient_count": len(recurrence_coefficients),
            "recurrence_equals_closed_formula": True,
            "finite_difference_checks_through": check_limit,
            "direct_binomial_equals_padic_unit_evaluation": True,
            "exact_coefficient_vector_sha256": sha256_integer_vector(
                recurrence_coefficients
            ),
            "coefficient_residue_vector_sha256": sha256_integer_vector(
                [value % modulus for value in recurrence_coefficients]
            ),
        },
        "scope": {
            "disproves": "v_p(q_n)<=1+ceil(log_p(n))",
            "does_not_disprove": "V_N(C)=o(N*log(N))",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    print(
        f"elapsed_seconds={elapsed:.6f} peak_rss_kib={peak_rss_kib}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
