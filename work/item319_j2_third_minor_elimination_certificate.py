#!/usr/bin/env python3
"""Deterministic certificate for Item 319's third connection minor.

The all-r theorem splits C_r=det(b,d) into an explicit hypergeometric
terminal unit and a canonical inhomogeneous determinant.  It also proves,
by two Laurent-chart substitutions, that eliminating the actual period from
the full exterior incidence produces only the old determinant ideal.
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
from typing import Any


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEPENDENCIES = {
    "scripts/item237_j1_algebraic_residual_certificate.py":
        "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf",
    "results/item237_j1_algebraic_residual_certificate.json":
        "eba1519f4d376d442f396048528190b474cc5464bbe42c3bdf31a9bdaf39dd6b",
    "scripts/item250_j2_ordinary_phase_certificate.py":
        "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce",
    "results/item250_j2_ordinary_phase_certificate.json":
        "6f8d0165448dd8949436649e2824a14578c1bce08e8875a6fd88f770c72cb5e3",
    "scripts/item291_j2_connection_plane_certificate.py":
        "5c86001827b0012605563b04dafc5f157f27fddf2f1625254e9196bc0de8c2df",
    "results/item291_j2_connection_plane_certificate.json":
        "831cd4c74b10555c261eccebef7fd9c5a871bcef97a43d52e77c731b9b7188b5",
    "scripts/item314_j2_two_branch_gate_certificate.py":
        "cc5f155e5f3248c500cd2101e401c25cec37ce43b31fbb4582843fc33a9b2f0e",
    "results/item314_j2_two_branch_gate_certificate.json":
        "77de2dd46726a5a48e9adc4e40f96341d5da6c8db304d79f0ef8eeb7807245b1",
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


i237 = load("item319_i237", "scripts/item237_j1_algebraic_residual_certificate.py")
i250 = load("item319_i250", "scripts/item250_j2_ordinary_phase_certificate.py")
i291 = load("item319_i291", "scripts/item291_j2_connection_plane_certificate.py")
i314 = load("item319_i314", "scripts/item314_j2_two_branch_gate_certificate.py")


def det(left: tuple[F, F], right: tuple[F, F]) -> F:
    return left[0] * right[1] - left[1] * right[0]


def rising(value: F, count: int) -> F:
    out = F(1)
    for index in range(count):
        out *= value + index
    return out


def beta_closed(r: int) -> F:
    if r < 1 or r % 2 != 1 or r % 3 == 0:
        raise ValueError(r)
    return -F(3, 2 * (2 * r + 3)) * F(math.factorial(r + 1), 1) / rising(F(-r, 3), r + 1)


def canonical_factorization(r: int, data: dict[str, Any] | None = None) -> dict[str, Any]:
    """Construct beta, the canonical particular chain, and K with C=beta*K."""
    if data is None:
        data = i250.phase_data(r)
    q: F = data["qbar"]
    k0: list[int] = data["k0"]
    k1: list[int] = data["k1"]
    kstar = 2 * r + 3

    eta = [F(0)] * (kstar + 1)
    eta[1] = F(1)
    for k in range(1, kstar - 1, 2):
        eta[k + 2] = -(q + k) * eta[k] / (3 * q + k)

    # y=v+w is canonical: the even chain starts at zero, while the odd
    # chain has the terminal boundary y_(2r+3)=0.
    y = [F(0)] * (kstar + 1)
    for k in range(0, kstar - 1, 2):
        y[k + 2] = (1 - (q + k) * y[k]) / (3 * q + k)
    y[kstar] = F(0)
    for k in range(kstar - 2, 0, -2):
        y[k] = (1 - (3 * q + k) * y[k + 2]) / (q + k)

    s0 = sum(F(coefficient) * (y[ell + 1] + y[ell + 3])
             for ell, coefficient in enumerate(k0))
    s1 = sum(F(coefficient) * y[ell] for ell, coefficient in enumerate(k1))
    delta0 = sum(F(coefficient) * (eta[ell + 1] + eta[ell + 3])
                 for ell, coefficient in enumerate(k0))
    delta1 = sum(F(coefficient) * eta[ell] for ell, coefficient in enumerate(k1))
    kernel = s0 * delta1 - s1 * delta0
    beta = beta_closed(r)

    _, b0, d0 = data["x0"]
    _, b1, d1 = data["x1"]
    c_minor = det((b0, b1), (d0, d1))
    if beta != data["terminal"][1]:
        raise AssertionError((r, "beta", beta, data["terminal"][1]))
    if (s0, s1) != (b0 + d0, b1 + d1):
        raise AssertionError((r, "particular chain"))
    if (beta * delta0, beta * delta1) != (d0, d1):
        raise AssertionError((r, "homogeneous chain"))
    if c_minor != beta * kernel:
        raise AssertionError((r, "C factorization"))

    return {
        "beta": beta,
        "S": (s0, s1),
        "Delta": (delta0, delta1),
        "K": kernel,
        "C": c_minor,
    }


def inherited_minor_normalization(r: int, data: dict[str, Any], branches: list[F]) -> dict[str, F]:
    residue = r % 6
    n = (r - residue) // 6
    sigma = i314.gauge_value(residue, n) * i314.KAPPA[residue] / F(16**n)
    f = tuple(data["st"])
    b = (data["x0"][1], data["x1"][1])
    d = (data["x0"][2], data["x1"][2])
    ell = det(f, b)
    m_value = det(f, d)
    a_value = branches[r]
    b_value = i314.i237.lagrange_coefficient(r)
    if ell != 2 * sigma * a_value:
        raise AssertionError((r, "ell normalization"))
    if m_value != -sigma * b_value:
        raise AssertionError((r, "m normalization"))
    return {
        "sigma": sigma,
        "ell": ell,
        "m": m_value,
        "a": a_value,
        "b": b_value,
    }


def factorization_theorem() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT ALL r ON BOTH ACTUAL RAYS",
        "old_minors": {
            "sigma": "g_n*kappa_e/16^n for r=6n+e, e in {1,5}",
            "ell": "2*sigma*a_r",
            "m": "-sigma*b_r",
            "unit": "Item314 proves sigma is a p-unit on every actual row",
        },
        "third_minor": {
            "C": "beta_r*K_r",
            "beta": "-3*(r+1)!/[2*(2r+3)*(-r/3)_(r+1)]",
            "K": "S_0*Delta_1-S_1*Delta_0",
            "S": "the b+d connection vector from the canonical inhomogeneous y-chain",
            "Delta": "the normalized d connection vector from the homogeneous eta-chain",
        },
        "chains": {
            "eta_even": "eta_(2t)=0",
            "eta_odd": "eta_1=1 and eta_(k+2)=-(qbar+k)*eta_k/(3*qbar+k)",
            "y_even": "y_0=0 and (qbar+k)y_k+(3qbar+k)y_(k+2)=1",
            "y_odd": "y_(2r+3)=0 with the same recurrence solved backward",
            "connection_sums": (
                "S_0=sum K0_l*(y_(l+1)+y_(l+3)), S_1=sum K1_l*y_l; "
                "Delta uses eta in the same two sums"
            ),
        },
        "quotient_on_ell_chart": "C/ell=(beta/(2*sigma))*(K/a_r)",
        "modular_warning": "the quotient is never used when p divides ell or a_r",
    }


def beta_unit_theorem() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT ALL ACTUAL ROWS",
        "formula": "beta_r=-3*(r+1)!/[2*(2r+3)*(-r/3)_(r+1)]",
        "nonzero_factors": (
            "actual rows have 3 not dividing r; the rising factors are "
            "(3j-r)/3 for 0<=j<=r and are nonzero"
        ),
        "range": (
            "abs(3j-r)<=2r<p and r+1<2r+3<p; constants 2,3 and 2r+3 are p-units"
        ),
        "conclusion": "v_p(beta_r)=0 and C_r=0 mod p iff K_r=0 mod p",
        "compulsory_content_removed": "beta_r only; removing it changes no actual prime support",
    }


def elimination_theorem() -> dict[str, Any]:
    # Exact coefficient checks of both universal syzygies.
    tests = [(F(2), F(3), F(5), F(7), F(11)),
             (F(-1), F(4), F(-2), F(9), F(6))]
    for ell, m_value, c_minor, c_value, z_value in tests:
        d_gate = 9 * c_value * ell - 11 * m_value
        e_b = ell * z_value + 11 * c_minor
        e_d = m_value * z_value + 9 * c_value * c_minor
        if ell * e_d - m_value * e_b != c_minor * d_gate:
            raise AssertionError("second Plucker syzygy")
        z_ell = -11 * c_minor / ell
        if (m_value * z_ell + 9 * c_value * c_minor) != c_minor * d_gate / ell:
            raise AssertionError("ell substitution")
        z_m = -9 * c_value * c_minor / m_value
        if (ell * z_m + 11 * c_minor) != -c_minor * d_gate / m_value:
            raise AssertionError("m substitution")

    return {
        "classification": "SYMBOLIC EXACT LAURENT-CHART ELIMINATION",
        "ring": "R=k[c,ell,m,C], with Z adjoined",
        "definitions": {
            "D": "9*c*ell-11*m",
            "E_b": "ell*Z+11*C",
            "E_d": "m*Z+9*c*C",
        },
        "syzygy": "ell*E_d-m*E_b=C*D",
        "ell_chart": {
            "substitution": "Z=-11*C/ell",
            "E_d_after_substitution": "C*D/ell",
            "elimination_ideal": "(D,E_b,E_d) intersect R[ell^(-1)] = (D)",
        },
        "m_chart": {
            "substitution": "Z=-9*c*C/m",
            "E_b_after_substitution": "-C*D/m",
            "elimination_ideal": "(D,E_b,E_d) intersect R[m^(-1)] = (D)",
        },
        "conclusion": (
            "on either nondegenerate chart, every coefficient-only resultant "
            "obtained by eliminating the actual period is inherited from D"
        ),
        "scope_warning": (
            "this does not remove the actual-period residual; it proves that "
            "one must retain arithmetic information about Z to get a second condition"
        ),
    }


def poly_eval(poly: list[F], value: F) -> F:
    out = F(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def operator_reuse_counterexamples(cache: dict[int, dict[str, Any]]) -> dict[str, Any]:
    """Exact first-row counterexamples to direct reuse of the old operator."""
    base = i237.recurrence_polynomials()
    rows = []
    maximum_r = 23
    branches = i314.i309.branch_coefficients(maximum_r)
    for residue, phase in ((1, 5), (5, 1)):
        r_values = [residue + 6 * shift for shift in range(4)]
        c_values = []
        k_values = []
        normalized_values = []
        for r in r_values:
            data = cache.setdefault(r, i250.phase_data(r))
            fac = canonical_factorization(r, data)
            old = inherited_minor_normalization(r, data, branches)
            c_values.append(fac["C"])
            k_values.append(fac["K"])
            normalized_values.append(fac["C"] / old["sigma"])

        candidate = i291.candidate_polynomials(phase)
        candidate_raw = sum(poly_eval(candidate[j], F(0)) * c_values[j] for j in range(4))
        candidate_16 = sum(poly_eval(candidate[j], F(0)) * F(16**j) * c_values[j]
                           for j in range(4))
        base_raw = sum(poly_eval(base[j], F(residue, 2)) * normalized_values[j]
                       for j in range(4))
        base_scaled = sum(poly_eval(base[j], F(residue, 2)) * F(1, 16**j)
                          * normalized_values[j] for j in range(4))
        base_kernel = sum(poly_eval(base[j], F(residue, 2)) * k_values[j]
                          for j in range(4))
        residuals = {
            "Item291_on_C": candidate_raw,
            "Item291_on_16^n_C": candidate_16,
            "Item237_on_C_over_sigma": base_raw,
            "Item237_scaled_on_C_over_sigma": base_scaled,
            "Item237_on_K": base_kernel,
        }
        if any(value == 0 for value in residuals.values()):
            raise AssertionError((residue, residuals))
        rows.append({
            "residue": residue,
            "indices": r_values,
            "residuals": {
                name: {
                    "numerator_digits": len(str(abs(value.numerator))),
                    "denominator_digits": len(str(value.denominator)),
                    "sha256": hashlib.sha256(str(value).encode("ascii")).hexdigest(),
                    "nonzero": True,
                }
                for name, value in residuals.items()
            },
        })
    return {
        "classification": "PROVED EXACT COUNTEREXAMPLES TO FIVE SPECIFIC REUSE ANSATZE",
        "rows": rows,
        "conclusion": (
            "C, 16^n*C, C/sigma, and K do not directly reuse the certified "
            "Item291/237 operator in any of the displayed natural gauges"
        ),
        "warning": "this does not exclude a different higher-order recurrence or algebraic realization",
    }


def exact_replay() -> dict[str, Any]:
    cache: dict[int, dict[str, Any]] = {}
    maximum_r = 53
    branches = i314.i309.branch_coefficients(maximum_r)
    rows = []
    for r in range(1, maximum_r + 1, 2):
        if r % 3 == 0:
            continue
        data = cache.setdefault(r, i250.phase_data(r))
        fac = canonical_factorization(r, data)
        old = inherited_minor_normalization(r, data, branches)
        rows.append({
            "r": r,
            "residue": r % 6,
            "beta": str(fac["beta"]),
            "K": str(fac["K"]),
            "C": str(fac["C"]),
            "ell": str(old["ell"]),
            "m": str(old["m"]),
            "factorization_checked": True,
            "old_normalization_checked": True,
        })
    stream = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return {
        "classification": "EXACT FINITE REPLAY OF ALL-r THEOREMS",
        "r_max": maximum_r,
        "rows": len(rows),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "operator_reuse": operator_reuse_counterexamples(cache),
        "warning": "the replay is not the proof of the chain factorization or elimination theorem",
    }


def capacity_audit() -> dict[str, Any]:
    return {
        "classification": "PROVED ACCOUNTING AND SCOPED NO-GO",
        "fixed_M_relation": "2*M=5*r+14*s+7",
        "old_gate": "H_r*(18*2^(2s)*a_r+11*b_r)",
        "second_integer_condition": (
            "Q_(r,s)^4*(ell_r*Z_actual+11*C_r), with Q a p-unit as in Item318"
        ),
        "overlap": (
            "the second condition lives strictly inside D=0 and cannot be "
            "added as independent raw capacity"
        ),
        "exact_target": (
            "weighted log support of primes dividing the gcd of the old gate "
            "and the cleared actual-period residual on fixed-M rows"
        ),
        "minor_only_no_go": (
            "on ell or m nondegenerate charts, eliminating Z from the full "
            "minor tower returns only (D); no second coefficient-only divisor exists"
        ),
        "height_no_go": (
            "P-recursiveness or individual O(M log M)-type numerator height "
            "does not imply an o(M) bound for the gcd support over O(M) tied rows"
        ),
        "retained_ordinary_j2_ceiling_per_6M": "1/105",
        "new_capacity_reduction": 0,
        "new_booking": 0,
    }


def build() -> dict[str, Any]:
    return {
        "item": 319,
        "schema": "item319-j2-third-minor-elimination-certificate-v1",
        "scope": "all-r third-minor arithmetic and period-elimination no-go",
        "dependencies": DEPENDENCIES,
        "capacity_first": capacity_audit(),
        "minor_factorization": factorization_theorem(),
        "beta_unit": beta_unit_theorem(),
        "elimination": elimination_theorem(),
        "replay": exact_replay(),
        "strict_labels": {
            "PROVED": [
                "the inherited all-r ell and m normalizations",
                "C_r=beta_r*K_r with explicit canonical chains",
                "beta_r is a p-unit on every actual row",
                "both Laurent-chart elimination ideals equal the old determinant ideal",
                "exact counterexamples to five direct old-operator reuse ansatze",
                "zero booking",
            ],
            "EXACT_FINITE_REPLAY": ["the declared r<=53 identity replay"],
            "OPEN": [
                "a different global recurrence or algebraic realization for K_r",
                "weighted gcd support for the actual-period residual on fixed-M rows",
                "any reduction of the 1/105 ceiling",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path,
        default=HERE / "item319_j2_third_minor_elimination_certificate.json",
    )
    args = parser.parse_args()
    result = build()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "sha256": sha256(args.output),
        "replay_rows": result["replay"]["rows"],
        "new_booking": result["capacity_first"]["new_booking"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
