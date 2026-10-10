#!/usr/bin/env python3
"""Exact certificate for Item 307's structural-ray fixed divisors.

The logical Frobenius and coefficient-substitution proof is in the companion
report.  This checker performs the exact rational-function/partial-fraction
calculation, verifies the six residue forms and fixed divisors, and replays a
fixed list of control rows.  It performs no prime scan and no factorization of
the fixed containers.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = ROOT / "results" / "item307_j1_structural_ray_fixed_divisor_certificate.json"
Q = Fraction

DEPENDENCIES = {
    "scripts/item222_j1_phase_resultant_certificate.py": "c16f75156ba8424c567163cedc6a93a7656c8a53036b48ef69b06327d76ad44b",
    "scripts/item229_j1_fixed_h_theta_certificate.py": "a8e2028ca6a53f8c843c25be375feac50e4704538686ee1e3a835f89aa11780f",
    "scripts/item237_j1_algebraic_residual_certificate.py": "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf",
    "results/item237_j1_algebraic_residual_certificate.json": "eba1519f4d376d442f396048528190b474cc5464bbe42c3bdf31a9bdaf39dd6b",
    "sources/item237_j1_algebraic_residual_report.md": "dd1278d5ec6e3960d5539f3b349f2245449d4801663beb7915140d722a62c569",
    "scripts/item243_order6_gauge_closure_certificate.py": "d619e0809aaa89b5d11cbe30a92a3e7f8cf14237f45dd066aedf84e017bbfdd8",
    "results/item243_order6_gauge_closure_certificate.json": "0ec0052ea270a84828cb1934373ad05e8e5b00cbf72e0d970ff805e716078546",
    "sources/item264_j1_weighted_gate_report.md": "767005f8fad07b1fa633bfdd23436e36c7cdef346d032030390c437f207c9344",
    "scripts/item264_j1_weighted_gate_certificate.py": "a91d0905ecd73ba8406902a5c33ff5f6c21c5b67fce65a91b087ec6cf79bf733",
    "results/item264_j1_weighted_gate_certificate.json": "08010c633f3baf5e075e892c5c786a5d9f686bf26d940fb10da6b9f46de196d2",
    "scripts/item288_j1_large_prime_redundancy_certificate.py": "89c9ffcb5496bfd208cfe55a2fceb2d37060c07493d01f17013d9e8c4303b189",
    "results/item288_j1_large_prime_redundancy_certificate.json": "fde756a5dff3b482bb38e342c4d26871dec90c32a7868110ba4f3186ba70b738",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def trim(poly: list[Q]) -> list[Q]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[Q], right: list[Q]) -> list[Q]:
    out = [Q(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: list[Q], scalar: Q | int) -> list[Q]:
    return trim([Q(scalar) * value for value in poly])


def multiply(left: list[Q], right: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for j, x_value in enumerate(left):
        for k, y_value in enumerate(right):
            out[j + k] += x_value * y_value
    return trim(out)


def power(poly: list[Q], exponent: int) -> list[Q]:
    out = [Q(1)]
    base = poly[:]
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        exponent //= 2
    return out


def derivative(poly: list[Q]) -> list[Q]:
    return [Q(index) * poly[index] for index in range(1, len(poly))] or [Q(0)]


def shift(poly: list[Q], amount: int = 1) -> list[Q]:
    return [Q(0)] * amount + poly


def rational_source(s_value: int) -> tuple[list[Q], list[Q], int, int]:
    one_minus_t = [Q(1), Q(-1)]
    d_poly = [Q(2), Q(-2), Q(1)]
    d_prime = derivative(d_poly)
    r_one = [Q(10, 3), Q(-13, 3), Q(5, 3)]
    r_zero = [Q(2), Q(-9), Q(4)]
    a_exponent = 2 * s_value + 5
    b_exponent = 2 * s_value

    # Numerator of t(R1/H)' + R0/H over
    # (1-t)^(a+1)D^(b+1), H=(1-t)^a D^b.
    first = multiply(
        add(shift(derivative(r_one)), r_zero), multiply(one_minus_t, d_poly)
    )
    second = scale(multiply(shift(r_one), d_poly), a_exponent)
    third = scale(
        multiply(multiply(shift(r_one), d_prime), one_minus_t), -b_exponent
    )
    numerator = add(add(first, second), third)
    denominator = multiply(
        power(one_minus_t, a_exponent + 1), power(d_poly, b_exponent + 1)
    )

    expected_numerator = [
        Q(4),
        Q(80 * s_value - 4, 3),
        Q(-224 * s_value - 8, 3),
        Q(256 * s_value + 16, 3),
        Q(-138 * s_value - 9, 3),
        Q(30 * s_value + 3, 3),
    ]
    if numerator != expected_numerator:
        raise AssertionError(("N_s", s_value, numerator))
    return numerator, denominator, a_exponent + 1, b_exponent + 1


def series_coefficients(numerator: list[Q], denominator: list[Q], count: int) -> list[Q]:
    answer: list[Q] = []
    for index in range(count):
        value = numerator[index] if index < len(numerator) else Q(0)
        for shift_index in range(1, min(index, len(denominator) - 1) + 1):
            value -= denominator[shift_index] * answer[index - shift_index]
        answer.append(value / denominator[0])
    return answer


def solve_exact(matrix: list[list[Q]], rhs: list[Q]) -> list[Q]:
    augmented = [row[:] + [value] for row, value in zip(matrix, rhs)]
    size = len(augmented)
    if any(len(row) != size + 1 for row in augmented):
        raise ValueError("matrix must be square")
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]), None
        )
        if pivot is None:
            raise ArithmeticError(("singular", column))
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(size):
            if row == column or augmented[row][column] == 0:
                continue
            quotient = augmented[row][column]
            augmented[row] = [
                value - quotient * pivot_entry
                for value, pivot_entry in zip(augmented[row], augmented[column])
            ]
    return [augmented[index][-1] for index in range(size)]


def lambda_powers(count: int) -> list[tuple[Q, Q]]:
    # lambda=(1+i)/2.
    answer = []
    real, imag = Q(1), Q(0)
    for _ in range(count):
        answer.append((real, imag))
        real, imag = (real - imag) / 2, (real + imag) / 2
    return answer


def generalized_binomial(top: Q, lower: int) -> Q:
    answer = Q(1)
    for index in range(1, lower + 1):
        answer *= (top - index + 1) / index
    return answer


def basis_row(index: int, one_order: int, gaussian_order: int, power_row: tuple[Q, Q]) -> list[Q]:
    row: list[Q] = []
    for order in range(1, one_order + 1):
        row.append(Q(math.comb(index + order - 1, order - 1)))
    real, imag = power_row
    for order in range(1, gaussian_order + 1):
        binomial = Q(math.comb(index + order - 1, order - 1))
        # 2 Re((u+iv)lambda^n) = 2u Re(lambda^n)-2v Im(lambda^n).
        row.extend((2 * binomial * real, -2 * binomial * imag))
    return row


EXPECTED_AGGREGATES = {
    2: (Q(6517, 8), Q(-55363, 2048), Q(28357, 2048)),
    4: (
        Q(-160741235, 1024),
        Q(-2209797565, 16777216),
        Q(-12326545165, 16777216),
    ),
    6: (
        Q(6164597613027, 262144),
        Q(4266522023635179, 274877906944),
        Q(492022610178771, 274877906944),
    ),
}


def partial_fraction_certificate(s_value: int) -> dict[str, Any]:
    numerator, denominator, one_order, gaussian_order = rational_source(s_value)
    denominator_degree = len(denominator) - 1
    coordinate_count = one_order + 2 * gaussian_order
    if coordinate_count != denominator_degree:
        raise AssertionError(("dimension", s_value, coordinate_count, denominator_degree))

    sequence = series_coefficients(numerator, denominator, coordinate_count + 8)
    powers = lambda_powers(coordinate_count + 8)
    matrix = [
        basis_row(index, one_order, gaussian_order, powers[index])
        for index in range(coordinate_count)
    ]
    solution = solve_exact(matrix, sequence[:coordinate_count])

    # The first denominator_degree coefficients are the exact proper-rational
    # certificate.  Extra rows are independent replay checks.
    for index in range(coordinate_count, coordinate_count + 8):
        reconstructed = sum(
            left * right
            for left, right in zip(
                basis_row(index, one_order, gaussian_order, powers[index]), solution
            )
        )
        if reconstructed != sequence[index]:
            raise AssertionError(("partial fraction replay", s_value, index))

    n_special = Q(-(6 * s_value + 3), 2)
    a_value = Q(0)
    for order in range(1, one_order + 1):
        a_value += solution[order - 1] * generalized_binomial(
            n_special + order - 1, order - 1
        )
    u_value = Q(0)
    v_value = Q(0)
    offset = one_order
    for order in range(1, gaussian_order + 1):
        binomial = generalized_binomial(n_special + order - 1, order - 1)
        u_value += solution[offset + 2 * (order - 1)] * binomial
        v_value += solution[offset + 2 * (order - 1) + 1] * binomial
    aggregate = (a_value, u_value, v_value)
    if aggregate != EXPECTED_AGGREGATES[s_value]:
        raise AssertionError(("aggregate", s_value, aggregate))

    return {
        "s": s_value,
        "N_s_low_to_high": [encode_fraction(value) for value in numerator],
        "denominator_degree": denominator_degree,
        "one_pole_order": one_order,
        "each_gaussian_pole_order": gaussian_order,
        "partial_fraction_A_at_one_by_increasing_pole_order": [
            encode_fraction(value) for value in solution[:one_order]
        ],
        "partial_fraction_B_at_lambda_real_imag_by_increasing_pole_order": [
            [
                encode_fraction(solution[offset + 2 * (order - 1)]),
                encode_fraction(solution[offset + 2 * (order - 1) + 1]),
            ]
            for order in range(1, gaussian_order + 1)
        ],
        "n_special": encode_fraction(n_special),
        "A_of_n_special": encode_fraction(a_value),
        "B_of_n_special_real": encode_fraction(u_value),
        "B_of_n_special_imag": encode_fraction(v_value),
        "exactness": (
            "The proper rational difference has denominator degree 6s+8; "
            "its first 6s+8 Taylor coefficients vanish exactly."
        ),
        "extra_exact_replay_coefficients": 8,
    }


CLOSED_ROWS = [
    {"s": 2, "parity": 0, "a": 6517, "b": -55363, "gamma": Q(2)},
    {"s": 2, "parity": 1, "a": 6517, "b": 28357, "gamma": Q(2)},
    {"s": 4, "parity": 0, "a": -160741235, "b": 2209797565, "gamma": Q(1, 4)},
    {"s": 4, "parity": 1, "a": -160741235, "b": 12326545165, "gamma": Q(1, 4)},
    {"s": 6, "parity": 0, "a": 6164597613027, "b": 4266522023635179, "gamma": Q(1, 64)},
    {"s": 6, "parity": 1, "a": 6164597613027, "b": 492022610178771, "gamma": Q(1, 64)},
]

EXPECTED_DIVISORS = {
    (2, 0): 2371263223,
    (2, 1): 6240444441,
    (4, 0): 216546009281712172425,
    (4, 1): 59719088298647365975,
    (6, 0): 1720920668592381569095693219911,
    (6, 1): 20166217095683535330649958652393,
}


def residue_and_divisor_rows() -> list[dict[str, Any]]:
    answer = []
    for row in CLOSED_ROWS:
        s_value = row["s"]
        parity = row["parity"]
        aggregate_a, aggregate_u, aggregate_v = EXPECTED_AGGREGATES[s_value]
        delta = (-1) ** (parity + s_value // 2 + 1)
        if parity == 0:
            gaussian_w_coefficient = 2 * aggregate_u * delta * 2 ** (3 * s_value + 1)
        else:
            gaussian_w_coefficient = -2 * aggregate_v * delta * 2 ** (3 * s_value + 1)
        if Q(2 ** (2 * s_value)) * aggregate_a != row["gamma"] * row["a"]:
            raise AssertionError(("a scaling", row))
        if Q(2 ** (2 * s_value)) * gaussian_w_coefficient != row["gamma"] * row["b"]:
            raise AssertionError(("b scaling", row))

        divisor = 2 ** (3 * s_value + 1) * row["a"] ** 2 - delta * row["b"] ** 2
        if divisor != EXPECTED_DIVISORS[(s_value, parity)] or divisor <= 0:
            raise AssertionError(("fixed divisor", row, divisor))
        answer.append(
            {
                "s": s_value,
                "h_parity": parity,
                "delta_equals_Legendre_2": delta,
                "a": row["a"],
                "b": row["b"],
                "gamma": encode_fraction(row["gamma"]),
                "closed_residue": "c_h^* = gamma*(a+b*w_h) mod p",
                "w_h": "(-1)^floor(h/2)*2^h",
                "w_square": f"2^({3*s_value+1})*w_h^2 = {delta} mod p",
                "necessary_fixed_divisor": divisor,
            }
        )
    return answer


def euler_case_rows() -> list[dict[str, int]]:
    answer = []
    for s_value in (2, 4, 6):
        for parity in (0, 1):
            p_mod_8 = (4 * parity + 6 * s_value + 3) % 8
            legendre_two = 1 if p_mod_8 in (1, 7) else -1
            delta = (-1) ** (parity + s_value // 2 + 1)
            if p_mod_8 not in (3, 7) or legendre_two != delta:
                raise AssertionError(("Euler case", s_value, parity))
            answer.append(
                {
                    "s": s_value,
                    "h_parity": parity,
                    "p_mod_8": p_mod_8,
                    "Legendre_symbol_2_over_p": legendre_two,
                    "delta": delta,
                }
            )
    return answer


def encode_fraction(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fraction_mod(value: Q, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def gauge_value(item229: Any, h_value: int) -> Q:
    if h_value % 3 == 1:
        index = 1
        value = Q(-49, 18)
    elif h_value % 3 == 2:
        index = 2
        value = Q(4235, 1944)
    else:
        raise ValueError(h_value)
    while index < h_value:
        value *= item229.rho(index)
        index += 3
    return value


CONTROL_ROWS = [
    (2, 1, 19),
    (2, 2, 23),
    (2, 8, 47),
    (4, 1, 31),
    (4, 4, 43),
    (6, 1, 43),
    (6, 7, 67),
    (6, 10, 79),
]


def exact_controls(item222: Any, item229: Any) -> list[dict[str, Any]]:
    by_case = {(row["s"], row["parity"]): row for row in CLOSED_ROWS}
    answer = []
    for s_value, h_value, prime in CONTROL_ROWS:
        if prime != 4 * h_value + 6 * s_value + 3 or not is_prime(prime):
            raise AssertionError(("control row", s_value, h_value, prime))
        c_value = item229.phase_c(h_value)
        e_value = item222.phase_fraction_and_integer(h_value)[0]
        gauge = gauge_value(item229, h_value)
        if c_value != gauge * e_value:
            raise AssertionError(("gauge replay", s_value, h_value))
        row = by_case[(s_value, h_value % 2)]
        w_mod = ((-1) ** (h_value // 2) * pow(2, h_value, prime)) % prime
        closed_mod = fraction_mod(row["gamma"], prime) * (
            row["a"] + row["b"] * w_mod
        ) % prime
        c_mod = fraction_mod(c_value, prime)
        e_mod = fraction_mod(e_value, prime)
        gauge_mod = fraction_mod(gauge, prime)
        if c_mod != closed_mod or not gauge_mod or c_mod != gauge_mod * e_mod % prime:
            raise AssertionError(("closed control", s_value, h_value, prime))
        answer.append(
            {
                "s": s_value,
                "h": h_value,
                "p": prime,
                "w_mod_p": w_mod,
                "c_mod_p": c_mod,
                "E_mod_p": e_mod,
                "gauge_mod_p": gauge_mod,
                "fixed_preselected_control_not_scan": True,
            }
        )
    return answer


def upstream_admission() -> dict[str, str]:
    item237 = json.loads(
        (ROOT / "results/item237_j1_algebraic_residual_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    if "the fixed algebraic coefficient formula c_h^*=[x^(2h)]C(x)" not in item237["status_ledger"]["PROVED"]:
        raise AssertionError("Item237 coefficient theorem")
    item243 = json.loads(
        (ROOT / "results/item243_order6_gauge_closure_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    all_h_gauge = item243.get("theorems", {}).get("all_h_gauge", "")
    if "for all h>=1" not in all_h_gauge:
        raise AssertionError("Item243 all-h gauge")
    item288 = json.loads(
        (ROOT / "results/item288_j1_large_prime_redundancy_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    gauge_unit = item288.get("theorem", {}).get("gauge", "")
    if "unit in that localization" not in gauge_unit:
        raise AssertionError("Item288 gauge unit")
    item264 = json.loads(
        (ROOT / "results/item264_j1_weighted_gate_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    if item264.get("theorem", {}).get("global_relation") != "4M+1=3p-2s; M=3h+4s+2":
        raise AssertionError("Item264 fixed-M relation")
    if item264.get("booking", {}).get("retained_ceiling_per_6M") != "1/36":
        raise AssertionError("Item264 retained ceiling")
    return {
        "Item237_coefficient_formula": "PROVED and pinned",
        "Item243_all_h_gauge": all_h_gauge,
        "Item264_fixed_M_normalization": "PROVED and pinned; retained ceiling 1/36 per 6M",
        "Item288_actual_row_gauge_unit": gauge_unit,
    }


def build_result() -> dict[str, Any]:
    pin_dependencies()
    item222 = load("item307_item222", "scripts/item222_j1_phase_resultant_certificate.py")
    item229 = load("item307_item229", "scripts/item229_j1_fixed_h_theta_certificate.py")

    partial_rows = [partial_fraction_certificate(s_value) for s_value in (2, 4, 6)]
    divisor_rows = residue_and_divisor_rows()
    controls = exact_controls(item222, item229)
    product = math.prod(EXPECTED_DIVISORS.values())

    return {
        "schema": "item307-j1-structural-ray-fixed-divisor-v1",
        "item": 307,
        "title": "fixed Gaussian divisors for the pinned j=1 orbit on s=2,4,6",
        "dependencies": DEPENDENCIES,
        "upstream_admission": upstream_admission(),
        "formal_reduction": {
            "Item237_start": "c_h^*=[y^(2h)](1+y)^(-2h-1)Q(y)^((4h+3)/3)(hA(y)+B(y))",
            "ray_phase": "p=4h+6s+3, s in {2,4,6}; Q^(p/3)=Q(y^p)^(1/3) below p",
            "fixed_source": "c_h^*=2^(2s)*[t^(2h)]G_s(t) mod p",
            "G_s": "N_s/((1-t)^(2s+6)*(t^2-2t+2)^(2s+1))",
            "three_exact_partial_fraction_rows": partial_rows,
            "classification": "EXACT_RATIONAL_FUNCTION_CERTIFICATE",
        },
        "actual_pinned_gate_bridge": {
            "ordinary_phase": "sigma_*=-(4h+3)/6 and 6(s-sigma_*)=p on p=4h+6s+3",
            "Item222_implication": "ordinary fixed-j=1 collision implies E_h(s)=E_h^*=0 mod p; no converse is claimed",
            "all_h_gauge": "c_h^*=G_h E_h^*",
            "gauge_unit_audit": (
                "For every gauge step a<=h-3, each nonzero linear factor is <=4h+3; "
                "the bases and 864 have prime support <=11; structural p>=4h+15."
            ),
            "conclusion": "G_h is a p-unit and E_h^*=0 iff c_h^*=0 on every admissible structural-ray prime",
            "classification": "PROVED FROM PINNED ITEMS 222,243,288",
        },
        "Euler_sign_cases": euler_case_rows(),
        "closed_residue_and_divisor_rows": divisor_rows,
        "weighted_zero_density": {
            "theorem": (
                "Every actual pinned collision on s=2,4,6 divides its fixed nonzero D_(s,h mod 2)."
            ),
            "bound": "W_str(H) <= sum_(s,epsilon) log rad(|D_s_epsilon|) <= log(product |D_s_epsilon|)",
            "fixed_container_product": product,
            "asymptotic": "O(1)=o(H)",
            "ray_multiplicity_is_retained": True,
            "exact_capacity_consequence": (
                "ZERO master-capacity reduction: at fixed M the three rays contain "
                "at most three candidates and have O(log M)=o(M) raw support already."
            ),
        },
        "coverage_and_smallest_remaining_lemma": {
            "structural_rays": (
                "s=2,4,6 exhaust the infinite coefficient-singular rays of the Item293 recurrence"
            ),
            "fixed_j1_cell": "contains every s>=1, so the three rays do not exhaust it",
            "off_ray_support": "s>=1 with s not in {2,4,6}",
            "fixed_M_reindexing": (
                "S_M={s>=1:4s<=M-5, s=M+1 mod 3}; "
                "p_s=(4M+2s+1)/3; h_s=(M-4s-2)/3"
            ),
            "smallest_remaining_weighted_lemma": (
                "W_off(M)=sum_(s in S_M minus {2,4,6}, p_s prime, "
                "p_s divides N_E(h_s)) log p_s = o(M)"
            ),
            "structural_ray_lemma_remaining": "NONE",
            "actual_1_over_36_target": "off-ray s varying through a set of length asymptotic to M",
        },
        "fixed_control_replay": {
            "classification": "PRESELECTED_EXACT_CONTROLS_NOT_A_PRIME_SCAN",
            "rows": controls,
        },
        "strict_labels": {
            "pinned_structural_ray_residue_formula": "PROVED",
            "fixed_divisor_implication": "PROVED",
            "structural_ray_weighted_collision_mass_O_1": "PROVED",
            "universal_nonvanishing": "NOT CLAIMED",
            "explicit_actual_zero_witness": "(h,s,p)=(8,2,47), E_h^*=0 mod p; PRESELECTED EXACT CONTROL",
            "factorization_or_complete_zero_classification": "NOT CLAIMED",
            "actual_prime_scan": "NONE",
            "off_ray_or_full_fixed_j1_weighted_density": "OPEN",
            "capacity_booking": "ZERO MASTER-CAPACITY REDUCTION; FIXED-M SUPPORT IS THIN",
            "Route_1_and_any_conclusion_about_e_plus_pi": "OPEN",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "fixed_divisors": len(result["closed_residue_and_divisor_rows"]),
                "partial_fraction_rays": len(
                    result["formal_reduction"]["three_exact_partial_fraction_rows"]
                ),
                "control_rows": len(result["fixed_control_replay"]["rows"]),
                "weighted_mass": result["weighted_zero_density"]["asymptotic"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()


