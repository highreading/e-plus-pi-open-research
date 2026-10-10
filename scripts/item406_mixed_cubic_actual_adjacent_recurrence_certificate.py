#!/usr/bin/env python3
"""Deterministic certificate for Item 406.

The report proves the all-q Hermite identities, the local ideal equivalence,
the diagonal-kernel and direct actual-row formulas, and the compatible-prime
reciprocal reduction.  This standard-library replay checks those formulas with
exact arithmetic and verifies the pinned canonical dependencies.  Its finite
rows are normalization controls only; no finite prime scan is used as evidence
for a support theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

DEPENDENCIES = {
    "sources/mixed_cubic_connection_determinant_3adic_nonvanishing.md":
        "984445948c10e423cf752af580c80345b6d3d861c41db043312d49c1e81dedcc",
    "sources/mixed_cubic_cube_smith_reduction.md":
        "b44cc15d1a846d5298d61b9e53539116b31bbab0338dbc6e320fb0a875b0d0a0",
    "sources/item387_mixed_kernel_quotient_and_claim_audit_report.md":
        "061e29589d427ccb5c8549c8344781c0c8f0e674d2fa525da03325312ce40625",
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "sources/item393_mixed_cubic_small_prime_strata_ceiling_report.md":
        "5e2c92f87075cbe3ac8af3191d8df7485ac6efd13609ede5f82819e355ae5f96",
    "sources/item396_fixed_gap_resultant_3adic_report.md":
        "7355b6909994357583f799e627e1ff19edb230a6a9002ee845be585057726aca",
    "sources/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_report.md":
        "245bf2e557dd81ac88c94e9d0adc8990f203e3ab40680d23bd50f8e435240c48",
    "scripts/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_certificate.py":
        "90c7f5d38b168e9999b220e52d565fb77faa4b9872b2ffb70a66387f1caecd3a",
    "results/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_certificate.json":
        "c7516c720ba6a3bdb0f8803f0199fb6d137f593d3ef07fc9cd2205a73eb2a1fa",
    "manifests/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_manifest.json":
        "71ad98ae5ff23cca6ebc32ad534879e6fac29ec0cbcb034838412f25e2f98f68",
    "results/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_root_audit.json":
        "a8cdc2a03f597ddcac48119b9afd5c331597dff6e0f035491d8db4753a1ee80d",
}

SERIES_ORDER = 24
NORMALIZATION_Q = (1, 5, 7, 11, 13, 25, 37, 43, 49)
COMPATIBLE_NORMALIZATION = ((5, 11), (7, 13), (13, 31))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_dependencies() -> dict[str, str]:
    observed = {}
    for relative, expected in DEPENDENCIES.items():
        digest = sha256_bytes((ROOT / relative).read_bytes())
        assert digest == expected, (relative, expected, digest)
        observed[relative] = digest
    return observed


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= value - index
    return answer / math.factorial(degree)


def h_power_coefficients(parameter: int, degree: int) -> list[Fraction]:
    """Coefficients of H(z)^(parameter/3), H=1+2z+3z^2/2+z^3/2."""
    exponent = Fraction(parameter, 3)
    polynomial = (Fraction(1), Fraction(2), Fraction(3, 2), Fraction(1, 2))
    coefficients = [Fraction(1)]
    for target in range(1, degree + 1):
        total = Fraction(0)
        for index in range(1, min(3, target) + 1):
            total += (
                ((exponent + 1) * index - target)
                * polynomial[index]
                * coefficients[target - index]
            )
        coefficients.append(total / target)
    return coefficients


def negative_power_with_polynomial(q_value: int, degree: int, shift: int) -> int:
    polynomial_degree = 1 + 3 * shift
    return sum(
        math.comb(polynomial_degree, index)
        * math.comb(q_value + degree - index - 1, degree - index)
        for index in range(min(polynomial_degree, degree) + 1)
    )


def actual_fixed_gap_coefficients(q_value: int) -> tuple[Fraction, ...]:
    """Independent replay of canonical C0,T0,C1,T1 definitions."""
    n_value = q_value - 1
    half_n = n_value // 2
    parameter = 2 * q_value - 3

    full_zero = h_power_coefficients(parameter, n_value)
    c_zero = 2 * full_zero[n_value]
    if n_value:
        c_zero += full_zero[n_value - 1]

    full_one = h_power_coefficients(parameter - 3, n_value)
    c_one = Fraction(0)
    for index in range(min(4, n_value) + 1):
        c_one += (
            Fraction(math.comb(4, index) * 2 ** (4 - index), 2)
            * full_one[n_value - index]
        )

    exponent_zero = Fraction(parameter, 3)
    exponent_one = exponent_zero - 1
    binomial_zero = Fraction(1)
    binomial_one = Fraction(1)
    t_zero = Fraction(0)
    t_one = Fraction(0)
    for index in range(half_n + 1):
        remaining = n_value - 2 * index
        t_zero += binomial_zero * negative_power_with_polynomial(
            q_value, remaining, 0
        )
        t_one += binomial_one * negative_power_with_polynomial(
            q_value, remaining, 1
        )
        binomial_zero *= (exponent_zero - index) / (index + 1)
        binomial_one *= (exponent_one - index) / (index + 1)
    return c_zero, t_zero, c_one, t_one


def base_adjacent_coefficients(q_value: int) -> tuple[Fraction, ...]:
    """Return a_n,a_(n-1),b_n,b_(n-1) in the report's notation."""
    n_value = q_value - 1
    parameter = 2 * q_value - 3
    exponent = Fraction(parameter, 3)
    h_coefficients = h_power_coefficients(parameter, n_value)
    a_value = h_coefficients[n_value]
    a_previous = h_coefficients[n_value - 1] if n_value else Fraction(0)

    b_coefficients = []
    for degree in range(n_value + 1):
        total = Fraction(0)
        for half_degree in range(degree // 2 + 1):
            total += generalized_binomial(exponent, half_degree) * math.comb(
                q_value + degree - 2 * half_degree - 1,
                degree - 2 * half_degree,
            )
        b_coefficients.append(total)
    b_value = b_coefficients[n_value]
    b_previous = b_coefficients[n_value - 1] if n_value else Fraction(0)
    return a_value, a_previous, b_value, b_previous


def hermite_normalization_rows() -> list[dict[str, object]]:
    rows = []
    for q_value in NORMALIZATION_Q:
        n_value = q_value - 1
        a_factor = 2 * n_value - 1
        a_value, a_previous, b_value, b_previous = base_adjacent_coefficients(q_value)
        c_zero, t_zero, c_one, t_one = actual_fixed_gap_coefficients(q_value)
        assert c_zero == 2 * a_value + a_previous
        assert a_factor * c_one == (5 * n_value - 1) * c_zero - 6 * a_value
        assert t_zero == b_value + b_previous
        assert a_factor * t_one == (5 * n_value - 7) * t_zero + 6 * b_value

        c_matrix = ((2, 1), (10 * n_value - 8, 5 * n_value - 1))
        t_matrix = ((1, 1), (5 * n_value - 1, 5 * n_value - 7))
        c_determinant = c_matrix[0][0] * c_matrix[1][1] - c_matrix[0][1] * c_matrix[1][0]
        t_determinant = t_matrix[0][0] * t_matrix[1][1] - t_matrix[0][1] * t_matrix[1][0]
        assert c_determinant == 6
        assert t_determinant == -6
        witness = ":".join(
            str(value)
            for value in (
                q_value,
                a_value,
                a_previous,
                b_value,
                b_previous,
                c_zero,
                t_zero,
                c_one,
                t_one,
            )
        ).encode("ascii")
        rows.append(
            {
                "q": q_value,
                "n": n_value,
                "A=2n-1": a_factor,
                "C_change_determinant": c_determinant,
                "T_change_determinant": t_determinant,
                "row_sha256": sha256_bytes(witness),
                "normalization_only_not_support_evidence": True,
            }
        )
    return rows


# Truncated exact series helpers, coefficients in ascending order.
def zero_series(order: int = SERIES_ORDER) -> list[Fraction]:
    return [Fraction(0) for _ in range(order + 1)]


def constant_series(value: Fraction | int, order: int = SERIES_ORDER) -> list[Fraction]:
    answer = zero_series(order)
    answer[0] = Fraction(value)
    return answer


def series_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [x_value + y_value for x_value, y_value in zip(left, right)]


def series_scale(series: list[Fraction], scalar: Fraction | int) -> list[Fraction]:
    scalar = Fraction(scalar)
    return [scalar * value for value in series]


def series_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    order = len(left) - 1
    answer = zero_series(order)
    for i, x_value in enumerate(left):
        if not x_value:
            continue
        for j, y_value in enumerate(right[: order + 1 - i]):
            answer[i + j] += x_value * y_value
    return answer


def series_power(series: list[Fraction], exponent: int) -> list[Fraction]:
    answer = constant_series(1, len(series) - 1)
    base = series[:]
    while exponent:
        if exponent & 1:
            answer = series_multiply(answer, base)
        base = series_multiply(base, base)
        exponent //= 2
    return answer


def series_shift(series: list[Fraction], degree: int) -> list[Fraction]:
    order = len(series) - 1
    if degree > order:
        return zero_series(order)
    return [Fraction(0)] * degree + series[: order + 1 - degree]


def series_inverse(series: list[Fraction]) -> list[Fraction]:
    order = len(series) - 1
    assert series[0]
    answer = zero_series(order)
    answer[0] = 1 / series[0]
    for degree in range(1, order + 1):
        answer[degree] = -sum(
            series[index] * answer[degree - index]
            for index in range(1, degree + 1)
        ) / series[0]
    return answer


def series_divide(numerator: list[Fraction], denominator: list[Fraction]) -> list[Fraction]:
    return series_multiply(numerator, series_inverse(denominator))


def series_polynomial(variable: list[Fraction], coefficients: tuple[Fraction, ...]) -> list[Fraction]:
    answer = zero_series(len(variable) - 1)
    power = constant_series(1, len(variable) - 1)
    for coefficient in coefficients:
        answer = series_add(answer, series_scale(power, coefficient))
        power = series_multiply(power, variable)
    return answer


A_RESULTANT_TERMS = (
    (9, 6, 16), (7, 4, -216), (6, 6, -216), (6, 3, 216),
    (5, 2, 729), (4, 4, 4374), (4, 1, -1458), (3, 6, 34722),
    (3, 3, -10206), (3, 0, 729), (2, 2, 6561), (1, 4, 2916),
    (0, 6, -1458), (0, 3, 1458),
)

B_RESULTANT_TERMS = (
    (9, 6, 1024), (7, 4, 1152), (6, 6, -3456), (5, 2, 324),
    (4, 4, 648), (3, 6, 138888), (3, 3, -7668), (2, 2, 2187),
    (1, 4, 16038), (1, 1, -2916), (0, 6, -1458), (0, 3, 729),
    (0, 0, 729),
)


def evaluate_bivariate_resultant(
    y_series: list[Fraction], terms: tuple[tuple[int, int, int], ...]
) -> list[Fraction]:
    order = len(y_series) - 1
    powers = {degree: series_power(y_series, degree) for degree in {term[1] for term in terms}}
    answer = zero_series(order)
    for x_degree, y_degree, coefficient in terms:
        answer = series_add(
            answer,
            series_scale(series_shift(powers[y_degree], x_degree), coefficient),
        )
    return answer


def algebraic_kernel_check() -> dict[str, object]:
    a_values = []
    a_previous_values = []
    b_values = []
    b_previous_values = []
    for n_value in range(SERIES_ORDER + 1):
        row = base_adjacent_coefficients(n_value + 1)
        a_values.append(row[0])
        a_previous_values.append(row[1])
        b_values.append(row[2])
        b_previous_values.append(row[3])

    w_c = series_divide(a_previous_values, a_values)
    w_t = series_divide(b_previous_values, b_values)
    x_series = zero_series()
    x_series[1] = Fraction(1)

    h_of_wc = series_polynomial(
        w_c, (Fraction(1), Fraction(2), Fraction(3, 2), Fraction(1, 2))
    )
    hp_of_wc = series_polynomial(
        w_c, (Fraction(2), Fraction(3), Fraction(3, 2))
    )
    d_c = series_add(
        series_scale(h_of_wc, 3),
        series_scale(series_multiply(w_c, hp_of_wc), -2),
    )
    c_kernel = series_add(
        series_power(w_c, 3),
        series_scale(series_shift(series_power(h_of_wc, 2), 3), -1),
    )
    c_rational = series_add(
        series_shift(series_multiply(d_c, a_values), 1),
        series_scale(w_c, -3),
    )
    assert not any(c_kernel)
    assert not any(c_rational)

    one_plus_wt_squared = series_polynomial(
        w_t, (Fraction(1), Fraction(0), Fraction(1))
    )
    one_minus_wt = series_add(constant_series(1), series_scale(w_t, -1))
    d_t = series_polynomial(
        w_t, (Fraction(3), Fraction(-6), Fraction(-1), Fraction(-2))
    )
    t_kernel = series_add(
        series_multiply(series_power(w_t, 3), series_power(one_minus_wt, 3)),
        series_scale(series_shift(series_power(one_plus_wt_squared, 2), 3), -1),
    )
    t_rational = series_add(
        series_shift(series_multiply(d_t, b_values), 1),
        series_scale(series_multiply(w_t, one_minus_wt), -3),
    )
    assert not any(t_kernel)
    assert not any(t_rational)

    a_resultant = evaluate_bivariate_resultant(a_values, A_RESULTANT_TERMS)
    b_resultant = evaluate_bivariate_resultant(b_values, B_RESULTANT_TERMS)
    assert not any(a_resultant)
    assert not any(b_resultant)

    # Direct diagonal formulas for the four actual coefficient rows.  These
    # checks are separate from the adjacent-basis identities: in particular,
    # algebraicity of C1 and T1 is not inferred by formally integrating an
    # Euler equation.
    actual_rows = [
        actual_fixed_gap_coefficients(n_value + 1)
        for n_value in range(SERIES_ORDER + 1)
    ]
    c_zero_values = [row[0] for row in actual_rows]
    t_zero_values = [row[1] for row in actual_rows]
    c_one_values = [row[2] for row in actual_rows]
    t_one_values = [row[3] for row in actual_rows]

    two_plus_wc = series_add(constant_series(2), w_c)
    one_plus_wt = series_add(constant_series(1), w_t)
    c_zero_direct = series_add(
        series_shift(series_multiply(d_c, c_zero_values), 1),
        series_scale(series_multiply(w_c, two_plus_wc), -3),
    )
    c_one_direct = series_add(
        series_scale(
            series_shift(
                series_multiply(
                    series_multiply(h_of_wc, d_c), c_one_values
                ),
                1,
            ),
            2,
        ),
        series_scale(
            series_multiply(w_c, series_power(two_plus_wc, 4)), -3
        ),
    )
    t_zero_direct = series_add(
        series_shift(series_multiply(d_t, t_zero_values), 1),
        series_scale(
            series_multiply(
                series_multiply(w_t, one_minus_wt), one_plus_wt
            ),
            -3,
        ),
    )
    t_one_direct = series_add(
        series_shift(
            series_multiply(
                series_multiply(one_plus_wt_squared, d_t), t_one_values
            ),
            1,
        ),
        series_scale(
            series_multiply(
                series_multiply(w_t, one_minus_wt),
                series_power(one_plus_wt, 4),
            ),
            -3,
        ),
    )
    assert not any(c_zero_direct)
    assert not any(c_one_direct)
    assert not any(t_zero_direct)
    assert not any(t_one_direct)

    witness = json.dumps(
        {
            "a": [str(value) for value in a_values],
            "a_previous": [str(value) for value in a_previous_values],
            "b": [str(value) for value in b_values],
            "b_previous": [str(value) for value in b_previous_values],
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("ascii")
    return {
        "series_order": SERIES_ORDER,
        "C_kernel": "w_C^3=x^3*H(w_C)^2",
        "C_base_generating_function": "A0=3*w_C/(x*(3H-2w_C H'))",
        "C_adjacent_generating_function": "A1=w_C*A0",
        "T_kernel": "w_T^3*(1-w_T)^3=x^3*(1+w_T^2)^2",
        "T_base_generating_function": "B0=3*w_T*(1-w_T)/(x*(3-6w_T-w_T^2-2w_T^3))",
        "T_adjacent_generating_function": "B1=w_T*B0",
        "actual_C0_generating_function": "C0=3*w_C*(2+w_C)/(x*D_C)",
        "actual_C1_generating_function": "C1=3*w_C*(2+w_C)^4/(2*x*H(w_C)*D_C)",
        "actual_T0_generating_function": "T0=3*w_T*(1-w_T)*(1+w_T)/(x*D_T)",
        "actual_T1_generating_function": "T1=3*w_T*(1-w_T)*(1+w_T)^4/(x*(1+w_T^2)*D_T)",
        "all_four_direct_actual_row_formulas_vanish_to_replay_order": True,
        "both_degree_six_resultants_vanish_to_replay_order": True,
        "normalization_only_not_uniform_proof": True,
        "series_witness_sha256": sha256_bytes(witness),
    }


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def truncated_multiply_mod(
    left: list[int], right: list[int], degree: int, prime: int
) -> list[int]:
    answer = [0] * (degree + 1)
    for i, x_value in enumerate(left[: degree + 1]):
        for j, y_value in enumerate(right[: degree + 1 - i]):
            answer[i + j] = (answer[i + j] + x_value * y_value) % prime
    return answer


def negative_binomial_mod(exponent: int, degree: int, prime: int) -> list[int]:
    coefficients = [1]
    for index in range(1, degree + 1):
        coefficients.append(
            coefficients[-1]
            * (exponent + index - 1)
            * pow(index, -1, prime)
            % prime
        )
    return coefficients


def one_plus_negative_power(exponent: int, degree: int, prime: int) -> list[int]:
    """Coefficients of (1+z)^(-exponent)."""
    return [
        value * (-1) ** index % prime
        for index, value in enumerate(negative_binomial_mod(exponent, degree, prime))
    ]


def positive_one_minus_power(exponent: int, degree: int, prime: int) -> list[int]:
    answer = [0] * (degree + 1)
    for index in range(min(exponent, degree) + 1):
        answer[index] = math.comb(exponent, index) * (-1) ** index % prime
    return answer


def even_negative_power(exponent: int, degree: int, prime: int) -> list[int]:
    answer = [0] * (degree + 1)
    base = negative_binomial_mod(exponent, degree // 2, prime)
    for index, value in enumerate(base):
        if 2 * index <= degree:
            answer[2 * index] = value * (-1) ** index % prime
    return answer


def compatible_reciprocal_rows() -> list[dict[str, object]]:
    rows = []
    for q_value, prime in COMPATIBLE_NORMALIZATION:
        assert prime > q_value and (prime - q_value) % 6 == 0
        m_value = (prime - q_value) // 6
        n_value = q_value - 1
        k_value = 4 * m_value + 1
        a_factor = 2 * q_value - 3
        assert a_factor * pow(3, -1, prime) % prime == (-k_value) % prime
        assert a_factor % prime

        a_value, a_previous, b_value, b_previous = base_adjacent_coefficients(q_value)
        r_series = truncated_multiply_mod(
            positive_one_minus_power(6 * m_value, n_value, prime),
            even_negative_power(k_value, n_value, prime),
            n_value,
            prime,
        )
        s_series = truncated_multiply_mod(
            r_series,
            one_plus_negative_power(k_value, n_value, prime),
            n_value,
            prime,
        )
        assert fraction_mod(b_value, prime) == r_series[n_value]
        assert fraction_mod(b_previous, prime) == (r_series[n_value - 1] if n_value else 0)
        assert fraction_mod(a_previous, prime) == (
            pow(2, 1 - n_value, prime) * (s_series[n_value - 1] if n_value else 0)
        ) % prime
        assert fraction_mod(a_value, prime) == (
            pow(2, -n_value, prime)
            * (s_series[n_value] - (s_series[n_value - 1] if n_value else 0))
        ) % prime
        rows.append(
            {
                "q": q_value,
                "p": prime,
                "m": m_value,
                "n": n_value,
                "k": k_value,
                "alpha_mod_p": (-k_value) % prime,
                "R_adjacent": [
                    r_series[n_value - 1] if n_value else 0,
                    r_series[n_value],
                ],
                "S_adjacent": [
                    s_series[n_value - 1] if n_value else 0,
                    s_series[n_value],
                ],
                "normalization_only_not_prime_scan": True,
            }
        )
    return rows


def run() -> dict[str, object]:
    dependencies = verify_dependencies()
    hermite_rows = hermite_normalization_rows()
    kernel = algebraic_kernel_check()
    compatible_rows = compatible_reciprocal_rows()
    witness = json.dumps(
        {
            "hermite": hermite_rows,
            "kernel": kernel,
            "compatible": compatible_rows,
            "dependencies": dependencies,
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return {
        "schema": "item406-actual-adjacent-recurrence-v1",
        "item": 406,
        "status": "CANONICAL_ROOT_AUDITED_NO_BOOKING",
        "labels": {
            "PROVED": [
                "all-q coefficientwise Hermite identities for the actual C and T pairs",
                "local ideal equivalence between actual coefficient pairs and four adjacent base diagonals away from 6(2q-3)",
                "degree-six algebraic diagonal kernels, direct actual-row formulas, and exact Euler-operator recurrences",
                "compatible-prime Frobenius/Cayley reduction to adjacent coefficients of R and S for q>=5, with q=1 trivial",
            ],
            "CONDITIONAL": [
                "the four-adjacent nonvanishing lemma would exclude compatible primes from H_q",
                "the combined unmarked H and primitive-G support theorem would give c_m^>=1 and is stronger than the marked target in q=1 mod 6",
            ],
            "OPEN": [
                "exclusion of simultaneous vanishing of the two adjacent R and S pairs for every compatible prime with m>=1 and q>=5",
                "H_q divides P_q with multiplicities",
                "primitive G_q support after H_q is removed",
                "the distinguished marked cube-root branch in q=1 mod 6",
                "H_q*G_q^prim divides P_q",
                "Route 1 and irrationality of e+pi",
            ],
        },
        "exact_change_matrices": {
            "C": "[[2,1],[10n-8,5n-1]], determinant 6",
            "T": "[[1,1],[5n-1,5n-7]], determinant -6",
        },
        "smallest_missing_H_only_lemma": (
            "For p=6m+q prime with m>=1 and q>=5, n=q-1, k=4m+1, R=(1-z)^(6m)/(1+z^2)^k "
            "and S=R/(1+z)^k, the coefficient pairs at degrees n-1,n are not "
            "simultaneously zero for both R and S modulo p."
        ),
        "hermite_normalization_rows": hermite_rows,
        "algebraic_kernel_replay": kernel,
        "compatible_reciprocal_normalization_rows": compatible_rows,
        "dependency_sha256": dependencies,
        "capacity": {
            "booking_delta": 0,
            "frozen_booked_deficit_unchanged": "1.0196329836694317938803064012",
            "combined_large_component_ceiling": "log(136)/6 = 0.8187758142893420014168718304...",
            "admission_residual_after_granting_full_large_ceiling": "0.2008571693800897924634345708...",
            "H_only_success_numeric_ceiling_reduction": 0,
            "reason": "primitive G can still occupy the full combined Item390 ceiling; no disjoint positive lower bound is known",
        },
        "assertions": {
            "no_isolated_prime_scan_used_as_progress": True,
            "ambient_perturbations_excluded": True,
            "actual_rows_distinguished_from_formal_extension_indices": True,
            "all_finite_rows_are_normalization_only": True,
            "booking_delta_is_zero": True,
        },
        "witness_sha256": sha256_bytes(witness),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results" / "item406_mixed_cubic_actual_adjacent_recurrence_certificate.json",
    )
    parser.add_argument("--replay", type=Path)
    arguments = parser.parse_args()
    payload = run()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if arguments.replay is not None:
        frozen = arguments.replay.read_bytes()
        if frozen != rendered:
            raise AssertionError("replay payload differs from frozen certificate")
    print(sha256_bytes(rendered))
    arguments.output.write_bytes(rendered)


if __name__ == "__main__":
    main()
