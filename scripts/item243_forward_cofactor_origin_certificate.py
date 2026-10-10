#!/usr/bin/env python3
"""Exact origin check completing the Item 243 Newton-sign argument."""

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


newton = load(
    "item243_origin_newton", "item243_forward_cofactor_newton_certificate.py"
)


def certificate():
    rows = []
    for residue in (1, 2):
        system = newton.special.build_system(residue)
        orbit_den = newton.common_denominators(residue)
        value = newton.cofactor_value(0, system, orbit_den)
        if value >= 0:
            raise AssertionError((residue, "forward cofactor at zero not negative"))
        rows.append(
            {
                "residue": residue,
                "newton_coefficient_index": 0,
                "strict_sign": -1,
                "nonzero": True,
                "fraction_fingerprint": newton.fraction_fingerprint(value),
            }
        )
    return {
        "item": 243,
        "classification": "PROVED_EXACT_FORWARD_COFACTOR_ORIGIN_SIGN",
        "rows": rows,
        "logical_completion": (
            "The Newton certificate proves every coefficient is <=0. This "
            "certificate proves coefficient Delta^0 C6(0)=C6(0)<0 in both "
            "residues. Since binomial(n,0)=1, C6(n)<0 for every integer n>=0."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "item243_forward_cofactor_origin_certificate.json",
    )
    args = parser.parse_args()
    result = certificate()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
