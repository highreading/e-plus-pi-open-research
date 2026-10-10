#!/usr/bin/env python3
"""Exact diagnostics for the critical-Fourier 2-adic closure theorem.

The all-degree proofs are in the companion source note.  This script:

* constructs the central coefficient from the beta-moment sum;
* checks its common-denominator numerator and Kummer-transform EGF;
* checks the exact v_2 formula;
* independently reconstructs the rational coordinate from monomial
  integrals and from Gaussian-integer Fourier coefficients; and
* checks the conservative rational-coordinate valuation bound.

All finite scans are diagnostics, not substitutes for the proofs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


sys.set_int_max_str_digits(0)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def v2_integer(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0) is infinite")
    value = abs(value)
    return (value & -value).bit_length() - 1


def v2_fraction(value: Fraction) -> int | None:
    if value == 0:
        return None
    return v2_integer(value.numerator) - v2_integer(value.denominator)


def odd_double_factorial(index: int) -> int:
    if index <= 0:
        return 1
    return math.prod(range(1, index + 1, 2))


def falling(value: int, order: int) -> int:
    if order < 0:
        raise ValueError("negative falling-factorial order")
    result = 1
    for offset in range(order):
        result *= value - offset
    return result


def s_moment(m: int, ell: int) -> int:
    if m < 0 or ell < 0:
        raise ValueError("negative beta-moment index")
    value = Fraction(
        math.factorial(2 * m) * math.factorial(2 * ell),
        math.factorial(m)
        * math.factorial(ell)
        * math.factorial(m + ell),
    )
    if value.denominator != 1:
        raise AssertionError("S(m,ell) was not integral")
    return value.numerator


def central_sum(r: int, K: int) -> int:
    return sum(
        math.comb(2 * r, 2 * j) * s_moment(r + j, K - r - j)
        for j in range(r + 1)
    )


def a_product(r: int, length: int) -> int:
    return math.prod(2 * r + 1 + 2 * t for t in range(length))


def b_product(q: int, length: int) -> int:
    return math.prod(2 * q + 1 + 2 * t for t in range(length))


def common_numerator(r: int, K: int) -> tuple[int, int]:
    q = K - 2 * r
    numerator = sum(
        math.comb(2 * r, 2 * j)
        * a_product(r, j)
        * b_product(q, r - j)
        for j in range(r + 1)
    )
    denominator = b_product(q, r)
    return numerator, denominator


def egf_triple_sum(r: int, K: int) -> Fraction:
    q = K - 2 * r
    total = Fraction()
    for u in range(r + 1):
        for v in range(r - u + 1):
            w = r - u - v
            multinomial = (
                math.factorial(r)
                // (
                    math.factorial(u)
                    * math.factorial(v)
                    * math.factorial(w)
                )
            )
            total += Fraction(
                multinomial * falling(r, u) * falling(q, v),
                odd_double_factorial(2 * u - 1)
                * odd_double_factorial(2 * v - 1),
            )
    return odd_double_factorial(2 * r - 1) * total


def predicted_c0_valuation(r: int, K: int) -> int:
    return (
        r
        + K.bit_count()
        + (r & 1) * v2_integer(K)
    )


def even_rational_coordinates(K: int) -> list[Fraction]:
    """Return E_{a,k}=I_{2a,k}-(1/4) full beta, 0<=a<=K."""
    k = K + 1
    values: list[Fraction | None] = [None] * (K + 1)
    inhomogeneous_numerator = Fraction(1, 2**K)
    if K % 2 == 0:
        center = K // 2
        values[center] = Fraction()
        first_upper = center + 1
        first_lower = center
    else:
        lower_center = K // 2
        anchor = Fraction(1, (2**k) * K)
        values[lower_center] = anchor
        values[lower_center + 1] = -anchor
        first_upper = lower_center + 2
        first_lower = lower_center

    for a in range(first_upper, K + 1):
        numerator = 2 * a - 1
        denominator = 2 * k - 2 * a - 1
        previous = values[a - 1]
        assert previous is not None
        values[a] = (
            numerator * previous - inhomogeneous_numerator
        ) / denominator

    for a in range(first_lower, 0, -1):
        numerator = 2 * a - 1
        denominator = 2 * k - 2 * a - 1
        current = values[a]
        assert current is not None
        values[a - 1] = (
            denominator * current + inhomogeneous_numerator
        ) / numerator

    output = [value for value in values if value is not None]
    if len(output) != K + 1:
        raise AssertionError("incomplete even-coordinate recurrence")
    for a in range(K + 1):
        if output[a] != -output[K - a]:
            raise AssertionError("even-coordinate reflection failed")
    return output


def odd_integral(a: int, K: int) -> Fraction:
    """Return I_{2a+1,K+1} exactly."""
    lam = K - a
    if not 1 <= lam <= K:
        raise ValueError("odd-integral index outside convergence range")
    beta = Fraction(
        math.factorial(a) * math.factorial(lam - 1),
        math.factorial(K),
    )
    tail = sum(
        (
            (-1) ** j
            * math.comb(a, j)
            * Fraction(1, (2 ** (lam + j)) * (lam + j))
        )
        for j in range(a + 1)
    )
    return (beta - tail) / 2


def rational_coordinate(r: int, K: int) -> Fraction:
    even = even_rational_coordinates(K)
    value = Fraction()
    for nu in range(2 * r + 1):
        exponent = 2 * r + nu
        coefficient = (-1) ** nu * math.comb(2 * r, nu)
        if exponent % 2 == 0:
            coordinate = even[exponent // 2]
        else:
            coordinate = odd_integral((exponent - 1) // 2, K)
        value += coefficient * coordinate
    return value


Gaussian = tuple[int, int]


def gaussian_multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gaussian_power(base: Gaussian, exponent: int) -> Gaussian:
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = gaussian_multiply(result, base)
        base = gaussian_multiply(base, base)
        exponent //= 2
    return result


def polynomial_multiply(
    left: list[Gaussian], right: list[Gaussian]
) -> list[Gaussian]:
    result = [(0, 0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            product = gaussian_multiply(x, y)
            old = result[i + j]
            result[i + j] = (
                old[0] + product[0],
                old[1] + product[1],
            )
    return result


def direct_fourier_coefficients(r: int, K: int) -> list[Gaussian]:
    n = 2 * r
    ell = K - 2 * r
    first = [
        ((-1) ** (n - j) * math.comb(n, j), 0)
        for j in range(n + 1)
    ]
    second = []
    for j in range(n + 1):
        left = gaussian_power((1, 1), j)
        right = gaussian_power((1, -1), n - j)
        product = gaussian_multiply(left, right)
        second.append(
            (
                math.comb(n, j) * product[0],
                math.comb(n, j) * product[1],
            )
        )
    third = [
        (math.comb(2 * ell, j), 0)
        for j in range(2 * ell + 1)
    ]
    phase = gaussian_power((0, -1), n)
    result = polynomial_multiply(
        polynomial_multiply(first, second), third
    )
    return [gaussian_multiply(phase, value) for value in result]


def fourier_coordinates(r: int, K: int) -> tuple[int, Fraction, Fraction]:
    coefficients = direct_fourier_coefficients(r, K)
    if len(coefficients) != 2 * K + 1:
        raise AssertionError("unexpected Fourier degree")
    center = K
    c0_pair = coefficients[center]
    if c0_pair[1] != 0:
        raise AssertionError("nonreal central coefficient")
    rational_sum = Fraction()
    for m in range(1, K + 1):
        real, imag = coefficients[center + m]
        sine = (0, 1, 0, -1)[m % 4]
        cosine = (1, 0, -1, 0)[m % 4]
        rational_sum += Fraction(
            real * sine - imag * (1 - cosine), m
        )
    R = rational_sum / (2 ** (2 * K))
    Q = Fraction(c0_pair[0], 2 ** (2 * K + 2))
    return c0_pair[0], R, Q


def symbolic_polynomial_record(r: int) -> dict[str, object]:
    K_symbol = sp.symbols("K")
    q_symbol = K_symbol - 2 * r
    numerator = sp.Poly(
        sum(
            math.comb(2 * r, 2 * j)
            * a_product(r, j)
            * sp.prod(
                2 * q_symbol + 1 + 2 * t
                for t in range(r - j)
            )
            for j in range(r + 1)
        ),
        K_symbol,
        domain=sp.ZZ,
    )
    divisor = (2**r) * (
        K_symbol if r % 2 else 1
    )
    quotient, remainder = sp.div(
        numerator,
        sp.Poly(divisor, K_symbol, domain=sp.ZZ),
        domain=sp.ZZ,
    )
    if remainder.as_expr() != 0:
        raise AssertionError("symbolic normalized polynomial remainder")
    coefficients = [int(value) for value in quotient.all_coeffs()]
    if math.gcd(*[abs(value) for value in coefficients]) % 2 == 0:
        raise AssertionError("symbolic quotient has even content")
    for K in range(0, 2 * r + 20):
        if int(quotient.eval(K)) % 2 != 1:
            raise AssertionError("normalized polynomial not odd-valued")
    return {
        "r": r,
        "degree": quotient.degree(),
        "coefficient_sha256": sha256_text(
            json.dumps(coefficients, separators=(",", ":"))
        ),
        "leading_coefficients": [
            str(value) for value in coefficients[: min(4, len(coefficients))]
        ],
        "constant_coefficient": str(coefficients[-1]),
    }


def exponential_pair(n: int) -> tuple[int, int]:
    """Return the accepted primitive pair (p_n,q_n) with q_n e-p_n>0."""
    if n == 0:
        return 1, 1
    p_previous, q_previous = 1, 1
    p_current, q_current = 3, 1
    if n == 1:
        return p_current, q_current
    for index in range(2, n + 1):
        multiplier = 2 * (2 * index - 1)
        p_previous, p_current = (
            p_current,
            multiplier * p_current + p_previous,
        )
        q_previous, q_current = (
            q_current,
            multiplier * q_current + q_previous,
        )
    return p_current, q_current


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/independent_critical_fourier_two_adic_closure.json"
        ),
    )
    args = parser.parse_args()

    central_cases = 0
    central_stream = hashlib.sha256()
    for r in range(1, 13):
        for K in range(2 * r, 121):
            c0 = central_sum(r, K)
            numerator, denominator = common_numerator(r, K)
            base = s_moment(r, K - r)
            if c0 * denominator != base * numerator:
                raise AssertionError("central common-denominator identity")
            if Fraction(numerator, 2**r) != egf_triple_sum(r, K):
                raise AssertionError("Kummer-transform EGF identity")
            if v2_integer(c0) != predicted_c0_valuation(r, K):
                raise AssertionError("central v2 formula")
            normalized = Fraction(
                numerator,
                (2**r) * (K if r % 2 else 1),
            )
            if normalized.denominator != 1 or normalized.numerator % 2 != 1:
                raise AssertionError("normalized numerator not odd")
            central_stream.update(
                (
                    f"{r},{K},{c0},{numerator},{denominator},"
                    f"{v2_integer(c0)}\n"
                ).encode()
            )
            central_cases += 1

    polynomial_records = [
        symbolic_polynomial_record(r) for r in range(1, 13)
    ]

    coordinate_cases = 0
    zero_rational_coordinates: list[list[int]] = []
    minimum_valuation_slack: int | None = None
    coordinate_stream = hashlib.sha256()
    for r in range(1, 11):
        for K in range(2 * r, 81):
            R = rational_coordinate(r, K)
            valuation = v2_fraction(R)
            lower_bound = -(K + 1) - (K.bit_length() - 1)
            if valuation is None:
                zero_rational_coordinates.append([r, K])
                valuation_text = "infinity"
            else:
                if valuation < lower_bound:
                    raise AssertionError("rational-coordinate v2 bound")
                slack = valuation - lower_bound
                if minimum_valuation_slack is None:
                    minimum_valuation_slack = slack
                else:
                    minimum_valuation_slack = min(
                        minimum_valuation_slack, slack
                    )
                valuation_text = str(valuation)

                c0 = central_sum(r, K)
                Q = Fraction(c0, 2 ** (2 * K + 2))
                ratio = R / Q
                exact_lower = (
                    (K + 1)
                    - r
                    - K.bit_count()
                    - (r & 1) * v2_integer(K)
                    - (K.bit_length() - 1)
                )
                ratio_valuation = v2_fraction(ratio)
                assert ratio_valuation is not None
                if ratio_valuation < exact_lower:
                    raise AssertionError("ratio valuation consequence")

            coordinate_stream.update(
                f"{r},{K},{R.numerator}/{R.denominator},{valuation_text}\n".encode()
            )
            coordinate_cases += 1

    fourier_spots = [
        (1, 2),
        (1, 9),
        (2, 4),
        (2, 15),
        (3, 6),
        (3, 18),
        (4, 12),
        (5, 15),
        (6, 20),
    ]
    fourier_records: list[dict[str, object]] = []
    for r, K in fourier_spots:
        c0_direct, R_direct, Q_direct = fourier_coordinates(r, K)
        c0_sum = central_sum(r, K)
        R_monomial = rational_coordinate(r, K)
        Q_sum = Fraction(c0_sum, 2 ** (2 * K + 2))
        if (c0_direct, R_direct, Q_direct) != (
            c0_sum,
            R_monomial,
            Q_sum,
        ):
            raise AssertionError("independent Fourier/monomial mismatch")
        fourier_records.append(
            {
                "r": r,
                "K": K,
                "n": 2 * r,
                "k": K + 1,
                "C0": str(c0_direct),
                "R": f"{R_direct.numerator}/{R_direct.denominator}",
                "Q": f"{Q_direct.numerator}/{Q_direct.denominator}",
                "v2_R": (
                    v2_fraction(R_direct)
                    if R_direct
                    else "infinity"
                ),
            }
        )

    # Exact warning example: primitive component divergence alone cannot
    # control the final content after matching.
    warning_r, warning_K = 1, 9
    warning_R = rational_coordinate(warning_r, warning_K)
    warning_Q = Fraction(
        central_sum(warning_r, warning_K),
        2 ** (2 * warning_K + 2),
    )
    warning_ratio = warning_R / warning_Q
    warning_A = warning_ratio.numerator
    warning_B = warning_ratio.denominator
    warning_p, warning_q = exponential_pair(2 * warning_r)
    warning_d = math.gcd(warning_q, warning_B)
    warning_u = warning_B // warning_d
    warning_v = warning_q // warning_d
    warning_constant = (
        -warning_u * warning_p + warning_v * warning_A
    )
    warning_coefficient = warning_u * warning_q
    warning_content = math.gcd(
        abs(warning_constant), warning_coefficient
    )
    if (warning_d, warning_content) != (7, 7):
        raise AssertionError("matching-content warning example changed")

    # This is only a scale diagnostic for the analytic lower bound.  Writing
    # n=10^p avoids constructing astronomically large integers.
    high_scale_records: list[dict[str, object]] = []
    gamma = (1 + math.sqrt(2)) / 2
    for decimal_exponent in (50, 100, 200, 500, 1000):
        log_n = decimal_exponent * math.log(10)
        x = log_n / 35
        normalized_main_lower = (
            (x - 0.5) * math.log(2)
            - 0.5 * math.log(x)
            - math.log(4)
            - 1 / math.sqrt(x)
            - 0.25
            - math.log(gamma)
        )
        high_scale_records.append(
            {
                "n": f"10^{decimal_exponent}",
                "threshold_k_over_n": format(x, ".15f"),
                "normalized_log_lower_main_terms": format(
                    normalized_main_lower, ".15f"
                ),
            }
        )

    result = {
        "description": (
            "Independent exact diagnostics for the critical-Fourier "
            "central v2 identity and rational-coordinate bound"
        ),
        "status": (
            "all-degree proofs are in the companion note; every scan "
            "reported here is finite"
        ),
        "central_coefficient_checks": {
            "range": "1<=r<=12, 2r<=K<=120",
            "case_count": central_cases,
            "all_beta_sum_common_denominator_identities_pass": True,
            "all_kummer_transform_egf_identities_pass": True,
            "all_exact_v2_formulas_pass": True,
            "all_normalized_numerators_are_odd_integers": True,
            "record_stream_sha256": central_stream.hexdigest(),
            "symbolic_polynomial_records": polynomial_records,
        },
        "rational_coordinate_checks": {
            "range": "1<=r<=10, 2r<=K<=80",
            "case_count": coordinate_cases,
            "all_v2_R_lower_bounds_pass": True,
            "all_ratio_valuation_consequences_pass": True,
            "minimum_finite_valuation_slack": minimum_valuation_slack,
            "zero_rational_coordinates": zero_rational_coordinates,
            "record_stream_sha256": coordinate_stream.hexdigest(),
        },
        "independent_fourier_monomial_spot_checks": fourier_records,
        "matching_content_warning_example": {
            "n": 2,
            "k": 10,
            "primitive_pi_pair_A_B": [
                str(warning_A),
                str(warning_B),
            ],
            "primitive_e_pair_minus_p_q": [
                str(-warning_p),
                str(warning_q),
            ],
            "matching_gcd_d": warning_d,
            "raw_matched_constant": str(warning_constant),
            "raw_common_e_pi_coefficient": str(warning_coefficient),
            "final_content": warning_content,
            "conclusion": (
                "parity does not force final content one; primitive pi "
                "divergence alone does not prove matched-form divergence"
            ),
        },
        "high_scale_analytic_diagnostic": {
            "role": (
                "floating diagnostic only; the uniform high-k limit is "
                "proved symbolically in the note"
            ),
            "records": high_scale_records,
        },
        "warnings": [
            (
                "The finite absence or presence of R=0 cannot be "
                "extrapolated.  The theorem handles R=0 separately."
            ),
            (
                "The primitive pi form equals pi when R=0; only the "
                "subsequently matched primitive e+pi form diverges there."
            ),
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "central_cases": central_cases,
                "coordinate_cases": coordinate_cases,
                "fourier_spot_count": len(fourier_records),
                "zero_rational_coordinate_count": len(
                    zero_rational_coordinates
                ),
                "central_record_stream_sha256": central_stream.hexdigest(),
                "coordinate_record_stream_sha256": coordinate_stream.hexdigest(),
            },
            indent=2,
            sort_keys=True,
        )
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
