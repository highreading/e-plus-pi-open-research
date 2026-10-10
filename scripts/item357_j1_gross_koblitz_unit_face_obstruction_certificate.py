#!/usr/bin/env python3
"""Deterministic exact replay for Item 357.

This checker verifies the target-specific F_(p^2) Jacobi/Appell transform,
the Gross--Koblitz/Stickelberger unit-face criterion, the exact triangular
leading-face reduction back to the selected Hasse coefficient, and two
predeclared valuation-one selected-zero controls.  No prime scan or density
inference is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any, Callable

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item357_j1_gross_koblitz_unit_face_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item353_j1_chosen_prime_first_digit_obstruction_report.md":
        "8b2bf4ab2df535e8016860fafdcaea40092a7a3c5dfdd59b84efd7e7a1e9fd7c",
    "scripts/item353_j1_chosen_prime_first_digit_obstruction_certificate.py":
        "3f35b8604b0210a66ddb1e8d740132c65f3fa0a74d8e3ddbf0e9785a0f9a62cf",
    "results/item353_j1_chosen_prime_first_digit_obstruction_certificate.json":
        "7a427d4c4a7f4ac7bc1f8a86e742b482b2fab83b5f2145f577159c5d844d87ca",
    "results/item353_j1_chosen_prime_first_digit_obstruction_certificate_replay.json":
        "7a427d4c4a7f4ac7bc1f8a86e742b482b2fab83b5f2145f577159c5d844d87ca",
    "results/item353_j1_chosen_prime_first_digit_obstruction_root_replay.json":
        "7a427d4c4a7f4ac7bc1f8a86e742b482b2fab83b5f2145f577159c5d844d87ca",
    "results/item353_j1_chosen_prime_first_digit_obstruction_ledger_delta.json":
        "2919c43ac141c0d2a0151d79f92bb05c52f67f9acee54c6bd2c2b86704088219",
    "results/item353_j1_chosen_prime_first_digit_obstruction_self_audit.json":
        "3597dc8a65064d3e6ff2d4ba3cb2120a0811d3e81ea2b0e422223bb020852dd0",
    "results/item353_j1_chosen_prime_first_digit_obstruction_root_audit.json":
        "61a15a35404078cf0d468cf7cb26610ddbcc2e03a33c1658ff3800c57cf43a0a",
    "manifests/item353_j1_chosen_prime_first_digit_obstruction_manifest.json":
        "0cea5de54d196d51869968f79dbe0f1a22781c05484effb5d913a9a25ec912f8",
    "sources/item356_j1_fermat_multiplicative_collapse_obstruction_report.md":
        "ae86c45748d8f084e2936829be191d4ea3f94e2450d7037c7ee7b8a841d500db",
    "scripts/item356_j1_fermat_multiplicative_collapse_obstruction_certificate.py":
        "698312a8ac3154c7843bbff8d0704f956e29f8eeb8fb19cc59c0557bcf1d2d92",
    "results/item356_j1_fermat_multiplicative_collapse_obstruction_certificate.json":
        "55deee2845bd9405964afa5508523ba9cb59f7ee0e39f86e2d3b873db9bba6a1",
    "results/item356_j1_fermat_multiplicative_collapse_obstruction_certificate_replay.json":
        "55deee2845bd9405964afa5508523ba9cb59f7ee0e39f86e2d3b873db9bba6a1",
    "results/item356_j1_fermat_multiplicative_collapse_obstruction_root_replay.json":
        "55deee2845bd9405964afa5508523ba9cb59f7ee0e39f86e2d3b873db9bba6a1",
    "results/item356_j1_fermat_multiplicative_collapse_obstruction_ledger_delta.json":
        "815fa2db3b1a67eb02adf589260a25064d40352feebcd3db155e5cab3d707467",
    "results/item356_j1_fermat_multiplicative_collapse_obstruction_self_audit.json":
        "53ab3cd3ebfcb53f3c81c683d1ffcec4d864ae7f48fb0e6a12cc53091071510c",
    "results/item356_j1_fermat_multiplicative_collapse_obstruction_root_audit.json":
        "b92125322d150a941a302d2dfef936a7014b5cb5a8a5e4899eceb56d3a872ac9",
    "manifests/item356_j1_fermat_multiplicative_collapse_obstruction_manifest.json":
        "d181ec76c8bf9ee3f15d655f1d0fe2fa48b01d925b3a0d6c82079ac8cbbb431e",
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
ITEM353 = load_module(
    "item357_pinned_item353",
    ROOT / "scripts/item353_j1_chosen_prime_first_digit_obstruction_certificate.py",
)
ITEM342 = ITEM353.ITEM342
ITEM339 = ITEM353.ITEM339


def digit_sum_p2(value: int, prime: int) -> int:
    if not 0 <= value < prime * prime:
        raise AssertionError("two-digit range")
    return value % prime + value // prime


def jacobi_valuation(m: int, exponent: int, prime: int) -> int:
    """v_p J(Omega^(-m),Omega^E), with q=p^2 and 0<=m<q-1.

    The two exceptional unit cases m=0 and m=E are handled directly.
    All other cases use the Gross--Koblitz/Stickelberger digit formula.
    """
    q_minus_one = prime * prime - 1
    if not (0 <= m < q_minus_one and 0 < exponent < prime):
        raise AssertionError("Jacobi parameter range")
    if m in (0, exponent):
        return 0
    shifted = (m - exponent) % q_minus_one
    numerator = (
        digit_sum_p2(m, prime)
        + digit_sum_p2(q_minus_one - exponent, prime)
        - digit_sum_p2(shifted, prime)
    )
    if numerator % (prime - 1):
        raise AssertionError("nonintegral Stickelberger valuation")
    return numerator // (prime - 1)


def least_nonsquare(prime: int) -> int:
    for value in range(2, prime):
        if pow(value, (prime - 1) // 2, prime) == prime - 1:
            return value
    raise AssertionError("nonsquare not found")


Pair = tuple[int, int]


def quadratic_operations(
    prime: int, modulus: int
) -> tuple[
    int,
    Callable[[Pair, Pair], Pair],
    Callable[[Pair, Pair], Pair],
    Callable[[Pair, int], Pair],
]:
    nonsquare = least_nonsquare(prime)

    def add(left: Pair, right: Pair) -> Pair:
        return (
            (left[0] + right[0]) % modulus,
            (left[1] + right[1]) % modulus,
        )

    def multiply(left: Pair, right: Pair) -> Pair:
        return (
            (left[0] * right[0] + nonsquare * left[1] * right[1]) % modulus,
            (left[0] * right[1] + left[1] * right[0]) % modulus,
        )

    def power(value: Pair, exponent: int) -> Pair:
        output = (1, 0)
        while exponent:
            if exponent & 1:
                output = multiply(output, value)
            value = multiply(value, value)
            exponent //= 2
        return output

    return nonsquare, add, multiply, power


def scalar(value: int, element: Pair, modulus: int) -> Pair:
    return (value * element[0] % modulus, value * element[1] % modulus)


def sqrt_minus_one(
    prime: int,
    multiply: Callable[[Pair, Pair], Pair],
) -> Pair:
    target = (prime - 1, 0)
    for first in range(prime):
        for second in range(prime):
            candidate = (first, second)
            if multiply(candidate, candidate) == target:
                return candidate
    raise AssertionError("sqrt(-1) not found in F_(p^2)")


def g_value(
    value: Pair,
    prime: int,
    add: Callable[[Pair, Pair], Pair],
    multiply: Callable[[Pair, Pair], Pair],
) -> Pair:
    square = multiply(value, value)
    cube = multiply(square, value)
    return add(
        add(
            add((1, 0), scalar(-4, value, prime)),
            scalar(6, square, prime),
        ),
        scalar(-4, cube, prime),
    )


def direct_jacobi_reduction(
    m: int,
    exponent: int,
    prime: int,
    add: Callable[[Pair, Pair], Pair],
    multiply: Callable[[Pair, Pair], Pair],
    power: Callable[[Pair, int], Pair],
) -> Pair:
    q_minus_one = prime * prime - 1
    total = (0, 0)
    for first in range(prime):
        for second in range(prime):
            z = (first, second)
            if z == (0, 0):
                continue
            one_minus_z = ((1 - first) % prime, (-second) % prime)
            term = multiply(
                power(z, (-m) % q_minus_one),
                power(one_minus_z, exponent),
            )
            total = add(total, term)
    return total


def extension_teichmueller_sum_mod_p2(n: int, r: int, prime: int) -> Pair:
    """The target-specific F_(p^2) Kummer lift modulo p^2."""
    q = prime * prime
    q_minus_one = q - 1
    exponent = prime - r
    _, add_field, multiply_field, power_field = quadratic_operations(prime, prime)
    _, add_ring, _, power_ring = quadratic_operations(prime, prime * prime)
    total = (0, 0)
    for first in range(prime):
        for second in range(prime):
            x = (first, second)
            if x == (0, 0):
                continue
            residue = multiply_field(
                power_field(x, q_minus_one - n),
                power_field(
                    g_value(x, prime, add_field, multiply_field), exponent
                ),
            )
            if residue == (0, 0):
                teichmueller = (0, 0)
            else:
                teichmueller = power_ring(residue, q)
            total = add_ring(total, teichmueller)
    return total


def polynomial_multiply_pairs(
    left: list[Pair],
    right: list[Pair],
    add: Callable[[Pair, Pair], Pair],
    multiply: Callable[[Pair, Pair], Pair],
) -> list[Pair]:
    output = [(0, 0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] = add(
                output[i + j], multiply(left_value, right_value)
            )
    return output


def triangle_reduction(n: int, r: int, prime: int) -> dict[str, Any]:
    exponent = prime - r
    _, add, multiply, power = quadratic_operations(prime, prime)
    imaginary = sqrt_minus_one(prime, multiply)
    inverse_two = pow(2, -1, prime)
    a = scalar(inverse_two, add((1, 0), imaginary), prime)
    b = scalar(inverse_two, add((1, 0), scalar(-1, imaginary, prime)), prime)

    product = [(1, 0)]
    for root_parameter in ((1, 0), a, b):
        product = polynomial_multiply_pairs(
            product, [(1, 0), root_parameter], add, multiply
        )
    expected_product = [
        (1, 0),
        (2 % prime, 0),
        (3 * inverse_two % prime, 0),
        (inverse_two, 0),
    ]
    if product != expected_product:
        raise AssertionError("factor product G(-z/2)")

    powers_a = [power(a, index) for index in range(n + 1)]
    powers_b = [power(b, index) for index in range(n + 1)]
    total = (0, 0)
    for s in range(n + 1):
        for t in range(n - s + 1):
            u = n - s - t
            coefficient = (
                comb(exponent, s)
                * comb(exponent, t)
                * comb(exponent, u)
            ) % prime
            term = scalar(
                coefficient,
                multiply(powers_a[t], powers_b[u]),
                prime,
            )
            total = add(total, term)

    sign = -1 if (n + 3) % 2 else 1
    scaled = scalar(sign * pow(2, n, prime), total, prime)
    target = ITEM339.a_hypergeometric(r, n) % prime
    if scaled != ((-target) % prime, 0):
        raise AssertionError("unit face does not reduce to negative target")

    return {
        "sqrt_minus_one": list(imaginary),
        "a": list(a),
        "b": list(b),
        "factor_product_coefficients": [list(value) for value in product],
        "unscaled_triangle_sum": list(total),
        "scaled_unit_face": list(scaled),
        "negative_selected_Hasse_coordinate": [(-target) % prime, 0],
    }


def fractional_part(value: Fraction) -> Fraction:
    return value - value.numerator // value.denominator


def classical_character_skeleton(n: int, r: int, prime: int) -> dict[str, Any]:
    upper = [Fraction(index - n, 4) for index in range(4)]
    lower_with_factorial = [
        Fraction(1),
        Fraction(r, 1) + Fraction(1, 4),
        Fraction(r, 1) + Fraction(1, 2),
        Fraction(r, 1) + Fraction(3, 4),
    ]
    upper_fractional = sorted(fractional_part(value) for value in upper)
    lower_fractional = sorted(
        fractional_part(value) for value in lower_with_factorial
    )
    expected = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]
    if upper_fractional != expected or lower_fractional != expected:
        raise AssertionError("fractional character skeleton")

    quotient, remainder = divmod(n, 4)
    if remainder == 0:
        distances = [quotient + 1] + [r + quotient] * 3
    elif remainder == 2:
        distances = [
            quotient + 1,
            r + quotient,
            r + quotient + 1,
            r + quotient + 1,
        ]
    else:
        raise AssertionError("actual n must be even")
    if sum(distances) != prime - n + 1:
        raise AssertionError("integer shift total")
    return {
        "upper_fractional_multiset": [str(value) for value in upper_fractional],
        "lower_plus_factorial_fractional_multiset": [
            str(value) for value in lower_fractional
        ],
        "integer_shift_distances": distances,
        "total_integer_shift": sum(distances),
        "character_only_Gauss_quotients": "cancel term by term",
    }


def symbolic_audit() -> dict[str, Any]:
    n, r, p, E, z = S.symbols("n r p E z", integer=True, positive=True)
    if S.expand((E - 2 * (n + r)).subs({E: p - r, p: 2 * n + 3 * r})) != 0:
        raise AssertionError("E identity")
    if S.expand((E - n).subs({E: p - r, p: 2 * n + 3 * r}) - (n + 2 * r)) != 0:
        raise AssertionError("E>n identity")

    a, b = S.symbols("a b")
    product = S.expand((1 + z) * (1 + a * z) * (1 + b * z))
    product = S.expand(product.subs({b: 1 - a, a * (1 - a): S.Rational(1, 2)}))
    # The direct substitution above need not reduce a^2.  Verify from the
    # symmetric expansion instead.
    symmetric_product = 1 + 2 * z + S.Rational(3, 2) * z**2 + S.Rational(1, 2) * z**3
    u = S.symbols("u")
    G = 1 - 4 * u + 6 * u**2 - 4 * u**3
    if S.expand(symmetric_product - G.subs(u, -z / 2)) != 0:
        raise AssertionError("cubic factor identity")

    return {
        "actual_parameters": {
            "p": "2n+3r",
            "E": "p-r=2(n+r)",
            "strict_inequality": "0<n<E<p",
        },
        "F_p2_factorization":
            "G(x)=(1-2x)(1-(1+i)x)(1-(1-i)x), i^2=-1",
        "scaled_parameters": "a=(1+i)/2, b=(1-i)/2, a+b=1, ab=1/2",
        "Jacobi_Fourier_transform":
            "S=Omega(2)^n/(q-1)^2 sum_(C,D) D(a)(bar(A)bar(C)bar(D))(b) J(bar(C),B)J(bar(D),B)J(ACD,B)",
        "characters": "A=Omega^(-n), B=Omega^E, q=p^2",
        "unit_criterion":
            "v_p J(Omega^(-m),Omega^E)=0 iff 0<=m<=E",
        "complete_unit_face": "s,t,u>=0 and s+t+u=n",
        "unit_face_cardinality": "(n+1)(n+2)/2",
        "unit_face_reduction":
            "-2^n sum_(s+t+u=n) C(E,s)C(E,t)C(E,u)a^t b^u=-[u^n]G(u)^E",
        "factor_identity": "(1+z)(1+az)(1+bz)=G(-z/2)",
    }


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        (1, 1, 13, 0, (143, 0), 11),
        (2, 1, 17, 8, (264, 0), None),
        (8, 2, 47, 0, (188, 0), 4),
        (4, 4, 43, 2, (428, 0), None),
        (2, 6, 47, 36, (199, 0), None),
    ]
    output = []
    for h, s, prime, expected_target, expected_lift, expected_quotient in declared:
        n = 2 * h
        r = 2 * s + 1
        M = 3 * h + 4 * s + 2
        exponent = prime - r
        q_minus_one = prime * prime - 1
        if prime != 2 * n + 3 * r or exponent != 2 * (n + r):
            raise AssertionError("actual row")

        target = ITEM339.a_hypergeometric(r, n) % prime
        if target != expected_target:
            raise AssertionError("declared target")

        unit_indices = [
            m for m in range(q_minus_one)
            if jacobi_valuation(m, exponent, prime) == 0
        ]
        if unit_indices != list(range(exponent + 1)):
            raise AssertionError("complete unit index interval")
        valuation_histogram: dict[str, int] = {}
        for m in range(q_minus_one):
            valuation = str(jacobi_valuation(m, exponent, prime))
            valuation_histogram[valuation] = valuation_histogram.get(valuation, 0) + 1

        face = [
            (first, second)
            for first in range(exponent + 1)
            for second in range(exponent + 1)
            if jacobi_valuation(
                (n - first - second) % q_minus_one,
                exponent,
                prime,
            ) == 0
        ]
        expected_face = [
            (first, second)
            for first in range(n + 1)
            for second in range(n - first + 1)
        ]
        if face != expected_face or len(face) != comb(n + 2, 2):
            raise AssertionError("complete triangular face")

        _, add, multiply, power = quadratic_operations(prime, prime)
        jacobi_reductions = []
        for m in range(n + 1):
            direct = direct_jacobi_reduction(
                m, exponent, prime, add, multiply, power
            )
            predicted = (((-1) ** (m + 1) * comb(exponent, m)) % prime, 0)
            if direct != predicted:
                raise AssertionError("Jacobi leading residue")
            jacobi_reductions.append(list(direct))

        triangle = triangle_reduction(n, r, prime)
        lift = extension_teichmueller_sum_mod_p2(n, r, prime)
        if lift != expected_lift or lift[0] % prime != (-target) % prime or lift[1] % prime:
            raise AssertionError("extension Kummer lift")
        quotient = None
        if target == 0:
            if lift[0] % prime or lift[1] % prime:
                raise AssertionError("selected-zero lift divisibility")
            quotient = [lift[0] // prime % prime, lift[1] // prime % prime]
            if quotient != [expected_quotient, 0] or quotient == [0, 0]:
                raise AssertionError("valuation-one selected-zero control")

        output.append(
            {
                "classification": "PREDECLARED EXACT CONTROL; NOT A PRIME SCAN",
                "M": M,
                "h": h,
                "s": s,
                "p": prime,
                "n": n,
                "r": r,
                "E": exponent,
                "selected_Hasse_coordinate": target,
                "full_original_collision_claimed": False,
                "Jacobi_valuation_histogram": valuation_histogram,
                "unit_Jacobi_indices": [0, exponent],
                "unit_Jacobi_index_count": len(unit_indices),
                "unit_face_size": len(face),
                "unit_face_size_formula": comb(n + 2, 2),
                "Jacobi_unit_reductions_m_0_to_n": jacobi_reductions,
                "triangle": triangle,
                "classical_character_skeleton": classical_character_skeleton(
                    n, r, prime
                ),
                "F_p2_Kummer_lift_mod_p2": list(lift),
                "selected_zero_quotient_if_applicable": quotient,
                "valuation_one_selected_zero_if_applicable": quotient is not None,
            }
        )
    return output


def capacity_and_scope() -> dict[str, Any]:
    return {
        "admission": {
            "actual_family": "n=2h, r=2s+1, p=2n+3r, 2M=3n+4r",
            "raw_support": "all actual fixed-j1 rows",
            "raw_fixed_j1_prime_mass": "M/6+o(M)",
            "maximum_retained_ceiling_per_6M": "1/36",
            "universal_nonvanishing_targeted": False,
        },
        "positive_rate_face_complexity": {
            "exact_unit_face_size": "C(n+2,2)",
            "zero_rate_edge": "Item339 proves rows with n=o(M) have weighted mass o(M)",
            "bulk_consequence":
                "outside that zero-rate edge the first Stickelberger face is not bounded; for n>=eta M it has at least eta^2 M^2/2+O(M) terms",
        },
        "scoped_no_go": {
            "closed": [
                "a unique-minimal-term or bounded-leading-face Gross--Koblitz proof for the target-specific F_(p^2) transform",
                "claiming a second collision condition from the first Stickelberger face",
                "the naive finite-character translation of the classical terminating 4F3 after discarding its integer shifts",
            ],
            "reason":
                "the complete first face is a triangular cancellation whose exact reduction is the already-booked selected Hasse coordinate; two selected-zero controls have valuation exactly one in this target-specific lift",
            "not_closed": [
                "nonconcentration or monodromy for the triangular face along the tied family",
                "an average theorem for higher Stickelberger faces",
                "a p-adic transformation retaining and exploiting the moving integer shifts",
                "additional information genuinely forced by the full original collision",
            ],
        },
        "ledger": {
            "new_forced_independent_condition": 0,
            "new_proved_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
            "retained_ceiling_per_6M": "1/36",
            "route_1_status": "ACTIVE",
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item357-j1-gross-koblitz-unit-face-obstruction-certificate-v1",
        "item": 357,
        "date": "2026-09-01",
        "status": "PROVED_TARGET_SPECIFIC_JACOBI_TRANSFORM_AND_COMPLETE_STICKELBERGER_FACE_SCOPED_NO_GO",
        "dependencies": DEPENDENCIES,
        "symbolic": symbolic_audit(),
        "capacity_and_scope": capacity_and_scope(),
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "exact target-specific two-frequency Jacobi/Appell transform over F_(p^2)",
                "complete Gross--Koblitz/Stickelberger unit criterion",
                "complete triangular unit-face theorem and exact cardinality",
                "exact reduction of that face to the already-booked Hasse coordinate",
                "quadratic positive-rate leading-face obstruction",
                "scoped unique-minimum/bounded-face Gross--Koblitz no-go",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "five predeclared rows and two valuation-one selected-zero extension-lift controls; no prime scan"
            ],
            "OPEN": [
                "weighted nonconcentration for the triangular Hasse face",
                "higher-face average cancellation",
                "a p-adic transformation exploiting the integer parameter shifts",
                "an additional gate from full-collision information",
                "W_b(M)=o(M), any fixed-j1 ceiling reduction, Route 1, and every conclusion about e+pi",
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
                "item": 357,
                "unit_face_size": "(n+1)(n+2)/2",
                "unit_face_equals_selected_Hasse_coordinate": True,
                "second_forced_condition": 0,
                "booking": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
