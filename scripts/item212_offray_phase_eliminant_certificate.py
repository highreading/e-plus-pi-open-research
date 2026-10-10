#!/usr/bin/env python3
"""Deterministic exact certificate for Item 212.

The checker uses only Python's standard library.  All unbounded claims in the
report are algebraic identities; bounded scans in the JSON are labelled
FINITE and are not extrapolated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item212_offray_phase_eliminant_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item212_offray_phase_eliminant_certificate.json"
)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def phase_coordinates(s_value: int, prime: int) -> tuple[int, int, int, int]:
    k_value = 3 * s_value + 2
    if not is_prime(prime) or prime <= k_value:
        raise ValueError((s_value, prime, k_value))
    q_value = 1 if prime >= 5 * s_value + 4 else 2
    b_value = q_value * prime - 5 * s_value - 4
    if b_value < 0 or b_value >= prime:
        raise AssertionError((s_value, prime, q_value, b_value))
    return k_value, q_value, b_value, k_value % 4


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
        next_value = numerator % prime * pow(n_value + 1, -1, prime) % prime
        state = [state[1], state[2], state[3], next_value]
    return sum(state) % prime, state[3], state


def direct_phase_coefficient_mod(
    s_value: int, b_value: int, component: int, prime: int
) -> int:
    """Finite coefficient D_a, where D_0=g1 and D_1=g0."""
    if component not in (0, 1):
        raise ValueError(component)
    k_value = 3 * s_value + 2
    fourth_exponent = 2 * s_value + component
    linear_exponent = b_value + 1 - component
    answer = 0
    for index in range(fourth_exponent + 1):
        remainder = k_value - 4 * index
        if 0 <= remainder <= linear_exponent:
            answer += (
                (-1) ** (index + remainder)
                * math.comb(fourth_exponent, index)
                * math.comb(linear_exponent, remainder)
            )
    return answer % prime


def falling(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value - offset
    return answer


def rising(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value + offset
    return answer


def normalized_phase_sum(
    s_value: Fraction, b_value: int, residue: int, component: int, stable: bool
) -> tuple[Fraction, bool, int]:
    """Return Phi_a, support-gap flag, and the summation cutoff.

    With stable=True the b-only/full-support cutoff is used.  This is valid on
    actual nodes whenever b <= k+2.  Otherwise the exact integer-s cutoff is
    used.
    """
    if component not in (0, 1) or residue not in range(4):
        raise ValueError((component, residue))
    linear_exponent = b_value + 1 - component
    if residue > linear_exponent:
        return Fraction(0), True, -1
    t_value = (3 * s_value + 2 - residue) / 4
    fourth_exponent = 2 * s_value + component
    full_cutoff = (linear_exponent - residue) // 4
    if stable:
        cutoff = full_cutoff
    else:
        if s_value.denominator != 1 or t_value.denominator != 1:
            raise ValueError("the exact nonstable cutoff requires integral s and t")
        cutoff = min(full_cutoff, int(t_value))
    answer = Fraction(0)
    ratio = Fraction(1)
    for h_value in range(cutoff + 1):
        if h_value:
            ratio *= (t_value - h_value + 1) / (fourth_exponent - t_value + h_value)
        answer += (
            (-1) ** h_value
            * math.comb(linear_exponent, residue + 4 * h_value)
            * ratio
        )
    return answer, False, cutoff


def stable_eliminant(b_value: int, residue: int, component: int) -> tuple[Fraction, bool, int]:
    substituted_s = Fraction(-(b_value + 4), 5)
    return normalized_phase_sum(substituted_s, b_value, residue, component, stable=True)


def fraction_mod(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value.denominator, prime))
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def survivor_compatibility(s_value: int, prime: int) -> tuple[int, list[int]]:
    """Propagate the common-zero terminal survivor to n=p-1."""
    k_value = 3 * s_value + 2
    if not is_prime(prime) or prime <= k_value:
        raise ValueError((s_value, prime, k_value))
    # (W[k-3],W[k-2],W[k-1],W[k])=(1,-1,0,0), with W[k-4]=0.
    state = [1, prime - 1, 0, 0]
    fixed = (5 * s_value + 3) % prime
    for n_value in range(k_value, prime - 1):
        numerator = fixed * (state[3] + state[2] + state[1])
        numerator += (n_value - 3 * s_value) * state[0]
        next_value = numerator % prime * pow(n_value + 1, -1, prime) % prime
        state = [state[1], state[2], state[3], next_value]
    n_value = prime - 1
    obstruction = (
        fixed * (state[3] + state[2] + state[1])
        + (n_value - 3 * s_value) * state[0]
    ) % prime
    return obstruction, state


def sieve(limit: int) -> bytearray:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for divisor in range(2, math.isqrt(limit) + 1):
        if flags[divisor]:
            flags[divisor * divisor : limit + 1 : divisor] = b"\x00" * (
                (limit - divisor * divisor) // divisor + 1
            )
    return flags


def sha256_integer(value: int) -> str:
    return hashlib.sha256(str(value).encode("ascii")).hexdigest()


def certificate(max_scan_s: int, max_eliminant_b: int) -> dict[str, Any]:
    if max_scan_s < 20 or max_eliminant_b < 100:
        raise ValueError("canonical ranges are intentionally nontrivial")

    # Exact mandatory counterexample and the q=2 compatibility false positive.
    mandatory_s, mandatory_p = 299, 2399
    mandatory_k, mandatory_q, mandatory_b, mandatory_r = phase_coordinates(
        mandatory_s, mandatory_p
    )
    if (mandatory_k, mandatory_q, mandatory_b, mandatory_r) != (899, 1, 900, 3):
        raise AssertionError((mandatory_k, mandatory_q, mandatory_b, mandatory_r))
    mandatory_recurrence = coefficient_recurrence_mod(mandatory_s, mandatory_p)
    if mandatory_recurrence != (0, 0, [7, 2392, 0, 0]):
        raise AssertionError(mandatory_recurrence)

    mandatory_eliminants = []
    for component, name in ((0, "g1"), (1, "g0")):
        value, gap, cutoff = stable_eliminant(mandatory_b, mandatory_r, component)
        if gap or cutoff != 224:
            raise AssertionError((component, gap, cutoff))
        if fraction_mod(value, mandatory_p) != 0:
            raise AssertionError((component, value.numerator % mandatory_p))
        mandatory_eliminants.append(
            {
                "component": name,
                "cutoff": cutoff,
                "numerator_digits": len(str(abs(value.numerator))),
                "denominator_digits": len(str(value.denominator)),
                "numerator_sha256": sha256_integer(value.numerator),
                "denominator_sha256": sha256_integer(value.denominator),
                "numerator_mod_2399": value.numerator % mandatory_p,
                "denominator_mod_2399": value.denominator % mandatory_p,
            }
        )

    value_g1, _, _ = stable_eliminant(mandatory_b, mandatory_r, 0)
    value_g0, _, _ = stable_eliminant(mandatory_b, mandatory_r, 1)
    mandatory_numerator_gcd = math.gcd(value_g1.numerator, value_g0.numerator)
    if mandatory_numerator_gcd % mandatory_p:
        raise AssertionError(mandatory_numerator_gcd % mandatory_p)

    false_s, false_p = 13, 53
    false_k, false_q, false_b, false_r = phase_coordinates(false_s, false_p)
    false_compatibility = survivor_compatibility(false_s, false_p)
    false_actual = coefficient_recurrence_mod(false_s, false_p)
    if (false_k, false_q, false_b, false_r) != (41, 2, 37, 1):
        raise AssertionError((false_k, false_q, false_b, false_r))
    if false_compatibility[0] != 0 or false_actual[:2] != (4, 5):
        raise AssertionError((false_compatibility, false_actual))
    mandatory_compatibility = survivor_compatibility(mandatory_s, mandatory_p)
    if mandatory_compatibility[0] != 0:
        raise AssertionError(mandatory_compatibility)

    # FINITE cross-check of the all-prime stable-band equivalence in both q phases.
    scan_limit = 12 * max_scan_s + 50
    prime_flags = sieve(scan_limit)
    stable_nodes = 0
    q_counts = {1: 0, 2: 0}
    zero_nodes: list[list[int]] = []
    scan_hash = hashlib.sha256()
    for s_value in range(1, max_scan_s + 1):
        k_value = 3 * s_value + 2
        for prime in range(k_value + 1, scan_limit + 1):
            if not prime_flags[prime]:
                continue
            _, q_value, b_value, residue = phase_coordinates(s_value, prime)
            if b_value > k_value + 2:
                continue
            stable_nodes += 1
            q_counts[q_value] += 1
            recurrence_g0, recurrence_g1, _ = coefficient_recurrence_mod(s_value, prime)
            direct_g1 = direct_phase_coefficient_mod(s_value, b_value, 0, prime)
            direct_g0 = direct_phase_coefficient_mod(s_value, b_value, 1, prime)
            if (direct_g0, direct_g1) != (recurrence_g0, recurrence_g1):
                raise AssertionError(
                    (s_value, prime, b_value, direct_g0, direct_g1, recurrence_g0, recurrence_g1)
                )
            predicted = []
            for component in (0, 1):
                eliminant, gap, _ = stable_eliminant(b_value, residue, component)
                if gap:
                    predicted.append(0)
                else:
                    t_value = (k_value - residue) // 4
                    fourth_exponent = 2 * s_value + component
                    base = (
                        (-1) ** (t_value + residue)
                        * math.comb(fourth_exponent, t_value)
                    ) % prime
                    predicted.append(base * fraction_mod(eliminant, prime) % prime)
            if tuple(predicted) != (direct_g1, direct_g0):
                raise AssertionError(
                    (s_value, prime, b_value, residue, predicted, direct_g1, direct_g0)
                )
            if (recurrence_g0, recurrence_g1) == (0, 0):
                zero_nodes.append([s_value, prime, q_value, b_value, residue])
            row = (
                s_value,
                prime,
                q_value,
                b_value,
                residue,
                recurrence_g0,
                recurrence_g1,
            )
            scan_hash.update((repr(row) + "\n").encode("ascii"))

    # FINITE rational audit: the only simultaneous rational zeros in this box
    # are the three literal support-gap phase pairs.
    rational_zero_phases = []
    eliminant_hash = hashlib.sha256()
    for b_value in range(max_eliminant_b + 1):
        for residue in range(4):
            row = [b_value, residue]
            both_zero = True
            gap_bits = []
            for component in (0, 1):
                value, gap, cutoff = stable_eliminant(b_value, residue, component)
                row.extend(
                    [
                        gap,
                        cutoff,
                        sha256_integer(value.numerator),
                        sha256_integer(value.denominator),
                    ]
                )
                gap_bits.append(gap)
                both_zero = both_zero and value == 0
            eliminant_hash.update((repr(row) + "\n").encode("ascii"))
            if both_zero:
                rational_zero_phases.append([b_value, residue, *gap_bits])
    expected_gap_phases = [[0, 2, True, True], [0, 3, True, True], [1, 3, True, True]]
    if rational_zero_phases != expected_gap_phases:
        raise AssertionError(rational_zero_phases)

    # Exact row phase identities, one example in each q phase.
    row_examples = []
    for s_value, prime, j_value in ((3, 19, 1), (13, 53, 1), (299, 2399, 1)):
        _, q_value, b_value, _ = phase_coordinates(s_value, prime)
        numerator = (j_value + 1) * prime - s_value - 1
        if numerator % 2:
            raise AssertionError((s_value, prime, j_value, numerator))
        m_value = numerator // 2
        quotient = 5 * j_value + 5 - q_value
        left = 10 * m_value + 1 - b_value
        right = quotient * prime
        if left != right:
            raise AssertionError((left, right))
        row_examples.append(
            {
                "s": s_value,
                "p": prime,
                "j": j_value,
                "m": m_value,
                "q": q_value,
                "b": b_value,
                "identity": f"{left}={quotient}*{prime}",
            }
        )

    return {
        "item": 212,
        "arithmetic": "exact integers, fractions, and prime fields; Python standard library only",
        "proved_all_prime_reduction": {
            "phase": "q=1 if p>=5s+4 else q=2; b=q*p-5s-4; r=(3s+2) mod 4",
            "components": (
                "D_a=[x^k](1-x^4)^(2s+a)(1-x)^(b+1-a), "
                "so D_0=g1 and D_1=g0"
            ),
            "normalized_sum": (
                "if r<=B_a, D_a=(-1)^(t+r)*C(2s+a,t)*Phi_a; "
                "Phi_a=sum_{h=0}^{min(t,floor((B_a-r)/4))} "
                "(-1)^h C(B_a,r+4h)*(t)_fall_h/(2s+a-t+1)_rise_h"
            ),
            "support_gap": "D_a=0 identically when r>B_a",
            "stable_band": (
                "if b<=k+2, both cutoffs are b,r-dependent; modulo p substitute "
                "s=-(b+4)/5, so D_a=0 iff p divides the reduced numerator N_a(b,r)"
            ),
        },
        "support_gap_classification": {
            "all_simultaneous_gap_pairs": [[0, 2], [0, 3], [1, 3]],
            "prime_feasibility": (
                "parity/divisibility excludes (b,r)=(0,2),(1,3); only "
                "b=0,r=3,q=1 remains, namely p=5s+4 with s=3 mod 4"
            ),
            "consequence": "every other common-content node is a genuine cancellation",
        },
        "mandatory_counterexample": {
            "s": mandatory_s,
            "k": mandatory_k,
            "p": mandatory_p,
            "q": mandatory_q,
            "b": mandatory_b,
            "r": mandatory_r,
            "relation": "b=k+1 and p=8s+7",
            "actual_mod_p": {
                "g0": mandatory_recurrence[0],
                "g1": mandatory_recurrence[1],
                "terminal_state": mandatory_recurrence[2],
            },
            "stable_eliminants": mandatory_eliminants,
            "numerator_gcd_digits": len(str(mandatory_numerator_gcd)),
            "numerator_gcd_sha256": sha256_integer(mandatory_numerator_gcd),
            "numerator_gcd_mod_2399": mandatory_numerator_gcd % mandatory_p,
        },
        "first_singularity_compatibility": {
            "necessary_scalar": (
                "propagate W[k-4..k]=(0,1,-1,0,0) to n=p-1 and require "
                "(5s+3)(W[p-1]+W[p-2]+W[p-3])+(p-1-3s)W[p-4]=0 mod p"
            ),
            "mandatory_pass": {
                "obstruction": mandatory_compatibility[0],
                "state_at_p_minus_1": mandatory_compatibility[1],
            },
            "exact_false_positive": {
                "s": false_s,
                "p": false_p,
                "q": false_q,
                "b": false_b,
                "r": false_r,
                "compatibility": false_compatibility[0],
                "survivor_state_at_p_minus_1": false_compatibility[1],
                "actual_g0": false_actual[0],
                "actual_g1": false_actual[1],
                "actual_terminal_state": false_actual[2],
            },
            "scope": (
                "the terminal line plus first-singularity solvability is necessary but not "
                "sufficient; this does not exclude a global fixed-initial-state eliminant"
            ),
        },
        "phase_rate_ledger": {
            "identity": "10m+1-b=(5j+5-q)*p",
            "q1_quotient": "5j+4",
            "q2_quotient": "5j+3",
            "near_phase_bound": (
                "for 0<=b<=B<=5m, total log-prime weight is at most "
                "(B+1)*log(10m+1); hence B=o(m/log m) contributes o(m)"
            ),
            "coefficient_per_m": 0,
            "gap_coefficient_needed_per_m": "0.1177979020165907632818384072...",
            "full_kappa1_cell_coefficient_per_m": "0.4820375017701112...",
            "unresolved": (
                "far moving-b phases are not bounded; they could still exceed the missing coefficient"
            ),
            "examples": row_examples,
        },
        "finite_stable_band_crosscheck": {
            "label": "FINITE; exact recurrence/direct coefficient/eliminant equivalence, not extrapolated",
            "max_s": max_scan_s,
            "prime_limit": scan_limit,
            "stable_nodes": stable_nodes,
            "q_counts": {str(key): value for key, value in q_counts.items()},
            "common_zero_nodes": zero_nodes,
            "stream_sha256": scan_hash.hexdigest(),
        },
        "finite_rational_eliminant_audit": {
            "label": "FINITE rational audit; not an all-b nonvanishing theorem",
            "max_b": max_eliminant_b,
            "simultaneous_zero_phases": rational_zero_phases,
            "stream_sha256": eliminant_hash.hexdigest(),
        },
        "verdict": (
            "PROVED an exact all-prime coefficient normalization and a b-only eliminant in "
            "the stable band b<=k+2; PROVED the only forced support-gap ray is b=0; "
            "PROVED all b=o(m/log m) phases have zero Route-1 rate; REPRODUCED the "
            "off-ray cancellation (299,2399,900); PROVED first-singularity compatibility "
            "alone has an actual-family false positive; far moving-b cancellation remains OPEN."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=80)
    parser.add_argument("--max-b", type=int, default=400)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_s, args.max_b)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "stable_scan_sha256": result["finite_stable_band_crosscheck"]["stream_sha256"],
                "eliminant_scan_sha256": result["finite_rational_eliminant_audit"]["stream_sha256"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
