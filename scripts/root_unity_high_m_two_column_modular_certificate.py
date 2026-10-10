#!/usr/bin/env python3
"""Good-reduction certificate for the genuine high-m two-column range.

For each tuple in the stated grid, all interpolation and endpoint matrices
are reduced modulo the fixed prime.  A nonzero coefficient of
Gamma=C_0 beta_1-C_1 beta_0 modulo that prime rigorously proves that the
rational Gamma is nonzero: the confluent interpolation matrix is invertible
and the endpoint matrix has full row rank at the same good prime.

This is a finite-grid certificate, not an extrapolated nonvanishing theorem.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import __version__ as flint_version
from flint import nmod_mat


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_high_m_two_column_modular_certificate.json"
PRIME = 1_000_000_007


def convolve_mod(a: list[int], b: list[int]) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] = (c[i + j] + ai * bj) % PRIME
    return c


def moments_mod(max_degree: int) -> list[int]:
    inverse_two = pow(2, PRIME - 2, PRIME)
    moments = [inverse_two]
    for k in range(1, max_degree + 1):
        total = sum(
            (math.comb(k, j) % PRIME) * moments[j] for j in range(k)
        ) % PRIME
        moments.append((-total * inverse_two) % PRIME)
    return moments


def factorial_tables(max_degree: int) -> tuple[list[int], list[int]]:
    factorials = [1] * (max_degree + 1)
    for k in range(1, max_degree + 1):
        factorials[k] = factorials[k - 1] * k % PRIME
    inverse_factorials = [pow(value, PRIME - 2, PRIME) for value in factorials]
    return factorials, inverse_factorials


def interpolation_map_mod(
    m: int,
    n: int,
    D: int,
    moments: list[int],
    factorials: list[int],
    inverse_factorials: list[int],
) -> nmod_mat:
    M = m * (n + 1)
    columns = [(j, a) for j in range(m) for a in range(n + 1)]
    jet_entries = []
    for k in range(M):
        for j, a in columns:
            if a <= k:
                value = (
                    factorials[k]
                    * inverse_factorials[k - a]
                    * pow(j, k - a, PRIME)
                ) % PRIME
            else:
                value = 0
            jet_entries.append(value)
    target_entries = []
    for k in range(M):
        for a in range(D + 1):
            if a <= k:
                value = (
                    -factorials[k]
                    * inverse_factorials[k - a]
                    * moments[k - a]
                ) % PRIME
            else:
                value = 0
            target_entries.append(value)
    jet = nmod_mat(M, M, jet_entries, PRIME)
    target = nmod_mat(M, D + 1, target_entries, PRIME)
    # solve() raises if the prime is bad for the confluent determinant.
    return jet.solve(target)


def endpoint_specialization_map_mod(
    interpolation: nmod_mat, m: int, n: int, D: int
) -> list[list[int]]:
    return [
        [
            sum(
                (-1 if j % 2 else 1)
                * int(interpolation[j * (n + 1) + a, c])
                for j in range(m)
            )
            % PRIME
            for c in range(D + 1)
        ]
        for a in range(n + 1)
    ]


def phi_mod(m: int, n: int) -> list[int]:
    phi = [1]
    for j in range(m):
        for _ in range(n + 1):
            phi = convolve_mod(phi, [(-j) % PRIME, 1])
    return phi


def endpoint_kernel_mod(
    phi: list[int],
    D: int,
    moments: list[int],
    factorials: list[int],
    inverse_factorials: list[int],
) -> nmod_mat:
    entries = []
    for q in range(D - 1):
        for a in range(D + 1):
            total = 0
            for k, coefficient in enumerate(phi):
                degree = k + q
                if degree >= a:
                    total += (
                        coefficient
                        * factorials[degree]
                        * inverse_factorials[degree - a]
                        * moments[degree - a]
                    )
            entries.append(total % PRIME)
    matrix = nmod_mat(D - 1, D + 1, entries, PRIME)
    basis, nullity = matrix.nullspace()
    assert matrix.rank() == D - 1
    assert nullity == 2
    return basis


def gamma_witness(
    basis: nmod_mat,
    beta_map: list[list[int]],
    n: int,
    D: int,
) -> tuple[int, int]:
    endpoints = [
        [int(basis[a, j]) for a in range(D + 1)] for j in range(2)
    ]
    beta = [
        [
            sum(beta_map[a][c] * endpoints[j][c] for c in range(D + 1))
            % PRIME
            for a in range(n + 1)
        ]
        for j in range(2)
    ]
    gamma = [0] * (n + D + 1)
    for a, coefficient_c in enumerate(endpoints[0]):
        for b, coefficient_beta in enumerate(beta[1]):
            gamma[a + b] = (
                gamma[a + b] + coefficient_c * coefficient_beta
            ) % PRIME
    for a, coefficient_d in enumerate(endpoints[1]):
        for b, coefficient_beta in enumerate(beta[0]):
            gamma[a + b] = (
                gamma[a + b] - coefficient_d * coefficient_beta
            ) % PRIME
    for index, coefficient in enumerate(gamma):
        if coefficient:
            return index, coefficient
    return -1, 0


def selected(row: dict) -> bool:
    return (row["m"], row["n"], row["D"]) in {
        (4, 6, 4),
        (4, 12, 8),
        (6, 6, 6),
        (8, 8, 8),
        (10, 10, 10),
        (12, 12, 12),
        (16, 16, 12),
        (20, 16, 12),
    }


def main() -> None:
    rows = []
    digest = hashlib.sha256()
    for m in range(4, 21):
        for n in range(2, 17):
            degrees = [
                D
                for D in range(2, min(12, n) + 1)
                if n < (m - 2) * D
            ]
            if not degrees:
                continue
            D_max = max(degrees)
            M = m * (n + 1)
            moments = moments_mod(M + D_max + 1)
            factorials, inverse_factorials = factorial_tables(M + D_max + 1)
            interpolation = interpolation_map_mod(
                m,
                n,
                D_max,
                moments,
                factorials,
                inverse_factorials,
            )
            beta_max = endpoint_specialization_map_mod(
                interpolation, m, n, D_max
            )
            phi = phi_mod(m, n)
            for D in degrees:
                basis = endpoint_kernel_mod(
                    phi,
                    D,
                    moments,
                    factorials,
                    inverse_factorials,
                )
                beta_map = [row[: D + 1] for row in beta_max]
                index, coefficient = gamma_witness(basis, beta_map, n, D)
                assert index >= 0 and coefficient
                row = {
                    "m": m,
                    "n": n,
                    "D": D,
                    "secondary_origin_order": m * (n + 1) + D - 1,
                    "secondary_ambient_dimension": (m - 1) * (n + D + 1),
                    "secondary_dimension_deficit": (m - 2) * D - n,
                    "gamma_first_nonzero_coefficient_index_mod_prime": index,
                    "gamma_first_nonzero_coefficient_mod_prime": coefficient,
                }
                rows.append(row)
                digest.update(
                    f"{m},{n},{D},{index},{coefficient}\n".encode()
                )

    assert len(rows) == 1762
    assert all(r["secondary_dimension_deficit"] > 0 for r in rows)
    payload = {
        "schema": "root-unity-high-m-two-column-modular-certificate-v1",
        "prime": PRIME,
        "exact_grid": {
            "m_range": [4, 20],
            "n_range": [2, 16],
            "D_rule": "2 <= D <= min(12,n) and n < (m-2)D",
            "row_count": len(rows),
            "all_interpolation_matrices_invertible_mod_prime": True,
            "all_endpoint_matrices_have_nullity_two_mod_prime": True,
            "all_gamma_polynomials_nonzero_mod_prime": True,
            "exact_witness_tuple_sha256": digest.hexdigest(),
        },
        "selected_rows": [row for row in rows if selected(row)],
        "logical_scope": {
            "rigorous_finite_grid": (
                "Good reduction and a nonzero Gamma coefficient modulo the prime "
                "prove Gamma is nonzero over Q for every listed tuple."
            ),
            "not_asymptotic": (
                "The finite modular grid is not extrapolated to an all-parameter "
                "nonvanishing theorem."
            ),
        },
        "versions": {"python_flint": flint_version},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["exact_grid"], indent=2, sort_keys=True))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
