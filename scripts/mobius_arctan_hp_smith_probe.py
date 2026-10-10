#!/usr/bin/env python3
"""Exact finite Smith-form probe for the endpoint-matched Mobius HP matrix.

This imports the integer matrix convention from ``mobius_arctan_hp_probe.py``
and computes its Smith invariant factors over ZZ.  The calculation is a
finite diagnostic only; it proves no formula for arbitrary degree.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


sys.set_int_max_str_digits(0)


def load_matrix_module(script_dir: Path):
    source = script_dir / "mobius_arctan_hp_probe.py"
    spec = importlib.util.spec_from_file_location("mobius_arctan_hp_probe", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def factorization(value: int) -> dict[str, int]:
    return {
        str(prime): exponent
        for prime, exponent in sorted(sp.factorint(abs(value)).items())
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=14)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--cofactor-result",
        type=Path,
        help="optional mobius_arctan_hp_n15.json used for an exact product check",
    )
    args = parser.parse_args()
    if args.max_n < 1:
        raise ValueError("max_n must be positive")

    matrix_module = load_matrix_module(Path(__file__).resolve().parent)
    expected: dict[int, int] = {}
    if args.cofactor_result:
        source = json.loads(args.cofactor_result.read_text())
        expected = {
            int(record["n"]): int(record["maximal_cofactor_common_content"])
            for record in source["records"]
            if "maximal_cofactor_common_content" in record
        }

    records = []
    for n in range(1, args.max_n + 1):
        matrix = matrix_module.high_matrix(n)
        smith = smith_normal_form(matrix, domain=ZZ)
        invariants = [
            abs(int(smith[index, index]))
            for index in range(min(smith.shape))
            if smith[index, index]
        ]
        product = math.prod(invariants)
        expected_content = expected.get(n)
        if expected_content is not None:
            assert product == expected_content
        records.append(
            {
                "n": n,
                "matrix_shape": list(matrix.shape),
                "nonzero_invariant_factors": invariants,
                "nonzero_invariant_factor_prime_factorizations": [
                    factorization(value) for value in invariants
                ],
                "product_of_nonzero_invariant_factors": product,
                "product_decimal_digits": len(str(product)),
                "matches_archived_maximal_cofactor_gcd": (
                    None if expected_content is None else product == expected_content
                ),
            }
        )

    rendered = json.dumps(
        {
            "matrix": "M_n from mobius_arctan_hp_probe.py",
            "range": [1, args.max_n],
            "records": records,
            "warning": "Finite exact diagnostics only; no all-degree Smith formula is claimed.",
        },
        indent=2,
        sort_keys=True,
    ) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
