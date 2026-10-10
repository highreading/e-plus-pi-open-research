#!/usr/bin/env python3
"""Deterministic certificate for Item 385.

The checker replays the exact fixed-M lattice, the complete intersection
with step-6 rays, and the rank-two full-mass comparison module.  Its prime
pair counts are explicitly finite diagnostics.  The asymptotic zero-rate
theorem uses the classical Brun--Selberg upper-bound sieve as stated in the
report; it is not inferred from these counts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item385_j2_bounded_window_aggregate_no_go_certificate.json"

DEPENDENCIES = {
    "work/item318_j2_actual_period_plucker_report.md":
        "e89f4892b3c2b9b999321de0ec6973547903b755f07b0d34be7f0da634ecd4db",
    "work/item319_j2_third_minor_elimination_report.md":
        "51b2505f71257f905b4b979f90eb74af24e9c3f2f29c1dd9ee57bd737e5581e1",
    "work/item322_j2_fixedM_period_transfer_report.md":
        "7941d4102861a96145cc38267463da1a78cf7c2d9dec384857ef5c16a3f0b875",
    "work/item326_j1_selected_factor_step12_no_go_report.md":
        "12f42dff3d52ab5d257eac675d9cff6888925568d29ea4894cad5e37c0c31b37",
    "work/item331_j2_global_cartier_concentration_report.md":
        "b721b9469b500a8b8fb5f6c0c0702f92015198264a7c6f931acaabd82796ee08",
    "work/item334_j2_coupled_cartier_carrier_report.md":
        "a9a1b42652e5157b850014758c321ffd8a5734e4f9ea3586510ae0549822357c",
    "work/item336_j2_carrier_resultant_obstruction_report.md":
        "761f09e999c0f76139e036f2f4db03743b363087e04f9ed661fe65229cb0b4c2",
    "work/item338_j2_secondary_cartier_saturation_report.md":
        "14aa87b718b4bb83dd3e5371412fd231829f809b853d1a52eabba6181650ac33",
    "work/item341_j2_diagonal_affine_state_report.md":
        "42f6ccd326e385f8034abe322756517a30a93d7468b3e6f85cbca3dba8080cb4",
    "work/item344_j2_frobenius_cutoff_obstruction_report.md":
        "1671dec30de80c047c52b6b4bf13157025ea631869f5ccacc73169002ec287a9",
    "work/item347_j2_chosen_prime_kummer_conductor_obstruction_report.md":
        "7845d01648f4860dee7cee0c12b5711693183015c99e25e923a9e49f316f5eea",
    "work/item349_j2_degenerate_triple_minor_carrier_report.md":
        "aec5a8bc6dd8996a3578e4cbc7975afad6247ddb32d03f6deca72b97af86b50d",
    "work/item352_j2_nonsemisimple_transition_no_go_report.md":
        "c60e1ba7771314c77b3fbe5d06f9c13c51a8c7e4d15f2589298641ff0f38e794",
    "work/item355_j2_target_residual_large_sieve_obstruction_report.md":
        "ea2f5f43a14a411849bc310409939891bfb496b681b028c20fcb3b990dd3377b",
    "work/item359_j2_fixedM_cross_prime_coefficient_barrier_report.md":
        "8fc3e4a16c71aeb50f7516e5e81572ea3d7265f30104707fc988945155759a77",
    "work/item361_j2_matched_cartier_norm_collapse_report.md":
        "0ad329d64d00853fd1b8adca1c982790bd293f01bdc1ea356ad3858374683af8",
    "work/item382_j1_explicit_operator_alignment_barrier_report.md":
        "8d8c74889a0cf066dea80db23adc117e8f927ff9a4eea4ca75321c18d3a6ff7b",
}


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


def prime_rows(M: int) -> list[tuple[int, int, int]]:
    lower = ceil_div(4 * M + 3, 5)
    upper = (6 * M - 1) // 7
    rows: list[tuple[int, int, int]] = []
    for prime in range(max(11, lower), upper + 1):
        if not is_prime(prime):
            continue
        r = 6 * M - 7 * prime
        s_numerator = 5 * prime - 4 * M - 1
        if s_numerator % 2:
            raise AssertionError((M, prime, "nonintegral s"))
        s = s_numerator // 2
        if r < 1 or s < 1 or r % 2 != 1 or r % 3 == 0:
            raise AssertionError((M, prime, r, s, "invalid actual row"))
        if prime != 2 * r + 6 * s + 3:
            raise AssertionError((M, prime, r, s, "tied phase"))
        if 2 * M != 5 * r + 14 * s + 7:
            raise AssertionError((M, prime, r, s, "fixed M"))
        rows.append((prime, r, s))
    return rows


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def alignment_replay() -> dict[str, Any]:
    equations = 0
    solutions: list[tuple[int, int, int]] = []
    for j in range(-24, 25):
        for d in range(-24, 25):
            aligned = 6 * j == -14 * d
            classified = j % 7 == 0 and d == -3 * (j // 7)
            if aligned != classified:
                raise AssertionError((j, d, aligned, classified))
            equations += 1
            if aligned:
                solutions.append((j, d, j // 7))

    nonzero_small = [row for row in solutions if row[0] != 0 and abs(row[0]) < 7]
    if nonzero_small:
        raise AssertionError(nonzero_small)

    expected = [(-21, 9, -3), (-14, 6, -2), (-7, 3, -1),
                (0, 0, 0), (7, -3, 1), (14, -6, 2), (21, -9, 3)]
    if solutions != expected:
        raise AssertionError((solutions, expected))

    return {
        "classification": "PROVED SYMBOLIC INTEGER IDENTITY REPLAY",
        "box": {"j_min": -24, "j_max": 24, "d_min": -24, "d_max": 24},
        "equations_checked": equations,
        "solutions": [list(row) for row in solutions],
        "first_positive_return": {"j": 7, "d": -3, "delta_r": 42,
                                  "delta_s": -15, "delta_p": -6},
        "no_nonzero_return_for_abs_j_below_7": True,
    }


def row_grid_replay() -> dict[str, Any]:
    declared_M = [80, 137, 250, 499, 1000]
    records: list[tuple[int, ...]] = []
    shifts_checked = 0
    for M in declared_M:
        for prime, r, s in prime_rows(M):
            for d in range(-6, 7):
                shifted_prime = prime + 2 * d
                shifted_r = r - 14 * d
                shifted_s = s + 5 * d
                if shifted_r < 1 or shifted_s < 1:
                    continue
                if shifted_prime != 2 * shifted_r + 6 * shifted_s + 3:
                    raise AssertionError((M, prime, r, s, d, "shifted phase"))
                if 2 * M != 5 * shifted_r + 14 * shifted_s + 7:
                    raise AssertionError((M, prime, r, s, d, "shifted M"))
                same_ray = shifted_r % 6 == r % 6
                if same_ray != (d % 3 == 0):
                    raise AssertionError((M, prime, r, s, d, same_ray))
                shifts_checked += 1

            carrier = 6 * M - r
            if carrier != 7 * prime:
                raise AssertionError((M, prime, r, carrier))
            saturated = carrier
            while saturated % 7 == 0:
                saturated //= 7
            if saturated != prime:
                raise AssertionError((M, prime, r, carrier, saturated))

            # Full-grid and same-ray comparison-module translations.
            if 6 * M - (r - 14) != carrier + 14:
                raise AssertionError((M, prime, r, "full-grid module"))
            if 6 * M - (r + 42) != carrier - 42:
                raise AssertionError((M, prime, r, "same-ray module"))
            records.append((M, prime, r, s, carrier, saturated))

    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "declared_M": declared_M,
        "prime_rows": len(records),
        "row_shifts_checked": shifts_checked,
        "comparison_module": "V_M(r+u)=[[1,0],[-u,1]] V_M(r)",
        "raw_carrier": "6M-r=7p",
        "fixed_7_saturated_carrier": "p",
        "row_digest_sha256": digest_rows(records),
    }


def prime_pair_diagnostics() -> dict[str, Any]:
    declared_M = [1000, 2000, 5000, 10000, 20000]
    offsets = [-12, -6, -4, -2, 2, 4, 6, 12]
    records: list[dict[str, Any]] = []
    stream: list[tuple[Any, ...]] = []
    for M in declared_M:
        rows = prime_rows(M)
        primes = [row[0] for row in rows]
        prime_set = set(primes)
        paired = [prime for prime in primes
                  if any(prime + offset in prime_set for offset in offsets)]
        isolated = [prime for prime in primes if prime not in set(paired)]
        raw_weight = sum(math.log(prime) for prime in primes)
        paired_weight = sum(math.log(prime) for prime in paired)
        isolated_weight = sum(math.log(prime) for prime in isolated)
        if abs(raw_weight - paired_weight - isolated_weight) > 1e-9:
            raise AssertionError((M, raw_weight, paired_weight, isolated_weight))
        # The comparison carrier selects every prime exactly.
        comparison_weight = sum(math.log((7 * prime) // 7) for prime in primes)
        if abs(comparison_weight - raw_weight) > 1e-9:
            raise AssertionError((M, comparison_weight, raw_weight))
        row = {
            "M": M,
            "prime_rows": len(primes),
            "paired_rows": len(paired),
            "isolated_rows": len(isolated),
            "raw_log_weight": raw_weight,
            "paired_log_weight": paired_weight,
            "isolated_log_weight": isolated_weight,
            "raw_weight_over_M": raw_weight / M,
            "paired_weight_over_M": paired_weight / M,
            "isolated_weight_over_M": isolated_weight / M,
            "comparison_weight_equals_raw": True,
        }
        records.append(row)
        stream.append((M, len(primes), len(paired), len(isolated),
                       f"{raw_weight:.12f}", f"{paired_weight:.12f}",
                       f"{isolated_weight:.12f}"))

    return {
        "classification": (
            "EXACT FINITE DIAGNOSTIC ONLY - ASYMPTOTIC PRIME-PAIR THEOREM "
            "USES BRUN--SELBERG, NOT THESE COUNTS"
        ),
        "offsets": offsets,
        "raw_asymptotic_constant": "2/35",
        "rows": records,
        "diagnostic_digest_sha256": digest_rows(stream),
    }


def build_result(skip_dependency_check: bool) -> dict[str, Any]:
    if not skip_dependency_check:
        verify_dependencies()
    return {
        "schema": "item385-j2-bounded-window-aggregate-no-go-v1",
        "classification": "PROVED_GLOBAL_BOUNDED_WINDOW_PROPAGATION_NO_GO",
        "dependency_hashes_verified": not skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "fixed_M": "r=6M-7p; s=(5p-4M-1)/2",
            "full_grid": "(p,r,s)->(p+2d,r-14d,s+5d)",
            "alignment": "6j=-14d iff j=7k,d=-3k",
            "same_ray_return": "(r,s,p)->(r+42k,s-15k,p-6k)",
            "bounded_pair_mass": "for fixed finite H, W_pair(M;H)=O_H(M/log M)=o(M)",
            "isolated_mass": "(2/35)M+o(M)",
            "comparison_module": "V_M(r)=(1,6M-r)^T and V_M(r+u)=[[1,0],[-u,1]]V_M(r)",
            "comparison_carrier": "(6M-r)/7=p on the exact selector",
        },
        "alignment_replay": alignment_replay(),
        "row_grid_replay": row_grid_replay(),
        "prime_pair_diagnostics": prime_pair_diagnostics(),
        "capacity": {
            "raw_ordinary_j2_chebyshev_mass": "(2/35)M+o(M)",
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "new_capacity_reduction": 0,
            "new_booking": 0,
            "chart_rule": "degenerate and nondegenerate charts partition one raw interval",
        },
        "closed_method_class": [
            "every fixed bounded-offset cross-row propagation requiring two actual prime rows",
            "every fixed-order same-ray recurrence used only through a second selected prime row",
            "finite mixtures of such transfers across the two rays or two connection charts",
            "translation/recurrence/height/pairwise-gcd metadata without a cross-characteristic reciprocity",
        ],
        "open": [
            "W_nd(M)+W_deg(M)=o(M) or any strict constant reduction",
            "one-row matched-modulus average gcd or factor localization for the actual aggregate carrier",
            "a reciprocity theorem forcing every collision into a second actual prime row",
            "growing-window propagation with quantitative offset control",
        ],
        "scope_warning": (
            "The comparison module is not the actual carrier.  It proves only that the listed structural "
            "metadata cannot imply matched-modulus sparsity.  Finite prime-pair counts are diagnostic only."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / RESULT_NAME)
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(args.skip_dependency_check)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

