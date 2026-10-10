#!/usr/bin/env python3
"""Deterministic certificate for the actual-lcm/Kummer barrier.

The companion source proves the all-parameter results.  This replay checks
the exact adjacent-Euler valuation identities, block-lcm sandwiches, actual
lcm clearing of the optimal beta filter, declared square-root blocks, the
Kummer-visible/excess split, and the exact common-content ledger.  Finite
checks are diagnostics and are not used as a classification theorem.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import mpmath as mp
from flint import fmpz


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_beta_actual_lcm_kummer_certificate.json"
RSS_LIMIT_KIB = 2 * 1024 * 1024
VALUATION_N_MAX = 24
VALUATION_P_MAX = 101
FILTER_H_MAX = 14
N0_H_MAX = 500
SQUARE_ROOT_N_VALUES = [50, 100, 200, 500]
VISIBLE_BLOCKS = [(2, 2), (4, 3), (7, 3), (10, 3)]
CONTENT_BLOCKS = [(2, 3), (5, 4), (9, 3)]


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def sha256_lines(lines: list[str]) -> str:
    return hashlib.sha256("".join(lines).encode()).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lcm(left: int, right: int) -> int:
    assert left > 0 and right > 0
    return left // math.gcd(left, right) * right


def lcm_range(limit: int) -> int:
    value = 1
    for integer in range(1, limit + 1):
        value = lcm(value, integer)
    return value


def valuation(value: int, prime: int) -> int:
    assert value > 0 and prime >= 2
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def prime_list(limit: int) -> list[int]:
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return primes


@lru_cache(maxsize=None)
def U(index: int) -> int:
    assert index >= 1
    return abs(int(fmpz.euler_number(2 * index)))


def A(index: int) -> int:
    assert index >= 1
    return (2 * index + 1) * (2 * index + 2)


@lru_cache(maxsize=None)
def reduced_pair(index: int) -> tuple[int, int]:
    numerator = U(index + 1)
    denominator = A(index) * U(index)
    divisor = math.gcd(numerator, denominator)
    pair = numerator // divisor, denominator // divisor
    assert math.gcd(*pair) == 1
    return pair


def ratio(index: int) -> Fraction:
    numerator, denominator = reduced_pair(index)
    return Fraction(numerator, denominator)


@lru_cache(maxsize=None)
def B(index: int) -> int:
    return U(index) // math.gcd(U(index), U(index + 1))


def block_lcm(values: list[int]) -> int:
    result = 1
    for value in values:
        result = lcm(result, value)
    return result


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_coefficient in enumerate(left):
        for j, right_coefficient in enumerate(right):
            result[i + j] += left_coefficient * right_coefficient
    return result


def filter_polynomial(height: int) -> list[int]:
    assert height >= 2
    coefficients = [-1, 1]
    for j in range(1, height - 1):
        odd = 2 * j + 1
        coefficients = polynomial_multiply(coefficients, [-1, odd * odd])
    assert len(coefficients) == height
    return coefficients


def filter_response(index: int, height: int) -> Fraction:
    coefficients = filter_polynomial(height)
    return sum(
        (Fraction(coefficient) * ratio(index + offset)
         for offset, coefficient in enumerate(coefficients)),
        Fraction(0),
    )


def N0(height: int) -> int:
    q = 2 * height - 1
    bracket = (
        3 * math.log(q)
        + (height - 2) * math.log(5 * math.e / 2)
        + math.log(9 / 8)
    )
    return 1 + math.ceil((q + 2) * bracket / 4)


def factor_map(value: int) -> dict[int, int]:
    assert value >= 1
    return {int(prime): int(exponent) for prime, exponent in fmpz(value).factor()}


def kappa(prime: int, endpoint: int) -> int:
    assert prime % 2 == 1
    exponent = 0
    totient = prime - 1
    while totient <= 2 * endpoint:
        exponent += 1
        totient *= prime
    return exponent


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def main() -> None:
    started = time.perf_counter()
    mp.mp.dps = 220
    alpha = mp.mpf(4) / (mp.pi * mp.pi)

    dependency_hashes = {
        "higher_determinant_manifest_sha256": (
            "abf5aae37871defe5a5fb0237506b0830fca17d94a6dd914bdf3994b086cf5c9"
        ),
        "Kummer_manifest_sha256": (
            "74b79cee3b86e5fe37700e1db68ed91976a56c01a783c1e10d5e13651d82ba49"
        ),
    }
    assert sha256_file(
        ROOT / "results" / "root_unity_beta_higher_determinant_hashes.sha256"
    ) == dependency_hashes["higher_determinant_manifest_sha256"]
    assert sha256_file(
        ROOT / "results" / "root_unity_quadratic_euler_gcd_kummer_hashes.sha256"
    ) == dependency_hashes["Kummer_manifest_sha256"]

    primes = prime_list(VALUATION_P_MAX)
    valuation_lines: list[str] = []
    for index in range(1, VALUATION_N_MAX + 1):
        numerator, denominator = reduced_pair(index)
        b_value = B(index)
        assert b_value & 1
        assert denominator == A(index) * U(index) // math.gcd(
            A(index) * U(index), U(index + 1)
        )
        assert b_value == U(index) // math.gcd(U(index), U(index + 1))
        assert denominator % b_value == 0
        assert A(index) * b_value % denominator == 0
        for prime in primes:
            e_now = valuation(U(index), prime)
            e_next = valuation(U(index + 1), prime)
            a_now = valuation(A(index), prime)
            q_now = valuation(denominator, prime)
            b_now = valuation(b_value, prime)
            assert q_now == max(0, a_now + e_now - e_next)
            assert b_now == max(0, e_now - e_next)
            valuation_lines.append(
                f"{index}:{prime}:{e_now}:{e_next}:{a_now}:{q_now}:{b_now}\n"
            )
        assert Fraction(numerator, denominator) == Fraction(
            U(index + 1), A(index) * U(index)
        )

    sandwich_rows: list[dict[str, int | str]] = []
    for index, height in [(1, 2), (2, 3), (5, 4), (10, 5), (18, 6)]:
        q_lcm = block_lcm(
            [reduced_pair(n)[1] for n in range(index, index + height)]
        )
        b_lcm = block_lcm([B(n) for n in range(index, index + height)])
        a_lcm = block_lcm([A(n) for n in range(index, index + height)])
        assert q_lcm % b_lcm == 0
        assert a_lcm * b_lcm % q_lcm == 0
        endpoint = index + height
        lambda_2m = lcm_range(2 * endpoint)
        product_a = math.prod(A(n) for n in range(index, index + height))
        assert lambda_2m**2 % a_lcm == 0
        assert product_a % a_lcm == 0
        sandwich_rows.append(
            {
                "N": index,
                "h": height,
                "Q_lcm_digits": len(str(q_lcm)),
                "B_lcm_digits": len(str(b_lcm)),
                "A_lcm": str(a_lcm),
            }
        )

    n0_rows: list[dict[str, int]] = []
    for height in range(2, N0_H_MAX + 1):
        threshold = N0(height)
        assert threshold <= 2 * height * height + 2
        if height <= FILTER_H_MAX:
            n0_rows.append(
                {
                    "h": height,
                    "N0": threshold,
                    "uniform_upper": 2 * height * height + 2,
                }
            )

    filter_rows: list[dict[str, int | str]] = []
    filter_digest_lines: list[str] = []
    for height in range(2, FILTER_H_MAX + 1):
        index = N0(height)
        q = 2 * height - 1
        response = filter_response(index, height)
        assert response
        q_lcm = block_lcm(
            [reduced_pair(n)[1] for n in range(index, index + height)]
        )
        cleared = response * q_lcm
        assert cleared.denominator == 1
        bound = (
            alpha
            * mp.power(q, -2 * index)
            * (mp.mpf(1) / q + mp.mpf(1) / (2 * index))
        )
        absolute_response = abs(mp_fraction(response))
        assert absolute_response <= bound
        lower = mp.power(q, 2 * index) / (
            alpha * (mp.mpf(1) / q + mp.mpf(1) / (2 * index))
        )
        assert mp.mpf(q_lcm) >= lower
        assert q * q <= 3**height
        if height == 2:
            assert q * q == 3**height
        else:
            assert q * q < 3**height
        filter_digest_lines.append(
            f"{height}:{index}:{response.numerator}/{response.denominator}:"
            f"{cleared.numerator}\n"
        )
        filter_rows.append(
            {
                "h": height,
                "N": index,
                "cleared_integer_sign": 1 if cleared > 0 else -1,
                "lcm_log": mp.nstr(mp.log(q_lcm), 30),
                "theorem_lower_log": mp.nstr(mp.log(lower), 30),
            }
        )

    square_root_rows: list[dict[str, int | str]] = []
    for index in SQUARE_ROOT_N_VALUES:
        height = math.isqrt((index - 2) // 2)
        # isqrt(floor(x)) equals floor(sqrt(x)); keep the defining identity explicit.
        assert height == math.floor(math.sqrt((index - 2) / 2))
        assert height >= 2
        assert N0(height) <= 2 * height * height + 2 <= index
        response = filter_response(index, height)
        assert response
        q_lcm = block_lcm(
            [reduced_pair(n)[1] for n in range(index, index + height)]
        )
        cleared = q_lcm * response
        assert cleared.denominator == 1 and cleared
        q = 2 * height - 1
        response_bound = (
            alpha
            * mp.power(q, -2 * index)
            * (mp.mpf(1) / q + mp.mpf(1) / (2 * index))
        )
        assert abs(mp_fraction(response)) <= response_bound
        lower = 1 / response_bound
        assert mp.mpf(q_lcm) >= lower
        square_root_rows.append(
            {
                "N": index,
                "h_N": height,
                "N0_h": N0(height),
                "log_Q_lcm": mp.nstr(mp.log(q_lcm), 35),
                "theorem_lower_log": mp.nstr(mp.log(lower), 35),
                "normalized_log_Q": mp.nstr(
                    mp.log(q_lcm) / (index * mp.log(index)), 25
                ),
                "cleared_integer_digits": len(str(abs(cleared.numerator))),
            }
        )

    visible_rows: list[dict[str, object]] = []
    visible_digest_lines: list[str] = []
    for index, height in VISIBLE_BLOCKS:
        endpoint = index + height
        b_lcm = block_lcm([B(n) for n in range(index, endpoint)])
        factors = factor_map(b_lcm)
        visible = 1
        excess = 1
        factor_rows: list[dict[str, int]] = []
        for prime, exponent in sorted(factors.items()):
            assert prime % 2 == 1
            boundary = kappa(prime, endpoint)
            visible_exponent = min(exponent, boundary)
            excess_exponent = exponent - visible_exponent
            visible *= prime**visible_exponent
            excess *= prime**excess_exponent
            if visible_exponent:
                assert prime**visible_exponent <= 3 * endpoint
            if excess_exponent:
                assert math.prod(
                    [prime - 1] + [prime] * (exponent - 1)
                ) > 2 * endpoint
                drops = [
                    valuation(U(n), prime) - valuation(U(n + 1), prime)
                    for n in range(index, endpoint)
                ]
                assert max(drops) == exponent
                witness_offset = drops.index(exponent)
                witness_index = index + witness_offset
                next_valuation = valuation(U(witness_index + 1), prime)
                for layer in range(boundary + 1, exponent + 1):
                    threshold = next_valuation + layer
                    totient = (prime - 1) * prime ** (threshold - 1)
                    assert totient > 2 * endpoint
                    assert valuation(U(witness_index), prime) >= threshold
                    assert valuation(U(witness_index + 1), prime) < threshold
                    assert totient // 2 > endpoint
            else:
                witness_index = -1
            factor_rows.append(
                {
                    "p": prime,
                    "b_p": exponent,
                    "kappa_p": boundary,
                    "visible_exponent": visible_exponent,
                    "excess_exponent": excess_exponent,
                    "first_period_witness_n": witness_index,
                }
            )
            visible_digest_lines.append(
                f"{index}:{height}:{prime}:{exponent}:{boundary}\n"
            )
        assert visible * excess == b_lcm
        assert lcm_range(3 * endpoint) % visible == 0
        visible_rows.append(
            {
                "N": index,
                "h": height,
                "M": endpoint,
                "B_lcm": str(b_lcm),
                "visible": str(visible),
                "first_period_excess": str(excess),
                "factors": factor_rows,
            }
        )

    content_rows: list[dict[str, object]] = []
    content_digest_lines: list[str] = []
    for index, height in CONTENT_BLOCKS:
        denominators = [
            reduced_pair(n)[1] for n in range(index, index + height)
        ]
        product = math.prod(denominators)
        denominator_lcm = block_lcm(denominators)
        content = product // denominator_lcm
        all_primes: set[int] = set()
        denominator_factors: list[dict[int, int]] = []
        for denominator in denominators:
            factors = factor_map(denominator)
            denominator_factors.append(factors)
            all_primes.update(factors)
        content_factors = factor_map(content)
        for prime in sorted(all_primes):
            exponents = [factors.get(prime, 0) for factors in denominator_factors]
            predicted = sum(exponents) - max(exponents)
            assert content_factors.get(prime, 0) == predicted
            content_digest_lines.append(
                f"{index}:{height}:{prime}:{','.join(map(str, exponents))}:"
                f"{predicted}\n"
            )
        assert denominator_lcm <= product
        assert product <= max(denominators) ** height
        content_rows.append(
            {
                "N": index,
                "h": height,
                "product_digits": len(str(product)),
                "lcm_digits": len(str(denominator_lcm)),
                "content": str(content),
            }
        )

    elapsed = time.perf_counter() - started
    rss = peak_rss_kib()
    assert rss < RSS_LIMIT_KIB
    result = {
        "theorem": (
            "The actual lcm of a certified square-root block of reduced beta "
            "denominators satisfies log lcm >= N log N - O(N).  Removing the "
            "elementary index factors preserves this scale, while the Kummer-"
            "visible part is only exp(O(N)); the remaining N log N mass lies "
            "in first-period adjacent Euler valuation drops."
        ),
        "obstruction": (
            "Canonical Kummer periodicity has period longer than the entire "
            "block on every excess layer, so it supplies no repetition or "
            "concentration theorem.  The block lcm alone yields only a "
            "sqrt(N) log(N) individual floor; an N log N individual result "
            "requires new first-period concentration or overlap arithmetic."
        ),
        "logical_scope": (
            "Finite exact replay for a proved block-lcm theorem and a canonical "
            "Kummer-period obstruction.  It does not prove an individual "
            "N log N denominator bound, control all first-period irregular "
            "layers, or classify e+pi."
        ),
        "declared_grids": {
            "valuation_n_max": VALUATION_N_MAX,
            "valuation_p_max": VALUATION_P_MAX,
            "filter_h_max": FILTER_H_MAX,
            "N0_h_max": N0_H_MAX,
            "square_root_N_values": SQUARE_ROOT_N_VALUES,
            "visible_blocks": [list(row) for row in VISIBLE_BLOCKS],
            "content_blocks": [list(row) for row in CONTENT_BLOCKS],
        },
        "exact_valuation_rows_sha256": sha256_lines(valuation_lines),
        "lcm_sandwich_rows": sandwich_rows,
        "N0_rows": n0_rows,
        "filter": {
            "rows_sha256": sha256_lines(filter_digest_lines),
            "rows": filter_rows,
        },
        "square_root_blocks": square_root_rows,
        "Kummer_split": {
            "rows_sha256": sha256_lines(visible_digest_lines),
            "rows": visible_rows,
        },
        "common_content": {
            "rows_sha256": sha256_lines(content_digest_lines),
            "rows": content_rows,
        },
        "dependencies": dependency_hashes,
        "replay_metadata": (
            "Elapsed time and peak RSS are emitted to stdout, not embedded, "
            "so the JSON is byte-stable across exact replays."
        ),
        "rss_limit_kib": RSS_LIMIT_KIB,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"elapsed_seconds={elapsed:.6f} peak_rss_kib={rss}")


if __name__ == "__main__":
    main()
