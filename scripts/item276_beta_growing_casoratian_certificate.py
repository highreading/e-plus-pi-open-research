#!/usr/bin/env python3
"""Deterministic certificate for Item 276's primitive growing-Casoratian theorem.

The script uses only exact integer arithmetic and the Python standard library.
Bounded checks replay identities; they are not a search for exceptional primes
and carry no asymptotic or density inference.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


Poly = tuple[int, ...]  # coefficients in increasing degree


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def p_add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    return trim(tuple(
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ))


def p_mul(left: Poly, right: Poly) -> Poly:
    result = [0] * (len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            result[i + j] += a_value * b_value
    return trim(tuple(result))


def p_eval(poly: Poly, value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def p_shift(poly: Poly, shift: int) -> Poly:
    """Return poly(X+shift), exactly."""
    result: Poly = (0,)
    power: Poly = (1,)
    affine = (shift, 1)
    for coefficient in poly:
        result = p_add(result, tuple(coefficient * value for value in power))
        power = p_mul(power, affine)
    return trim(result)


def continuant_polynomials(limit: int) -> list[Poly]:
    values: list[Poly] = [(0,), (1,)]
    for d in range(limit - 1):
        multiplier = (4 * d + 6, 4)  # 4X+4d+6
        values.append(p_add(p_mul(multiplier, values[-1]), values[-2]))
    return values[: limit + 1]


def continuant(n: int, h: int) -> int:
    if h == 0:
        return 0
    previous, current = 0, 1
    for d in range(h - 1):
        previous, current = current, (4 * n + 4 * d + 6) * current + previous
    return current


def q_values(limit: int) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero is not used in this certificate")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def digest_rows(rows: list[Any]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_result() -> dict[str, Any]:
    max_n = 36
    max_h = 24
    q = q_values(max_n + max_h + 64)
    polynomials = continuant_polynomials(max_h + 4)

    polynomial_rows: list[dict[str, Any]] = []
    for h in range(max_h + 1):
        for n in range(max_n + 1):
            exact = continuant(n, h)
            assert p_eval(polynomials[h], n) == exact
            polynomial_rows.append({"n": n, "h": h, "P": exact})

    transfer_rows: list[dict[str, Any]] = []
    for n in range(max_n + 1):
        for h in range(max_h + 1):
            coefficient_left = continuant(n, h)
            coefficient_right = continuant(n + 1, h - 1) if h >= 1 else 1
            # For h=0 the transfer formula is q_n=0*q_(n+1)+1*q_n.
            value = coefficient_left * q[n + 1] + coefficient_right * q[n]
            assert value == q[n + h]
            assert math.gcd(q[n], q[n + h]) == math.gcd(q[n], coefficient_left)
            transfer_rows.append(
                {
                    "n": n,
                    "h": h,
                    "P_h": coefficient_left,
                    "P_h_minus_1_shift": coefficient_right,
                    "q_target": value,
                }
            )

    minor_rows: list[dict[str, Any]] = []
    for n in range(0, 17):
        for d in range(0, 9):
            for e in range(d + 1, 13):
                row_e = (
                    continuant(n, e),
                    continuant(n + 1, e - 1) if e >= 1 else 1,
                )
                row_d = (
                    continuant(n, d),
                    continuant(n + 1, d - 1) if d >= 1 else 1,
                )
                determinant = row_e[0] * row_d[1] - row_e[1] * row_d[0]
                expected = (-1) ** d * continuant(n + d, e - d)
                assert determinant == expected
                minor_rows.append(
                    {"n": n, "d": d, "e": e, "determinant": determinant}
                )

    casoratian_rows: list[dict[str, Any]] = []
    valuation_rows: list[dict[str, Any]] = []
    check_primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    for n in range(1, max_n + 1):
        factors = {
            prime: valuation(q[n], prime)
            for prime in check_primes
            if q[n] % prime == 0
        }
        for h in range(1, max_h + 1):
            p_h = continuant(n, h)
            casoratian = q[n] * q[n + h + 1] - q[n + 1] * q[n + h]
            residual = casoratian + p_h * q[n + 1] ** 2
            assert residual % q[n] == 0
            casoratian_rows.append(
                {
                    "n": n,
                    "h": h,
                    "C": casoratian,
                    "P": p_h,
                    "residual_quotient": residual // q[n],
                }
            )
            for prime, exponent in factors.items():
                p_order = valuation(p_h, prime) if p_h else 10**9
                c_order = valuation(casoratian, prime) if casoratian else 10**9
                target_order = valuation(q[n + h], prime)
                for depth in range(1, exponent + 1):
                    left = c_order >= depth
                    middle = p_order >= depth
                    right = target_order >= depth
                    assert left == middle == right
                if p_order < exponent:
                    assert c_order == p_order
                valuation_rows.append(
                    {
                        "n": n,
                        "h": h,
                        "p": prime,
                        "a": exponent,
                        "v_P": p_order,
                        "v_C": c_order,
                        "v_q_shift": target_order,
                    }
                )

    height_rows: list[dict[str, Any]] = []
    for n in range(0, max_n + 1):
        for h in range(1, max_h + 1):
            p_h = continuant(n, h)
            lower = (4 * n + 6) ** (h - 1)
            upper = (4 * (n + h)) ** (h - 1)
            assert lower <= p_h <= upper
            height_rows.append(
                {"n": n, "h": h, "lower": lower, "P": p_h, "upper": upper}
            )

    antiperiod_rows: list[dict[str, Any]] = []
    for modulus in range(3, 48, 2):
        for n in range(0, 31):
            assert (q[n + modulus] + q[n]) % modulus == 0
            if q[n] % modulus == 0:
                assert continuant(n, modulus) % modulus == 0
            antiperiod_rows.append(
                {
                    "M": modulus,
                    "n": n,
                    "q_n_mod_M": q[n] % modulus,
                    "P_M_mod_M": continuant(n, modulus) % modulus,
                }
            )

    deoverlap_rows: list[dict[str, Any]] = []
    clearing_samples = (1, 3, 5, 7, 9, 11, 15, 25, 49, 77, 121)
    for n in range(1, 25):
        for clearing in clearing_samples:
            qbar = q[n] // math.gcd(q[n], clearing)
            assert math.gcd(qbar, q[n + 1]) == 1
            for h in range(1, 15):
                p_h = continuant(n, h)
                casoratian = q[n] * q[n + h + 1] - q[n + 1] * q[n + h]
                assertions = (
                    casoratian % qbar == 0,
                    p_h % qbar == 0,
                    q[n + h] % qbar == 0,
                )
                assert assertions[0] == assertions[1] == assertions[2]
                deoverlap_rows.append(
                    {
                        "n": n,
                        "D": clearing,
                        "h": h,
                        "qbar": qbar,
                        "equivalent_divisibility": assertions[0],
                    }
                )

    return {
        "schema": "item276-beta-growing-casoratian-certificate-v1",
        "description": (
            "Exact replay for the primitive two-state growing-window "
            "Casoratian/continuant singleton-depth theorem"
        ),
        "parameters": {
            "polynomial_n_max": max_n,
            "gap_h_max": max_h,
            "minor_n_max": 16,
            "minor_d_max": 8,
            "minor_e_max": 12,
            "antiperiod_odd_modulus_max": 47,
            "deoverlap_n_max": 24,
            "deoverlap_h_max": 14,
        },
        "exact_identities": {
            "beta_recurrence": "q_0=q_1=1; q_(n+2)=(4n+6)q_(n+1)+q_n",
            "continuant_recurrence": (
                "P_0=0; P_1=1; "
                "P_(h+2)(X)=(4X+4h+6)P_(h+1)(X)+P_h(X)"
            ),
            "transfer": (
                "q_(n+h)=P_h(n)q_(n+1)+P_(h-1)(n+1)q_n"
            ),
            "gap_gcd": "gcd(q_n,q_(n+h))=gcd(q_n,P_h(n))",
            "transition_minor": (
                "det(r_e,r_d)=(-1)^d P_(e-d)(n+d), "
                "r_d=(P_d(n),P_(d-1)(n+1))"
            ),
            "primitive_casoratian": (
                "C_h(n)=q_n q_(n+h+1)-q_(n+1)q_(n+h); "
                "C_h(n)=-P_h(n)q_(n+1)^2 mod q_n"
            ),
            "level_equivalence": (
                "for p^s|q_n: p^s|C_h(n) iff p^s|P_h(n) "
                "iff p^s|q_(n+h)"
            ),
            "height_bounds": (
                "(4n+6)^(h-1)<=P_h(n)<=[4(n+h)]^(h-1), h>=1"
            ),
            "odd_antiperiod": "q_(n+M)=-q_n mod M for odd M",
            "deoverlap": (
                "qbar=q_n/gcd(q_n,D): qbar|C_h(n) iff qbar|P_h(n) "
                "iff qbar|q_(n+h)"
            ),
        },
        "bounded_exact_checks": {
            "label": "EXACT FINITE ONLY",
            "polynomial_rows": len(polynomial_rows),
            "polynomial_digest": digest_rows(polynomial_rows),
            "transfer_and_gcd_rows": len(transfer_rows),
            "transfer_and_gcd_digest": digest_rows(transfer_rows),
            "transition_minor_rows": len(minor_rows),
            "transition_minor_digest": digest_rows(minor_rows),
            "casoratian_rows": len(casoratian_rows),
            "casoratian_digest": digest_rows(casoratian_rows),
            "valuation_rows": len(valuation_rows),
            "valuation_digest": digest_rows(valuation_rows),
            "height_rows": len(height_rows),
            "height_digest": digest_rows(height_rows),
            "antiperiod_rows": len(antiperiod_rows),
            "antiperiod_digest": digest_rows(antiperiod_rows),
            "deoverlap_rows": len(deoverlap_rows),
            "deoverlap_digest": digest_rows(deoverlap_rows),
            "exceptional_singleton_search": False,
            "asymptotic_extrapolation": False,
        },
        "theorem": {
            "admissible_class": (
                "one primitive 2x2 minor of the two-state transition-row "
                "matrix, equivalently one one-gap continuant P_h(n), or "
                "the associated scalar Casoratian C_h(n)"
            ),
            "singleton_no_go": (
                "A level p^s dividing q_n can divide the primitive "
                "Casoratian residual exactly when the same level divides "
                "q_(n+h); an in-window singleton cannot be reached."
            ),
            "height_threshold": (
                "log P_h(n)=O(n) is possible in this class exactly on the "
                "gap scale h=O(n/log n)."
            ),
            "universal_reach": (
                "Taking the odd modulus M as the gap reaches every divisor "
                "M|q_n, but costs log P_M(n)>=(M-1)log(4n+6)."
            ),
            "high_tail_consequence": (
                "For a high singleton prime power p^a>n-block-length, the "
                "universal gap h=p^a has at least main n log n coefficient "
                "height and is not an O(n)-height auxiliary."
            ),
            "deoverlap_consequence": (
                "With qbar=q_n/gcd(q_n,D_m), reaching qbar transports qbar "
                "to q_(n+h); the Item265 two-copy reservoir is not reduced."
            ),
            "scope_limit": (
                "No claim is made for products or sums of a growing number "
                "of minors, arbitrary growing Hankel determinants, or a new "
                "global relation among distinct gaps."
            ),
        },
        "admission": {
            "uniform_prime_power_height_O_n": False,
            "little_o_squarefull": False,
            "positive_linear_capacity_admission": "FAIL",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
        "open": [
            "growing products or sums in which p-adic depth can split among many gaps",
            "arbitrary growing Hankel or block determinants outside the two-state primitive class",
            "a uniform short second-zero theorem or its exclusion for each high singleton level",
            "the uniform v_p(q_n) log p=O(n) theorem or a sufficient little-oh aggregate",
            "the actual correlation with the clearing divisor and transverse matching factor",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_result(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
