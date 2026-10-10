#!/usr/bin/env python3
"""Deterministic exact replay for Item 378.

Checks predeclared top-elementary complement identities, adjacent scale bounds,
reciprocal-positive transforms, Schur gaps, transversality controls, and the
ambient cancellation variety.  No actual target or prime census is run.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
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
    "sources/item375_beta_symmetric_content_primitive_no_go_report.md": (
        "4acda264afe6fa40431d041fbbbc3634eeb0ec1395a35b682611764f5c92fb12"
    ),
    "scripts/item375_beta_symmetric_content_primitive_no_go_certificate.py": (
        "ab42775d9d854c1b62fe25e5aa929b00f7c8f07b1c04331a56b111c5b3d996b9"
    ),
    "results/item375_beta_symmetric_content_primitive_no_go_certificate.json": (
        "e96a358a761bf3f83ae791ebcc83756feb17725fd68ba58d611b00800f3ff6d3"
    ),
    "results/item375_beta_symmetric_content_primitive_no_go_ledger_delta.json": (
        "d0cc6de271dcf31adb0ec605d824410f0320b89a9ddcfd4f722a22d3d19adbf5"
    ),
    "results/item375_beta_symmetric_content_primitive_no_go_root_audit.json": (
        "8e0a605818fd7779552c9c196fb00584c9a8d58937d6b40063f9e6b6cad7e5d9"
    ),
    "manifests/item375_beta_symmetric_content_primitive_no_go_manifest.json": (
        "79db075b1c5cab090fa942c8bacb4dd0e7ea80eace9cc26c7f4e4cf91ce42621"
    ),
}


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]


def digest(value: Any) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


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


def elementary(values: list[Any], degree: int) -> Any:
    assert 0 <= degree <= len(values)
    if degree == 0:
        return 1
    return sum(
        (math.prod(values[index] for index in subset) for subset in itertools.combinations(range(len(values)), degree)),
        start=0,
    )


def clean(poly: Polynomial) -> Polynomial:
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + coefficient
    return clean(result)


def scale(poly: Polynomial, scalar: int) -> Polynomial:
    return clean({exponent: scalar * coefficient for exponent, coefficient in poly.items()})


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    assert left and right
    width = len(next(iter(left)))
    assert all(len(exponent) == width for exponent in right)
    result: Polynomial = {}
    for le, lc in left.items():
        for re, rc in right.items():
            exponent = tuple(a + b for a, b in zip(le, re))
            result[exponent] = result.get(exponent, 0) + lc * rc
    return clean(result)


def power(poly: Polynomial, exponent: int) -> Polynomial:
    assert exponent >= 0 and poly
    width = len(next(iter(poly)))
    result: Polynomial = {(0,) * width: 1}
    base = poly
    value = exponent
    while value:
        if value & 1:
            result = multiply(result, base)
        value >>= 1
        if value:
            base = multiply(base, base)
    return result


def evaluate(poly: Polynomial, values: list[Any]) -> Any:
    return sum(
        coefficient * math.prod(value**exponent for value, exponent in zip(values, powers))
        for powers, coefficient in poly.items()
    )


def elementary_polynomial(variable_count: int, degree: int) -> Polynomial:
    if degree == 0:
        return {(0,) * variable_count: 1}
    result: Polynomial = {}
    for subset in itertools.combinations(range(variable_count), degree):
        exponent = tuple(int(index in subset) for index in range(variable_count))
        result[exponent] = 1
    return result


def compose_in_elementaries(form: Polynomial, variable_count: int) -> Polynomial:
    coordinate_count = len(next(iter(form)))
    elementary_polys = [
        elementary_polynomial(variable_count, degree)
        for degree in range(1, coordinate_count + 1)
    ]
    result: Polynomial = {}
    for coordinate_exponents, coefficient in form.items():
        term: Polynomial = {(0,) * variable_count: coefficient}
        for base, exponent in zip(elementary_polys, coordinate_exponents):
            term = multiply(term, power(base, exponent))
        result = add(result, term)
    return clean(result)


def top_coordinates(loads: list[int], k_value: int) -> list[int]:
    count = len(loads)
    return [elementary(loads, count - degree) for degree in range(1, k_value + 1)]


def complement_and_scale_controls() -> dict[str, Any]:
    capital_A = 20
    loads = [2 * 23, 3 * 29, 7 * 31, 2 * 37, 5, 11]
    assert all(0 < load < capital_A**2 for load in loads)
    declared_primes = [23, 29, 31, 37]
    for prime in declared_primes:
        assert sum(load % prime == 0 for load in loads) == 1
    high_rows = sum(load > capital_A for load in loads)
    assert high_rows >= len(declared_primes)
    count = len(loads)
    product = math.prod(loads)
    reciprocals = [Fraction(1, load) for load in loads]
    coordinates = top_coordinates(loads, 3)
    complement_rows = []
    for degree, coordinate in enumerate(coordinates, start=1):
        complement = product * elementary(reciprocals, degree)
        assert complement.denominator == 1
        assert complement.numerator == coordinate
        complement_rows.append(
            {
                "s": degree,
                "T_s": coordinate,
                "P_times_e_s_reciprocal": complement.numerator,
            }
        )
    adjacent_rows = []
    for s_value in [1, 2]:
        ratio = Fraction(coordinates[s_value], coordinates[s_value - 1])
        lower = Fraction(count - s_value, (s_value + 1) * capital_A**2)
        upper = Fraction(count - s_value, s_value + 1)
        assert lower <= ratio <= upper
        adjacent_rows.append(
            {
                "s": s_value,
                "ratio": str(ratio),
                "lower": str(lower),
                "upper": str(upper),
            }
        )
    M = coordinates[0]
    assert M > capital_A ** (high_rows - 1)
    coarse_R = (count * capital_A**2) ** 3
    for coordinate in coordinates:
        assert Fraction(1, coarse_R) <= Fraction(coordinate, M) <= coarse_R
    return {
        "capital_A": capital_A,
        "loads": loads,
        "declared_singleton_primes": declared_primes,
        "high_rows": high_rows,
        "P": product,
        "coordinates": coordinates,
        "M_lower": capital_A ** (high_rows - 1),
        "coarse_R": coarse_R,
        "complement_rows": complement_rows,
        "adjacent_rows": adjacent_rows,
        "rows_digest": digest(complement_rows + adjacent_rows),
    }


def reciprocal_positive_controls() -> dict[str, Any]:
    loads = [3, 5, 7, 11, 13]
    count = len(loads)
    k_value = 3
    product = math.prod(loads)
    reciprocals = [Fraction(1, load) for load in loads]
    coordinates = top_coordinates(loads, k_value)
    M = coordinates[0]

    same_sign_form: Polynomial = {
        (2, 0, 0): 1,
        (0, 2, 0): 2,
        (0, 0, 2): 1,
        (1, 1, 0): 3,
    }
    schur_gap_form: Polynomial = {
        (0, 2, 0): 1,
        (1, 0, 1): -1,
    }
    rows = []
    for name, form in [
        ("same_sign_coordinate_form", same_sign_form),
        ("mixed_sign_schur_gap_s2", schur_gap_form),
    ]:
        phi = compose_in_elementaries(form, count)
        signs = {int(coefficient > 0) - int(coefficient < 0) for coefficient in phi.values()}
        assert signs == {1}
        form_value = evaluate(form, coordinates)
        phi_value = evaluate(phi, reciprocals)
        assert Fraction(form_value, product**2) == phi_value
        assert form_value > 0
        degree = 2
        lower_ratio = Fraction(1, 20 ** (2 * k_value * degree) * count**degree)
        actual_ratio = Fraction(form_value, M**degree)
        assert actual_ratio >= lower_ratio
        rows.append(
            {
                "name": name,
                "coordinate_form_value": form_value,
                "reciprocal_terms": len(phi),
                "reciprocal_coefficients_one_sign": True,
                "actual_ratio": str(actual_ratio),
                "declared_lower_ratio": str(lower_ratio),
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def transversality_controls() -> dict[str, Any]:
    loads = [46, 87, 217, 74, 5, 11]
    coordinates = top_coordinates(loads, 3)
    M = coordinates[0]
    leading: Polynomial = {(0, 2, 0): 1, (1, 0, 1): -1}
    lower: Polynomial = {(1, 0, 0): -3, (0, 0, 0): 2}
    full = add(leading, lower)
    leading_value = evaluate(leading, coordinates)
    lower_value = evaluate(lower, coordinates)
    full_value = evaluate(full, coordinates)
    assert leading_value > 0
    assert full_value == leading_value + lower_value
    assert abs(lower_value) * 2 < leading_value
    assert abs(full_value) * 2 >= leading_value
    K_value = Fraction(M**2, leading_value)
    return {
        "coordinates": coordinates,
        "M": M,
        "leading_value": leading_value,
        "lower_value": lower_value,
        "full_value": full_value,
        "M_squared_over_leading": str(K_value),
        "leading_dominates_lower_by_factor_two": True,
    }


def cancellation_variety_controls() -> dict[str, Any]:
    rows = []
    for count in [3, 5, 7, 9]:
        loads = [1] * count
        coordinates = top_coordinates(loads, 2)
        T1, T2 = coordinates
        leading_value = 2 * T2 - (count - 1) * T1
        full_value = leading_value + 1
        assert leading_value == 0
        assert full_value == 1
        form: Polynomial = {(0, 1): 2, (1, 0): -(count - 1)}
        phi = compose_in_elementaries(form, count)
        signs = {int(coefficient > 0) - int(coefficient < 0) for coefficient in phi.values()}
        assert signs == {-1, 1}
        assert evaluate(phi, [Fraction(1, 1)] * count) == 0
        rows.append(
            {
                "N": count,
                "T1": T1,
                "T2": T2,
                "leading_mixed_sign_value": leading_value,
                "primitive_full_value": full_value,
                "coefficient_height": count - 1,
                "actual_singleton_mass_claimed": False,
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def scale_box_controls() -> dict[str, Any]:
    rows = []
    for M, R, coefficient_bound, K_value, degree, monomial_count in [
        (10**12, 10**2, 10**2, 10**2, 2, 10),
        (10**30, 10**4, 10**3, 10**3, 3, 20),
        (10**60, 10**6, 10**4, 10**4, 4, 35),
    ]:
        lower_ratio = Fraction(monomial_count * coefficient_bound * K_value * R ** (degree - 1), M)
        assert lower_ratio < Fraction(1, 2)
        leading_lower = Fraction(M**degree, K_value)
        lower_degree_upper = monomial_count * coefficient_bound * (R * M) ** (degree - 1)
        assert lower_degree_upper * 2 < leading_lower
        rows.append(
            {
                "M": str(M),
                "R": R,
                "B": coefficient_bound,
                "K": K_value,
                "degree": degree,
                "monomial_count": monomial_count,
                "dominance_ratio": str(lower_ratio),
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    complement = complement_and_scale_controls()
    reciprocal_positive = reciprocal_positive_controls()
    transversality = transversality_controls()
    cancellation = cancellation_variety_controls()
    scale_boxes = scale_box_controls()
    core = {
        "schema": "item378-beta-top-symmetric-multivariate-cancellation-v1",
        "item": 378,
        "checked_date_beijing": "2026-09-01",
        "classification": "PROVED_RECIPROCAL_POSITIVE_NO_GO_AND_CANCELLATION_TUBE",
        "dependencies": dependencies,
        "controls": {
            "complement_and_scale": complement,
            "reciprocal_positive": reciprocal_positive,
            "transversality": transversality,
            "cancellation_variety": cancellation,
            "scale_boxes": scale_boxes,
        },
        "claims": {
            "common_scale": "positive singleton mass forces M=T1 beta-scale and all fixed T_s/M=b^o",
            "transversality": "a leading homogeneous value at least M^d/b^o dominates all bounded-degree lower layers",
            "reciprocal_transform": "H(T)=P^d H(e1(1/Z),...,ek(1/Z))",
            "one_sign_cone": "one-sign reciprocal monomial coefficients imply |H(T)|/M^d>=A^(-2kd)N^(-d)",
            "schur_gap": "X_s^2-X_(s-1)X_(s+1) lies in the reciprocal-positive cone",
            "cancellation_tube": "a sub-beta value requires normalized leading reciprocal form value <=b^(-eta/2+o(1))",
        },
        "declared_symbolic_controls_only": True,
        "actual_prime_or_target_census_performed": False,
        "constructed_actual_sub_beta_carrier": False,
        "strict_labels": {
            "PROVED": [
                "actual common-scale theorem",
                "primitive multivariate transversality",
                "reciprocal-positive criterion",
                "mixed-sign Schur gap corollary",
                "necessary cancellation tube",
                "zero booking",
            ],
            "PROVED_SCOPED_NO_GO": [
                "reciprocal-positive bounded-degree residuals on positive singleton mass",
                "same-sign leading forms and Schur gaps",
                "sub-beta denominators and content normalization as escapes",
            ],
            "EXACT_FINITE_ONLY": [
                "predeclared positive loads, transforms, Schur gaps, scale boxes, and ambient all-one cancellation"
            ],
            "OPEN": [
                "actual avoidance of mixed-sign cancellation tube",
                "canonical sub-beta mixed-sign divisibility carrier",
                "growing degree or k and beta-height nonlinear compression",
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
        default="work/item378_beta_top_symmetric_multivariate_cancellation_certificate.json",
    )
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(output),
                "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                "digest": payload["certificate_digest"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
