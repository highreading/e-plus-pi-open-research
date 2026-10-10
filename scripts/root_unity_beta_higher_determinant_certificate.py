#!/usr/bin/env python3
"""Deterministic certificate for the higher-beta-determinant barrier.

The companion source contains the all-parameter proofs.  This script
reconstructs the exact Dirichlet coefficients, filters, rational
determinants, clearing profiles, and selected asymptotic normalizations on
a declared finite grid.  The finite grid is not used as a classification.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from pathlib import Path

import mpmath as mp
from flint import fmpz


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "results"
    / "root_unity_beta_higher_determinant_certificate.json"
)
RSS_LIMIT_KIB = 2 * 1024 * 1024
COEFFICIENT_Q_MAX = 199
DIRICHLET_CUTOFF = 1001
FILTER_H_MAX = 10
VANDERMONDE_H_MAX = 7
HANKEL_H_MAX = 5
SIMULTANEOUS_H_MAX = 5


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def chi4(n: int) -> int:
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def odd_factorization(n: int) -> list[tuple[int, int]]:
    assert n >= 1 and n % 2 == 1
    factors: list[tuple[int, int]] = []
    p = 3
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                n //= p
                exponent += 1
            factors.append((p, exponent))
        p += 2
    if n > 1:
        factors.append((n, 1))
    return factors


def dirichlet_c(q: int) -> Fraction:
    assert q >= 1 and q % 2 == 1
    value = Fraction(1)
    for p, exponent in odd_factorization(q):
        value *= Fraction(
            -(chi4(p) ** exponent) * (p * p - 1),
            p ** (2 * exponent),
        )
    return value


def mode_b(q: int) -> Fraction:
    return dirichlet_c(q) / q


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def filter_polynomial(h: int) -> list[int]:
    assert h >= 2
    coefficients = [-1, 1]
    for j in range(1, h - 1):
        odd = 2 * j + 1
        coefficients = polynomial_multiply(coefficients, [-1, odd * odd])
    return coefficients


def evaluate_polynomial(coefficients: list[int], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


@lru_cache(maxsize=None)
def reduced_pair(N: int) -> tuple[int, int]:
    assert N >= 1
    low = abs(fmpz.euler_number(2 * N))
    high = abs(fmpz.euler_number(2 * N + 2))
    raw_denominator = (2 * N + 2) * (2 * N + 1) * low
    gcd_value = fmpz.gcd(raw_denominator, high)
    P = int(high // gcd_value)
    Q = int(raw_denominator // gcd_value)
    assert math.gcd(P, Q) == 1
    return P, Q


def ratio(N: int) -> Fraction:
    P, Q = reduced_pair(N)
    return Fraction(P, Q)


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    assert size >= 1 and all(len(row) == size for row in matrix)
    work = [row[:] for row in matrix]
    value = Fraction(1)
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work[column], work[pivot_row] = (
                work[pivot_row],
                work[column],
            )
            value = -value
        pivot = work[column][column]
        value *= pivot
        for j in range(column, size):
            work[column][j] /= pivot
        for row in range(column + 1, size):
            multiplier = work[row][column]
            for j in range(column, size):
                work[row][j] -= multiplier * work[column][j]
    return value


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def hankel_exponents(h: int) -> list[int]:
    return [
        min(t + 1, 2 * h - 1 - t, h)
        for t in range(2 * h - 1)
    ]


def simultaneous_exponents(h: int) -> list[int]:
    return [
        min(t + 1, h - 1, 2 * h - 2 - t)
        for t in range(2 * h - 2)
    ]


def simultaneous_ratio(n: int, a: int) -> Fraction:
    value = Fraction(1)
    for offset in range(a):
        value *= ratio(n + offset)
    return value


def main() -> None:
    started = time.perf_counter()
    mp.mp.dps = 180
    alpha = mp.mpf(4) / (mp.pi * mp.pi)

    coefficient_lines: list[str] = []
    for q in range(1, COEFFICIENT_Q_MAX + 1, 2):
        coefficient = dirichlet_c(q)
        assert coefficient
        assert abs(coefficient) <= 1
        explicit = Fraction(1)
        for p, exponent in odd_factorization(q):
            explicit *= Fraction(
                -(chi4(p) ** exponent) * (p * p - 1),
                p ** (2 * exponent),
            )
        assert coefficient == explicit
        coefficient_lines.append(
            f"{q}:{coefficient.numerator}/{coefficient.denominator}\n"
        )
    assert mode_b(3) == Fraction(8, 27)
    assert mode_b(5) == Fraction(-24, 125)

    dirichlet_rows: list[dict] = []
    for N in [1, 2, 5, 10]:
        partial = mp.mpf(0)
        for q in range(1, DIRICHLET_CUTOFF + 1, 2):
            coefficient = dirichlet_c(q)
            partial += (
                mp.mpf(coefficient.numerator)
                / coefficient.denominator
                / mp.power(q, 2 * N + 1)
            )
        exact = mp_fraction(ratio(N)) / alpha
        error = abs(exact - partial)
        tail_bound = mp.power(DIRICHLET_CUTOFF, -2 * N) / (2 * N)
        assert error < tail_bound
        dirichlet_rows.append(
            {
                "N": N,
                "absolute_error": mp.nstr(error, 40),
                "safe_tail_bound": mp.nstr(tail_bound, 40),
            }
        )

    filter_rows: list[dict] = []
    filter_digest_lines: list[str] = []
    for h in range(2, FILTER_H_MAX + 1):
        coefficients = filter_polynomial(h)
        assert len(coefficients) == h
        assert abs(coefficients[0]) == 1
        assert math.gcd(*map(abs, coefficients)) == 1
        assert evaluate_polynomial(coefficients, Fraction(1)) == 0
        for j in range(1, h - 1):
            odd = 2 * j + 1
            assert (
                evaluate_polynomial(coefficients, Fraction(1, odd * odd))
                == 0
            )

        q_h = 2 * h - 1
        leading_response = evaluate_polynomial(
            coefficients, Fraction(1, q_h * q_h)
        )
        formula = (
            Fraction(q_h * q_h - 1, q_h * q_h)
            * Fraction(
                4 ** (h - 2)
                * math.factorial(h - 2)
                * math.factorial(2 * h - 2),
                math.factorial(h) * q_h ** (2 * h - 4),
            )
        )
        assert abs(leading_response) == formula

        B_h = math.prod((2 * j + 1) ** 2 for j in range(1, h - 1))
        l1_height = sum(abs(value) for value in coefficients)
        exact_l1 = 2 * math.prod(
            1 + (2 * j + 1) ** 2 for j in range(1, h - 1)
        )
        assert l1_height == exact_l1
        assert B_h <= max(map(abs, coefficients)) <= l1_height
        assert l1_height <= (2 ** (h - 1)) * B_h

        N0 = 1 + math.ceil(
            (q_h + 2)
            / 4
            * (
                3 * math.log(q_h)
                + (h - 2) * math.log(5 * math.e / 2)
                + math.log(9 / 8)
            )
        )
        response = sum(
            Fraction(coefficients[offset]) * ratio(N0 + offset)
            for offset in range(h)
        )
        leading_sign = mode_b(q_h) * leading_response
        assert response
        assert (response > 0) == (leading_sign > 0)
        denominator_product = math.prod(
            reduced_pair(N0 + offset)[1] for offset in range(h)
        )
        cleared = response * denominator_product
        assert cleared.denominator == 1

        lower_leading = (
            mp.mpf(8)
            / 9
            * mp.power(2 / (5 * mp.e), h - 2)
            / mp.power(q_h, 3)
            * mp.power(q_h, -2 * N0)
        )
        tail_bound = mp.power(q_h + 2, -2 * N0)
        assert lower_leading > tail_bound

        response_bound = (
            alpha
            * mp.power(q_h, -2 * N0)
            * (mp.mpf(1) / q_h + mp.mpf(1) / (2 * N0))
        )
        assert abs(mp_fraction(response)) <= response_bound

        assert (2 * h - 1) ** 2 <= 3**h
        if h == 2:
            assert (2 * h - 1) ** 2 == 3**h
        else:
            assert (2 * h - 1) ** 2 < 3**h

        filter_digest_lines.append(
            f"{h}:{','.join(map(str, coefficients))}:{N0}:"
            f"{response.numerator}/{response.denominator}\n"
        )
        filter_rows.append(
            {
                "h": h,
                "q_h": q_h,
                "certified_N0": N0,
                "coefficient_height_digits": len(
                    str(max(map(abs, coefficients)))
                ),
                "coefficient_l1_digits": len(str(l1_height)),
                "response_sign_at_N0": 1 if response > 0 else -1,
                "cleared_integer_digits": len(str(abs(cleared.numerator))),
            }
        )

    C_tail = mp.mpf(432) / (13 * mp.pi * mp.pi)
    vandermonde_digest_lines: list[str] = []
    vandermonde_rows: list[dict] = []
    for h in range(2, VANDERMONDE_H_MAX + 1):
        for N in range(1, 9):
            values = [ratio(N + i) for i in range(h)]
            assert all(values[i] > values[i + 1] for i in range(h - 1))
            V = Fraction(1)
            integer_numerator = 1
            denominator_product = 1
            for i in range(h):
                P_i, Q_i = reduced_pair(N + i)
                denominator_product *= Q_i ** (h - 1)
                for j in range(i + 1, h):
                    P_j, Q_j = reduced_pair(N + j)
                    cross = P_i * Q_j - P_j * Q_i
                    assert cross > 0
                    integer_numerator *= cross
                    V *= values[i] - values[j]
            assert V == Fraction(integer_numerator, denominator_product)
            assert V > 0

            K = h * (h - 1) // 2
            S = h * (h - 1) * (h - 2) // 6
            analytic_upper = (
                mp.power(C_tail, K)
                * mp.power(3, -2 * (N * K + S) - 3 * K)
            )
            assert mp_fraction(V) < analytic_upper
            exact_log_sum = sum(
                mp.log(reduced_pair(N + i)[1]) for i in range(h)
            )
            floor = (
                h * (N + mp.mpf(h - 2) / 3 + mp.mpf(3) / 2)
                * mp.log(3)
                - mp.mpf(h) / 2 * mp.log(C_tail)
            )
            assert exact_log_sum > floor
            vandermonde_digest_lines.append(
                f"{h}:{N}:{V.numerator}/{V.denominator}\n"
            )
        N_asymptotic = 20
        values = [ratio(N_asymptotic + i) for i in range(h)]
        V = Fraction(1)
        for i in range(h):
            for j in range(i + 1, h):
                V *= values[i] - values[j]
        K = h * (h - 1) // 2
        S = h * (h - 1) * (h - 2) // 6
        c = mp.mpf(32) / (27 * mp.pi * mp.pi)
        predicted_log = (
            K * mp.log(c)
            - (N_asymptotic * K + S) * mp.log(9)
            + sum(
                (h - d) * mp.log(1 - mp.power(9, -d))
                for d in range(1, h)
            )
        )
        residual = mp.log(mp_fraction(V)) - predicted_log
        vandermonde_rows.append(
            {
                "h": h,
                "N": N_asymptotic,
                "log_asymptotic_residual": mp.nstr(residual, 40),
            }
        )

    profile_rows: list[dict] = []
    for h in range(2, 8):
        hankel_profile = hankel_exponents(h)
        assert sum(hankel_profile) == h * h
        for t, expected in enumerate(hankel_profile):
            maximum = max(
                sum(i + permutation[i] == t for i in range(h))
                for permutation in permutations(range(h))
            )
            assert maximum == expected

        simultaneous_profile = simultaneous_exponents(h)
        assert sum(simultaneous_profile) == h * (h - 1)
        for t, expected in enumerate(simultaneous_profile):
            maximum = max(
                sum(
                    i <= t < i + permutation[i]
                    for i in range(h)
                )
                for permutation in permutations(range(h))
            )
            assert maximum == expected
        profile_rows.append(
            {
                "h": h,
                "hankel": hankel_profile,
                "hankel_sum": sum(hankel_profile),
                "simultaneous": simultaneous_profile,
                "simultaneous_sum": sum(simultaneous_profile),
            }
        )

    hankel_digest_lines: list[str] = []
    hankel_rows: list[dict] = []
    exact_negative_minor = Fraction(
        -1238314183775556121,
        51629038152493172462784000,
    )
    for h in range(2, HANKEL_H_MAX + 1):
        for N in range(1, 13):
            H = determinant(
                [[ratio(N + i + j) for j in range(h)] for i in range(h)]
            )
            exponents = hankel_exponents(h)
            clearing = math.prod(
                reduced_pair(N + t)[1] ** exponents[t]
                for t in range(2 * h - 1)
            )
            assert (H * clearing).denominator == 1
            hankel_digest_lines.append(
                f"{h}:{N}:{H.numerator}/{H.denominator}\n"
            )
            if h == 3 and N == 1:
                assert H == exact_negative_minor

        N_asymptotic = 20
        H = determinant(
            [
                [ratio(N_asymptotic + i + j) for j in range(h)]
                for i in range(h)
            ]
        )
        q_nodes = list(range(1, 2 * h, 2))
        leading = alpha**h
        for q in q_nodes:
            leading *= mp_fraction(mode_b(q)) * mp.power(q, -2 * N_asymptotic)
        lambdas = [mp.mpf(1) / (q * q) for q in q_nodes]
        for i in range(h):
            for j in range(i + 1, h):
                leading *= (lambdas[j] - lambdas[i]) ** 2
        normalized = mp_fraction(H) / leading
        hankel_rows.append(
            {
                "h": h,
                "N": N_asymptotic,
                "determinant_sign": 1 if H > 0 else -1,
                "leading_normalized_ratio": mp.nstr(normalized, 40),
            }
        )

    simultaneous_digest_lines: list[str] = []
    simultaneous_rows: list[dict] = []
    for h in range(2, SIMULTANEOUS_H_MAX + 1):
        for N in range(2, 9):
            matrix: list[list[Fraction]] = []
            for i in range(h):
                row: list[Fraction] = []
                n = N + i
                for a in range(h):
                    telescoped = simultaneous_ratio(n, a)
                    factorial_ratio = math.prod(
                        range(2 * n + 1, 2 * n + 2 * a + 1)
                    )
                    if a == 0:
                        factorial_ratio = 1
                    raw = Fraction(
                        abs(int(fmpz.euler_number(2 * n + 2 * a))),
                        factorial_ratio
                        * abs(int(fmpz.euler_number(2 * n))),
                    )
                    assert telescoped == raw
                    row.append(telescoped)
                matrix.append(row)
            S_value = determinant(matrix)
            exponents = simultaneous_exponents(h)
            clearing = math.prod(
                reduced_pair(N + t)[1] ** exponents[t]
                for t in range(2 * h - 2)
            )
            assert (S_value * clearing).denominator == 1
            simultaneous_digest_lines.append(
                f"{h}:{N}:{S_value.numerator}/{S_value.denominator}\n"
            )

        N_asymptotic = 20
        S_value = determinant(
            [
                [
                    simultaneous_ratio(N_asymptotic + i, a)
                    for a in range(h)
                ]
                for i in range(h)
            ]
        )
        q_nodes = list(range(1, 2 * h, 2))
        leading = mp.power(alpha, h * (h - 1) // 2)
        for q in q_nodes:
            leading *= chi4(q) * mp.power(q, -(2 * N_asymptotic + 1))
        lambdas = [mp.mpf(1) / (q * q) for q in q_nodes]
        for i in range(h):
            for j in range(i + 1, h):
                leading *= (lambdas[j] - lambdas[i]) ** 2
        normalized = mp_fraction(S_value) / leading
        simultaneous_rows.append(
            {
                "h": h,
                "N": N_asymptotic,
                "determinant_sign": 1 if S_value > 0 else -1,
                "leading_normalized_ratio": mp.nstr(normalized, 40),
            }
        )

    payload = {
        "schema": "root_unity_beta_higher_determinant_certificate_v1",
        "logical_scope": (
            "Finite deterministic replay for an analytic canonical "
            "denominator-multiplicity barrier. It does not prove "
            "growing-Hankel nonvanishing, a large actual-lcm cancellation, "
            "log G_N=o(N log N), or any classification of e+pi."
        ),
        "declared_grids": {
            "coefficient_q_max": COEFFICIENT_Q_MAX,
            "dirichlet_cutoff": DIRICHLET_CUTOFF,
            "filter_h_max": FILTER_H_MAX,
            "vandermonde_h_max": VANDERMONDE_H_MAX,
            "hankel_h_max": HANKEL_H_MAX,
            "simultaneous_h_max": SIMULTANEOUS_H_MAX,
        },
        "dirichlet_modes": {
            "coefficient_rows_sha256": sha256_text(
                "".join(coefficient_lines)
            ),
            "b_3": "8/27",
            "b_5": "-24/125",
            "partial_sum_rows": dirichlet_rows,
        },
        "optimal_linear_filter": {
            "definition": (
                "A_h(X)=(X-1)*product_(j=1..h-2)"
                "((2j+1)^2*X-1)"
            ),
            "response_rows_sha256": sha256_text(
                "".join(filter_digest_lines)
            ),
            "rows": filter_rows,
            "per_denominator_rate": (
                "2*log(2h-1)/h <= log(3), equality only h=2"
            ),
            "certified_nonvanishing_range": (
                "N>=N0(h) from source equation (16c); N0(h)=O(h^2)"
            ),
        },
        "vandermonde": {
            "exact_rows_sha256": sha256_text(
                "".join(vandermonde_digest_lines)
            ),
            "asymptotic_rows": vandermonde_rows,
            "all_parameter_floor": (
                "sum_i log Q_(N+i) > "
                "h*(N+(h-2)/3+3/2)*log(3)-(h/2)*log(C)"
            ),
        },
        "clearing_profiles": profile_rows,
        "hankel": {
            "exact_rows_sha256": sha256_text(
                "".join(hankel_digest_lines)
            ),
            "asymptotic_rows": hankel_rows,
            "negative_3_by_3_minor_N_1": (
                f"{exact_negative_minor.numerator}/"
                f"{exact_negative_minor.denominator}"
            ),
            "ordinary_total_positivity": False,
        },
        "simultaneous_higher_ratios": {
            "exact_rows_sha256": sha256_text(
                "".join(simultaneous_digest_lines)
            ),
            "asymptotic_rows": simultaneous_rows,
            "telescoping": "R_(n,a)=product_(u=0..a-1) r_(n+u)",
        },
        "barrier": (
            "Canonical analytic decay divided by exact universal "
            "denominator multiplicity is at most linear in the relevant "
            "index. A systematic actual-lcm/common-content cancellation "
            "or a new growing-size nonvanishing mechanism is still open."
        ),
    }

    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_LIMIT_KIB
    OUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
