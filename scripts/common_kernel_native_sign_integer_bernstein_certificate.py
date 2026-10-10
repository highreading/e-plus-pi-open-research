#!/usr/bin/env python3
"""Exact replay for native sign existence via integer Bernstein approximation.

The finite diagnostics verify the algebraic identities, crossing estimates, and
endpoint lattice data.  The all-degree approximation step is Theorem 1.3 of
Draganov (J. Approx. Theory 237 (2019), 1--16), as stated and applied in the
companion proof; no finite scan is used as a substitute for that theorem.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_native_sign_integer_bernstein_existence.md"
OUTPUT = ROOT / "results/common_kernel_native_sign_integer_bernstein_certificate.json"
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_native_sign_endpoint_degree_hashes.sha256":
        "400b4e5ae612683394a657c69f6aee4e1e2369b0d518f8c6027d51aa26c3efc3",
}

t, s = sp.symbols("t s")


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


def native_parameters(exponent: int) -> tuple[int, int, int, int]:
    real, imaginary = gaussian_power_one_minus_i(exponent)
    m_native = math.factorial(exponent) - real
    assert m_native > 0 and m_native % 2 == 0
    a_value = -imaginary
    b_value = m_native // 2
    return real, imaginary, a_value, b_value


def symbolic_differential_checks() -> dict[str, str]:
    a, b, epsilon, y = sp.symbols("a b epsilon y", positive=True)
    mu = t * (a + b * t) * sp.exp(-t)
    mu_prime_target = sp.exp(-t) * (a * (1 - t) + b * t * (2 - t))
    assert sp.simplify(sp.diff(mu, t) - mu_prime_target) == 0

    phi = y**2 / (y + epsilon)
    phi_prime = sp.diff(phi, y)
    assert sp.simplify(
        phi_prime - (1 - epsilon**2 / (y + epsilon) ** 2)
    ) == 0

    left = sp.expand(mu * (1 - 4 * t**2))
    left_log_target = (
        1 / t + b / (a + b * t) - 1 - 8 * t / (1 - 4 * t**2)
    )
    assert sp.simplify(sp.diff(left, t) / left - left_log_target) == 0

    H, Hp = sp.symbols("H Hp")
    coefficient = a * (1 - t) + b * t * (2 - t)
    # This line records the exact integrating-factor algebra independently of
    # the unspecified exponent in w=e^-t*t^N.
    g_derivative = sp.diff(mu, t) * H + mu * Hp
    assert sp.simplify(
        g_derivative
        - sp.exp(-t) * (t * (a + b * t) * Hp + coefficient * H)
    ) == 0

    return {
        "mu_prime": "exp(-t)*(a*(1-t)+b*t*(2-t))",
        "phi_prime": "1-epsilon^2/(y+epsilon)^2",
        "left_log_derivative": (
            "1/t+b/(a+b*t)-1-8*t/(1-4*t^2)"
        ),
        "integrating_factor_difference": "0",
    }


def endpoint_series_checks() -> dict[str, object]:
    N, A, b = sp.symbols("N A b", integer=True, positive=True)
    y = sp.symbols("y")

    integrand = sp.series(sp.exp(y) * (1 - y) ** N, y, 0, 5).removeO()
    j_tilde = sp.integrate(integrand, (y, 0, s))
    mu_tilde = (1 - s) * (A - b * s) * sp.exp(s)
    g_tilde = j_tilde**2 / (j_tilde + A ** -2)
    h_right = sp.series(g_tilde / mu_tilde, s, 0, 4).removeO()
    expected_cubic = -A**3 + A * (1 - N) + b
    assert sp.simplify(h_right.coeff(s, 0)) == 0
    assert sp.simplify(h_right.coeff(s, 1)) == 0
    assert sp.simplify(h_right.coeff(s, 2) - A) == 0
    assert sp.simplify(h_right.coeff(s, 3) - expected_cubic) == 0

    q_right = sp.series(
        (h_right - 1) / (1 + s**2) ** 2, s, 0, 4
    ).removeO()
    assert sp.simplify(q_right.coeff(s, 0) + 1) == 0
    assert sp.simplify(q_right.coeff(s, 1)) == 0
    assert sp.simplify(q_right.coeff(s, 2) - (A + 2)) == 0
    assert sp.simplify(q_right.coeff(s, 3) - expected_cubic) == 0

    v = t**2 - 2 * t + 2
    q_left = sp.series(-4 * t**2 / v**2, t, 0, 4).removeO()
    assert sp.expand(q_left) == -t**2 - 2 * t**3

    return {
        "left_q_through_cubic": str(q_left),
        "right_H_coefficients_s2_s3": ["A", str(expected_cubic)],
        "right_q_coefficients_s0_s1_s2_s3": [
            "-1", "0", "A + 2", str(expected_cubic),
        ],
        "integral_jet_statement": (
            "q^(j)(0)/j! and q^(j)(1)/j! are integers for 0<=j<=3"
        ),
    }


def crossing_inequality_checks() -> dict[str, object]:
    exponential_upper = Fraction(113, 88)
    assert exponential_upper < Fraction(9, 7)

    n2_left_lower = Fraction(27, 64) * Fraction(7, 9)
    n2_tail_upper = Fraction(21, 64)
    assert n2_left_lower == n2_tail_upper

    n3_left_lower = Fraction(9, 16) * Fraction(3, 4)
    assert n3_left_lower == Fraction(27, 64) > Fraction(1, 4)

    general_left_lower = Fraction(3 * 14, 64) * Fraction(3, 4)
    assert general_left_lower == Fraction(126, 256) > Fraction(1, 5)

    rows = []
    for exponent in range(2, 101):
        real, imaginary, a_value, b_value = native_parameters(exponent)
        if exponent >= 4:
            assert b_value >= 14
        rows.append({
            "N": exponent,
            "R_N": real,
            "I_N": imaginary,
            "a": a_value,
            "b": b_value,
            "sign_allowed": imaginary <= 0,
            "expected_allowed_mod_8": exponent % 8 not in {5, 6, 7},
        })
        assert rows[-1]["sign_allowed"] == rows[-1]["expected_allowed_mod_8"]

    return {
        "exp_one_quarter_upper": str(exponential_upper),
        "exp_one_quarter_target": "9/7",
        "N2_strict_comparison": (
            "(27/64)*exp(-1/4) > 21/64 because exp(1/4)<9/7"
        ),
        "N3_left_lower": str(n3_left_lower),
        "N_ge_4_left_lower_using_b_ge_14": str(general_left_lower),
        "parameter_rows_N_2_through_100": rows,
    }


def integral_hermite_crt_checks() -> dict[str, object]:
    N, A, b = sp.symbols("N A b", integer=True)
    modulus_left = t**4
    modulus_right = (t - 1) ** 4
    inverse = sp.invert(modulus_left, modulus_right)
    assert sp.expand(inverse) == -20 * t**3 + 70 * t**2 - 84 * t + 35
    bezout_right = 20 * t**3 + 10 * t**2 + 4 * t + 1
    assert sp.expand(
        inverse * modulus_left + bezout_right * modulus_right
    ) == 1

    cubic = -A**3 + A * (1 - N) + b
    left_residue = -t**2 - 2 * t**3
    right_residue = -1 + (A + 2) * (t - 1) ** 2 - cubic * (t - 1) ** 3
    product_modulus = sp.expand(modulus_left * modulus_right)
    candidate = left_residue + modulus_left * inverse * (
        right_residue - left_residue
    )
    hermite = sp.rem(sp.expand(candidate), product_modulus, t)
    assert sp.rem(hermite - left_residue, modulus_left, t) == 0
    assert sp.rem(hermite - right_residue, modulus_right, t) == 0
    polynomial = sp.Poly(hermite, t, domain=sp.ZZ[N, A, b])

    examples = []
    for exponent in [2, 3, 4, 8, 9, 10, 11, 12]:
        _, imaginary, a_value, b_value = native_parameters(exponent)
        if imaginary > 0:
            continue
        A_value = a_value + b_value
        instance = sp.Poly(
            hermite.subs({N: exponent, A: A_value, b: b_value}),
            t,
            domain=sp.ZZ,
        )
        left = sp.rem(instance.as_expr() - left_residue, modulus_left, t)
        right_target = right_residue.subs(
            {N: exponent, A: A_value, b: b_value}
        )
        right = sp.rem(instance.as_expr() - right_target, modulus_right, t)
        assert left == 0 and right == 0
        examples.append({
            "N": exponent,
            "A": A_value,
            "b": b_value,
            "degree": instance.degree(),
            "coefficient_sha256": hashlib.sha256(
                str(instance.all_coeffs()).encode()
            ).hexdigest(),
        })

    return {
        "inverse_t4_mod_t_minus_1_4": str(inverse),
        "explicit_bezout_right_coefficient": str(bezout_right),
        "symbolic_hermite_degree": polynomial.degree(),
        "symbolic_coefficient_count": len(polynomial.all_coeffs()),
        "representative_instances": examples,
    }


def numerical_crossing_diagnostics() -> list[dict[str, str | int]]:
    """Representative high-precision checks only; not used in the proof."""
    mp.mp.dps = 60
    rows = []
    for exponent in [2, 3, 4, 8, 9, 10, 11, 12]:
        _, imaginary, a_value, b_value = native_parameters(exponent)
        if imaginary > 0:
            continue
        A_value = a_value + b_value
        epsilon = 1 / (mp.e * A_value**2)

        def tail(z: mp.mpf) -> mp.mpf:
            return mp.gammainc(exponent + 1, z, 1)

        def difference(z: mp.mpf) -> mp.mpf:
            mu = z * (a_value + b_value * z) * mp.exp(-z)
            left = mu * (1 - 4 * z**2)
            j_value = tail(z)
            right = j_value**2 / (j_value + epsilon)
            return left - right

        lo, hi = mp.mpf("0"), mp.mpf("0.25")
        assert difference(lo) < 0 and difference(hi) > 0
        for _ in range(240):
            middle = (lo + hi) / 2
            if difference(middle) < 0:
                lo = middle
            else:
                hi = middle
        tau = (lo + hi) / 2
        rows.append({
            "N": exponent,
            "a_bracketed_crossing_root": mp.nstr(tau, 40),
            "difference_at_one_quarter": mp.nstr(difference(mp.mpf("0.25")), 30),
        })
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

    payload = {
        "schema": "common_kernel_native_sign_integer_bernstein_certificate_v1",
        "logical_scope": (
            "Exact algebraic replay for an all-parameter sign-existence theorem. "
            "The published simultaneous integer-Bernstein theorem supplies the "
            "all-degree approximation step; finite diagnostics do not replace it. "
            "No degree, denominator/content, or e+pi classification follows."
        ),
        "all_parameter_theorem": {
            "existence_condition": "I_N<=0",
            "equivalent_mod_8_classes": [0, 1, 2, 3, 4],
            "impossible_mod_8_classes_from_dependency": [5, 6, 7],
            "admissible_output": (
                "h in Z[x], h=1 mod (1+x^2)^2, h(0)=0, "
                "0<=h<=1 and F_N,h>=0 on [0,1]"
            ),
            "quantitative_degree_claim": "none; prior lower bound still applies",
            "proof_location": "Sections 2--7 of the companion source",
        },
        "symbolic_differential_checks": symbolic_differential_checks(),
        "endpoint_series_checks": endpoint_series_checks(),
        "crossing_inequality_checks": crossing_inequality_checks(),
        "integral_hermite_crt_checks": integral_hermite_crt_checks(),
        "finite_numerical_crossing_diagnostics_nonproof": (
            numerical_crossing_diagnostics()
        ),
        "external_primary_theorem": {
            "author": "Borislav R. Draganov",
            "title": (
                "Simultaneous approximation by Bernstein polynomials with "
                "integer coefficients"
            ),
            "journal": "Journal of Approximation Theory 237 (2019), 1--16",
            "doi": "10.1016/j.jat.2018.08.003",
            "arxiv": "1804.08248",
            "used_result": (
                "Theorem 1.3 for the nearest-integer Bernstein operator, s=3"
            ),
            "coefficient_scope": (
                "ordinary monomial coefficients in Z, not merely integer-valued"
            ),
        },
        "dependency_checks": dependencies,
        "source_sha256": sha256(SOURCE),
        "control_audit": {
            "source": source_control,
            "script": script_control,
        },
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "The 40-GiB value is a failure guard, not an allocation or a "
                "2-GiB cap; the Colab instance has approximately 50 GiB RAM."
            ),
            "hardware_accelerator": (
                "Not used because every replay check is exact symbolic, integer, "
                "rational, or low-dimensional high-precision CPU arithmetic."
            ),
        },
        "remaining_gap": (
            "The construction supplies no useful degree/height bound and no "
            "control of the reduced output denominator D or primitive content g."
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
