#!/usr/bin/env python3
"""Deterministic certificate for Item 315's endpoint-resultant arithmetic.

The symbolic part proves sign/nonvanishing from the already certified
order-three recurrence, records the exact Hadamard-diagonal identity, and
splits the two residue rays into their natural cubic norm factors.  Bounded
rows only replay the formulas and provide exact counterexamples to one
specific strong-divisibility ansatz; they are not density evidence.
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
    "scripts/item309_j2_l_second_branch_bridge_certificate.py":
        "bd4dc6b96d8af44cb463a141fad14739909ad645c3a9b6067c4c653580dad6b4",
    "results/item309_j2_l_second_branch_bridge_certificate.json":
        "b44200c2e3fe16fca4518e45b40540230db43deee496d84c43336907ef304c5a",
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


i237 = load("item315_i237", "scripts/item237_j1_algebraic_residual_certificate.py")
i309 = load("item315_i309", "scripts/item309_j2_l_second_branch_bridge_certificate.py")
ITEM250 = json.loads(
    (ROOT / "results/item250_j2_ordinary_phase_certificate.json").read_text(
        encoding="utf-8"
    )
)


def encode(value: F) -> list[int]:
    return [value.numerator, value.denominator]


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def norm_value(r: int, minus: list[F]) -> F:
    a_value = minus[r]
    b_value = i237.lagrange_coefficient(r)
    return (
        F(18**3) * a_value**3
        + F(11**3 * 2 ** (2 * r + 2)) * b_value**3
    )


def recurrence_sign_theorem() -> dict[str, Any]:
    """Certify the all-index sign induction from factored recurrence data."""
    expected_signs = [-1, -1, -1, 1]
    factor_rows = []
    for shift, (scalar, roots, core) in enumerate(i237.RECURRENCE_FACTORS):
        scalar_sign = 1 if scalar > 0 else -1
        if scalar_sign != expected_signs[shift]:
            raise AssertionError((shift, scalar))
        if not all(numerator < 0 and denominator > 0
                   for numerator, denominator in roots):
            raise AssertionError((shift, roots))
        if not all(coefficient > 0 for coefficient in core):
            raise AssertionError((shift, core))
        # Every linear factor is denominator*h-numerator and every core
        # polynomial has positive coefficients.  Its sign on h>0 is exact.
        factor_rows.append({
            "shift": shift,
            "sign_for_h_positive": scalar_sign,
            "linear_factors_positive": True,
            "core_coefficients_positive": True,
            "polynomial_degree": len(i237.recurrence_polynomials()[shift]) - 1,
        })

    minus = i309.branch_coefficients(17)
    initials: dict[str, Any] = {}
    for residue in (1, 5):
        indices = [residue + 6 * offset for offset in range(3)]
        a_values = [minus[index] for index in indices]
        b_values = [i237.lagrange_coefficient(index) for index in indices]
        if not all(value < 0 for value in a_values + b_values):
            raise AssertionError((residue, a_values, b_values))
        initials[str(residue)] = {
            "indices": indices,
            "a_initials": [encode(value) for value in a_values],
            "b_initials": [encode(value) for value in b_values],
        }

    return {
        "classification": "SYMBOLIC EXACT ALL n",
        "recurrence": "sum_(m=0)^3 p_m(r/2)*b_(r+6m)=0",
        "minus_branch_recurrence": (
            "sum_(m=0)^3 p_m(r/2)*16^(-m)*a_(r+6m)=0"
        ),
        "coefficient_signs_for_r_positive": factor_rows,
        "initials": initials,
        "induction": (
            "p_0,p_1,p_2<0 and p_3>0; three negative consecutive "
            "ray values force the fourth negative, and iteration proves "
            "a_(6n+e)<0 and b_(6n+e)<0 for e=1,5 and every n>=0"
        ),
        "conclusion": {
            "a": "a_(6n+e)<0 for e in {1,5}, n>=0",
            "b": "b_(6n+e)<0 for e in {1,5}, n>=0",
        },
    }


def norm_factorization_theorem() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT ALL n",
        "definitions": {
            "A_r": "18*a_r",
            "e=1": {
                "r": "6n+1",
                "k": "(2r+1)/3=4n+1",
                "B_r": "11*2^k*b_r",
                "delta": 2,
                "norm": "N_r=A_r^3+2*B_r^3=Norm_Q(cuberoot(2))/Q(A_r+B_r*cuberoot(2))",
            },
            "e=5": {
                "r": "6n+5",
                "k": "(2r+2)/3=4n+4",
                "B_r": "11*2^k*b_r",
                "delta": 1,
                "norm": "N_r=A_r^3+B_r^3",
                "rational_factorization": "(A_r+B_r)*(A_r^2-A_r*B_r+B_r^2)",
            },
        },
        "sign": (
            "A_r<0 and B_r<0 on both rays, hence N_r<0.  On e=5 the "
            "linear factor is negative and the quadratic factor is strictly positive."
        ),
        "characteristic_zero_zeros": [],
        "conclusion": "N_(6n+1) and N_(6n+5) are strictly negative for every n>=0",
        "old_resultant_warning": (
            "N_r is still exactly Item250's resultant after Item314's p-unit "
            "hypergeometric cube; this theorem cannot be booked as a new divisor"
        ),
    }


def factor_content_audit() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT ALL ACTUAL ROWS",
        "old_scale": "sigma_(e,n)=g_n*kappa_e/16^n",
        "old_resultant": "R_old=sigma_(e,n)^3*N_r",
        "all_row_unit": (
            "Item314 proves sigma_(e,n) is a p-unit for every actual "
            "p=2r+6s+3"
        ),
        "e=5_factor_scales": {
            "linear": "L_r+2^k*M_r=sigma_(5,n)*(A_r+B_r)",
            "quadratic": (
                "L_r^2-2^k*L_r*M_r+2^(2k)*M_r^2="
                "sigma_(5,n)^2*(A_r^2-A_r*B_r+B_r^2)"
            ),
        },
        "e=1_norm_scale": (
            "L_r+2^k*M_r*cuberoot(2)="
            "sigma_(1,n)*(A_r+B_r*cuberoot(2)); field norms multiply by sigma^3"
        ),
        "integer_clearers": {
            "H_r": "6^(r+3)*r!",
            "linear_e=5": "H_r*(A_r+B_r) is an integer",
            "quadratic_e=5": "H_r^2*(A_r^2-A_r*B_r+B_r^2) is an integer",
            "norm_e=1": "H_r^3*(A_r^3+2*B_r^3) is an integer",
            "unit": "p does not divide H_r because p>2r+3>r and p>3",
        },
        "certified_compulsory_content_after_item314": (
            "none beyond the displayed p-unit powers"
        ),
        "unsafe_division": (
            "no further same-index numerator gcd of A_r and B_r is divided: "
            "it has not been proved to be a p-unit on all actual rows"
        ),
        "capacity": "factor splitting and unit clearing create no new divisor and no booking",
    }


def diagonal_theorem() -> dict[str, Any]:
    return {
        "classification": "SYMBOLIC EXACT",
        "hadamard_identity": (
            "N(z)=18^3*(A hadamard A hadamard A)(z)+"
            "4*11^3*(C_+ hadamard C_+ hadamard C_+)(4z)"
        ),
        "constant_term_identity": (
            "N(z)=18^3*CT_(u,v) A(u)A(v)A(z/(uv))+"
            "4*11^3*CT_(u,v) C_+(u)C_+(v)C_+(4z/(uv))"
        ),
        "coefficient": "[z^r]N(z)=18^3*a_r^3+11^3*2^(2r+2)*b_r^3",
        "algebraicity_input": (
            "A and C_+ are the two certified local algebraic branches of "
            "Item237's curve"
        ),
        "closure": (
            "algebraic series are D-finite; finite products and diagonals "
            "of D-finite series are D-finite"
        ),
        "conclusion": (
            "N_r is P-recursive, and each arithmetic-ray subsequence "
            "N_(6n+1), N_(6n+5) is P-recursive"
        ),
        "operator_warning": (
            "P-recursiveness supplies no prime-factor localization or "
            "weighted zero-density theorem by itself"
        ),
    }


def character_projection_replay(minus: list[F]) -> dict[str, Any]:
    rows = []
    failures = []
    for hit in ITEM250["finite_actual_replay"]["cubic_hits"]:
        p = int(hit["p"])
        s = int(hit["s"])
        r = int(hit["r"])
        residue = r % 6
        a_value = minus[r]
        b_value = i237.lagrange_coefficient(r)
        aa = fmod(18 * a_value, p)
        if residue == 1:
            k = (2 * r + 1) // 3
            delta = 2
        elif residue == 5:
            k = (2 * r + 2) // 3
            delta = 1
        else:
            raise AssertionError((r, residue))
        bb = fmod(F(11 * 2**k) * b_value, p)
        t = pow(2, k + 2 * s, p)
        scaled_gate = (aa * t + bb) % p
        norm_mod = (aa**3 + delta * bb**3) % p
        if norm_mod != 0 or pow(t, 3, p) != pow(delta, -1, p):
            failures.append((p, s, r, norm_mod, t))
        row = {
            "p": p,
            "s": s,
            "r": r,
            "residue": residue,
            "k": k,
            "delta": delta,
            "A_mod_p": aa,
            "B_mod_p": bb,
            "t_mod_p": t,
            "t_cubed_mod_p": pow(t, 3, p),
            "scaled_gate_mod_p": scaled_gate,
            "norm_mod_p": norm_mod,
        }
        if residue == 5:
            linear = (aa + bb) % p
            quadratic = (aa * aa - aa * bb + bb * bb) % p
            if linear * quadratic % p != norm_mod:
                failures.append((p, "factorization"))
            row.update({
                "cubic_character_of_2": t,
                "rational_linear_factor_mod_p": linear,
                "rational_quadratic_factor_mod_p": quadratic,
                "selected_factor": "linear" if t == 1 else "one conjugate inside quadratic",
            })
        rows.append(row)
    if failures:
        raise AssertionError(failures)
    digest = hashlib.sha256()
    for row in rows:
        digest.update((json.dumps(row, sort_keys=True) + "\n").encode("utf-8"))
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "source_bound": "Item250 p<=401 resultant-hit census",
        "rows": rows,
        "resultant_hits": len(rows),
        "actual_scaled_gate_hits": sum(row["scaled_gate_mod_p"] == 0 for row in rows),
        "failures": failures,
        "row_stream_sha256": digest.hexdigest(),
        "symbolic_projection": {
            "t": "2^(k+2s)",
            "relation": "t^3=delta^(-1) mod p",
            "gate": "2^k*G_(r,s)=A_r*t+B_r",
            "e=5": (
                "t=2^((p-1)/3) is a cubic character value; t=1 selects "
                "A+B, while t!=1 selects one conjugate factor of A^2-AB+B^2"
            ),
            "e=1": (
                "p=5 mod 6 and t is the unique cube root of 1/2 in F_p"
            ),
        },
    }


def factor_support_examples(minus: list[F]) -> dict[str, Any]:
    """Exact selected-factor examples; they disprove empty-factor claims only."""
    requested = [
        (2281, 378, 5, "e=5 selected rational linear factor"),
        (271, 7, 113, "e=5 selected conjugate inside rational quadratic factor"),
        (383, 27, 109, "e=1 selected Q(cuberoot(2)) norm component"),
    ]
    available = {
        (int(row["p"]), int(row["s"]), int(row["r"]))
        for row in ITEM250["explicit_counterexamples_to_sufficiency"]
    }
    available.update({
        (int(row["p"]), int(row["s"]), int(row["r"]))
        for row in ITEM250["finite_actual_replay"]["cubic_hits"]
    })
    rows = []
    for p, s, r, role in requested:
        if (p, s, r) not in available:
            raise AssertionError((p, s, r, "missing dependency row"))
        residue = r % 6
        a_value = minus[r]
        b_value = i237.lagrange_coefficient(r)
        aa = fmod(18 * a_value, p)
        if residue == 1:
            k = (2 * r + 1) // 3
            delta = 2
        else:
            k = (2 * r + 2) // 3
            delta = 1
        bb = fmod(F(11 * 2**k) * b_value, p)
        t = pow(2, k + 2 * s, p)
        gate = (aa * t + bb) % p
        norm = (aa**3 + delta * bb**3) % p
        if gate != 0 or norm != 0:
            raise AssertionError((p, s, r, gate, norm))
        row = {
            "p": p,
            "s": s,
            "r": r,
            "role": role,
            "A_mod_p": aa,
            "B_mod_p": bb,
            "t_mod_p": t,
            "scaled_gate_mod_p": gate,
            "norm_mod_p": norm,
        }
        if residue == 5:
            linear = (aa + bb) % p
            quadratic = (aa * aa - aa * bb + bb * bb) % p
            row["linear_mod_p"] = linear
            row["quadratic_mod_p"] = quadratic
            if p == 2281 and not (t == 1 and linear == 0 and quadratic != 0):
                raise AssertionError(row)
            if p == 271 and not (t != 1 and linear != 0 and quadratic == 0):
                raise AssertionError(row)
        rows.append(row)
    return {
        "classification": "EXACT COUNTEREXAMPLES TO UNIVERSAL FACTOR EXCLUSION",
        "rows": rows,
        "conclusion": (
            "both rational e=5 factors, and the e=1 pure-cubic norm, can "
            "contain an actual selected tied prime"
        ),
        "warning": (
            "three exact rows prove only that no displayed factor is universally "
            "absent; they give no positive density or Chebyshev-mass theorem"
        ),
    }


def odd_part(value: int) -> int:
    value = abs(value)
    if value == 0:
        return 0
    while value % 2 == 0:
        value //= 2
    return value


def primitive_odd_norm(r: int, minus: list[F]) -> tuple[int, dict[str, Any]]:
    a_value = minus[r]
    b_value = i237.lagrange_coefficient(r)
    denominator = math.lcm(a_value.denominator, b_value.denominator)
    a_integer = a_value.numerator * (denominator // a_value.denominator)
    b_integer = b_value.numerator * (denominator // b_value.denominator)
    content = math.gcd(abs(a_integer), abs(b_integer))
    u_value = a_integer // content
    v_value = b_integer // content
    raw = 18**3 * u_value**3 + 11**3 * 2 ** (2 * r + 2) * v_value**3
    answer = odd_part(raw)
    return answer, {
        "r": r,
        "common_denominator": denominator,
        "coefficient_content": content,
        "primitive_a": u_value,
        "primitive_b": v_value,
        "primitive_odd_norm": answer,
    }


def strong_divisibility_no_go(minus: list[F]) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for residue in (1, 5):
        values = []
        metadata = []
        for n in range(7):
            value, row = primitive_odd_norm(residue + 6 * n, minus)
            values.append(value)
            row["n"] = n
            metadata.append(row)
        common = math.gcd(values[1], values[2])
        if common != 1 or values[1] == 1:
            raise AssertionError((residue, values[1], values[2], common))
        digest = hashlib.sha256()
        for value in values:
            digest.update((str(value) + "\n").encode("ascii"))
        rows[str(residue)] = {
            "definition": (
                "clear the common denominator of (a_r,b_r), divide their "
                "integer gcd, form the norm, then remove its 2-part"
            ),
            "n_1_value": values[1],
            "n_2_value": values[2],
            "gcd_n_1_n_2": common,
            "strong_divisibility_prediction": "S_gcd(1,2)=S_1",
            "prediction_fails": True,
            "seven_value_stream_sha256": digest.hexdigest(),
            "rows": metadata,
        }
    return {
        "classification": "PROVED SCOPED NO-GO BY EXACT COUNTEREXAMPLES",
        "rays": rows,
        "conclusion": (
            "the most direct primitive odd norm on either ray is not a "
            "strong-divisibility sequence"
        ),
        "scope_warning": (
            "this rules out only the displayed ansatz.  The divided coefficient "
            "content is not proved to be a p-unit on all actual rows, so this "
            "primitive normalization cannot replace N_r in the collision gate"
        ),
    }


def finite_sign_replay(r_max: int, minus: list[F]) -> dict[str, Any]:
    rows = []
    failures = []
    for residue in (1, 5):
        n = 0
        while residue + 6 * n <= r_max:
            r = residue + 6 * n
            a_value = minus[r]
            b_value = i237.lagrange_coefficient(r)
            norm = norm_value(r, minus)
            if not (a_value < 0 and b_value < 0 and norm < 0):
                failures.append((residue, n, r))
            if residue == 1:
                k = (2 * r + 1) // 3
                delta = 2
            else:
                k = (2 * r + 2) // 3
                delta = 1
            aa = 18 * a_value
            bb = F(11 * 2**k) * b_value
            if norm != aa**3 + delta * bb**3:
                failures.append((residue, n, r, "factorization"))
            rows.append((residue, n, r, int(a_value < 0), int(b_value < 0),
                         int(norm < 0), abs(norm.numerator).bit_length()))
            n += 1
    if failures:
        raise AssertionError(failures)
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return {
        "classification": "EXACT FINITE REPLAY OF THE SYMBOLIC SIGN THEOREM",
        "r_max": r_max,
        "rows": rows,
        "failures": failures,
        "row_stream_sha256": digest.hexdigest(),
        "warning": "row signs do not prove the unbounded theorem; recurrence induction does",
    }


def method_no_go() -> dict[str, Any]:
    return {
        "classification": "PROVED SCOPED METHOD NO-GO",
        "comparison_sequence": "H_r=binomial(7r,r)",
        "properties": [
            "H_r is nonzero and first-order hypergeometric, hence P-recursive",
            "log H_r=O(r)",
            "every prime 6r<p<=7r divides H_r exactly once",
            (
                "restricting to p congruent to 2r+3 mod 6 makes each such p an "
                "actual tied-form prime p=2r+6s+3"
            ),
            (
                "the prime-number theorem in arithmetic progressions gives "
                "positive linear Chebyshev mass in that interval"
            ),
        ],
        "conclusion": (
            "P-recursiveness, exact nonvanishing, and O(r) individual height "
            "alone cannot imply thin prime support in the freely varying tied "
            "family (r,s)"
        ),
        "fixed_M_warning": (
            "this comparison is not a fixed-M capacity construction: it does not "
            "impose 2M=5r+14s+7 and therefore makes no claim that the 1/105 "
            "fixed-M ceiling is sharp"
        ),
        "remaining_needed_input": (
            "sequence-specific congruence, monodromy/Frobenius, or an average "
            "prime-incidence theorem for the actual G_(r,s) gate"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=131)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "work/item315_j2_resultant_arithmetic_certificate.json",
    )
    args = parser.parse_args()
    if args.r_max < 53 or args.r_max > 161:
        raise ValueError("r_max must lie in [53,161]")
    maximum = max(args.r_max, max(
        int(row["r"]) for row in ITEM250["finite_actual_replay"]["cubic_hits"]
    ))
    minus = i309.branch_coefficients(maximum)
    result = {
        "schema": "item315-j2-resultant-arithmetic-v1",
        "dependencies": DEPENDENCIES,
        "recurrence_sign_theorem": recurrence_sign_theorem(),
        "norm_factorization_theorem": norm_factorization_theorem(),
        "factor_content_audit": factor_content_audit(),
        "hadamard_diagonal_theorem": diagonal_theorem(),
        "character_projection_replay": character_projection_replay(minus),
        "factor_support_examples": factor_support_examples(minus),
        "strong_divisibility_no_go": strong_divisibility_no_go(minus),
        "finite_sign_replay": finite_sign_replay(args.r_max, minus),
        "method_no_go": method_no_go(),
        "capacity": {
            "old_resultant_rebooked": False,
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "new_capacity_reduction": 0,
            "new_booking": 0,
            "closed_open_sublemma": "N_(6n+e) is never zero over Q",
            "smallest_open_theorem": (
                "weighted logarithmic zero density for the actual unit-cleared "
                "gate 18*2^(2s)*a_(6n+e)+11*b_(6n+e) mod p under the "
                "fixed-M relation 2M=5r+14s+7"
            ),
        },
        "strict_labels": {
            "PROVED": [
                "a_(6n+e)<0 and b_(6n+e)<0 on both rays by recurrence induction",
                "N_(6n+e)<0, so exact characteristic-zero zero rows do not exist",
                "the raywise cubic norm/factorization and Hadamard-diagonal identity",
                "P-recursiveness of N and both ray subsequences",
                "the scoped strong-divisibility and abstract-method no-go statements",
            ],
            "EXACT_FINITE_ONLY": [
                "the declared sign/factorization replay",
                "the Item250 p<=401 character-projection replay",
            ],
            "OPEN": [
                "weighted zero density for N or the stronger actual gate",
                "any sequence-specific thin-support or average Frobenius theorem",
                "actual residual-period incidence and any ordinary-j2 capacity reduction",
            ],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "output": str(args.output),
        "sign_failures": len(result["finite_sign_replay"]["failures"]),
        "character_failures": len(result["character_projection_replay"]["failures"]),
        "actual_gate_hits_in_old_resultant_census":
            result["character_projection_replay"]["actual_scaled_gate_hits"],
    }, indent=2))


if __name__ == "__main__":
    main()
