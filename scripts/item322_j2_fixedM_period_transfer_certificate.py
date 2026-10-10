#!/usr/bin/env python3
"""Deterministic certificate for Item 322.

The package retains the actual ordinary-j=2 incomplete-beta period.  It
checks the exact one-step period system, the fifteen-step transfer along a
fixed-M slice, the induced division-free transfer of the exterior residual,
and the fixed-M finite-field Mellin normal form.  Bounded row replays are
diagnostic only; the all-parameter statements are proved algebraically in
the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item322_j2_fixedM_period_transfer_certificate.json"

DEPENDENCIES = {
    "scripts/item250_j2_ordinary_phase_certificate.py":
        "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce",
    "results/item250_j2_ordinary_phase_certificate.json":
        "6f8d0165448dd8949436649e2824a14578c1bce08e8875a6fd88f770c72cb5e3",
    "scripts/item251_j2_exceptional_period_certificate.py":
        "a255ebeef0d73ef82bc6197a1f3f88c9522b6d8408f449971911702842c92f61",
    "results/item251_j2_exceptional_period_certificate.json":
        "343cf92daf3acfabee68d09885810f71cd3b582cea08801a548c9b293676d697",
    "scripts/item252_diagonal_modp_certificate.py":
        "1bd8826880993bfbaaae260768b8349c5d2731e2c9694fbdae4e8654d8d4fc65",
    "results/item252_diagonal_modp_certificate.json":
        "eee18f4fc6ace51b5c29faf84c7424f2013ccf0395033029fd395339fc06ab89",
    "scripts/item254_half_binomial_arithmetic_certificate.py":
        "51597cb653af504269341057e1ae02e917d60e94e00b274797fe1da94e0d8b81",
    "results/item254_half_binomial_arithmetic_certificate.json":
        "a81313ecfc726400bffc36c203b1d4b499cfc8b94ebce37277bc8d1a16fa3781",
    "scripts/item291_j2_connection_plane_certificate.py":
        "5c86001827b0012605563b04dafc5f157f27fddf2f1625254e9196bc0de8c2df",
    "results/item291_j2_connection_plane_certificate.json":
        "831cd4c74b10555c261eccebef7fd9c5a871bcef97a43d52e77c731b9b7188b5",
    "scripts/item315_j2_resultant_arithmetic_certificate.py":
        "42def823c42497fa9ce4c5513c348464511a56cc6ff12480bec60408c9733b81",
    "results/item315_j2_resultant_arithmetic_certificate.json":
        "09fdd67a6535a043bcbd1e2a46c4b14a633b9928a5f1c65618c34fab65cfabb6",
    "scripts/item318_j2_actual_period_plucker_certificate.py":
        "334bade7313a2fb750874dfd53216cd5f1028afbc837473cdd19b365ca820e82",
    "results/item318_j2_actual_period_plucker_certificate.json":
        "75e84016af2c7580f1954f795ed080d25083345578558aae49f6df4253891fd7",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for dependency, expected in DEPENDENCIES.items():
    actual = sha256(ROOT / dependency)
    if actual != expected:
        raise RuntimeError((dependency, expected, actual))


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


i250 = load("item322_i250", "scripts/item250_j2_ordinary_phase_certificate.py")
i251 = load("item322_i251", "scripts/item251_j2_exceptional_period_certificate.py")
i252 = load("item322_i252", "scripts/item252_diagonal_modp_certificate.py")
i318 = load("item322_i318", "scripts/item318_j2_actual_period_plucker_certificate.py")


def default_output() -> Path:
    return HERE / RESULT_NAME


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def rho(s: int) -> F:
    return F(2 * s * (2 * s + 1), 3 * (3 * s + 1) * (3 * s + 2))


def eta(s: int) -> F:
    return F(28 * s + 11, 6 * (3 * s + 1) * (3 * s + 2))


def tail_ratio(r: int, s: int) -> F:
    h = (r - 1) // 2
    return -F(
        (2 * s + 1) * (2 * s + 2) * (s + h + 1),
        (3 * s + h + 2) * (3 * s + h + 3) * (3 * s + h + 4),
    )


def period_state(r: int, s: int) -> dict[str, Any]:
    data = i250.phase_data(r)
    kappa, _ = i250.reversal_certificate(r, data)
    beta = i251.beta_fraction(s)
    a_value = i251.a_direct(s)
    e_value = beta * a_value / 2
    tail = i251.tail_fraction(r, s)
    z_value = 9 * kappa * e_value - tail
    coeff = i318.coefficients(data)
    residual = coeff["ell"] * z_value + 11 * coeff["C"]
    return {
        "data": data,
        "kappa": kappa,
        "beta": beta,
        "A": a_value,
        "e": e_value,
        "tail": tail,
        "Z": z_value,
        "coeff": coeff,
        "E": residual,
    }


def fifteen_step_e(s: int) -> tuple[F, F]:
    """e_(s+15)=a*e_s+b*4^s."""
    a_value = F(1)
    b_value = F(0)
    for j in range(15):
        b_value = -rho(s + j) * b_value + eta(s + j) * (4 ** j)
        a_value = -rho(s + j) * a_value
    return a_value, b_value


def fixed_m_tail_ratio(r: int, s: int) -> F:
    """f_(r-42,s+15)/f_(r,s), for r>=43."""
    h = (r - 1) // 2
    numerator = math.prod(range(2 * s + 1, 2 * s + 31))
    denominator = math.prod(range(s + h - 5, s + h + 1))
    denominator *= math.prod(range(3 * s + h + 2, 3 * s + h + 26))
    return F(numerator, denominator)


def fixed_m_transfer(r: int, s: int) -> dict[str, Any]:
    if r < 43 or r % 2 == 0:
        raise ValueError((r, s))
    old = period_state(r, s)
    new = period_state(r - 42, s + 15)
    a15, b15 = fifteen_step_e(s)
    kappa_ratio = new["kappa"] / old["kappa"]
    f_ratio = fixed_m_tail_ratio(r, s)
    lam = kappa_ratio * a15

    if new["e"] != a15 * old["e"] + b15 * (4 ** s):
        raise AssertionError((r, s, "e transfer"))
    if new["tail"] != f_ratio * old["tail"]:
        raise AssertionError((r, s, "tail transfer"))
    z_rebuilt = (
        lam * old["Z"]
        + (lam - f_ratio) * old["tail"]
        + 9 * new["kappa"] * b15 * (4 ** s)
    )
    if new["Z"] != z_rebuilt:
        raise AssertionError((r, s, "Z transfer"))

    ell = old["coeff"]["ell"]
    c_minor = old["coeff"]["C"]
    ell_new = new["coeff"]["ell"]
    c_minor_new = new["coeff"]["C"]
    lhs = ell * new["E"]
    rhs = (
        ell_new * lam * old["E"]
        + ell * ell_new * (lam - f_ratio) * old["tail"]
        + 9 * ell * ell_new * new["kappa"] * b15 * (4 ** s)
        + 11 * ell * c_minor_new
        - 11 * ell_new * lam * c_minor
    )
    if lhs != rhs:
        raise AssertionError((r, s, "division-free E transfer"))

    p = 2 * r + 6 * s + 3
    m_value = F(5 * r + 14 * s + 7, 2)
    p_new = 2 * (r - 42) + 6 * (s + 15) + 3
    m_new = F(5 * (r - 42) + 14 * (s + 15) + 7, 2)
    if m_value.denominator != 1 or m_value != m_new or p_new != p + 6:
        raise AssertionError((r, s, "fixed-M geometry"))

    determinant = lam * f_ratio * (4 ** 15)
    if determinant == 0:
        raise AssertionError((r, s, "singular transfer"))

    return {
        "r": r,
        "s": s,
        "p": p,
        "M": int(m_value),
        "r_next": r - 42,
        "s_next": s + 15,
        "p_next": p_new,
        "a15_num_bits": a15.numerator.bit_length(),
        "a15_den_bits": a15.denominator.bit_length(),
        "b15_num_bits": b15.numerator.bit_length(),
        "b15_den_bits": b15.denominator.bit_length(),
        "lambda_num_bits": lam.numerator.bit_length(),
        "lambda_den_bits": lam.denominator.bit_length(),
        "tail_ratio_num_bits": f_ratio.numerator.bit_length(),
        "tail_ratio_den_bits": f_ratio.denominator.bit_length(),
        "transfer_determinant_nonzero": True,
        "residual_identity": True,
    }


def primes_up_to(bound: int) -> list[int]:
    sieve = bytearray(b"\1") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(bound) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : bound + 1 : prime] = b"\0" * (((bound - start) // prime) + 1)
    return [value for value in range(2, bound + 1) if sieve[value]]


def actual_rows(bound: int) -> Iterable[tuple[int, int, int]]:
    for prime in primes_up_to(bound):
        if prime < 11:
            continue
        for s in range(1, (prime - 3) // 6 + 1):
            r = (prime - 6 * s - 3) // 2
            if r >= 1 and r % 2 == 1 and r % 3 != 0:
                yield prime, r, s


def legendre_two(prime: int) -> int:
    value = pow(2, (prime - 1) // 2, prime)
    if value == 1:
        return 1
    if value == prime - 1:
        return -1
    raise AssertionError((prime, value))


def conic_moment(prime: int, q_value: int) -> int:
    inverse_two = pow(2, -1, prime)
    total = 0
    for x in range(1, prime):
        if x == 1:
            continue
        radicand = x * (1 - x * inverse_two) % prime
        if radicand == 0:
            character = 0
        else:
            symbol = pow(radicand, (prime - 1) // 2, prime)
            character = 1 if symbol == 1 else -1
        total += pow(x, q_value, prime) * character * pow(1 - x, -1, prime)
    return total % prime


def frobenius_row(prime: int, r: int, s: int) -> dict[str, Any]:
    state = period_state(r, s)
    ell = state["coeff"]["ell"]
    c_minor = state["coeff"]["C"]
    if fmod(ell, prime) == 0:
        return {"p": prime, "r": r, "s": s, "ell_chart": False}

    m = s - 1
    d = r + 2
    epsilon = legendre_two(prime)
    h_prefix = i252.h_prefix(m)
    h_last = i252.h_value(m)
    boundary = i252.p_boundary(d, m)
    tau = i251.tau_fraction(r, s)
    theta = h_last * boundary + epsilon * (
        1
        + ((-1) ** m) * F(2, 9 * state["kappa"])
        * (tau - F(11) * c_minor / (ell * state["beta"]))
    )
    alpha = (
        ell * state["beta"] * F(9, 2) * state["kappa"]
        * ((-1) ** m) * epsilon
    )
    if fmod(state["E"], prime) != fmod(alpha * (h_prefix - theta), prime):
        raise AssertionError((prime, r, s, "affine prefix normal form"))
    if fmod(alpha, prime) == 0:
        raise AssertionError((prime, r, s, "chart multiplier"))

    n = (prime - 1) // 2
    q_value = n - m
    M = (5 * r + 14 * s + 7) // 2
    if q_value != r + 2 * s + 2 or q_value != 2 * (M - prime) + 1:
        raise AssertionError((prime, r, s, "q geometry"))
    if not (3 * q_value > prime and 2 * q_value <= prime - 1):
        raise AssertionError((prime, q_value, "linear q range"))

    moment = conic_moment(prime, q_value)
    h_mod = fmod(h_prefix, prime)
    if h_mod != (epsilon * (q_value + 1) - moment) % prime:
        raise AssertionError((prime, r, s, "conic Mellin form"))

    monomial_degree_lower = min(q_value, (prime - q_value) // 2)
    # ceil((p-1-q)/2) = floor((p-q)/2).
    weight_degree_lower = min(q_value, (prime - 1 - q_value) // 2)
    # ceil((p-2-q)/2) = floor((p-1-q)/2).
    if monomial_degree_lower * 4 < prime - 1:
        raise AssertionError((prime, q_value, monomial_degree_lower, "monomial degree lower bound"))
    if weight_degree_lower * 4 < prime - 3:
        raise AssertionError((prime, q_value, weight_degree_lower, "weight degree lower bound"))

    return {
        "p": prime,
        "r": r,
        "s": s,
        "M": M,
        "m": m,
        "q": q_value,
        "epsilon": epsilon,
        "ell_chart": True,
        "E_mod_p": fmod(state["E"], prime),
        "H_mod_p": h_mod,
        "Theta_mod_p": fmod(theta, prime),
        "conic_moment_mod_p": moment,
        "monomial_degree_lower_bound": monomial_degree_lower,
        "rational_weight_degree_lower_bound": weight_degree_lower,
    }


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def recurrence_replay(r_max: int, s_max: int) -> dict[str, Any]:
    one_step_rows = []
    fixed_m_rows = []
    for r in range(1, r_max + 1, 2):
        if r % 3 == 0:
            continue
        for s in range(1, s_max + 1):
            old = period_state(r, s)
            new = period_state(r, s + 1)
            q_value = tail_ratio(r, s)
            if new["e"] != -rho(s) * old["e"] + eta(s) * (4 ** s):
                raise AssertionError((r, s, "one-step e"))
            if new["tail"] != q_value * old["tail"]:
                raise AssertionError((r, s, "one-step tail"))
            rebuilt = (
                -rho(s) * old["Z"]
                - (rho(s) + q_value) * old["tail"]
                + 9 * old["kappa"] * eta(s) * (4 ** s)
            )
            if new["Z"] != rebuilt:
                raise AssertionError((r, s, "one-step Z"))
            one_step_rows.append((r, s, old["Z"].numerator.bit_length(), old["Z"].denominator.bit_length()))

            if r >= 43:
                transfer = fixed_m_transfer(r, s)
                fixed_m_rows.append((
                    r, s, transfer["M"], transfer["p"], transfer["p_next"],
                    transfer["lambda_num_bits"], transfer["lambda_den_bits"],
                ))

    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "r_max_inclusive": r_max,
        "s_max_inclusive": s_max,
        "one_step_rows": len(one_step_rows),
        "fixed_M_transfer_rows": len(fixed_m_rows),
        "one_step_digest_sha256": digest_rows(one_step_rows),
        "fixed_M_digest_sha256": digest_rows(fixed_m_rows),
        "sample_fixed_M_rows": fixed_m_rows[:8],
    }


def frobenius_replay(prime_max: int) -> dict[str, Any]:
    rows = []
    ell_zero = []
    for prime, r, s in actual_rows(prime_max):
        row = frobenius_row(prime, r, s)
        if not row["ell_chart"]:
            ell_zero.append((prime, r, s))
            continue
        rows.append((
            prime, r, s, row["M"], row["q"], row["epsilon"],
            row["E_mod_p"], row["H_mod_p"], row["Theta_mod_p"],
            row["conic_moment_mod_p"], row["rational_weight_degree_lower_bound"],
        ))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "prime_max_inclusive": prime_max,
        "ell_chart_rows": len(rows),
        "ell_zero_rows": len(ell_zero),
        "first_ell_zero_rows": ell_zero[:10],
        "row_digest_sha256": digest_rows(rows),
        "sample_rows": rows[:8],
    }


def theorem_record() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT; PROOFS IN COMPANION REPORT",
        "one_step_state": {
            "e": "e_(s+1)=-rho_s*e_s+eta_s*4^s",
            "tail": "f_(r,s+1)=q_(r,s)*f_(r,s)",
            "Z": "Z_(r,s+1)=-rho_s*Z_(r,s)-(rho_s+q_(r,s))*f_(r,s)+9*kappa_r*eta_s*4^s",
            "rho": "2*s*(2*s+1)/(3*(3*s+1)*(3*s+2))",
            "eta": "(28*s+11)/(6*(3*s+1)*(3*s+2))",
        },
        "fixed_M_geometry": {
            "M": "(5*r+14*s+7)/2",
            "step": "(r,s,p)->(r-42,s+15,p+6)",
            "state": "(Z,f,4^s)",
            "matrix": [
                ["Lambda", "Lambda-F", "9*kappa_(r-42)*b15"],
                ["0", "F", "0"],
                ["0", "0", "4^15"],
            ],
            "determinant": "Lambda*F*4^15, nonzero and a p-unit on every source row r>=43",
            "residual": "exact division-free transfer for E=ell*Z+11*C",
        },
        "frobenius_chart": {
            "condition": "on D=0 and ell!=0, collision iff H_m=Theta_(r,s)",
            "multiplier": "E_b=ell*B_s*(9*kappa_r/2)*(-1)^m*epsilon*(H_m-Theta)",
            "fixed_M_moment": "H_m=epsilon*(q+1)-sum_[x!=0,1] x^q*chi(x*(1-x/2))/(1-x)",
            "q": "n-m=r+2*s+2=2*(M-p)+1",
            "range": "p/3<q<=(p-1)/2",
        },
        "rational_weight_barrier": {
            "coefficient_field": "arbitrary reduced A/B in F_p(x)",
            "degree": "max(deg A,deg B)",
            "monomial_statement": (
                "if A/B equals x^q on F_p^* wherever B is nonzero and "
                "D=max(deg A,deg B), then D>=min(q,ceil((p-1-q)/2))>=(p-1)/4"
            ),
            "weight_statement": (
                "if A/B equals x^q/(1-x) on F_p^* minus {1} wherever B is "
                "nonzero, then D>=min(q,ceil((p-2-q)/2))>=(p-3)/4"
            ),
            "consequence": (
                "no uniformly bounded-degree pointwise rational-weight "
                "compression of the fixed conic moment exists"
            ),
            "scope": (
                "does not exclude identities after summation specialized to C_p, "
                "higher-rank Frobenius methods, or weighted zero-density theorems"
            ),
        },
        "moving_modulus_warning": (
            "the transfer reduced modulo p controls the next rational state modulo p, "
            "whereas the adjacent collision is tested modulo p+6; invertibility does "
            "not propagate collision zeros between the two primes"
        ),
        "adjacent_prime_capacity": {
            "classification": "PROVED BY THE CLASSICAL FIXED-TWO-TUPLE UPPER-BOUND SIEVE",
            "support": "p and p+6 both prime in an interval of length O(M)",
            "count": "O(M/(log M)^2)",
            "logarithmic_mass": "O(M/log M)=o(M)",
            "conclusion": (
                "even perfect adjacent-prime propagation is a zero-rate mechanism "
                "and cannot control isolated collision primes"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=89)
    parser.add_argument("--s-max", type=int, default=5)
    parser.add_argument("--prime-max", type=int, default=199)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.r_max < 47 or args.s_max < 2 or args.prime_max < 101:
        raise ValueError("replay bounds too small")

    output = {
        "schema": "item322-j2-fixedM-period-transfer-v1",
        "strict_labels": {
            "proved": [
                "the one-step triangular period system",
                "the exact fifteen-step fixed-M transfer",
                "the division-free fixed-M exterior-residual transfer",
                "the affine half-binomial normal form on the ell chart",
                "the fixed-M conic Mellin representation",
                "the linear rational-weight degree barrier",
                "zero logarithmic rate of adjacent-prime transfer pairs",
                "zero capacity booking",
            ],
            "exact_finite_only": [
                "all row counts, digests, samples, and bounded modular replays in this JSON"
            ],
            "open": [
                "weighted zero density for the actual transverse residual",
                "a summation-specific bounded-rank Frobenius compression",
                "arithmetic propagation across the changing prime moduli",
                "any reduction of the ordinary-j=2 ceiling",
            ],
        },
        "theorem": theorem_record(),
        "recurrence_replay": recurrence_replay(args.r_max, args.s_max),
        "frobenius_replay": frobenius_replay(args.prime_max),
        "capacity": {
            "new_booking": 0,
            "new_capacity_reduction": 0,
            "ordinary_j2_ceiling_per_6M": "1/105",
        },
        "dependency_sha256": DEPENDENCIES,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

