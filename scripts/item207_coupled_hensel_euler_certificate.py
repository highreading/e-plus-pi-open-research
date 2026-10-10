#!/usr/bin/env python3
"""Portable exact replay for Item 207's coupled Hensel/Euler gate.

The report proves the all-prime identities.  This standard-library
checker verifies the actual-seed coordinate changes and line geometry,
replays an actual nonzero cancellation witness, and performs a bounded
prescribed-root census.  Every computed nonoccurrence is labelled FINITE.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item207_coupled_hensel_euler_certificate.json"
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


def left_factorial(prime: int) -> int:
    factorial = 1
    total = 1
    for value in range(1, prime):
        factorial = factorial * value % prime
        total = (total + factorial) % prime
    return total


def continuant_derivative_mod(prime: int, h: int) -> int:
    """Return D_h=K_h'(0) modulo prime by differentiated recurrence."""
    previous_previous_value = 1
    previous_previous_derivative = 0
    previous_value = (-4 * h) % prime
    previous_derivative = 1
    for index in range(-h + 1, h + 1):
        coefficient = 4 * index
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


def canonical_actual_seed_regression(limit: int = 100) -> dict:
    q, companion, jet = exact_sequences(limit)
    rows = []
    for n in range(1, limit + 1):
        sign_previous = 1 if (n - 1) % 2 == 0 else -1
        wronskian = companion[n] * q[n - 1] - companion[n - 1] * q[n]
        if wronskian != 2 * sign_previous:
            raise AssertionError((n, "Wronskian", wronskian))
        if math.gcd(q[n], q[n - 1]) != 1:
            raise AssertionError((n, "adjacent gcd"))
        if math.gcd(q[n], companion[n]) != 1:
            raise AssertionError((n, "companion gcd"))
        target = (
            0
            if q[n] == 1
            else jet[n] * pow(companion[n], -1, q[n]) % q[n]
        )
        if (companion[n] * target - jet[n]) % q[n]:
            raise AssertionError((n, "canonical target"))
        rows.append(
            {
                "N": n,
                "q_digits": len(str(q[n])),
                "P_digits": len(str(companion[n])),
                "T_N": str(target),
                "wronskian": wronskian,
            }
        )
    stream = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    return {
        "classification": "FINITE_EXACT_REPLAY_OF_PROVED_ACTUAL_SEED_IDENTITIES",
        "N_range": [1, limit],
        "checks": len(rows),
        "selected_rows": [rows[index - 1] for index in (2, 4, 8, 50, 100)],
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "all_exact": True,
    }


def actual_seed_cancellation_witness() -> dict:
    prime = 7
    n = 2
    h = 0
    reflected = prime - 1 - n
    q, companion, jet = exact_sequences(reflected)
    left_integer = sum(math.factorial(value) for value in range(prime))
    target = jet[n] * pow(companion[n], -1, q[n]) % q[n]
    divided_lower = q[n] // prime % prime
    divided_upper = q[reflected] // prime % prime
    q_previous = q[n - 1] % prime
    p_value = companion[n] % prime
    rho = (left_integer - target) % prime
    d_value = continuant_derivative_mod(prime, h)
    tau = -2 * divided_lower * pow(q_previous, -1, prime) % prime
    euler_residual = (p_value * left_integer - jet[n]) % prime
    invariant_lower = (2 * divided_lower - euler_residual) % prime
    invariant_upper = (3 * divided_upper - divided_lower) % prime
    determinant = -pow(p_value, 3, prime) * pow(4, -1, prime) % prime

    expected = {
        "q_N": 7,
        "q_s": 1001,
        "P_N": 19,
        "b_N": 28,
        "T_N": 0,
        "L_p_integer": 874,
        "lambda_N": 1,
        "lambda_s": 3,
        "rho": 6,
        "tau": 5,
        "D_h": 1,
        "E_N": 2,
        "I_N": 0,
        "I_s": 1,
    }
    actual = {
        "q_N": q[n],
        "q_s": q[reflected],
        "P_N": companion[n],
        "b_N": jet[n],
        "T_N": target,
        "L_p_integer": left_integer,
        "lambda_N": divided_lower,
        "lambda_s": divided_upper,
        "rho": rho,
        "tau": tau,
        "D_h": d_value,
        "E_N": euler_residual,
        "I_N": invariant_lower,
        "I_s": invariant_upper,
    }
    if actual != expected:
        raise AssertionError(("actual witness", actual, expected))
    if determinant == 0:
        raise AssertionError("coordinate determinant")
    if (tau + 2 * d_value) % prime != 0:
        raise AssertionError("nonzero cancellation line")
    if tau == 0 or d_value == 0 or rho == 0:
        raise AssertionError("witness must be nonzero in both coordinates")
    if prime <= 2 * n + 1:
        raise AssertionError("witness must be prescribed lower range")

    return {
        "classification": "FINITE_EXACT_ACTUAL_SEED_WITNESS_FOR_PROVED_SCOPED_NO_GO",
        "p": prime,
        "N": n,
        "h": h,
        "s": reflected,
        "p_gt_2N_plus_1": True,
        "values": actual,
        "coordinate_change_determinant_mod_p": determinant,
        "nonzero_cancellation": "I_N=0 because tau+2D_h=0, while tau,D_h,rho are all nonzero",
        "not_a_coupled_all_lift_row": True,
    }


def actual_prescribed_scan(prime_limit: int) -> dict:
    root_rows = []
    lower_square_rows = []
    upper_square_rows = []
    singular_rows = []
    lower_invariant_zero_rows = []
    upper_invariant_zero_rows = []
    paired_invariant_zero_rows = []
    coupled_rows = []
    direct_continuant_checks = 0

    for prime in primes_upto(prime_limit):
        if prime < 7:
            continue
        modulus = prime * prime
        q = [1, 1]
        companion = [1, 3 % prime]
        jet = [0, 4 % prime]
        for n in range(2, prime):
            coefficient = 4 * n - 2
            q.append((coefficient * q[-1] + q[-2]) % modulus)
            companion.append(
                (coefficient * companion[-1] + companion[-2]) % prime
            )
            jet.append(
                (
                    coefficient * jet[-1]
                    + jet[-2]
                    + 4 * (q[-2] % prime)
                )
                % prime
            )

        left = left_factorial(prime)
        center = (prime - 1) // 2
        inverse_two = pow(2, -1, prime)
        inverse_four = pow(4, -1, prime)
        for n in range(1, center):
            if q[n] % prime:
                continue
            reflected = prime - 1 - n
            h = (prime - 3) // 2 - n
            q_previous = q[n - 1] % prime
            p_value = companion[n] % prime
            if q_previous == 0 or p_value == 0:
                raise AssertionError((prime, n, "root units"))
            expected_wronskian = (
                2 if (n - 1) % 2 == 0 else -2
            ) % prime
            if p_value * q_previous % prime != expected_wronskian:
                raise AssertionError((prime, n, "Wronskian at root"))

            divided_lower = q[n] // prime % prime
            divided_upper = q[reflected] // prime % prime
            difference = (q[n] - q[reflected]) % modulus
            if difference % prime:
                raise AssertionError((prime, n, "reflection integrality"))
            delta = difference // prime % prime
            d_value = -delta * pow(2 * q_previous, -1, prime) % prime
            if prime <= 251:
                direct_d = continuant_derivative_mod(prime, h)
                if direct_d != d_value:
                    raise AssertionError((prime, n, "direct D", direct_d, d_value))
                direct_continuant_checks += 1

            target = jet[n] * pow(p_value, -1, prime) % prime
            rho = (left - target) % prime
            euler_residual = (p_value * left - jet[n]) % prime
            if euler_residual != p_value * rho % prime:
                raise AssertionError((prime, n, "Euler target"))
            sign_previous = 1 if (n - 1) % 2 == 0 else -1
            if (
                4 * sign_previous * d_value - p_value * p_value * rho
            ) % prime:
                raise AssertionError((prime, n, "D/Euler bridge"))

            derivative_at_root = q_previous * inverse_two % prime
            tau = (
                -divided_lower * pow(derivative_at_root, -1, prime)
            ) % prime
            sign_n = 1 if n % 2 == 0 else -1
            tau_from_actual_seed = sign_n * p_value * divided_lower % prime
            if tau != tau_from_actual_seed:
                raise AssertionError((prime, n, "actual-seed Hensel coordinate"))

            coordinate_determinant = (
                -pow(p_value, 3, prime) * inverse_four
            ) % prime
            if coordinate_determinant == 0:
                raise AssertionError((prime, n, "coordinate determinant"))

            predicted_upper = (
                q_previous * (-tau * inverse_two + 2 * d_value)
            ) % prime
            if divided_upper != predicted_upper:
                raise AssertionError((prime, n, "upper divided value"))

            invariant_lower = (2 * divided_lower - euler_residual) % prime
            invariant_lower_from_coordinates = (
                2
                * sign_n
                * pow(p_value, -1, prime)
                * (tau + 2 * d_value)
            ) % prime
            if invariant_lower != invariant_lower_from_coordinates:
                raise AssertionError((prime, n, "lower invariant"))
            if invariant_lower != -q_previous * (tau + 2 * d_value) % prime:
                raise AssertionError((prime, n, "lower invariant Wronskian form"))

            invariant_upper = (3 * divided_upper - divided_lower) % prime
            if invariant_upper != q_previous * (-tau + 6 * d_value) % prime:
                raise AssertionError((prime, n, "upper invariant"))

            lower_square = divided_lower == 0
            upper_square = divided_upper == 0
            singular = d_value == 0
            paired_invariant_zero = invariant_lower == 0 and invariant_upper == 0
            coupled = lower_square and singular

            if lower_square != (tau == 0):
                raise AssertionError((prime, n, "lower square line"))
            if upper_square != ((tau - 4 * d_value) % prime == 0):
                raise AssertionError((prime, n, "upper square line"))
            if singular != (rho == 0):
                raise AssertionError((prime, n, "Euler/singular line"))
            if (invariant_lower == 0) != ((tau + 2 * d_value) % prime == 0):
                raise AssertionError((prime, n, "lower invariant line"))
            if (invariant_upper == 0) != ((tau - 6 * d_value) % prime == 0):
                raise AssertionError((prime, n, "upper invariant line"))
            if coupled != (lower_square and upper_square):
                raise AssertionError((prime, n, "paired squares"))
            if coupled != (tau == 0 and rho == 0):
                raise AssertionError((prime, n, "coupled coordinates"))
            if coupled != paired_invariant_zero:
                raise AssertionError((prime, n, "paired invariants"))
            if coupled != (lower_square and invariant_lower == 0):
                raise AssertionError((prime, n, "lower square plus invariant"))
            if coupled != (singular and invariant_lower == 0):
                raise AssertionError((prime, n, "singular plus invariant"))

            row = {
                "p": prime,
                "N": n,
                "h": h,
                "s": reflected,
                "lambda_N": divided_lower,
                "lambda_s": divided_upper,
                "tau": tau,
                "D_h": d_value,
                "left_factorial_mod_p": left,
                "T_N_mod_p": target,
                "rho": rho,
                "I_N": invariant_lower,
                "I_s": invariant_upper,
                "lower_square": lower_square,
                "upper_square": upper_square,
                "singular": singular,
                "coupled_all_lift": coupled,
            }
            root_rows.append(row)
            if lower_square:
                lower_square_rows.append(row)
            if upper_square:
                upper_square_rows.append(row)
            if singular:
                singular_rows.append(row)
            if invariant_lower == 0:
                lower_invariant_zero_rows.append(row)
            if invariant_upper == 0:
                upper_invariant_zero_rows.append(row)
            if paired_invariant_zero:
                paired_invariant_zero_rows.append(row)
            if coupled:
                coupled_rows.append(row)

    witness_keys = [(row["p"], row["N"]) for row in lower_invariant_zero_rows]
    if (7, 2) not in witness_keys:
        raise AssertionError("missing actual p=7 cancellation witness")
    upper_square_keys = [(row["p"], row["N"]) for row in upper_square_rows]
    if (13, 4) not in upper_square_keys:
        raise AssertionError("missing actual p=13 upper-square witness")

    stream = json.dumps(root_rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    return {
        "classification": "EXPERIMENTAL_FINITE_NOT_AN_ALL_PRIME_OR_RATE_THEOREM",
        "prime_limit": prime_limit,
        "prescribed_lower_root_rows": len(root_rows),
        "direct_continuant_checks_through_251": direct_continuant_checks,
        "lower_square_rows": lower_square_rows,
        "upper_square_rows": upper_square_rows,
        "singular_rows": singular_rows,
        "lower_invariant_zero_rows": lower_invariant_zero_rows,
        "upper_invariant_zero_rows": upper_invariant_zero_rows,
        "paired_invariant_zero_rows": paired_invariant_zero_rows,
        "coupled_all_lift_rows": coupled_rows,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "scope_warning": (
            "Rows are lower-index roots N<(p-1)/2.  An upper_square row "
            "means p^2 divides the reflected q_s, not the prescribed q_N."
        ),
    }


def certificate(prime_limit: int) -> dict:
    return {
        "item": 207,
        "classification": {
            "PROVED": [
                "the actual-seed maps (lambda,rho) to (tau,D_h) by a diagonal p-unit matrix of determinant -P_N^3/4",
                "p^2|q_N iff tau=0, and p|D_h iff rho=L_p-T_N=0 mod p",
                "paired p^2 divisibility is equivalent to tau=D_h=0, tau=rho=0, or p^2|q_N with L_p=T_N mod p",
                "the lower and upper square lines are tau=0 and tau=4D_h; the paired invariant lines are tau=-2D_h and tau=6D_h",
                "the actual row (p,N,h)=(7,2,0) is a nonzero cancellation on the lower-invariant line, so a one-invariant collapse is invalid for the actual seed",
                "the coordinate repackaging contributes zero new exponent to the radical ledger; only R_N^2|q_N follows",
            ],
            "EXPERIMENTAL_FINITE": [
                f"actual prescribed lower-root census through p<={prime_limit}",
                "direct continuant cross-checks through p<=251",
                "the displayed p=7 actual-seed cancellation witness",
            ],
            "OPEN": [
                "existence of any prescribed lower root with p^2|q_N",
                "existence of any coupled actual all-lift row",
                "any global exclusion or zero-rate bound for the coupled radical",
                "any cross-prime theorem controlling the joint actual values tau and L_p-T_N",
            ],
        },
        "exact_coordinate_identities": {
            "definitions": (
                "lambda=q_N/p, rho=L_p-T_N, tau=Hensel digit, "
                "E_N=P_N L_p-b_N, all modulo p at p|q_N"
            ),
            "hensel_actual_seed": "tau=(-1)^N P_N lambda",
            "euler_continuant": "4(-1)^(N-1)D_h=P_N^2 rho",
            "coordinate_determinant": "-P_N^3/4, a p-unit",
            "lower_invariant": (
                "I_N=2lambda-E_N=2(-1)^N P_N^(-1)(tau+2D_h)"
            ),
            "upper_divided_value": (
                "lambda_s=q_(N-1)(-tau/2+2D_h), s=p-1-N"
            ),
            "upper_invariant": "I_s=q_(N-1)(-tau+6D_h)",
            "lower_square_line": "p^2|q_N iff tau=0",
            "upper_square_line": "p^2|q_s iff tau=4D_h",
            "lower_invariant_line": "I_N=0 iff tau=-2D_h",
            "upper_invariant_line": "I_s=0 iff tau=6D_h",
            "coupled_equivalence": (
                "p^2|q_N,q_s iff tau=D_h=0 iff tau=rho=0 iff "
                "p^2|q_N and L_p=T_N mod p"
            ),
        },
        "scoped_no_go": {
            "rank_statement": (
                "the two filters are related only by an invertible change of "
                "first-Witt coordinates; combining them creates no extra "
                "divisibility exponent"
            ),
            "single_invariant_kernel": "I_N has kernel tau+2D_h=0",
            "actual_seed_witness": "(p,N,h)=(7,2,0) gives (tau,D_h)=(5,1) and I_N=0",
            "scope": (
                "this rules out collapse to the known single invariant and "
                "direct discriminant/resultant-height bookkeeping; it does "
                "not rule out new arithmetic controlling the joint actual coordinates"
            ),
        },
        "rate_ledger": {
            "coupled_radical": (
                "R_N=product of p>2N+1 with p^2|q_N and L_p=T_N mod p"
            ),
            "proved_divisibility": "R_N^2 divides q_N",
            "new_exponent_from_coordinate_repackaging": 0,
            "R_squared_required_log_R_per_m": "0.05889895100829538164",
            "conclusion": "no global exclusion, o(m), or below-threshold bound is proved",
        },
        "dependency_sha256": {
            "sources/item165_noncentral_singular_report.md": (
                "d7b4475d2adfeff9a5f1c70a9c6b318d0c2b140bf90b194aa9acb6fdddcc2650"
            ),
            "sources/item193_actual_seed_invariant_report.md": (
                "85a0335501e5c81e6d45c2a33139fca2ac24be54324d40fe45d82f891cf51cb9"
            ),
            "sources/item198_actual_all_lift_pair_report.md": (
                "aad8ed39bd63717aae162d0cbcc60ec9d27c023b16c44e554442cd38d49ae749"
            ),
            "sources/item200_common_log_gcd_report.md": (
                "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68"
            ),
            "sources/item202_actual_squarefull_filter_report.md": (
                "abbc68e283f16871798be0c6da8af5df55ba6bf865a5864eefc0f8e19fe88f62"
            ),
            "sources/item204_squarefull_discriminant_report.md": (
                "45ad273d407323902745095bd7abbc1fe5d17cf4d8da35737276eb3e6c7fc665"
            ),
        },
        "canonical_actual_seed_regression": canonical_actual_seed_regression(),
        "actual_seed_cancellation_witness": actual_seed_cancellation_witness(),
        "finite_actual_prescribed_scan": actual_prescribed_scan(prime_limit),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=20000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.prime_limit < 13:
        raise SystemExit("--prime-limit must be at least 13")
    result = certificate(args.prime_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    finite = result["finite_actual_prescribed_scan"]
    print(
        json.dumps(
            {
                "output": str(args.output),
                "finite_prime_limit": finite["prime_limit"],
                "finite_prescribed_lower_roots": finite[
                    "prescribed_lower_root_rows"
                ],
                "finite_lower_square_rows": len(finite["lower_square_rows"]),
                "finite_upper_square_rows": len(finite["upper_square_rows"]),
                "finite_coupled_rows": len(finite["coupled_all_lift_rows"]),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
