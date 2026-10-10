#!/usr/bin/env python3
"""Exact certificate for Item 261's p == 1 (mod 6) punctured reduction.

The checker uses only the Python standard library.  Rational Hermite
identities are proved coefficientwise.  Bounded finite-field scans are
reported as EXACT FINITE ONLY and support no density inference.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray([1]) * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = bytes([0]) * (
                (limit - q * q) // q + 1
            )
    return [q for q in range(2, limit + 1) if sieve[q]]


def add(left: dict[int, F], right: dict[int, F]) -> dict[int, F]:
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, F(0)) + coefficient
        if out[exponent] == 0:
            del out[exponent]
    return out


def scale(poly: dict[int, F], scalar: F) -> dict[int, F]:
    return {
        exponent: scalar * coefficient
        for exponent, coefficient in poly.items()
        if scalar * coefficient
    }


def monomial(exponent: int, coefficient: F = F(1)) -> dict[int, F]:
    return {} if coefficient == 0 else {exponent: coefficient}


def primitive_operator(poly: dict[int, F]) -> dict[int, F]:
    """D on R_j=x^(j+1)/(1-x/2)^2.

    The dictionary exponent j denotes R_j.  The result is a Laurent
    polynomial in x:
      D(R_j)=(6j+1)/6*x^(j-1)-(3j+2)/6*x^j.
    """
    out: dict[int, F] = {}
    for j, coefficient in poly.items():
        out = add(
            out,
            {
                j - 1: coefficient * F(6 * j + 1, 6),
                j: -coefficient * F(3 * j + 2, 6),
            },
        )
    return out


def rising(value: F, count: int) -> F:
    out = F(1)
    for j in range(count):
        out *= value + j
    return out


def reduction_data(delta: int) -> dict[str, Any]:
    if delta < 1:
        raise ValueError(delta)
    c_values = [F(1)]
    primitives: list[dict[int, F]] = []
    previous: dict[int, F] = {}
    for j in range(delta):
        ratio = F(6 * j + 1, 3 * j + 2)
        c_values.append(c_values[-1] * ratio)
        current = add(
            scale(previous, ratio),
            monomial(j, F(6, 3 * j + 2)),
        )
        expected = add(monomial(-1, c_values[j + 1]), monomial(j, -1))
        assert primitive_operator(current) == expected
        primitives.append(current)
        previous = current

    total_primitive: dict[int, F] = {}
    for primitive in primitives:
        total_primitive = add(total_primitive, primitive)
    gamma = sum(c_values[1:], F(0))
    expected_total = monomial(-1, gamma)
    for j in range(delta):
        expected_total = add(expected_total, monomial(j, -1))
    assert primitive_operator(total_primitive) == expected_total

    boundary = sum(c_values[:delta], F(0))

    # Clear 1-x in x^delta/(1-x)=1/(1-x)-sum_(j<delta)x^j.
    telescoper = add(monomial(delta), monomial(0, -1))
    for j in range(delta):
        telescoper = add(telescoper, monomial(j, 1))
        telescoper = add(telescoper, monomial(j + 1, -1))
    assert telescoper == {}

    # Fixed gate correction from Item 251 after q=(p-1)/6 is reduced mod p.
    r = 3 * delta - 4
    gate_length = r + 2
    fixed_gate_tail = sum(
        (
            F(1, 2**k)
            * rising(F(1, 3) - delta, k)
            / rising(F(1, 2), k)
            for k in range(1, gate_length + 1)
        ),
        F(0),
    )
    gate_coefficient = boundary + c_values[delta] * fixed_gate_tail

    return {
        "delta": delta,
        "r": r,
        "C": c_values,
        "K": boundary,
        "Gamma": gamma,
        "primitive": total_primitive,
        "fixed_gate_tail": fixed_gate_tail,
        "fixed_gate_coefficient": gate_coefficient,
    }


def fmod(value: F, p: int) -> int:
    assert math.gcd(value.denominator, p) == 1
    return value.numerator * pow(value.denominator, -1, p) % p


def h_prefixes(p: int, maximum: int) -> tuple[list[int], list[int]]:
    h_values = [1]
    h_sums = [1]
    value = 1
    total = 1
    for j in range(1, maximum + 1):
        value = value * (2 * j - 1) * pow(4 * j, -1, p) % p
        total = (total + value) % p
        h_values.append(value)
        h_sums.append(total)
    return h_values, h_sums


def actual_rows_for_prime(p: int):
    for s in range(1, (p - 3) // 6 + 1):
        numerator = p - 6 * s - 3
        if numerator <= 0:
            break
        r = numerator // 2
        if 2 * r == numerator and r >= 1 and r % 2 == 1 and r % 3 != 0:
            yield r, s


def item251_period_integer(s: int) -> int:
    return sum(
        math.comb(3 * s - 1, s + j) * math.comb(s + j - 1, j)
        for j in range(2 * s)
    )


def direct_gate_tail(m: int, length: int) -> F:
    return sum(
        (
            F(1, 2**k)
            * rising(F(m) + F(1, 2), k)
            / rising(F(1, 2), k)
            for k in range(1, length + 1)
        ),
        F(0),
    )


def finite_field_replay(prime_max: int) -> dict[str, Any]:
    primes = [p for p in primes_upto(prime_max) if p >= 7 and p % 6 == 1]
    prime_coordinate_equalities = 0
    complete_moment_equalities = 0
    endpoint_equalities = 0
    actual_rows = 0
    localized_equalities = 0
    hermite_endpoint_equalities = 0
    gate_period_equalities = 0
    zero_rows: list[tuple[int, int, int, int, int]] = []
    first_rows: list[dict[str, int]] = []

    for p in primes:
        q = (p - 1) // 6
        n = 3 * q
        inv2 = pow(2, -1, p)
        epsilon = 1 if pow(2, n, p) == 1 else -1
        assert pow(2, n, p) == epsilon % p
        h_values, h_sums = h_prefixes(p, 3 * q + 1)

        point_data: list[tuple[int, int]] = []
        complete_data: list[tuple[int, int]] = []
        for x in range(1, p):
            f_value = (
                pow(1 - x * inv2, 3, p) * pow(x, -1, p)
            ) % p
            character = pow(f_value, q, p)
            complete_data.append((x, character))
            if x != 1:
                point_data.append((x, character))
        assert dict(complete_data)[1] == epsilon % p

        # Complete character moments: the unique surviving exponent is zero.
        for j in range(q + 1):
            observed = sum(pow(x, j, p) * value for x, value in complete_data) % p
            assert observed == (-h_values[q - j]) % p
            complete_moment_equalities += 1

        u_value = sum(pow(x, -1, p) * value for x, value in point_data) % p
        v_value = sum(pow(1 - x, -1, p) * value for x, value in point_data) % p
        assert h_values[q + 1] == h_values[q] * pow(5, -1, p) % p
        assert u_value == (-h_values[q] * pow(5, -1, p) - epsilon) % p
        assert v_value == (
            -h_sums[q] + 2 * epsilon * pow(3, -1, p)
        ) % p
        prime_coordinate_equalities += 3

        # Each Hermite exact differential has a nonzero finite-field defect.
        for j in range(q):
            observed = 0
            for x, character in point_data:
                d_value = (
                    fmod(F(6 * j + 1, 6), p) * pow(x, j - 1, p)
                    - fmod(F(3 * j + 2, 6), p) * pow(x, j, p)
                ) % p
                observed += d_value * character
            t = q - j + 1
            coefficient = (
                math.comb(n + 1, t) % p
                * pow(-inv2, t, p)
            ) % p
            endpoint = epsilon * fmod(F(3 * j - 1, 6), p)
            expected = (-coefficient - endpoint) % p
            assert observed % p == expected
            simplified = (
                -fmod(F(3, 2 * (3 * j - 1)), p) * h_values[t]
                - endpoint
            ) % p
            assert expected == simplified
            endpoint_equalities += 1

        for r, s in actual_rows_for_prime(p):
            if r % 6 != 5:
                continue
            m = s - 1
            delta = (r + 4) // 3
            assert delta % 2 == 1 and delta >= 3
            assert m == q - delta
            data = reduction_data(delta)
            k_value = fmod(data["K"], p)
            gamma = fmod(data["Gamma"], p)
            c_delta = fmod(data["C"][delta], p)
            assert all(value.denominator % p for value in data["C"])

            t_value = 0
            for x, character in point_data:
                t_value += (
                    pow(x, delta, p)
                    * pow(1 - x, -1, p)
                    * character
                )
            t_value %= p
            endpoint_total = (
                (gamma - 5 * k_value) * u_value
                + epsilon * (delta - 5 * k_value)
            ) % p
            d_total = 0
            for x, character in point_data:
                d_value = gamma * pow(x, -1, p)
                for j in range(delta):
                    d_value -= pow(x, j, p)
                d_total += d_value * character
            d_total %= p
            assert d_total == endpoint_total
            assert t_value == (
                v_value
                - 5 * k_value * u_value
                + epsilon * (delta - 5 * k_value)
            ) % p
            assert t_value == (
                -h_sums[q]
                + k_value * h_values[q]
                + epsilon * (2 * q + delta + 1)
            ) % p

            direct_h = h_sums[m]
            jacobi_a = 2 * q + delta + 1
            assert direct_h == (-t_value + epsilon * jacobi_a) % p
            assert direct_h == (h_sums[q] - k_value * h_values[q]) % p
            assert h_values[m] == c_delta * h_values[q] % p
            hermite_endpoint_equalities += 1
            localized_equalities += 5

            # Item-251's surviving period is also a fixed affine expression
            # in the same two residual coordinates.
            gate_length = r + 2
            direct_tail = direct_gate_tail(m, gate_length)
            fixed_tail = data["fixed_gate_tail"]
            assert fmod(direct_tail - fixed_tail, p) == 0
            fixed_gate_coefficient = fmod(data["fixed_gate_coefficient"], p)
            inside_direct = (
                direct_h - h_values[m] * fmod(direct_tail, p)
            ) % p
            inside_two_state = (
                h_sums[q] - fixed_gate_coefficient * h_values[q]
            ) % p
            assert inside_direct == inside_two_state
            a_s = item251_period_integer(s) % p
            predicted_a = (
                (-1 if m % 2 else 1)
                * (epsilon * inside_two_state - 1)
            ) % p
            assert a_s == predicted_a
            gate_period_equalities += 3

            actual_rows += 1
            if direct_h == 0:
                zero_rows.append((p, r, s, m, delta))
            if len(first_rows) < 12:
                first_rows.append(
                    {
                        "p": p,
                        "r": r,
                        "s": s,
                        "m": m,
                        "delta": delta,
                        "epsilon": epsilon,
                        "U_holomorphic": u_value,
                        "V_punctured": v_value,
                        "K_delta": k_value,
                        "Gamma_delta": gamma,
                        "H_m": direct_h,
                        "Item251_A_s": a_s,
                    }
                )

    assert (43, 11, 3, 2, 5) in zero_rows
    digest = hashlib.sha256(
        ("\n".join(",".join(map(str, row)) for row in zero_rows) + "\n").encode()
    ).hexdigest()
    return {
        "prime_max": prime_max,
        "p_eq_1_mod_6_primes": len(primes),
        "prime_level_coordinate_equalities": prime_coordinate_equalities,
        "complete_character_moment_equalities": complete_moment_equalities,
        "endpoint_summation_by_parts_equalities": endpoint_equalities,
        "actual_rows": actual_rows,
        "localized_row_equalities": localized_equalities,
        "summed_Hermite_endpoint_equalities": hermite_endpoint_equalities,
        "Item251_period_two_state_equalities": gate_period_equalities,
        "H_zero_count": len(zero_rows),
        "H_zero_rows_p_r_s_m_delta": [list(row) for row in zero_rows],
        "zero_digest_sha256": digest,
        "first_rows": first_rows,
        "strict_label": "EXACT FINITE ONLY; no density or all-prime inference",
    }


def symbolic_replay(delta_max: int) -> dict[str, Any]:
    rows: list[str] = []
    samples: list[dict[str, Any]] = []
    for delta in range(1, delta_max + 1):
        data = reduction_data(delta)
        rows.append(
            f"{delta},{data['r']},{data['K'].numerator},{data['K'].denominator},"
            f"{data['Gamma'].numerator},{data['Gamma'].denominator},"
            f"{len(data['primitive'])}"
        )
        if delta in {1, 2, 3, 5, 7, 11, delta_max}:
            samples.append(
                {
                    "delta": delta,
                    "r": data["r"],
                    "K_delta": str(data["K"]),
                    "Gamma_delta": str(data["Gamma"]),
                    "primitive_terms": len(data["primitive"]),
                    "fixed_gate_coefficient": str(data["fixed_gate_coefficient"]),
                }
            )
    digest = hashlib.sha256(("\n".join(rows) + "\n").encode()).hexdigest()
    return {
        "delta_max": delta_max,
        "exact_symbolic_rows": delta_max,
        "row_digest_sha256": digest,
        "samples": samples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item261_p1_punctured_cohomology_certificate.json",
    )
    parser.add_argument("--prime-max", type=int, default=401)
    parser.add_argument("--delta-max", type=int, default=67)
    args = parser.parse_args()
    assert args.prime_max >= 43
    assert args.delta_max >= 5

    output = {
        "schema": "item261-p1-punctured-cohomology-v1",
        "status": {
            "birational_transport": "PROVED_IN_REPORT",
            "Hermite_reduction": "PROVED_IN_REPORT",
            "endpoint_correction": "PROVED_IN_REPORT",
            "bounded_two_class_normal_form": "PROVED_IN_REPORT",
            "Item251_period_two_state_reduction": "PROVED_IN_REPORT",
            "unpunctured_trace_closure": "PROVED_SHARPLY_SCOPED_NO_GO",
            "all_prime_prefix_exclusion": "FALSE; explicit p=43 actual zero",
            "positive_mass_weighted_zero_theorem": "NOT_PROVED",
            "new_route1_rate": "0",
            "finite_scan": "EXACT_FINITE_ONLY",
        },
        "exact_normal_form": {
            "Kummer_curve": "y^6=(1-x/2)^3/x",
            "elliptic_curve": "Z^2=X^3-1/2, X=y^2/(1-x/2), Z=yX, x=X^-3",
            "operator": (
                "D(R)=F R'+(5/6)F'R, so D(R)dx/y=d(Ry^5), "
                "F=(1-x/2)^3/x"
            ),
            "Hermite_step": (
                "D(x^(j+1)/(1-x/2)^2)=(6j+1)x^(j-1)/6-(3j+2)x^j/6"
            ),
            "cohomology": (
                "w_delta dx/y=[w_0-Gamma_delta*x^-1]dx/y+d(P_delta*y^5)"
            ),
            "K_delta": (
                "sum_(j=0)^(delta-1) product_(i=0)^(j-1)(6i+1)/(3i+2)"
            ),
            "Gamma_delta": (
                "sum_(j=0)^(delta-1) product_(i=0)^j(6i+1)/(3i+2)"
            ),
            "endpoint_lemma": (
                "Lambda(D(R_j))=-3h_(q-j+1)/(2(3j-1))-epsilon(3j-1)/6"
            ),
            "residual_coordinates": (
                "U=-h_q/5-epsilon; V=-H_q+2epsilon/3"
            ),
            "finite_sum": (
                "T_delta=V-5K_delta*U+epsilon(delta-5K_delta)"
            ),
            "final_prefix": "H_(q-delta)=H_q-K_delta*h_q mod p",
            "Item251_period": (
                "A_s=(-1)^m{epsilon[H_q-D_r*h_q]-1}, "
                "D_r=K_delta+C_delta*Pi_r fixed for fixed r"
            ),
        },
        "obstruction": {
            "log_class": "-3*dX/((X^3-1)Z)",
            "residue_at_alpha_beta": "-alpha/beta, alpha^3=1, beta^2=1/2",
            "consequence": (
                "nonzero residues prevent reduction to exact plus unpunctured elliptic classes"
            ),
            "scope": (
                "does not rule out a new arithmetic theorem for the punctured base period H_q"
            ),
        },
        "recurrences": {
            "base_normalized_period": (
                "Z_(q+1)=1+(4q+4)/(2q+1)Z_q, Z_q=H_q/h_q"
            ),
            "warning": (
                "successive q use different row primes p=6q+1; modular propagation is invalid"
            ),
        },
        "symbolic_replay": symbolic_replay(args.delta_max),
        "finite_field_replay": finite_field_replay(args.prime_max),
        "booking": {
            "fixed_r_ray": "only frozen O(log M)=o(M) raw weight; not a new global saving",
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "NONE",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
