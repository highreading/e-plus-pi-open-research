#!/usr/bin/env python3
"""Replay for the quantitative native integer--Bernstein audit.

The symbolic checks verify the optimized endpoint jet, the explicit Hermite
CRT polynomial, the four-beta-moment identity, and the elementary ingredients
of the quantitative C^3 estimate.  Floating-point rows are explicitly marked
as asymptotic diagnostics and are not substituted for any theorem.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "sources/common_kernel_integer_bernstein_quantitative_arithmetic_audit.md"
)
OUTPUT = (
    ROOT
    / "results/common_kernel_integer_bernstein_quantitative_arithmetic_certificate.json"
)
RSS_CAP_KIB = 2 * 1024 * 1024

t, x, s = sp.symbols("t x s")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM unavailable")


def control_and_tex_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte not in (9, 10)
    ]
    text = data.decode("utf-8")
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    duplicate_tags = sorted({tag for tag in tags if tags.count(tag) > 1})
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "inline_open_close": [text.count(r"\("), text.count(r"\)")],
        "display_open_close": [text.count(r"\["), text.count(r"\]")],
        "equation_tag_count": len(tags),
        "duplicate_equation_tags": duplicate_tags,
        "clean": (
            not forbidden
            and text.count(r"\(") == text.count(r"\)")
            and text.count(r"\[") == text.count(r"\]")
            and not duplicate_tags
        ),
    }


def gaussian_power_one_minus_i(exponent: int) -> tuple[int, int]:
    real, imaginary = 1, 0
    for _ in range(exponent):
        real, imaginary = real + imaginary, imaginary - real
    return real, imaginary


def parameters(exponent: int) -> dict[str, int]:
    real, imaginary = gaussian_power_one_minus_i(exponent)
    assert imaginary <= 0
    a_value = -imaginary
    m_value = math.factorial(exponent) - real
    assert m_value > 0 and m_value % 2 == 0
    b_value = m_value // 2
    a_total = a_value + b_value
    ell_value = a_total // math.gcd(a_total, b_value)
    assert a_total % math.gcd(a_total, b_value) == 0
    assert (b_value * ell_value) % a_total == 0
    return {
        "N": exponent,
        "R_N": real,
        "I_N": imaginary,
        "a": a_value,
        "b": b_value,
        "A": a_total,
        "ell": ell_value,
        "b_ell_over_A": b_value * ell_value // a_total,
    }


def optimized_endpoint_series() -> dict[str, str]:
    n_sym, a_total, b_sym, ell = sp.symbols(
        "N A b ell", integer=True, positive=True
    )
    y = sp.symbols("y")
    integrand = sp.series(
        sp.exp(y) * (1 - y) ** n_sym, y, 0, 5
    ).removeO()
    j_tilde = sp.integrate(integrand, (y, 0, s))
    mu_tilde = (1 - s) * (a_total - b_sym * s) * sp.exp(s)
    phi_tilde = j_tilde**2 / (j_tilde + 1 / (a_total * ell))
    h_right = sp.series(phi_tilde / mu_tilde, s, 0, 4).removeO()
    cubic = ell * (1 - n_sym) - a_total * ell**2 + b_sym * ell / a_total
    assert sp.simplify(h_right.coeff(s, 0)) == 0
    assert sp.simplify(h_right.coeff(s, 1)) == 0
    assert sp.simplify(h_right.coeff(s, 2) - ell) == 0
    assert sp.simplify(h_right.coeff(s, 3) - cubic) == 0

    q_right = sp.series(
        (h_right - 1) / (1 + s**2) ** 2, s, 0, 4
    ).removeO()
    assert sp.simplify(q_right.coeff(s, 0) + 1) == 0
    assert sp.simplify(q_right.coeff(s, 1)) == 0
    assert sp.simplify(q_right.coeff(s, 2) - (ell + 2)) == 0
    assert sp.simplify(q_right.coeff(s, 3) - cubic) == 0

    v = t**2 - 2 * t + 2
    q_left = sp.series(-4 * t**2 / v**2, t, 0, 4).removeO()
    assert sp.expand(q_left) == -t**2 - 2 * t**3
    return {
        "H_right_s2": str(ell),
        "H_right_s3": str(cubic),
        "q_right_through_s3": str(q_right),
        "q_left_through_t3": str(q_left),
    }


def hermite_crt_checks() -> dict[str, object]:
    n_sym, a_total, b_sym, ell = sp.symbols(
        "N A b ell", integer=True
    )
    e0 = (-20 * t**3 + 70 * t**2 - 84 * t + 35) * t**4
    e1 = (20 * t**3 + 10 * t**2 + 4 * t + 1) * (t - 1) ** 4
    assert sp.expand(e0 + e1) == 1
    cubic = ell * (1 - n_sym) - a_total * ell**2 + b_sym * ell / a_total
    t0 = -t**2 - 2 * t**3
    t1 = -1 + (ell + 2) * (t - 1) ** 2 - cubic * (t - 1) ** 3
    hermite = sp.expand(e1 * t0 + e0 * t1)
    assert sp.rem(hermite - t0, t**4, t) == 0
    assert sp.rem(hermite - t1, (t - 1) ** 4, t) == 0

    rows = []
    for exponent in [2, 3, 4, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20]:
        if exponent % 8 in {5, 6, 7}:
            continue
        row = parameters(exponent)
        instance = sp.Poly(
            hermite.subs(
                {
                    n_sym: exponent,
                    a_total: row["A"],
                    b_sym: row["b"],
                    ell: row["ell"],
                }
            ),
            t,
            domain=sp.ZZ,
        )
        assert instance.degree() <= 10
        rows.append(
            {
                **row,
                "hermite_degree": instance.degree(),
                "hermite_coefficient_sha256": hashlib.sha256(
                    str(instance.all_coeffs()).encode()
                ).hexdigest(),
            }
        )

    return {
        "bezout_identity": "E0+E1=1",
        "symbolic_degree": int(sp.degree(hermite, t)),
        "representative_rows": rows,
    }


def four_beta_identity_checks() -> dict[str, object]:
    a_sym, b_sym = sp.symbols("a b", integer=True)
    q_coeffs = sp.symbols("q0:6")
    q_t = sum(q_coeffs[j] * t**j for j in range(6))
    q_x = sp.expand(q_t.subs(t, 1 - x))
    u = 1 + x**2
    k_x = -(a_sym + b_sym) + b_sym * x
    y_poly = sp.expand(u**2 * q_x * k_x)
    stein = sp.expand((1 - x) * sp.diff(y_poly, x) - x * y_poly)
    quotient = sp.cancel(stein / u)
    assert sp.denom(quotient) == 1
    left = sp.integrate(quotient, (x, 0, 1))
    weight = (a_sym + b_sym * t) * t * (2 - t) ** 2
    right = (
        -q_t.subs(t, 1) * k_x.subs(x, 0)
        - sp.integrate(q_t * weight, (t, 0, 1))
    )
    assert sp.simplify(left - right) == 0
    special_right = sp.simplify(right.subs(q_coeffs[0], -1 - sum(q_coeffs[1:])))
    expected_special = (
        k_x.subs(x, 0) - sp.integrate(
            q_t.subs(q_coeffs[0], -1 - sum(q_coeffs[1:])) * weight,
            (t, 0, 1),
        )
    )
    assert sp.simplify(special_right - expected_special) == 0

    expanded_weight = sp.expand(weight)
    expected_weight = (
        4 * a_sym * t
        + 4 * (b_sym - a_sym) * t**2
        + (a_sym - 4 * b_sym) * t**3
        + b_sym * t**4
    )
    assert sp.expand(expanded_weight - expected_weight) == 0

    beta_rows = []
    n_value = 9
    for k_value in range(n_value + 1):
        for j_value in range(1, 5):
            integral = sp.integrate(
                t ** (k_value + j_value) * (1 - t) ** (n_value - k_value),
                (t, 0, 1),
            )
            expected = sp.Rational(
                math.factorial(k_value + j_value)
                * math.factorial(n_value - k_value),
                math.factorial(n_value + j_value + 1),
            )
            assert integral == expected
            beta_rows.append(
                {
                    "n": n_value,
                    "k": k_value,
                    "j": j_value,
                    "value": str(integral),
                }
            )
    return {
        "integration_by_parts_difference": "0",
        "expanded_weight": str(expanded_weight),
        "beta_rows_n_9": beta_rows,
    }


def bernstein_estimate_ingredients() -> dict[str, object]:
    n_sym, z = sp.symbols("n z", integer=True, positive=True)
    alpha = sp.expand(n_sym * (n_sym - 1) * (n_sym - 2) / n_sym**3)
    assert sp.simplify(1 - alpha - (3 / n_sym - 2 / n_sym**2)) == 0

    # K~Bin(n-3,z), S=sum of three U[0,1], X=(K+S)/n.
    bias = sp.simplify(((n_sym - 3) * z + sp.Rational(3, 2)) / n_sym - z)
    variance = (
        (n_sym - 3) * z * (1 - z) + sp.Rational(1, 4)
    ) / n_sym**2
    assert sp.simplify(bias - 3 * (sp.Rational(1, 2) - z) / n_sym) == 0

    # The exact endpoint Taylor-to-rounding constant used in (49).
    endpoint_constant = sp.Rational(3**4, 24)
    rounding_product_constant = sp.Rational(9, 16)
    assert endpoint_constant == sp.Rational(27, 8)
    endpoint_product = (
        n_sym * (n_sym - 1) * (n_sym - 2) / 6
        * sp.Rational(3**4, 24)
        / n_sym**4
    )
    positive_difference = sp.factor(
        rounding_product_constant / n_sym - endpoint_product
    )
    assert sp.simplify(
        positive_difference - 9 * (3 * n_sym - 2) / (16 * n_sym**3)
    ) == 0

    return {
        "alpha_n": str(alpha),
        "one_minus_alpha_n": "3/n-2/n^2",
        "mean_bias": str(bias),
        "variance": str(variance),
        "endpoint_normalized_error_constant": str(endpoint_constant),
        "endpoint_rounding_threshold_constant": str(rounding_product_constant),
        "endpoint_product_bound_difference": str(positive_difference),
        "rounding_third_derivative_bound": "27*M4/n+96/(n-3)",
        "classical_third_derivative_bound": (
            "(3*M3+(3/2)*M4+(1/4)*M5)/n"
        ),
    }


def asymptotic_diagnostics() -> list[dict[str, object]]:
    mp.mp.dps = 100
    rows = []
    exponents = [2, 3, 4, 8, 9, 10, 11, 12, 16, 20, 24, 32, 40, 48, 64]
    for exponent in exponents:
        if exponent % 8 in {5, 6, 7}:
            continue
        row = parameters(exponent)
        a_value = mp.mpf(row["a"])
        b_value = mp.mpf(row["b"])
        a_total = mp.mpf(row["A"])
        ell = mp.mpf(row["ell"])
        epsilon = 1 / (mp.e * a_total * ell)
        j_value = (
            mp.e ** -1
            * (1 - mp.mpf(4) ** (-(exponent + 1)))
            / (exponent + 1)
        )
        gamma = j_value**2 / (j_value + epsilon)
        theta = gamma / (
            a_value + mp.sqrt(a_value**2 + 2 * b_value * gamma)
        )
        rho = epsilon**2 * mp.e**-1 * theta**exponent
        m_native = math.factorial(exponent) - row["R_N"]
        lower_log_degree = (
            mp.log(m_native)
            + mp.log(exponent + 1)
            - mp.log(54 * mp.e)
        ) / 4
        margin_inverse_log = -mp.log(rho / (10 * a_total))
        leading = mp.mpf(exponent) * mp.log(a_total) / 2
        rows.append(
            {
                **row,
                "log_A": mp.nstr(mp.log(a_total), 30),
                "minus_log_theta": mp.nstr(-mp.log(theta), 30),
                "minus_log_rho_over_10A": mp.nstr(margin_inverse_log, 30),
                "half_N_log_A": mp.nstr(leading, 30),
                "margin_to_half_N_log_A_ratio": mp.nstr(
                    margin_inverse_log / leading, 20
                ),
                "universal_lower_log_degree": mp.nstr(lower_log_degree, 30),
            }
        )
    return rows


def main() -> None:
    source_audit = control_and_tex_audit(SOURCE)
    script_audit = control_and_tex_audit(Path(__file__))
    assert source_audit["clean"] and script_audit["clean"]

    payload = {
        "schema": (
            "common_kernel_integer_bernstein_quantitative_arithmetic_"
            "certificate_v1"
        ),
        "scope": (
            "Quantitative replay for one explicit smoothed integer-Bernstein "
            "realization. It proves neither a Roth-scale content subsequence "
            "nor its impossibility."
        ),
        "all_parameter_results": {
            "optimized_endpoint_parameter": "ell=A/gcd(A,b)",
            "epsilon": "1/(e*A*ell)",
            "explicit_C3_error": (
                "(3*M3+(57/2)*M4+(1/4)*M5)/n+96/(n-3)"
            ),
            "rounding_threshold": "n>=8 and n>9*M4/8",
            "sufficient_log_degree": (
                "<=(N/2)*log(A)+O(N*log(N))"
            ),
            "coefficient_height": "<=n*log(6)+O(N*log(N))",
            "output_denominator_divides": "lcm(1,...,n+5)",
            "remaining_content": "gcd(N!, four-beta-moment numerator)",
        },
        "optimized_endpoint_series": optimized_endpoint_series(),
        "hermite_crt_checks": hermite_crt_checks(),
        "four_beta_identity_checks": four_beta_identity_checks(),
        "bernstein_estimate_ingredients": bernstein_estimate_ingredients(),
        "asymptotic_diagnostics_nonproof": asymptotic_diagnostics(),
        "source_sha256": sha256(SOURCE),
        "control_and_tex_audit": {
            "source": source_audit,
            "script": script_audit,
        },
        "primary_source": {
            "author": "Borislav R. Draganov",
            "title": (
                "Simultaneous approximation by Bernstein polynomials with "
                "integer coefficients"
            ),
            "journal": "Journal of Approximation Theory 237 (2019), 1--16",
            "doi": "10.1016/j.jat.2018.08.003",
            "arxiv": "1804.08248",
            "theorems": ["1.2", "2.3"],
        },
        "resource_policy": {
            "rss_cap_kib": RSS_CAP_KIB,
            "measured_peak_rss": (
                "checked against the cap and printed at replay time; omitted "
                "from JSON so the certificate remains byte-deterministic"
            ),
            "accelerator": "not used; exact symbolic and small MP arithmetic",
        },
    }
    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_CAP_KIB
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
