#!/usr/bin/env python3
"""Deterministic certificate for Item 231.

The exact theorem rewrites Item 228's second invariant as one coefficient
of the same generating series that supplies Item 223's first terminal.
The checker also verifies the Cartier/Frobenius defect formula, a declared
finite phase-Gosper comparison, and the precise scope of Item 232's
diagonal incomplete-binomial recurrence.
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
RESULT_NAME = "item231_j1_second_phase_coefficient_certificate.json"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, filename: str):
    path = resolve(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM222_PATH = resolve("item222_j1_phase_resultant_certificate.py")
ITEM223_PATH = resolve("item223_j1_frobenius_transfer_certificate.py")
ITEM228_PATH = resolve("item228_j1_second_frobenius_certificate.py")
ITEM229_PATH = resolve("item229_j1_fixed_h_theta_certificate.py")

item222 = load("item231_item222", ITEM222_PATH.name)
item223 = load("item231_item223", ITEM223_PATH.name)
item228 = load("item231_item228", ITEM228_PATH.name)
item229 = load("item231_item229", ITEM229_PATH.name)
item218 = item223.item218


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def g_coefficient(r_value: int, s_value: int, degree: int) -> int:
    """[x^degree] R(x)/((1-x)^(r+1)(1+x^2)^(2s))."""
    if degree < 0:
        return 0
    coefficient = item223.base_coefficient
    return (
        (2 * r_value + 4 * s_value - 1)
        * coefficient(r_value, s_value, degree)
        + (r_value + 1) * coefficient(r_value, s_value, degree - 1)
        - (r_value + 8 * s_value)
        * coefficient(r_value, s_value, degree - 2)
    )


def t_integer(s_value: int, index: int) -> int:
    return (-1) ** index * math.comb(2 * s_value + index - 1, index)


def h_tail_sum(
    prime: int, r_value: int, s_value: int
) -> int:
    """The reciprocal t_j expression for H=g_(a+p)-g_a modulo p."""
    a_coefficient = 2 * r_value + 4 * s_value - 1
    b_coefficient = r_value + 1
    c_coefficient = -(r_value + 8 * s_value)
    upper = (prime + r_value - 1) // 2
    first = c_coefficient * sum(
        t_integer(s_value, index) * math.comb(2 * index - r_value - 1, r_value)
        for index in range(r_value + 1, upper + 1)
    )
    second = b_coefficient * sum(
        t_integer(s_value, index) * math.comb(2 * index - r_value, r_value)
        for index in range(r_value, upper + 1)
    )
    third = a_coefficient * sum(
        t_integer(s_value, index) * math.comb(2 * index - r_value + 1, r_value)
        for index in range(r_value, upper)
    )
    return (first + second + third) % prime


def all_row_replay(prime_max: int) -> dict[str, Any]:
    rows = []
    for prime, h_value, r_value, s_value in item228.actual_rows(prime_max):
        data = item228.second_transfer_components(prime, r_value, s_value)
        lower_index = 2 * s_value + 4
        upper_index = lower_index + prime
        lower = g_coefficient(r_value, s_value, lower_index) % prime
        upper = g_coefficient(r_value, s_value, upper_index) % prime
        if lower != data["delta_plus"]:
            raise AssertionError((prime, r_value, s_value, "lower coefficient"))
        first_source = (-4 * data["epsilon"]) % prime
        cross_left = (
            lower * data["rho_constant"]
            + first_source * data["rho_lambda"]
        ) % prime
        cross_right = first_source * upper % prime
        if cross_left != cross_right:
            raise AssertionError(
                (prime, r_value, s_value, "cross relation", cross_left, cross_right)
            )
        expected_psi = (
            -2 * data["epsilon"] * (lower + 2 * upper)
        ) % prime
        if data["psi"] != expected_psi:
            raise AssertionError(
                (prime, r_value, s_value, data["psi"], expected_psi)
            )
        defect = (upper - lower) % prime
        reciprocal_defect = h_tail_sum(prime, r_value, s_value)
        if defect != reciprocal_defect:
            raise AssertionError(
                (prime, r_value, s_value, defect, reciprocal_defect)
            )
        upper_endpoint = (prime + r_value - 1) // 2
        lower_t = t_integer(s_value, s_value + 1) % prime
        upper_t = t_integer(s_value, upper_endpoint) % prime
        endpoint_ratio = upper_t * pow(lower_t, -1, prime) % prime
        ratio_numerator = (-1) ** (h_value + 1)
        ratio_denominator = 1
        for offset in range(h_value + 1):
            ratio_numerator = (
                ratio_numerator * (3 * s_value + 1 + offset)
            ) % prime
            ratio_denominator = (
                ratio_denominator * (s_value + 2 + offset)
            ) % prime
        expected_ratio = (
            ratio_numerator * pow(ratio_denominator, -1, prime)
        ) % prime
        if endpoint_ratio != expected_ratio:
            raise AssertionError(
                (prime, r_value, s_value, endpoint_ratio, expected_ratio)
            )
        delta_minus = data["delta_minus"]
        theta_zero = lower == 2 * delta_minus % prime and lower != 0
        psi_zero = data["psi"] == 0
        coefficient_condition = upper == -delta_minus % prime
        if theta_zero and psi_zero != coefficient_condition:
            raise AssertionError(
                (prime, r_value, s_value, "collision reformulation")
            )
        rows.append(
            (
                prime,
                h_value,
                s_value,
                lower,
                upper,
                defect,
                data["psi"],
                int(theta_zero),
                int(coefficient_condition),
            )
        )
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_REPLAY_OF_PROVED_ALL_ROW_IDENTITIES",
        "prime_max": prime_max,
        "actual_rows": len(rows),
        "lower_index": "a=2s+4",
        "upper_index": "a+p",
        "delta_plus": "g_a",
        "psi": "-2epsilon*(g_a+2g_(a+p)) mod p",
        "cross_relation": "g_a*rho_constant-4epsilon*rho_lambda=-4epsilon*g_(a+p)",
        "frobenius_defect": "H=g_(a+p)-g_a equals the displayed reciprocal t_j tail",
        "endpoint_ratio": "t_J/t_(s+1)=(-1)^(h+1)(3s+1)_(h+1)/(s+2)_(h+1) mod p",
        "collision_reformulation": (
            "Theta=Psi=0 with nonzero transfers iff "
            "g_a=2Delta_minus and g_(a+p)=-Delta_minus; equivalently H=-3Delta_minus"
        ),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def finite_survivors(prime_max: int) -> dict[str, Any]:
    counts = {
        "actual_rows": 0,
        "theta_survivors": 0,
        "upper_coefficient_nonzero_condition_on_survivors": 0,
        "theta_psi_joint_zero": 0,
        "theta_item222_E_joint_zero": 0,
        "theta_psi_E_triple_zero": 0,
    }
    rows = []
    for prime, h_value, r_value, s_value in item228.actual_rows(prime_max):
        counts["actual_rows"] += 1
        lower, delta_minus = item223.transfer_mod(r_value, s_value, prime)
        if lower != 2 * delta_minus % prime or lower == 0:
            continue
        counts["theta_survivors"] += 1
        upper = g_coefficient(r_value, s_value, prime + 2 * s_value + 4) % prime
        coefficient_condition = (upper + delta_minus) % prime
        psi = -2 * item228.epsilon_for(prime) * (lower + 2 * upper) % prime
        if coefficient_condition:
            counts["upper_coefficient_nonzero_condition_on_survivors"] += 1
        else:
            counts["theta_psi_joint_zero"] += 1
        eliminant, _ = item222.phase_mod(h_value, prime)
        if eliminant == 0:
            counts["theta_item222_E_joint_zero"] += 1
        if eliminant == coefficient_condition == 0:
            counts["theta_psi_E_triple_zero"] += 1
        rows.append(
            (
                prime,
                h_value,
                s_value,
                lower,
                delta_minus,
                upper,
                coefficient_condition,
                psi,
                eliminant,
            )
        )
    expected = {
        "actual_rows": 22934,
        "theta_survivors": 22,
        "upper_coefficient_nonzero_condition_on_survivors": 22,
        "theta_psi_joint_zero": 0,
        "theta_item222_E_joint_zero": 0,
        "theta_psi_E_triple_zero": 0,
    }
    if prime_max == 2000 and counts != expected:
        raise AssertionError((counts, expected))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_ONLY",
        "prime_max": prime_max,
        **counts,
        "first_rows": [list(row) for row in rows[:8]],
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "scope_warning": (
            "joint emptiness through the declared bound is not an all-prime theorem "
            "or a weighted-density estimate"
        ),
    }


def binomial_positive(top_constant: Fraction, degree: int) -> list[Fraction]:
    """The polynomial binom(2j+top_constant, degree), low-to-high in j."""
    answer = [Fraction(1)]
    for offset in range(degree):
        answer = item229.multiply(
            answer, [top_constant - offset, Fraction(2)]
        )
    return item229.scale(answer, Fraction(1, math.factorial(degree)))


def high_polynomial(h_value: int, s_value: Fraction) -> list[Fraction]:
    r_value = 2 * h_value
    a_coefficient = 2 * r_value + 4 * s_value - 1
    b_coefficient = r_value + 1
    c_coefficient = -(r_value + 8 * s_value)
    return item229.add(
        item229.add(
            item229.scale(
                binomial_positive(Fraction(-r_value - 1), r_value),
                c_coefficient,
            ),
            item229.scale(
                binomial_positive(Fraction(-r_value), r_value),
                b_coefficient,
            ),
        ),
        item229.scale(
            binomial_positive(Fraction(-r_value + 1), r_value),
            a_coefficient,
        ),
    )


def high_gosper_reduce(
    h_value: int, s_value: Fraction
) -> tuple[Fraction, list[Fraction]]:
    degree = 2 * h_value
    columns = []
    for power in range(degree):
        basis = [Fraction(0)] * power + [Fraction(1)]
        columns.append(item229.operator_l(basis, s_value))
    columns.append([Fraction(1)])
    polynomial = high_polynomial(h_value, s_value)
    solution = item229.solve_square(columns, polynomial)
    r_polynomial = item229.trim(solution[:-1])
    c_value = solution[-1]
    reconstructed = item229.add(
        item229.operator_l(r_polynomial, s_value), [c_value]
    )
    if reconstructed != polynomial:
        raise AssertionError((h_value, s_value, "high Gosper reconstruction"))
    return c_value, r_polynomial


def generalized_d_coefficient(
    r_value: int, s_value: Fraction, degree: int
) -> Fraction:
    return sum(
        (-1) ** index
        * item229.binomial_fraction(2 * s_value + index - 1, index)
        * math.comb(r_value + degree - 2 * index, degree - 2 * index)
        for index in range(degree // 2 + 1)
    )


def phase_delta_minus(h_value: int, s_value: Fraction) -> Fraction:
    r_value = 2 * h_value
    return (
        -(r_value + 3)
        * generalized_d_coefficient(r_value, s_value, r_value + 3)
        + (3 * r_value + 5)
        * generalized_d_coefficient(r_value, s_value, r_value + 2)
        - (2 * r_value + 4 * s_value + 2)
        * generalized_d_coefficient(r_value, s_value, r_value + 1)
    )


def rising_fraction(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value + offset
    return answer


def phase_boundary_data(h_value: int) -> dict[str, Fraction]:
    s_value = Fraction(-(4 * h_value + 3), 6)
    r_value = 2 * h_value
    a_coefficient = 2 * r_value + 4 * s_value - 1
    low_c, low_r = item229.gosper_reduce(h_value, s_value)
    high_c, high_r = high_gosper_reduce(h_value, s_value)

    tail_one = (
        (4 * h_value + 4 * s_value - 1) * math.comb(2 * h_value + 2, 2)
        + (2 * h_value + 1) ** 2
        - (2 * h_value + 8 * s_value)
    )
    t_s2_over_t_s1 = Fraction(-(3 * s_value + 1), s_value + 2)
    low_boundary = (
        (s_value + 1) * item229.evaluate(low_r, s_value + 1)
        + tail_one
        + a_coefficient * t_s2_over_t_s1
    )

    delta_minus = phase_delta_minus(h_value, s_value)
    upper = 3 * h_value + 3 * s_value + 1
    high_upper_boundary = (
        -(2 * s_value + upper) * item229.evaluate(high_r, upper + 1)
        - a_coefficient
        * item229.binomial_fraction(2 * upper - r_value + 1, r_value)
    )
    t_r = item229.binomial_fraction(2 * s_value + r_value - 1, r_value)
    high_lower_boundary = (
        r_value * t_r * item229.evaluate(high_r, r_value)
    )
    endpoint_ratio = (
        Fraction((-1) ** (h_value + 1))
        * rising_fraction(3 * s_value + 1, h_value + 1)
        / rising_fraction(s_value + 2, h_value + 1)
    )
    natural_eliminant = (
        2 * delta_minus * high_upper_boundary * endpoint_ratio
        - low_boundary * (high_lower_boundary - 3 * delta_minus)
    )
    return {
        "s_phase": s_value,
        "low_c": low_c,
        "high_c": high_c,
        "low_boundary": low_boundary,
        "delta_minus": delta_minus,
        "high_upper_boundary": high_upper_boundary,
        "high_lower_boundary": high_lower_boundary,
        "endpoint_ratio": endpoint_ratio,
        "natural_eliminant": natural_eliminant,
    }


def prime_factorization(value: int) -> list[tuple[int, int]]:
    value = abs(value)
    answer = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            exponent = 0
            while value % divisor == 0:
                value //= divisor
                exponent += 1
            answer.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        answer.append((value, 1))
    return answer


def finite_phase_comparison(h_max: int) -> dict[str, Any]:
    rows = []
    for h_value in range(1, h_max + 1):
        data = phase_boundary_data(h_value)
        c_equal = data["low_c"] == data["high_c"]
        if not c_equal:
            raise AssertionError((h_value, "phase residual mismatch"))
        row: dict[str, Any] = {
            "h": h_value,
            "low_high_residual_equal": True,
            "residual_numerator": data["low_c"].numerator,
            "residual_denominator": data["low_c"].denominator,
        }
        if h_value % 3:
            eliminant, _ = item222.phase_fraction_and_integer(h_value)
            natural = data["natural_eliminant"]
            common = math.gcd(abs(eliminant.numerator), abs(natural.numerator))
            quotient = abs(eliminant.numerator) // common
            factorization = prime_factorization(quotient)
            if any(prime > 4 * h_value + 3 for prime, _ in factorization):
                raise AssertionError((h_value, quotient, factorization))
            row.update(
                {
                    "admissible_h": True,
                    "phase_E_numerator_over_gcd_with_natural_eliminant": quotient,
                    "quotient_factorization": [list(pair) for pair in factorization],
                }
            )
        else:
            row["admissible_h"] = False
        rows.append(row)
    stream = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode("ascii")
    return {
        "classification": "EXACT_FINITE_PATTERN_ONLY",
        "h_max": h_max,
        "rows": rows,
        "observations": [
            "c_high(h,s*)=c_low(h,s*) on every tested h",
            (
                "for tested admissible h, every prime left in the reduced "
                "E numerator after gcd with the natural endpoint eliminant is <=4h+3"
            ),
        ],
        "all_h_status": (
            "OPEN: neither observation is promoted to an all-h factorization, "
            "resultant, or prime exclusion"
        ),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def s_diagonal(n_value: int) -> int:
    return sum(
        (-1) ** index * math.comb(2 * n_value + index - 1, index)
        for index in range(n_value + 1)
    ) if n_value else 1


def item232_scope_check(limit: int = 100) -> dict[str, Any]:
    rows = []
    for n_value in range(1, limit + 1):
        left = (
            2
            * n_value
            * (2 * n_value + 1)
            * (4 * s_diagonal(n_value + 1) - s_diagonal(n_value))
        )
        right = (
            (28 * n_value * n_value + 25 * n_value + 5)
            * (-1) ** (n_value + 1)
            * math.comb(3 * n_value, n_value + 1)
        )
        if left != right:
            raise AssertionError((n_value, left, right))
        rows.append((n_value, left))

    prime, h_value, r_value, s_value = next(item228.actual_rows(20))
    upper = (prime + r_value - 1) // 2
    fixed_parameter_partial = sum(
        t_integer(s_value, index) for index in range(upper + 1)
    )
    diagonal_partial = s_diagonal(upper)
    if fixed_parameter_partial == diagonal_partial:
        raise AssertionError("chosen scope witness unexpectedly equal")
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "PROVED_SCOPE_DISTINCTION_WITH_EXACT_REPLAY",
        "diagonal_identity_checked_through": limit,
        "diagonal_identity": (
            "2n(2n+1)(4S_(n+1)-S_n)=(28n^2+25n+5)(-1)^(n+1)binom(3n,n+1)"
        ),
        "high_residual_coordinate": (
            "T_(h,s)=sum_(j=r)^J (-1)^j binom(2s+j-1,j), "
            "J=3h+3s+1; its binomial parameter remains s"
        ),
        "scope_reason": (
            "Item232 shifts the diagonal sequence where both the upper endpoint "
            "and binomial parameter are n.  It does not relate the fixed-s partial "
            "sum at J to the row value at s."
        ),
        "first_parameter_mismatch_witness": {
            "p": prime,
            "h": h_value,
            "s": s_value,
            "J": upper,
            "fixed_s_partial_sum_0_to_J": fixed_parameter_partial,
            "diagonal_S_J": diagonal_partial,
        },
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def certificate(
    prime_max: int, proof_prime_max: int, phase_h_max: int
) -> dict[str, Any]:
    return {
        "item": 231,
        "schema": "item231-j1-second-phase-coefficient-v1",
        "dependencies": {
            ITEM222_PATH.name: sha256(ITEM222_PATH),
            ITEM223_PATH.name: sha256(ITEM223_PATH),
            ITEM228_PATH.name: sha256(ITEM228_PATH),
            ITEM229_PATH.name: sha256(ITEM229_PATH),
        },
        "definitions": {
            "cell": "p=2r+6s+3, r=2h, h>=1, s>=1",
            "a": "2s+4",
            "D": "1/((1-x)^(r+1)*(1+x^2)^(2s))",
            "R": "(2r+4s-1)+(r+1)x-(r+8s)x^2",
            "g_n": "[x^n]R*D",
            "H": "g_(a+p)-g_a",
        },
        "all_row_theorem": all_row_replay(proof_prime_max),
        "finite_survivor_census": finite_survivors(prime_max),
        "finite_phase_comparison": finite_phase_comparison(phase_h_max),
        "item232_scope": item232_scope_check(),
        "status_ledger": {
            "PROVED": [
                "Delta_plus=g_a and Psi=-2epsilon(g_a+2g_(a+p)) on every actual row",
                "simultaneous Theta=Psi=0 is equivalent to g_a=2Delta_minus and g_(a+p)=-Delta_minus, hence H=-3Delta_minus",
                "the explicit reciprocal t_j formula for H",
                "Item232's diagonal recurrence does not act on the fixed-s high partial sum",
            ],
            "EXACT_FINITE_ONLY": [
                f"the source replay through p<={proof_prime_max}",
                f"the survivor and triple scan through p<={prime_max}",
                f"the phase residual/resultant patterns through h<={phase_h_max}",
            ],
            "OPEN": [
                "an all-h proof of c_high(h,s*)=c_low(h,s*)",
                "an all-h factorization or unit-localized gcd theorem for the natural phase eliminant and Item222 A_h",
                "all-prime exclusion or a weighted bound for simultaneous Theta=Psi zeros",
                "any positive Route-1 rate or radical saving from the j=1 cell",
            ],
        },
        "rate_ledger": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "reason": (
                "the exact second coefficient condition leaves an uncontrolled "
                "same-row incomplete-binomial/Frobenius boundary coordinate"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=2000)
    parser.add_argument("--proof-prime-max", type=int, default=251)
    parser.add_argument("--phase-h-max", type=int, default=20)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.prime_max < 2000 or args.proof_prime_max < 13 or args.phase_h_max < 1:
        raise ValueError("canonical bounds require prime-max>=2000, proof-prime-max>=13, phase-h-max>=1")
    result = certificate(args.prime_max, args.proof_prime_max, args.phase_h_max)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "proof_rows": result["all_row_theorem"]["actual_rows"],
                "theta_survivors": result["finite_survivor_census"]["theta_survivors"],
                "theta_psi_joint_zero": result["finite_survivor_census"]["theta_psi_joint_zero"],
                "phase_h_max": args.phase_h_max,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
