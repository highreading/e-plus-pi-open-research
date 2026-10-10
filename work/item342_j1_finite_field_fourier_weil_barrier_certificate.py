#!/usr/bin/env python3
"""Deterministic exact replay for Item 342.

Starting from Item 339's integral selected carrier a_(r,n), this checker
verifies the positive-power Frobenius chart, the exact three-alias theorem
over F_p, Euler-moment de-aliasing, and exact coefficient isolation over
F_(p^2).  It also verifies the terminating 4F3 chart on five preselected
rows.  No prime scan or density inference is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item342_j1_finite_field_fourier_weil_barrier_certificate.json"

DEPENDENCIES = {
    "sources/item339_j1_local_coefficient_carry_obstruction_report.md":
        "e36986e06dad00a45872b79f60e3f6f616195c93fa3faaef7dd6b4215aa7f472",
    "scripts/item339_j1_local_coefficient_carry_obstruction_certificate.py":
        "386da4d3fc1178ea1a2cb19f4c2ea326a824cb7addd4dbc976c4c9991745d040",
    "results/item339_j1_local_coefficient_carry_obstruction_certificate.json":
        "9d023a49aade705caf3bad274e9af30fb47172ebe18c1f9ba00b1a43f27d4ea3",
    "results/item339_j1_local_coefficient_carry_obstruction_certificate_replay.json":
        "9d023a49aade705caf3bad274e9af30fb47172ebe18c1f9ba00b1a43f27d4ea3",
    "results/item339_j1_local_coefficient_carry_obstruction_root_audit.json":
        "9b84d37c25f914afd24af60402cede2dec1da5321912247c570292babeed5ce9",
    "manifests/item339_j1_local_coefficient_carry_obstruction_manifest.json":
        "d62e21ca22f6ca000d18b6f655ea351f53f06ee287bb4b24c8a6cbd761414e97",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pin_dependencies()
ITEM339 = load_module(
    "item342_pinned_item339",
    ROOT / "scripts/item339_j1_local_coefficient_carry_obstruction_certificate.py",
)


def polynomial_multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            output[i + j] = (output[i + j] + a_value * b_value) % prime
    return output


def polynomial_power(base: list[int], exponent: int, prime: int) -> list[int]:
    output = [1]
    while exponent:
        if exponent & 1:
            output = polynomial_multiply(output, base, prime)
        base = polynomial_multiply(base, base, prime)
        exponent //= 2
    return output


def polynomial_value(coefficients: list[int], value: int, prime: int) -> int:
    output = 0
    for coefficient in reversed(coefficients):
        output = (output * value + coefficient) % prime
    return output


def euler_coefficients(coefficients: list[int], order: int, prime: int) -> list[int]:
    if order == 0:
        return coefficients
    return [pow(index, order, prime) * value % prime for index, value in enumerate(coefficients)]


def base_field_moments(coefficients: list[int], n: int, prime: int) -> list[int]:
    moments = []
    for order in range(3):
        theta = euler_coefficients(coefficients, order, prime)
        total = 0
        for value in range(1, prime):
            total += pow(value, prime - 1 - n, prime) * polynomial_value(theta, value, prime)
        moments.append(total % prime)
    return moments


def dealiased_target(moments: list[int], n: int, prime: int) -> int:
    return (
        -pow(2, -1, prime)
        * (
            moments[2]
            + (3 - 2 * n) * moments[1]
            + (n - 1) * (n - 2) * moments[0]
        )
    ) % prime


def least_nonsquare(prime: int) -> int:
    for value in range(2, prime):
        if pow(value, (prime - 1) // 2, prime) == prime - 1:
            return value
    raise AssertionError("nonsquare not found")


def fp2_operations(prime: int):
    nonsquare = least_nonsquare(prime)

    def add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        return ((left[0] + right[0]) % prime, (left[1] + right[1]) % prime)

    def multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        return (
            (left[0] * right[0] + nonsquare * left[1] * right[1]) % prime,
            (left[0] * right[1] + left[1] * right[0]) % prime,
        )

    def power(value: tuple[int, int], exponent: int) -> tuple[int, int]:
        output = (1, 0)
        while exponent:
            if exponent & 1:
                output = multiply(output, value)
            value = multiply(value, value)
            exponent //= 2
        return output

    return nonsquare, add, multiply, power


def extension_fourier_moment(n: int, r: int, prime: int) -> tuple[int, int, int]:
    """Sum x^(-n)G(x)^(p-r) over F_(p^2)^*."""
    nonsquare, add, multiply, power = fp2_operations(prime)
    total = (0, 0)
    exponent = prime - r
    q_minus_one = prime * prime - 1
    for first in range(prime):
        for second in range(prime):
            value = (first, second)
            if value == (0, 0):
                continue
            square = multiply(value, value)
            cube = multiply(square, value)
            g_value = add(
                add(
                    add((1, 0), ((-4 * first) % prime, (-4 * second) % prime)),
                    ((6 * square[0]) % prime, (6 * square[1]) % prime),
                ),
                ((-4 * cube[0]) % prime, (-4 * cube[1]) % prime),
            )
            term = multiply(
                power(value, q_minus_one - n), power(g_value, exponent)
            )
            total = add(total, term)
    return nonsquare, total[0], total[1]


def rising(value: Fraction, length: int) -> Fraction:
    output = Fraction(1)
    for index in range(length):
        output *= value + index
    return output


def hypergeometric_4f3(r: int, n: int) -> Fraction:
    upper = [Fraction(j - n, 4) for j in range(4)]
    lower = [Fraction(r, 1) + Fraction(j, 4) for j in (1, 2, 3)]
    total = Fraction(0)
    for k in range(n // 4 + 1):
        term = Fraction(1, 1)
        for parameter in upper:
            term *= rising(parameter, k)
        for parameter in lower:
            term /= rising(parameter, k)
        term /= factorial(k)
        total += term
    return Fraction(comb(4 * r + n - 1, n), 1) * total


def symbolic_audit() -> dict[str, Any]:
    h, s, n, r, M, p, u = S.symbols("h s n r M p u", integer=True)
    k = S.symbols("k", integer=True, nonnegative=True)
    substitutions = {
        n: 2 * h,
        r: 2 * s + 1,
        M: 3 * h + 4 * s + 2,
        p: 4 * h + 6 * s + 3,
    }
    identities = {
        "p": p - 2 * n - 3 * r,
        "2M": 2 * M - 3 * n - 4 * r,
        "positive_exponent": p - r - 2 * (r + n),
        "degree": 3 * (p - r) - (2 * p + 2 * n),
    }
    if any(S.expand(value.subs(substitutions)) != 0 for value in identities.values()):
        raise AssertionError("actual-row identities")

    D = 2 * p + 2 * n
    if S.expand((D - (n + 2 * (p - 1))).subs(substitutions) - (n + 2).subs(substitutions)) != 0:
        raise AssertionError("third alias lies in degree")
    if S.expand((D - (n + 3 * (p - 1))).subs(substitutions) - (3 - 3 * r - n).subs(substitutions)) != 0:
        raise AssertionError("fourth alias lies above degree")

    G = 1 - 4 * u + 6 * u**2 - 4 * u**3
    theta_G = S.expand(u * S.diff(G, u))
    theta2_G = S.expand(u * S.diff(theta_G, u))
    if S.expand(theta2_G + 4 * u * (1 - 3 * u) ** 2) != 0:
        raise AssertionError("theta^2 G factorization")
    if S.gcd(G, S.diff(G, u)) != 1:
        raise AssertionError("G is not squarefree over Q")

    original_ratio = S.cancel(
        (r + k) / (k + 1)
        * S.prod(n - 4 * k - j for j in range(4))
        / S.prod(4 * r + 4 * k + j for j in range(4))
    )
    hypergeometric_ratio = S.cancel(
        S.prod(k + S.Rational(j, 4) - n / 4 for j in range(4))
        / (
            (k + r + S.Rational(1, 4))
            * (k + r + S.Rational(1, 2))
            * (k + r + S.Rational(3, 4))
            * (k + 1)
        )
    )
    if S.cancel(original_ratio - hypergeometric_ratio) != 0:
        raise AssertionError("terminating 4F3 term ratio")

    return {
        "actual_parameters": {
            "n": "2h",
            "r": "2s+1",
            "p": "2n+3r",
            "2M": "3n+4r",
        },
        "positive_power_frobenius":
            "[u^n]G^(-r)=[u^n]G^(p-r) mod p because G^p=G(u^p) and n<p",
        "positive_exponent": "p-r=2(r+n)",
        "degree": "D=3(p-r)=2p+2n",
        "base_field_alias_indices": ["n", "n+p-1", "n+2(p-1)"],
        "no_fourth_alias": "D-(n+3(p-1))=3-3r-n<0",
        "Euler_dealiasing":
            "c_n=-(S_2+(3-2n)S_1+(n-1)(n-2)S_0)/2, S_j=sum_(x in F_p^*)x^(-n)(theta^j H)(x)",
        "extension_isolation":
            "c_n=-sum_(x in F_(p^2)^*)x^(-n)G(x)^(p-r), since D<p^2-1",
        "terminating_hypergeometric":
            "a_(r,n)=C(4r+n-1,n) 4F3((-n/4,(1-n)/4,(2-n)/4,(3-n)/4);(r+1/4,r+1/2,r+3/4);1)",
        "theta2_G": str(S.factor(theta2_G)),
        "G_squarefree_over_Q": True,
        "hypergeometric_term_ratio_verified_symbolically": True,
    }


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        (1, 1, 13, [0, 9, 12], [5, 4, 4], 0),
        (2, 1, 17, [8, 14, 15], [14, 15, 9], 8),
        (8, 2, 47, [0, 22, 33], [39, 7, 3], 0),
        (4, 4, 43, [2, 2, 1], [38, 7, 39], 2),
        (2, 6, 47, [36, 35, 42], [28, 43, 22], 36),
    ]
    output = []
    for h, s, prime, expected_aliases, expected_moments, expected_target in declared:
        n = 2 * h
        r = 2 * s + 1
        M = 3 * h + 4 * s + 2
        exponent = prime - r
        coefficients = polynomial_power([1, -4 % prime, 6, -4 % prime], exponent, prime)
        degree = len(coefficients) - 1
        if degree != 2 * prime + 2 * n or degree >= prime * prime - 1:
            raise AssertionError("degree chart")
        aliases = [coefficients[n + offset * (prime - 1)] for offset in range(3)]
        if aliases != expected_aliases:
            raise AssertionError(("declared aliases", h, s, prime))

        moments = base_field_moments(coefficients, n, prime)
        if moments != expected_moments:
            raise AssertionError(("declared base moments", h, s, prime))
        if moments[0] != (-sum(aliases)) % prime:
            raise AssertionError("plain Fourier alias sum")
        recovered = dealiased_target(moments, n, prime)
        if recovered != aliases[0] or recovered != expected_target:
            raise AssertionError("Euler de-aliasing")

        a_value = ITEM339.a_hypergeometric(r, n)
        if a_value % prime != recovered:
            raise AssertionError("Item339 target bridge")
        if hypergeometric_4f3(r, n) != a_value:
            raise AssertionError("terminating 4F3 identity")

        nonsquare, extension_real, extension_imaginary = extension_fourier_moment(
            n, r, prime
        )
        if extension_imaginary != 0 or (-extension_real) % prime != recovered:
            raise AssertionError("F_(p^2) coefficient isolation")

        output.append(
            {
                "classification": "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN",
                "M": M,
                "h": h,
                "s": s,
                "p": prime,
                "n": n,
                "r": r,
                "H_degree": degree,
                "three_alias_coefficients": aliases,
                "base_Euler_moments": moments,
                "dealiased_target": recovered,
                "F_p2_nonsquare": nonsquare,
                "F_p2_moment": [extension_real, extension_imaginary],
                "target_equals_Item339_a_mod_p": True,
                "full_original_collision_claimed": False,
            }
        )
    return output


def kummer_and_capacity() -> dict[str, Any]:
    return {
        "base_field_plain_Fourier": {
            "statement":
                "the plain multiplicative moment over F_p sees c_n+c_(n+p-1)+c_(n+2p-2), not c_n alone",
            "scope":
                "a square-root bound for that one complete sum has no actual-gate implication without controlling two unforced aliases",
        },
        "extension_field_exact_Fourier": {
            "statement":
                "over F_(p^2), degree D<p^2-1 and one pure multiplicative Fourier moment isolates c_n exactly",
            "Weil_scale": "sqrt(p^2)=p",
            "scope":
                "a black-box O(p) Weil bound cannot exclude divisibility by p, even after rational descent",
        },
        "base_field_Euler_dealiasing": {
            "statement":
                "three Euler moments over F_p invert the three aliases by a 3x3 Vandermonde identity",
            "Kummer_lift":
                "after expanding theta^j(G^(p-r)), the target has an algebraic-integer lift T in Z[zeta_(p-1)] made from four fixed-support full-Teichmueller Kummer sums",
            "support_counts": {
                "x^(-n)G^(p-r)": 5,
                "x^(-n)(theta G)G^(p-r-1)": 7,
                "x^(-n)(theta^2 G)G^(p-r-1)": 6,
                "x^(-n)(theta G)^2G^(p-r-2)": 7,
            },
            "uniform_conjugate_bound": "|sigma(T)|<=21 sqrt(p)",
            "cyclotomic_degree": "[Q(zeta_(p-1)):Q]=phi(p-1), unbounded",
            "norm_barrier":
                "T in one chosen prime above p only implies p|Norm(T), compatible with |Norm(T)|<=(21 sqrt(p))^phi(p-1)",
        },
        "scoped_no_go": {
            "closed": [
                "plain base-field coefficient Fourier extraction plus a Weil bound",
                "extension-field coefficient isolation plus a black-box square-root Weil bound",
                "Euler de-aliasing plus conjugate-size bounds alone, without p-adic nonconcentration or descent",
            ],
            "not_closed": [
                "a p-adic unit-root or chosen-prime nonconcentration theorem for the Kummer lift",
                "rational or bounded-degree descent together with a trace nonzero theorem",
                "correlations among the three aliases forced by additional actual-family arithmetic",
                "average gcd or factor localization for the Item339 rational carrier",
            ],
        },
        "capacity": {
            "support_reached": "all actual fixed-j1 rows",
            "raw_fixed_j1_prime_mass": "M/6+o(M)",
            "proved_mass_excluded_by_complex_bounds": 0,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item342-j1-finite-field-fourier-weil-barrier-certificate-v1",
        "item": 342,
        "date": "2026-09-01",
        "status": "PROVED_EXACT_FINITE_FIELD_KUMMER_LIFT_AND_SCOPED_FOURIER_WEIL_NO_GO",
        "dependencies": DEPENDENCIES,
        "symbolic": symbolic_audit(),
        "kummer_and_capacity": kummer_and_capacity(),
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "positive-power Frobenius chart H=G^(p-r) and exact degree D=2p+2n",
                "exact three-alias theorem for the plain F_p Fourier moment",
                "exact three-Euler-moment de-aliasing identity",
                "exact coefficient isolation by one F_(p^2) Fourier moment",
                "terminating 4F3 representation of the Item339 positive prefix",
                "fixed-support Kummer lift with a 21 sqrt(p) conjugate bound",
                "scoped Fourier/Weil/norm obstruction",
            ],
            "EXACT_FINITE_ONLY": [
                "five preselected F_p and F_(p^2) replay rows; no scan or density inference"
            ],
            "OPEN": [
                "p-adic nonconcentration at the chosen prime above p",
                "bounded-degree descent and exact trace nonvanishing",
                "W_b(M)=o(M) or any strict fixed-j1 ceiling reduction",
                "fixed-j1 closure, Route 1, and every conclusion about e+pi",
            ],
        },
        "canonical_files_modified": False,
        "prime_scans": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "item": 342,
                "base_alias_count": 3,
                "Euler_dealiasing": "PROVED",
                "F_p2_isolation": "PROVED",
                "Weil_only_capacity_gain": 0,
                "weighted_density": "OPEN",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
