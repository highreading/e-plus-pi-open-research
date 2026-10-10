#!/usr/bin/env python3
"""Deterministic certificate for Item 411.

The report proves an exact generator transport for the actual mixed-cubic
family, an exact compatible-prime branch decomposition, a polynomial boundary
normal form, and a scoped transform-only no-go.  The finite rows below are
normalization controls only.  They are not used to infer a support theorem.
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

STEM = "item411_mixed_primitive_boundary_transport"

DEPENDENCIES = {
    "sources/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_report.md":
        "245bf2e557dd81ac88c94e9d0adc8990f203e3ab40680d23bd50f8e435240c48",
    "scripts/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_certificate.py":
        "90c7f5d38b168e9999b220e52d565fb77faa4b9872b2ffb70a66387f1caecd3a",
    "results/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_certificate.json":
        "c7516c720ba6a3bdb0f8803f0199fb6d137f593d3ef07fc9cd2205a73eb2a1fa",
    "manifests/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_manifest.json":
        "71ad98ae5ff23cca6ebc32ad534879e6fac29ec0cbcb034838412f25e2f98f68",
    "results/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_root_audit.json":
        "a8cdc2a03f597ddcac48119b9afd5c331597dff6e0f035491d8db4753a1ee80d",
    "sources/item406_mixed_cubic_actual_adjacent_recurrence_report.md":
        "a9c33967b42f5ae09c2c0c71de1b956ca240e49c367be46f3af2878cd96cbb83",
    "scripts/item406_mixed_cubic_actual_adjacent_recurrence_certificate.py":
        "d2ef50877b608916bd3f7a3857d234e575168b5ccf4cfd545f297a31e6054a99",
    "results/item406_mixed_cubic_actual_adjacent_recurrence_certificate.json":
        "14267bda592a0b302732901fbfb34f901940aec69ea824ed614f1bf385662caa",
    "manifests/item406_mixed_cubic_actual_adjacent_recurrence_manifest.json":
        "235d1d1a451eaaf0e73b7b16bd7541d77318f33cb7865282ac76e1fd9a190ff4",
    "results/item406_mixed_cubic_actual_adjacent_recurrence_root_audit.json":
        "ee2c1b614dfea36a7602c8b010cf3bd7ba93368d22daf47650367d4245bcb241",
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "sources/item396_fixed_gap_resultant_3adic_report.md":
        "7355b6909994357583f799e627e1ff19edb230a6a9002ee845be585057726aca",
}

NORMALIZATION_Q = (1, 5, 7, 11, 13, 17, 25, 37, 43, 49)
LOCAL_PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
COMPATIBLE_ROWS = ((5, 11), (7, 13), (13, 31), (25, 31), (37, 43))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_dependencies() -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        digest = sha256_bytes((ROOT / relative).read_bytes())
        assert digest == expected, (relative, expected, digest)
        observed[relative] = digest
    return observed


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= value - index
    return answer / math.factorial(degree)


def h_power_coefficients(parameter: int, degree: int) -> list[Fraction]:
    """Coefficients of H(z)^(parameter/3), H=1+2z+3z^2/2+z^3/2."""
    exponent = Fraction(parameter, 3)
    polynomial = (Fraction(1), Fraction(2), Fraction(3, 2), Fraction(1, 2))
    coefficients = [Fraction(1)]
    for target in range(1, degree + 1):
        total = Fraction(0)
        for index in range(1, min(3, target) + 1):
            total += (
                ((exponent + 1) * index - target)
                * polynomial[index]
                * coefficients[target - index]
            )
        coefficients.append(total / target)
    return coefficients


def negative_power_with_polynomial(q_value: int, degree: int, shift: int) -> int:
    polynomial_degree = 1 + 3 * shift
    return sum(
        math.comb(polynomial_degree, index)
        * math.comb(q_value + degree - index - 1, degree - index)
        for index in range(min(polynomial_degree, degree) + 1)
    )


def actual_fixed_gap_coefficients(q_value: int) -> tuple[Fraction, ...]:
    n_value = q_value - 1
    half_n = n_value // 2
    parameter = 2 * q_value - 3

    full_zero = h_power_coefficients(parameter, n_value)
    c_zero = 2 * full_zero[n_value]
    if n_value:
        c_zero += full_zero[n_value - 1]

    full_one = h_power_coefficients(parameter - 3, n_value)
    c_one = Fraction(0)
    for index in range(min(4, n_value) + 1):
        c_one += (
            Fraction(math.comb(4, index) * 2 ** (4 - index), 2)
            * full_one[n_value - index]
        )

    exponent_zero = Fraction(parameter, 3)
    exponent_one = exponent_zero - 1
    binomial_zero = Fraction(1)
    binomial_one = Fraction(1)
    t_zero = Fraction(0)
    t_one = Fraction(0)
    for index in range(half_n + 1):
        remaining = n_value - 2 * index
        t_zero += binomial_zero * negative_power_with_polynomial(
            q_value, remaining, 0
        )
        t_one += binomial_one * negative_power_with_polynomial(
            q_value, remaining, 1
        )
        binomial_zero *= (exponent_zero - index) / (index + 1)
        binomial_one *= (exponent_one - index) / (index + 1)
    return c_zero, t_zero, c_one, t_one


def base_adjacent_coefficients(q_value: int) -> tuple[Fraction, ...]:
    n_value = q_value - 1
    parameter = 2 * q_value - 3
    exponent = Fraction(parameter, 3)
    h_coefficients = h_power_coefficients(parameter, n_value)
    u_value = h_coefficients[n_value]
    v_value = h_coefficients[n_value - 1] if n_value else Fraction(0)

    b_coefficients: list[Fraction] = []
    for degree in range(n_value + 1):
        total = Fraction(0)
        for half_degree in range(degree // 2 + 1):
            total += generalized_binomial(exponent, half_degree) * math.comb(
                q_value + degree - 2 * half_degree - 1,
                degree - 2 * half_degree,
            )
        b_coefficients.append(total)
    r_value = b_coefficients[n_value]
    s_value = b_coefficients[n_value - 1] if n_value else Fraction(0)
    return u_value, v_value, r_value, s_value


def valuation(value: Fraction, prime: int) -> int:
    if not value:
        return 10**9
    numerator = abs(value.numerator)
    denominator = value.denominator
    answer = 0
    while numerator % prime == 0:
        numerator //= prime
        answer += 1
    while denominator % prime == 0:
        denominator //= prime
        answer -= 1
    return answer


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def convolution(left: list[int], right: list[int], degree: int, prime: int) -> list[int]:
    answer = [0] * (degree + 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right[: degree + 1 - i]):
            answer[i + j] = (answer[i + j] + left_value * right_value) % prime
    return answer


def binomial_series(exponent: int, degree: int, prime: int) -> list[int]:
    """Coefficients of (1+z)^exponent, including negative exponent."""
    answer = [1]
    for index in range(1, degree + 1):
        answer.append(
            answer[-1] * (exponent - index + 1) * pow(index, -1, prime) % prime
        )
    return answer


def substitute_even(series: list[int], degree: int) -> list[int]:
    answer = [0] * (degree + 1)
    for index, value in enumerate(series):
        if 2 * index <= degree:
            answer[2 * index] = value
    return answer


def reciprocal_rows(m_value: int, q_value: int, prime: int) -> tuple[list[int], ...]:
    n_value = q_value - 1
    k_value = 4 * m_value + 1
    e_value = prime - k_value
    one_minus = [math.comb(6 * m_value, index) * (-1) ** index % prime
                 for index in range(min(6 * m_value, n_value) + 1)]

    negative_even = substitute_even(
        binomial_series(-k_value, n_value // 2, prime), n_value
    )
    positive_even = substitute_even(
        binomial_series(e_value, n_value // 2, prime), n_value
    )
    negative_linear = binomial_series(-k_value, n_value, prime)
    positive_linear = binomial_series(e_value, n_value, prime)

    r_series = convolution(one_minus, negative_even, n_value, prime)
    s_series = convolution(r_series, negative_linear, n_value, prime)
    f_series = convolution(one_minus, positive_even, n_value, prime)
    j_series = convolution(f_series, positive_linear, n_value, prime)
    assert r_series == f_series
    assert s_series == j_series
    return r_series, s_series, f_series, j_series


def transport_and_smith_rows() -> dict[str, object]:
    stream: list[str] = []
    checked = 0
    for q_value in NORMALIZATION_Q:
        n_value = q_value - 1
        a_factor = 2 * n_value - 1
        k_value = 4 ** n_value
        u_value, v_value, r_value, s_value = base_adjacent_coefficients(q_value)
        c_zero, t_zero, c_one, t_one = actual_fixed_gap_coefficients(q_value)

        assert c_zero == 2 * u_value + v_value
        assert t_zero == r_value + s_value
        assert a_factor * c_one == (5 * n_value - 1) * c_zero - 6 * u_value
        assert a_factor * t_one == (5 * n_value - 7) * t_zero + 6 * r_value

        determinant = u_value * r_value - s_value * (u_value + v_value)
        rho = c_zero * t_one - c_one * t_zero
        assert a_factor * rho == 6 * determinant

        u_zero = t_zero**3 - k_value * c_zero**3
        u_one = t_one**3 - k_value * c_one**3
        v_zero = s_value**3 - k_value * u_value**3
        v_one = r_value**3 - k_value * (u_value + v_value) ** 3

        for prime in LOCAL_PRIMES:
            if 6 * a_factor % prime == 0:
                continue
            h_original = min(
                valuation(value, prime)
                for value in (c_zero, t_zero, c_one, t_one)
            )
            h_base = min(
                valuation(value, prime)
                for value in (u_value, v_value, r_value, s_value)
            )
            assert h_original == h_base
            gamma_original = min(
                valuation(rho, prime) - 2 * h_original,
                valuation(u_zero, prime) - 3 * h_original,
                valuation(u_one, prime) - 3 * h_original,
            )
            gamma_base = min(
                valuation(determinant, prime) - 2 * h_base,
                valuation(v_zero, prime) - 3 * h_base,
                valuation(v_one, prime) - 3 * h_base,
            )
            assert gamma_original == gamma_base
            checked += 1
            stream.append(
                f"{q_value}:{prime}:{h_base}:{gamma_base}:{determinant}:{v_zero}:{v_one}"
            )

    return {
        "generator_change_matrix": "-[ [1,1], [5n-7,5n-1] ] after scaling lambda1 by A=2n-1",
        "generator_change_determinant": 6,
        "connection_identity": "(2n-1)*(C0*T1-C1*T0)=6*(u*r-s*(u+v))",
        "local_content_and_primitive_gamma_rows_checked": checked,
        "normalization_only_not_uniform_proof": True,
        "witness_sha256": sha256_bytes("\n".join(stream).encode("ascii")),
    }


def compatible_normalization_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for q_value, prime in COMPATIBLE_ROWS:
        m_value = (prime - q_value) // 6
        assert m_value >= 1 and prime == 6 * m_value + q_value
        n_value = q_value - 1
        k_value = 4 * m_value + 1
        e_value = 2 * m_value + q_value - 1
        x_value = pow(2, e_value, prime)
        y_value = pow(4, m_value, prime)
        assert pow(x_value, 3, prime) == pow(4, n_value, prime)
        assert x_value * pow(2, -n_value, prime) % prime == y_value

        r_series, s_series, f_series, j_series = reciprocal_rows(
            m_value, q_value, prime
        )
        u_fraction, v_fraction, r_fraction, s_fraction = base_adjacent_coefficients(q_value)
        u_value = fraction_mod(u_fraction, prime)
        v_value = fraction_mod(v_fraction, prime)
        r_value = fraction_mod(r_fraction, prime)
        s_value = fraction_mod(s_fraction, prime)

        assert r_value == r_series[n_value]
        assert s_value == r_series[n_value - 1]
        assert v_value == pow(2, 1 - n_value, prime) * s_series[n_value - 1] % prime
        assert u_value == (
            pow(2, -n_value, prime)
            * (s_series[n_value] - s_series[n_value - 1])
        ) % prime

        c_zero, t_zero, c_one, t_one = actual_fixed_gap_coefficients(q_value)
        c_zero_mod, t_zero_mod, c_one_mod, t_one_mod = (
            fraction_mod(value, prime)
            for value in (c_zero, t_zero, c_one, t_one)
        )
        lambda_zero = (c_zero_mod * x_value - t_zero_mod) % prime
        lambda_one = (c_one_mod * x_value - t_one_mod) % prime
        epsilon_zero = (s_value - x_value * u_value) % prime
        epsilon_one = (r_value - x_value * (u_value + v_value)) % prime
        a_factor = 2 * n_value - 1
        assert lambda_zero == (-epsilon_zero - epsilon_one) % prime
        assert a_factor * lambda_one % prime == (
            -(5 * n_value - 7) * epsilon_zero
            - (5 * n_value - 1) * epsilon_one
        ) % prime
        assert (lambda_zero == 0 and lambda_one == 0) == (
            epsilon_zero == 0 and epsilon_one == 0
        )

        boundary_left = (f_series[n_value - 1], f_series[n_value])
        boundary_right = (
            y_value * (j_series[n_value] - j_series[n_value - 1]) % prime,
            y_value * (j_series[n_value] + j_series[n_value - 1]) % prime,
        )
        assert (epsilon_zero, epsilon_one) == (
            (boundary_left[0] - boundary_right[0]) % prime,
            (boundary_left[1] - boundary_right[1]) % prime,
        )

        rows.append(
            {
                "q": q_value,
                "p": prime,
                "m": m_value,
                "n": n_value,
                "k": k_value,
                "E=p-k": e_value,
                "X=2^E_mod_p": x_value,
                "Y=4^m_mod_p": y_value,
                "F_adjacent": list(boundary_left),
                "J_adjacent": [j_series[n_value - 1], j_series[n_value]],
                "selected_boundary_residual": [epsilon_zero, epsilon_one],
                "actual_lambda_residual": [lambda_zero, lambda_one],
                "positive_exponent_lift_matches_reciprocal_series": True,
                "normalization_only_not_support_evidence": True,
            }
        )
    return rows


def branch_separation_witness() -> dict[str, object]:
    """Ambient q=7,p=13 witness: unmarked G branch, wrong selected root."""
    prime = 13
    q_value = 7
    m_value = 1
    n_value = q_value - 1
    e_value = 2 * m_value + q_value - 1
    x_value = pow(2, e_value, prime)
    zeta = 3
    assert pow(zeta, 3, prime) == 1 and zeta != 1
    y_value = zeta * x_value % prime
    u_value, v_value = 1, 2
    s_value = y_value * u_value % prime
    r_value = y_value * (u_value + v_value) % prime
    k_value = pow(4, n_value, prime)
    determinant = (u_value * r_value - s_value * (u_value + v_value)) % prime
    v_zero = (s_value**3 - k_value * u_value**3) % prime
    v_one = (r_value**3 - k_value * (u_value + v_value) ** 3) % prime
    selected = (
        (s_value - x_value * u_value) % prime,
        (r_value - x_value * (u_value + v_value)) % prime,
    )
    assert (determinant, v_zero, v_one) == (0, 0, 0)
    assert selected != (0, 0)
    return {
        "q": q_value,
        "p": prime,
        "m": m_value,
        "mu3_nontrivial_zeta": zeta,
        "selected_root_X": x_value,
        "wrong_common_root_zeta_X": y_value,
        "base_quadruple_u_v_r_s": [u_value, v_value, r_value, s_value],
        "unmarked_primitive_forms_D_V0_V1": [determinant, v_zero, v_one],
        "selected_linear_residuals": list(selected),
        "ambient_branch_witness_not_actual_mixed_cubic_row": True,
    }


def boundary_functionals(
    coefficients: list[int], k_value: int, y_value: int, prime: int
) -> tuple[int, int]:
    n_value = len(coefficients) - 1
    kernel = binomial_series(-k_value, n_value, prime)
    transformed = convolution(coefficients, kernel, n_value, prime)
    minus_residual = (
        coefficients[n_value - 1]
        - y_value * (transformed[n_value] - transformed[n_value - 1])
    ) % prime
    plus_residual = (
        coefficients[n_value]
        - y_value * (transformed[n_value] + transformed[n_value - 1])
    ) % prime
    return minus_residual, plus_residual


def solve_two_by_two(
    a00: int, a01: int, a10: int, a11: int, b0: int, b1: int, prime: int
) -> tuple[int, int]:
    determinant = (a00 * a11 - a01 * a10) % prime
    inverse = pow(determinant, -1, prime)
    return (
        (b0 * a11 - a01 * b1) * inverse % prime,
        (a00 * b1 - b0 * a10) * inverse % prime,
    )


def transform_only_countermodels() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for q_value, prime in COMPATIBLE_ROWS:
        m_value = (prime - q_value) // 6
        n_value = q_value - 1
        k_value = 4 * m_value + 1
        y_value = pow(4, m_value, prime)
        assert n_value >= 4

        base = [0] * (n_value + 1)
        base[0] = 1
        residual = boundary_functionals(base, k_value, y_value, prime)

        column_vectors = []
        for index in (n_value - 2, n_value - 3):
            vector = [0] * (n_value + 1)
            vector[index] = 1
            column_vectors.append(boundary_functionals(vector, k_value, y_value, prime))
        a00, a10 = column_vectors[0]
        a01, a11 = column_vectors[1]
        determinant = (a00 * a11 - a01 * a10) % prime
        determinant_formula = (
            y_value**2
            * k_value**2
            * (k_value**2 - 1)
            * pow(6, -1, prime)
        ) % prime
        assert determinant == determinant_formula != 0

        solution = solve_two_by_two(
            a00, a01, a10, a11, -residual[0], -residual[1], prime
        )
        base[n_value - 2], base[n_value - 3] = solution
        assert boundary_functionals(base, k_value, y_value, prime) == (0, 0)
        rows.append(
            {
                "q": q_value,
                "p": prime,
                "m": m_value,
                "rank_minor": determinant,
                "rank_minor_formula": "Y^2*k^2*(k^2-1)/6",
                "R0": 1,
                "nonzero_coefficients": [
                    [index, value] for index, value in enumerate(base) if value
                ],
                "boundary_collision_residual": [0, 0],
                "ambient_transform_only_not_actual_R": True,
            }
        )
    return rows


def build_certificate() -> dict[str, object]:
    dependencies = verify_dependencies()
    transport = transport_and_smith_rows()
    compatible = compatible_normalization_rows()
    branch_witness = branch_separation_witness()
    countermodels = transform_only_countermodels()
    witness_payload = json.dumps(
        {
            "transport": transport,
            "compatible": compatible,
            "branch": branch_witness,
            "countermodels": countermodels,
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("ascii")
    return {
        "schema": "item411-mixed-primitive-boundary-transport-v1",
        "item": 411,
        "status": "CANONICAL_ROOT_AUDITED_NO_BOOKING",
        "dependency_sha256": dependencies,
        "exact_generator_transport": transport,
        "compatible_polynomial_boundary_normalization_rows": compatible,
        "unmarked_branch_separation": branch_witness,
        "transform_only_countermodels": countermodels,
        "assertions": {
            "primitive_G_carrier_is_exact_after_local_content_removal": True,
            "unmarked_G_has_three_cube_root_branches_when_p_is_1_mod_3": True,
            "actual_collision_is_only_the_zeta_equals_1_branch": True,
            "positive_exponent_polynomial_lift_is_exact_below_degree_p": True,
            "transform_only_no_go_is_ambient_not_actual_family": True,
            "finite_rows_are_normalization_only": True,
            "booking_delta_is_zero": True,
        },
        "smallest_missing_actual_lemma": (
            "For every compatible p=6m+q with m>=1,q>=5, the selected "
            "two-boundary polynomial residuals cannot both vanish."
        ),
        "capacity": {
            "frozen_booked_deficit_unchanged":
                "1.0196329836694317938803064012...",
            "combined_large_component_ceiling_unchanged":
                "log(136)/6 = 0.8187758142893420014168718304...",
            "proved_total_capacity_ceiling_delta": 0,
            "booking_delta": 0,
            "conditional_selected_lemma_consequence":
                "c_m^>=1 and closure of the separate large-prime component ceiling",
        },
        "labels": {
            "PROVED": [
                "exact all-q generator transport and local primitive carrier away from 6(2q-3)",
                "exact cube-root branch decomposition of H_q*G_q^prim at compatible primes",
                "exact selected two-boundary positive-exponent polynomial criterion",
                "uniform ambient transform-only collision countermodel",
            ],
            "CONDITIONAL": [
                "selected two-boundary noncollision for all compatible primes gives c_m^>=1",
            ],
            "OPEN": [
                "selected two-boundary noncollision in the actual polynomial family",
                "unmarked primitive-G support and H_q*G_q^prim divisibility by P_q",
                "any valuation-weighted o(m) theorem for c_m^>",
                "Route 1 and irrationality of e+pi",
            ],
        },
        "witness_sha256": sha256_bytes(witness_payload),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results" / f"{STEM}_certificate.json",
    )
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    certificate = build_certificate()
    payload = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.replay is not None:
        frozen = args.replay.read_text(encoding="utf-8")
        if frozen != payload:
            raise AssertionError("replay payload differs from frozen certificate")
    args.output.write_text(payload, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
