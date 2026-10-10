#!/usr/bin/env python3
"""Deterministic certificate for Item 247's j=2 bulk-pair eliminant.

The checker verifies the exact parity/derivative elimination, its unit
determinant on the regular actual locus, the singular r=1 specialization,
and the common-denominator content criterion.  Every scan is labelled finite.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item247_j2_bulk_pair_eliminant_certificate.json"
ITEM246_SHA256 = "5aaa0dd5e19d4ceefe3380b374b41ce3c172b5a041ff36b101f30cb72eb4e6ed"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


ITEM246_PATH = resolve("item246_j2_bulk_residual_structure_certificate.py")
if sha256(ITEM246_PATH) != ITEM246_SHA256:
    raise RuntimeError("Item246 checker hash mismatch")
item246 = load("item247_item246", ITEM246_PATH)
item239 = item246.item239


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def poly_mul(left: tuple[int, ...], right: tuple[int, ...], p: int) -> tuple[int, ...]:
    if not left or not right:
        return ()
    return item239.convolution_mod(left, right, p)


def poly_derivative(polynomial: tuple[int, ...], p: int) -> tuple[int, ...]:
    if len(polynomial) <= 1:
        return ()
    return item246.trim(tuple(k * polynomial[k] % p for k in range(1, len(polynomial))))


def parity_seeds(p: int, gap: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    even = tuple(math.comb(gap, 2 * j) % p for j in range(gap // 2 + 1))
    odd = tuple(
        math.comb(gap, 2 * j + 1) % p
        for j in range((gap - 1) // 2 + 1)
    ) if gap else ()
    return item246.trim(even), item246.trim(odd)


def actual_pair_data(p: int, s: int) -> dict[str, Any]:
    r = (p - 6 * s - 3) // 2
    if r < 1 or r % 2 != 1:
        raise AssertionError((p, s, r, "actual rows force positive odd r"))
    if r == 3:
        raise AssertionError((p, s, "r=3 would make p composite"))
    lower = (r + 1) // 2
    gap = r - 1
    even, odd = parity_seeds(p, gap)
    plus = item239.power_mod((1, 1), 2 * s - 1, p)
    common = item246.poly_linear(plus, -1, p)
    selected = item246.poly_scale(poly_mul(common, odd, p), -1, p)
    companion = poly_mul(common, even, p)

    _, direct_lower_0, direct_0 = item246.actual_projected(p, s, 0)
    _, direct_lower_1, direct_1 = item246.actual_projected(p, s, 1)
    if direct_lower_0 != lower or direct_lower_1 != lower:
        raise AssertionError((p, s, "lower-index mismatch"))

    predicted_0 = item246.poly_linear(selected, 1, p)
    predicted_1 = item246.poly_add(
        poly_mul((1, 3), selected, p),
        poly_mul((3, 1), companion, p),
        p,
    )
    if direct_0 != predicted_0 or direct_1 != predicted_1:
        raise AssertionError((p, s, "nu-pair decomposition"))

    bulk_0 = item246.functional_mod(p, lower, direct_0)[0]
    bulk_1 = item246.functional_mod(p, lower, direct_1)[0]
    x = item246.functional_mod(p, lower, selected)[0]
    y = item246.functional_mod(p, lower, item246.poly_shift(selected, 1))[0]
    z_polynomial = poly_mul((3, 1), companion, p)
    z = item246.functional_mod(p, lower, z_polynomial)[0]
    if bulk_0 != (x + y) % p or bulk_1 != (x + 3 * y + z) % p:
        raise AssertionError((p, s, "unit 2x2 common-state matrix"))

    eliminated_polynomial = poly_mul(
        common,
        item246.poly_add(poly_mul((3, 1), even, p), item246.poly_scale(odd, 2, p), p),
        p,
    )
    eliminated = item246.functional_mod(p, lower, eliminated_polynomial)[0]
    if eliminated != (bulk_1 - 3 * bulk_0) % p:
        raise AssertionError((p, s, "companion eliminant"))

    differential_ok = 0
    singular_ok = 0
    combined_determinant = 0
    if gap:
        odd_prime = poly_derivative(odd, p)
        ode_right = item246.poly_add(
            poly_mul((1, gap - 1), odd, p),
            item246.poly_scale(poly_mul((0, 1, -1), odd_prime, p), 2, p),
            p,
        )
        if item246.poly_scale(even, gap, p) != ode_right:
            raise AssertionError((p, s, "parity derivative identity"))

        d1_seed = item246.poly_add(
            poly_mul((3 - gap, -2, gap - 1), odd, p),
            item246.poly_scale(poly_mul((0, 3, -2, -1), odd_prime, p), 2, p),
            p,
        )
        predicted_d1_from_one_seed = poly_mul(common, d1_seed, p)
        if item246.poly_scale(direct_1, gap, p) != predicted_d1_from_one_seed:
            raise AssertionError((p, s, "one-seed D1 identity"))

        eliminated_seed = item246.poly_add(
            poly_mul((2 * gap + 3, 3 * gap - 2, gap - 1), odd, p),
            item246.poly_scale(poly_mul((0, 3, -2, -1), odd_prime, p), 2, p),
            p,
        )
        differential_eliminated = item246.functional_mod(
            p, lower, poly_mul(common, eliminated_seed, p)
        )[0]
        if differential_eliminated != gap * eliminated % p:
            raise AssertionError((p, s, "one-seed functional eliminant"))
        combined_determinant = 2 * gap % p
        if combined_determinant == 0:
            raise AssertionError((p, s, "regular determinant must be a unit"))
        differential_ok = 1
    else:
        expected_singular_0: tuple[int, ...] = ()
        expected_singular_1 = poly_mul(common, (3, 1), p)
        if direct_0 != expected_singular_0 or direct_1 != expected_singular_1:
            raise AssertionError((p, s, "singular r=1 specialization"))
        if eliminated != bulk_1:
            raise AssertionError((p, s, "singular eliminant"))
        singular_ok = 1

    return {
        "r": r,
        "lower": lower,
        "degree_0": len(direct_0) - 1,
        "degree_1": len(direct_1) - 1,
        "bulk_0": bulk_0,
        "bulk_1": bulk_1,
        "eliminated": eliminated,
        "differential_ok": differential_ok,
        "singular_ok": singular_ok,
        "combined_determinant": combined_determinant,
    }


def common_denominator_content(p: int, s: int) -> tuple[int, ...]:
    lower_0, polynomial_0 = item246.exact_integer_projected(p, s, 0)
    lower_1, polynomial_1 = item246.exact_integer_projected(p, s, 1)
    if lower_0 != lower_1:
        raise AssertionError((p, s, "exact lower mismatch"))
    lower = lower_0
    degree = max(len(polynomial_0), len(polynomial_1)) - 1
    if degree != lower + 2 * s:
        raise AssertionError((p, s, degree, "degree formula"))
    if 2 * (lower + degree) + 1 >= p:
        raise AssertionError((p, s, degree, "denominator range"))
    common_denominator = math.prod(2 * (lower + k) + 1 for k in range(degree + 1))
    if common_denominator % p == 0:
        raise AssertionError((p, s, "common denominator is not a p-unit"))
    bulk_0 = item246.functional_fraction(lower, polynomial_0)[0]
    bulk_1 = item246.functional_fraction(lower, polynomial_1)[0]
    integer_0 = bulk_0 * common_denominator * common_denominator
    integer_1 = bulk_1 * common_denominator * common_denominator
    if integer_0.denominator != 1 or integer_1.denominator != 1:
        raise AssertionError((p, s, "cleared functional not integral"))
    content = math.gcd(abs(integer_0.numerator), abs(integer_1.numerator))
    modular_0 = (
        bulk_0.numerator % p * pow(bulk_0.denominator % p, -1, p) % p
    )
    modular_1 = (
        bulk_1.numerator % p * pow(bulk_1.denominator % p, -1, p) % p
    )
    if (content % p == 0) != (modular_0 == 0 and modular_1 == 0):
        raise AssertionError((p, s, "content criterion"))
    return (
        p,
        s,
        lower,
        degree,
        common_denominator % p,
        integer_0.numerator % p,
        integer_1.numerator % p,
        content % p,
        modular_0,
        modular_1,
    )


def rational_replay(bound: int) -> dict[str, Any]:
    rows = [common_denominator_content(p, s) for p, s in item239.admissible_rows(bound)]
    return {
        "status": "EXACT FINITE RATIONAL REPLAY",
        "prime_max_inclusive": bound,
        "row_count": len(rows),
        "content_divisible_by_moving_prime_count": sum(row[7] == 0 for row in rows),
        "row_digest_sha256": row_digest(rows),
    }


def finite_census(bound: int) -> dict[str, Any]:
    digest_rows: list[tuple[int, ...]] = []
    separate_zero_rows: list[dict[str, int]] = []
    simultaneous_zero_rows: list[dict[str, int]] = []
    eliminated_zero_rows: list[dict[str, int]] = []
    row_count = 0
    regular_count = 0
    singular_count = 0
    eliminated_zero_count = 0
    for p, s in item239.admissible_rows(bound):
        row_count += 1
        data = actual_pair_data(p, s)
        regular_count += data["differential_ok"]
        singular_count += data["singular_ok"]
        eliminated_zero_count += data["eliminated"] == 0
        if data["eliminated"] == 0:
            eliminated_zero_rows.append({"p": p, "s": s})
        for nu, value in enumerate((data["bulk_0"], data["bulk_1"])):
            if value == 0 and data[f"degree_{nu}"] >= 0:
                separate_zero_rows.append({"p": p, "s": s, "nu": nu})
        if data["bulk_0"] == 0 and data["bulk_1"] == 0:
            simultaneous_zero_rows.append({"p": p, "s": s})
        digest_rows.append(
            (
                p,
                s,
                data["r"],
                data["lower"],
                data["degree_0"],
                data["degree_1"],
                data["bulk_0"],
                data["bulk_1"],
                data["eliminated"],
                data["combined_determinant"],
            )
        )
    return {
        "status": "EXACT FINITE ONLY",
        "prime_max_inclusive": bound,
        "admissible_row_count": row_count,
        "regular_r_greater_than_1_count": regular_count,
        "singular_r_equals_1_count": singular_count,
        "separate_nonempty_bulk_zero_count": len(separate_zero_rows),
        "separate_nonempty_bulk_zero_rows": separate_zero_rows,
        "eliminated_residual_zero_count": eliminated_zero_count,
        "eliminated_residual_zero_rows": eliminated_zero_rows,
        "simultaneous_bulk_zero_count": len(simultaneous_zero_rows),
        "simultaneous_bulk_zero_rows": simultaneous_zero_rows,
        "row_digest_sha256": row_digest(digest_rows),
    }


def prime_sieve(bound: int) -> bytearray:
    sieve = bytearray(b"\x01") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for divisor in range(2, math.isqrt(bound) + 1):
        if sieve[divisor]:
            start = divisor * divisor
            sieve[start : bound + 1 : divisor] = b"\x00" * (
                (bound - start) // divisor + 1
            )
    return sieve


def singular_polynomial(p: int, s: int) -> tuple[int, ...]:
    exponent = 2 * s - 1
    binomial = [1]
    for k in range(exponent):
        binomial.append(
            binomial[-1] * (exponent - k) * pow(k + 1, -1, p) % p
        )
    result = []
    for k in range(exponent + 3):
        result.append(
            (
                3 * (binomial[k] if k <= exponent else 0)
                - 2 * (binomial[k - 1] if 0 <= k - 1 <= exponent else 0)
                - (binomial[k - 2] if 0 <= k - 2 <= exponent else 0)
            )
            % p
        )
    return item246.trim(result)


def singular_locus_scan(bound: int) -> dict[str, Any]:
    sieve = prime_sieve(bound)
    rows: list[tuple[int, ...]] = []
    zero_rows: list[dict[str, int]] = []
    for s in range(2, (bound - 5) // 6 + 1):
        p = 6 * s + 5
        if not sieve[p]:
            continue
        if not (
            p >= 17
            and s >= 2
            and s <= (p - 3) // 6
            and (5 * p - 2 * s - 1) % 4 == 0
            and (p - 6 * s - 3) // 2 == 1
        ):
            raise AssertionError((p, s, "singular-row admissibility"))
        polynomial = singular_polynomial(p, s)
        bulk, sine = item246.functional_mod(p, 1, polynomial)
        if bulk == 0:
            zero_rows.append({"p": p, "s": s})
        rows.append((p, s, len(polynomial) - 1, bulk, sine))
    return {
        "status": "EXACT FINITE ONLY",
        "prime_max_inclusive": bound,
        "singular_row_count": len(rows),
        "bulk_1_zero_count": len(zero_rows),
        "bulk_1_zero_rows": zero_rows,
        "row_digest_sha256": row_digest(rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=401)
    parser.add_argument("--rational-prime-max", type=int, default=101)
    parser.add_argument("--singular-prime-max", type=int, default=20000)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if not (101 <= args.rational_prime_max <= args.prime_max):
        raise ValueError("require 101 <= rational-prime-max <= prime-max")
    if args.singular_prime_max < args.prime_max:
        raise ValueError("singular-prime-max must be at least prime-max")

    finite = finite_census(args.prime_max)
    rational = rational_replay(args.rational_prime_max)
    singular = singular_locus_scan(args.singular_prime_max)
    result = {
        "schema": "item247-j2-bulk-pair-eliminant-v1",
        "item": 247,
        "route": "Route 1A",
        "cell": "normalized common-log j=2 fixed cell, simultaneous canonical Item244 bulk residuals",
        "proved": {
            "actual_parity": "for r=(p-6s-3)/2 in the Item244 fixed j=2 parameterization, the admissibility congruence is equivalent to r odd; this r is unrelated to the separate j=1 branch parameter",
            "pair_normal_form": "with R=r-1, G=(1-t)(1+t)^(2s-1), and (1-z)^R=E(t)-zO(t), D0=-G(1+t)O and D1=G*((3-R-2t+(R-1)t^2)O+2t(1-t)(3+t)O')/R for R>0",
            "parity_derivative": "R E=(1+(R-1)t)O+2t(1-t)O'",
            "common_state_determinant": "(B0,B1-Z)^T=[[1,1],[1,3]](X,Y)^T with determinant 2, where X=B[A], Y=B[tA], Z=B[(3+t)C]",
            "eliminated_residual": "B1-3B0=B_L[G*((3+t)E+2O)]",
            "one_seed_eliminant": "R*(B1-3B0)=B_L[G*J_R(O)] with J_R(O)=(2R+3+(3R-2)t+(R-1)t^2)O+2t(1-t)(3+t)O'",
            "elimination_determinant": "the combined algebraic elimination determinant is 2R=2(r-1), a p-unit on every regular actual row",
            "singular_locus": "the exact elimination singular locus is r=1; there D0=0 and D1=(1-t)(1+t)^(2s-1)(3+t), and every prime p=6s+5 with s>=2 satisfies all original j=2 admissibility inequalities and congruences",
            "prime_exclusion": "r=3 produces p=3(2s+3), so every prime regular row has r>=5",
            "content_criterion": "if Q is the product of all odd denominators through deg D1 and I_nu=Q^2 B_nu, then I_nu are integers and simultaneous modular vanishing is equivalent to p dividing gcd(I0,I1)",
        },
        "finite_census": finite,
        "finite_rational_replay": rational,
        "finite_singular_locus_scan": singular,
        "scoped_consequence": {
            "proved": "the common A-state and companion parity admit an exact unit-determinant elimination on r>1, reducing simultaneous vanishing to two explicit functionals of the single odd seed O",
            "not_proved": "unit algebraic elimination does not imply that the two resulting scalar bulk functionals cannot vanish simultaneously",
            "open_arithmetic": "classify moving primes dividing the canonical common-denominator content gcd(I0,I1), including the singular r=1 family",
        },
        "status_ledger": {
            "PROVED": [
                "the all-row parity, derivative, pair, determinant, one-seed, singular-locus, and common-denominator content identities",
                "the combined determinant 2(r-1) is a p-unit on every regular actual row",
            ],
            "EXACT_FINITE": [
                "the bounded full-pair census, rational content replay, and extended singular-locus scan",
            ],
            "OPEN": [
                "prove or disprove all-prime simultaneous nonvanishing of the two scalar bulk functionals",
                "factor or control the moving-prime common-denominator content",
                "obtain any Route-1 rate or capacity reduction",
            ],
        },
        "global_interface": "the pair belongs only to the stronger Item239 p^3 carry and does not strengthen the ordinary p^2 common-log gate",
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "none",
        },
        "dependencies": {
            "item246_checker": ITEM246_PATH.name,
            "item246_checker_sha256": ITEM246_SHA256,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
