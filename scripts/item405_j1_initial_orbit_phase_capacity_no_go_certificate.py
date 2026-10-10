#!/usr/bin/env python3
"""Deterministic exact controls for Item 405.

The all-prime initial-orbit theorem, capacity comparison, and interpolation
no-go are proved in the report.  This standard-library checker pins the
canonical Items 218, 293, 360, 363, 391, 395, 398, 400 and the complete work
Item 401 package.  It verifies the six exact Hasse initials, their phase-
compatible prime divisors, the transverse residues at the resulting finite
candidate list, fixed-prime ages, and one exact order-four interpolation
countermodel.  It performs no unbounded prime scan and makes no density
inference from the declared finite control.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = (
    ROOT / "results" / "item405_j1_initial_orbit_phase_capacity_no_go_certificate.json"
)


DEPENDENCIES = {
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "results/item218_j1_common_log_manifest.json":
        "e1c6c3d713670c819b5f27b1005db26f9b804ec8ee0766671928fc30c1ff6d8d",
    "sources/item293_j1_E_gate_density_no_go_report.md":
        "d87baac933defb82511f50942a9d3ab09ef1dcdc341be507e163b04050537804",
    "manifests/item293_j1_E_gate_density_no_go_manifest.json":
        "7103f8d2db60315bb9c3128cebe9afb80615ba30eb58314f85088e17845619e2",
    "sources/item360_j1_full_gate_transverse_period_report.md":
        "4468412fb8631924952dc7f70fc4e75433a7524954b89525de508e55feefc8c4",
    "manifests/item360_j1_full_gate_transverse_period_manifest.json":
        "92f88a56162f3803b8699922da921333f5225c41a32d14c87641dd53c3f8b55b",
    "sources/item363_j1_joint_gate_crt_elimination_no_go_report.md":
        "377ed30c0c6be630c124ccd3050d37176264c659d23a502453a9aaa34ff132ee",
    "manifests/item363_j1_joint_gate_crt_elimination_no_go_manifest.json":
        "46aa9a81d3b92cd5e7e055d9280f32e0e5ca32b91dfd68d95cbc9fdaa26a464a",
    "sources/item391_j1_logarithmic_spacing_resultant_criterion_report.md":
        "304713605fcf33675a882b4f333d60cc35fd36bc6b860353eff36472d4a27564",
    "manifests/item391_j1_logarithmic_spacing_resultant_criterion_manifest.json":
        "07e4a438dbc32e52e67587d7a0fe4886d23e584fd7fae34aafe7f234c334e511",
    "sources/item395_j1_logscale_cluster_radical_height_obstruction_report.md":
        "af0d85607d665f5d6c12c2695a44a89d984abffb008bbd1318978471e79f4487",
    "manifests/item395_j1_logscale_cluster_radical_height_obstruction_manifest.json":
        "3ef54ba9d3caa5af1b76bde52822447e253256c4c0ebb30dd6bb8a6200502cbd",
    "sources/item398_j1_aggregate_endpoint_resultant_graph_valuation_no_go_report.md":
        "3773d8209ea6e5b08f524cc44f582739baa6393a9cb362a8e5cc0f9f34f13da4",
    "manifests/item398_j1_aggregate_endpoint_resultant_graph_valuation_no_go_manifest.json":
        "d62e46075fd88086ffdba4b05545cf57ac52ab9dc981941faf5352b71cf9a69f",
    "sources/item400_j1_discriminant_energy_sieve_threshold_no_go_report.md":
        "f9dfe5dd6082ec762c0e677760aff5367c1fd869241ed29a4fa50fc78dab124e",
    "manifests/item400_j1_discriminant_energy_sieve_threshold_no_go_manifest.json":
        "ffa52a35f31b98c717050dd1b01dfd2e7b6042838c326dbb8c970a5b2989aca7",
    "sources/item401_j1_crossM_algebraic_transport_no_go_report.md":
        "ae32a79bd5525bae4ca13501aef3cb030f500062214c72b7af077565df482a9a",
    "scripts/item401_j1_crossM_algebraic_transport_no_go_certificate.py":
        "d4d5d90852a1a96c5322f9bbb40b88d913c503dcbefe61a5edaa385f9cd7ab5b",
    "results/item401_j1_crossM_algebraic_transport_no_go_certificate.json":
        "20733cacbb0698d938376b1b82ff19bdae0bceb4666eebe9bf82f3fa833e1090",
    "manifests/item401_j1_crossM_algebraic_transport_no_go_manifest.json":
        "6daa3e8c868c7ebd09ede3f1fc450fb8e7906058717c99772592a04c272c89be",
    "results/item401_j1_crossM_algebraic_transport_no_go_root_audit.json":
        "19adb137729e87410f93d41c63f8b6127063fa12bf5e08db1f79f229353155f8",
}


INITIALS: dict[int, tuple[int, int]] = {
    1: (-104, 21),
    4: (-7104750016, 761805),
    7: (-49133396574985216, 2147198787),
    2: (13744, 231),
    5: (169877825152, 1380483),
    8: (5832403476713133056, 18259427025),
}


NUMERATOR_FACTORS: dict[int, dict[int, int]] = {
    1: {2: 3, 13: 1},
    4: {2: 6, 7: 1, 13: 1, 1219909: 1},
    7: {2: 10, 13: 1, 73: 1, 1103: 1, 1409: 1, 32533: 1},
    2: {2: 4, 859: 1},
    5: {2: 7, 7: 1, 53: 1, 1033: 1, 3463: 1},
    8: {2: 10, 11: 1, 47: 1, 1314127: 1, 8383391: 1},
}


DENOMINATOR_FACTORS: dict[int, dict[int, int]] = {
    1: {3: 1, 7: 1},
    4: {3: 6, 5: 1, 11: 1, 19: 1},
    7: {3: 11, 17: 1, 23: 1, 31: 1},
    2: {3: 1, 7: 1, 11: 1},
    5: {3: 5, 13: 1, 19: 1, 23: 1},
    8: {3: 11, 5: 2, 7: 1, 19: 1, 31: 1},
}


EXPECTED_PHASE_ROWS = [
    (13, 1, 1, 9, 4),
    (1219909, 4, 203315, 833864, 86967),
    (53, 5, 5, 36, 14),
    (73, 7, 7, 32, 58),
    (32533, 7, 5417, 20350, 11902),
    (47, 8, 2, 30, 41),
    (8383391, 8, 1397226, 6424621, 1596119),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file():
            raise AssertionError(("missing dependency", relative))
        actual = sha256(path)
        if actual != expected:
            raise AssertionError(("dependency mismatch", relative, expected, actual))


def factor_product(factors: dict[int, int]) -> int:
    answer = 1
    for prime, exponent in factors.items():
        answer *= prime ** exponent
    return answer


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def selected_factorials_mod(prime: int, indices: set[int]) -> dict[int, int]:
    """Return n! mod p at selected n<p using O(len(indices)) storage."""
    assert indices and min(indices) >= 0 and max(indices) < prime
    answer = {0: 1} if 0 in indices else {}
    running = 1
    for value in range(1, max(indices) + 1):
        running = running * value % prime
        if value in indices:
            answer[value] = running
    assert set(answer) == indices
    return answer


def kernel_coefficients(
    h_value: int,
    extra: int,
    prime: int,
) -> list[int]:
    answer = []
    for degree in range(2 * h_value + extra + 1):
        value = 0
        for right_degree in range(extra + 1):
            left_degree = degree - right_degree
            if 0 <= left_degree <= 2 * h_value:
                choose = math.comb(2 * h_value, left_degree)
                if left_degree % 2:
                    choose = -choose
                value += math.comb(extra, right_degree) * choose
        answer.append(value % prime)
    return answer


def normalized_sum_mod(
    kernel: list[int],
    a_value: int,
    q_value: int,
    odd: bool,
    prime: int,
) -> int:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    ratio = 1
    answer = 0
    for t_value in range(maximum_t + 1):
        degree = 2 * t_value + 1 if odd else 2 * t_value
        answer = (answer + ratio * kernel[degree]) % prime
        if t_value == maximum_t:
            break
        numerator = a_value + t_value + 1 if odd else a_value + t_value
        denominator = (
            q_value + a_value + t_value + 2
            if odd
            else q_value + a_value + t_value + 1
        )
        assert 0 < denominator < prime
        ratio = -ratio * numerator * pow(denominator, -1, prime) % prime
    return answer


def divided_conditions_mod(prime: int, h_value: int, s_value: int) -> tuple[int, int]:
    assert prime == 4 * h_value + 6 * s_value + 3
    kernel_0 = kernel_coefficients(h_value, 1, prime)
    kernel_1 = kernel_coefficients(h_value, 4, prime)
    x_value = normalized_sum_mod(kernel_0, s_value, 2 * s_value, True, prime)
    y_value = normalized_sum_mod(kernel_0, h_value, 2 * s_value, True, prime)
    u_value = normalized_sum_mod(kernel_1, s_value, 2 * s_value - 1, False, prime)
    v_value = normalized_sum_mod(kernel_1, h_value, 2 * s_value - 1, True, prime)
    needed = {
        2 * s_value,
        s_value,
        3 * s_value + 1,
        h_value,
        2 * s_value + h_value + 1,
        2 * s_value - 1,
        s_value - 1,
        3 * s_value - 1,
        2 * s_value + h_value,
    }
    factorial = selected_factorials_mod(prime, needed)
    sign_s = -1 if s_value % 2 else 1
    sign_h = -1 if h_value % 2 else 1
    a_base = (
        sign_s * factorial[2 * s_value] * factorial[s_value]
        * pow(factorial[3 * s_value + 1], -1, prime)
    ) % prime
    b_base = (
        sign_h * factorial[2 * s_value] * factorial[h_value]
        * pow(factorial[2 * s_value + h_value + 1], -1, prime)
    ) % prime
    c_base = (
        -sign_s * factorial[2 * s_value - 1] * factorial[s_value - 1]
        * pow(factorial[3 * s_value - 1], -1, prime)
    ) % prime
    d_base = (
        sign_h * factorial[2 * s_value - 1] * factorial[h_value]
        * pow(factorial[2 * s_value + h_value], -1, prime)
    ) % prime
    q0 = (2 * a_base * x_value - b_base * y_value) % prime
    q1 = (2 * c_base * u_value - d_base * v_value) % prime
    return q0, q1


def initial_factor_controls() -> tuple[list[dict[str, Any]], list[dict[str, int]]]:
    controls = []
    phase_rows = []
    for h_value in (1, 4, 7, 2, 5, 8):
        numerator, denominator = INITIALS[h_value]
        assert factor_product(NUMERATOR_FACTORS[h_value]) == abs(numerator)
        assert factor_product(DENOMINATOR_FACTORS[h_value]) == denominator
        for prime in NUMERATOR_FACTORS[h_value]:
            assert is_prime(prime)
        for prime in DENOMINATOR_FACTORS[h_value]:
            assert is_prime(prime)
            assert prime <= 4 * h_value + 3
        compatible = []
        for prime in NUMERATOR_FACTORS[h_value]:
            phase_numerator = prime - 4 * h_value - 3
            if (
                prime > 4 * h_value + 3
                and phase_numerator % 6 == 0
                and phase_numerator // 6 >= 1
            ):
                s_value = phase_numerator // 6
                assert math.gcd(denominator, prime) == 1
                q0, q1 = divided_conditions_mod(prime, h_value, s_value)
                assert q0 != 0
                compatible.append(prime)
                phase_rows.append({
                    "p": prime,
                    "h": h_value,
                    "s": s_value,
                    "E_star_mod_p": 0,
                    "Q0_mod_p": q0,
                    "Q1_mod_p": q1,
                    "joint_gate": False,
                })
        controls.append({
            "h": h_value,
            "E_star": {"numerator": numerator, "denominator": denominator},
            "numerator_factorization": {
                str(prime): exponent
                for prime, exponent in NUMERATOR_FACTORS[h_value].items()
            },
            "denominator_factorization": {
                str(prime): exponent
                for prime, exponent in DENOMINATOR_FACTORS[h_value].items()
            },
            "phase_compatible_actual_primes": compatible,
        })
    expected = [
        {"p": p, "h": h, "s": s, "E_star_mod_p": 0,
         "Q0_mod_p": q0, "Q1_mod_p": q1, "joint_gate": False}
        for p, h, s, q0, q1 in EXPECTED_PHASE_ROWS
    ]
    phase_rows.sort(key=lambda row: (row["h"], row["p"]))
    assert phase_rows == expected
    return controls, phase_rows


def candidate_block(prime: int) -> tuple[int, int]:
    return ceil_div(2 * prime + 1, 3), (3 * prime - 3) // 4


def candidates(M: int) -> list[int]:
    lower = ceil_div(4 * M + 3, 3)
    upper = (3 * M - 1) // 2
    return [prime for prime in range(lower, upper + 1) if is_prime(prime)]


def poly_add_mod(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * max(len(left), len(right))
    for index in range(len(output)):
        output[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def poly_mul_mod(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, x_value in enumerate(left):
        for j, y_value in enumerate(right):
            output[i + j] = (output[i + j] + x_value * y_value) % prime
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def poly_eval_mod(coefficients: list[int], value: int, prime: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = (answer * value + coefficient) % prime
    return answer


def interpolate_mod(points: list[tuple[int, int]], prime: int) -> list[int]:
    answer = [0]
    for index, (x_value, y_value) in enumerate(points):
        basis = [1]
        denominator = 1
        for other_index, (other_x, _) in enumerate(points):
            if other_index == index:
                continue
            basis = poly_mul_mod(basis, [(-other_x) % prime, 1], prime)
            denominator = denominator * (x_value - other_x) % prime
        scale = y_value * pow(denominator, -1, prime) % prime
        answer = poly_add_mod(
            answer,
            [(scale * coefficient) % prime for coefficient in basis],
            prime,
        )
    assert all(poly_eval_mod(answer, x, prime) == y % prime for x, y in points)
    return answer


def initial_coordinate(prime: int, t_value: int) -> tuple[int, int, int, int]:
    lower, upper = candidate_block(prime)
    M = lower + t_value
    assert M <= upper
    h_value = 3 * M - 2 * prime
    s_value = (3 * prime - 4 * M - 1) // 2
    assert h_value in INITIALS
    q0, _ = divided_conditions_mod(prime, h_value, s_value)
    numerator, denominator = INITIALS[h_value]
    assert math.gcd(denominator, prime) == 1
    e_value = numerator * pow(denominator, -1, prime) % prime
    return h_value, s_value, q0, e_value


def fourth_difference(values: list[int], prime: int) -> int:
    assert len(values) == 5
    coefficients = [1, -4, 6, -4, 1]
    return sum(c * v for c, v in zip(coefficients, values)) % prime


def interpolation_countermodel_control(M_target: int = 861) -> dict[str, Any]:
    primes = candidates(M_target)
    rows = []
    selector = []
    initial_primes = []
    for prime in primes:
        lower, upper = candidate_block(prime)
        assert lower <= M_target <= upper
        age = M_target - lower
        assert upper - lower + 1 == prime // 12
        initial_values = [initial_coordinate(prime, t) for t in range(3)]
        assert [row[0] for row in initial_values] in ([1, 4, 7], [2, 5, 8])
        q_points = [(t, initial_values[t][2]) for t in range(3)]
        e_points = [(t, initial_values[t][3]) for t in range(3)]
        if age >= 3:
            q_points.append((age, 0))
            e_points.append((age, 0))
            selector.append(prime)
        else:
            initial_primes.append(prime)
            assert not (
                initial_values[age][2] == 0 and initial_values[age][3] == 0
            )
        q_polynomial = interpolate_mod(q_points, prime)
        e_polynomial = interpolate_mod(e_points, prime)
        assert len(q_polynomial) <= 4 and len(e_polynomial) <= 4
        for t in range(upper - lower - 3):
            q_window = [poly_eval_mod(q_polynomial, t + j, prime) for j in range(5)]
            e_window = [poly_eval_mod(e_polynomial, t + j, prime) for j in range(5)]
            assert fourth_difference(q_window, prime) == 0
            assert fourth_difference(e_window, prime) == 0
        q_target = poly_eval_mod(q_polynomial, age, prime)
        e_target = poly_eval_mod(e_polynomial, age, prime)
        assert (q_target == 0 and e_target == 0) == (age >= 3)
        rows.append({
            "p": prime,
            "block_lower": lower,
            "block_upper": upper,
            "target_age": age,
            "initial_h_s_Q0_Estar": [list(value) for value in initial_values],
            "Q0_model_coefficients_ascending_mod_p": q_polynomial,
            "Estar_model_coefficients_ascending_mod_p": e_polynomial,
            "target_Q0_mod_p": q_target,
            "target_Estar_mod_p": e_target,
            "target_joint_gate": age >= 3,
        })
    assert len(initial_primes) <= 2
    assert selector == [prime for prime in primes if prime not in initial_primes]
    # Exactly floor(log(861))=6: e<3 gives e^6<3^6<861, while
    # e>1+1+1/2+1/6=8/3 gives e^7>(8/3)^7>861.
    assert M_target == 861
    assert 3 ** 6 < M_target
    assert Fraction(8, 3) ** 7 > M_target
    D = 6
    clustered = []
    for prime in selector:
        if any(other != prime and abs(other - prime) <= 2 * D for other in selector):
            clustered.append(prime)
    radical = math.prod(clustered)
    return {
        "M_target": M_target,
        "D_floor_natural_log_M": D,
        "candidate_primes": primes,
        "depth_three_initial_primes": initial_primes,
        "model_gate_primes": selector,
        "clustered_model_gate_primes": clustered,
        "cluster_radical": str(radical),
        "columns": rows,
        "common_homogeneous_recurrence":
            "X(t+4)-4X(t+3)+6X(t+2)-4X(t+1)+X(t)=0",
        "matches_all_three_actual_Q0_and_Estar_initial_values": True,
        "actual_Item401_operator_claim": False,
        "actual_orbit_claim": False,
    }


def rational_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def build_certificate() -> dict[str, Any]:
    verify_dependencies()
    initial_controls, phase_rows = initial_factor_controls()
    admission = Fraction(1, 12)
    raw = Fraction(1, 36)
    assert admission == (2 * Fraction(1) - 1) / (12 * Fraction(1))
    return {
        "schema": "item405-j1-initial-orbit-phase-capacity-no-go-certificate-v1",
        "item": 405,
        "checked_date_beijing": "2026-09-01",
        "classification": "EXACT_DEPTH_THREE_INITIAL_GATE_EXCLUSION_AND_SHARP_CAPACITY_NO_GO",
        "dependency_hashes": DEPENDENCIES,
        "exact_Hasse_initial_controls": initial_controls,
        "phase_compatible_Hasse_zero_rows_and_transverse_audit": phase_rows,
        "proved_initial_orbit_statement":
            "the first min(3,floor(p/12)) points of every fixed-p candidate column avoid Q0=Estar=0",
        "fixed_M_depth_three_candidate_count_upper_bound": 2,
        "maximum_raw_log_saving_from_depth_three_exclusion": "2*log(U_M)=o(M)",
        "admission_coefficient_at_c_1": rational_json(admission),
        "retained_raw_ceiling_per_6M": rational_json(raw),
        "interpolation_countermodel_control": interpolation_countermodel_control(),
        "proved_by_report": [
            "the six exact Hasse initials reduce every possible first-three Hasse zero to seven phase-compatible prime rows",
            "the exact transverse coordinate Q0 is nonzero on all seven rows, so every fixed-prime column is joint-gate-free through depth three",
            "at fixed M at most two candidate primes have column age below three",
            "the strongest direct saving is at most 2 log U_M=o(M), hence the retained 1/36 coefficient is unchanged",
            "removing any fixed number of initial column levels from the full candidate selector preserves the Item395-400 cluster lower coefficient (2c-1)/(12c)",
            "at c=1 the depth-three-excluded selector still has cluster radical at least M/12+o(M)",
            "degree-three interpolation matches every exact depth-three initial coordinate and realizes that selector under one common order-four homogeneous recurrence",
            "bounded recurrence existence plus bounded-depth exact initial data therefore cannot be booked as mass",
        ],
        "strict_scope": {
            "unbounded_prime_scan_performed": False,
            "finite_zero_census_performed": False,
            "phase_checks_are_exhaustive_from_exact_factorization": True,
            "countermodel_uses_actual_Item401_operator": False,
            "countermodel_is_actual_orbit": False,
            "cross_prime_reciprocity_proved": False,
            "actual_cluster_upper_bound_proved": False,
            "new_booked_mass": 0,
            "new_capacity_reduction": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    arguments.output.write_text(
        json.dumps(build_certificate(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
