#!/usr/bin/env python3
"""Exact replay for Item 329.

This checker proves the fixed-M Frobenius carrier, the Hermite collapse of
the actually selected j=1 factor to one coefficient of a pure cubic power,
the companion carrier for the opposite factor, and the exact product bridge
to the Item-308 container.  Finite rows are declared replay controls only.
No prime scan is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item329_j1_fixedM_cubic_cartier_certificate.json"

DEPENDENCIES = {
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
    "sources/item326_j1_selected_factor_step12_no_go_report.md":
        "12f42dff3d52ab5d257eac675d9cff6888925568d29ea4894cad5e37c0c31b37",
    "scripts/item326_j1_selected_factor_step12_no_go_certificate.py":
        "5293dcbeffdd3f69706a1b2ef164215d50b22a282f314b506754896c089e1e49",
    "results/item326_j1_selected_factor_step12_no_go_certificate.json":
        "9378b4078db1385f60a5128617f6e99c75cd282b6be3e5b0be95410da979450f",
    "results/item326_j1_selected_factor_step12_no_go_certificate_replay.json":
        "9378b4078db1385f60a5128617f6e99c75cd282b6be3e5b0be95410da979450f",
    "results/item326_j1_selected_factor_step12_no_go_ledger_delta.json":
        "2c8998fed0f0dd997c7a105431dfbd78d264eb79436009b45dcf95bacc56cc8a",
    "results/item326_j1_selected_factor_step12_no_go_root_audit.json":
        "e862c02a708e30df2b528a8d498c40d9c92944e53e1d5799113b5abebe816f20",
    "manifests/item326_j1_selected_factor_step12_no_go_manifest.json":
        "d3ee4d8afc71dbf4591a863b4d18877e497e2d6f7c56f8fc1e43fd8ea163bdd6",
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
    "item329_pinned_item308",
    ROOT / "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py",
)


def polynomial_multiply(
    left: list[int], right: list[int], maximum: int
) -> list[int]:
    output = [0] * min(maximum + 1, len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            if i + j > maximum:
                break
            output[i + j] += a_value * b_value
    return output


def polynomial_power(base: list[int], exponent: int, maximum: int) -> list[int]:
    answer = [1]
    power = base[: maximum + 1]
    remaining = exponent
    while remaining:
        if remaining & 1:
            answer = polynomial_multiply(answer, power, maximum)
        remaining //= 2
        if remaining:
            power = polynomial_multiply(power, power, maximum)
    return answer


def shifted_polynomial(coefficients: list[int]) -> list[int]:
    output = [0] * len(coefficients)
    for degree, coefficient in enumerate(coefficients):
        for power in range(degree + 1):
            output[power] += coefficient * math.comb(degree, power)
    return output


def r_coefficients(M: int) -> list[int]:
    return [
        12,
        -(160 * M + 44),
        448 * M + 104,
        -(512 * M + 112),
        276 * M + 60,
        -(60 * M + 12),
    ]


def k_coefficient(M: int, n: int) -> int:
    values = polynomial_power([2, -4, 3, -1], 4 * M, n)
    return values[n] if n < len(values) else 0


def c_coefficient(M: int, n: int) -> int:
    one = [(-1) ** k * math.comb(4 * M - 5, k)
           for k in range(min(4 * M - 5, n) + 1)]
    d_power = polynomial_power([2, -2, 1], 4 * M, n)
    values = polynomial_multiply(r_coefficients(M), one, n)
    values = polynomial_multiply(values, d_power, n)
    return values[n]


def hermite_auxiliary_coefficient(M: int, n: int) -> int:
    one = [(-1) ** k * math.comb(4 * M - 4, k)
           for k in range(min(4 * M - 4, n) + 1)]
    d_power = polynomial_power([2, -2, 1], 4 * M + 2, n)
    values = polynomial_multiply(one, d_power, n)
    return 2 * values[n]


def j_coefficient(M: int, m: int) -> int:
    r_shifted = shifted_polynomial(r_coefficients(M))
    even_power = [0] * (m + 1)
    for k in range(min(4 * M, m // 2) + 1):
        even_power[2 * k] = math.comb(4 * M, k)
    negative_power = [
        (-1) ** k * math.comb(6 * M + k, k) for k in range(m + 1)
    ]
    values = polynomial_multiply(r_shifted, even_power, m)
    values = polynomial_multiply(values, negative_power, m)
    return values[m]


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def symbolic_bridge_audit() -> dict[str, Any]:
    t, x, M, h, s, p = S.symbols("t x M h s p", integer=True)
    D = t**2 - 2 * t + 2
    P = S.expand((1 - t) * D)
    R = (
        12 - (160 * M + 44) * t + (448 * M + 104) * t**2
        - (512 * M + 112) * t**3 + (276 * M + 60) * t**4
        - (60 * M + 12) * t**5
    )
    substitutions = {M: 3 * h + 4 * s + 2, p: 4 * h + 6 * s + 3}
    identities = {
        "2s_plus_1": 2 * s + 1 - (3 * p - 4 * M),
        "2s_plus_6": 2 * s + 6 - (3 * p - 4 * M + 5),
        "2h": 2 * h - (6 * M - 4 * p),
        "2s_plus_5": 2 * s + 5 - (3 * p - 4 * M + 4),
        "2s": 2 * s - (3 * p - 4 * M - 1),
    }
    if any(S.expand(value.subs(substitutions)) != 0 for value in identities.values()):
        raise AssertionError("fixed-M identities")

    s_bar = -S.Rational(1, 2) * (4 * M + 1)
    three_n = (
        12 + (80 * s - 4) * t - (224 * s + 8) * t**2
        + (256 * s + 16) * t**3 - (138 * s + 9) * t**4
        + (30 * s + 3) * t**5
    )
    if S.expand(three_n.subs(s, s_bar) - R) != 0:
        raise AssertionError("fixed-M numerator")

    auxiliary = 2 * D**2 / (1 - t) ** 4
    logarithmic = 4 * M * S.diff(P, t) / P
    hermite = S.cancel(
        t * S.diff(auxiliary, t)
        + t * logarithmic * auxiliary
        - 6 * M * auxiliary
        + 12 * (4 * M + 1)
        - R / (1 - t) ** 5
    )
    if hermite != 0:
        raise AssertionError("Hermite collapse")

    n = S.symbols("n", integer=True)
    recurrence = [
        2 * (n + 1),
        16 * M - 4 * n,
        3 * n - 3 - 24 * M,
        -n + 2 + 12 * M,
    ]
    # Directly derive these four coefficients from P F'=4M P'F.
    p_coefficients = [2, -4, 3, -1]
    derivative_coefficients = [-4, 6, -3]
    derived = [
        p_coefficients[0] * (n + 1),
        p_coefficients[1] * n - 4 * M * derivative_coefficients[0],
        p_coefficients[2] * (n - 1) - 4 * M * derivative_coefficients[1],
        p_coefficients[3] * (n - 2) - 4 * M * derivative_coefficients[2],
    ]
    if any(S.expand(a - b) != 0 for a, b in zip(recurrence, derived)):
        raise AssertionError("cubic coefficient recurrence")

    reversed_p = S.expand(x**3 * P.subs(t, 1 / x))
    if reversed_p != 2 * x**3 - 4 * x**2 + 3 * x - 1:
        raise AssertionError("reversed cubic")

    return {
        "actual_index_identities": {
            "M": "3h+4s+2",
            "p": "4h+6s+3",
            "2s+1": "3p-4M",
            "2s+6": "3p-4M+5",
            "n=2h": "6M-4p",
            "m=2s+5": "3p-4M+4",
        },
        "D_t": str(D),
        "P_t": str(P),
        "R_M_t": str(S.expand(R)),
        "fixed_M_Frobenius_carrier":
            "c_h^*=C_(M,2h)/(3*2^(4M+1)) mod p, C_[M,n]=[t^n]R_M(t)(1-t)^(4M-5)D(t)^(4M)",
        "exact_Hermite_identity":
            "R_M/(1-t)^5*P^(4M)=(theta-6M)(2D^2/(1-t)^4*P^(4M))+12(4M+1)P^(4M)",
        "selected_factor_collapse":
            "c_plus=(4M+1)*2^(1-4M)*K_(M,2h) mod p, K_[M,n]=[t^n]P(t)^(4M)",
        "unit_audit":
            "4M+1=3p-2s is a p-unit because 0<2s<p; 2 and 3 are p-units for actual p>=13",
        "Frobenius_digit":
            "K_(M,2h)=8[t^(2h)]P(t)^(-2s-1) mod p because 4M=3p-2s-1 and 2h<p",
        "coefficient_recurrence_K_n":
            "2(n+1)K_(n+1)+(16M-4n)K_n+(3n-3-24M)K_(n-1)+(-n+2+12M)K_(n-2)=0",
        "K_initial": "K_0=2^(4M), K_n=0 for n<0",
        "fixed_rational_generating_function":
            "sum_(M,n)K_(M,n)z^M t^n=1/(1-z*P(t)^4)",
        "fixed_Laurent_Cartier_function":
            "Phi(z,u)=u^6/(u^6-z*(2u^3-4u^2+3u-1)^4)",
        "Cartier_readout":
            "K_(M,6M-4p)=[z^M u^(4p)]Phi=[z^M u^4]Lambda_p^(u)Phi",
    }


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        (1, 1, 13, (0, 3, 0, 2)),
        (2, 1, 17, (15, 16, 9, 10)),
        (8, 2, 47, (0, 30, 0, 24)),
        (4, 4, 43, (16, 0, 2, 0)),
        (2, 6, 47, (40, 7, 8, 41)),
    ]
    output = []
    for h, s, prime, expected in declared:
        M = 3 * h + 4 * s + 2
        n = 2 * h
        m = 2 * s + 5
        parity = h % 2
        alpha = ITEM308.alpha_coefficient(s)
        beta_real, beta_imaginary = ITEM308.beta_coefficient(s)
        delta = ITEM308.delta(s, parity)
        X = 2 ** (2 * s) * alpha
        Y = (
            delta * 2 ** (5 * s + 2) * beta_real
            if parity == 0
            else -delta * 2 ** (5 * s + 2) * beta_imaginary
        )
        w = (-1) ** (h // 2) * 2**h
        c_plus = (fraction_mod(X, prime) + fraction_mod(Y, prime) * w) % prime
        c_minus = (fraction_mod(X, prime) - fraction_mod(Y, prime) * w) % prime

        K_value = k_coefficient(M, n)
        C_value = c_coefficient(M, n)
        auxiliary_value = hermite_auxiliary_coefficient(M, n)
        J_value = j_coefficient(M, m)
        L_value = 4 * J_value + 3 * (4 * M + 1) * K_value

        if C_value != (n - 6 * M) * auxiliary_value + 12 * (4 * M + 1) * K_value:
            raise AssertionError("integer Hermite coefficient identity")
        predicted_plus = (
            (4 * M + 1) * pow(2, 1 - 4 * M, prime) * (K_value % prime)
        ) % prime
        predicted_minus = (
            -pow(2, 1 - 4 * M, prime) * pow(3, -1, prime) * (L_value % prime)
        ) % prime
        actual = (c_plus, c_minus, K_value % prime, L_value % prime)
        if actual != expected or predicted_plus != c_plus or predicted_minus != c_minus:
            raise AssertionError(("declared control", h, s, prime, actual))

        aggregate = (alpha, beta_real, beta_imaginary)
        integer_form = ITEM308.integer_form(s, parity, aggregate)
        d_zero = integer_form["D_s_epsilon"] % prime == 0
        carrier_zero = K_value % prime == 0 or L_value % prime == 0
        if d_zero != carrier_zero:
            raise AssertionError("container product bridge")

        output.append(
            {
                "classification": "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN",
                "M": M,
                "h": h,
                "s": s,
                "p": prime,
                "epsilon": parity,
                "c_plus_mod_p": c_plus,
                "c_minus_mod_p": c_minus,
                "K_mod_p": K_value % prime,
                "J_mod_p": J_value % prime,
                "L_mod_p": L_value % prime,
                "D_mod_p": integer_form["D_s_epsilon"] % prime,
                "full_collision_claimed": False,
            }
        )
    return output


def dual_carrier_audit() -> dict[str, Any]:
    return {
        "linear_forms": {
            "c_plus": "X_s+Y_(s,epsilon)w_h",
            "c_minus": "X_s-Y_(s,epsilon)w_h=2X_s-c_plus",
        },
        "X_fixed_M_carrier":
            "X_s=-2^(2-4M)J_(M,2s+5)/3 mod p",
        "J_definition":
            "J_(M,m)=[x^m]R_M(1+x)(1+x^2)^(4M)(1+x)^(-6M-1)",
        "L_definition":
            "L_(M,p)=4J_(M,2s+5)+3(4M+1)K_(M,2h)",
        "opposite_factor":
            "c_minus=-2^(1-4M)L_(M,p)/3 mod p",
        "container_product":
            "D_(s,epsilon)=Lambda_s^2*2^(3s+1)c_plus*c_minus mod p",
        "exact_zero_union":
            "p|D_(s,epsilon) iff p|K_(M,2h) or p|L_(M,p)",
        "original_gate":
            "ordinary collision implies c_plus=0 and hence p|K_(M,2h)",
        "fixed_rational_J_generating_function":
            "with Q=(1+x^2)^4/(1+x)^6 and R_M=R_0+MR_1, sum_M J_M(x)z^M=(1+x)^(-1)(R_0(1+x)/(1-zQ)+R_1(1+x)zQ/(1-zQ)^2)",
    }


def capacity_and_no_go() -> dict[str, Any]:
    return {
        "live_weighted_targets": {
            "W_K": "sum log p over actual rows with p|K_(M,2h_s)",
            "W_L": "sum log p over actual rows with p|L_(M,p_s)",
            "implications": [
                "W_off(M)<=W_K(M)",
                "W_D(M)<=W_K(M)+W_L(M)",
                "W_K=o(M) closes the original fixed-j1 gate",
                "W_K+W_L=o(M) closes the full Item-308 container envelope",
            ],
        },
        "exact_K_carrier_size": {
            "degree": "12M",
            "sign_pattern": "(-1)^n K_(M,n)>0 for every 0<=n<=12M",
            "reason": "P(-t)=2+4t+3t^2+t^3 has strictly positive coefficients",
            "l1_norm": "10^(4M) exactly",
            "per_coefficient_log_height": "at most 4M log 10",
        },
        "dual_height":
            "for tied m<=M on actual rows, log max(1,|J|,|L|)=O(M); direct products over O(M) rows give only O(M^2)",
        "comparison_family": {
            "definition":
                "tilde K_M(t)=sum_(j=0..12M)(-1)^j a_(M,j)t^j, where a_(M,6M-4p)=p for actual candidate primes p and a_(M,j)=1 otherwise",
            "properties": [
                "one shared primitive integer polynomial of degree 12M",
                "strict alternating nonzero coefficient signs",
                "log l1 norm=O(log M), stronger than the actual O(M) bound",
                "every candidate prime divides its tied coefficient",
                "retained weighted mass M/6+o(M), i.e. the full raw 1/36 per 6M ceiling",
            ],
            "scope":
                "shared carrier, degree, integrality, sign, and absolute/l1 height alone cannot prove any strict capacity reduction",
            "not_shared_with_comparison":
                "the specific cubic power, fixed rational Cartier function, and coefficient recurrence remain live arithmetic information",
        },
        "new_linear_log_rate": 0,
        "new_fixed_j1_capacity_reduction": 0,
        "retained_ceiling_per_6M": "1/36",
    }


def build_certificate() -> dict[str, Any]:
    symbolic = symbolic_bridge_audit()
    controls = direct_controls()
    dual = dual_carrier_audit()
    capacity = capacity_and_no_go()
    return {
        "schema": "item329-j1-fixedM-cubic-cartier-certificate-v1",
        "item": 329,
        "date": "2026-09-01",
        "status":
            "PROVED_FIXED_M_CUBIC_CARTIER_BRIDGE_AND_DUAL_CARRIER_SCOPED_SHARED_HEIGHT_NO_GO",
        "dependencies": DEPENDENCIES,
        "symbolic_bridge": symbolic,
        "dual_carrier": dual,
        "direct_controls": controls,
        "capacity": capacity,
        "classification": {
            "PROVED": [
                "fixed-M Frobenius carrier for the actual selected Item-308 digit",
                "exact Hermite collapse to one coefficient of P(t)^(4M)",
                "fixed rational Cartier readout and exact coefficient recurrence",
                "dual fixed-M carrier and exact zero-union for the full Item-308 container",
                "scoped shared-carrier/degree/sign/height information-class no-go",
            ],
            "SCOPED_NO_GO": [
                "shared polynomial carrier, degree O(M), integrality, alternating signs, and exp(O(M)) l1 height alone cannot reduce the raw fixed-j1 capacity"
            ],
            "EXACT_FINITE_ONLY": [
                "five preselected Item-308 replay rows; no scan or asymptotic inference"
            ],
            "OPEN": [
                "weighted zero density for the specific cubic Cartier coefficient K",
                "weighted zero density for the dual carrier L",
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
                "item": 329,
                "selected_factor": "PURE_CUBIC_CARTIER_COEFFICIENT",
                "full_container": "K_OR_DUAL_L",
                "weighted_density": "OPEN",
                "capacity_reduction": "ZERO",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
