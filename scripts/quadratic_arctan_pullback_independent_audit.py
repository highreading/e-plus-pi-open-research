#!/usr/bin/env python3
"""Independent exact/diagnostic audit for quadratic arctangent pullbacks.

This program deliberately does not import either audited quadratic-pullback
program.  It recomputes the endpoint-matched HP records with a small
Fraction-based row reduction, and recomputes the finite integral-jet box
enumeration with closed polynomial formulas.  All enumeration and jet tests
are exact.  Root moduli in the broad box search remain explicitly diagnostic
floating calculations.
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import heapq
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp


sys.set_int_max_str_digits(0)


def lcm(a: int, b: int) -> int:
    return abs(a // math.gcd(a, b) * b)


def falling(k: int, j: int) -> int:
    return 0 if j > k else math.factorial(k) // math.factorial(k - j)


def primitive_fraction_vector(values: list[Fraction]) -> list[int]:
    common_denominator = 1
    for value in values:
        common_denominator = lcm(common_denominator, value.denominator)
    integers = [value.numerator * (common_denominator // value.denominator) for value in values]
    common = 0
    for value in integers:
        common = math.gcd(common, abs(value))
    assert common
    integers = [value // common for value in integers]
    first = next(value for value in integers if value)
    return integers if first > 0 else [-value for value in integers]


def derivative_jets(p: int, maximum: int) -> list[Fraction]:
    """Expand the rational derivative by coefficient division."""
    derivative_coefficients = [Fraction(0) for _ in range(maximum)]
    middle = p * p - 4 * p + 1
    for m in range((maximum - 1) // 2 + 1):
        rhs = Fraction(4 * (p - 1) * p if m == 0 else 4 * (p - 1) if m == 1 else 0)
        if m >= 1:
            rhs -= middle * derivative_coefficients[2 * m - 2]
        if m >= 2:
            rhs -= derivative_coefficients[2 * m - 4]
        derivative_coefficients[2 * m] = rhs / (p * p)
    jets = [Fraction(0) for _ in range(maximum + 1)]
    for k in range(1, maximum + 1):
        jets[k] = derivative_coefficients[k - 1] * math.factorial(k - 1)
    return jets


def high_matrix(n: int, jets: list[Fraction]) -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    for k in range(n + 1, 3 * n + 1):
        rows.append(
            [Fraction(falling(k, j)) for j in range(n + 1)]
            + [Fraction(falling(k, j)) * jets[k - j] for j in range(n + 1)]
        )
    rows.append([Fraction(-1)] * (n + 1) + [Fraction(1)] * (n + 1))
    return rows


def rref_kernel(matrix: list[list[Fraction]]) -> tuple[int, list[list[Fraction]]]:
    """Return rank and a basis of the right kernel using exact row reduction."""
    work = [row[:] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    pivots: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        selected = next((r for r in range(pivot_row, row_count) if work[r][column]), None)
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        pivot = work[pivot_row][column]
        work[pivot_row] = [value / pivot for value in work[pivot_row]]
        for r in range(row_count):
            if r == pivot_row or not work[r][column]:
                continue
            multiplier = work[r][column]
            work[r] = [work[r][j] - multiplier * work[pivot_row][j] for j in range(column_count)]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    free_columns = [column for column in range(column_count) if column not in pivots]
    basis: list[list[Fraction]] = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free] = Fraction(1)
        for r, pivot in enumerate(pivots):
            vector[pivot] = -work[r][free]
        basis.append(vector)
    return len(pivots), basis


def reconstruct_triple(n: int, bc: list[Fraction], jets: list[Fraction]) -> list[int]:
    b = bc[: n + 1]
    c = bc[n + 1 :]
    a: list[Fraction] = []
    for k in range(n + 1):
        low_jet = Fraction(0)
        for j in range(k + 1):
            low_jet += falling(k, j) * b[j]
            low_jet += falling(k, j) * c[j] * jets[k - j]
        a.append(-low_jet / math.factorial(k))
    return primitive_fraction_vector(a + b + c)


def first_free_coefficient(n: int, triple: list[int], jets: list[Fraction]) -> Fraction:
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    k = 3 * n + 1
    result = Fraction(0)
    for j in range(n + 1):
        result += Fraction(b[j], math.factorial(k - j))
        result += Fraction(c[j], math.factorial(k - j)) * jets[k - j]
    return result


def e_bounds(last_index: int = 300) -> tuple[Fraction, Fraction]:
    partial = sum((Fraction(1, math.factorial(k)) for k in range(last_index + 1)), Fraction())
    return partial, partial + Fraction(1, last_index * math.factorial(last_index))


def atan_adjacent_bounds(inverse: int, last_even_index: int) -> tuple[Fraction, Fraction]:
    assert last_even_index % 2 == 0
    upper = sum(
        (
            (-1 if k & 1 else 1)
            * Fraction(1, (2 * k + 1) * inverse ** (2 * k + 1))
            for k in range(last_even_index + 1)
        ),
        Fraction(),
    )
    lower = upper - Fraction(
        1,
        (2 * last_even_index + 3) * inverse ** (2 * last_even_index + 3),
    )
    return lower, upper


def e_plus_pi_bounds() -> tuple[Fraction, Fraction]:
    e_lower, e_upper = e_bounds()
    five_lower, five_upper = atan_adjacent_bounds(5, 500)
    two39_lower, two39_upper = atan_adjacent_bounds(239, 120)
    return (
        e_lower + 16 * five_lower - 4 * two39_upper,
        e_upper + 16 * five_upper - 4 * two39_lower,
    )


def pow10(exponent: int) -> Fraction:
    return Fraction(10**exponent) if exponent >= 0 else Fraction(1, 10 ** (-exponent))


def floor_log10_positive(value: Fraction) -> int:
    assert value > 0
    estimate = len(str(value.numerator)) - len(str(value.denominator))
    while value < pow10(estimate):
        estimate -= 1
    while value >= pow10(estimate + 1):
        estimate += 1
    return estimate


def endpoint_certificate(a: int, b: int, bounds: tuple[Fraction, Fraction]) -> dict:
    lower_s, upper_s = bounds
    endpoints = sorted((Fraction(a) + b * lower_s, Fraction(a) + b * upper_s))
    lower, upper = endpoints
    assert lower > 0 or upper < 0
    if lower > 0:
        sign = 1
        abs_lower, abs_upper = lower, upper
    else:
        sign = -1
        abs_lower, abs_upper = -upper, -lower
    lower_decade = floor_log10_positive(abs_lower)
    upper_decade = floor_log10_positive(abs_upper)
    return {
        "sign": sign,
        "lower_decade": lower_decade,
        "upper_decade": upper_decade,
        "lower_sha256": hashlib.sha256(f"{lower.numerator}/{lower.denominator}".encode()).hexdigest(),
        "upper_sha256": hashlib.sha256(f"{upper.numerator}/{upper.denominator}".encode()).hexdigest(),
    }


def audit_hp_records(reported: dict) -> dict:
    reported_by_key = {(item["p"], item["n"]): item for item in reported["records"]}
    bounds = e_plus_pi_bounds()
    comparisons: list[dict] = []
    decades: dict[str, list[int]] = {}
    for p in (2, 3, 4, 5):
        decades[str(p)] = []
        for n in range(1, 9):
            jets = derivative_jets(p, 3 * n + 1)
            matrix = high_matrix(n, jets)
            rank, kernel = rref_kernel(matrix)
            assert len(kernel) == 1
            triple = reconstruct_triple(n, kernel[0], jets)
            a = triple[: n + 1]
            b = triple[n + 1 : 2 * (n + 1)]
            c = triple[2 * (n + 1) :]
            assert sum(b) == sum(c)
            endpoint_pair = [sum(a), sum(b)]
            endpoint_gcd = math.gcd(abs(endpoint_pair[0]), abs(endpoint_pair[1]))
            reduced_pair = [value // endpoint_gcd for value in endpoint_pair]
            free = first_free_coefficient(n, triple, jets)
            certificate = endpoint_certificate(reduced_pair[0], reduced_pair[1], bounds)
            published = reported_by_key[(p, n)]
            checks = {
                "rank": rank == published["rank"],
                "nullity": len(kernel) == published["nullity"],
                "shape": [len(matrix), len(matrix[0])] == published["shape"],
                "triple_height": len(str(max(map(abs, triple))))
                == published["primitive_triple_height_digits"],
                "triple_sha256": hashlib.sha256(
                    json.dumps(triple, separators=(",", ":")).encode()
                ).hexdigest()
                == published["primitive_triple_sha256"],
                "endpoint_pair": endpoint_pair == published["endpoint_pair"],
                "endpoint_gcd": endpoint_gcd == published["endpoint_gcd"],
                "reduced_endpoint_pair": reduced_pair == published["reduced_endpoint_pair"],
                "reduced_endpoint_height": len(str(max(map(abs, reduced_pair))))
                == published["reduced_endpoint_height_digits"],
                "first_free": {
                    "index": 3 * n + 1,
                    "numerator": free.numerator,
                    "denominator": free.denominator,
                    "nonzero": bool(free),
                }
                == published["first_free"],
                "endpoint_sign": certificate["sign"]
                == published["endpoint_interval_certificate"]["certified_sign"],
                "endpoint_interval_excludes_zero": not published["endpoint_interval_certificate"][
                    "interval_contains_zero"
                ],
                "endpoint_decades": certificate["lower_decade"]
                == published["endpoint_interval_certificate"]["floor_log10_abs_lower"]
                and certificate["upper_decade"]
                == published["endpoint_interval_certificate"]["floor_log10_abs_upper"]
                and certificate["lower_decade"]
                == certificate["upper_decade"]
                == published["endpoint_interval_certificate"]["single_certified_base10_decade"],
            }
            assert all(checks.values())
            decades[str(p)].append(certificate["lower_decade"])
            comparisons.append(
                {
                    "p": p,
                    "n": n,
                    "all_published_fields_checked_match": True,
                    "independent_interval": certificate,
                }
            )
    return {
        "record_count": len(comparisons),
        "all_records_match": all(item["all_published_fields_checked_match"] for item in comparisons),
        "decades": decades,
        "records": comparisons,
    }


def exact_denominator_formula_checks() -> dict:
    results: dict[str, dict] = {}
    for p in (2, 3, 4, 5):
        jets = derivative_jets(p, 201)
        mismatches: list[dict] = []
        for m in range(101):
            denominator = jets[2 * m + 1].denominator
            if p in (3, 5):
                exponent = 2 * m + 1
                factorial_value = math.factorial(2 * m)
                while factorial_value % p == 0:
                    exponent -= 1
                    factorial_value //= p
                predicted = p**exponent
            elif p == 2:
                predicted = 2 ** max(0, m.bit_count() - 1)
            else:
                predicted = 2 ** (2 * m + m.bit_count())
            if denominator != predicted:
                mismatches.append({"m": m, "actual": denominator, "predicted": predicted})
        results[str(p)] = {"m_range": [0, 100], "mismatches": mismatches}
    return results


def safe_denominator(c: int, d: int, e: int) -> bool:
    """Exact positivity test on [0,1], using c>0."""
    if c + d + e <= 0:
        return False
    if e > 0:
        vertex = Fraction(-d, 2 * e)
        if 0 < vertex < 1:
            return Fraction(c) + d * vertex + e * vertex * vertex > 0
    return True


def jets_are_integral(a: int, b: int, c: int, d: int, e: int, order: int) -> tuple[bool, list[int]]:
    # With N=az+bz^2 and Q=c+dz+ez^2,
    # 4(N'Q-NQ') = 4ac+8bc z+4(bd-ae)z^2.
    top = (4 * a * c, 8 * b * c, 4 * (b * d - a * e))
    bottom = (
        c * c,
        2 * c * d,
        d * d + 2 * c * e + a * a,
        2 * d * e + 2 * a * b,
        e * e + b * b,
    )
    coefficients: list[Fraction] = []
    jets: list[int] = []
    factorial = 1
    for r in range(order):
        if r:
            factorial *= r
        rhs = Fraction(top[r] if r < len(top) else 0)
        for j in range(1, min(r, len(bottom) - 1) + 1):
            rhs -= bottom[j] * coefficients[r - j]
        coefficient = rhs / bottom[0]
        coefficients.append(coefficient)
        jet = coefficient * factorial
        if jet.denominator != 1:
            return False, jets
        jets.append(jet.numerator)
    return True, jets


def singular_radius_float(a: int, b: int, c: int, d: int, e: int) -> float:
    alpha = complex(b, -e)
    beta = complex(a, -d)
    gamma = complex(0, -c)
    if alpha == 0:
        return abs(-gamma / beta)
    square_root = cmath.sqrt(beta * beta - 4 * alpha * gamma)
    return min(abs((-beta + square_root) / (2 * alpha)), abs((-beta - square_root) / (2 * alpha)))


def singular_radius_mp(parameters: tuple[int, int, int, int, int]) -> str:
    a, b, c, d, e = parameters
    alpha = mp.mpc(b, -e)
    beta = mp.mpc(a, -d)
    gamma = mp.mpc(0, -c)
    if alpha == 0:
        radius = abs(-gamma / beta)
    else:
        square_root = mp.sqrt(beta * beta - 4 * alpha * gamma)
        radius = min(abs((-beta + square_root) / (2 * alpha)), abs((-beta - square_root) / (2 * alpha)))
    return mp.nstr(radius, 80)


def audit_box_search(reported: dict) -> dict:
    bound = 16
    c_values = (1, 2, 4, 8, 16)
    order = 25
    tested = 0
    reducible = 0
    integral_candidates: list[tuple[int, int, int, int, int]] = []
    top: list[tuple[float, tuple[int, int, int, int, int]]] = []
    diagnostic_hits: list[tuple[int, int, int, int, int]] = []
    threshold = math.sqrt(2)
    for c in c_values:
        for a in range(-bound, bound + 1):
            if a == 0:
                continue
            for d in range(-bound, bound + 1):
                for e in range(-bound, bound + 1):
                    b = c + d + e - a
                    if abs(b) > bound or a + b == 0:
                        continue
                    if math.gcd(math.gcd(math.gcd(math.gcd(abs(a), abs(b)), c), abs(d)), abs(e)) != 1:
                        continue
                    if b and c * b * b - d * a * b + e * a * a == 0:
                        reducible += 1
                        continue
                    if not safe_denominator(c, d, e):
                        continue
                    tested += 1
                    integral, _ = jets_are_integral(a, b, c, d, e, order)
                    if not integral:
                        continue
                    parameters = (a, b, c, d, e)
                    integral_candidates.append(parameters)
                    radius = singular_radius_float(a, b, c, d, e)
                    if radius > threshold + 1e-12:
                        diagnostic_hits.append(parameters)
                    item = (radius, parameters)
                    if len(top) < 20:
                        heapq.heappush(top, item)
                    elif item > top[0]:
                        heapq.heapreplace(top, item)
    assert tested == reported["primitive_candidates_with_safe_real_path_tested"]
    assert reducible == reported["reducible_parameterizations_skipped"]
    assert len(integral_candidates) == reported["candidates_integral_through_tested_jet_order"]
    assert len(diagnostic_hits) == len(reported["hits"]) == 0
    mp.mp.dps = 100
    ranked = sorted(top, reverse=True)
    return {
        "exact_enumeration": {
            "tested": tested,
            "reducible_skipped": reducible,
            "integral_through_order_25": len(integral_candidates),
            "integral_candidate_tuple_sha256": hashlib.sha256(
                json.dumps(integral_candidates, separators=(",", ":")).encode()
            ).hexdigest(),
            "all_reported_counts_match": True,
        },
        "floating_radius_diagnostic": {
            "precision_note": "Ranking used binary64; listed moduli were then recomputed at 100 decimal digits.",
            "threshold_plus_1e_minus_12_hit_count": len(diagnostic_hits),
            "top_20": [
                {
                    "parameters_A_B_C_D_E": list(parameters),
                    "binary64_radius": radius,
                    "mp_100_digit_radius": singular_radius_mp(parameters),
                }
                for radius, parameters in ranked
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hp-json", type=Path, required=True)
    parser.add_argument("--search-json", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    hp_reported = json.loads(args.hp_json.read_text())
    search_reported = json.loads(args.search_json.read_text())
    result = {
        "scope": "Independent finite audit; root-radius ranking remains diagnostic floating arithmetic.",
        "jet_denominator_formula_finite_checks": exact_denominator_formula_checks(),
        "hp_exact_audit": audit_hp_records(hp_reported),
        "box_search_audit": audit_box_search(search_reported),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
