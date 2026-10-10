#!/usr/bin/env python3
"""Portable exact checker for Item 253's half-binomial phase diagonal.

Only Python's standard library is used.  Algebraic identities are checked
exactly over the integers/rationals.  Modular row counts are bounded evidence
and are emitted under the key EXACT_FINITE_ONLY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent


def primes_up_to(bound: int) -> list[int]:
    sieve = bytearray(b"\x01") * (bound + 1)
    if bound >= 0:
        sieve[0] = 0
    if bound >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(bound) + 1):
        if sieve[q]:
            start = q * q
            sieve[start : bound + 1 : q] = b"\x00" * (((bound - start) // q) + 1)
    return [q for q in range(2, bound + 1) if sieve[q]]


def actual_rows(bound: int):
    for p in primes_up_to(bound):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            numerator = p - 6 * s - 3
            if numerator <= 0:
                break
            if numerator % 2:
                continue
            r = numerator // 2
            if r >= 1 and r % 2 == 1 and r % 3 != 0:
                m = s - 1
                delta = r + 4
                assert p == 6 * m + 2 * delta + 1
                assert delta >= 5 and delta % 6 in (3, 5)
                yield p, r, s, m, delta


def q_poly(delta: int, j: int) -> int:
    return 28 * j * j + (21 * delta + 25) * j + 4 * delta * delta + 9 * delta + 5


def k_exact(delta: int, m: int) -> F:
    n = 3 * m + delta
    return sum((F((-1) ** j * math.comb(n, j), 2**j) for j in range(m + 1)), F(0))


def b_exact(delta: int, m: int) -> int:
    value = 2 ** (3 * m + delta) * k_exact(delta, m) - 1
    assert value.denominator == 1
    return value.numerator


def delta_three_coefficient(delta: int, j: int) -> int:
    n = 3 * j + delta
    total = 0
    for shift, coefficient in ((0, 8), (1, -5), (2, 1)):
        k = j + 1 - shift
        if 0 <= k <= n:
            total += coefficient * (-1) ** k * math.comb(n, k) * 2 ** (n - k)
    return total


def delta_closed(delta: int, j: int) -> int:
    numerator = (
        (-1) ** (j + 1)
        * 2 ** (2 * j + delta)
        * math.comb(3 * j + delta, j)
        * q_poly(delta, j)
    )
    denominator = (j + 1) * (2 * j + delta + 1)
    assert numerator % denominator == 0
    return numerator // denominator


def h_prefix_mod(m: int, p: int) -> tuple[int, int]:
    term = 1
    total = 1
    for j in range(m):
        numerator = 2 * j + 1
        denominator = 4 * (j + 1)
        assert 0 < numerator < p
        assert 0 < denominator < p
        term = term * numerator * pow(denominator, -1, p) % p
        total = (total + term) % p
    return term, total


def k_mod(delta: int, m: int, p: int) -> int:
    n = 3 * m + delta
    inv2 = pow(2, -1, p)
    return sum(
        (math.comb(n, j) % p) * ((-inv2) % p) ** j
        for j in range(m + 1)
    ) % p


def delta_mod_direct(delta: int, j: int, p: int) -> int:
    return delta_closed(delta, j) % p


def exact_identity_audit() -> dict[str, object]:
    rows = []
    increment_checks = 0
    ratio_checks = 0
    for delta in range(3, 42, 2):
        for m in range(0, 15):
            b0 = b_exact(delta, m)
            b1 = b_exact(delta, m + 1)
            direct = b1 - b0
            three = delta_three_coefficient(delta, m)
            closed = delta_closed(delta, m)
            assert direct == three == closed
            increment_checks += 1
            if m < 14:
                left = delta_closed(delta, m + 1) * (
                    (m + 2)
                    * (2 * m + delta + 2)
                    * (2 * m + delta + 3)
                    * q_poly(delta, m)
                )
                right = -4 * delta_closed(delta, m) * (
                    (3 * m + delta + 1)
                    * (3 * m + delta + 2)
                    * (3 * m + delta + 3)
                    * q_poly(delta, m + 1)
                )
                assert left == right
                ratio_checks += 1
        rows.append((delta, b_exact(delta, 0), b_exact(delta, 1), b_exact(delta, 2)))

    digest = hashlib.sha256(
        "".join(f"{a},{b},{c},{d}\n" for a, b, c, d in rows).encode("ascii")
    ).hexdigest()
    return {
        "delta_values": len(rows),
        "increment_equalities": increment_checks,
        "cross_multiplied_ratio_equalities": ratio_checks,
        "row_digest_sha256": digest,
        "integrality_checked": True,
    }


def cartier_polynomial_audit(prime_bound: int = 101) -> dict[str, object]:
    checked = 0
    coefficient_equalities = 0
    total_sum_equalities = 0
    for p in primes_up_to(prime_bound):
        if p < 5:
            continue
        n = (p - 1) // 2
        epsilon = pow(2, n, p)
        hs = []
        term = 1
        total = 0
        for k in range(n + 1):
            if k:
                term = term * (2 * k - 1) * pow(4 * k, -1, p) % p
            total = (total + term) % p
            hs.append(total)
        assert hs[-1] == epsilon

        left = [0] * (n + 2)
        for k, value in enumerate(hs):
            left[k] = (left[k] + value) % p
            left[k + 1] = (left[k + 1] - value) % p
        right = [0] * (n + 2)
        inv2 = pow(2, -1, p)
        for k in range(n + 1):
            right[k] = math.comb(n, k) * pow(-inv2, k, p) % p
        right[n + 1] = (-epsilon) % p
        assert left == right
        assert sum(hs) % p == 0
        coefficient_equalities += len(left)
        total_sum_equalities += 1
        checked += 1

    return {
        "checked_primes": checked,
        "prime_bound": prime_bound,
        "polynomial_coefficient_equalities": coefficient_equalities,
        "C_at_1_zero_equalities": total_sum_equalities,
        "six_section_kernel": "z^m-z^(m+6) vanishes at every sixth root when m+6<=n",
    }


def modular_row(p: int, r: int, s: int, m: int, delta: int) -> dict[str, int | bool]:
    n = 3 * m + delta
    assert n == (p - 1) // 2 < p
    h_m, h_sum = h_prefix_mod(m, p)
    k_value = k_mod(delta, m, p)
    assert k_value == h_sum
    epsilon = pow(2, n, p)
    assert epsilon in (1, p - 1)
    b_value = (pow(2, n, p) * k_value - 1) % p
    assert h_sum == epsilon * (b_value + 1) % p

    b_from_sum = (pow(2, delta, p) - 1) % p
    all_increment_nonzero = True
    intermediate_q_zeros = 0
    for j in range(m):
        increment = delta_mod_direct(delta, j, p)
        b_from_sum = (b_from_sum + increment) % p
        if increment == 0:
            all_increment_nonzero = False
        if q_poly(delta, j) % p == 0:
            intermediate_q_zeros += 1
        # All non-Q factors in the closed formula are units.
        assert 0 < j + 1 < p
        assert 0 < 2 * j + delta + 1 < p
        assert 0 <= j <= 3 * j + delta < p
        expected_zero = q_poly(delta, j) % p == 0
        assert (increment == 0) == expected_zero
    assert b_from_sum == b_value

    # Terminal factor and the two exact phase identities.
    q_terminal = q_poly(delta, m)
    assert 2 * q_terminal - (2 * m * m - m + 3) == p * (4 * delta + 9 * m + 7)
    assert 18 * q_terminal - (2 * delta * delta + 5 * delta + 29) == p * (
        35 * delta + 84 * m + 61
    )
    assert 2 * delta * delta + 5 * delta + 29 == 2 * r * r + 21 * r + 81

    terminal_increment = delta_mod_direct(delta, m, p)
    fixed_r_zero = (2 * r * r + 21 * r + 81) % p == 0
    assert (terminal_increment == 0) == (q_terminal % p == 0) == fixed_r_zero

    # Unit bounds, including the ratio's non-Q factors.
    assert 0 <= m <= n < p
    assert 0 < m + 1 < p
    assert 0 < 2 * m + delta + 1 < p
    assert 0 < m + 2 < p
    assert 0 < 2 * m + delta + 2 < 2 * m + delta + 3 < p

    return {
        "p": p,
        "r": r,
        "s": s,
        "m": m,
        "delta": delta,
        "epsilon_2": epsilon,
        "h_m": h_m,
        "H_m": h_sum,
        "B_m": b_value,
        "Q_terminal": q_terminal % p,
        "terminal_increment": terminal_increment,
        "terminal_increment_zero": terminal_increment == 0,
        "all_increments_through_terminal_nonzero": all_increment_nonzero
        and terminal_increment != 0,
        "intermediate_Q_zero_count": intermediate_q_zeros,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=601)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item253_half_binomial_phase_certificate.json",
    )
    args = parser.parse_args()
    assert args.bound >= 127

    exact = exact_identity_audit()
    rows = []
    terminal_zeros = []
    h_zeros = []
    intermediate_q_zero_rows = 0
    max_terminal_zeros_per_prime: dict[int, int] = {}
    for values in actual_rows(args.bound):
        row = modular_row(*values)
        rows.append(row)
        if row["terminal_increment_zero"]:
            terminal_zeros.append(
                {key: row[key] for key in ("p", "r", "s", "m", "delta", "H_m")}
            )
            p = int(row["p"])
            max_terminal_zeros_per_prime[p] = max_terminal_zeros_per_prime.get(p, 0) + 1
        if row["H_m"] == 0:
            h_zeros.append(
                {
                    key: row[key]
                    for key in (
                        "p",
                        "r",
                        "s",
                        "m",
                        "delta",
                        "Q_terminal",
                        "all_increments_through_terminal_nonzero",
                    )
                }
            )
        if row["intermediate_Q_zero_count"]:
            intermediate_q_zero_rows += 1

    assert max(max_terminal_zeros_per_prime.values(), default=0) <= 2
    witness_h = next(row for row in rows if row["p"] == 43 and row["r"] == 11 and row["s"] == 3)
    assert witness_h["H_m"] == 0
    assert witness_h["all_increments_through_terminal_nonzero"]
    witness_delta = next(
        row for row in rows if row["p"] == 127 and row["r"] == 17 and row["s"] == 15
    )
    assert witness_delta["terminal_increment_zero"]
    assert witness_delta["H_m"] == 109

    digest = hashlib.sha256(
        "".join(
            f"{row['p']},{row['r']},{row['s']},{row['m']},{row['delta']},"
            f"{row['H_m']},{row['B_m']},{row['Q_terminal']},"
            f"{row['terminal_increment']}\n"
            for row in rows
        ).encode("ascii")
    ).hexdigest()

    result = {
        "schema": "item253-half-binomial-phase-certificate-v1",
        "imports_item_code": False,
        "theorems": {
            "phase": "p=6m+2delta+1, delta=r+4, n=3m+delta=(p-1)/2",
            "diagonal": "K_(delta,m)=sum_(j<=m) C(3m+delta,j)(-1/2)^j",
            "phase_recovery": "H_m=epsilon_2*(B_(delta,m)+1) mod p",
            "integer_normalization": "B_(delta,m)=2^(3m+delta)K_(delta,m)-1",
            "increment": (
                "Delta=(-1)^(m+1)2^(2m+delta)C(3m+delta,m)Q_delta(m)/"
                "((m+1)(2m+delta+1))"
            ),
            "Q_delta": "28m^2+(21delta+25)m+4delta^2+9delta+5",
            "terminal_zero_criterion": (
                "Delta_(delta,m)=0 mod p iff p divides 2m^2-m+3 iff p divides "
                "2r^2+21r+81"
            ),
            "fixed_r_consequence": "terminal-zero primes divide one fixed nonzero integer",
            "fixed_p_consequence": "at most two terminal-zero phase indices; discriminant -23",
            "six_section_barrier": (
                "value-only evaluations at sixth roots do not isolate H_m; "
                "z^m-z^(m+6) is an ambient kernel vector"
            ),
        },
        "exact_identity_audit": exact,
        "cartier_polynomial_audit": cartier_polynomial_audit(),
        "unit_audit": {
            "all_actual_row_denominators_are_p_units": True,
            "n_bound": "0<=m<=n=(p-1)/2<p",
            "closed_increment_bounds": "m+1<p and 2m+delta+1<p",
            "ratio_non_Q_bounds": "m+2<p and 2m+delta+2<2m+delta+3<p",
            "Q_never_inverted_mod_p": True,
            "constants_2_3_6_18_are_units": True,
        },
        "EXACT_FINITE_ONLY": {
            "prime_bound": args.bound,
            "actual_rows": len(rows),
            "terminal_increment_zero_count": len(terminal_zeros),
            "terminal_increment_zero_witnesses_first_12": terminal_zeros[:12],
            "H_m_zero_count": len(h_zeros),
            "H_m_zero_witnesses_first_12": h_zeros[:12],
            "rows_with_an_intermediate_Q_zero": intermediate_q_zero_rows,
            "maximum_terminal_zeros_for_one_prime_in_scan": max(
                max_terminal_zeros_per_prime.values(), default=0
            ),
            "row_digest_sha256": digest,
            "first_rows": rows[:8],
            "scope": "bounded exact replay only; no density or rate inference",
        },
        "separation_witnesses": {
            "H_zero_all_increments_nonzero": witness_h,
            "terminal_increment_zero_H_nonzero": witness_delta,
        },
        "OPEN": [
            "evaluation or weighted zero theorem for the incomplete hypergeometric sum",
            "link from the terminal increment to the actual Item-251 collision gate",
            "derivative or Hasse-jet invariant separating the six-section residual",
            "any new divisibility exponent, capacity reduction, or conclusion about e+pi",
        ],
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

