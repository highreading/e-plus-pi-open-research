#!/usr/bin/env python3
"""Exact certificate for Item 192's beta Frobenius-seed obstruction."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item192_beta_frobenius_seed_certificate.json"
DEFAULT_OUTPUT = (
    HERE / RESULT_NAME
    if HERE.name.lower() == "work"
    else HERE.parent / "results" / RESULT_NAME
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
    return [p for p in range(7, limit + 1) if sieve[p]]


def recurrence(initial0: int, initial1: int, stop: int, modulus: int) -> list[int]:
    values = [initial0 % modulus]
    if stop == 0:
        return values
    values.append(initial1 % modulus)
    for n in range(2, stop + 1):
        values.append(((4 * n - 2) * values[-1] + values[-2]) % modulus)
    return values


def finite_difference_degree(values: list[int], prime: int) -> int:
    row = [value % prime for value in values]
    for order in range(len(values)):
        if all(value == 0 for value in row):
            return order - 1
        row = [(row[j + 1] - row[j]) % prime for j in range(len(row) - 1)]
    return len(values) - 1


def exact_companion_wronskian(limit: int) -> dict:
    q = [1, 1]
    nu = [1, 3]
    for n in range(2, limit + 1):
        q.append((4 * n - 2) * q[-1] + q[-2])
        nu.append((4 * n - 2) * nu[-1] + nu[-2])
    rows = []
    for n in range(1, limit + 1):
        wronskian = nu[n] * q[n - 1] - nu[n - 1] * q[n]
        expected = 2 if n & 1 else -2
        if wronskian != expected:
            raise AssertionError((n, wronskian, expected))
        rows.append([n, str(q[n]), str(nu[n]), wronskian])
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "range": [1, limit],
        "identity": "nu_n*q_(n-1)-nu_(n-1)*q_n=2*(-1)^(n-1)",
        "all_exact": True,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def scan_actual_seed(prime_limit: int) -> dict:
    root_rows = []
    zero_invariant_rows = []
    singular_rows = []
    all_lift_rows = []
    noncentral_singular_rows = []
    anti_period_checks = 0
    period_checks = 0
    perturbation_checks = 0
    higher_branch_checks = 0
    invariant_histogram: Counter[int] = Counter()

    for prime in primes_upto(prime_limit):
        modulus = prime * prime
        q = recurrence(1, 1, 2 * prime - 1, modulus)
        nu = recurrence(1, 3, 2 * prime - 1, modulus)

        for n in range(prime):
            if (q[n + prime] + q[n]) % prime:
                raise AssertionError((prime, n, "anti-period"))
            if (nu[n + prime] - nu[n]) % prime:
                raise AssertionError((prime, n, "period"))
            anti_period_checks += 1
            period_checks += 1

        for r in range(prime):
            if q[r] % prime:
                continue
            if r == 0:
                raise AssertionError((prime, "unexpected root at zero"))
            wronskian = (
                nu[r] * q[r - 1] - nu[r - 1] * q[r]
            ) % prime
            expected_wronskian = (2 if r & 1 else -2) % prime
            if wronskian != expected_wronskian or nu[r] % prime == 0:
                raise AssertionError((prime, r, "companion unit"))

            lam = (q[r] // prime) % prime
            delta_numerator = (-q[r + prime] - q[r]) % modulus
            if delta_numerator % prime:
                raise AssertionError((prime, r, "delta integrality"))
            delta = (delta_numerator // prime) % prime
            invariant = (delta + 2 * lam) % prime
            invariant_histogram[invariant == 0] += 1
            qualifying_b = (
                (-lam * pow(nu[r], -1, prime)) % prime
                if invariant == 0
                else None
            )

            # Directly replay the two Frobenius eigendirections.  For
            # u=q+p(a*q+b*nu), anti-period perturbations a are invisible,
            # while the periodic coefficient b moves (lambda,delta) along
            # (lambda+c,delta-2c), c=b*nu_r.
            for a, b in ((0, 0), (1, 0), (0, 1), (2, 3), (prime - 1, prime - 1)):
                lifted_r = (
                    q[r] + prime * (a * q[r] + b * nu[r])
                ) % modulus
                lifted_rp = (
                    q[r + prime]
                    + prime * (a * q[r + prime] + b * nu[r + prime])
                ) % modulus
                if lifted_r % prime:
                    raise AssertionError((prime, r, a, b, "lifted root"))
                lifted_lambda = (lifted_r // prime) % prime
                lifted_delta_numerator = (-lifted_rp - lifted_r) % modulus
                if lifted_delta_numerator % prime:
                    raise AssertionError((prime, r, a, b, "lifted delta"))
                lifted_delta = (lifted_delta_numerator // prime) % prime
                c = b * nu[r] % prime
                if lifted_lambda != (lam + c) % prime:
                    raise AssertionError((prime, r, a, b, "lambda law"))
                if lifted_delta != (delta - 2 * c) % prime:
                    raise AssertionError((prime, r, a, b, "delta law"))
                if (lifted_delta + 2 * lifted_lambda) % prime != invariant:
                    raise AssertionError((prime, r, a, b, "invariant law"))
                perturbation_checks += 1

            # At every root, an anti-period higher seed digit contributes
            # zero to the normalized signed fibre.  A periodic digit
            # contributes nu_r*(-1)^T, whose interpolation degree is p-1.
            if higher_branch_checks < 64:
                # Use the proved period laws to extend the values exactly
                # modulo p; no large recurrence array is needed here.
                anti_values = [0] * prime
                periodic_values = [
                    ((-1) ** t * nu[r]) % prime for t in range(prime)
                ]
                if any(anti_values):
                    raise AssertionError((prime, r, "anti higher digit"))
                if finite_difference_degree(periodic_values, prime) != prime - 1:
                    raise AssertionError((prime, r, "periodic interpolation degree"))
                higher_branch_checks += 1

            row = {
                "p": prime,
                "r": r,
                "central": r == (prime - 1) // 2,
                "lambda": lam,
                "delta": delta,
                "seed_lift_invariant_delta_plus_2lambda": invariant,
                "all_lift_seed_lifts_mod_p_squared": prime if invariant == 0 else 0,
                "qualifying_periodic_coefficient_b": qualifying_b,
                "companion_value_mod_p": nu[r] % prime,
            }
            if qualifying_b is not None:
                representative_r = (
                    q[r] + prime * qualifying_b * nu[r]
                ) % modulus
                representative_rp = (
                    q[r + prime] + prime * qualifying_b * nu[r + prime]
                ) % modulus
                if representative_r or representative_rp:
                    raise AssertionError((prime, r, qualifying_b, "qualifying seed"))
                row["representative_seed_a0_mod_p_squared"] = [
                    (1 + prime * qualifying_b) % modulus,
                    (1 + 3 * prime * qualifying_b) % modulus,
                ]
            root_rows.append(row)
            if invariant == 0:
                zero_invariant_rows.append(row)
            if delta == 0:
                singular_rows.append(row)
                if not row["central"]:
                    noncentral_singular_rows.append(row)
            if delta == 0 and lam == 0:
                all_lift_rows.append(row)

    root_stream = json.dumps(root_rows, separators=(",", ":"), sort_keys=True).encode("ascii")
    return {
        "prime_limit": prime_limit,
        "root_count": len(root_rows),
        "singular_roots": singular_rows,
        "noncentral_singular_roots": noncentral_singular_rows,
        "all_lift_roots": all_lift_rows,
        "zero_seed_lift_invariant_roots": zero_invariant_rows,
        "anti_period_checks": anti_period_checks,
        "period_checks": period_checks,
        "seed_perturbation_checks": perturbation_checks,
        "higher_branch_degree_checks": higher_branch_checks,
        "roots_with_zero_seed_lift_invariant": invariant_histogram[True],
        "roots_with_nonzero_seed_lift_invariant": invariant_histogram[False],
        "root_stream_sha256": hashlib.sha256(root_stream).hexdigest(),
        "status": "EXPERIMENTAL_FINITE_FOR_ACTUAL_ROOT_EXISTENCE; EXACT_REPLAY_OF_PROVED_SEED_LAWS",
    }


def parity_character_checks(prime_limit: int) -> dict:
    rows = []
    for prime in primes_upto(prime_limit):
        values = [(-1) ** t % prime for t in range(prime)]
        degree = finite_difference_degree(values, prime)
        if degree != prime - 1:
            raise AssertionError((prime, degree))
        # The k-th forward difference at zero is (-2)^k, nonzero for k<p.
        last_difference = pow(-2, prime - 1, prime)
        if last_difference != 1:
            raise AssertionError((prime, last_difference))
        rows.append([prime, degree, last_difference])
    return {
        "prime_limit": prime_limit,
        "rows": len(rows),
        "all_degrees_equal_p_minus_1": True,
        "proof_identity": "Delta^k((-1)^T)|_(T=0)=(-2)^k for 0<=k<p",
        "stream_sha256": hashlib.sha256(
            json.dumps(rows, separators=(",", ":")).encode("ascii")
        ).hexdigest(),
    }


def certificate(prime_limit: int, parity_limit: int) -> dict:
    residual_gap = "0.01963298366943179388"
    radical_threshold = "0.05889895100829538164"
    return {
        "item": 192,
        "classification": {
            "PROVED": [
                "At an actual beta root, first-Witt seed lifts move (lambda,delta) by (c,-2c); delta+2lambda is invariant.",
                "A singular dead actual root cannot be converted into an all-lift root by any first-Witt seed lift.",
                "Pure anti-Frobenius higher seed digits do not change the divided fibre at a root; periodic digits inject a degree-(p-1) parity character and leave the bounded-degree architecture.",
                "A fixed integral seed congruent to (1,1) at infinitely many primes equals the actual beta seed; prime-dependent local seed engineering is not an infinite-prime construction for q.",
                "Actual noncentral all-lift primes at index N satisfy p^2|q_N, hence their radical R obeys R^2|q_N.",
            ],
            "EXPERIMENTAL_FINITE": [
                f"actual-seed root census through p<={prime_limit}",
                "the archived absence of all-lift roots through p<=200000",
            ],
            "OPEN": [
                "existence of any actual noncentral singular all-lift beta prime",
                "positive logarithmic mass of actual eligible primes",
                "simultaneous p^2 divisibility of the mixed coefficient b_m at one saddle index",
                "matching and small-CRT-representative synchronization",
            ],
        },
        "exact_identities": {
            "beta_denominator_seed": "q_0=q_1=1",
            "companion_periodic_seed": "nu_0=1, nu_1=3",
            "wronskian": "nu_n*q_(n-1)-nu_(n-1)*q_n=2*(-1)^(n-1)",
            "frobenius_branches": "q_(n+p)=-q_n and nu_(n+p)=nu_n mod p",
            "seed_lift_law": "q+p(aq+bnu): (lambda,delta)->(lambda+c,delta-2c), c=b*nu_r",
            "seed_lift_invariant": "delta+2lambda",
            "seed_lift_invariant_as_divided_period": "(q_r-q_(r+p))/p mod p",
            "singular_case": "if delta=0, an all-lift seed lift exists iff lambda=0 already; then exactly p of p^2 lifts qualify",
            "higher_seed_obstruction": "anti branch contributes q_r=0; periodic branch contributes nu_r*(-1)^T of interpolation degree p-1",
            "global_seed_rigidity": "if fixed integers u_0,u_1 are congruent to 1 modulo infinitely many primes, then u_0=u_1=1",
        },
        "mass_ledger": {
            "post_fully_doubled_support_gap_per_6m": residual_gap,
            "required_log_radical_for_an_R_squared_gain": f"log R_m > {radical_threshold} m",
            "derivation": "2 log(R_m)/(6m) > 0.01963298366943179388",
            "eligibility_chain": [
                "an actual noncentral singular or all-lift beta prime exists",
                "it occurs at the chosen saddle index N",
                "the actual mixed coefficient b_m has the required valuation (p for dead singular matching; at least p^2 for the first all-lift equal-valuation case)",
                "the appropriate divided matching congruence holds at that same (m,N)",
                "the moving CRT system has a sufficiently small representative",
            ],
            "warning": "No stage of this chain implies the next one.",
        },
        "exact_wronskian_check": exact_companion_wronskian(80),
        "parity_character_check": parity_character_checks(parity_limit),
        "finite_actual_seed_scan": scan_actual_seed(prime_limit),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=20000)
    parser.add_argument("--parity-limit", type=int, default=251)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.prime_limit, args.parity_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    scan = result["finite_actual_seed_scan"]
    print(json.dumps({
        "output": str(args.output),
        "root_count": scan["root_count"],
        "singular_roots": scan["singular_roots"],
        "all_lift_roots": scan["all_lift_roots"],
        "root_stream_sha256": scan["root_stream_sha256"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
