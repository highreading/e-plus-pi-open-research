#!/usr/bin/env python3
"""Exact certificate for Item 177's actual fixed-band B0 slices.

This checker derives the characteristic-p primitives on the two minimal
parity slices (j,s)=(1,1),(2,0), evaluates their constrained five-divisor
values, contracts them with Item 175's exact Q(i)-coordinate weights, and
replays representative Hasse digits.  No scalar representative is used in
place of the exact integer coefficient before reduction.
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
DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    HERE / "item177_actual_fixed_band_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item177_actual_fixed_band_certificate.json"
)
ITEM175_PATH = HERE / "item175_fixed_band_certificate.py"
ITEM163_PATH = HERE / "item163_deeper_digits_certificate.py"

G = tuple[Fraction, Fraction]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))
I: G = (Fraction(0), Fraction(1))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def g(value: int | Fraction) -> G:
    return Fraction(value), Fraction(0)


def gadd(left: G, right: G) -> G:
    return left[0] + right[0], left[1] + right[1]


def gneg(value: G) -> G:
    return -value[0], -value[1]


def gmul(left: G, right: G) -> G:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gscale(value: G, scalar: int | Fraction) -> G:
    scalar = Fraction(scalar)
    return value[0] * scalar, value[1] * scalar


def ginv(value: G) -> G:
    norm = value[0] * value[0] + value[1] * value[1]
    if not norm:
        raise ZeroDivisionError(value)
    return value[0] / norm, -value[1] / norm


def gpow(value: G, exponent: int) -> G:
    if exponent < 0:
        return gpow(ginv(value), -exponent)
    answer = ONE
    while exponent:
        if exponent & 1:
            answer = gmul(answer, value)
        exponent >>= 1
        if exponent:
            value = gmul(value, value)
    return answer


def conjugate(value: G) -> G:
    return value[0], -value[1]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def gaussian_text(value: G) -> list[str]:
    return [fraction_text(value[0]), fraction_text(value[1])]


def polynomial_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    degree = max(len(left), len(right))
    answer = [Fraction(0)] * degree
    for index in range(degree):
        answer[index] = (
            left[index] if index < len(left) else 0
        ) + (right[index] if index < len(right) else 0)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def polynomial_scale(poly: list[Fraction], scalar: int | Fraction) -> list[Fraction]:
    return [Fraction(scalar) * value for value in poly]


def polynomial_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            answer[first + second] += left_value * right_value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def polynomial_derivative(poly: list[Fraction]) -> list[Fraction]:
    return [index * poly[index] for index in range(1, len(poly))] or [Fraction(0)]


def polynomial_evaluate_gaussian(poly: list[Fraction], value: G) -> G:
    answer = ZERO
    for coefficient in reversed(poly):
        answer = gadd(gmul(answer, value), g(coefficient))
    return answer


def factor_integer(integer: int) -> list[list[int]]:
    integer = abs(integer)
    factors = []
    prime = 2
    while prime * prime <= integer:
        if integer % prime == 0:
            exponent = 0
            while integer % prime == 0:
                integer //= prime
                exponent += 1
            factors.append([prime, exponent])
        prime = 3 if prime == 2 else prime + 2
    if integer > 1:
        factors.append([integer, 1])
    return factors


SLICE_DATA = {
    1: {
        "s": 1,
        "d": 6,
        "gamma0_mod_polynomial": 1260,
        "gamma1_mod_polynomial": 776,
        "B": [
            Fraction(484, 5), Fraction(290), Fraction(578), Fraction(952),
            Fraction(1132), Fraction(1106), Fraction(970), Fraction(388),
            Fraction(388),
        ],
    },
    2: {
        "s": 0,
        "d": 3,
        "gamma0_mod_polynomial": 10,
        "gamma1_mod_polynomial": 6,
        "B": [Fraction(2), Fraction(2), Fraction(3)],
    },
}


def exact_gamma(item175: Any, p: int, s: int) -> tuple[int, int]:
    r_value = p - 3 * s - 3
    h_value = 2 * s + 1
    degree = 3 * s + 2
    return (
        item175.four_section_exact(r_value - h_value, h_value, degree),
        item175.four_section_exact(r_value - h_value + 1, h_value - 1, degree),
    )


def derivative_identity(j: int) -> dict[str, Any]:
    data = SLICE_DATA[j]
    d_value = int(data["d"])
    gamma0 = int(data["gamma0_mod_polynomial"])
    gamma1 = int(data["gamma1_mod_polynomial"])
    b_poly = list(data["B"])
    u = [Fraction(0), Fraction(1), Fraction(-1)]
    u_prime = [Fraction(1), Fraction(-2)]
    q = [Fraction(1)] * 4

    left = polynomial_add(
        polynomial_multiply(u, polynomial_derivative(b_poly)),
        polynomial_scale(polynomial_multiply(u_prime, b_poly), -(d_value - 1)),
    )
    if j == 1:
        right = polynomial_multiply(
            polynomial_multiply(q, q),
            polynomial_add(polynomial_scale(q, gamma1), [Fraction(-gamma0)]),
        )
    else:
        right = polynomial_add(polynomial_scale(q, gamma1), [Fraction(-gamma0)])
    if left != right:
        raise AssertionError((j, left, right))
    # The convenient characteristic-p primitive can have an x^p term,
    # whereas Item 172's exact-integer primitive has literal x^p coefficient
    # zero.  Their difference is the displayed kernel multiple of x^p.
    kernel_coefficient = sum(
        b_poly[index]
        * math.comb(
            d_value + (d_value - 1 - index) - 2,
            d_value - 1 - index,
        )
        for index in range(min(len(b_poly), d_value))
    )
    return {
        "j": j,
        "identity": f"u*B' - {d_value-1}*u'*B = N",
        "B_coefficients": [fraction_text(value) for value in b_poly],
        "N_coefficients": [fraction_text(value) for value in right],
        "verified_over_Q": True,
        "convenient_primitive_representative_mod_p": f"That=u^(p-{d_value-1})*B",
        "coefficient_of_x_to_p_in_That": fraction_text(kernel_coefficient),
        "relation_to_exact_integer_primitive": (
            "Tbar=That-c*x^p, where c is the displayed coefficient; "
            "the kernel term contributes only a multiple of v_j and drops "
            "from both determinant wedges."
        ),
    }


def fixed_weights(item175: Any, j: int) -> dict[str, G]:
    base = item175.coordinates(j)
    answer = {}
    for name, divisor in (("-1", g(-1)), ("i", I), ("-i", gneg(I))):
        target = item175.coordinates(j, divisor)
        answer[name] = item175.wedge(base, target, 2, 1)
    return answer


def constrained_values(j: int, residue_mod_4: int) -> dict[str, G]:
    data = SLICE_DATA[j]
    d_value = int(data["d"])
    b_poly = list(data["B"])
    values = {}
    for name, root in (("-1", g(-1)), ("i", I), ("-i", gneg(I))):
        frobenius_root = root if residue_mod_4 == 1 else conjugate(root)
        u_root = gmul(root, gadd(ONE, gneg(root)))
        u_frobenius = gmul(
            frobenius_root, gadd(ONE, gneg(frobenius_root))
        )
        # u^(p-d+1)=u^p/u^(d-1).
        power = gmul(u_frobenius, gpow(u_root, -(d_value - 1)))
        values[name] = gmul(power, polynomial_evaluate_gaussian(b_poly, root))
    return values


def actual_constant(item175: Any, j: int, residue_mod_4: int) -> dict[str, Any]:
    data = SLICE_DATA[j]
    k_value = 2 * j + 2
    weights = fixed_weights(item175, j)
    values = constrained_values(j, residue_mod_4)
    total = ZERO
    terms = {}
    for name in ("-1", "i", "-i"):
        after_tau = values[name] if residue_mod_4 == 1 else conjugate(values[name])
        term = gscale(gmul(after_tau, weights[name]), -k_value)
        total = gadd(total, term)
        terms[name] = {
            "That": gaussian_text(values[name]),
            "tau_That": gaussian_text(after_tau),
            "weight_B": gaussian_text(weights[name]),
            "contracted_term": gaussian_text(term),
        }
    if total[1]:
        raise AssertionError((j, residue_mod_4, total))
    chi = 1 if residue_mod_4 == 1 else -1
    actual = chi * total[0]
    expected = {
        (1, 1): Fraction(2735, 4),
        (1, 3): Fraction(-5295, 4),
        (2, 1): Fraction(-918897, 128),
        (2, 3): Fraction(59829, 128),
    }[(j, residue_mod_4)]
    if actual != expected:
        raise AssertionError((j, residue_mod_4, actual, expected))
    return {
        "j": j,
        "s": int(data["s"]),
        "p_mod_4": residue_mod_4,
        "chi4": chi,
        "terms": terms,
        "raw_circular_contraction_before_chi4": fraction_text(total[0]),
        "actual_B0_constant": fraction_text(actual),
        "numerator_factorization": factor_integer(actual.numerator),
    }


def kernel_wedge_checks(item175: Any) -> list[dict[str, Any]]:
    """Check that changing a primitive by c*x^p drops from the B wedge."""
    rows = []
    for j in (1, 2):
        base = item175.coordinates(j)
        total = ZERO
        terms = []
        for name, divisor in (("1", g(1)), ("-1", g(-1)), ("i", I), ("-i", gneg(I))):
            n_value = 3 * j + 2 if name == "1" else -(2 * j + 2)
            weight = item175.wedge(base, item175.coordinates(j, divisor), 2, 1)
            # tau_p(a^p)=a in every residue class.
            term = gscale(gmul(divisor, weight), n_value)
            total = gadd(total, term)
            terms.append({"a": name, "term": gaussian_text(term)})
        if total != ZERO:
            raise AssertionError(("x^p kernel wedge", j, total))
        rows.append(
            {
                "j": j,
                "terms": terms,
                "sum": gaussian_text(total),
                "interpretation": "x^p primitive ambiguity is a scalar F_j differential modulo an endpoint-zero exact differential",
            }
        )
    return rows


def predicted_b0(j: int, p: int) -> int:
    constant = {
        (1, 1): Fraction(2735, 4),
        (1, 3): Fraction(-5295, 4),
        (2, 1): Fraction(-918897, 128),
        (2, 3): Fraction(59829, 128),
    }[(j, p % 4)]
    return constant.numerator * pow(constant.denominator, -1, p) % p


def primes_upto(limit: int) -> list[int]:
    answer = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, math.isqrt(value) + 1)):
            answer.append(value)
    return answer


def threshold_checks(item175: Any) -> dict[str, Any]:
    rows = []
    for j in (1, 2):
        s = int(SLICE_DATA[j]["s"])
        for p in primes_upto(1000):
            if p < 7:
                continue
            gamma = exact_gamma(item175, p, s)
            expected_gamma = (
                int(SLICE_DATA[j]["gamma0_mod_polynomial"]) % p,
                int(SLICE_DATA[j]["gamma1_mod_polynomial"]) % p,
            )
            if (gamma[0] % p, gamma[1] % p) != expected_gamma:
                raise AssertionError((j, p, gamma, expected_gamma))
            m = ((j + 1) * p - s - 1) // 2
            if 2 * m + 1 != (j + 1) * p - s:
                raise AssertionError((j, p, m))
            admissible = p <= 4 * m + 1 < p * p
            if not admissible:
                raise AssertionError(("e=1", j, p, m))
            value = predicted_b0(j, p)
            rows.append({"j": j, "s": s, "p": p, "m": m, "B0": value})
            if j == 1 and value == 0:
                raise AssertionError(("unexpected j=1 zero", p))
            if j == 2 and ((p in (7, 11)) != (value == 0)):
                raise AssertionError(("j=2 exception", p, value))
    return {
        "prime_check_limit": 1000,
        "j1_s1_zero_primes": [],
        "j2_s0_zero_primes": [7, 11],
        "theorem_from_factor_classes": {
            "j1_s1": "B0 is nonzero for every prime p>=7",
            "j2_s0": "B0 is nonzero for every prime p>=13; p=7,11 give B0=0",
        },
        "finite_formula_rows": rows,
    }


def hasse_replays(archive: Path, item163: Any) -> list[dict[str, Any]]:
    extended_path = archive / "scripts" / "lifted_endpoint_hasse_extended_certificate.py"
    extended = load_module("item177_extended", extended_path)
    controls = [(1, 7), (1, 13), (1, 19), (2, 7), (2, 11), (2, 13), (2, 19)]
    rows = []
    for j, p in controls:
        s = int(SLICE_DATA[j]["s"])
        m = ((j + 1) * p - s - 1) // 2
        l0, x0, e0, _ = item163.coordinates_mod(extended, m, 4 * m + 1, p, 2)
        l1, x1, e1, _ = item163.coordinates_mod(extended, m, 4 * m + 2, p, 2)
        determinant_b = (l1 * e0 - l0 * e1) % (p * p)
        actual = (determinant_b // p) % p
        predicted = predicted_b0(j, p)
        if actual != predicted:
            raise AssertionError(("Hasse B0", j, p, actual, predicted))
        rows.append(
            {
                "j": j,
                "s": s,
                "p": p,
                "m": m,
                "B0_Hasse": actual,
                "B0_closed_formula": predicted,
                "matched": True,
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not ITEM175_PATH.is_file() or not ITEM163_PATH.is_file():
        raise FileNotFoundError((ITEM175_PATH, ITEM163_PATH))
    item175 = load_module("item177_item175", ITEM175_PATH)
    item163 = load_module("item177_item163", ITEM163_PATH)

    constants = [
        actual_constant(item175, j, residue)
        for j in (1, 2)
        for residue in (1, 3)
    ]
    output = {
        "schema": "item177-actual-fixed-band-B0-v1",
        "status": {
            "actual_j1_s1_nonvanishing": "PROVED_IN_COMPANION_REPORT",
            "actual_j2_s0_classification": "PROVED_IN_COMPANION_REPORT",
            "positive_mass_consequence": "NONE; THESE_ARE_FIXED_RAYS",
            "A0_actual_slice": "NOT_CLASSIFIED",
        },
        "inputs": {
            "scripts/item175_fixed_band_certificate.py": sha256(ITEM175_PATH),
            "scripts/item163_deeper_digits_certificate.py": sha256(ITEM163_PATH),
            "scripts/lifted_endpoint_hasse_extended_certificate.py": sha256(
                args.archive / "scripts" / "lifted_endpoint_hasse_extended_certificate.py"
            ),
        },
        "exact_derivative_identities": [derivative_identity(j) for j in (1, 2)],
        "x_to_p_kernel_wedge_checks": kernel_wedge_checks(item175),
        "actual_constrained_constants": constants,
        "prime_threshold_checks": threshold_checks(item175),
        "exact_Hasse_normalization_replays": hasse_replays(args.archive, item163),
        "circular_sign_erratum": {
            "issue": (
                "The circular coordinate after Cartier carries chi4(p). "
                "Item172 (4.11) is correct for its zero set but its signed digit "
                "value needs an overall chi4(p) under the archive E convention; "
                "Item175 (4.1) and its signed coefficient (4.3) inherit the same factor."
            ),
            "proposed_formula": (
                "B0 = chi4(p) * sum_a tau_p(n_a*Tbar(a)) "
                "*(E_j*L_{j,a}-L_j*E_{j,a}) mod p"
            ),
            "zero_gate_changed": False,
            "item172_finite_counts_changed": False,
            "item175_nonvanishing_theorem_changed": False,
            "stored_Hasse_digits_changed": False,
        },
        "scope": {
            "proved": (
                "On actual constrained slices (j,s)=(1,1),(2,0), B0 is the "
                "displayed fixed rational constant according to p mod 4."
            ),
            "not_proved": (
                "No classification for other s or j, no A0/A1 theorem, and no "
                "positive-prime-mass content gain."
            ),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "Hasse_replays": len(output["exact_Hasse_normalization_replays"]),
                "j1_zeros": output["prime_threshold_checks"]["j1_s1_zero_primes"],
                "j2_zeros": output["prime_threshold_checks"]["j2_s0_zero_primes"],
                "output_sha256": sha256(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
