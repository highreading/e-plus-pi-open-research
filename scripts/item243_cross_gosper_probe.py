#!/usr/bin/env python3
"""Exact one-variable Gosper certificates for Item 243 cross relations."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


g = load("item243_cross_gosper_core", "item243_gosper_direct_probe.py")
F, n, j = g.F, g.n, g.j


RELATIONS = {
    "xu": ("x", "u", 1, 1, 7),
    "yv": ("y", "v", 0, 2, 12),
}


def integer_ground(value):
    if not value:
        return 0
    if value.denom != value.denom.ring.one or value.numer.degree() != 0:
        raise ArithmeticError(value)
    return int(value.numer.LC)


def factorial_ratio(base_degree, delta):
    if delta >= 0:
        return F.one / g.prod(base_degree + offset for offset in range(1, delta + 1))
    return g.prod(base_degree - offset for offset in range(-delta))


def tail_factorial_ratio(base_tail, delta):
    if delta >= 0:
        return F.one / g.prod(base_tail + offset for offset in range(1, delta + 1))
    return g.prod(base_tail - offset for offset in range(-delta))


def term_ratio(base_name, target_name, h, index, shift):
    _, _, base_extra, base_parity, base_alpha_fn, base_beta_fn = g.SPECS[base_name]
    _, _, extra, parity, alpha_fn, beta_fn = g.SPECS[target_name]
    target_h = h + 3 * shift
    base_degree = 2 * index + base_parity
    target_degree = 2 * index + parity
    degree_delta = parity - base_parity
    alpha = base_alpha_fn(h)
    beta = base_beta_fn(h)
    alpha_delta = integer_ground(alpha_fn(target_h) - alpha)
    beta_delta = integer_ground(beta_fn(target_h) - beta)
    binomial_ratio = (
        g.prod(2 * h + offset for offset in range(1, 6 * shift + 1))
        * factorial_ratio(base_degree, degree_delta)
        * tail_factorial_ratio(2 * h - base_degree, 6 * shift - degree_delta)
    )
    return (
        (-1 if degree_delta & 1 else 1)
        * g.rising_shift_ratio(alpha, index, alpha_delta)
        / g.rising_shift_ratio(beta, index, beta_delta)
        * binomial_ratio
        * g.kernel_ratio(extra, target_h, target_degree)
        / g.kernel_ratio(base_extra, h, base_degree)
    )


def relation_blocks(residue, key):
    data = json.loads((HERE / "item243_cross_reconstruct.json").read_text())["relations"]
    left, right, left_order, right_order, degree = RELATIONS[key]
    flat = data[f"r{residue}_{key}"]
    cursor = 0
    answer = []
    for name, order in ((left, left_order), (right, right_order)):
        current = []
        for _ in range(order + 1):
            current.append(flat[cursor : cursor + degree + 1])
            cursor += degree + 1
        answer.append((name, current))
    return answer, degree


def build(residue, key):
    (groups, degree) = relation_blocks(residue, key)
    base_name = groups[0][0]
    h = 3 * n + residue
    target = F.zero
    for name, blocks in groups:
        for shift, coefficients in enumerate(blocks):
            polynomial = F.zero
            for power, (numerator, denominator) in enumerate(coefficients):
                polynomial += g.q(numerator, denominator) * n**power
            target += polynomial * term_ratio(base_name, name, h, j, shift)
            print(json.dumps({"name": name, "built_shift": shift}), flush=True)
    _, _, extra, parity, alpha_fn, beta_fn = g.SPECS[base_name]
    base_ratio = g.base_index_ratio(extra, parity, alpha_fn, beta_fn, h)
    field_j = F.ring.gens[1]
    target_shift = F.new(
        target.numer.compose(field_j, field_j + 1),
        target.denom.compose(field_j, field_j + 1),
    )
    summand_ratio = base_ratio * target_shift / target
    ratio_numerator = g.convert_poly(summand_ratio.numer)
    ratio_denominator = g.convert_poly(summand_ratio.denom)
    a_poly, b_poly, c_poly, hits = g.gosper_normal_by_dispersion(
        ratio_numerator,
        ratio_denominator,
        1,
        g.convert_poly(target.numer),
    )
    if ratio_numerator * b_poly * c_poly - ratio_denominator * a_poly * g.shift(c_poly):
        raise AssertionError("normal form")
    b_shift = g.shift_by(b_poly, -1)
    candidate_degree = c_poly.degree() - max(a_poly.degree(), b_shift.degree())
    columns = [
        a_poly * (g.jj + 1) ** power - b_shift * g.jj**power
        for power in range(candidate_degree + 1)
    ]
    solution = g.solve_dense(columns, c_poly)
    if solution is None:
        raise ArithmeticError("no Gosper polynomial")
    x_poly = sum(
        (value * g.jj**power for power, value in enumerate(solution)),
        g.Rj.zero,
    )
    if a_poly * g.shift(x_poly) - b_shift * x_poly - c_poly:
        raise AssertionError("Gosper polynomial")
    target_numerator = g.convert_poly(target.numer)
    target_denominator = g.convert_poly(target.denom)
    telescoper_numerator = target_numerator.LC * b_shift * x_poly
    return {
        "classification": "SYMBOLIC_EXACT_INTERIOR",
        "residue": residue,
        "relation": key,
        "base_period": base_name,
        "target": str(target),
        "base_ratio": str(base_ratio),
        "normal_a": str(a_poly),
        "normal_b": str(b_poly),
        "normal_b_shift": str(b_shift),
        "normal_c": str(c_poly),
        "gosper_polynomial": str(x_poly),
        "certificate_numerator": str(b_shift * x_poly),
        "certificate_denominator": str(c_poly),
        "telescoper_numerator": str(telescoper_numerator),
        "telescoper_denominator": str(target_denominator),
        "dispersion_hits": hits,
        "verified_zero": True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("residue", type=int, choices=(1, 2))
    parser.add_argument("relation", choices=tuple(RELATIONS))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(args.residue, args.relation)
    output = args.output or HERE / f"item243_cross_gosper_r{args.residue}_{args.relation}.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(output)}))


if __name__ == "__main__":
    main()
