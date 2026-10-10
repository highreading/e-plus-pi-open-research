#!/usr/bin/env python3
"""Independent exact audit of the small-root Rivoal continuation note.

This script deliberately reconstructs the polynomials from the Rodrigues
formula, rather than importing the implementation used by the source note.
It checks exact coefficientwise clearings, the N=2 principal-value identity,
the complete stated finite scan, the exceptional N=6 norm calculation, and
the symbolic inequalities used to minimize the proportional-ray rate.

All decisions involving e, pi, or sqrt(3) use rational intervals.  Decimal
values in the JSON output are only renderings of those exact intervals.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


Interval = tuple[Fraction, Fraction]
Pair = tuple[Fraction, Fraction]
IPair = tuple[Interval, Interval]


def i_const(value: int | Fraction) -> Interval:
    x = Fraction(value)
    return x, x


def i_add(x: Interval, y: Interval) -> Interval:
    return x[0] + y[0], x[1] + y[1]


def i_neg(x: Interval) -> Interval:
    return -x[1], -x[0]


def i_sub(x: Interval, y: Interval) -> Interval:
    return i_add(x, i_neg(y))


def i_mul(x: Interval, y: Interval) -> Interval:
    values = [a * b for a in x for b in y]
    return min(values), max(values)


def i_scale(q: int | Fraction, x: Interval) -> Interval:
    return i_mul(i_const(Fraction(q)), x)


def i_square(x: Interval) -> Interval:
    if x[0] <= 0 <= x[1]:
        return Fraction(0), max(x[0] * x[0], x[1] * x[1])
    values = x[0] * x[0], x[1] * x[1]
    return min(values), max(values)


def i_div(x: Interval, y: Interval) -> Interval:
    if y[0] <= 0 <= y[1]:
        raise ZeroDivisionError("interval denominator contains zero")
    reciprocal = Fraction(1, 1) / y[1], Fraction(1, 1) / y[0]
    return i_mul(x, reciprocal)


def sqrt_fraction_floor(value: Fraction, scale: int) -> int:
    if value < 0:
        raise ValueError("square root of negative rational")
    return math.isqrt((value.numerator * scale * scale) // value.denominator)


def i_sqrt(x: Interval, digits: int = 80) -> Interval:
    if x[0] < 0:
        raise ValueError("square-root interval is not nonnegative")
    scale = 10**digits
    lo_int = sqrt_fraction_floor(x[0], scale)
    hi_int = sqrt_fraction_floor(x[1], scale)
    lo = Fraction(lo_int, scale)
    hi_candidate = Fraction(hi_int, scale)
    if hi_candidate * hi_candidate < x[1]:
        hi_int += 1
    return lo, Fraction(hi_int, scale)


def i_abs(z: IPair) -> Interval:
    return i_sqrt(i_add(i_square(z[0]), i_square(z[1])))


def iz_add(z: IPair, w: IPair) -> IPair:
    return i_add(z[0], w[0]), i_add(z[1], w[1])


def iz_sub(z: IPair, w: IPair) -> IPair:
    return i_sub(z[0], w[0]), i_sub(z[1], w[1])


def iz_mul(z: IPair, w: IPair) -> IPair:
    return (
        i_sub(i_mul(z[0], w[0]), i_mul(z[1], w[1])),
        i_add(i_mul(z[0], w[1]), i_mul(z[1], w[0])),
    )


def iz_scale(q: int | Fraction, z: IPair) -> IPair:
    return i_scale(q, z[0]), i_scale(q, z[1])


def iz_div(z: IPair, w: IPair) -> IPair:
    denominator = i_add(i_square(w[0]), i_square(w[1]))
    return (
        i_div(i_add(i_mul(z[0], w[0]), i_mul(z[1], w[1])), denominator),
        i_div(i_sub(i_mul(z[1], w[0]), i_mul(z[0], w[1])), denominator),
    )


def factorial_ratio(top: int, bottom: int) -> int:
    if top < bottom:
        raise ValueError("factorial ratio requires top >= bottom")
    answer = 1
    for value in range(bottom + 1, top + 1):
        answer *= value
    return answer


def polynomial_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def polynomial_multiply(
    left: list[Fraction], right: list[Fraction]
) -> list[Fraction]:
    answer = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def reconstruct_polynomials(
    c: int, d: int, f: int
) -> tuple[list[Fraction], list[Fraction], list[Fraction]]:
    """Build A,B,E independently from H and the Rodrigues identity."""
    if c < 0 or d < 2 * c or f < c:
        raise ValueError("inadmissible parameters")

    H = [
        Fraction((-1) ** r * math.comb(f + r, f), math.factorial(d - r))
        for r in range(d + 1)
    ]
    u_c = [Fraction(0)] * c + [Fraction(1)]
    one_minus_u_c = [Fraction((-1) ** j * math.comb(c, j)) for j in range(c + 1)]
    rodrigues_input = polynomial_multiply(polynomial_multiply(u_c, one_minus_u_c), H)
    P = []
    for degree in range(c, len(rodrigues_input)):
        coefficient = rodrigues_input[degree]
        coefficient *= Fraction(factorial_ratio(degree, degree - c), math.factorial(c))
        P.append(coefficient)

    C = c + d
    if len(P) < C + 1:
        P += [Fraction(0)] * (C + 1 - len(P))
    if len(P) != C + 1:
        raise AssertionError("Rodrigues polynomial has the wrong degree")
    A = list(reversed(P))

    B = [Fraction(0) for _ in range(C + 1)]
    for n in range(C + 1):
        B[n] = -sum((A[m] / (n - m) for m in range(n)), Fraction(0))

    F = f + 2 * c
    E = [Fraction(0) for _ in range(F + 1)]
    for n in range(F + 1):
        E[n] = sum(
            (
                A[m] / math.factorial(n - m)
                for m in range(min(n, C) + 1)
            ),
            Fraction(0),
        )
    return A, B, E


def rational_evaluate(polynomial: list[Fraction], value: int) -> Fraction:
    answer = Fraction(0)
    for coefficient in reversed(polynomial):
        answer = answer * value + coefficient
    return answer


def pair_add(left: Pair, right: Pair) -> Pair:
    return left[0] + right[0], left[1] + right[1]


def pair_scale(scale: Fraction, value: Pair) -> Pair:
    return scale * value[0], scale * value[1]


def pair_multiply(left: Pair, right: Pair, relation: Pair) -> Pair:
    a, b = left
    c, d = right
    return a * c + b * d * relation[0], a * d + b * c + b * d * relation[1]


def pair_evaluate(polynomial: list[Fraction], value: Pair, relation: Pair) -> Pair:
    answer = Fraction(0), Fraction(0)
    for coefficient in reversed(polynomial):
        answer = pair_add(pair_multiply(answer, value, relation), (coefficient, Fraction(0)))
    return answer


def field_data(N: int) -> tuple[Pair, Pair]:
    if N == 3:
        return (Fraction(1), Fraction(-1)), (Fraction(-1), Fraction(-1))
    if N == 4:
        return (Fraction(1), Fraction(-1)), (Fraction(-1), Fraction(0))
    if N == 6:
        return (Fraction(1), Fraction(-1)), (Fraction(-1), Fraction(1))
    raise ValueError("unsupported N")


def lcm_through(n: int) -> int:
    answer = 1
    for value in range(1, n + 1):
        answer = math.lcm(answer, value)
    return answer


def denominator_lcm(values: list[Fraction]) -> int:
    answer = 1
    for value in values:
        answer = math.lcm(answer, value.denominator)
    return answer


def exact_data(c: int, d: int, f: int, N: int) -> dict:
    A, B, E = reconstruct_polynomials(c, d, f)
    A1 = sum(A, Fraction(0))
    E1 = sum(E, Fraction(0))

    if N == 2:
        A2 = rational_evaluate(A, 2)
        B2 = rational_evaluate(B, 2)
        coordinates = [2 * A1 * B2, 2 * A1 * A2, 2 * A2 * E1]
        payload = {"A2": A2, "B2": B2}
    else:
        eta, relation = field_data(N)
        Aeta = pair_evaluate(A, eta, relation)
        Beta = pair_evaluate(B, eta, relation)
        if N == 4:
            # Here the pair generator is i itself.
            iA = -Aeta[1], Aeta[0]
            i_part = pair_scale(-2 * E1, iA)
            log_part = pair_scale(-4 * A1, Beta)
            U = pair_scale(2 * A1, iA)
            V = pair_add(i_part, log_part)
            coordinates = [*U, *V]
        else:
            U_i = pair_scale(2 * A1, Aeta)
            V_i = pair_scale(-2 * E1, Aeta)
            V_plain = pair_scale(-N * A1, Beta)
            coordinates = [*U_i, *V_i, *V_plain]
        payload = {"Aeta": Aeta, "Beta": Beta}

    q = denominator_lcm(coordinates)
    safe = math.factorial(d) ** 2 * math.lcm(
        lcm_through(c + d), math.factorial(f + 2 * c)
    )
    if safe % q:
        raise AssertionError("exact clearing does not divide the safe clearing")
    return {
        "A": A,
        "B": B,
        "E": E,
        "A1": A1,
        "E1": E1,
        "q": q,
        "safe": safe,
        **payload,
    }


def e_interval(terms: int = 36) -> Interval:
    partial = sum((Fraction(1, math.factorial(k)) for k in range(terms + 1)), Fraction(0))
    first_omitted = Fraction(1, math.factorial(terms + 1))
    return partial, partial + first_omitted * Fraction(terms + 2, terms + 1)


def atan_inverse_interval(inverse: int, terms: int = 42) -> Interval:
    total = Fraction(0)
    last_two = []
    for k in range(terms + 2):
        total += Fraction((-1) ** k, (2 * k + 1) * inverse ** (2 * k + 1))
        if k >= terms:
            last_two.append(total)
    return min(last_two[-2:]), max(last_two[-2:])


def s_interval() -> Interval:
    e_box = e_interval()
    a5 = atan_inverse_interval(5)
    a239 = atan_inverse_interval(239)
    pi_box = i_sub(i_scale(16, a5), i_scale(4, a239))
    return i_add(e_box, pi_box)


def sqrt3_interval(digits: int = 90) -> Interval:
    scale = 10**digits
    root_floor = math.isqrt(3 * scale * scale)
    return Fraction(root_floor, scale), Fraction(root_floor + 1, scale)


def affine(coefficient: Fraction, variable: Interval, constant: Fraction = Fraction(0)) -> Interval:
    return i_add(i_scale(coefficient, variable), i_const(constant))


def lambda_squared_interval(data: dict, N: int, s_box: Interval, root3: Interval) -> Interval:
    q = data["q"]
    A1 = data["A1"]
    E1 = data["E1"]

    if N == 2:
        A2 = data["A2"]
        B2 = data["B2"]
        a = 2 * q * A1 * B2
        b = 2 * q * A1 * A2
        g = 2 * q * A2 * E1
        imaginary = affine(b, s_box, -g)
        return i_add(i_const(a * a), i_square(imaginary))

    Aeta: Pair = data["Aeta"]
    Beta: Pair = data["Beta"]
    if N == 4:
        iA = -Aeta[1], Aeta[0]
        U = pair_scale(2 * A1, iA)
        V = pair_add(pair_scale(-2 * E1, iA), pair_scale(-4 * A1, Beta))
        real = affine(q * U[0], s_box, q * V[0])
        imaginary = affine(q * U[1], s_box, q * V[1])
        return i_add(i_square(real), i_square(imaginary))

    zeta_real = Fraction(-1, 2) if N == 3 else Fraction(1, 2)
    zeta_imag = i_scale(Fraction(1, 2), root3)
    multiplier = affine(2 * A1, s_box, -2 * E1)
    q0 = i_scale(Aeta[0], multiplier)
    q1 = i_scale(Aeta[1], multiplier)
    plain0 = -N * A1 * Beta[0]
    plain1 = -N * A1 * Beta[1]
    plain_real = i_const(plain0 + plain1 * zeta_real)
    plain_imag = i_scale(plain1, zeta_imag)
    sector_real = i_add(q0, i_scale(zeta_real, q1))
    sector_imag = i_mul(q1, zeta_imag)
    real = i_scale(q, i_sub(plain_real, sector_imag))
    imaginary = i_scale(q, i_add(plain_imag, sector_real))
    return i_add(i_square(real), i_square(imaginary))


def principal_value_from_A(A: list[Fraction], c: int, d: int) -> Fraction:
    M = 2 * c + d + 1
    answer = Fraction(0)
    for degree, coefficient in enumerate(A):
        exponent = M - 1 - degree
        # PV integral of t^exponent/(1-2t); the constant singular part
        # integrates to zero on [0,1].
        for j in range(exponent):
            answer -= coefficient * Fraction(1, 2) * Fraction(1, 2**j) * Fraction(1, exponent - j)
    return answer


def finite_scan(c_max: int, extra_d: int, extra_f: int) -> dict:
    s_box = s_interval()
    root3 = sqrt3_interval()
    result: dict[str, dict] = {}
    for N in (2, 3, 4, 6):
        below = []
        above = 0
        undecided = []
        minimum = None
        count = 0
        for c in range(c_max + 1):
            for d in range(2 * c, 2 * c + extra_d + 1):
                for f in range(c, c + extra_f + 1):
                    count += 1
                    data = exact_data(c, d, f, N)
                    if N == 2:
                        pv = principal_value_from_A(data["A"], c, d)
                        if pv != data["B2"] / 2 ** (2 * c + d + 1):
                            raise AssertionError("N=2 principal-value identity failed")
                    square_box = lambda_squared_interval(data, N, s_box, root3)
                    if square_box[1] < 1:
                        below.append((c, d, f, data["q"], square_box))
                    elif square_box[0] >= 1:
                        above += 1
                    else:
                        undecided.append((c, d, f, data["q"], square_box))
                    midpoint = float((square_box[0] + square_box[1]) / 2)
                    if minimum is None or midpoint < minimum[0]:
                        minimum = (midpoint, c, d, f, data["q"], square_box)
        if undecided:
            raise AssertionError(f"interval scan left undecided cases for N={N}")
        assert minimum is not None
        result[str(N)] = {
            "case_count": count,
            "certified_at_least_one_count": above,
            "certified_below_one": [
                {
                    "parameters": [c, d, f],
                    "q": q,
                    "q_squared_abs_lambda_squared_interval": interval_strings(box),
                }
                for c, d, f, q, box in below
            ],
            "minimum_parameters": [minimum[1], minimum[2], minimum[3]],
            "minimum_q": minimum[4],
            "minimum_squared_interval": interval_strings(minimum[5]),
        }
    return result


def cyclotomic_zeta_box(N: int, root3: Interval) -> IPair:
    if N == 3:
        return i_const(Fraction(-1, 2)), i_scale(Fraction(1, 2), root3)
    if N == 4:
        return i_const(0), i_const(1)
    if N == 6:
        return i_const(Fraction(1, 2)), i_scale(Fraction(1, 2), root3)
    raise ValueError("unsupported N")


def lower_saddle_box(N: int, root3: Interval) -> IPair:
    """Rigorous rational box from the quadratic formula at lambda=2."""
    zeta = cyclotomic_zeta_box(N, root3)
    eta = iz_sub((i_const(1), i_const(0)), zeta)
    aa = iz_scale(3, eta)
    bb = iz_scale(-1, iz_add(iz_scale(3, iz_add((i_const(1), i_const(0)), eta)), zeta))
    discriminant = iz_sub(iz_mul(bb, bb), iz_scale(12, aa))
    if discriminant[1][0] <= 0:
        raise AssertionError("expected positive imaginary part of discriminant")
    radius = i_sqrt(i_add(i_square(discriminant[0]), i_square(discriminant[1])))
    sqrt_real = i_sqrt(i_scale(Fraction(1, 2), i_add(radius, discriminant[0])))
    sqrt_imag = i_sqrt(i_scale(Fraction(1, 2), i_sub(radius, discriminant[0])))
    square_root = sqrt_real, sqrt_imag
    lower = iz_div(iz_sub(iz_scale(-1, bb), square_root), iz_scale(2, aa))
    if not lower[1][1] < 0:
        raise AssertionError("quadratic branch did not isolate the lower saddle")
    return lower


def fixed_slope_certificates() -> dict:
    root3 = sqrt3_interval()
    certificates = {}
    eta_fourth_power = {3: Fraction(9), 4: Fraction(4), 6: Fraction(1)}
    entropy_exponential = Fraction(729, 16)
    mp.mp.dps = 70
    for N in (3, 4, 6):
        u = lower_saddle_box(N, root3)
        zeta = cyclotomic_zeta_box(N, root3)
        eta = iz_sub((i_const(1), i_const(0)), zeta)
        one_minus_u = iz_sub((i_const(1), i_const(0)), u)
        one_minus_eta_u = iz_sub((i_const(1), i_const(0)), iz_mul(eta, u))
        exp_chi = i_div(
            i_scale(
                eta_fourth_power[N],
                i_mul(i_mul(i_abs(u), i_abs(u)), i_mul(i_abs(u), i_abs(one_minus_u))),
            ),
            i_abs(one_minus_eta_u),
        )
        exp_rho = i_scale(entropy_exponential, exp_chi)
        if exp_rho[0] <= 1:
            raise AssertionError("failed to certify positive minimum rate")

        # Decimal display is independently recomputed, but positivity above
        # was decided solely with exact rational intervals.
        z = mp.e ** (2j * mp.pi / N)
        et = 1 - z
        L = mp.mpf(3)
        aa = L * et
        bb = -(L * (1 + et) + z)
        disc = bb * bb - 4 * aa * L
        roots = [(-bb + mp.sqrt(disc)) / (2 * aa), (-bb - mp.sqrt(disc)) / (2 * aa)]
        saddle = min(roots, key=lambda value: mp.im(value))
        chi = 4 * mp.log(abs(et)) + 3 * mp.log(abs(saddle)) + mp.log(abs(1 - saddle)) - mp.log(abs(1 - et * saddle))
        entropy = 3 * mp.log(3) - 2 * mp.log(2)
        rho = 2 * entropy + chi
        certificates[str(N)] = {
            "lower_saddle_real_interval": interval_strings(u[0]),
            "lower_saddle_imag_interval": interval_strings(u[1]),
            "exp_rho_interval": interval_strings(exp_rho),
            "display_chi": mp.nstr(chi, 40),
            "display_rho": mp.nstr(rho, 40),
        }
    return certificates


def symbolic_monotonicity_checks() -> dict:
    L, t = sp.symbols("L t", positive=True, real=True)
    checks = {}
    for N in (3, 4):
        if N == 3:
            zeta = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
            eta = 1 - zeta
            y0 = 1 / sp.sqrt(3)
            expected = (L - 1) / L**2
        else:
            zeta = sp.I
            eta = 1 - zeta
            y0 = 1 / sp.sqrt(2)
            expected = (2 * L - 5) / L**2
        trace = sp.simplify((eta + 1 + zeta / L) / sp.sqrt(eta))
        a = sp.simplify(sp.re(sp.expand_complex(trace)))
        b = sp.simplify(sp.im(sp.expand_complex(trace)))
        modulus_equation_left = a**2 * y0 / (1 + y0) ** 2 + b**2 * y0 / (1 - y0) ** 2
        difference = sp.simplify(sp.radsimp(1 - modulus_equation_left - expected))
        if difference != 0:
            raise AssertionError(f"N={N} modulus substitution failed")
        checks[str(N)] = str(expected)

    y = (L - 1) ** 4 / L**4
    n6_left = 3 * y / (1 + y) ** 2 + y / (L**2 * (1 - y) ** 2)
    numerator = sp.Poly(sp.expand(sp.together(1 - n6_left).as_numer_denom()[0].subs(L, t + 3)), t)
    expected_coefficients = [
        12,
        424,
        7192,
        77320,
        585380,
        3282160,
        13979129,
        45741108,
        115153853,
        221419630,
        319558808,
        335307040,
        241643432,
        107018384,
        21971329,
    ]
    if numerator.all_coeffs() != expected_coefficients:
        raise AssertionError("N=6 positivity polynomial mismatch")
    checks["6_polynomial_coefficients_descending"] = expected_coefficients
    return checks


def exceptional_certificate() -> dict:
    s_box = s_interval()
    root3 = sqrt3_interval()
    data = exact_data(0, 3, 0, 6)
    if data["q"] != 9:
        raise AssertionError("exceptional exact clearing is not 9")
    diag = lambda_squared_interval(data, 6, s_box, root3)

    # Evaluate Y=12-9*zeta+i*((s-3)+(3s-9)*zeta) with the off-diagonal
    # embedding i fixed and zeta conjugated.
    zeta_real = Fraction(1, 2)
    zeta_imag = i_scale(Fraction(-1, 2), root3)
    plain_real = i_const(Fraction(12) - 9 * zeta_real)
    plain_imag = i_scale(-9, zeta_imag)
    q0 = affine(1, s_box, -3)
    q1 = affine(3, s_box, -9)
    sector_real = i_add(q0, i_scale(zeta_real, q1))
    sector_imag = i_mul(q1, zeta_imag)
    off_real = i_sub(plain_real, sector_imag)
    off_imag = i_add(plain_imag, sector_real)
    off = i_add(i_square(off_real), i_square(off_imag))
    product = i_mul(diag, off)
    if not (diag[1] < 1 and off[0] > 400 and product[0] > 180):
        raise AssertionError("exceptional embedding inequalities failed")

    s_symbol, root_symbol = sp.symbols("s root")
    diagonal_exact = (
        13 * s_symbol**2
        - (78 + 45 * root_symbol) * s_symbol
        + 234
        + 135 * root_symbol
    )
    off_diagonal_exact = (
        13 * s_symbol**2
        - (78 - 45 * root_symbol) * s_symbol
        + 234
        - 135 * root_symbol
    )
    reduced_product = sp.rem(
        sp.Poly(sp.expand(diagonal_exact * off_diagonal_exact), root_symbol),
        sp.Poly(root_symbol**2 - 3, root_symbol),
    ).as_expr()
    expected_product = (
        169 * s_symbol**4
        - 2028 * s_symbol**3
        + 6093 * s_symbol**2
        - 54 * s_symbol
        + 81
    )
    if sp.expand(reduced_product - expected_product) != 0:
        raise AssertionError("exceptional exact norm polynomial mismatch")
    return {
        "q": data["q"],
        "diagonal_pair_interval": interval_strings(diag),
        "off_diagonal_pair_interval": interval_strings(off),
        "four_evaluation_product_interval": interval_strings(product),
        "four_evaluation_polynomial_descending": [169, -2028, 6093, -54, 81],
    }


def interval_strings(box: Interval, digits: int = 45) -> list[str]:
    def render(value: Fraction) -> str:
        mp.mp.dps = digits + 10
        return mp.nstr(mp.mpf(value.numerator) / value.denominator, digits)

    return [render(box[0]), render(box[1])]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/independent_small_root_continuation_audit.json"),
    )
    args = parser.parse_args()

    report = {
        "description": "Independent exact audit of the N=2,3,4,6 continuation note",
        "finite_scan": finite_scan(6, 6, 8),
        "fixed_slope_minimum_certificates": fixed_slope_certificates(),
        "symbolic_monotonicity_checks": symbolic_monotonicity_checks(),
        "exceptional_N6": exceptional_certificate(),
        "sample_clearings_c1_d2_f1": {
            str(N): exact_data(1, 2, 1, N)["q"] for N in (2, 3, 4, 6)
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "all_checks_passed": True,
                "output": str(args.output),
                "output_sha256": sha256_file(args.output),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
