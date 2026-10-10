#!/usr/bin/env python3
"""Deterministic certificate for Item 334.

The checker retains the old determinant gate and the moving connection
target.  It verifies the Cartier-target substitution, all chart formulas,
primitive numerator clearing, and the exact rowwise gcd carrier.  Bounded
row counts are finite diagnostics only; the symbolic proofs and height
audit are in the companion report.
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
RESULT_NAME = "item334_j2_coupled_cartier_carrier_certificate.json"

DEPENDENCIES = {
    "sources/item318_j2_actual_period_plucker_report.md":
        "e89f4892b3c2b9b999321de0ec6973547903b755f07b0d34be7f0da634ecd4db",
    "scripts/item318_j2_actual_period_plucker_certificate.py":
        "334bade7313a2fb750874dfd53216cd5f1028afbc837473cdd19b365ca820e82",
    "results/item318_j2_actual_period_plucker_certificate.json":
        "75e84016af2c7580f1954f795ed080d25083345578558aae49f6df4253891fd7",
    "sources/item319_j2_third_minor_elimination_report.md":
        "75b4a3303e3cd216aebeb5189d8c97ef20f261bfd8ea400638214e96a0cc25a0",
    "results/item319_j2_third_minor_elimination_certificate.json":
        "c4ce360823dd2d781bebc492e79b65d6ea183a7dada1d4cbee1b1c37334ec194",
    "sources/item331_j2_global_cartier_concentration_report.md":
        "b721b9469b500a8b8fb5f6c0c0702f92015198264a7c6f931acaabd82796ee08",
    "scripts/item331_j2_global_cartier_concentration_certificate.py":
        "726157af0f7250c42c3594bb45f08074375e4eb5d1e9843cad37f3def85e27ba",
    "results/item331_j2_global_cartier_concentration_certificate.json":
        "08739a4a4061d5b9d78328aa52b6355711657d75259a133660a3181404f640b2",
    "manifests/item331_j2_global_cartier_concentration_manifest.json":
        "bdb026beb24ae1b97cf69c8c6ee062594620ed27e451bb8e91d0f9886b9b45fb",
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


def det(left: tuple[F, F], right: tuple[F, F]) -> F:
    return left[0] * right[1] - left[1] * right[0]


def h_value(m: int) -> F:
    return F(math.comb(2 * m, m), 8 ** m)


def p_correction(length: int, m: int) -> F:
    """P_length(m) from Item 251/252, computed exactly."""
    term = F(1)
    total = F(0)
    for k in range(1, length + 1):
        term *= F(2 * m + 2 * k - 1, 2 * (2 * k - 1))
        total += term
    return total


def gcd_many(values: Iterable[int]) -> int:
    result = 0
    for value in values:
        result = math.gcd(result, abs(value))
    return result


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def algebra_replay() -> dict[str, Any]:
    rows = []
    tests = [
        ((F(1), F(2)), (F(3), F(5)), (F(7), F(11)), F(13), F(17), 0),
        ((F(2), F(-1)), (F(4), F(3)), (F(-5), F(8)), F(-7), F(9), 1),
        ((F(0), F(1)), (F(1), F(0)), (F(2), F(0)), F(5), F(-3), 4),
    ]
    for f, b, d_vector, base, tau, m in tests:
        sign = (-1) ** (m + 1)
        c_value = F(2 ** (2 * (m + 1)))
        B = F(5, 7)
        ell, minor_m, C = det(f, b), det(f, d_vector), det(b, d_vector)
        W = B * (sign * base - tau)
        g = (
            f[0] * W + 9 * c_value * b[0] - 11 * d_vector[0],
            f[1] * W + 9 * c_value * b[1] - 11 * d_vector[1],
        )
        T = tuple(
            f[nu] * B * base
            + (-1) ** m * (f[nu] * B * tau - 9 * c_value * b[nu] + 11 * d_vector[nu])
            for nu in (0, 1)
        )
        if T != (sign * g[0], sign * g[1]):
            raise AssertionError((f, b, d_vector, base, tau, m, "coordinate identity"))
        T_ell = ell * B * base + (-1) ** m * (ell * B * tau - 11 * C)
        T_minor_m = minor_m * B * base + (-1) ** m * (minor_m * B * tau - 9 * c_value * C)
        if T_ell != det(T, b) or T_minor_m != det(T, d_vector):
            raise AssertionError((f, b, d_vector, "exterior target identity"))
        D = 9 * c_value * ell - 11 * minor_m
        if det(f, T) != sign * D:
            raise AssertionError((f, b, d_vector, "determinant identity"))
        if 11 * T_minor_m - 9 * c_value * T_ell != -D * sign * W:
            raise AssertionError((f, b, d_vector, "target syzygy"))
        rows.append((m, T[0], T[1], T_ell, T_minor_m, D))
    return {
        "classification": "SYMBOLIC EXACT RATIONAL IDENTITIES",
        "generic_rows": len(rows),
        "identity_checks": 12,
        "row_digest_sha256": digest_rows(rows),
    }


def chart_name(ell: int, minor_m: int, C: int, f: tuple[int, int]) -> str:
    if ell != 0:
        return "ell_nonzero"
    if minor_m != 0:
        return "m_nonzero"
    if C != 0:
        return "f_zero_b_d_independent"
    if f != (0, 0):
        return "rank_at_most_one_f_nonzero"
    return "rank_at_most_one_f_zero"


def tied_row(i318: Any, i331: Any, prime: int, r: int, s: int) -> dict[str, Any]:
    m = s - 1
    d_tied = r + 4
    n = 3 * m + d_tied
    q = 2 * m + d_tied
    M = (5 * r + 14 * s + 7) // 2
    if prime != 2 * r + 6 * s + 3 or prime != 6 * m + 2 * d_tied + 1:
        raise AssertionError((prime, r, s, m, d_tied, "tied phase"))
    if prime != (6 * M - r) // 7 or 5 * prime != 4 * M + 2 * m + 3:
        raise AssertionError((prime, r, s, M, m, "fixed-M map"))
    if not (5 * prime > 4 * M and 7 * prime < 6 * M):
        raise AssertionError((prime, M, "fixed-M prime interval"))

    data = i318.i250.phase_data(r)
    coeff = i318.coefficients(data)
    period = i318.actual_period(r, s, data)
    phase = i318.i250.evaluate_phase_row(prime, s, data)

    c_p = i331.coefficient(n, q, prime)
    epsilon = i331.legendre_two(prime)
    h_m = h_value(m)
    P = p_correction(r + 2, m)
    base = F(9, 2) * period["kappa"] * (F(c_p) + epsilon * h_m * P)
    sign = (-1) ** (m + 1)
    W = period["B"] * (sign * base - period["tau"])
    if fmod(W, prime) != fmod(period["Z"], prime):
        raise AssertionError((prime, r, s, "Cartier target substitution"))

    f = coeff["f"]
    b = coeff["b"]
    d_vector = coeff["d"]
    ell = coeff["ell"]
    minor_m = coeff["m"]
    C = coeff["C"]
    c_value = F(2 ** (2 * s))
    D = 9 * c_value * ell - 11 * minor_m
    G_c = tuple(
        f[nu] * W + 9 * c_value * b[nu] - 11 * d_vector[nu]
        for nu in (0, 1)
    )
    T = tuple(
        f[nu] * period["B"] * base
        + (-1) ** m * (
            f[nu] * period["B"] * period["tau"]
            - 9 * c_value * b[nu]
            + 11 * d_vector[nu]
        )
        for nu in (0, 1)
    )
    if T != (sign * G_c[0], sign * G_c[1]):
        raise AssertionError((prime, r, s, "coordinate target identity"))

    T_ell = (
        ell * period["B"] * base
        + (-1) ** m * (ell * period["B"] * period["tau"] - 11 * C)
    )
    T_minor_m = (
        minor_m * period["B"] * base
        + (-1) ** m * (
            minor_m * period["B"] * period["tau"] - 9 * c_value * C
        )
    )
    if T_ell != det(T, b) or T_minor_m != det(T, d_vector):
        raise AssertionError((prime, r, s, "exterior target identity"))
    if det(f, T) != sign * D:
        raise AssertionError((prime, r, s, "determinant target identity"))

    residues = {
        "f": tuple(fmod(value, prime) for value in f),
        "ell": fmod(ell, prime),
        "m": fmod(minor_m, prime),
        "C": fmod(C, prime),
        "D": fmod(D, prime),
        "T0": fmod(T[0], prime),
        "T1": fmod(T[1], prime),
        "T_ell": fmod(T_ell, prime),
        "T_m": fmod(T_minor_m, prime),
    }
    if residues["T0"] != sign * phase["g0"] % prime:
        raise AssertionError((prime, r, s, "T0 versus actual collision"))
    if residues["T1"] != sign * phase["g1"] % prime:
        raise AssertionError((prime, r, s, "T1 versus actual collision"))
    if residues["D"] != phase["linear"]:
        raise AssertionError((prime, r, s, "old determinant gate"))

    rationals = [D, T[0], T[1], T_ell, T_minor_m, W, h_m, P]
    if any(value.denominator % prime == 0 for value in rationals):
        raise AssertionError((prime, r, s, "nonunit denominator"))
    carrier = gcd_many((D.numerator, T[0].numerator, T[1].numerator))
    if carrier == 0:
        raise AssertionError((prime, r, s, "zero carrier"))
    collision = phase["g0"] == 0 and phase["g1"] == 0
    if (carrier % prime == 0) != collision:
        raise AssertionError((prime, r, s, carrier % prime, collision, "gcd carrier"))

    chart = chart_name(
        residues["ell"], residues["m"], residues["C"], residues["f"]
    )
    if residues["D"] == 0:
        if chart == "ell_nonzero" and (residues["T_ell"] == 0) != collision:
            raise AssertionError((prime, r, s, chart, "ell chart"))
        if chart == "m_nonzero" and (residues["T_m"] == 0) != collision:
            raise AssertionError((prime, r, s, chart, "m chart"))
        if chart == "f_zero_b_d_independent" and collision:
            raise AssertionError((prime, r, s, chart, "impossible chart"))
        if chart == "rank_at_most_one_f_nonzero":
            nu = 0 if residues["f"][0] != 0 else 1
            if (residues[f"T{nu}"] == 0) != collision:
                raise AssertionError((prime, r, s, chart, nu, "rank-one coordinate"))

    return {
        "p": prime,
        "r": r,
        "s": s,
        "M": M,
        "m_index": m,
        "d_tied": d_tied,
        "epsilon": epsilon,
        "chart": chart,
        "determinant_hit": residues["D"] == 0,
        "collision": collision,
        "c_p_bits": abs(c_p).bit_length(),
        "T0_numerator_bits": abs(T[0].numerator).bit_length(),
        "T1_numerator_bits": abs(T[1].numerator).bit_length(),
        "carrier_bits": carrier.bit_length(),
        "carrier_mod_p": carrier % prime,
        "T0_mod_p": residues["T0"],
        "T1_mod_p": residues["T1"],
        "D_mod_p": residues["D"],
    }


def finite_replay(i318: Any, i331: Any, prime_max: int) -> dict[str, Any]:
    declared = list(i331.actual_rows(prime_max))
    # Retain the three small old determinant hits even when above the cap.
    extras = [(271, 113, 7), (367, 65, 39), (383, 109, 27)]
    seen = set(declared)
    for row in extras:
        if row not in seen:
            declared.append(row)
            seen.add(row)

    rows = []
    charts: dict[str, int] = {}
    determinant_hits = []
    collision_rows = []
    max_bits = {"c_p": 0, "T0": 0, "T1": 0, "carrier": 0}
    fixed_M_counts: dict[int, int] = {}
    for prime, r, s in declared:
        row = tied_row(i318, i331, prime, r, s)
        charts[row["chart"]] = charts.get(row["chart"], 0) + 1
        fixed_M_counts[row["M"]] = fixed_M_counts.get(row["M"], 0) + 1
        if row["determinant_hit"]:
            determinant_hits.append((
                row["p"], row["r"], row["s"], row["M"], row["chart"],
                row["T0_mod_p"], row["T1_mod_p"], row["carrier_mod_p"],
            ))
        if row["collision"]:
            collision_rows.append((row["p"], row["r"], row["s"], row["M"]))
        max_bits["c_p"] = max(max_bits["c_p"], row["c_p_bits"])
        max_bits["T0"] = max(max_bits["T0"], row["T0_numerator_bits"])
        max_bits["T1"] = max(max_bits["T1"], row["T1_numerator_bits"])
        max_bits["carrier"] = max(max_bits["carrier"], row["carrier_bits"])
        rows.append((
            row["p"], row["r"], row["s"], row["M"], row["m_index"],
            row["d_tied"], row["epsilon"], row["chart"], row["D_mod_p"],
            row["T0_mod_p"], row["T1_mod_p"], row["carrier_mod_p"],
            row["c_p_bits"], row["T0_numerator_bits"],
            row["T1_numerator_bits"], row["carrier_bits"],
        ))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "prime_max_inclusive_for_full_census": prime_max,
        "explicit_old_gate_hits_added": extras,
        "rows": len(rows),
        "chart_counts": charts,
        "determinant_hits": determinant_hits,
        "collision_rows": collision_rows,
        "fixed_M_slices": len(fixed_M_counts),
        "largest_rows_in_one_fixed_M_slice": max(fixed_M_counts.values(), default=0),
        "maximum_bit_lengths": max_bits,
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:10],
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    i318 = load("item334_i318", "scripts/item318_j2_actual_period_plucker_certificate.py")
    i331 = load("item334_i331", "scripts/item331_j2_global_cartier_concentration_certificate.py")
    return {
        "schema": "item334-j2-coupled-cartier-carrier-v1",
        "classification": "PROVED_COUPLED_TARGET_AND_EXACT_ROWWISE_INTEGER_CARRIER",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "parameters": {"prime_max_inclusive": args.prime_max},
        "proved_formulae": {
            "cartier_target": (
                "W=B_s*((-1)^(m+1)*(9*kappa_r/2)*(c_p+epsilon*h_m*P_(r+2)(m))-tau_(r,s))"
            ),
            "coordinate_target": (
                "T_nu=(9*kappa_r/2)*f_nu*B_s*(c_p+epsilon*h_m*P)+"
                "(-1)^m*(f_nu*B_s*tau-9*c*b_nu+11*d_nu)"
            ),
            "coordinate_equivalence": "T_nu=(-1)^(m+1)*G_nu(W)",
            "ell_target": (
                "T_ell=(9*kappa_r/2)*ell*B_s*(c_p+epsilon*h_m*P)+"
                "(-1)^m*(ell*B_s*tau-11*C)"
            ),
            "m_target": (
                "T_m=(9*kappa_r/2)*m_minor*B_s*(c_p+epsilon*h_m*P)+"
                "(-1)^m*(m_minor*B_s*tau-9*c*C)"
            ),
            "row_carrier": "gcd(num(D),num(T_0),num(T_1))",
        },
        "algebra_replay": algebra_replay(),
        "finite_replay": finite_replay(i318, i331, args.prime_max),
        "height_and_capacity": {
            "proved_pointwise_log_height": "O(M log M)",
            "proved_aggregate_product_bound": "O(M^2 log M)",
            "required_aggregate_bound": "o(M)",
            "average_gcd_improvement": "OPEN",
            "new_booking": 0,
            "new_capacity_reduction": 0,
            "ordinary_j2_ceiling_per_6M": "1/105",
        },
        "scope_warning": (
            "The finite carrier census is diagnostic.  No sublinear height, average-gcd, "
            "or weighted-zero-density theorem is inferred from it."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime-max", type=int, default=199)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.prime_max < 11:
        raise ValueError("prime cap must be at least 11")
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
