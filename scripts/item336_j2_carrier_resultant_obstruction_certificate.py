#!/usr/bin/env python3
"""Deterministic certificate for Item 336.

The checker verifies the affine resultant collapse, the exact fixed-M
prime interval, the low-complexity full-mass comparison carrier, and four
declared primitive-carrier examples.  Finite Chebyshev sums and carrier
examples are diagnostic only; asymptotic and all-row proofs are in the
companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item336_j2_carrier_resultant_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item334_j2_coupled_cartier_carrier_report.md":
        "a9a1b42652e5157b850014758c321ffd8a5734e4f9ea3586510ae0549822357c",
    "scripts/item334_j2_coupled_cartier_carrier_certificate.py":
        "b9cab6a6ddc4a0817bae5852e78473ab3144ed9a3b8985c7eacaf27629c90cce",
    "results/item334_j2_coupled_cartier_carrier_certificate.json":
        "238046186f90bdffb2e9b4c72994bac4f0c2ba7e377b42f04753b5502ea861e2",
    "manifests/item334_j2_coupled_cartier_carrier_manifest.json":
        "518176b7e7cf5908e350bb857063bae47658050ca63c4a0e1976554efac87bc9",
    "scripts/item318_j2_actual_period_plucker_certificate.py":
        "334bade7313a2fb750874dfd53216cd5f1028afbc837473cdd19b365ca820e82",
    "scripts/item331_j2_global_cartier_concentration_certificate.py":
        "726157af0f7250c42c3594bb45f08074375e4eb5d1e9843cad37f3def85e27ba",
}


def default_output() -> Path:
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def det(left: tuple[F, F], right: tuple[F, F]) -> F:
    return left[0] * right[1] - left[1] * right[0]


def primes_up_to(bound: int) -> list[int]:
    if bound < 2:
        return []
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(bound) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start:bound + 1:prime] = b"\x00" * (((bound - start) // prime) + 1)
    return [value for value in range(2, bound + 1) if sieve[value]]


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def resultant_replay() -> dict[str, Any]:
    tests = [
        ((F(1), F(2)), (F(3), F(5)), (F(7), F(11)), F(13), F(17), F(19), 0),
        ((F(2), F(-1)), (F(4), F(3)), (F(-5), F(8)), F(-7), F(9), F(5, 3), 1),
        ((F(0), F(1)), (F(1), F(0)), (F(2), F(0)), F(5), F(-3), F(11, 2), 4),
        ((F(3), F(7)), (F(-2), F(5)), (F(11), F(-13)), F(2, 5), F(23), F(-17, 4), 7),
    ]
    rows = []
    for f, b, v, B, tau, K, m in tests:
        c = F(2 ** (2 * (m + 1)))
        U = (9 * c * b[0] - 11 * v[0], 9 * c * b[1] - 11 * v[1])
        D = det(f, U)
        a = (K * f[0], K * f[1])
        beta = (
            (-1) ** m * (f[0] * B * tau - U[0]),
            (-1) ** m * (f[1] * B * tau - U[1]),
        )
        resultant = a[0] * beta[1] - a[1] * beta[0]
        expected = (-1) ** (m + 1) * K * D
        if resultant != expected:
            raise AssertionError((f, b, v, B, tau, K, m, resultant, expected))
        for X in (F(-2), F(0), F(3, 7)):
            T = (a[0] * X + beta[0], a[1] * X + beta[1])
            if det(a, T) != resultant:
                raise AssertionError((f, b, v, m, X, "linear subresultant"))
        rows.append((m, D, K, resultant, expected))
    return {
        "classification": "SYMBOLIC EXACT RATIONAL IDENTITIES",
        "generic_rows": len(rows),
        "resultant_checks": len(rows),
        "linear_subresultant_checks": 3 * len(rows),
        "row_digest_sha256": digest_rows(rows),
    }


def fixed_M_prime_rows(M: int, primes: list[int]) -> list[tuple[int, int, int, int, int]]:
    rows = []
    for prime in primes:
        if 5 * prime < 4 * M + 3 or 7 * prime > 6 * M - 1:
            continue
        if prime == 2:
            continue
        m_numerator = 5 * prime - 4 * M - 3
        if m_numerator % 2:
            raise AssertionError((M, prime, "m parity"))
        m = m_numerator // 2
        d = 6 * M - 7 * prime + 4
        r = d - 4
        s = m + 1
        if m < 0 or d < 5:
            raise AssertionError((M, prime, m, d, "range"))
        if r < 1 or r % 2 != 1 or r % 3 == 0 or s < 1:
            raise AssertionError((M, prime, r, s, "actual row"))
        if prime != 2 * r + 6 * s + 3 or 2 * M != 5 * r + 14 * s + 7:
            raise AssertionError((M, prime, r, s, "bijection"))
        rows.append((prime, r, s, m, d))
    return rows


def fixed_M_replay(M_min: int, M_max: int) -> dict[str, Any]:
    primes = primes_up_to((6 * M_max) // 7 + 2)
    rows = []
    comparison_recurrence_checks = 0
    pairwise_prime_gcd_checks = 0
    theta_sum = 0.0
    last_summary = None
    for M in range(M_min, M_max + 1):
        actual = fixed_M_prime_rows(M, primes)
        theta = sum(math.log(prime) for prime, *_ in actual)
        theta_sum += theta

        # The comparison carrier is G_tilde=p on the actual tied row.
        for prime, r, s, m, d in actual:
            if math.gcd(prime, prime) != prime:
                raise AssertionError((M, prime, "comparison gcd"))
            rows.append((M, prime, r, s, m, d))
        for i in range(len(actual)):
            for j in range(i + 1, len(actual)):
                if math.gcd(actual[i][0], actual[j][0]) != 1:
                    raise AssertionError((M, actual[i][0], actual[j][0], "prime reuse"))
                pairwise_prime_gcd_checks += 1

        # On the full odd tied grid, p changes by two and has zero second difference.
        lower = (4 * M + 3 + 4) // 5
        upper = (6 * M - 1) // 7
        odd_grid = [value for value in range(lower, upper + 1) if value % 2 == 1]
        for i in range(len(odd_grid) - 2):
            if odd_grid[i + 1] - odd_grid[i] != 2:
                raise AssertionError((M, odd_grid[i:i + 3], "first difference"))
            if odd_grid[i + 2] - 2 * odd_grid[i + 1] + odd_grid[i] != 0:
                raise AssertionError((M, odd_grid[i:i + 3], "second difference"))
            comparison_recurrence_checks += 2
        if M == M_max:
            last_summary = {
                "M": M,
                "prime_rows": len(actual),
                "theta": theta,
                "theta_over_M": theta / M,
                "raw_limit_constant": 2 / 35,
                "normalized_per_6M": theta / (6 * M),
                "raw_ceiling_per_6M": 1 / 105,
                "sample_rows": actual[:8],
            }
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "M_min_inclusive": M_min,
        "M_max_inclusive": M_max,
        "fixed_M_values": M_max - M_min + 1,
        "prime_rows": len(rows),
        "comparison_recurrence_checks": comparison_recurrence_checks,
        "pairwise_distinct_prime_gcd_checks": pairwise_prime_gcd_checks,
        "aggregate_finite_theta": theta_sum,
        "row_digest_sha256": digest_rows(rows),
        "last_slice": last_summary,
    }


def exact_carrier_value(i334: Any, i318: Any, i331: Any, prime: int, r: int, s: int) -> int:
    m = s - 1
    d = r + 4
    n = 3 * m + d
    q = 2 * m + d
    c_p = i331.coefficient(n, q, prime)
    epsilon = i331.legendre_two(prime)
    data = i318.i250.phase_data(r)
    coeff = i318.coefficients(data)
    period = i318.actual_period(r, s, data)
    h_m = i334.h_value(m)
    P = i334.p_correction(r + 2, m)
    base = F(9, 2) * period["kappa"] * (F(c_p) + epsilon * h_m * P)
    c = F(2 ** (2 * s))
    T = tuple(
        coeff["f"][nu] * period["B"] * base
        + (-1) ** m * (
            coeff["f"][nu] * period["B"] * period["tau"]
            - 9 * c * coeff["b"][nu]
            + 11 * coeff["d"][nu]
        )
        for nu in (0, 1)
    )
    D = 9 * c * coeff["ell"] - 11 * coeff["m"]
    carrier = math.gcd(abs(D.numerator), math.gcd(abs(T[0].numerator), abs(T[1].numerator)))
    if carrier == 0:
        raise AssertionError((prime, r, s, "zero carrier"))
    return carrier


def carrier_examples(i334: Any, i318: Any, i331: Any) -> dict[str, Any]:
    declared = [
        (17, 1, 2, 3),
        (29, 1, 4, 7),
        (331, 17, 49, 23),
        (599, 7, 97, 173),
    ]
    rows = []
    for prime, r, s, expected in declared:
        carrier = exact_carrier_value(i334, i318, i331, prime, r, s)
        if carrier != expected:
            raise AssertionError((prime, r, s, carrier, expected))
        if carrier >= prime:
            raise AssertionError((prime, r, s, carrier, "declared example ordering"))
        rows.append((prime, r, s, carrier))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "rows": rows,
        "consequence": "the 334-row bound G<=7 and factor set {3,7} do not extend even to p=599",
        "no_unboundedness_claim": True,
        "row_digest_sha256": digest_rows(rows),
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    i334 = load("item336_i334", "scripts/item334_j2_coupled_cartier_carrier_certificate.py")
    i318 = load("item336_i318", "scripts/item318_j2_actual_period_plucker_certificate.py")
    i331 = load("item336_i331", "scripts/item331_j2_global_cartier_concentration_certificate.py")
    return {
        "schema": "item336-j2-carrier-resultant-obstruction-v1",
        "classification": "PROVED_RESULTANT_COLLAPSE_AND_CARRIER_INFORMATION_CLASS_NO_GO",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "parameters": {
            "M_min_inclusive": args.M_min,
            "M_max_inclusive": args.M_max,
        },
        "proved_formulae": {
            "affine_pair": "T_nu(X)=K*f_nu*X+(-1)^m*(f_nu*B*tau-U_nu)",
            "K": "9*kappa_r*B_s/2, an actual-row p-unit",
            "resultant": "Res_X(T_0,T_1)=(-1)^(m+1)*K*D",
            "fixed_M_prime_interval": "(4M+3)/5 <= p <= (6M-1)/7",
            "raw_chebyshev_mass": "theta((4M/5,6M/7))=(2/35)M+o(M)",
            "raw_ceiling_per_6M": "1/105",
            "comparison_carrier": "G_tilde_(M,p)=p on each actual tied row",
        },
        "resultant_replay": resultant_replay(),
        "fixed_M_replay": fixed_M_replay(args.M_min, args.M_max),
        "carrier_examples": carrier_examples(i334, i318, i331),
        "strict_ledger": {
            "new_booking": 0,
            "new_capacity_reduction": 0,
            "ordinary_j2_ceiling_per_6M": "1/105",
            "target_coupled_average_gcd": "OPEN",
        },
        "scope_warning": (
            "The comparison carrier is an information-class obstruction on the exact tied row grid, "
            "not a claim about the actual primitive carrier.  Finite carrier examples are not density evidence."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--M-min", type=int, default=50)
    parser.add_argument("--M-max", type=int, default=500)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.M_min < 13 or args.M_max < args.M_min:
        raise ValueError("require 13<=M_min<=M_max")
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
