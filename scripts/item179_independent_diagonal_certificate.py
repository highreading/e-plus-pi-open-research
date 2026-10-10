#!/usr/bin/env python3
"""Deterministic certificate for Item 179.

Run with a Python carrying NumPy (used only for exact arithmetic modulo the
fixed prime 65521).  Rational records are generated independently with
fractions by the sibling item179_independent_diagonal_exact.py helper.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

# Make the sibling helper resolution explicit, including after archive staging.
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import item179_independent_diagonal_exact as exact


PRIME = 65521
RESULT_NAME = "item179_independent_diagonal_certificate.json"


def default_output_path() -> Path:
    """Use work/ beside the script, or archive results/ from archive scripts/."""
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def e_interval(last_index: int = 1000) -> tuple[Fraction, Fraction]:
    partial = sum((Fraction(1, math.factorial(k)) for k in range(last_index + 1)), Fraction())
    return partial, partial + Fraction(1, last_index * math.factorial(last_index))


def atan_interval(inv: int, last_index: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        ((-1 if k & 1 else 1) * Fraction(1, (2 * k + 1) * inv ** (2 * k + 1)) for k in range(last_index + 1)),
        Fraction(),
    )
    omitted = Fraction(1, (2 * last_index + 3) * inv ** (2 * last_index + 3))
    return (partial, partial + omitted) if last_index & 1 else (partial - omitted, partial)


def e_plus_pi_interval() -> tuple[Fraction, Fraction]:
    elo, ehi = e_interval()
    alo, ahi = atan_interval(5, 1500)
    blo, bhi = atan_interval(239, 300)
    return elo + 16 * alo - 4 * bhi, ehi + 16 * ahi - 4 * blo


def pow10(k: int) -> Fraction:
    return Fraction(10**k) if k >= 0 else Fraction(1, 10 ** (-k))


def floor_log10_positive(x: Fraction) -> int:
    assert x > 0
    k = len(str(x.numerator)) - len(str(x.denominator))
    while x < pow10(k):
        k -= 1
    while x >= pow10(k + 1):
        k += 1
    return k


def signed_endpoint_interval(a: int, b: int, slo: Fraction, shi: Fraction) -> dict:
    ends = sorted((Fraction(a) + b * slo, Fraction(a) + b * shi))
    lo, hi = ends
    if lo > 0:
        sign, abslo, abshi = 1, lo, hi
    elif hi < 0:
        sign, abslo, abshi = -1, -hi, -lo
    elif lo == hi == 0:
        return {"certified_sign": 0, "interval_contains_zero": True, "identically_zero_pair": True}
    else:
        return {"certified_sign": None, "interval_contains_zero": True, "identically_zero_pair": False}
    dl, dh = floor_log10_positive(abslo), floor_log10_positive(abshi)
    encode = lambda x: f"{x.numerator}/{x.denominator}".encode("ascii")
    return {
        "certified_sign": sign,
        "interval_contains_zero": False,
        "abs_value_strictly_greater_than_one": abslo > 1,
        "floor_log10_abs_lower": dl,
        "floor_log10_abs_upper": dh,
        "single_certified_decade": dl if dl == dh else None,
        "lower_endpoint_sha256": hashlib.sha256(encode(lo)).hexdigest(),
        "upper_endpoint_sha256": hashlib.sha256(encode(hi)).hexdigest(),
    }


def is_prime_trial_division(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    d = 3
    while d * d <= value:
        if value % d == 0:
            return False
        d += 2
    return True


def factorials_and_jets(max_k: int, prime: int) -> tuple[list[int], list[int], list[int]]:
    fact = [1] * (max_k + 1)
    for k in range(1, max_k + 1):
        fact[k] = fact[k - 1] * k % prime
    invfact = [pow(x, prime - 2, prime) for x in fact]
    tau = [0] * (max_k + 1)
    inv4 = pow(4, prime - 2, prime)
    for k in range(1, max_k + 1):
        q, r = divmod(k - 1, 4)
        scale = pow(inv4, q, prime)
        if r == 0:
            v = 2 * fact[4 * q] * scale
        elif r == 1:
            v = 2 * fact[4 * q + 1] * scale
        elif r == 2:
            v = fact[4 * q + 2] * scale
        else:
            v = 0
        tau[k] = ((-v if q & 1 else v) % prime)
    for m in range(1, max_k):
        assert (2 * tau[m + 1] - 2 * m * tau[m] + m * (m - 1) * tau[m - 1]) % prime == 0
    return fact, invfact, tau


def high_matrix(n: int, family: str, prime: int, fact: list[int], invfact: list[int], tau: list[int]) -> np.ndarray:
    if family == "maximal":
        indices = range(n + 1, 3 * n + 2)
    elif family == "endpoint_matched":
        indices = range(n + 1, 3 * n + 1)
    else:
        raise ValueError(family)
    rows: list[list[int]] = []
    for k in indices:
        falling = [fact[k] * invfact[k - j] % prime for j in range(n + 1)]
        rows.append(falling + [falling[j] * tau[k - j] % prime for j in range(n + 1)])
    if family == "endpoint_matched":
        rows.append([prime - 1] * (n + 1) + [1] * (n + 1))
    return np.array(rows, dtype=np.int64)


def solve_square(matrix: np.ndarray, rhs: np.ndarray, prime: int) -> tuple[np.ndarray, int] | None:
    a = matrix.copy()
    b = rhs.copy()
    size = a.shape[0]
    det = 1
    for col in range(size):
        candidates = np.flatnonzero(a[col:, col])
        if len(candidates) == 0:
            return None
        pivot_row = col + int(candidates[0])
        if pivot_row != col:
            a[[col, pivot_row]] = a[[pivot_row, col]]
            b[col], b[pivot_row] = b[pivot_row], b[col]
            det = -det
        pivot = int(a[col, col])
        det = det * pivot % prime
        inv = pow(pivot, prime - 2, prime)
        a[col, col:] = a[col, col:] * inv % prime
        b[col] = b[col] * inv % prime
        if col + 1 < size:
            factors = a[col + 1 :, col].copy()
            a[col + 1 :, col:] = (a[col + 1 :, col:] - factors[:, None] * a[col, col:]) % prime
            b[col + 1 :] = (b[col + 1 :] - factors * b[col]) % prime
    x = np.zeros(size, dtype=np.int64)
    for row in range(size - 1, -1, -1):
        tail = int(np.dot(a[row, row + 1 :], x[row + 1 :]) % prime)
        x[row] = (b[row] - tail) % prime
    return x, det % prime


def jet_of_bc(k: int, n: int, b: np.ndarray, c: np.ndarray, prime: int, fact: list[int], invfact: list[int], tau: list[int]) -> int:
    ans = 0
    for j in range(min(n, k) + 1):
        falling = fact[k] * invfact[k - j] % prime
        ans = (ans + falling * int(b[j]) + falling * tau[k - j] * int(c[j])) % prime
    return ans


def endpoint_a(n: int, b: np.ndarray, c: np.ndarray, prime: int, fact: list[int], invfact: list[int], tau: list[int]) -> int:
    ans = 0
    for k in range(n + 1):
        jet = jet_of_bc(k, n, b, c, prime, fact, invfact, tau)
        ans = (ans - jet * invfact[k]) % prime
    return ans


def modular_record(n: int, family: str, prime: int, fact: list[int], invfact: list[int], tau: list[int]) -> dict:
    matrix = high_matrix(n, family, prime, fact, invfact, tau)
    solved = None
    deleted = None
    for column in range(matrix.shape[1]):
        trial = solve_square(np.delete(matrix, column, axis=1), (-matrix[:, column]) % prime, prime)
        if trial is not None:
            solved = trial
            deleted = column
            break
    if solved is None or deleted is None:
        return {"n": n, "family": family, "deleted_minor_mod_prime": 0, "certified": False}
    tail, det = solved
    kernel = np.insert(tail, deleted, 1)
    assert np.all(matrix.dot(kernel) % prime == 0)
    b, c = kernel[: n + 1], kernel[n + 1 :]
    eb, ec = int(b.sum() % prime), int(c.sum() % prime)
    free_index = 3 * n + (2 if family == "maximal" else 1)
    free = jet_of_bc(free_index, n, b, c, prime, fact, invfact, tau)
    ea = endpoint_a(n, b, c, prime, fact, invfact, tau)
    vector_hash = hashlib.sha256(json.dumps([int(x) for x in kernel], separators=(",", ":")).encode()).hexdigest()
    if family == "maximal":
        special = {
            "endpoint_mismatch_B_minus_C_mod_prime": (eb - ec) % prime,
            "certifies_endpoint_incompatibility": eb != ec,
            "certifies_exact_zero_order_3n_plus_2": free != 0,
        }
    else:
        assert eb == ec
        special = {
            "endpoint_equality_B_equals_C_mod_prime": True,
            "certifies_exact_zero_order_3n_plus_1": free != 0,
        }
    return {
        "n": n,
        "family": family,
        "matrix_shape": list(matrix.shape),
        "deleted_column_index": deleted,
        "deleted_column": ("B_" + str(deleted)) if deleted <= n else ("C_" + str(deleted - n - 1)),
        "normalization_mod_prime": "deleted coordinate = 1",
        "deleted_minor_mod_prime": det,
        "A_at_1_mod_prime": ea,
        "B_at_1_mod_prime": eb,
        "C_at_1_mod_prime": ec,
        "first_free_jet_index": free_index,
        "first_free_jet_mod_prime": free,
        "kernel_sha256": vector_hash,
        "certifies_full_row_rank": det != 0,
        "certified": det != 0 and free != 0 and (eb != ec if family == "maximal" else eb == ec),
        **special,
    }


def rational_records(nmax: int) -> dict:
    slo, shi = e_plus_pi_interval()
    maximal = []
    endpoint = []
    for n in range(1, nmax + 1):
        rm = exact.one(n, True)
        re = exact.one(n, False)
        assert rm["endpoint_mismatch_B_minus_C"] != 0
        assert rm["first_free_derivative"] != 0
        assert re["endpoint_A_B_C"][1] == re["endpoint_A_B_C"][2]
        assert re["first_free_derivative"] != 0
        a, b, _ = re["endpoint_A_B_C"]
        g = math.gcd(abs(a), abs(b))
        re["endpoint_pair_gcd"] = g
        re["primitive_e_plus_pi_pair"] = [a // g, b // g] if g else [0, 0]
        re["primitive_e_plus_pi_pair_denominator"] = 1
        re["primitive_endpoint_height"] = max(abs(a // g), abs(b // g)) if g else 0
        re["endpoint_interval_certificate"] = signed_endpoint_interval(a // g, b // g, slo, shi) if g else signed_endpoint_interval(0, 0, slo, shi)
        maximal.append(rm)
        endpoint.append(re)
    return {
        "e_plus_pi_interval": {
            "lower_sha256": hashlib.sha256(f"{slo.numerator}/{slo.denominator}".encode("ascii")).hexdigest(),
            "upper_sha256": hashlib.sha256(f"{shi.numerator}/{shi.denominator}".encode("ascii")).hexdigest(),
            "width_numerator_bits": (shi - slo).numerator.bit_length(),
            "width_denominator_bits": (shi - slo).denominator.bit_length(),
            "construction": "e Taylor interval plus Machin 16 atan(1/5)-4 atan(1/239) alternating intervals",
        },
        "maximal": maximal,
        "endpoint_matched": endpoint,
        "endpoint_matched_value_summary": {
            "nondegenerate_n": [n for n, r in enumerate(endpoint, 1) if r["endpoint_pair_gcd"]],
            "all_n_2_through_nmax_exclude_zero": all(not r["endpoint_interval_certificate"]["interval_contains_zero"] for r in endpoint[1:]),
            "all_n_2_through_nmax_abs_value_gt_one": all(r["endpoint_interval_certificate"]["abs_value_strictly_greater_than_one"] for r in endpoint[1:]),
            "certified_decades_n_2_through_nmax": [r["endpoint_interval_certificate"]["single_certified_decade"] for r in endpoint[1:]],
        },
    }


def crosscheck_exact_against_modular(exact_records: list[dict], modular_records: list[dict], prime: int) -> dict:
    transcript = []
    for er, mr in zip(exact_records, modular_records):
        n = er["n"]
        assert mr["n"] == n
        triple = er["triple"]
        a = triple[: n + 1]
        bc = triple[n + 1 :]
        deleted = mr["deleted_column_index"]
        pivot = bc[deleted] % prime
        assert pivot != 0
        scale = pow(pivot, prime - 2, prime)
        normalized = [(x % prime) * scale % prime for x in bc]
        kernel_hash = hashlib.sha256(json.dumps(normalized, separators=(",", ":")).encode()).hexdigest()
        assert kernel_hash == mr["kernel_sha256"]
        assert sum(a) % prime * scale % prime == mr["A_at_1_mod_prime"]
        assert er["first_free_derivative"] % prime * scale % prime == mr["first_free_jet_mod_prime"]
        transcript.append([n, deleted, pivot, scale, kernel_hash])
    return {
        "checked_n": [exact_records[0]["n"], exact_records[-1]["n"]],
        "all_projective_kernels_endpoints_and_first_free_jets_agree": True,
        "transcript_sha256": hashlib.sha256(json.dumps(transcript, separators=(",", ":")).encode()).hexdigest(),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--exact-max-n", type=int, default=30)
    ap.add_argument("--modular-max-n", type=int, default=256)
    ap.add_argument("--output", type=Path, default=default_output_path())
    args = ap.parse_args()
    if 3 * args.modular_max_n + 2 >= PRIME:
        raise SystemExit("fixed prime must exceed every derivative index")
    assert is_prime_trial_division(PRIME)
    fact, invfact, tau = factorials_and_jets(3 * args.modular_max_n + 2, PRIME)
    mod_max = [modular_record(n, "maximal", PRIME, fact, invfact, tau) for n in range(1, args.modular_max_n + 1)]
    mod_end = [modular_record(n, "endpoint_matched", PRIME, fact, invfact, tau) for n in range(1, args.modular_max_n + 1)]
    rational = rational_records(args.exact_max_n)
    crosschecks = {
        "maximal": crosscheck_exact_against_modular(rational["maximal"], mod_max, PRIME),
        "endpoint_matched": crosscheck_exact_against_modular(rational["endpoint_matched"], mod_end, PRIME),
    }
    obj = {
        "item": 179,
        "status": "PROVED finite rank/order/endpoint obstruction; exact rational families; no all-degree conclusion",
        "prime": PRIME,
        "prime_is_proved_prime": True,
        "ranges": {"exact_rational": [1, args.exact_max_n], "modular": [1, args.modular_max_n]},
        "definitions": {
            "maximal": "jets 0..3n+1 vanish; order at least 3n+2; no endpoint equation",
            "endpoint_matched": "jets 0..3n vanish and B(1)=C(1); order at least 3n+1",
        },
        "all_modular_maximal_records_certified": all(r["certified"] for r in mod_max),
        "all_modular_endpoint_records_certified": all(r["certified"] for r in mod_end),
        "modular_maximal": mod_max,
        "modular_endpoint_matched": mod_end,
        "exact_rational": rational,
        "exact_modular_crosschecks": crosschecks,
        "logical_bridge": {
            "statement": "For every n, maximal endpoint compatibility is equivalent to an extra zero of the endpoint-matched family at jet 3n+1, equivalently singularity of the square matrix formed by maximal high rows plus the endpoint row.",
            "scope": "all-degree linear-algebra identity; nonvanishing is certified here only in the stated finite ranges",
        },
        "open": [
            "No all-degree nonvanishing theorem for the compatibility determinant is proved.",
            "The one-order-lower endpoint-matched family remains a valid source of integer forms, but no shrinking primitive sequence is proved.",
            "Nothing here decides the arithmetic nature of e+pi.",
        ],
        "runtime": {
            "python": sys.version,
            "numpy": np.__version__,
            "modular_backend": "NumPy int64 arrays with deterministic modular Gaussian elimination",
            "integer_safety": "Every reduction operand is below int64 range: p^2*(2n+2) < 2^63 in the certified range",
            "rational_backend": "Python fractions.Fraction",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
