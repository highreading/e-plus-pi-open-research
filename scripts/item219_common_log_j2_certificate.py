#!/usr/bin/env python3
"""Deterministic certificate for Item 219's fixed common-log cell j=2.

The proof of the all-prime identities is in the companion report.  This
standard-library program independently reconstructs the fixed incidence
vector, verifies the finite-log / beta-period identities on every scanned
row, cross-checks the Frobenius-defect coordinates on a smaller range, and
emits path-stable JSON.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item219_common_log_j2_certificate.json"
A = [1, -3, 2]
D = [1, -2, 2]
J2 = (-245, 70, 315, -35)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    data = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return sha256_bytes(data)


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for k in range(2, math.isqrt(n) + 1):
        if sieve[k]:
            sieve[k * k : n + 1 : k] = b"\x00" * (((n - k * k) // k) + 1)
    return [k for k in range(2, n + 1) if sieve[k]]


def conv(left: list[int], right: list[int], mod: int | None = None) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] += x * y
    if mod is not None:
        answer = [x % mod for x in answer]
    return answer


def poly_pow(base: list[int], exponent: int, mod: int | None = None) -> list[int]:
    answer = [1]
    power = [x % mod for x in base] if mod is not None else list(base)
    e = exponent
    while e:
        if e & 1:
            answer = conv(answer, power, mod)
        e >>= 1
        if e:
            power = conv(power, power, mod)
    return answer


def coefficient_product(left: list[int], right: list[int], index: int, p: int) -> int:
    lo = max(0, index + 1 - len(right))
    hi = min(len(left), index + 1)
    return sum(left[k] * right[index - k] for k in range(lo, hi)) % p


def series_division(numerator: list[int], denominator: list[int], degree: int) -> list[int]:
    if denominator[0] != 1:
        raise ValueError("unit denominator required")
    answer = [0] * (degree + 1)
    for n in range(degree + 1):
        rhs = numerator[n] if n < len(numerator) else 0
        rhs -= sum(denominator[k] * answer[n - k] for k in range(1, min(n, len(denominator) - 1) + 1))
        answer[n] = rhs
    return answer


def reconstruct_fixed_data() -> dict[str, object]:
    # Item 217 normalization, reconstructed directly from A and D.
    u_series = series_division(poly_pow(A, 6), poly_pow(D, 5), 4)
    v_series = series_division(poly_pow(A, 7), poly_pow(D, 6), 4)
    u0, u1 = u_series[4], u_series[3]
    v0, v1 = v_series[4], v_series[3]
    reconstructed = (7 * u0, 7 * u1, -5 * v0, -5 * v1)
    if reconstructed != J2:
        raise AssertionError((reconstructed, J2))

    # Independent Item 197 three-coordinate normalization.
    def fixed_coefficient(j: int, kind: str) -> int:
        exponent_minus = 3 * j + (0 if kind == "u" else 1)
        exponent_plus = 2 * j + (1 if kind == "u" else 2)
        target = 2 * j if kind != "w" else 2 * j - 1
        total = 0
        for b in range(target // 2 + 1):
            k = target - 2 * b
            total += (
                (-1) ** k
                * math.comb(exponent_minus, k)
                * (-1) ** b
                * math.comb(exponent_plus + b - 1, b)
            )
        return total

    uvw = tuple(fixed_coefficient(2, kind) for kind in ("u", "v", "w"))
    if uvw != (-45, -70, 7):
        raise AssertionError(uvw)
    return {
        "a": 7,
        "c": 5,
        "u0": u0,
        "u1": u1,
        "v0": v0,
        "v1": v1,
        "J2": list(reconstructed),
        "item197_UVW": list(uvw),
        "item197_scalar_formula": "C_nu/p = -35*(9*X_nu - 10*Y_nu + Yprime_nu) mod p",
    }


def pnu_poly(p: int, s: int, nu: int) -> tuple[int, int, int, list[int]]:
    r = (p - 6 * s - 3) // 2
    q = 2 * s - nu
    b = 1 + 3 * nu
    result = conv(poly_pow([1, -1], r, p), poly_pow([1, 1], b, p), p)
    result = conv(result, poly_pow([1, 0, 1], q, p), p)
    return r, q, b, result


def log_moments(p: int, s: int, nu: int) -> tuple[int, int, int]:
    _, q, _, pnu = pnu_poly(p, s, nu)
    minus_log = [0] + [(-pow(k, -1, p)) % p for k in range(1, p)]
    plus_log = [0] * (2 * p - 1)
    for k in range(1, p):
        plus_log[2 * k] = ((-1) ** (k - 1) * pow(k, -1, p)) % p
    target = p - q - 1
    return (
        coefficient_product(minus_log, pnu, target, p),
        coefficient_product(plus_log, pnu, target, p),
        coefficient_product(plus_log, pnu, target + p, p),
    )


def residue_weight(n: int, chi4: int) -> int:
    residue = n % 4
    if residue == 0:
        return -11
    if residue == 1:
        return 9 - 2 * chi4
    if residue == 2:
        return 29
    return 9 + 2 * chi4


def period_sum(p: int, s: int, nu: int) -> int:
    r, q, _, pnu = pnu_poly(p, s, nu)
    target = p - q - 1
    if len(pnu) - 1 + r + 1 != target:
        raise AssertionError((p, s, nu, len(pnu), r, target))
    chi4 = 1 if p % 4 == 1 else -1
    total = 0
    for ell, coefficient in enumerate(pnu):
        n = r + ell + 1
        if not (1 <= n < p):
            raise AssertionError((p, s, nu, ell, n))
        total += coefficient * residue_weight(n, chi4) * pow(n, -1, p)
    return total % p


def quotient_digits(p: int, s: int) -> tuple[int, int, tuple[int, int], tuple[tuple[int, int, int], tuple[int, int, int]]]:
    values: list[int] = []
    periods: list[int] = []
    moments: list[tuple[int, int, int]] = []
    r = (p - 6 * s - 3) // 2
    sign = -1 if (r + 1) % 2 else 1
    for nu in (0, 1):
        x, y, yprime = log_moments(p, s, nu)
        moment_value = (9 * x - 10 * y + yprime) % p
        period = period_sum(p, s, nu)
        if moment_value != sign * period % p:
            raise AssertionError((p, s, nu, moment_value, period, sign))
        values.append((-35 * moment_value) % p)
        periods.append(period)
        moments.append((x, y, yprime))
    return values[0], values[1], (periods[0], periods[1]), (moments[0], moments[1])


def delta_frobenius(base: list[int], p: int) -> list[int]:
    modulus = p * p
    powered = poly_pow(base, p, modulus)
    substituted = [0] * (2 * p + 1)
    for k, coefficient in enumerate(base):
        substituted[k * p] = coefficient % modulus
    return [((powered[k] - substituted[k]) % modulus) // p for k in range(2 * p + 1)]


def incidence_rows(p: int, s: int) -> list[tuple[int, int, int, int]]:
    r = (p - 6 * s - 3) // 2
    q = 2 * s - 1
    moving = conv(poly_pow(A, r, p), poly_pow(D, q, p), p)
    L = p - 2 * s - 5
    if len(moving) - 1 != L:
        raise AssertionError((p, s, len(moving) - 1, L))
    delta_a = delta_frobenius(A, p)
    delta_d = delta_frobenius(D, p)
    rows = []
    for t in range(1, 6):
        rows.append(
            (
                coefficient_product(delta_a, moving, L + t, p),
                coefficient_product(delta_a, moving, p + L + t, p),
                coefficient_product(delta_d, moving, L + t, p),
                coefficient_product(delta_d, moving, p + L + t, p),
            )
        )
    return rows


def dot(row: tuple[int, ...], vector: tuple[int, ...], p: int) -> int:
    return sum(x * y for x, y in zip(row, vector)) % p


def incidence_check(p: int, s: int, q0: int, q1: int) -> tuple[int, int, int]:
    w = incidence_rows(p, s)
    e = [dot(row, J2, p) for row in w]
    q0_incidence = (e[3] - 2 * e[2] + 2 * e[1]) % p
    q1_incidence = e[4]
    if (q0_incidence, q1_incidence) != (q0, q1):
        raise AssertionError((p, s, (q0_incidence, q1_incidence), (q0, q1)))
    gate = (e[3], (e[2] - 2 * e[0]) % p, (e[1] - 2 * e[0]) % p)
    if (q0 == 0 and q1 == 0) != all(x == 0 for x in gate):
        raise AssertionError((p, s, q0, q1, gate))
    return gate


def capacity_data() -> dict[str, str]:
    # Digits are frozen upstream; exact rational cell subtractions are included.
    total_per_m = "0.3370475079987658..."
    j1 = "1/6"
    j2 = "2/35"
    removed = "47/210"
    remaining_per_m = "0.1132379841892420..."
    remaining_per_6m = "0.0188729973648737..."
    gap = "0.019632983669431793880306401240..."
    margin = "0.0007599863045581..."
    return {
        "raw_j_ge_1_ceiling_per_m": total_per_m,
        "j1_cell_per_m": j1,
        "j2_cell_per_m": j2,
        "j1_plus_j2_exact_per_m": removed,
        "conditional_remainder_per_m": remaining_per_m,
        "conditional_remainder_per_6m": remaining_per_6m,
        "required_G_per_6m": gap,
        "conditional_margin_below_G_per_6m": margin,
        "status": "CONDITIONAL on all-prime exclusion of both j=1 and j=2; neither is asserted here",
    }


def poly_s_add(left: list[int], right: list[int]) -> list[int]:
    result = [0] * max(len(left), len(right))
    for k, value in enumerate(left):
        result[k] += value
    for k, value in enumerate(right):
        result[k] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_s_mul(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def hermite_minor() -> list[int]:
    # Each pair is constant + linear*s.  These are rows 0,1,2,3,5,7 of
    # the augmented coefficient matrix for
    # H'+(f0'/f0)H = (1+z)^3/(1+z^2)-R,
    # H=(c0+c1*z+c2*z^2+c3*z^3)/(1+z), after 2 clears r=-3s-3/2.
    zero = (0, 0)
    matrix = [
        [(-3, -6), zero, zero, zero, zero, zero],
        [(3, 6), (-1, -6), zero, zero, (2, 0), (2, 0)],
        [(3, 14), (3, 6), (1, -6), zero, (2, 0), (8, 0)],
        [(3, 6), (3, 14), (3, 6), (3, -6), zero, (10, 0)],
        [zero, (4, 4), (3, 6), (3, 14), (-2, 0), (-10, 0)],
        [zero, zero, zero, (0, 4), zero, (-2, 0)],
    ]
    import itertools

    determinant = [0]
    for permutation in itertools.permutations(range(6)):
        term = [permutation_sign(permutation)]
        for row, column in enumerate(permutation):
            term = poly_s_mul(term, list(matrix[row][column]))
        determinant = poly_s_add(determinant, term)
    expected = [0, 2304, 9216, 9216]
    if determinant != expected:
        raise AssertionError((determinant, expected))
    return determinant


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-max", type=int, default=401)
    ap.add_argument("--incidence-prime-max", type=int, default=101)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if args.prime_max < 11 or not (11 <= args.incidence_prime_max <= args.prime_max):
        raise ValueError("require 11 <= incidence-prime-max <= prime-max")

    fixed = reconstruct_fixed_data()
    hermite_determinant = hermite_minor()
    counts: Counter[str] = Counter()
    rows: list[tuple[int, ...]] = []
    separate: list[dict[str, int | str]] = []
    common: list[dict[str, int]] = []
    incidence_rows_checked = 0

    for p in primes_upto(args.prime_max):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            m = (5 * p - 2 * s - 1) // 4
            r = (p - 6 * s - 3) // 2
            if r < 1:
                raise AssertionError((p, s, r))
            if (s - (p - 1) // 2) % 2:
                raise AssertionError((p, s, "parity"))
            q0, q1, periods, _ = quotient_digits(p, s)
            counts["rows"] += 1
            counts["q0_zero"] += q0 == 0
            counts["q1_zero"] += q1 == 0
            counts["common_zero"] += q0 == q1 == 0
            rows.append((p, s, m, r, q0, q1, periods[0], periods[1]))
            if q0 == 0 or q1 == 0:
                separate.append(
                    {
                        "p": p,
                        "s": s,
                        "m": m,
                        "zero": "both" if q0 == q1 == 0 else ("q0" if q0 == 0 else "q1"),
                        "q0": q0,
                        "q1": q1,
                    }
                )
            if q0 == q1 == 0:
                common.append({"p": p, "s": s, "m": m})
            if p <= args.incidence_prime_max:
                incidence_check(p, s, q0, q1)
                incidence_rows_checked += 1

    result = {
        "schema": "item219-common-log-j2-v1",
        "parameters": {
            "j": 2,
            "prime_max_inclusive": args.prime_max,
            "incidence_prime_max_inclusive": args.incidence_prime_max,
            "cell": "4m+1=5p-2s, 1<=s<=(p-3)/6, p>=11, s=(p-1)/2 mod 2",
        },
        "fixed_reconstruction": fixed,
        "proved_identity": {
            "r": "(p-6s-3)/2",
            "q_nu": "2s-nu",
            "P_nu": "(1-z)^r (1+z)^(1+3nu) (1+z^2)^(2s-nu)",
            "S_nu": "sum_l [z^l]P_nu * W_chi4(r+l+1)/(r+l+1) mod p",
            "weights_mod_4": {
                "0": -11,
                "1": "9-2*chi4(p)",
                "2": 29,
                "3": "9+2*chi4(p)",
            },
            "quotient": "C_nu/p = -35*(-1)^(r+1)*S_nu mod p",
            "common_log": "S_0=S_1=0 mod p",
            "denominators": "all r+l+1 lie in [1,p-1]",
        },
        "scoped_hermite_obstruction": {
            "status": "PROVED SCOPED NO-GO",
            "ansatz": "boundary-free scalar reduction below Frobenius degree with H=N/(1+z), deg N<=3",
            "augmented_minor_coefficients_in_s": hermite_determinant,
            "augmented_minor_factorization": "2304*s*(2*s+1)^2",
            "unit_audit": "p>=11 and 1<=s<=(p-3)/6 make 2304, s, and 2s+1 nonzero mod p",
            "conclusion": "no such scalar reduction exists on any admissible row",
            "not_excluded": "a Frobenius-resonant z^p term or a reduction with a nontrivial cohomology-basis remainder",
        },
        "finite_classification": {
            "status": "EXACT FINITE ONLY",
            "counts": dict(sorted(counts.items())),
            "incidence_rows_checked": incidence_rows_checked,
            "separate_zero_rows": separate,
            "common_zero_rows": common,
            "row_digest_sha256": row_digest(rows),
        },
        "capacity": capacity_data(),
        "status_ledger": {
            "PROVED": [
                "independent reconstruction J2=(-245,70,315,-35)",
                "equivalence to two explicit four-residue beta-period sums for every admissible prime row",
                "failure on every admissible row of the boundary-free scalar Hermite ansatz below Frobenius degree",
                "conditional capacity arithmetic after removal of both j=1 and j=2 cells",
            ],
            "EXACT_FINITE": [
                "all admissible j=2 rows through the recorded prime bound; no common zero in this finite set"
            ],
            "OPEN": [
                "all-prime nonvanishing of the pair (S0,S1)",
                "a finite exceptional-prime classification",
                "the separate all-prime j=1 exclusion needed for the joint capacity consequence",
            ],
        },
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(payload.decode("utf-8"), end="")


if __name__ == "__main__":
    main()
