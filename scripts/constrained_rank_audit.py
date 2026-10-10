#!/usr/bin/env python3
"""Exact finite rank audit for the endpoint-constrained arctangent matrix.

Reduction modulo a prime is exact.  If an integer matrix has full row rank
modulo that prime, then it also has full row rank over Q.  This script checks
the bordered matrix D_m described in research_log.md; it does not extrapolate
the finite result to all m.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def falling(k: int, a: int, prime: int) -> int:
    result = 1
    for j in range(a):
        result = result * (k - j) % prime
    return result


def tau(r: int, prime: int) -> int:
    if r % 2 == 0:
        return 0
    result = 1
    for j in range(1, r):
        result = result * j % prime
    if ((r - 1) // 2) % 2:
        result = -result
    return result % prime


def bordered_matrix(n: int, prime: int) -> list[list[int]]:
    m = n + 1
    rows: list[list[int]] = []
    # k=m,...,3m-3 gives 2m-2 jet rows.
    for k in range(m, 3 * m - 2):
        e_row = [falling(k, a, prime) for a in range(m)]
        h_row = [falling(k, a, prime) * tau(k - a, prime) % prime for a in range(m)]
        rows.append(e_row + h_row)
    rows.append([(-4) % prime] * m + [1] * m)
    assert len(rows) == 2 * m - 1
    assert all(len(row) == 2 * m for row in rows)
    return rows


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    a = [row[:] for row in matrix]
    row_count = len(a)
    column_count = len(a[0]) if a else 0
    rank = 0
    for column in range(column_count):
        pivot = next((r for r in range(rank, row_count) if a[r][column] % prime), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][column], prime - 2, prime)
        a[rank] = [value * inverse % prime for value in a[rank]]
        for r in range(rank + 1, row_count):
            if a[r][column]:
                factor = a[r][column]
                a[r] = [(x - factor * y) % prime for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == row_count:
            break
    return rank


def matrix_digest(matrix: list[list[int]]) -> str:
    encoded = json.dumps(matrix, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=60)
    parser.add_argument("--prime", type=int, default=1_000_000_007)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    # The default is prime; for a custom modulus the caller is responsible for
    # supplying a prime, since Fermat inversion is used below.
    records = []
    for n in range(args.max_n + 1):
        matrix = bordered_matrix(n, args.prime)
        rank = rank_mod_prime(matrix, args.prime)
        records.append(
            {
                "n": n,
                "rows": len(matrix),
                "columns": len(matrix[0]),
                "rank_mod_prime": rank,
                "full_row_rank": rank == len(matrix),
                "matrix_sha256": matrix_digest(matrix),
            }
        )
    result = {
        "prime": args.prime,
        "checked_n_inclusive": [0, args.max_n],
        "all_full_row_rank": all(record["full_row_rank"] for record in records),
        "implication": (
            "Full row rank modulo the stated prime certifies full row rank over Q "
            "for each displayed integer matrix."
        ),
        "warning": "This is a finite rank theorem, not an all-degree rank theorem.",
        "records": records,
    }
    encoded = json.dumps(result, indent=2, sort_keys=True).encode()
    rendered = encoded.decode() + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
