#!/usr/bin/env python3
"""Deterministic exact certificate for work Item 414.

The uniform theorem is proved in the report by Lucas' theorem and the root
set of binom(X,4m) modulo primes larger than 4m.  This checker pins the
canonical inputs and normalizes that proof on declared finite rows.  It does
not turn a finite check into an all-m theorem and does not claim to certify
the prime number theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SCHEMA_MAX_M = 256
SELECTED_M = (1, 2, 3, 10, 33, 109, 122, 128)

DEPENDENCIES = {
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "sources/mixed_cubic_boundary_cartier_content_and_recurrence.md":
        "286d9cf4d3591a1a9b9fefc6dd3ee3dcc9f7c2ba49a73310909491814544d9e8",
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "sources/item410_mixed_cubic_compatible_scalar_carrier_report.md":
        "c6dc7e439d2f828ec4d2d06ff0ca2aeef99946a70741e2ed8f25673e6e6e1157",
    "scripts/item410_mixed_cubic_compatible_scalar_carrier_certificate.py":
        "22617882e636dd2944f0166374bbc4e5a2bd063f82d44719779d956b24afece6",
    "results/item410_mixed_cubic_compatible_scalar_carrier_certificate.json":
        "e327dd22d615bb474027067f470082143cf39315aa5ff0814ddcf2aa131b31ed",
    "results/item410_mixed_cubic_compatible_scalar_carrier_certificate_replay.json":
        "e327dd22d615bb474027067f470082143cf39315aa5ff0814ddcf2aa131b31ed",
    "results/item410_mixed_cubic_compatible_scalar_carrier_root_replay.json":
        "e327dd22d615bb474027067f470082143cf39315aa5ff0814ddcf2aa131b31ed",
    "results/item410_mixed_cubic_compatible_scalar_carrier_ledger_delta.json":
        "443521b03db53990a0e0b82f1b33e9ceb1d90fbcf0affa26a0dfde7d10f90d0e",
    "manifests/item410_mixed_cubic_compatible_scalar_carrier_manifest.json":
        "672b877ebd83fda20b0dff198b2db3b6ba4eba5ebbad661bcfb1b2566ecab63d",
    "results/item410_mixed_cubic_compatible_scalar_carrier_root_audit.json":
        "dcc66283f87d242724d831e68f32f0dede8ae0102f69c88403b4fb2ac64191ad",
    "results/item410_mixed_cubic_compatible_scalar_carrier_hashes.sha256":
        "fbe49b6d16b857152b9d49acda595d397b21f960c5a02a10973f87d081f6b806",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_dependencies() -> dict[str, str]:
    observed = {}
    for relative, expected in DEPENDENCIES.items():
        digest = sha256_bytes((ROOT / relative).read_bytes())
        assert digest == expected, (relative, expected, digest)
        observed[relative] = digest
    return observed


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(limit + 1) if sieve[value]]


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= value - index
    return answer / math.factorial(degree)


def descending_binomial_values(
    initial: Fraction, degree: int, length: int
) -> list[Fraction]:
    value = generalized_binomial(initial, degree)
    answer = []
    for offset in range(length):
        answer.append(value)
        value *= Fraction(initial - offset - degree, initial - offset)
    return answer


def r_scalars(m_value: int) -> tuple[Fraction, Fraction]:
    degree = 4 * m_value
    even_bins = descending_binomial_values(
        Fraction(2 * m_value - 1, 2), degree, 3 * m_value + 1
    )
    even = sum(
        (-1) ** index
        * math.comb(6 * m_value, 2 * index)
        * even_bins[index]
        for index in range(3 * m_value + 1)
    )
    odd_bins = descending_binomial_values(
        Fraction(2 * m_value - 3, 2), degree, 3 * m_value
    )
    odd = sum(
        (-1) ** index
        * math.comb(6 * m_value, 2 * index + 1)
        * odd_bins[index]
        for index in range(3 * m_value)
    )
    return even, odd


def s_scalar_for_residue(
    m_value: int, residue: int, upper_offset: int
) -> Fraction:
    degree = 4 * m_value
    numerator_degree = 10 * m_value + 1
    indices = list(range(residue, numerator_degree + 1, 4))
    bins = descending_binomial_values(
        Fraction(10 * m_value - upper_offset - residue, 4),
        degree,
        len(indices),
    )
    return sum(
        (-1) ** index * math.comb(numerator_degree, index) * value
        for index, value in zip(indices, bins)
    )


def s_scalars(m_value: int, phase: int) -> tuple[Fraction, Fraction]:
    assert phase in (0, 2)
    return (
        s_scalar_for_residue(m_value, phase, 1),
        s_scalar_for_residue(m_value, (phase - 1) % 4, 2),
    )


def forced_primes(m_value: int, prime_table: list[int]) -> list[int]:
    return [
        prime for prime in prime_table if 4 * m_value < prime < 6 * m_value
    ]


def product(values: list[int]) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def remove_prime_support_at_most(
    value: int, bound: int, prime_table: list[int]
) -> int:
    answer = abs(value)
    for prime in prime_table:
        if prime > bound:
            break
        while answer and answer % prime == 0:
            answer //= prime
    return answer


def lucas_root_schema() -> dict[str, object]:
    """Finite normalization of every algebraic case in Sections 2 and 3."""
    prime_table = primes_up_to(6 * SCHEMA_MAX_M)
    case_counts = {
        "E_low": 0,
        "E_high": 0,
        "O_low": 0,
        "O_high": 0,
        "U_matching_terms": 0,
        "V_matching_terms": 0,
        "opposite_phase_gap_rows": 0,
    }
    witness_lines = []
    forced_prime_pairs = 0

    for m_value in range(1, SCHEMA_MAX_M + 1):
        for prime in forced_primes(m_value, prime_table):
            forced_prime_pairs += 1
            assert prime > 4 * m_value >= 4
            a_value = 6 * m_value - prime
            assert 1 <= a_value < 2 * m_value < prime
            assert a_value % 2 == 1

            # Lucas survivors for the E terms r=2j.
            for r_value in range(0, 6 * m_value + 1, 2):
                if r_value <= a_value:
                    numerator = 2 * m_value - r_value - 1 + prime
                    assert numerator % 2 == 0
                    root = numerator // 2
                    case_counts["E_low"] += 1
                elif r_value >= prime:
                    s_value = r_value - prime
                    assert 0 <= s_value <= a_value and s_value % 2 == 1
                    numerator = 2 * m_value - s_value - 1
                    assert numerator % 2 == 0
                    root = numerator // 2
                    case_counts["E_high"] += 1
                else:
                    continue
                assert 0 <= root < 4 * m_value
                x_numerator = 2 * m_value - r_value - 1
                assert (2 * root - x_numerator) % prime == 0

            # Lucas survivors for the O terms r=2j+1.
            for r_value in range(1, 6 * m_value + 1, 2):
                if r_value <= a_value:
                    numerator = 2 * m_value - 2 - r_value + prime
                    assert numerator % 2 == 0
                    root = numerator // 2
                    case_counts["O_low"] += 1
                elif r_value >= prime:
                    s_value = r_value - prime
                    assert 0 <= s_value <= a_value and s_value % 2 == 0
                    numerator = 2 * m_value - 2 - s_value
                    assert numerator % 2 == 0
                    root = numerator // 2
                    case_counts["O_high"] += 1
                else:
                    continue
                assert 0 <= root < 4 * m_value
                x_numerator = 2 * m_value - 2 - r_value
                assert (2 * root - x_numerator) % prime == 0

            n_value = prime - 6 * m_value - 1
            phase = n_value % 4
            assert n_value < 0 and phase in (0, 2)
            numerator_degree = 10 * m_value + 1

            for h_value in range(phase, numerator_degree + 1, 4):
                numerator = 10 * m_value + prime - 1 - h_value
                assert numerator % 4 == 0
                root = numerator // 4
                assert 0 <= root < 4 * m_value
                target_numerator = 10 * m_value - 1 - h_value
                assert (4 * root - target_numerator) % prime == 0
                case_counts["U_matching_terms"] += 1

            previous_residue = (phase - 1) % 4
            for h_value in range(previous_residue, numerator_degree + 1, 4):
                numerator = 10 * m_value + prime - 2 - h_value
                assert numerator % 4 == 0
                root = numerator // 4
                assert 0 <= root < 4 * m_value
                target_numerator = 10 * m_value - 2 - h_value
                assert (4 * root - target_numerator) % prime == 0
                case_counts["V_matching_terms"] += 1

            # Normalize the opposite-phase coefficient interpretation and
            # exact two-point support gap from report Section 3.
            opposite_phase = (phase + 2) % 4
            n_prime = 3 * prime - 6 * m_value - 1
            h_exponent = prime - 4 * m_value - 1
            degree_r = prime - a_value - 3
            assert h_exponent >= 0
            assert n_prime % 4 == opposite_phase
            assert 0 < n_prime < 4 * prime
            assert 10 * m_value + 1 + h_exponent == prime + 6 * m_value
            assert (
                a_value + 3 * h_exponent
                == degree_r
                == prime - a_value - 3
            )
            assert n_prime == 2 * prime - a_value - 1
            assert n_prime - 1 == prime + degree_r + 1
            assert n_prime == prime + degree_r + 2
            assert n_prime < 2 * prime

            for h_value in range(opposite_phase, numerator_degree + 1, 4):
                assert (n_prime - h_value) % 4 == 0
                upper_four = 16 * m_value + n_prime - h_value
                target_four = 10 * m_value - 1 - h_value
                assert (upper_four - target_four) % prime == 0
                if h_value > n_prime:
                    assert upper_four % 4 == 0
                    extension_root = upper_four // 4
                    assert upper_four >= 3 * prime - 2
                    assert 0 < extension_root < 4 * m_value
            opposite_previous = (opposite_phase - 1) % 4
            for h_value in range(
                opposite_previous, numerator_degree + 1, 4
            ):
                assert (n_prime - 1 - h_value) % 4 == 0
                upper_four = 16 * m_value + n_prime - 1 - h_value
                target_four = 10 * m_value - 2 - h_value
                assert (upper_four - target_four) % prime == 0
                if h_value > n_prime - 1:
                    assert upper_four % 4 == 0
                    extension_root = upper_four // 4
                    assert upper_four >= 3 * prime - 3
                    assert 0 < extension_root < 4 * m_value
            case_counts["opposite_phase_gap_rows"] += 1

            witness_lines.append(
                f"{m_value}:{prime}:{a_value}:{phase}"
            )

    witness = "\n".join(witness_lines).encode("ascii")
    return {
        "declared_finite_normalization_range": f"1<=m<={SCHEMA_MAX_M}",
        "forced_prime_pairs": forced_prime_pairs,
        "case_counts": case_counts,
        "all_denominator_units_checked": True,
        "all_Lucas_survivors_land_in_binomial_root_set": True,
        "matching_phase_U_V_terms_land_in_binomial_root_set": True,
        "opposite_phase_two_point_gap_verified": True,
        "opposite_phase_extension_terms_vanish": True,
        "finite_rows_are_not_the_uniform_proof": True,
        "witness_sha256": sha256_bytes(witness),
    }


def exact_selected_rows() -> list[dict[str, object]]:
    prime_table = primes_up_to(6 * max(SELECTED_M))
    rows = []
    for m_value in SELECTED_M:
        even, odd = r_scalars(m_value)
        u_zero, v_zero = s_scalars(m_value, 0)
        u_two, v_two = s_scalars(m_value, 2)
        assert all(
            value.denominator > 0
            and value.denominator & (value.denominator - 1) == 0
            for value in (even, odd, u_zero, v_zero, u_two, v_two)
        )
        w_value = math.gcd(abs(even.numerator), abs(odd.numerator))
        j_zero = math.gcd(
            w_value, abs(u_zero.numerator), abs(v_zero.numerator)
        )
        j_two = math.gcd(
            w_value, abs(u_two.numerator), abs(v_two.numerator)
        )
        interval_primes = forced_primes(m_value, prime_table)
        q_value = product(interval_primes)
        item200_j0_primes = [
            prime for prime in interval_primes if prime > 4 * m_value + 1
        ]
        d_value = product(item200_j0_primes)
        boundary_value = (
            4 * m_value + 1
            if 4 * m_value + 1 in interval_primes
            else 1
        )
        assert q_value == d_value * boundary_value
        phase_primes = {
            phase: [
                prime for prime in interval_primes
                if (prime - 6 * m_value - 1) % 4 == phase
            ]
            for phase in (0, 2)
        }
        q_zero = product(phase_primes[0])
        q_two = product(phase_primes[2])
        assert q_zero * q_two == q_value
        assert even.numerator % q_value == 0
        assert odd.numerator % q_value == 0
        assert w_value % q_value == 0
        assert j_zero % q_zero == 0
        assert j_two % q_two == 0
        assert j_zero % q_value == 0
        assert j_two % q_value == 0
        residual_zero = remove_prime_support_at_most(
            j_zero, 6 * m_value, prime_table
        )
        residual_two = remove_prime_support_at_most(
            j_two, 6 * m_value, prime_table
        )
        rows.append(
            {
                "m": m_value,
                "forced_primes": interval_primes,
                "Q_m": str(q_value),
                "Item200_D_m": str(d_value),
                "optional_boundary_factor": str(boundary_value),
                "Q_m_equals_D_m_times_boundary": True,
                "W_m_div_Q_m": str(w_value // q_value),
                "phase_0_forced_primes": phase_primes[0],
                "phase_2_forced_primes": phase_primes[2],
                "matching_phase_divisibility_verified": True,
                "opposite_phase_gap_divisibility_verified": True,
                "Q_m_divides_both_phase_carriers_on_this_row": True,
                "phase_0_residual_after_all_primes_at_most_6m": str(
                    residual_zero
                ),
                "phase_2_residual_after_all_primes_at_most_6m": str(
                    residual_two
                ),
                "finite_only": True,
            }
        )
    return rows


def run() -> dict[str, object]:
    dependencies = verify_dependencies()
    schema = lucas_root_schema()
    selected = exact_selected_rows()
    raw_constant = (14 * math.log(2) + 4 * math.log(3 * math.e / 2)) / 6
    stripped_constant = raw_constant - 1 / 3
    inherited_ceiling = math.log(136) / 6
    assert stripped_constant < raw_constant
    assert stripped_constant > inherited_ceiling
    witness = json.dumps(
        {
            "dependencies": dependencies,
            "schema_witness": schema["witness_sha256"],
            "selected": selected,
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return {
        "schema": "item414-mixed-scalar-forced-interval-v1",
        "item": 414,
        "status": "CANONICAL_ROOT_AUDITED_NO_BOOKING",
        "labels": {
            "PROVED_IN_REPORT": [
                "Q_m=product of primes 4m<ell<6m divides num(E_m) and num(O_m)",
                "Q_m divides both J_(m,0) and J_(m,2)",
                "the actual H support is bounded by rad_(>6m)(W_m)",
                "the full-radical o(m) target must be replaced by a large-prime radical target",
                "zero booking and zero proved capacity reduction",
            ],
            "EXACT_FINITE_ONLY": [
                "the proof-schema normalization through m=256",
                "the selected exact rational carrier rows",
                "any selected residual after removing primes at most 6m",
            ],
            "OPEN": [
                "uniform nonresonance of E_m,O_m",
                "log rad_(>6m)(W_m)=o(m)",
                "the phasewise large-prime radical theorem",
                "the four-adjacent lemma and primitive or marked branch control",
                "Route 1 and irrationality of e+pi",
            ],
        },
        "uniform_formulas": {
            "Item200_provenance": "Q_m is the j=0 strip D_m times the optional boundary prime 4m+1; the full prior forced source is F_m=G_m",
            "forced_product": "Q_m=prod_(4m<ell<6m, ell prime) ell",
            "forced_divisibility": "Q_m | num(E_m), num(O_m), hence Q_m | W_m when W_m>0",
            "phase": "delta_ell=ell-6m-1 mod 4 in {0,2}",
            "phase_forced_divisibility": "Q_m | J_(m,0) and Q_m | J_(m,2)",
            "corrected_actual_target": "log rad_(>6m)(W_m)=o(m), with uniform nonresonance",
        },
        "capacity": {
            "booking_delta": 0,
            "proved_total_capacity_ceiling_delta": 0,
            "raw_Item410_height_constant": format(raw_constant, ".15f"),
            "forced_interval_stripped_height_constant_using_PNT": format(
                stripped_constant, ".15f"
            ),
            "inherited_combined_ceiling": format(inherited_ceiling, ".15f"),
            "stripped_bound_is_still_noncompetitive": True,
            "PNT_is_invoked_in_report_not_certified_by_replay": True,
        },
        "proof_schema_normalization": schema,
        "selected_exact_rows": selected,
        "dependency_sha256": dependencies,
        "assertions": {
            "denominator_units_separated_from_numerator_divisibility": True,
            "ell_2_and_3_and_endpoints_excluded": True,
            "W_distinguished_from_phase_J": True,
            "opposite_phase_gap_is_uniform_not_finite_extrapolation": True,
            "finite_checks_not_promoted": True,
            "no_PNT_certificate_claim": True,
            "booking_delta_is_zero": True,
        },
        "witness_sha256": sha256_bytes(witness),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay", type=Path)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    payload = run()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )
    if arguments.replay:
        assert arguments.replay.read_bytes() == rendered
    print(sha256_bytes(rendered))
    if arguments.output:
        arguments.output.write_bytes(rendered)


if __name__ == "__main__":
    main()
