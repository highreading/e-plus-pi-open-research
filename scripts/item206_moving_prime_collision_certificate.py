#!/usr/bin/env python3
"""Deterministic exact certificate for Item 206.

The companion report proves the all-j cohomological kernel identity, the
Cartier rank-zero interval, and the regular-rank common-content reduction.
This checker replays those identities with exact rational/Gaussian arithmetic
and labels every bounded scan as FINITE.
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
    HERE / "item206_moving_prime_collision_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item206_moving_prime_collision_certificate.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dependency_dir() -> Path:
    names = (
        "item175_fixed_band_certificate.py",
        "item178_minimal_parity_certificate.py",
        "item196_rankone_moving_gate_certificate.py",
    )
    for candidate in (HERE, HERE.parent / "scripts"):
        if all((candidate / name).is_file() for name in names):
            return candidate
    raise FileNotFoundError("cannot resolve pinned Item 175/178/196 helpers")


DEPENDENCY_DIR = dependency_dir()
ITEM175_PATH = DEPENDENCY_DIR / "item175_fixed_band_certificate.py"
ITEM178_PATH = DEPENDENCY_DIR / "item178_minimal_parity_certificate.py"
ITEM196_PATH = DEPENDENCY_DIR / "item196_rankone_moving_gate_certificate.py"
I175 = load_module("item175_for_item206", ITEM175_PATH)
I196 = load_module("item196_for_item206", ITEM196_PATH)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def real_gate_row(j_value: int, gate: str) -> tuple[Fraction, Fraction, Fraction]:
    """Row acting on (V(-1), Re V(i), Im V(i))."""
    base = I175.coordinates(j_value)
    pair = (0, 1) if gate == "A" else (2, 1)
    weights = {}
    for name, root in (("-1", I175.g(-1)), ("i", I175.I), ("-i", I175.gneg(I175.I))):
        weights[name] = I175.wedge(base, I175.coordinates(j_value, root), *pair)
    if weights["-1"][1] != 0 or weights["-i"] != (weights["i"][0], -weights["i"][1]):
        raise AssertionError((j_value, gate, weights))
    return weights["-1"][0], 2 * weights["i"][0], -2 * weights["i"][1]


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def det3(a, b, c):
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def fraction_mod(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise AssertionError(("nonunit denominator", value, prime))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def row_mod(row, prime: int) -> tuple[int, int, int]:
    return tuple(fraction_mod(value, prime) for value in row)


def rank_two_rows(first, second, prime: int) -> tuple[int, str]:
    a = row_mod(first, prime)
    b = row_mod(second, prime)
    if not any(a) and not any(b):
        return 0, "both_zero"
    minors = (
        a[0] * b[1] - a[1] * b[0],
        a[0] * b[2] - a[2] * b[0],
        a[1] * b[2] - a[2] * b[1],
    )
    if any(value % prime for value in minors):
        return 2, "rank_two"
    if not any(a):
        return 1, "A_zero"
    if not any(b):
        return 1, "B_zero"
    return 1, "nonzero_parallel"


def prime_factors(value: int) -> list[int]:
    value = abs(value)
    answer = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            answer.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        answer.append(value)
    return answer


def primes_up_to(limit: int) -> list[int]:
    answer = []
    for candidate in range(2, limit + 1):
        if all(candidate % q for q in range(2, math.isqrt(candidate) + 1)):
            answer.append(candidate)
    return answer


def poly_add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (left[index] if index < len(left) else 0) + (right[index] if index < len(right) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * value for value in poly]


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def universal_identities() -> dict[str, Any]:
    # u=x(1-x), Q=(x+1)(x^2+1).
    u = [0, 1, -1]
    u_prime = [1, -2]
    q = [1, 1, 1, 1]
    q_prime = [1, 2, 3]
    # 3u'Q-2uQ'-8+5Q=0 gives the all-j differential identity.
    differential = poly_add(
        poly_add(poly_scale(poly_mul(u_prime, q), 3), poly_scale(poly_mul(u, q_prime), -2)),
        poly_add([-8], poly_scale(q, 5)),
    )
    if differential != [0]:
        raise AssertionError(differential)
    # uQ'+4=(4-3x)Q, hence uQ'=-4 mod Q.
    uq_plus_four = poly_add(poly_mul(u, q_prime), [4])
    expected = poly_mul([4, -3], q)
    if uq_plus_four != expected:
        raise AssertionError((uq_plus_four, expected))
    return {
        "partial_fraction_pole_vector": ["2", "-1-i", "-1+i"],
        "real_normal": [2, -1, -1],
        "differential_polynomial_identity_coefficients": differential,
        "uQprime_plus_4_quotient_by_Q": [4, -3],
    }


def q_adic_coefficient_check(max_s: int) -> dict[str, Any]:
    for s_value in range(max_s + 1):
        for a_value, b_value in ((1, 0), (0, 1), (7, -5)):
            expected = [
                -(3 * s_value + 2) * b_value,
                -(3 * s_value + 1) * a_value + (5 * s_value + 3) * b_value,
                (5 * s_value + 3) * (a_value + b_value),
                (5 * s_value + 3) * (a_value + b_value),
                (5 * s_value + 3) * a_value + b_value,
            ]
            # Direct expansion of r*u*Q'*(Ax+B)+Q*(u*A-k*u'*(Ax+B)).
            r_value = 2 * s_value + 1
            k_value = 3 * s_value + 2
            u = [0, 1, -1]
            up = [1, -2]
            q = [1, 1, 1, 1]
            qp = [1, 2, 3]
            linear = [b_value, a_value]
            direct = poly_add(
                poly_scale(poly_mul(poly_mul(u, qp), linear), r_value),
                poly_mul(q, poly_add(poly_scale(u, a_value), poly_scale(poly_mul(up, linear), -k_value))),
            )
            direct += [0] * (5 - len(direct))
            if direct != expected:
                raise AssertionError((s_value, a_value, b_value, direct, expected))
            if expected[2] - expected[1] != 4 * (2 * s_value + 1) * a_value:
                raise AssertionError((s_value, expected))
    return {
        "range": [0, max_s],
        "quotient_coefficient_formula_low_to_high": [
            "-(3s+2)B",
            "-(3s+1)A+(5s+3)B",
            "(5s+3)(A+B)",
            "(5s+3)(A+B)",
            "(5s+3)A+B",
        ],
        "x2_minus_x1": "4(2s+1)A",
    }


def moving_real_vector(data: dict[str, Any], rho: int) -> tuple[Fraction, Fraction, Fraction]:
    values = I196.moving_values(data, rho)
    if values["-1"][1] != 0:
        raise AssertionError(values)
    return values["-1"][0], values["i"][0], values["i"][1]


def line_residual_mod(vector, prime: int) -> tuple[int, int]:
    a, b, c = (fraction_mod(value, prime) for value in vector)
    return (b - c) % prime, (a + 2 * b) % prime


def finite_regular_anchor_audit(max_s: int, prime_cap: int) -> dict[str, Any]:
    tested = 0
    content_rows = []
    for s_value in range(max_s + 1):
        data = I196.primitive_data(s_value)
        j_value = 1 if s_value % 2 else 2
        for prime in primes_up_to(prime_cap):
            if prime <= 3 * s_value + 2 or prime < 2 * j_value + 3:
                continue
            if (s_value, j_value, prime) == (0, 2, 7):
                continue
            arow = real_gate_row(j_value, "A")
            brow = real_gate_row(j_value, "B")
            rank, _ = rank_two_rows(arow, brow, prime)
            if rank != 2:
                raise AssertionError(("anchor rank", s_value, j_value, prime, rank))
            rho = prime % 4
            a0 = I196.reduce_fraction(I196.gate_constant(j_value, data, rho, "A0"), prime)
            b0 = I196.reduce_fraction(I196.gate_constant(j_value, data, rho, "B0"), prime)
            content = data["gamma0"] % prime == 0 and data["gamma1"] % prime == 0
            line = line_residual_mod(moving_real_vector(data, rho), prime) == (0, 0)
            if ((a0 == 0 and b0 == 0) != content) or (line != content):
                raise AssertionError((s_value, j_value, prime, a0, b0, line, content))
            tested += 1
            if content:
                content_rows.append({"s": s_value, "j": j_value, "p": prime})
    return {"label": "FINITE", "max_s": max_s, "prime_cap": prime_cap, "tested": tested, "common_content_rows": content_rows}


def certificate(max_j: int, max_s: int, prime_cap: int) -> dict[str, Any]:
    identities = universal_identities()
    rows = {}
    row_records = []
    for j_value in range(1, max_j + 1):
        arow = real_gate_row(j_value, "A")
        brow = real_gate_row(j_value, "B")
        normal = cross(arow, brow)
        delta = normal[0] / 2
        if normal != (2 * delta, -delta, -delta) or delta == 0:
            raise AssertionError((j_value, normal, delta))
        rows[j_value] = (arow, brow)
        row_records.append({"j": j_value, "delta": ftext(delta)})

    for j_value in range(1, max_j + 1):
        for h_value in range(j_value + 1, max_j + 1):
            for target in rows[h_value]:
                if det3(rows[j_value][0], rows[j_value][1], target) != 0:
                    raise AssertionError((j_value, h_value))

    delta1 = cross(*rows[1])[0] / 2
    delta2 = cross(*rows[2])[0] / 2
    if delta1 != Fraction(125, 6144) or delta2 != Fraction(-343, 30720):
        raise AssertionError((delta1, delta2))

    rank_ledger = []
    for j_value in range(1, max_j + 1):
        delta = cross(*rows[j_value])[0] / 2
        candidates = [p for p in prime_factors(delta.numerator) if p >= 2 * j_value + 3]
        rank_zero = []
        rank_one = []
        for prime in candidates:
            rank, kind = rank_two_rows(*rows[j_value], prime)
            entry = {"p": prime, "kind": kind}
            if rank == 0:
                rank_zero.append(entry)
            elif rank == 1:
                rank_one.append(entry)
            else:
                raise AssertionError((j_value, prime, rank, delta))
        expected_zero = [p for p in primes_up_to(3 * j_value + 2) if p >= 2 * j_value + 3]
        if [entry["p"] for entry in rank_zero] != expected_zero:
            raise AssertionError((j_value, rank_zero, expected_zero))
        rank_ledger.append({"j": j_value, "rank_zero": rank_zero, "rank_one_above_3j_plus_2": rank_one})

    rank_zero_witness_data = I196.primitive_data(1)
    witness_a = I196.gate_constant(3, rank_zero_witness_data, 3, "A0")
    witness_b = I196.gate_constant(3, rank_zero_witness_data, 3, "B0")
    if (witness_a, witness_b) != (Fraction(-150464985, 256), Fraction(-191577969, 128)):
        raise AssertionError((witness_a, witness_b))
    if (I196.reduce_fraction(witness_a, 11), I196.reduce_fraction(witness_b, 11)) != (0, 0):
        raise AssertionError((witness_a, witness_b))
    if (rank_zero_witness_data["gamma0"] % 11, rank_zero_witness_data["gamma1"] % 11) != (6, 6):
        raise AssertionError(rank_zero_witness_data)

    collision_data = I196.primitive_data(3)
    collision = []
    for j_value in (1, 3, 5, 7):
        a0 = I196.reduce_fraction(I196.gate_constant(j_value, collision_data, 3, "A0"), 19)
        b0 = I196.reduce_fraction(I196.gate_constant(j_value, collision_data, 3, "B0"), 19)
        if (a0, b0) != (0, 0):
            raise AssertionError((j_value, a0, b0))
        collision.append({"j": j_value, "m": ((j_value + 1) * 19 - 3 - 1) // 2, "A0": a0, "B0": b0})

    s0 = I196.primitive_data(0)
    vector1 = moving_real_vector(s0, 1)
    vector3 = moving_real_vector(s0, 3)
    if vector1 != (Fraction(-3, 2), Fraction(1, 2), Fraction(3, 2)):
        raise AssertionError(vector1)
    if math.gcd(s0["gamma0"], s0["gamma1"]) != 2:
        raise AssertionError(s0)
    boundary_a = I196.gate_constant(2, s0, 3, "A0")
    boundary_b = I196.gate_constant(2, s0, 3, "B0")
    if (boundary_a, boundary_b) != (Fraction(58737, 320), Fraction(59829, 128)):
        raise AssertionError((boundary_a, boundary_b))
    if (I196.reduce_fraction(boundary_a, 7), I196.reduce_fraction(boundary_b, 7)) != (0, 0):
        raise AssertionError((boundary_a, boundary_b))

    return {
        "item": 206,
        "arithmetic": "exact rational/Gaussian arithmetic; all bounded scans explicitly FINITE",
        "dependencies": {
            "scripts/item175_fixed_band_certificate.py": sha256(ITEM175_PATH),
            "scripts/item178_minimal_parity_certificate.py": sha256(ITEM178_PATH),
            "scripts/item196_rankone_moving_gate_certificate.py": sha256(ITEM196_PATH),
        },
        "proved_identity_replay": identities,
        "proved_regular_rank_reduction": {
            "rank_two_condition": "delta_j is a p-unit",
            "joint_gate_equivalence": "A0=B0=0 iff p divides gcd(gamma_0(s),gamma_1(s))",
            "odd_s_anchor": {"j": 1, "delta": ftext(delta1), "only_numerator_prime": 5},
            "even_s_anchor": {"j": 2, "delta": ftext(delta2), "only_numerator_prime": 7},
            "s_zero_vectors_rho_1_rho_3": [
                [ftext(value) for value in vector1],
                [ftext(value) for value in vector3],
            ],
            "s_zero_gamma_gcd": 2,
            "s_zero_rank_zero_boundary": {
                "row": {"j": 2, "p": 7, "s": 0, "m": 10},
                "rational_gates": [ftext(boundary_a), ftext(boundary_b)],
                "mod_7": [0, 0],
            },
            "Q_adic_coefficient_replay": q_adic_coefficient_check(max_s),
        },
        "proved_rank_zero_interval": {
            "condition": "2j+3 <= p <= 3j+2",
            "Cartier_numerator_degrees": {"base": "p-2", "one_Q_pole_divisor": "p-3"},
            "capacity_bound": "p^2 <= 6m, hence total log-prime weight O(sqrt(m))",
            "primitive_joint_zero_witness": {
                "row": {"j": 3, "p": 11, "s": 1, "m": 21},
                "rational_A0": ftext(witness_a),
                "rational_B0": ftext(witness_b),
                "mod_11": [0, 0],
                "gamma_mod_11": [6, 6],
            },
        },
        "maximal_collision_witness": {
            "p": 19,
            "s": 3,
            "gamma_mod_19": [collision_data["gamma0"] % 19, collision_data["gamma1"] % 19],
            "admissible_rows": collision,
        },
        "finite_cross_row_audit": {"label": "FINITE", "max_j": max_j, "rows": row_records, "all_cross_j_determinants_zero": True},
        "finite_rank_drop_ledger": {"label": "FINITE", "max_j": max_j, "rows": rank_ledger},
        "finite_regular_anchor_audit": finite_regular_anchor_audit(max_s, prime_cap),
        "verdict": (
            "PROVED the universal all-j kernel and identically zero cross-j eliminants; "
            "PROVED regular-rank joint gates equal common moving content; PROVED the automatic "
            "rank-zero interval has zero rate; rank-one determinant divisors and common-content "
            "moving zeros remain open, so no positive missing rate is claimed."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-j", type=int, default=12)
    parser.add_argument("--max-s", type=int, default=12)
    parser.add_argument("--prime-cap", type=int, default=211)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_j, args.max_s, args.prime_cap)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "verdict": result["verdict"]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
