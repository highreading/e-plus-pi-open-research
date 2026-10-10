#!/usr/bin/env python3
"""Certificate for the quadratic Euler beta-tail denominator floors.

The companion source proves the all-N beta inequalities, the adjacent
integral-determinant bound, and the consequence of Zudilin's irrationality
exponent.  This replay checks exact reduced Euler ratios and high-precision
instances on a declared grid; the finite grid is not used as an all-N proof.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from pathlib import Path

import mpmath as mp
from flint import fmpz


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "results"
    / "root_unity_quadratic_euler_beta_denominator_certificate.json"
)
RSS_LIMIT_KIB = 2 * 1024 * 1024
GRID_MAX = 120
SEED_N = 1643
MU_SAFE_TEXT = "5.095412"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def reduced_pair(N: int) -> tuple[fmpz, fmpz, fmpz]:
    low = abs(fmpz.euler_number(2 * N))
    high = abs(fmpz.euler_number(2 * N + 2))
    A = (2 * N + 2) * (2 * N + 1)
    G = fmpz.gcd(A * low, high)
    P = high // G
    Q = A * low // G
    assert fmpz.gcd(P, Q) == 1
    return P, Q, G


def v2_positive(value: int) -> int:
    assert value > 0
    return (value & -value).bit_length() - 1


def main() -> None:
    started = time.perf_counter()
    mp.mp.dps = 300
    alpha = mp.mpf(4) / (mp.pi * mp.pi)
    mu_safe = mp.mpf(MU_SAFE_TEXT)

    q_digest_lines: list[str] = []
    determinant_digest_lines: list[str] = []
    normalized_errors: list[mp.mpf] = []
    adjacent_product_log_margins: list[mp.mpf] = []
    selected_rows: list[dict] = []
    selected_adjacent_rows: list[dict] = []

    for N in range(1, GRID_MAX + 1):
        P, Q, G = reduced_pair(N)
        p_int = int(P)
        q_int = int(Q)
        s = 2 * N + 1
        approximation = mp.mpf(p_int) / q_int
        error = approximation - alpha
        lower = alpha * (
            mp.mpf(8) / mp.power(3, s + 2)
            - mp.mpf(24) / mp.power(5, s + 2)
        )
        upper = (
            alpha
            * (mp.mpf(8) / mp.power(3, s + 2))
            / (1 - mp.power(3, -s))
        )
        assert lower < error < upper
        normalized = (
            error
            * mp.pi
            * mp.pi
            * mp.power(3, 2 * N + 3)
            / 32
        )
        normalized_errors.append(normalized)
        q_digest_lines.append(f"{N}:{q_int}\n")

        next_P, next_Q, _ = reduced_pair(N + 1)
        next_p_int = int(next_P)
        next_q_int = int(next_Q)
        determinant = p_int * next_q_int - next_p_int * q_int
        assert determinant > 0
        assert v2_positive(determinant) == 1
        next_error = mp.mpf(next_p_int) / next_q_int - alpha
        assert error > next_error > 0

        coarse_lower_ratio = 1 - 3 * mp.power(mp.mpf(3) / 5, s + 2)
        coarse_next_upper_ratio = 1 / (
            9 * (1 - mp.power(3, -(s + 2)))
        )
        assert coarse_lower_ratio > mp.mpf(3) / 4
        assert coarse_next_upper_ratio < mp.mpf(1) / 8

        determinant_upper = (
            mp.mpf(432)
            / (13 * mp.pi * mp.pi)
            * q_int
            * next_q_int
            * mp.power(3, -(2 * N + 3))
        )
        assert mp.mpf(determinant) < determinant_upper
        product_log_margin = (
            mp.log(mp.mpf(q_int) * next_q_int)
            - (2 * N + 3) * mp.log(3)
            - mp.log(13 * mp.pi * mp.pi / 216)
        )
        assert product_log_margin > 0
        adjacent_product_log_margins.append(product_log_margin)
        determinant_digest_lines.append(f"{N}:{determinant}\n")

        if N in {1, 2, 5, 10, 20, 40, 80, GRID_MAX}:
            selected_rows.append(
                {
                    "N": N,
                    "G": str(G),
                    "P_digits": len(str(P)),
                    "Q_digits": len(str(Q)),
                    "normalized_error": mp.nstr(normalized, 50),
                    "strict_lower_margin": mp.nstr(error - lower, 30),
                    "strict_upper_margin": mp.nstr(upper - error, 30),
                }
            )
            selected_adjacent_rows.append(
                {
                    "N": N,
                    "determinant_digits": len(str(determinant)),
                    "determinant_v2": v2_positive(determinant),
                    "Q_N_digits": len(str(Q)),
                    "Q_next_digits": len(str(next_Q)),
                    "product_log_margin": mp.nstr(
                        product_log_margin, 50
                    ),
                }
            )

    seed_P, seed_Q, seed_G = reduced_pair(SEED_N)
    assert int(seed_G) == 151_483
    seed_p_text = str(seed_P)
    seed_q_text = str(seed_Q)

    constant = 2 * mp.log(3) / mu_safe
    payload = {
        "schema": "root_unity_quadratic_euler_beta_denominator_certificate_v1",
        "logical_scope": (
            "Finite exact/high-precision replay supporting an analytic all-N "
            "beta-tail and adjacent-determinant theorem. The grid does not "
            "prove the irrationality measure, an asymptotic J_N bound, or "
            "any classification of e+pi."
        ),
        "definitions": {
            "A_N": "(2N+2)(2N+1)",
            "G_N": "gcd(A_N*abs(E_2N),abs(E_(2N+2)))",
            "P_N": "abs(E_(2N+2))/G_N",
            "Q_N": "A_N*abs(E_2N)/G_N",
            "alpha": "4/pi^2",
        },
        "all_N_theorem_checked_symbolically_in_source": {
            "exact_ratio": "P_N/Q_N=(4/pi^2)*beta(2N+3)/beta(2N+1)",
            "lower_error": (
                "alpha*(8/3^(2N+3)-24/5^(2N+3))"
            ),
            "upper_error": (
                "alpha*(8/3^(2N+3))/(1-3^(-(2N+1)))"
            ),
            "asymptotic_error": (
                "32/(pi^2*3^(2N+3))*(1+O((3/5)^(2N+1)))"
            ),
            "adjacent_determinant": (
                "D_N=P_N*Q_(N+1)-P_(N+1)*Q_N>0 and v2(D_N)=1"
            ),
            "adjacent_product_floor": (
                "Q_N*Q_(N+1)>(13*pi^2/216)*3^(2N+3)"
            ),
            "adjacent_asymptotic_consequences": (
                "liminf (log Q_N+log Q_(N+1))/N>=2 log 3; "
                "limsup log Q_N/N>=log 3"
            ),
        },
        "irrationality_measure": {
            "source": (
                "W. Zudilin, Russian Math. Surveys 68:6 (2013), "
                "1133-1135, doi:10.1070/RM2013v068n06ABEH004872"
            ),
            "published_mu_upper": "5.09541178...",
            "safe_decimal_upper_used": MU_SAFE_TEXT,
            "liminf_log_Q_over_N_lower_decimal": mp.nstr(constant, 50),
            "meaning": (
                "For every epsilon>0, log Q_N >= "
                "(2 log 3/(mu_bar+epsilon))*N+O_epsilon(1)."
            ),
        },
        "finite_grid": {
            "N_min": 1,
            "N_max": GRID_MAX,
            "precision_decimal_digits": mp.mp.dps,
            "Q_rows_sha256": sha256_bytes(
                "".join(q_digest_lines).encode()
            ),
            "adjacent_determinant_rows_sha256": sha256_bytes(
                "".join(determinant_digest_lines).encode()
            ),
            "normalized_error_min": mp.nstr(min(normalized_errors), 50),
            "normalized_error_max": mp.nstr(max(normalized_errors), 50),
            "adjacent_product_log_margin_min": mp.nstr(
                min(adjacent_product_log_margins), 50
            ),
            "adjacent_determinant_v2_values": [1],
            "selected_rows": selected_rows,
            "selected_adjacent_rows": selected_adjacent_rows,
        },
        "N_1643_exact_metadata": {
            "G_N": str(seed_G),
            "P_digits": len(seed_p_text),
            "Q_digits": len(seed_q_text),
            "P_sha256_decimal": sha256_bytes(seed_p_text.encode()),
            "Q_sha256_decimal": sha256_bytes(seed_q_text.encode()),
        },
        "barrier": (
            "The adjacent determinant gives an unconditional exponential "
            "floor for Q_N*Q_(N+1), while the pi^2 measure gives an "
            "individual log Q_N=Omega(N) floor. Both yield only O(N) "
            "improvements in log G_N and do not imply "
            "log G_N=o(N log N)."
        ),
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
