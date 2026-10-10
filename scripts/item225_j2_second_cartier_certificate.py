#!/usr/bin/env python3
"""Deterministic certificate for Item 225's second Cartier condition.

The checker imports the frozen Item 224 helper beside it.  It verifies
coefficient reciprocity, the exact regularized forcing formula through
the second Frobenius phase, the closed first-resonance impulse mode, and
the finite joint (Omega, Psi) census.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item225_j2_second_cartier_certificate.json"


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


ITEM224_PATH = resolve("item224_j2_cartier_terminal_certificate.py")
item224 = load("item225_item224", ITEM224_PATH)
item221 = item224.item221
item219 = item224.item219


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def covector_weight(n: int, chi: int, covector: tuple[int, int, int]) -> int:
    residue = n % 4
    coordinate = ((1, 0), (0, 1), (-1, 0), (0, -1))[residue]
    return covector[0] + covector[1] * coordinate[0] + covector[2] * coordinate[1]


def phase_audit() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for chi, p_residue in ((1, 1), (-1, 3)):
        left = (9, -20, -2 * chi)
        dual = (9, -2, -20 * chi)
        table_left = [covector_weight(n, chi, left) for n in range(4)]
        table_dual = [covector_weight(n, chi, dual) for n in range(4)]
        expected_left = [item219.residue_weight(n, chi) for n in range(4)]
        if table_left != expected_left:
            raise AssertionError((chi, table_left, expected_left))
        for n in range(4):
            if covector_weight(n, chi, dual) != covector_weight(p_residue - n, chi, left):
                raise AssertionError((chi, n, "dual phase"))
        wp = covector_weight(p_residue, chi, left)
        w2p = covector_weight(2 * p_residue, chi, left)
        if (wp, w2p) != (7, 29):
            raise AssertionError((chi, wp, w2p))
        rows.append(
            {
                "chi": chi,
                "p_mod_4": p_residue,
                "L_covector_E_C_S": list(left),
                "Ldual_covector_E_C_S": list(dual),
                "W_L_mod_4": table_left,
                "W_Ldual_mod_4": table_dual,
                "W_L_p": wp,
                "W_L_2p": w2p,
            }
        )
    return {"phases": rows, "duality": "W_Ldual(n)=W_L(p-n)"}


def g_polynomial(p: int, s: int) -> tuple[int, list[int]]:
    r, _, _, g = item219.pnu_poly(p, s, 0)
    return r, g


def h_coefficient(p: int, s: int, exponent: int) -> int:
    r, g = g_polynomial(p, s)

    def f_coefficient(q: int) -> int:
        index = q - r
        return g[index] if 0 <= index < len(g) else 0

    return (f_coefficient(exponent) - f_coefficient(exponent - 4)) % p


def recurrence_coefficients(k: int, r: int, s: int) -> tuple[int, int, int, int, int]:
    return (
        k + r + 1,
        1 - r,
        4 * s - r - 1,
        1 - r,
        -(k + 2 * r + 4 * s + 6),
    )


def regularized_rhs(p: int, s: int, k: int) -> int:
    chi = 1 if p % 4 == 1 else -1
    total = 0
    for multiple in (p, 2 * p):
        coefficient = h_coefficient(p, s, multiple - k - 1)
        total -= coefficient * item219.residue_weight(multiple, chi)
    return total % p


def finite_period(p: int, s: int, k: int, dual: bool = False) -> int:
    r, g = g_polynomial(p, s)
    chi = 1 if p % 4 == 1 else -1
    left = (9, -20, -2 * chi)
    dual_covector = (9, -2, -20 * chi)
    covector = dual_covector if dual else left
    total = 0
    for ell, coefficient in enumerate(g):
        denominator = r + ell + k + 1
        if denominator % p == 0:
            continue
        total += (
            coefficient
            * covector_weight(denominator, chi, covector)
            * pow(denominator % p, -1, p)
        )
    return total % p


Vector = tuple[int, int, int]  # inhomogeneous constant, lambda, free first residue


def vector_add(left: Vector, right: Vector, p: int) -> Vector:
    return tuple((left[j] + right[j]) % p for j in range(3))  # type: ignore[return-value]


def vector_scale(value: Vector, scalar: int, p: int) -> Vector:
    return tuple((scalar * value[j]) % p for j in range(3))  # type: ignore[return-value]


def linear_combination(
    values: dict[int, Vector], coefficients: tuple[int, int, int, int], k: int, p: int
) -> Vector:
    result: Vector = (0, 0, 0)
    for shift, coefficient in enumerate(coefficients):
        result = vector_add(result, vector_scale(values[k + shift], coefficient, p), p)
    return result


def second_phase_components(p: int, s: int) -> dict[str, int]:
    if s < 2:
        raise ValueError("second-phase theorem requires s>=2")
    beta, tau, omega, r = item224.compatibility_mod(p, s)
    polynomial_r, g = g_polynomial(p, s)
    if polynomial_r != r:
        raise AssertionError((p, s, r, polynomial_r))

    def local_h_coefficient(exponent: int) -> int:
        def f_coefficient(q: int) -> int:
            index = q - r
            return g[index] if 0 <= index < len(g) else 0

        return (f_coefficient(exponent) - f_coefficient(exponent - 4)) % p
    base = item224.initial_line_mod(p, s)
    values: dict[int, Vector] = {k: (0, value, 0) for k, value in base.items()}

    first = 2 * s - 3
    for k in range(0, first):
        coefficients = recurrence_coefficients(k, r, s)
        pivot = coefficients[4] % p
        if pivot == 0:
            raise AssertionError((p, s, k, "premature first pivot"))
        lower = linear_combination(values, coefficients[:4], k, p)
        values[k + 4] = vector_scale(lower, -pow(pivot, -1, p), p)

    first_lhs = linear_combination(values, recurrence_coefficients(first, r, s)[:4], first, p)
    if first_lhs != (0, tau, 0):
        raise AssertionError((p, s, "first terminal", first_lhs, tau))
    first_rhs = 7 * ((-1) ** r) % p

    first_resonant_index = 2 * s + 1
    values[first_resonant_index] = (0, 0, 1)
    second = p + 2 * s - 3
    for k in range(first + 1, second):
        coefficients = recurrence_coefficients(k, r, s)
        pivot = coefficients[4] % p
        if pivot == 0:
            raise AssertionError((p, s, k, "premature second pivot"))
        lower = linear_combination(values, coefficients[:4], k, p)
        # Before the second terminal K_k can contain z^p but not z^(2p).
        rhs = -7 * local_h_coefficient(p - k - 1) % p
        numerator = vector_add((rhs, 0, 0), vector_scale(lower, -1, p), p)
        values[k + 4] = vector_scale(numerator, pow(pivot, -1, p), p)

    second_lhs = linear_combination(values, recurrence_coefficients(second, r, s)[:4], second, p)
    rho_constant, rho_lambda, rho_free = second_lhs
    second_rhs = 29 * ((-1) ** r) % p

    degree = len(g) - 1
    if degree != (p + 2 * s - 1) // 2:
        raise AssertionError((p, s, degree))
    if not degree < p - 4:
        raise AssertionError((p, s, "degree support", degree, p - 4))
    for n in range(p):
        expected = g[n] if n < len(g) else 0
        if values[first_resonant_index + n][2] != expected % p:
            raise AssertionError((p, s, "free mode", n, values[first_resonant_index + n][2], expected))
    if rho_free != 0:
        raise AssertionError((p, s, "free mode reached second terminal", rho_free))

    psi = (
        tau * (rho_constant - second_rhs)
        + 7 * ((-1) ** r) * rho_lambda
    ) % p
    psi_bottom = (
        beta * (rho_constant - second_rhs)
        + 11 * rho_lambda
    ) % p
    if omega == 0 and (psi == 0) != (psi_bottom == 0):
        raise AssertionError((p, s, "top/bottom Psi disagreement", psi, psi_bottom))
    return {
        "r": r,
        "beta": beta,
        "tau": tau,
        "omega": omega,
        "rho_constant": rho_constant,
        "rho_lambda": rho_lambda,
        "rho_free": rho_free,
        "first_rhs": first_rhs,
        "second_rhs": second_rhs,
        "psi": psi,
        "psi_bottom": psi_bottom,
        "impulse_degree": degree,
        "support_gap": p - 4 - degree,
    }


def verify_row_identities(p: int, s: int) -> None:
    r, g = g_polynomial(p, s)
    degree = len(g) - 1
    sign = (-1) ** r
    for ell in range(degree + 1):
        if (g[ell] - sign * g[degree - ell]) % p:
            raise AssertionError((p, s, "coefficient reciprocity", ell))

    # Regularized reciprocal identity, including the paired p/0
    # resonance at k=2s+1 and k^vee=-r-1.
    for k in range(0, 2 * s + 2):
        dual_k = 2 * s - r - k
        left = finite_period(p, s, k)
        right = sign * -1 * finite_period(p, s, dual_k, dual=True)
        if left != right % p:
            raise AssertionError((p, s, "period reciprocity", k, dual_k, left, right))

    # Replay the exact forcing formula from the first through the second
    # Frobenius terminal using actual regularized periods.
    first = 2 * s - 3
    second = p + 2 * s - 3
    periods = {k: finite_period(p, s, k) for k in range(first, second + 5)}
    for k in range(first, second + 1):
        coefficients = recurrence_coefficients(k, r, s)
        lhs = sum(coefficients[j] * periods[k + j] for j in range(5)) % p
        rhs = regularized_rhs(p, s, k)
        if lhs != rhs:
            raise AssertionError((p, s, "regularized recurrence", k, lhs, rhs))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-max", type=int, default=401)
    ap.add_argument("--identity-prime-max", type=int, default=101)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if not (17 <= args.identity_prime_max <= args.prime_max):
        raise ValueError("require 17 <= identity-prime-max <= prime-max")

    phases = phase_audit()
    rows: list[tuple[int, ...]] = []
    item224_formal: list[dict[str, int | bool]] = []
    joint_formal: list[dict[str, int]] = []
    counts = {
        "rows": 0,
        "s_equals_1_rows": 0,
        "s_at_least_2_rows": 0,
        "omega_nonzero_rows": 0,
        "omega_zero_rows": 0,
        "omega_zero_psi_nonzero_rows": 0,
        "joint_omega_psi_zero_rows": 0,
        "actual_common_zero_rows": 0,
        "full_identity_replay_rows": 0,
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
                rows.append((p, s, m, -1, -1, -1, -1))
                continue

            counts["s_at_least_2_rows"] += 1
            data = second_phase_components(p, s)
            if p <= args.identity_prime_max:
                verify_row_identities(p, s)
                counts["full_identity_replay_rows"] += 1
            omega = data["omega"]
            psi = data["psi"]
            rows.append(
                (
                    p,
                    s,
                    m,
                    omega,
                    psi,
                    data["rho_constant"],
                    data["rho_lambda"],
                )
            )
            if omega:
                counts["omega_nonzero_rows"] += 1
                continue

            counts["omega_zero_rows"] += 1
            t0, s1 = item224.actual_gate(p, s)
            actual = t0 == s1 == 0
            counts["actual_common_zero_rows"] += actual
            entry: dict[str, int | bool] = {
                "p": p,
                "s": s,
                "m": m,
                "r": data["r"],
                "tau": data["tau"],
                "beta": data["beta"],
                "rho_constant": data["rho_constant"],
                "rho_lambda": data["rho_lambda"],
                "rho_free": data["rho_free"],
                "second_rhs": data["second_rhs"],
                "psi": psi,
                "psi_bottom": data["psi_bottom"],
                "T0_actual": t0,
                "S1_actual": s1,
                "actual_collision": actual,
            }
            item224_formal.append(entry)
            if psi:
                counts["omega_zero_psi_nonzero_rows"] += 1
            else:
                counts["joint_omega_psi_zero_rows"] += 1
                joint_formal.append({key: int(value) for key, value in entry.items() if isinstance(value, int)})

    if counts["rows"] != counts["s_equals_1_rows"] + counts["s_at_least_2_rows"]:
        raise AssertionError(counts)
    result = {
        "schema": "item225-j2-second-cartier-v1",
        "parameters": {
            "j": 2,
            "prime_max_inclusive": args.prime_max,
            "full_identity_replay_prime_max_inclusive": args.identity_prime_max,
            "cell": "4m+1=5p-2s, 1<=s<=(p-3)/6, p>=11, s=(p-1)/2 mod 2",
        },
        "dependencies": {
            "item224_checker": ITEM224_PATH.name,
            "item224_checker_sha256": sha256(ITEM224_PATH),
            "item221_checker": item224.ITEM221_PATH.name,
            "item221_checker_sha256": sha256(item224.ITEM221_PATH),
            "item219_checker": item224.item221.ITEM219_PATH.name,
            "item219_checker_sha256": sha256(item224.item221.ITEM219_PATH),
        },
        "phase_and_reciprocity": phases,
        "coefficient_reciprocity": {
            "g": "(1-z)^r*(1+z)*(1+z^2)^(2s)",
            "degree": "d=r+4s+1=(p+2s-1)/2",
            "identity": "g_l=(-1)^r*g_(d-l)",
            "period_identity": "That_L(k)=(-1)^(r+1)*That_Ldual(2s-r-k)",
        },
        "regularized_recurrence": {
            "definition": "That_L(k) omits primitive monomials whose exponent is divisible by p",
            "forcing": "sum_(j=0)^4 A_j(k) That_L(k+j)=-sum_(a>=1) [z^(ap)]K_k*W_L(ap)",
            "K_k": "z^(k+1)*(1-z^4)*f0",
            "first_terminal": "k=2s-3, RHS=7*(-1)^r",
            "second_terminal": "k=p+2s-3, RHS=29*(-1)^r",
            "W_L_p": 7,
            "W_L_2p": 29,
        },
        "free_mode": {
            "initial_data": "X_0=1 and X_-1=X_-2=X_-3=0 at moment index 2s+1",
            "generating_polynomial": "X(z)=g(z)",
            "differential_identity": "(1-z^4)X'=[(1-r)+(4s-r-1)z+(1-r)z^2+(r+2s+2)z^3]X mod p",
            "exact_integer_difference": "the z^3 coefficient differs from the logarithmic derivative of g by p=2r+6s+3",
            "degree_gap": "p-4-deg(g)=(p-2s-7)/2>0 for every admissible s>=2 row",
            "consequence": "the four free-mode entries at the second terminal vanish identically",
        },
        "second_condition": {
            "affine_terminal": "rho_constant+lambda*rho_lambda=29*(-1)^r; rho_free=0",
            "top_scaling": "lambda*tau=7*(-1)^r",
            "psi": "tau*(rho_constant-29*(-1)^r)+7*(-1)^r*rho_lambda",
            "necessary": "collision with s>=2 implies beta*tau!=0 and Omega=Psi=0 mod p",
        },
        "finite_classification": {
            "status": "EXACT FINITE ONLY",
            "counts": counts,
            "item224_omega_zero_rows": item224_formal,
            "joint_omega_psi_zero_rows": joint_formal,
            "row_digest_sha256": row_digest(rows),
            "interpretation": "Psi eliminates every Item224 formal-compatible row through the stated bound; no all-prime inference is made",
        },
        "status_ledger": {
            "PROVED": [
                "exact coefficient and period reciprocity with both p mod 4 phases",
                "exact regularized recurrence forcing through the second Frobenius terminal",
                "W_L(p)=7 and W_L(2p)=29",
                "the free first-resonance mode is g and vanishes before the second terminal",
                "a collision with s>=2 requires Omega=Psi=0 and beta*tau nonzero",
            ],
            "EXACT_FINITE": [
                "every Item224 Omega-zero row through the stated bound has Psi nonzero",
                "there are no joint Omega=Psi=0 rows through the stated bound",
            ],
            "OPEN": [
                "all-prime exclusion or density bound for simultaneous Omega=Psi zeros",
                "the exceptional s=1 family",
                "a zero-rate theorem for the j=2 cell",
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
