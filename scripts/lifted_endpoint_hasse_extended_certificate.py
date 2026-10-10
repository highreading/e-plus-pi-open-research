#!/usr/bin/env python3
"""Extended exact census for the mixed-cubic lifted Hasse digit.

Depends on the item-161 sibling script for normalization and endpoint logic,
but replaces its generic truncated-series exponentiation by an O(K) exact
p-adic recurrence.  All pattern searches are finite diagnostics.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "lifted_endpoint_hasse_certificate.py"
if not BASE_PATH.exists():
    BASE_PATH = HERE / "lifted_endpoint_hasse_certificate.py"
SPEC = importlib.util.spec_from_file_location("lifted_endpoint_hasse_item161", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {BASE_PATH}")
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)
slow_local_coefficients = base.local_coefficients


G = tuple[int, int]


def imul(x: G, y: G) -> G:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def iadd(x: G, y: G) -> G:
    return x[0] + y[0], x[1] + y[1]


def iscale(x: G, scalar: int) -> G:
    return x[0] * scalar, x[1] * scalar


def iconv(left: list[G], right: list[G]) -> list[G]:
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = iadd(out[i + j], imul(x, y))
    return out


def iderivative(poly: list[G]) -> list[G]:
    return [iscale(poly[j], j) for j in range(1, len(poly))]


def factorial_valuation(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def local_polynomials(root: str) -> tuple[list[G], list[G]]:
    if root == "minus_one":
        return [(-2, 0), (3, 0), (-1, 0)], [(2, 0), (-2, 0), (1, 0)]
    if root == "i":
        return [(1, 1), (1, -2), (-1, 0)], [(-2, 2), (1, 3), (1, 0)]
    raise ValueError(root)


def local_coefficients_fast(m: int, k: int, root: str, mod: int) -> list[G]:
    """Compute C_r=[t^r]A(t)^(6m)/B(t)^k in O(k) operations.

    If F=A^N/B^K, then (AB)F'=(N A'B-K AB')F.  Division by n+1
    is performed with a precision reserve v_p((k-1)!), so the returned
    coefficient C_r is still known modulo the requested p-power.
    """
    # Recover p and requested exponent from mod=p^precision.
    factors = base.primes_upto(math.isqrt(mod) + 1)
    p = next((candidate for candidate in factors if mod % candidate == 0), mod)
    if p == 2:
        raise ValueError("only odd p is used")
    requested = 0
    test = mod
    while test % p == 0:
        requested += 1
        test //= p
    if test != 1:
        raise ValueError(("modulus is not a prime power", mod))

    degree = k - 1
    reserve = factorial_valuation(degree, p)
    a_poly, b_poly = local_polynomials(root)
    product = iconv(a_poly, b_poly)
    right = iconv(iderivative(a_poly), b_poly)
    right = [iscale(value, 6 * m) for value in right]
    other = iconv(a_poly, iderivative(b_poly))
    if len(other) > len(right):
        right += [(0, 0)] * (len(other) - len(right))
    for index, value in enumerate(other):
        right[index] = iadd(right[index], iscale(value, -k))

    initial_precision = requested + reserve
    initial_mod = p**initial_precision
    a0 = base.ga(*a_poly[0], initial_mod)
    b0 = base.ga(*b_poly[0], initial_mod)
    c0 = base.gmul(
        base.gpow(a0, 6 * m, initial_mod),
        base.gpow(b0, -k, initial_mod),
        initial_mod,
    )
    coefficients: list[G] = [c0]
    precisions = [initial_precision]
    used_factorial_v = 0

    for n in range(degree):
        divisor = n + 1
        divisor_v = base.vp(divisor, p)
        required_precision = requested + reserve - used_factorial_v
        target_precision = required_precision - divisor_v
        required_mod = p**required_precision
        target_mod = p**target_precision
        rhs = (0, 0)

        for j in range(0, min(len(right) - 1, n) + 1):
            index = n - j
            if precisions[index] < required_precision:
                raise AssertionError(("insufficient RHS precision", n, j))
            term = base.gmul(
                base.ga(*right[j], required_mod),
                (coefficients[index][0] % required_mod, coefficients[index][1] % required_mod),
                required_mod,
            )
            rhs = base.gadd(rhs, term, required_mod)

        for j in range(1, min(len(product) - 1, n) + 1):
            index = n - j + 1
            if precisions[index] < required_precision:
                raise AssertionError(("insufficient LHS precision", n, j))
            term = base.gmul(
                base.ga(*product[j], required_mod),
                (coefficients[index][0] % required_mod, coefficients[index][1] % required_mod),
                required_mod,
            )
            term = base.gscale(term, n - j + 1, required_mod)
            rhs = base.gadd(rhs, base.gneg(term, required_mod), required_mod)

        p_power = p**divisor_v
        if rhs[0] % p_power or rhs[1] % p_power:
            raise AssertionError(("nonexact p-division", m, k, root, n, rhs, p_power))
        quotient = (rhs[0] // p_power % target_mod, rhs[1] // p_power % target_mod)
        unit = divisor // p_power
        quotient = base.gscale(quotient, pow(unit, -1, target_mod), target_mod)
        p0_inverse = base.ginv(base.ga(*product[0], target_mod), target_mod)
        next_coefficient = base.gmul(p0_inverse, quotient, target_mod)
        coefficients.append(next_coefficient)
        precisions.append(target_precision)
        used_factorial_v += divisor_v

    if precisions[-1] != requested:
        raise AssertionError(("precision ledger", precisions[-1], requested))
    return [(a % mod, b % mod) for a, b in coefficients]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def eta_with_top(m: int, p: int, e: int, delta: int) -> tuple[int, int, dict[str, Any]]:
    precision = 2 + delta
    modulus = p**precision
    k0 = 4 * m + 1
    l0, x0, bands0 = base.lifted_coordinates(m, k0, p, e, delta)
    l1, x1, bands1 = base.lifted_coordinates(m, k0 + 1, p, e, delta)
    divisor = p ** (1 + delta)
    determinant = (l1 * x0 - l0 * x1) % modulus
    top_determinant = (
        l1 * bands0.get(0, 0) - l0 * bands1.get(0, 0)
    ) % modulus
    if determinant % divisor or top_determinant % divisor:
        raise AssertionError(("forced determinant", m, p, determinant, top_determinant))
    return determinant // divisor % p, top_determinant // divisor % p, {
        "band_indices": sorted(set(bands0) | set(bands1)),
    }


def grouped_counts(rows: list[dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, collections.Counter[str]] = {
        "source": collections.Counter(),
        "delta": collections.Counter(),
        "e": collections.Counter(),
        "source_delta_e": collections.Counter(),
    }
    for row in rows:
        source = str(row["source"])
        delta = str(row["delta"])
        exponent = str(row["e"])
        out["source"][source] += 1
        out["delta"][delta] += 1
        out["e"][exponent] += 1
        out["source_delta_e"][f"{source}|delta={delta}|e={exponent}"] += 1
    return {key: dict(sorted(value.items())) for key, value in out.items()}


def affine_digit_search(rows: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = collections.defaultdict(list)
    for row in rows:
        key = (
            row["source"], row["p"], row["e"], row["delta"], row["m"] % row["q"]
        )
        groups[key].append(row)
    tested, passed, failed = [], [], []
    for key, group in sorted(groups.items(), key=lambda item: tuple(map(str, item[0]))):
        p = int(key[1])
        points = sorted({(int(row["m"]) // int(row["q"]), int(row["eta"])) for row in group})
        residues = sorted({t % p for t, _ in points})
        if len(points) < 3 or len(residues) < 3:
            continue
        pair = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if (points[j][0] - points[i][0]) % p:
                    pair = points[i], points[j]
                    break
            if pair:
                break
        if pair is None:
            continue
        (t0, y0), (t1, y1) = pair
        slope = (y1 - y0) * pow((t1 - t0) % p, -1, p) % p
        intercept = (y0 - slope * t0) % p
        agrees = all((slope * t + intercept - y) % p == 0 for t, y in points)
        record = {
            "source": key[0], "p": p, "e": key[2], "delta": key[3],
            "m_mod_q": key[4], "point_count": len(points),
            "slope": slope, "intercept": intercept, "points": points,
        }
        tested.append(record)
        (passed if agrees else failed).append(record)
    return {
        "status": "EXPERIMENTAL_FINITE_SEARCH_ONLY",
        "groups_tested": len(tested),
        "groups_passing": len(passed),
        "groups_failing": len(failed),
        "passing_groups": passed,
        "first_failing_groups": failed[:30],
    }


def residue_law_search(rows: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = collections.defaultdict(list)
    for row in rows:
        groups[(row["source"], row["p"], row["e"], row["delta"])].append(row)
    candidates, collisions = [], []
    for key, group in sorted(groups.items(), key=lambda item: tuple(map(str, item[0]))):
        by_residue: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
        p = int(key[1])
        for row in group:
            by_residue[int(row["m"]) % p].append(row)
        repeated = {r: values for r, values in by_residue.items() if len(values) >= 2}
        if len(group) < 5 or not repeated:
            continue
        mixed = {
            r: values for r, values in repeated.items()
            if len({int(value["eta"]) == 0 for value in values}) > 1
        }
        record = {
            "source": key[0], "p": p, "e": key[2], "delta": key[3],
            "row_count": len(group),
            "repeated_residue_count": len(repeated),
            "zero_repeated_residues": sorted(
                r for r, values in repeated.items() if all(int(value["eta"]) == 0 for value in values)
            ),
            "mixed_repeated_residues": sorted(mixed),
        }
        if mixed:
            collisions.append(record)
        else:
            candidates.append(record)
    return {
        "status": "EXPERIMENTAL_FINITE_SEARCH_ONLY",
        "collision_free_sample_groups": candidates,
        "groups_with_zero_nonzero_collision": collisions,
    }


def prime_ray_search(rows: list[dict[str, Any]], max_denominator: int = 12) -> dict[str, Any]:
    candidates = []
    large_zero_lines = []
    for denominator in range(1, max_denominator + 1):
        for numerator in range(1, 2 * denominator):
            if math.gcd(numerator, denominator) != 1:
                continue
            lines: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
            for row in rows:
                intercept = denominator * int(row["p"]) - numerator * int(row["m"])
                lines[intercept].append(row)
            for intercept, group in lines.items():
                large_zeros = [
                    row for row in group if int(row["eta"]) == 0 and int(row["p"]) >= 29
                ]
                if len(large_zeros) >= 2:
                    large_zero_lines.append({
                        "equation": f"{denominator}*p={numerator}*m+({intercept})",
                        "large_zero_points": sorted([int(row["m"]), int(row["p"])] for row in large_zeros),
                        "nonzero_counterexamples": sorted(
                            [int(row["m"]), int(row["p"]), int(row["eta"])]
                            for row in group if int(row["eta"]) != 0
                        ),
                    })
                if len(group) < 4:
                    continue
                if all(int(row["eta"]) == 0 for row in group):
                    candidates.append({
                        "equation": f"{denominator}*p={numerator}*m+({intercept})",
                        "numerator": numerator,
                        "denominator": denominator,
                        "intercept": intercept,
                        "point_count": len(group),
                        "m_span": max(int(row["m"]) for row in group) - min(int(row["m"]) for row in group),
                        "points": sorted([int(row["m"]), int(row["p"]), row["source"]] for row in group),
                    })
    candidates.sort(key=lambda item: (-item["point_count"], -item["m_span"], item["equation"]))
    return {
        "status": "EXPERIMENTAL_FINITE_SEARCH_ONLY_NO_RAY_IS_PROVED",
        "slope_denominator_bound": max_denominator,
        "minimum_points": 4,
        "all_zero_candidate_count": len(candidates),
        "all_zero_candidates": candidates,
        "lines_with_at_least_two_zero_points_p_ge_29": large_zero_lines,
        "such_lines_without_a_nonzero_counterexample": sum(
            not row["nonzero_counterexamples"] for row in large_zero_lines
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, default=base.DEFAULT_ARCHIVE)
    parser.add_argument("--max-m", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    maximum_m = min(args.max_m, 100)

    # Validate the fast recurrence against the item-161 generic power-series
    # implementation before replacing it.
    spot_cases = [(3, 3, 0), (6, 7, 0), (9, 13, 1), (13, 11, 1)]
    spot_checks = 0
    for m, p, delta in spot_cases:
        modulus = p ** (2 + delta)
        for k in (4 * m + 1, 4 * m + 2):
            for root in ("minus_one", "i"):
                slow = slow_local_coefficients(m, k, root, modulus)
                fast = local_coefficients_fast(m, k, root, modulus)
                if slow != fast:
                    raise AssertionError(("fast/slow mismatch", m, p, delta, k, root))
                spot_checks += 1
    base.local_coefficients = local_coefficients_fast

    scan_path = args.archive / "results" / "mixed_cubic_positive_match_exact_scan_m100_N6m.json"
    rank_two_path = args.archive / "results" / "mixed_cubic_rank_two_cartier_certificate.json"
    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    rank_two = json.loads(rank_two_path.read_text(encoding="utf-8"))
    u_by_m = {int(row["m"]): int(row["U"]["value"]) for row in scan["rows"]}

    tasks: dict[tuple[int, int], dict[str, Any]] = {}
    for m in range(1, maximum_m + 1):
        for row in base.rank_one_rows(m):
            tasks[(m, int(row["p"]))] = {**row, "sources": {"rank_one"}}
    for index_row in rank_two["index_rows"]:
        m = int(index_row["m"])
        if m > maximum_m:
            continue
        for archived in index_row["vanishing_rank_two_rows"]:
            p = int(archived["p"])
            candidate = {
                "p": p,
                "e": int(archived["denominator_exponent"]),
                "q": int(archived["top_prime_power_layer"]),
                "delta": int(bool(archived["rank_zero_at_first_cartier"])),
            }
            if (m, p) in tasks:
                existing = tasks[(m, p)]
                if any(int(existing[key]) != int(candidate[key]) for key in ("p", "e", "q", "delta")):
                    raise AssertionError(("source disagreement", m, existing, candidate))
                existing["sources"].add("rank_two_zero")
            else:
                tasks[(m, p)] = {**candidate, "sources": {"rank_two_zero"}}

    rows: list[dict[str, Any]] = []
    mismatches = []
    for (m, p), task in sorted(tasks.items()):
        source = "+".join(sorted(task["sources"]))
        eta, top_eta, details = eta_with_top(m, p, int(task["e"]), int(task["delta"]))
        expected = base.expected_eta_from_u(m, task, u_by_m[m])
        if eta != expected:
            mismatches.append((m, p, eta, expected))
        rows.append({
            "m": m, "p": p, "e": int(task["e"]), "q": int(task["q"]),
            "delta": int(task["delta"]), "source": source,
            "eta": eta, "expected_eta": expected, "top_only_eta": top_eta,
            "top_only_changes_eta": eta != top_eta,
            "band_indices": details["band_indices"],
        })
    if mismatches:
        raise AssertionError(mismatches[:5])

    zero_rows = [row for row in rows if int(row["eta"]) == 0]
    top_changes = [row for row in rows if bool(row["top_only_changes_eta"])]
    output = {
        "schema": "mixed-cubic-lifted-endpoint-hasse-extended-census-v1",
        "status": {
            "uniform_formula": "PROVED_IN_ITEM_161_COMPANION_NOTE",
            "fast_recurrence": "PROVED_BY_THE_DISPLAYED_FIRST_ORDER_ODE_AND_PRECISION_LEDGER",
            "finite_census_and_pattern_searches": "EXPERIMENTAL_EXACT_FINITE_ONLY",
            "positive_weighted_mass_family": "OPEN",
        },
        "inputs": {
            BASE_PATH.name: sha256(BASE_PATH),
            scan_path.name: sha256(scan_path),
            rank_two_path.name: sha256(rank_two_path),
        },
        "parameters": {"max_m": maximum_m},
        "summary": {
            "fast_slow_spot_checks": spot_checks,
            "total_unique_forced_rows": len(rows),
            "eta_zero_rows": len(zero_rows),
            "eta_nonzero_rows": len(rows) - len(zero_rows),
            "mismatches_against_frozen_actual_U": len(mismatches),
            "rows_where_deleting_lower_bands_changes_eta": len(top_changes),
            "all_rows_by_source_delta_e": grouped_counts(rows),
            "eta_zero_rows_by_source_delta_e": grouped_counts(zero_rows),
        },
        "eta_zero_rows": zero_rows,
        "affine_digit_search": affine_digit_search(rows),
        "fixed_prime_residue_search": residue_law_search(rows),
        "bounded_rational_slope_prime_ray_search": prime_ray_search(rows),
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output["summary"], indent=2, sort_keys=True))
    print(json.dumps({
        "affine_groups_tested": output["affine_digit_search"]["groups_tested"],
        "affine_groups_passing": output["affine_digit_search"]["groups_passing"],
        "prime_ray_candidates": output["bounded_rational_slope_prime_ray_search"]["all_zero_candidate_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
