#!/usr/bin/env python3
"""Replay the positive integer CRT cancellation of a full prime window.

The companion source proves the conditional CRT lemma and positivity.
This script reconstructs the degree-1075 example with exact arithmetic,
checks the solution orientation against the two ITEM96 residues, and
reduces both moments.  It makes no asymptotic inference from the example.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_positive_crt_all_window_cancellation_barrier.md"
OUTPUT = ROOT / "results/common_kernel_positive_crt_all_window_cancellation_certificate.json"
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_nonsymmetric_two_moment_residue_hashes.sha256":
        "14edc755bb18e6726f6e1e5f6006afcc76950e2d3206dd3d2b942e10ee471081",
}

M_VALUE = 115
L_VALUE = 75
C_ZERO = 139574584508098815002244647712452355913710915
C_ONE = 92665357687907045832657432294875741514399515
EXPECTED_PRIMES = [
    359, 367, 373, 379, 383, 389, 397, 401, 409,
    419, 421, 431, 433, 439, 443, 449, 457,
]
EXPECTED_PRODUCT = 237359812447644832129693355690076072498951997

U = [1, 0, 1]
U_SQUARED = [1, 0, 2, 0, 1]
A = [0, 0, 0, 0, 2, 0, 0, 0, -1]


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


def trim(poly: list[int]) -> list[int]:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [0]


def degree(poly: list[int]) -> int:
    normalized = trim(poly)
    return -1 if normalized == [0] else len(normalized) - 1


def coefficient(poly: list[int], index: int) -> int:
    if index < 0 or index >= len(poly):
        return 0
    return poly[index]


def order_at_zero(poly: list[int]) -> int:
    for index, value in enumerate(poly):
        if value:
            return index
    raise ValueError("zero polynomial has infinite order")


def add(*polynomials: list[int]) -> list[int]:
    size = max((len(poly) for poly in polynomials), default=1)
    output = [0] * size
    for poly in polynomials:
        for index, value in enumerate(poly):
            output[index] += value
    return trim(output)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        if not left_value:
            continue
        for right_index, right_value in enumerate(right):
            if right_value:
                output[left_index + right_index] += left_value * right_value
    return trim(output)


def power(poly: list[int], exponent: int) -> list[int]:
    assert exponent >= 0
    result = [1]
    base = trim(poly)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, base)
        remaining >>= 1
        if remaining:
            base = multiply(base, base)
    return result


def divide_monic(
    numerator: list[int], denominator: list[int]
) -> tuple[list[int], list[int]]:
    denominator = trim(denominator)
    remainder = trim(numerator)
    assert denominator[-1] == 1
    if len(remainder) < len(denominator):
        return [0], remainder
    quotient = [0] * (len(remainder) - len(denominator) + 1)
    while remainder != [0] and len(remainder) >= len(denominator):
        offset = len(remainder) - len(denominator)
        leading = remainder[-1]
        quotient[offset] += leading
        subtraction = [0] * offset + [leading * value for value in denominator]
        remainder = add(remainder, scale(subtraction, -1))
    return trim(quotient), trim(remainder)


def integral(poly: list[int], denominator_shift: int = 1) -> Fraction:
    return sum(
        (
            Fraction(value, index + denominator_shift)
            for index, value in enumerate(poly)
        ),
        Fraction(0),
    )


def polynomial_digest(poly: list[int]) -> str:
    digest = hashlib.sha256()
    for index, value in enumerate(trim(poly)):
        digest.update(f"{index}:{value};".encode())
    return digest.hexdigest()


def fraction_digest(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode()
    ).hexdigest()


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def primes_in_open_interval(lower_numerator: int, lower_denominator: int, upper: int) -> list[int]:
    return [
        value
        for value in range(2, upper)
        if lower_denominator * value > lower_numerator and is_prime(value)
    ]


def solve_two_by_two(
    matrix: tuple[int, int, int, int],
    rhs: tuple[int, int],
    prime: int,
) -> tuple[tuple[int, int], int]:
    a_value, b_value, c_value, d_value = matrix
    e_value, f_value = rhs
    determinant = (a_value * d_value - b_value * c_value) % prime
    assert determinant
    inverse = pow(determinant, -1, prime)
    solution = (
        ((e_value * d_value - b_value * f_value) * inverse) % prime,
        ((a_value * f_value - e_value * c_value) * inverse) % prime,
    )
    assert (a_value * solution[0] + b_value * solution[1] - e_value) % prime == 0
    assert (c_value * solution[0] + d_value * solution[1] - f_value) % prime == 0
    return solution, determinant


def crt_pair(left: int, left_modulus: int, right: int, prime: int) -> int:
    assert math.gcd(left_modulus, prime) == 1
    return (
        left
        + left_modulus
        * (((right - left) * pow(left_modulus, -1, prime)) % prime)
    ) % (left_modulus * prime)


def construction_checks() -> dict[str, object]:
    assert add(A, [-1]) == scale(
        multiply(U_SQUARED, [1, 0, -2, 0, 1]), -1
    )
    a_power = power(A, M_VALUE)
    r_base, remainder = divide_monic(add(a_power, [-1]), U)
    assert remainder == [0]
    assert all(
        coefficient(r_base, index) == 0
        for index in range(1, len(r_base), 2)
    )

    padding = [0] * L_VALUE + [
        ((-1) ** index) * math.comb(L_VALUE, index)
        for index in range(L_VALUE + 1)
    ]
    assert degree(padding) == 2 * L_VALUE
    assert order_at_zero(padding) == L_VALUE
    g_poly = multiply(multiply(a_power, U), padding)

    expected_d = 8 * M_VALUE + 2 * L_VALUE + 5
    expected_n = 4 * M_VALUE
    primes = primes_in_open_interval(expected_d, 3, expected_n)
    assert primes == EXPECTED_PRIMES
    assert math.prod(primes) == EXPECTED_PRODUCT

    table = []
    solutions = []
    for prime in primes:
        even_index = 2 * prime - 2
        odd_index = 2 * prime - 1
        epsilon = (-1) ** ((prime + 1) // 2)
        matrix = (
            coefficient(g_poly, even_index) % prime,
            coefficient(g_poly, even_index - 1) % prime,
            coefficient(g_poly, odd_index) % prime,
            coefficient(g_poly, odd_index - 1) % prime,
        )
        rhs = (
            coefficient(r_base, even_index) % prime,
            (2 * epsilon) % prime,
        )
        solution, determinant = solve_two_by_two(matrix, rhs, prime)
        assert solution == (C_ZERO % prime, C_ONE % prime)
        solutions.append((prime, solution))
        table.append(
            {
                "p": prime,
                "E": even_index,
                "O": odd_index,
                "epsilon": epsilon,
                "matrix_row_major_mod_p": list(matrix),
                "rhs_mod_p": list(rhs),
                "determinant_mod_p": determinant,
                "c0_mod_p": solution[0],
                "c1_mod_p": solution[1],
            }
        )

    crt_zero = 0
    crt_one = 0
    modulus = 1
    for prime, solution in solutions:
        crt_zero = crt_pair(crt_zero, modulus, solution[0], prime)
        crt_one = crt_pair(crt_one, modulus, solution[1], prime)
        modulus *= prime
    assert modulus == EXPECTED_PRODUCT
    assert crt_zero == C_ZERO
    assert crt_one == C_ONE
    assert 0 <= C_ZERO < modulus
    assert 0 <= C_ONE < modulus

    capacity = 4 ** (L_VALUE - 1)
    capacity_margin = capacity - C_ZERO - C_ONE
    assert capacity_margin > 0

    s_poly = multiply(padding, [C_ZERO, C_ONE])
    c_poly = add([1], scale(multiply(U_SQUARED, s_poly), -1))
    h_poly = multiply(a_power, c_poly)
    assert order_at_zero(h_poly) == expected_n
    assert degree(h_poly) == expected_d
    q_poly, remainder = divide_monic(add(h_poly, [-1]), U_SQUARED)
    assert remainder == [0]
    r_poly, remainder = divide_monic(add(h_poly, [-1]), U)
    assert remainder == [0]
    formula_r = add(r_base, scale(multiply(g_poly, [C_ZERO, C_ONE]), -1))
    assert r_poly == formula_r

    residue_rows = []
    for prime in primes:
        item96_i_zero = (
            2 * coefficient(r_poly, prime - 1)
            + coefficient(r_poly, 2 * prime - 1)
        ) % prime
        item96_i_one = coefficient(r_poly, 2 * prime - 2) % prime
        assert item96_i_zero == 0
        assert item96_i_one == 0
        residue_rows.append(
            {
                "p": prime,
                "2r_pminus1_plus_r_2pminus1_mod_p": item96_i_zero,
                "r_2pminus2_mod_p": item96_i_one,
            }
        )

    i_zero = integral(r_poly)
    i_one = integral(r_poly, 2)
    common_denominator = math.lcm(i_zero.denominator, i_one.denominator)
    denominator_residues = [
        {"p": prime, "common_denominator_mod_p": common_denominator % prime}
        for prime in primes
    ]
    assert all(row["common_denominator_mod_p"] for row in denominator_residues)
    assert math.gcd(common_denominator, EXPECTED_PRODUCT) == 1

    return {
        "parameters": {
            "m": M_VALUE,
            "L": L_VALUE,
            "c0": C_ZERO,
            "c1": C_ONE,
            "n": expected_n,
            "d": expected_d,
        },
        "window_primes": primes,
        "window_prime_count": len(primes),
        "window_product": EXPECTED_PRODUCT,
        "window_log_product_float": sum(math.log(prime) for prime in primes),
        "crt_table": table,
        "crt_reconstruction": {
            "modulus": modulus,
            "least_nonnegative_c0": crt_zero,
            "least_nonnegative_c1": crt_one,
        },
        "positivity_capacity": {
            "c0_plus_c1": C_ZERO + C_ONE,
            "four_to_L_minus_1": capacity,
            "margin": capacity_margin,
            "exact_bound": (
                "u^2*x^L*(1-x)^L*(c0+c1*x) "
                "<=4*4^(-L)*(c0+c1)<=1"
            ),
        },
        "item96_residue_orientation": {
            "I0": "2*r_(p-1)+r_(2p-1)",
            "I1": "r_(2p-2)",
            "rows": residue_rows,
        },
        "reduced_moments": {
            "I0_numerator_bits": abs(i_zero.numerator).bit_length(),
            "I0_denominator_bits": i_zero.denominator.bit_length(),
            "I1_numerator_bits": abs(i_one.numerator).bit_length(),
            "I1_denominator_bits": i_one.denominator.bit_length(),
            "common_denominator_bits": common_denominator.bit_length(),
            "I0_sha256": fraction_digest(i_zero),
            "I1_sha256": fraction_digest(i_one),
            "common_denominator_mod_primes": denominator_residues,
            "gcd_common_denominator_window_product": math.gcd(
                common_denominator, EXPECTED_PRODUCT
            ),
        },
        "polynomial_hashes": {
            "A_m": polynomial_digest(a_power),
            "R_m": polynomial_digest(r_base),
            "w_L": polynomial_digest(padding),
            "G_m_L": polynomial_digest(g_poly),
            "s": polynomial_digest(s_poly),
            "C": polynomial_digest(c_poly),
            "h": polynomial_digest(h_poly),
            "r": polynomial_digest(r_poly),
            "q": polynomial_digest(q_poly),
        },
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

    payload = {
        "schema": "common_kernel_positive_crt_all_window_cancellation_certificate_v1",
        "logical_scope": (
            "Exact positive integral cancellation of every prime in one "
            "17-prime d/3<p<n window. This is a finite aggregate barrier, "
            "not an infinite positive-density construction, an asymptotic "
            "impossibility theorem, or an e+pi classification."
        ),
        "conditional_all_parameter_lemma": {
            "matrix_orientation": (
                "Rows extract degrees E=2p-2 and O=2p-1 from "
                "G=A_m*u*x^L*(1-x)^L; RHS is (R_E,2*epsilon)."
            ),
            "identity": "r=R-G*(c0+c1*x)",
            "item96_target": (
                "r_E=0 and r_O=-2*epsilon, hence both ITEM96 residues vanish."
            ),
            "positivity": (
                "Nonnegative integer CRT representatives obeying "
                "c0+c1<=4^(L-1) give 0<=1-u^2*w*(c0+c1*x)<=1."
            ),
        },
        "explicit_construction": construction_checks(),
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
                "Not used: the replay is exact integer/rational arithmetic."
            ),
        },
        "missing_lemma": (
            "An asymptotic restriction on CRT matrix nonvanishing or least "
            "representatives versus padding degree, or a further output "
            "channel which recovers the cancelled window product."
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
