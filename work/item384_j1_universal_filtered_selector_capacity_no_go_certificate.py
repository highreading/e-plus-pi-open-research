#!/usr/bin/env python3
"""Exact replay for Item 384.

The checker verifies the all-subset CRT implementation on declared fixed-M
controls, the actual candidate-row bijection, selector regularity for the
two fixed logarithmic poles, and formal truncations of the rational
horizontal connection.  The all-M/all-subset theorem is proved directly by
CRT in the report; the finite controls are not distribution evidence.
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
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item384_j1_universal_filtered_selector_capacity_no_go_certificate.json"

DEPENDENCIES = {
    "sources/item360_j1_full_gate_transverse_period_report.md":
        "4468412fb8631924952dc7f70fc4e75433a7524954b89525de508e55feefc8c4",
    "sources/item363_j1_joint_gate_crt_elimination_no_go_report.md":
        "377ed30c0c6be630c124ccd3050d37176264c659d23a502453a9aaa34ff132ee",
    "sources/item374_j1_filtered_hasse_extension_realization_report.md":
        "ac04f52132e3355692b1744d625f765dd6b0d1e74f90b123ebd599c135b009d2",
    "sources/item383_j1_frobenius_lift_gauge_invariance_report.md":
        "840e76e85c1a8ebbc8fe3c1b21432c91f7745b2ea18d3f6b51d6612caee7c066",
    "results/item363_j1_joint_gate_crt_elimination_no_go_certificate.json":
        "621171b99b54e75ecba2fb58e000a05f0e0b9e8e3dfd20cb768a3b0d3baf2875",
    "results/item374_j1_filtered_hasse_extension_realization_certificate.json":
        "609f378221a2aafa823947dd967fe0c626df3c74ff726681e406d9b1d4a4fcaf",
    "results/item383_j1_frobenius_lift_gauge_invariance_certificate.json":
        "1c72215e36bd1bb1d24f0e86e2941cc29a5d32f6ff434f22d7c598be3507a80f",
    "manifests/item363_j1_joint_gate_crt_elimination_no_go_manifest.json":
        "46aa9a81d3b92cd5e7e055d9280f32e0e5ca32b91dfd68d95cbc9fdaa26a464a",
    "manifests/item374_j1_filtered_hasse_extension_realization_manifest.json":
        "5963968673fdb77e53ab4acdce5c1eb5e323491c79ef27a45f5f6ee39d73fcd5",
    "manifests/item383_j1_frobenius_lift_gauge_invariance_manifest.json":
        "b1faa6cd0843bc49d803a4016361e8bb54d569785d2d3d33c8df2ea514757926",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file():
            raise AssertionError(("missing dependency", relative))
        actual = sha256(path)
        if actual != expected:
            raise AssertionError(("dependency mismatch", relative, expected, actual))


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def candidate_primes(m_value: int) -> list[int]:
    return [
        prime
        for prime in range(2, (3 * m_value - 1) // 2 + 1)
        if is_prime(prime)
        and 3 * prime >= 4 * m_value + 3
        and 2 * prime <= 3 * m_value - 1
    ]


def actual_row(m_value: int, prime: int) -> tuple[int, int]:
    h_value = 3 * m_value - 2 * prime
    numerator = 3 * prime - 4 * m_value - 1
    if numerator % 2:
        raise AssertionError(("nonintegral s", m_value, prime))
    s_value = numerator // 2
    if h_value < 1 or s_value < 1:
        raise AssertionError(("nonpositive actual row", m_value, prime, h_value, s_value))
    if prime != 4 * h_value + 6 * s_value + 3:
        raise AssertionError(("prime identity", m_value, prime, h_value, s_value))
    if m_value != 3 * h_value + 4 * s_value + 2:
        raise AssertionError(("M identity", m_value, prime, h_value, s_value))
    return h_value, s_value


def crt_zero_one(primes: list[int], mask: int) -> tuple[int, int]:
    product = math.prod(primes)
    if not primes:
        return 0, 1
    selector = 0
    for index, prime in enumerate(primes):
        residue = 0 if (mask >> index) & 1 else 1
        cofactor = product // prime
        selector += residue * cofactor * pow(cofactor, -1, prime)
    return selector % product, product


def subset_controls() -> list[dict[str, Any]]:
    declared_m = [9, 34, 76, 120, 180]
    expected_counts = {9: 1, 34: 1, 76: 4, 120: 4, 180: 5}
    output: list[dict[str, Any]] = []
    for m_value in declared_m:
        primes = candidate_primes(m_value)
        if len(primes) != expected_counts[m_value]:
            raise AssertionError((m_value, primes))
        rows = [actual_row(m_value, prime) for prime in primes]
        digest = hashlib.sha256()
        subset_count = 1 << len(primes)
        for mask in range(subset_count):
            selector, product = crt_zero_one(primes, mask)
            shifted_selector = selector + product
            expected_radical = math.prod(
                prime for index, prime in enumerate(primes) if (mask >> index) & 1
            )
            actual_radical = math.gcd(product, shifted_selector, shifted_selector)
            if actual_radical != expected_radical:
                raise AssertionError(
                    (m_value, mask, shifted_selector, expected_radical, actual_radical)
                )
            if not (0 <= selector < product):
                raise AssertionError(("least representative", m_value, mask, selector))
            if not (product <= shifted_selector < 2 * product):
                raise AssertionError(
                    ("nonzero shifted representative", m_value, mask, shifted_selector)
                )
            for index, prime in enumerate(primes):
                expected_residue = 0 if (mask >> index) & 1 else 1
                if shifted_selector % prime != expected_residue:
                    raise AssertionError(("CRT residue", m_value, mask, prime))
                # lambda=2 has pole at q=1/2.  Both selector residues are regular.
                if (1 - 2 * expected_residue) % prime == 0:
                    raise AssertionError(("selector meets pole", m_value, mask, prime))
            digest.update(
                f"{m_value}|{mask}|{selector}|{shifted_selector}|{actual_radical}\n".encode("ascii")
            )
        empty_selector, product = crt_zero_one(primes, 0)
        full_selector, _ = crt_zero_one(primes, subset_count - 1)
        empty_shifted = empty_selector + product
        full_shifted = full_selector + product
        if empty_selector != 1 or math.gcd(product, empty_shifted) != 1:
            raise AssertionError(("empty selector", m_value, empty_selector))
        if full_selector != 0 or math.gcd(product, full_shifted) != product:
            raise AssertionError(("full selector", m_value, full_selector))
        output.append(
            {
                "classification": "DECLARED FIXED-M ALL-SUBSET CRT CONTROL; NOT DISTRIBUTION EVIDENCE",
                "M": m_value,
                "candidate_primes": primes,
                "actual_rows_h_s": [list(row) for row in rows],
                "subset_count": subset_count,
                "product": product,
                "empty_selector": empty_selector,
                "full_selector": full_selector,
                "empty_shifted_selector": empty_shifted,
                "full_shifted_selector": full_shifted,
                "all_shifted_selectors_nonzero_below_2P": True,
                "all_subset_digest_sha256": digest.hexdigest(),
                "all_radical_identities_verified": True,
                "all_selector_points_avoid_fixed_poles": True,
            }
        )
    return output


def add(left: list[Fraction], right: list[Fraction], order: int) -> list[Fraction]:
    return [
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(order + 1)
    ]


def multiply(left: list[Fraction], right: list[Fraction], order: int) -> list[Fraction]:
    output = [Fraction(0) for _ in range(order + 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            if i + j <= order:
                output[i + j] += left_value * right_value
    return output


def inverse_series(series: list[Fraction], order: int) -> list[Fraction]:
    if not series or series[0] == 0:
        raise ZeroDivisionError("series constant term")
    output = [Fraction(0) for _ in range(order + 1)]
    output[0] = 1 / series[0]
    for degree in range(1, order + 1):
        output[degree] = -sum(
            series[index] * output[degree - index]
            for index in range(1, min(degree, len(series) - 1) + 1)
        ) / series[0]
    return output


def derivative(series: list[Fraction], order: int) -> list[Fraction]:
    return [
        Fraction(index + 1) * series[index + 1]
        if index + 1 < len(series)
        else Fraction(0)
        for index in range(order + 1)
    ]


def formal_connection_control(prime: int, order: int = 12) -> dict[str, Any]:
    # One extra coefficient is retained before differentiation.
    work_order = order + 1
    binomial = [
        Fraction(math.comb(prime, degree) * ((-2) ** degree))
        for degree in range(min(prime, work_order) + 1)
    ]
    exponential = [
        Fraction((-2 * prime) ** degree, math.factorial(degree))
        for degree in range(work_order + 1)
    ]
    product = multiply(binomial, exponential, work_order)
    phi = [Fraction(0) for _ in range(work_order + 1)]
    phi[0] = Fraction(1, 2) * (1 - product[0])
    for degree in range(1, work_order + 1):
        phi[degree] = -product[degree] / 2

    one_minus_two_phi = [-2 * coefficient for coefficient in phi]
    one_minus_two_phi[0] += 1
    if one_minus_two_phi != product:
        raise AssertionError(("defining lift identity", prime))

    denominator = [prime * coefficient for coefficient in one_minus_two_phi]
    lhs = multiply(
        derivative(phi, order), inverse_series(denominator, order), order
    )
    right = [Fraction(2)] + [Fraction(2 ** degree) for degree in range(1, order + 1)]
    # 1/(1-2q)+1 has constant 2 and degree-d coefficient 2^d for d>=1.
    if lhs != right:
        raise AssertionError(("horizontal logarithmic identity", prime, lhs, right))

    # The lift is congruent to q^p modulo p in every retained integral
    # coefficient.  For p>order, the truncated reduction is zero, as is q^p.
    for degree, coefficient in enumerate(phi):
        if coefficient.denominator % prime == 0:
            raise AssertionError(("non-p-adic-integral lift coefficient", prime, degree, coefficient))
        expected = 1 if degree == prime else 0
        residue = (
            coefficient.numerator
            * pow(coefficient.denominator, -1, prime)
        ) % prime
        if residue != expected:
            raise AssertionError(("Frobenius reduction", prime, degree, coefficient))

    digest = hashlib.sha256(
        "|".join(str(value) for value in phi).encode("ascii")
    ).hexdigest()
    return {
        "classification": "DECLARED EXACT FORMAL-SERIES CONTROL; NOT PRIME-DISTRIBUTION EVIDENCE",
        "prime": prime,
        "lambda": 2,
        "verified_through_degree": order,
        "lift_coefficients_p_adically_integral": True,
        "lift_reduces_to_absolute_Frobenius": True,
        "one_minus_2Phi_identity": True,
        "horizontal_identity": "dPhi/[p(1-2Phi)]=dq/(1-2q)+dq",
        "phi_truncation_sha256": digest,
    }


def build_certificate() -> dict[str, Any]:
    verify_dependencies()
    return {
        "schema": "item384-j1-universal-filtered-selector-capacity-no-go-certificate-v1",
        "item": 384,
        "date": "2026-09-01",
        "dependency_hashes_verified": True,
        "all_family_theorem": {
            "candidate_set": "P_M={p prime:(4M+3)/3 <= p <= (3M-1)/2}",
            "actual_row": "h=3M-2p, s=(3p-4M-1)/2",
            "CRT_selector": "least Z is 0 mod p on S and 1 mod p off S; shifted Z_tilde=Z+P_M is nonzero below 2P_M with the same residues",
            "exact_radical": "gcd(P_M,Z_tilde,Z_tilde)=product_(p in S) p",
            "filtered_family": "E(q1) direct_sum E(q2), A_q=[[p,0],[pq,1]], Fil^1=<e1>",
            "joint_Hasse_divisor": "q1=q2=0, codimension 2",
            "fixed_finite_codimension_generalization": "direct sum of k copies has rank 2k, filtration rank k, determinant p^k, k pole components, and codimension-k joint divisor; the diagonal CRT selector realizes every subset",
            "connection": "omega_i=dq_i/(1-2q_i), two fixed logarithmic pole components",
            "selector_regularity": "q_i in {0,1}, hence 1-2q_i in {1,-1}",
            "sharp_capacity": "sup information-class joint-zero mass=log P_M=M/6+o(M)",
        },
        "proved_scope": {
            "information_class_closed": "rowwise bounded-rank/fixed-Hodge/codimension-two/flat/bounded-pole/no-splitting package plus raw-scale CRT height",
            "actual_selector_arbitrary_claimed": False,
            "actual_weighted_bound_claimed": False,
            "compatible_system_claimed": False,
            "collision_scan_performed": False,
            "finite_to_asymptotic_inference": False,
        },
        "subset_controls": subset_controls(),
        "formal_connection_controls": [
            formal_connection_control(13),
            formal_connection_control(17),
        ],
        "capacity": {
            "raw_log_mass": "M/6+o(M)",
            "raw_ceiling_per_6M": "1/36",
            "information_class_full_capacity_attained": True,
            "actual_W_H_T_bound_proved": False,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
            "retained_fixed_j1_ceiling_per_6M": "1/36",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    certificate = build_certificate()
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
