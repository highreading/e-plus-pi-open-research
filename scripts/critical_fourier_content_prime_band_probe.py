"""Exact diagnostics for the forced prime band in Fourier content.

This is validation only.  The proof is in
sources/critical_fourier_content_prime_band.md.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from math import comb, factorial, gcd, lcm


Gaussian = tuple[int, int]


def valuation_two(value: int) -> int:
    assert value != 0
    return (abs(value) & -abs(value)).bit_length() - 1


def super_catalan(left: int, right: int) -> int:
    assert left >= 0 and right >= 0
    numerator = comb(2 * left, left) * comb(2 * right, right)
    denominator = comb(left + right, left)
    assert numerator % denominator == 0
    return numerator // denominator


def exponential_pair(n: int) -> tuple[int, int]:
    terms = [
        factorial(n + j) // (factorial(j) * factorial(n - j))
        for j in range(n + 1)
    ]
    p_value = sum(terms)
    q_value = ((-1) ** n) * sum(
        ((-1) ** j) * value for j, value in enumerate(terms)
    )
    assert p_value > 0 and q_value > 0
    assert gcd(p_value, q_value) == 1
    assert p_value % 2 == 1 and q_value % 2 == 1
    return p_value, q_value


def gadd(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] + b[0], a[1] + b[1]


def gmul(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gscale(c: int, a: Gaussian) -> Gaussian:
    return c * a[0], c * a[1]


def gpow(a: Gaussian, exponent: int) -> Gaussian:
    out = (1, 0)
    base = a
    power = exponent
    while power:
        if power & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        power >>= 1
    return out


def polymul(left: list[Gaussian], right: list[Gaussian]) -> list[Gaussian]:
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = gadd(out[i + j], gmul(a, b))
    return out


def fourier_polynomial(n: int, k: int) -> list[Gaussian]:
    assert n > 0 and n % 2 == 0 and k > n
    ell = k - n - 1
    first = [(((-1) ** (n - j)) * comb(n, j), 0) for j in range(n + 1)]
    second = [
        gscale(comb(n, j), gmul(gpow((1, 1), j), gpow((1, -1), n - j)))
        for j in range(n + 1)
    ]
    third = [(comb(2 * ell, j), 0) for j in range(2 * ell + 1)]
    phase = gpow((0, -1), n)
    return [gmul(phase, coefficient) for coefficient in polymul(polymul(first, second), third)]


def primes_below(limit: int) -> list[int]:
    if limit <= 2:
        return []
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit - 1) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = b"\x00" * (((limit - 1 - p * p) // p) + 1)
    return [p for p in range(2, limit) if sieve[p]]


def exact_case(n: int, k: int, all_primes: list[int]) -> dict[str, int]:
    coefficients = fourier_polynomial(n, k)
    center = k - 1
    assert len(coefficients) == 2 * k - 1
    c_zero = coefficients[center]
    assert c_zero[1] == 0 and c_zero[0] > 0
    c0 = c_zero[0]

    lk = 1
    for m in range(1, k):
        lk = lcm(lk, m)

    t_value = 0
    n_values: dict[int, int] = {}
    for m in range(1, k):
        a_m, b_m = coefficients[center + m]
        sine = (0, 1, 0, -1)[m % 4]
        cosine = (1, 0, -1, 0)[m % 4]
        n_m = a_m * sine - b_m * (1 - cosine)
        n_values[m] = n_m
        t_value += (lk // m) * n_m

    content = gcd(abs(4 * t_value), lk * c0)
    reduced_ratio = Fraction(4 * t_value, lk * c0)
    assert reduced_ratio.denominator == lk * c0 // content

    r = n // 2
    K = k - 1
    super_catalan_sum = sum(
        comb(2 * r, 2 * j) * super_catalan(r + j, K - r - j)
        for j in range(r + 1)
    )
    assert super_catalan_sum == c0
    predicted_c0_valuation = (
        r + K.bit_count() + (r % 2) * valuation_two(K)
    )
    assert valuation_two(c0) == predicted_c0_valuation
    common_denominator = math.prod(
        2 * K - (2 * r + 1 + 2 * t) for t in range(r)
    )
    common_numerator = Fraction(common_denominator * c0, super_catalan(r, K - r))
    assert common_numerator.denominator == 1
    assert common_numerator.numerator % (2**r) == 0
    normalized_numerator = common_numerator.numerator // (2**r)
    if r % 2:
        assert normalized_numerator % K == 0
        assert (normalized_numerator // K) % 2 == 1
    else:
        assert normalized_numerator % 2 == 1

    assert t_value % (2**K) == 0

    primitive_a = 4 * t_value // content
    primitive_b = lk * c0 // content
    assert gcd(abs(primitive_a), primitive_b) == 1
    assert primitive_b % 2 == 1

    p_value, q_value = exponential_pair(n)
    matching_gcd = gcd(q_value, primitive_b)
    q_zero = q_value // matching_gcd
    b_zero = primitive_b // matching_gcd
    matched_constant = -b_zero * p_value + q_zero * primitive_a
    matched_coefficient = q_value * primitive_b // matching_gcd
    final_content = gcd(abs(matched_constant), matched_coefficient)
    assert gcd(abs(matched_constant), q_zero * b_zero) == 1
    assert final_content == gcd(abs(matched_constant), matching_gcd)
    assert matching_gcd % 2 == 1 and final_content % 2 == 1

    ell = k - n - 1
    forced_primes = [
        p for p in all_primes if 2 * p > center and 3 * p <= 2 * ell
    ]
    forced_product = 1
    for p in forced_primes:
        forced_product *= p
        for index in (center - p, center, center + p):
            real, imag = coefficients[index]
            assert real % p == 0 and imag % p == 0
        assert n_values[p] % p == 0
        assert t_value % p == 0
        assert content % p == 0
    assert content % forced_product == 0

    return {
        "forced_prime_count": len(forced_primes),
        "forced_product": forced_product,
        "content": content,
        "c0": c0,
        "lk": lk,
        "t_value": t_value,
        "c0_two_adic_valuation": valuation_two(c0),
        "t_two_adic_valuation": valuation_two(t_value),
        "primitive_a": primitive_a,
        "primitive_b": primitive_b,
        "matching_gcd": matching_gcd,
        "final_content": final_content,
    }


def main() -> None:
    maximum_k = 900
    all_primes = primes_below(maximum_k + 1)

    exhaustive_case_count = 0
    exhaustive_forced_incidence_count = 0
    nonempty_band_case_count = 0
    for n in range(2, 22, 2):
        for k in range(n + 1, 161):
            record = exact_case(n, k, all_primes)
            exhaustive_case_count += 1
            exhaustive_forced_incidence_count += record["forced_prime_count"]
            if record["forced_prime_count"]:
                nonempty_band_case_count += 1

    square_ray_records: list[dict[str, object]] = []
    for n in range(2, 32, 2):
        k = n * n
        record = exact_case(n, k, all_primes)
        h = record["content"]
        forced = record["forced_product"]
        square_ray_records.append(
            {
                "n": n,
                "k": k,
                "content": str(h),
                "forced_prime_product": str(forced),
                "forced_prime_count": record["forced_prime_count"],
                "log_content": format(math.log(h), ".12f"),
                "log_forced_prime_product": format(math.log(forced), ".12f") if forced > 1 else "0.000000000000",
                "log_content_over_n_log_n": format(math.log(h) / (n * math.log(n)), ".12f"),
            }
        )

    large_prime_example = exact_case(2, 26, all_primes)
    assert large_prime_example["content"] == 37_350_144
    assert large_prime_example["content"] % 43 == 0

    matching_warning = exact_case(2, 10, all_primes)
    assert matching_warning["primitive_a"] == -149_056
    assert matching_warning["primitive_b"] == 135_135
    assert matching_warning["matching_gcd"] == 7
    assert matching_warning["final_content"] == 7

    print(
        json.dumps(
            {
                "status": "pass",
                "role": "finite exact validation only; no finite scan is used in the proof",
                "proved_claim_tested": "product of primes (k-1)/2 < p <= 2(k-n-1)/3 divides h_{n,k}",
                "global_exact_identity_tested": "denominator(4T/(L_k C0)) = L_k C0 / h_{n,k}",
                "all_degree_exact_identities_tested": [
                    "C0 = sum_j binomial(2r,2j) super_catalan(r+j,K-r-j)",
                    "v2(C0) = r + s2(K) + (r mod 2) v2(K)",
                    "2^K divides T_{n,k}",
                ],
                "exhaustive_box": {
                    "n": "even 2..20",
                    "k": "all n+1..160",
                    "case_count": exhaustive_case_count,
                    "nonempty_prime_band_case_count": nonempty_band_case_count,
                    "forced_prime_incidence_count": exhaustive_forced_incidence_count,
                },
                "large_prime_example": {
                    "n": 2,
                    "k": 26,
                    "content": str(large_prime_example["content"]),
                    "factorization": "2^8 * 3^2 * 13 * 29 * 43",
                    "prime_above_k_minus_one": 43,
                },
                "matching_content_warning": {
                    "n": 2,
                    "k": 10,
                    "primitive_pi_pair": [
                        str(matching_warning["primitive_a"]),
                        str(matching_warning["primitive_b"]),
                    ],
                    "matching_gcd": matching_warning["matching_gcd"],
                    "final_content": matching_warning["final_content"],
                    "proved_identity_tested": "g = gcd(M,d)",
                    "scope": "shows that odd final content remains uncontrolled",
                },
                "square_ray_records": square_ray_records,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
