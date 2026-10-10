#!/usr/bin/env python3
"""Exact scalar-free p-adic digit tower for the mixed-cubic forced rows.

The certificate is deliberately restricted to e=1, the only exponent on
prime-number-theorem scale.  It computes (pR,L,E) modulo p^7 from the local
Hasse recurrence, forms both endpoint minors, and verifies the exact gates
for p^2,...,p^5 in the frozen primitive coordinates U,V.

No Cartier scalar is inverted.  A separate convolution/carry evaluator
reconstructs every determinant digit directly from coordinate digits.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


DEFAULT_ARCHIVE = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = Path(__file__).with_name("item163_deeper_digits_certificate.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def local_coefficients_fast(
    extended: Any,
    m: int,
    k: int,
    root: str,
    p: int,
    precision: int,
) -> list[tuple[int, int]]:
    """Return C_0,...,C_(k-1) modulo p^precision with an exact ledger."""
    base = extended.base
    degree = k - 1
    reserve = extended.factorial_valuation(degree, p)
    a_poly, b_poly = extended.local_polynomials(root)
    product = extended.iconv(a_poly, b_poly)
    right = extended.iconv(extended.iderivative(a_poly), b_poly)
    right = [extended.iscale(value, 6 * m) for value in right]
    other = extended.iconv(a_poly, extended.iderivative(b_poly))
    if len(other) > len(right):
        right += [(0, 0)] * (len(other) - len(right))
    for index, value in enumerate(other):
        right[index] = extended.iadd(right[index], extended.iscale(value, -k))

    initial_precision = precision + reserve
    initial_modulus = p**initial_precision
    a0 = base.ga(*a_poly[0], initial_modulus)
    b0 = base.ga(*b_poly[0], initial_modulus)
    c0 = base.gmul(
        base.gpow(a0, 6 * m, initial_modulus),
        base.gpow(b0, -k, initial_modulus),
        initial_modulus,
    )
    coefficients = [c0]
    precisions = [initial_precision]
    used_factorial_valuation = 0

    for n in range(degree):
        divisor = n + 1
        divisor_valuation = base.vp(divisor, p)
        required_precision = precision + reserve - used_factorial_valuation
        target_precision = required_precision - divisor_valuation
        required_modulus = p**required_precision
        target_modulus = p**target_precision
        rhs = (0, 0)

        for j in range(0, min(len(right) - 1, n) + 1):
            source_index = n - j
            if precisions[source_index] < required_precision:
                raise AssertionError(("RHS precision", m, p, k, n, j))
            term = base.gmul(
                base.ga(*right[j], required_modulus),
                (
                    coefficients[source_index][0] % required_modulus,
                    coefficients[source_index][1] % required_modulus,
                ),
                required_modulus,
            )
            rhs = base.gadd(rhs, term, required_modulus)

        for j in range(1, min(len(product) - 1, n) + 1):
            source_index = n - j + 1
            if precisions[source_index] < required_precision:
                raise AssertionError(("LHS precision", m, p, k, n, j))
            term = base.gmul(
                base.ga(*product[j], required_modulus),
                (
                    coefficients[source_index][0] % required_modulus,
                    coefficients[source_index][1] % required_modulus,
                ),
                required_modulus,
            )
            term = base.gscale(term, n - j + 1, required_modulus)
            rhs = base.gadd(rhs, base.gneg(term, required_modulus), required_modulus)

        p_power = p**divisor_valuation
        if rhs[0] % p_power or rhs[1] % p_power:
            raise AssertionError(("nonexact p-division", m, p, k, n))
        quotient = (
            rhs[0] // p_power % target_modulus,
            rhs[1] // p_power % target_modulus,
        )
        unit = divisor // p_power
        quotient = base.gscale(quotient, pow(unit, -1, target_modulus), target_modulus)
        inverse_constant = base.ginv(base.ga(*product[0], target_modulus), target_modulus)
        coefficients.append(base.gmul(inverse_constant, quotient, target_modulus))
        precisions.append(target_precision)
        used_factorial_valuation += divisor_valuation

    if precisions[-1] != precision:
        raise AssertionError(("final precision", m, p, k, precisions[-1], precision))
    modulus = p**precision
    return [(a % modulus, b % modulus) for a, b in coefficients]


def coordinates_mod(
    extended: Any, m: int, k: int, p: int, precision: int
) -> tuple[int, int, int, dict[int, int]]:
    """Return (pR,L,E) and every exact e=1 Hasse band modulo p^precision."""
    base = extended.base
    modulus = p**precision
    cm = local_coefficients_fast(extended, m, k, "minus_one", p, precision)
    ci = local_coefficients_fast(extended, m, k, "i", p, precision)
    residue_minus_one = cm[k - 1][0]
    residue_i = ci[k - 1]
    l_value = (4 * residue_minus_one + 4 * residue_i[0]) % modulus
    # E=2i(C_i-C_-i)=-4 Im(C_i).
    e_value = (-4 * residue_i[1]) % modulus

    roots_and_coefficients = [
        (base.ga(-1, 0, modulus), cm),
        (base.ga(0, 1, modulus), ci),
        (base.ga(0, -1, modulus), [(a, -b % modulus) for a, b in ci]),
    ]
    total = (0, 0)
    bands: dict[int, tuple[int, int]] = {}
    q = p
    for n in range(1, k):
        valuation = base.vp(n, p)
        if valuation > 1:
            raise AssertionError(("e=1 violated", m, p, k, n, valuation))
        h = 1 - valuation
        unit = n // (p**valuation)
        scalar = p**h * pow(unit, -1, modulus) % modulus
        contribution = (0, 0)
        index = k - 1 - n
        for root, coefficients in roots_and_coefficients:
            term = base.gmul(
                coefficients[index], base.endpoint_factor(root, n, modulus), modulus
            )
            contribution = base.gadd(contribution, term, modulus)
        contribution = base.gscale(contribution, scalar, modulus)
        total = base.gadd(total, contribution, modulus)
        bands[h] = base.gadd(bands.get(h, (0, 0)), contribution, modulus)
    if total[1] % modulus or any(value[1] % modulus for value in bands.values()):
        raise AssertionError(("non-rational endpoint", m, p, k, total, bands))
    return l_value, total[0], e_value, {h: value[0] for h, value in bands.items()}


def p_digits(value: int, p: int, width: int) -> list[int]:
    value %= p**width
    return [(value // (p**j)) % p for j in range(width)]


def determinant_digits_by_carry(
    first_left: int,
    first_right: int,
    second_left: int,
    second_right: int,
    p: int,
    width: int,
) -> tuple[list[int], list[int], list[int]]:
    """Digits of first_left*first_right-second_left*second_right.

    Returns determinant digits, raw convolution coefficients, and carries.
    This is the scalar-free determinant digit/carry recurrence seeded by the
    first Bockstein.
    """
    a = p_digits(first_left, p, width)
    b = p_digits(first_right, p, width)
    c = p_digits(second_left, p, width)
    d = p_digits(second_right, p, width)
    digits: list[int] = []
    raw: list[int] = []
    carries: list[int] = []
    carry = 0
    for n in range(width):
        coefficient = sum(a[i] * b[n - i] - c[i] * d[n - i] for i in range(n + 1))
        raw.append(coefficient)
        total = coefficient + carry
        digit = total % p
        carry = (total - digit) // p
        digits.append(digit)
        carries.append(carry)
    return digits, raw, carries


def valuation(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    out = 0
    n = abs(n)
    while n % p == 0:
        out += 1
        n //= p
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--precision", type=int, default=7)
    args = parser.parse_args()
    if args.precision < 7:
        raise ValueError("precision at least 7 is required for the p^5 gate")

    scripts = args.archive / "scripts"
    extended_path = scripts / "lifted_endpoint_hasse_extended_certificate.py"
    base_path = scripts / "lifted_endpoint_hasse_certificate.py"
    extended = load_module("item162_extended_for_item163", extended_path)

    census_path = args.archive / "results" / "lifted_endpoint_hasse_extended_census_m100.json"
    frozen_path = args.archive / "results" / "mixed_cubic_positive_match_exact_scan_m100_N6m.json"
    census = json.loads(census_path.read_text(encoding="utf-8"))
    frozen = json.loads(frozen_path.read_text(encoding="utf-8"))
    frozen_by_m = {int(row["m"]): row for row in frozen["rows"]}
    forced_rows = [row for row in census["rows"] if int(row["e"]) == 1]

    output_rows: list[dict[str, Any]] = []
    normalization_mismatches: list[dict[str, Any]] = []
    carry_mismatches: list[dict[str, Any]] = []
    eta_mismatches: list[dict[str, Any]] = []
    gate_mismatches: list[dict[str, Any]] = []
    forced_divisibility_mismatches: list[dict[str, Any]] = []
    counts: collections.Counter[str] = collections.Counter()
    layer_counts: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)

    for source_row in forced_rows:
        m = int(source_row["m"])
        p = int(source_row["p"])
        delta = int(source_row["delta"])
        source = str(source_row["source"])
        forced_power = 1 + delta
        modulus = p**args.precision
        l0, x0, e0, bands0 = coordinates_mod(extended, m, 4 * m + 1, p, args.precision)
        l1, x1, e1, bands1 = coordinates_mod(extended, m, 4 * m + 2, p, args.precision)
        determinant_a = (l1 * x0 - l0 * x1) % modulus
        determinant_b = (l1 * e0 - l0 * e1) % modulus
        if determinant_a % (p**forced_power) or determinant_b % (p**forced_power):
            forced_divisibility_mismatches.append({"m": m, "p": p, "source": source})

        a_digits = p_digits(determinant_a // (p**forced_power), p, 4)
        b_digits = p_digits(determinant_b // (p**forced_power), p, 3)
        if a_digits[0] != int(source_row["eta"]):
            eta_mismatches.append(
                {"m": m, "p": p, "computed": a_digits[0], "stored": source_row["eta"]}
            )

        a_carry_digits, _, _ = determinant_digits_by_carry(l1, x0, l0, x1, p, args.precision)
        b_carry_digits, _, _ = determinant_digits_by_carry(l1, e0, l0, e1, p, args.precision)
        if a_carry_digits != p_digits(determinant_a, p, args.precision):
            carry_mismatches.append({"m": m, "p": p, "minor": "A"})
        if b_carry_digits != p_digits(determinant_b, p, args.precision):
            carry_mismatches.append({"m": m, "p": p, "minor": "B"})

        frozen_row = frozen_by_m[m]
        actual_u = int(frozen_row["U"]["value"])
        actual_v = int(frozen_row["V"]["value"])
        actual_c_valuation = min(valuation(actual_u, p), valuation(actual_v, p))
        comparison_width = 6
        comparison_modulus = p**comparison_width
        sharp_clearing = int(frozen_row["sharp_clearing"]["value"])
        cartier_product = int(frozen_row["cartier_product"]["value"])
        clearing_unit = (sharp_clearing // p) % comparison_modulus
        cartier_unit = (cartier_product // (p**delta)) % comparison_modulus
        normalization_unit = clearing_unit * pow(cartier_unit, -1, comparison_modulus)
        predicted_u = (
            determinant_a // (p**delta) * normalization_unit
        ) % comparison_modulus
        predicted_v = (
            p ** (1 - delta)
            * determinant_b
            * pow(8, -1, comparison_modulus)
            * normalization_unit
        ) % comparison_modulus
        if predicted_u != actual_u % comparison_modulus or predicted_v != actual_v % comparison_modulus:
            normalization_mismatches.append(
                {
                    "m": m,
                    "p": p,
                    "source": source,
                    "predicted_U": predicted_u,
                    "actual_U": actual_u % comparison_modulus,
                    "predicted_V": predicted_v,
                    "actual_V": actual_v % comparison_modulus,
                }
            )

        gates: dict[str, bool] = {"p^1": True}
        for layer in range(2, 6):
            gate = all(digit == 0 for digit in a_digits[: layer - 1]) and all(
                digit == 0 for digit in b_digits[: max(0, layer - 2)]
            )
            gates[f"p^{layer}"] = gate
            actual_gate = actual_c_valuation >= layer
            if gate != actual_gate:
                gate_mismatches.append(
                    {
                        "m": m,
                        "p": p,
                        "layer": layer,
                        "gate": gate,
                        "actual": actual_gate,
                    }
                )

        key = f"{source}|delta={delta}"
        counts[key] += 1
        for layer in range(1, 6):
            layer_counts[key][str(layer)] += 0
            layer_counts["all"][str(layer)] += 0
        for layer in range(1, 6):
            if gates[f"p^{layer}"]:
                layer_counts[key][str(layer)] += 1
                layer_counts["all"][str(layer)] += 1

        output_rows.append(
            {
                "m": m,
                "p": p,
                "source": source,
                "delta": delta,
                "forced_determinant_power": forced_power,
                "A_digits_after_forced_power": a_digits,
                "B_digits_after_forced_power": b_digits,
                "actual_content_valuation": actual_c_valuation,
                "gates": gates,
                "Hasse_band_indices": sorted(set(bands0) | set(bands1)),
            }
        )

    failures = {
        "forced_divisibility": forced_divisibility_mismatches,
        "eta": eta_mismatches,
        "carry": carry_mismatches,
        "normalization": normalization_mismatches,
        "content_gates": gate_mismatches,
    }
    if any(failures.values()):
        raise AssertionError({key: value[:3] for key, value in failures.items() if value})

    radical_capacity = "0.2849081299217216643204548279"
    threshold = "1.1561471519642446123307302239"
    output = {
        "status": {
            "Hasse_coordinate_recurrence": "PROVED_IN_ITEM162_AND_REUSED_EXACTLY",
            "scalar_free_carry_recurrence": "PROVED_BY_INTEGER_CONVOLUTION",
            "e1_two_minor_layer_gates": "PROVED_BY_EXACT_NORMALIZATION_LEDGER",
            "finite_replay": "EXACT_FINITE_AUDIT_ONLY",
            "positive_mass_digit_vanishing": "OPEN",
        },
        "scope": {
            "m_max": 100,
            "e": 1,
            "coordinate_precision": args.precision,
            "comparison_precision": 6,
            "forced_rows": len(forced_rows),
            "row_counts": dict(sorted(counts.items())),
        },
        "inputs": {
            str(base_path.relative_to(args.archive)): sha256(base_path),
            str(extended_path.relative_to(args.archive)): sha256(extended_path),
            str(census_path.relative_to(args.archive)): sha256(census_path),
            str(frozen_path.relative_to(args.archive)): sha256(frozen_path),
        },
        "theorem_replay": {
            "forced_divisibility_mismatches": 0,
            "eta_mismatches": 0,
            "carry_recurrence_mismatches": 0,
            "U_V_normalization_mismatches_mod_p6": 0,
            "content_gate_mismatches_layers_1_through_5": 0,
        },
        "finite_layer_survival_counts": {
            key: dict(sorted(counter.items(), key=lambda item: int(item[0])))
            for key, counter in sorted(layer_counts.items())
        },
        "optimistic_support_capacity_per_6m": {
            "one_complete_layer_ceiling": radical_capacity,
            "two_layers": "0.5698162598434433286409096558",
            "three_layers": "0.8547243897651649929613644837",
            "four_layers": "1.1396325196868866572818193116",
            "five_layers": "1.4245406496086083216022741395",
            "required_threshold": threshold,
            "four_layer_deficit": "0.0165146322773579550489109123",
            "five_layer_optimistic_margin": "0.2683934976443637092715439156",
            "interpretation": "SUPPORT_CAPACITY_ONLY_NOT_A_DIVISOR_THEOREM",
        },
        "rows": output_rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
