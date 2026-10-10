#!/usr/bin/env python3
"""Exact certificate for the quartic power-kernel Hermite reduction."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial, gcd
from pathlib import Path

import sympy as sp


def v2(z: int) -> int:
    if z == 0:
        raise ValueError("v2(0) is infinite")
    z = abs(z)
    return (z & -z).bit_length() - 1


def popcount(z: int) -> int:
    return z.bit_count()


def raw_coordinate_numerators(n: int, k: int) -> tuple[int, int, int, int]:
    """Coordinates with common (not reduced) denominator 4^(k-1)(k-1)! ."""
    out = [0, 0, 0, 0]
    for j in range(n + 1):
        m = n + j
        prod = 1
        for s in range(1, k):
            prod *= 4 * s - m - 1
        r = m % 4
        out[r] += (-1) ** (j + (m - r) // 4) * comb(n, j) * prod
    return tuple(out)


def raw_coordinate_rows(
    n: int, k_max: int
) -> list[tuple[int, int, int, int]]:
    """All raw coordinate rows for 1 <= k <= k_max in one product pass."""
    products = [1] * (n + 1)
    rows: list[tuple[int, int, int, int]] = []
    signed_binomials = []
    residues = []
    for j in range(n + 1):
        m = n + j
        r = m % 4
        residues.append(r)
        signed_binomials.append((-1) ** (j + (m - r) // 4) * comb(n, j))
    for k in range(1, k_max + 1):
        out = [0, 0, 0, 0]
        for j in range(n + 1):
            out[residues[j]] += signed_binomials[j] * products[j]
        rows.append(tuple(out))
        for j in range(n + 1):
            products[j] *= 4 * k - (n + j) - 1
    return rows


def coordinates(n: int, k: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    den = 4 ** (k - 1) * factorial(k - 1)
    return tuple(Fraction(z, den) for z in raw_coordinate_numerators(n, k))


def monomial_reduction(m: int, k: int) -> tuple[Fraction, Fraction]:
    """Return A_mk and H_mk(1) from equations (4) and (8)."""
    scale = Fraction(1)
    endpoint = Fraction(0)
    for j in range(k, 1, -1):
        endpoint += scale * Fraction(1, 4 * (j - 1) * 2 ** (j - 1))
        scale *= Fraction(4 * j - m - 5, 4 * (j - 1))
    return scale, endpoint


def polynomial_integral(m: int) -> Fraction:
    q, r = divmod(m, 4)
    return sum(
        (Fraction((-1) ** u, r + 4 * (q - 1 - u) + 1) for u in range(q)),
        Fraction(0),
    )


def rational_and_coordinates(
    n: int, k: int
) -> tuple[Fraction, tuple[Fraction, Fraction, Fraction, Fraction]]:
    out = [Fraction(0) for _ in range(4)]
    rational = Fraction(0)
    for j in range(n + 1):
        m = n + j
        p = (-1) ** j * comb(n, j)
        multiplier, endpoint = monomial_reduction(m, k)
        q, r = divmod(m, 4)
        out[r] += p * multiplier * (-1) ** q
        rational += p * (endpoint + multiplier * polynomial_integral(m))
    return rational, tuple(out)


def scan_log_free(n_max: int, k_max: int) -> list[list[int]]:
    found: list[list[int]] = []
    for n in range(n_max + 1):
        for k, out in enumerate(raw_coordinate_rows(n, k_max), start=1):
            if out[3] == 0 and out[0] == out[2]:
                found.append([n, k])
    return found


def expected_pairs(n_max: int, k_max: int) -> list[list[int]]:
    out: set[tuple[int, int]] = {(3, 2)}
    for n in range(6, n_max + 1, 8):
        if 1 <= k_max:
            out.add((n, 1))
    j = 0
    while True:
        n, k = 4 * j + 2, 3 * j + 2
        if n > n_max:
            break
        if k <= k_max:
            out.add((n, k))
        j += 1
    return [list(z) for z in sorted(out)]


def verify_symbolic_identity() -> bool:
    x, m, j = sp.symbols("x m j")
    q = 1 + x**4
    a = (4 * j - m - 5) / (4 * (j - 1))
    # This is (6), divided by x^m/Q^j.  Writing it this way avoids
    # assumptions about simplification of symbolic integer powers.
    normalized_rhs = a * q + (
        (m + 1) * q - 4 * (j - 1) * x**4
    ) / (4 * (j - 1))
    return sp.simplify(normalized_rhs - 1) == 0


def verify_small_against_sympy() -> bool:
    x = sp.symbols("x")
    q = x**4 + 1
    # Keep this deliberately small: it is an independent symbolic
    # reconstruction, while the all-parameter proof is (6)--(12).
    for n in range(0, 5):
        for k in range(1, 4):
            f = x**n * (1 - x) ** n / q**k
            primitive = 0
            omega = 0
            for ell in range(n + 1):
                m = n + ell
                p = (-1) ** ell * comb(n, ell)
                scale = sp.Rational(1)
                hermite = 0
                for jj in range(k, 1, -1):
                    hermite += (
                        scale
                        * x ** (m + 1)
                        / (4 * (jj - 1) * q ** (jj - 1))
                    )
                    scale *= sp.Rational(4 * jj - m - 5, 4 * (jj - 1))
                qq, r = divmod(m, 4)
                polynomial_primitive = 0
                for u in range(qq):
                    exponent = r + 4 * (qq - 1 - u)
                    polynomial_primitive += (
                        (-1) ** u * x ** (exponent + 1) / (exponent + 1)
                    )
                primitive += p * (hermite + scale * polynomial_primitive)
                omega += p * scale * (-1) ** qq * x**r
            numerator = sp.together(f - sp.diff(primitive, x) - omega / q).as_numer_denom()[0]
            if sp.Poly(sp.expand(numerator), x).as_expr() != 0:
                return False
    return True


def verify_denominators(m_max: int, k_max: int) -> bool:
    for m in range(m_max + 1):
        for k in range(1, k_max + 1):
            a, _ = monomial_reduction(m, k)
            K = k - 1
            if m % 2 == 0:
                expected = 2 ** (2 * K + v2(factorial(K))) if K else 1
            elif m % 4 == 1:
                expected = 2 ** (K + v2(factorial(K))) if K else 1
            else:
                expected = 1
            if a.denominator != expected:
                return False
    return True


def balanced_denominator_check(j_max: int) -> list[dict[str, int]]:
    records: list[dict[str, int]] = []
    for j in range(j_max + 1):
        n, k = 4 * j + 2, 3 * j + 2
        a = coordinates(n, k)[0]
        exponent = 5 * j + 2 + v2(factorial(3 * j + 1))
        if a.denominator != 2**exponent or a.numerator % 2 == 0:
            raise AssertionError((j, a, exponent))
        records.append(
            {
                "j": j,
                "n": n,
                "k": k,
                "denominator_exponent": exponent,
            }
        )
    return records


def adjacent_determinant_scan(n_max: int, k_max: int) -> dict[str, object]:
    zero_pairs: list[list[int]] = []
    valuation_failures: list[dict[str, int]] = []
    count = 0
    for n in range(2, n_max + 1, 2):
        rows = raw_coordinate_rows(n, k_max + 1)
        for k in range(n // 2 + 1, k_max + 1):
            a, _, c, _ = rows[k - 1]
            ap, _, cp, _ = rows[k]
            determinant = 2 * (ap * c - cp * a)
            count += 1
            if determinant == 0:
                zero_pairs.append([n, k])
                continue
            # This stable valuation is diagnostic, not used as an all-n theorem.
            if n % 4 == 0:
                q = n // 4
                expected = n // 2 + 2 + v2(q)
            else:
                expected = (n - 2) // 2 + 2
            if v2(determinant) != expected:
                valuation_failures.append(
                    {
                        "n": n,
                        "k": k,
                        "observed": v2(determinant),
                        "expected": expected,
                    }
                )
    return {
        "pairs_checked": count,
        "zero_pairs": zero_pairs,
        "valuation_failures": valuation_failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "quartic_power_kernel_hermite_certificate.json",
    )
    parser.add_argument("--n-max", type=int, default=160)
    parser.add_argument("--k-max", type=int, default=160)
    args = parser.parse_args()

    symbolic = verify_symbolic_identity()
    small_crosscheck = verify_small_against_sympy()
    denominator_check = verify_denominators(80, 80)
    found = scan_log_free(args.n_max, args.k_max)
    expected = expected_pairs(args.n_max, args.k_max)
    balanced = balanced_denominator_check(40)
    adjacent = adjacent_determinant_scan(160, 160)

    if not symbolic or not small_crosscheck or not denominator_check:
        raise AssertionError("an exact identity check failed")
    if found != expected:
        raise AssertionError((found, expected))
    if adjacent["zero_pairs"] or adjacent["valuation_failures"]:
        raise AssertionError(adjacent)

    sqrt5 = sp.sqrt(5)
    y0 = (3 + sqrt5) / 2
    x0 = sp.N((y0 - sp.sqrt(y0**2 - 4)) / 2, 50)
    rho = sp.N(
        x0 * (1 - x0) / (1 + x0**4) ** sp.Rational(3, 4), 50
    )

    result = {
        "schema": "quartic-power-kernel-hermite-certificate-v1",
        "parameters": {"n_max": args.n_max, "k_max": args.k_max},
        "symbolic_differential_identity": symbolic,
        "small_sympy_hermite_crosscheck": small_crosscheck,
        "monomial_denominator_check_m80_k80": denominator_check,
        "log_free_pairs": found,
        "log_free_pair_count": len(found),
        "classification_matches_three_reported_families_in_box": found == expected,
        "balanced_denominator_check": {
            "j_max": 40,
            "all_match": True,
            "last_record": balanced[-1],
        },
        "adjacent_pi_determinant": adjacent,
        "balanced_saddle": {"x0": str(x0), "rho": str(rho)},
        "warnings": [
            "The bounded scans are diagnostics, not all-parameter proofs.",
            "The global completeness of the three displayed log-free families remains conjectural.",
            "The adjacent-determinant valuation pattern is certified only in the displayed finite box.",
            "Nothing in this result classifies e+pi.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
