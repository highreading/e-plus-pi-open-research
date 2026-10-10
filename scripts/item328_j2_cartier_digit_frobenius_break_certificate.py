#!/usr/bin/env python3
"""Deterministic certificate for Item 328.

The checker verifies the tied-phase Cartier coefficient, its exact
coefficient recurrence, the unique Frobenius break at index p, and the
linear-depth impulse transfer to the polynomial endpoint.  Finite row
counts and digests are diagnostic only; the all-prime proofs are in the
companion report.
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
RESULT_NAME = "item328_j2_cartier_digit_frobenius_break_certificate.json"

DEPENDENCIES = {
    "sources/item322_j2_fixedM_period_transfer_report.md":
        "8b2ad1806d972ea7ed2b49f488e124ac4609e68758d08690ce3f26f30aae8459",
    "scripts/item322_j2_fixedM_period_transfer_certificate.py":
        "96c9b0f801077904b3e892cdb49fde8ea0f62aa3cb87f594866579b86fde993f",
    "results/item322_j2_fixedM_period_transfer_certificate.json":
        "5266eab4b8856e4c4e3c78e261f85ff11977e06ff64169f602c474f83f06e5cf",
    "sources/item325_j2_conic_involution_recurrence_report.md":
        "a70b204ab2c8e426039f6b0b457edd55bd1eb7735a0fd655b910eccda0b37838",
    "scripts/item325_j2_conic_involution_recurrence_certificate.py":
        "38c283d4a93afb891ee673f8931e780f3c96e7974757080064c6aa003f895e96",
    "results/item325_j2_conic_involution_recurrence_certificate.json":
        "6ff7d4e393a70cd44b143cae227e7a04452c0c5af2ab7a3a287a2074d6275fde",
    "manifests/item325_j2_conic_involution_recurrence_manifest.json":
        "4863c3a367c6b811faa127fb88f01983059faf26b88eaf83f7d7b62f033cb5f9",
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


def legendre_two(prime: int) -> int:
    value = pow(2, (prime - 1) // 2, prime)
    if value == 1:
        return 1
    if value == prime - 1:
        return -1
    raise AssertionError((prime, value))


def h_value(index: int, prime: int) -> int:
    return (
        math.comb(2 * index, index)
        * pow(pow(8, index, prime), -1, prime)
    ) % prime


def h_prefix(index: int, prime: int) -> int:
    return sum(h_value(j, prime) for j in range(index + 1)) % prime


def polynomial_coefficients(n: int, q: int, prime: int) -> list[int]:
    """Coefficients of (1-x)^n(1+x)^(n+q), reduced modulo prime."""
    left = [((-1) ** j * math.comb(n, j)) % prime for j in range(n + 1)]
    right = [math.comb(n + q, j) % prime for j in range(n + q + 1)]
    result = [0] * (2 * n + q + 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] = (result[i + j] + left_value * right_value) % prime
    return result


def binomial_sum(n: int, q: int, prime: int) -> int:
    return sum(
        (-1) ** j * math.comb(q, 2 * j + 1) * math.comb(n, j)
        for j in range((q - 1) // 2 + 1)
    ) % prime


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def tied_row(prime: int, r: int, s: int) -> dict[str, Any]:
    m = s - 1
    d = r + 4
    n = 3 * m + d
    q = 2 * m + d
    degree = 2 * n + q
    M = (14 * m + 5 * d + 1) // 2
    if prime != 6 * m + 2 * d + 1 or prime != 2 * n + 1:
        raise AssertionError((prime, r, s, m, d, n, q, "tied phase"))
    if 2 * M != 14 * m + 5 * d + 1 or q != 2 * (M - prime) + 1:
        raise AssertionError((prime, r, s, M, q, "fixed-M phase"))
    if degree != prime + q - 1 or q % 2 != 1:
        raise AssertionError((prime, degree, q, "degree/parity"))
    if not (3 * q > prime and 2 * q <= prime - 1):
        raise AssertionError((prime, q, "actual range"))

    coeff = polynomial_coefficients(n, q, prime)
    if len(coeff) != degree + 1:
        raise AssertionError((prime, len(coeff), degree))

    recurrence_checks = 0
    for k in range(degree + 1):
        previous = coeff[k - 1] if k >= 1 else 0
        following = coeff[k + 1] if k < degree else 0
        lhs = (k + 1) * following
        rhs = q * coeff[k] + (k - prime - q) * previous
        if (lhs - rhs) % prime != 0:
            raise AssertionError((prime, r, s, k, lhs % prime, rhs % prime, "coefficient recurrence"))
        recurrence_checks += 1

    compatibility = (q * coeff[prime - 1] - (q + 1) * coeff[prime - 2]) % prime
    if compatibility != 0:
        raise AssertionError((prime, r, s, compatibility, "Frobenius compatibility"))

    convolution = binomial_sum(n, q, prime)
    if convolution != ((-1) ** n * coeff[prime]) % prime:
        raise AssertionError((prime, r, s, convolution, coeff[prime], "p-th coefficient"))
    if convolution != coeff[q - 1]:
        raise AssertionError((prime, r, s, convolution, coeff[q - 1], "reciprocity"))

    epsilon = legendre_two(prime)
    H = h_prefix(m, prime)
    if H != (epsilon * (1 - coeff[prime])) % prime:
        raise AssertionError((prime, r, s, H, coeff[prime], "Cartier digit"))

    c_q_closed = math.comb(2 * q, q) * pow(pow(2, q, prime), -1, prime) % prime
    if coeff[q] != c_q_closed or coeff[q] == 0:
        raise AssertionError((prime, r, s, coeff[q], c_q_closed, "endpoint multiplier"))

    # The impulse delta_(p+t)=c_t is the exact difference of two
    # recurrence-consistent continuations whose p-th digits differ by one.
    impulse_checks = 0
    delta_previous = 0
    delta_current = 1
    if delta_current != coeff[0]:
        raise AssertionError((prime, "impulse seed"))
    for t in range(q):
        delta_next = (
            q * delta_current + (t - q) * delta_previous
        ) * pow(t + 1, -1, prime) % prime
        if delta_next != coeff[t + 1]:
            raise AssertionError((prime, r, s, t, delta_next, coeff[t + 1], "impulse transfer"))
        delta_previous, delta_current = delta_current, delta_next
        impulse_checks += 1
    if delta_current != coeff[q] or delta_current == 0:
        raise AssertionError((prime, r, s, delta_current, "endpoint impulse"))

    return {
        "p": prime,
        "r": r,
        "s": s,
        "M": M,
        "m": m,
        "d": d,
        "n": n,
        "q": q,
        "degree": degree,
        "epsilon": epsilon,
        "H_mod_p": H,
        "convolution_mod_p": convolution,
        "c_q_minus_1_mod_p": coeff[q - 1],
        "c_p_mod_p": coeff[prime],
        "c_q_mod_p": coeff[q],
        "recurrence_checks": recurrence_checks,
        "impulse_checks": impulse_checks,
    }


def actual_replay(prime_max: int) -> dict[str, Any]:
    rows = []
    recurrence_checks = 0
    impulse_checks = 0
    for prime, r, s in actual_rows(prime_max):
        row = tied_row(prime, r, s)
        recurrence_checks += row["recurrence_checks"]
        impulse_checks += row["impulse_checks"]
        rows.append((
            row["p"], row["r"], row["s"], row["M"], row["m"], row["d"],
            row["n"], row["q"], row["degree"], row["epsilon"], row["H_mod_p"],
            row["convolution_mod_p"], row["c_p_mod_p"], row["c_q_mod_p"],
        ))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "prime_max_inclusive": prime_max,
        "actual_rows": len(rows),
        "coefficient_recurrence_checks": recurrence_checks,
        "impulse_transfer_checks": impulse_checks,
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:10],
    }


def generic_tied_replay(m_max: int, d_max: int) -> dict[str, Any]:
    """Exact integer coefficient identities before prime reduction."""
    rows: list[tuple[Any, ...]] = []
    for d in range(1, d_max + 1, 2):
        for m in range(m_max + 1):
            n = 3 * m + d
            q = 2 * m + d
            p_symbol = 6 * m + 2 * d + 1
            degree = 2 * n + q
            # Only the three coefficients needed for the exact identity.
            def coefficient(k: int) -> int:
                return sum(
                    (-1) ** i * math.comb(n, i) * math.comb(n + q, k - i)
                    for i in range(max(0, k - (n + q)), min(n, k) + 1)
                )

            convolution = sum(
                (-1) ** j * math.comb(q, 2 * j + 1) * math.comb(n, j)
                for j in range((q - 1) // 2 + 1)
            )
            c_p = coefficient(p_symbol)
            c_low = coefficient(q - 1)
            if degree != p_symbol + q - 1:
                raise AssertionError((m, d, degree, p_symbol, q))
            if convolution != ((-1) ** n) * c_p or convolution != c_low:
                raise AssertionError((m, d, convolution, c_p, c_low))
            rows.append((m, d, n, q, p_symbol, convolution.bit_length(), abs(c_p).bit_length()))
    return {
        "classification": "EXACT FINITE INTEGER REPLAY ONLY",
        "m_max_inclusive": m_max,
        "odd_d_max_inclusive": d_max,
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:10],
    }


def theorem_record() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT; PROOFS IN COMPANION REPORT",
        "tied_phase": {
            "p": "6*m+2*d+1=2*n+1",
            "n": "3*m+d",
            "q": "2*m+d=n-m",
            "polynomial": "F_(m,d)(x)=(1-x)^n*(1+x)^(n+q)=sum_k c_k*x^k",
            "degree": "D=2*n+q=p+q-1",
        },
        "cartier_digit": {
            "convolution": "S_(n,q)=sum_j (-1)^j*binom(q,2*j+1)*binom(n,j)",
            "coefficient_identity": "S_(n,q)=(-1)^n*c_p=c_(q-1)",
            "period": "H_m=epsilon*(1-c_p) modulo p",
            "actual_collision": "after D_(r,s)=0 and ell_r!=0, collision iff c_p=1-epsilon*Theta_(r,s)",
        },
        "coefficient_recurrence": {
            "integer": "(k+1)c_(k+1)=q*c_k+(k-p-q)*c_(k-1)",
            "mod_p": "(k+1)c_(k+1)=q*c_k+(k-q)*c_(k-1)",
            "Frobenius_break": "at k=p-1 the c_p coefficient vanishes and only q*c_(p-1)=(q+1)*c_(p-2) remains",
        },
        "impulse": {
            "seed": "delta_(p-1)=0, delta_p=1",
            "self_similarity": "delta_(p+t)=c_t for 0<=t<=q",
            "endpoint_distance": "D+1-p=q>p/3",
            "endpoint_multiplier": "delta_(D+1)=c_q=2^(-q)*binom(2q,q), a p-unit",
        },
        "scoped_no_go": {
            "method_class": "the local coefficient recurrence plus an endpoint reached after J forward steps, with no external global identity",
            "statement": "for every J<q there are p recurrence-consistent continuations with identical pre-p coefficients and arbitrary c_p",
            "asymptotic": "every bounded-depth or o(p)-depth method in this class is eventually blind to the Cartier digit",
            "scope": "does not exclude reciprocity, nonlinear identities, target-specific arithmetic, average gcds, or weighted zero-density theorems",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=199)
    parser.add_argument("--generic-m-max", type=int, default=8)
    parser.add_argument("--generic-d-max", type=int, default=15)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.prime_max < 101 or args.generic_m_max < 4 or args.generic_d_max < 9:
        raise ValueError("replay bounds too small")

    verify_dependencies()
    output = {
        "schema": "item328-j2-cartier-digit-frobenius-break-v1",
        "strict_labels": {
            "proved": [
                "the exact p-th Cartier-coefficient identity for the Item325 convolution",
                "the affine Cartier-digit form of the actual ell-chart collision",
                "the all-k coefficient recurrence and its unique Frobenius break before the endpoint",
                "the exact self-similar Frobenius impulse",
                "the p-unit endpoint multiplier 2^(-q)*binom(2q,q)",
                "the no-go for every bounded-depth or o(p)-depth local recurrence/endpoint method",
                "zero capacity booking",
            ],
            "exact_finite_only": [
                "all counts, samples, and digests in this JSON",
            ],
            "open": [
                "weighted zero density for the actual affine Cartier target",
                "divisor localization of c_p-(1-epsilon*Theta_(r,s))",
                "arithmetic on the degenerate connection charts",
                "any reduction of the ordinary-j2 ceiling",
            ],
        },
        "theorem": theorem_record(),
        "actual_replay": actual_replay(args.prime_max),
        "generic_tied_replay": generic_tied_replay(args.generic_m_max, args.generic_d_max),
        "capacity": {
            "raw_isolated_ordinary_j2_ceiling_per_6M": "1/105",
            "raw_decimal": "0.0095238095238095238095238095...",
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
