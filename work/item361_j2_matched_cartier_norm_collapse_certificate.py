#!/usr/bin/env python3
"""Deterministic certificate for Item 361.

The checker replays the exact base-p digit map, the two branchwise
Cartier reductions, their identification with the old branch coefficients,
and the cubic phase elimination.  It uses only predeclared actual rows and
symbolic rational controls; it performs no prime scan or collision census.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item361_j2_matched_cartier_norm_collapse_certificate.json"


# Item 359 pins are replaced with final canonical root-audited hashes
# before the Item 361 manifest is frozen.
DEPENDENCIES = {
    "sources/item315_j2_resultant_arithmetic_report.md":
        "3ce61af707268ceed6db0355a31333492bd8b07ec34e455cbee874fc6a2291b8",
    "scripts/item315_j2_resultant_arithmetic_certificate.py":
        "42def823c42497fa9ce4c5513c348464511a56cc6ff12480bec60408c9733b81",
    "results/item315_j2_resultant_arithmetic_certificate.json":
        "09fdd67a6535a043bcbd1e2a46c4b14a633b9928a5f1c65618c34fab65cfabb6",
    "results/item315_root_audit.json":
        "b764ea214de0c99a6398c981a5d35ca5b911c4d08e7e128f55276a30b1ea66d6",
    "manifests/item315_j2_resultant_arithmetic_manifest.json":
        "698abf2124e564c63cf4d1142cd33e872d6fb6b4da21e4e6ec7ac26c43c7a8c1",
    "sources/item359_j2_fixedM_cross_prime_coefficient_barrier_report.md":
        "f9dac057bcbbab144f5cc38964f997e5fcef14ff718a1ebd7615bc4fc6869edb",
    "scripts/item359_j2_fixedM_cross_prime_coefficient_barrier_certificate.py":
        "ec07fcb23d72e42e17f6f53f7263dc4aa2c9e611c02f355389566c927216b28e",
    "results/item359_j2_fixedM_cross_prime_coefficient_barrier_certificate.json":
        "b8ad2ebf3cc93b43649ff26d3c6deba888b4046d39224193b1c2ea53afa98227",
    "results/item359_j2_fixedM_cross_prime_coefficient_barrier_root_audit.json":
        "c6525ce001fb786619aee6aa48fb84009a7b14d6370e628d0c3f9945c369319a",
    "manifests/item359_j2_fixedM_cross_prime_coefficient_barrier_manifest.json":
        "6734e4b46e80892c6a8ac845064fa1f89e0e79e87d51af32f094e7279c89db3d",
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
        if expected.startswith("__"):
            raise AssertionError((relative, "unresolved dependency placeholder"))
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def poly_mul(left: list[int], right: list[int], limit: int, prime: int) -> list[int]:
    out = [0] * (min(limit, len(left) + len(right) - 2) + 1)
    for i, x in enumerate(left):
        if i > limit:
            break
        for j, y in enumerate(right):
            degree = i + j
            if degree > limit:
                break
            out[degree] = (out[degree] + x * y) % prime
    return out


def poly_pow(base: list[int], exponent: int, limit: int, prime: int) -> list[int]:
    result = [1]
    power = [value % prime for value in base[: limit + 1]]
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = poly_mul(result, power, limit, prime)
        remaining >>= 1
        if remaining:
            power = poly_mul(power, power, limit, prime)
    return result + [0] * (limit + 1 - len(result))


def inverse_series(denominator: list[int], limit: int, prime: int) -> list[int]:
    inverse_constant = pow(denominator[0] % prime, -1, prime)
    out = [inverse_constant]
    for degree in range(1, limit + 1):
        total = 0
        for index in range(1, min(degree, len(denominator) - 1) + 1):
            total += denominator[index] * out[degree - index]
        out.append((-inverse_constant * total) % prime)
    return out


def rational_series(
    numerator: list[int], denominator: list[int], limit: int, prime: int
) -> list[int]:
    return poly_mul(
        [value % prime for value in numerator],
        inverse_series(denominator, limit, prime),
        limit,
        prime,
    )


def negative_binomial_series(exponent: int, sign: int, limit: int, prime: int) -> list[int]:
    out = [1]
    for degree in range(1, limit + 1):
        value = out[-1] * (exponent + degree - 1) % prime
        value = value * pow(degree, -1, prime) % prime
        value = value * sign % prime
        out.append(value)
    return out


def fixed_r_series(branch: str, degree: int, prime: int) -> list[int]:
    if branch == "minus":
        p_poly = [45, -33, -42, 278, -199, 55, 16]
        numerator = poly_mul(poly_mul([1, 1], [1, 0, 1], 9, prime), p_poly, 9, prime)
        denominator = poly_pow([-3, 6, 1, 2], 4, 12, prime)
    elif branch == "plus":
        p_poly = [120, 292, 388, 352, 316, 151, 16]
        numerator = poly_mul(poly_mul([2, 1], [2, 2, 1], 9, prime), p_poly, 9, prime)
        denominator = poly_pow([6, 14, 7, 2], 4, 12, prime)
    else:
        raise ValueError(branch)
    return rational_series(numerator, denominator, degree, prime)


def u_power_series(branch: str, exponent: int, degree: int, prime: int) -> list[int]:
    if branch == "minus":
        numerator = poly_pow([1, 0, 1], 4 * exponent, degree, prime)
        denominator = negative_binomial_series(6 * exponent, 1, degree, prime)
    elif branch == "plus":
        numerator = poly_pow([1, 1, pow(2, -1, prime)], 4 * exponent, degree, prime)
        denominator = negative_binomial_series(6 * exponent, -1, degree, prime)
    else:
        raise ValueError(branch)
    return poly_mul(numerator, denominator, degree, prime)


def branch_component_mod(
    branch: str, exponent: int, degree: int, prime: int
) -> int:
    r_series = fixed_r_series(branch, degree, prime)
    u_series = u_power_series(branch, exponent, degree, prime)
    return sum(r_series[j] * u_series[degree - j] for j in range(degree + 1)) % prime


DECLARED_ROWS = [
    # p, r, s, M, Item355 Delta_1, Item355 Delta_2
    (11, 1, 1, 13, 4, 9),
    (17, 1, 2, 20, 12, 5),
    (29, 1, 4, 34, 4, 17),
    (271, 113, 7, 335, 0, 172),
    (367, 65, 39, 439, 0, 197),
    (383, 109, 27, 465, 0, 316),
    (599, 7, 97, 700, 275, 551),
]


def matched_cartier_replay() -> dict[str, Any]:
    item315 = load("item361_i315", "scripts/item315_j2_resultant_arithmetic_certificate.py")
    minus = item315.i309.branch_coefficients(max(row[1] for row in DECLARED_ROWS))
    rows = []
    for prime, r, s, fixed_M, delta_one, delta_two in DECLARED_ROWS:
        t = fixed_M - prime
        m = s - 1
        k = r - 1
        q = 2 * t + 1
        if prime != 6 * t - r:
            raise AssertionError((prime, r, fixed_M, t, "p=6t-r"))
        if s != (prime - 4 * t - 1) // 2 or 2 * s != prime - 4 * t - 1:
            raise AssertionError((prime, s, t, "s selector"))
        if m != (prime - 4 * t - 3) // 2 or 2 * m != prime - 4 * t - 3:
            raise AssertionError((prime, m, t, "m selector"))
        if not (0 < t < prime and 0 < r < prime and 0 <= k < prime and 0 <= m < prime):
            raise AssertionError((prime, r, s, fixed_M, t, m, k, "digit range"))
        if q != 2 * (fixed_M - prime) + 1:
            raise AssertionError((prime, q, "q"))

        minus_M = branch_component_mod("minus", fixed_M, k, prime)
        minus_t = branch_component_mod("minus", t, k, prime)
        plus_M = branch_component_mod("plus", fixed_M, k, prime)
        plus_t = branch_component_mod("plus", t, k, prime)
        if minus_M != minus_t or plus_M != plus_t:
            raise AssertionError((prime, minus_M, minus_t, plus_M, plus_t, "Cartier"))

        a_value = minus[r]
        b_value = item315.i237.lagrange_coefficient(r)
        expected_minus = -r * fmod(a_value, prime) * pow(12, -1, prime) % prime
        expected_plus = -r * fmod(b_value, prime) * pow(12, -1, prime) % prime
        if minus_t != expected_minus or plus_t != expected_plus:
            raise AssertionError((prime, minus_t, expected_minus, plus_t, expected_plus, "low digit"))

        z_value = pow(16, t, prime)
        phase_cube = pow(z_value, 3, prime)
        expected_cube = pow(2, 2 * r + 2, prime)
        if phase_cube != expected_cube:
            raise AssertionError((prime, z_value, phase_cube, expected_cube, "phase cube"))

        reduced_gate = (18 * fmod(a_value, prime) + 11 * z_value * fmod(b_value, prime)) % prime
        matched_coefficient = (18 * minus_M + 11 * pow(16, fixed_M - 1, prime) * plus_M) % prime
        expected_coefficient = -r * reduced_gate * pow(12, -1, prime) % prime
        if matched_coefficient != expected_coefficient:
            raise AssertionError((prime, matched_coefficient, expected_coefficient, "matched coefficient"))

        norm_exact = item315.norm_value(r, minus)
        norm_mod = fmod(norm_exact, prime)
        norm_from_phase = (
            pow(18 * fmod(a_value, prime), 3, prime)
            + pow(11 * fmod(b_value, prime), 3, prime) * expected_cube
        ) % prime
        if norm_mod != norm_from_phase:
            raise AssertionError((prime, norm_mod, norm_from_phase, "old norm"))
        if reduced_gate == 0 and norm_mod != 0:
            raise AssertionError((prime, reduced_gate, norm_mod, "gate implies norm"))

        rows.append(
            (
                prime,
                r,
                s,
                fixed_M,
                t,
                m,
                q,
                k,
                minus_M,
                minus_t,
                plus_M,
                plus_t,
                z_value,
                phase_cube,
                reduced_gate,
                matched_coefficient,
                norm_mod,
                delta_one,
                delta_two,
            )
        )
    return {
        "classification": "EXACT FINITE REPLAY ONLY - NO PRIME OR COLLISION CENSUS",
        "declared_rows": len(rows),
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
    }


def elimination_identity_replay() -> dict[str, Any]:
    controls = [
        (F(2), F(3), F(5), F(7)),
        (F(-11), F(13), F(17), F(-19)),
        (F(23, 2), F(-29, 3), F(31, 5), F(37, 7)),
        (F(0), F(41), F(-43), F(47)),
        (F(53), F(0), F(59), F(-61)),
    ]
    rows = []
    for A, B, c, z in controls:
        left = A**3 + B**3 * c
        right = (A + B * z) * (A**2 - A * B * z + B**2 * z**2) + B**3 * (c - z**3)
        if left != right:
            raise AssertionError((A, B, c, z, left, right))
        rows.append(
            (
                A.numerator, A.denominator,
                B.numerator, B.denominator,
                c.numerator, c.denominator,
                z.numerator, z.denominator,
                left.numerator, left.denominator,
            )
        )
    return {
        "classification": "SYMBOLIC EXACT POLYNOMIAL IDENTITY CONTROLS",
        "identity": "A^3+B^3*c=(A+Bz)(A^2-ABz+B^2z^2)+B^3(c-z^3)",
        "declared_rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
        "elimination_generator": "A^3+B^3*c",
    }


def capacity_replay() -> dict[str, Any]:
    raw = F(6, 7) - F(4, 5)
    normalized = raw / 6
    ray = raw / 2
    ray_normalized = ray / 6
    if (
        raw != F(2, 35)
        or normalized != F(1, 105)
        or ray != F(1, 35)
        or ray_normalized != F(1, 210)
    ):
        raise AssertionError((raw, normalized, ray, ray_normalized))
    return {
        "classification": "EXACT RATIONAL CAPACITY NORMALIZATION",
        "raw_chebyshev_coefficient": "2/35",
        "per_6M_capacity": "1/105",
        "each_mod6_ray_coefficient": "1/35",
        "each_mod6_ray_capacity_per_6M": "1/210",
        "new_booking": 0,
        "new_capacity_reduction": 0,
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    return {
        "schema": "item361-j2-matched-cartier-norm-collapse-v1",
        "classification": "PROVED_MATCHED_CARTIER_REDUCTION_COLLAPSES_TO_OLD_ENDPOINT_NORM",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "digit_map": "t=M-p, r=6t-p, s=(p-4t-1)/2, M=(t,1)_p, k=(r-1,0)_p",
            "Cartier": "A_(p+t,k)^plus/minus=A_(t,k)^plus/minus mod p for k<p",
            "low_digit": "A^-_(t,r-1)=-r*a_r/12 and A^+_(t,r-1)=-r*b_r/12 mod p",
            "selected_gate": "[X^(r-1)]K_M=-r*(18a_r+11z_p*b_r)/12, z_p=16^t",
            "phase_cube": "z_p^3=2^(2r+2) mod p",
            "elimination": "(18a_r)^3+(11b_r)^3*2^(2r+2)=N_r",
            "dichotomy": "retain z_p gives original gate; eliminate z_p gives Item315 old norm",
        },
        "matched_cartier_replay": matched_cartier_replay(),
        "elimination_identity_replay": elimination_identity_replay(),
        "capacity_replay": capacity_replay(),
        "capacity": {
            "raw_fixed_M_chebyshev_mass": "(2/35)M+o(M)",
            "ordinary_j2_ceiling_per_6M": "1/105",
            "each_mod6_ray_capacity_per_6M": "1/210",
            "chart_overlap": "nondegenerate and degenerate charts partition one raw interval and are not additive",
            "new_booking": 0,
            "new_capacity_reduction": 0,
        },
        "strict_labels": {
            "proved": [
                "complete one-digit Cartier reduction of both matched rational summands",
                "exact identification of the low digit with the old two-branch gate",
                "phase cube and old endpoint-norm elimination",
                "ordinary base-p digit exhaustion",
                "capacity and chart-overlap audit",
            ],
            "finite_only": [
                "seven predeclared actual rows",
                "five symbolic rational elimination controls",
                "no prime scan and no collision census",
            ],
            "open": [
                "weighted nonconcentration of the actual selected cubic component",
                "joint correlation with H_(s-1)-Theta_(r,s)",
                "selected-component reciprocity or average-gcd theorem",
                "higher p-adic information genuinely forced by the ordinary collision",
            ],
        },
        "scope_warning": (
            "The no-go covers ordinary Lucas/Dwork reduction of the two Item359 summands "
            "followed by target-free polynomial elimination. It does not close selected-root "
            "arithmetic, the moving second coordinate, or higher p-adic deformations."
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
