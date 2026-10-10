#!/usr/bin/env python3
"""Deterministic replay for Item 426.

This checker pins Item 424, reconstructs the exact cellwise first-Witt
gate from the four-section/Hermite recurrence, verifies the explicit j=0
formula, and constructs exact order-at-most-four step-two telescopers over
finite fields on representative actual cells.  It also certifies the cell
capacity and the zero-rate terminal-r band.  Finite rows are diagnostics;
the uniform proofs are given in the report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

import item424_small_prime_witt_escape_certificate as item424


ROOT = Path(__file__).resolve().parents[1]

DEPENDENCIES = {
    "work/item424_small_prime_witt_escape_report.md":
        "3a48bafbdd8f1971d5734dfaf7f1553b0d10939d3a93d9feef0cc19f1babe73f",
    "work/item424_small_prime_witt_escape_certificate.json":
        "8511bdb52f40a001ecbcf6f3720b473c9d063311a66c8b7ae9ca72808ec879fc",
    "work/item424_small_prime_witt_escape_certificate.py":
        "93bb653f6a3a518179a6bc3d66f3c0b8431512d60a89bd1a26c55973e96b5053",
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "sources/mixed_cubic_small_prime_rank_one_cartier_mass.md":
        "593e1f69809c44245bd2d79bf1a503f96d1972a39ba17ea43ba7cd9f4b0e124b",
    "results/item418_normalized_large_carrier_ledger_delta.json":
        "853301f7014dfde6c5edb0cdc8525ef81fcb3c921d8a777155932f8af651d869",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim_mod(poly: list[int], prime: int) -> list[int]:
    answer = [value % prime for value in poly]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def add_mod(left: list[int], right: list[int], prime: int) -> list[int]:
    answer = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] = (answer[index] + value) % prime
    for index, value in enumerate(right):
        answer[index] = (answer[index] + value) % prime
    return trim_mod(answer, prime)


def scale_mod(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim_mod([(scalar * value) % prime for value in poly], prime)


def mul_mod(left: list[int], right: list[int], prime: int) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] = (
                answer[left_index + right_index] + left_value * right_value
            ) % prime
    return trim_mod(answer, prime)


def pow_mod(poly: list[int], exponent: int, prime: int) -> list[int]:
    answer = [1]
    base = trim_mod(poly, prime)
    value = exponent
    while value:
        if value & 1:
            answer = mul_mod(answer, base, prime)
        base = mul_mod(base, base, prime)
        value //= 2
    return answer


def derivative_mod(poly: list[int], prime: int) -> list[int]:
    if len(poly) == 1:
        return [0]
    return trim_mod([index * poly[index] % prime for index in range(1, len(poly))], prime)


def coeff(poly: list[int], index: int) -> int:
    return poly[index] if 0 <= index < len(poly) else 0


def null_vector_mod(matrix: list[list[int]], prime: int) -> list[int]:
    work = [[value % prime for value in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [value * inverse % prime for value in work[pivot_row]]
        for row in range(row_count):
            if row != pivot_row and work[row][column]:
                factor = work[row][column]
                work[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(work[row], work[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    free_columns = [column for column in range(column_count) if column not in pivot_columns]
    if not free_columns:
        raise AssertionError("matrix unexpectedly has zero nullity")
    # Try free columns deterministically until the recurrence part is nonzero.
    for free in free_columns:
        vector = [0] * column_count
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = -work[row][free] % prime
        if any(vector[-5:]):
            return vector
    raise AssertionError("all null vectors found were derivative-only")


U = [0, 1, -1]
Q = [1, 1, 1, 1]


def telescope_witness(prime: int, j_value: int, s_value: int, nu: int) -> dict[str, object]:
    """Construct the uniform actual-step (s -> s+2) telescoper modulo p."""
    assert nu in (0, 1)
    assert 4 * ((2 * j_value + 1) * prime - 2 * s_value - 1) % 16 == 0
    r_value = (prime - 6 * s_value - 3) // 2
    e_value = 2 * s_value - nu
    assert r_value >= 24
    assert s_value + 8 <= (prime - 3) // 6

    u = trim_mod(U, prime)
    q = trim_mod(Q, prime)
    u_prime = derivative_mod(u, prime)
    q_prime = derivative_mod(q, prime)

    # Unknowns are a_0,...,a_44,c_0,...,c_4.  The identity is
    # sum c_k Q^(4k)U^(6(4-k)) =
    # UQ A' + {U(e+1)Q' + (r-23)QU'}A.
    a_columns: list[list[int]] = []
    for degree in range(45):
        basis = [0] * degree + [1]
        first = mul_mod(mul_mod(u, q, prime), derivative_mod(basis, prime), prime)
        bracket = add_mod(
            scale_mod(mul_mod(u, q_prime, prime), e_value + 1, prime),
            scale_mod(mul_mod(q, u_prime, prime), r_value - 23, prime),
            prime,
        )
        operator = add_mod(first, mul_mod(bracket, basis, prime), prime)
        a_columns.append(scale_mod(operator, -1, prime))

    c_columns = [
        mul_mod(pow_mod(q, 4 * k, prime), pow_mod(u, 6 * (4 - k), prime), prime)
        for k in range(5)
    ]
    columns = a_columns + c_columns
    matrix = [
        [coeff(column, degree) for column in columns]
        for degree in range(49)
    ]
    vector = null_vector_mod(matrix, prime)
    a_poly = trim_mod(vector[:45], prime)
    recurrence = [value % prime for value in vector[45:]]
    assert any(recurrence)

    left = [0]
    for k, c_value in enumerate(recurrence):
        term = mul_mod(pow_mod(q, 4 * k, prime), pow_mod(u, 6 * (4 - k), prime), prime)
        left = add_mod(left, scale_mod(term, c_value, prime), prime)
    right = add_mod(
        mul_mod(mul_mod(u, q, prime), derivative_mod(a_poly, prime), prime),
        mul_mod(
            add_mod(
                scale_mod(mul_mod(u, q_prime, prime), e_value + 1, prime),
                scale_mod(mul_mod(q, u_prime, prime), r_value - 23, prime),
                prime,
            ),
            a_poly,
            prime,
        ),
        prime,
    )
    assert trim_mod(left, prime) == trim_mod(right, prime)

    # Verify the integrated recurrence at x=1 and x=-1 directly from the
    # zero-constant primitives of the five actual shifted polynomials.
    endpoint_checks: dict[str, int] = {}
    for endpoint in (1, prime - 1):
        total = 0
        for k, c_value in enumerate(recurrence):
            shifted_s = s_value + 2 * k
            shifted_r = r_value - 6 * k
            shifted_e = e_value + 4 * k
            p_poly = mul_mod(pow_mod(u, shifted_r, prime), pow_mod(q, shifted_e, prime), prime)
            primitive = [0] + [
                coefficient * pow(index + 1, -1, prime) % prime
                for index, coefficient in enumerate(p_poly)
            ]
            value = 0
            for coefficient in reversed(primitive):
                value = (value * endpoint + coefficient) % prime
            total = (total + c_value * value) % prime
        assert total == 0
        endpoint_checks[str(endpoint if endpoint == 1 else -1)] = total

    return {
        "p": prime,
        "j": j_value,
        "s": s_value,
        "nu": nu,
        "r": r_value,
        "e": e_value,
        "A_degree": len(a_poly) - 1,
        "recurrence_coefficients_c0_to_c4_mod_p": recurrence,
        "recurrence_nonzero": True,
        "polynomial_identity_verified": True,
        "endpoint_recurrence_checks": endpoint_checks,
        "step": "s -> s+2 (equivalently m -> m-1 at fixed p,j)",
    }


def h_vector(prime: int, j_value: int, s_value: int, nu: int) -> list[Fraction]:
    r_value = (prime - 6 * s_value - 3) // 2
    e_value = 2 * s_value - nu
    p_poly = item424.poly_mul(
        item424.poly_power(item424.U_POLY, r_value),
        item424.poly_power(item424.Q, e_value),
    )
    t_poly = item424.primitive_zero(p_poly)
    d_poly = [Fraction(3 * j_value + 1)] + [Fraction(-(5 * j_value + 2))] * 3 + [Fraction(1)]
    n_poly = item424.poly_mul(t_poly, d_poly)
    answer: list[Fraction] = []
    for section in range(5):
        value = Fraction()
        for z_value in range(prime):
            index = prime * section - 4 * z_value
            if 0 <= index < len(n_poly):
                value += n_poly[index]
        answer.append(value)
    return answer


def cell_gate_formula(m_value: int, prime: int, scan_rows: dict[int, dict[str, object]]) -> dict[str, object]:
    bridge = item424.normalized_bridge(m_value, prime, scan_rows)
    j_value = int(bridge["cell_j"])
    s_value = int(bridge["row_s"])
    coordinate_rows: list[tuple[int, int, int]] = []
    h_rows: list[list[int]] = []
    for nu in (0, 1):
        h = h_vector(prime, j_value, s_value, nu)
        numerator = item424.poly_mul(
            item424.poly_power(item424.U_POLY, 3 * j_value), h
        )
        coordinates = item424.mixed_coordinates(numerator, 2 * j_value + 2)
        coordinate_rows.append(
            tuple(item424.mod_fraction(value, prime) for value in coordinates)
        )
        h_rows.append([item424.mod_fraction(value, prime) for value in h])

    kappa = (
        coordinate_rows[1][1] * coordinate_rows[0][0]
        - coordinate_rows[0][1] * coordinate_rows[1][0]
    ) % prime
    assert kappa == bridge["kappa_A_over_p_mod_p"]

    j_zero_formula_verified = None
    if j_value == 0:
        explicit = []
        inverse_two = pow(2, -1, prime)
        inverse_four = pow(4, -1, prime)
        for h in h_rows:
            rational = (h[2] - h[3]) * inverse_four % prime
            logarithmic = (-h[1] + h[3] - 2 * h[4]) * inverse_two % prime
            explicit.append((rational, logarithmic))
        explicit_kappa = (
            explicit[1][1] * explicit[0][0]
            - explicit[0][1] * explicit[1][0]
        ) % prime
        assert explicit_kappa == kappa
        j_zero_formula_verified = True

    return {
        "m": m_value,
        "p": prime,
        "j": j_value,
        "s": s_value,
        "H0_coefficients_mod_p": h_rows[0],
        "H1_coefficients_mod_p": h_rows[1],
        "endpoint_coordinates_R_L_E_mod_p": [list(row) for row in coordinate_rows],
        "kappa_from_cell_formula": kappa,
        "kappa_from_Item424": bridge["kappa_A_over_p_mod_p"],
        "j_zero_explicit_formula_verified": j_zero_formula_verified,
    }


def capacity_record() -> dict[str, object]:
    getcontext().prec = 70
    pi_value = Decimal(
        "3.1415926535897932384626433832795028841971693993751058209749445923"
    )
    c_f = -Decimal(4) * Decimal(2).ln() + pi_value / Decimal(3).sqrt() + Decimal(3) * Decimal(3).ln()
    cells = []
    for j_value in range(8):
        exact_denominator = 3 * (3 * j_value + 1) * (2 * j_value + 1)
        cells.append({
            "j": j_value,
            "exact_per_6m": f"1/{exact_denominator}",
            "decimal_per_6m": str(Decimal(1) / Decimal(exact_denominator)),
            "already_booked_Item149_overlap": j_value >= 1,
        })
    total = c_f / Decimal(6)
    booked = (c_f - Decimal(2)) / Decimal(6)
    if abs(Decimal(cells[0]["decimal_per_6m"]) - Decimal(1) / Decimal(3)) > Decimal("1e-65"):
        raise AssertionError
    return {
        "whole_ordinary_F_support_first_Witt_radical_ceiling": str(total),
        "j0_unbooked_cell_ceiling": str(Decimal(1) / Decimal(3)),
        "j_ge_1_Item149_overlap_ceiling": str(booked),
        "cell_formula": "C_j=1/[3(3j+1)(2j+1)] per 6m",
        "first_cells": cells,
        "tail_bound": "sum_{j>=J} C_j <= 1/[18(J-1)] for J>=2",
        "terminal_r_band": "r<24 has O(log m) total prime log-mass at each m because p divides one of 6m-r, 0<=r<24",
        "terminal_r_normalized_capacity": "0",
        "proved_ceiling_delta": "0",
        "booked_lower_bound_delta": "0",
        "global_total_content_ceiling_delta": "0",
        "frozen_deficit_delta": "0",
    }


def build_payload() -> dict[str, object]:
    observed_dependencies = {}
    for relative, expected in DEPENDENCIES.items():
        observed = sha256(ROOT / relative)
        if observed != expected:
            raise AssertionError((relative, observed, expected))
        observed_dependencies[relative] = observed

    scan_rows = item424.scan_rows()
    formula_rows = []
    formula_count = 0
    zero_count = 0
    j_zero_count = 0
    j_zero_explicit_count = 0
    row_stream: list[str] = []
    for m_value in range(1, 61):
        for prime in item424.primes_up_to(6 * m_value):
            if (
                prime != 2
                and prime * prime > 4 * m_value + 1
                and item424.ordinary_rank_zero(m_value, prime)
            ):
                row = cell_gate_formula(m_value, prime, scan_rows)
                formula_count += 1
                zero_count += int(row["kappa_from_cell_formula"] == 0)
                if row["j"] == 0:
                    j_zero_count += 1
                    j_zero_explicit_count += int(row["j_zero_explicit_formula_verified"] is True)
                row_stream.append(
                    f"{m_value},{prime},{row['j']},{row['s']},{row['kappa_from_cell_formula']}"
                )
                if len(formula_rows) < 12 or row["kappa_from_cell_formula"] == 0:
                    formula_rows.append(row)

    telescopers = []
    for prime, j_value, s_value in ((101, 1, 1), (103, 0, 1), (107, 0, 3)):
        for nu in (0, 1):
            telescopers.append(telescope_witness(prime, j_value, s_value, nu))

    capacity = capacity_record()
    witness_core = {
        "formula_count": formula_count,
        "zero_count": zero_count,
        "j0_count": j_zero_count,
        "telescopers": telescopers,
        "capacity": capacity,
    }
    witness_sha = hashlib.sha256(
        json.dumps(witness_core, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()
    return {
        "schema": "item426-witt-cell-recurrence-v1",
        "item": 426,
        "status": "WORK_ONLY_UNAUDITED_EXACT_CELL_RECURRENCE_CAPACITY_LOCALIZATION_NO_BOOKING",
        "generator": Path(__file__).name,
        "generator_sha256": sha256(Path(__file__)),
        "dependency_sha256": observed_dependencies,
        "cell_formula_diagnostic": {
            "range": "1<=m<=60, all Item424 ordinary rank-zero incidences with p^2>4m+1",
            "rows_checked": formula_count,
            "kappa_zeros": zero_count,
            "j0_rows_checked": j_zero_count,
            "j0_explicit_formula_rows_verified": j_zero_explicit_count,
            "row_stream_sha256": hashlib.sha256("\n".join(row_stream).encode("ascii")).hexdigest(),
            "selected_rows": formula_rows,
            "warning": "finite exact diagnostics only; no density inference",
        },
        "actual_step_two_telescopers": telescopers,
        "capacity": capacity,
        "theorem_pinned_to_report": {
            "cell_gate": "kappa=det((R_j(H_0),L_j(H_0)),(R_j(H_1),L_j(H_1))) with H_nu obtained by the exact p-section of T_nu D_j",
            "j0_formula": "R=(h2-h3)/4 and L=(-h1+h3-2h4)/2",
            "recurrence": "away from r<24, each of the four endpoint periods has a nonzero order-at-most-four recurrence in the actual step s->s+2",
            "boundary_capacity": "the omitted r<24 band has zero linear logarithmic capacity",
            "density_status": "the recurrence alone does not bound isolated zeros, so no weighted zero-density or smaller global ceiling is proved",
        },
        "strict_claims": {
            "PROVED": [
                "exact cellwise kappa formula through p-section plus Hermite endpoint recurrence",
                "explicit j=0 determinant formula",
                "uniform nonzero step-two telescoper outside r<24",
                "zero-rate terminal-r band",
                "exact cell capacity C_j and tail bound",
                "zero ledger delta",
            ],
            "OPEN": [
                "weighted zero-density or positive density for kappa",
                "nonconcentration for the order-four finite-field periods",
                "higher Witt depth after kappa vanishes",
                "Route 1 and irrationality of e+pi",
            ],
        },
        "witness_sha256": witness_sha,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--replay", type=Path)
    arguments = parser.parse_args()
    payload = (json.dumps(build_payload(), indent=2, sort_keys=True) + "\n").encode("utf-8")
    if arguments.replay is not None and arguments.replay.read_bytes() != payload:
        raise SystemExit("replay mismatch")
    arguments.output.write_bytes(payload)


if __name__ == "__main__":
    main()
