#!/usr/bin/env python3
"""Exact replay for Item 198's paired common-valuation theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item198_actual_all_lift_pair_certificate.json"
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
    for d in range(2, math.isqrt(limit) + 1):
        if sieve[d]:
            sieve[d * d : limit + 1 : d] = b"\x00" * (
                (limit - d * d) // d + 1
            )
    return [p for p in range(7, limit + 1) if sieve[p]]


def poly_add(left: list[int], right: list[int]) -> list[int]:
    result = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return result


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return result


def poly_eval(polynomial: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(polynomial):
        result = result * value + coefficient
    return result


def continuant_polynomial(h: int) -> list[int]:
    """Return [X-4h,X-4h+4,...,X+4h] in ascending powers."""
    previous_previous = [1]
    previous = [-4 * h, 1]
    for j in range(-h + 1, h + 1):
        previous_previous, previous = previous, poly_add(
            poly_mul([4 * j, 1], previous), previous_previous
        )
    return previous


def continuant_value(h: int, value: int, modulus: int | None = None) -> int:
    previous_previous = 1
    previous = value - 4 * h
    if modulus is not None:
        previous %= modulus
    for j in range(-h + 1, h + 1):
        new_value = (value + 4 * j) * previous + previous_previous
        if modulus is not None:
            new_value %= modulus
        previous_previous, previous = previous, new_value
    return previous


def continuant_derivative(h: int) -> int:
    previous_previous_value = 1
    previous_previous_derivative = 0
    previous_value = -4 * h
    previous_derivative = 1
    for j in range(-h + 1, h + 1):
        constant = 4 * j
        new_value = constant * previous_value + previous_previous_value
        new_derivative = (
            previous_value
            + constant * previous_derivative
            + previous_previous_derivative
        )
        previous_previous_value, previous_value = previous_value, new_value
        (
            previous_previous_derivative,
            previous_derivative,
        ) = previous_derivative, new_derivative
    return previous_derivative


def recurrence_values(
    initial_0: int,
    initial_1: int,
    last_index: int,
    modulus: int | None = None,
) -> list[int]:
    if last_index == 0:
        return [initial_0 % modulus if modulus else initial_0]
    values = [initial_0, initial_1]
    if modulus is not None:
        values = [value % modulus for value in values]
    for n in range(2, last_index + 1):
        value = (4 * n - 2) * values[-1] + values[-2]
        if modulus is not None:
            value %= modulus
        values.append(value)
    return values


def transfer_upper_row(r: int, s: int) -> tuple[int, int]:
    """Return A,B with u_s=A*u_r+B*u_(r-1)."""
    previous_a, current_a = 0, 1
    previous_b, current_b = 1, 0
    for n in range(r + 1, s + 1):
        previous_a, current_a = (
            current_a,
            (4 * n - 2) * current_a + previous_a,
        )
        previous_b, current_b = (
            current_b,
            (4 * n - 2) * current_b + previous_b,
        )
    return current_a, current_b


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero is not used in this certificate")
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def polynomial_regression(max_h: int = 8) -> dict:
    rows = []
    for h in range(max_h + 1):
        polynomial = continuant_polynomial(h)
        if len(polynomial) != 2 * h + 2:
            raise AssertionError((h, "degree"))
        if any(polynomial[index] for index in range(0, len(polynomial), 2)):
            raise AssertionError((h, "not odd"))
        derivative = continuant_derivative(h)
        if polynomial[1] != derivative:
            raise AssertionError((h, polynomial[1], derivative))
        for value in (-14, -2, 0, 6, 22):
            if poly_eval(polynomial, value) != continuant_value(h, value):
                raise AssertionError((h, value, "evaluation"))
        rows.append([h, derivative, polynomial[-1]])
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "h_range": [0, max_h],
        "oddness_and_derivative_checks": len(rows),
        "evaluation_checks": 5 * len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "all_exact": True,
    }


def transfer_gcd_regression(prime_limit: int = 43) -> dict:
    rows = []
    checks = 0
    for prime in primes_upto(prime_limit):
        q = recurrence_values(1, 1, prime - 1)
        for r in range(1, (prime - 1) // 2):
            s = prime - 1 - r
            h = (prime - 3) // 2 - r
            a_entry, b_entry = transfer_upper_row(r, s)
            if b_entry != continuant_value(h, 2 * prime):
                raise AssertionError((prime, r, "continuant entry"))
            if q[s] != a_entry * q[r] + b_entry * q[r - 1]:
                raise AssertionError((prime, r, "transfer value"))
            left_gcd = math.gcd(q[r], q[s])
            right_gcd = math.gcd(q[r], b_entry)
            if left_gcd != right_gcd:
                raise AssertionError((prime, r, left_gcd, right_gcd))
            if math.gcd(q[r], q[r - 1]) != 1:
                raise AssertionError((prime, r, "adjacent gcd"))
            if a_entry % prime != 1:
                raise AssertionError((prime, r, "A mod p"))
            rows.append([prime, r, s, h, left_gcd])
            checks += 1
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "prime_limit": prime_limit,
        "transfer_gcd_checks": checks,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "all_exact": True,
    }


def actual_root_regression(prime_limit: int) -> dict:
    root_rows = []
    square_rows = []
    cube_rows = []
    central_rows = []
    slope_checks = 0
    pair_checks = 0
    for prime in primes_upto(prime_limit):
        modulus = prime**3
        q = recurrence_values(1, 1, 2 * prime, modulus)
        companion = recurrence_values(1, 3, prime - 1, modulus)
        center = (prime - 1) // 2
        for r in range(1, center + 1):
            if q[r] % prime:
                continue
            if r == center:
                central_rows.append([prime, r, q[r] // prime % prime])
                continue
            s = prime - 1 - r
            h = (prime - 3) // 2 - r
            d_h = continuant_derivative(h)
            b_entry = continuant_value(h, 2 * prime)
            if q[s] % prime:
                raise AssertionError((prime, r, s, "missing mate"))

            slope_numerator = (-q[r + prime] - q[r]) % (prime**2)
            if slope_numerator % prime:
                raise AssertionError((prime, r, "slope integrality"))
            slope = slope_numerator // prime % prime
            expected_slope = (-2 * d_h * q[r - 1]) % prime
            if slope != expected_slope:
                raise AssertionError((prime, r, slope, expected_slope))
            slope_checks += 1

            wronskian = (
                companion[r] * q[r - 1] - companion[r - 1] * q[r]
            ) % prime
            expected_wronskian = (2 if r & 1 else -2) % prime
            if wronskian != expected_wronskian:
                raise AssertionError((prime, r, "Wronskian"))
            if q[r - 1] % prime == 0 or companion[r] % prime == 0:
                raise AssertionError((prime, r, "unit failure"))

            pair_square = q[r] % (prime**2) == 0 and q[s] % (prime**2) == 0
            criterion_square = q[r] % (prime**2) == 0 and d_h % prime == 0
            if pair_square != criterion_square:
                raise AssertionError((prime, r, "square iff"))

            pair_cube = q[r] % (prime**3) == 0 and q[s] % (prime**3) == 0
            criterion_cube = q[r] % (prime**3) == 0 and d_h % (prime**2) == 0
            if pair_cube != criterion_cube:
                raise AssertionError((prime, r, "cube iff"))

            if (b_entry % (prime**2) == 0) != (d_h % prime == 0):
                raise AssertionError((prime, r, "B square iff"))
            if (b_entry % (prime**3) == 0) != (d_h % (prime**2) == 0):
                raise AssertionError((prime, r, "B cube iff"))

            if criterion_square:
                next_digit = (
                    q[s] // (prime**2)
                    - q[r] // (prime**2)
                    - 2 * (d_h // prime) * q[r - 1]
                ) % prime
                if next_digit != 0:
                    raise AssertionError((prime, r, "next digit", next_digit))

            row = {
                "p": prime,
                "r": r,
                "s": s,
                "h": h,
                "lambda_r": q[r] // prime % prime,
                "lambda_s": q[s] // prime % prime,
                "D_h_mod_p": d_h % prime,
                "paired_square": pair_square,
                "paired_cube": pair_cube,
            }
            root_rows.append(row)
            if pair_square:
                square_rows.append(row)
            if pair_cube:
                cube_rows.append(row)
            pair_checks += 1

    stream = json.dumps(root_rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    return {
        "label": "EXPERIMENTAL_FINITE_IDENTITY_REGRESSION_NOT_EXISTENCE_PROOF",
        "prime_limit": prime_limit,
        "noncentral_lower_root_rows": len(root_rows),
        "central_root_rows": central_rows,
        "slope_and_wronskian_checks": slope_checks,
        "square_cube_pair_checks": pair_checks,
        "actual_paired_square_rows": square_rows,
        "actual_paired_cube_rows": cube_rows,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def modified_seed_countermodel() -> dict:
    lower_index = 1
    witnesses = [(7, 1), (97, 46), (107, 51)]
    radical = math.prod(prime for prime, _ in witnesses)
    lower_value = radical * radical
    maximum_index = max(prime - 1 - lower_index for prime, _ in witnesses)
    u = recurrence_values(1, lower_value, maximum_index)
    v = recurrence_values(0, 1, maximum_index)

    wronskian_checks = 0
    for n in range(1, maximum_index + 1):
        wronskian = v[n] * u[n - 1] - v[n - 1] * u[n]
        if wronskian != (-1) ** (n - 1):
            raise AssertionError((n, wronskian, "countermodel Wronskian"))
        wronskian_checks += 1

    rows = []
    for prime, h in witnesses:
        if prime != 2 * lower_index + 2 * h + 3:
            raise AssertionError((prime, h, "tied index"))
        d_h = continuant_derivative(h)
        b_entry = continuant_value(h, 2 * prime)
        if valuation(d_h, prime) != 1:
            raise AssertionError((prime, h, "D valuation"))
        if valuation(b_entry, prime) != 2:
            raise AssertionError((prime, h, "B valuation"))
        paired_index = prime - 1 - lower_index
        if u[lower_index] % (prime**2) or u[paired_index] % (prime**2):
            raise AssertionError((prime, paired_index, "paired square"))
        a_entry, transfer_b = transfer_upper_row(lower_index, paired_index)
        if transfer_b != b_entry:
            raise AssertionError((prime, "countermodel transfer B"))
        if u[paired_index] != a_entry * u[lower_index] + transfer_b * u[0]:
            raise AssertionError((prime, "countermodel exact transfer"))
        rows.append(
            {
                "p": prime,
                "h": h,
                "paired_index": paired_index,
                "v_p_D_h": valuation(d_h, prime),
                "v_p_K_h_2p": valuation(b_entry, prime),
                "lower_divided_square_digit": lower_value // (prime**2) % prime,
                "paired_divided_square_digit": u[paired_index] // (prime**2) % prime,
                "v_p_paired_value": valuation(u[paired_index], prime),
            }
        )

    stream = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    return {
        "classification": "PROVED_MODIFIED_SEED_COUNTERMODEL_NOT_ACTUAL_BETA_SEED",
        "witness_list_scope": "FINITE_EXPLICIT_FIXTURE_NOT_AN_EXISTENCE_SCAN",
        "lower_index": lower_index,
        "witness_primes": [prime for prime, _ in witnesses],
        "radical_R": radical,
        "lower_value_R_squared": lower_value,
        "initial_seed": [1, lower_value],
        "companion_seed": [0, 1],
        "wronskian_checks": wronskian_checks,
        "rows": rows,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "scope_warning": (
            "This solution has u_1=R^2, not the actual seed q_1=1; it "
            "does not assert the global actual-seed anti-period/reflection law."
        ),
    }


def certificate(prime_limit: int) -> dict:
    return {
        "item": 198,
        "classification": {
            "PROVED": [
                "gcd(q_r,q_s)=gcd(q_r,K_h(2p)) for the actual beta pair",
                "p^2 divides both paired values iff p^2 divides q_r and p divides D_h",
                "p^3 divides both paired values iff p^3 divides q_r and p^2 divides D_h",
                "q_s/p^2=q_r/p^2+2(D_h/p)q_(r-1) mod p on an all-lift pair",
                "the prescribed-index all-lift radical satisfies R_N^2|q_N",
                "transfer/continuant/unit-Wronskian data admit the modified-seed simultaneous countermodel",
            ],
            "EXPERIMENTAL_FINITE": [
                f"actual-root identity regression through p<={prime_limit}"
            ],
            "OPEN": [
                "existence of an actual noncentral all-lift beta pair",
                "a useful all-prime product bound or positive logarithmic mass",
                "actual mixed-coefficient valuation",
                "same-index divided matching and small moving-CRT synchronization",
            ],
        },
        "exact_identities": {
            "transfer": "q_s=A*q_r+K_h(2p)*q_(r-1), A=1 mod p",
            "common_gcd": "gcd(q_r,q_s)=gcd(q_r,K_h(2p))",
            "continuant_expansion": "K_h(2p)=2p*D_h+8p^3*E_h+...",
            "paired_square_iff": "p^2|q_r,q_s iff p^2|q_r and p|D_h",
            "paired_cube_iff": "p^3|q_r,q_s iff p^3|q_r and p^2|D_h",
            "next_square_digit": "q_s/p^2=q_r/p^2+2(D_h/p)q_(r-1) mod p",
            "wronskian": "P_r*q_(r-1)-P_(r-1)*q_r=2*(-1)^(r-1)",
        },
        "logical_separation": [
            "actual root existence at the prescribed lower index",
            "local all-lift criterion",
            "actual mixed-coefficient p^2 valuation",
            "same-index divided matching",
            "saddle-compatible small moving-CRT representative",
        ],
        "mass_ledger": {
            "post_3m_gap_per_6m": "0.01963298366943179388",
            "R_squared_required_log_R_per_m": "0.05889895100829538164",
            "beta_log_q_N_per_6m": "1.1685311871794864979",
            "proved_ceiling_only": "R_N^2 divides q_N; no positive lower mass follows",
        },
        "dependency_sha256": {
            "sources/item165_noncentral_singular_report.md": "d7b4475d2adfeff9a5f1c70a9c6b318d0c2b140bf90b194aa9acb6fdddcc2650",
            "sources/item166_actual_singular_report.md": "2a8f1c84b91fa7d18fb02417cf480baae819afa795968375e5a3767fc0f52f76",
            "sources/bessel_denominator_all_lift_branching_wieferich_barrier.md": "f02b4b936c2ca810299f037e158e7406214e89ef77e8ca98dcd67b2a9bd00911",
        },
        "polynomial_regression": polynomial_regression(),
        "transfer_gcd_regression": transfer_gcd_regression(),
        "actual_root_regression": actual_root_regression(prime_limit),
        "modified_seed_countermodel": modified_seed_countermodel(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=251)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.prime_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    actual = result["actual_root_regression"]
    countermodel = result["modified_seed_countermodel"]
    print(
        json.dumps(
            {
                "output": str(args.output),
                "finite_noncentral_lower_roots": actual[
                    "noncentral_lower_root_rows"
                ],
                "finite_actual_paired_square_rows": actual[
                    "actual_paired_square_rows"
                ],
                "countermodel_witness_primes": countermodel["witness_primes"],
                "countermodel_R_squared": countermodel["lower_value_R_squared"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
