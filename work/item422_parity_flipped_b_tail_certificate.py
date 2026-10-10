#!/usr/bin/env python3
"""Deterministic certificate for Item 422's parity-flipped upper-B tail.

Only exact integer and rational arithmetic is used. Geometry rows replay the
odd double-Frobenius sheet; they are not asserted to be actual foreign factors.
"""

from __future__ import annotations

from fractions import Fraction as F
import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item422_parity_flipped_b_tail_certificate.json"

DEPENDENCIES = {
    "sources/item250_j2_ordinary_phase_report.md":
        "56339ec89876abd68627d03b2d3e4e4d1c0fdc8b8d20a59afb274cb7dafe98ce",
    "results/item250_j2_ordinary_phase_certificate.json":
        "6f8d0165448dd8949436649e2824a14578c1bce08e8875a6fd88f770c72cb5e3",
    "sources/item318_j2_actual_period_plucker_report.md":
        "e89f4892b3c2b9b999321de0ec6973547903b755f07b0d34be7f0da634ecd4db",
    "results/item318_j2_actual_period_plucker_certificate.json":
        "75e84016af2c7580f1954f795ed080d25083345578558aae49f6df4253891fd7",
    "sources/item349_j2_degenerate_triple_minor_carrier_report.md":
        "ca3141156cb5034012a174377c3596e22d22cae924625649b6d620d510f4790c",
    "results/item349_j2_degenerate_triple_minor_carrier_certificate.json":
        "b26294d51b1844aeee04146004b2ecec9b6e1ff81aa271a3167e5d86c11bce44",
    "sources/item409_j2_actual_rejection_carrier_report.md":
        "99caf10f9f1561dcb0e3a712f381db639b8260da6594dd305915ebb66f0d69ce",
    "results/item409_j2_actual_rejection_carrier_certificate.json":
        "b6a68f27d131b9a9e8d7e2512d78d54dbbd7bb70f502b2fbaf8277b6a277f940",
    "sources/item416_j2_adaptive_foreign_tail_transport_report.md":
        "66cde3c776df067b600038ff16734e120036274b1e248b7c4644d0564fcc2e30",
    "results/item416_j2_adaptive_foreign_tail_transport_certificate.json":
        "3effb6a6162df9c5639ca155721adb165ed60ff0656d09aac5851c1ffd0bc64b",
    "sources/item419_j2_transverse_double_sheet_report.md":
        "11573a70d65f7c6c76e218ccf74e922b7448037b1612646c2ea0bf2111d4cfbb",
    "results/item419_j2_transverse_double_sheet_certificate.json":
        "3be72f1e942917cd39ff65313a49163e277517b513b12c5814b08d32c0fae682",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> dict[str, str]:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))
    return dict(DEPENDENCIES)


def conv(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def poly_pow(base: list[int], exponent: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = conv(out, base)
    return out


def rising(x: F, count: int) -> F:
    out = F(1)
    for j in range(count):
        out *= x + j
    return out


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise AssertionError((value, prime, "nonunit denominator"))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


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


def b_sum(coefficients: list[int], parity: int, n0: F, d0: F) -> F:
    total = F(0)
    for ell, coefficient in enumerate(coefficients):
        if ell % 2 != parity:
            continue
        t = (ell - parity) // 2
        denominator = rising(1 - d0, t)
        if denominator == 0:
            raise AssertionError((ell, n0, d0, "singular terminating sum"))
        total += coefficient * (-1) ** t * rising(-n0, t) / denominator
    return total


def phase_data(r: int) -> dict[str, Any]:
    if r < 1 or r % 2 != 1 or r % 3 == 0:
        raise ValueError(r)
    h = (r - 1) // 2
    qbar = F(-(2 * r + 3), 3)
    k0 = conv(poly_pow([1, -1], r), [1, 1])
    k1 = conv(poly_pow([1, -1], r), poly_pow([1, 1], 4))

    eta = [F(0)] * (r + 5)
    eta[1] = F(1)
    for k in range(1, r + 3, 2):
        eta[k + 2] = -(qbar + k) * eta[k] / (3 * qbar + k)

    delta0 = sum(F(a) * (eta[j + 1] + eta[j + 3]) for j, a in enumerate(k0))
    delta1 = sum(F(a) * eta[j] for j, a in enumerate(k1))

    # T_perp=2q-r-1=3Q+r+2 is even, so parity zero is the correct tail.
    dbar = F(r + 3, 6)
    nbar = -F(r + 1, 2)
    rho = -dbar / qbar
    g0 = b_sum(k0, 0, nbar, dbar)
    g1 = rho * b_sum(k1, 0, nbar, dbar + 1)
    kappa = -eta[r + 4] / rho

    # Item 349's exact scale v=beta*Delta.
    beta = -F(3 * math.factorial(r + 1), 2 * (2 * r + 3)) / rising(F(-r, 3), r + 1)
    v = (beta * delta0, beta * delta1)

    if (delta0, delta1) != (kappa * g0, kappa * g1):
        raise AssertionError((r, "rank-one parity-tail identity"))

    # Replay the proof term by term after anti-reciprocal coefficient reversal.
    termwise = 0
    for t in range(h + 2):
        u = h + 1 - t
        left = F(k0[2 * u]) * (eta[2 * u + 1] + eta[2 * u + 3])
        weight = (-1) ** t * rising(-nbar, t) / rising(1 - dbar, t)
        right = kappa * k0[2 * t] * weight
        if left != right:
            raise AssertionError((r, 0, t, left, right))
        termwise += 1
    for t in range(h + 3):
        u = h + 2 - t
        left = F(k1[2 * u + 1]) * eta[2 * u + 1]
        weight = (-1) ** t * rising(-nbar, t) / rising(-dbar, t)
        right = kappa * rho * k1[2 * t] * weight
        if left != right:
            raise AssertionError((r, 1, t, left, right))
        termwise += 1

    return {
        "r": r,
        "h": h,
        "qbar": qbar,
        "k0": k0,
        "k1": k1,
        "eta": eta,
        "delta": (delta0, delta1),
        "g": (g0, g1),
        "v": v,
        "dbar": dbar,
        "nbar": nbar,
        "rho": rho,
        "kappa": kappa,
        "beta": beta,
        "termwise": termwise,
    }


def log_tail_coefficient(coefficients: list[int], exponent: int, target: int) -> F:
    """Return [z^target] K(z)(1+z^2)^exponent log(1+z^2)."""
    total = F(0)
    for ell, coefficient in enumerate(coefficients):
        difference = target - ell
        if difference < 0 or difference % 2:
            continue
        index = difference // 2
        if index <= exponent:
            raise AssertionError((exponent, target, ell, index, "not an upper tail"))
        total += coefficient * F(
            (-1) ** (index - exponent - 1)
            * math.factorial(exponent)
            * math.factorial(index - exponent - 1),
            math.factorial(index),
        )
    return total


def geometry_tail_row(p: int, r: int, s: int, foreign_q: int) -> dict[str, Any]:
    kstar = 2 * r + 3
    if not (is_prime(p) and p == kstar + 6 * s and s >= 1):
        raise AssertionError((p, r, s, "actual source geometry"))
    if not (is_prime(foreign_q) and foreign_q > p):
        raise AssertionError((foreign_q, p, "forward prime geometry"))
    if foreign_q % 6 == kstar % 6:
        raise AssertionError((foreign_q, r, "not transverse"))
    numerator = 2 * foreign_q - kstar
    if numerator % 3:
        raise AssertionError((foreign_q, r, "nonintegral Q_perp"))
    Q = numerator // 3
    if not (0 < Q < foreign_q and Q % 2 == 1 and 3 * Q + kstar == 2 * foreign_q):
        raise AssertionError((foreign_q, r, Q, "odd double sheet"))

    target = 2 * foreign_q - r - 1
    if target != 3 * Q + r + 2 or target % 2:
        raise AssertionError((foreign_q, r, Q, target, "even upper target"))
    N = target // 2
    D = N - Q
    if D != (Q + r + 2) // 2 or not (0 < Q < N < foreign_q):
        raise AssertionError((foreign_q, r, Q, N, D, "factorial range"))

    data = phase_data(r)
    k0, k1 = data["k0"], data["k1"]
    g_actual = (
        b_sum(k0, 0, F(N), F(D)),
        -F(D, Q) * b_sum(k1, 0, F(N), F(D + 1)),
    )
    common = F(
        (-1) ** (D - 1) * math.factorial(Q) * math.factorial(D - 1),
        math.factorial(N),
    )
    direct = (
        log_tail_coefficient(k0, Q, target),
        log_tail_coefficient(k1, Q - 1, target),
    )
    if direct != (common * g_actual[0], common * g_actual[1]):
        raise AssertionError((p, r, foreign_q, "finite-tail formula"))

    for actual, phase in zip(g_actual, data["g"]):
        if fmod(actual, foreign_q) != fmod(phase, foreign_q):
            raise AssertionError((p, r, foreign_q, actual, phase, "phase reduction"))
    scale_denominator = data["beta"] * data["kappa"]
    if fmod(scale_denominator, foreign_q) == 0 or fmod(common, foreign_q) == 0:
        raise AssertionError((p, r, foreign_q, "claimed unit scale"))
    unit_scale = common / scale_denominator
    for value, v_value in zip(direct, data["v"]):
        if fmod(value, foreign_q) != fmod(unit_scale * v_value, foreign_q):
            raise AssertionError((p, r, foreign_q, "upper tail is old v-column"))

    return {
        "classification": (
            "EXACT GEOMETRY/FORMULA REPLAY ONLY; foreign_q is not asserted "
            "to divide the actual carrier"
        ),
        "p": p,
        "r": r,
        "s": s,
        "foreign_q": foreign_q,
        "Q_perp": Q,
        "T_perp": target,
        "N_perp": N,
        "D_perp": D,
        "D_perp_is_integral": True,
        "matched_K_parity": "even",
        "factorial_range": f"0<Q={Q}<N={N}<q={foreign_q}",
        "common_period_is_q_unit": True,
        "phase_tail_is_old_v_column": True,
        "phase_scale_is_q_unit": True,
    }


def all_r_reversal_replay() -> dict[str, Any]:
    rows = 0
    terms = 0
    digest_rows: list[str] = []
    for r in range(1, 200, 2):
        if r % 3 == 0:
            continue
        data = phase_data(r)
        rows += 1
        terms += data["termwise"]
        digest_rows.append(
            ":".join(
                [
                    str(r),
                    str(data["kappa"].numerator),
                    str(data["kappa"].denominator),
                    str(data["g"][0].numerator),
                    str(data["g"][0].denominator),
                    str(data["g"][1].numerator),
                    str(data["g"][1].denominator),
                ]
            )
        )
    stream = "\n".join(digest_rows) + "\n"
    return {
        "classification": "EXACT RATIONAL REPLAY; symbolic proof is coefficient reversal",
        "admissible_odd_r_through_199": rows,
        "termwise_equalities": terms,
        "row_digest_sha256": hashlib.sha256(stream.encode("ascii")).hexdigest(),
    }


def geometry_replay() -> dict[str, Any]:
    declared = [
        (23, 7, 1, 43),
        (61, 23, 2, 89),
        (71, 31, 1, 79),
        (131, 55, 3, 139),
        (823, 407, 1, 1019),
    ]
    rows = [geometry_tail_row(*row) for row in declared]
    stream = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    return {
        "classification": (
            "DECLARED GEOMETRY/FORMULA REPLAY ONLY; NO CARRIER DIVISIBILITY, "
            "NO PRIME CENSUS, NO DENSITY EXTRAPOLATION"
        ),
        "rows": rows,
        "row_digest_sha256": hashlib.sha256(stream.encode("utf-8")).hexdigest(),
    }


def ambient_target_no_go() -> dict[str, Any]:
    # Same rank-one columns and parity tail; only the source period changes.
    f = (F(1), F(2))
    b = (F(3), F(6))
    v = (F(5), F(10))
    g = (F(35), F(70))
    det = lambda x, y: x[0] * y[1] - x[1] * y[0]
    if any(det(x, y) for x in (f, b, v, g) for y in (f, b, v, g)):
        raise AssertionError("ambient packet should have rank one")
    residuals = {}
    for Z in (F(28), F(29)):
        residual = tuple(f[i] * Z + 9 * b[i] - 11 * v[i] for i in (0, 1))
        residuals[str(Z)] = [str(x) for x in residual]
    if residuals != {"28": ["0", "0"], "29": ["1", "2"]}:
        raise AssertionError(residuals)
    return {
        "classification": "ABSTRACT LINEAR-ALGEBRA COUNTERMODEL; NOT AN ACTUAL ROW",
        "fixed_column_packet": {
            "f": ["1", "2"],
            "b": ["3", "6"],
            "v": ["5", "10"],
            "parity_tail_g": ["35", "70"],
            "all_two_by_two_minors": 0,
        },
        "same_columns_different_source_period": residuals,
        "conclusion": (
            "the old columns plus the parity-flipped upper tail cannot distinguish "
            "source collision from rejection; a two-parameter identity involving "
            "Z_(r,s) or T_(r,s) is required"
        ),
    }


def build_payload() -> dict[str, Any]:
    return {
        "item": 422,
        "schema": "item422-parity-flipped-b-tail-v1",
        "title": "parity-flipped upper-B tail closes into the old v-column",
        "checked_date_beijing": "2026-09-01",
        "status": "ROOT_AUDITED_CANONICAL_PARITY_TAIL_AND_SCOPED_TARGET_BRIDGE_NO_GO_ZERO_BOOKING",
        "dependency_hashes_verified": verify_dependencies(),
        "theorem": {
            "corrected_integer_parameter": (
                "on Q=(2q-2r-3)/3, T_perp=2q-r-1=3Q+r+2 is even; "
                "matching even K-coefficients gives D_perp=(Q+r+2)/2 in Z"
            ),
            "finite_tail": (
                "U_0=C_perp*g_0 and U_1=C_perp*g_1, with "
                "C_perp=(-1)^(D-1)Q!(D-1)!/N! and N=Q+D"
            ),
            "rank_one_closure": (
                "Delta_nu=kappa_perp*g_nu by termwise anti-reciprocal reversal; "
                "because v=beta_r*Delta, the tail is a q-unit multiple of old v"
            ),
            "target_boundary": (
                "the tail creates no new connection minor and contains no source-s "
                "period; in the natural column/determinant class it cannot transport "
                "the source target or rejection"
            ),
        },
        "reversal_replay": all_r_reversal_replay(),
        "geometry_and_finite_tail_replay": geometry_replay(),
        "target_bridge_no_go": ambient_target_no_go(),
        "capacity": {
            "actual_target": "B_perp_e(M)=o(M)",
            "effect_of_new_tail": (
                "none: its determinant carrier is generated by existing "
                "det(f,v) and det(b,v), hence it is gate-only"
            ),
            "best_retained_unconditional_bound": "B_perp_e(M)=O(M^2/log M) from Item 419",
            "bound_is_not_linear": True,
            "new_booking": 0,
            "new_capacity_reduction": 0,
            "retained_ordinary_j2_ceiling": "1/105",
            "r1_and_deficit_unchanged": True,
        },
        "smallest_missing_lemma": {
            "statement": (
                "prove a two-parameter identity connecting the odd-sheet object to "
                "T_(r,s), or directly prove B_perp_e(M)=o(M)"
            ),
            "status": "OPEN",
        },
        "strict_labels": {
            "PROVED": [
                "integral parity-flipped normalization and finite-tail formula",
                "all-r identity Delta=kappa_perp*g",
                "q-unit proportionality of the tail to old v",
                "scoped determinant/column target-bridge no-go",
                "zero booking and zero capacity reduction",
            ],
            "EXACT_REPLAY_ONLY": [
                "five geometry rows without carrier divisibility assertion",
                "admissible r through 199 for the termwise identity",
            ],
            "ABSTRACT_NOT_ACTUAL": [
                "rank-one packet showing target status is independent of column data"
            ],
            "OPEN": [
                "actual source-target reciprocity across the odd second sheet",
                "B_perp_e(M)=o(M)",
                "a positive adaptive tail-minus-foreign margin",
                "Route 1 and every conclusion about e+pi",
            ],
        },
        "evidence_policy": {
            "gate_distinguished_from_target_and_rejection": True,
            "no_geometry_row_claimed_actual_foreign_support": True,
            "no_prime_census": True,
            "no_finite_extrapolation": True,
            "no_irrationality_claim": True,
        },
    }


def encode(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    data = encode(payload)
    if args.replay is not None and args.replay.read_bytes() != data:
        raise AssertionError((args.replay, "replay mismatch"))
    args.output.write_bytes(data)
    print(json.dumps({"output": str(args.output), "sha256": hashlib.sha256(data).hexdigest()}))


if __name__ == "__main__":
    main()
