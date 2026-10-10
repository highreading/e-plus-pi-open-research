#!/usr/bin/env python3
"""Deterministic exact replay for Item 368.

This checker verifies the denominator-clearing recurrence for the two j=1
saturation-boundary pairs, the K0 very-well-poised hypergeometric rectangle
and its two crossed Whipple evaluations, the exact parameter-state rank, the
K1 linear-rank lower bound, and the target-line saturated-carrier bridge.

There is no prime scan, collision census, or asymptotic extrapolation.
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
DEFAULT_OUTPUT = HERE / "item368_j1_boundary_whipple_rank_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "scripts/item218_j1_common_log_certificate.py":
        "a238c5ca37263f2553da47bf3f21253aedf1c34f8c57458a4a274fc6cdc9029a",
    "results/item218_j1_common_log_certificate.json":
        "963bbb8a9758e55ede72f965693d21fc41aa70d44e2d981d5873685c3f08ea0f",
    "results/item218_j1_common_log_manifest.json":
        "e1c6c3d713670c819b5f27b1005db26f9b804ec8ee0766671928fc30c1ff6d8d",
    "sources/item360_j1_full_gate_transverse_period_report.md":
        "4468412fb8631924952dc7f70fc4e75433a7524954b89525de508e55feefc8c4",
    "results/item360_j1_full_gate_transverse_period_root_audit.json":
        "7a23e487b4d70d63f9785339344bdc00ae0e8350bcf1d8b1fcf6228c230e5138",
    "manifests/item360_j1_full_gate_transverse_period_manifest.json":
        "92f88a56162f3803b8699922da921333f5225c41a32d14c87641dd53c3f8b55b",
    "sources/item364_j1_saturation_boundary_phase_carrier_report.md":
        "2c18f6ac22220e553349e44a723e200d20f4f3c89cfec5cd83812db260834e92",
    "scripts/item364_j1_saturation_boundary_phase_carrier_certificate.py":
        "ef9046fc4d7071779a73bf6e1bfd7d312789b994bd3274eec2a78d818d027b07",
    "results/item364_j1_saturation_boundary_phase_carrier_certificate.json":
        "ca1987d1688789dbf0e64f3eec2c4b771b9873f829e61d1b5f62302f47443926",
    "results/item364_j1_saturation_boundary_phase_carrier_root_audit.json":
        "fa6170a0c014cee655ba00c5288905344a969aa22b141d44b64ae4a2d3219a89",
    "manifests/item364_j1_saturation_boundary_phase_carrier_manifest.json":
        "bd0c5435fe4d0b7266d81b4f97dfacf8b2fca55fb2c95770e7cb853c2f77426c",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify_dependencies()
ITEM218 = load_module(
    "item368_pinned_item218",
    ROOT / "scripts/item218_j1_common_log_certificate.py",
)
ITEM364 = load_module(
    "item368_pinned_item364",
    ROOT / "scripts/item364_j1_saturation_boundary_phase_carrier_certificate.py",
)


def pochhammer(value: Fraction | int, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= Fraction(value) + offset
    return answer


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def k0_hyper_coefficient(h_value: int, t_value: int) -> Fraction:
    c_value = Fraction(1 - 2 * h_value, 4)
    return (
        (1 - 2 * h_value)
        * pochhammer(-h_value, t_value)
        * pochhammer(Fraction(1, 2) - h_value, t_value)
        * pochhammer(c_value + 1, t_value)
        / (
            pochhammer(Fraction(3, 2), t_value)
            * pochhammer(c_value, t_value)
            * math.factorial(t_value)
        )
    )


def hyper_f(h_value: int, a_value: Fraction, b_value: Fraction) -> Fraction:
    """The terminating 4F3(-1) after removing the factor 1-2h."""
    c_value = Fraction(1 - 2 * h_value, 4)
    answer = Fraction(0)
    for t_value in range(h_value + 1):
        answer += (
            pochhammer(-h_value, t_value)
            * pochhammer(Fraction(1, 2) - h_value, t_value)
            * pochhammer(c_value + 1, t_value)
            * pochhammer(a_value, t_value)
            * ((-1) ** t_value)
            / (
                pochhammer(Fraction(3, 2), t_value)
                * pochhammer(c_value, t_value)
                * pochhammer(b_value, t_value)
                * math.factorial(t_value)
            )
        )
    return answer


def whipple_rectangle_replay() -> dict[str, Any]:
    controls = (1, 2, 4, 5, 7, 8, 10, 11)
    rows = []
    for h_value in controls:
        kernel = ITEM218.kernel_integer(h_value, 1)
        for t_value in range(h_value + 1):
            if k0_hyper_coefficient(h_value, t_value) != kernel[2 * t_value + 1]:
                raise AssertionError((h_value, t_value, "K0 odd coefficient"))

        a_s = Fraction(3 - 4 * h_value, 6)
        a_h = Fraction(h_value + 1)
        b_s = Fraction(1 - 4 * h_value, 2)
        b_h = Fraction(3 - h_value, 3)
        delta = Fraction(10 * h_value + 3, 6)
        if a_h - a_s != delta or b_h - b_s != delta or delta.denominator == 1:
            raise AssertionError((h_value, "rectangle gap"))

        x_value, y_value, _, _ = ITEM364.phase_values(h_value)
        if x_value != (1 - 2 * h_value) * hyper_f(h_value, a_s, b_s):
            raise AssertionError((h_value, "X rectangle"))
        if y_value != (1 - 2 * h_value) * hyper_f(h_value, a_h, b_h):
            raise AssertionError((h_value, "Y rectangle"))

        cross_sh = hyper_f(h_value, a_s, b_h)
        cross_hs = hyper_f(h_value, a_h, b_s)
        product_sh = (
            pochhammer(Fraction(3, 2) - h_value, h_value)
            / pochhammer(Fraction(3 - h_value, 3), h_value)
        )
        product_hs = (
            pochhammer(Fraction(3, 2) - h_value, h_value)
            / pochhammer(Fraction(1, 2) - 2 * h_value, h_value)
        )
        if cross_sh != product_sh or cross_hs != product_hs:
            raise AssertionError((h_value, "Whipple product"))

        # Every numerator and denominator linear factor in the two products,
        # including 1-2h, has absolute value below every actual p>=4h+9.
        sh_num = [abs(2 * j_value + 3 - 2 * h_value) for j_value in range(h_value)]
        sh_den = [abs(3 * j_value + 3 - h_value) for j_value in range(h_value)]
        hs_den = [abs(2 * j_value + 1 - 4 * h_value) for j_value in range(h_value)]
        factors = [3, 2, abs(1 - 2 * h_value), *sh_num, *sh_den, *hs_den]
        if 0 in factors or max(factors) >= 4 * h_value + 9:
            raise AssertionError((h_value, "crossed p-unit factor audit", max(factors)))

        rows.append(
            {
                "h": h_value,
                "A_s": fraction_record(a_s),
                "A_h": fraction_record(a_h),
                "B_s": fraction_record(b_s),
                "B_h": fraction_record(b_h),
                "delta": fraction_record(delta),
                "cross_s_h": fraction_record(cross_sh),
                "cross_h_s": fraction_record(cross_hs),
                "maximum_absolute_product_factor": max(factors),
            }
        )
    return {
        "classification": "EXACT PREDECLARED SYMBOLIC CONTROLS; NO PRIME SCAN",
        "rows": rows,
        "general_identity": (
            "F_h(A_s;B_h)=(3/2-h)_h/(1-h/3)_h and "
            "F_h(A_h;B_s)=(3/2-h)_h/(1/2-2h)_h"
        ),
        "contiguity_gap": "A_h-A_s=B_h-B_s=(10h+3)/6 is nonintegral when 3 does not divide h",
        "actual_prime_unit": "both crossed normalized periods are p-units for p>=4h+9",
    }


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i_value, left_value in enumerate(left):
        for j_value, right_value in enumerate(right):
            answer[i_value + j_value] += left_value * right_value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def b_basis_polynomial(h_value: int, t_value: int) -> list[int]:
    answer = [1]
    for offset in range(t_value, h_value):
        answer = poly_mul(answer, [offset, 1])
    return answer


def parameter_rank_replay() -> dict[str, Any]:
    controls = (1, 2, 4, 5, 8, 11)
    rows = []
    for h_value in controls:
        degrees = []
        for t_value in range(h_value + 1):
            coefficient = k0_hyper_coefficient(h_value, t_value) / (1 - 2 * h_value)
            if coefficient == 0:
                raise AssertionError((h_value, t_value, "zero hyper coefficient"))
            basis = b_basis_polynomial(h_value, t_value)
            degree = len(basis) - 1
            if degree != h_value - t_value or basis[-1] != 1:
                raise AssertionError((h_value, t_value, basis))
            degrees.append(degree)
        if sorted(degrees) != list(range(h_value + 1)):
            raise AssertionError((h_value, degrees))
        rows.append({"h": h_value, "state_rank": h_value + 1, "basis_degrees": degrees})
    return {
        "classification": "EXACT TRIANGULAR BASIS CONTROLS",
        "rows": rows,
        "theorem": (
            "span_A F_h(A;B)=span{1/(B)_t:0<=t<=h}; multiplying by (B)_h gives "
            "the monic triangular basis (B+t)_(h-t), hence exact rank h+1"
        ),
        "method_scope": "parameter-uniform denominator transfer or bounded matched-value interpolation",
    }


def k1_numerator_polynomial(h_value: int, j_value: int) -> int:
    h = h_value
    j = j_value
    return 4 * (
        4 * h**4
        - 16 * h**3 * j
        + 20 * h**3
        + 24 * h**2 * j**2
        - 72 * h**2 * j
        + 35 * h**2
        - 16 * h * j**3
        + 84 * h * j**2
        - 112 * h * j
        + 25 * h
        + 4 * j**4
        - 32 * j**3
        + 80 * j**2
        - 64 * j
        + 6
    )


def k1_rank_replay() -> dict[str, Any]:
    controls = (2, 4, 5, 8, 11, 14)
    rows = []
    for h_value in controls:
        kernel = ITEM218.kernel_integer(h_value, 4)
        zero_even = 0
        zero_odd = 0
        for degree in range(2 * h_value + 1):
            denominator = math.prod(2 * h_value - degree + offset for offset in range(1, 5))
            left = kernel[degree] * denominator
            right = ((-1) ** degree) * math.comb(2 * h_value, degree) * k1_numerator_polynomial(
                h_value, degree
            )
            if left != right:
                raise AssertionError((h_value, degree, left, right))
            if kernel[degree] == 0:
                if degree % 2:
                    zero_odd += 1
                else:
                    zero_even += 1
        if zero_even > 4 or zero_odd > 4:
            raise AssertionError((h_value, zero_even, zero_odd))
        even_nonzero = sum(kernel[2 * t_value] != 0 for t_value in range(h_value + 3))
        odd_nonzero = sum(kernel[2 * t_value + 1] != 0 for t_value in range(h_value + 2))
        if even_nonzero < max(0, h_value - 3) or odd_nonzero < max(0, h_value - 4):
            raise AssertionError((h_value, even_nonzero, odd_nonzero))
        rows.append(
            {
                "h": h_value,
                "even_state_rank": even_nonzero,
                "odd_state_rank": odd_nonzero,
                "interior_even_zeros": zero_even,
                "interior_odd_zeros": zero_odd,
            }
        )
    return {
        "classification": "EXACT PREDECLARED COEFFICIENT CONTROLS",
        "rows": rows,
        "quartic_leading_coefficient_in_j": 16,
        "theorem": (
            "for 0<=j<=2h, K1_j=(-1)^j*C(2h,j)*P_h(j)/(2h-j+1)_4 with quartic P_h; "
            "there are at most four interior zeros, so the even and odd parameter-state ranks "
            "are at least h-3 and h-4 respectively"
        ),
        "exact_degeneracy": "h=2 has an identically zero odd family and is separately closed by Item 364",
    }


def cleared_value(kernel: list[int], a_value: Fraction, b_value: Fraction, odd: bool) -> tuple[Fraction, Fraction]:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    q_value = Fraction(kernel[1] if odd else kernel[0])
    for t_value in range(1, maximum_t + 1):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        term = ((-1) ** t_value) * pochhammer(a_value, t_value) * kernel[degree]
        q_value = (b_value + t_value - 1) * q_value + term
    denominator = pochhammer(b_value, maximum_t)
    return q_value, denominator


def poly_add(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * max(len(left), len(right))
    for index in range(len(answer)):
        answer[index] = (left[index] if index < len(left) else 0) + (
            right[index] if index < len(right) else 0
        )
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def poly_scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * value for value in poly]


def rising_linear(slope: int, constant: int, length: int) -> list[int]:
    answer = [1]
    for offset in range(length):
        answer = poly_mul(answer, [constant + offset, slope])
    return answer


def cleared_polynomial(
    kernel: list[int],
    a_slope: int,
    a_constant: int,
    b_slope: int,
    b_constant: int,
    odd: bool,
) -> tuple[list[int], int]:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    q_value = [kernel[1] if odd else kernel[0]]
    for t_value in range(1, maximum_t + 1):
        q_value = poly_mul(q_value, [b_constant + t_value - 1, b_slope])
        degree = 2 * t_value + 1 if odd else 2 * t_value
        term = poly_scale(
            rising_linear(a_slope, a_constant, t_value),
            ((-1) ** t_value) * kernel[degree],
        )
        q_value = poly_add(q_value, term)
    return q_value, maximum_t


def poly_eval(poly: list[int], value: Fraction) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def strip_small_prime_factors(value: int, bound: int) -> int:
    value = abs(value)
    for divisor in range(2, bound + 1):
        while value and value % divisor == 0:
            value //= divisor
    return value


def clearing_and_saturation_replay() -> dict[str, Any]:
    controls = (1, 2, 4, 5, 7, 8)
    rows = []
    for h_value in controls:
        sigma = Fraction(-(4 * h_value + 3), 6)
        kernel_0 = ITEM218.kernel_integer(h_value, 1)
        kernel_1 = ITEM218.kernel_integer(h_value, 4)
        x_value, y_value, u_value, v_value = ITEM364.phase_values(h_value)

        specifications = (
            ("X", kernel_0, 1, 1, 3, 2, True, x_value),
            ("Y", kernel_0, 0, h_value + 1, 2, h_value + 2, True, y_value),
            ("U", kernel_1, 1, 0, 3, 0, False, u_value),
            ("V", kernel_1, 0, h_value + 1, 2, h_value + 1, True, v_value),
        )
        scaled_values: dict[str, int] = {}
        for label, kernel, a_slope, a_constant, b_slope, b_constant, odd, phase in specifications:
            polynomial, maximum_t = cleared_polynomial(
                kernel, a_slope, a_constant, b_slope, b_constant, odd
            )
            a_phase = a_slope * sigma + a_constant
            b_phase = b_slope * sigma + b_constant
            direct_q, direct_denominator = cleared_value(kernel, a_phase, b_phase, odd)
            if poly_eval(polynomial, sigma) != direct_q:
                raise AssertionError((h_value, label, "clearing recurrence"))
            if direct_q / direct_denominator != phase:
                raise AssertionError((h_value, label, "phase quotient"))
            if len(polynomial) - 1 > maximum_t:
                raise AssertionError((h_value, label, "degree bound"))
            scaled = poly_eval(polynomial, sigma) * (6**maximum_t)
            if scaled.denominator != 1:
                raise AssertionError((h_value, label, "linear-resultant integrality"))
            scaled_values[label] = scaled.numerator
            if strip_small_prime_factors(scaled.numerator, 4 * h_value + 3) != strip_small_prime_factors(
                phase.numerator, 4 * h_value + 3
            ):
                raise AssertionError((h_value, label, "large-prime support bridge"))

        carrier_xy = math.gcd(abs(x_value.numerator), abs(y_value.numerator))
        carrier_uv = math.gcd(abs(u_value.numerator), abs(v_value.numerator))
        norm_xy = math.gcd(abs(scaled_values["X"]), abs(scaled_values["Y"]))
        norm_uv = math.gcd(abs(scaled_values["U"]), abs(scaled_values["V"]))
        sat_xy = strip_small_prime_factors(carrier_xy, 4 * h_value + 3)
        sat_uv = strip_small_prime_factors(carrier_uv, 4 * h_value + 3)
        if strip_small_prime_factors(norm_xy, 4 * h_value + 3) != sat_xy:
            raise AssertionError((h_value, "XY target norm"))
        if strip_small_prime_factors(norm_uv, 4 * h_value + 3) != sat_uv:
            raise AssertionError((h_value, "UV target norm"))
        rows.append(
            {
                "h": h_value,
                "large_prime_saturation_xy": sat_xy,
                "large_prime_saturation_uv": sat_uv,
                "scaled_target_line_values": scaled_values,
            }
        )
    return {
        "classification": "EXACT PREDECLARED TARGET-LINE CONTROLS; NO PRIME SCAN",
        "rows": rows,
        "clearing_recurrence": "Q_0=k_epsilon; Q_t=(B+t-1)Q_(t-1)+(-1)^t(A)_t*k_(epsilon+2t)",
        "quotient": "S=Q_n/(B)_n",
        "target_line": "L_h(s)=6s+4h+3; sigma_h=-(4h+3)/6",
        "large_prime_bridge": (
            "after removing every prime <=4h+3, the gcd of the two linear target-line norms "
            "has exactly the same prime support as the Item 364 phase carrier"
        ),
        "exact_zero_rule": "a zero pair is kept as a separate characteristic-zero phase stratum",
    }


def saturated_comparison_replay() -> dict[str, Any]:
    controls = (
        (12, 2, 1, 17),
        (34, 8, 2, 47),
        (30, 4, 4, 43),
    )
    rows = []
    for m_value, h_value, s_value, prime in controls:
        if m_value != 3 * h_value + 4 * s_value + 2:
            raise AssertionError((m_value, h_value, s_value, "M tie"))
        if prime != 4 * h_value + 6 * s_value + 3:
            raise AssertionError((m_value, h_value, s_value, prime, "p tie"))
        if 12 * h_value < m_value or not (4 * h_value + 3 < prime <= 18 * h_value):
            raise AssertionError((m_value, h_value, prime, "bulk"))
        carrier = math.factorial(18 * h_value) // math.factorial(4 * h_value)
        saturated = strip_small_prime_factors(carrier, 4 * h_value + 3)
        if saturated % prime:
            raise AssertionError((m_value, h_value, prime, "saturated comparison"))
        rows.append({"M": m_value, "h": h_value, "s": s_value, "p": prime})
    return {
        "classification": "EXACT PREDECLARED COMPARISON CONTROLS",
        "rows": rows,
        "comparison": "C_h=(18h)!/(4h)!, then remove all prime factors <=4h+3",
        "positive_rate_bulk": "M/12<=h<=M/3 retains every actual p and has Chebyshev mass M/8+o(M)",
        "capacity_per_6M": "1/48",
        "scope": (
            "small-prime saturation does not repair generic recurrence/height/divisor-sieve reasoning; "
            "no resemblance to the actual carriers is asserted"
        ),
    }


def capacity_replay() -> dict[str, Any]:
    if Fraction(1, 6) / 6 != Fraction(1, 36):
        raise AssertionError("fixed-j1 capacity normalization")
    if Fraction(1, 8) / 6 != Fraction(1, 48):
        raise AssertionError("comparison normalization")
    return {
        "raw_fixed_j1_mass_per_M": "1/6",
        "shared_full_fixed_j1_ceiling_per_6M": "1/36",
        "saturated_comparison_mass_per_M": "1/8",
        "saturated_comparison_capacity_per_6M": "1/48",
        "boundaries_are_nonadditive": True,
        "new_booking": 0,
        "new_capacity_reduction": 0,
    }


def build_result() -> dict[str, Any]:
    return {
        "item": 368,
        "schema": "item368-j1-boundary-whipple-rank-obstruction-v1",
        "classification": "PROVED_WHIPPLED_CROSSES_AND_LINEAR_PARAMETER_STATE_BARRIER",
        "dependencies": DEPENDENCIES,
        "dependency_hashes_verified": True,
        "whipple_rectangle_replay": whipple_rectangle_replay(),
        "parameter_rank_replay": parameter_rank_replay(),
        "k1_rank_replay": k1_rank_replay(),
        "clearing_and_saturation_replay": clearing_and_saturation_replay(),
        "saturated_comparison_replay": saturated_comparison_replay(),
        "capacity_replay": capacity_replay(),
        "strict_labels": {
            "proved": [
                "exact denominator-clearing recurrence and fixed-h target-line norm formulation",
                "large-prime saturation removes every factor incapable of being an actual tied prime",
                "K0 off-diagonal 4F3(-1) rectangle and both crossed Whipple product evaluations",
                "crossed products are p-units and lie in distinct integer-contiguity orbits from the actual entries",
                "exact K0 parameter-uniform state rank h+1 and K1 state rank at least h-O(1)",
                "scoped no-go for bounded matched-value/contiguous transfer and generic saturated recurrence-height sieve methods",
                "zero booking and retention of the shared 1/36 ceiling",
            ],
            "finite_only": [
                "eight declared Whipple controls, six rank controls, six K1 controls, six target-line controls, and three comparison controls",
                "no prime scan, collision census, or extrapolation",
            ],
            "open": [
                "classification of exact-zero phase pairs",
                "weighted zero density or average gcd for the actual saturated carriers",
                "a target-specific identity exploiting the two actual moving numerator parameters",
                "any strict fixed-j1 capacity reduction",
            ],
        },
        "scope_warning": (
            "The rank theorem is parameter-uniform and the contiguity theorem concerns classical integer shifts. "
            "They do not rule out a new target-specific arithmetic identity. The comparison closes only generic "
            "recurrence/height/resultant/divisor-sieve reasoning. Neither boundary is proved zero-rate."
        ),
        "verdict": (
            "The natural crossed Whipple completion evaluates only p-unit companions and cannot reach the actual "
            "off-diagonal periods by integer contiguity; the universal state grows linearly. Together with target-line "
            "saturation this closes a broad standard method class, but no actual-family weighted mass changes."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "classification": result["classification"],
                "new_booking": result["capacity_replay"]["new_booking"],
                "new_capacity_reduction": result["capacity_replay"]["new_capacity_reduction"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
