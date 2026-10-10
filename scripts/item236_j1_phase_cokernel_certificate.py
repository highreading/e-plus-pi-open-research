#!/usr/bin/env python3
"""Deterministic certificate for Item 236's all-h phase cokernel theorem."""

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
RESULT_NAME = "item236_j1_phase_cokernel_certificate.json"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, filename: str):
    path = resolve(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM222_PATH = resolve("item222_j1_phase_resultant_certificate.py")
ITEM229_PATH = resolve("item229_j1_fixed_h_theta_certificate.py")
ITEM231_PATH = resolve("item231_j1_second_phase_coefficient_certificate.py")

item222 = load("item236_item222", ITEM222_PATH.name)
item229 = load("item236_item229", ITEM229_PATH.name)
item231 = load("item236_item231", ITEM231_PATH.name)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stirling_second(maximum: int) -> list[list[int]]:
    table = [[0] * (maximum + 1) for _ in range(maximum + 1)]
    table[0][0] = 1
    for degree in range(1, maximum + 1):
        for index in range(1, degree + 1):
            table[degree][index] = (
                table[degree - 1][index - 1]
                + index * table[degree - 1][index]
            )
    return table


def falling(value: Fraction, length: int) -> Fraction:
    answer = Fraction(1)
    for offset in range(length):
        answer *= value - offset
    return answer


def phi_moments(s_value: Fraction, maximum: int) -> list[Fraction]:
    """Phi_s(j^degree), defined coefficientwise in the falling basis."""
    stirling = stirling_second(maximum)
    falling_values = [
        falling(-2 * s_value, index) / (2**index)
        for index in range(maximum + 1)
    ]
    return [
        sum(
            stirling[degree][index] * falling_values[index]
            for index in range(degree + 1)
        )
        for degree in range(maximum + 1)
    ]


def phi(poly: list[Fraction], s_value: Fraction) -> Fraction:
    moments = phi_moments(s_value, len(poly) - 1)
    return sum(coefficient * moments[degree] for degree, coefficient in enumerate(poly))


def binomial_positive(top_constant: Fraction, degree: int) -> list[Fraction]:
    """The polynomial binom(top_constant+2j,degree), low-to-high in j."""
    answer = [Fraction(1)]
    for offset in range(degree):
        answer = item229.multiply(
            answer, [top_constant - offset, Fraction(2)]
        )
    return item229.scale(answer, Fraction(1, math.factorial(degree)))


def high_polynomial(h_value: int, s_value: Fraction) -> list[Fraction]:
    r_value = 2 * h_value
    a_coefficient = 2 * r_value + 4 * s_value - 1
    b_coefficient = r_value + 1
    c_coefficient = -(r_value + 8 * s_value)
    return item229.add(
        item229.add(
            item229.scale(
                binomial_positive(Fraction(-r_value - 1), r_value),
                c_coefficient,
            ),
            item229.scale(
                binomial_positive(Fraction(-r_value), r_value),
                b_coefficient,
            ),
        ),
        item229.scale(
            binomial_positive(Fraction(-r_value + 1), r_value),
            a_coefficient,
        ),
    )


def cokernel_grid(h_max: int) -> dict[str, Any]:
    rows = []
    for h_value in range(1, h_max + 1):
        r_value = 2 * h_value
        s_phase = Fraction(-(4 * h_value + 3), 6)
        low_poly = item229.p_polynomial(h_value, s_phase)
        high_poly = high_polynomial(h_value, s_phase)
        low_residual = phi(low_poly, s_phase)
        high_residual = phi(high_poly, s_phase)
        if low_residual != high_residual:
            raise AssertionError(
                (h_value, low_residual, high_residual, "phase residual")
            )
        if low_residual != item229.phase_c(h_value):
            raise AssertionError(
                (h_value, low_residual, item229.phase_c(h_value), "Item229 c")
            )

        # Replay Phi_s(L_s U)=0 on a deterministic polynomial of maximal
        # allowed degree.  This checks the exact coefficientwise functional.
        test_poly = [
            Fraction((-1) ** degree * (h_value + degree + 1), degree + 1)
            for degree in range(r_value)
        ]
        annihilated = phi(item229.operator_l(test_poly, s_phase), s_phase)
        if annihilated:
            raise AssertionError((h_value, annihilated, "operator cokernel"))

        # Replay the binomial reflection on all six tops used in the theorem.
        reflection_tops = [
            Fraction(r_value + 2 * s_phase + offset)
            for offset in (2, 3, 4)
        ]
        reflected = []
        for top in reflection_tops:
            left = phi(item229.binomial_linear(top, r_value), s_phase)
            right = phi(
                binomial_positive(top + 4 * s_phase, r_value), s_phase
            )
            if left != right:
                raise AssertionError((h_value, top, left, right, "reflection"))
            reflected.append((left.numerator, left.denominator))

        # For a smaller exact grid, independently solve the two Gosper
        # systems and compare their returned constants with Phi.
        if h_value <= 12:
            low_solved, _ = item229.gosper_reduce(h_value, s_phase)
            high_solved, _ = item231.high_gosper_reduce(h_value, s_phase)
            if (low_solved, high_solved) != (low_residual, high_residual):
                raise AssertionError(
                    (h_value, low_solved, high_solved, low_residual)
                )

        rows.append(
            (
                h_value,
                s_phase.numerator,
                s_phase.denominator,
                low_residual.numerator,
                low_residual.denominator,
                *[entry for pair in reflected for entry in pair],
            )
        )
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_REPLAY_OF_PROVED_ALL_H_IDENTITY",
        "h_max": h_max,
        "rows": len(rows),
        "phase": "s*=-(4h+3)/6, r=2h, hence 2r+6s*+3=0",
        "cokernel": (
            "Phi_s(j^n)=sum_k Stirling2(n,k)*(-2s)_falling_k/2^k; "
            "Phi_s(1)=1 and Phi_s(L_s U)=0"
        ),
        "reflection": (
            "Phi_s binom(alpha-2j,r)=Phi_s binom(alpha+4s+2j,r)"
        ),
        "conclusion": "c_high(h,s*)=c_low(h,s*) for every h>=1",
        "gosper_square_replay_h_max": min(h_max, 12),
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def non_phase_grid(h_max: int, s_max: int) -> dict[str, Any]:
    """Show that equality is phase-specific, while Phi remains the cokernel."""
    rows = []
    unequal = 0
    for h_value in range(1, h_max + 1):
        for s_integer in range(1, s_max + 1):
            s_value = Fraction(s_integer)
            low = phi(item229.p_polynomial(h_value, s_value), s_value)
            high = phi(high_polynomial(h_value, s_value), s_value)
            unequal += low != high
            rows.append((h_value, s_integer, low.numerator, low.denominator, high.numerator, high.denominator))
    if unequal == 0:
        raise AssertionError("phase equality unexpectedly universal")
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_SCOPE_REPLAY",
        "h_max": h_max,
        "s_max": s_max,
        "rows": len(rows),
        "unequal_low_high_residual_rows": unequal,
        "scope": "the equality uses 2r+6s+3=0 and is not asserted away from the row phase",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def certificate(h_max: int) -> dict[str, Any]:
    return {
        "item": 236,
        "schema": "item236-j1-phase-cokernel-v1",
        "dependencies": {
            ITEM222_PATH.name: sha256(ITEM222_PATH),
            ITEM229_PATH.name: sha256(ITEM229_PATH),
            ITEM231_PATH.name: sha256(ITEM231_PATH),
        },
        "all_h_theorem": cokernel_grid(h_max),
        "scope_grid": non_phase_grid(8, 8),
        "localized_resultant_status": {
            "classification": "OPEN",
            "proved_input": "the low and high Gosper residuals coincide at phase for all h",
            "missing_inputs": [
                "an all-h identity relating the common residual c_h(s*) to Item222 E_h*",
                "a symbolic unit-localized factorization or gcd theorem for the natural endpoint scalar K_h and E_h*",
            ],
            "finite_patterns": "not used to infer redundancy or prime exclusion",
        },
        "rate_ledger": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "reason": (
                "residual equality synchronizes the two coefficient reductions but "
                "does not make the common residual vanish modulo an actual row prime"
            ),
        },
        "status_ledger": {
            "PROVED": [
                "the normalized coefficientwise functional Phi_s is the cokernel of L_s",
                "the exact positive/negative binomial reflection under Phi_s",
                "c_high(h,s*)=c_low(h,s*) for every h>=1",
            ],
            "EXACT_REPLAY": [
                f"the coefficientwise theorem through h<={h_max}",
                "independent square-system comparison through h<=12",
            ],
            "OPEN": [
                "an all-h c_h(s*)/E_h* factorization",
                "a symbolic K_h/E_h* localized resultant or gcd theorem",
                "all-prime exclusion, weighted exceptional-prime control, or any positive Route-1 rate",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--h-max", type=int, default=80)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.h_max < 12:
        raise ValueError("canonical h-max must be at least 12")
    result = certificate(args.h_max)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "h_max": args.h_max,
                "conclusion": result["all_h_theorem"]["conclusion"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
