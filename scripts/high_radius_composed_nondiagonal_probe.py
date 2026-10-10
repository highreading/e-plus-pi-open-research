#!/usr/bin/env python3
"""Exact non-diagonal endpoint-matched HP scan for the high-radius pullback.

For nonnegative degree bounds (a,b,c), put M=a+b+c+1 and solve

    A(z)+B(z) exp(z)+C(z) G(z) = O(z^M),
    B(1)=C(1),

where

    phi(z)=z+(z^7-z^8)/140,
    G(z)=4*atan(phi(z)/(2-phi(z))).

The low equations reconstruct A.  The remaining derivative-scaled Taylor
equations for B,C and the endpoint row form an integral matrix with one more
column than rows.  The program records its exact rank/nullity, primitive
kernel, maximal-cofactor content, the separately primitive full polynomial
triple, the separately reduced endpoint pair, the first free coefficient,
and a directed rational interval certificate for the endpoint value.

This is a bounded finite diagnostic.  It proves no all-degree rank,
nonvanishing, monotonicity, or asymptotic statement.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from high_radius_composed_pullback_hp_probe import composed_jets
from mobius_arctan_hp_probe import (
    e_plus_pi_interval,
    floor_log10_positive,
    signed_interval_record,
)

sys.set_int_max_str_digits(0)

# A simple completely rational Cauchy circle.  On |z|<=RADIUS,
# |phi(z)|<=PHI_BOUND<SQRT2_LO<sqrt(2), hence both factors
# phi(z)-(1+i) and phi(z)-(1-i) have modulus at least DELTA.
RADIUS = Fraction(5, 4)
SQRT2_LO = Fraction(1414213, 10**6)
assert SQRT2_LO * SQRT2_LO < 2
PHI_BOUND = RADIUS + (RADIUS**7 + RADIUS**8) / 140
DELTA = SQRT2_LO - PHI_BOUND
assert DELTA > 0
PHI_PRIME_BOUND = 1 + (7 * RADIUS**6 + 8 * RADIUS**7) / 140
G_CIRCLE_BOUND = 4 * RADIUS * PHI_PRIME_BOUND / DELTA**2


def vector_sha256(values: list[int]) -> str:
    return hashlib.sha256(
        json.dumps(values, separators=(",", ":")).encode()
    ).hexdigest()


def integer_sha256(value: int) -> str:
    return hashlib.sha256(str(value).encode()).hexdigest()


def fraction_sha256(value: Fraction) -> str:
    return hashlib.sha256(
        f"{value.numerator}/{value.denominator}".encode()
    ).hexdigest()


def fraction_summary(value: Fraction) -> dict:
    result = {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "fraction_sha256": fraction_sha256(value),
    }
    if value > 0:
        result["floor_log10"] = floor_log10_positive(value)
    elif value == 0:
        result["zero"] = True
    return result


def falling(k: int, j: int) -> int:
    if j > k:
        return 0
    return math.factorial(k) // math.factorial(k - j)


def integer_convolution(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def derivative_recurrence_certificate(jets: list[int]) -> dict:
    """Verify G'=P/Q and its fixed-denominator coefficient recurrence."""
    # phi=p/140 with p=140z+z^7-z^8.  Thus
    # G'=560p'/(p^2-280p+39200).
    p = [0, 140, 0, 0, 0, 0, 0, 1, -1]
    p_prime = [k * p[k] for k in range(1, len(p))]
    numerator = [560 * value for value in p_prime]
    denominator = integer_convolution(p, p)
    if len(denominator) < len(p):
        denominator.extend([0] * (len(p) - len(denominator)))
    for k, value in enumerate(p):
        denominator[k] -= 280 * value
    denominator[0] += 39200
    q0 = denominator[0]
    assert q0 == 39200

    h = [
        Fraction(jets[n + 1], math.factorial(n))
        for n in range(len(jets) - 1)
    ]
    for n, value in enumerate(h):
        lhs = sum(
            (Fraction(denominator[j]) * h[n - j]
             for j in range(min(n, len(denominator) - 1) + 1)),
            Fraction(),
        )
        rhs = Fraction(numerator[n] if n < len(numerator) else 0)
        assert lhs == rhs
        assert q0 ** (n + 1) % value.denominator == 0
    return {
        "identity": (
            "G'(z)=P(z)/Q(z), P=560*p'(z), "
            "Q=p(z)^2-280*p(z)+39200, p=140*z+z^7-z^8"
        ),
        "numerator_coefficients_low_to_high": numerator,
        "denominator_coefficients_low_to_high": denominator,
        "denominator_constant": q0,
        "coefficient_recurrence": (
            "q0*h_n=P_n-sum_{j=1}^{min(n,16)}Q_j*h_{n-j}, "
            "h_n=[z^n]G'"
        ),
        "verified_through_h_index": len(h) - 1,
        "verified_denominator_divisibility": "den(h_n) divides 39200^(n+1)",
        "truncation_denominator_consequence": (
            "den(T_a G(1)) divides 39200^a*lcm(1,...,a)"
        ),
    }


def primitive_integer_vector(vector: sp.Matrix) -> list[int]:
    denominators = [int(entry.q) for entry in vector]
    denominator = reduce(math.lcm, denominators, 1)
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // common for x in integers]
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def high_matrix(a: int, b: int, c: int, jets: list[int]) -> sp.Matrix:
    """Derivative-scaled high equations k=a+1,...,M-1 plus endpoint."""
    order = a + b + c + 1
    rows: list[list[int]] = []
    for k in range(a + 1, order):
        row = [falling(k, j) for j in range(b + 1)]
        row.extend(
            falling(k, j) * jets[k - j] if j <= k else 0
            for j in range(c + 1)
        )
        rows.append(row)
    rows.append([-1] * (b + 1) + [1] * (c + 1))
    return sp.Matrix(rows)


def cofactor_content(matrix: sp.Matrix, primitive_kernel: list[int]) -> int:
    """GCD of all maximal cofactors, from one nonzero primitive coordinate."""
    for j, coordinate in enumerate(primitive_kernel):
        if coordinate:
            minor = matrix[:, :j].row_join(matrix[:, j + 1 :])
            determinant = int(DomainMatrix.from_Matrix(minor).det())
            assert determinant % coordinate == 0
            return abs(determinant // coordinate)
    raise RuntimeError("zero kernel vector")


def reconstruct_full_triple(
    a: int,
    b: int,
    c: int,
    bc: list[int],
    jets: list[int],
) -> list[int]:
    b_values = bc[: b + 1]
    c_values = bc[b + 1 :]
    a_values: list[sp.Rational] = []
    for k in range(a + 1):
        derivative = 0
        for j in range(min(b, k) + 1):
            derivative += falling(k, j) * b_values[j]
        for j in range(min(c, k) + 1):
            derivative += falling(k, j) * c_values[j] * jets[k - j]
        a_values.append(sp.Rational(-derivative, math.factorial(k)))
    return primitive_integer_vector(
        sp.Matrix(
            a_values
            + list(map(sp.Rational, b_values))
            + list(map(sp.Rational, c_values))
        )
    )


def endpoint_abs_interval(
    alpha: int,
    beta: int,
    s_interval: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction] | None:
    lo, hi = sorted(
        (
            Fraction(alpha) + beta * s_interval[0],
            Fraction(alpha) + beta * s_interval[1],
        )
    )
    if lo > 0:
        return lo, hi
    if hi < 0:
        return -hi, -lo
    return None


def solve(
    a: int,
    b: int,
    c: int,
    jets: list[int],
    s_interval: tuple[Fraction, Fraction],
) -> tuple[dict, Fraction | None, list[int] | None]:
    order = a + b + c + 1
    matrix = high_matrix(a, b, c, jets)
    domain = DomainMatrix.from_Matrix(matrix).to_field()
    rank = domain.rank()
    nullspace = domain.nullspace()
    nullity = nullspace.shape[0]
    base: dict = {
        "a": a,
        "b": b,
        "c": c,
        "total_degree_budget": a + b + c,
        "zero_order": order,
        "high_endpoint_shape": list(matrix.shape),
        "rank": rank,
        "nullity": nullity,
    }
    if nullity != 1:
        return base, None, None

    bc = primitive_integer_vector(nullspace.to_Matrix().row(0).T)
    content = cofactor_content(matrix, bc)
    triple = reconstruct_full_triple(a, b, c, bc, jets)
    a_values = triple[: a + 1]
    b_values = triple[a + 1 : a + b + 2]
    c_values = triple[a + b + 2 :]
    assert sum(b_values) == sum(c_values)

    kernel_index = next(j for j, value in enumerate(bc) if value)
    full_bc = b_values + c_values
    assert full_bc[kernel_index] % bc[kernel_index] == 0
    low_reconstruction_scale = abs(full_bc[kernel_index] // bc[kernel_index])
    assert full_bc == [
        (full_bc[kernel_index] // bc[kernel_index]) * value for value in bc
    ]

    raw_alpha = sum(a_values)
    raw_beta = sum(b_values)
    endpoint_gcd = gcd(abs(raw_alpha), abs(raw_beta))
    if endpoint_gcd:
        alpha = raw_alpha // endpoint_gcd
        beta = raw_beta // endpoint_gcd
    else:
        alpha = beta = 0
    absolute = endpoint_abs_interval(alpha, beta, s_interval)

    exp_tail_start = order - b
    g_tail_start = order - c
    assert exp_tail_start >= 1 and g_tail_start >= 1
    if endpoint_gcd:
        effective_b_height = Fraction(max(map(abs, b_values)), endpoint_gcd)
        effective_c_height = Fraction(max(map(abs, c_values)), endpoint_gcd)
        exp_tail_bound = (
            effective_b_height
            * (b + 1)
            * Fraction(
                exp_tail_start + 1,
                exp_tail_start * math.factorial(exp_tail_start),
            )
        )
        g_tail_bound = (
            effective_c_height
            * (c + 1)
            * G_CIRCLE_BOUND
            * RADIUS ** (-g_tail_start)
            / (1 - 1 / RADIUS)
        )
        total_tail_bound = exp_tail_bound + g_tail_bound
        if absolute is not None:
            assert absolute[1] <= total_tail_bound
        height_and_tail = {
            "effective_B_height_after_endpoint_reduction": fraction_summary(
                effective_b_height
            ),
            "effective_C_height_after_endpoint_reduction": fraction_summary(
                effective_c_height
            ),
            "rigorous_tail_bound": {
                "exponential_tail_start": exp_tail_start,
                "G_tail_start": g_tail_start,
                "exponential_part": fraction_summary(exp_tail_bound),
                "G_part": fraction_summary(g_tail_bound),
                "total": fraction_summary(total_tail_bound),
                "certified_below_one": total_tail_bound < 1,
                "endpoint_interval_upper_le_total": (
                    absolute[1] <= total_tail_bound
                    if absolute is not None
                    else None
                ),
            },
        }
    else:
        height_and_tail = {
            "effective_B_height_after_endpoint_reduction": None,
            "effective_C_height_after_endpoint_reduction": None,
            "rigorous_tail_bound": None,
        }

    first_free_derivative = 0
    for j in range(b + 1):
        if j <= order:
            first_free_derivative += falling(order, j) * b_values[j]
    for j in range(c + 1):
        if j <= order:
            first_free_derivative += (
                falling(order, j) * c_values[j] * jets[order - j]
            )
    first_free_coefficient = Fraction(
        first_free_derivative, math.factorial(order)
    )
    first_nonzero_index = None
    first_nonzero_derivative = 0
    for k in range(order, len(jets)):
        derivative = 0
        for j in range(b + 1):
            if j <= k:
                derivative += falling(k, j) * b_values[j]
        for j in range(c + 1):
            if j <= k:
                derivative += falling(k, j) * c_values[j] * jets[k - j]
        if derivative:
            first_nonzero_index = k
            first_nonzero_derivative = derivative
            break

    high_height = max(map(abs, bc))
    triple_height = max(map(abs, triple))
    base.update(
        {
            "primitive_high_kernel_height": high_height,
            "primitive_high_kernel_height_digits": len(str(high_height)),
            "primitive_high_kernel_sha256": vector_sha256(bc),
            "maximal_cofactor_common_content": content,
            "maximal_cofactor_common_content_digits": len(str(content)),
            "maximal_cofactor_common_content_sha256": integer_sha256(content),
            "low_reconstruction_scale": low_reconstruction_scale,
            "low_reconstruction_scale_digits": len(str(low_reconstruction_scale)),
            "primitive_triple_height": triple_height,
            "primitive_triple_height_digits": len(str(triple_height)),
            "primitive_triple_sha256": vector_sha256(triple),
            "degree_bounds_attained": {
                "A": bool(a_values[-1]),
                "B": bool(b_values[-1]),
                "C": bool(c_values[-1]),
                "all": bool(a_values[-1] and b_values[-1] and c_values[-1]),
            },
            "raw_endpoint_pair": [raw_alpha, raw_beta],
            "endpoint_gcd": endpoint_gcd,
            "endpoint_gcd_digits": len(str(endpoint_gcd)),
            "reduced_endpoint_pair": [alpha, beta],
            "endpoint_B_nonzero": beta != 0,
            "endpoint_pair_nonzero": bool(alpha or beta),
            "endpoint_interval_certificate": signed_interval_record(
                alpha, beta, *s_interval
            ),
            "first_free": {
                "index": order,
                "derivative_value": first_free_derivative,
                "coefficient_numerator": first_free_coefficient.numerator,
                "coefficient_denominator": first_free_coefficient.denominator,
                "coefficient_sha256": fraction_sha256(first_free_coefficient),
                "nonzero": bool(first_free_derivative),
            },
            "first_nonzero_at_or_after_free": (
                {
                    "index": first_nonzero_index,
                    "derivative_value": first_nonzero_derivative,
                    "extra_vanishing_orders": first_nonzero_index - order,
                }
                if first_nonzero_index is not None
                else {
                    "index": None,
                    "lookahead_exhausted": True,
                    "checked_through_index": len(jets) - 1,
                }
            ),
        }
    )
    base.update(height_and_tail)
    return base, absolute[1] if absolute is not None else None, triple


def selected_record(
    record: dict,
    upper: Fraction,
    triple: list[int],
) -> dict:
    return {
        "total_degree_budget": record["total_degree_budget"],
        "degrees": [record["a"], record["b"], record["c"]],
        "floor_log10_abs_upper": floor_log10_positive(upper),
        "upper_fraction_sha256": fraction_sha256(upper),
        "primitive_triple": triple,
        "primitive_triple_sha256": record["primitive_triple_sha256"],
        "primitive_triple_height_digits": record[
            "primitive_triple_height_digits"
        ],
        "cofactor_content_digits": record[
            "maximal_cofactor_common_content_digits"
        ],
        "endpoint_gcd_digits": record["endpoint_gcd_digits"],
        "reduced_endpoint_pair": record["reduced_endpoint_pair"],
        "first_free_nonzero": record["first_free"]["nonzero"],
        "first_nonzero_at_or_after_free": record[
            "first_nonzero_at_or_after_free"
        ],
    }


def canonical_endpoint_pair(record: dict) -> tuple[int, int]:
    alpha, beta = record["reduced_endpoint_pair"]
    if alpha < 0 or (alpha == 0 and beta < 0):
        return -alpha, -beta
    return alpha, beta


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-total", type=int, default=18)
    parser.add_argument(
        "--free-lookahead",
        type=int,
        default=32,
        help="extra exact jet orders used to diagnose accidental superconvergence",
    )
    parser.add_argument(
        "--constant-bc-max-a",
        type=int,
        default=200,
        help="continue the constant B=C ray (a,0,0) through this a",
    )
    parser.add_argument(
        "--a0-cconstant-max-b",
        type=int,
        default=250,
        help="continue the edge (a,b,c)=(0,b,0) through this b",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_total < 0:
        raise ValueError("max-total must be nonnegative")
    if args.free_lookahead < 1:
        raise ValueError("free-lookahead must be positive")
    if args.constant_bc_max_a < 0:
        raise ValueError("constant-bc-max-a must be nonnegative")
    if args.a0_cconstant_max_b < 0:
        raise ValueError("a0-cconstant-max-b must be nonnegative")

    largest_order = max(
        args.max_total,
        args.constant_bc_max_a,
        args.a0_cconstant_max_b,
    )
    jets = composed_jets(largest_order + 1 + args.free_lookahead)
    s_interval = e_plus_pi_interval()
    records: list[dict] = []
    best: list[dict] = []
    best_attained: list[dict] = []
    best_interior: list[dict] = []
    best_coupled: list[dict] = []
    best_new_endpoint_line: list[dict] = []
    below_one: list[dict] = []
    rank_exceptions: list[dict] = []
    first_free_zeros: list[list[int]] = []
    endpoint_lines_seen_before_total: set[tuple[int, int]] = set()
    global_best_item: tuple[Fraction, dict, list[int]] | None = None
    cumulative_best: list[dict] = []

    for total in range(args.max_total + 1):
        candidates: list[tuple[Fraction, dict, list[int]]] = []
        attained_candidates: list[tuple[Fraction, dict, list[int]]] = []
        interior_candidates: list[tuple[Fraction, dict, list[int]]] = []
        coupled_candidates: list[tuple[Fraction, dict, list[int]]] = []
        new_line_candidates: list[tuple[Fraction, dict, list[int]]] = []
        endpoint_lines_this_total: set[tuple[int, int]] = set()
        for a in range(total + 1):
            for b in range(total - a + 1):
                c = total - a - b
                record, upper, triple = solve(a, b, c, jets, s_interval)
                records.append(record)
                if record["nullity"] != 1:
                    rank_exceptions.append(
                        {
                            "degrees": [a, b, c],
                            "rank": record["rank"],
                            "nullity": record["nullity"],
                        }
                    )
                    continue
                assert triple is not None
                if not record["first_free"]["nonzero"]:
                    first_free_zeros.append([a, b, c])
                if upper is None or not record["endpoint_B_nonzero"]:
                    continue
                item = (upper, record, triple)
                endpoint_line = canonical_endpoint_pair(record)
                endpoint_lines_this_total.add(endpoint_line)
                if endpoint_line not in endpoint_lines_seen_before_total:
                    new_line_candidates.append(item)
                candidates.append(item)
                if record["degree_bounds_attained"]["all"]:
                    attained_candidates.append(item)
                    if b >= 1 and c >= 1:
                        coupled_candidates.append(item)
                    if min(a, b, c) >= 1:
                        interior_candidates.append(item)
                if upper < 1:
                    below_one.append(selected_record(record, upper, triple))

        if candidates:
            upper, record, triple = min(candidates, key=lambda item: item[0])
            best.append(selected_record(record, upper, triple))
            if global_best_item is None or upper < global_best_item[0]:
                global_best_item = (upper, record, triple)
        if attained_candidates:
            upper, record, triple = min(
                attained_candidates, key=lambda item: item[0]
            )
            best_attained.append(selected_record(record, upper, triple))
        if interior_candidates:
            upper, record, triple = min(
                interior_candidates, key=lambda item: item[0]
            )
            best_interior.append(selected_record(record, upper, triple))
        if coupled_candidates:
            upper, record, triple = min(
                coupled_candidates, key=lambda item: item[0]
            )
            best_coupled.append(selected_record(record, upper, triple))
        if new_line_candidates:
            upper, record, triple = min(
                new_line_candidates, key=lambda item: item[0]
            )
            best_new_endpoint_line.append(
                selected_record(record, upper, triple)
            )
        endpoint_lines_seen_before_total.update(endpoint_lines_this_total)
        if global_best_item is not None:
            upper, record, triple = global_best_item
            cumulative = selected_record(record, upper, triple)
            cumulative["scanned_through_total_degree_budget"] = total
            cumulative_best.append(cumulative)

    constant_bc_ray: list[dict] = []
    for a in range(args.constant_bc_max_a + 1):
        record, upper, _triple = solve(a, 0, 0, jets, s_interval)
        assert record["nullity"] == 1
        assert record["endpoint_B_nonzero"]
        assert upper is not None
        alpha, beta = record["reduced_endpoint_pair"]
        if beta < 0:
            alpha, beta = -alpha, -beta
        constant_bc_ray.append(
            {
                "a": a,
                "approximant_numerator_P": -alpha,
                "approximant_denominator_Q": beta,
                "denominator_Q_digits": len(str(beta)),
                "denominator_Q_sha256": integer_sha256(beta),
                "floor_log10_abs_primitive_endpoint_upper": (
                    floor_log10_positive(upper)
                ),
                "primitive_triple_height_digits": record[
                    "primitive_triple_height_digits"
                ],
                "endpoint_gcd_digits": record["endpoint_gcd_digits"],
                "first_free_nonzero": record["first_free"]["nonzero"],
            }
        )

    # The edge (a,b,c)=(0,b,0) has a closed two-coordinate description.
    # Put H=e^{-z}G=sum eta_k z^k/k!.  Multiplying the cancellation
    # identity by e^{-z} gives
    #
    #   B=-T_b(Ae^{-z}+CH),  -A U_b=C V_b,
    #   U_b=b! T_b(e^{-z})(1),  V_b=b!(1+T_bH(1)).
    #
    # Integral G-jets imply integral eta_k.  Therefore
    # U_b=b U_{b-1}+(-1)^b and V_b=b V_{b-1}+eta_b.  After dividing by
    # gcd(U_b,V_b), the endpoint pair is (-V_b,U_b), up to common sign.
    eta = [
        sum(
            math.comb(k, j) * (-1) ** (k - j) * jets[j]
            for j in range(k + 1)
        )
        for k in range(args.a0_cconstant_max_b + 1)
    ]
    a0_cconstant_edge: list[dict] = []
    edge_best: tuple[Fraction, int, list[int]] | None = None
    u_coordinate = 0
    v_coordinate = 0
    scanned_record = {
        (record["a"], record["b"], record["c"]): record
        for record in records
    }
    for b in range(args.a0_cconstant_max_b + 1):
        if b == 0:
            u_coordinate = 1
            v_coordinate = 1 + eta[0]
        else:
            u_coordinate = b * u_coordinate + (-1) ** b
            v_coordinate = b * v_coordinate + eta[b]
        coordinate_gcd = gcd(abs(u_coordinate), abs(v_coordinate))
        alpha = -v_coordinate // coordinate_gcd
        beta = u_coordinate // coordinate_gcd
        absolute = endpoint_abs_interval(alpha, beta, s_interval)
        assert absolute is not None
        upper = absolute[1]
        canonical = (alpha, beta)
        if canonical[0] < 0 or (canonical[0] == 0 and canonical[1] < 0):
            canonical = (-canonical[0], -canonical[1])
        if b <= args.max_total:
            record = scanned_record[(0, b, 0)]
            assert canonical == canonical_endpoint_pair(record)
        item = {
            "b": b,
            "eta_b": eta[b],
            "eta_b_sha256": integer_sha256(eta[b]),
            "U_b": u_coordinate,
            "V_b": v_coordinate,
            "formula_coordinate_gcd": coordinate_gcd,
            "formula_coordinate_gcd_digits": len(str(coordinate_gcd)),
            "reduced_endpoint_pair_with_positive_beta": [alpha, beta],
            "floor_log10_abs_primitive_endpoint_upper": (
                floor_log10_positive(upper)
            ),
            "upper_fraction_sha256": fraction_sha256(upper),
        }
        a0_cconstant_edge.append(item)
        if beta and (edge_best is None or upper < edge_best[0]):
            edge_best = (upper, b, [alpha, beta])

    result = {
        "source_script_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "python_version": sys.version,
        "sympy_version": sp.__version__,
        "family": (
            "G(z)=4*atan(phi(z)/(2-phi(z))), "
            "phi=z+(z^7-z^8)/140"
        ),
        "system": (
            "deg(A)<=a, deg(B)<=b, deg(C)<=c; "
            "A+B*exp+C*G=O(z^(a+b+c+1)); B(1)=C(1)"
        ),
        "scan": "all nonnegative degree triples with a+b+c<=max_total",
        "max_total": args.max_total,
        "record_count": len(records),
        "computed_jet_count": len(jets),
        "first_free_lookahead": args.free_lookahead,
        "computed_G_jet_sha256": vector_sha256(jets),
        "all_computed_G_jets_integral": True,
        "G_derivative_recurrence_certificate": (
            derivative_recurrence_certificate(jets)
        ),
        "rational_cauchy_bound": {
            "radius": fraction_summary(RADIUS),
            "sqrt2_strict_lower": fraction_summary(SQRT2_LO),
            "phi_modulus_upper": fraction_summary(PHI_BOUND),
            "distance_lower_to_each_base_singularity": fraction_summary(DELTA),
            "phi_prime_modulus_upper": fraction_summary(PHI_PRIME_BOUND),
            "G_modulus_upper_on_circle": fraction_summary(G_CIRCLE_BOUND),
        },
        "rank_or_nullity_exceptions": rank_exceptions,
        "first_free_coefficient_zeros": first_free_zeros,
        "best_by_total_degree_budget": best,
        "best_with_all_degree_bounds_attained": best_attained,
        "best_interior_with_all_degree_bounds_attained": best_interior,
        "best_coupled_BC_with_all_degree_bounds_attained": best_coupled,
        "best_endpoint_line_not_seen_at_smaller_total": best_new_endpoint_line,
        "cumulative_best_through_each_total_budget": cumulative_best,
        "global_best_through_max_total": (
            selected_record(
                global_best_item[1], global_best_item[0], global_best_item[2]
            )
            if global_best_item is not None
            else None
        ),
        "distinct_nonzero_endpoint_lines": len(endpoint_lines_seen_before_total),
        "constant_B_equals_C_ray_max_a": args.constant_bc_max_a,
        "constant_B_equals_C_ray": constant_bc_ray,
        "a0_C_constant_edge_identity": (
            "H=e^{-z}G=sum eta_k*z^k/k!; "
            "U_b=b!*T_b(e^{-z})(1), V_b=b!*(1+T_bH(1)); "
            "U_b=b*U_{b-1}+(-1)^b, V_b=b*V_{b-1}+eta_b; "
            "primitive endpoint=(-V_b,U_b)/gcd(U_b,V_b) up to sign"
        ),
        "a0_C_constant_edge_max_b": args.a0_cconstant_max_b,
        "a0_C_constant_edge": a0_cconstant_edge,
        "a0_C_constant_edge_best": (
            {
                "b": edge_best[1],
                "reduced_endpoint_pair_with_positive_beta": edge_best[2],
                "floor_log10_abs_primitive_endpoint_upper": (
                    floor_log10_positive(edge_best[0])
                ),
                "upper_fraction_sha256": fraction_sha256(edge_best[0]),
            }
            if edge_best is not None
            else None
        ),
        "certified_nonzero_endpoint_forms_below_one": below_one,
        "records": records,
        "warning": (
            "Finite exact diagnostic only; observed rank, nonvanishing, "
            "degree-allocation, and size patterns have no automatic "
            "all-degree or asymptotic implication."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
