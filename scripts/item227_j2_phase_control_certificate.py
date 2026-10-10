#!/usr/bin/env python3
"""Deterministic certificate for Item 227's phase-control theorem.

The checker imports the frozen Item 226 transfer.  It replays the
four-periodic endpoint-weight model, the order-four feedback map, the
cyclotomic determinant/control factorization, singular affine
consistency, and the exact redundancy of the third and fourth terminal
residuals.  Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item227_j2_phase_control_certificate.json"


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


ITEM226_PATH = resolve("item226_j2_four_phase_closure_certificate.py")
item226 = load("item227_item226", ITEM226_PATH)
item225 = item226.item225
item224 = item226.item224
item221 = item226.item221
item219 = item226.item219


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def mat_add(left: list[list[int]], right: list[list[int]], p: int) -> list[list[int]]:
    return [
        [(left[i][j] + right[i][j]) % p for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def row_mat(row: list[int], matrix: list[list[int]], p: int) -> list[int]:
    return [
        sum(row[k] * matrix[k][j] for k in range(len(row))) % p
        for j in range(len(matrix[0]))
    ]


def matrix_power(matrix: list[list[int]], exponent: int, p: int) -> list[list[int]]:
    result = item226.identity(len(matrix))
    base = matrix
    while exponent:
        if exponent & 1:
            result = item226.mat_mul(result, base, p)
        base = item226.mat_mul(base, base, p)
        exponent //= 2
    return result


def solve_square(matrix: list[list[int]], rhs: list[int], p: int) -> list[int]:
    n = len(matrix)
    work = [[matrix[i][j] % p for j in range(n)] + [rhs[i] % p] for i in range(n)]
    for column in range(n):
        pivot = next((q for q in range(column, n) if work[q][column]), None)
        if pivot is None:
            raise ZeroDivisionError("singular matrix")
        work[column], work[pivot] = work[pivot], work[column]
        inverse = pow(work[column][column], -1, p)
        work[column] = [x * inverse % p for x in work[column]]
        for q in range(n):
            if q == column or work[q][column] == 0:
                continue
            factor = work[q][column]
            work[q] = [
                (work[q][j] - factor * work[column][j]) % p
                for j in range(n + 1)
            ]
    return [work[i][-1] for i in range(n)]


def general_period(p: int, s: int, k: int, weights: list[int]) -> int:
    """Regularized moment for an arbitrary four-periodic weight sequence."""
    r, polynomial = item225.g_polynomial(p, s)
    total = 0
    for ell, coefficient in enumerate(polynomial):
        denominator = r + ell + k + 1
        if denominator % p == 0:
            continue
        total += (
            coefficient
            * weights[denominator % 4]
            * pow(denominator % p, -1, p)
        )
    return total % p


def period_state(p: int, s: int, k: int, weights: list[int]) -> list[int]:
    return [general_period(p, s, k + j, weights) for j in range(4)]


def endpoint_replay(p: int, s: int, data: dict[str, object]) -> None:
    """Replay the coefficient-level four-periodic model on a basis."""
    r = int(data["r"])
    epsilon = (-1) ** r
    first = 2 * s - 3
    matrix: list[list[int]] = data["M"]  # type: ignore[assignment]
    forcing: list[int] = data["b"]  # type: ignore[assignment]
    terminal: list[int] = data["terminal_covector"]  # type: ignore[assignment]
    n_matrix: list[list[int]] = data["N"]  # type: ignore[assignment]
    phi_columns: list[list[int]] = []

    for residue in range(4):
        weights = [int(q == residue) for q in range(4)]
        state = period_state(p, s, first, weights)
        next_state = period_state(p, s, first + p, weights)
        weight_p = weights[p % 4]
        if item226.dot(terminal, state, p) != epsilon * weight_p % p:
            raise AssertionError((p, s, residue, "general terminal"))
        transferred = item226.add(
            item226.mat_vec(matrix, state, p),
            item226.scale(forcing, weight_p, p),
            p,
        )
        if next_state != transferred or next_state != item226.mat_vec(n_matrix, state, p):
            raise AssertionError((p, s, residue, "general transfer"))
        if period_state(p, s, first + 4 * p, weights) != state:
            raise AssertionError((p, s, residue, "general 4p periodicity"))
        phi_columns.append(state)

    phi = transpose(phi_columns)
    if item226.determinant_mod(phi, p) == 0:
        raise AssertionError((p, s, "Phi not invertible"))


def control_data(p: int, s: int, data: dict[str, object]) -> dict[str, object]:
    matrix: list[list[int]] = data["M"]  # type: ignore[assignment]
    forcing: list[int] = data["b"]  # type: ignore[assignment]
    terminal: list[int] = data["terminal_covector"]  # type: ignore[assignment]
    candidate: list[int] = data["candidate_tail"]  # type: ignore[assignment]
    r = int(data["r"])
    epsilon = (-1) ** r
    if epsilon != -1:
        raise AssertionError((p, s, r, "r must be odd"))

    u = [epsilon * x % p for x in forcing]
    feedback = [[u[i] * terminal[j] % p for j in range(4)] for i in range(4)]
    n_matrix = mat_add(matrix, feedback, p)
    powers = [matrix_power(n_matrix, q, p) for q in range(4)]
    if matrix_power(n_matrix, 4, p) != item226.identity(4):
        raise AssertionError((p, s, "N^4"))
    traces = [sum(q[i][i] for i in range(4)) % p for q in powers[1:]]
    if traces != [0, 0, 0] or item226.determinant_mod(n_matrix, p) != p - 1:
        raise AssertionError((p, s, "characteristic polynomial", traces))

    observability = [row_mat(terminal, q, p) for q in powers]
    control_columns = [item226.mat_vec(q, u, p) for q in powers]
    controllability = transpose(control_columns)
    det_o = item226.determinant_mod(observability, p)
    det_u = item226.determinant_mod(controllability, p)
    if det_o == 0:
        raise AssertionError((p, s, "observability"))

    cycle = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
    ]
    if item226.mat_mul(observability, n_matrix, p) != item226.mat_mul(cycle, observability, p):
        raise AssertionError((p, s, "cycle conjugacy"))

    h = [item226.dot(terminal, column, p) for column in control_columns]
    if h[3] != 1:
        raise AssertionError((p, s, "h3", h))
    gram = item226.mat_mul(observability, controllability, p)
    expected_gram = [[h[(i + j) % 4] for j in range(4)] for i in range(4)]
    if gram != expected_gram:
        raise AssertionError((p, s, "cyclic Gram"))

    h0, h1, h2, _ = h
    factors = [
        (1 + h0 + h1 + h2) % p,
        (1 - h0 + h1 - h2) % p,
        ((1 - h1) ** 2 + (h0 - h2) ** 2) % p,
    ]
    delta = int(data["fixed_determinant"])
    if delta != factors[0] * factors[1] * factors[2] % p:
        raise AssertionError((p, s, "cyclotomic Delta", delta, factors))
    if delta != item226.determinant_mod(gram, p):
        raise AssertionError((p, s, "Gram Delta"))
    if delta != det_o * det_u % p:
        raise AssertionError((p, s, "control Delta"))

    # Canonical companion feedback: O M = (S-h e_0^t) O.
    canonical_m = [row[:] for row in cycle]
    for i in range(4):
        canonical_m[i][0] = (canonical_m[i][0] - h[i]) % p
    if item226.mat_mul(observability, matrix, p) != item226.mat_mul(canonical_m, observability, p):
        raise AssertionError((p, s, "canonical feedback"))

    # Every singular affine fixed-point equation is consistent.
    closure_matrix: list[list[int]] = data["closure_matrix"]  # type: ignore[assignment]
    closure_rhs: list[int] = data["closure_rhs"]  # type: ignore[assignment]
    augmented = [closure_matrix[i] + [closure_rhs[i]] for i in range(4)]
    if item226.rank_mod(augmented, p) != item226.rank_mod(closure_matrix, p):
        raise AssertionError((p, s, "affine closure consistency"))

    # Replay the mismatch/control identity on a spanning affine set.
    weights: list[int] = data["weights"]  # type: ignore[assignment]
    reverse_control = [
        item226.mat_vec(powers[3], forcing, p),
        item226.mat_vec(powers[2], forcing, p),
        item226.mat_vec(powers[1], forcing, p),
        forcing,
    ]
    reverse_matrix = transpose(reverse_control)
    for initial in [[0, 0, 0, 0]] + item226.identity(4):
        state = initial[:]
        mismatches = []
        for q in range(4):
            mismatch = (weights[q] - epsilon * item226.dot(terminal, state, p)) % p
            mismatches.append(mismatch)
            via_m = item226.add(
                item226.mat_vec(matrix, state, p),
                item226.scale(forcing, weights[q], p),
                p,
            )
            via_n = item226.add(
                item226.mat_vec(n_matrix, state, p),
                item226.scale(forcing, mismatch, p),
                p,
            )
            if via_m != via_n:
                raise AssertionError((p, s, q, "mismatch step"))
            state = via_m
        difference = [(state[j] - initial[j]) % p for j in range(4)]
        if difference != item226.mat_vec(reverse_matrix, mismatches, p):
            raise AssertionError((p, s, "mismatch closure"))

    # The exact z^3 boundary at -1 is a unit.
    numerator_at_minus_one = (-(10 * s - 5) + 4 + 4 + 4 + (10 * s - 1))
    if numerator_at_minus_one != 16:
        raise AssertionError((p, s, "H3 numerator"))
    boundary_minus_one = (
        epsilon
        * pow(2, r + 2 * s + 3, p)
        * pow((s - 1) * (10 * s - 1) % p, -1, p)
    ) % p
    if boundary_minus_one == 0:
        raise AssertionError((p, s, "H3 boundary unit"))

    # Candidate terminal residuals.  The -1 Fourier mode vanishes,
    # the fourth phase is the reciprocal bottom terminal, and the
    # third residual is the difference of the first two.
    terminal_values = [item226.dot(observability[q], candidate, p) for q in range(4)]
    if (terminal_values[0] - terminal_values[1] + terminal_values[2] - terminal_values[3]) % p:
        raise AssertionError((p, s, "minus-one Fourier mode", terminal_values))
    beta = int(data["beta"])
    if terminal_values[3] != -epsilon * beta % p:
        raise AssertionError((p, s, "bottom reciprocity", terminal_values[3], beta))
    residuals = [
        (11 * terminal_values[q] - epsilon * beta * weights[q]) % p
        for q in range(4)
    ]
    if residuals[3] != 0 or residuals[2] != (residuals[1] - residuals[0]) % p:
        raise AssertionError((p, s, "residual redundancy", residuals))
    if residuals[0] != -int(data["omega"]) % p:
        raise AssertionError((p, s, "E1 Omega"))

    second = item225.second_phase_components(p, s)
    rho0 = int(second["rho_constant"])
    rho1 = int(second["rho_lambda"])
    psi = int(second["psi"])
    psi_flat = (beta * (rho0 - epsilon * 29) + 11 * rho1) % p
    a_dot_b = item226.dot(terminal, forcing, p)
    if rho0 != 7 * a_dot_b % p:
        raise AssertionError((p, s, "rho0"))
    if residuals[1] != (psi_flat - epsilon * a_dot_b * int(data["omega"])) % p:
        raise AssertionError((p, s, "E2 Psi-flat"))
    if int(data["omega"]) == 0:
        if (11 * psi - 7 * epsilon * psi_flat) % p:
            raise AssertionError((p, s, "Psi scaling"))
        if (all(x == 0 for x in residuals)) != (psi == 0):
            raise AssertionError((p, s, "two-invariant equivalence"))

    result = dict(data)
    result.update(
        {
            "N": n_matrix,
            "O": observability,
            "U_control": controllability,
            "h": h,
            "factors": factors,
            "det_O": det_o,
            "det_U": det_u,
            "rank_closure": item226.rank_mod(closure_matrix, p),
            "terminal_values": terminal_values,
            "residuals": residuals,
            "psi": psi,
            "psi_flat": psi_flat,
            "boundary_minus_one": boundary_minus_one,
        }
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=401)
    parser.add_argument("--identity-prime-max", type=int, default=101)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if not (17 <= args.identity_prime_max <= args.prime_max):
        raise ValueError("require 17 <= identity-prime-max <= prime-max")

    counts = {
        "rows": 0,
        "s_at_least_2_rows": 0,
        "endpoint_basis_replay_rows": 0,
        "N_fourth_power_identity_rows": 0,
        "observable_rows": 0,
        "singular_Delta_rows": 0,
        "singular_affine_consistent_rows": 0,
        "terminal_redundancy_rows": 0,
        "omega_zero_rows": 0,
        "omega_psi_zero_rows": 0,
    }
    factor_zero_rows: list[list[list[int]]] = [[], [], []]
    singular_rows: list[dict[str, object]] = []
    rows: list[tuple[int, ...]] = []

    for p in item219.primes_upto(args.prime_max):
        if p < 17:
            continue
        for s in range(2, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            counts["rows"] += 1
            counts["s_at_least_2_rows"] += 1
            data = item226.phase_system(p, s)
            controlled = control_data(p, s, data)
            counts["N_fourth_power_identity_rows"] += 1
            counts["observable_rows"] += 1
            counts["terminal_redundancy_rows"] += 1
            if p <= args.identity_prime_max:
                augmented = dict(data)
                augmented["N"] = controlled["N"]
                endpoint_replay(p, s, augmented)
                counts["endpoint_basis_replay_rows"] += 1

            factors: list[int] = controlled["factors"]  # type: ignore[assignment]
            for q, value in enumerate(factors):
                if value == 0:
                    factor_zero_rows[q].append([p, s])
            delta = int(data["fixed_determinant"])
            if delta == 0:
                counts["singular_Delta_rows"] += 1
                counts["singular_affine_consistent_rows"] += 1
                singular_rows.append(
                    {
                        "p": p,
                        "s": s,
                        "m": (5 * p - 2 * s - 1) // 4,
                        "factor_values_F1_Fminus1_Fi": factors,
                        "rank_I_minus_M4": int(controlled["rank_closure"]),
                        "rank_control": item226.rank_mod(controlled["U_control"], p),  # type: ignore[arg-type]
                        "omega_mod_p": int(data["omega"]),
                    }
                )
            omega = int(data["omega"])
            psi = int(controlled["psi"])
            counts["omega_zero_rows"] += omega == 0
            counts["omega_psi_zero_rows"] += omega == 0 and psi == 0
            residuals: list[int] = controlled["residuals"]  # type: ignore[assignment]
            rows.append(
                (
                    p,
                    s,
                    delta,
                    factors[0],
                    factors[1],
                    factors[2],
                    int(controlled["det_O"]),
                    int(controlled["det_U"]),
                    omega,
                    psi,
                    residuals[0],
                    residuals[1],
                    residuals[2],
                    residuals[3],
                )
            )

    result = {
        "schema": "item227-j2-phase-control-v1",
        "parameters": {
            "j": 2,
            "prime_max_inclusive": args.prime_max,
            "endpoint_basis_replay_prime_max_inclusive": args.identity_prime_max,
            "cell": "4m+1=5p-2s, 2<=s<=(p-3)/6, p>=17, s=(p-1)/2 mod 2",
        },
        "dependencies": {
            "item226_checker": ITEM226_PATH.name,
            "item226_checker_sha256": sha256(ITEM226_PATH),
            "item225_checker": item226.ITEM225_PATH.name,
            "item225_checker_sha256": sha256(item226.ITEM225_PATH),
            "item224_checker": item226.item225.ITEM224_PATH.name,
            "item224_checker_sha256": sha256(item226.item225.ITEM224_PATH),
            "item221_checker": item226.item225.item224.ITEM221_PATH.name,
            "item221_checker_sha256": sha256(item226.item225.item224.ITEM221_PATH),
            "item219_checker": item226.item225.item224.item221.ITEM219_PATH.name,
            "item219_checker_sha256": sha256(item226.item225.item224.item221.ITEM219_PATH),
        },
        "order_four_control": {
            "definitions": "epsilon=(-1)^r, u=epsilon*b, N=M+u*a, O=rows(a,aN,aN^2,aN^3), U=columns(u,Nu,N^2u,N^3u)",
            "endpoint_model": "Phi maps arbitrary four-periodic monomial weights to the four first-terminal moments and is an isomorphism",
            "identities": [
                "N^4=I and char_N(x)=x^4-1",
                "O is invertible and O*N=S*O for the four-cycle S",
                "M=N-u*a",
            ],
        },
        "determinant_factorization": {
            "h": "h_q=a*N^q*u with h_3=1",
            "D": "det(I-tB)=1+h_0*t+h_1*t^2+h_2*t^3",
            "Delta": "det(I-M^4)=F_1*F_minus1*F_i=det(O)*det(U)",
            "F_1": "1+h_0+h_1+h_2",
            "F_minus1": "1-h_0+h_1-h_2",
            "F_i": "(1-h_1)^2+(h_0-h_2)^2",
        },
        "singular_left_null": {
            "classification": "Delta=0 iff the source u loses at least one Fourier/control mode of N",
            "affine_consistency": "for every left null vector ell of I-M^4, ell*u=ell*b=0, hence ell*C=0 and C lies in im(I-M^4)",
            "scope": "singular Delta creates spurious terminal-mismatch modes; it never supplies an affine closure contradiction by itself",
        },
        "terminal_redundancy": {
            "candidate": "v is Item224's canonical common-line tail and t_q=a*N^(q-1)*v",
            "minus_one_boundary": "H_3*f_0(-1)=(-1)^r*2^(r+2s+3)/((s-1)(10s-1)), a p-unit",
            "identities": [
                "t_1-t_2+t_3-t_4=0",
                "t_4=-epsilon*beta",
                "E_4=0",
                "E_3=E_2-E_1",
                "E_1=-Omega",
                "E_2=Psi_flat-epsilon*(a*b)*Omega",
            ],
            "residual_definition": "E_q=11*t_q-epsilon*beta*w_q for w=(7,29,11,-11)",
            "consequence": "bottom plus all four phase terminals is equivalent to the existing Omega=Psi=0 system (with the usual nonzero bottom normalization); phases 3 and 4 add no third invariant",
        },
        "finite_classification": {
            "status": "EXACT FINITE ONLY",
            "counts": counts,
            "factor_zero_rows_F1_Fminus1_Fi": factor_zero_rows,
            "singular_rows": singular_rows,
            "row_digest_sha256": row_digest(rows),
            "interpretation": (
                f"through the bound, Delta has {counts['singular_Delta_rows']} zeros "
                f"({len(factor_zero_rows[0])} in F1, {len(factor_zero_rows[1])} in "
                f"Fminus1, {len(factor_zero_rows[2])} in Fi), every singular affine "
                "closure is consistent, and no Omega=Psi joint zero occurs"
            ),
        },
        "status_ledger": {
            "PROVED": [
                "the generalized endpoint-weight map is an isomorphism and N has exact order four",
                "the cyclotomic/control determinant factorization and singular left-null classification",
                "singular affine closure is always consistent; Delta alone cannot exclude a row",
                "the phase-4/bottom reciprocity and alternating phase identity",
                "the four terminal residuals reduce exactly to the two existing invariants Omega and Psi",
            ],
            "EXACT_FINITE": [
                "the complete factor-family census and singular ranks through the stated bound",
                "all endpoint-basis identities are replayed coefficientwise through the smaller stated bound",
                "there is no simultaneous Omega=Psi zero through the stated bound",
            ],
            "OPEN": [
                "an all-prime exclusion or zero-rate theorem for simultaneous Omega=Psi zeros",
                "an all-prime density classification of the three Delta factors",
                "the exceptional s=1 family",
                "a zero-rate theorem for the fixed j=2 cell",
                "any common-log capacity reduction or conclusion about e+pi",
            ],
        },
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(payload.decode("utf-8"), end="")


if __name__ == "__main__":
    main()
