#!/usr/bin/env python3
"""Deterministic certificate for an interior adjacent Euler-irregular seed.

This supplement verifies, by several exact routes, that

    gcd(E_3286, E_3288) = 151483,

that 151483 is prime and occurs to valuation one in both Euler numbers, and
that its complete first-period E-irregular index set is exactly
{3286, 3288}.  It also replays the exact gcd scan through N=1643 and checks
that this is the sole nontrivial J_N row in that finite range.

The computation is a finite theorem/counterexample, not an asymptotic bound
for J_N and not a classification of e+pi.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from pathlib import Path

import sympy as sp
from flint import fmpz, fmpz_mod_poly_ctx


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_adjacent_euler_irregular_seed_certificate.json"
RSS_LIMIT_KIB = 2 * 1024 * 1024
P = 151_483
N_SEED = 1_643
LOW_INDEX = 2 * N_SEED
HIGH_INDEX = LOW_INDEX + 2
MODULUS_SQUARED = P * P


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_ints(values: list[int]) -> str:
    return sha256_bytes((",".join(map(str, values)) + "\n").encode())


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def trial_division_prime(value: int) -> tuple[bool, int]:
    """Deterministic primality check, returning the last tested divisor."""
    assert value >= 2
    if value % 2 == 0:
        return value == 2, 2
    limit = math.isqrt(value)
    last = 1
    for divisor in range(3, limit + 1, 2):
        last = divisor
        if value % divisor == 0:
            return False, divisor
    return True, last


def euler_even_mod(max_half_index: int, modulus: int) -> list[int]:
    """Return E_0,E_2,... modulo modulus from the defining recurrence."""
    values = [1]
    for n in range(1, max_half_index + 1):
        choose = 1
        total = 0
        for k in range(n):
            total = (total + choose * values[k]) % modulus
            choose = (
                choose
                * (2 * n - 2 * k)
                * (2 * n - 2 * k - 1)
                // ((2 * k + 1) * (2 * k + 2))
            )
        values.append((-total) % modulus)
    return values


def complete_first_period_indices(p: int) -> tuple[list[int], str]:
    """Find every even 2<=r<=p-3 with E_r=0 mod p.

    In F_p[[x]], sech(x) is the inverse of cosh(x).  Truncation below
    degree p-1 is valid because all factorials involved are units modulo p.
    """
    context = fmpz_mod_poly_ctx(p)
    coefficients = [0] * (p - 1)
    inverse_factorial = 1
    coefficients[0] = 1
    for degree in range(1, p - 1):
        inverse_factorial = inverse_factorial * pow(degree, -1, p) % p
        if degree % 2 == 0:
            coefficients[degree] = inverse_factorial
    cosh_series = context(coefficients)
    sech_series = cosh_series.inverse_series_trunc(p - 1)
    assert cosh_series.mul_low(sech_series, p - 1) == context([1])
    assert all(int(sech_series[degree]) == 0 for degree in range(1, p - 1, 2))
    indices = [
        degree
        for degree in range(2, p - 1, 2)
        if int(sech_series[degree]) == 0
    ]
    coefficient_digest = digest_ints(
        [int(sech_series[degree]) for degree in range(p - 1)]
    )
    return indices, coefficient_digest


def kummer_depth(p: int, X: int) -> int:
    depth = 0
    phi = p - 1
    while phi <= X:
        depth += 1
        phi *= p
    return depth


def split_h(H: int, N: int) -> tuple[int, int]:
    S = 1
    for p_sp, valuation in sp.factorint(H).items():
        p = int(p_sp)
        depth = kummer_depth(p, 2 * N + 2)
        S *= p ** min(int(valuation), depth)
    assert H % S == 0
    return S, H // S


def exact_scan_rows(limit: int) -> tuple[list[dict], list[list[int]]]:
    """Exact FLINT gcd scan; rows with H_N>1 plus a digest input."""
    previous = abs(fmpz.euler_number(2))
    nontrivial: list[dict] = []
    digest_rows: list[list[int]] = []
    for N in range(1, limit + 1):
        current = abs(fmpz.euler_number(2 * N + 2))
        H = int(fmpz.gcd(previous, current))
        S, J = split_h(H, N)
        digest_rows.append([N, H, S, J])
        if H > 1:
            nontrivial.append(
                {
                    "N": N,
                    "H": H,
                    "factorization": {
                        str(int(q)): int(a) for q, a in sp.factorint(H).items()
                    },
                    "S": S,
                    "J": J,
                }
            )
        previous = current
    return nontrivial, digest_rows


def main() -> None:
    started = time.perf_counter()

    prime, last_trial_divisor = trial_division_prime(P)
    assert prime
    assert last_trial_divisor == math.isqrt(P) or last_trial_divisor == math.isqrt(P) - 1

    exact_low = fmpz.euler_number(LOW_INDEX)
    exact_high = fmpz.euler_number(HIGH_INDEX)
    H = int(fmpz.gcd(abs(exact_low), abs(exact_high)))
    assert H == P

    recurrence_mod_p2 = euler_even_mod(HIGH_INDEX // 2, MODULUS_SQUARED)
    low_residue = recurrence_mod_p2[LOW_INDEX // 2]
    high_residue = recurrence_mod_p2[HIGH_INDEX // 2]
    assert low_residue == int(exact_low % MODULUS_SQUARED) == 6_825_521_014
    assert high_residue == int(exact_high % MODULUS_SQUARED) == 7_214_529_358
    assert low_residue % P == 0 and high_residue % P == 0
    assert low_residue != 0 and high_residue != 0
    assert math.gcd(low_residue // P, P) == 1
    assert math.gcd(high_residue // P, P) == 1

    irregular_indices, first_period_digest = complete_first_period_indices(P)
    assert irregular_indices == [LOW_INDEX, HIGH_INDEX]

    # This prime is strictly beyond the N=1643 Kummer-period cutoff.
    X = 2 * N_SEED + 2
    assert P - 1 > X
    assert P > X + 1
    assert kummer_depth(P, X) == 0
    S_seed, J_seed = split_h(H, N_SEED)
    assert S_seed == 1 and J_seed == P

    A = (2 * N_SEED + 2) * (2 * N_SEED + 1)
    G = int(fmpz.gcd(A * abs(exact_low), abs(exact_high)))
    assert G == P

    nontrivial_rows, scan_digest_rows = exact_scan_rows(N_SEED)
    J_rows = [row for row in nontrivial_rows if row["J"] > 1]
    assert J_rows == [
        {
            "N": N_SEED,
            "H": P,
            "factorization": {str(P): 1},
            "S": 1,
            "J": P,
        }
    ]

    external_table_url = "https://www.bernoulli.org/download/en_factors.txt"
    payload = {
        "schema": "root_unity_adjacent_euler_irregular_seed_certificate_v1",
        "logical_scope": (
            "Exact finite counterexample to branch incompatibility and index "
            "amplification. It validates the S_N,J_N decomposition but proves no "
            "asymptotic bound for J_N and does not classify e+pi."
        ),
        "seed": {
            "N": N_SEED,
            "p": P,
            "indices": [LOW_INDEX, HIGH_INDEX],
            "phi_p": P - 1,
            "kummer_cutoff": X,
            "gcd_H_N": H,
            "S_N": S_seed,
            "J_N": J_seed,
            "A_N": A,
            "G_N": G,
            "valuations": {str(LOW_INDEX): 1, str(HIGH_INDEX): 1},
            "signed_residues_mod_p_squared": {
                str(LOW_INDEX): low_residue,
                str(HIGH_INDEX): high_residue,
            },
            "complete_first_period_E_irregular_indices": irregular_indices,
            "E_irregularity_index": len(irregular_indices),
        },
        "primality": {
            "method": "deterministic trial division",
            "is_prime": prime,
            "integer_sqrt": math.isqrt(P),
            "last_odd_trial_divisor": last_trial_divisor,
        },
        "exact_Euler_numbers": {
            str(LOW_INDEX): {
                "decimal_digits": len(str(abs(exact_low))),
                "sign": -1 if exact_low < 0 else 1,
                "sha256_abs_decimal": sha256_bytes(str(abs(exact_low)).encode()),
            },
            str(HIGH_INDEX): {
                "decimal_digits": len(str(abs(exact_high))),
                "sign": -1 if exact_high < 0 else 1,
                "sha256_abs_decimal": sha256_bytes(str(abs(exact_high)).encode()),
            },
        },
        "independent_exact_methods": [
            "FLINT exact fmpz Euler numbers and gcd",
            "integer secant-Euler recurrence modulo p^2",
            "truncated reciprocal-cosh identity over F_p",
        ],
        "first_period_sech_coefficient_digest": first_period_digest,
        "finite_scan": {
            "N_max": N_SEED,
            "nontrivial_H_rows": nontrivial_rows,
            "J_greater_than_one_rows": J_rows,
            "all_rows_digest": hashlib.sha256(
                (
                    "".join(
                        ":".join(map(str, row)) + "\n" for row in scan_digest_rows
                    )
                ).encode()
            ).hexdigest(),
            "scope": "Finite exact diagnostic only; no all-N extrapolation.",
        },
        "independent_public_factor_table": {
            "url": external_table_url,
            "listed_rows": {
                "3286": "19 151483 ...",
                "3288": "5 13 43 1097 1663 151483 ...",
            },
            "role": "Contextual corroboration only; replay does not use network data.",
        },
    }

    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    measured_peak_rss_kib = peak_rss_kib()
    assert measured_peak_rss_kib < RSS_LIMIT_KIB
    OUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUT}")
    print(f"sha256 {sha256_bytes(encoded)}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak_rss_kib}")


if __name__ == "__main__":
    main()
