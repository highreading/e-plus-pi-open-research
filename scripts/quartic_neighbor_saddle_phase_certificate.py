#!/usr/bin/env python3
"""Certificate for the neighboring quartic saddle/phase analysis.

The exact identities and formal series are checked symbolically or with
integer arithmetic.  Numerical saddle and quadrature records are explicitly
labelled diagnostics.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import ceil, comb, factorial, floor, gcd, lcm, log
from pathlib import Path

import mpmath as mp
import sympy as sp


def v2(z: int) -> int:
    if z == 0:
        raise ValueError("v2(0)")
    z = abs(z)
    return (z & -z).bit_length() - 1


def popcount(z: int) -> int:
    return z.bit_count()


def raw_coordinate_numerators(n: int, k: int) -> tuple[int, int, int, int]:
    """Hermite coordinates on 4^(k-1)(k-1)!, independently reconstructed."""
    out = [0, 0, 0, 0]
    for j in range(n + 1):
        m = n + j
        p = 1
        for s in range(1, k):
            p *= 4 * s - m - 1
        residue = m % 4
        out[residue] += (
            (-1) ** (j + (m - residue) // 4) * comb(n, j) * p
        )
    return tuple(out)


def raw_coordinate_rows(n: int, k_max: int) -> list[tuple[int, int, int, int]]:
    products = [1] * (n + 1)
    signs = []
    residues = []
    for j in range(n + 1):
        m = n + j
        residue = m % 4
        residues.append(residue)
        signs.append((-1) ** (j + (m - residue) // 4) * comb(n, j))
    rows = []
    for k in range(1, k_max + 1):
        out = [0, 0, 0, 0]
        for j in range(n + 1):
            out[residues[j]] += signs[j] * products[j]
        rows.append(tuple(out))
        for j in range(n + 1):
            products[j] *= 4 * k - n - j - 1
    return rows


def coordinates(n: int, k: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    denominator = 4 ** (k - 1) * factorial(k - 1)
    return tuple(Fraction(z, denominator) for z in raw_coordinate_numerators(n, k))


def beta_coordinate_check(n_max: int, k_extra: int) -> bool:
    """Check the reflection/Beta sign reconstruction exactly.

    Equation (6) says (2 sqrt(2)/pi) times the monomial integral is
    +A_mk or -A_mk according to the displayed sine.  This routine rebuilds
    L and E from those signs, without using the residue-class signs in the
    raw-coordinate routine.
    """
    for n in range(2, n_max + 1, 2):
        for k in range(n // 2 + 1, n // 2 + k_extra + 1):
            den = 4 ** (k - 1) * factorial(k - 1)
            beta_l = Fraction(0)
            beta_e = Fraction(0)
            for j in range(0, n + 1, 2):
                m = n + j
                product = 1
                for s in range(1, k):
                    product *= 4 * s - m - 1
                a_mk = Fraction(product, den)
                # (2 sqrt(2)/pi) I_m = sign(sin) * A_mk.
                sin_sign = 1 if m % 8 in (0, 2) else -1
                scaled_integral = sin_sign * a_mk
                beta_l += (
                    (-1) ** (n // 2 + j // 2)
                    * comb(n, j)
                    * scaled_integral
                )
                # Expanding the two terms in (10) supplies a factor two,
                # so each even monomial contributes the same scaled integral.
                beta_e += comb(n, j) * scaled_integral
            a, _, c, _ = coordinates(n, k)
            if beta_l != a - c or beta_e != a + c:
                return False
    return True


def symbolic_series_checks() -> dict[str, bool]:
    r, u = sp.symbols("r u")
    ui = (
        1
        + sp.I * r / 4
        + sp.Rational(9, 32) * r**2
        - sp.I * r**3 / 4
        + sp.Rational(247, 2048) * r**4
    )
    um = (
        1
        - r / 4
        - sp.Rational(9, 32) * r**2
        - r**3 / 4
        + sp.Rational(247, 2048) * r**4
    )
    up = um.subs(r, -r)

    def psi(sigma: sp.Expr) -> sp.Expr:
        return (
            sp.log(u)
            + sp.log(1 + sigma * r * u)
            - sp.log(1 + r**4 * u**4) / (4 * r**4)
        )

    psi_i = psi(sp.I)
    psi_m = psi(sp.Integer(-1))
    psi_p = psi(sp.Integer(1))

    saddle_i = sp.series(sp.diff(psi_i, u).subs(u, ui), r, 0, 5).removeO()
    saddle_m = sp.series(sp.diff(psi_m, u).subs(u, um), r, 0, 5).removeO()

    expected_i = (
        -sp.Rational(1, 4)
        + sp.I * r
        + sp.Rational(3, 8) * r**2
        - sp.Rational(7, 96) * sp.I * r**3
        + sp.Rational(1, 4) * r**4
    )
    expected_m = (
        -sp.Rational(1, 4)
        - r
        - sp.Rational(3, 8) * r**2
        - sp.Rational(7, 96) * r**3
        + sp.Rational(1, 4) * r**4
    )
    expected_p = expected_m.subs(r, -r)

    exponent_i = sp.series(psi_i.subs(u, ui), r, 0, 5).removeO()
    exponent_m = sp.series(psi_m.subs(u, um), r, 0, 5).removeO()
    exponent_p = sp.series(psi_p.subs(u, up), r, 0, 5).removeO()

    hessian_i = sp.series(-sp.diff(psi_i, u, 2).subs(u, ui), r, 0, 4).removeO()
    hessian_m = sp.series(-sp.diff(psi_m, u, 2).subs(u, um), r, 0, 4).removeO()
    expected_hi = 4 + sp.I * r - r**2 / 4 + sp.Rational(61, 32) * sp.I * r**3
    expected_hm = 4 - r + r**2 / 4 + sp.Rational(61, 32) * r**3

    gi = sp.series(1 / (1 + (r * ui) ** 4), r, 0, 8).removeO()
    gm = sp.series(1 / (1 + (r * um) ** 4), r, 0, 8).removeO()
    gp = sp.series(1 / (1 + (r * up) ** 4), r, 0, 8).removeO()
    expected_dm = (
        -(1 + sp.I) * r**5
        - sp.Rational(3, 2) * r**6
        + sp.Rational(7, 32) * (-1 + sp.I) * r**7
    )
    expected_dp = (
        (1 - sp.I) * r**5
        - sp.Rational(3, 2) * r**6
        + sp.Rational(7, 32) * (1 + sp.I) * r**7
    )
    theta, eta, rho, magnitude = sp.symbols(
        "theta eta rho magnitude", real=True
    )
    hankel_identity = sp.trigsimp(
        (magnitude * rho * sp.cos(theta + eta)) ** 2
        - magnitude
        * sp.cos(theta)
        * magnitude
        * rho**2
        * sp.cos(theta + 2 * eta)
        - magnitude**2 * rho**2 * sp.sin(eta) ** 2
    )

    y, kappa = sp.symbols("y kappa", positive=True, real=True)
    absolute_phase = (
        sp.log(y)
        + sp.log(1 + y**2) / 2
        - kappa * sp.log(1 + y**4)
    )
    scaled_absolute_derivative = sp.factor(y * sp.diff(absolute_phase, y))
    expected_absolute_derivative = (
        1 + y**2 / (1 + y**2) - 4 * kappa * y**4 / (1 + y**4)
    )

    return {
        "complex_saddle_equation_through_r4": sp.expand(saddle_i) == 0,
        "real_saddle_equation_through_r4": sp.expand(saddle_m) == 0,
        "complex_exponent_through_r4": sp.expand(exponent_i - expected_i) == 0,
        "real_exponent_through_r4": sp.expand(exponent_m - expected_m) == 0,
        "plus_exponent_through_r4": sp.expand(exponent_p - expected_p) == 0,
        "complex_hessian_through_r3": sp.expand(hessian_i - expected_hi) == 0,
        "real_hessian_through_r3": sp.expand(hessian_m - expected_hm) == 0,
        "minus_multiplier_through_r7": sp.expand(gi - gm - expected_dm) == 0,
        "plus_multiplier_through_r7": sp.expand(gi - gp - expected_dp) == 0,
        "phase_independent_three_power_hankel_identity": hankel_identity == 0,
        "complex_tail_scaled_log_derivative_identity": sp.simplify(
            scaled_absolute_derivative - expected_absolute_derivative
        )
        == 0,
    }


def dyadic_identity_scan(n_max: int, k_max: int) -> dict[str, object]:
    failures = []
    valuation_failures = []
    zeros = []
    pairs = 0
    for n in range(2, n_max + 1, 2):
        rows = raw_coordinate_rows(n, k_max + 1)
        for k in range(n // 2 + 1, k_max + 1):
            a0, _, c0, _ = rows[k - 1]
            a1, _, c1, _ = rows[k]
            odd0 = factorial(k - 1) >> v2(factorial(k - 1))
            odd1 = factorial(k) >> v2(factorial(k))
            if any(z % odd0 for z in (a0, c0)) or any(z % odd1 for z in (a1, c1)):
                failures.append([n, k, "odd-factorial-divisibility"])
                continue
            aa0, cc0 = a0 // odd0, c0 // odd0
            aa1, cc1 = a1 // odd1, c1 // odd1
            t = 2 * (aa1 * cc0 - cc1 * aa0)
            pairs += 1
            if t == 0:
                zeros.append([n, k])
                continue
            d0 = 3 * (k - 1) - popcount(k - 1)
            d1 = 3 * k - popcount(k)
            # Direct Fraction reconstruction of B^(sqrt2).
            u0 = tuple(Fraction(z, 4 ** (k - 1) * factorial(k - 1)) for z in rows[k - 1])
            u1 = tuple(Fraction(z, 4**k * factorial(k)) for z in rows[k])
            l0, e0 = u0[0] - u0[2], u0[0] + u0[2]
            l1, e1 = u1[0] - u1[2], u1[0] + u1[2]
            b1 = (l1 * e0 - l0 * e1) / 8
            predicted = Fraction(t, 2 ** (d0 + d1 + 3))
            if b1 != predicted:
                failures.append([n, k, "equation-36"])
            expected = n // 2 + 1
            if n % 4 == 0:
                expected = n // 2 + 2 + v2(n // 4)
            if v2(t) != expected:
                valuation_failures.append([n, k, v2(t), expected])
    return {
        "pairs_checked": pairs,
        "identity_failures": failures,
        "zero_wronskians": zeros,
        "finite_conjectural_valuation_failures": valuation_failures,
    }


def primitive_integer_log_vector(
    n: int, k: int
) -> tuple[tuple[int, int, int], tuple[Fraction, Fraction, Fraction]]:
    values = []
    for s in range(3):
        a, _, c, _ = coordinates(n, k + s)
        values.append(a - c)
    common = 1
    for value in values:
        common = lcm(common, value.denominator)
    integers = [value.numerator * (common // value.denominator) for value in values]
    content = 0
    for value in integers:
        content = gcd(content, abs(value))
    integers = [value // content for value in integers]
    return tuple(integers), tuple(values)


def positive_kernel_from_log_vector(
    vector: tuple[int, int, int], eta: mp.mpf
) -> tuple[tuple[int, int, int], dict[str, str | int]]:
    """Construct equation (53), checking strict positivity exactly."""
    a, b, c = vector
    discriminant = b * b - a * c
    if discriminant <= 0:
        raise ValueError("the Hankel minor is not positive")
    if c == 0:
        return (0, 0, 1), {
            "u": 0,
            "v": 1,
            "height_ratio_over_H_eta_inverse": "0",
            "negative_quadratic_discriminant": True,
        }

    root_gap = mp.sqrt(discriminant) / abs(c)
    center = mp.mpf(b) / c
    lo, hi = center - root_gap, center + root_gap
    stable_is_lo = abs(lo - 1) <= abs(hi - 1)
    local = min((hi - lo) / 5, abs(eta) / 5)
    if stable_is_lo:
        sub_lo, sub_hi = lo + local, lo + 2 * local
    else:
        sub_lo, sub_hi = hi - 2 * local, hi - local

    chosen = None
    max_v = max(10, int(ceil(10 / local)))
    for v in range(1, max_v + 1):
        u = floor(sub_lo * v) + 1
        if mp.mpf(u) / v < sub_hi:
            g = gcd(abs(u), v)
            chosen = (u // g, v // g)
            break
    if chosen is None:
        raise AssertionError((vector, lo, hi, sub_lo, sub_hi, max_v))
    u, v = chosen
    t = Fraction(u, v)
    f_t = Fraction(a) - 2 * b * t + c * t * t
    if c * f_t >= 0:
        raise AssertionError((vector, t, f_t))

    sign = 1 if c > 0 else -1
    coeffs = [sign * c * v, -2 * sign * c * u, sign * (-a * v + 2 * b * u)]
    content = 0
    for value in coeffs:
        content = gcd(content, abs(value))
    coeffs = [value // content for value in coeffs]
    if a * coeffs[0] + b * coeffs[1] + c * coeffs[2] != 0:
        raise AssertionError("kernel identity failed")
    polynomial_discriminant = coeffs[1] ** 2 - 4 * coeffs[0] * coeffs[2]
    if coeffs[0] <= 0 or polynomial_discriminant >= 0:
        raise AssertionError((coeffs, polynomial_discriminant))

    height = max(abs(z) for z in vector)
    coefficient_height = max(abs(z) for z in coeffs)
    ratio = mp.mpf(coefficient_height) * abs(eta) / height
    return tuple(coeffs), {
        "u": u,
        "v": v,
        "stable_root_distance_from_one": mp.nstr(
            min(abs(lo - 1), abs(hi - 1)), 16
        ),
        "root_interval_width": mp.nstr(hi - lo, 16),
        "height_ratio_over_H_eta_inverse": mp.nstr(ratio, 16),
        "negative_quadratic_discriminant": polynomial_discriminant < 0,
    }


def critical_hankel_and_kernel_scan(n_max: int) -> dict[str, object]:
    mp.mp.dps = 100
    negative = []
    zero = []
    positive_count = 0
    construction_records = []
    first_persistent_positive = None
    last_nonpositive = None
    for n in range(4, n_max + 1, 2):
        k = int(mp.nint(n * mp.log(n)))
        vector, values = primitive_integer_log_vector(n, k)
        delta = values[1] * values[1] - values[0] * values[2]
        if delta < 0:
            negative.append([n, k])
            last_nonpositive = n
            continue
        if delta == 0:
            zero.append([n, k])
            last_nonpositive = n
            continue
        positive_count += 1
        kappa = mp.mpf(k) / n
        r = (4 * kappa) ** (-mp.mpf(1) / 4)
        eta = r**5
        coeffs, metadata = positive_kernel_from_log_vector(vector, eta)
        if n in (20, 40, 80, n_max):
            construction_records.append(
                {
                    "n": n,
                    "k": k,
                    "log_vector_height_digits": len(str(max(abs(z) for z in vector))),
                    "positive_kernel_coefficient_digit_counts": [
                        len(str(abs(z))) for z in coeffs
                    ],
                    "positive_kernel_coefficient_signs": [
                        1 if z > 0 else (-1 if z < 0 else 0) for z in coeffs
                    ],
                    **metadata,
                    "log_tail_ratio_upper_exponent": str(
                        -(k - n) * log(2)
                        + n * log(4 * kappa) / 4
                        + 2 * log(1 / eta)
                    ),
                }
            )
    if last_nonpositive is not None and last_nonpositive + 2 <= n_max:
        first_persistent_positive = last_nonpositive + 2
    return {
        "n_max": n_max,
        "positive_count": positive_count,
        "negative_pairs": negative,
        "zero_pairs": zero,
        "first_positive_after_last_nonpositive_in_scan": first_persistent_positive,
        "positive_integer_kernel_records": construction_records,
    }


def exact_double_integral_diagnostic() -> list[dict[str, str | int]]:
    mp.mp.dps = 70
    records = []
    for n, k in [(4, 4), (8, 7), (12, 11)]:
        u0 = coordinates(n, k)
        u1 = coordinates(n, k + 1)
        l0 = mp.mpf((u0[0] - u0[2]).numerator) / (u0[0] - u0[2]).denominator
        l1 = mp.mpf((u1[0] - u1[2]).numerator) / (u1[0] - u1[2]).denominator
        f0 = lambda x: (x * (1 - x)) ** n / (1 + x**4) ** k
        j0 = mp.quad(f0, [0, 1])
        j1 = mp.quad(lambda x: f0(x) / (1 + x**4), [0, 1])
        direct = l1 * j0 - l0 * j1

        i0 = complex_beta_integral(n, k)
        i1 = complex_beta_integral(n, k + 1)
        double = (
            (-1) ** (n // 2)
            * 2
            * mp.sqrt(2)
            / mp.pi
            * mp.re(i1 * j0 - i0 * j1)
        )
        relative = abs(direct - double) / max(abs(direct), mp.mpf("1e-100"))
        records.append(
            {
                "n": n,
                "k": k,
                "direct": mp.nstr(direct, 35),
                "double_integral": mp.nstr(double, 35),
                "relative_error": mp.nstr(relative, 8),
            }
        )
    return records


def complex_beta_integral(n: int, k: int) -> mp.mpc:
    """Exact finite beta expansion of I_nk, evaluated at current precision."""
    return sum(
        (
            mp.mpc(0),
            *(
                mp.mpf(comb(n, j))
                * mp.j**j
                * mp.beta(mp.mpf(n + j + 1) / 4, k - mp.mpf(n + j + 1) / 4)
                / 4
                for j in range(n + 1)
            ),
        )
    )


def saddle_diagnostics() -> list[dict[str, str | int]]:
    mp.mp.dps = 70
    records = []
    for n in (40, 80, 160):
        mp.mp.dps = max(100, n)
        k = int(mp.nint(n * mp.log(n)))
        kappa = mp.mpf(k) / n
        r = (4 * kappa) ** (-mp.mpf(1) / 4)

        def saddle(sigma: mp.mpc) -> mp.mpc:
            return mp.findroot(
                lambda u: 1 / u
                + sigma * r / (1 + sigma * r * u)
                - u**3 / (1 + r**4 * u**4),
                1 + sigma * r / 4,
            )

        ui = saddle(1j)
        um = saddle(-1)
        psi = lambda u, sigma: (
            mp.log(u)
            + mp.log(1 + sigma * r * u)
            - mp.log(1 + r**4 * u**4) / (4 * r**4)
        )
        d2 = lambda u, sigma: (
            -1 / u**2
            - (sigma * r) ** 2 / (1 + sigma * r * u) ** 2
            - 3 * u**2 / (1 + r**4 * u**4)
            + 4 * r**4 * u**6 / (1 + r**4 * u**4) ** 2
        )
        i_saddle = (
            r ** (n + 1)
            * mp.e ** (n * psi(ui, 1j))
            * mp.sqrt(2 * mp.pi / (-n * d2(ui, 1j)))
        )
        j_saddle = (
            r ** (n + 1)
            * mp.e ** (n * psi(um, -1))
            * mp.sqrt(2 * mp.pi / (-n * d2(um, -1)))
        )
        i_exact = complex_beta_integral(n, k)
        x_minus = r * um
        j_exact = mp.quad(
            lambda x: (x * (1 - x)) ** n / (1 + x**4) ** k,
            [0, x_minus / 2, x_minus, 2 * x_minus, 1],
        )
        dm = 1 / (1 + (r * ui) ** 4) - 1 / (1 + (r * um) ** 4)
        records.append(
            {
                "n": n,
                "k": k,
                "r": mp.nstr(r, 20),
                "I_relative_error": mp.nstr(abs(i_exact / i_saddle - 1), 10),
                "J_relative_error": mp.nstr(abs(j_exact / j_saddle - 1), 10),
                "D_over_r5": mp.nstr(dm / r**5, 20),
                "phase_mesh_over_r5": mp.nstr(
                    mp.arg(complex_beta_integral(n, k + 1) / i_exact)
                    / r**5,
                    15,
                ),
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "results"
        / "quartic_neighbor_saddle_phase_certificate.json",
    )
    parser.add_argument("--n-max", type=int, default=80)
    parser.add_argument("--k-max", type=int, default=120)
    args = parser.parse_args()

    beta_ok = beta_coordinate_check(20, 8)
    series = symbolic_series_checks()
    dyadic = dyadic_identity_scan(args.n_max, args.k_max)
    hankel = critical_hankel_and_kernel_scan(160)
    if not beta_ok or not all(series.values()):
        raise AssertionError((beta_ok, series))
    if dyadic["identity_failures"]:
        raise AssertionError(dyadic)

    result = {
        "schema": "quartic-neighbor-saddle-phase-certificate-v1",
        "parameters": {"n_max": args.n_max, "k_max": args.k_max},
        "exact_beta_coordinate_reconstruction": beta_ok,
        "symbolic_series_checks": series,
        "dyadic_wronskian": dyadic,
        "critical_three_power_hankel_and_positive_kernel": hankel,
        "double_integral_diagnostics": exact_double_integral_diagnostic(),
        "saddle_diagnostics": saddle_diagnostics(),
        "warnings": [
            "Numerical quadratures and bounded scans are diagnostics, not proofs.",
            "The all-parameter dyadic valuation pattern remains conjectural.",
            "The bounded Hankel sign scan is diagnostic; eventual positivity is proved by the saddle theorem.",
            "The symmetric positive-form ratio is an analytic obstruction, not a quadratic-field primitive-content theorem.",
            "The saddle theorem does not give uniform arithmetic separation from every integer-power phase zero.",
            "Nothing in this certificate classifies e+pi.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
