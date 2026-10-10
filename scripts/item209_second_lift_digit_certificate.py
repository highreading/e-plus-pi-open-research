#!/usr/bin/env python3
"""Deterministic exact checker for Item 209's kappa=1 second-lift digit.

This file is deliberately standalone (Python standard library only).  It
replays the local Hasse recurrence modulo p^3, forms the raw A and B
determinants, and reconstructs their base-p digits by signed convolution
and carry.  The finite scans are audits only; the all-row statements are
proved in the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "item209_second_lift_digit_certificate.json"
PRECISION = 3
FINITE_ANCHOR_MAX_J = 12
G = tuple[int, int]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, math.isqrt(n) + 1, 2))


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("vp(0) is not used")
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def factorial_valuation(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def ga(a: int, b: int, mod: int) -> G:
    return a % mod, b % mod


def gadd(x: G, y: G, mod: int) -> G:
    return (x[0] + y[0]) % mod, (x[1] + y[1]) % mod


def gneg(x: G, mod: int) -> G:
    return (-x[0]) % mod, (-x[1]) % mod


def gmul(x: G, y: G, mod: int) -> G:
    return (
        (x[0] * y[0] - x[1] * y[1]) % mod,
        (x[0] * y[1] + x[1] * y[0]) % mod,
    )


def gscale(x: G, scalar: int, mod: int) -> G:
    return x[0] * scalar % mod, x[1] * scalar % mod


def ginv(x: G, mod: int) -> G:
    inv_norm = pow((x[0] * x[0] + x[1] * x[1]) % mod, -1, mod)
    return x[0] * inv_norm % mod, -x[1] * inv_norm % mod


def gpow(x: G, exponent: int, mod: int) -> G:
    if exponent < 0:
        return gpow(ginv(x, mod), -exponent, mod)
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = gmul(out, x, mod)
        x = gmul(x, x, mod)
        exponent >>= 1
    return out


def iadd(x: G, y: G) -> G:
    return x[0] + y[0], x[1] + y[1]


def imul(x: G, y: G) -> G:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def iscale(x: G, scalar: int) -> G:
    return x[0] * scalar, x[1] * scalar


def iconv(left: list[G], right: list[G]) -> list[G]:
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = iadd(out[i + j], imul(x, y))
    return out


def iderivative(poly: list[G]) -> list[G]:
    return [iscale(poly[j], j) for j in range(1, len(poly))]


def local_polynomials(root: str) -> tuple[list[G], list[G]]:
    if root == "minus_one":
        return [(-2, 0), (3, 0), (-1, 0)], [(2, 0), (-2, 0), (1, 0)]
    if root == "i":
        return [(1, 1), (1, -2), (-1, 0)], [(-2, 2), (1, 3), (1, 0)]
    raise ValueError(root)


def local_coefficients(
    m: int, k: int, root: str, p: int, precision: int
) -> list[G]:
    """C_0,...,C_(k-1) with the exact factorial-valuation reserve."""
    degree = k - 1
    reserve = factorial_valuation(degree, p)
    a_poly, b_poly = local_polynomials(root)
    product = iconv(a_poly, b_poly)
    right = iconv(iderivative(a_poly), b_poly)
    right = [iscale(value, 6 * m) for value in right]
    other = iconv(a_poly, iderivative(b_poly))
    if len(other) > len(right):
        right += [(0, 0)] * (len(other) - len(right))
    for index, value in enumerate(other):
        right[index] = iadd(right[index], iscale(value, -k))

    initial_precision = precision + reserve
    initial_modulus = p**initial_precision
    a0 = ga(*a_poly[0], initial_modulus)
    b0 = ga(*b_poly[0], initial_modulus)
    c0 = gmul(
        gpow(a0, 6 * m, initial_modulus),
        gpow(b0, -k, initial_modulus),
        initial_modulus,
    )
    coefficients = [c0]
    precisions = [initial_precision]
    used_factorial_valuation = 0

    for n in range(degree):
        divisor = n + 1
        divisor_valuation = vp(divisor, p)
        required_precision = precision + reserve - used_factorial_valuation
        target_precision = required_precision - divisor_valuation
        required_modulus = p**required_precision
        target_modulus = p**target_precision
        rhs = (0, 0)

        for shift in range(0, min(len(right) - 1, n) + 1):
            source = n - shift
            if precisions[source] < required_precision:
                raise AssertionError(("RHS precision", m, p, k, n, shift))
            term = gmul(
                ga(*right[shift], required_modulus),
                (
                    coefficients[source][0] % required_modulus,
                    coefficients[source][1] % required_modulus,
                ),
                required_modulus,
            )
            rhs = gadd(rhs, term, required_modulus)

        for shift in range(1, min(len(product) - 1, n) + 1):
            source = n - shift + 1
            if precisions[source] < required_precision:
                raise AssertionError(("LHS precision", m, p, k, n, shift))
            term = gmul(
                ga(*product[shift], required_modulus),
                (
                    coefficients[source][0] % required_modulus,
                    coefficients[source][1] % required_modulus,
                ),
                required_modulus,
            )
            term = gscale(term, n - shift + 1, required_modulus)
            rhs = gadd(rhs, gneg(term, required_modulus), required_modulus)

        p_power = p**divisor_valuation
        if rhs[0] % p_power or rhs[1] % p_power:
            raise AssertionError(("nonexact p-division", m, p, k, n))
        quotient = (
            rhs[0] // p_power % target_modulus,
            rhs[1] // p_power % target_modulus,
        )
        unit = divisor // p_power
        quotient = gscale(quotient, pow(unit, -1, target_modulus), target_modulus)
        inverse_constant = ginv(ga(*product[0], target_modulus), target_modulus)
        coefficients.append(gmul(inverse_constant, quotient, target_modulus))
        precisions.append(target_precision)
        used_factorial_valuation += divisor_valuation

    if precisions[-1] != precision:
        raise AssertionError(("final precision", m, p, k, precisions[-1]))
    modulus = p**precision
    return [(a % modulus, b % modulus) for a, b in coefficients]


def endpoint_factor(root: G, n: int, modulus: int) -> G:
    minus_root = gneg(root, modulus)
    one_minus_root = gadd((1, 0), gneg(root, modulus), modulus)
    return gadd(
        gpow(minus_root, -n, modulus),
        gneg(gpow(one_minus_root, -n, modulus), modulus),
        modulus,
    )


def coordinates_mod(
    m: int, k: int, p: int, precision: int = PRECISION
) -> tuple[int, int, int, dict[int, int]]:
    """Return (L,X=pR,E) and the exact e=1 Hasse bands mod p^precision."""
    modulus = p**precision
    cm = local_coefficients(m, k, "minus_one", p, precision)
    ci = local_coefficients(m, k, "i", p, precision)
    residue_minus_one = cm[k - 1][0]
    residue_i = ci[k - 1]
    l_value = (4 * residue_minus_one + 4 * residue_i[0]) % modulus
    e_value = (-4 * residue_i[1]) % modulus

    roots_and_coefficients = [
        (ga(-1, 0, modulus), cm),
        (ga(0, 1, modulus), ci),
        (ga(0, -1, modulus), [(a, -b % modulus) for a, b in ci]),
    ]
    total = (0, 0)
    bands: dict[int, G] = {}
    for n in range(1, k):
        valuation = vp(n, p)
        if valuation > 1:
            raise AssertionError(("e=1 violated", m, p, k, n))
        band = 1 - valuation
        unit = n // (p**valuation)
        scalar = p**band * pow(unit, -1, modulus) % modulus
        contribution = (0, 0)
        index = k - 1 - n
        for root, coefficients in roots_and_coefficients:
            term = gmul(
                coefficients[index], endpoint_factor(root, n, modulus), modulus
            )
            contribution = gadd(contribution, term, modulus)
        contribution = gscale(contribution, scalar, modulus)
        total = gadd(total, contribution, modulus)
        bands[band] = gadd(bands.get(band, (0, 0)), contribution, modulus)
    if total[1] or any(value[1] for value in bands.values()):
        raise AssertionError(("non-rational endpoint", m, p, k, total, bands))
    return l_value, total[0], e_value, {h: value[0] for h, value in bands.items()}


def p_digits(value: int, p: int, width: int = PRECISION) -> list[int]:
    value %= p**width
    return [(value // (p**index)) % p for index in range(width)]


def determinant_digits_by_carry(
    first_left: int,
    first_right: int,
    second_left: int,
    second_right: int,
    p: int,
    width: int = PRECISION,
) -> tuple[list[int], list[int], list[int]]:
    first_left_digits = p_digits(first_left, p, width)
    first_right_digits = p_digits(first_right, p, width)
    second_left_digits = p_digits(second_left, p, width)
    second_right_digits = p_digits(second_right, p, width)
    digits: list[int] = []
    raw: list[int] = []
    carries: list[int] = []
    carry = 0
    for n in range(width):
        coefficient = sum(
            first_left_digits[q] * first_right_digits[n - q]
            - second_left_digits[q] * second_right_digits[n - q]
            for q in range(n + 1)
        )
        raw.append(coefficient)
        total = coefficient + carry
        digit = total % p
        carry = (total - digit) // p
        digits.append(digit)
        carries.append(carry)
    return digits, raw, carries


def common_numerator_state(s: int, p: int) -> dict[str, Any]:
    """Item205/208 coefficient recurrence, evaluated exactly in F_p."""
    k = 3 * s + 2
    if not (k < p and is_prime(p)):
        raise ValueError((s, p, k))
    values = [0] * (k + 1)
    values[0] = 1

    def at(index: int) -> int:
        return values[index] if index >= 0 else 0

    for n in range(k):
        rhs = (5 * s + 3) * (at(n) + at(n - 1) + at(n - 2))
        rhs += (n - 3 * s) * at(n - 3)
        values[n + 1] = rhs * pow(n + 1, -1, p) % p
    g1 = values[k]
    g0 = sum(values[k - shift] for shift in range(4)) % p
    return {
        "s": s,
        "p": p,
        "k": k,
        "terminal_A_k_minus_3_through_A_k": values[k - 3 : k + 1],
        "g0_mod_p": g0,
        "g1_mod_p": g1,
        "common_content_mod_p": g0 == g1 == 0,
    }


def evaluate_row(s: int, p: int, j: int) -> dict[str, Any]:
    if not is_prime(p):
        raise ValueError(("not prime", p))
    numerator = (j + 1) * p - s - 1
    if numerator % 2:
        raise ValueError(("nonintegral m", s, p, j))
    m = numerator // 2
    if not (j >= 1 and 0 <= s <= (p - 3) // 3 and s % 2 == j % 2):
        raise ValueError(("not admissible", m, p, j, s))
    if not (p < 2 * m and 4 * m + 1 < p * p):
        raise ValueError(("not e=1 cell", m, p, j, s))

    l0, x0, e0, bands0 = coordinates_mod(m, 4 * m + 1, p)
    l1, x1, e1, bands1 = coordinates_mod(m, 4 * m + 2, p)
    modulus = p**PRECISION
    determinant_a = (l1 * x0 - l0 * x1) % modulus
    determinant_b = (l1 * e0 - l0 * e1) % modulus
    a_digits, a_raw, a_carries = determinant_digits_by_carry(l1, x0, l0, x1, p)
    b_digits, b_raw, b_carries = determinant_digits_by_carry(l1, e0, l0, e1, p)
    if a_digits != p_digits(determinant_a, p):
        raise AssertionError(("A direct/carry mismatch", m, p))
    if b_digits != p_digits(determinant_b, p):
        raise AssertionError(("B direct/carry mismatch", m, p))
    if a_digits[0] or b_digits[0]:
        raise AssertionError(("rank-one first digit", m, p, a_digits, b_digits))

    # First exact divisions: rank one gives determinant_A,B in p Z_p.
    if determinant_a % p or determinant_b % p:
        raise AssertionError(("first exact division", m, p))
    a_after_forced_p = determinant_a // p
    b_after_forced_p = determinant_b // p
    a0 = a_after_forced_p % p
    b0 = b_after_forced_p % p
    if (a0, b0) != (a_digits[1], b_digits[1]):
        raise AssertionError(("first gate naming", m, p))

    a1: int | None = None
    a_after_second_p: int | None = None
    if a0 == 0:
        # Second exact division: A0=0 gives determinant_A in p^2 Z_p.
        if determinant_a % (p * p):
            raise AssertionError(("second exact division", m, p))
        a_after_second_p = determinant_a // (p * p)
        a1 = a_after_second_p % p
        if a1 != a_digits[2]:
            raise AssertionError(("second-lift naming", m, p, a1, a_digits))

        # The signed carry formula, including the two pre-reduction divisions.
        if a_raw[0] % p:
            raise AssertionError(("S0/p", m, p, a_raw))
        c0 = a_raw[0] // p
        if (a_raw[1] + c0) % p:
            raise AssertionError(("(S1+c0)/p", m, p, a_raw, c0))
        c1 = (a_raw[1] + c0) // p
        if (a_raw[2] + c1) % p != a1:
            raise AssertionError(("A1 carry quotient", m, p))

    return {
        "m": m,
        "p": p,
        "j": j,
        "s": s,
        "coordinate_digits": {
            "L0": p_digits(l0, p),
            "L1": p_digits(l1, p),
            "X0_equals_pR0": p_digits(x0, p),
            "X1_equals_pR1": p_digits(x1, p),
            "E0": p_digits(e0, p),
            "E1": p_digits(e1, p),
        },
        "raw_A_determinant_mod_p3": determinant_a,
        "raw_A_determinant_digits_d0_d1_d2": a_digits,
        "raw_A_convolutions_S0_S1_S2": a_raw,
        "raw_A_carries_c0_c1_c2": a_carries,
        "A_after_forced_p_mod_p2": a_after_forced_p,
        "A0_equals_raw_digit_d1": a0,
        "A1_equals_raw_digit_d2_when_A0_zero": a1,
        "A_after_second_exact_p_mod_p": a_after_second_p,
        "raw_B_determinant_mod_p3": determinant_b,
        "raw_B_determinant_digits_d0_d1_d2": b_digits,
        "raw_B_convolutions_S0_S1_S2": b_raw,
        "raw_B_carries_c0_c1_c2": b_carries,
        "B_after_forced_p_mod_p2": b_after_forced_p,
        "B0_equals_raw_digit_d1": b0,
        "B_raw_digit_d2_not_named_A1": b_digits[2],
        "A0_B0_zero": a0 == b0 == 0,
        "joint_cubic_gate": a0 == 0 and a1 == 0 and b0 == 0,
        "Hasse_band_indices": sorted(set(bands0) | set(bands1)),
    }


def automatic_anchor_scan(max_j: int) -> dict[str, Any]:
    rows = []
    degree_audit = []
    for j in range(1, max_j + 1):
        K = 2 * j + 2
        A = 3 * j + 2
        for p in range(K + 1, A + 1):
            if not is_prime(p):
                continue
            h = p - K
            r = A - p
            polynomial_degree = r + 3 * h
            if not (1 <= h <= j and r == j - h):
                raise AssertionError(("anchor parameters", j, p, h, r))
            if polynomial_degree != j + 2 * h or polynomial_degree > p - 2:
                raise AssertionError(("Cartier degree", j, p, polynomial_degree))
            degree_audit.append(
                {
                    "j": j,
                    "p": p,
                    "h_equals_p_minus_K": h,
                    "r_equals_A_minus_p": r,
                    "base_and_divided_polynomial_degree": polynomial_degree,
                    "p_minus_2": p - 2,
                }
            )
            for s in range(0, (p - 3) // 3 + 1):
                if s % 2 != j % 2:
                    continue
                row = evaluate_row(s, p, j)
                if not row["A0_B0_zero"]:
                    raise AssertionError(("automatic first gates", row))
                if p * p > 6 * row["m"]:
                    raise AssertionError(("p^2 <= 6m", row))
                rows.append(row)
    return {
        "status": "FINITE_EXACT_AUDIT_ONLY",
        "range": {"1<=j<=": max_j, "all_primes_2j+3<=p<=3j+2": True},
        "degree_audit": degree_audit,
        "row_count": len(rows),
        "A0_B0_zero_count": sum(row["A0_B0_zero"] for row in rows),
        "A1_zero_count": sum(row["A1_equals_raw_digit_d2_when_A0_zero"] == 0 for row in rows),
        "A1_nonzero_count": sum(row["A1_equals_raw_digit_d2_when_A0_zero"] != 0 for row in rows),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--anchor-max-j", type=int, default=FINITE_ANCHOR_MAX_J)
    args = parser.parse_args()
    if args.anchor_max_j != FINITE_ANCHOR_MAX_J:
        raise ValueError(
            f"canonical checker requires --anchor-max-j={FINITE_ANCHOR_MAX_J}"
        )

    content_states = [
        common_numerator_state(3, 19),
        common_numerator_state(299, 1499),
        common_numerator_state(299, 2399),
    ]
    if not all(row["common_content_mod_p"] for row in content_states):
        raise AssertionError(content_states)
    expected_terminal = {
        (3, 19): [15, 4, 0, 0],
        (299, 1499): [468, 1031, 0, 0],
        (299, 2399): [7, 2392, 0, 0],
    }
    for row in content_states:
        key = row["s"], row["p"]
        if row["terminal_A_k_minus_3_through_A_k"] != expected_terminal[key]:
            raise AssertionError(("terminal state", row))

    controls = [
        evaluate_row(3, 19, 1),
        evaluate_row(3, 19, 3),
        evaluate_row(299, 1499, 1),
        evaluate_row(299, 2399, 1),
        evaluate_row(0, 7, 2),
    ]
    expected = {
        (17, 19): (0, 16, 0),
        (36, 19): (0, 0, 0),
        (1349, 1499): (0, 925, 0),
        (2249, 2399): (0, 404, 0),
        (10, 7): (0, 1, 0),
    }
    for row in controls:
        observed = (
            row["A0_equals_raw_digit_d1"],
            row["A1_equals_raw_digit_d2_when_A0_zero"],
            row["B0_equals_raw_digit_d1"],
        )
        if observed != expected[(row["m"], row["p"])]:
            raise AssertionError(("control", row, observed))

    anchor = automatic_anchor_scan(args.anchor_max_j)
    output = {
        "schema": "item209-kappa1-second-lift-v1",
        "status": {
            "all_row_exact_A1_quotient_and_carry_formula": "PROVED_IN_COMPANION_REPORT",
            "automatic_anchor_first_gate_theorem": "PROVED_IN_COMPANION_REPORT",
            "automatic_anchor_zero_rate_bound": "PROVED_IN_COMPANION_REPORT",
            "common_content_does_not_force_A1": "PROVED_BY_EXACT_NONZERO_WITNESSES",
            "finite_Hasse_replays": "FINITE_EXACT_AUDIT_ONLY",
            "A1_density_or_global_exclusion": "OPEN",
        },
        "digit_convention": {
            "raw_A_determinant": "mathscrA=L1*X0-L0*X1 with Xnu=p*Rnu",
            "raw_digits": "mathscrA=d0+p*d1+p^2*d2 mod p^3, 0<=dq<p",
            "forced_rank_one_digit": "d0=0",
            "A0": "d1=(mathscrA/p) mod p",
            "A1": "d2=(mathscrA/p^2) mod p, defined as the second gate only after A0=0",
            "B0": "raw B determinant digit d1; B raw digit d2 is not A1",
        },
        "all_row_formula": {
            "S_n": "sum_{q=0}^n(ell_1q*x_0,n-q-ell_0q*x_1,n-q)",
            "first_exact_division": "rank one gives p|S0 and c0=S0/p",
            "A0": "(S1+c0) mod p",
            "second_exact_division": "A0=0 gives c1=(S1+c0)/p",
            "A1": "(S2+c1) mod p",
            "direct_quotient": "if A0=0, A1=(L1*X0-L0*X1)/p^2 mod p",
            "B0_role": "B0=0 is required by the cubic gate but is not needed to make the A1 quotient integral",
        },
        "common_moving_content_states": content_states,
        "distinguished_exact_controls": controls,
        "automatic_anchor_scan": anchor,
        "rate_ledger": {
            "p_equals_5s_plus_4": "10m+1=(5j+4)p, so fixed-m log weight is O(log m)",
            "p_equals_8s_plus_7_if_it_were_a_family": "16m+1=(8j+7)p, so fixed-m log weight would be O(log m)",
            "automatic_anchor": "p^2<=6m, hence total log weight is at most theta(sqrt(6m))=O(sqrt(m))",
            "new_exponent_from_these_repackagings": 0,
        },
        "scope": {
            "p_2399_and_p_1499_rows": "FINITE exact Hasse computations",
            "p_equals_8s_plus_7": "only the s=299 content point is certified; no infinite content ray is claimed",
            "finite_scan_no_extrapolation": True,
            "no_A1_density_claim": True,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "anchor_rows": anchor["row_count"],
                "anchor_A1_zero": anchor["A1_zero_count"],
                "anchor_A1_nonzero": anchor["A1_nonzero_count"],
                "controls": len(controls),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
