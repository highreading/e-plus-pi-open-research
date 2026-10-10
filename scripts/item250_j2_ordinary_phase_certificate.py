#!/usr/bin/env python3
"""Deterministic certificate for Item 250's ordinary j=2 phase gate.

The checker reconstructs the fixed-r affine phase state, retains the unique
Frobenius terminal residue, verifies the coefficient-reversal rank-one
identity, compares the phase formulas with frozen Item 219 on actual rows,
and emits the exact finite census.  All arithmetic is standard-library
integer/Fraction arithmetic; bounded scans are evidence only.
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
RESULT_NAME = "item250_j2_ordinary_phase_certificate.json"
ITEM219_NAME = "item219_common_log_j2_certificate.py"
ITEM219_SHA256 = "bf9ee30675b5745225f08d2d82e500fd1f6797d69f94ab5949602e266f8b38cc"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        path = base / name
        if path.exists():
            return path
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


ITEM219_PATH = resolve(ITEM219_NAME)
if sha256(ITEM219_PATH) != ITEM219_SHA256:
    raise RuntimeError("Item219 checker hash mismatch")
item219 = load("item250_item219", ITEM219_PATH)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def conv(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def poly_pow(base: list[int], exponent: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = conv(out, base)
    return out


def rising(x: F, count: int) -> F:
    out = F(1)
    for k in range(count):
        out *= x + k
    return out


def fmod(value: F, p: int) -> int:
    if value.denominator % p == 0:
        raise AssertionError(("nonunit fraction", value, p))
    return value.numerator * pow(value.denominator, -1, p) % p


def row_digest(rows: list[tuple[int, ...]]) -> str:
    data = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(data.encode("ascii")).hexdigest()


def b_sum(coefficients: list[int], parity: int, n0: F, d0: F) -> F:
    total = F(0)
    for ell, coefficient in enumerate(coefficients):
        if ell % 2 != parity:
            continue
        t = (ell - parity) // 2
        total += (
            coefficient
            * ((-1) ** t)
            * rising(-n0, t)
            / rising(1 - d0, t)
        )
    return total


def phase_data(r: int) -> dict[str, Any]:
    if r < 1 or r % 2 != 1 or r % 3 == 0:
        raise ValueError(r)
    qbar = F(-(2 * r + 3), 3)
    k0 = conv(poly_pow([1, -1], r), [1, 1])
    k1 = conv(poly_pow([1, -1], r), poly_pow([1, 1], 4))

    # Backward odd chain.  At k*=2r+3, p*J_(k*+2) retains the unique
    # top coefficient 1, so J_k*=(c-1)/(Q+k*).
    kstar = 2 * r + 3
    alpha = F(1, 1) / (qbar + kstar)
    beta = -alpha
    for k in range(kstar - 2, 0, -2):
        alpha = (1 - (3 * qbar + k) * alpha) / (qbar + k)
        beta = -(3 * qbar + k) * beta / (qbar + k)
    terminal = (alpha, beta)

    # J_k = u_k*e+v_k*c+w_k for every argument used by X_0,X_1.
    states: list[tuple[F, F, F] | None] = [None] * (r + 5)
    states[0] = (F(1), F(0), F(0))
    states[1] = (F(0), alpha, beta)
    for k in range(r + 3):
        u, v, w = states[k]  # type: ignore[misc]
        denominator = 3 * qbar + k
        states[k + 2] = (
            -(qbar + k) * u / denominator,
            (1 - (qbar + k) * v) / denominator,
            -(qbar + k) * w / denominator,
        )

    def add_state(total: tuple[F, F, F], coefficient: int, state: tuple[F, F, F]):
        return tuple(total[j] + coefficient * state[j] for j in range(3))

    x0 = (F(0), F(0), F(0))
    for ell, coefficient in enumerate(k0):
        pair = tuple(states[ell + 1][j] + states[ell + 3][j] for j in range(3))  # type: ignore[index]
        x0 = add_state(x0, coefficient, pair)  # type: ignore[arg-type]
    x1 = (F(0), F(0), F(0))
    for ell, coefficient in enumerate(k1):
        x1 = add_state(x1, coefficient, states[ell])  # type: ignore[arg-type]

    # The two lower B tails at a_nu.
    n_a = r + qbar + 1
    sa0 = b_sum(k0, 0, n_a, F(r + 1))
    sa1 = b_sum(k1, 1, n_a, F(r + 2))
    ca0 = F((-1) ** r * math.factorial(r), 1) / rising(qbar + 1, r + 1)
    ca1 = F((-1) ** (r + 1) * math.factorial(r + 1), 1) / rising(qbar, r + 2)
    ba0 = ca0 * sa0
    ba1 = ca1 * sa1

    # The common factorial f is retained on the two upper B tails.
    dbar = F(r, 6)
    rbar = -F(r + 2, 2)
    st0 = b_sum(k0, 1, rbar, dbar)
    st1_raw = b_sum(k1, 1, rbar, dbar + 1)
    rho = -dbar / qbar
    st1 = rho * st1_raw

    a0, b0, d0 = x0
    a1, b1, d1 = x1
    l_value = 9 * (st0 * b1 - st1 * b0)
    m_value = st0 * (9 * d1 - 10 * ba1) - st1 * (9 * d0 - 10 * ba0)
    obstruction = l_value**3 + F(2 ** (2 * r + 2), 1) * m_value**3

    return {
        "r": r,
        "qbar": qbar,
        "k0": k0,
        "k1": k1,
        "terminal": terminal,
        "states": states,
        "x0": x0,
        "x1": x1,
        "ba": (ba0, ba1),
        "st": (st0, st1),
        "rho": rho,
        "L": l_value,
        "M": m_value,
        "R": obstruction,
    }


def reversal_certificate(r: int, data: dict[str, Any]) -> tuple[F, int]:
    h = (r - 1) // 2
    qbar: F = data["qbar"]
    k0: list[int] = data["k0"]
    k1: list[int] = data["k1"]
    states = data["states"]
    dbar = F(r, 6)
    rbar = -F(r + 2, 2)
    rho: F = data["rho"]
    kappa = (
        F(2 * (4 * h + 5), 9 * (4 * h + 3))
        * ((-1) ** h)
        * rising(F(5 - 2 * h, 6), h)
        / rising(F(2 * h + 3, 2), h)
    )

    a0_terms: list[F] = []
    f0_terms: list[F] = []
    for t in range(h + 1):
        ell = 2 * t + 1
        a0_terms.append(k0[ell] * (states[ell + 1][0] + states[ell + 3][0]))
        f0_terms.append(
            k0[ell] * ((-1) ** t) * rising(-rbar, t) / rising(1 - dbar, t)
        )
    for t in range(h + 1):
        if a0_terms[t] != kappa * f0_terms[h - t]:
            raise AssertionError(("nu0 reversal", r, t))

    a1_terms: list[F] = []
    f1_terms: list[F] = []
    for t in range(h + 3):
        a1_terms.append(k1[2 * t] * states[2 * t][0])
        f1_terms.append(
            rho
            * k1[2 * t + 1]
            * ((-1) ** t)
            * rising(-rbar, t)
            / rising(-dbar, t)
        )
    for t in range(h + 3):
        if a1_terms[t] != kappa * f1_terms[h + 2 - t]:
            raise AssertionError(("nu1 reversal", r, t))

    if data["x0"][0] != kappa * data["st"][0]:
        raise AssertionError(("nu0 rank one", r))
    if data["x1"][0] != kappa * data["st"][1]:
        raise AssertionError(("nu1 rank one", r))
    data["kappa"] = kappa
    return kappa, len(a0_terms) + len(a1_terms)


def unit_and_resonance_audit(p: int, s: int, data: dict[str, Any]) -> dict[str, int]:
    """Audit every denominator family on one actual row.

    The proof report supplies the all-row inequalities.  This routine checks
    those sharp inequalities, the first resonant denominator, the direct
    J_1 value, and every reduced phase fraction used by the implementation.
    It deliberately keeps the lower and upper B-tail ranges separate.
    """

    r = data["r"]
    q = 2 * s
    if p != 2 * r + 3 * q + 3 or r < 1 or r % 2 != 1 or r % 3 == 0:
        raise AssertionError(("bad actual row", p, s, r))

    checks = 0

    def unit(value: int, label: str) -> None:
        nonlocal checks
        checks += 1
        if value % p == 0:
            raise AssertionError(("nonunit", label, p, s, r, value))

    # Every direct J_k used in X_0 or X_1 has a denominator in [1,p-1].
    used_k = set(range(r + 5))
    for k in used_k:
        low = q + k
        high = q + k + 2 * (q - 1)
        checks += 1
        if not (1 <= low <= high <= 3 * q + r + 2 == p - r - 1 < p):
            raise AssertionError(("J range", p, s, r, k, low, high))

    # Forward and backward recurrence pivots.  The sole zero pivot is never
    # inverted; it is the explicitly retained Frobenius terminal.
    for k in range(r + 3):
        unit(3 * q + k, "forward 3Q+k")
    kstar = 2 * r + 3
    for k in range(1, kstar + 1, 2):
        unit(q + k, "backward Q+k")
    if (3 * q + kstar) != p:
        raise AssertionError(("resonance", p, s, r))
    checks += 1

    # The direct terminal has one and only one p denominator, at t=Q-1,
    # with binomial coefficient one.  All earlier terms are p-units.
    resonant_denominators = [q + kstar + 2 + 2 * t for t in range(q)]
    if resonant_denominators[-1] != p or any(
        not (1 <= denominator < p) for denominator in resonant_denominators[:-1]
    ):
        raise AssertionError(("terminal denominator pattern", p, s, r))
    if math.comb(q - 1, q - 1) != 1:
        raise AssertionError("top binomial coefficient")
    checks += len(resonant_denominators)

    c_value = pow(2, q, p)
    direct_j1 = sum(
        math.comb(q - 1, t) * pow(q + 1 + 2 * t, -1, p)
        for t in range(q)
    ) % p
    alpha, beta = data["terminal"]
    localized_j1 = (fmod(alpha, p) * c_value + fmod(beta, p)) % p
    if direct_j1 != localized_j1:
        raise AssertionError(("direct J1", p, s, r, direct_j1, localized_j1))
    direct_jstar = sum(
        math.comb(q - 1, t) * pow(q + kstar + 2 * t, -1, p)
        for t in range(q)
    ) % p
    if (q + kstar) * direct_jstar % p != (c_value - 1) % p:
        raise AssertionError(("inhomogeneous terminal", p, s, r, direct_jstar))
    checks += 2

    # Lower tails: both have N_a=r+Q+1<p, but distinct D_0 and t ranges.
    h = (r - 1) // 2
    n_a = r + q + 1
    if not (max(q, r, r + 1, n_a) < p):
        raise AssertionError(("lower factorial range", p, s, r, n_a))
    if not (h + 1 < r + 1 and h + 2 < r + 2):
        raise AssertionError(("lower hypergeometric range", r, h))
    checks += 3

    # Upper tails: D and R are different from N_a and must be audited
    # separately.  The two denominator strings stop before their first zero.
    d_value = (r + q + 1) // 2
    r_value = q + d_value
    if not (1 <= d_value <= r_value == (p - r - 2) // 2 < p):
        raise AssertionError(("upper factorial range", p, s, r, d_value, r_value))
    if not (h < d_value and h + 2 <= d_value):
        raise AssertionError(("upper hypergeometric range", p, s, r, h, d_value))
    checks += 3

    # The specialized rational state is a reduction of the preceding actual
    # p-unit formulas.  Check every reduced fraction that is subsequently
    # used, including kappa; numerator zeros are retained and never divided.
    fractions: list[F] = [
        data["qbar"],
        data["rho"],
        data["L"],
        data["M"],
        data["R"],
        data["kappa"],
        *data["terminal"],
        *data["x0"],
        *data["x1"],
        *data["ba"],
        *data["st"],
    ]
    for state in data["states"]:
        if state is not None:
            fractions.extend(state)
    for value in fractions:
        unit(value.denominator, "reduced phase denominator")

    # Explicit small constants and the exponentiation bases are units.
    for value in (2, 3, c_value, 2 * r + 1, 2 * r + 3):
        unit(value, "fixed phase factor")
    if not (2 * r + 3 < p):
        raise AssertionError(("kappa/rho range", p, r))
    checks += 1
    return {"assertions": checks, "resonant_terms": len(resonant_denominators)}


def factorial_tail(p: int, r: int, q: int) -> int:
    d_value = (r + q + 1) // 2
    r_value = q + d_value
    out = (-1) ** (d_value - 1) % p
    for k in range(1, q + 1):
        out = out * k % p
    for k in range(1, d_value):
        out = out * k % p
    for k in range(1, r_value + 1):
        out = out * pow(k, -1, p) % p
    return out


def evaluate_phase_row(p: int, s: int, data: dict[str, Any]) -> dict[str, int]:
    r = data["r"]
    q = 2 * s
    c_value = pow(2, q, p)
    e_value = sum(
        math.comb(q - 1, t) * pow(q + 2 * t, -1, p)
        for t in range(q)
    ) % p
    f_value = factorial_tail(p, r, q)

    x_values = []
    for a_value, b_value, d_value in (data["x0"], data["x1"]):
        x_values.append(
            (fmod(a_value, p) * e_value + fmod(b_value, p) * c_value + fmod(d_value, p)) % p
        )
    ba_values = tuple(fmod(value, p) for value in data["ba"])
    bt_values = tuple(f_value * fmod(value, p) % p for value in data["st"])
    gates = tuple(
        (9 * x_values[nu] - 10 * ba_values[nu] - bt_values[nu]) % p
        for nu in (0, 1)
    )
    residual = (fmod(data["st"][0], p) * gates[1] - fmod(data["st"][1], p) * gates[0]) % p
    lm_residual = (fmod(data["L"], p) * c_value + fmod(data["M"], p)) % p
    if residual != lm_residual:
        raise AssertionError(("residual", p, s, residual, lm_residual))
    if pow(c_value, 3, p) * pow(2, 2 * r + 2, p) % p != 1:
        raise AssertionError(("cube", p, s))
    return {
        "e": e_value,
        "c": c_value,
        "f": f_value,
        "x0": x_values[0],
        "x1": x_values[1],
        "ba0": ba_values[0],
        "ba1": ba_values[1],
        "bt0": bt_values[0],
        "bt1": bt_values[1],
        "g0": gates[0],
        "g1": gates[1],
        "linear": residual,
        "resultant": fmod(data["R"], p),
    }


def actual_rows(prime_max: int):
    for p in item219.primes_upto(prime_max):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            r = (p - 6 * s - 3) // 2
            yield p, s, r


TARGET_LINEAR = (
    (953, 158, 1),
    (2281, 378, 5),
    (5711, 941, 31),
    (1279, 199, 41),
    (3929, 636, 55),
    (1657, 256, 59),
    (367, 39, 65),
)
TARGET_CUBIC_ONLY = ((67, 7, 11), (127, 3, 53))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-max", type=int, default=401)
    ap.add_argument("--identity-r-max", type=int, default=199)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if args.prime_max < 23 or args.identity_r_max < 5:
        raise ValueError("require prime-max>=23 and identity-r-max>=5")

    cache: dict[int, dict[str, Any]] = {}
    identity_rows: list[tuple[int, int, int, int, int]] = []
    identity_terms = 0
    exact_resultant_zeros: list[int] = []
    for r in range(1, args.identity_r_max + 1, 2):
        if r % 3 == 0:
            continue
        data = phase_data(r)
        cache[r] = data
        kappa, terms = reversal_certificate(r, data)
        identity_terms += terms
        identity_rows.append(
            (r, kappa.numerator, kappa.denominator, data["R"].numerator, data["R"].denominator)
        )
        if data["R"] == 0:
            exact_resultant_zeros.append(r)

    counts = {
        "rows": 0,
        "common_gate_zeros": 0,
        "linear_residual_zeros": 0,
        "cubic_resultant_zeros": 0,
        "direct_phase_coordinate_equalities": 0,
        "unit_audit_rows": 0,
        "unit_audit_assertions": 0,
        "frobenius_resonant_terms": 0,
    }
    finite_rows: list[tuple[int, ...]] = []
    linear_hits: list[dict[str, int]] = []
    cubic_hits: list[dict[str, int]] = []
    for p, s, r in actual_rows(args.prime_max):
        data = cache.get(r)
        if data is None:
            data = phase_data(r)
            cache[r] = data
            reversal_certificate(r, data)
        audit = unit_and_resonance_audit(p, s, data)
        counts["unit_audit_rows"] += 1
        counts["unit_audit_assertions"] += audit["assertions"]
        counts["frobenius_resonant_terms"] += audit["resonant_terms"]
        phase = evaluate_phase_row(p, s, data)
        direct = [item219.log_moments(p, s, nu) for nu in (0, 1)]
        for nu in (0, 1):
            x, y, yprime = direct[nu]
            if x != phase[f"x{nu}"] or y != phase[f"ba{nu}"] or yprime != (-phase[f"bt{nu}"]) % p:
                raise AssertionError(("Item219 phase mismatch", p, s, nu, direct[nu], phase))
            counts["direct_phase_coordinate_equalities"] += 3
        if tuple((9 * x - 10 * y + yp) % p for x, y, yp in direct) != (phase["g0"], phase["g1"]):
            raise AssertionError(("gate mismatch", p, s))

        counts["rows"] += 1
        common = phase["g0"] == phase["g1"] == 0
        counts["common_gate_zeros"] += common
        counts["linear_residual_zeros"] += phase["linear"] == 0
        counts["cubic_resultant_zeros"] += phase["resultant"] == 0
        record = (p, s, r, phase["g0"], phase["g1"], phase["linear"], phase["resultant"])
        finite_rows.append(record)
        if phase["linear"] == 0:
            linear_hits.append({"p": p, "s": s, "r": r, "g0": phase["g0"], "g1": phase["g1"]})
        if phase["resultant"] == 0:
            cubic_hits.append(
                {"p": p, "s": s, "r": r, "linear": phase["linear"], "g0": phase["g0"], "g1": phase["g1"]}
            )
        if common and (phase["linear"] != 0 or phase["resultant"] != 0):
            raise AssertionError(("necessary condition", p, s))

    target_rows = []
    for kind, targets in (("linear", TARGET_LINEAR), ("cubic_only", TARGET_CUBIC_ONLY)):
        for p, s, r in targets:
            if (
                p != 2 * r + 6 * s + 3
                or not item219.primes_upto(p)[-1] == p
                or not (1 <= s <= (p - 3) // 6)
                or (5 * p - 2 * s - 1) % 4
                or r % 2 != 1
                or r % 3 == 0
            ):
                raise AssertionError(("bad target", p, s, r))
            data = cache.get(r) or phase_data(r)
            reversal_certificate(r, data)
            audit = unit_and_resonance_audit(p, s, data)
            row = evaluate_phase_row(p, s, data)
            if row["resultant"] != 0:
                raise AssertionError(("target resultant", kind, p, s, row))
            if kind == "linear" and row["linear"] != 0:
                raise AssertionError(("target linear", p, s, row))
            if kind == "cubic_only" and row["linear"] == 0:
                raise AssertionError(("target not cubic-only", p, s, row))
            if row["g0"] == row["g1"] == 0:
                raise AssertionError(("target collision", p, s))
            target_rows.append(
                {
                    "kind": kind,
                    "p": p,
                    "s": s,
                    "r": r,
                    "unit_audit_assertions": audit["assertions"],
                    **row,
                }
            )

    result = {
        "schema": "item250-j2-ordinary-phase-v2",
        "parameters": {
            "prime_max_inclusive": args.prime_max,
            "identity_r_max_inclusive": args.identity_r_max,
            "cell": "p=2r+6s+3, r odd, Q=2s",
        },
        "exact_formulas": {
            "phase": "Qbar=-(2r+3)/3",
            "base_period": "J_k=sum_(t=0)^(Q-1) C(Q-1,t)/(Q+k+2t)",
            "recurrence": "(3Q+k)J_(k+2)=2^Q-(Q+k)J_k",
            "resonant_terminal": "J_(2r+3)=(2^Q-1)/(Q+2r+3)",
            "affine_state": "J_k=u_k*e+v_k*c+w_k, e=J_0, c=2^Q",
            "rank_one": "a_nu=kappa_r*f_nu for nu=0,1 by termwise coefficient reversal",
            "gate": "G_nu=f_nu*Z+P_nu*c+Q_nu, Z=9*kappa_r*e-f",
            "linear_eliminant": "f_0*G_1-f_1*G_0=L_r*c+M_r",
            "cube": "2^(2r+2)*c^3=1 mod p",
            "fixed_r_resultant": "R_r=L_r^3+2^(2r+2)*M_r^3",
        },
        "symbolic_reversal_replay": {
            "admissible_r_values": len(identity_rows),
            "term_equalities": identity_terms,
            "exact_resultant_zero_r": exact_resultant_zeros,
            "digest_sha256": row_digest(identity_rows),
            "r1_terminal": {
                "alpha": [phase_data(1)["terminal"][0].numerator, phase_data(1)["terminal"][0].denominator],
                "beta": [phase_data(1)["terminal"][1].numerator, phase_data(1)["terminal"][1].denominator],
                "L": [phase_data(1)["L"].numerator, phase_data(1)["L"].denominator],
                "M": [phase_data(1)["M"].numerator, phase_data(1)["M"].denominator],
            },
        },
        "finite_actual_replay": {
            "counts": counts,
            "linear_hits": linear_hits,
            "cubic_hits": cubic_hits,
            "row_digest_sha256": row_digest(finite_rows),
            "role": "bounded exact replay only",
        },
        "all_row_unit_audit": {
            "A_state_direct_denominators": "1 <= Q+k+2t <= 3Q+r+2 = p-r-1 < p",
            "A_state_forward_pivots": "1 <= 3Q+k <= 3Q+r+2 = p-r-1 < p",
            "A_state_backward_pivots": "1 <= Q+k <= Q+2r+3 = p-2Q < p",
            "Frobenius_exception": "3Q+(2r+3)=p is not inverted; its unique top coefficient is retained as 1",
            "lower_B_factorials": "N_a=r+Q+1<p, separately from the upper range",
            "upper_B_factorials": "D=(r+Q+1)/2 and R=Q+D=(p-r-2)/2<p",
            "phase_specialization": "each displayed phase denominator is the reduction of one of these actual p-unit factors; 2 and 3 are units",
            "primitive_content_division": False,
        },
        "explicit_counterexamples_to_sufficiency": target_rows,
        "status": {
            "PROVED": [
                "exact affine fixed-r reduction of both A tails, with the unique Frobenius residue -1 retained",
                "exact fixed-r rational formulas for both B tails, with their common factorial period retained",
                "termwise reciprocal identity a_nu=kappa_r*f_nu for both rows",
                "collision implies L_r*c+M_r=0 and hence p divides the reduced numerator of R_r",
                "all phase denominators are p-units on every actual row",
            ],
            "EXACT_FINITE": [
                "direct equality with all three frozen Item219 coordinates on every row through the recorded prime bound",
                "the recorded linear and cubic false-positive rows",
                "termwise rational replay through the recorded r bound",
            ],
            "OPEN": [
                "all-prime nonvanishing or weighted control of R_r at p=2r+6s+3",
                "control of the actual residual period Z on rows where the eliminant vanishes",
                "any capacity reduction or conclusion about e+pi",
            ],
        },
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
        },
        "dependency": {ITEM219_NAME: ITEM219_SHA256},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
