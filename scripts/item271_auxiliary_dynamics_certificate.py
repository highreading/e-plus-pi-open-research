#!/usr/bin/env python3
"""Deterministic certificate for Item 271's auxiliary slope dynamics.

The script proves the displayed telescoping identities by exact rational
interpolation certificates with explicit degree bounds.  Bounded sequence
replays are separately labelled EXACT FINITE ONLY.  It performs no search
for exceptional collision primes.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path


INNER_TERMS = {
    5: [
        (8, 0, 222771669120), (7, 1, -74104377984), (7, 0, 3963632439744),
        (6, 2, -127370880), (6, 1, -1071196425792), (6, 0, 29894531541192),
        (5, 3, 25474176), (5, 2, -1671917760), (5, 1, -6369221894184),
        (5, 0, 124229238840108), (4, 3, 274943808), (4, 2, -8700206760),
        (4, 1, -20064611035188), (4, 0, 309157710319800),
        (3, 3, 1098505800), (3, 2, -22629707100), (3, 1, -35857616801796),
        (3, 0, 467812621640916), (2, 3, 1962761220), (2, 2, -30230926920),
        (2, 1, -35895450842208), (2, 0, 415189617006078),
        (1, 3, 1466409204), (1, 2, -18648679140), (1, 1, -18252382555146),
        (1, 0, 193700387876037), (0, 3, 308114352), (0, 2, -3594667440),
        (0, 1, -3487246491547), (0, 0, 34993656560590),
    ],
    1: [
        (8, 0, 222771669120), (7, 1, -74104377984), (7, 0, 2775516871104),
        (6, 2, -127370880), (6, 1, -725375995200), (6, 0, 14169849815880),
        (5, 3, 25474176), (5, 2, -1162434240), (5, 1, -2776077052200),
        (5, 0, 37948655899404), (4, 3, 190029888), (4, 2, -3976286760),
        (4, 1, -5206691047428), (4, 0, 56333087670960),
        (3, 3, 478540872), (3, 2, -6105110940), (3, 1, -4824136130148),
        (3, 0, 44129296161396), (2, 3, 423454068), (2, 2, -3595628880),
        (2, 1, -1783062800568), (2, 0, 14061143173590),
        (1, 3, 13368996), (1, 2, 246998700), (1, 1, 88590336198),
        (1, 0, -1138064082099), (0, 3, -71681400), (0, 2, 597345000),
        (0, 1, 137614422625), (0, 0, -1112384405000),
    ],
}


def is_prime(value: int) -> bool:
    return value >= 2 and all(value % divisor for divisor in range(2, isqrt(value) + 1))


def q_poly(phase: int, delta: int) -> int:
    if phase == 5:
        return 78624 * delta**3 + 245808 * delta**2 + 232866 * delta + 61727
    return 78624 * delta**3 + 88560 * delta**2 + 9954 * delta - 7565


def recurrence_polynomials(phase: int, delta: int) -> tuple[int, int, int]:
    if phase == 5:
        p0 = (
            4 * (3 * delta + 1) * (3 * delta + 4)
            * (6 * delta + 5) * (6 * delta + 11) * q_poly(phase, delta + 2)
        )
        p2 = (
            6561 * (2 * delta + 5) * (2 * delta + 7)
            * (6 * delta + 13) * (6 * delta + 19) * q_poly(phase, delta)
        )
    else:
        p0 = (
            4 * (3 * delta - 1) * (3 * delta + 2)
            * (6 * delta + 1) * (6 * delta + 7) * q_poly(phase, delta + 2)
        )
        p2 = (
            6561 * (2 * delta + 3) * (2 * delta + 5)
            * (6 * delta + 11) * (6 * delta + 17) * q_poly(phase, delta)
        )
    return p0, -p0 - p2, p2


def phase_parameters(phase: int, delta: int) -> tuple[int, int, int, int]:
    if phase == 5:
        return 5, 4, -1, 3 * delta
    return 1, 2, 1, 3 * delta - 2


def slope_data(phase: int, delta: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    numerator_shift, denominator_shift, mu, length = phase_parameters(phase, delta)
    coefficient = Fraction(1)
    prefix = Fraction(0)
    for index in range(delta):
        prefix += coefficient
        coefficient *= Fraction(6 * index + numerator_shift, 3 * index + denominator_shift)
    numerator = 1
    denominator = 1
    tail = Fraction(0)
    for index in range(length):
        numerator *= 3 * index - 3 * delta + mu
        denominator *= 3 * (2 * index + 1)
        tail += Fraction(numerator, denominator)
    return prefix + coefficient * tail, prefix, coefficient, tail


def a_parameter(phase: int, delta: int) -> Fraction:
    return -Fraction(delta) - Fraction(1, 3) if phase == 5 else Fraction(1, 3) - delta


def c_ratios(phase: int, delta: int) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    ns, ds = (5, 4) if phase == 5 else (1, 2)
    values = [Fraction(1)]
    current = Fraction(1)
    for offset in range(4):
        current *= Fraction(6 * (delta + offset) + ns, 3 * (delta + offset) + ds)
        values.append(current)
    return values[1], values[2], values[3], values[4]


def shifted_pochhammer_ratio(a: Fraction, parameter_shift: int, k: int) -> Fraction:
    result = Fraction(1)
    for index in range(1, parameter_shift + 1):
        result *= Fraction(a - index, a + k - index)
    return result


def inner_certificate(phase: int, delta: int, k: int) -> int:
    return sum(
        coefficient * delta**delta_power * k**k_power
        for delta_power, k_power, coefficient in INNER_TERMS[phase]
    )


def certificate_r(phase: int, delta: int, k: int) -> Fraction:
    if phase == 5:
        outside = -9 * (6 * delta + 5) * (6 * delta + 11) * (2 * k - 1)
        shifts = (4, 7, 10, 13)
    else:
        outside = -9 * (6 * delta + 1) * (6 * delta + 7) * (2 * k - 1)
        shifts = (2, 5, 8, 11)
    denominator = 1
    for shift in shifts:
        denominator *= 3 * delta - 3 * k + shift
    return Fraction(outside * inner_certificate(phase, delta, k), denominator)


def telescoper_q(phase: int, delta: int, k: int) -> Fraction:
    p0, p1, p2 = recurrence_polynomials(phase, delta)
    a = a_parameter(phase, delta)
    _, c2, _, c4 = c_ratios(phase, delta)
    return (
        p0
        + p1 * c2 * shifted_pochhammer_ratio(a, 2, k)
        + p2 * c4 * shifted_pochhammer_ratio(a, 4, k)
    )


def check_telescoping_certificate() -> dict[str, object]:
    # After clearing the displayed denominators, the WZ numerator has
    # degree at most 32 in delta and 16 in k.  A (33 x 17) exact grid
    # therefore proves the bivariate polynomial identity.
    wz_delta_bound = 32
    wz_k_bound = 16
    wz_checks = 0
    for phase in (5, 1):
        for delta in range(100, 100 + wz_delta_bound + 1):
            a = a_parameter(phase, delta)
            for k in range(wz_k_bound + 1):
                step_ratio = Fraction(a + k, 2 * k + 1)
                left = (
                    step_ratio * certificate_r(phase, delta, k + 1)
                    - certificate_r(phase, delta, k)
                )
                assert left == telescoper_q(phase, delta, k)
                wz_checks += 1

    # The two moving-boundary defects have cleared numerator degree at
    # most 64 in delta.  Sixty-five exact values prove each identity.
    boundary_degree_bound = 64
    terminal_checks = 0
    rational_checks = 0
    for phase in (5, 1):
        for delta in range(100, 100 + boundary_degree_bound + 1):
            p0, p1, p2 = recurrence_polynomials(phase, delta)
            a = a_parameter(phase, delta)
            c1, c2, c3, c4 = c_ratios(phase, delta)
            length = 3 * delta if phase == 5 else 3 * delta - 2
            base_index = length + 1

            def shifted_base(parameter_shift: int, advance: int) -> Fraction:
                value = shifted_pochhammer_ratio(a, parameter_shift, base_index)
                for offset in range(advance):
                    value *= Fraction(
                        a - parameter_shift + base_index + offset,
                        2 * (base_index + offset) + 1,
                    )
                return value

            terminal = certificate_r(phase, delta, base_index)
            terminal += p1 * c2 * sum(
                (shifted_base(2, advance) for advance in range(6)), Fraction(0)
            )
            terminal += p2 * c4 * sum(
                (shifted_base(4, advance) for advance in range(12)), Fraction(0)
            )
            assert terminal == 0
            terminal_checks += 1

            rational = (
                -a * certificate_r(phase, delta, 1)
                - p0 * (1 + c1)
                + p2 * (c2 + c3)
            )
            assert rational == 0
            rational_checks += 1
    return {
        "proof_method": "exact rational interpolation after explicit denominator clearing",
        "wz_cleared_degree_bounds": {"delta": wz_delta_bound, "k": wz_k_bound},
        "wz_grid_checks": wz_checks,
        "boundary_cleared_degree_bound_delta": boundary_degree_bound,
        "terminal_boundary_checks": terminal_checks,
        "rational_boundary_checks": rational_checks,
        "status": "PROVED SYMBOLIC CERTIFICATE, not a finite-pattern inference",
    }


def check_recurrence_and_dynamics(max_delta: int) -> dict[str, object]:
    recurrence_checks = 0
    orbit_checks = 0
    initial = {}
    for phase, start in ((5, 1), (1, 3)):
        first = slope_data(phase, start)[0]
        second = slope_data(phase, start + 2)[0]
        difference = second - first
        initial[str(phase)] = {
            "delta_0": start,
            "D_0": str(first),
            "Delta_0": str(difference),
        }
        delta = start
        state_d = first
        state_delta = difference
        while delta + 4 <= max_delta:
            direct0 = slope_data(phase, delta)[0]
            direct1 = slope_data(phase, delta + 2)[0]
            direct2 = slope_data(phase, delta + 4)[0]
            p0, p1, p2 = recurrence_polynomials(phase, delta)
            assert p0 * direct0 + p1 * direct1 + p2 * direct2 == 0
            recurrence_checks += 1
            assert state_d == direct0
            assert state_delta == direct1 - direct0
            rho = Fraction(p0, p2)
            state_d, state_delta = state_d + state_delta, rho * state_delta
            delta += 2
            orbit_checks += 1
    return {
        "recurrence": "P0(delta)D_delta+P1(delta)D_(delta+2)+P2(delta)D_(delta+4)=0, P1=-P0-P2",
        "difference_update": "Delta_(delta+2)=[P0(delta)/P2(delta)]Delta_delta",
        "autonomous_map": "T(delta,D,Delta)=(delta+2,D+Delta,[P0(delta)/P2(delta)]Delta)",
        "rank": 3,
        "projective_rational_degree_upper_bound": 8,
        "initial_states": initial,
        "bounded_recurrence_checks": recurrence_checks,
        "bounded_orbit_checks": orbit_checks,
        "bounded_check_label": "EXACT FINITE ONLY; the all-delta theorem comes from the telescoping certificate",
    }


def root_offsets(phase: int) -> tuple[list[Fraction], list[Fraction]]:
    if phase == 5:
        numerator = [Fraction(-1, 3), Fraction(-4, 3), Fraction(-5, 6), Fraction(-11, 6)]
        denominator = [Fraction(-5, 2), Fraction(-7, 2), Fraction(-13, 6), Fraction(-19, 6)]
    else:
        numerator = [Fraction(1, 3), Fraction(-2, 3), Fraction(-1, 6), Fraction(-7, 6)]
        denominator = [Fraction(-3, 2), Fraction(-5, 2), Fraction(-11, 6), Fraction(-17, 6)]
    return numerator, denominator


def check_iterate_complexity() -> dict[str, object]:
    residue_checks = 0
    irreducibility_checks = 0
    for phase in (5, 1):
        numerator, denominator = root_offsets(phase)
        for left in numerator:
            for right in denominator:
                assert (left - right) / 2 not in range(-100, 101)
                assert ((left - right) / 2).denominator != 1
                residue_checks += 1
        # A cubic over F_31 is irreducible iff it has no root.
        assert 78624 % 31 != 0
        for value in range(31):
            assert q_poly(phase, value) % 31 != 0
            irreducibility_checks += 1
    return {
        "multiplier_iterate": "rho_n(delta)=product_(i<n)rho(delta+2i)",
        "reduced_numerator_degree": "4n+3",
        "reduced_denominator_degree": "4n+3",
        "linear_root_class_non_cancellation_checks": residue_checks,
        "Q_irreducibility_mod_31_root_checks": irreducibility_checks,
        "scope": "proves direct-coordinate iterate degree growth only; does not obstruct a fixed rational dynamical system or a new lisse realization",
    }


def check_singular_actual_rows() -> dict[str, object]:
    witnesses = []
    for phase, prime, delta in ((5, 167, 7), (1, 241, 11)):
        assert is_prime(prime) and prime % 6 == phase
        q = (prime - phase) // 6
        assert q >= delta and delta % 2 == 1
        p0, _, p2 = recurrence_polynomials(phase, delta)
        slope = slope_data(phase, delta)[0]
        next_slope = slope_data(phase, delta + 2)[0]
        assert p2 % prime == 0
        assert p0 % prime != 0
        assert slope.denominator % prime != 0
        assert next_slope.denominator % prime != 0
        difference = next_slope - slope
        assert difference.denominator % prime != 0
        assert difference.numerator % prime == 0
        witnesses.append(
            {
                "phase": phase,
                "p": prime,
                "q": q,
                "delta": delta,
                "P0_mod_p": p0 % prime,
                "P2_mod_p": 0,
                "Delta_delta_mod_p": 0,
                "original_D_denominator_is_p_unit": True,
            }
        )
    return {
        "forward_map_pole_divisor": "P2(delta)=0",
        "difference_module_singular_support": "P0(delta)*P2(delta)=0, together with infinity",
        "exact_witnesses": witnesses,
        "label": "EXACT FINITE ONLY singular-map witnesses, not collision-prime census",
        "consequence": "the rational update is not defined on every actual mod-p row although the original slope is defined",
    }


def build_result(max_delta: int) -> dict[str, object]:
    return {
        "schema": "item271-auxiliary-dynamics-certificate-v1",
        "strict_labels": {
            "order_two_recurrence": "PROVED BY EXACT TELESCOPING CERTIFICATE",
            "rank_three_autonomous_skew_product": "PROVED",
            "difference_module": "PROVED POSITIVE RECOGNITION",
            "lisse_or_crystalline_frobenius_realization": "OPEN; NOT CONSTRUCTED",
            "full_two_gate_fixed_frobenius_divisor": "NOT OBTAINED",
            "bounded_sequence_checks": "EXACT FINITE ONLY",
            "exceptional_collision_search": "NONE",
            "positive_linear_capacity_admission": "FAIL",
            "booking": "zero new Route-1 rate and zero ordinary-j=2 capacity reduction",
        },
        "telescoping_certificate": check_telescoping_certificate(),
        "recurrence_and_dynamics": check_recurrence_and_dynamics(max_delta),
        "iterate_complexity": check_iterate_complexity(),
        "singular_actual_rows": check_singular_actual_rows(),
        "admission_audit": {
            "fixed_period_divisor_after_augmentation": "epsilon*(H-D*h)-1=0",
            "full_gate": "still requires both rows of external R_(r,s) from Item269",
            "translation_difference_not_frobenius": True,
            "uniform_conductor_theorem": False,
            "nontrivial_geometric_monodromy_theorem": False,
            "uniform_local_density_theorem": False,
            "capacity_result": 0,
        },
        "open": [
            "realize the translation-difference module, including its singular actual rows, as a bounded-conductor lisse or crystalline Frobenius family",
            "construct a bounded-state update for the complete two-row matrix R_(r,s), not only D_delta",
            "prove nontrivial geometric monodromy and a uniform local-density bound for the resulting full collision divisor",
            "Route 1 and every conclusion about e+pi",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--max-delta", type=int, default=31)
    args = parser.parse_args()
    if args.max_delta < 11 or args.max_delta % 2 == 0:
        raise SystemExit("--max-delta must be odd and at least 11")
    result = build_result(args.max_delta)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
