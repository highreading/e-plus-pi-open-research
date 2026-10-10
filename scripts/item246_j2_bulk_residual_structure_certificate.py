#!/usr/bin/env python3
"""Deterministic certificate for Item 246's canonical j=2 bulk residual.

The checker gives the Item 244 scalar B_0 a closed coefficient/double-
integral functional, verifies exact factor/seed recurrences in the row
parameters, audits reciprocity at the reflected pole, and checks the
two-coordinate companion-parity relation.  Finite censuses are labelled.
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
RESULT_NAME = "item246_j2_bulk_residual_structure_certificate.json"
ITEM244_SHA256 = "2cf312df16f7ddc65e57f7b6409a04f38a14242725ac89c1199b7364aa2a84a9"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


ITEM244_PATH = resolve("item244_j2_actual_character_bulk_certificate.py")
if sha256(ITEM244_PATH) != ITEM244_SHA256:
    raise RuntimeError("Item244 checker hash mismatch")
item244 = load("item246_item244", ITEM244_PATH)
item241 = item244.item241
item239 = item244.item239


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def valuation(integer: int, prime: int) -> int:
    value = abs(integer)
    result = 0
    while value and value % prime == 0:
        value //= prime
        result += 1
    return result


def trim(polynomial: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    result = list(polynomial)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def poly_add(left: tuple[int, ...], right: tuple[int, ...], p: int) -> tuple[int, ...]:
    size = max(len(left), len(right))
    result = [0] * size
    for k in range(size):
        result[k] = (
            (left[k] if k < len(left) else 0)
            + (right[k] if k < len(right) else 0)
        ) % p
    return trim(result)


def poly_shift(polynomial: tuple[int, ...], places: int) -> tuple[int, ...]:
    return (0,) * places + polynomial if polynomial else ()


def poly_scale(polynomial: tuple[int, ...], scalar: int, p: int) -> tuple[int, ...]:
    return trim(tuple(scalar * value % p for value in polynomial))


def poly_linear(polynomial: tuple[int, ...], sign: int, p: int) -> tuple[int, ...]:
    """Multiply by 1+sign*t."""
    if not polynomial:
        return ()
    result = [0] * (len(polynomial) + 1)
    for k, value in enumerate(polynomial):
        result[k] = (result[k] + value) % p
        result[k + 1] = (result[k + 1] + sign * value) % p
    return trim(result)


def functional_mod(p: int, lower: int, polynomial: tuple[int, ...]) -> tuple[int, int]:
    """Return (B_L[D], S_L[D]) modulo p in O(deg D)."""
    if not polynomial:
        return 0, 0
    degree = len(polynomial) - 1
    q_next = 0
    bulk_next = 0
    sine = 0
    for k in range(degree, -1, -1):
        denominator = (2 * (lower + k) + 1) % p
        if denominator == 0:
            raise ZeroDivisionError((p, lower, k, "functional pole"))
        inverse = pow(denominator, -1, p)
        weight = polynomial[k] * inverse % p
        sine += ((-1) ** k) * weight
        bulk_here = bulk_next
        if k < degree:
            bulk_here = (bulk_next + q_next * inverse) % p
        q_here = (weight - q_next) % p
        q_next, bulk_next = q_here, bulk_here
    return bulk_next % p, sine % p


def bulk_pair_mod(p: int, lower: int, polynomial: tuple[int, ...]) -> int:
    """Closed triangular coefficient representation of B_L[D]."""
    total = 0
    for v in range(1, len(polynomial)):
        denominator_v = (2 * (lower + v) + 1) % p
        inverse_v = pow(denominator_v, -1, p)
        for k in range(v):
            denominator_k = (2 * (lower + k) + 1) % p
            total += (
                ((-1) ** (v - k - 1))
                * polynomial[v]
                * inverse_v
                * pow(denominator_k, -1, p)
            )
    return total % p


def functional_fraction(lower: int, polynomial: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    """Exact rational (B_L[D], S_L[D]) for an integer polynomial."""
    if not polynomial:
        return Fraction(0), Fraction(0)
    degree = len(polynomial) - 1
    q_next = Fraction(0)
    bulk_next = Fraction(0)
    sine = Fraction(0)
    for k in range(degree, -1, -1):
        denominator = 2 * (lower + k) + 1
        weight = Fraction(polynomial[k], denominator)
        sine += ((-1) ** k) * weight
        bulk_here = bulk_next
        if k < degree:
            bulk_here = bulk_next + q_next / denominator
        q_here = weight - q_next
        q_next, bulk_next = q_here, bulk_here
    return bulk_next, sine


def bulk_pair_fraction(lower: int, polynomial: tuple[int, ...]) -> Fraction:
    total = Fraction(0)
    for v in range(1, len(polynomial)):
        denominator_v = 2 * (lower + v) + 1
        for k in range(v):
            denominator_k = 2 * (lower + k) + 1
            total += Fraction(
                ((-1) ** (v - k - 1)) * polynomial[v],
                denominator_v * denominator_k,
            )
    return total


def parity_seeds(p: int, gap: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Generate E_(gap,0), E_(gap,1) by the exact R recurrence."""
    even = (1,)
    odd: tuple[int, ...] = ()
    for _ in range(gap):
        new_even = poly_add(even, poly_shift(odd, 1), p)
        new_odd = poly_add(even, odd, p)
        even, odd = new_even, new_odd
    expected_even = trim(
        tuple(math.comb(gap, 2 * j) % p for j in range(gap // 2 + 1))
    )
    expected_odd = trim(
        tuple(
            math.comb(gap, 2 * j + 1) % p
            for j in range((gap - 1) // 2 + 1)
        ) if gap else ()
    )
    if even != expected_even or odd != expected_odd:
        raise AssertionError((p, gap, "seed recurrence", even, odd))
    return even, odd


def row_functional_recurrence(p: int, s: int, nu: int) -> tuple[int, int]:
    """Evaluate (B,S) from the row parameters using only exact operators."""
    r = (p - 6 * s - 3) // 2
    a = 1 + 3 * nu
    q = 2 * s - nu
    delta = r % 2
    common = min(r, a)
    gap = abs(r - a)
    even, odd = parity_seeds(p, gap)
    seed = even if delta == 0 else odd
    if not seed:
        return 0, 0
    sigma = (-1) ** delta if r >= a else 1
    total_factors = common + q
    lower = (r + 1) // 2
    states = [functional_mod(p, lower + shift, seed) for shift in range(total_factors + 1)]

    # Multiplication by 1+sign*t acts on (B_L,S_L) through L and L+1.
    for sign, count in ((-1, common), (1, q)):
        for _ in range(count):
            updated: list[tuple[int, int]] = []
            for shift in range(len(states) - 1):
                bulk, sine = states[shift]
                bulk_next, sine_next = states[shift + 1]
                denominator = (2 * (lower + shift) + 1) % p
                updated.append(
                    (
                        (
                            bulk
                            + sign
                            * (bulk_next + sine_next * pow(denominator, -1, p))
                        )
                        % p,
                        (sine - sign * sine_next) % p,
                    )
                )
            states = updated
    if len(states) != 1:
        raise AssertionError((p, s, nu, "row recurrence dimension"))
    return sigma * states[0][0] % p, sigma * states[0][1] % p


def actual_projected(p: int, s: int, nu: int) -> tuple[int, int, tuple[int, ...]]:
    r, polynomial = item239.p_polynomial(p, s, nu, p)
    delta = r % 2
    return r, (r + 1) // 2, trim(polynomial[delta::2])


def verify_two_coordinate_relation(p: int, s: int) -> int:
    """Verify the exact P1/P0 companion-parity relation."""
    r, p0 = item239.p_polynomial(p, s, 0, p)
    _, p1 = item239.p_polynomial(p, s, 1, p)
    delta = r % 2
    f = item239.power_mod((1, -1), r, p)
    f = item239.convolution_mod(f, (1, 1), p)
    f = item239.convolution_mod(f, item239.power_mod((1, 0, 1), 2 * s - 1, p), p)
    selected = trim(f[delta::2])
    companion = trim(f[(1 - delta)::2])
    if not companion:
        raise AssertionError((p, s, r, "companion parity must be nonzero"))
    d0 = trim(p0[delta::2])
    d1 = trim(p1[delta::2])
    expected0 = poly_linear(selected, 1, p)
    first = poly_add(selected, poly_scale(poly_shift(selected, 1), 3, p), p)
    companion_factor = poly_add(poly_scale(companion, 3, p), poly_shift(companion, 1), p)
    expected1 = poly_add(first, poly_shift(companion_factor, 1 - delta), p)
    if d0 != expected0 or d1 != expected1:
        raise AssertionError((p, s, "two-coordinate relation"))
    return len(companion) - 1


def reciprocity_check(p: int, lower: int, polynomial: tuple[int, ...]) -> tuple[int, int]:
    """Verify the exact reflected-pole reciprocity relation."""
    degree = len(polynomial) - 1
    reflected_lower = -lower - degree - 1
    if (reflected_lower - lower) % p == 0:
        raise AssertionError((p, lower, degree, "reflected pole collision"))
    reversed_polynomial = tuple(reversed(polynomial))
    reversed_bulk, _ = functional_mod(p, lower, reversed_polynomial)
    reflected_bulk, reflected_sine = functional_mod(p, reflected_lower, polynomial)
    unweighted_alt = sum(
        ((-1) ** k) * pow((2 * (reflected_lower + k) + 1) % p, -1, p)
        for k in range(degree + 1)
    ) % p
    double_pole = sum(
        polynomial[k]
        * pow((2 * (reflected_lower + k) + 1) % p, -2, p)
        for k in range(degree + 1)
    ) % p
    expected = (double_pole - reflected_sine * unweighted_alt - reflected_bulk) % p
    if reversed_bulk != expected:
        raise AssertionError((p, lower, degree, "reciprocity relation"))
    self_sign = 0
    if reversed_polynomial == polynomial:
        self_sign = 1
    elif reversed_polynomial == tuple((-value) % p for value in polynomial):
        self_sign = -1
    if self_sign:
        original_bulk, _ = functional_mod(p, lower, polynomial)
        if self_sign * original_bulk % p != reversed_bulk:
            raise AssertionError((p, lower, degree, "self reciprocal sign"))
    return self_sign, reflected_lower % p


def exact_integer_projected(p: int, s: int, nu: int) -> tuple[int, tuple[int, ...]]:
    r = (p - 6 * s - 3) // 2
    a = 1 + 3 * nu
    q = 2 * s - nu
    polynomial = item239.item235.exact_power((1, -1), r)
    polynomial = item239.item235.exact_convolution(
        polynomial, item239.item235.exact_power((1, 1), a)
    )
    polynomial = item239.item235.exact_convolution(
        polynomial, item239.item235.exact_power((1, 0, 1), q)
    )
    return (r + 1) // 2, trim(polynomial[r % 2 :: 2])


def rational_replay(bound: int) -> dict[str, Any]:
    rows: list[tuple[int, ...]] = []
    zero_projections = 0
    nonempty_numerator_divisible = 0
    for p, s in item239.admissible_rows(bound):
        for nu in (0, 1):
            lower, polynomial = exact_integer_projected(p, s, nu)
            bulk, sine = functional_fraction(lower, polynomial)
            if bulk != bulk_pair_fraction(lower, polynomial):
                raise AssertionError((p, s, nu, "rational pair representation"))
            modular = item244.actual_coordinate(p, s, nu)
            reduced_bulk = (
                bulk.numerator % p * pow(bulk.denominator % p, -1, p) % p
            )
            reduced_sine = (
                sine.numerator % p * pow(sine.denominator % p, -1, p) % p
            )
            if reduced_bulk != modular["bulk_b_0"]:
                raise AssertionError((p, s, nu, "rational bulk reduction"))
            expected_sine = ((-1) ** lower) * modular["old_sine_endpoint"] % p
            if reduced_sine != expected_sine:
                raise AssertionError((p, s, nu, "rational sine reduction"))
            projection_zero = not polynomial
            zero_projections += projection_zero
            if not projection_zero:
                nonempty_numerator_divisible += bulk.numerator % p == 0
            rows.append(
                (
                    p,
                    s,
                    nu,
                    lower,
                    len(polynomial) - 1,
                    int(projection_zero),
                    bulk.numerator % p,
                    bulk.denominator % p,
                    reduced_bulk,
                )
            )
    return {
        "status": "EXACT FINITE RATIONAL REPLAY",
        "prime_max_inclusive": bound,
        "coordinate_count": len(rows),
        "zero_projection_count": zero_projections,
        "nonempty_moving_prime_numerator_divisibility_count": nonempty_numerator_divisible,
        "row_digest_sha256": row_digest(rows),
    }


def witness_rows() -> dict[str, Any]:
    lower_nonzero, polynomial_nonzero = exact_integer_projected(17, 2, 1)
    rational_nonzero, _ = functional_fraction(lower_nonzero, polynomial_nonzero)
    lower_zero, polynomial_zero = exact_integer_projected(37, 4, 0)
    rational_zero, _ = functional_fraction(lower_zero, polynomial_zero)
    if rational_nonzero == 0 or rational_zero == 0:
        raise AssertionError("rational witness must be nonzero")
    if rational_nonzero.numerator % 17 == 0 or rational_zero.numerator % 37:
        raise AssertionError("moving-prime witness divisibility")
    return {
        "nonzero_mod_p": {
            "p": 17,
            "s": 2,
            "nu": 1,
            "rational_numerator": str(rational_nonzero.numerator),
            "rational_denominator": str(rational_nonzero.denominator),
            "residue_mod_p": 9,
        },
        "zero_mod_p_nonzero_rational": {
            "p": 37,
            "s": 4,
            "nu": 0,
            "rational_numerator": str(rational_zero.numerator),
            "rational_denominator": str(rational_zero.denominator),
            "numerator_valuation_at_p": valuation(rational_zero.numerator, 37),
            "residue_mod_p": 0,
        },
    }


def finite_census(bound: int, operator_bound: int) -> dict[str, Any]:
    rows = 0
    coordinates = 0
    nonempty = 0
    bulk_zeros = 0
    self_reciprocal = 0
    reflected_collisions = 0
    operator_checks = 0
    companion_zero = 0
    simultaneous_nonempty_bulk_zeros = 0
    separate_bulk_zero_rows: list[dict[str, int]] = []
    digest_rows: list[tuple[int, ...]] = []
    for p, s in item239.admissible_rows(bound):
        rows += 1
        companion_degree = verify_two_coordinate_relation(p, s)
        companion_zero += companion_degree < 0
        row_nonempty_zero: list[bool] = []
        for nu in (0, 1):
            coordinates += 1
            r, lower, polynomial = actual_projected(p, s, nu)
            if not polynomial:
                row_nonempty_zero.append(False)
                digest_rows.append((p, s, nu, r, lower, -1, 0, 0, companion_degree))
                continue
            nonempty += 1
            bulk, sine = functional_mod(p, lower, polynomial)
            if bulk != bulk_pair_mod(p, lower, polynomial):
                raise AssertionError((p, s, nu, "pair representation"))
            data = item244.actual_coordinate(p, s, nu)
            if bulk != data["bulk_b_0"]:
                raise AssertionError((p, s, nu, "Item244 bulk"))
            bulk_zeros += bulk == 0
            row_nonempty_zero.append(bulk == 0)
            if bulk == 0:
                separate_bulk_zero_rows.append({"p": p, "s": s, "nu": nu})
            self_sign, reflected = reciprocity_check(p, lower, polynomial)
            self_reciprocal += self_sign != 0
            reflected_collisions += reflected == lower % p
            if p <= operator_bound:
                recurrence_bulk, recurrence_sine = row_functional_recurrence(p, s, nu)
                if recurrence_bulk != bulk or recurrence_sine != sine:
                    raise AssertionError((p, s, nu, "row-parameter recurrence"))
                operator_checks += 1
            digest_rows.append(
                (
                    p,
                    s,
                    nu,
                    r,
                    lower,
                    len(polynomial) - 1,
                    bulk,
                    sine,
                    companion_degree,
                    self_sign,
                    reflected,
                )
            )
        simultaneous_nonempty_bulk_zeros += all(row_nonempty_zero)
    return {
        "status": "EXACT FINITE ONLY",
        "prime_max_inclusive": bound,
        "operator_replay_prime_max_inclusive": operator_bound,
        "admissible_row_count": rows,
        "coordinate_count": coordinates,
        "nonempty_projection_count": nonempty,
        "bulk_zero_count_on_nonempty_projections": bulk_zeros,
        "separate_bulk_zero_rows": separate_bulk_zero_rows,
        "simultaneous_nonempty_bulk_zero_count": simultaneous_nonempty_bulk_zeros,
        "self_reciprocal_projection_count": self_reciprocal,
        "reflected_pole_collision_count": reflected_collisions,
        "operator_recurrence_check_count": operator_checks,
        "companion_parity_zero_count": companion_zero,
        "row_digest_sha256": row_digest(digest_rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=401)
    parser.add_argument("--operator-prime-max", type=int, default=101)
    parser.add_argument("--rational-prime-max", type=int, default=101)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if not (37 <= args.operator_prime_max <= args.prime_max):
        raise ValueError("require 37 <= operator-prime-max <= prime-max")
    if not (37 <= args.rational_prime_max <= args.prime_max):
        raise ValueError("require 37 <= rational-prime-max <= prime-max")

    finite = finite_census(args.prime_max, args.operator_prime_max)
    rational = rational_replay(args.rational_prime_max)
    witnesses = witness_rows()
    result = {
        "schema": "item246-j2-bulk-residual-structure-v1",
        "item": 246,
        "route": "Route 1A",
        "cell": "normalized common-log j=2 fixed cell, canonical Item244 bulk residual",
        "proved": {
            "coefficient_representation": "B_L[D]=sum_{0<=k<v<=D} (-1)^(v-k-1)d_v/((2(L+k)+1)(2(L+v)+1))",
            "double_integral": "B_L[D]=int_0^1 int_0^1 x^(2L)y^(2L)*(D(x^2 y^2)-D(-x^2))/(1+y^2) dx dy as an exact polynomial integral",
            "moving_prime_reduction": "for integer D and in-range denominators, B mod p vanishes iff p divides the numerator of the reduced rational B_L[D]",
            "factor_S": "S_L[(1+epsilon t)D]=S_L[D]-epsilon*S_(L+1)[D]",
            "factor_B": "B_L[(1+epsilon t)D]=B_L[D]+epsilon*(B_(L+1)[D]+S_(L+1)[D]/(2L+1))",
            "seed_recurrence": "E_(R+1,0)=E_(R,0)+t E_(R,1), E_(R+1,1)=E_(R,0)+E_(R,1), starting from (1,0)",
            "row_parameter_recurrence": "the factor and seed recurrences evaluate B_nu exactly from (L,b,q,R,delta) in Item244's factorization",
            "reciprocity": "if D*=t^D D(1/t) and Lvee=-L-D-1, then B_L[D*]=J_(Lvee)[D]-S_(Lvee)[D]A_(Lvee)-B_(Lvee)[D]",
            "distinct_reflected_pole": "0<2L+D+1<p, so Lvee is never congruent to L modulo p and reciprocity alone is not a scalar closure",
            "two_coordinate_relation": "writing F=P0/(1+z^2) with selected parity A and nonzero companion C, D0=(1+t)A and D1=(1+3t)A+t^(1-delta)(3+t)C",
            "baseline_common_factor": "D0 and D1 share (1-t)^min(r,1)*(1+t)^(2s-1), but the factor recurrence shifts L and does not factor this polynomial out of B as a scalar",
        },
        "exact_witnesses": witnesses,
        "finite_census": finite,
        "rational_replay": rational,
        "scoped_consequence": {
            "proved": "B_0 is a closed rational double-period functional with an exact finite row-parameter recurrence; reciprocity and the nu-pair both require an additional reflected-pole or companion-parity state",
            "nonvanishing_false": "an all-row B_0 nonvanishing theorem is false: the actual nonempty row (37,4,0) has B_0=0 modulo 37",
            "not_proved": "no Bezout eliminant, zero-rate theorem, or classification of moving-prime numerator divisibility is known",
        },
        "status_ledger": {
            "PROVED": [
                "the coefficient and exact polynomial double-integral representations",
                "the factor and parity-seed row-parameter recurrences",
                "the exact reflected-pole reciprocity identity and pole-separation theorem",
                "the two-coordinate companion-parity identity and nonzero-companion theorem",
                "the moving-prime numerator reformulation and exact zero/nonzero witnesses",
            ],
            "EXACT_FINITE": [
                "the bounded modular census, operator replay, and rational numerator replay",
            ],
            "OPEN": [
                "derive a larger-state eliminant using the reflected pole or companion parity",
                "classify primes dividing the exact rational numerator of B_0",
                "classify simultaneous j=2 common-log zeros",
                "obtain any Route-1 rate or capacity reduction",
            ],
        },
        "global_interface": "B_0 enters only Item239's stronger p^3 carry; Item246 does not strengthen the ordinary p^2 common-log gate",
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "none",
        },
        "dependencies": {
            "item244_checker": ITEM244_PATH.name,
            "item244_checker_sha256": ITEM244_SHA256,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
