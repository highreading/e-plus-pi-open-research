#!/usr/bin/env python3
"""Exact finite replay for the cardinal Newton arithmetic theorem.

The companion source proves the all-parameter residue formula, denominator
sandwich, primitive-content cap, and height bounds.  This checker reconstructs
all three cardinal families over QQ.  It is deliberately finite evidence for
the formulas, not the proof of their universal scope.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp

import root_unity_gamma_augmented_newton_certificate as base


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_cardinal_newton_arithmetic_certificate.json"
x = base.x


def convolution(a: list[sp.Rational], b: list[sp.Rational], cutoff: int) -> list[sp.Rational]:
    result = [sp.Rational(0)] * min(cutoff + 1, len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            if i + j <= cutoff:
                result[i + j] += left * right
    return result


def local_jet(family: str, node: int, order: int, h: int, nu: int) -> sp.Rational:
    """Normalized Taylor coefficient at the integer rate node."""
    if family == "even-Lambda0-scaled":
        return (
            2
            * (-1) ** (node - 1)
            * sp.binomial(2 * order, order)
            / sp.Integer(4) ** order
            / sp.Integer(2 * node - 1) ** (2 * order + 1)
        )
    if family == "odd-Lambda0":
        central_power = (nu + 1) // 2
        if node % 2 == 0:
            return sp.Rational(0)
        return (
            2
            * sp.binomial(central_power + order - 1, order)
            / sp.Integer(node) ** (2 * (central_power + order))
        )
    if family == "odd-Lambda1-defect":
        epsilon = (-1) ** node
        half_h = h // 2
        return (
            (1 - epsilon) * sp.binomial(half_h + order - 1, order)
            + epsilon
            * sp.rf(sp.Rational(h + 1, 2), order)
            / sp.factorial(order)
        ) / sp.Integer(node) ** (h + 2 * order)
    raise ValueError(family)


def integer_base_rates(family: str, k: int) -> list[sp.Integer]:
    if family == "even-Lambda0-scaled":
        return [sp.Integer((2 * node - 1) ** 2) for node in range(1, k + 1)]
    return [sp.Integer(node * node) for node in range(1, k + 1)]


def residue_newton_coefficient(
    family: str, k: int, h: int, nu: int, degree: int
) -> sp.Rational:
    """Exact local-germ residue formula for one confluent Newton coefficient."""
    full_blocks, within_block = divmod(degree, h)
    block_count = full_blocks + 1
    multiplicities = [h] * full_blocks + [within_block + 1]
    rates = integer_base_rates(family, block_count)
    answer = sp.Rational(0)
    for j in range(block_count):
        target = multiplicities[j] - 1
        series = [local_jet(family, j + 1, order, h, nu) for order in range(target + 1)]
        pole = -rates[j]
        for ell in range(block_count):
            if ell == j:
                continue
            difference = pole - (-rates[ell])
            multiplicity = multiplicities[ell]
            factor = [
                (-1) ** order
                * sp.binomial(multiplicity + order - 1, order)
                / difference ** (multiplicity + order)
                for order in range(target + 1)
            ]
            series = convolution(series, factor, target)
        answer += series[target]
    return sp.factor(answer)


def denominator_lcm(values: list[sp.Rational]) -> int:
    answer = 1
    for value in values:
        answer = int(sp.ilcm(answer, int(sp.denom(value))))
    return answer


def primitive_denominator_content(poly: sp.Poly) -> tuple[int, int, list[int]]:
    denominator = denominator_lcm(list(map(sp.Rational, poly.all_coeffs())))
    integers = [int(coefficient * denominator) for coefficient in poly.all_coeffs()]
    content = 0
    for value in integers:
        content = math.gcd(content, abs(value))
    return denominator, content, integers


def explicit_denominator_upper(family: str, k: int, h: int, nu: int) -> int:
    rates = list(map(int, integer_base_rates(family, k)))
    if family == "even-Lambda0-scaled":
        local = 4 ** (h - 1) * math.prod(
            (2 * node - 1) ** (2 * h - 1) for node in range(1, k + 1)
        )
    elif family == "odd-Lambda0":
        central_power = (nu + 1) // 2
        local = math.prod(
            node ** (2 * (central_power + h - 1)) for node in range(1, k + 1)
        )
    else:
        local = 4 ** (h - 1) * math.prod(
            node ** (3 * h - 2) for node in range(1, k + 1)
        )
    cross = math.prod(
        (rates[j] - rates[i]) ** (2 * h - 1)
        for i in range(k)
        for j in range(i + 1, k)
    )
    return local * cross


def local_denominator_lower(family: str, k: int, h: int, nu: int) -> int:
    return denominator_lcm(
        [
            local_jet(family, node, order, h, nu)
            for node in range(1, k + 1)
            for order in range(h)
        ]
    )


def jet_absolute_bound(family: str, h: int, nu: int) -> sp.Rational:
    if family == "even-Lambda0-scaled":
        return sp.Integer(2)
    if family == "odd-Lambda0":
        central_power = (nu + 1) // 2
        return 2 * sp.binomial(central_power + h - 2, h - 1)
    half_h = h // 2
    order = h - 1
    return (
        2 * sp.binomial(half_h + order - 1, order)
        + sp.rf(sp.Rational(h + 1, 2), order) / sp.factorial(order)
    )


def rational_height_bound(family: str, k: int, h: int, nu: int) -> sp.Rational:
    rates = base.repeated_rates(
        2 * k if family == "even-Lambda0-scaled" else 2 * k + 1, h
    )
    if family == "even-Lambda0-scaled":
        rates = [4 * rate for rate in rates]
    prefix_l1 = sp.Integer(1)
    total = sp.Integer(0)
    for degree, rate in enumerate(rates):
        total += sp.Integer(2) ** degree * prefix_l1
        if degree < len(rates) - 1:
            prefix_l1 *= 1 + rate
    return sp.factor(k * jet_absolute_bound(family, h, nu) * total)


def normalized_cardinal(family: str, k: int, n: int) -> tuple[sp.Poly, list[sp.Rational]]:
    h = n + 1
    if family == "even-Lambda0-scaled":
        m = 2 * k
        cardinal = base.polynomial_crt_cardinal(m, n, 0)
        numerator, _ = base.normalize_positive(
            base.odd_center_transform(cardinal, sp.Rational(m - 1, 2))
        )
        numerator = sp.Poly(numerator.as_expr().subs(x, x / 4), x, domain=sp.QQ)
        rates = [sp.Integer((2 * node - 1) ** 2) for node in range(1, k + 1) for _ in range(h)]
    elif family == "odd-Lambda0":
        m = 2 * k + 1
        cardinal = base.polynomial_crt_cardinal(m, n, 0)
        numerator, _ = base.normalize_positive(
            base.even_flat_transform(
                cardinal,
                sp.Integer(k),
                sp.Integer((-1) ** k),
                h + h % 2,
            )
        )
        rates = [sp.Integer(node * node) for node in range(1, k + 1) for _ in range(h)]
    elif family == "odd-Lambda1-defect":
        assert n % 2 == 1
        m = 2 * k + 1
        cardinal = base.polynomial_crt_cardinal(m, n, 1)
        numerator, _ = base.normalize_positive(
            base.odd_flat_transform(
                cardinal,
                sp.Integer(k),
                sp.Integer((-1) ** k),
                h + 1,
            )
        )
        rates = [sp.Integer(node * node) for node in range(1, k + 1) for _ in range(h)]
    else:
        raise ValueError(family)
    return numerator, rates


def check_row(family: str, k: int, n: int) -> dict:
    h = n + 1
    nu = 2 * (n // 2) + 1
    numerator, rates = normalized_cardinal(family, k, n)
    coefficients = base.newton_coefficients(numerator, rates)
    residues = [
        residue_newton_coefficient(family, k, h, nu, degree)
        for degree in range(k * h)
    ]
    assert coefficients == residues
    assert all(value > 0 for value in coefficients)

    # Check every local jet directly from the polynomial.
    distinct_rates = integer_base_rates(family, k)
    for node, rate in enumerate(distinct_rates, 1):
        for order in range(h):
            actual = sp.diff(numerator.as_expr(), x, order).subs(x, -rate) / sp.factorial(order)
            assert sp.factor(actual - local_jet(family, node, order, h, nu)) == 0

    q_n, content, integer_coefficients = primitive_denominator_content(numerator)
    q_newton = denominator_lcm(coefficients)
    assert q_n == q_newton
    assert math.gcd(q_n, content) == 1
    if family == "even-Lambda0-scaled":
        assert coefficients[0] == 2 and coefficients[2] == sp.Rational(3, 4)
        assert content == 1
    elif family == "odd-Lambda0":
        assert coefficients[0] == 2 and content in (1, 2)
    else:
        assert coefficients[0] == 1 and content == 1

    endpoint_coordinate_content = None
    endpoint_coordinate_content_bound = None
    if family == "even-Lambda0-scaled":
        primitive_poly = sp.Poly(
            sp.cancel(sp.Integer(q_n) * numerator.as_expr() / content),
            x,
            domain=sp.ZZ,
        )
        endpoint_poly = sp.Poly(
            primitive_poly.as_expr().subs(x, -(2 * x - (2 * k - 1)) ** 2),
            x,
            domain=sp.ZZ,
        )
        endpoint_coordinate_content = 0
        for value in endpoint_poly.all_coeffs():
            endpoint_coordinate_content = math.gcd(
                endpoint_coordinate_content, abs(int(value))
            )
        endpoint_coordinate_content_bound = 2 ** (2 * numerator.degree())
        assert endpoint_coordinate_content > 0
        assert endpoint_coordinate_content & (endpoint_coordinate_content - 1) == 0
        assert endpoint_coordinate_content <= endpoint_coordinate_content_bound

    local_lower = local_denominator_lower(family, k, h, nu)
    denominator_upper = explicit_denominator_upper(family, k, h, nu)
    assert q_n % local_lower == 0
    assert denominator_upper % q_n == 0

    primitive_height = max(abs(value // content) for value in integer_coefficients)
    # All Newton coefficients and all integer-rate prefix coefficients are
    # positive.  Hence the constant monomial coefficient is at least gamma_0,
    # so primitive height is at least q_n in all three families.
    lower_height = sp.Integer(q_n)
    upper_rational_height = rational_height_bound(family, k, h, nu)
    upper_primitive_height = denominator_upper * upper_rational_height
    assert primitive_height >= lower_height
    assert primitive_height <= upper_primitive_height

    digest = hashlib.sha256(
        ",".join(f"{sp.numer(v)}/{sp.denom(v)}" for v in coefficients).encode()
    ).hexdigest()
    return {
        "family": family,
        "k": k,
        "m": 2 * k if family == "even-Lambda0-scaled" else 2 * k + 1,
        "n": n,
        "h": h,
        "nu": nu,
        "degree": numerator.degree(),
        "first_newton_coefficient": str(coefficients[0]),
        "last_newton_coefficient": str(coefficients[-1]),
        "newton_sha256": digest,
        "least_denominator": str(q_n),
        "local_jet_denominator_lcm": str(local_lower),
        "explicit_denominator_upper": str(denominator_upper),
        "primitive_content": content,
        "endpoint_coordinate_induced_content": (
            str(endpoint_coordinate_content)
            if endpoint_coordinate_content is not None
            else None
        ),
        "proved_endpoint_coordinate_content_bound": (
            str(endpoint_coordinate_content_bound)
            if endpoint_coordinate_content_bound is not None
            else None
        ),
        "primitive_height": str(primitive_height),
        "proved_height_lower": str(lower_height),
        "proved_height_upper": str(upper_primitive_height),
        "all_local_jets_exact": True,
        "all_residue_formulas_exact": True,
    }


def main() -> None:
    rows: list[dict] = []
    digest = hashlib.sha256()
    for family in ("even-Lambda0-scaled", "odd-Lambda0"):
        for k in range(1, 4):
            for n in range(2, 6):
                row = check_row(family, k, n)
                rows.append(row)
                digest.update(
                    f"{family},{k},{n},{row['newton_sha256']},{row['least_denominator']},{row['primitive_content']},{row['endpoint_coordinate_induced_content']}\n".encode()
                )
    for k in range(1, 4):
        for n in (3, 5):
            row = check_row("odd-Lambda1-defect", k, n)
            rows.append(row)
            digest.update(
                f"defect,{k},{n},{row['newton_sha256']},{row['least_denominator']},{row['primitive_content']},{row['endpoint_coordinate_induced_content']}\n".encode()
            )

    selected_keys = {
        ("even-Lambda0-scaled", 3, 5),
        ("odd-Lambda0", 3, 4),
        ("odd-Lambda1-defect", 3, 5),
    }
    payload = {
        "schema": "root-unity-cardinal-newton-arithmetic-v1",
        "exact_arithmetic": "QQ only; no floating-point comparisons",
        "grid": {
            "generic_k_range": [1, 3],
            "generic_n_range": [2, 5],
            "defect_k_range": [1, 3],
            "defect_n_values": [3, 5],
            "row_count": len(rows),
            "all_local_jet_formulas_exact": True,
            "all_confluent_residue_formulas_exact": True,
            "all_least_denominators_equal_in_newton_and_monomial_bases": True,
            "all_local_lower_divisors_exact": True,
            "all_explicit_upper_multiples_exact": True,
            "all_content_caps_exact": True,
            "all_even_endpoint_coordinate_contents_dyadic_and_bounded": True,
            "all_height_bounds_verified": True,
            "row_digest_sha256": digest.hexdigest(),
        },
        "selected_rows": [
            row for row in rows if (row["family"], row["k"], row["n"]) in selected_keys
        ],
        "logical_scope": {
            "proved_in_companion_source": (
                "The formulas, denominator sandwich, content cap, and height bounds are all-parameter theorems; the grid only replays them."
            ),
            "cardinal_content_result": (
                "In integer-rate coordinates, intrinsic content is 1 for even Lambda0 and defect Lambda1, and at most 2 for odd Lambda0."
            ),
            "even_coordinate_warning": (
                "Returning scaled even Lambda0 to the endpoint variable can create dyadic content; universally it is at most 2^(2(kh-1)), and the checker records it exactly."
            ),
            "corrected_endpoint_warning": (
                "This does not bound corrected Delta content or saturated endpoint Pluecker height; those require the special kernel and W-Gamma contraction."
            ),
        },
        "versions": {"sympy": sp.__version__},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["grid"], indent=2, sort_keys=True))
    print(json.dumps(payload["selected_rows"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
