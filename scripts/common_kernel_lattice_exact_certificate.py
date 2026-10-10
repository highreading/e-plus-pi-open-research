#!/usr/bin/env python3
"""Exact certificate for the common-kernel e+pi lattice audit.

All assertions that carry mathematical content use integers or exact
fractions.  Decimal-looking claims about e+pi are deliberately avoided:
the script constructs rational enclosures for e and pi and records exact
interval endpoints.

The companion note is
    sources/common_kernel_lattice_identity_and_capacity_audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def derangement(n: int) -> int:
    if n == 0:
        return 1
    previous, current = 1, 0
    for k in range(2, n + 1):
        previous, current = current, (k - 1) * (previous + current)
    return current


def endpoint_a_monomial(n: int) -> int:
    """A(x^n), where A(g)=sum_k (-1)^k g^(k)(1)."""
    return (-1) ** n * derangement(n)


def constraints(g_degree: int) -> sp.Matrix:
    """Constraint matrix on (a,h_1,...,h_{g_degree+1})."""
    number = g_degree + 2
    rows: list[list[int]] = []

    row = [0] * number
    for j in range(g_degree + 1):
        row[j + 1] = (j + 1) * (
            endpoint_a_monomial(j) + endpoint_a_monomial(j + 2)
        )
    rows.append(row)

    row = [0] * number
    row[0] = 1
    row[1] = 1
    rows.append(row)

    row = [0] * number
    row[0] = 1
    for j in range(g_degree + 1):
        row[j + 1] = 2 * (j + 1)
    rows.append(row)
    return sp.Matrix(rows)


def variable_to_f(variable: list[int], g_degree: int) -> list[int]:
    """Return monomial coefficients of f=a+(1+x^2)H'."""
    a = variable[0]
    h = variable[1:]
    coefficients = [0] * (g_degree + 3)
    coefficients[0] = a
    for j in range(g_degree + 1):
        derivative_coefficient = (j + 1) * h[j]
        coefficients[j] += derivative_coefficient
        coefficients[j + 2] += derivative_coefficient
    return coefficients


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return g>=0 and s,t with s*a+t*b=g."""
    aa, bb = abs(a), abs(b)
    old_r, r = aa, bb
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if a < 0:
        old_s = -old_s
    if b < 0:
        old_t = -old_t
    return old_r, old_s, old_t


def saturated_integer_kernel(g_degree: int) -> list[list[int]]:
    """Construct a saturated Z-basis after exact endpoint elimination.

    Write M=g_degree+1.  Endpoint vanishing gives
        h_1=-sum_{r=2}^M 2r h_r,  a=-h_1.
    Substitution in A((1+x^2)H')=0 leaves one primitive equation in
    h_2,...,h_M.  A recorded unimodular column reduction of that row gives
    the full, saturated integer kernel.
    """
    matrix = constraints(g_degree)
    maximum_h_index = g_degree + 1
    a_row = [int(matrix[0, r]) for r in range(1, maximum_h_index + 1)]
    reduced_row = [
        a_row[r - 1] - 4 * r for r in range(2, maximum_h_index + 1)
    ]
    common = 0
    for value in reduced_row:
        common = math.gcd(common, abs(value))
    assert common == 2
    primitive = [value // common for value in reduced_row]

    length = len(primitive)
    transform = [[int(i == j) for j in range(length)] for i in range(length)]
    transformed_row = primitive[:]
    for j in range(1, length):
        left, right = transformed_row[0], transformed_row[j]
        gcd_value, s, t = extended_gcd(left, right)
        old_left = [transform[i][0] for i in range(length)]
        old_right = [transform[i][j] for i in range(length)]
        for i in range(length):
            transform[i][0] = s * old_left[i] + t * old_right[i]
            transform[i][j] = (
                -(right // gcd_value) * old_left[i]
                + (left // gcd_value) * old_right[i]
            )
        transformed_row[0] = gcd_value
        transformed_row[j] = 0

    assert transformed_row == [1] + [0] * (length - 1)
    basis: list[list[int]] = []
    for column in range(1, length):
        h_tail = [transform[i][column] for i in range(length)]
        h_1 = -sum(
            2 * r * h_tail[r - 2] for r in range(2, maximum_h_index + 1)
        )
        variable = [-h_1, h_1] + h_tail
        assert matrix * sp.Matrix(variable) == sp.zeros(3, 1)
        basis.append(variable)
    assert len(basis) == g_degree - 1
    return basis


def endpoint_b(f_coefficients: list[int]) -> int:
    return sum(
        (-1) ** k * math.factorial(k) * coefficient
        for k, coefficient in enumerate(f_coefficients)
    )


def phi(variable: list[int], g_degree: int) -> tuple[int, int]:
    f_coefficients = variable_to_f(variable, g_degree)
    a = variable[0]
    b = -endpoint_b(f_coefficients) + 4 * sum(variable[1:])
    return a, b


def shifted_chebyshev_matrix(degree: int) -> sp.Matrix:
    x = sp.Symbol("x")
    columns = []
    for k in range(degree + 1):
        polynomial = sp.Poly(sp.chebyshevt(k, 2 * x - 1), x)
        columns.append([polynomial.nth(j) for j in range(degree + 1)])
    return sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))


def canonical_fraction(value: Fraction | sp.Rational) -> str:
    if isinstance(value, sp.Rational):
        numerator = int(value.p)
        denominator = int(value.q)
    else:
        numerator = value.numerator
        denominator = value.denominator
    return f"{numerator}/{denominator}"


def as_fraction(value: sp.Rational) -> Fraction:
    return Fraction(int(value.p), int(value.q))


def rational_hash(value: sp.Rational) -> str:
    return hashlib.sha256(canonical_fraction(value).encode("ascii")).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def e_bounds(terms: int = 80) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, math.factorial(k)) for k in range(terms + 1)), Fraction()
    )
    first_omitted = Fraction(1, math.factorial(terms + 1))
    upper_tail = first_omitted * Fraction(terms + 2, terms + 1)
    return partial, partial + upper_tail


def atan_reciprocal_bounds(q: int, last_index: int = 100) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            Fraction((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
            for k in range(last_index + 1)
        ),
        Fraction(),
    )
    next_term = Fraction(
        (-1) ** (last_index + 1),
        (2 * last_index + 3) * q ** (2 * last_index + 3),
    )
    return min(partial, partial + next_term), max(partial, partial + next_term)


def alpha_bounds() -> tuple[Fraction, Fraction]:
    """Certified enclosure of alpha=e+pi using Machin's formula."""
    e_lower, e_upper = e_bounds()
    a5_lower, a5_upper = atan_reciprocal_bounds(5)
    a239_lower, a239_upper = atan_reciprocal_bounds(239)
    pi_lower = 16 * a5_lower - 4 * a239_upper
    pi_upper = 16 * a5_upper - 4 * a239_lower
    return e_lower + pi_lower, e_upper + pi_upper


def linear_interval(
    coefficient: int, constant: int, lower: Fraction, upper: Fraction
) -> tuple[Fraction, Fraction]:
    if coefficient >= 0:
        return coefficient * lower + constant, coefficient * upper + constant
    return coefficient * upper + constant, coefficient * lower + constant


def signed_decade(interval: tuple[Fraction, Fraction]) -> dict[str, object]:
    lower, upper = interval
    assert not (lower <= 0 <= upper)
    sign = 1 if lower > 0 else -1
    smallest = min(abs(lower), abs(upper))
    largest = max(abs(lower), abs(upper))
    exponent = 0
    if largest < 1:
        while largest < Fraction(1, 10**exponent):
            exponent += 1
        exponent -= 1
        # 10^(-exponent-1) < |x| < 10^(-exponent) is the desired form.
        while not (
            Fraction(1, 10 ** (exponent + 1)) < smallest
            and largest < Fraction(1, 10**exponent)
        ):
            exponent += 1
    else:
        while Fraction(10**exponent, 1) <= largest:
            exponent += 1
        exponent = -exponent
    return {
        "sign": sign,
        "exact_lower": canonical_fraction(lower),
        "exact_upper": canonical_fraction(upper),
        "absolute_value_between": [
            canonical_fraction(Fraction(1, 10 ** (exponent + 1))),
            canonical_fraction(Fraction(1, 10**exponent)),
        ],
    }


def primitive_rational_nullspace(matrix: sp.Matrix) -> list[list[int]]:
    rows = []
    for vector in matrix.nullspace():
        denominator = 1
        for value in vector:
            denominator = math.lcm(denominator, int(value.q))
        values = [int(value * denominator) for value in vector]
        common = 0
        for value in values:
            common = math.gcd(common, abs(value))
        rows.append([value // common for value in values])
    return rows


def row_lattice_saturation_index(rows: list[list[int]]) -> int:
    matrix = sp.Matrix(rows)
    smith = smith_normal_form(matrix, domain=ZZ)
    index = 1
    for i in range(min(smith.rows, smith.cols)):
        if smith[i, i] != 0:
            index *= abs(int(smith[i, i]))
    return index


def image_invariants(g_degree: int) -> dict[str, int]:
    basis = saturated_integer_kernel(g_degree)
    pairs = [phi(vector, g_degree) for vector in basis]
    gcd_a = 0
    gcd_b = 0
    gcd_entries = 0
    gcd_two_minors = 0
    for a, b in pairs:
        gcd_a = math.gcd(gcd_a, abs(a))
        gcd_b = math.gcd(gcd_b, abs(b))
        gcd_entries = math.gcd(gcd_entries, abs(a))
        gcd_entries = math.gcd(gcd_entries, abs(b))
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            determinant = pairs[i][0] * pairs[j][1] - pairs[j][0] * pairs[i][1]
            gcd_two_minors = math.gcd(gcd_two_minors, abs(determinant))
    assert gcd_a == 8
    assert gcd_b == 2
    assert gcd_entries == 2
    assert gcd_two_minors == 16
    return {
        "gcd_a": gcd_a,
        "gcd_b": gcd_b,
        "first_smith_invariant": gcd_entries,
        "image_index_in_Z2": gcd_two_minors,
        "second_smith_invariant": gcd_two_minors // gcd_entries,
    }


def quotient_metric_record(
    g_degree: int,
    alpha_interval: tuple[Fraction, Fraction],
    rho_interval: tuple[Fraction, Fraction],
) -> dict[str, object]:
    f_degree = g_degree + 2
    basis = saturated_integer_kernel(g_degree)
    inverse_chebyshev = shifted_chebyshev_matrix(f_degree).inv()
    chebyshev_rows = sp.Matrix.hstack(
        *(
            inverse_chebyshev * sp.Matrix(variable_to_f(vector, g_degree))
            for vector in basis
        )
    ).T
    gram = chebyshev_rows * chebyshev_rows.T
    output_matrix = sp.Matrix(
        [[phi(vector, g_degree)[coordinate] for vector in basis] for coordinate in (0, 1)]
    )
    riesz_covariance = output_matrix * gram.inv() * output_matrix.T
    image_basis = sp.diag(8, 2)
    quotient_metric = image_basis.T * riesz_covariance.inv() * image_basis
    quotient_metric = quotient_metric.applyfunc(sp.factor)
    determinant = sp.factor(quotient_metric.det())
    assert determinant > 0

    slope = sp.factor(-quotient_metric[0, 1] / quotient_metric[1, 1])
    slope_fraction = as_fraction(slope)
    alpha_lower, alpha_upper = alpha_interval
    slope_error = (
        slope_fraction + 4 * alpha_lower,
        slope_fraction + 4 * alpha_upper,
    )
    assert not (slope_error[0] <= 0 <= slope_error[1])

    determinant_fraction = as_fraction(determinant)
    rho_lower, rho_upper = rho_interval
    normalized_lower = determinant_fraction * rho_lower ** (2 * f_degree)
    normalized_upper = determinant_fraction * rho_upper ** (2 * f_degree)
    integer_lower = normalized_lower.numerator // normalized_lower.denominator
    integer_upper = (
        normalized_upper.numerator + normalized_upper.denominator - 1
    ) // normalized_upper.denominator

    return {
        "g_degree": g_degree,
        "f_degree": f_degree,
        "rank": len(basis),
        "quotient_metric_on_u_v": [
            [canonical_fraction(quotient_metric[i, j]) for j in range(2)]
            for i in range(2)
        ],
        "quotient_metric_determinant": canonical_fraction(determinant),
        "quotient_metric_determinant_sha256": rational_hash(determinant),
        "continuous_optimal_v_over_u": canonical_fraction(slope),
        "continuous_slope_plus_4alpha_enclosure": signed_decade(slope_error),
        "determinant_times_rho_to_2D_integer_enclosure": [
            integer_lower,
            integer_upper,
        ],
    }


CORRECTED_CANDIDATES: dict[int, dict[str, object]] = {
    32: {
        "h": [
            52439838563088, 0, -17479946187696, -1, 10487967712712,
            -4159, -7491405397112, -2054137, 5826676081235,
            -274471444, -4765130826093, -12919445924, 4095621828964,
            -230779743379, -2845987790488, -1221827384981,
            3670750839088, 5935768085953, -30818269103405,
            77985908348611, -157609682538877, 257405266122305,
            -332147639079563, 336989407235076, -269367336364750,
            169522114116633, -83328246162956, 31391856813539,
            -8743125445655, 1682321932733, -193085035475,
            7875562931, 436689535,
        ],
        "a": -52439838563088,
        "b": 307290871838600,
        "chebyshev_l1": Fraction(342075143692469, 36893488147419103232),
    },
    40: {
        "h": [
            -461515305521655600, 0, 153838435173885200, 0,
            -92303061104331116, -482, 65930757931692817, -1006912,
            -51279478365459305, -498189459, 41955944369935747,
            -90672448622, -35500281547655382, -7341284601930,
            30818147942358238, -293402742768892,
            -25695426639948069, -6151908266544618, 46650705001800828,
            -69852477682017961, 165502470330655435,
            -431146618797011914, 864582102724254122,
            -1393290173864306361, 1877383119436032177,
            -2036571379396784218, 1552530965177864966,
            -408066030868110354, -934473227571679177,
            1832395393035383687, -1964159576942462350,
            1507737650884391879, -882394651106129320,
            399908943992292704, -139488463620305290,
            36558545744702825, -6867755692364982, 844645328977184,
            -55153961514524, 646233951621, 59502596865,
        ],
        "a": 461515305521655600,
        "b": -2704421761901323052,
        "chebyshev_l1": Fraction(
            1672003183159179573, 4835703278458516698824704
        ),
    },
}


def candidate_record(
    g_degree: int, alpha_interval: tuple[Fraction, Fraction]
) -> dict[str, object]:
    data = CORRECTED_CANDIDATES[g_degree]
    h = list(data["h"])
    a = int(data["a"])
    b = int(data["b"])
    variable = [a] + h
    matrix = constraints(g_degree)
    assert matrix * sp.Matrix(variable) == sp.zeros(3, 1)
    assert phi(variable, g_degree) == (a, b)

    f_degree = g_degree + 2
    f_coefficients = variable_to_f(variable, g_degree)
    inverse_chebyshev = shifted_chebyshev_matrix(f_degree).inv()
    chebyshev = inverse_chebyshev * sp.Matrix(f_coefficients)
    l1 = sum((abs(as_fraction(value)) for value in chebyshev), Fraction())
    assert l1 == data["chebyshev_l1"]
    assert f_coefficients[0] == 0
    assert sum(f_coefficients) == 0

    form_interval = linear_interval(a, b, *alpha_interval)
    assert not (form_interval[0] <= 0 <= form_interval[1])
    common = math.gcd(abs(a), abs(b))
    return {
        "g_degree": g_degree,
        "f_degree": f_degree,
        "a": a,
        "b": b,
        "gcd_a_b": common,
        "primitive_a": a // common,
        "primitive_b": b // common,
        "chebyshev_l1_bound": canonical_fraction(l1),
        "certified_form_enclosure": signed_decade(form_interval),
        "monomial_coefficients_sha256": hashlib.sha256(
            json.dumps(f_coefficients, separators=(",", ":")).encode("ascii")
        ).hexdigest(),
    }


def rho_polynomial(value: Fraction) -> Fraction:
    return (
        value**8
        - 20 * value**6
        - 26 * value**4
        - 20 * value**2
        + 1
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/common_kernel_lattice_exact_certificate.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/common_kernel_lattice_identity_and_capacity_audit.md"),
    )
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    assert source_path.is_file()

    alpha_interval = alpha_bounds()
    assert alpha_interval[0] < alpha_interval[1]

    rho_lower = Fraction(1152895447327, 250000000000)
    rho_upper = Fraction(4611581789309, 1000000000000)
    assert rho_polynomial(rho_lower) < 0 < rho_polynomial(rho_upper)
    # The polynomial is strictly increasing on [4, infinity): after division
    # of its derivative by 8x, x^6-15x^4-13x^2-5 is positive at 4 and
    # increasing there.
    assert 4**6 - 15 * 4**4 - 13 * 4**2 - 5 > 0
    rho_interval = (rho_lower, rho_upper)

    # The old operation "primitive each rational nullspace ray" does not in
    # general return the saturated integer kernel.  Record exact indices.
    old_indices: dict[str, int] = {}
    expected_old_indices = {
        8: 24,
        16: 10368,
        24: 4478976,
        32: 644972544,
        40: 278628139008,
    }
    for degree, expected in expected_old_indices.items():
        old_basis = primitive_rational_nullspace(constraints(degree))
        index = row_lattice_saturation_index(old_basis)
        assert index == expected
        old_indices[str(degree)] = index

    image_records = {}
    for degree in range(5, 41):
        image_records[str(degree)] = image_invariants(degree)

    # Explicit generators prove the all-degree statement once g_degree>=5,
    # since they may be padded by zero high coefficients.
    generator_80 = [8, -8, 57626, -102668, 38706, 7590, -3]
    generator_02 = [0, 0, -57301, 102118, -38505, -7550, 3]
    assert constraints(5) * sp.Matrix(generator_80) == sp.zeros(3, 1)
    assert constraints(5) * sp.Matrix(generator_02) == sp.zeros(3, 1)
    assert phi(generator_80, 5) == (8, 0)
    assert phi(generator_02, 5) == (0, 2)

    quotient_records = [
        quotient_metric_record(degree, alpha_interval, rho_interval)
        for degree in (8, 16, 24, 32, 40)
    ]
    candidate_records = [
        candidate_record(degree, alpha_interval) for degree in (32, 40)
    ]

    output: dict[str, object] = {
        "description": "Exact certificate for the common-kernel e+pi lattice audit",
        "script_path": str(script_path),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "identity_convention": {
            "A_g": "sum_{k>=0} (-1)^k g^(k)(1)",
            "B_g": "sum_{k>=0} (-1)^k g^(k)(0)",
            "f": "a+(1+x^2)H'(x)",
            "integer_form": "a*(e+pi)-B(f)+4*(H(1)-H(0))",
        },
        "certified_alpha_enclosure": {
            "lower": canonical_fraction(alpha_interval[0]),
            "upper": canonical_fraction(alpha_interval[1]),
            "method": "80-term exponential series and 101-term alternating Machin arctangent series",
        },
        "rho": {
            "defining_polynomial": "x^8-20*x^6-26*x^4-20*x^2+1",
            "lower": canonical_fraction(rho_lower),
            "upper": canonical_fraction(rho_upper),
            "lower_polynomial_sign": -1,
            "upper_polynomial_sign": 1,
        },
        "saturation_audit": {
            "old_primitive_rational_ray_basis_indices": old_indices,
            "corrected_method": "endpoint elimination followed by a recorded unimodular reduction of the remaining primitive row",
        },
        "image_theorem": {
            "statement": "Phi(K_D)=8Z x 2Z for every g_degree>=5",
            "finite_exhaustive_tested_g_degrees": [5, 40],
            "per_degree_invariants": image_records,
            "explicit_generator_for_8_0": generator_80,
            "explicit_generator_for_0_2": generator_02,
        },
        "corrected_candidates": candidate_records,
        "quotient_metric_records": quotient_records,
        "scope": {
            "exact": "All stored matrices, determinants, slopes, bounds, and candidate checks use integers or rational numbers.",
            "not_proved": "The finite quotient data do not prove an asymptotic capacity limit and do not exclude exceptional exponent-greater-than-one vectors.",
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(args.output),
        "old_index_degree_40": old_indices["40"],
        "image_degrees_checked": 36,
        "quotient_degrees": [record["f_degree"] for record in quotient_records],
        "candidate_degrees": [record["f_degree"] for record in candidate_records],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
