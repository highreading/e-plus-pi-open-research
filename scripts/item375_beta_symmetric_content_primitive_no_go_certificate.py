#!/usr/bin/env python3
"""Deterministic exact replay for Item 375.

Checks predeclared sparse-polynomial content normalizations, the exact scalar
valuation rule, mandatory singleton/content saturation, portfolios, and the
height inequality.  It performs no actual target, prime, or load census.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from functools import reduce
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "results/item316_beta_intermediate_ostrowski_no_go_certificate.json": (
        "5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "manifests/item316_beta_intermediate_ostrowski_no_go_manifest.json": (
        "aac741658430fb661de078adfeafdbc3a9d20312a8fd8725cb4244d406d9bcf6"
    ),
    "sources/item358_beta_actual_low_incidence_saturation_barrier_report.md": (
        "681c9f9cbe926978c78f632084c8be83439c2ac3f5e50f2c2697a49f2f0da68d"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_certificate.json": (
        "4da88e55dec36f3c130def549007c8ae1509ff0a029dfed9ff25f67a78c2ffa3"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_root_audit.json": (
        "a1a48f7d7080834ebf3be56b47d8056733e88e1913e8f6ea784f97a5eb2d9172"
    ),
    "manifests/item358_beta_actual_low_incidence_saturation_barrier_manifest.json": (
        "4ba799fe2fc8cb6063034d844f91bcaec6c3fc84d043b1f46c675fce400acfb1"
    ),
    "sources/item370_beta_q_free_residual_saturation_no_go_report.md": (
        "760767813ab0bbd56114f6a6c264ce396ccc2ec8eb9e7a3139e56b155051fef4"
    ),
    "results/item370_beta_q_free_residual_saturation_no_go_certificate.json": (
        "78703c11fee6715189fc8c0c7a513bef5eda1d973ab27b3e1f486d0b908008fb"
    ),
    "results/item370_beta_q_free_residual_saturation_no_go_root_audit.json": (
        "264c64d6495c2d1a20eff67b270379adb95ffc5f5711269dc325f11988c12ea2"
    ),
    "manifests/item370_beta_q_free_residual_saturation_no_go_manifest.json": (
        "53147f04c406d69c67f3b53b7032d6c90db20380583ebb79238f84505cd6d6d2"
    ),
    "sources/item373_beta_symmetric_singleton_first_quotient_report.md": (
        "daa16600359a52501fcbe303359e39696c1f0b0acfdb62b944b19be77784d6c5"
    ),
    "scripts/item373_beta_symmetric_singleton_first_quotient_certificate.py": (
        "8158fd3e100c1a7abb5efa0048a979a6e368e7328ae67743731041b756944bcf"
    ),
    "results/item373_beta_symmetric_singleton_first_quotient_certificate.json": (
        "335be8c519597bc1fd1a6e21cb9bbbbe37b1785a2468e4f0a7d6c205a9cb2cc5"
    ),
    "results/item373_beta_symmetric_singleton_first_quotient_ledger_delta.json": (
        "6d2193aecb20165fd44082c5e0a2959756e7f62bbac7e35efd6ac5be76b28a39"
    ),
    "results/item373_beta_symmetric_singleton_first_quotient_root_audit.json": (
        "3b5d6b13fdd327e27b518744edd2666cc58895fb401f7050ad52046810bb1128"
    ),
    "manifests/item373_beta_symmetric_singleton_first_quotient_manifest.json": (
        "a42cd4b5e306b5fe864e4832e11726380d9bf4197868884f1879dc98b91aeacf"
    ),
}


Monomial = tuple[int, int]
Polynomial = dict[Monomial, int]


def digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def dependency_audit() -> dict[str, Any]:
    root = Path(__file__).resolve().parent.parent
    rows = []
    for relative_path, expected in DEPENDENCY_HASHES.items():
        payload = (root / relative_path).read_bytes()
        actual = hashlib.sha256(payload).hexdigest()
        assert actual == expected, (relative_path, actual, expected)
        rows.append(
            {"path": relative_path, "bytes": len(payload), "sha256": actual}
        )
    return {"count": len(rows), "rows": rows, "rows_digest": digest(rows)}


def clean(poly: Polynomial) -> Polynomial:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def coefficient_content(poly: Polynomial) -> int:
    poly = clean(poly)
    assert poly
    return reduce(math.gcd, (abs(value) for value in poly.values()))


def scale(poly: Polynomial, scalar: int) -> Polynomial:
    assert scalar != 0
    return clean({monomial: scalar * coefficient for monomial, coefficient in poly.items()})


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for (lx, ly), lc in left.items():
        for (rx, ry), rc in right.items():
            key = (lx + rx, ly + ry)
            result[key] = result.get(key, 0) + lc * rc
    return clean(result)


def primitive_part(poly: Polynomial) -> Polynomial:
    content = coefficient_content(poly)
    result = {monomial: coefficient // content for monomial, coefficient in poly.items()}
    highest = max(result)
    if result[highest] < 0:
        result = {monomial: -coefficient for monomial, coefficient in result.items()}
    return clean(result)


def evaluate(poly: Polynomial, x_value: int, y_value: int) -> int:
    return sum(
        coefficient * x_value**x_power * y_value**y_power
        for (x_power, y_power), coefficient in poly.items()
    )


def valuation(value: int, prime: int) -> int:
    assert value != 0 and prime > 1
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def radical(value: int) -> int:
    value = abs(value)
    assert value > 0
    answer = 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            answer *= divisor
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        answer *= value
    return answer


def symmetric_data(loads: list[int], t_value: int) -> dict[str, int]:
    assert loads and all(load > 0 for load in loads)
    product = math.prod(loads)
    top_derivative = sum(product // load for load in loads)
    exponent = len(loads)
    saturated = product // math.gcd(product, abs(t_value * top_derivative) ** exponent)
    return {"P": product, "E": top_derivative, "N": exponent, "S_sym": saturated}


def normalization_controls() -> dict[str, Any]:
    one: Polynomial = {(0, 0): 1}
    x_plus_y: Polynomial = {(1, 0): 1, (0, 1): 1}
    x_plus_two: Polynomial = {(1, 0): 1, (0, 0): 2}
    y_plus_three: Polynomial = {(0, 1): 1, (0, 0): 3}
    declared = [
        {
            "name": "fully_scalar_after_common_polynomial_cancellation",
            "a": 18,
            "b": 30,
            "H": x_plus_y,
            "A1": one,
            "B1": one,
        },
        {
            "name": "content_degenerate_numerator_variable_unit_denominator",
            "a": 42,
            "b": 30,
            "H": x_plus_two,
            "A1": one,
            "B1": y_plus_three,
        },
        {
            "name": "nonconstant_primitive_branch_boundary",
            "a": 14,
            "b": 21,
            "H": y_plus_three,
            "A1": x_plus_two,
            "B1": x_plus_y,
        },
    ]
    rows = []
    for case in declared:
        a = case["a"]
        b = case["b"]
        H = case["H"]
        A1 = case["A1"]
        B1 = case["B1"]
        A = scale(multiply(H, A1), a)
        B = scale(multiply(H, B1), b)
        assert coefficient_content(A) == a
        assert coefficient_content(B) == b
        assert primitive_part(A) == multiply(H, A1)
        assert primitive_part(B) == multiply(H, B1)
        common_scalar = math.gcd(a, b)
        alpha = a // common_scalar
        beta = b // common_scalar
        assert math.gcd(alpha, beta) == 1
        point_rows = []
        for x_value, y_value in [(2, 5), (7, 11), (13, 17)]:
            left = evaluate(A, x_value, y_value) * beta * evaluate(B1, x_value, y_value)
            right = evaluate(B, x_value, y_value) * alpha * evaluate(A1, x_value, y_value)
            assert left == right
            point_rows.append({"X": x_value, "Y": y_value, "cross_product": left})
        rows.append(
            {
                "name": case["name"],
                "content_A": a,
                "content_B": b,
                "reduced_alpha": alpha,
                "reduced_beta": beta,
                "A1_constant_primitive": A1 == one,
                "B1_constant_primitive": B1 == one,
                "point_rows": point_rows,
            }
        )
    constant_rows = []
    for constant in [-60, -1, 1, 42]:
        poly = {(0, 0): constant}
        primitive = primitive_part(poly)
        assert primitive == one
        constant_rows.append(
            {
                "constant": constant,
                "content": coefficient_content(poly),
                "canonical_primitive_part": primitive[0, 0],
            }
        )
    return {
        "rows": rows,
        "rows_digest": digest(rows),
        "constant_primitive_rows": constant_rows,
        "constant_primitive_rows_digest": digest(constant_rows),
    }


def actual_saturation_controls() -> dict[str, Any]:
    capital_A = 20
    loads = [2 * 23, 3 * 29, 7]
    assert all(0 < load < capital_A**2 for load in loads)
    t_value = 5
    data = symmetric_data(loads, t_value)
    t_zero_data = symmetric_data(loads, 0)
    assert t_zero_data["S_sym"] == 1
    q_squarefree = 23 * 29
    u_11 = math.gcd(q_squarefree, radical(data["S_sym"]))
    assert u_11 == 23 * 29
    rows = []
    for alpha in [1, 23 * 17, 29 * 19, 23 * 29, 5 * 23 * 29]:
        t_away_alpha_radical = radical(alpha) // math.gcd(radical(alpha), radical(t_value))
        explicit = math.gcd(
            math.gcd(q_squarefree, radical(data["S_sym"])), t_away_alpha_radical
        )
        compact = math.gcd(u_11, radical(alpha))
        assert explicit == compact
        assert compact <= abs(alpha)
        rows.append(
            {
                "alpha": alpha,
                "rad_alpha": radical(alpha),
                "captured_content": compact,
                "captures_all_U11": compact == u_11,
            }
        )
    return {
        "capital_A": capital_A,
        "declared_loads": loads,
        "t": t_value,
        "P": data["P"],
        "E": data["E"],
        "S_sym": data["S_sym"],
        "Q_squarefree": q_squarefree,
        "U_11": u_11,
        "t_zero_S_sym": t_zero_data["S_sym"],
        "rows": rows,
        "rows_digest": digest(rows),
    }


def valuation_controls() -> dict[str, Any]:
    p_value = 23
    P_value = 2 * p_value * 7
    E_value = 31
    assert valuation(P_value, p_value) == 1
    assert E_value % p_value != 0
    rows = []
    for alpha, beta, denominator_value in [
        (1, 5, 7),
        (23, 5, 7),
        (23**2 * 11, 5, 7),
        (29, 5, 7),
    ]:
        assert (beta * denominator_value) % p_value != 0
        residual_valuation = valuation(alpha, p_value) if alpha % p_value == 0 else 0
        product_valuation = valuation(P_value * alpha, p_value)
        denominator_valuation = 0
        assert residual_valuation == valuation(alpha, p_value) - denominator_valuation
        assert product_valuation == 1 + residual_valuation
        assert (product_valuation >= 2) == (alpha % p_value == 0)
        rows.append(
            {
                "prime": p_value,
                "alpha": alpha,
                "beta": beta,
                "B1_at_actual_point": denominator_value,
                "residual_valuation": residual_valuation,
                "P_times_residual_valuation": product_valuation,
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def representation_and_integrality_controls() -> dict[str, Any]:
    primitive_pair_height = 1
    alphas = [1, 23 * 29, 23 * 29 * 31 * 37]
    support_rows = []
    for alpha in alphas:
        support_rows.append(
            {
                "alpha": alpha,
                "primitive_pair_height": primitive_pair_height,
                "radical": radical(alpha),
            }
        )
    assert len({row["primitive_pair_height"] for row in support_rows}) == 1
    assert len({row["radical"] for row in support_rows}) == len(support_rows)

    P_value = 46
    denominator_value = 1 + P_value
    alpha = 23 * denominator_value
    assert alpha % denominator_value == 0
    integral_residual = alpha // denominator_value
    assert integral_residual == 23
    return {
        "same_primitive_height_different_scalar_support": support_rows,
        "integral_specialization": {
            "P": P_value,
            "B1_P_E": denominator_value,
            "alpha": alpha,
            "integral_residual": integral_residual,
        },
    }


def portfolio_and_height_controls() -> dict[str, Any]:
    target_primes = [23, 29, 31]
    u_value = math.prod(target_primes)
    portfolios = [
        [23, 29, 31],
        [23 * 37, 29 * 41, 31 * 43],
        [23 * 29, 31],
    ]
    portfolio_rows = []
    for alphas in portfolios:
        alpha_product = math.prod(alphas)
        captured = math.gcd(u_value, radical(alpha_product))
        assert captured == u_value
        assert math.log(captured) <= sum(math.log(abs(alpha)) for alpha in alphas) + 1e-12
        portfolio_rows.append(
            {
                "alphas": alphas,
                "product": alpha_product,
                "captured": captured,
                "log_captured": math.log(captured),
                "sum_log_alpha": sum(math.log(abs(alpha)) for alpha in alphas),
            }
        )

    scale_rows = []
    for b_value, alpha in [(10**12, 23 * 29), (10**30, 23 * 29 * 31), (10**60, 23**2 * 29)]:
        captured = math.gcd(u_value, radical(alpha))
        assert captured <= abs(alpha)
        log_b = math.log(b_value)
        log_captured = math.log(captured)
        log_alpha = math.log(abs(alpha))
        assert log_captured <= log_alpha + 1e-12
        scale_rows.append(
            {
                "b": str(b_value),
                "alpha": alpha,
                "captured": captured,
                "log_captured_over_log_b": log_captured / log_b,
                "log_alpha_over_log_b": log_alpha / log_b,
            }
        )
    return {
        "U_declared": u_value,
        "portfolio_rows": portfolio_rows,
        "portfolio_rows_digest": digest(portfolio_rows),
        "scale_rows": scale_rows,
        "scale_rows_digest": digest(scale_rows),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    normalization = normalization_controls()
    saturation = actual_saturation_controls()
    valuations = valuation_controls()
    representation = representation_and_integrality_controls()
    portfolio = portfolio_and_height_controls()
    core = {
        "schema": "item375-beta-symmetric-content-primitive-no-go-v1",
        "item": 375,
        "checked_date_beijing": "2026-09-01",
        "classification": "PROVED_SCOPED_CONTENT_PRIMITIVE_PART_NO_GO",
        "dependencies": dependencies,
        "controls": {
            "normalization": normalization,
            "actual_saturation": saturation,
            "valuations": valuations,
            "representation_and_integrality": representation,
            "portfolio_and_height": portfolio,
        },
        "claims": {
            "normal_form": "R=alpha*A1/(beta*B1), with coprime scalar ratio and primitive coprime polynomial pair",
            "constant_primitive_numerator": "A1 constant implies A1=+/-1",
            "singleton_valuation": "for denominator-unit singleton p, v_p(R(P,E))=v_p(alpha)",
            "saturated_content": "C_cont=gcd(U_11,rad(alpha))",
            "capacity": "log C_cont<=log rad|alpha|<=log|alpha|; portfolios use sum log|alpha_l|",
            "primitive_height_warning": "omitting reduced scalar content is not a representation-invariant divisibility height",
            "integral_specialization": "beta*B1(P,E)|alpha; it cannot compress the scalar numerator",
        },
        "declared_symbolic_controls_only": True,
        "actual_prime_or_target_census_performed": False,
        "constructed_actual_sub_beta_scalar": False,
        "strict_labels": {
            "PROVED": [
                "content/primitive normalization",
                "exact singleton scalar valuation",
                "mandatory saturated content carrier",
                "portfolio and height bounds",
                "zero booking",
            ],
            "PROVED_SCOPED_NO_GO": [
                "content-degenerate symmetric rational carriers at sub-beta total scalar height",
                "primitive height with coefficient content omitted",
                "sub-beta aggregate content portfolios",
                "unit variable denominators as content compression",
            ],
            "EXACT_FINITE_ONLY": [
                "predeclared sparse-polynomial, valuation, saturation, portfolio, and height controls"
            ],
            "OPEN": [
                "nonconstant multivariate symmetric one-point cancellation",
                "beta-height gcd/radical compression",
                "new actual sub-beta scalar divisibility theorem",
                "U_11 weighted bound and Route 1",
            ],
        },
        "capacity_booking": {
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "new_booking": 0,
        },
    }
    core["certificate_digest"] = digest(core)
    return core


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item375_beta_symmetric_content_primitive_no_go_certificate.json",
    )
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "sha256": hashlib.sha256(output.read_bytes()).hexdigest(), "digest": payload["certificate_digest"]}, sort_keys=True))


if __name__ == "__main__":
    main()
