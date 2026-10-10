#!/usr/bin/env python3
"""Deterministic exact certificate for Item 216.

The checker imports the frozen Item 214 recurrence from the same directory.
All symbolic polynomial work below uses only Python's standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import item214_stable_eliminant_gcd_certificate as joint  # noqa: E402


DEFAULT_OUTPUT = (
    HERE / "item216_gosper_phase_obstruction_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item216_gosper_phase_obstruction_certificate.json"
)

# A polynomial in (b,h) is a sparse map (degree_b,degree_h) -> coefficient.
Poly = dict[tuple[int, int], Fraction]


def clean(poly: Poly) -> Poly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def poly_add(left: Poly, right: Poly) -> Poly:
    answer = dict(left)
    for monomial, coefficient in right.items():
        answer[monomial] = answer.get(monomial, Fraction(0)) + coefficient
    return clean(answer)


def poly_scale(poly: Poly, scalar: Fraction | int) -> Poly:
    scalar = Fraction(scalar)
    return clean({monomial: scalar * coefficient for monomial, coefficient in poly.items()})


def poly_mul(left: Poly, right: Poly) -> Poly:
    answer: Poly = {}
    for (left_b, left_h), left_coefficient in left.items():
        for (right_b, right_h), right_coefficient in right.items():
            monomial = (left_b + right_b, left_h + right_h)
            answer[monomial] = answer.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
    return clean(answer)


def linear(b_coefficient: int, h_coefficient: int, constant: int) -> Poly:
    return clean(
        {
            (1, 0): Fraction(b_coefficient),
            (0, 1): Fraction(h_coefficient),
            (0, 0): Fraction(constant),
        }
    )


def poly_shift_h(poly: Poly, shift: int) -> Poly:
    """Return poly(b,h+shift), exactly."""
    answer: Poly = {}
    for (b_degree, h_degree), coefficient in poly.items():
        for new_h_degree in range(h_degree + 1):
            term = (
                coefficient
                * math.comb(h_degree, new_h_degree)
                * Fraction(shift) ** (h_degree - new_h_degree)
            )
            monomial = (b_degree, new_h_degree)
            answer[monomial] = answer.get(monomial, Fraction(0)) + term
    return clean(answer)


def coefficient_in_h(poly: Poly, degree: int) -> dict[int, Fraction]:
    return clean_one({b_degree: coefficient for (b_degree, h_degree), coefficient in poly.items() if h_degree == degree})


def clean_one(poly: dict[int, Fraction]) -> dict[int, Fraction]:
    return {degree: coefficient for degree, coefficient in poly.items() if coefficient}


def poly_eval(poly: Poly, b_value: int, h_value: int) -> Fraction:
    answer = Fraction(0)
    for (b_degree, h_degree), coefficient in poly.items():
        answer += coefficient * b_value**b_degree * h_value**h_degree
    return answer


def polynomial_sha256(poly: Poly) -> str:
    rows = [
        (b_degree, h_degree, coefficient.numerator, coefficient.denominator)
        for (b_degree, h_degree), coefficient in sorted(poly.items())
    ]
    return hashlib.sha256((repr(rows) + "\n").encode("ascii")).hexdigest()


def reduced_ratio_polynomials(residue: int) -> tuple[Poly, Poly]:
    """Return the monic A_r,B_r with F_(h+1)/F_h=A_r(h)/B_r(h)."""
    if residue not in range(4):
        raise ValueError(residue)
    numerator: Poly = {(0, 0): Fraction(1)}
    for offset in (residue - 1, residue, residue + 1):
        numerator = poly_mul(numerator, linear(1, -4, -offset))
    numerator = poly_mul(numerator, linear(3, 20, 2 + 5 * residue))
    numerator = poly_scale(numerator, Fraction(-1, 1280))

    floor_half = residue // 2
    ceil_half = (residue + 1) // 2
    denominator: Poly = {(0, 0): Fraction(1)}
    denominator = poly_mul(denominator, linear(0, 1, 1))
    denominator = poly_mul(denominator, linear(0, 2, 1 + 2 * floor_half))
    denominator = poly_mul(denominator, linear(0, 4, 1 + 2 * ceil_half))
    denominator = poly_mul(denominator, linear(0, 4, 3 + 2 * ceil_half))
    denominator = poly_scale(denominator, Fraction(1, 32))
    return numerator, denominator


def raw_ratio_polynomials(residue: int) -> tuple[Poly, Poly]:
    """Uncancelled exact ratio for the unique common residual summand."""
    numerator: Poly = {(0, 0): Fraction(1)}
    denominator: Poly = {(0, 0): Fraction(5)}
    for offset in range(4):
        numerator = poly_mul(numerator, linear(1, -4, -residue - offset))
        denominator = poly_mul(denominator, linear(0, 4, residue + offset + 1))
    numerator = poly_mul(numerator, linear(3, 20, 2 + 5 * residue))
    numerator = poly_mul(numerator, linear(-1, 4, residue - 1))
    denominator = poly_mul(denominator, linear(-1, 4, residue + 2))
    denominator = poly_mul(denominator, linear(-1, 4, residue + 3))
    return numerator, denominator


def residual_fraction(b_value: int, residue: int) -> Fraction:
    phi_g1, phi_g0 = joint.common_term_phase_sums(b_value, residue)
    return (residue - b_value - 2) * phi_g1 + (b_value + 1) * phi_g0


def common_residual_terms(b_value: int, residue: int) -> tuple[list[Fraction], Fraction]:
    """Return common F_h terms and the explicit g1 endpoint contribution."""
    if b_value < residue:
        raise ValueError("the common-support formula requires r<=b")
    alpha = Fraction(3 * b_value + 2 + 5 * residue, 20)
    delta = Fraction(residue - b_value - 2, 4)
    cutoff = (b_value - residue) // 4
    term = Fraction(math.comb(b_value, residue))
    values = []
    for h_value in range(cutoff + 1):
        z_value = delta + h_value
        values.append(term * Fraction((b_value + 1) * delta, 1) / (z_value * (4 * z_value + 1)))
        if h_value == cutoff:
            break
        ratio = Fraction(1)
        degree = residue + 4 * h_value
        for offset in range(4):
            ratio *= Fraction(b_value - degree - offset, degree + offset + 1)
        ratio *= (alpha + h_value) / (delta + h_value)
        term *= ratio

    endpoint = Fraction(0)
    if (b_value + 1 - residue) % 4 == 0:
        endpoint_index = (b_value + 1 - residue) // 4
        endpoint = Fraction(residue - b_value - 2) * joint.rising(alpha, endpoint_index) / joint.rising(
            delta, endpoint_index
        )
    return values, endpoint


def certificate(crosscheck_max_b: int) -> dict[str, Any]:
    if crosscheck_max_b < 100:
        raise ValueError("the canonical cross-check range must be at least 100")

    symbolic_rows = []
    ratio_crosscheck_hash = hashlib.sha256()
    ratio_crosschecks = 0
    for residue in range(4):
        reduced_numerator, reduced_denominator = reduced_ratio_polynomials(residue)
        raw_numerator, raw_denominator = raw_ratio_polynomials(residue)
        if poly_add(
            poly_mul(raw_numerator, reduced_denominator),
            poly_scale(poly_mul(raw_denominator, reduced_numerator), -1),
        ):
            raise AssertionError((residue, "raw/reduced ratio identity failed"))
        if coefficient_in_h(reduced_numerator, 4) != {0: Fraction(1)}:
            raise AssertionError((residue, "A is not monic quartic"))
        if coefficient_in_h(reduced_denominator, 4) != {0: Fraction(1)}:
            raise AssertionError((residue, "B is not monic quartic"))

        shifted_denominator = poly_shift_h(reduced_denominator, -1)
        degree_obstruction = clean_one(
            {
                degree: coefficient_in_h(shifted_denominator, 3).get(degree, Fraction(0))
                - coefficient_in_h(reduced_numerator, 3).get(degree, Fraction(0))
                for degree in set(coefficient_in_h(shifted_denominator, 3))
                | set(coefficient_in_h(reduced_numerator, 3))
            }
        )
        if degree_obstruction != {1: Fraction(3, 5), 0: Fraction(-8, 5)}:
            raise AssertionError((residue, degree_obstruction))

        # Exact values test the reduced ratio directly against consecutive F_h.
        for b_value in range(5, crosscheck_max_b + 1):
            if b_value < residue:
                continue
            terms, endpoint = common_residual_terms(b_value, residue)
            if sum(terms, Fraction(0)) + endpoint != residual_fraction(b_value, residue):
                raise AssertionError((b_value, residue, "contiguous decomposition"))
            for h_value in range(len(terms) - 1):
                if not terms[h_value]:
                    continue
                left = terms[h_value + 1] / terms[h_value]
                right = poly_eval(reduced_numerator, b_value, h_value) / poly_eval(
                    reduced_denominator, b_value, h_value
                )
                if left != right:
                    raise AssertionError((b_value, residue, h_value, left, right))
                ratio_crosschecks += 1
                ratio_crosscheck_hash.update(
                    (repr((b_value, residue, h_value, left.numerator, left.denominator)) + "\n").encode(
                        "ascii"
                    )
                )

        symbolic_rows.append(
            {
                "r": residue,
                "A_sha256": polynomial_sha256(reduced_numerator),
                "B_sha256": polynomial_sha256(reduced_denominator),
                "A_h3": {
                    str(degree): str(coefficient)
                    for degree, coefficient in sorted(coefficient_in_h(reduced_numerator, 3).items())
                },
                "B_shift_minus_1_h3": {
                    str(degree): str(coefficient)
                    for degree, coefficient in sorted(coefficient_in_h(shifted_denominator, 3).items())
                },
                "forced_polynomial_degree": "(3*b-8)/5",
            }
        )

    # Phase arithmetic: b=1 mod 5 would force p=5, so it cannot occur for p>5.
    phase_hash = hashlib.sha256()
    phase_checks = 0
    phase_ceiling = 4 * crosscheck_max_b + 100
    prime_flags = joint.phase.sieve(phase_ceiling + 1)
    phase_primes = [prime for prime in range(7, phase_ceiling + 1) if prime_flags[prime]]
    for b_value in range(5, crosscheck_max_b + 1):
        for residue in range(4):
            for q_value in (1, 2):
                for prime in phase_primes:
                    nodes = joint.phase_feasible_nodes(b_value, residue, prime)
                    if any(q == q_value for q, _ in nodes):
                        if b_value % 5 == 1:
                            raise AssertionError((b_value, residue, prime, q_value))
                        phase_checks += 1
                        phase_hash.update(
                            (repr((b_value, residue, prime, q_value)) + "\n").encode("ascii")
                        )

    # Directly dispose of b<5.  Zero gcds are support gaps, not factors.
    small_rows = []
    for b_value in range(5):
        for residue in range(4):
            common, _, _ = joint.stable_gcd(b_value, residue)
            feasible_odd_primes = []
            if common:
                for prime in range(7, abs(common) + 1):
                    if common % prime == 0 and joint.phase.sieve(prime + 1)[prime]:
                        if joint.phase_feasible_nodes(b_value, residue, prime):
                            feasible_odd_primes.append(prime)
            small_rows.append(
                {
                    "b": b_value,
                    "r": residue,
                    "gcd": common,
                    "support_gap": common == 0,
                    "phase_feasible_odd_primes_gt_5": feasible_odd_primes,
                }
            )
    if any(row["phase_feasible_odd_primes_gt_5"] for row in small_rows):
        raise AssertionError(small_rows)
    actual_small_support_gaps = []
    for row in small_rows:
        if not row["support_gap"]:
            continue
        b_value = row["b"]
        residue = row["r"]
        right = (b_value + 4 + 5 * joint.phase_sigma(residue)) % 20
        # q=1 requires an odd prime residue; q=2 requires twice an odd residue.
        q1_possible = right % 2 == 1 and math.gcd(right, 20) == 1
        q2_possible = right % 2 == 0 and any((2 * odd - right) % 20 == 0 for odd in (1, 3, 7, 9, 11, 13, 17, 19))
        if q1_possible or q2_possible:
            actual_small_support_gaps.append([b_value, residue])
    if actual_small_support_gaps != [[0, 3]]:
        raise AssertionError(actual_small_support_gaps)

    # Mandatory exact exception.  The unique combination retains the entire
    # eliminant gcd in its reduced numerator, including 2399.
    mandatory_b = 900
    mandatory_r = 3
    mandatory_residual = residual_fraction(mandatory_b, mandatory_r)
    mandatory_gcd, _, _ = joint.stable_gcd(mandatory_b, mandatory_r)
    if mandatory_residual.numerator % mandatory_gcd:
        raise AssertionError("mandatory gcd does not divide the residual numerator")
    if math.gcd(mandatory_residual.denominator, mandatory_gcd) != 1:
        raise AssertionError("mandatory denominator is not coprime to the gcd")
    if mandatory_residual.numerator % 2399 or mandatory_residual.denominator % 2399 != 954:
        raise AssertionError("the p=2399 exception was not retained")
    quotient = mandatory_residual.numerator // mandatory_gcd

    return {
        "item": 216,
        "arithmetic": "exact rational and sparse bivariate-polynomial arithmetic; Python standard library only",
        "proved_unique_contiguous_reduction": {
            "parameters": "z=delta+h; delta=(r-b-2)/4",
            "common_weights": {
                "Phi_g1": "-(b+1)/(4*z+1)",
                "Phi_g0": "delta/z",
            },
            "unique_pair_up_to_scale": "lambda=r-b-2, mu=b+1",
            "combination": "R_(b,r)=(r-b-2)*Phi_g1+(b+1)*Phi_g0",
            "common_summand": "F_h=T_h*(b+1)*delta/(z*(4*z+1))",
            "endpoint": "add (r-b-2)*(alpha)_e/(delta)_e when e=(b+1-r)/4 is a nonnegative integer",
            "scope": "exact for r<=b; finite support gaps are treated separately",
        },
        "proved_reduced_ratio": {
            "identity": "F_(h+1)/F_h=A_r(h)/B_r(h)",
            "A": "-product_{u=r-1}^{r+1}(b-4h-u)*(3b+20h+2+5r)/1280",
            "B": "(h+1)*(2h+1+2floor(r/2))*(4h+1+2ceil(r/2))*(4h+3+2ceil(r/2))/32",
            "symbolic_rows": symbolic_rows,
            "finite_crosscheck": {
                "label": "FINITE verification of the separately proved polynomial identities and recurrence",
                "max_b": crosscheck_max_b,
                "consecutive_ratios": ratio_crosschecks,
                "stream_sha256": ratio_crosscheck_hash.hexdigest(),
            },
        },
        "proved_gosper_obstruction": {
            "normality_over_Qb": (
                "the three roots (b-u)/4 and the root -(3b+2+5r)/20 of A cannot equal "
                "a root of B(h+j) identically in b, for any integer j>=0"
            ),
            "specialized_normality": (
                "for b>=5 the first three A-roots are positive while every B(h+j)-root is negative; "
                "a collision of the fourth root requires b=1 (mod 5)"
            ),
            "polynomial_equation": "A(h)*x(h+1)-B(h-1)*x(h)=1",
            "forced_degree": "deg(x)=[h^3]B(h-1)-[h^3]A(h)=(3b-8)/5",
            "phase_exclusion": "b=1 (mod 5) and q*p=b+4 (mod 5) force p=5",
            "theorem": (
                "for every actual p>5 stable phase with b>=5, F_h has no hypergeometric "
                "antidifference certified by Gosper's normal form"
            ),
            "finite_phase_crosscheck": {
                "label": "FINITE check of the separately proved phase exclusion",
                "max_b": crosscheck_max_b,
                "nodes": phase_checks,
                "stream_sha256": phase_hash.hexdigest(),
            },
            "small_b_exact_rows": small_rows,
            "only_phase-compatible_small_support_gap": [0, 3],
        },
        "mandatory_b900_exception": {
            "node": {"s": 299, "p": 2399, "q": 1, "b": 900, "r": 3, "k": 899},
            "forced_degree": "2692/5",
            "residual_numerator_digits": len(str(abs(mandatory_residual.numerator))),
            "residual_denominator_digits": len(str(mandatory_residual.denominator)),
            "residual_numerator_sha256": hashlib.sha256(
                str(mandatory_residual.numerator).encode("ascii")
            ).hexdigest(),
            "residual_denominator_sha256": hashlib.sha256(
                str(mandatory_residual.denominator).encode("ascii")
            ).hexdigest(),
            "residual_fraction_sha256": hashlib.sha256(str(mandatory_residual).encode("ascii")).hexdigest(),
            "numerator_mod_2399": mandatory_residual.numerator % 2399,
            "denominator_mod_2399": mandatory_residual.denominator % 2399,
            "entire_G_900_3_divides_reduced_numerator": True,
            "gcd_with_denominator": math.gcd(mandatory_residual.denominator, mandatory_gcd),
            "quotient_digits": len(str(abs(quotient))),
            "quotient_sha256": hashlib.sha256(str(quotient).encode("ascii")).hexdigest(),
        },
        "route_1_rate_ledger": {
            "new_usable_rate_credit_per_m": 0,
            "actual_common_prime_log_mass_bound": "OPEN; neither an upper nor a lower asymptotic coefficient is proved",
            "needed_coefficient_per_m": "0.1177979020165907632818384072...",
            "full_kappa_1_cell_coefficient_per_m": "0.4820375017701112",
            "consequence": (
                "this is a method obstruction only; it neither bounds nor supplies stable/far moving-b prime mass"
            ),
        },
        "labels": {
            "PROVED": [
                "unique h-independent first contiguous combination",
                "reduced quartic term ratio",
                "Gosper no-antidifference theorem on every actual p>5 stable phase with b>=5",
                "phase exclusion of the only possible collision class",
                "mandatory p=2399 survives in the residual numerator",
            ],
            "FINITE": [
                "recurrence and phase crosschecks through the declared max_b",
                "direct b<5 eliminant-gcd rows",
            ],
            "OPEN": [
                "higher-order creative telescoping in b",
                "closed forced-product extraction from G_(b,r)",
                "resultant or prime-localization bounds",
                "any positive or negative asymptotic stable/far-phase log-mass bound",
            ],
        },
        "verdict": (
            "PROVED that the unique first contiguous residual is non-Gosper-summable on every actual "
            "non-gap p>5 stable phase; the b=900,p=2399 cancellation survives. This rules out the "
            "most direct first-order gamma/Pochhammer telescoping route but gives coefficient 0, so "
            "higher-order identities and all-b prime localization remain OPEN."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--crosscheck-max-b", type=int, default=120)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate(args.crosscheck_max_b)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "ratio_stream_sha256": result["proved_reduced_ratio"]["finite_crosscheck"]["stream_sha256"],
                "verdict": result["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
