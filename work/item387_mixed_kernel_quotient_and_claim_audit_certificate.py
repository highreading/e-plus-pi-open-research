#!/usr/bin/env python3
"""Exact controls for Item 387.

The mathematical proof is symbolic.  These deterministic integer-ring
checks exercise the automorphism, endpoint quotient, kernel decomposition,
and a rational-interval counterexample to the claimed inequality.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(out)


def sub(a: list[int], b: list[int]) -> list[int]:
    return add(a, [-x for x in b])


def deriv(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return [0]
    return trim([i * a[i] for i in range(1, len(a))])


def scale(a: list[int], c: int) -> list[int]:
    return trim([c * x for x in a])


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def eval_at(a: list[int], x: int) -> int:
    v = 0
    for c in reversed(a):
        v = v * x + c
    return v


def U(p: list[int]) -> list[int]:
    out = [0]
    q = p[:]
    sign = 1
    while q != [0]:
        out = add(out, scale(q, sign))
        q = deriv(q)
        sign = -sign
    return trim(out)


def U_inverse(s: list[int]) -> list[int]:
    return add(s, deriv(s))


def controls() -> dict:
    cases = []
    total = 0
    for degree in range(9):
        for seed in range(1, 8):
            p = [((seed + 2 * i) * (i + 1)) % 17 - 8 for i in range(degree + 1)]
            if p[-1] == 0:
                p[-1] = seed
            p = trim(p)
            s = U(p)
            assert U_inverse(s) == p
            A, C = eval_at(s, 1), eval_at(s, 0)
            p0 = [A, A - C]
            remainder = sub(s, [C, A - C])
            # Exact division by x(x-1)=x^2-x.  Since the constant and value
            # at one vanish, synthetic division is integral and exact.
            assert eval_at(remainder, 0) == 0
            assert eval_at(remainder, 1) == 0
            q1 = remainder[1:] if len(remainder) > 1 else [0]  # divide by x
            # Divide q1 by x-1 using descending synthetic division.
            if len(q1) <= 1:
                R = [0]
                rem = q1[0]
            else:
                desc = list(reversed(q1))
                syn = [desc[0]]
                for c in desc[1:]:
                    syn.append(c + syn[-1])
                rem = syn[-1]
                R = trim(list(reversed(syn[:-1]))) if len(syn) > 1 else [0]
            assert rem == 0
            reconstructed_s = add([C, A - C], mul([0, -1, 1], R))
            assert reconstructed_s == s
            reconstructed_p = add(p0, U_inverse(mul([0, -1, 1], R)))
            assert reconstructed_p == p
            total += 1
            if seed == 1:
                cases.append({"degree": degree, "A": A, "C": C, "P": p, "R": R})

    # Rational enclosures: 2718/1000 < e < 2719/1000 and
    # 3141/1000 < pi < 3142/1000.  For x=e,m=1,a=3*pi/2,
    # the first absolute value is <1 and the alleged lower comparator >2.9.
    e_lo, e_hi = Fraction(2718, 1000), Fraction(2719, 1000)
    pi_lo, pi_hi = Fraction(3141, 1000), Fraction(3142, 1000)
    lhs_upper = Fraction(3, 2) * pi_hi - (e_lo + 1)
    rhs_lower = Fraction(3, 2) * pi_lo - (e_hi - 1)
    assert 0 < lhs_upper < 1
    assert rhs_lower > Fraction(29, 10)

    return {
        "schema": "item387-mixed-kernel-quotient-and-claim-audit-certificate-v1",
        "classification": "EXACT_INTEGER_RING_CONTROLS_FOR_SYMBOLIC_ALL_DEGREE_THEOREM",
        "automorphism_cases": total,
        "representative_cases": cases,
        "identities_checked": [
            "U_inverse(U(P))=P",
            "E(P)=(S_P(1),S_P(0))",
            "P=P_(A,C)+(1+D)(x(x-1)R)",
            "degree-one section P_(A,C)=A+(A-C)x",
        ],
        "inequality_counterexample": {
            "parameters": {"k": 1, "m": 1, "r": 1, "a": "3*pi/2"},
            "bounds": {"e": ["2718/1000", "2719/1000"], "pi": ["3141/1000", "3142/1000"]},
            "lhs_upper": str(lhs_upper),
            "rhs_lower": str(rhs_lower),
            "conclusion": "|e+1-3*pi/2|<1<2.9<||e-1|-3*pi/2|",
        },
        "asymptotic_inference_from_controls": False,
        "proof_scope": "The report supplies the symbolic all-degree proof; these are deterministic controls only.",
    }


def main() -> None:
    payload = controls()
    encoded = (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_bytes(encoded)
    else:
        sys.stdout.buffer.write(encoded)


if __name__ == "__main__":
    main()
