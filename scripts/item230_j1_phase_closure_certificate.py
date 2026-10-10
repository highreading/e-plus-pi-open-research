#!/usr/bin/env python3
"""Deterministic exact certificate for Item 230.

This checker builds the one-prime affine transfer for Item 228's regularized
j=1 Pearson moments, verifies their coefficientwise 2p antiperiodicity and
4p periodicity, constructs the exact augmented-rank collision criterion, and
keeps all bounded computations explicitly finite.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item230_j1_phase_closure_certificate.json"


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


ITEM228_PATH = resolve("item228_j1_second_frobenius_certificate.py")
ITEM223_PATH = resolve("item223_j1_frobenius_transfer_certificate.py")
ITEM218_PATH = resolve("item218_j1_common_log_certificate.py")
item228 = load("item230_item228", ITEM228_PATH)
item223 = item228.item223
item218 = item223.item218


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    return [(left[j] + right[j]) % prime for j in range(len(left))]


def scale(value: list[int], scalar: int, prime: int) -> list[int]:
    return [scalar * entry % prime for entry in value]


def dot(left: list[int], right: list[int], prime: int) -> int:
    return sum(x * y for x, y in zip(left, right)) % prime


def mat_vec(matrix: list[list[int]], vector: list[int], prime: int) -> list[int]:
    return [dot(row, vector, prime) for row in matrix]


def mat_mul(
    left: list[list[int]], right: list[list[int]], prime: int
) -> list[list[int]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right))) % prime
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def matrix_add(
    left: list[list[int]], right: list[list[int]], prime: int
) -> list[list[int]]:
    return [
        [(left[i][j] + right[i][j]) % prime for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def determinant_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    determinant = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]), None
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * inverse % prime
            for j in range(column, len(work)):
                work[row][j] = (
                    work[row][j] - factor * work[column][j]
                ) % prime
    return determinant % prime


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((j for j in range(row, len(work)) if work[j][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, prime)
        work[row] = [entry * inverse % prime for entry in work[row]]
        for j in range(len(work)):
            if j != row and work[j][column]:
                factor = work[j][column]
                work[j] = [
                    (work[j][q] - factor * work[row][q]) % prime
                    for q in range(len(work[0]))
                ]
        row += 1
    return row


def normalized_phase_weight(prime: int, phase: int) -> int:
    """Return epsilon*ell_(phase*p-1), reduced modulo p."""
    epsilon = item228.epsilon_for(prime)
    return epsilon * item223.ell_numerator(phase * prime - 1, epsilon) % prime


def terminal_index(prime: int, s_value: int, phase: int) -> int:
    return 2 * s_value + 1 + (phase - 2) * prime


def common_line_terminal(prime: int, r_value: int, s_value: int) -> list[int]:
    terminal = 2 * s_value + 1
    values = {0: 1, 1: 1, 2: -1}
    for t_value in range(terminal):
        exact = item228.recurrence_coefficients(
            prime, r_value, s_value, t_value
        )
        pivot = -exact[3] % prime
        if not pivot:
            raise AssertionError((prime, r_value, s_value, t_value, "early pole"))
        lower = sum(exact[j] * values[t_value + j] for j in range(3))
        values[t_value + 3] = lower * pow(pivot, -1, prime) % prime
    return [values[terminal + j] for j in range(3)]


def one_phase_transfer(prime: int, r_value: int, s_value: int) -> dict[str, Any]:
    """Construct Y_(a+1)=M*Y_a+b*w_a for normalized phase weight w_a.

    Coordinates 0--2 are the input terminal state, coordinate 3 is the
    post-terminal free value, and coordinate 4 is a unit normalized source.
    """
    terminal = 2 * s_value + 1
    weight, sigma_weight = item228.weight_polynomials(r_value, s_value)
    sigma_degree = len(sigma_weight) - 1
    if sigma_degree >= prime:
        raise AssertionError((prime, r_value, s_value, "support too long"))

    dimension = 5
    values: dict[int, list[int]] = {}
    for j in range(3):
        values[terminal + j] = [int(k == j) for k in range(dimension)]
    values[terminal + 3] = [int(k == 3) for k in range(dimension)]

    for t_value in range(terminal + 1, terminal + prime):
        exact = item228.recurrence_coefficients(
            prime, r_value, s_value, t_value
        )
        pivot = -exact[3] % prime
        relative = t_value - terminal
        if pivot != relative % prime or not pivot:
            raise AssertionError(
                (prime, r_value, s_value, t_value, relative, "pivot", pivot)
            )
        lower = [0] * dimension
        for j in range(3):
            lower = add(lower, scale(values[t_value + j], exact[j], prime), prime)

        # In this open interval the only possible deleted derivative is
        # z^(a*p).  Its local coefficient is independent of a.  The regularized
        # right side is -coefficient*w_a, and A*u_(t+3)=lower-rhs.
        local_degree = sigma_degree - relative
        rhs_for_unit_weight = -item228.coefficient(sigma_weight, local_degree)
        lower[4] = (lower[4] - rhs_for_unit_weight) % prime
        values[t_value + 3] = scale(lower, pow(pivot, -1, prime), prime)

    output = [values[terminal + prime + j] for j in range(3)]
    matrix = [[output[row][column] for column in range(3)] for row in range(3)]
    free_column = [output[row][3] for row in range(3)]
    forcing = [output[row][4] for row in range(3)]

    # The free response is exactly W coefficientwise.  The output positions
    # p-3,p-2,p-1 are beyond its degree.
    free_start = terminal + 3
    for absolute in range(free_start, terminal + prime + 3):
        degree = absolute - free_start
        expected = item228.coefficient(weight, degree) % prime
        if values[absolute][3] != expected:
            raise AssertionError(
                (prime, r_value, s_value, degree, values[absolute][3], expected)
            )
    if free_column != [0, 0, 0]:
        raise AssertionError((prime, r_value, s_value, "free column", free_column))
    if any(matrix[row][0] for row in range(3)):
        raise AssertionError((prime, r_value, s_value, "forgotten coordinate", matrix))

    return {
        "M": matrix,
        "b": forcing,
        "free_column": free_column,
        "rank_M": rank_mod(matrix, prime),
        "terminal": terminal,
        "weight_degree": len(weight) - 1,
        "support_gap": prime - 3 - (len(weight) - 1),
    }


def terminal_row(prime: int, r_value: int, s_value: int) -> list[int]:
    terminal = 2 * s_value + 1
    return [
        (r_value + terminal + 1) % prime,
        -(2 * r_value + terminal + 2) % prime,
        (r_value + 4 * s_value + terminal + 1) % prime,
    ]


def phase_system(prime: int, r_value: int, s_value: int) -> dict[str, Any]:
    if prime != 2 * r_value + 6 * s_value + 3 or r_value < 2 or r_value % 2:
        raise ValueError((prime, r_value, s_value))
    epsilon = item228.epsilon_for(prime)
    transfer = one_phase_transfer(prime, r_value, s_value)
    matrix: list[list[int]] = transfer["M"]
    forcing: list[int] = transfer["b"]
    candidate = common_line_terminal(prime, r_value, s_value)
    row = terminal_row(prime, r_value, s_value)
    delta_plus, delta_minus = item223.transfer_mod(r_value, s_value, prime)
    if dot(row, candidate, prime) != delta_plus:
        raise AssertionError((prime, r_value, s_value, "Delta_plus mismatch"))

    weights = [normalized_phase_weight(prime, phase) for phase in range(2, 6)]
    expected_weights = [-4, 2, 4, -2]
    if weights != [entry % prime for entry in expected_weights]:
        raise AssertionError((prime, r_value, s_value, "phase weights", weights))
    for phase in range(2, 6):
        t_value = terminal_index(prime, s_value, phase)
        exact_pivot = prime + 2 * r_value + 4 * s_value + t_value + 2
        if exact_pivot != phase * prime:
            raise AssertionError(
                (prime, r_value, s_value, phase, exact_pivot, "multiplicity")
            )

    # Normalize Z_a=epsilon*Y_a and mu=epsilon*lambda.  The source cycle is
    # then (-4,2,4,-2), with Z_(a+2)=-Z_a.
    constant2 = [0, 0, 0]
    lambda2 = candidate
    constant3 = add(mat_vec(matrix, constant2, prime), scale(forcing, weights[0], prime), prime)
    lambda3 = mat_vec(matrix, lambda2, prime)

    coefficient_column = [
        delta_minus,
        delta_plus,
        dot(row, lambda3, prime),
    ]
    rhs_column = [
        -2 % prime,
        -4 % prime,
        (2 - dot(row, constant3, prime)) % prime,
    ]
    equation_names = ["bottom_p", "terminal_2p", "terminal_3p"]

    matrix2 = mat_mul(matrix, matrix, prime)
    anti_matrix = matrix_add(identity(3), matrix2, prime)
    anti_rhs = add(
        scale(mat_vec(matrix, forcing, prime), 4, prime),
        scale(forcing, -2, prime),
        prime,
    )
    anti_coefficient = mat_vec(anti_matrix, candidate, prime)
    for coordinate in range(3):
        coefficient_column.append(anti_coefficient[coordinate])
        rhs_column.append(anti_rhs[coordinate])
        equation_names.append(f"antiperiod_coordinate_{coordinate}")

    minors: list[dict[str, Any]] = []
    for i in range(len(coefficient_column)):
        for j in range(i + 1, len(coefficient_column)):
            value = (
                coefficient_column[i] * rhs_column[j]
                - coefficient_column[j] * rhs_column[i]
            ) % prime
            minors.append({"i": i, "j": j, "name": f"{equation_names[i]}__{equation_names[j]}", "value": value})

    coefficient_rank = int(any(coefficient_column))
    augmented_rank = rank_mod(
        [[coefficient_column[j], rhs_column[j]] for j in range(6)], prime
    )
    formally_solvable = coefficient_rank == augmented_rank == 1
    theta = (delta_plus - 2 * delta_minus) % prime
    if minors[0]["value"] != 2 * theta % prime:
        raise AssertionError((prime, r_value, s_value, "Theta minor"))

    anti_determinant = determinant_mod(anti_matrix, prime)
    return {
        "epsilon": epsilon,
        "M": matrix,
        "b": forcing,
        "terminal_row": row,
        "candidate_terminal_state": candidate,
        "normalized_weights_2_through_5": weights,
        "coefficient_column": coefficient_column,
        "rhs_column": rhs_column,
        "equation_names": equation_names,
        "minors": minors,
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "formally_solvable": formally_solvable,
        "theta": theta,
        "anti_matrix": anti_matrix,
        "anti_rhs": anti_rhs,
        "anti_determinant": anti_determinant,
        "rank_M": transfer["rank_M"],
        "support_gap": transfer["support_gap"],
    }


def regularized_moment_mod(
    prime: int,
    r_value: int,
    epsilon: int,
    shift: int,
    weight: list[int],
) -> int:
    base_exponent = prime + r_value + shift
    total = 0
    for degree, coefficient in enumerate(weight):
        denominator = base_exponent + degree + 1
        if denominator % prime == 0:
            continue
        total += (
            coefficient
            * item223.ell_numerator(base_exponent + degree, epsilon)
            * pow(denominator % prime, -1, prime)
        )
    return total % prime


def source_and_identity_replay(prime_max: int) -> dict[str, Any]:
    source_rows: list[tuple[int, ...]] = []
    state_rows: list[tuple[int, ...]] = []
    direct_moment_evaluations = 0
    unreduced_fraction_evaluations = 0

    for prime, _h_value, r_value, s_value in item228.actual_rows(prime_max):
        epsilon = item228.epsilon_for(prime)
        weight, sigma_weight = item228.weight_polynomials(r_value, s_value)
        system = phase_system(prime, r_value, s_value)
        matrix: list[list[int]] = system["M"]
        forcing: list[int] = system["b"]
        row: list[int] = system["terminal_row"]

        states: dict[int, list[int]] = {}
        for phase in range(2, 7):
            t_value = terminal_index(prime, s_value, phase)
            states[phase] = [
                regularized_moment_mod(
                    prime, r_value, epsilon, t_value + j, weight
                )
                for j in range(3)
            ]
            direct_moment_evaluations += 3

            exact_weight = item223.ell_numerator(phase * prime - 1, epsilon)
            if dot(row, states[phase], prime) != exact_weight % prime:
                raise AssertionError(
                    (prime, r_value, s_value, phase, "direct terminal")
                )

        for phase in range(2, 6):
            exact_weight = item223.ell_numerator(phase * prime - 1, epsilon)
            predicted = add(
                mat_vec(matrix, states[phase], prime),
                scale(forcing, exact_weight, prime),
                prime,
            )
            if predicted != states[phase + 1]:
                raise AssertionError(
                    (prime, r_value, s_value, phase, "direct one-phase transfer")
                )
        for phase in range(2, 5):
            if states[phase + 2] != scale(states[phase], -1, prime):
                raise AssertionError(
                    (prime, r_value, s_value, phase, "2p antiperiod")
                )
        if states[6] != states[2]:
            raise AssertionError((prime, r_value, s_value, "4p period"))

        for phase in range(2, 6):
            t_value = terminal_index(prime, s_value, phase)
            exact = item228.recurrence_coefficients(
                prime, r_value, s_value, t_value
            )
            if exact[3] != -phase * prime:
                raise AssertionError(
                    (prime, r_value, s_value, phase, "exact terminal pivot", exact[3])
                )
            moments = [
                item228.boundary_moment_from_weight(
                    prime, r_value, epsilon, t_value + j, weight
                )
                for j in range(4)
            ]
            unreduced_fraction_evaluations += 4
            lower = sum(exact[j] * moments[j] for j in range(3))
            pole_product = -exact[3] * moments[3]
            if lower != pole_product:
                raise AssertionError(
                    (prime, r_value, s_value, phase, "unreduced recurrence")
                )
            pole_residue = item223.fraction_mod(prime * moments[3], prime)
            ell_value = item223.ell_numerator(phase * prime - 1, epsilon)
            expected_residue = ell_value * pow(phase, -1, prime) % prime
            terminal_source = item223.fraction_mod(pole_product, prime)
            regularized_source = item228.regularized_rhs(
                prime, r_value, t_value, epsilon, sigma_weight
            )
            if (
                pole_residue != expected_residue
                or terminal_source != ell_value % prime
                or regularized_source != ell_value % prime
            ):
                raise AssertionError(
                    (
                        prime,
                        r_value,
                        s_value,
                        phase,
                        pole_residue,
                        expected_residue,
                        terminal_source,
                        regularized_source,
                    )
                )
            source_rows.append(
                (
                    prime,
                    r_value,
                    s_value,
                    phase,
                    ell_value,
                    pole_residue,
                    -exact[3],
                    terminal_source,
                )
            )

        # Match Item 228's second invariant with the corresponding normalized
        # augmented minor.  It differs by exactly the unit -epsilon.
        old = item228.second_transfer_components(prime, r_value, s_value)
        phase_minor = next(
            entry["value"]
            for entry in system["minors"]
            if entry["i"] == 1 and entry["j"] == 2
        )
        if phase_minor != (-epsilon * old["psi"]) % prime:
            raise AssertionError(
                (prime, r_value, s_value, phase_minor, old["psi"], epsilon)
            )
        state_rows.append(
            (
                prime,
                r_value,
                s_value,
                system["anti_determinant"],
                system["coefficient_rank"],
                system["augmented_rank"],
                phase_minor,
            )
        )

    return {
        "classification": "EXACT_REPLAY_OF_PROVED_IDENTITIES",
        "prime_max_inclusive": prime_max,
        "actual_rows": len(state_rows),
        "terminal_phases_per_row": [2, 3, 4, 5],
        "source_rows": len(source_rows),
        "direct_regularized_moment_evaluations": direct_moment_evaluations,
        "unreduced_fraction_moment_evaluations": unreduced_fraction_evaluations,
        "source_row_stream_sha256": row_digest(source_rows),
        "state_row_stream_sha256": row_digest(state_rows),
        "verified": [
            "the exact terminal multiplier is a*p before reduction for a=2,3,4,5",
            "p*u_(t_a+3)=ell_(a*p-1)/a before regularization",
            "multiplication by a*p gives terminal source ell_(a*p-1), with a cancelling exactly",
            "direct regularized coefficient sums obey every one-phase transfer",
            "direct regularized coefficient sums obey Y_(a+2)=-Y_a and Y_(a+4)=Y_a",
            "the terminal_2p__terminal_3p minor equals -epsilon times Item 228 Psi",
        ],
    }


def finite_census(prime_max: int) -> dict[str, Any]:
    counts = {
        "actual_rows": 0,
        "anti_determinant_nonzero": 0,
        "anti_determinant_zero": 0,
        "formally_solvable_six_equation_rows": 0,
        "item223_transfer_survivors": 0,
        "joint_item223_item228_survivors": 0,
        "direct_common_gate_zeros": 0,
    }
    determinant_zero_rows: list[tuple[int, ...]] = []
    formal_rows: list[tuple[int, ...]] = []
    minor_zero_rows: list[list[tuple[int, ...]]] = [[] for _ in range(15)]
    transcript: list[tuple[int, ...]] = []

    for prime, h_value, r_value, s_value in item228.actual_rows(prime_max):
        counts["actual_rows"] += 1
        system = phase_system(prime, r_value, s_value)
        determinant = system["anti_determinant"]
        counts["anti_determinant_nonzero"] += determinant != 0
        counts["anti_determinant_zero"] += determinant == 0
        if determinant == 0:
            determinant_zero_rows.append((prime, r_value, s_value))

        if system["formally_solvable"]:
            counts["formally_solvable_six_equation_rows"] += 1
            formal_rows.append((prime, r_value, s_value))

        delta_plus, delta_minus = item223.transfer_mod(r_value, s_value, prime)
        item223_survivor = (
            delta_plus != 0
            and delta_minus != 0
            and (delta_plus - 2 * delta_minus) % prime == 0
        )
        counts["item223_transfer_survivors"] += item223_survivor
        if item223_survivor:
            old = item228.second_transfer_components(prime, r_value, s_value)
            counts["joint_item223_item228_survivors"] += old["psi"] == 0

        q0, q1 = item218.candidate_conditions(prime, h_value, s_value)
        counts["direct_common_gate_zeros"] += q0 == q1 == 0

        minor_values = [entry["value"] for entry in system["minors"]]
        for index, value in enumerate(minor_values):
            if value == 0:
                minor_zero_rows[index].append((prime, r_value, s_value))
        transcript.append(
            (
                prime,
                r_value,
                s_value,
                determinant,
                system["coefficient_rank"],
                system["augmented_rank"],
                *minor_values,
                q0,
                q1,
            )
        )

    expected = {
        "actual_rows": 2435,
        "anti_determinant_nonzero": 2432,
        "anti_determinant_zero": 3,
        "formally_solvable_six_equation_rows": 0,
        "item223_transfer_survivors": 11,
        "joint_item223_item228_survivors": 0,
        "direct_common_gate_zeros": 0,
    }
    if prime_max == 601 and counts != expected:
        raise AssertionError((counts, expected))

    names = [entry["name"] for entry in phase_system(13, 2, 1)["minors"]]
    return {
        "classification": "EXACT_FINITE_ONLY",
        "prime_max_inclusive": prime_max,
        **counts,
        "anti_determinant_zero_rows": [list(row) for row in determinant_zero_rows],
        "formally_solvable_rows": [list(row) for row in formal_rows],
        "minor_zero_counts": {
            names[index]: len(minor_zero_rows[index]) for index in range(15)
        },
        "first_minor_zero_rows": {
            names[index]: [list(row) for row in minor_zero_rows[index][:8]]
            for index in range(15)
        },
        "full_row_transcript_sha256": row_digest(transcript),
        "scope_warning": "no finite count is extrapolated to an all-prime theorem, density bound, or logarithmic rate",
    }


def certificate(prime_max: int, source_prime_max: int) -> dict[str, Any]:
    source = source_and_identity_replay(source_prime_max)
    finite = finite_census(prime_max)
    return {
        "item": 230,
        "schema": "item230-j1-phase-closure-v1",
        "dependencies": {
            "item228_checker": ITEM228_PATH.name,
            "item228_checker_sha256": sha256(ITEM228_PATH),
            "item223_checker": ITEM223_PATH.name,
            "item223_checker_sha256": sha256(ITEM223_PATH),
            "item218_checker": ITEM218_PATH.name,
            "item218_checker_sha256": sha256(ITEM218_PATH),
        },
        "parameters": {
            "cell": "p=2r+6s+3, r=2h, h>=1, s>=1",
            "finite_prime_max_inclusive": prime_max,
            "source_replay_prime_max_inclusive": source_prime_max,
        },
        "phase_transfer_theorem": {
            "terminal_indices": "t_a=2s+1+(a-2)p, so the exact leading multiplier is A_(t_a)=a*p",
            "terminal_source": "ell_(a*p-1); in the unreduced pole p*u_(t_a+3)=ell_(a*p-1)/a and the factor a cancels exactly",
            "normalized_state": "Z_a=epsilon*Y_a and mu=epsilon*lambda",
            "normalized_source_cycle_a_2_to_5": [-4, 2, 4, -2],
            "one_phase_transfer": "Z_(a+1)=M*Z_a+b*w_a",
            "free_mode": "the post-terminal free mode has generating polynomial W=(1-z)^r(1+z^2)^(2s-1)",
            "free_mode_support": "deg W=r+4s-2<p-3, so its entire next-terminal column vanishes identically",
            "coefficientwise_antiperiod": "uhat_(t+2p)=-uhat_t mod p",
            "coefficientwise_period": "uhat_(t+4p)=uhat_t mod p",
            "exact_phase_period": "the terminal source has exact period four and antiperiod two for every p>=13",
        },
        "augmented_rank_theorem": {
            "equations": [
                "Delta_minus*mu=-2",
                "Delta_plus*mu=-4",
                "a*(M*v)*mu=2-a*(-4*b)",
                "the three coordinates of (I+M^2)*v*mu=4*M*b-2*b",
            ],
            "number_of_scalar_equations": 6,
            "number_of_augmented_2_by_2_minors": 15,
            "criterion": "formal solvability iff rank([c|d])=rank(c)=1, equivalently some c_i is nonzero and all 15 minors c_i*d_j-c_j*d_i vanish",
            "item223_relation": "the bottom__terminal_2p minor is 2*(Delta_plus-2*Delta_minus)",
            "item228_relation": "the terminal_2p__terminal_3p minor is -epsilon*Psi",
            "necessity": "every original common-log collision satisfies the six-equation system",
            "regular_completeness": "if det(I+M^2) is nonzero, formal solvability is equivalent to the original common-log collision",
            "singular_scope": "if det(I+M^2)=0, the six-equation system remains necessary but sufficiency is not claimed",
        },
        "source_and_identity_replay": source,
        "finite_census": finite,
        "rate_ledger": {
            "j1_cell_mass_per_m_if_fully_excluded": "1/6",
            "full_cell_exclusion": "OPEN",
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "reason": "no all-prime augmented-minor inconsistency or zero-rate theorem is proved",
        },
        "status_ledger": {
            "PROVED": [
                "the exact a*p terminal multiplier and ell_(a*p-1) source with the factor a retained and cancelled",
                "the fixed one-phase affine transfer and exact vanishing of every post-terminal free column at the next phase",
                "coefficientwise 2p antiperiodicity and 4p periodicity",
                "the six-equation augmented-rank necessary criterion",
                "regular-row equivalence when det(I+M^2) is nonzero",
            ],
            "EXACT_FINITE": [
                "the direct source and coefficientwise identity replay through the declared source bound",
                "the determinant and augmented-rank census through the declared finite bound",
            ],
            "OPEN": [
                "all-prime inconsistency of the six-equation system",
                "classification or zero-rate control of det(I+M^2)=0 rows",
                "any positive Route-1 rate or radical saving from the j=1 cell",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=601)
    parser.add_argument("--source-prime-max", type=int, default=151)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.prime_max < 151 or not (13 <= args.source_prime_max <= args.prime_max):
        raise ValueError("require prime-max>=151 and 13<=source-prime-max<=prime-max")
    result = certificate(args.prime_max, args.source_prime_max)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "source_rows": result["source_and_identity_replay"]["actual_rows"],
                "finite_rows": result["finite_census"]["actual_rows"],
                "anti_determinant_zero": result["finite_census"]["anti_determinant_zero"],
                "formally_solvable": result["finite_census"]["formally_solvable_six_equation_rows"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
