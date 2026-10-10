#!/usr/bin/env python3
"""Exact certificate for the (1-x)^2 positive common-kernel cone.

The companion proof note is

    sources/factor_endpoint_positive_cone_lattice_and_rays.md

All algebraic assertions use Python integers and fractions.  The only
decimal output consists of outward-rounded intervals obtained from exact
rational bounds for e and pi.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


# Each tuple is (primitive coefficient q, positive integer p, degree m,
# support of a nonnegative Bernstein vertex).  The desired ray is (q,-p).
RAYS = [
    (7, 41, 7, (2, 3, 6)),
    (157, 920, 15, (6, 8, 11)),
    (6851, 40146, 20, (7, 10, 13)),
    (27247, 159664, 24, (9, 11, 14)),
    (91939, 538751, 26, (9, 12, 15)),
    (405201, 2374427, 30, (11, 13, 16)),
    (4521903, 26497784, 35, (15, 18, 20)),
    (56602103, 331681219, 41, (17, 20, 22)),
    (180222349, 1056080344, 43, (18, 20, 23)),
    (484064944, 2836559813, 45, (18, 21, 24)),
    (2847787561, 16687677659, 49, (20, 22, 25)),
    (31933348361, 187125413187, 55, (22, 24, 27)),
    (557409702537, 3266350891943, 61, (24, 26, 29)),
    (1246188493618, 7302508153575, 63, (27, 30, 32)),
]


H_STAR = [3, 8, 3]
H_A = [-17, 21, 161, 95, 167, 74, -11, -2]
H_B = [7, -26, 2, -26, -5, 0, 0, 0]
H_P = [11, -85, 78, -13, 66, 71, -1, -1]


# This is a genuine zero-output direction.  Its degree is larger than all
# the finite cone witnesses.  Since its leading H coefficient is 1, the
# leading coefficient of (1-x)^2 H is also 1.
H_ZERO_64 = [
    -2, 16, -12, -15, 3, -1, -16, 0, 11, -19, 24, 14, -1,
    -16, -16, -15, 3, -14, 5, -14, 28, -15, 7, -40, 10, -14,
    13, 14, 14, 14, 14, 14, -19, 15, -19, 17, -19, 19, -19,
    21, 22, 22, -21, 23, -21, 25, -21, 27, -21, 29, 30, 30,
    -23, 85, 31, 198, 27, 256, 20, 256, 12, 194, 5, 66, 1,
]


def fraction_string(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def vector_hash(values: list[int]) -> str:
    payload = ",".join(str(value) for value in values).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def derangement(n: int) -> int:
    if n == 0:
        return 1
    previous, current = 1, 0
    for k in range(2, n + 1):
        previous, current = current, (k - 1) * (previous + current)
    return current


def a_monomial(n: int) -> int:
    """A(x^n), for A(F)=sum_j (-1)^j F^(j)(1)."""
    return (-1) ** n * derangement(n)


def target_from_h(h: list[int]) -> int:
    """Real value of (1-i)^2 H(i), assuming its imaginary part vanishes."""
    return sum(
        (2 if k % 4 == 1 else -2 if k % 4 == 3 else 0) * value
        for k, value in enumerate(h)
    )


def real_h_at_i(h: list[int]) -> int:
    return sum(
        (1 if k % 4 == 0 else -1 if k % 4 == 2 else 0) * value
        for k, value in enumerate(h)
    )


def f_from_h(h: list[int]) -> list[int]:
    f = [0] * (len(h) + 2)
    for k, value in enumerate(h):
        f[k] += value
        f[k + 1] -= 2 * value
        f[k + 2] += value
    return f


def quotient_by_one_plus_x2(
    f: list[int], target: int
) -> tuple[list[int], list[int]]:
    """Return quotient and two-term remainder of (F-target)/(1+x^2)."""
    remainder = f[:]
    remainder[0] -= target
    quotient = [0] * (len(remainder) - 2)
    for degree in range(len(remainder) - 1, 1, -1):
        quotient[degree - 2] = remainder[degree]
        remainder[degree - 2] -= remainder[degree]
        remainder[degree] = 0
    return quotient, remainder[:2]


def output_data(h: list[int], require_common: bool = True) -> dict[str, object]:
    f = f_from_h(h)
    target = target_from_h(h)
    endpoint_real_constraint = real_h_at_i(h)
    a_value = sum(coefficient * a_monomial(k) for k, coefficient in enumerate(f))
    b_value = sum(
        (-1) ** k * math.factorial(k) * coefficient
        for k, coefficient in enumerate(f)
    )
    quotient, remainder = quotient_by_one_plus_x2(f, target)
    correction = sum(
        (Fraction(4 * coefficient, k + 1) for k, coefficient in enumerate(quotient)),
        Fraction(0),
    )
    if require_common:
        assert endpoint_real_constraint == 0
        assert a_value == target
        assert remainder == [0, 0]

    M = correction.numerator
    D = correction.denominator
    N = M - b_value * D
    cross_content = math.gcd(abs(target * D), abs(N))
    if cross_content:
        primitive_pair = [target * D // cross_content, N // cross_content]
    else:
        primitive_pair = [0, 0]
    return {
        "target": target,
        "A": a_value,
        "B": b_value,
        "correction": correction,
        "constant": correction - b_value,
        "M": M,
        "D": D,
        "N": N,
        "cross_content": cross_content,
        "primitive_pair": primitive_pair,
        "f": f,
        "quotient": quotient,
        "endpoint_real_constraint": endpoint_real_constraint,
        "remainder": remainder,
    }


def formal_column_data(h: list[int]) -> tuple[tuple[int, int, int], Fraction]:
    """Three cone constraints and the linear rational output coordinate.

    Individual Bernstein columns need not satisfy the endpoint constraints.
    Euclidean quotient and remainder are linear, so the returned output is
    the correct one after a constrained linear combination is formed.
    """
    data = output_data(h, require_common=False)
    constraints = (
        int(data["endpoint_real_constraint"]),
        int(data["A"]) - int(data["target"]),
        int(data["target"]),
    )
    return constraints, data["constant"]  # type: ignore[return-value]


def bernstein_column(m: int, j: int) -> list[int]:
    """Monomial coefficients of binom(m,j)x^j(1-x)^(m-j)."""
    h = [0] * (m + 1)
    for t in range(m - j + 1):
        h[j + t] = math.comb(m, j) * math.comb(m - j, t) * (-1) ** t
    return h


def determinant3(c1: tuple[int, int, int], c2: tuple[int, int, int], c3: tuple[int, int, int]) -> int:
    return (
        c1[0] * (c2[1] * c3[2] - c2[2] * c3[1])
        - c2[0] * (c1[1] * c3[2] - c1[2] * c3[1])
        + c3[0] * (c1[1] * c2[2] - c1[2] * c2[1])
    )


def clear_fraction_vector(values: list[Fraction]) -> tuple[list[int], Fraction]:
    denominator = 1
    for value in values:
        denominator = math.lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in values]
    content = 0
    for value in integers:
        content = math.gcd(content, abs(value))
    assert content > 0
    primitive = [value // content for value in integers]
    return primitive, Fraction(denominator, content)


def add_vectors(left: list[int], right: list[int]) -> list[int]:
    length = max(len(left), len(right))
    return [
        (left[k] if k < len(left) else 0)
        + (right[k] if k < len(right) else 0)
        for k in range(length)
    ]


def e_bounds(number_terms: int = 180) -> tuple[Fraction, Fraction]:
    lower = sum(
        (Fraction(1, math.factorial(k)) for k in range(number_terms + 1)),
        Fraction(0),
    )
    # For j>=0, (N+2)...(N+1+j) >= (N+2)^j.
    upper_tail = Fraction(
        number_terms + 2,
        (number_terms + 1) * math.factorial(number_terms + 1),
    )
    return lower, lower + upper_tail


def atan_reciprocal_bounds(inverse: int, last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            Fraction((-1) ** j, (2 * j + 1) * inverse ** (2 * j + 1))
            for j in range(last_index + 1)
        ),
        Fraction(0),
    )
    next_term = Fraction(
        (-1) ** (last_index + 1),
        (2 * last_index + 3) * inverse ** (2 * last_index + 3),
    )
    if next_term > 0:
        return partial, partial + next_term
    return partial + next_term, partial


def e_plus_pi_bounds() -> tuple[Fraction, Fraction]:
    e_lower, e_upper = e_bounds()
    a5_lower, a5_upper = atan_reciprocal_bounds(5, 150)
    a239_lower, a239_upper = atan_reciprocal_bounds(239, 50)
    # Machin: pi=16 atan(1/5)-4 atan(1/239).
    pi_lower = 16 * a5_lower - 4 * a239_upper
    pi_upper = 16 * a5_upper - 4 * a239_lower
    return e_lower + pi_lower, e_upper + pi_upper


def outward_decimal_interval(
    lower: Fraction, upper: Fraction, places: int = 40
) -> list[str]:
    scale = 10**places
    lower_integer = lower.numerator * scale // lower.denominator
    upper_integer = (
        upper.numerator * scale + upper.denominator - 1
    ) // upper.denominator

    def render(value: int) -> str:
        sign = "-" if value < 0 else ""
        value = abs(value)
        return f"{sign}{value // scale}.{value % scale:0{places}d}"

    return [render(lower_integer), render(upper_integer)]


def degree_seven_lattice_record() -> dict[str, object]:
    records = {}
    expected = {
        "target_generator": (H_A, (4, 0, Fraction(0))),
        "B_generator": (H_B, (0, 1, Fraction(0))),
        "correction_generator": (H_P, (0, 0, Fraction(1, 210))),
        "positive_interior": (H_STAR, (16, 41, Fraction(-44))),
    }
    for name, (h, wanted) in expected.items():
        data = output_data(h)
        actual = (int(data["target"]), int(data["B"]), data["correction"])
        assert actual == wanted
        records[name] = {
            "H": h,
            "target": actual[0],
            "B": actual[1],
            "correction": fraction_string(actual[2]),
            "l1_norm_H": sum(abs(value) for value in h),
        }

    # The congruence A((1-x)^2x^k)-a_k == 2 (mod 4) is the
    # all-degree proof ingredient for 4|a.  Check a long exact prefix as a
    # guard against transcription errors; the companion note gives the
    # four-residue-class proof.
    congruence_prefix = []
    for k in range(257):
        unit = [0] * (k + 1)
        unit[k] = 1
        data = output_data(unit, require_common=False)
        discrepancy = int(data["A"]) - int(data["target"])
        assert discrepancy % 4 == 2
        congruence_prefix.append(discrepancy % 4)

    return {
        "degree_7_exact_image": "4*Z x Z x (1/210)*Z in (a,B,I)",
        "generators": records,
        "universal_congruence_prefix_checked_through_k": 256,
        "local_positive_cone_sufficient_condition": (
            "3*t > 548*abs(r)+66*abs(s)+326*abs(u)"
        ),
        "local_positive_cone_data": {
            "a": "16*t+4*r",
            "B": "41*t+s",
            "I": "-44*t+u/210",
        },
    }


def finite_ray_record(
    q: int,
    p: int,
    m: int,
    support: tuple[int, int, int],
    s_bounds: tuple[Fraction, Fraction],
) -> dict[str, object]:
    columns = [bernstein_column(m, j) for j in support]
    constraint_columns = []
    output_columns = []
    for column in columns:
        constraints, output = formal_column_data(column)
        constraint_columns.append(constraints)
        output_columns.append(output)

    determinant = determinant3(*constraint_columns)
    assert determinant != 0
    rhs = (0, 0, 1)
    numerators = []
    for index in range(3):
        replaced = constraint_columns[:]
        replaced[index] = rhs
        numerators.append(determinant3(*replaced))
    weights = [Fraction(value, determinant) for value in numerators]
    assert all(weight >= 0 for weight in weights)

    vertex_output = sum(
        (weights[index] * output_columns[index] for index in range(3)),
        Fraction(0),
    )
    target_output = Fraction(-p, q)
    base_output = Fraction(-85, 16)
    assert vertex_output < target_output < base_output

    interpolation = (base_output - target_output) / (base_output - vertex_output)
    assert 0 < interpolation < 1

    rational_h = [Fraction(0) for _ in range(m + 1)]
    for k, coefficient in enumerate(H_STAR):
        rational_h[k] += (1 - interpolation) * Fraction(coefficient, 16)
    for index, column in enumerate(columns):
        for k, coefficient in enumerate(column):
            rational_h[k] += interpolation * weights[index] * coefficient

    cleared_h, scale = clear_fraction_vector(rational_h)
    base_data = output_data(cleared_h)
    assert int(base_data["target"]) == int(base_data["A"])
    assert base_data["primitive_pair"] == [q, -p]

    # H_vertex is nonnegative because it is a nonnegative Bernstein sum;
    # H_star>=3 on [0,1].  This is therefore a certified pointwise lower
    # bound for the cleared polynomial H.
    positivity_lower = scale * (1 - interpolation) * Fraction(3, 16)
    assert positivity_lower > sum(abs(value) for value in H_ZERO_64)

    final_h = add_vectors(cleared_h, H_ZERO_64)
    final_data = output_data(final_h)
    assert final_data["target"] == base_data["target"]
    assert final_data["B"] == base_data["B"]
    assert final_data["correction"] == base_data["correction"]
    assert final_data["primitive_pair"] == [q, -p]
    final_f = final_data["f"]
    assert isinstance(final_f, list)
    assert final_f[-1] == 1
    polynomial_content = 0
    for coefficient in final_f:
        polynomial_content = math.gcd(polynomial_content, abs(coefficient))
    assert polynomial_content == 1

    s_lower, s_upper = s_bounds
    error_lower = q * s_lower - p
    error_upper = q * s_upper - p
    assert error_lower > 0

    return {
        "degree_H_before_zero_direction": m,
        "degree_F_after_zero_direction": len(final_f) - 1,
        "support": list(support),
        "bernstein_vertex_weights": [fraction_string(value) for value in weights],
        "bernstein_vertex_output": fraction_string(vertex_output),
        "target_ray": [q, -p],
        "interpolation_weight_on_vertex": fraction_string(interpolation),
        "clearing_scale": fraction_string(scale),
        "cleared_H_coefficient_hash": vector_hash(cleared_h),
        "final_F_coefficient_hash": vector_hash(final_f),
        "maximum_final_F_coefficient_digits": max(
            len(str(abs(value))) for value in final_f
        ),
        "positivity_lower_bound_before_zero_direction": fraction_string(
            positivity_lower
        ),
        "zero_direction_l1_bound": sum(abs(value) for value in H_ZERO_64),
        "target_a": str(final_data["target"]),
        "B": str(final_data["B"]),
        "M": str(final_data["M"]),
        "D": str(final_data["D"]),
        "N": str(final_data["N"]),
        "cross_content_g": str(final_data["cross_content"]),
        "polynomial_content": polynomial_content,
        "primitive_value_interval": outward_decimal_interval(
            error_lower, error_upper
        ),
    }


def zero_direction_record() -> dict[str, object]:
    data = output_data(H_ZERO_64)
    assert data["target"] == 0
    assert data["A"] == 0
    assert data["B"] == 0
    assert data["correction"] == 0
    f = data["f"]
    assert isinstance(f, list)
    assert f[-1] == 1
    return {
        "degree_H": len(H_ZERO_64) - 1,
        "degree_F": len(f) - 1,
        "H": H_ZERO_64,
        "H_l1_norm": sum(abs(value) for value in H_ZERO_64),
        "F_leading_coefficient": f[-1],
        "F_coefficient_hash": vector_hash(f),
        "data": {"a": 0, "A": 0, "B": 0, "I": "0/1"},
    }


def moving_ray_record() -> dict[str, object]:
    samples = []
    for n in (343, 513, 683, 853, 1023):
        assert n % 170 == 3
        assert n >= 183
        margin = 3 * n - 548
        multiplier = 2028 // margin + 1
        h = add_vectors(
            [multiplier * (n * (H_STAR[k] if k < len(H_STAR) else 0) + H_A[k])
             for k in range(len(H_A))],
            H_ZERO_64,
        )
        data = output_data(h)
        assert data["primitive_pair"] == [16 * n + 4, -85 * n]
        assert data["cross_content"] == multiplier
        f = data["f"]
        assert isinstance(f, list) and f[-1] == 1
        samples.append(
            {
                "n": n,
                "multiplier": multiplier,
                "positive_H_lower_bound": multiplier * margin - 2028,
                "raw_target": data["target"],
                "cross_content": data["cross_content"],
                "primitive_pair": data["primitive_pair"],
            }
        )

    return {
        "admissible_n": "n == 3 (mod 170), n >= 183",
        "polynomial": "(1-x)^2*(t*(n*H_star+H_A)+H_zero_64)",
        "positivity_condition": "t*(3*n-548)>2028",
        "raw_data": {
            "a": "t*(16*n+4)",
            "B": "41*t*n",
            "I": "-44*t*n",
            "g": "t",
        },
        "primitive_pair": ["16*n+4", "-85*n"],
        "primitive_value": "n*(16*(e+pi)-85)+4*(e+pi)",
        "samples": samples,
    }


def build_certificate() -> dict[str, object]:
    s_bounds = e_plus_pi_bounds()
    assert s_bounds[0] < s_bounds[1]

    zero_record = zero_direction_record()
    finite_records = [
        finite_ray_record(q, p, m, support, s_bounds)
        for q, p, m, support in RAYS
    ]
    exact_upper_errors = [q * s_bounds[1] - p for q, p, _, _ in RAYS]
    assert all(
        exact_upper_errors[index + 1] < exact_upper_errors[index]
        for index in range(len(exact_upper_errors) - 1)
    )

    return {
        "title": "Factor-endpoint positive cone: lattice and changing primitive rays",
        "arithmetic": "exact integers and fractions",
        "degree_seven_lattice": degree_seven_lattice_record(),
        "zero_output_direction": zero_record,
        "finite_changing_primitive_rays": finite_records,
        "primitive_values_strictly_decrease": True,
        "smallest_certified_primitive_value_interval": finite_records[-1][
            "primitive_value_interval"
        ],
        "infinite_moving_ray_family": moving_ray_record(),
        "scope": (
            "finite small rays plus an infinite nonshrinking moving-ray family; "
            "no irrationality or transcendence conclusion"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "factor_endpoint_positive_cone_rays_certificate.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(arguments.output)


if __name__ == "__main__":
    main()
