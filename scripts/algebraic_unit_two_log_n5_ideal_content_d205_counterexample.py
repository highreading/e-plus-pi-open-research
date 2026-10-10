#!/usr/bin/env python3
"""Exact countercertificate to the degree-200 n=5 ideal-content pattern.

All arithmetic is integral.  The reconstruction and integral-basis arithmetic
are imported from the archived finite certificate; this script independently
computes every determinantal divisor of the resulting 4-by-8 lattice matrix.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp

import algebraic_unit_two_log_n5_ideal_content as base


Pair2 = tuple[int, int]


def divide_by_delta(value: Pair2, m: int) -> Pair2:
    """Divide a+b*t by m-t in Z[t], where t^2+t-1=0.

    The norm of m-t is p=m^2+m-1.  Exact division is equivalent to the
    integrality of the two displayed quotients.
    """

    a, b = value
    p = m * m + m - 1
    numerator_0 = a * (m + 1) + b
    numerator_1 = a + m * b
    if numerator_0 % p or numerator_1 % p:
        raise ValueError(f"{value} is not divisible by {m}-t")
    return numerator_0 // p, numerator_1 // p


def delta_valuation(value: Pair2, m: int) -> int:
    answer = 0
    while True:
        try:
            value = divide_by_delta(value, m)
        except ValueError:
            return answer
        answer += 1


def determinantal_divisors(matrix: sp.Matrix) -> list[int]:
    """Return gcds of all k-minors, 1<=k<=number of rows."""

    rows, columns = matrix.shape
    divisors: list[int] = []
    for size in range(1, rows + 1):
        common = 0
        for row_set in itertools.combinations(range(rows), size):
            for column_set in itertools.combinations(range(columns), size):
                minor = int(matrix.extract(row_set, column_set).det())
                common = math.gcd(common, abs(minor))
                if common == 1:
                    break
            if common == 1:
                break
        divisors.append(common)
    return divisors


def sha256_json(value: object) -> str:
    payload = json.dumps(value, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(payload).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    d = 205
    eta: base.Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    data = base.edge_integer_data(d, eta, eta_bar)

    u_coordinates = base.plus_coordinates(data["u_plus"])
    v_coordinates = base.plus_coordinates(data["v_plus"])
    matrix = base.plus_multiplication_matrix(data["u_plus"]).row_join(
        base.plus_multiplication_matrix(data["v_plus"])
    )

    divisors = determinantal_divisors(matrix)
    if divisors != [1, 1, 361, 130321]:
        raise AssertionError(f"unexpected determinantal divisors: {divisors}")
    smith_invariants = [
        divisors[0],
        divisors[1] // divisors[0],
        divisors[2] // divisors[1],
        divisors[3] // divisors[2],
    ]
    if smith_invariants != [1, 1, 361, 361]:
        raise AssertionError(f"unexpected Smith invariants: {smith_invariants}")

    # In O_F=Z[t], delta=4-t has norm 19.  The O_K-basis is
    # (1,t,z,tz), so divisibility by delta^2 can be checked separately on
    # the two F-coordinate pairs of u and v.
    component_pairs = {
        "u_F": u_coordinates[:2],
        "v_F": v_coordinates[:2],
        "v_zF": v_coordinates[2:],
    }
    valuations = {
        name: delta_valuation(value, 4)
        for name, value in component_pairs.items()
    }
    if valuations != {"u_F": 2, "v_F": 12, "v_zF": 3}:
        raise AssertionError(f"unexpected (4-t)-valuations: {valuations}")

    delta: base.Pair = (
        base.kadd(base.kscale(4, base.ONE), base.kneg(base.BPLUS[1][0])),
        base.ZERO,
    )
    delta_squared = base.pmul(delta, delta)
    delta_matrix = base.plus_multiplication_matrix(delta_squared)
    delta_divisors = determinantal_divisors(delta_matrix)
    if base.plus_coordinates(delta_squared) != (17, -9, 0, 0):
        raise AssertionError("(4-t)^2 did not equal 17-9t")
    if delta_divisors != divisors:
        raise AssertionError("the content lattice and (4-t)^2 have different index")

    # Every generator of the content lattice is divisible by delta^2, and
    # both lattices have the same index.  Hence c_205=(delta^2)O_K.
    dependency = Path(base.__file__).resolve()
    script = Path(__file__).resolve()
    result = {
        "description": (
            "Exact d=205 countercertificate to the residue-class ideal-content "
            "formula inferred from d<=200."
        ),
        "degree": d,
        "old_formula_predicted_smith_invariants": [1, 1, 19, 19],
        "old_formula_predicted_norm": "361",
        "determinantal_divisors": divisors,
        "actual_smith_invariants": smith_invariants,
        "actual_content_ideal_norm": str(divisors[-1]),
        "exact_ideal_identity": "c_205=((4-t)^2) O_K, t=zeta_5+zeta_5^-1",
        "delta_squared_coordinates_in_basis_1_t_z_tz": [17, -9, 0, 0],
        "delta_squared_determinantal_divisors": delta_divisors,
        "delta_valuations_of_generators": valuations,
        "coordinate_sha256": sha256_json(
            {"u": u_coordinates, "v": v_coordinates}
        ),
        "q_min_digits": len(str(data["q_min"])),
        "dependency_path": str(dependency),
        "dependency_sha256": file_sha256(dependency),
        "script_sha256": file_sha256(script),
        "scope_warning": (
            "This is an exact counterexample at d=205.  It does not assert "
            "an all-degree replacement formula or exclude later primes."
        ),
    }
    output = Path(
        "results/algebraic_unit_two_log_n5_ideal_content_d205_counterexample.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
