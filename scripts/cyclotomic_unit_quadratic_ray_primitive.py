#!/usr/bin/env python3
"""Exact primitive-content diagnostics on quadratic cyclotomic-unit rays.

The companion note proves the primitive no-go without using the finite
diagnostics.  This script verifies the relative-trace reduction and the
two-dimensional Smith gcd formula through d=200 by default.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

import algebraic_unit_two_log_n5_ideal_content as base
import cyclotomic_unit_trace_probe as prior


sys.set_int_max_str_digits(0)


Pair = base.Pair
F_GRAM = sp.Matrix([[2, -1], [-1, 3]])
K_GRAM = (
    (4, -2, 0, 0),
    (-2, 6, 0, 0),
    (0, 0, 10, 0),
    (0, 0, 0, 10),
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def padd(a: Pair, b: Pair) -> Pair:
    return base.kadd(a[0], b[0]), base.kadd(a[1], b[1])


def tau(a: Pair) -> Pair:
    return a[0], base.kneg(a[1])


def relative_trace(a: Pair) -> Pair:
    return padd(a, tau(a))


def f_coordinates(a: Pair) -> tuple[int, int]:
    coordinates = base.plus_coordinates(a)
    if coordinates[2:] != (0, 0):
        raise AssertionError("element did not lie in the quadratic subfield")
    return coordinates[0], coordinates[1]


def k_trace_product(a: Pair, b: Pair) -> int:
    x = base.plus_coordinates(a)
    y = base.plus_coordinates(b)
    return sum(x[j] * K_GRAM[j][k] * y[k] for j in range(4) for k in range(4))


def primitive_pair(a: int, b: int) -> tuple[int, int, int]:
    common = math.gcd(abs(a), abs(b))
    if common == 0:
        return 0, 0, 0
    aa, bb = a // common, b // common
    if aa < 0 or (aa == 0 and bb < 0):
        aa, bb = -aa, -bb
    return aa, bb, common


def relative_matrix(xi: Pair, u: Pair, v: Pair) -> sp.Matrix:
    x = relative_trace(base.pmul(xi, u))
    y = relative_trace(base.pmul(xi, v))
    return sp.Matrix.hstack(sp.Matrix(f_coordinates(x)), sp.Matrix(f_coordinates(y)))


def trace_row(q: Pair) -> sp.Matrix:
    coordinates = sp.Matrix(1, 2, f_coordinates(q))
    return coordinates * F_GRAM


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/cyclotomic_unit_quadratic_ray_primitive_d200.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/cyclotomic_unit_quadratic_ray_primitive.md"),
    )
    args = parser.parse_args()
    if args.max_d < 20:
        raise ValueError("max-d must be at least 20")

    eta: base.Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    w: Pair = (base.ZERO, base.kpow(base.ZETA, 4))
    units = [prior.cyclotomic_unit(w, a) for a in (3, 7, 9)]
    u3, u7, u9 = units
    phi_squared = base.pmul(
        base.pmul(u3, u7), prior.pinverse_unit(u9)
    )
    if base.plus_coordinates(phi_squared) != (2, 1, 0, 0):
        raise AssertionError("wrong quadratic unit")

    offsets = {
        "u3": u3,
        "u7": u7,
        "u9": u9,
        "u3_u7": base.pmul(u3, u7),
    }
    if any(tau(value) == value for value in offsets.values()):
        raise AssertionError("diagnostic offset unexpectedly lay in F")

    slopes = {
        "minus_1_over_2": Fraction(-1, 2),
        "zero": Fraction(0, 1),
        "one_over_4": Fraction(1, 4),
        "one_over_2": Fraction(1, 2),
        "one": Fraction(1, 1),
        "two": Fraction(2, 1),
    }
    selected_degrees = {2, 3, 4, 5, 10, 20, 40, 80, 120, 160, args.max_d}
    summary = {
        (slope_name, offset_name): {
            "slope": str(slope),
            "offset": offset_name,
            "degree_count": 0,
            "rank_one_exceptional_degrees": [],
            "max_gcd": 0,
            "max_gcd_degree": None,
            "max_gcd_digits": 0,
            "max_log_gcd_plus_one_over_d": 0.0,
        }
        for slope_name, slope in slopes.items()
        for offset_name in offsets
    }
    selected_records = []
    compact_records = []
    all_direct_relative_checks = True
    all_smith_checks = True
    all_trace_rows_primitive = True

    for d in range(2, args.max_d + 1):
        edge = base.edge_integer_data(d, eta, eta_bar)
        u, v = edge["u_plus"], edge["v_plus"]
        relative_data = {}
        for offset_name, xi in offsets.items():
            matrix = relative_matrix(xi, u, v)
            determinant = int(matrix.det())
            if determinant:
                diagonal, left, right = smith_normal_decomp(matrix, domain=sp.ZZ)
                if left * matrix * right != diagonal:
                    raise AssertionError("Smith decomposition identity failed")
                alpha = abs(int(diagonal[0, 0]))
                beta = abs(int(diagonal[1, 1]))
                if alpha == 0 or beta % alpha:
                    raise AssertionError("invalid Smith invariant ordering")
                if alpha != math.gcd(*(abs(int(x)) for x in matrix)):
                    raise AssertionError("first determinantal divisor failed")
                if alpha * beta != abs(determinant):
                    raise AssertionError("second determinantal divisor failed")
            else:
                diagonal = left = right = None
                alpha = beta = 0
            relative_data[offset_name] = (
                matrix,
                determinant,
                diagonal,
                left,
                right,
                alpha,
                beta,
            )

        for slope_name, slope in slopes.items():
            if d % slope.denominator:
                continue
            n = slope.numerator * d // slope.denominator
            q = prior.ppow_unit(phi_squared, n)
            row = trace_row(q)
            if math.gcd(abs(int(row[0])), abs(int(row[1]))) != 1:
                all_trace_rows_primitive = False
                raise AssertionError("quadratic trace row was not primitive")

            for offset_name, xi in offsets.items():
                theta = base.pmul(q, xi)
                direct_a = k_trace_product(theta, u)
                direct_b = k_trace_product(theta, v)
                primitive_a, primitive_b, common = primitive_pair(direct_a, direct_b)
                matrix, determinant, diagonal, left, right, alpha, beta = relative_data[
                    offset_name
                ]
                relative_pair = row * matrix
                relative_ok = [int(relative_pair[0]), int(relative_pair[1])] == [
                    direct_a,
                    direct_b,
                ]
                all_direct_relative_checks &= relative_ok
                if not relative_ok:
                    raise AssertionError("relative trace pair disagreed with direct trace")

                smith_ok = None
                z_values = None
                if determinant:
                    assert left is not None
                    z = row * left.inv()
                    z_values = [int(z[0]), int(z[1])]
                    if math.gcd(abs(z_values[0]), abs(z_values[1])) != 1:
                        raise AssertionError("unimodularly transformed row lost primitivity")
                    smith_gcd = math.gcd(
                        abs(alpha * z_values[0]), abs(beta * z_values[1])
                    )
                    simplified_gcd = alpha * math.gcd(
                        abs(z_values[0]), beta // alpha
                    )
                    smith_ok = smith_gcd == simplified_gcd == common
                    all_smith_checks &= smith_ok
                    if not smith_ok:
                        raise AssertionError("Smith gcd formula failed")

                item = summary[(slope_name, offset_name)]
                item["degree_count"] += 1
                if not determinant:
                    item["rank_one_exceptional_degrees"].append(d)
                if common > item["max_gcd"]:
                    item["max_gcd"] = common
                    item["max_gcd_degree"] = d
                    item["max_gcd_digits"] = len(str(common))
                normalized_log = math.log(common + 1) / d
                item["max_log_gcd_plus_one_over_d"] = max(
                    item["max_log_gcd_plus_one_over_d"], normalized_log
                )

                record_tuple = (
                    d,
                    slope_name,
                    offset_name,
                    n,
                    direct_a,
                    direct_b,
                    common,
                    determinant,
                    alpha,
                    beta,
                    tuple(z_values) if z_values is not None else None,
                )
                compact_records.append(record_tuple)
                if d in selected_degrees:
                    selected_records.append(
                        {
                            "d": d,
                            "slope_name": slope_name,
                            "slope": str(slope),
                            "offset": offset_name,
                            "quadratic_power_n": n,
                            "primitive_pair": [str(primitive_a), str(primitive_b)],
                            "ordinary_trace_gcd": str(common),
                            "q_min_digits": len(str(edge["q_min"])),
                            "relative_matrix_rank": matrix.rank(),
                            "relative_matrix_sha256": hashlib.sha256(
                                repr(tuple(int(x) for x in matrix)).encode()
                            ).hexdigest(),
                            "smith_invariants": [str(alpha), str(beta)]
                            if determinant
                            else None,
                            "transformed_primitive_trace_row": [str(x) for x in z_values]
                            if z_values is not None
                            else None,
                            "smith_formula_matches": smith_ok,
                        }
                    )

    summary_records = []
    for key in sorted(summary):
        item = summary[key]
        summary_records.append(
            {
                **item,
                "max_gcd": str(item["max_gcd"]),
                "max_log_gcd_plus_one_over_d": format(
                    item["max_log_gcd_plus_one_over_d"], ".17g"
                ),
            }
        )

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependency_paths = [Path(base.__file__).resolve(), Path(prior.__file__).resolve()]
    result = {
        "description": (
            "Exact relative-trace and Smith diagnostics for primitive content "
            "on selected quadratic cyclotomic-unit rays."
        ),
        "scope_warning": (
            "All finite gcd sizes are diagnostics only. The companion source's "
            "primitive no-go uses the gcd-free value/coefficient quotient."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependency_paths
        ],
        "max_d": args.max_d,
        "quadratic_basis": ["1", "omega=phi-1"],
        "quadratic_trace_gram": [[2, -1], [-1, 3]],
        "trace_row_initial": [2, -1],
        "trace_row_update": [[2, 1], [1, 1]],
        "trace_row_update_determinant": 1,
        "slopes": {name: str(value) for name, value in slopes.items()},
        "offsets": {
            name: list(base.plus_coordinates(value)) for name, value in offsets.items()
        },
        "all_direct_relative_checks_pass": all_direct_relative_checks,
        "all_trace_rows_primitive": all_trace_rows_primitive,
        "all_rank_two_smith_checks_pass": all_smith_checks,
        "compact_record_sha256": hashlib.sha256(
            repr(compact_records).encode()
        ).hexdigest(),
        "summary_diagnostics": summary_records,
        "selected_exact_records": selected_records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
