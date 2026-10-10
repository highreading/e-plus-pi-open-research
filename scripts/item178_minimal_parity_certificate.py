#!/usr/bin/env python3
"""Deterministic exact certificate for Item 178.

For the minimal-parity slice s=j (mod 2), the reduced primitive and its
five-divisor values depend only on the parity of j and on rho=p (mod 4).
This checker constructs the resulting exact obstruction determinant for
every 1 <= j <= --max-j.  All arithmetic is over Z (the odd-parity
numerator vector is cleared by 5); no prime scan and no floating-point
calculation occurs.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    HERE / "item178_minimal_parity_certificate.json"
    if HERE.name == "work"
    else HERE.parent / "results" / "item178_minimal_parity_certificate.json"
)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            answer[first + second] += left_value * right_value
    return answer


def polynomial_power(base: list[int], exponent: int) -> list[int]:
    answer = [1]
    while exponent:
        if exponent & 1:
            answer = polynomial_multiply(answer, base)
        exponent >>= 1
        if exponent:
            base = polynomial_multiply(base, base)
    return answer


def determinant(columns: list[list[int]]) -> int:
    """Exact small determinant, with columns supplied explicitly."""
    dimension = len(columns)
    if any(len(column) != dimension for column in columns):
        raise ValueError("determinant must be square")
    answer = 0
    for permutation in itertools.permutations(range(dimension)):
        inversions = sum(
            permutation[first] > permutation[second]
            for first in range(dimension)
            for second in range(first + 1, dimension)
        )
        term = -1 if inversions & 1 else 1
        for row in range(dimension):
            term *= columns[permutation[row]][row]
        answer += term
    return answer


def rank_three_minors(columns: list[list[int]]) -> list[int]:
    """The four row minors of a 4 by 3 matrix."""
    answer = []
    for omitted in range(4):
        rows = [row for row in range(4) if row != omitted]
        restricted = [[column[row] for row in rows] for column in columns]
        answer.append(determinant(restricted))
    return answer


def factor_integer(value: int) -> list[list[int]]:
    value = abs(value)
    answer: list[list[int]] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            exponent = 0
            while value % divisor == 0:
                value //= divisor
                exponent += 1
            answer.append([divisor, exponent])
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        answer.append([value, 1])
    return answer


def binomial_poly(power: int, sign: int = 1) -> list[Fraction]:
    """Coefficients of (1+sign*z)^power, used only in degree <=3."""
    from math import comb

    return [Fraction(comb(power, degree) * sign**degree) for degree in range(power + 1)]


def multiply_fraction(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for first, left_value in enumerate(left):
        for second, right_value in enumerate(right):
            answer[first + second] += left_value * right_value
    return answer


def add_fraction(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * max(len(left), len(right))
    for index in range(len(answer)):
        if index < len(left):
            answer[index] += left[index]
        if index < len(right):
            answer[index] += right[index]
    return answer


def derive_m_vector(numerator_x: list[Fraction]) -> list[Fraction]:
    """M(y)=(1+y)^3*N((y-1)/(y+1)), returned in t=y-1."""
    # First form M in y: sum n_k (y-1)^k (y+1)^(3-k).
    m_y = [Fraction(0)]
    for degree, coefficient in enumerate(numerator_x):
        term = multiply_fraction(
            [(-1) ** degree * value for value in binomial_poly(degree, -1)],
            binomial_poly(3 - degree, 1),
        )
        m_y = add_fraction(m_y, [coefficient * value for value in term])

    # Substitute y=1+t.
    m_t = [Fraction(0)]
    for degree, coefficient in enumerate(m_y):
        term = [coefficient * value for value in binomial_poly(degree, 1)]
        m_t = add_fraction(m_t, term)
    m_t += [Fraction(0)] * (4 - len(m_t))
    if len(m_t) != 4:
        raise AssertionError(m_t)
    return m_t


NUMERATOR_X = {
    "odd": {
        1: [Fraction(274, 5), Fraction(-32, 5), Fraction(-38, 5)],
        3: [Fraction(306, 5), Fraction(32, 5), Fraction(-6, 5)],
    },
    "even": {
        1: [Fraction(-9, 2), Fraction(-2), Fraction(-1, 2)],
        3: [Fraction(-5, 2), Fraction(2), Fraction(3, 2)],
    },
}

EXPECTED_M_T = {
    "odd": {
        1: [Fraction(2192, 5), Fraction(632), Fraction(288), Fraction(204, 5)],
        3: [Fraction(2448, 5), Fraction(760), Fraction(1952, 5), Fraction(332, 5)],
    },
    "even": {
        1: [Fraction(-36), Fraction(-62), Fraction(-36), Fraction(-7)],
        3: [Fraction(-20), Fraction(-22), Fraction(-4), Fraction(1)],
    },
}


def m_vectors() -> dict[str, dict[int, list[int]]]:
    answer: dict[str, dict[int, list[int]]] = {"odd": {}, "even": {}}
    for parity in ("odd", "even"):
        clearing = 5 if parity == "odd" else 1
        for rho in (1, 3):
            derived = derive_m_vector(NUMERATOR_X[parity][rho])
            if derived != EXPECTED_M_T[parity][rho]:
                raise AssertionError((parity, rho, derived))
            cleared = [value * clearing for value in derived]
            if any(value.denominator != 1 for value in cleared):
                raise AssertionError(cleared)
            answer[parity][rho] = [value.numerator for value in cleared]
    return answer


def obstruction_data(
    j: int,
    polynomial: list[int],
    polynomial_minus_one: list[int],
    vectors: dict[str, dict[int, list[int]]],
) -> dict[str, Any]:
    a_value = 3 * j + 2
    k_value = 2 * j + 2
    p2, p3, p4 = (polynomial[a_value + offset] for offset in (2, 3, 4))

    q_vector = [
        2 * (a_value + 1),
        4 * (a_value + 1 - k_value),
        3 * (a_value + 1 - 2 * k_value),
        a_value + 1 - 3 * k_value,
    ]
    c_vector = [
        0,
        -2 * (a_value + 2) * p2,
        -(4 * (a_value + 2 - k_value) * p2 + 2 * (a_value + 3) * p3),
        -(
            3 * (a_value + 2 - 2 * k_value) * p2
            + 4 * (a_value + 3 - k_value) * p3
            + 2 * (a_value + 4) * p4
        ),
    ]
    d_vector = [2, 4, 3, 1]
    parity = "odd" if j & 1 else "even"

    omega: dict[int, int] = {}
    simplified: dict[int, int] = {}
    for rho in (1, 3):
        omega[rho] = determinant(
            [q_vector, c_vector, d_vector, vectors[parity][rho]]
        )

    if parity == "odd":
        simplified[1] = 64 * (j + 1) * (
            -11 * (5 * j + 4) * p2
            + (51 * j + 101) * p3
            + 18 * (j + 2) * p4
        )
        simplified[3] = 64 * (j + 1) * (
            -11 * (5 * j + 4) * p2
            + (53 - 29 * j) * p3
            + 114 * (j + 2) * p4
        )
    else:
        simplified[1] = 16 * (j + 1) * (
            (5 * j + 4) * p2
            + (9 * j - 1) * p3
            - 18 * (j + 2) * p4
        )
        simplified[3] = 16 * (j + 1) * (
            (5 * j + 4) * p2
            - (11 * j + 13) * p3
            + 6 * (j + 2) * p4
        )
    if omega != simplified:
        raise AssertionError((j, omega, simplified))

    # Euler coefficient reduction.  Put n=j+1 and k=3n+3.  For any S,
    # [t^k](t*d/dt-k)(S*Delta^(2n))=0.  The choices of S recorded in the
    # report reduce the four braces to the following manifestly signed
    # coefficients of Delta^(2n-1).
    n_value = j + 1
    target_degree = 3 * n_value + 3
    left_central = polynomial_minus_one[target_degree - 5]
    right_central = polynomial_minus_one[target_degree - 4]
    if parity == "odd":
        braces = {
            1: simplified[1] // (64 * (j + 1)),
            3: simplified[3] // (64 * (j + 1)),
        }
        reduced_braces = {
            1: -n_value * (6 * right_central + 22 * left_central),
            3: -n_value * (38 * right_central + 22 * left_central),
        }
    else:
        braces = {
            1: simplified[1] // (16 * (j + 1)),
            3: simplified[3] // (16 * (j + 1)),
        }
        reduced_braces = {
            1: n_value * (6 * right_central + 2 * left_central),
            3: 2 * n_value * (left_central - right_central),
        }
    if braces != reduced_braces:
        raise AssertionError((j, braces, reduced_braces))
    if left_central <= right_central:
        raise AssertionError((j, left_central, right_central))

    return {
        "j": j,
        "parity": parity,
        "A": a_value,
        "K": k_value,
        "p2_p3_p4": [p2, p3, p4],
        "q": q_vector,
        "c": c_vector,
        "rank3_minors_q_c_d": rank_three_minors([q_vector, c_vector, d_vector]),
        "omega": omega,
        "coefficient_reduction": {
            "n": n_value,
            "L": 2 * n_value - 1,
            "central_left": left_central,
            "central_right": right_central,
            "braces": braces,
        },
    }


def certificate(max_j: int) -> dict[str, Any]:
    if max_j < 2:
        raise ValueError("--max-j must be at least 2")
    vectors = m_vectors()
    d_poly = [2, 4, 3, 1]
    d_squared = polynomial_multiply(d_poly, d_poly)
    polynomial = polynomial_power(d_poly, 4)  # K=4 when j=1.
    polynomial_minus_one = polynomial_power(d_poly, 3)

    requested_checkpoints = set(range(1, min(max_j, 10) + 1))
    requested_checkpoints.update(
        value for value in (20, 50, 100, 250, 500, 750, 1000, max_j)
        if value <= max_j
    )
    checkpoints = []
    zero_failures = []
    sign_failures = []
    rank_failures = []
    digest = hashlib.sha256()

    first_factorizations: dict[str, Any] = {}
    first_omega: dict[int, dict[int, int]] = {}
    for j in range(1, max_j + 1):
        if j > 1:
            polynomial = polynomial_multiply(polynomial, d_squared)
            polynomial_minus_one = polynomial_multiply(polynomial_minus_one, d_squared)
        row = obstruction_data(j, polynomial, polynomial_minus_one, vectors)
        expected_sign = -1 if j & 1 else 1
        if not any(row["rank3_minors_q_c_d"]):
            rank_failures.append(j)
        for rho in (1, 3):
            omega = row["omega"][rho]
            digest.update(f"{j},{rho},{omega}\n".encode("ascii"))
            if omega == 0:
                zero_failures.append([j, rho])
            if (omega > 0) - (omega < 0) != expected_sign:
                sign_failures.append([j, rho])
            if j <= 3:
                first_factorizations[f"j={j},rho={rho}"] = {
                    "omega": str(omega),
                    "factorization_of_abs_omega": factor_integer(omega),
                }
        if j <= 2:
            first_omega[j] = dict(row["omega"])
        if j in requested_checkpoints:
            checkpoints.append(
                {
                    "j": j,
                    "parity": row["parity"],
                    "A": row["A"],
                    "K": row["K"],
                    "p2_p3_p4": [str(value) for value in row["p2_p3_p4"]],
                    "omega_rho_1": str(row["omega"][1]),
                    "omega_rho_3": str(row["omega"][3]),
                    "rank3_minors_q_c_d": [
                        str(value) for value in row["rank3_minors_q_c_d"]
                    ],
                    "central_left_minus_right_for_Delta_to_2n_minus_1": str(
                        row["coefficient_reduction"]["central_left"]
                        - row["coefficient_reduction"]["central_right"]
                    ),
                }
            )

    if zero_failures or sign_failures or rank_failures:
        raise AssertionError(
            {
                "zero_failures": zero_failures,
                "sign_failures": sign_failures,
                "rank_failures": rank_failures,
            }
        )

    item177_b0 = {
        1: {1: Fraction(2735, 4), 3: Fraction(-5295, 4)},
        2: {1: Fraction(-918897, 128), 3: Fraction(59829, 128)},
    }
    item177_positive_factor = {1: Fraction(5, 12288), 2: Fraction(49, 122880)}
    item177_crosscheck = []
    for j in (1, 2):
        for rho in (1, 3):
            chi4 = 1 if rho == 1 else -1
            reconstructed = -chi4 * item177_positive_factor[j] * first_omega[j][rho]
            if reconstructed != item177_b0[j][rho]:
                raise AssertionError((j, rho, reconstructed, item177_b0[j][rho]))
            item177_crosscheck.append({
                "j": j,
                "rho": rho,
                "omega_sharp": str(first_omega[j][rho]),
                "positive_normalization": fraction_text(item177_positive_factor[j]),
                "chi4": chi4,
                "B0_equals_minus_chi4_times_normalization_times_omega": fraction_text(reconstructed),
            })

    return {
        "item": 178,
        "arithmetic": "exact integer arithmetic only; no prime scan",
        "minimal_parity_slice": {
            "s": "1 for odd j and 0 for even j",
            "m": "((j+1)*p-s-1)/2",
            "sufficient_admissibility_threshold": "odd prime p >= max(7,2*j+3)",
        },
        "cayley_normal_form": {
            "y": "(x+1)/(1-x)",
            "t": "y-1",
            "D_in_t": d_poly,
            "A": "3*j+2",
            "K": "2*j+2",
            "base_differential_up_to_nonzero_scalar": "(1-y)^A / D(y)^K dy",
            "second_multiplier": "M(y)/(4*D(y))",
        },
        "M_t_coefficients": {
            parity: {
                str(rho): vectors[parity][rho] for rho in (1, 3)
            }
            for parity in ("odd", "even")
        },
        "M_clearing_factor": {"odd": 5, "even": 1},
        "obstruction": {
            "p_r": "p_r=[t^(A+r)]D(t)^K for r=2,3,4",
            "omega_sharp": "det[q,c,d,M_sharp]",
            "logic": (
                "B0=0 implies omega_sharp=0. Therefore omega_sharp!=0 "
                "is a sufficient exact certificate that the constrained "
                "characteristic-zero band constant is nonzero."
            ),
            "necessity_scope": (
                "The checker does not use the converse. It also verifies "
                "rank(q,c,d)=3 throughout the finite certified range."
            ),
            "simplified_formulas": {
                "odd,rho=1": "64(j+1)(-11(5j+4)p2+(51j+101)p3+18(j+2)p4)",
                "odd,rho=3": "64(j+1)(-11(5j+4)p2+(53-29j)p3+114(j+2)p4)",
                "even,rho=1": "16(j+1)((5j+4)p2+(9j-1)p3-18(j+2)p4)",
                "even,rho=3": "16(j+1)((5j+4)p2-(11j+13)p3+6(j+2)p4)",
            },
        },
        "all_j_theorem": {
            "omega_sign": "sign(omega_sharp)=(-1)^j for both rho and every j>=1",
            "Euler_reductions": {
                "odd,rho=1": "brace=-n*(6*a_right+22*a_left)",
                "odd,rho=3": "brace=-n*(38*a_right+22*a_left)",
                "even,rho=1": "brace=n*(6*a_right+2*a_left)",
                "even,rho=3": "brace=2*n*(a_left-a_right)",
            },
            "central_asymmetry_proof": (
                "For L=2n-1 and m=(3L-1)/2, Delta^L is the sum over "
                "r=0..L of binom(L,r)*(1+t)^(L+2r). For r<L, m is at "
                "or right of the binomial center, so coefficient m is at "
                "least coefficient m+1, with a strict supported term; "
                "for r=L the two central binomial coefficients are equal. "
                "Thus a_left>a_right."
            ),
            "consequence": (
                "The actual constrained minimal-parity B0 rational constant "
                "is nonzero for every fixed j>=1 and both rho classes."
            ),
        },
        "finite_replay_check": {
            "range": f"1 <= j <= {max_j}",
            "number_of_bands": max_j,
            "number_of_rho_cases": 2 * max_j,
            "zero_failures": zero_failures,
            "rank_failures": rank_failures,
            "omega_stream_sha256": digest.hexdigest(),
        },
        "finite_sign_replay": {
            "theorem_replayed": "sign(omega_sharp)=(-1)^j for both rho",
            "verified_range": f"1 <= j <= {max_j}",
            "sign_failures": sign_failures,
        },
        "first_factorizations": first_factorizations,
        "item177_crosscheck": item177_crosscheck,
        "checkpoints": checkpoints,
        "verdict": (
            "PROVED for every fixed j>=1 and rho in {1,3}: the actual "
            "minimal-parity fixed-band B0 constant is nonzero over Q, hence "
            "B0 is nonzero modulo every sufficiently large admissible prime "
            f"in that rho class. Exact DP replayed 1<=j<={max_j}."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-j", type=int, default=1000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()

    result = certificate(arguments.max_j)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "output": str(arguments.output),
        "max_j": arguments.max_j,
        "omega_stream_sha256": result["finite_replay_check"]["omega_stream_sha256"],
        "verdict": result["verdict"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
