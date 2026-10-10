#!/usr/bin/env python3
"""Cross-audit full-window matching maxima against saddle-window data."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]
DEFAULT_PRIMEWISE = Path(__file__).with_name(
    "sequential_matching_primewise_audit_m100_N6m.json"
)
PINNED = {
    "results/mixed_cubic_equal_valuation_m1_100_w20.json":
        "ff2db605c747501dc87cf80493c3f957d4c80fe55e5805153afda3b364882273",
    "results/mixed_cubic_equal_valuation_m105_200_step5_w20.json":
        "5558ab9aaf3eed8d0c2f03fa60167ec28917b9a832c49092155cab8889c97b96",
    "results/mixed_cubic_primitive_b_support_probe_selected.json":
        "eb00bd8e8e0d2b2f0368560655f7a99d59a54636ca0a8ca82597683e7548cc98",
    "sources/mixed_cubic_equal_valuation_crt_reduction.md":
        "56b2b3297e5c2d780ad8c7dd5c8605f7c8fdba51fca7786d2669758b3ed1ba93",
}
PINNED_PRIMEWISE = "ab22c075132c72d9aa80206ef009220d93bc03907bf5b95faf6fb5db730daff9"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_upto(limit: int) -> list[int]:
    out = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, math.isqrt(value) + 1)):
            out.append(value)
    return out


def mean(rows: list[dict[str, object]], extractor) -> float:
    return math.fsum(extractor(row) for row in rows) / len(rows)


def saddle_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    actual = [row["best_actual"] for row in rows]
    return {
        "row_count": len(rows),
        "m_values": [int(row["m"]) for row in rows],
        "mean_c_rate": mean(rows, lambda row: float(row["content_log_per_n"])),
        "mean_Delta_rate": mean(
            actual, lambda row: float(row["delta_log_per_n"])
        ),
        "mean_g_rate": mean(actual, lambda row: float(row["g_log_per_n"])),
        "mean_matching_rate": mean(
            actual,
            lambda row: float(row["delta_log_per_n"])
            + float(row["g_log_per_n"]),
        ),
        "mean_total_rate": mean(
            actual, lambda row: float(row["c_delta_g_log_per_n"])
        ),
        "max_total_rate": max(
            [
                {
                "m": int(parent["m"]),
                "N": int(parent["best_actual"]["N"]),
                "rate": float(parent["best_actual"]["c_delta_g_log_per_n"]),
                }
                for parent in rows
            ],
            key=lambda item: item["rate"],
        ),
        "max_equal_level_ceiling_rate": max(
            float(row["best_equal_level_upper"]["c_delta_equal_upper_log_per_n"])
            for row in rows
        ),
        "actual_g_nontrivial_rows": sum(
            int(row["best_actual"]["g"]) > 1 for row in rows
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--primewise", type=Path, default=DEFAULT_PRIMEWISE)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    pinned_actual = {}
    for relative, expected in PINNED.items():
        actual = sha256(args.archive / relative)
        assert actual == expected, (relative, actual, expected)
        pinned_actual[relative] = actual
    primewise_hash = sha256(args.primewise)
    assert primewise_hash == PINNED_PRIMEWISE, primewise_hash

    primewise = json.loads(args.primewise.read_text(encoding="utf-8"))
    saddle100 = json.loads(
        (args.archive / "results/mixed_cubic_equal_valuation_m1_100_w20.json")
        .read_text(encoding="utf-8")
    )
    saddle200 = json.loads(
        (
            args.archive
            / "results/mixed_cubic_equal_valuation_m105_200_step5_w20.json"
        ).read_text(encoding="utf-8")
    )
    b_support = json.loads(
        (args.archive / "results/mixed_cubic_primitive_b_support_probe_selected.json")
        .read_text(encoding="utf-8")
    )

    assert len(primewise["rows"]) == len(saddle100["rows"]) == 100
    full_equals_saddle = []
    full_inside_saddle_window = []
    for full, saddle in zip(primewise["rows"], saddle100["rows"]):
        assert int(full["m"]) == int(saddle["m"])
        n_full = int(full["content_maximizer"]["N"])
        n_saddle = int(saddle["best_actual"]["N"])
        candidate_indices = {
            int(entry)
            for entry in range(
                max(1, math.floor(0.8 * int(saddle["target_N"]))),
                math.ceil(1.2 * int(saddle["target_N"])) + 1,
            )
            if entry % 2 == n_saddle % 2
        }
        full_equals_saddle.append(n_full == n_saddle)
        full_inside_saddle_window.append(n_full in candidate_indices)

    support_rows = []
    for row in b_support["rows"]:
        m_value = int(row["m"])
        listed = {int(prime) for prime in row["small_prime_factors"]}
        odd_primes = [prime for prime in primes_upto(6 * m_value) if prime != 2]
        missing = [prime for prime in odd_primes if prime not in listed]
        small_factor_rate = (
            float(row["primitive_b_log_per_6m"])
            - float(row["cofactor_log_per_6m"])
        )
        support_rows.append(
            {
                "m": m_value,
                "odd_primes_at_most_6m": len(odd_primes),
                "missing_odd_primes": missing,
                "small_factor_rate": small_factor_rate,
                "large_cofactor_rate": float(row["cofactor_log_per_6m"]),
                "primitive_b_rate": float(row["primitive_b_log_per_6m"]),
            }
        )

    tail100 = saddle100["rows"][80:]
    rank_one_rate = (-4 * math.log(2) + 6 * math.log(3) - 3) / 6
    target_rate = 1.1561471519642446123307302238571333989
    one_copy_ceiling = rank_one_rate + 0.5
    doubled_ceiling = rank_one_rate + 1.0
    payload = {
        "schema": "item163-sequential-matching-context-audit-v1",
        "status": "PASS",
        "generator": {
            "filename": Path(__file__).name,
            "sha256": sha256(Path(__file__)),
        },
        "pinned_inputs": pinned_actual,
        "primewise_input": {
            "logical_artifact": "sequential_matching_primewise_audit_m100_N6m.json",
            "sha256": primewise_hash,
        },
        "full_window_vs_saddle_window": {
            "same_maximizer_rows_m1_100": sum(full_equals_saddle),
            "full_maximizer_inside_saddle_window_rows_m1_100": sum(
                full_inside_saddle_window
            ),
            "same_maximizer_rows_m81_100": sum(full_equals_saddle[80:]),
            "full_maximizer_inside_saddle_window_rows_m81_100": sum(
                full_inside_saddle_window[80:]
            ),
            "warning": (
                "The N <= 6m content maximum is generally not analytically "
                "saddle-compatible and must not be used as the applicable rate."
            ),
        },
        "saddle_window_m81_100": saddle_summary(tail100),
        "saddle_window_m105_200_step5": saddle_summary(saddle200["rows"]),
        "primitive_b_selected_support": support_rows,
        "clearing_reservoir_scoped_capacity": {
            "rank_one_rate": rank_one_rate,
            "K_rate_limit": 0.5,
            "target_rate": target_rate,
            "one_copy_plus_rank_one_ceiling": one_copy_ceiling,
            "one_copy_gap_to_target": target_rate - one_copy_ceiling,
            "fully_doubled_plus_rank_one_ceiling": doubled_ceiling,
            "fully_doubled_gap_to_target": target_rate - doubled_ceiling,
            "scope": (
                "This is a ceiling only for certificates whose booked mass "
                "comes from the rank-one radical and factors traceable to "
                "K_after_Cartier. It is not an upper bound on actual c*Delta*g."
            ),
            "primewise_accounting": (
                "If k=vp(K_after_Cartier), kappa=vp(c), and "
                "r=max(k-kappa,0), then at most min(k,kappa)+2r <= 2k "
                "exponents are traceable to this reservoir, even granting "
                "full Delta and g recovery."
            ),
        },
        "classification": {
            "PROVED_FINITE": [
                "All displayed rates and support counts are exact consequences of pinned integer scans; logarithms are diagnostic floating evaluations.",
                "Only 13 of 100 unrestricted-window content maximizers equal the saddle-window maximizer; only 5 of the last 20 do.",
            ],
            "PROVED_GENERAL": [
                "Delta*g divides q_N^2, so log(Delta*g) <= 2 log(q_N).",
                "Since q_N < 4^(N-1) N!, every N_m=o(m/log m) has log(Delta*g)/(6m) -> 0.",
                "The K clearing reservoir has rate at most 1/2. One synchronized copy plus rank one reaches at most 0.6365141683; even full primewise doubling through Delta and g reaches at most 1.1365141683, still below target by 0.0196329837.",
                "On ordinary root branches, prescribed full local synchronization lies in at most product R_p classes modulo 2*Delta*g; a positive-rate gain at saddle scale requires an exponentially small representative of a moving CRT class.",
            ],
            "EXPERIMENTAL": [
                "The selected primitive b_m probes contain nearly every odd prime <= 6m but also retain a large cofactor of rate about 1.1.",
                "The saddle-window matching increments decrease sharply in the sampled data and remain far below theorem scale.",
            ],
            "OPEN": [
                "A theorem coupling the actual large cofactor of b_m to Bessel root classes.",
                "An asymptotic upper bound excluding rare exponentially small ordinary CRT representatives.",
                "An all-prime theorem controlling singular branches and excess prime-power valuations.",
            ],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.write_bytes(encoded)
    print(hashlib.sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
