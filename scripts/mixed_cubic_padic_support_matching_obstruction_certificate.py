#!/usr/bin/env python3
"""Deterministic replay for the mixed-cubic p-adic support obstruction.

The all-parameter proofs are in the companion source.  This script checks
the pinned inputs and replays exact instances of every algebraic identity.
It makes no classification claim about e+pi.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "mixed_cubic_padic_support_matching_obstruction.md"
OUTPUT = ROOT / "results" / "mixed_cubic_padic_support_matching_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/padic_subspace_prime_support_transcendence_criterion.md":
        "384c195a8e113a817f9bbc08ad68b9eca1733491a99508cbfc53d76d8d7c637c",
    "sources/mixed_cubic_boundary_cartier_content_and_recurrence.md":
        "286d9cf4d3591a1a9b9fefc6dd3ee3dcc9f7c2ba49a73310909491814544d9e8",
    "sources/mixed_cubic_fixed_circle_complex_laplace_theorem.md":
        "ef8cc49a5a9b5533da790be732a7a5144be22cefacca8253320d297e22359318",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primes_upto(n: int) -> list[int]:
    return list(sp.primerange(2, n + 1))


def lcm_upto(n: int) -> int:
    value = 1
    for j in range(1, n + 1):
        value = math.lcm(value, j)
    return value


def d_p(n: int, k: int, prime: int) -> int:
    r = n % prime
    s = k % prime
    if s == 0:
        return 2 * r
    return 2 * r + 3 * (prime - s)


def cartier_product(m: int) -> int:
    value = 1
    for prime in primes_upto(6 * m):
        if prime == 2:
            continue
        if d_p(6 * m, 4 * m + 1, prime) <= prime - 2 and d_p(
            6 * m, 4 * m + 2, prime
        ) <= prime - 2:
            value *= prime
    return value


def beta_pair(n: int) -> tuple[int, int]:
    """Return (p_n,q_n) for the standard beta form.

    Initial values are (p_0,q_0)=(1,1), (p_1,q_1)=(3,1), and both
    coordinates obey z_n=(4n-2)z_{n-1}+z_{n-2}.
    """
    if n == 0:
        return 1, 1
    p_prev2, p_prev1 = 1, 3
    q_prev2, q_prev1 = 1, 1
    if n == 1:
        return p_prev1, q_prev1
    for j in range(2, n + 1):
        p_now = (4 * j - 2) * p_prev1 + p_prev2
        q_now = (4 * j - 2) * q_prev1 + q_prev2
        p_prev2, p_prev1 = p_prev1, p_now
        q_prev2, q_prev1 = q_prev1, q_now
    return p_prev1, q_prev1


def outside_part(value: int, selected_primes: tuple[int, ...]) -> int:
    value = abs(value)
    assert value > 0
    for prime in selected_primes:
        while value % prime == 0:
            value //= prime
    return value


def fresh_prime(start: int, forbidden_product: int, used: set[int]) -> int:
    prime = int(sp.nextprime(start))
    while forbidden_product % prime == 0 or prime in used:
        prime = int(sp.nextprime(prime))
    return prime


def replay_case(m: int, used: set[int]) -> dict[str, int | str]:
    n = 2 * m
    p, q = beta_pair(n)
    assert math.gcd(p, q) == 1

    middle = math.prod(prime for prime in primes_upto(3 * m - 1) if 2 * m < prime < 3 * m)
    ambient_lcm = lcm_upto(4 * m + 1)
    assert ambient_lcm % middle == 0
    k_value = ambient_lcm // middle
    g_cartier = cartier_product(m)
    clearing = (2 ** (9 * m + 5)) * k_value

    r = fresh_prime(1000 + 100 * m, k_value * g_cartier * q, used)
    used.add(r)

    x_coord = g_cartier
    y_coord = g_cartier * k_value * r
    a_coord = Fraction(x_coord, clearing)
    b_coord = Fraction(y_coord, clearing)
    assert a_coord * clearing == x_coord
    assert b_coord * clearing == y_coord
    assert (2 ** (9 * m + 5)) * b_coord == g_cartier * r
    assert math.gcd(x_coord, y_coord) == g_cartier

    u_coord = x_coord // g_cartier
    v_coord = y_coord // g_cartier
    extra_content = math.gcd(u_coord, v_coord)
    assert (u_coord, v_coord, extra_content) == (1, k_value * r, 1)

    a = 1
    b = k_value * r
    delta = math.gcd(b, q)
    delta0 = math.gcd(k_value, q)
    assert delta == delta0
    b0 = b // delta
    q0 = q // delta
    assert math.gcd(b0, q0) == 1

    p_star = b0 * p - q0
    q_star = delta * b0 * q0
    final_gcd = math.gcd(abs(p_star), q_star)
    assert final_gcd == math.gcd(abs(p_star), delta)
    assert delta % final_gcd == 0
    p_final = p_star // final_gcd
    q_final = q_star // final_gcd
    assert math.gcd(abs(p_final), q_final) == 1
    assert q_final == b * q // (delta * final_gcd)
    assert q_final % r == 0
    assert p_final % r != 0

    # Exact coefficient expansion of W=q*alpha-P before final reduction.
    # E_n=q e-p (n is even), L=1+b*pi.
    constant_w = -b0 * p + q0
    e_coefficient_w = b0 * q
    pi_coefficient_w = q0 * b
    assert e_coefficient_w == q_star == pi_coefficient_w
    assert constant_w == -p_star

    selected = (2, 3, 5, 7, 11, 13)
    lhs_outside = outside_part(p_final, selected) * outside_part(q_final, selected)
    rhs_outside = (
        outside_part(p_star, selected)
        * outside_part(q_star, selected)
        // (outside_part(final_gcd, selected) ** 2)
    )
    assert lhs_outside == rhs_outside

    # Since pi>3, |Lambda| > 3*q*K*r/delta^2.  For eta=1/2,
    # this lower bound times Q_out (at least r) exceeds sqrt(Q).
    lower_numerator = 3 * q * k_value * r * r
    lower_denominator = delta0 * delta0
    assert lower_numerator * lower_numerator > lower_denominator * lower_denominator * q_final

    return {
        "m": m,
        "beta_index": n,
        "beta_p": str(p),
        "beta_q": str(q),
        "K_m": str(k_value),
        "cartier_product": str(g_cartier),
        "fresh_prime": r,
        "matching_delta": str(delta),
        "final_gcd": str(final_gcd),
        "primitive_P": str(p_final),
        "primitive_Q": str(q_final),
        "fresh_prime_divides_Q_not_P": True,
        "outside_identity": True,
        "eta_half_support_failure_certified_by_pi_gt_3": True,
    }


def source_audit() -> dict[str, int | bool]:
    text = SOURCE.read_text(encoding="utf-8")
    open_display = text.count("\\[")
    close_display = text.count("\\]")
    open_inline = text.count("\\(")
    close_inline = text.count("\\)")
    tags = []
    for part in text.split("\\tag{")[1:]:
        tags.append(part.split("}", 1)[0])
    assert open_display == close_display
    assert open_inline == close_inline
    assert len(tags) == len(set(tags))
    assert "No conclusion about the arithmetic nature" in text
    assert "countermodels are not the actual" in text
    return {
        "display_open": open_display,
        "display_close": close_display,
        "inline_open": open_inline,
        "inline_close": close_inline,
        "numbered_tags": len(tags),
        "unique_numbered_tags": len(set(tags)),
        "scope_caveats_present": True,
    }


def main() -> None:
    dependency_report = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependency_report[relative] = actual

    used: set[int] = set()
    cases = [replay_case(m, used) for m in range(1, 13)]
    assert len(used) == len(cases)

    payload = {
        "claim_scope": (
            "Exact primitive matching/outside-product theorem and an arithmetic "
            "countermodel showing that the item-133 clearing, dyadic coordinate, "
            "and certified Cartier content alone imply neither fixed nor moving "
            "prime support. This does not model the actual saddle-size forms and "
            "does not classify e+pi."
        ),
        "dependencies": dependency_report,
        "source_audit": source_audit(),
        "number_of_exact_cases": len(cases),
        "fresh_primes_pairwise_distinct": len(used) == len(cases),
        "all_cases_pass": True,
        "cases": cases,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
