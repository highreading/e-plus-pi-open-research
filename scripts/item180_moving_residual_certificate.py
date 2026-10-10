#!/usr/bin/env python3
"""Exact certificate for Item 180: the moving residual determinant locus.

All arithmetic in the proved checks is integer or finite-field arithmetic.
The finite scan is explicitly diagnostic and is not extrapolated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item180_moving_residual_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item180_moving_residual_certificate.json"
)


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
    return [q for q in range(7, limit + 1) if sieve[q]]


def coefficient_vector_mod_p(p: int, s: int) -> list[int]:
    """a_n=[x^n](1-x)^(5s+2)/(1-x^4)^(2s+2), 0<=n<p."""
    assert p >= 7 and 0 <= s <= (p - 1) // 3
    a = [0] * p
    a[0] = 1
    for n in range(p - 1):
        rhs = (n - 5 * s - 2) * a[n]
        if n >= 3:
            rhs += (n + 8 * s + 5) * a[n - 3]
        if n >= 4:
            rhs -= (n + 3 * s + 2) * a[n - 4]
        a[n + 1] = rhs * pow(n + 1, -1, p) % p
    return a


def rows_from_recurrence(p: int, s: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return (row0,row1), with rowi=(alpha_i,beta_i)."""
    a = coefficient_vector_mod_p(p, s)
    d = p - 3 * s
    sign = -1 if s % 2 else 1
    row1 = (a[d - 1], sign * a[p - 5] % p)
    row0 = (
        sum(a[d - 1 - k] if d - 1 - k >= 0 else 0 for k in range(4)) % p,
        sign * sum(a[p - 5 + k] for k in range(4)) % p,
    )
    return row0, row1


def determinant_mod_p(p: int, s: int) -> int:
    row0, row1 = rows_from_recurrence(p, s)
    return (row0[0] * row1[1] - row0[1] * row1[0]) % p


def multiply_mod_p(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, u in enumerate(left):
        if u:
            for j, v in enumerate(right):
                out[i + j] = (out[i + j] + u * v) % p
    return out


def rows_from_original_polynomial(
    p: int, s: int
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Independent construction from P=x^(3s)(1-x)^(3s)Q^(p-2s-2)."""
    q_power = [1]
    for _ in range(p - 2 * s - 2):
        q_power = multiply_mod_p(q_power, [1, 1, 1, 1], p)
    signed_binomial = [
        ((-1) ** k * math.comb(3 * s, k)) % p for k in range(3 * s + 1)
    ]
    j_poly = multiply_mod_p(signed_binomial, q_power, p)
    coeff = [0] * (3 * s) + j_poly

    def c(index: int) -> int:
        return coeff[index] if 0 <= index < len(coeff) else 0

    row1 = (c(p - 1), c(2 * p - 1))
    row0 = (
        sum(c(p - 1 - r) for r in range(4)) % p,
        sum(c(2 * p - 1 - r) for r in range(4)) % p,
    )
    return row0, row1


def positive_lift_coefficients(p: int, s: int) -> list[int]:
    """Coefficients of (1-x)^(-b)(1-x^4)^(-c), b=p-5s-2>=0."""
    b = p - 5 * s - 2
    c = 2 * s + 2
    assert b >= 0
    g = [0] * p
    g[0] = 1
    for n in range(p - 1):
        rhs = (n + b) * g[n]
        if n >= 3:
            rhs += (n - 3 + 4 * c) * g[n - 3]
        if n >= 4:
            rhs -= (n - 4 + b + 4 * c) * g[n - 4]
        assert rhs % (n + 1) == 0
        g[n + 1] = rhs // (n + 1)
        assert g[n + 1] >= 0
    return g


def known_ray_labels(p: int, s: int) -> list[str]:
    labels = []
    if p == 3 * s + 4:
        labels.append("p=3s+4")
    if p == 5 * s + 2 and s % 4 == 1:
        labels.append("p=5s+2,s=1(mod4)")
    if p == 5 * s + 1 and s % 4 == 2:
        labels.append("p=5s+1,s=2(mod4)")
    return labels


def valuation(number: int, prime: int) -> int:
    number = abs(number)
    answer = 0
    while number and number % prime == 0:
        number //= prime
        answer += 1
    return answer


def positive_lift_witness(p: int, s: int) -> dict:
    assert not known_ray_labels(p, s)
    assert 20 * s > p and 5 * s < p
    g = positive_lift_coefficients(p, s)
    d = p - 3 * s
    integer_det = (
        (g[d - 2] + g[d - 3] + g[d - 4]) * g[p - 5]
        - (g[p - 4] + g[p - 3] + g[p - 2]) * g[d - 1]
    )
    assert integer_det != 0
    assert integer_det % p == 0
    row0, row1 = rows_from_recurrence(p, s)
    assert row0 != (0, 0) and row1 != (0, 0)
    assert (row0[0] * row1[1] - row0[1] * row1[0]) % p == 0
    quotient = integer_det // (p ** valuation(integer_det, p))
    return {
        "p": p,
        "s": s,
        "b=p-5s-2": p - 5 * s - 2,
        "ratio_interval_check": "1/20<s/p<1/5",
        "integer_determinant_sign": -1 if integer_det < 0 else 1,
        "integer_determinant_bit_length": abs(integer_det).bit_length(),
        "integer_determinant_decimal_digits": len(str(abs(integer_det))),
        "integer_determinant_sha256": hashlib.sha256(
            str(integer_det).encode("ascii")
        ).hexdigest(),
        "p_adic_valuation": valuation(integer_det, p),
        "unit_quotient_mod_p": quotient % p,
        "row0_mod_p": list(row0),
        "row1_mod_p": list(row1),
    }


def proof_checks(direct_limit: int, positive_limit: int) -> dict:
    direct_pairs = 0
    for p in primes_upto(direct_limit):
        for s in range((p - 1) // 3 + 1):
            assert rows_from_recurrence(p, s) == rows_from_original_polynomial(p, s)
            direct_pairs += 1

    positive_pairs = 0
    for p in primes_upto(positive_limit):
        for s in range((p - 2) // 5 + 1):
            if p - 5 * s - 2 < 0:
                continue
            modular = coefficient_vector_mod_p(p, s)
            lifted = positive_lift_coefficients(p, s)
            assert all(modular[n] == lifted[n] % p for n in range(p))
            positive_pairs += 1

    witnesses = [
        positive_lift_witness(337, 52),
        positive_lift_witness(751, 83),
        positive_lift_witness(797, 140),
        positive_lift_witness(857, 71),
    ]
    return {
        "recurrence_vs_original_polynomial": {
            "prime_limit": direct_limit,
            "pairs_checked": direct_pairs,
        },
        "positive_lift_congruence": {
            "prime_limit": positive_limit,
            "pairs_checked": positive_pairs,
        },
        "positive_lift_off_ray_zero_witnesses": witnesses,
    }


def finite_scan(limit: int) -> dict:
    primes = primes_upto(limit)
    zero_pairs: list[list[int]] = []
    off_ray_pairs: list[list[int]] = []
    interior_off_ray_pairs: list[list[int]] = []
    nonzero_counts: dict[str, int] = {}
    classification = Counter()
    histogram = Counter()
    candidate_pairs = 0
    for p in primes:
        roots = []
        for s in range((p - 1) // 3 + 1):
            candidate_pairs += 1
            if determinant_mod_p(p, s) != 0:
                continue
            roots.append(s)
            zero_pairs.append([p, s])
            labels = known_ray_labels(p, s)
            if labels:
                classification[" + ".join(labels)] += 1
            else:
                classification["off_known_rays"] += 1
                off_ray_pairs.append([p, s])
                if p >= 200 and 20 * s > p and 25 * s < 8 * p:
                    interior_off_ray_pairs.append([p, s])
        histogram[len(roots)] += 1
        if roots:
            nonzero_counts[str(p)] = len(roots)

    encoded = json.dumps(zero_pairs, separators=(",", ":")).encode("ascii")
    return {
        "scope": {"prime_min": 7, "prime_max": limit},
        "prime_count": len(primes),
        "candidate_pair_count": candidate_pairs,
        "zero_pair_count": len(zero_pairs),
        "primes_with_at_least_one_zero": len(nonzero_counts),
        "root_count_histogram": {
            str(key): histogram[key] for key in sorted(histogram)
        },
        "maximum_roots_for_one_prime": max(histogram) if histogram else 0,
        "classification_counts": dict(sorted(classification.items())),
        "zero_pairs_sha256": hashlib.sha256(encoded).hexdigest(),
        "zero_pairs": zero_pairs,
        "off_known_rays_count": len(off_ray_pairs),
        "off_known_rays": off_ray_pairs,
        "interior_off_ray_scope": "p>=200 and 1/20<s/p<8/25",
        "interior_off_ray_count": len(interior_off_ray_pairs),
        "interior_off_ray_pairs": interior_off_ray_pairs,
        "per_prime_nonzero_root_counts": nonzero_counts,
        "warning": "Finite exact computation only; no density or uniform root-count claim.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-limit", type=int, default=1000)
    parser.add_argument("--direct-limit", type=int, default=101)
    parser.add_argument("--positive-limit", type=int, default=101)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.scan_limit < 857:
        raise SystemExit("scan-limit must be at least 857 so every stored witness is in scope")
    if args.direct_limit < 7 or args.positive_limit < 7:
        raise SystemExit("cross-check limits must be at least 7")

    obj = {
        "item": 180,
        "status": "PROVED exact moving recurrence and mean-mass transference; finite root scan; uniform moving root count OPEN",
        "definitions": {
            "A_s": "(1-x)^(5s+2)/(1-x^4)^(2s+2)=sum a_n x^n",
            "d": "p-3s",
            "admissible": "p prime >=7 and 0<=s<=(p-1)/3",
            "determinant": "(-1)^s*((a[d-2]+a[d-3]+a[d-4])*a[p-5]-(a[p-4]+a[p-3]+a[p-2])*a[d-1]) mod p",
        },
        "proved": {
            "sub_p_recurrence": "(n+1)a[n+1]=(n-5s-2)a[n]+(n+8s+5)a[n-3]-(n+3s+2)a[n-4], 0<=n<=p-2",
            "positive_lift_sector": "If b=p-5s-2>=0, then a_n is congruent mod p to [x^n](1-x)^(-b)(1-x^4)^(-2s-2) for 0<=n<p.",
            "uniform_height_barrier": "On every compact ratio interval inside (0,1/5), the positive lift coefficient g[d-1] is exp(Omega(p)); this follows from g[d-1]>=binomial(b+d-2,d-1) and uniform Stirling bounds.",
            "mean_mass_transference": "If r_p/p tends to zero, where r_p counts admissible determinant roots for p, then the mean over m<=M of their log-prime weight is o(M). This is a conditional implication, not a proof that r_p=o(p).",
        },
        "proved_checks": proof_checks(args.direct_limit, args.positive_limit),
        "experimental_finite": finite_scan(args.scan_limit),
        "open": [
            "Prove or disprove r_p=o(p) uniformly as p tends to infinity.",
            "Obtain p-adic cancellation estimates for the exponentially large positive-lift determinant; real positivity or saddle size alone cannot decide divisibility by p.",
            "Upgrade the mean-mass implication to a pointwise zero-rate theorem for the actual m-slices.",
            "No conclusion here decides the arithmetic nature of e+pi.",
        ],
        "dependencies": {
            "item174_report_sha256": "9c5be8adfc33252de0d4c49153b7633f7b6dbe0ee5e03d0aeab7dda5d083e7c2",
            "item174_certificate_sha256": "4c3e64285d41b936ea8c61ad1f99194330b8f64d910ecb63676d482fa5f6c891",
            "item174_json_sha256": "125fec0cd9d2444c9296302a884845d2a8d6880a54072d09c0d8e1f7778cc019",
        },
    }
    args.output.write_text(
        json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
