#!/usr/bin/env python3
"""Portable exact certificate for Item 266.

The bounded row replay is labelled EXACT FINITE ONLY.  No common-zero scan
is performed.  All theorem-level formulas are checked symbolically or by
exact integer/rational arithmetic, apart from a rigorously enclosed decimal
evaluation of the convergent raw-capacity series.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item266_far_offray_weighted_barrier_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item266_far_offray_weighted_barrier_certificate.json"
)


def rising(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value + offset
    return answer


def falling(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value - offset
    return answer


def stable_phi(b_value: int, residue: int, a_value: int) -> Fraction:
    """Item 212 stable rational Phi after s=-(b+4)/5.

    a=0 gives Phi_g1 and a=1 gives Phi_g0.
    """
    if b_value < 0 or residue not in range(4) or a_value not in (0, 1):
        raise ValueError((b_value, residue, a_value))
    B = b_value + 1 - a_value
    if residue > B:
        return Fraction(0)
    s_value = Fraction(-(b_value + 4), 5)
    E = 2 * s_value + a_value
    t_value = (3 * s_value + 2 - residue) / 4
    cutoff = (B - residue) // 4
    answer = Fraction(0)
    for h_value in range(cutoff + 1):
        denominator = rising(E - t_value + 1, h_value)
        if denominator == 0:
            raise AssertionError((b_value, residue, a_value, h_value))
        answer += (
            (-1) ** h_value
            * math.comb(B, residue + 4 * h_value)
            * falling(t_value, h_value)
            / denominator
        )
    return answer


def sieve(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, math.isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return [value for value, flag in enumerate(flags) if flag]


def terminal_state_mod(s_value: int, prime: int) -> tuple[int, int, int, int]:
    """Last four coefficients of Item 205's exact F_s recurrence."""
    k_value = 3 * s_value + 2
    coefficients = [0] * (k_value + 1)
    coefficients[0] = 1
    for n_value in range(k_value):
        def A(index: int) -> int:
            return coefficients[index] if index >= 0 else 0

        right = (
            (5 * s_value + 3) * (A(n_value) + A(n_value - 1) + A(n_value - 2))
            + (n_value - 3 * s_value) * A(n_value - 3)
        ) % prime
        denominator = n_value + 1
        if not (0 < denominator < prime):
            raise AssertionError((n_value, prime))
        coefficients[n_value + 1] = right * pow(denominator, -1, prime) % prime
    return tuple(coefficients[k_value - 3 : k_value + 1])  # type: ignore[return-value]


def actual_stable_rows(M: int, primes: list[int]) -> set[tuple[int, int, int, int, int]]:
    rows: set[tuple[int, int, int, int, int]] = set()
    for j_value in range(1, 2 * M + 1):
        upper = 6 * M // (3 * j_value + 2)
        for prime in primes:
            if prime > upper:
                break
            s_value = (j_value + 1) * prime - (2 * M + 1)
            if s_value < 0 or prime <= 3 * s_value + 2:
                continue
            q_value = 1 if prime >= 5 * s_value + 4 else 2
            b_value = q_value * prime - 5 * s_value - 4
            if b_value <= 3 * s_value + 4:
                rows.add((j_value, prime, q_value, s_value, b_value))
    return rows


def interval_stable_rows(M: int, primes: list[int]) -> set[tuple[int, int, int, int, int]]:
    rows: set[tuple[int, int, int, int, int]] = set()
    for j_value in range(1, 2 * M + 1):
        for prime in primes:
            if prime < 11:
                continue
            if prime > 6 * M // (3 * j_value + 2) + 2:
                break
            if (8 * j_value + 7) * prime >= 16 * M and (5 * j_value + 4) * prime <= 10 * M + 1:
                s_value = (j_value + 1) * prime - (2 * M + 1)
                b_value = 10 * M + 1 - (5 * j_value + 4) * prime
                rows.add((j_value, prime, 1, s_value, b_value))
            if (4 * j_value + 3) * prime >= 8 * M and (3 * j_value + 2) * prime <= 6 * M:
                s_value = (j_value + 1) * prime - (2 * M + 1)
                b_value = 10 * M + 1 - (5 * j_value + 3) * prime
                rows.add((j_value, prime, 2, s_value, b_value))
    return rows


def capacity_enclosure(cutoff: int = 1_000_000) -> tuple[str, str]:
    """Rigorous decimal enclosure from the integral test.

    f(x) is positive decreasing.  Hence S_N+int_(N+1)^inf f <= C <=
    S_N+int_N^inf f.  Decimal roundoff is covered by 1e-35.
    """
    with localcontext() as context:
        context.prec = 50
        total = Decimal(0)
        for j_value in range(1, cutoff + 1):
            j = Decimal(j_value)
            total += Decimal(6) / ((5 * j + 4) * (8 * j + 7))
            total += Decimal(2) / ((3 * j + 2) * (4 * j + 3))

        def tail_integral(N: int) -> Decimal:
            n = Decimal(N)
            first = Decimal(5) * (8 * n + 7) / (Decimal(8) * (5 * n + 4))
            second = Decimal(3) * (4 * n + 3) / (Decimal(4) * (3 * n + 2))
            return Decimal(2) * (first.ln() + second.ln())

        guard = Decimal("1e-35")
        lower = total + tail_integral(cutoff + 1) - guard
        upper = total + tail_integral(cutoff) + guard
        if not (lower < Decimal("0.2391110146981") < upper):
            raise AssertionError((lower, upper))
        return format(lower, "f"), format(upper, "f")


def certificate(max_M: int) -> dict[str, Any]:
    if max_M < 200:
        raise ValueError("canonical finite replay requires max_M >= 200")

    primes = sieve(2 * max_M + 20)
    row_hash = hashlib.sha256()
    row_count = 0
    small_prime_rows = 0
    for M in range(1, max_M + 1):
        actual = actual_stable_rows(M, primes)
        actual_large = {row for row in actual if row[1] >= 11}
        inverse = interval_stable_rows(M, primes)
        if actual_large != inverse:
            raise AssertionError((M, sorted(actual_large - inverse), sorted(inverse - actual_large)))
        small_prime_rows += len(actual - actual_large)
        for row in sorted(actual):
            j_value, prime, q_value, s_value, b_value = row
            if 10 * M + 1 - b_value != (5 * j_value + 5 - q_value) * prime:
                raise AssertionError((M, row, "layer identity"))
            if not (0 <= b_value < prime):
                raise AssertionError((M, row, "b range"))
            if 7 * b_value > 6 * M + 7:
                raise AssertionError((M, row, "global stable b range"))
            residue = (3 * s_value + 2) % 4
            row_hash.update((repr((M,) + row + (residue,)) + "\n").encode("ascii"))
            row_count += 1

    # Exact far-subcell lengths.
    far_terms = {
        1: (Fraction(1, 45), Fraction(2, 35)),
        2: (Fraction(1, 230), Fraction(1, 44)),
        3: (Fraction(0), Fraction(1, 90)),
        4: (Fraction(0), Fraction(11, 2185)),
        5: (Fraction(0), Fraction(1, 460)),
        6: (Fraction(0), Fraction(1, 1485)),
    }
    reconstructed_terms: dict[int, tuple[Fraction, Fraction]] = {}
    eta = Fraction(1, 5)
    for j_value in range(1, 20):
        q1 = max(
            Fraction(0),
            min(Fraction(10, 5 * j_value + 4), (10 - eta) / (5 * j_value + 4))
            - Fraction(16, 8 * j_value + 7),
        )
        q2 = max(
            Fraction(0),
            min(Fraction(6, 3 * j_value + 2), (10 - eta) / (5 * j_value + 3))
            - Fraction(8, 4 * j_value + 3),
        )
        if q1 or q2:
            reconstructed_terms[j_value] = (q1, q2)
    if reconstructed_terms != far_terms:
        raise AssertionError(reconstructed_terms)
    far_coefficient = sum((left + right for left, right in far_terms.values()), Fraction(0))
    expected_far = Fraction(1139587, 9085230)
    if far_coefficient != expected_far:
        raise AssertionError(far_coefficient)

    lower, upper = capacity_enclosure()

    # Independent b=900 rational reconstruction and exact factorization.
    phi_g1 = stable_phi(900, 3, 0)
    phi_g0 = stable_phi(900, 3, 1)
    common = math.gcd(abs(phi_g1.numerator), abs(phi_g0.numerator))
    odd_factors = [911, 971, 991, 1031, 1051, 1091, 1151, 1171, 1231, 1291, 2399]
    expected_common = 2**449 * math.prod(odd_factors)
    if common != expected_common:
        raise AssertionError((common, expected_common))
    for factor in odd_factors:
        if any(factor % divisor == 0 for divisor in range(2, math.isqrt(factor) + 1)):
            raise AssertionError((factor, "not prime"))
    if phi_g1.numerator % 2399 or phi_g0.numerator % 2399:
        raise AssertionError("mandatory numerator residue")
    if phi_g1.denominator % 2399 == 0 or phi_g0.denominator % 2399 == 0:
        raise AssertionError("mandatory denominator unit")

    terminal = terminal_state_mod(299, 2399)
    if terminal != (7, 2392, 0, 0):
        raise AssertionError(terminal)
    if terminal[-1] != 0 or sum(terminal) % 2399 != 0:
        raise AssertionError((terminal, "g1/g0"))
    if 10 * 2249 + 1 - 900 != 9 * 2399:
        raise AssertionError("mandatory row identity")

    # The geometric blocks and the elementary inherited-height domination.
    blocks = []
    previous_upper = -1
    for n_value in range(3, 11):
        M = 5**n_value
        lower_b = (M + 4) // 5
        upper_b = math.floor(Fraction(6 * M, 7) + 1)
        if lower_b <= previous_upper:
            raise AssertionError((n_value, lower_b, previous_upper))
        if lower_b < 8 or 2 ** (lower_b + 1) < 50 * lower_b + 1:
            raise AssertionError((n_value, lower_b, "height domination"))
        blocks.append([n_value, M, lower_b, upper_b])
        previous_upper = upper_b

    missing_per_M = Decimal("0.1177979020165907632818384072")
    far_decimal = Decimal(far_coefficient.numerator) / Decimal(far_coefficient.denominator)
    if far_decimal <= missing_per_M:
        raise AssertionError((far_decimal, missing_per_M))

    body: dict[str, Any] = {
        "schema": "item266-far-offray-weighted-barrier-certificate-v1",
        "labels": {
            "globalization": "PROVED",
            "stable_and_far_capacity": "PROVED using PNT and exact interval algebra",
            "stable_eliminant_and_witness": "PROVED",
            "bounded_row_replay": "EXACT FINITE ONLY",
            "information_barrier": "PROVED, scoped to the layer-product and inherited componentwise-height containers",
            "cross_b_cancellation_theorem": "OPEN",
            "new_route1_rate": 0,
        },
        "finite_globalization_replay": {
            "M_range": [1, max_M],
            "stable_rows": row_count,
            "fixed_small_prime_rows": small_prime_rows,
            "forward_inverse_match_for_p_ge_11": True,
            "row_sha256": row_hash.hexdigest(),
        },
        "stable_capacity": {
            "series": "sum_j>=1 (6/((5j+4)(8j+7)) + 2/((3j+2)(4j+3)))",
            "decimal_enclosure": [lower, upper],
            "reported_decimal": "0.239111014698... per M",
            "reported_per_6M": "0.039851835783...",
        },
        "far_b_ge_M_over_5": {
            "terms": {str(j): [str(left), str(right)] for j, (left, right) in far_terms.items()},
            "coefficient_exact": str(far_coefficient),
            "coefficient_decimal": format(far_decimal, "f"),
            "per_6M_decimal": format(far_decimal / 6, "f"),
            "missing_per_M": format(missing_per_M, "f"),
            "excess_over_missing": format(far_decimal - missing_per_M, "f"),
        },
        "mandatory_witness": {
            "row_M_s_p_j_q_b_r": [2249, 299, 2399, 1, 1, 900, 3],
            "terminal_mod_p": list(terminal),
            "phi_g1_sha256": hashlib.sha256(str(phi_g1).encode("ascii")).hexdigest(),
            "phi_g0_sha256": hashlib.sha256(str(phi_g0).encode("ascii")).hexdigest(),
            "denominators_mod_p": [phi_g1.denominator % 2399, phi_g0.denominator % 2399],
            "gcd_factorization": {"2": 449, **{str(factor): 1 for factor in odd_factors}},
            "gcd_decimal_sha256": hashlib.sha256(str(common).encode("ascii")).hexdigest(),
        },
        "mock_block_check": {
            "M_n": "5^n",
            "checked_blocks": blocks,
            "proof_bound": "G_tilde(b,r) <= 10M_n+1 <= 50b+1 <= 2^(b+1) for b>=8",
            "scope": "countermodel to layer divisibility plus inherited height only; not to the actual hypergeometric recurrence",
        },
        "item149_overlap": {
            "already_booked": "first post-Cartier rank-one copy",
            "candidate_only": "one additional common first-gate copy",
            "not_implied": "A1 or a third copy",
            "new_rate_booking": 0,
        },
    }
    payload = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    body["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-M", type=int, default=240)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_M)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "output": str(args.output), "payload_sha256": result["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
