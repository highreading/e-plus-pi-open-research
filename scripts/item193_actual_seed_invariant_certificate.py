#!/usr/bin/env python3
"""Exact certificate for Item 193's paired actual-seed invariant theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item193_actual_seed_invariant_certificate.json"
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
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * (
                (limit - q * q) // q + 1
            )
    return [p for p in range(7, limit + 1) if sieve[p]]


def beta_data(prime: int) -> tuple[list[int], list[int], list[int], int]:
    modulus = prime * prime
    q = [1, 1]
    for n in range(2, 2 * prime):
        q.append(((4 * n - 2) * q[-1] + q[-2]) % modulus)

    companion = [1, 3]
    jet = [0, 4]
    for n in range(2, prime):
        coefficient = (4 * n - 2) % prime
        companion.append(
            (coefficient * companion[-1] + companion[-2]) % prime
        )
        jet.append(
            (
                coefficient * jet[-1]
                + jet[-2]
                + 4 * (q[n - 1] % prime)
            )
            % prime
        )

    factorial = 1
    left_factorial = 1
    for n in range(1, prime):
        factorial = factorial * n % prime
        left_factorial = (left_factorial + factorial) % prime
    return q, companion, jet, left_factorial


def continuant_derivative(prime: int, lower_root: int) -> int:
    """Return D_h=K'_h(0) mod p by differentiated continuant recurrence."""
    h = (prime - 3) // 2 - lower_root
    if h < 0:
        raise ValueError((prime, lower_root, h))
    previous_previous_value = 1
    previous_previous_derivative = 0
    previous_value = (-4 * h) % prime
    previous_derivative = 1
    if h == 0:
        return previous_derivative
    for j in range(-h + 1, h + 1):
        constant = 4 * j
        value = (
            constant * previous_value + previous_previous_value
        ) % prime
        derivative = (
            previous_value
            + constant * previous_derivative
            + previous_previous_derivative
        ) % prime
        previous_previous_value, previous_value = previous_value, value
        (
            previous_previous_derivative,
            previous_derivative,
        ) = previous_derivative, derivative
    return previous_derivative


def divided(value: int, prime: int, label: tuple) -> int:
    if value % prime:
        raise AssertionError((*label, "not divisible by p", value))
    return value // prime % prime


def replay_prime_square_reflection(prime_limit: int) -> dict:
    """Directly replay q_(p^2-1-n)=q_n and the paired lift orientation."""
    rows = []
    reflection_value_checks = 0
    affine_fibre_checks = 0
    paired_lift_checks = 0
    for prime in primes_upto(prime_limit):
        modulus = prime * prime
        q = [1, 1]
        for n in range(2, modulus):
            q.append(((4 * n - 2) * q[-1] + q[-2]) % modulus)
        for n in range(modulus):
            if q[modulus - 1 - n] != q[n]:
                raise AssertionError((prime, n, "prime-square reflection"))
            reflection_value_checks += 1

        roots = [r for r in range(prime) if q[r] % prime == 0]
        root_set = set(roots)
        for x in roots:
            lam = divided(q[x], prime, (prime, x, "small lambda"))
            delta = divided(
                (-q[x + prime] - q[x]) % modulus,
                prime,
                (prime, x, "small delta"),
            )
            for t in range(prime):
                index = x + t * prime
                signed = ((-1 if t & 1 else 1) * q[index]) % modulus
                value = divided(
                    signed,
                    prime,
                    (prime, x, t, "small affine fibre"),
                )
                if value != (lam + t * delta) % prime:
                    raise AssertionError((prime, x, t, "affine law"))
                affine_fibre_checks += 1

            if x < (prime - 1) // 2:
                mate = prime - 1 - x
                if mate not in root_set:
                    raise AssertionError((prime, x, mate, "small mate"))
                for t in range(prime):
                    reflected_digit = prime - 1 - t
                    if q[x + t * prime] != q[mate + reflected_digit * prime]:
                        raise AssertionError((prime, x, mate, t, "paired lift"))
                    paired_lift_checks += 1
        rows.append([prime, len(roots)])
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "prime_limit": prime_limit,
        "prime_square_reflection_value_checks": reflection_value_checks,
        "signed_affine_fibre_checks": affine_fibre_checks,
        "paired_lift_checks": paired_lift_checks,
        "all_exact": True,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def scan(prime_limit: int) -> dict:
    pair_rows = []
    zero_invariant_rows = []
    singular_pair_rows = []
    all_lift_pair_rows = []
    central_root_rows = []
    total_roots = 0
    reflection_checks = 0
    continuant_checks = 0
    euler_checks = 0
    determinant_checks = 0

    for prime in primes_upto(prime_limit):
        modulus = prime * prime
        center = (prime - 1) // 2
        q, companion, jet, left_factorial = beta_data(prime)
        roots = [r for r in range(prime) if q[r] % prime == 0]
        total_roots += len(roots)
        root_set = set(roots)

        for r in roots:
            if r == center:
                lam = divided(q[r], prime, (prime, r, "central lambda"))
                delta = divided(
                    (-q[r + prime] - q[r]) % modulus,
                    prime,
                    (prime, r, "central delta"),
                )
                central_root_rows.append(
                    {
                        "p": prime,
                        "r": r,
                        "lambda": lam,
                        "delta": delta,
                        "I": (delta + 2 * lam) % prime,
                    }
                )
                continue
            if r > center:
                continue

            s = prime - 1 - r
            if s not in root_set:
                raise AssertionError((prime, r, s, "missing reflection mate"))

            lambda_r = divided(q[r], prime, (prime, r, "lambda_r"))
            lambda_s = divided(q[s], prime, (prime, s, "lambda_s"))
            delta_r = divided(
                (-q[r + prime] - q[r]) % modulus,
                prime,
                (prime, r, "delta_r"),
            )
            delta_s = divided(
                (-q[s + prime] - q[s]) % modulus,
                prime,
                (prime, s, "delta_s"),
            )
            reflection_r = divided(
                (q[r] - q[s]) % modulus,
                prime,
                (prime, r, s, "reflection_r"),
            )
            reflection_s = divided(
                (q[s] - q[r]) % modulus,
                prime,
                (prime, r, s, "reflection_s"),
            )
            if delta_r != reflection_r or delta_s != reflection_s:
                raise AssertionError(
                    (prime, r, s, delta_r, delta_s, reflection_r, reflection_s)
                )
            if delta_r != (lambda_r - lambda_s) % prime:
                raise AssertionError((prime, r, s, "lower orientation"))
            if delta_s != (lambda_s - lambda_r) % prime:
                raise AssertionError((prime, r, s, "upper orientation"))
            reflection_checks += 1

            invariant_r = (delta_r + 2 * lambda_r) % prime
            invariant_s = (delta_s + 2 * lambda_s) % prime
            if invariant_r != (3 * lambda_r - lambda_s) % prime:
                raise AssertionError((prime, r, s, "I_r formula"))
            if invariant_s != (3 * lambda_s - lambda_r) % prime:
                raise AssertionError((prime, r, s, "I_s formula"))

            all_lift = lambda_r == 0 and lambda_s == 0
            both_zero = invariant_r == 0 and invariant_s == 0
            if both_zero != all_lift:
                raise AssertionError((prime, r, s, "determinant classification"))
            if not all_lift and both_zero:
                raise AssertionError((prime, r, s, "pair nonvanishing"))
            determinant_checks += 1

            d_h = continuant_derivative(prime, r)
            q_previous = q[r - 1] % prime
            if delta_r != (-2 * d_h * q_previous) % prime:
                raise AssertionError((prime, r, s, "continuant slope"))
            if invariant_r != (2 * (lambda_r - d_h * q_previous)) % prime:
                raise AssertionError((prime, r, s, "continuant invariant"))
            if (invariant_r == 0) != (
                lambda_r == d_h * q_previous % prime
            ):
                raise AssertionError((prime, r, s, "continuant zero criterion"))
            continuant_checks += 1

            for x, lam, delta, invariant in (
                (r, lambda_r, delta_r, invariant_r),
                (s, lambda_s, delta_s, invariant_s),
            ):
                wronskian = (
                    companion[x] * (q[x - 1] % prime)
                    - companion[x - 1] * (q[x] % prime)
                ) % prime
                expected = (2 if x & 1 else -2) % prime
                if wronskian != expected or companion[x] == 0:
                    raise AssertionError((prime, x, "companion unit"))
                euler_residual = (
                    companion[x] * left_factorial - jet[x]
                ) % prime
                if euler_residual != (-delta) % prime:
                    raise AssertionError((prime, x, "Euler slope bridge"))
                target = (
                    (jet[x] + 2 * lam)
                    * pow(companion[x], -1, prime)
                ) % prime
                if (left_factorial == target) != (invariant == 0):
                    raise AssertionError((prime, x, "shifted Euler criterion"))
                euler_checks += 1

            pair_type = (
                "all_lift"
                if all_lift
                else "dead_singular"
                if delta_r == 0
                else "ordinary"
            )
            row = {
                "p": prime,
                "r": r,
                "s": s,
                "lambda_r": lambda_r,
                "lambda_s": lambda_s,
                "delta_r": delta_r,
                "delta_s": delta_s,
                "I_r": invariant_r,
                "I_s": invariant_s,
                "D_h": d_h,
                "h": (prime - 3) // 2 - r,
                "left_factorial_mod_p": left_factorial,
                "type": pair_type,
            }
            pair_rows.append(row)
            if invariant_r == 0 or invariant_s == 0:
                zero_invariant_rows.append(row)
            if delta_r == 0:
                singular_pair_rows.append(row)
            if all_lift:
                all_lift_pair_rows.append(row)

    stream = json.dumps(pair_rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    return {
        "prime_limit": prime_limit,
        "total_actual_roots": total_roots,
        "noncentral_reflection_pairs": len(pair_rows),
        "central_root_rows": central_root_rows,
        "pairs_with_at_least_one_zero_invariant": zero_invariant_rows,
        "singular_noncentral_pairs": singular_pair_rows,
        "all_lift_noncentral_pairs": all_lift_pair_rows,
        "reflection_orientation_checks": reflection_checks,
        "continuant_obstruction_checks": continuant_checks,
        "shifted_euler_residue_checks": euler_checks,
        "pair_determinant_checks": determinant_checks,
        "pair_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "status": "EXPERIMENTAL_FINITE_FOR_EXISTENCE; EXACT_REPLAY_OF_PROVED_IDENTITIES",
    }


def certificate(prime_limit: int) -> dict:
    return {
        "item": 193,
        "classification": {
            "PROVED": [
                "For a noncentral reflection pair, delta_r=lambda_r-lambda_s and delta_s=lambda_s-lambda_r.",
                "The seed invariants are I_r=3lambda_r-lambda_s and I_s=3lambda_s-lambda_r.",
                "For p>=7, I_r=I_s=0 iff the actual pair is already all-lift; otherwise at least one invariant is nonzero.",
                "I_r=0 iff lambda_r=D_h*q_(r-1), equivalently iff the shifted prescribed left-factorial residue holds.",
            ],
            "EXPERIMENTAL_FINITE": [
                f"actual reflection-pair census through p<={prime_limit}",
            ],
            "OPEN": [
                "all-prime exclusion or logarithmic-mass bound for one-sided I-zero roots",
                "existence of an actual noncentral singular or all-lift pair",
                "required mixed-coefficient divisibility",
                "same-saddle-index matching and a sufficiently small moving CRT representative",
            ],
        },
        "exact_identities": {
            "lower_slope": "delta_r=lambda_r-lambda_s",
            "upper_slope": "delta_s=lambda_s-lambda_r=-delta_r",
            "paired_invariants": [
                "I_r=3lambda_r-lambda_s",
                "I_s=3lambda_s-lambda_r",
            ],
            "determinant": "det([[3,-1],[-1,3]])=8, a unit for p>=7",
            "continuant_zero_criterion": "I_r=0 iff lambda_r=D_h*q_(r-1) mod p",
            "shifted_euler_zero_criterion": "!p=(b_r+2lambda_r)*P_r^(-1) mod p",
        },
        "logical_separation": [
            "root/invariant existence",
            "positive logarithmic mass",
            "actual b_m divisibility at the required valuation",
            "same-index divided matching",
            "small moving-CRT representative in the saddle window",
        ],
        "prime_square_reflection_replay": replay_prime_square_reflection(251),
        "finite_scan": scan(prime_limit),
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
    scan_result = result["finite_scan"]
    print(
        json.dumps(
            {
                "output": str(args.output),
                "total_actual_roots": scan_result["total_actual_roots"],
                "noncentral_reflection_pairs": scan_result[
                    "noncentral_reflection_pairs"
                ],
                "pairs_with_at_least_one_zero_invariant": scan_result[
                    "pairs_with_at_least_one_zero_invariant"
                ],
                "singular_noncentral_pairs": scan_result[
                    "singular_noncentral_pairs"
                ],
                "pair_stream_sha256": scan_result["pair_stream_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
