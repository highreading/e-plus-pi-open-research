#!/usr/bin/env python3
"""Exact certificate for the centered closer-root/sech Pade construction.

The analytic theorems in the companion source are proved there.  This replay
checks their finite algebraic identities without treating a grid as an
all-parameter proof.  In particular it checks

* the parity reduction and the exact first nonzero remainder coefficient;
* the three positive Schur minors used for normality;
* the cofactor normalization of the [N/K] denominator of sech(sqrt(x))/2;
* the fixed-K pole asymptotic and its exact rational leading constant;
* the exact D=2 Euler/beta identity;
* the diagonal 2-adic/Catalan determinant identities and primitive clearing;
* pure dilation equivalence after endpoint clearing and primitive gcd; and
* divisibility of symmetric Laurent bands by w^2+1 at w=i.

No finite diagnostic is used to classify e+pi.  The JSON is deterministic:
elapsed time and peak RSS are printed, not written to the result file.
"""

from __future__ import annotations

import hashlib
import json
import math
import resource
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_closer_root_sech_pade_certificate.json"
RSS_LIMIT_KIB = 2 * 1024 * 1024
MP_DPS = 100


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_integer_rows(rows: list[list[int]]) -> str:
    payload = "".join(
        f"{len(row)}:" + ",".join(str(value) for value in row) + "\n"
        for row in rows
    )
    return sha256_bytes(payload.encode())


def rational_string(value: sp.Rational | sp.Integer) -> str:
    value = sp.Rational(value)
    return str(value.p) if value.q == 1 else f"{value.p}/{value.q}"


def v2_integer(value: int) -> int:
    assert value != 0
    value = abs(value)
    return (value & -value).bit_length() - 1


def v2_rational(value: sp.Rational) -> int:
    value = sp.Rational(value)
    return v2_integer(int(value.p)) - v2_integer(int(value.q))


def primitive_integer_vector(values: list[int]) -> tuple[list[int], int]:
    assert any(values)
    content = math.gcd(*(abs(value) for value in values))
    assert content > 0
    primitive = [value // content for value in values]
    first = next(value for value in primitive if value)
    if first < 0:
        primitive = [-value for value in primitive]
    assert math.gcd(*(abs(value) for value in primitive)) == 1
    return primitive, content


def primitive_rational_vector(
    values: list[sp.Rational],
) -> tuple[list[int], int]:
    denominators = [int(sp.denom(value)) for value in values]
    denominator = math.lcm(*denominators)
    integers = [int(value * denominator) for value in values]
    primitive, content = primitive_integer_vector(integers)
    return primitive, denominator // content


def cofactor_kernel(matrix: sp.Matrix) -> list[sp.Rational]:
    assert matrix.cols == matrix.rows + 1
    if matrix.rows == 0:
        return [sp.Integer(1)]
    values: list[sp.Rational] = []
    for column in range(matrix.cols):
        columns = [index for index in range(matrix.cols) if index != column]
        values.append(sp.Rational((-1) ** column * matrix[:, columns].det()))
    assert any(values)
    assert matrix * sp.Matrix(values) == sp.zeros(matrix.rows, 1)
    return values


def euler_sech_coefficient(index: int) -> sp.Rational:
    if index < 0:
        return sp.Integer(0)
    return sp.Rational(sp.euler(2 * index), 2 * sp.factorial(2 * index))


def cosh_x_coefficient(index: int) -> sp.Rational:
    if index < 0:
        return sp.Integer(0)
    return sp.Rational(2, sp.factorial(2 * index))


def sech_pade_denominator(N: int, K: int) -> list[sp.Rational]:
    matrix = sp.Matrix(
        K,
        K + 1,
        lambda row, column: euler_sech_coefficient(N + row + 1 - column),
    )
    kernel = cofactor_kernel(matrix)
    assert kernel[0] != 0
    normalized = [sp.cancel(value / kernel[0]) for value in kernel]
    assert normalized[0] == 1
    return normalized


def sech_remainder_audit(N: int, K: int) -> dict:
    denominator = sech_pade_denominator(N, K)
    numerator = [
        sum(
            denominator[column] * euler_sech_coefficient(index - column)
            for column in range(K + 1)
        )
        for index in range(N + 1)
    ]
    # U=-numerator and Q+2*cosh(sqrt(x))*U is the original bracket.
    coefficients: list[sp.Rational] = []
    for index in range(N + K + 2):
        q_term = denominator[index] if index <= K else sp.Integer(0)
        h_u = sum(
            cosh_x_coefficient(index - column) * (-numerator[column])
            for column in range(N + 1)
            if index - column >= 0
        )
        coefficients.append(sp.cancel(q_term + h_u))
    assert all(value == 0 for value in coefficients[: N + K + 1])
    assert coefficients[N + K + 1] != 0
    primitive, clearing = primitive_rational_vector(denominator)
    assert primitive[-1] != 0
    return {
        "N": N,
        "K": K,
        "primitive_denominator": primitive,
        "rational_clearing_after_content": clearing,
        "first_remainder_coefficient": rational_string(
            coefficients[N + K + 1]
        ),
    }


def parity_data(n: int, D: int) -> dict:
    N, parity_n = divmod(n, 2)
    K, parity_D = divmod(D, 2)
    epsilon = int(parity_n == 1 and parity_D == 1)
    actual_degree = 2 * K + epsilon
    exact_order = epsilon + 2 * (N + K + 1)
    predicted_minimum = n + D + 1
    assert exact_order == predicted_minimum + int(parity_n == parity_D == 0)
    return {
        "n": n,
        "D": D,
        "N": N,
        "K": K,
        "epsilon": epsilon,
        "actual_endpoint_degree": actual_degree,
        "exact_origin_order": exact_order,
        "extra_even_order": exact_order - predicted_minimum,
    }


def schur_minor_audit(N: int, K: int) -> dict:
    coefficient = lambda index: (
        sp.Rational(1, sp.factorial(2 * index))
        if index >= 0
        else sp.Integer(0)
    )
    rank_minor = (
        sp.Matrix(
            N,
            N,
            lambda row, column: coefficient(K + row - column),
        ).det()
        if N
        else sp.Integer(1)
    )
    degree_minor = sp.Matrix(
        N + 1,
        N + 1,
        lambda row, column: coefficient(K + row - column),
    ).det()
    remainder_minor = sp.Matrix(
        N + 1,
        N + 1,
        lambda row, column: coefficient(K + row + 1 - column),
    ).det()
    assert rank_minor > 0
    assert degree_minor > 0
    assert remainder_minor > 0
    return {
        "N": N,
        "K": K,
        "rank_minor": rational_string(rank_minor),
        "degree_minor": rational_string(degree_minor),
        "remainder_minor": rational_string(remainder_minor),
    }


def vandermonde(values: list[sp.Rational]) -> sp.Rational:
    result = sp.Integer(1)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            result *= values[j] - values[i]
    return sp.Rational(result)


def fixed_K_constant(K: int) -> sp.Rational:
    assert K >= 1
    rates = [sp.Rational(1, (2 * index + 1) ** 2) for index in range(K + 1)]
    constant = (
        sp.Integer(2 * K + 1) ** (2 * K - 3)
        * (vandermonde(rates[1 : K + 1]) / vandermonde(rates[:K])) ** 2
        * sp.prod(1 - rates[index] for index in range(1, K + 1))
    )
    constant = sp.factor(constant)
    assert constant > 0
    return constant


def mp_polynomial_value(coefficients: list[int | sp.Rational], value) -> mp.mpc:
    total = mp.mpc(0)
    for coefficient in reversed(coefficients):
        total = total * value + mp.mpf(str(sp.Rational(coefficient)))
    return total


def fixed_K_diagnostic(K: int, N: int) -> dict:
    denominator = sech_pade_denominator(N, K)
    height = max(abs(mp.mpf(str(value))) for value in denominator)
    endpoint = abs(mp_polynomial_value(denominator, -(mp.pi ** 2) / 4))
    scaled = endpoint / height * mp.mpf(2 * K + 1) ** (2 * N)
    constant = mp.mpf(str(fixed_K_constant(K)))
    return {
        "K": K,
        "N": N,
        "scaled_relative_endpoint": mp.nstr(scaled, 50),
        "predicted_constant": mp.nstr(constant, 50),
        "relative_error": mp.nstr(abs(scaled / constant - 1), 30),
    }


def beta_value(exponent: int) -> mp.mpf:
    return mp.nsum(
        lambda index: (-1) ** index / (2 * index + 1) ** exponent,
        [0, mp.inf],
    )


def D2_audit(N: int) -> dict:
    first = abs(int(sp.euler(2 * N)))
    second = abs(int(sp.euler(2 * N + 2)))
    factorial_factor = (2 * N + 2) * (2 * N + 1)
    raw_constant = factorial_factor * first
    content = math.gcd(raw_constant, second)
    primitive = [raw_constant // content, second // content]
    assert primitive[0] > primitive[1] > 0
    # 2^2*C(i*T/2) is already primitive: [4*q0,-q1].
    endpoint_primitive = [4 * primitive[0], -primitive[1]]
    assert math.gcd(*map(abs, endpoint_primitive)) == 1
    endpoint = abs(
        mp.mpf(endpoint_primitive[0])
        + mp.mpf(endpoint_primitive[1]) * mp.pi**2
    )
    relative = endpoint / max(map(abs, endpoint_primitive))
    beta_relative = beta_value(2 * N + 3) / beta_value(2 * N + 1) - 1
    assert abs(relative - beta_relative) < mp.mpf("1e-80")
    return {
        "N": N,
        "euler_gcd": content,
        "primitive_C_in_x": primitive,
        "primitive_cleared_endpoint_in_T2": endpoint_primitive,
        "endpoint_height": max(map(abs, endpoint_primitive)),
        "relative_endpoint": mp.nstr(relative, 50),
        "scaled_beta_asymptotic": mp.nstr(
            relative * mp.mpf(3) ** (2 * N + 3) / 8,
            40,
        ),
    }


def cosh_diagonal_numerator(N: int) -> tuple[list[sp.Rational], list[sp.Rational]]:
    series = [sp.Rational(1, sp.factorial(2 * index)) for index in range(2 * N + 1)]
    if N == 0:
        return [sp.Integer(1)], [sp.Integer(1)]
    matrix = sp.Matrix(
        N,
        N,
        lambda row, column: series[N + row + 1 - (column + 1)],
    )
    right = sp.Matrix([-series[N + row + 1] for row in range(N)])
    tail = list(matrix.inv().multiply(right))
    denominator = [sp.Integer(1)] + [sp.cancel(value) for value in tail]
    numerator = [
        sp.cancel(
            sum(
                denominator[column] * series[index - column]
                for column in range(min(index, N) + 1)
            )
        )
        for index in range(N + 1)
    ]
    # The reciprocal of numerator/denominator approximates sech; the
    # closer-root endpoint denominator Q is this numerator up to a scalar.
    return numerator, denominator


def catalan_hankel_determinants(N: int) -> tuple[int, int]:
    unshifted = sp.Matrix(
        N,
        N,
        lambda row, column: sp.catalan(row + column),
    ).det() if N else sp.Integer(1)
    shifted = sp.Matrix(
        N,
        N,
        lambda row, column: sp.catalan(row + column + 1),
    ).det() if N else sp.Integer(1)
    assert unshifted == shifted == 1
    return int(unshifted), int(shifted)


def diagonal_2adic_audit(N: int) -> dict:
    numerator, _ = cosh_diagonal_numerator(N)
    primitive, _ = primitive_rational_vector(numerator)
    assert primitive[0] > 0
    valuations = [v2_integer(value) for value in primitive]
    lower_bounds = [2 * (N - index) for index in range(N + 1)]
    assert all(
        valuations[index] >= lower_bounds[index]
        for index in range(N + 1)
    )
    assert valuations[0] == 2 * N
    assert valuations[-1] == 0
    cleared = [
        (-1) ** index * primitive[index] * 2 ** (2 * N - 2 * index)
        for index in range(N + 1)
    ]
    assert math.gcd(*map(abs, cleared)) == 1
    assert v2_integer(cleared[0]) == 4 * N
    assert max(map(abs, cleared)) >= 2 ** (4 * N)

    H = lambda index: sp.Rational(4**index, sp.factorial(2 * index))
    moment = sp.Matrix(
        N,
        N,
        lambda row, column: H(row + column + 1),
    ) if N else sp.zeros(0, 0)
    augmented = sp.Matrix(
        N + 1,
        N + 1,
        lambda row, column: H(row + column),
    )
    det_moment = moment.det() if N else sp.Integer(1)
    det_augmented = augmented.det()
    assert v2_rational(det_moment) == N
    assert v2_rational(det_augmented) == N
    determinant_ratio = sp.cancel((-1) ** N * det_augmented / det_moment)
    assert determinant_ratio == sp.cancel(4**N * numerator[-1])
    catalan_hankel_determinants(N)

    endpoint = abs(mp_polynomial_value(primitive, -(mp.pi**2) / 4))
    height = max(map(abs, primitive))
    relative_log_gain = -mp.log(endpoint / height)
    cleared_endpoint = abs(mp_polynomial_value(cleared, mp.pi**2))
    assert abs(cleared_endpoint - 2 ** (2 * N) * endpoint) < mp.mpf("1e-70") * max(1, cleared_endpoint)
    return {
        "N": N,
        "primitive_C_coefficients_digest": digest_integer_rows([primitive]),
        "primitive_C_height_digits": len(str(height)),
        "coefficient_v2": valuations,
        "cleared_endpoint_coefficients_digest": digest_integer_rows([cleared]),
        "cleared_endpoint_height_digits": len(str(max(map(abs, cleared)))),
        "relative_log_gain": mp.nstr(relative_log_gain, 40),
        "relative_log_gain_over_4NlogN": (
            mp.nstr(relative_log_gain / (4 * N * mp.log(N)), 30)
            if N > 1
            else None
        ),
        "moment_determinant_v2": v2_rational(det_moment),
        "augmented_determinant_v2": v2_rational(det_augmented),
    }


def reciprocal_series_one_plus_exp(maximum: int) -> list[sp.Rational]:
    coefficients = [sp.Rational(1, 2)]
    for index in range(1, maximum + 1):
        coefficients.append(
            sp.cancel(
                -sp.Rational(1, 2)
                * sum(
                    sp.Rational(1, sp.factorial(step))
                    * coefficients[index - step]
                    for step in range(1, index + 1)
                )
            )
        )
    return coefficients


def generic_pade_denominator(
    coefficients: list[sp.Rational],
    n: int,
    D: int,
) -> list[int]:
    matrix = sp.Matrix(
        D,
        D + 1,
        lambda row, column: (
            coefficients[n + row + 1 - column]
            if n + row + 1 - column >= 0
            else sp.Integer(0)
        ),
    )
    kernel = cofactor_kernel(matrix)
    primitive, _ = primitive_rational_vector(kernel)
    return primitive


def actual_degree(coefficients: list[int]) -> int:
    return max(index for index, coefficient in enumerate(coefficients) if coefficient)


def cleared_endpoint_vector(coefficients: list[int], scale: int) -> list[int]:
    degree = actual_degree(coefficients)
    weighted = [
        coefficient * scale ** (degree - index)
        for index, coefficient in enumerate(coefficients[: degree + 1])
    ]
    primitive, _ = primitive_integer_vector(weighted)
    return primitive


def dilation_and_centered_audit(n: int, D: int) -> dict:
    maximum = n + D
    base_series = reciprocal_series_one_plus_exp(maximum)
    q1 = generic_pade_denominator(base_series, n, D)
    q2_even_series = [2**index * value for index, value in enumerate(base_series)]
    q2_even = generic_pade_denominator(q2_even_series, n, D)
    centered_series = [
        sp.Rational(sp.euler(index), 2 * sp.factorial(index))
        if index % 2 == 0
        else sp.Integer(0)
        for index in range(maximum + 1)
    ]
    centered = generic_pade_denominator(centered_series, n, D)

    q1_endpoint = cleared_endpoint_vector(q1, 1)
    q2_even_endpoint = cleared_endpoint_vector(q2_even, 2)
    assert q1_endpoint == q2_even_endpoint
    centered_endpoint = cleared_endpoint_vector(centered, 2)

    q1_value = abs(mp_polynomial_value(q1_endpoint, 1j * mp.pi))
    centered_value = abs(mp_polynomial_value(centered_endpoint, 1j * mp.pi))
    assert max(map(abs, centered_endpoint)) >= max(map(abs, q1_endpoint))
    return {
        "n": n,
        "D": D,
        "q1_denominator": q1,
        "q2_even_dilated_denominator": q2_even,
        "common_primitive_endpoint": q1_endpoint,
        "q2_centered_sech_denominator": centered,
        "q2_centered_primitive_endpoint": centered_endpoint,
        "q1_endpoint_height": max(map(abs, q1_endpoint)),
        "q2_centered_endpoint_height": max(map(abs, centered_endpoint)),
        "centered_to_q1_absolute_value_ratio": mp.nstr(
            centered_value / q1_value,
            35,
        ),
    }


def symmetric_laurent_factor_audit(m: int) -> dict:
    w = sp.symbols("w")
    # A deterministic nontrivial reciprocal Laurent band.  Choose all
    # positive-frequency coefficients, then solve the central coefficient
    # from B(i)=0.  Real reciprocity gives the second root -i.
    positive = [sp.Integer((index + 1) ** 2 - 3 * index) for index in range(1, m + 1)]
    central = -sum(
        positive[index - 1] * (sp.I**index + sp.I ** (-index))
        for index in range(1, m + 1)
    )
    assert central.is_Integer
    polynomial = sp.expand(
        central * w**m
        + sum(
            positive[index - 1] * (w ** (m + index) + w ** (m - index))
            for index in range(1, m + 1)
        )
    )
    quotient, remainder = sp.div(polynomial, w**2 + 1, domain=sp.ZZ)
    assert remainder == 0
    assert sp.expand(polynomial.subs(w, sp.I)) == 0
    assert sp.expand(polynomial.subs(w, -sp.I)) == 0
    # The quotient retains the reciprocal symmetry with degree 2m-2.
    quotient_coefficients = sp.Poly(quotient, w).all_coeffs()
    assert quotient_coefficients == list(reversed(quotient_coefficients))
    return {
        "m": m,
        "central_coefficient": int(central),
        "band_polynomial_digest": sha256_bytes(str(polynomial).encode()),
        "quotient_digest": sha256_bytes(str(quotient).encode()),
        "divisible_by_w2_plus_1": True,
    }


def main() -> None:
    started = time.perf_counter()
    mp.mp.dps = MP_DPS

    parity_grid = [parity_data(n, D) for n in range(0, 13) for D in range(0, 13)]
    remainder_grid = [
        sech_remainder_audit(N, K)
        for N in range(0, 7)
        for K in range(0, 6)
    ]
    schur_grid = [
        schur_minor_audit(N, K)
        for N in range(0, 7)
        for K in range(0, 6)
    ]
    fixed_constants = {
        str(K): rational_string(fixed_K_constant(K))
        for K in range(1, 6)
    }
    fixed_diagnostics = [
        fixed_K_diagnostic(K, N)
        for K in range(1, 5)
        for N in (max(K + 2, 8), 16, 28)
        if N >= K
    ]
    D2_grid = [D2_audit(N) for N in range(1, 31)]
    diagonal_grid = [diagonal_2adic_audit(N) for N in range(1, 13)]
    dilation_grid = [
        dilation_and_centered_audit(n, D)
        for D in (2, 3)
        for n in range(max(2, D), 13)
    ]
    symmetric_grid = [symmetric_laurent_factor_audit(m) for m in range(1, 9)]

    sample = next(
        row for row in dilation_grid if row["n"] == 8 and row["D"] == 2
    )
    assert sample["q1_denominator"] == [306, 0, 31]
    assert sample["q2_even_dilated_denominator"] == [153, 0, 62]
    assert sample["common_primitive_endpoint"] == [306, 0, 31]
    assert sample["q2_centered_sech_denominator"] == [124650, 0, 50521]
    assert sample["q2_centered_primitive_endpoint"] == [498600, 0, 50521]

    result = {
        "schema_version": 1,
        "logical_scope": (
            "Exact finite replay of parity, Schur minors, cofactors, fixed-K "
            "constants, D=2 beta arithmetic, diagonal 2-adic clearing, pure "
            "dilation, and symmetric-band factorization. Finite grids are not "
            "classification or all-parameter asymptotic proofs."
        ),
        "environment": {
            "python": sys.version.split()[0],
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
            "mp_dps": MP_DPS,
            "rss_limit_kib": RSS_LIMIT_KIB,
        },
        "parity_grid": parity_grid,
        "remainder_grid": remainder_grid,
        "schur_grid": schur_grid,
        "fixed_K_constants": fixed_constants,
        "fixed_K_diagnostics": fixed_diagnostics,
        "D2_grid": D2_grid,
        "diagonal_2adic_grid": diagonal_grid,
        "dilation_centered_grid": dilation_grid,
        "symmetric_laurent_grid": symmetric_grid,
        "distinguished_n8_D2_sample": sample,
        "proof_boundaries": {
            "all_parameter_normality": "proved in companion source by Schur positivity",
            "fixed_K_asymptotic": "proved in companion source by signed Cauchy-Binet dominance",
            "diagonal_asymptotic": "proved from Dzyadyk's primary theorem plus coefficient bounds",
            "unknown_arithmetic": "no uniform primitive cofactor-content asymptotic for fixed K",
            "classification_of_e_plus_pi": False,
        },
    }

    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss < RSS_LIMIT_KIB
    elapsed = time.perf_counter() - started
    print(f"wrote {OUT}")
    print(f"elapsed_seconds={elapsed:.6f}")
    print(f"peak_rss_kib={peak_rss}")
    print(f"json_sha256={sha256_bytes(OUT.read_bytes())}")


if __name__ == "__main__":
    main()
