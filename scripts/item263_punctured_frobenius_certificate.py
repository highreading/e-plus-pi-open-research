#!/usr/bin/env python3
"""Portable exact checker for Item 263.

This verifies the mod-p Cartier/Frobenius matrices on the odd part of
H^1(E minus D), E: Z^2=X^3-1/2 and D above X^3=1.  It also checks the
finite endpoint dictionaries and the phase-specific Item-251 period.
Every bounded prime scan is EXACT FINITE ONLY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray([1]) * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for d in range(2, math.isqrt(limit) + 1):
        if sieve[d]:
            sieve[d * d : limit + 1 : d] = bytes([0]) * (
                (limit - d * d) // d + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def inv(a: int, p: int) -> int:
    a %= p
    assert a
    return pow(a, -1, p)


def half_states(count: int, p: int) -> tuple[list[int], list[int]]:
    """h_j=(1/2)_j/(j!2^j), H_j=sum_(i<=j)h_i, modulo p."""
    h = [1]
    H = [1]
    for j in range(count):
        denominator = 4 * (j + 1)
        assert denominator < p or denominator % p
        h.append(h[-1] * (2 * j + 1) * inv(denominator, p) % p)
        H.append((H[-1] + h[-1]) % p)
    return h, H


def n_coefficients(n: int, p: int) -> list[int]:
    """Coefficients of (v-1/2)^n, independently generated."""
    coefficients = []
    minus_half = -inv(2, p) % p
    for k in range(n + 1):
        coefficients.append(math.comb(n, k) * pow(minus_half, n - k, p) % p)
    return coefficients


def quotient_by_v_minus_one(n_coeffs: list[int], p: int) -> tuple[list[int], int]:
    """Return Q and remainder in N(v)=(v-1)Q(v)+N(1)."""
    n = len(n_coeffs) - 1
    q_coeffs = [0] * n
    running = 0
    for k in range(n, 0, -1):
        running = (running + n_coeffs[k]) % p
        q_coeffs[k - 1] = running
    remainder = sum(n_coeffs) % p

    reconstructed = [0] * (n + 1)
    reconstructed[0] = (remainder - q_coeffs[0]) % p
    for k in range(1, n):
        reconstructed[k] = (q_coeffs[k - 1] - q_coeffs[k]) % p
    reconstructed[n] = q_coeffs[n - 1]
    assert reconstructed == n_coeffs
    return q_coeffs, remainder


def cartier_polynomial(poly: dict[int, int], p: int) -> dict[int, int]:
    """C(sum c_e X^e dX)=sum c_(pj+p-1) X^j dX over F_p."""
    out: dict[int, int] = {}
    for exponent, coefficient in poly.items():
        if (exponent + 1) % p == 0:
            output_exponent = (exponent + 1) // p - 1
            out[output_exponent] = coefficient % p
    return {e: c for e, c in out.items() if c}


def quotient_polynomial_in_x(q_coeffs: list[int], a: int, p: int) -> dict[int, int]:
    return {
        a + 3 * degree: coefficient
        for degree, coefficient in enumerate(q_coeffs)
        if coefficient % p
    }


def g_polynomial_in_x(n_coeffs: list[int], a: int, p: int) -> dict[int, int]:
    return {
        a + 3 * degree: coefficient
        for degree, coefficient in enumerate(n_coeffs)
        if coefficient % p
    }


def phase_coefficients(delta: int, phase: int, p: int) -> tuple[list[int], int]:
    assert phase in (1, 5)
    c = [1]
    for j in range(delta):
        if phase == 1:
            numerator, denominator = 6 * j + 1, 3 * j + 2
        else:
            numerator, denominator = 6 * j + 5, 3 * j + 4
        assert 0 < denominator < p
        c.append(c[-1] * numerator * inv(denominator, p) % p)
    return c, sum(c[:delta]) % p


def rising_ratio_sum(start: int, denominator_start: int, count: int, p: int) -> int:
    """sum 2^-k (start)_k/(denominator_start)_k, values scaled by 6.

    start and denominator_start represent six times the rational starts.
    This avoids a rational package and directly checks all denominators.
    """
    term = 1
    total = 0
    for k in range(1, count + 1):
        numerator = (start + 6 * (k - 1)) % p
        denominator = (denominator_start + 6 * (k - 1)) % p
        assert denominator
        term = term * numerator * inv(denominator, p) * inv(2, p) % p
        total = (total + term) % p
    return total


def direct_P(m: int, d: int, p: int) -> int:
    term = 1
    total = 0
    inv2 = inv(2, p)
    for k in range(1, d + 1):
        numerator = (2 * m + 2 * k - 1) % p
        denominator = (2 * k - 1) % p
        assert denominator
        term = term * numerator * inv(denominator, p) * inv2 % p
        total = (total + term) % p
    return total


def integer_period_A(s: int, p: int) -> int:
    return sum(
        math.comb(3 * s - 1, s + j) * math.comb(s + j - 1, j)
        for j in range(2 * s)
    ) % p


def p1_coordinates(p: int, q: int) -> tuple[int, int]:
    inv2 = inv(2, p)
    U = 0
    V = 0
    for x in range(1, p):
        if x == 1:
            continue
        F = pow((1 - x * inv2) % p, 3, p) * inv(x, p) % p
        weight = pow(F, q, p)
        U = (U + inv(x, p) * weight) % p
        V = (V + inv(1 - x, p) * weight) % p
    return U, V


def p1_lambda(poly_exponents: dict[int, int], p: int, q: int) -> int:
    total = 0
    for exponent, coefficient in poly_exponents.items():
        if exponent == -1:
            value_sum = p - 1
        else:
            value_sum = p - 1 if exponent % (p - 1) == 0 else 0
        total = (total + coefficient * value_sum) % p
    return total


def p1_endpoint_defect(p: int, q: int, j: int) -> int:
    inv6 = inv(6, p)
    poly = {
        j - 1: (6 * j + 1) * inv6 % p,
        j: -(3 * j + 2) * inv6 % p,
    }
    # Sum D(R_j)(x) F(x)^q on F_p^* minus {1}.
    inv2 = inv(2, p)
    total = 0
    for x in range(1, p):
        if x == 1:
            continue
        F = pow((1 - x * inv2) % p, 3, p) * inv(x, p) % p
        value = 0
        for exponent, coefficient in poly.items():
            value += coefficient * pow(x, exponent % (p - 1), p)
        total = (total + value * pow(F, q, p)) % p
    return total


def p5_coordinates(p: int, q: int) -> tuple[int, int]:
    inv2 = inv(2, p)
    U = 0
    V = 0
    for x in range(1, p):
        if x == 1:
            continue
        g = (pow(x, 3, p) - inv2) % p
        chi = legendre(g, p)
        U = (U + x * chi) % p
        denominator = (pow(x, 3, p) - 1) % p
        assert denominator  # cube map is bijective for p == 5 (mod 6)
        V = (V + x * inv(denominator, p) * chi) % p
    return U, V


def p5_endpoint_defect(p: int, j: int) -> int:
    inv2 = inv(2, p)
    total = 0
    for x in range(1, p):
        if x == 1:
            continue
        g = (pow(x, 3, p) - inv2) % p
        # L(X^-j)=(3/2-j)X^(2-j)+(j/2)X^(-j-1).
        value = (
            (3 * inv2 - j) * pow(x, (2 - j) % (p - 1), p)
            + j * inv2 * pow(x, (-j - 1) % (p - 1), p)
        ) % p
        total = (total + value * legendre(g, p)) % p
    return total


def run(limit: int) -> dict[str, Any]:
    assert limit >= 83
    prime_rows = []
    endpoint_checks_p1 = 0
    endpoint_checks_p5 = 0
    cutoff_checks = 0
    period_checks = 0
    coordinate_checks = 0
    lambda_zeros_p1 = []
    lambda_zeros_p5 = []
    ordinary_gap_zeros = []
    cutoff_zeros = {"p1": [], "p5": []}

    for p in primes_upto(limit):
        if p < 5 or p % 6 not in (1, 5):
            continue
        phase = p % 6
        q = (p - phase) // 6
        n = (p - 1) // 2
        eps = legendre(2, p) % p
        h, H = half_states(q + 1, p)
        n_coeffs = n_coefficients(n, p)
        q_coeffs, remainder = quotient_by_v_minus_one(n_coeffs, p)
        assert remainder == eps

        cartier_logs = {}
        for a in range(3):
            selected = cartier_polynomial(quotient_polynomial_in_x(q_coeffs, a, p), p)
            cartier_logs[str(a)] = selected

        eta_selected = cartier_polynomial(g_polynomial_in_x(n_coeffs, 0, p), p)
        xi_selected = cartier_polynomial(g_polynomial_in_x(n_coeffs, 1, p), p)

        if phase == 1:
            lam = (H[q] - h[q]) % p
            assert cartier_logs == {"0": ({0: lam} if lam else {}), "1": {}, "2": {}}
            assert eta_selected == {0: h[q]}
            assert xi_selected == {}
            if lam == 0:
                lambda_zeros_p1.append([p, q])
            if h[q] == eps:
                ordinary_gap_zeros.append([p, q, h[q], H[q], lam])

            U, V = p1_coordinates(p, q)
            assert U == (-h[q] * inv(5, p) - eps) % p
            assert V == (-H[q] + 2 * eps * inv(3, p)) % p
            assert lam == (-V + 5 * U + 17 * eps * inv(3, p)) % p
            coordinate_checks += 1

            for j in range(q):
                actual = p1_endpoint_defect(p, q, j)
                denominator = (2 * (3 * j - 1)) % p
                assert denominator
                expected = (
                    -3 * h[q - j + 1] * inv(denominator, p)
                    - eps * (3 * j - 1) * inv(6, p)
                ) % p
                assert actual == expected
                endpoint_checks_p1 += 1

            # On every actual p == 1 phase, at least one of j=0,1 is a
            # nonzero exact-differential endpoint.  Their scaled sum is eps.
            if q >= 3:
                d0 = p1_endpoint_defect(p, q, 0)
                d1 = p1_endpoint_defect(p, q, 1)
                assert (30 * d0 + 12 * d1) % p == eps
                assert d0 or d1
            deltas = range(3, q + 1, 2)
        else:
            lam = H[q]
            assert cartier_logs == {"0": {}, "1": ({0: lam} if lam else {}), "2": {}}
            assert eta_selected == {}
            assert xi_selected == ({0: (-h[q]) % p} if h[q] else {})
            assert h[q]  # all factors are p-units
            if lam == 0:
                lambda_zeros_p5.append([p, q, h[q]])

            U, V = p5_coordinates(p, q)
            assert U == (h[q] - eps) % p
            assert V == (-H[q] + 4 * eps * inv(3, p)) % p
            assert lam == (-V + 4 * eps * inv(3, p)) % p
            coordinate_checks += 1

            # j=1 is an all-prime nonzero exact-differential endpoint.
            assert p5_endpoint_defect(p, 1) == (-eps) % p
            endpoint_checks_p5 += 1
            for j in range(4, min(3 * q + 1, p - 1), 3):
                actual = p5_endpoint_defect(p, j)
                expected = eps * (j - 3) * inv(2, p) % p
                assert actual == expected
                endpoint_checks_p5 += 1
            deltas = range(1, q + 1, 2)

        # Residue character action e_k -> eps e_(k*p^-1 mod 3).
        permutation = [(k * pow(p, -1, 3)) % 3 for k in range(3)]
        assert permutation == ([0, 1, 2] if phase == 1 else [0, 2, 1])

        phase_rows = 0
        for delta in deltas:
            m = q - delta
            s = m + 1
            r = 3 * delta - (4 if phase == 1 else 2)
            assert p == 2 * r + 6 * s + 3
            c, K = phase_coefficients(delta, phase, p)
            assert h[m] == c[delta] * h[q] % p
            assert H[m] == (H[q] - K * h[q]) % p
            cutoff_checks += 1
            phase_rows += 1
            if H[m] == 0:
                cutoff_zeros["p1" if phase == 1 else "p5"].append(
                    [p, r, s, m, delta]
                )

            d = r + 2
            assert 2 * d - 1 < p
            P_direct = direct_P(m, d, p)
            start = (2 - 6 * delta) if phase == 1 else (-2 - 6 * delta)
            Pi = rising_ratio_sum(start, 3, d, p)
            assert P_direct == Pi
            D = (K + c[delta] * Pi) % p
            predicted_A = (
                pow(-1, m, p) * (eps * (H[q] - D * h[q]) - 1)
            ) % p
            assert predicted_A == integer_period_A(s, p)
            period_checks += 1

        prime_rows.append(
            {
                "p": p,
                "phase": phase,
                "q": q,
                "epsilon": eps if eps == 1 else -1,
                "h_q": h[q],
                "H_q": H[q],
                "lambda": lam,
                "actual_rows": phase_rows,
            }
        )

    assert [83, 13, 22] in lambda_zeros_p5
    assert any(row[:2] == [19, 3] for row in ordinary_gap_zeros)
    assert [43, 11, 3, 2, 5] in cutoff_zeros["p1"]
    assert [47, 7, 5, 4, 3] in cutoff_zeros["p5"]

    theorem = {
        "curve_and_divisor": "E: Z^2=X^3-1/2; D={(alpha,beta): alpha^3=1, beta^2=1/2}",
        "basis": "omega_a=X^a/(X^3-1)dX/Z (a=0,1,2), eta=dX/Z, xi=X dX/Z",
        "residues": "res_(alpha,beta)(omega_a)=alpha^(a-2)/(3 beta)",
        "residue_cartier": "C(e_k)=epsilon e_(k*p^(-1) mod 3)",
        "p1_matrix_columns": {
            "C(omega_0)": "epsilon*omega_0+(H_q-h_q)*eta",
            "C(omega_1)": "epsilon*omega_1",
            "C(omega_2)": "epsilon*omega_2",
            "C(eta)": "h_q*eta",
            "C(xi)": "0",
        },
        "p5_matrix_columns": {
            "C(omega_0)": "epsilon*omega_1",
            "C(omega_1)": "epsilon*omega_0+H_q*eta",
            "C(omega_2)": "epsilon*omega_2",
            "C(eta)": "0",
            "C(xi)": "-h_q*eta",
        },
        "endpoint_dictionary_p1": "U=-h_q/5-epsilon; V=-H_q+2epsilon/3; lambda=-V+5U+17epsilon/3",
        "endpoint_dictionary_p5": "U=h_q-epsilon; V=-H_q+4epsilon/3; lambda=-V+4epsilon/3",
        "cutoff": "H_(q-delta)=H_q-K_delta*h_q",
        "item251": "A_s=(-1)^m{epsilon[H_q-D_r*h_q]-1}, D_r=K_delta+c_delta*Pi_r",
        "scope": "Cartier/residue plus exact endpoint augmentation recovers the same moving pair (H_q,h_q); it supplies no independent scalar or unit relation.",
    }
    scan = {
        "label": "EXACT FINITE ONLY",
        "prime_limit": limit,
        "prime_phase_count": len(prime_rows),
        "coordinate_checks": coordinate_checks,
        "endpoint_checks_p1": endpoint_checks_p1,
        "endpoint_checks_p5": endpoint_checks_p5,
        "cutoff_checks": cutoff_checks,
        "item251_period_checks": period_checks,
        "lambda_zeros_p1": lambda_zeros_p1,
        "lambda_zeros_p5": lambda_zeros_p5,
        "ordinary_gap_hq_equals_epsilon": ordinary_gap_zeros,
        "cutoff_zeros": cutoff_zeros,
    }
    payload: dict[str, Any] = {
        "schema": "item263-punctured-frobenius-v1",
        "theorem": theorem,
        "unit_audit": {
            "base": "p>=5, so 2 and 3 are units",
            "h_q": "0<=j<q gives 1<=2j+1<p and 1<=4(j+1)<p",
            "p1_endpoint": "0<=j<q gives |3j-1|<p",
            "fixed_tail": "d=r+2 and 2d-1<p on every actual row",
            "p1_actual": "q>=delta>=3 odd",
            "p5_actual": "q>=delta>=1 odd; X^3=1 has only X=1 in F_p",
        },
        "scan": scan,
        "booking": {
            "new_unconditional_route1_rate": 0,
            "new_j2_capacity_reduction": 0,
            "reason": "no all-prime exclusion or weighted zero theorem; actual cutoff zeros remain",
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=401)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item263_punctured_frobenius_certificate.json",
    )
    args = parser.parse_args()
    payload = run(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "payload_sha256": payload["payload_sha256"],
        "scan": payload["scan"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
