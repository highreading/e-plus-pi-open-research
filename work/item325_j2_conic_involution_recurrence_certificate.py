#!/usr/bin/env python3
"""Deterministic certificate for Item 325.

The certificate checks the summation-specific involution of the actual
ordinary-j=2 conic moment, its complete centered-moment evaluation, the
full Fourier support of the punctured weight, and the exact rank-two
recurrence in the moving exponent.  Bounded row counts and digests are
diagnostic only.  The all-prime proofs, including the rational-gauge pole
orbit, are given in the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item325_j2_conic_involution_recurrence_certificate.json"

DEPENDENCIES = {
    "sources/item252_diagonal_modp_report.md":
        "2a8cea239945f77a52d12957a99ffd16c2e4786f6876e1c08e04904f999d2c00",
    "scripts/item252_diagonal_modp_certificate.py":
        "1bd8826880993bfbaaae260768b8349c5d2731e2c9694fbdae4e8654d8d4fc65",
    "results/item252_diagonal_modp_certificate.json":
        "eee18f4fc6ace51b5c29faf84c7424f2013ccf0395033029fd395339fc06ab89",
    "sources/item254_half_binomial_arithmetic_report.md":
        "971d50dab6a8f944334503c46d369151f390db534bc50ec54e1711ecf9b83a2a",
    "scripts/item254_half_binomial_arithmetic_certificate.py":
        "51597cb653af504269341057e1ae02e917d60e94e00b274797fe1da94e0d8b81",
    "results/item254_half_binomial_arithmetic_certificate.json":
        "a81313ecfc726400bffc36c203b1d4b499cfc8b94ebce37277bc8d1a16fa3781",
    "sources/item322_j2_fixedM_period_transfer_report.md":
        "8b2ad1806d972ea7ed2b49f488e124ac4609e68758d08690ce3f26f30aae8459",
    "scripts/item322_j2_fixedM_period_transfer_certificate.py":
        "96c9b0f801077904b3e892cdb49fde8ea0f62aa3cb87f594866579b86fde993f",
    "results/item322_j2_fixedM_period_transfer_certificate.json":
        "5266eab4b8856e4c4e3c78e261f85ff11977e06ff64169f602c474f83f06e5cf",
    "results/item322_j2_fixedM_period_transfer_root_audit.json":
        "c579fe6b873db4f81efb217dcf94142d8f74975b2961cb0f0df209232988f3ee",
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
        path = ROOT / relative
        actual = sha256(path)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


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


def actual_rows(bound: int) -> Iterable[tuple[int, int, int]]:
    for prime in primes_up_to(bound):
        if prime < 11:
            continue
        for s in range(1, (prime - 3) // 6 + 1):
            r = (prime - 6 * s - 3) // 2
            if r >= 1 and r % 2 == 1 and r % 3 != 0:
                yield prime, r, s


def chi(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    symbol = pow(value, (prime - 1) // 2, prime)
    if symbol == 1:
        return 1
    if symbol == prime - 1:
        return -1
    raise AssertionError((value, prime, symbol))


def h_value(index: int, prime: int) -> int:
    return (
        math.comb(2 * index, index)
        * pow(pow(8, index, prime), -1, prime)
    ) % prime


def h_prefix(index: int, prime: int) -> int:
    return sum(h_value(j, prime) for j in range(index + 1)) % prime


def conic_kernel(x: int, prime: int) -> int:
    inverse_two = pow(2, -1, prime)
    return chi(x * (1 - x * inverse_two), prime)


def punctured_moment(prime: int, exponent: int) -> int:
    total = 0
    for x in range(prime):
        if x in (0, 1):
            continue
        total += (
            pow(x, exponent, prime)
            * conic_kernel(x, prime)
            * pow(1 - x, -1, prime)
        )
    return total % prime


def complete_moment(prime: int, exponent: int) -> int:
    return sum(
        pow(x, exponent, prime) * conic_kernel(x, prime)
        for x in range(prime)
    ) % prime


def orbit_polynomial_value(prime: int, exponent: int, x: int) -> int:
    if x % prime == 1:
        return (-exponent) % prime
    numerator = (pow(x, exponent, prime) - pow(2 - x, exponent, prime)) % prime
    return numerator * pow(2 * (1 - x), -1, prime) % prime


def centered_orbit_value(prime: int, exponent: int, x: int) -> int:
    y = (x - 1) % prime
    total = 0
    for j in range((exponent - 1) // 2 + 1):
        total -= math.comb(exponent, 2 * j + 1) * pow(y, 2 * j, prime)
    return total % prime


def even_conic_moment(prime: int, index: int) -> int:
    return sum(
        pow(y, 2 * index, prime) * chi(1 - y * y, prime)
        for y in range(prime)
    ) % prime


def centered_convolution(prime: int, exponent: int) -> int:
    n = (prime - 1) // 2
    return sum(
        (-1) ** j
        * math.comb(exponent, 2 * j + 1)
        * math.comb(n, j)
        for j in range((exponent - 1) // 2 + 1)
    ) % prime


def fourier_weight_value(prime: int, exponent: int, x: int) -> int:
    if x % prime == 1:
        return 0
    return pow(x, exponent, prime) * pow(1 - x, -1, prime) % prime


def fourier_expansion_value(prime: int, exponent: int, x: int) -> int:
    return sum(
        (k + 1) * pow(x, (exponent + k) % (prime - 1), prime)
        for k in range(prime - 1)
    ) % prime


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def actual_replay(prime_max: int) -> dict[str, Any]:
    rows: list[tuple[Any, ...]] = []
    moment_rows = 0
    for prime, r, s in actual_rows(prime_max):
        n = (prime - 1) // 2
        m = s - 1
        q = n - m
        epsilon = chi(2, prime)
        M = (5 * r + 14 * s + 7) // 2
        if 2 * M != 5 * r + 14 * s + 7:
            raise AssertionError((prime, r, s, "M parity"))
        if q != r + 2 * s + 2 or q != 2 * (M - prime) + 1:
            raise AssertionError((prime, r, s, q, M, "fixed-M q"))
        if q % 2 != 1 or not (3 * q > prime and 2 * q <= prime - 1):
            raise AssertionError((prime, r, s, q, "actual q range"))

        H = h_prefix(m, prime)
        W = punctured_moment(prime, q)
        if H != (epsilon * (q + 1) - W) % prime:
            raise AssertionError((prime, r, s, "Item322 conic form"))

        complete_orbit = sum(
            orbit_polynomial_value(prime, q, x) * conic_kernel(x, prime)
            for x in range(prime)
        ) % prime
        if H != (epsilon - complete_orbit) % prime:
            raise AssertionError((prime, r, s, "orbit completion"))

        for x in range(prime):
            if orbit_polynomial_value(prime, q, x) != centered_orbit_value(prime, q, x):
                raise AssertionError((prime, q, x, "centered polynomial"))

        mode_count = (q + 1) // 2
        for j in range(mode_count):
            direct = even_conic_moment(prime, j)
            explicit = (-((-1) ** (n - j)) * math.comb(n, j)) % prime
            if direct != explicit or explicit == 0:
                raise AssertionError((prime, q, j, direct, explicit, "even moment"))
            moment_rows += 1

        convolution = centered_convolution(prime, q)
        formula = (epsilon * (1 - ((-1) ** n) * convolution)) % prime
        if H != formula:
            raise AssertionError((prime, r, s, H, formula, "binomial convolution"))

        if 3 * q <= prime or 6 * mode_count <= prime:
            raise AssertionError((prime, q, mode_count, "linear complexity"))

        rows.append((
            prime, r, s, M, n, m, q, epsilon, H, W,
            complete_orbit, convolution, q - 1, mode_count,
        ))

    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "prime_max_inclusive": prime_max,
        "actual_rows": len(rows),
        "direct_even_moment_rows": moment_rows,
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:10],
    }


def recurrence_replay(prime_max: int) -> dict[str, Any]:
    rows: list[tuple[Any, ...]] = []
    for prime in primes_up_to(prime_max):
        if prime < 5:
            continue
        n = (prime - 1) // 2
        epsilon = chi(2, prime)
        Y = h_prefix(n, prime)
        T = complete_moment(prime, 0)
        W = punctured_moment(prime, 0)
        if Y != epsilon % prime or W != 0 or T != (-h_value(n, prime)) % prime:
            raise AssertionError((prime, Y, T, W, "initial state"))
        for q in range(n + 1):
            expected_Y = h_prefix(n - q, prime)
            expected_T = (-h_value(n - q, prime)) % prime
            expected_W = punctured_moment(prime, q)
            if (Y, T, W) != (expected_Y, expected_T, expected_W):
                raise AssertionError((prime, q, Y, T, W, "state"))
            rows.append((prime, q, Y, T, W))
            if q == n:
                continue
            alpha = (2 * q + 1) * pow(q + 1, -1, prime) % prime
            if alpha == 0:
                raise AssertionError((prime, q, "singular alpha"))
            next_Y = (Y + T) % prime
            next_T = alpha * T % prime
            next_W = (W + epsilon - T) % prime
            Y, T, W = next_Y, next_T, next_W
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "prime_max_inclusive": prime_max,
        "state_rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:12],
    }


def fourier_replay(prime_max: int) -> dict[str, Any]:
    rows: list[tuple[Any, ...]] = []
    for prime in primes_up_to(prime_max):
        if prime < 5:
            continue
        n = (prime - 1) // 2
        for q in range(1, n + 1, 2):
            coefficients = [(k + 1) % prime for k in range(prime - 1)]
            if any(value == 0 for value in coefficients) or len(set((q + k) % (prime - 1) for k in range(prime - 1))) != prime - 1:
                raise AssertionError((prime, q, "full Fourier support"))
            for x in range(1, prime):
                left = fourier_weight_value(prime, q, x)
                right = fourier_expansion_value(prime, q, x)
                if left != right:
                    raise AssertionError((prime, q, x, left, right, "Fourier identity"))
            rows.append((prime, q, prime - 1, q - 1, (q + 1) // 2))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "prime_max_inclusive": prime_max,
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:12],
    }


def pole_orbit_replay(prime_max: int) -> dict[str, Any]:
    rows: list[tuple[Any, ...]] = []
    for prime in primes_up_to(prime_max):
        if prime < 5:
            continue
        n = (prime - 1) // 2
        inverse_two = pow(2, -1, prime)
        zero = (-inverse_two) % prime
        pole = (-1) % prime
        arc = [((zero + step) % prime) for step in range(1, n + 1)]
        if len(set(arc)) != n or arc[-1] != pole:
            raise AssertionError((prime, zero, pole, arc, "exceptional orbit"))
        rows.append((prime, zero, pole, len(arc)))
    return {
        "classification": "EXACT FINITE REPLAY OF THE ALL-PRIME ORBIT GEOMETRY",
        "prime_max_inclusive": prime_max,
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:12],
    }


def theorem_record() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT; PROOFS IN COMPANION REPORT",
        "actual_implication": {
            "family": "p=2*r+6*s+3, 2*M=5*r+14*s+7, m=s-1",
            "q": "(p-1)/2-m=r+2*s+2=2*(M-p)+1",
            "range": "q odd and p/3<q<=(p-1)/2",
            "chart": "after D=0 and ell_r!=0, original collision iff H_m=Theta_(r,s)",
        },
        "summation_specific_completion": {
            "kernel": "K_p(x)=chi(x*(1-x/2)), invariant under x->2-x",
            "orbit_polynomial": "R_q(x)=(x^q-(2-x)^q)/(2*(1-x))",
            "complete_identity": "H_(n-q)=epsilon-sum_[x in F_p] R_q(x)*K_p(x)",
            "centered_polynomial": "R_q(1+y)=-sum_[j=0..(q-1)/2] binom(q,2*j+1)*y^(2*j)",
            "even_moment": "sum_y y^(2*j)*chi(1-y^2)=-(-1)^(n-j)*binom(n,j)",
            "binomial_convolution": "H_(n-q)=epsilon*(1-(-1)^n*sum_j (-1)^j*binom(q,2*j+1)*binom(n,j))",
        },
        "linear_complexity": {
            "pointwise_Fourier_support": "the punctured weight has exactly p-1 nonzero multiplicative Fourier modes",
            "orbit_polynomial_minimal_degree": "q-1 on the active conic points",
            "actual_degree": "q-1>p/3-1",
            "centered_even_modes": "exactly (q+1)/2>p/6, all coefficients and complete moments nonzero",
        },
        "moving_exponent_recurrence": {
            "T_q": "sum_x x^q*K_p(x)=-h_(n-q)",
            "Y_q": "H_(n-q)",
            "system": "Y_(q+1)=Y_q+T_q; T_(q+1)=((2*q+1)/(q+1))*T_q",
            "initial_state": "Y_0=epsilon; T_0=-(-1)^n*epsilon",
            "unit_range": "0<=q<n; every diagonal factor is nonzero",
        },
        "rank_one_gauge_barrier": {
            "equation": "((2*x+1)/(x+1))*R(x+1)-R(x)=1",
            "characteristic_zero": "no rational solution",
            "characteristic_p": "every rational solution, if one exists, has reduced denominator degree at least (p-1)/2",
            "meaning": "the exact rank-two recurrence has no uniformly bounded-degree rational rank-one gauge",
        },
        "strict_scope": {
            "proved": "summation-specific completion and stated bounded-complexity no-go theorems",
            "not_proved": "weighted zero density, target avoidance, degenerate-chart control, or capacity reduction",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--actual-prime-max", type=int, default=199)
    parser.add_argument("--recurrence-prime-max", type=int, default=149)
    parser.add_argument("--fourier-prime-max", type=int, default=89)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.actual_prime_max < 101 or args.recurrence_prime_max < 101 or args.fourier_prime_max < 43:
        raise ValueError("replay bounds too small")

    verify_dependencies()
    output = {
        "schema": "item325-j2-conic-involution-recurrence-v1",
        "strict_labels": {
            "proved": [
                "the conic-involution complete-sum identity",
                "the centered even-moment evaluation and binomial convolution",
                "full multiplicative Fourier support of the punctured pointwise weight",
                "minimal degree q-1 of the orbit polynomial on active conic points",
                "the exact initialized rank-two moving-exponent recurrence",
                "the denominator-degree barrier for every rational rank-one gauge",
                "zero capacity booking",
            ],
            "exact_finite_only": [
                "all row counts, samples, and digests in this JSON",
            ],
            "open": [
                "weighted zero density for H_(s-1)=Theta_(r,s) after the determinant gate",
                "cancellation or factor localization in the terminating binomial convolution",
                "control of the ell-zero and rank-at-most-one charts",
                "any reduction of the ordinary-j2 ceiling",
            ],
        },
        "theorem": theorem_record(),
        "actual_replay": actual_replay(args.actual_prime_max),
        "recurrence_replay": recurrence_replay(args.recurrence_prime_max),
        "fourier_replay": fourier_replay(args.fourier_prime_max),
        "pole_orbit_replay": pole_orbit_replay(args.recurrence_prime_max),
        "capacity": {
            "raw_isolated_ordinary_j2_ceiling_per_6M": "1/105",
            "raw_decimal": "0.0095238095238095238095238095...",
            "adjacent_prime_submechanism": "o(M) logarithmic mass by Item322",
            "new_booking": 0,
            "new_capacity_reduction": 0,
        },
        "dependency_sha256": DEPENDENCIES,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
