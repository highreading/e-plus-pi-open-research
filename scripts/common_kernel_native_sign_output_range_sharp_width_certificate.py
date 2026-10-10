#!/usr/bin/env python3
"""Deterministic replay for the sharp native sign-output width theorem.

The symbolic layer checks the integrating-factor weight, the generalized
right-endpoint jet with c=1/m, and every exact constant used in the explicit
construction.  High-precision quadrature rows are diagnostics only; the
theorem's limiting statements are proved analytically in the source.
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
SOURCE = ROOT / "sources/common_kernel_native_sign_output_range_sharp_width.md"
OUTPUT = (
    ROOT
    / "results/common_kernel_native_sign_output_range_sharp_width_certificate.json"
)
RSS_CAP_KIB = 2 * 1024 * 1024

t, s, y = sp.symbols("t s y")


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


def native_parameters(exponent: int) -> dict[str, int]:
    real, imaginary = gaussian_power_one_minus_i(exponent)
    assert imaginary <= 0
    a_value = -imaginary
    b_value = (math.factorial(exponent) - real) // 2
    assert 2 * b_value == math.factorial(exponent) - real
    total = a_value + b_value
    divisor = math.gcd(total, b_value)
    ell = total // divisor
    assert (b_value * ell) % total == 0
    return {
        "N": exponent,
        "R_N": real,
        "I_N": imaginary,
        "a": a_value,
        "b": b_value,
        "A": total,
        "gcd_A_b": divisor,
        "ell": ell,
        "b_ell_over_A": b_value * ell // total,
    }


def symbolic_checks() -> dict[str, object]:
    n_sym, a_total, b_sym, ell, c = sp.symbols(
        "N A b ell c", positive=True
    )
    v = t**2 - 2 * t + 2
    r_weight = sp.E + 4 * sp.exp(t) / v
    derivative = sp.factor(sp.diff(r_weight, t))
    expected_derivative = 4 * sp.exp(t) * (2 - t) ** 2 / v**2
    assert sp.simplify(derivative - expected_derivative) == 0
    assert sp.simplify(r_weight.subs(t, 0) - (sp.E + 2)) == 0
    assert sp.simplify(r_weight.subs(t, 1) - 5 * sp.E) == 0

    # Work after removing the common factor e^{-1}.  Namely,
    # J=e^{-1}*j_tilde and mu=e^{-1}*mu_tilde.
    integrand = sp.series(
        sp.exp(y) * (1 - y) ** n_sym, y, 0, 5
    ).removeO()
    j_tilde = sp.integrate(integrand, (y, 0, s))
    mu_tilde = (1 - s) * (a_total - b_sym * s) * sp.exp(s)
    # epsilon_c=c/(e*A*ell), so e*epsilon_c=c/(A*ell).
    phi_tilde = c * j_tilde**2 / (j_tilde + c / (a_total * ell))
    h_right = sp.series(phi_tilde / mu_tilde, s, 0, 4).removeO()
    cubic = ell * (1 - n_sym) - a_total * ell**2 / c + b_sym * ell / a_total
    expected_h = ell * s**2 + cubic * s**3
    assert sp.simplify(h_right - expected_h) == 0

    q_right = sp.series((h_right - 1) / (1 + s**2) ** 2, s, 0, 4).removeO()
    expected_q_right = -1 + (ell + 2) * s**2 + cubic * s**3
    assert sp.simplify(q_right - expected_q_right) == 0
    q_left = sp.series(-4 * t**2 / v**2, t, 0, 4).removeO()
    assert sp.expand(q_left) == -t**2 - 2 * t**3

    r_three_quarters = sp.simplify(r_weight.subs(t, sp.Rational(3, 4)))
    r_one_quarter = sp.simplify(r_weight.subs(t, sp.Rational(1, 4)))
    r_difference = sp.simplify(r_three_quarters - r_one_quarter)
    expected_difference = 64 * (
        sp.exp(sp.Rational(3, 4)) / 17
        - sp.exp(sp.Rational(1, 4)) / 25
    )
    assert sp.simplify(r_difference - expected_difference) == 0

    # The logarithmic inequality in the explicit C_N lower bound.
    assert sp.Rational(56, 25) < 3
    assert sp.Rational(25, 32) == 1 - sp.Rational(7, 4) / 8

    return {
        "R_prime": str(expected_derivative),
        "R_0": str(r_weight.subs(t, 0)),
        "R_1": str(r_weight.subs(t, 1)),
        "H_right_through_s3": str(expected_h),
        "q_right_through_s3": str(expected_q_right),
        "q_left_through_t3": str(q_left),
        "R_three_quarters_minus_R_one_quarter": str(r_difference),
        "explicit_log_exponent": "56/25<3",
    }


def integral_jet_rows() -> list[dict[str, int]]:
    rows = []
    for exponent in range(8, 41):
        if exponent % 8 in {5, 6, 7}:
            continue
        row = native_parameters(exponent)
        for m_value in (2, 4, 7):
            cubic = (
                row["ell"] * (1 - exponent)
                - m_value * row["A"] * row["ell"] ** 2
                + row["b_ell_over_A"]
            )
            assert isinstance(cubic, int)
            if exponent in {8, 9, 10, 11, 12, 16, 24, 32, 40}:
                rows.append({**row, "m": m_value, "right_cubic": cubic})
    return rows


def mp_r(value: mp.mpf) -> mp.mpf:
    return mp.e + 4 * mp.e**value / (value * value - 2 * value + 2)


def smooth_step(value: mp.mpf) -> mp.mpf:
    if value <= 0:
        return mp.mpf("0")
    if value >= 1:
        return mp.mpf("1")
    left = mp.e ** (-1 / value)
    right = mp.e ** (-1 / (1 - value))
    return left / (left + right)


def chi(value: mp.mpf) -> mp.mpf:
    return smooth_step(4 * (value - 1)) * smooth_step(4 * (2 - value))


def rho_unnormalized(value: mp.mpf) -> mp.mpf:
    if abs(value) >= 1:
        return mp.mpf("0")
    return mp.e ** (-1 / (1 - value * value))


def numerical_diagnostics() -> dict[str, object]:
    mp.mp.dps = 80
    rho_mass = mp.quad(rho_unnormalized, [-1, 0, 1])
    early_average = mp.quad(
        lambda x: mp_r((x + 3) / 16) * rho_unnormalized(x) / rho_mass,
        [-1, 0, 1],
    )

    rows = []
    for exponent in (8, 9, 10, 11, 12, 16, 24, 32, 48, 64, 96, 128):
        if exponent % 8 in {5, 6, 7}:
            continue
        n_mp = mp.mpf(exponent)
        b_mass = mp.quad(lambda z: mp.e ** (-z) * z**exponent, [0, 1])
        c_mass = mp.quad(
            lambda yy: (
                mp.e ** (-(1 - yy / n_mp))
                * (1 - yy / n_mp) ** exponent
                * chi(yy)
                / n_mp
            ),
            [1, mp.mpf("1.25"), mp.mpf("1.75"), 2],
        )
        late_num = mp.quad(
            lambda yy: (
                mp_r(1 - yy / n_mp)
                * mp.e ** (-(1 - yy / n_mp))
                * (1 - yy / n_mp) ** exponent
                * chi(yy)
                / n_mp
            ),
            [1, mp.mpf("1.25"), mp.mpf("1.75"), 2],
        )
        late_average = late_num / c_mass
        delta = mp.mpf("0.5") * c_mass * (late_average - early_average)
        assert delta > 0
        assert c_mass >= mp.e ** -4 / (2 * exponent)
        rows.append(
            {
                "N": exponent,
                "N_B_N": mp.nstr(exponent * b_mass, 30),
                "N_C_N_chi": mp.nstr(exponent * c_mass, 30),
                "late_R_average": mp.nstr(late_average, 30),
                "early_R_average": mp.nstr(early_average, 30),
                "N_explicit_delta": mp.nstr(exponent * delta, 30),
                "upper_scaled_diameter": mp.nstr(
                    exponent * (4 * mp.e - 2) * b_mass, 30
                ),
            }
        )

    c_star = 16 * mp.e ** -4 * (
        mp.e ** mp.mpf("0.75") / 17
        - mp.e ** mp.mpf("0.25") / 25
    )
    sharp = 4 - 2 / mp.e
    return {
        "R_0": mp.nstr(mp_r(mp.mpf("0")), 40),
        "R_1": mp.nstr(mp_r(mp.mpf("1")), 40),
        "R_one_quarter": mp.nstr(mp_r(mp.mpf("0.25")), 40),
        "R_three_quarters": mp.nstr(mp_r(mp.mpf("0.75")), 40),
        "c_star": mp.nstr(c_star, 40),
        "sharp_scaled_width": mp.nstr(sharp, 40),
        "raw_multiplier_ratio": mp.nstr(5 * mp.e / (4 * mp.e - 2), 40),
        "fixed_cutoff_rows_nonproof": rows,
    }


def main() -> None:
    source_audit = control_and_tex_audit(SOURCE)
    script_audit = control_and_tex_audit(Path(__file__))
    assert source_audit["clean"] and script_audit["clean"]

    payload = {
        "schema": "common_kernel_native_sign_output_range_sharp_width_v1",
        "scope": (
            "Sharp real-output diameter and rational-grid limitation for the "
            "native sign family. No irrationality or transcendence claim."
        ),
        "all_parameter_results": {
            "universal_output_interval": "((e+2)*B_N, 5*e*B_N)",
            "universal_width": "<=(4*e-2)*B_N",
            "sharp_same_germ_limit": "lim N*W_N=4-2/e",
            "explicit_width": "Delta_N>=c_star/N for admissible N>=8",
            "grid_denominator": "D<=floor(1/w_N)+1",
            "native_divergent_width_condition": "N*w_N->infinity is impossible",
        },
        "symbolic_checks": symbolic_checks(),
        "integral_endpoint_jet_rows": integral_jet_rows(),
        "numerical_diagnostics_nonproof": numerical_diagnostics(),
        "source_sha256": sha256(SOURCE),
        "control_and_tex_audit": {
            "source": source_audit,
            "script": script_audit,
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
