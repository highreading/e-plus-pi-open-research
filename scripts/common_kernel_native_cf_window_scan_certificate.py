#!/usr/bin/env python3
"""Exact certificate for the native factorial/continued-fraction window.

The scan contains no floating-point arithmetic.  It constructs a common
fixed-point enclosure of e+pi, proves a common continued-fraction prefix for
every real number in that enclosure, and exhausts all principal convergents
allowed by the universal normalized-error window through N=2000.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path


sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_native_cf_window_scan.md"
OUTPUT = ROOT / "results/common_kernel_native_cf_window_scan_certificate.json"
PREVIOUS_JSON = (
    ROOT / "results/common_kernel_native_fixed_N_output_closure_certificate.json"
)
PREVIOUS_MANIFEST = (
    ROOT / "results/common_kernel_native_fixed_N_output_closure_hashes.sha256"
)

N_MIN = 10
N_MAX = 2000
DECIMAL_GUARD_DIGITS = 120
RSS_CAP_KIB = 2 * 1024 * 1024

EXPECTED_PREVIOUS_HASHES = {
    "sources/common_kernel_native_fixed_N_output_closure.md": (
        "c9a018f47b54ed565c958da3dbd53b38b912238b63e56234dfb8a9e68ec99d42"
    ),
    "scripts/common_kernel_native_fixed_N_output_closure_certificate.py": (
        "75631e0c53a5851bc36f77d592c2c4737cdd4b4ebe8bc5a637062781e93be875"
    ),
    "results/common_kernel_native_fixed_N_output_closure_certificate.json": (
        "a1bb13e6083592872cc0b90d466153e5cb5e76b0f3d685d218ca18cfb4b5ee45"
    ),
}
EXPECTED_PREVIOUS_MANIFEST_HASH = (
    "a5c167be7be4ee5924131c4e0dfa2f97ac64232b5a8c90242e6fb064c2d8fcab"
)
EXPECTED_BROAD_CANDIDATES = [25, 33, 43, 86, 88, 164, 331, 351, 1477]
EXPECTED_ADMISSIBLE_HITS = [25, 33, 43, 88, 164, 331]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def literal_fraction_digest(numerator: int, denominator: int) -> str:
    return hashlib.sha256(f"{numerator}/{denominator}".encode()).hexdigest()


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM unavailable")


def control_and_tex_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte not in (9, 10)
    ]
    text = data.decode("utf-8")
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    duplicate_tags = sorted({tag for tag in tags if tags.count(tag) > 1})
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "inline_open_close": [text.count(r"\("), text.count(r"\)")],
        "display_open_close": [text.count(r"\["), text.count(r"\]")],
        "equation_tag_count": len(tags),
        "duplicate_equation_tags": duplicate_tags,
        "clean": (
            not forbidden
            and text.count(r"\(") == text.count(r"\)")
            and text.count(r"\[") == text.count(r"\]")
            and not duplicate_tags
        ),
    }


def ceil_div(numerator: int, denominator: int) -> int:
    assert denominator > 0
    return -((-numerator) // denominator)


def decimal_outward(
    numerator: int, denominator: int, digits: int, direction: str
) -> str:
    scale = 10**digits
    scaled_numerator = numerator * scale
    if direction == "down":
        integer = scaled_numerator // denominator
    else:
        integer = ceil_div(scaled_numerator, denominator)
    sign = "-" if integer < 0 else ""
    absolute = abs(integer)
    whole, fraction = divmod(absolute, scale)
    return f"{sign}{whole}.{fraction:0{digits}d}"


def scaled_e_interval(scale: int) -> tuple[int, int, int]:
    """Return integers L,U with L/scale <= e <= U/scale."""
    index = 0
    factorial = 1
    numerator = 1  # index! * sum_{j=0}^index 1/j!
    while True:
        # The tail after index is at most
        # (index+2)/((index+1)!*(index+1)).
        tail_numerator = scale * (index + 2)
        tail_denominator = factorial * (index + 1) * (index + 1)
        if tail_numerator < tail_denominator:
            break
        index += 1
        factorial *= index
        numerator = index * numerator + 1
    lower = scale * numerator // factorial
    upper = ceil_div(scale * numerator, factorial) + 1
    return lower, upper, index


def scaled_atan_interval(scale: int, reciprocal: int) -> tuple[int, int, int]:
    """Alternating-series enclosure of atan(1/reciprocal), scaled by scale."""
    lower = 0
    upper = 0
    power = reciprocal
    index = 0
    while True:
        denominator = (2 * index + 1) * power
        term_lower = scale // denominator
        term_upper = ceil_div(scale, denominator)
        if index % 2 == 0:
            lower += term_lower
            upper += term_upper
        else:
            lower -= term_upper
            upper -= term_lower

        next_power = power * reciprocal * reciprocal
        next_denominator = (2 * index + 3) * next_power
        if next_denominator > scale:
            remainder_upper = ceil_div(scale, next_denominator)
            if (index + 1) % 2 == 0:
                upper += remainder_upper
            else:
                lower -= remainder_upper
            return lower, upper, index + 1
        power = next_power
        index += 1


def scaled_s_interval(decimal_digits: int) -> tuple[int, int, dict[str, int]]:
    scale = 10**decimal_digits
    e_lower, e_upper, e_terms = scaled_e_interval(scale)
    atan5_lower, atan5_upper, atan5_terms = scaled_atan_interval(scale, 5)
    atan239_lower, atan239_upper, atan239_terms = scaled_atan_interval(
        scale, 239
    )
    # Machin: pi=16 atan(1/5)-4 atan(1/239).
    lower = e_lower + 16 * atan5_lower - 4 * atan239_upper
    upper = e_upper + 16 * atan5_upper - 4 * atan239_lower
    assert lower < upper
    return lower, upper, {
        "e_last_taylor_index": e_terms,
        "atan_1_over_5_terms": atan5_terms,
        "atan_1_over_239_terms": atan239_terms,
        "interval_width_units": upper - lower,
    }


def common_continued_fraction_prefix(
    lower: int, upper: int, scale: int, denominator_cap: int
) -> tuple[
    list[int],
    list[tuple[int, int, int, int, int]],
    tuple[int, int],
]:
    """Common CF prefix and certified below-s convergents.

    Each below row is (q,p,error_lower_numerator,error_upper_numerator,k),
    where the error bounds have common denominator scale*q.
    """
    lower_numerator, lower_denominator = lower, scale
    upper_numerator, upper_denominator = upper, scale
    p_previous_previous, p_previous = 0, 1
    q_previous_previous, q_previous = 1, 0
    coefficients: list[int] = []
    below: list[tuple[int, int, int, int, int]] = []

    for index in range(100000):
        lower_floor = lower_numerator // lower_denominator
        upper_floor = upper_numerator // upper_denominator
        assert lower_floor == upper_floor, (
            "the fixed-point enclosure exhausted its common CF prefix before "
            "the requested denominator cap"
        )
        coefficient = lower_floor
        coefficients.append(coefficient)
        numerator = coefficient * p_previous + p_previous_previous
        denominator = coefficient * q_previous + q_previous_previous
        assert denominator > 0 and math.gcd(numerator, denominator) == 1

        error_lower = lower * denominator - numerator * scale
        error_upper = upper * denominator - numerator * scale
        if error_lower > 0:
            below.append(
                (denominator, numerator, error_lower, error_upper, index)
            )
        else:
            assert error_upper < 0, "convergent side is not certified"

        lower_remainder = lower_numerator - coefficient * lower_denominator
        upper_remainder = upper_numerator - coefficient * upper_denominator
        p_previous_previous, p_previous = p_previous, numerator
        q_previous_previous, q_previous = q_previous, denominator
        if denominator > denominator_cap:
            break
        assert lower_remainder > 0 and upper_remainder > 0
        # Reciprocal reverses the interval.
        old_lower_denominator = lower_denominator
        old_upper_denominator = upper_denominator
        lower_numerator, lower_denominator = (
            old_upper_denominator,
            upper_remainder,
        )
        upper_numerator, upper_denominator = (
            old_lower_denominator,
            lower_remainder,
        )
    else:
        raise AssertionError("continued-fraction iteration cap reached")

    return coefficients, below, (numerator, denominator)


def native_admissible(exponent: int) -> bool:
    # Im((1-i)^N)<=0 exactly in the five residue classes below.
    return exponent % 8 in (0, 1, 2, 3, 4)


def scan_broad_window(
    lower: int,
    upper: int,
    scale: int,
    coefficients: list[int],
    below: list[tuple[int, int, int, int, int]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    first_relevant = 0
    factorial = 1

    for exponent in range(1, N_MAX + 1):
        factorial *= exponent
        if exponent < N_MIN:
            continue
        denominator_cap = math.isqrt(factorial)

        # Below-side convergent errors decrease with their index.  Discard
        # those whose certified lower normalized error is already at least 5.
        while first_relevant < len(below):
            denominator, _, error_lower, _, _ = below[first_relevant]
            if (
                exponent * factorial * error_lower
                >= 5 * scale * denominator
            ):
                first_relevant += 1
            else:
                break

        position = first_relevant
        while position < len(below):
            denominator, numerator, error_lower, error_upper, cf_index = below[
                position
            ]
            if denominator > denominator_cap:
                break
            normalized_lower = exponent * factorial * error_lower
            normalized_upper = exponent * factorial * error_upper
            normalized_denominator = scale * denominator
            if normalized_upper <= normalized_denominator:
                # Every subsequent below-side error is still smaller.
                break
            if normalized_lower < 5 * normalized_denominator:
                # The guard interval makes both boundary comparisons
                # decisive; no retained row merely straddles 1 or 5.
                assert normalized_lower > normalized_denominator
                assert normalized_upper < 5 * normalized_denominator
                assert cf_index + 1 < len(coefficients)
                lambda_value = Fraction(factorial, denominator * denominator)
                rows.append(
                    {
                        "N": exponent,
                        "N_mod_8": exponent % 8,
                        "native_admissible": native_admissible(exponent),
                        "continued_fraction_index_zero_based": cf_index,
                        "a_k": coefficients[cf_index],
                        "a_k_plus_1": coefficients[cf_index + 1],
                        "P": str(numerator),
                        "Q": str(denominator),
                        "P_digits": len(str(numerator)),
                        "Q_digits": len(str(denominator)),
                        "P_over_Q_sha256": literal_fraction_digest(
                            numerator, denominator
                        ),
                        "fraction_reduced": True,
                        "Q_le_floor_sqrt_factorial": True,
                        "lambda_N_factorial_over_Q_squared_lower": decimal_outward(
                            lambda_value.numerator,
                            lambda_value.denominator,
                            16,
                            "down",
                        ),
                        "lambda_N_factorial_over_Q_squared_upper": decimal_outward(
                            lambda_value.numerator,
                            lambda_value.denominator,
                            16,
                            "up",
                        ),
                        "normalized_error_lower": decimal_outward(
                            normalized_lower,
                            normalized_denominator,
                            16,
                            "down",
                        ),
                        "normalized_error_upper": decimal_outward(
                            normalized_upper,
                            normalized_denominator,
                            16,
                            "up",
                        ),
                        "normalized_error_interval_digests": {
                            "lower": literal_fraction_digest(
                                normalized_lower, normalized_denominator
                            ),
                            "upper": literal_fraction_digest(
                                normalized_upper, normalized_denominator
                            ),
                        },
                    }
                )
            position += 1

    return rows


def truncated_inverse_products(weights: list[int], degree: int) -> list[int]:
    """Asymptotic coefficients of sum_j weights[j]/prod_{r<=j+1}(N+r)."""
    answer = [0] * (degree + 1)
    for index, weight in enumerate(weights):
        shift = index + 1
        if shift > degree:
            continue
        polynomial = [1] + [0] * (degree - shift)
        for factor in range(1, index + 2):
            updated = [0] * len(polynomial)
            for target in range(len(polynomial)):
                total = 0
                sign = 1
                # Coefficients of (1+factor*x)^(-1).
                for source in range(target, -1, -1):
                    total += polynomial[source] * sign
                    sign *= -factor
                updated[target] = total
            polynomial = updated
        for power, coefficient in enumerate(polynomial):
            answer[shift + power] += weight * coefficient
    return answer


def asymptotic_coefficient_checks() -> dict[str, object]:
    # L0=5*A0+A1-7*A2+A3+O(A4), where
    # Aj=N!/(N+j+1)!.  e*B=A0+A1+A2+A3+O(A4).
    l0 = truncated_inverse_products([5, 1, -7, 1], 4)
    e_times_b = truncated_inverse_products([1, 1, 1, 1], 4)
    assert l0 == [0, 5, -4, -5, 45]
    assert e_times_b == [0, 1, 0, -1, 1]
    return {
        "L0_coefficients_N_inverse_powers_0_through_4": l0,
        "e_times_B_coefficients_N_inverse_powers_0_through_4": e_times_b,
        "Lmin_statement": (
            "Lmin=(e+2)B+O(B*tau), with "
            "tau~sqrt(2/(e*N*N!))"
        ),
    }


def verify_previous_package(rows: list[dict[str, object]]) -> dict[str, object]:
    manifest_hash = sha256(PREVIOUS_MANIFEST)
    assert manifest_hash == EXPECTED_PREVIOUS_MANIFEST_HASH
    manifest_lines = PREVIOUS_MANIFEST.read_text().splitlines()
    parsed_manifest = {}
    for line in manifest_lines:
        digest, relative = line.split("  ", 1)
        parsed_manifest[relative] = digest
    assert parsed_manifest == EXPECTED_PREVIOUS_HASHES
    for relative, expected in EXPECTED_PREVIOUS_HASHES.items():
        assert sha256(ROOT / relative) == expected

    previous = json.loads(PREVIOUS_JSON.read_text())
    prior_indices = previous["genuine_approximant_hit_indices"]
    assert prior_indices == EXPECTED_ADMISSIBLE_HITS
    prior_rows = {
        row["N"]: (row["P"], row["Q"])
        for row in previous[
            "finite_genuine_approximant_scan_exact_rational_rows"
        ]
    }
    current_rows = {row["N"]: (row["P"], row["Q"]) for row in rows}
    for exponent in prior_indices:
        assert current_rows[exponent] == prior_rows[exponent]
    return {
        "manifest_sha256": manifest_hash,
        "pinned_hashes": EXPECTED_PREVIOUS_HASHES,
        "certified_prior_hit_indices": prior_indices,
        "candidate_fraction_identity_verified": True,
    }


def main() -> None:
    source_audit = control_and_tex_audit(SOURCE)
    script_audit = control_and_tex_audit(Path(__file__))
    assert source_audit["clean"] and script_audit["clean"]

    factorial_max = math.factorial(N_MAX)
    factorial_digits = len(str(factorial_max))
    decimal_digits = factorial_digits + DECIMAL_GUARD_DIGITS
    scale = 10**decimal_digits
    lower, upper, series_metadata = scaled_s_interval(decimal_digits)
    assert upper - lower < 100000

    denominator_cap = math.isqrt(factorial_max)
    coefficients, below, first_beyond_cap = common_continued_fraction_prefix(
        lower, upper, scale, denominator_cap
    )
    assert first_beyond_cap[1] > denominator_cap
    rows = scan_broad_window(lower, upper, scale, coefficients, below)
    broad_indices = [row["N"] for row in rows]
    assert broad_indices == EXPECTED_BROAD_CANDIDATES
    admissible_indices = [row["N"] for row in rows if row["native_admissible"]]
    assert admissible_indices == EXPECTED_ADMISSIBLE_HITS

    previous_verification = verify_previous_package(rows)
    cf_prefix_text = ",".join(map(str, coefficients))
    payload = {
        "schema": "common_kernel_native_cf_window_scan_certificate_v1",
        "scope": (
            "Exact necessary-window and continued-fraction exhaustion for "
            "10<=N<=2000, combined with a hash-pinned prior exact membership "
            "certificate. No extrapolation beyond N=2000 and no irrationality "
            "or transcendence claim."
        ),
        "all_parameter_results_checked_symbolically": {
            "universal_hit_window": "1<N*N!*(s-P/Q)<5",
            "legendre_threshold": "N>=10 and Q^2<=N! imply P/Q is principal",
            "native_admissible_residues_mod_8": [0, 1, 2, 3, 4],
            "asymptotic_coefficients": asymptotic_coefficient_checks(),
        },
        "exact_fixed_point_enclosure": {
            "N_max": N_MAX,
            "factorial_digits": factorial_digits,
            "guard_digits": DECIMAL_GUARD_DIGITS,
            "decimal_digits": decimal_digits,
            "lower_integer_sha256": hashlib.sha256(str(lower).encode()).hexdigest(),
            "upper_integer_sha256": hashlib.sha256(str(upper).encode()).hexdigest(),
            "series_metadata": series_metadata,
        },
        "continued_fraction_certificate": {
            "common_prefix_length": len(coefficients),
            "common_prefix_sha256": hashlib.sha256(
                cf_prefix_text.encode()
            ).hexdigest(),
            "last_denominator_exceeds_floor_sqrt_2000_factorial": True,
            "floor_sqrt_2000_factorial_digits": len(str(denominator_cap)),
            "first_denominator_beyond_cap_digits": len(
                str(first_beyond_cap[1])
            ),
            "first_convergent_beyond_cap_sha256": literal_fraction_digest(
                first_beyond_cap[0], first_beyond_cap[1]
            ),
            "certified_below_convergents_stored_internally": len(below),
        },
        "finite_scan": {
            "N_min": N_MIN,
            "N_max": N_MAX,
            "broad_candidate_indices": broad_indices,
            "native_admissible_candidate_indices": admissible_indices,
            "excluded_only_by_native_sign_indices": [86, 351, 1477],
            "new_admissible_hits_after_331": [],
            "rows": rows,
        },
        "pinned_previous_membership_certificate": previous_verification,
        "source_sha256": sha256(SOURCE),
        "control_and_tex_audit": {
            "source": source_audit,
            "script": script_audit,
        },
        "resource_policy": {
            "rss_cap_kib": RSS_CAP_KIB,
            "measured_peak_rss": (
                "checked against cap and printed at replay time; omitted from "
                "JSON for byte determinism"
            ),
            "accelerator": "not used; exact integer and rational arithmetic",
        },
    }

    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_CAP_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
