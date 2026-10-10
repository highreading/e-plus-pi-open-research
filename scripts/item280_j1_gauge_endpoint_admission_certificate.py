#!/usr/bin/env python3
"""Deterministic certificate for Item 280's j=1 gauge/endpoint admission.

The all-parameter theorem is a formal composition of the pinned Items 222,
229, 231, 236, and 243.  The checker verifies the dependency hashes, the
division-free endpoint elimination identity, and a bounded exact replay.
Finite gcd patterns are kept explicitly separate from the theorem.
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
DEPENDENCIES = {
    "item222_j1_phase_resultant_certificate.py": "c16f75156ba8424c567163cedc6a93a7656c8a53036b48ef69b06327d76ad44b",
    "item229_j1_fixed_h_theta_certificate.py": "a8e2028ca6a53f8c843c25be375feac50e4704538686ee1e3a835f89aa11780f",
    "item231_j1_second_phase_coefficient_certificate.py": "b2ab5da4624a6b91d10a52976c6996b2e04b077f0b12c02a581a1551f6879045",
    "item236_j1_phase_cokernel_certificate.py": "a1aaa2dc857420b555b52a9d96282a37b193834069815194f3ccc0531b7aed96",
    "item243_order6_gauge_closure_certificate.py": "d619e0809aaa89b5d11cbe30a92a3e7f8cf14237f45dd066aedf84e017bbfdd8",
    "item243_order6_gauge_closure_certificate.json": "0ec0052ea270a84828cb1934373ad05e8e5b00cbf72e0d970ff805e716078546",
}
FINITE_H_MAX = 40


def resolve(name: str) -> Path:
    candidates = (
        HERE / name,
        HERE.parent / "scripts" / name,
        HERE.parent / "results" / name,
    )
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


for dependency_name, expected_hash in DEPENDENCIES.items():
    dependency_path = resolve(dependency_name)
    if sha256(dependency_path) != expected_hash:
        raise RuntimeError(f"dependency hash mismatch: {dependency_name}")


item222 = load("item280_item222", resolve("item222_j1_phase_resultant_certificate.py"))
item229 = load("item280_item229", resolve("item229_j1_fixed_h_theta_certificate.py"))
item231 = load("item280_item231", resolve("item231_j1_second_phase_coefficient_certificate.py"))


# Sparse commutative polynomials used only for the formal elimination audit.
VARIABLES = ("c", "S", "t", "L", "d", "T", "U", "F", "eta")
Monomial = tuple[int, ...]
Polynomial = dict[Monomial, int]


def constant(value: int) -> Polynomial:
    return {(0,) * len(VARIABLES): value} if value else {}


def variable(name: str) -> Polynomial:
    exponent = [0] * len(VARIABLES)
    exponent[VARIABLES.index(name)] = 1
    return {tuple(exponent): 1}


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def negate(value: Polynomial) -> Polynomial:
    return {monomial: -coefficient for monomial, coefficient in value.items()}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            result[monomial] = result.get(monomial, 0) + left_coefficient * right_coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def scale(value: Polynomial, scalar: int) -> Polynomial:
    return {monomial: scalar * coefficient for monomial, coefficient in value.items() if scalar * coefficient}


def formal_elimination_check() -> dict[str, Any]:
    c, s_sum, t_lower, low, delta, t_sum, upper, fixed, eta = (
        variable(name) for name in VARIABLES
    )
    theta = add(add(multiply(c, s_sum), multiply(t_lower, low)), scale(delta, -2))
    second = add(
        add(add(multiply(c, t_sum), multiply(multiply(eta, t_lower), upper)), negate(fixed)),
        scale(delta, 3),
    )
    endpoint = add(scale(multiply(multiply(delta, eta), upper), 2), negate(multiply(low, add(fixed, scale(delta, -3)))))
    incomplete_coefficient = add(multiply(multiply(eta, upper), s_sum), negate(multiply(low, t_sum)))
    left = add(multiply(multiply(eta, upper), theta), negate(multiply(low, second)))
    right = add(multiply(c, incomplete_coefficient), negate(endpoint))
    assert left == right
    return {
        "identity": "eta*U*Theta-L*Second=c*(eta*U*S-L*T)-K",
        "Theta": "c*S+t*L-2*d",
        "Second": "c*T+eta*t*U-F+3*d",
        "K": "2*d*eta*U-L*(F-3*d)",
        "monomial_terms_after_expansion": len(left),
        "division_by_L_U_d_or_t": False,
        "consequence": "Theta=Second=c=0 implies K=0 in every commutative coefficient ring",
        "label": "PROVED FORMAL IDENTITY",
    }


def gauge_ratio(h_value: int) -> Fraction:
    if h_value < 1 or h_value % 3 == 0:
        raise ValueError(h_value)
    residue = h_value % 3
    current = residue
    result = Fraction(-49, 18) if residue == 1 else Fraction(4235, 1944)
    while current < h_value:
        result *= Fraction(
            current
            * (4 * current + 1)
            * (4 * current + 5)
            * (4 * current + 7)
            * (4 * current + 9)
            * (4 * current + 11)
            * (4 * current + 15) ** 2,
            864
            * (current + 1)
            * (current + 2)
            * (2 * current + 1) ** 2
            * (2 * current + 3)
            * (2 * current + 5) ** 2
            * (4 * current + 3),
        )
        current += 3
    return result


def prime_factors(value: int) -> list[int]:
    value = abs(value)
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append(value)
    return factors


def maximum_prime_factor(value: int) -> int:
    factors = prime_factors(value)
    return max(factors) if factors else 1


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def finite_replay() -> dict[str, Any]:
    rows: list[list[Any]] = []
    admissible = 0
    max_e_denominator_prime = 1
    max_k_denominator_prime = 1
    max_gauge_denominator_prime = 1
    max_e_quotient_prime = 1
    max_k_over_c_denominator_prime = 1
    for h_value in range(1, FINITE_H_MAX + 1):
        if h_value % 3 == 0:
            continue
        admissible += 1
        eliminant, _ = item222.phase_fraction_and_integer(h_value)
        phase = item231.phase_boundary_data(h_value)
        common_residual = item229.phase_c(h_value)
        ratio = gauge_ratio(h_value)
        natural = phase["natural_eliminant"]
        assert phase["low_c"] == phase["high_c"] == common_residual
        assert common_residual == ratio * eliminant

        p_min = 4 * h_value + 9
        e_denominator_prime = maximum_prime_factor(eliminant.denominator)
        k_denominator_prime = maximum_prime_factor(natural.denominator)
        gauge_denominator_prime = maximum_prime_factor(ratio.denominator)
        assert e_denominator_prime < p_min
        assert k_denominator_prime < p_min
        assert gauge_denominator_prime < p_min

        common_numerator = math.gcd(abs(eliminant.numerator), abs(natural.numerator))
        e_quotient = abs(eliminant.numerator) // common_numerator
        e_quotient_prime = maximum_prime_factor(e_quotient)
        k_over_c_denominator_prime = maximum_prime_factor((natural / common_residual).denominator)
        assert e_quotient_prime <= 4 * h_value + 3
        assert k_over_c_denominator_prime < p_min

        max_e_denominator_prime = max(max_e_denominator_prime, e_denominator_prime)
        max_k_denominator_prime = max(max_k_denominator_prime, k_denominator_prime)
        max_gauge_denominator_prime = max(max_gauge_denominator_prime, gauge_denominator_prime)
        max_e_quotient_prime = max(max_e_quotient_prime, e_quotient_prime)
        max_k_over_c_denominator_prime = max(
            max_k_over_c_denominator_prime, k_over_c_denominator_prime
        )
        rows.append(
            [
                h_value,
                fraction_text(eliminant),
                fraction_text(natural),
                fraction_text(common_residual),
                fraction_text(ratio),
                e_quotient,
                e_quotient_prime,
                k_over_c_denominator_prime,
            ]
        )
    stream = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return {
        "classification": "EXACT FINITE ONLY; NOT USED TO INFER THE ALL-h GCD PATTERN",
        "h_max": FINITE_H_MAX,
        "admissible_h_count": admissible,
        "exact_low_high_and_gauge_equalities": 2 * admissible,
        "max_denominator_prime_in_replay": {
            "E": max_e_denominator_prime,
            "K": max_k_denominator_prime,
            "gauge_ratio": max_gauge_denominator_prime,
        },
        "finite_patterns_only": {
            "largest_prime_in_E_numerator_after_gcd_with_K": max_e_quotient_prime,
            "largest_prime_in_reduced_denominator_of_K_over_c": max_k_over_c_denominator_prime,
            "pointwise_bounds_checked": "prime(E_num/gcd)<=4h+3 and prime(den(K/c))<4h+9",
        },
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item280-j1-gauge-endpoint-admission-v1",
        "dependencies": DEPENDENCIES,
        "strict_labels": {
            "all_actual_collision_to_simultaneous_E_K_divisibility": "PROVED",
            "division_free_endpoint_elimination": "PROVED",
            "all_actual_denominators_are_units": "PROVED",
            "K_adds_arithmetic_codimension": "OPEN; NOT PROVED",
            "K_is_redundant_after_E": "OPEN; NOT PROVED",
            "finite_gcd_patterns": "EXACT FINITE ONLY",
            "weighted_prime_mass_saving": "FAIL; NOT PROVED",
            "new_Route_1_booking": 0,
        },
        "formal_elimination": formal_elimination_check(),
        "all_parameter_theorem": {
            "actual_rows": "p=4h+6s+3 prime, h,s>=1, 3 does not divide h",
            "gauge": "c_h^*=R_h*E_h^*, with R_h a p-unit",
            "common_residual": "Item236 identifies the lower and upper residuals; Item243 makes their common value zero whenever E_h^*=0 mod p",
            "endpoint_equations_on_a_collision": [
                "t_(s+1)*L_h=2*d_h",
                "t_J*U_h=F_h-3*d_h",
                "t_J/t_(s+1)=eta_h",
            ],
            "natural_endpoint_scalar": "K_h=2*d_h*U_h*eta_h-L_h*(F_h-3*d_h)",
            "conclusion": "original j=1 collision implies E_h^*=K_h=0 mod p",
            "smallest_integer_restatement": "if N_E,N_K are the reduced numerators, then p divides gcd(N_E(h),N_K(h))",
        },
        "unit_audit": {
            "E": "Item222 clearing factors have absolute value at most 4h+3<p",
            "gauge": "Item243/229 transition product has no actual numerator or denominator zero",
            "Gosper_antidifferences": "binomial-polynomial denominators divide (2h)!; triangular inversion adds only powers of 2; phase substitution adds only powers of 2 and 3",
            "endpoint_ratio": "its possible denominator factors are powers of 2,3 and the nonzero odd integers 6i-4h+9 (0<=i<=h), all of absolute value <4h+9<=p",
            "consequence": "the reduced denominators of E_h^* and K_h are p-units on every actual row",
        },
        "divisor_height_weighted_mass_admission": {
            "divisor_localization": "all surviving collision primes for fixed h divide gcd(N_E(h),N_K(h))",
            "inherited_integer_clearing": "E_h^*=A_h/[2(4h+3)D_xD_yD_uD_v]",
            "height_bound_when_A_h_nonzero": "|A_h|<=47h*M_h^4, M_h=(h+3)2^(2h+4)(21h)^(h+2)",
            "gcd_height_consequence": "log gcd(N_E,N_K)<=log|A_h|=O(h log h) when A_h is nonzero",
            "summed_bound": "sum_(h<=H) O(h log h)=O(H^2 log H), not o(H)",
            "zero_integer_case": "if A_h=0, the individual E-height argument supplies no restriction and a separate K theorem is still required",
            "small_h_strip": "h=o(H/log H) has zero linear weight, as in Item222; the unbounded-h range remains uncontrolled",
            "admission": "FAIL: no collective gcd/radical estimate and no weighted-density theorem",
        },
        "finite_replay": finite_replay(),
        "capacity": {
            "conditional_j1_cell": "1/6 per m = 1/36 per 6m",
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "booking": 0,
        },
        "open": [
            "prove a unit-localized all-h gcd or resultant theorem for N_E and N_K",
            "decide whether K is redundant modulo every moving prime dividing E or adds genuine arithmetic codimension",
            "prove a collective radical or weighted prime-log-mass bound",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    output = Path(arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_result(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
