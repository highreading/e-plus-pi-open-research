#!/usr/bin/env python3
"""Deterministic checker for Item 238's squared-denominator phase carry."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item238_j1_squared_carry_certificate.json"

DEPENDENCIES = {
    "sources/item233_j1_antiperiod_determinant_report.md":
        "7f595b7d4100fa069d90dea1b899864cba2238070e3e9bd919fdf4cb380badfd",
    "scripts/item233_j1_antiperiod_determinant_certificate.py":
        "f3196c577a0083e6b429b30c56a71bca03ad15330e09f7044453a681dab2a5b9",
    "sources/item234_j1_first_witt_report.md":
        "9bd5bb91fe813622db0c15d8bfc25714bcefb00512ed8f5eafddacd8cfb9b016",
    "scripts/item234_j1_first_witt_certificate.py":
        "8d41a5a73e9467cf4c998d3e345767c04c68ab6467605290480825b15b08e125",
    "results/item234_j1_first_witt_certificate.json":
        "6797c1f2cd072ec92d311e01b596c3ac95888ce9b761bc325a625ef6f9f0c748",
}


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def resolve_dependency(relative_name: str) -> Path:
    candidates = (HERE.parent / relative_name, HERE / Path(relative_name).name)
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(relative_name)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def primes_upto(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value, flag in enumerate(flags) if flag]


def rows_upto(limit: int):
    for prime in primes_upto(limit):
        if prime < 13:
            continue
        for s_value in range(1, (prime - 7) // 6 + 1):
            remainder = prime - 6 * s_value - 3
            if remainder > 0 and remainder % 4 == 0:
                h_value = remainder // 4
                if h_value >= 1:
                    yield prime, 2 * h_value, s_value


def convolution(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        if left_value:
            for right_degree, right_value in enumerate(right):
                if right_value:
                    answer[left_degree + right_degree] += left_value * right_value
    return answer


def w_polynomial(r_value: int, s_value: int) -> list[int]:
    left = [(-1) ** degree * math.comb(r_value, degree) for degree in range(r_value + 1)]
    even = [0] * (4 * s_value - 1)
    for degree in range(2 * s_value):
        even[2 * degree] = math.comb(2 * s_value - 1, degree)
    return convolution(left, even)


MODE_VALUES = {
    "one": (1, 1, 1, 1),
    "cos": (1, 0, -1, 0),
    "sin": (0, 1, 0, -1),
}
MODES = ("one", "cos", "sin")


def mode_value(mode: str, integer: int) -> int:
    return MODE_VALUES[mode][integer % 4]


def ell_numerator(integer: int, epsilon: int) -> int:
    # This is ell_(integer-1), as a function of the primitive denominator.
    return 4 * epsilon * mode_value("cos", integer) - 2 * mode_value("sin", integer)


def u_mode_mod(
    poly: list[int],
    prime: int,
    r_value: int,
    t_value: int,
    mode: str,
    modulus: int,
    numerator_shift: int = 0,
) -> int:
    answer = 0
    for degree, coefficient in enumerate(poly):
        denominator = prime + r_value + t_value + degree + 1
        if denominator % prime:
            answer += (
                coefficient
                * mode_value(mode, denominator + numerator_shift)
                * pow(denominator, -1, modulus)
            )
    return answer % modulus


def v_mode_mod(
    poly: list[int],
    prime: int,
    r_value: int,
    t_value: int,
    mode: str,
    numerator_shift: int = 0,
) -> int:
    answer = 0
    for degree, coefficient in enumerate(poly):
        denominator = prime + r_value + t_value + degree + 1
        if denominator % prime:
            answer += (
                coefficient
                * mode_value(mode, denominator + numerator_shift)
                * pow(denominator, -2, prime)
            )
    return answer % prime


def u_ell_mod(
    poly: list[int], prime: int, r_value: int, t_value: int, modulus: int
) -> int:
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    return (
        4 * epsilon * u_mode_mod(poly, prime, r_value, t_value, "cos", modulus)
        - 2 * u_mode_mod(poly, prime, r_value, t_value, "sin", modulus)
    ) % modulus


def v_ell_mod(poly: list[int], prime: int, r_value: int, t_value: int) -> int:
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    return (
        4 * epsilon * v_mode_mod(poly, prime, r_value, t_value, "cos")
        - 2 * v_mode_mod(poly, prime, r_value, t_value, "sin")
    ) % prime


def mat_mul(left: list[list[int]], right: list[list[int]], prime: int) -> list[list[int]]:
    return [
        [
            sum(left[row][inner] * right[inner][column] for inner in range(len(right))) % prime
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def mat_vec(matrix: list[list[int]], vector: list[int], prime: int) -> list[int]:
    return [sum(row[index] * vector[index] for index in range(len(vector))) % prime for row in matrix]


def determinant_3(matrix: list[list[int]], prime: int) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    ) % prime


def inverse_3(matrix: list[list[int]], prime: int) -> list[list[int]]:
    determinant = determinant_3(matrix, prime)
    if not determinant:
        raise ZeroDivisionError((prime, matrix))
    inverse_det = pow(determinant, -1, prime)
    cofactors = [
        [
            (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]),
            -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
            (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]),
        ],
        [
            -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]),
            (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]),
            -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]),
        ],
        [
            (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]),
            -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]),
            (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]),
        ],
    ]
    return [
        [cofactors[column][row] * inverse_det % prime for column in range(3)]
        for row in range(3)
    ]


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0]) if work else 0):
        pivot = next((row for row in range(rank, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                scalar = work[row][column]
                work[row] = [
                    (work[row][index] - scalar * work[rank][index]) % prime
                    for index in range(len(work[row]))
                ]
        rank += 1
        if rank == len(work):
            break
    return rank


def endpoint_maps(
    poly: list[int], prime: int, r_value: int, s_value: int
) -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    terminal = 2 * s_value + 1
    phi = [
        [u_mode_mod(poly, prime, r_value, terminal + row, mode, prime) for mode in MODES]
        for row in range(3)
    ]
    psi = [
        [v_mode_mod(poly, prime, r_value, terminal + row, mode) for mode in MODES]
        for row in range(3)
    ]
    inverse = inverse_3(phi, prime)
    k_matrix = mat_mul(psi, inverse, prime)
    if mat_mul(k_matrix, phi, prime) != psi:
        raise AssertionError((prime, r_value, s_value, "K Phi"))
    if rank_mod(phi + psi, prime) != 3:
        raise AssertionError((prime, r_value, s_value, "stacked rank"))
    return phi, psi, k_matrix


def recurrence_check(
    poly: list[int], prime: int, r_value: int, s_value: int, t_value: int, mode: str
) -> bool:
    u_values = [u_mode_mod(poly, prime, r_value, t_value + offset, mode, prime) for offset in range(4)]
    v_values = [v_mode_mod(poly, prime, r_value, t_value + offset, mode) for offset in range(4)]
    a_value = (prime + 2 * r_value + 4 * s_value + t_value + 2) % prime
    b_value = (prime + r_value + t_value + 1) % prime
    c_value = (prime + 2 * r_value + t_value + 2) % prime
    d_value = (prime + r_value + 4 * s_value + t_value + 1) % prime
    left = (
        b_value * v_values[0]
        - c_value * v_values[1]
        + d_value * v_values[2]
        - a_value * v_values[3]
    ) % prime
    right = (u_values[0] - u_values[1] + u_values[2] - u_values[3]) % prime
    if left != right:
        raise AssertionError((prime, r_value, s_value, t_value, mode, left, right))
    if a_value == 0:
        predicted_u3 = (
            u_values[0]
            - u_values[1]
            + u_values[2]
            - b_value * v_values[0]
            + c_value * v_values[1]
            - d_value * v_values[2]
        ) % prime
        if predicted_u3 != u_values[3]:
            raise AssertionError((prime, t_value, mode, "terminal free digit"))
        return True
    return False


def phase_check(
    poly: list[int], prime: int, r_value: int, t_value: int, mode: str
) -> int:
    modulus = prime * prime
    checks = 0
    for multiple in (1, 2, 4):
        shifted_u = u_mode_mod(
            poly, prime, r_value, t_value + multiple * prime, mode, modulus
        )
        twisted_u = u_mode_mod(
            poly,
            prime,
            r_value,
            t_value,
            mode,
            modulus,
            numerator_shift=multiple * prime,
        )
        twisted_v = v_mode_mod(
            poly,
            prime,
            r_value,
            t_value,
            mode,
            numerator_shift=multiple * prime,
        )
        if (shifted_u - twisted_u + multiple * prime * twisted_v) % modulus:
            raise AssertionError((prime, r_value, t_value, mode, multiple, "phase U"))
        shifted_v = v_mode_mod(
            poly, prime, r_value, t_value + multiple * prime, mode
        )
        if shifted_v != twisted_v:
            raise AssertionError((prime, r_value, t_value, mode, multiple, "phase V"))
        checks += 2
    return checks


def row_digest(rows: list[list[int]]) -> str:
    payload = "".join(
        ",".join(str(value) for value in row) + "\n" for row in rows
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def build_certificate(direct_limit: int, map_limit: int) -> dict:
    dependency_hashes = {
        name: sha256_file(resolve_dependency(name)) for name in DEPENDENCIES
    }
    if dependency_hashes != DEPENDENCIES:
        raise AssertionError((dependency_hashes, DEPENDENCIES))

    direct_rows = 0
    recurrence_checks = 0
    terminal_checks = 0
    phase_checks = 0
    sample_rows = []
    for prime, r_value, s_value in rows_upto(direct_limit):
        poly = w_polynomial(r_value, s_value)
        terminal = 2 * s_value + 1
        t_values = set(range(0, terminal + 5))
        for a_value in range(2, 6):
            terminal_index = terminal + (a_value - 2) * prime
            t_values.update((terminal_index - 1, terminal_index, terminal_index + 1))
        for mode in MODES:
            for t_value in sorted(t_values):
                is_terminal = recurrence_check(
                    poly, prime, r_value, s_value, t_value, mode
                )
                recurrence_checks += 1
                terminal_checks += is_terminal
            for t_value in (0, terminal, terminal + 1, terminal + 2):
                phase_checks += phase_check(poly, prime, r_value, t_value, mode)

        phi, psi, k_matrix = endpoint_maps(poly, prime, r_value, s_value)
        terminal_vectors = 0
        for a_value in range(2, 6):
            t_value = terminal + (a_value - 2) * prime
            for mode_index, mode in enumerate(MODES):
                y_vector = [
                    u_mode_mod(poly, prime, r_value, t_value + offset, mode, prime)
                    for offset in range(3)
                ]
                v_vector = [
                    v_mode_mod(poly, prime, r_value, t_value + offset, mode)
                    for offset in range(3)
                ]
                if mat_vec(k_matrix, y_vector, prime) != v_vector:
                    raise AssertionError((prime, r_value, s_value, a_value, mode, "K phase"))
                terminal_vectors += 1

        # The actual numerator ell_(N-1)=4 epsilon cos(N)-2 sin(N).
        for a_value in range(2, 4):
            t_value = terminal + (a_value - 2) * prime
            y_value = [u_ell_mod(poly, prime, r_value, t_value + offset, prime * prime) for offset in range(3)]
            v_value = [v_ell_mod(poly, prime, r_value, t_value + offset) for offset in range(3)]
            y_two = [u_ell_mod(poly, prime, r_value, t_value + 2 * prime + offset, prime * prime) for offset in range(3)]
            y_four = [u_ell_mod(poly, prime, r_value, t_value + 4 * prime + offset, prime * prime) for offset in range(3)]
            if any((y_two[index] + y_value[index] - 2 * prime * v_value[index]) % (prime * prime) for index in range(3)):
                raise AssertionError((prime, a_value, "actual 2p closure"))
            if any((y_four[index] - y_value[index] + 4 * prime * v_value[index]) % (prime * prime) for index in range(3)):
                raise AssertionError((prime, a_value, "actual 4p closure"))

        if len(sample_rows) < 3:
            sample_rows.append({
                "row": [prime, r_value, s_value],
                "det_phi": determinant_3(phi, prime),
                "K": k_matrix,
                "terminal_mode_vectors": terminal_vectors,
            })
        direct_rows += 1

    map_rows = 0
    k_rows: list[list[int]] = []
    psi_rank_counts = [0, 0, 0, 0]
    for prime, r_value, s_value in rows_upto(map_limit):
        poly = w_polynomial(r_value, s_value)
        phi, psi, k_matrix = endpoint_maps(poly, prime, r_value, s_value)
        psi_rank_counts[rank_mod(psi, prime)] += 1
        k_rows.append(
            [prime, r_value, s_value, determinant_3(phi, prime)]
            + [entry for row in k_matrix for entry in row]
        )
        map_rows += 1

    if direct_limit == 151 and direct_rows != 184:
        raise AssertionError(direct_rows)
    if map_limit == 601 and map_rows != 2435:
        raise AssertionError(map_rows)

    return {
        "item": 238,
        "title": "squared-denominator recurrence and corrected lifted phase closure",
        "parameters": {
            "row": "p=2r+6s+3, r even positive, s positive",
            "direct_limit": direct_limit,
            "endpoint_map_limit": map_limit,
        },
        "proved": {
            "coupled_recurrence": (
                "B_t v_t-C_t v_(t+1)+D_t v_(t+2)-A_t v_(t+3)="
                "u_t-u_(t+1)+u_(t+2)-u_(t+3) mod p"
            ),
            "terminal_law": (
                "at t_a=2s+1+(a-2)p, A_t=0 mod p; the v equation determines "
                "the formerly free u_(t+3), while v_(t+3) remains free"
            ),
            "arbitrary_mode_phase_law": (
                "U_(t+kp)(q)=U_t(sigma^k q)-kp V_t(sigma^k q) mod p^2; "
                "V_(t+kp)(q)=V_t(sigma^k q) mod p for k=1,2,4"
            ),
            "actual_closure": (
                "for q=ell, U_(t+2p)+U_t=2pV_t and U_(t+4p)-U_t=-4pV_t mod p^2"
            ),
            "mode_redundancy": (
                "on E=span(1,cos(pi n/2),sin(pi n/2)), Phi is invertible and "
                "K=Psi Phi^-1 gives V_a=K*bar(U_a) at every terminal phase"
            ),
            "scoped_no_go": (
                "v adds no independent endpoint Fourier mode and one terminal adds no scalar "
                "compatibility; relation to the extra p^3/Omega^W gate is not proved"
            ),
        },
        "exact_replay": {
            "rows": direct_rows,
            "coupled_recurrence_checks": recurrence_checks,
            "terminal_free_digit_checks": terminal_checks,
            "arbitrary_mode_phase_checks": phase_checks,
            "sample_rows": sample_rows,
        },
        "exact_finite_only": {
            "endpoint_map_rows": map_rows,
            "psi_rank_counts_rank_0_through_3": psi_rank_counts,
            "K_stream_sha256": row_digest(k_rows),
        },
        "open": [
            "whether the corrected carry yields an additional invariant after imposing p^3 divisibility/Omega^W=0",
            "a full p^2 lift of the Item233 terminal-residual redundancy identity",
            "any all-prime common-log exclusion or Route-1 rate consequence",
        ],
        "dependencies": dependency_hashes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--direct-limit", type=int, default=151)
    parser.add_argument("--map-limit", type=int, default=601)
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.direct_limit, arguments.map_limit)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "output": str(arguments.output),
        "direct_rows": certificate["exact_replay"]["rows"],
        "map_rows": certificate["exact_finite_only"]["endpoint_map_rows"],
        "recurrence_checks": certificate["exact_replay"]["coupled_recurrence_checks"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
