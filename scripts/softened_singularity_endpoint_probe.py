#!/usr/bin/env python3
"""Exact probe for the D(z)^n softened-singularity endpoint family.

The integer coordinates are computed only with Python integers.  Comparisons
of |u(e+pi)-v| use directed fixed-point rational enclosures obtained from the
positive series for e and the alternating Machin formula

    pi = 16 atan(1/5) - 4 atan(1/239).

Thus the reported finite minimizers are certificates, not floating-point
guesses.  Decimal logarithms are included only as diagnostics.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from math import ceil, comb, gcd
from pathlib import Path


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def e_fixed_interval(scale: int) -> tuple[int, int, int]:
    """Return lo, hi with lo/scale <= e <= hi/scale."""
    # Stop once the rigorous geometric tail is below one scale unit.
    fact = 1
    m = 0
    while True:
        if m >= 1:
            tail_num = scale * (m + 2)
            tail_den = fact * (m + 1) * (m + 1)
            # Here fact=m!, and this is a deliberately slightly enlarged
            # version of (m+2)/((m+1)!(m+1)).
            if tail_num < tail_den:
                break
        m += 1
        fact *= m

    lo = 0
    hi = 0
    fact = 1
    for k in range(m + 1):
        if k:
            fact *= k
        lo += scale // fact
        hi += ceil_div(scale, fact)

    # sum_{j>m}1/j! <= (m+2)/((m+1)!(m+1)).
    tail_den = fact * (m + 1) * (m + 1)
    hi += ceil_div(scale * (m + 2), tail_den)
    return lo, hi, m


def atan_recip_fixed_interval(q: int, scale: int) -> tuple[int, int, int]:
    """Directed interval for atan(1/q), using its alternating series."""
    lo = 0
    hi = 0
    k = 0
    while True:
        den = (2 * k + 1) * pow(q, 2 * k + 1)
        floor_term = scale // den
        ceil_term = ceil_div(scale, den)
        if k % 2 == 0:
            lo += floor_term
            hi += ceil_term
        else:
            lo -= ceil_term
            hi -= floor_term

        next_k = k + 1
        next_den = (2 * next_k + 1) * pow(q, 2 * next_k + 1)
        if scale < next_den:
            # The true alternating remainder lies between zero and the next
            # term, with its sign.
            if next_k % 2 == 0:
                hi += 1
            else:
                lo -= 1
            return lo, hi, k
        k = next_k


def e_plus_pi_fixed_interval(digits: int) -> tuple[int, int, dict[str, int]]:
    scale = 10**digits
    e_lo, e_hi, e_terms = e_fixed_interval(scale)
    a5_lo, a5_hi, a5_terms = atan_recip_fixed_interval(5, scale)
    a239_lo, a239_hi, a239_terms = atan_recip_fixed_interval(239, scale)
    pi_lo = 16 * a5_lo - 4 * a239_hi
    pi_hi = 16 * a5_hi - 4 * a239_lo
    return (
        e_lo + pi_lo,
        e_hi + pi_hi,
        {
            "digits": digits,
            "e_last_index": e_terms,
            "atan_1_5_last_index": a5_terms,
            "atan_1_239_last_index": a239_terms,
        },
    )


def eta_zero(max_k: int) -> list[int]:
    """eta_{0,k} from the integer differential recurrence."""
    eta = [0] * (max_k + 1)
    eta[0] = 0
    for k in range(max_k):
        em1 = eta[k - 1] if k >= 1 else 0
        em2 = eta[k - 2] if k >= 2 else 0
        numerator = (
            4 * ((-1) ** k)
            - 2 * eta[k]
            + 2 * k * (eta[k] + em1)
            - k * (k - 1) * (em1 + em2)
        )
        assert numerator % 2 == 0
        eta[k + 1] = numerator // 2
    return eta


def multiply_by_D(eta: list[int]) -> list[int]:
    out = [0] * len(eta)
    for k in range(len(eta)):
        out[k] = 2 * eta[k]
        if k >= 1:
            out[k] -= 2 * k * eta[k - 1]
        if k >= 2:
            out[k] += k * (k - 1) * eta[k - 2]
    return out


def derangements(max_b: int) -> list[int]:
    out = [0] * (max_b + 1)
    out[0] = 1
    for b in range(1, max_b + 1):
        out[b] = b * out[b - 1] + (-1) ** b
    return out


def v_coordinates(eta: list[int], max_b: int) -> list[int]:
    out = [0] * (max_b + 1)
    out[0] = 1
    for b in range(1, max_b + 1):
        out[b] = b * out[b - 1] + eta[b]
    return out


def abs_interval(
    u: int, v: int, s_lo: int, s_hi: int, scale: int
) -> tuple[int, int]:
    """Bounds scaled by `scale` for |u(e+pi)-v|, for u>=0."""
    lo = u * s_lo - v * scale
    hi = u * s_hi - v * scale
    assert lo <= hi
    if lo > 0:
        return lo, hi
    if hi < 0:
        return -hi, -lo
    return 0, max(-lo, hi)


def log10_mid(lo: int, hi: int, scale: int) -> str:
    mid_num = lo + hi
    if mid_num <= 0:
        return "-Infinity"
    with localcontext() as ctx:
        ctx.prec = 30
        value = Decimal(mid_num) / (Decimal(2) * Decimal(scale))
        return format(value.log10(), ".18f")


def c_add(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]):
    return x[0] + y[0], x[1] + y[1]


def c_mul(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def c_scale(x: tuple[Fraction, Fraction], q: Fraction):
    return x[0] * q, x[1] * q


def c_pow(x: tuple[Fraction, Fraction], n: int):
    out = (Fraction(1), Fraction(0))
    base = x
    while n:
        if n & 1:
            out = c_mul(out, base)
        base = c_mul(base, base)
        n //= 2
    return out


def f_ordinary_coefficient(k: int) -> Fraction:
    """[z^k]F(z), from the logarithmic representation."""
    if k <= 0:
        return Fraction(0)
    alpha = (Fraction(1, 2), Fraction(1, 2))
    alpha_bar = (Fraction(1, 2), Fraction(-1, 2))
    # log(1-a z) contributes -a^k/k.
    lb = c_scale(c_pow(alpha_bar, k), Fraction(-1, k))
    la = c_scale(c_pow(alpha, k), Fraction(-1, k))
    diff = (lb[0] - la[0], lb[1] - la[1])
    # Multiply by -2i; the result is real.
    result = (2 * diff[1], -2 * diff[0])
    assert result[1] == 0
    return result[0]


def D_power_coefficients(n: int) -> list[int]:
    out = [1]
    for _ in range(n):
        nxt = [0] * (len(out) + 2)
        for j, value in enumerate(out):
            nxt[j] += 2 * value
            nxt[j + 1] -= 2 * value
            nxt[j + 2] += value
        out = nxt
    return out


def branch_formula_rhs(n: int, k: int) -> Fraction:
    """Right side of equation (39) in the companion note, exactly."""
    assert k > 2 * n
    integral = (Fraction(0), Fraction(0))
    iunit = (Fraction(0), Fraction(1))
    # (1-t)^n (t+i)^n.
    for a in range(n + 1):
        ca = Fraction(((-1) ** a) * comb(n, a))
        for c in range(n + 1):
            cc = Fraction(comb(n, c))
            ipow = c_pow(iunit, n - c)
            den = k - 2 * n + a + c
            term = c_scale(ipow, ca * cc / den)
            integral = c_add(integral, term)
    alpha = (Fraction(1, 2), Fraction(1, 2))
    product = c_mul(c_pow(alpha, k), integral)
    return Fraction(((-1) ** n) * (2 ** (n + 2))) * product[1]


def verify_branch_formula() -> dict[str, int | bool]:
    checks = 0
    for n in range(5):
        dcoeff = D_power_coefficients(n)
        for k in range(2 * n + 1, 2 * n + 7):
            lhs = sum(
                Fraction(dcoeff[j]) * f_ordinary_coefficient(k - j)
                for j in range(min(2 * n, k) + 1)
            )
            rhs = branch_formula_rhs(n, k)
            assert lhs == rhs, (n, k, lhs, rhs)
            checks += 1
    return {"passed": True, "exact_cases": checks}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=60)
    parser.add_argument("--b-multiple", type=int, default=4)
    parser.add_argument("--digits", type=int, default=700)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    max_b = args.b_multiple * args.n_max
    scale = 10**args.digits
    s_lo, s_hi, interval_meta = e_plus_pi_fixed_interval(args.digits)
    assert s_lo < s_hi

    eta = eta_zero(max_b)
    U = derangements(max_b)
    records = []
    representative_ns = {1, 2, 5, 10, 20, 40, args.n_max}

    for n in range(1, args.n_max + 1):
        eta = multiply_by_D(eta)
        V = v_coordinates(eta, args.b_multiple * n)
        entries = []
        for b in range(2, args.b_multiple * n + 1):
            g = gcd(abs(U[b]), abs(V[b]))
            up = U[b] // g
            vp = V[b] // g
            alo, ahi = abs_interval(up, vp, s_lo, s_hi, scale)
            entries.append(
                {
                    "b": b,
                    "gcd": g,
                    "u_primitive": up,
                    "v_primitive": vp,
                    "abs_lo_scaled": alo,
                    "abs_hi_scaled": ahi,
                }
            )

        # The candidate selected by exact interval midpoints is certified if
        # its upper endpoint is below every competing lower endpoint.
        candidate = min(entries, key=lambda x: x["abs_lo_scaled"] + x["abs_hi_scaled"])
        certified = all(
            candidate["abs_hi_scaled"] < item["abs_lo_scaled"]
            for item in entries
            if item is not candidate
        )

        lower_b = max(2, ceil(n / 2))
        restricted = [item for item in entries if item["b"] >= lower_b]
        rcandidate = min(
            restricted, key=lambda x: x["abs_lo_scaled"] + x["abs_hi_scaled"]
        )
        rcertified = all(
            rcandidate["abs_hi_scaled"] < item["abs_lo_scaled"]
            for item in restricted
            if item is not rcandidate
        )

        # Verify the closed b=2 formula exactly.
        assert U[2] == 1
        assert V[2] == 2 + (2 ** (n + 1)) * (1 - 2 * n)

        record = {
            "n": n,
            "global_min_b": candidate["b"],
            "global_min_certified": certified,
            "global_min_log10_mid": log10_mid(
                candidate["abs_lo_scaled"], candidate["abs_hi_scaled"], scale
            ),
            "global_min_gcd": candidate["gcd"],
            "restricted_b_minimum": lower_b,
            "restricted_min_b": rcandidate["b"],
            "restricted_min_certified": rcertified,
            "restricted_min_log10_mid": log10_mid(
                rcandidate["abs_lo_scaled"], rcandidate["abs_hi_scaled"], scale
            ),
            "restricted_min_gcd": rcandidate["gcd"],
        }
        if n in representative_ns:
            b2 = entries[0]
            record["b2"] = {
                "u_primitive": b2["u_primitive"],
                "v_primitive": b2["v_primitive"],
                "gcd": b2["gcd"],
                "log10_mid": log10_mid(
                    b2["abs_lo_scaled"], b2["abs_hi_scaled"], scale
                ),
            }
        records.append(record)

    branch_check = verify_branch_formula()
    finite_claim = all(
        rec["global_min_certified"] and rec["global_min_b"] == 2
        for rec in records
        if rec["n"] >= 2
    )
    payload = {
        "description": "Exact softened-singularity endpoint-family scan",
        "parameters": {
            "n_min": 1,
            "n_max": args.n_max,
            "b_min": 2,
            "b_max_for_n": f"{args.b_multiple}*n",
        },
        "s_interval": {
            **interval_meta,
            "scaled_width": s_hi - s_lo,
            "scale": f"10^{args.digits}",
            "construction": "positive e series and alternating Machin pi series, directed integer rounding",
        },
        "branch_formula_exact_check": branch_check,
        "certified_statement": {
            "for_every_n_2_through_nmax_global_min_is_b2": finite_claim,
            "scope_warning": "finite certificate only; not an all-n optimality theorem",
        },
        "records": records,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["certified_statement"], indent=2))
    print(json.dumps(payload["branch_formula_exact_check"], indent=2))


if __name__ == "__main__":
    main()
