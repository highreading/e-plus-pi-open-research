#!/usr/bin/env python3
"""Exact replay for the coupled centered-cosh parity obstruction.

The companion source proves the all-n terminal band.  This script checks
the exact coupled rank criterion on a bounded grid and never promotes the
remaining finite rank pattern to an all-slope theorem.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

from flint import __version__ as flint_version
from flint import fmpq, fmpq_mat


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/centered_cosh_unbalanced_coupled_parity_obstruction.md"
OUTPUT = ROOT / "results/centered_cosh_unbalanced_coupled_parity_certificate.json"

GRID_MIN_N = 5
GRID_MAX_N = 28
RSS_GUARD_KIB = 8 * 1024 * 1024

DEPENDENCIES = {
    "sources/centered_cosh_unbalanced_pade_slope_obstruction.md":
        "a9e1d82af845b01150b4075c26a45425d7907fbc1b48862d9b1ca70bb2e08f00",
    "scripts/centered_cosh_unbalanced_pade_slope_obstruction_certificate.py":
        "193cda9b3eace30006c4ca839dac379212bf340dd5063e0b204a0a12cb81de0b",
    "results/centered_cosh_unbalanced_pade_slope_obstruction_certificate.json":
        "1699b6167fc69c3858fccb33abbdd9c27590a64ee14aa290b7eecfdf0d04db79",
    "results/centered_cosh_unbalanced_pade_slope_obstruction_hashes.sha256":
        "343a7a07d9a7b706caf7752a423b29e4b10be40f3c31cce0bfadc9d7ef978dd5",
}


Polynomial = list[Fraction]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte != 10
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def to_fmpq(value: Fraction | int) -> fmpq:
    value = Fraction(value)
    return fmpq(value.numerator, value.denominator)


def from_fmpq(value: fmpq) -> Fraction:
    return Fraction(int(value.numerator), int(value.denominator))


def trim(poly: Polynomial) -> Polynomial:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [Fraction(0)]


def poly_shift(poly: Polynomial, shift: int) -> Polynomial:
    assert shift >= 0
    return [Fraction(0)] * shift + poly


def poly_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return trim(result)


def matrix_rank(rows: list[list[Fraction]]) -> int:
    if not rows or not rows[0]:
        return 0
    matrix = fmpq_mat([[to_fmpq(value) for value in row] for row in rows])
    return int(matrix.rank())


def matrix_digest(rows: list[list[Fraction]]) -> str:
    digest = hashlib.sha256()
    column_count = len(rows[0]) if rows else 0
    digest.update(f"{len(rows)},{column_count}\n".encode())
    for row in rows:
        for value in row:
            digest.update(f"{value.numerator}/{value.denominator}\n".encode())
    return digest.hexdigest()


def secant_f_coefficients(limit: int) -> list[Fraction]:
    """Coefficients of F(x)=1/(2 cosh(sqrt(x))) without floating point."""
    coefficients = [Fraction(1, 2)]
    for degree in range(1, limit + 1):
        coefficients.append(
            -sum(
                Fraction(1, math.factorial(2 * index))
                * coefficients[degree - index]
                for index in range(1, degree + 1)
            )
        )
    return coefficients


F_COEFFICIENTS = secant_f_coefficients(GRID_MAX_N + 4)


@lru_cache(maxsize=None)
def pade_denominator(numerator_degree: int, denominator_degree: int) -> tuple[Fraction, ...]:
    """Normal Padé denominator, normalized to constant coefficient one."""
    L = numerator_degree
    D = denominator_degree
    assert L >= 0 and D >= 0
    if D == 0:
        return (Fraction(1),)
    matrix = fmpq_mat(
        [
            [
                to_fmpq(F_COEFFICIENTS[row_degree - column])
                for column in range(1, D + 1)
            ]
            for row_degree in range(L + 1, L + D + 1)
        ]
    )
    target = fmpq_mat(
        [
            [to_fmpq(-F_COEFFICIENTS[row_degree])]
            for row_degree in range(L + 1, L + D + 1)
        ]
    )
    solution = matrix.solve(target)
    denominator = [Fraction(1)] + [
        from_fmpq(solution[index, 0]) for index in range(D)
    ]
    assert denominator[-1] != 0
    for row_degree in range(L + 1, L + D + 1):
        convolution = sum(
            denominator[column] * F_COEFFICIENTS[row_degree - column]
            for column in range(D + 1)
        )
        assert convolution == 0
    return tuple(denominator)


@lru_cache(maxsize=None)
def constraint_rank(factor_degree: int, last_constraint: int) -> int:
    d_value = factor_degree
    B_value = last_constraint
    rows = [
        [
            F_COEFFICIENTS[degree - column]
            if degree >= column else Fraction(0)
            for column in range(d_value + 1)
        ]
        for degree in range(d_value + 1, B_value + 1)
    ]
    return matrix_rank(rows)


def block_metadata(n_value: int, t_value: int, epsilon: int) -> dict[str, int]:
    d_value = (n_value - 1 - epsilon) // 2
    B_value = (n_value + t_value - epsilon) // 2
    M_value, sigma = divmod(B_value, 2)
    r_value = d_value - M_value
    equation_count = max(0, B_value - d_value)
    rank = constraint_rank(d_value, B_value)
    dimension = d_value + 1 - rank
    expected_dimension = max(0, 2 * d_value - B_value + 1)
    assert rank == min(equation_count, d_value + 1)
    assert dimension == expected_dimension
    return {
        "epsilon": epsilon,
        "d": d_value,
        "B": B_value,
        "M": M_value,
        "sigma": sigma,
        "r": r_value,
        "factor_dimension": dimension,
        "constraint_rank": rank,
    }


def product_basis(metadata: dict[str, int]) -> list[Polynomial]:
    dimension = metadata["factor_dimension"]
    if dimension == 0:
        return []
    M_value = metadata["M"]
    sigma = metadata["sigma"]
    r_value = metadata["r"]
    assert r_value >= 0
    q_value = list(pade_denominator(M_value + sigma, M_value))
    q_squared = poly_multiply(q_value, q_value)
    if r_value == 0:
        assert sigma == 0 and dimension == 1
        return [q_squared]

    assert M_value >= 2 * r_value - sigma
    g_value = list(
        pade_denominator(
            M_value + 1 - sigma,
            M_value + 2 * sigma - 1,
        )
    )
    qg_value = poly_multiply(q_value, g_value)
    g_squared = poly_multiply(g_value, g_value)
    basis = [
        poly_shift(q_squared, shift)
        for shift in range(2 * r_value - 2 * sigma + 1)
    ]
    basis += [
        poly_shift(qg_value, shift)
        for shift in range(2 * r_value - sigma)
    ]
    basis += [
        poly_shift(g_squared, shift)
        for shift in range(2 * r_value - 1)
    ]
    assert len(basis) == 6 * r_value - 3 * sigma
    return basis


def coefficient_rows(columns: list[Polynomial], degree_limit: int) -> list[list[Fraction]]:
    return [
        [
            column[degree] if degree < len(column) else Fraction(0)
            for column in columns
        ]
        for degree in range(degree_limit + 1)
    ]


def equal_block_reduced_basis(metadata: dict[str, int]) -> list[Polynomial]:
    M_value = metadata["M"]
    sigma = metadata["sigma"]
    r_value = metadata["r"]
    assert r_value >= 1
    q_value = list(pade_denominator(M_value + sigma, M_value))
    g_value = list(
        pade_denominator(
            M_value + 1 - sigma,
            M_value + 2 * sigma - 1,
        )
    )
    q_squared = poly_multiply(q_value, q_value)
    qg_value = poly_multiply(q_value, g_value)
    g_squared = poly_multiply(g_value, g_value)
    basis = [
        poly_shift(q_squared, shift)
        for shift in range(2 * r_value - 2 * sigma + 2)
    ]
    basis += [
        poly_shift(qg_value, shift)
        for shift in range(2 * r_value - sigma + 1)
    ]
    basis += [
        poly_shift(g_squared, shift)
        for shift in range(2 * r_value)
    ]
    expected = 6 * r_value if sigma else 6 * r_value + 3
    assert len(basis) == expected
    return basis


def coupled_row(n_value: int, t_value: int) -> tuple[dict[str, object], list[object]]:
    assert 3 * t_value > n_value
    metadata = [
        block_metadata(n_value, t_value, epsilon)
        for epsilon in (0, 1)
    ]
    columns: list[Polynomial] = []
    for epsilon, block in enumerate(metadata):
        basis = product_basis(block)
        if epsilon:
            basis = [poly_shift(poly, 1) for poly in basis]
        columns.extend(basis)

    full_rows = coefficient_rows(columns, n_value - 1)
    high_rows = full_rows[2:]
    full_rank = matrix_rank(full_rows)
    high_rank = matrix_rank(high_rows)
    low_dimension = full_rank - high_rank
    assert low_dimension >= 0

    equal_leading_nonzero: bool | None = None
    equal_leading_size = 0
    if (
        n_value % 2 == 0
        and t_value % 2 == 1
        and metadata[0]["factor_dimension"] > 0
        and metadata[0]["r"] >= 1
    ):
        assert metadata[0] == {
            **metadata[1],
            "epsilon": 0,
        }
        reduced = equal_block_reduced_basis(metadata[0])
        reduced_rows = coefficient_rows(reduced, n_value - 1)
        reduced_rank = matrix_rank(reduced_rows)
        assert reduced_rank == full_rank == len(reduced)
        assert matrix_rank(
            [
                reduced_rows[row] + full_rows[row]
                for row in range(n_value)
            ]
        ) == full_rank
        equal_leading_size = len(reduced)
        leading_high_rows = list(reversed(reduced_rows))[:equal_leading_size]
        equal_leading_nonzero = (
            matrix_rank(leading_high_rows) == equal_leading_size
        )

    selected = (
        n_value <= 10
        or t_value in {n_value // 3 + 1, n_value - 3, n_value - 2, n_value - 1}
        or (n_value, t_value) in {(16, 7), (20, 7), (24, 9), (28, 11)}
    )
    row: dict[str, object] = {
        "n": n_value,
        "t": t_value,
        "three_t_minus_n": 3 * t_value - n_value,
        "column_count_before_cross_block_relations": len(columns),
        "full_rank": full_rank,
        "high_rank": high_rank,
        "low_survivor_dimension": low_dimension,
        "blocks": metadata,
        "equal_block_leading_jet_size": equal_leading_size,
        "equal_block_leading_jet_nonzero": equal_leading_nonzero,
    }
    if selected:
        row["full_matrix_sha256"] = matrix_digest(full_rows)
        row["high_matrix_sha256"] = matrix_digest(high_rows)
    compact = [
        n_value,
        t_value,
        len(columns),
        full_rank,
        high_rank,
        low_dimension,
        [
            [
                block["d"], block["B"], block["M"], block["sigma"],
                block["r"], block["factor_dimension"],
            ]
            for block in metadata
        ],
        equal_leading_size,
        equal_leading_nonzero,
    ]
    return row, compact


def terminal_assertions(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    lookup = {(int(row["n"]), int(row["t"])): row for row in rows}
    selected: list[dict[str, object]] = []
    for n_value in range(GRID_MIN_N, GRID_MAX_N + 1):
        for offset in (3, 2, 1):
            t_value = n_value - offset
            row = lookup[(n_value, t_value)]
            assert row["low_survivor_dimension"] == 0
            blocks = row["blocks"]
            if n_value % 2 == 0:
                if offset == 1:
                    assert [block["factor_dimension"] for block in blocks] == [0, 0]
                elif offset == 2:
                    assert [block["factor_dimension"] for block in blocks] == [0, 1]
                else:
                    assert [block["factor_dimension"] for block in blocks] == [1, 1]
                    assert blocks[0]["r"] == blocks[1]["r"] == 0
                    assert blocks[0]["sigma"] == blocks[1]["sigma"] == 0
            else:
                assert blocks[1]["factor_dimension"] == 0
                if offset in (1, 2):
                    assert blocks[0]["factor_dimension"] == 1
                else:
                    assert blocks[0]["factor_dimension"] == 2
                    assert blocks[0]["r"] == blocks[0]["sigma"] == 1
                    M_value = blocks[0]["M"]
                    q_value = pade_denominator(M_value + 1, M_value)
                    g_value = pade_denominator(M_value, M_value + 1)
                    k_one = q_value[-1] / g_value[-1]
                    assert k_one != 0 and k_one**3 != 0
            if n_value in {5, 6, 7, 8, 15, 16, 27, 28}:
                selected.append(
                    {
                        "n": n_value,
                        "t": t_value,
                        "offset": offset,
                        "block_dimensions": [
                            block["factor_dimension"] for block in blocks
                        ],
                        "verified_no_low_survivor": True,
                    }
                )
    return selected


def main() -> None:
    started = time.perf_counter()
    dependency_checks: dict[str, dict[str, object]] = {}
    for relative_path, expected_hash in DEPENDENCIES.items():
        actual_hash = sha256(ROOT / relative_path)
        assert actual_hash == expected_hash, (
            f"dependency hash mismatch for {relative_path}: "
            f"expected {expected_hash}, got {actual_hash}"
        )
        dependency_checks[relative_path] = {
            "expected_sha256": expected_hash,
            "actual_sha256": actual_hash,
            "match": True,
        }

    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__))
    assert source_control["clean"] and script_control["clean"]

    rows: list[dict[str, object]] = []
    compact_rows: list[list[object]] = []
    for n_value in range(GRID_MIN_N, GRID_MAX_N + 1):
        for t_value in range(0, n_value):
            if 3 * t_value <= n_value:
                continue
            row, compact = coupled_row(n_value, t_value)
            rows.append(row)
            compact_rows.append(compact)

    assert rows
    assert all(row["low_survivor_dimension"] == 0 for row in rows)
    equal_rows = [
        row for row in rows if row["equal_block_leading_jet_nonzero"] is not None
    ]
    assert equal_rows
    assert all(row["equal_block_leading_jet_nonzero"] for row in equal_rows)
    terminal_rows = terminal_assertions(rows)

    compact_encoding = json.dumps(
        compact_rows, sort_keys=True, separators=(",", ":")
    ).encode()
    selected_rows = [
        row for row in rows
        if "full_matrix_sha256" in row
    ]
    payload = {
        "schema": "centered_cosh_unbalanced_coupled_parity_certificate_v1",
        "logical_scope": {
            "all_parameter": [
                "rank(C)-rank(J) equals the dimension of the coupled low survivor space",
                "the reversed coupled-jet formulation",
                "the equal-block jet reductions",
                "no coupled degree-at-most-one survivor for n>=5 and n-3<=t<=n-1",
                "generic coupled maximal-minor logarithmic height O(n^3)",
            ],
            "finite_only": [
                "full/high rank equality on the bounded all-t grid",
                "nonvanishing of equal-block leading jets on that grid",
            ],
            "not_claimed": [
                "all-slope coupled nonvanishing for 3t>n",
                "a primitive height lower bound",
                "classification of e+pi",
            ],
        },
        "bounded_grid": {
            "n_range": [GRID_MIN_N, GRID_MAX_N],
            "condition": "0<=t<=n-1 and 3t>n",
            "row_count": len(rows),
            "all_full_high_ranks_equal": True,
            "all_equal_block_leading_jets_nonzero": True,
            "compact_rows_sha256": hashlib.sha256(compact_encoding).hexdigest(),
            "selected_rows": selected_rows,
        },
        "terminal_band_checks": {
            "n_range": [GRID_MIN_N, GRID_MAX_N],
            "offsets_n_minus_t": [1, 2, 3],
            "selected_rows": terminal_rows,
            "all_no_low_survivor": True,
            "proof_scope": (
                "The source proves this terminal band for every n>=5; "
                "these rows replay examples only."
            ),
        },
        "dependency_checks": dependency_checks,
        "source_sha256": sha256(SOURCE),
        "control_audit": {"source": source_control, "script": script_control},
        "software": {"python_flint": flint_version},
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "Failure guard only; it neither allocates nor caps the "
                "approximately 50 GiB available Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: exact rational matrix ranks require CPU integer "
                "arithmetic, not floating-point GPU kernels."
            ),
        },
    }

    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_GUARD_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
