#!/usr/bin/env python3
"""Exact Hasse-band certificate for the mixed-cubic lifted digit.

This standard-library script evaluates q*R_s modulo p^(2+delta) directly
from the Laurent coefficients at -1, i, -i.  It compares the resulting
eta=q*A_m/p^(1+delta) mod p with the frozen exact U_m coordinates.

Finite agreement is a normalization audit, not the proof of the formula.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n, flag in enumerate(sieve) if flag]


def lcm_upto(limit: int) -> int:
    value = 1
    for n in range(2, limit + 1):
        value = math.lcm(value, n)
    return value


def lcm_exponent(limit: int, p: int) -> int:
    e, power = 0, p
    while power <= limit:
        e += 1
        power *= p
    return e


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("vp(0) is not used")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def d_value(n: int, k: int, q: int) -> int:
    r, t = n % q, k % q
    return 2 * r if t == 0 else 2 * r + 3 * (q - t)


def rank_one_rows(m: int) -> list[dict[str, int]]:
    n, k0 = 6 * m, 4 * m + 1
    rows = []
    for p in primes_upto(2 * m - 1):
        if p == 2:
            continue
        e = lcm_exponent(k0, p)
        q = p**e
        if d_value(n, k0, q) <= 2 * q - 2 and d_value(n, k0 + 1, q) <= 2 * q - 2:
            delta = int(
                d_value(n, k0, p) <= p - 2
                and d_value(n, k0 + 1, p) <= p - 2
            )
            rows.append({"p": p, "e": e, "q": q, "delta": delta})
    return rows


# Gaussian arithmetic in (Z/mod Z)[i].  Every inverse used below has norm
# a power of 2 times a p-unit, so it exists for odd p even when i splits.
G = tuple[int, int]


def ga(a: int, b: int, mod: int) -> G:
    return a % mod, b % mod


def gadd(x: G, y: G, mod: int) -> G:
    return (x[0] + y[0]) % mod, (x[1] + y[1]) % mod


def gneg(x: G, mod: int) -> G:
    return (-x[0]) % mod, (-x[1]) % mod


def gmul(x: G, y: G, mod: int) -> G:
    return (x[0] * y[0] - x[1] * y[1]) % mod, (
        x[0] * y[1] + x[1] * y[0]
    ) % mod


def gscale(x: G, a: int, mod: int) -> G:
    return x[0] * a % mod, x[1] * a % mod


def ginv(x: G, mod: int) -> G:
    inv_norm = pow((x[0] * x[0] + x[1] * x[1]) % mod, -1, mod)
    return x[0] * inv_norm % mod, -x[1] * inv_norm % mod


def gpow(x: G, exponent: int, mod: int) -> G:
    if exponent < 0:
        return gpow(ginv(x, mod), -exponent, mod)
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = gmul(out, x, mod)
        x = gmul(x, x, mod)
        exponent >>= 1
    return out


def series_mul(left: list[G], right: list[G], degree: int, mod: int) -> list[G]:
    out = [(0, 0)] * (degree + 1)
    for i, a in enumerate(left):
        if i > degree:
            break
        for j, b in enumerate(right[: degree - i + 1]):
            out[i + j] = gadd(out[i + j], gmul(a, b, mod), mod)
    return out


def series_pow(base: list[G], exponent: int, degree: int, mod: int) -> list[G]:
    out = [(1, 0)] + [(0, 0)] * degree
    cur = base[: degree + 1] + [(0, 0)] * max(0, degree + 1 - len(base))
    while exponent:
        if exponent & 1:
            out = series_mul(out, cur, degree, mod)
        exponent >>= 1
        if exponent:
            cur = series_mul(cur, cur, degree, mod)
    return out


def series_inverse(base: list[G], degree: int, mod: int) -> list[G]:
    inv0 = ginv(base[0], mod)
    out = [inv0] + [(0, 0)] * degree
    for n in range(1, degree + 1):
        total = (0, 0)
        for j in range(1, min(n, len(base) - 1) + 1):
            total = gadd(total, gmul(base[j], out[n - j], mod), mod)
        out[n] = gneg(gmul(inv0, total, mod), mod)
    return out


def local_coefficients(m: int, k: int, root: str, mod: int) -> list[G]:
    """C_{alpha,r}=[t^r]u(alpha+t)^(6m)/Q_alpha(alpha+t)^k."""
    degree = k - 1
    if root == "minus_one":
        numerator = [ga(-2, 0, mod), ga(3, 0, mod), ga(-1, 0, mod)]
        denominator = [ga(2, 0, mod), ga(-2, 0, mod), ga(1, 0, mod)]
    elif root == "i":
        numerator = [ga(1, 1, mod), ga(1, -2, mod), ga(-1, 0, mod)]
        denominator = [ga(-2, 2, mod), ga(1, 3, mod), ga(1, 0, mod)]
    else:
        raise ValueError(root)
    num_power = series_pow(numerator, 6 * m, degree, mod)
    den_inverse = series_inverse(denominator, degree, mod)
    den_power = series_pow(den_inverse, k, degree, mod)
    return series_mul(num_power, den_power, degree, mod)


def endpoint_factor(root: G, n: int, mod: int) -> G:
    # Integral of a/(x-alpha)^(n+1): a*h_alpha(n)/n.
    minus_alpha = gneg(root, mod)
    one_minus_alpha = gadd((1, 0), gneg(root, mod), mod)
    return gadd(gpow(minus_alpha, -n, mod), gneg(gpow(one_minus_alpha, -n, mod), mod), mod)


def lifted_coordinates(
    m: int, k: int, p: int, e: int, delta: int, *, top_only: bool = False
) -> tuple[int, int, dict[int, int]]:
    """Return L_s and q R_s modulo p^(2+delta), plus band contributions."""
    precision = 2 + delta
    mod = p**precision
    q = p**e
    cm = local_coefficients(m, k, "minus_one", mod)
    ci = local_coefficients(m, k, "i", mod)
    # C_{-i,r} is the Gaussian conjugate of C_{i,r}.
    residue_minus = cm[k - 1][0]
    residue_i = ci[k - 1]
    l_value = (4 * residue_minus + 4 * residue_i[0]) % mod

    roots_and_coefficients = [
        (ga(-1, 0, mod), cm),
        (ga(0, 1, mod), ci),
        (ga(0, -1, mod), [(a, -b % mod) for a, b in ci]),
    ]
    total = (0, 0)
    bands: dict[int, G] = {}
    for n in range(1, k):
        v = vp(n, p)
        if v > e:
            raise AssertionError((m, k, p, e, n, v))
        h = e - v
        if h >= precision or (top_only and h != 0):
            continue
        unit = n // (p**v)
        scalar = p**h * pow(unit, -1, mod) % mod
        contribution = (0, 0)
        index = k - 1 - n
        for root, coefficients in roots_and_coefficients:
            term = gmul(coefficients[index], endpoint_factor(root, n, mod), mod)
            contribution = gadd(contribution, term, mod)
        contribution = gscale(contribution, scalar, mod)
        total = gadd(total, contribution, mod)
        bands[h] = gadd(bands.get(h, (0, 0)), contribution, mod)
    if total[1] % mod:
        raise AssertionError(("non-rational qR", m, k, p, total))
    if any(value[1] % mod for value in bands.values()):
        raise AssertionError(("non-rational band", m, k, p, bands))
    return l_value, total[0], {h: value[0] for h, value in bands.items()}


def hasse_eta(m: int, p: int, e: int, delta: int, *, top_only: bool = False) -> tuple[int, dict[str, Any]]:
    precision = 2 + delta
    mod = p**precision
    k0 = 4 * m + 1
    l0, x0, bands0 = lifted_coordinates(m, k0, p, e, delta, top_only=top_only)
    l1, x1, bands1 = lifted_coordinates(m, k0 + 1, p, e, delta, top_only=top_only)
    determinant = (l1 * x0 - l0 * x1) % mod
    divisor = p ** (1 + delta)
    if determinant % divisor:
        raise AssertionError(("expected divisibility", m, p, delta, determinant))
    return (determinant // divisor) % p, {
        "L0": l0,
        "L1": l1,
        "qR0": x0,
        "qR1": x1,
        "bands0": bands0,
        "bands1": bands1,
    }


def cartier_product(m: int) -> int:
    n, k0 = 6 * m, 4 * m + 1
    value = 1
    for p in primes_upto(6 * m):
        if p != 2 and d_value(n, k0, p) <= p - 2 and d_value(n, k0 + 1, p) <= p - 2:
            value *= p
    return value


def expected_eta_from_u(m: int, row: dict[str, int], u_value: int) -> int:
    p, q, delta = row["p"], row["q"], row["delta"]
    k0 = 4 * m + 1
    middle = math.prod(r for r in primes_upto(3 * m - 1) if 2 * m < r < 3 * m)
    clearing = 2 ** (9 * m + 5) * lcm_upto(k0) // middle
    g = cartier_product(m)
    if u_value % p:
        raise AssertionError(("forced p missing", m, p))
    clearing_unit = (clearing // q) % p
    g_unit = (g // (p**delta)) % p
    return (u_value // p) * g_unit * pow(clearing_unit, -1, p) % p


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--max-m", type=int, default=30)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    input_path = args.archive / "results" / "mixed_cubic_positive_match_exact_scan_m100_N6m.json"
    rank_two_path = args.archive / "results" / "mixed_cubic_rank_two_cartier_certificate.json"
    frozen = json.loads(input_path.read_text(encoding="utf-8"))
    rank_two_frozen = json.loads(rank_two_path.read_text(encoding="utf-8"))
    u_by_m = {int(row["m"]): int(row["U"]["value"]) for row in frozen["rows"]}
    rows: list[dict[str, Any]] = []
    mismatches = []
    top_only_changes = []
    band_histogram: dict[str, int] = {}
    maximum_m = min(args.max_m, 100)
    seen: set[tuple[int, int]] = set()
    rank_one_count = 0
    rank_two_count = 0
    for m in range(1, maximum_m + 1):
        for row in rank_one_rows(m):
            seen.add((m, row["p"]))
            rank_one_count += 1
            eta, details = hasse_eta(m, row["p"], row["e"], row["delta"])
            expected = expected_eta_from_u(m, row, u_by_m[m])
            top_eta, _ = hasse_eta(m, row["p"], row["e"], row["delta"], top_only=True)
            agrees = eta == expected
            if not agrees:
                mismatches.append({"m": m, **row, "eta": eta, "expected": expected})
            if top_eta != eta:
                top_only_changes.append({"m": m, **row, "eta": eta, "top_only_eta": top_eta})
            for h in sorted(set(details["bands0"]) | set(details["bands1"])):
                band_histogram[str(h)] = band_histogram.get(str(h), 0) + 1
            rows.append({
                "source": "rank_one",
                "m": m,
                **row,
                "eta": eta,
                "expected_eta": expected,
                "top_only_eta": top_eta,
                "agrees": agrees,
                "top_only_changes_eta": top_eta != eta,
                "band_indices": sorted(set(details["bands0"]) | set(details["bands1"])),
            })

    # Independently replay the genuinely new vanishing rank-two rows as well.
    for index_row in rank_two_frozen["index_rows"]:
        m = int(index_row["m"])
        if m > maximum_m:
            continue
        for archived in index_row["vanishing_rank_two_rows"]:
            p = int(archived["p"])
            if (m, p) in seen:
                continue
            e = int(archived["denominator_exponent"])
            q = int(archived["top_prime_power_layer"])
            delta = int(bool(archived["rank_zero_at_first_cartier"]))
            row = {"p": p, "e": e, "q": q, "delta": delta}
            eta, details = hasse_eta(m, p, e, delta)
            expected = expected_eta_from_u(m, row, u_by_m[m])
            top_eta, _ = hasse_eta(m, p, e, delta, top_only=True)
            agrees = eta == expected
            if not agrees:
                mismatches.append({"m": m, **row, "eta": eta, "expected": expected})
            if top_eta != eta:
                top_only_changes.append({"m": m, **row, "eta": eta, "top_only_eta": top_eta})
            for h in sorted(set(details["bands0"]) | set(details["bands1"])):
                band_histogram[str(h)] = band_histogram.get(str(h), 0) + 1
            rows.append({
                "source": "rank_two_zero",
                "m": m,
                **row,
                "eta": eta,
                "expected_eta": expected,
                "top_only_eta": top_eta,
                "agrees": agrees,
                "top_only_changes_eta": top_eta != eta,
                "band_indices": sorted(set(details["bands0"]) | set(details["bands1"])),
            })
            seen.add((m, p))
            rank_two_count += 1

    if mismatches:
        raise AssertionError(mismatches[:3])
    output = {
        "schema": "mixed-cubic-lifted-endpoint-hasse-bands-v1",
        "status": {
            "uniform_hasse_band_identity": "PROVED_IN_COMPANION_NOTE",
            "finite_replay": "EXACT_FINITE_AUDIT_ONLY",
            "positive_mass_of_eta_zeros": "OPEN",
        },
        "inputs": {
            input_path.name: sha256(input_path),
            rank_two_path.name: sha256(rank_two_path),
        },
        "parameters": {"max_m": maximum_m},
        "summary": {
            "rank_one_rows": rank_one_count,
            "new_rank_two_zero_rows": rank_two_count,
            "total_forced_rows": len(rows),
            "mismatches_against_frozen_actual_U": len(mismatches),
            "rows_where_deleting_lower_bands_changes_eta": len(top_only_changes),
            "band_presence_row_counts": band_histogram,
            "eta_zero_rows": sum(row["eta"] == 0 for row in rows),
        },
        "first_top_only_failures": top_only_changes[:20],
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
