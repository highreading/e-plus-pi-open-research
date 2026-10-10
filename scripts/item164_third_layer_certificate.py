#!/usr/bin/env python3
"""Exact second-Cartier certificate for the item-162 congruence slab.

For p=19 (mod 20) and m=(9p-1)/10+ell*p in the complete e=1 band,
the first Cartier polynomials P_0,P_1 have zero x^(p-1) coefficient.
Writing P_s=T_s' and F=u^a/Q^c, integration by parts reduces the next
content digit to the R/L determinant of two explicit second-Cartier
differentials.  This script constructs those differentials over F_p,
checks the formula against the independent p-adic Hasse tower where frozen
data are available, and performs a rigorously finite extension.

The symbolic proof is recorded in the companion note.  Finite nonvanishing
is never promoted to a uniform theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ARCHIVE = Path(__file__).resolve().parents[1]
ITEM163 = HERE / "item163_deeper_digits_certificate.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n, flag in enumerate(sieve) if flag]


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i in range(len(out)):
        out[i] = (
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
        ) % p
    return trim(out)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([(scalar * value) % p for value in poly])


def conv(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out)


def binomial_row(n: int, p: int) -> list[int]:
    row = [1]
    value = 1
    for j in range(1, n + 1):
        value = value * (n - j + 1) % p * pow(j, -1, p) % p
        row.append(value)
    return row


def slab_polynomial(p: int, s: int) -> list[int]:
    """Return P_s over F_p for the item-162 slab."""
    r = (2 * p - 3) // 5
    if s == 0:
        powers = binomial_row(r, p)
        out = [0] * (5 * r + 1)
        for j, value in enumerate(powers):
            out[r + 4 * j] = value if j % 2 == 0 else -value % p
        return trim(out)
    if s == 1:
        powers = binomial_row(r - 1, p)
        out = [0] * (5 * r - 2)
        for j, value in enumerate(powers):
            coefficient = value if j % 2 == 0 else -value % p
            out[r + 4 * j] = coefficient
            out[r + 4 * j + 1] = -coefficient % p
        return trim(out)
    raise ValueError(s)


def primitive(poly: list[int], p: int) -> list[int]:
    """The zero-constant primitive, requiring the forbidden term to vanish."""
    out = [0] * (len(poly) + 1)
    for exponent, value in enumerate(poly):
        denominator = exponent + 1
        if denominator % p == 0:
            if value % p:
                raise AssertionError(("nonintegrable coefficient", exponent, value, p))
            continue
        out[denominator] = value * pow(denominator, -1, p) % p
    return trim(out)


def second_cartier_numerator(p: int, ell: int, s: int) -> dict[str, Any]:
    """Return H_s with C((F'/F)T_s dx)=H_s/(uQ) dx.

    If D=uQ=x(1-x^4) and N=T_s(a*u'*Q-c*Q'*u), then

      H_{s,n}=sum_{0<=j<p} [x^(pn-4j)]N.

    This is the exact polynomial Cartier rule after using
    D^(p-1)=x^(p-1) sum_{j=0}^{p-1}x^(4j) in F_p[x].
    """
    a = 5 + 6 * ell
    c = 4 + 4 * ell
    u = [0, 1, -1]
    u_prime = [1, -2]
    q = [1, 1, 1, 1]
    q_prime = [1, 2, 3]
    w = add(scale(conv(u_prime, q, p), a, p), scale(conv(q_prime, u, p), -c, p), p)
    p_poly = slab_polynomial(p, s)
    t = primitive(p_poly, p)
    n_poly = conv(t, w, p)
    maximum_n = (len(n_poly) - 1 + 4 * (p - 1)) // p
    h = [0] * (maximum_n + 1)
    for n in range(maximum_n + 1):
        total = 0
        for j in range(p):
            index = p * n - 4 * j
            if 0 <= index < len(n_poly):
                total += n_poly[index]
        h[n] = total % p
    h = trim(h)
    if h[0] != 0 or len(h) > 6:
        raise AssertionError(("unexpected H support", p, ell, s, h))
    return {
        "P": p_poly,
        "T": t,
        "W": w,
        "N": n_poly,
        "H": h,
        "a": a,
        "c": c,
    }


def gaussian_poly_eval(poly: list[int], root: tuple[int, int], p: int) -> tuple[int, int]:
    base = _EXTENDED.base
    out = (0, 0)
    for value in reversed(poly):
        out = base.gadd(base.gmul(out, root, p), (value % p, 0), p)
    return out


def gaussian_shift(poly: list[int], root: tuple[int, int], p: int) -> list[tuple[int, int]]:
    """Coefficients of poly(root+t) over F_p[i], in ascending order."""
    out: list[tuple[int, int]] = [(0, 0)]
    for coefficient in reversed(poly):
        shifted = [(0, 0)] * (len(out) + 1)
        for j, value in enumerate(out):
            shifted[j] = _EXTENDED.base.gadd(
                shifted[j], _EXTENDED.base.gmul(value, root, p), p
            )
            shifted[j + 1] = _EXTENDED.base.gadd(shifted[j + 1], value, p)
        shifted[0] = _EXTENDED.base.gadd(shifted[0], (coefficient % p, 0), p)
        out = shifted
    return out


def base_local_coefficients(
    numerator_exponent: int, denominator_exponent: int, root: str, p: int
) -> list[tuple[int, int]]:
    """Coefficients of u^(numerator_exponent)/Q_alpha^K through K-1."""
    base = _EXTENDED.base
    degree = denominator_exponent - 1
    a_poly, b_poly = _EXTENDED.local_polynomials(root)
    product = _EXTENDED.iconv(a_poly, b_poly)
    right = _EXTENDED.iconv(_EXTENDED.iderivative(a_poly), b_poly)
    right = [_EXTENDED.iscale(value, numerator_exponent) for value in right]
    other = _EXTENDED.iconv(a_poly, _EXTENDED.iderivative(b_poly))
    if len(other) > len(right):
        right += [(0, 0)] * (len(other) - len(right))
    for index, value in enumerate(other):
        right[index] = _EXTENDED.iadd(
            right[index], _EXTENDED.iscale(value, -denominator_exponent)
        )
    a0 = base.ga(*a_poly[0], p)
    b0 = base.ga(*b_poly[0], p)
    coefficients = [
        base.gmul(
            base.gpow(a0, numerator_exponent, p),
            base.gpow(b0, -denominator_exponent, p),
            p,
        )
    ]
    product0_inverse = base.ginv(base.ga(*product[0], p), p)
    for n in range(degree):
        divisor = n + 1
        if divisor % p == 0:
            raise AssertionError(("unexpected precision loss", p, denominator_exponent, n))
        rhs = (0, 0)
        for j in range(0, min(len(right) - 1, n) + 1):
            rhs = base.gadd(
                rhs,
                base.gmul(base.ga(*right[j], p), coefficients[n - j], p),
                p,
            )
        for j in range(1, min(len(product) - 1, n) + 1):
            term = base.gmul(
                base.ga(*product[j], p), coefficients[n - j + 1], p
            )
            term = base.gscale(term, n - j + 1, p)
            rhs = base.gadd(rhs, base.gneg(term, p), p)
        rhs = base.gscale(rhs, pow(divisor, -1, p), p)
        coefficients.append(base.gmul(product0_inverse, rhs, p))
    return coefficients


def multiply_truncated(
    left: list[tuple[int, int]], right: list[tuple[int, int]], degree: int, p: int
) -> list[tuple[int, int]]:
    base = _EXTENDED.base
    out = [(0, 0)] * (degree + 1)
    for i, a in enumerate(left):
        if i > degree:
            break
        for j, b in enumerate(right):
            if i + j > degree:
                break
            out[i + j] = base.gadd(out[i + j], base.gmul(a, b, p), p)
    return out


def transformed_coordinates(p: int, ell: int, h: list[int]) -> tuple[int, int, int]:
    """Coordinates of Phi=u^(a-1)H/Q^(c+1) over F_p."""
    base = _EXTENDED.base
    numerator_exponent = 4 + 6 * ell
    denominator_exponent = 5 + 4 * ell
    if denominator_exponent >= p:
        raise AssertionError(("slab exponent bound", p, ell, denominator_exponent))
    degree = denominator_exponent - 1
    minus_base = base_local_coefficients(
        numerator_exponent, denominator_exponent, "minus_one", p
    )
    i_base = base_local_coefficients(numerator_exponent, denominator_exponent, "i", p)
    minus_h = gaussian_shift(h, (-1 % p, 0), p)
    i_h = gaussian_shift(h, (0, 1), p)
    c_minus = multiply_truncated(minus_base, minus_h, degree, p)
    c_i = multiply_truncated(i_base, i_h, degree, p)
    residue_minus = c_minus[degree][0]
    residue_i = c_i[degree]
    l_value = (4 * residue_minus + 4 * residue_i[0]) % p
    e_value = (-4 * residue_i[1]) % p

    roots_and_coefficients = [
        ((-1 % p, 0), c_minus),
        ((0, 1), c_i),
        ((0, -1 % p), [(a, -b % p) for a, b in c_i]),
    ]
    total = (0, 0)
    for n in range(1, denominator_exponent):
        coefficient_index = degree - n
        contribution = (0, 0)
        for root, coefficients in roots_and_coefficients:
            term = base.gmul(
                coefficients[coefficient_index], base.endpoint_factor(root, n, p), p
            )
            contribution = base.gadd(contribution, term, p)
        contribution = base.gscale(contribution, pow(n, -1, p), p)
        total = base.gadd(total, contribution, p)
    if total[1] % p:
        raise AssertionError(("non-rational transformed endpoint", p, ell, h, total))
    return total[0], l_value, e_value


def slab_row(p: int, ell: int) -> dict[str, Any]:
    k = (p - 19) // 20
    m0 = 18 * k + 17
    m = m0 + ell * p
    if not (p <= 4 * m + 1 < p * p):
        raise ValueError((p, ell, m))
    records = [second_cartier_numerator(p, ell, s) for s in (0, 1)]
    coordinates = [transformed_coordinates(p, ell, record["H"]) for record in records]
    r0, l0, e0 = coordinates[0]
    r1, l1, e1 = coordinates[1]
    next_digit = (l1 * r0 - l0 * r1) % p
    period_digit = (l1 * e0 - l0 * e1) % p
    tail_applies = 6 * ell + 4 >= p
    tail_residual_degrees = [p - 7 + len(record["H"]) - 1 for record in records]
    if tail_applies:
        if not all(degree <= p - 2 for degree in tail_residual_degrees):
            raise AssertionError(("tail degree bound", p, ell, tail_residual_degrees))
        if next_digit != 0:
            raise AssertionError(("proved tail failed", p, ell, next_digit))
    return {
        "p": p,
        "k": k,
        "ell": ell,
        "m": m,
        "a": 5 + 6 * ell,
        "c": 4 + 4 * ell,
        "H0": records[0]["H"],
        "H1": records[1]["H"],
        "Phi0_coordinates_R_L_E": list(coordinates[0]),
        "Phi1_coordinates_R_L_E": list(coordinates[1]),
        "next_A_digit": next_digit,
        "next_period_determinant": period_digit,
        "p3_divides_content": next_digit == 0,
        "proved_tail_applies": tail_applies,
        "tail_residual_degrees": tail_residual_degrees if tail_applies else None,
    }


def direct_hasse_digit(p: int, ell: int) -> dict[str, Any]:
    k = (p - 19) // 20
    m = 18 * k + 17 + ell * p
    precision = 4
    modulus = p**precision
    l0, x0, e0, _ = _TOWER.coordinates_mod(
        _EXTENDED, m, 4 * m + 1, p, precision
    )
    l1, x1, e1, _ = _TOWER.coordinates_mod(
        _EXTENDED, m, 4 * m + 2, p, precision
    )
    determinant_a = (l1 * x0 - l0 * x1) % modulus
    determinant_b = (l1 * e0 - l0 * e1) % modulus
    a_digits = _TOWER.p_digits(determinant_a // p, p, 3)
    b_digits = _TOWER.p_digits(determinant_b // p, p, 3)
    return {
        "a0": a_digits[0],
        "a1": a_digits[1],
        "b0": b_digits[0],
        "b1": b_digits[1],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-bound", type=int, default=500)
    parser.add_argument("--direct-max-m", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rows = []
    cross_checks = []
    prime_ranges = []
    for p in primes_upto(args.prime_bound):
        if p % 20 != 19:
            continue
        k = (p - 19) // 20
        m0 = 18 * k + 17
        expected_ell_max = 5 * k + 3
        first_index = len(rows)
        ell = 0
        while 4 * (m0 + ell * p) + 1 < p * p:
            row = slab_row(p, ell)
            rows.append(row)
            if row["m"] <= args.direct_max_m:
                direct = direct_hasse_digit(p, ell)
                agrees = (
                    direct["a0"] == 0
                    and direct["b0"] == 0
                    and direct["a1"] == row["next_A_digit"]
                )
                if not agrees:
                    raise AssertionError(("direct Hasse mismatch", row, direct))
                cross_checks.append(
                    {
                        "m": row["m"],
                        "p": p,
                        "ell": ell,
                        "direct": direct,
                        "agrees": agrees,
                    }
                )
            ell += 1
        if ell - 1 != expected_ell_max:
            raise AssertionError(("ell range", p, ell - 1, expected_ell_max))
        tail_ell_min = (p - 4 + 5) // 6
        if tail_ell_min > expected_ell_max:
            raise AssertionError(("empty proved tail", p, tail_ell_min, expected_ell_max))
        quadratic_ray_m = (5 * p * p - 17 * p - 2) // 20
        last = rows[-1]
        if (
            last["ell"] != expected_ell_max
            or last["m"] != quadratic_ray_m
            or not last["proved_tail_applies"]
            or not last["p3_divides_content"]
        ):
            raise AssertionError(("quadratic subray", p, last, quadratic_ray_m))
        prime_ranges.append(
            {
                "p": p,
                "k": k,
                "ell_min": 0,
                "ell_max": expected_ell_max,
                "proved_tail_ell_min": tail_ell_min,
                "proved_tail_ell_max": expected_ell_max,
                "row_count": len(rows) - first_index,
                "quadratic_subray_m": quadratic_ray_m,
                "quadratic_subray_identity": "20m=5p^2-17p-2",
            }
        )

    survivors = [
        {key: row[key] for key in ("m", "p", "ell", "next_A_digit")}
        for row in rows
        if row["p3_divides_content"]
    ]
    tail_rows = [row for row in rows if row["proved_tail_applies"]]
    tail_failures = [row for row in tail_rows if not row["p3_divides_content"]]
    if tail_failures:
        raise AssertionError(("proved tail failures", tail_failures[:3]))
    pre_tail_survivors = [
        {key: row[key] for key in ("m", "p", "ell", "next_A_digit")}
        for row in rows
        if row["p3_divides_content"] and not row["proved_tail_applies"]
    ]
    square_ray_diagnostics = [
        row for row in pre_tail_survivors if 10 * row["ell"] + 9 == row["p"]
    ]
    output = {
        "schema": "mixed-cubic-item162-slab-third-layer-v1",
        "status": {
            "second_Cartier_transform": "PROVED_IN_COMPANION_NOTE",
            "third_layer_criterion": "PROVED_IN_COMPANION_NOTE",
            "infinite_third_layer_tail": "PROVED_IN_COMPANION_NOTE",
            "uniform_large_prime_obstruction": "REFUTED_BY_PROVED_INFINITE_TAIL",
            "finite_extension": "EXACT_FINITE_AUDIT_ONLY",
            "pre_tail_classification": "OPEN",
        },
        "parameters": {
            "prime_bound": args.prime_bound,
            "direct_Hasse_max_m": args.direct_max_m,
        },
        "inputs": {
            str(ITEM163.relative_to(HERE)): sha256(ITEM163),
            "scripts/lifted_endpoint_hasse_extended_certificate.py": sha256(
                ARCHIVE / "scripts" / "lifted_endpoint_hasse_extended_certificate.py"
            ),
            "scripts/lifted_endpoint_hasse_certificate.py": sha256(
                ARCHIVE / "scripts" / "lifted_endpoint_hasse_certificate.py"
            ),
        },
        "summary": {
            "slab_rows": len(rows),
            "primes": len({row["p"] for row in rows}),
            "direct_Hasse_cross_checks": len(cross_checks),
            "direct_Hasse_mismatches": 0,
            "p3_survivors": len(survivors),
            "proved_tail_rows": len(tail_rows),
            "proved_tail_failures": len(tail_failures),
            "pre_tail_survivors_diagnostic_only": len(pre_tail_survivors),
            "prime_square_ray_survivors_diagnostic_only": len(square_ray_diagnostics),
        },
        "uniform_theorem": {
            "hypotheses": [
                "p=20k+19 is prime",
                "m=18k+17+ell*p",
                "0<=ell<=5k+3 (equivalently p<=4m+1<p^2)",
                "6ell+4>=p",
            ],
            "conclusion": "p^3 divides c_m",
            "nonempty_subray": "ell=5k+3, equivalently 20m=5p^2-17p-2",
            "fixed_m_mass": "thin: every selected p divides 10m+1",
        },
        "p3_survivors": survivors,
        "pre_tail_survivors_diagnostic_only": pre_tail_survivors,
        "prime_square_ray_survivors_diagnostic_only": square_ray_diagnostics,
        "prime_ranges": prime_ranges,
        "direct_Hasse_cross_checks": cross_checks,
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


_TOWER = load("item163_for_item164", ITEM163)
_EXTENDED = load(
    "item162_for_item164",
    ARCHIVE / "scripts" / "lifted_endpoint_hasse_extended_certificate.py",
)


if __name__ == "__main__":
    main()
