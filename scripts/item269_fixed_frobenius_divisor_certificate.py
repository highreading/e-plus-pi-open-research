#!/usr/bin/env python3
"""Deterministic certificate for Item 269's fixed-divisor admission test.

The checker performs exact rational and finite-field identity checks only.
It does not search for exceptional collision primes and does not infer a
density statement from any bounded range.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def v_p_integer(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero")
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def v_p_fraction(value: Fraction, prime: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero")
    return v_p_integer(value.numerator, prime) - v_p_integer(value.denominator, prime)


def odd_double_factorial(length: int) -> int:
    result = 1
    for index in range(length):
        result *= 2 * index + 1
    return result


def phase_parameters(phase: int, delta: int) -> tuple[int, int, int, int]:
    if phase == 5:
        return 5, 4, -1, 3 * delta
    if phase == 1:
        return 1, 2, 1, 3 * delta - 2
    raise ValueError("phase must be 1 or 5")


def boundary_slope(phase: int, delta: int) -> dict[str, object]:
    numerator_shift, denominator_shift, pochhammer_shift, length = phase_parameters(
        phase, delta
    )
    coefficient = Fraction(1)
    prefix = Fraction(0)
    for index in range(delta):
        prefix += coefficient
        coefficient *= Fraction(
            6 * index + numerator_shift, 3 * index + denominator_shift
        )

    terms: list[Fraction] = []
    numerator_product = 1
    denominator_product = 1
    for index in range(length):
        numerator_product *= 3 * index - 3 * delta + pochhammer_shift
        denominator_product *= 3 * (2 * index + 1)
        terms.append(Fraction(numerator_product, denominator_product))
    tail = sum(terms, Fraction(0))
    slope = prefix + coefficient * tail
    expected_valuation = -length - v_p_integer(odd_double_factorial(length), 3)
    return {
        "phase": phase,
        "delta": delta,
        "length": length,
        "c_delta": coefficient,
        "K_delta": prefix,
        "Pi_delta": tail,
        "D_delta": slope,
        "term_valuations": [v_p_fraction(term, 3) for term in terms],
        "expected_valuation": expected_valuation,
    }


def check_slope_valuations(max_delta: int) -> dict[str, object]:
    records: list[dict[str, object]] = []
    comparisons = 0
    term_checks = 0
    for phase, start in ((5, 1), (1, 3)):
        previous_valuation: int | None = None
        for delta in range(start, max_delta + 1, 2):
            data = boundary_slope(phase, delta)
            coefficient = data["c_delta"]
            prefix = data["K_delta"]
            slope = data["D_delta"]
            valuations = data["term_valuations"]
            expected = data["expected_valuation"]
            assert isinstance(coefficient, Fraction)
            assert isinstance(prefix, Fraction)
            assert isinstance(slope, Fraction)
            assert isinstance(valuations, list)
            assert isinstance(expected, int)
            assert v_p_fraction(coefficient, 3) == 0
            assert v_p_fraction(prefix, 3) >= 0
            assert valuations == sorted(valuations, reverse=True)
            assert all(
                valuations[index + 1] < valuations[index]
                for index in range(len(valuations) - 1)
            )
            assert valuations[-1] == expected
            assert v_p_fraction(slope, 3) == expected
            assert v_p_integer(slope.denominator, 3) == -expected
            assert v_p_integer(slope.numerator, 3) == 0
            if previous_valuation is not None:
                assert expected < previous_valuation
                comparisons += 1
            previous_valuation = expected
            term_checks += len(valuations)
            if delta <= 7:
                records.append(
                    {
                        "phase": phase,
                        "delta": delta,
                        "length": data["length"],
                        "D_delta": str(slope),
                        "v3_D_delta": expected,
                        "reduced_numerator_v3": 0,
                        "reduced_denominator_v3": -expected,
                    }
                )
    return {
        "max_actual_odd_delta": max_delta,
        "sample_records": records,
        "strict_distinctness_comparisons": comparisons,
        "individual_tail_term_valuation_checks": term_checks,
        "formula": {
            "phase_5": "v3(D_delta)=-3*delta-v3((6*delta-1)!!)",
            "phase_1": "v3(D_delta)=-(3*delta-2)-v3((6*delta-5)!!)",
        },
    }


def inv(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def matrix_identity(size: int) -> list[list[int]]:
    return [[int(row == column) for column in range(size)] for row in range(size)]


def matrix_multiply(
    left: list[list[int]], right: list[list[int]], prime: int
) -> list[list[int]]:
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    assert len(left[0]) == inner
    return [
        [
            sum(left[row][index] * right[index][column] for index in range(inner))
            % prime
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def matrix_inverse(matrix: list[list[int]], prime: int) -> list[list[int]]:
    size = len(matrix)
    augmented = [
        [entry % prime for entry in matrix[row]] + matrix_identity(size)[row]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column] % prime)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = inv(augmented[column][column], prime)
        augmented[column] = [(entry * scale) % prime for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column] % prime
            if factor:
                augmented[row] = [
                    (augmented[row][index] - factor * augmented[column][index]) % prime
                    for index in range(2 * size)
                ]
    return [row[size:] for row in augmented]


def p5_cartier_matrix(prime: int, epsilon: int, H: int, h: int) -> list[list[int]]:
    matrix = [[0] * 5 for _ in range(5)]
    matrix[1][0] = epsilon % prime
    matrix[0][1] = epsilon % prime
    matrix[3][1] = H % prime
    matrix[2][2] = epsilon % prime
    matrix[3][4] = -h % prime
    return matrix


def p5_change_of_frame(prime: int, epsilon: int, H: int, h: int) -> list[list[int]]:
    change = matrix_identity(5)
    change[3][0] = H * inv(epsilon, prime) % prime
    change[4][4] = -inv(h, prime) % prime
    return change


def p1_cartier_matrix(prime: int, epsilon: int, H: int, h: int) -> list[list[int]]:
    matrix = [[0] * 5 for _ in range(5)]
    matrix[0][0] = epsilon % prime
    matrix[3][0] = (H - h) % prime
    matrix[1][1] = epsilon % prime
    matrix[2][2] = epsilon % prime
    matrix[3][3] = h % prime
    return matrix


def p1_change_of_frame(prime: int, epsilon: int, H: int, h: int) -> list[list[int]]:
    change = matrix_identity(5)
    lam = (H - h) % prime
    change[3][0] = -lam * inv(h - epsilon, prime) % prime
    return change


def primes_through(limit: int) -> list[int]:
    result = []
    for value in range(5, limit + 1):
        if all(value % divisor for divisor in range(2, int(value**0.5) + 1)):
            result.append(value)
    return result


def check_conjugacy_no_go(prime_limit: int) -> dict[str, object]:
    p5_checks = 0
    p1_checks = 0
    gate_separations = 0
    for prime in primes_through(prime_limit):
        epsilon = 1 if pow(2, (prime - 1) // 2, prime) == 1 else -1
        epsilon_mod = epsilon % prime
        sample_H = sorted({0, 1, 2, prime // 2, prime - 1})
        sample_h = sorted({1, 2, prime // 2, prime - 1})
        if prime % 6 == 5:
            canonical = p5_cartier_matrix(prime, epsilon_mod, 0, 1)
            canonical_change = p5_change_of_frame(prime, epsilon_mod, 0, 1)
            canonical_normal = matrix_multiply(
                matrix_multiply(matrix_inverse(canonical_change, prime), canonical, prime),
                canonical_change,
                prime,
            )
            for H in sample_H:
                for h in sample_h:
                    matrix = p5_cartier_matrix(prime, epsilon_mod, H, h)
                    change = p5_change_of_frame(prime, epsilon_mod, H, h)
                    normal = matrix_multiply(
                        matrix_multiply(matrix_inverse(change, prime), matrix, prime),
                        change,
                        prime,
                    )
                    assert normal == canonical_normal
                    p5_checks += 1
            D = 3 % prime
            h = 1
            H_zero = (D * h + epsilon_mod) % prime
            H_nonzero = (H_zero + 1) % prime
            assert (H_zero - D * h - epsilon_mod) % prime == 0
            assert (H_nonzero - D * h - epsilon_mod) % prime != 0
            for H in (H_zero, H_nonzero):
                matrix = p5_cartier_matrix(prime, epsilon_mod, H, h)
                change = p5_change_of_frame(prime, epsilon_mod, H, h)
                normal = matrix_multiply(
                    matrix_multiply(matrix_inverse(change, prime), matrix, prime),
                    change,
                    prime,
                )
                assert normal == canonical_normal
            gate_separations += 1
        elif prime % 6 == 1:
            for h in sample_h:
                if h % prime == epsilon_mod:
                    continue
                canonical = p1_cartier_matrix(prime, epsilon_mod, h, h)
                for H in sample_H:
                    matrix = p1_cartier_matrix(prime, epsilon_mod, H, h)
                    change = p1_change_of_frame(prime, epsilon_mod, H, h)
                    normal = matrix_multiply(
                        matrix_multiply(matrix_inverse(change, prime), matrix, prime),
                        change,
                        prime,
                    )
                    assert normal == canonical
                    p1_checks += 1
            D = 3 % prime
            h = next(value for value in range(1, prime) if value != epsilon_mod)
            H_zero = (D * h + epsilon_mod) % prime
            H_nonzero = (H_zero + 1) % prime
            assert (H_zero - D * h - epsilon_mod) % prime == 0
            assert (H_nonzero - D * h - epsilon_mod) % prime != 0
            for H in (H_zero, H_nonzero):
                matrix = p1_cartier_matrix(prime, epsilon_mod, H, h)
                change = p1_change_of_frame(prime, epsilon_mod, H, h)
                normal = matrix_multiply(
                    matrix_multiply(matrix_inverse(change, prime), matrix, prime),
                    change,
                    prime,
                )
                assert normal == p1_cartier_matrix(prime, epsilon_mod, h, h)
            gate_separations += 1
    return {
        "prime_limit": prime_limit,
        "p5_normal_form_checks": p5_checks,
        "p1_nonresonant_normal_form_checks": p1_checks,
        "same_conjugacy_class_gate_separations": gate_separations,
        "scope": "bounded exact matrix identities only; no Frobenius-density inference",
    }


def full_gate_rows(
    phase: int,
    delta: int,
    epsilon: int,
    parity: int,
    B: Fraction,
    kappa: Fraction,
    tau: Fraction,
    f_values: tuple[Fraction, Fraction],
    U_values: tuple[Fraction, Fraction],
) -> list[list[Fraction]]:
    slope = boundary_slope(phase, delta)["D_delta"]
    assert isinstance(slope, Fraction)
    sign = -1 if parity else 1
    alpha = Fraction(9, 2) * kappa
    z_row = [
        B * (-alpha * sign - tau),
        B * alpha * sign * epsilon,
        -B * alpha * sign * epsilon * slope,
    ]
    return [
        [
            f_values[index] * z_row[0] + U_values[index],
            f_values[index] * z_row[1],
            f_values[index] * z_row[2],
        ]
        for index in range(2)
    ]


def check_universal_incidence() -> dict[str, object]:
    checks = 0
    sample_rows = []
    for phase, start in ((5, 1), (1, 3)):
        for offset, delta in enumerate(range(start, start + 6, 2)):
            epsilon = -1 if offset % 2 else 1
            parity = offset % 2
            B = Fraction(delta + 2, 2 * delta + 3)
            kappa = Fraction(2 * delta + 1, delta + 4)
            tau = Fraction((-1) ** delta * (delta + 1), 3 * delta + 2)
            f_values = (Fraction(delta + 1), Fraction(2 - delta, delta + 2))
            U_values = (Fraction(3, delta + 1), Fraction(delta - 1, 2 * delta + 1))
            H = Fraction(5 * delta + 1, delta + 3)
            h = Fraction(delta + 2, 2 * delta + 5)
            slope = boundary_slope(phase, delta)["D_delta"]
            assert isinstance(slope, Fraction)
            sign = -1 if parity else 1
            A = sign * (epsilon * (H - slope * h) - 1)
            Z = B * (Fraction(9, 2) * kappa * A - tau)
            direct = [f_values[index] * Z + U_values[index] for index in range(2)]
            row_matrix = full_gate_rows(
                phase,
                delta,
                epsilon,
                parity,
                B,
                kappa,
                tau,
                f_values,
                U_values,
            )
            vector = [Fraction(1), H, h]
            incidence = [sum(row[i] * vector[i] for i in range(3)) for row in row_matrix]
            assert incidence == direct
            checks += 2
            if offset == 0:
                sample_rows.append(
                    {
                        "phase": phase,
                        "delta": delta,
                        "matrix": [[str(entry) for entry in row] for row in row_matrix],
                        "state": [str(entry) for entry in vector],
                        "gate": [str(entry) for entry in direct],
                    }
                )
    return {
        "bilinear_incidence_identity_checks": checks,
        "sample_rows": sample_rows,
        "fixed_incidence": "I={(R,x) in Mat_(2x3) x A^3: R*x=0, x_0=1}",
        "admission_warning": "R_(r,s) is external moving row data, not Frobenius of the sealed fixed motive",
    }


def half_binomial_prefix(prime: int, cutoff: int) -> int:
    return sum(
        comb(2 * index, index) * inv(pow(8, index, prime), prime)
        for index in range(cutoff + 1)
    ) % prime


def check_same_prime_row_dependence() -> dict[str, object]:
    prime = 47
    rows = []
    for delta in (1, 3, 5, 7):
        r = 3 * delta - 2
        s = (prime - 2 * r - 3) // 6
        cutoff = s - 1
        rows.append(
            {
                "delta": delta,
                "r": r,
                "s": s,
                "cutoff": cutoff,
                "H_cutoff_mod_p": half_binomial_prefix(prime, cutoff),
            }
        )
    assert [row["H_cutoff_mod_p"] for row in rows] == [33, 0, 41, 1]
    return {
        "role": "exact factor-through-prime obstruction inherited from the known p=47 row; not an exceptional-prime search",
        "prime": prime,
        "rows": rows,
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def build_result(max_delta: int, prime_limit: int) -> dict[str, object]:
    return {
        "schema": "item269-fixed-frobenius-divisor-certificate-v1",
        "strict_labels": {
            "slope_valuation_and_distinctness": "PROVED",
            "algebraic_correspondence_obstruction": "PROVED IN THE STATED ALGEBRAIC-SECTION SCOPE",
            "conjugacy_stable_fixed_divisor": "PROVED NO-GO FOR THE SEALED CARTIER REALIZATION",
            "universal_incidence": "EXACT POSITIVE RECOGNITION, BUT NOT LARGE-SIEVE ADMISSIBLE BY ITSELF",
            "bounded_checks": "EXACT FINITE ONLY",
            "exceptional_zero_search": "NONE",
            "positive_linear_capacity_admission": "FAIL",
            "booking": "zero new Route-1 rate and zero ordinary-j=2 capacity reduction",
        },
        "valuation": check_slope_valuations(max_delta),
        "conjugacy": check_conjugacy_no_go(prime_limit),
        "universal_incidence": check_universal_incidence(),
        "same_prime_row_dependence": check_same_prime_row_dependence(),
        "proved_symbolic_lemmas": [
            "The unique lowest 3-adic tail term gives the exact reduced valuation of D_delta.",
            "Strictly decreasing v3(D_delta) makes all actual slopes pairwise distinct.",
            "A fixed P(delta,Y) over Q would bound the rational-root height by O(log delta), contradicting -v3(D_delta)>=3 delta.",
            "A conjugacy-stable divisor cannot distinguish coefficients erased by the exact Cartier normal forms.",
            "The full two-coordinate affine gate is exactly the fixed bilinear incidence R_(r,s)*(1,H_q,h_q)^T=0.",
        ],
        "open": [
            "a new bounded-conductor sheaf or dynamical realization whose Frobenius data encodes the moving row matrix R_(r,s)",
            "nontrivial geometric monodromy and a conjugacy-stable proper collision divisor for the actual (p,r) family",
            "any weighted zero-density theorem for the moving full gate",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--max-delta", type=int, default=31)
    parser.add_argument("--prime-limit", type=int, default=97)
    args = parser.parse_args()
    if args.max_delta < 7 or args.max_delta % 2 == 0:
        raise SystemExit("--max-delta must be odd and at least 7")
    result = build_result(args.max_delta, args.prime_limit)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    output.write_text(encoded, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
