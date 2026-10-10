#!/usr/bin/env python3
"""Exact replay for the factorial-window CF entry dichotomy.

Finite rows below are regression diagnostics.  The all-parameter arguments
are the inequalities and symbolic identities proved in the source.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "sources/common_kernel_factorial_window_cf_entry_dichotomy.md"
)
OUTPUT = (
    ROOT
    / "results/common_kernel_factorial_window_cf_entry_dichotomy_certificate.json"
)
DEPENDENCIES = {
    "results/common_kernel_native_cf_window_scan_hashes.sha256":
        "45c9253a4d4572806c0650345f2e47e4d8953618daf5c87512a1d62e0e1cd958",
}
RSS_GUARD_KIB = 40 * 1024 * 1024


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM unavailable")


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte not in (9, 10)
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def markup_audit(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    stack: list[int] = []
    blocks = 0
    for line_number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped == r"\[":
            assert not stack, ("nested display", line_number, stack)
            stack.append(line_number)
            blocks += 1
        elif stripped == r"\]":
            assert stack, ("orphan display close", line_number)
            stack.pop()
    assert not stack
    text = "\n".join(lines)
    assert text.count(r"\(") == text.count(r"\)")
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    expected_tags = (
        [str(index) for index in range(1, 14)]
        + ["13a"]
        + [str(index) for index in range(14, 32)]
        + ["31a"]
        + [str(index) for index in range(32, 35)]
    )
    assert tags == expected_tags
    return {
        "display_blocks": blocks,
        "inline_delimiters_each": text.count(r"\("),
        "tags": tags,
        "status": "PASS",
    }


def admissible(integer: int) -> bool:
    return integer % 8 in {0, 1, 2, 3, 4}


def previous_admissible(integer: int) -> int:
    candidate = integer - 1
    while not admissible(candidate):
        candidate -= 1
    return candidate


def entry_index_square(q: int, all_residues: bool = False) -> int:
    factorial = 1
    integer = 1
    while True:
        integer += 1
        factorial *= integer
        if (all_residues or admissible(integer)) and q * q <= factorial:
            return integer


def admissible_gap_audit() -> dict[str, object]:
    residues = [integer for integer in range(8) if admissible(integer)]
    cycle = [0, 1, 2, 3, 4, 8]
    gaps = [cycle[index + 1] - cycle[index] for index in range(5)]
    assert gaps == [1, 1, 1, 1, 4]

    rows = []
    for q in [
        2,
        3,
        5,
        13,
        89,
        1597,
        514229,
        433494437,
        7778742049,
    ]:
        entry = entry_index_square(q)
        previous = previous_admissible(entry)
        assert previous < entry and entry - previous <= 4
        assert math.factorial(previous) < q * q <= math.factorial(entry)
        entry_phase = Fraction(math.factorial(entry), q * q)
        assert 1 <= entry_phase < entry**4

        full_entry = entry_index_square(q, all_residues=True)
        assert math.factorial(full_entry - 1) < q * q <= math.factorial(full_entry)
        full_phase = Fraction(math.factorial(full_entry), q * q)
        assert 1 <= full_phase < full_entry
        rows.append({
            "q": str(q),
            "native_entry": entry,
            "native_gap": entry - previous,
            "native_lambda": str(entry_phase),
            "native_lambda_lt_N4": True,
            "all_residue_entry": full_entry,
            "all_residue_lambda": str(full_phase),
            "all_residue_lambda_lt_N": True,
        })
    return {
        "admissible_residues_mod_8": residues,
        "cyclic_positive_gaps": gaps,
        "maximum_gap": max(gaps),
        "diagnostic_rows": rows,
    }


def fibonacci_rows() -> dict[str, object]:
    # p/q = F_(n+1)/F_n are the convergents of phi.
    fibonacci = [0, 1]
    for _ in range(2, 45):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    rows = []
    for index in range(2, 35):
        q = fibonacci[index]
        p = fibonacci[index + 1]
        norm = p * p - p * q - q * q
        assert norm in (-1, 1)
        assert norm == (-1) ** index
        below = norm == -1
        if below:
            entry = entry_index_square(q)
            # N>=12 is exactly enough for N^2>125, i.e. N>5*sqrt(5).
            excludes_native_by_norm = entry >= 12
            if excludes_native_by_norm:
                assert entry * entry > 125
            rows.append({
                "cf_index": index,
                "p": str(p),
                "q": str(q),
                "quadratic_norm": norm,
                "native_entry": entry,
                "N_squared_gt_125": entry * entry > 125,
                "native_window_excluded_if_N_ge_12":
                    excludes_native_by_norm,
            })
    assert rows
    return {
        "continued_fraction": "[1;1,1,1,...]",
        "all_partial_quotients": 1,
        "below_convergent_rows": rows,
        "exact_obstruction": (
            "(phi-p/q)*(p/q-phi')=abs(p^2-p*q-q^2)/q^2 "
            "and abs(p/q-phi')<sqrt(5)"
        ),
        "uniform_no_hit_threshold": "N>=12",
    }


def symbolic_ledgers() -> dict[str, object]:
    N, q, tau, Lambda, Z, A, B, scale = sp.symbols(
        "N q tau Lambda Z A B scale", positive=True
    )
    factorial_ratio = sp.factor(
        ((N + 1) * sp.factorial(N + 1))
        / (N * sp.factorial(N))
    )
    assert sp.simplify(factorial_ratio - (N + 1) ** 2 / N) == 0

    ordinary_lambda = Lambda * q ** (tau - 2)
    D = sp.factor(N * ordinary_lambda / Z)
    assert D == N * Lambda * q ** (tau - 2) / Z

    # A chain of m copies with ratio rho can cover multiplicative span
    # at most rho^m.  Check exact representative chains.
    covering_rows = []
    for rho_value in [Fraction(3, 2), Fraction(2, 1), Fraction(5, 1)]:
        for copies in [1, 2, 4, 8]:
            scales = [rho_value**index for index in range(copies)]
            total_span = scales[-1] * rho_value / scales[0]
            assert total_span == rho_value**copies
            covering_rows.append({
                "rho": str(rho_value),
                "copies": copies,
                "maximum_connected_span": str(total_span),
            })

    return {
        "consecutive_factorial_normalized_ratio": str(factorial_ratio),
        "continued_fraction_D_coordinate": str(D),
        "low_rule": "Z<=A<5 => a_next>N*lambda/5-2",
        "high_rule": "Z>=B>1 => a_next<N*lambda",
        "covering_rows": covering_rows,
    }


def fixed_scale_countermodel() -> dict[str, object]:
    # If the largest scale is S, the golden-ratio norm lower bound and
    # q^2<=N! force S>N/(5*sqrt(5)).  Squaring avoids floating point.
    rows = []
    for scales in [
        [Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(4)],
        [Fraction(1, 3), Fraction(7, 2), Fraction(19)],
    ]:
        maximum = max(scales)
        # Find the first integer N which is certainly beyond the necessary
        # range: N > 5*sqrt(5)*S, equivalently N^2>125*S^2.
        threshold = 1
        while Fraction(threshold * threshold, 1) <= 125 * maximum * maximum:
            threshold += 1
        assert Fraction(threshold * threshold, 1) > 125 * maximum * maximum
        rows.append({
            "scales": [str(value) for value in scales],
            "maximum_scale": str(maximum),
            "first_certified_no_hit_N": threshold,
            "exact_squared_inequality": (
                f"{threshold**2} > {125 * maximum * maximum}"
            ),
        })
    return {
        "rows": rows,
        "general_badly_approximable_rule": (
            "if abs(x-p/q)>=c(x)/q^2 and the normalized upper endpoint "
            "is C*S_N, then any q^2<=N! hit requires S_N>=c(x)*N/C"
        ),
        "scope": (
            "Exact golden-ratio countermodel for each displayed finite "
            "scale set; the symbolic proof covers every fixed finite set."
        ),
    }


def main() -> None:
    dependency_audit = {}
    for relative, expected in DEPENDENCIES.items():
        observed = sha256(ROOT / relative)
        assert observed == expected, (relative, observed, expected)
        dependency_audit[relative] = observed

    controls = [control_audit(SOURCE), control_audit(Path(__file__))]
    assert all(item["clean"] for item in controls)
    result = {
        "theorem": (
            "factorial-window CF entry dichotomy and finite-scaling barrier"
        ),
        "dependency_audit": dependency_audit,
        "control_audit": controls,
        "markup_audit": markup_audit(SOURCE),
        "admissible_entry_ledger": admissible_gap_audit(),
        "golden_ratio_countermodel": fibonacci_rows(),
        "symbolic_ledgers": symbolic_ledgers(),
        "fixed_scale_countermodel": fixed_scale_countermodel(),
        "scope": {
            "proved_all_parameter": [
                "native gap-four entry phase 1<=Lambda<N^4",
                "exact low/high next-partial-quotient dichotomy",
                "fixed-power low entries imply one-sided exponent tau",
                "square-root low entries supply only logarithmic gain",
                "golden ratio excludes any miss-to-large-partial-quotient inference",
                "finite fixed scales and o(N) scales cannot remove the obstruction",
                "fixed-ratio multiplicative coverage needs Omega(log N) scales",
            ],
            "not_claimed": [
                "future continued-fraction behavior of e+pi",
                "irrationality or transcendence of e+pi",
            ],
        },
    }
    observed_peak = peak_rss_kib()
    assert observed_peak < RSS_GUARD_KIB
    result["rss_guard_kib"] = RSS_GUARD_KIB
    result["rss_guard_passed"] = True

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "peak_rss_kib": observed_peak,
        "status": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
