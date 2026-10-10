#!/usr/bin/env python3
"""Exact checker for Item 240's j=1 Witt/squared-endpoint bridge."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item240_j1_witt_endpoint_bridge_certificate.json"

DEPENDENCIES = {
    "sources/item234_j1_first_witt_report.md":
        "9bd5bb91fe813622db0c15d8bfc25714bcefb00512ed8f5eafddacd8cfb9b016",
    "scripts/item234_j1_first_witt_certificate.py":
        "8d41a5a73e9467cf4c998d3e345767c04c68ab6467605290480825b15b08e125",
    "results/item234_j1_first_witt_certificate.json":
        "6797c1f2cd072ec92d311e01b596c3ac95888ce9b761bc325a625ef6f9f0c748",
    "sources/item238_j1_squared_carry_report.md":
        "5c2cc3ab4009bef750503588452c0f25e3f33754476edf1fcdba13454fa95c98",
    "scripts/item238_j1_squared_carry_certificate.py":
        "a2a2519d4f18c9b3bfa4b29c29068fb81b1d53e2abab4cc10cae3520d75cea04",
    "results/item238_j1_squared_carry_certificate.json":
        "a12fd42e9d53b4f50a595b65d2146b16423c8547a2f3348220fc33d976e51b31",
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


def load_module(name: str, relative_name: str):
    path = resolve_dependency(relative_name)
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def mode_value(mode: int, integer: int) -> int:
    values = (
        (1, 1, 1, 1),
        (1, 0, -1, 0),
        (0, 1, 0, -1),
    )
    return values[mode][integer % 4]


def tower_value(
    poly: list[int],
    prime: int,
    r_value: int,
    t_value: int,
    mode: int,
    power: int,
) -> int:
    answer = 0
    for degree, coefficient in enumerate(poly):
        denominator = prime + r_value + t_value + degree + 1
        if denominator % prime:
            answer += (
                coefficient
                * mode_value(mode, denominator)
                * pow(denominator, -power, prime)
            )
    return answer % prime


def mat_mul(left: list[list[int]], right: list[list[int]], prime: int) -> list[list[int]]:
    return [
        [
            sum(left[row][inner] * right[inner][column] for inner in range(len(right))) % prime
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def inverse_3(matrix: list[list[int]], prime: int) -> list[list[int]]:
    determinant = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    ) % prime
    if not determinant:
        raise ZeroDivisionError((prime, matrix))
    inverse_det = pow(determinant, -1, prime)
    cofactors = [
        [
            matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1],
            -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
            matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0],
        ],
        [
            -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]),
            matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0],
            -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]),
        ],
        [
            matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1],
            -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]),
            matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0],
        ],
    ]
    return [
        [cofactors[column][row] * inverse_det % prime for column in range(3)]
        for row in range(3)
    ]


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
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
                    for index in range(columns)
                ]
        rank += 1
        if rank == len(work):
            break
    return rank


def determinant_mod(matrix: list[list[int]], prime: int) -> int:
    """Return the determinant by exact elimination in F_prime."""
    work = [[value % prime for value in row] for row in matrix]
    determinant = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
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
            scalar = work[row][column] * inverse % prime
            if scalar:
                for index in range(column, len(work)):
                    work[row][index] = (
                        work[row][index] - scalar * work[column][index]
                    ) % prime
    return determinant % prime


def first_nonzero_maximal_minor(
    matrix: list[list[int]], prime: int
) -> tuple[list[int], int]:
    """Find a row set certifying full column rank."""
    size = len(matrix[0])
    for row_indices in itertools.combinations(range(len(matrix)), size):
        determinant = determinant_mod([matrix[index] for index in row_indices], prime)
        if determinant:
            return list(row_indices), determinant
    raise AssertionError((prime, len(matrix), size, "no full-column-rank minor"))


def add_frobenius_factor(
    output: list[int],
    kernel: list[int],
    a_power: int,
    b_power: int,
    prime: int,
    target: int,
    scalar: int,
    item234,
) -> None:
    sections = item234.frobenius_sections(a_power, b_power, prime, target, prime)
    for shift, section_coefficient in sections.items():
        for degree, coefficient in enumerate(kernel):
            if shift + degree <= target:
                output[shift + degree] = (
                    output[shift + degree]
                    + scalar * section_coefficient * coefficient
                ) % prime


def e_kernel(prime: int, q_value: int, item234) -> list[int]:
    target = 3 * prime - q_value - 1
    a_zero, a_one, b_zero, b_one = item234.harmonic_digits(prime)
    aa = item234.convolution_mod(a_zero, a_zero, prime, target)
    ab = item234.convolution_mod(a_zero, b_zero, prime, target)
    bb = item234.convolution_mod(b_zero, b_zero, prime, target)
    output = [0] * (target + 1)
    add_frobenius_factor(output, a_one, 3, 3, prime, target, 4, item234)
    add_frobenius_factor(output, b_one, 4, 4, prime, target, -3, item234)
    add_frobenius_factor(output, aa, 2, 3, prime, target, 6, item234)
    add_frobenius_factor(output, ab, 3, 4, prime, target, -12, item234)
    add_frobenius_factor(output, bb, 4, 5, prime, target, 6, item234)
    return output


def e_functional_direct(
    poly: list[int], prime: int, q_value: int, item234
) -> int:
    """Independent direct convolution formula for Item 234's E functional."""
    target = 3 * prime - q_value - 1
    reduced_poly = [value % prime for value in poly]
    a_zero, a_one, b_zero, b_one = item234.harmonic_digits(prime)
    aa = item234.convolution_mod(a_zero, a_zero, prime, target)
    ab = item234.convolution_mod(a_zero, b_zero, prime, target)
    bb = item234.convolution_mod(b_zero, b_zero, prime, target)
    return (
        4 * item234.sectioned_coefficient(3, 3, a_one, reduced_poly, target, prime)
        - 3 * item234.sectioned_coefficient(4, 4, b_one, reduced_poly, target, prime)
        + 6 * item234.sectioned_coefficient(2, 3, aa, reduced_poly, target, prime)
        - 12 * item234.sectioned_coefficient(3, 4, ab, reduced_poly, target, prime)
        + 6 * item234.sectioned_coefficient(4, 5, bb, reduced_poly, target, prime)
    ) % prime


def functional_matrix(
    prime: int,
    h_value: int,
    s_value: int,
    nu: int,
    maximum_power: int,
    item234,
) -> tuple[list[list[int]], list[int]]:
    q_value = 2 * s_value - nu
    degree = 2 * h_value + 4 * s_value + 1 + nu
    target = 3 * prime - q_value - 1
    kernel = e_kernel(prime, q_value, item234)
    e_weights = [kernel[target - index] for index in range(degree + 1)]
    denominators = [2 * prime - q_value - 1 - index for index in range(degree + 1)]
    columns = []
    for power in range(1, maximum_power + 1):
        for mode in range(3):
            columns.append([
                mode_value(mode, denominator) * pow(denominator, -power, prime) % prime
                for denominator in denominators
            ])
    matrix = [
        [columns[column][row] for column in range(len(columns))] + [e_weights[row]]
        for row in range(degree + 1)
    ]
    return matrix, denominators


def matrix_digest(matrix: list[list[int]]) -> str:
    payload = "".join(
        ",".join(str(value) for value in row) + "\n" for row in matrix
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def matrix_row_digests(matrix: list[list[int]]) -> list[str]:
    return [
        hashlib.sha256(
            (",".join(str(value) for value in row) + "\n").encode("ascii")
        ).hexdigest()
        for row in matrix
    ]


def build_certificate(direct_limit: int, tower_power: int) -> dict:
    dependency_hashes = {
        name: sha256_file(resolve_dependency(name)) for name in DEPENDENCIES
    }
    if dependency_hashes != DEPENDENCIES:
        raise AssertionError((dependency_hashes, DEPENDENCIES))

    item234 = load_module("item234_frozen", "scripts/item234_j1_first_witt_certificate.py")

    rows = 0
    coordinates = 0
    j_identity_checks = 0
    tower_recurrence_checks = 0
    tower_factorization_checks = 0
    e_actual_polynomial_checks = 0
    gate_records = []
    for prime, h_value, s_value in item234.rows_upto(direct_limit):
        r_value = 2 * h_value
        poly = item234.w_polynomial(h_value, s_value)
        epsilon = -1 if ((prime - 1) // 2) % 2 else 1
        terminal = 2 * s_value + 1

        phi_one = [
            [tower_value(poly, prime, r_value, terminal + row, mode, 1) for mode in range(3)]
            for row in range(3)
        ]
        inverse_phi = inverse_3(phi_one, prime)
        for power in range(2, tower_power + 1):
            phi_power = [
                [tower_value(poly, prime, r_value, terminal + row, mode, power) for mode in range(3)]
                for row in range(3)
            ]
            k_power = mat_mul(phi_power, inverse_phi, prime)
            if mat_mul(k_power, phi_one, prime) != phi_power:
                raise AssertionError((prime, h_value, s_value, power, "factorization"))
            tower_factorization_checks += 1

        for mode in range(3):
            test_indices = (0, terminal, terminal + 1, terminal + prime, terminal + 2 * prime)
            for power in range(2, tower_power + 1):
                for t_value in test_indices:
                    current = [
                        tower_value(poly, prime, r_value, t_value + offset, mode, power)
                        for offset in range(4)
                    ]
                    previous = [
                        tower_value(poly, prime, r_value, t_value + offset, mode, power - 1)
                        for offset in range(4)
                    ]
                    a_value = (prime + 2 * r_value + 4 * s_value + t_value + 2) % prime
                    b_value = (prime + r_value + t_value + 1) % prime
                    c_value = (prime + 2 * r_value + t_value + 2) % prime
                    d_value = (prime + r_value + 4 * s_value + t_value + 1) % prime
                    left = (
                        b_value * current[0]
                        - c_value * current[1]
                        + d_value * current[2]
                        - a_value * current[3]
                    ) % prime
                    right = (
                        previous[0] - previous[1] + previous[2] - previous[3]
                    ) % prime
                    if left != right:
                        raise AssertionError((prime, h_value, s_value, mode, power, t_value))
                    tower_recurrence_checks += 1

        q_pair = item234.q_pair_fast(prime, h_value, s_value)
        for nu in (0, 1):
            q_value = 2 * s_value - nu
            p_poly = item234.p_polynomial(prime, h_value, s_value, nu)
            target = 3 * prime - q_value - 1
            kernel = e_kernel(prime, q_value, item234)
            kernel_value = sum(
                coefficient * kernel[target - degree]
                for degree, coefficient in enumerate(p_poly)
            ) % prime
            frozen_value = item234.e_digit(prime, h_value, s_value, nu)
            direct_value = e_functional_direct(p_poly, prime, q_value, item234)
            if kernel_value != frozen_value or direct_value != frozen_value:
                raise AssertionError((
                    prime, h_value, s_value, nu,
                    kernel_value, direct_value, frozen_value, "E functional",
                ))
            e_actual_polynomial_checks += 1

            q_exact, reflection, moment, hermite, h_one = item234.q_r_m_j(
                prime, h_value, s_value, nu
            )
            multiplier = (1, 1, 1, 1) if nu == 0 else (1, 4, 6, 4, 1)
            sine_square = sum(
                coefficient * tower_value(poly, prime, r_value, shift, 2, 2)
                for shift, coefficient in enumerate(multiplier)
            ) % prime
            hermite_mod = item234.fraction_mod(hermite, prime)
            if hermite_mod != 2 * epsilon * sine_square % prime:
                raise AssertionError((prime, h_value, s_value, nu, "J bridge"))
            j_identity_checks += 1

            if q_pair[nu] == 0:
                e_value = item234.e_digit(prime, h_value, s_value, nu)
                moment_digit = item234.divided_fraction_mod(moment, prime)
                omega = (
                    -6 * epsilon * moment_digit
                    + 12 * epsilon * sine_square
                    + e_value
                ) % prime
                old_omega = (
                    6 * item234.divided_fraction_mod(q_exact, prime)
                    + 12 * item234.fraction_mod(reflection, prime)
                    + e_value
                ) % prime
                if omega != old_omega:
                    raise AssertionError((prime, h_value, s_value, nu, "Omega bridge"))
                compatibility_rhs = (
                    2 * sine_square + e_value * pow(6 * epsilon, -1, prime)
                ) % prime
                gate_records.append([
                    prime,
                    h_value,
                    s_value,
                    nu,
                    moment_digit,
                    sine_square,
                    e_value,
                    omega,
                    compatibility_rhs,
                ])
            coordinates += 1
        rows += 1

    witness_matrix, witness_denominators = functional_matrix(
        29, 5, 1, 1, 2, item234
    )
    witness_q = 1
    witness_target = 3 * 29 - witness_q - 1
    witness_kernel = e_kernel(29, witness_q, item234)
    e_basis_checks = 0
    for degree in range(17):
        basis = [0] * 17
        basis[degree] = 1
        kernel_weight = witness_kernel[witness_target - degree]
        direct_weight = e_functional_direct(basis, 29, witness_q, item234)
        if kernel_weight != direct_weight:
            raise AssertionError((degree, kernel_weight, direct_weight, "E basis"))
        e_basis_checks += 1
    tower_rank = rank_mod([row[:-1] for row in witness_matrix], 29)
    augmented_rank = rank_mod(witness_matrix, 29)
    if (len(witness_matrix), len(witness_matrix[0]), tower_rank, augmented_rank) != (
        17,
        7,
        6,
        7,
    ):
        raise AssertionError((len(witness_matrix), len(witness_matrix[0]), tower_rank, augmented_rank))
    tower_minor_rows, tower_minor_determinant = first_nonzero_maximal_minor(
        [row[:-1] for row in witness_matrix], 29
    )
    augmented_minor_rows, augmented_minor_determinant = first_nonzero_maximal_minor(
        witness_matrix, 29
    )

    bounded_evidence = []
    for bound in range(1, 13):
        matrix, _ = functional_matrix(109, 10, 11, 0, bound, item234)
        base_rank = rank_mod([row[:-1] for row in matrix], 109)
        full_rank = rank_mod(matrix, 109)
        bounded_evidence.append([bound, base_rank, full_rank])
        if full_rank != base_rank + 1:
            raise AssertionError((bound, base_rank, full_rank))

    if direct_limit == 151 and (rows, coordinates) != (184, 368):
        raise AssertionError((rows, coordinates))

    return {
        "item": 240,
        "title": "j=1 Witt digit versus squared endpoint tower",
        "parameters": {
            "row": "p=4h+6s+3, r=2h, h,s>=1",
            "direct_limit": direct_limit,
            "tower_power": tower_power,
        },
        "proved": {
            "termwise_J_bridge": (
                "J0=2epsilon(vs0+vs1+vs2+vs3), "
                "J1=2epsilon(vs0+4vs1+6vs2+4vs3+vs4) mod p"
            ),
            "Omega_bridge_on_original_gate": (
                "Omega^W_nu=-6epsilon M_nu^(1)+12epsilon V^s_nu+E_nu mod p"
            ),
            "extra_p3_compatibility": (
                "on p^2|C_nu, p^3|C_nu iff "
                "M_nu^(1)=2V^s_nu+(6epsilon)^(-1)E_nu mod p"
            ),
            "all_power_tower_recurrence": (
                "Rbar_t(V^(k))=V_t^(k-1)-V_(t+1)^(k-1)+"
                "V_(t+2)^(k-1)-V_(t+3)^(k-1), k>=2"
            ),
            "tower_mode_factorization": (
                "Phi_k=K_k Phi_1 on the three endpoint modes for every fixed k; "
                "no denominator-power level adds an endpoint Fourier mode"
            ),
            "u_v_universal_linear_no_go": (
                "over F_29 on degree<=16 polynomial inputs at (p,h,s,nu)=(29,5,1,1), "
                "the six power-1/2 endpoint functionals have rank 6 and adjoining E has rank 7"
            ),
        },
        "exact_replay": {
            "rows": rows,
            "coordinates": coordinates,
            "J_identity_checks": j_identity_checks,
            "tower_recurrence_checks": tower_recurrence_checks,
            "tower_factorization_checks": tower_factorization_checks,
            "E_actual_polynomial_checks": e_actual_polynomial_checks,
            "first_gate_records": gate_records,
        },
        "rank_witness": {
            "scope": (
                "universal F_29-linear functionals on coefficient vectors of degree <=16; "
                "not actual-family or nonlinear identities"
            ),
            "row": [29, 5, 1, 1],
            "denominators": witness_denominators,
            "column_schema": [
                "q0/D", "qc/D", "qs/D", "q0/D^2", "qc/D^2", "qs/D^2", "E"
            ],
            "matrix": witness_matrix,
            "tower_rank": tower_rank,
            "augmented_rank": augmented_rank,
            "tower_minor": {
                "row_indices_zero_based": tower_minor_rows,
                "determinant_mod_29": tower_minor_determinant,
            },
            "augmented_minor": {
                "row_indices_zero_based": augmented_minor_rows,
                "determinant_mod_29": augmented_minor_determinant,
            },
            "row_sha256": matrix_row_digests(witness_matrix),
            "row_stream_encoding": "comma-separated decimal entries, LF after every row",
            "matrix_sha256": matrix_digest(witness_matrix),
            "E_basis_vector_direct_convolution_checks": e_basis_checks,
        },
        "exact_finite_only": {
            "p109_degree65_power_bounds_1_through_12": bounded_evidence,
            "interpretation": (
                "E stays outside the tested endpoint denominator-power spans; "
                "this does not prove an all-power theorem"
            ),
        },
        "open": [
            "an actual-family-specific or nonlinear formula eliminating E_nu",
            "whether E admits a finite enlarged recurrence with a genuinely new endpoint mode",
            "an all-power obstruction beyond the exact u/v rank witness and finite K<=12 evidence",
            "any all-prime common-log exclusion or Route-1 rate consequence",
        ],
        "dependencies": dependency_hashes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--direct-limit", type=int, default=151)
    parser.add_argument("--tower-power", type=int, default=6)
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.direct_limit, arguments.tower_power)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "output": str(arguments.output),
        "rows": certificate["exact_replay"]["rows"],
        "J_checks": certificate["exact_replay"]["J_identity_checks"],
        "tower_checks": certificate["exact_replay"]["tower_recurrence_checks"],
        "witness_ranks": [
            certificate["rank_witness"]["tower_rank"],
            certificate["rank_witness"]["augmented_rank"],
        ],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
