#!/usr/bin/env python3
"""Deterministic certificate for Item 293's surviving j=1 E-gate analysis.

The checker derives the integral E recurrence from the pinned Item237
recurrence and Item243 gauge by exact polynomial cross multiplication.  It
also verifies primitivity, the positive forward coefficient, the localized
large-prime-part bridge, and the formal comparison sequence used in the
strict holonomy/height information-class no-go.  No prime search is run.
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
DEPENDENCIES = {
    "item222_j1_phase_resultant_certificate.py": "c16f75156ba8424c567163cedc6a93a7656c8a53036b48ef69b06327d76ad44b",
    "item229_j1_fixed_h_theta_certificate.py": "a8e2028ca6a53f8c843c25be375feac50e4704538686ee1e3a835f89aa11780f",
    "item237_j1_algebraic_residual_certificate.py": "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf",
    "item237_j1_algebraic_residual_certificate.json": "eba1519f4d376d442f396048528190b474cc5464bbe42c3bdf31a9bdaf39dd6b",
    "item243_order6_gauge_closure_certificate.py": "d619e0809aaa89b5d11cbe30a92a3e7f8cf14237f45dd066aedf84e017bbfdd8",
    "item243_order6_gauge_closure_certificate.json": "0ec0052ea270a84828cb1934373ad05e8e5b00cbf72e0d970ff805e716078546",
    "item288_j1_large_prime_redundancy_certificate.py": "89c9ffcb5496bfd208cfe55a2fceb2d37060c07493d01f17013d9e8c4303b189",
    "item288_j1_large_prime_redundancy_certificate.json": "fde756a5dff3b482bb38e342c4d26871dec90c32a7868110ba4f3186ba70b738",
}
REPLAY_H_MAX = 8


def resolve(name: str) -> Path:
    candidates = (
        HERE / name,
        HERE.parent / "scripts" / name,
        HERE.parent / "results" / name,
    )
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


for dependency_name, expected_hash in DEPENDENCIES.items():
    dependency_path = resolve(dependency_name)
    if sha256(dependency_path) != expected_hash:
        raise RuntimeError(f"dependency hash mismatch: {dependency_name}")


item222 = load("item293_item222", resolve("item222_j1_phase_resultant_certificate.py"))
item229 = load("item293_item229", resolve("item229_j1_fixed_h_theta_certificate.py"))
item237 = load("item293_item237", resolve("item237_j1_algebraic_residual_certificate.py"))
item243_result = json.loads(
    resolve("item243_order6_gauge_closure_certificate.json").read_text(encoding="utf-8")
)
item288_result = json.loads(
    resolve("item288_j1_large_prime_redundancy_certificate.json").read_text(encoding="utf-8")
)


Polynomial = list[Fraction]


def trim(polynomial: Polynomial) -> Polynomial:
    answer = list(polynomial)
    while len(answer) > 1 and not answer[-1]:
        answer.pop()
    return answer or [Fraction(0)]


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    answer = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    return trim(answer)


def scale(polynomial: Polynomial, scalar: Fraction | int) -> Polynomial:
    return trim([value * scalar for value in polynomial])


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return trim(answer)


def power(polynomial: Polynomial, exponent: int) -> Polynomial:
    answer = [Fraction(1)]
    factor = polynomial
    while exponent:
        if exponent & 1:
            answer = multiply(answer, factor)
        exponent >>= 1
        if exponent:
            factor = multiply(factor, factor)
    return answer


def evaluate(polynomial: Polynomial, value: int | Fraction) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(polynomial):
        answer = answer * value + coefficient
    return answer


def divide_with_remainder(
    numerator: Polynomial, denominator: Polynomial
) -> tuple[Polynomial, Polynomial]:
    numerator = trim(numerator)
    denominator = trim(denominator)
    if denominator == [0]:
        raise ZeroDivisionError
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0)] * (len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[shift] = coefficient
        subtraction = [Fraction(0)] * shift + scale(denominator, coefficient)
        remainder = add(remainder, scale(subtraction, -1))
    return trim(quotient), trim(remainder)


def monic_gcd(left: Polynomial, right: Polynomial) -> Polynomial:
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = divide_with_remainder(left, right)
        left, right = right, remainder
    return scale(left, Fraction(1, 1) / left[-1]) if left != [0] else [Fraction(0)]


def linear(constant: int, slope: int = 1) -> Polynomial:
    return [Fraction(constant), Fraction(slope)]


def factored_polynomial(
    scalar: int, factors: list[tuple[int, int, int]], core: list[int]
) -> Polynomial:
    answer: Polynomial = [Fraction(scalar)]
    for constant, slope, exponent in factors:
        answer = multiply(answer, power(linear(constant, slope), exponent))
    answer = multiply(answer, [Fraction(value) for value in core])
    if any(value.denominator != 1 for value in answer):
        raise AssertionError("nonintegral Q polynomial")
    return answer


Q_FACTORS = [
    (
        -4096,
        [
            (1, 1, 1), (3, 1, 1), (5, 1, 1), (6, 1, 1),
            (1, 2, 2), (3, 2, 2), (5, 2, 2), (7, 2, 1),
            (9, 2, 2), (11, 2, 1), (13, 2, 1), (17, 2, 1),
            (3, 4, 1),
        ],
        [6414233265, 5112300033, 1603835736, 247582992, 18819760, 564080],
    ),
    (
        -512,
        [
            (0, 1, 1), (6, 1, 1), (7, 2, 1), (9, 2, 2),
            (11, 2, 1), (13, 2, 1), (17, 2, 1),
            (1, 4, 1), (5, 4, 1), (7, 4, 1), (11, 4, 1), (15, 4, 1),
        ],
        [
            402660529612416, 1002494068911927, 1039962332216826,
            596405304955566, 209971952382012, 47325249956016,
            6857541598288, 618060903584, 31525303040, 694946560,
        ],
    ),
    (
        -4,
        [
            (0, 1, 1), (3, 1, 1), (13, 2, 1), (17, 2, 1),
            (1, 4, 1), (5, 4, 1), (7, 4, 1), (11, 4, 1),
            (13, 4, 1), (17, 4, 1), (19, 4, 1), (23, 4, 1),
            (27, 4, 1),
        ],
        [
            1090010738003273316, 2470146696629963712,
            2354075629101513405, 1243406090403290781,
            403775302745693160, 84106392952710132,
            11294493697293648, 946720367971824,
            45093571774720, 932385882560,
        ],
    ),
    (
        27,
        [
            (0, 1, 1), (3, 1, 1), (6, 1, 1), (9, 1, 1),
            (1, 4, 1), (5, 4, 1), (7, 4, 1), (11, 4, 1),
            (13, 4, 1), (17, 4, 1), (19, 4, 1), (23, 4, 1),
            (25, 4, 1), (29, 4, 1), (31, 4, 1), (35, 4, 1),
            (39, 4, 1),
        ],
        [214443126, 369944721, 239554248, 72513072, 10358560, 564080],
    ),
]


def q_polynomials() -> list[Polynomial]:
    answer = [factored_polynomial(*record) for record in Q_FACTORS]
    if [len(polynomial) - 1 for polynomial in answer] != [22, 22, 22, 22]:
        raise AssertionError("Q degree")
    return answer


def rho_pair(shift: int) -> tuple[Polynomial, Polynomial]:
    numerator: Polynomial = [Fraction(1)]
    for constant, slope, exponent in [
        (shift, 1, 1),
        (4 * shift + 1, 4, 1),
        (4 * shift + 5, 4, 1),
        (4 * shift + 7, 4, 1),
        (4 * shift + 9, 4, 1),
        (4 * shift + 11, 4, 1),
        (4 * shift + 15, 4, 2),
    ]:
        numerator = multiply(numerator, power(linear(constant, slope), exponent))
    denominator: Polynomial = [Fraction(864)]
    for constant, slope, exponent in [
        (shift + 1, 1, 1),
        (shift + 2, 1, 1),
        (2 * shift + 1, 2, 2),
        (2 * shift + 3, 2, 1),
        (2 * shift + 5, 2, 2),
        (4 * shift + 3, 4, 1),
    ]:
        denominator = multiply(denominator, power(linear(constant, slope), exponent))
    return numerator, denominator


def gauged_rational_coefficients() -> list[tuple[Polynomial, Polynomial]]:
    answer: list[tuple[Polynomial, Polynomial]] = []
    gauge_numerator: Polynomial = [Fraction(1)]
    gauge_denominator: Polynomial = [Fraction(1)]
    for shift, p_polynomial in enumerate(item237.recurrence_polynomials()):
        if shift:
            numerator, denominator = rho_pair(3 * (shift - 1))
            gauge_numerator = multiply(gauge_numerator, numerator)
            gauge_denominator = multiply(gauge_denominator, denominator)
        answer.append((multiply(p_polynomial, gauge_numerator), gauge_denominator))
    return answer


def derive_integral_recurrence() -> dict[str, Any]:
    q_values = q_polynomials()
    rational = gauged_rational_coefficients()
    base_numerator, base_denominator = rational[0]
    for index in range(1, 4):
        numerator, denominator = rational[index]
        left = multiply(multiply(q_values[index], base_numerator), denominator)
        right = multiply(multiply(q_values[0], numerator), base_denominator)
        if trim(left) != trim(right):
            raise AssertionError((index, "gauge clearing mismatch"))

    contents = []
    for polynomial in q_values:
        polynomial_content = 0
        for coefficient in polynomial:
            polynomial_content = math.gcd(
                polynomial_content, abs(coefficient.numerator)
            )
            if coefficient.denominator != 1:
                raise AssertionError("Q not integral")
        contents.append(polynomial_content)
    content = math.gcd(*contents)
    gcd_polynomial = q_values[0]
    for polynomial in q_values[1:]:
        gcd_polynomial = monic_gcd(gcd_polynomial, polynomial)
    if content != 1 or gcd_polynomial != [Fraction(1)]:
        raise AssertionError((content, gcd_polynomial))

    scalar_signs = [record[0] for record in Q_FACTORS]
    if scalar_signs != [-4096, -512, -4, 27]:
        raise AssertionError(scalar_signs)
    if contents != [4096, 512, 4, 27]:
        raise AssertionError(("individual contents", contents))
    for _, factors, core in Q_FACTORS:
        if any(exponent < 1 or slope <= 0 or constant + slope <= 0
               for constant, slope, exponent in factors):
            raise AssertionError(("factor positivity for h>=1", factors))
        if any(coefficient <= 0 for coefficient in core):
            raise AssertionError(("core positivity", core))
    if (39, 4, 1) not in Q_FACTORS[3][1]:
        raise AssertionError("missing structural s=6 singular factor")
    if 4 * 1 + 6 * 6 + 3 != 43 or 43 % 2 == 0 or 43 % 3 == 0 or 43 % 5 == 0:
        raise AssertionError("genuine actual prime-row witness")

    return {
        "classification": "SYMBOLIC_EXACT_DERIVATION_FROM_PINNED_GAUGE",
        "recurrence": "sum_(k=0)^3 Q_k(h) E_(h+3k)^*=0",
        "degrees": [len(polynomial) - 1 for polynomial in q_values],
        "individual_integer_contents": contents,
        "primitive_integer_content": content,
        "common_polynomial_gcd": "1",
        "scalar_signs": scalar_signs,
        "coefficient_signs": "Q_0,Q_1,Q_2<0 and Q_3>0 for every integer h>=1",
        "forward_coefficient": "Q_3(h)>0 over Q for every integer h>=1",
        "forward_modular_unit": (
            "NOT UNIFORM: Q_3 contains 4h+39, equal to the actual row "
            "prime on the structural subline s=6; (h,s,p)=(1,6,43) is "
            "a genuine admissible prime-row witness"
        ),
        "derivation_check": (
            "Q_k/[p_k*product_(j=0)^(k-1)rho(h+3j)] is independent of k"
        ),
        "factor_records": [
            {
                "scalar": scalar,
                "linear_factors_constant_slope_exponent": [list(factor) for factor in factors],
                "positive_core_low_to_high": core,
            }
            for scalar, factors, core in Q_FACTORS
        ],
    }


def upstream_theorem_admission() -> dict[str, Any]:
    if item243_result.get("classification") != (
        "PROVED_EXACT_ACTUAL_FAMILY_ORDER6_GAUGE_CLOSURE"
    ):
        raise AssertionError("Item243 theorem classification")
    item243_theorems = item243_result.get("theorems", {})
    if item243_theorems.get("all_h_gauge") != (
        "c_h^*=R_h E_h^* for all h>=1 with 3 not dividing h."
    ):
        raise AssertionError("Item243 all-h gauge")
    if "product_(j=0)^(k-1)rho(h+3j)" not in item243_theorems.get(
        "gauged_E_recurrence", ""
    ):
        raise AssertionError("Item243 gauged recurrence")
    item288_theorem = item288_result.get("theorem", {})
    if item288_theorem.get("classification") != "PROVED EXACT ALL-H":
        raise AssertionError("Item288 theorem classification")
    if "unit in that localization" not in item288_theorem.get("gauge", ""):
        raise AssertionError("Item288 gauge localization")
    closed_form = item237.verify_rational_closed_form()
    if closed_form.get("identity") != "C(x(y))=N(y)/D(y)^3":
        raise AssertionError("Item237 algebraic closed form")
    for h_value in range(1, 13):
        numerator, denominator = rho_pair(0)
        if evaluate(numerator, h_value) / evaluate(denominator, h_value) != item229.rho(
            h_value
        ):
            raise AssertionError(("pinned rho mismatch", h_value))
    return {
        "Item243_all_h_gauge": "PROVED and semantically admitted from pinned JSON",
        "Item288_large_prime_gauge_unit": (
            "PROVED and semantically admitted from pinned JSON"
        ),
        "Item237_algebraic_closed_form": (
            "SYMBOLIC_EXACT and recomputed from the pinned module"
        ),
        "rho_formula_consistency": (
            "12 exact consistency values against the pinned Item229 implementation; "
            "the Q derivation uses the displayed symbolic factor formula, not interpolation"
        ),
    }


def sign_theorem() -> dict[str, Any]:
    negative_indices = (1, 4, 7)
    positive_indices = (2, 5, 8)
    negative_values = [item222.phase_fraction_and_integer(index)[0] for index in negative_indices]
    positive_values = [item222.phase_fraction_and_integer(index)[0] for index in positive_indices]
    if not all(value < 0 for value in negative_values):
        raise AssertionError(negative_values)
    if not all(value > 0 for value in positive_values):
        raise AssertionError(positive_values)
    return {
        "classification": "PROVED_BY_SIGN_PROPAGATION",
        "negative_initials_h_1_4_7": [str(value) for value in negative_values],
        "positive_initials_h_2_5_8": [str(value) for value in positive_values],
        "recurrence_signs": "Q_0,Q_1,Q_2<0<Q_3 for h>=1",
        "conclusion": "E_h^*<0 for h=1 mod 3 and E_h^*>0 for h=2 mod 3",
        "large_prime_part_nonzero": True,
    }


def large_prime_part(value: int, bound: int) -> int:
    answer = abs(value)
    for prime in item222.primes_upto(bound):
        while answer and answer % prime == 0:
            answer //= prime
    return answer


def exact_replay() -> dict[str, Any]:
    q_values = q_polynomials()
    rows = []
    for h_value in range(1, REPLAY_H_MAX + 1):
        if h_value % 3 == 0:
            continue
        e_values = [
            item222.phase_fraction_and_integer(h_value + 3 * shift)[0]
            for shift in range(4)
        ]
        recurrence_value = sum(
            evaluate(q_values[shift], h_value) * e_values[shift]
            for shift in range(4)
        )
        if recurrence_value:
            raise AssertionError((h_value, recurrence_value))
        e_value = e_values[0]
        c_value = item229.phase_c(h_value)
        bound = 4 * h_value + 3
        e_large = large_prime_part(e_value.numerator, bound)
        c_large = large_prime_part(c_value.numerator, bound)
        if e_large != c_large:
            raise AssertionError((h_value, e_large, c_large))
        rows.append([h_value, str(e_value), str(c_value), e_large])
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_REPLAY_OF_PROVED_IDENTITIES_NOT_EXTRAPOLATION",
        "h_max": REPLAY_H_MAX,
        "rows": len(rows),
        "checks": [
            "primitive integral Q recurrence",
            "large-prime part of numerator(E) equals that of numerator(c)",
        ],
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def comparison_no_go() -> dict[str, Any]:
    # a_h=4h+9: exact second difference and rational generating function.
    for h_value in range(1, 6):
        values = [4 * (h_value + shift) + 9 for shift in range(3)]
        if values[2] - 2 * values[1] + values[0]:
            raise AssertionError("comparison recurrence")
    # Sum_(h>=1)(4h+9)z^h = z(13-9z)/(1-z)^2.
    denominator = [1, -2, 1]
    coefficients = [0] + [4 * h_value + 9 for h_value in range(1, 8)]
    product = [0] * (len(coefficients) + len(denominator) - 1)
    for i, left in enumerate(coefficients):
        for j, right in enumerate(denominator):
            product[i + j] += left * right
    if product[:8] != [0, 13, -9, 0, 0, 0, 0, 0]:
        raise AssertionError(product[:8])
    return {
        "classification": "RIGOROUS_SCOPED_INFORMATION_CLASS_NO_GO",
        "comparison_sequence": "a_h=4h+9",
        "rational_generating_function": "z*(13-9z)/(1-z)^2",
        "integral_recurrence": "a_(h+2)-2a_(h+1)+a_h=0",
        "height": "log|a_h|=O(log h), stronger than exponential height",
        "actual_row_embedding": (
            "a_h=4h+6*1+3, so every prime value is an actual s=1 row; "
            "if 3 divides h then a_h>3 is divisible by 3, so every prime "
            "value automatically has admissible 3-nondivisible h"
        ),
        "PNT_in_AP_normalization": (
            "sum_(h<=H, 4h+9 prime) log(4h+9)="
            "theta(4H+9;4,1)+O(1)~2H"
        ),
        "scope": (
            "algebraicity/rationality, fixed-order integral holonomy, integrality, "
            "and exponential height alone cannot imply o(H); sequence-specific "
            "congruence, monodromy, or auxiliary-local input is not obstructed"
        ),
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item293-j1-E-gate-density-no-go-v1",
        "item": 293,
        "title": "integral recurrence and holonomy-height no-go for the sole j=1 E gate",
        "dependencies": DEPENDENCIES,
        "upstream_theorem_admission": upstream_theorem_admission(),
        "integral_E_recurrence": derive_integral_recurrence(),
        "rational_sign_theorem": sign_theorem(),
        "large_prime_numerator": {
            "definition": (
                "M_h is the reduced numerator N_E(h) with every prime-power "
                "factor at primes <=4h+3 removed"
            ),
            "exact_bridge": (
                "M_h equals the >4h+3 part of numerator(c_h), because "
                "c_h=G_h E_h and G_h is a unit in the Item288 localization"
            ),
            "algebraic_generating_function": (
                "c_h=[x^(2h)]C(x), C(x(y))=N(y)/D(y)^3, "
                "x=y(1+y)/(1+y+y^2/2)^(2/3)"
            ),
            "classification": "PROVED ALL-H DESCRIPTION",
        },
        "height_consequence": {
            "Eisenstein_and_local_analytic_bound": "log|numerator(c_h)|=O(h)",
            "individual": "log rad(M_h)=O(h)",
            "collective_h_le_H": "sum log rad(M_h)=O(H^2)",
            "target": "o(H)",
            "admission": "the generic height bound is insufficient by two orders",
        },
        "information_class_no_go": comparison_no_go(),
        "exact_replay": exact_replay(),
        "actual_family": {
            "row": "p=4h+6s+3, h,s>=1",
            "sole_gate_after_Item288": "p divides M_h",
            "retained_conditional_capacity_per_m": "1/6",
            "retained_conditional_capacity_per_6m": "1/36",
        },
        "capacity": {
            "new_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_booked": 0,
            "reason": "the exact recurrence and algebraic height do not control the actual-prime zero set",
        },
        "strict_labels": {
            "integral_E_recurrence": "PROVED",
            "large_prime_part_algebraic_coefficient_bridge": "PROVED",
            "holonomy_height_information_class_no_go": "PROVED WITH NARROW SCOPE",
            "sequence_specific_density_bound": "OPEN",
            "weighted_actual_prime_mass_o_H": "OPEN",
            "Route_1": "OPEN",
            "prime_search": "NONE",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = build_result()
    output = arguments.output or (
        HERE / "item293_j1_E_gate_density_no_go_certificate.json"
        if HERE.name == "work"
        else HERE.parent / "results" / "item293_j1_E_gate_density_no_go_certificate.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"output": str(output), "sha256": sha256(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
