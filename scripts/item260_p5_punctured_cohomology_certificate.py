#!/usr/bin/env python3
"""Exact certificate for Item 260's p == 5 (mod 6) punctured reduction.

The checker proves finite rational-function identities coefficientwise,
replays the endpoint-retaining finite-field summation formulas, and scans a
bounded set of actual rows.  All bounded row counts are EXACT FINITE ONLY.
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
RESULT_NAME = "item260_p5_punctured_cohomology_certificate.json"
ITEM254_NAME = "item254_half_binomial_arithmetic_report.md"
ITEM254_SHA256 = "971d50dab6a8f944334503c46d369151f390db534bc50ec54e1711ecf9b83a2a"


def resolve(name: str) -> Path:
    for candidate in (HERE / name, HERE.parent / "sources" / name):
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(name)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def hermite_operator(poly: dict[int, F]) -> dict[int, F]:
    """L(R)=(X^3-1/2)R'+(3/2)X^2 R."""
    out: dict[int, F] = {}
    for exponent, coefficient in poly.items():
        out = add(
            out,
            {
                exponent + 2: coefficient * (F(exponent) + F(3, 2)),
                exponent - 1: -coefficient * F(exponent, 2),
            },
        )
    return out


def reduction_data(delta: int) -> dict[str, Any]:
    """Return C_j, K_delta, primitives A_n and total primitive P_delta."""
    if delta < 1:
        raise ValueError(delta)
    exponents = [3 * j + 2 for j in range(delta)]
    c_values = [F(1)]
    primitives: list[dict[int, F]] = [{}]
    for n in exponents[1:]:
        ratio = F(2 * n - 5, n - 1)
        c_value = ratio * c_values[-1]
        primitive = add(
            monomial(-(n - 1), F(2, n - 1)),
            scale(primitives[-1], ratio),
        )
        expected = add(monomial(-n), monomial(-2, -c_value))
        assert hermite_operator(primitive) == expected
        c_values.append(c_value)
        primitives.append(primitive)

    k_value = sum(c_values, F(0))
    total_primitive: dict[int, F] = {}
    for primitive in primitives:
        total_primitive = add(total_primitive, primitive)
    total_primitive = add(total_primitive, monomial(-1, 2 * k_value))
    expected_total = monomial(1, k_value)
    for n in exponents:
        expected_total = add(expected_total, monomial(-n))
    assert hermite_operator(total_primitive) == expected_total

    # Exact partial fraction identity after multiplying by X^a(X^3-1).
    a = 3 * delta - 1
    telescoper = monomial(a + 1)
    for n in exponents:
        telescoper = add(telescoper, monomial(a - n + 3, -1))
        telescoper = add(telescoper, monomial(a - n, 1))
    assert telescoper == {0: F(1)}

    # Item-254's fixed boundary coefficient B_delta^(5).
    boundary_terms = [F(1)]
    for j in range(1, delta):
        boundary_terms.append(
            boundary_terms[-1] * F(6 * j - 1, 3 * j + 1)
        )
    assert boundary_terms == c_values
    assert sum(boundary_terms, F(0)) == k_value

    # The endpoint inhomogeneity E_n equals C_n-1 termwise.
    e_value = F(0)
    e_values = [e_value]
    for n, c_value in zip(exponents[1:], c_values[1:]):
        ratio = F(2 * n - 5, n - 1)
        e_value = ratio * e_value + F(n - 4, n - 1)
        assert e_value == c_value - 1
        e_values.append(e_value)
    assert sum(e_values, F(0)) == k_value - delta

    return {
        "delta": delta,
        "r": 3 * delta - 2,
        "a": a,
        "exponents": exponents,
        "C": c_values,
        "K": k_value,
        "E": e_values,
        "primitive": total_primitive,
    }


def fmod(value: F, p: int) -> int:
    return value.numerator * pow(value.denominator, -1, p) % p


def chi(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def prefixes(p: int, q_max: int) -> tuple[list[int], list[int]]:
    h_values = [1]
    h_sum = [1]
    h = 1
    total = 1
    for q in range(1, q_max + 1):
        h = h * (2 * q - 1) * pow(4 * q, -1, p) % p
        total = (total + h) % p
        h_values.append(h)
        h_sum.append(total)
    return h_values, h_sum


def finite_field_replay(prime_max: int) -> dict[str, Any]:
    primes = [p for p in primes_upto(prime_max) if p >= 5 and p % 6 == 5]
    prime_identities = 0
    endpoint_identities = 0
    actual_rows = 0
    localized_equalities = 0
    zero_rows: list[tuple[int, int, int, int, int]] = []
    first_rows: list[dict[str, int]] = []

    for p in primes:
        n = (p - 1) // 2
        q = (p - 5) // 6
        epsilon = chi(2, p)
        inv2 = pow(2, -1, p)
        h_values, h_sums = prefixes(p, q + 1)

        u_value = 0
        v_value = 0
        t2_value = 0
        point_data: list[tuple[int, int]] = []
        for x in range(1, p):
            if x == 1:
                continue
            character = chi(pow(x, 3, p) - inv2, p)
            point_data.append((x, character))
            u_value += x * character
            t2_value += pow(x, -2, p) * character
            v_value += (
                x * pow(pow(x, 3, p) - 1, -1, p) * character
            )
        u_value %= p
        t2_value %= p
        v_value %= p
        assert u_value == (h_values[q] - epsilon) % p
        assert t2_value == (-h_values[q] - epsilon) % p
        assert (u_value + t2_value) % p == (-2 * epsilon) % p
        assert v_value == (-h_sums[q] + 4 * epsilon * pow(3, -1, p)) % p
        prime_identities += 4

        # Endpoint-retaining summation-by-parts lemma for every relevant
        # j == 1 (mod 3) below the actual phase ceiling.
        for j in range(1, (p - 9) // 2 + 1, 3):
            observed = 0
            for x, character in point_data:
                l_value = (
                    fmod(F(3, 2) - j, p) * pow(x, 2 - j, p)
                    + fmod(F(j, 2), p) * pow(x, -j - 1, p)
                ) % p
                observed += l_value * character
            expected = epsilon * fmod(F(j - 3, 2), p) % p
            assert observed % p == expected
            endpoint_identities += 1

        for s in range(1, (p - 3) // 6 + 1):
            r_numerator = p - 6 * s - 3
            if r_numerator % 2:
                continue
            r = r_numerator // 2
            if r < 1 or r % 2 == 0:
                continue
            assert r % 6 == 1
            m = s - 1
            delta = (r + 2) // 3
            assert delta % 2 == 1
            assert m == q - delta
            data = reduction_data(delta)
            k_value = data["K"]
            assert all(value.denominator % p for value in data["C"])
            k_mod = fmod(k_value, p)

            s_value = 0
            x_localized = 0
            for x, character in point_data:
                s_value += (
                    pow(x, -r - 1, p)
                    * pow(pow(x, 3, p) - 1, -1, p)
                    * character
                )
                original_x = pow(x, -1, p)
                original_character = chi(
                    original_x
                    * (1 - pow(original_x, 3, p) * inv2),
                    p,
                )
                x_localized += (
                    pow(original_x, r + 4, p)
                    * pow(1 - pow(original_x, 3, p), -1, p)
                    * original_character
                )
            s_value %= p
            x_localized %= p
            assert s_value == x_localized
            expected_s = (
                v_value
                + k_mod * u_value
                + epsilon * (k_mod + delta)
            ) % p
            assert s_value == expected_s
            jacobi_a = 2 * m + r + 5
            direct_h = h_sums[m]
            assert direct_h == (epsilon * jacobi_a - s_value) % p
            assert direct_h == (h_sums[q] - k_mod * h_values[q]) % p
            localized_equalities += 4
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
                        "U_second_kind": u_value,
                        "V_punctured": v_value,
                        "K_delta": k_mod,
                        "H_m": direct_h,
                    }
                )

    assert (47, 7, 5, 4, 3) in zero_rows
    digest = hashlib.sha256(
        ("\n".join(",".join(map(str, row)) for row in zero_rows) + "\n").encode()
    ).hexdigest()
    return {
        "prime_max": prime_max,
        "p_eq_5_mod_6_primes": len(primes),
        "prime_level_coordinate_equalities": prime_identities,
        "endpoint_summation_by_parts_equalities": endpoint_identities,
        "actual_rows": actual_rows,
        "localized_row_equalities": localized_equalities,
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
            f"{len(data['primitive'])}"
        )
        if delta in {1, 2, 3, 5, 7, 11, delta_max}:
            samples.append(
                {
                    "delta": delta,
                    "r": data["r"],
                    "K_delta": f"{data['K'].numerator}/{data['K'].denominator}",
                    "primitive_laurent_terms": len(data["primitive"]),
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
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--prime-max", type=int, default=401)
    parser.add_argument("--delta-max", type=int, default=67)
    args = parser.parse_args()

    item254 = resolve(ITEM254_NAME)
    if sha256(item254) != ITEM254_SHA256:
        raise RuntimeError("Item254 report hash mismatch")

    output = {
        "schema": "item260-p5-punctured-cohomology-v1",
        "status": {
            "hermite_reduction": "PROVED_IN_REPORT",
            "endpoint_correction": "PROVED_IN_REPORT",
            "bounded_residual_classes": "PROVED_IN_REPORT",
            "unpunctured_trace_closure": "PROVED_SHARPLY_SCOPED_NO_GO",
            "all_prime_exclusion": "FALSE_UNIFORMLY; explicit actual zero",
            "positive_mass_weighted_zero_theorem": "NOT_PROVED",
            "new_route1_rate": "0",
            "finite_scan": "EXACT_FINITE_ONLY",
        },
        "exact_normal_form": {
            "curve": "Y^2=X^3-1/2",
            "weight": "w_r=X^(-r-1)/(X^3-1), r=3delta-2",
            "operator": "L(R)=(X^3-1/2)R'+(3/2)X^2R, so L(R)dX/Y=d(RY)",
            "cohomology": (
                "w_r dX/Y = [X/(X^3-1)+K_delta X]dX/Y - d(P_delta Y)"
            ),
            "K_delta": (
                "sum_(j=0)^(delta-1) product_(i=0)^(j-1)(6i+5)/(3i+4)"
            ),
            "endpoint_lemma": (
                "Lambda_p(L(X^-j))=epsilon*(j-3)/2 for j=1 mod 3"
            ),
            "residual_coordinates": (
                "U_p=h_q-epsilon; V_p=-H_q+4epsilon/3, q=(p-5)/6"
            ),
            "final": "H_(q-delta)=H_q-K_delta*h_q mod p",
        },
        "obstruction": {
            "log_class": "[X/(X^3-1)]dX/Y",
            "residue_at_alpha_beta": "1/(3 alpha beta), alpha^3=1, beta^2=1/2",
            "consequence": (
                "nonzero residues prevent reduction to exact plus unpunctured regular/second-kind de Rham classes"
            ),
            "scope": (
                "does not rule out a new arithmetic theorem for the punctured base period H_q"
            ),
        },
        "recurrences": {
            "base_normalized_period": (
                "Z_(q+1)=1+(4q+4)/(2q+1) Z_q, Z_q=H_q/h_q"
            ),
            "warning": (
                "successive q use different row primes p=6q+5; modular propagation is invalid"
            ),
        },
        "symbolic_replay": symbolic_replay(args.delta_max),
        "finite_field_replay": finite_field_replay(args.prime_max),
        "dependencies": {ITEM254_NAME: sha256(item254)},
        "booking": {
            "fixed_r_ray": "at most one row per global M, hence O(log M)=o(M) raw weight",
            "new_positive_mass_reduction": "0",
            "conclusion_about_e_plus_pi": "NONE",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
