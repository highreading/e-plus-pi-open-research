#!/usr/bin/env python3
"""Exact certificate for Item 291's ordinary-j=2 connection plane.

The all-row theorem is the termwise identity lower_B_nu=2*d_nu,
the resulting H_nu=-11*d_nu simplification, and the exact row-rank
stratification.  The reconstructed order-three recurrence is deliberately
kept in a separately labelled bounded finite section.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item291_j2_connection_plane_certificate.json"
ITEM250_NAME = "item250_j2_ordinary_phase_certificate.py"
ITEM250_SHA256 = "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce"


def resolve(name: str) -> Path:
    for base in (HERE, HERE / "scripts", HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM250_PATH = resolve(ITEM250_NAME)
if sha256(ITEM250_PATH) != ITEM250_SHA256:
    raise RuntimeError("Item250 checker hash mismatch")
item250 = load("item291_item250", ITEM250_PATH)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def rising(x: F, count: int) -> F:
    out = F(1)
    for index in range(count):
        out *= x + index
    return out


def termwise_identity_replay(r_max: int) -> dict[str, Any]:
    rows = []
    terms = 0
    for r in range(1, r_max + 1, 2):
        if r % 3 == 0:
            continue
        data = item250.phase_data(r)
        q = data["qbar"]
        states = data["states"]
        lower0, lower1 = data["ba"]
        d0, d1 = data["x0"][2], data["x1"][2]
        if lower0 != 2 * d0 or lower1 != 2 * d1:
            raise AssertionError((r, "lower=2d"))

        # The odd homogeneous chain w_t=constant coordinate of J_(2t+1).
        beta = states[1][2]
        h = (r - 1) // 2
        ca0 = F((-1) ** r * math.factorial(r), 1) / rising(q + 1, r + 1)
        ca1 = F((-1) ** (r + 1) * math.factorial(r + 1), 1) / rising(q, r + 2)
        if ca1 != 2 * beta:
            raise AssertionError((r, "ca1=2beta"))
        a0 = states[3][2] / states[1][2]
        if ca0 != ca1 * (1 + a0):
            raise AssertionError((r, "ca0 base"))

        # nu=1: ca1*lower_weight_t=2*w_t term by term.
        weight = F(1)
        for t in range(h + 3):
            w = states[2 * t + 1][2]
            if ca1 * weight != 2 * w:
                raise AssertionError((r, 1, t))
            terms += 1
            if t < h + 2:
                weight *= F(r, 3) - t
                weight /= t - r - 1

        # nu=0: ca0*lower_weight_t=2*(w_t+w_(t+1)).
        weight = F(1)
        for t in range(h + 2):
            left = ca0 * weight
            right = 2 * (states[2 * t + 1][2] + states[2 * t + 3][2])
            if left != right:
                raise AssertionError((r, 0, t))
            terms += 1
            if t < h + 1:
                weight *= F(r, 3) - t
                weight /= t - r

        rows.append((r, lower0.numerator, lower0.denominator,
                     lower1.numerator, lower1.denominator))

    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return {
        "r_max_inclusive": r_max,
        "admissible_r_rows": len(rows),
        "term_equalities": terms,
        "row_digest_sha256": digest.hexdigest(),
        "role": "EXACT FINITE replay of the all-r termwise proof",
    }


def all_r_symbolic_certificate() -> dict[str, Any]:
    # These are the literal rational identities used in the proof.  Their
    # cleared numerators have displayed total degree at most two.  The grid
    # below is an independent replay; the report gives the direct algebraic
    # simplification and the complementary-factor bijection.
    def a(r: F, t: F) -> F:
        q = -(2 * r + 3) / 3
        return -(q + 1 + 2 * t) / (3 * q + 1 + 2 * t)

    def r1(r: F, t: F) -> F:
        return (r / 3 - t) / (t - r - 1)

    def r0(r: F, t: F) -> F:
        return (r / 3 - t) / (t - r)

    checks = 0
    for rv in (F(1), F(5), F(7), F(11)):
        for tv in (F(0), F(1), F(2), F(4)):
            if tv == rv or tv == rv + 1:
                continue
            av = a(rv, tv)
            if av != r1(rv, tv):
                raise AssertionError((rv, tv, "A=R1"))
            av1 = a(rv, tv + 1)
            if av * (1 + av1) / (1 + av) != r0(rv, tv):
                raise AssertionError((rv, tv, "S ratio"))
            checks += 2

    # Reversal of complementary factors in ca1=2*beta:
    # 3(r+1-i)-2r-3 = -(3i-r), and r+2 is odd for odd r.
    for rv in (1, 5, 7, 11, 101):
        if rv % 2 != 1:
            raise AssertionError(rv)
        for i in range(rv + 2):
            if 3 * (rv + 1 - i) - 2 * rv - 3 != -(3 * i - rv):
                raise AssertionError((rv, i, "factor reversal"))

    return {
        "phase_identity": "q=-(2r+3)/3 and n_a=r+q+1=r/3",
        "odd_chain_ratio": "A_t=-(q+1+2t)/(3q+1+2t)=(r/3-t)/(t-r-1)",
        "nu1_term_ratio": "lower_(t+1)/lower_t=A_t",
        "nu0_term_ratio": "(w_(t+1)+w_(t+2))/(w_t+w_(t+1))=(r/3-t)/(t-r)",
        "base_identities": "ca1=2*beta and ca0=ca1*(1+A_0)",
        "complementary_factor_map": "j=r+1-i sends 3j-2r-3 to -(3i-r); r+2 is odd",
        "cleared_degree_bound": 2,
        "grid_checks": checks,
        "classification": "SYMBOLIC FORMULAS RECORDED; bounded grid is an independent replay of the direct proof",
    }


# ---------------------------------------------------------------------------
# Independent finite modular replay for the experimentally reconstructed
# order-three operator.  No all-n conclusion is drawn from this section.


MOD = 1_000_000_007


def mi(x: int) -> int:
    return pow(x % MOD, MOD - 2, MOD)


def conv(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % MOD
    return out


def poly_pow(a: list[int], exponent: int) -> list[int]:
    out = [1]
    while exponent:
        if exponent & 1:
            out = conv(out, a)
        exponent >>= 1
        if exponent:
            a = conv(a, a)
    return out


def rise_mod(x: int, count: int) -> int:
    out = 1
    for index in range(count):
        out = out * (x + index) % MOD
    return out


def bsum_mod(coeff: list[int], parity: int, n0: int, d0: int) -> int:
    out = 0
    factor = 1
    t = 0
    for ell in range(parity, len(coeff), 2):
        if t:
            j = t - 1
            factor = factor * (n0 - j) % MOD * mi(1 - d0 + j) % MOD
        out = (out + coeff[ell] * factor) % MOD
        t += 1
    return out


def phase_mod(r: int) -> dict[str, int]:
    if r < 1 or r % 2 != 1 or r % 3 == 0:
        raise ValueError(r)
    q = -(2 * r + 3) * mi(3) % MOD
    k0 = conv(poly_pow([1, -1], r), [1, 1])
    k1 = conv(poly_pow([1, -1], r), poly_pow([1, 1], 4))
    kstar = 2 * r + 3
    alpha, beta = mi(q + kstar), -mi(q + kstar) % MOD
    for k in range(kstar - 2, 0, -2):
        alpha = (1 - (3 * q + k) * alpha) % MOD * mi(q + k) % MOD
        beta = -(3 * q + k) * beta % MOD * mi(q + k) % MOD
    states: list[tuple[int, int, int] | None] = [None] * (r + 5)
    states[0], states[1] = (1, 0, 0), (0, alpha, beta)
    for k in range(r + 3):
        u, v, w = states[k]  # type: ignore[misc]
        den = 3 * q + k
        states[k + 2] = (
            -(q + k) * u % MOD * mi(den) % MOD,
            (1 - (q + k) * v) % MOD * mi(den) % MOD,
            -(q + k) * w % MOD * mi(den) % MOD,
        )
    x0 = [0, 0, 0]
    for ell, coefficient in enumerate(k0):
        for coordinate in range(3):
            x0[coordinate] = (x0[coordinate] + coefficient * (
                states[ell + 1][coordinate] + states[ell + 3][coordinate]  # type: ignore[index]
            )) % MOD
    x1 = [0, 0, 0]
    for ell, coefficient in enumerate(k1):
        for coordinate in range(3):
            x1[coordinate] = (x1[coordinate] + coefficient * states[ell][coordinate]) % MOD  # type: ignore[index]
    dbar, rbar = r * mi(6) % MOD, -(r + 2) * mi(2) % MOD
    f0 = bsum_mod(k0, 1, rbar, dbar)
    rho = -dbar * mi(q) % MOD
    f1 = rho * bsum_mod(k1, 1, rbar, dbar + 1) % MOD
    b0, d0 = x0[1], x0[2]
    b1, d1 = x1[1], x1[2]
    return {
        "L": 9 * (f0 * b1 - f1 * b0) % MOD,
        "M": -11 * (f0 * d1 - f1 * d0) % MOD,
    }


def mul_poly(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def candidate_polynomials(phase: int) -> list[list[F]]:
    if phase == 5:
        rows = [
            (F(-27, 564080), [(1, 1), (1, 1), (1, 2), (1, 3), (2, 1),
              (3, 1), (3, 1), (3, 2), (3, 4), (3, 5), (3, 7), (6, 11)],
             [2350870988, 5183556876, 4509326169, 1934770806, 409656690, 34267860]),
            (F(-1, 8772572160), [(1, 2), (1, 3), (3, 4), (3, 5), (3, 7),
              (6, 1), (12, 11), (12, 17)],
             [417721024506116, 2610890880871852, 6946599948475155,
              10378928504066580, 9634829425335684, 5780876389931016,
              2247441103501056, 547053726757536, 75785154318720, 4559544380160]),
            (F(-1, 3683638140272640), [(1, 3), (3, 7), (6, 1), (6, 7),
              (12, 11), (12, 17), (12, 23), (12, 29)],
             [774269271695037200, 4490378931705322710, 11117723790981942441,
              15468367505613985368, 13379954498399498445, 7489451576199749634,
              2721623092177907502, 620827040491514532, 80846787850895160,
              4588037831607120]),
            (F(1, 2386997514896670720), [(3, 8), (6, 1), (6, 7), (6, 13),
              (6, 19), (6, 19), (12, 11), (12, 17), (12, 23), (12, 29),
              (12, 35), (12, 41)],
             [117258305, 501929496, 820275291, 638822646, 238317390, 34267860]),
        ]
    elif phase == 1:
        rows = [
            (F(-81, 564080), [(1, 1), (1, 1), (1, 2), (1, 3), (2, 5),
              (3, 4), (3, 5), (3, 5), (3, 7), (3, 8), (3, 11), (6, 7)],
             [2823139480, 4765016672, 3190940007, 1059830082, 174627630, 11422620]),
            (F(-1, 2924190720), [(1, 2), (1, 3), (3, 7), (3, 8), (3, 11),
              (6, 5), (12, 19), (12, 25)],
             [3739258081641544, 14996396031171744, 26297893955136521,
              26485787030581308, 16894685331622908, 7082476590214872,
              1952314877043648, 341397975513312, 34380806866560, 1519848126720]),
            (F(-1, 1227879380090880), [(1, 3), (3, 11), (6, 5), (6, 11),
              (12, 19), (12, 25), (12, 31), (12, 37)],
             [5733349927526586008, 21921540219246187478, 36638210004098965275,
              35161669971889956576, 21373720777662208155, 8541992877734690478,
              2246366823845371506, 375139504778445324, 36125004946845960,
              1529345943869040]),
            (F(1, 795665838298890240), [(3, 10), (6, 5), (6, 11), (6, 17),
              (6, 23), (6, 23), (12, 19), (12, 25), (12, 31), (12, 37),
              (12, 43), (12, 49)],
             [352437743, 921229484, 944989341, 475545762, 117514530, 11422620]),
        ]
    else:
        raise ValueError(phase)
    out = []
    for scalar, factors, core in rows:
        poly = [scalar * F(value) for value in core]
        for slope, intercept in factors:
            poly = mul_poly(poly, [F(intercept), F(slope)])
        if len(poly) != 18:
            raise AssertionError((phase, len(poly)))
        out.append(poly)
    return out


def fmod(value: F) -> int:
    if value.denominator % MOD == 0:
        raise AssertionError(("candidate denominator", value, MOD))
    return value.numerator % MOD * mi(value.denominator) % MOD


def poly_eval(poly: list[F], n: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * n + fmod(coefficient)) % MOD
    return out


def matrix_rank(matrix: list[list[int]]) -> int:
    matrix = [[value % MOD for value in row] for row in matrix]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(rank, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = mi(matrix[rank][column])
        matrix[rank] = [value * inverse % MOD for value in matrix[rank]]
        for row in range(rank + 1, len(matrix)):
            if matrix[row][column]:
                multiple = matrix[row][column]
                matrix[row] = [(x - multiple * y) % MOD
                               for x, y in zip(matrix[row], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def recurrence_matrix(sequence: list[int], order: int, degree: int) -> list[list[int]]:
    return [[sequence[n + shift] * pow(n, power, MOD) % MOD
             for shift in range(order + 1) for power in range(degree + 1)]
            for n in range(len(sequence) - order)]


def finite_recurrence_probe(term_count: int, primes: list[int]) -> dict[str, Any]:
    global MOD
    rows = []
    for prime in primes:
        MOD = prime
        for phase, start in ((5, 1), (1, 5)):
            values = [phase_mod(start + 6 * n) for n in range(term_count)]
            l_values = [row["L"] for row in values]
            b_values = [pow(16, n, MOD) * row["M"] % MOD
                        for n, row in enumerate(values)]
            polynomials = candidate_polynomials(phase)
            for name, sequence in (("L", l_values), ("16^n M", b_values)):
                bad = []
                for n in range(term_count - 3):
                    residual = sum(poly_eval(polynomials[j], n) * sequence[n + j]
                                   for j in range(4)) % MOD
                    if residual:
                        bad.append((n, residual))
                if bad:
                    raise AssertionError((prime, phase, name, bad[:3]))
                rank_2_17 = matrix_rank(recurrence_matrix(sequence, 2, 17))
                rank_3_16 = matrix_rank(recurrence_matrix(sequence, 3, 16))
                if rank_2_17 != 54 or rank_3_16 != 68:
                    raise AssertionError((prime, phase, name, rank_2_17, rank_3_16))
                rows.append((prime, phase, name, term_count - 3,
                             rank_2_17, rank_3_16))
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return {
        "primes": primes,
        "terms_per_phase": term_count,
        "candidate_order": 3,
        "candidate_coefficient_degree": 17,
        "candidate_verified_rows_per_sequence": term_count - 3,
        "candidate_conjugacy": "the same P_j(n) is tested on L_n and 16^n M_n; equivalently M has P_j/16^(3-j)",
        "full_rank_exclusions": [
            "no nonzero recurrence of order<=2 and coefficient degree<=17",
            "no nonzero recurrence of order<=3 and coefficient degree<=16",
        ],
        "rows": rows,
        "row_digest_sha256": digest.hexdigest(),
        "classification": "candidate agreement is EXACT FINITE ONLY; exclusions are exact for the stated bounded classes",
        "missing_for_all_n": "no symbolic telescoping, de-Rham, or annihilating-operator certificate is present",
    }


def rank_and_unit_replay(prime_max: int) -> dict[str, Any]:
    rows = 0
    rank_drops = 0
    common_collisions = 0
    digest = hashlib.sha256()
    cache: dict[int, dict[str, Any]] = {}
    for p, s, r in item250.actual_rows(prime_max):
        data = cache.get(r)
        if data is None:
            data = item250.phase_data(r)
            item250.reversal_certificate(r, data)
            cache[r] = data
        phase = item250.evaluate_phase_row(p, s, data)
        f0 = item250.fmod(data["st"][0], p)
        f1 = item250.fmod(data["st"][1], p)
        _, b0, d0 = data["x0"]
        _, b1, d1 = data["x1"]
        c = phase["c"]
        u0 = (9 * item250.fmod(b0, p) * c - 11 * item250.fmod(d0, p)) % p
        u1 = (9 * item250.fmod(b1, p) * c - 11 * item250.fmod(d1, p)) % p
        determinant = (f0 * u1 - f1 * u0) % p
        if determinant != phase["linear"]:
            raise AssertionError((p, s, r, "determinant"))
        # z1 is a unit by the all-row inequalities in the report; direct replay.
        kappa = item250.fmod(data["kappa"], p)
        beta_s = math.factorial(2 * s - 1) * math.factorial(s - 1)
        beta_s %= p
        beta_s = beta_s * pow(math.factorial(3 * s - 1) % p, -1, p) % p
        z1 = beta_s * (9 * kappa * pow(2, -1, p) % p) % p
        if z1 == 0:
            raise AssertionError((p, s, r, "z1"))
        row_rank = 2 if determinant else (0 if f0 == f1 == u0 == u1 == 0 else 1)
        if determinant == 0:
            rank_drops += 1
        if phase["g0"] == phase["g1"] == 0:
            common_collisions += 1
            if determinant:
                raise AssertionError((p, s, r, "collision necessity"))
        rows += 1
        digest.update(f"{p},{s},{r},{determinant},{row_rank},{phase['g0']},{phase['g1']}\n".encode("ascii"))
    return {
        "prime_max_inclusive": prime_max,
        "actual_rows": rows,
        "rank_drop_rows": rank_drops,
        "common_collision_rows": common_collisions,
        "row_digest_sha256": digest.hexdigest(),
        "role": "EXACT FINITE replay of the all-prime rank theorem",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=199)
    parser.add_argument("--phase-prime-max", type=int, default=401)
    parser.add_argument("--recurrence-terms", type=int, default=82)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.r_max < 31 or args.phase_prime_max < 101 or args.recurrence_terms < 75:
        raise ValueError("bounds too small")

    result = {
        "schema": "item291-j2-connection-plane-v1",
        "dependency": {ITEM250_NAME: ITEM250_SHA256},
        "all_r_termwise_proof": all_r_symbolic_certificate(),
        "termwise_replay": termwise_identity_replay(args.r_max),
        "exact_consequences": {
            "lower_tail": "lowerB_nu=2*d_nu",
            "H": "H_nu^flat=9*d_nu-10*lowerB_nu=-11*d_nu",
            "U": "U_nu=9*c*b_nu-11*d_nu (b_nu is distinct from lowerB_nu)",
            "determinant": "D=f0*U1-f1*U0=9*c*det(f,b)-11*det(f,d)",
            "row_minors": "minor(0,1)=-z1*D, minor(0,2)=-z2*D, minor(1,2)=0",
            "actual_rank": "because z1 is a p-unit, rank(R)=2 iff D!=0; on D=0 rank is 1 except f=U=0 gives rank 0",
            "collision": "G0=G1=0 implies D=0; D=0 alone is not sufficient for R*x_p=0",
        },
        "unit_and_boundary_audit": {
            "kappa_numerators": "raw rising numerators 6-r+6i are nonzero and lie between 6-r and 2r-3; 2r+3<p",
            "kappa_denominators": "constants 2,3 and factors through 2r+1 are p-units; Item250 audited the same denominators",
            "B_s": "factorial arguments are <=3s-1<p",
            "z1": "B_s*(9*kappa/2)*sigma_m*epsilon is a p-unit",
            "r1_endpoint": "h=0 has an empty rising product and is included",
            "warning": "lowerB_nu is not b_nu; no (18c-11) scalar factor exists",
        },
        "rank_replay": rank_and_unit_replay(args.phase_prime_max),
        "experimental_recurrence": finite_recurrence_probe(
            args.recurrence_terms, [1_000_000_007, 1_000_000_009]
        ),
        "admission": {
            "actual_family_implication": "collision forces the already known Item250 determinant D=0",
            "new_divisor": False,
            "all_prime_nonvanishing": False,
            "weighted_zero_density": False,
            "fixed_lisse_or_crystalline_realization": False,
            "raw_capacity": "2/35 per M = 1/105 per 6M",
            "new_capacity_reduction": 0,
            "booking": 0,
        },
        "strict_labels": {
            "PROVED": [
                "lowerB_nu=2*d_nu termwise and H_nu^flat=-11*d_nu",
                "D=9*c*det(f,b)-11*det(f,d)",
                "z1 is a p-unit and the complete actual-row rank stratification",
                "collision implies D=0, with every f=0/U=0 chart retained",
                "the two explicitly bounded recurrence-class exclusions",
            ],
            "EXACT_FINITE_ONLY": [
                "the displayed order-three degree-seventeen candidate and its L versus 16^n*M conjugacy",
                "bounded rational/modular row replays at the recorded bounds",
            ],
            "OPEN": [
                "an all-n symbolic telescoping or de-Rham certificate for the reconstructed operator",
                "a complete bounded-rank update for W=(f0,f1,U0,U1)",
                "any all-prime or weighted-density theorem for D=0",
                "any capacity reduction, Route-1 completion, or conclusion about e+pi",
            ],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
