#!/usr/bin/env python3
"""Finite exact modular certificates for the Mobius-arctangent HP family.

Let

    F(z) = 4*atan(z/(2-z))

and, for n >= 1, let M_n be the (2n+1) by (2n+2) integer matrix whose
unknowns are the monomial coefficients of B and C.  Its first 2n rows are
the jets n+1,...,3n of B*exp(z)+C*F(z), and its last row is C(1)-B(1).

For each requested n this script deletes the B_0 column and performs exact
Gaussian elimination over GF(PRIME).  When that square minor and three
reported residues are nonzero, the calculation proves over Q that

* M_n has full row rank and its kernel is projectively unique;
* the normalized kernel has B(1)=C(1) != 0;
* the reconstructed A has A(1) != 0; and
* the first unconstrained jet, at index 3n+1, is nonzero.

The endpoint claims are exceptional at n=1: both endpoint coordinates are
zero there, although the rank and first-free-jet certificates remain valid.

This is a finite certificate, not an all-degree theorem.  All arithmetic is
integer arithmetic modulo a proved prime.  NumPy is used only to vectorize
those exact operations; the chosen prime and max_n keep every intermediate
dot product safely below the signed-int64 limit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


PRIME = 65521


def is_prime_trial_division(value: int) -> bool:
    """Deterministic primality test, sufficient for the fixed small modulus."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def factorials_and_jets(max_k: int, prime: int) -> tuple[list[int], list[int], list[int]]:
    """Return k!, (k!)^{-1}, and tau_k=F^(k)(0), all modulo prime."""
    factorial = [1] * (max_k + 1)
    for k in range(1, max_k + 1):
        factorial[k] = factorial[k - 1] * k % prime
    inverse_factorial = [pow(value, prime - 2, prime) for value in factorial]

    tau = [0] * (max_k + 1)
    inverse_four = pow(4, prime - 2, prime)
    for k in range(1, max_k + 1):
        q, residue = divmod(k - 1, 4)
        denominator_inverse = pow(inverse_four, q, prime)
        if residue == 0:
            value = 2 * factorial[4 * q] * denominator_inverse
        elif residue == 1:
            value = 2 * factorial[4 * q + 1] * denominator_inverse
        elif residue == 2:
            value = factorial[4 * q + 2] * denominator_inverse
        else:
            value = 0
        if q & 1:
            value = -value
        tau[k] = value % prime

    # Independent differential-equation check: (z^2-2z+2)F'(z)=4.
    for m in range(1, max_k):
        recurrence = (
            2 * tau[m + 1]
            - 2 * m * tau[m]
            + m * (m - 1) * tau[m - 1]
        ) % prime
        assert recurrence == 0
    return factorial, inverse_factorial, tau


def high_endpoint_matrix(
    n: int, prime: int
) -> tuple[np.ndarray, list[int], list[int], list[int]]:
    """Construct M_n over GF(prime), together with factorial and jet tables."""
    factorial, inverse_factorial, tau = factorials_and_jets(3 * n + 1, prime)
    rows: list[list[int]] = []
    for k in range(n + 1, 3 * n + 1):
        falling: list[int] = []
        value = 1
        for j in range(n + 1):
            if j:
                value = value * (k - j + 1) % prime
            falling.append(value)
        rows.append(
            falling
            + [falling[j] * tau[k - j] % prime for j in range(n + 1)]
        )
    rows.append([prime - 1] * (n + 1) + [1] * (n + 1))
    return np.array(rows, dtype=np.int64), factorial, inverse_factorial, tau


def solve_square_mod_prime(
    matrix: np.ndarray, rhs: np.ndarray, prime: int
) -> tuple[np.ndarray, int] | None:
    """Solve a square system and return (solution, determinant), or None."""
    matrix = matrix.copy()
    rhs = rhs.copy()
    size = matrix.shape[0]
    determinant = 1
    for column in range(size):
        candidates = np.flatnonzero(matrix[column:, column])
        if len(candidates) == 0:
            return None
        pivot_row = column + int(candidates[0])
        if pivot_row != column:
            matrix[[column, pivot_row]] = matrix[[pivot_row, column]]
            rhs[column], rhs[pivot_row] = rhs[pivot_row], rhs[column]
            determinant = -determinant

        pivot = int(matrix[column, column])
        determinant = determinant * pivot % prime
        inverse = pow(pivot, prime - 2, prime)
        matrix[column, column:] = matrix[column, column:] * inverse % prime
        rhs[column] = rhs[column] * inverse % prime

        if column + 1 < size:
            factors = matrix[column + 1 :, column].copy()
            matrix[column + 1 :, column:] = (
                matrix[column + 1 :, column:]
                - factors[:, None] * matrix[column, column:]
            ) % prime
            rhs[column + 1 :] = (
                rhs[column + 1 :] - factors * rhs[column]
            ) % prime

    solution = np.zeros(size, dtype=np.int64)
    for row in range(size - 1, -1, -1):
        tail = int(np.dot(matrix[row, row + 1 :], solution[row + 1 :]) % prime)
        solution[row] = (rhs[row] - tail) % prime
    return solution, determinant % prime


def certificate(n: int, prime: int) -> dict:
    """Produce one exact modular certificate, normalized by B_0=1."""
    matrix, factorial, inverse_factorial, tau = high_endpoint_matrix(n, prime)
    solved = solve_square_mod_prime(matrix[:, 1:], (-matrix[:, 0]) % prime, prime)
    if solved is None:
        return {
            "n": n,
            "deleted_column": "B_0",
            "deleted_minor_determinant_mod_prime": 0,
            "warning": "This prime does not certify the deleted minor.",
        }
    tail, determinant = solved
    kernel = np.concatenate((np.array([1], dtype=np.int64), tail))
    assert np.all(matrix.dot(kernel) % prime == 0)
    b = kernel[: n + 1]
    c = kernel[n + 1 :]
    endpoint_b = int(b.sum() % prime)
    endpoint_c = int(c.sum() % prime)
    assert endpoint_b == endpoint_c

    # For 0 <= k <= n, A's z^k coefficient is minus the k-th jet of
    # B*exp+C*F divided by k!.  Since prime > 3n+1, all divisions are valid.
    endpoint_a = 0
    for k in range(n + 1):
        jet = 0
        for j in range(k + 1):
            falling = factorial[k] * inverse_factorial[k - j] % prime
            jet = (
                jet
                + falling * int(b[j])
                + falling * tau[k - j] * int(c[j])
            ) % prime
        endpoint_a = (endpoint_a - jet * inverse_factorial[k]) % prime

    first_free_index = 3 * n + 1
    first_free_jet = 0
    for j in range(n + 1):
        falling = (
            factorial[first_free_index]
            * inverse_factorial[first_free_index - j]
            % prime
        )
        first_free_jet = (
            first_free_jet
            + falling * int(b[j])
            + falling * tau[first_free_index - j] * int(c[j])
        ) % prime

    vector_bytes = json.dumps(
        [int(value) for value in kernel], separators=(",", ":")
    ).encode()
    return {
        "n": n,
        "matrix_shape": [2 * n + 1, 2 * n + 2],
        "deleted_column": "B_0",
        "normalization_mod_prime": "B_0=1",
        "deleted_minor_determinant_mod_prime": determinant,
        "B_at_1_mod_prime": endpoint_b,
        "C_at_1_mod_prime": endpoint_c,
        "A_at_1_mod_prime": endpoint_a,
        "first_free_jet_index": first_free_index,
        "first_free_jet_mod_prime": int(first_free_jet),
        "normalized_kernel_mod_prime_sha256": hashlib.sha256(vector_bytes).hexdigest(),
        "certifies_full_row_rank": determinant != 0,
        "certifies_nonzero_endpoint_pair": endpoint_a != 0 and endpoint_b != 0,
        "certifies_exact_zero_order_3n_plus_1": first_free_jet != 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=100)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_n < 1:
        raise ValueError("max_n must be positive")
    assert is_prime_trial_division(PRIME)
    if 3 * args.max_n + 1 >= PRIME:
        raise ValueError("max_n is too large for the fixed-prime factorial check")

    records = [certificate(n, PRIME) for n in range(1, args.max_n + 1)]
    result = {
        "construction": (
            "endpoint-matched type-I Hermite--Pade for 1, exp(z), "
            "and F(z)=4*atan(z/(2-z))"
        ),
        "prime": PRIME,
        "prime_status": "65521 is prime",
        "range": [1, args.max_n],
        "deleted_minor": "M_n with its B_0 column deleted",
        "all_deleted_minor_residues_nonzero": all(
            record["deleted_minor_determinant_mod_prime"] != 0 for record in records
        ),
        "all_first_free_jet_residues_nonzero": all(
            record.get("first_free_jet_mod_prime", 0) != 0 for record in records
        ),
        "endpoint_summary": (
            "A(1)=B(1)=C(1)=0 at n=1; A(1) and B(1)=C(1) are nonzero "
            "modulo the prime, hence over Q, for every 2<=n<=max_n"
        ),
        "records": records,
        "warning": (
            "Finite exact certificates only.  They do not prove all-degree rank, "
            "endpoint smallness, irrationality, or transcendence."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
