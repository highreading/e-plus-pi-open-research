#!/usr/bin/env python3
"""Deterministic certificate for Item 349.

The checker reconstructs the three normalized connection minors, their
r-only primitive gcd carrier, connection-denominator saturation, exact
internal chart split, and fixed-M parameter identities on declared
actual rows.  It performs no prime or collision census.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item349_j2_degenerate_triple_minor_carrier_certificate.json"

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
    "sources/item319_j2_third_minor_elimination_report.md":
        "75b4a3303e3cd216aebeb5189d8c97ef20f261bfd8ea400638214e96a0cc25a0",
    "scripts/item319_j2_third_minor_elimination_certificate.py":
        "d5d283930062c6de55e0c338a152cc96502b72f62cc9f74af0623247307d91f7",
    "results/item319_j2_third_minor_elimination_certificate.json":
        "c4ce360823dd2d781bebc492e79b65d6ea183a7dada1d4cbee1b1c37334ec194",
    "results/item319_j2_third_minor_elimination_root_audit.json":
        "73c5418a83e8aff962993e0d3358e65122471ff98e4e174835b85222bb159a8c",
    "manifests/item319_j2_third_minor_elimination_manifest.json":
        "1795f625a0f8f26a51670a73635624c17c37d9fc01c810abe4dcc52ae535a174",
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


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def largest_divisor_coprime_to(value: int, support: int) -> int:
    remaining = abs(value)
    while True:
        common = math.gcd(remaining, support)
        if common == 1:
            return remaining
        remaining //= common


def normalized_row(i319: Any, prime: int, r: int, s: int) -> tuple[Any, ...]:
    if prime != 2 * r + 6 * s + 3:
        raise AssertionError((prime, r, s, "tied phase"))
    if r % 2 != 1 or r % 3 == 0:
        raise AssertionError((prime, r, s, "ordinary r"))

    data = i319.i250.phase_data(r)
    factorization = i319.canonical_factorization(r, data)
    f = tuple(data["st"])
    b = (data["x0"][1], data["x1"][1])
    v = (data["x0"][2], data["x1"][2])
    ell = i319.det(f, b)
    mu = i319.det(f, v)
    C = i319.det(b, v)

    residue = r % 6
    index = (r - residue) // 6
    sigma = (
        i319.i314.gauge_value(residue, index)
        * i319.i314.KAPPA[residue]
        / F(16 ** index)
    )
    beta = i319.beta_closed(r)
    a_value = ell / (2 * sigma)
    b_value = -mu / sigma
    K = factorization["K"]

    # Item 315 proves this on both complete rays by a sign-preserving
    # four-term recurrence.  The declared replay checks compatibility,
    # while the all-r induction is written in the report.
    if not a_value < 0:
        raise AssertionError((prime, r, s, a_value, "all-ray a_r sign"))

    if ell != 2 * sigma * a_value or mu != -sigma * b_value or C != beta * K:
        raise AssertionError((prime, r, s, "normalized minor factorization"))

    normalized = [a_value, b_value, K]
    audited = [*f, *b, *v, sigma, beta, *normalized]
    if any(value.denominator % prime == 0 for value in audited):
        raise AssertionError((prime, r, s, "nonunit denominator"))
    if fmod(sigma, prime) == 0 or fmod(beta, prime) == 0:
        raise AssertionError((prime, r, s, "nonunit compulsory scale"))

    carrier = math.gcd(
        abs(a_value.numerator),
        math.gcd(abs(b_value.numerator), abs(K.numerator)),
    )
    if carrier == 0:
        raise AssertionError((prime, r, s, "zero carrier"))
    triple_zero = all(fmod(value, prime) == 0 for value in (ell, mu, C))
    normalized_zero = all(fmod(value, prime) == 0 for value in normalized)
    if triple_zero != normalized_zero or triple_zero != (carrier % prime == 0):
        raise AssertionError((prime, r, s, carrier, "carrier equivalence"))

    f_zero = all(fmod(value, prime) == 0 for value in f)
    ab_zero = fmod(a_value, prime) == 0 and fmod(b_value, prime) == 0
    K_zero = fmod(K, prime) == 0
    split_condition = ((not f_zero) and ab_zero) or (f_zero and K_zero)
    if triple_zero != split_condition:
        raise AssertionError((prime, r, s, f_zero, ab_zero, K_zero, "chart split"))

    A_carrier = math.gcd(abs(a_value.numerator), abs(b_value.numerator))
    F_carrier = math.gcd(abs(f[0].numerator), abs(f[1].numerator))
    FK_carrier = math.gcd(F_carrier, abs(K.numerator))
    integer_split = (
        (F_carrier % prime != 0 and A_carrier % prime == 0)
        or FK_carrier % prime == 0
    )
    if triple_zero != integer_split:
        raise AssertionError((prime, r, s, A_carrier, F_carrier, FK_carrier, "integer split"))

    connection_support = 6
    for value in (*f, *b, *v):
        connection_support *= value.denominator
    saturated = largest_divisor_coprime_to(carrier, connection_support)
    if connection_support % prime == 0:
        raise AssertionError((prime, r, s, "connection saturation removed tied prime"))
    if (carrier % prime == 0) != (saturated % prime == 0):
        raise AssertionError((prime, r, s, carrier, saturated, "saturation equivalence"))

    M_numerator = 5 * r + 14 * s + 7
    if M_numerator % 2:
        raise AssertionError((prime, r, s, "nonintegral M"))
    M = M_numerator // 2
    reconstructed_r = 6 * M - 7 * prime
    reconstructed_s_numerator = 5 * prime - 4 * M - 1
    if reconstructed_s_numerator % 2:
        raise AssertionError((prime, r, s, M, "nonintegral reconstructed s"))
    reconstructed_s = reconstructed_s_numerator // 2
    if (reconstructed_r, reconstructed_s) != (r, s):
        raise AssertionError((prime, r, s, M, reconstructed_r, reconstructed_s))

    return (
        prime,
        r,
        s,
        M,
        carrier,
        math.gcd(carrier, connection_support),
        saturated,
        int(triple_zero),
        int(f_zero),
        int(ab_zero),
        int(K_zero),
        A_carrier % prime,
        F_carrier % prime,
        FK_carrier % prime,
        hashlib.sha256(
            (",".join(str(value.denominator) for value in (*f, *b, *v)) + "\n").encode("ascii")
        ).hexdigest(),
    )


def actual_rows_replay(i319: Any) -> dict[str, Any]:
    declared = [
        (11, 1, 1),
        (17, 1, 2),
        (29, 1, 4),
        (251, 121, 1),
        (313, 149, 2),
        (347, 157, 5),
    ]
    rows = [normalized_row(i319, *row) for row in declared]
    special = next(row for row in rows if row[0:3] == (251, 121, 1))
    if special[4:7] != (7, 7, 1):
        raise AssertionError((special, "declared saturation witness"))
    return {
        "classification": "EXACT FINITE REPLAY ONLY - NO PRIME OR COLLISION CENSUS",
        "declared_rows": len(rows),
        "rows": rows,
        "saturation_witness": {
            "row": [251, 121, 1],
            "raw_normalized_carrier": 7,
            "connection_denominator_gcd": 7,
            "connection_saturated_carrier": 1,
        },
        "row_digest_sha256": digest_rows(rows),
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    i319 = load("item349_i319", "scripts/item319_j2_third_minor_elimination_certificate.py")
    return {
        "schema": "item349-j2-degenerate-triple-minor-carrier-v1",
        "classification": "PROVED_EXACT_DEGENERATE_CARRIER_AND_HEIGHT_PRODUCT_NO_GO",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "minor_normalization": "ell=2*sigma*a_r, mu=-sigma*b_r, C=beta*K_r",
            "primitive_carrier": "Pi_r=gcd(abs(num(a_r)),abs(num(b_r)),abs(num(K_r)))",
            "carrier_nonzero": "Item315 all-ray sign theorem a_r<0 implies Pi_r>=1 on every admissible row",
            "carrier_equivalence": "ell=mu=C=0 mod p iff p divides Pi_r",
            "safe_saturation": "p divides Pi_r iff p divides (Pi_r)_(S_(r,s))",
            "nonzero_f_chart": "if f!=0, triple vanishing iff a_r=b_r=0",
            "zero_f_chart": "if f=0, triple vanishing iff K_r=0",
            "fixed_M": "r=6M-7p and s=(5p-4M-1)/2",
            "height": "log^+(Pi_r)=O(r log r); aggregate raw product is O(M^2 log M)",
        },
        "actual_rows_replay": actual_rows_replay(i319),
        "capacity": {
            "raw_ordinary_j2_chebyshev_mass": "(2/35)M+o(M)",
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "overlap_rule": "degenerate and nondegenerate charts partition the same raw interval; capacities are not additive",
            "new_capacity_reduction": 0,
            "new_booking": 0,
        },
        "closed_method_class": [
            "individual carrier-height bounds",
            "the raw product of r-only carriers over a fixed-M slice",
            "recurrence or D-finiteness without modular zero-density",
        ],
        "open": [
            "o(M) weighted support for p dividing the safely saturated moving carrier",
            "an average-gcd theorem for (a_r,b_r,K_r)",
            "a good-reduction theorem forcing the saturated carrier to one or to small-prime support",
            "separate weighted theorems for the f-nonzero and f-zero branches",
        ],
        "scope_warning": (
            "The carrier is an exact necessary gate for the degenerate chart, not a sufficient original-collision test. "
            "The declared rows validate formulas and one foreign-factor saturation witness only."
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
