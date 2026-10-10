#!/usr/bin/env python3
"""Replay finite-channel cancellation of a fixed full correction residue.

The all-parameter coefficient-block and PNT arguments are in the companion
source.  This replay uses exact integer and rational arithmetic only.
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
SOURCE = ROOT / "sources/common_kernel_positive_crt_full_correction_cancellation.md"
OUTPUT = ROOT / "results/common_kernel_positive_crt_full_correction_certificate.json"
BASE_SCRIPT = ROOT / "scripts/common_kernel_positive_crt_asymptotic_full_window_certificate.py"
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_positive_crt_asymptotic_full_window_hashes.sha256":
        "0d4277f69ba4fc92e7b0ebc9222cceb9172994f03dadfabfd169ad7b23fff008",
    "scripts/common_kernel_positive_crt_asymptotic_full_window_certificate.py":
        "7f22f68204fbd302bdf73d1e07c32e6f487a814ef4d28f3a7aed986c96fa1e29",
}

Q_VALUE = 10


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_base_module():
    spec = importlib.util.spec_from_file_location("full_window_base", BASE_SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


FW = load_base_module()


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


def derivative(poly: list[int]) -> list[int]:
    if len(poly) <= 1:
        return [0]
    return FW.trim([(index + 1) * poly[index + 1] for index in range(len(poly) - 1)])


def stein(poly: list[int]) -> list[int]:
    deriv = derivative(poly)
    return FW.add(
        deriv,
        FW.scale(FW.shift(deriv, 1), -1),
        FW.scale(FW.shift(poly, 1), -1),
    )


def quotient_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    quotient, remainder = FW.divide_monic(numerator, denominator)
    assert remainder == [0]
    return quotient


def remainder_monic(numerator: list[int], denominator: list[int]) -> list[int]:
    return FW.divide_monic(numerator, denominator)[1]


def polynomial_content(poly: list[int]) -> int:
    values = [abs(value) for value in poly if value]
    assert values
    return math.gcd(*values)


def mod_four_components(poly: list[int]) -> list[list[int]]:
    components = []
    for residue in range(4):
        values = [poly[index] for index in range(residue, len(poly), 4)]
        components.append(FW.trim(values or [0]))
    return components


def is_scalar_one_minus_y(poly: list[int]) -> bool:
    poly = FW.trim(poly)
    if FW.degree(poly) > 1:
        return False
    h0 = FW.coefficient(poly, 0)
    h1 = FW.coefficient(poly, 1)
    return h0 + h1 == 0


def nonproportional_witness(poly: list[int]) -> int:
    candidates = [FW.coefficient(poly, 0) + FW.coefficient(poly, 1)]
    candidates.extend(FW.coefficient(poly, index) for index in range(2, len(poly)))
    for value in candidates:
        if value:
            return abs(value)
    raise AssertionError("polynomial is proportional to 1-y")


def fixed_data(K: list[int]) -> dict[str, object]:
    K = FW.trim(K)
    h_kernel = FW.multiply([1, 1, -2, -2, 1, 1], K)
    H0, H1, H2, H3 = mod_four_components(h_kernel)
    degree_k = max(0, FW.degree(K))

    if H3 != [0] or H2 != [0]:
        if H3 != [0]:
            F = H3
            rho = 2
        else:
            F = H2
            rho = 3
        e_value = FW.degree(F) + 1
        channels = [1] + [rho + 4 * offset for offset in range(e_value + 1)]
        delta = polynomial_content(F)
        s_max = rho + 4 * e_value
        tau = e_value + 1
        case = "A_unused_residue"
        auxiliary_component = 3 if rho == 2 else 2
    elif not is_scalar_one_minus_y(H0):
        F = None
        rho = None
        e_value = max(FW.degree(H0), 1) + 1
        channels = [1 + 4 * offset for offset in range(e_value + 1)]
        delta = nonproportional_witness(H0)
        s_max = 1 + 4 * e_value
        tau = e_value
        case = "B_class_zero_rank_two"
        auxiliary_component = None
    else:
        F = None
        rho = None
        e_value = 0
        channels = [1]
        delta = 1
        s_max = 1
        tau = 2
        case = "C_automatic"
        auxiliary_component = None

    c_star = max(10 + s_max + degree_k, 6 * tau - 3)
    tk = stein(K)
    g0, remainder = FW.divide_monic(tk, FW.U)
    alpha = FW.coefficient(remainder, 0)
    beta = FW.coefficient(remainder, 1)
    assert FW.degree(remainder) <= 1

    if case == "C_automatic":
        assert H0 == [0]
        assert H2 == [0] and H3 == [0]
        assert alpha == 0 and beta == 0

    return {
        "K": K,
        "H": h_kernel,
        "H_components": [H0, H1, H2, H3],
        "case": case,
        "F": F,
        "rho": rho,
        "e": e_value,
        "channels": channels,
        "Delta": delta,
        "s_max": s_max,
        "tau": tau,
        "C_star": c_star,
        "degree_K": degree_k,
        "G0": g0,
        "remainder": remainder,
        "alpha": alpha,
        "beta": beta,
        "auxiliary_component": auxiliary_component,
    }


def V_polynomial(q_value: int) -> list[int]:
    return FW.shift(
        FW.multiply(
            [5 * q_value + 1, 0, 0, 0, -5 * q_value],
            FW.power([1, 0, 0, 0, -1], 4 * q_value),
        ),
        32 * q_value,
    )


def target_primes(q_value: int, data: dict[str, object]) -> list[int]:
    c_star = int(data["C_star"])
    delta = int(data["Delta"])
    k_one = 40 * q_value * q_value + 44 * q_value + 5
    return [
        prime
        for prime in range(2, 20 * q_value)
        if 3 * prime > 48 * q_value + c_star
        and FW.is_prime(prime)
        and (delta * k_one) % prime != 0
    ]


def solve_local_systems(
    q_value: int,
    data: dict[str, object],
    V: list[int],
    G: list[int],
) -> tuple[list[int], list[dict[str, object]], int]:
    channels = list(data["channels"])
    H = list(data["H"])
    VH = FW.multiply(V, H)
    alpha = int(data["alpha"])
    primes = target_primes(q_value, data)
    assert primes
    local_rows: list[dict[str, object]] = []

    for prime in primes:
        even_index = 2 * prime - 2
        odd_index = even_index + 1
        t_value = (prime - 1) // 2 - 8 * q_value
        epsilon = (-1) ** ((prime + 1) // 2)
        assert t_value >= int(data["tau"])
        moment_responses = {
            exponent: FW.coefficient(G, odd_index - exponent) % prime
            for exponent in channels
        }
        full_responses = {
            exponent: FW.coefficient(VH, odd_index - exponent) % prime
            for exponent in channels
        }
        local = {exponent: 0 for exponent in channels}

        if data["case"] == "A_unused_residue":
            assert moment_responses[1]
            local[1] = (
                2 * epsilon * pow(moment_responses[1], -1, prime)
            ) % prime
            auxiliary = [exponent for exponent in channels if exponent != 1]
            nonzero = [exponent for exponent in auxiliary if full_responses[exponent]]
            assert nonzero
            chosen = nonzero[0]
            residual_target = (
                2 * epsilon * alpha - local[1] * full_responses[1]
            ) % prime
            local[chosen] = (
                residual_target * pow(full_responses[chosen], -1, prime)
            ) % prime
            chosen_channels = [1, chosen]
        elif data["case"] == "B_class_zero_rank_two":
            first = channels[0]
            assert first == 1 and moment_responses[first]
            chosen = None
            chosen_det = 0
            for exponent in channels[1:]:
                determinant = (
                    moment_responses[first] * full_responses[exponent]
                    - moment_responses[exponent] * full_responses[first]
                ) % prime
                if determinant:
                    chosen = exponent
                    chosen_det = determinant
                    break
            assert chosen is not None and chosen_det
            b_moment = (2 * epsilon) % prime
            b_full = (2 * epsilon * alpha) % prime
            local[first] = (
                (
                    b_moment * full_responses[chosen]
                    - moment_responses[chosen] * b_full
                )
                * pow(chosen_det, -1, prime)
            ) % prime
            local[chosen] = (
                (
                    moment_responses[first] * b_full
                    - b_moment * full_responses[first]
                )
                * pow(chosen_det, -1, prime)
            ) % prime
            chosen_channels = [first, chosen]
        else:
            assert data["case"] == "C_automatic"
            assert moment_responses[1]
            assert full_responses[1] == 0 and alpha == 0
            local[1] = (
                2 * epsilon * pow(moment_responses[1], -1, prime)
            ) % prime
            chosen_channels = [1]

        moment_check = sum(
            local[exponent] * moment_responses[exponent]
            for exponent in channels
        ) % prime
        full_check = sum(
            local[exponent] * full_responses[exponent]
            for exponent in channels
        ) % prime
        assert moment_check == (2 * epsilon) % prime
        assert full_check == (2 * epsilon * alpha) % prime

        local_rows.append(
            {
                "p": prime,
                "p_mod_4": prime % 4,
                "t": t_value,
                "epsilon": epsilon,
                "chosen_channels": chosen_channels,
                "local_residues": {str(key): value for key, value in local.items()},
                "moment_responses": {
                    str(key): value for key, value in moment_responses.items()
                },
                "full_responses": {
                    str(key): value for key, value in full_responses.items()
                },
                "moment_target": moment_check,
                "full_target": full_check,
            }
        )

    product = math.prod(primes)
    global_coefficients = []
    for exponent in channels:
        value = 0
        modulus = 1
        for prime, row in zip(primes, local_rows):
            residue = int(row["local_residues"][str(exponent)])
            value = FW.crt_pair(value, modulus, residue, prime)
            modulus *= prime
        assert modulus == product
        assert 0 <= value < product
        global_coefficients.append(value)

    assert any(global_coefficients)
    return global_coefficients, local_rows, product


def build_c_polynomial(channels: list[int], coefficients: list[int]) -> list[int]:
    size = max(channels) + 1
    output = [0] * size
    for exponent, value in zip(channels, coefficients):
        output[exponent] = value
    return FW.trim(output)


def block_checks(
    q_value: int,
    data: dict[str, object],
    primes: list[int],
) -> list[dict[str, object]]:
    rows = []
    if data["case"] == "A_unused_residue":
        F = list(data["F"])
        e_value = int(data["e"])
        for prime in primes:
            t_value = (prime - 1) // 2 - 8 * q_value
            values = []
            # Compute in y directly for the exact block used in Section 5.
            v_y = FW.multiply(
                [5 * q_value + 1, -5 * q_value],
                FW.power([1, -1], 4 * q_value),
            )
            filtered = FW.multiply(v_y, F)
            for offset in range(e_value + 1):
                values.append(FW.coefficient(filtered, t_value - 1 - offset) % prime)
            assert any(values)
            rows.append({"p": prime, "block": values})
    elif data["case"] == "B_class_zero_rank_two":
        H0 = list(data["H_components"])[0]
        e_value = int(data["e"])
        v_y = FW.multiply(
            [5 * q_value + 1, -5 * q_value],
            FW.power([1, -1], 4 * q_value),
        )
        moment_y = FW.multiply(v_y, [1, -1])
        full_y = FW.multiply(v_y, H0)
        for prime in primes:
            t_value = (prime - 1) // 2 - 8 * q_value
            columns = [
                (
                    FW.coefficient(moment_y, t_value - offset) % prime,
                    FW.coefficient(full_y, t_value - offset) % prime,
                )
                for offset in range(e_value + 1)
            ]
            determinants = [
                (columns[0][0] * column[1] - column[0] * columns[0][1])
                % prime
                for column in columns[1:]
            ]
            assert any(determinants)
            rows.append(
                {
                    "p": prime,
                    "columns": columns,
                    "minors_with_column_zero": determinants,
                }
            )
    return rows


def replay_case(name: str, K: list[int]) -> dict[str, object]:
    q_value = Q_VALUE
    data = fixed_data(K)
    base = FW.sparse_base(q_value)
    padding = FW.shifted_padding(q_value)
    V = V_polynomial(q_value)
    G = FW.multiply(V, [1, 0, 0, 0, -1])
    assert G == FW.multiply(FW.multiply(base, FW.U), padding)
    coefficients, local_rows, product = solve_local_systems(
        q_value, data, V, G
    )
    primes = [int(row["p"]) for row in local_rows]
    channels = list(data["channels"])
    c_poly = build_c_polynomial(channels, coefficients)
    correction_factor = FW.add(
        [1],
        FW.scale(
            FW.multiply(FW.U_SQUARED, FW.multiply(padding, c_poly)),
            -1,
        ),
    )
    h_poly = FW.multiply(base, correction_factor)
    quotient_h = quotient_exact(FW.add(h_poly, [-1]), FW.U_SQUARED)
    r_poly = quotient_exact(FW.add(h_poly, [-1]), FW.U)

    K_poly = list(data["K"])
    s_numerator = FW.add(
        stein(FW.multiply(h_poly, K_poly)),
        FW.scale(stein(K_poly), -1),
    )
    s_poly = quotient_exact(s_numerator, FW.U)
    base_s = quotient_exact(
        FW.add(
            stein(FW.multiply(base, K_poly)),
            FW.scale(stein(K_poly), -1),
        ),
        FW.U,
    )
    delta_s = FW.add(s_poly, FW.scale(base_s, -1))

    q_variation = FW.scale(
        FW.multiply(FW.multiply(base, padding), c_poly), -1
    )
    exact_delta = quotient_exact(
        stein(FW.multiply(FW.multiply(FW.U_SQUARED, q_variation), K_poly)),
        FW.U,
    )
    assert delta_s == exact_delta

    order_at_zero = FW.order_at_zero(h_poly)
    assert order_at_zero == 20 * q_value
    assert FW.degree(h_poly) <= 48 * q_value + 10 + int(data["s_max"])
    assert quotient_h

    coefficient_sum = sum(coefficients)
    capacity_left = (
        4
        * coefficient_sum
        * 3 ** (3 * q_value)
        * 4 ** (4 * q_value)
    )
    capacity_right = 7 ** (7 * q_value)
    assert capacity_left < capacity_right

    residue_rows = []
    alpha = int(data["alpha"])
    h_minus_one = FW.add(h_poly, [-1])
    h_prime_over_u = quotient_exact(derivative(h_poly), FW.U)
    for prime in primes:
        even_index = 2 * prime - 2
        odd_index = even_index + 1
        epsilon = (-1) ** ((prime + 1) // 2)
        i_zero_residue = (
            2 * FW.coefficient(r_poly, prime - 1)
            + FW.coefficient(r_poly, odd_index)
        ) % prime
        i_one_residue = FW.coefficient(r_poly, even_index) % prime
        s_low = FW.coefficient(s_poly, prime - 1) % prime
        s_high = FW.coefficient(s_poly, odd_index) % prime
        full_residue = (2 * s_low + s_high) % prime
        assert i_zero_residue == 0
        assert i_one_residue == 0
        assert s_low == (epsilon * alpha) % prime
        assert full_residue == 0
        residue_rows.append(
            {
                "p": prime,
                "I0_residue": i_zero_residue,
                "I1_residue": i_one_residue,
                "S_low_mod_p": s_low,
                "S_high_mod_p": s_high,
                "full_residue": full_residue,
            }
        )

    i_zero = FW.integral(r_poly)
    i_one = FW.integral(r_poly, 2)
    j_value = FW.integral(s_poly)
    common_denominator = math.lcm(
        i_zero.denominator, i_one.denominator, j_value.denominator
    )
    assert math.gcd(common_denominator, product) == 1

    even_term_rows = []
    if name == "exceptional_linear_non_even":
        g0 = list(data["G0"])
        remainder = list(data["remainder"])
        assert any(
            FW.coefficient(h_poly, index)
            for index in range(1, len(h_poly), 2)
        )
        k_zero = FW.coefficient(K_poly, 0)
        k_one = FW.coefficient(K_poly, 1)
        assert k_zero + k_one == 0
        for prime in primes:
            odd_index = 2 * prime - 1
            term_hg = FW.coefficient(FW.multiply(h_minus_one, g0), odd_index)
            term_r = FW.coefficient(FW.multiply(r_poly, remainder), odd_index)
            derivative_term = FW.coefficient(
                FW.multiply(
                    FW.multiply([1, -1], h_prime_over_u),
                    K_poly,
                ),
                odd_index,
            )
            exact = FW.coefficient(s_poly, odd_index)
            assert exact == term_hg + term_r + derivative_term
            even_only_expression = (k_zero + k_one) * (
                FW.coefficient(quotient_h, 2 * prime - 2)
                - FW.coefficient(quotient_h, 2 * prime - 4)
            )
            assert even_only_expression == 0
            even_term_rows.append(
                {
                    "p": prime,
                    "h_minus_one_G0_mod_p": term_hg % prime,
                    "remainder_term_mod_p": term_r % prime,
                    "derivative_term_mod_p": derivative_term % prime,
                    "sum_mod_p": exact % prime,
                    "even_only_formula_rhs_mod_p": (
                        even_only_expression % prime
                    ),
                    "h_is_even": False,
                    "standing_even_formula_not_applicable": True,
                }
            )

    return {
        "name": name,
        "fixed_data": {
            "K": K_poly,
            "case": data["case"],
            "H_components": data["H_components"],
            "alpha": data["alpha"],
            "beta": data["beta"],
            "Delta": data["Delta"],
            "e": data["e"],
            "tau": data["tau"],
            "s_max": data["s_max"],
            "C_star": data["C_star"],
            "channels": channels,
        },
        "target_primes": primes,
        "target_product": product,
        "global_coefficients": {
            str(exponent): value
            for exponent, value in zip(channels, coefficients)
        },
        "coefficient_sum": coefficient_sum,
        "local_system_rows": local_rows,
        "block_checks": block_checks(q_value, data, primes),
        "exact_capacity": {
            "left": capacity_left,
            "right": capacity_right,
            "holds": True,
        },
        "degrees": {
            "ord0_h": order_at_zero,
            "deg_h": FW.degree(h_poly),
            "deg_r": FW.degree(r_poly),
            "deg_S": FW.degree(s_poly),
        },
        "residue_rows": residue_rows,
        "even_non_even_reconciliation": even_term_rows,
        "reduced_coordinates": {
            "I0_sha256": FW.fraction_digest(i_zero),
            "I1_sha256": FW.fraction_digest(i_one),
            "J_sha256": FW.fraction_digest(j_value),
            "I0_denominator_bits": i_zero.denominator.bit_length(),
            "I1_denominator_bits": i_one.denominator.bit_length(),
            "J_denominator_bits": j_value.denominator.bit_length(),
            "common_denominator_bits": common_denominator.bit_length(),
            "gcd_common_denominator_target_product": math.gcd(
                common_denominator, product
            ),
        },
        "polynomial_hashes": {
            "C": FW.polynomial_digest(c_poly),
            "h": FW.polynomial_digest(h_poly),
            "r": FW.polynomial_digest(r_poly),
            "S": FW.polynomial_digest(s_poly),
            "delta_S": FW.polynomial_digest(delta_s),
        },
    }


def linear_closed_checks() -> dict[str, object]:
    q_value = Q_VALUE
    primes = FW.primes_in_window(q_value)
    k_one = 40 * q_value * q_value + 44 * q_value + 5
    k_two = 40 * q_value * q_value + 34 * q_value + 5
    k_three = (
        1760 * q_value**3
        + 1976 * q_value**2
        + 644 * q_value
        + 63
    )
    rows = []
    for prime in primes:
        t_value = (prime - 1) // 2 - 8 * q_value
        v_y = FW.multiply(
            [5 * q_value + 1, -5 * q_value],
            FW.power([1, -1], 4 * q_value),
        )
        v_previous = FW.coefficient(v_y, t_value - 1)
        v_previous_two = FW.coefficient(v_y, t_value - 2)
        assert (v_previous % prime == 0) == (k_two % prime == 0)
        numerator = (
            240 * q_value**3
            - 80 * q_value**2 * t_value
            + 308 * q_value**2
            - 48 * q_value * t_value
            + 114 * q_value
            + 4 * t_value**2
            - 19 * t_value
            + 21
        )
        assert (4 * numerator - 2 * k_three) % prime == 0
        assert (
            (3 * v_previous + v_previous_two) % prime == 0
        ) == (k_three % prime == 0)
        rows.append(
            {
                "p": prime,
                "t": t_value,
                "K1_mod_p": k_one % prime,
                "K2_mod_p": k_two % prime,
                "K3_mod_p": k_three % prime,
                "v_tminus1_mod_p": v_previous % prime,
                "3v_tminus1_plus_v_tminus2_mod_p": (
                    3 * v_previous + v_previous_two
                ) % prime,
            }
        )
    return {
        "q": q_value,
        "K1": k_one,
        "K2": k_two,
        "K3": k_three,
        "rows": rows,
    }


def structural_symbolic_checks() -> dict[str, object]:
    one_minus_x = [1, -1]
    u_cubed = FW.power(FW.U, 3)
    class_zero_K = FW.multiply(one_minus_x, u_cubed)
    automatic_K = FW.shift(class_zero_K, 1)
    class_zero_data = fixed_data(class_zero_K)
    automatic_data = fixed_data(automatic_K)
    assert class_zero_data["case"] == "B_class_zero_rank_two"
    assert automatic_data["case"] == "C_automatic"
    assert automatic_data["alpha"] == 0 and automatic_data["beta"] == 0
    return {
        "class_zero_nonproportional_K": class_zero_K,
        "class_zero_H_components": class_zero_data["H_components"],
        "automatic_K": automatic_K,
        "automatic_H_components": automatic_data["H_components"],
        "automatic_remainder": automatic_data["remainder"],
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

    cases = [
        replay_case("generic_linear", [1, 1]),
        replay_case("exceptional_linear_non_even", [1, -1]),
        replay_case(
            "class_zero_nonproportional",
            FW.multiply([1, -1], FW.power(FW.U, 3)),
        ),
        replay_case(
            "automatic_structural",
            FW.shift(FW.multiply([1, -1], FW.power(FW.U, 3)), 1),
        ),
    ]

    payload = {
        "schema": "common_kernel_positive_crt_full_correction_certificate_v1",
        "logical_scope": (
            "Replay of an unconditional finite-channel construction which, "
            "for every fixed K, cancels asymptotically the full one-third "
            "prime-window mass from I0, I1, and integral S_h. It does not "
            "treat K growing with q, primitive full-form content, or classify "
            "e+pi."
        ),
        "all_parameter_theorem": {
            "q_range": "all sufficiently large positive integers q",
            "K_scope": "each fixed K in Z[x]",
            "order_h": "20q",
            "degree_h": "48q+O_K(1)",
            "prime_window_mass": "4q+o(q)",
            "possible_surviving_mass": "O_K(log q)",
            "full_response": (
                "delta s_(2p-1)=-[x^(2p-1)] "
                "V_q(1+x)(1-x^2)^2 K C mod p"
            ),
            "finite_rank_source": "coefficient-block lemma in source Section 4",
            "proof_location": "Sections 2--7 of the companion source",
        },
        "representative_q10_cases": cases,
        "linear_closed_checks": linear_closed_checks(),
        "structural_symbolic_checks": structural_symbolic_checks(),
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
                "Not used: exact polynomial, integer, modular, and rational "
                "arithmetic is CPU-bound at this scale."
            ),
        },
        "remaining_scope": (
            "A growing correction K, a coupled varying primitive-content "
            "argument, or a different analytic sign constraint may carry "
            "information absent from these three rational residues."
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
