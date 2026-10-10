#!/usr/bin/env python3
"""Exact finite diagnostic for the general-prime content criterion.

For every odd prime p<=bound, p!=5, and every 1<=r<p, this computes
J_r=(N_r,a_r*T_r) modulo p and tests whether it is a proper ideal of
F_p[t]/(t^2+t-1).  The scan is finite evidence, not an all-prime theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


Elt = tuple[int, int, int, int]
ONE: Elt = (1, 0, 0, 0)
ZERO: Elt = (0, 0, 0, 0)
ETA: Elt = (0, -1, 0, -1)


def add(a: Elt, b: Elt, p: int) -> Elt:
    return tuple((a[j] + b[j]) % p for j in range(4))  # type: ignore[return-value]


def scale(scalar: int, a: Elt, p: int) -> Elt:
    return tuple(scalar * value % p for value in a)  # type: ignore[return-value]


def multiply(a: Elt, b: Elt, p: int) -> Elt:
    raw = [0] * 7
    for j, aj in enumerate(a):
        for k, bk in enumerate(b):
            raw[j + k] += aj * bk
    # zeta^4=-(1+zeta+zeta^2+zeta^3).
    for degree in range(6, 3, -1):
        value = raw[degree]
        for target in range(degree - 4, degree):
            raw[target] -= value
    return tuple(value % p for value in raw[:4])  # type: ignore[return-value]


def ideal_is_proper(n_value: tuple[int, int], t_value: tuple[int, int], p: int) -> bool:
    """Test rank<2 for [M(n)|M(t)] in Z[t], t^2+t-1=0."""

    a, b = n_value
    c, d = t_value
    minors = (
        a * a - a * b - b * b,
        c * c - c * d - d * d,
        a * d - b * c,
        a * (c - d) - b * d,
        b * d - (a - b) * c,
        b * (c - d) - (a - b) * d,
    )
    return all(value % p == 0 for value in minors)


def scan(max_prime: int) -> list[dict[str, int]]:
    hits: list[dict[str, int]] = []
    for p in sp.primerange(3, max_prime + 1):
        if p == 5:
            continue
        eta = tuple(value % p for value in ETA)
        eta_bar = add(ONE, scale(-1, eta, p), p)
        x_power = y_power = ONE
        p_x = p_y = ONE
        c_x = c_y = ZERO
        a_value = 1
        top_c = 0
        for r in range(1, p):
            x_power = multiply(x_power, eta, p)
            y_power = multiply(y_power, eta_bar, p)
            p_x = add(x_power, scale(-r, p_x, p), p)
            p_y = add(y_power, scale(-r, p_y, p), p)
            top_c = (top_c + a_value) % p
            a_value = (1 - r * a_value) % p
            c_x = add(scale(-r, c_x, p), scale(top_c, x_power, p), p)
            c_y = add(scale(-r, c_y, p), scale(top_c, y_power, p), p)

            n_raw = multiply(p_x, p_y, p)
            d_raw = add(
                multiply(p_x, c_y, p),
                scale(-1, multiply(p_y, c_x, p), p),
                p,
            )
            # Fixed and anti-fixed lattice checks, followed by coordinates
            # N=n0+n1*t and D/(zeta-zeta^-1)=d0+d1*t.
            if n_raw[1] or (n_raw[2] - n_raw[3]) % p:
                raise AssertionError("N_r was not fixed by conjugation")
            if (d_raw[1] - 2 * d_raw[0]) % p or (
                d_raw[2] + d_raw[3] - 2 * d_raw[0]
            ) % p:
                raise AssertionError("D_r was not anti-fixed")
            n_coordinates = (n_raw[0] - n_raw[2], -n_raw[2])
            at_coordinates = (
                a_value * d_raw[0],
                a_value * (d_raw[2] - d_raw[0]),
            )
            if ideal_is_proper(n_coordinates, at_coordinates, p):
                hits.append({"p": int(p), "r": r})
    return hits


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=1000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/algebraic_unit_two_log_n5_general_prime_probe_p1000.json"),
    )
    args = parser.parse_args()
    if args.max_prime < 19:
        raise ValueError("max-prime must be at least 19")
    hits = scan(args.max_prime)
    if args.max_prime == 1000 and hits != [{"p": 19, "r": 15}]:
        raise AssertionError(f"unexpected default-range hits: {hits}")
    script = Path(__file__).resolve()
    result = {
        "description": "Exact finite diagnostic for J_r=(N_r,a_r*T_r).",
        "range": f"odd primes p<= {args.max_prime}, p!=5; 1<=r<p",
        "hits": hits,
        "script_sha256": file_sha256(script),
        "scope_warning": "Finite scan only; it does not exclude a hit at a later prime.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
