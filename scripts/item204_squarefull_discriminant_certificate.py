#!/usr/bin/env python3
"""Portable exact replay for Item 204.

The companion report proves the all-index polynomial and resultant
identities.  This standard-library checker verifies them symbolically on
an exact finite grid, replays the scoped discriminant counterexamples,
and performs a finite actual lower-index square scan.  Every scan
nonoccurrence is labelled FINITE in the emitted JSON.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item204_squarefull_discriminant_certificate.json"
DEFAULT_OUTPUT = (
    HERE / RESULT_NAME
    if HERE.name.lower() == "work"
    else HERE.parent / "results" / RESULT_NAME
)


def trim(poly: list[int]) -> list[int]:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    result = [0] * size
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def subtract(left: list[int], right: list[int]) -> list[int]:
    return add(left, [-value for value in right])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def shift(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def derivative(poly: list[int]) -> list[int]:
    if len(poly) <= 1:
        return [0]
    return [index * poly[index] for index in range(1, len(poly))]


def evaluate(poly: list[int], value: int, modulus: int | None = None) -> int:
    result = 0
    if modulus is None:
        for coefficient in reversed(poly):
            result = result * value + coefficient
        return result
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % modulus
    return result


def reverse_bessel_closed(n: int) -> list[int]:
    return [
        math.factorial(2 * n - k)
        // (math.factorial(k) * math.factorial(n - k))
        for k in range(n + 1)
    ]


def reverse_bessel_polynomials(limit: int) -> list[list[int]]:
    if limit == 0:
        return [[1]]
    polynomials = [[1], [2, 1]]
    for n in range(2, limit + 1):
        polynomials.append(
            add(scale(polynomials[-1], 4 * n - 2), shift(polynomials[-2], 2))
        )
    return polynomials


def bareiss_determinant(matrix: list[list[int]]) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    if size == 1:
        return matrix[0][0]
    work = [row[:] for row in matrix]
    sign = 1
    previous_pivot = 1
    for column in range(size - 1):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign = -sign
        pivot = work[column][column]
        for row in range(column + 1, size):
            for next_column in range(column + 1, size):
                numerator = (
                    work[row][next_column] * pivot
                    - work[row][column] * work[column][next_column]
                )
                if column:
                    if numerator % previous_pivot:
                        raise AssertionError("non-exact Bareiss division")
                    numerator //= previous_pivot
                work[row][next_column] = numerator
            work[row][column] = 0
        previous_pivot = pivot
    return sign * work[-1][-1]


def resultant(first: list[int], second: list[int]) -> int:
    first = trim(first)
    second = trim(second)
    first_degree = len(first) - 1
    second_degree = len(second) - 1
    if second_degree == 0:
        return second[0] ** first_degree
    if first_degree == 0:
        return first[0] ** second_degree
    first_descending = list(reversed(first))
    second_descending = list(reversed(second))
    size = first_degree + second_degree
    matrix: list[list[int]] = []
    for offset in range(second_degree):
        matrix.append(
            [0] * offset
            + first_descending
            + [0] * (second_degree - 1 - offset)
        )
    for offset in range(first_degree):
        matrix.append(
            [0] * offset
            + second_descending
            + [0] * (first_degree - 1 - offset)
        )
    if any(len(row) != size for row in matrix):
        raise AssertionError("bad Sylvester matrix")
    return bareiss_determinant(matrix)


def odd_double_factorial(n: int) -> int:
    result = 1
    for value in range(1, n + 1, 2):
        result *= value
    return result


def symbolic_resultant_regression(limit: int) -> dict:
    polynomials = reverse_bessel_polynomials(limit)
    rows = []
    adjacent_product = 1
    for n in range(1, limit + 1):
        current = polynomials[n]
        previous = polynomials[n - 1]
        if current != reverse_bessel_closed(n):
            raise AssertionError((n, "closed form"))
        derivative_identity = subtract(
            subtract(scale(derivative(current), 2), current),
            scale(shift(previous, 1), -1),
        )
        # 2 A_n' - A_n + X A_(n-1) = 0.
        if derivative_identity != [0]:
            raise AssertionError((n, "derivative identity", derivative_identity))

        if n > 1:
            previous_constant = math.factorial(2 * (n - 1)) // math.factorial(n - 1)
            adjacent_product *= previous_constant * previous_constant
        adjacent = resultant(current, previous)
        self_resultant = resultant(current, derivative(current))
        predicted_self = odd_double_factorial(2 * n - 1) * adjacent_product
        if adjacent != adjacent_product:
            raise AssertionError((n, "adjacent resultant", adjacent, adjacent_product))
        if self_resultant != predicted_self:
            raise AssertionError((n, "derivative resultant", self_resultant, predicted_self))

        q_n = evaluate(current, -1)
        q_previous = evaluate(previous, -1)
        derivative_at_minus_one = evaluate(derivative(current), -1)
        if 2 * derivative_at_minus_one != q_n + q_previous:
            raise AssertionError((n, "fixed-point derivative"))
        rows.append(
            {
                "N": n,
                "q_N": str(q_n),
                "A_N_prime_at_minus_1": str(derivative_at_minus_one),
                "adjacent_resultant": str(adjacent),
                "derivative_resultant": str(self_resultant),
                "discriminant_sign": -1 if (n * (n - 1) // 2) & 1 else 1,
            }
        )
    stream = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode("ascii")
    return {
        "classification": "FINITE_EXACT_SYMBOLIC_REPLAY_OF_PROVED_IDENTITIES",
        "N_range": [1, limit],
        "checks": len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "rows": rows,
        "all_exact": True,
    }


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for divisor in range(2, math.isqrt(limit) + 1):
        if sieve[divisor]:
            sieve[divisor * divisor : limit + 1 : divisor] = b"\x00" * (
                (limit - divisor * divisor) // divisor + 1
            )
    return [prime for prime in range(2, limit + 1) if sieve[prime]]


def exact_q_and_shift_derivative(limit: int) -> tuple[list[int], list[int]]:
    q = [1, 1]
    shift_derivative = [0, 1]
    for n in range(2, limit + 1):
        coefficient = 4 * n - 2
        q.append(coefficient * q[-1] + q[-2])
        shift_derivative.append(
            coefficient * shift_derivative[-1]
            + shift_derivative[-2]
            + q[-2]
        )
    return q[: limit + 1], shift_derivative[: limit + 1]


def valuation(number: int, prime: int) -> int:
    result = 0
    while number % prime == 0:
        result += 1
        number //= prime
    return result


def hensel_and_discriminant_witnesses() -> dict:
    polynomials = reverse_bessel_polynomials(4)
    n = 4
    prime = 13
    current = polynomials[n]
    q_n = evaluate(current, -1)
    q_previous = evaluate(polynomials[n - 1], -1)
    derivative_value = evaluate(derivative(current), -1)
    lift_digit = (
        -(q_n // prime) * pow(derivative_value, -1, prime)
    ) % prime
    predicted_digit = (
        -2 * (q_n // prime) * pow(q_previous, -1, prime)
    ) % prime
    lifted_argument = -1 + prime * lift_digit
    lifted_value = evaluate(current, lifted_argument)
    if not (
        prime > 2 * n + 1
        and q_n % prime == 0
        and q_n % (prime * prime) != 0
        and derivative_value % prime != 0
        and lift_digit == predicted_digit == 9
        and lifted_value % (prime * prime) == 0
    ):
        raise AssertionError("reverse-Bessel Hensel witness")

    q, shift_derivative = exact_q_and_shift_derivative(79)
    fixture_specs = [
        (8, 13, "SQUARE_WITH_UNIT_SHIFT_DERIVATIVE_OUTSIDE_TARGET_RANGE"),
        (79, 7, "SQUARE_WITH_UNIT_SHIFT_DERIVATIVE_OUTSIDE_TARGET_RANGE"),
        (79, 31, "SQUARE_WITH_UNIT_SHIFT_DERIVATIVE_OUTSIDE_TARGET_RANGE"),
        (48, 2879, "MULTIPLE_SHIFT_ROOT_WITH_SIMPLE_VALUE_IN_TARGET_RANGE"),
    ]
    fixtures = []
    for index, fixture_prime, classification in fixture_specs:
        if not is_prime(fixture_prime):
            raise AssertionError((fixture_prime, "not prime"))
        exponent = valuation(q[index], fixture_prime)
        derivative_mod_prime = shift_derivative[index] % fixture_prime
        in_target = fixture_prime > 2 * index + 1
        if index in (8, 79):
            if exponent != 2 or derivative_mod_prime == 0 or in_target:
                raise AssertionError((index, fixture_prime, "necessity fixture"))
        else:
            if exponent != 1 or derivative_mod_prime != 0 or not in_target:
                raise AssertionError((index, fixture_prime, "sufficiency fixture"))
        fixtures.append(
            {
                "N": index,
                "p": fixture_prime,
                "p_gt_2N_plus_1": in_target,
                "v_p_q_N": exponent,
                "Q_N_prime_at_0_mod_p": derivative_mod_prime,
                "q_N_over_p_mod_p": (q[index] // fixture_prime) % fixture_prime,
                "classification": classification,
            }
        )

    return {
        "classification": "FINITE_EXACT_WITNESSES_SUPPORTING_SCOPED_NO_GO",
        "reverse_bessel_same_mod_p_root_data": {
            "N": n,
            "p": prime,
            "p_gt_2N_plus_1": True,
            "q_N": q_n,
            "q_N_over_p_mod_p": (q_n // prime) % prime,
            "A_N_prime_at_minus_1_mod_p": derivative_value % prime,
            "hensel_lift_digit": lift_digit,
            "lifted_argument": lifted_argument,
            "A_N_at_lifted_argument_over_p_squared": lifted_value // (prime * prime),
            "meaning": (
                "same A_N and same root residue modulo p, but the first-Witt "
                "evaluation lift changes valuation one into valuation at least two"
            ),
        },
        "coefficient_shift_continuant_fixtures": fixtures,
        "scope_warning": (
            "The square-with-unit-derivative rows are outside p>2N+1.  "
            "Only (N,p)=(48,2879) is a target-range fixture, and it refutes "
            "sufficiency of shift-polynomial multiplicity, not necessity."
        ),
    }


def finite_actual_lower_scan(prime_limit: int) -> dict:
    root_rows = []
    square_rows = []
    for prime in primes_upto(prime_limit):
        if prime < 7:
            continue
        modulus = prime * prime
        previous = 1
        current = 1
        for n in range(2, (prime - 1) // 2):
            following = ((4 * n - 2) * current + previous) % modulus
            previous, current = current, following
            if current % prime:
                continue
            if previous % prime == 0:
                raise AssertionError((prime, n, "adjacent common root"))
            divided_value = current // prime % prime
            derivative_at_root = previous * pow(2, -1, prime) % prime
            lift_digit = (
                -divided_value * pow(derivative_at_root, -1, prime)
            ) % prime
            predicted_digit = (
                -2 * divided_value * pow(previous, -1, prime)
            ) % prime
            if lift_digit != predicted_digit:
                raise AssertionError((prime, n, "Hensel digit"))
            row = {
                "p": prime,
                "N": n,
                "q_N_over_p_mod_p": divided_value,
                "q_N_minus_1_mod_p": previous % prime,
                "A_N_prime_at_minus_1_mod_p": derivative_at_root,
                "hensel_lift_digit": lift_digit,
                "p_squared_divides_q_N": divided_value == 0,
            }
            root_rows.append(row)
            if divided_value == 0:
                square_rows.append(row)
    stream = json.dumps(root_rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    return {
        "classification": "EXPERIMENTAL_FINITE_NOT_AN_ALL_PRIME_THEOREM",
        "prime_limit": prime_limit,
        "condition": "prime p>2N+1 and p divides q_N",
        "actual_root_rows": len(root_rows),
        "actual_large_prime_square_rows": square_rows,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def certificate(prime_limit: int, symbolic_limit: int) -> dict:
    return {
        "item": 204,
        "classification": {
            "PROVED": [
                "q_N=A_N(-1) for the monic scaled reverse-Bessel polynomial A_N",
                "2*A_N'=A_N-X*A_(N-1) and the exact adjacent, derivative, and discriminant product formulas",
                "every odd actual root p|q_N is simple as a polynomial root at X=-1",
                "for p>2N+1, p^2|q_N iff the unique first Hensel evaluation digit is zero",
                "reverse-Bessel discriminant and mod-p root data alone do not determine that Hensel digit",
                "multiplicity at T=0 for the all-coefficient-shift continuant is not sufficient for p^2|q_N even in the target range",
                "multiplicity at T=0 for the all-coefficient-shift continuant is not necessary globally, with no target-range necessity claim",
            ],
            "EXPERIMENTAL_FINITE": [
                f"actual lower-index square scan through p<={prime_limit}",
                f"direct Sylvester-resultant replay through N<={symbolic_limit}",
                "the displayed exact Hensel and coefficient-shift fixtures",
            ],
            "OPEN": [
                "whether any prime p>2N+1 satisfies p^2|q_N for the actual seed q_0=q_1=1",
                "any proper all-N upper bound for the large-prime squarefull radical",
                "any recurrence-mod-p^2 identity forcing the actual Hensel digit to be nonzero",
            ],
        },
        "exact_identities": {
            "polynomial": (
                "A_N(X)=sum_(k=0)^N (2N-k)!/(k!(N-k)!) X^k; q_N=A_N(-1)"
            ),
            "polynomial_recurrence": (
                "A_0=1, A_1=X+2, A_N=(4N-2)A_(N-1)+X^2 A_(N-2)"
            ),
            "derivative": "2 A_N'(X)=A_N(X)-X A_(N-1)(X)",
            "adjacent_resultant": (
                "Res(A_N,A_(N-1))=product_(k=1)^(N-1)(((2k)!/k!)^2)"
            ),
            "derivative_resultant": (
                "Res(A_N,A_N')=(2N-1)!! product_(k=1)^(N-1)(((2k)!/k!)^2)"
            ),
            "discriminant": (
                "Disc(A_N)=(-1)^(N(N-1)/2) Res(A_N,A_N')"
            ),
            "fixed_point_derivative": "2 A_N'(-1)=q_N+q_(N-1)",
            "hensel_digit": (
                "if p|q_N, t_p=-(q_N/p)/A_N'(-1)="
                "-2(q_N/p)q_(N-1)^(-1) mod p"
            ),
            "square_criterion": "p^2|q_N iff t_p=0",
            "shift_continuant": (
                "Q_0=1,Q_1=T+1,Q_N=(T+4N-2)Q_(N-1)+Q_(N-2); "
                "Q_N(0)=q_N and Q_N'(0)=b_N/4"
            ),
        },
        "dependency_sha256": {
            "sources/item202_actual_squarefull_filter_report.md": (
                "abbc68e283f16871798be0c6da8af5df55ba6bf865a5864eefc0f8e19fe88f62"
            )
        },
        "symbolic_resultant_regression": symbolic_resultant_regression(
            symbolic_limit
        ),
        "finite_exact_no_go_witnesses": hensel_and_discriminant_witnesses(),
        "finite_actual_lower_scan": finite_actual_lower_scan(prime_limit),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=20000)
    parser.add_argument("--symbolic-limit", type=int, default=8)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.prime_limit < 7:
        raise SystemExit("--prime-limit must be at least 7")
    if not 1 <= args.symbolic_limit <= 10:
        raise SystemExit("--symbolic-limit must lie in 1..10")
    result = certificate(args.prime_limit, args.symbolic_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    finite = result["finite_actual_lower_scan"]
    print(
        json.dumps(
            {
                "output": str(args.output),
                "finite_prime_limit": finite["prime_limit"],
                "finite_actual_lower_roots": finite["actual_root_rows"],
                "finite_actual_large_prime_square_rows": len(
                    finite["actual_large_prime_square_rows"]
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
