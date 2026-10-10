#!/usr/bin/env python3
"""Exact certificate for all four prime-square residue classes (item 170).

This file is developed together with the companion theorem note.  It uses
only the standard library plus the pinned item-163/164 certificate modules.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ITEM164 = HERE / "item164_third_layer_certificate.py"
ITEM167 = HERE / "item167_p2_ray_certificate.py"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M = load("item164_for_item170", ITEM164)
RAY19 = load("item167_for_item170", ITEM167)
TOWER = M._TOWER
EXTENDED = M._EXTENDED
ITEM163 = Path(M.ITEM163).resolve()
EXTENDED_PATH = Path(EXTENDED.__file__).resolve()
BASE_PATH = Path(EXTENDED.BASE_PATH).resolve()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n, flag in enumerate(sieve) if flag]


def square_parameters(p: int) -> dict[str, int]:
    if p == 5 or p % 2 == 0 or p % 10 not in (1, 9):
        raise ValueError(p)
    m = (p * p - 1) // 10
    N = 6 * m
    K0 = 4 * m + 1
    r = N % p
    t0 = K0 % p
    A = N // p
    c = K0 // p + 1
    if not (
        p <= K0 < p * p
        and N == A * p + r
        and K0 == (c - 1) * p + t0
        and (K0 + 1) % p == t0 + 1
    ):
        raise AssertionError(p)
    return {
        "p": p,
        "m": m,
        "N": N,
        "K0": K0,
        "r": r,
        "t0": t0,
        "A": A,
        "c": c,
    }


def residual_polynomial(p: int, s: int) -> list[int]:
    par = square_parameters(p)
    r = par["r"]
    if s == 0:
        row = M.binomial_row(r, p)
        out = [0] * (5 * r + 1)
        for j, value in enumerate(row):
            out[r + 4 * j] = value if j % 2 == 0 else -value % p
        return M.trim(out)
    if s == 1:
        row = M.binomial_row(r - 1, p)
        out = [0] * (5 * r - 2)
        for j, value in enumerate(row):
            coefficient = value if j % 2 == 0 else -value % p
            out[r + 4 * j] = coefficient
            out[r + 4 * j + 1] = -coefficient % p
        return M.trim(out)
    raise ValueError(s)


def resonant_vector(poly: list[int], p: int) -> list[int]:
    return [poly[j * p - 1] if j * p - 1 < len(poly) else 0 for j in (1, 2)]


def shifted(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def d_power(exponent: int, p: int) -> list[int]:
    """D^exponent for D=x(1-x^4), over F_p."""
    row = M.binomial_row(exponent, p)
    out = [0] * (5 * exponent + 1)
    for j, value in enumerate(row):
        out[exponent + 4 * j] = value if j % 2 == 0 else -value % p
    return M.trim(out)


def theta_numerator(p: int) -> list[int]:
    """Numerator of dx/(1+x^2) over Q^p."""
    out = [0] * (3 * p - 1)
    for j in range(p):
        value = 1 if j % 2 == 0 else -1 % p
        out[2 * j] = value
        out[p + 2 * j] = (out[p + 2 * j] + value) % p
    return M.trim(out)


def zero_resonance_sections(poly: list[int], p: int) -> list[int]:
    """Four section sums of the zero-constant primitive of poly dx."""
    out = [0, 0, 0, 0]
    for exponent, coefficient in enumerate(poly):
        if not coefficient:
            continue
        denominator = (exponent + 1) % p
        if denominator == 0:
            raise AssertionError(("unremoved resonance", p, exponent, coefficient))
        out[(exponent + 1) % 4] = (
            out[(exponent + 1) % 4]
            + coefficient * pow(denominator, -1, p)
        ) % p
    return out


def paired_reciprocal_sum(p: int) -> tuple[int, list[int]]:
    """The endpoint sections supplied by the elementary theta term."""
    if p % 4 == 1:
        denominators = [4 * r + 3 for r in range((p - 3) // 2 + 1)]
    else:
        denominators = [4 * r + 1 for r in range((p - 1) // 2 + 1)]
    value = sum(pow(d % p, -1, p) for d in denominators) % p
    return value, denominators


def factorial_mod(n: int, p: int) -> int:
    out = 1
    for j in range(2, n + 1):
        out = out * j % p
    return out


def choose_signed(n: int, j: int, p: int) -> int:
    value = math.comb(n, j) % p
    return -value % p if j & 1 else value


def syzygy_second_cartier(p: int) -> dict[str, Any] | None:
    """First determinant Bockstein for rank-one square classes."""
    par = square_parameters(p)
    polys = [residual_polynomial(p, s) for s in (0, 1)]
    vectors = [resonant_vector(poly, p) for poly in polys]
    if (vectors[0][0] * vectors[1][1] - vectors[0][1] * vectors[1][0]) % p:
        return None
    if vectors[0][0] or vectors[1][0]:
        gammas = [vectors[0][0], vectors[1][0]]
    else:
        gammas = [vectors[0][1], vectors[1][1]]
    theta = M.add(M.scale(polys[0], gammas[1], p), M.scale(polys[1], -gammas[0], p), p)
    if any(resonant_vector(theta, p)):
        raise AssertionError((p, vectors, gammas))
    primitive = M.primitive(theta, p)
    A = par["A"]
    c = par["c"]
    u = [0, 1, -1]
    up = [1, -2]
    q = [1, 1, 1, 1]
    qp = [1, 2, 3]
    logarithmic_derivative_numerator = M.add(
        M.scale(M.conv(up, q, p), A, p),
        M.scale(M.conv(qp, u, p), -c, p),
        p,
    )
    numerator = M.conv(primitive, logarithmic_derivative_numerator, p)
    maximum_n = (len(numerator) - 1 + 4 * (p - 1)) // p
    h = [0] * (maximum_n + 1)
    for n in range(maximum_n + 1):
        h[n] = sum(
            numerator[p * n - 4 * j]
            for j in range(p)
            if 0 <= p * n - 4 * j < len(numerator)
        ) % p
    h = M.trim(h)
    return {
        "vectors": vectors,
        "gammas": gammas,
        "theta": theta,
        "primitive": primitive,
        "H": h,
    }


def balanced_relative_certificate(p: int, syzygy: dict[str, Any] | None) -> dict[str, Any]:
    """Construct the Cartier-zero relative differential used for A-minors."""
    par = square_parameters(p)
    residue_class = p % 20
    theta = theta_numerator(p)
    non_theta_sections: set[int] = set()

    if residue_class == 1:
        k = (p - 1) // 20
        exponent = 12 * k
        f = d_power(exponent, p)
        xf = shifted(f, 1)
        gamma = resonant_vector(f, p)[0]
        delta = resonant_vector(xf, p)[1]
        poly = M.add(
            M.add(M.scale(f, delta, p), M.scale(xf, gamma, p), p),
            M.scale(theta, -gamma * delta, p),
            p,
        )
        for exponent0, coefficient in enumerate(M.add(M.scale(f, delta, p), M.scale(xf, gamma, p), p)):
            if coefficient:
                non_theta_sections.add((exponent0 + 1) % 4)
        factors = {"gamma": gamma, "delta": delta}
        maximum_pole_order = par["c"]
    elif residue_class == 9:
        k = (p - 9) // 20
        exponent = 12 * k + 5
        n = exponent - 1
        f = d_power(exponent, p)
        x_form = shifted(d_power(n, p), 4)
        gamma = resonant_vector(f, p)[1]
        delta = resonant_vector(x_form, p)[0]
        poly = M.add(
            M.add(M.scale(f, delta, p), M.scale(x_form, gamma, p), p),
            M.scale(theta, -gamma * delta, p),
            p,
        )
        for exponent0, coefficient in enumerate(
            M.add(M.scale(f, delta, p), M.scale(x_form, gamma, p), p)
        ):
            if coefficient:
                non_theta_sections.add((exponent0 + 1) % 4)
        factors = {"gamma": gamma, "delta": delta}
        maximum_pole_order = par["c"] + 1
    elif residue_class == 11:
        if syzygy is None:
            raise AssertionError(p)
        k = (p - 11) // 20
        exponent = 12 * k + 6
        n = exponent - 1
        f = d_power(exponent, p)
        phi = M.conv(d_power(n, p), syzygy["H"], p)
        gamma = resonant_vector(f, p)[0]
        a_coefficient, b_coefficient = resonant_vector(phi, p)
        first = M.add(
            M.scale(phi, gamma, p),
            M.scale(f, -(a_coefficient - b_coefficient), p),
            p,
        )
        poly = M.add(first, M.scale(theta, gamma * b_coefficient, p), p)
        for exponent0, coefficient in enumerate(first):
            if coefficient:
                non_theta_sections.add((exponent0 + 1) % 4)
        factors = {
            "gamma": gamma,
            "a": a_coefficient,
            "b": b_coefficient,
        }
        required_nonzero = [gamma, b_coefficient]
        maximum_pole_order = par["c"] + 1
    else:
        raise ValueError(residue_class)

    resonances = resonant_vector(poly, p)
    if resonances != [0, 0]:
        raise AssertionError(("balanced resonances", p, resonances))
    proper_at_infinity = len(poly) - 1 <= 3 * p - 2
    if not proper_at_infinity:
        raise AssertionError(("balanced degree", p, len(poly) - 1))
    sections = zero_resonance_sections(poly, p)
    paired_sum, denominators = paired_reciprocal_sum(p)
    target_section = 3 if p % 4 == 1 else 1
    if paired_sum or sections[0] or sections[target_section]:
        raise AssertionError(("relative endpoint", p, sections, paired_sum))
    if 0 in non_theta_sections or target_section in non_theta_sections:
        raise AssertionError(("non-theta section leak", p, non_theta_sections))
    if residue_class in (1, 9):
        required_nonzero = list(factors.values())
    if not all(value % p for value in required_nonzero):
        raise AssertionError(("zero balanced factor", p, factors))
    if not (maximum_pole_order < p):
        raise AssertionError(("pole order", p, maximum_pole_order))
    return {
        "factors": factors,
        "zero_resonances": resonances,
        "numerator_degree": len(poly) - 1,
        "maximum_pole_order": maximum_pole_order,
        "proper_at_infinity": proper_at_infinity,
        "non_theta_primitive_sections": sorted(non_theta_sections),
        "zero_resonance_primitive_sections": sections,
        "endpoint_target_sections": [0, target_section],
        "paired_reciprocal_sum": paired_sum,
        "paired_reciprocal_term_count": len(denominators),
    }


def class_formula_certificate(p: int, syzygy: dict[str, Any] | None) -> dict[str, Any]:
    """Closed leading period digit and theorem valuation for one class."""
    residue_class = p % 20
    vectors = [resonant_vector(residual_polynomial(p, s), p) for s in (0, 1)]
    if residue_class == 1:
        k = (p - 1) // 20
        a = 12 * k
        g0 = choose_signed(a, 2 * k, p)
        d1 = -choose_signed(a - 1, 7 * k, p) % p
        gamma = g0
        delta = choose_signed(a, 7 * k, p)
        expected_vectors = [[g0, 0], [choose_signed(a - 1, 2 * k, p), d1]]
        leading_b = -2 * g0 * d1 * gamma * delta % p
        rank = 2
        b_power = 0
        a_lower = 1
        content_valuation = 1
        factors = {"g0": g0, "d1": d1, "gamma": gamma, "delta": delta}
    elif residue_class == 9:
        k = (p - 9) // 20
        r = 8 * k + 3
        a = 12 * k + 5
        n = a - 1
        epsilon = -choose_signed(r - 1, 3 * k + 1, p) % p
        integral = (
            pow(4, -1, p)
            * factorial_mod(2 * k, p)
            * factorial_mod(8 * k + 3, p)
            * pow(factorial_mod(10 * k + 4, p), -1, p)
        ) % p
        h = -4 * a * integral % p
        gamma = choose_signed(a, 7 * k + 3, p)
        delta = choose_signed(n, 2 * k, p)
        expected_vectors = [[0, 0], [epsilon, 0]]
        leading_b = 2 * epsilon * h * gamma * delta % p
        rank = 1
        b_power = 1
        a_lower = 2
        content_valuation = 2
        factors = {
            "epsilon": epsilon,
            "beta_integral": integral,
            "h": h,
            "gamma": gamma,
            "delta": delta,
        }
        if syzygy is None or syzygy["H"] != [0, 0, 0, 0, epsilon * h % p]:
            raise AssertionError(("class 9 H", p, None if syzygy is None else syzygy["H"]))
    elif residue_class == 11:
        if syzygy is None:
            raise AssertionError(p)
        k = (p - 11) // 20
        a = 12 * k + 6
        n = a - 1
        g = choose_signed(a, 2 * k + 1, p)
        g1 = 5 * g * pow(6, -1, p) % p
        integral = (
            pow(4, -1, p)
            * factorial_mod(3 * k + 1, p)
            * factorial_mod(12 * k + 5, p)
            * pow(factorial_mod(15 * k + 7, p), -1, p)
        ) % p
        h4 = -4 * a * g * integral % p
        delta = choose_signed(n, 7 * k + 3, p)
        b_coefficient = h4 * delta % p
        expected_vectors = [[g, 0], [g1, 0]]
        leading_b = -2 * g * b_coefficient % p
        rank = 1
        b_power = 1
        a_lower = 2
        content_valuation = 2
        factors = {
            "g": g,
            "g1": g1,
            "beta_integral": integral,
            "h4": h4,
            "delta": delta,
            "b": b_coefficient,
        }
        if syzygy["H"][4] != h4:
            raise AssertionError(("class 11 H4", p, syzygy["H"], h4))
    elif residue_class == 19:
        k = (p - 19) // 20
        a = 12 * k + 11
        n = a - 1
        rho = 8 * k + 7
        integral = (
            pow(4, -1, p)
            * factorial_mod(2 * k + 1, p)
            * factorial_mod(8 * k + 7, p)
            * pow(factorial_mod(10 * k + 9, p), -1, p)
        ) % p
        h = -4 * a * integral % p
        z = (rho + 2) * pow(4, -1, p) % p
        pochhammer = 1
        for q in range(rho):
            pochhammer = pochhammer * (z + q) % p
        s_value = (
            -pow(4, -1, p)
            * factorial_mod(rho - 1, p)
            * pow(pochhammer, -1, p)
        ) % p
        lam = -4 * a * s_value % p
        gamma = choose_signed(n, 7 * k + 6, p)
        delta = choose_signed(n, 2 * k + 1, p)
        expected_vectors = [[0, 0], [0, 0]]
        leading_b = -2 * h * lam * gamma * delta % p
        rank = 0
        b_power = 2
        a_lower = 3
        content_valuation = 3
        factors = {
            "beta_integral": integral,
            "h": h,
            "reciprocal_binomial_sum": s_value,
            "lambda": lam,
            "gamma": gamma,
            "delta": delta,
        }
    else:
        raise ValueError(residue_class)

    if vectors != expected_vectors:
        raise AssertionError(("first Cartier vectors", p, vectors, expected_vectors))
    if any(value == 0 for value in factors.values()) or leading_b == 0:
        raise AssertionError(("zero leading factor", p, factors, leading_b))
    return {
        "cartier_rank": rank,
        "resonant_vectors": vectors,
        "leading_period_digit_power": b_power,
        "leading_period_digit": leading_b,
        "A_minor_valuation_lower_bound": a_lower,
        "B_minor_exact_valuation": b_power,
        "content_exact_valuation": content_valuation,
        "nonzero_factors": factors,
    }


def direct_row(p: int, precision: int = 4) -> dict[str, Any]:
    par = square_parameters(p)
    m = par["m"]
    modulus = p**precision
    l0, x0, e0, _ = TOWER.coordinates_mod(EXTENDED, m, 4 * m + 1, p, precision)
    l1, x1, e1, _ = TOWER.coordinates_mod(EXTENDED, m, 4 * m + 2, p, precision)
    determinant_a = (l1 * x0 - l0 * x1) % modulus
    determinant_b = (l1 * e0 - l0 * e1) % modulus

    def vp(value: int) -> int:
        for exponent in range(precision):
            if value % p ** (exponent + 1):
                return exponent
        return precision

    v_a = vp(determinant_a)
    v_b = vp(determinant_b)
    return {
        **par,
        "class_mod_20": p % 20,
        "resonant_vectors": [resonant_vector(residual_polynomial(p, s), p) for s in (0, 1)],
        "rank": None,
        "v_A_minor": v_a,
        "v_B_minor": v_b,
        "content_valuation": min(v_a, 1 + v_b),
        "A_digits": TOWER.p_digits(determinant_a, p, precision),
        "B_digits": TOWER.p_digits(determinant_b, p, precision),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-bound", type=int, default=200)
    parser.add_argument("--direct-bound", type=int, default=200)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for p in primes_upto(args.prime_bound):
        if p == 5 or p % 10 not in (1, 9):
            continue
        vectors = [resonant_vector(residual_polynomial(p, s), p) for s in (0, 1)]
        determinant = (vectors[0][0] * vectors[1][1] - vectors[0][1] * vectors[1][0]) % p
        syzygy = syzygy_second_cartier(p)
        formula = class_formula_certificate(p, syzygy)
        record: dict[str, Any] = {
            **square_parameters(p),
            "class_mod_20": p % 20,
            "resonant_vectors": vectors,
            "cartier_determinant": determinant,
            "cartier_rank": formula["cartier_rank"],
            "theorem": formula,
        }
        if syzygy is not None:
            record["syzygy_gammas"] = syzygy["gammas"]
            record["syzygy_H"] = syzygy["H"]
        if p % 20 == 19:
            ray = RAY19.row_certificate(p, 0)
            if (
                ray["actual_b1"] != formula["leading_period_digit"]
                or ray["valuation_of_content"] != 3
            ):
                raise AssertionError(("item 167 dependency", p, ray, formula))
            record["relative_endpoint_certificate"] = {
                "source": "item167_p2_ray_certificate.py",
                "paired_reciprocal_sum": ray["paired_reciprocal_sum"],
                "zero_resonances": ray["zero_resonances_at_p_minus_1_2p_minus_1"],
                "zero_resonance_primitive_sections": ray[
                    "zero_resonance_primitive_section_sums"
                ],
                "relative_boundary": ray["relative_boundary"],
            }
        else:
            record["relative_endpoint_certificate"] = balanced_relative_certificate(
                p, syzygy
            )
        if p <= args.direct_bound:
            direct = direct_row(p)
            b_power = formula["leading_period_digit_power"]
            if (
                direct["B_digits"][b_power] != formula["leading_period_digit"]
                or any(direct["B_digits"][:b_power])
                or any(direct["A_digits"][: formula["A_minor_valuation_lower_bound"]])
                or direct["content_valuation"] != formula["content_exact_valuation"]
            ):
                raise AssertionError(("direct Hasse", p, direct, formula))
            record["direct"] = direct
        rows.append(record)
    class_counts = {
        str(residue): sum(row["class_mod_20"] == residue for row in rows)
        for residue in (1, 9, 11, 19)
    }
    direct_rows = [row for row in rows if "direct" in row]
    payload = {
        "item": 170,
        "title": "Complete prime-square residue-class valuation theorem",
        "status": {
            "all_prime_classification": "PROVED in companion note",
            "class_1_mod_20": "v_p(c_m)=1",
            "class_9_mod_20": "v_p(c_m)=2",
            "class_11_mod_20": "v_p(c_m)=2",
            "class_19_mod_20": "v_p(c_m)=3 (item 167, reproduced)",
            "finite_rows": "EXPERIMENTAL exact diagnostics only",
            "positive_mass": "NONE: 10m+1=p^2 is a zero-rate locus",
        },
        "scope": {
            "prime_bound": args.prime_bound,
            "direct_hasse_bound": args.direct_bound,
            "locus": "10m+1=p^2, p an odd prime other than 5",
        },
        "summary": {
            "prime_rows": len(rows),
            "class_counts": class_counts,
            "direct_hasse_rows": len(direct_rows),
            "direct_hasse_primes": [row["p"] for row in direct_rows],
            "classification_failures": 0,
            "relative_endpoint_failures": 0,
            "leading_period_digit_failures": 0,
        },
        "dependencies": {
            str(ITEM164.name): sha256(ITEM164),
            str(ITEM167.name): sha256(ITEM167),
            str(ITEM163.name): sha256(ITEM163),
            str(EXTENDED_PATH.name): sha256(EXTENDED_PATH),
            str(BASE_PATH.name): sha256(BASE_PATH),
            Path(__file__).name: sha256(Path(__file__).resolve()),
        },
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
