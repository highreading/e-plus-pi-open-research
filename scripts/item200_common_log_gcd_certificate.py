#!/usr/bin/env python3
"""Exact certificate for Item 200's normalized common-log gcd audit.

The all-m arguments are written in the companion report.  This checker is
self-contained: it replays the coefficient identities, the forced Cartier
divisor, the PNT-row/Item-149 overlap, and the local recurrence-kernel
calculation using only Python's standard library.  Its JSON contains no host
paths, timestamps, or elapsed-time fields.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item200_common_log_gcd_certificate.json"
PINNED_DEPENDENCIES = {
    "sources/item194_rankzero_pnt_report.md": "9062718b5dbb0781f1084b6496adbf0dfffb836838e2f202a1257c5f23b095b0",
    "scripts/item194_rankzero_pnt_certificate.py": "ef23f22deea2fa4053ee8af24f9e73e70a2e50a74e805ddcc04426100ebdf02e",
    "sources/item197_common_log_locus_report.md": "2241656ac9c47e81b5026449a97c15bed7d35290bf2b6a91cdfed4bb3fe3683c",
    "scripts/item197_common_log_locus_certificate.py": "f85c36169c7eb0aee3fb73f8030d3ddb2296b00077370012be84479eea9aeeb9",
    "sources/mixed_cubic_boundary_cartier_content_and_recurrence.md": "286d9cf4d3591a1a9b9fefc6dd3ee3dcc9f7c2ba49a73310909491814544d9e8",
    "sources/mixed_cubic_small_prime_rank_one_cartier_mass.md": "593e1f69809c44245bd2d79bf1a503f96d1972a39ba17ea43ba7cd9f4b0e124b",
}


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(flags) if flag]


def coefficient_c(m: int, nu: int) -> int:
    """The defining coefficient C_nu(m), by an exact finite sum."""
    index = 4 * m + nu
    extra = 1 + 3 * nu
    denominator_power = 4 * m + 1 + nu
    answer = 0
    for b in range(index // 2 + 1):
        remaining = index - 2 * b
        numerator_coefficient = 0
        for q in range(extra + 1):
            a = remaining - q
            if 0 <= a <= 6 * m:
                numerator_coefficient += (
                    (-1) ** a * math.comb(6 * m, a) * math.comb(extra, q)
                )
        answer += (
            (-1) ** b
            * math.comb(denominator_power + b - 1, b)
            * numerator_coefficient
        )
    return answer


def scalar_coefficients(m: int) -> list[int]:
    """Return g_{m,k}, 0 <= k <= 4m+1, from the exact four-step recurrence."""
    target = 4 * m + 1
    coefficient = [1]
    for degree in range(target):
        rhs = (20 * m - 8 - 10 * degree) * coefficient[degree]
        if degree >= 1:
            rhs += (
                2
                * (10 * degree + 10 - 20 * m)
                * coefficient[degree - 1]
            )
        if degree >= 2:
            rhs += (
                4
                * (10 * m - 5 * degree - 6)
                * coefficient[degree - 2]
            )
        if degree >= 3:
            rhs += (
                8
                * (degree + 1 - 4 * m)
                * coefficient[degree - 3]
            )
        divisor = -2 * (degree + 1)
        quotient, remainder = divmod(rhs, divisor)
        if remainder:
            raise AssertionError((m, degree, rhs, divisor))
        coefficient.append(quotient)
    return coefficient


def scalar_pair(m: int) -> tuple[int, int, list[int]]:
    coefficient = scalar_coefficients(m)
    n = 4 * m
    c0 = coefficient[n] - 2 * coefficient[n - 1] + 2 * coefficient[n - 2]
    c1 = coefficient[n + 1]
    return c0, c1, coefficient


def cartier_degree(modulus: int, n: int, k: int) -> int:
    r = n % modulus
    t = k % modulus
    return 2 * r if t == 0 else 2 * r + 3 * (modulus - t)


def forced_primes(m: int, primes: list[int]) -> list[int]:
    return [
        p
        for p in primes
        if p & 1
        and cartier_degree(p, 6 * m, 4 * m + 1) <= p - 2
        and cartier_degree(p, 6 * m, 4 * m + 2) <= p - 2
    ]


def row_parameters(m: int, p: int) -> tuple[int, int, int]:
    """Recover the unique (j,s,r) rank-zero row from p in P_m."""
    n, k = 6 * m, 4 * m + 1
    b = k // p
    if b % 2:
        raise AssertionError((m, p, "odd denominator quotient", b))
    j = b // 2
    s_numerator = (2 * j + 1) * p - k
    if s_numerator % 2:
        raise AssertionError((m, p, "odd s numerator", s_numerator))
    s = s_numerator // 2
    r = n - (3 * j + 1) * p
    if not (1 <= s <= (p - 3) // 6):
        raise AssertionError((m, p, j, s, "s range"))
    if r != (p - 6 * s - 3) // 2 or not (0 <= r < p):
        raise AssertionError((m, p, j, s, r, "r identity"))
    if k != (2 * j + 1) * p - 2 * s:
        raise AssertionError((m, p, j, s, "row identity"))
    if (cartier_degree(p, n, k), cartier_degree(p, n, k + 1)) != (
        p - 3,
        p - 6,
    ):
        raise AssertionError((m, p, j, s, "degree identity"))
    return j, s, r


def largest_prime_power_at_most(p: int, limit: int) -> int:
    answer = 1
    while answer <= limit // p:
        answer *= p
    return answer


def in_item149_h(m: int, p: int) -> bool:
    if not (p & 1 and p < 2 * m):
        return False
    q = largest_prime_power_at_most(p, 4 * m + 1)
    return (
        cartier_degree(q, 6 * m, 4 * m + 1) <= 2 * q - 2
        and cartier_degree(q, 6 * m, 4 * m + 2) <= 2 * q - 2
    )


def product(values: list[int]) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode(
        "ascii"
    )
    return hashlib.sha256(payload).hexdigest()


def verify_local_recurrence_kernel(m: int) -> None:
    """Check the exact rank-three local matrix and its nonzero kernel."""
    # Columns are (g_n,g_{n-1},g_{n-2},g_{n-3}), n=4m.
    matrix = (
        (1, -2, 2, 0),
        (-20 * m - 8, 40 * m + 20, -40 * m - 24, 8),
        (-8 * m, 20 * m - 2, -40 * m, 40 * m + 4),
    )
    kernel = (0, 2, 2, 1)
    if any(sum(a * b for a, b in zip(row, kernel)) for row in matrix):
        raise AssertionError((m, "kernel"))

    # The first 3x3 minor is -16(4m+1), hence the rank is exactly three
    # over Q and over every F_p with p not dividing 2(4m+1).
    a, b, c = (matrix[row][:3] for row in range(3))
    determinant = (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )
    if determinant != -16 * (4 * m + 1):
        raise AssertionError((m, determinant, "minor"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m-max", type=int, default=160)
    parser.add_argument("--direct-crosscheck-m-max", type=int, default=80)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if not (1 <= args.direct_crosscheck_m_max <= args.m_max):
        raise ValueError("require 1 <= direct crosscheck maximum <= m maximum")

    primes = primes_upto(6 * args.m_max)
    forced_incidence_count = 0
    interval_incidence_count = 0
    pnt_row_count = 0
    item149_overlap_count = 0
    exceptional_rows: list[dict[str, int]] = []
    rows: list[tuple[int, ...]] = []
    normalized_gcd_max = {"bits": 0, "m": 0}
    power_of_two_odd_witnesses: list[int] = []

    for m in range(1, args.m_max + 1):
        c0, c1, coefficients = scalar_pair(m)
        if m <= args.direct_crosscheck_m_max:
            direct = (coefficient_c(m, 0), coefficient_c(m, 1))
            if direct != (c0, c1):
                raise AssertionError((m, direct, (c0, c1), "coefficient bridge"))
        if (c0 & 1) != (math.comb(6 * m, 4 * m) & 1) or (c1 & 1):
            raise AssertionError((m, c0 & 1, c1 & 1, "parity identity"))
        if m & (m - 1) == 0:
            if not (c0 & 1):
                raise AssertionError((m, "power-of-two nonvanishing witness"))
            power_of_two_odd_witnesses.append(m)

        n = 4 * m
        identity_left = 2 * (4 * m + 1) * coefficients[n]
        identity_right = (
            (10 * m + 2) * (10 * m + 3) * c0
            - (4 * m + 1) * (10 * m + 1) * c1
        )
        if identity_left != identity_right:
            raise AssertionError((m, "target recurrence identity"))
        verify_local_recurrence_kernel(m)

        p_at_m = [p for p in primes if p <= 6 * m]
        forced = forced_primes(m, p_at_m)
        interval = [p for p in p_at_m if 4 * m + 1 < p <= 6 * m]
        forced_set = set(forced)
        if not set(interval) <= forced_set:
            raise AssertionError((m, interval, forced, "j=0 containment"))

        f_m = product(forced)
        d_m = product(interval)
        if c0 % f_m or c1 % f_m or f_m % d_m:
            raise AssertionError((m, "forced divisor"))
        normalized_gcd = math.gcd(abs(c0 // f_m), abs(c1 // f_m))
        if normalized_gcd.bit_length() > normalized_gcd_max["bits"]:
            normalized_gcd_max = {"bits": normalized_gcd.bit_length(), "m": m}

        forced_incidence_count += len(forced)
        interval_incidence_count += len(interval)
        for p in forced:
            j, s, _r = row_parameters(m, p)
            if (j == 0) != (p in interval):
                raise AssertionError((m, p, j, "j=0 interval equality"))
            pnt = j >= 1 and 3 * j + 1 < p
            if not pnt:
                continue
            pnt_row_count += 1
            q = largest_prime_power_at_most(p, 4 * m + 1)
            if not (p < 2 * m and q == p and in_item149_h(m, p)):
                raise AssertionError((m, p, j, s, q, "Item149 overlap"))
            item149_overlap_count += 1
            q0, q1 = (c0 // p) % p, (c1 // p) % p
            exceptional = q0 == 0 and q1 == 0
            if exceptional:
                exceptional_rows.append({"m": m, "p": p, "j": j, "s": s})
            rows.append((m, p, j, s, q0, q1, int(exceptional)))

    if item149_overlap_count != pnt_row_count:
        raise AssertionError("PNT/Item149 overlap count")

    output = {
        "schema": "item200-common-log-gcd-v1",
        "status": {
            "full_forced_divisor_Fm": "PROVED_IN_REPORT",
            "raw_subexponential_gcd_or_radical_bound": "IMPOSSIBLE_ALONG_M_POWERS_OF_TWO",
            "normalized_exceptional_bridge": "PROVED_IN_REPORT",
            "local_recurrence_resultant_closure": "PROVED_SCOPED_NO_GO",
            "normalized_exceptional_radical_subexponential": "OPEN",
            "finite_nonoccurrence": "EXACT_FINITE_ONLY",
        },
        "definitions": {
            "C_nu": "[z^(4m+nu)](1-z)^(6m)(1+z)^(1+3nu)/(1+z^2)^(4m+1+nu)",
            "P_m": "odd p with d_p(6m,4m+1),d_p(6m,4m+2)<=p-2",
            "F_m": "product of p in P_m; exactly the archived squarefree Cartier G_m",
            "D_m_zero_band": "product of primes 4m+1<p<=6m; the j=0 subproduct of F_m",
            "Cbar_nu": "C_nu/F_m",
            "normalized_exceptional_bridge": "R_m divides gcd(Cbar_0,Cbar_1)",
        },
        "exact_rates": {
            "log_Fm_per_m": "-4*log(2)+pi/sqrt(3)+3*log(3)",
            "log_Dm_zero_band_per_m": "2",
            "log_PNT_j_ge_1_band_per_m": "-4*log(2)+pi/sqrt(3)+3*log(3)-2",
            "log_PNT_j_ge_1_band_per_6m": "(-4*log(2)+pi/sqrt(3)+3*log(3)-2)/6",
            "decimal_unit_audit": {
                "per_m": "0.3370475079987658",
                "per_6m": "0.0561745846664610",
            },
        },
        "parity": {
            "C0_mod_2": "binom(6m,4m) mod 2",
            "C1_mod_2": "0",
            "all_m_power_of_two": "C0(m) is odd, so the pair is nonzero",
        },
        "recurrence": {
            "generating_polynomial_series": "sum_k g_(m,k)v^k=((1-v)(1-2v))^(6m)/(1-2v+2v^2)^(4m+2)",
            "pair": "C0=g_(m,4m)-2g_(m,4m-1)+2g_(m,4m-2); C1=g_(m,4m+1)",
            "target_identity": "2(4m+1)g_(m,4m)=(10m+2)(10m+3)C0-(4m+1)(10m+1)C1",
            "local_matrix_rank": "3 when 2(4m+1) is a unit",
            "local_kernel": "span(0,2,2,1) in coordinates (g_4m,g_(4m-1),g_(4m-2),g_(4m-3))",
            "scope": "two target congruences plus the two adjacent recurrence rows do not force the local state to vanish; a global boundary/transfer argument is still possible",
        },
        "pinned_dependencies": PINNED_DEPENDENCIES,
        "finite_replay": {
            "m_max": args.m_max,
            "direct_crosscheck_m_max": args.direct_crosscheck_m_max,
            "forced_prime_incidences": forced_incidence_count,
            "j0_interval_incidences": interval_incidence_count,
            "pnt_rows": pnt_row_count,
            "item149_overlap_rows": item149_overlap_count,
            "common_second_digit_rows": len(exceptional_rows),
            "common_second_digit_diagnostics": exceptional_rows,
            "pnt_row_digest": row_digest(rows),
            "normalized_gcd_max_bits": normalized_gcd_max,
            "power_of_two_odd_witnesses": power_of_two_odd_witnesses,
            "warning": "all counts, nonoccurrence, and bit sizes are exact finite diagnostics only",
        },
        "external_numeric_backend": None,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "m_max": args.m_max,
                "pnt_rows": pnt_row_count,
                "common_second_digit_rows": len(exceptional_rows),
                "pnt_row_digest": output["finite_replay"]["pnt_row_digest"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
