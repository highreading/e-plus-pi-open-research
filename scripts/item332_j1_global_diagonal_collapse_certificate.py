#!/usr/bin/env python3
"""Exact replay for Item 332.

This checker proves that the fixed-M cubic carriers of Item 329 collapse,
on the actual moving row, to the already pinned Item-237/308 selected and
opposite factors.  It verifies the characteristic-zero Hermite identity,
the fixed algebraic diagonal, the dual J/L reduction, denominator support,
and five declared replay rows.  No prime scan is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item332_j1_global_diagonal_collapse_certificate.json"

DEPENDENCIES = {
    "sources/item237_j1_algebraic_residual_report.md":
        "dd1278d5ec6e3960d5539f3b349f2245449d4801663beb7915140d722a62c569",
    "scripts/item237_j1_algebraic_residual_certificate.py":
        "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf",
    "results/item237_j1_algebraic_residual_certificate.json":
        "eba1519f4d376d442f396048528190b474cc5464bbe42c3bdf31a9bdaf39dd6b",
    "results/item237_root_audit.json":
        "eba1519f4d376d442f396048528190b474cc5464bbe42c3bdf31a9bdaf39dd6b",
    "manifests/item237_j1_algebraic_residual_manifest.json":
        "3d18d6d997612166ce4dd4b4cb983fa6d0a20def46cc07d7d456c32be9ce55c0",
    "sources/item308_j1_all_s_fixed_divisor_no_go_report.md":
        "4eb8f8c37dfde9d19e57c8df5ff8090bd95f03be59fff7d6aede55d02993bdc8",
    "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py":
        "9b60d380b503c7ac9fed13792fae67735cfcf6b0f376581a0076fde16a82f0b9",
    "results/item308_j1_all_s_fixed_divisor_no_go_certificate.json":
        "4efff9ca2fb1bc11cc6030e260ff73aae89c28bd157bb41fa6bbc3b32e41e5cf",
    "results/item308_root_audit.json":
        "11feb8105ea46c27d83df2449404297fe74709eceaa8be6a21bd9484cbffba22",
    "manifests/item308_j1_all_s_fixed_divisor_no_go_manifest.json":
        "1c4721f43b5bbdc0c68e4d9fd689562a32a4af4fbbab2a9e7075da96b151b4d5",
    "sources/item329_j1_fixedM_cubic_cartier_report.md":
        "ba042d98a2c12cdeaf1858ea604488b0f5ae65406c1a8b450ccae90ed00f71e8",
    "scripts/item329_j1_fixedM_cubic_cartier_certificate.py":
        "01a779fb9420d39ce9728d6d46f008871dcc438b9b4aed2ba97cb2db5f294e40",
    "results/item329_j1_fixedM_cubic_cartier_certificate.json":
        "4c89f82c9f83dccfb3a32540532e5c986bff1043ec7bfd6f5584500bd7ecc7fc",
    "results/item329_j1_fixedM_cubic_cartier_certificate_replay.json":
        "4c89f82c9f83dccfb3a32540532e5c986bff1043ec7bfd6f5584500bd7ecc7fc",
    "results/item329_j1_fixedM_cubic_cartier_root_audit.json":
        "87ebfaad2321a5e3edb9d710bbccfe5a96884e48b3b939db1945d15cd68fa34d",
    "manifests/item329_j1_fixedM_cubic_cartier_manifest.json":
        "25f5eed9e5b3231e6c5ab4ad1c2fdfbe0fbe40c4b0cf0b4abc03c6a251d2ebf7",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pin_dependencies()
ITEM308 = load_module(
    "item332_pinned_item308",
    ROOT / "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py",
)
ITEM329 = load_module(
    "item332_pinned_item329",
    ROOT / "scripts/item329_j1_fixedM_cubic_cartier_certificate.py",
)


def polynomial_multiply(
    left: list[Fraction], right: list[Fraction], maximum: int
) -> list[Fraction]:
    output = [Fraction(0)] * min(maximum + 1, len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            if i + j > maximum:
                break
            output[i + j] += a_value * b_value
    return output


def rational_power_series(
    base: list[Fraction], exponent: Fraction, maximum: int
) -> list[Fraction]:
    """Coefficients of base(t)^exponent, for base(0)=1."""
    if base[0] != 1:
        raise ValueError("unit constant required")
    degree = len(base) - 1
    output = [Fraction(0)] * (maximum + 1)
    output[0] = Fraction(1)
    # base*F'=exponent*base'*F.
    for n in range(maximum):
        value = Fraction(0)
        for j in range(0, min(degree - 1, n) + 1):
            value += exponent * (j + 1) * base[j + 1] * output[n - j]
        for j in range(1, min(degree, n + 1) + 1):
            value -= base[j] * (n - j + 1) * output[n - j + 1]
        output[n + 1] = value / (n + 1)
    return output


def b_coefficient(h: int) -> Fraction:
    base = [Fraction(1), Fraction(-2), Fraction(3, 2), Fraction(-1, 2)]
    return rational_power_series(base, Fraction(4 * h, 3), 2 * h)[2 * h]


def item237_coefficient(h: int) -> Fraction:
    maximum = 2 * h
    one = rational_power_series(
        [Fraction(1), Fraction(1)], Fraction(-2 * h - 1), maximum
    )
    q_power = rational_power_series(
        [Fraction(1), Fraction(1), Fraction(1, 2)],
        Fraction(4 * h + 3, 3),
        maximum,
    )
    kernel = polynomial_multiply(one, q_power, maximum)
    phase = [
        Fraction(20 * h, 3) + 2,
        Fraction(14 * h, 3) - 5,
        Fraction(4 * h, 3) - 3,
    ]
    return polynomial_multiply(kernel, phase, maximum)[maximum]


def shifted_polynomial(coefficients: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * len(coefficients)
    for degree, coefficient in enumerate(coefficients):
        for power in range(degree + 1):
            output[power] += coefficient * Fraction(S.binomial(degree, power))
    return output


def j_coefficient(s: int) -> Fraction:
    maximum = 2 * s + 5
    mu = Fraction(-(2 * s + 1), 4)
    shifted_r = shifted_polynomial(
        [Fraction(value) for value in ITEM329.r_coefficients(mu)]
    )
    even = rational_power_series(
        [Fraction(1), Fraction(0), Fraction(1)],
        Fraction(-2 * s - 1),
        maximum,
    )
    half = rational_power_series(
        [Fraction(1), Fraction(1)],
        Fraction(3 * s, 1) + Fraction(1, 2),
        maximum,
    )
    return polynomial_multiply(
        polynomial_multiply(shifted_r, even, maximum), half, maximum
    )[maximum]


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def symbolic_audit() -> dict[str, Any]:
    y, t, x, h, s, M, p, T = S.symbols(
        "y t x h s M p T", integer=True
    )
    Q = 1 + y + y**2 / 2
    A = (20 + 14 * y + 4 * y**2) / 3
    B = 2 - 5 * y - 3 * y**2
    R = -S.Rational(1, 2) * (y + 1) * (y + 2) * (y**2 + 2 * y + 2)
    log_derivative = (
        -(2 * h + 1) * y / (1 + y)
        + S.Rational(4, 3) * h * y * S.diff(Q, y) / Q
    )
    target = S.expand(Q * (h * A + B) - S.Rational(2, 3) * (4 * h + 3))
    hermite = S.cancel(
        y * S.diff(R, y) + R * log_derivative - 2 * h * R - target
    )
    if hermite != 0:
        raise AssertionError("characteristic-zero Hermite collapse")

    P = 2 - 4 * t + 3 * t**2 - t**3
    F = P / 2
    change = S.cancel(
        F.subs(t, y / (1 + y)) - Q / (1 + y) ** 3
    )
    if change != 0:
        raise AssertionError("residue change of variable")

    substitutions = {M: 3 * h + 4 * s + 2, p: 4 * h + 6 * s + 3}
    index_identities = {
        "K_exponent": 4 * M - S.Rational(4, 3) * h - S.Rational(8, 3) * p,
        "K_prefactor":
            4 * M + 1 - (4 * h + 3) / 3 - S.Rational(8, 3) * p,
        "J_parameter":
            M + (2 * s + 1) / 4 - S.Rational(3, 4) * p,
        "J_even_exponent": 4 * M + 2 * s + 1 - 3 * p,
        "J_one_exponent":
            -6 * M - 1 - (3 * s + S.Rational(1, 2))
            + S.Rational(9, 2) * p,
    }
    if any(
        S.expand(value.subs(substitutions)) != 0
        for value in index_identities.values()
    ):
        raise AssertionError("actual-row exponent identities")

    mu = -(2 * s + 1) / 4
    R_M = (
        12 - (160 * M + 44) * t + (448 * M + 104) * t**2
        - (512 * M + 112) * t**3 + (276 * M + 60) * t**4
        - (60 * M + 12) * t**5
    )
    three_N = (
        12 + (80 * s - 4) * t - (224 * s + 8) * t**2
        + (256 * s + 16) * t**3 - (138 * s + 9) * t**4
        + (30 * s + 3) * t**5
    )
    if S.expand(R_M.subs(M, mu) - three_N) != 0:
        raise AssertionError("dual numerator collapse")

    logarithmic_derivative = S.cancel(
        S.Rational(2, 3) * T * S.diff(F, t).subs(t, T) / F.subs(t, T)
    )
    diagonal_readout = S.cancel(1 / (1 - logarithmic_derivative))
    curve = S.expand(4 * T**3 - x**3 * P.subs(t, T) ** 2)

    return {
        "P_t": str(P),
        "F_t": str(F),
        "b_h": "[t^(2h)]F(t)^(4h/3)",
        "exact_selected_identity":
            "c_h^*=2(4h+3)b_h/3 over Q for every h>=1",
        "Hermite_identity":
            "Q(hA+B)-2(4h+3)/3=H_h^(-1)(theta_y-2h)(R H_h), H_h=(1+y)^(-2h-1)Q^(4h/3)",
        "Hermite_R_y": str(S.factor(R)),
        "unit_exponent_lemma":
            "for G(0)=1, [t^n]G(t)^a=sum_(k=0..n) binom(a,k)[t^n](G-1)^k, so below p it depends only on a mod p",
        "actual_row_reductions": {
            "2^(-4M)K_(M,2h)": "b_h mod p",
            "4M-4h/3": "8p/3",
            "4M+1-(4h+3)/3": "8p/3",
            "J_(M,2s+5)": "j_s mod p",
            "M+(2s+1)/4": "3p/4",
        },
        "psi": "psi(t)=F(t)^(2/3), psi^3=F^2",
        "Lagrange_parameter": "T=x psi(T)",
        "fixed_degree_six_curve": str(curve),
        "full_diagonal_generating_function":
            "A(x)=sum_(n>=0)[t^n]psi(t)^n x^n=xT'(x)/T(x)=1/(1-T psi'(T)/psi(T))",
        "diagonal_readout_rational_in_T": str(diagonal_readout),
        "even_section":
            "B(z)=sum_(h>=0)b_h z^h=(A(sqrt(z))+A(-sqrt(z)))/2",
        "old_series_recovery":
            "sum_h c_h^* z^h=2B(z)+(8/3)z B'(z)",
        "dual_exact_identity":
            "at mu=-(2s+1)/4, R_mu=3N_s and j_s=-3A_s; hence X_s=-2^(2s)j_s/3",
    }


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        (1, 1, 13, (0, 7, 0, 7, 2)),
        (2, 1, 17, (9, 16, 9, 16, 10)),
        (8, 2, 47, (0, 6, 0, 6, 2)),
        (4, 4, 43, (42, 12, 42, 12, 0)),
        (2, 6, 47, (14, 0, 14, 0, 13)),
    ]
    output = []
    for h, s, prime, expected in declared:
        M = 3 * h + 4 * s + 2
        n = 2 * h
        m = 2 * s + 5
        b_value = b_coefficient(h)
        c_value = item237_coefficient(h)
        predicted_c = Fraction(2 * (4 * h + 3), 3) * b_value
        if c_value != predicted_c:
            raise AssertionError("declared exact selected identity")

        j_value = j_coefficient(s)
        A_s = ITEM308.alpha_coefficient(s)
        if j_value != -3 * A_s:
            raise AssertionError("declared exact dual identity")
        X_s = 2 ** (2 * s) * A_s

        K_value = ITEM329.k_coefficient(M, n)
        J_value = ITEM329.j_coefficient(M, m)
        L_value = 4 * J_value + 3 * (4 * M + 1) * K_value
        K_normalized = K_value % prime * pow(pow(2, 4 * M, prime), -1, prime) % prime
        J_mod = J_value % prime
        L_normalized = L_value % prime * pow(pow(2, 4 * M, prime), -1, prime) % prime
        actual = (
            fraction_mod(b_value, prime),
            fraction_mod(j_value, prime),
            K_normalized,
            J_mod,
            L_normalized,
        )
        if actual != expected:
            raise AssertionError(("declared carrier control", h, s, prime, actual))

        c_plus = fraction_mod(c_value, prime)
        c_minus = fraction_mod(2 * X_s - c_value, prime)
        dual_chart = fraction_mod(
            -3 * X_s + (4 * h + 3) * b_value, prime
        )
        if dual_chart != L_normalized:
            raise AssertionError("dual L chart")
        if c_minus != (-2 * L_normalized * pow(3, -1, prime)) % prime:
            raise AssertionError("opposite factor chart")

        output.append(
            {
                "classification": "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN",
                "M": M,
                "h": h,
                "s": s,
                "p": prime,
                "b_h": str(b_value),
                "j_s": str(j_value),
                "b_mod_p": actual[0],
                "j_s_mod_p": actual[1],
                "normalized_K_mod_p": actual[2],
                "J_carrier_mod_p": actual[3],
                "normalized_L_mod_p": actual[4],
                "c_plus_mod_p": c_plus,
                "c_minus_mod_p": c_minus,
                "full_collision_claimed": False,
            }
        )
    return output


def arithmetic_and_capacity() -> dict[str, Any]:
    return {
        "denominator_support": {
            "b_h":
                "b_h is in Z[1/6]: psi=F^(2/3) satisfies psi^3=F^2; recursively 3 psi_n lies in Z[1/6] once earlier coefficients do",
            "j_s":
                "j_s is in Z[1/6]: N_s is in (1/3)Z[t], the negative integral power is integral, and the half-binomial coefficients have only powers of 2 in their denominators",
            "actual_prime_unit": "every actual p>=13 is a unit for both denominator sets",
        },
        "integer_even_normalization": {
            "definition": "kappa_(M,h)=2^(h-4M)K_(M,2h)",
            "integrality":
                "kappa_(M,h)=[u^(2h)](1-2sqrt(2)u+3u^2-sqrt(2)u^3)^(4M) is an integer because every even-degree monomial has an even total sqrt(2) parity",
            "actual_row_reduction": "kappa_(M,h)=2^h b_h mod p",
        },
        "zero_chart": {
            "selected_original_gate":
                "ordinary collision => c_h^*=0 iff b_h=0 iff K_(M,2h)=0 mod p",
            "opposite_factor":
                "c_minus=2X_s-c_h^*=-(2/3)2^(-4M)L_(M,p) mod p",
            "full_container":
                "p|D_(s,epsilon) iff p|b_h or p|(-3X_s+(4h+3)b_h)",
        },
        "capacity_audit": {
            "raw_actual_prime_mass": "M/6+o(M)",
            "fixed_target_support":
                "any bounded set of fixed h- or fixed s-targets occupies O(1) rows and O(log M)=o(M) raw mass at fixed M",
            "growing_target_height":
                "log numerator(b_h)=O(h) and log numerator(j_s)=O(s), but summing componentwise bounds over Theta(M) moving rows gives O(M^2)",
            "new_independent_condition": 0,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
        },
        "scoped_no_go": {
            "closed_class":
                "normalize the Item-329 carriers by their constant powers, reduce their exponent parameters modulo the actual p below the target degree, and treat the resulting fixed algebraic coefficient as a new period",
            "reason":
                "that procedure recovers exactly c_h^* and 2X_s-c_h^*, the already known selected/opposite Item-308 rank-one factors",
            "not_closed":
                "sequence-specific prime-factor localization, monodromy, average gcd, or weighted zero density for the exact diagonal b_h",
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item332-j1-global-diagonal-collapse-certificate-v1",
        "item": 332,
        "date": "2026-09-01",
        "status":
            "PROVED_GLOBAL_DIAGONAL_AND_DUAL_COLLAPSE_SCOPED_FROBENIUS_FIXED_TARGET_NO_GO",
        "dependencies": DEPENDENCIES,
        "symbolic": symbolic_audit(),
        "arithmetic_and_capacity": arithmetic_and_capacity(),
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "exact characteristic-zero collapse c_h^*=2(4h+3)b_h/3",
                "actual-row normalized K carrier equals b_h modulo p",
                "fixed algebraic diagonal and degree-six Lagrange curve for b_h",
                "exact dual j_s=-3A_s identity and normalized L chart",
                "denominator support at 2 and 3 and integer even normalization",
                "scoped Frobenius/fixed-target no-go for claiming a new independent period",
            ],
            "EXACT_FINITE_ONLY": [
                "five preselected replay rows; no scan or asymptotic inference"
            ],
            "OPEN": [
                "weighted zero density for the exact diagonal numerator b_h on h=3M-2p",
                "sequence-specific factor localization, average gcd, or Frobenius non-concentration",
                "W_off(M)=o(M), W_D(M)=o(M), fixed-j1 closure, Route 1, and e+pi",
            ],
        },
        "canonical_files_modified": False,
        "prime_scans": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "item": 332,
                "selected_carrier": "OLD_RESIDUAL_DIAGONAL",
                "dual_carrier": "OLD_OPPOSITE_FACTOR",
                "new_codimension": 0,
                "weighted_density": "OPEN",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
