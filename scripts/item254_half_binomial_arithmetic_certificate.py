#!/usr/bin/env python3
"""Portable exact checker for Item 254's half-binomial arithmetic forms.

The script uses only Python's standard library.  It checks the coefficient,
finite-field Mellin/Greene, incomplete-beta, fixed-cutoff boundary, and
2-adic numerator identities in the companion report.  Every bounded census
emitted here is labeled EXACT FINITE ONLY; the all-row statements are proved
algebraically in the report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
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
            sieve[start : bound + 1 : q] = b"\x00" * (
                ((bound - start) // q) + 1
            )
    return [q for q in range(2, bound + 1) if sieve[q]]


def chi(value: int, p: int) -> int:
    return pow(value % p, (p - 1) // 2, p)


def h_prefixes_mod(p: int, limit: int) -> tuple[list[int], list[int]]:
    terms = [1]
    prefixes = [1]
    term = 1
    total = 1
    for j in range(limit):
        numerator = 2 * j + 1
        denominator = 4 * (j + 1)
        assert numerator % p != 0 and denominator % p != 0
        term = term * numerator * pow(denominator, -1, p) % p
        total = (total + term) % p
        terms.append(term)
        prefixes.append(total)
    return terms, prefixes


def actual_rows_for_prime(p: int):
    for s in range(1, (p - 3) // 6 + 1):
        numerator = p - 6 * s - 3
        if numerator <= 0:
            break
        assert numerator % 2 == 0
        r = numerator // 2
        if r >= 1 and r % 2 == 1 and r % 3 != 0:
            yield r, s


def fixed_cutoff_boundaries(p: int, q: int) -> tuple[list[int], int]:
    """Return B_delta for 0<=delta<=q and the number of unit ratios."""

    residue = p % 6
    assert residue in (1, 5)
    values = [0]
    product = 1
    total = 0
    checks = 0
    for delta in range(1, q + 1):
        total = (total + product) % p
        values.append(total)
        if delta < q:
            i = delta - 1
            if residue == 1:
                numerator = 6 * i + 1
                denominator = 3 * i + 2
            else:
                numerator = 6 * i + 5
                denominator = 3 * i + 4
            assert 0 < numerator < p
            assert 0 < denominator < p
            product = product * numerator * pow(denominator, -1, p) % p
            checks += 1
    return values, checks


def beta_value_mod(p: int, r: int, m: int) -> tuple[int, int]:
    d = r + 4
    n = (p - 1) // 2
    assert n == 3 * m + d
    integral = 0
    unit_checks = 0
    for k in range(m + 1):
        denominator = 2 * m + d + k
        assert 0 < 2 * m + d <= denominator <= 3 * m + d == n < p
        integral += (
            math.comb(m, k)
            * pow(-2, k, p)
            * pow(denominator, -1, p)
        )
        unit_checks += 1
    prefactor = (
        pow(2, -m, p)
        * (2 * m + d)
        * (math.comb(n, m) % p)
    ) % p
    assert prefactor != 0
    return prefactor * (integral % p) % p, unit_checks


def coefficient_and_row_audit(bound: int, identity_bound: int) -> dict[str, object]:
    rows = 0
    beta_equalities = 0
    beta_unit_checks = 0
    frobenius_term_equalities = 0
    boundary_equalities = 0
    boundary_unit_checks = 0
    zeros: list[dict[str, int]] = []
    zero_count = 0
    first_rows: list[dict[str, int]] = []
    digest = hashlib.sha256()

    for p in primes_up_to(bound):
        if p < 5:
            continue
        n = (p - 1) // 2
        q = p // 6
        terms, prefixes = h_prefixes_mod(p, q)
        inv2 = pow(2, -1, p)
        power = 1
        for j in range(q + 1):
            rhs = math.comb(n, j) % p * power % p
            assert terms[j] == rhs
            frobenius_term_equalities += 1
            power = power * (-inv2) % p

        boundaries, unit_count = fixed_cutoff_boundaries(p, q)
        boundary_unit_checks += unit_count
        h_q = terms[q]
        h_q_prefix = prefixes[q]
        assert h_q != 0

        for r, s in actual_rows_for_prime(p):
            m = s - 1
            d = r + 4
            assert p == 6 * m + 2 * d + 1
            assert n == 3 * m + d
            if p % 6 == 1:
                assert r % 3 == 2
                delta = (r + 4) // 3
            else:
                assert r % 3 == 1
                delta = (r + 2) // 3
            assert q - m == delta and 1 <= delta <= q

            predicted = (h_q_prefix - h_q * boundaries[delta]) % p
            direct = prefixes[m]
            assert predicted == direct
            boundary_equalities += 1

            if p <= identity_bound:
                beta, checks = beta_value_mod(p, r, m)
                assert beta == direct
                beta_equalities += 1
                beta_unit_checks += checks

            row = {
                "p": p,
                "r": r,
                "s": s,
                "m": m,
                "d": d,
                "H_m": direct,
                "q": q,
                "delta": delta,
                "H_q": h_q_prefix,
                "h_term_q": h_q,
                "B_delta": boundaries[delta],
            }
            digest.update(
                json.dumps(row, sort_keys=True, separators=(",", ":")).encode()
            )
            rows += 1
            if len(first_rows) < 8:
                first_rows.append(row)
            if direct == 0:
                zero_count += 1
                if len(zeros) < 20:
                    zeros.append({"p": p, "r": r, "s": s, "m": m})

    return {
        "prime_bound": bound,
        "incomplete_beta_replay_prime_bound": identity_bound,
        "actual_rows": rows,
        "frobenius_term_equalities": frobenius_term_equalities,
        "incomplete_beta_equalities": beta_equalities,
        "incomplete_beta_unit_checks": beta_unit_checks,
        "fixed_cutoff_boundary_equalities": boundary_equalities,
        "fixed_cutoff_ratio_unit_checks": boundary_unit_checks,
        "H_m_zero_count": zero_count,
        "H_m_zero_witnesses_first_20": zeros,
        "first_rows": first_rows,
        "row_digest_sha256": digest.hexdigest(),
        "scope": "EXACT FINITE ONLY; no inference outside the stated bound",
    }


def character_audit(bound: int) -> dict[str, object]:
    primes = 0
    rows = 0
    polynomial_coefficients = 0
    pointwise_c_equalities = 0
    mellin_equalities = 0
    greene_split_equalities = 0
    jacobi_unit_equalities = 0
    sixth_power_equalities = 0
    order_lower_bound_equalities = 0
    residue_phase_equalities = 0
    punctured_elliptic_rational_equalities = 0
    first_rows: list[dict[str, int]] = []

    for p in primes_up_to(bound):
        if p < 11:
            continue
        prime_rows = list(actual_rows_for_prime(p))
        if not prime_rows:
            continue
        primes += 1
        n = (p - 1) // 2
        epsilon = pow(2, n, p)
        assert epsilon in (1, p - 1)
        terms, prefixes = h_prefixes_mod(p, n)
        assert prefixes[n] == epsilon

        # (1-z)C(z)=Q(z)-epsilon*z^(n+1), including both endpoints.
        for k in range(n + 2):
            left = 0
            if k <= n:
                left += prefixes[k]
            if 1 <= k <= n + 1:
                left -= prefixes[k - 1]
            right = terms[k] if k <= n else -epsilon
            assert left % p == right % p
            polynomial_coefficients += 1
        assert sum(prefixes) % p == 0  # C(1)=0.

        inv2 = pow(2, -1, p)
        c_values: dict[int, int] = {}
        for x in range(1, p):
            polynomial = 0
            for coefficient in reversed(prefixes):
                polynomial = (polynomial * x + coefficient) % p
            if x == 1:
                pointwise = 0
            else:
                numerator = (
                    chi(1 - x * inv2, p)
                    - epsilon * x * chi(x, p)
                ) % p
                pointwise = numerator * pow(1 - x, -1, p) % p
            assert polynomial == pointwise
            c_values[x] = pointwise
            pointwise_c_equalities += 1

        for r, s in prime_rows:
            m = s - 1
            d = r + 4
            a = n - m + 1
            assert a == 2 * m + d + 1
            assert 1 <= a <= p - 2

            mellin = 0
            three_point = 0
            jacobi = 0
            for x in range(1, p):
                theta = pow(x, -m, p)
                mellin += theta * c_values[x]
                if x != 1:
                    inverse = pow(1 - x, -1, p)
                    three_point += (
                        theta * chi(1 - x * inv2, p) * inverse
                    )
                    jacobi += theta * x * chi(x, p) * inverse
                    assert pow(theta, 6, p) == pow(x, 2 * r + 8, p)
                    sixth_power_equalities += 1
            direct = prefixes[m]
            assert (-mellin) % p == direct
            mellin_equalities += 1
            assert jacobi % p == a % p
            jacobi_unit_equalities += 1
            assert (-three_point + epsilon * jacobi) % p == direct
            greene_split_equalities += 1

            if p % 6 == 1:
                q = (p - 1) // 6
                delta = (r + 4) // 3
                assert m == q - delta
                localized = 0
                for x in range(1, p):
                    rho = pow(x, q, p)
                    assert pow(rho, 6, p) == 1
                    phase = pow(x, delta, p) * pow(rho, -1, p) % p
                    assert phase == pow(x, -m, p)
                    if x != 1:
                        localized += (
                            phase
                            * chi(1 - x * inv2, p)
                            * pow(1 - x, -1, p)
                        )
                assert localized % p == three_point % p
                residue_phase_equalities += 1
            else:
                assert p % 6 == 5
                # The cube map is a permutation.  The first Greene term
                # becomes a punctured rational moment on
                # y^2=x(1-x^3/2), birational to Y^2=X^3-1/2.
                localized = 0
                rational = 0
                for x in range(1, p):
                    if x == 1:
                        continue
                    denominator = 1 - pow(x, 3, p)
                    assert denominator % p != 0
                    inverse = pow(denominator, -1, p)
                    localized += (
                        pow(x, r + 4, p)
                        * chi(x * (1 - pow(x, 3, p) * inv2), p)
                        * inverse
                    )
                    rational += pow(x, r + 7, p) * inverse
                assert localized % p == three_point % p
                assert rational % p == a % p
                assert (-localized + epsilon * rational) % p == direct
                residue_phase_equalities += 1
                punctured_elliptic_rational_equalities += 1

            order = (p - 1) // math.gcd(m, p - 1)
            assert math.gcd(m, p - 1) == math.gcd(m, 2 * r + 8)
            assert order * (2 * r + 8) >= p - 1
            order_lower_bound_equalities += 1
            rows += 1
            if len(first_rows) < 10:
                first_rows.append(
                    {
                        "p": p,
                        "r": r,
                        "s": s,
                        "m": m,
                        "H_m": direct,
                        "three_point_Greene_reduction": three_point % p,
                        "explicit_Jacobi_reduction": jacobi % p,
                        "theta_order": order,
                    }
                )

    return {
        "prime_bound": bound,
        "primes_with_actual_rows": primes,
        "actual_rows": rows,
        "prefix_polynomial_coefficient_equalities": polynomial_coefficients,
        "pointwise_C_equalities": pointwise_c_equalities,
        "Mellin_coefficient_equalities": mellin_equalities,
        "three_point_Greene_split_equalities": greene_split_equalities,
        "explicit_Jacobi_unit_equalities": jacobi_unit_equalities,
        "theta_sixth_power_point_equalities": sixth_power_equalities,
        "theta_order_lower_bound_equalities": order_lower_bound_equalities,
        "residue_phase_localization_equalities": residue_phase_equalities,
        "p_mod_6_eq_5_punctured_elliptic_rational_equalities": (
            punctured_elliptic_rational_equalities
        ),
        "first_rows": first_rows,
        "scope": "EXACT FINITE ONLY replay of the proved character formulas",
    }


def numerator_height_audit(bound: int) -> dict[str, object]:
    checks = 0
    first_rows: list[dict[str, object]] = []
    for m in range(bound + 1):
        common_numerator = sum(
            math.comb(2 * j, j) * 8 ** (m - j) for j in range(m + 1)
        )
        binary_weight = m.bit_count()
        if common_numerator == 0:
            valuation = 10**9
        else:
            valuation = (common_numerator & -common_numerator).bit_length() - 1
        assert valuation == binary_weight
        reduced_numerator = common_numerator >> binary_weight
        reduced_denominator = 1 << (3 * m - binary_weight)
        assert math.gcd(reduced_numerator, reduced_denominator) == 1
        assert reduced_numerator * (1 << binary_weight) == common_numerator
        assert reduced_numerator * reduced_denominator > 0
        # H_m<sqrt(2), checked without floating point.
        assert reduced_numerator * reduced_numerator < 2 * (
            reduced_denominator * reduced_denominator
        )
        if len(first_rows) < 10 or m in (43, 64, 128, bound):
            first_rows.append(
                {
                    "m": m,
                    "binary_weight": binary_weight,
                    "reduced_numerator": str(reduced_numerator),
                    "reduced_denominator": str(reduced_denominator),
                }
            )
        checks += 1

    # Two symbolic all-row counterexamples to universal H_m nonvanishing.
    assert sum(math.comb(2 * j, j) * 8 ** (2 - j) for j in range(3)) == 86
    assert 86 // 2 == 43
    common_m4 = sum(math.comb(2 * j, j) * 8 ** (4 - j) for j in range(5))
    assert common_m4 == 5734 and common_m4 // 2 == 2867 == 47 * 61

    return {
        "m_bound": bound,
        "exact_2_adic_and_height_checks": checks,
        "theorem_replayed": (
            "v2(U_m)=s_2(m), so H_m=N_m/2^(3m-s_2(m)) in lowest terms; "
            "for any distinct odd zero primes Z_m, sum_(p in Z_m) log p "
            "<=log N_m<(3m-s_2(m)+1/2)log 2"
        ),
        "asymptotic_container_ceiling_per_6m": "log(2)/2 (positive, not zero)",
        "exact_counterexamples": [
            {"p": 43, "r": 11, "s": 3, "m": 2, "H_m": "43/32"},
            {"p": 47, "r": 7, "s": 5, "m": 4, "H_m": "2867/2048=47*61/2048"},
        ],
        "first_rows": first_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=5000)
    parser.add_argument("--character-bound", type=int, default=251)
    parser.add_argument("--identity-bound", type=int, default=601)
    parser.add_argument("--numerator-bound", type=int, default=256)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item254_half_binomial_arithmetic_certificate.json",
    )
    args = parser.parse_args()

    assert args.bound >= 47
    assert 11 <= args.character_bound <= args.bound
    assert 11 <= args.identity_bound <= args.bound
    assert args.numerator_bound >= 4

    payload = {
        "schema": "item254-half-binomial-arithmetic-certificate-v1",
        "imports_item_code": False,
        "theorems": {
            "prefix_polynomial": (
                "(1-z)C_p(z)=(1-z/2)^((p-1)/2)-epsilon_2*z^((p+1)/2), "
                "C_p(z)=sum_(k=0)^((p-1)/2) H_k z^k, C_p(1)=0"
            ),
            "Mellin_period": (
                "H_m=-sum_(x in F_p^*) x^(-m) C_p(x), with "
                "(x^(-m))^6=x^(2r+8)"
            ),
            "Greene_split": (
                "H_m=-T_p+epsilon_2*J_p, where T_p is the three-point "
                "Teichmuller/Greene sum and J_p=n-m+1 is a p-unit modulo p"
            ),
            "residue_phase_localization": (
                "for p=1 mod 6, x^(-m)=x^delta*rho^(-1)(x) with rho sextic; "
                "for p=5 mod 6, cube substitution localizes T_p to a "
                "punctured rational moment on y^2=x(1-x^3/2)"
            ),
            "incomplete_beta": (
                "H_m=2^(-m)(2m+d)binom(3m+d,m) "
                "integral_0^1 u^(2m+d-1)(1-2u)^m du mod p, d=r+4"
            ),
            "fixed_cutoff": (
                "H_m=H_floor(p/6)-h_floor(p/6)*B_delta mod p, with a "
                "fixed-length rational B_delta for fixed r"
            ),
            "weighted_zero_container": (
                "sum_(p in Z_m) log p < (3m-s_2(m)+1/2)log 2"
            ),
        },
        "coefficient_and_row_audit": coefficient_and_row_audit(
            args.bound, args.identity_bound
        ),
        "character_audit": character_audit(args.character_bound),
        "numerator_height_audit": numerator_height_audit(args.numerator_bound),
        "OPEN": [
            "a transformation of the moving high-order three-point Greene period to a bounded-order invariant",
            "a zero weighted-rate theorem for the actual moving row family",
            "all-prime or zero-rate control of the full Item 251 gate rather than H_m alone",
            "any Route-1 capacity reduction or conclusion about e+pi",
        ],
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
