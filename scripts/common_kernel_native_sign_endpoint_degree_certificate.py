#!/usr/bin/env python3
"""Exact replay for the native sign/endpoint-layer degree barrier.

Finite examples verify identities and normalization only.  The uniform
Markov and integrating-factor inequalities are proved in the companion
source.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_native_sign_endpoint_degree_barrier.md"
OUTPUT = ROOT / "results/common_kernel_native_sign_endpoint_degree_certificate.json"
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_growing_correction_full_window_hashes.sha256":
        "ef4c51baa0a9a2660be5e1360682f4bcb522354e1af8a6c87c6d3b9bfa057fc6",
    "results/common_kernel_stein_robin_quadratic_correction_hashes.sha256":
        "208982ad388c02ba42c79726b6eaefa8acd1ed7d5a2fad6de5c138a44483038a",
}

x, t = sp.symbols("x t")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte != 10
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def gaussian_power_one_minus_i(exponent: int) -> tuple[int, int]:
    real, imaginary = 1, 0
    for _ in range(exponent):
        real, imaginary = real + imaginary, imaginary - real
    return real, imaginary


def stein_x(polynomial: sp.Expr) -> sp.Expr:
    return sp.expand((1 - x) * sp.diff(polynomial, x) - x * polynomial)


def h_sparse(m_value: int) -> sp.Expr:
    return sp.expand(x ** (4 * m_value) * (m_value + 1 - m_value * x**4))


def exact_divide(numerator: sp.Expr, denominator: sp.Expr) -> sp.Expr:
    quotient, remainder = sp.div(
        sp.Poly(sp.expand(numerator), x, domain=sp.ZZ),
        sp.Poly(sp.expand(denominator), x, domain=sp.ZZ),
    )
    assert remainder.is_zero
    return quotient.as_expr()


def rational_integral(polynomial: sp.Expr) -> Fraction:
    poly = sp.Poly(sp.expand(polynomial), x, domain=sp.ZZ)
    value = Fraction(0)
    for (degree,), coefficient in poly.terms():
        value += Fraction(int(coefficient), degree + 1)
    return value


def exponential_integral_pair(polynomial_t: sp.Expr) -> tuple[Fraction, Fraction]:
    """Return A,B with integral_0^1 exp(-t)p(t)dt = A+B/e."""
    poly = sp.Poly(sp.expand(polynomial_t), t, domain=sp.ZZ)
    constant = Fraction(0)
    inverse_e = Fraction(0)
    for (degree,), coefficient in poly.terms():
        factorial = math.factorial(degree)
        partial = sum(Fraction(1, math.factorial(j)) for j in range(degree + 1))
        constant += int(coefficient) * factorial
        inverse_e -= int(coefficient) * factorial * partial
    return constant, inverse_e


def strict_power_threshold(numerator: int, denominator: int, power: int) -> int:
    """Least nonnegative d for which denominator*d**power > numerator."""
    if numerator <= 0:
        return 0
    high = 1
    while denominator * high**power <= numerator:
        high *= 2
    low = high // 2
    while low + 1 < high:
        middle = (low + high) // 2
        if denominator * middle**power > numerator:
            high = middle
        else:
            low = middle
    assert denominator * high**power > numerator
    assert high == 0 or denominator * (high - 1) ** power <= numerator
    return high


def symbolic_integrating_factor_check() -> dict[str, str]:
    a, b = sp.symbols("a b")
    h_symbol, hp_symbol = sp.symbols("H Hp")
    mu = t * (a + b * t) * sp.exp(-t)
    coefficient = a * (1 - t) + b * t * (2 - t)
    left = sp.diff(mu, t) * h_symbol + mu * hp_symbol
    right = sp.exp(-t) * (
        t * (a + b * t) * hp_symbol + coefficient * h_symbol
    )
    assert sp.simplify(left - right) == 0
    logarithmic = sp.simplify(
        sp.diff(mu, t) / mu - coefficient / (t * (a + b * t))
    )
    assert logarithmic == 0
    return {
        "mu": "t*(a+b*t)*exp(-t)",
        "coefficient": "a*(1-t)+b*t*(2-t)",
        "derivative_identity_difference": "0",
        "logarithmic_derivative_difference": "0",
    }


def exact_case(exponent: int, m_value: int) -> dict[str, object]:
    real, imaginary = gaussian_power_one_minus_i(exponent)
    factorial = math.factorial(exponent)
    m_native = factorial - real
    assert m_native > 0 and m_native % 2 == 0
    b_native = m_native // 2

    h_poly = h_sparse(m_value)
    u_poly = 1 + x**2
    q_h = exact_divide(h_poly - 1, u_poly**2)
    derivative_target = sp.expand(
        sp.diff(h_poly, x)
        - 4 * m_value * (m_value + 1)
        * x ** (4 * m_value - 1) * (1 - x**4)
    )
    assert derivative_target == 0
    assert h_poly.subs(x, 0) == 0 and h_poly.subs(x, 1) == 1

    k_poly = imaginary - b_native * (1 - x)
    residual = sp.expand((1 - x) ** exponent + stein_x(h_poly * k_poly))
    assert residual.subs(x, 1) == -imaginary
    endpoint_zero = sp.expand(
        residual.subs(x, 0)
        - (1 - (b_native - imaginary) * sp.diff(h_poly, x).subs(x, 0))
    )
    assert endpoint_zero == 0

    residual_t = sp.expand(residual.subs(x, 1 - t))
    moment_pair = exponential_integral_pair(residual_t)
    baseline_pair = exponential_integral_pair(t**exponent)
    assert moment_pair == baseline_pair

    p_zero = sp.expand(
        factorial
        * sum((1 - x) ** j / math.factorial(j + 1)
              for j in range(exponent))
    )
    assert sp.Poly(p_zero, x).get_domain() == sp.ZZ
    p_full = sp.expand(p_zero + h_poly * k_poly)
    q_output = exact_divide(residual - factorial, u_poly)
    rho = (
        Fraction(-factorial - int(p_full.subs(x, 0)), 1)
        + 4 * rational_integral(q_output)
    )
    denominator = rho.denominator
    numerator = rho.numerator
    content = math.gcd(factorial, numerator)
    primitive_e_pi = factorial * denominator // content
    primitive_rational = numerator // content
    assert math.gcd(abs(primitive_e_pi), abs(primitive_rational)) == 1
    approximation_denominator = primitive_e_pi
    approximation_numerator = -primitive_rational
    assert approximation_denominator > 0
    assert math.gcd(
        abs(approximation_denominator), abs(approximation_numerator)
    ) == 1
    # If alpha=e+pi and L=N!*alpha+rho, then the following reduced
    # rational has the exact error |alpha-p/q|=L/N! whenever L>0.
    assert Fraction(approximation_denominator, factorial) == Fraction(
        denominator, content
    )

    return {
        "N": exponent,
        "N_mod_8": exponent % 8,
        "R_N": real,
        "I_N": imaginary,
        "M_N": m_native,
        "m_sparse": m_value,
        "degree_h": int(sp.degree(h_poly, x)),
        "h_minus_one_over_u_squared_sha256": hashlib.sha256(
            str(sp.Poly(q_h, x).all_coeffs()).encode()
        ).hexdigest(),
        "residual_degree": int(sp.degree(residual, x)),
        "residual_at_x_1": int(residual.subs(x, 1)),
        "residual_at_x_0": int(residual.subs(x, 0)),
        "weighted_exp_moment_pair_A_plus_B_over_e": [
            str(moment_pair[0]),
            str(moment_pair[1]),
        ],
        "baseline_moment_pair_A_plus_B_over_e": [
            str(baseline_pair[0]),
            str(baseline_pair[1]),
        ],
        "rho": str(rho),
        "rho_denominator": denominator,
        "output_content": content,
        "primitive_pair": [primitive_e_pi, primitive_rational],
        "rational_approximant_p_over_q": [
            approximation_numerator,
            approximation_denominator,
        ],
        "exact_approximant_error_scale": "L/N!",
        "q_output_sha256": hashlib.sha256(
            str(sp.Poly(q_output, x).all_coeffs()).encode()
        ).hexdigest(),
    }


def degree_threshold_table(maximum_n: int = 100) -> list[dict[str, object]]:
    rows = []
    for exponent in range(2, maximum_n + 1):
        real, imaginary = gaussian_power_one_minus_i(exponent)
        m_native = math.factorial(exponent) - real
        assert m_native > 0 and m_native % 2 == 0
        sign_possible = imaginary <= 0
        expected = exponent % 8 not in {5, 6, 7}
        assert sign_possible == expected
        row: dict[str, object] = {
            "N": exponent,
            "N_mod_8": exponent % 8,
            "I_N_sign": (imaginary > 0) - (imaginary < 0),
            "sign_not_immediately_excluded": sign_possible,
            "M_N_bits": m_native.bit_length(),
        }
        if sign_possible:
            fourth = strict_power_threshold(
                m_native * (exponent + 1), 162, 4
            )
            square = strict_power_threshold(
                max(0, -imaginary) * (exponent + 1), 24, 2
            )
            assert 162 * fourth**4 > m_native * (exponent + 1)
            if fourth:
                assert 162 * (fourth - 1) ** 4 <= m_native * (exponent + 1)
            row.update(
                {
                    "exact_rational_fourth_root_degree_floor": fourth,
                    "fourth_root_degree_bits": fourth.bit_length(),
                    "exact_rational_square_root_degree_floor": square,
                }
            )
        rows.append(row)
    return rows


def main() -> None:
    dependencies = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependencies[relative] = {"expected": expected, "actual": actual}

    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__))
    assert source_control["clean"] and script_control["clean"]

    symbolic = symbolic_integrating_factor_check()
    cases = [
        exact_case(8, 5),
        exact_case(9, 7),
        exact_case(10, 8),
    ]
    thresholds = degree_threshold_table()

    payload = {
        "schema": "common_kernel_native_sign_endpoint_degree_certificate_v2",
        "logical_scope": (
            "Exact replay for an all-parameter conditional sign theorem. "
            "It proves that any one-signed native residual has "
            "factorial-quarter-root localizer degree and isolates "
            "D/g=o(N) as the additional primitive-decay condition. "
            "It neither constructs a sign-controlled localizer nor "
            "classifies e+pi."
        ),
        "all_parameter_theorem": {
            "admissible_h": (
                "h in Z[x], h=1 mod (1+x^2)^2, h(0)=0, "
                "and 0<=h<=1 on [0,1]"
            ),
            "impossible_N_mod_8": [5, 6, 7],
            "degree_bound": "d^4 >= M_N*(N+1)/(54e)",
            "secondary_bound": "d^2 >= (-I_N)*(N+1)/(8e) when I_N<0",
            "raw_integral_bounds": "1/(N+1) <= L <= 5e/(N+1)",
            "primitive_decay_equivalence": "Lambda->0 iff D/g=o(N)",
            "exact_rational_approximation_error": (
                "|e+pi-p/q|=L/N! with q=N!*D/g"
            ),
            "conditional_roth_threshold": (
                "q<=(N!)^(1/2-delta), equivalently "
                "g/D>=(N!)^(1/2+delta), infinitely often"
            ),
            "proof_location": "Sections 2--6 of the companion source",
        },
        "symbolic_integrating_factor": symbolic,
        "exact_polynomial_cases": cases,
        "rational_degree_thresholds_N_2_through_100": thresholds,
        "dependency_checks": dependencies,
        "source_sha256": sha256(SOURCE),
        "control_audit": {
            "source": source_control,
            "script": script_control,
        },
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "The 40-GiB value is a failure guard only; it does not "
                "allocate or cap the approximately 50 GiB Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: all checks are exact symbolic, integer, "
                "polynomial, or rational arithmetic."
            ),
        },
        "remaining_gap": (
            "Existence of a sign-controlled h in the nonexcluded residue "
            "classes, the arithmetic ratio D/g=o(N), and a fortiori the "
            "stronger Roth-scale content threshold remain open."
        ),
    }

    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_GUARD_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
