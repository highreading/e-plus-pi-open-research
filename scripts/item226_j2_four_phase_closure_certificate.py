#!/usr/bin/env python3
"""Deterministic certificate for Item 226's four-phase closure.

The checker imports the frozen Item 225 helper beside it.  It constructs
the exact one-phase transfer, retains the q*p multiplicity at every
Cartier terminal, proves the formal system's augmented-rank criterion,
and performs a finite census of regular and rank-degenerate rows.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item226_j2_four_phase_closure_certificate.json"


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


ITEM225_PATH = resolve("item225_j2_second_cartier_certificate.py")
item225 = load("item226_item225", ITEM225_PATH)
item224 = item225.item224
item221 = item225.item221
item219 = item225.item219


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def add(left: list[int], right: list[int], p: int) -> list[int]:
    return [(left[j] + right[j]) % p for j in range(len(left))]


def scale(value: list[int], scalar: int, p: int) -> list[int]:
    return [scalar * x % p for x in value]


def dot(left: list[int], right: list[int], p: int) -> int:
    return sum(x * y for x, y in zip(left, right)) % p


def mat_vec(matrix: list[list[int]], vector: list[int], p: int) -> list[int]:
    return [dot(row, vector, p) for row in matrix]


def mat_mul(left: list[list[int]], right: list[list[int]], p: int) -> list[list[int]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right))) % p
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def matrix_sub(left: list[list[int]], right: list[list[int]], p: int) -> list[list[int]]:
    return [
        [(left[i][j] - right[i][j]) % p for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def determinant_mod(matrix: list[list[int]], p: int) -> int:
    work = [[x % p for x in row] for row in matrix]
    result = 1
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result = result * pivot_value % p
        inverse = pow(pivot_value, -1, p)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * inverse % p
            for j in range(column, len(work)):
                work[row][j] = (work[row][j] - factor * work[column][j]) % p
    return result % p


def rank_mod(matrix: list[list[int]], p: int) -> int:
    work = [[x % p for x in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((j for j in range(row, len(work)) if work[j][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, p)
        work[row] = [x * inverse % p for x in work[row]]
        for j in range(len(work)):
            if j != row and work[j][column]:
                factor = work[j][column]
                work[j] = [
                    (work[j][q] - factor * work[row][q]) % p
                    for q in range(len(work[0]))
                ]
        row += 1
    return row


def candidate_tail(p: int, s: int) -> tuple[int, list[int]]:
    beta, tau, omega, r = item224.compatibility_mod(p, s)
    values = item224.initial_line_mod(p, s)
    first = 2 * s - 3
    for k in range(0, first):
        coefficients = item225.recurrence_coefficients(k, r, s)
        lower = sum(coefficients[j] * values[k + j] for j in range(4))
        values[k + 4] = -lower * pow(coefficients[4] % p, -1, p) % p
    tail = [values[first + j] for j in range(4)]
    if dot([x % p for x in item225.recurrence_coefficients(first, r, s)[:4]], tail, p) != tau:
        raise AssertionError((p, s, "candidate tail"))
    return r, tail


def one_phase_transfer(p: int, s: int) -> dict[str, object]:
    r, g = item225.g_polynomial(p, s)
    first = 2 * s - 3
    dimension = 6  # four state inputs, one free input, one phase-weight input

    def h_coefficient(exponent: int) -> int:
        def f_coefficient(q: int) -> int:
            index = q - r
            return g[index] if 0 <= index < len(g) else 0

        return (f_coefficient(exponent) - f_coefficient(exponent - 4)) % p

    values: dict[int, list[int]] = {}
    for j in range(4):
        values[first + j] = [int(q == j) for q in range(dimension)]
    values[first + 4] = [int(q == 4) for q in range(dimension)]

    # At relative offset t, the q-th phase K contains z^(q p) with
    # coefficient h_(p-2s+2-t).  The normalized forcing coordinate is
    # the exact weight W(qp), with no division by q.
    for k in range(first + 1, first + p):
        t = k - first
        coefficients = item225.recurrence_coefficients(k, r, s)
        pivot = coefficients[4] % p
        if pivot != (-t) % p or pivot == 0:
            raise AssertionError((p, s, k, t, pivot))
        numerator = [0] * dimension
        for j in range(4):
            numerator = add(numerator, scale(values[k + j], -coefficients[j], p), p)
        numerator[5] = (numerator[5] - h_coefficient(p - 2 * s + 2 - t)) % p
        values[k + 4] = scale(numerator, pow(pivot, -1, p), p)

    next_state = [values[first + p + j] for j in range(4)]
    matrix = [[next_state[row][column] for column in range(4)] for row in range(4)]
    free_column = [next_state[row][4] for row in range(4)]
    forcing = [next_state[row][5] for row in range(4)]
    if free_column != [0, 0, 0, 0]:
        raise AssertionError((p, s, "free column", free_column))
    if any(matrix[row][0] for row in range(4)):
        raise AssertionError((p, s, "forgotten first coordinate", matrix))
    return {
        "M": matrix,
        "b": forcing,
        "free_column": free_column,
        "rank_M": rank_mod(matrix, p),
        "first": first,
        "r": r,
    }


def phase_weight(p: int, q: int) -> int:
    chi = 1 if p % 4 == 1 else -1
    return item219.residue_weight(q * p, chi) % p


def phase_system(p: int, s: int) -> dict[str, object]:
    beta, tau, omega, r = item224.compatibility_mod(p, s)
    transfer = one_phase_transfer(p, s)
    if transfer["r"] != r:
        raise AssertionError((p, s, "r mismatch"))
    matrix: list[list[int]] = transfer["M"]  # type: ignore[assignment]
    forcing: list[int] = transfer["b"]  # type: ignore[assignment]
    _, candidate = candidate_tail(p, s)
    first = 2 * s - 3
    terminal = [x % p for x in item225.recurrence_coefficients(first, r, s)[:4]]
    epsilon = (-1) ** r
    weights = [phase_weight(p, q) for q in range(1, 5)]
    expected_integer_weights = [7, 29, 11, -11]
    if weights != [x % p for x in expected_integer_weights]:
        raise AssertionError((p, s, "phase weights", weights))

    # Exact q*p audit: the terminal pivot is -q*p, and the omitted
    # leading primitive is (-1)^r z^(q p)/(q p), so q cancels.
    for q in range(1, 5):
        kq = (q - 1) * p + first
        coefficient = -(kq + 2 * r + 4 * s + 6)
        if coefficient != -q * p:
            raise AssertionError((p, s, q, coefficient))

    constants: list[list[int]] = []
    lambdas: list[list[int]] = []
    constant = [0, 0, 0, 0]
    lambda_vector = candidate[:]
    for q in range(4):
        constants.append(constant)
        lambdas.append(lambda_vector)
        constant = add(mat_vec(matrix, constant, p), scale(forcing, weights[q], p), p)
        lambda_vector = mat_vec(matrix, lambda_vector, p)
    constant_after_four = constant
    lambda_after_four = lambda_vector

    coefficient_column: list[int] = [beta]
    rhs_column: list[int] = [11 % p]
    equation_names = ["bottom"]
    terminal_rows: list[dict[str, int]] = []
    for q in range(4):
        coefficient = dot(terminal, lambdas[q], p)
        rhs = (epsilon * weights[q] - dot(terminal, constants[q], p)) % p
        coefficient_column.append(coefficient)
        rhs_column.append(rhs)
        equation_names.append(f"terminal_{q + 1}")
        terminal_rows.append(
            {
                "q": q + 1,
                "coefficient_of_lambda": coefficient,
                "rhs": rhs,
                "weight": weights[q],
                "exact_pivot_multiple": q + 1,
            }
        )
    if coefficient_column[1] != tau or rhs_column[1] != 7 * epsilon % p:
        raise AssertionError((p, s, "first terminal replay"))
    if (coefficient_column[0] * rhs_column[1] - coefficient_column[1] * rhs_column[0]) % p != omega:
        raise AssertionError((p, s, "Omega minor replay"))
    second_phase = item225.second_phase_components(p, s)
    psi_minor = (
        coefficient_column[1] * rhs_column[2]
        - coefficient_column[2] * rhs_column[1]
    ) % p
    if psi_minor != (-second_phase["psi"]) % p:
        raise AssertionError((p, s, "Psi minor replay", psi_minor, second_phase["psi"]))

    matrix_four = mat_mul(mat_mul(matrix, matrix, p), mat_mul(matrix, matrix, p), p)
    closure_matrix = matrix_sub(identity(4), matrix_four, p)
    closure_coefficient = mat_vec(closure_matrix, candidate, p)
    closure_rhs = constant_after_four
    # Direct replay of M^4 v.
    if mat_vec(matrix_four, candidate, p) != lambda_after_four:
        raise AssertionError((p, s, "M4"))
    for j in range(4):
        coefficient_column.append(closure_coefficient[j])
        rhs_column.append(closure_rhs[j])
        equation_names.append(f"closure_{j}")

    augmented = [[coefficient_column[j], rhs_column[j]] for j in range(len(coefficient_column))]
    minors: list[dict[str, int | str]] = []
    all_zero = True
    for i in range(len(augmented)):
        for j in range(i + 1, len(augmented)):
            value = (
                coefficient_column[i] * rhs_column[j]
                - coefficient_column[j] * rhs_column[i]
            ) % p
            all_zero &= value == 0
            minors.append({"rows": f"{equation_names[i]}|{equation_names[j]}", "value": value})
    coefficient_rank = int(any(coefficient_column))
    augmented_rank = rank_mod(augmented, p)
    formal_solvable = coefficient_rank == augmented_rank == 1
    if formal_solvable != (coefficient_rank == 1 and all_zero):
        raise AssertionError((p, s, "rank/minor criterion"))

    closure_augmented = [
        [closure_coefficient[j], closure_rhs[j]]
        for j in range(4)
    ]
    closure_minors = [
        (
            closure_coefficient[i] * closure_rhs[j]
            - closure_coefficient[j] * closure_rhs[i]
        )
        % p
        for i in range(4)
        for j in range(i + 1, 4)
    ]
    closure_solvable = rank_mod(closure_augmented, p) == rank_mod(
        [[x] for x in closure_coefficient], p
    )
    fixed_determinant = determinant_mod(closure_matrix, p)
    return {
        "r": r,
        "beta": beta,
        "tau": tau,
        "omega": omega,
        "M": matrix,
        "b": forcing,
        "rank_M": transfer["rank_M"],
        "free_column": transfer["free_column"],
        "terminal_covector": terminal,
        "weights": weights,
        "candidate_tail": candidate,
        "terminal_rows": terminal_rows,
        "closure_matrix": closure_matrix,
        "closure_coefficient": closure_coefficient,
        "closure_rhs": closure_rhs,
        "fixed_determinant": fixed_determinant,
        "equation_names": equation_names,
        "coefficient_column": coefficient_column,
        "rhs_column": rhs_column,
        "all_augmented_minors_zero": all_zero,
        "formal_system_solvable": formal_solvable,
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "closure_minors": closure_minors,
        "closure_solvable": closure_solvable,
        "all_augmented_minors": minors,
    }


def verify_actual_phases(p: int, s: int, data: dict[str, object]) -> None:
    r = int(data["r"])
    first = 2 * s - 3
    matrix: list[list[int]] = data["M"]  # type: ignore[assignment]
    forcing: list[int] = data["b"]  # type: ignore[assignment]
    terminal: list[int] = data["terminal_covector"]  # type: ignore[assignment]
    weights: list[int] = data["weights"]  # type: ignore[assignment]
    epsilon = (-1) ** r
    states: list[list[int]] = []
    for q in range(1, 6):
        kq = (q - 1) * p + first
        state = [item225.finite_period(p, s, kq + j) for j in range(4)]
        states.append(state)
        if q <= 4 and dot(terminal, state, p) != epsilon * weights[q - 1] % p:
            raise AssertionError((p, s, q, "actual terminal"))
    for q in range(4):
        expected = add(mat_vec(matrix, states[q], p), scale(forcing, weights[q], p), p)
        if states[q + 1] != expected:
            raise AssertionError((p, s, q + 1, "actual transfer", states[q + 1], expected))
    if states[4] != states[0]:
        raise AssertionError((p, s, "4p periodicity", states[0], states[4]))

    # Coefficientwise replay beyond just the four state entries.
    for k in range(-r, 2 * s + 2):
        if item225.finite_period(p, s, k) != item225.finite_period(p, s, k + 4 * p):
            raise AssertionError((p, s, k, "coefficientwise 4p periodicity"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-max", type=int, default=401)
    ap.add_argument("--identity-prime-max", type=int, default=101)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if not (17 <= args.identity_prime_max <= args.prime_max):
        raise ValueError("require 17 <= identity-prime-max <= prime-max")

    counts = {
        "rows": 0,
        "s_equals_1_rows": 0,
        "s_at_least_2_rows": 0,
        "fixed_determinant_unit_rows": 0,
        "fixed_determinant_zero_rows": 0,
        "formal_system_solvable_rows": 0,
        "formal_system_inconsistent_rows": 0,
        "closure_solvable_rows": 0,
        "actual_common_zero_rows": 0,
        "full_phase_replay_rows": 0,
        "omega_zero_rows": 0,
        "omega_psi_zero_rows": 0,
    }
    determinant_zero_rows: list[dict[str, int | bool]] = []
    formal_solvable_rows: list[dict[str, int]] = []
    closure_minor_zero_rows: list[list[list[int]]] = [[] for _ in range(6)]
    rows: list[tuple[int, ...]] = []

    for p in item219.primes_upto(args.prime_max):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            counts["rows"] += 1
            m = (5 * p - 2 * s - 1) // 4
            if s == 1:
                counts["s_equals_1_rows"] += 1
                rows.append((p, s, m, -1, -1, -1, -1, -1))
                continue

            counts["s_at_least_2_rows"] += 1
            data = phase_system(p, s)
            if p <= args.identity_prime_max:
                verify_actual_phases(p, s, data)
                counts["full_phase_replay_rows"] += 1

            if data["fixed_determinant"]:
                counts["fixed_determinant_unit_rows"] += 1
            else:
                counts["fixed_determinant_zero_rows"] += 1
                determinant_zero_rows.append(
                    {
                        "p": p,
                        "s": s,
                        "m": m,
                        "rank_M": int(data["rank_M"]),
                        "closure_solvable": bool(data["closure_solvable"]),
                        "formal_system_solvable": bool(data["formal_system_solvable"]),
                    }
                )
            if data["formal_system_solvable"]:
                counts["formal_system_solvable_rows"] += 1
                formal_solvable_rows.append({"p": p, "s": s, "m": m})
            else:
                counts["formal_system_inconsistent_rows"] += 1
            counts["closure_solvable_rows"] += bool(data["closure_solvable"])

            for j, value in enumerate(data["closure_minors"]):
                if value == 0:
                    closure_minor_zero_rows[j].append([p, s])

            counts["omega_zero_rows"] += data["omega"] == 0
            # terminal_1|terminal_2 is -Psi by the all-row assertion in
            # phase_system; recover it from the recorded augmented minors.
            terminal_psi_minor = next(
                entry["value"]
                for entry in data["all_augmented_minors"]
                if entry["rows"] == "terminal_1|terminal_2"
            )
            counts["omega_psi_zero_rows"] += data["omega"] == 0 and terminal_psi_minor == 0
            t0, s1 = item224.actual_gate(p, s)
            actual = t0 == s1 == 0
            counts["actual_common_zero_rows"] += actual
            rows.append(
                (
                    p,
                    s,
                    m,
                    int(data["fixed_determinant"]),
                    int(data["augmented_rank"]),
                    int(data["formal_system_solvable"]),
                    int(data["closure_solvable"]),
                    int(actual),
                )
            )

    result = {
        "schema": "item226-j2-four-phase-closure-v1",
        "parameters": {
            "j": 2,
            "prime_max_inclusive": args.prime_max,
            "full_phase_replay_prime_max_inclusive": args.identity_prime_max,
            "cell": "4m+1=5p-2s, 1<=s<=(p-3)/6, p>=11, s=(p-1)/2 mod 2",
        },
        "dependencies": {
            "item225_checker": ITEM225_PATH.name,
            "item225_checker_sha256": sha256(ITEM225_PATH),
            "item224_checker": item225.ITEM224_PATH.name,
            "item224_checker_sha256": sha256(item225.ITEM224_PATH),
            "item221_checker": item225.item224.ITEM221_PATH.name,
            "item221_checker_sha256": sha256(item225.item224.ITEM221_PATH),
            "item219_checker": item225.item224.item221.ITEM219_PATH.name,
            "item219_checker_sha256": sha256(item225.item224.item221.ITEM219_PATH),
        },
        "phase_transfer": {
            "state": "Y_q=(That_(k_q),...,That_(k_q+3)), k_q=(q-1)p+2s-3",
            "identity": "Y_(q+1)=M Y_q+b W_L(qp)",
            "free_column": "zero identically by Item225's X=g support theorem",
            "terminal": "a dot Y_q=(-1)^r W_L(qp)",
            "integer_weight_cycle": [7, 29, 11, -11],
            "exact_terminal_coefficient": "-q*p",
            "multiplicity_audit": "(-q*p)*((-1)^r/(q*p)) cancels q exactly; no factor q is lost or added",
        },
        "periodicity": {
            "identity": "That_(k+4p)=That_k coefficientwise",
            "reason": "denominators and omitted p-multiples agree mod p, and endpoint monomial weights have period 4",
            "closure": "(I-M^4)Y_1=(M^3 b)w_1+(M^2 b)w_2+(M b)w_3+b w_4",
        },
        "formal_system": {
            "unknown": "lambda",
            "equations": [
                "lambda*beta=11",
                "four terminal equations a dot (C_q+lambda V_q)=(-1)^r w_q",
                "four closure-coordinate equations"
            ],
            "augmented_rows": 9,
            "solvability": "rank([coefficient|rhs])=rank(coefficient)=1, equivalently one coefficient is nonzero and all 36 pairwise 2x2 minors vanish",
            "necessity": "every actual collision with s>=2 makes the formal system solvable",
            "regular_row_equivalence": "if Delta=det(I-M^4) is nonzero, closure solvability is equivalent to the original common-log collision",
            "singular_row_scope": "if Delta=0, the augmented system remains necessary but closure alone need not be sufficient",
        },
        "finite_classification": {
            "status": "EXACT FINITE ONLY",
            "counts": counts,
            "fixed_determinant_zero_rows": determinant_zero_rows,
            "formal_solvable_rows": formal_solvable_rows,
            "closure_minor_zero_rows_by_pair_01_02_03_12_13_23": closure_minor_zero_rows,
            "row_digest_sha256": row_digest(rows),
            "interpretation": "the exact augmented system is inconsistent on every s>=2 row through the bound; each individual closure minor nevertheless has explicit zeros",
        },
        "status_ledger": {
            "PROVED": [
                "exact q-phase transfer with the q*p multiplicity retained",
                "coefficientwise 4p periodicity and four-phase affine closure",
                "exact nine-equation augmented-rank/minor solvability criterion",
                "collision implies formal solvability for every s>=2 row",
                "when det(I-M^4) is a unit, closure solvability is equivalent to the original common gate",
            ],
            "EXACT_FINITE": [
                "the formal system is inconsistent on every s>=2 row through the stated bound",
                "fixed-point determinant zeros through the stated bound are isolated and separately audited",
                "the recorded zero lists audit individual closure minors only through the stated bound; no all-row unit inference is made",
            ],
            "OPEN": [
                "an all-prime unit-minor or augmented-rank inconsistency theorem",
                "classification or density control of det(I-M^4)=0 rows",
                "the exceptional s=1 family",
                "a zero-rate theorem for the j=2 cell",
                "any capacity reduction or conclusion about e+pi",
            ],
        },
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(payload.decode("utf-8"), end="")


if __name__ == "__main__":
    main()
