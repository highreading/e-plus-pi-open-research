#!/usr/bin/env python3
"""Exact certificate for the Laguerre-square common-kernel construction.

All identities and searches use Fraction/integer arithmetic.  Floating-point
values are labelled diagnostics and are never used to certify an identity.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, gcd
import json
import random

import mpmath as mp


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


def laguerre(n: int) -> list[Fraction]:
    return [Fraction((-1) ** j * comb(n, j), factorial(j))
            for j in range(n + 1)]


def gaussian_mul_w(z: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    # (a+bi)(1-i)=(a+b)+(b-a)i
    a, b = z
    return a + b, b - a


def eval_at_w(poly: list[Fraction]) -> tuple[Fraction, Fraction]:
    power = (Fraction(1), Fraction(0))
    out = (Fraction(0), Fraction(0))
    for coefficient in poly:
        out = (out[0] + coefficient * power[0],
               out[1] + coefficient * power[1])
        power = gaussian_mul_w(power)
    return out


def laguerre_evaluation(n: int) -> tuple[Fraction, Fraction]:
    return eval_at_w(laguerre(n))


def add_poly(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        out[j] += x
    for j, x in enumerate(b):
        out[j] += x
    return out


def scale_poly(a: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * x for x in a]


def multiply(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            out[j + k] += x * y
    return out


def laguerre_to_monomial(c: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)]
    for k, coefficient in enumerate(c):
        out = add_poly(out, scale_poly(laguerre(k), coefficient))
    return out


def monomial_to_laguerre(q: list[int]) -> list[int]:
    # t^j=j! sum_{k=0}^j (-1)^k binom(j,k)L_k(t).
    out = [0] * len(q)
    for j, coefficient in enumerate(q):
        for k in range(j + 1):
            out[k] += coefficient * factorial(j) * (-1) ** k * comb(j, k)
    return out


def primitive_integer(poly: list[Fraction]) -> list[int]:
    denominator = 1
    for x in poly:
        denominator = lcm(denominator, x.denominator)
    out = [x.numerator * (denominator // x.denominator) for x in poly]
    content = 0
    for x in out:
        content = gcd(content, abs(x))
    assert content
    out = [x // content for x in out]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    if out[-1] < 0:
        out = [-x for x in out]
    return out


def construct_from_direction(n: int, parameters: list[int]) -> dict:
    assert len(parameters) == n - 1
    evaluations = [laguerre_evaluation(k) for k in range(n + 1)]
    u = [z[0] for z in evaluations]
    v = [z[1] for z in evaluations]
    assert u[0] == 1 and v[0] == 0 and v[1] == 1
    d = [Fraction(0)] * (n + 1)
    for k in range(2, n + 1):
        d[k] = Fraction(parameters[k - 2])
    d[1] = -sum((v[k] * d[k] for k in range(2, n + 1)), Fraction(0))
    U = sum((u[k] * d[k] for k in range(n + 1)), Fraction(0))
    if U == 0:
        raise ValueError("constant/tangent direction")
    norm_d = sum((x * x for x in d), Fraction(0))
    delta = norm_d - U * U
    c = [delta] + [2 * U * d[k] for k in range(1, n + 1)]
    q = laguerre_to_monomial(c)
    Q = primitive_integer(q)
    return {"d": d, "U": U, "delta": delta, "c": c, "Q": Q}


def divide_by_h(poly: list[Fraction]) -> list[Fraction]:
    # Divide by H=t^2-2t+2; require zero remainder.
    work = list(poly)
    quotient = [Fraction(0)] * (len(poly) - 2)
    for k in range(len(poly) - 1, 1, -1):
        leading = work[k]
        quotient[k - 2] = leading
        work[k] -= leading
        work[k - 1] += 2 * leading
        work[k - 2] -= 2 * leading
    assert work[0] == 0 and work[1] == 0
    return quotient


def shifted_exponential_moment(poly: list[Fraction]) -> Fraction:
    # Integral_0^infty exp(-u) poly(1+u) du.
    out = Fraction(0)
    for n, coefficient in enumerate(poly):
        out += coefficient * sum(Fraction(comb(n, r) * factorial(r))
                                 for r in range(n + 1))
    return out


def output_data(Q: list[int]) -> dict:
    q = [Fraction(x) for x in Q]
    wr, wi = eval_at_w(q)
    assert wi == 0 and wr.denominator == 1 and wr != 0
    m = wr.numerator
    square = multiply(q, q)
    a = m * m
    numerator = list(square)
    numerator[0] -= a
    R = divide_by_h(numerator)
    T = shifted_exponential_moment(square)
    assert all(x.denominator == 1 for x in R)
    assert T.denominator == 1
    integral_R = sum((x / (j + 1) for j, x in enumerate(R)), Fraction(0))
    b = T - 4 * integral_R
    D = b.denominator
    B = b.numerator
    denominator_cap = 1
    for j in range(1, 2 * (len(Q) - 1)):
        denominator_cap = lcm(denominator_cap, j)
    assert denominator_cap % D == 0
    common = gcd(D * a, abs(B))
    alpha = D * a // common
    beta = B // common
    lag_c = monomial_to_laguerre(Q)
    assert sum(x * x for x in lag_c) == a
    assert abs(m) >= factorial(len(Q) - 1)
    return {
        "Q": Q,
        "degree": len(Q) - 1,
        "m": m,
        "a": a,
        "laguerre_coefficients": lag_c,
        "R": [int(x) for x in R],
        "T": int(T),
        "b_numerator": B,
        "b_denominator": D,
        "gcd": common,
        "primitive_pair": [alpha, beta],
    }


def verify_orthogonality(limit: int) -> None:
    for j in range(limit + 1):
        for k in range(limit + 1):
            product = multiply(laguerre(j), laguerre(k))
            moment = sum((coefficient * factorial(r)
                          for r, coefficient in enumerate(product)), Fraction(0))
            assert moment == (1 if j == k else 0)


def verify_parameterization_samples() -> list[dict]:
    records = []
    rng = random.Random(20260827)
    for n in range(2, 11):
        checked = 0
        while checked < 12:
            parameters = [rng.randint(-7, 7) for _ in range(n - 1)]
            if not any(parameters):
                continue
            try:
                item = construct_from_direction(n, parameters)
            except ValueError:
                continue
            c, d, U = item["c"], item["d"], item["U"]
            evaluations = [laguerre_evaluation(k) for k in range(n + 1)]
            u = [z[0] for z in evaluations]
            v = [z[1] for z in evaluations]
            real_value = sum((u[k] * c[k] for k in range(n + 1)), Fraction(0))
            imag_value = sum((v[k] * c[k] for k in range(n + 1)), Fraction(0))
            norm = sum((x * x for x in c), Fraction(0))
            assert imag_value == 0 and norm == real_value * real_value
            # Exact converse: reconstruct d'=c-c0e0 and recover c.
            inverse_d = list(c)
            inverse_d[0] -= c[0]
            inverse_U = real_value - c[0]
            assert inverse_U != 0
            inverse_norm = sum((x * x for x in inverse_d), Fraction(0))
            inverse_delta = inverse_norm - inverse_U * inverse_U
            recovered = [inverse_delta] + [2 * inverse_U * inverse_d[k]
                                           for k in range(1, n + 1)]
            assert recovered == [2 * inverse_U * x for x in c]
            output_data(item["Q"])
            checked += 1
        records.append({"degree": n, "directions_checked": checked})
    return records


def degree_three_formula(r: int, z: int) -> tuple[int, int, int, int]:
    M = 27 * r * r + 36 * r * z + 35 * z * z
    N = (46980 * r**4 + 188190 * r**3 * z + 277227 * r*r*z*z
         + 189840 * r*z**3 + 92575 * z**4)
    denominator = 15 * M * M
    common = gcd(abs(N), denominator)
    return M, N, denominator // common, N // common


def degree_three_search(bound: int) -> dict:
    mp.mp.dps = 60
    s = mp.e + mp.pi
    count = 0
    minimum_alpha = None
    best = None
    for r in range(-bound, bound + 1):
        for z in range(-bound, bound + 1):
            if not (r or z) or gcd(abs(r), abs(z)) != 1:
                continue
            if 3 * r + 5 * z == 0:
                continue
            M, N, alpha, beta = degree_three_formula(r, z)
            assert M > 0
            value = alpha * s - beta
            assert value > 0
            count += 1
            if minimum_alpha is None or alpha < minimum_alpha[0]:
                minimum_alpha = (alpha, beta, r, z)
            if best is None or value < best[0]:
                best = (value, alpha, beta, r, z)
    assert minimum_alpha is not None and best is not None
    return {
        "bound": bound,
        "primitive_directions": count,
        "minimum_alpha": list(minimum_alpha),
        "diagnostic_best_pair": [best[1], best[2]],
        "diagnostic_best_direction": [best[3], best[4]],
        "diagnostic_best_value": mp.nstr(best[0], 40),
    }


def degree_four_forms(r: int, y: int, z: int) -> tuple[int, int, int, int]:
    M = (108*r*r + 144*r*y + 84*r*z + 140*y*y + 204*y*z + 173*z*z)
    N = (
        21047040*r**4 + 84309120*r**3*y + 77825664*r**3*z
        + 124197696*r*r*y*y + 181569024*r*r*y*z + 74520036*r*r*z*z
        + 85048320*r*y**3 + 108632832*r*y*y*z + 5414328*r*y*z*z
        - 5887500*r*z**3 + 41473600*y**4 + 84712320*y**3*z
        + 54042036*y*y*z*z + 44846524*y*z**3 + 41818993*z**4
    )
    denominator = 420 * M * M
    common = gcd(abs(N), denominator)
    return M, N, denominator // common, N // common


def degree_four_search(bound: int) -> dict:
    mp.mp.dps = 60
    s = mp.e + mp.pi
    count = 0
    minimum_alpha = None
    best = None
    for r in range(-bound, bound + 1):
        for y in range(-bound, bound + 1):
            for z in range(-bound, bound + 1):
                if gcd(gcd(abs(r), abs(y)), abs(z)) != 1:
                    continue
                if z == 0:  # embedded degree at most three
                    continue
                if 6*r + 10*y + 11*z == 0:
                    continue
                M, N, alpha, beta = degree_four_forms(r, y, z)
                assert M > 0
                value = alpha * s - beta
                assert value > 0
                count += 1
                if minimum_alpha is None or alpha < minimum_alpha[0]:
                    minimum_alpha = (alpha, beta, r, y, z)
                if best is None or value < best[0]:
                    best = (value, alpha, beta, r, y, z)
    assert minimum_alpha is not None and best is not None
    return {
        "bound": bound,
        "genuine_primitive_directions": count,
        "minimum_alpha": list(minimum_alpha),
        "diagnostic_best_pair": [best[1], best[2]],
        "diagnostic_best_direction": [best[3], best[4], best[5]],
        "diagnostic_best_value": mp.nstr(best[0], 40),
    }


def sparse_degree_records(limit: int) -> list[dict]:
    records = []
    for n in range(2, limit + 1):
        parameters = [0] * (n - 1)
        parameters[-1] = 1
        try:
            item = construct_from_direction(n, parameters)
        except ValueError:
            continue
        data = output_data(item["Q"])
        alpha, beta = data["primitive_pair"]
        records.append({
            "degree": n,
            "max_Q_digits": max(len(str(abs(x))) for x in data["Q"]),
            "alpha_digits": len(str(abs(alpha))),
            "primitive_pair": [alpha, beta],
        })
    return records


def main() -> None:
    verify_orthogonality(12)
    parameter_checks = verify_parameterization_samples()

    degree_two = output_data([1, 2, -1])
    assert degree_two["laguerre_coefficients"] == [1, 2, -2]
    assert degree_two["m"] == 3
    assert degree_two["b_numerator"] == 116
    assert degree_two["b_denominator"] == 3
    assert degree_two["primitive_pair"] == [27, 116]

    # Cross-check the explicit degree-three quartics against the general engine.
    for r in range(-12, 13):
        for z in range(-12, 13):
            if not (r or z) or 3*r + 5*z == 0:
                continue
            P = [
                9*r*r - 36*r*z - 35*z*z,
                18*r*r + 78*r*z + 80*z*z,
                -9*r*r - 42*r*z - 45*z*z,
                3*r*z + 5*z*z,
            ]
            data = output_data(primitive_integer([Fraction(x) for x in P]))
            M, N, alpha, beta = degree_three_formula(r, z)
            assert Fraction(data["b_numerator"],
                            data["b_denominator"] * data["a"]) == Fraction(N, 15*M*M)
            assert data["primitive_pair"] == [alpha, beta]

    # Cross-check the degree-four quartics on a deterministic box.
    for r in range(-4, 5):
        for y in range(-4, 5):
            for z in range(-4, 5):
                if not (r or y or z) or 6*r + 10*y + 11*z == 0:
                    continue
                try:
                    item = construct_from_direction(4, [r, y, z])
                except ValueError:
                    continue
                data = output_data(item["Q"])
                M, N, alpha, beta = degree_four_forms(r, y, z)
                assert Fraction(data["b_numerator"],
                                data["b_denominator"] * data["a"]) == Fraction(N, 420*M*M)
                assert data["primitive_pair"] == [alpha, beta]

    mp.mp.dps = 60
    z0 = 1 - 2j
    phi = z0 + mp.sqrt(z0*z0 - 1)
    if abs(phi) < 1:
        phi = z0 - mp.sqrt(z0*z0 - 1)
    C = abs(phi)

    result = {
        "status": "exact identities verified; finite searches are diagnostics only",
        "orthogonality_checked_through_degree": 12,
        "parameterization_samples": parameter_checks,
        "degree_two": degree_two,
        "degree_three_search": degree_three_search(500),
        "degree_four_search": degree_four_search(50),
        "sparse_records": sparse_degree_records(16),
        "bernstein_walsh_C": mp.nstr(C, 50),
        "analytic_lower_bound": "I(Q)/m^2 >= 3/(16*n^2*C^(2*n))",
        "scope": "No all-degree gcd bound and no irrationality/transcendence conclusion.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
