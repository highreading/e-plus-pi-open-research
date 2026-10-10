#!/usr/bin/env python3
"""Exact checker for Item 248's local tail and split-root reductions."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item248_j1_joint_root_reduction_certificate.json"

DEPENDENCIES = {
    "sources/item234_j1_first_witt_report.md":
        "9bd5bb91fe813622db0c15d8bfc25714bcefb00512ed8f5eafddacd8cfb9b016",
    "scripts/item234_j1_first_witt_certificate.py":
        "8d41a5a73e9467cf4c998d3e345767c04c68ab6467605290480825b15b08e125",
    "results/item234_j1_first_witt_certificate.json":
        "6797c1f2cd072ec92d311e01b596c3ac95888ce9b761bc325a625ef6f9f0c748",
    "sources/item242_j1_E_kernel_state_report.md":
        "174db03d85654f526fa20af1abd135944d2995babd2a682e16d1416bfe9c9d09",
    "scripts/item242_j1_E_kernel_state_certificate.py":
        "6941b01522fd981de0a70139715b57883e15b23fd43858581a8cb4f07bbe1d84",
    "results/item242_j1_E_kernel_state_certificate.json":
        "77a6ffe1af55e03504def21883af74d6abe07000d75301459fe812b8ca585f73",
    "sources/item245_j1_generalized_phase_observation_report.md":
        "cdd1d5cb45d68615c983529bd465263ffe6b350279bfdf44f9c54e203dae196e",
    "scripts/item245_j1_generalized_phase_observation_certificate.py":
        "3721a0a7fbfa5a2812049239c4428eaf705c003120f3e1aab7c4bd6259c11812",
    "results/item245_j1_generalized_phase_observation_certificate.json":
        "f8b826c2292b91b740cdb45771598612b317f1ae82091279c073387707cdb357",
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


def pair_add(a: tuple[int, int], b: tuple[int, int], prime: int):
    return ((a[0] + b[0]) % prime, (a[1] + b[1]) % prime)


def pair_sub(a: tuple[int, int], b: tuple[int, int], prime: int):
    return ((a[0] - b[0]) % prime, (a[1] - b[1]) % prime)


def pair_scale(scalar: int, a: tuple[int, int], prime: int):
    return (scalar * a[0] % prime, scalar * a[1] % prime)


def pair_mul(a: tuple[int, int], b: tuple[int, int], prime: int):
    return (
        (a[0] * b[0] - a[1] * b[1]) % prime,
        (a[0] * b[1] + a[1] * b[0]) % prime,
    )


def pair_power(a: tuple[int, int], exponent: int, prime: int):
    answer = (1, 0)
    while exponent:
        if exponent & 1:
            answer = pair_mul(answer, a, prime)
        a = pair_mul(a, a, prime)
        exponent //= 2
    return answer


def pair_norm(a: tuple[int, int], prime: int) -> int:
    return (a[0] * a[0] + a[1] * a[1]) % prime


def pair_convolution(left, right, prime: int):
    answer = [(0, 0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            answer[left_index + right_index] = pair_add(
                answer[left_index + right_index],
                pair_mul(left_value, right_value, prime),
                prime,
            )
    return answer


def pair_polynomial_power(poly, exponent: int, prime: int):
    answer = [(1, 0)]
    while exponent:
        if exponent & 1:
            answer = pair_convolution(answer, poly, prime)
        exponent //= 2
        if exponent:
            poly = pair_convolution(poly, poly, prime)
    return answer


def linear_data(prime: int):
    chi = 1 if prime % 4 == 1 else -1
    x_value = (0, chi % prime)
    linears = [
        [(1, 0), (-1 % prime, 0)],
        [(2, 0), (-1 % prime, 0)],
        [pair_sub((1, 0), x_value, prime), x_value],
        [pair_add((1, 0), x_value, prime), pair_scale(-1, x_value, prime)],
    ]
    return x_value, linears


def direct_factor_coefficients(
    prime: int, exponents: tuple[int, int, int, int]
):
    _, linears = linear_data(prime)
    answer = [(1, 0)]
    for linear, exponent in zip(linears, exponents):
        answer = pair_convolution(
            answer, pair_polynomial_power(linear, exponent, prime), prime
        )
    return answer


def factor_coefficients(
    prime: int,
    exponents: tuple[int, int, int, int],
    limit: int,
):
    """Pearson recurrence for the product of the four local linears."""
    _, linears = linear_data(prime)
    numerator = [(0, 0)] * 4
    for omitted, (linear, exponent) in enumerate(zip(linears, exponents)):
        product = [(1, 0)]
        for index, other in enumerate(linears):
            if index != omitted:
                product = pair_convolution(product, other, prime)
        for degree, value in enumerate(product):
            contribution = pair_scale(
                exponent,
                pair_mul(linear[1], value, prime),
                prime,
            )
            numerator[degree] = pair_add(
                numerator[degree], contribution, prime
            )

    initial = (1, 0)
    for linear, exponent in zip(linears, exponents):
        initial = pair_mul(
            initial, pair_power(linear[0], exponent, prime), prime
        )

    # Product of the four distinct linears is
    # D=4-10u+10u^2-5u^3+u^4.
    denominator = (4, -10, 10, -5, 1)
    coefficients = [initial]
    inverse_four = pow(4, -1, prime)
    for degree in range(1, limit + 1):
        right = (0, 0)
        for index in range(min(3, degree - 1) + 1):
            right = pair_add(
                right,
                pair_mul(
                    numerator[index],
                    coefficients[degree - 1 - index],
                    prime,
                ),
                prime,
            )
        correction = (0, 0)
        for index in range(1, min(4, degree) + 1):
            correction = pair_add(
                correction,
                pair_scale(
                    denominator[index] * (degree - index),
                    coefficients[degree - index],
                    prime,
                ),
                prime,
            )
        value = pair_scale(
            inverse_four * pow(degree, -1, prime),
            pair_sub(right, correction, prime),
            prime,
        )
        coefficients.append(value)
    return coefficients


def local_data(prime: int, h_value: int, s_value: int, nu: int):
    r_value = 2 * h_value
    x_value, _ = linear_data(prime)
    if nu == 0:
        m_value = 2 * s_value + 2
        n_value = prime - 2 * s_value - 3
        exponents = (2 * s_value, 2 * s_value, r_value, 1)
    else:
        m_value = 2 * s_value + 1
        n_value = prime - 2 * s_value - 2
        exponents = (
            2 * s_value - 1,
            2 * s_value - 1,
            r_value,
            4,
        )
    factor = factor_coefficients(prime, exponents, n_value + 1)

    harmonic = 0
    local_square = (0, 0)
    for degree in range(n_value + 1):
        harmonic = (harmonic + pow(degree + 1, -1, prime)) % prime
        a_square = (
            8 * harmonic * pow(degree + 2, -1, prime)
        ) % prime
        local_square = pair_add(
            local_square,
            pair_scale(a_square, factor[n_value - degree], prime),
            prime,
        )

    target = n_value + 2
    first_derivative = (0, 0)
    for index in range(1, target + 1):
        source = target - index
        if source < len(factor):
            first_derivative = pair_add(
                first_derivative,
                pair_scale(-pow(index, -1, prime), factor[source], prime),
                prime,
            )
    second_derivative = pair_scale(
        pow(4, -1, prime), local_square, prime
    )

    a_value = prime - m_value + 1
    inverse_x_power = pair_power(
        x_value, (4 - a_value % 4) % 4, prime
    )
    leading_pair = pair_scale(
        -24,
        pair_mul(local_square, inverse_x_power, prime),
        prime,
    )
    return {
        "a": a_value,
        "m": m_value,
        "n": n_value,
        "exponents": exponents,
        "factor": factor,
        "first": first_derivative,
        "second": second_derivative,
        "leading": leading_pair,
    }


def split_roots(prime: int) -> list[int]:
    if prime % 4 == 3:
        return []
    root = next(value for value in range(1, prime) if value * value % prime == prime - 1)
    return sorted((root, prime - root))


def root_evaluations(pair: tuple[int, int], prime: int):
    return [
        [root, (pair[0] + pair[1] * root) % prime]
        for root in split_roots(prime)
    ]


def build_certificate(direct_limit: int, census_limit: int):
    dependency_hashes = {
        name: sha256_file(resolve_dependency(name)) for name in DEPENDENCIES
    }
    if dependency_hashes != DEPENDENCIES:
        raise AssertionError((dependency_hashes, DEPENDENCIES))

    item234 = load_module(
        "item234_frozen", "scripts/item234_j1_first_witt_certificate.py"
    )
    item242 = load_module(
        "item242_frozen", "scripts/item242_j1_E_kernel_state_certificate.py"
    )
    item245 = load_module(
        "item245_frozen",
        "scripts/item245_j1_generalized_phase_observation_certificate.py",
    )

    direct_rows = 0
    direct_coordinates = 0
    recurrence_checks = 0
    leading_checks = 0
    bb_cache: dict[int, list[int]] = {}
    samples = []
    for prime, h_value, s_value in item234.rows_upto(direct_limit):
        for nu in (0, 1):
            data = local_data(prime, h_value, s_value, nu)
            expected = item245.leading_pair_fast(
                prime, h_value, s_value, nu, item234, bb_cache
            )
            if data["leading"] != expected:
                raise AssertionError((
                    prime, h_value, s_value, nu,
                    data["leading"], expected, "local leading pair",
                ))
            leading_checks += 1
            if prime <= 61:
                direct = direct_factor_coefficients(prime, data["exponents"])
                if data["factor"] != (
                    direct + [(0, 0)] * len(data["factor"])
                )[:len(data["factor"])]:
                    raise AssertionError((prime, h_value, s_value, nu, "recurrence"))
                recurrence_checks += 1
            if (prime, h_value, s_value) == (29, 5, 1):
                samples.append({
                    "nu": nu,
                    "a_m_n": [data["a"], data["m"], data["n"]],
                    "first_parameter_derivative": list(data["first"]),
                    "second_parameter_derivative": list(data["second"]),
                    "leading_pair": list(data["leading"]),
                })
            direct_coordinates += 1
        direct_rows += 1
    if direct_limit == 151 and (direct_rows, direct_coordinates) != (184, 368):
        raise AssertionError((direct_rows, direct_coordinates))

    rows = 0
    split_rows = 0
    inert_rows = 0
    leading_root_losses = []
    leading_pair_zeros = []
    joint_root_records = []
    g_root_zeros = []
    wronskian_root_zeros = []
    for prime, h_value, s_value in item234.rows_upto(census_limit):
        r_value = 2 * h_value
        data = [
            local_data(prime, h_value, s_value, nu) for nu in (0, 1)
        ]
        leading = [entry["leading"] for entry in data]
        norms = [pair_norm(value, prime) for value in leading]
        cross = (
            leading[0][0] * leading[1][1]
            - leading[0][1] * leading[1][0]
        ) % prime
        for nu in (0, 1):
            if norms[nu] == 0:
                leading_root_losses.append([
                    prime, h_value, s_value, nu,
                    list(leading[nu]), root_evaluations(leading[nu], prime),
                ])
            if leading[nu] == (0, 0):
                leading_pair_zeros.append([
                    prime, h_value, s_value, nu,
                ])
        if norms == [0, 0] and cross == 0:
            joint_root_records.append([
                prime, h_value, s_value,
                [list(value) for value in leading], cross,
            ])

        factorial = math.prod(range(1, r_value + 1)) % prime
        inverse_factorial = pow(factorial, -1, prime)
        g_values = [
            pair_scale(inverse_factorial, entry["first"], prime)
            for entry in data
        ]
        for nu, value in enumerate(g_values):
            if pair_norm(value, prime) == 0:
                g_root_zeros.append([
                    prime, h_value, s_value, nu,
                    list(value), root_evaluations(value, prime),
                ])

        raw_wronskian = pair_sub(
            pair_mul(data[0]["first"], data[1]["second"], prime),
            pair_mul(data[1]["first"], data[0]["second"], prime),
            prime,
        )
        normalized_wronskian = pair_scale(
            pow(2 * factorial * factorial % prime, -1, prime),
            raw_wronskian,
            prime,
        )
        if pair_norm(normalized_wronskian, prime) == 0:
            wronskian_root_zeros.append([
                prime, h_value, s_value,
                list(normalized_wronskian),
                root_evaluations(normalized_wronskian, prime),
            ])

        if prime % 4 == 1:
            split_rows += 1
        else:
            inert_rows += 1
            for value in leading + g_values + [normalized_wronskian]:
                if pair_norm(value, prime) == 0 and value != (0, 0):
                    raise AssertionError((prime, value, "inert norm distinction"))
        rows += 1

    if census_limit == 601:
        if rows != 2435:
            raise AssertionError(rows)
        if (split_rows, inert_rows) != (1189, 1246):
            raise AssertionError((split_rows, inert_rows))
        if len(leading_root_losses) != 19 or len(g_root_zeros) != 17:
            raise AssertionError((len(leading_root_losses), len(g_root_zeros)))
        if leading_pair_zeros != [[59, 2, 8, 1]]:
            raise AssertionError(leading_pair_zeros)
        if joint_root_records:
            raise AssertionError(joint_root_records)
        if g_root_zeros[0] != [
            41, 2, 5, 0, [12, 15], [[9, 24], [32, 0]],
        ]:
            raise AssertionError(g_root_zeros[0])
        expected_w_primes = [109, 149, 181, 241, 389, 521, 601]
        if [record[0] for record in wronskian_root_zeros] != expected_w_primes:
            raise AssertionError(wronskian_root_zeros)
        if wronskian_root_zeros[:2] != [
            [109, 4, 15, [88, 70], [[33, 0], [76, 67]]],
            [149, 26, 7, [42, 60], [[44, 0], [105, 84]]],
        ]:
            raise AssertionError(wronskian_root_zeros[:2])

    state_59, digits_59, _ = item245.generalized_state(
        59, 2, 8, 1, item234, item242, {}
    )
    rank_59 = item242.rank_mod(
        item245.multiplication_matrix(state_59, 59, item242), 59
    )
    if digits_59[0] != [0, 0] or rank_59 != 6:
        raise AssertionError((digits_59, rank_59))

    return {
        "item": 248,
        "title": "local logarithmic tails and the joint-root Wronskian no-go",
        "parameters": {
            "row": "p=4h+6s+3=2r+6s+3, r=2h, h,s>=1",
            "direct_limit": direct_limit,
            "census_limit": census_limit,
        },
        "proved": {
            "local_logarithm": (
                "for I^2=-1, x=I^p and u=1-z/x, "
                "B0(x(1-u))=u A_p(u) mod u^p, "
                "A_p=-2 sum_{j=1}^{p-1}u^(j-1)/j"
            ),
            "tail_formula": (
                "x^a C_nu(I) is the coefficient [u^n] of A_p^2 times "
                "the four explicit linear powers recorded in the report"
            ),
            "square_coefficients": (
                "[u^k]A_p^2=8 H_(k+1)/(k+2) for every required k"
            ),
            "pearson_recurrence": (
                "D H'=N H with D=4-10u+10u^2-5u^3+u^4; "
                "all coefficient pivots 4n are p-units"
            ),
            "lambda_roots": (
                "F_nu(lambda)=lambda falling_(r+1) G_nu(lambda)"
            ),
            "division_free_wronskian": (
                "G1'G0-G1G0'=(F0'F1''-F1'F0'')/(2(r!)^2); "
                "a common second-derivative root forces this Wronskian to vanish"
            ),
            "split_distinction": (
                "for p=1 mod 4 rootwise zero means pair norm zero; "
                "pair nonzero is insufficient. For p=3 mod 4 norm zero "
                "is equivalent to the whole pair being zero"
            ),
        },
        "exact_replay": {
            "direct_rows": direct_rows,
            "direct_coordinates": direct_coordinates,
            "leading_formula_checks": leading_checks,
            "direct_recurrence_checks": recurrence_checks,
            "sample_row_29_5_1": samples,
            "individual_nonvanishing_counterexample": {
                "row_nu": [59, 2, 8, 1],
                "Q_adic_digits": digits_59,
                "state_mod_Q4": state_59,
                "state_rank": rank_59,
            },
        },
        "exact_finite_only": {
            "rows": rows,
            "split_rows": split_rows,
            "inert_rows": inert_rows,
            "leading_root_loss_records": leading_root_losses,
            "leading_pair_zero_records": leading_pair_zeros,
            "joint_root_records": joint_root_records,
            "G_root_zero_records": g_root_zeros,
            "Wronskian_root_zero_records": wronskian_root_zeros,
            "interpretation": (
                "the Wronskian-unit strategy already fails on split rows, "
                "while no common leading root occurs through the stated bound"
            ),
        },
        "open": [
            "an all-row exclusion of a common root of the two leading pairs",
            "a replacement invariant after the universal Wronskian-unit strategy fails",
            "any all-prime p^3 terminal obstruction or common-log exclusion",
            "any Route-1 rate or conclusion about e+pi",
        ],
        "dependencies": dependency_hashes,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--direct-limit", type=int, default=151)
    parser.add_argument("--census-limit", type=int, default=601)
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.direct_limit, arguments.census_limit)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(arguments.output),
        "rows": certificate["exact_finite_only"]["rows"],
        "joint_roots": len(certificate["exact_finite_only"]["joint_root_records"]),
        "wronskian_root_zeros": len(
            certificate["exact_finite_only"]["Wronskian_root_zero_records"]
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
