#!/usr/bin/env python3
"""Deterministic certificate for Item 272's complete-row admission test.

The checker reconstructs the six hard Item-250 coefficient sequences by
independent exact arithmetic, verifies the four elementary scalar shift
ratios and Item 271's slope block, proves the scoped degree-seven rank-one
exclusion by full modular rank, and emits only bounded replays (never an
exceptional-prime or zero census).
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ITEM250_NAME = "item250_j2_ordinary_phase_certificate.py"
ITEM271_NAME = "item271_auxiliary_dynamics_certificate.py"
ITEM250_SHA256 = "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce"
ITEM271_SHA256 = "27821646fc3120713082f6f7e848970f16a3ed03cc74d65ccd0cf236a5ff0fdf"
RANK_PRIMES = (1_000_000_007, 1_000_000_009)
RANK_DEGREE = 7
RANK_TERMS = 28


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        path = base / name
        if path.exists():
            return path
    raise FileNotFoundError(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM250_PATH = resolve(ITEM250_NAME)
ITEM271_PATH = resolve(ITEM271_NAME)
if sha256(ITEM250_PATH) != ITEM250_SHA256:
    raise RuntimeError("Item250 checker hash mismatch")
if sha256(ITEM271_PATH) != ITEM271_SHA256:
    raise RuntimeError("Item271 checker hash mismatch")
item250 = load("item272_item250", ITEM250_PATH)
item271 = load("item272_item271", ITEM271_PATH)


def rising(value: Fraction, count: int) -> Fraction:
    result = Fraction(1)
    for index in range(count):
        result *= value + index
    return result


def kernel_coefficients(r: int, plus_power: int) -> list[int]:
    """Coefficients of (1-z)^r(1+z)^plus_power in linear time."""
    coefficients: list[int] = []
    for ell in range(r + plus_power + 1):
        value = 0
        for index in range(plus_power + 1):
            left = ell - index
            if 0 <= left <= r:
                value += (
                    math.comb(plus_power, index)
                    * (-1) ** left
                    * math.comb(r, left)
                )
        coefficients.append(value)
    return coefficients


def b_sum(
    coefficients: list[int], parity: int, n0: Fraction, d0: Fraction
) -> Fraction:
    total = Fraction(0)
    factor = Fraction(1)
    term_index = 0
    for ell in range(parity, len(coefficients), 2):
        if term_index:
            previous = term_index - 1
            factor *= -(-n0 + previous) / (1 - d0 + previous)
        total += coefficients[ell] * factor
        term_index += 1
    return total


def phase_row(r: int) -> dict[str, Fraction]:
    """Independent exact reconstruction of Item 250's six coefficients."""
    if r < 1 or r % 2 != 1 or r % 3 == 0:
        raise ValueError(r)
    qbar = Fraction(-(2 * r + 3), 3)
    k0 = kernel_coefficients(r, 1)
    k1 = kernel_coefficients(r, 4)

    kstar = 2 * r + 3
    alpha = Fraction(1, 1) / (qbar + kstar)
    beta = -alpha
    for k in range(kstar - 2, 0, -2):
        alpha = (1 - (3 * qbar + k) * alpha) / (qbar + k)
        beta = -(3 * qbar + k) * beta / (qbar + k)

    states: list[tuple[Fraction, Fraction, Fraction] | None] = [None] * (r + 5)
    states[0] = (Fraction(1), Fraction(0), Fraction(0))
    states[1] = (Fraction(0), alpha, beta)
    for k in range(r + 3):
        u, v, w = states[k]  # type: ignore[misc]
        denominator = 3 * qbar + k
        states[k + 2] = (
            -(qbar + k) * u / denominator,
            (1 - (qbar + k) * v) / denominator,
            -(qbar + k) * w / denominator,
        )

    x0 = [Fraction(0), Fraction(0), Fraction(0)]
    for ell, coefficient in enumerate(k0):
        for coordinate in range(3):
            x0[coordinate] += coefficient * (
                states[ell + 1][coordinate] + states[ell + 3][coordinate]  # type: ignore[index]
            )
    x1 = [Fraction(0), Fraction(0), Fraction(0)]
    for ell, coefficient in enumerate(k1):
        for coordinate in range(3):
            x1[coordinate] += coefficient * states[ell][coordinate]  # type: ignore[index]

    n_a = r + qbar + 1
    sa0 = b_sum(k0, 0, n_a, Fraction(r + 1))
    sa1 = b_sum(k1, 1, n_a, Fraction(r + 2))
    ca0 = Fraction((-1) ** r * math.factorial(r), 1) / rising(qbar + 1, r + 1)
    ca1 = Fraction((-1) ** (r + 1) * math.factorial(r + 1), 1) / rising(qbar, r + 2)
    ba0 = ca0 * sa0
    ba1 = ca1 * sa1

    dbar = Fraction(r, 6)
    rbar = -Fraction(r + 2, 2)
    f0 = b_sum(k0, 1, rbar, dbar)
    rho = -dbar / qbar
    f1 = rho * b_sum(k1, 1, rbar, dbar + 1)

    h = (r - 1) // 2
    kappa = (
        Fraction(2 * (4 * h + 5), 9 * (4 * h + 3))
        * (-1) ** h
        * rising(Fraction(5 - 2 * h, 6), h)
        / rising(Fraction(2 * h + 3, 2), h)
    )
    return {
        "f0": f0,
        "f1": f1,
        "P0": 9 * x0[1],
        "P1": 9 * x1[1],
        "H0": 9 * x0[2] - 10 * ba0,
        "H1": 9 * x1[2] - 10 * ba1,
        "kappa": kappa,
    }


def b_value(s: int) -> Fraction:
    return Fraction(
        math.factorial(2 * s - 1) * math.factorial(s - 1),
        math.factorial(3 * s - 1),
    )


def tau_value(r: int, s: int) -> Fraction:
    h = (r - 1) // 2
    return (
        Fraction((-1) ** (s + h) * 2, 3)
        * rising(Fraction(s), h + 1)
        / rising(Fraction(3 * s + 1), h + 1)
    )


def b_multiplier(s: int) -> Fraction:
    numerator = math.prod(3 * s - index for index in range(1, 7))
    denominator = (
        (2 * s - 1) * (2 * s - 2) * (2 * s - 3) * (2 * s - 4)
        * (s - 1) * (s - 2)
    )
    return Fraction(numerator, denominator)


def kappa_multiplier(r: int) -> Fraction:
    return Fraction(
        r * (r + 2) * (r + 4) * (r + 6) * (2 * r + 15),
        27 * (2 * r + 3) * (2 * r + 5) * (2 * r + 7)
        * (2 * r + 11) * (2 * r + 13),
    )


def tau_multiplier(r: int, s: int) -> Fraction:
    h = (r - 1) // 2
    numerator = -(
        (s - 2) * (s - 1) * (s + h + 1)
        * (3 * s + h - 1) * (3 * s + h) * (3 * s + h + 1)
    )
    denominator = math.prod(range(3 * s - 5, 3 * s + 1))
    return Fraction(numerator, denominator)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest_rows(rows: list[list[Any]]) -> str:
    text = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def modular_value(value: Fraction, prime: int) -> int:
    denominator = value.denominator % prime
    if denominator == 0:
        raise AssertionError(("nonunit rank denominator", value, prime))
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def modular_rank(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
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
        work[pivot_row] = [(entry * inverse) % prime for entry in work[pivot_row]]
        for row in range(pivot_row + 1, row_count):
            if work[row][column]:
                multiplier = work[row][column]
                work[row] = [
                    (left - multiplier * right) % prime
                    for left, right in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def canonical_reconstruction_check() -> dict[str, Any]:
    rows: list[list[Any]] = []
    checks = 0
    for phase, start in ((5, 1), (1, 5)):
        for offset in range(6):
            r = start + 6 * offset
            fast = phase_row(r)
            data = item250.phase_data(r)
            item250.reversal_certificate(r, data)
            f0, f1 = data["st"]
            _, b0, d0 = data["x0"]
            _, b1, d1 = data["x1"]
            ba0, ba1 = data["ba"]
            canonical = {
                "f0": f0,
                "f1": f1,
                "P0": 9 * b0,
                "P1": 9 * b1,
                "H0": 9 * d0 - 10 * ba0,
                "H1": 9 * d1 - 10 * ba1,
                "kappa": data["kappa"],
            }
            assert fast == canonical
            rows.append([phase, r] + [fraction_text(fast[key]) for key in fast])
            checks += len(fast)
    return {
        "phase_rows": 12,
        "coordinate_equalities": checks,
        "row_digest": digest_rows(rows),
        "label": "EXACT FINITE ONLY independent equality replay",
    }


def scalar_update_check() -> dict[str, Any]:
    rows: list[list[Any]] = []
    checks = 0
    for phase, start in ((5, 1), (1, 5)):
        for offset in range(12):
            r = start + 6 * offset
            h = (r - 1) // 2
            s = 3 + offset
            current = phase_row(r)["kappa"]
            following = phase_row(r + 6)["kappa"]
            assert following == kappa_multiplier(r) * current
            assert b_value(s - 2) == b_multiplier(s) * b_value(s)
            assert tau_value(r + 6, s - 2) == tau_multiplier(r, s) * tau_value(r, s)
            assert (s - 2) + (h + 3) == s + h + 1
            rows.append([
                phase,
                r,
                s,
                fraction_text(kappa_multiplier(r)),
                fraction_text(b_multiplier(s)),
                fraction_text(tau_multiplier(r, s)),
            ])
            checks += 4

    slope_checks = 0
    for phase, first in ((5, 1), (1, 3)):
        for delta in range(first, 28, 2):
            d0 = item271.slope_data(phase, delta)[0]
            d2 = item271.slope_data(phase, delta + 2)[0]
            d4 = item271.slope_data(phase, delta + 4)[0]
            p0, _, p2 = item271.recurrence_polynomials(phase, delta)
            assert d4 - d2 == Fraction(p0, p2) * (d2 - d0)
            slope_checks += 1

    return {
        "rank_seven_state": ["1", "c", "B_s", "kappa_r", "tau_(r,s)", "D_delta", "Delta_delta"],
        "scalar_ratio_equalities": checks,
        "slope_block_equalities": slope_checks,
        "ratio_row_digest": digest_rows(rows),
        "forward_range": "s>=3",
        "slope_singular_divisor": "P2^(e)(delta)=0, together with infinity",
        "label": "ratios are proved algebraically; these bounded values are EXACT FINITE ONLY replay",
    }


def rank_one_exclusion() -> dict[str, Any]:
    keys = ("f0", "f1", "P0", "P1", "H0", "H1")
    results: list[dict[str, Any]] = []
    value_rows: list[list[Any]] = []
    for phase, start in ((5, 1), (1, 5)):
        values = [phase_row(start + 6 * index) for index in range(RANK_TERMS)]
        for key in keys:
            ranks: dict[str, int] = {}
            for prime in RANK_PRIMES:
                sequence = [modular_value(row[key], prime) for row in values]
                matrix: list[list[int]] = []
                for n in range(RANK_TERMS - 1):
                    matrix.append(
                        [sequence[n] * pow(n, degree, prime) for degree in range(RANK_DEGREE + 1)]
                        + [sequence[n + 1] * pow(n, degree, prime) for degree in range(RANK_DEGREE + 1)]
                    )
                rank = modular_rank(matrix, prime)
                assert rank == 2 * (RANK_DEGREE + 1)
                ranks[str(prime)] = rank
            results.append({"phase": phase, "sequence": key, "ranks": ranks})
        for index, value in enumerate(values):
            value_rows.append(
                [phase, start + 6 * index]
                + [fraction_text(value[key]) for key in keys]
            )
    return {
        "relation_class": "A(n)*a_n+B(n)*a_(n+1)=0 with deg(A),deg(B)<=7",
        "evaluation_matrix": "27 x 16",
        "terms_per_phase": RANK_TERMS,
        "all_reduced_sequence_denominators_unit_at_both_certificate_primes": True,
        "full_rank_results": results,
        "value_digest": digest_rows(value_rows),
        "logical_consequence": "no nonzero rational-coefficient relation in the displayed class for any of the twelve phase/sequence pairs",
        "scope_limit": "does not exclude higher degree, higher rank, a direct U-module, or creative-telescoping compression",
        "label": "PROVED SCOPED NO-GO, not finite extrapolation",
    }


def endpoint_and_literal_state() -> dict[str, Any]:
    row = phase_row(1)
    assert row["f0"] == 0
    assert row["P0"] == -81
    assert row["H0"] == -33
    return {
        "exact_endpoint": {
            "phase": 5,
            "delta": 1,
            "r": 1,
            "f0": "0",
            "U0": "-81*c-33",
            "row0": "(U0,0,0)",
        },
        "literal_item250_state": {
            "J_indices": "0<=k<=r+4",
            "dimension_growth": "at least r+5 affine J states before coefficient arrays",
            "parameter": "Qbar=-(2r+3)/3",
            "shift": "r->r+6 sends Qbar->Qbar-4 and adds six J indices",
            "consequence": "the literal basis is neither bounded-dimensional nor invariant",
        },
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item272-complete-row-dynamics-certificate-v1",
        "dependencies": {
            ITEM250_NAME: ITEM250_SHA256,
            ITEM271_NAME: ITEM271_SHA256,
        },
        "strict_labels": {
            "partial_rank_seven_translation_module": "PROVED",
            "degree_seven_rank_one_hard_block_admission": "PROVED SCOPED NO-GO",
            "complete_row_bounded_rank_module": "OPEN; NOT CONSTRUCTED",
            "lisse_or_crystalline_frobenius_realization": "OPEN; NOT CONSTRUCTED",
            "bounded_replays": "EXACT FINITE ONLY",
            "exceptional_collision_search": "NONE",
            "positive_linear_capacity_admission": "FAIL",
            "booking": "zero new Route-1 rate; raw ordinary-j=2 capacity remains 2/35 per M = 1/105 per 6M",
        },
        "canonical_reconstruction": canonical_reconstruction_check(),
        "partial_module": scalar_update_check(),
        "rank_one_exclusion": rank_one_exclusion(),
        "endpoint_and_literal_state": endpoint_and_literal_state(),
        "complete_row_admission": {
            "full_row_entries": ["f0", "f1", "U0", "U1", "B_s", "kappa_r", "tau_(r,s)", "D_delta"],
            "closed_entries": ["B_s", "kappa_r", "tau_(r,s)", "D_delta", "c"],
            "smallest_missing_block": "W=(f0,f1,U0,U1), equivalently the q-independent refinement (f0,f1,P0,P1,H0,H1)",
            "fixed_incidence": "conditional only; the universal Item269 incidence still has an external moving row matrix",
            "uniform_conductor_theorem": False,
            "nontrivial_geometric_monodromy_theorem": False,
            "uniform_local_density_theorem": False,
            "raw_capacity": "2/35 per M = 1/105 per 6M",
            "new_capacity_reduction": 0,
        },
        "open": [
            "construct and prove a higher-rank or higher-degree translation update for W=(f0,f1,U0,U1)",
            "regularize the actual reductions on Item271's D-pole divisor",
            "construct a compatible uniform-conductor lisse or crystalline realization with nontrivial monodromy",
            "prove a uniform local-density theorem for the complete fixed incidence",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_result(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
