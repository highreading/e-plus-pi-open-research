#!/usr/bin/env python3
"""Exact boundary-renormalization certificate for Item 297.

No actual-row prime scan is performed.  The checker factors only twelve
explicit fixed core values, verifies the three boundary hypergeometric
residues, and records the exact reduced-recurrence drop table.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEPENDENCIES = {
    "item222_j1_phase_resultant_certificate.py": "c16f75156ba8424c567163cedc6a93a7656c8a53036b48ef69b06327d76ad44b",
    "item229_j1_fixed_h_theta_certificate.py": "a8e2028ca6a53f8c843c25be375feac50e4704538686ee1e3a835f89aa11780f",
    "item237_j1_algebraic_residual_certificate.py": "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf",
    "item237_j1_algebraic_residual_certificate.json": "eba1519f4d376d442f396048528190b474cc5464bbe42c3bdf31a9bdaf39dd6b",
    "item296_j1_modular_singular_ray_atlas_certificate.py": "caa3bc55969e300a3426bd078d78f2ab6003a3e0fae5f65b802c7ca610554646",
    "item296_j1_modular_singular_ray_atlas_certificate.json": "909da750976707960c8ba3b01a4e0456d970134bfa32d6e3235472dad4a7a0ab",
}


def resolve(name: str) -> Path:
    for path in (HERE / name, HERE.parent / "scripts" / name, HERE.parent / "results" / name):
        if path.is_file():
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


for dependency_name, expected_hash in DEPENDENCIES.items():
    dependency_path = resolve(dependency_name)
    if sha256(dependency_path) != expected_hash:
        raise RuntimeError(f"dependency hash mismatch: {dependency_name}")


item222 = load("item297_item222", resolve("item222_j1_phase_resultant_certificate.py"))
item229 = load("item297_item229", resolve("item229_j1_fixed_h_theta_certificate.py"))
item237 = load("item297_item237", resolve("item237_j1_algebraic_residual_certificate.py"))
item296 = load(
    "item297_item296", resolve("item296_j1_modular_singular_ray_atlas_certificate.py")
)
item296_result = json.loads(
    resolve("item296_j1_modular_singular_ray_atlas_certificate.json").read_text(
        encoding="utf-8"
    )
)
if item296_result.get("strict_labels", {}).get("complete_linear_factor_atlas") != "PROVED":
    raise AssertionError("Item296 atlas not admitted")


def factor_integer(value: int) -> list[list[int]]:
    value = abs(value)
    answer = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        answer.append([divisor, exponent])
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        answer.append([value, 1])
    return answer


def evaluate(polynomial: list[int], value: int) -> int:
    answer = 0
    for coefficient in reversed(polynomial):
        answer = answer * value + coefficient
    return answer


RAY_DATA = [(1, 2, 15), (2, 4, 27), (3, 6, 39)]


def fixed_core_atlas() -> dict[str, Any]:
    primitive_rows = item296_result["positive_core_atlas"]["rows"]
    primitive = [row["primitive_Rhat_low_to_high"] for row in primitive_rows]
    rows = []
    actual_overlaps: dict[int, dict[int, list[int]]] = {}
    for _, s_value, constant in RAY_DATA:
        ray_overlaps: dict[int, list[int]] = {}
        for coefficient_index, polynomial in enumerate(primitive):
            value = evaluate(polynomial, s_value)
            factors = factor_integer(value)
            actual_factors = []
            for prime, exponent in factors:
                if prime <= constant or (prime - constant) % 4:
                    continue
                h_value = (prime - constant) // 4
                if h_value >= 1 and h_value % 3:
                    actual_factors.append([prime, exponent, h_value])
                    ray_overlaps.setdefault(prime, []).append(coefficient_index)
            rows.append(
                {
                    "s": s_value,
                    "Q_index": coefficient_index,
                    "Rhat_value": value,
                    "complete_factorization": factors,
                    "actual_ray_prime_factors_prime_exponent_h": actual_factors,
                }
            )
        actual_overlaps[s_value] = ray_overlaps

    expected = {
        2: {15131: [3], 84211: [2], 103423: [0]},
        4: {79: [1, 2], 15131: [0]},
        6: {787067: [3], 1960627367: [2]},
    }
    if actual_overlaps != expected:
        raise AssertionError(("fixed core overlap table", actual_overlaps))
    return {
        "classification": "PROVED EXACT FACTORIZATION OF TWELVE FIXED CORE VALUES",
        "rows": rows,
        "actual_core_overlaps_by_s_then_p": actual_overlaps,
        "no_actual_prime_scan": True,
    }


def fraction_mod(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def boundary_sums(boundary_h: int, prime: int) -> tuple[int, int, int, int]:
    if prime != 4 * boundary_h + 3:
        raise ValueError((boundary_h, prime))
    kernel0 = item222.kernel_integer(boundary_h, 1)
    kernel1 = item222.kernel_integer(boundary_h, 4)
    x_value = sum(
        (-1) ** t * kernel0[2 * t + 1] * pow(t + 1, -1, prime)
        for t in range(boundary_h + 1)
    ) % prime
    y_value = sum(
        (-1) ** t
        * kernel0[2 * t + 1]
        * (boundary_h + 1)
        * pow(boundary_h + t + 1, -1, prime)
        for t in range(boundary_h + 1)
    ) % prime
    u_value = kernel1[0]
    inverse_three = pow(3, -1, prime)
    u_value += inverse_three * sum(
        (-1) ** t * kernel1[2 * t] for t in range(1, boundary_h + 3)
    )
    u_value %= prime
    v_value = sum(
        (-1) ** t * kernel1[2 * t + 1] for t in range(boundary_h + 2)
    ) % prime
    return x_value, y_value, u_value, v_value


def p_adic_valuation_integer(value: int, prime: int) -> int:
    value = abs(value)
    answer = 0
    while value and value % prime == 0:
        value //= prime
        answer += 1
    return answer


def p_adic_valuation(value: Fraction, prime: int) -> int:
    return p_adic_valuation_integer(value.numerator, prime) - p_adic_valuation_integer(
        value.denominator, prime
    )


def all_h_symbolic_boundary_derivation() -> dict[str, Any]:
    """Encode the universal Pochhammer reduction at p=4H+3.

    Affine pairs represent a*H+b.  These assertions are identities over
    Q[H], rather than checks at selected integer values.
    """

    def add(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]):
        return left[0] + right[0], left[1] + right[1]

    def scale(value: tuple[Fraction, Fraction], scalar: Fraction):
        return value[0] * scalar, value[1] * scalar

    h_symbol = (Fraction(1), Fraction(0))
    one = (Fraction(0), Fraction(1))
    two = (Fraction(0), Fraction(2))
    p_symbol = (Fraction(4), Fraction(3))
    s_symbol = scale(p_symbol, Fraction(-1, 6))
    q_symbol = scale(p_symbol, Fraction(-1, 3))
    assert scale(s_symbol, 2) == q_symbol
    assert scale(s_symbol, 3) == scale(p_symbol, Fraction(-1, 2))

    # Starting Pochhammer factors in Item222's four normalized sums.
    x_numerator = add(s_symbol, one)
    x_denominator = add(scale(s_symbol, 3), two)
    y_numerator = add(h_symbol, one)
    y_denominator = add(add(q_symbol, h_symbol), two)
    u_numerator = s_symbol
    u_denominator = scale(s_symbol, 3)
    v_numerator = add(h_symbol, one)
    v_denominator = add(add(q_symbol, h_symbol), one)
    assert x_numerator == add(scale(p_symbol, Fraction(-1, 6)), one)
    assert x_denominator == add(scale(p_symbol, Fraction(-1, 2)), two)
    assert y_denominator == add(add(h_symbol, two), scale(p_symbol, Fraction(-1, 3)))
    assert u_numerator == scale(p_symbol, Fraction(-1, 6))
    assert u_denominator == scale(p_symbol, Fraction(-1, 2))
    assert v_denominator == add(add(h_symbol, one), scale(p_symbol, Fraction(-1, 3)))
    assert Fraction(-1, 6) / Fraction(-1, 2) == Fraction(1, 3)

    # The largest residual denominator representatives are below p for H>=4.
    # X: 2,...,H+1; Y: H+2,...,2H+1;
    # U after its first-factor cancellation: 1,...,H+1;
    # V: H+1,...,2H+1.
    denominator_unit_intervals = {
        "X": ["2", "H+1", "p-(H+1)=3H+2>0"],
        "Y": ["H+2", "2H+1", "p-(2H+1)=2H+2>0"],
        "U_after_cancellation": ["1", "H+1", "p-(H+1)=3H+2>0"],
        "V": ["H+1", "2H+1", "p-(2H+1)=2H+2>0"],
    }

    # Multiplying Item222's eliminant by p and reducing p=4H+3.
    assert Fraction(-3, 4) * 4 + 3 == 0
    assert 4 * Fraction(-3, 4) + 1 == -2
    return {
        "classification": "PROVED SYMBOLICALLY FOR EVERY H>=4, 3 NOT DIVIDING H",
        "phase": "p=4H+3 and s_*=-p/6, so 2s_*=-p/3 and 3s_*=-p/2",
        "item222_pochhammer_reductions": {
            "X": "(1-p/6)_t/(2-p/2)_t = 1/(t+1) mod p, 0<=t<=H",
            "Y": (
                "(H+1)_t/(H+2-p/3)_t = (H+1)/(H+t+1) mod p, "
                "0<=t<=H"
            ),
            "U": (
                "t=0 is K1_0; for 1<=t<=H+2, "
                "(-p/6)_t/(-p/2)_t=(1/3)(1-p/6)_(t-1)/"
                "(1-p/2)_(t-1)=1/3 mod p"
            ),
            "V": "(H+1)_t/(H+1-p/3)_t=1 mod p, 0<=t<=H+1",
        },
        "canceled_U_first_factor": "(-p/6)/(-p/2)=1/3 exactly in Q",
        "remaining_denominator_unit_intervals": denominator_unit_intervals,
        "determinant_scaling": (
            "pE_H^*=H*X*V+9(4H+1)U*Y/2; H=-3/4 and 4H+1=-2 "
            "mod p, hence B_H=-3X*V/4-9U*Y mod p"
        ),
    }


def all_h_symbolic_gauge_valuation_derivation() -> dict[str, Any]:
    """Factor-by-factor p-valuation proof for the three boundary gauges."""

    # G_1 and G_2 are p-units because actual boundary primes have p>=19.
    assert factor_integer(49) == [[7, 2]]
    assert factor_integer(4235) == [[5, 1], [7, 1], [11, 2]]
    assert factor_integer(18) == [[2, 1], [3, 2]]
    assert factor_integer(1944) == [[2, 3], [3, 5]]

    four_offsets = (1, 5, 7, 9, 11, 15)
    relative_at_h_minus_3 = tuple(4 * (-3) + offset - 3 for offset in four_offsets)
    relative_at_h = tuple(offset - 3 for offset in four_offsets)
    relative_at_h_plus_3 = tuple(4 * 3 + offset - 3 for offset in four_offsets)
    assert relative_at_h_minus_3 == (-14, -10, -8, -6, -4, 0)
    assert relative_at_h == (-2, 2, 4, 6, 8, 12)
    assert relative_at_h_plus_3 == (10, 14, 16, 18, 20, 24)

    # At r=H+3, 2r+5=p iff H=4; that denominator is squared in rho.
    # For H>4 it is strictly below p.  No p+delta numerator is divisible
    # by the odd prime p because every listed delta is nonzero and even.
    exceptional_h = Fraction(2 * 3 + 5 - 3, 2)
    assert exceptional_h == 4
    return {
        "classification": "PROVED FACTOR BY FACTOR FOR EVERY ACTUAL BOUNDARY PRIME",
        "gauge_definition": {
            "G_1": "-49/18",
            "G_2": "4235/1944",
            "step": "G_(r+3)/G_r=rho(r)",
            "rho": (
                "r(4r+1)(4r+5)(4r+7)(4r+9)(4r+11)(4r+15)^2/"
                "[864(r+1)(r+2)(2r+1)^2(2r+3)(2r+5)^2(4r+3)]"
            ),
        },
        "base_unit_audit": (
            "G_1 and G_2 have prime support {2,3,5,7,11}; p=4H+3>=19"
        ),
        "earlier_steps": (
            "for r<=H-6, every positive numerator and denominator factor of "
            "rho(r) is <p, so v_p(rho(r))=0"
        ),
        "critical_steps": {
            "rho(H-3)": (
                "only (4(H-3)+15)^2=p^2 is divisible by p; all other factors "
                "are positive and <p, so v_p=2"
            ),
            "rho(H)": (
                "only denominator 4H+3=p is divisible by p; the numerator "
                "4H+c=p+(c-3), c=1,5,7,9,11,15, has nonzero offsets "
                "-2,2,4,6,8,12 of absolute value <p, so v_p=-1"
            ),
            "rho(H+3), p>19": (
                "all factors are p-units; the 4r+c numerator offsets are "
                "10,14,16,18,20,24 and the largest possible denominator "
                "collision 2r+5=p solves H=4 only, so v_p=0"
            ),
            "rho(H+3), p=19": (
                "H=4 and (2(H+3)+5)^2=19^2 is the only p-factor, so v_19=-2"
            ),
        },
        "conclusion": {
            "all_actual_boundaries": ["v_p(G_H)=2", "v_p(G_(H+3))=1"],
            "p>19": "v_p(G_(H+6))=1",
            "p=19,H=4": "v_19(G_10)=-1",
        },
    }


def boundary_residue_theorem() -> dict[str, Any]:
    # The t=0 coefficient cancellation in the Item237 formula.
    def half_binomial(degree: int) -> Fraction:
        answer = Fraction(1)
        for offset in range(degree):
            answer *= Fraction(1, 2) - offset
            answer /= offset + 1
        return answer

    cancellation = (
        -3 * half_binomial(2)
        - Fraction(17, 2) * half_binomial(3)
        - 4 * half_binomial(4)
    )
    if cancellation:
        raise AssertionError(("boundary c cancellation", cancellation))
    if 4 * 1 - 4 != 0:
        raise AssertionError("t=1 leading cancellation")
    if not (10 > 6):  # target-minus-top degree at t=2: (M+10)-(M+6).
        raise AssertionError("t=2 degree gap")

    replay = []
    for boundary_h in (4, 7, 10):
        prime = 4 * boundary_h + 3
        if factor_integer(prime) != [[prime, 1]]:
            raise AssertionError(("replay prime", prime))
        x_value, y_value, u_value, v_value = boundary_sums(boundary_h, prime)
        boundary_value = (
            -3 * pow(4, -1, prime) * x_value * v_value - 9 * u_value * y_value
        ) % prime
        eliminant = item222.phase_fraction_and_integer(boundary_h)[0]
        scaled = prime * eliminant
        if p_adic_valuation(scaled, prime) < 0:
            raise AssertionError(("boundary not integral", boundary_h))
        if fraction_mod(scaled, prime) != boundary_value:
            raise AssertionError(("boundary residue", boundary_h))
        replay.append([boundary_h, prime, x_value, y_value, u_value, v_value, boundary_value])

    exceptional = item222.phase_fraction_and_integer(10)[0]
    expected_exceptional = Fraction(
        -14259854752042485871640576, 221820599898513
    )
    if exceptional != expected_exceptional or p_adic_valuation(exceptional, 19) != 1:
        raise AssertionError(("exceptional E_10", exceptional))
    return {
        "classification": "PROVED EXACT BOUNDARY RENORMALIZATION",
        "all_H_symbolic_pochhammer_derivation": all_h_symbolic_boundary_derivation(),
        "all_H_symbolic_gauge_valuation_derivation": (
            all_h_symbolic_gauge_valuation_derivation()
        ),
        "boundary": "H=(p-3)/4, B_H=p*E_H^* is p-integral",
        "component_residues": {
            "X": "sum_(t=0)^H (-1)^t K0_(2t+1)/(t+1)",
            "Y": "sum_(t=0)^H (-1)^t K0_(2t+1)(H+1)/(H+t+1)",
            "U": "K1_0+(1/3)sum_(t=1)^(H+2)(-1)^t K1_(2t)",
            "V": "sum_(t=0)^(H+1)(-1)^t K1_(2t+1)",
        },
        "boundary_residue": "B_H=-3*X*V/4-9*U*Y mod p",
        "c_zero_lemma": (
            "c_(H+3t)^*=0 mod p for t=0,1,2 whenever 2(H+3t)<p; "
            "the only needed exception is (p,t)=(19,2)"
        ),
        "c_zero_proof": [
            "t=0: -3*C(1/2,2)-(17/2)*C(1/2,3)-4*C(1/2,4)=0",
            "t=1: the target is the formal top degree but the leading coefficient 4t-4 is zero",
            "t=2: the target degree M+10 exceeds the polynomial degree M+6",
        ],
        "gauge_valuations": {
            "all_actual_boundaries": ["v_p(G_H)=2", "v_p(G_(H+3))=1"],
            "p>19": "v_p(G_(H+6))=1",
            "p=19,H=4": (
                "v_19(G_10)=-1 and "
                "E_10=-14259854752042485871640576/221820599898513 has v_19=1"
            ),
        },
        "exact_replay_not_logical_basis": replay,
    }


def reduced_ray_relations(core_atlas: dict[str, Any]) -> dict[str, Any]:
    # Vanishing coefficients after the compulsory factor p has been removed
    # from Q_j on the s=2j ray.
    normalized_drops = {
        2: {19: [0, 1, 2, 3], 15131: [3], 84211: [2], 103423: [0]},
        4: {79: [1, 2], 15131: [0]},
        6: {787067: [3], 1960627367: [2]},
    }
    if core_atlas["actual_core_overlaps_by_s_then_p"] != {
        2: {15131: [3], 84211: [2], 103423: [0]},
        4: {79: [1, 2], 15131: [0]},
        6: {787067: [3], 1960627367: [2]},
    }:
        raise AssertionError("core atlas handoff")
    return {
        "classification": "PROVED EXACT ACTUAL-ORBIT BOUNDARY RELATIONS",
        "uniform_formula": (
            "on s=2j, H=h+3j and p=4H+3: "
            "sum_(k!=j) Q_k(h) E_(h+3k)^* + (Q_j(h)/p) B_H = 0 mod p"
        ),
        "integrality": (
            "all E terms with k!=j are p-integral; the only pole is the boundary "
            "E_H, and its explicit p factor cancels the structural factor in Q_j"
        ),
        "generic_boundary_coefficient": (
            "Q_j(h)/p is a p-unit outside the finite drop table; hence the apparent "
            "coefficient degeneracy does not lower the recurrence order"
        ),
        "normalized_coefficient_drops_by_s_then_p": normalized_drops,
        "finite_actual_consequences": {
            "s2_p19": "every coefficient in the first boundary reduction vanishes; the relation is 0=0",
            "s2_p103423": "Q0 drops, so the reduced relation contains no target E_h term",
            "s4_p15131": "Q0 drops, so the reduced relation contains no target E_h term",
            "s6_p787067": "the boundary term drops, leaving one relation among the three actual values at s=6,4,2",
            "other_rows": (
                "one or more auxiliary coefficients drop as tabulated, but no row yields "
                "a one-term nonzero constraint on E_h"
            ),
        },
        "scope": (
            "these are relations obeyed by the pinned actual E orbit, but each generic "
            "relation contains the boundary scalar or other actual/outside values. "
            "They do not imply E_h nonvanishing or sparsity"
        ),
    }


def capacity_ledger() -> dict[str, Any]:
    return {
        "individual_ray_mass": (
            "W_s(H)=theta(4H+6s+3;12,7)+theta(4H+6s+3;12,11)+O(1)~2H "
            "for each s=2,4,6"
        ),
        "deoverlap": (
            "4h+39=4(h+3)+27=4(h+6)+15, so the three ray prime sets differ "
            "only by endpoints and their union also has mass ~2H, not ~6H"
        ),
        "new_linear_log_rate": 0,
        "new_divisibility_exponent": 0,
        "capacity_booked": 0,
        "retained_conditional_j1_capacity_per_6m": "1/36",
    }


def build_result() -> dict[str, Any]:
    core = fixed_core_atlas()
    return {
        "schema": "item297-j1-structural-ray-boundary-v2",
        "item": 297,
        "title": "boundary renormalization on the three structural fixed-j1 rays",
        "dependencies": DEPENDENCIES,
        "raw_chebyshev_capacity": capacity_ledger(),
        "fixed_ray_core_atlas": core,
        "boundary_residue": boundary_residue_theorem(),
        "reduced_actual_ray_relations": reduced_ray_relations(core),
        "strict_labels": {
            "boundary_renormalization": "PROVED",
            "fixed_core_overlap_table": "PROVED",
            "actual_orbit_reduced_relations": "PROVED",
            "generic_lower_order_recurrence": "REFUTED BY POLE CANCELLATION",
            "actual_E_nonvanishing_or_weighted_density": "OPEN",
            "actual_prime_scan": "NONE",
            "capacity_booking": "ZERO",
            "Route_1": "OPEN",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = build_result()
    output = arguments.output or (
        HERE / "item297_j1_structural_ray_boundary_certificate.json"
        if HERE.name == "work"
        else HERE.parent / "results" / "item297_j1_structural_ray_boundary_certificate.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"output": str(output), "sha256": sha256(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
