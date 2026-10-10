#!/usr/bin/env python3
"""Deterministic certificate for Item 288's large-prime redundancy theorem.

The theorem is proved in the companion report by two finite Gosper
telescopings and a localization argument.  This checker pins the upstream
dependencies, verifies the formal coefficient-recurrence and endpoint
factorizations, and replays the proved identities exactly on a bounded grid.
The bounded replay is not used to extrapolate the theorem.
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
REPLAY_H_MAX = 12


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


item222 = load("item288_item222", resolve("item222_j1_phase_resultant_certificate.py"))
item229 = load("item288_item229", resolve("item229_j1_fixed_h_theta_certificate.py"))
item231 = load("item288_item231", resolve("item231_j1_second_phase_coefficient_certificate.py"))


def compose_linear(
    polynomial: list[Fraction], constant: Fraction, slope: Fraction
) -> list[Fraction]:
    """Return polynomial(constant+slope*j), low-to-high in j."""
    answer = [Fraction(0)]
    power = [Fraction(1)]
    linear = [constant, slope]
    for coefficient in polynomial:
        answer = item229.add(answer, item229.scale(power, coefficient))
        power = item229.multiply(power, linear)
    return item229.trim(answer)


def t_value(s_value: Fraction, index: int) -> Fraction:
    return Fraction((-1) ** index) * item229.binomial_fraction(
        2 * s_value + index - 1, index
    )


def mu_value(s_value: Fraction, index: int) -> Fraction:
    return (
        Fraction((-1) ** index)
        * item231.rising_fraction(3 * s_value + 1, index)
        / item231.rising_fraction(s_value + 2, index)
    )


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


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


def denominator_is_supported(value: Fraction, bound: int) -> bool:
    denominator = value.denominator
    for prime in primes_upto(bound):
        while denominator % prime == 0:
            denominator //= prime
    return denominator == 1


# A linear form is constant + r_coefficient*r + s_coefficient*s.
LinearForm = tuple[int, int, int]


def linear_add(left: LinearForm, right: LinearForm) -> LinearForm:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def linear_scale(value: LinearForm, scalar: int) -> LinearForm:
    return tuple(scalar * entry for entry in value)  # type: ignore[return-value]


def recurrence_row(offset: int) -> dict[int, LinearForm]:
    """Coefficient recurrence for D_n at n=r+offset, keyed by D_(r+shift)."""
    return {
        offset + 1: (offset + 1, 1, 0),
        offset: (-offset - 1, -2, 0),
        offset - 1: (offset - 1, 1, 4),
        offset - 2: (-offset + 1, -2, -4),
    }


def combine_rows(weighted_rows: list[tuple[int, dict[int, LinearForm]]]) -> dict[int, LinearForm]:
    result: dict[int, LinearForm] = {}
    for scalar, row in weighted_rows:
        for shift, coefficient in row.items():
            result[shift] = linear_add(
                result.get(shift, (0, 0, 0)), linear_scale(coefficient, scalar)
            )
    return {shift: value for shift, value in result.items() if value != (0, 0, 0)}


def formal_d_reversal_check() -> dict[str, Any]:
    target = {
        3: (-3, -1, 0),
        2: (5, 3, 0),
        1: (-2, -2, -4),
        0: (0, 1, 8),
        -1: (-1, -1, 0),
        -2: (1, -2, -4),
    }
    derived = combine_rows(
        [(-1, recurrence_row(2)), (1, recurrence_row(1)), (1, recurrence_row(0))]
    )
    if derived != target:
        raise AssertionError((derived, target))
    return {
        "classification": "FORMAL_EXACT",
        "D_recurrence": (
            "(n+1)D_(n+1)-(n+r+1)D_n+(n-1+4s)D_(n-1)"
            "-(n+r-1+4s)D_(n-2)=0"
        ),
        "combination": "-Rec_(r+2)+Rec_(r+1)+Rec_r",
        "consequence": (
            "d=C*D_r+B*D_(r-1)+A*D_(r-2)="
            "sum_(j=0)^(r-1)t_j*Pplus(j)"
        ),
        "coefficient_vector_matches": True,
    }


# Sparse commutative polynomials for the final endpoint factorization.
VARIABLES = ("c", "d", "L", "X", "Y")
Monomial = tuple[int, ...]
Polynomial = dict[Monomial, int]


def variable(name: str) -> Polynomial:
    exponent = [0] * len(VARIABLES)
    exponent[VARIABLES.index(name)] = 1
    return {tuple(exponent): 1}


def polynomial_add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def polynomial_scale(value: Polynomial, scalar: int) -> Polynomial:
    return {monomial: scalar * coefficient for monomial, coefficient in value.items() if scalar * coefficient}


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            result[monomial] = result.get(monomial, 0) + left_coefficient * right_coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def formal_endpoint_factorization_check() -> dict[str, Any]:
    c, d, low, x_value, y_value = (variable(name) for name in VARIABLES)
    eta_u = polynomial_add(polynomial_multiply(c, y_value), polynomial_scale(low, -1))
    fixed = polynomial_add(d, polynomial_multiply(c, x_value))
    original = polynomial_add(
        polynomial_scale(polynomial_multiply(d, eta_u), 2),
        polynomial_scale(
            polynomial_multiply(
                low, polynomial_add(fixed, polynomial_scale(d, -3))
            ),
            -1,
        ),
    )
    factored = polynomial_multiply(
        c,
        polynomial_add(
            polynomial_scale(polynomial_multiply(d, y_value), 2),
            polynomial_scale(polynomial_multiply(low, x_value), -1),
        ),
    )
    if original != factored:
        raise AssertionError((original, factored))
    return {
        "classification": "FORMAL_EXACT",
        "substitutions": ["F=d+c*X", "eta*U+L=c*Y"],
        "identity": "K=c*(2*d*Y-L*X)",
        "expanded_sparse_polynomials_match": True,
    }


def exact_replay() -> dict[str, Any]:
    rows: list[list[Any]] = []
    for h_value in range(1, REPLAY_H_MAX + 1):
        r_value = 2 * h_value
        s_value = Fraction(-(4 * h_value + 3), 6)
        a_value = s_value + 1
        j_value = 3 * h_value + 3 * s_value + 1
        b_value = a_value + h_value + 1
        if j_value != Fraction(2 * h_value - 1, 2):
            raise AssertionError((h_value, "J phase"))
        if b_value != -2 * s_value - j_value:
            raise AssertionError((h_value, "reflected endpoint"))

        low_c, low_r = item229.gosper_reduce(h_value, s_value)
        high_c, high_r = item231.high_gosper_reduce(h_value, s_value)
        if low_c != high_c:
            raise AssertionError((h_value, "residual mismatch"))
        low_polynomial = item229.p_polynomial(h_value, s_value)
        high_polynomial = item231.high_polynomial(h_value, s_value)
        if compose_linear(low_polynomial, -2 * s_value, Fraction(-1)) != high_polynomial:
            raise AssertionError((h_value, "polynomial reflection"))
        reflected_r = item229.scale(
            compose_linear(low_r, -2 * s_value + 1, Fraction(-1)), Fraction(-1)
        )
        if reflected_r != high_r:
            raise AssertionError((h_value, "antidifference reflection"))

        phase = item231.phase_boundary_data(h_value)
        d_value = phase["delta_minus"]
        d_sum = sum(
            t_value(s_value, index) * item229.evaluate(high_polynomial, Fraction(index))
            for index in range(r_value)
        )
        if d_value != d_sum:
            raise AssertionError((h_value, "d finite sum"))

        x_value = -sum(t_value(s_value, index) for index in range(r_value))
        y_value = sum(mu_value(s_value, index) for index in range(h_value + 1))
        if phase["high_lower_boundary"] - d_value != low_c * x_value:
            raise AssertionError((h_value, "F-d factor"))
        if (
            phase["endpoint_ratio"] * phase["high_upper_boundary"]
            + phase["low_boundary"]
            != low_c * y_value
        ):
            raise AssertionError((h_value, "etaU+L factor"))
        z_value = 2 * d_value * y_value - phase["low_boundary"] * x_value
        if phase["natural_eliminant"] != low_c * z_value:
            raise AssertionError((h_value, "K factor"))

        bound = 4 * h_value + 3
        audited = [
            low_c,
            d_value,
            phase["low_boundary"],
            phase["high_lower_boundary"],
            x_value,
            y_value,
            z_value,
            phase["natural_eliminant"],
        ]
        if not all(denominator_is_supported(value, bound) for value in audited):
            raise AssertionError((h_value, "localization denominator"))

        admissible_data: list[Any] = []
        if h_value % 3:
            eliminant, _ = item222.phase_fraction_and_integer(h_value)
            gauge = gauge_ratio(h_value)
            if low_c != gauge * eliminant:
                raise AssertionError((h_value, "Item243 gauge"))
            if not denominator_is_supported(eliminant, bound):
                raise AssertionError((h_value, "E denominator"))
            if not denominator_is_supported(gauge, bound):
                raise AssertionError((h_value, "gauge denominator"))
            numerator_gcd = math.gcd(
                abs(eliminant.numerator), abs(phase["natural_eliminant"].numerator)
            )
            quotient = abs(eliminant.numerator) // numerator_gcd
            quotient_remainder = quotient
            for prime in primes_upto(bound):
                while quotient_remainder % prime == 0:
                    quotient_remainder //= prime
            if quotient_remainder != 1:
                raise AssertionError((h_value, "numerator quotient support"))
            admissible_data = [str(eliminant), str(gauge), quotient]

        row = [
            h_value,
            str(low_c),
            str(x_value),
            str(y_value),
            str(z_value),
            *admissible_data,
        ]
        rows.append(row)

    stream = json.dumps(rows, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return {
        "classification": "EXACT_REPLAY_OF_PROVED_IDENTITIES_NOT_EXTRAPOLATION",
        "h_max": REPLAY_H_MAX,
        "rows": len(rows),
        "admissible_rows": sum(h_value % 3 != 0 for h_value in range(1, REPLAY_H_MAX + 1)),
        "checked_identities": [
            "Pplus(j)=Pminus(-2s-j)",
            "Rplus(j)=-Rminus(-2s-j+1)",
            "d=sum_(j=0)^(2h-1)t_j*Pplus(j)",
            "F-d=c*X",
            "eta*U+L=c*Y",
            "K=c*(2*d*Y-L*X)",
            "c=gauge*E on admissible h",
            "all replay denominators supported on primes <=4h+3",
        ],
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item288-j1-large-prime-redundancy-v1",
        "item": 288,
        "title": "all-h localized redundancy of the Item280 endpoint scalar",
        "dependencies": DEPENDENCIES,
        "formal_d_reversal": formal_d_reversal_check(),
        "formal_endpoint_factorization": formal_endpoint_factorization_check(),
        "theorem": {
            "phase": "s_h=-(4h+3)/6, r=2h",
            "localized_factors": {
                "X_h": "-sum_(j=0)^(2h-1) (-1)^j*binom(2s_h+j-1,j)",
                "Y_h": "sum_(k=0)^h (-1)^k*(3s_h+1)_k/(s_h+2)_k",
                "Z_h": "2*d_h*Y_h-L_h*X_h",
            },
            "exact_identities": [
                "F_h-d_h=c_h*X_h",
                "eta_h*U_h+L_h=c_h*Y_h",
                "K_h=c_h*Z_h",
            ],
            "localization": "X_h,Y_h,Z_h,c_h,K_h lie in Z localized at primes <=4h+3",
            "gauge": "for h>=1, 3 not dividing h, c_h=G_h*E_h with G_h a unit in that localization",
            "prime_implication": (
                "for every prime q>4h+3, q dividing the reduced numerator N_E(h) "
                "implies q divides the reduced numerator N_K(h)"
            ),
            "converse": "NOT CLAIMED",
            "actual_rows": "p=4h+6s+3 with s>=1 has p>=4h+9, so every actual prime is covered",
            "classification": "PROVED EXACT ALL-H",
        },
        "denominator_ledger": {
            "X_terms": "denominator divides 3^j*j!, 0<=j<=2h-1",
            "Y_terms": "denominator divides product_(ell=0)^(k-1)(6ell-4h+9)",
            "Y_linear_factors": "nonzero with absolute value <=4h+3",
            "Gosper_system": "P coefficients use (2h)! and powers of 2,3; descending solve divides only by 2",
            "Item222_E": "2(4h+3)D_xD_yD_uD_v with the pinned explicit linear-factor clearings",
            "gauge": "all prime factors in the bases and every step-ratio numerator/denominator factor are <=4h+3",
        },
        "exact_replay": exact_replay(),
        "capacity": {
            "endpoint_K_large_moving_prime_codimension": 0,
            "new_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_booked": 0,
            "reason": "K is redundant after E at every actual moving prime; nonvanishing or weighted control of E remains open",
        },
        "strict_labels": {
            "large_prime_redundancy": "PROVED",
            "small_prime_support_of_N_E_over_gcd": "PROVED WHEN THE QUOTIENT IS DEFINED",
            "E_nonvanishing_or_sparsity": "OPEN",
            "weighted_prime_mass_saving": "OPEN",
            "Route_1_completion": "OPEN",
            "finite_scan_inference": "NONE",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = build_result()
    output = arguments.output or (
        HERE / "item288_j1_large_prime_redundancy_certificate.json"
        if HERE.name == "work"
        else HERE.parent / "results" / "item288_j1_large_prime_redundancy_certificate.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"output": str(output), "sha256": sha256(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
