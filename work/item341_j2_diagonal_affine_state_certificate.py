#!/usr/bin/env python3
"""Deterministic certificate for Item 341.

The checker verifies the exact centered affine coordinates for the
determinant and moving period target, the diagonal Cartier substitution,
the degenerate Pluecker localization, and finite diagnostics for the
actual half-binomial state.  The all-parameter ideal and Zariski-density
proofs are in the companion report.
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
RESULT_NAME = "item341_j2_diagonal_affine_state_certificate.json"

DEPENDENCIES = {
    "sources/item338_j2_secondary_cartier_saturation_report.md":
        "14aa87b718b4bb83dd3e5371412fd231829f809b853d1a52eabba6181650ac33",
    "scripts/item338_j2_secondary_cartier_saturation_certificate.py":
        "5209d57fee32a6bad74e8f5b933116aa4d62448b1f9ca44e539cadf7f95fe6bd",
    "results/item338_j2_secondary_cartier_saturation_certificate.json":
        "accf5bf87b148c73117f05b8d9f7eee92af1d59611871498593cc992c758450d",
    "manifests/item338_j2_secondary_cartier_saturation_manifest.json":
        "d3ecc6c74e3dbd3b921a3f5c3aa363eac10e68322536c88ced5e6972785a6573",
}


def default_output() -> Path:
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def det(left: tuple[F, F], right: tuple[F, F]) -> F:
    return left[0] * right[1] - left[1] * right[0]


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def h_term(index: int) -> F:
    return F(math.comb(2 * index, index), 8 ** index)


def h_prefix(index: int) -> F:
    return sum((h_term(j) for j in range(index + 1)), F(0))


def generic_affine_replay() -> dict[str, Any]:
    tests = [
        (F(2), F(3), F(5), F(7), F(11), F(13), F(17), 0),
        (F(-3), F(4), F(7, 2), F(-5), F(19), F(23, 3), F(-29), 1),
        (F(5, 7), F(-11, 3), F(13), F(17, 2), F(-19), F(31), F(37, 5), 4),
    ]
    rows = []
    for ell, mu, C, B, kappa, tau, phi, m in tests:
        c = F(41, 3)
        K = F(9, 2) * kappa * B
        D = 9 * c * ell - 11 * mu
        T_ell = K * ell * phi + (-1) ** m * (ell * B * tau - 11 * C)
        c_star = 11 * mu / (9 * ell)
        phi_star = (-1) ** (m + 1) * F(2, 9) / kappa * (tau - 11 * C / (ell * B))
        if D != 9 * ell * (c - c_star):
            raise AssertionError((ell, mu, c, "D centered"))
        if T_ell != K * ell * (phi - phi_star):
            raise AssertionError((ell, mu, C, B, kappa, tau, phi, m, "T centered"))
        jacobian = 9 * K * ell**2
        if jacobian == 0:
            raise AssertionError((ell, K, "Jacobian"))
        rows.append((ell, mu, C, B, kappa, tau, phi, m, c_star, phi_star, jacobian))
    return {
        "classification": "SYMBOLIC EXACT RATIONAL IDENTITIES",
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
    }


def actual_affine_row(i318: Any, i331: Any, i334: Any, prime: int, r: int, s: int) -> tuple[Any, ...]:
    m = s - 1
    d = r + 4
    n = 3 * m + d
    q = 2 * m + d
    if prime != 6 * m + 2 * d + 1:
        raise AssertionError((prime, r, s, "tied phase"))
    epsilon = i331.legendre_two(prime)
    c_p = i331.coefficient(n, q, prime)
    data = i318.i250.phase_data(r)
    coeff = i318.coefficients(data)
    period = i318.actual_period(r, s, data)
    h_m = i334.h_value(m)
    correction = i334.p_correction(r + 2, m)
    H_m = h_prefix(m)
    phi = F(c_p) + epsilon * h_m * correction
    c = F(4 ** s)
    ell = coeff["ell"]
    mu = coeff["m"]
    C = coeff["C"]
    B = period["B"]
    kappa = period["kappa"]
    tau = period["tau"]
    K = F(9, 2) * kappa * B
    D = 9 * c * ell - 11 * mu
    T_ell = K * ell * phi + (-1) ** m * (ell * B * tau - 11 * C)
    if fmod(ell, prime) == 0:
        raise AssertionError((prime, r, s, "declared ell chart"))
    c_star = 11 * mu / (9 * ell)
    phi_star = (-1) ** (m + 1) * F(2, 9) / kappa * (tau - 11 * C / (ell * B))
    theta = h_m * correction + epsilon * (1 - phi_star)
    if D != 9 * ell * (c - c_star):
        raise AssertionError((prime, r, s, "actual D centered"))
    if T_ell != K * ell * (phi - phi_star):
        raise AssertionError((prime, r, s, "actual T centered"))
    if fmod(phi - phi_star, prime) != fmod(-epsilon * (H_m - theta), prime):
        raise AssertionError((prime, r, s, "Cartier-to-H substitution"))
    if fmod(T_ell, prime) != fmod(-epsilon * K * ell * (H_m - theta), prime):
        raise AssertionError((prime, r, s, "actual H target"))
    jacobian = 9 * K * ell**2
    if fmod(jacobian, prime) == 0:
        raise AssertionError((prime, r, s, "Jacobian unit"))
    return (
        prime, r, s, m, fmod(D, prime), fmod(T_ell, prime),
        fmod(c, prime), fmod(c_star, prime), fmod(H_m, prime),
        fmod(theta, prime), fmod(jacobian, prime),
    )


def actual_affine_replay(i318: Any, i331: Any, i334: Any) -> dict[str, Any]:
    declared = [
        (11, 1, 1),
        (17, 1, 2),
        (29, 1, 4),
        (271, 113, 7),
        (367, 65, 39),
        (383, 109, 27),
        (599, 7, 97),
    ]
    rows = [actual_affine_row(i318, i331, i334, *row) for row in declared]
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
    }


def pluecker_replay() -> dict[str, Any]:
    tests = [
        ((F(1), F(2)), (F(3), F(6)), (F(5), F(10))),
        ((F(0), F(0)), (F(1), F(3)), (F(2), F(6))),
        ((F(2), F(-1)), (F(-4), F(2)), (F(6), F(-3))),
    ]
    rows = []
    for f, b, v in tests:
        ell, mu, C = det(f, b), det(f, v), det(b, v)
        if (ell, mu, C) != (F(0), F(0), F(0)):
            raise AssertionError((f, b, v, ell, mu, C))
        for c in (F(-2), F(0), F(7, 3)):
            U = (9 * c * b[0] - 11 * v[0], 9 * c * b[1] - 11 * v[1])
            if det(f, U) != 9 * c * ell - 11 * mu:
                raise AssertionError((f, b, v, c, "D identity"))
        rows.append((*f, *b, *v, ell, mu, C))
    # If ell=mu=0 but C!=0, then f=0 and 9cb-11v cannot vanish.
    f, b, v, c = (F(0), F(0)), (F(1), F(0)), (F(0), F(1)), F(5)
    if det(f, b) != 0 or det(f, v) != 0 or det(b, v) == 0:
        raise AssertionError("rank-two exceptional chart")
    U = (9 * c * b[0] - 11 * v[0], 9 * c * b[1] - 11 * v[1])
    if U == (0, 0):
        raise AssertionError("impossible C chart")
    return {
        "classification": "SYMBOLIC EXACT RATIONAL IDENTITIES",
        "rank_one_examples": len(rows),
        "impossible_C_chart_checked": True,
        "row_digest_sha256": digest_rows(rows),
    }


def primes_up_to(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(bound) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start:bound + 1:prime] = b"\x00" * (((bound - start) // prime) + 1)
    return [value for value in range(2, bound + 1) if sieve[value]]


def state_replay(m_max: int) -> dict[str, Any]:
    rows = []
    H = F(1)
    h = F(1)
    for m in range(m_max + 1):
        if m:
            previous_h = h
            h *= F(2 * m - 1, 4 * m)
            H += h
            if h != previous_h * F(2 * m - 1, 4 * m):
                raise AssertionError((m, "h recurrence"))
        if h != h_term(m) or H != h_prefix(m):
            raise AssertionError((m, h, H, "direct prefix"))
        rows.append((m, 4 ** (m + 1), H.numerator, H.denominator, h.numerator, h.denominator))

    actual_r1 = []
    for prime in primes_up_to(6 * m_max + 11):
        if prime < 11 or prime % 6 != 5:
            continue
        m = (prime - 11) // 6
        if prime != 6 * m + 11:
            raise AssertionError((prime, m, "r=1 ray"))
        actual_r1.append((prime, m, 4 ** (m + 1), h_prefix(m).numerator, h_prefix(m).denominator))

    # The asymptotic proof orders nonzero terms by exponential weight
    # 2*i-k, then by the smallest k.  Distinct (i,k) have a unique leader.
    ordering_checks = 0
    pairs = [(i, k) for i in range(13) for k in range(13)]
    keys = {}
    for pair in pairs:
        i, k = pair
        key = (2 * i - k, -k)
        if key in keys and keys[key] != pair:
            raise AssertionError((key, keys[key], pair, "nonunique asymptotic leader"))
        keys[key] = pair
        ordering_checks += 1

    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "m_max_inclusive": m_max,
        "state_rows": len(rows),
        "actual_r1_prime_rows": len(actual_r1),
        "actual_r1_sample": actual_r1[:10],
        "asymptotic_ordering_checks": ordering_checks,
        "state_digest_sha256": digest_rows(rows),
        "actual_r1_digest_sha256": digest_rows(actual_r1),
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    i318 = load("item341_i318", "scripts/item318_j2_actual_period_plucker_certificate.py")
    i331 = load("item341_i331", "scripts/item331_j2_global_cartier_concentration_certificate.py")
    i334 = load("item341_i334", "scripts/item334_j2_coupled_cartier_carrier_certificate.py")
    return {
        "schema": "item341-j2-diagonal-affine-state-v1",
        "classification": "PROVED_DIAGONAL_AFFINE_COORDINATES_AND_FIXED_CURVE_NO_GO",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "c_star": "11*mu/(9*ell)",
            "phi_star": "(-1)^(m+1)*(2/(9*kappa))*(tau-11*C/(ell*B))",
            "D_centered": "D=9*ell*(c-c_star)",
            "T_centered": "T_ell=(9*kappa*B/2)*ell*(Phi-Phi_star)",
            "H_centered_mod_p": "T_ell=-epsilon*(9*kappa*B/2)*ell*(H_m-Theta)",
            "Jacobian": "81*kappa*B*ell^2/2, a unit on the ell chart",
            "degenerate_localization": "for p>11, a collision with ell=0 forces ell=mu=C=0",
        },
        "generic_affine_replay": generic_affine_replay(),
        "actual_affine_replay": actual_affine_replay(i318, i331, i334),
        "pluecker_replay": pluecker_replay(),
        "state_replay": state_replay(args.m_max),
        "capacity": {
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "new_capacity_reduction": 0,
            "new_booking": 0,
            "missing_input": (
                "moving mod-p correlation for the actual state (4^s,H_m) against "
                "(c_star,Theta), plus weighted control of the degenerate triple-minor content"
            ),
        },
        "scope_warning": (
            "The affine ideal and fixed characteristic-zero curve classes are closed. "
            "Moving p-dependent Frobenius relations and weighted zero density remain open."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m-max", type=int, default=120)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.m_max < 10:
        raise ValueError("m_max must be at least 10")
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
