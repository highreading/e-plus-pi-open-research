#!/usr/bin/env python3
"""Portable exact certificate for Item 264.

The checker verifies the global j=1 row bijection, the admission-test
counterexamples inherited from Items 245/248, and the exact full-gate
coordinates at those rows.  It performs no asymptotic collision scan.
Any bounded arithmetic replay is labelled EXACT FINITE ONLY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def factorial_tables(prime: int) -> tuple[list[int], list[int], list[int]]:
    factorial = [1] * prime
    for value in range(1, prime):
        factorial[value] = factorial[value - 1] * value % prime
    inverse_factorial = [1] * prime
    inverse_factorial[-1] = pow(factorial[-1], -1, prime)
    for value in range(prime - 1, 0, -1):
        inverse_factorial[value - 1] = inverse_factorial[value] * value % prime
    inverse = [0] * prime
    for value in range(1, prime):
        inverse[value] = factorial[value - 1] * inverse_factorial[value] % prime
    return factorial, inverse_factorial, inverse


def kernel_coefficients(
    h_value: int,
    extra: int,
    prime: int,
    factorial: list[int],
    inverse_factorial: list[int],
) -> list[int]:
    """Coefficients of (1-z)^(2h)(1+z)^extra modulo p."""
    answer = []
    factorial_2h = factorial[2 * h_value]
    for degree in range(2 * h_value + extra + 1):
        value = 0
        for right_degree in range(extra + 1):
            left_degree = degree - right_degree
            if 0 <= left_degree <= 2 * h_value:
                choose = (
                    factorial_2h
                    * inverse_factorial[left_degree]
                    * inverse_factorial[2 * h_value - left_degree]
                ) % prime
                if left_degree % 2:
                    choose = -choose
                value += math.comb(extra, right_degree) * choose
        answer.append(value % prime)
    return answer


def normalized_sum_mod(
    kernel: list[int],
    a_value: int,
    q_value: int,
    odd: bool,
    prime: int,
    inverse: list[int],
) -> int:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    ratio = 1
    answer = 0
    for t_value in range(maximum_t + 1):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        answer = (answer + ratio * kernel[degree]) % prime
        if t_value == maximum_t:
            break
        numerator = a_value + t_value + 1 if odd else a_value + t_value
        denominator = (
            q_value + a_value + t_value + 2
            if odd
            else q_value + a_value + t_value + 1
        )
        assert 0 < denominator < prime
        ratio = -ratio * numerator * inverse[denominator] % prime
    return answer


def divided_gate(prime: int, h_value: int, s_value: int) -> tuple[int, int, int]:
    """Return Item-218 Q0,Q1 and its necessary eliminant."""
    assert prime == 4 * h_value + 6 * s_value + 3
    factorial, inverse_factorial, inverse = factorial_tables(prime)
    kernel_0 = kernel_coefficients(h_value, 1, prime, factorial, inverse_factorial)
    kernel_1 = kernel_coefficients(h_value, 4, prime, factorial, inverse_factorial)
    x_value = normalized_sum_mod(kernel_0, s_value, 2 * s_value, True, prime, inverse)
    y_value = normalized_sum_mod(kernel_0, h_value, 2 * s_value, True, prime, inverse)
    u_value = normalized_sum_mod(kernel_1, s_value, 2 * s_value - 1, False, prime, inverse)
    v_value = normalized_sum_mod(kernel_1, h_value, 2 * s_value - 1, True, prime, inverse)

    sign_s = -1 if s_value % 2 else 1
    sign_h = -1 if h_value % 2 else 1
    A = sign_s * factorial[2 * s_value] * factorial[s_value]
    A = A * inverse_factorial[3 * s_value + 1] % prime
    B = sign_h * factorial[2 * s_value] * factorial[h_value]
    B = B * inverse_factorial[2 * s_value + h_value + 1] % prime
    C = -sign_s * factorial[2 * s_value - 1] * factorial[s_value - 1]
    C = C * inverse_factorial[3 * s_value - 1] % prime
    D = sign_h * factorial[2 * s_value - 1] * factorial[h_value]
    D = D * inverse_factorial[2 * s_value + h_value] % prime
    q0 = (2 * A * x_value - B * y_value) % prime
    q1 = (2 * C * u_value - D * v_value) % prime
    eliminant = (
        (2 * s_value + h_value + 1) * x_value * v_value
        + 3 * (3 * s_value + 1) * u_value * y_value
    ) * inverse[2 * s_value] % prime
    if q0 == q1 == 0:
        assert eliminant == 0
    return q0, q1, eliminant


def rows_from_s(global_m: int) -> list[tuple[int, int, int]]:
    rows = []
    for s_value in range(1, max(1, (global_m - 5) // 4 + 1)):
        if 4 * s_value > global_m - 5:
            break
        if (s_value - global_m - 1) % 3:
            continue
        prime = (4 * global_m + 2 * s_value + 1) // 3
        h_value = (global_m - 4 * s_value - 2) // 3
        assert 3 * prime == 4 * global_m + 2 * s_value + 1
        assert global_m == 3 * h_value + 4 * s_value + 2
        assert prime == 4 * h_value + 6 * s_value + 3
        if is_prime(prime):
            rows.append((prime, h_value, s_value))
    return rows


def rows_from_prime_interval(global_m: int) -> list[tuple[int, int, int]]:
    lower_num = 4 * global_m + 3
    upper_num = 3 * global_m - 1
    rows = []
    # p >= lower_num/3 and p <= upper_num/2.
    lower = (lower_num + 2) // 3
    upper = upper_num // 2
    for prime in range(lower, upper + 1):
        if not is_prime(prime):
            continue
        numerator_s = 3 * prime - 4 * global_m - 1
        assert numerator_s % 2 == 0
        s_value = numerator_s // 2
        h_value = 3 * global_m - 2 * prime
        assert s_value >= 1 and h_value >= 1
        assert global_m == 3 * h_value + 4 * s_value + 2
        assert prime == 4 * h_value + 6 * s_value + 3
        rows.append((prime, h_value, s_value))
    return rows


def run(replay_limit: int) -> dict[str, Any]:
    assert replay_limit >= 108
    bijection_rows = 0
    for global_m in range(9, replay_limit + 1):
        left = rows_from_s(global_m)
        right = rows_from_prime_interval(global_m)
        assert left == right
        bijection_rows += len(left)

    # General disjointness: I_j=(4/(2j+1),6/(3j+1)).  The upper
    # endpoint of I_(j+1) lies strictly below the lower endpoint of I_j.
    for j in range(100):
        assert 6 * (2 * j + 1) < 4 * (3 * j + 4)

    witnesses = []
    frozen = [
        # p,h,s,M, W=(a,b), root I, Item-248 interpretation
        (59, 2, 8, 40, None, None, "individual leading pair nu=1 is zero"),
        (109, 4, 15, 74, (88, 70), 33, "normalized Wronskian vanishes at one root"),
        (149, 26, 7, 108, (42, 60), 44, "normalized Wronskian vanishes at one root"),
    ]
    expected_gates = {59: (39, 11, 36), 109: (71, 106, 87), 149: (42, 106, 3)}
    for prime, h_value, s_value, global_m, wronskian, root_i, label in frozen:
        assert global_m == 3 * h_value + 4 * s_value + 2
        assert 4 * global_m + 1 == 3 * prime - 2 * s_value
        gate = divided_gate(prime, h_value, s_value)
        assert gate == expected_gates[prime]
        assert gate[0] or gate[1]
        if wronskian is not None:
            a_value, b_value = wronskian
            assert root_i * root_i % prime == prime - 1
            assert (a_value + b_value * root_i) % prime == 0
        witnesses.append(
            {
                "p": prime,
                "h": h_value,
                "s": s_value,
                "M": global_m,
                "local_record": label,
                "Wronskian_pair": wronskian,
                "root_I": root_i,
                "full_gate_Q0_Q1_E": list(gate),
                "full_gate_collision": False,
            }
        )

    getcontext().prec = 50
    sqrt33 = Decimal(33).sqrt()
    rho = (sqrt33 - Decimal(3)) / Decimal(6)
    H = (
        Decimal(2) * (Decimal(1) + rho).ln()
        - Decimal(4) * (Decimal(1) - rho).ln()
        - Decimal(4) * rho.ln()
    )
    assert abs(H - Decimal("6.327627545440858")) < Decimal("1e-15")
    raw_per_M = Decimal(1) / Decimal(6)
    raw_per_6M = Decimal(1) / Decimal(36)
    square_height_per_M = H / Decimal(2)
    square_height_per_6M = H / Decimal(12)
    multiplicity_threshold = Decimal(6) * H
    assert square_height_per_M > raw_per_M
    assert multiplicity_threshold > 37 and multiplicity_threshold < 38

    theorem = {
        "global_relation": "4M+1=3p-2s; M=3h+4s+2",
        "integral_rows": "s>=1, 4s<=M-5, s=M+1 (mod 3); p=(4M+2s+1)/3; h=(M-4s-2)/3",
        "prime_interval": "(4M+3)/3 <= p <= (3M-1)/2",
        "raw_weight_per_M": "1/6",
        "raw_weight_per_6M": "1/36",
        "full_gate": "Q0=Q1=0 iff the two j=1 divided coordinates vanish",
        "square_container": "R_M^2 divides gcd(C_0(M),C_1(M))",
        "inherited_estimate_ceiling": "mechanically inheriting the componentwise Cauchy bound for any bounded-degree recombination certifies no better than H/2+o(1)=3.1638...; a separately proved low-height cancellation remains open",
        "valuation_needed_to_beat_raw": "a same-height divisibility exponent t must satisfy t>6H=37.9657..., hence t>=38",
        "admission_result": "individual observation seeds and the Item-248 Wronskian are not substitutes for the full Q0=Q1 gate",
    }
    result: dict[str, Any] = {
        "schema": "item264-j1-weighted-gate-v1",
        "theorem": theorem,
        "constants": {
            "rho": str(rho),
            "H": str(H),
            "raw_per_M": str(raw_per_M),
            "raw_per_6M": str(raw_per_6M),
            "square_height_per_M": str(square_height_per_M),
            "square_height_per_6M": str(square_height_per_6M),
            "multiplicity_threshold_strict": str(multiplicity_threshold),
            "minimum_integer_multiplicity": 38,
        },
        "exact_witnesses": witnesses,
        "finite_replay": {
            "label": "EXACT FINITE ONLY",
            "M_range": [9, replay_limit],
            "prime_rows_in_bijection_replay": bijection_rows,
            "collision_scan_performed": False,
            "purpose": "arithmetic bijection and three declared counterexamples only",
        },
        "booking": {
            "new_unconditional_route1_rate": 0,
            "new_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
            "reason": "no weighted full-gate zero-density theorem and every admitted height ceiling is weaker than raw support",
        },
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-limit", type=int, default=600)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item264_j1_weighted_gate_certificate.json",
    )
    args = parser.parse_args()
    result = run(args.replay_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "payload_sha256": result["payload_sha256"],
        "finite_replay": result["finite_replay"],
        "booking": result["booking"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
