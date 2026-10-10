#!/usr/bin/env python3
"""Replay the positive two-moment one-third-window counterexample.

The companion source proves the all-parameter residue criterion and the
interval positivity.  This script recomputes every polynomial coefficient
and rational moment exactly.  It makes no inference from a finite scan.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_nonsymmetric_two_moment_residue_counterexample.md"
OUTPUT = ROOT / "results/common_kernel_nonsymmetric_two_moment_residue_certificate.json"
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_even_nonlocal_moment_denominator_hashes.sha256":
        "bc6aae22ca67cb7e04678432e3befdd33b7072ab3cc67b1d656134fd7e0a1806",
}

U = [1, 0, 1]
U_SQUARED = [1, 0, 2, 0, 1]
A = [0, 0, 0, 0, 2, 0, 0, 0, -1]
B = [1, 0, 0, -1, 2, -3, 4, -3, 2, -1]
H = [0, 0, 1, -4, 7, -8, 7, -4, 2]


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


def counterexample_checks() -> dict[str, object]:
    # A-1 = -u^2(1-x^2)^2.
    assert add(A, [-1]) == scale(
        multiply(U_SQUARED, [1, 0, -2, 0, 1]), -1
    )

    # B-1 = -u^2*x^3*(1-x)^2.
    x_cubed_one_minus_x_squared = shift([1, -2, 1], 3)
    assert add(B, [-1]) == scale(
        multiply(U_SQUARED, x_cubed_one_minus_x_squared), -1
    )

    h_poly = multiply(power(A, 6), power(B, 2))
    assert order_at_zero(h_poly) == 24
    assert degree(h_poly) == 66
    q_poly, remainder = divide_monic(add(h_poly, [-1]), U_SQUARED)
    assert remainder == [0]
    r_poly, remainder = divide_monic(add(h_poly, [-1]), U)
    assert remainder == [0]
    assert r_poly == multiply(U, q_poly)
    assert degree(r_poly) == 64

    n_value = order_at_zero(h_poly)
    for index in range(n_value):
        expected = 0 if index % 2 else (-1) ** (index // 2 + 1)
        assert coefficient(r_poly, index) == expected

    prime = 23
    assert is_prime(prime)
    assert 3 * prime > degree(h_poly)
    assert prime < order_at_zero(h_poly)
    relevant = {
        "r_22": coefficient(r_poly, 22),
        "r_44": coefficient(r_poly, 44),
        "r_45": coefficient(r_poly, 45),
    }
    assert relevant == {"r_22": 1, "r_44": 3887, "r_45": -1520}
    i_zero_residue = (
        2 * coefficient(r_poly, prime - 1)
        + coefficient(r_poly, 2 * prime - 1)
    ) % prime
    i_one_residue = coefficient(r_poly, 2 * prime - 2) % prime
    assert i_zero_residue == 0
    assert i_one_residue == 0
    assert 2 * relevant["r_22"] + relevant["r_45"] == -66 * prime
    assert relevant["r_44"] == 169 * prime

    i_zero = integral(r_poly)
    i_one = integral(r_poly, 2)
    expected_i_zero = Fraction(
        -9392594521692168961341691,
        12850727001117633342514800,
    )
    expected_i_one = Fraction(
        -1690320846078465619890203,
        5711434222718948152228800,
    )
    assert i_zero == expected_i_zero
    assert i_one == expected_i_one
    assert i_zero.denominator % prime == 22
    assert i_one.denominator % prime == 20
    common_denominator = math.lcm(i_zero.denominator, i_one.denominator)
    assert common_denominator % prime != 0

    return {
        "A_coefficients": A,
        "B_coefficients": B,
        "h_degree": degree(h_poly),
        "h_order_at_zero": order_at_zero(h_poly),
        "prime": prime,
        "three_p_minus_d": 3 * prime - degree(h_poly),
        "n_minus_p": order_at_zero(h_poly) - prime,
        "relevant_r_coefficients": relevant,
        "I0_residue_numerator_mod_p": i_zero_residue,
        "I1_residue_numerator_mod_p": i_one_residue,
        "I0": str(i_zero),
        "I1": str(i_one),
        "I0_denominator_mod_p": i_zero.denominator % prime,
        "I1_denominator_mod_p": i_one.denominator % prime,
        "common_denominator_mod_p": common_denominator % prime,
        "h_sha256": polynomial_digest(h_poly),
        "q_sha256": polynomial_digest(q_poly),
        "r_sha256": polynomial_digest(r_poly),
        "I0_sha256": fraction_digest(i_zero),
        "I1_sha256": fraction_digest(i_one),
        "positivity_proof_data": {
            "A_identity": "A=1-(1-x^4)^2",
            "B_identity": "B=1-(1+x^2)^2*x^3*(1-x)^2",
            "bound": (
                "0<=x^3(1-x)^2<=x(1-x)<=1/4 and "
                "(1+x^2)^2<=4 on [0,1]"
            ),
        },
    }


def ratio_four_checks() -> dict[str, object]:
    q_h, remainder = divide_monic(add(H, [-1]), U_SQUARED)
    assert remainder == [0]
    assert order_at_zero(H) == 2
    assert degree(H) == 8

    selected = {1, 2, 3, 5, 10, 20, 40, 80, 120}
    rows = []
    all_rows = []
    h_power = [1]
    for exponent in range(1, 121):
        h_power = multiply(h_power, H)
        n_value = order_at_zero(h_power)
        d_value = degree(h_power)
        assert n_value == 2 * exponent
        assert d_value == 8 * exponent
        assert d_value > 3 * n_value
        quotient, remainder = divide_monic(add(h_power, [-1]), U_SQUARED)
        assert remainder == [0]
        row = {
            "k": exponent,
            "n": n_value,
            "d": d_value,
            "d_minus_3n": d_value - 3 * n_value,
            "h_sha256": polynomial_digest(h_power),
            "q_sha256": polynomial_digest(quotient),
        }
        all_rows.append(row)
        if exponent in selected:
            rows.append(row)
    encoded = json.dumps(all_rows, sort_keys=True, separators=(",", ":")).encode()
    return {
        "H_coefficients": H,
        "H_q_coefficients": q_h,
        "k_range": [1, 120],
        "all_rows_sha256": hashlib.sha256(encoded).hexdigest(),
        "selected_rows": rows,
        "all_parameter_reason": (
            "The nonzero lowest and highest coefficients give n=2k,d=8k "
            "for every k>=1, hence d/3>n and the tested prime window is empty."
        ),
        "finite_scope": (
            "The row hashes check normalization only; emptiness of the window "
            "is the symbolic degree/order identity."
        ),
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
        "schema": "common_kernel_nonsymmetric_two_moment_residue_certificate_v1",
        "logical_scope": (
            "Exact positive counterexample to prime-by-prime one-third-window "
            "survival for the two isolated moments. It does not disprove an "
            "aggregate surviving-prime bound, a third-channel theorem, or any "
            "classification of e+pi."
        ),
        "all_parameter_residue_criterion": {
            "hypotheses": "odd p with d/3<p<n",
            "I0": (
                "I0 is p-integral iff 2*r_(p-1)+r_(2p-1)=0 mod p; "
                "r_(p-1)=(-1)^((p+1)/2)."
            ),
            "I1": (
                "I1 is p-integral iff r_(2p-2)=0 mod p because "
                "the forced coefficient r_(p-2) vanishes."
            ),
            "proof_location": "Section 3 of the companion source.",
        },
        "positive_counterexample": counterexample_checks(),
        "ratio_four_H_power_checks": ratio_four_checks(),
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
                "Not used: the replay is small exact integer/rational arithmetic."
            ),
        },
        "missing_lemma": (
            "An aggregate bound on primes for which both high-coefficient "
            "congruences cancel, or a further output channel which recovers them."
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
