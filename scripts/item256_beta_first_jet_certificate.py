#!/usr/bin/env python3
"""Portable exact checker for Item 256's beta first-jet orbit.

Uses only Python's standard library.  Exact identities are rational;
bounded modular counts are placed under EXACT_FINITE_ONLY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent


def primes_up_to(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(bound) + 1):
        if sieve[q]:
            start = q * q
            sieve[start : bound + 1 : q] = b"\x00" * (((bound - start) // q) + 1)
    return [q for q in range(2, bound + 1) if sieve[q]]


def actual_rows(bound: int):
    for p in primes_up_to(bound):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            numerator = p - 6 * s - 3
            if numerator <= 0:
                break
            if numerator % 2:
                continue
            r = numerator // 2
            if r >= 1 and r % 2 == 1 and r % 3 != 0:
                m = s - 1
                d = r + 4
                assert p == 6 * m + 2 * d + 1
                yield p, r, s, m, d


def frac_mod(value: F, modulus: int) -> int:
    denominator = value.denominator % modulus
    assert math.gcd(denominator, modulus) == 1
    return value.numerator % modulus * pow(denominator, -1, modulus) % modulus


def moment(m: int, d: int, c: F, q: int = 0, jet: int = 0) -> F:
    a = 2 * m + d + q
    power = jet + 1
    return sum(
        (F(math.comb(m, k), (a + k) ** power) * c**k for k in range(m + 1)),
        F(0),
    )


def jet_iteration(m: int, d: int, c: F) -> tuple[F, F, F, F]:
    """Return A,B,E,G with M_L=A M_0+E, N_L=B M_0+A N_0+G."""
    length = m + 1
    a = 2 * m + d
    b = 3 * m + d + 1
    endpoint = (1 + c) ** length
    A = F(1)
    B = F(0)
    E = F(0)
    G = F(0)
    for q in range(length):
        lam = -F(a + q, 1) / (c * (b + q))
        mu = endpoint / (c * (b + q))
        eta = F(length, 1) / (c * (b + q) ** 2)
        nu = endpoint / (c * (b + q) ** 2)
        G = lam * G + eta * E + nu
        B = lam * B + eta * A
        E = lam * E + mu
        A = lam * A
    return A, B, E, G


def rank_mod(matrix: list[list[int]], p: int) -> int:
    work = [[entry % p for entry in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(row, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, p)
        work[row] = [entry * inverse % p for entry in work[row]]
        for i in range(len(work)):
            if i != row and work[i][column]:
                factor = work[i][column]
                work[i] = [
                    (x - factor * y) % p for x, y in zip(work[i], work[row])
                ]
        row += 1
    return row


def exact_identity_audit() -> dict[str, object]:
    value_recurrences = 0
    jet_recurrences = 0
    iteration_checks = 0
    b_formula_checks = 0
    rows = []
    for m in range(0, 11):
        for d in range(3, 20, 2):
            for c in (F(-2), F(-1, 2), F(3, 2)):
                endpoint = (1 + c) ** (m + 1)
                for q in range(0, min(m + 1, 5)):
                    M0 = moment(m, d, c, q, 0)
                    M1 = moment(m, d, c, q + 1, 0)
                    N0 = moment(m, d, c, q, 1)
                    N1 = moment(m, d, c, q + 1, 1)
                    a_q = 2 * m + d + q
                    b_q = 3 * m + d + q + 1
                    assert a_q * M0 + c * b_q * M1 == endpoint
                    assert a_q * N0 + c * b_q * N1 == M0 + c * M1
                    value_recurrences += 1
                    jet_recurrences += 1

                A, B, E, G = jet_iteration(m, d, c)
                assert moment(m, d, c, m + 1, 0) == A * moment(m, d, c) + E
                assert moment(m, d, c, m + 1, 1) == (
                    B * moment(m, d, c) + A * moment(m, d, c, 0, 1) + G
                )
                length = m + 1
                a = 2 * m + d
                b = 3 * m + d + 1
                sigma = sum((F(1, (a + q) * (b + q)) for q in range(length)), F(0))
                assert B == -length * A * sigma
                iteration_checks += 1
                b_formula_checks += 1
            rows.append((m, d, moment(m, d, F(-2), 0, 1).numerator))

    digest = hashlib.sha256(
        "".join(f"{m},{d},{value}\n" for m, d, value in rows).encode("ascii")
    ).hexdigest()
    return {
        "value_recurrence_equalities": value_recurrences,
        "jet_recurrence_equalities": jet_recurrences,
        "full_iteration_equalities": iteration_checks,
        "B_formula_equalities": b_formula_checks,
        "row_digest_sha256": digest,
    }


def modular_row(p: int, r: int, s: int, m: int, d: int) -> dict[str, int | bool]:
    length = m + 1
    c = F(-2)
    ci = 1 / c
    cmod = frac_mod(c, p)
    cimod = pow(cmod, -1, p)

    X = moment(m, d, c)
    Y = moment(m, d, ci)
    U = moment(m, d, c, 0, 1)
    V = moment(m, d, ci, 0, 1)
    XL = moment(m, d, c, length)
    YL = moment(m, d, ci, length)
    UL = moment(m, d, c, length, 1)
    VL = moment(m, d, ci, length, 1)

    # Exact reflection expansions at the required precisions.
    assert frac_mod(XL + c**m * (Y + p * V), p * p) == 0
    assert frac_mod(YL + ci**m * (X + p * U), p * p) == 0
    assert frac_mod(UL - c**m * V, p) == 0
    assert frac_mod(VL - ci**m * U, p) == 0

    A, B, E, G = jet_iteration(m, d, c)
    Ai, Bi, Ei, Gi = jet_iteration(m, d, ci)
    assert XL == A * X + E
    assert UL == B * X + A * U + G
    assert YL == Ai * Y + Ei
    assert VL == Bi * Y + Ai * V + Gi

    harmonic = sum((F(1, 2 * m + d + t) for t in range(length)), F(0))
    expected_A = c ** (-length) * (1 + p * harmonic)
    expected_Ai = c**length * (1 + p * harmonic)
    assert frac_mod(A - expected_A, p * p) == 0
    assert frac_mod(Ai - expected_Ai, p * p) == 0
    determinant = A * Ai - 1
    assert frac_mod(determinant - 2 * p * harmonic, p * p) == 0

    # Exact and modular reciprocal relations for the jet transfer.
    assert Bi == c ** (2 * length) * B
    assert frac_mod(Ei - c * E, p) == 0
    beta = c * B / A
    assert frac_mod(Gi - (-c * G + beta * E), p) == 0

    Am = frac_mod(A, p)
    Aim = frac_mod(Ai, p)
    Bm = frac_mod(B, p)
    Bim = frac_mod(Bi, p)
    cm = pow(cmod, m, p)
    cim = pow(cimod, m, p)
    matrix = [
        [Am, cm, 0, 0],
        [cim, Aim, 0, 0],
        [Bm, 0, Am, (-cm) % p],
        [0, Bim, (-cim) % p, Aim],
    ]
    matrix_rank = rank_mod(matrix, p)
    assert matrix_rank == 2
    assert matrix[1] == [cmod * entry % p for entry in matrix[0]]
    beta_mod = frac_mod(beta, p)
    predicted_fourth = [
        (-cmod * matrix[2][j] + beta_mod * matrix[0][j]) % p for j in range(4)
    ]
    assert matrix[3] == predicted_fourth

    # Affine endpoint compatibility and full mod-p^2 value equations.
    assert frac_mod(Ei, p) == cmod * frac_mod(E, p) % p
    assert frac_mod(Gi, p) == (
        -cmod * frac_mod(G, p) + beta_mod * frac_mod(E, p)
    ) % p
    eq1 = A * X + c**m * Y + E + p * c**m * V
    eq2 = ci**m * X + Ai * Y + Ei + p * ci**m * U
    assert frac_mod(eq1, p * p) == 0
    assert frac_mod(eq2, p * p) == 0

    # Unit ranges for values, first jets, and the shifted reflection.
    for q in range(length):
        assert 0 < 3 * m + d + q + 1 <= 4 * m + d + 1 < p
        for k in range(m + 1):
            assert 0 < 2 * m + d + q + k <= 4 * m + d < p
    for k in range(m + 1):
        assert 0 < 2 * m + d + length + k <= 4 * m + d + 1 < p

    return {
        "p": p,
        "r": r,
        "s": s,
        "m": m,
        "d": d,
        "M_minus_2": frac_mod(X, p),
        "M_minus_half": frac_mod(Y, p),
        "N_minus_2": frac_mod(U, p),
        "N_minus_half": frac_mod(V, p),
        "harmonic_interval": frac_mod(harmonic, p),
        "determinant_over_p": frac_mod(determinant / p, p),
        "B_minus_2": Bm,
        "B_minus_half": Bim,
        "jet_matrix_rank": matrix_rank,
        "mod_p2_reflection_verified": True,
        "affine_endpoint_compatibility_verified": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=601)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item256_beta_first_jet_certificate.json",
    )
    args = parser.parse_args()
    assert args.bound >= 43

    exact = exact_identity_audit()
    rows = [modular_row(*values) for values in actual_rows(args.bound)]
    harmonic_zeros = [
        {key: row[key] for key in ("p", "r", "s", "m", "d", "M_minus_2")}
        for row in rows
        if row["harmonic_interval"] == 0
    ]
    value_zeros = [
        {key: row[key] for key in ("p", "r", "s", "m", "d", "harmonic_interval")}
        for row in rows
        if row["M_minus_2"] == 0
    ]
    joint_zeros = [
        {key: row[key] for key in ("p", "r", "s", "m", "d")}
        for row in rows
        if row["M_minus_2"] == 0 and row["harmonic_interval"] == 0
    ]

    witness = next(row for row in rows if row["p"] == 23 and row["r"] == 1 and row["s"] == 3)
    assert witness["harmonic_interval"] == witness["determinant_over_p"] == 0
    A, _, _, _ = jet_iteration(2, 5, F(-2))
    Ai, _, _, _ = jet_iteration(2, 5, F(-1, 2))
    exact_det = A * Ai - 1
    numerator = abs(exact_det.numerator)
    valuation = 0
    while numerator % 23 == 0:
        numerator //= 23
        valuation += 1
    assert valuation == 2

    digest = hashlib.sha256(
        "".join(
            f"{row['p']},{row['r']},{row['s']},{row['m']},{row['d']},"
            f"{row['M_minus_2']},{row['M_minus_half']},{row['N_minus_2']},"
            f"{row['N_minus_half']},{row['harmonic_interval']},"
            f"{row['determinant_over_p']},{row['B_minus_2']},"
            f"{row['B_minus_half']}\n"
            for row in rows
        ).encode("ascii")
    ).hexdigest()

    result = {
        "schema": "item256-beta-first-jet-certificate-v1",
        "imports_item_code": False,
        "theorems": {
            "mod_p2_reflection": (
                "M_L(c)=-c^m*(M_0(c^-1)+p*N_0(c^-1)) mod p^2"
            ),
            "mod_p_jet_reflection": "N_L(c)=c^m*N_0(c^-1) mod p",
            "jet_recurrence": (
                "(a+q)N_q+c(b+q)N_(q+1)=M_q+cM_(q+1), with exact value endpoint retained"
            ),
            "multiplier_mod_p2": "A_c=c^(-L)*(1+p*H_interval) mod p^2",
            "determinant_mod_p2": "A_c*A_(c^-1)-1=2p*H_interval mod p^2",
            "H_interval": "sum_(t=0)^m 1/(2m+d+t)",
            "jet_off_diagonal": "B_c=-L*A_c*sum_q 1/((a+q)(b+q))",
            "reciprocal_B_relation": "B_(c^-1)=c^(2L)*B_c exactly",
            "augmented_matrix_rank": 2,
            "affine_compatibilities": (
                "E_(c^-1)=cE_c and F_(c^-1)=-cF_c+(cB_c/A_c)E_c mod p"
            ),
            "scoped_no_go": (
                "the reciprocal value plus first squared-denominator jet supplies no independent "
                "condition on M_0(-2), H_m, or an affine gate target"
            ),
            "universal_Hasse_unit_false": "exact admissible witness p=23 has v_p(value determinant)=2",
        },
        "exact_identity_audit": exact,
        "unit_audit": {
            "all_value_and_jet_denominators_are_p_units": True,
            "orbit_bound": "a+q+k<=4m+d<p",
            "contiguous_bound": "b+q<=4m+d+1<p",
            "reflected_bound": "a+L+k<=4m+d+1<p",
            "value_endpoint_retained": "(1+c)^L",
            "jet_endpoint_derivative": 0,
        },
        "first_Hasse_unit_counterexample": {
            "row": witness,
            "harmonic_interval_exact": "1/9+1/10+1/11=299/990",
            "characteristic_zero_determinant": str(exact_det),
            "determinant_numerator_v_23": valuation,
        },
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.bound,
            "actual_rows": len(rows),
            "rank_two_augmented_rows": sum(row["jet_matrix_rank"] == 2 for row in rows),
            "harmonic_interval_zero_count": len(harmonic_zeros),
            "harmonic_interval_zero_witnesses_first_12": harmonic_zeros[:12],
            "target_value_zero_count": len(value_zeros),
            "target_value_zero_witnesses_first_12": value_zeros[:12],
            "joint_target_and_harmonic_zero_count": len(joint_zeros),
            "joint_witnesses_first_12": joint_zeros[:12],
            "first_rows": rows[:8],
            "row_digest_sha256": digest,
            "scope": "bounded exact replay only; no density or rate inference",
        },
        "OPEN": [
            "a second or higher jet genuinely independent of the reciprocal tower",
            "all-prime or weighted control of the moving harmonic interval",
            "an independent obstruction for the actual Item-251 collision",
            "any new divisibility exponent, capacity reduction, or e+pi conclusion",
        ],
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
