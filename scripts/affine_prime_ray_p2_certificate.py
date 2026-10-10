#!/usr/bin/env python3
"""Certificate for a uniform e=1 congruence slab, including 9p=10m+1.

The uniform proof is the support calculation recorded in the companion note.
This script checks that algebra for every prime below a requested bound and
independently evaluates the item-161 Hasse digit on a bounded family sample.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
EXTENDED_PATH = HERE / "lifted_endpoint_hasse_extended_certificate.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n, flag in enumerate(sieve) if flag]


def family_member(p: int, ell: int) -> dict[str, Any]:
    if p % 20 != 19:
        raise ValueError(p)
    k = (p - 19) // 20
    m0 = 18 * k + 17
    m = m0 + ell * p
    n, k0 = 6 * m, 4 * m + 1
    a, r = divmod(n, p)
    b, t = divmod(k0, p)
    q_exponent_p0 = p - t
    q_exponent_p1 = p - t - 1
    target_offset = p - 1 - r
    degree_p0 = 5 * r
    degree_p1 = 5 * r - 3
    checks = {
        "congruence_identity": 10 * m + 1 == (10 * ell + 9) * p,
        "base_affine_identity": 9 * p == 10 * m0 + 1,
        "a_equals_5_plus_6ell": a == 5 + 6 * ell,
        "b_equals_3_plus_4ell": b == 3 + 4 * ell,
        "r_equals_8k_plus_7": r == 8 * k + 7,
        "t_equals_12k_plus_12": t == 12 * k + 12,
        "P0_Q_exponent_equals_r": q_exponent_p0 == r,
        "P1_Q_exponent_equals_r_minus_1": q_exponent_p1 == r - 1,
        "target_offset_is_3_mod_4": target_offset % 4 == 3,
        "gamma0_support_excludes_target": target_offset % 4 != 0,
        "gamma1_support_excludes_target": target_offset % 4 not in (0, 1),
        "degree_P0_equals_2p_minus_3": degree_p0 == 2 * p - 3,
        "degree_P1_equals_2p_minus_6": degree_p1 == 2 * p - 6,
        "rank_one_degree_bound": max(degree_p0, degree_p1) <= 2 * p - 2,
        "not_forced_rank_zero": degree_p0 > p - 2,
        "top_layer_is_p": p <= k0 < p * p,
        "small_prime_condition": p < 2 * m,
        "Bockstein_integrality_safe": b + 1 <= p - 1,
    }
    if not all(checks.values()):
        raise AssertionError((p, checks))
    return {
        "k": k, "ell": ell, "m0": m0, "m": m, "p": p,
        "N": n, "K0": k0,
        "a": a, "b": b, "r": r, "t": t,
        "degree_P0": degree_p0, "degree_P1": degree_p1,
        "target_offset": target_offset,
        "gamma0": 0, "gamma1": 0,
        "checks": checks,
    }


def prime_record(p: int) -> dict[str, Any]:
    if p % 20 != 19:
        raise ValueError(p)
    k = (p - 19) // 20
    m0 = 18 * k + 17
    # K0=4m+1 must be strictly below p^2.  The -2 converts the strict
    # integer inequality 4(m0+ell*p)+1 < p^2 into an inclusive floor.
    ell_max = (p * p - 4 * m0 - 2) // (4 * p)
    if ell_max < 0:
        raise AssertionError((p, m0, ell_max))
    # This finite replay checks every member in the complete e=1 band for
    # each sampled prime.  Only the endpoints are serialized because the
    # identities are affine in ell and the full list is unnecessarily large.
    checked_members = [family_member(p, ell) for ell in range(ell_max + 1)]
    first = checked_members[0]
    last = checked_members[-1]
    return {
        "p": p,
        "k": k,
        "m0": m0,
        "ell_min": 0,
        "ell_max": ell_max,
        "family_member_count": ell_max + 1,
        "all_family_members_checked": True,
        "first_member": first,
        "last_member": last,
    }


def load_extended() -> Any:
    spec = importlib.util.spec_from_file_location("item162_extended", EXTENDED_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(EXTENDED_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.base.local_coefficients = module.local_coefficients_fast
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbolic-prime-bound", type=int, default=5000)
    parser.add_argument("--hasse-prime-bound", type=int, default=500)
    parser.add_argument("--hasse-max-m", type=int, default=500)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    symbolic_records = [
        prime_record(p) for p in primes_upto(args.symbolic_prime_bound) if p % 20 == 19
    ]

    extended = load_extended()
    hasse_rows = []
    for record in symbolic_records:
        if record["p"] > args.hasse_prime_bound:
            continue
        for ell in range(record["ell_max"] + 1):
            row = family_member(record["p"], ell)
            if row["m"] > args.hasse_max_m:
                break
            forced = {item["p"]: item for item in extended.base.rank_one_rows(row["m"])}
            if row["p"] not in forced:
                raise AssertionError(("missing forced row", row["m"], row["p"]))
            item = forced[row["p"]]
            eta, top_eta, details = extended.eta_with_top(
                row["m"], row["p"], item["e"], item["delta"]
            )
            if (item["e"], item["delta"], eta) != (1, 0, 0):
                raise AssertionError((row, item, eta))
            hasse_rows.append({
                "ell": ell, "m": row["m"], "p": row["p"], "eta": eta,
                "top_only_eta": top_eta, "band_indices": details["band_indices"],
            })

    # The neighboring admissible congruence p=9 mod 20 is a useful finite
    # control: the support argument no longer kills gamma1.
    contrast_rows = []
    for p in primes_upto(min(args.hasse_prime_bound, 500)):
        if p % 20 != 9:
            continue
        m = (9 * p - 1) // 10
        if 10 * m + 1 != 9 * p:
            continue
        forced = {item["p"]: item for item in extended.base.rank_one_rows(m)}
        if p not in forced:
            continue
        item = forced[p]
        eta, top_eta, _ = extended.eta_with_top(m, p, item["e"], item["delta"])
        contrast_rows.append({"m": m, "p": p, "eta": eta, "top_only_eta": top_eta})

    output = {
        "schema": "mixed-cubic-congruence-slab-p2-v2",
        "status": {
            "uniform_congruence_slab": "PROVED_IN_COMPANION_NOTE",
            "ell_zero_affine_ray": "PROVED_AS_A_SUBFAMILY",
            "finite_Hasse_replay": "EXACT_FINITE_AUDIT_ONLY",
            "positive_exponential_mass_gain": "NO_THE_GAIN_IS_THIN_O_M",
        },
        "inputs": {
            EXTENDED_PATH.name: sha256(EXTENDED_PATH),
            extended.BASE_PATH.name: sha256(extended.BASE_PATH),
        },
        "parameters": {
            "symbolic_prime_bound": args.symbolic_prime_bound,
            "hasse_prime_bound": args.hasse_prime_bound,
            "hasse_max_m": args.hasse_max_m,
        },
        "summary": {
            "symbolic_prime_records": len(symbolic_records),
            "symbolic_family_members_in_full_e1_bands": sum(
                row["family_member_count"] for row in symbolic_records
            ),
            "Hasse_family_rows": len(hasse_rows),
            "Hasse_ell_zero_ray_rows": sum(row["ell"] == 0 for row in hasse_rows),
            "Hasse_nonzero_eta_failures": sum(row["eta"] != 0 for row in hasse_rows),
            "neighboring_p_9_mod_20_controls": len(contrast_rows),
            "neighboring_controls_with_nonzero_eta": sum(row["eta"] != 0 for row in contrast_rows),
        },
        "uniform_identity": {
            "p": "20k+19 prime",
            "m": "18k+17+ell*p",
            "ell_range": "ell>=0 and p<=4m+1<p^2",
            "equation": "10m+1=(10ell+9)p",
            "P0": "x^r(1-x^4)^r", "P1": "x^r(1-x)(1-x^4)^(r-1)",
            "conclusion": "gamma0=gamma1=0 and p^2 divides c_m",
            "fixed_m_mass_bound": "the product of all selected p divides 10m+1",
        },
        "symbolic_prime_records": symbolic_records,
        "Hasse_family_rows": hasse_rows,
        "neighboring_congruence_controls": contrast_rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
