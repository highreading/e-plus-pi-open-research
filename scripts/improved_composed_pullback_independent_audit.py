#!/usr/bin/env python3
"""Independent audit calculations for the improved composed pullback.

No audited project module is imported.  Exact Schur--Cohn arithmetic is done
in a hand-written Q(sqrt(2), i) four-tuple model; composite jets are generated
with integer Bell-polynomial recurrences; and the HP kernels are obtained by
Fraction Gauss--Jordan elimination.  Decimal roots remain diagnostics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp


sys.set_int_max_str_digits(0)
Elt = tuple[Fraction, Fraction, Fraction, Fraction]


def elt(a: int | Fraction = 0, b: int | Fraction = 0,
        c: int | Fraction = 0, d: int | Fraction = 0) -> Elt:
    """Represent a+b*sqrt(2)+i(c+d*sqrt(2))."""
    return (Fraction(a), Fraction(b), Fraction(c), Fraction(d))


def pair_add(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (x[0] + y[0], x[1] + y[1])


def pair_sub(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (x[0] - y[0], x[1] - y[1])


def pair_mul(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def elt_add(x: Elt, y: Elt) -> Elt:
    return tuple(a + b for a, b in zip(x, y))  # type: ignore[return-value]


def elt_neg(x: Elt) -> Elt:
    return tuple(-a for a in x)  # type: ignore[return-value]


def elt_sub(x: Elt, y: Elt) -> Elt:
    return elt_add(x, elt_neg(y))


def elt_mul(x: Elt, y: Elt) -> Elt:
    real_x, imag_x = x[:2], x[2:]
    real_y, imag_y = y[:2], y[2:]
    real = pair_sub(pair_mul(real_x, real_y), pair_mul(imag_x, imag_y))
    imag = pair_add(pair_mul(real_x, imag_y), pair_mul(imag_x, real_y))
    return real + imag


def elt_conjugate(x: Elt) -> Elt:
    return (x[0], x[1], -x[2], -x[3])


def independent_schur_gaps() -> list[Fraction]:
    # Descending coefficients of
    # -(1+i)w^5+sqrt(2)w^4-sqrt(2)w^2/3+5w/6-sqrt(2)/6.
    polynomial = [
        elt(-1, 0, -1, 0),
        elt(0, 1),
        elt(),
        elt(0, Fraction(-1, 3)),
        elt(Fraction(5, 6)),
        elt(0, Fraction(-1, 6)),
    ]
    gaps: list[Fraction] = []
    while len(polynomial) > 1:
        leading = polynomial[0]
        constant = polynomial[-1]
        gap = elt_sub(
            elt_mul(elt_conjugate(leading), leading),
            elt_mul(elt_conjugate(constant), constant),
        )
        assert gap[1:] == (0, 0, 0) and gap[0] > 0
        gaps.append(gap[0])
        reciprocal = [elt_conjugate(value) for value in polynomial[::-1]]
        numerator = [
            elt_sub(
                elt_mul(elt_conjugate(leading), value),
                elt_mul(constant, reverse_value),
            )
            for value, reverse_value in zip(polynomial, reciprocal)
        ]
        assert numerator[-1] == elt()
        polynomial = numerator[:-1]
    assert polynomial[0] == elt(gaps[-1])
    return gaps


def base_f_jet(k: int) -> int:
    if k == 0:
        return 0
    q, residue = divmod(k - 1, 4)
    if residue == 0:
        numerator = 2 * math.factorial(4 * q)
    elif residue == 1:
        numerator = 2 * math.factorial(4 * q + 1)
    elif residue == 2:
        numerator = math.factorial(4 * q + 2)
    else:
        return 0
    denominator = 4**q
    assert numerator % denominator == 0
    value = numerator // denominator
    return -value if q & 1 else value


def composed_jets_by_bell(maximum: int) -> list[int]:
    phi_jets = [0, 1, 0, -1, 5, -5]
    bell = [[0] * (maximum + 1) for _ in range(maximum + 1)]
    bell[0][0] = 1
    for n in range(1, maximum + 1):
        for k in range(1, n + 1):
            bell[n][k] = sum(
                math.comb(n - 1, j - 1)
                * (phi_jets[j] if j < len(phi_jets) else 0)
                * bell[n - j][k - 1]
                for j in range(1, n - k + 2)
            )
    jets = [0]
    for n in range(1, maximum + 1):
        jets.append(sum(base_f_jet(k) * bell[n][k] for k in range(1, n + 1)))
    return jets


def falling(k: int, j: int) -> int:
    return math.factorial(k) // math.factorial(k - j)


def high_matrix(n: int, jets: list[int]) -> list[list[int]]:
    rows = [
        [falling(k, j) for j in range(n + 1)]
        + [falling(k, j) * jets[k - j] for j in range(n + 1)]
        for k in range(n + 1, 3 * n + 1)
    ]
    rows.append([-1] * (n + 1) + [1] * (n + 1))
    return rows


def exact_kernel(matrix: list[list[int]]) -> tuple[int, list[Fraction]]:
    work = [[Fraction(value) for value in row] for row in matrix]
    row_count, column_count = len(work), len(work[0])
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
            work[r] = [
                work[r][j] - multiplier * work[pivot_row][j]
                for j in range(column_count)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    free = [column for column in range(column_count) if column not in pivots]
    assert len(free) == 1
    vector = [Fraction(0)] * column_count
    vector[free[0]] = Fraction(1)
    for r, pivot in enumerate(pivots):
        vector[pivot] = -work[r][free[0]]
    return len(pivots), vector


def primitive_vector(values: list[Fraction]) -> list[int]:
    common_denominator = 1
    for value in values:
        common_denominator = math.lcm(common_denominator, value.denominator)
    integers = [
        value.numerator * (common_denominator // value.denominator)
        for value in values
    ]
    common = 0
    for value in integers:
        common = math.gcd(common, abs(value))
    assert common
    integers = [value // common for value in integers]
    first = next(value for value in integers if value)
    return integers if first > 0 else [-value for value in integers]


def bareiss_determinant(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    n = len(work)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        selected = next((r for r in range(k, n) if work[r][k]), None)
        if selected is None:
            return 0
        if selected != k:
            work[k], work[selected] = work[selected], work[k]
            sign = -sign
        pivot = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = work[i][j] * pivot - work[i][k] * work[k][j]
                assert numerator % previous == 0
                work[i][j] = numerator // previous
            work[i][k] = 0
        previous = pivot
    return sign * work[-1][-1]


def reconstruct_triple(n: int, bc: list[int], jets: list[int]) -> list[int]:
    b = bc[: n + 1]
    c = bc[n + 1 :]
    a: list[Fraction] = []
    for k in range(n + 1):
        derivative = sum(
            falling(k, j) * (b[j] + c[j] * jets[k - j])
            for j in range(k + 1)
        )
        a.append(Fraction(-derivative, math.factorial(k)))
    return primitive_vector(a + [Fraction(value) for value in b + c])


def first_free_coefficient(n: int, triple: list[int], jets: list[int]) -> Fraction:
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    k = 3 * n + 1
    return sum(
        (
            Fraction(b[j] + c[j] * jets[k - j], math.factorial(k - j))
            for j in range(n + 1)
        ),
        Fraction(),
    )


def e_bounds(last_index: int = 300) -> tuple[Fraction, Fraction]:
    partial = sum((Fraction(1, math.factorial(k)) for k in range(last_index + 1)), Fraction())
    return partial, partial + Fraction(1, last_index * math.factorial(last_index))


def atan_bounds(inverse: int, last_even: int) -> tuple[Fraction, Fraction]:
    assert last_even % 2 == 0
    upper = sum(
        (
            (-1 if k & 1 else 1)
            * Fraction(1, (2 * k + 1) * inverse ** (2 * k + 1))
            for k in range(last_even + 1)
        ),
        Fraction(),
    )
    lower = upper - Fraction(1, (2 * last_even + 3) * inverse ** (2 * last_even + 3))
    return lower, upper


def e_plus_pi_bounds() -> tuple[Fraction, Fraction]:
    e_lower, e_upper = e_bounds()
    five_lower, five_upper = atan_bounds(5, 500)
    two39_lower, two39_upper = atan_bounds(239, 120)
    return (
        e_lower + 16 * five_lower - 4 * two39_upper,
        e_upper + 16 * five_upper - 4 * two39_lower,
    )


def power10(exponent: int) -> Fraction:
    return Fraction(10**exponent) if exponent >= 0 else Fraction(1, 10 ** (-exponent))


def floor_log10_positive(value: Fraction) -> int:
    estimate = len(str(value.numerator)) - len(str(value.denominator))
    while value < power10(estimate):
        estimate -= 1
    while value >= power10(estimate + 1):
        estimate += 1
    return estimate


def endpoint_certificate(a: int, b: int, bounds: tuple[Fraction, Fraction]) -> dict:
    lower_s, upper_s = bounds
    lower, upper = sorted((Fraction(a) + b * lower_s, Fraction(a) + b * upper_s))
    assert lower > 0 or upper < 0
    if lower > 0:
        sign = 1
        abs_lower, abs_upper = lower, upper
    else:
        sign = -1
        abs_lower, abs_upper = -upper, -lower
    return {
        "sign": sign,
        "lower_decade": floor_log10_positive(abs_lower),
        "upper_decade": floor_log10_positive(abs_upper),
        "lower_sha256": hashlib.sha256(f"{lower.numerator}/{lower.denominator}".encode()).hexdigest(),
        "upper_sha256": hashlib.sha256(f"{upper.numerator}/{upper.denominator}".encode()).hexdigest(),
    }


def audit_hp(published: dict, jets: list[int]) -> dict:
    assert hashlib.sha256(json.dumps(jets[:47], separators=(",", ":")).encode()).hexdigest() == published[
        "computed_G_jet_sha256"
    ]
    bounds = e_plus_pi_bounds()
    records: list[dict] = []
    decades: list[int] = []
    for source_record in published["records"]:
        n = source_record["n"]
        matrix = high_matrix(n, jets)
        rank, rational_kernel = exact_kernel(matrix)
        bc = primitive_vector(rational_kernel)
        deleted = next(j for j, value in enumerate(bc) if value)
        minor = [row[:deleted] + row[deleted + 1 :] for row in matrix]
        signed_cofactor = bareiss_determinant(minor) * (-1 if deleted & 1 else 1)
        assert signed_cofactor % bc[deleted] == 0
        content = abs(signed_cofactor // bc[deleted])
        triple = reconstruct_triple(n, bc, jets)
        a = triple[: n + 1]
        b = triple[n + 1 : 2 * (n + 1)]
        c = triple[2 * (n + 1) :]
        assert sum(b) == sum(c)
        endpoint_pair = [sum(a), sum(b)]
        endpoint_gcd = math.gcd(abs(endpoint_pair[0]), abs(endpoint_pair[1]))
        reduced = [value // endpoint_gcd for value in endpoint_pair]
        free = first_free_coefficient(n, triple, jets)
        certificate = endpoint_certificate(reduced[0], reduced[1], bounds)
        checks = {
            "shape": [len(matrix), len(matrix[0])] == source_record["shape"],
            "rank": rank == source_record["rank"],
            "nullity": len(matrix[0]) - rank == source_record["nullity"],
            "high_kernel_sha256": hashlib.sha256(
                json.dumps(bc, separators=(",", ":")).encode()
            ).hexdigest()
            == source_record["primitive_high_kernel_sha256"],
            "cofactor_content_digits": len(str(content))
            == source_record["maximal_cofactor_common_content_digits"],
            "triple_height": len(str(max(map(abs, triple))))
            == source_record["primitive_triple_height_digits"],
            "triple_sha256": hashlib.sha256(
                json.dumps(triple, separators=(",", ":")).encode()
            ).hexdigest()
            == source_record["primitive_triple_sha256"],
            "raw_endpoint_pair": endpoint_pair == source_record["raw_endpoint_pair"],
            "endpoint_gcd": endpoint_gcd == source_record["endpoint_gcd"],
            "reduced_endpoint_pair": reduced == source_record["reduced_endpoint_pair"],
            "first_free": {
                "index": 3 * n + 1,
                "numerator": free.numerator,
                "denominator": free.denominator,
                "nonzero": bool(free),
            }
            == source_record["first_free"],
            "endpoint_sign": certificate["sign"]
            == source_record["endpoint_interval_certificate"]["certified_sign"],
            "endpoint_interval_excludes_zero": not source_record["endpoint_interval_certificate"][
                "interval_contains_zero"
            ],
            "endpoint_decades": certificate["lower_decade"]
            == source_record["endpoint_interval_certificate"]["floor_log10_abs_lower"]
            and certificate["upper_decade"]
            == source_record["endpoint_interval_certificate"]["floor_log10_abs_upper"]
            and certificate["lower_decade"]
            == certificate["upper_decade"]
            == source_record["endpoint_interval_certificate"]["single_certified_base10_decade"],
        }
        assert all(checks.values())
        decades.append(certificate["lower_decade"])
        records.append(
            {
                "n": n,
                "all_checked_fields_match": True,
                "cofactor_content_sha256": hashlib.sha256(str(content).encode()).hexdigest(),
                "independent_endpoint_interval": certificate,
            }
        )
    return {"all_records_match": True, "decades": decades, "records": records}


def numeric_root_diagnostic() -> dict:
    mp.mp.dps = 100
    coefficients = [
        -mp.mpf(1) / 24,
        mp.mpf(5) / 24,
        -mp.mpf(1) / 6,
        mp.mpf(0),
        mp.mpf(1),
        -mp.mpc(1, 1),
    ]
    roots = mp.polyroots(coefficients, maxsteps=1000, error=False)
    ordered = sorted(roots, key=abs)
    return {
        "method": "mpmath.polyroots at 100 decimal digits",
        "roots_by_modulus": [
            {
                "real": mp.nstr(mp.re(root), 80),
                "imag": mp.nstr(mp.im(root), 80),
                "modulus": mp.nstr(abs(root), 80),
                "residual": mp.nstr(abs(mp.polyval(coefficients, root)), 12),
            }
            for root in ordered
        ],
        "nearest_to_second_modulus_gap": mp.nstr(abs(ordered[1]) - abs(ordered[0]), 80),
        "nearest_minus_sqrt2": mp.nstr(abs(ordered[0]) - mp.sqrt(2), 80),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate-json", type=Path, required=True)
    parser.add_argument("--hp-json", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    certificate = json.loads(args.certificate_json.read_text())
    hp = json.loads(args.hp_json.read_text())
    gaps = independent_schur_gaps()
    published_gaps = [
        Fraction(item["numerator"], item["denominator"])
        for item in certificate["schur_cohn_positive_gaps"]
    ]
    assert gaps == published_gaps
    jets = composed_jets_by_bell(100)
    jet_sha = hashlib.sha256(json.dumps(jets, separators=(",", ":")).encode()).hexdigest()
    assert jet_sha == certificate["computed_composite_jets_sha256"]
    result = {
        "scope": "Exact independent audit except explicitly diagnostic decimal roots.",
        "schur_cohn": {
            "all_five_gaps_match": True,
            "gaps": [
                {"numerator": gap.numerator, "denominator": gap.denominator}
                for gap in gaps
            ],
        },
        "bell_composition_jets": {
            "maximum_order": 100,
            "all_integral_by_construction": True,
            "sha256": jet_sha,
        },
        "hp_exact_audit": audit_hp(hp, jets),
        "root_diagnostic": numeric_root_diagnostic(),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
