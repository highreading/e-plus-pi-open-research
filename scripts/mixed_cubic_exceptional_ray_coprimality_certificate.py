#!/usr/bin/env python3
"""Exact modular replay for the exceptional ray p = 10m + 3.

This checks the L/rho orientation signs using two independent coefficient
recurrences.  The accompanying markdown file contains the uniform proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def prime_flags(limit: int) -> bytearray:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return flags


def inverses_upto(limit: int, prime: int) -> list[int]:
    inverse = [0] * (limit + 1)
    inverse[1] = 1
    for value in range(2, limit + 1):
        inverse[value] = (
            prime - (prime // value) * inverse[prime % value] % prime
        )
    return inverse


def original_log_pair(m_value: int, prime: int) -> tuple[int, int]:
    """Return the actual rational residues (L0,L1) modulo p."""
    target = 4 * m_value + 1
    inverse = inverses_upto(target, prime)
    inverse_minus_four = pow(prime - 4, prime - 2, prime)
    coefficient = [pow(2, 2 * m_value - 2, prime)]
    for degree in range(target):
        rhs = (20 * m_value - 8 - 10 * degree) * coefficient[degree]
        if degree >= 1:
            rhs += (
                (10 * degree + 10 - 20 * m_value)
                * coefficient[degree - 1]
            )
        if degree >= 2:
            rhs += (
                (10 * m_value - 5 * degree - 6)
                * coefficient[degree - 2]
            )
        if degree >= 3:
            rhs += (
                (degree + 1 - 4 * m_value) * coefficient[degree - 3]
            )
        coefficient.append(
            rhs * inverse[degree + 1] * inverse_minus_four % prime
        )

    r_value = 4 * m_value
    ell0_over_two = (
        2 * coefficient[r_value]
        - 2 * coefficient[r_value - 1]
        + coefficient[r_value - 2]
    ) % prime
    ell1_over_two = coefficient[r_value + 1]
    return 2 * ell0_over_two % prime, 2 * ell1_over_two % prime


def rho_values(m_value: int, prime: int) -> list[int]:
    """Compute rho_0,...,rho_6 independently from B(x)^(6m)."""
    n_value = 4 * m_value + 3
    target = n_value - 1
    exponent = 6 * m_value
    inverse = inverses_upto(target, prime)
    b_coefficient = (4, 10, 10, 5, 1)

    # Coefficients c_j of B(x)^exponent, from B P' = exponent B' P.
    coefficient = [pow(4, exponent, prime)]
    for degree in range(target):
        rhs = 0
        for power in range(1, 5):
            old_index = degree - power + 1
            if old_index < 0:
                continue
            rhs += (
                b_coefficient[power]
                * (old_index - exponent * power)
                * coefficient[old_index]
            )
        next_value = (
            -rhs
            * pow(4, prime - 2, prime)
            * inverse[degree + 1]
        ) % prime
        coefficient.append(next_value)

    inverse_four = pow(4, prime - 2, prime)
    rho = []
    for power in range(7):
        value = 0
        for offset in range(power + 1):
            value += (
                math.comb(power, offset)
                * coefficient[target - offset]
            )
        rho.append(value * inverse_four % prime)
    return rho


def verify_row(m_value: int) -> dict[str, int | str]:
    prime = 10 * m_value + 3
    n_value = 4 * m_value + 3
    if 5 * n_value != 2 * prime + 9:
        raise AssertionError((m_value, "linear identity"))
    if not (n_value < prime and 6 * m_value + 5 < prime):
        raise AssertionError((m_value, "unit inequalities"))

    ell0, ell1 = original_log_pair(m_value, prime)
    rho = rho_values(m_value, prime)
    inverse_three = pow(3, prime - 2, prime)

    from_rho_ell1 = -4 * (
        rho[3] - rho[2] + rho[1] - rho[0]
    ) % prime
    from_rho_ell0 = 4 * (
        rho[6]
        - 2 * rho[5]
        + 3 * rho[4]
        - 4 * rho[3]
        + 3 * rho[2]
        - 2 * rho[1]
        + rho[0]
    ) % prime
    if (ell0, ell1) != (from_rho_ell0, from_rho_ell1):
        raise AssertionError(
            (m_value, "orientation", ell0, ell1, from_rho_ell0, from_rho_ell1)
        )

    anchor = math.comb(5 * m_value + 2, m_value) % prime
    checks = {
        "rho0": rho[0] == 0,
        "rho4": rho[4] == 0,
        "rho2_anchor": 4 * rho[2] % prime == anchor,
        "rho5_reduction": (
            rho[5]
            == (n_value - 2) * inverse_three * rho[1] % prime
        ),
        "rho6_reduction": rho[6] == 2 * m_value * rho[2] % prime,
        "parity_zero": (
            rho[3] == 0 if m_value % 2 == 0 else rho[1] == 0
        ),
        "anchor_unit": anchor != 0,
        "not_common_zero": ell0 != 0 or ell1 != 0,
    }
    if not all(checks.values()):
        raise AssertionError((m_value, checks, rho, ell0, ell1))

    reduced_ell0_over_four = (
        (2 * m_value + 3) * rho[2]
        - 8 * (m_value + 1) * inverse_three * rho[1]
        - 4 * rho[3]
    ) % prime
    if ell0 != 4 * reduced_ell0_over_four % prime:
        raise AssertionError((m_value, "reduced L0"))

    return {
        "m": m_value,
        "p": prime,
        "L0_mod_p": ell0,
        "L1_mod_p": ell1,
        "rho2_mod_p": rho[2],
        "vanishing_parity_residue": "rho3" if m_value % 2 == 0 else "rho1",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=2_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    flags = prime_flags(10 * args.max_m + 3)
    tested = 0
    samples = []
    for m_value in range(1, args.max_m + 1):
        prime = 10 * m_value + 3
        if not flags[prime]:
            continue
        row = verify_row(m_value)
        tested += 1
        if len(samples) < 12 or m_value == args.max_m:
            samples.append(row)

    payload = {
        "schema": "mixed-cubic-exceptional-ray-coprimality-v2",
        "generator": Path(__file__).name,
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "max_m": args.max_m,
        "tested_prime_ray_indices": tested,
        "identities_checked": [
            "exact original Taylor L0,L1 equal the oriented rho formulas",
            "rho0=rho4=0",
            "4 rho2 = binomial(5m+2,m) != 0 mod p",
            "rho5=(n-2)rho1/3 and rho6=2m rho2",
            "rho3=0 for even m; rho1=0 for odd m",
            "L0,L1 are not simultaneously zero",
        ],
        "sample_rows": samples,
        "warning": "finite replay; the companion proof is uniform",
    }
    rendered = json.dumps(payload, indent=2) + "\n"
    print(rendered)
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()

