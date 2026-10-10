#!/usr/bin/env python3
"""Replay the exact even-localizer one-third prime-window theorem.

The all-parameter proof is in the companion source.  This script checks
normalizations, exact rational valuations, the positive boundary family,
the full-channel residue criterion, and an exact positive example outside
the proved window.  Finite checks are not used as asymptotic evidence.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_even_nonlocal_moment_denominator_barrier.md"
OUTPUT = ROOT / "results/common_kernel_even_nonlocal_moment_denominator_certificate.json"

# This is a failure guard, not an allocation or an imposed 2-GiB limit.
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_robin_localizer_moment_denominator_hashes.sha256":
        "1a523213cd86f5b3865bf86a7b35a4f0bd682df262af920cc7b02623f0560c03",
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


def memory_snapshot_kib() -> dict[str, int]:
    wanted = {"MemTotal", "MemAvailable"}
    output: dict[str, int] = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        if key in wanted:
            fields = rest.split()
            assert fields[1] == "kB"
            output[key] = int(fields[0])
    assert set(output) == wanted
    return output


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


def evaluate(poly: list[int], value: Fraction) -> Fraction:
    result = Fraction(0)
    for item in reversed(poly):
        result = result * value + item
    return result


def substitute_one_minus_x(poly: list[int]) -> list[int]:
    output = [0]
    for exponent, value in enumerate(poly):
        term = [
            value * math.comb(exponent, index) * ((-1) ** index)
            for index in range(exponent + 1)
        ]
        output = add(output, term)
    return output


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


def integer_valuation(value: int, prime: int) -> int:
    assert value
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def rational_valuation(value: Fraction, prime: int) -> int:
    assert value
    return (
        integer_valuation(value.numerator, prime)
        - integer_valuation(value.denominator, prime)
    )


def integer_digest(value: int) -> str:
    return hashlib.sha256(str(value).encode()).hexdigest()


def fraction_digest(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode()
    ).hexdigest()


def polynomial_digest(poly: list[int]) -> str:
    digest = hashlib.sha256()
    for index, value in enumerate(trim(poly)):
        digest.update(f"{index}:{value};".encode())
    return digest.hexdigest()


BASE = [0, 0, 0, 0, 2, 0, 0, 0, -1]


def check_even_localizer(h_poly: list[int]) -> dict[str, object]:
    h_poly = trim(h_poly)
    d_value = degree(h_poly)
    n_value = order_at_zero(h_poly)
    assert h_poly[0] == 0
    assert all(value == 0 for index, value in enumerate(h_poly) if index % 2)

    q_poly, remainder = divide_monic(add(h_poly, [-1]), U_SQUARED)
    assert remainder == [0]
    r_poly, remainder = divide_monic(add(h_poly, [-1]), U)
    assert remainder == [0]
    assert r_poly == multiply(U, q_poly)
    assert degree(r_poly) == d_value - 2
    assert all(value == 0 for index, value in enumerate(r_poly) if index % 2)

    for index in range(n_value):
        expected = 0 if index % 2 else (-1) ** (index // 2 + 1)
        assert coefficient(r_poly, index) == expected

    i_zero = integral(r_poly)
    i_one = integral(r_poly, 2)
    common_denominator = math.lcm(i_zero.denominator, i_one.denominator)

    window = [
        prime
        for prime in primes_up_to(n_value)
        if prime % 2 and 3 * prime > d_value
    ]
    prime_product = math.prod(window)
    for prime in window:
        assert rational_valuation(i_zero, prime) == -1
        assert coefficient(r_poly, prime - 1) in {-1, 1}
        assert coefficient(r_poly, 2 * prime - 1) == 0
    assert i_zero.denominator % prime_product == 0
    assert common_denominator % prime_product == 0

    return {
        "n": n_value,
        "d": d_value,
        "I0": i_zero,
        "I1": i_one,
        "common_denominator": common_denominator,
        "window_primes": window,
        "window_product": prime_product,
        "h_sha256": polynomial_digest(h_poly),
        "q_sha256": polynomial_digest(q_poly),
        "r_sha256": polynomial_digest(r_poly),
    }


def boundary_family_checks() -> dict[str, object]:
    expected_q_base = [-1, 0, 2, 0, -1]
    q_base, remainder = divide_monic(add(BASE, [-1]), U_SQUARED)
    assert remainder == [0]
    assert q_base == expected_q_base
    assert add(BASE, [-1]) == scale(
        multiply(U_SQUARED, [1, 0, -2, 0, 1]), -1
    )

    t_expansion = substitute_one_minus_x(BASE)
    assert coefficient(t_expansion, 0) == 1
    assert coefficient(t_expansion, 1) == 0
    assert coefficient(t_expansion, 2) == -16
    one_minus_base_at_one_minus_t = add([1], scale(t_expansion, -1))
    one_minus_fourth_power = add([1], scale(power([1, -1], 4), -1))
    assert one_minus_base_at_one_minus_t == power(one_minus_fourth_power, 2)

    selected = {1, 2, 3, 5, 10, 20, 40, 80, 120}
    records = []
    all_rows = []
    h_poly = [1]
    for k_value in range(1, 121):
        h_poly = multiply(h_poly, BASE)
        row = check_even_localizer(h_poly)
        assert row["n"] == 4 * k_value
        assert row["d"] == 8 * k_value
        mass = integral(h_poly)
        assert mass > 0
        assert row["window_primes"] == [
            prime
            for prime in primes_up_to(4 * k_value)
            if 3 * prime > 8 * k_value
        ]
        compact = {
            "k": k_value,
            "n": row["n"],
            "d": row["d"],
            "window_prime_count": len(row["window_primes"]),
            "window_product_bits": int(row["window_product"]).bit_length(),
            "window_product_sha256": integer_digest(int(row["window_product"])),
            "I0_denominator_bits": row["I0"].denominator.bit_length(),
            "I0_sha256": fraction_digest(row["I0"]),
            "pair_denominator_bits": int(row["common_denominator"]).bit_length(),
            "pair_denominator_sha256": integer_digest(
                int(row["common_denominator"])
            ),
            "mass_sha256": fraction_digest(mass),
            "sqrt_k_times_mass_float": math.sqrt(k_value) * float(mass),
            "h_sha256": row["h_sha256"],
        }
        all_rows.append(compact)
        if k_value in selected:
            records.append(
                {
                    **compact,
                    "window_primes": row["window_primes"],
                    "mass": str(mass),
                }
            )

    encoded = json.dumps(all_rows, sort_keys=True, separators=(",", ":")).encode()
    return {
        "base_coefficients": BASE,
        "base_q_coefficients": q_base,
        "base_taylor_at_x=1_first_terms": t_expansion[:5],
        "k_range": [1, 120],
        "all_rows_sha256": hashlib.sha256(encoded).hexdigest(),
        "selected_records": records,
        "finite_scope": (
            "Exact finite valuations and normalization checks only. The "
            "prime-window theorem and mass asymptotic are proved in the source."
        ),
    }


def perturbed_even_checks() -> dict[str, object]:
    records = []
    for k_value in [4, 6, 10, 16, 24, 40]:
        n_value = 4 * k_value
        base_power = power(BASE, k_value)
        # The perturbation begins after the initial gap and gives degree 5n/2.
        seed = [3, 0, -2, 0, 1]
        start = 5 * n_value // 2 - 8
        perturbation = multiply(U_SQUARED, shift(seed, start))
        h_poly = add(base_power, perturbation)
        row = check_even_localizer(h_poly)
        assert row["n"] == n_value
        assert row["d"] == 5 * n_value // 2
        records.append(
            {
                "k_seed": k_value,
                "n": row["n"],
                "d": row["d"],
                "window_primes": row["window_primes"],
                "I0_sha256": fraction_digest(row["I0"]),
                "pair_denominator_bits": int(row["common_denominator"]).bit_length(),
                "h_sha256": row["h_sha256"],
            }
        )
    return {
        "records": records,
        "meaning": (
            "Even integral congruence-preserving examples with d=5n/2. "
            "No positivity is assumed or inferred from these perturbations."
        ),
    }


def quotient_data(h_poly: list[int], k_poly: list[int]) -> dict[str, object]:
    tk = stein(k_poly)
    g_poly, remainder = divide_monic(tk, U)
    padded = remainder + [0] * (2 - len(remainder))
    alpha, beta = padded[:2]

    q_poly, remainder = divide_monic(add(h_poly, [-1]), U_SQUARED)
    assert remainder == [0]
    r_poly = multiply(U, q_poly)
    h_prime_over_u, remainder = divide_monic(derivative(h_poly), U)
    assert remainder == [0]
    formula = add(
        multiply(add(h_poly, [-1]), g_poly),
        multiply(r_poly, [alpha, beta]),
        multiply([1, -1], multiply(h_prime_over_u, k_poly)),
    )
    direct, remainder = divide_monic(
        add(stein(multiply(h_poly, k_poly)), scale(tk, -1)), U
    )
    assert remainder == [0]
    assert direct == formula
    return {
        "S": formula,
        "G": g_poly,
        "alpha": alpha,
        "beta": beta,
        "q": q_poly,
        "r": r_poly,
    }


def full_channel_residue_checks() -> dict[str, object]:
    k_zero, k_one = 7, 5
    k_poly = [k_zero, k_one]
    records = []
    for exponent in [4, 8, 12, 20, 30, 50]:
        h_poly = power(BASE, exponent)
        n_value = order_at_zero(h_poly)
        data = quotient_data(h_poly, k_poly)
        s_poly = data["S"]
        q_poly = data["q"]
        alpha = int(data["alpha"])
        beta = int(data["beta"])
        assert data["G"] == [-k_one]
        assert alpha == 2 * k_one
        assert beta == -(k_zero + k_one)
        s_integral = integral(s_poly)

        tested = []
        cancelled = []
        survived = []
        for prime in primes_up_to(n_value - 1):
            if prime % 2 == 0 or 3 * prime <= degree(s_poly) + 1:
                continue
            low = coefficient(s_poly, prime - 1)
            high = coefficient(s_poly, 2 * prime - 1)
            epsilon = (-1) ** ((prime + 1) // 2)
            assert low == epsilon * alpha

            q_a = coefficient(q_poly, 2 * prime - 2)
            q_b = coefficient(q_poly, 2 * prime - 4)
            expected_high = (k_zero + k_one) * (q_a - q_b)
            assert (high - expected_high) % prime == 0

            residue = (2 * low + high) % prime
            valuation = rational_valuation(s_integral, prime)
            assert (valuation == -1) == (residue != 0)
            item = {
                "p": prime,
                "combined_residue": residue,
                "v_p_integral_S": valuation,
            }
            tested.append(item)
            if residue:
                survived.append(prime)
            else:
                cancelled.append(prime)

        records.append(
            {
                "base_power": exponent,
                "n": n_value,
                "degree_S": degree(s_poly),
                "tested": tested,
                "survived_primes": survived,
                "cancelled_primes": cancelled,
                "S_sha256": polynomial_digest(s_poly),
                "integral_S_sha256": fraction_digest(s_integral),
            }
        )
    return {
        "K_coefficients": k_poly,
        "records": records,
        "scope": (
            "Checks the iff residue criterion and the linear-K high coefficient. "
            "Observed survival or cancellation is not extrapolated across primes."
        ),
    }


def positive_outside_window_checks() -> dict[str, object]:
    h_poly = [0, 0, 1, -4, 7, -8, 7, -4, 2]
    factor_h = multiply(
        [0, 0, 1],
        multiply([1, -1, 1], [1, -3, 3, -2, 2]),
    )
    assert h_poly == factor_h

    q_poly = [-1, 0, 3, -4, 2]
    assert add(h_poly, [-1]) == multiply(U_SQUARED, q_poly)
    cubic = [1, 1, -2, 2]
    assert add([1], scale(h_poly, -1)) == multiply(
        [1, -1], multiply(U_SQUARED, cubic)
    )
    assert order_at_zero(h_poly) == 2
    assert degree(h_poly) == 8
    assert evaluate(h_poly, Fraction(0)) == 0
    assert evaluate(h_poly, Fraction(1)) == 1
    assert evaluate(derivative(h_poly), Fraction(1)) == 8
    assert integral(h_poly) == Fraction(11, 90)

    power_records = []
    for exponent in [1, 2, 3, 5, 10, 20]:
        item = power(h_poly, exponent)
        quotient, remainder = divide_monic(add(item, [-1]), U_SQUARED)
        assert remainder == [0]
        assert order_at_zero(item) == 2 * exponent
        assert degree(item) == 8 * exponent
        power_records.append(
            {
                "power": exponent,
                "n": order_at_zero(item),
                "d": degree(item),
                "h_sha256": polynomial_digest(item),
                "q_sha256": polynomial_digest(quotient),
            }
        )

    return {
        "H_coefficients": h_poly,
        "q_coefficients": q_poly,
        "integral_H": "11/90",
        "H_prime_at_1": 8,
        "power_records": power_records,
        "proof_scope": (
            "Exact factor identities support the interval-positivity proof in "
            "the source. No denominator asymptotic for these powers is claimed."
        ),
    }


def main() -> None:
    started = time.perf_counter()
    initial_memory = memory_snapshot_kib()
    assert initial_memory["MemTotal"] > 0

    dependency_checks = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependency_checks[relative] = {"expected": expected, "actual": actual}

    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__))
    assert source_control["clean"] and script_control["clean"]

    payload = {
        "schema": "common_kernel_even_nonlocal_moment_denominator_certificate_v1",
        "logical_scope": (
            "Exact replay of the one-third prime-window denominator theorem "
            "for even Robin localizers, including a positive d=2n family. "
            "Non-even, d>=3n, and unrestricted cross-channel cases remain open; "
            "no e+pi classification is asserted."
        ),
        "all_parameter_theorem": {
            "hypotheses": (
                "h is even in Z[x], h(0)=0, and h=1 mod (1+x^2)^2; "
                "n=ord_0(h), d=deg(h)."
            ),
            "prime_window": (
                "Every odd prime d/3<p<=n has v_p(I0)=-1 for "
                "I0=integral((h-1)/(1+x^2))."
            ),
            "pair_bound": (
                "If 0<=h<=1 and D clears I0,I1, then "
                "D*max(abs(I0),abs(I1)) is at least the window-prime "
                "product divided by 16*d^2."
            ),
            "asymptotic": (
                "If n>=(1/3+eps)d, log D>=eps*d+o(d)."
            ),
            "boundary_family": (
                "For h_k=(2*x^4-x^8)^k, n=4k,d=8k, and "
                "sqrt(k)*integral(h_k) tends to sqrt(pi)/8."
            ),
            "full_channel_scope": (
                "For p>(deg(S)+1)/3, survival is equivalent to "
                "2*S_(p-1)+S_(2p-1) nonzero mod p; even h alone does not "
                "annihilate the second coefficient."
            ),
        },
        "boundary_positive_family_checks": boundary_family_checks(),
        "perturbed_even_d=5n/2_checks": perturbed_even_checks(),
        "full_channel_residue_checks": full_channel_residue_checks(),
        "positive_degree_order_ratio_four_example": positive_outside_window_checks(),
        "dependency_checks": dependency_checks,
        "source_sha256": sha256(SOURCE),
        "control_audit": {"source": source_control, "script": script_control},
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "The 40-GiB value is only a failure guard. It neither allocates "
                "nor limits the approximately 50 GiB available Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: the replay is small exact integer/rational arithmetic "
                "for which GPU transfer and non-exact kernels provide no benefit."
            ),
        },
        "missing_lemma": (
            "Control the 2p coefficient for non-even moments or for the full "
            "output residue, or find a different denominator obstruction for "
            "even positive localizers with d>=3n."
        ),
    }

    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_GUARD_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    final_memory = memory_snapshot_kib()
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak}")
    print(f"MemAvailable_kib {final_memory['MemAvailable']}")


if __name__ == "__main__":
    main()
