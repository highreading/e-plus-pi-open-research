#!/usr/bin/env python3
"""Factor the four coefficient-section polynomials for a fixed m.

This is an exact symbolic aid for the proposed uniform proof.  It verifies
the forced consecutive-root factor in every section and writes the two
Cartier obstruction forms after the common-index shift.
"""

from __future__ import annotations

import argparse

import sympy as sp


k = sp.symbols("k")


def section_polynomial(m: int, a: int) -> sp.Expr:
    order = 4 * m + 2
    degree = (10 * m + 3 - a) // 4
    answer = 0
    for ell in range(degree + 1):
        coefficient = (-1) ** a * sp.binomial(10 * m + 3, a + 4 * ell)
        answer += coefficient * sp.prod(
            k - ell + order - index for index in range(order)
        ) / sp.factorial(order)
    return sp.factor(answer)


def forced_factor(m: int, a: int) -> sp.Expr:
    numerator_degree = (10 * m + 3 - a) // 4
    length = 4 * m + 2 - numerator_degree
    return sp.prod(k + index for index in range(1, length + 1))


def window_value(
    sections: list[sp.Expr], residue: int, r: int, base_k: sp.Rational
) -> sp.Expr:
    section = (residue - r) % 4
    offset = (residue - r - section) // 4
    return sp.factor(sections[section].subs(k, base_k + offset))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int)
    parser.add_argument("--show-residuals", action="store_true")
    arguments = parser.parse_args()
    m = arguments.m

    sections = [section_polynomial(m, a) for a in range(4)]
    print(f"m={m}")
    for a, section in enumerate(sections):
        factor = forced_factor(m, a)
        quotient, remainder = sp.div(sp.Poly(section, k), sp.Poly(factor, k))
        print(
            f"a={a}: degree={sp.degree(section, k)}, "
            f"forced_degree={sp.degree(factor, k)}, remainder={remainder.as_expr()}"
        )
        if arguments.show_residuals:
            print(f"  forced={sp.factor(factor)}")
            print(f"  residual={sp.factor(quotient.as_expr())}")

    for epsilon in (1, 3):
        delta = (epsilon - 2 * m) % 4
        q_base_k = sp.Rational(-6 * m - delta, 4)
        p_base_k = sp.Rational(-epsilon, 4)
        a = {
            r: window_value(sections, delta, r, q_base_k)
            for r in range(1, 9)
        }
        b = {
            r: window_value(sections, epsilon, r, p_base_k)
            for r in range(1, 9)
        }
        left_value = sp.factor(a[1] - b[8])
        right_value = sp.factor(
            a[2] + a[3] + a[4] - b[5] - b[6] - b[7]
        )
        common = sp.gcd(
            abs(sp.numer(left_value)), abs(sp.numer(right_value))
        )
        print(
            f"epsilon={epsilon}, delta=q mod 4={delta}: "
            f"k_q={q_base_k}, k_p={p_base_k}; "
            f"gcd(num L1,num L2)={common}; "
            f"divides (6m)!={sp.factorial(6*m) % common == 0}"
        )


if __name__ == "__main__":
    main()
