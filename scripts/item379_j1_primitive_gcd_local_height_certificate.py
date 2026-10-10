#!/usr/bin/env python3
"""Deterministic exact replay for Item 379.

The checker verifies the prime-by-prime local gcd identity, the lcm bound
for the reduced denominators, the elementary Archimedean estimate, and
the actual-selector invisibility of primitive gcd reduction.

Finite controls are predeclared.  There is no prime scan, collision
census, recurrence guessing, or asymptotic extrapolation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item379_j1_primitive_gcd_local_height_certificate.json"

DEPENDENCIES = {
    "sources/item376_j1_terminal_normalized_carrier_recurrence_barrier_report.md":
        "6104750dae85ecbb1fe3b0a0f1a702d7edd3ecbab33098e0f665a6438d49be37",
    "scripts/item376_j1_terminal_normalized_carrier_recurrence_barrier_certificate.py":
        "828b19188cf954b15fc19aa4bbc803da9cbcb62421c20591ea148c5fc5042551",
    "results/item376_j1_terminal_normalized_carrier_recurrence_barrier_certificate.json":
        "d6a367da2b86a0cdbcf6e7f1f284ed98875a27a98bcc4f90efe25f02ee68dadf",
    "results/item376_j1_terminal_normalized_carrier_recurrence_barrier_ledger_delta.json":
        "f6b126b39bacc59fec3cf78e1911884f8b6c319675417743f05e5627b34ba9a3",
    "results/item376_j1_terminal_normalized_carrier_recurrence_barrier_root_audit.json":
        "9f8eacb9ba180e5cd5f9999aa49631998f129c78e15386ee9063a83b20adc489",
    "manifests/item376_j1_terminal_normalized_carrier_recurrence_barrier_manifest.json":
        "b7bba97013ed32ccae2228aff337493bda0478c50dcc49b6be885c901f77a733",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify_dependencies()
ITEM376 = load_module(
    "item379_pinned_item376",
    ROOT / "scripts/item376_j1_terminal_normalized_carrier_recurrence_barrier_certificate.py",
)


def product(values) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def prime_factors(value: int) -> list[int]:
    residue = abs(value)
    factors: list[int] = []
    candidate = 2
    while candidate * candidate <= residue:
        if residue % candidate == 0:
            factors.append(candidate)
            while residue % candidate == 0:
                residue //= candidate
        candidate = 3 if candidate == 2 else candidate + 2
    if residue > 1:
        factors.append(residue)
    return factors


def valuation_integer(value: int, prime: int) -> int:
    if value == 0:
        raise ZeroDivisionError("valuation of zero")
    residue = abs(value)
    answer = 0
    while residue % prime == 0:
        residue //= prime
        answer += 1
    return answer


def valuation_fraction(value: Fraction, prime: int) -> int:
    if value == 0:
        raise ZeroDivisionError("valuation of zero")
    return valuation_integer(value.numerator, prime) - valuation_integer(
        value.denominator, prime
    )


def reverse_terms(
    kernel: list[int], h_value: int, terminal: int, tail_constant: int
) -> list[Fraction]:
    terms = []
    odd_prefix = 1
    denominator_prefix = 1
    for r_value in range(terminal + 1):
        terms.append(
            Fraction(
                ((-1) ** r_value)
                * kernel[2 * r_value]
                * (3**r_value)
                * odd_prefix,
                denominator_prefix,
            )
        )
        if r_value < terminal:
            odd_prefix *= 2 * h_value + 1 + 2 * r_value
            denominator_prefix *= tail_constant - 2 * h_value + 6 * r_value
    return terms


def local_prime_record(
    terms: list[Fraction],
    value: Fraction,
    denominator: int,
    primitive_gcd: int,
    prime: int,
) -> dict[str, int]:
    nonzero_terms = [term for term in terms if term]
    lam = max(max(0, -valuation_fraction(term, prime)) for term in nonzero_terms)
    local_sum = (prime**lam) * value
    local_sum_valuation = valuation_fraction(local_sum, prime)
    reduced_denominator_exponent = max(0, lam - local_sum_valuation)
    actual_reduced_exponent = valuation_integer(value.denominator, prime)
    if reduced_denominator_exponent != actual_reduced_exponent:
        raise AssertionError(
            (prime, lam, local_sum_valuation, reduced_denominator_exponent,
             actual_reduced_exponent)
        )
    gcd_exponent = valuation_integer(denominator, prime) - actual_reduced_exponent
    if gcd_exponent < 0:
        raise AssertionError((prime, gcd_exponent))
    if gcd_exponent != valuation_integer(primitive_gcd, prime):
        raise AssertionError((prime, gcd_exponent, "primitive gcd mismatch"))
    return {
        "prime": prime,
        "lambda": lam,
        "local_sum_valuation": local_sum_valuation,
        "reduced_denominator_exponent": actual_reduced_exponent,
        "clearing_denominator_exponent": valuation_integer(denominator, prime),
        "primitive_gcd_exponent": gcd_exponent,
    }


def progression_count(values: list[int], modulus: int) -> int:
    return sum(1 for value in values if value % modulus == 0)


def carrier_record(h_value: int, family: str) -> dict[str, Any]:
    if family == "x":
        terminal = h_value
        tail_constant = 3
        kernel = ITEM376.ITEM364.ITEM218.kernel_integer(h_value, 1)
    elif family == "u":
        terminal = h_value + 2
        tail_constant = -3
        kernel = ITEM376.ITEM364.ITEM218.kernel_integer(h_value, 4)
    else:
        raise ValueError(family)

    terms = reverse_terms(kernel, h_value, terminal, tail_constant)
    value = sum(terms, Fraction(0))
    numerator, denominator = ITEM376.cleared_pair(
        kernel, h_value, terminal, tail_constant
    )
    if value != Fraction(numerator, denominator):
        raise AssertionError((h_value, family, "reverse value"))
    primitive = ITEM376.primitive_record(numerator, denominator)
    if value != Fraction(
        primitive["primitive_numerator"], primitive["primitive_denominator"]
    ):
        raise AssertionError((h_value, family, "primitive value"))

    denominator_factors = [
        tail_constant - 2 * h_value + 6 * index for index in range(terminal)
    ]
    odd_factors = [2 * h_value + 1 + 2 * index for index in range(terminal)]
    if any(value == 0 for value in denominator_factors):
        raise AssertionError((h_value, family, "zero factor"))
    if len(set(map(abs, denominator_factors))) != terminal:
        raise AssertionError((h_value, family, "absolute factors not distinct"))

    for r_value in range(terminal + 1):
        if product(abs(value) for value in denominator_factors[:r_value]) < math.factorial(
            r_value
        ):
            raise AssertionError((h_value, family, r_value, "factorial bound"))

    factor_primes = prime_factors(denominator)
    local_records = [
        local_prime_record(terms, value, denominator, primitive["gcd"], prime)
        for prime in factor_primes
    ]
    if 2 in factor_primes or 3 in factor_primes:
        raise AssertionError((h_value, family, "2 or 3 in denominator"))

    cutoff = 4 * h_value + 3
    lcm_value = 1
    for integer in range(1, cutoff + 1):
        lcm_value = math.lcm(lcm_value, integer)
    if lcm_value % primitive["primitive_denominator"]:
        raise AssertionError((h_value, family, "lcm bound"))
    for local in local_records:
        prime = local["prime"]
        exponent_bound = 0
        power = prime
        while power <= cutoff:
            exponent_bound += 1
            power *= prime
        if local["lambda"] > exponent_bound:
            raise AssertionError((h_value, family, prime, "lambda bound"))

        # The proof compares two invertible-step progressions at every q^a.
        power = prime
        while power <= cutoff:
            for r_value in range(terminal + 1):
                denominator_count = progression_count(
                    denominator_factors[:r_value], power
                )
                numerator_count = progression_count(odd_factors[:r_value], power)
                if abs(denominator_count - numerator_count) > 1:
                    raise AssertionError(
                        (h_value, family, prime, power, r_value, "count defect")
                    )
            power *= prime

    kernel_l1_bound = 2 ** (2 * h_value + (1 if family == "x" else 4))
    if max(map(abs, kernel)) > kernel_l1_bound:
        raise AssertionError((h_value, family, "kernel bound"))
    scale = 3 * cutoff
    exponential_majorant = sum(
        Fraction(scale**r_value, math.factorial(r_value))
        for r_value in range(terminal + 1)
    )
    if abs(value) > kernel_l1_bound * exponential_majorant:
        raise AssertionError((h_value, family, "Archimedean bound"))

    gcd_value = primitive["gcd"]
    if math.gcd(gcd_value, 6) != 1:
        raise AssertionError((h_value, family, "gcd is not a 6-unit"))
    if factor_primes and max(factor_primes) > cutoff:
        raise AssertionError((h_value, family, "prime support"))

    return {
        "h": h_value,
        "family": family,
        "primitive_numerator_digits": len(str(abs(primitive["primitive_numerator"]))),
        "primitive_denominator": primitive["primitive_denominator"],
        "primitive_gcd": gcd_value,
        "local_prime_records": local_records,
        "lcm_divisibility": True,
        "absolute_denominator_factors_distinct": True,
        "archimedean_majorant_verified": True,
    }


def local_replay() -> dict[str, Any]:
    controls = (1, 2, 4, 5, 7, 8, 10, 11, 13, 14)
    rows = []
    for h_value in controls:
        if h_value % 3 == 0:
            raise AssertionError((h_value, "composite ray"))
        rows.append(carrier_record(h_value, "x"))
        rows.append(carrier_record(h_value, "u"))
    return {
        "classification": "EXACT PREDECLARED LOCAL CONTROLS; NO PRIME SCAN",
        "rows": rows,
        "prime_by_prime_identity": (
            "lambda_q=max_r max(0,-v_q(rho_r)); Z_q=q^lambda_q sum rho_r; "
            "v_q(E)=max(0,lambda_q-v_q(Z_q)); v_q(g)=v_q(D)-v_q(E)"
        ),
        "uniform_local_bound": (
            "lambda_q<=floor(log_q(4h+3)), hence E_x and E_u divide "
            "lcm(1,...,4h+3)"
        ),
        "uniform_height": (
            "|N_x|<=lcm(1,...,4h+3)*2^(2h+1)*exp(12h+9), and the "
            "same bound with 2^(2h+4) holds for |N_u|; therefore log|N|=O(h)"
        ),
    }


def actual_selector_replay() -> dict[str, Any]:
    controls = ((1, 1, 13), (2, 1, 17), (4, 4, 43), (8, 2, 47))
    rows = []
    for h_value, s_value, prime in controls:
        if prime != 4 * h_value + 6 * s_value + 3:
            raise AssertionError((h_value, s_value, prime, "tie"))
        if not ITEM376.ITEM364.ITEM218.is_prime(prime):
            raise AssertionError((prime, "not prime"))
        if prime < 4 * h_value + 9:
            raise AssertionError((prime, h_value, "selector cutoff"))

        row: dict[str, Any] = {"h": h_value, "s": s_value, "p": prime}
        for family, terminal, tail_constant, power in (
            ("x", h_value, 3, 1),
            ("u", h_value + 2, -3, 4),
        ):
            kernel = ITEM376.ITEM364.ITEM218.kernel_integer(h_value, power)
            numerator, denominator = ITEM376.cleared_pair(
                kernel, h_value, terminal, tail_constant
            )
            primitive = ITEM376.primitive_record(numerator, denominator)
            if primitive["gcd"] % prime == 0:
                raise AssertionError((prime, h_value, family, "gcd visible"))
            if (numerator % prime == 0) != (
                primitive["primitive_numerator"] % prime == 0
            ):
                raise AssertionError((prime, h_value, family, "carrier changed"))
            row[f"{family}_gcd_p_unit"] = True
        rows.append(row)
    return {
        "classification": "EXACT PREDECLARED ACTUAL-ROW CONTROLS; NO SCAN",
        "rows": rows,
        "global_theorem": (
            "every prime divisor of g_x or g_u is at most 4h+3, whereas every "
            "actual selected prime is at least 4h+9; therefore p|N_x iff p|A_x "
            "and p|N_u iff p|A_u"
        ),
    }


def capacity_replay() -> dict[str, Any]:
    return {
        "shared_full_fixed_j1_ceiling_per_6M": "1/36",
        "individual_primitive_height": "O(h)",
        "aggregate_over_O(M)_rows": "O(M^2), not O(M) and not o(M)",
        "gcd_selector_effect": "none: primitive reduction changes no actual selected-prime event",
        "new_booking": 0,
        "new_capacity_reduction": 0,
    }


def build_result() -> dict[str, Any]:
    return {
        "item": 379,
        "schema": "item379-j1-primitive-gcd-local-height-v1",
        "classification": "PROVED_LOCAL_GCD_FORMULA_LCM_HEIGHT_AND_SELECTOR_INVISIBILITY",
        "dependencies": DEPENDENCIES,
        "dependency_hashes_verified": True,
        "local_replay": local_replay(),
        "actual_selector_replay": actual_selector_replay(),
        "capacity_replay": capacity_replay(),
        "strict_labels": {
            "proved": [
                "exact prime-by-prime local gcd identity",
                "E_x and E_u divide lcm(1,...,4h+3)",
                "uniform exponential height for N_x and N_u",
                "primitive gcd reduction is invisible to every actual selected prime",
                "zero booking and zero capacity reduction",
            ],
            "finite_only": [
                "ten declared h controls and four declared actual rows",
                "no prime scan, collision census, recurrence guess, or extrapolation",
            ],
            "open": [
                "uniform evaluation of the local residue Z_q for q<=4h+3",
                "a closed product formula for the full primitive gcd",
                "a recurrence for the primitive reduced numerators",
                "selector-aware weighted zero density for the actual paired gates",
            ],
        },
        "smallest_missing_local_lemma": (
            "evaluate or uniformly bound v_q(Z_q), the cancellation among the "
            "least-q-adic reverse-sum terms, for primes q<=4h+3"
        ),
        "scope_warning": (
            "The O(h) individual height sums to O(M^2) over O(M) rows and gives "
            "no weighted capacity reduction.  Local gcd primes are below the actual "
            "selector and cannot decide selected-prime divisibility."
        ),
        "verdict": (
            "The primitive denominators and numerators have uniform exponential "
            "height, but primitive gcd reduction removes only sub-selector primes. "
            "It is therefore arithmetically invisible to the actual collision set."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "classification": result["classification"],
                "new_booking": result["capacity_replay"]["new_booking"],
                "new_capacity_reduction": result["capacity_replay"][
                    "new_capacity_reduction"
                ],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
