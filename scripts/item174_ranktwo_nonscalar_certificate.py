#!/usr/bin/env python3
"""Exact certificate for Item 174: rank-two zeros and scalar-free lifts.

The uniform arguments are in the companion report.  This script performs
exact rational/quasipolynomial checks, audits the archived finite rows, and
replays the scalar-free determinant carry law.  Finite counts are diagnostics
only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb
from pathlib import Path


DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item174_ranktwo_nonscalar_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item174_ranktwo_nonscalar_certificate.json"
)
AUXILIARY_PRIME = 2**61 - 1


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic for 64-bit integers.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p, flag in enumerate(sieve) if flag]


def generalized_binomial(x: Fraction, n: int) -> Fraction:
    value = Fraction(1)
    for j in range(n):
        value *= x - j
        value /= j + 1
    return value


@lru_cache(maxsize=None)
def branch_coefficient_constant(
    s: int, rho: int, multiple: int, z_series: bool
) -> Fraction:
    """Constant term at P=0 of [x^(multiple*P-1)] W_s or Z_s.

    W_s=x^(3s)(1-x)^(5s+2)/(1-x^4)^(2s+2),
    Z_s=x^(3s)(1-x)^(5s+1)/(1-x^4)^(2s+1).
    The branch is P == rho (mod 4).
    """
    numerator_exponent = 5 * s + (1 if z_series else 2)
    order = 2 * s + (0 if z_series else 1)
    residue = (multiple * rho - 1 - 3 * s) % 4
    total = Fraction(0)
    for k in range(residue, numerator_exponent + 1, 4):
        h_at_zero = Fraction(-1 - 3 * s - k, 4)
        total += (
            (-1) ** k
            * comb(numerator_exponent, k)
            * generalized_binomial(order + h_at_zero, order)
        )
    return total


@lru_cache(maxsize=None)
def determinant_constant(s: int, rho: int) -> Fraction:
    z1 = branch_coefficient_constant(s, rho, 1, True)
    z2 = branch_coefficient_constant(s, rho, 2, True)
    w1 = branch_coefficient_constant(s, rho, 1, False)
    w2 = branch_coefficient_constant(s, rho, 2, False)
    return z1 * w2 - z2 * w1


def generalized_binomial_mod(
    numerator_over_four: int, n: int, modulus: int
) -> int:
    value = 1
    inverse_four = pow(4, -1, modulus)
    for j in range(n):
        value = value * ((numerator_over_four - 4 * j) % modulus) % modulus
        value = value * inverse_four % modulus
        value = value * pow(j + 1, -1, modulus) % modulus
    return value


def branch_coefficient_constant_mod(
    s: int, rho: int, multiple: int, z_series: bool, modulus: int
) -> int:
    numerator_exponent = 5 * s + (1 if z_series else 2)
    order = 2 * s + (0 if z_series else 1)
    residue = (multiple * rho - 1 - 3 * s) % 4
    inverses = [0, 1]
    for j in range(2, numerator_exponent + 1):
        inverses.append((modulus - (modulus // j) * inverses[modulus % j]) % modulus)
    binomials = [1]
    for k in range(numerator_exponent):
        binomials.append(
            binomials[-1]
            * (numerator_exponent - k)
            % modulus
            * inverses[k + 1]
            % modulus
        )
    first_top_numerator = 4 * order - 1 - 3 * s - residue
    generalized = generalized_binomial_mod(first_top_numerator, order, modulus)
    x = first_top_numerator * pow(4, -1, modulus) % modulus
    total = 0
    for k in range(residue, numerator_exponent + 1, 4):
        term = binomials[k] * generalized % modulus
        total = (total + (-term if k % 2 else term)) % modulus
        # k -> k+4 sends x -> x-1.
        generalized = generalized * ((x - order) % modulus) % modulus
        generalized = generalized * pow(x, -1, modulus) % modulus
        x = (x - 1) % modulus
    return total


def determinant_constant_mod(s: int, rho: int, modulus: int) -> int:
    z1 = branch_coefficient_constant_mod(s, rho, 1, True, modulus)
    z2 = branch_coefficient_constant_mod(s, rho, 2, True, modulus)
    w1 = branch_coefficient_constant_mod(s, rho, 1, False, modulus)
    w2 = branch_coefficient_constant_mod(s, rho, 2, False, modulus)
    return (z1 * w2 - z2 * w1) % modulus


def coefficient_mod(p: int, s: int, n: int, z_series: bool) -> int:
    numerator_exponent = 5 * s + (1 if z_series else 2)
    order = 2 * s + (0 if z_series else 1)
    target = n - 3 * s
    total = 0
    for k in range(numerator_exponent + 1):
        remainder = target - k
        if remainder < 0 or remainder % 4:
            continue
        h = remainder // 4
        term = comb(numerator_exponent, k) * comb(order + h, order)
        total = (total + (-term if k % 2 else term)) % p
    return total


def direct_determinant_mod(p: int, s: int) -> int:
    z1 = coefficient_mod(p, s, p - 1, True)
    z2 = coefficient_mod(p, s, 2 * p - 1, True)
    w1 = coefficient_mod(p, s, p - 1, False)
    w2 = coefficient_mod(p, s, 2 * p - 1, False)
    return (z1 * w2 - z2 * w1) % p


def ray_label(p: int, s: int) -> str:
    if p == 3 * s + 4:
        return "p=3s+4"
    if p == 5 * s + 2 and s % 4 == 1:
        return "p=5s+2,s=1(mod4)"
    if p == 5 * s + 1 and s % 4 == 2:
        return "p=5s+1,s=2(mod4)"
    return "sporadic"


def determinant_carry(
    left_1: list[int], right_0: list[int], left_0: list[int], right_1: list[int], p: int
) -> list[int]:
    width = len(left_1)
    carry = 0
    out = []
    for n in range(width):
        raw = sum(
            left_1[i] * right_0[n - i] - left_0[i] * right_1[n - i]
            for i in range(n + 1)
        )
        total = raw + carry
        digit = total % p
        carry = (total - digit) // p
        out.append(digit)
    return out


def digits_to_int(digits: list[int], p: int) -> int:
    return sum(value * p**i for i, value in enumerate(digits))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--exact-s-max", type=int, default=64)
    parser.add_argument("--modular-s-max", type=int, default=256)
    args = parser.parse_args()

    if not is_prime(AUXILIARY_PRIME):
        raise AssertionError("auxiliary modulus is not prime")
    if args.modular_s_max * 5 + 2 >= AUXILIARY_PRIME:
        raise ValueError("auxiliary characteristic is too small")

    probe_path = args.archive / "results" / "mixed_cubic_rank_two_cartier_probe_m500.json"
    deeper_path = args.archive / "results" / "item163_deeper_digits_certificate.json"

    exact_constants = []
    exact_nonzero = True
    exact_denominators_power_of_two = True
    exact_to_auxiliary_agreement = True
    exact_opposite_sign_equal_magnitude = True
    for s in range(args.exact_s_max + 1):
        c1 = determinant_constant(s, 1)
        c3 = determinant_constant(s, 3)
        exact_nonzero &= c1 != 0 and c3 != 0
        exact_denominators_power_of_two &= (
            c1.denominator & (c1.denominator - 1) == 0
            and c3.denominator & (c3.denominator - 1) == 0
        )
        exact_to_auxiliary_agreement &= (
            determinant_constant_mod(s, 1, AUXILIARY_PRIME)
            == c1.numerator * pow(c1.denominator, -1, AUXILIARY_PRIME) % AUXILIARY_PRIME
            and determinant_constant_mod(s, 3, AUXILIARY_PRIME)
            == c3.numerator * pow(c3.denominator, -1, AUXILIARY_PRIME) % AUXILIARY_PRIME
        )
        exact_opposite_sign_equal_magnitude &= c1 == -c3
        exact_constants.append(
            {
                "s": s,
                "C_s_1": [c1.numerator, c1.denominator],
                "C_s_3": [c3.numerator, c3.denominator],
                "opposite_sign_equal_magnitude": c1 == -c3,
            }
        )

    modular_witnesses = []
    modular_nonzero = True
    for s in range(args.modular_s_max + 1):
        c1 = determinant_constant_mod(s, 1, AUXILIARY_PRIME)
        c3 = determinant_constant_mod(s, 3, AUXILIARY_PRIME)
        modular_nonzero &= c1 != 0 and c3 != 0
        modular_witnesses.append({"s": s, "C_s_1_mod_q": c1, "C_s_3_mod_q": c3})

    isolated_witness_specs = ((73, 3), (347, 6), (79, 9), (509, 9), (233, 14), (112291, 4))
    isolated_witnesses = []
    for p, s in isolated_witness_specs:
        constant = determinant_constant(s, p % 4)
        j = 2 + (s % 2)
        m = (j * p + s) // 2
        isolated_witnesses.append(
            {
                "p": p,
                "s": s,
                "p_is_prime": is_prime(p),
                "large_p_hypothesis": p >= 8 * s + 3,
                "p_divides_constant_numerator": constant.numerator % p == 0,
                "direct_determinant_mod_p": direct_determinant_mod(p, s),
                "one_realizing_j": j,
                "one_realizing_m": m,
                "realizing_cell_checks": (
                    2 * m == j * p + s
                    and p < 2 * m
                    and p <= 4 * m + 1 < p * p
                ),
            }
        )

    direct_crosschecks = []
    direct_crosscheck_failures = []
    for p in primes_upto(401):
        if p < 5:
            continue
        for s in range(min(args.exact_s_max, (p - 1) // 3) + 1):
            if p < 8 * s + 3:
                continue
            direct = direct_determinant_mod(p, s)
            constant = determinant_constant(s, p % 4)
            predicted = constant.numerator * pow(constant.denominator, -1, p) % p
            row = {"p": p, "s": s, "direct": direct, "predicted": predicted}
            direct_crosschecks.append(row)
            if direct != predicted:
                direct_crosscheck_failures.append(row)

    probe = json.loads(probe_path.read_text(encoding="utf-8"))
    e1_rows = [
        row
        for row in probe["rows"]
        if int(row["p"]) ** 2 > 4 * int(row["m"]) + 1
    ]
    e1_zero_rows = [row for row in e1_rows if bool(row["vanishes"])]
    unique_pairs: dict[tuple[int, int], dict[str, object]] = {}
    thin_identity_failures = []
    fixed_formula_probe_failures = []
    for row in e1_rows:
        m = int(row["m"])
        p = int(row["p"])
        s = int(row["s"])
        if (2 * m - s) % p:
            thin_identity_failures.append({"m": m, "p": p, "s": s})
        if s <= args.exact_s_max and p >= 8 * s + 3:
            constant = determinant_constant(s, p % 4)
            predicted = constant.numerator * pow(constant.denominator, -1, p) % p
            if predicted != int(row["determinant"]):
                fixed_formula_probe_failures.append(
                    {"m": m, "p": p, "s": s, "direct": row["determinant"], "predicted": predicted}
                )
        if bool(row["vanishes"]):
            key = (p, s)
            if key not in unique_pairs:
                unique_pairs[key] = {"p": p, "s": s, "label": ray_label(p, s), "row_count": 0}
            unique_pairs[key]["row_count"] = int(unique_pairs[key]["row_count"]) + 1

    pair_label_counts = Counter(str(row["label"]) for row in unique_pairs.values())
    captured_fixed_s_pairs = []
    captured_modular_range_pairs = []
    for pair in unique_pairs.values():
        p = int(pair["p"])
        s = int(pair["s"])
        if s <= args.exact_s_max and p >= 8 * s + 3:
            constant = determinant_constant(s, p % 4)
            captured_fixed_s_pairs.append(
                {
                    **pair,
                    "p_divides_constant_numerator": constant.numerator % p == 0,
                }
            )
        if s <= args.modular_s_max and p >= 8 * s + 3:
            captured_modular_range_pairs.append(
                {
                    **pair,
                    "C_s_rho_mod_p": determinant_constant_mod(s, p % 4, p),
                }
            )
    if not all(row["p_divides_constant_numerator"] for row in captured_fixed_s_pairs):
        raise AssertionError("fixed-s zero classification failed")
    if not all(row["C_s_rho_mod_p"] == 0 for row in captured_modular_range_pairs):
        raise AssertionError("modular-range fixed-s zero classification failed")

    deeper = json.loads(deeper_path.read_text(encoding="utf-8"))
    rank_two_lifts = [row for row in deeper["rows"] if row["source"] == "rank_two_zero"]
    lift_layer_counts = {
        f"p^{layer}": sum(bool(row["gates"][f"p^{layer}"]) for row in rank_two_lifts)
        for layer in range(1, 6)
    }
    lift_survivors = []
    for row in rank_two_lifts:
        if int(row["actual_content_valuation"]) < 2:
            continue
        m = int(row["m"])
        p = int(row["p"])
        s = (2 * m) % p
        j = (2 * m - s) // p
        lift_survivors.append(
            {
                "m": m,
                "p": p,
                "j": j,
                "s": s,
                "valuation": int(row["actual_content_valuation"]),
                "A_digits": row["A_digits_after_forced_power"],
                "B_digits": row["B_digits_after_forced_power"],
            }
        )

    # Ambient lift-freedom theorem, exhaustively instantiated at p=5.
    ambient_lift_checks = 0
    ambient_lift_failures = []
    p = 5
    for a0 in range(p):
        for a1 in range(p):
            for b0 in range(p):
                t0 = (0, 1, 0)
                t1 = (-p * (a0 + p * a1), 1, -p * b0)
                minor_a = t1[1] * t0[0] - t0[1] * t1[0]
                minor_b = t1[1] * t0[2] - t0[1] * t1[2]
                ambient_lift_checks += 1
                if (
                    tuple(value % p for value in t0) != tuple(value % p for value in t1)
                    or (minor_a // p) % p != a0
                    or (minor_a // p**2) % p != a1
                    or (minor_b // p) % p != b0
                ):
                    ambient_lift_failures.append({"a0": a0, "a1": a1, "b0": b0})

    rng = random.Random(174)
    carry_checks = 0
    carry_failures = []
    for _ in range(2000):
        p = rng.choice((3, 5, 7, 11, 13, 17, 19, 23, 29, 31))
        width = 7
        arrays = [[rng.randrange(p) for _ in range(width)] for _ in range(4)]
        carried = determinant_carry(*arrays, p)
        modulus = p**width
        direct = (
            digits_to_int(arrays[0], p) * digits_to_int(arrays[1], p)
            - digits_to_int(arrays[2], p) * digits_to_int(arrays[3], p)
        ) % modulus
        carry_checks += 1
        if digits_to_int(carried, p) != direct:
            carry_failures.append({"p": p, "arrays": arrays})

    failures = {
        "exact_constants_zero": not exact_nonzero,
        "unexpected_exact_denominator": not exact_denominators_power_of_two,
        "modular_nonzero_witness_failed": not modular_nonzero,
        "exact_to_auxiliary_agreement": not exact_to_auxiliary_agreement,
        "exact_opposite_sign_equal_magnitude": not exact_opposite_sign_equal_magnitude,
        "isolated_fixed_s_witnesses": not all(
            row["p_is_prime"]
            and row["large_p_hypothesis"]
            and row["p_divides_constant_numerator"]
            and row["direct_determinant_mod_p"] == 0
            and row["realizing_cell_checks"]
            for row in isolated_witnesses
        ),
        "direct_quasipolynomial_crosschecks": direct_crosscheck_failures,
        "probe_quasipolynomial_crosschecks": fixed_formula_probe_failures,
        "cell_thin_identity": thin_identity_failures,
        "ambient_lift_freedom": ambient_lift_failures,
        "carry_recurrence": carry_failures,
    }
    failure_count = sum(bool(value) for value in failures.values())
    if failure_count:
        raise AssertionError({key: value for key, value in failures.items() if value})

    output = {
        "schema": "item174-ranktwo-nonscalar-v1",
        "status": {
            "rank_two_determinant_and_digit_gate": "PROVED",
            "fixed_s_quasipolynomial_reduction": "PROVED",
            "fixed_s_nonzero_range": f"PROVED_FOR_0_LE_S_LE_{args.modular_s_max}_BY_AUXILIARY_CHARACTERISTIC_WITNESS",
            "ambient_lift_freedom": "PROVED_AMBIENT_ONLY_NOT_AN_ACTUAL_MIXED_CUBIC_REALIZATION",
            "finite_lift_census": "EXPERIMENTAL_FINITE",
            "positive_mass_rank_two_family": "OPEN",
        },
        "inputs": {
            str(probe_path.relative_to(args.archive)): sha256(probe_path),
            str(deeper_path.relative_to(args.archive)): sha256(deeper_path),
        },
        "fixed_s": {
            "exact_s_max": args.exact_s_max,
            "modular_s_max": args.modular_s_max,
            "auxiliary_prime": AUXILIARY_PRIME,
            "auxiliary_prime_check": True,
            "all_exact_constants_nonzero": exact_nonzero,
            "all_exact_denominators_are_powers_of_two": exact_denominators_power_of_two,
            "all_modular_witnesses_nonzero": modular_nonzero,
            "all_exact_constants_agree_with_auxiliary_reduction": exact_to_auxiliary_agreement,
            "all_exact_constants_have_C_s_3_equals_minus_C_s_1": exact_opposite_sign_equal_magnitude,
            "exact_constants": exact_constants,
            "modular_witnesses": modular_witnesses,
            "direct_formula_crosscheck_count": len(direct_crosschecks),
            "direct_formula_crosscheck_failures": 0,
            "isolated_fixed_s_zero_witnesses": isolated_witnesses,
        },
        "archived_probe": {
            "e1_row_count": len(e1_rows),
            "e1_zero_row_count_with_repetition_in_j": len(e1_zero_rows),
            "unique_zero_pair_count": len(unique_pairs),
            "unique_zero_pairs_by_label": dict(sorted(pair_label_counts.items())),
            "captured_fixed_s_large_p_pair_count": len(captured_fixed_s_pairs),
            "captured_fixed_s_large_p_pairs": sorted(captured_fixed_s_pairs, key=lambda row: (row["p"], row["s"])),
            "captured_modular_range_large_p_pair_count": len(captured_modular_range_pairs),
            "captured_modular_range_large_p_pairs": sorted(captured_modular_range_pairs, key=lambda row: (row["p"], row["s"])),
            "all_cell_identities_2m_equals_jp_plus_s_hold": True,
            "all_available_fixed_s_formulas_agree": True,
            "sporadic_pairs": sorted(
                [row for row in unique_pairs.values() if row["label"] == "sporadic"],
                key=lambda row: (row["p"], row["s"]),
            ),
        },
        "scalar_free_lifts": {
            "rank_two_zero_rows_m_le_100": len(rank_two_lifts),
            "finite_layer_survival_counts": lift_layer_counts,
            "p2_survivors": lift_survivors,
            "ambient_surjectivity_checks_at_p5": ambient_lift_checks,
            "ambient_surjectivity_failures": 0,
            "random_carry_checks": carry_checks,
            "random_carry_failures": 0,
        },
        "failure_count": failure_count,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "failure_count": failure_count,
                "fixed_s_nonzero_through": args.modular_s_max,
                "e1_zero_rows": len(e1_zero_rows),
                "unique_zero_pairs": len(unique_pairs),
                "rank_two_lift_counts": lift_layer_counts,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
