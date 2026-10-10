#!/usr/bin/env python3
"""Portable exact checker for Item 252's final-diagonal normal form.

The script uses only Python's standard library.  It checks exact integer and
rational identities, replays the modular formula on actual ordinary-j=2
rows, audits every denominator range, and checks the finite-field pole-orbit
profile used in the scalar fixed-degree lower bound.

Finite row counts are evidence only inside the emitted bound.  The no-go and
normal-form claims are algebraic proofs documented in the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent


def primes_up_to(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(bound) + 1):
        if sieve[q]:
            start = q * q
            sieve[start : bound + 1 : q] = b"\x00" * (((bound - start) // q) + 1)
    return [q for q in range(2, bound + 1) if sieve[q]]


def rising(a: F, length: int) -> F:
    out = F(1)
    for j in range(length):
        out *= a + j
    return out


def s_sum(a: F, m: int) -> F:
    return sum(
        (rising(a, j) / (math.factorial(j) * 2**j) for j in range(m + 1)),
        F(0),
    )


def h_value(j: int) -> F:
    return rising(F(1, 2), j) / (math.factorial(j) * 2**j)


def h_prefix(m: int) -> F:
    return sum((h_value(j) for j in range(m + 1)), F(0))


def p_boundary(d: int, m: int) -> F:
    return sum(
        (
            F(1, 2**k)
            * rising(F(m, 1) + F(1, 2), k)
            / rising(F(1, 2), k)
            for k in range(1, d + 1)
        ),
        F(0),
    )


def a_double_sum(s: int) -> int:
    return sum(
        math.comb(3 * s - 1, s + j) * math.comb(s + j - 1, j)
        for j in range(2 * s)
    )


def a_quotient_coefficient(s: int) -> int:
    n = 3 * s - 1
    m = s - 1
    main = sum(
        (-1) ** (m - j) * math.comb(n, j) * 2 ** (n - j)
        for j in range(m + 1)
    )
    return main - (-1) ** m


def c_boundary(s: int) -> int:
    numerator = 4**s * (28 * s + 11) * math.comb(3 * s - 1, s - 1)
    assert numerator % (2 * s + 1) == 0
    return numerator // (2 * s + 1)


def frac_mod(value: F, p: int) -> int:
    den = value.denominator % p
    assert den != 0
    return (value.numerator % p) * pow(den, -1, p) % p


def actual_rows(bound: int):
    for p in primes_up_to(bound):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            numerator = p - 6 * s - 3
            if numerator <= 0:
                break
            if numerator % 2:
                continue
            r = numerator // 2
            if r >= 1 and r % 2 == 1 and r % 3 != 0:
                assert p == 2 * r + 6 * s + 3
                yield p, r, s


def direct_a_mod(p: int, s: int) -> int:
    n = 3 * s - 1
    m = s - 1
    total = 0
    for j in range(m + 1):
        total += (-1) ** (m - j) * math.comb(n, j) * pow(2, n - j, p)
    return (total - (-1) ** m) % p


def double_a_mod(p: int, s: int) -> int:
    return sum(
        (math.comb(3 * s - 1, s + j) % p)
        * (math.comb(s + j - 1, j) % p)
        for j in range(2 * s)
    ) % p


def modular_row(p: int, r: int, s: int) -> dict[str, int]:
    m = s - 1
    d = r + 2
    n = 3 * s - 1
    assert n == (p - 1) // 2 - d

    inv2 = pow(2, -1, p)
    epsilon = pow(2, (p - 1) // 2, p)
    assert epsilon in (1, p - 1)

    # Direct shifted-parameter sum S_m(d+1/2).
    shifted_term = 1
    shifted_sum = 1
    rising_over_factorial = 1
    lucas_equalities = 0
    for j in range(m + 1):
        # binom(N,j)=(-1)^j(d+1/2)_j/j! modulo p.
        assert math.comb(n, j) % p == ((-1) ** j * rising_over_factorial) % p
        lucas_equalities += 1
        if j < m:
            numerator = 2 * d + 1 + 2 * j
            denominator = 4 * (j + 1)
            assert 0 < numerator <= 2 * m + 2 * d - 1 < p
            assert 0 < denominator <= 4 * m < p
            rising_over_factorial = (
                rising_over_factorial
                * numerator
                * pow(2 * (j + 1), -1, p)
                % p
            )
            shifted_term = shifted_term * numerator * pow(denominator, -1, p) % p
            shifted_sum = (shifted_sum + shifted_term) % p

    # Universal half-binomial period and its boundary term.
    h_term = 1
    h_sum = 1
    for j in range(m):
        numerator = 2 * j + 1
        denominator = 4 * (j + 1)
        assert 0 < numerator < p
        assert 0 < denominator <= 4 * m < p
        h_term = h_term * numerator * pow(denominator, -1, p) % p
        h_sum = (h_sum + h_term) % p

    # Fixed-r contiguous boundary polynomial P_d(m).
    rectangle_ratio = 1
    p_value = 0
    inverse_two_power = inv2
    rectangle_equalities = 0
    for k in range(1, d + 1):
        numerator = 2 * m + 2 * k - 1
        denominator = 2 * k - 1
        assert 0 < denominator <= 2 * d - 1 < p
        assert 0 < numerator <= 2 * m + 2 * d - 1 < p
        rectangle_ratio = rectangle_ratio * numerator * pow(denominator, -1, p) % p
        p_value = (p_value + inverse_two_power * rectangle_ratio) % p
        inverse_two_power = inverse_two_power * inv2 % p
        rectangle_equalities += 1

    shifted_normalized = pow(2, -d, p) * shifted_sum % p
    contiguous_normalized = (h_sum - h_term * p_value) % p
    assert shifted_normalized == contiguous_normalized

    predicted = (epsilon * contiguous_normalized - 1) % p
    if m % 2:
        predicted = (-predicted) % p

    direct = direct_a_mod(p, s)
    doubled = double_a_mod(p, s)
    assert predicted == direct == doubled

    # The explicit range bounds used above.
    assert 0 <= m < p
    assert 2 * d - 1 == 2 * r + 3 == p - 6 * s < p
    assert 2 * m + 2 * d - 1 == 2 * s + 2 * r + 1 == p - 4 * s - 2 < p

    return {
        "p": p,
        "r": r,
        "s": s,
        "m": m,
        "d": d,
        "epsilon_2": epsilon,
        "h_boundary_m": h_term,
        "H_prefix_m": h_sum,
        "P_d": p_value,
        "A_s": direct,
        "lucas_equalities": lucas_equalities,
        "rectangle_equalities": rectangle_equalities,
    }


def exact_identity_audit() -> dict[str, object]:
    rows = []
    values: dict[int, int] = {}
    for s in range(1, 51):
        first = a_double_sum(s)
        second = a_quotient_coefficient(s)
        assert first == second
        values[s] = first
        rows.append((s, first))
    for s in range(1, 50):
        assert values[s + 1] + values[s] == c_boundary(s)

    contiguous_checks = 0
    rectangle_checks = 0
    for m in range(0, 13):
        for numerator in range(1, 14, 2):
            a = F(numerator, 2)
            left = s_sum(a + 1, m)
            right = 2 * s_sum(a, m) - rising(a + 1, m) / (
                math.factorial(m) * 2**m
            )
            assert left == right
            contiguous_checks += 1
    for r in range(1, 18, 2):
        if r % 3 == 0:
            continue
        d = r + 2
        for s in range(1, 9):
            m = s - 1
            left = s_sum(F(1, 2) + d, m) / 2**d
            right = h_prefix(m) - h_value(m) * p_boundary(d, m)
            assert left == right
            rectangle_checks += 1

    digest = hashlib.sha256(
        "".join(f"{s},{value}\n" for s, value in rows).encode("ascii")
    ).hexdigest()
    return {
        "integer_rows": len(rows),
        "double_sum_equals_quotient": len(rows),
        "first_order_factor_equalities": 49,
        "contiguous_shift_equalities": contiguous_checks,
        "pochhammer_rectangle_equalities": rectangle_checks,
        "A_1": values[1],
        "A_2": values[2],
        "A_3": values[3],
        "row_digest_sha256": digest,
    }


def pole_orbit_audit(bound: int = 251) -> dict[str, object]:
    rows = []
    for p in primes_up_to(bound):
        if p < 5:
            continue
        inv2 = pow(2, -1, p)
        z = (-inv2) % p
        w = p - 1
        distance = (w - z) % p
        assert distance == (p - 1) // 2

        # Minimal nonnegative pole profile on the exceptional orbit:
        # order one from z+1 through w, order zero on the complement.
        orders = [0] * p
        for k in range(1, distance + 1):
            orders[(z + k) % p] = 1
        assert sum(orders) == (p - 1) // 2

        for x in range(p):
            q_pole_order = 1 if x == w else (-1 if x == z else 0)
            product_pole_order = max(0, orders[(x + 1) % p] + q_pole_order)
            assert product_pole_order == orders[x]

        rows.append(
            {
                "p": p,
                "zero": z,
                "pole": w,
                "forward_distance": distance,
                "minimal_denominator_degree": sum(orders),
            }
        )

    return {
        "checked_primes": len(rows),
        "prime_bound": bound,
        "first_rows": rows[:8],
        "all_minimal_profiles_verified": True,
        "theorem_scope": (
            "for every prime p>=5, any scalar rational solution over Fbar_p, "
            "if it exists, has reduced-denominator degree at least (p-1)/2"
        ),
        "polynomial_branch": {
            "cleared_equation": "(2x+1)R(x+1)-4(x+1)R(x)=4(x+1)",
            "positive_degree_leading_multiplier": "-2 (nonzero for p>=5)",
            "constant_x_equation": "-2c=4",
            "constant_term_equation": "-3c=4",
            "compatible_only_in_characteristic": 2,
        },
        "characteristic_zero": {
            "q_zero": "-1/2",
            "q_pole": "-1",
            "required_left_pole_endpoint": "1/2",
            "endpoint_difference": "-3/2, not an integer",
            "rational_solution": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=601)
    parser.add_argument("--output", type=Path, default=HERE / "item252_diagonal_modp_certificate.json")
    args = parser.parse_args()
    assert args.bound >= 11

    exact = exact_identity_audit()
    finite_rows = []
    total_lucas = 0
    total_rectangle = 0
    zeros = []
    h_zeros = []
    for p, r, s in actual_rows(args.bound):
        row = modular_row(p, r, s)
        finite_rows.append(row)
        total_lucas += row["lucas_equalities"]
        total_rectangle += row["rectangle_equalities"]
        if row["A_s"] == 0:
            zeros.append({"p": p, "r": r, "s": s})
        if row["H_prefix_m"] == 0:
            h_zeros.append({"p": p, "r": r, "s": s})

    row_digest = hashlib.sha256(
        "".join(
            f"{row['p']},{row['r']},{row['s']},{row['A_s']},{row['h_boundary_m']},"
            f"{row['H_prefix_m']},{row['P_d']}\n"
            for row in finite_rows
        ).encode("ascii")
    ).hexdigest()

    result = {
        "schema": "item252-diagonal-modp-certificate-v1",
        "imports_item_code": False,
        "theorems": {
            "one_period_normal_form": (
                "A_s=(-1)^m*(eps_2*(H_m-h_m*P_(r+2)(m))-1) mod p, m=s-1"
            ),
            "contiguous_boundary": (
                "P_d(m)=sum_(k=1)^d 2^(-k)*(m+1/2)_k/(1/2)_k"
            ),
            "scalar_characteristic_zero_no_go": True,
            "scalar_Fbar_p_reduced_denominator_lower_bound": "(p-1)/2 for every p>=5",
        },
        "exact_identity_audit": exact,
        "unit_audit": {
            "actual_row_denominators_are_units": True,
            "m_bound": "0<=m=s-1<p",
            "P_denominator_bound": "2d-1=2r+3=p-6s<p",
            "P_numerator_bound": "2m+2d-1=2s+2r+1=p-4s-2<p",
            "shifted_sum_denominator_bound": "4(j+1)<=4m=4s-4<p",
            "shifted_sum_numerator_bound": "2d+1+2j<=2m+2d-1<p",
            "lucas_term_equalities": total_lucas,
            "rectangle_term_equalities": total_rectangle,
        },
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.bound,
            "actual_rows": len(finite_rows),
            "direct_double_sum_frobenius_normal_form_equalities": len(finite_rows),
            "A_s_zero_count": len(zeros),
            "A_s_zero_witnesses_first_12": zeros[:12],
            "H_m_zero_count": len(h_zeros),
            "H_m_zero_witnesses_first_12": h_zeros[:12],
            "first_rows": finite_rows[:8],
            "row_digest_sha256": row_digest,
            "scope": "bounded exact replay only; no all-prime or density inference",
        },
        "scalar_fixed_degree_no_go": pole_orbit_audit(),
        "OPEN": [
            "a phase-only identity at m=(p-2r-9)/6",
            "a higher-rank Cartier or nonlinear relation removing H_m",
            "all-prime nonvanishing or weighted zero control for A_s",
            "any capacity reduction or conclusion about e+pi",
        ],
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
