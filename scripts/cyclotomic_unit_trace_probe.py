#!/usr/bin/env python3
"""Exact unit-trace probe for the n=5 two-log Rivoal edge.

The proved statements are in sources/cyclotomic_unit_trace_rationalization.md.
This script verifies the exact field/unit identities and rational primitive
pairs.  The bounded exponent search and continuous log-lattice balancing
records are diagnostics only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp

import algebraic_unit_two_log_n5_ideal_content as base


Pair = base.Pair
Kelt = base.Kelt
ZERO_PAIR: Pair = (base.ZERO, base.ZERO)
ONE_PAIR: Pair = (base.ONE, base.ZERO)


def padd(a: Pair, b: Pair) -> Pair:
    return (base.kadd(a[0], b[0]), base.kadd(a[1], b[1]))


def pneg(a: Pair) -> Pair:
    return (base.kneg(a[0]), base.kneg(a[1]))


def pscale(n: int, a: Pair) -> Pair:
    return (base.kscale(n, a[0]), base.kscale(n, a[1]))


def plus_from_coordinates(coordinates: tuple[int, int, int, int] | list[int]) -> Pair:
    answer = ZERO_PAIR
    for coefficient, basis in zip(coordinates, base.BPLUS):
        answer = padd(answer, pscale(int(coefficient), basis))
    return answer


def pinverse_unit(a: Pair) -> Pair:
    matrix = base.plus_multiplication_matrix(a)
    if abs(int(matrix.det())) != 1:
        raise AssertionError("attempted to invert a nonunit")
    return plus_from_coordinates([int(x) for x in matrix.inv()[:, 0]])


def ppow_unit(a: Pair, exponent: int) -> Pair:
    if exponent < 0:
        a = pinverse_unit(a)
        exponent = -exponent
    answer = ONE_PAIR
    while exponent:
        if exponent & 1:
            answer = base.pmul(answer, a)
        a = base.pmul(a, a)
        exponent //= 2
    return answer


def wpow(w: Pair, exponent: int) -> Pair:
    # w=zeta_20 has exact order 20.
    exponent %= 20
    answer = ONE_PAIR
    while exponent:
        if exponent & 1:
            answer = base.pmul(answer, w)
        w = base.pmul(w, w)
        exponent //= 2
    return answer


def cyclotomic_unit(w: Pair, a: int) -> Pair:
    geometric_sum = ZERO_PAIR
    for j in range(a):
        geometric_sum = padd(geometric_sum, wpow(w, j))
    return base.pmul(wpow(w, (1 - a) // 2), geometric_sum)


def tau(a: Pair) -> Pair:
    """The nontrivial automorphism of K/Q(sqrt(5)): i -> -i."""
    return (a[0], base.kneg(a[1]))


TRACE_GRAM = (
    (4, -2, 0, 0),
    (-2, 6, 0, 0),
    (0, 0, 10, 0),
    (0, 0, 0, 10),
)


def trace_product_coordinates(
    a: tuple[int, int, int, int], b: tuple[int, int, int, int]
) -> int:
    return sum(a[j] * TRACE_GRAM[j][k] * b[k] for j in range(4) for k in range(4))


def primitive_pair(a: int, b: int) -> tuple[int, int, int]:
    common = math.gcd(abs(a), abs(b))
    if common == 0:
        return 0, 0, 0
    a //= common
    b //= common
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return a, b, common


def derangement(d: int) -> int:
    previous = 1
    for n in range(1, d + 1):
        previous = n * previous + (-1) ** n
    return previous


def theta_coordinates(
    powers: list[dict[int, Pair]], exponents: tuple[int, int, int]
) -> tuple[int, int, int, int]:
    answer = ONE_PAIR
    for table, exponent in zip(powers, exponents):
        answer = base.pmul(answer, table[exponent])
    return base.plus_coordinates(answer)


def edge_trace_pair(
    d: int,
    theta_coordinates_value: tuple[int, int, int, int],
    eta: Kelt,
    eta_bar: Kelt,
) -> tuple[int, int, int, int]:
    """Return primitive A,B, trace gcd, and least edge denominator.

    The integral pair in edge_integer_data is q_min*(-i Lambda)=u*s+v.
    Taking the field trace after multiplication by theta gives two integers.
    """
    data = base.edge_integer_data(d, eta, eta_bar)
    u_coordinates = base.plus_coordinates(data["u_plus"])
    v_coordinates = base.plus_coordinates(data["v_plus"])
    a = trace_product_coordinates(theta_coordinates_value, u_coordinates)
    b = trace_product_coordinates(theta_coordinates_value, v_coordinates)
    primitive_a, primitive_b, common = primitive_pair(a, b)
    return primitive_a, primitive_b, common, int(data["q_min"])


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--box", type=int, default=7)
    parser.add_argument("--max-d", type=int, default=30)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/cyclotomic_unit_trace_probe.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/cyclotomic_unit_trace_rationalization.md"),
    )
    args = parser.parse_args()
    if args.box < 1 or args.max_d < 2:
        raise ValueError("box>=1 and max-d>=2 are required")
    mp.mp.dps = 250

    # zeta_20=i*zeta_5^4 in the ambient pair representation.
    w: Pair = (base.ZERO, base.kpow(base.ZETA, 4))
    units = [cyclotomic_unit(w, a) for a in (3, 7, 9)]
    expected_unit_coordinates = [
        (1, 0, -1, 0),
        (2, 1, -1, -1),
        (2, 2, -1, -1),
    ]
    actual_unit_coordinates = [base.plus_coordinates(unit) for unit in units]
    if actual_unit_coordinates != expected_unit_coordinates:
        raise AssertionError("cyclotomic-unit coordinates changed")
    unit_norms = [int(base.plus_multiplication_matrix(unit).det()) for unit in units]
    if unit_norms != [1, 1, 1]:
        raise AssertionError("a proposed cyclotomic unit has nonunit norm")

    u3, u7, u9 = units
    tau_checks = {
        "tau_u3_equals_minus_u7_over_u9": tau(u3)
        == pneg(base.pmul(u7, pinverse_unit(u9))),
        "tau_u7_equals_minus_u3_over_u9": tau(u7)
        == pneg(base.pmul(u3, pinverse_unit(u9))),
        "tau_u9_equals_u9_inverse": tau(u9) == pinverse_unit(u9),
    }
    if not all(tau_checks.values()):
        raise AssertionError("relative automorphism identity failed")

    quadratic_unit = base.pmul(
        u9, base.pmul(pinverse_unit(u3), pinverse_unit(u7))
    )
    quadratic_coordinates = base.plus_coordinates(quadratic_unit)
    if quadratic_coordinates != (1, -1, 0, 0) or tau(quadratic_unit) != quadratic_unit:
        raise AssertionError("u9/(u3*u7) is not the expected quadratic unit")
    quadratic_characteristic = str(
        sp.factor(base.plus_multiplication_matrix(quadratic_unit).charpoly().as_expr())
    )

    eta: Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)

    # Exact collapse of every tested quadratic-unit power to the same
    # primitive truncated-exponential pair.  This is a finite verification
    # of the all-degree algebraic proof in the note.
    quadratic_collapse_records = []
    for d in range(2, args.max_d + 1):
        expected_d = derangement(d)
        factorial = math.factorial(d)
        expected_common = math.gcd(expected_d, factorial)
        expected_pair = (expected_d // expected_common, -factorial // expected_common)
        power_records = []
        for exponent in (-3, -1, 0, 2, 4):
            theta = ppow_unit(quadratic_unit, exponent)
            a, b, trace_common, q_min = edge_trace_pair(
                d, base.plus_coordinates(theta), eta, eta_bar
            )
            if (a, b) != expected_pair:
                raise AssertionError(
                    f"quadratic collapse failed at d={d}, exponent={exponent}"
                )
            power_records.append(
                {
                    "exponent": exponent,
                    "primitive_pair": [str(a), str(b)],
                    "trace_coordinate_gcd_digits": len(str(trace_common)),
                }
            )
        quadratic_collapse_records.append(
            {
                "d": d,
                "expected_reduced_derangement_pair": [
                    str(expected_pair[0]),
                    str(expected_pair[1]),
                ],
                "powers": power_records,
                "q_min_digits": len(str(q_min)),
            }
        )

    # Precompute the bounded exponent cube exactly.
    box = args.box
    powers: list[dict[int, Pair]] = []
    for unit in units:
        powers.append({j: ppow_unit(unit, j) for j in range(-box, box + 1)})
    theta_table = []
    for m3 in range(-box, box + 1):
        for m7 in range(-box, box + 1):
            partial = base.pmul(powers[0][m3], powers[1][m7])
            for m9 in range(-box, box + 1):
                theta = base.pmul(partial, powers[2][m9])
                theta_table.append(
                    (base.plus_coordinates(theta), (m3, m7, m9))
                )
    if len({coordinates for coordinates, _ in theta_table}) != len(theta_table):
        raise AssertionError("unit exponent box contained a duplicate")

    sval = mp.e + mp.pi
    bounded_box_records = []
    for d in range(2, args.max_d + 1):
        edge = base.edge_integer_data(d, eta, eta_bar)
        u_coordinates = base.plus_coordinates(edge["u_plus"])
        v_coordinates = base.plus_coordinates(edge["v_plus"])
        best = None
        identically_zero_count = 0
        for theta_value, exponents in theta_table:
            raw_a = trace_product_coordinates(theta_value, u_coordinates)
            raw_b = trace_product_coordinates(theta_value, v_coordinates)
            a, b, common = primitive_pair(raw_a, raw_b)
            if common == 0:
                identically_zero_count += 1
                continue
            magnitude = abs(mp.mpf(a) * sval + b)
            key = (magnitude, abs(a), exponents, a, b, common)
            if best is None or key[:2] < best[:2]:
                best = key
        if best is None:
            raise AssertionError("bounded box contained only zero forms")
        bounded_box_records.append(
            {
                "d": d,
                "best_exponents": list(best[2]),
                "best_primitive_pair": [str(best[3]), str(best[4])],
                "best_log10_abs": mp.nstr(mp.log10(best[0]), 30),
                "trace_coordinate_gcd_digits": len(str(best[5])),
                "identically_zero_trace_forms": identically_zero_count,
            }
        )

    # Continuous log-lattice minimax diagnostic.  Embeddings are ordered by
    # w -> w^k for k=1,3,7,9; raw edge rates are phi^(-d),phi^d,phi^d,1.
    embedding_indices = (1, 3, 7, 9)
    log_matrix = mp.matrix(
        [
            [
                mp.log(
                    abs(
                        mp.sin(a * k * mp.pi / 20)
                        / mp.sin(k * mp.pi / 20)
                    )
                )
                for a in (3, 7, 9)
            ]
            for k in embedding_indices
        ]
    )
    golden = (1 + mp.sqrt(5)) / 2
    log_golden = mp.log(golden)
    raw_rates = mp.matrix([-log_golden, log_golden, log_golden, 0])
    average_rate = sum(raw_rates) / 4
    target_unit_logs = mp.matrix([average_rate - value for value in raw_rates])
    # The fourth row follows from the norm-one column sums; solve the first 3.
    slope = mp.lu_solve(log_matrix[:3, :], target_unit_logs[:3, :])
    residual = log_matrix * slope - target_unit_logs

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependency_path = Path(base.__file__).resolve()
    result = {
        "description": (
            "Exact algebra/unit/primitive-pair certificate and bounded "
            "diagnostics for cyclotomic-unit traces of the n=5 edge."
        ),
        "scope_warning": (
            "The exponent-box minima and continuous balancing records are "
            "diagnostics only; the source note states the proved height regimes."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependency_path": str(dependency_path),
        "dependency_sha256": file_sha256(dependency_path),
        "field_checks": {
            "integral_basis_trace_gram": TRACE_GRAM,
            "trace_discriminant": int(sp.Matrix(TRACE_GRAM).det()),
            "unit_coordinates_for_a_3_7_9": actual_unit_coordinates,
            "unit_norms": unit_norms,
            "tau_checks": tau_checks,
            "quadratic_unit_coordinates": quadratic_coordinates,
            "quadratic_unit_characteristic_polynomial": quadratic_characteristic,
        },
        "quadratic_subfield_collapse_exact_records": quadratic_collapse_records,
        "bounded_exponent_cube_diagnostics": {
            "box": [-box, box],
            "candidate_count_per_degree": len(theta_table),
            "records": bounded_box_records,
        },
        "continuous_balancing_diagnostic": {
            "embedding_order": list(embedding_indices),
            "raw_exponential_rates_in_log_phi_units": [-1, 1, 1, 0],
            "minimax_rate_in_log_phi_units": "1/4",
            "target_unit_log_vector_in_log_phi_units": [
                "5/4",
                "-3/4",
                "-3/4",
                "1/4",
            ],
            "unit_exponent_slopes": [mp.nstr(value, 50) for value in slope],
            "linear_solve_max_abs_residual": mp.nstr(
                max(abs(value) for value in residual), 20
            ),
            "required_unit_height_scale": "phi^(5*d/4)",
            "balanced_largest_raw_summand_scale": "phi^(d/4) times a power of d",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
