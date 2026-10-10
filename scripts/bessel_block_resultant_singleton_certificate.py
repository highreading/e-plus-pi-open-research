#!/usr/bin/env python3
"""Finite checks for the Bessel block/resultant singleton dichotomy.

The all-index identities and asymptotic estimates are proved in
``sources/bessel_block_resultant_singleton_dichotomy.md``.  This script
checks representative exact instances and records explicitly labelled
finite lcm diagnostics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


def q_values(limit: int) -> list[int]:
    q = [1, 1]
    for n in range(2, limit + 1):
        q.append((4 * n - 2) * q[-1] + q[-2])
    return q[: limit + 1]


def p_values(limit: int) -> list[int]:
    p = [1, 3]
    for n in range(2, limit + 1):
        p.append((4 * n - 2) * p[-1] + p[-2])
    return p[: limit + 1]


def continuant(d: int, n: int) -> int:
    if d == 0:
        return 0
    if d == 1:
        return 1
    p0, p1 = 0, 1
    for j in range(d - 1):
        p0, p1 = p1, (4 * n + 4 * j + 6) * p1 + p0
    return p1


def vp(value: int, prime: int) -> int:
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def log_int(value: int) -> float:
    """Stable natural logarithm of an arbitrarily large positive integer."""
    bits = value.bit_length()
    keep = min(bits, 53)
    lead = value >> (bits - keep)
    return math.log(lead) + (bits - keep) * math.log(2.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/bessel_block_resultant_singleton_certificate.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/bessel_block_resultant_singleton_dichotomy.md"),
    )
    args = parser.parse_args()

    q = q_values(1360)
    p = p_values(1360)
    transition_checks = []
    for n in (0, 1, 3, 10):
        for d in range(1, 8):
            lhs = continuant(d + 1, n) * continuant(d - 1, n + 1)
            lhs -= continuant(d, n) * continuant(d, n + 1)
            assert lhs == (-1) ** d
            if n + d < len(q):
                value = continuant(d, n) * q[n + 1]
                value += continuant(d - 1, n + 1) * q[n]
                assert value == q[n + d]
            for e in range(d + 1, 9):
                determinant = continuant(e, n) * continuant(d - 1, n + 1)
                determinant -= continuant(d, n) * continuant(e - 1, n + 1)
                assert determinant == (-1) ** d * continuant(e - d, n + d)
            transition_checks.append({"n": n, "d": d, "cassini": lhs})

    reflection_checks = []
    for n in range(1, 101):
        reflected = continuant(2 * n + 1, -n - 1)
        expected = (-1) ** n * p[n] * q[n]
        assert reflected == expected
        wronskian = p[n] * q[n - 1] - p[n - 1] * q[n]
        assert wronskian == 2 * (-1) ** (n - 1)
        assert math.gcd(p[n], q[n]) == 1
        reflection_checks.append(
            {
                "n": n,
                "reflection": str(reflected),
                "wronskian": wronskian,
            }
        )

    x = sp.Symbol("x")
    interpolation_checks = []
    for n_block in range(2, 8):
        points = [(j, q[n_block + j]) for j in range(n_block)]
        interpolant = sp.interpolate(points, x)
        f_poly = sp.Poly(sp.factorial(n_block - 1) * interpolant, x)
        assert all(coefficient.q == 1 for coefficient in f_poly.all_coeffs())
        b_poly = sp.Poly(sp.prod(x - j for j in range(n_block)), x)
        product = math.prod(q[n_block : 2 * n_block])
        resultant = abs(int(sp.resultant(b_poly.as_expr(), f_poly.as_expr(), x)))
        expected = math.factorial(n_block - 1) ** n_block * product
        assert resultant == expected
        grid_disc = abs(int(sp.discriminant(b_poly.as_expr(), x)))
        expected_disc = math.prod(math.factorial(j) ** 2 for j in range(1, n_block))
        assert grid_disc == expected_disc
        interpolation_checks.append(
            {
                "N": n_block,
                "resultant": str(resultant),
                "grid_discriminant": str(grid_disc),
            }
        )

    # The p=13 block [8,16) has one zero, of exact depth two.
    singleton = []
    for index in range(8, 16):
        singleton.append(
            {
                "index": index,
                "residue_mod_13": q[index] % 13,
                "valuation_if_zero": vp(q[index], 13) if q[index] % 13 == 0 else 0,
            }
        )
    assert [(z["index"], z["valuation_if_zero"]) for z in singleton if z["valuation_if_zero"]] == [(8, 2)]
    derivative_mod_13 = 1
    for index in range(9, 16):
        derivative_mod_13 = derivative_mod_13 * q[index] % 13
    derivative_mod_13 = (-derivative_mod_13) % 13  # (-1)^(8-1)
    assert derivative_mod_13 == 8

    # An actual high singleton: in [680,1360), q_1359 has 11-adic
    # valuation five.  Since b_11(680)=3, its excess depth is three.
    lift_representatives = [6, 28, 28, 1359, 1359]
    lift_moduli = [11, 11**2, 11**3, 11**4, 11**5]
    assert all(q[index] % modulus == 0 for index, modulus in
               zip(lift_representatives, lift_moduli))
    high_singleton = {
        "prime": 11,
        "block": [680, 1360],
        "index": 1359,
        "valuation": vp(q[1359], 11),
        "threshold_b": 3,
        "excess_depth": vp(q[1359], 11) - 3 + 1,
        "lift_representatives": lift_representatives,
        "lift_moduli": lift_moduli,
    }
    assert high_singleton["valuation"] == 5
    assert high_singleton["excess_depth"] == 3

    lcm_diagnostics = []
    for n_block in (40, 80, 160, 320):
        product = 1
        block_lcm = 1
        for value in q[n_block : 2 * n_block]:
            product *= value
            block_lcm = math.lcm(block_lcm, value)
        lcm_diagnostics.append(
            {
                "N": n_block,
                "log_lcm_over_log_product": log_int(block_lcm) / log_int(product),
                "log_lcm_over_N2_log_N": log_int(block_lcm)
                / (n_block * n_block * math.log(n_block)),
            }
        )

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    output = {
        "description": "Finite exact checks for the Bessel block transition, central reflection factorization, interpolation resultant, singleton subresultant example, and explicitly diagnostic lcm ratios.",
        "scope_warning": "The lcm ratios are finite diagnostics. The all-index identities and asymptotics are proved in the source note; this file does not prove an o(N^2 log N) smooth-lcm bound.",
        "script_sha256": sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": sha256(source_path),
        "transition_checks": transition_checks,
        "reflection_checks": reflection_checks,
        "interpolation_checks": interpolation_checks,
        "singleton_p13_block_8_16": singleton,
        "singleton_derivative_mod_13": derivative_mod_13,
        "high_singleton_p11": high_singleton,
        "lcm_diagnostics": lcm_diagnostics,
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
