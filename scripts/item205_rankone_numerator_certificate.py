#!/usr/bin/env python3
"""Exact certificate for Item 205's rank-one moving-content reduction.

The all-s statements are proved in the companion report.  Every bounded
loop in this checker is explicitly reported as a FINITE audit.
"""

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
    HERE / "item205_rankone_numerator_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item205_rankone_numerator_certificate.json"
)


def locate(name: str) -> Path:
    for candidate in (HERE / name, HERE.parent / "scripts" / name):
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(name)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


ITEM196_PATH = locate("item196_rankone_moving_gate_certificate.py")
I196 = load_module("item196_for_item205", ITEM196_PATH)


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def primes_through(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def strip_primes_through(value: int, limit: int) -> int:
    answer = abs(value)
    for prime in primes_through(limit):
        while answer % prime == 0:
            answer //= prime
    return answer


def moving_integer_vector(data: dict[str, Any]) -> tuple[int, int, int, int]:
    """Return (X,Y,Z,h) for Lambda*(a,b,c), with Lambda p-unit for p>k."""
    values = I196.moving_values(data, 1)
    a_value = values["-1"][0]
    b_value, c_value = values["i"]
    scale = (2 ** (data["k"] - 1)) * data["lcm_k"]
    scaled = [scale * value for value in (a_value, b_value, c_value)]
    if any(value.denominator != 1 for value in scaled):
        raise AssertionError((data["s"], scale, scaled))
    integers = tuple(value.numerator for value in scaled)
    content = math.gcd(*(abs(value) for value in integers))
    return integers[0], integers[1], integers[2], content


def rho_swap_check(data: dict[str, Any]) -> None:
    first = I196.moving_values(data, 1)
    third = I196.moving_values(data, 3)
    a_value = first["-1"][0]
    b_value, c_value = first["i"]
    expected = {
        "-1": (a_value, Fraction(0)),
        "i": (c_value, b_value),
        "-i": (c_value, -b_value),
    }
    if third != expected:
        raise AssertionError((data["s"], third, expected))


def coefficient_recurrence(s_value: int) -> list[int]:
    """Coefficients A_n through n=k from the exact four-term recurrence."""
    k_value = 3 * s_value + 2
    coefficients: list[int] = []

    def get(index: int) -> int:
        return coefficients[index] if 0 <= index < len(coefficients) else 0

    coefficients.append(1)
    for n_value in range(k_value):
        numerator = (5 * s_value + 3) * (
            get(n_value) + get(n_value - 1) + get(n_value - 2)
        ) + (n_value - 3 * s_value) * get(n_value - 3)
        quotient, remainder = divmod(numerator, n_value + 1)
        if remainder:
            raise AssertionError((s_value, n_value, numerator, n_value + 1))
        coefficients.append(quotient)
    return coefficients


def height_envelope_countermodel(prime: int) -> dict[str, int]:
    """A scoped countermodel showing that the proved height bound alone is inert."""
    if not is_prime(prime):
        raise ValueError(prime)
    max_s = (prime - 3) // 3
    first_s = 0
    while prime > 4 ** (5 * first_s + 2):
        first_s += 1
    roots = max_s - first_s + 1
    if roots <= 0:
        raise AssertionError((prime, max_s, first_s))
    for s_value in range(first_s, max_s + 1):
        if prime > 4 ** (5 * s_value + 2):
            raise AssertionError((prime, s_value))
    return {
        "p": prime,
        "admissible_s_count": max_s + 1,
        "first_s_with_p_inside_height_envelope": first_s,
        "mock_common_roots": roots,
    }


def certificate(max_s: int) -> dict[str, Any]:
    if max_s < 15:
        raise ValueError("max_s must be at least 15 to include all frozen witnesses")

    stream = hashlib.sha256()
    checkpoints = []
    observed_large_content = []
    resonance_rows = []
    data_by_s: dict[int, dict[str, Any]] = {}

    for s_value in range(max_s + 1):
        data = I196.primitive_data(s_value)
        data_by_s[s_value] = data
        rho_swap_check(data)
        x_value, y_value, z_value, content = moving_integer_vector(data)
        delta = math.gcd(data["gamma0"], data["gamma1"])
        large_content = strip_primes_through(content, data["k"])
        large_delta = strip_primes_through(delta, data["k"])
        if large_content != large_delta:
            raise AssertionError((s_value, large_content, large_delta))

        recurrence = coefficient_recurrence(s_value)
        k_value = data["k"]
        if recurrence[k_value] != data["gamma1"]:
            raise AssertionError((s_value, recurrence[k_value], data["gamma1"]))
        recurrence_gamma0 = sum(
            recurrence[index] if index >= 0 else 0
            for index in range(k_value - 3, k_value + 1)
        )
        if recurrence_gamma0 != data["gamma0"]:
            raise AssertionError((s_value, recurrence_gamma0, data["gamma0"]))

        singular_steps = [
            n_value
            for n_value in range(k_value)
            if 3 * s_value - n_value == 0
        ]
        if singular_steps != [3 * s_value]:
            raise AssertionError((s_value, singular_steps))

        if data["gamma0"] > 4 ** (5 * s_value + 3):
            raise AssertionError((s_value, "gamma0 height"))
        if data["gamma1"] > 4 ** (5 * s_value + 2):
            raise AssertionError((s_value, "gamma1 height"))

        endpoint = 5 * s_value + 4
        predicted_resonance = s_value % 4 == 3 and is_prime(endpoint)
        expected_large_delta = endpoint if predicted_resonance else 1
        if large_delta != expected_large_delta:
            raise AssertionError(
                (s_value, large_delta, expected_large_delta, "FINITE scan only")
            )
        if large_delta != 1:
            observed_large_content.append({"s": s_value, "p": large_delta})
            if data["gamma0"] % large_delta or data["gamma1"] % large_delta:
                raise AssertionError((s_value, large_delta))
            # Choose j=1; s is odd, so the cell parity is respected.
            j_value = 1
            numerator = (j_value + 1) * large_delta - s_value - 1
            if numerator % 2:
                raise AssertionError((s_value, large_delta, numerator))
            m_value = numerator // 2
            if (10 * m_value + 1) % large_delta:
                raise AssertionError((m_value, large_delta))
            resonance_rows.append(
                {"m": m_value, "p": large_delta, "j": j_value, "s": s_value}
            )

        row = (
            s_value,
            data["gamma0"],
            data["gamma1"],
            x_value,
            y_value,
            z_value,
            content,
            large_content,
        )
        stream.update((repr(row) + "\n").encode("ascii"))
        if s_value in {0, 1, 2, 3, 11, 15, max_s}:
            checkpoints.append(
                {
                    "s": s_value,
                    "k": k_value,
                    "gamma": [data["gamma0"], data["gamma1"]],
                    "integer_vector": [str(x_value), str(y_value), str(z_value)],
                    "content": str(content),
                    "large_prime_content": str(large_content),
                }
            )

    # Exact s=3 moving vector and the two arithmetically distinct witnesses.
    data3 = data_by_s[3]
    values3 = I196.moving_values(data3, 1)
    a3 = values3["-1"][0]
    b3, c3 = values3["i"]
    if (a3, b3, c3) != (
        Fraction(20878112, 165),
        Fraction(-312208, 5),
        Fraction(-10458512, 165),
    ):
        raise AssertionError((a3, b3, c3))
    denominator3 = math.lcm(a3.denominator, b3.denominator, c3.denominator)
    raw3 = [int(denominator3 * value) for value in (a3, b3, c3)]
    raw_content3 = math.gcd(*(abs(value) for value in raw3))
    primitive3 = [value // raw_content3 for value in raw3]
    if (denominator3, raw_content3, primitive3) != (
        165,
        304,
        [68678, -33891, -34403],
    ):
        raise AssertionError((denominator3, raw_content3, primitive3))
    delta3 = math.gcd(data3["gamma0"], data3["gamma1"])
    if delta3 != 608:
        raise AssertionError(delta3)

    p13_a = I196.gate_constant(1, data3, 1, "A0")
    p13_b = I196.gate_constant(1, data3, 1, "B0")
    if (p13_a, p13_b) != (Fraction(2607104, 99), Fraction(-2213120, 33)):
        raise AssertionError((p13_a, p13_b))
    if (
        I196.reduce_fraction(p13_a, 13),
        I196.reduce_fraction(p13_b, 13),
    ) != (4, 0):
        raise AssertionError((p13_a, p13_b))
    if delta3 % 13 == 0:
        raise AssertionError("the p=13 witness must survive content removal")

    p19_rows = []
    for j_value in (1, 3):
        a0 = I196.reduce_fraction(I196.gate_constant(j_value, data3, 3, "A0"), 19)
        b0 = I196.reduce_fraction(I196.gate_constant(j_value, data3, 3, "B0"), 19)
        if (a0, b0) != (0, 0):
            raise AssertionError((j_value, a0, b0))
        m_value = ((j_value + 1) * 19 - 3 - 1) // 2
        p19_rows.append({"m": m_value, "p": 19, "j": j_value, "s": 3})

    envelope_models = [height_envelope_countermodel(prime) for prime in (101, 211, 503)]

    return {
        "item": 205,
        "arithmetic": "exact integer/rational/Gaussian arithmetic",
        "dependency": {
            "scripts/item196_rankone_moving_gate_certificate.py": sha256(ITEM196_PATH)
        },
        "proved_all_s_reductions": {
            "rho_swap": "(a,b,c) for rho=1 becomes (a,c,b) for rho=3",
            "canonical_scale": "Lambda_s=2^(k-1)*lcm(1,...,k)",
            "localized_smith_content": (
                "for every odd p>k and e>=1, min(v_p(X),v_p(Y),v_p(Z)) "
                "=min(v_p(gamma_0),v_p(gamma_1))"
            ),
            "coefficient_recurrence": (
                "(n+1)A[n+1]=(5s+3)(A[n]+A[n-1]+A[n-2])+(n-3s)A[n-3]"
            ),
            "transfer_determinant": "det(T_n)=(3s-n)/(n+1), singular exactly at n=3s",
            "terminal_survivor": (
                "common gamma zero leaves t*(A[k],A[k-1],A[k-2],A[k-3],A[k-4])="
                "t*(0,0,-1,1,0)"
            ),
            "height": "gcd(gamma_0,gamma_1)<=gamma_1<=4^(5s+2)",
            "resonance_ray": (
                "s=3 mod 4 and prime p=5s+4 implies p divides both gammas; "
                "on a cell row p divides 10m+1"
            ),
        },
        "finite_audit": {
            "label": "FINITE; no extrapolation beyond max_s",
            "max_s": max_s,
            "stream_sha256": stream.hexdigest(),
            "checkpoints": checkpoints,
            "observed_admissible_large_content": observed_large_content,
            "resonance_rows_with_j_1": resonance_rows,
        },
        "s3_content_witness": {
            "D3": denominator3,
            "D3_times_abc": [str(value) for value in raw3],
            "content": raw_content3,
            "primitive_vector": primitive3,
            "gcd_gamma": delta3,
            "p19_common_gate_rows": p19_rows,
        },
        "primitive_contraction_witness": {
            "row": {"m": 11, "p": 13, "j": 1, "s": 3, "rho": 1},
            "rational_A0": ftext(p13_a),
            "rational_B0": ftext(p13_b),
            "mod_13": {"A0": 4, "B0": 0},
            "13_divides_common_content": False,
        },
        "height_only_countermodels": {
            "scope": (
                "mock common contents obey the proved height envelope only; "
                "they are not claimed to satisfy the actual recurrence"
            ),
            "rows": envelope_models,
        },
        "verdict": (
            "PROVED exact localized common-content reduction and zero-rate resonance overlap; "
            "PROVED height/local-transfer methods do not yield a moving-prime sublinear count; "
            "OPEN primitive A0/B0 zero counts; A1 and joint gates remain separate."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-s", type=int, default=40)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_s)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "stream_sha256": result["finite_audit"]["stream_sha256"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
