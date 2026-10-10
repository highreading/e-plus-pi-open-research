#!/usr/bin/env python3
"""Deterministic replay for the quadratic tangent-survivor no-go.

The companion source proves the all-r odd-zeta error bound, the adjacent
integral determinant, and the irrationality-measure denominator floor.
This script reconstructs tangent numbers by their quadratic recurrence,
checks an exact finite grid, and certifies the two adjacent irregular pairs.
No finite scan is promoted to an all-r theorem.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from pathlib import Path

import mpmath as mp
from flint import fmpq


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "results"
    / "root_unity_tangent_survivor_exponential_no_go_certificate.json"
)
GRID_MAX = 200
MU_SAFE_TEXT = "5.095412"
# The Colab host has 50 GiB.  This is a safety ceiling, not an allocation.
RSS_SAFETY_CEILING_KIB = 40 * 1024 * 1024


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def v_p(value: int, prime: int) -> int:
    assert value != 0 and prime > 1
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def v2(value: int) -> int:
    assert value > 0
    return (value & -value).bit_length() - 1


def odd_part(value: int) -> int:
    assert value > 0
    return value >> v2(value)


def tangent_numbers(max_index: int) -> list[int]:
    """Return tau_0,...,tau_max_index using tan'=1+tan^2.

    Comparing the z^(2n) coefficient gives
      tau_(n+1)=sum_{k=1}^n C(2n,2k-1) tau_k tau_(n+1-k).
    """
    assert max_index >= 1
    values = [0, 1]
    for n in range(1, max_index):
        next_value = sum(
            math.comb(2 * n, 2 * k - 1)
            * values[k]
            * values[n + 1 - k]
            for k in range(1, n + 1)
        )
        values.append(next_value)
    return values


def tangent_from_bernoulli(index: int) -> int:
    bernoulli = fmpq.bernoulli(2 * index)
    value = (
        bernoulli
        * (1 << (2 * index))
        * ((1 << (2 * index)) - 1)
        / (2 * index)
    )
    if index % 2 == 0:
        value = -value
    assert value.denominator == 1 and value > 0
    return int(value.numerator)


def reduced_pair(tau: list[int], r: int) -> tuple[int, int, int]:
    raw_p = 8 * r * (2 * r + 1) * tau[r]
    raw_q = tau[r + 1]
    common = math.gcd(raw_p, raw_q)
    p = raw_p // common
    q = raw_q // common
    assert math.gcd(p, q) == 1
    return p, q, common


def bernoulli_seed(prime: int, index: int) -> dict[str, object]:
    bernoulli = fmpq.bernoulli(index)
    numerator = int(bernoulli.numerator)
    denominator = int(bernoulli.denominator)
    assert v_p(numerator, prime) == 1
    assert denominator % prime != 0
    assert pow(2, index, prime) != 1
    return {
        "prime": prime,
        "bernoulli_index": index,
        "B_numerator": str(numerator),
        "B_denominator": str(denominator),
        "numerator_v_p": v_p(numerator, prime),
        "numerator_mod_p_squared": numerator % (prime * prime),
        "denominator_mod_p": denominator % prime,
        "two_to_index_mod_p": pow(2, index, prime),
    }


def main() -> None:
    started = time.perf_counter()
    mp.mp.dps = 300
    tau = tangent_numbers(GRID_MAX + 2)

    # Independent exact Bernoulli reconstruction on the full declared grid.
    for index in range(1, GRID_MAX + 2):
        assert tau[index] == tangent_from_bernoulli(index)

    q_digest_lines: list[str] = []
    determinant_digest_lines: list[str] = []
    normalized_errors: list[mp.mpf] = []
    product_log_margins: list[mp.mpf] = []
    selected_rows: list[dict[str, object]] = []
    selected_adjacent_rows: list[dict[str, object]] = []
    odd_consecutive_gcd_hits: list[dict[str, object]] = []

    pi_squared = mp.pi * mp.pi
    for r in range(1, GRID_MAX + 1):
        p, q, common = reduced_pair(tau, r)
        next_p, next_q, _ = reduced_pair(tau, r + 1)

        assert q % 2 == 1
        assert v2(p) == 1 + v2(r + 1)
        assert v2(tau[r]) == 2 * r - 2 - v2(r)

        determinant = p * next_q - next_p * q
        assert determinant > 0
        assert v2(determinant) == 1

        approximation = mp.mpf(p) / q
        error = approximation - pi_squared
        upper = mp.mpf(5) * pi_squared / 2 * mp.power(9, -r)
        assert 0 < error < upper
        normalized = error * mp.power(9, r + 1) / (8 * pi_squared)
        normalized_errors.append(normalized)

        product_margin = (
            mp.log(mp.mpf(q) * next_q)
            - r * mp.log(9)
            - mp.log(mp.mpf(4) / (5 * pi_squared))
        )
        assert product_margin > 0
        product_log_margins.append(product_margin)

        q_digest_lines.append(f"{r}:{p}:{q}:{common}\n")
        determinant_digest_lines.append(f"{r}:{determinant}\n")

        consecutive = math.gcd(tau[r], tau[r + 1])
        consecutive_odd = odd_part(consecutive)
        if consecutive_odd > 1:
            odd_consecutive_gcd_hits.append(
                {
                    "r": r,
                    "odd_part": str(consecutive_odd),
                    "two_adic_valuation": v2(consecutive),
                    "full_gcd": str(consecutive),
                }
            )

        if r in {1, 2, 5, 10, 45, 100, 168, GRID_MAX}:
            selected_rows.append(
                {
                    "r": r,
                    "G": str(common),
                    "P_digits": len(str(p)),
                    "Q_digits": len(str(q)),
                    "Q_is_odd": q % 2 == 1,
                    "P_v2": v2(p),
                    "normalized_error": mp.nstr(normalized, 60),
                    "strict_upper_margin": mp.nstr(upper - error, 40),
                }
            )
            selected_adjacent_rows.append(
                {
                    "r": r,
                    "determinant_digits": len(str(determinant)),
                    "determinant_v2": v2(determinant),
                    "Q_r_digits": len(str(q)),
                    "Q_next_digits": len(str(next_q)),
                    "product_log_margin": mp.nstr(product_margin, 60),
                }
            )

    assert odd_consecutive_gcd_hits == [
        {
            "r": 45,
            "odd_part": "587",
            "two_adic_valuation": 88,
            "full_gcd": str((1 << 88) * 587),
        },
        {
            "r": 168,
            "odd_part": "491",
            "two_adic_valuation": 331,
            "full_gcd": str((1 << 331) * 491),
        },
    ]

    irregular_seeds = [
        bernoulli_seed(587, 90),
        bernoulli_seed(587, 92),
        bernoulli_seed(491, 336),
        bernoulli_seed(491, 338),
    ]

    assert math.gcd(tau[45], tau[46]) == (1 << 88) * 587
    assert math.gcd(tau[168], tau[169]) == (1 << 331) * 491
    assert math.gcd((1 << 90) - 1, (1 << 92) - 1) == 3
    assert math.gcd((1 << 336) - 1, (1 << 338) - 1) == 3

    mu_safe = mp.mpf(MU_SAFE_TEXT)
    lower_constant = mp.log(9) / mu_safe
    payload = {
        "schema": "root_unity_tangent_survivor_exponential_no_go_v1",
        "logical_scope": (
            "Finite exact/high-precision replay supporting analytic all-r "
            "odd-zeta, adjacent-determinant, and irrationality-measure "
            "theorems. The finite grid does not prove an all-r gcd law, a "
            "factorial lower bound, or any classification of e+pi."
        ),
        "definitions": {
            "tau_r": "tan(z)=sum_(r>=1) tau_r*z^(2r-1)/(2r-1)!",
            "G_r": "gcd(tau_(r+1),8*r*(2r+1)*tau_r)",
            "P_r": "8*r*(2r+1)*tau_r/G_r",
            "Q_r": "tau_(r+1)/G_r",
            "A_r": "sum_(j>=0) (2j+1)^(-2r)",
        },
        "all_r_theorem_proved_in_source": {
            "exact_ratio": "P_r/Q_r=pi^2*A_r/A_(r+1)>pi^2",
            "uniform_error": "0<P_r/Q_r-pi^2<(5*pi^2/2)*9^(-r)",
            "error_asymptotic": (
                "P_r/Q_r-pi^2=(8*pi^2/9)*9^(-r)"
                "*(1+O((9/25)^r))"
            ),
            "individual_floor": (
                "for every epsilon>0, log Q_r >= "
                "(log(9)/(5.095412+epsilon))*r+O_epsilon(1)"
            ),
            "no_small_subsequence": "no infinite subsequence has log Q_r=o(r)",
            "adjacent_determinant": (
                "D_r=P_r*Q_(r+1)-P_(r+1)*Q_r>0 and v2(D_r)=1"
            ),
            "adjacent_product_floor": "Q_r*Q_(r+1)>(4/(5*pi^2))*9^r",
        },
        "irrationality_measure": {
            "source": (
                "W. Zudilin, Russian Math. Surveys 68:6 (2013), "
                "1133-1135, doi:10.1070/RM2013v068n06ABEH004872"
            ),
            "published_mu_upper": "5.09541178...",
            "safe_decimal_upper_used": MU_SAFE_TEXT,
            "liminf_log_Q_over_r_lower_decimal": mp.nstr(
                lower_constant, 60
            ),
        },
        "finite_grid": {
            "r_min": 1,
            "r_max": GRID_MAX,
            "precision_decimal_digits": mp.mp.dps,
            "tangent_reconstruction_methods": [
                "quadratic recurrence from tan'=1+tan^2",
                "Bernoulli closed formula using exact FLINT rationals",
            ],
            "all_reconstructions_match": True,
            "reduced_rows_sha256": sha256_bytes(
                "".join(q_digest_lines).encode()
            ),
            "adjacent_determinant_rows_sha256": sha256_bytes(
                "".join(determinant_digest_lines).encode()
            ),
            "normalized_error_min": mp.nstr(min(normalized_errors), 60),
            "normalized_error_max": mp.nstr(max(normalized_errors), 60),
            "adjacent_product_log_margin_min": mp.nstr(
                min(product_log_margins), 60
            ),
            "selected_rows": selected_rows,
            "selected_adjacent_rows": selected_adjacent_rows,
            "odd_consecutive_gcd_hits_in_grid": odd_consecutive_gcd_hits,
        },
        "irregular_pair_certificates": {
            "exact_bernoulli_seeds": irregular_seeds,
            "exact_tangent_gcds": [
                "gcd(tau_45,tau_46)=2^88*587",
                "gcd(tau_168,tau_169)=2^331*491",
            ],
            "cyclotomic_gcds": [
                "gcd(2^90-1,2^92-1)=3",
                "gcd(2^336-1,2^338-1)=3",
            ],
            "kummer_progressions_proved_in_source": [
                "587 divides gcd(tau_r,tau_(r+1)) for r=45+293k "
                "when 587 does not divide r(r+1)",
                "491 divides gcd(tau_r,tau_(r+1)) for r=168+245k "
                "when 491 does not divide r(r+1)",
            ],
        },
        "barrier": (
            "The individual exponential floor rules out the required "
            "log Q_r=o(r) subsequence. It is smaller by a factor log r "
            "than the full 2r log r tangent scale. Adjacent irregular "
            "Bernoulli pairs refute universal odd coprimality but do not "
            "preclude a deeper factorial-scale lower bound."
        ),
    }

    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    measured_peak_rss_kib = peak_rss_kib()
    assert measured_peak_rss_kib < RSS_SAFETY_CEILING_KIB
    OUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUT}")
    print(f"sha256 {sha256_bytes(encoded)}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak_rss_kib}")
    print("hardware_accelerator not used: exact big-integer arithmetic is CPU-bound")


if __name__ == "__main__":
    main()
