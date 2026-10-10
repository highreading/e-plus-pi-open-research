#!/usr/bin/env python3
"""Exact certificate for Item 181's next parity-compatible layer."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item181_next_layer_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item181_next_layer_certificate.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


I175 = load_module("item175_for_item181", HERE / "item175_fixed_band_certificate.py")
I178 = load_module("item178_for_item181", HERE / "item178_minimal_parity_certificate.py")


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * max(len(left), len(right))
    for index in range(len(answer)):
        if index < len(left):
            answer[index] += left[index]
        if index < len(right):
            answer[index] += right[index]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def poly_scale(poly: list[Fraction], scalar: int | Fraction) -> list[Fraction]:
    return [Fraction(scalar) * value for value in poly]


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            answer[first + second] += left_value * right_value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def poly_pow(base: list[Fraction], exponent: int) -> list[Fraction]:
    answer = [Fraction(1)]
    while exponent:
        if exponent & 1:
            answer = poly_mul(answer, base)
        exponent >>= 1
        if exponent:
            base = poly_mul(base, base)
    return answer


def poly_derivative(poly: list[Fraction]) -> list[Fraction]:
    return [index * poly[index] for index in range(1, len(poly))] or [Fraction(0)]


def primitive_data(s_value: int) -> dict[str, Any]:
    degree = 3 * s_value + 2
    gamma0 = I175.four_section_exact(-5 * s_value - 4, 2 * s_value + 1, degree)
    gamma1 = I175.four_section_exact(-5 * s_value - 3, 2 * s_value, degree)
    q_poly = [Fraction(1)] * 4
    target = poly_mul(
        poly_pow(q_poly, 2 * s_value),
        [Fraction(gamma1 - gamma0), Fraction(gamma1), Fraction(gamma1), Fraction(gamma1)],
    )
    b_degree = 6 * s_value + 2
    b_poly = [Fraction(0)] * (b_degree + 1)
    resonance = 3 * s_value + 2
    for power in range(b_degree + 1, 0, -1):
        next_value = b_poly[power] if power <= b_degree else 0
        target_value = target[power] if power < len(target) else 0
        b_poly[power - 1] = (
            target_value - (power - resonance) * next_value
        ) / Fraction(2 * resonance - power + 1)
    if -resonance * b_poly[0] != target[0]:
        raise AssertionError((s_value, b_poly[0], target[0]))

    u = [Fraction(0), Fraction(1), Fraction(-1)]
    u_prime = [Fraction(1), Fraction(-2)]
    left = poly_add(
        poly_mul(u, poly_derivative(b_poly)),
        poly_scale(poly_mul(u_prime, b_poly), -resonance),
    )
    if left != target:
        raise AssertionError((s_value, left, target))
    return {
        "s": s_value,
        "gamma0": gamma0,
        "gamma1": gamma1,
        "B": b_poly,
        "identity_verified": True,
    }


def gaussian_eval(poly: list[Fraction], value):
    answer = I175.ZERO
    for coefficient in reversed(poly):
        answer = I175.gadd(I175.gmul(answer, value), I175.g(coefficient))
    return answer


def constrained_values(data: dict[str, Any], rho: int) -> dict[str, Any]:
    s_value = data["s"]
    exponent_shift = 3 * s_value + 2
    answer = {}
    for name, root in (("-1", I175.g(-1)), ("i", I175.I), ("-i", I175.gneg(I175.I))):
        frobenius_root = root if rho == 1 else (root[0], -root[1])
        u_root = I175.gmul(root, I175.gsub(I175.ONE, root))
        u_frobenius = I175.gmul(frobenius_root, I175.gsub(I175.ONE, frobenius_root))
        power = I175.gmul(u_frobenius, I175.gpow(u_root, -exponent_shift))
        value = I175.gmul(power, gaussian_eval(data["B"], root))
        answer[name] = value if rho == 1 else (value[0], -value[1])
    return answer


def numerator_from_values(values: dict[str, Any]) -> list[Fraction]:
    a_value, b_value, c_value = values["-1"], values["i"], values["-i"]
    # N=a(x^2+1)+b(x+1)(x+i)+c(x+1)(x-i).
    coefficients = [
        I175.gadd(a_value, I175.gadd(I175.gmul(b_value, I175.I), I175.gmul(c_value, I175.gneg(I175.I)))),
        I175.gadd(I175.gmul(b_value, I175.gadd(I175.ONE, I175.I)), I175.gmul(c_value, I175.gsub(I175.ONE, I175.I))),
        I175.gadd(a_value, I175.gadd(b_value, c_value)),
    ]
    if any(value[1] for value in coefficients):
        raise AssertionError(coefficients)
    return [value[0] for value in coefficients]


EXPECTED_M = {
    (2, 1): [-490880, -728128, -359944, -59300],
    (2, 3): [-507264, -769088, -392712, -67492],
    (3, 1): [334361088, 502786816, 252560768, 42378816],
    (3, 3): [331870720, 496560896, 247580032, 41133632],
}
CLEARING = {2: 21, 3: 165}


def actual_constant(j: int, values: dict[str, Any]) -> Fraction:
    base = I175.coordinates(j)
    total = I175.ZERO
    for name, divisor in (("-1", I175.g(-1)), ("i", I175.I), ("-i", I175.gneg(I175.I))):
        weight = I175.wedge(base, I175.coordinates(j, divisor), 2, 1)
        total = I175.gadd(total, I175.gscale(I175.gmul(values[name], weight), -(2 * j + 2)))
    if total[1]:
        raise AssertionError(total)
    return total[0]


def scan(max_j: int, vectors: dict[tuple[int, int], list[int]]) -> dict[str, Any]:
    delta = [2, 4, 3, 1]
    delta2 = I178.polynomial_multiply(delta, delta)
    polynomial = I178.polynomial_power(delta, 4)
    polynomial_minus_one = I178.polynomial_power(delta, 3)
    digest = hashlib.sha256()
    checkpoints = []
    failures = []
    for j in range(1, max_j + 1):
        if j > 1:
            polynomial = I178.polynomial_multiply(polynomial, delta2)
            polynomial_minus_one = I178.polynomial_multiply(polynomial_minus_one, delta2)
        a_value, k_value = 3 * j + 2, 2 * j + 2
        p2, p3, p4 = (polynomial[a_value + offset] for offset in (2, 3, 4))
        q_vector = [2 * (a_value + 1), 4 * (a_value + 1 - k_value), 3 * (a_value + 1 - 2 * k_value), a_value + 1 - 3 * k_value]
        c_vector = [0, -2 * (a_value + 2) * p2, -(4 * (a_value + 2 - k_value) * p2 + 2 * (a_value + 3) * p3), -(3 * (a_value + 2 - 2 * k_value) * p2 + 4 * (a_value + 3 - k_value) * p3 + 2 * (a_value + 4) * p4)]
        n_value, target = j + 1, 3 * (j + 1) + 3
        left = polynomial_minus_one[target - 5]
        right = polynomial_minus_one[target - 4]
        s_value = 3 if j & 1 else 2
        if j & 1:
            braces = {1: (15 * j + 12) * p2 + (-23 * j - 33) * p3 + (6 * j + 12) * p4, 3: (15 * j + 12) * p2 + (17 * j - 9) * p3 - (42 * j + 84) * p4}
            reduced = {1: 2 * n_value * (3 * left - right), 3: n_value * (14 * right + 6 * left)}
            scale = 1245184
        else:
            braces = {1: -(1265 * j + 1012) * p2 + (-1027 * j + 1003) * p3 + (3054 * j + 6108) * p4, 3: -(1265 * j + 1012) * p2 + (1533 * j + 2539) * p3 - (18 * j + 36) * p4}
            reduced = {1: -n_value * (1018 * right + 506 * left), 3: n_value * (6 * right - 506 * left)}
            scale = 128
        if braces != reduced or left <= right:
            failures.append([j, "Euler/central", braces, reduced])
        expected_sign = 1 if j & 1 else -1
        for rho in (1, 3):
            omega = I178.determinant([q_vector, c_vector, [2, 4, 3, 1], vectors[(s_value, rho)]])
            expected = scale * (j + 1) * braces[rho]
            if omega != expected or ((omega > 0) - (omega < 0)) != expected_sign:
                failures.append([j, rho, omega, expected])
            digest.update(f"{j},{rho},{omega}\n".encode("ascii"))
        if j <= 6 or j in (20, 100, 250, 500, max_j):
            checkpoints.append({"j": j, "s": s_value, "left_minus_right": str(left - right), "brace_rho1": str(braces[1]), "brace_rho3": str(braces[3])})
    if failures:
        raise AssertionError(failures[:5])
    return {"max_j": max_j, "failures": failures, "stream_sha256": digest.hexdigest(), "checkpoints": checkpoints}


def certificate(max_j: int) -> dict[str, Any]:
    primitives = {s: primitive_data(s) for s in (2, 3)}
    vectors = {}
    value_rows = []
    for s_value in (2, 3):
        for rho in (1, 3):
            values = constrained_values(primitives[s_value], rho)
            numerator = numerator_from_values(values)
            m_vector = I178.derive_m_vector(numerator)
            cleared = [value * CLEARING[s_value] for value in m_vector]
            if any(value.denominator != 1 for value in cleared):
                raise AssertionError(cleared)
            vectors[(s_value, rho)] = [value.numerator for value in cleared]
            if vectors[(s_value, rho)] != EXPECTED_M[(s_value, rho)]:
                raise AssertionError((s_value, rho, vectors[(s_value, rho)]))
            value_rows.append({"s": s_value, "rho": rho, "N_coefficients": [ftext(value) for value in numerator], "M_sharp_t_coefficients": vectors[(s_value, rho)]})
    samples = []
    expected_samples = {(1, 1): Fraction(-2213120, 33), (1, 3): Fraction(8439040, 33), (2, 1): Fraction(8513771, 16), (2, 3): Fraction(-3277547, 16)}
    for j, s_value in ((1, 3), (2, 2)):
        for rho in (1, 3):
            raw = actual_constant(j, constrained_values(primitives[s_value], rho))
            actual = (1 if rho == 1 else -1) * raw
            if actual != expected_samples[(j, rho)]:
                raise AssertionError((j, rho, actual))
            samples.append({"j": j, "s": s_value, "rho": rho, "B0": ftext(actual)})
    replay = scan(max_j, vectors)
    return {
        "item": 181,
        "arithmetic": "exact rational/integer arithmetic; no prime scan",
        "gamma_reductions": {str(s): [primitives[s]["gamma0"], primitives[s]["gamma1"]] for s in (2, 3)},
        "primitive_B_coefficients": {str(s): [ftext(value) for value in primitives[s]["B"]] for s in (2, 3)},
        "value_rows": value_rows,
        "all_j_theorem": {
            "sign": "sign(Omega_sharp)=(-1)^(j+1) for rho=1,3 and every j>=1",
            "Euler_reductions": {"odd,rho=1": "2n(3a_left-a_right)", "odd,rho=3": "n(14a_right+6a_left)", "even,rho=1": "-n(1018a_right+506a_left)", "even,rho=3": "n(6a_right-506a_left)"},
            "central_fact": "a_left>a_right by the Item178 binomial decomposition of Delta^(2n-1)",
            "consequence": "actual next-layer constrained B0 is nonzero over Q for every fixed j and both rho classes",
        },
        "fixed_m_scope": {"even_j": "p divides 2m+3", "odd_j": "p divides 2m+4", "log_weight_bound": "log((2m+3)(2m+4))=O(log m)"},
        "sample_constants": samples,
        "finite_replay_only": replay,
        "verdict": f"PROVED all-j next-layer nonidentity; exact replay through j={max_j}.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-j", type=int, default=500)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_j)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "verdict": result["verdict"], "stream_sha256": result["finite_replay_only"]["stream_sha256"]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
