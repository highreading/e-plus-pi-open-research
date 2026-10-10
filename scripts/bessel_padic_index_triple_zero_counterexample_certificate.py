#!/usr/bin/env python3
"""Exact certificate for three consecutive zero index-Hensel digits.

The calculation uses the proved Mahler recurrence for
f(n)=(-1)^n q_n and an explicit coefficient-divisibility cutoff.
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
EXPONENT = 1172
CUTOFF = 2 * PRIME * (EXPONENT + 2)
INDEX_DECIMAL = (
    "756802081867351982204451880554288071372661809387728506437223003807921305001531327850791372970568236738039269463551121587659762466697025131751747386425314510022501248091390490254910243153397622842631947544945105455555167541116997051854319779700562468279231661109672707626186222729132787790172820015411884497288138968007428827195209890220011879606528681347680177711651451208784368084187621995157410375476545693501243461606979342522148757496590562296108929649686894530606864701937313469464285117803962870511668050942541393380291389143345921647004017647768179615176200380011740237499060386655568238207690456588020880017061093834650567265572503602612869614465025172879311948222773343533570503735606401553440822468974526317736217626926401369808061492116730577270964040751089418069810166878648649788255737899233592072253452313622878623041551026124325386211328995026509361063647117890796072612864887581297684824047649317050437834859644201449494370301768729581294368437600130737150198513243339206"
)
INDEX = int(INDEX_DECIMAL)


def q_values(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values[: limit + 1]


def mahler_recurrence_mod(limit: int, modulus: int) -> list[int]:
    values = [1, modulus - 2]
    for j in range(limit - 1):
        previous = values[j - 1] if j else 0
        values.append(
            (
                -4 * (j + 2) * values[j + 1]
                - (8 * j + 6) * values[j]
                - 4 * j * previous
            )
            % modulus
        )
    return values[: limit + 1]


def mahler_recurrence_exact(limit: int) -> list[int]:
    values = [1, -2]
    for j in range(limit - 1):
        previous = values[j - 1] if j else 0
        values.append(
            -4 * (j + 2) * values[j + 1]
            - (8 * j + 6) * values[j]
            - 4 * j * previous
        )
    return values[: limit + 1]


def mahler_closed_exact(limit: int) -> list[int]:
    factorials = [math.factorial(j) for j in range(limit + 1)]
    values = []
    for j in range(limit + 1):
        inner = sum(
            (-1) ** m
            * (factorials[j] // factorials[m])
            * math.comb(2 * j - 2 * m, j)
            for m in range(j // 2 + 1)
        )
        values.append((-1) ** j * inner)
    return values


def denominator_unit_inverses(
    limit: int, modulus: int, prime: int
) -> list[int]:
    units = [1] * (limit + 1)
    for j in range(1, limit + 1):
        unit = j
        while unit % prime == 0:
            unit //= prime
        units[j] = unit % modulus

    prefixes = [1] * (limit + 1)
    for j in range(1, limit + 1):
        prefixes[j] = prefixes[j - 1] * units[j] % modulus

    inverse_product = pow(prefixes[limit], -1, modulus)
    inverses = [1] * (limit + 1)
    for j in range(limit, 0, -1):
        inverses[j] = inverse_product * prefixes[j - 1] % modulus
        inverse_product = inverse_product * units[j] % modulus
    return inverses


def newton_value_padic_binomial(
    x: int,
    coefficients: list[int],
    prime: int,
    exponent: int,
    denominator_inverses: list[int],
) -> int:
    modulus = prime**exponent
    powers = [1] * (exponent + 1)
    for j in range(1, exponent + 1):
        powers[j] = powers[j - 1] * prime

    total = coefficients[0]
    binomial_unit = 1
    binomial_valuation = 0
    for j in range(1, len(coefficients)):
        numerator = x - j + 1
        if numerator == 0:
            break
        while numerator % prime == 0:
            numerator //= prime
            binomial_valuation += 1
        denominator = j
        while denominator % prime == 0:
            denominator //= prime
            binomial_valuation -= 1
        assert binomial_valuation >= 0
        binomial_unit *= numerator % modulus
        binomial_unit %= modulus
        binomial_unit *= denominator_inverses[j]
        binomial_unit %= modulus
        if binomial_valuation < exponent:
            binomial = binomial_unit * powers[binomial_valuation] % modulus
            total += coefficients[j] * binomial
            total %= modulus
    return total


def base_digits(value: int, base: int) -> list[int]:
    digits = []
    while value:
        digits.append(value % base)
        value //= base
    return digits or [0]


def sha256_lines(values: list[int]) -> str:
    payload = "".join(f"{value}\n" for value in values).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/bessel_padic_index_triple_zero_counterexample_certificate.json"
        ),
    )
    args = parser.parse_args()
    started = time.perf_counter()

    p = PRIME
    k = EXPONENT
    modulus = p**k

    # A small exact cross-check of all three definitions of A_j.
    exact_limit = 120
    exact_recurrence = mahler_recurrence_exact(exact_limit)
    closed = mahler_closed_exact(exact_limit)
    assert exact_recurrence == closed
    q_initial = q_values(exact_limit)
    for j in range(exact_limit + 1):
        finite_difference = sum(
            (-1) ** (j - n)
            * math.comb(j, n)
            * (-1) ** n
            * q_initial[n]
            for n in range(j + 1)
        )
        assert finite_difference == exact_recurrence[j]

    coefficients = mahler_recurrence_mod(CUTOFF, modulus)
    assert coefficients[: exact_limit + 1] == [
        value % modulus for value in exact_recurrence
    ]

    first_omitted = CUTOFF + 1
    first_level_lower_bound = (
        first_omitted // p - (first_omitted // 2) // p
    )
    assert first_level_lower_bound >= k
    assert first_omitted / (2 * p) - 1 > k

    inverses = denominator_unit_inverses(CUTOFF, modulus, p)
    f_index = newton_value_padic_binomial(
        INDEX, coefficients, p, k, inverses
    )
    assert INDEX % 2 == 0
    assert f_index == p ** (k - 1)

    digits = base_digits(INDEX, p)
    assert len(digits) == 1168
    assert digits[-1] == 4
    assert p**1167 < INDEX < p**1168

    next_digit = 4
    next_representative = INDEX + next_digit * p ** (k - 1)
    f_next = newton_value_padic_binomial(
        next_representative, coefficients, p, k, inverses
    )
    assert f_next == 0

    q_small = q_values(9)
    delta_7_at_2 = ((-q_small[9] - q_small[2]) // p) % p
    assert INDEX % p == 2
    assert delta_7_at_2 == 5

    result = {
        "counterexample": {
            "prime": p,
            "index": INDEX,
            "index_decimal_sha256": hashlib.sha256(
                INDEX_DECIMAL.encode("ascii")
            ).hexdigest(),
            "index_decimal_digits": len(INDEX_DECIMAL),
            "index_between_powers": [1167, 1168],
            "ceil_log_p_index": 1168,
            "valuation_q_index": 1171,
            "violated_additive_bound": "v_p(q_n)<=ceil(log_p(n))+2",
            "additive_bound_right_side": 1170,
            "ordinary_base_root": 2,
            "ordinary_delta_mod_p": delta_7_at_2,
            "terminal_base_p_window_positions_1165_through_1171": [
                digits[1165],
                digits[1166],
                digits[1167],
                0,
                0,
                0,
                next_digit,
            ],
            "zero_lift_digit_positions": [1168, 1169, 1170],
            "next_lift_digit_position": 1171,
            "next_lift_digit": next_digit,
            "next_representative_mod_p1172": next_representative,
        },
        "exact_modular_evaluation": {
            "modulus_exponent": k,
            "f_and_q_index_residue": f_index,
            "q_index_quotient_mod_p": 1,
            "f_next_representative_residue": f_next,
        },
        "mahler_certificate": {
            "cutoff_inclusive": CUTOFF,
            "first_omitted_index": first_omitted,
            "first_level_valuation_lower_bound_at_first_omitted": (
                first_level_lower_bound
            ),
            "coefficient_count": len(coefficients),
            "exact_closed_and_finite_difference_checks_through": exact_limit,
            "coefficient_residue_vector_sha256": sha256_lines(coefficients),
        },
        "scope": {
            "disproves": (
                "the two proposed fixed additive repairs +1 and +2"
            ),
            "does_not_prove": (
                "unbounded zero-run length or failure of V_N(C)=o(N*log(N))"
            ),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    print(
        "elapsed_seconds="
        f"{time.perf_counter() - started:.6f} "
        f"peak_rss_kib={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
