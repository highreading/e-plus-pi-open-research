#!/usr/bin/env python3
"""Deterministic exact controls for Item 408.

The all-M endpoint localization, prime-number-theorem asymptotics, and
capacity no-go are proved in the report.  This standard-library checker pins
audited canonical Items 391, 395, 400, 401, and 405.
It verifies the exact age/endpoint equivalence on declared structural grids,
the shortened candidate-interval length, finite cluster/isolated packing,
and the rational coefficient formulas.  The finite prime sets are controls
only: no density claim or actual-gate claim is inferred from them.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = ROOT / "results" / "item408_j1_growing_initial_depth_capacity_threshold_no_go_certificate.json"


DEPENDENCIES = {
    "sources/item391_j1_logarithmic_spacing_resultant_criterion_report.md":
        "304713605fcf33675a882b4f333d60cc35fd36bc6b860353eff36472d4a27564",
    "manifests/item391_j1_logarithmic_spacing_resultant_criterion_manifest.json":
        "07e4a438dbc32e52e67587d7a0fe4886d23e584fd7fae34aafe7f234c334e511",
    "sources/item395_j1_logscale_cluster_radical_height_obstruction_report.md":
        "af0d85607d665f5d6c12c2695a44a89d984abffb008bbd1318978471e79f4487",
    "manifests/item395_j1_logscale_cluster_radical_height_obstruction_manifest.json":
        "3ef54ba9d3caa5af1b76bde52822447e253256c4c0ebb30dd6bb8a6200502cbd",
    "sources/item400_j1_discriminant_energy_sieve_threshold_no_go_report.md":
        "f9dfe5dd6082ec762c0e677760aff5367c1fd869241ed29a4fa50fc78dab124e",
    "manifests/item400_j1_discriminant_energy_sieve_threshold_no_go_manifest.json":
        "ffa52a35f31b98c717050dd1b01dfd2e7b6042838c326dbb8c970a5b2989aca7",
    "sources/item401_j1_crossM_algebraic_transport_no_go_report.md":
        "ae32a79bd5525bae4ca13501aef3cb030f500062214c72b7af077565df482a9a",
    "scripts/item401_j1_crossM_algebraic_transport_no_go_certificate.py":
        "d4d5d90852a1a96c5322f9bbb40b88d913c503dcbefe61a5edaa385f9cd7ab5b",
    "results/item401_j1_crossM_algebraic_transport_no_go_certificate.json":
        "20733cacbb0698d938376b1b82ff19bdae0bceb4666eebe9bf82f3fa833e1090",
    "results/item401_j1_crossM_algebraic_transport_no_go_certificate_replay.json":
        "20733cacbb0698d938376b1b82ff19bdae0bceb4666eebe9bf82f3fa833e1090",
    "results/item401_j1_crossM_algebraic_transport_no_go_ledger_delta.json":
        "f036fa1b12bd942c908bfc47231fa2b58582029c392d60c44fe356e162c57df7",
    "manifests/item401_j1_crossM_algebraic_transport_no_go_manifest.json":
        "6daa3e8c868c7ebd09ede3f1fc450fb8e7906058717c99772592a04c272c89be",
    "results/item401_j1_crossM_algebraic_transport_no_go_hashes.sha256":
        "23b920ae2bc19d7fb78f1e620d22a57084729608e5176aaccfb4f406ea720795",
    "results/item401_j1_crossM_algebraic_transport_no_go_root_audit.json":
        "19adb137729e87410f93d41c63f8b6127063fa12bf5e08db1f79f229353155f8",
    "sources/item405_j1_initial_orbit_phase_capacity_no_go_report.md":
        "e53bab04d62ec910dd2d6b1e6ec90930fe901468c26e2a6cdc405b59b76a222f",
    "scripts/item405_j1_initial_orbit_phase_capacity_no_go_certificate.py":
        "8f417a695b41332c9f1faedb831e8f6537cc093d0c892bf3545f6ff75e7243f1",
    "results/item405_j1_initial_orbit_phase_capacity_no_go_certificate.json":
        "f76e6061a5b9657fbf2840a20d111cf0ba41b7db268e8eef5abe335cfa452b07",
    "manifests/item405_j1_initial_orbit_phase_capacity_no_go_manifest.json":
        "4851391bd6fa7ab7c5b28daad1ee7b2d64c99e7e24d1be067db4307b2bda931a",
    "results/item405_j1_initial_orbit_phase_capacity_no_go_root_audit.json":
        "4e81e7bcf9522c75802f57a56f744c8a8f9690531e727b5f534b1fd74aeb54ca",
}


DECLARED_GRIDS = (
    (180, (0, 1, 3, 7, 19), 5),
    (300, (0, 2, 3, 11, 25), 6),
    (861, (0, 3, 17, 48, 95), 7),
    (1728, (0, 3, 31, 96, 191), 8),
)


COEFFICIENT_CASES = (
    (Fraction(3, 4), Fraction(0, 1)),
    (Fraction(1, 1), Fraction(0, 1)),
    (Fraction(2, 1), Fraction(0, 1)),
    (Fraction(1, 1), Fraction(1, 36)),
    (Fraction(1, 1), Fraction(1, 18)),
    (Fraction(1, 1), Fraction(1, 12)),
    (Fraction(1, 1), Fraction(1, 9)),
)


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


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def frac_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def candidate_primes(M: int) -> list[int]:
    upper = (3 * M - 1) // 2
    answer = []
    for prime in range(5, upper + 1):
        if not is_prime(prime):
            continue
        if 3 * prime < 4 * M + 3 or 2 * prime > 3 * M - 1:
            continue
        h_value = 3 * M - 2 * prime
        s_numerator = 3 * prime - 4 * M - 1
        assert h_value >= 1
        assert s_numerator >= 2 and s_numerator % 2 == 0
        s_value = s_numerator // 2
        assert prime == 4 * h_value + 6 * s_value + 3
        assert M == 3 * h_value + 4 * s_value + 2
        answer.append(prime)
    return answer


def column_start(prime: int) -> int:
    return ceil_div(2 * prime + 1, 3)


def split_by_depth(M: int, depth: int, primes: list[int]) -> tuple[list[int], list[int]]:
    excluded_by_age = [prime for prime in primes if M - column_start(prime) < depth]
    excluded_by_endpoint = [
        prime for prime in primes if 2 * prime > 3 * M - 3 * depth - 1
    ]
    assert excluded_by_age == excluded_by_endpoint
    retained = [prime for prime in primes if prime not in set(excluded_by_age)]
    assert all(M - column_start(prime) >= depth for prime in retained)
    return retained, excluded_by_age


def cluster_partition(primes: list[int], D: int) -> tuple[list[int], list[int]]:
    clustered = []
    isolated = []
    for index, prime in enumerate(primes):
        has_neighbor = (
            (index > 0 and prime - primes[index - 1] <= 2 * D)
            or (index + 1 < len(primes) and primes[index + 1] - prime <= 2 * D)
        )
        (clustered if has_neighbor else isolated).append(prime)
    assert set(clustered).isdisjoint(isolated)
    assert sorted(clustered + isolated) == primes
    assert all(b - a > 2 * D for a, b in zip(isolated, isolated[1:]))
    return clustered, isolated


def digest_integers(values: list[int]) -> str:
    payload = ",".join(str(value) for value in values).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def grid_control(M: int, depths: tuple[int, ...], D: int) -> dict[str, Any]:
    primes = candidate_primes(M)
    rows = []
    for depth in depths:
        retained, excluded = split_by_depth(M, depth, primes)
        threshold = Fraction(3 * M - 3 * depth - 1, 2)
        raw_span = Fraction(M - 9 - 9 * depth, 6)
        span = max(Fraction(0, 1), raw_span)
        clustered, isolated = cluster_partition(retained, D)
        packing_bound = 0 if not retained else 1 + int(span // (2 * D))
        assert len(isolated) <= packing_bound
        rows.append({
            "depth": depth,
            "endpoint_threshold_T": frac_text(threshold),
            "retained_interval_length": frac_text(span),
            "retained_count": len(retained),
            "excluded_count": len(excluded),
            "retained_sha256": digest_integers(retained),
            "excluded_sha256": digest_integers(excluded),
            "clustered_count_at_declared_D": len(clustered),
            "isolated_count_at_declared_D": len(isolated),
            "isolated_packing_bound": packing_bound,
        })
    return {
        "M": M,
        "D": D,
        "candidate_count": len(primes),
        "candidate_sha256": digest_integers(primes),
        "depth_rows": rows,
    }


def retained_mass_coefficient(depth_ratio: Fraction) -> Fraction:
    return max(Fraction(0, 1), Fraction(1, 6) - Fraction(3, 2) * depth_ratio)


def cluster_coefficient(c_value: Fraction, depth_ratio: Fraction) -> Fraction:
    assert c_value > Fraction(1, 2)
    return retained_mass_coefficient(depth_ratio) * (
        Fraction(1, 1) - Fraction(1, 2) / c_value
    )


def coefficient_control(c_value: Fraction, depth_ratio: Fraction) -> dict[str, str]:
    base = cluster_coefficient(c_value, Fraction(0, 1))
    shortened = cluster_coefficient(c_value, depth_ratio)
    expected_base = (2 * c_value - 1) / (12 * c_value)
    assert base == expected_base
    if depth_ratio <= Fraction(1, 9):
        expected_drop = Fraction(3, 2) * depth_ratio * (
            Fraction(1, 1) - Fraction(1, 2) / c_value
        )
        assert base - shortened == expected_drop
    if c_value == 1 and depth_ratio <= Fraction(1, 9):
        assert shortened == Fraction(1, 12) - Fraction(3, 4) * depth_ratio
    return {
        "c": frac_text(c_value),
        "depth_ratio_b": frac_text(depth_ratio),
        "retained_mass_coefficient": frac_text(retained_mass_coefficient(depth_ratio)),
        "item395_admission_coefficient_a_c": frac_text(base),
        "shortened_interval_cluster_lower_coefficient": frac_text(shortened),
        "drop_from_item395_coefficient": frac_text(base - shortened),
    }


def build_certificate() -> dict[str, Any]:
    verify_dependencies()
    grids = [grid_control(M, depths, D) for M, depths, D in DECLARED_GRIDS]
    coefficients = [coefficient_control(c_value, b_value)
                    for c_value, b_value in COEFFICIENT_CASES]
    assert cluster_coefficient(Fraction(1), Fraction(0)) == Fraction(1, 12)
    assert retained_mass_coefficient(Fraction(1, 9)) == 0
    return {
        "schema": "item408-j1-growing-initial-depth-capacity-threshold-no-go-certificate-v1",
        "item": 408,
        "checked_date_beijing": "2026-09-01",
        "classification": "PROVED_SUBLINEAR_INITIAL_DEPTH_ZERO_RATE_AND_LINEAR_DEPTH_THRESHOLD",
        "dependency_hashes": DEPENDENCIES,
        "exact_identities": {
            "column_start": "M_p0=ceil((2p+1)/3)",
            "age_exclusion_endpoint": "M-M_p0<B iff p>(3M-3B-1)/2",
            "retained_interval_length": "max(0,(M-9-9B)/6)",
            "retained_mass_coefficient_for_B_over_M_to_b": "max(0,1/6-3b/2)",
            "cluster_lower_coefficient": "max(0,1/6-3b/2)*(1-1/(2c))",
            "item395_coefficient_at_b_0": "(2c-1)/(12c)",
            "c_1_coefficient": "max(0,1/12-3b/4)",
            "necessary_depth_ratio_for_epsilon_drop": "b>=4c*epsilon/(3*(2c-1))",
        },
        "declared_structural_controls": grids,
        "exact_rational_coefficient_controls": coefficients,
        "strict_labels": {
            "PROVED": [
                "exact localization of the first-B column levels to one upper endpoint interval",
                "every sublinear depth B=o(M) removes only o(M) ambient prime logarithmic mass",
                "the maximal selector allowed by a sublinear initial-strip theorem retains the exact Item395 coefficient",
                "a positive change of linear mass requires linear depth B=Omega(M)",
            ],
            "DECLARED_EXACT_CONTROL_ONLY": [
                "finite prime grids, endpoint splits, and cluster packing checks",
                "no actual gate values or density inference from finite data",
            ],
            "NOT_ACTUAL_ORBIT_CLAIM": [
                "the full-minus-strip selector is an information-class witness only",
                "no recurrence interpolation is promoted to an actual Item401 orbit",
            ],
            "OPEN": [
                "any actual joint-gate exclusion beyond Item405 depth three",
                "actual operator-specific horizontal nonconcentration or cross-prime reciprocity",
                "any strict Route-1 capacity reduction",
            ],
        },
        "ledger": {
            "new_route1_linear_log_rate": 0,
            "new_route1_booking": 0,
            "new_whole_cell_capacity_reduction": 0,
            "retained_fixed_j1_ceiling_per_6M": "1/36",
            "conclusion_about_e_plus_pi": "OPEN",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    certificate = build_certificate()
    payload = json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.replay is not None:
        frozen = args.replay.read_text(encoding="utf-8")
        if frozen != payload:
            raise AssertionError("replay payload differs from frozen certificate")
    args.output.write_text(payload, encoding="utf-8", newline="\n")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
