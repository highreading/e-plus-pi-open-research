#!/usr/bin/env python3
"""Exact diagnostics for Item 189's moving-root collision route.

The theorem in the companion report is combinatorial.  This certificate
checks the determinant data, the finite Sidon diagnostic, a bounded-window
characteristic-zero recurrence obstruction, and two specialized finite-field
recurrence fits.  The finite observations are not promoted to theorems.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from collections import Counter
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item189_collision_route_certificate.json"
ITEM185_NAME = "item185_moving_root_count_certificate.json"
AUXILIARY_PRIME = 65521


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def item185_path() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / ITEM185_NAME
    return HERE / ITEM185_NAME


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * (
                (limit - q * q) // q + 1
            )
    return [p for p in range(7, limit + 1) if sieve[p]]


def scalar_coefficients(index_parameter: int, s: int, modulus: int) -> list[int]:
    """a_n(s) modulo modulus for 0 <= n < index_parameter.

    When modulus=index_parameter is prime this is the Item180 finite-field
    sequence.  When modulus is larger than index_parameter, it is the exact
    characteristic-zero coefficient sequence reduced modulo modulus.
    """
    p = index_parameter
    a = [0] * p
    a[0] = 1
    for n in range(p - 1):
        rhs = (n - 5 * s - 2) * a[n]
        if n >= 3:
            rhs += (n + 8 * s + 5) * a[n - 3]
        if n >= 4:
            rhs -= (n + 3 * s + 2) * a[n - 4]
        a[n + 1] = (rhs % modulus) * pow(n + 1, -1, modulus) % modulus
    return a


def determinant_from_coefficients(
    index_parameter: int, s: int, a: list[int], modulus: int
) -> int:
    p = index_parameter
    d = p - 3 * s
    low = sum(a[d - r] if d - r >= 0 else 0 for r in (2, 3, 4)) % modulus
    high = sum(a[p - r] for r in (4, 3, 2)) % modulus
    value = low * a[p - 5] - high * a[d - 1]
    return ((-1 if s & 1 else 1) * value) % modulus


def scalar_roots(p: int) -> list[int]:
    return [
        s
        for s in range((p - 1) // 3 + 1)
        if determinant_from_coefficients(p, s, scalar_coefficients(p, s, p), p)
        == 0
    ]


def vector_determinants(p: int) -> np.ndarray:
    """All admissible determinants for one prime, using exact int64 residues."""
    if not is_prime(p):
        raise ValueError(f"not prime: {p}")
    if p > 100_000:
        raise ValueError("the certified int64 implementation is scoped to p<=100000")
    count = (p - 1) // 3 + 1
    s_values = np.arange(count, dtype=np.int64)
    zero = np.zeros(count, dtype=np.int64)
    ring = [zero.copy() for _ in range(5)]
    ring[0][:] = 1
    low = [zero.copy() for _ in range(5)]
    high: list[np.ndarray | None] = [None] * 6

    for n in range(p):
        current = ring[n % 5]
        for r in (1, 2, 3, 4):
            numerator = p - r - n
            if numerator >= 0 and numerator % 3 == 0:
                s = numerator // 3
                if s < count:
                    low[r][s] = current[s]
        for r in (2, 3, 4, 5):
            if n == p - r:
                high[r] = current.copy()
        if n == p - 1:
            break
        rhs = (n - 5 * s_values - 2) * current
        if n >= 3:
            rhs += (n + 8 * s_values + 5) * ring[(n - 3) % 5]
        if n >= 4:
            rhs -= (n + 3 * s_values + 2) * ring[(n - 4) % 5]
        ring[(n + 1) % 5] = (rhs % p) * pow(n + 1, -1, p) % p

    if any(high[r] is None for r in (2, 3, 4, 5)):
        raise AssertionError("missing high coefficient vector")
    h2, h3, h4, h5 = (high[r] for r in (2, 3, 4, 5))
    assert h2 is not None and h3 is not None and h4 is not None and h5 is not None
    # The omitted (-1)^s factor is a unit and does not affect roots.
    return (
        ((low[2] + low[3] + low[4]) % p) * h5
        - ((h4 + h3 + h2) % p) * low[1]
    ) % p


def vector_roots(p: int) -> list[int]:
    return np.flatnonzero(vector_determinants(p) == 0).astype(int).tolist()


def difference_profile(roots: list[int]) -> tuple[int, dict[int, int]]:
    counts = Counter(
        right - left
        for index, left in enumerate(roots)
        for right in roots[index + 1 :]
    )
    return max(counts.values(), default=0), dict(sorted(counts.items()))


def finite_census(limit: int, dependency: dict) -> dict:
    zero_pairs: list[list[int]] = []
    histogram: Counter[int] = Counter()
    repeated_difference_failures = []
    maximum_collision = 0
    scalar_crosschecks = 0
    item185_pairs = dependency["finite_census"]["zero_pairs"]

    for p in primes_upto(limit):
        roots = vector_roots(p)
        if p <= 251:
            if roots != scalar_roots(p):
                raise AssertionError((p, roots, scalar_roots(p)))
            scalar_crosschecks += 1
        zero_pairs.extend([p, s] for s in roots)
        histogram[len(roots)] += 1
        local_maximum, profile = difference_profile(roots)
        maximum_collision = max(maximum_collision, local_maximum)
        repeated = [[h, multiplicity] for h, multiplicity in profile.items() if multiplicity > 1]
        if repeated:
            repeated_difference_failures.append(
                {"p": p, "roots": roots, "repeated_differences": repeated}
            )

    dependency_scope = [pair for pair in zero_pairs if pair[0] <= 2000]
    if dependency_scope != item185_pairs:
        raise AssertionError("vectorized scan disagrees with the frozen Item185 census")
    encoded = json.dumps(zero_pairs, separators=(",", ":")).encode("ascii")
    return {
        "scope": [7, limit],
        "prime_count": sum(histogram.values()),
        "candidate_pair_count": sum(
            (p - 1) // 3 + 1 for p in primes_upto(limit)
        ),
        "zero_pair_count": len(zero_pairs),
        "root_count_histogram": {str(k): histogram[k] for k in sorted(histogram)},
        "maximum_roots_for_one_prime": max(histogram, default=0),
        "maximum_same_difference_multiplicity": maximum_collision,
        "all_root_sets_are_sidon_in_finite_scope": not repeated_difference_failures,
        "repeated_difference_failures": repeated_difference_failures,
        "scalar_vs_vector_prime_crosschecks": scalar_crosschecks,
        "item185_p_le_2000_zero_pairs_match": True,
        "zero_pairs_sha256": hashlib.sha256(encoded).hexdigest(),
        "zero_pairs": zero_pairs,
        "warning": "finite exact computation only; the Sidon property is not proved uniformly",
    }


def large_prime_spot_checks(primes: list[int]) -> dict:
    rows = []
    for p in primes:
        roots = vector_roots(p)
        collision, _ = difference_profile(roots)
        rows.append({"p": p, "roots": roots, "root_count": len(roots), "max_difference_multiplicity": collision})
    encoded = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode("ascii")
    return {
        "primes": primes,
        "rows": rows,
        "maximum_root_count": max((row["root_count"] for row in rows), default=0),
        "all_sidon": all(row["max_difference_multiplicity"] <= 1 for row in rows),
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "warning": "selected-prime exact checks only, not an interval census",
    }


def lifted_determinants(index_parameter: int, modulus: int) -> list[int]:
    if index_parameter >= modulus:
        raise ValueError("auxiliary modulus must exceed every coefficient index")
    return [
        determinant_from_coefficients(
            index_parameter,
            s,
            scalar_coefficients(index_parameter, s, modulus),
            modulus,
        )
        for s in range((index_parameter - 1) // 3 + 1)
    ]


def rank_mod_prime(matrix: np.ndarray, prime: int) -> int:
    a = matrix.copy().astype(np.int64, copy=False) % prime
    rows, columns = a.shape
    rank = 0
    for column in range(columns):
        candidates = np.flatnonzero(a[rank:, column])
        if not candidates.size:
            continue
        pivot = rank + int(candidates[0])
        if pivot != rank:
            a[[rank, pivot]] = a[[pivot, rank]]
        a[rank] = a[rank] * pow(int(a[rank, column]), -1, prime) % prime
        indices = np.flatnonzero(a[:, column])
        indices = indices[indices != rank]
        for start in range(0, len(indices), 256):
            block = indices[start : start + 256]
            factors = a[block, column].copy()
            a[block] = (a[block] - factors[:, None] * a[rank]) % prime
        rank += 1
        if rank == rows or rank == columns:
            break
    return rank


def formal_recurrence_obstruction() -> dict:
    """Exclude one explicit bounded polynomial-recurrence ansatz over Q."""
    if not is_prime(AUXILIARY_PRIME):
        raise AssertionError("auxiliary modulus is not prime")
    order, p_degree, s_degree = 6, 6, 10
    rows = []
    for index_parameter in range(40, 161):
        values = lifted_determinants(index_parameter, AUXILIARY_PRIME)
        p_powers = [pow(index_parameter, degree, AUXILIARY_PRIME) for degree in range(p_degree + 1)]
        for s in range(len(values) - order):
            s_powers = [pow(s, degree, AUXILIARY_PRIME) for degree in range(s_degree + 1)]
            row = []
            for shift in range(order + 1):
                value = values[s + shift]
                for p_power in p_powers:
                    row.extend(value * p_power * s_power % AUXILIARY_PRIME for s_power in s_powers)
            rows.append(row)
    matrix = np.asarray(rows, dtype=np.uint16)
    column_count = (order + 1) * (p_degree + 1) * (s_degree + 1)
    if matrix.shape != (3348, column_count):
        raise AssertionError(matrix.shape)
    digest = hashlib.sha256(matrix.astype("<u2", copy=False).tobytes()).hexdigest()
    rank = rank_mod_prime(matrix.astype(np.int64), AUXILIARY_PRIME)
    if rank != column_count:
        raise AssertionError((rank, column_count))
    return {
        "characteristic_zero_index_grid": [40, 160],
        "auxiliary_prime": AUXILIARY_PRIME,
        "auxiliary_prime_verified_by_trial_division": True,
        "ansatz": "sum_(k=0)^6 P_k(P,s) D(P,s+k)=0 with deg_P P_k<=6 and deg_s P_k<=10",
        "row_count": matrix.shape[0],
        "column_count": column_count,
        "rank_mod_auxiliary_prime": rank,
        "full_column_rank": True,
        "matrix_uint16_little_endian_sha256": digest,
        "proved_scope": "No nonzero characteristic-zero polynomial-coefficient recurrence exists inside this cleared bidegree/order window.",
        "not_excluded": [
            "higher-order or higher-degree recurrences",
            "recurrences existing only after reduction in the defining characteristic p",
            "recurrences with p-specific accessory coefficients not rational in (P,s)",
        ],
    }


def recurrence_matrix(values: np.ndarray, p: int, order: int, degree: int) -> np.ndarray:
    rows = []
    for s in range(len(values) - order):
        row = []
        for shift in range(order + 1):
            power = 1
            value = int(values[s + shift])
            for _ in range(degree + 1):
                row.append(value * power % p)
                power = power * s % p
        rows.append(row)
    return np.asarray(rows, dtype=np.int64)


def unique_nullvector(matrix: np.ndarray, p: int) -> tuple[int, list[int]]:
    a = matrix.copy() % p
    rows, columns = a.shape
    pivots = []
    rank = 0
    for column in range(columns):
        candidates = np.flatnonzero(a[rank:, column])
        if not candidates.size:
            continue
        pivot = rank + int(candidates[0])
        if pivot != rank:
            a[[rank, pivot]] = a[[pivot, rank]]
        a[rank] = a[rank] * pow(int(a[rank, column]), -1, p) % p
        indices = np.flatnonzero(a[:, column])
        indices = indices[indices != rank]
        for start in range(0, len(indices), 256):
            block = indices[start : start + 256]
            factors = a[block, column].copy()
            a[block] = (a[block] - factors[:, None] * a[rank]) % p
        pivots.append(column)
        rank += 1
        if rank == rows:
            break
    free = [column for column in range(columns) if column not in pivots]
    if len(free) != 1:
        raise AssertionError((rank, columns, free))
    vector = [0] * columns
    vector[free[0]] = 1
    for row, pivot in enumerate(pivots):
        vector[pivot] = (-int(a[row, free[0]])) % p
    if np.any(matrix.dot(np.asarray(vector, dtype=np.int64)) % p):
        raise AssertionError("null vector verification failed")
    return rank, vector


def specialized_recurrence_diagnostics() -> dict:
    rows = []
    for p in (1009, 2003):
        values = vector_determinants(p)
        main = recurrence_matrix(values, p, 3, 10)
        rank, vector = unique_nullvector(main, p)
        lower_order_rank = rank_mod_prime(recurrence_matrix(values, p, 2, 10), p)
        lower_degree_rank = rank_mod_prime(recurrence_matrix(values, p, 3, 9), p)
        if lower_order_rank != 33 or lower_degree_rank != 40 or rank != 43:
            raise AssertionError((p, lower_order_rank, lower_degree_rank, rank))
        rows.append(
            {
                "p": p,
                "admissible_node_count": len(values),
                "order_3_degree_10_matrix_shape": list(main.shape),
                "rank": rank,
                "nullity": 1,
                "normalized_recurrence_vector_sha256": hashlib.sha256(
                    json.dumps(vector, separators=(",", ":")).encode("ascii")
                ).hexdigest(),
                "order_2_degree_10_full_rank": lower_order_rank == 33,
                "order_3_degree_9_full_rank": lower_degree_rank == 40,
            }
        )
    return {
        "rows": rows,
        "classification": "finite specialized recurrences only",
        "warning": "A bounded-order recurrence alone cannot bound zeros; e.g. a nonzero period-two sequence can vanish on half of its indices.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-limit", type=int, default=5000)
    parser.add_argument(
        "--large-primes",
        type=int,
        nargs="*",
        default=[10007, 20011, 30011, 50021],
    )
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.scan_limit < 2000:
        raise SystemExit("--scan-limit must be at least 2000 for the Item185 cross-check")

    dependency_path = item185_path()
    dependency_hash = sha256_file(dependency_path)
    expected_dependency_hash = "6fbccedc4e2664cc67d01564cd5ffb1591cb78ade06e7048cb4ac2e732ef7617"
    if dependency_hash != expected_dependency_hash:
        raise AssertionError((dependency_hash, expected_dependency_hash))
    dependency = json.loads(dependency_path.read_text(encoding="utf-8"))

    obj = {
        "item": 189,
        "status": "PROVED collision-to-root-count lemmas and exact shift identities; finite Sidon evidence; uniform moving root bound OPEN",
        "proved_collision_lemmas": {
            "definition": "C_p(h)=#{s: s and s+h are determinant roots}",
            "global_bound": "If C_p(h)<=B for every 1<=h<=N_p, then binom(r_p,2)<=B*N_p and r_p<=(1+sqrt(1+8*B*N_p))/2.",
            "sidon_consequence": "If every positive root difference occurs at most once, then r_p=O(sqrt(p)).",
            "short_shift_bound": "If C_p(h)<=C*h^alpha for 1<=h<H, block energy gives r_p=O(N_p/H+sqrt(N_p*H^alpha)); choosing H about N_p^(1/(alpha+2)) gives exponent (alpha+1)/(alpha+2).",
            "alpha_1_consequence": "A proved C_p(h)=O(h) short-shift bound would give r_p=O(p^(2/3)).",
        },
        "proved_fixed_map_shift_identities": {
            "H": "(1-x)^5/(1-x^4)^2",
            "K": "x^3*H",
            "A_shift": "(1-x^4)^(2h) A_(s+h)=(1-x)^(5h) A_s",
            "K_shift": "(1-x^4)^(2h) (A0*K^(s+h))=x^(3h)(1-x)^(5h)(A0*K^s)",
            "coefficient_width": "The displayed identities use coefficient windows growing linearly in h (up to shifts 8h and 5h); they are not a bounded-state scalar recurrence for Delta_(p,s).",
        },
        "formal_recurrence_test": formal_recurrence_obstruction(),
        "specialized_recurrence_diagnostics": specialized_recurrence_diagnostics(),
        "finite_census": finite_census(args.scan_limit, dependency),
        "large_prime_spot_checks": large_prime_spot_checks(args.large_primes),
        "route_scope": {
            "would_close_if_uniform_sidon_or_collision_bound_is_proved": "the Item174/180 kappa=0 rank-two moving determinant adversary; combined with Item180 it gives the corresponding mean zero-mass statement",
            "does_not_close": [
                "other Route-1 cells or mechanisms",
                "a global pointwise density theorem",
                "Route 2",
                "the arithmetic nature of e+pi",
            ],
        },
        "dependencies": {"item185_json_sha256": dependency_hash},
        "runtime_dependency": {
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "numpy": np.__version__,
        },
        "open": [
            "Prove a uniform Sidon theorem or any sublinear collision estimate for the actual root sets.",
            "Derive a genuine all-p bounded-conductor recurrence or sheaf with a nondegeneracy theorem strong enough to control zeros.",
            "The finite specialized order-three recurrences do not imply a root-count bound.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(obj, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
