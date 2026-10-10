#!/usr/bin/env python3
"""Exact checker for Item 245's generalized j=1 phase observations."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item245_j1_generalized_phase_observation_certificate.json"

DEPENDENCIES = {
    "sources/item234_j1_first_witt_report.md":
        "9bd5bb91fe813622db0c15d8bfc25714bcefb00512ed8f5eafddacd8cfb9b016",
    "scripts/item234_j1_first_witt_certificate.py":
        "8d41a5a73e9467cf4c998d3e345767c04c68ab6467605290480825b15b08e125",
    "results/item234_j1_first_witt_certificate.json":
        "6797c1f2cd072ec92d311e01b596c3ac95888ce9b761bc325a625ef6f9f0c748",
    "sources/item242_j1_E_kernel_state_report.md":
        "174db03d85654f526fa20af1abd135944d2995babd2a682e16d1416bfe9c9d09",
    "scripts/item242_j1_E_kernel_state_certificate.py":
        "6941b01522fd981de0a70139715b57883e15b23fd43858581a8cb4f07bbe1d84",
    "results/item242_j1_E_kernel_state_certificate.json":
        "77a6ffe1af55e03504def21883af74d6abe07000d75301459fe812b8ca585f73",
}


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def resolve_dependency(relative_name: str) -> Path:
    candidates = (HERE.parent / relative_name, HERE / Path(relative_name).name)
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(relative_name)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_module(name: str, relative_name: str):
    path = resolve_dependency(relative_name)
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def p_section(poly: list[int], prime: int, residue: int) -> list[int]:
    if residue >= len(poly):
        return [0]
    return [
        poly[residue + index * prime] % prime
        for index in range((len(poly) - 1 - residue) // prime + 1)
    ]


def pad(poly: list[int], length: int) -> list[int]:
    return (poly + [0] * length)[:length]


def q_power(power: int, item242, prime: int) -> list[int]:
    answer = [1]
    factor = [1, 0, 1]
    for _ in range(power):
        answer = item242.poly_mul(answer, factor, prime)
    return answer


def qadic_digits(
    section: list[int], levels: int, item242, prime: int
) -> list[list[int]]:
    current = section[:]
    digits = []
    factor = [1, 0, 1]
    for _ in range(levels):
        quotient, remainder = item242.poly_divmod(current, factor, prime)
        digits.append(pad(remainder, 2))
        current = quotient
    return digits


def generalized_state(
    prime: int,
    h_value: int,
    s_value: int,
    nu: int,
    item234,
    item242,
    numerator_cache: dict[int, list[int]],
) -> tuple[list[int], list[list[int]], list[int]]:
    if prime not in numerator_cache:
        numerator_cache[prime] = item242.kernel_numerator(prime, item234)[0]
    numerator = numerator_cache[prime]
    poly = [value % prime for value in item234.p_polynomial(
        prime, h_value, s_value, nu
    )]
    product = item242.poly_mul(numerator, poly, prime)
    residue = prime - (2 * s_value - nu) - 1
    section = p_section(product, prime, residue)
    q_four = q_power(4, item242, prime)
    _, state = item242.poly_divmod(section, q_four, prime)
    state = pad(state, 8)
    digits = qadic_digits(section, 5, item242, prime)
    reconstruction = [0]
    factor_power = [1]
    for digit in digits:
        reconstruction = item242.poly_add(
            reconstruction,
            item242.poly_mul(digit, factor_power, prime),
            prime,
        )
        factor_power = item242.poly_mul(factor_power, [1, 0, 1], prime)
    q_five = q_power(5, item242, prime)
    _, expected = item242.poly_divmod(section, q_five, prime)
    _, reconstructed = item242.poly_divmod(reconstruction, q_five, prime)
    if expected != reconstructed:
        raise AssertionError((prime, h_value, s_value, nu, "Q-adic digits"))
    return state, digits, section


def leading_pair_fast(
    prime: int,
    h_value: int,
    s_value: int,
    nu: int,
    item234,
    bb_cache: dict[int, list[int]],
) -> tuple[int, int]:
    if prime not in bb_cache:
        _, _, b_zero, _ = item234.harmonic_digits(prime)
        bb_cache[prime] = item234.convolution_mod(
            b_zero, b_zero, prime, 4 * prime - 4
        )
    bb = bb_cache[prime]
    poly = [value % prime for value in item234.p_polynomial(
        prime, h_value, s_value, nu
    )]
    residue = prime - (2 * s_value - nu) - 1
    alpha = 0
    beta = 0
    section_index = 0
    maximum = len(bb) + len(poly) - 2
    while residue + section_index * prime <= maximum:
        value = (
            -24
            * item234.coefficient_product(
                bb, poly, residue + section_index * prime, prime
            )
        ) % prime
        if section_index % 2 == 0:
            alpha += (-1) ** (section_index // 2) * value
        else:
            beta += (-1) ** ((section_index - 1) // 2) * value
        section_index += 1
    return alpha % prime, beta % prime


def multiplication_matrix(
    state: list[int], prime: int, item242
) -> list[list[int]]:
    modulus = q_power(4, item242, prime)
    columns = []
    for shift in range(8):
        _, remainder = item242.poly_divmod(
            [0] * shift + state, modulus, prime
        )
        columns.append(pad(remainder, 8))
    return [
        [columns[column][row] for column in range(8)]
        for row in range(8)
    ]


def universal_observation_matrix(prime: int) -> list[list[int]]:
    """First eight phase coefficients of Z^j/(1+Z^2)^4."""
    matrix = []
    for phase in range(8):
        row = []
        for numerator_degree in range(8):
            difference = phase - numerator_degree
            if difference < 0 or difference % 2:
                row.append(0)
            else:
                index = difference // 2
                row.append(
                    (-1) ** index * math.comb(index + 3, 3) % prime
                )
        matrix.append(row)
    return matrix


def matrix_multiply(
    left: list[list[int]], right: list[list[int]], prime: int
) -> list[list[int]]:
    return [
        [
            sum(
                left[row][inner] * right[inner][column]
                for inner in range(len(right))
            ) % prime
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def matrix_digest(matrix: list[list[int]]) -> str:
    payload = "".join(
        ",".join(str(value) for value in row) + "\n" for row in matrix
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def matrix_row_digests(matrix: list[list[int]]) -> list[str]:
    return [
        hashlib.sha256(
            (",".join(str(value) for value in row) + "\n").encode("ascii")
        ).hexdigest()
        for row in matrix
    ]


def reciprocal_section_check(
    prime: int,
    h_value: int,
    s_value: int,
    nu: int,
    item234,
    item242,
    bb_cache: dict[int, list[int]],
) -> tuple[list[int], list[int]]:
    if prime not in bb_cache:
        _, _, b_zero, _ = item234.harmonic_digits(prime)
        bb_cache[prime] = item234.convolution_mod(
            b_zero, b_zero, prime, 4 * prime - 4
        )
    bb = bb_cache[prime]
    poly = [value % prime for value in item234.p_polynomial(
        prime, h_value, s_value, nu
    )]
    product = item242.poly_mul(bb, poly, prime)
    r_value = 2 * h_value
    q_value = 2 * s_value - nu
    degree = r_value + 4 * s_value + 1 + nu
    reciprocal_degree = 4 * prime + degree
    for index in range(reciprocal_degree + 1):
        left = product[index] if index < len(product) else 0
        right_index = reciprocal_degree - index
        right = product[right_index] if right_index < len(product) else 0
        if left != right:
            raise AssertionError((
                prime, h_value, s_value, nu, index, left, right,
                "reciprocity",
            ))
    target_residue = prime - q_value - 1
    common_residue = prime - r_value - 1
    target_section = pad(p_section(product, prime, target_residue), 4)
    common_section = pad(p_section(product, prime, common_residue), 4)
    if target_section != list(reversed(common_section)):
        raise AssertionError((
            prime, h_value, s_value, nu,
            target_section, common_section, "section reciprocity",
        ))
    return target_section, common_section


def build_certificate(direct_limit: int, census_limit: int) -> dict:
    dependency_hashes = {
        name: sha256_file(resolve_dependency(name)) for name in DEPENDENCIES
    }
    if dependency_hashes != DEPENDENCIES:
        raise AssertionError((dependency_hashes, DEPENDENCIES))

    item234 = load_module("item234_frozen", "scripts/item234_j1_first_witt_certificate.py")
    item242 = load_module("item242_frozen", "scripts/item242_j1_E_kernel_state_certificate.py")
    numerator_cache: dict[int, list[int]] = {}
    bb_cache: dict[int, list[int]] = {}

    direct_rows = 0
    direct_coordinates = 0
    determinant_checks = 0
    reciprocity_checks = 0
    qadic_checks = 0
    old_pair_absence_checks = 0
    sample_matrices = []
    for prime, h_value, s_value in item234.rows_upto(direct_limit):
        observation = universal_observation_matrix(prime)
        if item242.determinant_mod(observation, prime) != 1:
            raise AssertionError((prime, "universal observation determinant"))
        for nu in (0, 1):
            state, digits, section = generalized_state(
                prime, h_value, s_value, nu,
                item234, item242, numerator_cache,
            )
            while len(section) > 1 and section[-1] == 0:
                section.pop()
            if len(section) > 8 or digits[4] != [0, 0]:
                raise AssertionError((
                    prime, h_value, s_value, nu,
                    len(section) - 1, digits[4], "old-pair absence",
                ))
            alpha, beta = digits[0]
            fast_pair = leading_pair_fast(
                prime, h_value, s_value, nu, item234, bb_cache
            )
            if (alpha, beta) != fast_pair:
                raise AssertionError((
                    prime, h_value, s_value, nu,
                    (alpha, beta), fast_pair, "leading pair",
                ))
            cyclic = multiplication_matrix(state, prime, item242)
            terminal = matrix_multiply(observation, cyclic, prime)
            determinant = item242.determinant_mod(terminal, prime)
            expected_determinant = pow(
                (alpha * alpha + beta * beta) % prime, 4, prime
            )
            if determinant != expected_determinant:
                raise AssertionError((
                    prime, h_value, s_value, nu,
                    determinant, expected_determinant,
                ))
            reciprocal_section_check(
                prime, h_value, s_value, nu,
                item234, item242, bb_cache,
            )
            # Q^4*c4/Q^5=c4/Q is precisely the old simple +/-i layer.
            simple_pair_present = False
            qadic_checks += 1
            old_pair_absence_checks += 1
            determinant_checks += 1
            reciprocity_checks += 1
            direct_coordinates += 1
            if (prime, h_value, s_value) == (29, 5, 1):
                sample_matrices.append({
                    "nu": nu,
                    "state_mod_Q4": state,
                    "Q_adic_digits_c0_through_c4": digits,
                    "c4_old_pair_nonzero": simple_pair_present,
                    "leading_pair": [alpha, beta],
                    "leading_norm": (alpha * alpha + beta * beta) % prime,
                    "terminal_matrix": terminal,
                    "terminal_matrix_rank": item242.rank_mod(terminal, prime),
                    "terminal_matrix_determinant": determinant,
                    "terminal_matrix_sha256": matrix_digest(terminal),
                    "terminal_matrix_row_sha256": matrix_row_digests(terminal),
                })
        direct_rows += 1

    if direct_limit == 151 and (direct_rows, direct_coordinates) != (184, 368):
        raise AssertionError((direct_rows, direct_coordinates))

    individual_records = []
    joint_deficient_records = []
    rank_counts = {str(rank): 0 for rank in range(9)}
    census_rows = 0
    for prime, h_value, s_value in item234.rows_upto(census_limit):
        pairs = [
            leading_pair_fast(
                prime, h_value, s_value, nu, item234, bb_cache
            )
            for nu in (0, 1)
        ]
        norms = [
            (alpha * alpha + beta * beta) % prime
            for alpha, beta in pairs
        ]
        cross = (
            pairs[0][0] * pairs[1][1] - pairs[1][0] * pairs[0][1]
        ) % prime
        for nu in (0, 1):
            if norms[nu]:
                rank = 8
            else:
                state, _, _ = generalized_state(
                    prime, h_value, s_value, nu,
                    item234, item242, numerator_cache,
                )
                rank = item242.rank_mod(
                    multiplication_matrix(state, prime, item242), prime
                )
                individual_records.append([
                    prime, h_value, s_value, nu,
                    pairs[nu][0], pairs[nu][1], rank,
                ])
            rank_counts[str(rank)] += 1
        if norms[0] == 0 and norms[1] == 0 and cross == 0:
            state_zero, _, _ = generalized_state(
                prime, h_value, s_value, 0,
                item234, item242, numerator_cache,
            )
            state_one, _, _ = generalized_state(
                prime, h_value, s_value, 1,
                item234, item242, numerator_cache,
            )
            matrix_zero = multiplication_matrix(state_zero, prime, item242)
            matrix_one = multiplication_matrix(state_one, prime, item242)
            joint_rank = item242.rank_mod(matrix_zero + matrix_one, prime)
            joint_deficient_records.append([
                prime, h_value, s_value, joint_rank,
                pairs, norms, cross,
            ])
        census_rows += 1

    if census_limit == 601:
        if census_rows != 2435:
            raise AssertionError(census_rows)
        if rank_counts != {
            "0": 0, "1": 0, "2": 0, "3": 0, "4": 0,
            "5": 0, "6": 1, "7": 18, "8": 4851,
        }:
            raise AssertionError(rank_counts)
        if joint_deficient_records:
            raise AssertionError(joint_deficient_records)

    return {
        "item": 245,
        "title": "generalized +/-i terminal observations on the actual j=1 family",
        "parameters": {
            "row": "p=4h+6s+3, r=2h, h,s>=1",
            "direct_limit": direct_limit,
            "census_limit": census_limit,
        },
        "proved": {
            "Q_adic_split": (
                "A mod Q^5=c0+Qc1+Q^2c2+Q^3c3+Q^4c4; "
                "c4/Q is the old +/-i pair and A mod Q^4 is the "
                "eight-dimensional generalized quotient"
            ),
            "actual_family_old_pair_absence": (
                "deg of the target p-section is at most 7, so c4=0 on "
                "every actual row and the independent simple-pole +/-i "
                "summand is absent"
            ),
            "universal_terminal_observability": (
                "the first-eight-phase observation matrix for "
                "F_p[Z]/(1+Z^2)^4 is unit lower triangular with determinant 1"
            ),
            "actual_observation_determinant": (
                "det T_nu=(alpha_nu^2+beta_nu^2)^4"
            ),
            "leading_pair_formula": (
                "alpha_nu+beta_nu Z=-24 Cartier_a(B0^2 P_nu) mod (1+Z^2), "
                "a=p-(2s-nu)-1"
            ),
            "reciprocity_alignment": (
                "Cartier_a(B0^2P_nu)(Z)=Z^3 Cartier_b(B0^2P_nu)(Z^-1), "
                "b=p-r-1, for both nu"
            ),
            "rank_classification": (
                "over an algebraic closure rank T_nu=8-k_+-k_-, where "
                "k_+/- are the Q-adic root valuations truncated at 4"
            ),
            "joint_rank_criterion": (
                "the stacked two-coordinate matrix has rank "
                "8-min(k0,+,k1,+)-min(k0,-,k1,-)"
            ),
        },
        "exact_replay": {
            "rows": direct_rows,
            "coordinates": direct_coordinates,
            "Q_adic_checks": qadic_checks,
            "old_pair_absence_checks": old_pair_absence_checks,
            "determinant_checks": determinant_checks,
            "reciprocity_checks": reciprocity_checks,
            "sample_row_29_5_1": sample_matrices,
        },
        "exact_finite_only": {
            "rows_through_census_limit": census_rows,
            "coordinate_rank_counts": rank_counts,
            "individual_rank_drop_records": individual_records,
            "joint_rank_drop_records": joint_deficient_records,
            "interpretation": (
                "no joint rank drop occurs through the stated bound; "
                "this is not an all-row nonvanishing theorem"
            ),
        },
        "scope": {
            "comparison_with_Item233": (
                "c4 is the old +/-i pair; the q0 eigenmode is not part of "
                "this Q-primary kernel module, and no Item233 M/N matrix "
                "identity is assumed"
            ),
            "terminal_normalization": (
                "the actual target section begins at phase 2; after applying "
                "the canonical Q-primary quotient, any resulting phase-origin "
                "translation is a unit and does not change rank or determinant"
            ),
            "no_family_wide_dependency": (
                "the exact determinant factors may vanish on special rows; "
                "reciprocity aligns the residues but does not itself force a "
                "rank loss"
            ),
        },
        "open": [
            "all-row nonvanishing of at least one of the two coordinate factors",
            "an exact family-specific identity excluding a joint root of Q",
            "whether generalized phase observability yields an actual p^3 terminal obstruction",
            "any all-prime common-log exclusion or Route-1 rate consequence",
        ],
        "dependencies": dependency_hashes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--direct-limit", type=int, default=151)
    parser.add_argument("--census-limit", type=int, default=601)
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.direct_limit, arguments.census_limit)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(arguments.output),
        "direct_rows": certificate["exact_replay"]["rows"],
        "rank_counts": certificate["exact_finite_only"]["coordinate_rank_counts"],
        "joint_drops": len(
            certificate["exact_finite_only"]["joint_rank_drop_records"]
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
