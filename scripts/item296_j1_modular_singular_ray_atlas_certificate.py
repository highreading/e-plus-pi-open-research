#!/usr/bin/env python3
"""Exact Item 296 atlas for the modular singular loci of the Item 293 operator.

This checker performs no scan of actual primes.  It solves the finitely many
linear-factor divisibility equations, constructs the four exact diagonal core
polynomials, certifies their irreducibility with finite-field Rabin witnesses,
and records the exact three-state same-characteristic transport theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEPENDENCIES = {
    "item293_j1_E_gate_density_no_go_certificate.py": (
        "2aaa465558d224e1115764fd399a33e07cbc411d57085eefdfcf149ccbb14657"
    ),
    "item293_j1_E_gate_density_no_go_certificate.json": (
        "7af9fd9fe5e6bff2a0402c142479bbca0632c9b5e0f8591a29b41741e1be81f7"
    ),
}


def resolve(name: str) -> Path:
    candidates = (
        HERE / name,
        HERE.parent / "scripts" / name,
        HERE.parent / "results" / name,
    )
    for path in candidates:
        if path.is_file():
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


item293 = load(
    "item296_item293", resolve("item293_j1_E_gate_density_no_go_certificate.py")
)
item293_result = json.loads(
    resolve("item293_j1_E_gate_density_no_go_certificate.json").read_text(
        encoding="utf-8"
    )
)
if item293_result.get("strict_labels", {}).get("integral_E_recurrence") != "PROVED":
    raise AssertionError("Item293 recurrence theorem not admitted")


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1
    return True


def factor_label(constant: int, slope: int) -> str:
    if slope == 1:
        return "h" if constant == 0 else f"h+{constant}"
    return f"{slope}h+{constant}"


def factor_occurrences() -> tuple[list[dict[str, Any]], dict[tuple[int, int], list]]:
    rows = []
    occurrence_map: dict[tuple[int, int], list] = {}
    for coefficient_index, (_, factors, _) in enumerate(item293.Q_FACTORS):
        row_factors = []
        for constant, slope, exponent in factors:
            record = {
                "factor": factor_label(constant, slope),
                "constant": constant,
                "slope": slope,
                "multiplicity": exponent,
            }
            row_factors.append(record)
            occurrence_map.setdefault((slope, constant), []).append(
                [coefficient_index, exponent]
            )
        rows.append({"Q_index": coefficient_index, "linear_factors": row_factors})
    return rows, occurrence_map


def finite_equality_solutions(
    occurrence_map: dict[tuple[int, int], list]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    candidates = []
    for (slope, constant), occurrences in sorted(occurrence_map.items()):
        if slope != 2:
            continue
        # Since 0 < 2h+c < 2p for every factor in the atlas, divisibility
        # forces equality: c=2h+6s+3.
        for s_value in range(1, constant // 6 + 1):
            remainder = constant - 6 * s_value - 3
            if remainder <= 0 or remainder % 2:
                continue
            h_value = remainder // 2
            p_value = 4 * h_value + 6 * s_value + 3
            candidates.append(
                {
                    "source": "slope-2 equality",
                    "factor": factor_label(constant, slope),
                    "h": h_value,
                    "s": s_value,
                    "p": p_value,
                    "h_admissible": h_value % 3 != 0,
                    "p_prime": is_prime(p_value),
                    "occurrences": occurrences,
                }
            )

    # For 4h+c, parity and the global size bound leave quotient 1 or 3.
    # Quotient 3 is possible only at h=1; solve c=17+18s exactly.
    for (slope, constant), occurrences in sorted(occurrence_map.items()):
        if slope != 4:
            continue
        for s_value in range(1, constant // 18 + 1):
            if constant != 17 + 18 * s_value:
                continue
            h_value = 1
            p_value = 4 * h_value + 6 * s_value + 3
            candidates.append(
                {
                    "source": "slope-4 exceptional quotient 3",
                    "factor": factor_label(constant, slope),
                    "factor_over_p": 3,
                    "h": h_value,
                    "s": s_value,
                    "p": p_value,
                    "h_admissible": True,
                    "p_prime": is_prime(p_value),
                    "occurrences": occurrences,
                }
            )

    candidates.sort(key=lambda row: (row["p"], row["factor"], row["source"]))
    actual = [
        row for row in candidates if row["h_admissible"] and row["p_prime"]
    ]
    eliminated = [row for row in candidates if row not in actual]
    expected_actual = [
        (13, "2h+11"),
        (13, "4h+35"),
        (17, "2h+13"),
        (19, "2h+17"),
    ]
    if [(row["p"], row["factor"]) for row in actual] != expected_actual:
        raise AssertionError(("finite singular list", actual))
    if [(row["h"], row["s"], row["p"]) for row in eliminated] != [(4, 1, 25)]:
        raise AssertionError(("eliminated equality list", eliminated))
    return actual, eliminated


def structural_rays(occurrence_map: dict[tuple[int, int], list]) -> list[dict[str, Any]]:
    rows = []
    for (slope, constant), occurrences in sorted(occurrence_map.items()):
        if slope != 4 or (constant - 3) % 6:
            continue
        s_value = (constant - 3) // 6
        if s_value < 1:
            continue
        rows.append(
            {
                "s": s_value,
                "p": f"4h+{constant}",
                "conditions": "h>=1, 3 does not divide h, and p is prime",
                "factor": factor_label(constant, slope),
                "occurrences": occurrences,
            }
        )
    expected = [(2, "4h+15", [[1, 1]]), (4, "4h+27", [[2, 1]]), (6, "4h+39", [[3, 1]])]
    observed = [(row["s"], row["factor"], row["occurrences"]) for row in rows]
    if observed != expected:
        raise AssertionError(("structural rays", observed))
    return rows


def linear_atlas() -> dict[str, Any]:
    factor_rows, occurrence_map = factor_occurrences()
    actual, eliminated = finite_equality_solutions(occurrence_map)
    rays = structural_rays(occurrence_map)

    maximum = {1: 9, 2: 17, 4: 39}
    observed_maximum = {1: 0, 2: 0, 4: 0}
    for slope, constant in occurrence_map:
        observed_maximum[slope] = max(observed_maximum[slope], constant)
    if observed_maximum != maximum:
        raise AssertionError(("linear factor bounds", observed_maximum))

    return {
        "classification": "PROVED EXACT COMPLETE LINEAR-FACTOR ATLAS",
        "factorizations": factor_rows,
        "global_argument": {
            "slope_1": "0<h+c<p for every listed factor; never singular",
            "slope_2": (
                "0<2h+c<2p, so p,2p,3p,... are audited at once: only "
                "the equality 2h+c=p is possible"
            ),
            "slope_4": (
                "0<4h+c<4p.  The possibilities p,2p,3p are complete; 2p is "
                "excluded because 4h+c is odd, p gives the three rays, and 3p "
                "gives the sole finite witness (1,1,13) through 4h+35"
            ),
            "scalar": "all scalar primes are 2 or 3, while every actual p is at least 13",
        },
        "structural_rays": rays,
        "finite_actual_prime_rows": actual,
        "eliminated_composite_or_inadmissible_equalities": eliminated,
        "overlaps": [
            "At (h,s,p)=(1,1,13), 2h+11 divides Q0,Q1 and 4h+35=3p divides Q3.",
            "At (h,s,p)=(1,2,19), the finite factor 2h+17 divides Q0,Q1,Q2 and the s=2 ray factor 4h+15 divides Q1.",
        ],
        "completeness": (
            "These rays and finite rows are every actual-prime divisibility of every "
            "displayed linear factor of Q_0,Q_1,Q_2,Q_3"
        ),
    }


IntegerPolynomial = list[int]


def trim(polynomial: IntegerPolynomial) -> IntegerPolynomial:
    answer = list(polynomial)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def convolution(left: IntegerPolynomial, right: IntegerPolynomial) -> IntegerPolynomial:
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return trim(answer)


def integer_power(polynomial: IntegerPolynomial, exponent: int) -> IntegerPolynomial:
    answer = [1]
    factor = list(polynomial)
    while exponent:
        if exponent & 1:
            answer = convolution(answer, factor)
        exponent >>= 1
        if exponent:
            factor = convolution(factor, factor)
    return answer


def diagonal_core(core: list[int]) -> tuple[int, IntegerPolynomial]:
    degree = len(core) - 1
    raw = [0]
    base = [-3, -6]  # -(6s+3)
    for exponent, coefficient in enumerate(core):
        term = [
            coefficient * 4 ** (degree - exponent) * value
            for value in integer_power(base, exponent)
        ]
        if len(raw) < len(term):
            raw.extend([0] * (len(term) - len(raw)))
        for index, value in enumerate(term):
            raw[index] += value
    content = 0
    for coefficient in raw:
        content = math.gcd(content, abs(coefficient))
    primitive = [coefficient // content for coefficient in raw]
    return content, trim(primitive)


def shift_polynomial(polynomial: IntegerPolynomial, shift: int) -> IntegerPolynomial:
    """Return P(s+shift), low-to-high, exactly."""
    answer = [0] * len(polynomial)
    for exponent, coefficient in enumerate(polynomial):
        for power in range(exponent + 1):
            answer[power] += (
                coefficient
                * math.comb(exponent, power)
                * shift ** (exponent - power)
            )
    return trim(answer)


def mod_trim(polynomial: list[int], prime: int) -> list[int]:
    return trim([coefficient % prime for coefficient in polynomial])


def mod_add(left: list[int], right: list[int], prime: int, sign: int = 1) -> list[int]:
    answer = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += sign * value
    return mod_trim(answer, prime)


def mod_divrem(
    numerator: list[int], denominator: list[int], prime: int
) -> tuple[list[int], list[int]]:
    numerator = mod_trim(numerator, prime)
    denominator = mod_trim(denominator, prime)
    if denominator == [0]:
        raise ZeroDivisionError
    if len(numerator) < len(denominator):
        return [0], numerator
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    inverse_leading = pow(denominator[-1], -1, prime)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse_leading % prime
        quotient[shift] = coefficient
        subtraction = [0] * shift + [coefficient * value for value in denominator]
        remainder = mod_add(remainder, subtraction, prime, -1)
    return mod_trim(quotient, prime), mod_trim(remainder, prime)


def mod_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    left, right = mod_trim(left, prime), mod_trim(right, prime)
    while right != [0]:
        _, remainder = mod_divrem(left, right, prime)
        left, right = right, remainder
    inverse = pow(left[-1], -1, prime)
    return mod_trim([inverse * value for value in left], prime)


def mod_multiply(
    left: list[int], right: list[int], modulus: list[int], prime: int
) -> list[int]:
    product = convolution(left, right)
    _, remainder = mod_divrem(product, modulus, prime)
    return remainder


def mod_power(
    base: list[int], exponent: int, modulus: list[int], prime: int
) -> list[int]:
    answer = [1]
    factor = mod_trim(base, prime)
    while exponent:
        if exponent & 1:
            answer = mod_multiply(answer, factor, modulus, prime)
        exponent >>= 1
        if exponent:
            factor = mod_multiply(factor, factor, modulus, prime)
    return answer


def distinct_prime_divisors(value: int) -> list[int]:
    answer = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            answer.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        answer.append(value)
    return answer


def rabin_irreducible(polynomial: list[int], prime: int) -> bool:
    polynomial = mod_trim(polynomial, prime)
    degree = len(polynomial) - 1
    if degree < 1 or polynomial[-1] == 0:
        return False
    x_polynomial = [0, 1]
    frobenius = x_polynomial
    check_indices = {degree // divisor for divisor in distinct_prime_divisors(degree)}
    for index in range(1, degree + 1):
        frobenius = mod_power(frobenius, prime, polynomial, prime)
        if index in check_indices:
            difference = mod_add(frobenius, x_polynomial, prime, -1)
            if mod_gcd(polynomial, difference, prime) != [1]:
                return False
    return mod_add(frobenius, x_polynomial, prime, -1) == [0]


def core_atlas() -> dict[str, Any]:
    witnesses = [17, 53, 157, 17]
    expected_contents = [432, 62208, 139968, 432]
    content_factorizations = ["2^4*3^3", "2^8*3^5", "2^6*3^7", "2^4*3^3"]
    rows = []
    primitive_polynomials = []
    for coefficient_index, ((_, _, core), witness) in enumerate(
        zip(item293.Q_FACTORS, witnesses)
    ):
        content, primitive = diagonal_core(core)
        if content != expected_contents[coefficient_index]:
            raise AssertionError(("diagonal content", coefficient_index, content))
        supported_part = content
        for small_prime in (2, 3):
            while supported_part % small_prime == 0:
                supported_part //= small_prime
        if supported_part != 1:
            raise AssertionError(("content is not 2,3-supported", content))
        if not rabin_irreducible(primitive, witness):
            raise AssertionError(("irreducibility witness", coefficient_index, witness))
        primitive_polynomials.append(primitive)
        rows.append(
            {
                "Q_index": coefficient_index,
                "core_degree": len(core) - 1,
                "raw_R_content": content,
                "raw_R_content_factorization": content_factorizations[coefficient_index],
                "primitive_Rhat_low_to_high": primitive,
                "irreducible_modulus": witness,
                "primitive_Rhat_irreducible_over_Q": True,
            }
        )
    if primitive_polynomials[0] != shift_polynomial(primitive_polynomials[3], -2):
        raise AssertionError("Rhat_0(s)=Rhat_3(s-2)")
    if item293.Q_FACTORS[0][2] != shift_polynomial(item293.Q_FACTORS[3][2], 3):
        raise AssertionError("q_0(h)=q_3(h+3)")
    return {
        "classification": "PROVED EXACT CORE-CONGRUENCE ATLAS",
        "definition": (
            "R_k(s)=4^deg(q_k)*q_k(-(6s+3)/4); content(R_k)=c_k and "
            "primitive part Rhat_k=R_k/c_k"
        ),
        "exact_actual_row_equivalence": (
            "on p=4h+6s+3, p divides q_k(h) iff p divides Rhat_k(s); "
            "the only primes in 4*c_k are 2 and 3, while every actual p>=13"
        ),
        "rows": rows,
        "structural_distinction": (
            "Each primitive Rhat_k is irreducible over Q and has degree 5 or 9, hence has no "
            "integer root.  Core singularities are genuine varying-prime congruences, "
            "not additional exact fixed-s rays"
        ),
        "fixed_s_consequence": (
            "for each fixed positive s, Rhat_k(s) is a fixed nonzero integer, so only "
            "finitely many row primes on that fixed s can be core-singular"
        ),
        "adjacent_endpoint_identity": (
            "Rhat_0(s)=Rhat_3(s-2), equivalently q_0(h)=q_3(h+3); "
            "a trailing core singularity is the next diagonal cell's leading core singularity"
        ),
    }


def transport_theorem() -> dict[str, Any]:
    # The companion matrix [[0,1,0],[0,0,1],[-Q0/Q3,-Q1/Q3,-Q2/Q3]]
    # has determinant -Q0/Q3.  Its first two rows and nonzero determinant
    # also show that every coordinate pullback is a nonzero linear form.
    return {
        "classification": "PROVED EXACT RECURRENCE-ONLY MODULAR OBSTRUCTION",
        "same_prime_diagonal": "(h,s)->(h+3,s-2), preserving p=4h+6s+3",
        "interior_relation": (
            "for s>=7 the four entries E_h,E_(h+3),E_(h+6),E_(h+9) are "
            "all p-integral and lie on the same actual-prime diagonal"
        ),
        "companion_matrix": (
            "T_h=[[0,1,0],[0,0,1],[-Q0/Q3,-Q1/Q3,-Q2/Q3]] over F_p"
        ),
        "determinant": "det(T_h)=-Q0(h)/Q3(h)",
        "regular_locus": (
            "in the interior s>=7 all linear factors of Q0 and Q3 are p-units; "
            "the forward companion step is defined and invertible exactly off "
            "Rhat0(s)=0 or Rhat3(s)=0 mod p"
        ),
        "zero_hyperplane": (
            "on every regular finite diagonal interval, the states form F_p^3. "
            "Vanishing of any selected scalar coordinate is a dimension-2 hyperplane "
            "of p^2 valid recurrence states, and invertible transport pulls it back "
            "to another dimension-2 hyperplane"
        ),
        "consequence": (
            "the recurrence supplies exact three-state same-characteristic transport "
            "but no scalar zero descent or zero propagation.  Excluding the actual "
            "E_h state from those hyperplanes requires sequence-specific initial-state, "
            "congruence, monodromy, Cartier, or auxiliary-local input"
        ),
        "not_ruled_out": (
            "an argument evaluating the exact Item293 initial state through the transfer, "
            "or any new sequence-specific local invariant"
        ),
        "scope": (
            "the p^2 zero-hyperplane statement concerns the unrestricted module of "
            "valid recurrence states.  It does not assert that the pinned actual E "
            "initial orbit meets any such hyperplane"
        ),
    }


def build_result() -> dict[str, Any]:
    return {
        "schema": "item296-j1-modular-singular-ray-atlas-v1",
        "item": 296,
        "title": "exact modular singular-ray atlas for the primitive E recurrence",
        "dependencies": DEPENDENCIES,
        "linear_factor_atlas": linear_atlas(),
        "positive_core_atlas": core_atlas(),
        "complete_modular_criterion": (
            "For each k=0,1,2,3 and every actual row, p divides Q_k(h) if and "
            "only if at least one linear factor lies in the proved linear atlas "
            "or p divides the corresponding primitive diagonal core Rhat_k(s)."
        ),
        "same_characteristic_transport": transport_theorem(),
        "capacity": {
            "new_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_booked": 0,
            "retained_conditional_j1_capacity_per_6m": "1/36",
            "reason": (
                "the atlas classifies operator singularities but does not bound the "
                "moving-prime zero set of the pinned E sequence"
            ),
        },
        "strict_labels": {
            "complete_linear_factor_atlas": "PROVED",
            "core_congruence_reduction_and_irreducibility": "PROVED",
            "regular_three_state_transport": "PROVED",
            "recurrence_only_scalar_zero_control": "PROVED IMPOSSIBLE IN STATED LOCAL SCOPE",
            "sequence_specific_weighted_density": "OPEN",
            "prime_scan": "NONE",
            "Route_1": "OPEN",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = build_result()
    output = arguments.output or (
        HERE / "item296_j1_modular_singular_ray_atlas_certificate.json"
        if HERE.name == "work"
        else HERE.parent / "results" / "item296_j1_modular_singular_ray_atlas_certificate.json"
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
