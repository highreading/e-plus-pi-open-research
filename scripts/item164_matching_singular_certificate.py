#!/usr/bin/env python3
"""Exact diagnostics for singular beta roots and sequential matching.

The script is read-only with respect to the Desktop archive.  It scans beta
roots modulo p^2, separates dead first-level singular fibres from all-lift
fibres, and replays every singular prime event in the frozen m<=100 matching
window.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from decimal import Decimal, getcontext
from pathlib import Path


ARCHIVE = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = Path("work/item164_matching_singular_certificate.json")

PINNED = {
    "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json":
        "7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96",
    "results/mixed_cubic_equal_valuation_m1_100_w20.json":
        "ff2db605c747501dc87cf80493c3f957d4c80fe55e5805153afda3b364882273",
    "results/mixed_cubic_equal_valuation_m105_200_step5_w20.json":
        "5558ab9aaf3eed8d0c2f03fa60167ec28917b9a832c49092155cab8889c97b96",
    "results/mixed_cubic_matching_factor_two_and_classification_barrier_certificate.json":
        "8591bc62937f6e07eea35cd903e2cc32f3e72d970f59e584cc1768da349898a2",
    "sources/mixed_cubic_equal_valuation_crt_reduction.md":
        "56b2b3297e5c2d780ad8c7dd5c8605f7c8fdba51fca7786d2669758b3ed1ba93",
    "sources/bessel_denominator_zero_gap_smooth_radical_barrier.md":
        "dac7cd496b4342a8afc6d379274986d2030bc327c9017b3f6fa877108e62e1fc",
    "sources/bessel_denominator_all_lift_branching_wieferich_barrier.md":
        "f02b4b936c2ca810299f037e158e7406214e89ef77e8ca98dcd67b2a9bd00911",
    "results/bessel_denominator_all_lift_branching_certificate.json":
        "09a3622c5a4362127bddede30793b378765040da397d2e0dd50ca4cc50fdddf4",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    return [p for p in range(3, limit + 1, 2) if sieve[p]]


def beta_pairs(limit: int) -> tuple[list[int], list[int]]:
    p_values = [1, 3]
    q_values = [1, 1]
    for n in range(2, limit + 1):
        p_values.append((4 * n - 2) * p_values[-1] + p_values[-2])
        q_values.append((4 * n - 2) * q_values[-1] + q_values[-2])
    return p_values, q_values


def vp(value: int, prime: int) -> int:
    value = abs(value)
    if value == 0:
        return 10**9
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def factor_small(value: int) -> dict[int, int]:
    value = abs(value)
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def q_mod_values(limit: int, modulus: int) -> list[int]:
    values = [1 % modulus, 1 % modulus]
    for n in range(2, limit + 1):
        values.append(((4 * n - 2) * values[-1] + values[-2]) % modulus)
    return values[: limit + 1]


def scan_roots(prime_limit: int) -> tuple[dict[tuple[int, int], dict[str, object]], dict[str, object]]:
    singular: dict[tuple[int, int], dict[str, object]] = {}
    prime_count = 0
    root_count = 0
    central_root_count = 0
    ordinary_root_count = 0
    anti_period_checks = 0
    for p in primes_upto(prime_limit):
        prime_count += 1
        modulus = p * p
        q = q_mod_values(2 * p - 1, modulus)
        for r in range(p):
            assert (q[r + p] + q[r]) % p == 0
            anti_period_checks += 1
            if q[r] % p:
                continue
            root_count += 1
            lam = (q[r] // p) % p
            delta = (-(q[r + p] + q[r]) // p) % p
            central = (2 * r + 1 == p)
            if central:
                central_root_count += 1
                assert delta == 0
            if delta:
                ordinary_root_count += 1
                continue
            entry = {
                "p": p,
                "r": r,
                "central": central,
                "lambda_qr_over_p_mod_p": lam,
                "first_level_type": "all_lift" if lam == 0 else "dead_exact_vp_1",
            }
            # Exhaust the p standard lifts on each singular fibre.  The
            # signed quotient must be constant because delta=0.
            q_lifts = q_mod_values(r + (p - 1) * p, modulus)
            lift_valuations = []
            for t in range(p):
                n = r + t * p
                signed = ((-1) ** t * q_lifts[n]) % modulus
                assert signed % p == 0
                assert (signed // p) % p == lam
                lift_valuations.append(2 if q_lifts[n] % modulus == 0 else 1)
            if lam:
                assert set(lift_valuations) == {1}
            else:
                assert set(lift_valuations) == {2}
            entry["standard_lifts_checked"] = p
            entry["standard_lift_valuation_floor"] = min(lift_valuations)
            singular[(p, r)] = entry
    summary = {
        "prime_limit": prime_limit,
        "odd_prime_count": prime_count,
        "anti_period_residue_checks": anti_period_checks,
        "root_count": root_count,
        "ordinary_root_count": ordinary_root_count,
        "singular_root_count": len(singular),
        "central_root_count": central_root_count,
        "singular_roots": [singular[key] for key in sorted(singular)],
    }
    assert ordinary_root_count + len(singular) == root_count
    return singular, summary


def exact_candidate_replay(
    scan: dict[str, object],
    singular: dict[tuple[int, int], dict[str, object]],
) -> dict[str, object]:
    rows = scan["rows"]
    p_beta, q_beta = beta_pairs(600)
    candidate_count = 0
    delta_prime_slots = 0
    singular_delta_events: list[dict[str, object]] = []
    singular_g_events: list[dict[str, object]] = []
    singular_rows: set[int] = set()
    coefficient_hit_rows: set[tuple[int, int]] = set()
    central_product_checks = 0

    for row in rows:
        m = int(row["m"])
        a = int(row["primitive_positive_form"]["a"])
        b = int(row["primitive_positive_form"]["b"])
        epsilon = int(row["epsilon"])
        for n in range(1, 6 * m + 1):
            if (-1 if n % 2 else 1) != epsilon:
                continue
            candidate_count += 1
            delta_value = math.gcd(b, q_beta[n])
            b0 = b // delta_value
            q0 = q_beta[n] // delta_value
            p_star = b0 * p_beta[n] - epsilon * q0 * a
            g_value = math.gcd(abs(p_star), delta_value)
            central_radical = 1
            for p in factor_small(delta_value):
                delta_prime_slots += 1
                r = n % p
                data = singular.get((p, r))
                if data is None:
                    continue
                B = vp(b, p)
                Q = vp(q_beta[n], p)
                G = vp(g_value, p)
                event = {
                    "m": m,
                    "N": n,
                    "p": p,
                    "r": r,
                    "central": bool(data["central"]),
                    "first_level_type": data["first_level_type"],
                    "vp_b": B,
                    "vp_qN": Q,
                    "vp_g": G,
                }
                if B == Q == 1:
                    lam = int(data["lambda_qr_over_p_mod_p"])
                    s = -1 if r % 2 else 1
                    matching_residue = ((b // p) * p_beta[r] - s * lam * a) % p
                    event["singular_matching_residue"] = matching_residue
                    assert (G > 0) == (matching_residue == 0)
                    if matching_residue == 0:
                        coefficient_hit_rows.add((m, p))
                singular_delta_events.append(event)
                singular_rows.add(m)
                if G:
                    singular_g_events.append(event)
                if data["central"]:
                    central_radical *= p
                    assert (2 * n + 1) % p == 0
            if central_radical > 1:
                assert (2 * n + 1) % central_radical == 0
                central_product_checks += 1

    return {
        "candidate_count": candidate_count,
        "delta_prime_slots": delta_prime_slots,
        "singular_Delta_prime_events": len(singular_delta_events),
        "rows_with_singular_Delta_event": len(singular_rows),
        "singular_g_prime_events": len(singular_g_events),
        "coefficient_hit_rows": [
            {"m": m, "p": p} for m, p in sorted(coefficient_hit_rows)
        ],
        "central_radical_divides_2N_plus_1_checks": central_product_checks,
        "singular_g_events": singular_g_events,
        "first_singular_Delta_events": singular_delta_events[:25],
        "all_singular_events_equal_level_one": all(
            event["vp_b"] == event["vp_qN"] == 1
            for event in singular_delta_events
        ),
    }


def saddle_diagnostics(
    singular: dict[tuple[int, int], dict[str, object]],
    archive: Path,
) -> dict[str, object]:
    outputs: dict[str, object] = {}
    for label, relative in (
        ("m1_100", "results/mixed_cubic_equal_valuation_m1_100_w20.json"),
        ("m105_200_step5", "results/mixed_cubic_equal_valuation_m105_200_step5_w20.json"),
    ):
        rows = json.loads((archive / relative).read_text(encoding="utf-8"))["rows"]
        actual = []
        equal_upper = []
        for row in rows:
            for field, target in (
                ("best_actual", actual),
                ("best_equal_level_upper", equal_upper),
            ):
                candidate = row[field]
                n = int(candidate["N"])
                for p_text, local in candidate.get("local_ledger", {}).items():
                    p = int(p_text)
                    if (p, n % p) in singular:
                        target.append(
                            {
                                "m": int(row["m"]),
                                "N": n,
                                "p": p,
                                "g": str(candidate["g"]),
                                "local_ledger": local,
                            }
                        )
        outputs[label] = {
            "best_actual_singular_events": actual,
            "best_equal_level_upper_singular_events": equal_upper,
        }
    return outputs


def rate_constants(archive: Path) -> dict[str, str]:
    getcontext().prec = 80
    barrier = json.loads(
        (
            archive
            / "results/mixed_cubic_matching_factor_two_and_classification_barrier_certificate.json"
        ).read_text(encoding="utf-8")
    )
    theta = Decimal(barrier["analytic_constants"]["values"]["d_over_2"])
    target = Decimal(
        barrier["analytic_constants"]["values"]["h_minus_d_over_2"]
    )
    r1 = (
        -4 * Decimal(2).ln() + 6 * Decimal(3).ln() - Decimal(3)
    ) / Decimal(6)
    extra = target - r1
    return {
        "theta_log_qN_per_6m": str(theta),
        "rank_one_rate": str(r1),
        "total_target": str(target),
        "post_rank_one_deficit": str(extra),
        "required_dead_singular_radical_rate_if_fully_doubled": str(extra / 2),
        "required_fraction_of_qN_log_height_if_fully_doubled": str(
            extra / (2 * theta)
        ),
        "fully_doubled_radical_supported_on_p_le_3m_ceiling": "1",
        "gap_after_all_p_le_3m_are_optimistically_doubled": str(extra - 1),
        "critical_linear_support_alpha_for_p_le_alpha_m": str(3 * extra),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=ARCHIVE)
    parser.add_argument("--prime-limit", type=int, default=20000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    pinned_actual = {}
    for relative, expected in PINNED.items():
        actual = sha256(args.archive / relative)
        assert actual == expected, (relative, actual, expected)
        pinned_actual[relative] = actual

    singular, root_scan = scan_roots(args.prime_limit)
    exact_scan = json.loads(
        (
            args.archive
            / "results/mixed_cubic_positive_match_exact_scan_m100_N6m.json"
        ).read_text(encoding="utf-8")
    )
    replay = exact_candidate_replay(exact_scan, singular)
    assert replay["candidate_count"] == 15150

    extended_scan = json.loads(
        (
            args.archive
            / "results/bessel_denominator_all_lift_branching_certificate.json"
        ).read_text(encoding="utf-8")
    )
    assert int(extended_scan["prime_limit"]) == 200000
    assert extended_scan["singular_roots"] == [
        {
            "p": 79,
            "r": 39,
            "q_r_mod_p2": 948,
            "q_r_plus_p_mod_p2": 5293,
            "delta_mod_p": 0,
            "central": True,
        }
    ]
    assert not extended_scan["all_p_lift_roots"]

    payload = {
        "schema": "item164-matching-singular-certificate-v1",
        "status": "PASS",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": sha256(Path(__file__)),
        },
        "pinned_inputs": pinned_actual,
        "root_scan": root_scan,
        "pinned_extended_root_scan": {
            "prime_limit": int(extended_scan["prime_limit"]),
            "odd_primes_scanned": int(extended_scan["odd_primes_scanned"]),
            "total_roots_mod_p": int(extended_scan["total_roots_mod_p"]),
            "singular_roots": extended_scan["singular_roots"],
            "all_p_lift_roots": extended_scan["all_p_lift_roots"],
            "classification": "EXPERIMENTAL_FINITE",
        },
        "actual_full_window_replay": replay,
        "saddle_diagnostics": saddle_diagnostics(singular, args.archive),
        "rate_capacity": rate_constants(args.archive),
        "proved_symbolic_statements": [
            "For a first-level root r, signed q_(r+tp)/p is lambda+t*delta mod p.",
            "On a singular fibre delta=0: lambda nonzero gives exact vp(q)=1 on every lift, while lambda=0 gives the all-lift alternative vp(q)>=2.",
            "At equal level vp(b)=vp(q)=1, singular matching is all-or-none on the fibre: (b/p)*p_r - (-1)^r*lambda*a = 0 mod p.",
            "A central root class satisfies p | 2N+1. Hence the product of distinct central singular primes at one index divides 2N+1, and even doubled first-level mass is o(m) for N=O(m/log m).",
            "More generally, any distinct-prime singular mechanism supported on p<=x_m=o(m) has zero doubled logarithmic rate by the prime number theorem.",
            "Even optimistically doubling every distinct prime p<=3m supplies at most rate 1 per 6m, below the post-rank-one deficit by 0.0196329836694317...; a rank-one-plus-first-level-singular proof must use positive mass above 3m or another source.",
        ],
        "classification": {
            "PROVED": [
                "The first-level singular dead/all-lift and all-or-none matching dichotomy.",
                "The central singular radical and p<=o(m) support-scale no-go theorems.",
            ],
            "EXPERIMENTAL": [
                "The exact prime scan and all finite matching-event frequencies.",
                "No noncentral singular root in the scanned range.",
            ],
            "OPEN": [
                "Any all-prime exclusion or mass bound for noncentral singular roots.",
                "Any positive-mass correlation between noncentral dead singular roots, the actual b_m, and one saddle-compatible N.",
                "Higher all-lift/excess-valuation mass at singular primes.",
            ],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.write_bytes(encoded)
    print(
        json.dumps(
            {
                "status": "PASS",
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded).hexdigest(),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
