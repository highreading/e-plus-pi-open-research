#!/usr/bin/env python3
"""Exact certificate for Item 210's rank-one endpoint-weight anchors.

All unbounded statements in the companion report are proved algebraically.
The row and diagonal scans in this file are explicitly labelled FINITE.
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from functools import cache
from fractions import Fraction
from pathlib import Path
from typing import Any


sys.set_int_max_str_digits(1_000_000)
HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item210_rankone_anchor_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item210_rankone_anchor_certificate.json"
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


ITEM175_PATH = locate("item175_fixed_band_certificate.py")
ITEM196_PATH = locate("item196_rankone_moving_gate_certificate.py")
I175 = load_module("item175_for_item210", ITEM175_PATH)
I196 = load_module("item196_for_item210", ITEM196_PATH)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@cache
def coordinate(j_value: int, name: str):
    roots = {
        "base": None,
        "-1": I175.g(-1),
        "i": I175.I,
        "-i": I175.gneg(I175.I),
    }
    return I175.coordinates(j_value, roots[name])


@cache
def real_gate_row(j_value: int, gate: str) -> tuple[Fraction, Fraction, Fraction]:
    base = coordinate(j_value, "base")
    pair = (0, 1) if gate == "A" else (2, 1)
    weights = {
        name: I175.wedge(base, coordinate(j_value, name), *pair)
        for name in ("-1", "i", "-i")
    }
    if weights["-1"][1] or weights["-i"] != (weights["i"][0], -weights["i"][1]):
        raise AssertionError((j_value, gate, weights))
    return weights["-1"][0], 2 * weights["i"][0], -2 * weights["i"][1]


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def determinant3(a, b, c):
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def integer_profile(row: tuple[Fraction, ...]) -> dict[str, Any]:
    denominator = math.lcm(*(value.denominator for value in row))
    integers = tuple(value.numerator * (denominator // value.denominator) for value in row)
    content = math.gcd(*(abs(value) for value in integers))
    primitive = tuple(value // content for value in integers)
    if next(value for value in primitive if value) < 0:
        primitive = tuple(-value for value in primitive)
    return {
        "denominator": denominator,
        "content": content,
        "integers": integers,
        "primitive": primitive,
    }


def fraction_mod(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise AssertionError(("nonunit denominator", value, prime))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def row_mod(row, prime: int) -> tuple[int, int, int]:
    return tuple(fraction_mod(value, prime) for value in row)


def row_rank(first, second, prime: int) -> tuple[int, str]:
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


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (((limit - prime * prime) // prime) + 1)
    return [value for value in range(2, limit + 1) if sieve[value]]


def prime_factors(value: int) -> list[int]:
    value = abs(value)
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append(value)
    return factors


def normalized_nonzero_row(row, prime: int) -> list[int]:
    reduced = row_mod(row, prime)
    pivot = next(value for value in reduced if value)
    inverse = pow(pivot, -1, prime)
    return [(value * inverse) % prime for value in reduced]


def ell_direct(j_value: int) -> int:
    """[y^(2j+1)] (y-1)^(3j+2) / (1+y^2)^(2j+2)."""
    return sum(
        (-1) ** (j_value + 1 + t)
        * math.comb(3 * j_value + 2, 2 * j_value + 1 - 2 * t)
        * math.comb(2 * j_value + 1 + t, t)
        for t in range(j_value + 1)
    )


P_COEFFICIENTS = (
    (-11753280, -46086408, -75353094, -66698343, -34568046, -10504404, -1735020, -120285),
    (1621956672, 5897336856, 9019719984, 7528419750, 3706107054, 1076695974, 171005850, 11458260),
    (-52220160, -183220704, -269869776, -216686448, -102607824, -28701648, -4397760, -285120),
    (17579520, 61204608, 89232320, 70702080, 32916800, 9013632, 1345280, 84480),
)


def polynomial_value(coefficients: tuple[int, ...], value: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = answer * value + coefficient
    return answer


def recurrence_coefficients(n_value: int) -> tuple[int, int, int, int]:
    return tuple(polynomial_value(coefficients, n_value) for coefficients in P_COEFFICIENTS)


# N_TABLE[n-degree][y-degree] is the exact telescoping numerator N_n(y).
N_TABLE = (
    (-2511360, 24695040, -111651840, 256897920, -642206784, 1170671328, -1643944224, 2035490304, -1945336896, 1535587968, -1084914816, 465598656, -224488320, 30950304, 5876640, 3917760),
    (-8025984, 78643136, -353686944, 814489664, -2026960904, 3685784868, -5165736812, 6380892640, -6081864648, 4799407840, -3374098432, 1452845832, -693827056, 95836668, 18635724, 11444376),
    (-10454336, 102002208, -455959792, 1050840648, -2601727016, 4717584560, -6597609954, 8126226166, -7724503372, 6090542396, -4261684088, 1840223448, -871234668, 120834420, 23699754, 13673322),
    (-7113344, 69052544, -306556016, 706948136, -1740255666, 3145679797, -4388779968, 5387899155, -5107392512, 4021621550, -2801343620, 1212293778, -569436974, 79346637, 15574356, 8559459),
    (-2670016, 25763232, -113502608, 261833112, -640514110, 1153894897, -1605688332, 1964140295, -1856596472, 1459350646, -1012151164, 438710586, -204598122, 28638441, 5603256, 2963223),
    (-524800, 5027840, -21965200, 50667080, -123120670, 221012735, -306686500, 373716605, -352228120, 276295890, -190838220, 82807110, -38368170, 5392575, 1049760, 538245),
    (-42240, 401280, -1737120, 4004880, -9664050, 17283255, -23912130, 29022675, -27273180, 21345390, -14685660, 6376590, -2937330, 414315, 80190, 40095),
)


# Sparse bivariate polynomials in (n,y), stored as (n_degree,y_degree)->coefficient.
def bp_clean(poly):
    return {key: value for key, value in poly.items() if value}


def bp_add(*polys):
    answer = {}
    for poly in polys:
        for key, value in poly.items():
            answer[key] = answer.get(key, 0) + value
    return bp_clean(answer)


def bp_scale(poly, scalar: int):
    return bp_clean({key: scalar * value for key, value in poly.items()})


def bp_mul(left, right):
    answer = {}
    for (an, ay), av in left.items():
        for (bn, by), bv in right.items():
            key = (an + bn, ay + by)
            answer[key] = answer.get(key, 0) + av * bv
    return bp_clean(answer)


def bp_pow(poly, exponent: int):
    answer = {(0, 0): 1}
    while exponent:
        if exponent & 1:
            answer = bp_mul(answer, poly)
        exponent >>= 1
        if exponent:
            poly = bp_mul(poly, poly)
    return answer


def bp_dy(poly):
    return bp_clean({(dn, dy - 1): dy * value for (dn, dy), value in poly.items() if dy})


def bp_from_y(coefficients):
    return bp_clean({(0, degree): value for degree, value in enumerate(coefficients)})


def bp_from_n(coefficients):
    return bp_clean({(degree, 0): value for degree, value in enumerate(coefficients)})


def telescoper_symbolic_check() -> dict[str, Any]:
    y = bp_from_y((0, 1))
    ym1 = bp_from_y((-1, 1))
    q = bp_from_y((1, 0, 1))
    n1 = bp_from_n((1, 1))
    two_n_plus_two = bp_from_n((2, 2))
    three_n_plus_two = bp_from_n((2, 3))
    four_n_plus_four = bp_from_n((4, 4))
    numerator_n = bp_clean(
        {(n_degree, y_degree): value for n_degree, row in enumerate(N_TABLE) for y_degree, value in enumerate(row)}
    )
    d = bp_mul(bp_pow(y, 5), bp_pow(q, 5))
    u = bp_mul(ym1, numerator_n)
    left = bp_add(
        bp_mul(bp_dy(u), d),
        bp_scale(bp_mul(u, bp_dy(d)), -1),
        bp_mul(bp_mul(d, three_n_plus_two), numerator_n),
        bp_scale(bp_mul(bp_mul(bp_mul(bp_pow(y, 4), bp_pow(q, 5)), two_n_plus_two), u), -1),
        bp_scale(bp_mul(bp_mul(bp_mul(bp_mul(bp_pow(y, 5), bp_pow(q, 4)), n1), y), u), -4),
    )
    base = bp_mul(bp_pow(y, 2), bp_pow(q, 2))
    s_numerator = {}
    for k_value, coefficients in enumerate(P_COEFFICIENTS):
        term = bp_mul(
            bp_from_n(coefficients),
            bp_mul(bp_pow(ym1, 3 * k_value), bp_pow(base, 3 - k_value)),
        )
        s_numerator = bp_add(s_numerator, term)
    right = bp_mul(s_numerator, bp_mul(bp_pow(y, 4), bp_pow(q, 4)))
    defect = bp_add(left, bp_scale(right, -1))
    if defect:
        raise AssertionError((len(defect), sorted(defect.items())[:3]))
    return {
        "identity": "C_n'+C_n(R'/R+nJ'/J)=sum_{k=0}^3 P_k(n)J^k",
        "C_denominator": "y^5(1+y^2)^5",
        "N_degree_in_n": 6,
        "N_degree_in_y": 15,
        "symbolic_defect_terms": 0,
    }


def diagonal_scan(limit: int, direct_check: int) -> dict[str, Any]:
    values = [None, ell_direct(1), ell_direct(2), ell_direct(3)]
    digest = hashlib.sha256()
    for value in values[1:]:
        digest.update(f"{value}\n".encode("ascii"))
    zeros = [index for index in range(1, 4) if values[index] == 0]
    for n_value in range(1, limit - 2):
        p0, p1, p2, p3 = recurrence_coefficients(n_value)
        numerator = -(p0 * values[n_value] + p1 * values[n_value + 1] + p2 * values[n_value + 2])
        quotient, remainder = divmod(numerator, p3)
        if remainder:
            raise AssertionError((n_value, remainder))
        values.append(quotient)
        digest.update(f"{quotient}\n".encode("ascii"))
        if quotient == 0:
            zeros.append(n_value + 3)
    for j_value in range(1, min(limit, direct_check) + 1):
        if values[j_value] != ell_direct(j_value):
            raise AssertionError((j_value, values[j_value], ell_direct(j_value)))
    return {
        "label": "FINITE",
        "range": [1, limit],
        "zeros": zeros,
        "direct_binomial_cross_check_through": min(limit, direct_check),
        "sequence_sha256_newline_decimal": digest.hexdigest(),
        "last_decimal_digits": len(str(abs(values[-1]))),
        "last_mod_2^64": values[-1] % (1 << 64),
        "cell_tail_coefficient_upper_bound": ftext(Fraction(2, 3 * (limit + 1))),
    }


def rank_and_content_audit(max_j: int) -> dict[str, Any]:
    records = []
    for j_value in range(1, max_j + 1):
        arow = real_gate_row(j_value, "A")
        brow = real_gate_row(j_value, "B")
        normal = cross(arow, brow)
        mu = normal[0] / 2
        if normal != (2 * mu, -mu, -mu):
            raise AssertionError((j_value, normal))
        ell = ell_direct(j_value)
        base_l = I175.rational(coordinate(j_value, "base")[1])
        if base_l != Fraction(ell, 1 << j_value):
            raise AssertionError((j_value, base_l, ell))
        a_profile = integer_profile(arow)
        b_profile = integer_profile(brow)
        if any(prime > 2 * j_value + 2 for prime in prime_factors(a_profile["denominator"] * b_profile["denominator"])):
            raise AssertionError(("denominator support", j_value, a_profile, b_profile))
        candidates = [prime for prime in prime_factors(mu.numerator) if prime >= 2 * j_value + 3]
        rank_zero = []
        rank_one = []
        for prime in candidates:
            rank, kind = row_rank(arow, brow, prime)
            entry = {"p": prime, "kind": kind}
            (rank_zero if rank == 0 else rank_one if rank == 1 else []).append(entry)
            if rank == 2:
                raise AssertionError((j_value, prime, mu))
        expected_zero = [
            prime for prime in primes_up_to(3 * j_value + 2) if prime >= 2 * j_value + 3
        ]
        if [entry["p"] for entry in rank_zero] != expected_zero:
            raise AssertionError((j_value, rank_zero, expected_zero))
        if any(entry["p"] <= 3 * j_value + 2 for entry in rank_one):
            raise AssertionError((j_value, rank_one))
        primitive_anchor = abs(
            a_profile["primitive"][0] * b_profile["primitive"][1]
            - a_profile["primitive"][1] * b_profile["primitive"][0]
        )
        records.append(
            {
                "j": j_value,
                "ell_j": str(ell),
                "L_j": ftext(base_l),
                "mu_j": ftext(mu),
                "H_j_equals_mu_over_L": ftext(mu / base_l),
                "A_denominator": a_profile["denominator"],
                "A_content": a_profile["content"],
                "A_primitive": list(a_profile["primitive"]),
                "B_denominator": b_profile["denominator"],
                "B_content": b_profile["content"],
                "B_primitive": list(b_profile["primitive"]),
                "primitive_anchor_absolute": primitive_anchor,
                "rank_zero": rank_zero,
                "rank_one_above_3j_plus_2": rank_one,
            }
        )
    return {"label": "FINITE", "range": [1, max_j], "rows": records}


def selected_joint_gates() -> dict[str, Any]:
    cases = []
    for j_value, prime, residuals in ((3, 19, range(1, 6, 2)), (7, 79, range(1, 26, 2))):
        arow = real_gate_row(j_value, "A")
        brow = real_gate_row(j_value, "B")
        rank, kind = row_rank(arow, brow, prime)
        if rank != 1:
            raise AssertionError((j_value, prime, rank, kind))
        survivor = arow if any(row_mod(arow, prime)) else brow
        rows = []
        for s_value in residuals:
            data = I196.primitive_data(s_value)
            rho = prime % 4
            a0 = I196.reduce_fraction(I196.gate_constant(j_value, data, rho, "A0"), prime)
            b0 = I196.reduce_fraction(I196.gate_constant(j_value, data, rho, "B0"), prime)
            rows.append({"s": s_value, "A0": a0, "B0": b0, "joint": a0 == 0 and b0 == 0})
        cases.append(
            {
                "j": j_value,
                "p": prime,
                "rank_type": kind,
                "surviving_equation_on_(V(-1),ReV(i),ImV(i))": normalized_nonzero_row(survivor, prime),
                "residual_rows": rows,
            }
        )
    if cases[0]["rank_type"] != "B_zero" or cases[0]["surviving_equation_on_(V(-1),ReV(i),ImV(i))"] != [1, 17, 4]:
        raise AssertionError(cases[0])
    if cases[1]["rank_type"] != "nonzero_parallel" or cases[1]["surviving_equation_on_(V(-1),ReV(i),ImV(i))"] != [1, 21, 60]:
        raise AssertionError(cases[1])
    return {"label": "FINITE exact selected witnesses", "cases": cases}


def certificate(max_j: int, diagonal_limit: int, direct_check: int) -> dict[str, Any]:
    recurrence = telescoper_symbolic_check()
    diagonal = diagonal_scan(diagonal_limit, direct_check)
    if diagonal["zeros"]:
        raise AssertionError(diagonal["zeros"])
    required_per_m = Fraction(1177979020165907632818384072, 10**28)
    gap_per_6m = Fraction(196329836694317938803064012, 10**28)
    tail = Fraction(2, 3 * (diagonal_limit + 1))
    tail_per_6m = tail / 6
    return {
        "item": 210,
        "arithmetic": "exact rational/Gaussian and integer arithmetic; bounded scans explicitly FINITE",
        "dependencies": {
            "scripts/item175_fixed_band_certificate.py": sha256(ITEM175_PATH),
            "scripts/item196_rankone_moving_gate_certificate.py": sha256(ITEM196_PATH),
        },
        "proved_all_j_reduction": {
            "real_row_normal": [2, -1, -1],
            "anchor_factorization": "mu_j=L_j H_j with H_j nonzero; hence mu_j=0 iff ell_j=0",
            "L_j": "2^(-j) ell_j",
            "ell_j": "[y^(2j+1)](y-1)^(3j+2)/(1+y^2)^(2j+2)",
            "rank_zero": "for 2j+3<=p<=3j+2",
            "rank_above": "for p>3j+2 rank is 1 iff mu_j=0 mod p, otherwise 2; rank 0 is impossible",
            "content_radical": "large-prime support of gcd(A_content,B_content) is exactly primes 2j+3<=p<=3j+2",
        },
        "proved_recurrence": {
            "order": 3,
            "valid_for": "n>=1",
            "P_coefficients_low_to_high": [list(row) for row in P_COEFFICIENTS],
            "P_factorizations": [
                "-9(n+1)(3n+4)(3n+5)(3n+7)(3n+8)(165n^2+895n+1166)",
                "6(2n+3)(3n+7)(3n+8)(106095n^4+893770n^3+2704043n^2+3484796n+1609084)",
                "-48(n+2)(2n+3)(2n+5)(3n+8)(495n^3+3345n^2+7103n+4533)",
                "64(n+2)(n+3)(2n+3)(2n+5)(2n+7)(165n^2+565n+436)",
            ],
            "telescoping_certificate": recurrence,
            "consequence": "P0(n) and P3(n) are nonzero for n>=1, so three consecutive ell zeros are impossible; isolated zeros are not excluded",
        },
        "finite_diagonal_nonzero_scan": diagonal,
        "finite_row_content_and_rank_audit": rank_and_content_audit(max_j),
        "selected_rank_one_joint_gate_witnesses": selected_joint_gates(),
        "proved_capacity_bound_from_finite_prefix": {
            "principle": "fixed nonzero-mu bands have only finitely many determinant primes; every unresolved rationally singular band lies above the certified prefix and is bounded by the full cell tail",
            "limsup_log_weight_coefficient_per_m_less_than": ftext(tail),
            "decimal_upper_bound": float(tail),
            "limsup_coefficient_per_6m_less_than": ftext(tail_per_6m),
            "decimal_upper_bound_per_6m": float(tail_per_6m),
            "current_gap_requirement_per_m": ftext(required_per_m),
            "current_gap_G_per_6m": ftext(gap_per_6m),
            "below_gap_requirement": tail < required_per_m,
            "below_G_per_6m": tail_per_6m < gap_per_6m,
            "ratio_to_gap_requirement_upper_bound": float(tail / required_per_m),
        },
        "verdict": (
            "PROVED exact row-content/rank classification and reduction of rational degeneracy to ell_j; "
            "PROVED an order-three telescoper recurrence; FINITE nonzero scan through the declared prefix "
            "gives the displayed global capacity ceiling. Full zero rate remains equivalent to excluding "
            "isolated ell_j=0 beyond that prefix. Rank-one joint gates use the surviving row only."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-j", type=int, default=12)
    parser.add_argument("--diagonal-limit", type=int, default=20_000)
    parser.add_argument("--direct-check", type=int, default=80)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.max_j, args.diagonal_limit, args.direct_check)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "verdict": result["verdict"]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
