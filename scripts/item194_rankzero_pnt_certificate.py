#!/usr/bin/env python3
"""Exact finite replay for the PNT-side kappa=2 rank-zero gate.

The companion report proves the all-prime regular-branch exclusion.  This
script reconstructs every second-Cartier differential in a finite range,
checks the four-section/evaluation and endpoint-kernel identities, and then
uses the independent p-adic Hasse recurrence for a smaller full-digit scan.
All arithmetic is exact Python integer or finite-field arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ARCHIVE = Path(__file__).resolve().parents[1]
RESULT_NAME = "item194_rankzero_pnt_certificate.json"


def load(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def dependency_dir() -> Path:
    names = (
        "item163_deeper_digits_certificate.py",
        "item164_third_layer_certificate.py",
        "lifted_endpoint_hasse_extended_certificate.py",
        "lifted_endpoint_hasse_certificate.py",
    )
    if all((HERE / name).exists() for name in names):
        return HERE
    candidate = ARCHIVE / "scripts"
    if all((candidate / name).exists() for name in names):
        return candidate
    raise FileNotFoundError("cannot resolve Item163/164 Hasse dependencies")


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p in range(7, limit + 1) if sieve[p]]


def pow_poly(poly: list[int], exponent: int, p: int, second: Any) -> list[int]:
    out = [1]
    base = poly[:]
    while exponent:
        if exponent & 1:
            out = second.conv(out, base, p)
        exponent >>= 1
        if exponent:
            base = second.conv(base, base, p)
    return out


def pad(poly: list[int], length: int = 5) -> list[int]:
    if len(poly) > length:
        raise AssertionError((poly, length))
    return poly + [0] * (length - len(poly))


def rank_mod(rows: list[list[int]], p: int) -> int:
    matrix = [[value % p for value in row] for row in rows]
    rank = 0
    columns = len(matrix[0]) if matrix else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, p)
        matrix[rank] = [(inverse * value) % p for value in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank and matrix[i][column]:
                multiple = matrix[i][column]
                matrix[i] = [
                    (left - multiple * right) % p
                    for left, right in zip(matrix[i], matrix[rank])
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def gmul(left: tuple[int, int], right: tuple[int, int], p: int) -> tuple[int, int]:
    a, b = left
    c, d = right
    return ((a * c - b * d) % p, (a * d + b * c) % p)


def gpow(value: tuple[int, int], exponent: int, p: int) -> tuple[int, int]:
    out = (1, 0)
    base = value
    while exponent:
        if exponent & 1:
            out = gmul(out, base, p)
        exponent >>= 1
        if exponent:
            base = gmul(base, base, p)
    return out


def admissible_rows(prime_max: int, j_max: int | None = None):
    for p in primes_upto(prime_max):
        top_j = (p - 2) // 3
        if j_max is not None:
            top_j = min(top_j, j_max)
        for j in range(1, top_j + 1):
            for s in range(1, (p - 3) // 6 + 1):
                numerator = (2 * j + 1) * p - 2 * s - 1
                if numerator % 4:
                    continue
                yield p, j, s, numerator // 4


class SecondCartier:
    def __init__(self, second: Any, extended: Any):
        self.second = second
        self.extended = extended

    def coordinates(self, h: list[int], p: int, j: int) -> tuple[int, int, int]:
        numerator_exponent = 3 * j
        denominator_exponent = 2 * j + 2
        degree = denominator_exponent - 1
        minus_base = self.second.base_local_coefficients(
            numerator_exponent, denominator_exponent, "minus_one", p
        )
        i_base = self.second.base_local_coefficients(
            numerator_exponent, denominator_exponent, "i", p
        )
        minus_h = self.second.gaussian_shift(h, (-1 % p, 0), p)
        i_h = self.second.gaussian_shift(h, (0, 1), p)
        c_minus = self.second.multiply_truncated(minus_base, minus_h, degree, p)
        c_i = self.second.multiply_truncated(i_base, i_h, degree, p)
        residue_minus = c_minus[degree][0]
        residue_i = c_i[degree]
        l_value = (4 * residue_minus + 4 * residue_i[0]) % p
        e_value = (-4 * residue_i[1]) % p
        roots_and_coefficients = [
            ((-1 % p, 0), c_minus),
            ((0, 1), c_i),
            ((0, -1 % p), [(x, -y % p) for x, y in c_i]),
        ]
        total = (0, 0)
        for n in range(1, denominator_exponent):
            contribution = (0, 0)
            for root, coefficients in roots_and_coefficients:
                term = self.extended.base.gmul(
                    coefficients[degree - n],
                    self.extended.base.endpoint_factor(root, n, p),
                    p,
                )
                contribution = self.extended.base.gadd(contribution, term, p)
            contribution = self.extended.base.gscale(contribution, pow(n, -1, p), p)
            total = self.extended.base.gadd(total, contribution, p)
        if total[1]:
            raise AssertionError((p, j, total))
        return total[0], l_value, e_value

    def build(self, p: int, j: int, s: int) -> dict[str, Any]:
        r = (p - 6 * s - 3) // 2
        a = 3 * j + 1
        c = 2 * j + 1
        u = [0, 1, -1]
        q = [1, 1, 1, 1]
        up = pow_poly(u, r, p, self.second)
        d = [a, -(5 * j + 2), -(5 * j + 2), -(5 * j + 2), 1]
        records = []
        for nu in (0, 1):
            p_poly = self.second.conv(up, pow_poly(q, 2 * s - nu, p, self.second), p)
            t_poly = self.second.primitive(p_poly, p)
            n_poly = self.second.conv(t_poly, d, p)
            h = [0] * 5
            for n in range(5):
                h[n] = sum(
                    n_poly[index]
                    for z in range(p)
                    if 0 <= (index := p * n - 4 * z) < len(n_poly)
                ) % p
            h = self.second.trim(h)
            if h[0] or len(h) > 5:
                raise AssertionError((p, j, s, nu, h))
            coords = self.coordinates(h, p, j)
            records.append({"P": p_poly, "T": t_poly, "N": n_poly, "H": h, "C": coords})

        r0, l0, e0 = records[0]["C"]
        r1, l1, e1 = records[1]["C"]
        return {
            "r": r,
            "D": d,
            "records": records,
            "A0_raw": (l1 * r0 - l0 * r1) % p,
            "B0_raw": (l1 * e0 - l0 * e1) % p,
        }


def verify_four_section(data: dict[str, Any], p: int, j: int, second: Any) -> None:
    roots = ((1, 0), (-1 % p, 0), (0, 1), (0, -1 % p))
    generator = [0, 3 * j + 2, -(5 * j + 2), -(5 * j + 2), -(5 * j + 2)]
    for root in roots:
        root_p = gpow(root, p, p)
        d_at_root = second.gaussian_poly_eval(data["D"], root, p)
        if d_at_root == (0, 0):
            raise AssertionError((p, j, root, "D vanishes"))
        g_at_root_p = second.gaussian_poly_eval(generator, root_p, p)
        if g_at_root_p != gmul(root_p, d_at_root, p):
            raise AssertionError((p, j, root, "G/D identity"))
        for record in data["records"]:
            n_value = second.gaussian_poly_eval(record["N"], root, p)
            h_value = second.gaussian_poly_eval(record["H"], root_p, p)
            if n_value != h_value:
                raise AssertionError((p, j, root, "four section"))


def full_digits(item163: Any, extended: Any, m: int, p: int) -> dict[str, Any]:
    precision = 4
    modulus = p**precision
    l0, x0, e0, _ = item163.coordinates_mod(extended, m, 4 * m + 1, p, precision)
    l1, x1, e1, _ = item163.coordinates_mod(extended, m, 4 * m + 2, p, precision)
    da = (l1 * x0 - l0 * x1) % modulus
    db = (l1 * e0 - l0 * e1) % modulus
    if da % (p * p) or db % (p * p):
        raise AssertionError((m, p, "rank-zero normalization"))
    a0 = da // (p * p) % p
    a1 = da // (p**3) % p
    b0 = db // (p * p) % p

    ell0, ell1 = l0 // p, l1 // p
    rho0, rho1 = x0 // p, x1 // p
    eps0, eps1 = e0 // p, e1 // p
    e00, e01 = ell0 % p, ell0 // p % p
    e10, e11 = ell1 % p, ell1 // p % p
    r00, r01 = rho0 % p, rho0 // p % p
    r10, r11 = rho1 % p, rho1 // p % p
    s0 = e10 * r00 - e00 * r10
    canonical_a0 = s0 % p
    carry0 = (s0 - canonical_a0) // p
    s1 = e10 * r01 + e11 * r00 - e00 * r11 - e01 * r10
    carry_a1 = (s1 + carry0) % p
    if (canonical_a0, carry_a1) != (a0, a1):
        raise AssertionError((m, p, "carry", (canonical_a0, carry_a1), (a0, a1)))
    carry_b0 = (e10 * (eps0 % p) - e00 * (eps1 % p)) % p
    if carry_b0 != b0:
        raise AssertionError((m, p, "B carry", carry_b0, b0))
    return {"A0": a0, "A1": a1, "B0": b0}


def digest_rows(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--first-prime-max", type=int, default=151)
    ap.add_argument("--full-prime-max", type=int, default=101)
    ap.add_argument("--full-j-max", type=int, default=6)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if args.full_prime_max > args.first_prime_max:
        raise ValueError("full scan must be contained in first scan")

    deps = dependency_dir()
    paths = {
        "scripts/item163_deeper_digits_certificate.py": deps / "item163_deeper_digits_certificate.py",
        "scripts/item164_third_layer_certificate.py": deps / "item164_third_layer_certificate.py",
        "scripts/lifted_endpoint_hasse_extended_certificate.py": deps / "lifted_endpoint_hasse_extended_certificate.py",
        "scripts/lifted_endpoint_hasse_certificate.py": deps / "lifted_endpoint_hasse_certificate.py",
    }
    item163 = load("item194_item163", paths["scripts/item163_deeper_digits_certificate.py"])
    second = load("item194_item164", paths["scripts/item164_third_layer_certificate.py"])
    extended = load("item194_extended", paths["scripts/lifted_endpoint_hasse_extended_certificate.py"])
    builder = SecondCartier(second, extended)

    first_rows: list[tuple[int, ...]] = []
    first_counts = Counter()
    prime_counts: dict[int, Counter] = defaultdict(Counter)
    diagnostic_rows: list[dict[str, int]] = []
    cached: dict[tuple[int, int, int], dict[str, Any]] = {}
    checked_pj: set[tuple[int, int]] = set()

    for p, j, s, m in admissible_rows(args.first_prime_max):
        data = builder.build(p, j, s)
        if p <= args.full_prime_max and j <= args.full_j_max:
            cached[(p, j, s)] = data
        r = data["r"]
        if 2 * r + 6 * s + 3 != p:
            raise AssertionError((p, j, s, "r identity"))
        if len(data["records"][0]["P"]) - 1 != p - 3:
            raise AssertionError((p, j, s, "P0 degree"))
        if len(data["records"][1]["P"]) - 1 != p - 6:
            raise AssertionError((p, j, s, "P1 degree"))
        verify_four_section(data, p, j, second)

        generator = [0, 3 * j + 2, -(5 * j + 2), -(5 * j + 2), -(5 * j + 2)]
        if builder.coordinates(generator, p, j) != (0, 0, 0):
            raise AssertionError((p, j, "kernel generator"))
        if (p, j) not in checked_pj:
            basis_coordinates = [builder.coordinates([0] * n + [1], p, j) for n in range(1, 5)]
            if rank_mod([list(row) for row in basis_coordinates], p) != 3:
                raise AssertionError((p, j, "endpoint rank"))
            checked_pj.add((p, j))

        h0 = pad(data["records"][0]["H"])[1:]
        h1 = pad(data["records"][1]["H"])[1:]
        regular_rank = rank_mod([h0, h1, generator[1:]], p) <= 2
        if regular_rank:
            raise AssertionError((p, j, s, "contradicts regular-branch theorem"))
        c0 = data["records"][0]["C"]
        c1 = data["records"][1]["C"]
        both_log_zero = c0[1] == c1[1] == 0
        simultaneous = data["A0_raw"] == data["B0_raw"] == 0
        if simultaneous != (both_log_zero or regular_rank):
            raise AssertionError((p, j, s, "gate union"))

        # Coefficients used by the uniform elimination in the report.
        R = r + 1
        if (2 * R + 1 - 2 * s) != p - 8 * s:
            raise AssertionError((p, j, s, "lambda equation"))
        if 2 * R + 6 * s != p - 1:
            raise AssertionError((p, j, s, "mu equation"))

        first_counts["rows"] += 1
        first_counts["A0_zero"] += data["A0_raw"] == 0
        first_counts["B0_zero"] += data["B0_raw"] == 0
        first_counts["both_log_zero"] += both_log_zero
        first_counts["simultaneous"] += simultaneous
        prime_counts[p]["rows"] += 1
        prime_counts[p]["A0_zero"] += data["A0_raw"] == 0
        prime_counts[p]["B0_zero"] += data["B0_raw"] == 0
        prime_counts[p]["both_log_zero"] += both_log_zero
        if data["A0_raw"] == 0 or data["B0_raw"] == 0 or both_log_zero:
            diagnostic_rows.append(
                {
                    "p": p, "j": j, "s": s, "m": m,
                    "A0_raw": data["A0_raw"], "B0_raw": data["B0_raw"],
                    "L0": c0[1], "L1": c1[1],
                }
            )
        first_rows.append(
            (p, j, s, m, data["A0_raw"], data["B0_raw"], c0[1], c1[1])
        )

    full_rows: list[tuple[int, ...]] = []
    full_counts = Counter()
    full_diagnostics: list[dict[str, int]] = []
    for p, j, s, m in admissible_rows(args.full_prime_max, args.full_j_max):
        data = cached[(p, j, s)]
        digits = full_digits(item163, extended, m, p)
        chi = 1 if p % 4 == 1 else -1
        if digits["A0"] != data["A0_raw"]:
            raise AssertionError((p, j, s, "A0 second/full mismatch"))
        if digits["B0"] != chi * data["B0_raw"] % p:
            raise AssertionError((p, j, s, "B0 second/full mismatch"))
        full_counts["rows"] += 1
        full_counts["A0_zero"] += digits["A0"] == 0
        full_counts["A1_zero"] += digits["A1"] == 0
        full_counts["B0_zero"] += digits["B0"] == 0
        full_counts["A0_A1_zero"] += digits["A0"] == digits["A1"] == 0
        full_counts["cubic"] += digits["A0"] == digits["A1"] == digits["B0"] == 0
        if 0 in digits.values():
            full_diagnostics.append({"p": p, "j": j, "s": s, "m": m, **digits})
        full_rows.append((p, j, s, m, digits["A0"], digits["A1"], digits["B0"]))

    output = {
        "schema": "item194-rankzero-pnt-gate-v1",
        "status": {
            "rational_map_and_four_section": "PROVED_IN_REPORT",
            "regular_simultaneous_gate_exclusion": "PROVED_IN_REPORT",
            "exceptional_common_log_locus": "OPEN",
            "positive_weighted_cubic_family": "NOT_PROVED",
            "finite_replays": "EXACT_FINITE_ONLY",
        },
        "scope": {
            "cell": "kappa=2 rank zero, 4m+1=(2j+1)p-2s",
            "PNT_side": "3j+1<p; the p<=sqrt(6m) exact tail is excluded",
            "first_gate_prime_max": args.first_prime_max,
            "first_gate_j_scope": "all admissible j",
            "full_digit_prime_max": args.full_prime_max,
            "full_digit_j_max": args.full_j_max,
        },
        "definitions": {
            "r": "(p-6s-3)/2",
            "P_nu": "u^r Q^(2s-nu)",
            "rational_map": "P_nu=u^((p-3)/2)*(Q^2/u^3)^s*Q^(-nu)",
            "D_j": "(3j+1)-(5j+2)(x+x^2+x^3)+x^4",
            "G_j": "uQ+xD_j=(3j+2)x-(5j+2)(x^2+x^3+x^4)",
            "regular_gate_equivalent_rank": "rank(H0,H1,G_j)<=2 iff rank((T0(zeta),T1(zeta),zeta^p) over zeta^4=1)<=2",
            "all_simultaneous_gate_locus": "(L0=L1=0) union (regular rank locus)",
            "A1": "second canonical digit of the normalized A determinant, including carry",
        },
        "symbolic_elimination": {
            "divisor_degree": "deg(u^(r+1)Q^(2s))=p-1",
            "quotient": "lambda*x+mu",
            "x_vs_x2_equation": "(p-8s)*lambda=0 mod p, hence lambda=0",
            "x4_equation_after_lambda_zero": "-(p-1)*mu=0 mod p, hence mu=0",
            "conclusion": "the regular rank locus is empty for every admissible PNT-side cell",
        },
        "dependencies": {key: sha256(path) for key, path in paths.items()},
        "runtime": {
            "python": sys.version.split()[0],
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "external_numeric_backend": None,
        },
        "first_gate_replay": {
            "row_count": first_counts["rows"],
            "parameter_pair_count": len(checked_pj),
            "A0_zero_count": first_counts["A0_zero"],
            "B0_zero_count": first_counts["B0_zero"],
            "both_log_zero_count": first_counts["both_log_zero"],
            "simultaneous_A0_B0_zero_count": first_counts["simultaneous"],
            "regular_rank_locus_count": 0,
            "row_digest": digest_rows(first_rows),
            "per_prime": {str(p): dict(sorted(counts.items())) for p, counts in sorted(prime_counts.items())},
            "single_gate_diagnostic_rows": diagnostic_rows,
        },
        "full_digit_replay": {
            "row_count": full_counts["rows"],
            "A0_zero_count": full_counts["A0_zero"],
            "A1_zero_count": full_counts["A1_zero"],
            "B0_zero_count": full_counts["B0_zero"],
            "A0_A1_zero_count": full_counts["A0_A1_zero"],
            "cubic_gate_count": full_counts["cubic"],
            "row_digest": digest_rows(full_rows),
            "zero_digit_diagnostic_rows": full_diagnostics,
        },
        "capacity": {
            "raw_rankzero_PNT_mass_per_m": "C0=-4log(2)+pi/sqrt(3)+3log(3)-2",
            "proved_cubic_support": "contained in the exceptional common-log locus L0=L1=0",
            "common_log_weight_bound": "OPEN",
            "new_content_exponent": "NONE",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    first_summary_keys = (
        "row_count", "parameter_pair_count", "A0_zero_count", "B0_zero_count",
        "both_log_zero_count", "simultaneous_A0_B0_zero_count",
        "regular_rank_locus_count", "row_digest",
    )
    full_summary_keys = (
        "row_count", "A0_zero_count", "A1_zero_count", "B0_zero_count",
        "A0_A1_zero_count", "cubic_gate_count", "row_digest",
    )
    print(json.dumps({
        "first_gate": {key: output["first_gate_replay"][key] for key in first_summary_keys},
        "full_digit": {key: output["full_digit_replay"][key] for key in full_summary_keys},
    }, sort_keys=True))


if __name__ == "__main__":
    main()
