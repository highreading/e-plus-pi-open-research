#!/usr/bin/env python3
"""Exact certificate for the item-167 prime-square ray.

For primes p=19 (mod 20), put m=(p^2-1)/10.  The companion note proves
that p^3 divides the item-163 content c_m and that p^4 does not.  This
checker reconstructs the item-164 second-Cartier row, checks the symbolic
support and root-interpolation identities used by the proof, verifies the
closed nonzero fourth-layer digit, and runs an independent deeper-Hasse
cross-check on the requested finite range.

Finite scans are diagnostics only; the all-prime conclusion is proved in
the companion note.
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
ITEM164_PATH = HERE / "item164_third_layer_certificate.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M = load("item164_for_item167", ITEM164_PATH)


def factorial_mod(n: int, p: int) -> int:
    out = 1
    for j in range(2, n + 1):
        out = out * j % p
    return out


def binomial_mod(n: int, j: int, p: int) -> int:
    return math.comb(n, j) % p


def add_term(poly: dict[int, int], exponent: int, coefficient: int, p: int) -> None:
    poly[exponent] = (poly.get(exponent, 0) + coefficient) % p


def theorem_polynomial(p: int, k: int, delta: int, gamma: int) -> dict[int, int]:
    """P with W=P/Q^p dx in the proof of the endpoint lemma."""
    n = 12 * k + 10
    out: dict[int, int] = {}
    for j in range(n + 1):
        coefficient = binomial_mod(n, j, p)
        if j & 1:
            coefficient = -coefficient % p
        add_term(out, n + 3 + 4 * j, delta * coefficient, p)
        add_term(out, n + 4 + 4 * j, gamma * coefficient, p)
    theta_scale = gamma * delta % p
    # (1+x)^p(1+x^2)^(p-1)=(1+x^p)sum_j(-1)^j x^(2j).
    for j in range(p):
        coefficient = theta_scale if j % 2 == 0 else -theta_scale % p
        add_term(out, 2 * j, coefficient, p)
        add_term(out, p + 2 * j, coefficient, p)
    return {exponent: value for exponent, value in out.items() if value % p}


def row_certificate(p: int, direct_bound: int) -> dict[str, Any]:
    if p % 20 != 19:
        raise ValueError(p)
    k = (p - 19) // 20
    ell = 2 * k + 1
    m = (p * p - 1) // 10
    alpha = 12 * k + 11
    d = 8 * k + 8
    n = alpha - 1
    K = d + 1
    rho = 8 * k + 7
    if not (
        m == 18 * k + 17 + ell * p
        and 10 * m + 1 == p * p
        and 0 <= ell <= 5 * k + 3
        and p <= 4 * m + 1 < p * p
        and alpha + d == p
        and n + K == p
        and 0 < d < K < p
    ):
        raise AssertionError((p, k, ell, m))

    row = M.slab_row(p, ell)
    h0 = row["H0"] + [0] * (5 - len(row["H0"]))
    h1 = row["H1"] + [0] * (5 - len(row["H1"]))
    if any(h0[j] for j in range(len(h0)) if j != 4):
        raise AssertionError(("H0 support", p, h0))
    if any(h1[j] for j in range(len(h1)) if j not in (3, 4)):
        raise AssertionError(("H1 support", p, h1))
    h = h0[4] % p
    a_coefficient = h1[3] % p
    b_coefficient = h1[4] % p

    inv4 = pow(4, -1, p)
    t0_at_1 = (
        inv4
        * factorial_mod(2 * k + 1, p)
        * factorial_mod(8 * k + 7, p)
        * pow(factorial_mod(10 * k + 9, p), -1, p)
    ) % p
    h_formula = -4 * alpha * t0_at_1 % p

    z = (rho + 2) * inv4 % p
    pochhammer = 1
    denominator_units = True
    for q in range(rho):
        factor = (z + q) % p
        denominator_units = denominator_units and factor != 0
        pochhammer = pochhammer * factor % p
    s1_formula = (
        -inv4 * factorial_mod(rho - 1, p) * pow(pochhammer, -1, p)
    ) % p
    a_formula = -4 * alpha * s1_formula % p
    if not denominator_units or h != h_formula or a_coefficient != a_formula:
        raise AssertionError(("H coefficient formula", p, h, h_formula, a_coefficient, a_formula))

    delta_index = 2 * k + 1
    gamma_index = 7 * k + 6
    delta = (-1 if delta_index & 1 else 1) * binomial_mod(n, delta_index, p) % p
    gamma = (-1 if gamma_index & 1 else 1) * binomial_mod(n, gamma_index, p) % p
    factors = [2 % p, h, a_coefficient, gamma, delta]
    if any(value == 0 for value in factors):
        raise AssertionError(("zero fourth-layer factor", p, factors))

    r0, l0, e0 = row["Phi0_coordinates_R_L_E"]
    r1, l1, e1 = row["Phi1_coordinates_R_L_E"]
    inv_h = pow(h, -1, p)
    xg = tuple(value * inv_h % p for value in (r0, l0, e0))
    inv_a = pow(a_coefficient, -1, p)
    g = tuple(
        (left - b_coefficient * right) * inv_a % p
        for left, right in zip((r1, l1, e1), xg)
    )
    if g[1:] != ((-gamma) % p, (-gamma) % p):
        raise AssertionError(("G periods", p, g, gamma))
    if xg[1:] != (delta, (-delta) % p):
        raise AssertionError(("xG periods", p, xg, delta))
    relative_boundary = (delta * g[0] + gamma * xg[0]) % p
    if relative_boundary != 0 or row["next_A_digit"] != 0:
        raise AssertionError(("relative endpoint", p, relative_boundary, row["next_A_digit"]))

    # Exact proof-side polynomial and its two zero Cartier resonances.
    proof_poly = theorem_polynomial(p, k, delta, gamma)
    resonances = [proof_poly.get(p - 1, 0), proof_poly.get(2 * p - 1, 0)]
    if resonances != [0, 0] or max(proof_poly) > 3 * p - 2:
        raise AssertionError(("resonance", p, resonances, max(proof_poly)))

    first_summand_primitive_sections: set[int] = set()
    for j in range(n + 1):
        first_summand_primitive_sections.add((n + 3 + 4 * j + 1) % 4)
        first_summand_primitive_sections.add((n + 4 + 4 * j + 1) % 4)
    if first_summand_primitive_sections != {2, 3}:
        raise AssertionError(
            ("first summand section support", p, first_summand_primitive_sections)
        )

    t_sections = [0, 0, 0, 0]
    for exponent, coefficient in proof_poly.items():
        denominator = (exponent + 1) % p
        if denominator == 0:
            raise AssertionError(("unremoved resonance", p, exponent, coefficient))
        primitive_exponent = exponent + 1
        section = primitive_exponent % 4
        t_sections[section] = (
            t_sections[section] + coefficient * pow(denominator, -1, p)
        ) % p

    paired_sum = sum(
        pow((4 * r + 1) % p, -1, p) for r in range((p - 1) // 2 + 1)
    ) % p
    theta_single_section_formula = gamma * delta * paired_sum % p
    if (
        paired_sum != 0
        or t_sections[0] != theta_single_section_formula
        or t_sections[1] != theta_single_section_formula
    ):
        raise AssertionError(
            (
                "root interpolation endpoint",
                p,
                paired_sum,
                t_sections,
                theta_single_section_formula,
            )
        )

    period_determinant_formula = 2 * h * a_coefficient * gamma * delta % p
    if row["next_period_determinant"] != period_determinant_formula:
        raise AssertionError(
            ("period determinant", p, row["next_period_determinant"], period_determinant_formula)
        )
    b1 = -period_determinant_formula % p
    if b1 == 0:
        raise AssertionError(("p4 survivor", p))

    direct = None
    if p <= direct_bound:
        direct = M.direct_hasse_digit(p, ell)
        expected = {"a0": 0, "a1": 0, "b0": 0, "b1": b1}
        if direct != expected:
            raise AssertionError(("direct Hasse", p, direct, expected))

    return {
        "p": p,
        "k": k,
        "ell": ell,
        "m": m,
        "band": {
            "ten_m_plus_one": 10 * m + 1,
            "four_m_plus_one": 4 * m + 1,
            "four_m_plus_two": 4 * m + 2,
            "alpha": alpha,
            "d": d,
            "n": n,
            "K": K,
        },
        "H0": row["H0"],
        "H1": row["H1"],
        "h": h,
        "A": a_coefficient,
        "B": b_coefficient,
        "gamma": gamma,
        "delta": delta,
        "G_coordinates_R_L_E": list(g),
        "xG_coordinates_R_L_E": list(xg),
        "relative_boundary": relative_boundary,
        "paired_reciprocal_sum": paired_sum,
        "first_summand_primitive_sections": sorted(first_summand_primitive_sections),
        "zero_resonance_primitive_section_sums": t_sections,
        "zero_resonances_at_p_minus_1_2p_minus_1": resonances,
        "next_A_digit": row["next_A_digit"],
        "next_period_determinant": row["next_period_determinant"],
        "actual_b1": b1,
        "factor_nonzero": True,
        "valuation_of_content": 3,
        "direct_hasse": direct,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-bound", type=int, default=2000)
    parser.add_argument("--direct-bound", type=int, default=200)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rows = [
        row_certificate(p, args.direct_bound)
        for p in M.primes_upto(args.prime_bound)
        if p % 20 == 19
    ]
    direct_rows = [row for row in rows if row["direct_hasse"] is not None]
    payload = {
        "item": 167,
        "title": "Prime-square ray: exact third layer and fourth-layer obstruction",
        "scope": {
            "prime_bound": args.prime_bound,
            "direct_hasse_bound": args.direct_bound,
            "ray": "p=20k+19 prime, ell=2k+1, m=(p^2-1)/10",
        },
        "status": {
            "all_prime_endpoint_identity": "PROVED in companion note",
            "p3_divides_content": "PROVED for every prime on the ray",
            "p4_divides_content": "PROVED false for every prime on the ray",
            "exact_content_valuation": 3,
            "finite_rows": "EXPERIMENTAL diagnostics only",
            "positive_mass_gain": "OPEN and not supplied by this thin ray",
        },
        "summary": {
            "prime_rows": len(rows),
            "first_prime": rows[0]["p"] if rows else None,
            "last_prime": rows[-1]["p"] if rows else None,
            "p3_failures": sum(row["valuation_of_content"] < 3 for row in rows),
            "p4_survivors": sum(row["actual_b1"] == 0 for row in rows),
            "direct_hasse_rows": len(direct_rows),
            "direct_hasse_primes": [row["p"] for row in direct_rows],
        },
        "dependencies": {
            "item164_third_layer_certificate.py": sha256(ITEM164_PATH),
            "item167_p2_ray_certificate.py": sha256(Path(__file__).resolve()),
        },
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
