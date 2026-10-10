#!/usr/bin/env python3
"""Deterministic certificate for Item 338.

The checker verifies the exact base-l carry automaton for the global
Cartier coefficient, the diagonal degeneration at l=p, and the distinct
off-diagonal mechanisms behind the primitive carrier hits 23 and 173.
All bounded searches are diagnostics only; the symbolic statements and
capacity audit are in the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item338_j2_secondary_cartier_saturation_certificate.json"

DEPENDENCIES = {
    "sources/item336_j2_carrier_resultant_obstruction_report.md":
        "761f09e999c0f76139e036f2f4db03743b363087e04f9ed661fe65229cb0b4c2",
    "scripts/item336_j2_carrier_resultant_obstruction_certificate.py":
        "af5a5ef313df81275f989236cc9a600c1132d90e14a95a4fb2dc508fc7c09022",
    "results/item336_j2_carrier_resultant_obstruction_certificate.json":
        "2769620afcf258e84dd4713113f32662e4140bfa1706f4983c137aca2d132010",
    "manifests/item336_j2_carrier_resultant_obstruction_manifest.json":
        "5ee017780f55425a2e9598c12e370c6e194f96e79be5e69c1f0f1d176c5d13f3",
}


def default_output() -> Path:
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def valuation(value: int, prime: int) -> int:
    value = abs(value)
    result = 0
    while value and value % prime == 0:
        value //= prime
        result += 1
    return result


def prime_factors(value: int) -> list[int]:
    value = abs(value)
    result = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            result.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        result.append(value)
    return result


def digits(value: int, prime: int, length: int | None = None) -> list[int]:
    if value < 0:
        raise ValueError(value)
    result = []
    while value:
        result.append(value % prime)
        value //= prime
    if not result:
        result = [0]
    if length is not None:
        result.extend([0] * (length - len(result)))
    return result


def coefficient(a: int, b: int, index: int) -> int:
    """[x^index](1-x)^a(1+x)^b over the integers."""
    if index < 0 or index > a + b:
        return 0
    return sum(
        (-1) ** j * math.comb(a, j) * math.comb(b, index - j)
        for j in range(max(0, index - b), min(a, index) + 1)
    )


def local_coefficient(a_digit: int, b_digit: int, index: int, prime: int) -> int:
    return coefficient(a_digit, b_digit, index) % prime


def carry_matrices(a: int, b: int, index: int, prime: int) -> list[list[list[int]]]:
    """Two-state base-prime carry matrices.

    The entry [incoming][outgoing] at digit i is
    [x^(index_i-incoming+prime*outgoing)]
    (1-x)^(a_i)(1+x)^(b_i).
    """
    length = max(len(digits(a, prime)), len(digits(b, prime)), len(digits(index, prime))) + 1
    aa = digits(a, prime, length)
    bb = digits(b, prime, length)
    kk = digits(index, prime, length)
    matrices = []
    for ai, bi, ki in zip(aa, bb, kk):
        matrix = [[0, 0], [0, 0]]
        for incoming in (0, 1):
            for outgoing in (0, 1):
                degree = ki - incoming + prime * outgoing
                matrix[incoming][outgoing] = local_coefficient(ai, bi, degree, prime)
        matrices.append(matrix)
    return matrices


def carry_coefficient(a: int, b: int, index: int, prime: int) -> int:
    vector = [1, 0]
    for matrix in carry_matrices(a, b, index, prime):
        vector = [
            sum(vector[incoming] * matrix[incoming][outgoing] for incoming in (0, 1))
            % prime
            for outgoing in (0, 1)
        ]
    if vector[1] != 0:
        raise AssertionError((a, b, index, prime, vector, "unresolved final carry"))
    return vector[0]


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def automaton_replay() -> dict[str, Any]:
    rows = []
    checks = 0
    for prime in (3, 5, 7, 11):
        for a in range(0, 2 * prime + 2):
            for b in range(0, 2 * prime + 2):
                for index in range(a + b + 1):
                    direct = coefficient(a, b, index) % prime
                    carried = carry_coefficient(a, b, index, prime)
                    if direct != carried:
                        raise AssertionError((prime, a, b, index, direct, carried))
                    checks += 1
                    rows.append((prime, a, b, index, direct))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "primes": [3, 5, 7, 11],
        "checks": checks,
        "row_digest_sha256": digest_rows(rows),
    }


def exact_row_data(i318: Any, i331: Any, i334: Any, prime: int, r: int, s: int) -> dict[str, Any]:
    m = s - 1
    d = r + 4
    n = 3 * m + d
    q = 2 * m + d
    upper_exponent = n + q
    c_p = i331.coefficient(n, q, prime)
    epsilon = i331.legendre_two(prime)
    data = i318.i250.phase_data(r)
    coeff = i318.coefficients(data)
    period = i318.actual_period(r, s, data)
    h_m = i334.h_value(m)
    correction = i334.p_correction(r + 2, m)
    phi = F(c_p) + epsilon * h_m * correction
    c_value = F(2 ** (2 * s))
    base = F(9, 2) * period["kappa"] * phi
    target = tuple(
        coeff["f"][nu] * period["B"] * base
        + (-1) ** m * (
            coeff["f"][nu] * period["B"] * period["tau"]
            - 9 * c_value * coeff["b"][nu]
            + 11 * coeff["d"][nu]
        )
        for nu in (0, 1)
    )
    determinant = 9 * c_value * coeff["ell"] - 11 * coeff["m"]
    carrier = math.gcd(
        abs(determinant.numerator),
        math.gcd(abs(target[0].numerator), abs(target[1].numerator)),
    )
    ingredients = {
        "f0": coeff["f"][0],
        "f1": coeff["f"][1],
        "b0": coeff["b"][0],
        "b1": coeff["b"][1],
        "v0": coeff["d"][0],
        "v1": coeff["d"][1],
        "B": period["B"],
        "kappa": period["kappa"],
        "tau": period["tau"],
        "h": h_m,
        "P": correction,
    }
    return {
        "p": prime,
        "r": r,
        "s": s,
        "m": m,
        "d": d,
        "n": n,
        "q": q,
        "upper_exponent": upper_exponent,
        "c_p": c_p,
        "epsilon": epsilon,
        "coeff": coeff,
        "period": period,
        "h": h_m,
        "P": correction,
        "phi": phi,
        "D": determinant,
        "T": target,
        "carrier": carrier,
        "ingredients": ingredients,
    }


def support_saturated_carrier(row: dict[str, Any]) -> tuple[int, list[int]]:
    """Remove carrier primes supported by safe denominators or binom(2m,m)."""
    carrier = row["carrier"]
    central = math.comb(2 * row["m"], row["m"])
    removed = []
    remaining = carrier
    for prime in prime_factors(carrier):
        denominator_hit = any(
            value.denominator % prime == 0 for value in row["ingredients"].values()
        )
        central_hit = central % prime == 0
        if denominator_hit or central_hit:
            removed.append(prime)
            while remaining % prime == 0:
                remaining //= prime
    return remaining, removed


def two_digit_paths(row: dict[str, Any], secondary_prime: int) -> dict[str, Any]:
    a = row["n"]
    b = row["upper_exponent"]
    index = row["p"]
    if max(a, b, index) >= secondary_prime**2:
        raise AssertionError((secondary_prime, a, b, index, "not two digit"))
    a0, a1 = a % secondary_prime, a // secondary_prime
    b0, b1 = b % secondary_prime, b // secondary_prime
    k0, k1 = index % secondary_prime, index // secondary_prime
    no_carry = (
        local_coefficient(a0, b0, k0, secondary_prime)
        * local_coefficient(a1, b1, k1, secondary_prime)
    ) % secondary_prime
    one_carry = (
        local_coefficient(a0, b0, k0 + secondary_prime, secondary_prime)
        * local_coefficient(a1, b1, k1 - 1, secondary_prime)
    ) % secondary_prime
    result = (no_carry + one_carry) % secondary_prime
    if result != row["c_p"] % secondary_prime:
        raise AssertionError((secondary_prime, row["p"], result, row["c_p"] % secondary_prime))
    if result != carry_coefficient(a, b, index, secondary_prime):
        raise AssertionError((secondary_prime, row["p"], result, "matrix"))
    return {
        "secondary_prime": secondary_prime,
        "p_digits_low_to_high": [k0, k1],
        "n_digits_low_to_high": [a0, a1],
        "upper_exponent_digits_low_to_high": [b0, b1],
        "no_carry_contribution": no_carry,
        "one_carry_contribution": one_carry,
        "c_p_mod_secondary_prime": result,
    }


def hit_replay(i318: Any, i331: Any, i334: Any, i336: Any) -> dict[str, Any]:
    declared = [(23, 331, 17, 49), (173, 599, 7, 97)]
    records = []
    for secondary, prime, r, s in declared:
        row = exact_row_data(i318, i331, i334, prime, r, s)
        carrier_via_item336 = i336.exact_carrier_value(i334, i318, i331, prime, r, s)
        if row["carrier"] != secondary or carrier_via_item336 != secondary:
            raise AssertionError((secondary, prime, r, s, row["carrier"], carrier_via_item336))
        if any(value.denominator % secondary == 0 for value in [row["D"], *row["T"]]):
            raise AssertionError((secondary, prime, "final primitive denominator"))
        valuations = [
            [valuation(value.numerator, secondary), valuation(value.denominator, secondary)]
            for value in [row["D"], *row["T"]]
        ]
        if valuations != [[1, 0], [1, 0], [1, 0]]:
            raise AssertionError((secondary, prime, valuations))
        central = math.comb(2 * row["m"], row["m"])
        denominator_hits = [
            name for name, value in row["ingredients"].items()
            if value.denominator % secondary == 0
        ]
        saturated, removed = support_saturated_carrier(row)
        if saturated != 1 or removed != [secondary]:
            raise AssertionError((secondary, prime, saturated, removed))
        record = {
            "row": [prime, r, s],
            "carrier": row["carrier"],
            "D_T_valuations_numerator_denominator": valuations,
            "intermediate_denominator_hits": denominator_hits,
            "central_binomial_valuation": valuation(central, secondary),
            "structurally_saturated_carrier": saturated,
            "cartier_paths": two_digit_paths(row, secondary),
        }
        if secondary == 23:
            if denominator_hits != ["b0", "b1", "kappa"]:
                raise AssertionError((secondary, denominator_hits))
            if valuation(central, secondary) != 0:
                raise AssertionError((secondary, "central"))
            record["mechanism"] = "bad intermediate reduction with exact cancellation"
        else:
            if denominator_hits:
                raise AssertionError((secondary, denominator_hits))
            if valuation(central, secondary) != 1 or fmod(row["h"], secondary) != 0:
                raise AssertionError((secondary, "Kummer carry"))
            coeff = row["coeff"]
            period = row["period"]
            c_value = F(2 ** (2 * row["s"]))
            K = F(9, 2) * period["kappa"] * period["B"]
            U = tuple(9 * c_value * coeff["b"][nu] - 11 * coeff["d"][nu] for nu in (0, 1))
            theta_values = []
            for nu in (0, 1):
                theta = (
                    (-1) ** (row["m"] + 1)
                    * (coeff["f"][nu] * period["B"] * period["tau"] - U[nu])
                    / (K * coeff["f"][nu])
                )
                theta_values.append(fmod(theta, secondary))
            if theta_values != [162, 162] or fmod(row["phi"], secondary) != 162:
                raise AssertionError((secondary, theta_values, fmod(row["phi"], secondary)))
            record["mechanism"] = "good reduction; central-binomial Kummer carry kills h_m"
            record["phi_mod_secondary_prime"] = fmod(row["phi"], secondary)
            record["moving_target_mod_secondary_prime"] = theta_values
        records.append(record)
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "records": records,
    }


def diagonal_replay(i331: Any) -> dict[str, Any]:
    declared = [
        (11, 1, 1),
        (17, 1, 2),
        (29, 1, 4),
        (271, 113, 7),
        (331, 17, 49),
        (599, 7, 97),
    ]
    rows = []
    for prime, r, s in declared:
        m = s - 1
        d = r + 4
        n = 3 * m + d
        q = 2 * m + d
        upper = n + q
        if n != (prime - 1) // 2 or upper != prime - m - 1:
            raise AssertionError((prime, r, s, n, upper, "tied exponents"))
        direct = i331.coefficient(n, q, prime) % prime
        carried = carry_coefficient(n, upper, prime, prime)
        if direct != carried:
            raise AssertionError((prime, r, s, direct, carried))
        matrices = carry_matrices(n, upper, prime, prime)
        distinguished = matrices[0][0][1] * matrices[1][1][0] % prime
        if distinguished != direct or matrices[1][1][0] != 1:
            raise AssertionError((prime, distinguished, direct, matrices[:2]))
        if math.comb(2 * m, m) % prime == 0:
            raise AssertionError((prime, m, "central p-unit"))
        rows.append((prime, r, s, m, direct, distinguished))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
        "diagonal_transition": "M_0[0,1]=c_p and M_1[1,0]=1",
    }


def character_counterexamples(i318: Any, i331: Any, i334: Any, i336: Any) -> dict[str, Any]:
    declared = [(251, 1, 41, 3), (281, 1, 46, 7)]
    rows = []
    for prime, r, s, carrier in declared:
        actual = i336.exact_carrier_value(i334, i318, i331, prime, r, s)
        if actual != carrier:
            raise AssertionError((prime, r, s, actual, carrier))
        tied_character = i331.legendre_two(prime)
        secondary_character = i331.legendre_two(carrier)
        if tied_character != secondary_character:
            raise AssertionError((prime, carrier, tied_character, secondary_character))
        rows.append((prime, r, s, carrier, tied_character, secondary_character))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "rows": rows,
        "conclusion": "opposite quadratic character is not a valid carrier theorem",
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    i318 = load("item338_i318", "scripts/item318_j2_actual_period_plucker_certificate.py")
    i331 = load("item338_i331", "scripts/item331_j2_global_cartier_concentration_certificate.py")
    i334 = load("item338_i334", "scripts/item334_j2_coupled_cartier_carrier_certificate.py")
    i336 = load("item338_i336", "scripts/item336_j2_carrier_resultant_obstruction_certificate.py")
    return {
        "schema": "item338-j2-secondary-cartier-saturation-v1",
        "classification": "PROVED_SECONDARY_CARTIER_DIAGONAL_COLLAPSE_AND_OFF_DIAGONAL_SATURATION_NO_GO",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "local_digit_polynomial": "F_i(X)=(1-X)^(a_i)*(1+X)^(b_i)",
            "carry_matrix": "M_i[u,v]=[X^(k_i-u+ell*v)]F_i(X), u,v in {0,1}",
            "global_coefficient": "[X^k](1-X)^a(1+X)^b=e_0^T prod_i M_i e_0 mod ell",
            "actual_exponents": "a=n=(p-1)/2, b=n+q=p-m-1, k=p",
            "diagonal_collapse": "at ell=p the product is the single distinguished transition M_0[0,1]=c_p followed by M_1[1,0]=1",
            "safe_saturation": "remove from G all prime powers supported by ingredient denominators or binom(2m,m); p-divisibility is unchanged",
        },
        "automaton_replay": automaton_replay(),
        "diagonal_replay": diagonal_replay(i331),
        "carrier_hit_replay": hit_replay(i318, i331, i334, i336),
        "character_counterexamples": character_counterexamples(i318, i331, i334, i336),
        "capacity": {
            "raw_fixed_M_chebyshev_mass": "(2/35)M+o(M)",
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "new_capacity_reduction": 0,
            "new_booking": 0,
            "required_next_input": (
                "weighted diagonal correlation for D=0 and "
                "c_p+epsilon_p*h_m*P_(r+2)(m)=Theta_(r,s), after safe saturation"
            ),
        },
        "scope_warning": (
            "Secondary-prime digit factorizations and the finite carrier hits do not "
            "bound tied-prime mass.  At ell=p the automaton returns c_p itself; a "
            "new target-correlated distribution theorem is required."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
