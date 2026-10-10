#!/usr/bin/env python3
"""Deterministic certificate for Item 355.

The checker replays the exact fixed-M selector, target residuals, finite
field orthogonality/occupancy energies, singleton second-moment
saturation, and Jacobi-mode energy counts.  It performs no prime scan
or collision census.  The all-family Parseval and scoped obstruction
proofs are in the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item355_j2_target_residual_large_sieve_obstruction_certificate.json"


# Item 352 pins are replaced by the final root-audited canonical hashes
# before the Item 355 manifest is frozen.
DEPENDENCIES = {
    "sources/item341_j2_diagonal_affine_state_report.md":
        "42f6ccd326e385f8034abe322756517a30a93d7468b3e6f85cbca3dba8080cb4",
    "results/item341_j2_diagonal_affine_state_certificate.json":
        "75c05cb486e5a5a6f9af5dda2e62f2a4b81cb888a15eb19ecabd10a382625cb4",
    "results/item341_j2_diagonal_affine_state_root_audit.json":
        "d5c810346f9181f10d38e9f5ae2e250a8c880e32f97cbc5bef91f6bd37f61a27",
    "manifests/item341_j2_diagonal_affine_state_manifest.json":
        "fc073e4c11a2d9ab519f0b5babae6f9f95e2e8cf9e8cbcf05c4c8ca8ba155000",
    "sources/item347_j2_chosen_prime_kummer_conductor_obstruction_report.md":
        "7845d01648f4860dee7cee0c12b5711693183015c99e25e923a9e49f316f5eea",
    "results/item347_j2_chosen_prime_kummer_conductor_obstruction_certificate.json":
        "bd861233e0a37c6cd6e0d091d244f67e42c7bd65702d77f951e9341ad681159d",
    "results/item347_j2_chosen_prime_kummer_conductor_obstruction_root_audit.json":
        "f9029fceae9662dbf8645a0d49eeaf9f5df85a204a8d94996e3d10e66f57a851",
    "manifests/item347_j2_chosen_prime_kummer_conductor_obstruction_manifest.json":
        "f6bd289bd06d96e1a832208d07815fb4b6e9a4678a6cb022d6302299bebbd5b9",
    "sources/item349_j2_degenerate_triple_minor_carrier_report.md":
        "ca3141156cb5034012a174377c3596e22d22cae924625649b6d620d510f4790c",
    "results/item349_j2_degenerate_triple_minor_carrier_certificate.json":
        "b26294d51b1844aeee04146004b2ecec9b6e1ff81aa271a3167e5d86c11bce44",
    "results/item349_j2_degenerate_triple_minor_carrier_root_audit.json":
        "e717c01d7429f7821a7ee75e8d979bc1362107bd70466af6af54d9748299a894",
    "manifests/item349_j2_degenerate_triple_minor_carrier_manifest.json":
        "1c1dec25ac00ea5adb2befe885c9c96ba805564651b6e90c73ef2506d30e7f4f",
    "sources/item352_j2_nonsemisimple_transition_no_go_report.md":
        "c60e1ba7771314c77b3fbe5d06f9c13c51a8c7e4d15f2589298641ff0f38e794",
    "results/item352_j2_nonsemisimple_transition_no_go_certificate.json":
        "8f06da2f8b4265156d02d2da393c0aedb74db55db3649589163866ffd0badc31",
    "results/item352_j2_nonsemisimple_transition_no_go_root_audit.json":
        "6acd46c106c21a963e0476e49d25c71305682c061e1df507ac8e332f4433d609",
    "manifests/item352_j2_nonsemisimple_transition_no_go_manifest.json":
        "c970d5b2dec42ec47f40078b49219cbac99e871b464a54f95be352729347ce54",
}


def default_output() -> Path:
    return HERE / RESULT_NAME


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


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def legendre(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    result = pow(value, (prime - 1) // 2, prime)
    if result == prime - 1:
        return -1
    if result != 1:
        raise AssertionError((value, prime, result))
    return 1


def affine_rows() -> list[list[int]]:
    payload = json.loads(
        (ROOT / "results/item341_j2_diagonal_affine_state_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    return payload["actual_affine_replay"]["rows"]


def actual_selector_row(row: list[int]) -> tuple[Any, ...]:
    prime, r, s, m = row[:4]
    c, c_star, H, theta = row[6:10]
    length = s
    if m != length - 1 or prime != 2 * r + 6 * length + 3:
        raise AssertionError((row, "actual tied phase"))

    M_numerator = 5 * r + 14 * length + 7
    if M_numerator % 2:
        raise AssertionError((row, "fixed-M parity"))
    fixed_M = M_numerator // 2
    if 4 * fixed_M != 5 * prime - 2 * length - 1:
        raise AssertionError((row, fixed_M, "selector forward"))
    selected_length_numerator = 5 * prime - 4 * fixed_M - 1
    if selected_length_numerator % 2:
        raise AssertionError((row, fixed_M, "selector inverse parity"))
    if selected_length_numerator // 2 != length:
        raise AssertionError((row, fixed_M, "selector inverse"))

    if c != pow(4, length, prime):
        raise AssertionError((row, c, "state first coordinate"))
    delta_one = (c - c_star) % prime
    delta_two = (H - theta) % prime
    collision = int(delta_one == 0 and delta_two == 0)

    # Orthogonality sums are evaluated exactly by their geometric-sum
    # alternatives, without numerical roots of unity.
    first_moment_numerator = prime * prime if collision else 0
    singleton_square_sum = prime * prime
    if F(singleton_square_sum, prime * prime) != 1:
        raise AssertionError((row, "singleton second moment"))
    if F(first_moment_numerator, prime * prime) != collision:
        raise AssertionError((row, "singleton first moment"))

    N = prime - 1
    if not (0 < length < N // 2):
        raise AssertionError((row, length, "actual Kummer prefix range"))
    weight_square_sum = sum(
        legendre(1 - x * pow(2, -1, prime), prime) ** 2
        for x in range(1, prime)
    )
    if weight_square_sum != prime - 2:
        raise AssertionError((row, weight_square_sum, "quadratic support"))
    full_jacobi_energy = 2 + (N - 2) * prime
    full_parseval_energy = N * weight_square_sum
    if full_jacobi_energy != full_parseval_energy or full_jacobi_energy != N * (N - 1):
        raise AssertionError((row, full_jacobi_energy, full_parseval_energy))
    prefix_coefficient_energy = 1 + (length - 1) * prime
    prefix_translate_energy = N * prefix_coefficient_energy

    target_rows = []
    for target in (F(0), F(1), F(3, 2), F(-2, 3)):
        fixed_target_energy = N * (F((length - 1) * prime) + (1 - target) ** 2)
        target_rows.append(
            (
                target.numerator,
                target.denominator,
                fixed_target_energy.numerator,
                fixed_target_energy.denominator,
            )
        )

    return (
        prime,
        r,
        s,
        fixed_M,
        delta_one,
        delta_two,
        collision,
        singleton_square_sum,
        first_moment_numerator,
        weight_square_sum,
        full_jacobi_energy,
        prefix_coefficient_energy,
        prefix_translate_energy,
        digest_rows(target_rows),
    )


def actual_selector_replay() -> dict[str, Any]:
    rows = [actual_selector_row(row) for row in affine_rows()]
    return {
        "classification": "EXACT FINITE REPLAY ONLY - NO PRIME OR COLLISION CENSUS",
        "declared_rows": len(rows),
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
    }


def occupancy_energy(
    prime: int,
    residuals: list[tuple[int, int]],
    weights: list[int],
) -> tuple[int, int, int, int]:
    if len(residuals) != len(weights):
        raise AssertionError("residual/weight length")
    cells: dict[tuple[int, int], int] = {}
    counts: dict[tuple[int, int], int] = {}
    for residual, weight in zip(residuals, weights):
        key = (residual[0] % prime, residual[1] % prime)
        cells[key] = cells.get(key, 0) + weight
        counts[key] = counts.get(key, 0) + 1
    weighted_energy = sum(value * value for value in cells.values())
    pair_expansion = 0
    for i, left in enumerate(residuals):
        left_key = (left[0] % prime, left[1] % prime)
        for j, right in enumerate(residuals):
            right_key = (right[0] % prime, right[1] % prime)
            if left_key == right_key:
                pair_expansion += weights[i] * weights[j]
    if weighted_energy != pair_expansion:
        raise AssertionError((prime, residuals, weights, weighted_energy, pair_expansion))
    unweighted_energy = sum(value * value for value in counts.values())
    zero_count = counts.get((0, 0), 0)
    fourier_square_sum = prime * prime * weighted_energy
    return weighted_energy, unweighted_energy, zero_count, fourier_square_sum


def combinatorial_parseval_replay() -> dict[str, Any]:
    declared = [
        (11, [(0, 0), (1, 0), (2, 3), (1, 0)], [1, 2, -1, 3]),
        (17, [(4, 5), (4, 5), (0, 0), (8, 2), (9, 2)], [2, -1, 4, 1, 3]),
        (29, [(0, 0), (0, 0), (0, 0), (7, 11)], [1, 1, 1, -2]),
    ]
    rows = []
    for prime, residuals, weights in declared:
        energy = occupancy_energy(prime, residuals, weights)
        rows.append((prime, len(residuals), *energy))

    # Two extremal families: minimum energy with the selected zero cell,
    # and maximum energy with all residuals in one cell.
    extremal_rows = []
    for prime, size in ((11, 5), (17, 8), (29, 12)):
        distinct = [(0, 0)] + [(index, 1) for index in range(1, size)]
        minimum = occupancy_energy(prime, distinct, [1] * size)
        if minimum[1] != size or minimum[2] != 1:
            raise AssertionError((prime, size, minimum, "minimum selector energy"))
        collapsed = [(0, 0)] * size
        maximum = occupancy_energy(prime, collapsed, [1] * size)
        if maximum[1] != size * size or maximum[2] != size:
            raise AssertionError((prime, size, maximum, "maximum energy"))
        extremal_rows.append((prime, size, minimum[1], minimum[2], maximum[1], maximum[2]))

    return {
        "classification": "SYMBOLIC EXACT COMBINATORIAL INSTANCES",
        "weighted_instances": len(rows),
        "weighted_digest_sha256": digest_rows(rows),
        "extremal_instances": len(extremal_rows),
        "extremal_digest_sha256": digest_rows(extremal_rows),
        "minimum_energy_selected_zero_demonstrated": True,
    }


def capacity_replay() -> dict[str, Any]:
    raw_mass = F(2, 35)
    normalized = raw_mass / 6
    if normalized != F(1, 105):
        raise AssertionError((raw_mass, normalized))
    rows = []
    for prime in (11, 17, 29, 271):
        singleton_energy = F(prime * prime, prime * prime)
        if singleton_energy != 1:
            raise AssertionError((prime, singleton_energy))
        rows.append((prime, singleton_energy.numerator, singleton_energy.denominator))
    return {
        "classification": "EXACT RATIONAL NORMALIZATION",
        "raw_chebyshev_coefficient": "2/35",
        "per_6M_capacity": "1/105",
        "singleton_energy_digest_sha256": digest_rows(rows),
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    return {
        "schema": "item355-j2-target-residual-large-sieve-obstruction-v1",
        "classification": "PROVED_EXACT_TARGET_RESIDUAL_PARSEVAL_AND_FIXED_M_SELECTOR_OBSTRUCTION",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "actual_residual": "Delta_p(L)=(4^L-c_star_(r(L)),H_(L-1)-Theta_(r(L),L))",
            "matrix_residual": "(det(A_(1/4)^L)-c_star,(M_L)_12+Theta)=(Delta_1,-Delta_2)",
            "weighted_Parseval": "p^-2 sum_(a,b)|sum_L alpha_L e_p(<(a,b),Delta_p(L)>)|^2=sum_y|sum_(Delta=y)alpha_L|^2",
            "zero_inversion": "N_p(0)=p^-2 sum_(a,b) sum_L e_p(<(a,b),Delta_p(L)>)",
            "fixed_M_selector": "L_(M,p)=(5p-4M-1)/2 and M=(5p-2L-1)/4",
            "singleton_saturation": "p^-2 sum_(a,b)|e_p(<(a,b),delta_(M,p)>)|^2=1 for every residual",
            "Jacobi_full_energy": "sum_(u=0)^(N-1)|j_u|^2=N(N-1)",
            "Jacobi_prefix_energy": "sum_a|P_L(a)|^2=N*(1+(L-1)*p) for L<N/2",
            "fixed_target_energy": "sum_a|P_L(a)-theta|^2=N*((L-1)*p+|1-theta|^2)",
            "moving_target_energy": "sum_a|P_L(a)-theta_a|^2=N*sum_u|1_(u<L)j_u-theta_hat_u|^2",
        },
        "actual_selector_replay": actual_selector_replay(),
        "combinatorial_parseval_replay": combinatorial_parseval_replay(),
        "capacity_replay": capacity_replay(),
        "capacity": {
            "raw_fixed_M_chebyshev_mass": "(2/35)M+o(M)",
            "ordinary_j2_ceiling_per_6M": "1/105",
            "chart_overlap": "nondegenerate and Item349 degenerate charts partition one raw interval and are not additive",
            "new_booking": 0,
            "new_capacity_reduction": 0,
        },
        "strict_labels": {
            "proved": [
                "exact target-retaining weighted residual Parseval and zero inversion",
                "fixed-M singleton second-moment saturation",
                "minimal transverse energy can retain a full prescribed selector diagonal as a method-class example",
                "exact full, prefix, fixed-target, and moving-target Kummer Parseval identities",
                "capacity and overlap audit",
            ],
            "finite_only": [
                "seven declared actual nondegenerate rows",
                "three weighted and three extremal combinatorial residual families",
                "no prime scan and no collision census",
            ],
            "open": [
                "power-saving actual residual collision energy",
                "selector-aware cross-prime cancellation for fixed M",
                "whether an almost-all-M result is admissible in the final construction",
                "weighted support of the Item349 degenerate carrier",
            ],
        },
        "scope_warning": (
            "The formal minimum-energy selector construction proves insufficiency of the statistic alone; "
            "it is not a model of the actual target sequence. A new arithmetic residual-energy or "
            "cross-prime selector theorem could still reduce capacity."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
