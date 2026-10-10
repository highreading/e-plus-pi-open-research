#!/usr/bin/env python3
"""Deterministic exact certificate for Item 214.

This checker imports the frozen Item 212 phase formulas from the same
directory.  It uses only Python's standard library and labels every bounded
factorization statement FINITE.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import item212_offray_phase_eliminant_certificate as phase  # noqa: E402


DEFAULT_OUTPUT = (
    HERE / "item214_stable_eliminant_gcd_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item214_stable_eliminant_gcd_certificate.json"
)


def rising(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value + offset
    return answer


def common_term_phase_sums(b_value: int, residue: int) -> tuple[Fraction, Fraction]:
    """Return (Phi_g1,Phi_g0) from Item 214's common-term recurrence."""
    if b_value < 0 or residue not in range(4):
        raise ValueError((b_value, residue))
    # The formal simultaneous support gaps are handled literally.
    if residue > b_value:
        phi_g0 = Fraction(0)
        phi_g1 = Fraction(1) if residue == b_value + 1 else Fraction(0)
        return phi_g1, phi_g0

    alpha = Fraction(3 * b_value + 2 + 5 * residue, 20)
    delta = Fraction(residue - b_value - 2, 4)
    cutoff = (b_value - residue) // 4
    term = Fraction(math.comb(b_value, residue))
    phi_g1 = Fraction(0)
    phi_g0 = Fraction(0)

    for h_value in range(cutoff + 1):
        degree = residue + 4 * h_value
        phi_g1 += term * Fraction(b_value + 1, b_value + 1 - degree)
        phi_g0 += term * delta / (delta + h_value)
        if h_value == cutoff:
            break
        ratio = Fraction(1)
        for offset in range(4):
            ratio *= Fraction(
                b_value - degree - offset,
                degree + offset + 1,
            )
        ratio *= (alpha + h_value) / (delta + h_value)
        term *= ratio

    # C(b+1,b+1)=1 supplies one endpoint not present in C(b,*).
    if (b_value + 1 - residue) % 4 == 0:
        endpoint = (b_value + 1 - residue) // 4
        phi_g1 += rising(alpha, endpoint) / rising(delta, endpoint)
    return phi_g1, phi_g0


def phase_sigma(residue: int) -> int:
    """The unique s mod 4 with 3s+2=residue mod 4."""
    if residue not in range(4):
        raise ValueError(residue)
    return (3 * (residue - 2)) % 4


def phase_feasible_nodes(b_value: int, residue: int, prime: int) -> list[tuple[int, int]]:
    """Return all actual stable nodes (q,s) represented by (b,r,p)."""
    nodes = []
    for q_value in (1, 2):
        numerator = q_value * prime - b_value - 4
        if numerator % 5:
            continue
        s_value = numerator // 5
        if s_value < 0:
            continue
        k_value = 3 * s_value + 2
        if prime <= k_value or k_value % 4 != residue or b_value > k_value + 2:
            continue
        actual_q = 1 if prime >= 5 * s_value + 4 else 2
        if actual_q == q_value:
            nodes.append((q_value, s_value))
    return nodes


def stable_gcd(b_value: int, residue: int) -> tuple[int, Fraction, Fraction]:
    phi_g1, gap_g1, _ = phase.stable_eliminant(b_value, residue, 0)
    phi_g0, gap_g0, _ = phase.stable_eliminant(b_value, residue, 1)
    if gap_g1:
        phi_g1 = Fraction(0)
    if gap_g0:
        phi_g0 = Fraction(0)
    common = math.gcd(abs(phi_g1.numerator), abs(phi_g0.numerator))
    return common, phi_g1, phi_g0


def factor_over_sieve(value: int, primes: list[int], ceiling: int) -> tuple[Counter[int], int]:
    remainder = abs(value)
    factors: Counter[int] = Counter()
    for prime in primes:
        if prime > ceiling:
            break
        while remainder and remainder % prime == 0:
            factors[prime] += 1
            remainder //= prime
    return factors, remainder


def height_log_bound(b_value: int) -> float:
    """The explicit crude logarithmic numerator bound proved in the report."""
    return (
        math.log(b_value + 2)
        + (b_value + 1) * math.log(2)
        + Fraction(b_value + 2, 2) * math.log(10 * (b_value + 3))
    )


def certificate(max_b: int, recurrence_max_b: int) -> dict[str, Any]:
    if max_b < 900 or recurrence_max_b < 50:
        raise ValueError("the canonical run must retain b=900 and a nontrivial recurrence audit")

    # Independent common-term reconstruction of Item 212's fractions.
    recurrence_hash = hashlib.sha256()
    recurrence_nodes = 0
    recurrence_set = set(range(recurrence_max_b + 1)) | {299, 400, 899, 900}
    for b_value in sorted(value for value in recurrence_set if value <= max_b):
        for residue in range(4):
            paired_g1, paired_g0 = common_term_phase_sums(b_value, residue)
            item_g1, gap_g1, cutoff_g1 = phase.stable_eliminant(b_value, residue, 0)
            item_g0, gap_g0, cutoff_g0 = phase.stable_eliminant(b_value, residue, 1)
            if gap_g1:
                item_g1 = Fraction(0)
            if gap_g0:
                item_g0 = Fraction(0)
            if (paired_g1, paired_g0) != (item_g1, item_g0):
                raise AssertionError(
                    (b_value, residue, paired_g1, paired_g0, item_g1, item_g0)
                )
            recurrence_nodes += 1
            row = (
                b_value,
                residue,
                cutoff_g1,
                cutoff_g0,
                hashlib.sha256(str(paired_g1).encode("ascii")).hexdigest(),
                hashlib.sha256(str(paired_g0).encode("ascii")).hexdigest(),
            )
            recurrence_hash.update((repr(row) + "\n").encode("ascii"))

    # FINITE complete factorization scan.  Residual=1 certifies that every
    # factor was actually removed; no probable-prime assumption is used.
    factor_ceiling = 4 * max_b + 100
    flags = phase.sieve(factor_ceiling)
    primes = [value for value, flag in enumerate(flags) if flag]
    factor_hash = hashlib.sha256()
    factorized_phase_count = 0
    distinct_factor_occurrences = 0
    total_factor_multiplicity = 0
    phase_feasible_hits: list[dict[str, int]] = []
    maximum_prime_factor = 0
    maximum_factor_ratio = Fraction(0)
    maximum_factor_ratio_node: tuple[int, int, int] | None = None
    support_gap_phases = []

    for b_value in range(max_b + 1):
        for residue in range(4):
            common, phi_g1, phi_g0 = stable_gcd(b_value, residue)
            if common == 0:
                support_gap_phases.append([b_value, residue])
                factor_hash.update((repr((b_value, residue, "gcd=0")) + "\n").encode("ascii"))
                continue
            ceiling = 4 * b_value + 100
            factors, residual = factor_over_sieve(common, primes, ceiling)
            if residual != 1:
                raise AssertionError(
                    (b_value, residue, residual, "FINITE factor ceiling was insufficient")
                )
            factorized_phase_count += 1
            distinct_factor_occurrences += len(factors)
            total_factor_multiplicity += sum(factors.values())
            if factors:
                local_max = max(factors)
                maximum_prime_factor = max(maximum_prime_factor, local_max)
                ratio = Fraction(local_max, max(1, b_value))
                if ratio > maximum_factor_ratio:
                    maximum_factor_ratio = ratio
                    maximum_factor_ratio_node = (b_value, residue, local_max)
            for prime in factors:
                if prime <= 5:
                    continue
                for q_value, s_value in phase_feasible_nodes(b_value, residue, prime):
                    g0_mod, g1_mod, terminal = phase.coefficient_recurrence_mod(s_value, prime)
                    if (g0_mod, g1_mod) != (0, 0):
                        raise AssertionError(
                            (b_value, residue, prime, q_value, s_value, g0_mod, g1_mod)
                        )
                    phase_feasible_hits.append(
                        {
                            "b": b_value,
                            "r": residue,
                            "p": prime,
                            "q": q_value,
                            "s": s_value,
                            "k": 3 * s_value + 2,
                            "valuation_in_eliminant_gcd": factors[prime],
                            "terminal_t": terminal[0],
                        }
                    )
            factor_row = (
                b_value,
                residue,
                str(common),
                tuple(sorted(factors.items())),
                hashlib.sha256(str(phi_g1).encode("ascii")).hexdigest(),
                hashlib.sha256(str(phi_g0).encode("ascii")).hexdigest(),
            )
            factor_hash.update((repr(factor_row) + "\n").encode("ascii"))

    expected_hit = [
        {
            "b": 900,
            "r": 3,
            "p": 2399,
            "q": 1,
            "s": 299,
            "k": 899,
            "valuation_in_eliminant_gcd": 1,
            "terminal_t": 7,
        }
    ]
    if phase_feasible_hits != expected_hit:
        raise AssertionError(phase_feasible_hits)

    # The mandatory full factorization.
    mandatory_common, mandatory_g1, mandatory_g0 = stable_gcd(900, 3)
    mandatory_factors, mandatory_residual = factor_over_sieve(
        mandatory_common, primes, factor_ceiling
    )
    expected_mandatory = Counter(
        {
            2: 449,
            911: 1,
            971: 1,
            991: 1,
            1031: 1,
            1051: 1,
            1091: 1,
            1151: 1,
            1171: 1,
            1231: 1,
            1291: 1,
            2399: 1,
        }
    )
    if mandatory_residual != 1 or mandatory_factors != expected_mandatory:
        raise AssertionError((mandatory_factors, mandatory_residual))
    infeasible_large = [prime for prime in mandatory_factors if prime not in (2, 2399)]
    if any(prime % 20 != 11 for prime in infeasible_large):
        raise AssertionError(infeasible_large)
    mandatory_congruence = (900 + 4 + 5 * phase_sigma(3)) % 20
    if mandatory_congruence != 19 or 2399 % 20 != 19:
        raise AssertionError((mandatory_congruence, 2399 % 20))

    # Check the phase-feasibility congruence on a broad finite grid.  The proof
    # itself is the one-line substitution qp=b+4+5s in the report.
    congruence_hash = hashlib.sha256()
    congruence_checks = 0
    for s_value in range(1, 301):
        for prime in primes:
            if prime <= 3 * s_value + 2:
                continue
            q_value = 1 if prime >= 5 * s_value + 4 else 2
            b_value = q_value * prime - 5 * s_value - 4
            if b_value < 0:
                continue
            residue = (3 * s_value + 2) % 4
            sigma = phase_sigma(residue)
            right = (b_value + 4 + 5 * sigma) % 20
            if (q_value * prime - right) % 20:
                raise AssertionError((s_value, prime, q_value, b_value, residue, sigma, right))
            congruence_checks += 1
            congruence_hash.update(
                (repr((s_value, prime, q_value, b_value, residue, right)) + "\n").encode("ascii")
            )

    height_checkpoints = []
    for b_value in (10, 100, 400, 900):
        largest_log_numerator = 0.0
        for residue in range(4):
            _, phi_g1, phi_g0 = stable_gcd(b_value, residue)
            for value in (phi_g1, phi_g0):
                if value.numerator:
                    largest_log_numerator = max(
                        largest_log_numerator,
                        math.log(abs(value.numerator)),
                    )
        bound = float(height_log_bound(b_value))
        if largest_log_numerator > bound + 1e-10:
            raise AssertionError((b_value, largest_log_numerator, bound))
        height_checkpoints.append(
            {
                "b": b_value,
                "largest_log_abs_numerator": largest_log_numerator,
                "proved_log_bound": bound,
            }
        )

    return {
        "item": 214,
        "arithmetic": "exact fractions, integers, and complete trial division in a declared finite range",
        "proved_common_term_recurrence": {
            "parameters": "alpha=(3b+2+5r)/20; delta=(r-b-2)/4",
            "sums": (
                "Phi_g1=sum C(b+1,r+4h)*(alpha)_h/(delta)_h; "
                "Phi_g0=sum C(b,r+4h)*(alpha)_h/(delta+1)_h"
            ),
            "common_term": "T_h=C(b,r+4h)*(alpha)_h/(delta)_h",
            "term_ratio": (
                "T_(h+1)/T_h = product_{u=0}^3 (b-r-4h-u)/(r+4h+u+1) "
                "* (alpha+h)/(delta+h)"
            ),
            "weights": (
                "apart from the possible g1 endpoint C(b+1,b+1), "
                "Phi_g1=sum T_h*(b+1)/(b+1-r-4h), "
                "Phi_g0=sum T_h*delta/(delta+h)"
            ),
            "scope": "exact for every b>=0 and r in {0,1,2,3}, with support gaps handled separately",
        },
        "proved_phase_feasibility": {
            "sigma_by_r": {str(residue): phase_sigma(residue) for residue in range(4)},
            "necessary_congruence": "q*p = b+4+5*sigma_r (mod 20)",
            "derivation": "s=sigma_r (mod 4) and q*p=b+4+5s",
            "q1": "p=b+4+5*sigma_r (mod 20)",
            "q2": "2p=b+4+5*sigma_r (mod 20); an odd right side is impossible",
        },
        "mandatory_b900_factorization": {
            "gcd": str(mandatory_common),
            "factorization": [[prime, exponent] for prime, exponent in sorted(mandatory_factors.items())],
            "identity": (
                "G(900,3)=2^449*911*971*991*1031*1051*1091*1151*1171*1231*1291*2399"
            ),
            "phase_required_residue_mod_20": 19,
            "infeasible_odd_factors_mod_20": {
                "residue": 11,
                "factors": infeasible_large,
            },
            "unique_feasible_factor": 2399,
            "node": {"s": 299, "p": 2399, "q": 1, "b": 900, "r": 3, "k": 899},
            "g1_numerator_sha256": hashlib.sha256(
                str(mandatory_g1.numerator).encode("ascii")
            ).hexdigest(),
            "g0_numerator_sha256": hashlib.sha256(
                str(mandatory_g0.numerator).encode("ascii")
            ).hexdigest(),
        },
        "finite_factorization_scan": {
            "label": "FINITE complete factorization through b=max_b; no extrapolation",
            "max_b": max_b,
            "per_phase_trial_division_ceiling": "4*b+100",
            "all_residuals_after_division": 1,
            "factorized_phase_count": factorized_phase_count,
            "support_gap_phases": support_gap_phases,
            "distinct_factor_occurrences": distinct_factor_occurrences,
            "total_factor_multiplicity": total_factor_multiplicity,
            "maximum_prime_factor": maximum_prime_factor,
            "maximum_factor_ratio": {
                "numerator": maximum_factor_ratio.numerator,
                "denominator": maximum_factor_ratio.denominator,
                "node": list(maximum_factor_ratio_node) if maximum_factor_ratio_node else None,
            },
            "phase_feasible_hits": phase_feasible_hits,
            "stream_sha256": factor_hash.hexdigest(),
        },
        "finite_recurrence_crosscheck": {
            "label": "FINITE independent common-term reconstruction; not an all-b factorization theorem",
            "max_contiguous_b": recurrence_max_b,
            "extra_b": sorted(value for value in recurrence_set if value > recurrence_max_b and value <= max_b),
            "nodes": recurrence_nodes,
            "stream_sha256": recurrence_hash.hexdigest(),
        },
        "finite_congruence_crosscheck": {
            "label": "FINITE check of the separately proved congruence identity",
            "s_max": 300,
            "prime_max": factor_ceiling,
            "nodes": congruence_checks,
            "stream_sha256": congruence_hash.hexdigest(),
        },
        "proved_height_ledger": {
            "bound": (
                "log|N_a(b,r)| <= log(b+2)+(b+1)log2+((b+2)/2)log(10(b+3)) "
                "whenever N_a is nonzero"
            ),
            "order": "O(b log(b+2)) per phase",
            "route_consequence": (
                "summing this envelope over b comparable to m costs O(m^2 log m), "
                "so it gives no O(m) coefficient and cannot supply or exclude the needed "
                "0.1177979020165907632818384072... per m"
            ),
            "finite_checkpoints": height_checkpoints,
        },
        "verdict": (
            "PROVED an exact common-term recurrence and phase-feasibility congruence; "
            "PROVED the full b=900 gcd factorization and retained p=2399; FINITE complete "
            "factorization through b=900 finds p=2399 as the only phase-feasible odd factor; "
            "PROVED only an O(b log b) eliminant-height bound, which is globally inadequate; "
            "an all-b prime-localization theorem and a positive Route-1 rate bound remain OPEN."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-b", type=int, default=900)
    parser.add_argument("--recurrence-max-b", type=int, default=100)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_b, args.recurrence_max_b)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "factor_scan_sha256": result["finite_factorization_scan"]["stream_sha256"],
                "recurrence_sha256": result["finite_recurrence_crosscheck"]["stream_sha256"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
