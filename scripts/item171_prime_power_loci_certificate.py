#!/usr/bin/env python3
"""Deterministic certificate for item 171: 10m+1=p^a, a>=3.

The symbolic part reconstructs the exact top-Cartier sparse polynomials,
checks their ranks with Lucas' theorem, verifies the floor/normalization
table, and checks the reciprocal cancellation used on the p=1 (mod 20)
rank-two class.  The finite part independently evaluates the actual mixed-
cubic minors modulo p^precision using the archived integral Hasse recurrence.

Finite valuations are diagnostics.  The all-prime conclusions are proved in
the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ARCHIVE = Path(__file__).resolve().parents[1]
EXTENDED_CANDIDATES = [
    HERE / "lifted_endpoint_hasse_extended_certificate.py",
    ARCHIVE / "scripts" / "lifted_endpoint_hasse_extended_certificate.py",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_extended():
    path = next((candidate for candidate in EXTENDED_CANDIDATES if candidate.exists()), None)
    if path is None:
        raise FileNotFoundError(EXTENDED_CANDIDATES)
    spec = importlib.util.spec_from_file_location("item171_extended", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, path


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n, flag in enumerate(sieve) if flag]


def lucas_binomial(n: int, k: int, p: int) -> int:
    if k < 0 or k > n:
        return 0
    out = 1
    while n or k:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        out = out * math.comb(ni, ki) % p
        n //= p
        k //= p
    return out


def p0_coefficient(rho: int, exponent: int, p: int) -> int:
    offset = exponent - rho
    if offset < 0 or offset % 4:
        return 0
    j = offset // 4
    return (-1 if j & 1 else 1) * lucas_binomial(rho, j, p) % p


def p1_coefficient(rho: int, exponent: int, p: int) -> int:
    for shift, sign in ((0, 1), (1, -1)):
        offset = exponent - rho - shift
        if offset >= 0 and offset % 4 == 0:
            j = offset // 4
            value = lucas_binomial(rho - 1, j, p)
            if j & 1:
                value = -value
            return sign * value % p
    return 0


def matrix_rank_two_rows(left: list[int], right: list[int], p: int) -> int:
    if not any(left) and not any(right):
        return 0
    for i in range(len(left)):
        for j in range(i):
            if (left[i] * right[j] - left[j] * right[i]) % p:
                return 2
    return 1


def predicted_rank(p: int, exponent: int) -> int:
    residue = p % 20
    if residue == 1:
        return 2
    if residue in (11, 9):
        return 1
    if residue == 3 and p == 3 and exponent == 4:
        return 1
    return 0


def predicted_first_cartier_delta(p: int) -> int:
    return int(p % 5 == 3 and p != 3)


def top_row(p: int, exponent: int) -> dict[str, Any]:
    power = p**exponent
    if exponent < 3 or power % 10 != 1:
        raise ValueError((p, exponent))
    m = (power - 1) // 10
    q = p ** (exponent - 1)
    n = 6 * m
    k0 = 4 * m + 1
    floor_a, rho = divmod(n, q)
    floor_b, tau = divmod(k0, q)
    kappa = 2 * floor_a - 3 * floor_b
    expected_kappa = {1: 0, 2: 2, 3: -1, 4: 1}[p % 5]
    expected_rho = {
        1: 3 * (q - 1) // 5,
        2: (q - 3) // 5,
        3: (4 * q - 3) // 5,
        4: (2 * q - 3) // 5,
    }[p % 5]
    if not (
        kappa == expected_kappa
        and rho == expected_rho
        and q - tau == rho
        and floor_a == (3 * p) // 5
        and floor_b == (2 * p) // 5
    ):
        raise AssertionError((p, exponent, floor_a, floor_b, rho, tau, kappa))

    maximum_selected = (5 * rho + 1) // q
    vector0 = [p0_coefficient(rho, j * q - 1, p) for j in range(1, maximum_selected + 1)]
    vector1 = [p1_coefficient(rho, j * q - 1, p) for j in range(1, maximum_selected + 1)]
    rank = matrix_rank_two_rows(vector0, vector1, p)
    if rank != predicted_rank(p, exponent):
        raise AssertionError(("rank", p, exponent, vector0, vector1, rank))

    base = _EXTENDED.base
    d0 = base.d_value(n, k0, p)
    d1 = base.d_value(n, k0 + 1, p)
    first_delta = int(d0 <= p - 2 and d1 <= p - 2)
    if first_delta != predicted_first_cartier_delta(p):
        raise AssertionError(("first delta", p, exponent, d0, d1, first_delta))

    relative_endpoint = None
    if p % 20 == 1:
        h = (p - 1) // 20
        small_n = 12 * h
        small_k = 8 * h + 1
        gamma = lucas_binomial(small_n, 2 * h, p)
        delta = (-1 if (7 * h) & 1 else 1) * lucas_binomial(small_n, 7 * h, p) % p
        reciprocal_sum = sum(
            pow((4 * r + 3) % p, -1, p) for r in range((p - 1) // 2)
        ) % p
        if not (
            small_n + small_k == p
            and gamma != 0
            and delta != 0
            and reciprocal_sum == 0
        ):
            raise AssertionError(("relative endpoint", p, gamma, delta, reciprocal_sum))
        relative_endpoint = {
            "n": small_n,
            "K": small_k,
            "gamma": gamma,
            "delta": delta,
            "odd_section_reciprocal_sum": reciprocal_sum,
        }

    # Rank zero makes both top endpoint vectors zero, giving two minor
    # copies before the squarefree first-Cartier normalization.  Rank one,
    # and the special rank-two relative-endpoint lemma, give one A-minor copy.
    content_lower_bound = (2 - first_delta) if rank == 0 else 1
    return {
        "p": p,
        "p_mod_20": p % 20,
        "a": exponent,
        "m": m,
        "q": q,
        "q_mod_20": q % 20,
        "floor_A": floor_a,
        "floor_B": floor_b,
        "rho": rho,
        "tau": tau,
        "kappa": kappa,
        "P0_selected": vector0,
        "P1_selected": vector1,
        "top_cartier_rank": rank,
        "first_cartier_delta": first_delta,
        "proved_content_valuation_lower_bound": content_lower_bound,
        "rank_two_relative_endpoint": relative_endpoint,
    }


def valuation_mod(value: int, p: int, precision: int) -> int:
    value %= p**precision
    if value == 0:
        return precision
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def coordinates(m: int, k: int, p: int, e: int, precision: int) -> tuple[int, int, int]:
    modulus = p**precision
    base = _EXTENDED.base
    cm = _EXTENDED.local_coefficients_fast(m, k, "minus_one", modulus)
    ci = _EXTENDED.local_coefficients_fast(m, k, "i", modulus)
    l_value = (4 * cm[k - 1][0] + 4 * ci[k - 1][0]) % modulus
    e_value = (-4 * ci[k - 1][1]) % modulus
    roots_and_coefficients = [
        (base.ga(-1, 0, modulus), cm),
        (base.ga(0, 1, modulus), ci),
        (base.ga(0, -1, modulus), [(x, -y % modulus) for x, y in ci]),
    ]
    total = (0, 0)
    for index_n in range(1, k):
        valuation = base.vp(index_n, p)
        if valuation > e:
            raise AssertionError((m, k, p, e, index_n, valuation))
        h = e - valuation
        if h >= precision:
            continue
        unit = index_n // (p**valuation)
        scalar = p**h * pow(unit, -1, modulus) % modulus
        contribution = (0, 0)
        coefficient_index = k - 1 - index_n
        for root, coefficients in roots_and_coefficients:
            term = base.gmul(
                coefficients[coefficient_index],
                base.endpoint_factor(root, index_n, modulus),
                modulus,
            )
            contribution = base.gadd(contribution, term, modulus)
        total = base.gadd(total, base.gscale(contribution, scalar, modulus), modulus)
    if total[1] % modulus:
        raise AssertionError((m, k, p, "nonrational", total))
    return l_value, total[0], e_value


def actual_row(p: int, exponent: int, precision: int) -> dict[str, Any]:
    theorem = top_row(p, exponent)
    m = int(theorem["m"])
    k0 = 4 * m + 1
    e = exponent - 1
    l0, x0, e0 = coordinates(m, k0, p, e, precision)
    l1, x1, e1 = coordinates(m, k0 + 1, p, e, precision)
    modulus = p**precision
    determinant_a = (l1 * x0 - l0 * x1) % modulus
    determinant_b = (l1 * e0 - l0 * e1) % modulus
    delta = int(theorem["first_cartier_delta"])
    va = valuation_mod(determinant_a, p, precision)
    vb = valuation_mod(determinant_b, p, precision)
    vu = va - delta
    vv = e + vb - delta
    vc = min(vu, vv)
    if vc < int(theorem["proved_content_valuation_lower_bound"]):
        raise AssertionError(("content theorem", p, exponent, vc, theorem))
    return {
        "p": p,
        "p_mod_20": p % 20,
        "a": exponent,
        "m": m,
        "top_exponent_e": e,
        "first_cartier_delta": delta,
        "vp_qA": va,
        "vp_B8": vb,
        "vp_U": vu,
        "vp_V": vv,
        "vp_content": vc,
        "precision": precision,
    }


_EXTENDED, _EXTENDED_PATH = load_extended()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-bound", type=int, default=500)
    parser.add_argument("--max-exponent", type=int, default=12)
    parser.add_argument("--precision", type=int, default=9)
    parser.add_argument(
        "--actual-mode", choices=("none", "quick", "full"), default="full"
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.max_exponent < 3 or args.precision < 7:
        raise ValueError(args)

    symbolic_rows: list[dict[str, Any]] = []
    rank_counts: dict[str, int] = {"0": 0, "1": 0, "2": 0}
    for p in primes_upto(args.prime_bound):
        if p in (2, 5):
            continue
        for exponent in range(3, args.max_exponent + 1):
            if pow(p, exponent, 10) != 1:
                continue
            row = top_row(p, exponent)
            symbolic_rows.append(row)
            rank_counts[str(row["top_cartier_rank"])] += 1

    quick_tasks = [(3, 4), (7, 4), (11, 3), (13, 4)]
    full_tasks = quick_tasks + [(11, 4), (17, 4), (31, 3), (41, 3)]
    tasks = [] if args.actual_mode == "none" else (
        quick_tasks if args.actual_mode == "quick" else full_tasks
    )
    actual_rows = [actual_row(p, exponent, args.precision) for p, exponent in tasks]

    payload = {
        "schema": "item171-prime-power-loci-v1",
        "parameters": {
            "prime_bound": args.prime_bound,
            "max_exponent": args.max_exponent,
            "precision": args.precision,
            "actual_mode": args.actual_mode,
        },
        "proved_symbolic_checks": {
            "admissible_rows": len(symbolic_rows),
            "rank_counts": rank_counts,
            "all_floor_rows_agree": True,
            "all_rank_rows_agree": True,
            "all_first_cartier_delta_rows_agree": True,
            "all_p_1_mod_20_reciprocal_sums_zero": True,
            "top_polynomials": [
                "P0=x^rho(1-x^4)^rho",
                "P1=x^rho(1-x)(1-x^4)^(rho-1)",
            ],
        },
        "symbolic_rows": symbolic_rows,
        "actual_finite_rows": actual_rows,
        "scope": {
            "actual_rows_are_finite_diagnostics": True,
            "naive_v_equals_a_plus_one_is_false": True,
            "proved_locus_radical_mass": "log p <= log(10m+1)/3 = O(log m) = o(m)",
            "proved_top_exponent_mass": "(a-1) log p <= log(10m+1) = O(log m) = o(m)",
            "no_result_about_e_plus_pi": True,
        },
        "dependencies": {
            "extended_hasse_path": str(_EXTENDED_PATH),
            "extended_hasse_sha256": sha256(_EXTENDED_PATH),
            "base_hasse_path": str(_EXTENDED.BASE_PATH),
            "base_hasse_sha256": sha256(_EXTENDED.BASE_PATH),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "output": str(args.output),
        "symbolic_rows": len(symbolic_rows),
        "rank_counts": rank_counts,
        "actual_rows": len(actual_rows),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
