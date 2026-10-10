#!/usr/bin/env python3
"""Deterministic certificate for Item 359.

The checker replays the fixed-M selector, the Fermat/Lagrange common-kernel
congruence on predeclared actual rows, the exact pole and degree data, and
the fixed rational comparison kernel.  It performs no prime scan or
collision census.  The all-parameter truncated-exponent, height, and
method-class proofs are in the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item359_j2_fixedM_cross_prime_coefficient_barrier_certificate.json"


# Item 355 pins are replaced with the final canonical root-audited hashes
# before the Item 359 manifest is frozen.
DEPENDENCIES = {
    "sources/item314_j2_two_branch_gate_report.md":
        "266f70523770a2a4147ee75289885fcb8dc945a65b650f2c8411e005ba110faa",
    "scripts/item314_j2_two_branch_gate_certificate.py":
        "cc5f155e5f3248c500cd2101e401c25cec37ce43b31fbb4582843fc33a9b2f0e",
    "results/item314_j2_two_branch_gate_certificate.json":
        "77de2dd46726a5a48e9adc4e40f96341d5da6c8db304d79f0ef8eeb7807245b1",
    "manifests/item314_j2_two_branch_gate_manifest.json":
        "ad5c5435aa169c4fb3e235a1293975f191cee27b1e56ed439988c6b43eac5e14",
    "sources/item352_j2_nonsemisimple_transition_no_go_report.md":
        "c60e1ba7771314c77b3fbe5d06f9c13c51a8c7e4d15f2589298641ff0f38e794",
    "results/item352_j2_nonsemisimple_transition_no_go_certificate.json":
        "8f06da2f8b4265156d02d2da393c0aedb74db55db3649589163866ffd0badc31",
    "results/item352_j2_nonsemisimple_transition_no_go_root_audit.json":
        "6acd46c106c21a963e0476e49d25c71305682c061e1df507ac8e332f4433d609",
    "manifests/item352_j2_nonsemisimple_transition_no_go_manifest.json":
        "c970d5b2dec42ec47f40078b49219cbac99e871b464a54f95be352729347ce54",
    "sources/item355_j2_target_residual_large_sieve_obstruction_report.md":
        "ea2f5f43a14a411849bc310409939891bfb496b681b028c20fcb3b990dd3377b",
    "results/item355_j2_target_residual_large_sieve_obstruction_certificate.json":
        "e246cfcec626d662d970a5a7a63da38914e9e0c98225e35f3ec7f80f5a30d3f2",
    "results/item355_j2_target_residual_large_sieve_obstruction_root_audit.json":
        "40bea19e6d09e7bbdd3945d9fc6e8a1f95c1cd8b5f906f5b6e2a57fea3924175",
    "manifests/item355_j2_target_residual_large_sieve_obstruction_manifest.json":
        "fa7554389223e4fa96f6e58c2766abacc4ad3c7e56df4c68a74d2f440ea8aaff",
}


def default_output() -> Path:
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        if expected.startswith("__"):
            raise AssertionError((relative, "unresolved dependency placeholder"))
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def poly_mul(left: list[int], right: list[int], limit: int, prime: int) -> list[int]:
    out = [0] * (min(limit, len(left) + len(right) - 2) + 1)
    for i, x in enumerate(left):
        if i > limit:
            break
        for j, y in enumerate(right):
            degree = i + j
            if degree > limit:
                break
            out[degree] = (out[degree] + x * y) % prime
    return out


def poly_pow(base: list[int], exponent: int, limit: int, prime: int) -> list[int]:
    result = [1]
    power = [value % prime for value in base[: limit + 1]]
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = poly_mul(result, power, limit, prime)
        remaining >>= 1
        if remaining:
            power = poly_mul(power, power, limit, prime)
    return result + [0] * (limit + 1 - len(result))


def inverse_series(denominator: list[int], limit: int, prime: int) -> list[int]:
    if denominator[0] % prime == 0:
        raise ZeroDivisionError((denominator[0], prime))
    inverse_constant = pow(denominator[0] % prime, -1, prime)
    out = [inverse_constant]
    for degree in range(1, limit + 1):
        total = 0
        for index in range(1, min(degree, len(denominator) - 1) + 1):
            total += denominator[index] * out[degree - index]
        out.append((-inverse_constant * total) % prime)
    return out


def rational_series(
    numerator: list[int], denominator: list[int], limit: int, prime: int
) -> list[int]:
    inverse = inverse_series(denominator, limit, prime)
    return poly_mul([x % prime for x in numerator], inverse, limit, prime)


def negative_binomial_series(exponent: int, sign: int, limit: int, prime: int) -> list[int]:
    """Coefficients of (1-sign*x)^(-exponent), through degree < p."""
    out = [1]
    for degree in range(1, limit + 1):
        value = out[-1] * (exponent + degree - 1) % prime
        value = value * pow(degree, -1, prime) % prime
        value = value * sign % prime
        out.append(value)
    return out


def kernel_coefficient_mod(prime: int, fixed_M: int, degree: int) -> int:
    if not (0 <= degree < prime):
        raise AssertionError((prime, fixed_M, degree, "truncation range"))
    inv_two = pow(2, -1, prime)

    p_minus = [45, -33, -42, 278, -199, 55, 16]
    p_plus = [120, 292, 388, 352, 316, 151, 16]
    n_minus = poly_mul(poly_mul([1, 1], [1, 0, 1], 9, prime), p_minus, 9, prime)
    n_plus = poly_mul(poly_mul([2, 1], [2, 2, 1], 9, prime), p_plus, 9, prime)
    e_minus_four = poly_pow([-3, 6, 1, 2], 4, 12, prime)
    e_plus_four = poly_pow([6, 14, 7, 2], 4, 12, prime)
    r_minus = rational_series(n_minus, e_minus_four, degree, prime)
    r_plus = rational_series(n_plus, e_plus_four, degree, prime)

    minus_numerator = poly_pow([1, 0, 1], 4 * fixed_M, degree, prime)
    minus_denominator = negative_binomial_series(6 * fixed_M, 1, degree, prime)
    u_minus = poly_mul(minus_numerator, minus_denominator, degree, prime)

    plus_numerator = poly_pow([1, 1, inv_two], 4 * fixed_M, degree, prime)
    plus_denominator = negative_binomial_series(6 * fixed_M, -1, degree, prime)
    u_plus = poly_mul(plus_numerator, plus_denominator, degree, prime)

    first = sum(r_minus[j] * u_minus[degree - j] for j in range(degree + 1))
    second = sum(r_plus[j] * u_plus[degree - j] for j in range(degree + 1))
    return (18 * first + 11 * pow(16, fixed_M - 1, prime) * second) % prime


DECLARED_ROWS = [
    # prime, r, s, M, Item355 Delta_1, Item355 Delta_2
    (11, 1, 1, 13, 4, 9),
    (17, 1, 2, 20, 12, 5),
    (29, 1, 4, 34, 4, 17),
    (271, 113, 7, 335, 0, 172),
    (367, 65, 39, 439, 0, 197),
    (383, 109, 27, 465, 0, 316),
    (599, 7, 97, 700, 275, 551),
]


def selector_kernel_replay() -> dict[str, Any]:
    item314 = load("item359_i314", "scripts/item314_j2_two_branch_gate_certificate.py")
    minus, plus = item314.exact_branch_values(max(row[1] for row in DECLARED_ROWS))
    rows = []
    for prime, r, s, fixed_M, delta_one, delta_two in DECLARED_ROWS:
        if prime != 2 * r + 6 * s + 3:
            raise AssertionError((prime, r, s, "tied prime"))
        if 2 * fixed_M != 5 * r + 14 * s + 7:
            raise AssertionError((prime, r, s, fixed_M, "fixed M"))
        selected_r = 6 * fixed_M - 7 * prime
        selected_s_numerator = 5 * prime - 4 * fixed_M - 1
        if selected_s_numerator % 2:
            raise AssertionError((prime, fixed_M, "selector parity"))
        selected_s = selected_s_numerator // 2
        if (selected_r, selected_s) != (r, s):
            raise AssertionError((prime, r, s, selected_r, selected_s, "selector"))
        degree = r - 1
        if not (0 <= degree < prime):
            raise AssertionError((prime, degree, "degree range"))
        fermat_state = pow(4, s, prime)
        fixed_state = pow(16, 1 - fixed_M, prime)
        if fermat_state != fixed_state:
            raise AssertionError((prime, fixed_M, fermat_state, fixed_state, "Fermat"))

        a_value = minus[r]
        b_value = plus[r]
        gate = 18 * F(4**s) * a_value + 11 * b_value
        gate_mod = fmod(gate, prime)
        c_star = -11 * b_value / (18 * a_value)
        calculated_delta_one = (fermat_state - fmod(c_star, prime)) % prime
        if calculated_delta_one != delta_one:
            raise AssertionError((prime, calculated_delta_one, delta_one, "Item355 Delta1"))

        kernel_mod = kernel_coefficient_mod(prime, fixed_M, degree)
        left = pow(16, fixed_M - 1, prime) * r * gate_mod % prime
        right = -12 * kernel_mod % prime
        if left != right:
            raise AssertionError((prime, r, s, fixed_M, left, right, "kernel bridge"))
        if (gate_mod == 0) != (kernel_mod == 0):
            raise AssertionError((prime, gate_mod, kernel_mod, "zero equivalence"))
        rows.append(
            (
                prime,
                r,
                s,
                fixed_M,
                degree,
                fermat_state,
                gate_mod,
                kernel_mod,
                left,
                right,
                delta_one,
                delta_two,
            )
        )
    return {
        "classification": "EXACT FINITE REPLAY ONLY - NO PRIME OR COLLISION CENSUS",
        "declared_rows": len(rows),
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
    }


def comparison_coefficient(fixed_M: int, degree: int) -> int:
    value = 0
    if degree >= 4 and (degree - 4) % 6 == 0:
        b = (degree - 4) // 6
        remainder = fixed_M - b - 2
        if remainder >= 0 and remainder % 7 == 0:
            a = remainder // 7
            value += 6 * a + 1
    if degree >= 0 and degree % 6 == 0:
        b = degree // 6
        remainder = fixed_M - b - 6
        if remainder >= 0 and remainder % 7 == 0:
            a = remainder // 7
            value += 6 * a + 5
    return value


def comparison_kernel_replay() -> dict[str, Any]:
    rows = []
    for a in range(6):
        for b in range(8):
            p_one = 6 * a + 1
            r_one = 6 * b + 5
            M_one = b + 7 * a + 2
            coefficient_one = comparison_coefficient(M_one, r_one - 1)
            if coefficient_one != p_one or 6 * M_one != r_one + 7 * p_one:
                raise AssertionError((a, b, "one ray"))
            rows.append((1, a, b, p_one, r_one, M_one, coefficient_one))

            p_five = 6 * a + 5
            r_five = 6 * b + 1
            M_five = b + 7 * a + 6
            coefficient_five = comparison_coefficient(M_five, r_five - 1)
            if coefficient_five != p_five or 6 * M_five != r_five + 7 * p_five:
                raise AssertionError((a, b, "five ray"))
            rows.append((5, a, b, p_five, r_five, M_five, coefficient_five))
    return {
        "classification": "EXACT FINITE COEFFICIENT REPLAY OF AN ALL-PARAMETER RATIONAL IDENTITY",
        "declared_parameter_pairs": 48,
        "declared_ray_rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
        "generating_function": (
            "(X^4*Y^2*(1+5Y^7)+Y^6*(5+Y^7))/"
            "((1-X^6Y)*(1-Y^7)^2)"
        ),
    }


def pole_and_degree_replay() -> dict[str, Any]:
    p_minus_at_one = 16 + 55 - 199 + 278 - 42 - 33 + 45
    p_plus_at_minus_one = 16 - 151 + 316 - 352 + 388 - 292 + 120
    if p_minus_at_one != 120 or p_plus_at_minus_one != 45:
        raise AssertionError((p_minus_at_one, p_plus_at_minus_one))
    r_minus_numerator_at_one = 2 * 2 * p_minus_at_one
    e_minus_at_one = 2 + 1 + 6 - 3
    r_plus_numerator_at_minus_one = 1 * 1 * p_plus_at_minus_one
    e_plus_at_minus_one = -2 + 7 - 14 + 6
    q_at_minus_one = F(1) - 1 + F(1, 2)
    if (
        r_minus_numerator_at_one != 480
        or e_minus_at_one != 6
        or r_plus_numerator_at_minus_one != 45
        or e_plus_at_minus_one != -3
        or q_at_minus_one != F(1, 2)
    ):
        raise AssertionError("pole evaluations")

    degree_rows = []
    for fixed_M in (1, 2, 13, 335, 700):
        common_denominator_degree = 12 * fixed_M + 24
        common_numerator_degree = 14 * fixed_M + 21
        pole_degree_lower_bound = 12 * fixed_M
        infinity_degree = 2 * fixed_M - 3
        infinity_leading_coefficient = F(299, 16)
        if common_numerator_degree - common_denominator_degree != infinity_degree:
            raise AssertionError((fixed_M, "degree at infinity"))
        degree_rows.append(
            (
                fixed_M,
                common_denominator_degree,
                common_numerator_degree,
                pole_degree_lower_bound,
                infinity_degree,
                infinity_leading_coefficient.numerator,
                infinity_leading_coefficient.denominator,
            )
        )
    return {
        "classification": "SYMBOLIC EXACT POLE EVALUATIONS AND AFFINE DEGREE FORMULAS",
        "pole_at_1": "exact order 6M",
        "pole_at_minus_1": "exact order 6M",
        "minimal_eventual_recurrence_order_lower_bound": "12M",
        "degree_rows": degree_rows,
        "degree_digest_sha256": digest_rows(degree_rows),
    }


def capacity_replay() -> dict[str, Any]:
    raw = F(6, 7) - F(4, 5)
    normalized = raw / 6
    if raw != F(2, 35) or normalized != F(1, 105):
        raise AssertionError((raw, normalized))
    selector_rows = []
    for prime, r, s, fixed_M, *_ in DECLARED_ROWS:
        lower_num = 4 * fixed_M + 3
        upper_num = 6 * fixed_M - 1
        if not (5 * prime >= lower_num and 7 * prime <= upper_num):
            raise AssertionError((prime, fixed_M, "raw interval"))
        max_degree_numerator = 2 * fixed_M - 26
        if 5 * (r - 1) > max_degree_numerator:
            raise AssertionError((prime, fixed_M, r, "selected degree window"))
        selector_rows.append((prime, fixed_M, r - 1, max_degree_numerator))
    return {
        "classification": "EXACT RATIONAL CAPACITY AND SELECTOR-WINDOW NORMALIZATION",
        "raw_chebyshev_coefficient": "2/35",
        "per_6M_capacity": "1/105",
        "selector_window": "0 <= k <= (2M-26)/5",
        "row_digest_sha256": digest_rows(selector_rows),
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    return {
        "schema": "item359-j2-fixedM-cross-prime-coefficient-barrier-v1",
        "classification": "PROVED_FIXED_M_CROSS_PRIME_COEFFICIENT_BRIDGE_AND_SELECTOR_BARRIER",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "selector": "r=6M-7p, s=(5p-4M-1)/2, k=6M-7p-1",
            "Fermat_collapse": "4^s=16^(1-M) mod p",
            "kernel_bridge": "16^(M-1)*r*G_(r,s)=-12*[X^(r-1)]K_M(X) mod p",
            "bivariate_kernel": (
                "sum_(M>=1) K_M(X)Y^M=18R_-*YU_-/(1-YU_-)+"
                "11R_+*YU_+/(1-16YU_+)"
            ),
            "pole_order": "ord_(X=1)=ord_(X=-1)=6M, recurrence order >=12M",
            "comparison_kernel": (
                "V=(X^4Y^2(1+5Y^7)+Y^6(5+Y^7))/"
                "((1-X^6Y)(1-Y^7)^2)"
            ),
            "comparison_selector": "[X^(r-1)Y^M]V=p whenever 6M=r+7p on the two prime rays",
        },
        "selector_kernel_replay": selector_kernel_replay(),
        "pole_and_degree_replay": pole_and_degree_replay(),
        "comparison_kernel_replay": comparison_kernel_replay(),
        "capacity_replay": capacity_replay(),
        "capacity": {
            "raw_fixed_M_chebyshev_mass": "(2/35)M+o(M)",
            "ordinary_j2_ceiling_per_6M": "1/105",
            "chart_overlap": "nondegenerate and degenerate charts partition one raw interval and are not additive",
            "new_booking": 0,
            "new_capacity_reduction": 0,
        },
        "strict_labels": {
            "proved": [
                "fixed-M selector and Fermat collapse",
                "common fixed-M and bivariate rational coefficient bridges",
                "exact linear pole/recurrence obstruction",
                "fixed rational full-selector-mass comparison kernel",
                "height-scale, capacity, and chart-overlap audits",
            ],
            "finite_only": [
                "seven predeclared actual rows",
                "forty-eight declared parameter pairs on each of two comparison rays",
                "no prime scan and no collision census",
            ],
            "open": [
                "matched-modulus divisibility nonconcentration for the actual coefficient diagonal",
                "joint cross-prime theorem retaining H_(s-1)-Theta_(r,s)",
                "selector-aware average gcd or reciprocity law",
                "almost-all-M energy saving admissible in the main construction",
            ],
        },
        "scope_warning": (
            "The comparison rational kernel proves insufficiency of rationality, holonomicity, "
            "and pointwise height as metadata. It is not the actual determinant kernel."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
