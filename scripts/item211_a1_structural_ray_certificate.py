#!/usr/bin/env python3
"""Deterministic checker for Item 211's structural-ray A1 formula.

The all-s proof is in the companion report.  This checker evaluates the
closed sparse-sum formula, checks its internal Cayley-vector form, and
replays a bounded set of rows with Item 209's independent modulo-p^3 Hasse
engine.  Every scan recorded here is finite and is not extrapolated.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any, Iterator


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item211_a1_structural_ray_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item211_a1_structural_ray_certificate.json"
)
ITEM209_NAME = "item209_second_lift_digit_certificate.py"
FORMULA_SCAN_MAX_P = 20_000
HASSE_SCAN_MAX_P = 500
LARGE_HASSE_CONTROL_P = 1499


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % divisor for divisor in range(3, math.isqrt(n) + 1, 2))


def ray_primes(limit: int) -> list[int]:
    return [p for p in range(19, limit + 1, 20) if is_prime(p)]


def binomial_row_mod(n: int, p: int) -> Iterator[tuple[int, int]]:
    """Yield (-1)^r binom(n,r) modulo p for 0 <= r <= n."""
    value = 1
    yield 0, value
    for r in range(n):
        value = -value * (n - r) * pow(r + 1, -1, p) % p
        yield r + 1, value


def rational_mod(numerator: int, denominator: int, p: int) -> int:
    return numerator % p * pow(denominator % p, -1, p) % p


# Fixed (R,L) Cayley-coordinate pairs at j=1.
V = ((-11, 6), (-5, 1))
Z0 = ((-35, 24), (7, 1))
W3 = ((-577, 24), (75, 1))


def reduce_pair(pair: tuple[tuple[int, int], tuple[int, int]], p: int) -> tuple[int, int]:
    return tuple(rational_mod(n, d, p) for n, d in pair)  # type: ignore[return-value]


def ray_sums(s: int, p: int) -> dict[str, int]:
    """Return beta,A,B,H0,H1 and the two equivalent j=1 A1 formulas."""
    if s % 4 != 3 or p != 5 * s + 4 or not is_prime(p):
        raise ValueError((s, p))
    threshold = (3 * s + 3) // 4
    beta = 0
    a_value = 0
    b_value = 0
    h0 = 0
    h1 = 0

    for r, signed_binomial in binomial_row_mod(2 * s + 1, p):
        degree = 2 * s + 2 + 4 * r
        term = signed_binomial * pow(degree, -1, p) % p
        beta = (beta + term) % p
        if r >= threshold:
            if degree < p:
                raise AssertionError(("H0 threshold", s, p, r, degree))
            h0 = (h0 + term) % p

    for r, signed_binomial in binomial_row_mod(2 * s, p):
        degree_a = 2 * s + 2 + 4 * r
        degree_b = degree_a + 1
        term_a = signed_binomial * pow(degree_a, -1, p) % p
        term_b = signed_binomial * pow(degree_b, -1, p) % p
        a_value = (a_value + term_a) % p
        b_value = (b_value + term_b) % p
        if r >= threshold:
            if degree_a < p or degree_b < p:
                raise AssertionError(("H1 threshold", s, p, r, degree_a, degree_b))
            h1 = (h1 + term_a - term_b) % p

    if beta != (s + 2) * a_value % p:
        raise AssertionError(("beta/A relation", s, p, beta, a_value))
    if not beta or not a_value or not b_value:
        raise AssertionError(("nonzero beta factors", s, p, beta, a_value, b_value))

    v = reduce_pair(V, p)
    z0 = reduce_pair(Z0, p)
    w3 = reduce_pair(W3, p)
    d0 = 9 * h0 % p
    d1 = 9 * h1 % p
    q0 = tuple((5 * beta * z0[k] - d0 * v[k]) % p for k in range(2))
    q1 = tuple(
        (5 * a_value * z0[k] + b_value * w3[k] - d1 * v[k]) % p
        for k in range(2)
    )
    determinant = (q0[0] * q1[1] - q0[1] * q1[0]) % p
    phi = (
        1414 * beta * b_value
        - 4347 * beta * h1
        + 4347 * a_value * h0
        + 11133 * h0 * b_value
    ) % p
    closed = 5 * phi * pow(24, -1, p) % p
    if determinant != closed:
        raise AssertionError(("closed formula", s, p, determinant, closed))

    return {
        "s": s,
        "p": p,
        "threshold_R": threshold,
        "beta_mod_p": beta,
        "A_mod_p": a_value,
        "B_mod_p": b_value,
        "H0_mod_p": h0,
        "H1_mod_p": h1,
        "d0_equals_9H0_mod_p": d0,
        "d1_equals_9H1_mod_p": d1,
        "q0_equals_X0_over_p_L0_over_p_mod_p": list(q0),
        "q1_equals_X1_over_p_L1_over_p_mod_p": list(q1),
        "Phi_mod_p": phi,
        "A1_mod_p": closed,
    }


def load_item209() -> tuple[Any, Path]:
    path = HERE / ITEM209_NAME
    if not path.exists():
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location("item209_for_item211", path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, path


def validate_hasse_row(item209: Any, p: int, j: int) -> dict[str, Any]:
    s = (p - 4) // 5
    row = item209.evaluate_row(s, p, j)
    result = {
        "p": p,
        "s": s,
        "j": j,
        "m": row["m"],
        "A1_mod_p": row["A1_equals_raw_digit_d2_when_A0_zero"],
        "joint_cubic_gate": row["joint_cubic_gate"],
    }
    if j == 1:
        formula = ray_sums(s, p)
        digits = row["coordinate_digits"]
        actual_q0 = [digits["X0_equals_pR0"][1], digits["L0"][1]]
        actual_q1 = [digits["X1_equals_pR1"][1], digits["L1"][1]]
        if actual_q0 != formula["q0_equals_X0_over_p_L0_over_p_mod_p"]:
            raise AssertionError(("q0/Hasse mismatch", p, actual_q0, formula))
        if actual_q1 != formula["q1_equals_X1_over_p_L1_over_p_mod_p"]:
            raise AssertionError(("q1/Hasse mismatch", p, actual_q1, formula))
        if result["A1_mod_p"] != formula["A1_mod_p"]:
            raise AssertionError(("A1/Hasse mismatch", p, result, formula))
        result["formula_q0"] = actual_q0
        result["formula_q1"] = actual_q1
        result["formula_match"] = True
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--formula-scan-max-p", type=int, default=FORMULA_SCAN_MAX_P)
    parser.add_argument("--hasse-scan-max-p", type=int, default=HASSE_SCAN_MAX_P)
    args = parser.parse_args()

    item209, item209_path = load_item209()
    formula_rows = [ray_sums((p - 4) // 5, p) for p in ray_primes(args.formula_scan_max_p)]
    formula_zeros = [
        {"p": row["p"], "s": row["s"]}
        for row in formula_rows
        if row["A1_mod_p"] == 0
    ]

    small_hasse_primes = ray_primes(args.hasse_scan_max_p)
    j1_hasse_primes = list(small_hasse_primes)
    if LARGE_HASSE_CONTROL_P > args.hasse_scan_max_p:
        j1_hasse_primes.append(LARGE_HASSE_CONTROL_P)
    j1_hasse = [validate_hasse_row(item209, p, 1) for p in j1_hasse_primes]
    j3_hasse = [validate_hasse_row(item209, p, 3) for p in small_hasse_primes]
    j3_zeros = [
        {"p": row["p"], "s": row["s"], "m": row["m"]}
        for row in j3_hasse
        if row["A1_mod_p"] == 0
    ]

    # Support-gap checks are symbolic in the report; these residues audit them.
    support_residues = {
        "P0_target_difference_3s_plus_2_mod_4": (3 * 3 + 2) % 4,
        "P1_first_target_difference_3s_plus_2_mod_4": (3 * 3 + 2) % 4,
        "P1_second_target_difference_3s_plus_1_mod_4": (3 * 3 + 1) % 4,
    }
    if 0 in support_residues.values():
        raise AssertionError(support_residues)

    payload = {
        "schema": "item211-a1-structural-ray-v1",
        "statuses": {
            "integer_resonant_coefficients_gamma0_gamma1_are_zero_on_the_ray": "PROVED_IN_COMPANION_REPORT",
            "j1_exact_sparse_sum_A1_formula": "PROVED_IN_COMPANION_REPORT",
            "j1_A1_zero_iff_Phi_zero_mod_p": "PROVED_IN_COMPANION_REPORT",
            "j1_global_nonvanishing_or_zero_classification": "OPEN",
            "bounded_scans": "FINITE_NO_EXTRAPOLATION",
            "route1_exponent_gain": "NONE_ZERO_RATE_RAY",
        },
        "ray": {
            "conditions": "s=3 mod 4; p=5s+4 prime; j=1; m=(9s+7)/2",
            "fixed_m_identity_all_j": "10m+1=(5j+4)p",
            "fixed_m_log_weight": "at most log(10m+1)=O(log m)",
        },
        "support_gap_residues": support_residues,
        "fixed_cayley_data_R_L": {
            "v_coord_Fdx": ["-11/6", "-5"],
            "z0_coord_F_over_x_dx": ["-35/24", "7"],
            "W3_equals_sum_n_a_a3_z_a": ["-577/24", "75"],
            "det_v_z0": "-161/8",
            "det_v_W3": "-6185/24",
            "det_z0_W3": "707/12",
        },
        "formula": {
            "d0": "9 H0 mod p",
            "d1": "9 H1 mod p",
            "q0": "5 beta z0 - d0 v mod p",
            "q1": "5 A z0 + B W3 - d1 v mod p",
            "Phi": "1414 beta B - 4347 beta H1 + 4347 A H0 + 11133 H0 B",
            "A1": "5 Phi / 24 mod p",
            "zero_criterion": "A1=0 iff Phi=0 mod p",
            "beta_relation": "beta=2(2s+1)A/(5s+3), hence beta=(s+2)A mod p",
        },
        "finite_formula_scan": {
            "max_p": args.formula_scan_max_p,
            "ray_prime_count": len(formula_rows),
            "zero_count": len(formula_zeros),
            "zero_rows": formula_zeros,
            "first_rows": formula_rows[:8],
            "last_rows": formula_rows[-8:],
            "label": "FINITE_NO_EXTRAPOLATION",
        },
        "finite_hasse_replay": {
            "small_max_p": args.hasse_scan_max_p,
            "j1_formula_match_count": len(j1_hasse),
            "j1_rows": j1_hasse,
            "j3_row_count": len(j3_hasse),
            "j3_A1_zero_rows": j3_zeros,
            "label": "FINITE_NO_EXTRAPOLATION",
        },
        "dependency_hashes": {
            "scripts/item209_second_lift_digit_certificate.py": sha256(item209_path)
        },
        "scope": {
            "j1_nonzero_scan_is_not_a_theorem": True,
            "actual_ray_zero_witness_at_j3": {"s": 3, "p": 19, "j": 3, "m": 36},
            "off_ray_extension": "template only; exact support gap and quotient simplification generally fail",
            "no_claim_about_e_plus_pi": True,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "formula_rows": len(formula_rows),
                "formula_zeros": len(formula_zeros),
                "j1_hasse_matches": len(j1_hasse),
                "j3_hasse_zeros": len(j3_zeros),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
