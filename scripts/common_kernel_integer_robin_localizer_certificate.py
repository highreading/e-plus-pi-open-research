#!/usr/bin/env python3
"""Replay the exact integer Robin-localizer and denominator barrier.

The companion note contains the all-parameter proofs.  This script checks
the polynomial identities, rational output formula, finite endpoint-order
lattices, and predicted prime valuations on exact grids.  It does not
extrapolate finite data and proves nothing about the arithmetic nature of
e+pi.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_integer_robin_localizer_barrier.md"
OUTPUT = ROOT / "results/common_kernel_integer_robin_localizer_certificate.json"

# Failure guard only.  It neither allocates nor caps the available Colab RAM.
RSS_GUARD_KIB = 8 * 1024 * 1024
MAX_M_IDENTITY = 80
MAX_N_ORDER = 80
MAX_N_SMITH = 30

DEPENDENCIES = {
    "sources/common_kernel_stein_robin_parameterization.md":
        "6853ceef8ae4065c65d0954a5ef0d0c7b1ae43e76167f999cbd3a11818432406",
    "scripts/common_kernel_stein_robin_certificate.py":
        "a841840c5b6abe8778ae58cb50eb00eb201cacdcbde389f32a9f4cdae9673bbf",
    "results/common_kernel_stein_robin_certificate.json":
        "be08f99f85f11a42f9f9efc32091eb6d6300a81b4511352ca58d0c6792d09aa5",
    "sources/common_kernel_stein_robin_quadratic_correction_barrier.md":
        "1611c4976a64836a20209871a55b92e09bcb6c0c9cb18701cd800567b1a0ac21",
    "scripts/common_kernel_stein_robin_quadratic_correction_certificate.py":
        "f814471c0c627ff2fb9c4da2f99a4a37ebf6380316d030796c7ddc946c4921dc",
    "results/common_kernel_stein_robin_quadratic_correction_certificate.json":
        "4641657f345e13bde4ed84b4642ffd4942d3f6b8448f9c9a60ecbe573dbf216d",
}


Number = int | Fraction
Polynomial = list[Number]
GaussianInteger = tuple[int, int]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
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


def trim(poly: Polynomial) -> Polynomial:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [0]


def poly_add(*polynomials: Polynomial) -> Polynomial:
    size = max((len(poly) for poly in polynomials), default=1)
    result: Polynomial = [0] * size
    for poly in polynomials:
        for index, value in enumerate(poly):
            result[index] += value
    return trim(result)


def poly_scale(poly: Polynomial, scalar: Number) -> Polynomial:
    return trim([scalar * value for value in poly])


def poly_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return trim(result)


def poly_power(poly: Polynomial, exponent: int) -> Polynomial:
    assert exponent >= 0
    result: Polynomial = [1]
    base = trim(poly)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = poly_multiply(result, base)
        remaining //= 2
        if remaining:
            base = poly_multiply(base, base)
    return result


def derivative(poly: Polynomial) -> Polynomial:
    if len(poly) <= 1:
        return [0]
    return trim([index * poly[index] for index in range(1, len(poly))])


def stein_x(poly: Polynomial) -> Polynomial:
    return poly_add(
        derivative(poly),
        poly_scale(poly_multiply([0, 1], derivative(poly)), -1),
        poly_scale(poly_multiply([0, 1], poly), -1),
    )


def stein_t(poly: Polynomial) -> Polynomial:
    return poly_add(
        poly_scale(poly_multiply([0, 1], derivative(poly)), -1),
        poly_scale(poly, -1),
        poly_multiply([0, 1], poly),
    )


def t_to_x(poly: Polynomial) -> Polynomial:
    result: Polynomial = [0]
    for exponent, coefficient in enumerate(poly):
        term = [
            coefficient * math.comb(exponent, index) * (-1) ** index
            for index in range(exponent + 1)
        ]
        result = poly_add(result, term)
    return trim(result)


def divide_monic(dividend: Polynomial, divisor: Polynomial) -> tuple[Polynomial, Polynomial]:
    dividend = trim(dividend)
    divisor = trim(divisor)
    assert divisor[-1] == 1
    if len(dividend) < len(divisor):
        return [0], dividend
    remainder = dividend[:]
    quotient: Polynomial = [0] * (len(dividend) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[shift] += coefficient
        for index, value in enumerate(divisor):
            remainder[index + shift] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def integral_01(poly: Polynomial) -> Fraction:
    return sum(
        (Fraction(value, index + 1) for index, value in enumerate(poly)),
        Fraction(0),
    )


def evaluate(poly: Polynomial, value: Number) -> Number:
    result: Number = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def fraction_string(value: Fraction | int) -> str:
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def gaussian_multiply(left: GaussianInteger, right: GaussianInteger) -> GaussianInteger:
    a_value, b_value = left
    c_value, d_value = right
    return a_value * c_value - b_value * d_value, a_value * d_value + b_value * c_value


def gaussian_power_w(exponent: int) -> GaussianInteger:
    result = (1, 0)
    base = (1, -1)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = gaussian_multiply(result, base)
        remaining //= 2
        if remaining:
            base = gaussian_multiply(base, base)
    return result


def v2(value: int) -> int:
    assert value > 0
    valuation = 0
    while value % 2 == 0:
        valuation += 1
        value //= 2
    return valuation


def factorial_v2(n_value: int) -> int:
    total = 0
    divisor = 2
    while divisor <= n_value:
        total += n_value // divisor
        divisor *= 2
    return total


def h_polynomial(m_value: int) -> Polynomial:
    assert m_value >= 1
    result: Polynomial = [0] * (4 * m_value + 5)
    result[4 * m_value] = m_value + 1
    result[4 * m_value + 4] = -m_value
    return trim(result)


def localizer_quotient(m_value: int) -> Polynomial:
    # -(1-x^2)^2 * sum_{j=0}^{m-1}(j+1)x^(4j)
    series: Polynomial = [0] * (4 * (m_value - 1) + 1)
    for index in range(m_value):
        series[4 * index] = index + 1
    return poly_scale(poly_multiply(poly_power([1, 0, -1], 2), series), -1)


def primes_below(limit: int) -> list[int]:
    if limit <= 2:
        return []
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit - 1) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start:limit:prime] = b"\x00" * (((limit - 1 - start) // prime) + 1)
    return [index for index, is_prime in enumerate(sieve) if is_prime]


def factor_integer(value: int) -> dict[str, int]:
    value = abs(value)
    factors: dict[str, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            exponent = 0
            while value % divisor == 0:
                value //= divisor
                exponent += 1
            factors[str(divisor)] = exponent
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[str(value)] = 1
    return factors


def gcd_of_maximal_minors(columns: list[tuple[int, int]]) -> int:
    result = 0
    for left in range(len(columns)):
        for right in range(left + 1, len(columns)):
            determinant = (
                columns[left][0] * columns[right][1]
                - columns[left][1] * columns[right][0]
            )
            result = math.gcd(result, abs(determinant))
    return result


def reduce_mod_v_t(poly: Polynomial) -> tuple[int, int]:
    # v=t^2-2t+2 is monic.  The inputs used here have integer coefficients.
    _, remainder = divide_monic(poly, [2, -2, 1])
    remainder = remainder + [0] * (2 - len(remainder))
    assert all(Fraction(value).denominator == 1 for value in remainder)
    return int(remainder[0]), int(remainder[1])


def correction_order_possible(n_value: int, order: int) -> tuple[bool, int, int]:
    columns: list[tuple[int, int]] = []
    for offset in range(4):
        monomial = [0] * (order + offset) + [1]
        columns.append(reduce_mod_v_t(stein_t(monomial)))
    target = reduce_mod_v_t(
        poly_add([math.factorial(n_value)], poly_scale([0] * n_value + [1], -1))
    )
    lattice_index = gcd_of_maximal_minors(columns)
    augmented_index = gcd_of_maximal_minors(columns + [target])
    assert lattice_index > 0
    return augmented_index == lattice_index, lattice_index, augmented_index


def localizer_identity_rows() -> tuple[list[dict[str, object]], str]:
    u_squared = poly_power([1, 0, 1], 2)
    rows: list[dict[str, object]] = []
    compact: list[list[object]] = []
    for m_value in range(1, MAX_M_IDENTITY + 1):
        h_value = h_polynomial(m_value)
        quotient, remainder = divide_monic(poly_add(h_value, [-1]), u_squared)
        assert remainder == [0]
        assert quotient == localizer_quotient(m_value)

        expected_derivative: Polynomial = [0] * (4 * m_value + 4)
        expected_derivative[4 * m_value - 1] = 4 * m_value * (m_value + 1)
        expected_derivative[4 * m_value + 3] = -4 * m_value * (m_value + 1)
        assert derivative(h_value) == trim(expected_derivative)
        assert evaluate(h_value, 0) == 0
        assert evaluate(h_value, 1) == 1

        mass = integral_01(h_value)
        expected_mass = Fraction(8 * m_value + 5, (4 * m_value + 1) * (4 * m_value + 5))
        assert mass == expected_mass
        derivative_mass = integral_01(poly_multiply([1, -1], derivative(h_value)))
        assert derivative_mass == mass

        compact.append([m_value, mass.numerator, mass.denominator])
        if m_value in {1, 2, 3, 4, 8, 16, 32, 64, 80}:
            rows.append(
                {
                    "m": m_value,
                    "degree": len(h_value) - 1,
                    "mass": fraction_string(mass),
                    "quotient_degree": len(quotient) - 1,
                    "endpoint_values": [0, 1],
                }
            )
    encoding = json.dumps(compact, separators=(",", ":")).encode()
    return rows, hashlib.sha256(encoding).hexdigest()


def gaussian_order_rows() -> tuple[list[dict[str, object]], str]:
    rows: list[dict[str, object]] = []
    compact: list[list[object]] = []
    for n_value in range(1, MAX_N_ORDER + 1):
        excess = 2 * factorial_v2(n_value) - n_value
        if n_value in {1, 3}:
            category = "nonintegral_U"
            assert excess < 0
        elif n_value == 2:
            category = "U_equals_minus_w_mod_w2"
            assert excess == 0
        elif n_value % 2:
            category = "odd_mod_w_contradiction"
            assert n_value >= 5 and excess >= 1
        else:
            category = "even_mod_w2_contradiction"
            assert n_value >= 4 and excess >= 2
        compact.append([n_value, excess, category])
        if n_value <= 10 or n_value in {16, 25, 40, 60, 80}:
            rows.append(
                {
                    "N": n_value,
                    "w_valuation_excess": excess,
                    "proof_case": category,
                }
            )
    encoding = json.dumps(compact, separators=(",", ":")).encode()
    return rows, hashlib.sha256(encoding).hexdigest()


def smith_order_rows() -> tuple[list[dict[str, object]], str]:
    rows: list[dict[str, object]] = []
    compact: list[list[object]] = []
    for n_value in range(1, MAX_N_SMITH + 1):
        possibilities: list[int] = []
        indices: list[list[int]] = []
        for order in range(n_value + 1):
            possible, lattice_index, augmented_index = correction_order_possible(n_value, order)
            if possible:
                possibilities.append(order)
            indices.append([order, lattice_index, augmented_index])
        assert possibilities
        maximum = max(possibilities)
        assert maximum < n_value
        compact.append([n_value, maximum, indices])
        rows.append(
            {
                "N": n_value,
                "max_attainable_order": maximum,
                "order_N_possible": correction_order_possible(n_value, n_value)[0],
            }
        )
    encoding = json.dumps(compact, separators=(",", ":")).encode()
    return rows, hashlib.sha256(encoding).hexdigest()


def output_formula(
    m_value: int,
    g_zero: Polynomial,
    g_value: Polynomial,
    remainder_a: int,
    remainder_b: int,
    k_value: Polynomial,
) -> Fraction:
    result = 4 * integral_01(g_zero)
    for index, coefficient in enumerate(g_value):
        result += Fraction(4 * (m_value + 1) * coefficient, 4 * m_value + index + 1)
        result -= Fraction(4 * m_value * coefficient, 4 * m_value + index + 5)
        result -= Fraction(4 * coefficient, index + 1)

    s_a = Fraction(0)
    s_b = Fraction(0)
    for index in range(m_value):
        s_a += Fraction(1, 4 * index + 1) - Fraction(1, 4 * index + 3)
        s_b += Fraction(1, 4 * index + 2) - Fraction(1, 4 * index + 4)
    s_a -= m_value * (
        Fraction(1, 4 * m_value + 1) - Fraction(1, 4 * m_value + 3)
    )
    s_b -= m_value * (
        Fraction(1, 4 * m_value + 2) - Fraction(1, 4 * m_value + 4)
    )
    result -= 4 * remainder_a * s_a
    result -= 4 * remainder_b * s_b

    for index, coefficient in enumerate(k_value):
        result += 16 * m_value * (m_value + 1) * coefficient * (
            Fraction(1, 4 * m_value + index)
            - Fraction(1, 4 * m_value + index + 1)
            - Fraction(1, 4 * m_value + index + 2)
            + Fraction(1, 4 * m_value + index + 3)
        )
    return result


def exact_output_row(n_value: int, m_value: int) -> dict[str, object]:
    target = math.factorial(n_value)
    real_part, imag_part = gaussian_power_w(n_value)
    remainder_a = target - real_part
    remainder_b = -imag_part
    assert remainder_a > 0
    assert remainder_a % 2 == 0

    p_zero_t: Polynomial = [
        target // math.factorial(index + 1) for index in range(n_value)
    ]
    # The q=0 member of the exact quadratic correction family.
    k_t: Polynomial = [imag_part, -remainder_a // 2]
    p_zero_x = t_to_x(p_zero_t)
    k_x = t_to_x(k_t)
    u_value: Polynomial = [1, 0, 1]

    tk = stein_x(k_x)
    g_value, remainder = divide_monic(tk, u_value)
    remainder = remainder + [0] * (2 - len(remainder))
    assert remainder == [remainder_a, remainder_b]

    p_base = poly_add(p_zero_x, k_x)
    g_zero, base_remainder = divide_monic(stein_x(p_base), u_value)
    assert base_remainder == [0]

    h_value = h_polynomial(m_value)
    p_localized = poly_add(p_zero_x, poly_multiply(h_value, k_x))
    g_localized, localized_remainder = divide_monic(stein_x(p_localized), u_value)
    assert localized_remainder == [0]
    direct_coordinate = 4 * integral_01(g_localized)
    formula_coordinate = output_formula(
        m_value,
        g_zero,
        g_value,
        remainder_a,
        remainder_b,
        k_x,
    )
    assert direct_coordinate == formula_coordinate

    degree_guard = max(len(g_zero), len(g_value) + 4, len(k_x) + 2, 5)
    predicted_primes = [
        prime
        for prime in primes_below(3 * m_value)
        if 2 * prime > 5 * m_value
        and prime < 3 * m_value
        and remainder_a % prime != 0
    ] if m_value > degree_guard else []

    denominator = direct_coordinate.denominator
    numerator = direct_coordinate.numerator
    for prime in predicted_primes:
        assert denominator % prime == 0
        assert denominator % (prime * prime) != 0
        assert numerator % prime != 0
        assert prime > 2 and prime % 2 == 1

    return {
        "N": n_value,
        "m": m_value,
        "A": remainder_a,
        "B": remainder_b,
        "correction_coefficients_t": k_t,
        "degree_guard_D": degree_guard,
        "coordinate": fraction_string(direct_coordinate),
        "numerator_digits": len(str(abs(numerator))),
        "denominator_digits": len(str(denominator)),
        "denominator_factorization": factor_integer(denominator),
        "predicted_interval_primes": predicted_primes,
        "all_predicted_primes_have_exact_denominator_valuation_one": True,
    }


def output_rows() -> tuple[list[dict[str, object]], str]:
    selected_pairs = [
        (2, 16), (2, 32), (2, 64),
        (3, 16), (3, 32), (3, 64),
        (4, 16), (4, 32), (4, 64),
        (8, 16), (8, 32), (8, 64),
        (12, 16), (12, 32), (12, 64),
    ]
    rows = [exact_output_row(n_value, m_value) for n_value, m_value in selected_pairs]
    compact = [
        [
            row["N"], row["m"], row["A"], row["B"],
            row["coordinate"], row["predicted_interval_primes"],
        ]
        for row in rows
    ]
    encoding = json.dumps(compact, separators=(",", ":")).encode()
    return rows, hashlib.sha256(encoding).hexdigest()


def main() -> None:
    started = time.perf_counter()
    dependency_checks: dict[str, dict[str, object]] = {}
    for relative_path, expected_hash in DEPENDENCIES.items():
        actual_hash = sha256(ROOT / relative_path)
        assert actual_hash == expected_hash, (
            f"dependency hash mismatch for {relative_path}: "
            f"expected {expected_hash}, got {actual_hash}"
        )
        dependency_checks[relative_path] = {
            "expected_sha256": expected_hash,
            "actual_sha256": actual_hash,
            "match": True,
        }

    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__))
    assert source_control["clean"] and script_control["clean"]

    localizer_rows, localizer_digest = localizer_identity_rows()
    order_rows, order_digest = gaussian_order_rows()
    smith_rows, smith_digest = smith_order_rows()
    coordinate_rows, coordinate_digest = output_rows()

    payload = {
        "schema": "common_kernel_integer_robin_localizer_certificate_v1",
        "logical_scope": (
            "Exact replay for an optimal integer Robin boundary layer, its "
            "Taylor-correction sign obstruction, and the unavoidable harmonic "
            "output denominator.  Finite Smith rows are diagnostic only.  The "
            "package proves no irrationality or transcendence result for e+pi."
        ),
        "all_parameter_theorem": {
            "localizer": "h_m=x^(4m)*(m+1-m*x^4)",
            "congruence": "h_m=1 mod (1+x^2)^2",
            "sharp_sup_norm": 1,
            "mass": "(8m+5)/((4m+1)(4m+5))",
            "stein_L1_bound": (
                "||T(h_m K)||_1 <= mass*(||TK||_infinity+||K||_infinity)"
            ),
            "endpoint_order_obstruction": (
                "Every integer correction K of the Taylor near-solution has "
                "ord_(x=1)(K)<N."
            ),
            "boundary_profile": (
                "m^r*(t^N+T(h_m K))(1-y/(4m)) tends to "
                "-c*(y/4)^r*exp(-y)*((r+1)*(1+y)-y^2), hence changes sign."
            ),
            "defect_remainder": (
                "A=N!-Re((1-i)^N), B=-Im((1-i)^N); A>0 for N>=2."
            ),
            "denominator_lower_bound": (
                "Every prime 5m/2<p<3m not dividing A divides the reduced "
                "output denominator once m exceeds fixed degree guards; thus "
                "log q >= (1/2+o(1))*m for fixed N,K."
            ),
            "primitive_positive_lower_bound": "3q/(N!*(degree+1)^2)",
        },
        "finite_replay": {
            "localizer_identity_range": [1, MAX_M_IDENTITY],
            "localizer_compact_sha256": localizer_digest,
            "selected_localizer_rows": localizer_rows,
            "gaussian_order_range": [1, MAX_N_ORDER],
            "gaussian_order_compact_sha256": order_digest,
            "selected_gaussian_order_rows": order_rows,
            "smith_order_range": [1, MAX_N_SMITH],
            "smith_order_compact_sha256": smith_digest,
            "smith_order_rows": smith_rows,
            "smith_scope": (
                "Finite diagnostic of maximal endpoint order only; the all-N "
                "order-N impossibility is the Gaussian proof in the source."
            ),
            "coordinate_compact_sha256": coordinate_digest,
            "coordinate_rows": coordinate_rows,
        },
        "dependency_checks": dependency_checks,
        "source_sha256": sha256(SOURCE),
        "control_audit": {"source": source_control, "script": script_control},
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "Failure guard only; it neither allocates nor limits the full "
                "approximately 50 GiB available Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: exact low-degree integer/rational arithmetic is "
                "CPU-suitable and gains nothing from floating-point GPU kernels."
            ),
        },
        "open_scope": (
            "The theorem rules out the large-m sparse localizer mechanism.  It "
            "does not rule out every moderate N-dependent correction and does "
            "not classify e+pi."
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
