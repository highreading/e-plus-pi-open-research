#!/usr/bin/env python3
"""Exact certificate for rational tropical walls of the n=5 unit trace.

The companion note supplies the endpoint asymptotics.  This script checks,
with exact cyclotomic-field arithmetic and rational linear algebra:

* the signed Galois action on u_3,u_7,u_9;
* the relation u_3*u_7/u_9=phi^2;
* all six rational pairwise-wall solution sets;
* the quadratic-subfield exponent line and its rate formula.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import algebraic_unit_two_log_n5_ideal_content as base
import cyclotomic_unit_trace_probe as prior


Pair = base.Pair
Kelt = base.Kelt


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def k_automorphism(a: Kelt, k: int) -> Kelt:
    """zeta_5 -> zeta_5^k on Z[zeta_5]."""
    answer = base.ZERO
    for exponent, coefficient in enumerate(a):
        term = base.kpow(base.ZETA, (k * exponent) % 5)
        answer = base.kadd(answer, base.kscale(coefficient, term))
    return answer


def sigma(a: Pair, k: int) -> Pair:
    """w -> w^k, using zeta_5=w^4 and i=w^5."""
    real = k_automorphism(a[0], k)
    imag = k_automorphism(a[1], k)
    if k % 4 == 3:
        imag = base.kneg(imag)
    return real, imag


def product_of_powers(units: list[Pair], exponents: tuple[int, int, int]) -> Pair:
    answer = prior.ONE_PAIR
    for unit, exponent in zip(units, exponents):
        answer = base.pmul(answer, prior.ppow_unit(unit, exponent))
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/cyclotomic_unit_rational_ray_tropical.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/cyclotomic_unit_rational_ray_tropical.md"),
    )
    args = parser.parse_args()

    w: Pair = (base.ZERO, base.kpow(base.ZETA, 4))
    units = [prior.cyclotomic_unit(w, a) for a in (3, 7, 9)]
    u3, u7, u9 = units

    # Columns are exponent vectors of sigma_k(u_3), sigma_k(u_7),
    # sigma_k(u_9) in the original unit basis; signs are recorded separately.
    action_matrices = {
        1: sp.eye(3),
        3: sp.Matrix([[-1, -1, -1], [0, 0, 1], [1, 0, 0]]),
        7: sp.Matrix([[0, 0, 1], [-1, -1, -1], [0, 1, 0]]),
        9: sp.Matrix([[0, 1, 0], [1, 0, 0], [-1, -1, -1]]),
    }
    sign_columns = {
        1: (1, 1, 1),
        3: (1, -1, -1),
        7: (-1, 1, -1),
        9: (-1, -1, 1),
    }

    action_checks: dict[str, bool] = {}
    action_coordinates: dict[str, list[list[int]]] = {}
    for k in (1, 3, 7, 9):
        images = [sigma(unit, k) for unit in units]
        expected_images = []
        for column in range(3):
            exponents = tuple(int(action_matrices[k][row, column]) for row in range(3))
            value = product_of_powers(units, exponents)
            if sign_columns[k][column] == -1:
                value = prior.pneg(value)
            expected_images.append(value)
        passed = images == expected_images
        action_checks[f"sigma_{k}"] = passed
        if not passed:
            raise AssertionError(f"signed action failed for sigma_{k}")
        action_coordinates[str(k)] = [
            list(base.plus_coordinates(image)) for image in images
        ]

    phi = prior.plus_from_coordinates((1, 1, 0, 0))
    phi_squared = base.pmul(phi, phi)
    unit_relation_value = base.pmul(
        base.pmul(u3, u7), prior.pinverse_unit(u9)
    )
    if unit_relation_value != phi_squared:
        raise AssertionError("u3*u7/u9 != phi^2")

    tau = lambda value: sigma(value, 9)
    relative_norm_coordinates = []
    for unit in units:
        relative_norm_coordinates.append(
            list(base.plus_coordinates(base.pmul(unit, tau(unit))))
        )
    minus_phi_squared = prior.pneg(phi_squared)
    if base.pmul(u3, tau(u3)) != minus_phi_squared:
        raise AssertionError("wrong relative norm for u3")
    if base.pmul(u7, tau(u7)) != minus_phi_squared:
        raise AssertionError("wrong relative norm for u7")
    if base.pmul(u9, tau(u9)) != prior.ONE_PAIR:
        raise AssertionError("wrong relative norm for u9")

    h = sp.Matrix([1, 1, -1])
    raw_exponents = {1: -1, 3: 1, 7: 1, 9: 0}
    r_symbols = sp.symbols("r3 r7 r9")
    r_vector = sp.Matrix(r_symbols)
    expected_wall_solutions = {
        (1, 3): sp.FiniteSet((sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(-1, 2))),
        (1, 7): sp.FiniteSet((sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(-1, 2))),
        (1, 9): sp.EmptySet,
        (3, 7): sp.FiniteSet((-r_symbols[2], -r_symbols[2], r_symbols[2])),
        (3, 9): sp.FiniteSet((sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(-1, 4))),
        (7, 9): sp.FiniteSet((sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(-1, 4))),
    }
    wall_records = []
    indices = (1, 3, 7, 9)
    for position, i in enumerate(indices):
        for j in indices[position + 1 :]:
            matrix = action_matrices[i] - action_matrices[j]
            rhs = -sp.Rational(raw_exponents[i] - raw_exponents[j], 2) * h
            solution = sp.linsolve((matrix, rhs), r_symbols)
            if solution != expected_wall_solutions[(i, j)]:
                raise AssertionError(f"unexpected rational wall for {(i, j)}: {solution}")
            wall_records.append(
                {
                    "pair": [i, j],
                    "matrix": [[int(x) for x in row] for row in matrix.tolist()],
                    "rhs": [str(x) for x in rhs],
                    "rank": matrix.rank(),
                    "augmented_rank": matrix.row_join(rhs).rank(),
                    "rational_solution": str(solution),
                }
            )

    # tau-fixed exponent vectors are precisely multiples of (1,1,-1).
    fixed_nullspace = (action_matrices[9] - sp.eye(3)).nullspace()
    if fixed_nullspace != [sp.Matrix([-1, -1, 1])]:
        raise AssertionError("unexpected quadratic-subfield exponent line")
    fixed_sign_parity = "m3+m7 is even automatically when m3=m7"

    c = sp.symbols("c", real=True)
    line_rate_vectors = {}
    expected_rate_multipliers = {
        1: -1 + 2 * c,
        3: 1 - 2 * c,
        7: 1 - 2 * c,
        9: 2 * c,
    }
    for k in indices:
        coefficient_vector = (
            action_matrices[k] * (c * h)
            + sp.Rational(raw_exponents[k], 2) * h
        )
        expected_vector = expected_rate_multipliers[k] * h / 2
        if sp.simplify(coefficient_vector - expected_vector) != sp.zeros(3, 1):
            raise AssertionError(f"line rate formula failed at {k}")
        line_rate_vectors[str(k)] = [str(x) for x in coefficient_vector]

    if sum(action_matrices.values(), sp.zeros(3)) != sp.zeros(3):
        raise AssertionError("unit log rates do not sum to zero")
    if sum(raw_exponents.values()) != 1:
        raise AssertionError("raw endpoint exponents do not sum to one")

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependency_paths = [
        Path(base.__file__).resolve(),
        Path(prior.__file__).resolve(),
    ]
    result = {
        "description": (
            "Exact signed Galois action and rational tropical-wall certificate "
            "for cyclotomic-unit traces of the n=5 edge."
        ),
        "scope_warning": (
            "The exact certificate classifies rational exponential-rate ties. "
            "The companion source proves raw-trace noncancellation from the "
            "accepted endpoint asymptotics; neither artifact bounds the "
            "primitive rational coordinate gcd."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependency_paths
        ],
        "unit_coordinates": {
            str(a): list(base.plus_coordinates(unit))
            for a, unit in zip((3, 7, 9), units)
        },
        "signed_galois_action": {
            "action_matrices": {
                str(k): [[int(x) for x in row] for row in matrix.tolist()]
                for k, matrix in action_matrices.items()
            },
            "sign_columns": {str(k): list(value) for k, value in sign_columns.items()},
            "image_coordinates": action_coordinates,
            "all_exact_checks_pass": all(action_checks.values()),
        },
        "phi_squared_relation": {
            "u3_u7_over_u9_coordinates": list(
                base.plus_coordinates(unit_relation_value)
            ),
            "phi_squared_coordinates": list(base.plus_coordinates(phi_squared)),
            "holds": True,
        },
        "relative_norm_coordinates_u3_u7_u9": relative_norm_coordinates,
        "multiplicative_independence_certificate": {
            "first_step": "relative norm forces a+b=0",
            "second_step_log_matrix": [["-beta", "gamma"], ["gamma", "beta"]],
            "determinant": "-beta^2-gamma^2 != 0",
        },
        "rational_pairwise_walls": wall_records,
        "quadratic_subfield_exponent_line": {
            "span": [1, 1, -1],
            "tau_fixed_nullspace_basis_as_computed": [
                [int(x) for x in fixed_nullspace[0]]
            ],
            "sign_condition": fixed_sign_parity,
        },
        "rates_on_quadratic_line_divided_by_log_phi": {
            "1": "-1+2*c",
            "3": "1-2*c",
            "7": "1-2*c",
            "9": "2*c",
            "exact_coefficient_vectors": line_rate_vectors,
            "rational_upper_wall": "(c,c,-c), c<=1/4",
        },
        "rate_sum_identity": {
            "sum_action_matrices": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            "sum_raw_endpoint_exponents": 1,
            "conclusion": "sum of four rates is log(phi), so max >= log(phi)/4",
        },
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
