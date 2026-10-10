#!/usr/bin/env python3
"""Deterministic certificate for Item 318's actual-period incidence.

The theorem is exterior algebra over an arbitrary field, specialized to the
already certified ordinary-j=2 connection plane.  Bounded actual rows replay
the identities only; they are not used as density evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEPENDENCIES = {
    "scripts/item250_j2_ordinary_phase_certificate.py":
        "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce",
    "results/item250_j2_ordinary_phase_certificate.json":
        "6f8d0165448dd8949436649e2824a14578c1bce08e8875a6fd88f770c72cb5e3",
    "scripts/item251_j2_exceptional_period_certificate.py":
        "a255ebeef0d73ef82bc6197a1f3f88c9522b6d8408f449971911702842c92f61",
    "results/item251_j2_exceptional_period_certificate.json":
        "343cf92daf3acfabee68d09885810f71cd3b582cea08801a548c9b293676d697",
    "scripts/item291_j2_connection_plane_certificate.py":
        "5c86001827b0012605563b04dafc5f157f27fddf2f1625254e9196bc0de8c2df",
    "results/item291_j2_connection_plane_certificate.json":
        "831cd4c74b10555c261eccebef7fd9c5a871bcef97a43d52e77c731b9b7188b5",
    "scripts/item314_j2_two_branch_gate_certificate.py":
        "cc5f155e5f3248c500cd2101e401c25cec37ce43b31fbb4582843fc33a9b2f0e",
    "results/item314_j2_two_branch_gate_certificate.json":
        "77de2dd46726a5a48e9adc4e40f96341d5da6c8db304d79f0ef8eeb7807245b1",
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


i250 = load("item318_i250", "scripts/item250_j2_ordinary_phase_certificate.py")
i251 = load("item318_i251", "scripts/item251_j2_exceptional_period_certificate.py")
ITEM250 = json.loads(
    (ROOT / "results/item250_j2_ordinary_phase_certificate.json").read_text(
        encoding="utf-8"
    )
)


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def det(left: tuple[F, F], right: tuple[F, F]) -> F:
    return left[0] * right[1] - left[1] * right[0]


def coefficients(data: dict[str, Any]) -> dict[str, Any]:
    f = tuple(data["st"])
    b = (data["x0"][1], data["x1"][1])
    d = (data["x0"][2], data["x1"][2])
    ell = det(f, b)
    m_value = det(f, d)
    c_minor = det(b, d)
    return {"f": f, "b": b, "d": d, "ell": ell, "m": m_value, "C": c_minor}


def actual_period(r: int, s: int, data: dict[str, Any]) -> dict[str, Any]:
    kappa, _ = i250.reversal_certificate(r, data)
    beta = i251.beta_fraction(s)
    a_value = i251.a_direct(s)
    tau = i251.tau_fraction(r, s)
    z_value = beta * (F(9, 2) * kappa * a_value - tau)
    return {
        "kappa": kappa,
        "B": beta,
        "A": a_value,
        "tau": tau,
        "Z": z_value,
    }


def algebra_theorem() -> dict[str, Any]:
    """Record and directly test the universal polynomial identities."""
    test_rows = [
        ((F(1), F(2)), (F(3), F(5)), (F(7), F(11)), F(13), F(17)),
        ((F(2), F(-1)), (F(4), F(3)), (F(-5), F(8)), F(-7), F(9)),
        ((F(0), F(1)), (F(1), F(0)), (F(2), F(0)), F(5), F(-3)),
    ]
    for f, b, d, z_value, c_value in test_rows:
        ell, m_value, c_minor = det(f, b), det(f, d), det(b, d)
        g = (
            f[0] * z_value + 9 * c_value * b[0] - 11 * d[0],
            f[1] * z_value + 9 * c_value * b[1] - 11 * d[1],
        )
        d_gate = 9 * c_value * ell - 11 * m_value
        e_b = ell * z_value + 11 * c_minor
        e_d = m_value * z_value + 9 * c_value * c_minor
        if det(f, g) != d_gate:
            raise AssertionError("D identity")
        if det(g, b) != e_b or det(g, d) != e_d:
            raise AssertionError("exterior identity")
        if 11 * e_d - 9 * c_value * e_b != -d_gate * z_value:
            raise AssertionError("syzygy")

    # Ambient independence of C from (ell,m): with f=(1,0),
    # b=(x,ell), d=(y,m), C=x*m-ell*y can vary at fixed ell,m.
    fixed = []
    for x_value, y_value in ((0, 0), (1, 0), (0, 1)):
        f = (F(1), F(0))
        b = (F(x_value), F(2))
        d = (F(y_value), F(3))
        fixed.append((det(f, b), det(f, d), det(b, d)))
    if {pair[:2] for pair in fixed} != {(F(2), F(3))}:
        raise AssertionError(fixed)
    if len({pair[2] for pair in fixed}) != 3:
        raise AssertionError(fixed)

    # E_b is not a consequence of D in the universal connection plane.
    # At c=1, f=(1,0), b=(0,1), d=(0,9/11) gives D=0 and E_b=Z.
    independent_rows = []
    for z_value in (F(0), F(1)):
        f, b, d, c_value = (F(1), F(0)), (F(0), F(1)), (F(0), F(9, 11)), F(1)
        ell, m_value, c_minor = det(f, b), det(f, d), det(b, d)
        d_gate = 9 * c_value * ell - 11 * m_value
        e_b = ell * z_value + 11 * c_minor
        if d_gate != 0 or e_b != z_value:
            raise AssertionError((z_value, d_gate, e_b))
        independent_rows.append({"Z": int(z_value), "D": int(d_gate), "E_b": int(e_b)})

    return {
        "classification": (
            "SYMBOLIC EXACT: IDENTITIES OVER EVERY COMMUTATIVE RING; "
            "RANK AND CHART EQUIVALENCES OVER FIELDS"
        ),
        "definitions": {
            "g": "f*Z+9*c*b-11*d",
            "ell": "det(f,b)",
            "m": "det(f,d)",
            "C": "det(b,d)",
            "D": "det(f,g)=9*c*ell-11*m",
            "E_b": "det(g,b)=ell*Z+11*C",
            "E_d": "det(g,d)=m*Z+9*c*C",
        },
        "syzygy": "11*E_d-9*c*E_b=-D*Z",
        "nondegenerate_chart": {
            "hypothesis": "D=0 and ell!=0",
            "formal_value": "Z_form=-11*C/ell",
            "collision_equivalence": "g=0 iff E_b=0",
            "division_free_actual_condition": (
                "ell*B_s*((9*kappa_r/2)*A_s-tau_(r,s))+11*C=0"
            ),
        },
        "second_nondegenerate_chart": {
            "hypothesis": "D=0 and m!=0",
            "formal_value": "Z_form=-9*c*C/m",
            "collision_equivalence": "g=0 iff E_d=0",
            "division_free_actual_condition": (
                "m*B_s*((9*kappa_r/2)*A_s-tau_(r,s))+9*c*C=0"
            ),
        },
        "rank_two_chart": (
            "if span(f,b,d) has rank 2, then g=0 iff D=E_b=E_d=0; "
            "on D=0 only one of E_b,E_d is independent"
        ),
        "rank_one_no_go": (
            "if span(f,b,d) has rank at most 1, every pairwise exterior "
            "minor vanishes for all Z and c, so no determinant-only tower "
            "can distinguish g=0 from a nonzero collinear g"
        ),
        "ambient_transversality": {
            "statement": "C is not a formal function of ell and m in the universal 2-by-3 plane",
            "fixed_ell_m_examples": [
                [int(row[0]), int(row[1]), int(row[2])] for row in fixed
            ],
            "warning": "this is not arithmetic independence on the actual (r,s)-family",
        },
        "independence_on_D_zero": {
            "examples": independent_rows,
            "conclusion": "E_b is not in the universal ideal generated by D",
            "logical_direction": "an original collision g=0 always forces D=E_b=E_d=0",
            "warning": "universal independence is not a fixed-M weighted-support theorem",
        },
        "characteristic_11_chart": (
            "at p=11, D=0 forces ell=0 because 9*c is a unit; E_b is then "
            "automatic and E_d is the surviving exterior condition.  Thus the "
            "m-chart covers the only exceptional coefficient characteristic"
        ),
    }


def clearing_theorem() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT ALL ACTUAL ROWS",
        "definition": (
            "Q_(r,s)=6 times the product of the reduced denominators of "
            "f_0,f_1,b_0,b_1,d_0,d_1,B_s,kappa_r,tau_(r,s)"
        ),
        "unit": (
            "Items250 and 251 prove that every displayed denominator is a "
            "p-unit on p=2r+6s+3; every actual prime has p>3, so 6 is a p-unit"
        ),
        "integer_clearings": {
            "Q^2*D": "integer",
            "Q^4*E_b_actual": "integer",
            "Q^4*E_d_actual": "integer",
        },
        "equivalence": (
            "because p does not divide Q, reduction of a cleared integer "
            "vanishes mod p exactly when the corresponding rational does"
        ),
        "important_chart_rule": (
            "the certified condition is ell*Z_actual+11*C; it never divides "
            "by ell, so rows with p dividing ell remain in scope"
        ),
    }


def denominator_clearer(values: list[F]) -> int:
    out = 6
    for value in values:
        out *= value.denominator
    return out


def replay_row(prime: int, s: int, r: int) -> dict[str, Any]:
    data = i250.phase_data(r)
    phase = i250.evaluate_phase_row(prime, s, data)
    coeff = coefficients(data)
    period = actual_period(r, s, data)
    f = coeff["f"]
    b = coeff["b"]
    d = coeff["d"]
    ell, m_value, c_minor = coeff["ell"], coeff["m"], coeff["C"]
    z_value = period["Z"]
    c_value = F(2 ** (2 * s))
    g = (
        f[0] * z_value + 9 * c_value * b[0] - 11 * d[0],
        f[1] * z_value + 9 * c_value * b[1] - 11 * d[1],
    )
    d_gate = 9 * c_value * ell - 11 * m_value
    e_b = ell * z_value + 11 * c_minor
    e_d = m_value * z_value + 9 * c_value * c_minor

    if fmod(z_value, prime) != (
        9 * fmod(period["kappa"], prime) * phase["e"] - phase["f"]
    ) % prime:
        raise AssertionError((prime, "period"))
    if tuple(fmod(value, prime) for value in g) != (phase["g0"], phase["g1"]):
        raise AssertionError((prime, "gates"))
    if fmod(d_gate, prime) != phase["linear"]:
        raise AssertionError((prime, "D"))
    if fmod(e_b, prime) != (
        phase["g0"] * fmod(b[1], prime) - phase["g1"] * fmod(b[0], prime)
    ) % prime:
        raise AssertionError((prime, "E_b"))
    if fmod(e_d, prime) != (
        phase["g0"] * fmod(d[1], prime) - phase["g1"] * fmod(d[0], prime)
    ) % prime:
        raise AssertionError((prime, "E_d"))
    if 11 * e_d - 9 * c_value * e_b != -d_gate * z_value:
        raise AssertionError((prime, "syzygy"))

    q_value = denominator_clearer(
        [*f, *b, *d, period["B"], period["kappa"], period["tau"]]
    )
    if q_value % prime == 0:
        raise AssertionError((prime, "nonunit clearer"))
    if (q_value**2 * d_gate).denominator != 1:
        raise AssertionError((prime, "D clearing"))
    if (q_value**4 * e_b).denominator != 1 or (q_value**4 * e_d).denominator != 1:
        raise AssertionError((prime, "E clearing"))

    d_zero = fmod(d_gate, prime) == 0
    ell_nonzero = fmod(ell, prime) != 0
    actual_collision = phase["g0"] == phase["g1"] == 0
    e_b_zero = fmod(e_b, prime) == 0
    if d_zero and ell_nonzero and (e_b_zero != actual_collision):
        raise AssertionError((prime, "chart equivalence"))

    return {
        "p": prime,
        "s": s,
        "r": r,
        "D_mod_p": fmod(d_gate, prime),
        "ell_mod_p": fmod(ell, prime),
        "m_mod_p": fmod(m_value, prime),
        "C_mod_p": fmod(c_minor, prime),
        "E_b_mod_p": fmod(e_b, prime),
        "E_d_mod_p": fmod(e_d, prime),
        "g0": phase["g0"],
        "g1": phase["g1"],
        "actual_collision": actual_collision,
        "clearer_is_p_unit": True,
        "chart_equivalence_checked": bool(d_zero and ell_nonzero),
    }


def finite_replay() -> dict[str, Any]:
    rows: set[tuple[int, int, int]] = set()
    for row in ITEM250["finite_actual_replay"]["linear_hits"]:
        rows.add((row["p"], row["s"], row["r"]))
    for row in ITEM250["explicit_counterexamples_to_sufficiency"]:
        if row["kind"] == "linear":
            rows.add((row["p"], row["s"], row["r"]))
    replays = [replay_row(*row) for row in sorted(rows)]
    if not all(row["D_mod_p"] == 0 for row in replays):
        raise AssertionError("declared determinant-zero rows")

    rank_zero_f = 0
    determinant_zero = 0
    determinant_zero_ell_zero = 0
    actual_collisions = 0
    cache: dict[int, dict[str, Any]] = {}
    for prime, s, r in i250.actual_rows(401):
        data = cache.setdefault(r, i250.phase_data(r))
        phase = i250.evaluate_phase_row(prime, s, data)
        coeff = coefficients(data)
        f_zero = all(fmod(value, prime) == 0 for value in coeff["f"])
        if f_zero:
            rank_zero_f += 1
        if phase["linear"] == 0:
            determinant_zero += 1
            if fmod(coeff["ell"], prime) == 0:
                determinant_zero_ell_zero += 1
        if phase["g0"] == phase["g1"] == 0:
            actual_collisions += 1

    stream = json.dumps(replays, sort_keys=True, separators=(",", ":")).encode()
    return {
        "classification": "EXACT FINITE ONLY / DIAGNOSTIC",
        "declared_D_zero_rows": replays,
        "declared_row_count": len(replays),
        "declared_row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "bounded_actual_census": {
            "prime_max": 401,
            "D_zero_rows": determinant_zero,
            "D_zero_and_ell_zero_rows": determinant_zero_ell_zero,
            "f_zero_rows": rank_zero_f,
            "actual_collision_rows": actual_collisions,
        },
        "warning": (
            "these counts verify charts and known false positives only; they "
            "are not an asymptotic or weighted-density statement"
        ),
    }


def capacity_audit() -> dict[str, Any]:
    return {
        "classification": "PROVED ACCOUNTING / NO NEW BOUND",
        "fixed_M_relation": "2*M=5*r+14*s+7",
        "retained_branch_ceiling_per_6M": "1/105",
        "role": "Closer condition internal to the already retained ordinary-j=2 branch",
        "what_is_new": (
            "after D=0, the actual period supplies one division-free transverse "
            "condition on the rank-two chart"
        ),
        "what_is_not_new": [
            "the Item250/314 endpoint determinant or resultant",
            "either cubic-character component counted by Item315",
            "a second independent exterior condition on D=0",
            "a weighted zero-density theorem on the fixed-M slices",
        ],
        "admission_decision": (
            "retain E_b as the exact incidence target, but do not expand through "
            "height or recurrence fitting until a fixed-M weighted support theorem is available"
        ),
        "new_capacity_reduction": 0,
        "new_booking": 0,
    }


def build() -> dict[str, Any]:
    return {
        "item": 318,
        "schema": "item318-j2-actual-period-plucker-certificate-v1",
        "scope": "actual-period incidence after the ordinary-j=2 determinant gate",
        "dependencies": DEPENDENCIES,
        "algebra_theorem": algebra_theorem(),
        "p_unit_clearing": clearing_theorem(),
        "finite_replay": finite_replay(),
        "capacity": capacity_audit(),
        "strict_labels": {
            "PROVED": [
            "the three Plucker identities and their exact syzygy",
                "both nondegenerate-chart formal values and division-free actual-period equivalences",
                "logical necessity and universal independence of the transverse condition on D=0",
                "the rank-at-most-one determinant-only no-go",
                "the all-row p-unit integer clearing",
                "zero capacity booking",
            ],
            "EXACT_FINITE_ONLY": [
                "the declared determinant-zero replay and p<=401 chart census"
            ],
            "OPEN": [
                "weighted zero density for the cleared actual-period residual on fixed-M slices",
                "arithmetic independence of C on the actual family",
                "a non-exterior coordinate condition on the rank-at-most-one chart",
                "any reduction of the 1/105 ceiling",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "item318_j2_actual_period_plucker_certificate.json")
    args = parser.parse_args()
    result = build()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "sha256": sha256(args.output),
        "declared_rows": result["finite_replay"]["declared_row_count"],
        "new_booking": result["capacity"]["new_booking"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
