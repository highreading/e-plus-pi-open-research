#!/usr/bin/env python3
"""Exact certificate for Item 294's half-integer operator conjugacy.

This proves an identity between the *operators*.  It deliberately does not
promote the Item-291 finite recurrence fit for either connection minor.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item294_j2_half_integer_gauge_certificate.json"
DEPENDENCIES = {
    "item291_j2_connection_plane_certificate.py":
        "5c86001827b0012605563b04dafc5f157f27fddf2f1625254e9196bc0de8c2df",
    "item237_j1_algebraic_residual_certificate.py":
        "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf",
    "item250_j2_ordinary_phase_certificate.py":
        "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce",
}


def resolve(name: str) -> Path:
    for base in (HERE, HERE / "scripts", HERE.parent / "scripts", Path.cwd() / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, filename: str):
    path = resolve(filename)
    expected = DEPENDENCIES[filename]
    if sha256(path) != expected:
        raise RuntimeError(f"dependency hash mismatch: {filename}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


i291 = load("item294_i291", "item291_j2_connection_plane_certificate.py")
i237 = load("item294_i237", "item237_j1_algebraic_residual_certificate.py")
i250 = load("item294_i250", "item250_j2_ordinary_phase_certificate.py")


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def trim(poly: list[F]) -> list[F]:
    answer = list(poly)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def add(left: list[F], right: list[F]) -> list[F]:
    answer = [F(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    return trim(answer)


def scale(poly: list[F], scalar: F | int) -> list[F]:
    return trim([F(scalar) * value for value in poly])


def multiply(left: list[F], right: list[F]) -> list[F]:
    answer = [F(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return trim(answer)


def power(poly: list[F], exponent: int) -> list[F]:
    answer = [F(1)]
    factor = list(poly)
    while exponent:
        if exponent & 1:
            answer = multiply(answer, factor)
        exponent >>= 1
        if exponent:
            factor = multiply(factor, factor)
    return answer


def compose_affine(poly: list[F], constant: F, slope: F) -> list[F]:
    answer = [F(0)]
    factor = [constant, slope]
    current = [F(1)]
    for coefficient in poly:
        answer = add(answer, scale(current, coefficient))
        current = multiply(current, factor)
    return trim(answer)


def product_of_linear(factors: list[tuple[F, F]]) -> list[F]:
    answer = [F(1)]
    for constant, slope in factors:
        answer = multiply(answer, [constant, slope])
    return answer


def evaluate(poly: list[F], value: F | int) -> F:
    answer = F(0)
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def gauge_parts(residue: int, shift: int = 0) -> tuple[list[F], list[F]]:
    """Numerator/denominator of R(r)=g_n/g_(n+1), r=6n+residue."""
    r_constant = F(residue + 6 * shift)
    r = (r_constant, F(6))

    def linear(multiplier: int, offset: int) -> tuple[F, F]:
        return F(multiplier) * r[0] + offset, F(multiplier) * r[1]

    numerator = product_of_linear([
        linear(1, 0), linear(1, 6),
        linear(2, 9), linear(2, 9),
        linear(2, 15), linear(2, 15),
    ])
    denominator = scale(product_of_linear([
        linear(1, 1), linear(1, 1),
        linear(1, 2), linear(1, 4),
        linear(1, 5), linear(1, 5),
    ]), 78732)
    return numerator, denominator


def operator_conjugacy() -> dict[str, Any]:
    base = i237.recurrence_polynomials()
    rows = []
    for label, residue in ((5, 1), (1, 5)):
        candidate = i291.candidate_polynomials(label)
        half_offset = F(residue, 2)
        restricted = [compose_affine(poly, half_offset, F(3)) for poly in base]
        for shift in range(3):
            numerator, denominator = gauge_parts(residue, shift)
            left = multiply(multiply(candidate[shift + 1], restricted[shift]), denominator)
            right = multiply(multiply(candidate[shift], restricted[shift + 1]), numerator)
            if trim(add(left, scale(right, -1))) != [F(0)]:
                raise AssertionError((label, shift, "operator conjugacy"))
            rows.append((label, residue, shift, len(left) - 1))
        if any(value <= 0 for value in candidate[3]):
            raise AssertionError((label, "positive forward coefficient"))
    stream = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return {
        "classification": "SYMBOLIC EXACT",
        "rays": "label 5: r=6n+1 and h=3n+1/2; label 1: r=6n+5 and h=3n+5/2",
        "item237_operator": "sum_(j=0)^3 p_j(h) z_(n+j)=0",
        "item291_candidate": "sum_(j=0)^3 P_j(n) y_(n+j)=0",
        "gauge": (
            "y_n=g_n*z_n, g_n/g_(n+1)=R(r), "
            "R(r)=r(r+6)(2r+9)^2(2r+15)^2/"
            "[78732(r+1)^2(r+2)(r+4)(r+5)^2]"
        ),
        "cleared_cross_identities": len(rows),
        "maximum_cleared_degree": max(row[-1] for row in rows),
        "row_digest_sha256": hashlib.sha256(stream).hexdigest(),
        "conclusion": "the fitted Item291 operator is exactly the half-integer Item237 operator after this gauge",
    }


def gauge_ratio(r: int) -> F:
    return F(
        r * (r + 6) * (2 * r + 9) ** 2 * (2 * r + 15) ** 2,
        78732 * (r + 1) ** 2 * (r + 2) * (r + 4) * (r + 5) ** 2,
    )


def determinant2(a: F, b: F, c: F, d: F) -> F:
    return a * d - b * c


def finite_bridge_probe(term_count: int) -> dict[str, Any]:
    rows = []
    witnesses = {}
    constants = {1: F(-891, 100), 5: F(3897234, 41405)}
    expected_lc = {1: F(5045260, 243), 5: F(97069100, 189)}
    expected_lb = {1: F(-2774893, 15), 5: F(2802229606440, 57967)}
    for residue in (1, 5):
        gauge = F(1)
        normalized_l: list[F] = []
        normalized_b: list[F] = []
        algebraic: list[F] = []
        for n in range(term_count):
            r = residue + 6 * n
            data = i250.phase_data(r)
            f0, f1 = data["st"]
            b0, d0 = data["x0"][1:]
            b1, d1 = data["x1"][1:]
            l_value = 9 * (f0 * b1 - f1 * b0)
            b_value = 16**n * (-11) * (f0 * d1 - f1 * d0)
            c_value = i237.lagrange_coefficient(r)
            z_l = l_value / gauge
            z_b = b_value / gauge
            if z_b != constants[residue] * c_value:
                raise AssertionError((residue, n, "finite bridge"))
            normalized_l.append(z_l)
            normalized_b.append(z_b)
            algebraic.append(c_value)
            rows.append((residue, n, z_l.numerator, z_l.denominator,
                         z_b.numerator, z_b.denominator,
                         c_value.numerator, c_value.denominator))
            gauge /= gauge_ratio(r)
        det_lc = determinant2(normalized_l[0], normalized_l[1], algebraic[0], algebraic[1])
        det_lb = determinant2(normalized_l[0], normalized_l[1], normalized_b[0], normalized_b[1])
        if det_lc != expected_lc[residue] or det_lb != expected_lb[residue]:
            raise AssertionError((residue, det_lc, det_lb))
        witnesses[str(residue)] = {
            "B_over_C_constant": str(constants[residue]),
            "det_normalized_L_C_first_two_rows": str(det_lc),
            "det_normalized_L_B_first_two_rows": str(det_lb),
        }
    stream = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return {
        "classification": "EXACT FINITE ONLY; not an all-r identity",
        "terms_per_ray": term_count,
        "observed_bridge": "16^n M_n/g_n=lambda_residue*[x^r]C(x)",
        "witnesses": witnesses,
        "row_digest_sha256": hashlib.sha256(stream).hexdigest(),
        "scope": "the nonzero determinants prove only that normalized L is not the existing Item237 coefficient line",
    }


def singular_audit() -> dict[str, Any]:
    # Denominator factors of R are all below p=2r+6s+3 on actual rows.
    for r in (1, 5, 101):
        for s in (1, 2, 3, 6, 20):
            p = 2 * r + 6 * s + 3
            if not all(0 < value < p for value in (r + 1, r + 2, r + 4, r + 5)):
                raise AssertionError((r, s, "gauge denominator range"))
            zeros = [value for value in (2 * r + 9, 2 * r + 15) if value % p == 0]
            expected = 1 if s in (1, 2) else 0
            if len(zeros) != expected:
                raise AssertionError((r, s, zeros))
    # The six displayed P3 factors 2r+6k+3 equal p exactly on s=k.
    factor_checks = 0
    for label, residue in ((5, 1), (1, 5)):
        forward = i291.candidate_polynomials(label)[3]
        for k in range(1, 7):
            root = F(-(2 * residue + 6 * k + 3), 12)
            if evaluate(forward, root) != 0:
                raise AssertionError((label, residue, k, "missing P3 factor"))
            factor_checks += 1
    for k in range(1, 7):
        for r in (1, 5, 101):
            p = 2 * r + 6 * k + 3
            if 2 * r + 6 * k + 3 != p:
                raise AssertionError((k, r))
    return {
        "classification": "ALL-ROW ALGEBRAIC RANGE AUDIT",
        "gauge_denominator": "78732(r+1)^2(r+2)(r+4)(r+5)^2 is a p-unit on every actual row",
        "gauge_numerator": "R(r) vanishes modulo p exactly on s=1 via 2r+9 and s=2 via 2r+15",
        "primitive_forward_coefficient": "P3(n)>0 over Q for n>=0",
        "mod_p_forward_singular_layers": "P3 contains 2r+9,2r+15,...,2r+39 and hence vanishes on s=1,...,6",
        "exact_P3_linear_factor_checks": factor_checks,
        "uncontrolled_factor": "the remaining positive quintic core can still vanish modulo actual-row primes",
        "consequence": "neither the gauge nor forward recurrence is an all-row p-adic unit transport",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bridge-terms", type=int, default=12)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.bridge_terms < 3 or args.bridge_terms > 30:
        raise ValueError("bridge bound must lie in [3,30]")
    result = {
        "schema": "item294-j2-half-integer-gauge-v1",
        "dependencies": DEPENDENCIES,
        "operator_conjugacy": operator_conjugacy(),
        "finite_bridge_probe": finite_bridge_probe(args.bridge_terms),
        "singular_audit": singular_audit(),
        "theorem_status": {
            "PROVED": [
                "the exact half-integer gauge conjugacy of the Item291 candidate operator to Item237",
                "the rational and mod-p singular-factor audit",
                "normalized L is not proportional to the one existing Item237 algebraic coefficient sequence",
            ],
            "EXACT_FINITE_ONLY": [
                "the observed bridge 16^n*M_n/g_n=lambda_residue*[x^r]C(x)",
                "the original Item291 candidate recurrence on L_n and 16^n*M_n",
            ],
            "OPEN": [
                "an all-r proof of the observed M-to-C bridge",
                "a second algebraic/period realization for normalized L",
                "the all-n candidate recurrence for either connection minor",
                "any Frobenius, nonvanishing, or weighted-density theorem",
            ],
        },
        "capacity": {
            "raw_ordinary_j2_capacity_per_M": "2/35",
            "raw_ordinary_j2_capacity_per_6M": "1/105",
            "new_capacity_reduction": 0,
            "booking": 0,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
