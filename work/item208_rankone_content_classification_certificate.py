#!/usr/bin/env python3
"""Deterministic exact certificate for Item 208.

All arithmetic is Python standard-library integer or finite-field arithmetic.
Bounded scans are labelled FINITE in the JSON and are never extrapolated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item208_rankone_content_classification_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item208_rankone_content_classification_certificate.json"
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def gamma_binomial(s_value: int, exponent: int) -> int:
    """Exact terminating coefficient, without polynomial expansion."""
    k_value = 3 * s_value + 2
    top = exponent + 2 * k_value
    stop = min(exponent, k_value // 4)
    term = math.comb(top, k_value)
    answer = term
    for index in range(stop):
        numerator = exponent - index
        denominator = index + 1
        for offset in range(4):
            numerator *= k_value - 4 * index - offset
            denominator *= top - 4 * index - offset
        product = term * numerator
        quotient, remainder = divmod(product, denominator)
        if remainder:
            raise AssertionError((s_value, exponent, index, product, denominator))
        term = -quotient
        answer += term
    return answer


def gamma_pair(s_value: int) -> tuple[int, int]:
    return gamma_binomial(s_value, 2 * s_value + 1), gamma_binomial(s_value, 2 * s_value)


def coefficient_recurrence_integer(s_value: int) -> tuple[int, int, list[int]]:
    """Independently reconstruct g0,g1 from Item 205's exact A_n recurrence."""
    k_value = 3 * s_value + 2
    state = [0, 0, 0, 1]  # A[-3], A[-2], A[-1], A[0]
    for n_value in range(k_value):
        numerator = (5 * s_value + 3) * (state[3] + state[2] + state[1])
        numerator += (n_value - 3 * s_value) * state[0]
        quotient, remainder = divmod(numerator, n_value + 1)
        if remainder:
            raise AssertionError((s_value, n_value, numerator, n_value + 1))
        state = [state[1], state[2], state[3], quotient]
    return sum(state), state[3], state


def coefficient_recurrence_mod(s_value: int, prime: int) -> tuple[int, int, list[int]]:
    """Return g0,g1 and (A[k-3],...,A[k]) in F_p."""
    k_value = 3 * s_value + 2
    if not is_prime(prime) or prime <= k_value:
        raise ValueError((s_value, prime, k_value))
    state = [0, 0, 0, 1]
    fixed = (5 * s_value + 3) % prime
    for n_value in range(k_value):
        numerator = fixed * (state[3] + state[2] + state[1])
        numerator += (n_value - 3 * s_value) * state[0]
        next_value = (numerator % prime) * pow(n_value + 1, -1, prime) % prime
        state = [state[1], state[2], state[3], next_value]
    return sum(state) % prime, state[3], state


def frobenius_coefficient_pair(s_value: int, prime: int) -> tuple[int, int, int, int]:
    """The finite-polynomial Frobenius normal form (q,b,g0,g1)."""
    k_value = 3 * s_value + 2
    if not is_prime(prime) or prime <= k_value:
        raise ValueError((s_value, prime, k_value))
    q_value = 1 if prime >= 5 * s_value + 4 else 2
    b_value = q_value * prime - 5 * s_value - 4
    if b_value < 0:
        raise AssertionError((s_value, prime, q_value, b_value))

    def coefficient(fourth_power_exponent: int, linear_exponent: int) -> int:
        answer = 0
        for index in range(min(fourth_power_exponent, k_value // 4) + 1):
            remainder = k_value - 4 * index
            if remainder > linear_exponent:
                continue
            answer += (
                (-1) ** (index + remainder)
                * math.comb(fourth_power_exponent, index)
                * math.comb(linear_exponent, remainder)
            )
        return answer % prime

    gamma0 = coefficient(2 * s_value + 1, b_value)
    gamma1 = coefficient(2 * s_value, b_value + 1)
    return q_value, b_value, gamma0, gamma1


def strip_factorial_support(value: int, factorial: int) -> tuple[int, int]:
    """Remove every prime-power factor supported on primes dividing factorial."""
    answer = abs(value)
    rounds = 0
    while answer > 1:
        common = math.gcd(answer, factorial)
        if common == 1:
            break
        answer //= common
        rounds += 1
    if math.gcd(answer, factorial) != 1:
        raise AssertionError((answer, rounds))
    return answer, rounds


def certificate(max_s: int, ray8_max_s: int) -> dict[str, Any]:
    if max_s < 299 or ray8_max_s < 299:
        raise ValueError("both finite ranges must include the s=299 counterexample")

    factorial = 1
    factorial_end = 0
    scan_hash = hashlib.sha256()
    checkpoints: list[dict[str, Any]] = []
    structural_nodes: list[tuple[int, int]] = []
    off_ray_nodes: list[tuple[int, int]] = []
    max_strip_rounds = 0
    pair299: tuple[int, int] | None = None

    checkpoint_set = {0, 1, 3, 40, 298, 299, 300, max_s}
    for s_value in range(max_s + 1):
        k_value = 3 * s_value + 2
        for factor in range(factorial_end + 1, k_value + 1):
            factorial *= factor
        factorial_end = k_value

        gamma0, gamma1 = gamma_pair(s_value)
        if gamma0 <= 0 or gamma1 <= 0:
            raise AssertionError((s_value, gamma0, gamma1))
        common = math.gcd(gamma0, gamma1)
        large_part, rounds = strip_factorial_support(common, factorial)
        max_strip_rounds = max(max_strip_rounds, rounds)

        endpoint = 5 * s_value + 4
        structural = endpoint if s_value % 4 == 3 and is_prime(endpoint) else 1
        expected = structural * (2399 if s_value == 299 else 1)
        if large_part != expected:
            raise AssertionError(
                (s_value, large_part, expected, "FINITE range has an unlisted large factor")
            )

        if structural != 1:
            structural_nodes.append((s_value, structural))
            mod0, mod1, _ = coefficient_recurrence_mod(s_value, structural)
            if (mod0, mod1) != (0, 0):
                raise AssertionError((s_value, structural, mod0, mod1))
        if s_value == 299:
            pair299 = (gamma0, gamma1)
            off_ray_nodes.append((s_value, 2399))

        row = (s_value, large_part, structural, rounds, gamma0.bit_length(), gamma1.bit_length())
        scan_hash.update((repr(row) + "\n").encode("ascii"))
        if s_value in checkpoint_set:
            checkpoints.append(
                {
                    "s": s_value,
                    "k": k_value,
                    "large_gcd_part": str(large_part),
                    "structural_factor": str(structural),
                    "g0_bits": gamma0.bit_length(),
                    "g1_bits": gamma1.bit_length(),
                    "factorial_gcd_rounds": rounds,
                }
            )

    # Independent exact-integer recurrence at selected nodes.
    recurrence_checks = []
    for s_value in sorted(checkpoint_set):
        expected_pair = gamma_pair(s_value)
        actual0, actual1, state = coefficient_recurrence_integer(s_value)
        if (actual0, actual1) != expected_pair:
            raise AssertionError((s_value, actual0, actual1, expected_pair))
        recurrence_checks.append(
            {
                "s": s_value,
                "terminal_state_mod_1000000007": [value % 1_000_000_007 for value in state],
            }
        )

    if pair299 is None:
        raise AssertionError("missing s=299")
    s_counterexample = 299
    k_counterexample = 899
    structural_prime = 1499
    counterexample_prime = 2399
    if not is_prime(structural_prime) or not is_prime(counterexample_prime):
        raise AssertionError((structural_prime, counterexample_prime))
    if counterexample_prime != 8 * s_counterexample + 7:
        raise AssertionError(counterexample_prime)
    if counterexample_prime == 5 * s_counterexample + 4:
        raise AssertionError("counterexample accidentally lies on the structural ray")

    counter_mod = coefficient_recurrence_mod(s_counterexample, counterexample_prime)
    structural_mod = coefficient_recurrence_mod(s_counterexample, structural_prime)
    if counter_mod != (0, 0, [7, 2392, 0, 0]):
        raise AssertionError(counter_mod)
    if structural_mod != (0, 0, [468, 1031, 0, 0]):
        raise AssertionError(structural_mod)
    if pair299[0] % counterexample_prime or pair299[1] % counterexample_prime:
        raise AssertionError("exact integers miss p=2399")
    if pair299[0] % structural_prime or pair299[1] % structural_prime:
        raise AssertionError("exact integers miss p=1499")
    if structural_prime * counterexample_prime != 3_596_101:
        raise AssertionError("product")

    # Check the all-p Frobenius normal form in both q-regimes and at both s=299 roots.
    frobenius_checks = []
    for s_value, prime in ((3, 13), (10, 37), (10, 59), (299, 1499), (299, 2399)):
        q_value, b_value, f0, f1 = frobenius_coefficient_pair(s_value, prime)
        r0, r1, _ = coefficient_recurrence_mod(s_value, prime)
        if (f0, f1) != (r0, r1):
            raise AssertionError((s_value, prime, f0, f1, r0, r1))
        frobenius_checks.append(
            {"s": s_value, "p": prime, "q": q_value, "b": b_value, "g0": f0, "g1": f1}
        )

    # Targeted modular scan of the tempting p=8s+7 line.
    ray8_hash = hashlib.sha256()
    ray8_prime_nodes = 0
    ray8_hits: list[dict[str, int]] = []
    for s_value in range(ray8_max_s + 1):
        prime = 8 * s_value + 7
        if not is_prime(prime):
            continue
        ray8_prime_nodes += 1
        gamma0_mod, gamma1_mod, state = coefficient_recurrence_mod(s_value, prime)
        ray8_hash.update((repr((s_value, prime, gamma0_mod, gamma1_mod)) + "\n").encode("ascii"))
        if (gamma0_mod, gamma1_mod) == (0, 0):
            ray8_hits.append(
                {"s": s_value, "p": prime, "terminal_state": state}
            )
    if ray8_max_s == 5000 and ray8_hits != [
        {"s": 299, "p": 2399, "terminal_state": [7, 2392, 0, 0]}
    ]:
        raise AssertionError((ray8_max_s, ray8_hits))

    # One actual cell row for the counterexample and its affine-ray identity.
    j_value = 1
    m_value = ((j_value + 1) * counterexample_prime - s_counterexample - 1) // 2
    if (m_value, 16 * m_value + 1, (8 * j_value + 7) * counterexample_prime) != (
        2249,
        35985,
        35985,
    ):
        raise AssertionError((m_value, 16 * m_value + 1))
    admissible_j = [
        j
        for j in range(1, (counterexample_prime - 3) // 2 + 1)
        if j % 2 == s_counterexample % 2
    ]
    if len(admissible_j) != 599:
        raise AssertionError(len(admissible_j))

    return {
        "item": 208,
        "arithmetic": "exact integers and exact prime-field recurrence; no integer factorization",
        "proved_formulas": {
            "gamma0": "[x^(3s+2)] Q^(2s+1)/(1-x)^(3s+3)",
            "gamma1": "[x^(3s+2)] Q^(2s)/(1-x)^(3s+3)",
            "coefficient_recurrence": (
                "(n+1)A[n+1]=(5s+3)(A[n]+A[n-1]+A[n-2])+(n-3s)A[n-3]"
            ),
            "frobenius_phase": (
                "q=1 if p>=5s+4 else 2; b=qp-5s-4; modulo p, "
                "g1=[x^k](1-x^4)^(2s)(1-x)^(b+1), and g0 is the "
                "sum of its coefficients at k,k-1,k-2,k-3"
            ),
            "affine_ray_row_identity": (
                "if p=a*s+b on a cell row, then p divides 2*a*m+a-b"
            ),
        },
        "classification_counterexample": {
            "s": s_counterexample,
            "k": k_counterexample,
            "p": counterexample_prime,
            "relation": "p=8s+7",
            "structural_ray_prime_at_same_s": structural_prime,
            "large_gcd_part": 3_596_101,
            "large_gcd_factor_identity": "3596101=1499*2399",
            "mod_2399": {"g0": counter_mod[0], "g1": counter_mod[1], "state": counter_mod[2]},
            "mod_1499": {"g0": structural_mod[0], "g1": structural_mod[1], "state": structural_mod[2]},
            "point": "p=2399 is an off-structural-ray cancellation, so the proposed classification is false",
        },
        "finite_all_prime_divisor_audit": {
            "label": "FINITE; exact residual after removing the complete (3s+2)! prime support",
            "max_s": max_s,
            "stream_sha256": scan_hash.hexdigest(),
            "max_factorial_gcd_rounds": max_strip_rounds,
            "structural_node_count": len(structural_nodes),
            "structural_first_five": [list(row) for row in structural_nodes[:5]],
            "structural_last_five": [list(row) for row in structural_nodes[-5:]],
            "off_structural_nodes": [list(row) for row in off_ray_nodes],
            "checkpoints": checkpoints,
            "independent_recurrence_checks": recurrence_checks,
        },
        "finite_p_equals_8s_plus_7_scan": {
            "label": "FINITE targeted modular-recurrence scan; not an all-s theorem",
            "max_s": ray8_max_s,
            "prime_nodes": ray8_prime_nodes,
            "stream_sha256": ray8_hash.hexdigest(),
            "hits": ray8_hits,
        },
        "frobenius_checks": frobenius_checks,
        "row_rate_ledger": {
            "proved_structural_ray": "p=5s+4 gives p|(10m+1), hence O(log m) total log-weight",
            "counterexample_affine_identity": {
                "row": {"m": m_value, "p": counterexample_prime, "j": j_value, "s": s_counterexample},
                "identity": "16m+1=(8j+7)p",
                "admissible_j_count_for_this_fixed_pair": len(admissible_j),
                "scope": "this fixed exceptional pair has finite support and zero asymptotic rate",
            },
            "conditional_finite_union": (
                "a fixed finite union p=a_r*s+b_r has O(log m) total log-weight, "
                "because each ray prime divides 2*a_r*m+a_r-b_r"
            ),
            "open": "no finite-union classification of all actual large common-content primes is proved",
        },
        "verdict": (
            "REFUTED the proposed all-s classification by the exact pair (s,p)=(299,2399); "
            "PROVED the Frobenius phase reduction and the zero-rate affine-ray ledger; "
            "FINITE scans find no other off-structural pair through s=1500 and only this hit "
            "on p=8s+7 through s=5000; the all-s off-ray set remains OPEN."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=1500)
    parser.add_argument("--ray8-max-s", type=int, default=5000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_s, args.ray8_max_s)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "finite_scan_sha256": result["finite_all_prime_divisor_audit"]["stream_sha256"],
                "ray8_scan_sha256": result["finite_p_equals_8s_plus_7_scan"]["stream_sha256"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
