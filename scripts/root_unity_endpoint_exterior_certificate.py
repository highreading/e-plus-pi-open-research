#!/usr/bin/env python3
"""Exact certificate for exterior powers of root-of-unity endpoints.

The companion note proves the general statements symbolically.  This replay
builds the reduced endpoint matrices over Q, computes their saturated
Pluecker vectors, maps those vectors through the divided-derivative
Wronskian, and makes the resulting endpoint polynomial primitive.  All rank,
degree, content, and basis-invariance checks are exact.  Decimal evaluations
at i*pi are explicitly diagnostic and are not used to prove any assertion.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_endpoint_exterior_certificate.json"
Z = sp.symbols("z")


def convolve(a: list[int], b: list[int]) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def derivative(p: list[int], order: int) -> list[int]:
    p = p[:]
    for _ in range(order):
        p = [(k + 1) * p[k + 1] for k in range(len(p) - 1)]
    return p


def phi_coefficients(m: int, n: int) -> list[int]:
    p = [1]
    for j in range(m):
        for _ in range(n + 1):
            p = convolve(p, [-j, 1])
    return p


def logistic_moments(max_degree: int) -> list[Fraction]:
    """Return L(X^k)=f^(k)(0), f=1/(1+exp(z)), exactly."""
    moments = [Fraction(1, 2)]
    for k in range(1, max_degree + 1):
        moments.append(
            -sum(
                (Fraction(math.comb(k, j)) * moments[j] for j in range(k)),
                Fraction(),
            )
            / 2
        )
    return moments


def functional(p: list[int], moments: list[Fraction]) -> Fraction:
    return sum(
        (Fraction(a) * moments[k] for k, a in enumerate(p)), Fraction()
    )


def endpoint_matrix(
    m: int, n: int, D: int, p: int, moments: list[Fraction]
) -> sp.Matrix:
    """The (D-p+1)-by-(D+1) reduced endpoint matrix."""
    row_count = D - p + 1
    if row_count == 0:
        return sp.zeros(0, D + 1)
    phi = phi_coefficients(m, n)
    rows = []
    for q in range(row_count):
        xq_phi = [0] * q + phi
        row = []
        for a in range(D + 1):
            value = functional(derivative(xq_phi, a), moments)
            row.append(sp.Rational(value.numerator, value.denominator))
        rows.append(row)
    return sp.Matrix(rows)


def primitive_rational_vector(
    values: list[sp.Rational],
) -> tuple[list[int], sp.Rational]:
    """Return primitive integers and scale with ints=scale*values."""
    denominators = [int(sp.denom(v)) for v in values]
    denominator = math.lcm(*denominators)
    integers = [int(v * denominator) for v in values]
    content = math.gcd(*(abs(v) for v in integers))
    assert content > 0
    integers = [v // content for v in integers]
    scale = sp.Rational(denominator, content)
    first = next(v for v in integers if v)
    if first < 0:
        integers = [-v for v in integers]
        scale = -scale
    assert all(scale * value == integer for value, integer in zip(values, integers))
    return integers, scale


def saturated_pluecker_vector(
    basis: sp.Matrix,
) -> tuple[list[tuple[int, ...]], list[int], sp.Rational]:
    """Primitive Pluecker coordinates of the rational column space."""
    ambient_dimension, p = basis.shape
    subsets = list(itertools.combinations(range(ambient_dimension), p))
    minors = [sp.det(basis[list(subset), :]) for subset in subsets]
    assert any(minors)
    primitive, scale = primitive_rational_vector(minors)
    return subsets, primitive, scale


def wronskian_from_pluecker(
    subsets: list[tuple[int, ...]], pluecker: list[int], p: int
) -> list[int]:
    """Integer coefficients, ascending, of the saturated exterior Wronskian."""
    D = max(max(subset) for subset in subsets)
    degree_bound = p * (D - p + 1)
    coefficients = [0] * (degree_bound + 1)
    triangular_sum = p * (p - 1) // 2
    for subset, coordinate in zip(subsets, pluecker):
        binomial_matrix = sp.Matrix(
            [[math.comb(k, a) if k >= a else 0 for a in range(p)] for k in subset]
        )
        multiplier = int(binomial_matrix.det())
        exponent = sum(subset) - triangular_sum
        if exponent >= len(coefficients):
            coefficients.extend([0] * (exponent + 1 - len(coefficients)))
        coefficients[exponent] += coordinate * multiplier
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    assert any(coefficients)
    return coefficients


def primitive_integer_polynomial(
    coefficients: list[int],
) -> tuple[list[int], int]:
    content = math.gcd(*(abs(c) for c in coefficients))
    assert content > 0
    primitive = [c // content for c in coefficients]
    if primitive[-1] < 0:
        primitive = [-c for c in primitive]
    assert math.gcd(*(abs(c) for c in primitive)) == 1
    return primitive, content


def direct_wronskian(basis: sp.Matrix, p: int) -> sp.Expr:
    polynomials = [
        sum(basis[a, j] * Z**a for a in range(basis.rows)) for j in range(p)
    ]
    matrix = sp.Matrix(
        [
            [sp.diff(polynomials[j], Z, a) / math.factorial(a) for a in range(p)]
            for j in range(p)
        ]
    )
    return sp.expand(matrix.det())


def coefficients_to_expr(coefficients: list[int]) -> sp.Expr:
    return sum(c * Z**k for k, c in enumerate(coefficients))


def same_up_to_sign(a: list[int], b: list[int]) -> bool:
    return a == b or a == [-x for x in b]


def exact_row(
    m: int,
    n: int,
    D: int,
    p: int,
    moments: list[Fraction],
    check_direct: bool,
) -> dict:
    matrix = endpoint_matrix(m, n, D, p, moments)
    expected_rank = D - p + 1
    rank = matrix.rank()
    assert rank == expected_rank
    if p == D + 1:
        basis = sp.eye(D + 1)
    else:
        nullspace = matrix.nullspace()
        assert len(nullspace) == p
        basis = sp.Matrix.hstack(*nullspace)

    subsets, pluecker, scale = saturated_pluecker_vector(basis)
    lattice_wronskian = wronskian_from_pluecker(subsets, pluecker, p)
    primitive_wronskian, exterior_content = primitive_integer_polynomial(
        lattice_wronskian
    )
    actual_degree = len(primitive_wronskian) - 1
    degree_bound = p * (D - p + 1)
    assert actual_degree <= degree_bound

    if check_direct:
        direct = direct_wronskian(basis, p)
        assert sp.expand(scale * direct - coefficients_to_expr(lattice_wronskian)) == 0

        # A deterministic determinant-one basis change leaves the Wronskian
        # fixed, while scaling one basis vector by two changes it by two.  In
        # both cases primitive normalization is basis-independent up to sign.
        changed = basis.copy()
        for j in range(p - 1):
            changed[:, j] += basis[:, j + 1]
        changed_direct = direct_wronskian(changed, p)
        assert sp.expand(changed_direct - direct) == 0
        scaled = basis.copy()
        scaled[:, 0] *= 2
        scaled_direct = direct_wronskian(scaled, p)
        assert sp.expand(scaled_direct - 2 * direct) == 0

        direct_poly = sp.Poly(direct, Z, domain=sp.QQ)
        direct_coefficients = [
            sp.Rational(direct_poly.nth(k)) for k in range(direct_poly.degree() + 1)
        ]
        direct_primitive, _ = primitive_rational_vector(direct_coefficients)
        assert same_up_to_sign(direct_primitive, primitive_wronskian)

    if p == D + 1:
        assert pluecker == [1]
        assert lattice_wronskian == [1]
        assert primitive_wronskian == [1]
        assert exterior_content == 1

    return {
        "m": m,
        "n": n,
        "D": D,
        "p": p,
        "vanishing_order_lower_bound": m * (n + 1) + D - p + 1,
        "endpoint_matrix_rank": rank,
        "expected_rank": expected_rank,
        "degree_bound": degree_bound,
        "actual_degree": actual_degree,
        "degree_defect": degree_bound - actual_degree,
        "pluecker_coordinates": pluecker,
        "pluecker_height": max(abs(c) for c in pluecker),
        "lattice_wronskian_coefficients_ascending": lattice_wronskian,
        "lattice_wronskian_height": max(abs(c) for c in lattice_wronskian),
        "exterior_content": exterior_content,
        "primitive_wronskian_coefficients_ascending": primitive_wronskian,
        "primitive_wronskian_height": max(abs(c) for c in primitive_wronskian),
        "direct_determinant_checked": check_direct,
    }


def diagnostic(row: dict) -> dict:
    coefficients = row["primitive_wronskian_coefficients_ascending"]
    height = row["primitive_wronskian_height"]
    digits = max(180, 3 * len(str(height)) + 80)
    mp.mp.dps = digits
    argument = mp.j * mp.pi
    value = mp.fsum(mp.mpf(c) * argument**k for k, c in enumerate(coefficients))
    absolute_value = abs(value)
    ratio = absolute_value / height
    exponent = None
    if height > 1 and absolute_value:
        exponent = mp.nstr(-mp.log(ratio) / mp.log(height), 35)
    return {
        "m": row["m"],
        "n": row["n"],
        "D": row["D"],
        "p": row["p"],
        "actual_degree": row["actual_degree"],
        "degree_bound": row["degree_bound"],
        "pluecker_height_decimal_digits": len(str(row["pluecker_height"])),
        "exterior_content_decimal_digits": len(str(row["exterior_content"])),
        "primitive_height_decimal_digits": len(str(height)),
        "endpoint_absolute_value": mp.nstr(absolute_value, 50),
        "endpoint_abs_over_height": mp.nstr(ratio, 50),
        "endpoint_height_exponent": exponent,
    }


def digest_row(row: dict) -> dict:
    return {
        key: row[key]
        for key in (
            "m",
            "n",
            "D",
            "p",
            "endpoint_matrix_rank",
            "actual_degree",
            "degree_bound",
            "pluecker_coordinates",
            "lattice_wronskian_coefficients_ascending",
            "exterior_content",
            "primitive_wronskian_coefficients_ascending",
        )
    }


def selected(row: dict) -> bool:
    m, n, D, p = row["m"], row["n"], row["D"], row["p"]
    principal = D == 6 and n in (7, 8) and m in (1, 3, 4)
    diagonal = m == 1 and n == D and p in {1, (D + 1) // 2, D, D + 1}
    return principal or diagonal


def main() -> None:
    max_m = 4
    max_n = 8
    max_D = 6
    max_moment_degree = max_m * (max_n + 1) + max_D
    moments = logistic_moments(max_moment_degree)

    selected_keys = set()
    for m in (1, 3, 4):
        for n in (7, 8):
            for p in range(1, 8):
                selected_keys.add((m, n, 6, p))
    for D in range(2, 7):
        for p in {1, (D + 1) // 2, D, D + 1}:
            selected_keys.add((1, D, D, p))

    rows = []
    for m in range(1, max_m + 1):
        for D in range(2, max_D + 1):
            for n in range(D, max_n + 1):
                for p in range(1, D + 2):
                    key = (m, n, D, p)
                    rows.append(
                        exact_row(
                            m, n, D, p, moments, check_direct=key in selected_keys
                        )
                    )

    assert len(rows) == 460
    assert all(r["endpoint_matrix_rank"] == r["expected_rank"] for r in rows)
    assert all(r["actual_degree"] <= r["degree_bound"] for r in rows)
    top_rows = [r for r in rows if r["p"] == r["D"] + 1]
    assert all(
        r["primitive_wronskian_coefficients_ascending"] == [1] for r in top_rows
    )

    degree_defects = [
        {
            "m": r["m"],
            "n": r["n"],
            "D": r["D"],
            "p": r["p"],
            "degree_defect": r["degree_defect"],
        }
        for r in rows
        if r["degree_defect"]
    ]
    nontrivial_contents = [
        {
            "m": r["m"],
            "n": r["n"],
            "D": r["D"],
            "p": r["p"],
            "exterior_content": r["exterior_content"],
        }
        for r in rows
        if r["exterior_content"] > 1
    ]
    maximum_content = max(r["exterior_content"] for r in rows)
    maximum_content_tuples = [
        [r["m"], r["n"], r["D"], r["p"]]
        for r in rows
        if r["exterior_content"] == maximum_content
    ]

    exact_material = json.dumps(
        [digest_row(row) for row in rows],
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    selected_rows = [row for row in rows if selected(row)]

    payload = {
        "schema": "root-unity-endpoint-exterior-certificate-v1",
        "exact_grid": {
            "m_range": [1, max_m],
            "n_rule": "D <= n <= 8",
            "D_range": [2, max_D],
            "p_rule": "1 <= p <= D+1",
            "row_count": len(rows),
            "all_expected_ranks": all(
                r["endpoint_matrix_rank"] == r["expected_rank"] for r in rows
            ),
            "all_wronskians_nonzero": all(
                any(r["primitive_wronskian_coefficients_ascending"]) for r in rows
            ),
            "all_degree_bounds": all(
                r["actual_degree"] <= r["degree_bound"] for r in rows
            ),
            "degree_defect_count": len(degree_defects),
            "maximum_degree_defect": max(
                (r["degree_defect"] for r in rows), default=0
            ),
            "nontrivial_exterior_content_count": len(nontrivial_contents),
            "maximum_exterior_content": maximum_content,
            "maximum_exterior_content_tuples": maximum_content_tuples,
            "all_top_exterior_powers_equal_one": all(
                r["primitive_wronskian_coefficients_ascending"] == [1]
                for r in top_rows
            ),
            "direct_determinant_check_count": sum(
                r["direct_determinant_checked"] for r in rows
            ),
            "exact_tuple_sha256": hashlib.sha256(exact_material).hexdigest(),
        },
        "degree_defects": degree_defects,
        "nontrivial_exterior_contents": nontrivial_contents,
        "selected_exact_rows": [digest_row(row) for row in selected_rows],
        "selected_diagnostics": [diagnostic(row) for row in selected_rows],
        "logical_scope": {
            "exact": (
                "Ranks, Pluecker coordinates, Wronskian coefficients, contents, "
                "degree bounds, top exterior identities, and selected direct "
                "determinant/basis-change checks are exact over Q or Z."
            ),
            "diagnostic": (
                "Decimal evaluations at i*pi describe only this finite grid and "
                "are not evidence for an asymptotic or a nonvanishing theorem."
            ),
        },
        "versions": {
            "python_sympy": sp.__version__,
            "mpmath": mp.__version__,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["exact_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
