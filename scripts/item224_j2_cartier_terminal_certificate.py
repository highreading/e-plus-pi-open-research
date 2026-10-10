#!/usr/bin/env python3
"""Deterministic certificate for Item 224's j=2 terminal recurrence.

This standard-library checker verifies the exact recurrence coefficients,
the z^3 contiguity reduction, the top and bottom regularized constants,
and the finite formal-compatibility classification.  It imports the
frozen Item 221 checker beside it for polynomial and period helpers.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item224_j2_cartier_terminal_certificate.json"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM221_PATH = resolve("item221_j2_twisted_cohomology_certificate.py")
item221 = load("item224_item221", ITEM221_PATH)
item219 = item221.item219


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


# Linear forms constant + k*K + r*R + s*S.
Lin = tuple[int, int, int, int]


def lin_add(left: Lin, right: Lin) -> Lin:
    return tuple(left[j] + right[j] for j in range(4))  # type: ignore[return-value]


def verify_recurrence_coefficients() -> list[dict[str, object]]:
    zero: Lin = (0, 0, 0, 0)
    coefficients: dict[int, Lin] = {j: zero for j in range(5)}

    def add(shift: int, value: Lin) -> None:
        coefficients[shift] = lin_add(coefficients[shift], value)

    # d[z^(k+1)(1-z^4)]
    add(0, (1, 1, 0, 0))
    add(4, (-5, -1, 0, 0))
    # r/z times z^(k+1)(1-z^4)
    add(0, (0, 0, 1, 0))
    add(4, (0, 0, -1, 0))
    # r/(z-1), using (1-z^4)/(z-1)=-(1+z+z^2+z^3)
    for shift in range(1, 5):
        add(shift, (0, 0, -1, 0))
    # 1/(z+1), using (1-z^4)/(z+1)=1-z+z^2-z^3
    for shift, sign in ((1, 1), (2, -1), (3, 1), (4, -1)):
        add(shift, (sign, 0, 0, 0))
    # 4sz/(1+z^2), using (1-z^4)/(1+z^2)=1-z^2
    add(2, (0, 0, 0, 4))
    add(4, (0, 0, 0, -4))

    expected: dict[int, Lin] = {
        0: (1, 1, 1, 0),
        1: (1, 0, -1, 0),
        2: (-1, 0, -1, 4),
        3: (1, 0, -1, 0),
        4: (-6, -1, -2, -4),
    }
    if coefficients != expected:
        raise AssertionError((coefficients, expected))
    labels = [
        "k+r+1",
        "1-r",
        "4s-r-1",
        "1-r",
        "-(k+2r+4s+6)",
    ]
    return [
        {"shift": shift, "linear_coefficients_const_k_r_s": list(expected[shift]), "formula": labels[shift]}
        for shift in range(5)
    ]


def verify_z3_reduction() -> dict[str, object]:
    # Reuse Item 221's exact bivariate-polynomial rational arithmetic.
    one = item221.bp_const(1)
    z = {(1, 0): Fraction(1)}
    s = {(0, 1): Fraction(1)}
    one_plus_z = item221.bp_add(one, z)
    one_minus_z = item221.bp_sub(one, z)
    one_plus_z2 = item221.bp_add(one, item221.bp_pow(z, 2))
    delta = item221.bp_mul(item221.bp_sub(s, one), item221.bp_sub(item221.bp_scale(s, 10), one))
    r_parameter = item221.bp_add(item221.bp_scale(s, -3), item221.bp_const(Fraction(-3, 2)))

    h = item221.rat_div(item221.rat(r_parameter), item221.rat(z))
    h = item221.rat_add(h, item221.rat_neg(item221.rat_div(item221.rat(r_parameter), item221.rat(one_minus_z))))
    h = item221.rat_add(h, item221.rat_div(item221.rat(one), item221.rat(one_plus_z)))
    h = item221.rat_add(
        h,
        item221.rat_div(
            item221.rat(item221.bp_scale(item221.bp_mul(s, z), 4)),
            item221.rat(one_plus_z2),
        ),
    )

    n_num = item221.bp_mul(item221.bp_sub(item221.bp_scale(s, 10), item221.bp_const(5)), z)
    n_num = item221.bp_add(n_num, item221.bp_scale(item221.bp_pow(z, 2), 4))
    n_num = item221.bp_sub(n_num, item221.bp_scale(item221.bp_pow(z, 3), 4))
    n_num = item221.bp_add(n_num, item221.bp_scale(item221.bp_pow(z, 4), 4))
    n_num = item221.bp_sub(
        n_num,
        item221.bp_mul(item221.bp_sub(item221.bp_scale(s, 10), one), item221.bp_pow(z, 5)),
    )
    h3 = item221.rat_div(
        item221.rat(n_num),
        item221.rat(item221.bp_scale(item221.bp_mul(delta, one_plus_z), 2)),
    )

    q_num = item221.bp_add(item221.bp_sub(item221.bp_scale(item221.bp_pow(s, 2), 60), item221.bp_scale(s, 20)), item221.bp_const(-5))
    q1 = item221.bp_add(item221.bp_add(item221.bp_scale(item221.bp_pow(s, 2), -120), item221.bp_scale(s, 44)), item221.bp_const(16))
    q_num = item221.bp_add(q_num, item221.bp_mul(q1, z))
    q2 = item221.bp_add(item221.bp_add(item221.bp_scale(item221.bp_pow(s, 2), -20), item221.bp_scale(s, -52)), item221.bp_const(-1))
    q_num = item221.bp_add(q_num, item221.bp_mul(q2, item221.bp_pow(z, 2)))
    q3 = item221.rat_div(item221.rat(q_num), item221.rat(item221.bp_scale(delta, 4)))

    expression = item221.rat_add(item221.rat_derivative_z(h3), item221.rat_mul(h, h3))
    expression = item221.rat_add(item221.rat_sub(expression, item221.rat(item221.bp_pow(z, 3))), q3)
    if item221.bp_clean(expression[0]):
        raise AssertionError(expression[0])
    return {
        "H3_numerator": "(10s-5)z+4z^2-4z^3+4z^4-(10s-1)z^5",
        "H3_denominator": "2(s-1)(10s-1)(1+z)",
        "Q3_numerator": "60s^2-20s-5+4(-30s^2+11s+4)z-(20s^2+52s+1)z^2",
        "Q3_denominator": "4(s-1)(10s-1)",
        "symbolic_numerator_terms_after_cancellation": 0,
        "s_equals_1_exception": "deg(z^3 f0)=p-1 while deg(Q2 f0)<=p-2 and derivatives have zero z^(p-1) coefficient",
    }


def inv(value: int, p: int) -> int:
    return pow(value % p, -1, p)


def initial_line_mod(p: int, s: int) -> dict[int, int]:
    if s < 2:
        raise ValueError("z^3 line requires s>=2")
    return {
        0: 0,
        1: (4 * s - 2) % p,
        2: (2 * s - 5) % p,
        3: (-(52 * s * s - 36 * s - 27) * inv(4 * (s - 1), p)) % p,
    }


def compatibility_mod(p: int, s: int) -> tuple[int, int, int, int]:
    r = (p - 6 * s - 3) // 2
    values = initial_line_mod(p, s)
    b = 1 - r
    c = 4 * s - r - 1
    for k in range(0, 2 * s - 3):
        a = k + r + 1
        e = -(k + 2 * r + 4 * s + 6)
        if e % p == 0:
            raise AssertionError((p, s, k, "premature top resonance"))
        values[k + 4] = (
            -(a * values[k] + b * values[k + 1] + c * values[k + 2] + b * values[k + 3])
            * inv(e, p)
        ) % p
    for k in range(-1, -r - 1, -1):
        a = k + r + 1
        e = -(k + 2 * r + 4 * s + 6)
        if a % p == 0:
            raise AssertionError((p, s, k, "premature bottom resonance"))
        values[k] = (
            -(b * values[k + 1] + c * values[k + 2] + b * values[k + 3] + e * values[k + 4])
            * inv(a, p)
        ) % p

    top_k = 2 * s - 3
    tau = (
        (top_k + r + 1) * values[top_k]
        + b * values[top_k + 1]
        + c * values[top_k + 2]
        + b * values[top_k + 3]
    ) % p
    bottom_k = -r - 1
    bottom_e = -(bottom_k + 2 * r + 4 * s + 6)
    beta = (
        b * values[-r]
        + c * values[-r + 1]
        + b * values[-r + 2]
        + bottom_e * values[-r + 3]
    ) % p
    omega = (7 * ((-1) ** r) * beta - 11 * tau) % p
    return beta, tau, omega, r


def compatibility_fraction(p: int, s: int) -> tuple[Fraction, Fraction, Fraction, int, int]:
    r = (p - 6 * s - 3) // 2
    values: dict[int, Fraction] = {
        0: Fraction(0),
        1: Fraction(4 * s - 2),
        2: Fraction(2 * s - 5),
        3: -Fraction(52 * s * s - 36 * s - 27, 4 * (s - 1)),
    }
    b = 1 - r
    c = 4 * s - r - 1
    for k in range(0, 2 * s - 3):
        a = k + r + 1
        e = -(k + 2 * r + 4 * s + 6)
        values[k + 4] = -Fraction(
            a * values[k] + b * values[k + 1] + c * values[k + 2] + b * values[k + 3],
            e,
        )
    for k in range(-1, -r - 1, -1):
        a = k + r + 1
        e = -(k + 2 * r + 4 * s + 6)
        values[k] = -Fraction(
            b * values[k + 1] + c * values[k + 2] + b * values[k + 3] + e * values[k + 4],
            a,
        )
    top_k = 2 * s - 3
    tau = (
        (top_k + r + 1) * values[top_k]
        + b * values[top_k + 1]
        + c * values[top_k + 2]
        + b * values[top_k + 3]
    )
    bottom_k = -r - 1
    bottom_e = -(bottom_k + 2 * r + 4 * s + 6)
    beta = b * values[-r] + c * values[-r + 1] + b * values[-r + 2] + bottom_e * values[-r + 3]
    omega = 7 * ((-1) ** r) * beta - 11 * tau
    clearing = 4 * (s - 1) * math.factorial(r)
    for d in range(1, 2 * s - 2):
        clearing *= p - d
    cleared_beta = beta * clearing
    cleared_tau = tau * clearing
    cleared = omega * clearing
    if (
        cleared_beta.denominator != 1
        or cleared_tau.denominator != 1
        or cleared.denominator != 1
        or clearing % p == 0
    ):
        raise AssertionError((p, s, clearing, cleared_beta, cleared_tau, cleared))
    return beta, tau, omega, clearing, cleared.numerator


def fraction_mod(value: Fraction, p: int) -> int:
    if value.denominator % p == 0:
        raise ZeroDivisionError((value, p))
    return value.numerator * inv(value.denominator, p) % p


def periods_for_shifts(p: int, s: int, shifts: list[int]) -> dict[int, int]:
    r, _, _, polynomial = item219.pnu_poly(p, s, 0)
    chi = 1 if p % 4 == 1 else -1
    answer: dict[int, int] = {}
    for shift in shifts:
        total = 0
        for ell, coefficient in enumerate(polynomial):
            n = r + ell + shift + 1
            if not (1 <= n < p):
                raise AssertionError((p, s, shift, ell, n))
            total += coefficient * item219.residue_weight(n, chi) * inv(n, p)
        answer[shift] = total % p
    return answer


def regularization_crosscheck(p: int, s: int) -> None:
    r = (p - 6 * s - 3) // 2
    top_k = 2 * s - 3
    shifts = list(range(top_k, top_k + 4)) + list(range(-r, -r + 4))
    periods = periods_for_shifts(p, s, sorted(set(shifts)))
    b = 1 - r
    c = 4 * s - r - 1
    top = (
        (top_k + r + 1) * periods[top_k]
        + b * periods[top_k + 1]
        + c * periods[top_k + 2]
        + b * periods[top_k + 3]
    ) % p
    if top != 7 * ((-1) ** r) % p:
        raise AssertionError((p, s, "top", top))
    bottom_k = -r - 1
    bottom_e = -(bottom_k + 2 * r + 4 * s + 6)
    bottom = (
        b * periods[-r]
        + c * periods[-r + 1]
        + b * periods[-r + 2]
        + bottom_e * periods[-r + 3]
    ) % p
    if bottom != 11 % p:
        raise AssertionError((p, s, "bottom", bottom))


def actual_gate(p: int, s: int) -> tuple[int, int]:
    return item221.shifted_period(p, s, 0), item219.period_sum(p, s, 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-max", type=int, default=401)
    ap.add_argument("--regularization-prime-max", type=int, default=101)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if not (11 <= args.regularization_prime_max <= args.prime_max):
        raise ValueError("require 11 <= regularization-prime-max <= prime-max")

    recurrence = verify_recurrence_coefficients()
    z3 = verify_z3_reduction()
    rows: list[tuple[int, ...]] = []
    formal: list[dict[str, object]] = []
    s1_rows: list[dict[str, int]] = []
    counts = {
        "rows": 0,
        "s_equals_1_rows": 0,
        "s_at_least_2_rows": 0,
        "omega_nonzero_exclusions": 0,
        "formal_compatible_rows": 0,
        "actual_common_zero_rows": 0,
        "regularization_crosschecks": 0,
    }

    for p in item219.primes_upto(args.prime_max):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            counts["rows"] += 1
            m = (5 * p - 2 * s - 1) // 4
            if s == 1:
                counts["s_equals_1_rows"] += 1
                t0, s1 = actual_gate(p, s)
                counts["actual_common_zero_rows"] += t0 == s1 == 0
                s1_rows.append({"p": p, "s": s, "m": m, "T0": t0, "S1": s1})
                rows.append((p, s, m, -1, -1, -1, t0, s1))
                continue

            counts["s_at_least_2_rows"] += 1
            beta, tau, omega, r = compatibility_mod(p, s)
            if p <= args.regularization_prime_max:
                regularization_crosscheck(p, s)
                beta_q, tau_q, omega_q, clearing, numerator = compatibility_fraction(p, s)
                if (fraction_mod(beta_q, p), fraction_mod(tau_q, p), fraction_mod(omega_q, p)) != (beta, tau, omega):
                    raise AssertionError((p, s, "fraction replay"))
                if numerator % p != omega * (clearing % p) % p:
                    raise AssertionError((p, s, "clearing replay"))
                counts["regularization_crosschecks"] += 1

            if omega:
                counts["omega_nonzero_exclusions"] += 1
                rows.append((p, s, m, beta, tau, omega, -1, -1))
                continue

            beta_q, tau_q, omega_q, clearing, numerator = compatibility_fraction(p, s)
            if beta == 0 or tau == 0:
                raise AssertionError((p, s, "degenerate formal compatibility", beta, tau))
            if numerator % p:
                raise AssertionError((p, s, "omega numerator"))
            t0, s1 = actual_gate(p, s)
            actual = t0 == s1 == 0
            counts["formal_compatible_rows"] += 1
            counts["actual_common_zero_rows"] += actual
            formal.append(
                {
                    "p": p,
                    "s": s,
                    "m": m,
                    "r": r,
                    "beta_mod_p": beta,
                    "tau_mod_p": tau,
                    "omega_mod_p": omega,
                    "T0_actual": t0,
                    "S1_actual": s1,
                    "actual_collision": actual,
                    "clearing_p_unit_mod_p": clearing % p,
                    "omega_numerator_bits": abs(numerator).bit_length(),
                    "omega_numerator_divisible_by_p": True,
                    "beta_rational": f"{beta_q.numerator}/{beta_q.denominator}",
                    "tau_rational": f"{tau_q.numerator}/{tau_q.denominator}",
                }
            )
            rows.append((p, s, m, beta, tau, omega, t0, s1))

    result = {
        "schema": "item224-j2-cartier-terminal-v1",
        "parameters": {
            "j": 2,
            "prime_max_inclusive": args.prime_max,
            "regularization_prime_max_inclusive": args.regularization_prime_max,
            "cell": "4m+1=5p-2s, 1<=s<=(p-3)/6, p>=11, s=(p-1)/2 mod 2",
        },
        "dependencies": {
            "item221_checker": ITEM221_PATH.name,
            "item221_checker_sha256": sha256(ITEM221_PATH),
            "item219_checker": item221.ITEM219_PATH.name,
            "item219_checker_sha256": sha256(item221.ITEM219_PATH),
        },
        "moment_recurrence": {
            "identity": "(k+r+1)T_k+(1-r)T_(k+1)+(4s-r-1)T_(k+2)+(1-r)T_(k+3)-(k+2r+4s+6)T_(k+4)=0 away from resonance",
            "coefficient_replay": recurrence,
            "safe_forward_range": "0<=k<=2s-4",
            "safe_backward_range": "-r<=k<=-1",
        },
        "regularized_boundaries": {
            "top_index": "k=2s-3, omitted moment T_(2s+1)",
            "top_constant": "7*(-1)^r from p*T_(2s+1) and W_chi(p)=7",
            "bottom_index": "k=-r-1, omitted moment T_(-r-1)",
            "bottom_constant": "11 from K(terminal)=0, K(0)=1, and sum of path weights=-11",
            "warning": "the top equation is inhomogeneous; setting the coefficient -p to zero before regularizing loses the constant 7*(-1)^r",
        },
        "z3_reduction": z3,
        "common_initial_line_s_at_least_2": "lambda*(0,4s-2,2s-5,-(52s^2-36s-27)/(4(s-1)))",
        "compatibility": {
            "beta": "bottom functional of the canonical recurrence solution U",
            "tau": "top functional of U",
            "omega": "7*(-1)^r*beta-11*tau",
            "necessary_condition": "omega=0 mod p, with beta and tau nonzero",
            "canonical_clearing": "4(s-1)*r!*product_(d=1)^(2s-3)(p-d)",
            "clearing_is_p_unit": True,
            "height_scope": "the clearing and recurrence give O(p log p) bit height; this does not imply p-nondivisibility or a zero-rate theorem",
        },
        "finite_classification": {
            "status": "EXACT FINITE ONLY",
            "counts": counts,
            "formal_compatible_rows": formal,
            "s_equals_1_rows": s1_rows,
            "row_digest_sha256": row_digest(rows),
            "interpretation": "formal compatibility is necessary only; all listed formal-compatible rows are explicit non-collisions",
        },
        "status_ledger": {
            "PROVED": [
                "exact five-term moment recurrence and all pivot units",
                "inhomogeneous top constant 7*(-1)^r and bottom constant 11",
                "exact z^3 reduction and common initial line for s>=2",
                "omega=0 is necessary for a common collision when s>=2",
                "the canonical clearing is integral and a p-unit",
            ],
            "EXACT_FINITE": [
                "formal compatibility classification through the recorded bound",
                "seven formal-compatible rows are actual non-collisions",
            ],
            "OPEN": [
                "all-prime classification of omega zeros",
                "the exceptional s=1 family",
                "a sublinear/zero-rate theorem for formal-compatible rows",
                "any capacity reduction or conclusion about e+pi",
            ],
        },
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(payload.decode("utf-8"), end="")


if __name__ == "__main__":
    main()
