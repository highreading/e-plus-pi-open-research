#!/usr/bin/env python3
"""Portable exact checker for Item 258's beta second-jet orbit.

The algebraic identities use exact rational arithmetic.  Every bounded
enumeration is reported under EXACT_FINITE_ONLY and carries no density claim.
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
            r = numerator // 2
            if 2 * r != numerator:
                continue
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
    base = 2 * m + d + q
    return sum(
        (
            F(math.comb(m, k), (base + k) ** (jet + 1)) * c**k
            for k in range(m + 1)
        ),
        F(0),
    )


def second_jet_iteration(m: int, d: int, c: F) -> tuple[F, F, F, F, F, F]:
    """Return A,B,C,E,G,J for the value, first jet, and second jet.

    M_L=A*M_0+E
    N_L=B*M_0+A*N_0+G
    P_L=C*M_0+B*N_0+A*P_0+J
    """
    length = m + 1
    a = 2 * m + d
    b = 3 * m + d + 1
    endpoint = (1 + c) ** length
    A = F(1)
    B = F(0)
    C = F(0)
    E = F(0)
    G = F(0)
    J = F(0)
    for q in range(length):
        beta = b + q
        lam = -F(a + q, 1) / (c * beta)
        mu = endpoint / (c * beta)
        eta = F(length, 1) / (c * beta**2)
        nu = endpoint / (c * beta**2)
        theta = F(length, 1) / (c * beta**3)
        xi = endpoint / (c * beta**3)
        J = lam * J + eta * G + theta * E + xi
        C = lam * C + eta * B + theta * A
        G = lam * G + eta * E + nu
        B = lam * B + eta * A
        E = lam * E + mu
        A = lam * A
    return A, B, C, E, G, J


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
    first_jet_recurrences = 0
    second_jet_recurrences = 0
    full_iterations = 0
    closed_transfer_checks = 0
    digest_rows = []
    for m in range(0, 10):
        for d in range(3, 18, 2):
            for c in (F(-2), F(-1, 2), F(3, 2)):
                length = m + 1
                a = 2 * m + d
                b = 3 * m + d + 1
                endpoint = (1 + c) ** length
                for q in range(0, min(length, 5)):
                    M0 = moment(m, d, c, q, 0)
                    M1 = moment(m, d, c, q + 1, 0)
                    N0 = moment(m, d, c, q, 1)
                    N1 = moment(m, d, c, q + 1, 1)
                    P0 = moment(m, d, c, q, 2)
                    P1 = moment(m, d, c, q + 1, 2)
                    alpha = a + q
                    beta = b + q
                    assert alpha * M0 + c * beta * M1 == endpoint
                    assert alpha * N0 + c * beta * N1 == M0 + c * M1
                    assert alpha * P0 + c * beta * P1 == N0 + c * N1
                    value_recurrences += 1
                    first_jet_recurrences += 1
                    second_jet_recurrences += 1

                A, B, C, E, G, J = second_jet_iteration(m, d, c)
                M = moment(m, d, c)
                N = moment(m, d, c, 0, 1)
                P = moment(m, d, c, 0, 2)
                assert moment(m, d, c, length, 0) == A * M + E
                assert moment(m, d, c, length, 1) == B * M + A * N + G
                assert moment(m, d, c, length, 2) == C * M + B * N + A * P + J
                delta1 = sum(
                    (F(1, a + q) - F(1, b + q) for q in range(length)), F(0)
                )
                delta2 = sum(
                    (
                        F(1, (a + q) ** 2) - F(1, (b + q) ** 2)
                        for q in range(length)
                    ),
                    F(0),
                )
                assert B == -A * delta1
                assert C == A * (delta1 * delta1 - delta2) / 2
                assert B * B - 2 * A * C == A * A * delta2
                full_iterations += 1
                closed_transfer_checks += 1
            digest_rows.append((m, d, moment(m, d, F(-2), 0, 2).numerator))

    digest = hashlib.sha256(
        "".join(f"{m},{d},{value}\n" for m, d, value in digest_rows).encode("ascii")
    ).hexdigest()
    return {
        "value_recurrence_equalities": value_recurrences,
        "first_jet_recurrence_equalities": first_jet_recurrences,
        "second_jet_recurrence_equalities": second_jet_recurrences,
        "full_iteration_equalities": full_iterations,
        "closed_transfer_equalities": closed_transfer_checks,
        "row_digest_sha256": digest,
    }


def modular_row(p: int, r: int, s: int, m: int, d: int) -> dict[str, int | bool]:
    length = m + 1
    a = 2 * m + d
    b = 3 * m + d + 1
    c = F(-2)
    ci = 1 / c
    cmod = frac_mod(c, p)
    cimod = pow(cmod, -1, p)
    t = pow(cmod, m, p)
    ti = pow(cimod, m, p)

    X = moment(m, d, c)
    Y = moment(m, d, ci)
    U = moment(m, d, c, 0, 1)
    V = moment(m, d, ci, 0, 1)
    W = moment(m, d, c, 0, 2)
    Z = moment(m, d, ci, 0, 2)
    XL = moment(m, d, c, length, 0)
    YL = moment(m, d, ci, length, 0)
    UL = moment(m, d, c, length, 1)
    VL = moment(m, d, ci, length, 1)
    WL = moment(m, d, c, length, 2)
    ZL = moment(m, d, ci, length, 2)

    # Complementary-denominator reflection through the second jet.
    assert frac_mod(XL + c**m * (Y + p * V + p * p * Z), p**3) == 0
    assert frac_mod(YL + ci**m * (X + p * U + p * p * W), p**3) == 0
    assert frac_mod(UL - c**m * (V + 2 * p * Z), p**2) == 0
    assert frac_mod(VL - ci**m * (U + 2 * p * W), p**2) == 0
    assert frac_mod(WL + c**m * Z, p) == 0
    assert frac_mod(ZL + ci**m * W, p) == 0

    A, B, C, E, G, J = second_jet_iteration(m, d, c)
    Ai, Bi, Ci, Ei, Gi, Ji = second_jet_iteration(m, d, ci)
    assert XL == A * X + E
    assert UL == B * X + A * U + G
    assert WL == C * X + B * U + A * W + J
    assert YL == Ai * Y + Ei
    assert VL == Bi * Y + Ai * V + Gi
    assert ZL == Ci * Y + Bi * V + Ai * Z + Ji

    # Exact closed transfer and reciprocal scaling.
    delta1 = sum(
        (F(1, a + q) - F(1, b + q) for q in range(length)), F(0)
    )
    delta2 = sum(
        (
            F(1, (a + q) ** 2) - F(1, (b + q) ** 2)
            for q in range(length)
        ),
        F(0),
    )
    assert B == -A * delta1
    assert C == A * (delta1 * delta1 - delta2) / 2
    curvature = B * B - 2 * A * C
    assert curvature == A * A * delta2
    scale = c ** (2 * length)
    assert Ai == scale * A
    assert Bi == scale * B
    assert Ci == scale * C

    H1 = sum((F(1, a + q) for q in range(length)), F(0))
    H2 = sum((F(1, (a + q) ** 2) for q in range(length)), F(0))
    H3 = sum((F(1, (a + q) ** 3) for q in range(length)), F(0))
    A_expansion = c ** (-length) * (
        1 + p * H1 + F(p * p, 2) * (H2 + H1 * H1)
    )
    Ai_expansion = c**length * (
        1 + p * H1 + F(p * p, 2) * (H2 + H1 * H1)
    )
    assert frac_mod(A - A_expansion, p**3) == 0
    assert frac_mod(Ai - Ai_expansion, p**3) == 0
    determinant = A * Ai - 1
    second_hasse = H2 + 2 * H1 * H1
    assert frac_mod(
        determinant - 2 * p * H1 - p * p * second_hasse, p**3
    ) == 0
    assert frac_mod(delta2 + 2 * p * H3, p**2) == 0
    assert frac_mod(curvature + 2 * p * A * A * H3, p**2) == 0

    Am = frac_mod(A, p)
    Aim = frac_mod(Ai, p)
    Bm = frac_mod(B, p)
    Bim = frac_mod(Bi, p)
    Cm = frac_mod(C, p)
    Cim = frac_mod(Ci, p)
    matrix = [
        [Am, t, 0, 0, 0, 0],
        [ti, Aim, 0, 0, 0, 0],
        [Bm, 0, Am, (-t) % p, 0, 0],
        [0, Bim, (-ti) % p, Aim, 0, 0],
        [Cm, 0, Bm, 0, Am, t],
        [0, Cim, 0, Bim, ti, Aim],
    ]
    matrix_rank = rank_mod(matrix, p)
    assert matrix_rank == 3
    assert matrix[1] == [cmod * value % p for value in matrix[0]]
    beta_mod = frac_mod(c * B / A, p)
    gamma_mod = frac_mod(c * C / A, p)
    predicted_fourth = [
        (-cmod * matrix[2][j] + beta_mod * matrix[0][j]) % p
        for j in range(6)
    ]
    predicted_sixth = [
        (
            cmod * matrix[4][j]
            - beta_mod * matrix[2][j]
            + gamma_mod * matrix[0][j]
        )
        % p
        for j in range(6)
    ]
    assert matrix[3] == predicted_fourth
    assert matrix[5] == predicted_sixth

    # Affine endpoint compatibility at the same three levels.
    assert frac_mod(Ei - c * E, p) == 0
    assert frac_mod(Gi - (-c * G + c * B / A * E), p) == 0
    assert frac_mod(Ji - (c * J - c * B / A * G + c * C / A * E), p) == 0

    # The complete mixed-precision equations: values mod p^3, first jets
    # mod p^2, and second jets mod p.
    eq_m_c = A * X + c**m * Y + E + p * c**m * V + p * p * c**m * Z
    eq_m_i = Ai * Y + ci**m * X + Ei + p * ci**m * U + p * p * ci**m * W
    eq_n_c = B * X + A * U + G - c**m * V - 2 * p * c**m * Z
    eq_n_i = Bi * Y + Ai * V + Gi - ci**m * U - 2 * p * ci**m * W
    eq_p_c = C * X + B * U + A * W + J + c**m * Z
    eq_p_i = Ci * Y + Bi * V + Ai * Z + Ji + ci**m * W
    assert frac_mod(eq_m_c, p**3) == 0
    assert frac_mod(eq_m_i, p**3) == 0
    assert frac_mod(eq_n_c, p**2) == 0
    assert frac_mod(eq_n_i, p**2) == 0
    assert frac_mod(eq_p_c, p) == 0
    assert frac_mod(eq_p_i, p) == 0

    # Every denominator occurring in the orbit, reflection, and all jets is a unit.
    for q in range(length):
        assert 0 < b + q <= 4 * m + d + 1 < p
        for k in range(m + 1):
            assert 0 < a + q + k <= 4 * m + d < p
    for k in range(m + 1):
        assert 0 < a + length + k <= 4 * m + d + 1 < p
        assert 0 < p - (a + k) < p

    return {
        "p": p,
        "r": r,
        "s": s,
        "m": m,
        "d": d,
        "M_minus_2": frac_mod(X, p),
        "H1": frac_mod(H1, p),
        "H2": frac_mod(H2, p),
        "H3": frac_mod(H3, p),
        "second_determinant_Hasse": frac_mod(second_hasse, p),
        "curvature_over_p": frac_mod(curvature / p, p),
        "second_jet_matrix_rank": matrix_rank,
        "mod_p3_reflection_verified": True,
        "affine_endpoint_compatibility_verified": True,
    }


def p_valuation_of_numerator(value: F, p: int) -> int:
    numerator = abs(value.numerator)
    valuation = 0
    while numerator and numerator % p == 0:
        numerator //= p
        valuation += 1
    return valuation


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=601)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item258_beta_second_jet_certificate.json",
    )
    args = parser.parse_args()
    assert args.bound >= 157

    exact = exact_identity_audit()
    rows = [modular_row(*values) for values in actual_rows(args.bound)]
    second_hasse_zeros = [
        {key: row[key] for key in ("p", "r", "s", "m", "d", "H1", "H2")}
        for row in rows
        if row["second_determinant_Hasse"] == 0
    ]
    curvature_zeros = [
        {key: row[key] for key in ("p", "r", "s", "m", "d", "H1", "H2")}
        for row in rows
        if row["H3"] == 0
    ]
    target_zeros = [
        {
            key: row[key]
            for key in (
                "p",
                "r",
                "s",
                "m",
                "d",
                "H1",
                "second_determinant_Hasse",
                "H3",
            )
        }
        for row in rows
        if row["M_minus_2"] == 0
    ]
    target_and_second_hasse = [
        {key: row[key] for key in ("p", "r", "s", "m", "d")}
        for row in rows
        if row["M_minus_2"] == 0 and row["second_determinant_Hasse"] == 0
    ]
    target_and_curvature = [
        {key: row[key] for key in ("p", "r", "s", "m", "d")}
        for row in rows
        if row["M_minus_2"] == 0 and row["H3"] == 0
    ]

    determinant_witness = next(
        row for row in rows if row["p"] == 89 and row["r"] == 19 and row["s"] == 8
    )
    assert determinant_witness["H1"] == 44
    assert determinant_witness["H2"] == 44
    assert determinant_witness["second_determinant_Hasse"] == 0
    curvature_witness = next(
        row for row in rows if row["p"] == 157 and row["r"] == 59 and row["s"] == 6
    )
    assert curvature_witness["H3"] == 0
    A157, B157, C157, _, _, _ = second_jet_iteration(5, 63, F(-2))
    curvature157 = B157 * B157 - 2 * A157 * C157
    assert p_valuation_of_numerator(curvature157, 157) >= 2

    digest = hashlib.sha256(
        "".join(
            f"{row['p']},{row['r']},{row['s']},{row['m']},{row['d']},"
            f"{row['M_minus_2']},{row['H1']},{row['H2']},{row['H3']},"
            f"{row['second_determinant_Hasse']},{row['curvature_over_p']}\n"
            for row in rows
        ).encode("ascii")
    ).hexdigest()

    result = {
        "schema": "item258-beta-second-jet-certificate-v1",
        "imports_item_code": False,
        "theorems": {
            "mod_p3_value_reflection": (
                "M_L(c)=-c^m*(M_0(c^-1)+p*N_0(c^-1)+p^2*P_0(c^-1)) mod p^3"
            ),
            "mod_p2_first_jet_reflection": (
                "N_L(c)=c^m*(N_0(c^-1)+2p*P_0(c^-1)) mod p^2"
            ),
            "mod_p_second_jet_reflection": "P_L(c)=-c^m*P_0(c^-1) mod p",
            "second_jet_recurrence": (
                "(a+q)P_q+c(b+q)P_(q+1)=N_q+c*N_(q+1), with original endpoint retained"
            ),
            "homogeneous_transfer": "[[A,0,0],[B,A,0],[C,B,A]]",
            "closed_transfer": (
                "B=-A*Delta1, C=A*(Delta1^2-Delta2)/2, B^2-2AC=A^2*Delta2"
            ),
            "multiplier_mod_p3": (
                "A_c=c^(-L)*(1+pH1+p^2*(H2+H1^2)/2) mod p^3"
            ),
            "determinant_mod_p3": (
                "A_c*A_(c^-1)-1=2pH1+p^2*(H2+2H1^2) mod p^3"
            ),
            "phase_curvature": "B^2-2AC=-2p*A^2*H3 mod p^2",
            "augmented_matrix_rank": 3,
            "scoped_no_go": (
                "the reciprocal value plus first two denominator jets leaves M_0(c) arbitrary mod p"
            ),
            "universal_second_Hasse_unit_false": (
                "p=89,r=19,s=8 has H1=H2=44 and H2+2H1^2=0 mod 89"
            ),
            "universal_curvature_unit_false": (
                "p=157,r=59,s=6 has H3=0 and v_157(B^2-2AC)>=2"
            ),
        },
        "exact_identity_audit": exact,
        "unit_audit": {
            "all_value_and_jet_denominators_are_p_units": True,
            "orbit_bound": "a+q+k<=4m+d<p",
            "contiguous_bound": "b+q<=4m+d+1<p",
            "terminal_orbit_bound": "a+L+k<=4m+d+1<p",
            "reflected_denominators": "0<p-(a+k)<p",
            "value_endpoint_retained": "(1+c)^L",
            "first_and_second_endpoint_derivatives": 0,
        },
        "exact_counterexamples": {
            "second_determinant_Hasse_unit": {
                "row": determinant_witness,
                "interval": "37,...,44",
                "verification": "H1=44, H2=44, H2+2H1^2=44+2*44^2=44*89",
            },
            "curvature_over_p_unit": {
                "row": curvature_witness,
                "interval": "73,...,78",
                "inverse_cube_residues_mod_157": [92, 45, 108, 118, 116, 149],
                "sum": 628,
                "sum_over_157": 4,
                "curvature_numerator_v_157": p_valuation_of_numerator(
                    curvature157, 157
                ),
            },
        },
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.bound,
            "actual_rows": len(rows),
            "rank_three_rows": sum(row["second_jet_matrix_rank"] == 3 for row in rows),
            "second_determinant_Hasse_zero_count": len(second_hasse_zeros),
            "second_determinant_Hasse_zero_witnesses_first_12": second_hasse_zeros[:12],
            "curvature_lead_H3_zero_count": len(curvature_zeros),
            "curvature_lead_H3_zero_witnesses_first_12": curvature_zeros[:12],
            "target_value_zero_count": len(target_zeros),
            "target_value_zero_witnesses_first_12": target_zeros[:12],
            "joint_target_and_second_Hasse_zero_count": len(target_and_second_hasse),
            "joint_target_and_second_Hasse_witnesses_first_12": target_and_second_hasse[:12],
            "joint_target_and_curvature_zero_count": len(target_and_curvature),
            "joint_target_and_curvature_witnesses_first_12": target_and_curvature[:12],
            "first_rows": rows[:8],
            "row_digest_sha256": digest,
            "scope": "bounded exact replay only; no density or rate inference",
        },
        "OPEN": [
            "a third or higher jet genuinely independent of the reciprocal translation tower",
            "an all-prime or weighted theorem for the moving H1,H2,H3 intervals",
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
