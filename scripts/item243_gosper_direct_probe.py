#!/usr/bin/env python3
"""Exact direct rational-difference certificates for Item 243 recurrences.

This is an exploratory prover.  It avoids expression-level simplification by
working in QQ(n,j) and solves

    b(j) H(j+1) - H(j) = T(j)

directly over QQ(n), where b is the base summand ratio and T is the proposed
recurrence multiplier.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sympy.polys.domains import QQ
from sympy.polys.fields import field
from sympy.polys.rings import ring


HERE = Path(__file__).resolve().parent
F, n, j = field("n,j", QQ)
Fn, nn = field("n", QQ)
Rj, jj = ring("j", Fn)
Frj = Rj.to_field()


SPECS = {
    # order, coefficient degree, (extra, parity), alpha, beta as functions of h
    "x": (4, 15, 1, 1, lambda h: (-4 * h + 3) / 6, lambda h: (-4 * h + 1) / 2),
    "y": (3, 14, 1, 1, lambda h: h + 1, lambda h: 1 - h / 3),
    "u": (5, 15, 4, 0, lambda h: -(4 * h + 3) / 6, lambda h: -(4 * h + 3) / 2),
    "v": (3, 16, 4, 1, lambda h: h + 1, lambda h: -h / 3),
}


def q(num, den=1):
    return QQ(num, den)


def prod(values):
    answer = F.one
    for value in values:
        answer *= value
    return answer


def kernel_ratio(extra, h, degree):
    answer = F.zero
    falling = F.one
    rising = F.one
    binomial = 1
    for shift in range(extra + 1):
        if shift:
            falling *= degree - (shift - 1)
            rising *= 2 * h - degree + shift
            binomial = binomial * (extra - shift + 1) // shift
        answer += (-1 if shift & 1 else 1) * binomial * falling / rising
    return answer


def rising_shift_ratio(alpha, length, shift):
    if shift >= 0:
        return prod(
            (alpha + length + offset) / (alpha + offset)
            for offset in range(shift)
        )
    return prod(
        (alpha + offset) / (alpha + length + offset)
        for offset in range(shift, 0)
    )


def term_h_shift(extra, parity, alpha_fn, beta_fn, h, index, shift):
    degree = 2 * index + parity
    alpha = alpha_fn(h)
    beta = beta_fn(h)
    alpha_shift = alpha_fn(h + 3 * shift) - alpha
    beta_shift = beta_fn(h + 3 * shift) - beta
    if alpha_shift.denom != alpha_shift.denom.ring.one or beta_shift.denom != beta_shift.denom.ring.one:
        raise ArithmeticError("nonintegral parameter shift")
    alpha_shift_int = int(alpha_shift.numer.LC)
    beta_shift_int = int(beta_shift.numer.LC)
    binomial_ratio = prod(
        (2 * h + offset) / (2 * h - degree + offset)
        for offset in range(1, 6 * shift + 1)
    )
    return (
        rising_shift_ratio(alpha, index, alpha_shift_int)
        / rising_shift_ratio(beta, index, beta_shift_int)
        * binomial_ratio
        * kernel_ratio(extra, h + 3 * shift, degree)
        / kernel_ratio(extra, h, degree)
    )


def base_index_ratio(extra, parity, alpha_fn, beta_fn, h):
    degree = 2 * j + parity
    alpha = alpha_fn(h)
    beta = beta_fn(h)
    return (
        -(alpha + j)
        / (beta + j)
        * (2 * h - degree)
        * (2 * h - degree - 1)
        / ((degree + 1) * (degree + 2))
        * kernel_ratio(extra, h, degree + 2)
        / kernel_ratio(extra, h, degree)
    )


def convert_poly(poly):
    """View a QQ[n,j] polynomial as an element of QQ(n)[j]."""
    answer = Rj.zero
    for (n_degree, j_degree), coefficient in poly.terms():
        answer += coefficient * nn**n_degree * jj**j_degree
    return answer


def shift(poly):
    return poly.compose(jj, jj + 1)


def shift_by(poly, amount):
    return poly.compose(jj, jj + amount)


def shift_fraction(value, amount=1):
    return Frj.new(shift_by(value.numer, amount), shift_by(value.denom, amount))


def coefficient(poly, degree):
    return poly.get((degree,), Fn.zero)


def solve_dense(columns, right):
    """Solve columns*y=right over QQ(n), setting free variables to zero."""
    row_count = max([right.degree()] + [value.degree() for value in columns]) + 1
    column_count = len(columns)
    rows = [
        [coefficient(value, degree) for value in columns]
        + [coefficient(right, degree)]
        for degree in range(row_count)
    ]
    pivot_rows = []
    pivot_row = 0
    for column in range(column_count):
        source = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if source is None:
            continue
        rows[pivot_row], rows[source] = rows[source], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [value / pivot for value in rows[pivot_row]]
        for row in range(pivot_row + 1, row_count):
            if not rows[row][column]:
                continue
            multiplier = rows[row][column]
            rows[row] = [
                rows[row][entry] - multiplier * rows[pivot_row][entry]
                for entry in range(column_count + 1)
            ]
        pivot_rows.append((pivot_row, column))
        pivot_row += 1
        print(json.dumps({"pivot": pivot_row, "columns": column_count}), flush=True)
        if pivot_row == row_count:
            break
    for row in range(row_count):
        if not any(rows[row][:-1]) and rows[row][-1]:
            return None
    answer = [Fn.zero] * column_count
    for row, column in reversed(pivot_rows):
        answer[column] = rows[row][-1] - sum(
            (rows[row][later] * answer[later] for later in range(column + 1, column_count)),
            Fn.zero,
        )
    return answer


def build_target(residue, name):
    recurrences = json.loads(
        (HERE / "item243_univariate_recurrence_probe.json").read_text()
    )["recurrences"]
    order, coefficient_degree, extra, parity, alpha_fn, beta_fn = SPECS[name]
    exact = recurrences[f"r{residue}_{name}"]
    h = 3 * n + residue
    target = F.zero
    for step in range(order + 1):
        polynomial = F.zero
        for degree in range(coefficient_degree + 1):
            numerator, denominator = exact[step * (coefficient_degree + 1) + degree]
            polynomial += q(numerator, denominator) * n**degree
        target += polynomial * term_h_shift(
            extra, parity, alpha_fn, beta_fn, h, j, step
        )
        print(json.dumps({"built_shift": step}), flush=True)
    return target, base_index_ratio(extra, parity, alpha_fn, beta_fn, h)


def find_certificate(residue, name, maximum_degree):
    target, base_ratio = build_target(residue, name)
    numerator = convert_poly(target.numer)
    denominator = convert_poly(target.denom)
    base_numerator = convert_poly(base_ratio.numer)
    base_denominator = convert_poly(base_ratio.denom)
    denominator_shift = shift(denominator)
    right = base_denominator * numerator * denominator_shift
    print(
        json.dumps(
            {
                "target_degrees": [numerator.degree(), denominator.degree()],
                "base_degrees": [base_numerator.degree(), base_denominator.degree()],
                "right_degree": right.degree(),
            }
        ),
        flush=True,
    )
    columns = [
            base_numerator * (jj + 1) ** degree * denominator
            - base_denominator * jj**degree * denominator_shift
            for degree in range(maximum_degree + 1)
    ]
    solution = solve_dense(columns, right)
    print(json.dumps({"tried_degree": maximum_degree, "found": solution is not None}), flush=True)
    if solution is None:
        return None
    y_poly = sum((value * jj**power for power, value in enumerate(solution)), Rj.zero)
    check = base_numerator * shift(y_poly) * denominator - base_denominator * y_poly * denominator_shift - right
    if check:
        raise AssertionError("linear solve did not verify")
    return target, base_ratio, y_poly, denominator


def gosper_normal_by_dispersion(
    numerator, denominator, maximum_shift=40, preferred_c=None
):
    """Gosper normal form over QQ(n)[j], using an exact shift scan."""
    # ``summand_ratio`` is a FracElement, hence these are already coprime.
    if preferred_c is not None:
        preferred_c = preferred_c.monic()
        try:
            a_direct = numerator.exquo(shift(preferred_c))
            b_direct = denominator.exquo(preferred_c)
        except Exception:
            pass
        else:
            return a_direct, b_direct, preferred_c, [[1, preferred_c.degree()]]
    initial_a_factors = [
        factor.monic()
        for factor, multiplicity in numerator.factor_list()[1]
        for _ in range(multiplicity)
    ]
    initial_b_factors = [
        factor.monic()
        for factor, multiplicity in denominator.factor_list()[1]
        for _ in range(multiplicity)
    ]
    scale = numerator.LC / denominator.LC
    a_poly = numerator.monic()
    b_poly = denominator.monic()
    c_poly = Rj.one
    hits = []
    # The input fraction was reduced above, so the amount-zero gcd is one.
    for amount in range(1, maximum_shift + 1):
        a_factors = initial_a_factors if amount == 1 else [
            factor.monic() for factor, multiplicity in a_poly.factor_list()[1]
            for _ in range(multiplicity)
        ]
        b_factors = initial_b_factors if amount == 1 else [
            factor.monic() for factor, multiplicity in b_poly.factor_list()[1]
            for _ in range(multiplicity)
        ]
        used_b = set()
        divisor = Rj.one
        for a_factor in a_factors:
            for index, b_factor in enumerate(b_factors):
                if index in used_b:
                    continue
                if a_factor == shift_by(b_factor, amount).monic():
                    divisor *= a_factor
                    used_b.add(index)
                    break
        if divisor.degree() <= 0:
            continue
        hits.append([amount, divisor.degree()])
        a_poly = a_poly.exquo(divisor)
        b_poly = b_poly.exquo(shift_by(divisor, -amount))
        for offset in range(1, amount + 1):
            c_poly *= shift_by(divisor, -offset)
    return a_poly * scale, b_poly, c_poly, hits


def find_gosper_certificate(residue, name, maximum_shift=1):
    target, base_ratio = build_target(residue, name)
    field_j = F.ring.gens[1]
    target_shift = F.new(
        target.numer.compose(field_j, field_j + 1),
        target.denom.compose(field_j, field_j + 1),
    )
    summand_ratio = base_ratio * target_shift / target
    ratio_numerator = convert_poly(summand_ratio.numer)
    ratio_denominator = convert_poly(summand_ratio.denom)
    print(
        json.dumps(
            {
                "summand_ratio_degrees": [ratio_numerator.degree(), ratio_denominator.degree()],
                "summand_ratio_terms": [len(ratio_numerator.terms()), len(ratio_denominator.terms())],
            }
        ),
        flush=True,
    )
    a_poly, b_poly, c_poly, hits = gosper_normal_by_dispersion(
        ratio_numerator,
        ratio_denominator,
        maximum_shift,
        convert_poly(target.numer),
    )
    if (
        ratio_numerator * b_poly * c_poly
        - ratio_denominator * a_poly * shift(c_poly)
    ):
        raise AssertionError("Gosper normal form did not verify")
    b_shift = shift_by(b_poly, -1)
    a_degree = a_poly.degree()
    b_degree = b_shift.degree()
    c_degree = c_poly.degree()
    if a_degree != b_degree or a_poly.LC != b_shift.LC:
        candidates = {c_degree - max(a_degree, b_degree)}
    elif not a_degree:
        candidates = {c_degree - a_degree + 1, 0}
    else:
        candidates = {
            c_degree - a_degree + 1,
            (coefficient(b_shift, a_degree - 1) - coefficient(a_poly, a_degree - 1)) / a_poly.LC,
        }
    candidates = sorted(
        {
            int(value.numer.LC)
            for value in candidates
            if getattr(value, "denom", None) is not None
            and value.denom == value.denom.ring.one
            and value.numer.degree() == 0
            and int(value.numer.LC) >= 0
        }
        | {value for value in candidates if isinstance(value, int) and value >= 0},
        reverse=True,
    )
    print(
        json.dumps(
            {
                "dispersion_hits": hits,
                "normal_degrees": [a_degree, b_degree, c_degree],
                "candidate_degrees": candidates,
            }
        ),
        flush=True,
    )
    for degree in candidates:
        columns = [
            a_poly * (jj + 1) ** power - b_shift * jj**power
            for power in range(degree + 1)
        ]
        solution = solve_dense(columns, c_poly)
        if solution is None:
            continue
        x_poly = sum(
            (value * jj**power for power, value in enumerate(solution)), Rj.zero
        )
        if a_poly * shift(x_poly) - b_shift * x_poly - c_poly:
            raise AssertionError("Gosper polynomial did not verify")
        target_numerator = convert_poly(target.numer)
        target_denominator = convert_poly(target.denom)
        telescoper_numerator = target_numerator.LC * b_shift * x_poly
        return {
            "target": target,
            "base_ratio": base_ratio,
            "normal_a": a_poly,
            "normal_b": b_poly,
            "normal_b_shift": b_shift,
            "normal_c": c_poly,
            "gosper_polynomial": x_poly,
            "certificate_numerator": b_shift * x_poly,
            "certificate_denominator": c_poly,
            "telescoper_numerator": telescoper_numerator,
            "telescoper_denominator": target_denominator,
            "dispersion_hits": hits,
        }
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("residue", type=int, choices=(1, 2))
    parser.add_argument("period", choices=tuple(SPECS))
    parser.add_argument("--maximum-degree", type=int, default=35)
    parser.add_argument("--maximum-shift", type=int, default=1)
    parser.add_argument("--direct", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = (
        find_certificate(args.residue, args.period, args.maximum_degree)
        if args.direct
        else find_gosper_certificate(args.residue, args.period, args.maximum_shift)
    )
    if result is None:
        raise ArithmeticError("no certificate with denominator target_denominator")
    if args.direct:
        target, base_ratio, y_poly, denominator = result
        payload = {
            "residue": args.residue,
            "period": args.period,
            "method": "direct_target_denominator",
            "target": str(target),
            "base_ratio": str(base_ratio),
            "certificate_numerator": str(y_poly),
            "certificate_denominator": str(denominator),
            "verified_zero": True,
        }
        certificate_degree = y_poly.degree()
    else:
        payload = {
            "residue": args.residue,
            "period": args.period,
            "method": "gosper_normal_dispersion",
            "target": str(result["target"]),
            "base_ratio": str(result["base_ratio"]),
            "normal_a": str(result["normal_a"]),
            "normal_b": str(result["normal_b"]),
            "normal_b_shift": str(result["normal_b_shift"]),
            "normal_c": str(result["normal_c"]),
            "gosper_polynomial": str(result["gosper_polynomial"]),
            "certificate_numerator": str(result["certificate_numerator"]),
            "certificate_denominator": str(result["certificate_denominator"]),
            "telescoper_numerator": str(result["telescoper_numerator"]),
            "telescoper_denominator": str(result["telescoper_denominator"]),
            "dispersion_hits": result["dispersion_hits"],
            "verified_zero": True,
        }
        certificate_degree = result["certificate_numerator"].degree()
    output = args.output or HERE / f"item243_direct_r{args.residue}_{args.period}.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(output), "numerator_degree": certificate_degree}))


if __name__ == "__main__":
    main()
