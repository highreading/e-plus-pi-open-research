#!/usr/bin/env python3
"""Exact initial-value layers for the prospective Item 243 closure theorem."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


item222 = load("item243_initial_item222", "item222_j1_phase_resultant_certificate.py")
item229 = load("item243_initial_item229", "item229_j1_fixed_h_theta_certificate.py")
item237 = load("item243_initial_item237", "item237_j1_algebraic_residual_certificate.py")


def evaluate(coefficients, argument):
    answer = Fraction(0)
    for coefficient in reversed(coefficients):
        answer = answer * argument + coefficient
    return answer


def fraction_row(value):
    return [value.numerator, value.denominator]


def gauge_initials():
    rows = []
    for residue in (1, 2):
        for index in range(3):
            h = 3 * index + residue
            e_value, _ = item222.phase_fraction_and_integer(h)
            c_value = item229.phase_c(h)
            r_value = item229.conjectural_ratio(h)
            difference = c_value - r_value * e_value
            if difference:
                raise AssertionError(("gauge-initial", h, difference))
            rows.append(
                {
                    "residue": residue,
                    "index": index,
                    "h": h,
                    "c": fraction_row(c_value),
                    "R": fraction_row(r_value),
                    "E": fraction_row(e_value),
                    "difference": fraction_row(difference),
                    "all_displayed_denominators_nonzero": all(
                        value.denominator != 0 for value in (c_value, r_value, e_value)
                    ),
                }
            )
    return rows


def defect_value(h, recurrence):
    gauge = Fraction(1)
    answer = Fraction(0)
    terms = []
    for shift in range(4):
        if shift:
            gauge *= item229.rho(h + 3 * (shift - 1))
        e_value, _ = item222.phase_fraction_and_integer(h + 3 * shift)
        coefficient = evaluate(recurrence[shift], h)
        term = coefficient * gauge * e_value
        terms.append(term)
        answer += term
    return answer, terms


def defect_initials():
    recurrence = item237.recurrence_polynomials()
    rows = []
    for residue in (1, 2):
        for index in range(6):
            h = 3 * index + residue
            defect, terms = defect_value(h, recurrence)
            if defect:
                raise AssertionError(("defect-initial", h, defect))
            rows.append(
                {
                    "residue": residue,
                    "index": index,
                    "h": h,
                    "four_terms": [fraction_row(value) for value in terms],
                    "defect": fraction_row(defect),
                    "all_term_denominators_nonzero": all(
                        value.denominator != 0 for value in terms
                    ),
                }
            )
    return rows


def digest(rows):
    stream = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(stream).hexdigest()


def certificate():
    gauge = gauge_initials()
    defect = defect_initials()
    return {
        "item": 243,
        "classification": {
            "PROVED": [
                "six exact rational gauge initials c_h^*=R_h E_h^* (three per residue)",
                "twelve exact rational zeros of the target gauged-recurrence defect (six per residue)",
            ],
            "OPEN": [
                "an all-index recurrence for the defect",
                "the resulting all-h gauge identity",
                "any capacity or Route-1 rate consequence",
            ],
        },
        "logical_scope": (
            "These are initial-value prerequisites only. They do not prove either "
            "the defect recurrence or the all-h gauge identity."
        ),
        "gauge_initial_layer": {
            "count": len(gauge),
            "rows": gauge,
            "row_stream_sha256": digest(gauge),
        },
        "defect_initial_layer": {
            "count": len(defect),
            "rows": defect,
            "row_stream_sha256": digest(defect),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "item243_initial_layers_probe.json")
    args = parser.parse_args()
    result = certificate()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "gauge_initials": result["gauge_initial_layer"]["count"],
                "defect_initials": result["defect_initial_layer"]["count"],
                "gauge_stream": result["gauge_initial_layer"]["row_stream_sha256"],
                "defect_stream": result["defect_initial_layer"]["row_stream_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
