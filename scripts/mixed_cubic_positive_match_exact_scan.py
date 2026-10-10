#!/usr/bin/env python3
"""Exact finite lower-bound scan for positive mixed-cubic/beta matches.

The only transcendental input is enclosed by rational Machin-series bounds.
The beta-form lower bound is the elementary integral bound
N!/(2N+1)! <= E_N.  Consequently every reported `lower_bound_gt_one`
is an exact finite statement, not a floating-point observation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
if hasattr(sys, "set_int_max_str_digits"):
    # Exact certificate integers legitimately exceed Python 3.11's defensive
    # decimal-conversion limit; certificate generation is not parsing untrusted input.
    sys.set_int_max_str_digits(0)


def trim(polynomial: list[Fraction]) -> list[Fraction]:
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def poly_add(
    left: list[Fraction], right: list[Fraction], scale: Fraction = Fraction(1)
) -> list[Fraction]:
    output = [Fraction()] * max(len(left), len(right))
    for index, value in enumerate(left):
        output[index] += value
    for index, value in enumerate(right):
        output[index] += scale * value
    return trim(output)


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction()] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return trim(output)


def poly_derivative(polynomial: list[Fraction]) -> list[Fraction]:
    return [
        Fraction(index) * polynomial[index] for index in range(1, len(polynomial))
    ] or [Fraction()]


def mixed_divmod_q(polynomial: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    """Divide by Q=1+x+x^2+x^3."""
    remainder = polynomial[:]
    quotient = [Fraction()] * max(1, len(remainder) - 3)
    while len(remainder) >= 4:
        shift = len(remainder) - 4
        leading = remainder[-1]
        quotient[shift] = leading
        for index in range(4):
            remainder[shift + index] -= leading
        trim(remainder)
    return trim(quotient), trim(remainder)


def mixed_remainder(polynomial: list[Fraction]) -> list[Fraction]:
    return mixed_divmod_q(polynomial)[1]


def poly_evaluate(polynomial: list[Fraction], value: Fraction) -> Fraction:
    output = Fraction()
    for coefficient in reversed(polynomial):
        output = output * value + coefficient
    return output


MIXED_Q = [Fraction(1)] * 4
MIXED_Q_PRIME = [Fraction(1), Fraction(2), Fraction(3)]
MIXED_Q_PRIME_INVERSE = [Fraction(), Fraction(-1, 4), Fraction(1, 4)]


def mixed_coordinates(n_value: int, power: int) -> tuple[Fraction, Fraction, Fraction]:
    """H=R+(L/4)log(2)+(E/8)pi for Q=(1+x)(1+x^2)."""
    numerator = [Fraction()] * n_value + [
        Fraction((-1) ** offset * math.comb(n_value, offset))
        for offset in range(n_value + 1)
    ]
    rational = Fraction()
    for level in range(power, 1, -1):
        reduced = mixed_remainder(numerator)
        primitive = mixed_remainder(poly_mul(reduced, MIXED_Q_PRIME_INVERSE))
        primitive = [-value / Fraction(level - 1) for value in primitive]
        lowered_numerator = poly_add(
            numerator, poly_mul(poly_derivative(primitive), MIXED_Q), Fraction(-1)
        )
        lowered_numerator = poly_add(
            lowered_numerator,
            poly_mul(primitive, MIXED_Q_PRIME),
            Fraction(level - 1),
        )
        numerator, remainder = mixed_divmod_q(lowered_numerator)
        if remainder != [0]:
            raise AssertionError((n_value, power, level, remainder))
        rational += poly_evaluate(primitive, Fraction(1)) / 4 ** (level - 1)
        rational -= poly_evaluate(primitive, Fraction())

    polynomial_part, remainder = mixed_divmod_q(numerator)
    rational += sum(
        (
            coefficient / Fraction(index + 1)
            for index, coefficient in enumerate(polynomial_part)
        ),
        Fraction(),
    )
    remainder += [Fraction()] * (3 - len(remainder))
    a_value, b_value, c_value = remainder[:3]
    logarithmic = a_value - b_value + 3 * c_value
    pi_coordinate = a_value + b_value - c_value
    return rational, logarithmic, pi_coordinate


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def lcm_upto(limit: int) -> int:
    result = 1
    for value in range(2, limit + 1):
        result = math.lcm(result, value)
    return result


def d_value(n_value: int, power: int, prime: int) -> int:
    remainder_n = n_value % prime
    remainder_k = power % prime
    if remainder_k == 0:
        return 2 * remainder_n
    return 2 * remainder_n + 3 * (prime - remainder_k)


def cartier_product(m_value: int) -> int:
    n_value = 6 * m_value
    power = 4 * m_value + 1
    result = 1
    for prime in primes_upto(n_value):
        if prime == 2:
            continue
        if (
            d_value(n_value, power, prime) <= prime - 2
            and d_value(n_value, power + 1, prime) <= prime - 2
        ):
            result *= prime
    return result


def beta_pairs(maximum_n: int) -> list[tuple[int, int]]:
    pairs = [(1, 1)]
    if maximum_n == 0:
        return pairs
    pairs.append((3, 1))
    for index in range(2, maximum_n + 1):
        p0, q0 = pairs[-2]
        p1, q1 = pairs[-1]
        multiplier = 4 * index - 2
        pairs.append((multiplier * p1 + p0, multiplier * q1 + q0))
    return pairs


def log_int(value: int) -> float:
    """Natural logarithm without converting a huge integer to float."""
    value = abs(value)
    if value == 0:
        return float("-inf")
    bits = value.bit_length()
    keep = min(bits, 53)
    head = value >> (bits - keep)
    return math.log(head) + (bits - keep) * math.log(2.0)


def exact_pi_pair(m_value: int) -> tuple[int, int, int, int, int]:
    """Return (U,V,c,Dsharp,G) in the frozen item-133 normalization."""
    n_value = 6 * m_value
    power = 4 * m_value + 1
    r0, l0, e0 = mixed_coordinates(n_value, power)
    r1, l1, e1 = mixed_coordinates(n_value, power + 1)
    a_form = l1 * r0 - l0 * r1
    b_form = (l1 * e0 - l0 * e1) / 8

    middle_product = math.prod(
        prime
        for prime in primes_upto(3 * m_value - 1)
        if 2 * m_value < prime < 3 * m_value
    )
    sharp_clearing = 2 ** (9 * m_value + 5) * lcm_upto(power) // middle_product
    x_value = a_form * sharp_clearing
    y_value = b_form * sharp_clearing
    if x_value.denominator != 1 or y_value.denominator != 1:
        raise AssertionError((m_value, x_value, y_value))
    common_cartier = cartier_product(m_value)
    if x_value.numerator % common_cartier or y_value.numerator % common_cartier:
        raise AssertionError((m_value, "Cartier divisor"))
    u_value = x_value.numerator // common_cartier
    v_value = y_value.numerator // common_cartier
    extra_content = math.gcd(abs(u_value), abs(v_value))
    return u_value, v_value, extra_content, sharp_clearing, common_cartier


def atan_reciprocal_bounds(inverse: int, terms: int) -> tuple[Fraction, Fraction]:
    """Alternating-series enclosure for atan(1/inverse)."""
    if inverse <= 1 or terms <= 0:
        raise ValueError((inverse, terms))
    total = Fraction()
    power = Fraction(1, inverse)
    square = Fraction(1, inverse * inverse)
    for index in range(terms):
        summand = power / (2 * index + 1)
        total = total + summand if index % 2 == 0 else total - summand
        power *= square
    next_magnitude = power / (2 * terms + 1)
    if (terms - 1) % 2 == 0:
        return total - next_magnitude, total
    return total, total + next_magnitude


def machin_pi_bounds(decimal_digits: int) -> tuple[Fraction, Fraction, dict[str, int]]:
    """Enclose pi via pi=16 atan(1/5)-4 atan(1/239)."""
    safety = 12
    terms_5 = math.ceil((decimal_digits + safety) * math.log(10) / (2 * math.log(5)))
    terms_239 = math.ceil(
        (decimal_digits + safety) * math.log(10) / (2 * math.log(239))
    )
    low_5, high_5 = atan_reciprocal_bounds(5, terms_5)
    low_239, high_239 = atan_reciprocal_bounds(239, terms_239)
    lower = 16 * low_5 - 4 * high_239
    upper = 16 * high_5 - 4 * low_239
    if not lower < upper:
        raise AssertionError("Invalid Machin enclosure")
    return lower, upper, {"terms_5": terms_5, "terms_239": terms_239}


def oriented_form_exact(
    u_value: int,
    v_value: int,
    content: int,
    pi_lower: Fraction,
    pi_upper: Fraction,
) -> tuple[int, int, int, Fraction, Fraction]:
    """Return a,b,epsilon and an exact positive interval for a+epsilon*b*pi."""
    if v_value >= 0:
        raw_lower = Fraction(u_value) + v_value * pi_lower
        raw_upper = Fraction(u_value) + v_value * pi_upper
    else:
        raw_lower = Fraction(u_value) + v_value * pi_upper
        raw_upper = Fraction(u_value) + v_value * pi_lower
    if raw_lower > 0:
        sigma = 1
        value_lower, value_upper = raw_lower / content, raw_upper / content
    elif raw_upper < 0:
        sigma = -1
        value_lower, value_upper = -raw_upper / content, -raw_lower / content
    else:
        raise AssertionError("Pi enclosure is not fine enough to orient the form")
    a_value = sigma * (u_value // content)
    signed_b = sigma * (v_value // content)
    epsilon = 1 if signed_b > 0 else -1
    b_value = abs(signed_b)
    if math.gcd(abs(a_value), b_value) != 1:
        raise AssertionError((a_value, b_value))
    return a_value, b_value, epsilon, value_lower, value_upper


def fraction_digest(value: Fraction) -> dict[str, object]:
    encoded = f"{value.numerator}/{value.denominator}".encode("ascii")
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "numerator_digits": len(str(abs(value.numerator))),
        "denominator_digits": len(str(value.denominator)),
        "sha256": hashlib.sha256(encoded).hexdigest(),
    }


def integer_digest(value: int) -> dict[str, object]:
    encoded = str(value).encode("ascii")
    return {
        "value": str(value),
        "digits": len(str(abs(value))),
        "sha256": hashlib.sha256(encoded).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=100)
    parser.add_argument("--search-factor", type=int, default=2)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    raw_rows = []
    maximum_digits = 0
    for m_value in range(1, args.max_m + 1):
        u_value, v_value, content, sharp_clearing, common_cartier = exact_pi_pair(
            m_value
        )
        maximum_digits = max(
            maximum_digits, len(str(abs(u_value))), len(str(abs(v_value)))
        )
        raw_rows.append(
            (m_value, u_value, v_value, content, sharp_clearing, common_cartier)
        )

    pi_lower, pi_upper, machin_data = machin_pi_bounds(maximum_digits + 40)
    if not (Fraction(3) < pi_lower < pi_upper < Fraction(22, 7)):
        raise AssertionError("Coarse pi sanity bound failed")

    beta = beta_pairs(args.search_factor * args.max_m)
    rows = []
    all_lower_bounds_gt_one = True
    for (
        m_value,
        u_value,
        v_value,
        content,
        sharp_clearing,
        common_cartier,
    ) in raw_rows:
        a_value, b_value, epsilon, form_lower, form_upper = oriented_form_exact(
            u_value, v_value, content, pi_lower, pi_upper
        )
        required_parity = 0 if epsilon == 1 else 1
        maximum_n = args.search_factor * m_value
        best_lower: Fraction | None = None
        best_index = -1
        best_data: tuple[int, int, int] | None = None
        maximum_gamma_numerator = 0
        maximum_gamma_index = -1
        maximum_gamma_parts: tuple[int, int] | None = None
        admissible_count = 0
        candidate_transcript = hashlib.sha256()
        for index in range(1, maximum_n + 1):
            if index % 2 != required_parity:
                continue
            admissible_count += 1
            p_beta, q_beta = beta[index]
            delta = math.gcd(b_value, q_beta)
            b0 = b_value // delta
            q0 = q_beta // delta
            p_star = b0 * p_beta - epsilon * q0 * a_value
            final_content = math.gcd(abs(p_star), delta)
            e_lower = Fraction(math.factorial(index), math.factorial(2 * index + 1))
            matched_lower = (b0 * e_lower + q0 * form_lower) / final_content
            candidate_transcript.update(
                (
                    f"{index}:{matched_lower.numerator}/"
                    f"{matched_lower.denominator}\n"
                ).encode("ascii")
            )
            if best_lower is None or matched_lower < best_lower:
                best_lower = matched_lower
                best_index = index
                best_data = (delta, final_content, q_beta)
            total_content = content * delta * final_content
            if total_content > maximum_gamma_numerator:
                maximum_gamma_numerator = total_content
                maximum_gamma_index = index
                maximum_gamma_parts = (delta, final_content)
        if best_lower is None or best_data is None or maximum_gamma_parts is None:
            raise AssertionError(m_value)
        row_pass = best_lower > 1
        all_lower_bounds_gt_one &= row_pass
        delta_best, final_best, q_beta_best = best_data
        delta_gamma, final_gamma = maximum_gamma_parts
        rows.append(
            {
                "m": m_value,
                "n": 6 * m_value,
                "epsilon": epsilon,
                "U": integer_digest(u_value),
                "V": integer_digest(v_value),
                "extra_content": str(content),
                "extra_content_log_per_n": log_int(content) / (6 * m_value),
                "primitive_positive_form": {
                    "a": str(a_value),
                    "b": str(b_value),
                    "epsilon": epsilon,
                    "lower": fraction_digest(form_lower),
                    "upper": fraction_digest(form_upper),
                },
                "positive_form_interval_width": fraction_digest(form_upper - form_lower),
                "minimum_positive_match": {
                    "N": best_index,
                    "delta": str(delta_best),
                    "final_content": str(final_best),
                    "q_N": integer_digest(q_beta_best),
                    "lower_bound": fraction_digest(best_lower),
                    "lower_bound_log_per_n": (
                        log_int(best_lower.numerator)
                        - log_int(best_lower.denominator)
                    )
                    / (6 * m_value),
                    "lower_bound_gt_one": row_pass,
                },
                "candidate_scan": {
                    "admissible_count": admissible_count,
                    "canonical_fraction_transcript_sha256": candidate_transcript.hexdigest(),
                },
                "maximum_total_content_in_window": {
                    "N": maximum_gamma_index,
                    "delta": str(delta_gamma),
                    "final_content": str(final_gamma),
                    "total_content": str(maximum_gamma_numerator),
                    "log_per_n": log_int(maximum_gamma_numerator)
                    / (6 * m_value),
                },
                "sharp_clearing": integer_digest(sharp_clearing),
                "cartier_product": integer_digest(common_cartier),
            }
        )
        print(
            f"m={m_value:3d} Nmin={best_index:3d} "
            f"log(lower)/(6m)={rows[-1]['minimum_positive_match']['lower_bound_log_per_n']:.6f} "
            f"pass={row_pass}",
            flush=True,
        )

    payload = {
        "schema": "mixed-cubic-positive-match-exact-scan-v2",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "scope": {
            "m": [1, args.max_m],
            "parity_compatible_N": f"1 <= N <= {args.search_factor}m",
        },
        "theorem_boundary": (
            "Every lower_bound_gt_one entry is an exact finite consequence of "
            "rational Machin bounds and the beta integral bound. This does not "
            "imply an asymptotic obstruction or classify e+pi."
        ),
        "machin_pi_enclosure": {
            **machin_data,
            "decimal_digits_requested": maximum_digits + 40,
            "lower": fraction_digest(pi_lower),
            "upper": fraction_digest(pi_upper),
            "width": fraction_digest(pi_upper - pi_lower),
        },
        "all_positive_matches_in_scope_have_exact_lower_bound_gt_one": all_lower_bounds_gt_one,
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    encoded_bytes = encoded.encode("utf-8")
    # Write bytes so the printed digest is invariant under host newline rules.
    args.output.write_bytes(encoded_bytes)
    print(hashlib.sha256(encoded_bytes).hexdigest())


if __name__ == "__main__":
    main()
