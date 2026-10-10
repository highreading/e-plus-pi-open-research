#!/usr/bin/env python3
"""Deterministic exact replay for Item 363.

This checker reconstructs the fixed-M j=1 candidate support, removes the
compulsory first prime copy from Item 197's two fixed integers, clears the
Item 218 boundary coordinate y integrally, and verifies the exact CRT/gcd
formula for the joint Hasse--transverse gate on three predeclared fixed-M
controls.  It also verifies the gate resultants, the zero parameter
elimination ideal, and the finite-log Frobenius-defect identity.  It does
not scan for collisions or infer a density theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, gcd, prod
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item363_j1_joint_gate_crt_elimination_no_go_certificate.json"

# Frozen canonical predecessors make the replay path-stable.
DEPENDENCIES = {
    "sources/item197_common_log_locus_report.md":
        "2241656ac9c47e81b5026449a97c15bed7d35290bf2b6a91cdfed4bb3fe3683c",
    "scripts/item197_common_log_locus_certificate.py":
        "f85c36169c7eb0aee3fb73f8030d3ddb2296b00077370012be84479eea9aeeb9",
    "results/item197_common_log_locus_certificate.json":
        "01dc392a36fdb1d3005d18b104c55e1d3327bd9ae3e850f60cdf37cf578368e8",
    "results/item197_common_log_locus_certificate_replay.json":
        "01dc392a36fdb1d3005d18b104c55e1d3327bd9ae3e850f60cdf37cf578368e8",
    "sources/item218_j1_common_log_report.md":
        "2cabc5a705a974d6989718e24443b59c00715fd4e9aff288e0e17b297096d585",
    "scripts/item218_j1_common_log_certificate.py":
        "a238c5ca37263f2553da47bf3f21253aedf1c34f8c57458a4a274fc6cdc9029a",
    "results/item218_j1_common_log_certificate.json":
        "963bbb8a9758e55ede72f965693d21fc41aa70d44e2d981d5873685c3f08ea0f",
    "results/item218_j1_common_log_certificate.replay.json":
        "963bbb8a9758e55ede72f965693d21fc41aa70d44e2d981d5873685c3f08ea0f",
    "results/item218_j1_common_log_manifest.json":
        "e1c6c3d713670c819b5f27b1005db26f9b804ec8ee0766671928fc30c1ff6d8d",
    "sources/item264_j1_weighted_gate_report.md":
        "767005f8fad07b1fa633bfdd23436e36c7cdef346d032030390c437f207c9344",
    "scripts/item264_j1_weighted_gate_certificate.py":
        "a91d0905ecd73ba8406902a5c33ff5f6c21c5b67fce65a91b087ec6cf79bf733",
    "results/item264_j1_weighted_gate_certificate.json":
        "08010c633f3baf5e075e892c5c786a5d9f686bf26d940fb10da6b9f46de196d2",
    "results/item264_j1_weighted_gate_certificate_replay.json":
        "08010c633f3baf5e075e892c5c786a5d9f686bf26d940fb10da6b9f46de196d2",
    "results/item264_j1_weighted_gate_archive_replay.json":
        "08010c633f3baf5e075e892c5c786a5d9f686bf26d940fb10da6b9f46de196d2",
    "results/item264_j1_weighted_gate_ledger.json":
        "bd5db6e6a3215025e41507d45c8190398c74f00eabe07e250923618136113076",
    "manifests/item264_j1_weighted_gate_manifest.json":
        "9ff5fb02deb8e1acd8499f3481be306ca4539d0a7f0bc1ce45b55b449a25b18b",
    "sources/item360_j1_full_gate_transverse_period_report.md":
        "4468412fb8631924952dc7f70fc4e75433a7524954b89525de508e55feefc8c4",
    "scripts/item360_j1_full_gate_transverse_period_certificate.py":
        "84cabfb296a0892e620f252a1c413648c30664c8667245bd6fe444095bcad7e0",
    "results/item360_j1_full_gate_transverse_period_certificate.json":
        "a3f9e5b8e55b0a36bf7aef18fd1b81010eef0e8b9c8ade05995e2c4a25f9084d",
    "results/item360_j1_full_gate_transverse_period_certificate_replay.json":
        "a3f9e5b8e55b0a36bf7aef18fd1b81010eef0e8b9c8ade05995e2c4a25f9084d",
    "results/item360_j1_full_gate_transverse_period_root_replay.json":
        "a3f9e5b8e55b0a36bf7aef18fd1b81010eef0e8b9c8ade05995e2c4a25f9084d",
    "results/item360_j1_full_gate_transverse_period_ledger_delta.json":
        "20a7676bd6c14bc24d3cd9623e64ef7836afae8ad9bb1536f357fccfd050e11e",
    "results/item360_j1_full_gate_transverse_period_self_audit.json":
        "79677ecf502683a38de56c134a48bba21cf352ca3374e74253c9aa0f8cee95df",
    "results/item360_j1_full_gate_transverse_period_root_audit.json":
        "7a23e487b4d70d63f9785339344bdc00ae0e8350bcf1d8b1fcf6228c230e5138",
    "manifests/item360_j1_full_gate_transverse_period_manifest.json":
        "92f88a56162f3803b8699922da921333f5225c41a32d14c87641dd53c3f8b55b",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def candidate_primes(M: int) -> list[int]:
    """The exact Item 264 fixed-j1 prime interval."""
    lower = (4 * M + 3 + 2) // 3
    upper = (3 * M - 1) // 2
    return [p for p in range(lower, upper + 1) if is_prime(p)]


def actual_parameters(M: int, prime: int) -> tuple[int, int]:
    h = 3 * M - 2 * prime
    numerator = 3 * prime - 4 * M - 1
    if numerator % 2:
        raise AssertionError("nonintegral s")
    s = numerator // 2
    if h < 1 or s < 1 or prime != 4 * h + 6 * s + 3:
        raise AssertionError((M, prime, h, s))
    return h, s


def residue_numerator(M: int, nu: int) -> int:
    """Item 197's fixed integer C_nu(M), reconstructed independently."""
    index = 4 * M + nu
    extra = 1 + 3 * nu
    denominator_power = 4 * M + 1 + nu
    answer = 0
    for b in range(index // 2 + 1):
        remaining = index - 2 * b
        numerator_coefficient = 0
        for q in range(extra + 1):
            a = remaining - q
            if 0 <= a <= 6 * M:
                numerator_coefficient += (
                    (-1) ** a * comb(6 * M, a) * comb(extra, q)
                )
        answer += (
            (-1) ** b
            * comb(denominator_power + b - 1, b)
            * numerator_coefficient
        )
    return answer


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return output


def polynomial_power(base: list[int], exponent: int) -> list[int]:
    output = [1]
    while exponent:
        if exponent & 1:
            output = polynomial_multiply(output, base)
        base = polynomial_multiply(base, base)
        exponent //= 2
    return output


def kernel_coefficients(h: int, extra: int) -> list[int]:
    return polynomial_multiply(
        [(-1) ** k * comb(2 * h, k) for k in range(2 * h + 1)],
        [comb(extra, k) for k in range(extra + 1)],
    )


def normalized_sum_mod(
    kernel: list[int], a: int, q: int, odd: bool, prime: int
) -> int:
    maximum_t = (len(kernel) - 2) // 2 if odd else (len(kernel) - 1) // 2
    ratio = 1
    answer = 0
    for t in range(maximum_t + 1):
        degree = 2 * t + 1 if odd else 2 * t
        answer = (answer + ratio * kernel[degree]) % prime
        if t == maximum_t:
            break
        numerator = a + t + 1 if odd else a + t
        denominator = q + a + t + 2 if odd else q + a + t + 1
        if not 0 < denominator < prime:
            raise AssertionError((prime, a, q, t, denominator))
        ratio = -ratio * numerator * pow(denominator, -1, prime) % prime
    return answer


def gate_coordinates(prime: int, h: int, s: int) -> dict[str, int]:
    kernel_0 = kernel_coefficients(h, 1)
    kernel_1 = kernel_coefficients(h, 4)
    x = normalized_sum_mod(kernel_0, s, 2 * s, True, prime)
    y = normalized_sum_mod(kernel_0, h, 2 * s, True, prime)
    u = normalized_sum_mod(kernel_1, s, 2 * s - 1, False, prime)
    v = normalized_sum_mod(kernel_1, h, 2 * s - 1, True, prime)
    fac = [factorial(k) % prime for k in range(prime)]
    A = ((-1) ** s * fac[2 * s] * fac[s] * pow(fac[3 * s + 1], -1, prime)) % prime
    B = ((-1) ** h * fac[2 * s] * fac[h] * pow(fac[2 * s + h + 1], -1, prime)) % prime
    C = ((-1) ** (s - 1) * fac[2 * s - 1] * fac[s - 1] * pow(fac[3 * s - 1], -1, prime)) % prime
    D = ((-1) ** h * fac[2 * s - 1] * fac[h] * pow(fac[2 * s + h], -1, prime)) % prime
    q0 = (2 * A * x - B * y) % prime
    q1 = (2 * C * u - D * v) % prime
    H = (
        ((2 * s + h + 1) * x * v + 3 * (3 * s + 1) * u * y)
        * pow(2 * s, -1, prime)
    ) % prime
    return {"x": x, "y": y, "u": u, "v": v, "A": A, "B": B,
            "C": C, "D": D, "Q0": q0, "Q1": q1, "H": H}


def rising(start: int, length: int) -> int:
    return prod(range(start, start + length)) if length else 1


def cleared_y(h: int, s: int) -> tuple[int, int]:
    """Return (Y,D_y) with y=Y/D_y and D_y a p-unit on actual rows."""
    kernel = kernel_coefficients(h, 1)
    start = 2 * s + h + 2
    denominator = rising(start, h)
    numerator = 0
    for t in range(h + 1):
        numerator += (
            (-1) ** t
            * rising(h + 1, t)
            * rising(start + t, h - t)
            * kernel[2 * t + 1]
        )
    return numerator, denominator


def selected_hasse(h: int, s: int) -> int:
    r = 2 * s + 1
    n = 2 * h
    return sum(
        comb(r + k - 1, k) * comb(4 * r + n - 1, n - 4 * k)
        for k in range(n // 4 + 1)
    )


def crt(entries: list[tuple[int, int]]) -> tuple[int, int]:
    modulus = prod(prime for prime, _ in entries)
    if modulus == 1:
        return 0, 1
    value = 0
    for prime, residue in entries:
        cofactor = modulus // prime
        value += residue * cofactor * pow(cofactor, -1, prime)
    return value % modulus, modulus


def frobenius_log_q0(prime: int, h: int, s: int) -> int:
    p0 = polynomial_multiply(
        polynomial_multiply(
            polynomial_power([1, -1], 2 * h),
            [1, 1],
        ),
        polynomial_power([1, 0, 1], 2 * s),
    )
    T = 2 * h + 6 * s + 2
    L = 4 * h + 4 * s + 2
    if not (T < prime and L < prime):
        raise AssertionError("low-index condition")

    def coefficient(index: int) -> int:
        answer = 0
        for k in range(1, min(prime - 1, index // 2) + 1):
            degree = index - 2 * k
            if degree < len(p0):
                answer += (comb(prime, k) // prime) * p0[degree]
        return answer % prime

    return (2 * coefficient(T) - coefficient(L)) % prime


def symbolic_gate_no_go() -> dict[str, Any]:
    x, y, u, v, lam, alpha, beta = S.symbols(
        "x y u v lambda alpha beta"
    )
    f0 = 2 * x - lam * y
    f1 = 2 * alpha * u - beta * lam * v
    H = beta * x * v - alpha * u * y
    if S.expand(beta * v * f0 - y * f1 - 2 * H) != 0:
        raise AssertionError("syzygy")
    resultant_y = S.factor(S.resultant(f0, H, y))
    resultant_x = S.factor(S.resultant(f0, H, x))
    if S.expand(resultant_y - x * f1) != 0:
        raise AssertionError(resultant_y)
    if S.expand(resultant_x + y * f1) != 0:
        raise AssertionError(resultant_x)
    groebner_joint = S.groebner(
        [f0, H], x, y, u, v, lam, alpha, beta, order="lex"
    )
    eliminated = [
        polynomial.as_expr()
        for polynomial in groebner_joint.polys
        if not polynomial.as_expr().has(x, y, u, v)
    ]
    if eliminated:
        raise AssertionError(("unexpected parameter eliminant", eliminated))
    witness = {
        x: lam / 2,
        y: 1,
        u: beta * lam / (2 * alpha),
        v: 1,
    }
    if S.factor(f0.subs(witness)) != 0 or S.factor(f1.subs(witness)) != 0:
        raise AssertionError("dominant nonzero-chart witness")
    M, p = S.symbols("M p")
    h_phase = 3 * M - 2 * p
    twice_s_phase = 3 * p - 4 * M - 1
    if S.expand(h_phase - 3 * M + 2 * p) != 0:
        raise AssertionError("fixed-M h phase")
    if S.expand(twice_s_phase + 4 * M + 1 - 3 * p) != 0:
        raise AssertionError("fixed-M s phase")
    return {
        "syzygy": "beta*v*f0-y*f1=2H",
        "resultant_eliminate_y": "Res_y(f0,H)=x*f1",
        "resultant_eliminate_x": "Res_x(f0,H)=-y*f1",
        "joint_primary_decomposition": "<f0,H>=<f0,f1> intersect <x,y>",
        "parameter_elimination_ideal": "<f0,H> intersect Q[lambda,alpha,beta]=<0>",
        "nonzero_chart_projection": "dominant: y=v=1, x=lambda/2, u=beta*lambda/(2alpha)",
        "fixed_M_parameter_phase": "h=3M and 2s=-(4M+1) modulo p",
        "moving_prime_polynomial_collapse": "F_M(p)=F_M(0) modulo p",
        "conclusion": "gate-only resultants return the second gate times a boundary coordinate and force no parameter divisor",
    }


# Chosen before Item 363 computation: M=9 and 34 are Item 360 selected-zero
# separation rows; M=76 contains Item 218's opposite Q0-zero separation row
# p=109 and has four fixed-M candidate primes, so it tests the CRT formula.
DECLARED_M = [9, 34, 76]


def fixed_M_control(M: int) -> dict[str, Any]:
    primes = candidate_primes(M)
    P = prod(primes)
    C0 = residue_numerator(M, 0)
    C1 = residue_numerator(M, 1)
    if C0 % P or C1 % P:
        raise AssertionError(("compulsory product", M))
    C0_bar = C0 // P
    C1_bar = C1 // P
    rows = []
    y_entries = []
    direct_joint_primes = []
    direct_full_primes = []
    direct_boundary_primes = []
    for prime in primes:
        h, s = actual_parameters(M, prime)
        gate = gate_coordinates(prime, h, s)
        Y, D_y = cleared_y(h, s)
        if D_y % prime == 0:
            raise AssertionError("boundary denominator")
        if Y * pow(D_y, -1, prime) % prime != gate["y"]:
            raise AssertionError("integral y clearing")
        cofactor = P // prime
        unit = cofactor * pow(6, -1, prime) % prime
        if gate["Q0"] != unit * (C0_bar % prime) % prime:
            raise AssertionError("C0 de-overlap bridge")
        if gate["Q1"] != unit * (C1_bar % prime) % prime:
            raise AssertionError("C1 de-overlap bridge")
        if frobenius_log_q0(prime, h, s) != gate["Q0"]:
            raise AssertionError("Frobenius finite-log coordinate")
        for k in range(1, prime):
            if (comb(prime, k) // prime) % prime != (
                (-1) ** (k - 1) * pow(k, -1, prime)
            ) % prime:
                raise AssertionError("finite-log coefficient")
        hasse = selected_hasse(h, s) % prime
        if (hasse == 0) != (gate["H"] == 0):
            raise AssertionError("selected Hasse bridge")
        q0_zero = gate["Q0"] == 0
        q1_zero = gate["Q1"] == 0
        boundary_zero = Y % prime == 0
        joint = q0_zero and hasse == 0
        criterion = (
            C0_bar % prime == 0
            and (C1_bar * Y) % prime == 0
        )
        if joint != criterion:
            raise AssertionError("joint arithmetic criterion")
        if joint:
            direct_joint_primes.append(prime)
        if q0_zero and q1_zero:
            direct_full_primes.append(prime)
        if q0_zero and boundary_zero:
            direct_boundary_primes.append(prime)
        y_entries.append((prime, Y % prime))
        rows.append({
            "classification": "PREDECLARED EXACT CONTROL; NOT A COLLISION SCAN",
            "p": prime,
            "h": h,
            "s": s,
            "Q0": gate["Q0"],
            "Q1": gate["Q1"],
            "H": gate["H"],
            "selected_Hasse": hasse,
            "Y_mod_p": Y % prime,
            "C0_bar_mod_p": C0_bar % prime,
            "C1_bar_mod_p": C1_bar % prime,
            "joint_Hasse_transverse_zero": joint,
            "full_gate_zero": q0_zero and q1_zero,
            "boundary_zero": q0_zero and boundary_zero,
        })
    Z, modulus = crt(y_entries)
    if modulus != P:
        raise AssertionError("CRT modulus")
    joint_radical = gcd(P, gcd(abs(C0_bar), abs(C1_bar * Z)))
    full_radical = gcd(P, gcd(abs(C0_bar), abs(C1_bar)))
    boundary_radical = gcd(P, gcd(abs(C0_bar), abs(Z)))
    if joint_radical != prod(direct_joint_primes):
        raise AssertionError("joint radical formula")
    if full_radical != prod(direct_full_primes):
        raise AssertionError("full radical formula")
    if boundary_radical != prod(direct_boundary_primes):
        raise AssertionError("boundary radical formula")
    if joint_radical != full_radical * boundary_radical // gcd(full_radical, boundary_radical):
        raise AssertionError("union lcm")
    return {
        "classification": "PREDECLARED FIXED-M CONTROL; NOT ASYMPTOTIC EVIDENCE",
        "M": M,
        "candidate_primes": primes,
        "candidate_product_P": P,
        "C0_bar": C0_bar,
        "C1_bar": C1_bar,
        "CRT_boundary_carrier_Z": Z,
        "CRT_height_bound_verified": 0 <= Z < P,
        "joint_radical_direct": prod(direct_joint_primes),
        "joint_radical_gcd": joint_radical,
        "full_radical": full_radical,
        "boundary_radical": boundary_radical,
        "rows": rows,
    }


def crt_information_neutrality() -> dict[str, Any]:
    primes = candidate_primes(76)
    P = prod(primes)
    checks = 0
    for size in range(len(primes) + 1):
        for subset_tuple in combinations(primes, size):
            subset = set(subset_tuple)
            # Residue zero on the chosen subset and one elsewhere.
            Z, modulus = crt([(p, 0 if p in subset else 1) for p in primes])
            if modulus != P or gcd(P, Z) != prod(subset):
                raise AssertionError("arbitrary CRT zero pattern")
            checks += 1
    return {
        "theorem": "for any subset S of a squarefree candidate product P, CRT packs the exact zero pattern into one 0<=Z<P",
        "proof": "choose residues 0 on S and 1 off S; primewise gcd(P,Z)=product(S)",
        "declared_M76_subset_checks": checks,
        "meaning": "a linear-height CRT carrier alone gives no zero-density restriction",
    }


def build_certificate() -> dict[str, Any]:
    controls = [fixed_M_control(M) for M in DECLARED_M]
    return {
        "schema": "item363-j1-joint-gate-crt-elimination-no-go-certificate-v1",
        "item": 363,
        "date": "2026-09-01",
        "status": "PROVED_EXACT_FIXED_M_RADICAL_AND_GATE_ONLY_ELIMINATION_NO_GO",
        "scope_correction": {
            "classification": "RESEARCH-MANAGEMENT NOTE; NOT A THEOREM ISSUE",
            "canonical_family": "p=4h+6s+3, M=3h+4s+2",
            "fixed_M_parameters": "h=3M-2p, s=(3p-4M-1)/2",
            "excluded_notation": "p=6m+2d+1 belongs to the j2 chain and is not imported",
        },
        "dependencies": DEPENDENCIES,
        "symbolic_gate_no_go": symbolic_gate_no_go(),
        "fixed_M_arithmetic": {
            "candidate_product": "P_M=product of primes (4M+3)/3 <= p <= (3M-1)/2",
            "compulsory_de_overlap": "Cbar_nu(M)=C_nu(M)/P_M is integral",
            "quotient_bridge": "Q_nu(p)=((P_M/p)/6)*Cbar_nu(M) mod p",
            "boundary_integer": "Y_(h,s)=(2s+h+2)_h*y_(h,s), with p-unit denominator",
            "joint_primewise_criterion": "Q0=a=0 iff p|Cbar_0 and p|Cbar_1*Y_(h,s)",
            "CRT_carrier": "Z_M is the unique 0<=Z<P_M with Z=Y_(h_p,s_p) mod p",
            "exact_radical": "R_joint(M)=gcd(P_M,Cbar_0(M),Cbar_1(M)*Z_M)",
            "decomposition": "R_joint=lcm(R_full,R_boundary), R_full=gcd(P,Cbar_0,Cbar_1), R_boundary=gcd(P,Cbar_0,Z)",
        },
        "frobenius_form": {
            "finite_log": "L_p(w)=((1+w)^p-1-w^p)/p in Z[w]",
            "coefficient_congruence": "[w^k]L_p=(-1)^(k-1)/k mod p for 1<=k<p",
            "transverse_coordinate": "Q0=(2[z^T]-[z^L0])P0(z)L_p(z^2) mod p",
            "conclusion": "this is the original first Frobenius-defect coordinate, not a third condition",
        },
        "crt_information_neutrality": crt_information_neutrality(),
        "capacity": {
            "raw_log_mass": "log P_M=M/6+o(M)",
            "raw_ceiling_per_6M": "1/36",
            "CRT_height": "log max(1,Z_M)<=M/6+o(M)",
            "available_Cauchy_constant_for_C_nu": "H=6.327627545440858... per M before compulsory de-overlap",
            "height_route": "strictly weaker than raw support",
            "weighted_target": "log R_joint(M)=o(M)",
            "weighted_target_proved": False,
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "booking": 0,
            "route_1_status": "ACTIVE",
        },
        "declared_controls": controls,
        "classification": {
            "PROVED": [
                "exact compulsory-prime de-overlap and fixed-M quotient bridge",
                "integral p-unit clearing of the boundary coordinate y",
                "exact primewise and CRT/gcd radical formulations of the joint gate",
                "gate resultants equal the second gate times boundary coordinates",
                "zero gate-only parameter elimination ideal even on the nonzero chart",
                "finite-log Frobenius form of Q0",
                "CRT zero-pattern information-class no-go",
                "zero booking",
            ],
            "EXACT_FINITE_ONLY": [
                "three predeclared fixed-M controls (six total rows) and all 16 M=76 CRT subset patterns; no collision scan",
            ],
            "OPEN": [
                "sequence-specific structure or sublinear-height compression of Z_M",
                "weighted average gcd for (Cbar_0,Cbar_1*Z_M)",
                "log R_joint(M)=o(M), any fixed-j1 ceiling reduction, Route 1, and every conclusion about e+pi",
            ],
        },
        "canonical_files_modified": False,
        "prime_scans": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    pin_dependencies()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "item": 363,
        "exact_fixed_M_radical": True,
        "parameter_elimination_ideal": "zero",
        "weighted_target_proved": False,
        "booking": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
