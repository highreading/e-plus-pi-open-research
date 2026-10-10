#!/usr/bin/env python3
"""Exact replay for the conditional native denominator-saturation barrier.

The finite rows are deterministic regression diagnostics.  The theorem is
the all-parameter chain of exact inequalities verified symbolically here and
proved in the accompanying source.
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
    / "sources/common_kernel_rational_case_denominator_saturation_barrier.md"
)
OUTPUT = (
    ROOT
    / "results/common_kernel_rational_case_denominator_saturation_certificate.json"
)
DEPENDENCIES = {
    "results/common_kernel_native_output_bernstein_congruence_hashes.sha256":
        "559cc412db81ed449d4255654ad370f44a8ceb4d8acdce234a7f607d448ffcb7",
    "results/common_kernel_integer_bernstein_quantitative_arithmetic_hashes.sha256":
        "80ac4f4e108fd87b7549499abe702e0ddee83c45450ba338e820d18a5ab8437d",
    "results/common_kernel_native_exact_moment_integer_approximation_hashes.sha256":
        "aa35956007909d980f86d43909eaad180d56b9c80a654059425513a1debbb6b9",
    "results/common_kernel_native_sign_output_range_sharp_width_hashes.sha256":
        "de1348caca545595e79ddc00929ece5d0ef7f18fb7eeb3f979beb26f2b766677",
    "results/common_kernel_native_fixed_N_output_closure_hashes.sha256":
        "a5c167be7be4ee5924131c4e0dfa2f97ac64232b5a8c90242e6fb064c2d8fcab",
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
    displays = 0
    for line_number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped == r"\[":
            assert not stack, ("nested display", line_number, stack)
            stack.append(line_number)
            displays += 1
        elif stripped == r"\]":
            assert stack, ("orphan display close", line_number)
            stack.pop()
    assert not stack
    text = "\n".join(lines)
    assert text.count(r"\(") == text.count(r"\)")
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    assert tags == [str(index) for index in range(1, 40)]
    required_scope = [
        "The theorem is conditional",
        "does not prove that \\(e+\\pi\\) is rational, irrational, or",
        "does not unconditionally exclude",
        "No claim about the arithmetic classification",
    ]
    for phrase in required_scope:
        assert phrase in text
    return {
        "display_blocks": displays,
        "inline_delimiters_each": text.count(r"\("),
        "tags": tags,
        "scope_phrases": required_scope,
        "status": "PASS",
    }


def verify_manifest(path: Path) -> dict[str, object]:
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split(maxsplit=1)
        relative = relative.strip()
        observed = sha256(ROOT / relative)
        assert observed == expected, (relative, observed, expected)
        entries.append({"path": relative, "sha256": observed})
    assert entries
    return {
        "manifest": str(path.relative_to(ROOT)),
        "entries": entries,
        "status": "PASS",
    }


def dependency_audit() -> dict[str, object]:
    result = {}
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        observed = sha256(path)
        assert observed == expected, (relative, observed, expected)
        result[relative] = {
            "manifest_sha256": observed,
            "replayed_entries": verify_manifest(path)["entries"],
            "status": "PASS",
        }
    return result


def constant_audit() -> dict[str, object]:
    half = Fraction(1, 2)
    exp_half_lower = sum(
        half**index / math.factorial(index) for index in range(4)
    )
    assert exp_half_lower == Fraction(79, 48)

    x = Fraction(15, 4)
    partial = sum(x**index / math.factorial(index) for index in range(7))
    tail_upper = x**7 / math.factorial(7) / (1 - x / 8)
    exp_15_4_upper = partial + tail_upper
    assert exp_15_4_upper == Fraction(333375299, 7798784)
    assert exp_15_4_upper < 43

    lhs_lower = 32 * (25 * exp_half_lower - 17)
    rhs_upper = 17 * 43
    assert lhs_lower == Fraction(2318, 3)
    assert rhs_upper == 731
    assert lhs_lower - rhs_upper == Fraction(125, 3) > 0

    # 32(25*sqrt(e)-17)>17*e^(15/4) is algebraically equivalent
    # to c_*>1/50 for c_*=16(25*sqrt(e)-17)/(425*e^(15/4)).
    return {
        "exp_half_strict_lower": str(exp_half_lower),
        "exp_15_over_4_strict_upper": str(exp_15_4_upper),
        "exp_15_over_4_upper_lt_43": True,
        "equivalent_lhs_lower": str(lhs_lower),
        "equivalent_rhs_upper": str(rhs_upper),
        "strict_rational_margin": str(lhs_lower - rhs_upper),
        "conclusion": "c_*>1/50",
    }


def beta_and_threshold_audit() -> dict[str, object]:
    N = sp.symbols("N", integer=True, positive=True)
    beta_lower = (
        sp.Rational(5, 1) / (N + 1)
        + 1 / ((N + 1) * (N + 2))
        - 8 / ((N + 1) * (N + 2) * (N + 3))
    )
    beta_simplified = (
        sp.Rational(5, 1) / (N + 1)
        + (N - 5) / ((N + 1) * (N + 2) * (N + 3))
    )
    assert sp.simplify(beta_lower - beta_simplified) == 0

    threshold_gap = sp.factor(
        sp.Rational(5, 1) / (N + 5)
        - sp.Rational(249, 50) / N
    )
    expected_gap = (N - 1245) / (50 * N * (N + 5))
    assert sp.simplify(threshold_gap - expected_gap) == 0

    at_1245 = threshold_gap.subs(N, 1245)
    at_1246 = threshold_gap.subs(N, 1246)
    assert at_1245 == 0
    assert at_1246 > 0

    return {
        "beta_lower_bound": str(beta_lower),
        "beta_lower_simplified": str(beta_simplified),
        "target_lower_margin": str(threshold_gap),
        "margin_at_1245": str(at_1245),
        "margin_at_1246": str(at_1246),
        "strict_threshold": 1246,
    }


def denominator_residue_audit() -> dict[str, object]:
    k = sp.symbols("k", integer=True, nonnegative=True)
    rows = []
    for residue in range(5):
        N = 5 * k + residue
        D = k + 1
        lower_margin = sp.simplify(D - (N + 1) / 5)
        upper_margin = sp.simplify((N + 5) / 5 - D)
        assert lower_margin == sp.Rational(4 - residue, 5)
        assert upper_margin == sp.Rational(residue, 5)
        rows.append({
            "N_mod_5": residue,
            "D": "k+1",
            "D_minus_(N+1)/5": str(lower_margin),
            "(N+5)/5_minus_D": str(upper_margin),
        })
    return {
        "rows": rows,
        "conclusion": (
            "(N+1)/5<=floor(N/5)+1<=(N+5)/5 in every residue"
        ),
    }


def deterministic_target_rows() -> dict[str, object]:
    rows = []
    for N in [1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1600]:
        D = N // 5 + 1
        target = Fraction(1, D)
        lower_proxy = Fraction(249, 50 * N)
        endpoint_lower_bound = Fraction(5, N + 1)
        target_minus_proxy = target - lower_proxy
        endpoint_bound_minus_target = endpoint_lower_bound - target
        admissible = N % 8 in {0, 1, 2, 3, 4}
        if N >= 1246:
            assert target_minus_proxy > 0
        if N >= 5:
            assert endpoint_bound_minus_target >= 0
        assert D * Fraction(5, N) <= 1 + Fraction(5, N)
        rows.append({
            "N": N,
            "admissible": admissible,
            "D": D,
            "target": str(target),
            "target_minus_249/(50N)": str(target_minus_proxy),
            "5/(N+1)_minus_target": str(endpoint_bound_minus_target),
            "D_times_5/N": str(D * Fraction(5, N)),
        })

    first_admissible_at_or_after_threshold = next(
        integer
        for integer in range(1246, 1260)
        if integer % 8 in {0, 1, 2, 3, 4}
    )
    assert first_admissible_at_or_after_threshold == 1248
    return {
        "rows": rows,
        "first_admissible_at_or_after_1246": first_admissible_at_or_after_threshold,
    }


def integer_translation_audit() -> dict[str, object]:
    rows = []
    for N in [1248, 1249, 1250, 1251, 1252, 1600]:
        D = N // 5 + 1
        for M in [1, 2, 17, math.factorial(12)]:
            numerator = 1 - M * D
            gcd_value = math.gcd(abs(numerator), D)
            assert gcd_value == 1
            rows.append({
                "N": N,
                "M": M,
                "coordinate_numerator": str(numerator),
                "coordinate_denominator": D,
                "gcd": gcd_value,
            })
    return {
        "euclidean_identity": "gcd(1-MD,D)=gcd(1,D)=1",
        "diagnostic_rows": rows,
    }


def main() -> None:
    dependencies = dependency_audit()
    controls = [control_audit(SOURCE), control_audit(Path(__file__))]
    assert all(item["clean"] for item in controls)

    result = {
        "theorem": (
            "conditional rational-output saturation at the native "
            "positive-integer threshold"
        ),
        "dependency_audit": dependencies,
        "control_audit": controls,
        "markup_audit": markup_audit(SOURCE),
        "constant_audit": constant_audit(),
        "beta_and_threshold_audit": beta_and_threshold_audit(),
        "denominator_residue_audit": denominator_residue_audit(),
        "deterministic_target_rows": deterministic_target_rows(),
        "integer_translation_audit": integer_translation_audit(),
        "scope": {
            "proved_all_parameter": [
                (
                    "under e+pi=u/v and v|N!, strict integer outputs are "
                    "exactly the rational points of the real output interval"
                ),
                (
                    "under that hypothesis every reduced coordinate "
                    "denominator satisfies D*L0>1"
                ),
                (
                    "for every admissible N>=1246 the output 1/"
                    "(floor(N/5)+1) is realizable under that hypothesis"
                ),
                (
                    "the minimal denominator times L0 lies strictly between "
                    "1 and 1+5/N"
                ),
            ],
            "not_claimed": [
                "an unconditional coefficient-explicit localizer at the target",
                "an unconditional exclusion of D*L0<1",
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
