#!/usr/bin/env python3
"""Independent root audit for Item 242's kernel module and rank witness."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


ROWS = [
    (13, 1, 1),
    (17, 2, 1),
    (29, 5, 1),
    (31, 4, 2),
    (41, 8, 1),
    (53, 11, 1),
    (101, 23, 1),
    (109, 10, 11),
]


def trim(a):
    a = [x for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p, scale_b=1):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] = (out[i] + x) % p
    for i, x in enumerate(b):
        out[i] = (out[i] + scale_b * x) % p
    return trim(out)


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    support_a = [(i, x) for i, x in enumerate(a) if x]
    support_b = [(j, y) for j, y in enumerate(b) if y]
    for i, x in support_a:
        for j, y in support_b:
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def power(a, exponent, p):
    out = [1]
    base = list(a)
    while exponent:
        if exponent & 1:
            out = mul(out, base, p)
        exponent //= 2
        if exponent:
            base = mul(base, base, p)
    return out


def divmod_poly(numerator, denominator, p):
    remainder = trim(numerator)
    denominator = trim(denominator)
    if len(remainder) < len(denominator):
        return [0], remainder
    quotient = [0] * (len(remainder) - len(denominator) + 1)
    lead_inverse = pow(denominator[-1], -1, p)
    while len(remainder) >= len(denominator) and remainder != [0]:
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] * lead_inverse % p
        quotient[shift] = coefficient
        for j, value in enumerate(denominator):
            remainder[shift + j] = (remainder[shift + j] - coefficient * value) % p
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def valuation(polynomial, factor, p):
    value = 0
    quotient = list(polynomial)
    while True:
        next_quotient, remainder = divmod_poly(quotient, factor, p)
        if remainder != [0]:
            return value
        quotient = next_quotient
        value += 1


def harmonic_prefixes(p):
    h = [0] * p
    for k in range(1, p):
        h[k] = (h[k - 1] + pow(k, -1, p)) % p
    return h


def kernel_numerator(p):
    harmonic = harmonic_prefixes(p)
    a0 = [0] * p
    a1 = [0] * p
    b0 = [0] * (2 * p - 1)
    b1 = [0] * (2 * p - 1)
    for k in range(1, p):
        inverse = pow(k, -1, p)
        sign = 1 if k % 2 else -1
        a0[k] = -inverse % p
        a1[k] = harmonic[k - 1] * inverse % p
        b0[2 * k] = sign * inverse % p
        b1[2 * k] = -sign * harmonic[k - 1] * inverse % p
    u = [1] + [0] * (p - 1) + [-1 % p]
    v = [1] + [0] * (2 * p - 1) + [1]
    terms = [
        (4, mul(mul(power(u, 3, p), power(v, 2, p), p), a1, p)),
        (-3, mul(mul(power(u, 4, p), v, p), b1, p)),
        (6, mul(mul(power(u, 2, p), power(v, 2, p), p), mul(a0, a0, p), p)),
        (-12, mul(mul(power(u, 3, p), v, p), mul(a0, b0, p), p)),
        (6, mul(power(u, 4, p), mul(b0, b0, p), p)),
    ]
    numerator = [0]
    for scalar, term in terms:
        numerator = add(numerator, term, p, scalar)
    return trim(numerator), trim(b0)


def actual_w(p, h, s):
    return mul(
        power([1, -1 % p], 2 * h, p),
        power([1, 0, 1], 2 * s - 1, p),
        p,
    )


def p_sections(polynomial, p):
    sections = []
    for residue in range(p):
        section = trim(polynomial[residue::p])
        sections.append(section if section else [0])
    return sections


def evaluate(polynomial, x, p):
    value = 0
    for coefficient in reversed(polynomial):
        value = (value * x + coefficient) % p
    return value


def square_root_minus_one(p):
    for x in range(1, p):
        if x * x % p == p - 1:
            return x
    return None


def section_module_check(p, h, s, numerator):
    q = [1, 0, 1]
    source = mul(numerator, actual_w(p, h, s), p)
    source_valuation = valuation(source, q, p)
    sections = p_sections(source, p)
    if p % 4 == 3:
        witnesses = sum(divmod_poly(section, q, p)[1] != [0] for section in sections)
        module_ok = witnesses > 0
        root_witnesses = {"irreducible_Q_noncancelled_sections": witnesses}
    else:
        iota = square_root_minus_one(p)
        roots = [pow(iota, p, p), pow(-iota % p, p, p)]
        counts = [
            sum(evaluate(section, root, p) != 0 for section in sections)
            for root in roots
        ]
        module_ok = all(counts)
        root_witnesses = {
            "roots": roots,
            "noncancelled_sections_by_root": counts,
            "single_section_coprime_count": sum(
                all(evaluate(section, root, p) != 0 for root in roots)
                for section in sections
            ),
        }
    return {
        "p": p,
        "h": h,
        "s": s,
        "source_q_valuation": source_valuation,
        "expected_q_valuation": 2 * s + 1,
        "module_lcm_q_power_5": module_ok,
        "root_witnesses": root_witnesses,
    }


def kernel_series(numerator, p, maximum):
    # (1+z^(2p))^-5 = sum_j (-1)^j binom(j+4,4) z^(2pj).
    out = [0] * (maximum + 1)
    for j in range(maximum // (2 * p) + 1):
        factor = ((-1) ** j) * math.comb(j + 4, 4)
        shift = 2 * p * j
        for degree, value in enumerate(numerator):
            if degree + shift > maximum:
                break
            out[degree + shift] = (out[degree + shift] + factor * value) % p
    return out


def mode_value(mode, n):
    if mode == 0:
        return 1
    if mode == 1:
        return (1, 0, -1, 0)[n % 4]
    return (0, 1, 0, -1)[n % 4]


def matrix_rank(rows, p):
    matrix = [[x % p for x in row] for row in rows]
    rank = 0
    columns = len(matrix[0]) if matrix else 0
    for column in range(columns):
        pivot = next((r for r in range(rank, len(matrix)) if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, p)
        matrix[rank] = [x * inverse % p for x in matrix[rank]]
        for r in range(len(matrix)):
            if r != rank and matrix[r][column]:
                factor = matrix[r][column]
                matrix[r] = [
                    (x - factor * y) % p
                    for x, y in zip(matrix[r], matrix[rank])
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def rank_witness_29(numerator):
    p, h, s = 29, 5, 1
    maximum = 90
    kernel = kernel_series(numerator, p, maximum)
    functional_rows = []
    for denominator_power in (1, 2):
        for mode in range(3):
            row = []
            for d in range(13):
                denominator = p + 2 * h + d + 1
                row.append(
                    mode_value(mode, denominator)
                    * pow(denominator, -denominator_power, p)
                    % p
                )
            functional_rows.append(row)
    target0 = 3 * p - 2 * s - 1
    target1 = 3 * p - 2 * s
    short0 = [1, 1, 1, 1]
    short1 = [1, 4, 6, 4, 1]
    e_rows = []
    for target, short in ((target0, short0), (target1, short1)):
        row = []
        for d in range(13):
            value = 0
            for j, coefficient in enumerate(short):
                index = target - d - j
                if 0 <= index < len(kernel):
                    value += coefficient * kernel[index]
            row.append(value % p)
        e_rows.append(row)
    ranks = [
        matrix_rank(functional_rows, p),
        matrix_rank(functional_rows + e_rows[:1], p),
        matrix_rank(functional_rows + e_rows, p),
    ]
    matrix_columns = list(zip(*(functional_rows + e_rows)))
    payload = "".join(",".join(map(str, row)) + "\n" for row in matrix_columns)
    return {
        "ranks": ranks,
        "matrix_sha256": hashlib.sha256(payload.encode("ascii")).hexdigest(),
        "matrix_shape": [13, 8],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    failures = []
    kernel_cache = {}
    row_results = []
    for p, h, s in ROWS:
        if p != 4 * h + 6 * s + 3:
            failures.append(["row_equation", p, h, s])
            continue
        if p not in kernel_cache:
            numerator, b0 = kernel_numerator(p)
            q = [1, 0, 1]
            kernel_cache[p] = numerator
            b_valuation = valuation(b0, q, p)
            r_valuation = valuation(numerator, q, p)
            if b_valuation != 1 or r_valuation != 2:
                failures.append(["kernel_valuation", p, b_valuation, r_valuation])
        result = section_module_check(p, h, s, kernel_cache[p])
        row_results.append(result)
        if (
            result["source_q_valuation"] != result["expected_q_valuation"]
            or not result["module_lcm_q_power_5"]
        ):
            failures.append(["section_module", result])

    rank_result = rank_witness_29(kernel_cache[29])
    if rank_result["ranks"] != [6, 7, 8]:
        failures.append(["rank", rank_result])

    result = {
        "schema": "item242-root-independent-audit-v1",
        "classification": "EXACT_INDEPENDENT_AUDIT",
        "rows": row_results,
        "rank_witness": rank_result,
        "kernel_primes": sorted(kernel_cache),
        "failures": failures,
        "all_pass": not failures,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
