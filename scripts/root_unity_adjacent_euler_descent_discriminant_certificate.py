#!/usr/bin/env python3
"""Exact replay for the adjacent-Euler descent/discriminant barrier.

Finite grids below audit identities proved for all parameters in the
companion source.  They are not extrapolated to an asymptotic Euler-gcd
claim or to a classification of e+pi.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import resource
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "sources/root_unity_adjacent_euler_descent_discriminant_barrier.md"
)
OUTPUT = (
    ROOT
    / "results/root_unity_adjacent_euler_descent_discriminant_certificate.json"
)
RSS_GUARD_KIB = 8 * 1024 * 1024

DEPENDENCIES = {
    "sources/root_unity_quadratic_euler_gcd_kummer_obstruction.md":
        "a720ef166a3b772d85c32934782fcfa4d41797b274ea964259973a216bb369ca",
    "sources/root_unity_quadratic_euler_beta_denominator_floor.md":
        "8b22a86eea520400245e5529809da2dcce56cbfb26c9836677e23ccd0a197a0a",
    "sources/root_unity_quadratic_two_regime_canonical_no_go.md":
        "697f3b29d899a3dd229b6b7b9748ec77c74d60d603fb67ea5e7f10fef56cfdb3",
    "results/root_unity_quadratic_euler_gcd_kummer_hashes.sha256":
        "74b79cee3b86e5fe37700e1db68ed91976a56c01a783c1e10d5e13651d82ba49",
    "results/root_unity_quadratic_euler_beta_denominator_hashes.sha256":
        "22fba2af00e25aa5a956b923e490d2a853dd170ab2292178190bb5a1507d6f1d",
    "results/root_unity_quadratic_two_regime_canonical_hashes.sha256":
        "398c9b03759673e2e0cce91e52abe74bf2a70b098f546158c8e972fba6de4398",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    bad = [
        {"offset": i, "byte": byte}
        for i, byte in enumerate(data)
        if byte < 32 and byte != 10
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": bad,
        "clean": not bad,
    }


def valuation(number: int, prime: int) -> int:
    assert number
    number = abs(number)
    result = 0
    while number % prime == 0:
        result += 1
        number //= prime
    return result


def euler_even(limit: int) -> list[int]:
    """Return E_0,E_2,...,E_{2*limit} in the sech convention."""
    values = [1]
    for n in range(1, limit + 1):
        values.append(
            -sum(math.comb(2 * n, 2 * j) * values[j] for j in range(n))
        )
    return values


def reduced_q(n: int, values: list[int]) -> tuple[int, int]:
    raw_q = (2 * n + 2) * (2 * n + 1) * abs(values[n])
    raw_p = abs(values[n + 1])
    common = math.gcd(raw_q, raw_p)
    return raw_q // common, common


def off_index_part(number: int, forbidden: int) -> tuple[int, dict[int, int]]:
    factors = {int(p): int(a) for p, a in sp.factorint(number).items()}
    off = 1
    for prime, exponent in factors.items():
        if forbidden % prime:
            off *= prime**exponent
    return off, factors


def main() -> None:
    dependency_checks = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependency_checks[relative] = {"expected": expected, "actual": actual}

    # Exhaustive formal-prime valuation ledger.  The five coordinates are
    # b,c,x,y,z from equation (5) of the source.
    valuation_cases = 0
    positive_cases = 0
    off_index_cases = 0
    for b in range(7):
        for c in range(7):
            for x in range(7):
                for y in range(7):
                    for z in range(7):
                        q0 = max(b + x - y, 0)
                        q1 = max(c + y - z, 0)
                        t = min(q0, q1)
                        assert 2 * t <= b + c + x
                        if t:
                            assert 2 * t <= b + c + x - z
                            positive_cases += 1
                        if b == c == 0:
                            assert (t > 0) == (x > y > z)
                            assert 2 * t <= x
                            off_index_cases += 1
                        valuation_cases += 1

    # Exact Euler rows check the global and off-index square divisibilities,
    # the valuation formulas, and the exact dyadic contribution.
    row_max = 100
    values = euler_even(max(row_max + 2, 74))
    selected_rows = []
    odd_off_support_rows = []
    for n in range(1, row_max + 1):
        q0, g0 = reduced_q(n, values)
        q1, g1 = reduced_q(n + 1, values)
        h = math.gcd(q0, q1)
        a0 = (2 * n + 2) * (2 * n + 1)
        a1 = (2 * n + 4) * (2 * n + 3)
        off, factors = off_index_part(h, a0 * a1)

        assert (a0 * a1 * abs(values[n])) % (h * h) == 0
        assert abs(values[n]) % (off * off) == 0
        assert valuation(h, 2) == 1

        primes = set(factors)
        primes.update(int(p) for p in sp.factorint(a0 * a1))
        for prime in primes:
            b = valuation(a0, prime)
            c = valuation(a1, prime)
            x = valuation(values[n], prime)
            y = valuation(values[n + 1], prime)
            z = valuation(values[n + 2], prime)
            expected = min(max(b + x - y, 0), max(c + y - z, 0))
            assert valuation(h, prime) == expected
            if (a0 * a1) % prime and expected:
                assert x > y > z
                assert x >= 2 and y >= 1

        if off > 1:
            odd_off_support_rows.append({
                "N": n,
                "h_N": str(h),
                "h_off": str(off),
                "factorization_h": {str(p): a for p, a in factors.items()},
            })
        if n in (1, 2, 3, 10, 30, 73, 100):
            selected_rows.append({
                "N": n,
                "Q_N": str(q0),
                "Q_N_plus_1": str(q1),
                "G_N": str(g0),
                "G_N_plus_1": str(g1),
                "h_N": str(h),
                "h_off": str(off),
                "factorization_h": {str(p): a for p, a in factors.items()},
            })

    # Nontrivial fourth-order-root audit at the known endpoint pair
    # E_146,E_148.  This avoids constructing an unnecessary degree-148
    # discriminant.
    endpoint_modulus = 149
    assert values[73] % endpoint_modulus == 0
    assert values[74] % endpoint_modulus == 0
    endpoint_t0 = values[74] % endpoint_modulus
    endpoint_t2 = (
        math.comb(148, 2) * values[73]
    ) % endpoint_modulus
    assert endpoint_t0 == endpoint_t2 == 0

    # Centered Euler polynomials, square-coordinate discriminants, and the
    # exact composition identity on a declared degree grid.
    T, Y = sp.symbols("T Y")
    polynomial_rows = []
    polynomial_max_m = 8
    poly_values = euler_even(polynomial_max_m)
    for m in range(2, polynomial_max_m + 1):
        degree = 2 * m
        centered = sp.Poly(
            sum(
                sp.binomial(degree, j)
                * (poly_values[j // 2] if j % 2 == 0 else 0)
                * T ** (degree - j)
                for j in range(degree + 1)
            ),
            T,
            domain=sp.ZZ,
        )
        square_poly = sp.Poly(
            sum(
                sp.binomial(degree, 2 * k)
                * poly_values[m - k]
                * Y**k
                for k in range(m + 1)
            ),
            Y,
            domain=sp.ZZ,
        )
        assert centered.as_expr() == sp.expand(
            square_poly.as_expr().subs(Y, T**2)
        )
        assert square_poly.LC() == 1
        assert square_poly.eval(0) == poly_values[m]
        assert square_poly.diff().eval(0) == (
            math.comb(degree, 2) * poly_values[m - 1]
        )
        assert max(abs(int(c)) for c in square_poly.all_coeffs()) <= (
            math.factorial(degree)
        )

        disc_square = int(sp.discriminant(square_poly.as_expr(), Y))
        disc_centered = int(sp.discriminant(centered.as_expr(), T))
        assert disc_square
        assert disc_centered
        assert disc_centered == (
            (-4) ** m * int(square_poly.eval(0)) * disc_square**2
        )

        common = math.gcd(
            abs(poly_values[m]), abs(poly_values[m - 1])
        )
        assert disc_square % common == 0
        assert disc_centered % (common**3) == 0

        # Squared Hadamard bound from equation (25), kept integral.
        factorial = math.factorial(degree)
        hadamard_squared = (
            (m + 1) ** (m - 1)
            * m ** (3 * m)
            * factorial ** (2 * (2 * m - 1))
        )
        assert disc_square**2 <= hadamard_squared
        polynomial_rows.append({
            "M": degree,
            "degree_f_M": m,
            "gcd_E_M_E_M_minus_2": str(common),
            "disc_f_M_bits": abs(disc_square).bit_length(),
            "disc_centered_bits": abs(disc_centered).bit_length(),
            "composition_identity": True,
            "cubic_divisibility": True,
            "hadamard_squared_bound": True,
        })

    # Level-4 Eisenstein constant and initial coefficients.  The
    # generalized Bernoulli formula is evaluated exactly.
    eisenstein_rows = []
    for n in range(1, 13):
        k = 2 * n + 1
        generalized_bernoulli = 4 ** (k - 1) * (
            sp.bernoulli(k, sp.Rational(1, 4))
            - sp.bernoulli(k, sp.Rational(3, 4))
        )
        l_value = -generalized_bernoulli / k
        assert l_value == sp.Rational(values[n], 2)

        coefficients = {}
        sturm = k // 2
        for index in range(1, sturm + 1):
            coefficient = sum(
                (
                    0 if d % 2 == 0
                    else (1 if d % 4 == 1 else -1)
                )
                * d ** (k - 1)
                for d in sp.divisors(index)
            )
            assert abs(coefficient) <= index**k
            if index <= 3:
                coefficients[str(index)] = str(coefficient)
        assert coefficients["1"] == "1"
        if sturm >= 2:
            assert coefficients["2"] == "1"
        if sturm >= 3:
            assert coefficients["3"] == str(1 - 3 ** (2 * n))
        eisenstein_rows.append({
            "N": n,
            "weight": k,
            "L_1_minus_k": str(l_value),
            "E_2N_over_2": str(sp.Rational(values[n], 2)),
            "constant_term": str(l_value / 2),
            "initial_coefficients": coefficients,
            "sturm_bound": sturm,
        })

    # A finite audit of the distinct adjacent residual eigenvalues.  The
    # all-p proof in the source uses a prime in a residue class not ±1.
    eigenpacket_rows = []
    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        witness = None
        for ell in list(sp.primerange(3, 500)):
            if ell == prime:
                continue
            chi = 1 if ell % 4 == 1 else -1
            left = (1 + chi * pow(ell, 4, prime)) % prime
            right = (1 + chi * pow(ell, 6, prime)) % prime
            if left != right:
                witness = {"ell": ell, "weight_5": left, "weight_7": right}
                break
        assert witness is not None
        eigenpacket_rows.append({"p": prime, **witness})

    source_text = SOURCE.read_text(encoding="utf-8")
    tags = [int(value) for value in re.findall(r"\\tag\{(\d+)\}", source_text)]
    assert tags == list(range(1, 34)), tags
    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__).resolve())
    assert source_control["clean"] and script_control["clean"]
    assert source_text.count(r"\(") == source_text.count(r"\)")
    assert sum(line.strip() == r"\[" for line in source_text.splitlines()) == 33
    assert sum(line.strip() == r"\]" for line in source_text.splitlines()) == 33
    assert "do not bound the first-period factor" in source_text
    assert "no claim here" in source_text

    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_GUARD_KIB, peak_rss_kib

    result = {
        "schema": (
            "root_unity_adjacent_euler_descent_discriminant_certificate/v1"
        ),
        "checked_utc": "2026-08-27",
        "claim_scope": {
            "all_parameter_proofs_in_source": True,
            "finite_grids_are_formula_audits_only": True,
            "bounds_J_N_by_exp_o_N_log_N": False,
            "classification_of_e_plus_pi": False,
        },
        "dependencies": dependency_checks,
        "valuation_ledger": {
            "coordinate_range": [0, 6],
            "cases": valuation_cases,
            "positive_h_cases": positive_cases,
            "off_index_cases": off_index_cases,
            "global_2t_le_b_plus_c_plus_x": True,
            "off_index_strict_descent": True,
        },
        "exact_euler_rows": {
            "N_min": 1,
            "N_max": row_max,
            "global_h_square_divisibility": True,
            "off_index_h_square_divisibility": True,
            "v2_h_is_one": True,
            "selected_rows": selected_rows,
            "rows_with_odd_off_index_support": odd_off_support_rows,
        },
        "fourth_order_endpoint_audit": {
            "M": 148,
            "modulus": endpoint_modulus,
            "constant_coefficient_modulus": endpoint_t0,
            "quadratic_coefficient_modulus": endpoint_t2,
        },
        "centered_polynomial_grid": {
            "M_min": 4,
            "M_max": 2 * polynomial_max_m,
            "rows": polynomial_rows,
        },
        "level4_eisenstein_grid": {
            "N_min": 1,
            "N_max": 12,
            "constant_identity_checked": True,
            "first_nonconstant_coefficient_is_one": True,
            "coefficient_bound_through_sturm": True,
            "rows": eisenstein_rows,
            "adjacent_residual_eigenpacket_witnesses": eigenpacket_rows,
        },
        "source_audit": {
            "equation_tags": tags,
            "equation_tags_contiguous_1_through_33": True,
            "inline_math_balanced": True,
            "display_math_pairs": 33,
            "source_control": source_control,
            "script_control": script_control,
        },
        "resource_audit": {
            "limit_kib": RSS_GUARD_KIB,
            "peak_rss_kib_omitted_from_deterministic_payload": True,
            "guard_passed": True,
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "ok",
        "output": str(OUTPUT.relative_to(ROOT)),
        "valuation_cases": valuation_cases,
        "euler_rows": row_max,
        "polynomial_rows": len(polynomial_rows),
        "eisenstein_rows": len(eisenstein_rows),
        "peak_rss_kib": peak_rss_kib,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
