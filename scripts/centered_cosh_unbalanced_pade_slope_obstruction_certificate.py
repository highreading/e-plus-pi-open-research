#!/usr/bin/env python3
"""Exact replay for the unbalanced centered-cosh Padé slope audit.

All rank, determinant, Padé, Schur, and divisibility assertions are exact.
The bounded determinant grid is diagnostic and is not extrapolated.
"""

from __future__ import annotations

import hashlib
import json
import math
import resource
import time
from pathlib import Path

import sympy as sp
from flint import __version__ as flint_version
from flint import fmpq, fmpq_mat


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "centered_cosh_unbalanced_pade_slope_obstruction.md"
OUT = ROOT / "results" / "centered_cosh_unbalanced_pade_slope_obstruction_certificate.json"
RSS_LIMIT_KIB = 2 * 1024 * 1024
x = sp.symbols("x")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def rat(value: sp.Expr | int) -> sp.Rational:
    return sp.Rational(value)


def rat_text(value: sp.Expr | int) -> str:
    value = rat(value)
    return str(value.p) if value.q == 1 else f"{value.p}/{value.q}"


def f_coefficients(limit: int) -> list[sp.Rational]:
    """Coefficients of F(x)=1/(2 cosh(sqrt(x)))."""
    return [
        sp.Rational(sp.euler(2 * j), 2 * math.factorial(2 * j))
        for j in range(limit + 1)
    ]


def h_coefficients(f: list[sp.Rational]) -> list[sp.Rational]:
    """Coefficients of 2F(-y)=sec(sqrt(y))."""
    return [sp.Rational(2 * ((-1) ** j) * value) for j, value in enumerate(f)]


def poly_trim(poly: list[sp.Rational]) -> list[sp.Rational]:
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_shift(poly: list[sp.Rational], shift: int) -> list[sp.Rational]:
    return [sp.S.Zero] * shift + list(poly)


def poly_mul(left: list[sp.Rational], right: list[sp.Rational]) -> list[sp.Rational]:
    result = [sp.S.Zero] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return [sp.Rational(value) for value in result]


def coeff_f_times(poly: list[sp.Rational], degree: int, f: list[sp.Rational]) -> sp.Rational:
    return sp.Rational(
        sum(poly[k] * f[degree - k] for k in range(min(degree, len(poly) - 1) + 1))
    )


def pade_entry(
    L: int, D: int, f: list[sp.Rational]
) -> tuple[list[sp.Rational], list[sp.Rational]]:
    """Return Q,P with Q(0)=1 for the normal [L/D] entry."""
    if D == 0:
        q = [sp.S.One]
    else:
        matrix = sp.Matrix(
            [
                [f[j - k] if j >= k else 0 for k in range(D + 1)]
                for j in range(L + 1, L + D + 1)
            ]
        )
        kernel = matrix.nullspace()
        assert len(kernel) == 1
        vector = [sp.Rational(v) for v in kernel[0]]
        assert vector[0] != 0
        q = [sp.cancel(v / vector[0]) for v in vector]
    p = [coeff_f_times(q, j, f) for j in range(L + 1)]
    assert len(q) == D + 1 and q[0] == 1 and q[-1] != 0
    assert p[-1] != 0
    for j in range(L + 1, L + D + 1):
        assert coeff_f_times(q, j, f) == 0
    return [sp.Rational(v) for v in q], [sp.Rational(v) for v in p]


def to_fmpq_matrix(rows: list[list[sp.Rational]]) -> fmpq_mat:
    if not rows:
        return fmpq_mat(0, 0)
    return fmpq_mat(
        [
            [fmpq(int(sp.numer(v)), int(sp.denom(v))) for v in row]
            for row in rows
        ]
    )


def coefficient_matrix(polys: list[list[sp.Rational]], length: int) -> fmpq_mat:
    rows = []
    for degree in range(length):
        rows.append(
            [poly[degree] if degree < len(poly) else sp.S.Zero for poly in polys]
        )
    return to_fmpq_matrix(rows)


def matrix_digest(matrix: fmpq_mat) -> str:
    digest = hashlib.sha256()
    digest.update(f"{matrix.nrows()},{matrix.ncols()}\n".encode())
    for i in range(matrix.nrows()):
        for j in range(matrix.ncols()):
            digest.update(f"{matrix[i, j]}\n".encode())
    return digest.hexdigest()


def schur_cofactor(L: int, D: int, k: int, h: list[sp.Rational]) -> sp.Rational:
    shape = [L + 1] * k + [L] * (D - k)
    if D == 0:
        return sp.S.One
    matrix = sp.Matrix(
        [
            [
                h[shape[i] - i + j]
                if shape[i] - i + j >= 0
                else sp.S.Zero
                for j in range(D)
            ]
            for i in range(D)
        ]
    )
    return sp.Rational(matrix.det())


def common_schur_denominator(M: int, sigma: int) -> int:
    width = (M + sigma) * (M + 1)
    bound = 4 * M + 2 * sigma
    result = 1
    for prime in sp.primerange(2, bound + 1):
        result *= int(prime) ** math.floor(2 * width / (int(prime) - 1))
    return result


def reverse(poly: list[sp.Rational]) -> list[sp.Rational]:
    return list(reversed(poly_trim(poly)))


def series_ratio(
    numerator: list[sp.Rational], denominator: list[sp.Rational], length: int
) -> list[sp.Rational]:
    assert denominator[0] != 0
    result = [sp.S.Zero] * length
    for n in range(length):
        target = numerator[n] if n < len(numerator) else sp.S.Zero
        target -= sum(
            denominator[k] * result[n - k]
            for k in range(1, min(n, len(denominator) - 1) + 1)
        )
        result[n] = sp.cancel(target / denominator[0])
    return [sp.Rational(v) for v in result]


def truncated_mul(
    left: list[sp.Rational], right: list[sp.Rational], length: int
) -> list[sp.Rational]:
    result = [sp.S.Zero] * length
    for i, a in enumerate(left[:length]):
        if a == 0:
            continue
        for j, b in enumerate(right[: length - i]):
            result[i + j] += a * b
    return [sp.Rational(v) for v in result]


def shifted_trunc(poly: list[sp.Rational], shift: int, length: int) -> list[sp.Rational]:
    return ([sp.S.Zero] * shift + poly[: max(0, length - shift)])[:length]


def verify_case(
    M: int, sigma: int, r: int, f: list[sp.Rational]
) -> dict[str, object]:
    B = 2 * M + sigma
    d = M + r
    Q, P = pade_entry(M + sigma, M, f)
    G, R = pade_entry(M + 1 - sigma, M + 2 * sigma - 1, f)

    cross = poly_trim(
        [a - b for a, b in zip(
            poly_mul(R, Q) + [sp.S.Zero] * max(0, len(poly_mul(P, G)) - len(poly_mul(R, Q))),
            poly_mul(P, G) + [sp.S.Zero] * max(0, len(poly_mul(R, Q)) - len(poly_mul(P, G))),
        )]
    )
    assert len(cross) == B + 2
    assert all(value == 0 for value in cross[:-1]) and cross[-1] != 0

    constraint_rows = [
        [f[j - k] if j >= k else sp.S.Zero for k in range(d + 1)]
        for j in range(d + 1, B + 1)
    ]
    constraint = to_fmpq_matrix(constraint_rows) if constraint_rows else fmpq_mat(0, d + 1)
    expected_constraint_rank = B - d
    assert int(constraint.rank()) == expected_constraint_rank

    factor_basis = [poly_shift(Q, j) for j in range(r - sigma + 1)]
    factor_basis += [poly_shift(G, j) for j in range(r)]
    for poly in factor_basis:
        assert len(poly_trim(poly)) <= d + 1
        for j in range(d + 1, B + 1):
            assert coeff_f_times(poly, j, f) == 0
    factor_matrix = coefficient_matrix(factor_basis, d + 1)
    assert int(factor_matrix.rank()) == 2 * r - sigma + 1
    assert factor_matrix.ncols() == d + 1 - expected_constraint_rank

    q2 = poly_mul(Q, Q)
    qg = poly_mul(Q, G)
    g2 = poly_mul(G, G)
    product_basis = [poly_shift(q2, j) for j in range(2 * r - 2 * sigma + 1)]
    product_basis += [poly_shift(qg, j) for j in range(2 * r - sigma)]
    product_basis += [poly_shift(g2, j) for j in range(2 * r - 1)]
    dimension = 6 * r - 3 * sigma
    product_matrix = coefficient_matrix(product_basis, 2 * d + 1)
    assert product_matrix.ncols() == dimension
    assert int(product_matrix.rank()) == dimension

    delta = 2 * M - 4 * r + 3 * sigma + 1
    assert delta == 3 * (B - d) - d + 1
    high_rows = [
        [
            poly[degree] if degree < len(poly) else sp.S.Zero
            for poly in product_basis
        ]
        for degree in range(delta, 2 * d + 1)
    ]
    high = to_fmpq_matrix(high_rows)
    assert high.nrows() == high.ncols() == dimension
    high_det = high.det()

    jet_length = dimension
    if sigma == 0:
        ratio = series_ratio(reverse(G), reverse(Q), jet_length)
        H = shifted_trunc(ratio, 2, jet_length)
        H2 = truncated_mul(H, H, jet_length)
        jet_polys = [shifted_trunc([sp.S.One], j, jet_length) for j in range(2 * r + 1)]
        jet_polys += [shifted_trunc(H, j, jet_length) for j in range(2 * r)]
        jet_polys += [shifted_trunc(H2, j, jet_length) for j in range(2 * r - 1)]
    else:
        ratio = series_ratio(reverse(Q), reverse(G), jet_length)
        K = shifted_trunc(ratio, 1, jet_length)
        K2 = truncated_mul(K, K, jet_length)
        jet_polys = [shifted_trunc([sp.S.One], j, jet_length) for j in range(2 * r - 1)]
        jet_polys += [shifted_trunc(K, j, jet_length) for j in range(2 * r - 1)]
        jet_polys += [shifted_trunc(K2, j, jet_length) for j in range(2 * r - 1)]
    jet = coefficient_matrix(jet_polys, jet_length)
    jet_det = jet.det()
    assert (high_det != 0) == (jet_det != 0)

    if sigma == 1 and r == 1:
        k1 = ratio[0]
        assert jet_det == fmpq(int(sp.numer(k1**3)), int(sp.denom(k1**3)))

    if sigma == 0 and r == 1:
        r0, r1c, r2c, r3c = ratio[:4]
        formula = r0 * (2 * r1c**3 - 3 * r0 * r1c * r2c + r0**2 * r3c)
        assert jet_det == fmpq(int(sp.numer(formula)), int(sp.denom(formula)))

    return {
        "M": M,
        "sigma": sigma,
        "r": r,
        "B": B,
        "factor_degree": d,
        "constraint_count": B - d,
        "factor_dimension": 2 * r - sigma + 1,
        "product_dimension": dimension,
        "codimension_delta": delta,
        "cross_kappa": rat_text(cross[-1]),
        "high_determinant_nonzero": bool(high_det != 0),
        "jet_determinant_nonzero": bool(jet_det != 0),
        "high_matrix_digest_sha256": matrix_digest(high),
        "jet_matrix_digest_sha256": matrix_digest(jet),
    }


def verify_schur_rows(
    M: int, sigma: int, f: list[sp.Rational], h: list[sp.Rational]
) -> dict[str, object]:
    common = common_schur_denominator(M, sigma)
    entries = [
        (M + sigma, M, "Q"),
        (M + 1 - sigma, M + 2 * sigma - 1, "G"),
    ]
    rows = []
    for L, D, label in entries:
        denominator, _ = pade_entry(L, D, f)
        cofactors = [schur_cofactor(L, D, k, h) for k in range(D + 1)]
        assert cofactors[0] != 0
        assert all(value > 0 for value in cofactors)
        ratios = [sp.cancel(value / cofactors[0]) for value in cofactors]
        assert ratios == denominator
        cleared = [sp.Rational(common * value) for value in cofactors]
        assert all(value.q == 1 for value in cleared)
        rows.append(
            {
                "entry": label,
                "type": [L, D],
                "cofactor_count": D + 1,
                "common_clearing_verified": True,
                "max_cleared_bits": max(abs(int(value)).bit_length() for value in cleared),
            }
        )
    return {
        "M": M,
        "sigma": sigma,
        "W": (M + sigma) * (M + 1),
        "prime_cutoff": 4 * M + 2 * sigma,
        "common_denominator_bits": common.bit_length(),
        "entries": rows,
    }


def lower_lift_parameter_rows() -> list[dict[str, object]]:
    rows = []
    for n in range(8, 31):
        baseline = (n - 1) // 3
        for offset in (0, 1):
            t = baseline + offset
            blocks = []
            for epsilon in (0, 1):
                d = (n - 1 - epsilon) // 2
                B = (n + t - epsilon) // 2
                M, sigma = divmod(B, 2)
                r = d - M
                delta = 3 * (B - d) - d + 1
                assert delta == 2 * M - 4 * r + 3 * sigma + 1
                blocks.append(
                    {
                        "epsilon": epsilon,
                        "d": d,
                        "B": B,
                        "M": M,
                        "sigma": sigma,
                        "r": r,
                        "delta": delta,
                        "direct_regime": bool(r >= 1 and M >= 2 * r - sigma),
                    }
                )
            rows.append({"n": n, "t": t, "offset_from_floor": offset, "blocks": blocks})
    return rows


def main() -> None:
    started = time.perf_counter()
    f = f_coefficients(80)
    h = h_coefficients(f)

    determinant_rows = []
    for sigma in (0, 1):
        for M in range(1, 9):
            if sigma == 0 and M == 1:
                max_r = 0
            else:
                max_r = (M + sigma) // 2
            for r in range(1, max_r + 1):
                assert M >= 2 * r - sigma
                determinant_rows.append(verify_case(M, sigma, r, f))

    assert determinant_rows
    assert all(row["high_determinant_nonzero"] for row in determinant_rows)

    schur_rows = [
        verify_schur_rows(M, sigma, f, h)
        for sigma in (0, 1)
        for M in range(2, 6)
    ]
    parameter_rows = lower_lift_parameter_rows()

    elapsed = time.perf_counter() - started
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss < RSS_LIMIT_KIB

    payload = {
        "schema": "centered-cosh-unbalanced-pade-slope-obstruction-v1",
        "logical_status": {
            "all_parameter": [
                "anti-diagonal Padé normality and cross identity",
                "one-parity factor decomposition",
                "product direct sum in the positive-codimension regime",
                "codimension delta = 3 constraints - factor degree + 1",
                "reversed square-jet determinant equivalence",
                "uniform Schur clearing and O(M^2) input-height scale",
            ],
            "finite_only": [
                "nonvanishing of the secant square-jet determinants on this bounded grid",
                "displayed lower-lift parameter rows",
            ],
            "not_claimed": [
                "all-parameter square-jet determinant nonvanishing",
                "coupled two-parity quadratic nonexistence",
                "a primitive height lower bound",
                "classification of e+pi",
            ],
        },
        "determinant_grid": {
            "M_range": [1, 8],
            "rows": determinant_rows,
            "all_nonzero": True,
        },
        "schur_clearing_grid": schur_rows,
        "lower_lift_parameter_grid": parameter_rows,
        "source_sha256": sha256_file(SOURCE),
        "software": {
            "python_flint": flint_version,
            "sympy": sp.__version__,
        },
        "replay": {
            "rss_limit_kib": RSS_LIMIT_KIB,
            "live_metrics_excluded_from_hashed_json": True,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                **payload["replay"],
                "elapsed_seconds": round(elapsed, 6),
                "peak_rss_kib": peak_rss,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
