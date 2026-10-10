#!/usr/bin/env python3
"""Deterministic certificate for Item 352.

The checker replays the exact two-by-two nonsemisimple transition, its
quadratic-character moment, the chosen-prime p-step/Jordan identities,
the two target-retaining coordinates on declared actual rows, and the
exact truncation-tail identity.  Finite rows validate formulas only;
the p-curvature, complexity, edge-mass, and capacity proofs are in the
companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item352_j2_nonsemisimple_transition_no_go_certificate.json"


# Item 349 entries are replaced by the final root-audited canonical pins
# before the Item 352 manifest is frozen.
DEPENDENCIES = {
    "sources/item341_j2_diagonal_affine_state_report.md":
        "42f6ccd326e385f8034abe322756517a30a93d7468b3e6f85cbca3dba8080cb4",
    "results/item341_j2_diagonal_affine_state_certificate.json":
        "75c05cb486e5a5a6f9af5dda2e62f2a4b81cb888a15eb19ecabd10a382625cb4",
    "results/item341_j2_diagonal_affine_state_root_audit.json":
        "d5c810346f9181f10d38e9f5ae2e250a8c880e32f97cbc5bef91f6bd37f61a27",
    "manifests/item341_j2_diagonal_affine_state_manifest.json":
        "fc073e4c11a2d9ab519f0b5babae6f9f95e2e8cf9e8cbcf05c4c8ca8ba155000",
    "sources/item344_j2_frobenius_cutoff_obstruction_report.md":
        "1671dec30de80c047c52b6b4bf13157025ea631869f5ccacc73169002ec287a9",
    "results/item344_j2_frobenius_cutoff_obstruction_certificate.json":
        "f390d14d2b14ce965a33da8499e450294be3a038be2269d564d3cc3fda5f1179",
    "results/item344_j2_frobenius_cutoff_obstruction_root_audit.json":
        "1de770fc9f8cf23ec215d936e31b08bb59b5aad2ce8fb3480a0bd835011b5376",
    "manifests/item344_j2_frobenius_cutoff_obstruction_manifest.json":
        "9824b1a18fd645e729e103e32d0911d2392edc7b6c6642e5bea28d97489ef286",
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
}


Matrix = tuple[tuple[int, int], tuple[int, int]]


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


def matmul(left: Matrix, right: Matrix, prime: int) -> Matrix:
    return (
        (
            (left[0][0] * right[0][0] + left[0][1] * right[1][0]) % prime,
            (left[0][0] * right[0][1] + left[0][1] * right[1][1]) % prime,
        ),
        (
            (left[1][0] * right[0][0] + left[1][1] * right[1][0]) % prime,
            (left[1][0] * right[0][1] + left[1][1] * right[1][1]) % prime,
        ),
    )


def matpow(matrix: Matrix, exponent: int, prime: int) -> Matrix:
    answer: Matrix = ((1, 0), (0, 1))
    base = matrix
    while exponent:
        if exponent & 1:
            answer = matmul(answer, base, prime)
        base = matmul(base, base, prime)
        exponent >>= 1
    return answer


def matdet(matrix: Matrix, prime: int) -> int:
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % prime


def mattrace(matrix: Matrix, prime: int) -> int:
    return (matrix[0][0] + matrix[1][1]) % prime


def transition(x: int, prime: int) -> Matrix:
    return ((pow(x, -1, prime), 1), (0, 1))


def legendre(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    result = pow(value, (prime - 1) // 2, prime)
    if result == prime - 1:
        return -1
    if result != 1:
        raise AssertionError((value, prime, result, "Euler criterion"))
    return 1


def h_term_mod(index: int, prime: int) -> int:
    return math.comb(2 * index, index) % prime * pow(pow(8, index, prime), -1, prime) % prime


def h_prefix_mod(index: int, prime: int) -> int:
    if index < 0:
        return 0
    return sum(h_term_mod(u, prime) for u in range(index + 1)) % prime


def matrix_add_scaled(total: Matrix, matrix: Matrix, scale: int, prime: int) -> Matrix:
    return (
        (
            (total[0][0] + scale * matrix[0][0]) % prime,
            (total[0][1] + scale * matrix[0][1]) % prime,
        ),
        (
            (total[1][0] + scale * matrix[1][0]) % prime,
            (total[1][1] + scale * matrix[1][1]) % prime,
        ),
    )


def affine_targets() -> dict[tuple[int, int, int], tuple[int, int, int, int]]:
    payload = json.loads(
        (ROOT / "results/item341_j2_diagonal_affine_state_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    answer: dict[tuple[int, int, int], tuple[int, int, int, int]] = {}
    for row in payload["actual_affine_replay"]["rows"]:
        prime, r, s = row[:3]
        c, c_star, H, theta = row[6:10]
        answer[(prime, r, s)] = (c, c_star, H, theta)
    return answer


def rational_transition_replay() -> dict[str, Any]:
    rows = []
    for a in (F(2), F(3, 2), F(-1), F(5, 3)):
        for length in (1, 2, 3, 7):
            # [[a,1],[0,1]]^L has the asserted geometric-sum entry.
            geometric = sum((a ** u for u in range(length)), F(0))
            top_left = a ** length
            determinant = top_left
            trace = top_left + 1
            if geometric * (a - 1) != top_left - 1:
                raise AssertionError((a, length, "geometric transition"))
            rows.append(
                (
                    a.numerator,
                    a.denominator,
                    length,
                    top_left.numerator,
                    top_left.denominator,
                    geometric.numerator,
                    geometric.denominator,
                    trace.numerator,
                    trace.denominator,
                    determinant.numerator,
                    determinant.denominator,
                )
            )
    return {
        "classification": "SYMBOLIC EXACT RATIONAL INSTANCES",
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
    }


def tame_cover_replay() -> dict[str, Any]:
    rows = []
    for y in (F(1), F(2), F(-1), F(3, 2), F(-2)):
        if 2 * y * y == 1:
            continue
        z = 2 - 2 * y * y
        alpha = F(1, 1) / (1 - z) + F(1, 2) / (2 - z)
        dz_dy = -4 * y
        pulled = alpha * dz_dy
        dlog_f = -F(1, 1) / y - 4 * y / (2 * y * y - 1)
        if pulled != dlog_f:
            raise AssertionError((y, z, pulled, dlog_f, "tame-cover gauge"))
        rows.append(
            (
                y.numerator,
                y.denominator,
                z.numerator,
                z.denominator,
                pulled.numerator,
                pulled.denominator,
            )
        )
    return {
        "classification": "SYMBOLIC EXACT RATIONAL INSTANCES",
        "cover": "y^2=1-z/2",
        "pulled_gauge": "F=1/(y*(2*y^2-1))",
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
    }


def global_jordan_replay() -> dict[str, Any]:
    """Exercise both exact eigenvalue strata independently of actual rows."""
    rows = []
    for prime, h_value, H_value in (
        (11, 1, 0),
        (11, 1, 3),
        (13, 5, 7),
        (17, 2, 4),
    ):
        moment: Matrix = (((-h_value) % prime, (-H_value) % prime), (0, prime - 1))
        if h_value % prime != 1:
            parameter = H_value * pow((1 - h_value) % prime, -1, prime) % prime
            P: Matrix = ((1, parameter), (0, 1))
            P_inverse: Matrix = ((1, (-parameter) % prime), (0, 1))
            reduced = matmul(matmul(P_inverse, moment, prime), P, prime)
            expected: Matrix = ((moment[0][0], 0), (0, moment[1][1]))
            if reduced != expected:
                raise AssertionError((prime, h_value, H_value, reduced, expected))
            jordan_rank = 0
        else:
            nilpotent: Matrix = (
                ((moment[0][0] + 1) % prime, moment[0][1]),
                (0, (moment[1][1] + 1) % prime),
            )
            if matmul(nilpotent, nilpotent, prime) != ((0, 0), (0, 0)):
                raise AssertionError((prime, h_value, H_value, nilpotent))
            parameter = 0
            jordan_rank = int(H_value % prime != 0)
        rows.append(
            (
                prime,
                h_value,
                H_value,
                mattrace(moment, prime),
                matdet(moment, prime),
                parameter,
                jordan_rank,
            )
        )
    return {
        "classification": "SYMBOLIC EXACT FINITE-FIELD INSTANCES",
        "distinct_and_repeated_eigenvalue_strata_checked": True,
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
    }


def actual_transition_row(
    prime: int,
    r: int,
    s: int,
    targets: dict[tuple[int, int, int], tuple[int, int, int, int]],
) -> tuple[Any, ...]:
    if prime != 2 * r + 6 * s + 3:
        raise AssertionError((prime, r, s, "tied phase"))
    if not (r >= 1 and r % 2 == 1 and r % 3 != 0):
        raise AssertionError((prime, r, s, "actual residue restrictions"))
    length = s
    m = length - 1
    if not (0 < length < (prime - 1) // 2):
        raise AssertionError((prime, length, "actual prefix range"))

    H = h_prefix_mod(m, prime)
    h_length = h_term_mod(length, prime)
    inverse_two = pow(2, -1, prime)
    identity: Matrix = ((1, 0), (0, 1))
    moment: Matrix = ((0, 0), (0, 0))
    fiber_rows = []
    jordan_contribution = 0

    for x in range(1, prime):
        A = transition(x, prime)
        A_length = matpow(A, length, prime)
        inverse_x = pow(x, -1, prime)
        geometric = sum(pow(inverse_x, u, prime) for u in range(length)) % prime
        expected_power: Matrix = ((pow(inverse_x, length, prime), geometric), (0, 1))
        if A_length != expected_power:
            raise AssertionError((prime, x, length, A_length, expected_power))

        weight = legendre(1 - x * inverse_two, prime)
        moment = matrix_add_scaled(moment, A_length, weight, prime)
        if x == 1:
            if matpow(A, prime, prime) != identity:
                raise AssertionError((prime, x, "Jordan p-step"))
            expected_jordan = length * legendre(inverse_two, prime) % prime
            jordan_contribution = weight * A_length[0][1] % prime
            if jordan_contribution != expected_jordan:
                raise AssertionError((prime, jordan_contribution, expected_jordan))
        else:
            if matpow(A, prime, prime) != A or matpow(A, prime - 1, prime) != identity:
                raise AssertionError((prime, x, "semisimple p-step"))
        fiber_rows.append((x, weight, *A_length[0], *A_length[1]))

    expected_moment: Matrix = (((-h_length) % prime, (-H) % prime), (0, prime - 1))
    if moment != expected_moment:
        raise AssertionError((prime, r, s, moment, expected_moment, "complete moment"))

    x_quarter = pow(4, -1, prime)
    local = matpow(transition(x_quarter, prime), length, prime)
    local_det = matdet(local, prime)
    c, c_star, H_source, theta = targets[(prime, r, s)]
    if c != pow(4, length, prime) or local_det != c or H_source != H:
        raise AssertionError((prime, r, s, c, local_det, H_source, H, "actual state"))

    det_residual = (local_det - c_star) % prime
    extension_residual = (moment[0][1] + theta) % prime
    if extension_residual != (theta - H) % prime:
        raise AssertionError((prime, extension_residual, theta, H, "targeted extension"))

    # The characteristic polynomial of the complete moment ignores the
    # extension coordinate.  All finite powers keep only the same one
    # upper-right coordinate.
    power_rows = []
    for exponent in (1, 2, 3, 5):
        power = matpow(moment, exponent, prime)
        zero_extension: Matrix = ((moment[0][0], 0), (0, moment[1][1]))
        comparison = matpow(zero_extension, exponent, prime)
        if mattrace(power, prime) != mattrace(comparison, prime):
            raise AssertionError((prime, exponent, "power trace depends on extension"))
        if matdet(power, prime) != matdet(comparison, prime):
            raise AssertionError((prime, exponent, "power determinant depends on extension"))
        if power[1] != (0, comparison[1][1]):
            raise AssertionError((prime, exponent, "upper-triangular power"))
        power_rows.append((exponent, *power[0], *power[1]))

    diagonalizable = h_length != 1
    if diagonalizable:
        conjugator = H * pow((1 - h_length) % prime, -1, prime) % prime
        P: Matrix = ((1, conjugator), (0, 1))
        P_inverse: Matrix = ((1, (-conjugator) % prime), (0, 1))
        diagonal = matmul(matmul(P_inverse, moment, prime), P, prime)
        if diagonal != ((moment[0][0], 0), (0, moment[1][1])):
            raise AssertionError((prime, diagonal, "global semisimple conjugacy"))
        jordan_rank = 0
    else:
        nilpotent: Matrix = (
            ((moment[0][0] + 1) % prime, moment[0][1]),
            (0, (moment[1][1] + 1) % prime),
        )
        if matmul(nilpotent, nilpotent, prime) != ((0, 0), (0, 0)):
            raise AssertionError((prime, nilpotent, "global Jordan square"))
        conjugator = 0
        jordan_rank = int(H != 0)

    window_rows = []
    for window in sorted({0, 1, length // 2, length}):
        if not (0 <= window <= length):
            continue
        truncated = h_prefix_mod(window - 1, prime)
        tail = (H - truncated) % prime
        weighted_tail = 0
        for x in range(1, prime):
            weight = legendre(1 - x * inverse_two, prime)
            inverse_x = pow(x, -1, prime)
            tail_weight = sum(
                pow(inverse_x, u, prime) for u in range(window, length)
            ) % prime
            weighted_tail = (weighted_tail - weight * tail_weight) % prime
        if weighted_tail != tail:
            raise AssertionError((prime, length, window, weighted_tail, tail))
        window_rows.append((window, truncated, tail, weighted_tail))

    fixed_M_numerator = 5 * r + 14 * s + 7
    if fixed_M_numerator % 2:
        raise AssertionError((prime, r, s, "fixed-M parity"))
    fixed_M = fixed_M_numerator // 2
    if r != 6 * fixed_M - 7 * prime or 5 * prime != 4 * fixed_M + 2 * m + 3:
        raise AssertionError((prime, r, s, fixed_M, "fixed-M identities"))

    return (
        prime,
        r,
        s,
        fixed_M,
        length,
        h_length,
        H,
        c_star,
        theta,
        local_det,
        det_residual,
        extension_residual,
        moment[0][0],
        moment[0][1],
        moment[1][1],
        legendre(2, prime),
        jordan_contribution,
        int(diagonalizable),
        conjugator,
        jordan_rank,
        digest_rows(fiber_rows),
        digest_rows(power_rows),
        digest_rows(window_rows),
    )


def actual_transition_replay() -> dict[str, Any]:
    declared = [
        (11, 1, 1),
        (17, 1, 2),
        (29, 1, 4),
        (271, 113, 7),
        (367, 65, 39),
        (383, 109, 27),
        (599, 7, 97),
    ]
    targets = affine_targets()
    rows = [actual_transition_row(*row, targets) for row in declared]
    return {
        "classification": "EXACT FINITE REPLAY ONLY - NO PRIME OR COLLISION CENSUS",
        "declared_rows": len(rows),
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    return {
        "schema": "item352-j2-nonsemisimple-transition-no-go-v1",
        "classification": "PROVED_EXACT_JORDAN_TRANSITION_AND_FORMAL_WINDOW_NO_GO",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "transition": "A_x=[[x^-1,1],[0,1]]",
            "transition_power": "A_x^L=[[x^-L,sum_(u=0)^(L-1)x^-u],[0,1]]",
            "complete_matrix_moment": "sum_(x!=0) chi(1-x/2) A_x^L=[[-h_L,-H_(L-1)],[0,-1]]",
            "nondegenerate_collision_coordinates": "det(A_(1/4)^L)=4^L=c_star and M_12=-Theta",
            "p_step": "A_x^p=A_x and A_x^(p-1)=I for x!=1; A_1^p=I",
            "unique_Jordan_fiber": "A_1^L=I+L*N, weighted extension L*(2/p)",
            "global_Jordan_strata": "M diagonalizable if h_L!=1; if h_L=1 then M=-I-H_(L-1)E_12",
            "functorial_extension_ideal": "after the target shift delta=Theta-H_(L-1), every nilpotent polynomial/tensor/symmetric/exterior readout lies in the old ideal (delta)",
            "tame_cover": "y^2=1-z/2 trivializes d-dlog(1/((1-z)y)); p-curvature is zero for odd p",
            "window_tail": "H_(L-1)-H_(D-1)=-sum_x chi(1-x/2) sum_(u=D)^(L-1)x^-u",
            "compressed_complexity": "tr(A_x^L)=1+x^-L and det(A_x^L)=x^-L have pole order L at x=0",
            "rank_pole_tradeoff": "an exact n-state companion retaining determinant x^-L with entry pole order <=K satisfies n*K>=L",
        },
        "rational_transition_replay": rational_transition_replay(),
        "tame_cover_replay": tame_cover_replay(),
        "global_jordan_replay": global_jordan_replay(),
        "actual_transition_replay": actual_transition_replay(),
        "chart_and_capacity_audit": {
            "raw_fixed_M_prime_mass": "(2/35)M+o(M)",
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "outer_charts": "ell!=0 and ell=0 partition one raw interval; capacities are not additive",
            "degenerate_internal_charts": "f!=0 and f=0 partition the Item349 carrier; capacities are not additive",
            "sublinear_window_reach": "formal/uniform exactness requires L<=D; D=o(M) then implies m=o(M) and o(M) logarithmic prime mass",
            "pointwise_tail_warning": "for D<L the weighted tail can vanish accidentally at a chosen prime; its weighted zero density is open",
            "positive_rate_complexity": "on m asymptotic to M, n*K>=L=Omega(M); bounded pole order forces linear rank and bounded rank forces linear pole order",
            "new_booking": 0,
            "new_capacity_reduction": 0,
        },
        "strict_labels": {
            "proved": [
                "exact two-by-two transition and complete matrix moment",
                "chosen-prime p-step and unique fiberwise Jordan contribution",
                "zero p-curvature of the fixed quadratic rank-one connection",
                "no new global-moment invariant beyond the existing extension coordinate",
                "natural formal/uniform bounded-sublinear nonsemisimple-window no-go",
                "chart-overlap and raw-capacity audit",
            ],
            "finite_only": [
                "seven declared actual-row transition, moment, target-coordinate, p-step, power, and tail replays",
                "four synthetic exact finite-field instances exercising both global Jordan strata",
                "no prime scan and no collision census",
            ],
            "open": [
                "weighted nonconcentration for the moving joint state on the nondegenerate chart",
                "weighted support of the safely saturated Item349 carrier on the degenerate chart",
                "weighted control of accidental vanishing for proper truncation tails",
                "a target-specific chosen-prime construction outside the exact transition/Kummer/window classes",
            ],
        },
        "scope_warning": (
            "The no-go is for exact powers of the canonical transition, their finite matrix invariants, "
            "and bounded/sublinear truncation windows. It is not a theorem about every possible "
            "p-dependent nonlinear or nonsemisimple sheaf."
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
