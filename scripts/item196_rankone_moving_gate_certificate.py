#!/usr/bin/env python3
"""Exact certificate for Item 196's all-moving rank-one first gates."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item196_rankone_moving_gate_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item196_rankone_moving_gate_certificate.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dependency_dir() -> Path:
    names = (
        "item175_fixed_band_certificate.py",
        "item178_minimal_parity_certificate.py",
    )
    candidates = (HERE, HERE.parent / "scripts")
    for candidate in candidates:
        if all((candidate / name).is_file() for name in names):
            return candidate
    raise FileNotFoundError(
        "cannot resolve Item175/178 helpers beside the checker or in archived scripts/"
    )


DEPENDENCY_DIR = dependency_dir()
ITEM175_PATH = DEPENDENCY_DIR / "item175_fixed_band_certificate.py"
ITEM178_PATH = DEPENDENCY_DIR / "item178_minimal_parity_certificate.py"
I175 = load_module("item175_for_item196", ITEM175_PATH)
I178 = load_module("item178_for_item196", ITEM178_PATH)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * max(len(left), len(right))
    for index in range(len(answer)):
        if index < len(left):
            answer[index] += left[index]
        if index < len(right):
            answer[index] += right[index]
    return poly_trim(answer)


def poly_scale(poly: list[Fraction], scalar: int | Fraction) -> list[Fraction]:
    return poly_trim([Fraction(scalar) * value for value in poly])


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            answer[first + second] += left_value * right_value
    return poly_trim(answer)


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


def poly_substitute_one_minus(poly: list[Fraction]) -> list[Fraction]:
    """Return poly(1-y), low degree first in y."""
    answer = [Fraction(0)]
    for degree, coefficient in enumerate(poly):
        term = [coefficient * math.comb(degree, power) * ((-1) ** power) for power in range(degree + 1)]
        answer = poly_add(answer, term)
    return answer


def series_product_coefficient(poly: list[Fraction], exponent: int, degree: int) -> Fraction:
    """Coefficient of poly(x)*(1-x)^(-exponent) at x^degree."""
    return sum(
        poly[index] * math.comb(exponent + degree - index - 1, degree - index)
        for index in range(min(degree, len(poly) - 1) + 1)
    )


def gamma_coefficient(s_value: int, q_exponent: int) -> int:
    k_value = 3 * s_value + 2
    q_power = poly_pow([Fraction(1)] * 4, q_exponent)
    answer = series_product_coefficient(q_power, k_value + 1, k_value)
    if answer.denominator != 1:
        raise AssertionError(answer)
    return answer.numerator


def primitive_data(s_value: int) -> dict[str, Any]:
    k_value = 3 * s_value + 2
    gamma0 = gamma_coefficient(s_value, 2 * s_value + 1)
    gamma1 = gamma_coefficient(s_value, 2 * s_value)
    target = poly_mul(
        poly_pow([Fraction(1)] * 4, 2 * s_value),
        [Fraction(gamma1 - gamma0), Fraction(gamma1), Fraction(gamma1), Fraction(gamma1)],
    )

    # Solve u B' - k u' B = target from the top coefficient down.
    b_degree = 2 * k_value - 2
    b_poly = [Fraction(0)] * (b_degree + 1)
    for power in range(b_degree + 1, 0, -1):
        next_value = b_poly[power] if power <= b_degree else Fraction(0)
        target_value = target[power] if power < len(target) else Fraction(0)
        b_poly[power - 1] = (
            target_value - (power - k_value) * next_value
        ) / Fraction(2 * k_value - power + 1)
    if -k_value * b_poly[0] != target[0]:
        raise AssertionError((s_value, b_poly[0], target[0]))

    u = [Fraction(0), Fraction(1), Fraction(-1)]
    u_prime = [Fraction(1), Fraction(-2)]
    left = poly_add(
        poly_mul(u, poly_derivative(b_poly)),
        poly_scale(poly_mul(u_prime, b_poly), -k_value),
    )
    if left != target:
        raise AssertionError((s_value, left, target))
    if len(b_poly) - 1 != 2 * k_value - 2 or b_poly[-1] != Fraction(gamma1, 2):
        raise AssertionError((s_value, len(b_poly) - 1, b_poly[-1], gamma1))

    # Principal parts of target/u^(k+1) at 0 and 1.
    target_at_one_minus = poly_substitute_one_minus(target)
    a_values = [Fraction(0)] * (k_value + 2)
    b_values = [Fraction(0)] * (k_value + 2)
    for order in range(1, k_value + 2):
        degree = k_value + 1 - order
        a_values[order] = series_product_coefficient(target, k_value + 1, degree)
        b_values[order] = series_product_coefficient(target_at_one_minus, k_value + 1, degree)
    if a_values[1] != 0 or b_values[1] != 0:
        raise AssertionError((s_value, a_values[1], b_values[1]))

    lcm_k = math.lcm(*range(1, k_value + 1))
    if any((lcm_k * coefficient).denominator != 1 for coefficient in b_poly):
        raise AssertionError((s_value, lcm_k))

    gamma0_four = I175.four_section_exact(-5 * s_value - 4, 2 * s_value + 1, k_value)
    gamma1_four = I175.four_section_exact(-5 * s_value - 3, 2 * s_value, k_value)
    if (gamma0, gamma1) != (gamma0_four, gamma1_four):
        raise AssertionError((s_value, gamma0, gamma1, gamma0_four, gamma1_four))

    return {
        "s": s_value,
        "k": k_value,
        "gamma0": gamma0,
        "gamma1": gamma1,
        "target": target,
        "B": b_poly,
        "principal_at_zero": a_values,
        "principal_at_one": b_values,
        "lcm_k": lcm_k,
    }


def gaussian_eval(poly: list[Fraction], value):
    answer = I175.ZERO
    for coefficient in reversed(poly):
        answer = I175.gadd(I175.gmul(answer, value), I175.g(coefficient))
    return answer


def normalized_primitive_eval(data: dict[str, Any], value):
    """Evaluate G_s, the primitive of H_s/u^(k+1) vanishing at infinity."""
    answer = I175.ZERO
    one_minus = I175.gsub(I175.ONE, value)
    for order in range(2, data["k"] + 2):
        denominator = Fraction(1, order - 1)
        first = I175.gscale(
            I175.gpow(value, 1 - order),
            -data["principal_at_zero"][order] * denominator,
        )
        second = I175.gscale(
            I175.gpow(one_minus, 1 - order),
            data["principal_at_one"][order] * denominator,
        )
        answer = I175.gadd(answer, I175.gadd(first, second))
    return answer


def sigma(value, rho: int):
    return value if rho == 1 else (value[0], -value[1])


ROOTS = (("-1", I175.g(-1)), ("i", I175.I), ("-i", I175.gneg(I175.I)))


def moving_values(data: dict[str, Any], rho: int) -> dict[str, Any]:
    answer = {}
    for name, root in ROOTS:
        conjugate_root = sigma(root, rho)
        u_root = I175.gmul(root, I175.gsub(I175.ONE, root))
        g_value = normalized_primitive_eval(data, conjugate_root)
        answer[name] = I175.gmul(u_root, g_value)

        # Independent B_s/u^k evaluation of the same rational map.
        u_conjugate = I175.gmul(conjugate_root, I175.gsub(I175.ONE, conjugate_root))
        via_b = I175.gmul(
            u_root,
            I175.gmul(
                I175.gpow(u_conjugate, -data["k"]),
                gaussian_eval(data["B"], conjugate_root),
            ),
        )
        if answer[name] != via_b:
            raise AssertionError((data["s"], rho, name, answer[name], via_b))
    return answer


def gate_constant(j_value: int, data: dict[str, Any], rho: int, gate: str) -> Fraction:
    base = I175.coordinates(j_value)
    values = moving_values(data, rho)
    pair = (0, 1) if gate == "A0" else (2, 1)
    total = I175.ZERO
    for name, root in ROOTS:
        weight = I175.wedge(base, I175.coordinates(j_value, root), *pair)
        total = I175.gadd(
            total,
            I175.gscale(I175.gmul(values[name], weight), -(2 * j_value + 2)),
        )
    if total[1] != 0:
        raise AssertionError((j_value, data["s"], rho, gate, total))
    value = total[0]
    if gate == "B0" and rho == 3:
        value = -value
    return value


def reduce_fraction(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise AssertionError((value, prime))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def numerator_and_m_vector(values: dict[str, Any]) -> tuple[list[Fraction], list[Fraction]]:
    a_value, b_value, c_value = values["-1"], values["i"], values["-i"]
    numerator_gaussian = [
        I175.gadd(a_value, I175.gadd(I175.gmul(b_value, I175.I), I175.gmul(c_value, I175.gneg(I175.I)))),
        I175.gadd(I175.gmul(b_value, I175.gadd(I175.ONE, I175.I)), I175.gmul(c_value, I175.gsub(I175.ONE, I175.I))),
        I175.gadd(a_value, I175.gadd(b_value, c_value)),
    ]
    if any(value[1] for value in numerator_gaussian):
        raise AssertionError(numerator_gaussian)
    numerator = [value[0] for value in numerator_gaussian]
    return numerator, I178.derive_m_vector(numerator)


def certificate(max_s: int) -> dict[str, Any]:
    digest = hashlib.sha256()
    checkpoints = []
    data_by_s = {}
    for s_value in range(max_s + 1):
        data = primitive_data(s_value)
        data_by_s[s_value] = data
        for rho in (1, 3):
            values = moving_values(data, rho)
            numerator, m_vector = numerator_and_m_vector(values)
            row = (
                s_value,
                rho,
                data["gamma0"],
                data["gamma1"],
                tuple(ftext(value) for value in numerator),
                tuple(ftext(value) for value in m_vector),
            )
            digest.update((repr(row) + "\n").encode("ascii"))
            if s_value in {0, 1, 2, 3, max_s}:
                checkpoints.append(
                    {
                        "s": s_value,
                        "rho": rho,
                        "gamma": [data["gamma0"], data["gamma1"]],
                        "N_coefficients": [ftext(value) for value in numerator],
                        "M_coefficients": [ftext(value) for value in m_vector],
                    }
                )

    expected_constants = {
        (1, 1, 1, "B0"): Fraction(2735, 4),
        (1, 1, 3, "B0"): Fraction(-5295, 4),
        (2, 0, 1, "B0"): Fraction(-918897, 128),
        (2, 0, 3, "B0"): Fraction(59829, 128),
        (1, 3, 1, "B0"): Fraction(-2213120, 33),
        (1, 3, 3, "B0"): Fraction(8439040, 33),
        (2, 2, 1, "B0"): Fraction(8513771, 16),
        (2, 2, 3, "B0"): Fraction(-3277547, 16),
    }
    constants = []
    for key, expected in expected_constants.items():
        j_value, s_value, rho, gate = key
        actual = gate_constant(j_value, data_by_s[s_value], rho, gate)
        if actual != expected:
            raise AssertionError((key, actual, expected))
        constants.append({"j": j_value, "s": s_value, "rho": rho, gate: ftext(actual)})

    controls_expected = {
        (1, 15, 107): (0, 50),
        (3, 15, 107): (65, 73),
        (1, 3, 19): (0, 0),
        (3, 3, 19): (0, 0),
    }
    controls = []
    for (j_value, s_value, prime), expected in controls_expected.items():
        if s_value not in data_by_s:
            data_by_s[s_value] = primitive_data(s_value)
        rho = prime % 4
        a0 = reduce_fraction(gate_constant(j_value, data_by_s[s_value], rho, "A0"), prime)
        b0 = reduce_fraction(gate_constant(j_value, data_by_s[s_value], rho, "B0"), prime)
        if (a0, b0) != expected:
            raise AssertionError((j_value, s_value, prime, a0, b0, expected))
        controls.append({"j": j_value, "s": s_value, "p": prime, "A0": a0, "B0": b0})

    witness_a = gate_constant(1, data_by_s[3], 1, "A0")
    witness_b = gate_constant(1, data_by_s[3], 1, "B0")
    if witness_a != Fraction(2607104, 99) or witness_b != Fraction(-2213120, 33):
        raise AssertionError((witness_a, witness_b))
    if reduce_fraction(witness_a, 13) != 4 or reduce_fraction(witness_b, 13) != 0:
        raise AssertionError((witness_a, witness_b))

    c_near = math.log(432) - math.sqrt(3) * math.pi - Fraction(2, 5)
    c_far = -math.log(16) - Fraction(3, 5) + 2 * math.pi / math.sqrt(3)
    c_total = -1 - math.pi / math.sqrt(3) + 3 * math.log(3)
    if abs(float(c_near + c_far) - c_total) > 1e-14:
        raise AssertionError((c_near, c_far, c_total))

    return {
        "item": 196,
        "arithmetic": "exact rational/Gaussian arithmetic; transcendental capacity constants evaluated in binary64",
        "dependencies": {
            "scripts/item175_fixed_band_certificate.py": sha256(ITEM175_PATH),
            "scripts/item178_minimal_parity_certificate.py": sha256(ITEM178_PATH),
        },
        "proved_formula_replay": {
            "max_s": max_s,
            "checks": [
                "two coefficient forms for gamma_0,gamma_1",
                "u*B'-k*u'*B=H",
                "degree(B)=2k-2 and leading(B)=gamma_1/2",
                "lcm(1,...,k)*B integral",
                "principal-part G equals B/u^k at all three Q-roots",
                "Cayley numerator and four-coordinate moving map",
            ],
            "stream_sha256": digest.hexdigest(),
            "checkpoints": checkpoints,
        },
        "known_constant_replays": constants,
        "hasse_digit_controls": controls,
        "moving_sign_obstruction_witness": {
            "row": {"m": 11, "p": 13, "j": 1, "s": 3, "rho": 1},
            "rational_A0": ftext(witness_a),
            "rational_B0": ftext(witness_b),
            "mod_13": {"A0": 4, "B0": 0},
            "point": "the nonzero rational B0 constant is divisible by the moving prime",
        },
        "PNT_capacity_per_m": {
            "near_s_over_p_below_1_over_6": float(c_near),
            "far_s_over_p_at_least_1_over_6": float(c_far),
            "total_kappa_1": c_total,
            "one_extra_layer_far_per_6m": float(c_far) / 6,
            "one_extra_layer_total_per_6m": c_total / 6,
        },
        "verdict": (
            "PROVED the all-moving rational primitive and exact A0/B0 map; "
            "PROVED a scoped obstruction to fixed-s sign arguments; no moving zero-count theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=24)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_s)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "verdict": result["verdict"],
                "stream_sha256": result["proved_formula_replay"]["stream_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
