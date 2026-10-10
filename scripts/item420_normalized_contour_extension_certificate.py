#!/usr/bin/env python3
"""Deterministic exact replay for Item 420.

The report proves an analytic saddle lemma.  This replay certifies all of
its algebraic hypotheses: the common phase, the critical cubic, the unique
fixed-coordinate cancellation, the exact integration-by-parts amplitude,
and the nonvanishing resultants.  It also cross-checks the coefficient
identity on exact integer rows and pins the canonical dependencies.
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


Poly = list[Fraction]  # ascending coefficients


EXPECTED_DEPENDENCIES = {
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "results/item390_mixed_cubic_fresh_primitive_saturation_certificate.json":
        "45b61f683a29305e4fcfd8810f146068f950070496e8e88a2a6b800f9dc1ada6",
    "results/item390_mixed_cubic_fresh_primitive_saturation_root_audit.json":
        "8287cf78f5af6e4824c2034bd9af2aa5c7669afc0eb555c926ef59ab74914813",
    "sources/item415_marked_selector_compulsory_strip_report.md":
        "da79ea786471a6abb35288f242a0b0b2307a695bd9352eaa3c4e2033fc701777",
    "results/item415_marked_selector_compulsory_strip_certificate.json":
        "af731cf70e9a6d40cab380d38d5b404786cefef196eb42f743634b8d390cb29e",
    "results/item415_marked_selector_compulsory_strip_root_audit.json":
        "123576c914528abdc1e3ffa3993e5161c56f92ac21e4ec33b9c6f450edfa653c",
    "sources/item418_normalized_large_carrier_report.md":
        "5b490e38d127deec51cac34a80c6856ed824534daad8fc3a387fe6cbb7f7db68",
    "results/item418_normalized_large_carrier_certificate.json":
        "bcea1e6be723e48e3d1ca63bc5644b208059e5138799108ea403b0ba5d789075",
    "results/item418_normalized_large_carrier_root_audit.json":
        "530eb0827398480fcff5c8afb564c174d6f9cab8f6be00f5e965ed796eb29c63",
    "manifests/item418_normalized_large_carrier_manifest.json":
        "22f0c0fcdacf6b887ad11adeb7341408551a20a60321ad7d44cd3eeb35ea68cb",
    "results/item418_normalized_large_carrier_hashes.sha256":
        "688a95b3eb20f54b59b5418af02097d54f3ac6ef4c8eff5b9d9e3d0775cdb38b",
}


def trim(poly: Poly) -> Poly:
    out = poly[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim([scalar * value for value in poly])


def multiply(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            out[left_index + right_index] += left_value * right_value
    return trim(out)


def power(poly: Poly, exponent: int) -> Poly:
    out = [Fraction(1)]
    base = poly[:]
    value = exponent
    while value:
        if value & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        value >>= 1
    return out


def derivative(poly: Poly) -> Poly:
    if len(poly) == 1:
        return [Fraction(0)]
    return trim([index * poly[index] for index in range(1, len(poly))])


def divide_with_remainder(dividend: Poly, divisor: Poly) -> tuple[Poly, Poly]:
    numerator = trim(dividend)
    denominator = trim(divisor)
    if denominator == [0]:
        raise ZeroDivisionError("zero polynomial")
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0) for _ in range(len(numerator) - len(denominator) + 1)]
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] / denominator[-1]
        quotient[shift] += coefficient
        for index, value in enumerate(denominator):
            numerator[index + shift] -= coefficient * value
        numerator = trim(numerator)
    return trim(quotient), trim(numerator)


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    size = len(work)
    value = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value *= pivot_value
        for entry in range(column, size):
            work[column][entry] /= pivot_value
        for row in range(column + 1, size):
            factor = work[row][column]
            if factor:
                for entry in range(column, size):
                    work[row][entry] -= factor * work[column][entry]
    return value


def resultant(left: Poly, right: Poly) -> Fraction:
    left = trim(left)
    right = trim(right)
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    left_desc = list(reversed(left))
    right_desc = list(reversed(right))
    size = left_degree + right_degree
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for row in range(right_degree):
        for index, value in enumerate(left_desc):
            matrix[row][row + index] = value
    for local_row in range(left_degree):
        row = right_degree + local_row
        for index, value in enumerate(right_desc):
            matrix[row][local_row + index] = value
    return determinant(matrix)


def rational_equal(
    left_num: Poly, left_den: Poly, right_num: Poly, right_den: Poly
) -> bool:
    return trim(multiply(left_num, right_den)) == trim(multiply(right_num, left_den))


def text_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def negative_binomial(power_value: int, half_degree: int) -> int:
    return math.comb(power_value + half_degree - 1, half_degree)


def lambda_pair(m_value: int) -> tuple[int, int]:
    target0 = 4 * m_value
    lambda0 = 0
    for numerator_degree in range(6 * m_value + 1):
        base = (-1) ** numerator_degree * math.comb(6 * m_value, numerator_degree)
        for plus_degree in range(2):
            residual = target0 - numerator_degree - plus_degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                lambda0 += base * (-1) ** half * negative_binomial(4 * m_value + 1, half)

    target1 = 4 * m_value + 1
    lambda1 = 0
    for numerator_degree in range(6 * m_value + 1):
        base = (-1) ** numerator_degree * math.comb(6 * m_value, numerator_degree)
        for plus_degree in range(5):
            residual = target1 - numerator_degree - plus_degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                lambda1 += (
                    base
                    * math.comb(4, plus_degree)
                    * (-1) ** half
                    * negative_binomial(4 * m_value + 2, half)
                )
    return lambda0, lambda1


def q_constant_term(m_value: int) -> int:
    """CT(q H^m), using the coefficient form with its factor 1/2."""
    target = 4 * m_value + 1
    raw = 0
    q_terms = {0: -1, 2: -4, 4: 1}
    for numerator_degree in range(6 * m_value + 1):
        base = (-1) ** numerator_degree * math.comb(6 * m_value, numerator_degree)
        for q_degree, q_coefficient in q_terms.items():
            residual = target - numerator_degree - q_degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                raw += (
                    base
                    * q_coefficient
                    * (-1) ** half
                    * negative_binomial(4 * m_value + 2, half)
                )
    if raw % 2:
        raise AssertionError((m_value, raw))
    return raw // 2


def complex_saddle() -> complex:
    value = complex(-0.14, 0.52)
    for _ in range(30):
        polynomial = 3 * value**3 - 6 * value**2 - value - 2
        derivative_value = 9 * value**2 - 12 * value - 1
        value -= polynomial / derivative_value
    return value


def build_payload() -> dict[str, object]:
    root = Path(__file__).resolve().parents[1]
    dependency_hashes: dict[str, str] = {}
    for relative, expected in EXPECTED_DEPENDENCIES.items():
        actual = sha256(root / relative)
        if actual != expected:
            raise AssertionError(f"dependency hash mismatch: {relative}: {actual} != {expected}")
        dependency_hashes[relative] = actual

    y = [Fraction(0), Fraction(1)]
    one_minus_y = [Fraction(1), Fraction(-1)]
    one_plus_y = [Fraction(1), Fraction(1)]
    one_plus_y2 = [Fraction(1), Fraction(0), Fraction(1)]
    critical = [Fraction(-2), Fraction(-1), Fraction(-6), Fraction(3)]

    h_num = power(one_minus_y, 6)
    h_den = multiply(power(y, 4), power(one_plus_y2, 4))
    log_num = add(multiply(derivative(h_num), h_den), scale(multiply(h_num, derivative(h_den)), -1))
    log_den = multiply(h_num, h_den)
    critical_den = multiply(multiply(y, one_minus_y), one_plus_y2)
    log_derivative_identity = rational_equal(
        log_num, log_den, scale(critical, 2), critical_den
    )
    if not log_derivative_identity:
        raise AssertionError("H'/H critical-cubic identity failed")

    f0_num = one_plus_y
    f0_den = one_plus_y2
    f1_num = power(one_plus_y, 4)
    f1_den = multiply(y, power(one_plus_y2, 2))
    fd_num = add(scale(multiply(f1_num, f0_den), 2), scale(multiply(f0_num, f1_den), -5))
    fd_den = multiply(f1_den, f0_den)
    a_num = [Fraction(1), Fraction(0), Fraction(-1)]
    a_den = scale(one_plus_y2, 2)
    minus_a_log_num = scale(multiply(a_num, log_num), -1)
    minus_a_log_den = multiply(a_den, log_den)
    cancellation_identity = rational_equal(fd_num, fd_den, minus_a_log_num, minus_a_log_den)
    if not cancellation_identity:
        raise AssertionError("fixed-coordinate cancellation identity failed")

    # q=y(A/y)' and 2 lambda_1-5 lambda_0 = CT(q H^m)/m.
    a_over_y_num = a_num
    a_over_y_den = multiply(a_den, y)
    q_derived_num = multiply(
        y,
        add(
            multiply(derivative(a_over_y_num), a_over_y_den),
            scale(multiply(a_over_y_num, derivative(a_over_y_den)), -1),
        ),
    )
    q_derived_den = power(a_over_y_den, 2)
    q_num = [Fraction(-1), Fraction(0), Fraction(-4), Fraction(0), Fraction(1)]
    q_den = scale(multiply(y, power(one_plus_y2, 2)), 2)
    q_identity = rational_equal(q_derived_num, q_derived_den, q_num, q_den)
    if not q_identity:
        raise AssertionError("integration-by-parts amplitude identity failed")

    critical_resultant = resultant(critical, derivative(critical))
    q_resultant = resultant(critical, q_num)
    f0_numerator_resultant = resultant(critical, f0_num)
    if critical_resultant != 9900:
        raise AssertionError(critical_resultant)
    if q_resultant != 176:
        raise AssertionError(q_resultant)
    if f0_numerator_resultant != 10:
        raise AssertionError(f0_numerator_resultant)

    # If beta is the real root and x=alpha*conjugate(alpha)=2/(3 beta),
    # then 9 x^3 P(2/(3x))=-2 h(x).
    h_poly = [Fraction(-4), Fraction(12), Fraction(3), Fraction(9)]
    substituted_numerator = [Fraction(8), Fraction(-24), Fraction(-6), Fraction(-18)]
    vieta_identity = trim(substituted_numerator) == trim(scale(h_poly, -2))
    if not vieta_identity:
        raise AssertionError("Vieta modulus identity failed")

    # Eliminate a critical point from t=H(y).  Clearing H's denominator,
    # the following polynomial is divisible by P(y).
    critical_value_poly = [
        Fraction(-531441),
        Fraction(4819949712),
        Fraction(68124672),
        Fraction(262144),
    ]
    critical_value_relation = add(
        add(
            scale(power(h_num, 3), critical_value_poly[3]),
            scale(multiply(power(h_num, 2), h_den), critical_value_poly[2]),
        ),
        add(
            scale(multiply(h_num, power(h_den, 2)), critical_value_poly[1]),
            scale(power(h_den, 3), critical_value_poly[0]),
        ),
    )
    _, critical_value_remainder = divide_with_remainder(critical_value_relation, critical)
    if critical_value_remainder != [0]:
        raise AssertionError("critical-value polynomial relation failed")
    d0, c0, b0, a0 = [int(value) for value in critical_value_poly]
    critical_value_discriminant = (
        b0 * b0 * c0 * c0
        - 4 * a0 * c0 * c0 * c0
        - 4 * b0 * b0 * b0 * d0
        - 27 * a0 * a0 * d0 * d0
        + 18 * a0 * b0 * c0 * d0
    )
    expected_value_discriminant = -9597549474870371132689612800000000
    if critical_value_discriminant != expected_value_discriminant:
        raise AssertionError(critical_value_discriminant)
    # For nonzero t the second Sylvester polynomial has its generic degree
    # twelve.  Four exact evaluations certify the cubic resultant identity
    # Res_y(P, t*H_den-H_num)=64*R(t).
    critical_value_resultant_checks: dict[str, str] = {}
    for t_value in range(1, 5):
        t_fraction = Fraction(t_value)
        left_value = resultant(
            critical,
            add(scale(h_den, t_fraction), scale(h_num, -1)),
        )
        right_value = 64 * sum(
            critical_value_poly[index] * t_fraction**index
            for index in range(len(critical_value_poly))
        )
        if left_value != right_value:
            raise AssertionError((t_value, left_value, right_value))
        critical_value_resultant_checks[str(t_value)] = text_fraction(left_value)

    exact_rows = []
    for m_value in range(1, 17):
        lambda0, lambda1 = lambda_pair(m_value)
        difference = 2 * lambda1 - 5 * lambda0
        q_value = q_constant_term(m_value)
        if q_value != m_value * difference:
            raise AssertionError((m_value, q_value, difference))
        exact_rows.append(
            {
                "m": m_value,
                "lambda0": str(lambda0),
                "lambda1": str(lambda1),
                "D=2lambda1-5lambda0": str(difference),
                "CT(qH^m)": str(q_value),
            }
        )

    item418 = json.loads((root / "results/item418_normalized_large_carrier_certificate.json").read_text(encoding="utf-8"))
    rho_text = item418["capacity"]["rho_star_decimal"]
    c_f_text = item418["capacity"]["forced_Item200_rate_per_m"]
    ceiling_text = item418["capacity"]["Item418_sharp_circular_component_ceiling"]

    getcontext().prec = 80
    rho = Decimal(rho_text)
    c_f = Decimal(c_f_text)
    normalized_base = rho / c_f.exp()
    recomputed_ceiling = normalized_base.ln() / Decimal(6)
    if abs(recomputed_ceiling - Decimal(ceiling_text)) > Decimal("1e-70"):
        raise AssertionError("normalized-base rate mismatch")

    alpha = complex_saddle()
    h_alpha = (1 - alpha) ** 6 / (alpha**4 * (1 + alpha**2) ** 4)
    f0_alpha = (1 + alpha) / (1 + alpha**2)
    f1_alpha = (1 + alpha) ** 4 / (alpha * (1 + alpha**2) ** 2)
    q_alpha = (alpha**4 - 4 * alpha**2 - 1) / (2 * alpha * (1 + alpha**2) ** 2)
    if abs(3 * alpha**3 - 6 * alpha**2 - alpha - 2) > 1e-12:
        raise AssertionError("complex saddle Newton witness failed")
    if abs(f1_alpha / f0_alpha - 2.5) > 1e-12:
        raise AssertionError("saddle amplitude ratio failed")
    if abs(abs(h_alpha) - float(rho)) > 1e-10:
        raise AssertionError("saddle modulus mismatch")
    if abs(q_alpha) < 1e-8:
        raise AssertionError("q saddle amplitude vanished numerically")

    algebraic_witness = {
        "common_phase": "H(y)=(1-y)^6/(y^4(1+y^2)^4)",
        "critical_polynomial_coefficients_ascending": [text_fraction(value) for value in critical],
        "log_derivative_identity": "H'/H=2P/(y(1-y)(1+y^2))",
        "log_derivative_identity_verified": log_derivative_identity,
        "P_resultant_Pprime": text_fraction(critical_resultant),
        "fixed_amplitude_ratio_identity": "f1/f0-5/2=-P/(2y(1+y^2))",
        "unique_fixed_cancellation": "D_m=2lambda1,m-5lambda0,m",
        "cancellation_identity": "2f1-5f0=-A H'/H, A=(1-y^2)/(2(1+y^2))",
        "cancellation_identity_verified": cancellation_identity,
        "integration_by_parts": "D_m=CT(qH^m)/m",
        "q": "(y^4-4y^2-1)/(2y(1+y^2)^2)",
        "q_identity_verified": q_identity,
        "resultant_P_qnumerator": text_fraction(q_resultant),
        "resultant_P_f0numerator": text_fraction(f0_numerator_resultant),
        "h_modulus_polynomial_coefficients_ascending": [text_fraction(value) for value in h_poly],
        "vieta_identity": "9x^3 P(2/(3x))=-2(9x^3+3x^2+12x-4)",
        "vieta_identity_verified": vieta_identity,
        "critical_value_polynomial_coefficients_ascending": [
            text_fraction(value) for value in critical_value_poly
        ],
        "critical_value_relation_remainder_mod_P": [
            text_fraction(value) for value in critical_value_remainder
        ],
        "critical_value_polynomial_discriminant": str(critical_value_discriminant),
        "critical_value_resultant_identity": "Res_y(P,t*H_den-H_num)=64*R(t)",
        "critical_value_resultant_exact_checks_t_1_to_4": critical_value_resultant_checks,
        "phase_consequence": "the two complex critical points have distinct nonreal conjugate H-values",
    }
    witness_sha = hashlib.sha256(
        json.dumps(algebraic_witness, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    return {
        "schema": "item420-normalized-contour-extension-v1",
        "item": 420,
        "status": "CANONICAL_ROOT_AUDITED_SCOPED_HEIGHT_NO_GO_NO_BOOKING",
        "generator": Path(__file__).name,
        "generator_sha256": sha256(Path(__file__)),
        "dependency_sha256": dependency_hashes,
        "algebraic_saddle_witness": algebraic_witness,
        "complex_numeric_witness": {
            "alpha": [format(alpha.real, ".17g"), format(alpha.imag, ".17g")],
            "H_alpha": [format(h_alpha.real, ".17g"), format(h_alpha.imag, ".17g")],
            "abs_H_alpha": format(abs(h_alpha), ".17g"),
            "f1_over_f0": [format((f1_alpha / f0_alpha).real, ".17g"), format((f1_alpha / f0_alpha).imag, ".17g")],
            "q_alpha_abs": format(abs(q_alpha), ".17g"),
            "role": "floating cross-check only; exact claims use polynomial identities and resultants",
        },
        "exact_coefficient_rows": exact_rows,
        "capacity": {
            "rho_star": rho_text,
            "forced_C_F_per_m": c_f_text,
            "normalized_fixed_combination_root_base": format(normalized_base, "f"),
            "unchanged_component_ceiling": ceiling_text,
            "component_ceiling_delta": "0",
            "booked_lower_bound_delta": "0",
            "global_total_content_ceiling_delta": "0",
            "frozen_deficit_delta": "0",
        },
        "analytic_claim_pinned_to_report": {
            "statement": "for every fixed nonzero rational pair (a,b), limsup |a lambda0,m+b lambda1,m|^(1/m)=rho_star",
            "ordinary_case": "2a+5b nonzero: nonzero m^(-1/2) saddle amplitude",
            "cancelled_case": "2a+5b=0: exact integration by parts leaves nonzero q amplitude and m^(-3/2)",
            "method_consequence": "no absolute height bound for a fixed normalized coordinate combination can have exponential base below rho_star*exp(-C_F)",
        },
        "strict_claims": {
            "PROVED": [
                "unique leading fixed-coordinate cancellation D=2lambda1-5lambda0",
                "exact integration-by-parts identity D=CT(qH^m)/m",
                "q is nonzero at every critical point",
                "all fixed nonzero rational combinations retain limsup root rho_star",
                "zero ledger delta",
            ],
            "SCOPED_NO_GO": [
                "fixed-coordinate linear-combination height arguments, including asymmetric or noncircular absolute contour estimates, cannot improve Item418's exponential base",
            ],
            "OPEN": [
                "m-dependent coordinate combinations",
                "joint gcd or resultant bounds",
                "weighted zero density for the actual normalized pair",
                "Route 1 and irrationality of e+pi",
            ],
        },
        "witness_sha256": witness_sha,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--replay")
    arguments = parser.parse_args()
    payload = build_payload()
    if arguments.replay:
        expected = json.loads(Path(arguments.replay).read_text(encoding="utf-8"))
        if payload != expected:
            raise SystemExit("replay mismatch")
    Path(arguments.output).write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
