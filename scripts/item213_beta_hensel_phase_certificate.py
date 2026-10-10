#!/usr/bin/env python3
"""Portable exact replay for Item 213's actual beta Hensel phase.

The proved part is elementary integer-polynomial algebra.  This checker
reconstructs the Charlier-type polynomial, verifies the exact Taylor and
harmonic phase formulas, checks the complementary-factorial expansion, and
performs a bounded census of the actual beta denominator.  Every
nonoccurrence in the census is explicitly finite evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item213_beta_hensel_phase_certificate.json"
DEFAULT_OUTPUT = (
    HERE / RESULT_NAME
    if HERE.name.lower() == "work"
    else HERE.parent / "results" / RESULT_NAME
)


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


def exact_sequences(limit: int) -> tuple[list[int], list[int]]:
    q = [1, 1]
    companion = [1, 3]
    for n in range(2, limit + 1):
        coefficient = 4 * n - 2
        q.append(coefficient * q[-1] + q[-2])
        companion.append(coefficient * companion[-1] + companion[-2])
    return q[: limit + 1], companion[: limit + 1]


def polynomial_add(left: list[int], right: list[int]) -> list[int]:
    result = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def polynomial_scale(polynomial: list[int], scalar: int) -> list[int]:
    return [scalar * value for value in polynomial]


def polynomial_times_x_minus(polynomial: list[int], shift: int) -> list[int]:
    result = [0] * (len(polynomial) + 1)
    for index, value in enumerate(polynomial):
        result[index] -= shift * value
        result[index + 1] += value
    return result


def polynomial_value(polynomial: list[int], x: int) -> int:
    value = 0
    for coefficient in reversed(polynomial):
        value = value * x + coefficient
    return value


def polynomial_derivative_value(polynomial: list[int], x: int) -> int:
    value = 0
    for degree in range(len(polynomial) - 1, 0, -1):
        value = value * x + degree * polynomial[degree]
    return value


def charlier_polynomial(n: int) -> list[int]:
    """C_n(X)=sum_j binom(n,j) X^(falling j), ascending coefficients."""
    falling = [1]
    result = [1]
    binomial = 1
    for j in range(1, n + 1):
        falling = polynomial_times_x_minus(falling, j - 1)
        binomial = binomial * (n - j + 1) // j
        result = polynomial_add(result, polynomial_scale(falling, binomial))
    return result


def charlier_regression(limit: int = 14) -> dict:
    q, _ = exact_sequences(limit)
    polynomials = [charlier_polynomial(n) for n in range(limit + 1)]
    rows = []
    for n, polynomial in enumerate(polynomials):
        if polynomial[-1] != 1 or len(polynomial) != n + 1:
            raise AssertionError((n, "monicity/degree", polynomial))
        expected = (1 if n % 2 == 0 else -1) * q[n]
        actual = polynomial_value(polynomial, -n - 1)
        if actual != expected:
            raise AssertionError((n, "actual-seed specialization", actual, expected))
        if n >= 1 and n < limit:
            recurrence = polynomial_add(
                polynomial_times_x_minus(polynomial, n - 1),
                polynomial_scale(polynomials[n - 1], n),
            )
            if recurrence != polynomials[n + 1]:
                raise AssertionError((n, "Charlier recurrence"))
        rows.append(
            {
                "N": n,
                "C_N_coefficients_ascending": polynomial,
                "C_N_at_minus_N_minus_1": actual,
                "signed_q_N": expected,
                "derivative_at_minus_N_minus_1": polynomial_derivative_value(
                    polynomial, -n - 1
                ),
            }
        )
    stream = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode("ascii")
    return {
        "classification": "FINITE_EXACT_REPLAY_OF_PROVED_POLYNOMIAL_IDENTITIES",
        "N_range": [0, limit],
        "checks": len(rows),
        "selected_rows": [rows[index] for index in (0, 2, 4, 8, 14)],
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "all_exact": True,
    }


def phase_components_mod(prime: int, degree: int, x: int) -> tuple[int, int, int]:
    """Return C_degree(x) mod p^2, its carry /p mod p, and C' mod p.

    The carry is legitimate only if the returned C value is divisible by p.
    Binomial coefficients are kept exact.  In the target scan degree<p/2,
    so this remains inexpensive and avoids any modular-division convention.
    """
    modulus = prime * prime
    falling = 1
    falling_derivative = 0
    binomial = 1
    value = 1
    derivative = 0
    for j in range(1, degree + 1):
        factor = x - j + 1
        falling_derivative = (
            falling_derivative * factor + falling
        ) % modulus
        falling = falling * factor % modulus
        binomial = binomial * (degree - j + 1) // j
        value = (value + (binomial % modulus) * falling) % modulus
        derivative = (
            derivative + (binomial % prime) * (falling_derivative % prime)
        ) % prime
    if value % prime:
        raise AssertionError((prime, degree, x, "C value is not a root", value))
    return value, value // prime % prime, derivative


def harmonic_derivative_mod(prime: int, degree: int, x: int) -> int:
    """Evaluate the target-range falling-factorial/harmonic derivative."""
    if not (degree <= x < prime):
        raise ValueError("harmonic formula requires degree<=x<p")
    falling = 1
    binomial = 1
    reciprocal_sum = 0
    derivative = 0
    for j in range(1, degree + 1):
        factor = x - j + 1
        falling = falling * factor % prime
        binomial = binomial * (degree - j + 1) // j
        reciprocal_sum = (reciprocal_sum + pow(factor, -1, prime)) % prime
        derivative = (
            derivative + (binomial % prime) * falling * reciprocal_sum
        ) % prime
    return derivative


def continuant_derivative_mod(prime: int, h: int) -> int:
    previous_previous_value = 1
    previous_previous_derivative = 0
    previous_value = (-4 * h) % prime
    previous_derivative = 1
    for index in range(-h + 1, h + 1):
        coefficient = 4 * index
        new_value = (
            coefficient * previous_value + previous_previous_value
        ) % prime
        new_derivative = (
            previous_value
            + coefficient * previous_derivative
            + previous_previous_derivative
        ) % prime
        previous_previous_value, previous_value = previous_value, new_value
        previous_previous_derivative, previous_derivative = (
            previous_derivative,
            new_derivative,
        )
    return previous_derivative


def continuant_derivative_exact(h: int) -> int:
    previous_previous_value = 1
    previous_previous_derivative = 0
    previous_value = -4 * h
    previous_derivative = 1
    for index in range(-h + 1, h + 1):
        coefficient = 4 * index
        new_value = coefficient * previous_value + previous_previous_value
        new_derivative = (
            previous_value
            + coefficient * previous_derivative
            + previous_previous_derivative
        )
        previous_previous_value, previous_value = previous_value, new_value
        previous_previous_derivative, previous_derivative = (
            previous_derivative,
            new_derivative,
        )
    return previous_derivative


def moving_resultant_obstruction_witness() -> dict:
    prime = 107
    h = 2
    n = (prime - 2 * h - 3) // 2
    d_h = continuant_derivative_exact(h)
    q, _ = exact_sequences(n)
    if d_h != 963 or d_h % prime:
        raise AssertionError(("moving resultant witness", d_h))
    if q[n] % prime == 0:
        raise AssertionError("the p=107 row must not be an actual beta root")
    return {
        "classification": "EXACT_STRUCTURAL_WITNESS_NOT_AN_ACTUAL_ROOT",
        "p": prime,
        "N": n,
        "h": h,
        "p_gt_2N_plus_1": prime > 2 * n + 1,
        "D_h": d_h,
        "D_h_factorization": "3^2*107",
        "q_N_mod_p": q[n] % prime,
        "conclusion": (
            "The adjacent/resultant factor D_h is not automatically a p-unit "
            "in the target geometry.  This row is not an actual q_N root and "
            "therefore is not a coupled-square example."
        ),
    }


def complementary_factorial_regression(prime_limit: int = 251) -> dict:
    checks = 0
    for prime in primes_upto(prime_limit):
        if prime < 3:
            continue
        modulus = prime * prime
        factorial = [1]
        for value in range(1, prime):
            factorial.append(factorial[-1] * value)
        wilson = (factorial[prime - 1] + 1) // prime % prime
        harmonic = 0
        for a in range(0, prime):
            if a:
                harmonic = (harmonic + pow(a, -1, prime)) % prime
            lhs = factorial[prime - 1 - a] % modulus
            sign = -1 if (a + 1) % 2 else 1
            rhs = (
                sign
                * pow(factorial[a], -1, modulus)
                * (1 + prime * ((harmonic - wilson) % prime))
            ) % modulus
            if lhs != rhs:
                raise AssertionError((prime, a, "complementary factorial", lhs, rhs))
            checks += 1
    return {
        "classification": "FINITE_EXACT_REPLAY_OF_PROVED_COMPLEMENT_FORMULA",
        "prime_range": [3, prime_limit],
        "factorial_complement_checks": checks,
        "formula": (
            "(p-1-a)! = (-1)^(a+1)/a! * "
            "(1+p(H_a-W_p)) mod p^2"
        ),
        "all_exact": True,
    }


def outside_target_square_witnesses() -> dict:
    rows = []
    for prime, n in ((13, 8), (7, 79), (31, 79)):
        q, companion = exact_sequences(n)
        x = prime - 1 - n
        c_value, carry, derivative = phase_components_mod(prime, n, x)
        sign = 1 if n % 2 == 0 else -1
        divided = q[n] // prime % prime
        phase = (carry - derivative) % prime
        tau = sign * companion[n] * divided % prime
        if q[n] % (prime * prime):
            raise AssertionError((prime, n, "expected actual square"))
        if divided or phase or tau:
            raise AssertionError((prime, n, "phase must collide", divided, phase, tau))
        rows.append(
            {
                "p": prime,
                "N": n,
                "s=p-1-N": x,
                "p_gt_2N_plus_1": prime > 2 * n + 1,
                "C_N_s_mod_p2": c_value,
                "carry_C_over_p_mod_p": carry,
                "C_N_prime_s_mod_p": derivative,
                "phase": phase,
                "q_N_over_p_mod_p": divided,
                "tau": tau,
            }
        )
    return {
        "classification": "FINITE_EXACT_OUT_OF_TARGET_WITNESSES_ONLY",
        "rows": rows,
        "scope_warning": (
            "These rows verify that the exact phase detects known actual "
            "squares, but every row violates p>2N+1 and gives no target-range example."
        ),
    }


def actual_prescribed_scan(prime_limit: int) -> dict:
    root_rows = []
    carry_zero_rows = []
    lower_derivative_zero_rows = []
    upper_derivative_zero_rows = []
    derivative_collision_rows = []
    lower_square_rows = []
    upper_square_rows = []
    coupled_rows = []
    harmonic_checks = 0
    direct_mirror_checks = 0
    continuant_checks = 0

    for prime in primes_upto(prime_limit):
        if prime < 7:
            continue
        modulus = prime * prime
        q = [1, 1]
        companion = [1, 3 % prime]
        for n in range(2, prime):
            coefficient = 4 * n - 2
            q.append((coefficient * q[-1] + q[-2]) % modulus)
            companion.append(
                (coefficient * companion[-1] + companion[-2]) % prime
            )

        center = (prime - 1) // 2
        for n in range(1, center):
            if q[n] % prime:
                continue
            reflected = prime - 1 - n
            c_value, carry, lower_derivative = phase_components_mod(
                prime, n, reflected
            )
            sign = 1 if n % 2 == 0 else -1
            divided_lower = q[n] // prime % prime
            divided_upper = q[reflected] // prime % prime
            phase = (carry - lower_derivative) % prime
            tau = sign * companion[n] * divided_lower % prime
            tau_from_phase = companion[n] * phase % prime
            if divided_lower != sign * phase % prime:
                raise AssertionError((prime, n, "Taylor phase"))
            if tau != tau_from_phase:
                raise AssertionError((prime, n, "actual-seed tau phase"))

            upper_derivative = (carry - sign * divided_upper) % prime
            if prime <= 251:
                mirror_value, mirror_carry, mirror_derivative = phase_components_mod(
                    prime, reflected, n
                )
                if mirror_value != c_value or mirror_carry != carry:
                    raise AssertionError((prime, n, "symmetric kernel value/carry"))
                if mirror_derivative != upper_derivative:
                    raise AssertionError((prime, n, "upper Taylor derivative"))
                direct_mirror_checks += 1

                harmonic_derivative = harmonic_derivative_mod(
                    prime, n, reflected
                )
                if harmonic_derivative != lower_derivative:
                    raise AssertionError((prime, n, "harmonic derivative"))
                harmonic_checks += 1

                h = (prime - 3) // 2 - n
                d_h = continuant_derivative_mod(prime, h)
                q_previous = q[n - 1] % prime
                derivative_gap = (upper_derivative - lower_derivative) % prime
                expected_gap = -2 * sign * d_h * q_previous % prime
                if derivative_gap != expected_gap:
                    raise AssertionError((prime, n, "phase triangle/continuant gap"))
                continuant_checks += 1

            lower_square = divided_lower == 0
            upper_square = divided_upper == 0
            derivative_collision = upper_derivative == lower_derivative
            coupled = lower_square and upper_square
            if lower_square != (carry == lower_derivative):
                raise AssertionError((prime, n, "lower collision"))
            if upper_square != (carry == upper_derivative):
                raise AssertionError((prime, n, "upper collision"))
            if coupled != (
                carry == lower_derivative == upper_derivative
            ):
                raise AssertionError((prime, n, "triple collision"))

            row = {
                "p": prime,
                "N": n,
                "s": reflected,
                "carry_kappa": carry,
                "lower_derivative": lower_derivative,
                "upper_derivative": upper_derivative,
                "phase_kappa_minus_lower_derivative": phase,
                "lambda_N": divided_lower,
                "lambda_s": divided_upper,
                "P_N_mod_p": companion[n],
                "tau": tau,
                "carry_zero": carry == 0,
                "lower_derivative_zero": lower_derivative == 0,
                "upper_derivative_zero": upper_derivative == 0,
                "derivative_collision": derivative_collision,
                "lower_square": lower_square,
                "upper_square": upper_square,
                "coupled_square": coupled,
            }
            root_rows.append(row)
            if carry == 0:
                carry_zero_rows.append(row)
            if lower_derivative == 0:
                lower_derivative_zero_rows.append(row)
            if upper_derivative == 0:
                upper_derivative_zero_rows.append(row)
            if derivative_collision:
                derivative_collision_rows.append(row)
            if lower_square:
                lower_square_rows.append(row)
            if upper_square:
                upper_square_rows.append(row)
            if coupled:
                coupled_rows.append(row)

    selected_keys = {(7, 2), (13, 4), (71, 3), (2879, 48)}
    selected_rows = [
        row for row in root_rows if (row["p"], row["N"]) in selected_keys
    ]
    if {(row["p"], row["N"]) for row in selected_rows} != selected_keys:
        raise AssertionError(("missing selected phase fixtures", selected_rows))
    stream = json.dumps(root_rows, separators=(",", ":"), sort_keys=True).encode(
        "ascii"
    )
    return {
        "classification": "EXPERIMENTAL_FINITE_NOT_AN_ALL_PRIME_OR_RATE_THEOREM",
        "prime_limit": prime_limit,
        "prescribed_lower_root_rows": len(root_rows),
        "harmonic_derivative_checks_through_251": harmonic_checks,
        "direct_mirror_phase_checks_through_251": direct_mirror_checks,
        "continuant_gap_checks_through_251": continuant_checks,
        "carry_zero_rows": carry_zero_rows,
        "lower_derivative_zero_rows": lower_derivative_zero_rows,
        "upper_derivative_zero_rows": upper_derivative_zero_rows,
        "derivative_collision_rows": derivative_collision_rows,
        "lower_square_rows": lower_square_rows,
        "upper_square_rows": upper_square_rows,
        "coupled_square_rows": coupled_rows,
        "selected_rows": selected_rows,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "scope_warning": (
            "All zero counts are bounded computations.  In particular, no "
            "all-prime nonvanishing, density, or radical estimate follows."
        ),
    }


def certificate(prime_limit: int) -> dict:
    return {
        "item": 213,
        "classification": {
            "PROVED": [
                "C_N(X)=sum binom(N,j) X^(falling j) is monic with C_N(-N-1)=(-1)^N q_N",
                "at a prescribed root p|q_N, s=p-1-N and kappa=C_N(s)/p, the exact phase is q_N/p=(-1)^N(kappa-C_N'(s)) mod p",
                "the actual Hensel digit is tau=P_N(kappa-C_N'(s)) mod p",
                "C_N'(s) has the displayed falling-factorial/harmonic formula with only p-units",
                "the complementary-factorial Wilson quotient cancels at a root and leaves exactly the same carry-minus-slope phase",
                "the mirrored polynomial C_s(N) has the same carry; lower and upper squares are the two carry/derivative collisions, and coupled squares are their triple collision",
                "the phase reduction adds no divisibility exponent and gives no improvement over S_N^2|q_N",
            ],
            "EXPERIMENTAL_FINITE": [
                f"actual prescribed lower-root phase census through p<={prime_limit}",
                "direct harmonic, mirrored-phase, and continuant-gap checks through p<=251",
                "the three known actual square rows outside p>2N+1",
            ],
            "OPEN": [
                "whether kappa-C_N'(s) is nonzero at every prescribed root",
                "whether any prescribed lower square or coupled square exists",
                "any density, product, or zero-rate theorem for the phase collisions",
                "any proper bound for the large-prime squarefull radical below square capacity",
            ],
        },
        "exact_phase": {
            "polynomial": "C_N(X)=sum_{j=0}^N binom(N,j) X^(falling j)",
            "generating_function": "sum_N C_N(X)t^N/N! = exp(t)(1+t)^X",
            "actual_seed_specialization": "C_N(-N-1)=(-1)^N q_N",
            "parameters": "p>2N+1, p|q_N, s=p-1-N, kappa=C_N(s)/p mod p",
            "divided_value": "q_N/p=(-1)^N(kappa-C_N'(s)) mod p",
            "hensel_digit": "tau=P_N(kappa-C_N'(s)) mod p",
            "lower_square": "p^2|q_N iff kappa=C_N'(s) mod p",
            "harmonic_slope": (
                "C_N'(s)=sum_{j=1}^N binom(N,j)s^(falling j)"
                "(H_s-H_(s-j)) mod p"
            ),
        },
        "phase_triangle": {
            "common_value": "C_N(s)=C_s(N), so both orientations have the same carry kappa",
            "lower_slope": "D_minus=C_N'(s)",
            "upper_slope": "D_plus=C_s'(N)",
            "lower_divided_value": "lambda_N=(-1)^N(kappa-D_minus)",
            "upper_divided_value": "lambda_s=(-1)^N(kappa-D_plus)",
            "continuant_gap": "D_plus-D_minus=-2(-1)^N D_h q_(N-1) mod p",
            "lower_square": "kappa=D_minus",
            "upper_square": "kappa=D_plus",
            "singular_continuant": "D_minus=D_plus",
            "coupled_square": "kappa=D_minus=D_plus",
        },
        "precise_actual_family_obstruction": {
            "statement": (
                "The carry and both slopes are actual beta/Charlier values, not "
                "formal CRT coordinates.  Nevertheless kappa-C_N'(s) is exactly "
                "(-1)^N q_N/p.  Thus proving its nonvanishing is precisely the "
                "original large-prime squarefreeness problem; the binomial, "
                "harmonic, and Wilson rewrite supplies no independent condition."
            ),
            "wilson_cancellation": (
                "In the complementary-factorial expansion the Wilson term is "
                "multiplied by C_N(s)=0 mod p, while the harmonic sum equals "
                "-C_N'(s) mod p."
            ),
            "scope": (
                "This closes only the direct first-order complement/Taylor rewrite. "
                "It does not preclude a new theorem controlling the actual carries."
            ),
        },
        "rate_ledger": {
            "squarefull_radical": (
                "S_N=product of p>2N+1 with p|q_N and kappa=C_N'(p-1-N) mod p"
            ),
            "proved_divisibility": "S_N^2 divides q_N",
            "new_divisibility_exponent_from_phase_formula": 0,
            "new_bookable_log_rate_per_m": 0,
            "coupled_R_squared_required_log_R_per_m": "0.05889895100829538164",
            "conclusion": (
                "the phase is an exact selector, but no all-index upper or lower "
                "mass estimate is proved"
            ),
        },
        "dependency_sha256": {
            "sources/item165_noncentral_singular_report.md": (
                "d7b4475d2adfeff9a5f1c70a9c6b318d0c2b140bf90b194aa9acb6fdddcc2650"
            ),
            "sources/item202_actual_squarefull_filter_report.md": (
                "abbc68e283f16871798be0c6da8af5df55ba6bf865a5864eefc0f8e19fe88f62"
            ),
            "sources/item204_squarefull_discriminant_report.md": (
                "45ad273d407323902745095bd7abbc1fe5d17cf4d8da35737276eb3e6c7fc665"
            ),
            "sources/item207_coupled_hensel_euler_report.md": (
                "854a6b7fefc75e06913641a9e31e875e6b06ea31b2b6f7000da3b011b07be0a9"
            ),
        },
        "charlier_polynomial_regression": charlier_regression(),
        "complementary_factorial_regression": complementary_factorial_regression(),
        "moving_resultant_obstruction_witness": moving_resultant_obstruction_witness(),
        "outside_target_square_witnesses": outside_target_square_witnesses(),
        "finite_actual_prescribed_scan": actual_prescribed_scan(prime_limit),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=20000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.prime_limit < 2879:
        raise SystemExit("--prime-limit must be at least 2879")
    result = certificate(args.prime_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    finite = result["finite_actual_prescribed_scan"]
    print(
        json.dumps(
            {
                "output": str(args.output),
                "finite_prime_limit": finite["prime_limit"],
                "finite_prescribed_lower_roots": finite[
                    "prescribed_lower_root_rows"
                ],
                "finite_lower_square_rows": len(finite["lower_square_rows"]),
                "finite_derivative_collision_rows": len(
                    finite["derivative_collision_rows"]
                ),
                "finite_coupled_square_rows": len(finite["coupled_square_rows"]),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
