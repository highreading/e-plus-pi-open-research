#!/usr/bin/env python3
"""Exact image lattices for arbitrary O_K multipliers of the n=5 edge.

For q_d*(-i Lambda_d)=u_d*s+v_d in O_K[s], this computes the Smith
invariants of

    theta -> (Tr(theta*u_d), Tr(theta*v_d)),  theta in O_K.

The companion note proves the all-degree rank statement and explains why
rank two makes rational primitivization projectively universal.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

import algebraic_unit_two_log_n5_ideal_content as base


TRACE_GRAM = (
    (4, -2, 0, 0),
    (-2, 6, 0, 0),
    (0, 0, 10, 0),
    (0, 0, 0, 10),
)


def trace_row(coordinates: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(
        sum(TRACE_GRAM[j][k] * coordinates[k] for k in range(4))
        for j in range(4)
    )  # type: ignore[return-value]


def gcd_values(values: list[int] | tuple[int, ...]) -> int:
    answer = 0
    for value in values:
        answer = math.gcd(answer, abs(value))
    return answer


def lattice_record(d: int, eta: base.Kelt, eta_bar: base.Kelt) -> tuple[dict, sp.Matrix]:
    edge = base.edge_integer_data(d, eta, eta_bar)
    u = base.plus_coordinates(edge["u_plus"])
    v = base.plus_coordinates(edge["v_plus"])
    row_u = trace_row(u)
    row_v = trace_row(v)
    matrix = sp.Matrix([row_u, row_v])
    first = gcd_values(list(row_u + row_v))
    minors = [
        row_u[j] * row_v[k] - row_u[k] * row_v[j]
        for j in range(4)
        for k in range(j + 1, 4)
    ]
    determinant_divisor = gcd_values(minors)
    rank = 2 if determinant_divisor else (1 if first else 0)
    second = determinant_divisor // first if rank == 2 else 0

    # Since u lies in Q(sqrt(5)), its last two coordinates vanish.  The
    # resulting block formula is an independent check on all six minors.
    if u[2:] != (0, 0):
        raise AssertionError("coefficient on s left the quadratic subfield")
    block_determinant = row_u[0] * row_v[1] - row_u[1] * row_v[0]
    block_cross = gcd_values([row_u[0], row_u[1]]) * gcd_values(
        [row_v[2], row_v[3]]
    )
    block_determinant_divisor = math.gcd(abs(block_determinant), block_cross)
    if block_determinant_divisor != determinant_divisor:
        raise AssertionError("block formula disagrees with literal minors")

    return (
        {
            "d": d,
            "rank": rank,
            "smith_invariants": [str(first), str(second)] if rank == 2 else [str(first)],
            "image_index": str(determinant_divisor) if rank == 2 else None,
            "second_invariant_digits": len(str(second)) if rank == 2 else 0,
            "q_min_digits": len(str(edge["q_min"])),
            "ordinary_coordinate_content": edge["rational_content"],
            "anti_fixed_constant_coordinates": [str(v[2]), str(v[3])],
            "row_sha256": hashlib.sha256(repr((row_u, row_v)).encode()).hexdigest(),
        },
        matrix,
    )


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/arbitrary_integer_trace_lattice_d200.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/arbitrary_integer_trace_lattice.md"),
    )
    parser.add_argument(
        "--content-result",
        type=Path,
        default=Path("results/algebraic_unit_two_log_n5_ideal_content_d200.json"),
    )
    args = parser.parse_args()
    if args.max_d < 20:
        raise ValueError("max-d must be at least 20")

    eta: base.Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    content_result = json.loads(args.content_result.read_text())
    content_by_d = {
        record["d"]: record for record in content_result["records"]
    }
    if args.max_d > max(content_by_d):
        raise ValueError("content dependency does not cover max-d")

    records = []
    matrices: dict[int, sp.Matrix] = {}
    selected_degrees = {1, 2, 3, 4, 5, 7, 15, 72, args.max_d}
    for d in range(1, args.max_d + 1):
        record, matrix = lattice_record(d, eta, eta_bar)
        record["content_ideal_norm_Lplus"] = content_by_d[d][
            "content_ideal_norm_Lplus"
        ]
        record["content_smith_diagonal_Lplus"] = content_by_d[d][
            "smith_diagonal_Lplus"
        ]
        records.append(record)
        if d in selected_degrees:
            matrices[d] = matrix

    if records[0]["rank"] != 1:
        raise AssertionError("d=1 should be the zero-s-coefficient degeneration")
    if not all(record["rank"] == 2 for record in records[1:]):
        raise AssertionError("a rank defect occurred for d>=2")

    first_pattern = all(
        int(record["smith_invariants"][0])
        == (10 if record["d"] % 5 == 2 else 2)
        for record in records[1:]
    )
    if not first_pattern:
        raise AssertionError("finite first-invariant residue pattern failed")

    # Exact low-degree half of the all-degree rank proof: the source note
    # proves nonvanishing analytically for d>=20.
    low_degree_anti_checks = [
        {
            "d": record["d"],
            "anti_fixed_constant_coordinates": record[
                "anti_fixed_constant_coordinates"
            ],
            "nonzero": any(
                int(value) != 0
                for value in record["anti_fixed_constant_coordinates"]
            ),
        }
        for record in records[1:19]
    ]
    if not all(item["nonzero"] for item in low_degree_anti_checks):
        raise AssertionError("low-degree anti-fixed coordinate vanished")

    # The rational inequality used after the explicit remainder estimates:
    # 36*(5/8)^20 < 24/125 iff 375*5^20 < 2*8^20.
    analytic_bound_check = 375 * 5**20 < 2 * 8**20
    if not analytic_bound_check:
        raise AssertionError("the exact d>=20 domination inequality failed")

    selected_records = []
    for d in sorted(matrices):
        matrix = matrices[d]
        item = {
            "d": d,
            "trace_matrix": [[str(int(x)) for x in row] for row in matrix.tolist()],
        }
        if d >= 2:
            hnf = hermite_normal_form(matrix)
            first, second = map(int, records[d - 1]["smith_invariants"])
            if abs(int(hnf.det())) != first * second:
                raise AssertionError("HNF determinant disagrees with Smith index")
            item["column_hermite_basis"] = [
                [str(int(x)) for x in row] for row in hnf.tolist()
            ]
            item["contains_second_invariant_times_Z2"] = True
        selected_records.append(item)

    # At d=2 the universality has an especially simple literal witness.
    expected_d2 = sp.Matrix(
        [[10, -10, 0, 0], [-20, 20, 50, -50]]
    )
    if matrices[2] != expected_d2:
        raise AssertionError("unexpected d=2 trace matrix")
    p_symbol, q_symbol = sp.symbols("P Q", integer=True)
    witness = sp.Matrix([5 * p_symbol, 0, q_symbol + 2 * p_symbol, 0])
    witness_image = expected_d2 * witness
    if witness_image != sp.Matrix([50 * p_symbol, 50 * q_symbol]):
        raise AssertionError("d=2 universal witness failed")

    compact_rows = [
        (
            record["d"],
            record["rank"],
            tuple(record["smith_invariants"]),
            record["row_sha256"],
        )
        for record in records
    ]
    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependency_script = Path(base.__file__).resolve()
    content_path = args.content_result.resolve()
    result = {
        "description": (
            "Exact image lattices of O_K under the two-coordinate trace map "
            "for the minimally cleared n=5,c=f=0 edge."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "arithmetic_dependency_path": str(dependency_script),
        "arithmetic_dependency_sha256": file_sha256(dependency_script),
        "content_result_path": str(content_path),
        "content_result_sha256": file_sha256(content_path),
        "max_d": args.max_d,
        "integral_basis_trace_gram": TRACE_GRAM,
        "trace_gram_discriminant": int(sp.Matrix(TRACE_GRAM).det()),
        "all_d_ge_2_rank_two": True,
        "finite_first_invariant_pattern": {
            "verified_through": args.max_d,
            "formula_for_d_ge_2": "10 if d=2 mod 5, otherwise 2",
            "matches": first_pattern,
            "interpretation": "positive generator of Tr_{K/Q}(content ideal c_d)",
        },
        "all_degree_rank_certificate": {
            "low_degree_exact_range": "2<=d<=19",
            "low_degree_anti_checks": low_degree_anti_checks,
            "analytic_range": "d>=20",
            "exact_domination_inequality": "375*5^20 < 2*8^20",
            "exact_domination_inequality_holds": analytic_bound_check,
        },
        "d2_projective_universality": {
            "trace_matrix": [
                [int(value) for value in row] for row in expected_d2.tolist()
            ],
            "theta_coordinates_for_target_P_Q": ["5*P", "0", "Q+2*P", "0"],
            "trace_image": ["50*P", "50*Q"],
            "conclusion": "after gcd division, every primitive integer pair (P,Q) occurs already at d=2",
        },
        "selected_exact_matrices": selected_records,
        "all_record_sha256": hashlib.sha256(repr(compact_rows).encode()).hexdigest(),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
