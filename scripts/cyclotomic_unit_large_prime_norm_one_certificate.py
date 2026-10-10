#!/usr/bin/env python3
"""Exact certificate for the primitive moving-target/norm-one obstruction.

This script verifies the divided-difference normalization, coefficient
primitivity, recurrence, resultant scalar cancellation, and finite-field
surjectivity statements in the companion note.  Witness data are read from
the already frozen boundary-resultant certificate and reconstructed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import sympy as sp

import algebraic_unit_two_log_n5_ideal_content as base
import cyclotomic_unit_large_prime_boundary_resultant as boundary


sys.set_int_max_str_digits(0)

Kelt = base.Kelt


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def r_coefficients(prime: int, r: int) -> list[int]:
    """Coefficients of R_{p,r}=sum_(k=r)^(p-1) (k!/r!)*L_k."""
    if not 0 <= r <= prime - 1:
        raise ValueError("r outside 0..p-1")
    if r == prime - 1:
        # L_(p-1) has degree p-2 and coefficient one throughout.
        return [1] * (prime - 1)
    ratios = [0] * prime
    ratios[r] = 1
    for k in range(r + 1, prime):
        ratios[k] = ratios[k - 1] * k
    suffix = [0] * (prime + 1)
    for k in range(prime - 1, r - 1, -1):
        suffix[k] = suffix[k + 1] + ratios[k]
    coefficients = []
    for j in range(prime - 1):
        coefficients.append(suffix[r] if j < r else suffix[j + 1])
    return coefficients


def l_coefficients(r: int, length: int) -> list[int]:
    return [1 if j < r else 0 for j in range(length)]


def pad(values: list[int], length: int) -> list[int]:
    return values + [0] * (length - len(values))


def recurrence_check(prime: int, r: int) -> bool:
    current = r_coefficients(prime, r)
    if r == prime - 1:
        following = [0] * len(current)  # R_(p,p)=0
    else:
        following = r_coefficients(prime, r + 1)
    length = max(len(current), len(following), r)
    current = pad(current, length)
    following = pad(following, length)
    ell = l_coefficients(r, length)
    return current == [
        ell[j] + (r + 1) * following[j] for j in range(length)
    ]


def quotient_mod_p(prime: int, r: int) -> list[int]:
    factorials = [1]
    for k in range(1, prime):
        factorials.append(factorials[-1] * k % prime)
    s_coefficients = [
        factorials[k] if k >= r else 0 for k in range(prime)
    ]
    return boundary.divide_by_y_minus_one(s_coefficients, prime)


def reduce_coefficients(values: list[int], prime: int) -> list[int]:
    return [value % prime for value in values]


def f_iota_mod(a: Kelt, prime: int) -> Kelt:
    c0, c1 = boundary.f_coordinates_mod(a, prime)
    return boundary.f_from_coordinates_mod(
        (c0 - c1) % prime, -c1 % prime, prime
    )


def f_multiply_coordinates(
    a: tuple[int, int], b: tuple[int, int], prime: int
) -> tuple[int, int]:
    # t^2=1-t for t=zeta_5+zeta_5^-1.
    a0, a1 = a
    b0, b1 = b
    return (
        (a0 * b0 + a1 * b1) % prime,
        (a0 * b1 + a1 * b0 - a1 * b1) % prime,
    )


def f_iota_coordinates(
    a: tuple[int, int], prime: int
) -> tuple[int, int]:
    a0, a1 = a
    return ((a0 - a1) % prime, -a1 % prime)


def f_norm_coordinates(a: tuple[int, int], prime: int) -> int:
    product = f_multiply_coordinates(
        a, f_iota_coordinates(a, prime), prime
    )
    if product[1] != 0:
        raise AssertionError("quadratic norm did not land in F_p")
    return product[0]


def f_inverse_coordinates(
    a: tuple[int, int], prime: int
) -> tuple[int, int]:
    norm = f_norm_coordinates(a, prime)
    if norm == 0:
        raise ZeroDivisionError("nonunit in the quadratic algebra")
    scalar = pow(norm, -1, prime)
    conjugate = f_iota_coordinates(a, prime)
    return (scalar * conjugate[0] % prime, scalar * conjugate[1] % prime)


def delta_coordinates(
    a: tuple[int, int], prime: int
) -> tuple[int, int]:
    return f_multiply_coordinates(
        f_iota_coordinates(a, prime),
        f_inverse_coordinates(a, prime),
        prime,
    )


def torus_surjectivity_record(prime: int) -> dict[str, object]:
    image: set[tuple[int, int]] = set()
    unit_count = 0
    norm_one_count = 0
    for a0 in range(prime):
        for a1 in range(prime):
            value = (a0, a1)
            norm = f_norm_coordinates(value, prime)
            if norm:
                unit_count += 1
                image.add(delta_coordinates(value, prime))
            if norm == 1:
                norm_one_count += 1
    expected = (
        prime - 1 if sp.legendre_symbol(5, prime) == 1 else prime + 1
    )
    if len(image) != expected or norm_one_count != expected:
        raise AssertionError("finite norm-one surjectivity failed")
    if any(f_norm_coordinates(value, prime) != 1 for value in image):
        raise AssertionError("delta image left the norm-one torus")
    return {
        "p": prime,
        "F_split": sp.legendre_symbol(5, prime) == 1,
        "quadratic_algebra_unit_count": unit_count,
        "delta_image_size": len(image),
        "norm_one_torus_size": norm_one_count,
        "expected_torus_size": expected,
        "surjective": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/cyclotomic_unit_large_prime_norm_one_certificate.json"
        ),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "sources/cyclotomic_unit_large_prime_norm_one_obstruction.md"
        ),
    )
    parser.add_argument(
        "--boundary-result",
        type=Path,
        default=Path(
            "results/cyclotomic_unit_large_prime_boundary_resultant_p2000.json"
        ),
    )
    args = parser.parse_args()

    boundary_result = json.loads(args.boundary_result.read_text())
    witnesses = boundary_result["finite_diagnostics"]["witness_records"]
    eta: Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    q_value = base.kmul(eta, eta_bar)
    z_value = base.kmul(
        (1, 1, 0, 0), (0, -1, -1, -1)
    )
    if base.kmul(q_value, z_value) != base.ONE:
        raise AssertionError("q inverse identity changed")

    witness_records = []
    for witness in witnesses:
        prime = int(witness["p"])
        degree = int(witness["d"])
        r = int(witness["r=p-1-d"])
        coefficients = r_coefficients(prime, r)
        if not recurrence_check(prime, r):
            raise AssertionError("R recurrence failed")
        if r + 1 <= prime - 1 and not recurrence_check(prime, r + 1):
            raise AssertionError("adjacent R recurrence failed")
        content = math.gcd(*(abs(value) for value in coefficients))
        if content != 1:
            raise AssertionError("R coefficients were not primitive")
        if r >= 1:
            if coefficients[r - 1] - coefficients[r] != 1:
                raise AssertionError("adjacent coefficient difference was not one")
        leading = math.factorial(prime - 1) // math.factorial(r)
        if coefficients[-1] != leading:
            raise AssertionError("leading factorial quotient failed")
        height = max(coefficients)
        if not leading <= height <= (degree + 1) * leading:
            raise AssertionError("projective height bounds failed")

        quotient = quotient_mod_p(prime, r)
        quotient_hash = hashlib.sha256(repr(quotient).encode()).hexdigest()
        if quotient_hash != witness["Q_coefficients_sha256"]:
            raise AssertionError("boundary Q hash changed")
        r_factorial_mod_p = math.factorial(r) % prime
        predicted_quotient = [
            r_factorial_mod_p * value % prime for value in coefficients
        ]
        if predicted_quotient != quotient:
            raise AssertionError("Q=r!*R reduction failed")

        resultant_q, _, _ = boundary.quadratic_resultant_mod(
            quotient, z_value, prime
        )
        resultant_r, _, _ = boundary.quadratic_resultant_mod(
            reduce_coefficients(coefficients, prime), z_value, prime
        )
        predicted_resultant_q = boundary.kscale_mod(
            r_factorial_mod_p**2, resultant_r, prime
        )
        if resultant_q != predicted_resultant_q:
            raise AssertionError("quadratic resultant scalar law failed")
        if list(boundary.f_coordinates_mod(resultant_q, prime)) != witness[
            "resultant_F_coordinates"
        ]:
            raise AssertionError("witness resultant coordinates changed")
        # Cross multiplication verifies equality of conjugate ratios without
        # making a field/split-algebra inversion assumption in this step.
        if boundary.kmul_mod(
            f_iota_mod(resultant_q, prime), resultant_r, prime
        ) != boundary.kmul_mod(
            f_iota_mod(resultant_r, prime), resultant_q, prime
        ):
            raise AssertionError("factorial scalar did not cancel in ratio")

        witness_records.append(
            {
                "p": prime,
                "d": degree,
                "r": r,
                "coefficient_count": len(coefficients),
                "coefficient_content": content,
                "adjacent_coefficients_differ_by_one": True,
                "leading_coefficient_digits": len(str(leading)),
                "projective_height_digits": len(str(height)),
                "height_over_leading_upper_multiplier": (
                    str(height // leading)
                ),
                "log_height": format(math.log(height), ".17g"),
                "log_factorial_quotient": format(math.log(leading), ".17g"),
                "Q_equals_r_factorial_times_R_mod_p": True,
                "resultant_Q_equals_r_factorial_squared_times_resultant_R": True,
                "conjugate_ratio_unchanged": True,
                "primitive_R_coefficients_sha256": hashlib.sha256(
                    repr(coefficients).encode()
                ).hexdigest(),
            }
        )

    # The split/inert examples independently enumerate every element of the
    # small quadratic algebra and verify surjectivity of x -> iota(x)/x.
    torus_records = [
        torus_surjectivity_record(13),
        torus_surjectivity_record(31),
    ]

    # Exercise the two boundary cases omitted by the cancellation witnesses:
    # r=0 and d=1 (r=p-2).  The d=1 case detects the corrected factor d+1
    # in the elementary height upper bound.
    edge_records = []
    for prime, r in ((7, 0), (7, 5)):
        degree = prime - 1 - r
        coefficients = r_coefficients(prime, r)
        content = math.gcd(*(abs(value) for value in coefficients))
        if content != 1 or not recurrence_check(prime, r):
            raise AssertionError("edge primitivity/recurrence failed")
        if r == 0:
            adjacent_difference = coefficients[0] - coefficients[1]
        else:
            adjacent_difference = coefficients[r - 1] - coefficients[r]
        if adjacent_difference != 1:
            raise AssertionError("edge adjacent difference failed")
        leading = math.factorial(prime - 1) // math.factorial(r)
        height = max(coefficients)
        if not leading <= height <= (degree + 1) * leading:
            raise AssertionError("corrected edge height bound failed")
        edge_records.append(
            {
                "p": prime,
                "d": degree,
                "r": r,
                "content": content,
                "adjacent_difference": adjacent_difference,
                "leading_coefficient": leading,
                "height": height,
                "corrected_upper_bound": (degree + 1) * leading,
            }
        )

    # A finite illustration of the growing ambient coefficient prime support.
    # The theorem itself is immediate from the leading interval product.
    ambient_support: set[int] = set()
    support_records = []
    for prime in (11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        leading = math.factorial(prime - 1)  # r=1
        factors = sorted(int(value) for value in sp.factorint(leading))
        ambient_support.update(factors)
        support_records.append(
            {"p": prime, "r": 1, "leading_prime_support": factors}
        )

    source_path = args.source.resolve()
    script_path = Path(__file__).resolve()
    boundary_result_path = args.boundary_result.resolve()
    dependencies = [
        Path(base.__file__).resolve(),
        Path(boundary.__file__).resolve(),
        boundary_result_path,
        Path(
            "sources/cyclotomic_unit_large_prime_boundary_resultant.md"
        ).resolve(),
    ]
    if not source_path.exists() or not all(path.exists() for path in dependencies):
        raise FileNotFoundError("source or dependency was missing")

    result = {
        "description": (
            "Exact divided-difference, primitive-height, bounded-recurrence, "
            "factorial-resultant cancellation, and norm-one torus certificate."
        ),
        "scope_warning": (
            "The identities and height bounds are all-degree statements. "
            "Finite witness/support/enumeration records illustrate them only; "
            "no uniform large-prime gcd bound is asserted."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependencies
        ],
        "proved_identities": {
            "integer_divided_difference": (
                "Qhat_(p,r)=sum_(k=r)^(p-1) k!*L_k(Y)"
            ),
            "primitive_normalization": "R_(p,r)=Qhat_(p,r)/r!",
            "recurrence": "R_(p,r)=L_r+(r+1)*R_(p,r+1), R_(p,p)=0",
            "coefficient_formula": (
                "c_j=sum_(k=max(r,j+1))^(p-1) k!/r!"
            ),
            "primitivity": (
                "c_(r-1)-c_r=1 for 1<=r<=p-2; "
                "c_0-c_1=1 for r=0"
            ),
            "height_bounds": (
                "(p-1)!/r! <= H(R) <= (p-r)*(p-1)!/r!"
            ),
            "resultant_scaling": "N_(p,r)=(r!)^2*M_(p,r) mod p",
            "torus_map": "delta_p(x)=iota(x)/x is surjective",
        },
        "witness_reconstructions": witness_records,
        "edge_case_reconstructions": edge_records,
        "finite_torus_surjectivity_enumerations": torus_records,
        "finite_ambient_coefficient_support_diagnostic": {
            "records": support_records,
            "union": sorted(ambient_support),
            "warning": (
                "The all-family non-fixed-S statement follows from the interval "
                "product, not from this finite list; no root-subsequence claim "
                "is made."
            ),
        },
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
