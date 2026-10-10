#!/usr/bin/env python3
"""Independent exact audit of the high-radius integral-jet pullback.

This program deliberately does not import either of the two programs under
audit.  It uses:

* SymPy Gaussian-rational polynomials for the Schur recursion;
* composition of the ordinary Taylor series of F with phi for the G jets;
* the full coefficient-plus-endpoint Hermite--Pade matrix for the primitive
  polynomial triple; and
* shorter, independently chosen exact Taylor/Machin intervals for e+pi.

The archived source programs use rational-complex pairs, direct division of
the rational function G', and a reduced high-derivative matrix.  Agreement
therefore cross-checks the claimed exact data by materially different routes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path

import sympy as sp
import mpmath as mp
from sympy.polys.matrices import DomainMatrix


sys.set_int_max_str_digits(0)


FROZEN_HASHES = {
    "sources/high_radius_composed_integral_jet_pullback.md":
        "0f1a41bb40ec457e51f1b0c1fa5299de784f93a3c7f92bc372bcad2fff7e7b87",
    "scripts/high_radius_composed_pullback_certificate.py":
        "ed1e0e6c92392f0fa27f5fbe6e00603151c22ed1ec05d3eaaed9e0211ae7fce4",
    "results/high_radius_composed_pullback_certificate.json":
        "b3bbdda30c993a122dc056cc137689ee9281d4ecc11efabac69174891c348e23",
    "scripts/high_radius_composed_pullback_hp_probe.py":
        "f7cb212ebb4b9e79cc08486c8d090e36e9245144e24ffc06aca120699149963d",
    "results/high_radius_composed_pullback_hp_n15.json":
        "831626a38451e3a060f1e790038a27935c226210cb6fc4bf0c4fae448f6e772d",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_json_vector(values: list[int]) -> str:
    data = json.dumps(values, separators=(",", ":")).encode()
    return sha256_bytes(data)


def primitive(values: list[sp.Rational]) -> list[int]:
    denominator = sp.ilcm(*[entry.q for entry in values])
    integers = [int(entry * denominator) for entry in values]
    common = reduce(gcd, (abs(entry) for entry in integers if entry))
    integers = [entry // common for entry in integers]
    if next(entry for entry in integers if entry) < 0:
        integers = [-entry for entry in integers]
    return integers


def multiply_truncated(
    left: list[Fraction], right: list[Fraction], maximum: int
) -> list[Fraction]:
    answer = [Fraction(0)] * (maximum + 1)
    for j, x in enumerate(left):
        if j > maximum or not x:
            continue
        for k, y in enumerate(right):
            if j + k > maximum:
                break
            if y:
                answer[j + k] += x * y
    return answer


def independent_composite_jets(maximum: int) -> list[int]:
    """Compose ordinary Taylor series; do not divide the rational G'."""
    # F'(w)=sum u_m w^m and (2-2w+w^2)F'(w)=4.
    derivative_coefficients: list[Fraction] = []
    for m in range(maximum):
        rhs = Fraction(4 if m == 0 else 0)
        if m >= 1:
            rhs += 2 * derivative_coefficients[m - 1]
        if m >= 2:
            rhs -= derivative_coefficients[m - 2]
        derivative_coefficients.append(rhs / 2)
    f_coefficients = [Fraction(0)] + [
        derivative_coefficients[m] / (m + 1) for m in range(maximum)
    ]

    phi = [Fraction(0)] * (maximum + 1)
    phi[1] = Fraction(1)
    if maximum >= 7:
        phi[7] = Fraction(1, 140)
    if maximum >= 8:
        phi[8] = Fraction(-1, 140)

    answer = [Fraction(0)] * (maximum + 1)
    power = [Fraction(0)] * (maximum + 1)
    power[0] = Fraction(1)
    for k in range(1, maximum + 1):
        power = multiply_truncated(power, phi, maximum)
        if f_coefficients[k]:
            for j in range(maximum + 1):
                answer[j] += f_coefficients[k] * power[j]

    jets: list[int] = []
    for k, coefficient in enumerate(answer):
        jet = coefficient * math.factorial(k)
        assert jet.denominator == 1
        jets.append(jet.numerator)
    return jets


def gaussian_rational_pair(value: sp.Expr) -> tuple[Fraction, Fraction]:
    value = sp.expand_complex(sp.simplify(value))
    real = sp.Rational(sp.re(value))
    imag = sp.Rational(sp.im(value))
    return Fraction(int(real.p), int(real.q)), Fraction(int(imag.p), int(imag.q))


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def complex_record(value: sp.Expr) -> dict[str, dict[str, int]]:
    real, imag = gaussian_rational_pair(value)
    return {"real": fraction_record(real), "imag": fraction_record(imag)}


def independent_schur_records() -> tuple[list[dict], sp.Poly]:
    """Schur recursion using SymPy polynomials over QQ_I."""
    z, w = sp.symbols("z w")
    phi = z + (z**7 - z**8) / sp.Integer(140)
    q = phi - (1 + sp.I)
    radius = sp.Rational(3, 2)
    reciprocal = sp.Poly(sp.cancel(w**8 * q.subs(z, radius / w)), w)
    assert reciprocal.degree() == 8

    polynomial = reciprocal
    records: list[dict] = []
    while polynomial.degree() > 0:
        degree = polynomial.degree()
        monic_expression = sp.expand(polynomial.as_expr() / polynomial.LC())
        monic = sp.Poly(monic_expression, w)
        coefficients = monic.all_coeffs()
        constant = coefficients[-1]
        gap_expr = sp.simplify(1 - constant * sp.conjugate(constant))
        gap = sp.Rational(gap_expr)
        assert gap > 0
        star = sp.Add(*[
            sp.conjugate(coefficients[degree - j]) * w ** (degree - j)
            for j in range(degree + 1)
        ])
        # The expression above indexes the coefficient of w^j in P^* as
        # conjugate of the coefficient of w^(d-j).
        transformed_numerator = sp.Poly(
            sp.expand(monic.as_expr() - constant * star), w
        )
        assert transformed_numerator.TC() == 0
        transformed = sp.Poly(
            sp.cancel(transformed_numerator.as_expr() / w), w
        )
        assert transformed.degree() == degree - 1
        records.append(
            {
                "degree": degree,
                "normalized_constant": complex_record(constant),
                "one_minus_constant_modulus_squared": fraction_record(
                    Fraction(int(gap.p), int(gap.q))
                ),
            }
        )
        polynomial = transformed
    assert polynomial.TC() != 0
    return records, reciprocal


def independent_numeric_root_diagnostic() -> list[dict[str, str]]:
    """Numerically solve q=0 with mpmath, independently of SymPy nroots."""
    mp.mp.dps = 80
    coefficients = [
        -mp.mpf(1) / 140,
        mp.mpf(1) / 140,
        mp.mpf(0),
        mp.mpf(0),
        mp.mpf(0),
        mp.mpf(0),
        mp.mpf(0),
        mp.mpf(1),
        -(mp.mpc(1, 1)),
    ]
    roots = mp.polyroots(coefficients, maxsteps=2000, error=False)
    roots.sort(key=abs)
    return [
        {
            "real": mp.nstr(root.real, 60),
            "imag": mp.nstr(root.imag, 60),
            "modulus": mp.nstr(abs(root), 60),
            "absolute_residual": mp.nstr(
                abs(mp.polyval(coefficients, root)), 8
            ),
        }
        for root in roots
    ]


def e_interval(last: int = 200) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, math.factorial(k)) for k in range(last + 1)),
        Fraction(0),
    )
    # For last>=1, sum_{k>last}1/k! < 1/(last*last!).
    return partial, partial + Fraction(1, last * math.factorial(last))


def atan_interval(inv: int, last: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            (-1 if k & 1 else 1)
            * Fraction(1, (2 * k + 1) * inv ** (2 * k + 1))
            for k in range(last + 1)
        ),
        Fraction(0),
    )
    omitted = Fraction(1, (2 * last + 3) * inv ** (2 * last + 3))
    return (partial, partial + omitted) if last & 1 else (partial - omitted, partial)


def independent_e_plus_pi_interval() -> tuple[Fraction, Fraction]:
    e_lo, e_hi = e_interval(200)
    x_lo, x_hi = atan_interval(5, 200)
    y_lo, y_hi = atan_interval(239, 60)
    return e_lo + 16 * x_lo - 4 * y_hi, e_hi + 16 * x_hi - 4 * y_lo


def power10(k: int) -> Fraction:
    return Fraction(10**k) if k >= 0 else Fraction(1, 10 ** (-k))


def floor_log10_positive(value: Fraction) -> int:
    assert value > 0
    guess = len(str(value.numerator)) - len(str(value.denominator))
    while value < power10(guess):
        guess -= 1
    while value >= power10(guess + 1):
        guess += 1
    return guess


def interval_semantics(
    alpha: int, beta: int, interval: tuple[Fraction, Fraction]
) -> dict:
    lo, hi = sorted(
        (Fraction(alpha) + beta * interval[0], Fraction(alpha) + beta * interval[1])
    )
    if lo == hi == 0:
        return {"certified_sign": 0, "interval_contains_zero": True}
    if lo <= 0 <= hi:
        return {"certified_sign": None, "interval_contains_zero": True}
    if lo > 0:
        sign, abs_lo, abs_hi = 1, lo, hi
    else:
        sign, abs_lo, abs_hi = -1, -hi, -lo
    lower_decade = floor_log10_positive(abs_lo)
    upper_decade = floor_log10_positive(abs_hi)
    return {
        "certified_sign": sign,
        "interval_contains_zero": False,
        "floor_log10_abs_lower": lower_decade,
        "floor_log10_abs_upper": upper_decade,
        "single_certified_base10_decade": (
            lower_decade if lower_decade == upper_decade else None
        ),
    }


def full_coefficient_matrix(n: int, jets: list[int]) -> sp.Matrix:
    """Full A+B exp+C G coefficient equations plus B(1)=C(1)."""
    width = 3 * (n + 1)
    rows: list[list[sp.Rational]] = []
    for k in range(3 * n + 1):
        row = [sp.Rational(0)] * width
        if k <= n:
            row[k] = 1
        for j in range(min(k, n) + 1):
            row[n + 1 + j] = sp.Rational(1, math.factorial(k - j))
            row[2 * (n + 1) + j] = sp.Rational(
                jets[k - j], math.factorial(k - j)
            )
        rows.append(row)
    rows.append(
        [sp.Rational(0)] * (n + 1)
        + [sp.Rational(-1)] * (n + 1)
        + [sp.Rational(1)] * (n + 1)
    )
    return sp.Matrix(rows)


def falling(k: int, j: int) -> int:
    return math.factorial(k) // math.factorial(k - j) if j <= k else 0


def high_derivative_matrix(n: int, jets: list[int]) -> sp.Matrix:
    rows: list[list[int]] = []
    for k in range(n + 1, 3 * n + 1):
        rows.append(
            [falling(k, j) for j in range(n + 1)]
            + [falling(k, j) * jets[k - j] for j in range(n + 1)]
        )
    rows.append([-1] * (n + 1) + [1] * (n + 1))
    return sp.Matrix(rows)


def independent_hp_record(
    n: int, jets: list[int], s_interval: tuple[Fraction, Fraction]
) -> dict:
    full = full_coefficient_matrix(n, jets)
    full_dm = DomainMatrix.from_Matrix(full).to_field()
    full_rank = full_dm.rank()
    full_nullspace = full_dm.nullspace()
    assert full_nullspace.shape[0] == 1
    triple = primitive(list(full_nullspace.to_Matrix().row(0)))

    high = high_derivative_matrix(n, jets)
    high_rank = DomainMatrix.from_Matrix(high).to_field().rank()
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    bc = primitive([sp.Rational(entry) for entry in b + c])

    # A cofactor vector of a full-row-rank (m x (m+1)) integer matrix is
    # content times its primitive integer kernel.  Compute the content using
    # a nonzero coordinate selected independently from the source program.
    nonzero_indices = [j for j, coordinate in enumerate(bc) if coordinate]
    chosen = nonzero_indices[-1]
    minor = high[:, :chosen].row_join(high[:, chosen + 1 :])
    determinant = int(DomainMatrix.from_Matrix(minor).det())
    signed_cofactor = determinant if chosen % 2 == 0 else -determinant
    assert signed_cofactor % bc[chosen] == 0
    content = abs(signed_cofactor // bc[chosen])
    # A second coordinate checks that this is the common cofactor factor.
    alternate = nonzero_indices[0]
    minor2 = high[:, :alternate].row_join(high[:, alternate + 1 :])
    determinant2 = int(DomainMatrix.from_Matrix(minor2).det())
    signed2 = determinant2 if alternate % 2 == 0 else -determinant2
    assert signed2 == (signed_cofactor // bc[chosen]) * bc[alternate]

    endpoint_a = sum(triple[: n + 1])
    endpoint_b = sum(b)
    endpoint_gcd = gcd(abs(endpoint_a), abs(endpoint_b))
    if endpoint_gcd:
        reduced = [endpoint_a // endpoint_gcd, endpoint_b // endpoint_gcd]
    else:
        reduced = [0, 0]

    k = 3 * n + 1
    first_free = Fraction(0)
    for j in range(n + 1):
        first_free += Fraction(b[j], math.factorial(k - j))
        first_free += Fraction(c[j] * jets[k - j], math.factorial(k - j))

    return {
        "n": n,
        "source_high_shape": list(high.shape),
        "source_high_rank": high_rank,
        "source_high_nullity": high.cols - high_rank,
        "independent_full_shape": list(full.shape),
        "independent_full_rank": full_rank,
        "independent_full_nullity": full.cols - full_rank,
        "primitive_high_kernel_sha256": sha256_json_vector(bc),
        "maximal_cofactor_common_content_digits": len(str(content)),
        "primitive_triple_height_digits": len(str(max(map(abs, triple)))),
        "primitive_triple_sha256": sha256_json_vector(triple),
        "raw_endpoint_pair": [endpoint_a, endpoint_b],
        "endpoint_gcd": endpoint_gcd,
        "reduced_endpoint_pair": reduced,
        "independent_endpoint_interval_semantics": interval_semantics(
            reduced[0], reduced[1], s_interval
        ),
        "first_free": {
            "index": k,
            "numerator": first_free.numerator,
            "denominator": first_free.denominator,
            "nonzero": bool(first_free),
        },
    }


def compare_with_archived(
    root: Path,
    schur_records: list[dict],
    jets_120: list[int],
    jets_46: list[int],
    hp_records: list[dict],
    numeric_roots: list[dict[str, str]],
) -> dict:
    certificate = json.loads(
        (root / "results/high_radius_composed_pullback_certificate.json").read_text()
    )
    hp = json.loads(
        (root / "results/high_radius_composed_pullback_hp_n15.json").read_text()
    )
    schur_agrees = schur_records == certificate["normalized_schur_cohn_records"]
    cert_jets_agree = (
        sha256_json_vector(jets_120)
        == certificate["computed_composite_jets_sha256"]
    )
    hp_jets_agree = sha256_json_vector(jets_46) == hp["computed_G_jet_sha256"]
    mp.mp.dps = 70
    archived_roots = certificate[
        "roots_of_phi_equals_1_plus_i_high_precision_diagnostic"
    ]
    numeric_roots_agree = len(numeric_roots) == len(archived_roots) and all(
        abs(mp.mpf(independent["real"]) - mp.mpf(archived["real"])) < mp.mpf("1e-50")
        and abs(mp.mpf(independent["imag"]) - mp.mpf(archived["imag"]))
        < mp.mpf("1e-50")
        and abs(mp.mpf(independent["modulus"]) - mp.mpf(archived["modulus"]))
        < mp.mpf("1e-50")
        for independent, archived in zip(numeric_roots, archived_roots)
    )

    field_agreement: list[dict] = []
    for independent, archived in zip(hp_records, hp["records"], strict=True):
        checks = {
            "shape": independent["source_high_shape"] == archived["shape"],
            "rank": independent["source_high_rank"] == archived["rank"],
            "nullity": independent["source_high_nullity"] == archived["nullity"],
            "primitive_high_kernel_sha256": (
                independent["primitive_high_kernel_sha256"]
                == archived["primitive_high_kernel_sha256"]
            ),
            "maximal_cofactor_common_content_digits": (
                independent["maximal_cofactor_common_content_digits"]
                == archived["maximal_cofactor_common_content_digits"]
            ),
            "primitive_triple_height_digits": (
                independent["primitive_triple_height_digits"]
                == archived["primitive_triple_height_digits"]
            ),
            "primitive_triple_sha256": (
                independent["primitive_triple_sha256"]
                == archived["primitive_triple_sha256"]
            ),
            "raw_endpoint_pair": (
                independent["raw_endpoint_pair"] == archived["raw_endpoint_pair"]
            ),
            "endpoint_gcd": independent["endpoint_gcd"] == archived["endpoint_gcd"],
            "reduced_endpoint_pair": (
                independent["reduced_endpoint_pair"]
                == archived["reduced_endpoint_pair"]
            ),
            "endpoint_sign_and_decade": all(
                independent["independent_endpoint_interval_semantics"].get(key)
                == archived["endpoint_interval_certificate"].get(key)
                for key in (
                    "certified_sign",
                    "interval_contains_zero",
                    "floor_log10_abs_lower",
                    "floor_log10_abs_upper",
                    "single_certified_base10_decade",
                )
                if key in independent["independent_endpoint_interval_semantics"]
                or key in archived["endpoint_interval_certificate"]
            ),
            "first_free": independent["first_free"] == archived["first_free"],
        }
        field_agreement.append(
            {
                "n": independent["n"],
                "checks": checks,
                "all_checked_fields_agree": all(checks.values()),
            }
        )
    return {
        "schur_records_exactly_agree": schur_agrees,
        "120_composite_jets_hash_agrees": cert_jets_agree,
        "46_composite_jets_hash_agrees": hp_jets_agree,
        "mpmath_numeric_roots_agree_to_50_decimal_places": numeric_roots_agree,
        "hp_record_field_agreement": field_agreement,
        "all_hp_checked_fields_agree": all(
            record["all_checked_fields_agree"] for record in field_agreement
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()

    observed_hashes_at_start = {
        relative: sha256_bytes((root / relative).read_bytes())
        for relative in FROZEN_HASHES
    }
    assert observed_hashes_at_start == FROZEN_HASHES, (
        observed_hashes_at_start,
        FROZEN_HASHES,
    )

    schur_records, reciprocal = independent_schur_records()
    numeric_roots = independent_numeric_root_diagnostic()
    jets_120 = independent_composite_jets(120)
    jets_46 = jets_120[:47]
    s_interval = independent_e_plus_pi_interval()
    hp_records = [
        independent_hp_record(n, jets_46, s_interval) for n in range(1, 16)
    ]
    comparison = compare_with_archived(
        root, schur_records, jets_120, jets_46, hp_records, numeric_roots
    )
    all_gaps_positive = all(
        item["one_minus_constant_modulus_squared"]["numerator"] > 0
        and item["one_minus_constant_modulus_squared"]["denominator"] > 0
        for item in schur_records
    )
    assert all_gaps_positive
    assert all(comparison[key] for key in (
        "schur_records_exactly_agree",
        "120_composite_jets_hash_agrees",
        "46_composite_jets_hash_agrees",
        "mpmath_numeric_roots_agree_to_50_decimal_places",
        "all_hp_checked_fields_agree",
    ))

    observed_hashes_at_end = {
        relative: sha256_bytes((root / relative).read_bytes())
        for relative in FROZEN_HASHES
    }
    frozen_unchanged = (
        observed_hashes_at_start == observed_hashes_at_end == FROZEN_HASHES
    )
    assert frozen_unchanged, (
        observed_hashes_at_start,
        observed_hashes_at_end,
        FROZEN_HASHES,
    )

    z = sp.symbols("z")
    phi = z + (z**7 - z**8) / sp.Integer(140)
    result = {
        "verdict": "accept",
        "frozen_hashes": FROZEN_HASHES,
        "observed_hashes_at_start": observed_hashes_at_start,
        "observed_hashes_at_end": observed_hashes_at_end,
        "frozen_files_unchanged": frozen_unchanged,
        "endpoint_checks": {
            "phi_at_zero": str(phi.subs(z, 0)),
            "phi_at_one": str(phi.subs(z, 1)),
            "phi_derivative_jets_1_through_8": [
                int(sp.diff(phi, z, k).subs(z, 0)) for k in range(1, 9)
            ],
        },
        "reciprocal_polynomial": str(reciprocal.as_expr()),
        "independent_schur_records": schur_records,
        "all_eight_schur_gaps_strictly_positive": all_gaps_positive,
        "independent_mpmath_root_diagnostic": numeric_roots,
        "independent_120_composite_jets_sha256": sha256_json_vector(jets_120),
        "independent_46_composite_jets_sha256": sha256_json_vector(jets_46),
        "hp_records": hp_records,
        "comparison_with_archived": comparison,
        "limitations": (
            "The finite HP records are diagnostic only. The accepted theorem "
            "is endpoint identity, all-order integral jets, genuine logarithmic "
            "singularities at all preimages, and the strict radius bound >3/2."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
