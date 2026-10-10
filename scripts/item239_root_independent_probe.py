#!/usr/bin/env python3
"""Independent small-row audit of Item 239's separated j=2 Witt bridge."""

from __future__ import annotations

import hashlib
import json
import math


def primes_upto(limit: int) -> list[int]:
    answer = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, math.isqrt(value) + 1)):
            answer.append(value)
    return answer


def convolution(left: list[int], right: list[int], modulus: int | None = None) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
            if modulus:
                output[i + j] %= modulus
    return output


def binomial_poly(base: tuple[int, ...], exponent: int, modulus: int) -> list[int]:
    output = [1]
    factor = [entry % modulus for entry in base]
    while exponent:
        if exponent & 1:
            output = convolution(output, factor, modulus)
        exponent //= 2
        if exponent:
            factor = convolution(factor, factor, modulus)
    return output


def p_poly(p: int, s: int, nu: int, modulus: int) -> tuple[int, int, list[int]]:
    r = (p - 6 * s - 3) // 2
    q = 2 * s - nu
    output = convolution(
        binomial_poly((1, -1), r, modulus),
        binomial_poly((1, 1), 1 + 3 * nu, modulus),
        modulus,
    )
    output = convolution(output, binomial_poly((1, 0, 1), q, modulus), modulus)
    return r, q, output


def coefficient_product(left: list[int], right: list[int], target: int, modulus: int) -> int:
    return sum(
        left[index] * right[target - index]
        for index in range(max(0, target - len(right) + 1), min(target, len(left) - 1) + 1)
    ) % modulus


def exact_c(p: int, s: int, nu: int) -> int:
    r = (p - 6 * s - 3) // 2
    q = 2 * s - nu
    target = 5 * p - q - 1
    plus_power = 1 + 3 * nu
    minus_power = 7 * p + r

    def numerator_coefficient(degree: int) -> int:
        return sum(
            math.comb(plus_power, shift)
            * (-1) ** (degree - shift)
            * math.comb(minus_power, degree - shift)
            for shift in range(max(0, degree - minus_power), min(plus_power, degree) + 1)
        )

    negative_power = 5 * p - q
    return sum(
        numerator_coefficient(target - 2 * index)
        * (-1) ** index
        * math.comb(negative_power + index - 1, index)
        for index in range(target // 2 + 1)
    )


def separated_quotient(p: int, s: int, nu: int) -> int:
    modulus = p * p
    _, q, poly2 = p_poly(p, s, nu, modulus)
    _, _, poly1 = p_poly(p, s, nu, p)
    atilde = [0] * p
    btilde = [0] * (2 * p - 1)
    for k in range(1, p):
        quotient = math.comb(p, k) // p
        atilde[k] = (-1) ** k * quotient % modulus
        btilde[2 * k] = quotient % modulus
    target1 = p - q - 1
    target2 = 2 * p - q - 1
    x = coefficient_product(atilde, poly2, target1, modulus)
    y = coefficient_product(btilde, poly2, target1, modulus)
    yprime = coefficient_product(btilde, poly2, target2, modulus)
    linear = (9 * x - 10 * y + yprime) % modulus

    a = [entry % p for entry in atilde]
    b = [entry % p for entry in btilde]
    aa, bb, ab = convolution(a, a, p), convolution(b, b, p), convolution(a, b, p)

    def section(kernel: list[int], phase: int) -> int:
        return coefficient_product(kernel, poly1, phase * p - q - 1, p)

    quadratic = (
        9 * section(aa, 2) - 18 * section(aa, 1)
        - 3 * section(bb, 4) + 6 * section(bb, 3)
        + 6 * section(bb, 2) - 36 * section(bb, 1)
        - 9 * section(ab, 3) - 16 * section(ab, 2) + 54 * section(ab, 1)
    ) % p
    return (-35 * linear + 35 * p * quadratic) % modulus


def barrier_witness() -> dict[str, int]:
    p = 17
    harmonics = [0] * p
    for k in range(1, p):
        harmonics[k] = (harmonics[k - 1] + pow(k, -1, p)) % p
    a = [0] * p
    b = [0] * (2 * p - 1)
    for k in range(1, p):
        a[k] = -pow(k, -1, p) % p
        b[2 * k] = (-1) ** (k - 1) * pow(k, -1, p) % p
    aa, bb, ab = convolution(a, a, p), convolution(b, b, p), convolution(a, b, p)

    def coefficient(poly: list[int], degree: int) -> int:
        return poly[degree] if 0 <= degree < len(poly) else 0

    def total(n: int) -> tuple[int, int, int]:
        c = (2, 0, -2, 0)[n % 4]
        j = (0, -2, 0, 2)[n % 4]  # chi=1 for p=17
        inv = pow(n, -1, p)
        one = -j * inv * inv - 9 * harmonics[n - 1] * inv
        if n % 2 == 0:
            one += 10 * c * harmonics[n // 2 - 1] * inv
        else:
            one -= j * harmonics[(p + n) // 2 - 1] * inv
        two = 9 * coefficient(aa, p + n) - 18 * coefficient(aa, n)
        two += -3 * coefficient(bb, 3 * p + n) + 6 * coefficient(bb, 2 * p + n)
        two += 6 * coefficient(bb, p + n) - 36 * coefficient(bb, n)
        two += -9 * coefficient(ab, 2 * p + n) - 16 * coefficient(ab, p + n)
        two += 54 * coefficient(ab, n)
        one, two = one % p, two % p
        weight = 9 - 10 * c + j
        corrected = (weight + p * n * (one + two)) % (p * p)
        return one, two, corrected

    first = total(2)
    second = total(6)
    if first != (4, 4, 12) or second != (9, 4, 199):
        raise AssertionError((first, second))
    return {"n2_depth1": first[0], "n2_depth2": first[1], "n2_weight": first[2],
            "n6_depth1": second[0], "n6_depth2": second[1], "n6_weight": second[2]}


def main() -> None:
    rows = []
    for p in primes_upto(83):
        if p < 17:
            continue
        for s in range(2, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            for nu in (0, 1):
                coefficient = exact_c(p, s, nu)
                if coefficient % p:
                    raise AssertionError((p, s, nu, "p divisibility"))
                actual = coefficient // p % (p * p)
                predicted = separated_quotient(p, s, nu)
                if actual != predicted:
                    raise AssertionError((p, s, nu, actual, predicted))
                rows.append((p, s, nu, actual))
    digest = hashlib.sha256(
        "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    ).hexdigest()
    print(json.dumps({"row_nu_count": len(rows), "row_digest_sha256": digest,
                      "barrier": barrier_witness()}, sort_keys=True))


if __name__ == "__main__":
    main()
