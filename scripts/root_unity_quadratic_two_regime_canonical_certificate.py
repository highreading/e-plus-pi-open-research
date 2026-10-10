#!/usr/bin/env python3
"""Deterministic certificate for the quadratic two-regime canonical no-go.

The finite exact checks below audit algebraic identities and declared
constants.  The accompanying source proves the all-parameter statements.
No finite grid is used as an extrapolation.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import resource
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/root_unity_quadratic_two_regime_canonical_no_go.md"
OUTPUT = ROOT / "results/root_unity_quadratic_two_regime_canonical_certificate.json"
RSS_GUARD_KIB = 4 * 1024 * 1024

DEPENDENCIES = {
    "sources/root_unity_closer_root_sech_pade_audit.md":
        "f837e5be64de4985e721f9e5d3731e6d13e01c41fa973a937c4bc1dce0977ecf",
    "sources/root_unity_quadratic_euler_gcd_kummer_obstruction.md":
        "a720ef166a3b772d85c32934782fcfa4d41797b274ea964259973a216bb369ca",
    "sources/root_unity_quadratic_euler_beta_denominator_floor.md":
        "8b22a86eea520400245e5529809da2dcce56cbfb26c9836677e23ccd0a197a0a",
    "results/root_unity_quadratic_euler_gcd_kummer_hashes.sha256":
        "74b79cee3b86e5fe37700e1db68ed91976a56c01a783c1e10d5e13651d82ba49",
    "results/root_unity_quadratic_euler_beta_denominator_hashes.sha256":
        "22fba2af00e25aa5a956b923e490d2a853dd170ab2292178190bb5a1507d6f1d",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def v2(n: int) -> int:
    assert n
    n = abs(n)
    return (n & -n).bit_length() - 1


def euler_even(limit: int) -> list[int]:
    """Return E_0,E_2,...,E_{2*limit} for sech."""
    values = [1]
    for n in range(1, limit + 1):
        value = -sum(
            math.comb(2 * n, 2 * j) * values[j] for j in range(n)
        )
        values.append(value)
    return values


def reduced_row(n: int, values: list[int]) -> tuple[int, int, int]:
    raw_q = (2 * n + 2) * (2 * n + 1) * abs(values[n])
    raw_p = abs(values[n + 1])
    g = math.gcd(raw_p, raw_q)
    return raw_p // g, raw_q // g, g


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": i, "byte": b}
        for i, b in enumerate(data)
        if b < 32 and b not in (9, 10, 13)
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def main() -> None:
    dependency_checks = {}
    for rel, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / rel)
        assert actual == expected, (rel, expected, actual)
        dependency_checks[rel] = {"expected": expected, "actual": actual}

    # Formal determinant, elimination, product, and resultant identities.
    P, Q, Pp, Qp, T = sp.symbols("P Q Pp Qp T")
    U = sp.symbols("U")
    C = 4 * Q - P * T**2
    Cp = 4 * Qp - Pp * T**2
    D = P * Qp - Pp * Q
    assert sp.expand(Qp * C - Q * Cp + D * T**2) == 0
    assert sp.expand(Pp * C - P * Cp + 4 * D) == 0
    product = sp.Poly(sp.expand(C * Cp), T)
    assert product.all_coeffs() == [
        P * Pp, 0, -4 * (P * Qp + Pp * Q), 0, 16 * Q * Qp
    ]
    res_u = sp.factor(sp.resultant(4 * Q - P * U, 4 * Qp - Pp * U, U))
    res_t = sp.factor(sp.resultant(C, Cp, T))
    assert sp.simplify(res_u + 4 * D) == 0
    assert sp.simplify(res_t - 16 * D**2) == 0

    # Nearest-pole coefficients and unique fixed two-row cancellation.
    a, b = sp.symbols("a b")
    pole3 = sp.expand(a + b / sp.Integer(9))
    pole5 = sp.expand(a + b / sp.Integer(25))
    assert sp.solve(sp.Eq(pole3, 0), b) == [-9 * a]
    assert sp.simplify(pole5.subs(b, -9 * a)) == 16 * a / 25
    richardson_5 = (
        9 * (-sp.Integer(24)) - (-sp.Integer(24)) * 25
    )
    assert richardson_5 == 384
    normalized_richardson_5 = Fraction(richardson_5, 8)
    assert normalized_richardson_5 == 48

    # Conditional rate ledger.
    threshold_ledger = []
    for r in range(1, 9):
        tau2 = 2 * r * r + r
        tau4 = 4 * r * r + r
        c3 = 2 * math.log(3) / tau2
        c5 = 2 * math.log(5) / tau2
        h_common_floor = math.log(3) - math.log(5) / tau2
        assert tau4 >= 5
        assert 2 * c3 < 2 * math.log(3)
        assert h_common_floor > 0
        threshold_ledger.append({
            "algebraic_degree_r": r,
            "quadratic_relative_threshold": tau2,
            "quartic_relative_threshold": tau4,
            "c3": c3,
            "c5": c5,
            "c5_over_c3": c5 / c3,
            "necessary_common_gcd_rate_for_richardson": h_common_floor,
        })
    assert abs(threshold_ledger[0]["c3"] - 0.7324081924454064) < 1e-15
    assert abs(threshold_ledger[0]["c5"] - 1.0729586082894003) < 1e-15
    assert abs(
        threshold_ledger[0]["necessary_common_gcd_rate_for_richardson"]
        - 0.5621329845234097
    ) < 1e-15

    # Exact Euler rows audit all parity, determinant, and reduced-denominator
    # identities on a declared finite grid.
    grid_max_n = 120
    evens = euler_even(grid_max_n + 2)
    rows = [reduced_row(n, evens) for n in range(1, grid_max_n + 2)]
    row_checks = []
    for n in range(1, grid_max_n + 1):
        pn, qn, gn = rows[n - 1]
        pp, qp, gp = rows[n]
        assert math.gcd(pn, qn) == math.gcd(pp, qp) == 1
        assert pn % 2 == pp % 2 == 1
        assert v2(qn) == 1 + v2(n + 1)
        assert v2(qp) == 1 + v2(n + 2)

        det = pn * qp - pp * qn
        assert det > 0
        assert v2(det) == 1

        raw_r = 9 * pp * qn - pn * qp
        raw_s = 8 * qn * qp
        k = math.gcd(raw_r, raw_s)
        phat, qhat = raw_r // k, raw_s // k
        assert raw_r > 0
        assert v2(raw_r) == v2(k) == 1
        assert phat % 2 == 1
        assert math.gcd(phat, qhat) == 1
        assert math.gcd(phat, 4 * qhat) == 1

        h = math.gcd(qn, qp)
        u, vv = qn // h, qp // h
        x = 9 * pp * u - pn * vv
        ell = math.gcd(x, 8 * h * u * vv)
        assert math.gcd(u, vv) == 1
        assert raw_r == h * x
        assert k == h * ell
        assert math.gcd(x, u) == 1
        assert 9 % math.gcd(x, vv) == 0
        assert v2(h) == 1
        assert x % 2 == 1
        assert (9 * (h // 2)) % ell == 0
        assert 9 * h * h * qhat >= 16 * qn * qp
        assert h * qhat <= 8 * qn * qp

        # Exact primewise quotient identity, checked from raw coefficients.
        raw_qn = (2 * n + 2) * (2 * n + 1) * abs(evens[n])
        raw_pn = abs(evens[n + 1])
        raw_qp = (2 * n + 4) * (2 * n + 3) * abs(evens[n + 1])
        raw_pp = abs(evens[n + 2])
        assert qn == raw_qn // math.gcd(raw_qn, raw_pn)
        assert qp == raw_qp // math.gcd(raw_qp, raw_pp)

        if n in (1, 2, 3, 10, 30, 60, 120):
            row_checks.append({
                "N": n,
                "P_N": str(pn),
                "Q_N": str(qn),
                "G_N": str(gn),
                "D_N": str(det),
                "h_N": str(h),
                "K_N": str(k),
                "P_hat": str(phat),
                "Q_hat": str(qhat),
                "L_N": str(ell),
            })

    # Exhaustive bounded audit of the fixed-field content lemma in its
    # rational-integer specialization.  Algebraic prime ideals are covered
    # in the source by the same valuation argument.
    content_cases = 0
    max_content_ratio = Fraction(0)
    for p in range(1, 31):
        for q in range(1, 31):
            if math.gcd(p, q) != 1:
                continue
            for m in range(1, 9):
                for theta in range(-8, 9):
                    a0 = 4 * m * m * q - p * theta * theta
                    a1 = 2 * p * m * theta
                    a2 = -p * m * m
                    content = math.gcd(math.gcd(abs(a0), abs(a1)), abs(a2))
                    assert content > 0
                    assert (4 * m**4) % content == 0
                    assert m * m * a0 - theta * theta * a2 == 4 * m**4 * q
                    max_content_ratio = max(
                        max_content_ratio, Fraction(content, 4 * m**4)
                    )
                    content_cases += 1

    # Exhaustive valuation-ledger audit of equation (42).
    valuation_cases = 0
    for x0 in range(8):
        for y0 in range(8):
            for aa in range(8):
                for z0 in range(8):
                    qv = max(x0 - y0, 0)
                    qpv = max(aa + y0 - z0, 0)
                    hv = min(qv, qpv)
                    # Model the valuations with powers of a formal prime.
                    prime = 3
                    q_model = prime**qv
                    qp_model = prime**qpv
                    h_model = math.gcd(q_model, qp_model)
                    observed_hv = 0
                    while h_model % prime == 0:
                        observed_hv += 1
                        h_model //= prime
                    assert observed_hv == hv
                    valuation_cases += 1

    # Source equation tags and byte hygiene.
    source_text = SOURCE.read_text(encoding="utf-8")
    tags = [int(x) for x in re.findall(r"\\tag\{(\d+)\}", source_text)]
    assert tags == list(range(1, 44)), tags
    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__).resolve())
    assert source_control["clean"] and script_control["clean"]
    assert "No finite data" in source_text
    assert "No such theorem is asserted here" in source_text

    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_GUARD_KIB, peak_rss_kib

    result = {
        "schema": "root_unity_quadratic_two_regime_canonical_certificate/v1",
        "checked_utc": "2026-08-27",
        "claim_scope": {
            "all_parameter_proofs_in_source": True,
            "finite_grid_is_formula_audit_only": True,
            "classification_of_e_plus_pi": False,
            "growing_two_row_weights_classified": False,
        },
        "dependencies": dependency_checks,
        "formal_identities": {
            "aligned_constant_cancellation": str(sp.expand(Qp * C - Q * Cp)),
            "aligned_quadratic_cancellation": str(sp.expand(Pp * C - P * Cp)),
            "resultant_in_U": str(res_u),
            "resultant_in_T": str(res_t),
            "product_coefficients_descending": [str(x) for x in product.all_coeffs()],
        },
        "pole_cancellation": {
            "base3_coefficient": str(pole3),
            "base5_coefficient": str(pole5),
            "unique_fixed_weight_relation": "b = -9*a",
            "richardson_base5_raw_coefficient": int(richardson_5),
            "richardson_base5_normalized_coefficient": str(normalized_richardson_5),
        },
        "threshold_ledger": threshold_ledger,
        "exact_euler_grid": {
            "N_min": 1,
            "N_max": grid_max_n,
            "all_checks_passed": True,
            "selected_rows": row_checks,
        },
        "content_lemma_grid": {
            "P_max": 30,
            "Q_max": 30,
            "m_max": 8,
            "theta_abs_max": 8,
            "cases": content_cases,
            "max_content_over_4m4": str(max_content_ratio),
            "all_checks_passed": True,
        },
        "valuation_ledger_grid": {
            "coordinate_max": 7,
            "cases": valuation_cases,
            "all_checks_passed": True,
        },
        "source_audit": {
            "equation_tags": tags,
            "equation_tags_contiguous_1_through_43": True,
            "source_control": source_control,
            "script_control": script_control,
        },
        "resource_audit": {
            "limit_kib": RSS_GUARD_KIB,
            "guard_passed": True,
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "ok",
        "output": str(OUTPUT.relative_to(ROOT)),
        "source_equations": len(tags),
        "euler_rows_checked": grid_max_n,
        "content_cases": content_cases,
        "valuation_cases": valuation_cases,
        "peak_rss_kib": peak_rss_kib,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
