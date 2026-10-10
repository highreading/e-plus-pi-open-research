#!/usr/bin/env python3
"""Deterministic certificate for Item 237's algebraic phase residual."""

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
RESULT_NAME = "item237_j1_algebraic_residual_certificate.json"
F = Fraction


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, filename: str):
    path = resolve(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM222_PATH = resolve("item222_j1_phase_resultant_certificate.py")
ITEM229_PATH = resolve("item229_j1_fixed_h_theta_certificate.py")
ITEM231_PATH = resolve("item231_j1_second_phase_coefficient_certificate.py")
ITEM236_PATH = resolve("item236_j1_phase_cokernel_certificate.py")

item222 = load("item237_item222", ITEM222_PATH.name)
item229 = load("item237_item229", ITEM229_PATH.name)
item231 = load("item237_item231", ITEM231_PATH.name)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Small exact polynomial and series layer.  Coefficients are low-to-high.


def trim(poly):
    answer = list(poly)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def add(left, right):
    answer = [F(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    return trim(answer)


def scale(poly, scalar):
    return trim([scalar * value for value in poly])


def multiply(left, right):
    answer = [F(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return trim(answer)


def power(poly, exponent):
    answer = [F(1)]
    factor = list(poly)
    while exponent:
        if exponent & 1:
            answer = multiply(answer, factor)
        exponent >>= 1
        if exponent:
            factor = multiply(factor, factor)
    return answer


def derivative(poly):
    return [F(index) * poly[index] for index in range(1, len(poly))] or [F(0)]


def truncated_multiply(left, right, maximum):
    answer = [F(0)] * (maximum + 1)
    for left_index, left_value in enumerate(left[: maximum + 1]):
        for right_index, right_value in enumerate(
            right[: maximum + 1 - left_index]
        ):
            answer[left_index + right_index] += left_value * right_value
    return answer


def inverse_series(poly, maximum):
    answer = [F(1, poly[0])]
    for degree in range(1, maximum + 1):
        answer.append(
            -sum(
                poly[index] * answer[degree - index]
                for index in range(1, min(degree, len(poly) - 1) + 1)
            )
            / poly[0]
        )
    return answer


def integer_power_series(poly, exponent, maximum):
    answer = [F(1)] + [F(0)] * maximum
    factor = list(poly) + [F(0)] * (maximum + 1 - len(poly))
    while exponent:
        if exponent & 1:
            answer = truncated_multiply(answer, factor, maximum)
        exponent >>= 1
        if exponent:
            factor = truncated_multiply(factor, factor, maximum)
    return answer


def q_power_series(exponent, maximum):
    """(1+y+y^2/2)^exponent, by its first-order differential equation."""
    answer = [F(1)]
    for degree in range(maximum):
        previous = answer[degree]
        previous_two = answer[degree - 1] if degree else F(0)
        answer.append(
            (
                (exponent - degree) * previous
                + (exponent - F(degree - 1, 2)) * previous_two
            )
            / (degree + 1)
        )
    return answer


Q = [F(1), F(1), F(1, 2)]
A = [F(20, 3), F(14, 3), F(4, 3)]
B = [F(2), F(-5), F(-3)]
D = [F(6), F(14), F(7), F(2)]
N = [F(432), F(2064), F(4440), F(5376), F(4044), F(1860), F(486), F(48)]


def verify_rational_closed_form() -> dict[str, Any]:
    """Check C=U_B+(x/2)dU_A/dx=N/D^3 exactly in Q[y]."""
    q_squared = power(Q, 2)
    u_a_numerator = scale(multiply(q_squared, A), F(6))
    first = scale(multiply(multiply(q_squared, B), power(D, 2)), F(6))
    derivative_numerator = add(
        multiply(derivative(u_a_numerator), D),
        scale(multiply(u_a_numerator, derivative(D)), F(-1)),
    )
    second = scale(
        multiply(multiply([F(0), F(1), F(1)], Q), derivative_numerator),
        F(3),
    )
    derived_numerator = add(first, second)
    if derived_numerator != N:
        raise AssertionError((derived_numerator, N))
    return {
        "classification": "SYMBOLIC_EXACT",
        "change_of_variable": "x=y(1+y)/Q(y)^(2/3)",
        "Q_low_to_high": [str(value) for value in Q],
        "D_low_to_high": [str(value) for value in D],
        "N_low_to_high": [str(value) for value in N],
        "identity": "C(x(y))=N(y)/D(y)^3",
        "derived_numerator_matches": True,
    }


def lagrange_coefficient(index):
    """[x^index]N(y(x))/D(y(x))^3, exactly by Lagrange inversion."""
    if index == 0:
        return F(2)
    maximum = index - 1
    n_derivative = derivative(N)
    d_derivative = derivative(D)
    c_derivative_numerator = add(
        multiply(n_derivative, D),
        scale(multiply(N, d_derivative), F(-3)),
    )
    d_inverse = inverse_series(D, maximum)
    d_minus_four = integer_power_series(d_inverse, 4, maximum)
    q_factor = q_power_series(F(2 * index, 3), maximum)
    one_plus = [F(1)]
    for degree in range(1, maximum + 1):
        one_plus.append(one_plus[-1] * (-index - degree + 1) / degree)
    product = truncated_multiply(
        c_derivative_numerator, d_minus_four, maximum
    )
    product = truncated_multiply(product, q_factor, maximum)
    product = truncated_multiply(product, one_plus, maximum)
    return product[maximum] / index


def coefficient_replay(h_max):
    rows = []
    for h_value in range(1, h_max + 1):
        algebraic = lagrange_coefficient(2 * h_value)
        original = item229.phase_c(h_value)
        if algebraic != original:
            raise AssertionError((h_value, algebraic, original))
        rows.append(
            (h_value, algebraic.numerator, algebraic.denominator)
        )
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_REPLAY_OF_SYMBOLIC_CHANGE_OF_VARIABLE",
        "h_max": h_max,
        "rows": len(rows),
        "identity": "c_h^*=[x^(2h)]C(x)",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


# ---------------------------------------------------------------------------
# Explicit resultant of the rational parametrization.


def int_trim(poly):
    answer = list(poly)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def int_add(left, right):
    answer = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    return int_trim(answer)


def int_scale(poly, scalar):
    return int_trim([scalar * value for value in poly])


def int_multiply(left, right):
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return int_trim(answer)


def int_power(poly, exponent):
    answer = [1]
    factor = poly
    while exponent:
        if exponent & 1:
            answer = int_multiply(answer, factor)
        exponent >>= 1
        if exponent:
            factor = int_multiply(factor, factor)
    return answer


def sylvester_resultant(left, right):
    left = int_trim(left)
    right = int_trim(right)
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    size = left_degree + right_degree
    matrix = []
    for shift in range(right_degree):
        matrix.append(
            [0] * shift + list(reversed(left))
            + [0] * (size - shift - len(left))
        )
    for shift in range(left_degree):
        matrix.append(
            [0] * shift + list(reversed(right))
            + [0] * (size - shift - len(right))
        )
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        selected = next(
            (row for row in range(pivot_index, size) if matrix[row][pivot_index]),
            None,
        )
        if selected is None:
            return 0
        if selected != pivot_index:
            matrix[pivot_index], matrix[selected] = matrix[selected], matrix[pivot_index]
            sign = -sign
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column]
                )
                if numerator % previous:
                    raise ArithmeticError((pivot_index, numerator, previous))
                matrix[row][column] = numerator // previous
        previous = pivot
        for row in range(pivot_index + 1, size):
            matrix[row][pivot_index] = 0
    return sign * matrix[-1][-1]


def binomial_polynomial(degree):
    polynomial = [F(1)]
    for root in range(degree):
        polynomial = add(
            [F(0)] + polynomial,
            scale(polynomial, -root),
        )
    return scale(polynomial, F(1, math.factorial(degree)))


def interpolate_consecutive(values):
    differences = [F(value) for value in values]
    newton = []
    while differences:
        newton.append(differences[0])
        differences = [
            differences[index + 1] - differences[index]
            for index in range(len(differences) - 1)
        ]
    answer = [F(0)]
    for degree, coefficient in enumerate(newton):
        answer = add(answer, scale(binomial_polynomial(degree), coefficient))
    return answer


def interpolate_points(points):
    answer = [F(0)]
    for point_index, (abscissa, ordinate) in enumerate(points):
        basis = [F(1)]
        denominator = 1
        for other_index, (other_abscissa, _) in enumerate(points):
            if other_index == point_index:
                continue
            basis = multiply(basis, [F(-other_abscissa), F(1)])
            denominator *= abscissa - other_abscissa
        answer = add(answer, scale(basis, F(ordinate, denominator)))
    return answer


R_INTEGER = [2, 2, 1]
D_INTEGER = [6, 14, 7, 2]
N_INTEGER = [432, 2064, 4440, 5376, 4044, 1860, 486, 48]


def specialized_polynomials(u_value, v_value):
    first = int_scale(int_power(R_INTEGER, 2), u_value)
    second = [0, 0, 0] + int_scale(int_power([1, 1], 3), -4)
    curve = int_add(first, second)
    value = int_add(
        int_scale(int_power(D_INTEGER, 3), v_value),
        int_scale(N_INTEGER, -1),
    )
    return curve, value


def resultant_value(u_value, v_value):
    return sylvester_resultant(*specialized_polynomials(u_value, v_value))


EXPECTED_RESULTANT = [
    [0, 0, -24794911296], [0, 2, 18596183472], [0, 4, -4649045868],
    [0, 6, 387420489], [1, 0, -320531198976], [1, 1, 10203667200],
    [1, 2, 142774813296], [1, 3, 18706723200], [1, 4, -956593800],
    [1, 6, 27679041603], [2, 0, -1035825905664], [2, 1, 84728229120],
    [2, 2, -163471251600], [2, 3, 365291285760], [2, 4, 6273838152],
    [2, 6, 659343436911], [3, 0, 9555148800], [3, 1, -229233991680],
    [3, 2, 1366692726672], [3, 3, 2240051371200], [3, 4, -5399990896680],
    [3, 6, 5240894368977], [4, 1, 1751777280], [4, 2, -29242114560],
    [4, 3, 69725525760], [4, 4, -384747712560], [4, 6, 98288005284],
    [5, 2, 80289792], [5, 3, -440501760], [5, 4, 5360898816],
    [5, 6, 7844978952], [6, 3, -4423680], [6, 4, 64955520],
    [6, 6, 91399104], [7, 4, -405504], [7, 6, 3613248],
    [8, 6, 20736], [9, 6, 512],
]


def resultant_certificate():
    u_degree = 9
    v_degree = 6
    v_values = list(range(1, v_degree + 2))
    grid = [
        [resultant_value(u_value, v_value) for v_value in v_values]
        for u_value in range(u_degree + 1)
    ]
    in_u = [
        interpolate_consecutive(
            [grid[u_value][v_index] for u_value in range(u_degree + 1)]
        )
        for v_index in range(v_degree + 1)
    ]
    coefficients = {}
    for u_power in range(u_degree + 1):
        values = [
            in_u[v_index][u_power] if u_power < len(in_u[v_index]) else F(0)
            for v_index in range(v_degree + 1)
        ]
        in_v = interpolate_points(list(zip(v_values, values)))
        for v_power, value in enumerate(in_v):
            if value:
                if value.denominator != 1:
                    raise ArithmeticError(value)
                coefficients[(u_power, v_power)] = value.numerator
    content = 0
    for value in coefficients.values():
        content = math.gcd(content, abs(value))
    primitive = {
        index: value // content for index, value in coefficients.items()
    }
    if primitive[max(primitive)] < 0:
        primitive = {index: -value for index, value in primitive.items()}
    encoded = [
        [u_power, v_power, value]
        for (u_power, v_power), value in sorted(primitive.items())
    ]
    if encoded != EXPECTED_RESULTANT:
        raise AssertionError("resultant coefficient mismatch")
    test_u, test_v = 13, 11
    predicted_raw = sum(
        content * value * test_u**u_power * test_v**v_power
        for u_power, v_power, value in encoded
    )
    actual = resultant_value(test_u, test_v)
    if predicted_raw != actual:
        raise AssertionError((predicted_raw, actual))
    return {
        "classification": "SYMBOLIC_EXACT",
        "definition": (
            "P(u,v)=2^-27 Res_y(u(y^2+2y+2)^2-4y^3(1+y)^3,"
            "vD(y)^3-N(y))"
        ),
        "raw_content": content,
        "u_degree": u_degree,
        "v_degree": v_degree,
        "nonzero_terms": len(encoded),
        "primitive_coefficients_u_v_value": encoded,
        "off_grid_check": [test_u, test_v, actual],
        "conclusion": "P(x^3,C(x))=0 on the y(0)=0 branch",
    }


# ---------------------------------------------------------------------------
# Exact differential-operator certificate for the step-three recurrence.


RECURRENCE_FACTORS = [
    (
        F(-1, 76742461255680),
        [(-3, 1), (-3, 2), (-5, 1), (-6, 1), (-9, 2), (-9, 4),
         (-15, 4), (-21, 4), (-27, 4), (-33, 4), (-39, 4)],
        [6414233265, 5112300033, 1603835736, 247582992, 18819760, 564080],
    ),
    (
        F(-1, 710578344960),
        [(-2, 1), (-6, 1), (-9, 2), (-21, 4), (-27, 4), (-33, 4), (-39, 4)],
        [402660529612416, 1002494068911927, 1039962332216826,
         596405304955566, 209971952382012, 47325249956016,
         6857541598288, 618060903584, 31525303040, 694946560],
    ),
    (
        F(-1, 105270865920),
        [(-2, 1), (-4, 1), (-5, 1), (-7, 2), (-11, 2), (-33, 4), (-39, 4)],
        [1090010738003273316, 2470146696629963712, 2354075629101513405,
         1243406090403290781, 403775302745693160, 84106392952710132,
         11294493697293648, 946720367971824, 45093571774720, 932385882560],
    ),
    (
        F(1, 18050560),
        [(-2, 1), (-4, 1), (-5, 1), (-7, 1), (-8, 1), (-7, 2),
         (-9, 1), (-11, 2), (-13, 2), (-15, 2), (-17, 2)],
        [214443126, 369944721, 239554248, 72513072, 10358560, 564080],
    ),
]


def recurrence_polynomials():
    answer = []
    for scalar, roots, core in RECURRENCE_FACTORS:
        polynomial = [F(value) * scalar for value in core]
        for numerator, denominator in roots:
            polynomial = multiply(
                polynomial, [F(-numerator), F(denominator)]
            )
        if len(polynomial) != 17:
            raise AssertionError(len(polynomial))
        answer.append(polynomial)
    return answer


J_NUMERATOR = scale(
    multiply([F(0), F(1), F(1)], [F(2), F(2), F(1)]), F(3)
)


def shifted_theta(numerator, denominator_exponent, shift):
    logarithmic_numerator = add(
        multiply(derivative(numerator), D),
        scale(
            multiply(numerator, derivative(D)),
            -denominator_exponent,
        ),
    )
    theta_numerator = multiply(J_NUMERATOR, logarithmic_numerator)
    shifted = add(
        theta_numerator,
        scale(multiply(numerator, power(D, 2)), -shift),
    )
    return scale(shifted, F(1, 2)), denominator_exponent + 2


def operator_certificate():
    recurrence = recurrence_polynomials()
    common_d_exponent = 35
    common_r_exponent = 12
    r_poly = [F(2), F(2), F(1)]
    total = [F(0)]
    summaries = []
    for recurrence_shift in range(4):
        iterates = [(N, 3)]
        for _ in range(16):
            iterates.append(
                shifted_theta(*iterates[-1], shift=6 * recurrence_shift)
            )
        block = [F(0)]
        for degree, coefficient in enumerate(recurrence[recurrence_shift]):
            numerator, d_exponent = iterates[degree]
            lifted = multiply(
                numerator, power(D, common_d_exponent - d_exponent)
            )
            block = add(block, scale(lifted, coefficient))
        u_exponent = 6 - 2 * recurrence_shift
        u_numerator = scale(
            multiply(
                [F(0)] * (3 * u_exponent) + [F(1)],
                power([F(1), F(1)], 3 * u_exponent),
            ),
            4**u_exponent,
        )
        lifted_block = multiply(block, u_numerator)
        lifted_block = multiply(
            lifted_block,
            power(r_poly, common_r_exponent - 2 * u_exponent),
        )
        total = add(total, lifted_block)
        summaries.append(
            {
                "shift": recurrence_shift,
                "numerator_degree": len(block) - 1,
                "lifted_degree": len(lifted_block) - 1,
            }
        )
    if total != [F(0)]:
        raise AssertionError((len(total) - 1, total[:4], total[-4:]))
    encoded = []
    for scalar, roots, core in RECURRENCE_FACTORS:
        encoded.append(
            {
                "scalar": str(scalar),
                "linear_factor_roots_numerator_denominator": [list(pair) for pair in roots],
                "remaining_core_low_to_high": core,
            }
        )
    return {
        "classification": "SYMBOLIC_EXACT",
        "recurrence": "sum_(k=0)^3 p_k(h)c_(h+3k)^*=0",
        "coefficient_degrees": [16, 16, 16, 16],
        "factored_coefficients": encoded,
        "operator": (
            "sum_(k=0)^3 x^(18-6k) p_k((theta-6k)/2), theta=x*d/dx"
        ),
        "parameter_theta": (
            "theta=3y(1+y)(y^2+2y+2)D(y)^(-1)*d/dy"
        ),
        "common_denominator": "D(y)^35*(y^2+2y+2)^12",
        "cleared_numerator_zero": True,
        "block_summaries": summaries,
    }


# ---------------------------------------------------------------------------
# Finite c/E evidence, exact target gauge, and K/E scoped obstruction.


def rho_fraction(h_value):
    return item229.rho(h_value)


def fraction_mod(value, prime):
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def polynomial_mod(coefficients, value, prime):
    answer = 0
    for coefficient in reversed(coefficients):
        answer = (
            answer * value + fraction_mod(coefficient, prime)
        ) % prime
    return answer


def phase_factorization_finite(h_max):
    rows = []
    for h_value in range(1, h_max + 1):
        if h_value % 3 == 0:
            continue
        eliminant, _ = item222.phase_fraction_and_integer(h_value)
        residual = item229.phase_c(h_value)
        ratio = item229.conjectural_ratio(h_value)
        if residual != ratio * eliminant:
            raise AssertionError((h_value, residual, ratio, eliminant))
        rows.append(
            (
                h_value,
                residual.numerator,
                residual.denominator,
                eliminant.numerator,
                eliminant.denominator,
                ratio.numerator,
                ratio.denominator,
            )
        )
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_ONLY",
        "h_max": h_max,
        "admissible_rows": len(rows),
        "observed_identity": "c_h^*=R_h E_h^*",
        "initial_ratios": {"R_1": "-49/18", "R_2": "4235/1944"},
        "step_ratio": "R_(h+3)/R_h=rho(h)",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def gauge_recurrence_finite(h_max, primes):
    recurrence = recurrence_polynomials()
    prime_results = []
    for prime in primes:
        values = {
            h_value: item222.phase_mod(h_value, prime)[0]
            for h_value in range(1, h_max + 10)
            if h_value % 3
        }
        rows = []
        for h_value in range(1, h_max + 1):
            if h_value % 3 == 0:
                continue
            gauge = F(1)
            total = 0
            terms = []
            for shift in range(4):
                if shift:
                    gauge *= rho_fraction(h_value + 3 * (shift - 1))
                coefficient = polynomial_mod(
                    recurrence[shift], h_value, prime
                )
                coefficient = coefficient * fraction_mod(gauge, prime) % prime
                term = coefficient * values[h_value + 3 * shift] % prime
                terms.append(term)
                total = (total + term) % prime
            if total:
                raise AssertionError((prime, h_value, terms, total))
            rows.append((h_value, *terms))
        stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
        prime_results.append(
            {
                "prime": prime,
                "h_max": h_max,
                "rows": len(rows),
                "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
            }
        )
    return {
        "classification": "EXACT_FINITE_ONLY",
        "tested_operator": (
            "sum_(k=0)^3 p_k(h)(product_(j=0)^(k-1)rho(h+3j))E_(h+3k)^*=0"
        ),
        "prime_results": prime_results,
        "logical_status": (
            "finite modular agreement does not supply a symbolic telescoping certificate"
        ),
    }


def rank_mod(matrix, prime):
    work = [[value % prime for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    rank = 0
    for column in range(columns):
        selected = next(
            (row for row in range(rank, rows) if work[row][column]), None
        )
        if selected is None:
            continue
        work[rank], work[selected] = work[selected], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for row in range(rows):
            if row != rank and work[row][column]:
                multiplier = work[row][column]
                work[row] = [
                    (left - multiplier * right) % prime
                    for left, right in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def localized_k_obstruction(h_max=40, degree=5, prime=1_000_000_007):
    values = {}
    for h_value in range(1, h_max + 1):
        if h_value % 3 == 0:
            continue
        eliminant, _ = item222.phase_fraction_and_integer(h_value)
        boundary = item231.phase_boundary_data(h_value)
        values[h_value] = {
            "E": eliminant,
            "K": boundary["natural_eliminant"],
            "c": boundary["low_c"],
        }
    rank_results = []
    for residue in (1, 2):
        h_values = sorted(h for h in values if h % 3 == residue)
        matrix = []
        for index, (left_h, right_h) in enumerate(zip(h_values, h_values[1:])):
            left = values[left_h]
            right = values[right_h]
            cross_next = fraction_mod(right["K"] * left["E"], prime)
            cross_current = fraction_mod(left["K"] * right["E"], prime)
            matrix.append(
                [
                    pow(index, power_value, prime) * cross_next % prime
                    for power_value in range(degree + 1)
                ]
                + [
                    pow(index, power_value, prime) * cross_current % prime
                    for power_value in range(degree + 1)
                ]
            )
        rank = rank_mod(matrix, prime)
        columns = 2 * (degree + 1)
        if rank != columns:
            raise AssertionError((residue, rank, columns))
        rank_results.append(
            {
                "residue": residue,
                "rows": len(matrix),
                "columns": columns,
                "rank": rank,
            }
        )
    gcd_rows = []
    violations = []
    for h_value, row in sorted(values.items()):
        common = math.gcd(abs(row["E"].numerator), abs(row["K"].numerator))
        quotient = abs(row["E"].numerator) // common
        factors = item231.prime_factorization(quotient)
        if any(factor > 4 * h_value + 3 for factor, _ in factors):
            violations.append((h_value, quotient, factors))
        gcd_rows.append((h_value, quotient, factors))
    stream = json.dumps(gcd_rows, separators=(",", ":")).encode("ascii")
    return {
        "proved_scoped_no_go": {
            "classification": "SYMBOLIC_CONSEQUENCE_OF_EXACT_FULL_RANK_CERTIFICATE",
            "ansatz": (
                "A(n)K_(h+3)/E_(h+3)+B(n)K_h/E_h=0, "
                "h=3n+r, deg(A),deg(B)<=5"
            ),
            "prime": prime,
            "denominator_audit": "every sampled rational denominator is nonzero modulo the prime",
            "rank_results": rank_results,
            "logic": (
                "a rational identity gives a primitive integer null vector; "
                "one full-column-rank prime reduction rules it out"
            ),
        },
        "finite_gcd_pattern": {
            "classification": "EXACT_FINITE_ONLY",
            "h_max": h_max,
            "rows": len(gcd_rows),
            "violations_of_remaining_prime_factors_le_4h_plus_3": violations,
            "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
            "logical_status": "no all-h gcd or unit-localized factorization is inferred",
        },
    }


def certificate(coefficient_h_max, phase_h_max, gauge_h_max):
    return {
        "item": 237,
        "schema": "item237-j1-algebraic-residual-v1",
        "dependencies": {
            ITEM222_PATH.name: sha256(ITEM222_PATH),
            ITEM229_PATH.name: sha256(ITEM229_PATH),
            ITEM231_PATH.name: sha256(ITEM231_PATH),
            ITEM236_PATH.name: sha256(ITEM236_PATH),
        },
        "algebraic_closed_form": verify_rational_closed_form(),
        "coefficient_replay": coefficient_replay(coefficient_h_max),
        "algebraic_resultant": resultant_certificate(),
        "all_h_recurrence": operator_certificate(),
        "phase_factorization_evidence": phase_factorization_finite(phase_h_max),
        "gauged_E_recurrence_evidence": gauge_recurrence_finite(
            gauge_h_max, [1_000_000_007, 1_009_999_999]
        ),
        "endpoint_scalar_comparison": localized_k_obstruction(),
        "missing_certificate_barrier": {
            "classification": "OPEN",
            "exact_reduction": (
                "E_h^* is a bilinear double sum of proper hypergeometric beta-period "
                "terms; c=R E would follow from the displayed gauged recurrence plus "
                "three initial values in each nonzero residue class"
            ),
            "missing_input": (
                "a symbolic bivariate WZ/Hermite certificate for the gauged E recurrence, "
                "or an equivalent all-h hypergeometric transformation"
            ),
            "warning": (
                "finite recurrence agreement and finite gcd patterns are not recurrence "
                "or nonvanishing theorems"
            ),
        },
        "rate_ledger": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "reason": (
                "the algebraic residual recurrence does not exclude its simultaneous "
                "zero with E_h^* or the remaining endpoint scalar on actual row primes"
            ),
        },
        "status_ledger": {
            "PROVED": [
                "the fixed algebraic coefficient formula c_h^*=[x^(2h)]C(x)",
                "the explicit degree-(9,6) primitive resultant P(x^3,C)=0",
                "the all-h order-3 step-3 degree-16 recurrence for c_h^*",
                "the degree<=5 first-order rational K/E ansatz no-go",
            ],
            "EXACT_FINITE_ONLY": [
                f"c_h^*=R_hE_h^* through admissible h<={phase_h_max}",
                f"the gauged E recurrence modulo two primes through h<={gauge_h_max}",
                "the K/E gcd pattern through h<=40",
            ],
            "OPEN": [
                "the all-h identity c_h^*=R_hE_h^*",
                "a symbolic certificate for the gauged E recurrence",
                "a unit-localized all-h K/E factorization or gcd theorem",
                "all-prime exclusion, a radical/log-mass saving, or a positive Route-1 rate",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coefficient-h-max", type=int, default=40)
    parser.add_argument("--phase-h-max", type=int, default=80)
    parser.add_argument("--gauge-h-max", type=int, default=220)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.coefficient_h_max < 12 or args.phase_h_max < 40 or args.gauge_h_max < 80:
        raise ValueError("replay bounds are below the canonical minimum")
    result = certificate(
        args.coefficient_h_max, args.phase_h_max, args.gauge_h_max
    )
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "algebraic_resultant_terms": result["algebraic_resultant"]["nonzero_terms"],
                "operator_zero": result["all_h_recurrence"]["cleared_numerator_zero"],
                "phase_status": result["phase_factorization_evidence"]["classification"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
