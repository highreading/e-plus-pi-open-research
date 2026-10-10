#!/usr/bin/env python3
"""Deterministic certificate for Item 347.

The checker verifies the exact complete quadratic-moment formula, its
target-retaining collapse, the chosen-prime Jacobi reduction, full
Fourier support, and minimal Kummer support on declared actual rows.
Finite rows are formula replay only; no zero census is performed.
"""

from __future__ import annotations

import argparse
import hashlib
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
RESULT_NAME = "item347_j2_chosen_prime_kummer_conductor_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item341_j2_diagonal_affine_state_report.md":
        "42f6ccd326e385f8034abe322756517a30a93d7468b3e6f85cbca3dba8080cb4",
    "results/item341_j2_diagonal_affine_state_certificate.json":
        "75c05cb486e5a5a6f9af5dda2e62f2a4b81cb888a15eb19ecabd10a382625cb4",
    "results/item341_j2_diagonal_affine_state_root_audit.json":
        "d5c810346f9181f10d38e9f5ae2e250a8c880e32f97cbc5bef91f6bd37f61a27",
    "manifests/item341_j2_diagonal_affine_state_manifest.json":
        "fc073e4c11a2d9ab519f0b5babae6f9f95e2e8cf9e8cbcf05c4c8ca8ba155000",
    "sources/item344_j2_frobenius_cutoff_obstruction_report.md":
        "1671dec30de80c047c52b6b4bf13157025ea631869f5ccacc73169002ec287a9",
    "results/item344_j2_frobenius_cutoff_obstruction_certificate.json":
        "f390d14d2b14ce965a33da8499e450294be3a038be2269d564d3cc3fda5f1179",
    "results/item344_j2_frobenius_cutoff_obstruction_root_audit.json":
        "1de770fc9f8cf23ec215d936e31b08bb59b5aad2ce8fb3480a0bd835011b5376",
    "manifests/item344_j2_frobenius_cutoff_obstruction_manifest.json":
        "9824b1a18fd645e729e103e32d0911d2392edc7b6c6642e5bea28d97489ef286",
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


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def h_term(index: int) -> F:
    return F(math.comb(2 * index, index), 8 ** index)


def h_prefix(index: int) -> F:
    return sum((h_term(j) for j in range(index + 1)), F(0))


def prime_factors(value: int) -> list[int]:
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(prime: int) -> int:
    order = prime - 1
    factors = prime_factors(order)
    for candidate in range(2, prime):
        if all(pow(candidate, order // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError((prime, "no primitive root"))


def chi(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    residue = pow(value, (prime - 1) // 2, prime)
    if residue == 1:
        return 1
    if residue == prime - 1:
        return -1
    raise AssertionError((prime, value, residue, "Euler criterion"))


def fixed_power(value: int, exponent: int, prime: int) -> int:
    if exponent >= 0:
        return pow(value, exponent, prime)
    return pow(pow(value, -1, prime), -exponent, prime)


def load_item341_targets() -> dict[tuple[int, int, int], tuple[int, int, int, int]]:
    path = ROOT / "results/item341_j2_diagonal_affine_state_certificate.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    targets = {}
    for row in data["actual_affine_replay"]["rows"]:
        prime, r, s, m = map(int, row[:4])
        c_mod, c_star_mod = int(row[6]), int(row[7])
        H_mod, theta_mod = int(row[8]), int(row[9])
        targets[(prime, r, s)] = (c_mod, c_star_mod, H_mod, theta_mod)
    return targets


def actual_row_replay(
    prime: int,
    r: int,
    s: int,
    target_data: tuple[int, int, int, int],
) -> tuple[Any, ...]:
    m = s - 1
    L = m + 1
    N = prime - 1
    n = N // 2
    d = r + 4
    if prime != 2 * r + 6 * s + 3 or n != 3 * m + d:
        raise AssertionError((prime, r, s, "tied phase"))
    if not (0 < 6 * L < N):
        raise AssertionError((prime, r, s, L, N, "actual prefix range"))

    inverse_two = pow(2, -1, prime)
    inverse_eight = pow(8, -1, prime)
    H_mod = sum(
        (math.comb(2 * u, u) % prime) * pow(inverse_eight, u, prime)
        for u in range(L)
    ) % prime
    if H_mod != fmod(h_prefix(m), prime):
        raise AssertionError((prime, m, H_mod, "rational prefix"))

    term_rows = []
    complete_total = 0
    jacobi_rows = []
    for u in range(L):
        moment = 0
        jacobi = 0
        for x in range(1, prime):
            moment += fixed_power(x, -u, prime) * chi(1 - x * inverse_two, prime)
            jacobi += fixed_power(x, -u, prime) * chi(1 - x, prime)
        moment %= prime
        jacobi %= prime
        expected = (math.comb(2 * u, u) % prime) * pow(inverse_eight, u, prime) % prime
        if (-moment) % prime != expected:
            raise AssertionError((prime, u, moment, expected, "complete moment"))
        if (-pow(2, -u, prime) * jacobi) % prime != expected:
            raise AssertionError((prime, u, jacobi, expected, "Jacobi reduction"))
        complete_total = (complete_total + moment) % prime
        term_rows.append((u, moment, expected))
        jacobi_rows.append((u, jacobi, expected))
    if (-complete_total) % prime != H_mod:
        raise AssertionError((prime, m, complete_total, H_mod, "summed moments"))

    collapsed = 0
    weight_rows = []
    for x in range(1, prime):
        weight = sum(fixed_power(x, -u, prime) for u in range(L)) % prime
        value = weight * chi(1 - x * inverse_two, prime) % prime
        collapsed = (collapsed + value) % prime
        weight_rows.append((x, weight, value))
    if (-collapsed) % prime != H_mod:
        raise AssertionError((prime, m, collapsed, H_mod, "collapsed sum"))

    c_mod, c_star_mod, item341_H_mod, theta_mod = target_data
    if item341_H_mod != H_mod or c_mod != pow(4, L, prime):
        raise AssertionError((prime, r, s, target_data, "Item341 target import"))
    target_complete = sum(
        (theta_mod - weight * chi(1 - x * inverse_two, prime)) % prime
        for x, weight, _ in weight_rows
    ) % prime
    if target_complete != (H_mod - theta_mod) % prime:
        raise AssertionError((prime, r, s, target_complete, "target-retaining sum"))

    generator = primitive_root(prime)
    fourier_coefficients = []
    for a in range(N):
        coefficient = sum(
            fixed_power(generator, -a * u, prime) for u in range(L)
        ) % prime
        fourier_coefficients.append(coefficient)
    support = sum(value != 0 for value in fourier_coefficients)
    expected_support = N - math.gcd(N, L) + 1
    if support != expected_support or 6 * support <= 5 * N + 6:
        raise AssertionError((prime, L, support, expected_support, "Fourier support"))

    fourier_collapse = 0
    for a, coefficient in enumerate(fourier_coefficients):
        x = pow(generator, a, prime)
        fourier_collapse += coefficient * chi(1 - x * inverse_two, prime)
    fourier_collapse %= prime
    if (-fourier_collapse) % prime != H_mod:
        raise AssertionError((prime, m, fourier_collapse, H_mod, "Fourier collapse"))

    # Multiplicative Fourier coefficients of W_m have support exactly L.
    # In exponent coordinates x=g^a, the coefficient of g^(-a*u) is one.
    recovered = []
    inverse_N = pow(N, -1, prime)
    for u in range(N):
        coefficient = 0
        for a in range(N):
            x = pow(generator, a, prime)
            weight = weight_rows[x - 1][1]
            coefficient += weight * pow(x, u, prime)
        recovered.append(coefficient * inverse_N % prime)
    recovered_support = [u for u, value in enumerate(recovered) if value]
    if recovered_support != list(range(L)) or any(recovered[u] != 1 for u in range(L)):
        raise AssertionError((prime, L, recovered_support, "minimal Kummer support"))

    M_numerator = 5 * r + 14 * s + 7
    if M_numerator % 2:
        raise AssertionError((prime, r, s, "nonintegral M"))
    M = M_numerator // 2
    if 5 * prime != 4 * M + 2 * m + 3 or r != 6 * M - 7 * prime:
        raise AssertionError((prime, r, s, M, "fixed-M relation"))

    return (
        prime,
        r,
        s,
        m,
        M,
        generator,
        H_mod,
        theta_mod,
        (c_mod - c_star_mod) % prime,
        target_complete,
        support,
        expected_support,
        L,
        digest_rows(term_rows),
        digest_rows(jacobi_rows),
        digest_rows(weight_rows),
        hashlib.sha256(
            (",".join(map(str, fourier_coefficients)) + "\n").encode("ascii")
        ).hexdigest(),
    )


def actual_rows_replay() -> dict[str, Any]:
    targets = load_item341_targets()
    declared = [
        (11, 1, 1),
        (17, 1, 2),
        (29, 1, 4),
        (271, 113, 7),
        (367, 65, 39),
        (383, 109, 27),
        (599, 7, 97),
    ]
    rows = [actual_row_replay(*row, targets[row]) for row in declared]
    return {
        "classification": "EXACT FINITE REPLAY ONLY - NO ZERO CENSUS",
        "declared_rows": len(rows),
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    return {
        "schema": "item347-j2-chosen-prime-kummer-conductor-obstruction-v1",
        "classification": "PROVED_TARGET_FORCED_COMPLETE_SUM_AND_LINEAR_KUMMER_CONDUCTOR_NO_GO",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "termwise_moment": "h_u=-sum_(x!=0) x^(-u)*chi(1-x/2) mod p",
            "collapsed_sum": "H_m=-sum_(x!=0) W_m(x)*chi(1-x/2), W_m=sum_(u=0)^m x^(-u)",
            "target_forced_sum": "H_m-Theta=sum_(x!=0)(Theta-W_m(x)*chi(1-x/2))",
            "Jacobi_lift": "h_u=-B_u(2)*J(B_u,phi) mod chosen P",
            "cutoff_Fourier_support": "N-gcd(N,m+1)+1 > 5N/6",
            "minimal_Kummer_rank": "m+1 distinct character modes",
            "conductor_lower_bound": "cond >= rank >= m+1 in the semisimple Kummer/Greene category",
        },
        "actual_rows_replay": actual_rows_replay(),
        "capacity": {
            "raw_ordinary_j2_chebyshev_mass": "(2/35)M+o(M)",
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "new_capacity_reduction": 0,
            "new_booking": 0,
        },
        "closed_method_class": [
            "bounded-rank or bounded-conductor semisimple Kummer/Greene completion of the diagonal cutoff",
            "Archimedean Jacobi or Weil bounds without chosen-prime divisibility control",
            "sublinear-rank restriction as a positive-rate mechanism",
        ],
        "open": [
            "nonlinear or nonsemisimple target-specific compression",
            "a chosen-prime F-crystal for the full joint residual not arising from the Kummer diagonalization",
            "weighted distribution uniform in linearly growing conductor",
            "weighted support of the degenerate triple-minor carrier",
        ],
        "scope_warning": (
            "The rank lower bound is for exact semisimple Kummer/Greene lifts of the actual cutoff weight. "
            "It does not classify arbitrary p-dependent sheaves whose trace is merely congruent at one chosen prime."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
