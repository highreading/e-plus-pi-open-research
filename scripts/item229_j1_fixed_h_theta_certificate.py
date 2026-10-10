#!/usr/bin/env python3
"""Deterministic certificate for Item 229's fixed-h Theta reduction.

The all-h theorem checked here is the polynomial Gosper decomposition of the
corrected Item 223 transfer determinant.  The attractive phase factorization
against Item 222 is deliberately recorded as finite exact evidence only.
Output has no clock, host, or absolute-path dependence.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item229_j1_fixed_h_theta_certificate.json"

DEPENDENCIES = {
    "scripts/item218_j1_common_log_certificate.py":
        "a238c5ca37263f2553da47bf3f21253aedf1c34f8c57458a4a274fc6cdc9029a",
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "scripts/item222_j1_phase_resultant_certificate.py":
        "c16f75156ba8424c567163cedc6a93a7656c8a53036b48ef69b06327d76ad44b",
    "sources/item222_j1_phase_resultant_report.md":
        "9e088b216901a826a516453f133f2e362308154bb16296147d68bc66f2549133",
    "scripts/item223_j1_frobenius_transfer_certificate.py":
        "928ddc876ed70939fd4a39fccd0e91d8c59d8aa2a8a694967d8fc7f737512d4a",
    "sources/item223_j1_frobenius_transfer_report.md":
        "d1102c3efec35e9b08d1a8bcdf46f1b00b33b18f20391016a4e17632b0c4a2e0",
}


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load_module(name: str, filename: str):
    path = resolve(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


item218 = load_module("item229_item218", "item218_j1_common_log_certificate.py")
item222 = load_module("item229_item222", "item222_j1_phase_resultant_certificate.py")
item223 = load_module("item229_item223", "item223_j1_frobenius_transfer_certificate.py")


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def trim(poly: list[Fraction]) -> list[Fraction]:
    answer = poly[:]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(size)
    ])


def scale(poly: list[Fraction], scalar: Fraction | int) -> list[Fraction]:
    return trim([Fraction(scalar) * value for value in poly])


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] += left_value * right_value
    return trim(answer)


def shift(poly: list[Fraction]) -> list[Fraction]:
    """Return poly(j+1), low-to-high in j."""
    answer = [Fraction(0)] * len(poly)
    for degree, coefficient in enumerate(poly):
        for index in range(degree + 1):
            answer[index] += coefficient * math.comb(degree, index)
    return trim(answer)


def evaluate(poly: list[Fraction], value: Fraction | int) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def binomial_linear(top_constant: Fraction, degree: int) -> list[Fraction]:
    """The polynomial binom(top_constant-2j, degree) in j."""
    answer = [Fraction(1)]
    for offset in range(degree):
        answer = multiply(answer, [top_constant - offset, Fraction(-2)])
    return scale(answer, Fraction(1, math.factorial(degree)))


def p_polynomial(h_value: int, s_value: Fraction) -> list[Fraction]:
    degree = 2 * h_value
    first = scale(
        binomial_linear(2 * h_value + 2 * s_value + 4, degree),
        4 * h_value + 4 * s_value - 1,
    )
    second = scale(
        binomial_linear(2 * h_value + 2 * s_value + 3, degree),
        2 * h_value + 1,
    )
    third = scale(
        binomial_linear(2 * h_value + 2 * s_value + 2, degree),
        -(2 * h_value + 8 * s_value),
    )
    return add(add(first, second), third)


def operator_l(poly: list[Fraction], s_value: Fraction) -> list[Fraction]:
    """L_s R=-(2s+j)R(j+1)-jR(j)."""
    first = multiply([2 * s_value, Fraction(1)], shift(poly))
    second = multiply([Fraction(0), Fraction(1)], poly)
    return scale(add(first, second), -1)


def solve_square(columns: list[list[Fraction]], target: list[Fraction]) -> list[Fraction]:
    size = len(columns)
    matrix = []
    for row in range(size):
        matrix.append([
            columns[column][row] if row < len(columns[column]) else Fraction(0)
            for column in range(size)
        ] + [target[row] if row < len(target) else Fraction(0)])
    for column in range(size):
        pivot = next(row for row in range(column, size) if matrix[row][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        pivot_value = matrix[column][column]
        matrix[column] = [value / pivot_value for value in matrix[column]]
        for row in range(size):
            if row == column or not matrix[row][column]:
                continue
            scalar = matrix[row][column]
            matrix[row] = [
                left - scalar * right
                for left, right in zip(matrix[row], matrix[column])
            ]
    return [matrix[row][-1] for row in range(size)]


def gosper_reduce(h_value: int, s_value: Fraction) -> tuple[Fraction, list[Fraction]]:
    """Unique P=c+L_s R with deg_j R<=2h-1."""
    degree = 2 * h_value
    columns = []
    for power in range(degree):
        basis = [Fraction(0)] * power + [Fraction(1)]
        columns.append(operator_l(basis, s_value))
    columns.append([Fraction(1)])
    solution = solve_square(columns, p_polynomial(h_value, s_value))
    r_poly = trim(solution[:-1])
    c_value = solution[-1]
    reconstructed = add(operator_l(r_poly, s_value), [c_value])
    if reconstructed != p_polynomial(h_value, s_value):
        raise AssertionError((h_value, s_value, "Gosper reconstruction"))
    return c_value, r_poly


def t_value(s_value: int, index: int) -> int:
    return (-1) ** index * math.comb(2 * s_value + index - 1, index)


def theta_decomposition(h_value: int, s_value: int) -> tuple[int, Fraction]:
    c_value, r_poly = gosper_reduce(h_value, Fraction(s_value))
    s_sum = sum(t_value(s_value, index) for index in range(s_value + 1))
    t_next = t_value(s_value, s_value + 1)
    tail_one = (
        (4 * h_value + 4 * s_value - 1) * math.comb(2 * h_value + 2, 2)
        + (2 * h_value + 1) ** 2
        - (2 * h_value + 8 * s_value)
    )
    tail_two = (4 * h_value + 4 * s_value - 1) * t_value(
        s_value, s_value + 2
    )
    upper = (
        c_value * s_sum
        + t_next * (s_value + 1) * evaluate(r_poly, s_value + 1)
        + t_next * tail_one
        + tail_two
    )
    closed_upper = item223.closed_delta_plus(2 * h_value, s_value)
    if upper.denominator != 1 or upper.numerator != closed_upper:
        raise AssertionError((h_value, s_value, upper, closed_upper))
    theta = closed_upper - 2 * item223.closed_delta_minus(2 * h_value, s_value)
    decomposed = upper - 2 * item223.closed_delta_minus(2 * h_value, s_value)
    if decomposed != theta:
        raise AssertionError((h_value, s_value, decomposed, theta))
    return theta, decomposed


def exact_decomposition_grid(limit: int = 8) -> dict:
    rows = []
    for h_value in range(1, limit + 1):
        for s_value in range(1, limit + 1):
            theta, decomposed = theta_decomposition(h_value, s_value)
            rows.append((h_value, s_value, theta, decomposed.numerator))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_REPLAY_OF_ALL_H_IDENTITY",
        "formal_identity": (
            "P_h(s,j)=c_h(s)-(2s+j)R_h(s,j+1)-jR_h(s,j), "
            "deg_j(R_h)<=2h-1"
        ),
        "theta_decomposition": (
            "Theta_h(s)=c_h(s)S_s+t_(s+1)G_h(s)-2Delta_minus(h,s)"
        ),
        "grid_h_max": limit,
        "grid_s_max": limit,
        "rows": len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def degree_leading_grid(limit: int = 8) -> dict:
    rows = []
    for h_value in range(1, limit + 1):
        degree = 2 * h_value + 1
        values = [
            gosper_reduce(h_value, Fraction(s_value))[0]
            for s_value in range(degree + 2)
        ]
        differences = values[:]
        for _ in range(degree):
            differences = [
                differences[index + 1] - differences[index]
                for index in range(len(differences) - 1)
            ]
        if len(set(differences)) != 1:
            raise AssertionError((h_value, "degree exceeds", degree))
        leading = differences[0] / math.factorial(degree)
        expected = Fraction(-(2 ** (4 * h_value + 2)), math.factorial(2 * h_value))
        if leading != expected:
            raise AssertionError((h_value, leading, expected))
        rows.append((h_value, degree, leading.numerator, leading.denominator))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_REPLAY_OF_ALL_H_TOP_DEGREE_PROOF",
        "degree": "deg_s(c_h)=2h+1",
        "leading_coefficient": "-2^(4h+2)/(2h)!",
        "checked_h_max": limit,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def binomial_fraction(value: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(degree):
        answer *= value - offset
        answer /= offset + 1
    return answer


def convolve_truncated(
    left: list[Fraction], right: list[Fraction], degree: int
) -> list[Fraction]:
    answer = [Fraction(0)] * (degree + 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            if left_index + right_index <= degree:
                answer[left_index + right_index] += left_value * right_value
    return answer


def phase_c(h_value: int) -> Fraction:
    """c_h(-(4h+3)/6) via its normalized-binomial coefficient formula."""
    degree = 2 * h_value
    exponent = Fraction(4 * h_value + 3, 3)
    middle = [Fraction(0)] * (degree + 1)
    for power in range(degree + 1):
        outer = binomial_fraction(exponent, power)
        for extra in range(min(power, degree - power) + 1):
            middle[power + extra] += (
                outer * math.comb(power, extra) * Fraction(1, 2**extra)
            )
    inverse = [
        Fraction((-1) ** index * math.comb(2 * h_value + index, index))
        for index in range(degree + 1)
    ]
    first = Fraction(4 * h_value - 9, 3)
    last = Fraction(10 * h_value + 12, 3)
    boundary = [
        first + (2 * h_value + 1) + last,
        2 * first + (2 * h_value + 1),
        first,
    ]
    product = convolve_truncated(middle, inverse, degree)
    product = convolve_truncated(product, boundary, degree)
    return product[degree]


def rho(h_value: int) -> Fraction:
    numerator = (
        h_value
        * (4 * h_value + 1)
        * (4 * h_value + 5)
        * (4 * h_value + 7)
        * (4 * h_value + 9)
        * (4 * h_value + 11)
        * (4 * h_value + 15) ** 2
    )
    denominator = (
        864
        * (h_value + 1)
        * (h_value + 2)
        * (2 * h_value + 1) ** 2
        * (2 * h_value + 3)
        * (2 * h_value + 5) ** 2
        * (4 * h_value + 3)
    )
    return Fraction(numerator, denominator)


def conjectural_ratio(h_value: int) -> Fraction:
    if h_value < 1 or h_value % 3 == 0:
        raise ValueError(h_value)
    residue = h_value % 3
    current = 1 if residue == 1 else 2
    answer = Fraction(-49, 18) if residue == 1 else Fraction(4235, 1944)
    while current < h_value:
        answer *= rho(current)
        current += 3
    return answer


def finite_phase_factorization(h_max: int = 80) -> dict:
    rows = []
    for h_value in range(1, h_max + 1):
        if h_value % 3 == 0:
            continue
        eliminant, _ = item222.phase_fraction_and_integer(h_value)
        c_value = phase_c(h_value)
        ratio = conjectural_ratio(h_value)
        if c_value != ratio * eliminant:
            raise AssertionError((h_value, c_value, ratio, eliminant))
        rows.append(
            (
                h_value,
                c_value.numerator,
                c_value.denominator,
                eliminant.numerator,
                eliminant.denominator,
                ratio.numerator,
                ratio.denominator,
            )
        )
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_PATTERN_NOT_ALL_H_THEOREM",
        "h_max": h_max,
        "admissible_h_rows": len(rows),
        "observed_identity": "c_h(s*)=R_h E_h*",
        "initial_values": {"R_1": "-49/18", "R_2": "4235/1944"},
        "observed_ratio": (
            "R_(h+3)/R_h=h(4h+1)(4h+5)(4h+7)(4h+9)(4h+11)(4h+15)^2/"
            "[864(h+1)(h+2)(2h+1)^2(2h+3)(2h+5)^2(4h+3)]"
        ),
        "all_h_proof": "OPEN: no symbolic WZ/telescoping certificate is claimed",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def finite_joint_scan(prime_max: int) -> dict:
    counts = {"rows": 0, "Theta_zero": 0, "E_zero": 0, "joint_zero": 0}
    theta_rows = []
    e_rows = []
    joint_rows = []
    for prime in item218.primes_upto(prime_max):
        if prime < 13:
            continue
        factorial, inverse_factorial, inverse = item218.factorial_tables(prime)
        for s_value in range(1, (prime - 7) // 6 + 1):
            numerator = prime - 6 * s_value - 3
            if numerator % 4:
                continue
            h_value = numerator // 4
            if h_value < 1:
                continue
            plus, minus = item223.transfer_mod(2 * h_value, s_value, prime)
            theta = (plus - 2 * minus) % prime
            _, _, eliminant, _ = item218.divided_conditions_mod(
                prime,
                h_value,
                s_value,
                factorial,
                inverse_factorial,
                inverse,
            )
            counts["rows"] += 1
            counts["Theta_zero"] += theta == 0
            counts["E_zero"] += eliminant == 0
            counts["joint_zero"] += theta == eliminant == 0
            if theta == 0:
                theta_rows.append((prime, h_value, s_value))
            if eliminant == 0:
                e_rows.append((prime, h_value, s_value))
            if theta == eliminant == 0:
                joint_rows.append((prime, h_value, s_value))
    expected = {"rows": 22934, "Theta_zero": 22, "E_zero": 58, "joint_zero": 0}
    if prime_max == 2000 and counts != expected:
        raise AssertionError((counts, expected))
    digest = lambda rows: hashlib.sha256(
        json.dumps(rows, separators=(",", ":")).encode("ascii")
    ).hexdigest()
    return {
        "classification": "EXACT_FINITE_ONLY",
        "prime_max": prime_max,
        **counts,
        "Theta_zero_stream_sha256": digest(theta_rows),
        "E_zero_stream_sha256": digest(e_rows),
        "joint_zero_stream_sha256": digest(joint_rows),
        "scope_warning": "joint emptiness implies no all-prime density or rate theorem",
    }


def certificate(prime_max: int) -> dict:
    return {
        "item": 229,
        "classification": {
            "PROVED": [
                "the exact fixed-h Gosper decomposition of corrected Theta",
                "deg_s(c_h)=2h+1 with leading coefficient -2^(4h+2)/(2h)!",
                "the displayed polynomial Gosper-antidifference ansatz retains a nonzero S_s coefficient",
            ],
            "EXACT_FINITE_ONLY": [
                "the phase factor pattern c_h(s*)=R_h E_h* through h<=80",
                f"the joint Theta/E scan through p<={prime_max}",
            ],
            "OPEN": [
                "an all-h symbolic certificate for the observed phase factorization",
                "any separate non-rationality, independence, or universal cancellation theorem for S_s",
                "control of the remaining boundary/binomial coordinate after E=Theta=0",
                "any positive Route-1 linear log-rate or divisibility exponent",
            ],
        },
        "definitions": {
            "t_j": "(-1)^j binom(2s+j-1,j)",
            "S_s": "sum_(j=0)^s t_j",
            "Theta": "Delta_plus-2Delta_minus",
            "phase": "s*=-(4h+3)/6",
        },
        "all_h_gosper_theorem": exact_decomposition_grid(),
        "all_h_degree_theorem": degree_leading_grid(),
        "phase_factorization_evidence": finite_phase_factorization(),
        "finite_joint_scan": finite_joint_scan(prime_max),
        "rate_ledger": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "reason": "the exact reduction leaves an uncontrolled incomplete-binomial/boundary coordinate",
        },
        "dependency_sha256": DEPENDENCIES,
        "runtime": {"external_numeric_backend": None},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=2000)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    result = certificate(args.prime_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "output": str(args.output),
        "prime_max": args.prime_max,
        "rows": result["finite_joint_scan"]["rows"],
        "joint_zero": result["finite_joint_scan"]["joint_zero"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
