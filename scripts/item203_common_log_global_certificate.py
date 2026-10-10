#!/usr/bin/env python3
"""Deterministic checks for Item 203's global common-log transfer.

The all-row arguments are in the companion report.  This self-contained
checker verifies the support gap, the five Frobenius-defect coordinates,
the cancellation-aware recurrence gauge, and the exact local-line test on
a finite range.  Its output deliberately contains no host path, timestamp,
elapsed time, or external numeric-backend field.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item203_common_log_global_certificate.json"
PINNED_DEPENDENCIES = {
    "sources/item194_rankzero_pnt_report.md": "9062718b5dbb0781f1084b6496adbf0dfffb836838e2f202a1257c5f23b095b0",
    "scripts/item194_rankzero_pnt_certificate.py": "ef23f22deea2fa4053ee8af24f9e73e70a2e50a74e805ddcc04426100ebdf02e",
    "sources/item197_common_log_locus_report.md": "2241656ac9c47e81b5026449a97c15bed7d35290bf2b6a91cdfed4bb3fe3683c",
    "scripts/item197_common_log_locus_certificate.py": "f85c36169c7eb0aee3fb73f8030d3ddb2296b00077370012be84479eea9aeeb9",
    "sources/item200_common_log_gcd_report.md": "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "scripts/item200_common_log_gcd_certificate.py": "26ef60a6f89d569d7f22fdd504dd76f5b3b6a2c11d9b99f2c56a0be645c1396b",
}

A_POLY = [1, -3, 2]
D_POLY = [1, -2, 2]


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


def scalar_coefficients(m: int) -> list[int]:
    """Return g_(m,k), 0 <= k <= 4m+1, by the exact recurrence."""
    target = 4 * m + 1
    coefficient = [1]
    for degree in range(target):
        rhs = (20 * m - 8 - 10 * degree) * coefficient[degree]
        if degree >= 1:
            rhs += 2 * (10 * degree + 10 - 20 * m) * coefficient[degree - 1]
        if degree >= 2:
            rhs += 4 * (10 * m - 5 * degree - 6) * coefficient[degree - 2]
        if degree >= 3:
            rhs += 8 * (degree + 1 - 4 * m) * coefficient[degree - 3]
        divisor = -2 * (degree + 1)
        quotient, remainder = divmod(rhs, divisor)
        if remainder:
            raise AssertionError((m, degree, "nonintegral recurrence"))
        coefficient.append(quotient)
    return coefficient


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
    b = (4 * m + 1) // p
    if b % 2:
        raise AssertionError((m, p, "odd quotient"))
    j = b // 2
    s_num = (2 * j + 1) * p - (4 * m + 1)
    if s_num % 2:
        raise AssertionError((m, p, "odd s numerator"))
    s = s_num // 2
    r = 6 * m - (3 * j + 1) * p
    if not (1 <= s <= (p - 3) // 6):
        raise AssertionError((m, p, j, s, "s range"))
    if r != (p - 6 * s - 3) // 2:
        raise AssertionError((m, p, j, s, r, "r identity"))
    return j, s, r


def convolution_mod(
    left: list[int], right: list[int], modulus: int, limit: int | None = None
) -> list[int]:
    if not left or not right:
        return []
    size = len(left) + len(right) - 1
    if limit is not None:
        size = min(size, limit + 1)
    answer = [0] * size
    for i, a in enumerate(left):
        if not a:
            continue
        stop = min(len(right), size - i)
        for j in range(stop):
            answer[i + j] = (answer[i + j] + a * right[j]) % modulus
    return answer


def power_series_mod(
    base: list[int], exponent: int, limit: int, modulus: int
) -> list[int]:
    answer = [1]
    factor = [value % modulus for value in base[: limit + 1]]
    while exponent:
        if exponent & 1:
            answer = convolution_mod(answer, factor, modulus, limit)
        exponent >>= 1
        if exponent:
            factor = convolution_mod(factor, factor, modulus, limit)
    answer.extend([0] * (limit + 1 - len(answer)))
    return answer


def inverse_series_mod(base: list[int], limit: int, modulus: int) -> list[int]:
    if not base or base[0] % modulus != 1:
        raise ValueError("series must have constant coefficient one")
    answer = [1]
    for degree in range(1, limit + 1):
        value = 0
        for k in range(1, min(degree, len(base) - 1) + 1):
            value += base[k] * answer[degree - k]
        answer.append((-value) % modulus)
    return answer


def ratio_series_mod(
    numerator_exponent: int,
    denominator_exponent: int,
    limit: int,
    modulus: int,
) -> list[int]:
    numerator = power_series_mod(A_POLY, numerator_exponent, limit, modulus)
    inverse_d = inverse_series_mod(D_POLY, limit, modulus)
    denominator = power_series_mod(
        inverse_d, denominator_exponent, limit, modulus
    )
    return convolution_mod(numerator, denominator, modulus, limit)


@lru_cache(maxsize=None)
def frobenius_delta(poly_key: tuple[int, ...], p: int) -> tuple[int, ...]:
    """Return (R(v)^p-R(v^p))/p modulo p, coefficientwise."""
    poly = list(poly_key)
    modulus = p * p
    powered = power_series_mod(poly, p, p * (len(poly) - 1), modulus)
    evaluated = [0] * len(powered)
    for degree, value in enumerate(poly):
        evaluated[p * degree] = value % modulus
    answer = []
    for left, right in zip(powered, evaluated):
        difference = (left - right) % modulus
        if difference % p:
            raise AssertionError((p, poly, "Frobenius difference"))
        answer.append((difference // p) % p)
    return tuple(answer)


@lru_cache(maxsize=None)
def moving_polynomial(p: int, s: int) -> tuple[int, ...]:
    r = (p - 6 * s - 3) // 2
    q = 2 * s - 1
    left = power_series_mod(A_POLY, r, 2 * r, p)
    right = power_series_mod(D_POLY, q, 2 * q, p)
    return tuple(convolution_mod(left, right, p))


def coefficient_at(poly: list[int] | tuple[int, ...], degree: int) -> int:
    return poly[degree] if 0 <= degree < len(poly) else 0


def product_coefficient(
    left: list[int] | tuple[int, ...],
    right: list[int] | tuple[int, ...],
    degree: int,
    modulus: int,
) -> int:
    if degree < 0:
        return 0
    lower = max(0, degree - len(right) + 1)
    upper = min(len(left) - 1, degree)
    return sum(left[k] * right[degree - k] for k in range(lower, upper + 1)) % modulus


def substituted_product_coefficient(
    section: list[int], ordinary: list[int] | tuple[int, ...], degree: int, p: int
) -> int:
    return sum(
        value * coefficient_at(ordinary, degree - block * p)
        for block, value in enumerate(section)
        if 0 <= degree - block * p < len(ordinary)
    ) % p


def defect_coordinates(p: int, j: int, s: int, n: int) -> dict[int, int]:
    """Five coefficients of E_(p,j) P_s via the divided defect formula."""
    a, c = 3 * j + 1, 2 * j + 1
    moving = moving_polynomial(p, s)
    delta_a = frobenius_delta(tuple(A_POLY), p)
    delta_d = frobenius_delta(tuple(D_POLY), p)
    delta_a_times_p = convolution_mod(list(delta_a), list(moving), p)
    delta_d_times_p = convolution_mod(list(delta_d), list(moving), p)
    # A(v^p)^(a-1)D(v^p)^(-c) and A(v^p)^aD(v^p)^(-c-1)
    # are obtained from these short y-series after y=v^p.
    section_limit = c
    first_section = ratio_series_mod(a - 1, c, section_limit, p)
    second_section = ratio_series_mod(a, c + 1, section_limit, p)
    answer = {}
    for offset in range(-3, 2):
        degree = n + offset
        first = substituted_product_coefficient(
            first_section, delta_a_times_p, degree, p
        )
        second = substituted_product_coefficient(
            second_section, delta_d_times_p, degree, p
        )
        answer[offset] = (a * first - c * second) % p
    return answer


def main_term_coefficient(p: int, j: int, s: int, degree: int) -> int:
    """Coefficient of F_j(v^p)P_s(v), reduced modulo p."""
    a, c = 3 * j + 1, 2 * j + 1
    section = ratio_series_mod(a, c, degree // p, p)
    moving = moving_polynomial(p, s)
    return substituted_product_coefficient(section, moving, degree, p)


def recurrence_residue(m: int, coefficient: list[int], degree: int, modulus: int) -> int:
    def at(index: int) -> int:
        return coefficient[index] if index >= 0 else 0

    return (
        -2 * (degree + 1) * at(degree + 1)
        - (20 * m - 8 - 10 * degree) * at(degree)
        - 2 * (10 * degree + 10 - 20 * m) * at(degree - 1)
        - 4 * (10 * m - 5 * degree - 6) * at(degree - 2)
        - 8 * (degree + 1 - 4 * m) * at(degree - 3)
    ) % modulus


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m-max", type=int, default=160)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.m_max < 1:
        raise ValueError("m maximum must be positive")

    primes = primes_upto(6 * args.m_max)
    rows: list[tuple[int, ...]] = []
    counts = {
        "rows": 0,
        "five_coordinate_checks": 0,
        "gauge_recurrence_checks": 0,
        "gauge_target_checks": 0,
        "e0_zero": 0,
        "line_membership": 0,
        "common_log_zero": 0,
    }
    checked_primes: set[int] = set()

    for m in range(1, args.m_max + 1):
        g = scalar_coefficients(m)
        p_at_m = [p for p in primes if p <= 6 * m]
        for p in forced_primes(m, p_at_m):
            j, s, r = row_parameters(m, p)
            if not (j >= 1 and 3 * j + 1 < p):
                continue
            n = 4 * m
            a, c, q = 3 * j + 1, 2 * j + 1, 2 * s - 1
            moving_degree = 2 * r + 2 * q
            if not (
                6 * m == a * p + r
                and 4 * m + 2 == c * p - q
                and moving_degree == p - 2 * s - 5
                and n + 1 < p * p
            ):
                raise AssertionError((m, p, j, s, "row identities"))

            defect = defect_coordinates(p, j, s, n)
            for offset in range(-3, 2):
                degree = n + offset
                residue = degree % p
                if not (moving_degree < residue < p):
                    raise AssertionError((m, p, offset, moving_degree, residue))
                if main_term_coefficient(p, j, s, degree):
                    raise AssertionError((m, p, offset, "support gap"))
                if g[degree] % p:
                    raise AssertionError((m, p, offset, "actual support gap"))
                if (g[degree] // p) % p != defect[offset]:
                    raise AssertionError((m, p, offset, "defect coordinate"))
                counts["five_coordinate_checks"] += 1

            q0 = (defect[0] - 2 * defect[-1] + 2 * defect[-2]) % p
            q1 = defect[1]
            line = (
                defect[0] == 0
                and defect[-1] == 2 * defect[-3] % p
                and defect[-2] == 2 * defect[-3] % p
            )
            common = q0 == 0 and q1 == 0
            if line != common:
                raise AssertionError((m, p, j, s, defect, q0, q1, "line equivalence"))
            counts["e0_zero"] += defect[0] == 0
            counts["line_membership"] += line
            counts["common_log_zero"] += common

            # A nontrivial Frobenius gauge K=1+p*v^p preserves every
            # recurrence row modulo p^2.  The support gap makes it invisible
            # on all five normalized target coordinates.
            modulus = p * p
            gauged = []
            for degree, value in enumerate(g):
                shifted = g[degree - p] if degree >= p else 0
                gauged.append((value + p * shifted) % modulus)
            if gauged[0] != 1:
                raise AssertionError((m, p, "gauge constant"))
            for degree in range(n + 1):
                if recurrence_residue(m, gauged, degree, modulus):
                    raise AssertionError((m, p, degree, "gauged recurrence"))
                counts["gauge_recurrence_checks"] += 1
            for offset in range(-3, 2):
                degree = n + offset
                if gauged[degree] != g[degree] % modulus:
                    raise AssertionError((m, p, offset, "gauge target invariance"))
                counts["gauge_target_checks"] += 1

            rows.append(
                (
                    m,
                    p,
                    j,
                    s,
                    defect[-3],
                    defect[-2],
                    defect[-1],
                    defect[0],
                    defect[1],
                    q0,
                    q1,
                    int(line),
                )
            )
            counts["rows"] += 1
            checked_primes.add(p)

    degree_checks = []
    for p in sorted(checked_primes):
        delta_a = frobenius_delta(tuple(A_POLY), p)
        delta_d = frobenius_delta(tuple(D_POLY), p)
        if delta_a[2 * p - 1] != -3 % p:
            raise AssertionError((p, "Delta A top-minus-one"))
        if delta_d[2 * p - 1] != -2 % p:
            raise AssertionError((p, "Delta D top-minus-one"))
        tau_previous, tau = 2, 2
        for degree in range(1, p):
            if degree == 1:
                tau_degree = tau
            else:
                tau_previous, tau = tau, (2 * tau - 2 * tau_previous) % p
                tau_degree = tau
            predicted_a = (-(1 + pow(2, degree, p)) * pow(degree, -1, p)) % p
            predicted_d = (-tau_degree * pow(degree, -1, p)) % p
            if delta_a[degree] != predicted_a or delta_d[degree] != predicted_d:
                raise AssertionError((p, degree, "truncated logarithm"))
        degree_checks.append((p, 2 * p - 1))

    output = {
        "schema": "item203-common-log-global-v1",
        "status": {
            "actual_target_support_gap": "PROVED_IN_REPORT",
            "five_coordinate_frobenius_defect": "PROVED_IN_REPORT",
            "cancellation_aware_global_transfer_uniqueness": "PROVED_IN_REPORT",
            "common_log_local_line_equivalence": "PROVED_IN_REPORT",
            "direct_defect_kernel_degree_growth": "PROVED_IN_REPORT",
            "common_log_exclusion_or_sublinear_mass": "OPEN",
            "A1_digit": "SEPARATE_NOT_USED",
            "finite_nonoccurrence": "EXACT_FINITE_ONLY",
        },
        "definitions": {
            "A": "(1-v)(1-2v)=1-3v+2v^2",
            "D": "1-2v+2v^2",
            "F_pj": "A(v)^(3j+1)/D(v)^(2j+1)",
            "P_ps": "A(v)^((p-6s-3)/2)*D(v)^(2s-1)",
            "E_pj": "(F_pj(v)^p-F_pj(v^p))/p",
            "five_coordinates": "e_d=[v^(4m+d)]E_pj(v)P_ps(v), d=-3,-2,-1,0,1",
            "undivided_actual_state_mod_p": "(g_4m,g_(4m-1),g_(4m-2),g_(4m-3))=(0,0,0,0)",
            "common_log_three_equations": "e_0=0, e_-1=2e_-3, e_-2=2e_-3 (mod p)",
            "divided_line_parameter": "e_-3 is arbitrary; the support-gap lambda=0 statement concerns the undivided state modulo p",
            "global_gauge": "all same-g0 solutions through degree <p^2 differ by multiplication by 1+pH(v^p), H(0)=0",
        },
        "exact_identities": {
            "factorization": "G_m(v)=F_pj(v)^p P_ps(v)",
            "moving_degree": "deg(P_ps)=p-2s-5",
            "support_gap_residues": "p-2s-4,...,p-2s are strictly above deg(P_ps)",
            "defect_mod_p": "E_pj = a*A(v^p)^(a-1)*D(v^p)^(-c)*Delta_p(A)-c*A(v^p)^a*D(v^p)^(-c-1)*Delta_p(D)",
            "Delta_p": "(R(v)^p-R(v^p))/p",
            "truncated_A_kernel": "[v^k]Delta_p(A)=-(1+2^k)/k for 1<=k<p (mod p)",
            "truncated_D_kernel": "[v^k]Delta_p(D)=-tau_k/k, tau_0=tau_1=2, tau_k=2tau_(k-1)-2tau_(k-2)",
            "degree_witnesses": "[v^(2p-1)]Delta_p(A)=-3 and [v^(2p-1)]Delta_p(D)=-2 (mod p)",
        },
        "pinned_dependencies": PINNED_DEPENDENCIES,
        "finite_replay": {
            "m_max": args.m_max,
            **counts,
            "distinct_primes": len(checked_primes),
            "minimum_prime": min(checked_primes) if checked_primes else None,
            "maximum_prime": max(checked_primes) if checked_primes else None,
            "delta_degree_checks": degree_checks,
            "row_digest": row_digest(rows),
            "warning": "all row counts and nonoccurrence statements are exact finite diagnostics only",
        },
        "scope": {
            "what_is_removed": "the apparent factorial/nonunit-division ambiguity in the full recurrence transfer",
            "what_remains": "membership of an explicit five-coordinate Frobenius defect in a fixed local line",
            "bounded_degree_claim": "none; the displayed direct kernels have degree at least 2p-1",
            "alternative_representation": "not ruled out",
            "mass_or_density_claim": "none",
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
                "rows": counts["rows"],
                "common_log_zero": counts["common_log_zero"],
                "row_digest": output["finite_replay"]["row_digest"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
