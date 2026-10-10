#!/usr/bin/env python3
"""Deterministic certificate for Item 425's adjacent-index transfer.

The checker is standard-library only.  Finite rows normalize exact formulas;
the asymptotic theorem is proved symbolically in the companion report from
the pinned saddle expansions of Items 420 and 423.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction as F
import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item425_adjacent_transfer_certificate.json"

DEPENDENCIES = {
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "results/item390_mixed_cubic_fresh_primitive_saturation_certificate.json":
        "45b61f683a29305e4fcfd8810f146068f950070496e8e88a2a6b800f9dc1ada6",
    "sources/item415_marked_selector_compulsory_strip_report.md":
        "da79ea786471a6abb35288f242a0b0b2307a695bd9352eaa3c4e2033fc701777",
    "results/item415_marked_selector_compulsory_strip_certificate.json":
        "af731cf70e9a6d40cab380d38d5b404786cefef196eb42f743634b8d390cb29e",
    "sources/item418_normalized_large_carrier_report.md":
        "5b490e38d127deec51cac34a80c6856ed824534daad8fc3a387fe6cbb7f7db68",
    "results/item418_normalized_large_carrier_certificate.json":
        "bcea1e6be723e48e3d1ca63bc5644b208059e5138799108ea403b0ba5d789075",
    "sources/item420_normalized_contour_extension_report.md":
        "eebbcd02c654d6be1ca6ae50e427931abc16aae773300b4d1f32dc8f2291a414",
    "results/item420_normalized_contour_extension_certificate.json":
        "ddac30da2c3c7ebca84cce7c412f99c05b6d6281a5598c2346f33b50efe18095",
    "work/item423_polynomial_bezout_no_go_report.md":
        "fddb0af24dd970dd3835aad6688a02d3da277cf854781c822875698d2d2350a6",
    "work/item423_polynomial_bezout_no_go_certificate.json":
        "3ccb1fadac9f770cc999af24cb1781dd4c875bcaea3d01c252de94c725ad08aa",
}

Poly = list[F]
Rat = tuple[Poly, Poly]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> dict[str, str]:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))
    return dict(DEPENDENCIES)


def trim(poly: Poly) -> Poly:
    out = poly[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: Poly, right: Poly) -> Poly:
    out = [F(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def scale(poly: Poly, scalar: F) -> Poly:
    return trim([scalar * value for value in poly])


def multiply(left: Poly, right: Poly) -> Poly:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def power(poly: Poly, exponent: int) -> Poly:
    out = [F(1)]
    base = poly[:]
    value = exponent
    while value:
        if value & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        value >>= 1
    return out


def derivative(poly: Poly) -> Poly:
    return [F(0)] if len(poly) == 1 else trim([i * poly[i] for i in range(1, len(poly))])


def divide_with_remainder(dividend: Poly, divisor: Poly) -> tuple[Poly, Poly]:
    numerator = trim(dividend)
    denominator = trim(divisor)
    quotient = [F(0)] * max(1, len(numerator) - len(denominator) + 1)
    while numerator != [0] and len(numerator) >= len(denominator):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] / denominator[-1]
        quotient[shift] += coefficient
        for i, value in enumerate(denominator):
            numerator[i + shift] -= coefficient * value
        numerator = trim(numerator)
    return trim(quotient), trim(numerator)


def determinant(matrix: list[list[F]]) -> F:
    work = [row[:] for row in matrix]
    value = F(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value *= pivot_value
        for entry in range(column, len(work)):
            work[column][entry] /= pivot_value
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            if factor:
                for entry in range(column, len(work)):
                    work[row][entry] -= factor * work[column][entry]
    return value


def resultant(left: Poly, right: Poly) -> F:
    left, right = trim(left), trim(right)
    ld, rd = len(left) - 1, len(right) - 1
    size = ld + rd
    matrix = [[F(0)] * size for _ in range(size)]
    for row in range(rd):
        for i, value in enumerate(reversed(left)):
            matrix[row][row + i] = value
    for local in range(ld):
        for i, value in enumerate(reversed(right)):
            matrix[rd + local][local + i] = value
    return determinant(matrix)


def rat_add(left: Rat, right: Rat) -> Rat:
    return add(multiply(left[0], right[1]), multiply(right[0], left[1])), multiply(left[1], right[1])


def rat_scale(value: Rat, scalar: F) -> Rat:
    return scale(value[0], scalar), value[1]


def rat_mul(left: Rat, right: Rat) -> Rat:
    return multiply(left[0], right[0]), multiply(left[1], right[1])


def rat_div(left: Rat, right: Rat) -> Rat:
    return multiply(left[0], right[1]), multiply(left[1], right[0])


def rat_derivative(value: Rat) -> Rat:
    return (
        add(multiply(derivative(value[0]), value[1]), scale(multiply(value[0], derivative(value[1])), F(-1))),
        multiply(value[1], value[1]),
    )


def rat_equal(left: Rat, right: Rat) -> bool:
    return trim(multiply(left[0], right[1])) == trim(multiply(right[0], left[1]))


def lambda_pair(m: int) -> tuple[int, int]:
    l0 = 0
    for degree in range(6 * m + 1):
        base = (-1) ** degree * math.comb(6 * m, degree)
        for plus in range(2):
            residual = 4 * m - degree - plus
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                l0 += base * (-1) ** half * math.comb(4 * m + half, half)
    l1 = 0
    for degree in range(6 * m + 1):
        base = (-1) ** degree * math.comb(6 * m, degree)
        for plus in range(5):
            residual = 4 * m + 1 - degree - plus
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                l1 += base * math.comb(4, plus) * (-1) ** half * math.comb(4 * m + 1 + half, half)
    return l0, l1


def q_constant_term(m: int) -> int:
    raw = 0
    for degree in range(6 * m + 1):
        base = (-1) ** degree * math.comb(6 * m, degree)
        for shift, coefficient in ((0, -1), (2, -4), (4, 1)):
            residual = 4 * m + 1 - degree - shift
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                raw += base * coefficient * (-1) ** half * math.comb(4 * m + 1 + half, half)
    if raw % 2:
        raise AssertionError((m, raw))
    return raw // 2


Q2_NUM = [
    -3801088, 41574400, -205971456, 619161600, -1586297344,
    3456708288, -6253518656, 12447250341, -17002039104,
    40590677491, -34510619944, 116864052888, -69541566360,
    257666823352, -128134405320, 374285602250, -162511549560,
    335484606006, -129182415480, 174669454224, -62286636744,
    44447571936, -16889613912, 1416301929, -2001384936, -1142868609,
]


def q2_constant_term(m: int) -> F:
    target = 4 * m + 8
    total = 0
    for q_degree, q_coefficient in enumerate(Q2_NUM):
        for degree in range(6 * m + 1):
            residual = target - q_degree - degree
            if residual >= 0 and residual % 2 == 0:
                half = residual // 2
                total += (
                    q_coefficient
                    * (-1) ** degree
                    * math.comb(6 * m, degree)
                    * (-1) ** half
                    * math.comb(4 * m + 8 + half, half)
                )
    return F(total, 15_420_537_000)


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * ((limit - prime * prime) // prime + 1)
    return [value for value in range(2, limit + 1) if sieve[value]]


def cartier_defect(modulus: int, numerator_degree: int, pole_order: int) -> int:
    remainder = numerator_degree % modulus
    target = pole_order % modulus
    return 2 * remainder if target == 0 else 2 * remainder + 3 * (modulus - target)


def full_F(m: int) -> int:
    primes = primes_up_to(6 * m)
    return math.prod(
        prime for prime in primes if prime != 2
        and cartier_defect(prime, 6 * m, 4 * m + 1) <= prime - 2
        and cartier_defect(prime, 6 * m, 4 * m + 2) <= prime - 2
    )


def symbolic_second_reduction() -> dict[str, Any]:
    y = [F(0), F(1)]
    one_minus_y = [F(1), F(-1)]
    one_plus_y = [F(1), F(1)]
    one_plus_y2 = [F(1), F(0), F(1)]
    H = (power(one_minus_y, 6), multiply(power(y, 4), power(one_plus_y2, 4)))
    f0 = (one_plus_y, one_plus_y2)
    q = ([F(-1), F(0), F(-4), F(0), F(1)], scale(multiply(y, power(one_plus_y2, 2)), F(2)))
    a = F(195029, 3525500)
    b = F(-1339328, 71391375)
    c = F(-237568, 1927567125)
    S = rat_add(([a], [F(1)]), rat_add(rat_scale(H, b), rat_scale(rat_mul(H, H), c)))
    residual = rat_add(q, rat_scale(rat_mul(f0, S), F(-1)))
    critical = [F(-2), F(-1), F(-6), F(3)]
    _, remainder = divide_with_remainder(residual[0], critical)
    if remainder != [F(0)]:
        raise AssertionError(("critical divisibility", remainder))

    log_derivative = rat_div(rat_derivative(H), H)
    A = rat_scale(rat_div(residual, log_derivative), F(-1))
    A_over_y = rat_div(A, (y, [F(1)]))
    q2_computed = rat_mul((y, [F(1)]), rat_derivative(A_over_y))
    q2_den = scale(multiply(power(y, 8), power(one_plus_y2, 9)), F(15_420_537_000))
    q2 = ([F(value) for value in Q2_NUM], q2_den)
    if not rat_equal(q2_computed, q2):
        raise AssertionError("q2 rational identity")
    q2_num_resultant = resultant(critical, q2[0])
    q2_den_resultant = resultant(critical, q2[1])
    if q2_num_resultant != -181207723609599379275366250837463531520000000:
        raise AssertionError(q2_num_resultant)
    if q2_den_resultant != 33028455344443562055745346250291019776000000000:
        raise AssertionError(q2_den_resultant)
    return {
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "critical_divides_reduced_amplitude_numerator": True,
        "q2_numerator_degree": len(Q2_NUM) - 1,
        "q2_denominator": "15420537000*y^8*(1+y^2)^9",
        "Res(P,q2_num)": str(q2_num_resultant),
        "Res(P,q2_den)": str(q2_den_resultant),
        "q2_nonzero_and_finite_at_all_critical_points": True,
    }


def finite_replay() -> dict[str, Any]:
    pairs = [lambda_pair(m) for m in range(27)]
    rows = []
    second_reductions = 0
    determinant_divisibility = 0
    for m in range(1, 25):
        l0, l1 = pairs[m]
        next0, next1 = pairs[m + 1]
        next20, _ = pairs[m + 2]
        D = 2 * l1 - 5 * l0
        D_next = 2 * next1 - 5 * next0
        if q_constant_term(m) != m * D:
            raise AssertionError((m, "first integration by parts"))
        a = F(195029, 3525500)
        b = F(-1339328, 71391375)
        c = F(-237568, 1927567125)
        left = m * D - a * l0 - b * next0 - c * next20
        right = q2_constant_term(m) / m
        if left != right:
            raise AssertionError((m, left, right, "second reduction"))
        second_reductions += 1

        W = l0 * next1 - l1 * next0
        if 2 * W != l0 * D_next - D * next0:
            raise AssertionError((m, "adjacent exterior identity"))
        Fm, Fn = full_F(m), full_F(m + 1)
        if any(value % Fm for value in (l0, l1)) or any(value % Fn for value in (next0, next1)):
            raise AssertionError((m, "F divisibility"))
        mu = (l0 // Fm, l1 // Fm)
        mu_next = (next0 // Fn, next1 // Fn)
        Wmu = mu[0] * mu_next[1] - mu[1] * mu_next[0]
        if W != Fm * Fn * Wmu:
            raise AssertionError((m, "normalized determinant"))
        gm = math.gcd(abs(mu[0]), abs(mu[1]))
        gn = math.gcd(abs(mu_next[0]), abs(mu_next[1]))
        if Wmu % (gm * gn):
            raise AssertionError((m, gm, gn, Wmu, "product gcd divisibility"))
        determinant_divisibility += 1
        if m in (1, 2, 3, 5, 10, 15, 20, 24):
            rows.append({
                "m": m,
                "lambda_m": [str(l0), str(l1)],
                "lambda_m_plus_1": [str(next0), str(next1)],
                "F_m": str(Fm),
                "F_m_plus_1": str(Fn),
                "normalized_adjacent_determinant": str(Wmu),
                "gcd_mu_m": str(gm),
                "gcd_mu_m_plus_1": str(gn),
            })
    stream = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "classification": "EXACT NORMALIZATION REPLAY ONLY; NO FINITE-TO-ASYMPTOTIC INFERENCE",
        "first_reduction_rows": 24,
        "second_reduction_rows": second_reductions,
        "adjacent_determinant_divisibility_rows": determinant_divisibility,
        "selected_rows": rows,
        "row_digest_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
    }


def capacity_screen() -> dict[str, Any]:
    getcontext().prec = 50
    normalized_base = Decimal("13.1004071782333102143382142797")
    squared = normalized_base * normalized_base
    component = Decimal("0.4287738853386578689457603829")
    return {
        "current_normalized_single_row_base": str(normalized_base),
        "adjacent_determinant_base": str(squared),
        "direct_bound_for_one_gcd_is_worse": True,
        "direct_determinant_ceiling_per_6m": str(component * 2),
        "two_row_product_after_dividing_by_two": str(component),
        "strict_improvement": 0,
        "new_booking": 0,
        "new_capacity_reduction": 0,
        "retained_component_ceiling": str(component),
    }


def build_payload() -> dict[str, Any]:
    return {
        "item": 425,
        "schema": "item425-adjacent-transfer-v1",
        "title": "adjacent exterior transfer saturates the normalized mixed-cubic base",
        "checked_date_beijing": "2026-09-01",
        "status": "PROVED_ADJACENT_DETERMINANT_SATURATION_AND_SCOPED_HOLONOMIC_NO_GO_ZERO_LEDGER",
        "dependency_hashes_verified": verify_dependencies(),
        "exact_identities": {
            "D_m": "D_m=2*lambda_1,m-5*lambda_0,m=CT(q*H^m)/m",
            "adjacent_exterior": "2*W_m=lambda_0,m*D_(m+1)-D_m*lambda_0,(m+1)",
            "normalized_determinant": "W_mu,m=W_lambda,m/(F_m*F_(m+1)) is an integer",
            "gcd_product": "g_m*g_(m+1) divides W_mu,m",
            "second_critical_reduction": (
                "m*D_m-a*lambda_0,m-b*lambda_0,(m+1)-c*lambda_0,(m+2)="
                "CT(q2*H^m)/m, with exact a,b,c and q2 nonzero at every critical point"
            ),
        },
        "symbolic_second_reduction": symbolic_second_reduction(),
        "finite_replay": finite_replay(),
        "asymptotic_theorem": {
            "inherited": (
                "lambda_0,m has saddle amplitude C and D_m has amplitude C*t(alpha); "
                "Items 420/423 prove tau and t(alpha) are nonreal"
            ),
            "leading_cross_coefficient": "(|C|^2/2)*(t-conj(t))*(tau-conj(tau)) is nonzero",
            "conclusion_lambda": "lim |W_lambda,m|^(1/m)=rho_star^2",
            "conclusion_normalized": (
                "lim |W_mu,m|^(1/m)=(rho_star*exp(-C_F))^2"
            ),
            "scope": (
                "adjacent h=1 determinant and the first degree-2 critical-value reduction; "
                "not every growing window, adaptive recurrence, or modular resultant"
            ),
        },
        "capacity": capacity_screen(),
        "smallest_missing_lemma": {
            "statement": (
                "find genuinely arithmetic cross-index information whose carrier root base, "
                "after accounting for every row gcd it contains, is strictly below "
                "rho_star*exp(-C_F), or prove weighted nonconcentration directly"
            ),
            "status": "OPEN",
        },
        "strict_labels": {
            "PROVED": [
                "exact adjacent exterior identity and normalized product-gcd divisibility",
                "exact degree-2 critical-value transfer with nonzero reduced amplitude",
                "adjacent determinant root base rho_star^2",
                "normalized determinant base (rho_star*exp(-C_F))^2",
                "zero booking and zero capacity reduction",
            ],
            "SCOPED_NO_GO": [
                "the adjacent 2x2 determinant gives a worse one-row bound and exactly reproduces the current ceiling after averaging its two row gcds",
                "the natural degree-2 shifted critical-value cancellation saves only a polynomial factor",
            ],
            "OPEN": [
                "larger or growing windows and adaptive coefficients",
                "a different resultant with strict per-contained-gcd exponential gain",
                "log c_m^>=o(m), Route 1, and every conclusion about e+pi",
            ],
        },
        "evidence_policy": {
            "actual_family_only": True,
            "finite_rows_only_normalize_formulas": True,
            "no_finite_extrapolation": True,
            "component_not_subtracted_from_global_ceiling": True,
            "no_irrationality_claim": True,
        },
    }


def encode(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    data = encode(build_payload())
    if args.replay is not None and args.replay.read_bytes() != data:
        raise AssertionError((args.replay, "replay mismatch"))
    args.output.write_bytes(data)
    print(json.dumps({"output": str(args.output), "sha256": hashlib.sha256(data).hexdigest()}))


if __name__ == "__main__":
    main()
