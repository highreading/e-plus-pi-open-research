#!/usr/bin/env python3
"""Exact checker for Item 242's j=1 E-kernel phase realization."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item242_j1_E_kernel_state_certificate.json"

DEPENDENCIES = {
    "sources/item234_j1_first_witt_report.md":
        "9bd5bb91fe813622db0c15d8bfc25714bcefb00512ed8f5eafddacd8cfb9b016",
    "scripts/item234_j1_first_witt_certificate.py":
        "8d41a5a73e9467cf4c998d3e345767c04c68ab6467605290480825b15b08e125",
    "results/item234_j1_first_witt_certificate.json":
        "6797c1f2cd072ec92d311e01b596c3ac95888ce9b761bc325a625ef6f9f0c748",
    "sources/item240_j1_witt_endpoint_bridge_report.md":
        "b0c7e8c1504ac5df52c71088f940cc83887d589997f6ff98a028906d920eebb7",
    "scripts/item240_j1_witt_endpoint_bridge_certificate.py":
        "621c82355a760e43d228317ed4ed9da2d5fc1bbab722b6ecfcf8bc106cebdff0",
    "results/item240_j1_witt_endpoint_bridge_certificate.json":
        "f5a420207f9b42f90743b369ff6aaf5eb2ff660a31e018a00a80deaefb944430",
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


def trim(poly: list[int]) -> list[int]:
    answer = poly[:]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def poly_add(left: list[int], right: list[int], prime: int) -> list[int]:
    answer = [0] * max(len(left), len(right))
    for index in range(len(answer)):
        answer[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(answer)


def poly_scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([scalar * value % prime for value in poly])


def poly_mul(left: list[int], right: list[int], prime: int) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        if left_value:
            for right_index, right_value in enumerate(right):
                answer[left_index + right_index] = (
                    answer[left_index + right_index] + left_value * right_value
                ) % prime
    return trim(answer)


def spaced_binomial(power: int, spacing: int, sign: int, prime: int) -> list[int]:
    answer = [0] * (power * spacing + 1)
    for index in range(power + 1):
        answer[index * spacing] = (
            math.comb(power, index) * sign ** index
        ) % prime
    return trim(answer)


def poly_divmod(
    numerator: list[int], denominator: list[int], prime: int
) -> tuple[list[int], list[int]]:
    work = trim([value % prime for value in numerator])
    divisor = trim([value % prime for value in denominator])
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    while len(work) >= len(divisor) and work != [0]:
        offset = len(work) - len(divisor)
        scalar = work[-1] * pow(divisor[-1], -1, prime) % prime
        quotient[offset] = scalar
        for index, value in enumerate(divisor):
            work[offset + index] = (work[offset + index] - scalar * value) % prime
        work = trim(work)
    return trim(quotient), work


def factor_multiplicity(poly: list[int], factor: list[int], prime: int) -> int:
    multiplicity = 0
    current = trim(poly)
    while current != [0]:
        quotient, remainder = poly_divmod(current, factor, prime)
        if remainder != [0]:
            break
        multiplicity += 1
        current = quotient
    return multiplicity


def kernel_numerator(prime: int, item234) -> tuple[list[int], dict[str, list[int]]]:
    """Return R_E with H_E=R_E/(1+z^(2p))^5 over F_p."""
    a_zero, a_one, b_zero, b_one = item234.harmonic_digits(prime)
    aa = poly_mul(a_zero, a_zero, prime)
    ab = poly_mul(a_zero, b_zero, prime)
    bb = poly_mul(b_zero, b_zero, prime)
    u_two = spaced_binomial(2, prime, -1, prime)
    u_three = spaced_binomial(3, prime, -1, prime)
    u_four = spaced_binomial(4, prime, -1, prime)
    v_one = spaced_binomial(1, 2 * prime, 1, prime)
    v_two = spaced_binomial(2, 2 * prime, 1, prime)
    terms = (
        poly_scale(poly_mul(poly_mul(u_three, v_two, prime), a_one, prime), 4, prime),
        poly_scale(poly_mul(poly_mul(u_four, v_one, prime), b_one, prime), -3, prime),
        poly_scale(poly_mul(poly_mul(u_two, v_two, prime), aa, prime), 6, prime),
        poly_scale(poly_mul(poly_mul(u_three, v_one, prime), ab, prime), -12, prime),
        poly_scale(poly_mul(u_four, bb, prime), 6, prime),
    )
    numerator = [0]
    for term in terms:
        numerator = poly_add(numerator, term, prime)
    return numerator, {
        "A0": a_zero,
        "B0": b_zero,
        "U4": u_four,
        "V": v_one,
        "B0_squared": bb,
    }


def rational_series(
    numerator: list[int], prime: int, maximum: int
) -> list[int]:
    """Expand numerator/(1+z^(2p))^5 through maximum."""
    answer = [0] * (maximum + 1)
    for index in range(maximum // (2 * prime) + 1):
        shift = 2 * prime * index
        scalar = (-1) ** index * math.comb(index + 4, 4)
        for degree, value in enumerate(numerator):
            if shift + degree > maximum:
                break
            answer[shift + degree] = (
                answer[shift + degree] + scalar * value
            ) % prime
    return answer


def rational_coefficient(numerator: list[int], prime: int, degree: int) -> int:
    if degree < 0:
        return 0
    answer = 0
    for index in range(degree // (2 * prime) + 1):
        source = degree - 2 * prime * index
        if source < len(numerator):
            answer += (
                (-1) ** index
                * math.comb(index + 4, 4)
                * numerator[source]
            )
    return answer % prime


def mode_value(mode: int, integer: int) -> int:
    modes = (
        (1, 1, 1, 1),
        (1, 0, -1, 0),
        (0, 1, 0, -1),
    )
    return modes[mode][integer % 4]


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
    return rank


def determinant_mod(matrix: list[list[int]], prime: int) -> int:
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
            for index in range(column, len(work)):
                work[row][index] = (
                    work[row][index] - scalar * work[column][index]
                ) % prime
    return determinant % prime


def first_nonzero_maximal_minor(
    matrix: list[list[int]], prime: int
) -> tuple[list[int], int]:
    size = len(matrix[0])
    for row_indices in itertools.combinations(range(len(matrix)), size):
        determinant = determinant_mod([matrix[index] for index in row_indices], prime)
        if determinant:
            return list(row_indices), determinant
    raise AssertionError((prime, len(matrix), size, "no full-column-rank minor"))


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


def observation_matrix(
    prime: int,
    h_value: int,
    s_value: int,
    maximum_power: int,
    numerator: list[int],
) -> list[list[int]]:
    r_value = 2 * h_value
    degree = r_value + 4 * s_value - 2
    target_zero = 3 * prime - 2 * s_value - 1
    series = rational_series(numerator, prime, target_zero + 1)
    matrix = []
    for degree_index in range(degree + 1):
        denominator = prime + r_value + degree_index + 1
        row = []
        for power in range(1, maximum_power + 1):
            row.extend(
                mode_value(mode, denominator) * pow(denominator, -power, prime) % prime
                for mode in range(3)
            )
        e_zero = sum(
            series[target_zero - shift - degree_index] for shift in range(4)
        ) % prime
        e_one = sum(
            (1, 4, 6, 4, 1)[shift]
            * series[target_zero + 1 - shift - degree_index]
            for shift in range(5)
        ) % prime
        matrix.append(row + [e_zero, e_one])
    return matrix


def build_certificate(direct_limit: int) -> dict:
    dependency_hashes = {
        name: sha256_file(resolve_dependency(name)) for name in DEPENDENCIES
    }
    if dependency_hashes != DEPENDENCIES:
        raise AssertionError((dependency_hashes, DEPENDENCIES))

    item234 = load_module("item234_frozen", "scripts/item234_j1_first_witt_certificate.py")
    item240 = load_module("item240_frozen", "scripts/item240_j1_witt_endpoint_bridge_certificate.py")

    cache: dict[int, tuple[list[int], dict[str, list[int]]]] = {}
    rows = 0
    coordinates = 0
    kernel_identity_checks = 0
    observation_checks = 0
    phase_recurrence_checks = 0
    minimal_denominator_checks = 0
    prime_structure_checks = 0
    checked_primes: set[int] = set()

    recurrence_coefficients = (1, 5, 10, 10, 5, 1)
    for prime, h_value, s_value in item234.rows_upto(direct_limit):
        if prime not in cache:
            cache[prime] = kernel_numerator(prime, item234)
        numerator, pieces = cache[prime]
        if prime not in checked_primes:
            if len(numerator) - 1 > 8 * prime - 1:
                raise AssertionError((prime, len(numerator) - 1, "degree R"))
            factor = [1, 0, 1]
            if factor_multiplicity(pieces["B0"], factor, prime) != 1:
                raise AssertionError((prime, "B0 multiplicity"))
            if factor_multiplicity(numerator, factor, prime) != 2:
                raise AssertionError((prime, "R multiplicity"))
            right = poly_scale(
                poly_mul(pieces["U4"], pieces["B0_squared"], prime),
                6,
                prime,
            )
            _, left_remainder = poly_divmod(numerator, pieces["V"], prime)
            _, right_remainder = poly_divmod(right, pieces["V"], prime)
            if left_remainder != right_remainder:
                raise AssertionError((prime, "R mod V"))
            prime_structure_checks += 1
            checked_primes.add(prime)

        r_value = 2 * h_value
        w_poly = [value % prime for value in item234.w_polynomial(h_value, s_value)]
        product_numerator = poly_mul(numerator, w_poly, prime)
        expected_multiplicity = 2 * s_value + 1
        actual_multiplicity = factor_multiplicity(
            product_numerator, [1, 0, 1], prime
        )
        if actual_multiplicity != expected_multiplicity or not expected_multiplicity < prime:
            raise AssertionError((
                prime, h_value, s_value,
                actual_multiplicity, expected_multiplicity,
                "minimal denominator",
            ))
        minimal_denominator_checks += 1

        target_zero = 3 * prime - 2 * s_value - 1
        maximum = target_zero + 1
        h_series = rational_series(numerator, prime, maximum)
        for nu in (0, 1):
            q_value = 2 * s_value - nu
            target = 3 * prime - q_value - 1
            independent_kernel = item240.e_kernel(prime, q_value, item234)
            if h_series[:target + 1] != independent_kernel:
                raise AssertionError((prime, h_value, s_value, nu, "kernel identity"))
            kernel_identity_checks += 1

        base_index = target_zero - 3
        e_values = []
        for offset in range(5):
            coefficient = 0
            degree = base_index + offset
            for w_degree, w_value in enumerate(w_poly):
                coefficient += w_value * h_series[degree - w_degree]
            e_values.append(coefficient % prime)
        e_zero = sum(e_values[:4]) % prime
        e_one = sum(
            coefficient * value
            for coefficient, value in zip((1, 4, 6, 4, 1), e_values)
        ) % prime
        frozen_pair = (
            item234.e_digit(prime, h_value, s_value, 0),
            item234.e_digit(prime, h_value, s_value, 1),
        )
        if (e_zero, e_one) != frozen_pair:
            raise AssertionError((prime, h_value, s_value, (e_zero, e_one), frozen_pair))
        observation_checks += 2

        phase_offsets = (0, 1, 2, 3, 4, 2 * s_value + 1)
        for offset in phase_offsets:
            recurrence = sum(
                coefficient
                * rational_coefficient(
                    product_numerator,
                    prime,
                    base_index + offset + 2 * prime * step,
                )
                for step, coefficient in enumerate(recurrence_coefficients)
            ) % prime
            if recurrence:
                raise AssertionError((prime, h_value, s_value, offset, recurrence))
            phase_recurrence_checks += 1

        coordinates += 2
        rows += 1

    if direct_limit == 151 and (rows, coordinates) != (184, 368):
        raise AssertionError((rows, coordinates))

    witness_numerator, _ = kernel_numerator(29, item234)
    witness = observation_matrix(29, 5, 1, 2, witness_numerator)
    base = [row[:6] for row in witness]
    first = [row[:7] for row in witness]
    ranks = (rank_mod(base, 29), rank_mod(first, 29), rank_mod(witness, 29))
    if (len(witness), len(witness[0]), ranks) != (13, 8, (6, 7, 8)):
        raise AssertionError((len(witness), len(witness[0]), ranks))
    base_rows, base_det = first_nonzero_maximal_minor(base, 29)
    first_rows, first_det = first_nonzero_maximal_minor(first, 29)
    full_rows, full_det = first_nonzero_maximal_minor(witness, 29)

    finite_numerator, _ = kernel_numerator(109, item234)
    bounded_ranks = []
    for power_bound in range(1, 13):
        matrix = observation_matrix(109, 10, 11, power_bound, finite_numerator)
        tower_rank = rank_mod([row[:-2] for row in matrix], 109)
        first_rank = rank_mod([row[:-1] for row in matrix], 109)
        both_rank = rank_mod(matrix, 109)
        bounded_ranks.append([power_bound, tower_rank, first_rank, both_rank])
        if (tower_rank, first_rank, both_rank) != (
            3 * power_bound,
            3 * power_bound + 1,
            3 * power_bound + 2,
        ):
            raise AssertionError((power_bound, tower_rank, first_rank, both_rank))

    return {
        "item": 242,
        "title": "finite phase realization of the j=1 E kernel",
        "parameters": {
            "row": "p=4h+6s+3, r=2h, h,s>=1",
            "direct_limit": direct_limit,
        },
        "proved": {
            "rational_kernel": (
                "H_E=R_E/(1+z^(2p))^5 with the explicit five-term numerator"
            ),
            "common_observations": (
                "E0=e0+e1+e2+e3 and E1=e0+4e1+6e2+4e3+e4"
            ),
            "phase_recurrence": (
                "(S_p^2+1)^5 e=0, i.e. e_(t+10p)+5e_(t+8p)+"
                "10e_(t+6p)+10e_(t+4p)+5e_(t+2p)+e_t=0"
            ),
            "minimal_global_phase_polynomial": (
                "the rootwise orders of R_E W are 2s+1<p; for each root "
                "some p-section retains its fifth denominator power, so the "
                "section-denominator lcm is (1+Z^2)^5 and has phase degree 10"
            ),
            "new_generalized_modes": (
                "relative to the semisimple +/-i endpoint pair, E adds eight "
                "generalized +/-i phase directions in the full kernel module"
            ),
            "scoped_uv_no_go": (
                "over F_29 on degree<=12 coefficient inputs, u/v has rank 6, "
                "adjoining E0 has rank 7, and adjoining E1 has rank 8"
            ),
        },
        "exact_replay": {
            "rows": rows,
            "coordinates": coordinates,
            "distinct_prime_structure_checks": prime_structure_checks,
            "kernel_identity_checks": kernel_identity_checks,
            "E_observation_checks": observation_checks,
            "phase_recurrence_checks": phase_recurrence_checks,
            "minimal_denominator_checks": minimal_denominator_checks,
        },
        "rank_witness": {
            "scope": (
                "universal F_29-linear functionals on degree<=12 coefficient "
                "inputs; not nonlinear or actual-binomial-family identities"
            ),
            "row": [29, 5, 1],
            "column_schema": [
                "q0/D", "qc/D", "qs/D",
                "q0/D^2", "qc/D^2", "qs/D^2",
                "E0", "E1",
            ],
            "matrix": witness,
            "ranks": list(ranks),
            "base_minor": {
                "row_indices_zero_based": base_rows,
                "determinant_mod_29": base_det,
            },
            "E0_minor": {
                "row_indices_zero_based": first_rows,
                "determinant_mod_29": first_det,
            },
            "E0_E1_minor": {
                "row_indices_zero_based": full_rows,
                "determinant_mod_29": full_det,
            },
            "row_sha256": matrix_row_digests(witness),
            "row_stream_encoding": "comma-separated decimal entries, LF after every row",
            "matrix_sha256": matrix_digest(witness),
        },
        "exact_finite_only": {
            "p109_degree62_power_bounds_1_through_12": bounded_ranks,
            "interpretation": (
                "both E observations stay independent of the tested denominator "
                "tower spans; this is not an all-power or all-row theorem"
            ),
        },
        "scoped_terminal_consequence": (
            "the p^3 equations fix two coordinates in the enlarged E state; "
            "the F_29 witness proves they do not reduce to universal linear "
            "constraints on u/v, but it does not prove actual-family independence"
        ),
        "open": [
            "a uniform small adjacent-t Pearson realization of the E kernel",
            "an actual-binomial-family or nonlinear elimination of E0,E1",
            "whether the p^3 gate gives an all-row terminal obstruction after all lift data",
            "any all-prime common-log exclusion or Route-1 rate consequence",
        ],
        "dependencies": dependency_hashes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--direct-limit", type=int, default=151)
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.direct_limit)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(arguments.output),
        "rows": certificate["exact_replay"]["rows"],
        "phase_checks": certificate["exact_replay"]["phase_recurrence_checks"],
        "rank_witness": certificate["rank_witness"]["ranks"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
