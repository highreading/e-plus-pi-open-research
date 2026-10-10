#!/usr/bin/env python3
"""Exact extension of the slope-10 moving-ray certificate through b=57.

Dependencies:
  sympy 1.14.0       exact factorization of the fixed ray constants
  python-flint 0.9.0 fast product-tree factorials for candidate replay

Every returned factor is independently checked by deterministic Miller-
Rabin in the <2^64 range, and the factor product is checked exactly.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
for vendor in ("_sympy", "_flint"):
    candidate = HERE / vendor
    if candidate.is_dir():
        sys.path.insert(0, str(candidate))

import flint  # type: ignore  # python-flint 0.9.0
import sympy  # type: ignore  # sympy 1.14.0
from flint import nmod_poly  # type: ignore


def load_base_module():
    candidates = (
        HERE / "mixed_cubic_moving_ray_y5_minus_y_certificate.py",
        HERE / "moving_ray_y5_minus_y_certificate.py",
    )
    path = next((candidate for candidate in candidates if candidate.is_file()), None)
    if path is None:
        raise RuntimeError(f"cannot find moving-ray base certificate in {HERE}")
    spec = importlib.util.spec_from_file_location("moving_ray_base", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_base_module()
INTERCEPTS = (27, 29, 31, 33, 37, 39, 41, 43, 47, 49, 51, 53, 57)


def deterministic_prime_u64(value: int) -> bool:
    if value < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if value % prime == 0:
            return value == prime
    odd_part = value - 1
    exponent = 0
    while odd_part % 2 == 0:
        exponent += 1
        odd_part //= 2
    # Deterministic for every unsigned 64-bit integer.
    for witness in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if witness % value == 0:
            continue
        residue = pow(witness, odd_part, value)
        if residue in (1, value - 1):
            continue
        for _ in range(exponent - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def product_level(polynomials: list[nmod_poly]) -> nmod_poly:
    assert polynomials and len(polynomials) & (len(polynomials) - 1) == 0
    level = polynomials
    while len(level) > 1:
        level = [level[index] * level[index + 1] for index in range(0, len(level), 2)]
    return level[0]


def point_product_tree(points: list[int], prime: int) -> list[list[nmod_poly]]:
    assert points and len(points) & (len(points) - 1) == 0
    levels = [[nmod_poly([(-point) % prime, 1], prime) for point in points]]
    while len(levels[-1]) > 1:
        previous = levels[-1]
        levels.append(
            [previous[index] * previous[index + 1] for index in range(0, len(previous), 2)]
        )
    return levels


def multipoint_evaluate(poly: nmod_poly, tree: list[list[nmod_poly]]) -> list[int]:
    remainders = [poly % tree[-1][0]]
    for level_index in range(len(tree) - 2, -1, -1):
        nodes = tree[level_index]
        next_remainders: list[nmod_poly] = []
        for index, remainder in enumerate(remainders):
            next_remainders.extend(
                (remainder % nodes[2 * index], remainder % nodes[2 * index + 1])
            )
        remainders = next_remainders
    return [int(remainder[0]) if len(remainder) else 0 for remainder in remainders]


def factorials_mod_prime(indices: list[int], prime: int) -> tuple[list[int], int]:
    """Evaluate every n! mod prime in O(sqrt(max n)) polynomial operations."""
    assert 0 <= max(indices) < prime < 2**64
    block_size = 1
    while block_size * block_size < max(indices):
        block_size *= 2
    block_poly = product_level(
        [nmod_poly([value % prime, 1], prime) for value in range(1, block_size + 1)]
    )
    tree = point_product_tree(
        [(block * block_size) % prime for block in range(block_size)], prime
    )
    block_values = multipoint_evaluate(block_poly, tree)
    block_prefix = [1]
    for value in block_values:
        block_prefix.append(block_prefix[-1] * value % prime)

    output: list[int] = []
    for index in indices:
        blocks, remainder = divmod(index, block_size)
        value = block_prefix[blocks]
        start = blocks * block_size
        for offset in range(1, remainder + 1):
            value = value * (start + offset) % prime
        output.append(value)
    return output, block_size


def evaluate_fraction_poly(poly, m_value: int, prime: int) -> int:
    result = 0
    power = 1
    for coefficient in poly:
        result += (
            coefficient.numerator
            * pow(coefficient.denominator, prime - 2, prime)
            * power
        )
        result %= prime
        power = power * m_value % prime
    return result


def sparse_candidate_replay(intercept: int, prime: int) -> dict[str, object]:
    """Replay a determinant candidate using the sparse Cartier/binomial formula."""
    m_value = (prime - intercept) // 10
    assert 10 * m_value + intercept == prime
    n_value = 4 * m_value + intercept
    binomial_top = 6 * m_value
    anchor_class = (intercept - 1) % 4
    high_zero_class = 3 if m_value % 2 == 0 else 1
    other_class = (high_zero_class + 2) % 4

    def unique_index(residue_index: int) -> int:
        choices = []
        for quotient in range(4):
            numerator = n_value - residue_index - 1 + quotient * prime
            if numerator % 4 == 0 and 0 <= numerator // 4 <= binomial_top:
                choices.append(numerator // 4)
        assert len(choices) == 1
        return choices[0]

    anchor_index = unique_index(anchor_class)
    other_index = unique_index(other_class)
    factorial_indices = [
        binomial_top,
        anchor_index,
        binomial_top - anchor_index,
        other_index,
        binomial_top - other_index,
    ]
    factorial_values, block_size = factorials_mod_prime(factorial_indices, prime)
    top_factorial, anchor_factorial, anchor_complement, other_factorial, other_complement = (
        factorial_values
    )
    four_anchor = (
        top_factorial
        * pow(anchor_factorial * anchor_complement % prime, prime - 2, prime)
        % prime
    )
    four_other = (
        top_factorial
        * pow(other_factorial * other_complement % prime, prime - 2, prime)
        % prime
    )
    if (binomial_top - anchor_index) % 2:
        four_anchor = -four_anchor % prime
    if (binomial_top - other_index) % 2:
        four_other = -four_other % prime

    inverse_four = pow(4, prime - 2, prime)
    anchor = four_anchor * inverse_four % prime
    other = four_other * inverse_four % prime
    first, second = BASE.functional_matrix(intercept, m_value % 2)
    first_pair = (
        evaluate_fraction_poly(first[0], m_value, prime),
        evaluate_fraction_poly(first[1], m_value, prime),
    )
    second_pair = (
        evaluate_fraction_poly(second[0], m_value, prime),
        evaluate_fraction_poly(second[1], m_value, prime),
    )
    log_pair = [
        4 * (first_pair[0] * anchor + first_pair[1] * other) % prime,
        4 * (second_pair[0] * anchor + second_pair[1] * other) % prime,
    ]
    assert log_pair != [0, 0]

    # Independent scalar recurrence for all modest candidates.
    scalar_pair = None
    if m_value <= 10_000:
        scalar_pair = list(BASE.original_log_pair(m_value, prime))
        assert scalar_pair == log_pair

    return {
        "intercept": intercept,
        "m": m_value,
        "prime": prime,
        "parity": "even" if m_value % 2 == 0 else "odd",
        "anchor_class": anchor_class,
        "other_class": other_class,
        "binomial_top": binomial_top,
        "anchor_index": anchor_index,
        "other_index": other_index,
        "factorial_indices": factorial_indices,
        "factorial_residues": factorial_values,
        "product_tree_block_size": block_size,
        "four_anchor": four_anchor,
        "four_other": four_other,
        "L_pair": log_pair,
        "independent_scalar_pair": scalar_pair,
    }


def factor_and_verify(value: int) -> dict[int, int]:
    factorization = {int(prime): int(exponent) for prime, exponent in sympy.factorint(value).items()}
    product = 1
    for prime, exponent in factorization.items():
        assert prime < 2**64
        assert deterministic_prime_u64(prime)
        product *= prime**exponent
    assert product == value
    return factorization


def certify_intercept(intercept: int) -> dict[str, object]:
    singular_index = 3 * intercept - 5
    parity_rows: list[dict[str, object]] = []
    candidates: set[int] = set()
    for parity in (0, 1):
        determinant = BASE.determinant_polynomial(intercept, parity)
        primitive, scale = BASE.primitive_integer_polynomial_with_scale(determinant)
        scale_numerator_factors = factor_and_verify(abs(scale.numerator))
        scale_denominator_factors = factor_and_verify(scale.denominator)
        assert all(prime <= singular_index for prime in scale_numerator_factors)
        assert all(prime <= singular_index for prime in scale_denominator_factors)

        ray_constant = abs(BASE.evaluate_ray_constant(primitive, intercept))
        assert ray_constant
        factors = factor_and_verify(ray_constant)
        compatible: list[dict[str, int]] = []
        for prime in factors:
            if prime <= singular_index or prime % 10 != intercept % 10:
                continue
            if (prime - intercept) <= 0 or (prime - intercept) % 10:
                continue
            m_value = (prime - intercept) // 10
            if m_value % 2 != parity:
                continue
            candidates.add(prime)
            compatible.append({"prime": prime, "m": m_value})

        parity_rows.append(
            {
                "parity": "even" if parity == 0 else "odd",
                "determinant_degree": len(primitive) - 1,
                "determinant_scale": {
                    "numerator": scale.numerator,
                    "denominator": scale.denominator,
                    "numerator_factorization": {
                        str(prime): exponent
                        for prime, exponent in sorted(scale_numerator_factors.items())
                    },
                    "denominator_factorization": {
                        str(prime): exponent
                        for prime, exponent in sorted(scale_denominator_factors.items())
                    },
                },
                "primitive_coefficients_low_to_high": list(primitive),
                "ray_constant": ray_constant,
                "ray_constant_factorization": {
                    str(prime): exponent for prime, exponent in sorted(factors.items())
                },
                "compatible_large_candidates": compatible,
            }
        )

    small_replays: list[dict[str, object]] = []
    maximum_small_m = max(0, (singular_index - intercept) // 10)
    for m_value in range(1, maximum_small_m + 1):
        prime = 10 * m_value + intercept
        if prime <= singular_index and deterministic_prime_u64(prime):
            pair = list(BASE.original_log_pair(m_value, prime))
            assert pair != [0, 0]
            small_replays.append({"m": m_value, "prime": prime, "L_pair": pair})

    candidate_replays = [
        sparse_candidate_replay(intercept, prime) for prime in sorted(candidates)
    ]
    return {
        "intercept": intercept,
        "singular_index": singular_index,
        "parity_rows": parity_rows,
        "small_prime_replays": small_replays,
        "large_candidate_replays": candidate_replays,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE.parent / "results" / "moving_ray_y5_minus_y_extended_certificate.json",
    )
    args = parser.parse_args()
    rows = [certify_intercept(intercept) for intercept in INTERCEPTS]
    payload = {
        "claim": (
            "For every listed intercept b and every m>=1 with p=10m+b prime, "
            "(L0,L1) is nonzero modulo p."
        ),
        "intercepts": list(INTERCEPTS),
        "dependencies": {
            "python": sys.version.split()[0],
            "sympy": sympy.__version__,
            "python_flint": flint.__version__,
            "flint_runtime": str(flint.__FLINT_VERSION__),
        },
        "factor_primality_check": (
            "seven-base deterministic Miller-Rabin for unsigned 64-bit integers"
        ),
        "candidate_replay": (
            "sparse Cartier binomial formula; factorials evaluated by a "
            "sqrt(p) FLINT polynomial product tree"
        ),
        "rows": rows,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["canonical_payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
