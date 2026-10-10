#!/usr/bin/env python3
"""Deterministic certificate for Item 314's unit-cleared two-branch gate.

The symbolic theorem is obtained from Items 250, 306, and 309.  This
checker verifies all dependency hashes, the universal 18:11 normalization,
the endpoint-cubic norm/resultant identity, exact coefficient formulas, and
a bounded replay of all six structurally singular recurrence layers.  The
bounded rows are implementation checks only.
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
    "scripts/item309_j2_l_second_branch_bridge_certificate.py":
        "bd4dc6b96d8af44cb463a141fad14739909ad645c3a9b6067c4c653580dad6b4",
    "results/item309_j2_l_second_branch_bridge_certificate.json":
        "b44200c2e3fe16fca4518e45b40540230db43deee496d84c43336907ef304c5a",
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


i237 = load("item314_i237", "scripts/item237_j1_algebraic_residual_certificate.py")
i250 = load("item314_i250", "scripts/item250_j2_ordinary_phase_certificate.py")
i309 = load("item314_i309", "scripts/item309_j2_l_second_branch_bridge_certificate.py")


MU = {1: F(-729, 50), 5: F(6377292, 41405)}
LAMBDA = {1: F(-891, 100), 5: F(3897234, 41405)}
KAPPA = {1: F(-81, 100), 5: F(354294, 41405)}


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


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def gauge_ratio(r: int) -> F:
    return F(
        r * (r + 6) * (2 * r + 9) ** 2 * (2 * r + 15) ** 2,
        78732 * (r + 1) ** 2 * (r + 2) * (r + 4) * (r + 5) ** 2,
    )


def gauge_value(residue: int, n: int) -> F:
    value = F(1)
    for step in range(n):
        value /= gauge_ratio(residue + 6 * step)
    return value


def universal_normalization_theorem() -> dict[str, Any]:
    rows = []
    for residue in (1, 5):
        if MU[residue] != 18 * KAPPA[residue]:
            raise AssertionError((residue, "mu"))
        if LAMBDA[residue] != 11 * KAPPA[residue]:
            raise AssertionError((residue, "lambda"))
        rows.append({
            "residue": residue,
            "mu": str(MU[residue]),
            "lambda": str(LAMBDA[residue]),
            "kappa": str(KAPPA[residue]),
            "mu_over_lambda": "18/11",
        })
    return {
        "classification": "SYMBOLIC EXACT",
        "rows": rows,
        "universal_gate": "G_(r,s)=18*2^(2s)*a_r+11*b_r",
        "scale": "D_(r,s)=g_n*kappa_e*G_(r,s)/16^n",
        "branch_coefficients": {
            "a_r": "[X^r] A(X), the Item309 y=-1 branch",
            "b_r": "[x^r] C_+(x), the Item237 y=0 branch",
        },
        "cleared_lagrange_formula": (
            "r*G=18*2^(2s)*[z^(r-1)]A'(z)*((1+z^2)^(2/3)/(1-z))^r"
            "+11*[y^(r-1)]C_+'(y)*(Q(y)^(2/3)/(1+y))^r"
        ),
    }


def symbolic_coefficient_formula() -> dict[str, Any]:
    """Verify the two rational derivatives used in the p-integral formula."""
    mul = i237.multiply
    add = i237.add
    scale = i237.scale
    deriv = i237.derivative
    power = i237.power

    plus_numerator = add(
        mul(deriv(i237.N), i237.D),
        scale(mul(i237.N, deriv(i237.D)), F(-3)),
    )
    plus_expected = scale(
        mul(
            mul([F(2), F(1)], [F(2), F(2), F(1)]),
            [F(120), F(292), F(388), F(352), F(316), F(151), F(16)],
        ),
        F(-12),
    )
    if plus_numerator != plus_expected:
        raise AssertionError("plus derivative factorization")

    minus_denominator = [F(-3), F(6), F(1), F(2)]
    minus_numerator = scale(
        mul(
            power([F(1), F(0), F(1)], 2),
            [F(9), F(-24), F(25), F(8)],
        ),
        F(6),
    )
    minus_derivative_numerator = add(
        mul(deriv(minus_numerator), minus_denominator),
        scale(mul(minus_numerator, deriv(minus_denominator)), F(-3)),
    )
    minus_expected = scale(
        mul(
            mul([F(1), F(1)], [F(1), F(0), F(1)]),
            [F(45), F(-33), F(-42), F(278), F(-199), F(55), F(16)],
        ),
        F(-12),
    )
    if minus_derivative_numerator != minus_expected:
        raise AssertionError("minus derivative factorization")

    return {
        "classification": "SYMBOLIC EXACT",
        "plus_derivative": (
            "C_+'(y)=-12*(y+2)*(y^2+2y+2)*"
            "(16y^6+151y^5+316y^4+352y^3+388y^2+292y+120)/"
            "(2y^3+7y^2+14y+6)^4"
        ),
        "minus_derivative": (
            "A'(z)=-12*(z+1)*(z^2+1)*"
            "(16z^6+55z^5-199z^4+278z^3-42z^2-33z+45)/"
            "(2z^3+z^2+6z-3)^4"
        ),
        "p_integral_gate": (
            "r*G=-12*(18*2^(2s)*[z^(r-1)]U_-(z)+"
            "11*[y^(r-1)]U_+(y)); all coefficient denominators are p-units"
        ),
        "global_integer_clearer": (
            "H_r=6^(r+3)*r!; H_r*a_r and H_r*b_r are integers, hence "
            "H_r*G_(r,s) is an integer"
        ),
        "clearer_proof": (
            "through degree d, inverse fourth-power coefficients have denominator "
            "dividing 6^(d+4), generalized 2r/3-power coefficients have denominator "
            "dividing 6^d*d!, and the negative integral powers are integral; "
            "Lagrange's factor 1/r is cleared by r!"
        ),
        "factorizations_verified": True,
    }


def p_unit_theorem() -> dict[str, Any]:
    return {
        "classification": "ALL ACTUAL ROWS",
        "row": "p=2r+6s+3, r=6n+e, e in {1,5}, s>=1",
        "gauge_product": "g_n=product_(j=0)^(n-1) 1/R(e+6j)",
        "past_step_bound": (
            "for t=e+6j<=r-6, every positive linear factor of R(t) is "
            "at most 2t+15<=2r+3<p; all denominator factors and 78732 "
            "are also p-units"
        ),
        "n_zero": "g_0=1",
        "kappa_units": {
            "e=1": "kappa=-3^4/(2^2*5^2); actual p>=11",
            "e=5": "kappa=2*3^11/(5*7^2*13^2); actual p>=19",
        },
        "branch_denominators": (
            "Lagrange denominators have prime factors <=r together with 2,3; "
            "p>2r+3, hence a_r and b_r are p-integral"
        ),
        "integer_clearer": (
            "H_r=6^(r+3)*r! clears a_r and b_r globally, and p does not divide H_r"
        ),
        "six_forward_singular_layers": [
            {"s": s, "forward_factor": f"2r+{6 * s + 3}=p"}
            for s in range(1, 7)
        ],
        "distinction": (
            "the six factors belong to the current forward recurrence coefficient; "
            "none occurs in the past-step value normalization g_n"
        ),
        "conclusion": "D_(r,s)=0 mod p iff G_(r,s)=0 mod p on every actual row",
    }


def exact_branch_values(maximum_r: int) -> tuple[list[F], dict[int, F]]:
    minus = i309.branch_coefficients(maximum_r)
    plus = {r: i237.lagrange_coefficient(r) for r in range(1, maximum_r + 1)}
    return minus, plus


def six_layer_replay(r_max: int) -> dict[str, Any]:
    minus, plus = exact_branch_values(r_max)
    rows = []
    failures = []
    for residue in (1, 5):
        n = 0
        while True:
            r = residue + 6 * n
            if r > r_max:
                break
            data = i250.phase_data(r)
            gauge = gauge_value(residue, n)
            for s in range(1, 7):
                p = 2 * r + 6 * s + 3
                if not is_prime(p):
                    continue
                c = 2 ** (2 * s)
                d_value = c * data["L"] + data["M"]
                g_value = 18 * c * minus[r] + 11 * plus[r]
                integer_clearer = 6 ** (r + 3) * math.factorial(r)
                integer_clear_ok = (
                    (integer_clearer * minus[r]).denominator == 1
                    and (integer_clearer * plus[r]).denominator == 1
                    and integer_clearer % p != 0
                )
                scale = gauge * KAPPA[residue] / (16**n)
                exact_ok = d_value == scale * g_value
                unit_ok = (
                    gauge.numerator % p != 0
                    and gauge.denominator % p != 0
                    and KAPPA[residue].numerator % p != 0
                    and KAPPA[residue].denominator % p != 0
                    and minus[r].denominator % p != 0
                    and plus[r].denominator % p != 0
                )
                d_mod = fmod(d_value, p)
                g_mod = fmod(g_value, p)
                equivalent = (d_mod == 0) == (g_mod == 0)
                structural = (2 * r + 6 * s + 3) % p == 0
                if not (exact_ok and unit_ok and integer_clear_ok
                        and equivalent and structural):
                    failures.append((residue, n, r, s, p, exact_ok, unit_ok,
                                     integer_clear_ok, equivalent, structural))
                rows.append((residue, n, r, s, p, d_mod, g_mod,
                             int(exact_ok), int(unit_ok), int(integer_clear_ok),
                             int(equivalent)))
            n += 1
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return {
        "classification": "EXACT FINITE REPLAY OF THE ALL-ROW UNIT THEOREM",
        "r_max": r_max,
        "prime_rows_in_layers_s_1_to_6": len(rows),
        "failures": failures,
        "row_stream_sha256": digest.hexdigest(),
        "rows": rows,
    }


def endpoint_norm_and_old_resultant(r_max: int) -> dict[str, Any]:
    minus, plus = exact_branch_values(r_max)
    rows = []
    failures = []
    exact_zero_rows = []
    max_height_bits_per_r = F(0)
    for residue in (1, 5):
        n = 0
        while True:
            r = residue + 6 * n
            if r > r_max:
                break
            data = i250.phase_data(r)
            gauge = gauge_value(residue, n)
            norm = 18**3 * minus[r]**3 + 11**3 * 2 ** (2 * r + 2) * plus[r]**3
            old = data["L"]**3 + F(2 ** (2 * r + 2)) * data["M"]**3
            scale = (gauge * KAPPA[residue] / (16**n)) ** 3
            ok = old == scale * norm
            if not ok:
                failures.append((residue, n, r))
            if norm == 0:
                exact_zero_rows.append((residue, n, r))
            height_bits = max(abs(norm.numerator).bit_length(), norm.denominator.bit_length())
            if r:
                max_height_bits_per_r = max(max_height_bits_per_r, F(height_bits, r))
            rows.append((residue, n, r, int(ok), int(norm == 0), height_bits))
            n += 1
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return {
        "classification": {
            "identity": "SYMBOLIC EXACT FROM THE TWO BRIDGES",
            "rows_and_height": "EXACT FINITE REPLAY ONLY",
        },
        "endpoint_relation": "2^(2r+2)*c^3=1 mod p",
        "norm": "N_r=18^3*a_r^3+11^3*2^(2r+2)*b_r^3",
        "forced_divisor": "G_(r,s)=0 mod p implies N_r=0 mod p",
        "old_resultant_identity": (
            "L_r^3+2^(2r+2)M_r^3="
            "(g_n*kappa_e/16^n)^3*N_r"
        ),
        "new_divisor": False,
        "reason": "N_r is exactly the p-unit normalization of Item250's old resultant",
        "r_max": r_max,
        "rows": rows,
        "failures": failures,
        "exact_zero_rows": exact_zero_rows,
        "row_stream_sha256": digest.hexdigest(),
        "finite_max_height_bits_per_r": str(max_height_bits_per_r),
        "height_warning": "the finite ratio is diagnostic and is not an asymptotic constant",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r-max", type=int, default=101)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "results" /
                        "item314_j2_two_branch_gate_certificate.json")
    args = parser.parse_args()
    if args.r_max < 29 or args.r_max > 199:
        raise ValueError("r_max must lie in [29,199]")
    result = {
        "schema": "item314-j2-two-branch-gate-v1",
        "dependencies": DEPENDENCIES,
        "universal_normalization": universal_normalization_theorem(),
        "symbolic_coefficient_formula": symbolic_coefficient_formula(),
        "all_row_p_unit_theorem": p_unit_theorem(),
        "six_singular_layer_replay": six_layer_replay(args.r_max),
        "endpoint_norm_and_resultant": endpoint_norm_and_old_resultant(args.r_max),
        "height_and_norm_no_go": {
            "classification": "SCOPED PROVED NO-GO FOR THE INDIVIDUAL-HEIGHT METHOD",
            "algebraic_height": (
                "Eisenstein global boundedness and a fixed convergence radius give "
                "h(a_r),h(b_r)=O(r), hence h(N_r)=O(r) when N_r is nonzero"
            ),
            "aggregate": (
                "summing the individual divisor bounds over linearly many r gives "
                "O(M^2), weaker than the already known O(M) raw cell ceiling"
            ),
            "coefficient_norm_warning": (
                "field norm of the algebraic generating-series values does not norm "
                "same-index coefficients: multiplication of series produces convolution"
            ),
            "conclusion": (
                "conjugate-branch norms provide no new weighted divisor and no "
                "ordinary-j2 capacity reduction"
            ),
        },
        "capacity": {
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "new_capacity_reduction": 0,
            "booking": 0,
            "smallest_open_theorem": (
                "weighted zero density for the actual unit-cleared coefficient "
                "G_(r,s)=18*2^(2s)*a_r+11*b_r"
            ),
        },
        "strict_labels": {
            "PROVED": [
                "the universal unit-cleared 18:11 gate on every actual row",
                "the exact rational-derivative and p-integral coefficient formula",
                "the distinction between fixed-value units and six forward singular layers",
                "the endpoint-cubic norm is exactly the old Item250 resultant",
                "the scoped individual-height and coefficientwise-norm no-go",
            ],
            "EXACT_FINITE_ONLY": [
                "the declared six-layer replay and height rows",
            ],
            "OPEN": [
                "weighted zero density for the actual two-branch coefficient",
                "the residual actual period incidence on gate-zero rows",
            ],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "six_layer_failures": len(result["six_singular_layer_replay"]["failures"]),
        "norm_failures": len(result["endpoint_norm_and_resultant"]["failures"]),
    }, indent=2))


if __name__ == "__main__":
    main()
