#!/usr/bin/env python3
"""Replay the scalable positive CRT three-quarter cancellation theorem.

The companion source contains the all-parameter proof.  This script checks
the exact polynomial identities and the m=100,L=75 normalization instance,
including the ITEM96 residue orientation and reduced moment denominators.
Finite checks are not used to infer the asymptotic theorem.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_positive_crt_asymptotic_three_quarter_cancellation.md"
OUTPUT = ROOT / "results/common_kernel_positive_crt_asymptotic_three_quarter_certificate.json"
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_positive_crt_all_window_cancellation_hashes.sha256":
        "fd2a96672780209dcca4fd2ea4cf2d437fb491432667ed9fd32db0cc154f16b4",
}

M_VALUE = 100
L_VALUE = 75
K_VALUE = 15905
C_VALUE = 53995197867219543727
TARGET_PRIMES = [353, 359, 367, 373, 379, 383, 389, 397]
NATURAL_WINDOW_PRIMES = [347, 349, 353, 359, 367, 373, 379, 383, 389, 397]
TARGET_PRODUCT = 388885850766419537617

U = [1, 0, 1]
U_SQUARED = [1, 0, 2, 0, 1]


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


def shift(poly: list[int], amount: int) -> list[int]:
    if trim(poly) == [0]:
        return [0]
    return [0] * amount + poly


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


def primes_in_open_rational_interval(
    lower_numerator: int,
    lower_denominator: int,
    upper: int,
) -> list[int]:
    return [
        value
        for value in range(2, upper)
        if lower_denominator * value > lower_numerator and is_prime(value)
    ]


def crt_pair(left: int, left_modulus: int, right: int, prime: int) -> int:
    assert math.gcd(left_modulus, prime) == 1
    return (
        left
        + left_modulus
        * (((right - left) * pow(left_modulus, -1, prime)) % prime)
    ) % (left_modulus * prime)


def sparse_base(m_value: int) -> list[int]:
    output = [0] * (4 * m_value + 5)
    output[4 * m_value] = m_value + 1
    output[4 * m_value + 4] = -m_value
    return trim(output)


def padding_w(l_value: int) -> list[int]:
    one_minus_x_four = [1, 0, 0, 0, -1]
    one_minus_x_two = [1, 0, -1]
    return shift(
        multiply(power(one_minus_x_four, l_value), one_minus_x_two),
        4 * l_value,
    )


def closed_g(m_value: int, l_value: int, prime: int) -> tuple[int, int, int]:
    t_value = (prime - 1) // 2 - m_value - l_value
    assert 0 <= t_value <= l_value + 1
    previous = math.comb(l_value + 1, t_value - 1) if t_value else 0
    value = ((-1) ** t_value) * (
        (m_value + 1) * math.comb(l_value + 1, t_value)
        + m_value * previous
    )
    numerator = (m_value + 1) * (l_value + 2) - t_value
    assert (
        value * (l_value + 2 - t_value)
        == ((-1) ** t_value)
        * math.comb(l_value + 1, t_value)
        * numerator
    )
    k_value = 2 * m_value * l_value + 6 * m_value + 4 * l_value + 5
    assert 2 * numerator == k_value - prime
    return t_value, value, numerator


def symbolic_family_checks() -> dict[str, object]:
    rows = []
    # These finite identities check formula orientation for varied parity
    # classes only; the source proves the all-parameter result.
    for m_value, l_value in [(20, 15), (40, 30), (60, 45), (80, 60)]:
        base = sparse_base(m_value)
        r_base, remainder = divide_monic(add(base, [-1]), U)
        assert remainder == [0]
        w_poly = padding_w(l_value)
        g_poly = multiply(multiply(base, U), w_poly)
        direct = shift(
            multiply(
                [m_value + 1, 0, 0, 0, -m_value],
                power([1, 0, 0, 0, -1], l_value + 1),
            ),
            4 * (m_value + l_value),
        )
        assert g_poly == direct
        k_value = 2 * m_value * l_value + 6 * m_value + 4 * l_value + 5
        target_primes = [
            prime
            for prime in range(2 * m_value + 2 * l_value + 1, 4 * m_value)
            if is_prime(prime)
        ]
        for prime in target_primes:
            even_index = 2 * prime - 2
            odd_index = even_index + 1
            assert even_index % 4 == 0
            assert coefficient(g_poly, even_index - 1) == 0
            assert coefficient(g_poly, odd_index) == 0
            assert coefficient(g_poly, odd_index - 1) == coefficient(
                g_poly, even_index
            )
            assert coefficient(r_base, even_index) == 0
            t_value, formula, numerator = closed_g(m_value, l_value, prime)
            assert formula == coefficient(g_poly, even_index)
            assert (formula % prime == 0) == (k_value % prime == 0)
            rows.append(
                {
                    "m": m_value,
                    "L": l_value,
                    "p": prime,
                    "p_mod_4": prime % 4,
                    "t": t_value,
                    "g_mod_p": formula % prime,
                    "K_mod_p": k_value % prime,
                    "numerator_mod_p": numerator % prime,
                }
            )
    encoded = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return {
        "row_count": len(rows),
        "all_rows_sha256": hashlib.sha256(encoded).hexdigest(),
        "selected_rows": rows[:8] + rows[-8:],
        "finite_scope": (
            "Checks exact identities and both p mod 4 cases. "
            "The asymptotic quantifiers are proved in the source."
        ),
    }


def representative_instance_checks() -> dict[str, object]:
    m_value = M_VALUE
    l_value = L_VALUE
    base = sparse_base(m_value)
    assert degree(base) == 4 * m_value + 4
    assert order_at_zero(base) == 4 * m_value
    q_base, remainder = divide_monic(add(base, [-1]), U_SQUARED)
    assert remainder == [0]
    r_base, remainder = divide_monic(add(base, [-1]), U)
    assert remainder == [0]
    assert degree(r_base) == 4 * m_value + 2
    assert all(
        coefficient(r_base, index) == 0
        for index in range(1, len(r_base), 2)
    )

    w_poly = padding_w(l_value)
    assert degree(w_poly) == 8 * l_value + 2
    assert order_at_zero(w_poly) == 4 * l_value
    g_poly = multiply(multiply(base, U), w_poly)
    direct_g = shift(
        multiply(
            [m_value + 1, 0, 0, 0, -m_value],
            power([1, 0, 0, 0, -1], l_value + 1),
        ),
        4 * (m_value + l_value),
    )
    assert g_poly == direct_g

    k_value = 2 * m_value * l_value + 6 * m_value + 4 * l_value + 5
    assert k_value == K_VALUE
    top_primes = [
        prime
        for prime in range(2 * m_value + 2 * l_value + 1, 4 * m_value)
        if is_prime(prime)
    ]
    target_primes = [prime for prime in top_primes if k_value % prime]
    degenerate_primes = [prime for prime in top_primes if k_value % prime == 0]
    assert target_primes == TARGET_PRIMES
    assert not degenerate_primes
    assert math.prod(target_primes) == TARGET_PRODUCT

    crt_value = 0
    modulus = 1
    table = []
    for prime in target_primes:
        even_index = 2 * prime - 2
        odd_index = even_index + 1
        epsilon = (-1) ** ((prime + 1) // 2)
        t_value, formula_g, numerator = closed_g(m_value, l_value, prime)
        assert formula_g == coefficient(g_poly, even_index)
        assert formula_g % prime
        assert coefficient(g_poly, even_index - 1) == 0
        assert coefficient(g_poly, odd_index) == 0
        assert coefficient(g_poly, odd_index - 1) == formula_g
        assert coefficient(r_base, even_index) == 0
        target = (2 * epsilon * pow(formula_g, -1, prime)) % prime
        crt_value = crt_pair(crt_value, modulus, target, prime)
        modulus *= prime
        table.append(
            {
                "p": prime,
                "p_mod_4": prime % 4,
                "E": even_index,
                "O": odd_index,
                "t": t_value,
                "g_mod_p": formula_g % prime,
                "K_mod_p": k_value % prime,
                "numerator_mod_p": numerator % prime,
                "epsilon": epsilon,
                "target_2epsilon_over_g_mod_p": target,
            }
        )
    assert modulus == TARGET_PRODUCT
    assert crt_value == C_VALUE
    assert 0 < crt_value < modulus

    capacity = 4 ** (l_value - 1)
    assert crt_value < capacity
    x_w = shift(w_poly, 1)
    correction_factor = add(
        [1],
        scale(multiply(U_SQUARED, x_w), -crt_value),
    )
    h_poly = multiply(base, correction_factor)
    expected_n = 4 * m_value
    expected_d = 4 * m_value + 8 * l_value + 11
    assert expected_n == 400
    assert expected_d == 1011
    assert order_at_zero(h_poly) == expected_n
    assert degree(h_poly) == expected_d
    q_poly, remainder = divide_monic(add(h_poly, [-1]), U_SQUARED)
    assert remainder == [0]
    r_poly, remainder = divide_monic(add(h_poly, [-1]), U)
    assert remainder == [0]
    formula_r = add(r_base, scale(shift(g_poly, 1), -crt_value))
    assert r_poly == formula_r

    natural_primes = primes_in_open_rational_interval(expected_d, 3, expected_n)
    assert natural_primes == NATURAL_WINDOW_PRIMES
    assert set(target_primes).issubset(natural_primes)
    assert 3 * (2 * m_value + 2 * l_value) > expected_d

    residue_rows = []
    for prime in target_primes:
        i_zero_residue = (
            2 * coefficient(r_poly, prime - 1)
            + coefficient(r_poly, 2 * prime - 1)
        ) % prime
        i_one_residue = coefficient(r_poly, 2 * prime - 2) % prime
        assert i_zero_residue == 0
        assert i_one_residue == 0
        residue_rows.append(
            {
                "p": prime,
                "2r_pminus1_plus_r_2pminus1_mod_p": i_zero_residue,
                "r_2pminus2_mod_p": i_one_residue,
            }
        )

    i_zero = integral(r_poly)
    i_one = integral(r_poly, 2)
    common_denominator = math.lcm(i_zero.denominator, i_one.denominator)
    assert math.gcd(common_denominator, TARGET_PRODUCT) == 1

    return {
        "parameters": {
            "m": m_value,
            "L": l_value,
            "lambda": "3/4",
            "K": k_value,
            "c": crt_value,
            "n": expected_n,
            "d": expected_d,
        },
        "top_interval_primes": top_primes,
        "degenerate_primes_dividing_K": degenerate_primes,
        "target_primes": target_primes,
        "target_product": TARGET_PRODUCT,
        "natural_window_primes": natural_primes,
        "crt_table": table,
        "positivity_capacity": {
            "c": crt_value,
            "four_to_L_minus_1": capacity,
            "margin": capacity - crt_value,
            "exact_bound": "c*u^2*x*w<=4*c*4^(-L)<=1",
        },
        "item96_residue_rows": residue_rows,
        "reduced_moments": {
            "I0_numerator_bits": abs(i_zero.numerator).bit_length(),
            "I0_denominator_bits": i_zero.denominator.bit_length(),
            "I1_numerator_bits": abs(i_one.numerator).bit_length(),
            "I1_denominator_bits": i_one.denominator.bit_length(),
            "common_denominator_bits": common_denominator.bit_length(),
            "I0_sha256": fraction_digest(i_zero),
            "I1_sha256": fraction_digest(i_one),
            "gcd_common_denominator_target_product": math.gcd(
                common_denominator, TARGET_PRODUCT
            ),
            "common_denominator_mod_target_primes": [
                {"p": prime, "residue": common_denominator % prime}
                for prime in target_primes
            ],
        },
        "polynomial_hashes": {
            "B_m": polynomial_digest(base),
            "base_q": polynomial_digest(q_base),
            "R_m": polynomial_digest(r_base),
            "w_L": polynomial_digest(w_poly),
            "G_m": polynomial_digest(g_poly),
            "correction_factor": polynomial_digest(correction_factor),
            "h_m": polynomial_digest(h_poly),
            "q_m": polynomial_digest(q_poly),
            "r_m": polynomial_digest(r_poly),
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

    lambda_zero = 2.0 / (2.0 + math.log(4.0))
    delta_three_quarters = 0.75 * math.log(4.0) - 0.5
    assert 0.5 < lambda_zero < 0.75 < 1.0
    assert delta_three_quarters > 0

    payload = {
        "schema": "common_kernel_positive_crt_asymptotic_three_quarter_certificate_v1",
        "logical_scope": (
            "Replay of an unconditional asymptotic construction cancelling "
            "three quarters of the d/3<p<n Chebyshev mass from both isolated "
            "moment denominators. It does not control the bottom quarter, the "
            "full correction output, or classify e+pi."
        ),
        "all_parameter_theorem": {
            "lambda_range": "2/(2+log(4))<lambda<1",
            "lambda0_float": lambda_zero,
            "L": "floor(lambda*m)",
            "target_set": (
                "primes 2m+2L<p<4m which do not divide "
                "K=2mL+6m+4L+5"
            ),
            "determinant": (
                "The ITEM96 matrix is diag(g_p,g_p), and g_p=0 mod p "
                "iff p divides K."
            ),
            "CRT": (
                "c=2*epsilon/g_p mod p; its least nonnegative CRT "
                "representative satisfies c<P and eventually c<=4^(L-1)."
            ),
            "cancelled_mass": "2*(1-lambda)*m+o(m)",
            "full_window_mass": "(8/3)*(1-lambda)*m+o(m)",
            "cancelled_fraction": "3/4",
            "proof_location": "Sections 2--8 of the companion source.",
        },
        "symbolic_identity_checks": symbolic_family_checks(),
        "representative_m100_L75_instance": representative_instance_checks(),
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
        "remaining_scope": (
            "The bottom quarter of the one-third window and the full correction "
            "channel remain uncontrolled."
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
