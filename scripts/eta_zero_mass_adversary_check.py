#!/usr/bin/env python3
"""Exact finite and constant audit for the lifted eta-zero mass ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from decimal import Decimal, getcontext
from pathlib import Path


EXPECTED_SHA256 = "54025499d507749259d7d52a231f5594a77885bf0bf1ee0df747d94d86afde3c"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "lifted_endpoint_hasse_certificate_m30.json",
    )
    args = parser.parse_args()
    assert hashlib.sha256(args.certificate.read_bytes()).hexdigest() == EXPECTED_SHA256
    data = json.loads(args.certificate.read_text(encoding="utf-8"))
    rows = data["rows"]
    zero_rows = [row for row in rows if int(row["eta"]) == 0]
    assert len(rows) == 118
    assert len(zero_rows) == 45
    assert all(int(row["p"]) < 2 * int(row["m"]) for row in rows)
    assert len({(int(row["m"]), int(row["p"])) for row in rows}) == len(rows)

    distinct_zero_primes = sorted({int(row["p"]) for row in zero_rows})
    assert distinct_zero_primes == [3, 5, 7, 11, 19, 31]
    by_m: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in zero_rows:
        by_m[int(row["m"])].append(row)
    finite_rates = {
        m: sum(math.log(int(row["p"])) for row in group) / (6 * m)
        for m, group in by_m.items()
    }

    getcontext().prec = 70
    ln2 = Decimal(2).ln()
    ln3 = Decimal(3).ln()
    pi = Decimal(
        "3.141592653589793238462643383279502884197169399375105820974944592307816"
    )
    r1 = (-4 * ln2 + 6 * ln3 - 3) / 6
    c2 = 6 - pi / Decimal(3).sqrt() - 3 * ln3
    threshold = Decimal(
        "1.15614715196424461233073022385713339889672487062787565"
    )
    deficit = threshold - r1
    two_digit_forced_ceiling = 2 * (r1 + c2 / 6)
    unavoidable_remaining = threshold - two_digit_forced_ceiling
    assert two_digit_forced_ceiling < threshold

    payload = {
        "status": "PASS",
        "certificate_sha256": EXPECTED_SHA256,
        "finite": {
            "rows": len(rows),
            "eta_zero_rows": len(zero_rows),
            "eta_zero_by_source": dict(Counter(row["source"] for row in zero_rows)),
            "distinct_eta_zero_primes": distinct_zero_primes,
            "maximum_observed_eta_zero_weight_per_6m": max(finite_rates.values()),
            "maximum_observed_at_m": max(finite_rates, key=finite_rates.get),
        },
        "certified_constants": {
            "rank_one_rate_r1": str(r1),
            "rank_two_radical_ceiling_per_m_C2": str(c2),
            "optimal_matching_threshold_T": str(threshold),
            "post_rank_one_deficit_T_minus_r1": str(deficit),
            "first_two_forced_digits_absolute_ceiling_per_6m": str(
                two_digit_forced_ceiling
            ),
            "remaining_even_under_that_optimistic_ceiling": str(
                unavoidable_remaining
            ),
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
