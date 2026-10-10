#!/usr/bin/env python3
"""Deterministic certificate for Item 233.

Starting from frozen Item 230, this checker replays the three-endpoint
phase model, the exact closed form for det(I+M^2), its rank/singular
classification, and the coefficientwise redundancy of the antiperiod
coordinates.  All bounded enumerations are labelled finite in the output.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item233_j1_antiperiod_determinant_certificate.json"


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


ITEM230_PATH = resolve("item230_j1_phase_closure_certificate.py")
item230 = load("item233_item230", ITEM230_PATH)
item228 = item230.item228
item223 = item230.item223


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def mat_add(
    left: list[list[int]], right: list[list[int]], prime: int
) -> list[list[int]]:
    return [
        [(left[i][j] + right[i][j]) % prime for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def mat_sub(
    left: list[list[int]], right: list[list[int]], prime: int
) -> list[list[int]]:
    return [
        [(left[i][j] - right[i][j]) % prime for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def row_mat(row: list[int], matrix: list[list[int]], prime: int) -> list[int]:
    return [
        sum(row[k] * matrix[k][j] for k in range(len(row))) % prime
        for j in range(len(matrix[0]))
    ]


def matrix_power(
    matrix: list[list[int]], exponent: int, prime: int
) -> list[list[int]]:
    result = item230.identity(len(matrix))
    base = matrix
    while exponent:
        if exponent & 1:
            result = item230.mat_mul(result, base, prime)
        base = item230.mat_mul(base, base, prime)
        exponent //= 2
    return result


def inverse_matrix(matrix: list[list[int]], prime: int) -> list[list[int]]:
    size = len(matrix)
    work = [
        [matrix[i][j] % prime for j in range(size)]
        + [int(i == j) for j in range(size)]
        for i in range(size)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot is None:
            raise ZeroDivisionError("singular matrix")
        work[column], work[pivot] = work[pivot], work[column]
        inverse = pow(work[column][column], -1, prime)
        work[column] = [entry * inverse % prime for entry in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (work[row][j] - factor * work[column][j]) % prime
                for j in range(2 * size)
            ]
    return [row[size:] for row in work]


def solve_square(
    matrix: list[list[int]], rhs: list[int], prime: int
) -> list[int]:
    return item230.mat_vec(inverse_matrix(matrix, prime), rhs, prime)


def phase_basis() -> list[list[int]]:
    """Integer bases for the endpoint modes 1, i+(-i), and i-(-i)."""
    return [
        [1, 1, 1, 1],
        [1, 0, -1, 0],
        [0, 1, 0, -1],
    ]


def phase_shift_matrix(prime: int) -> list[list[int]]:
    epsilon = 1 if prime % 4 == 1 else -1
    return [
        [1, 0, 0],
        [0, 0, epsilon % prime],
        [0, (-epsilon) % prime, 0],
    ]


def generalized_moment(
    prime: int,
    r_value: int,
    shift: int,
    polynomial: list[int],
    phase_weight: list[int],
) -> int:
    total = 0
    for degree, coefficient in enumerate(polynomial):
        denominator = prime + r_value + shift + degree + 1
        if denominator % prime == 0:
            continue
        total += (
            coefficient
            * phase_weight[denominator % 4]
            * pow(denominator % prime, -1, prime)
        )
    return total % prime


def endpoint_matrix(
    prime: int, r_value: int, s_value: int
) -> tuple[list[list[int]], list[int]]:
    polynomial, _sigma_polynomial = item228.weight_polynomials(r_value, s_value)
    terminal = 2 * s_value + 1
    columns = [
        [
            generalized_moment(
                prime, r_value, terminal + coordinate, polynomial, weight
            )
            for coordinate in range(3)
        ]
        for weight in phase_basis()
    ]
    return transpose(columns), polynomial


def endpoint_replay(
    prime: int,
    r_value: int,
    s_value: int,
    system: dict[str, Any],
) -> tuple[int, ...]:
    matrix: list[list[int]] = system["M"]
    forcing: list[int] = system["b"]
    terminal_row: list[int] = system["terminal_row"]
    terminal = 2 * s_value + 1
    phi, polynomial = endpoint_matrix(prime, r_value, s_value)
    det_phi = item230.determinant_mod(phi, prime)
    if not det_phi:
        raise AssertionError((prime, r_value, s_value, "endpoint matrix"))

    feedback = [
        [forcing[i] * terminal_row[j] % prime for j in range(3)]
        for i in range(3)
    ]
    n_matrix = mat_add(matrix, feedback, prime)
    shift_matrix = phase_shift_matrix(prime)
    closed_n = item230.mat_mul(
        item230.mat_mul(phi, shift_matrix, prime),
        inverse_matrix(phi, prime),
        prime,
    )
    if closed_n != n_matrix:
        raise AssertionError((prime, r_value, s_value, "closed N"))

    for column, weight in enumerate(phase_basis()):
        state = [phi[row][column] for row in range(3)]
        terminal_weight = weight[(2 * prime) % 4] % prime
        if item230.dot(terminal_row, state, prime) != terminal_weight:
            raise AssertionError((prime, r_value, s_value, column, "terminal"))
        shifted_weight = [weight[(residue + prime) % 4] for residue in range(4)]
        next_state = [
            generalized_moment(
                prime,
                r_value,
                terminal + prime + coordinate,
                polynomial,
                weight,
            )
            for coordinate in range(3)
        ]
        shifted_state = [
            generalized_moment(
                prime,
                r_value,
                terminal + coordinate,
                polynomial,
                shifted_weight,
            )
            for coordinate in range(3)
        ]
        predicted = item230.add(
            item230.mat_vec(matrix, state, prime),
            item230.scale(forcing, terminal_weight, prime),
            prime,
        )
        if next_state != shifted_state or next_state != predicted:
            raise AssertionError((prime, r_value, s_value, column, "transfer"))

    a0 = terminal_row[0]
    if not a0:
        raise AssertionError((prime, r_value, s_value, "a0"))
    closed_b = item230.scale(
        item230.mat_vec(n_matrix, [1, 0, 0], prime), pow(a0, -1, prime), prime
    )
    if closed_b != forcing:
        raise AssertionError((prime, r_value, s_value, "closed b"))

    inverse_phi = inverse_matrix(phi, prime)
    adjugate_e0 = item230.scale(
        item230.mat_vec(inverse_phi, [1, 0, 0], prime), det_phi, prime
    )
    shifted_once = item230.mat_vec(shift_matrix, adjugate_e0, prime)
    shifted_twice = item230.mat_vec(
        matrix_power(shift_matrix, 2, prime), adjugate_e0, prime
    )
    r1 = item230.dot(
        terminal_row, item230.mat_vec(phi, shifted_once, prime), prime
    )
    r2 = item230.dot(
        terminal_row, item230.mat_vec(phi, shifted_twice, prime), prime
    )
    closed_numerator = (
        (r1 - r2) ** 2 + (a0 * det_phi - r1) ** 2
    ) % prime
    anti_determinant = int(system["anti_determinant"])
    if closed_numerator != anti_determinant * (a0 * det_phi) ** 2 % prime:
        raise AssertionError((prime, r_value, s_value, "closed numerator"))
    return (
        prime,
        r_value,
        s_value,
        det_phi,
        r1,
        r2,
        closed_numerator,
        anti_determinant,
    )


def control_data(
    prime: int,
    r_value: int,
    s_value: int,
    system: dict[str, Any],
) -> dict[str, Any]:
    matrix: list[list[int]] = system["M"]
    forcing: list[int] = system["b"]
    terminal_row: list[int] = system["terminal_row"]
    candidate: list[int] = system["candidate_terminal_state"]
    if any(matrix[row][0] for row in range(3)):
        raise AssertionError((prime, r_value, s_value, "first column"))

    feedback = [
        [forcing[i] * terminal_row[j] % prime for j in range(3)]
        for i in range(3)
    ]
    n_matrix = mat_add(matrix, feedback, prime)
    powers = [matrix_power(n_matrix, q, prime) for q in range(5)]
    identity = item230.identity(3)
    expected_n3 = mat_add(
        mat_sub(powers[2], powers[1], prime), identity, prime
    )
    if powers[3] != expected_n3 or powers[4] != identity:
        raise AssertionError((prime, r_value, s_value, "phase polynomial"))
    if (
        sum(n_matrix[j][j] for j in range(3)) % prime != 1
        or sum(powers[2][j][j] for j in range(3)) % prime != prime - 1
        or item230.determinant_mod(n_matrix, prime) != 1
    ):
        raise AssertionError((prime, r_value, s_value, "characteristic data"))

    observability = [row_mat(terminal_row, powers[q], prime) for q in range(3)]
    det_observability = item230.determinant_mod(observability, prime)
    if not det_observability:
        raise AssertionError((prime, r_value, s_value, "observability"))

    control_columns = [item230.mat_vec(powers[q], forcing, prime) for q in range(4)]
    h = [item230.dot(terminal_row, column, prime) for column in control_columns]
    h0, h1, h2, h3 = h
    if h3 != 1 or h2 != (1 + h1 - h0) % prime:
        raise AssertionError((prime, r_value, s_value, "feedback sequence", h))

    a0 = terminal_row[0]
    if not 0 < a0 < prime:
        raise AssertionError((prime, r_value, s_value, "a0 range", a0))
    if item230.scale(
        item230.mat_vec(n_matrix, [1, 0, 0], prime), pow(a0, -1, prime), prime
    ) != forcing:
        raise AssertionError((prime, r_value, s_value, "forcing formula"))

    block = [row[1:] for row in matrix[1:]]
    trace_block = (block[0][0] + block[1][1]) % prime
    determinant_block = item230.determinant_mod(block, prime)
    if trace_block != (1 - h0) % prime:
        raise AssertionError((prime, r_value, s_value, "trace B"))
    if determinant_block != (1 + h1 - h0) % prime:
        raise AssertionError((prime, r_value, s_value, "det B"))

    x_value = (h0 - h1) % prime
    y_value = (1 - h0) % prime
    closed_determinant = (x_value * x_value + y_value * y_value) % prime
    if closed_determinant != int(system["anti_determinant"]):
        raise AssertionError((prime, r_value, s_value, "anti determinant"))
    anti_matrix: list[list[int]] = system["anti_matrix"]
    rank_anti = item230.rank_mod(anti_matrix, prime)
    expected_rank = 3 if closed_determinant else (1 if not x_value and not y_value else 2)
    if rank_anti != expected_rank:
        raise AssertionError((prime, r_value, s_value, "anti rank"))

    if prime % 4 != (1 if s_value % 2 else 3):
        raise AssertionError((prime, r_value, s_value, "phase parity"))
    if not closed_determinant and prime % 4 == 3 and (x_value or y_value):
        raise AssertionError((prime, r_value, s_value, "nonsquare split"))

    # Every singular affine closure is consistent.  The check is made on
    # every row, not merely the three finite singular examples.
    anti_rhs: list[int] = system["anti_rhs"]
    augmented = [anti_matrix[row] + [anti_rhs[row]] for row in range(3)]
    if item230.rank_mod(augmented, prime) != rank_anti:
        raise AssertionError((prime, r_value, s_value, "affine consistency"))

    # Candidate terminal sequence.  Its fourth entry is the lower terminal,
    # and the missing -1 Fourier mode is the order-three recurrence.
    terminal_values = [
        item230.dot(terminal_row, item230.mat_vec(powers[q], candidate, prime), prime)
        for q in range(4)
    ]
    delta_plus, delta_minus = item223.transfer_mod(r_value, s_value, prime)
    if terminal_values[0] != delta_plus or terminal_values[3] != delta_minus:
        raise AssertionError((prime, r_value, s_value, "bottom reciprocity"))
    if (
        terminal_values[0]
        - terminal_values[1]
        + terminal_values[2]
        - terminal_values[3]
    ) % prime:
        raise AssertionError((prime, r_value, s_value, "minus-one mode"))

    # Exact coordinatewise redundancy.  With e0,e1,e3 the phase-2,
    # phase-3, and bottom terminal residuals, closure residual R is
    #   R=(h0*b-N*b)e0+(c-b)e1+c*e3,
    # where O*c=(1,1,1)^t.  Checking two scalar values would suffice for
    # this affine identity; four values provide a deterministic replay.
    constant_state = solve_square(observability, [1, 1, 1], prime)
    n_forcing = item230.mat_vec(n_matrix, forcing, prime)
    coefficient0 = [
        (h0 * forcing[j] - n_forcing[j]) % prime for j in range(3)
    ]
    coefficient1 = [
        (constant_state[j] - forcing[j]) % prime for j in range(3)
    ]
    anti_coefficient = item230.mat_vec(anti_matrix, candidate, prime)
    for scalar in (0, 1, 2, prime - 1):
        e0 = (scalar * terminal_values[0] + 4) % prime
        e1 = (scalar * terminal_values[1] - 2) % prime
        e3 = (scalar * terminal_values[3] + 2) % prime
        direct = [
            (scalar * anti_coefficient[j] - anti_rhs[j]) % prime
            for j in range(3)
        ]
        decomposed = [
            (
                coefficient0[j] * e0
                + coefficient1[j] * e1
                + constant_state[j] * e3
            )
            % prime
            for j in range(3)
        ]
        if direct != decomposed:
            raise AssertionError(
                (prime, r_value, s_value, scalar, "closure redundancy")
            )

    third_coefficient = int(system["coefficient_column"][2])
    third_rhs = int(system["rhs_column"][2])
    if terminal_values[1] != (third_coefficient + h0 * delta_plus) % prime:
        raise AssertionError((prime, r_value, s_value, "phase-3 coefficient"))
    if third_rhs != (2 + 4 * h0) % prime:
        raise AssertionError((prime, r_value, s_value, "phase-3 rhs"))

    return {
        "N": n_matrix,
        "O": observability,
        "det_O": det_observability,
        "h": h,
        "trace_B": trace_block,
        "det_B": determinant_block,
        "x": x_value,
        "y": y_value,
        "anti_determinant": closed_determinant,
        "anti_rank": rank_anti,
        "terminal_values": terminal_values,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=601)
    parser.add_argument("--identity-prime-max", type=int, default=151)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if not (13 <= args.identity_prime_max <= args.prime_max):
        raise ValueError("require 13 <= identity-prime-max <= prime-max")

    rows: list[tuple[int, ...]] = []
    endpoint_rows: list[tuple[int, ...]] = []
    singular_rows: list[dict[str, Any]] = []
    counts = {
        "actual_rows": 0,
        "endpoint_closed_formula_replay_rows": 0,
        "regular_rows": 0,
        "singular_rows": 0,
        "singular_p_mod_1_rows": 0,
        "singular_p_mod_3_rows": 0,
        "singular_rank_1_rows": 0,
        "singular_rank_2_rows": 0,
        "singular_affine_consistent_rows": 0,
        "singular_terminal_formally_solvable_rows": 0,
        "six_equation_formally_solvable_rows": 0,
    }

    for prime, _h_value, r_value, s_value in item228.actual_rows(args.prime_max):
        counts["actual_rows"] += 1
        system = item230.phase_system(prime, r_value, s_value)
        data = control_data(prime, r_value, s_value, system)
        if prime <= args.identity_prime_max:
            endpoint_rows.append(endpoint_replay(prime, r_value, s_value, system))
            counts["endpoint_closed_formula_replay_rows"] += 1

        determinant = int(data["anti_determinant"])
        if determinant:
            counts["regular_rows"] += 1
        else:
            counts["singular_rows"] += 1
            counts[f"singular_p_mod_{prime % 4}_rows"] += 1
            counts[f"singular_rank_{data['anti_rank']}_rows"] += 1
            counts["singular_affine_consistent_rows"] += 1

        terminal_coefficients = list(system["coefficient_column"][:3])
        terminal_rhs = list(system["rhs_column"][:3])
        terminal_rank = int(any(terminal_coefficients))
        terminal_augmented_rank = item230.rank_mod(
            [
                [terminal_coefficients[j], terminal_rhs[j]]
                for j in range(3)
            ],
            prime,
        )
        terminal_solvable = terminal_rank == terminal_augmented_rank == 1
        full_solvable = bool(system["formally_solvable"])
        if terminal_solvable != full_solvable:
            raise AssertionError((prime, r_value, s_value, "formal equivalence"))
        counts["six_equation_formally_solvable_rows"] += full_solvable
        if not determinant:
            counts["singular_terminal_formally_solvable_rows"] += terminal_solvable
            old = item228.second_transfer_components(prime, r_value, s_value)
            singular_rows.append(
                {
                    "p": prime,
                    "r": r_value,
                    "s": s_value,
                    "p_mod_4": prime % 4,
                    "h": data["h"],
                    "trace_B": data["trace_B"],
                    "det_B": data["det_B"],
                    "rank_I_plus_M2": data["anti_rank"],
                    "theta": system["theta"],
                    "psi": old["psi"],
                    "terminal_formally_solvable": terminal_solvable,
                }
            )

        rows.append(
            (
                prime,
                r_value,
                s_value,
                int(data["h"][0]),
                int(data["h"][1]),
                int(data["trace_B"]),
                int(data["det_B"]),
                determinant,
                int(data["anti_rank"]),
                int(system["theta"]),
                int(full_solvable),
            )
        )

    expected_default = {
        "actual_rows": 2435,
        "endpoint_closed_formula_replay_rows": 184,
        "regular_rows": 2432,
        "singular_rows": 3,
        "singular_p_mod_1_rows": 3,
        "singular_p_mod_3_rows": 0,
        "singular_rank_1_rows": 0,
        "singular_rank_2_rows": 3,
        "singular_affine_consistent_rows": 3,
        "singular_terminal_formally_solvable_rows": 0,
        "six_equation_formally_solvable_rows": 0,
    }
    if args.prime_max == 601 and args.identity_prime_max == 151:
        if counts != expected_default:
            raise AssertionError((counts, expected_default))
        expected_singular = [(349, 2, 57), (457, 128, 33), (577, 86, 67)]
        if [(x["p"], x["r"], x["s"]) for x in singular_rows] != expected_singular:
            raise AssertionError((singular_rows, expected_singular))

    result = {
        "schema": "item233-j1-antiperiod-determinant-v1",
        "dependency": {
            "item230_checker_sha256": sha256(ITEM230_PATH),
        },
        "proved": {
            "phase_model": [
                "the generalized {1,i,-i} endpoint map Phi is an isomorphism",
                "N=M+b*a has N^4=I and characteristic polynomial (x-1)(x^2+1)",
                "O=(a;aN;aN^2) is invertible and h3=aN^3b=1",
            ],
            "block_formula": {
                "h_q": "h_q=a*N^q*b",
                "trace_B": "1-h_0",
                "det_B": "1+h_1-h_0",
                "det_I_plus_M2": "(h_0-h_1)^2+(1-h_0)^2",
            },
            "rank_classification": [
                "rank(I+M^2)=3 off the determinant locus",
                "on the locus the rank is 1 iff h0=h1=1, and otherwise 2",
                "if s is even (p=3 mod 4), singularity is equivalent to h0=h1=1",
                "if s is odd (p=1 mod 4), the locus splits into the two linear factors over sqrt(-1)",
            ],
            "closed_coefficient_formula": {
                "polynomial": "C(z)=(1-z)^r(1+z^2)^(2s-1)",
                "phase_basis": phase_basis(),
                "Phi_kj": "sum_d [z^d]C(z)*q_j(p+r+T+k+d+1)/(p+r+T+k+d+1), deleting p-divisible denominators",
                "S": "diag(1, rotation by p) on the displayed phase basis",
                "N": "Phi*S*Phi^(-1)",
                "b": "N*e0/a0, where a0=r+2s+2",
                "numerator": "if D=det(Phi), Rk=a*Phi*S^k*adj(Phi)*e0, then det(I+M^2)=((R1-R2)^2+(a0*D-R1)^2)/(a0*D)^2",
            },
            "singular_no_go": "the affine antiperiod closure is consistent on every singular row; determinant singularity alone is never a contradiction",
            "terminal_redundancy": {
                "terminal_values": "t_q=a*N^q*v, with t_0=Delta_plus and t_3=Delta_minus",
                "phase_relation": "t_0-t_1+t_2-t_3=0",
                "residual_identity": "R=(h0*b-N*b)e0+(c-b)e1+c*e3, O*c=(1,1,1)^t",
                "consequence": "bottom, 2p, and 3p terminal equations force all three antiperiod coordinates without division by det(I+M^2)",
                "formal_criterion": "the six Item230 equations are solvable iff the three terminal equations are; equivalently Delta_plus!=0, Theta=0, and Psi=0",
            },
        },
        "exact_finite": {
            "prime_max_inclusive": args.prime_max,
            "identity_prime_max_inclusive": args.identity_prime_max,
            "counts": counts,
            "singular_rows": singular_rows,
            "row_stream_sha256": row_digest(rows),
            "endpoint_closed_formula_stream_sha256": row_digest(endpoint_rows),
        },
        "open": [
            "all-prime nonvanishing of the two exact singular factors",
            "all-prime exclusion or zero-rate control of the singular locus",
            "all-prime inconsistency of the equivalent terminal criterion Theta=Psi=0",
            "any new Route-1 rate or divisibility exponent",
        ],
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "conclusion_about_e_plus_pi": "none",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
