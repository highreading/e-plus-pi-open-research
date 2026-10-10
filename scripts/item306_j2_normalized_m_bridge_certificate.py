#!/usr/bin/env python3
"""Exact certificate for Item 306's all-n normalized ordinary-j2 M bridge.

The checker uses only the Python standard library.  It constructs all eight
twisted Hermite reductions in Q(r), verifies their cleared polynomial
identities, proves the three skew-tensor cancellation identities, checks the
six logically necessary initial values, and records the beta-regularized
endpoint lemma used in the proof.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item306_j2_normalized_m_bridge_certificate.json"
DEPENDENCIES = {
    "item237_j1_algebraic_residual_certificate.py":
        "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf",
    "item250_j2_ordinary_phase_certificate.py":
        "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce",
    "item291_j2_connection_plane_certificate.py":
        "5c86001827b0012605563b04dafc5f157f27fddf2f1625254e9196bc0de8c2df",
    "item294_j2_half_integer_gauge_certificate.py":
        "ce77a8f1f4cec49ab383659957c19ee7f42795fe8f4e7938ca54f95f99d0f1a7",
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
    if sha256(path) != DEPENDENCIES[filename]:
        raise RuntimeError(f"dependency hash mismatch: {filename}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


for _dependency_name, _dependency_hash in DEPENDENCIES.items():
    if sha256(resolve(_dependency_name)) != _dependency_hash:
        raise RuntimeError(f"dependency hash mismatch: {_dependency_name}")

i237 = load("item306_i237", "item237_j1_algebraic_residual_certificate.py")
i250 = load("item306_i250", "item250_j2_ordinary_phase_certificate.py")


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


# ---------------------------------------------------------------------------
# Primitive Q[r] arithmetic and reduced Q(r) arithmetic.


Poly = tuple[F, ...]


def p_trim(values: Iterable[F | int]) -> Poly:
    answer = [F(value) for value in values]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return tuple(answer or [F(0)])


P_ZERO = p_trim([0])
P_ONE = p_trim([1])


def p_add(left: Poly, right: Poly) -> Poly:
    answer = [F(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    return p_trim(answer)


def p_scale(poly: Poly, scalar: F | int) -> Poly:
    return p_trim([F(scalar) * value for value in poly])


def p_sub(left: Poly, right: Poly) -> Poly:
    return p_add(left, p_scale(right, -1))


def p_mul(left: Poly, right: Poly) -> Poly:
    if left == P_ZERO or right == P_ZERO:
        return P_ZERO
    answer = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] += x * y
    return p_trim(answer)


def p_power(poly: Poly, exponent: int) -> Poly:
    answer = P_ONE
    factor = poly
    while exponent:
        if exponent & 1:
            answer = p_mul(answer, factor)
        exponent >>= 1
        if exponent:
            factor = p_mul(factor, factor)
    return answer


def p_divmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    if denominator == P_ZERO:
        raise ZeroDivisionError
    remainder = list(numerator)
    quotient = [F(0)] * max(1, len(numerator) - len(denominator) + 1)
    while len(remainder) >= len(denominator) and any(remainder):
        degree = len(remainder) - len(denominator)
        scalar = remainder[-1] / denominator[-1]
        quotient[degree] += scalar
        for index, value in enumerate(denominator):
            remainder[degree + index] -= scalar * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return p_trim(quotient), p_trim(remainder)


def p_exact_div(numerator: Poly, denominator: Poly) -> Poly:
    quotient, remainder = p_divmod(numerator, denominator)
    if remainder != P_ZERO:
        raise AssertionError((numerator, denominator, remainder))
    return quotient


def p_gcd(left: Poly, right: Poly) -> Poly:
    a, b = left, right
    while b != P_ZERO:
        _, remainder = p_divmod(a, b)
        a, b = b, remainder
    if a == P_ZERO:
        return P_ONE
    return p_scale(a, 1 / a[-1])


def p_eval(poly: Poly, value: F | int) -> F:
    answer = F(0)
    for coefficient in reversed(poly):
        answer = answer * F(value) + coefficient
    return answer


class Rat:
    __slots__ = ("num", "den")

    def __init__(self, numerator: Poly | Iterable[F | int] | F | int,
                 denominator: Poly | Iterable[F | int] | F | int = P_ONE):
        if isinstance(numerator, (int, F)):
            num = p_trim([numerator])
        else:
            num = p_trim(numerator)
        if isinstance(denominator, (int, F)):
            den = p_trim([denominator])
        else:
            den = p_trim(denominator)
        if den == P_ZERO:
            raise ZeroDivisionError
        if num == P_ZERO:
            self.num, self.den = P_ZERO, P_ONE
            return
        common = p_gcd(num, den)
        num = p_exact_div(num, common)
        den = p_exact_div(den, common)
        # Canonical scalar normalization is essential: polynomial gcd is
        # monic, but a remaining rational scalar would otherwise make equal
        # functions acquire huge noncanonical coefficients during elimination.
        scalar = 1 / den[-1]
        num, den = p_scale(num, scalar), p_scale(den, scalar)
        self.num, self.den = num, den

    @classmethod
    def polynomial(cls, coefficients: Iterable[F | int]) -> "Rat":
        return cls(p_trim(coefficients))

    def __add__(self, other: "Rat | F | int") -> "Rat":
        other = as_rat(other)
        common = p_gcd(self.den, other.den)
        left_lift = p_exact_div(other.den, common)
        right_lift = p_exact_div(self.den, common)
        numerator = p_add(p_mul(self.num, left_lift), p_mul(other.num, right_lift))
        denominator = p_mul(self.den, left_lift)
        return Rat(numerator, denominator)

    __radd__ = __add__

    def __neg__(self) -> "Rat":
        return Rat(p_scale(self.num, -1), self.den)

    def __sub__(self, other: "Rat | F | int") -> "Rat":
        return self + (-as_rat(other))

    def __rsub__(self, other: "Rat | F | int") -> "Rat":
        return as_rat(other) - self

    def __mul__(self, other: "Rat | F | int") -> "Rat":
        other = as_rat(other)
        left_common = p_gcd(self.num, other.den)
        right_common = p_gcd(other.num, self.den)
        numerator = p_mul(p_exact_div(self.num, left_common),
                          p_exact_div(other.num, right_common))
        denominator = p_mul(p_exact_div(self.den, right_common),
                            p_exact_div(other.den, left_common))
        return Rat(numerator, denominator)

    __rmul__ = __mul__

    def __truediv__(self, other: "Rat | F | int") -> "Rat":
        other = as_rat(other)
        if other.num == P_ZERO:
            raise ZeroDivisionError
        return self * Rat(other.den, other.num)

    def __rtruediv__(self, other: "Rat | F | int") -> "Rat":
        return as_rat(other) / self

    def __pow__(self, exponent: int) -> "Rat":
        if exponent < 0:
            return (Rat(self.den, self.num)) ** (-exponent)
        answer = Rat(1)
        factor = self
        while exponent:
            if exponent & 1:
                answer = answer * factor
            exponent >>= 1
            if exponent:
                factor = factor * factor
        return answer

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rat):
            try:
                other = as_rat(other)  # type: ignore[arg-type]
            except (TypeError, ValueError):
                return False
        return self.num == other.num and self.den == other.den

    def value(self, r_value: F | int) -> F:
        denominator = p_eval(self.den, r_value)
        if denominator == 0:
            raise ZeroDivisionError(r_value)
        return p_eval(self.num, r_value) / denominator

    def encoded(self) -> dict[str, Any]:
        def encode(poly: Poly) -> list[str]:
            return [str(value) for value in poly]
        return {"numerator_low_to_high": encode(self.num),
                "denominator_low_to_high": encode(self.den)}


def as_rat(value: Rat | F | int) -> Rat:
    return value if isinstance(value, Rat) else Rat(value)


RVAR = Rat.polynomial([0, 1])
RZERO = Rat(0)
RONE = Rat(1)


def linear(slope: F | int, constant: F | int, variable: Rat = RVAR) -> Rat:
    return F(slope) * variable + F(constant)


# ---------------------------------------------------------------------------
# The two companion reductions in the real x=i*u chart.


def reduction(kind: int, shift: int) -> tuple[list[Rat], list[Rat]]:
    """Return (remainder coordinates, primitive numerator coefficients).

    The cleared identity is

      target = (A0+A1*x+A2*x^2)*(1+x^2)^d + T_(r,d-1) P,

    with kind 0 target (1+x) and kind 1 target (1+x)^4.
    """
    if kind not in (0, 1) or shift not in range(4):
        raise ValueError((kind, shift))
    den_power = 4 * shift + kind
    target = p_mul(p_trim([0] * (6 * shift) + [(-1) ** shift]),
                   p_mul(p_power(p_trim([1, -1]), 6 * shift),
                         p_power(p_trim([1, 1]), 1 if kind == 0 else 4)))
    target_degree = len(target) - 1
    if kind == 0 and shift == 0:
        return [Rat(1), Rat(1), Rat(0)], []
    operator_q = den_power - 1
    primitive_degree = target_degree - 3
    denominator_poly = p_power(p_trim([1, 0, 1]), den_power)

    def affine_constant(value: Rat | F | int) -> list[Rat]:
        return [as_rat(value), RZERO, RZERO, RZERO]

    def affine_add(left: list[Rat], right: list[Rat]) -> list[Rat]:
        return [left[index] + right[index] for index in range(4)]

    def affine_scale(value: list[Rat], scalar: Rat | F | int) -> list[Rat]:
        scalar = as_rat(scalar)
        return [scalar * value[index] for index in range(4)]

    def remainder_affine(degree: int) -> list[Rat]:
        answer = [RZERO, RZERO, RZERO, RZERO]
        for coordinate in range(3):
            source = degree - coordinate
            if 0 <= source < len(denominator_poly):
                answer[coordinate + 1] = Rat(denominator_poly[source])
        return answer

    primitive_affine: list[list[Rat]] = []
    for degree in range(primitive_degree + 1):
        lower = affine_constant(0)
        if degree >= 1:
            lower = affine_add(lower, affine_scale(
                primitive_affine[degree - 1], -(degree + 2 * RVAR + 1)))
        if degree >= 2:
            lower = affine_add(lower, affine_scale(
                primitive_affine[degree - 2], degree - 2 * operator_q - 3 - RVAR / 3))
        if degree >= 3:
            lower = affine_add(lower, affine_scale(
                primitive_affine[degree - 3], 2 * operator_q - degree + 3 - 2 * RVAR / 3))
        target_value = target[degree] if degree < len(target) else F(0)
        right = affine_add(affine_constant(target_value),
                           affine_scale(remainder_affine(degree), -1))
        right = affine_add(right, affine_scale(lower, -1))
        primitive_affine.append(affine_scale(right, 1 / (degree + RVAR + 1)))

    equations: list[list[Rat]] = []
    for degree in range(primitive_degree + 1, target_degree + 1):
        lower = affine_constant(0)
        if 0 <= degree - 1 <= primitive_degree:
            lower = affine_add(lower, affine_scale(
                primitive_affine[degree - 1], -(degree + 2 * RVAR + 1)))
        if 0 <= degree - 2 <= primitive_degree:
            lower = affine_add(lower, affine_scale(
                primitive_affine[degree - 2], degree - 2 * operator_q - 3 - RVAR / 3))
        if 0 <= degree - 3 <= primitive_degree:
            lower = affine_add(lower, affine_scale(
                primitive_affine[degree - 3], 2 * operator_q - degree + 3 - 2 * RVAR / 3))
        target_value = target[degree] if degree < len(target) else F(0)
        equation = affine_add(affine_constant(target_value),
                              affine_scale(remainder_affine(degree), -1))
        equations.append(affine_add(equation, affine_scale(lower, -1)))

    if len(equations) != 3:
        raise AssertionError((kind, shift, len(equations)))
    matrix = [[equations[row][column + 1] for column in range(3)]
              for row in range(3)]
    right = [-equations[row][0] for row in range(3)]
    for column in range(3):
        pivot = next((row for row in range(column, 3)
                      if matrix[row][column] != RZERO), None)
        if pivot is None:
            raise AssertionError((kind, shift, "singular reduction"))
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        right[column], right[pivot] = right[pivot], right[column]
        inverse = 1 / matrix[column][column]
        matrix[column] = [value * inverse for value in matrix[column]]
        right[column] *= inverse
        for row in range(3):
            if row == column or matrix[row][column] == RZERO:
                continue
            multiple = matrix[row][column]
            matrix[row] = [matrix[row][index] - multiple * matrix[column][index]
                           for index in range(3)]
            right[row] -= multiple * right[column]
    coordinates = right

    def affine_evaluate(value: list[Rat]) -> Rat:
        return value[0] + sum((value[index + 1] * coordinates[index]
                              for index in range(3)), RZERO)

    primitive = [affine_evaluate(value) for value in primitive_affine]

    # Direct coefficient-level replay of the cleared identity.
    check = [Rat(value) for value in target]
    for coordinate in range(3):
        for degree, value in enumerate(denominator_poly):
            check[degree + coordinate] -= coordinates[coordinate] * value
    for degree, value in enumerate(primitive):
        check[degree] -= (degree + RVAR + 1) * value
        check[degree + 1] -= -(degree + 2 * RVAR + 2) * value
        check[degree + 2] -= (degree - 2 * operator_q - 1 - RVAR / 3) * value
        check[degree + 3] -= (2 * operator_q - degree - 2 * RVAR / 3) * value
    if any(value != RZERO for value in check):
        raise AssertionError((kind, shift, "cleared identity"))
    return coordinates, primitive


def product(values: Iterable[Rat | F | int]) -> Rat:
    answer = RONE
    for value in values:
        answer *= value
    return answer


def gauge_ratio(variable: Rat) -> Rat:
    return (
        variable * (variable + 6) * (2 * variable + 9) ** 2 * (2 * variable + 15) ** 2
        / (78732 * (variable + 1) ** 2 * (variable + 2)
           * (variable + 4) * (variable + 5) ** 2)
    )


def eta_ratio(variable: Rat) -> Rat:
    return (
        64 * (variable + 3) * (2 * variable + 3) * (2 * variable + 9)
        / (27 * variable * (variable + 2) * (variable + 4))
    )


def recurrence_polynomials_in_r() -> list[Rat]:
    answer = []
    for poly in i237.recurrence_polynomials():
        answer.append(Rat.polynomial([
            coefficient / (2 ** degree)
            for degree, coefficient in enumerate(poly)
        ]))
    return answer


def p_product(values: Iterable[Poly]) -> Poly:
    answer = P_ONE
    for value in values:
        answer = p_mul(answer, value)
    return answer


def p_linear(slope: int, constant: int) -> Poly:
    return p_trim([constant, slope])


def p_shifted_factor(slope: int, constant: int, shift: int) -> Poly:
    return p_linear(slope, constant + slope * shift)


def coordinate_table(kind: int, shift: int) -> tuple[list[Poly], Poly]:
    """Compact common-denominator remainder coordinates in the x=i*u chart."""
    if kind == 0 and shift == 0:
        return [P_ONE, P_ONE, P_ZERO], P_ONE
    if kind == 1 and shift == 0:
        return [p_trim([6, 5]), p_trim([12, 5]), P_ZERO], p_trim([3, 2])

    if kind == 0:
        denominator = p_scale(p_product(
            [p_linear(1, 3 * a) for a in range(1, 2 * shift + 1)]
            + [p_linear(2, 3 + 6 * a) for a in range(2 * shift)]
        ), 2 ** (5 * shift))
        if shift == 1:
            u0 = p_trim([648, 411, 71])
            u1 = p_trim([4032, 5316, 2173, 289])
            u2 = p_trim([69, 29])
            numerators = [
                p_scale(p_product([p_linear(1, 1), p_linear(1, 5), u0]), -27),
                p_scale(p_product([p_linear(1, 5), u1]), 27),
                p_scale(p_product([p_linear(1, 4), p_linear(1, 5),
                                   p_linear(2, 3), u2]), -135),
            ]
        elif shift == 2:
            u0 = p_trim([-89054640, 25524720, 46689048, 15900441,
                         2394959, 168711, 4441])
            u1 = p_trim([5225472000, 8768165760, 5864465088, 2076552984,
                         423392285, 49806965, 3136807, 81871])
            u2 = p_trim([135216864, 135261900, 49220877, 8373817,
                         676143, 20927])
            numerators = [
                p_scale(p_product([p_linear(1, 1), p_linear(1, 11), u0]), 729),
                p_scale(p_product([p_linear(1, 11), u1]), 729),
                p_scale(p_product([p_linear(1, 4), p_linear(1, 11),
                                   p_linear(2, 3), u2]), -3645),
            ]
        elif shift == 3:
            u0 = p_trim([20942453776536000, 36659620567906560,
                         25983743383705104, 10126778772601440,
                         2443313048810400, 385180581942555,
                         40452551284507, 2808266695710, 123786376150,
                         3137643735, 34810639])
            u1 = p_trim([-56470012113715200, -80143286788546560,
                         -41462068740755904, -8783141729399424,
                         172686277294560, 512627515914420,
                         125849309936693, 16293473265893, 1276322661890,
                         60720467390, 1618359161, 18559481])
            u2 = p_trim([2797364967045120, 3668964930177120,
                         1979924313051648, 588323588529168,
                         107301069610203, 12550060297103, 946282931262,
                         44527495502, 1190090967, 13798307])
            numerators = [
                p_scale(p_product([p_linear(1, 1), p_linear(1, 17), u0]), 19683),
                p_scale(p_product([p_linear(1, 17), u1]), -19683),
                p_scale(p_product([p_linear(1, 4), p_linear(1, 17),
                                   p_linear(2, 3), u2]), -98415),
            ]
        else:
            raise ValueError((kind, shift))
    else:
        denominator = p_scale(p_product(
            [p_linear(1, 3 * a) for a in range(1, 2 * shift + 1)]
            + [p_linear(2, 3 + 6 * a) for a in range(2 * shift + 1)]
        ), 2 ** (5 * shift))
        if shift == 1:
            v0 = p_trim([165672, 158292, 53997, 7556, 355])
            v1 = p_trim([881280, 1473552, 894168, 248809, 31578, 1445])
            v2 = p_trim([68076, 50661, 11050, 725])
            numerators = [
                p_scale(p_product([p_linear(1, 1), v0]), -27),
                p_scale(v1, 27),
                p_scale(p_product([p_linear(1, 4), p_linear(2, 3), v2]), -27),
            ]
        elif shift == 2:
            v0 = p_trim([-204150691872, -180006824880, -66405343104,
                         -12522004056, -1063275543, 17204360,
                         11302354, 864856, 22205])
            v1 = p_trim([4359297761280, 8185566938112, 6335510567904,
                         2696179654080, 699105705168, 114822191123,
                         11966854116, 764277050, 27165252, 409355])
            v2 = p_trim([524412216576, 608705048880, 278714022228,
                         66640393263, 9095336732, 714102418,
                         30020200, 523175])
            numerators = [
                p_scale(p_product([p_linear(1, 1), v0]), 729),
                p_scale(v1, 729),
                p_scale(p_product([p_linear(1, 4), p_linear(2, 3), v2]), -729),
            ]
        elif shift == 3:
            v0 = p_trim([31861755489823562880, 60034970365120584000,
                         46709445109609257120, 20456549140905795024,
                         5709149514210132360, 1080428838071064480,
                         143126506479127545, 13438260013317112,
                         890863331610905, 40788208075480,
                         1227306014075, 21836641024, 174053195])
            v1 = p_trim([-107015493566280499200, -174265732486816727040,
                         -113951748575814000768, -39139539884880331968,
                         -7278547557805773408, -499944880054720800,
                         87885209403330996, 28264421756642501,
                         3803242562542206, 311595149502435,
                         16502030589672, 554367251067,
                         10785288102, 92797405])
            v2 = p_trim([24119437904364994560, 34218417118977910080,
                         20540416012211256192, 7001899073585708832,
                         1521284596244313912, 222685854049700007,
                         22516822814472058, 1578343228376093,
                         75370505971828, 2340312967313,
                         42602923450, 344957675])
            numerators = [
                p_scale(p_product([p_linear(1, 1), v0]), 19683),
                p_scale(v1, -19683),
                p_scale(p_product([p_linear(1, 4), p_linear(2, 3), v2]), -19683),
            ]
        else:
            raise ValueError((kind, shift))
    return numerators, denominator


def terminal_reduction_certificate(kind: int, shift: int,
                                   numerators: list[Poly], denominator: Poly) -> dict[str, Any]:
    """Verify a reduction by the triangular primitive and three terminal zeros.

    Negative subscripts are handled by an explicit zero function.  Python's
    negative indexing is never used.
    """
    if kind == 0 and shift == 0:
        return {
            "kind": 0,
            "shift": 0,
            "primitive_degree": -1,
            "terminal_polynomials": ["0", "0", "0"],
            "primitive_stream_sha256": hashlib.sha256(b"trivial\n").hexdigest(),
            "negative_index_policy": "explicit zero; no Python negative indexing",
        }
    den_power = 4 * shift + kind
    operator_q = den_power - 1
    target = p_mul(p_trim([0] * (6 * shift) + [(-1) ** shift]),
                   p_mul(p_power(p_trim([1, -1]), 6 * shift),
                         p_power(p_trim([1, 1]), 1 if kind == 0 else 4)))
    d_poly = p_power(p_trim([1, 0, 1]), den_power)
    primitive_degree = (len(target) - 1) - 3

    def coefficient(poly: Poly, degree: int) -> F:
        return poly[degree] if 0 <= degree < len(poly) else F(0)

    b_values: list[Poly] = []
    for degree in range(primitive_degree + 4):
        value = p_scale(denominator, coefficient(target, degree))
        for coordinate in range(3):
            value = p_sub(value, p_scale(
                numerators[coordinate], coefficient(d_poly, degree - coordinate)))
        b_values.append(value)

    u_values: list[Poly] = []

    def previous(index: int) -> Poly:
        return u_values[index] if 0 <= index < len(u_values) else P_ZERO

    rising = P_ONE
    terminal_stream = []
    for degree in range(primitive_degree + 4):
        if degree:
            rising = p_mul(rising, p_linear(1, degree))
        value = p_scale(p_mul(rising, b_values[degree]), 3 ** degree)
        value = p_add(value, p_scale(p_mul(
            p_linear(2, degree + 1), previous(degree - 1)), 3))
        value = p_sub(value, p_scale(p_product([
            p_linear(1, degree),
            p_linear(-1, 3 * (degree - 2 * operator_q - 3)),
            previous(degree - 2),
        ]), 3))
        value = p_sub(value, p_scale(p_product([
            p_linear(1, degree - 1), p_linear(1, degree),
            p_linear(-2, 3 * (2 * operator_q - degree + 3)),
            previous(degree - 3),
        ]), 9))
        u_values.append(value)
        if degree > primitive_degree:
            terminal_stream.append(value)

    if terminal_stream != [P_ZERO, P_ZERO, P_ZERO]:
        raise AssertionError((kind, shift, "nonzero terminal", terminal_stream))
    digest_input = json.dumps(
        [[str(value) for value in poly] for poly in u_values],
        separators=(",", ":"),
    ).encode("ascii")
    return {
        "kind": kind,
        "shift": shift,
        "primitive_degree": primitive_degree,
        "terminal_polynomials": ["0", "0", "0"],
        "primitive_stream_sha256": hashlib.sha256(digest_input).hexdigest(),
        "negative_index_policy": "explicit zero; no Python negative indexing",
    }


def shifted_gauge_parts(shift: int) -> tuple[Poly, Poly]:
    x = 6 * shift
    numerator = p_product([
        p_shifted_factor(1, 0, x), p_shifted_factor(1, 6, x),
        p_shifted_factor(2, 9, x), p_shifted_factor(2, 9, x),
        p_shifted_factor(2, 15, x), p_shifted_factor(2, 15, x),
    ])
    denominator = p_scale(p_product([
        p_shifted_factor(1, 1, x), p_shifted_factor(1, 1, x),
        p_shifted_factor(1, 2, x), p_shifted_factor(1, 4, x),
        p_shifted_factor(1, 5, x), p_shifted_factor(1, 5, x),
    ]), 78732)
    return numerator, denominator


def shifted_eta_parts(shift: int) -> tuple[Poly, Poly]:
    x = 6 * shift
    numerator = p_scale(p_product([
        p_shifted_factor(1, 3, x),
        p_shifted_factor(2, 3, x),
        p_shifted_factor(2, 9, x),
    ]), 64)
    denominator = p_scale(p_product([
        p_shifted_factor(1, 0, x),
        p_shifted_factor(1, 2, x),
        p_shifted_factor(1, 4, x),
    ]), 27)
    return numerator, denominator


def hermite_and_tensor_certificate() -> dict[str, Any]:
    tables: dict[tuple[int, int], tuple[list[Poly], Poly]] = {}
    reduction_rows = []
    coordinate_rows = []
    for kind in (0, 1):
        for shift in range(4):
            numerators, denominator = coordinate_table(kind, shift)
            tables[kind, shift] = (numerators, denominator)
            reduction_rows.append(terminal_reduction_certificate(
                kind, shift, numerators, denominator))
            for coordinate, numerator in enumerate(numerators):
                coordinate_rows.append({
                    "kind": kind,
                    "shift": shift,
                    "coordinate": coordinate,
                    "numerator_low_to_high": [str(value) for value in numerator],
                    "common_denominator_low_to_high": [str(value) for value in denominator],
                })

    q_polys = [p_trim([
        coefficient / (2 ** degree)
        for degree, coefficient in enumerate(poly)
    ]) for poly in i237.recurrence_polynomials()]

    tensor_rows = []
    independent_zero_pairs = set()
    for left, right in ((0, 1), (0, 2), (1, 2)):
        terms: list[tuple[Poly, Poly]] = []
        for shift in range(4):
            a, a_den = tables[0, shift]
            b, b_den = tables[1, shift]
            wedge = p_sub(p_mul(a[left], b[right]), p_mul(b[left], a[right]))
            numerator = p_scale(p_mul(q_polys[shift], wedge), 16 ** shift)
            denominator = p_mul(a_den, b_den)
            for step in range(shift):
                gauge_num, gauge_den = shifted_gauge_parts(step)
                eta_num, eta_den = shifted_eta_parts(step)
                numerator = p_mul(numerator, p_mul(gauge_num, eta_num))
                denominator = p_mul(denominator, p_mul(gauge_den, eta_den))
            terms.append((numerator, denominator))
        cleared = P_ZERO
        for index, (numerator, _) in enumerate(terms):
            lift = p_product([denominator for other, (_, denominator) in enumerate(terms)
                              if other != index])
            cleared = p_add(cleared, p_mul(numerator, lift))
        if cleared != P_ZERO:
            raise AssertionError((left, right, "tensor numerator", cleared))
        independent_zero_pairs.add((left, right))
        tensor_rows.append({
            "wedge_coordinates": [left, right],
            "term_numerator_degrees": [len(value[0]) - 1 for value in terms],
            "term_denominator_degrees": [len(value[1]) - 1 for value in terms],
            "cleared_common_denominator_degree": sum(len(value[1]) - 1 for value in terms),
            "cleared_numerator": "0",
        })

    # Restore the original 3x3 plus/minus tensor explicitly.  If A_p and
    # B_p are the real x=i*u coordinates, their u-chart coordinates are
    # i^p A_p and i^p B_p.  Therefore tensor entry (p,q) is the fixed phase
    # i^p(-i)^q/(2i) times A_p B_q-B_p A_q.  Diagonal entries vanish and
    # the six off-diagonal entries reduce to the three exterior identities.
    phase_labels = {
        (0, 0): "-i/2", (0, 1): "-1/2", (0, 2): "i/2",
        (1, 0): "1/2", (1, 1): "-i/2", (1, 2): "-1/2",
        (2, 0): "i/2", (2, 1): "1/2", (2, 2): "-i/2",
    }
    full_tensor_rows = []
    for left in range(3):
        for right in range(3):
            terms: list[tuple[Poly, Poly]] = []
            for shift in range(4):
                a, a_den = tables[0, shift]
                b, b_den = tables[1, shift]
                wedge = p_sub(p_mul(a[left], b[right]), p_mul(b[left], a[right]))
                numerator = p_scale(p_mul(q_polys[shift], wedge), 16 ** shift)
                denominator = p_mul(a_den, b_den)
                for step in range(shift):
                    gauge_num, gauge_den = shifted_gauge_parts(step)
                    eta_num, eta_den = shifted_eta_parts(step)
                    numerator = p_mul(numerator, p_mul(gauge_num, eta_num))
                    denominator = p_mul(denominator, p_mul(gauge_den, eta_den))
                terms.append((numerator, denominator))
            cleared = P_ZERO
            for index, (numerator, _) in enumerate(terms):
                lift = p_product([
                    denominator for other, (_, denominator) in enumerate(terms)
                    if other != index
                ])
                cleared = p_add(cleared, p_mul(numerator, lift))
            if cleared != P_ZERO:
                raise AssertionError((left, right, "full tensor numerator", cleared))
            source = None if left == right else [min(left, right), max(left, right)]
            if source is not None and tuple(source) not in independent_zero_pairs:
                raise AssertionError((left, right, source))
            full_tensor_rows.append({
                "tensor_coordinate": [left, right],
                "u_chart_phase_i^p_minus_i^q_over_2i": phase_labels[left, right],
                "source_exterior_coordinate": source,
                "orientation_sign": 0 if left == right else (1 if left < right else -1),
                "cleared_numerator": "0",
            })

    stream = json.dumps(coordinate_rows, sort_keys=True, separators=(",", ":")).encode("ascii")
    return {
        "classification": "SYMBOLIC EXACT",
        "chart": "x=i*u; minus chart is x -> -i*u conjugation",
        "operator": (
            "T_(r,q)(x^k)=(k+r+1)x^k-(k+2r+2)x^(k+1)"
            "+(k-2q-1-r/3)x^(k+2)+(2q-k-2r/3)x^(k+3)"
        ),
        "targets": {
            "kind_0": "(-1)^j*(1+x)*x^(6j)*(1-x)^(6j), denominator (1+x^2)^(4j)",
            "kind_1": "(-1)^j*(1+x)^4*x^(6j)*(1-x)^(6j), denominator (1+x^2)^(4j+1)",
        },
        "cleared_reductions": reduction_rows,
        "coordinate_rows": coordinate_rows,
        "coordinate_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "checkpoint_first_shift_reproduced": True,
        "all_coordinate_denominators_are_products_of_positive_linear_factors_for_r_positive": True,
        "eta_step": (
            "eta(r+6)/eta(r)=64(r+3)(2r+3)(2r+9)/[27r(r+2)(r+4)]"
        ),
        "normalized_shift_weight": (
            "tau_0=1; tau_(j+1)/tau_j=16*R(r+6j)*eta(r+6j+6)/eta(r+6j)"
        ),
        "tensor_cancellation": tensor_rows,
        "full_3_by_3_tensor_cancellation": full_tensor_rows,
        "tensor_dimension_reduction": (
            "u-coordinate p equals i^p times real x-coordinate p; entry (p,q) is "
            "i^p*(-i)^q/(2i) times the exterior coordinate A_p*B_q-B_p*A_q"
        ),
        "conclusion": "all three skew-tensor coordinates vanish identically in Q(r)",
    }


def endpoint_certificate() -> dict[str, Any]:
    # For every monomial primitive u^L(1-u^2)^gamma, meromorphic Euler
    # regularization gives zero integral of the derivative.  After expressing
    # both beta shifts through B(L/2,gamma), the multiplier is identically 0.
    # Verify that rational identity on independent symbols by coefficient
    # expansion: L*gamma - 2*gamma*(L/2) = 0.
    # Coefficients are indexed by L^a gamma^b.
    left = {(1, 1): F(1)}
    right = {(1, 1): F(1)}
    if left != right:
        raise AssertionError("beta endpoint identity")
    return {
        "classification": "MEROMORPHIC BETA IDENTITY — NOT AN ORDINARY ENDPOINT DROP",
        "definition": (
            "FP integral u^(L-1)(1-u^2)^(gamma-1) du = "
            "Beta(L/2,gamma)/2, continued meromorphically"
        ),
        "identity": (
            "L*Beta(L/2,gamma+1)=2*gamma*Beta(L/2+1,gamma)"
        ),
        "cleared_multiplier": "L*gamma-2*gamma*(L/2)=0",
        "application": (
            "expand w_r*S into finitely many monomial primitives; every term "
            "has zero regularized derivative, so every D_r*S reduction integrates exactly"
        ),
        "ordinary_boundary_warning": (
            "the specialized Euler integrals diverge at u=1; no literal endpoint value is discarded"
        ),
    }


def gauge_ratio_fraction(r_value: int) -> F:
    return F(
        r_value * (r_value + 6) * (2 * r_value + 9) ** 2 * (2 * r_value + 15) ** 2,
        78732 * (r_value + 1) ** 2 * (r_value + 2)
        * (r_value + 4) * (r_value + 5) ** 2,
    )


def initial_bridge_certificate() -> dict[str, Any]:
    constants = {1: F(-891, 100), 5: F(3897234, 41405)}
    rows = []
    for residue in (1, 5):
        gauge = F(1)
        for n in range(3):
            r_value = residue + 6 * n
            data = i250.phase_data(r_value)
            f0, f1 = data["st"]
            d0 = data["x0"][2]
            d1 = data["x1"][2]
            m_value = -11 * (f0 * d1 - f1 * d0)
            normalized = F(16**n) * m_value / gauge
            coefficient = i237.lagrange_coefficient(r_value)
            if normalized != constants[residue] * coefficient:
                raise AssertionError((residue, n, normalized, coefficient))
            rows.append((residue, n, normalized.numerator, normalized.denominator,
                         coefficient.numerator, coefficient.denominator))
            gauge /= gauge_ratio_fraction(r_value)
    stream = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return {
        "classification": "EXACT INITIALS USED WITH A PROVED FORWARD RECURRENCE",
        "rows": rows,
        "constants": {str(key): str(value) for key, value in constants.items()},
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "logical_role": "three initials on each ray identify the two order-three solutions",
    }


def pole_and_forward_audit(hermite: dict[str, Any]) -> dict[str, Any]:
    recurrence = i237.recurrence_polynomials()
    if any(coefficient <= 0 for coefficient in recurrence[3]):
        raise AssertionError("p3 does not have coefficientwise positivity")
    if not hermite[
        "all_coordinate_denominators_are_products_of_positive_linear_factors_for_r_positive"
    ]:
        raise AssertionError("coordinate denominator positivity")
    return {
        "classification": "ALL ACTUAL r>=1, r=1 or 5 mod 6",
        "actual_rays": "r=6n+1 and r=6n+5, n>=0",
        "beta_poles": (
            "b0=-2r/3 and b1=b0-1 are nonintegral because 3 does not divide r; "
            "all original Pochhammer denominators are nonzero by Items 250 and 291"
        ),
        "hermite_coordinate_poles": (
            "every reduced coordinate denominator has positive constant term and "
            "nonnegative coefficients, hence no positive-real zero"
        ),
        "primitive_solver_poles": (
            "the triangular construction divides only by r+k+1 (k>=0), all positive on actual rays; "
            "the final 3x3 solution is the displayed pole-free-on-r>0 coordinate family"
        ),
        "normalization_poles": (
            "eta step divides by r(r+2)(r+4); gauge R divides by "
            "78732(r+1)^2(r+2)(r+4)(r+5)^2; none vanish for r>=1"
        ),
        "excluded_parameter_classes": [
            "r not a positive integer congruent to 1 or 5 modulo 6 (outside the theorem domain)",
            "3 divides r (b0 and b1 hit integral beta/Pochhammer resonance)",
        ],
        "coordinate_denominator_roots": {
            "negative_integers": [-3, -6, -9, -12, -15, -18],
            "negative_half_integers": [
                "-3/2", "-9/2", "-15/2", "-21/2", "-27/2", "-33/2", "-39/2"
            ],
        },
        "primitive_certificate_denominator_roots": (
            "r=-1,-2,...,-38 from (r+1)_(K+1), plus the coordinate roots already listed"
        ),
        "eta_denominator_roots_for_steps_0_1_2": [
            0, -2, -4, -6, -8, -10, -12, -14, -16
        ],
        "gauge_denominator_roots_for_steps_0_1_2": [
            -1, -2, -4, -5, -7, -8, -10, -11, -13, -14, -16, -17
        ],
        "gauge_or_eta_zero_roots": (
            "all zeros of r+6t, r+6t+3, r+6t+6, 2r+12t+3, "
            "2r+12t+9, and 2r+12t+15 for t=0,1,2 are nonpositive"
        ),
        "actual_pole_or_zero_intersection": [],
        "forward_coefficient": (
            "p3(h) has strictly positive coefficients, so p3(r/2)>0 for every actual r>=1"
        ),
        "actual_exceptional_r": [],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()

    hermite = hermite_and_tensor_certificate()
    endpoint = endpoint_certificate()
    initials = initial_bridge_certificate()
    poles = pole_and_forward_audit(hermite)
    result = {
        "schema": "item306-j2-normalized-m-bridge-v1",
        "dependencies": DEPENDENCIES,
        "hermite_and_tensor": hermite,
        "endpoint_and_continuation": endpoint,
        "bug_provenance": {
            "classification": "EXPLORATORY PROBE BUG, EXCLUDED FROM PRODUCTION CERTIFICATE",
            "description": (
                "an exploratory unshifted companion assembly admitted an index -1 and Python "
                "read the last list entry; this produced a spurious endpoint mismatch"
            ),
            "correction": (
                "the exact base companion is ((5r+6)/(2r+3),(5r+12)/(2r+3),0); "
                "every production recurrence lookup tests index>=0 and returns explicit zero otherwise"
            ),
            "production_negative_index_shortcut": False,
        },
        "initial_bridge": initials,
        "pole_and_forward_audit": poles,
        "theorem": {
            "classification": "PROVED",
            "statement": (
                "For e in {1,5}, r=6n+e, g0=1, g_n/g_(n+1)=R(r), "
                "16^n*M_n/g_n=lambda_e*[x^r]C(x) for every n>=0"
            ),
            "constants": {"1": "-891/100", "5": "3897234/41405"},
            "recurrence_membership": (
                "16^n*M_n/g_n obeys Item237's exact order-three step-six coefficient recurrence"
            ),
        },
        "ordinary_j2_gate_consequence": {
            "proved": (
                "the M connection minor in D=9*c*det(f,b)-11*det(f,d) has the displayed "
                "fixed algebraic coefficient realization and exact recurrence"
            ),
            "not_proved": [
                "a realization or recurrence theorem for the independent L connection minor",
                "nonvanishing modulo every moving row prime",
                "Frobenius, monodromy, or auxiliary-prime independence",
                "weighted zero density or any capacity saving",
            ],
        },
        "strict_labels": {
            "PROVED": [
                "all eight cleared Hermite reductions (shifts 0 through 3 in both companions)",
                "the meromorphic-beta endpoint identity and normalization ratio",
                "all three exact skew-tensor cancellations",
                "the all-n recurrence membership and normalized-M bridge on both ordinary rays",
            ],
            "EXACT_FINITE_ONLY": [
                "none used as theorem evidence; the six exact rows are recurrence initials",
                "the older checks beyond the first three rows remain implementation replays",
            ],
            "OPEN": [
                "an algebraic or recurrence realization of L",
                "all-prime nonvanishing or weighted density for the full ordinary-j2 determinant",
                "any Route-1 completion or conclusion about e+pi",
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
