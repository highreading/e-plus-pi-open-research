#!/usr/bin/env python3
"""Exact replay for Item 202's actual-seed squarefull/Euler filter.

The all-index proofs are written in the companion report.  This program
checks their integer algebra, the first two p-adic Euler digits, and a
finite actual-root census.  Every nonoccurrence statement emitted by the
program is explicitly labelled FINITE.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item202_actual_squarefull_filter_certificate.json"
DEFAULT_OUTPUT = (
    HERE / RESULT_NAME
    if HERE.name.lower() == "work"
    else HERE.parent / "results" / RESULT_NAME
)


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for divisor in range(2, math.isqrt(limit) + 1):
        if sieve[divisor]:
            sieve[divisor * divisor : limit + 1 : divisor] = b"\x00" * (
                (limit - divisor * divisor) // divisor + 1
            )
    return [prime for prime in range(2, limit + 1) if sieve[prime]]


def exact_sequences(limit: int) -> tuple[list[int], list[int], list[int]]:
    q = [1, 1]
    companion = [1, 3]
    jet = [0, 4]
    for n in range(2, limit + 1):
        coefficient = 4 * n - 2
        q.append(coefficient * q[-1] + q[-2])
        companion.append(coefficient * companion[-1] + companion[-2])
        jet.append(
            coefficient * jet[-1] + jet[-2] + 4 * q[-2]
        )
    return q[: limit + 1], companion[: limit + 1], jet[: limit + 1]


def continuant_derivative_mod(prime: int, h: int) -> int:
    """D_h modulo prime by differentiating the continuant recurrence."""
    previous_previous_value = 1
    previous_previous_derivative = 0
    previous_value = (-4 * h) % prime
    previous_derivative = 1
    for j in range(-h + 1, h + 1):
        coefficient = 4 * j
        new_value = (
            coefficient * previous_value + previous_previous_value
        ) % prime
        new_derivative = (
            previous_value
            + coefficient * previous_derivative
            + previous_previous_derivative
        ) % prime
        previous_previous_value, previous_value = previous_value, new_value
        previous_previous_derivative, previous_derivative = (
            previous_derivative,
            new_derivative,
        )
    return previous_derivative


def left_factorial(prime: int, modulus: int | None = None) -> int:
    if modulus is None:
        modulus = prime * prime
    factorial = 1
    total = 1
    for j in range(1, prime):
        factorial = factorial * j % modulus
        total = (total + factorial) % modulus
    return total


def canonical_target_regression(limit: int = 100) -> dict:
    q, companion, jet = exact_sequences(limit)
    rows = []
    for n in range(1, limit + 1):
        expected_wronskian = 2 if (n - 1) % 2 == 0 else -2
        wronskian = companion[n] * q[n - 1] - companion[n - 1] * q[n]
        if wronskian != expected_wronskian:
            raise AssertionError((n, "Wronskian", wronskian))
        if q[n] % 2 != 1 or companion[n] % 2 != 1:
            raise AssertionError((n, "parity"))
        if math.gcd(q[n], companion[n]) != 1:
            raise AssertionError((n, "same-index gcd"))

        if q[n] == 1:
            target = 0
            carry = companion[n] * target - jet[n]
        else:
            target = jet[n] * pow(companion[n], -1, q[n]) % q[n]
            numerator = companion[n] * target - jet[n]
            if numerator % q[n]:
                raise AssertionError((n, "target integrality"))
            carry = numerator // q[n]

            inverse_two = pow(2, -1, q[n])
            inverse_from_wronskian = (
                (1 if (n - 1) % 2 == 0 else -1)
                * q[n - 1]
                * inverse_two
            ) % q[n]
            if companion[n] * inverse_from_wronskian % q[n] != 1:
                raise AssertionError((n, "Wronskian inverse"))
            target_from_wronskian = jet[n] * inverse_from_wronskian % q[n]
            if target_from_wronskian != target:
                raise AssertionError((n, "target formulas"))

        rows.append(
            {
                "N": n,
                "q_digits": len(str(q[n])),
                "P_digits": len(str(companion[n])),
                "b_digits": len(str(abs(jet[n]))),
                "T_N": str(target),
                "carry_C_N": str(carry),
            }
        )

    stream = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    selected = [rows[index - 1] for index in (2, 3, 4, 8, 20, 50, 100)]
    return {
        "N_range": [1, limit],
        "checks": len(rows),
        "selected_rows": selected,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "all_exact": True,
    }


def euler_two_digit_regression(prime_limit: int = 251) -> dict:
    rows = []
    for prime in primes_upto(prime_limit):
        if prime < 3:
            continue
        modulus = prime * prime
        lower_block = left_factorial(prime, modulus)

        factorial = 1
        full_sum = 1
        for j in range(1, 2 * prime):
            factorial = factorial * j % modulus
            full_sum = (full_sum + factorial) % modulus

        predicted = (1 - prime) * lower_block % modulus
        if full_sum != predicted:
            raise AssertionError((prime, full_sum, predicted))
        rows.append([prime, lower_block, full_sum])

    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "prime_range": [3, prime_limit],
        "checks": len(rows),
        "identity": "sum_(j>=0)j! = (1-p)*sum_(j=0)^(p-1)j! mod p^2",
        "wilson_quotient_needed_at_this_digit": False,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "all_exact": True,
    }


def squarefull_quotient_fixtures(
    index_limit: int = 200, prime_limit: int = 499
) -> dict:
    """Check carry cancellation at actual q_N square divisors.

    These rows are algebra fixtures only.  Their small primes are not in
    the prescribed moving range p>2N+1, and formal L values are not claimed
    to be actual left factorials.
    """
    q, companion, jet = exact_sequences(index_limit)
    primes = [prime for prime in primes_upto(prime_limit) if prime % 2]
    rows = []
    for n in range(2, index_limit + 1):
        target = jet[n] * pow(companion[n], -1, q[n]) % q[n]
        carry_numerator = companion[n] * target - jet[n]
        if carry_numerator % q[n]:
            raise AssertionError((n, "carry"))
        for prime in primes:
            if q[n] % (prime * prime):
                continue
            for lift_digit in (0, 1, prime - 1):
                formal_left_factorial = target + prime * lift_digit
                numerator = (
                    companion[n] * formal_left_factorial - jet[n]
                )
                if numerator % prime:
                    raise AssertionError((n, prime, "formal residual"))
                quotient = numerator // prime % prime
                predicted = companion[n] * lift_digit % prime
                if quotient != predicted:
                    raise AssertionError(
                        (n, prime, lift_digit, quotient, predicted)
                    )
            rows.append(
                {
                    "N": n,
                    "p": prime,
                    "v_p_at_least_2": True,
                    "T_N_mod_p_squared": target % (prime * prime),
                    "tested_formal_lift_digits": [0, 1, prime - 1],
                }
            )

    # N=79 has two small squared prime divisors and makes the CRT freedom
    # visible in one actual normalized triple (q_N,P_N,b_N).
    crt_row = next((row for row in rows if row["N"] == 79), None)
    n79_primes = [row["p"] for row in rows if row["N"] == 79]
    if crt_row is None or n79_primes != [7, 31]:
        raise AssertionError(("expected N=79 fixture", n79_primes))

    stream = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    return {
        "classification": (
            "FINITE_FORMAL_LOCAL_DATA_FIXTURES_NOT_PRESCRIBED_ALL_LIFT_ROWS"
        ),
        "index_limit": index_limit,
        "prime_limit": prime_limit,
        "actual_q_N_square_divisor_rows": len(rows),
        "N_79_simultaneous_squared_primes": n79_primes,
        "formal_lift_digits_are_arbitrary": True,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "rows": rows,
    }


def actual_prescribed_scan(prime_limit: int) -> dict:
    root_rows = []
    lower_square_rows = []
    upper_square_rows = []
    all_lift_rows = []
    direct_continuant_checks = 0
    target_checks = 0

    for prime in primes_upto(prime_limit):
        if prime < 7:
            continue
        modulus = prime * prime
        q2 = [1, 1]
        companion = [1, 3 % prime]
        jet = [0, 4 % prime]
        for n in range(2, prime):
            coefficient = 4 * n - 2
            q2.append((coefficient * q2[-1] + q2[-2]) % modulus)
            companion.append(
                (coefficient * companion[-1] + companion[-2]) % prime
            )
            jet.append(
                (
                    coefficient * jet[-1]
                    + jet[-2]
                    + 4 * (q2[-2] % prime)
                )
                % prime
            )

        left = left_factorial(prime, prime) % prime
        center = (prime - 1) // 2
        for n in range(1, center):
            if q2[n] % prime:
                continue
            reflected = prime - 1 - n
            difference = q2[n] - q2[reflected]
            if difference % prime:
                raise AssertionError((prime, n, "reflection quotient"))
            delta = difference // prime % prime
            q_previous = q2[n - 1] % prime
            if q_previous == 0 or companion[n] == 0:
                raise AssertionError((prime, n, "unit"))
            d_from_slope = (
                -delta * pow(2 * q_previous, -1, prime)
            ) % prime
            h = (prime - 3) // 2 - n
            if prime <= 251:
                direct_d = continuant_derivative_mod(prime, h)
                if direct_d != d_from_slope:
                    raise AssertionError(
                        (prime, n, direct_d, d_from_slope)
                    )
                direct_continuant_checks += 1

            target = jet[n] * pow(companion[n], -1, prime) % prime
            if (d_from_slope == 0) != (left == target):
                raise AssertionError((prime, n, "Euler target"))
            target_checks += 1

            lower_square = q2[n] == 0
            upper_square = q2[reflected] == 0
            all_lift = lower_square and d_from_slope == 0
            row = {
                "p": prime,
                "N": n,
                "h": h,
                "reflected_index": reflected,
                "lambda_lower": q2[n] // prime % prime,
                "lambda_upper": q2[reflected] // prime % prime,
                "D_h_mod_p": d_from_slope,
                "left_factorial_mod_p": left,
                "T_N_mod_p": target,
                "lower_square": lower_square,
                "upper_square": upper_square,
                "actual_all_lift": all_lift,
            }
            root_rows.append(row)
            if lower_square:
                lower_square_rows.append(row)
            if upper_square:
                upper_square_rows.append(row)
            if all_lift:
                all_lift_rows.append(row)

    stream = json.dumps(
        root_rows, separators=(",", ":"), sort_keys=True
    ).encode("ascii")
    return {
        "classification": "EXPERIMENTAL_FINITE_NOT_AN_ALL_PRIME_THEOREM",
        "prime_limit": prime_limit,
        "noncentral_lower_root_rows": len(root_rows),
        "normalization_target_checks": target_checks,
        "direct_continuant_checks_through_251": direct_continuant_checks,
        "lower_large_prime_square_rows": lower_square_rows,
        "upper_mate_square_rows": upper_square_rows,
        "actual_all_lift_rows": all_lift_rows,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def certificate(prime_limit: int) -> dict:
    return {
        "item": 202,
        "classification": {
            "PROVED": [
                "gcd(P_N,q_N)=1 and the canonical actual-seed target T_N exists modulo q_N",
                "at a prescribed actual root, gcd(p,D_h)=gcd(p,!p-T_N)",
                "actual paired all-lift iff p^2|q_N and !p=T_N mod p",
                "under p^2|q_N the first residual quotient is P_N*(!p-T_N)/p mod p",
                "the p-adic Euler sum is (1-p)!p mod p^2, so no Wilson quotient occurs at this digit",
                "the exact local identities alone permit every next left-factorial lift digit and cannot improve the full squarefull-radical ceiling",
            ],
            "EXPERIMENTAL_FINITE": [
                f"actual prescribed-index scan through p<={prime_limit}",
                "small-prime square-divisor and formal lift-digit fixtures",
            ],
            "OPEN": [
                "existence of a prime p>2N+1 with p^2|q_N at a lower prescribed index",
                "existence of any actual noncentral all-lift pair",
                "any sub-capacity all-N bound for the large-prime squarefull radical",
                "any nonvanishing or density theorem for the prescribed left-factorial residues or their lift digits",
                "actual coefficient valuation, divided matching, saddle synchronization, and a small moving-CRT representative",
            ],
        },
        "exact_identities": {
            "canonical_target": "P_N*T_N=b_N mod q_N, 0<=T_N<q_N",
            "target_from_wronskian": (
                "T_N=(-1)^(N-1)*b_N*q_(N-1)/2 mod q_N"
            ),
            "normalization_filter": (
                "if p=2N+2h+3 is prime and p|q_N, then "
                "gcd(p,D_h)=gcd(p,!p-T_N)"
            ),
            "all_lift": "p^2|q_N and p|D_h iff p^2|q_N and !p=T_N mod p",
            "squarefull_quotient": (
                "if p^2|q_N and !p=T_N mod p, then "
                "(P_N*!p-b_N)/p=P_N*(!p-T_N)/p mod p"
            ),
            "p_adic_euler_two_digits": (
                "E_p=sum_(j>=0)j!=(1-p)!p mod p^2"
            ),
            "next_euler_digit": (
                "(P_N*E_p-b_N)/p=P_N*((!p-T_N)/p-T_N) mod p"
            ),
        },
        "logical_separation": [
            "actual root existence at prescribed N",
            "large-prime square divisibility p^2|q_N",
            "local singular/all-lift residue !p=T_N mod p",
            "next left-factorial/Euler lift digit",
            "actual mixed-coefficient valuation",
            "same-index divided matching",
            "saddle-compatible small moving-CRT representative",
        ],
        "mass_ledger": {
            "all_lift_radical": "R_N=product of p>2N+1 with p^2|q_N and !p=T_N mod p",
            "proved_capacity_only": "R_N^2 divides q_N",
            "post_3m_gap_per_6m": "0.01963298366943179388",
            "R_squared_required_log_R_per_m": "0.05889895100829538164",
            "beta_log_q_N_per_6m": "1.1685311871794864979",
        },
        "dependency_sha256": {
            "sources/item166_actual_singular_report.md": "2a8f1c84b91fa7d18fb02417cf480baae819afa795968375e5a3767fc0f52f76",
            "sources/item193_actual_seed_invariant_report.md": "85a0335501e5c81e6d45c2a33139fca2ac24be54324d40fe45d82f891cf51cb9",
            "sources/item198_actual_all_lift_pair_report.md": "aad8ed39bd63717aae162d0cbcc60ec9d27c023b16c44e554442cd38d49ae749",
        },
        "canonical_target_regression": canonical_target_regression(),
        "euler_two_digit_regression": euler_two_digit_regression(),
        "squarefull_quotient_fixtures": squarefull_quotient_fixtures(),
        "actual_prescribed_scan": actual_prescribed_scan(prime_limit),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=20000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.prime_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    finite = result["actual_prescribed_scan"]
    print(
        json.dumps(
            {
                "output": str(args.output),
                "finite_prime_limit": finite["prime_limit"],
                "finite_noncentral_lower_roots": finite[
                    "noncentral_lower_root_rows"
                ],
                "finite_lower_square_rows": len(
                    finite["lower_large_prime_square_rows"]
                ),
                "finite_actual_all_lift_rows": len(
                    finite["actual_all_lift_rows"]
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
