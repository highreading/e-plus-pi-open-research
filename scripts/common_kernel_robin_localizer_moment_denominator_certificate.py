#!/usr/bin/env python3
"""Replay the exact Robin-localizer prime-window denominator theorem.

The all-parameter proofs are in the companion source.  This script checks
the polynomial identities, isolated and full-output prime valuations, the
sparse h_m family, the Taylor correction, and the signed scope witness.
It does not infer an e+pi classification from finite data.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_robin_localizer_moment_denominator_barrier.md"
OUTPUT = ROOT / "results/common_kernel_robin_localizer_moment_denominator_certificate.json"
RSS_GUARD_KIB = 8 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_stein_robin_quadratic_correction_hashes.sha256":
        "208982ad388c02ba42c79726b6eaefa8acd1ed7d5a2fad6de5c138a44483038a",
}

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


def order_at_zero(poly: list[int]) -> int:
    for index, value in enumerate(poly):
        if value:
            return index
    return math.inf  # type: ignore[return-value]


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
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return trim(output)


def shift(poly: list[int], amount: int) -> list[int]:
    if trim(poly) == [0]:
        return [0]
    return [0] * amount + poly


def derivative(poly: list[int]) -> list[int]:
    if len(poly) <= 1:
        return [0]
    return trim([index * poly[index] for index in range(1, len(poly))])


def stein(poly: list[int]) -> list[int]:
    deriv = derivative(poly)
    return add(deriv, scale(shift(deriv, 1), -1), scale(shift(poly, 1), -1))


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
        remainder = add(
            remainder,
            scale([0] * offset + [leading * value for value in denominator], -1),
        )
    return trim(quotient), trim(remainder)


def substitute_one_minus_x(poly: list[int]) -> list[int]:
    output = [0]
    for power, coefficient in enumerate(poly):
        term = [
            coefficient * math.comb(power, index) * ((-1) ** index)
            for index in range(power + 1)
        ]
        output = add(output, term)
    return output


def evaluate_fraction(poly: list[int], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def evaluate_integer(poly: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def derivative_value(poly: list[int], order: int, value: int) -> int:
    current = poly[:]
    for _ in range(order):
        current = derivative(current)
    return evaluate_integer(current, value)


def integral(poly: list[int], shift_denominator: int = 1) -> Fraction:
    return sum(
        (
            Fraction(coefficient, index + shift_denominator)
            for index, coefficient in enumerate(poly)
        ),
        Fraction(0),
    )


def polynomial_digest(poly: list[int]) -> str:
    digest = hashlib.sha256()
    for index, value in enumerate(trim(poly)):
        digest.update(f"{index}:{value};".encode())
    return digest.hexdigest()


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if not sieve[prime]:
            continue
        start = prime * prime
        sieve[start : limit + 1 : prime] = b"\x00" * (
            (limit - start) // prime + 1
        )
    return [index for index, flag in enumerate(sieve) if flag]


def gaussian_power_w(exponent: int) -> tuple[int, int]:
    real, imag = 1, 0
    for _ in range(exponent):
        real, imag = real + imag, imag - real
    return real, imag


def h_sparse(m_value: int) -> list[int]:
    assert m_value >= 1
    output = [0] * (4 * m_value + 5)
    output[4 * m_value] = m_value + 1
    output[4 * m_value + 4] = -m_value
    return trim(output)


def q_sparse(m_value: int) -> list[int]:
    # -(x^2-1)^2 * sum_(j=0)^(m-1) (j+1)x^(4j)
    summation = [0] * (4 * (m_value - 1) + 1)
    for index in range(m_value):
        summation[4 * index] = index + 1
    return scale(multiply([1, 0, -2, 0, 1], summation), -1)


def quotient_data(
    h_poly: list[int], k_poly: list[int]
) -> dict[str, object]:
    tk = stein(k_poly)
    g_poly, remainder = divide_monic(tk, U)
    padded_remainder = remainder + [0] * (2 - len(remainder))
    alpha = padded_remainder[0]
    beta = padded_remainder[1]

    q_poly, h_remainder = divide_monic(add(h_poly, [-1]), U_SQUARED)
    assert h_remainder == [0]
    r_poly = multiply(U, q_poly)
    h_prime_over_u, derivative_remainder = divide_monic(derivative(h_poly), U)
    assert derivative_remainder == [0]

    formula = add(
        multiply(add(h_poly, [-1]), g_poly),
        multiply(r_poly, [alpha, beta]),
        multiply([1, -1], multiply(h_prime_over_u, k_poly)),
    )
    direct, direct_remainder = divide_monic(
        add(stein(multiply(h_poly, k_poly)), scale(tk, -1)), U
    )
    assert direct_remainder == [0]
    assert direct == formula

    return {
        "tk": tk,
        "G": g_poly,
        "alpha": alpha,
        "beta": beta,
        "q": q_poly,
        "r": r_poly,
        "h_prime_over_u": h_prime_over_u,
        "S": direct,
    }


def verify_prime_window(
    h_poly: list[int], k_poly: list[int], base_denominator: int = 1
) -> dict[str, object]:
    data = quotient_data(h_poly, k_poly)
    g_poly = data["G"]
    alpha = int(data["alpha"])
    r_poly = data["r"]
    s_poly = data["S"]
    assert isinstance(g_poly, list) and isinstance(r_poly, list)
    assert isinstance(s_poly, list)

    n_value = order_at_zero(h_poly)
    d_value = degree(h_poly)
    e_value = degree(s_poly)
    assert isinstance(n_value, int)
    g_degree = degree(g_poly)

    # Forced alternating quotient prefix.
    for index in range(n_value):
        expected = 0 if index % 2 else (-1) ** (index // 2 + 1)
        actual = r_poly[index] if index < len(r_poly) else 0
        assert actual == expected

    i_zero = integral(r_poly)
    i_one = integral(r_poly, 2)
    isolated_moment_primes = [
        prime
        for prime in primes_up_to(n_value)
        if prime > d_value / 2
    ]
    for prime in isolated_moment_primes:
        assert i_zero.denominator % prime == 0
        assert i_zero.denominator % (prime * prime) != 0
        assert i_one.denominator % prime != 0

    full_primes = [
        prime
        for prime in primes_up_to(max(n_value - 1, 1))
        if prime > (e_value + 1) / 2
        and prime - 1 > g_degree
        and prime < n_value
        and alpha % prime != 0
    ]
    s_integral = 4 * integral(s_poly)
    for prime in full_primes:
        coefficient = s_poly[prime - 1]
        r_sign = r_poly[prime - 1]
        assert r_sign in (-1, 1)
        assert coefficient == alpha * r_sign
        assert s_integral.denominator % prime == 0
        assert s_integral.denominator % (prime * prime) != 0

    product = math.prod(full_primes)
    assert s_integral.denominator % product == 0

    base_coordinate = Fraction(7, base_denominator)
    total_coordinate = base_coordinate + k_poly[0] + s_integral
    persistent_primes = [
        prime for prime in full_primes if base_denominator % prime != 0
    ]
    persistent_product = math.prod(persistent_primes)
    assert total_coordinate.denominator % persistent_product == 0

    # Endpoint jet retention.
    k_t = substitute_one_minus_x(k_poly)
    endpoint_order = order_at_zero(k_t)
    assert isinstance(endpoint_order, int)
    correction = stein(multiply(h_poly, k_poly))
    actual_jet = derivative_value(correction, endpoint_order, 1)
    expected_jet = -(
        (endpoint_order + 1)
        * derivative_value(k_poly, endpoint_order, 1)
    )
    assert actual_jet == expected_jet != 0

    return {
        "n": n_value,
        "d": d_value,
        "e": e_value,
        "deg_G": g_degree,
        "alpha": alpha,
        "beta": data["beta"],
        "I0_numerator": i_zero.numerator,
        "I0_denominator": i_zero.denominator,
        "I1_numerator": i_one.numerator,
        "I1_denominator": i_one.denominator,
        "isolated_moment_primes": isolated_moment_primes,
        "full_output_primes": full_primes,
        "full_prime_product": product,
        "output_shift_numerator": s_integral.numerator,
        "output_shift_denominator": s_integral.denominator,
        "base_denominator": base_denominator,
        "persistent_prime_product": persistent_product,
        "endpoint_order": endpoint_order,
        "endpoint_jet": actual_jet,
        "h_sha256": polynomial_digest(h_poly),
        "S_sha256": polynomial_digest(s_poly),
    }


def sparse_family_checks() -> dict[str, object]:
    records = []
    checks = 0
    selected = {1, 2, 3, 5, 10, 20, 40, 60, 80, 100}
    for m_value in range(1, 101):
        h_poly = h_sparse(m_value)
        q_poly = q_sparse(m_value)
        assert add([1], multiply(U_SQUARED, q_poly)) == h_poly
        assert order_at_zero(h_poly) == 4 * m_value
        assert degree(h_poly) == 4 * m_value + 4
        assert evaluate_integer(h_poly, 1) == 1
        assert derivative_value(h_poly, 1, 1) == 0
        expected_integral = Fraction(
            8 * m_value + 5,
            (4 * m_value + 1) * (4 * m_value + 5),
        )
        assert integral(h_poly) == expected_integral
        weighted_derivative_integral = integral(
            multiply([1, -1], derivative(h_poly))
        )
        assert weighted_derivative_integral == expected_integral

        # Monotonicity is certified by the exact factorization
        # h'=4m(m+1)x^(4m-1)(1-x^4).
        expected_derivative = scale(
            shift([1, 0, 0, 0, -1], 4 * m_value - 1),
            4 * m_value * (m_value + 1),
        )
        assert derivative(h_poly) == expected_derivative
        for grid_index in range(101):
            value = evaluate_fraction(h_poly, Fraction(grid_index, 100))
            assert 0 <= value <= 1
        checks += 1
        if m_value in selected:
            records.append(
                {
                    "m": m_value,
                    "n": 4 * m_value,
                    "d": 4 * m_value + 4,
                    "integral": str(expected_integral),
                    "q_sha256": polynomial_digest(q_poly),
                    "h_sha256": polynomial_digest(h_poly),
                }
            )
    return {"checks": checks, "selected_records": records}


def signed_scope_witness() -> dict[str, object]:
    q_poly = [-1, 117, -795, 1687, -1230, 0, 222]
    h_poly = add([1], multiply(U_SQUARED, q_poly))
    expected_h = [
        0,
        117,
        -797,
        1921,
        -2821,
        3491,
        -3033,
        1687,
        -786,
        0,
        222,
    ]
    assert h_poly == expected_h
    assert evaluate_integer(q_poly, 1) == 0
    assert derivative_value(q_poly, 1, 1) == 0
    assert evaluate_integer(h_poly, 0) == 0
    assert evaluate_integer(h_poly, 1) == 1
    assert derivative_value(h_poly, 1, 1) == 0
    i_zero = integral(multiply(U, q_poly))
    i_one = integral(multiply(U, q_poly), 2)
    assert i_zero == i_one == 0
    half_value = evaluate_fraction(h_poly, Fraction(1, 2))
    assert half_value == Fraction(-2513, 512)
    return {
        "q_coefficients": q_poly,
        "h_coefficients": h_poly,
        "I0": str(i_zero),
        "I1": str(i_one),
        "h_at_one_half": str(half_value),
        "sign_control_fails": True,
    }


def taylor_correction_checks() -> dict[str, object]:
    rows = []
    row_digests = []
    selected_n = {2, 3, 4, 5, 6, 8, 10, 16, 24, 32, 40}
    for n_value in range(2, 41):
        target = math.factorial(n_value)
        real_part, imag_part = gaussian_power_w(n_value)
        m_defect = target - real_part
        assert m_defect > 0 and m_defect % 2 == 0
        k_poly = [imag_part - m_defect // 2, m_defect // 2]
        tk = stein(k_poly)
        expected_tk = [m_defect // 2, -imag_part, -m_defect // 2]
        assert tk == expected_tk
        g_poly, remainder = divide_monic(tk, U)
        assert g_poly == [-m_defect // 2]
        assert remainder + [0] * (2 - len(remainder)) == [m_defect, -imag_part]

        localizer_index = n_value + 10
        h_poly = h_sparse(localizer_index)
        row = verify_prime_window(h_poly, k_poly, base_denominator=30)
        assert row["alpha"] == m_defect
        assert row["beta"] == -imag_part
        compact = {
            "N": n_value,
            "R_N": real_part,
            "I_N": imag_part,
            "M_N": m_defect,
            "localizer_m": localizer_index,
            "forced_prime_count": len(row["full_output_primes"]),
            "forced_prime_product_bits": int(row["full_prime_product"]).bit_length(),
            "output_denominator_bits": int(row["output_shift_denominator"]).bit_length(),
            "row_sha256": hashlib.sha256(
                json.dumps(row, sort_keys=True).encode()
            ).hexdigest(),
        }
        row_digests.append(compact)
        if n_value in selected_n:
            rows.append({**compact, "prime_window_record": row})
    encoded = json.dumps(row_digests, sort_keys=True, separators=(",", ":")).encode()
    return {
        "N_range": [2, 40],
        "row_count": len(row_digests),
        "all_rows_sha256": hashlib.sha256(encoded).hexdigest(),
        "selected_rows": rows,
    }


def perturbed_localizer_checks() -> dict[str, object]:
    records = []
    for m_value in [4, 7, 12, 20, 30]:
        h_base = h_sparse(m_value)
        n_value = 4 * m_value
        # This is not h_m: add u^2*x^n*(2-3x+x^2).  It preserves the
        # congruence and the initial order while keeping d<2n.
        perturbation = multiply(U_SQUARED, shift([2, -3, 1], n_value))
        h_poly = add(h_base, perturbation)
        assert order_at_zero(h_poly) == n_value
        assert add(h_poly, [-1]) == multiply(
            U_SQUARED,
            divide_monic(add(h_poly, [-1]), U_SQUARED)[0],
        )
        k_poly = [3, -2, 1]
        row = verify_prime_window(h_poly, k_poly, base_denominator=42)
        records.append(
            {
                "m_seed": m_value,
                "n": row["n"],
                "d": row["d"],
                "e": row["e"],
                "alpha": row["alpha"],
                "forced_primes": row["full_output_primes"],
                "output_shift_denominator": row["output_shift_denominator"],
                "h_sha256": row["h_sha256"],
            }
        )
    return {
        "record_count": len(records),
        "meaning": (
            "Non-h_m integral localizers with the same long initial gap; "
            "no positivity is assumed or inferred."
        ),
        "records": records,
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
        "schema": "common_kernel_robin_localizer_moment_denominator_certificate_v1",
        "logical_scope": (
            "Exact replay of a prime-window denominator obstruction for "
            "high-order Robin localizers. It includes the full quotient, "
            "not only two isolated moments, but leaves nonlocal and signed "
            "cross-channel cancellation open and proves no classification "
            "of e+pi."
        ),
        "all_parameter_theorem": {
            "quotient": (
                "S=(h-1)G+((h-1)/u)(alpha+beta*x)+"
                "(1-x)(h'/u)K"
            ),
            "forced_prefix": (
                "For j<ord_0(h), r=(h-1)/u has r_2k=(-1)^(k+1) "
                "and r_(2k+1)=0."
            ),
            "prime_window": (
                "If p>(deg(S)+1)/2, p-1>deg(G), p<ord_0(h), "
                "and p does not divide alpha, then "
                "v_p(4*integral(S))=-1."
            ),
            "asymptotic": (
                "For fixed correction data and ord_0(h)>=(1/2+eps)deg(h), "
                "the forced denominator has log at least eps*deg(h)+o(deg(h))."
            ),
            "norm_scope": (
                "A fixed nonzero K retains its first endpoint jet, so its "
                "weighted L1 correction norm is only polynomially small; "
                "denominator times absolute norm diverges in this regime."
            ),
        },
        "sparse_h_m_checks": sparse_family_checks(),
        "perturbed_non_h_m_checks": perturbed_localizer_checks(),
        "taylor_correction_checks": taylor_correction_checks(),
        "signed_zero_moment_scope_witness": signed_scope_witness(),
        "dependency_checks": dependency_checks,
        "source_sha256": sha256(SOURCE),
        "control_audit": {"source": source_control, "script": script_control},
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "Failure guard only; it neither allocates nor limits the "
                "approximately 50 GiB available Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: exact low-degree integer and rational arithmetic "
                "is CPU-suitable."
            ),
        },
        "missing_lemma": (
            "A construction or obstruction for nonlocal multipliers with "
            "deg(h) at least about twice ord_0(h), including possible signed "
            "cancellation among varying output channels."
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
