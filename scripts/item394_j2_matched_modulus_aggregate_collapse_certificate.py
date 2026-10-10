#!/usr/bin/env python3
"""Deterministic certificate for Item 394.

The checker reconstructs the actual target-retaining and degenerate
carriers on declared integer slices, verifies the matched-modulus/lcm
support identities, and computes the exact modulus-envelope constant.
All finite row data are diagnostic; the all-M proof is in the report.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item394_j2_matched_modulus_aggregate_collapse_certificate.json"

DEPENDENCIES = {
    "work/item334_j2_coupled_cartier_carrier_report.md":
        "a9a1b42652e5157b850014758c321ffd8a5734e4f9ea3586510ae0549822357c",
    "work/item334_j2_coupled_cartier_carrier_certificate.py":
        "b9cab6a6ddc4a0817bae5852e78473ab3144ed9a3b8985c7eacaf27629c90cce",
    "work/item334_j2_coupled_cartier_carrier_certificate.json":
        "238046186f90bdffb2e9b4c72994bac4f0c2ba7e377b42f04753b5502ea861e2",
    "work/item349_j2_degenerate_triple_minor_carrier_report.md":
        "aec5a8bc6dd8996a3578e4cbc7975afad6247ddb32d03f6deca72b97af86b50d",
    "work/item349_j2_degenerate_triple_minor_carrier_certificate.py":
        "b72b1ee335f243ae6a2761c417e27640f443183ec625027a14d5b7e06b91cf9b",
    "work/item349_j2_degenerate_triple_minor_carrier_certificate.json":
        "b26294d51b1844aeee04146004b2ecec9b6e1ff81aa271a3167e5d86c11bce44",
    "work/item355_j2_target_residual_large_sieve_obstruction_report.md":
        "ea2f5f43a14a411849bc310409939891bfb496b681b028c20fcb3b990dd3377b",
    "work/item359_j2_fixedM_cross_prime_coefficient_barrier_report.md":
        "8fc3e4a16c71aeb50f7516e5e81572ea3d7265f30104707fc988945155759a77",
    "work/item361_j2_matched_cartier_norm_collapse_report.md":
        "0ad329d64d00853fd1b8adca1c982790bd293f01bdc1ea356ad3858374683af8",
    "work/item385_j2_bounded_window_aggregate_no_go_report.md":
        "68081934a0c5f836f826e3583cef21879686a0c68db5140d4b66387f4bebbe12",
    "work/item392_j2_growing_window_aggregate_no_go_report.md":
        "9fd149b27a8ca64c727c35fca4cd8a196da0d9172883b31bb3aa75c45873bb7a",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> dict[str, str]:
    actuals: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))
        actuals[relative] = actual
    return actuals


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def gcd_many(values: Iterable[int]) -> int:
    result = 0
    for value in values:
        result = math.gcd(result, abs(value))
    return result


def lcm(left: int, right: int) -> int:
    return abs(left // math.gcd(left, right) * right)


def radical(value: int) -> int:
    value = abs(value)
    result = 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            result *= divisor
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result *= value
    return result


def largest_divisor_coprime_to(value: int, support: int) -> int:
    remaining = abs(value)
    while True:
        common = math.gcd(remaining, support)
        if common == 1:
            return remaining
        remaining //= common


def chi8(odd: int) -> int:
    if odd % 2 == 0:
        raise ValueError(odd)
    return -1 if odd % 8 in (3, 5) else 1


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


def bounds(M: int) -> tuple[int, int]:
    return ceil_div(4 * M + 3, 5), (6 * M - 1) // 7


def q_rows(M: int) -> list[int]:
    lower, upper = bounds(M)
    return [q for q in range(lower, upper + 1) if math.gcd(q, 6) == 1]


def product(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def support_product(values: Iterable[F], extra: int = 1) -> int:
    result = abs(extra)
    for value in values:
        result *= value.denominator
    return result


def extended_row(
    M: int,
    q_selected: int,
    i334: Any,
    i318: Any,
    i331: Any,
    i349: Any,
    i319: Any,
) -> dict[str, Any]:
    r = 6 * M - 7 * q_selected
    s_numerator = 5 * q_selected - 4 * M - 1
    if s_numerator % 2:
        raise AssertionError((M, q_selected, r, s_numerator))
    s = s_numerator // 2
    if r < 1 or s < 1 or r % 2 != 1 or r % 3 == 0:
        raise AssertionError((M, q_selected, r, s, "invalid integer row"))

    m = s - 1
    d_tied = r + 4
    n = 3 * m + d_tied
    q_exponent = 2 * m + d_tied

    data = i318.i250.phase_data(r)
    coeff = i318.coefficients(data)
    period = i318.actual_period(r, s, data)
    c_selected = i331.coefficient(n, q_exponent, q_selected)
    epsilon = chi8(q_selected)
    h_m = i334.h_value(m)
    correction = i334.p_correction(r + 2, m)
    phi = F(c_selected) + epsilon * h_m * correction
    base = F(9, 2) * period["kappa"] * phi
    c_value = F(2 ** (2 * s))
    f = coeff["f"]
    b = coeff["b"]
    v = coeff["d"]
    ell = coeff["ell"]
    minor_mu = coeff["m"]
    D = 9 * c_value * ell - 11 * minor_mu
    T = tuple(
        f[nu] * period["B"] * base
        + (-1) ** m * (
            f[nu] * period["B"] * period["tau"]
            - 9 * c_value * b[nu]
            + 11 * v[nu]
        )
        for nu in (0, 1)
    )
    G_raw = gcd_many((D.numerator, T[0].numerator, T[1].numerator))
    if G_raw == 0:
        raise AssertionError((M, q_selected, "zero Item334 extension carrier"))
    G_support = support_product(
        (
            *f, *b, *v,
            period["B"], period["kappa"], period["tau"],
            h_m, correction, D, T[0], T[1],
        ),
        extra=6 * math.comb(2 * m, m),
    )
    G_sat = largest_divisor_coprime_to(G_raw, G_support)

    factorization = i319.canonical_factorization(r, data)
    residue = r % 6
    index = (r - residue) // 6
    sigma = (
        i319.i314.gauge_value(residue, index)
        * i319.i314.KAPPA[residue]
        / F(16 ** index)
    )
    beta = i319.beta_closed(r)
    a_value = ell / (2 * sigma)
    b_value = -minor_mu / sigma
    K_value = factorization["K"]
    Pi_raw = gcd_many((
        a_value.numerator, b_value.numerator, K_value.numerator
    ))
    if Pi_raw == 0:
        raise AssertionError((M, q_selected, "zero Item349 extension carrier"))
    Pi_support = support_product(
        (
            *f, *b, *v, sigma, beta, a_value, b_value, K_value,
        ),
        extra=6 * math.comb(2 * m, m),
    )
    Pi_sat = largest_divisor_coprime_to(Pi_raw, Pi_support)

    d_matched = radical(math.gcd(q_selected, G_sat))
    e_matched = radical(math.gcd(q_selected, Pi_sat))
    d_deg = math.gcd(d_matched, e_matched)
    d_nd = largest_divisor_coprime_to(d_matched, e_matched)
    if d_matched != d_deg * d_nd or math.gcd(d_deg, d_nd) != 1:
        raise AssertionError((M, q_selected, d_matched, e_matched, d_deg, d_nd))

    prime = is_prime(q_selected)
    actual_collision = None
    actual_degenerate = None
    if prime:
        replay334 = i334.tied_row(i318, i331, q_selected, r, s)
        replay349 = i349.normalized_row(i319, q_selected, r, s)
        if replay334["epsilon"] != epsilon:
            raise AssertionError((q_selected, replay334["epsilon"], epsilon))
        if (G_raw % q_selected == 0) != replay334["collision"]:
            raise AssertionError((M, q_selected, G_raw, replay334["collision"]))
        if replay349[4] != Pi_raw:
            raise AssertionError((M, q_selected, Pi_raw, replay349[4]))
        actual_collision = bool(replay334["collision"])
        actual_degenerate = bool(replay349[7])
        if (G_sat % q_selected == 0) != actual_collision:
            raise AssertionError((M, q_selected, "unsafe G saturation"))
        if (Pi_sat % q_selected == 0) != actual_degenerate:
            raise AssertionError((M, q_selected, "unsafe Pi saturation"))

    return {
        "q": q_selected,
        "r": r,
        "s": s,
        "prime": prime,
        "chi8": epsilon,
        "G_raw_bits": G_raw.bit_length(),
        "G_sat_bits": G_sat.bit_length(),
        "Pi_raw": Pi_raw,
        "Pi_sat": Pi_sat,
        "d_matched": d_matched,
        "e_matched": e_matched,
        "d_nd": d_nd,
        "d_deg": d_deg,
        "actual_collision": actual_collision,
        "actual_degenerate": actual_degenerate,
    }


def primorial(limit: int) -> int:
    return product(value for value in range(2, limit + 1) if is_prime(value))


def aggregate_slice(
    M: int,
    i334: Any,
    i318: Any,
    i331: Any,
    i349: Any,
    i319: Any,
) -> dict[str, Any]:
    rows = [
        extended_row(M, q, i334, i318, i331, i349, i319)
        for q in q_rows(M)
    ]
    lower, upper = bounds(M)
    if not upper < 2 * lower:
        raise AssertionError((M, lower, upper, "narrow interval"))

    aggregate = 1
    aggregate_nd = 1
    aggregate_deg = 1
    envelope = 1
    for row in rows:
        aggregate = lcm(aggregate, row["d_matched"])
        aggregate_nd = lcm(aggregate_nd, row["d_nd"])
        aggregate_deg = lcm(aggregate_deg, row["d_deg"])
        envelope = lcm(envelope, row["q"])
    envelope = radical(envelope)
    if aggregate > 0 and envelope % aggregate:
        raise AssertionError((M, aggregate, envelope))

    low_support = primorial(lower - 1)
    sharp = largest_divisor_coprime_to(aggregate, low_support)
    sharp_nd = largest_divisor_coprime_to(aggregate_nd, low_support)
    sharp_deg = largest_divisor_coprime_to(aggregate_deg, low_support)
    collision_product = product(
        row["q"] for row in rows
        if row["prime"] and row["actual_collision"]
    )
    collision_nd_product = product(
        row["q"] for row in rows
        if row["prime"] and row["actual_collision"]
        and not row["actual_degenerate"]
    )
    collision_deg_product = product(
        row["q"] for row in rows
        if row["prime"] and row["actual_collision"]
        and row["actual_degenerate"]
    )
    if sharp != collision_product:
        raise AssertionError((M, sharp, collision_product, "exact sharp support"))
    if sharp_nd != collision_nd_product or sharp_deg != collision_deg_product:
        raise AssertionError((
            M, sharp_nd, collision_nd_product, sharp_deg,
            collision_deg_product, "chart support",
        ))
    if sharp != sharp_nd * sharp_deg or math.gcd(sharp_nd, sharp_deg) != 1:
        raise AssertionError((M, sharp, sharp_nd, sharp_deg))

    return {
        "M": M,
        "interval": [lower, upper],
        "integer_rows": len(rows),
        "prime_rows": sum(row["prime"] for row in rows),
        "collision_rows": sum(bool(row["actual_collision"]) for row in rows),
        "aggregate": aggregate,
        "aggregate_sharp": sharp,
        "aggregate_nd_sharp": sharp_nd,
        "aggregate_deg_sharp": sharp_deg,
        "envelope_radical_bits": envelope.bit_length(),
        "row_digest_sha256": hashlib.sha256(
            ("\n".join(json.dumps(row, sort_keys=True) for row in rows) + "\n")
            .encode("utf-8")
        ).hexdigest(),
        "rows": rows,
    }


def exact_constant() -> dict[str, Any]:
    alpha = F(4, 5)
    beta = F(6, 7)
    singles = (1, 5, 7, 11, 13, 17, 19, 23, 25)
    pair_starts = (29, 35, 41, 47, 53)
    constant = sum((beta - alpha) / u for u in singles)
    constant += sum(beta / u - alpha / (u + 2) for u in pair_starts)
    constant += beta / 59
    expected = F(
        6979177263689987598318,
        56080510212831201972875,
    )
    if constant != expected:
        raise AssertionError((constant, expected))

    allowed = [u for u in range(1, 10_001) if math.gcd(u, 6) == 1]
    transitions: dict[tuple[int, int], bool] = {}
    for left, right in zip(allowed, allowed[1:]):
        overlap = F(right, left) <= F(15, 14)
        if left >= 59 and not overlap:
            raise AssertionError((left, right, "tail failed to overlap"))
        if left in (55,) and overlap:
            raise AssertionError((left, right, "last gap should not overlap"))
        if left in pair_starts and not overlap:
            raise AssertionError((left, right, "declared pair failed"))
        if left in (25, 31, 37, 43, 49, 55) and overlap:
            raise AssertionError((left, right, "declared component gap failed"))
        if left in (*pair_starts, 55, 59, 61):
            transitions[(left, right)] = overlap

    return {
        "alpha": "4/5",
        "beta": "6/7",
        "single_components": list(singles),
        "pair_components": [[u, u + 2] for u in pair_starts],
        "tail_component": "(0,(6/7)/59]",
        "tail_overlap_verified_through_multiplier": 10_000,
        "declared_transitions": {
            f"{left}->{right}": overlap
            for (left, right), overlap in transitions.items()
        },
        "C6_fraction": f"{constant.numerator}/{constant.denominator}",
        "C6_decimal": float(constant),
        "C6_over_6_decimal": float(constant / 6),
        "raw_constant_2_over_35": float(F(2, 35)),
        "raw_normalized_1_over_105": float(F(1, 105)),
        "C6_over_raw_ratio": float(constant / F(2, 35)),
    }


def envelope_diagnostic(M: int) -> dict[str, Any]:
    prime_support: set[int] = set()
    for q in q_rows(M):
        value = q
        divisor = 2
        while divisor * divisor <= value:
            if value % divisor == 0:
                prime_support.add(divisor)
                while value % divisor == 0:
                    value //= divisor
            divisor = 3 if divisor == 2 else divisor + 2
        if value > 1:
            prime_support.add(value)
    log_weight = math.fsum(math.log(prime) for prime in prime_support)
    return {
        "M": M,
        "row_count": len(q_rows(M)),
        "distinct_prime_divisors": len(prime_support),
        "log_rad_lcm": log_weight,
        "log_rad_lcm_over_M": log_weight / M,
    }


def build_payload() -> dict[str, Any]:
    dependency_actuals = verify_dependencies()
    i334 = load(
        "item394_i334",
        "work/item334_j2_coupled_cartier_carrier_certificate.py",
    )
    i349 = load(
        "item394_i349",
        "work/item349_j2_degenerate_triple_minor_carrier_certificate.py",
    )
    i318 = i334.load(
        "item394_i318",
        "scripts/item318_j2_actual_period_plucker_certificate.py",
    )
    i331 = i334.load(
        "item394_i331",
        "scripts/item331_j2_global_cartier_concentration_certificate.py",
    )
    i319 = i349.load(
        "item394_i319",
        "scripts/item319_j2_third_minor_elimination_certificate.py",
    )

    slices = [
        aggregate_slice(M, i334, i318, i331, i349, i319)
        for M in (20, 35, 100, 335)
    ]
    return {
        "item": 394,
        "title": "actual ordinary-j2 matched-modulus aggregate and saturation collapse",
        "checked_date_beijing": "2026-09-01",
        "status": "proved_no_booking",
        "dependency_hashes_verified": dependency_actuals,
        "evidence_policy": {
            "finite_rows": "EXACT FINITE ONLY / DIAGNOSTIC",
            "finite_lcm_ratios": "EXACT FINITE ONLY / DIAGNOSTIC",
            "no_asymptotic_inference_from_enumeration": True,
        },
        "proved_theorems": {
            "matched_row_factor": "d_(M,q)=rad gcd(q,Ghat_(M,q))",
            "prime_independent_aggregate": "A_M=lcm_(q in Q_M) d_(M,q)",
            "safe_high_saturation": "A_M^sharp=(A_M)_((L_M-1)!)",
            "exact_support": (
                "A_M^sharp=product of all actual ordinary-j2 collision "
                "primes on the fixed-M slice"
            ),
            "chart_factorization": (
                "A_M^sharp=A_M,nd^sharp*A_M,deg^sharp with coprime factors"
            ),
            "unsaturated_envelope": "log A_M <= C6*M+o(M)",
            "C6": (
                "6979177263689987598318/"
                "56080510212831201972875"
            ),
            "sharp_height": "log A_M^sharp <= (2/35)M+o(M)",
            "equivalent_open_target": (
                "log A_M^sharp=o(M) iff W_nd(M)+W_deg(M)=o(M)"
            ),
        },
        "exact_constant_certificate": exact_constant(),
        "actual_formula_slice_replays": slices,
        "finite_envelope_diagnostics": [
            envelope_diagnostic(M) for M in (1_000, 5_000, 20_000, 100_000)
        ],
        "ledger": {
            "delta_r1": 0,
            "delta_booked_capacity": 0,
            "best_rigorous_sharp_height_per_M": "2/35",
            "ordinary_j2_raw_normalized_ceiling": "1/105",
            "strict_capacity_reduction": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / RESULT_NAME)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    if args.replay is not None:
        frozen = json.loads(args.replay.read_text(encoding="utf-8"))
        if frozen != payload:
            raise AssertionError("replay payload differs from frozen certificate")
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "item": 394,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
