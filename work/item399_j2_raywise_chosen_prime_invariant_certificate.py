#!/usr/bin/env python3
"""Deterministic certificate for Item 399.

The checker reconstructs the rational moving target, replays the
chosen-prime Jacobi reduction, verifies the selected residual after
denominator clearing, and records the exact Galois cutoff orbits and
ray-capacity arithmetic.  Finite rows are diagnostic only.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item399_j2_raywise_chosen_prime_invariant_certificate.json"

DEPENDENCIES = {
    "sources/item397_j2_matched_aggregate_factor_localization_report.md":
        "4f30aab79be7039866bbad7e71cc545bd0e553d51d1166b77cb3d5f5371476ee",
    "scripts/item397_j2_matched_aggregate_factor_localization_certificate.py":
        "f7fe2d81b31ce31fb41e77c551119ac66fa7b62fadda2691ae06036ef4426186",
    "results/item397_j2_matched_aggregate_factor_localization_certificate.json":
        "45df777a3a93c0c7e4b62dadd75da7d7231d4235b2e9efde1b5204fee43254d3",
    "sources/item341_j2_diagonal_affine_state_report.md":
        "42f6ccd326e385f8034abe322756517a30a93d7468b3e6f85cbca3dba8080cb4",
    "scripts/item341_j2_diagonal_affine_state_certificate.py":
        "2faefea6477bb74d735d82e763191bb690d970b8f6eedfd8dbda276c93ce529e",
    "results/item341_j2_diagonal_affine_state_certificate.json":
        "75c05cb486e5a5a6f9af5dda2e62f2a4b81cb888a15eb19ecabd10a382625cb4",
    "sources/item347_j2_chosen_prime_kummer_conductor_obstruction_report.md":
        "7845d01648f4860dee7cee0c12b5711693183015c99e25e923a9e49f316f5eea",
    "scripts/item347_j2_chosen_prime_kummer_conductor_obstruction_certificate.py":
        "6726a0c257beeb3fa8d231014b685691588c7c8a090d8d60e66cdfb352b04340",
    "results/item347_j2_chosen_prime_kummer_conductor_obstruction_certificate.json":
        "bd861233e0a37c6cd6e0d091d244f67e42c7bd65702d77f951e9341ad681159d",
    "sources/item349_j2_degenerate_triple_minor_carrier_report.md":
        "ca3141156cb5034012a174377c3596e22d22cae924625649b6d620d510f4790c",
    "sources/item394_j2_matched_modulus_aggregate_collapse_report.md":
        "f0fd654dc80ad3c0eab26abfd8f8741e89ba572f825ef5afd214f2c149c01204",
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


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return (
        value.numerator % prime
        * pow(value.denominator, -1, prime)
        % prime
    )


def euler_phi(value: int) -> int:
    result = value
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            result -= result // divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result -= result // remaining
    return result


def rational_target(
    prime: int,
    r: int,
    s: int,
    i318: Any,
    i331: Any,
    i334: Any,
) -> dict[str, Any]:
    m = s - 1
    data = i318.i250.phase_data(r)
    coeff = i318.coefficients(data)
    period = i318.actual_period(r, s, data)
    epsilon = i331.legendre_two(prime)
    h_m = i334.h_value(m)
    correction = i334.p_correction(r + 2, m)
    ell = coeff["ell"]
    mu = coeff["m"]
    C = coeff["C"]
    B = period["B"]
    kappa = period["kappa"]
    tau = period["tau"]
    if ell == 0:
        raise AssertionError((prime, r, s, "characteristic-zero ell zero"))
    phi_star = (
        (-1) ** (m + 1)
        * F(2, 9)
        / kappa
        * (tau - 11 * C / (ell * B))
    )
    theta = h_m * correction + epsilon * (1 - phi_star)
    H = i347_h_prefix(m)
    D = 9 * F(4 ** s) * ell - 11 * mu
    if theta.denominator % prime == 0:
        raise AssertionError((prime, r, s, "target denominator not a unit"))
    selected_residual = (
        theta.denominator * H.numerator * pow(H.denominator, -1, prime)
        - theta.numerator
    ) % prime
    if selected_residual != (
        theta.denominator * fmod(H - theta, prime)
    ) % prime:
        raise AssertionError((prime, r, s, selected_residual))
    return {
        "theta": theta,
        "H": H,
        "D": D,
        "selected_residual": selected_residual,
        "ell_mod_p": fmod(ell, prime),
        "D_mod_p": fmod(D, prime),
    }


# Bound after loading Item347.  This keeps rational_target's signature compact.
i347_h_prefix = None


def cutoff_orbit(prime: int, m: int) -> dict[str, Any]:
    N = prime - 1
    base = tuple(range(m + 1))
    units = [a for a in range(1, N) if math.gcd(a, N) == 1]
    cutoff_sets = {
        tuple(sorted((a * u) % N for u in base))
        for a in units
    }
    actual = tuple(base)
    if actual not in cutoff_sets:
        raise AssertionError((prime, m, "actual cutoff absent"))
    degree = euler_phi(N)
    if degree != len(units):
        raise AssertionError((prime, degree, len(units)))
    return {
        "N": N,
        "m": m,
        "cyclotomic_degree": degree,
        "galois_multipliers": len(units),
        "distinct_cutoff_sets": len(cutoff_sets),
        "actual_cutoff_size": len(base),
        "orbit_digest_sha256": hashlib.sha256(
            ("\n".join(",".join(map(str, row)) for row in sorted(cutoff_sets))
             + "\n").encode("ascii")
        ).hexdigest(),
    }


def actual_replay() -> dict[str, Any]:
    global i347_h_prefix
    i341 = load(
        "item399_i341",
        "scripts/item341_j2_diagonal_affine_state_certificate.py",
    )
    i347 = load(
        "item399_i347",
        "scripts/item347_j2_chosen_prime_kummer_conductor_obstruction_certificate.py",
    )
    i318 = i341.load(
        "item399_i318",
        "scripts/item318_j2_actual_period_plucker_certificate.py",
    )
    i331 = i341.load(
        "item399_i331",
        "scripts/item331_j2_global_cartier_concentration_certificate.py",
    )
    i334 = i341.load(
        "item399_i334",
        "scripts/item334_j2_coupled_cartier_carrier_certificate.py",
    )
    i347_h_prefix = i347.h_prefix

    kummer = i347.actual_rows_replay()
    target_rows = i347.load_item341_targets()
    replay_rows = []
    orbits = []
    for raw in kummer["rows"]:
        prime, r, s, m, M = map(int, raw[:5])
        H_mod = int(raw[6])
        theta_mod = int(raw[7])
        target_complete = int(raw[9])
        data = rational_target(prime, r, s, i318, i331, i334)
        if fmod(data["H"], prime) != H_mod:
            raise AssertionError((prime, "H mismatch"))
        if fmod(data["theta"], prime) != theta_mod:
            raise AssertionError((prime, "theta mismatch"))
        if data["selected_residual"] != (
            data["theta"].denominator * target_complete
        ) % prime:
            raise AssertionError((prime, "cleared Xi reduction mismatch"))
        if target_rows[(prime, r, s)][3] != theta_mod:
            raise AssertionError((prime, "Item341 target mismatch"))
        ray = r % 6
        if (ray, prime % 6) not in ((1, 5), (5, 1)):
            raise AssertionError((prime, r, ray))
        replay_rows.append({
            "p": prime,
            "r": r,
            "s": s,
            "m": m,
            "M": M,
            "ray_r_mod_6": ray,
            "p_mod_6": prime % 6,
            "theta_numerator_bits": abs(data["theta"].numerator).bit_length(),
            "theta_denominator_bits": data["theta"].denominator.bit_length(),
            "theta_denominator_mod_p": data["theta"].denominator % prime,
            "D_mod_p": data["D_mod_p"],
            "H_minus_theta_mod_p": target_complete,
            "Xi_reduction_mod_p": data["selected_residual"],
        })
        orbits.append({
            "p": prime,
            **cutoff_orbit(prime, m),
        })
    return {
        "classification": "EXACT FINITE ONLY / DIAGNOSTIC",
        "kummer_source_digest": kummer["row_digest_sha256"],
        "rows": replay_rows,
        "galois_cutoff_orbits": orbits,
        "row_digest_sha256": hashlib.sha256(
            ("\n".join(json.dumps(row, sort_keys=True) for row in replay_rows)
             + "\n").encode("utf-8")
        ).hexdigest(),
    }


def capacity_certificate() -> dict[str, Any]:
    full = F(2, 35)
    ray = F(1, 35)
    normalized_ray = ray / 6
    half_ray = ray / 2
    if normalized_ray != F(1, 210):
        raise AssertionError(normalized_ray)
    return {
        "full_ordinary_mass_per_M": "2/35",
        "one_ray_mass_per_M": "1/35",
        "one_ray_normalized_per_6M": "1/210",
        "half_ray_eta_per_M": "1/70",
        "half_ray_normalized_saving": "1/420",
        "both_rays_normalized": "1/105",
        "decimal": {
            "one_ray_mass_per_M": float(ray),
            "one_ray_normalized": float(normalized_ray),
            "half_ray_eta_per_M": float(half_ray),
        },
        "chart_warning": (
            "nondegenerate o(M) alone has zero fixed booking without "
            "a complementary degenerate-chart upper bound"
        ),
    }


def build_payload() -> dict[str, Any]:
    dependency_actuals = verify_dependencies()
    return {
        "item": 399,
        "title": "ordinary-j2 raywise chosen-prime collision invariant",
        "checked_date_beijing": "2026-09-01",
        "status": "minimal_invariant_isolated_no_booking",
        "dependency_hashes_verified": dependency_actuals,
        "evidence_policy": {
            "finite_rows_and_character_sums": (
                "EXACT FINITE ONLY / DIAGNOSTIC"
            ),
            "no_asymptotic_inference_from_enumeration": True,
        },
        "proved_theorems": {
            "chosen_prime_integer": (
                "Xi=-Q*sum_(u=0)^m B_u(2)J(B_u,phi)-A in O_(Q(mu_(p-1)))"
            ),
            "selected_reduction": (
                "Xi mod P_p = Q*(H_m-Theta_(r,s))"
            ),
            "nondegenerate_collision_ideal": (
                "collision iff p|E_(p,r,s) and P_p|Xi_(p,r,s)"
            ),
            "galois_action": (
                "sigma_a sends cutoff {0,...,m} to a*{0,...,m} mod p-1"
            ),
            "norm_implication_only": (
                "P_p|Xi implies p|Norm(Xi); converse loses selected prime/cutoff"
            ),
            "norm_height": "log^+|Norm(Xi)|=O(M^2 log M) per row",
            "proved_eta": 0,
        },
        "actual_chosen_prime_replay": actual_replay(),
        "capacity_certificate": capacity_certificate(),
        "minimal_missing_theorems": {
            "nondegenerate": (
                "weighted chosen-prime nonconcentration for the ideal (E,Xi)"
            ),
            "degenerate": (
                "weighted moving-divisor theorem for Pi_hat plus the "
                "surviving Item334 target coordinate"
            ),
            "full_ray": "both chart bounds are required for a 1/210 saving",
        },
        "ledger": {
            "eta_per_M": 0,
            "delta_r1": 0,
            "delta_booked_capacity": 0,
            "ordinary_j2_raw_normalized_ceiling": "1/105",
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
        "item": 399,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
