#!/usr/bin/env python3
"""Exact deterministic replay for Item 350.

This replay checks declared triangular-coordinate, symbolic penultimate
resonance, lower-slice carrier, CRT, exact-target-lift, and nonzero-row
controls.  It performs no prime census, target search, or half-bound scan.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item333_beta_nonlinear_state_saturation_no_go_report.md": (
        "8f4bc0a6f93cbd4882392ade311d68e25be1ceb282db71cc5e1ef2f70aee75d6"
    ),
    "results/item333_beta_nonlinear_state_saturation_no_go_root_audit.json": (
        "6ddd4949f5d7f91fdc160634da06079661ebf373ac0f061495a7b41135924ecc"
    ),
    "sources/item340_beta_full_complement_loop_correlation_report.md": (
        "4f3ddc5e09544e7c4d8077413b968f5b8a61694b8872dfdccf89d18dc03018b6"
    ),
    "results/item340_beta_full_complement_loop_correlation_certificate.json": (
        "4be0540e6835c3621482ab42bf5218420d76d7091a827386b1f6978146f6bfd0"
    ),
    "results/item340_beta_full_complement_loop_correlation_root_audit.json": (
        "1b0a53ab7a2c99a5be681a233c1a4c55ff8e6addb702ff287996cab3eb3e1900"
    ),
    "manifests/item340_beta_full_complement_loop_correlation_manifest.json": (
        "3197f620428af855b016842f156f69894f704de2d71846a675860d1a6b679366"
    ),
    "sources/item343_beta_quotient_radical_excess_capacity_report.md": (
        "0fb48e3bbf30d05bcf40d2e4dc9b04e2e80893e6c4fee925d9c6b99b25126c66"
    ),
    "results/item343_beta_quotient_radical_excess_capacity_certificate.json": (
        "c700ffaa6898bd50e4d6b790dea307ec883ecab6374e07a7c62622eb5ba7d57b"
    ),
    "results/item343_beta_quotient_radical_excess_capacity_root_audit.json": (
        "1788b3f5247b132c8ea8f8133d64d9fadcd716013b041964be46b7c71c9747e4"
    ),
    "manifests/item343_beta_quotient_radical_excess_capacity_manifest.json": (
        "eddaff62ba519ece9bac2c881b04b0a0ec3f5dc5d06d780ac03a4b0b7dc69439"
    ),
    "sources/item346_beta_t_avoiding_radical_localization_report.md": (
        "2ad742c14d0adbc74da6c46394ed89f68cec8888a3c9d22ee4f230a4e16548a5"
    ),
    "results/item346_beta_t_avoiding_radical_localization_certificate.json": (
        "29a20d6ede62db23658d66db8e57af4a2982c9b66fd12d104f0070b3280aefab"
    ),
    "results/item346_beta_t_avoiding_radical_localization_root_audit.json": (
        "c9273d7e187ee2c9b4b91bffc65769f1a29f937613c36960e4ed5871c5782089"
    ),
    "manifests/item346_beta_t_avoiding_radical_localization_manifest.json": (
        "5029cf3483fdf6cce4bbc0d454bca362bb2796104ca36b353d0161e374915530"
    ),
}


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    archive_root = Path(__file__).resolve().parent.parent
    rows: list[dict[str, Any]] = []
    for relative_path, expected_hash in DEPENDENCY_HASHES.items():
        path = archive_root / relative_path
        payload = path.read_bytes()
        actual_hash = hashlib.sha256(payload).hexdigest()
        assert actual_hash == expected_hash, (
            relative_path,
            actual_hash,
            expected_hash,
        )
        rows.append(
            {
                "path": relative_path,
                "bytes": len(payload),
                "sha256": actual_hash,
            }
        )
    return {"count": len(rows), "rows": rows, "digest": digest(rows)}


def beta_q(limit: int) -> list[int]:
    values = [1, 1]
    for index in range(2, limit + 1):
        values.append((4 * index - 2) * values[-1] + values[-2])
    return values


def weight_data(n: int) -> tuple[int, int, list[int]]:
    m = n - 2
    A = 4 * n - 2
    weights = [0] * (m + 2)
    weights[1] = 7
    for index in range(2, m + 1):
        weights[index] = 4 * index + 2
    weights[m + 1] = A
    return A, m, weights


def e_coefficient_sequence(n: int) -> list[list[int]]:
    _, m, weights = weight_data(n)
    zero = [0] * m
    E_previous = zero[:]
    E_current = zero[:]
    E_current[0] = 1
    vectors = [E_previous, E_current]
    for index in range(1, m + 1):
        following = [
            weights[index + 1] * E_current[column] + E_previous[column]
            for column in range(m)
        ]
        if index + 1 <= m:
            following[index] += (-1) ** index
        vectors.append(following)
        E_previous, E_current = E_current, following
    return vectors


def e_coefficient_vectors(n: int) -> tuple[list[int], list[int]]:
    _, m, _ = weight_data(n)
    vectors = e_coefficient_sequence(n)
    return vectors[m], vectors[m + 1]


def dot(left: list[int], right: list[int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    x = old_s if a >= 0 else -old_s
    y = old_t if b >= 0 else -old_t
    assert a * x + b * y == old_r
    return old_r, x, y


def modular_inverse(value: int, modulus: int) -> int:
    gcd_value, coefficient, _ = extended_gcd(value, modulus)
    assert gcd_value == 1
    return coefficient % modulus


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


def load_values(digits: list[int], weights: list[int], epsilon: int) -> list[int]:
    m = len(digits)
    values = [0] * (m + 1)
    for index in range(3, m + 1):
        values[index] = epsilon * (
            digits[index - 1] - weights[index] * digits[index - 2]
        )
    return values


def transition_control(n: int) -> dict[str, Any]:
    A, m, weights = weight_data(n)
    digits = [((-1) ** index) * (index + 3) for index in range(m)]
    x_values = [0] * (m + 1)
    for index in range(3, m + 1):
        x_values[index] = (
            weights[index] * digits[index - 2] - digits[index - 1]
        )
    reconstructed = digits[:2]
    for index in range(3, m + 1):
        reconstructed.append(
            weights[index] * reconstructed[index - 2] - x_values[index]
        )
    assert reconstructed == digits

    windows: list[dict[str, Any]] = []
    declared_windows = [(2, m), (2, min(m, 5)), (max(2, m - 4), m)]
    for lower, upper in declared_windows:
        coefficient = math.prod(weights[index] for index in range(lower + 1, upper + 1))
        right = coefficient * digits[lower - 1]
        terms: list[dict[str, Any]] = []
        for index in range(lower + 1, upper + 1):
            tail = math.prod(weights[r] for r in range(index + 1, upper + 1))
            right -= x_values[index] * tail
            terms.append({"j": index, "x": x_values[index], "tail": tail})
        assert right == digits[upper - 1]
        windows.append(
            {
                "u": lower,
                "v": upper,
                "weight_product": str(coefficient),
                "endpoint": digits[upper - 1],
                "terms": terms,
                "terms_digest": digest(terms),
            }
        )
    return {
        "n": n,
        "A": A,
        "m": m,
        "digits": digits,
        "x_values": x_values[3:],
        "inverse_reconstruction": True,
        "unimodular_determinant": (-1) ** (m - 2),
        "windows": windows,
        "windows_digest": digest(windows),
        "formal_noncanonical_control": True,
        "finite_only": True,
    }


def transition_controls() -> dict[str, Any]:
    declared_n_values = [5, 13, 25]
    rows = [transition_control(n) for n in declared_n_values]
    return {
        "declared_n_values": declared_n_values,
        "row_count": len(rows),
        "rows": rows,
        "rows_digest": digest(rows),
        "finite_rows_promoted": False,
    }


def resonance_control(n: int) -> dict[str, Any]:
    A, m, weights = weight_data(n)
    assert m >= 4
    q_values = beta_q(n)
    a, b, c = q_values[n - 1], q_values[n], q_values[n - 2]
    previous_weight = weights[m - 1]
    top_weight = weights[m]
    D = previous_weight * top_weight + 1
    matrix = [
        [D, -top_weight, 1],
        [-(A * D + previous_weight), A * top_weight + 1, -A],
        [-previous_weight, 1, 0],
    ]
    determinant = (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    assert determinant == 0
    assert matrix[1] == [
        -A * matrix[0][column] + matrix[2][column]
        for column in range(3)
    ]

    vectors = e_coefficient_sequence(n)
    E_previous = vectors[m - 1]
    E_m = vectors[m]
    E_next = vectors[m + 1]
    symbolic_rows: list[dict[str, Any]] = []
    for sigma in (-1, 1):
        epsilon = sigma * ((-1) ** m)
        z_gradient = [0] * m
        z_gradient[m - 3] = -epsilon * previous_weight
        z_gradient[m - 2] = epsilon
        left_gradient = [
            sigma * E_next[index]
            - A * sigma * E_m[index]
            - z_gradient[index]
            for index in range(m)
        ]
        expected_gradient = [
            sigma * E_previous[index] if index < m - 3 else 0
            for index in range(m)
        ]
        assert left_gradient == expected_gradient
        symbolic_rows.append(
            {
                "sigma": sigma,
                "epsilon": epsilon,
                "left_gradient_digest": digest(left_gradient),
                "expected_gradient_digest": digest(expected_gradient),
                "affine_constant": str(A * c - a),
                "identity_verified": True,
            }
        )

    rho_coefficients = E_previous[: m - 3]
    rho_content = math.gcd(*(abs(value) for value in rho_coefficients))
    if m >= 5:
        assert rho_content == 1
        primitive_reason = "last two lower continuants have gcd one"
    else:
        assert n == 6 and rho_coefficients == [141]
        assert math.gcd(rho_content, b) == 1
        primitive_reason = "m=4 edge: gcd(141,q_6)=1"

    lower_slice_carrier = math.gcd(b, A * A + 1)
    return {
        "n": n,
        "A": A,
        "m": m,
        "matrix": matrix,
        "determinant": determinant,
        "row_relation": "row_Delta=-A*row_t+row_z",
        "symbolic_affine_identity": (
            "Delta+A*t-z_(m-1)=A*c-a+rho_lower"
        ),
        "symbolic_rows": symbolic_rows,
        "symbolic_rows_digest": digest(symbolic_rows),
        "rho_coefficient_count": len(rho_coefficients),
        "rho_coefficients_digest": digest(rho_coefficients),
        "rho_content": rho_content,
        "rho_is_mod_p_surjective_for_every_p_gt_A_dividing_b": True,
        "primitive_reason": primitive_reason,
        "lower_zero_slice_carrier": str(lower_slice_carrier),
        "lower_zero_slice_carrier_bound": str(A * A + 1),
        "lower_zero_slice_carrier_zero_rate": True,
        "actual_family_exclusion_claim": False,
        "finite_only": True,
    }


def resonance_controls() -> dict[str, Any]:
    declared_n_values = [5, 6, 13, 30]
    applicable_n_values = [n for n in declared_n_values if n - 2 >= 4]
    rows = [resonance_control(n) for n in applicable_n_values]
    return {
        "declared_n_values": declared_n_values,
        "applicable_n_values": applicable_n_values,
        "n_5_penultimate_depth_outside_active_range": True,
        "row_count": len(rows),
        "rows": rows,
        "rows_digest": digest(rows),
        "symbolic_identity_not_inferred_from_rows": True,
    }


def reconstruct_target_coordinates(
    n: int,
    sigma: int,
    lower_values: list[int],
    z_top: int,
    modulus: int,
) -> list[int]:
    q_values = beta_q(n)
    a = q_values[n - 1]
    A, m, weights = weight_data(n)
    _, E_next = e_coefficient_vectors(n)
    epsilon = sigma * ((-1) ** m)
    lower_target_coefficients = [sigma * E_next[index] for index in range(m - 2)]
    lower_value = sum(
        coefficient * value
        for coefficient, value in zip(lower_target_coefficients, lower_values)
    )
    u = epsilon * (A * weights[m] + 1)
    v = -epsilon * A
    alpha = epsilon
    beta = epsilon * weights[m]
    d_previous = alpha * (-lower_value + a) - v * z_top
    d_top = beta * (-lower_value + a) + u * z_top
    return [value % modulus for value in lower_values + [d_previous, d_top]]


def per_prime_solution(n: int, sigma: int, depth: int, prime: int) -> list[int]:
    q_values = beta_q(n)
    a, b, c = q_values[n - 1], q_values[n], q_values[n - 2]
    A, m, weights = weight_data(n)
    E_m, E_next = e_coefficient_vectors(n)
    epsilon = sigma * ((-1) ** m)
    assert prime > A and b % prime == 0 and is_prime(prime)

    if depth <= m - 2:
        lower = [0] * (m - 2)
        z_top = (1 - c) % prime
        digits = reconstruct_target_coordinates(n, sigma, lower, z_top, prime)
    elif depth == m:
        lower = [0] * (m - 2)
        lower_kappa_coefficients = [sigma * E_m[index] for index in range(m - 2)]
        if c % prime == 0:
            selected = next(
                index
                for index, coefficient in enumerate(lower_kappa_coefficients)
                if coefficient % prime
            )
            lower[selected] = (-modular_inverse(lower_kappa_coefficients[selected], prime)) % prime
        digits = reconstruct_target_coordinates(n, sigma, lower, 0, prime)
    else:
        assert depth == m - 1 and m >= 4
        vectors = e_coefficient_sequence(n)
        rho_coefficients = [
            sigma * value for value in vectors[m - 1][: m - 3]
        ]
        selected = next(
            index
            for index, coefficient in enumerate(rho_coefficients)
            if coefficient % prime
        )
        lower = [0] * (m - 2)
        desired_rho = (A - (A * c - a)) % prime
        lower[selected] = (
            desired_rho * modular_inverse(rho_coefficients[selected], prime)
        ) % prime
        lower_target_coefficients = [
            sigma * E_next[index] for index in range(m - 2)
        ]
        lower_value = dot(lower_target_coefficients, lower) % prime
        z_top = (
            lower_value
            - a
            + epsilon * weights[m - 1] * lower[m - 3]
        ) * modular_inverse(A, prime) % prime
        digits = reconstruct_target_coordinates(n, sigma, lower, z_top, prime)

    delta_value = (sigma * dot(E_next, digits) - a) % prime
    z_values = load_values(digits, weights, epsilon)
    quotient = (c - sigma * dot(E_m, digits)) % prime
    assert delta_value == 0
    assert z_values[depth] % prime == 0
    assert quotient != 0
    if depth == m - 1:
        assert quotient == 1
    return digits


def crt_pair(a: int, modulus_a: int, b: int, modulus_b: int) -> tuple[int, int]:
    assert math.gcd(modulus_a, modulus_b) == 1
    step = ((b - a) * modular_inverse(modulus_a, modulus_b)) % modulus_b
    modulus = modulus_a * modulus_b
    value = (a + modulus_a * step) % modulus
    assert value % modulus_a == a % modulus_a
    assert value % modulus_b == b % modulus_b
    return value, modulus


def coordinatewise_crt(rows: list[tuple[list[int], int]]) -> tuple[list[int], int]:
    values = rows[0][0][:]
    modulus = rows[0][1]
    for next_values, next_modulus in rows[1:]:
        combined: list[int] = []
        for left, right in zip(values, next_values):
            value, checked_modulus = crt_pair(left, modulus, right, next_modulus)
            assert checked_modulus == modulus * next_modulus
            combined.append(value)
        values = combined
        modulus *= next_modulus
    return values, modulus


def kernel_basis(target_gradient: list[int]) -> list[list[int]]:
    m = len(target_gradient)
    u = target_gradient[m - 2]
    v = target_gradient[m - 1]
    gcd_value, coefficient_u, coefficient_v = extended_gcd(u, v)
    assert gcd_value == 1
    basis: list[list[int]] = []
    for index in range(m - 2):
        vector = [0] * m
        vector[index] = 1
        vector[m - 2] = -target_gradient[index] * coefficient_u
        vector[m - 1] = -target_gradient[index] * coefficient_v
        assert dot(target_gradient, vector) == 0
        basis.append(vector)
    top_vector = [0] * m
    top_vector[m - 2] = v
    top_vector[m - 1] = -u
    assert dot(target_gradient, top_vector) == 0
    basis.append(top_vector)
    return basis


def nonzero_kernel_direction(
    target_gradient: list[int],
    weights: list[int],
    epsilon: int,
    depths: list[int],
) -> tuple[list[int], int]:
    basis = kernel_basis(target_gradient)
    degree_bound = len(basis) - 1
    search_bound = len(depths) * degree_bound + 2
    for parameter in range(search_bound + 1):
        vector = [0] * len(target_gradient)
        power = 1
        for basis_vector in basis:
            vector = [left + power * right for left, right in zip(vector, basis_vector)]
            power *= parameter
        z_values = load_values(vector, weights, epsilon)
        if all(z_values[depth] != 0 for depth in depths):
            assert dot(target_gradient, vector) == 0
            return vector, parameter
    raise AssertionError("kernel direction search exhausted its exact root bound")


def crt_control() -> dict[str, Any]:
    n = 13
    sigma = 1
    depths = [3, 10, 11]
    primes = [13691, 95731, 961991]
    q_values = beta_q(n)
    a, b, c = q_values[n - 1], q_values[n], q_values[n - 2]
    A, m, weights = weight_data(n)
    assert m == 11 and depths == [3, m - 1, m]
    for prime in primes:
        assert prime > A and is_prime(prime) and b % prime == 0

    residue_rows: list[tuple[list[int], int]] = []
    per_prime_rows: list[dict[str, Any]] = []
    for depth, prime in zip(depths, primes):
        digits = per_prime_solution(n, sigma, depth, prime)
        residue_rows.append((digits, prime))
        per_prime_rows.append(
            {
                "j": depth,
                "p": prime,
                "digits_mod_p_digest": digest(digits),
            }
        )
    digits, modulus = coordinatewise_crt(residue_rows)
    assert modulus == math.prod(primes)

    E_m, E_next = e_coefficient_vectors(n)
    epsilon = sigma * ((-1) ** m)
    delta_value = sigma * dot(E_next, digits) - a
    assert delta_value % modulus == 0
    target_gradient = [sigma * coefficient for coefficient in E_next]
    k_value = delta_value // modulus
    u = target_gradient[m - 2]
    v = target_gradient[m - 1]
    gcd_value, coefficient_u, coefficient_v = extended_gcd(u, v)
    assert gcd_value == 1
    digits[m - 2] += modulus * (-k_value * coefficient_u)
    digits[m - 1] += modulus * (-k_value * coefficient_v)
    assert sigma * dot(E_next, digits) - a == 0

    direction, parameter = nonzero_kernel_direction(
        target_gradient, weights, epsilon, depths
    )
    chosen_multiplier = None
    for multiplier in range(1, len(depths) + 3):
        candidate = [
            value + multiplier * modulus * step
            for value, step in zip(digits, direction)
        ]
        z_values = load_values(candidate, weights, epsilon)
        if all(z_values[depth] != 0 for depth in depths):
            chosen_multiplier = multiplier
            digits = candidate
            break
    assert chosen_multiplier is not None

    delta_exact = sigma * dot(E_next, digits) - a
    quotient = c - sigma * dot(E_m, digits)
    z_values = load_values(digits, weights, epsilon)
    assert delta_exact == 0
    assert math.gcd(quotient, modulus) == 1
    selected_rows: list[dict[str, Any]] = []
    for depth, prime in zip(depths, primes):
        assert z_values[depth] and z_values[depth] % prime == 0
        selected_rows.append(
            {
                "j": depth,
                "p": prime,
                "z": str(z_values[depth]),
                "z_over_p": str(z_values[depth] // prime),
                "t_mod_p": quotient % prime,
                "nonzero": True,
            }
        )

    return {
        "n": n,
        "A": A,
        "m": m,
        "sigma": sigma,
        "epsilon": epsilon,
        "a": str(a),
        "b": str(b),
        "c": str(c),
        "depths": depths,
        "primes": primes,
        "P_S": str(modulus),
        "per_prime_rows": per_prime_rows,
        "per_prime_rows_digest": digest(per_prime_rows),
        "kernel_parameter": parameter,
        "nonzero_multiplier": chosen_multiplier,
        "digits_digest": digest([str(value) for value in digits]),
        "Delta_exact": delta_exact,
        "t": str(quotient),
        "gcd_t_P_S": math.gcd(quotient, modulus),
        "selected_rows": selected_rows,
        "selected_rows_digest": digest(selected_rows),
        "formal_noncanonical_control": True,
        "actual_item316_target_claim": False,
        "earlier_row_avoidance_imposed": False,
        "formal_first_occurrence_claim": False,
        "prime_census_performed": False,
        "finite_only": True,
    }


def proof_object() -> dict[str, Any]:
    return {
        "triangular_coordinates": (
            "x_j=w_j d_(j-1)-d_j gives an integral triangular automorphism; "
            "all cross-depth identities are its telescoping inverse."
        ),
        "elimination": (
            "The transition ideal quotient is a polynomial ring in the "
            "initial digit and all loads, so its load-only elimination ideal is zero."
        ),
        "window_capacity": (
            "A window with r actual first hits has product carrier height "
            "below 2r log A; sublinear windows are zero rate and linear "
            "coverage remains on the full beta scale."
        ),
        "per_prime_compatibility": (
            "For lower depths t varies in the free z_m coordinate; at the top "
            "the primitive t_0 survives; at m-1 the top gradients are resonant, "
            "while the primitive lower coordinate rho_< restores t-unit freedom."
        ),
        "penultimate_resonance": (
            "Exactly Delta+A*t-z_(m-1)=A*c-a+rho_<. On rho_<=0 the only "
            "t-unit obstruction over p|b is p|(A^2+1), a zero-rate carrier; "
            "this is a slice obstruction and not an actual-family exclusion."
        ),
        "exact_CRT": (
            "Per-prime solutions combine by CRT. The coprime top target "
            "coefficients lift Delta=0 mod P to exact Delta=0, and a target-kernel "
            "direction avoids exact zero of each selected row. Earlier-row "
            "nondivisibility is not imposed."
        ),
        "scope": (
            "First-occurrence avoidance, canonical digit inequalities, and the small "
            "positive quotients h_j are not imposed. They remain possible sources "
            "of an actual bound."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    transitions = transition_controls()
    resonances = resonance_controls()
    crt = crt_control()
    proof = proof_object()
    return {
        "schema": "item350-beta-mesoscopic-first-hit-crt-no-go-certificate-v1",
        "item": 350,
        "date": "2026-09-01",
        "status": "PROVED_MESOSCOPIC_LOAD_CRT_RESULTANT_SCOPED_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "integral_load_coordinate_automorphism": "PROVED",
            "all_window_telescoping_identity": "PROVED",
            "load_only_elimination_ideal_zero": "PROVED",
            "window_product_height_bound": "PROVED",
            "penultimate_top_gradient_resonance": "PROVED",
            "penultimate_affine_rho_bridge": "PROVED",
            "lower_zero_slice_carrier_A_squared_plus_1_zero_rate": "PROVED",
            "lower_coordinate_primitive_escape": "PROVED",
            "per_prime_target_t_unit_compatibility": "PROVED",
            "exact_integer_CRT_compatibility": "PROVED",
            "selected_exact_zero_rows_stratified_away": "PROVED",
            "earlier_row_avoidance_for_assigned_primes": "OPEN_NOT_IMPOSED",
            "formal_first_occurrence_pattern": "NOT_CLAIMED",
            "actual_mesoscopic_weighted_upper_bound": "OPEN",
            "actual_Xi_Q": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "transition_controls": transitions,
        "resonance_controls": resonances,
        "crt_control": crt,
        "strict_scope": {
            "actual_target_claim_from_finite_rows": False,
            "finite_rows_promoted": False,
            "formal_integer_digits_are_actual_beta_specialization": False,
            "actual_specialization_bridge": "OPEN",
            "closes": [
                "pairwise and finite-window recurrence resultants for selected distinct hit congruences",
                "the exact formal target equality plus t-unit localization at selected hit rows",
                "exact-zero selected rows as the explanation for the CRT compatibility control",
            ],
            "isolates": [
                "earlier-row nondivisibility required for genuine first occurrence",
                "canonical inequalities and small h_j quotients across linearly many depths",
                "external arithmetic of the common divisor b",
            ],
            "does_not_close": [
                "formal or actual first-occurrence patterns",
                "the actual mesoscopic weighted sum, Xi_Q, H_Q, K_Q, or Gamma_Q",
                "the squarefull branch, half-bound, beta capacity, Route 1, or e+pi",
            ],
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_mesoscopic_maximum": "log rad(Q)<=log Q<=log b",
            "bounded_window_rate": 0,
            "sublinear_window_rate": 0,
            "actual_weighted_upper_bound": "OPEN",
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item350_beta_mesoscopic_first_hit_crt_no_go_certificate.json",
    )
    args = parser.parse_args()
    result = build_certificate()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = Path(__file__).resolve().parent.parent / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "actual_Xi_Q": "OPEN",
                "booking": 0,
                "item": 350,
                "remaining_input": "CANONICAL_SMALL_H_MATCHING",
                "status": result["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
