#!/usr/bin/env python3
"""Exact certificate for the fixed-D=2, growing-m endpoint construction.

The proof in the companion source is symbolic.  This replay checks its
finite algebraic identities over Q, the multiset-Eulerian numerator identity,
and selected primitive endpoint data.  Decimal quantities are diagnostics
only and are never used to prove nonvanishing or a rank assertion.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_D2_growing_m_certificate.json"


def convolve(a: list[int], b: list[int]) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def derivative(p: list[int], order: int = 1) -> list[int]:
    p = p[:]
    for _ in range(order):
        p = [(k + 1) * p[k + 1] for k in range(len(p) - 1)]
    return p


def x_times(p: list[int]) -> list[int]:
    return [0] + p


def phi_coefficients(m: int, n: int) -> list[int]:
    q = n + 1
    p = [1]
    for j in range(m):
        for _ in range(q):
            p = convolve(p, [-j, 1])
    return p


def logistic_moments(max_degree: int) -> list[Fraction]:
    """Return L(X^k)=f^(k)(0), f=1/(1+exp(z)), exactly."""
    moments = [Fraction(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(Fraction(math.comb(k, j)) * moments[j] for j in range(k)) / 2
        )
    return moments


def functional(p: list[int], moments: list[Fraction]) -> Fraction:
    return sum((Fraction(a) * moments[k] for k, a in enumerate(p)), Fraction())


def primitive_pair(a: Fraction, b: Fraction) -> tuple[int, int]:
    den = math.lcm(a.denominator, b.denominator)
    aa = a.numerator * (den // a.denominator)
    bb = b.numerator * (den // b.denominator)
    g = math.gcd(abs(aa), abs(bb))
    aa //= g
    bb //= g
    if bb < 0:
        aa, bb = -aa, -bb
    return aa, bb


def multiset_eulerian_numerator(m: int, q: int) -> list[int]:
    """A(x) in sum binom(r+m,m)^q x^r=A(x)/(1-x)^(mq+1)."""
    total_degree = m * q
    values = [math.comb(r + m, m) ** q for r in range(total_degree + 1)]
    numerator = []
    for k in range(total_degree + 1):
        numerator.append(
            sum(
                (-1) ** j * math.comb(total_degree + 1, j) * values[k - j]
                for j in range(k + 1)
            )
        )
    while numerator and numerator[-1] == 0:
        numerator.pop()
    return numerator


def at_minus_one(p: list[int]) -> int:
    return sum(a * (-1) ** k for k, a in enumerate(p))


def derivative_at_minus_one(p: list[int]) -> int:
    return sum(k * a * (-1) ** (k - 1) for k, a in enumerate(p) if k)


def exact_row(m: int, n: int, moments: list[Fraction]) -> dict:
    phi = phi_coefficients(m, n)
    mn_parity = (m * n) % 2
    psi = x_times(phi) if mn_parity else phi
    l_psi = functional(psi, moments)
    l_psi_2 = functional(derivative(psi, 2), moments)
    assert l_psi
    p, qcoef = primitive_pair(-l_psi_2, l_psi)

    odd_pivot = (
        functional(derivative(x_times(phi), 1), moments)
        if not mn_parity
        else functional(derivative(phi, 1), moments)
    )
    assert odd_pivot

    # Exact D=2 even-column relations from the shift/reflection lemma.
    even_relation_checks = []
    g = x_times(phi)
    for a in (0, 2):
        pa = derivative(phi, a)
        ga = derivative(g, a)
        lp = functional(pa, moments)
        lg = functional(ga, moments)
        if mn_parity:
            ok = lp == 0
        else:
            ok = 2 * lg == (m - 1) * lp
        even_relation_checks.append(ok)
    assert all(even_relation_checks)

    # MacMahon numerator, symmetry, and the exact Abel-value formula.
    q = n + 1
    M = m * q
    A = multiset_eulerian_numerator(m, q)
    assert len(A) - 1 == m * n
    assert A == A[::-1]
    assert all(a > 0 for a in A)
    aval = at_minus_one(A)
    ader = derivative_at_minus_one(A)
    scale = math.factorial(m) ** q
    if mn_parity:
        assert aval == 0 and ader != 0
        predicted = Fraction(((-1) ** (m + 1)) * scale * ader, 2 ** (M + 1))
    else:
        assert aval != 0
        predicted = Fraction(((-1) ** m) * scale * aval, 2 ** (M + 1))
    assert l_psi == predicted

    return {
        "m": m,
        "n": n,
        "M": M,
        "mn_parity": mn_parity,
        "P": p,
        "Q": qcoef,
        "L_Psi_numerator": l_psi.numerator,
        "L_Psi_denominator": l_psi.denominator,
        "odd_pivot_numerator": odd_pivot.numerator,
        "odd_pivot_denominator": odd_pivot.denominator,
        "multiset_Eulerian_degree": len(A) - 1,
        "A_at_minus_one": aval,
        "A_derivative_at_minus_one": ader,
        "even_column_relations": even_relation_checks,
    }


def diagnostic(row: dict) -> dict:
    m, n, M = row["m"], row["n"], row["M"]
    p, q = row["P"], row["Q"]
    digits = max(120, 5 * M)
    mp.mp.dps = digits
    rho = mp.mpf(p) / q
    error = abs(rho - mp.pi**2)
    height = max(abs(p), abs(q))
    endpoint_ratio = mp.mpf(abs(q)) * error / height
    return {
        "m": m,
        "n": n,
        "M": M,
        "P": p,
        "Q": q,
        "height_decimal_digits": len(str(height)),
        "rho_minus_pi_squared_abs": mp.nstr(error, 50),
        "endpoint_abs_over_height": mp.nstr(endpoint_ratio, 50),
        "minus_log_error_over_M": mp.nstr(-mp.log(error) / M, 35),
        "log_height_over_M_log_M": mp.nstr(
            mp.log(height) / (M * mp.log(M)), 35
        ),
        "endpoint_height_exponent": mp.nstr(
            -mp.log(endpoint_ratio) / mp.log(height), 35
        ),
    }


def main() -> None:
    max_m = 12
    max_n = 12
    max_degree = max_m * (max_n + 1) + 1
    moments = logistic_moments(max_degree)

    rows = []
    for m in range(1, max_m + 1):
        for n in range(2, max_n + 1):
            rows.append(exact_row(m, n, moments))

    selected_pairs = set()
    for k in range(2, 13):
        selected_pairs.add((k, k))
    for n in (2, 3, 4, 6, 8, 12):
        for m in (1, 2, 4, 8, 12):
            selected_pairs.add((m, n))
    lookup = {(row["m"], row["n"]): row for row in rows}
    diagnostics = [diagnostic(lookup[pair]) for pair in sorted(selected_pairs)]

    exact_digest_material = "\n".join(
        f'{r["m"]},{r["n"]},{r["P"]},{r["Q"]},'
        f'{r["L_Psi_numerator"]},{r["L_Psi_denominator"]},'
        f'{r["odd_pivot_numerator"]},{r["odd_pivot_denominator"]}'
        for r in rows
    ).encode()

    payload = {
        "schema": "root-unity-D2-growing-m-certificate-v1",
        "exact_grid": {
            "m_range": [1, max_m],
            "n_range": [2, max_n],
            "row_count": len(rows),
            "all_L_Psi_nonzero": all(r["L_Psi_numerator"] for r in rows),
            "all_even_column_relations": all(
                all(r["even_column_relations"]) for r in rows
            ),
            "all_odd_pivots_nonzero": all(r["odd_pivot_numerator"] for r in rows),
            "all_multiset_Eulerian_degrees_correct": all(
                r["multiset_Eulerian_degree"] == r["m"] * r["n"] for r in rows
            ),
            "exact_tuple_sha256": hashlib.sha256(exact_digest_material).hexdigest(),
        },
        "selected_exact_and_decimal_diagnostics": diagnostics,
        "claims": {
            "grid_arithmetic": "exact over Q and Z",
            "Eulerian_palindromicity_and_minus_one_values": "exact over Z on grid",
            "decimal_endpoint_values": "diagnostic only",
            "all_parameter_nonvanishing": "proved in source using Simion's theorem, not inferred from grid",
        },
    }
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUT.write_bytes(encoded)
    print(f"wrote {OUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"exact rows {len(rows)}")


if __name__ == "__main__":
    main()
