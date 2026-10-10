#!/usr/bin/env python3
"""Replay complete prime-window cancellation for growing corrections.

All computations are deterministic and exact.  The all-parameter theorem,
including the constant-gap endpoint, and the Pascal-block proof are in the
companion source.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import time
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_growing_correction_full_window_cancellation.md"
OUTPUT = ROOT / "results/common_kernel_growing_correction_full_window_certificate.json"
BASE_SCRIPT = ROOT / "scripts/common_kernel_positive_crt_full_correction_certificate.py"
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_positive_crt_full_correction_hashes.sha256":
        "227318fce04df7c79dafb4a570ede3f0767c1c75b084aaaefe746b55a7c1a99a",
    "scripts/common_kernel_positive_crt_full_correction_certificate.py":
        "64fd00d3c07ed7685362ee0df7c3872be7815c03360b9b6e67ae461d41644207",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_base_module():
    spec = importlib.util.spec_from_file_location("fixed_full_correction", BASE_SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


FC = load_base_module()
FW = FC.FW


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


def target_primes(q_value: int, degree_k: int) -> list[int]:
    return [
        prime
        for prime in range(2, 20 * q_value)
        if 3 * prime > 48 * q_value + degree_k + 13
        and FW.is_prime(prime)
    ]


def shifted_padding(q_value: int, e_value: int) -> list[int]:
    a_value = 3 * q_value - e_value
    assert a_value > 0
    return FW.shift(
        FW.multiply(
            FW.power([1, 0, 0, 0, -1], 4 * q_value),
            [1, 0, -1],
        ),
        4 * a_value,
    )


def shifted_v(q_value: int, e_value: int) -> list[int]:
    a_value = 3 * q_value - e_value
    return FW.shift(
        FW.multiply(
            [5 * q_value + 1, 0, 0, 0, -5 * q_value],
            FW.power([1, 0, 0, 0, -1], 4 * q_value),
        ),
        20 * q_value + 4 * a_value,
    )


def determinant_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    size = len(work)
    determinant = 1
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, size):
            factor = work[row][column] * inverse % prime
            if not factor:
                continue
            for inner in range(column, size):
                work[row][inner] = (
                    work[row][inner] - factor * work[column][inner]
                ) % prime
    return determinant % prime


def pascal_determinant_formula(n_value: int, e_value: int, start: int) -> int:
    assert 0 <= start <= n_value
    result = Fraction(1)
    for ell in range(e_value + 1):
        result *= Fraction(
            math.factorial(n_value + ell) * math.factorial(ell),
            math.factorial(n_value + ell - start)
            * math.factorial(start + ell),
        )
    assert result.denominator == 1
    return result.numerator


def pascal_block_check(
    n_value: int, e_value: int, start: int, prime: int
) -> dict[str, object]:
    assert n_value + e_value < prime
    matrix = []
    for row in range(e_value + 1):
        values = []
        for column in range(e_value + 1):
            index = start + row - column
            entry = math.comb(n_value, index) if 0 <= index <= n_value else 0
            if index & 1:
                entry = -entry
            values.append(entry)
        matrix.append(values)
    direct_mod = determinant_mod(matrix, prime)
    formula = pascal_determinant_formula(n_value, e_value, start)
    assert direct_mod
    assert direct_mod in {formula % prime, (-formula) % prime}
    return {
        "n": n_value,
        "e": e_value,
        "start": start,
        "p": prime,
        "direct_determinant_mod_p": direct_mod,
        "absolute_formula_mod_p": formula % prime,
        "formula_bits": formula.bit_length(),
        "nonzero": True,
    }


def channel_exponents(e_value: int) -> list[int]:
    return [
        residue + 4 * offset
        for residue in (1, 2, 3)
        for offset in range(e_value + 1)
    ]


def solve_local_residues(
    q_value: int,
    K: list[int],
    e_value: int,
    V: list[int],
    G: list[int],
    primes: list[int],
) -> tuple[list[int], list[dict[str, object]], int]:
    channels = channel_exponents(e_value)
    H = FW.multiply([1, 1, -2, -2, 1, 1], K)
    H0, H1, H2, H3 = FC.mod_four_components(H)
    VH = FW.multiply(V, H)
    tk = FC.stein(K)
    _, remainder = FW.divide_monic(tk, FW.U)
    alpha = FW.coefficient(remainder, 0)
    rows = []

    for prime in primes:
        odd_index = 2 * prime - 1
        t_zero = (prime - 1) // 2 - 8 * q_value
        t_value = t_zero + e_value
        epsilon = (-1) ** ((prime + 1) // 2)
        assert 2 <= t_zero <= 2 * q_value - 1
        assert 4 * q_value + e_value < prime

        moment = {
            exponent: FW.coefficient(G, odd_index - exponent) % prime
            for exponent in channels
        }
        full = {
            exponent: FW.coefficient(VH, odd_index - exponent) % prime
            for exponent in channels
        }
        local = {exponent: 0 for exponent in channels}
        class_one = [exponent for exponent in channels if exponent % 4 == 1]
        anchors = [exponent for exponent in class_one if moment[exponent]]
        assert anchors
        anchor = anchors[0]

        if any(value % prime for value in H3):
            candidates = [
                exponent
                for exponent in channels
                if exponent % 4 == 2 and full[exponent]
            ]
            assert candidates
            auxiliary = candidates[0]
            local[anchor] = (
                2 * epsilon * pow(moment[anchor], -1, prime)
            ) % prime
            local[auxiliary] = (
                (
                    2 * epsilon * alpha
                    - local[anchor] * full[anchor]
                )
                * pow(full[auxiliary], -1, prime)
            ) % prime
            branch = "H3_class2"
            chosen = [anchor, auxiliary]
        elif any(value % prime for value in H2):
            candidates = [
                exponent
                for exponent in channels
                if exponent % 4 == 3 and full[exponent]
            ]
            assert candidates
            auxiliary = candidates[0]
            local[anchor] = (
                2 * epsilon * pow(moment[anchor], -1, prime)
            ) % prime
            local[auxiliary] = (
                (
                    2 * epsilon * alpha
                    - local[anchor] * full[anchor]
                )
                * pow(full[auxiliary], -1, prime)
            ) % prime
            branch = "H2_class3"
            chosen = [anchor, auxiliary]
        else:
            minors = [
                (
                    exponent,
                    (
                        moment[anchor] * full[exponent]
                        - moment[exponent] * full[anchor]
                    )
                    % prime,
                )
                for exponent in class_one
            ]
            nonzero_minors = [item for item in minors if item[1]]
            if nonzero_minors:
                auxiliary, determinant = nonzero_minors[0]
                b_moment = (2 * epsilon) % prime
                b_full = (2 * epsilon * alpha) % prime
                local[anchor] = (
                    (
                        b_moment * full[auxiliary]
                        - moment[auxiliary] * b_full
                    )
                    * pow(determinant, -1, prime)
                ) % prime
                local[auxiliary] = (
                    (
                        moment[anchor] * b_full
                        - b_moment * full[anchor]
                    )
                    * pow(determinant, -1, prime)
                ) % prime
                branch = "H0_rank2"
                chosen = [anchor, auxiliary]
            else:
                assert alpha % prime == 0
                assert all(full[exponent] == 0 for exponent in channels)
                local[anchor] = (
                    2 * epsilon * pow(moment[anchor], -1, prime)
                ) % prime
                branch = "automatic_structural"
                chosen = [anchor]

        moment_target = sum(
            local[exponent] * moment[exponent] for exponent in channels
        ) % prime
        full_target = sum(
            local[exponent] * full[exponent] for exponent in channels
        ) % prime
        assert moment_target == (2 * epsilon) % prime
        assert full_target == (2 * epsilon * alpha) % prime
        rows.append(
            {
                "p": prime,
                "t0": t_zero,
                "t": t_value,
                "epsilon": epsilon,
                "alpha_mod_p": alpha % prime,
                "branch": branch,
                "chosen_channels": chosen,
                "chosen_local_residues": {
                    str(exponent): local[exponent] for exponent in chosen
                },
                "chosen_moment_responses": {
                    str(exponent): moment[exponent] for exponent in chosen
                },
                "chosen_full_responses": {
                    str(exponent): full[exponent] for exponent in chosen
                },
                "moment_target": moment_target,
                "full_target": full_target,
                "all_local_residues": local,
            }
        )

    product = math.prod(primes)
    coefficients = []
    for exponent in channels:
        value = 0
        modulus = 1
        for prime, row in zip(primes, rows):
            residue = int(row["all_local_residues"][exponent])
            value = FW.crt_pair(value, modulus, residue, prime)
            modulus *= prime
        assert modulus == product
        assert 0 <= value < product
        coefficients.append(value)

    top_index = channels.index(3 + 4 * e_value)
    coefficients[top_index] += product
    assert product <= coefficients[top_index] < 2 * product
    for row in rows:
        del row["all_local_residues"]
    return coefficients, rows, product


def replay_uniform_case(
    name: str,
    q_value: int,
    K: list[int],
    check_rationals: bool = True,
) -> tuple[dict[str, object], dict[str, list[int]]]:
    K = FW.trim(K)
    degree_k = FW.degree(K)
    assert degree_k >= 0
    e_value = (degree_k + 5) // 4 + 1
    a_value = 3 * q_value - e_value
    assert a_value > 0
    primes = target_primes(q_value, degree_k)
    assert primes
    product = math.prod(primes)
    base = FW.sparse_base(q_value)
    base_congruence_quotient = FC.quotient_exact(
        FW.add(base, [-1]), FW.U_SQUARED
    )
    assert FW.add(
        [1], FW.multiply(FW.U_SQUARED, base_congruence_quotient)
    ) == base
    padding = shifted_padding(q_value, e_value)
    V = shifted_v(q_value, e_value)
    G = FW.multiply(V, [1, 0, 0, 0, -1])
    assert G == FW.multiply(FW.multiply(base, FW.U), padding)
    channels = channel_exponents(e_value)
    coefficients, local_rows, reconstructed_product = solve_local_residues(
        q_value, K, e_value, V, G, primes
    )
    assert reconstructed_product == product
    assert sum(value != 0 for value in coefficients) <= 2 * len(primes) + 1
    c_poly = FC.build_c_polynomial(channels, coefficients)

    capacity_left = (
        4
        * sum(coefficients)
        * (a_value ** a_value)
        * ((4 * q_value) ** (4 * q_value))
    )
    capacity_right = (a_value + 4 * q_value) ** (
        a_value + 4 * q_value
    )
    assert capacity_left < capacity_right

    correction_factor = FW.add(
        [1],
        FW.scale(
            FW.multiply(FW.U_SQUARED, FW.multiply(padding, c_poly)),
            -1,
        ),
    )
    h_poly = FW.multiply(base, correction_factor)
    assert FW.order_at_zero(h_poly) == 20 * q_value
    assert FW.degree(h_poly) == 48 * q_value + 13
    quotient_h = FC.quotient_exact(FW.add(h_poly, [-1]), FW.U_SQUARED)
    r_poly = FC.quotient_exact(FW.add(h_poly, [-1]), FW.U)
    tk = FC.stein(K)
    s_poly = FC.quotient_exact(
        FW.add(
            FC.stein(FW.multiply(h_poly, K)),
            FW.scale(tk, -1),
        ),
        FW.U,
    )
    assert FW.degree(s_poly) + 1 == 48 * q_value + degree_k + 13

    residue_rows = []
    for prime in primes:
        i_zero = (
            2 * FW.coefficient(r_poly, prime - 1)
            + FW.coefficient(r_poly, 2 * prime - 1)
        ) % prime
        i_one = FW.coefficient(r_poly, 2 * prime - 2) % prime
        full = (
            2 * FW.coefficient(s_poly, prime - 1)
            + FW.coefficient(s_poly, 2 * prime - 1)
        ) % prime
        assert i_zero == 0 and i_one == 0 and full == 0
        residue_rows.append(
            {"p": prime, "I0": i_zero, "I1": i_one, "full_S": full}
        )

    reduced = None
    if check_rationals:
        i_zero_value = FW.integral(r_poly)
        i_one_value = FW.integral(r_poly, 2)
        j_value = FW.integral(s_poly)
        denominator = math.lcm(
            i_zero_value.denominator,
            i_one_value.denominator,
            j_value.denominator,
        )
        assert math.gcd(denominator, product) == 1
        reduced = {
            "I0_sha256": FW.fraction_digest(i_zero_value),
            "I1_sha256": FW.fraction_digest(i_one_value),
            "J_sha256": FW.fraction_digest(j_value),
            "common_denominator_bits": denominator.bit_length(),
            "gcd_common_denominator_window_product": math.gcd(
                denominator, product
            ),
        }

    branch_counts = {}
    for row in local_rows:
        branch = str(row["branch"])
        branch_counts[branch] = branch_counts.get(branch, 0) + 1

    representative_blocks = [
        pascal_block_check(
            4 * q_value,
            e_value,
            (primes[0] - 1) // 2 - 8 * q_value,
            primes[0],
        ),
        pascal_block_check(
            4 * q_value,
            e_value,
            (primes[-1] - 1) // 2 - 8 * q_value - 1,
            primes[-1],
        ),
    ]

    result = {
        "name": name,
        "parameters": {
            "q": q_value,
            "degree_K": degree_k,
            "E": e_value,
            "A": a_value,
            "channel_count": len(channels),
            "degree_h": FW.degree(h_poly),
            "degree_S": FW.degree(s_poly),
        },
        "K": {
            "coefficient_count": len(K),
            "max_coefficient_bits": max(abs(value).bit_length() for value in K),
            "sha256": FW.polynomial_digest(K),
        },
        "window_primes": primes,
        "window_product": product,
        "window_product_bits": product.bit_length(),
        "branch_counts": branch_counts,
        "local_rows": local_rows,
        "global_coefficients": {
            "nonzero_count": sum(value != 0 for value in coefficients),
            "sum_bits": sum(coefficients).bit_length(),
            "max_bits": max(value.bit_length() for value in coefficients),
            "sha256": FW.polynomial_digest(c_poly),
        },
        "capacity": {
            "left_bits": capacity_left.bit_length(),
            "right_bits": capacity_right.bit_length(),
            "strict": True,
        },
        "pascal_block_checks": representative_blocks,
        "residue_rows": residue_rows,
        "reduced_coordinates": reduced,
        "polynomial_hashes": {
            "h": FW.polynomial_digest(h_poly),
            "q_h": FW.polynomial_digest(quotient_h),
            "r": FW.polynomial_digest(r_poly),
            "S": FW.polynomial_digest(s_poly),
        },
    }
    return result, {
        "K": K,
        "h": h_poly,
        "r": r_poly,
        "S": s_poly,
        "C": c_poly,
    }


def prototype_polynomials() -> list[list[int]]:
    base_structural = FW.multiply([1, -1], FW.power(FW.U, 3))
    return [
        [1, 1],
        [1, -1],
        base_structural,
        FW.shift(base_structural, 1),
    ]


def adaptive_degree_sixty_K(q_value: int = 20, degree_k: int = 60) -> list[int]:
    primes = target_primes(q_value, degree_k)
    prototypes = prototype_polynomials()
    product = math.prod(primes)
    coefficients = []
    for index in range(max(len(poly) for poly in prototypes)):
        value = 0
        modulus = 1
        for prime_index, prime in enumerate(primes):
            target = FW.coefficient(
                prototypes[prime_index % len(prototypes)], index
            )
            value = FW.crt_pair(value, modulus, target % prime, prime)
            modulus *= prime
        assert modulus == product
        coefficients.append(value)
    coefficients.extend([0] * (degree_k + 1 - len(coefficients)))
    coefficients[degree_k] = product
    return FW.trim(coefficients)


def high_ratio_K(degree_k: int = 300) -> list[int]:
    coefficients = [
        ((-1) ** index) * (index + 1) * (index * index + 3)
        for index in range(degree_k + 1)
    ]
    assert coefficients[-1]
    return coefficients


def gaussian_power_one_minus_i(exponent: int) -> tuple[int, int]:
    real, imaginary = 1, 0
    for _ in range(exponent):
        real, imaginary = real + imaginary, imaginary - real
    return real, imaginary


def native_K(exponent: int) -> tuple[list[int], dict[str, int]]:
    real, imaginary = gaussian_power_one_minus_i(exponent)
    m_value = math.factorial(exponent) - real
    assert m_value % 2 == 0
    K = [imaginary - m_value // 2, m_value // 2]
    return K, {"N": exponent, "R_N": real, "I_N": imaginary, "M_N": m_value}


def native_target_zero_output_check(
    q_value: int,
    exponent: int,
    case_polynomials: dict[str, list[int]],
    case_result: dict[str, object],
) -> dict[str, object]:
    K = case_polynomials["K"]
    h_poly = case_polynomials["h"]
    s_poly = case_polynomials["S"]
    primes = list(case_result["window_primes"])
    product = int(case_result["window_product"])
    assert exponent - 1 < (48 * q_value + 14) / 3

    t_power = [
        ((-1) ** index) * math.comb(exponent, index)
        for index in range(exponent + 1)
    ]
    target = math.factorial(exponent)
    base_form = FW.add(t_power, FC.stein(K))
    base_quotient = FC.quotient_exact(
        FW.add(base_form, [-target]), FW.U
    )
    localized_form = FW.add(t_power, FC.stein(FW.multiply(h_poly, K)))
    localized_quotient = FC.quotient_exact(
        FW.add(localized_form, [-target]), FW.U
    )
    assert localized_quotient == FW.add(base_quotient, s_poly)
    assert FW.coefficient(localized_form, 0) == 1
    polynomial_content = math.gcd(*(abs(value) for value in localized_form))
    assert polynomial_content == 1

    base_coordinate = FW.integral(base_quotient)
    localized_coordinate = FW.integral(localized_quotient)
    assert math.gcd(base_coordinate.denominator, product) == 1
    assert math.gcd(localized_coordinate.denominator, product) == 1
    for prime in primes:
        assert prime > exponent - 1

    return {
        "N": exponent,
        "base_coordinate": "integral_0^1 (F_N^*-N!)/(1+x^2) dx",
        "localized_coordinate": (
            "integral_0^1 (F_{N,q}-N!)/(1+x^2) dx"
        ),
        "target_factorial_bits": target.bit_length(),
        "K_max_coefficient_bits": max(abs(value).bit_length() for value in K),
        "base_quotient_degree": FW.degree(base_quotient),
        "base_coordinate_sha256": FW.fraction_digest(base_coordinate),
        "localized_coordinate_sha256": FW.fraction_digest(localized_coordinate),
        "base_denominator_bits": base_coordinate.denominator.bit_length(),
        "localized_denominator_bits": localized_coordinate.denominator.bit_length(),
        "gcd_base_denominator_window_product": math.gcd(
            base_coordinate.denominator, product
        ),
        "gcd_localized_denominator_window_product": math.gcd(
            localized_coordinate.denominator, product
        ),
        "localized_constant_coefficient": FW.coefficient(localized_form, 0),
        "localized_polynomial_content": polynomial_content,
        "localized_form_sha256": FW.polynomial_digest(localized_form),
    }


def main() -> None:
    started = time.perf_counter()
    dependency_checks = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependency_checks[relative] = {"expected": expected, "actual": actual}

    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__))
    assert source_control["clean"] and script_control["clean"]

    adaptive_result, _ = replay_uniform_case(
        "adaptive_all_four_branches_degree_60",
        20,
        adaptive_degree_sixty_K(),
    )
    expected_cycle = [
        "H3_class2",
        "H2_class3",
        "H0_rank2",
        "automatic_structural",
    ]
    actual_cycle = [row["branch"] for row in adaptive_result["local_rows"]]
    assert actual_cycle == [
        expected_cycle[index % 4] for index in range(len(actual_cycle))
    ]

    high_result, _ = replay_uniform_case(
        "high_linear_ratio_degree_300_q30",
        30,
        high_ratio_K(),
    )

    endpoint_result, _ = replay_uniform_case(
        "constant_gap_endpoint_degree_235_q21",
        21,
        high_ratio_K(235),
    )
    assert endpoint_result["parameters"]["A"] == 2
    assert endpoint_result["window_primes"] == [419]

    native_poly, native_parameters = native_K(200)
    native_result, native_polynomials = replay_uniform_case(
        "native_factorial_height_N200_q20",
        20,
        native_poly,
    )
    native_target_zero_output = native_target_zero_output_check(
        20, 200, native_polynomials, native_result
    )

    payload = {
        "schema": "common_kernel_growing_correction_full_window_certificate_v1",
        "logical_scope": (
            "Replay of an unconditional construction canceling every prime "
            "in the complete one-third window for arbitrary coefficient-height "
            "corrections of degree at most 12q-10, which covers every "
            "potentially nonempty window. It does not prove "
            "positivity of the corrected Taylor residual or classify e+pi."
        ),
        "all_parameter_theorem": {
            "K_scope": (
                "arbitrary nonzero K_q in Z[x] with deg K_q <= 12q-10"
            ),
            "coefficient_height_restriction": "none",
            "order_h": "20q",
            "degree_h": "48q+13",
            "degree_S_plus_one": "48q+deg(K_q)+13",
            "window": "(48q+deg(K_q)+13)/3 < p < 20q",
            "window_exceptional_primes": "none",
            "channel_count": "3(floor((deg(K_q)+5)/4)+2)",
            "active_CRT_channel_bound": "2*(number of window primes)+1",
            "natural_linear_threshold": 12,
            "complete_nonvacuous_range": (
                "yes; the window is empty once deg K_q >= 12q-13"
            ),
            "capacity_inputs": (
                "PNT at positive A/q; parity plus Montgomery-Vaughan "
                "Brun-Titchmarsh at A/q tending to zero"
            ),
            "proof_location": "Sections 2--7 of the companion source",
        },
        "adaptive_degree_60_case": adaptive_result,
        "high_ratio_degree_300_case": high_result,
        "constant_gap_endpoint_case": endpoint_result,
        "native_N200_case": native_result,
        "native_parameters": {
            "N": native_parameters["N"],
            "R_N_bits": abs(native_parameters["R_N"]).bit_length(),
            "I_N_bits": abs(native_parameters["I_N"]).bit_length(),
            "M_N_bits": native_parameters["M_N"].bit_length(),
        },
        "native_target_zero_output_check": native_target_zero_output,
        "dependency_checks": dependency_checks,
        "source_sha256": sha256(SOURCE),
        "control_audit": {"source": source_control, "script": script_control},
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "The 40-GiB value is a failure guard only; it neither allocates "
                "nor limits the approximately 50 GiB available Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: all decisive computations are exact integer, "
                "modular, polynomial, determinant, or rational arithmetic."
            ),
        },
        "remaining_scope": (
            "The analytic sign of the localized Taylor residual and a "
            "genuinely shrinking primitive output remain unresolved."
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
