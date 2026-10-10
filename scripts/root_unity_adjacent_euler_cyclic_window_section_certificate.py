#!/usr/bin/env python3
"""Replay the cyclic Euler bounded-window polynomial-section obstruction.

All-parameter proofs are in the companion source.  This script checks the
cyclic convolution normalization, exact anchor sections on declared grids,
and the full N=1643, p=151483 synthetic low-window completion.  It does not
extrapolate finite data to a product estimate or a classification of e+pi.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT / "sources/root_unity_adjacent_euler_cyclic_window_section_no_go.md"
)
OUTPUT = (
    ROOT
    / "results/root_unity_adjacent_euler_cyclic_window_section_certificate.json"
)

# Failure guard only.  It neither allocates nor caps the available Colab RAM.
RSS_GUARD_KIB = 8 * 1024 * 1024

DEPENDENCIES = {
    "results/root_unity_adjacent_euler_first_period_moment_hashes.sha256":
        "af340ed10de55eb9587fdb3167d475b7f5cda405367fedb3ca00244ed1b23adf",
}

PRIME_GRID = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 43, 61, 101]
SECTION_MODULUS = 1_000_003
SEED_P = 151_483
SEED_N = 1_643


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_u32(values: list[int]) -> str:
    digest = hashlib.sha256()
    for value in values:
        digest.update(int(value).to_bytes(4, "little"))
    return digest.hexdigest()


def sha256_index_values(values: dict[int, int]) -> str:
    digest = hashlib.sha256()
    for index, value in sorted(values.items()):
        digest.update(int(index).to_bytes(4, "little"))
        digest.update(int(value).to_bytes(4, "little"))
    return digest.hexdigest()


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte != 10
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def trial_prime(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    for divisor in range(3, math.isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def secant_even_mod(max_n: int, modulus: int) -> list[int]:
    """E_0,E_2,...,E_(2 max_n) modulo a prime above 2 max_n."""
    assert trial_prime(modulus)
    assert 2 * max_n < modulus
    factorial = [1] * (2 * max_n + 1)
    for index in range(1, len(factorial)):
        factorial[index] = factorial[index - 1] * index % modulus
    inverse_factorial = [1] * len(factorial)
    inverse_factorial[-1] = pow(factorial[-1], -1, modulus)
    for index in range(len(factorial) - 1, 0, -1):
        inverse_factorial[index - 1] = (
            inverse_factorial[index] * index % modulus
        )

    values = [1]
    for n in range(1, max_n + 1):
        factorial_2n = factorial[2 * n]
        total = 0
        for k in range(n):
            choose = (
                factorial_2n
                * inverse_factorial[2 * k]
                % modulus
                * inverse_factorial[2 * n - 2 * k]
                % modulus
            )
            total = (total + choose * values[k]) % modulus
        values.append((-total) % modulus)
    return values


def cyclic_convolution_dense(values: list[int], modulus: int) -> list[int]:
    length = len(values)
    output = [0] * length
    for i, left in enumerate(values):
        for j, right in enumerate(values):
            output[(i + j) % length] = (
                output[(i + j) % length] + left * right
            ) % modulus
    return output


def cyclic_value_sparse(
    values: dict[int, int],
    target: int,
    period: int,
    modulus: int,
) -> int:
    return sum(
        left * values.get((target - index) % period, 0)
        for index, left in values.items()
    ) % modulus


def cyclic_interval(start: int, length: int, period: int) -> set[int]:
    return {(start + offset) % period for offset in range(length)}


def sumset(left: set[int], right: set[int], period: int) -> set[int]:
    return {(a + b) % period for a in left for b in right}


def negated(values: set[int], period: int) -> set[int]:
    return {(-value) % period for value in values}


def anchor_conditions(
    period: int,
    prescribed: set[int],
    targets: set[int],
    anchor: int,
) -> dict[str, bool]:
    anchor %= period
    partners = {(target - anchor) % period for target in targets}
    anchor_plus_prescribed = {
        (anchor + value) % period for value in prescribed
    }
    partner_plus_prescribed = sumset(partners, prescribed, period)
    partner_plus_partner = sumset(partners, partners, period)
    checks = {
        "anchor_not_prescribed": anchor not in prescribed,
        "partners_disjoint_prescribed": not (partners & prescribed),
        "anchor_plus_prescribed_avoids_targets":
            not (anchor_plus_prescribed & targets),
        "partners_plus_prescribed_avoid_targets":
            not (partner_plus_prescribed & targets),
        "twice_anchor_avoids_targets":
            (2 * anchor) % period not in targets,
        "partners_plus_partners_avoid_targets":
            not (partner_plus_partner & targets),
    }
    return checks


def construct_section(
    period: int,
    prescribed_values: dict[int, int],
    target_values: dict[int, int],
    anchor: int,
    modulus: int,
) -> tuple[dict[int, int], dict[int, int]]:
    prescribed = set(prescribed_values)
    targets = set(target_values)
    checks = anchor_conditions(period, prescribed, targets, anchor)
    assert all(checks.values()), checks

    values = {index: value % modulus for index, value in prescribed_values.items()}
    values[anchor % period] = 1
    partners = {}
    inverse_two = pow(2, -1, modulus)
    for target in sorted(targets):
        low_contribution = sum(
            left
            * prescribed_values.get((target - index) % period, 0)
            for index, left in prescribed_values.items()
        ) % modulus
        partner = (target - anchor) % period
        assert partner not in values
        partner_value = (
            (target_values[target] - low_contribution) * inverse_two
        ) % modulus
        values[partner] = partner_value
        partners[target] = partner

    for target, wanted in target_values.items():
        actual = cyclic_value_sparse(values, target, period, modulus)
        assert actual == wanted % modulus, (target, actual, wanted)
    return values, partners


def cyclic_euler_grid() -> list[dict[str, object]]:
    rows = []
    for p in PRIME_GRID:
        assert trial_prime(p)
        r = (p - 1) // 2
        euler = secant_even_mod(r, p)
        coefficients = [euler[r]] + euler[1:r]
        convolution = cyclic_convolution_dense(coefficients, p)
        assert convolution == [1] + [0] * (r - 1)
        assert coefficients[0] == (1 - (-1) ** r) % p
        reflection_matches = [
            k
            for k in range(1, r)
            if 2 * (r - k) % (2 * r) == 2 * k % (2 * r)
        ]
        expected_matches = [r // 2] if r % 2 == 0 else []
        assert reflection_matches == expected_matches
        rows.append(
            {
                "p": p,
                "r": r,
                "a_0_E_p_minus_1_mod_p": coefficients[0],
                "coefficient_sha256_u32le": sha256_u32(coefficients),
                "cyclic_convolution_sha256_u32le":
                    sha256_u32(convolution),
                "A_squared_is_1_mod_X_to_r_minus_1": True,
                "Kummer_reflection_match_half_indices":
                    reflection_matches,
            }
        )
    return rows


def initial_interval_grid() -> list[dict[str, object]]:
    rows = []
    cases = [
        (31, 3, 4),
        (47, 6, 5),
        (73, 8, 9),
        (101, 12, 10),
        (151, 17, 13),
    ]
    for period, low_end, target_end in cases:
        assert period > 2 * low_end + 3 * target_end + 2
        anchor = low_end + target_end + 1
        prescribed_values = {
            index: (17 * index * index + 31 * index + 9) % SECTION_MODULUS
            for index in range(low_end + 1)
        }
        target_values = {
            index: (23 * index + 5) % SECTION_MODULUS
            for index in range(target_end + 1)
        }
        values, partners = construct_section(
            period,
            prescribed_values,
            target_values,
            anchor,
            SECTION_MODULUS,
        )
        assert min(partners.values()) == period - anchor
        assert max(partners.values()) == period - anchor + target_end
        rows.append(
            {
                "period": period,
                "L": low_end,
                "K": target_end,
                "threshold_rhs": 2 * low_end + 3 * target_end + 2,
                "anchor": anchor,
                "partner_interval": [
                    min(partners.values()),
                    max(partners.values()),
                ],
                "prescribed_digest": sha256_index_values(prescribed_values),
                "target_digest": sha256_index_values(target_values),
                "completion_digest": sha256_index_values(values),
                "all_target_convolutions_verified": True,
            }
        )
    return rows


def arbitrary_interval_grid() -> list[dict[str, object]]:
    rows = []
    cases = [
        (97, 4, 3, 11, 47),
        (149, 7, 5, 131, 61),
        (211, 9, 7, 205, 103),
    ]
    for period, low_length, target_length, low_start, target_start in cases:
        # Parameters L,K are cardinality minus one.
        L = low_length - 1
        K = target_length - 1
        assert period > 3 * L + 11 * K + 7
        prescribed = cyclic_interval(low_start, low_length, period)
        targets = cyclic_interval(target_start, target_length, period)
        anchors = [
            candidate
            for candidate in range(period)
            if all(
                anchor_conditions(
                    period, prescribed, targets, candidate
                ).values()
            )
        ]
        assert anchors
        anchor = anchors[0]
        prescribed_values = {
            index: (29 * index + 7) % SECTION_MODULUS
            for index in prescribed
        }
        target_values = {
            index: (37 * index + 11) % SECTION_MODULUS
            for index in targets
        }
        values, partners = construct_section(
            period,
            prescribed_values,
            target_values,
            anchor,
            SECTION_MODULUS,
        )
        rows.append(
            {
                "period": period,
                "S_start": low_start,
                "S_cardinality": low_length,
                "T_start": target_start,
                "T_cardinality": target_length,
                "forbidden_union_bound": 3 * L + 11 * K + 7,
                "admissible_anchor_count": len(anchors),
                "first_anchor": anchor,
                "partner_count": len(set(partners.values())),
                "completion_digest": sha256_index_values(values),
                "all_target_convolutions_verified": True,
            }
        )
    return rows


def seed_section() -> dict[str, object]:
    p = SEED_P
    n = SEED_N
    r = (p - 1) // 2
    L = K = n + 1
    anchor = L + K + 1
    assert trial_prime(p)
    assert r > 2 * L + 3 * K + 2
    assert anchor == 3_289

    euler = secant_even_mod(L, p)
    a_0 = (1 - (-1) ** r) % p
    prescribed_values = {0: a_0}
    prescribed_values.update({index: euler[index] for index in range(1, L + 1)})
    assert prescribed_values[n] == prescribed_values[n + 1] == 0

    target_values = {index: (1 if index == 0 else 0) for index in range(K + 1)}
    completion, partners = construct_section(
        r,
        prescribed_values,
        target_values,
        anchor,
        p,
    )
    assert min(partners.values()) == 72_452
    assert max(partners.values()) == 74_096
    assert len(set(partners.values())) == K + 1

    verified_values = [
        cyclic_value_sparse(completion, target, r, p)
        for target in range(K + 1)
    ]
    assert verified_values == [1] + [0] * K
    following = {
        str(target): cyclic_value_sparse(completion, target, r, p)
        for target in range(K + 1, K + 10)
    }
    assert following[str(K + 1)] == 131_736
    assert following[str(K + 1)] != 0

    selected_values = [
        completion[partners[target]]
        for target in range(K + 1)
    ]
    return {
        "N": n,
        "p": p,
        "r": r,
        "L": L,
        "K": K,
        "section_threshold_rhs": 2 * L + 3 * K + 2,
        "anchor": anchor,
        "partner_interval": [
            min(partners.values()),
            max(partners.values()),
        ],
        "partner_count": len(partners),
        "a_0": a_0,
        "a_N": prescribed_values[n],
        "a_N_plus_1": prescribed_values[n + 1],
        "low_prefix_sha256_u32le": sha256_u32(
            [prescribed_values[index] for index in range(L + 1)]
        ),
        "selected_partner_values_sha256_u32le":
            sha256_u32(selected_values),
        "selected_partner_values_first_five": selected_values[:5],
        "selected_partner_values_last_five": selected_values[-5:],
        "sparse_completion_entry_count": len(completion),
        "sparse_completion_sha256_index_u32le":
            sha256_index_values(completion),
        "verified_window": [0, K],
        "verified_window_digest_u32le": sha256_u32(verified_values),
        "following_convolution_values": following,
        "next_equation_fails": True,
        "scope": (
            "A synthetic section of the stated window, not the actual "
            "global Euler square root."
        ),
    }


def main() -> None:
    started = time.perf_counter()

    dependency_checks = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependency_checks[relative] = {
            "expected": expected,
            "actual": actual,
        }

    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__))
    assert source_control["clean"] and script_control["clean"]
    assert trial_prime(SECTION_MODULUS)

    payload = {
        "schema":
            "root_unity_adjacent_euler_cyclic_window_section_certificate_v1",
        "logical_scope": (
            "Exact replay for an all-parameter polynomial-section theorem "
            "for bounded cyclic-convolution windows. It proves that these "
            "windows add no low-coefficient eliminant, but proves no bound "
            "for J_N, no global full-system obstruction, and no "
            "classification of e+pi."
        ),
        "all_parameter_theorem": {
            "cyclic_equations":
                "F_t=sum_i a_i a_(t-i mod r)=delta_(t,0)",
            "anchor_section": (
                "Under the six disjoint-sum conditions, a_u=1 and "
                "a_(t-u)=(c_t-B_t)/2 give a polynomial section."
            ),
            "elimination": (
                "The bounded-window convolution ideal intersects the "
                "prescribed low-data ring in zero; after any base low-data "
                "ideal J, the intersection is exactly J."
            ),
            "initial_interval_threshold": "r>2L+3K+2",
            "arbitrary_interval_threshold": "r>3L+11K+7",
            "product_scale": (
                "For L=K=N+1, primes p<=10N+15 have total log O(N), "
                "while every p>10N+15 lies in the section regime."
            ),
        },
        "prime_grid_cyclic_euler_checks": cyclic_euler_grid(),
        "initial_interval_section_grid": initial_interval_grid(),
        "arbitrary_interval_section_grid": arbitrary_interval_grid(),
        "seed_section": seed_section(),
        "dependency_checks": dependency_checks,
        "source_sha256": sha256(SOURCE),
        "control_audit": {
            "source": source_control,
            "script": script_control,
        },
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "Failure guard only; it neither allocates nor limits the "
                "approximately 50 GiB available Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: exact modular sparse convolution and recurrence "
                "are CPU-suitable and small."
            ),
        },
        "missing_lemma": (
            "A genuinely nonlocal cross-prime coupling using the full "
            "cyclic system or arithmetic of the actual alternating sign "
            "assignment, with a subfactorial-height integer consequence."
        ),
    }

    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_GUARD_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()

