#!/usr/bin/env python3
"""Deterministic certificate for Item 197's common-log reduction.

All theorem statements are proved in the companion report.  This program
replays the finite exact identities and emits path-stable JSON.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item197_common_log_locus_certificate.json"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve(name: str) -> Path:
    # In a work checkout dependencies may sit beside this checker; after
    # archival they all sit in the archive's scripts directory.  The second
    # candidate also supports invoking a copied checker one level below an
    # archive root without embedding any host-specific path.
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


ITEM194_PATH = resolve("item194_rankzero_pnt_certificate.py")
item194 = load("item197_item194", ITEM194_PATH)
deps = item194.dependency_dir()
SECOND_PATH = deps / "item164_third_layer_certificate.py"
EXTENDED_PATH = deps / "lifted_endpoint_hasse_extended_certificate.py"
second = load("item197_second", SECOND_PATH)
extended = load("item197_extended", EXTENDED_PATH)
builder = item194.SecondCartier(second, extended)
pow_poly = item194.pow_poly


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def coefficient_product(left: list[int], right: list[int], index: int, p: int) -> int:
    return sum(
        left[k] * right[index - k]
        for k in range(max(0, index + 1 - len(right)), min(len(left), index + 1))
    ) % p


@lru_cache(maxsize=None)
def fixed_coefficient(j: int, kind: str) -> int:
    exponent_minus = 3 * j + (0 if kind == "u" else 1)
    exponent_plus = 2 * j + (1 if kind == "u" else 2)
    target = 2 * j if kind != "w" else 2 * j - 1
    answer = 0
    for b in range(target // 2 + 1):
        k = target - 2 * b
        answer += (
            (-1) ** k
            * math.comb(exponent_minus, k)
            * (-1) ** b
            * math.comb(exponent_plus + b - 1, b)
        )
    return answer


@lru_cache(maxsize=None)
def moments(p: int, s: int, nu: int) -> tuple[int, int, int]:
    r = (p - 6 * s - 3) // 2
    q = 2 * s - nu
    pnu = second.conv(
        pow_poly([1, -1], r, p, second),
        pow_poly([1, 1], 1 + 3 * nu, p, second),
        p,
    )
    pnu = second.conv(pnu, pow_poly([1, 0, 1], q, p, second), p)
    truncated_minus_log = [0] + [(-pow(k, -1, p)) % p for k in range(1, p)]
    truncated_plus_log = [0] * (2 * p - 1)
    for k in range(1, p):
        truncated_plus_log[2 * k] = ((-1) ** (k - 1) * pow(k, -1, p)) % p
    target = p - q - 1
    return (
        coefficient_product(truncated_minus_log, pnu, target, p),
        coefficient_product(truncated_plus_log, pnu, target, p),
        coefficient_product(truncated_plus_log, pnu, target + p, p),
    )


def quotient_digits(p: int, j: int, s: int) -> tuple[int, int, int]:
    a, c = 3 * j + 1, 2 * j + 1
    u = fixed_coefficient(j, "u") % p
    v = fixed_coefficient(j, "v") % p
    w = fixed_coefficient(j, "w") % p
    values = []
    for nu in (0, 1):
        x, y, y_high = moments(p, s, nu)
        values.append((a * u * x - c * (v * y + w * y_high)) % p)
    x0, y0, h0 = moments(p, s, 0)
    x1, y1, h1 = moments(p, s, 1)
    determinant = (
        v * (x0 * y1 - x1 * y0) + w * (x0 * h1 - x1 * h0)
    ) % p
    return values[0], values[1], determinant


def residue_numerator(m: int, nu: int) -> int:
    index = 4 * m + nu
    extra = 1 + 3 * nu
    denominator_power = 4 * m + 1 + nu
    answer = 0
    for b in range(index // 2 + 1):
        remaining = index - 2 * b
        numerator_coefficient = 0
        for q in range(extra + 1):
            a = remaining - q
            if 0 <= a <= 6 * m:
                numerator_coefficient += (
                    (-1) ** a * math.comb(6 * m, a) * math.comb(extra, q)
                )
        answer += (
            (-1) ** b
            * math.comb(denominator_power + b - 1, b)
            * numerator_coefficient
        )
    return answer


def minus_residue(h: list[int], p: int, j: int) -> int:
    numerator_exponent = 3 * j
    denominator_exponent = 2 * j + 2
    degree = denominator_exponent - 1
    base = second.base_local_coefficients(
        numerator_exponent, denominator_exponent, "minus_one", p
    )
    shifted = second.gaussian_shift(h, (-1 % p, 0), p)
    product = second.multiply_truncated(base, shifted, degree, p)
    return product[degree][0]


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def lcm_upto(n: int) -> int:
    answer = 1
    for k in range(1, n + 1):
        answer = math.lcm(answer, k)
    return answer


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-max", type=int, default=151)
    ap.add_argument("--crosscheck-prime-max", type=int, default=71)
    ap.add_argument("--integer-prime-max", type=int, default=31)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if not (args.integer_prime_max <= args.crosscheck_prime_max <= args.prime_max):
        raise ValueError("require integer <= crosscheck <= prime maximum")

    counts = Counter()
    rows: list[tuple[int, ...]] = []
    diagnostics: list[dict[str, int]] = []
    crosscheck_rows = 0
    integer_rows = 0
    for p, j, s, m in item194.admissible_rows(args.prime_max):
        q0, q1, determinant = quotient_digits(p, j, s)
        log0 = (-q0 * pow(pow(2, 2 * m, p), -1, p)) % p
        log1 = (-q1 * pow(pow(2, 2 * m + 2, p), -1, p)) % p
        counts["rows"] += 1
        counts["log0_zero"] += log0 == 0
        counts["log1_zero"] += log1 == 0
        counts["elimination_determinant_zero"] += determinant == 0
        counts["common_log_zero"] += log0 == log1 == 0
        if determinant == 0:
            diagnostics.append(
                {"p": p, "j": j, "s": s, "m": m, "q0": q0, "q1": q1}
            )
        rows.append((p, j, s, m, q0, q1, determinant))

        if p <= args.crosscheck_prime_max:
            data = builder.build(p, j, s)
            for nu, record in enumerate(data["records"]):
                actual_log = record["C"][1]
                predicted_log = log0 if nu == 0 else log1
                if actual_log != predicted_log:
                    raise AssertionError((p, j, s, nu, actual_log, predicted_log))
                residue = minus_residue(record["H"], p, j)
                if actual_log != 2 * residue % p:
                    raise AssertionError((p, j, s, nu, "global residue collapse"))
            item194.verify_four_section(data, p, j, second)
            crosscheck_rows += 1

        if p <= args.integer_prime_max:
            for nu, qnu in enumerate((q0, q1)):
                coefficient = residue_numerator(m, nu)
                if coefficient % p:
                    raise AssertionError((p, j, s, m, nu, "rank-zero divisibility"))
                if coefficient // p % p != qnu:
                    raise AssertionError((p, j, s, m, nu, "integer bridge"))
            integer_rows += 1

    # Exact counterexample to either full-gcd/K divisibility direction.
    c0_m2, c1_m2 = residue_numerator(2, 0), residue_numerator(2, 1)
    gcd_m2 = math.gcd(c0_m2, c1_m2)
    t_m2 = 5
    k_m2 = lcm_upto(9) // t_m2
    if (gcd_m2, k_m2) != (11, 504):
        raise AssertionError((gcd_m2, k_m2))

    rho = (math.sqrt(33.0) - 3.0) / 6.0
    height = 2 * math.log(1 + rho) - 4 * math.log(1 - rho) - 4 * math.log(rho)
    output = {
        "schema": "item197-common-log-locus-v1",
        "status": {
            "integer_residue_bridge": "PROVED_IN_REPORT",
            "simultaneous_square_divisibility": "PROVED_IN_REPORT",
            "frobenius_defect_projective_form": "PROVED_IN_REPORT",
            "uniform_sublinear_exception_bound": "OPEN",
            "positive_weighted_family": "NOT_PROVED",
            "finite_scan": "EXACT_FINITE_ONLY",
        },
        "definitions": {
            "C_nu": "[z^(4m+nu)](1-z)^(6m)(1+z)^(1+3nu)/(1+z^2)^(4m+1+nu)",
            "common_log_equivalence": "ell_00=ell_10=0 iff p^2 divides C_0(m),C_1(m)",
            "radical_consequence": "R_m^2 divides gcd(C_0(m),C_1(m))",
            "s_map": "K(z)=(1+z^2)^2/(1-z)^3",
            "j_map": "J(y)=(1-y)^3/(y^2(1+y^2)^2)",
            "projective_pair": "q_nu=(3j+1)U_j X_nu-(2j+1)(V_j Y_nu+W_j Y'_nu)",
        },
        "finite_replay": {
            "prime_max": args.prime_max,
            "rows": counts["rows"],
            "log0_zero": counts["log0_zero"],
            "log1_zero": counts["log1_zero"],
            "elimination_determinant_zero": counts["elimination_determinant_zero"],
            "common_log_zero": counts["common_log_zero"],
            "crosscheck_prime_max": args.crosscheck_prime_max,
            "crosscheck_rows": crosscheck_rows,
            "integer_prime_max": args.integer_prime_max,
            "integer_bridge_rows": integer_rows,
            "row_digest": row_digest(rows),
            "determinant_zero_diagnostics": diagnostics,
        },
        "height_and_reservoir": {
            "rho_exact": "(sqrt(33)-3)/6",
            "H_decimal": format(height, ".15f"),
            "radical_rate_ceiling_H_over_12": format(height / 12, ".15f"),
            "raw_cell_mass_per_m": "0.3370475079987658",
            "raw_cell_ceiling_per_6m": "0.05617458466646097",
            "comparison": "H/12 per 6m is weaker than raw_cell_mass_per_m/6",
            "smith_status": "first Smith divisor of log row; not an independent reservoir",
            "K_m_relation": "no universal divisibility in either direction",
            "m2_exact_counterexample": {"gcd_C0_C1": gcd_m2, "K_m": k_m2},
        },
        "dependencies": {
            "item194_rankzero_pnt_certificate.py": sha256(ITEM194_PATH),
            "item164_third_layer_certificate.py": sha256(SECOND_PATH),
            "lifted_endpoint_hasse_extended_certificate.py": sha256(EXTENDED_PATH),
        },
        "runtime": {"external_numeric_backend": None},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "rows": counts["rows"],
        "common_log_zero": counts["common_log_zero"],
        "determinant_zero": counts["elimination_determinant_zero"],
        "row_digest": output["finite_replay"]["row_digest"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
