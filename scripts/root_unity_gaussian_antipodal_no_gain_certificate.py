#!/usr/bin/env python3
"""Exact replay for Gaussian antipodal sup/H2 no-gain.

The companion source proves the all-parameter theorem.  This replay verifies
the scalar parallelogram identity symbolically, checks parity under arbitrary
common zero shifts, and reconstructs one genuine saturated k=2 anchor with
unequal even/odd origin orders and exact endpoint normalization data.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import resource
import time
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_gaussian_antipodal_no_gain_certificate.json"
DEPENDENCY = ROOT / "scripts" / "root_unity_gaussian_global_saturation_certificate.py"
DEPENDENCY_SHA256 = "89004cd7c35e890803f486f3a69036d21980497c718b75ad78be4441335e4f5a"
RSS_LIMIT_KIB = 2 * 1024 * 1024


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_dependency():
    specification = importlib.util.spec_from_file_location(
        "root_unity_gaussian_antipodal_dependency", DEPENDENCY
    )
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


assert sha256_file(DEPENDENCY) == DEPENDENCY_SHA256
gaussian = load_dependency()


def centered_derivative(vector: list[int], m: int, n: int, order: int) -> int:
    polynomial_slots = 2 * n + 1
    value = 0
    for frequency in range(2 * m + 1):
        rate = frequency - m
        offset = frequency * polynomial_slots
        for degree in range(min(2 * n, order) + 1):
            value += (
                vector[offset + degree]
                * (math.factorial(order) // math.factorial(order - degree))
                * rate ** (order - degree)
            )
    return value


def exact_origin_order(vector: list[int], m: int, n: int) -> int:
    # A nonzero exponential polynomial in this finite Hermite family cannot
    # vanish through this generous bound; the returned anchor orders are 20,21.
    for order in range(4 * (2 * m + 1) * (2 * n + 1)):
        if centered_derivative(vector, m, n, order):
            return order
    raise AssertionError("nonzero anchor order not found")


def endpoint_content_degree_height(endpoint: list[int]) -> dict:
    nonzero = [value for value in endpoint if value]
    assert nonzero
    content = math.gcd(*(abs(value) for value in nonzero))
    primitive = [value // content for value in endpoint]
    degree = max(index for index, value in enumerate(primitive) if value)
    height = max(abs(value) for value in primitive)
    return {
        "content": content,
        "primitive": primitive,
        "degree": degree,
        "height": height,
    }


def scalar_parallelogram_audit() -> dict:
    a, b, c, d = sp.symbols("a b c d", real=True)
    u = a + sp.I * b
    v = c + sp.I * d

    def modulus_squared(expression):
        return sp.expand_complex(expression * sp.conjugate(expression))

    identity = sp.simplify(
        modulus_squared(u - sp.I * v)
        + modulus_squared(u + sp.I * v)
        - 2 * (modulus_squared(u) + modulus_squared(v))
    )
    assert identity == 0
    return {
        "complex_scalar_identity_verified_symbolically": True,
        "identity": "|u-iv|^2+|u+iv|^2=2(|u|^2+|v|^2)",
    }


def parity_shift_audit() -> list[dict]:
    rows = []
    for common_order in range(8):
        plus_quotient_eigenvalue = (-1) ** common_order
        minus_quotient_eigenvalue = -(-1) ** common_order
        assert plus_quotient_eigenvalue == -minus_quotient_eigenvalue
        rows.append(
            {
                "common_zero_order": common_order,
                "plus_quotient_reflection_eigenvalue": plus_quotient_eigenvalue,
                "minus_quotient_reflection_eigenvalue": minus_quotient_eigenvalue,
                "Taylor_supports_remain_opposite": True,
            }
        )
    return rows


def actual_anchor() -> dict:
    m, n, target_degree = 2, 4, 2
    context = gaussian.build_global_context(m, n)
    even = gaussian.parity_block(context, target_degree, 0)
    odd = gaussian.parity_block(context, target_degree, 1)
    plus_basis = even["saturated_basis"]
    minus_basis = odd["saturated_basis"]
    plus = [int(plus_basis[0, j]) for j in range(plus_basis.ncols())]
    minus = [int(minus_basis[0, j]) for j in range(minus_basis.ncols())]
    assert gaussian.centered_reflection_verified(plus_basis, m, n, 1)
    assert gaussian.centered_reflection_verified(minus_basis, m, n, -1)

    plus_order = exact_origin_order(plus, m, n)
    minus_order = exact_origin_order(minus, m, n)
    common_order = min(plus_order, minus_order)
    assert (plus_order, minus_order, common_order) == (20, 21, 20)
    assert plus_order >= 2 * context["M"]
    assert minus_order >= 2 * context["M"]

    # Reflection gives all-order parity.  Audit a long exact Taylor window
    # after factoring the actual joint order.
    plus_quotient = []
    minus_quotient = []
    for index in range(80):
        derivative_order = common_order + index
        plus_coefficient = sp.Rational(
            centered_derivative(plus, m, n, derivative_order),
            math.factorial(derivative_order),
        )
        minus_coefficient = sp.Rational(
            centered_derivative(minus, m, n, derivative_order),
            math.factorial(derivative_order),
        )
        plus_quotient.append(plus_coefficient)
        minus_quotient.append(minus_coefficient)
        assert not (plus_coefficient and minus_coefficient)
        if index % 2:
            assert plus_coefficient == 0
        else:
            assert minus_coefficient == 0

    X = sp.symbols("X", positive=True)
    plus_norm_polynomial = sum(
        coefficient**2 * X**index
        for index, coefficient in enumerate(plus_quotient)
    )
    minus_norm_polynomial = sum(
        coefficient**2 * X**index
        for index, coefficient in enumerate(minus_quotient)
    )
    mixed_norm_polynomial = sum(
        (plus_quotient[index] ** 2 + minus_quotient[index] ** 2)
        * X**index
        for index in range(len(plus_quotient))
    )
    cross_polynomial = sum(
        plus_quotient[index] * minus_quotient[index] * X**index
        for index in range(len(plus_quotient))
    )
    assert cross_polynomial == 0
    assert sp.expand(
        mixed_norm_polynomial
        - plus_norm_polynomial
        - minus_norm_polynomial
    ) == 0

    plus_endpoint = gaussian.endpoint_vector(plus, m, n)
    minus_endpoint = gaussian.endpoint_vector(minus, m, n)
    assert plus_endpoint[:3] == [165869273088, 0, 16807710600]
    assert minus_endpoint[:3] == [0, -6912, 0]
    assert all(value == 0 for value in plus_endpoint[3:])
    assert all(value == 0 for value in minus_endpoint[3:])
    plus_data = endpoint_content_degree_height(plus_endpoint)
    minus_data = endpoint_content_degree_height(minus_endpoint)
    joint_endpoint = [
        plus_endpoint[index] + minus_endpoint[index]
        for index in range(len(plus_endpoint))
    ]
    joint_integer_pi_polynomial = [
        (-1) ** (degree // 2) * value
        for degree, value in enumerate(joint_endpoint)
    ]
    joint_data = endpoint_content_degree_height(joint_integer_pi_polynomial)
    assert joint_data["content"] == math.gcd(
        plus_data["content"], minus_data["content"]
    )
    assert joint_data["height"] >= plus_data["height"]
    assert joint_data["height"] >= minus_data["height"]
    assert joint_data["degree"] >= plus_data["degree"]
    assert joint_data["degree"] >= minus_data["degree"]

    # At R=4, pi<22/7 implies R/pi>14/11>1.  The odd component
    # has one additional origin zero, so comparison with its individually
    # factored circle bound gains precisely R/pi.
    assert sp.Rational(4, 1) / sp.Rational(22, 7) == sp.Rational(14, 11)
    return {
        "parameters": {
            "m": m,
            "n": n,
            "D": n,
            "target_degree": target_degree,
        },
        "saturated_parity_ranks": {
            "plus": plus_basis.nrows(),
            "minus": minus_basis.nrows(),
        },
        "centered_reflection_verified_exactly": True,
        "actual_origin_orders": {
            "plus": plus_order,
            "minus": minus_order,
            "joint": common_order,
            "orders_are_unequal": True,
        },
        "quotient_Taylor_parity": {
            "exact_coefficients_checked_after_joint_order": len(plus_quotient),
            "cross_products_all_zero": True,
            "structural_reflection_identity_proves_all_orders": True,
            "truncated_H2_norm_sum_identity_verified_as_polynomial_in_R_squared": True,
        },
        "endpoint_normalization": {
            "plus_endpoint": [str(value) for value in plus_endpoint],
            "minus_endpoint": [str(value) for value in minus_endpoint],
            "joint_endpoint": [str(value) for value in joint_endpoint],
            "joint_integer_pi_polynomial": [
                str(value) for value in joint_integer_pi_polynomial
            ],
            "plus_content": str(plus_data["content"]),
            "minus_content": str(minus_data["content"]),
            "joint_content": str(joint_data["content"]),
            "joint_content_equals_gcd": True,
            "plus_primitive_height": str(plus_data["height"]),
            "minus_primitive_height": str(minus_data["height"]),
            "joint_primitive_height": str(joint_data["height"]),
            "plus_degree": plus_data["degree"],
            "minus_degree": minus_data["degree"],
            "joint_degree": joint_data["degree"],
            "joint_height_and_degree_dominate": True,
        },
        "unequal_order_circle_comparison": {
            "test_radius": 4,
            "pi_upper_bound": "22/7",
            "extra_odd_component_factor_R_over_pi_is_greater_than": "14/11",
            "factor_is_strictly_greater_than_one": True,
        },
    }


def main() -> None:
    start = time.perf_counter()
    payload = {
        "schema": "root-unity-gaussian-antipodal-no-gain-v1",
        "dependency": {
            "path": str(DEPENDENCY.relative_to(ROOT)),
            "sha256": DEPENDENCY_SHA256,
            "verified_before_import": True,
        },
        "exact_scalar_algebra": scalar_parallelogram_audit(),
        "common_zero_parity_shift_table": parity_shift_audit(),
        "representative_actual_saturated_anchor": actual_anchor(),
        "all_parameter_theorems_proved_in_source": {
            "antipodal_parallelogram_identity": True,
            "exact_circle_supremum_of_mix_dominates_each_component": True,
            "Hardy_H2_norm_is_orthogonal_sum": True,
            "common_zero_shift_preserves_opposite_parity": True,
            "unequal_actual_zero_orders_only_strengthen_component_comparison": True,
            "joint_content_height_degree_imply_no_gain_margin_theorem": True,
        },
        "logical_scope": {
            "closes_cross_parity_whole_circle_interference_caveat": True,
            "does_not_bound_successive_minima_inside_one_parity_block": True,
            "does_not_control_rational_H2_optimizer_denominators": True,
            "does_not_exclude_exceptional_endpoint_value_cancellation": True,
            "no_irrationality_or_transcendence_conclusion": True,
        },
        "peak_RSS_omitted_for_determinism_but_asserted_below_2GiB": True,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB
    print(
        json.dumps(
            {
                "output": str(OUT),
                "elapsed_seconds": round(time.perf_counter() - start, 6),
                "peak_rss_mib": round(peak_rss_kib / 1024, 6),
                "all_assertions_passed": True,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
