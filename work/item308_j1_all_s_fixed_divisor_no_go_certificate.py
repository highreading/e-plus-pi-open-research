#!/usr/bin/env python3
"""Exact replay for Item 308's all-s residue and scoped height no-go.

The all-s proof is symbolic and is written in the companion report.  This
checker verifies the polynomial source identity in Q[s,t], evaluates the two
finite coefficient definitions by exact rational/Gaussian arithmetic,
independently reconstructs the partial fractions on a fixed bounded control
list, and checks preselected residue rows.  It performs no factorization and
no prime scan.
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
DEFAULT_OUTPUT = HERE / "item308_j1_all_s_fixed_divisor_no_go_certificate.json"
BASE_PATH = HERE / "item307_j1_structural_ray_fixed_divisor_certificate.py"
BASE_HASH = "77984debb89364022ec7055754dac68e07d3027a2af1f69cc36d478602474d22"
Q = Fraction


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if sha256(BASE_PATH) != BASE_HASH:
    raise RuntimeError(("Item307 base mismatch", sha256(BASE_PATH)))
base = load("item308_item307_base", BASE_PATH)


def encode_fraction(value: Q) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def qseries_multiply(left: list[Q], right: list[Q], maximum: int) -> list[Q]:
    out = [Q(0)] * (maximum + 1)
    for j, x_value in enumerate(left[: maximum + 1]):
        for k, y_value in enumerate(right[: maximum + 1 - j]):
            out[j + k] += x_value * y_value
    return out


def half_binomial_series(top: Q, maximum: int) -> list[Q]:
    out = [Q(1)]
    for degree in range(maximum):
        out.append(out[-1] * (top - degree) / (degree + 1))
    return out


def gadd(left: tuple[Q, Q], right: tuple[Q, Q]) -> tuple[Q, Q]:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: tuple[Q, Q], right: tuple[Q, Q]) -> tuple[Q, Q]:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gscale(value: tuple[Q, Q], scalar: Q | int) -> tuple[Q, Q]:
    return value[0] * scalar, value[1] * scalar


def ginv(value: tuple[Q, Q]) -> tuple[Q, Q]:
    norm = value[0] * value[0] + value[1] * value[1]
    return value[0] / norm, -value[1] / norm


def gpow(value: tuple[Q, Q], exponent: int) -> tuple[Q, Q]:
    out = (Q(1), Q(0))
    while exponent:
        if exponent & 1:
            out = gmul(out, value)
        value = gmul(value, value)
        exponent //= 2
    return out


def gseries_multiply(
    left: list[tuple[Q, Q]], right: list[tuple[Q, Q]], maximum: int
) -> list[tuple[Q, Q]]:
    out = [(Q(0), Q(0)) for _ in range(maximum + 1)]
    for j, x_value in enumerate(left[: maximum + 1]):
        for k, y_value in enumerate(right[: maximum + 1 - j]):
            out[j + k] = gadd(out[j + k], gmul(x_value, y_value))
    return out


def inverse_linear_series(
    coefficient: tuple[Q, Q], exponent: int, maximum: int
) -> list[tuple[Q, Q]]:
    powers = [(Q(1), Q(0))]
    for _ in range(maximum):
        powers.append(gmul(powers[-1], coefficient))
    return [
        gscale(
            powers[degree],
            (-1) ** degree * math.comb(exponent + degree - 1, degree),
        )
        for degree in range(maximum + 1)
    ]


def alpha_coefficient(s_value: int) -> Q:
    """Formula (4.2)."""
    maximum = 2 * s_value + 5
    top = Q(6 * s_value + 1, 2)
    numerator = base.rational_source(s_value)[0]

    # N_s(1+x).
    shifted = [Q(0)] * len(numerator)
    for degree, coefficient in enumerate(numerator):
        for index in range(degree + 1):
            shifted[index] += coefficient * math.comb(degree, index)

    inverse = [Q(0)] * (maximum + 1)
    for twice_degree in range(0, maximum + 1, 2):
        degree = twice_degree // 2
        inverse[twice_degree] = (
            (-1) ** degree * math.comb(2 * s_value + degree, degree)
        )

    product = qseries_multiply(
        half_binomial_series(top, maximum), shifted, maximum
    )
    product = qseries_multiply(product, inverse, maximum)
    return -product[maximum]


def beta_coefficient(s_value: int) -> tuple[Q, Q]:
    """Formula (4.3), returned as (real, imaginary)."""
    maximum = 2 * s_value
    top = Q(6 * s_value + 1, 2)
    q_value = 2 * s_value + 1
    r_value = 2 * s_value + 6
    numerator = base.rational_source(s_value)[0]

    # N_s((1-i)(1+x)).
    t_zero = (Q(1), Q(-1))
    shifted = [(Q(0), Q(0)) for _ in range(len(numerator))]
    for degree, coefficient in enumerate(numerator):
        t_power = gpow(t_zero, degree)
        for index in range(degree + 1):
            shifted[index] = gadd(
                shifted[index],
                gscale(t_power, coefficient * math.comb(degree, index)),
            )

    half = [(value, Q(0)) for value in half_binomial_series(top, maximum)]
    first_inverse = inverse_linear_series(
        (Q(1), Q(1)), r_value, maximum
    )
    second_inverse = inverse_linear_series(
        (Q(1, 2), Q(1, 2)), q_value, maximum
    )
    product = gseries_multiply(half, shifted, maximum)
    product = gseries_multiply(product, first_inverse, maximum)
    product = gseries_multiply(product, second_inverse, maximum)
    constant = gmul(
        gscale(gpow((Q(0), Q(1)), r_value), 2**q_value),
        gpow((Q(1), Q(1)), q_value),
    )
    return gmul(product[maximum], ginv(constant))


def partial_fraction_aggregate(s_value: int) -> tuple[Q, Q, Q]:
    """Independent exact evaluation of A_s,U_s,V_s from (5.2)."""
    numerator, denominator, one_order, gaussian_order = base.rational_source(
        s_value
    )
    coordinate_count = one_order + 2 * gaussian_order
    if coordinate_count != 6 * s_value + 8:
        raise AssertionError(("denominator degree", s_value, coordinate_count))
    sequence = base.series_coefficients(
        numerator, denominator, coordinate_count
    )
    powers = base.lambda_powers(coordinate_count)
    matrix = [
        base.basis_row(index, one_order, gaussian_order, powers[index])
        for index in range(coordinate_count)
    ]
    solution = base.solve_exact(matrix, sequence)
    n_special = Q(-(6 * s_value + 3), 2)

    a_value = Q(0)
    for order in range(1, one_order + 1):
        a_value += solution[order - 1] * base.generalized_binomial(
            n_special + order - 1, order - 1
        )

    u_value = Q(0)
    v_value = Q(0)
    offset = one_order
    for order in range(1, gaussian_order + 1):
        binomial = base.generalized_binomial(
            n_special + order - 1, order - 1
        )
        u_value += solution[offset + 2 * (order - 1)] * binomial
        v_value += solution[offset + 2 * (order - 1) + 1] * binomial
    return a_value, u_value, v_value


def delta(s_value: int, parity: int) -> int:
    return (-1) ** (
        s_value * (s_value + 1) // 2 + 1 + parity
    )


def eta(s_value: int) -> int:
    exponent = 3 * s_value + 1
    return 2 ** (exponent - 2 * (exponent // 2))


def clearing(s_value: int) -> int:
    return 3 * 2 ** (10 * s_value + 10)


def integer_form(
    s_value: int, parity: int, aggregate: tuple[Q, Q, Q]
) -> dict[str, Any]:
    alpha, real, imaginary = aggregate
    sign = delta(s_value, parity)
    x_value = 2 ** (2 * s_value) * alpha
    if parity == 0:
        y_value = sign * 2 ** (5 * s_value + 2) * real
    else:
        y_value = -sign * 2 ** (5 * s_value + 2) * imaginary
    scale = clearing(s_value)
    a_integer = scale * x_value
    b_integer = scale * y_value
    if a_integer.denominator != 1 or b_integer.denominator != 1:
        raise AssertionError(("clearing", s_value, parity))
    a_integer = a_integer.numerator
    b_integer = b_integer.numerator
    divisor = (
        2 ** (3 * s_value + 1) * a_integer * a_integer
        - sign * b_integer * b_integer
    )
    k_value = (3 * s_value + 1) // 2
    z_value = 2**k_value * a_integer
    norm_rewrite = eta(s_value) * z_value * z_value - sign * b_integer * b_integer
    if divisor != norm_rewrite:
        raise AssertionError(("norm identity", s_value, parity))
    if eta(s_value) != (1 if s_value % 2 else 2):
        raise AssertionError(("eta", s_value))
    return {
        "parity": parity,
        "delta": sign,
        "eta": eta(s_value),
        "a_s": a_integer,
        "b_s_epsilon": b_integer,
        "D_s_epsilon": divisor,
        "norm_identity": (
            "D=eta*z^2-delta*b^2="
            "-delta*Norm_(K/Q)(b+z*theta), where "
            "K=Q[T]/(T^2-delta*eta)"
        ),
        "z": z_value,
        "D_nonzero_on_this_control": divisor != 0,
    }


def denominator_divides(value: Q, bound: int) -> bool:
    return bound % value.denominator == 0


CONTROL_S = (1, 2, 3, 4, 5, 6, 8)


def coefficient_controls() -> list[dict[str, Any]]:
    answer: list[dict[str, Any]] = []
    for s_value in CONTROL_S:
        direct_alpha = alpha_coefficient(s_value)
        direct_real, direct_imag = beta_coefficient(s_value)
        aggregate = partial_fraction_aggregate(s_value)
        if aggregate != (direct_alpha, direct_real, direct_imag):
            raise AssertionError(("coefficient formula", s_value))

        alpha_denominator_bound = 3 * 2 ** (4 * s_value + 10)
        beta_denominator_bound = 3 * 2 ** (10 * s_value + 2)
        if not denominator_divides(direct_alpha, alpha_denominator_bound):
            raise AssertionError(("alpha denominator", s_value))
        if not all(
            denominator_divides(value, beta_denominator_bound)
            for value in (direct_real, direct_imag)
        ):
            raise AssertionError(("beta denominator", s_value))

        answer.append(
            {
                "s": s_value,
                "denominator_degree": 6 * s_value + 8,
                "A_s": encode_fraction(direct_alpha),
                "U_s": encode_fraction(direct_real),
                "V_s": encode_fraction(direct_imag),
                "proved_uniform_alpha_denominator_bound": (
                    f"3*2^{4*s_value+10}"
                ),
                "proved_uniform_beta_denominator_bound": (
                    f"3*2^{10*s_value+2}"
                ),
                "integer_forms": [
                    integer_form(s_value, parity, aggregate)
                    for parity in (0, 1)
                ],
                "classification": (
                    "FIXED BOUNDED EXACT REPLAY OF THE SYMBOLIC ALL-s FORMULA"
                ),
            }
        )
    return answer


# A tiny affine polynomial ring Q[s], encoded as (constant, s coefficient).
Lin = tuple[Q, Q]


def ladd(left: Lin, right: Lin) -> Lin:
    return left[0] + right[0], left[1] + right[1]


def lscale(value: Lin, scalar: Q | int) -> Lin:
    return value[0] * scalar, value[1] * scalar


def poly_add(left: list[Lin], right: list[Lin]) -> list[Lin]:
    out = [(Q(0), Q(0))] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] = ladd(out[index], value)
    for index, value in enumerate(right):
        out[index] = ladd(out[index], value)
    return out


def poly_multiply_constant(
    left: list[Lin], right: list[Q]
) -> list[Lin]:
    out = [(Q(0), Q(0))] * (len(left) + len(right) - 1)
    for j, x_value in enumerate(left):
        for k, y_value in enumerate(right):
            out[j + k] = ladd(out[j + k], lscale(x_value, y_value))
    return out


def poly_shift(left: list[Lin]) -> list[Lin]:
    return [(Q(0), Q(0))] + left


def symbolic_source_audit() -> dict[str, Any]:
    """Verify (3.5) as an identity in Q[s,t], not at sampled s."""
    # Constant polynomials used in Item307's derivation.
    d_poly = [Q(2), Q(-2), Q(1)]
    d_prime = [Q(-2), Q(2)]
    one_minus_t = [Q(1), Q(-1)]
    r_one = [Q(10, 3), Q(-13, 3), Q(5, 3)]
    r_one_prime = [Q(-13, 3), Q(10, 3)]
    r_zero = [Q(2), Q(-9), Q(4)]

    # Recompute (t R1' + R0)(1-t)D.
    t_r_one_prime = [Q(0)] + r_one_prime
    length = max(len(t_r_one_prime), len(r_zero))
    sum_poly = [Q(0)] * length
    for index, value in enumerate(t_r_one_prime):
        sum_poly[index] += value
    for index, value in enumerate(r_zero):
        sum_poly[index] += value
    recomputed_first = base.multiply(
        sum_poly, base.multiply(one_minus_t, d_poly)
    )

    first = [(value, Q(0)) for value in recomputed_first]
    second_base = base.multiply(base.shift(r_one), d_poly)
    third_base = base.multiply(
        base.multiply(base.shift(r_one), d_prime), one_minus_t
    )
    # (2s+5)*second_base - 2s*third_base.
    second = [(5 * value, 2 * value) for value in second_base]
    third = [(Q(0), -2 * value) for value in third_base]
    numerator = poly_add(poly_add(first, second), third)

    expected = [
        (Q(4), Q(0)),
        (Q(-4, 3), Q(80, 3)),
        (Q(-8, 3), Q(-224, 3)),
        (Q(16, 3), Q(256, 3)),
        (Q(-3), Q(-46)),
        (Q(1), Q(10)),
    ]
    if numerator != expected:
        raise AssertionError(("symbolic N_s", numerator, expected))

    # Parameter identities behind the negative-binomial transforms.
    # Each tuple means coefficient of s, then constant term.
    n_special = (Q(-3), Q(-3, 2))
    minus_n_minus_one = (
        -n_special[0],
        -n_special[1] - 1,
    )
    if minus_n_minus_one != (Q(3), Q(1, 2)):
        raise AssertionError("negative-binomial top")

    return {
        "identity_ring": "Q[s,t]",
        "N_s_coefficients_low_to_high_as_constant_plus_s_coefficient": [
            [encode_fraction(value[0]), encode_fraction(value[1])]
            for value in numerator
        ],
        "one_pole_order": "2s+6",
        "gaussian_pole_order": "2s+1",
        "denominator_degree": "6s+8",
        "special_index": "-(6s+3)/2",
        "negative_binomial_top": "3s+1/2",
        "one_pole_extraction_degree": "2s+5 (odd sign)",
        "gaussian_pole_extraction_degree": "2s (even sign)",
        "classification": "SYMBOLIC IDENTITY FOR EVERY INTEGER s>=1",
    }


def legendre_two_from_mod_8(residue: int) -> int:
    return 1 if residue in (1, 7) else -1


def euler_sign_audit() -> list[dict[str, int]]:
    answer = []
    representative = {0: 4, 1: 1, 2: 2, 3: 3}
    expected = {
        0: (-1, 1, 2),
        1: (1, -1, 1),
        2: (1, -1, 2),
        3: (-1, 1, 1),
    }
    for residue in range(4):
        s_value = representative[residue]
        row = []
        for parity in (0, 1):
            p_mod_8 = (4 * parity + 6 * s_value + 3) % 8
            sign = delta(s_value, parity)
            if legendre_two_from_mod_8(p_mod_8) != sign:
                raise AssertionError(("Euler sign", residue, parity))
            row.append(sign)
        if (row[0], row[1], eta(s_value)) != expected[residue]:
            raise AssertionError(("sign table", residue))
        answer.append(
            {
                "s_mod_4": residue,
                "delta_parity_0": row[0],
                "delta_parity_1": row[1],
                "eta": eta(s_value),
            }
        )
    return answer


def fraction_mod(value: Q, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return (
        value.numerator
        * pow(value.denominator % prime, -1, prime)
        % prime
    )


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(
        value % divisor
        for divisor in range(3, math.isqrt(value) + 1, 2)
    )


RESIDUE_CONTROLS = (
    (1, 1, 13),
    (1, 2, 17),
    (2, 1, 19),
    (2, 2, 23),
    (2, 8, 47),
    (3, 2, 29),
    (3, 4, 37),
    (4, 1, 31),
    (4, 4, 43),
    (5, 1, 37),
    (5, 2, 41),
    (6, 1, 43),
    (6, 2, 47),
    (7, 2, 53),
    (8, 2, 59),
)


def residue_controls(item229: Any) -> list[dict[str, Any]]:
    aggregates = {
        s_value: (
            alpha_coefficient(s_value),
            *beta_coefficient(s_value),
        )
        for s_value in sorted({row[0] for row in RESIDUE_CONTROLS})
    }
    answer = []
    for s_value, h_value, prime in RESIDUE_CONTROLS:
        if prime != 4 * h_value + 6 * s_value + 3:
            raise AssertionError(("row equation", s_value, h_value, prime))
        if not is_prime(prime):
            raise AssertionError(("preselected prime", prime))
        if math.gcd(clearing(s_value), prime) != 1:
            raise AssertionError(("p-unit clearing", s_value, prime))

        alpha, real, imaginary = aggregates[s_value]
        parity = h_value % 2
        sign = delta(s_value, parity)
        x_value = 2 ** (2 * s_value) * alpha
        if parity == 0:
            y_value = sign * 2 ** (5 * s_value + 2) * real
        else:
            y_value = -sign * 2 ** (5 * s_value + 2) * imaginary
        w_value = (-1) ** (h_value // 2) * 2**h_value
        residue = (
            fraction_mod(x_value, prime)
            + fraction_mod(y_value, prime) * (w_value % prime)
        ) % prime
        actual = fraction_mod(item229.phase_c(h_value), prime)
        if residue != actual:
            raise AssertionError(
                ("all-s residue", s_value, h_value, prime, residue, actual)
            )

        form = integer_form(s_value, parity, aggregates[s_value])
        if actual == 0 and form["D_s_epsilon"] % prime:
            raise AssertionError(("necessary divisor", s_value, h_value))
        answer.append(
            {
                "s": s_value,
                "h": h_value,
                "p": prime,
                "h_parity": parity,
                "delta": sign,
                "w_mod_p": w_value % prime,
                "closed_residue_mod_p": residue,
                "direct_Item229_c_mod_p": actual,
                "container_mod_p": form["D_s_epsilon"] % prime,
                "classification": (
                    "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN"
                ),
            }
        )
    return answer


def upstream_admission() -> dict[str, Any]:
    base.pin_dependencies()
    admission = base.upstream_admission()
    if (
        admission["Item264_fixed_M_normalization"]
        != "PROVED and pinned; retained ceiling 1/36 per 6M"
    ):
        raise AssertionError("Item264 admission")
    return {
        "Item307_base_sha256": BASE_HASH,
        "Item307_pinned_dependencies": base.DEPENDENCIES,
        "upstream_theorems": admission,
        "all_s_gauge_unit_extension": (
            "p=4h+6s+3>=4h+9; every gauge recurrence factor is "
            "<=4h+3 and every base/constant prime is <=11"
        ),
    }


def comparison_no_go() -> dict[str, Any]:
    # No primes are enumerated.  These are exact endpoint inequalities.
    rho = Q(1, 10)
    retained = Q(1, 6) - 2 * rho / 3
    normalized = retained / 6
    if retained != Q(1, 10) or normalized != Q(1, 60):
        raise AssertionError("comparison arithmetic")
    # If s>=rho*M, then 2s/rho>=2M>3M/2>=p_s.
    if Q(2) <= Q(3, 2):
        raise AssertionError("endpoint comparison")
    return {
        "generic_parameter": "any fixed 0<rho<1/4",
        "comparison_prime_product": (
            "P_s^(rho)=product of primes q<=2s/rho; fixed in s and M-independent"
        ),
        "comparison_linear_form": "a_tilde=b_tilde=P_s^(rho)",
        "comparison_container": (
            "D_tilde=(P_s^(rho))^2*(2^(3s+1)-delta_s_epsilon)"
        ),
        "height": "log|D_tilde|=O_rho(s)",
        "actual_index_check": (
            "s>=rho*M implies p_s<=(3M-1)/2<2s/rho, so p_s divides P_s^(rho)"
        ),
        "retained_mass": "(1/6-2rho/3)M+o(M)",
        "retained_per_6M": "1/36-rho/9+o(1)",
        "arbitrarily_small_rho_consequence": (
            "the retained coefficient approaches the raw 1/6 (1/36 per 6M)"
        ),
        "exact_rho_1_over_10_control": {
            "retained_mass_coefficient": encode_fraction(retained),
            "retained_per_6M": encode_fraction(normalized),
        },
        "scope": (
            "INFORMATION-CLASS NO-GO ONLY; the comparison family is not "
            "the actual E_h^* or D_s_epsilon sequence"
        ),
    }


def build_result() -> dict[str, Any]:
    admission = upstream_admission()
    item229 = load(
        "item308_item229",
        ROOT / "scripts/item229_j1_fixed_h_theta_certificate.py",
    )
    return {
        "schema": "item308-j1-all-s-fixed-divisor-no-go-v1",
        "item": 308,
        "title": (
            "all-s fixed divisors for the pinned j=1 orbit and the "
            "height-information no-go"
        ),
        "dependencies": admission,
        "symbolic_all_s_source_audit": symbolic_source_audit(),
        "exact_all_s_definitions": {
            "lambda": "(1+i)/2",
            "N_s": (
                "(12+(80s-4)t-(224s+8)t^2+(256s+16)t^3"
                "-(138s+9)t^4+(30s+3)t^5)/3"
            ),
            "G_s": (
                "N_s/((1-t)^(2s+6)*(t^2-2t+2)^(2s+1))"
            ),
            "aggregate_A_s": (
                "-[x^(2s+5)](1+x)^(3s+1/2)N_s(1+x)"
                "/(1+x^2)^(2s+1)"
            ),
            "aggregate_B_s": (
                "[x^(2s)](1+x)^(3s+1/2)N_s((1-i)(1+x))/"
                "(2^(2s+1)i^(2s+6)(1+i)^(2s+1)"
                "(1+(1+i)x)^(2s+6)(1+lambda*x)^(2s+1))"
            ),
            "delta": "(-1)^(s(s+1)/2+1+epsilon)=(2/p)",
            "X_s": "2^(2s)A_s",
            "Y_s_0": "delta_s_0*2^(5s+2)*Re(B_s)",
            "Y_s_1": "-delta_s_1*2^(5s+2)*Im(B_s)",
            "Lambda_s": "3*2^(10s+10)",
            "cleared_a_s": "Lambda_s*X_s",
            "cleared_b_s_epsilon": "Lambda_s*Y_s_epsilon",
            "residue": (
                "c_h^*=Lambda_s^(-1)(a_s+b_s_epsilon*w_h) mod p"
            ),
            "w_h": "(-1)^floor(h/2)*2^h",
            "container": (
                "D_s_epsilon=2^(3s+1)a_s^2-delta_s_epsilon*b_s_epsilon^2"
            ),
            "necessary_divisor": (
                "ordinary collision => E_h^*=0 => c_h^*=0 => p|D_s_epsilon"
            ),
        },
        "denominator_and_height_audit": {
            "A_s_denominator_divides": "3*2^(4s+10)",
            "B_s_coordinate_denominators_divide": "3*2^(10s+2)",
            "Lambda_prime_support": [2, 3],
            "Lambda_is_p_unit": "yes for every actual p>=13",
            "rational_source_denominator_degree": "6s+8",
            "coefficient_extraction_orders": ["2s+5", "2s"],
            "integer_container_algebraic_degree": 1,
            "height": (
                "log max(1,|a_s|,|b_s,0|,|b_s,1|,"
                "|D_s,0|,|D_s,1|)=O(s)"
            ),
            "integer_container_prime_support": (
                "UNCONTROLLED; only total logarithmic height is proved"
            ),
        },
        "Euler_sign_and_eta_cases": euler_sign_audit(),
        "bounded_exact_replay": {
            "classification": (
                "REPLAY OF THE SYMBOLIC THEOREM ONLY; NOT A SCAN INFERENCE"
            ),
            "coefficient_rows": coefficient_controls(),
            "residue_rows": residue_controls(item229),
        },
        "fixed_M_admission": {
            "S_M": "{s>=1:4s<=M-5 and s=M+1 mod 3}",
            "p_s": "(4M+2s+1)/3",
            "h_s": "(M-4s-2)/3",
            "candidate_prime_interval": "[(4M+3)/3,(3M-1)/2]",
            "raw_log_mass": "M/6+o(M)=1/36 per 6M",
            "number_of_containers": "M/12+O(1)",
            "product_height": "O(M^2), so absolute product height is inadmissible",
            "comparison_information_class_no_go": comparison_no_go(),
            "new_capacity_reduction": "ZERO",
            "retained_fixed_j1_ceiling_per_6M": "1/36",
        },
        "strict_labels": {
            "all_s_residue_and_container_formula": "PROVED",
            "all_s_denominator_p_unit_audit": "PROVED",
            "all_s_quadratic_norm_identity": "PROVED",
            "linear_log_height": "PROVED",
            "height_only_information_class_no_go": "PROVED",
            "uniform_D_nonzero_or_factor_localization": "OPEN",
            "container_weighted_density_W_D_o_M": "OPEN",
            "actual_off_ray_weighted_density_W_off_o_M": "OPEN",
            "factorization_or_prime_scan": "NONE",
            "capacity_booking": "ZERO",
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
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "item": result["item"],
                "symbolic_source": (
                    result["symbolic_all_s_source_audit"]["classification"]
                ),
                "coefficient_control_rows": len(
                    result["bounded_exact_replay"]["coefficient_rows"]
                ),
                "residue_control_rows": len(
                    result["bounded_exact_replay"]["residue_rows"]
                ),
                "capacity_reduction": (
                    result["fixed_M_admission"]["new_capacity_reduction"]
                ),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
