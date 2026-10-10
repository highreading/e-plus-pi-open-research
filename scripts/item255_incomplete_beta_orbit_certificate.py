#!/usr/bin/env python3
"""Portable exact checker for Item 255's incomplete-beta orbit.

The checker uses only Python's standard library.  It verifies exact rational
identities, endpoint terms, modular reflection, the phase-singular 2x2
system, and denominator ranges.  Bounded counts are evidence only.
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
                m = s - 1
                d = r + 4
                assert p == 6 * m + 2 * d + 1
                assert d >= 5 and d % 6 in (3, 5)
                yield p, r, s, m, d


def moment(m: int, d: int, c: F, q: int = 0) -> F:
    a = 2 * m + d + q
    return sum((F(math.comb(m, k), a + k) * c**k for k in range(m + 1)), F(0))


def k_diagonal(m: int, d: int) -> F:
    n = 3 * m + d
    return sum((F((-1) ** k * math.comb(n, k), 2**k) for k in range(m + 1)), F(0))


def frac_mod(value: F, p: int) -> int:
    denominator = value.denominator % p
    assert denominator != 0
    return value.numerator % p * pow(denominator, -1, p) % p


def affine_iteration(m: int, d: int, c: F) -> tuple[F, F]:
    length = m + 1
    a = 2 * m + d
    b = 3 * m + d + 1
    endpoint = (1 + c) ** length
    multiplier = F(1)
    affine = F(0)
    for q in range(length):
        lam = -F(a + q, 1) / (c * (b + q))
        mu = endpoint / (c * (b + q))
        multiplier = lam * multiplier
        affine = lam * affine + mu
    return multiplier, affine


def exact_identity_audit() -> dict[str, object]:
    beta_checks = 0
    contiguous_checks = 0
    iteration_checks = 0
    rows = []
    for m in range(0, 13):
        for d in range(3, 22, 2):
            n = 3 * m + d
            i_value = moment(m, d, F(-2))
            left = 2**m * k_diagonal(m, d)
            right = (2 * m + d) * math.comb(n, m) * i_value
            assert left == right
            beta_checks += 1

            for c in (F(-2), F(-1, 2), F(3, 2)):
                for q in range(0, min(m + 1, 5)):
                    lhs = (2 * m + d + q) * moment(m, d, c, q)
                    lhs += c * (3 * m + d + q + 1) * moment(m, d, c, q + 1)
                    assert lhs == (1 + c) ** (m + 1)
                    contiguous_checks += 1
                multiplier, affine = affine_iteration(m, d, c)
                assert moment(m, d, c, m + 1) == multiplier * moment(m, d, c) + affine
                expected_multiplier = (
                    (-F(1, 1) / c) ** (m + 1)
                    * F(math.prod(range(2 * m + d, 3 * m + d + 1)))
                    / F(math.prod(range(3 * m + d + 1, 4 * m + d + 2)))
                )
                assert multiplier == expected_multiplier
                iteration_checks += 1
            rows.append((m, d, i_value.numerator, i_value.denominator))

    digest = hashlib.sha256(
        "".join(f"{m},{d},{a},{b}\n" for m, d, a, b in rows).encode("ascii")
    ).hexdigest()
    return {
        "beta_localization_equalities": beta_checks,
        "contiguous_endpoint_equalities": contiguous_checks,
        "full_iteration_equalities": iteration_checks,
        "row_digest_sha256": digest,
    }


def h_prefix_mod(m: int, p: int) -> int:
    term = 1
    total = 1
    for j in range(m):
        term = term * (2 * j + 1) * pow(4 * (j + 1), -1, p) % p
        total = (total + term) % p
    return total


def modular_row(p: int, r: int, s: int, m: int, d: int) -> dict[str, int | bool]:
    n = 3 * m + d
    length = m + 1
    assert n == (p - 1) // 2 < p
    assert 0 <= m <= n

    h_value = h_prefix_mod(m, p)
    k_value = frac_mod(k_diagonal(m, d), p)
    assert h_value == k_value
    i_value = frac_mod(moment(m, d, F(-2)), p)
    prefactor = (
        pow(2, m, p)
        * pow((2 * m + d) * (math.comb(n, m) % p), -1, p)
    ) % p
    assert i_value == prefactor * k_value % p
    assert (i_value == 0) == (h_value == 0)

    c = F(-2)
    c_inv = 1 / c
    x = frac_mod(moment(m, d, c), p)
    y = frac_mod(moment(m, d, c_inv), p)
    x_shift = frac_mod(moment(m, d, c, length), p)
    y_shift = frac_mod(moment(m, d, c_inv, length), p)
    c_mod = frac_mod(c, p)
    c_inv_mod = pow(c_mod, -1, p)
    assert x_shift == -pow(c_mod, m, p) * y % p
    assert y_shift == -pow(c_inv_mod, m, p) * x % p

    a_c, e_c = affine_iteration(m, d, c)
    a_inv, e_inv = affine_iteration(m, d, c_inv)
    a_c_mod = frac_mod(a_c, p)
    a_inv_mod = frac_mod(a_inv, p)
    e_c_mod = frac_mod(e_c, p)
    e_inv_mod = frac_mod(e_inv, p)
    assert x_shift == (a_c_mod * x + e_c_mod) % p
    assert y_shift == (a_inv_mod * y + e_inv_mod) % p
    assert a_c_mod == pow(c_mod, -length, p)
    assert a_inv_mod == pow(c_mod, length, p)
    assert e_inv_mod == c_mod * e_c_mod % p

    matrix = (
        pow(c_mod, -length, p),
        pow(c_mod, m, p),
        pow(c_mod, -m, p),
        pow(c_mod, length, p),
    )
    determinant = (matrix[0] * matrix[3] - matrix[1] * matrix[2]) % p
    assert determinant == 0
    assert matrix[2] == c_mod * matrix[0] % p
    assert matrix[3] == c_mod * matrix[1] % p

    # Exact characteristic-zero determinant is nonzero and negative.
    exact_det = a_c * a_inv - 1
    assert exact_det < 0
    det_quotient = exact_det / p
    harmonic = sum((F(1, 2 * m + d + t) for t in range(length)), F(0))
    assert frac_mod(det_quotient, p) == 2 * frac_mod(harmonic, p) % p

    # Unit ranges for every q,k in the orbit.
    assert 0 < 2 * m + d
    assert 4 * m + d + 1 < p
    for q in range(length):
        assert 0 < 3 * m + d + q + 1 < p
        for k in range(m + 1):
            assert 0 < 2 * m + d + q + k < p
    for k in range(m + 1):
        assert 0 < 2 * m + d + length + k <= 4 * m + d + 1 < p

    return {
        "p": p,
        "r": r,
        "s": s,
        "m": m,
        "d": d,
        "H_m": h_value,
        "I_m_d": i_value,
        "reciprocal_companion": y,
        "A_minus_2": a_c_mod,
        "A_minus_half": a_inv_mod,
        "E_minus_2": e_c_mod,
        "E_minus_half": e_inv_mod,
        "matrix_determinant": determinant,
        "characteristic_zero_determinant_sign": -1,
        "first_Hasse_determinant_quotient": frac_mod(det_quotient, p),
        "harmonic_interval": frac_mod(harmonic, p),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=601)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item255_incomplete_beta_orbit_certificate.json",
    )
    args = parser.parse_args()
    assert args.bound >= 43

    exact = exact_identity_audit()
    rows = [modular_row(*values) for values in actual_rows(args.bound)]
    zeros = [
        {key: row[key] for key in ("p", "r", "s", "m", "d", "reciprocal_companion")}
        for row in rows
        if row["I_m_d"] == 0
    ]
    harmonic_zeros = [
        {key: row[key] for key in ("p", "r", "s", "m", "d")}
        for row in rows
        if row["harmonic_interval"] == 0
    ]
    witness = next(row for row in rows if row["p"] == 43 and row["r"] == 11 and row["s"] == 3)
    assert witness["H_m"] == witness["I_m_d"] == 0
    assert witness["reciprocal_companion"] != 0
    hasse_witness = next(
        row for row in rows if row["p"] == 23 and row["r"] == 1 and row["s"] == 3
    )
    assert hasse_witness["harmonic_interval"] == 0
    hasse_a, _ = affine_iteration(2, 5, F(-2))
    hasse_b, _ = affine_iteration(2, 5, F(-1, 2))
    hasse_det = hasse_a * hasse_b - 1
    hasse_numerator = abs(hasse_det.numerator)
    hasse_valuation = 0
    while hasse_numerator % 23 == 0:
        hasse_numerator //= 23
        hasse_valuation += 1
    assert hasse_valuation == 2

    digest = hashlib.sha256(
        "".join(
            f"{row['p']},{row['r']},{row['s']},{row['m']},{row['d']},"
            f"{row['H_m']},{row['I_m_d']},{row['reciprocal_companion']},"
            f"{row['A_minus_2']},{row['A_minus_half']},{row['E_minus_2']},"
            f"{row['E_minus_half']},{row['first_Hasse_determinant_quotient']},"
            f"{row['harmonic_interval']}\n"
            for row in rows
        ).encode("ascii")
    ).hexdigest()

    result = {
        "schema": "item255-incomplete-beta-orbit-certificate-v1",
        "imports_item_code": False,
        "theorems": {
            "beta_localization": (
                "2^m K_(d,m)=(2m+d)C(3m+d,m)I_(m,d), "
                "I=int_0^1 u^(2m+d-1)(1-2u)^m du"
            ),
            "phase_zero_equivalence": "H_m=0 mod p iff I_(m,d)=0 mod p",
            "contiguous_recurrence": (
                "(2m+d+q)M_q(c)+c(3m+d+q+1)M_(q+1)(c)=(1+c)^(m+1)"
            ),
            "endpoint_for_c_minus_2": "(-1)^(m+1), retained exactly",
            "phase_reflection": "M_(m+1)(c)=-c^m M_0(c^(-1)) mod p",
            "homogeneous_multiplier": "A_c=c^(-(m+1)) mod p",
            "reciprocal_orbit_matrix": "[[c^(-L),c^m],[c^(-m),c^L]], L=m+1",
            "matrix_rank": 1,
            "affine_compatibility": "E_(c^(-1))=c E_c mod p",
            "first_Hasse_lift": (
                "(R^2-1)/p=2*sum_(t=0)^m 1/(2m+d+t) mod p, "
                "R=(2m+d)_(m+1)/(3m+d+1)_(m+1)"
            ),
            "scoped_no_go": (
                "the reciprocal pair plus first contiguous orbit gives no second condition "
                "on I, H_m, or an affine H_m target"
            ),
        },
        "exact_identity_audit": exact,
        "unit_audit": {
            "all_moment_denominators_are_p_units": True,
            "moment_bound": "2m+d+q+k<=4m+d<p for 0<=q,k<=m",
            "contiguous_bound": "3m+d+q+1<=4m+d+1<p",
            "factorial_bound": "m<=n=(p-1)/2<p",
            "endpoint_at_u_1_retained": True,
            "endpoint_at_u_0_zero_by_positive_exponent": True,
        },
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.bound,
            "actual_rows": len(rows),
            "rank_one_matrix_rows": len(rows),
            "H_and_I_zero_count": len(zeros),
            "zero_witnesses_first_12": zeros[:12],
            "harmonic_interval_zero_count": len(harmonic_zeros),
            "harmonic_interval_zero_witnesses_first_12": harmonic_zeros[:12],
            "first_rows": rows[:8],
            "row_digest_sha256": digest,
            "scope": "bounded exact replay only; no density or rate inference",
        },
        "separation_witness": witness,
        "first_Hasse_nonunit_witness": {
            "row": hasse_witness,
            "harmonic_interval_exact": "1/9+1/10+1/11=299/990",
            "characteristic_zero_determinant": str(hasse_det),
            "determinant_numerator_v_23": hasse_valuation,
        },
        "OPEN": [
            "all-prime or weighted control of the moving first-Hasse harmonic interval",
            "a derivative-jet or independent period condition beyond it on I or the actual gate",
            "any weighted zero theorem, divisibility exponent, capacity reduction, or e+pi conclusion",
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
