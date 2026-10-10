#!/usr/bin/env python3
"""Exploratory exact Gosper certificate search for Item312.

Discovery only until the returned rational certificate is independently
verified as an identity in Q(s,m).
"""

from __future__ import annotations

import os
import json
import time

import sympy as S
from sympy.concrete.gosper import gosper_normal


s, m, x, t = S.symbols("s m x t", integer=True)
N0 = (
    4
    - S.Rational(4, 3) * t
    - S.Rational(8, 3) * t**2
    + S.Rational(16, 3) * t**3
    - 3 * t**4
    + t**5
)
N1 = (
    S.Rational(80, 3) * t
    - S.Rational(224, 3) * t**2
    + S.Rational(256, 3) * t**3
    - 46 * t**4
    + 10 * t**5
)
M = S.Poly(S.expand((N0 + s * N1).subs(t, 1 + x)), x)
alpha = 3 * s + S.Rational(1, 2)
k_lower = 2 * s + 5 - 2 * m
contiguous = S.Integer(0)
for degree in range(6):
    coefficient = M.coeff_monomial(x**degree)
    if degree:
        quotient = S.prod(k_lower - j for j in range(degree)) / S.prod(
            alpha - k_lower + 1 + j for j in range(degree)
        )
    else:
        quotient = S.Integer(1)
    contiguous += coefficient * quotient
contiguous = S.factor(contiguous)

summand = (
    -(-1) ** m
    * S.binomial(2 * s + m, m)
    * S.binomial(alpha, k_lower)
    * contiguous
)
print("summand_ready", flush=True)

n = s
operators = [
    9
    * (2 * n + 1)
    * (6 * n + 5)
    * (6 * n + 7)
    * (6 * n + 11)
    * (6 * n + 13)
    * (660 * n**2 + 2920 * n + 3039),
    24
    * n
    * (6 * n + 11)
    * (6 * n + 13)
    * (
        1697520 * n**4
        + 10905280 * n**3
        + 24360488 * n**2
        + 22368528 * n
        + 7001703
    ),
    768
    * n
    * (n + 1)
    * (2 * n + 3)
    * (6 * n + 13)
    * (3960 * n**3 + 20820 * n**2 + 33034 * n + 14047),
    4096
    * n
    * (n + 1)
    * (n + 2)
    * (2 * n + 3)
    * (2 * n + 5)
    * (660 * n**2 + 1600 * n + 779),
]

def rising(z, count):
    return S.prod((z + j for j in range(count)), start=S.Integer(1))


shift_ratios = []
for shift in range(4):
    # These two factors are the exact quotients of the two generalized
    # binomials in summand(s+shift,m)/summand(s,m).  Writing them down
    # directly avoids a half-integral-binomial limitation in hypersimp.
    first_binomial = rising(2 * s + m + 1, 2 * shift) / rising(
        2 * s + 1, 2 * shift
    )
    second_binomial = rising(alpha + 1, 3 * shift) / (
        rising(k_lower + 1, 2 * shift)
        * rising(alpha - k_lower + 1, shift)
    )
    quotient = S.factor(
        first_binomial
        * second_binomial
        * contiguous.subs(s, s + shift)
        / contiguous
    )
    if not quotient.is_rational_function(s, m):
        raise AssertionError(("nonrational shift", shift))
    shift_ratios.append(quotient)
    print("shift_ready", shift, "characters", len(str(quotient)), flush=True)

combined_ratio = S.factor(
    sum(
        operators[shift] * shift_ratios[shift]
        for shift in range(4)
    )
)
print(
    "combined_ready",
    "characters",
    len(str(combined_ratio)),
    flush=True,
)

summand_ratio = S.factor(
    -(2 * s + m + 1)
    / (m + 1)
    * k_lower
    * (k_lower - 1)
    / ((alpha - k_lower + 1) * (alpha - k_lower + 2))
    * contiguous.subs(m, m + 1)
    / contiguous
)
target_ratio = S.cancel(
    summand_ratio
    * combined_ratio.subs(m, m + 1)
    / combined_ratio
)
print("target_ratio_ready", "characters", len(str(target_ratio)), flush=True)
if os.environ.get("ITEM312_RATIO_ONLY") == "1":
    ratio_numerator, ratio_denominator = target_ratio.as_numer_denom()
    recorded_factors = {}
    for label, polynomial in (
        ("NUMERATOR", ratio_numerator),
        ("DENOMINATOR", ratio_denominator),
    ):
        started = time.time()
        content, factors = S.factor_list(polynomial, m)
        recorded_factors[label] = (content, factors)
        print(label + "_CONTENT", S.factor(content), flush=True)
        for factor_polynomial, multiplicity in factors:
            print(
                label + "_FACTOR",
                multiplicity,
                S.factor(factor_polynomial),
                flush=True,
            )
        print(label + "_FACTOR_SECONDS", round(time.time() - started, 3), flush=True)
    numerator_large = max(
        recorded_factors["NUMERATOR"][1],
        key=lambda item: S.degree(item[0], m),
    )[0]
    denominator_large = max(
        recorded_factors["DENOMINATOR"][1],
        key=lambda item: S.degree(item[0], m),
    )[0]
    print(
        "LARGE_SHIFT_PLUS_ONE",
        S.Poly(
            numerator_large - denominator_large.subs(m, m + 1),
            m,
        ).is_zero,
        flush=True,
    )
    raise SystemExit(0)


def gosper_from_ratio(ratio, variable):
    """Return g/t for g(n+1)-g(n)=t(n), given t(n+1)/t(n)."""
    numerator, denominator = S.cancel(ratio).as_numer_denom()
    _, numerator_factors = S.factor_list(numerator, variable)
    _, denominator_factors = S.factor_list(denominator, variable)
    numerator_large = max(
        numerator_factors, key=lambda item: S.degree(item[0], variable)
    )[0]
    denominator_large = max(
        denominator_factors, key=lambda item: S.degree(item[0], variable)
    )[0]
    if S.Poly(
        numerator_large - denominator_large.subs(variable, variable + 1),
        variable,
    ).is_zero:
        extracted_shift_factor = denominator_large
        ratio = S.cancel(
            ratio
            * extracted_shift_factor
            / extracted_shift_factor.subs(variable, variable + 1)
        )
        numerator, denominator = ratio.as_numer_denom()
        print(
            "pre_normal_shift_factor_degree",
            S.degree(extracted_shift_factor, variable),
            flush=True,
        )
    else:
        extracted_shift_factor = S.Integer(1)
    A, B, C = gosper_normal(numerator, denominator, variable)
    C *= S.Poly(extracted_shift_factor, variable, domain=C.domain)
    B = B.shift(-1)
    degree_A = S.Integer(A.degree())
    degree_B = S.Integer(B.degree())
    degree_C = S.Integer(C.degree())
    if degree_A != degree_B or A.LC() != B.LC():
        candidates = {degree_C - max(degree_A, degree_B)}
    elif not degree_A:
        candidates = {degree_C - degree_A + 1, S.Zero}
    else:
        candidates = {
            degree_C - degree_A + 1,
            S.cancel((B.nth(degree_A - 1) - A.nth(degree_A - 1)) / A.LC()),
        }
    degrees = [int(d) for d in candidates if d.is_Integer and d >= 0]
    if not degrees:
        return None
    degree = max(degrees)
    coefficients = S.symbols("c:{}".format(degree + 1))
    polynomial = sum(coefficients[j] * variable**j for j in range(degree + 1))
    equation = S.Poly(
        S.together(
            A.as_expr() * polynomial.subs(variable, variable + 1)
            - B.as_expr() * polynomial
            - C.as_expr()
        ),
        variable,
    )
    solution = S.solve(equation.all_coeffs(), coefficients, dict=True)
    if not solution:
        return None
    polynomial = polynomial.subs(solution[0])
    for coefficient in coefficients:
        if coefficient not in solution[0]:
            polynomial = polynomial.subs(coefficient, 0)
    if polynomial == 0:
        return None
    return S.cancel(B.as_expr() * polynomial / C.as_expr())


started = time.time()
certificate_ratio = gosper_from_ratio(target_ratio, m)
print(
    "gosper_finished",
    "seconds",
    round(time.time() - started, 3),
    "success",
    certificate_ratio is not None,
    flush=True,
)
if certificate_ratio is None:
    raise RuntimeError("no Gosper certificate")

certificate_ratio = S.factor(certificate_ratio)
print("certificate_characters", len(str(certificate_ratio)), flush=True)
print("CERTIFICATE_BEGIN", flush=True)
print(certificate_ratio, flush=True)
print("CERTIFICATE_END", flush=True)
base_certificate = S.factor(S.cancel(certificate_ratio * combined_ratio))
print("base_certificate_characters", len(str(base_certificate)), flush=True)
print("BASE_CERTIFICATE_BEGIN", flush=True)
print(base_certificate, flush=True)
print("BASE_CERTIFICATE_END", flush=True)
base_identity_started = time.time()
base_identity = S.cancel(
    base_certificate.subs(m, m + 1) * summand_ratio
    - base_certificate
    - combined_ratio
)
print(
    "base_identity_zero",
    base_identity == 0,
    "seconds",
    round(time.time() - base_identity_started, 3),
    flush=True,
)
if base_identity != 0:
    raise AssertionError("base Gosper identity replay")
export_path = os.environ.get("ITEM312_EXPORT_DATA")
if export_path:
    base_numerator, base_denominator = base_certificate.as_numer_denom()
    _, base_numerator_factors = S.factor_list(base_numerator, m)
    certificate_polynomial = max(
        base_numerator_factors,
        key=lambda item: S.degree(item[0], m),
    )[0]
    polynomial_in_m = S.Poly(certificate_polynomial, m)
    payload = {
        "schema": "item312_A_telescoper_data_v1",
        "operators_factored": [str(S.factor(operator)) for operator in operators],
        "contiguous_factor": str(contiguous),
        "certificate_J_degree_m": polynomial_in_m.degree(),
        "certificate_J_coefficients_descending_m": [
            str(S.factor(coefficient))
            for coefficient in polynomial_in_m.all_coeffs()
        ],
        "base_certificate": str(base_certificate),
    }
    with open(export_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print("exported", export_path, flush=True)

# certificate_ratio is g_m/t_m with g_(m+1)-g_m=t_m.
identity = S.factor(
    certificate_ratio.subs(m, m + 1) * target_ratio
    - certificate_ratio
    - 1
)
print("identity_zero", identity == 0, flush=True)
if identity != 0:
    raise AssertionError("Gosper identity replay")
