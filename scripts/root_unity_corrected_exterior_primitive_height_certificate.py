#!/usr/bin/env python3
"""Exact finite certificate for the corrected two-column endpoint.

The all-parameter statements live in the companion source.  This replay is
deliberately finite: it constructs the natural two-dimensional endpoint
space over Q, saturates its exterior line, and keeps separate

* the bare Wronskian content;
* the Gamma denominator/content;
* the corrected Delta denominator/content; and
* the content of one globally cleared corrected-coefficient map.

It also checks the coefficient formula

    Delta = W(C,D) - (C beta_D - D beta_C)

on a rational kernel basis and computes ranks/Smith data for the ambient
integer coefficient map.  Decimal values at i*pi are diagnostics only.
No assertion outside the listed tuples is inferred from this script.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_corrected_exterior_primitive_height_certificate.json"
sys.path.insert(0, str(ROOT / "scripts"))
import root_unity_gamma_logistic_minor_certificate as logistic  # noqa: E402


def primitive_rational_vector(values: list[sp.Rational]) -> dict:
    """Canonical denominator, cleared content, and primitive integer vector."""
    values = [sp.Rational(value) for value in values]
    assert any(values)
    denominator = math.lcm(*(int(sp.denom(value)) for value in values))
    cleared = [int(value * denominator) for value in values]
    content = math.gcd(*(abs(value) for value in cleared))
    assert content > 0
    primitive = [value // content for value in cleared]
    first = next(value for value in primitive if value)
    if first < 0:
        primitive = [-value for value in primitive]
        cleared = [-value for value in cleared]
    assert math.gcd(*(abs(value) for value in primitive)) == 1
    return {
        "denominator": denominator,
        "cleared_content": content,
        "cleared": cleared,
        "primitive": primitive,
    }


def saturated_pluecker(basis: sp.Matrix) -> tuple[list[tuple[int, int]], list[int], sp.Rational]:
    pairs = list(itertools.combinations(range(basis.rows), 2))
    minors = [sp.det(basis[list(pair), :]) for pair in pairs]
    data = primitive_rational_vector(minors)
    primitive = data["primitive"]
    # scale*basis-minors equals the oriented primitive vector.
    first_index = next(index for index, value in enumerate(minors) if value)
    scale = sp.cancel(sp.Rational(primitive[first_index]) / minors[first_index])
    assert all(sp.cancel(scale * value) == target for value, target in zip(minors, primitive))
    return pairs, primitive, scale


def antisymmetric_coordinate(
    lookup: dict[tuple[int, int], int], a: int, b: int
) -> int:
    if a == b:
        return 0
    if a < b:
        return lookup[a, b]
    return -lookup[b, a]


def wronskian_coefficients(
    pairs: list[tuple[int, int]], pluecker: list[int], n: int, D: int
) -> list[int]:
    lookup = dict(zip(pairs, pluecker))
    out = [0] * (n + D + 1)
    for a in range(D + 1):
        for b in range(a + 1, D + 1):
            out[a + b - 1] += (b - a) * lookup[a, b]
    return out


def gamma_coefficients(
    pairs: list[tuple[int, int]],
    pluecker: list[int],
    E: sp.Matrix,
    n: int,
    D: int,
) -> list[sp.Rational]:
    lookup = dict(zip(pairs, pluecker))
    out = [sp.Rational(0)] * (n + D + 1)
    for a in range(D + 1):
        for b in range(n + 1):
            ell = a + b
            for j in range(D + 1):
                out[ell] += E[b, j] * antisymmetric_coordinate(lookup, a, j)
    return out


def direct_wronskian(c: sp.Matrix, d: sp.Matrix, D: int) -> list[sp.Rational]:
    out = [sp.Rational(0)] * (2 * D - 1)
    for a in range(D + 1):
        for b in range(D + 1):
            if a == b:
                continue
            out[a + b - 1] += b * (c[a] * d[b] - d[a] * c[b])
    return out


def direct_gamma(
    c: sp.Matrix, d: sp.Matrix, E: sp.Matrix, n: int, D: int
) -> list[sp.Rational]:
    beta_c = E * c
    beta_d = E * d
    out = [sp.Rational(0)] * (n + D + 1)
    for a in range(D + 1):
        for b in range(n + 1):
            out[a + b] += c[a] * beta_d[b] - d[a] * beta_c[b]
    return out


def interpolation_determinant(m: int, n: int) -> int:
    return (
        math.prod(math.factorial(a) for a in range(n + 1)) ** m
        * math.prod(
            h ** ((m - h) * (n + 1) ** 2) for h in range(1, m)
        )
    )


def corrected_integer_map(E: sp.Matrix, n: int, D: int) -> tuple[int, sp.Matrix]:
    q_E = math.lcm(*(int(sp.denom(value)) for value in E))
    E_star = E * q_E
    assert all(value.q == 1 for value in E_star)
    pairs = list(itertools.combinations(range(D + 1), 2))
    matrix = sp.zeros(n + D + 1, len(pairs))
    for column, (u, v) in enumerate(pairs):
        matrix[u + v - 1, column] += q_E * (v - u)
        for b in range(n + 1):
            matrix[u + b, column] -= E_star[b, v]
            matrix[v + b, column] += E_star[b, u]
    return q_E, matrix


def vector_content(vector: sp.Matrix) -> int:
    integers = [int(value) for value in vector]
    return math.gcd(*(abs(value) for value in integers))


def endpoint_value_diagnostic(coefficients: list[int]) -> dict:
    height = max(abs(value) for value in coefficients)
    mp.mp.dps = max(120, 4 * len(str(height)) + 60)
    z = mp.j * mp.pi
    value = mp.fsum(mp.mpf(coefficient) * z**degree for degree, coefficient in enumerate(coefficients))
    absolute = abs(value)
    relative = absolute / height
    exponent = None
    if height > 1 and relative:
        exponent = -mp.log(relative) / mp.log(height)
    return {
        "height": height,
        "height_decimal_digits": len(str(height)),
        "absolute_value_at_i_pi": mp.nstr(absolute, 45),
        "relative_value_over_height": mp.nstr(relative, 45),
        "relative_small_value_exponent": None if exponent is None else mp.nstr(exponent, 35),
        "diagnostic_only": True,
    }


def exact_row(m: int, n: int, D: int) -> dict:
    M = m * (n + 1)
    moments = logistic.logistic_moments(M + D + 4)
    K = logistic.endpoint_matrix(m, n, D, moments, centered=False)
    assert K.rank() == D - 1
    basis = sp.Matrix.hstack(*K.nullspace())
    assert basis.shape == (D + 1, 2)
    pairs, pluecker, exterior_scale = saturated_pluecker(basis)

    lambdas = logistic.hermite_cardinal_polynomials(m, n)
    E = logistic.beta_rows(lambdas, D, moments)
    V = interpolation_determinant(m, n)
    Q = (2**M) * V
    assert all((Q * value).q == 1 for value in E)

    w = wronskian_coefficients(pairs, pluecker, n, D)
    gamma = gamma_coefficients(pairs, pluecker, E, n, D)
    delta = [sp.Rational(wi) - gi for wi, gi in zip(w, gamma)]
    assert any(delta)

    # Check the exterior contraction against an arbitrary rational kernel basis.
    c, d = basis[:, 0], basis[:, 1]
    w_direct = direct_wronskian(c, d, D) + [sp.Rational(0)] * (n - D + 2)
    gamma_direct = direct_gamma(c, d, E, n, D)
    delta_direct = [wi - gi for wi, gi in zip(w_direct, gamma_direct)]
    assert all(sp.cancel(exterior_scale * value - target) == 0 for value, target in zip(w_direct, w))
    assert all(sp.cancel(exterior_scale * value - target) == 0 for value, target in zip(gamma_direct, gamma))
    assert all(sp.cancel(exterior_scale * value - target) == 0 for value, target in zip(delta_direct, delta))

    w_nonzero = [value for value in w if value]
    c_W = math.gcd(*(abs(value) for value in w_nonzero))
    gamma_data = primitive_rational_vector(gamma)
    delta_data = primitive_rational_vector(delta)
    primitive_delta = delta_data["primitive"]
    actual_degree = max(index for index, value in enumerate(primitive_delta) if value)

    q_E, A_delta = corrected_integer_map(E, n, D)
    p_column = sp.Matrix(pluecker)
    globally_cleared = A_delta * p_column
    assert all(
        globally_cleared[index] == q_E * delta[index]
        for index in range(n + D + 1)
    )
    c_global = vector_content(globally_cleared)
    assert q_E % delta_data["denominator"] == 0
    assert c_global == (q_E // delta_data["denominator"]) * delta_data["cleared_content"]

    ambient_rank = A_delta.rank()
    smith = None
    if ambient_rank == A_delta.cols and A_delta.cols <= 10:
        smith_matrix = smith_normal_form(A_delta, domain=sp.ZZ)
        invariants = [abs(int(smith_matrix[index, index])) for index in range(A_delta.cols)]
        assert invariants == sorted(invariants)
        assert all(invariants[index + 1] % invariants[index] == 0 for index in range(len(invariants) - 1))
        assert invariants[-1] % c_global == 0
        smith = {
            "invariants": invariants,
            "largest_invariant": invariants[-1],
            "endpoint_global_content_divides_largest_invariant": True,
        }

    digest_payload = {
        "tuple": [m, n, D],
        "pluecker": pluecker,
        "w": w,
        "gamma_primitive": gamma_data["primitive"],
        "delta_primitive": primitive_delta,
    }
    exact_digest = hashlib.sha256(
        json.dumps(digest_payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    return {
        "m": m,
        "n": n,
        "D": D,
        "M": M,
        "endpoint_rank": int(K.rank()),
        "pluecker_height": max(abs(value) for value in pluecker),
        "pluecker_gcd": math.gcd(*(abs(value) for value in pluecker)),
        "interpolation_determinant_V": V,
        "universal_interpolation_clearing_Q_equals_2_to_M_times_V": Q,
        "Q_clears_every_E_entry": True,
        "bare_wronskian_content": c_W,
        "bare_wronskian_primitive_height": max(abs(value // c_W) for value in w),
        "gamma_is_nonzero": any(gamma),
        "gamma_degree": max(index for index, value in enumerate(gamma) if value),
        "gamma_minimal_denominator": gamma_data["denominator"],
        "gamma_cleared_content": gamma_data["cleared_content"],
        "delta_is_nonzero": True,
        "delta_actual_degree": actual_degree,
        "delta_minimal_denominator": delta_data["denominator"],
        "delta_cleared_content": delta_data["cleared_content"],
        "primitive_delta_coefficients_ascending": primitive_delta,
        "global_E_denominator_q_E": q_E,
        "global_map_content_on_endpoint_pluecker": c_global,
        "ambient_corrected_map_shape": list(A_delta.shape),
        "ambient_corrected_map_rank": int(ambient_rank),
        "ambient_corrected_map_full_column_rank": ambient_rank == A_delta.cols,
        "ambient_smith_data": smith,
        "direct_basis_and_exterior_contractions_agree": True,
        "endpoint_diagnostic": endpoint_value_diagnostic(primitive_delta),
        "exact_row_sha256": exact_digest,
    }


def main() -> None:
    tuples = [
        (1, 4, 4),
        (2, 4, 4),
        (3, 3, 2),
        (3, 5, 4),
        (4, 5, 5),
        (4, 6, 4),
    ]
    rows = [exact_row(*parameters) for parameters in tuples]
    digest = hashlib.sha256()
    for row in rows:
        digest.update((row["exact_row_sha256"] + "\n").encode())

    dependency = ROOT / "scripts" / "root_unity_gamma_logistic_minor_certificate.py"
    payload = {
        "schema": "root-unity-corrected-exterior-primitive-height-v1",
        "exact_rows": rows,
        "exact_grid_digest_sha256": digest.hexdigest(),
        "dependency_sha256": {
            str(dependency.relative_to(ROOT)): hashlib.sha256(dependency.read_bytes()).hexdigest()
        },
        "logical_scope": {
            "exact": (
                "All rational ranks, exterior contractions, denominators, contents, "
                "primitive coefficient vectors, and recorded Smith invariants are exact."
            ),
            "diagnostic": (
                "Decimal evaluations and relative exponents are diagnostics and prove no "
                "inequality or all-parameter statement."
            ),
            "no_extrapolation": (
                "The six tuples replay the formulas only.  No claim about unlisted "
                "parameters, Delta nonvanishing, content one, degree, or asymptotics is "
                "inferred from them."
            ),
        },
        "versions": {"python": sys.version, "sympy": sp.__version__, "mpmath": mp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "schema": payload["schema"],
        "row_count": len(rows),
        "digest": payload["exact_grid_digest_sha256"],
        "tuples": tuples,
    }, indent=2))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
