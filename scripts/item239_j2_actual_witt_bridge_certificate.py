#!/usr/bin/env python3
"""Deterministic certificate for Item 239's actual j=2 Witt bridge.

This checker expands the true integer quotient C_nu/p modulo p^2,
separates its lifted-linear and quadratic Frobenius terms, translates both
to a corrected beta-period kernel, and checks the result against direct
integer coefficient extraction.  Bounded censuses are explicitly finite.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item239_j2_actual_witt_bridge_certificate.json"


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


ITEM235_PATH = resolve("item235_j2_witt_terminal_certificate.py")
item235 = load("item239_item235", ITEM235_PATH)
item219 = item235.item219


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def convolution_mod(left: tuple[int, ...], right: tuple[int, ...], modulus: int) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right):
            if y:
                result[i + j] = (result[i + j] + x * y) % modulus
    return tuple(result)


def power_mod(base: tuple[int, ...], exponent: int, modulus: int) -> tuple[int, ...]:
    result = (1,)
    power = tuple(x % modulus for x in base)
    while exponent:
        if exponent & 1:
            result = convolution_mod(result, power, modulus)
        exponent //= 2
        if exponent:
            power = convolution_mod(power, power, modulus)
    return result


def p_polynomial(p: int, s: int, nu: int, modulus: int) -> tuple[int, tuple[int, ...]]:
    r = (p - 6 * s - 3) // 2
    result = convolution_mod(power_mod((1, -1), r, modulus), power_mod((1, 1), 1 + 3 * nu, modulus), modulus)
    result = convolution_mod(result, power_mod((1, 0, 1), 2 * s - nu, modulus), modulus)
    expected_degree = (p + 2 * s - 1) // 2 + nu
    if len(result) - 1 != expected_degree:
        raise AssertionError((p, s, nu, len(result) - 1, expected_degree))
    return r, result


def coefficient_product(left: tuple[int, ...], right: tuple[int, ...], target: int, modulus: int) -> int:
    low = max(0, target - len(right) + 1)
    high = min(len(left) - 1, target)
    if low > high:
        return 0
    return sum(left[k] * right[target - k] for k in range(low, high + 1)) % modulus


@functools.lru_cache(maxsize=None)
def harmonic_table(p: int) -> tuple[int, ...]:
    result = [0] * p
    for k in range(1, p):
        result[k] = (result[k - 1] + pow(k, -1, p)) % p
    if result[p - 1] != 0:
        raise AssertionError((p, "H_(p-1)"))
    return tuple(result)


@functools.lru_cache(maxsize=None)
def lifted_defects(p: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Exact binomial quotients, reduced modulo p^2."""
    modulus = p * p
    a = [0] * p
    b = [0] * (2 * p - 1)
    harmonics = harmonic_table(p)
    for k in range(1, p):
        quotient = math.comb(p, k) // p
        a[k] = ((-1) ** k * quotient) % modulus
        b[2 * k] = quotient % modulus
        inverse = pow(k, -1, modulus)
        expected_a = (-inverse * (1 - p * harmonics[k - 1])) % modulus
        expected_b = (
            (-1) ** (k - 1) * inverse * (1 - p * harmonics[k - 1])
        ) % modulus
        if a[k] != expected_a or b[2 * k] != expected_b:
            raise AssertionError((p, k, "binomial quotient digit"))
    return tuple(a), tuple(b)


@functools.lru_cache(maxsize=None)
def kernel_data(p: int) -> dict[str, tuple[int, ...]]:
    """Mod-p logarithms, quadratic convolutions, and endpoint carries."""
    a = [0] * p
    b = [0] * (2 * p - 1)
    for k in range(1, p):
        a[k] = -pow(k, -1, p) % p
        b[2 * k] = (-1) ** (k - 1) * pow(k, -1, p) % p
    a_tuple = tuple(a)
    b_tuple = tuple(b)
    aa = convolution_mod(a_tuple, a_tuple, p)
    bb = convolution_mod(b_tuple, b_tuple, p)
    ab = convolution_mod(a_tuple, b_tuple, p)
    harmonics = harmonic_table(p)
    chi = 1 if p % 4 == 1 else -1

    depth_one = [0] * p
    depth_two = [0] * p
    total = [0] * p

    def coefficient(polynomial: tuple[int, ...], degree: int) -> int:
        return polynomial[degree] if 0 <= degree < len(polynomial) else 0

    for n in range(1, p):
        c_weight = (2, 0, -2, 0)[n % 4]
        j_weight = (0, -2 * chi, 0, 2 * chi)[n % 4]
        inverse = pow(n, -1, p)
        value_one = -j_weight * inverse * inverse
        value_one -= 9 * harmonics[n - 1] * inverse
        if n % 2 == 0:
            value_one += 10 * c_weight * harmonics[n // 2 - 1] * inverse
        else:
            value_one -= (
                j_weight * harmonics[(p + n) // 2 - 1] * inverse
            )
        depth_one[n] = value_one % p

        value_two = 9 * coefficient(aa, p + n) - 18 * coefficient(aa, n)
        value_two -= 3 * coefficient(bb, 3 * p + n)
        value_two += 6 * coefficient(bb, 2 * p + n)
        value_two += 6 * coefficient(bb, p + n)
        value_two -= 36 * coefficient(bb, n)
        value_two -= 9 * coefficient(ab, 2 * p + n)
        value_two -= 16 * coefficient(ab, p + n)
        value_two += 54 * coefficient(ab, n)
        depth_two[n] = value_two % p
        total[n] = (depth_one[n] + depth_two[n]) % p

    return {
        "A": a_tuple,
        "B": b_tuple,
        "AA": aa,
        "BB": bb,
        "AB": ab,
        "depth_one": tuple(depth_one),
        "depth_two": tuple(depth_two),
        "total": tuple(total),
    }


def fixed_series_coefficients(a: int, c: int, maximum: int) -> list[int]:
    """Coefficients of (1-y)^a/(1+y^2)^c over the integers."""
    result = []
    for degree in range(maximum + 1):
        value = 0
        for b in range(degree // 2 + 1):
            k = degree - 2 * b
            if k <= a:
                value += (
                    (-1) ** k
                    * math.comb(a, k)
                    * (-1) ** b
                    * math.comb(c + b - 1, b)
                )
        result.append(value)
    return result


def verify_fixed_sections() -> dict[str, list[int]]:
    linear_a = fixed_series_coefficients(6, 5, 4)
    linear_b = fixed_series_coefficients(7, 6, 4)
    aa = fixed_series_coefficients(5, 5, 4)
    bb = fixed_series_coefficients(7, 7, 4)
    ab = fixed_series_coefficients(6, 6, 4)
    if linear_a[4] != -45 or linear_b[3:5] != [7, -70]:
        raise AssertionError((linear_a, linear_b, "linear sections"))
    if aa[3:5] != [15, -30]:
        raise AssertionError((aa, "AA sections"))
    if bb[1:5] != [-7, 14, 14, -84]:
        raise AssertionError((bb, "BB sections"))
    if ab[2:5] != [9, 16, -54]:
        raise AssertionError((ab, "AB sections"))
    # Formal binomial expansion and section multiplication, with no
    # numerical specialization of p,s,nu.
    frobenius_quadratic = [math.comb(7, 2), math.comb(5 + 1, 2), 7 * (-5)]
    if frobenius_quadratic != [21, 15, -35]:
        raise AssertionError((frobenius_quadratic, "formal Frobenius coefficients"))
    linear_ledger = [7 * linear_a[4], -5 * linear_b[4], -5 * linear_b[3]]
    if linear_ledger != [-35 * 9, -35 * (-10), -35]:
        raise AssertionError((linear_ledger, "linear separation ledger"))
    quadratic_ledger = [
        21 * aa[3],
        21 * aa[4],
        15 * bb[1],
        15 * bb[2],
        15 * bb[3],
        15 * bb[4],
        -35 * ab[2],
        -35 * ab[3],
        -35 * ab[4],
    ]
    expected_quadratic = [35 * x for x in (9, -18, -3, 6, 6, -36, -9, -16, 54)]
    if quadratic_ledger != expected_quadratic:
        raise AssertionError((quadratic_ledger, "quadratic separation ledger"))
    return {
        "linear_A_0_to_4": linear_a,
        "linear_B_0_to_4": linear_b,
        "quadratic_AA_0_to_4": aa,
        "quadratic_BB_0_to_4": bb,
        "quadratic_AB_0_to_4": ab,
        "formal_Frobenius_X2_Y2_XY": frobenius_quadratic,
        "linear_section_ledger": linear_ledger,
        "quadratic_section_ledger": quadratic_ledger,
    }


def phase_weights(p: int, n: int) -> tuple[int, int, int]:
    chi = 1 if p % 4 == 1 else -1
    c_weight = (2, 0, -2, 0)[n % 4]
    j_weight = (0, -2 * chi, 0, 2 * chi)[n % 4]
    total = 9 - 10 * c_weight + j_weight
    if total != item235.phase_weight(p, n):
        raise AssertionError((p, n, total, item235.phase_weight(p, n)))
    return c_weight, j_weight, total


def moment_data(p: int, s: int, nu: int) -> dict[str, int]:
    modulus = p * p
    q = 2 * s - nu
    r, polynomial_2 = p_polynomial(p, s, nu, modulus)
    _, polynomial_1 = p_polynomial(p, s, nu, p)
    degree = len(polynomial_2) - 1
    if p - q - 1 - degree != r + 1:
        raise AssertionError((p, s, nu, "reciprocal degree"))

    lifted_a, lifted_b = lifted_defects(p)
    kernels = kernel_data(p)
    target_1 = p - q - 1
    target_2 = 2 * p - q - 1
    x_lift = coefficient_product(lifted_a, polynomial_2, target_1, modulus)
    y_lift = coefficient_product(lifted_b, polynomial_2, target_1, modulus)
    yprime_lift = coefficient_product(lifted_b, polynomial_2, target_2, modulus)
    linear = (9 * x_lift - 10 * y_lift + yprime_lift) % modulus

    aa: tuple[int, ...] = kernels["AA"]
    bb: tuple[int, ...] = kernels["BB"]
    ab: tuple[int, ...] = kernels["AB"]

    def quadratic_moment(poly: tuple[int, ...], phase: int) -> int:
        return coefficient_product(poly, polynomial_1, phase * p - q - 1, p)

    aa_1, aa_2 = quadratic_moment(aa, 1), quadratic_moment(aa, 2)
    bb_1, bb_2 = quadratic_moment(bb, 1), quadratic_moment(bb, 2)
    bb_3, bb_4 = quadratic_moment(bb, 3), quadratic_moment(bb, 4)
    ab_1, ab_2, ab_3 = (
        quadratic_moment(ab, 1),
        quadratic_moment(ab, 2),
        quadratic_moment(ab, 3),
    )
    quadratic = (
        9 * aa_2
        - 18 * aa_1
        - 3 * bb_4
        + 6 * bb_3
        + 6 * bb_2
        - 36 * bb_1
        - 9 * ab_3
        - 16 * ab_2
        + 54 * ab_1
    ) % p
    separated_quotient = (-35 * linear + 35 * p * quadratic) % modulus

    sigma = (-1) ** (r + 1)
    epsilon = (-1) ** r
    canonical_period = 0
    depth_one_sum = 0
    depth_two_sum = 0
    for ell, coefficient in enumerate(polynomial_2):
        n = r + ell + 1
        if not (1 <= n < p):
            raise AssertionError((p, s, nu, ell, n, "endpoint denominator"))
        _, _, weight = phase_weights(p, n)
        canonical_period += coefficient * weight * pow(n, -1, modulus)
        coefficient_mod_p = polynomial_1[ell]
        depth_one_sum += coefficient_mod_p * kernels["depth_one"][n]
        depth_two_sum += coefficient_mod_p * kernels["depth_two"][n]
    canonical_period %= modulus
    depth_one_sum %= p
    depth_two_sum %= p

    # This is the exact Item 219 period, lifted canonically to Z/(p^2).
    if canonical_period % p != item219.period_sum(p, s, nu):
        raise AssertionError((p, s, nu, "Item219 first-gate interface"))

    if linear != sigma * (canonical_period + p * depth_one_sum) % modulus:
        raise AssertionError((p, s, nu, "linear endpoint carry"))
    if quadratic != epsilon * depth_two_sum % p:
        raise AssertionError((p, s, nu, "quadratic endpoint carry"))

    total_carry = (depth_one_sum + depth_two_sum) % p
    corrected_period = (canonical_period + p * total_carry) % modulus
    endpoint_quotient = (-35 * sigma * corrected_period) % modulus
    if endpoint_quotient != separated_quotient:
        raise AssertionError((p, s, nu, "endpoint/separated bridge"))

    first_zero = corrected_period % p == 0
    second_digit = corrected_period // p if first_zero else -1
    return {
        "r": r,
        "q": q,
        "canonical_period_mod_p2": canonical_period,
        "depth_one_carry_mod_p": depth_one_sum,
        "depth_two_carry_mod_p": depth_two_sum,
        "total_carry_mod_p": total_carry,
        "corrected_period_mod_p2": corrected_period,
        "first_digit_zero": int(first_zero),
        "corrected_second_digit_mod_p": second_digit,
        "linear_moment_mod_p2": linear,
        "quadratic_moment_mod_p": quadratic,
        "quotient_mod_p2": endpoint_quotient,
    }


def admissible_rows(bound: int):
    for p in item219.primes_upto(bound):
        if p < 17:
            continue
        for s in range(2, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4 == 0:
                yield p, s


def exact_integer_replay(bound: int) -> dict[str, Any]:
    rows: list[tuple[int, ...]] = []
    p_cubed_checks = 0
    for p, s in admissible_rows(bound):
        for nu in (0, 1):
            data = moment_data(p, s, nu)
            coefficient = item235.common_log_coefficient(p, s, nu)
            if coefficient % p:
                raise AssertionError((p, s, nu, "rank-zero divisibility"))
            actual = (coefficient // p) % (p * p)
            if actual != data["quotient_mod_p2"]:
                raise AssertionError((p, s, nu, actual, data["quotient_mod_p2"]))
            if (coefficient % (p**3) == 0) != (
                data["corrected_period_mod_p2"] == 0
            ):
                raise AssertionError((p, s, nu, "p^3 criterion"))
            p_cubed_checks += 1
            rows.append(
                (
                    p,
                    s,
                    nu,
                    data["r"],
                    data["canonical_period_mod_p2"],
                    data["depth_one_carry_mod_p"],
                    data["depth_two_carry_mod_p"],
                    data["corrected_period_mod_p2"],
                    actual,
                )
            )
    return {
        "prime_max_inclusive": bound,
        "row_nu_count": len(rows),
        "p_cubed_equivalence_checks": p_cubed_checks,
        "row_digest_sha256": row_digest(rows),
    }


def finite_census(bound: int) -> dict[str, Any]:
    rows = 0
    first_zero = [0, 0]
    extra_zero = [0, 0]
    simultaneous_first: list[dict[str, int]] = []
    first_zero_rows: list[dict[str, int]] = []
    individual_extra: list[dict[str, int]] = []
    digest_rows: list[tuple[int, ...]] = []
    for p, s in admissible_rows(bound):
        rows += 1
        data = [moment_data(p, s, nu) for nu in (0, 1)]
        for nu in (0, 1):
            is_first = bool(data[nu]["first_digit_zero"])
            is_extra = is_first and data[nu]["corrected_second_digit_mod_p"] == 0
            first_zero[nu] += is_first
            extra_zero[nu] += is_extra
            if is_first:
                first_zero_rows.append(
                    {
                        "p": p,
                        "s": s,
                        "nu": nu,
                        "eta_mod_p": data[nu]["corrected_second_digit_mod_p"],
                        "depth_one_carry_mod_p": data[nu]["depth_one_carry_mod_p"],
                        "depth_two_carry_mod_p": data[nu]["depth_two_carry_mod_p"],
                    }
                )
            if is_extra:
                individual_extra.append({"p": p, "s": s, "nu": nu})
        if data[0]["first_digit_zero"] and data[1]["first_digit_zero"]:
            simultaneous_first.append(
                {
                    "p": p,
                    "s": s,
                    "eta_0": data[0]["corrected_second_digit_mod_p"],
                    "eta_1": data[1]["corrected_second_digit_mod_p"],
                }
            )
        digest_rows.append(
            (
                p,
                s,
                data[0]["corrected_period_mod_p2"],
                data[1]["corrected_period_mod_p2"],
                data[0]["depth_one_carry_mod_p"],
                data[0]["depth_two_carry_mod_p"],
                data[1]["depth_one_carry_mod_p"],
                data[1]["depth_two_carry_mod_p"],
            )
        )
    return {
        "prime_max_inclusive": bound,
        "row_count": rows,
        "first_digit_zero_counts_nu_0_nu_1": first_zero,
        "first_digit_zero_rows": first_zero_rows,
        "individual_p_cubed_counts_nu_0_nu_1": extra_zero,
        "individual_p_cubed_rows": individual_extra,
        "simultaneous_common_log_rows": simultaneous_first,
        "simultaneous_common_log_count": len(simultaneous_first),
        "row_digest_sha256": row_digest(digest_rows),
    }


def direct_extra_digit_spotcheck() -> dict[str, int]:
    """Directly confirm the sole bounded individual p^3 row beyond p=101."""
    p, s, nu = 227, 13, 1
    data = moment_data(p, s, nu)
    coefficient = item235.common_log_coefficient(p, s, nu)
    if coefficient % (p**3) or data["corrected_period_mod_p2"] != 0:
        raise AssertionError((p, s, nu, "direct p^3 spotcheck"))
    return {
        "p": p,
        "s": s,
        "nu": nu,
        "m": (5 * p - 2 * s - 1) // 4,
        "C_nu_mod_p_cubed": coefficient % (p**3),
        "C_nu_over_p_mod_p_squared": (coefficient // p) % (p * p),
        "canonical_period_mod_p_squared": data["canonical_period_mod_p2"],
        "total_carry_mod_p": data["total_carry_mod_p"],
        "corrected_period_mod_p_squared": data["corrected_period_mod_p2"],
    }


def endpoint_barrier_witness() -> dict[str, int]:
    p = 17
    s = 2
    kernels = kernel_data(p)
    n_1, n_2 = 2, 6
    if n_1 % 4 != n_2 % 4:
        raise AssertionError("bad witness residues")
    k_1 = kernels["total"][n_1]
    k_2 = kernels["total"][n_2]
    depth_one_1 = kernels["depth_one"][n_1]
    depth_one_2 = kernels["depth_one"][n_2]
    depth_two_1 = kernels["depth_two"][n_1]
    depth_two_2 = kernels["depth_two"][n_2]
    r, polynomial = p_polynomial(p, s, 0, p)
    support_1 = polynomial[n_1 - r - 1]
    support_2 = polynomial[n_2 - r - 1]
    if not support_1 or not support_2:
        raise AssertionError((p, s, n_1, n_2, "witness not in P_0 support"))
    derivative_1 = n_1 * k_1 % p
    derivative_2 = n_2 * k_2 % p
    if derivative_1 == derivative_2:
        raise AssertionError("correction accidentally four-periodic")
    weight = item235.phase_weight(p, n_1)
    corrected_1 = (weight + p * derivative_1) % (p * p)
    corrected_2 = (weight + p * derivative_2) % (p * p)
    return {
        "p": p,
        "s": s,
        "nu": 0,
        "n_same_mod_4_first": n_1,
        "n_same_mod_4_second": n_2,
        "P_nu_coefficient_first_mod_p": support_1,
        "P_nu_coefficient_second_mod_p": support_2,
        "K_depth_one_first_mod_p": depth_one_1,
        "K_depth_one_second_mod_p": depth_one_2,
        "K_depth_two_first_mod_p": depth_two_1,
        "K_depth_two_second_mod_p": depth_two_2,
        "K_first_mod_p": k_1,
        "K_second_mod_p": k_2,
        "nK_first_mod_p": derivative_1,
        "nK_second_mod_p": derivative_2,
        "corrected_derivative_weight_first_mod_p2": corrected_1,
        "corrected_derivative_weight_second_mod_p2": corrected_2,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--integer-prime-max", type=int, default=101)
    parser.add_argument("--finite-prime-max", type=int, default=401)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if not (17 <= args.integer_prime_max <= args.finite_prime_max):
        raise ValueError("require 17 <= integer-prime-max <= finite-prime-max")

    sections = verify_fixed_sections()
    integer_replay = exact_integer_replay(args.integer_prime_max)
    finite = finite_census(args.finite_prime_max)
    extra_spotcheck = direct_extra_digit_spotcheck()
    barrier = endpoint_barrier_witness()

    result = {
        "schema": "item239-j2-actual-witt-bridge-v1",
        "item": 239,
        "route": "Route 1A",
        "cell": "j=2, s>=2, 4m+1=5p-2s",
        "proved": {
            "lifted_binomial_quotients": {
                "Atilde": "((1-z)^p-(1-z^p))/p=-sum k^(-1)(1-p H_(k-1)) z^k mod p^2",
                "Btilde": "((1+z^2)^p-(1+z^(2p)))/p=sum (-1)^(k-1) k^(-1)(1-p H_(k-1)) z^(2k) mod p^2",
            },
            "fixed_sections": sections,
            "separated_bridge": "C_nu/p=-35*(9 Xtilde_nu-10 Ytilde_nu+Ytildeprime_nu)+35p R_nu mod p^2",
            "quadratic_R": "9 AA_2-18 AA_1-3 BB_4+6 BB_3+6 BB_2-36 BB_1-9 AB_3-16 AB_2+54 AB_1",
            "endpoint_bridge": "C_nu/p=-35*(-1)^(r+1)*(S2_nu+p K_nu) mod p^2",
            "first_gate_interface": "S2_nu modulo p is exactly the ordinary Item219 beta period, so S2_nu=0 modulo p is precisely the per-coordinate first gate p^2|C_nu",
            "carry_split": "K_nu is the sum of an explicit depth-one harmonic/inverse-square endpoint carry and one explicit depth-two A^2,B^2,AB convolution coordinate",
            "p_cubed_condition": "p^3 divides C_nu iff S2_nu+p K_nu=0 mod p^2; after the first digit vanishes this is S2_nu/p+K_nu=0 mod p",
        },
        "integer_replay": integer_replay,
        "exact_finite": {
            "status": "EXACT FINITE ONLY",
            **finite,
            "direct_individual_p_cubed_spotcheck": extra_spotcheck,
        },
        "endpoint_scope_barrier": {
            "status": "PROVED SCOPED BARRIER",
            "witness": barrier,
            "conclusion": "the corrected derivative coefficient kernel is not four-periodic even on one admissible row, so that kernel is not represented coefficientwise by a fixed covector on the old endpoints 1,i,-i",
            "not_excluded": "an aggregate identity after cancellation on the restricted P_nu row family, a larger endpoint/cohomology system, or a new terminal recurrence for the explicit corrected kernel",
        },
        "status_ledger": {
            "PROVED": [
                "the complete actual C_nu/p formula modulo p^2 including both lifted-linear and quadratic Frobenius terms",
                "the exact corrected beta-period bridge with depth-one and depth-two carries",
                "the necessary and sufficient scalar condition for p^3 dividing each C_nu",
                "failure of the old fixed-endpoint four-periodic space to contain the corrected derivative coefficient kernel",
            ],
            "EXACT_FINITE": [
                "direct integer coefficient replay and p^3 equivalence through the stated integer bound",
                "the bounded corrected-period census through the stated finite bound",
            ],
            "OPEN": [
                "derive a useful terminal recurrence for the non-four-periodic corrected kernel",
                "decide whether restricted-family coefficient cancellations yield an aggregate old-endpoint identity despite the coefficientwise obstruction",
                "classify simultaneous zeros for nu=0 and nu=1 over all admissible primes",
                "prove any all-prime exclusion, zero-rate theorem, or Route-1 gain",
            ],
        },
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "none",
        },
        "dependencies": {
            "item235_checker": ITEM235_PATH.name,
            "item235_checker_sha256": sha256(ITEM235_PATH),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
