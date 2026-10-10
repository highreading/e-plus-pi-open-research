#!/usr/bin/env python3
"""Deterministic certificate for Item 173's rank-zero missing digit.

The script checks the complete kappa=2 cell algebra, the second-Cartier
endpoint identity H(1)=-4aT(1), the one-row extension of the exact tail,
and the scalar-free determinant carry formula for A_1.  Finite scans are
kept explicitly separate from the symbolic assertions in the report.
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
ARCHIVE = Path(__file__).resolve().parents[1]
PROBE = HERE / "item173_probe.py"
DEFAULT_OUTPUT = (
    HERE / "item173_rankzero_nonscalar_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item173_rankzero_nonscalar_certificate.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def cell_rows(probe: Any, prime_bound: int) -> tuple[list[dict[str, Any]], dict[tuple[int, int], dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    cache: dict[tuple[int, int], dict[str, Any]] = {}
    for p in primes_upto(prime_bound):
        if p < 7:
            continue
        for j in range(1, (p - 3) // 2 + 1):
            for s in range(1, (p - 3) // 6 + 1):
                numerator = (2 * j + 1) * p - 2 * s - 1
                if numerator % 4:
                    continue
                m = numerator // 4
                r = (p - 6 * s - 3) // 2
                t = p - 2 * s
                a = 3 * j + 1
                b = 2 * j
                if not (
                    6 * m == a * p + r
                    and 4 * m + 1 == b * p + t
                    and 2 * a - 3 * b == 2
                    and 0 <= r < p
                    and 0 < t < p
                    and p <= 4 * m + 1 < p * p
                ):
                    raise AssertionError((m, p, j, s, "cell identity"))
                second = probe.rank_zero_second(m, p)
                cache[(m, p)] = second
                for identity in second["endpoint_identity"]:
                    if len(set(identity.values())) != 1:
                        raise AssertionError((m, p, identity))
                rows.append(
                    {
                        "m": m,
                        "p": p,
                        "j": j,
                        "s": s,
                        "a": a,
                        "c": 2 * j + 1,
                        "r": r,
                        "t": t,
                        "H0": second["H"][0],
                        "H1": second["H"][1],
                        "H_endpoint_identity": second["endpoint_identity"],
                        "A0_second_Cartier": second["A0_raw"],
                        "B0_second_Cartier_before_Frobenius_sign": second["B0_raw"],
                    }
                )
    return rows, cache


def exact_tail_rows(
    probe: Any, rows: list[dict[str, Any]], cache: dict[tuple[int, int], dict[str, Any]]
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for source in rows:
        p = source["p"]
        j = source["j"]
        if 3 * j + 1 < p or 2 * j + 2 > p:
            continue
        m = source["m"]
        second = cache[(m, p)]
        mode = "ordinary_3j_at_least_p" if 3 * j >= p else "boundary_3j_plus_1_equals_p"
        residual_degrees: list[int] = []
        for h in second["H"]:
            degree_h = len(h) - 1
            if mode == "ordinary_3j_at_least_p":
                degree = 2 * (3 * j - p) + degree_h + 3 * (p - (2 * j + 2))
            else:
                if 3 * j + 1 != p or h[0] % p or sum(h) % p:
                    raise AssertionError((m, p, j, h, "boundary u divisibility"))
                degree = degree_h - 2 + 3 * (p - (2 * j + 2))
            if degree > p - 2:
                raise AssertionError((m, p, j, degree, "residual degree"))
            residual_degrees.append(degree)
        if p * p > 6 * m:
            raise AssertionError((m, p, "support bound"))

        hasse = probe.row(m, p, precision=4)
        a_digits = hasse["A"]
        b_digits = hasse["B"]
        coordinate_digits = hasse["coordinate_digits"]
        l0 = coordinate_digits["L0_over_p"]
        l1 = coordinate_digits["L1_over_p"]
        x0 = coordinate_digits["X0_over_p"]
        x1 = coordinate_digits["X1_over_p"]
        e0 = coordinate_digits["E0_over_p"]
        e1 = coordinate_digits["E1_over_p"]

        raw0 = l1[0] * x0[0] - l0[0] * x1[0]
        carry0 = (raw0 - raw0 % p) // p
        raw1 = (
            l1[0] * x0[1]
            + l1[1] * x0[0]
            - l0[0] * x1[1]
            - l0[1] * x1[0]
        )
        carry_a0 = raw0 % p
        carry_a1 = (raw1 + carry0) % p
        carry_b0 = (l1[0] * e0[0] - l0[0] * e1[0]) % p
        if [carry_a0, carry_a1] != a_digits[:2] or carry_b0 != b_digits[0]:
            raise AssertionError((m, p, "carry mismatch"))
        if a_digits[0] or b_digits[0] or l0[0] or l1[0] or e0[0] or e1[0]:
            raise AssertionError((m, p, "exact-tail leading digit"))
        simplified_a1 = (l1[1] * x0[0] - l0[1] * x1[0]) % p
        if simplified_a1 != a_digits[1]:
            raise AssertionError((m, p, "simplified A1"))
        out.append(
            {
                "m": m,
                "p": p,
                "j": j,
                "s": source["s"],
                "mode": mode,
                "residual_degrees": residual_degrees,
                "p_squared_at_most_6m": True,
                "ell0_rho0_digits": {
                    "ell_0": l0[:2],
                    "ell_1": l1[:2],
                    "rho_0": x0[:2],
                    "rho_1": x1[:2],
                },
                "A0": a_digits[0],
                "A1": a_digits[1],
                "B0": b_digits[0],
                "cubic_gate": a_digits[1] == 0,
            }
        )
    return out


def frozen_crosschecks(
    probe: Any, prime_bound: int, cache: dict[tuple[int, int], dict[str, Any]]
) -> list[dict[str, int]]:
    frozen_path = ARCHIVE / "results" / "item163_deeper_digits_certificate.json"
    frozen = json.loads(frozen_path.read_text(encoding="utf-8"))
    checks: list[dict[str, int]] = []
    for row in frozen["rows"]:
        m = int(row["m"])
        p = int(row["p"])
        if p > prime_bound:
            continue
        a = (6 * m) // p
        b = (4 * m + 1) // p
        if 2 * a - 3 * b != 2 or 2 * (b // 2) + 2 >= p:
            continue
        second = cache.get((m, p))
        if second is None:
            second = probe.rank_zero_second(m, p)
        expected_a0 = int(row["A_digits_after_forced_power"][0])
        expected_b0 = int(row["B_digits_after_forced_power"][0])
        frobenius_sign = 1 if p % 4 == 1 else -1
        got_a0 = int(second["A0_raw"])
        got_b0 = frobenius_sign * int(second["B0_raw"]) % p
        if (got_a0, got_b0) != (expected_a0, expected_b0):
            raise AssertionError((m, p, got_a0, got_b0, expected_a0, expected_b0))
        checks.append({"m": m, "p": p, "A0": got_a0, "B0": got_b0})
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-bound", type=int, default=43)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.prime_bound < 29:
        raise ValueError("prime bound at least 29 is required for the counterpair")
    probe = load("item173_probe_for_certificate", PROBE)
    rows, cache = cell_rows(probe, args.prime_bound)
    tail = exact_tail_rows(probe, rows, cache)
    checks = frozen_crosschecks(probe, args.prime_bound, cache)
    survivors = [row for row in tail if row["cubic_gate"]]
    failures = [row for row in tail if not row["cubic_gate"]]
    counter_failure = next(row for row in tail if (row["m"], row["p"]) == (54, 17))
    counter_survivor = next(row for row in tail if (row["m"], row["p"]) == (180, 29))
    if counter_failure["A1"] != 4 or counter_survivor["A1"] != 0:
        raise AssertionError("counterpair changed")

    dependencies = [
        ("scripts/item173_probe.py", PROBE),
        (
            "scripts/item163_deeper_digits_certificate.py",
            ARCHIVE / "scripts" / "item163_deeper_digits_certificate.py",
        ),
        (
            "scripts/item164_third_layer_certificate.py",
            ARCHIVE / "scripts" / "item164_third_layer_certificate.py",
        ),
        (
            "scripts/lifted_endpoint_hasse_extended_certificate.py",
            ARCHIVE / "scripts" / "lifted_endpoint_hasse_extended_certificate.py",
        ),
        (
            "scripts/lifted_endpoint_hasse_certificate.py",
            ARCHIVE / "scripts" / "lifted_endpoint_hasse_certificate.py",
        ),
        (
            "results/item163_deeper_digits_certificate.json",
            ARCHIVE / "results" / "item163_deeper_digits_certificate.json",
        ),
        (
            "sources/item168_positive_mass_report.md",
            ARCHIVE / "sources" / "item168_positive_mass_report.md",
        ),
    ]
    output = {
        "schema": "mixed-cubic-item173-rankzero-missing-A1-v1",
        "status": {
            "rank_zero_carry_formula": "PROVED_IN_COMPANION_REPORT",
            "boundary_tail_extension": "PROVED_IN_COMPANION_REPORT",
            "tail_mass": "PROVED_ZERO_RATE",
            "tail_hypotheses_determine_A1": "REFUTED_BY_EXACT_COUNTERPAIR",
            "positive_PNT_mass": "OPEN",
            "e_plus_pi": "OPEN",
        },
        "parameters": {"prime_bound": args.prime_bound},
        "dependencies": {label: sha256(path) for label, path in dependencies},
        "theorem_replay": {
            "cell": "4m+1=(2j+1)p-2s; a=3j+1; c=2j+1; kappa=2",
            "minor_identity": "A/p^2=ell_1*rho_0-ell_0*rho_1 with ell_s=L_s/p and rho_s=X_s/p",
            "carry": "A0=S0 mod p; c0=(S0-A0)/p; A1=S1+c0 mod p",
            "tail_simplification": "ell_00=ell_10=0, hence A1=ell_11*rho_00-ell_01*rho_10",
            "endpoint_identity": "H_s(1)=N_s(1)=-4aT_s(1)",
            "extended_tail": "3j+1>=p and 2j+2<=p imply A0=B0=0 and p^2|c_m",
            "support": "extended tail implies p^2<=6m and therefore zero logarithmic mass",
        },
        "summary": {
            "regular_second_Cartier_cells": len(rows),
            "primes": len({row["p"] for row in rows}),
            "endpoint_identity_failures": 0,
            "frozen_second_Cartier_crosschecks": len(checks),
            "frozen_crosscheck_failures": 0,
            "extended_tail_rows": len(tail),
            "boundary_extension_rows": sum(row["mode"].startswith("boundary") for row in tail),
            "tail_A0_failures": sum(bool(row["A0"]) for row in tail),
            "tail_B0_failures": sum(bool(row["B0"]) for row in tail),
            "tail_A1_zeros": len(survivors),
            "tail_A1_nonzeros": len(failures),
            "carry_formula_failures": 0,
        },
        "counterpair": {
            "noncubic": counter_failure,
            "cubic": counter_survivor,
            "scope": "The same extended-tail hypotheses force neither A1=0 nor A1!=0; the rows are not claimed to have identical reduced coordinate data.",
        },
        "tail_cubic_survivors_finite": survivors,
        "tail_rows": tail,
        "frozen_crosschecks": checks,
        "complete_second_Cartier_rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
