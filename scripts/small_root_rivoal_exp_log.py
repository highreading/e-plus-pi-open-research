#!/usr/bin/env python3
"""Exact arithmetic and numerical checks for N=2,3,4,6 in Rivoal's form.

The accompanying proof is in
``sources/small_root_of_unity_exp_log_continuation.md``.  Exact arithmetic
uses Fraction coordinates in the full ring of integers of Q(i,zeta_N).
Numerical values are diagnostics; the script labels them accordingly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

import mpmath as mp


Pair = tuple[Fraction, Fraction]


def pair_add(left: Pair, right: Pair) -> Pair:
    return left[0] + right[0], left[1] + right[1]


def pair_scale(scale: Fraction, value: Pair) -> Pair:
    return scale * value[0], scale * value[1]


def pair_multiply(left: Pair, right: Pair, relation: Pair) -> Pair:
    """Multiply a+b*z and c+d*z when z^2=relation[0]+relation[1]*z."""
    a, b = left
    c, d = right
    return (
        a * c + b * d * relation[0],
        a * d + b * c + b * d * relation[1],
    )


def pair_evaluate(
    polynomial: list[Fraction], value: Pair, relation: Pair
) -> Pair:
    answer = (Fraction(0), Fraction(0))
    power = (Fraction(1), Fraction(0))
    for coefficient in polynomial:
        answer = pair_add(answer, pair_scale(coefficient, power))
        power = pair_multiply(power, value, relation)
    return answer


def rational_evaluate(polynomial: list[Fraction], value: int) -> Fraction:
    """Evaluate a rational polynomial at an integer exactly."""
    answer = Fraction(0)
    for coefficient in reversed(polynomial):
        answer = answer * value + coefficient
    return answer


def lcm_through(n: int) -> int:
    answer = 1
    for value in range(1, n + 1):
        answer = math.lcm(answer, value)
    return answer


def rivoal_polynomials(
    c: int, d: int, f: int
) -> tuple[list[Fraction], list[Fraction], list[Fraction]]:
    if c < 0 or d < 2 * c or f < c:
        raise ValueError("parameters must satisfy c>=0, d>=2c, f>=c")
    C = c + d
    F = f + 2 * c
    A = [Fraction(0) for _ in range(C + 1)]
    for j in range(d + 1):
        for k in range(c + 1):
            index = c + j - k
            A[index] += (
                (-1) ** (d - j + k)
                * math.comb(c, k)
                * math.comb(c + d - j + k, c)
                * math.comb(d + f - j, f)
                * Fraction(1, math.factorial(j))
            )

    B = [Fraction(0) for _ in range(C + 1)]
    for n in range(C + 1):
        B[n] = -sum(
            (A[m] * Fraction(1, n - m) for m in range(n)), Fraction(0)
        )

    E = [Fraction(0) for _ in range(F + 1)]
    for n in range(F + 1):
        E[n] = sum(
            (
                A[m] * Fraction(1, math.factorial(n - m))
                for m in range(min(n, C) + 1)
            ),
            Fraction(0),
        )
    return A, B, E


def field_data(N: int) -> tuple[Pair, Pair]:
    """Return eta=1-zeta and the quadratic relation for zeta."""
    if N == 3:
        return (Fraction(1), Fraction(-1)), (Fraction(-1), Fraction(-1))
    if N == 4:
        # Here the quadratic generator is i itself.
        return (Fraction(1), Fraction(-1)), (Fraction(-1), Fraction(0))
    if N == 6:
        return (Fraction(1), Fraction(-1)), (Fraction(-1), Fraction(1))
    raise ValueError("N must be 3, 4, or 6")


def coordinate_denominator(values: tuple[Fraction, ...]) -> int:
    answer = 1
    for value in values:
        answer = math.lcm(answer, value.denominator)
    return answer


def exact_clearing(c: int, d: int, f: int, N: int) -> dict:
    """Return the least universal integer q with q*U,q*V integral.

    Lambda=U*s+V.  For N=3,6 coordinates use the integral basis
    1,zeta,i,i*zeta.  For N=4 they use 1,i.
    """
    A, B, E = rivoal_polynomials(c, d, f)
    A_one = sum(A, Fraction(0))
    E_one = sum(E, Fraction(0))

    if N == 2:
        A_two = rational_evaluate(A, 2)
        B_two = rational_evaluate(B, 2)
        U_i = 2 * A_one * A_two
        V_plain = -2 * A_one * B_two
        V_i = -2 * A_two * E_one
        coordinates = (U_i, V_plain, V_i)
        coordinate_labels = ("U_i", "V_1", "V_i")
    else:
        eta, relation = field_data(N)
        A_eta = pair_evaluate(A, eta, relation)
        B_eta = pair_evaluate(B, eta, relation)

    if N == 4:
        def times_i(value: Pair) -> Pair:
            return -value[1], value[0]

        U = pair_scale(2 * A_one, times_i(A_eta))
        V = pair_add(
            pair_scale(-2 * E_one, times_i(A_eta)),
            pair_scale(-4 * A_one, B_eta),
        )
        coordinates = U + V
        coordinate_labels = ("U_1", "U_i", "V_1", "V_i")
    elif N in (3, 6):
        # U and the first part of V are in the i,i*zeta sector.  The
        # logarithmic part of V is in the 1,zeta sector, so no coordinates
        # overlap or cancel.
        U_i = pair_scale(2 * A_one, A_eta)
        V_i = pair_scale(-2 * E_one, A_eta)
        V_plain = pair_scale(-N * A_one, B_eta)
        coordinates = U_i + V_i + V_plain
        coordinate_labels = (
            "U_i",
            "U_i_zeta",
            "Vexp_i",
            "Vexp_i_zeta",
            "Vlog_1",
            "Vlog_zeta",
        )

    q = coordinate_denominator(coordinates)
    C = c + d
    F = f + 2 * c
    safe = math.factorial(d) ** 2 * math.lcm(lcm_through(C), math.factorial(F))
    if safe % q:
        raise RuntimeError("minimal coordinate clearing did not divide safe clearing")
    return {
        "q_minimal": q,
        "safe_clearing": safe,
        "safe_over_minimal": safe // q,
        "coordinates": {
            label: f"{value.numerator}/{value.denominator}"
            for label, value in zip(coordinate_labels, coordinates)
        },
    }


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def mp_evaluate(polynomial: list[Fraction], value: mp.mpc) -> mp.mpc:
    return mp.fsum(
        mp_fraction(coefficient) * value**index
        for index, coefficient in enumerate(polynomial)
    )


def numerical_form(c: int, d: int, f: int, N: int) -> dict:
    A, B, E = rivoal_polynomials(c, d, f)
    A_one = mp_evaluate(A, 1)
    E_one = mp_evaluate(E, 1)
    R_exp = A_one * mp.e - E_one
    if N == 2:
        A_eta = mp_evaluate(A, 2)
        B_eta = mp_evaluate(B, 2)
        # Boundary value from x=2-i*0, so log(1-x)=+i*pi.
        R_log = 1j * mp.pi * A_eta - B_eta
    else:
        zeta = mp.e ** (2j * mp.pi / N)
        eta = 1 - zeta
        A_eta = mp_evaluate(A, eta)
        B_eta = mp_evaluate(B, eta)
        R_log = A_eta * (2j * mp.pi / N) - B_eta
    Lambda = 2j * A_eta * R_exp + N * A_one * R_log
    q = exact_clearing(c, d, f, N)["q_minimal"]
    return {
        "abs_R_exp": mp.nstr(abs(R_exp), 30),
        "abs_R_log": mp.nstr(abs(R_log), 30),
        "abs_Lambda": mp.nstr(abs(Lambda), 30),
        "q_minimal_times_abs_Lambda": mp.nstr(q * abs(Lambda), 30),
        "q_minimal": q,
    }


def continuation_check(c: int, d: int, f: int, N: int) -> dict:
    if N == 2:
        raise ValueError("N=2 is a boundary value, not an ordinary path integral")
    A, B, _ = rivoal_polynomials(c, d, f)
    zeta = mp.e ** (2j * mp.pi / N)
    eta = 1 - zeta
    M = 2 * c + d + 1

    def H(u: mp.mpf) -> mp.mpf:
        return mp.fsum(
            (-1) ** r
            * math.comb(f + r, f)
            * u**r
            / math.factorial(d - r)
            for r in range(d + 1)
        )

    direct = mp_evaluate(A, eta) * (2j * mp.pi / N) - mp_evaluate(B, eta)
    continued = (
        (-1) ** (c - 1)
        * eta**M
        * mp.quad(
            lambda u: (
                u**c
                * (1 - u) ** c
                * H(u)
                / (1 - eta * u) ** (c + 1)
            ),
            [0, 1],
        )
    )
    relative_error = abs(direct - continued) / max(abs(direct), mp.mpf("1e-100"))
    return {
        "parameters": [c, d, f, N],
        "direct": mp.nstr(direct, 35),
        "continued_integral": mp.nstr(continued, 35),
        "relative_error": mp.nstr(relative_error, 10),
    }


def n2_boundary_record(c: int, d: int, f: int) -> dict:
    """Archive the exact coefficients in the two N=2 boundary values."""
    A, B, E = rivoal_polynomials(c, d, f)
    A_one = sum(A, Fraction(0))
    A_two = rational_evaluate(A, 2)
    B_two = rational_evaluate(B, 2)
    E_one = sum(E, Fraction(0))
    clearing = exact_clearing(c, d, f, 2)
    M = 2 * c + d + 1

    # h(t)=t^(M-1)A(1/t).  Since PV integral 1/(1-2t) is zero,
    # subtract h(1/2) and integrate the resulting polynomial quotient.
    principal_value = Fraction(0)
    for exponent_in_A, coefficient in enumerate(A):
        exponent_in_h = M - 1 - exponent_in_A
        for j in range(exponent_in_h):
            principal_value -= (
                coefficient
                * Fraction(1, 2)
                * Fraction(1, 2**j)
                * Fraction(1, exponent_in_h - j)
            )
    expected_principal_value = B_two / 2**M
    if principal_value != expected_principal_value:
        raise RuntimeError("N=2 exact principal-value identity failed")
    return {
        "parameters": [c, d, f, 2],
        "A_1": f"{A_one.numerator}/{A_one.denominator}",
        "A_2": f"{A_two.numerator}/{A_two.denominator}",
        "B_2": f"{B_two.numerator}/{B_two.denominator}",
        "E_1": f"{E_one.numerator}/{E_one.denominator}",
        "lower_x_half_plane_boundary": "R_log=i*pi*A(2)-B(2)",
        "upper_x_half_plane_boundary": "R_log=-i*pi*A(2)-B(2)",
        "boundary_jump": "2*i*pi*A(2)",
        "principal_value_integral": (
            f"{principal_value.numerator}/{principal_value.denominator}"
        ),
        "B_2_over_2_power_M": (
            f"{expected_principal_value.numerator}/"
            f"{expected_principal_value.denominator}"
        ),
        "cleared_form": (
            "q*Lambda=-a+i*(b*s-g), with "
            "a=2*q*A(1)*B(2), b=2*q*A(1)*A(2), "
            "g=2*q*A(2)*E(1) integers"
        ),
        "exact_clearing": clearing,
    }


def lower_saddle(N: int, lam: mp.mpf) -> mp.mpc:
    zeta = mp.e ** (2j * mp.pi / N)
    eta = 1 - zeta
    L = lam + 1
    aa = L * eta
    bb = -(L * (1 + eta) + zeta)
    discriminant = bb * bb - 4 * aa * L
    roots = [
        (-bb + mp.sqrt(discriminant)) / (2 * aa),
        (-bb - mp.sqrt(discriminant)) / (2 * aa),
    ]
    candidates = [root for root in roots if mp.im(root) < 0]
    if len(candidates) != 1:
        raise RuntimeError("failed to isolate the lower saddle")
    return candidates[0]


def saddle_record(N: int, lam: int = 2, mu: int = 1) -> dict:
    lam_mp = mp.mpf(lam)
    mu_mp = mp.mpf(mu)
    zeta = mp.e ** (2j * mp.pi / N)
    eta = 1 - zeta
    saddle = lower_saddle(N, lam_mp)
    chi = (
        (lam_mp + 2) * mp.log(abs(eta))
        + (lam_mp + 1) * mp.log(abs(saddle))
        + mp.log(abs(1 - saddle))
        - mp.log(abs(1 - eta * saddle))
    )
    entropy = (
        (lam_mp + mu_mp) * mp.log(lam_mp + mu_mp)
        - lam_mp * mp.log(lam_mp)
        - mu_mp * mp.log(mu_mp)
    )
    rho = 2 * entropy + chi
    return {
        "N": N,
        "lambda": lam,
        "mu": mu,
        "lower_saddle_real": mp.nstr(mp.re(saddle), 30),
        "lower_saddle_imag": mp.nstr(mp.im(saddle), 30),
        "chi_log_remainder_rate": mp.nstr(chi, 30),
        "entropy": mp.nstr(entropy, 30),
        "rho_full_form_rate": mp.nstr(rho, 30),
    }


def fraction_interval_add(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return left[0] + right[0], left[1] + right[1]


def fraction_interval_multiply(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    products = [a * b for a in left for b in right]
    return min(products), max(products)


def fraction_interval_polynomial(
    coefficients: list[int], interval: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    answer = (Fraction(0), Fraction(0))
    for coefficient in reversed(coefficients):
        answer = fraction_interval_add(
            fraction_interval_multiply(answer, interval),
            (Fraction(coefficient), Fraction(coefficient)),
        )
    return answer


def e_interval(terms: int = 25) -> tuple[Fraction, Fraction]:
    lower = sum((Fraction(1, math.factorial(k)) for k in range(terms + 1)), Fraction(0))
    first = Fraction(1, math.factorial(terms + 1))
    upper = lower + first * Fraction(terms + 2, terms + 1)
    return lower, upper


def atan_interval(inverse: int, terms: int = 35) -> tuple[Fraction, Fraction]:
    partials = []
    running = Fraction(0)
    for k in range(terms + 2):
        running += (-1) ** k * Fraction(1, (2 * k + 1) * inverse ** (2 * k + 1))
        partials.append(running)
    return min(partials[-2], partials[-1]), max(partials[-2], partials[-1])


def s_interval() -> tuple[Fraction, Fraction]:
    e_low, e_high = e_interval()
    a5_low, a5_high = atan_interval(5)
    a239_low, a239_high = atan_interval(239)
    pi_low = 16 * a5_low - 4 * a239_high
    pi_high = 16 * a5_high - 4 * a239_low
    return e_low + pi_low, e_high + pi_high


def sqrt3_interval(digits: int = 60) -> tuple[Fraction, Fraction]:
    scale = 10**digits
    floor_value = math.isqrt(3 * scale * scale)
    return Fraction(floor_value, scale), Fraction(floor_value + 1, scale)


def decimal_interval(
    interval: tuple[Fraction, Fraction], digits: int = 25
) -> list[str]:
    getcontext().prec = digits + 10
    rendered = []
    for value in interval:
        rendered.append(
            str(Decimal(value.numerator) / Decimal(value.denominator))
        )
    return rendered


def exceptional_certificate() -> dict:
    # N=6, (c,d,f)=(0,3,0), with q_minimal=9:
    # Y=9 Lambda=i(1+3 zeta)s+12-9 zeta-3i-9i zeta.
    s_box = s_interval()
    root_box = sqrt3_interval()
    # Simultaneous-conjugate pair and off-diagonal pair, respectively.
    # D(s,r)=13s^2-(78+45r)s+234+135r.
    # O(s,r)=13s^2-(78-45r)s+234-135r.
    def b(value: int) -> tuple[Fraction, Fraction]:
        return Fraction(value), Fraction(value)

    s_squared = fraction_interval_multiply(s_box, s_box)
    forty_five_root = fraction_interval_multiply(b(45), root_box)
    coeff_diag = fraction_interval_add(b(-78), (-forty_five_root[1], -forty_five_root[0]))
    coeff_off = fraction_interval_add(b(-78), forty_five_root)
    diag = fraction_interval_add(
        fraction_interval_add(
            fraction_interval_multiply(b(13), s_squared),
            fraction_interval_multiply(coeff_diag, s_box),
        ),
        fraction_interval_add(b(234), fraction_interval_multiply(b(135), root_box)),
    )
    off = fraction_interval_add(
        fraction_interval_add(
            fraction_interval_multiply(b(13), s_squared),
            fraction_interval_multiply(coeff_off, s_box),
        ),
        fraction_interval_add(b(234), (-135 * root_box[1], -135 * root_box[0])),
    )
    norm_polynomial = [81, -54, 6093, -2028, 169]
    norm_box = fraction_interval_polynomial(norm_polynomial, s_box)
    return {
        "N": 6,
        "parameters": [0, 3, 0],
        "q_minimal": 9,
        "Y_expression": "i(1+3*zeta)*s + 12-9*zeta-3*i-9*i*zeta",
        "Y_coordinate_vector_in_basis_1_zeta_i_i_zeta": [12, -9, "s-3", "3*s-9"],
        "simultaneous_conjugate_pair_abs_squared_interval": decimal_interval(diag),
        "off_diagonal_pair_abs_squared_interval": decimal_interval(off),
        "four_embedding_relative_norm_polynomial_ascending": norm_polynomial,
        "four_embedding_relative_norm_interval": decimal_interval(norm_box),
        "scope": (
            "Intervals are rigorous rational enclosures obtained from the "
            "positive e series and alternating Machin arctangent series."
        ),
    }


def finite_scan(c_max: int, extra_d: int, extra_f: int) -> dict:
    records = {}
    for N in (2, 3, 4, 6):
        best: tuple[mp.mpf, tuple[int, int, int], int, str] | None = None
        below_one = []
        count = 0
        for c in range(c_max + 1):
            for d in range(2 * c, 2 * c + extra_d + 1):
                for f in range(c, c + extra_f + 1):
                    count += 1
                    form = numerical_form(c, d, f, N)
                    value = mp.mpf(form["q_minimal_times_abs_Lambda"])
                    item = (value, (c, d, f), form["q_minimal"], form["abs_Lambda"])
                    if best is None or item[0] < best[0]:
                        best = item
                    if value < 1:
                        below_one.append(
                            {
                                "parameters": [c, d, f],
                                "q_minimal": form["q_minimal"],
                                "abs_Lambda": form["abs_Lambda"],
                                "q_minimal_times_abs_Lambda": form[
                                    "q_minimal_times_abs_Lambda"
                                ],
                            }
                        )
        assert best is not None
        records[str(N)] = {
            "case_count": count,
            "minimum_parameters": list(best[1]),
            "minimum_q": best[2],
            "minimum_abs_Lambda": best[3],
            "minimum_q_times_abs_Lambda": mp.nstr(best[0], 30),
            "cases_below_one": below_one,
        }
    return records


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--c-max", type=int, default=6)
    parser.add_argument("--extra-d", type=int, default=6)
    parser.add_argument("--extra-f", type=int, default=8)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/small_root_rivoal_exp_log.json"),
    )
    args = parser.parse_args()
    if min(args.c_max, args.extra_d, args.extra_f) < 0:
        raise SystemExit("scan limits must be nonnegative")

    mp.mp.dps = 90
    report = {
        "description": (
            "Exact minimal coordinate clearing and numerical diagnostics "
            "for Rivoal's corrected simultaneous exp/log form at N=2,3,4,6."
        ),
        "sample_exact_clearings": {
            str(N): exact_clearing(1, 2, 1, N) for N in (2, 3, 4, 6)
        },
        "N2_boundary_records": [
            n2_boundary_record(1, 2, 1),
            n2_boundary_record(0, 1, 1),
        ],
        "continuation_checks": [
            continuation_check(1, 2, 1, N) for N in (3, 4, 6)
        ],
        "fixed_slope_rates_at_lambda_2_mu_1": [
            saddle_record(N) for N in (3, 4, 6)
        ],
        "exceptional_local_contraction": exceptional_certificate(),
        "finite_scan": finite_scan(args.c_max, args.extra_d, args.extra_f),
        "scan_scope_warning": (
            "The finite scan is diagnostic only. The source note's "
            "fixed-slope no-go theorem is analytic and all-degree."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "output_sha256": sha256_file(args.output),
                "all_checks_passed": True,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
