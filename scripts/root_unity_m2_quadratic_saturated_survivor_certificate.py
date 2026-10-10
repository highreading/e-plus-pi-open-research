#!/usr/bin/env python3
"""Exact replay for the fixed m=2 quadratic saturated survivor.

The companion source proves the all-n (n>=5) nonvanishing theorem and the
height ledger.  This replay checks the algebraic identities symbolically,
certifies the rational bound pi < 355/113 by Machin's formula and alternating
series, and reconstructs exact lower lifts and their quadratic product
survivor on a representative finite grid.  Finite height data are diagnostics
only.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import resource
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_m2_quadratic_saturated_survivor_certificate.json"
DEPENDENCY = ROOT / "scripts" / "root_unity_endpoint_displacement_square_certificate.py"
RSS_LIMIT_KIB = 2 * 1024 * 1024


def load_dependency():
    specification = importlib.util.spec_from_file_location(
        "root_unity_endpoint_displacement_dependency", DEPENDENCY
    )
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


sq = load_dependency()
X = sq.X


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arctan_partial(x: sp.Rational, last_index: int) -> sp.Rational:
    return sum(
        ((-1) ** j) * x ** (2 * j + 1) / (2 * j + 1)
        for j in range(last_index + 1)
    )


def machin_pi_upper_certificate() -> dict:
    # Machin: pi=16 atan(1/5)-4 atan(1/239).  An even-index terminal
    # partial sum is an upper bound for atan(1/5), while an odd-index
    # terminal partial sum is a lower bound for atan(1/239).
    upper = 16 * arctan_partial(sp.Rational(1, 5), 4)
    upper -= 4 * arctan_partial(sp.Rational(1, 239), 1)
    target = sp.Rational(355, 113)
    gap = sp.factor(target - upper)
    assert gap == sp.Rational(45167474711, 189820334689453125)
    assert gap > 0

    x_upper = target**2
    polynomial_at_upper = sp.factor(
        2688 * x_upper - 4416 - 227 * x_upper**2
    )
    assert polynomial_at_upper == sp.Rational(265760749, 163047361)
    assert polynomial_at_upper > 0
    return {
        "machin_upper_rational": str(upper),
        "355_over_113_minus_upper": str(gap),
        "quadratic_at_355_over_113_squared": str(polynomial_at_upper),
        "pi_less_than_355_over_113_certified": True,
    }


def fourier_ratio_anchor() -> dict:
    u = sp.symbols("u")
    pi = sp.pi
    sech = 1 / sp.cosh(u / 2)
    transform_3 = (u**2 + pi**2) * sech / (2 * pi**2)
    transform_5 = (
        sp.Rational(2, 3)
        * (u**2 / (4 * pi**2) + sp.Rational(1, 4))
        * (u**2 / (4 * pi**2) + sp.Rational(9, 4))
        * sech
    )

    def shifted_even_moment(transform: sp.Expr, n: int) -> sp.Expr:
        return sp.factor(
            sum(
                sp.binomial(n, j)
                * sp.Rational(1, 4) ** (n - j)
                * (-1) ** j
                * sp.diff(transform, u, 2 * j).subs(u, 0)
                for j in range(n + 1)
            )
        )

    i3 = shifted_even_moment(transform_3, 5)
    i5 = shifted_even_moment(transform_5, 5)
    difference = sp.factor(i3 - 3 * i5)
    expected = 5 * (2688 * pi**2 - 4416 - 227 * pi**4) / (32 * pi**4)
    assert sp.simplify(difference - expected) == 0
    return {
        "I3_at_n5": str(i3),
        "I5_at_n5": str(i5),
        "I3_minus_3I5_at_n5": str(difference),
        "strict_positivity_follows_from_pi_certificate": True,
    }


def symbolic_probability_identity() -> dict:
    alpha, beta, gamma = sp.symbols("alpha beta gamma")
    f = 1 - 8 * alpha
    k = 1 - 24 * gamma
    g = 1 - 80 * alpha + 384 * beta
    normalized_k = sp.factor(2 * f * k - (f**2 + g))
    expected_k = 16 * (
        2 * alpha
        + 20 * alpha**2
        - 24 * beta
        + (24 * alpha - 3) * (gamma - alpha)
    )
    assert sp.expand(normalized_k - expected_k) == 0

    normalized_l = sp.factor(k**2 - 4 * f * k + g + 2 * f**2)
    delta = sp.symbols("delta")
    normalized_l_delta = sp.factor(normalized_l.subs(gamma, alpha - delta) / 16)
    expected_l_delta = (
        delta * (36 * delta - 24 * alpha - 3)
        + 24 * beta
        - 2 * alpha
        - 4 * alpha**2
    )
    assert sp.expand(normalized_l_delta - expected_l_delta) == 0
    return {
        "normalized_K_identity": str(normalized_k),
        "normalized_L_identity": str(normalized_l),
        "normalized_L_after_delta_substitution": str(normalized_l_delta),
        "all_symbolic_identities_verified": True,
    }


def primitive_integer_polynomial(coefficients: list[sp.Rational]) -> tuple[list[int], sp.Rational]:
    denominator = math.lcm(*(int(sp.denom(value)) for value in coefficients))
    integral = [int(value * denominator) for value in coefficients]
    content = math.gcd(*(abs(value) for value in integral))
    assert content > 0
    primitive = [value // content for value in integral]
    if next(value for value in primitive if value) < 0:
        primitive = [-value for value in primitive]
        scale = -sp.Rational(denominator, content)
    else:
        scale = sp.Rational(denominator, content)
    assert math.gcd(*(abs(value) for value in primitive)) == 1
    return primitive, scale


def add_scaled_products(
    terms: list[tuple[sp.Rational, list[list[sp.Rational]], list[list[sp.Rational]]]],
    n: int,
) -> list[list[sp.Rational]]:
    output = sq.zero_form(5, 2 * n - 2)
    for scalar, first, second in terms:
        product = sq.exp_product(first, second)
        for frequency in range(5):
            for degree in range(2 * n - 1):
                output[frequency][degree] += scalar * product[frequency][degree]
    return output


def scale_form(
    form: list[list[sp.Rational]], scalar: sp.Rational
) -> list[list[sp.Rational]]:
    return [[sp.factor(scalar * value) for value in row] for row in form]


def rational_log(value: sp.Rational | int) -> mp.mpf:
    value = abs(sp.Rational(value))
    assert value > 0
    return mp.log(int(sp.numer(value))) - mp.log(int(sp.denom(value)))


def form_denominator(form: list[list[sp.Rational]]) -> int:
    return math.lcm(*(int(sp.denom(value)) for row in form for value in row))


def form_content_after_clearing(form: list[list[sp.Rational]], denominator: int) -> int:
    return math.gcd(
        *(abs(int(value * denominator)) for row in form for value in row)
    )


def exact_row(n: int) -> dict:
    moments = sq.logistic_moments(4 * n + 20)
    excess = sq.reduced_excess_matrix(2, n, 5, moments)
    A = sp.Rational(excess[0, 0])
    B = sp.Rational(excess[0, 2])
    C = sp.Rational(excess[0, 4])
    g1 = sp.Rational(excess[1, 1])
    g3 = sp.Rational(excess[1, 3])
    assert all(excess[q, a] == 0 for q in range(2) for a in range(5) if (q - a) % 2)

    E0 = [B, 0, -A, 0, 0]
    E1 = [C, 0, 0, 0, -A]
    O = [0, g3, 0, -g1, 0]
    for endpoint in (E0, E1, O):
        assert excess * sp.Matrix(endpoint) == sp.zeros(2, 1)

    coefficient_x = sp.factor(2 * A * g1 * g3 - B * g1**2)
    coefficient_y = sp.factor(-A * g1**2)
    coefficient_w = sp.factor(A**3)

    endpoint_expression = sp.expand(
        coefficient_x * (B - A * X**2) ** 2
        + coefficient_y * (B - A * X**2) * (C - A * X**4)
        + coefficient_w * (g3 * X - g1 * X**3) ** 2
    )
    endpoint = sp.Poly(endpoint_expression, X, domain=sp.QQ)
    assert endpoint.degree() == 2
    p0 = sp.factor(endpoint.nth(0))
    p2 = sp.factor(endpoint.nth(2))
    assert endpoint.nth(1) == 0
    assert p0 * p2 > 0

    a = 2 * abs(A)
    b = 2 * abs(B)
    c = 2 * abs(C)
    uu = 2 * abs(g1)
    v = 2 * abs(g3)
    K = sp.factor(2 * a * b * v - (b**2 + a * c) * uu)
    L = sp.factor(a**2 * v**2 - 4 * a * b * uu * v + a * c * uu**2 + 2 * b**2 * uu**2)
    assert K > 0 and L < 0
    assert abs(p0) == b * uu * K / 32
    assert abs(p2) == a * (-L) / 32

    _, interpolation, _, labels = sq.interpolation_data(2, n - 1, 4, moments)
    remainders = [
        sq.remainder_from_interpolation(2, n - 1, endpoint_vector, interpolation, labels)
        for endpoint_vector in (E0, E1, O)
    ]
    for remainder in remainders:
        assert all(sq.exp_jet(remainder, order) == 0 for order in range(2 * n + 2))

    raw_form = add_scaled_products(
        [
            (coefficient_x, remainders[0], remainders[0]),
            (coefficient_y, remainders[0], remainders[1]),
            (coefficient_w, remainders[2], remainders[2]),
        ],
        n,
    )
    assert sq.trim_polynomial(sq.endpoint_polynomial(raw_form)) == [p0, 0, p2]
    assert all(sq.exp_jet(raw_form, order) == 0 for order in range(4 * n + 4))
    exact_order = sq.exact_origin_order(raw_form, 4 * n + 4)

    primitive_endpoint, endpoint_scale = primitive_integer_polynomial([p0, 0, p2])
    primitive_form = scale_form(raw_form, endpoint_scale)
    assert [int(value) for value in sq.trim_polynomial(sq.endpoint_polynomial(primitive_form))] == primitive_endpoint

    denominator = form_denominator(primitive_form)
    global_content = form_content_after_clearing(primitive_form, denominator)
    endpoint_content_after_clearing = math.gcd(
        *(abs(value * denominator) for value in primitive_endpoint)
    )
    assert endpoint_content_after_clearing == denominator
    assert denominator % global_content == 0
    intrinsic_height = sq.form_height(primitive_form)
    cleared_primitive_height = max(
        abs(int(value * denominator // global_content))
        for row in primitive_form
        for value in row
    )
    primitive_global_endpoint_content = denominator // global_content
    assert sp.Rational(cleared_primitive_height, primitive_global_endpoint_content) == intrinsic_height

    q_n = 2 ** (2 * n) * math.factorial(n - 1)
    # The common excess-row denominator D_n makes all three kernel endpoints
    # integral.  The explicit lower cardinal formula then proves q_n clears
    # their lower lifts; the exact row verifies this divisibility directly.
    D_n = 2 ** (2 * n + 3)
    assert all(D_n % int(sp.denom(value)) == 0 for value in (A, B, C, g1, g3))
    cleared_endpoint_pair = [int(D_n**5 * p0), int(D_n**5 * p2)]
    cleared_endpoint_content = math.gcd(*(abs(value) for value in cleared_endpoint_pair))
    assert cleared_endpoint_content > 0
    cleared_endpoint_primitive = [
        value // cleared_endpoint_content for value in cleared_endpoint_pair
    ]
    if cleared_endpoint_primitive[0] < 0:
        cleared_endpoint_primitive = [-value for value in cleared_endpoint_primitive]
    assert cleared_endpoint_primitive == [primitive_endpoint[0], primitive_endpoint[2]]
    raw_rank_one_smith_numerator = q_n**2 * cleared_endpoint_content * global_content
    assert raw_rank_one_smith_numerator % denominator == 0
    raw_rank_one_smith_invariant = raw_rank_one_smith_numerator // denominator
    assert raw_rank_one_smith_invariant > 0
    integral_endpoint_remainders = [scale_form(remainder, D_n) for remainder in remainders]
    assert all(
        int(sp.denom(value)) != 0 and q_n % int(sp.denom(value)) == 0
        for remainder in integral_endpoint_remainders
        for row in remainder
        for value in row
    )
    integral_raw_form = scale_form(raw_form, D_n**5)
    assert all(
        sp.denom(value * q_n**2) == 1
        for row in integral_raw_form
        for value in row
    )

    endpoint_height = max(abs(value) for value in primitive_endpoint)
    mp.mp.dps = 100
    global_log = rational_log(intrinsic_height)
    endpoint_log = mp.log(endpoint_height)
    scale = n * mp.log(n)
    gain = (n + 3) * mp.log((n + 3) / (mp.e * mp.pi)) - (n - 1) * mp.log(mp.pi)
    threshold_margin = 2 * gain - global_log - 2 * endpoint_log

    return {
        "n": n,
        "excess_entries_A_B_C_g1_g3": [str(value) for value in (A, B, C, g1, g3)],
        "K_positive": str(K),
        "L_negative": str(L),
        "primitive_quadratic_coefficients_ascending": [str(value) for value in primitive_endpoint],
        "primitive_quadratic_height": str(endpoint_height),
        "primitive_quadratic_content": 1,
        "D_n_fifth_power_cleared_endpoint_pair": [
            str(value) for value in cleared_endpoint_pair
        ],
        "D_n_fifth_power_cleared_endpoint_content_g_n": str(cleared_endpoint_content),
        "log_g_n_over_n_log_n": mp.nstr(mp.log(cleared_endpoint_content) / scale, 35),
        "quadratic_coefficients_same_sign": True,
        "exact_global_origin_order": exact_order,
        "intrinsic_rational_global_height": str(intrinsic_height),
        "exact_global_denominator_after_endpoint_primitivization": str(denominator),
        "global_content_after_denominator_clearing": str(global_content),
        "primitive_global_endpoint_content": str(primitive_global_endpoint_content),
        "raw_rank_one_smith_invariant": str(raw_rank_one_smith_invariant),
        "raw_rank_one_smith_divides_endpoint_content": bool(
            q_n**2 * cleared_endpoint_content % raw_rank_one_smith_invariant == 0
        ),
        "intrinsic_height_equals_primitive_global_height_over_endpoint_content": True,
        "q_n": str(q_n),
        "D_n": str(D_n),
        "q_n_clears_each_integral_endpoint_lower_lift": True,
        "q_n_squared_clears_integral_raw_product_form": True,
        "log_endpoint_height_over_n_log_n": mp.nstr(endpoint_log / scale, 35),
        "log_intrinsic_global_height_over_n_log_n": mp.nstr(global_log / scale, 35),
        "centered_2G_over_n_log_n": mp.nstr(2 * gain / scale, 35),
        "rational_degree_2_measure_margin_over_n_log_n": mp.nstr(threshold_margin / scale, 35),
        "height_and_margin_values_are_finite_diagnostics_only": True,
    }


def main() -> None:
    machin = machin_pi_upper_certificate()
    fourier = fourier_ratio_anchor()
    symbolic = symbolic_probability_identity()
    rows = [exact_row(n) for n in range(5, 21)]
    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_LIMIT_KIB

    payload = {
        "schema": "root-unity-m2-quadratic-saturated-survivor-v1",
        "dependency": {
            "path": str(DEPENDENCY.relative_to(ROOT)),
            "sha256": sha256_file(DEPENDENCY),
        },
        "all_parameter_proof_anchors": {
            "machin_pi_bound": machin,
            "n5_fourier_ratio_anchor": fourier,
            "probability_identities": symbolic,
            "monotonicity_and_strict_covariance_proofs_are_in_companion_source": True,
            "proved_parameter_range": "m=2, n>=5, endpoint space Q[z]_{<=5}, target degree 2",
        },
        "exact_finite_rows": rows,
        "finite_grid": {
            "n_values": list(range(5, 21)),
            "all_quadratics_primitive_and_exact_degree_2": all(
                row["primitive_quadratic_content"] == 1
                and row["quadratic_coefficients_same_sign"]
                for row in rows
            ),
            "all_origin_orders_equal_4n_plus_4": all(
                row["exact_global_origin_order"] == 4 * row["n"] + 4
                for row in rows
            ),
            "all_degree_2_measure_margins_negative": all(
                mp.mpf(row["rational_degree_2_measure_margin_over_n_log_n"]) < 0
                for row in rows
            ),
            "finite_patterns_not_extrapolated": True,
        },
        "logical_scope": {
            "quadratic_nonvanishing_is_all_parameter": True,
            "fixed_dimension_global_height_is_exp_O_n_log_n": True,
            "leading_height_ledger_and_content_threshold_are_proved_in_source": True,
            "no_unproved_gcd_cancellation_assumed": True,
            "does_not_classify_e_plus_pi": True,
        },
        "peak_rss_checked_below_2GiB": True,
        "rss_limit_kib": RSS_LIMIT_KIB,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(OUT),
        "rows": len(rows),
        "peak_rss_kib": peak_rss_kib,
        "status": "ok",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
