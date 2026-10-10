#!/usr/bin/env python3
"""Independent exact audit of the sparse four-jet pullback certificate.

Independence choices:

* Schur reduction uses SymPy's QQ_I Gaussian-rational domain, whereas the
  source certificate uses hand-written pairs of fractions.
* G=F(phi) jets are obtained by direct truncated formal composition,
  whereas the source HP probe obtains them by division of G'.
* HP kernels use Matrix.nullspace and Bareiss minors, rather than the
  source probe's DomainMatrix nullspace/determinant path.

Floating-point search records are diagnostics only.  They are recomputed
with a separately written NumPy polynomial builder and never enter the
exact theorem audit.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import QQ, QQ_I


sys.set_int_max_str_digits(0)

BASE = Path("/content/drive/MyDrive/e_pi_research_20260826")
SOURCE_NOTE = BASE / "sources/sparse_multijet_pullback_radius_improvement.md"
CERT_SCRIPT = BASE / "scripts/sparse_multijet_pullback_certificate.py"
CERT_RESULT = BASE / "results/sparse_multijet_pullback_certificate.json"
SEARCH_SCRIPT = BASE / "scripts/sparse_multijet_pullback_search.py"
SEARCH_RESULT = BASE / "results/sparse_multijet_pullback_search.json"
HP_SCRIPT = BASE / "scripts/sparse_multijet_pullback_hp_probe.py"
HP_RESULT = BASE / "results/sparse_multijet_pullback_hp_n15.json"

EXPECTED_HASHES = {
    str(SOURCE_NOTE): "ea37af35ebfb97e0b8a79353eff5d6da4cbe49aebb1bd9ad0a7d6e9d1306163a",
    str(CERT_SCRIPT): "b32190715af12fa82a223a5f8165e75efbf307f1f0bcfa813a8b524e4b1fed0c",
    str(CERT_RESULT): "5b71cb31187d87037524a1932ea422ad3d757e68583ca84eadce9078549169db",
    str(SEARCH_SCRIPT): "946e8e9df6177cdff848ffd668291c20eec8b91b41726373fb655b4b4010241c",
    str(SEARCH_RESULT): "fa7ecd1590f01ce2b1185edea26e9bfd1889dd1168f18b855a89a1badc1568eb",
    str(HP_SCRIPT): "6ab090b23352b42f6c21126afda57cff52e1c5dbf50e719aa3c7407f218946c4",
    str(HP_RESULT): "1b64b42a0caaadd6e7670ec65305698af55e5ac1bf11f34856f42324d67bfedd",
}

SUPPORT = (7, 9, 10, 11)
PARAMETERS = (46, 213, -763, 20078)
RADIUS = Fraction(1747, 1000)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def vector_sha256(values: list[int]) -> str:
    return sha256_bytes(json.dumps(values, separators=(",", ":")).encode())


def fraction_sha256(value: Fraction) -> str:
    return sha256_bytes(f"{value.numerator}/{value.denominator}".encode())


def phi_coefficients(parameters: tuple[int, ...] = PARAMETERS) -> list[Fraction]:
    degree = max(SUPPORT) + 1
    result = [Fraction(0) for _ in range(degree + 1)]
    result[1] = Fraction(1)
    for m, a in zip(SUPPORT, parameters):
        result[m] += Fraction(a, math.factorial(m))
        result[m + 1] -= Fraction(a, math.factorial(m))
    return result


def qqi(real: Fraction, imag: Fraction = Fraction(0)):
    return QQ_I.dtype(
        QQ.convert(sp.Rational(real.numerator, real.denominator)),
        QQ.convert(sp.Rational(imag.numerator, imag.denominator)),
    )


def qconj(value):
    return QQ_I.dtype(value.x, -value.y)


def schur_coefficients(
    parameters: tuple[int, ...], radius: Fraction
) -> list:
    """Leading-to-constant coefficients of w^12(phi(r/w)-(1+i))."""
    phi = phi_coefficients(parameters)
    result = [qqi(Fraction(-1), Fraction(-1))]
    result.extend(qqi(phi[k] * radius**k) for k in range(1, len(phi)))
    assert len(result) == 13 and result[-1]
    return result


def exact_schur(
    parameters: tuple[int, ...], radius: Fraction, keep_records: bool
) -> tuple[bool, list[dict], int | None]:
    """Normalized Schur recursion in SymPy's exact QQ_I domain."""
    coefficients = schur_coefficients(parameters, radius)
    records: list[dict] = []
    while len(coefficients) > 1:
        degree = len(coefficients) - 1
        leading = coefficients[0]
        assert leading
        coefficients = [value / leading for value in coefficients]
        assert coefficients[0] == QQ_I.one
        constant = coefficients[-1]
        norm = constant.x * constant.x + constant.y * constant.y
        gap = QQ.one - norm
        if keep_records:
            gap_fraction = Fraction(int(gap.numerator), int(gap.denominator))
            records.append(
                {
                    "degree": degree,
                    "constant_real": {
                        "numerator": int(constant.x.numerator),
                        "denominator": int(constant.x.denominator),
                    },
                    "constant_imag": {
                        "numerator": int(constant.y.numerator),
                        "denominator": int(constant.y.denominator),
                    },
                    "gap": {
                        "numerator": int(gap.numerator),
                        "denominator": int(gap.denominator),
                        "numerator_digits": len(str(abs(int(gap.numerator)))),
                        "denominator_digits": len(str(int(gap.denominator))),
                        "fraction_sha256": fraction_sha256(gap_fraction),
                        "strictly_positive": gap > 0,
                    },
                }
            )
        if gap <= 0:
            return False, records, degree
        star = [qconj(value) for value in reversed(coefficients)]
        reduced = [
            value - constant * reflected
            for value, reflected in zip(coefficients, star)
        ]
        assert reduced[-1] == QQ_I.zero
        coefficients = reduced[:-1]
        assert coefficients[0] == QQ_I.convert(gap)
    assert coefficients[0]
    return True, records, None


def exact_neighbor_box() -> dict:
    passing: list[list[int]] = []
    failure_counts: dict[str, int] = {}
    for offsets in itertools.product((-1, 0, 1), repeat=4):
        parameters = tuple(a + d for a, d in zip(PARAMETERS, offsets))
        passed, _, failed = exact_schur(parameters, RADIUS, False)
        if passed:
            passing.append(list(parameters))
        else:
            assert failed is not None
            key = str(failed)
            failure_counts[key] = failure_counts.get(key, 0) + 1
    return {
        "number_tested": 81,
        "passing_parameters": passing,
        "failure_degree_counts": failure_counts,
    }


def convolution_truncated(
    left: list[Fraction], right: list[Fraction], maximum: int
) -> list[Fraction]:
    result = [Fraction(0) for _ in range(maximum + 1)]
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right):
            if i + j > maximum:
                break
            if y:
                result[i + j] += x * y
    return result


def base_F_coefficients(maximum: int) -> list[Fraction]:
    """Ordinary coefficients of F from (w^2-2w+2)F'=4."""
    derivative: list[Fraction] = []
    for n in range(maximum):
        previous = derivative[n - 1] if n >= 1 else Fraction(0)
        previous2 = derivative[n - 2] if n >= 2 else Fraction(0)
        rhs = Fraction(4) if n == 0 else Fraction(0)
        derivative.append((rhs + 2 * previous - previous2) / 2)
    result = [Fraction(0)]
    result.extend(derivative[n] / (n + 1) for n in range(maximum))
    return result[: maximum + 1]


def composed_jets(maximum: int) -> list[int]:
    """Directly compose ordinary series F(phi), then convert to jets."""
    phi = phi_coefficients()
    phi.extend([Fraction(0)] * (maximum + 1 - len(phi)))
    phi = phi[: maximum + 1]
    base = base_F_coefficients(maximum)
    result = [Fraction(0) for _ in range(maximum + 1)]
    power = [Fraction(0) for _ in range(maximum + 1)]
    power[0] = Fraction(1)
    for k in range(1, maximum + 1):
        power = convolution_truncated(power, phi, maximum)
        if base[k]:
            for j, value in enumerate(power):
                result[j] += base[k] * value
    jets: list[int] = []
    for k, coefficient in enumerate(result):
        jet = coefficient * math.factorial(k)
        assert jet.denominator == 1
        jets.append(jet.numerator)
    return jets


def falling(k: int, j: int) -> int:
    return 0 if j > k else math.factorial(k) // math.factorial(k - j)


def primitive_rational_vector(values) -> list[int]:
    fractions = [
        Fraction(int(value.p), int(value.q))
        if isinstance(value, sp.Rational)
        else Fraction(value)
        for value in values
    ]
    denominator = reduce(math.lcm, (x.denominator for x in fractions), 1)
    integers = [x.numerator * (denominator // x.denominator) for x in fractions]
    common = reduce(gcd, (abs(x) for x in integers if x))
    integers = [x // common for x in integers]
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def hp_rows(n: int, jets: list[int]) -> list[list[int]]:
    rows = []
    for k in range(n + 1, 3 * n + 1):
        row = [falling(k, j) for j in range(n + 1)]
        row.extend(
            falling(k, j) * jets[k - j] if j <= k else 0
            for j in range(n + 1)
        )
        rows.append(row)
    rows.append([-1] * (n + 1) + [1] * (n + 1))
    return rows


def reconstruct_triple(n: int, kernel: list[int], jets: list[int]) -> list[int]:
    b = kernel[: n + 1]
    c = kernel[n + 1 :]
    a: list[Fraction] = []
    for k in range(n + 1):
        derivative = 0
        for j in range(k + 1):
            derivative += falling(k, j) * (b[j] + c[j] * jets[k - j])
        a.append(Fraction(-derivative, math.factorial(k)))
    return primitive_rational_vector(a + b + c)


def first_free(n: int, triple: list[int], jets: list[int]) -> Fraction:
    b = triple[n + 1 : 2 * (n + 1)]
    c = triple[2 * (n + 1) :]
    k = 3 * n + 1
    return sum(
        (
            Fraction(b[j] + c[j] * jets[k - j], math.factorial(k - j))
            for j in range(n + 1)
        ),
        Fraction(0),
    )


def e_interval(last: int = 900) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction(1, math.factorial(k)) for k in range(last + 1)),
        Fraction(0),
    )
    return partial, partial + Fraction(1, last * math.factorial(last))


def atan_interval(inv: int, last: int) -> tuple[Fraction, Fraction]:
    partial = sum(
        (
            (-1 if k & 1 else 1)
            * Fraction(1, (2 * k + 1) * inv ** (2 * k + 1))
            for k in range(last + 1)
        ),
        Fraction(0),
    )
    omitted = Fraction(1, (2 * last + 3) * inv ** (2 * last + 3))
    return (
        (partial, partial + omitted)
        if last & 1
        else (partial - omitted, partial)
    )


def s_interval() -> tuple[Fraction, Fraction]:
    elo, ehi = e_interval()
    a5lo, a5hi = atan_interval(5, 1200)
    a239lo, a239hi = atan_interval(239, 320)
    return elo + 16 * a5lo - 4 * a239hi, ehi + 16 * a5hi - 4 * a239lo


def floor_log10(value: Fraction) -> int:
    assert value > 0
    guess = len(str(value.numerator)) - len(str(value.denominator))
    power = Fraction(10**guess) if guess >= 0 else Fraction(1, 10 ** (-guess))
    while value < power:
        guess -= 1
        power /= 10
    while value >= 10 * power:
        guess += 1
        power *= 10
    return guess


def endpoint_certificate(
    alpha: int, beta: int, interval: tuple[Fraction, Fraction]
) -> dict:
    lo, hi = sorted(
        (Fraction(alpha) + beta * interval[0], Fraction(alpha) + beta * interval[1])
    )
    if lo > 0:
        abs_lo, abs_hi, sign = lo, hi, 1
    elif hi < 0:
        abs_lo, abs_hi, sign = -hi, -lo, -1
    else:
        return {"contains_zero": True, "sign": 0, "decade": None}
    dlo, dhi = floor_log10(abs_lo), floor_log10(abs_hi)
    assert dlo == dhi
    return {
        "contains_zero": False,
        "sign": sign,
        "decade": dlo,
        "lower_fraction_sha256": fraction_sha256(abs_lo),
        "upper_fraction_sha256": fraction_sha256(abs_hi),
    }


def independent_hp(max_n: int, jets: list[int], archived: dict) -> list[dict]:
    interval = s_interval()
    archived_by_n = {item["n"]: item for item in archived["records"]}
    records: list[dict] = []
    for n in range(1, max_n + 1):
        rows = hp_rows(n, jets)
        matrix = sp.Matrix(rows)
        nullspace = matrix.nullspace(simplify=False)
        assert len(nullspace) == 1
        kernel = primitive_rational_vector(list(nullspace[0]))

        # Use the last nonzero coordinate; the source probe uses the first.
        index = max(j for j, value in enumerate(kernel) if value)
        minor = matrix[:, :index].row_join(matrix[:, index + 1 :])
        determinant = int(minor.det(method="bareiss"))
        signed = determinant if index % 2 == 0 else -determinant
        assert signed and signed % kernel[index] == 0
        content = abs(signed // kernel[index])

        triple = reconstruct_triple(n, kernel, jets)
        a = triple[: n + 1]
        b = triple[n + 1 : 2 * (n + 1)]
        c = triple[2 * (n + 1) :]
        assert sum(b) == sum(c)
        raw = [sum(a), sum(b)]
        endpoint_gcd = gcd(abs(raw[0]), abs(raw[1]))
        reduced = (
            [raw[0] // endpoint_gcd, raw[1] // endpoint_gcd]
            if endpoint_gcd
            else [0, 0]
        )
        free = first_free(n, triple, jets)
        endpoint = endpoint_certificate(reduced[0], reduced[1], interval)

        record = {
            "n": n,
            "shape": [len(rows), len(rows[0])],
            "rank": len(rows),
            "nullity": 1,
            "matrix_sha256": vector_sha256([x for row in rows for x in row]),
            "primitive_high_kernel_sha256": vector_sha256(kernel),
            "cofactor_content": content,
            "cofactor_content_digits": len(str(content)),
            "primitive_triple_sha256": vector_sha256(triple),
            "primitive_triple_height_digits": len(str(max(map(abs, triple)))),
            "raw_endpoint_pair": raw,
            "endpoint_gcd": endpoint_gcd,
            "reduced_endpoint_pair": reduced,
            "first_free": {
                "index": 3 * n + 1,
                "numerator": free.numerator,
                "denominator": free.denominator,
                "nonzero": bool(free),
            },
            "independent_endpoint_certificate": endpoint,
        }
        expected = archived_by_n[n]
        comparisons = {
            "shape": record["shape"] == expected["shape"],
            "rank": record["rank"] == expected["rank"],
            "nullity": record["nullity"] == expected["nullity"],
            "kernel_hash": (
                record["primitive_high_kernel_sha256"]
                == expected["primitive_high_kernel_sha256"]
            ),
            "cofactor_content_digits": (
                record["cofactor_content_digits"]
                == expected["maximal_cofactor_common_content_digits"]
            ),
            "triple_hash": (
                record["primitive_triple_sha256"]
                == expected["primitive_triple_sha256"]
            ),
            "triple_height_digits": (
                record["primitive_triple_height_digits"]
                == expected["primitive_triple_height_digits"]
            ),
            "raw_endpoint_pair": raw == expected["raw_endpoint_pair"],
            "endpoint_gcd": endpoint_gcd == expected["endpoint_gcd"],
            "reduced_endpoint_pair": reduced == expected["reduced_endpoint_pair"],
            "first_free": record["first_free"] == expected["first_free"],
            "endpoint_sign": (
                endpoint["sign"]
                == expected["endpoint_interval_certificate"]["certified_sign"]
            ),
            "endpoint_contains_zero": (
                endpoint["contains_zero"]
                == expected["endpoint_interval_certificate"]["interval_contains_zero"]
            ),
            "endpoint_decade": (
                endpoint["decade"]
                == expected["endpoint_interval_certificate"].get(
                    "single_certified_base10_decade"
                )
            ),
        }
        assert all(comparisons.values())
        record["archived_record_comparisons"] = comparisons
        records.append(record)
    return records


def numeric_radius(support: tuple[int, ...], parameters: tuple[int, ...]) -> float:
    degree = max(support) + 1
    ascending = np.zeros(degree + 1, dtype=np.complex128)
    ascending[0] = -(1 + 1j)
    ascending[1] = 1
    for m, a in zip(support, parameters):
        value = a / math.factorial(m)
        ascending[m] += value
        ascending[m + 1] -= value
    roots = np.polynomial.polynomial.polyroots(ascending)
    return float(np.min(np.abs(roots)))


def audit_search(archived: dict) -> dict:
    one_term_differences = []
    for item in archived["one_term_records"]:
        m = item["m"]
        a = item["nearby_integer_a"]
        value = numeric_radius((m,), (a,))
        one_term_differences.append(
            abs(value - item["nearby_integer_radius_diagnostic"])
        )
    best = max(
        archived["one_term_records"],
        key=lambda item: item["nearby_integer_radius_diagnostic"],
    )

    catalog_differences = []
    for item in archived["selected_multijet_candidate_catalog"]:
        value = numeric_radius(tuple(item["support"]), tuple(item["parameters"]))
        catalog_differences.append(abs(value - item["radius_diagnostic"]))

    box = archived["final_candidate_local_integer_box"]
    best_parameters = None
    best_radius = -1.0
    tested = 0
    for a9 in range(box["a9_range_inclusive"][0], box["a9_range_inclusive"][1] + 1):
        for a10 in range(
            box["a10_range_inclusive"][0], box["a10_range_inclusive"][1] + 1
        ):
            for a11 in range(
                box["a11_range_inclusive"][0], box["a11_range_inclusive"][1] + 1
            ):
                parameters = (box["fixed_a7"], a9, a10, a11)
                value = numeric_radius(SUPPORT, parameters)
                tested += 1
                if value > best_radius:
                    best_radius = value
                    best_parameters = parameters
    assert tested == 2197
    assert list(best_parameters) == box["best_record"]["parameters"]
    assert max(one_term_differences) < 2e-11
    assert max(catalog_differences) < 2e-11
    return {
        "diagnostic_only": True,
        "one_term_records_recomputed": len(one_term_differences),
        "maximum_one_term_radius_difference": max(one_term_differences),
        "archived_best_one_term_m_a": [best["m"], best["nearby_integer_a"]],
        "catalog_records_recomputed": len(catalog_differences),
        "maximum_catalog_radius_difference": max(catalog_differences),
        "local_box_records_recomputed": tested,
        "independent_local_box_best_parameters": list(best_parameters),
        "independent_local_box_best_radius": best_radius,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=15)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    actual_hashes = {path: file_sha256(Path(path)) for path in EXPECTED_HASHES}
    assert actual_hashes == EXPECTED_HASHES
    archived_certificate = json.loads(CERT_RESULT.read_text())
    archived_search = json.loads(SEARCH_RESULT.read_text())
    archived_hp = json.loads(HP_RESULT.read_text())

    phi = phi_coefficients()
    derivative_jets = [
        (phi[k] * math.factorial(k)).numerator for k in range(1, len(phi))
    ]
    assert all(
        (phi[k] * math.factorial(k)).denominator == 1
        for k in range(1, len(phi))
    )
    assert phi[0] == 0 and sum(phi) == 1
    assert derivative_jets == archived_certificate[
        "phi_derivative_jets_1_through_12"
    ]

    passed, schur_records, failed = exact_schur(PARAMETERS, RADIUS, True)
    assert passed and failed is None
    assert [x["degree"] for x in schur_records] == list(range(12, 0, -1))
    archived_schur = archived_certificate["normalized_schur_cohn_records"]
    schur_comparisons = []
    for independent, expected in zip(schur_records, archived_schur):
        comparison = {
            "degree": independent["degree"] == expected["degree"],
            "constant_real": independent["constant_real"]
            == expected["normalized_constant"]["real"],
            "constant_imag": independent["constant_imag"]
            == expected["normalized_constant"]["imag"],
            "gap_numerator": independent["gap"]["numerator"]
            == expected["one_minus_constant_modulus_squared"]["numerator"],
            "gap_denominator": independent["gap"]["denominator"]
            == expected["one_minus_constant_modulus_squared"]["denominator"],
            "positive": independent["gap"]["strictly_positive"]
            == expected["gap_is_strictly_positive"],
        }
        assert all(comparison.values())
        schur_comparisons.append(comparison)

    neighbor = exact_neighbor_box()
    archived_neighbor = archived_certificate["exact_neighboring_lattice_classification"]
    assert neighbor["number_tested"] == archived_neighbor["number_tested"]
    assert neighbor["passing_parameters"] == [
        item["parameters"] for item in archived_neighbor["passing_records"]
    ]
    assert neighbor["failure_degree_counts"] == archived_neighbor[
        "first_nonpositive_schur_gap_degree_counts"
    ]

    jets = composed_jets(3 * args.max_n + 1)
    jet_hash = vector_sha256(jets)
    assert jet_hash == archived_hp["computed_G_jet_sha256"]
    hp_records = independent_hp(args.max_n, jets, archived_hp)

    z = sp.symbols("z")
    phi_expression = sum(
        sp.Rational(x.numerator, x.denominator) * z**k
        for k, x in enumerate(phi)
    )
    roots = sp.nroots(phi_expression - (1 + sp.I), n=75, maxsteps=1000)
    smallest_root = min(roots, key=lambda root: sp.Abs(root))

    result = {
        "audit_script_sha256": file_sha256(Path(__file__)),
        "audit_snapshot_sha256": actual_hashes,
        "python_version": sys.version,
        "sympy_version": sp.__version__,
        "numpy_version": np.__version__,
        "phi": {
            "at_zero": [phi[0].numerator, phi[0].denominator],
            "at_one": [sum(phi).numerator, sum(phi).denominator],
            "ordinary_coefficients_low_to_high": [
                [x.numerator, x.denominator] for x in phi
            ],
            "derivative_jets_1_through_12": derivative_jets,
            "endpoint_and_jet_records_match": True,
        },
        "schur": {
            "radius": [RADIUS.numerator, RADIUS.denominator],
            "all_gaps_strictly_positive": passed,
            "records": schur_records,
            "all_exact_records_match_archived_certificate": all(
                all(item.values()) for item in schur_comparisons
            ),
            "neighbor_box": neighbor,
            "neighbor_box_matches_archived_certificate": True,
        },
        "high_precision_root_diagnostic": {
            "real": str(sp.re(smallest_root).evalf(65)),
            "imag": str(sp.im(smallest_root).evalf(65)),
            "modulus": str(sp.Abs(smallest_root).evalf(70)),
            "diagnostic_only": True,
        },
        "formal_composition_jets": {
            "computed_through_order": len(jets) - 1,
            "all_integral": True,
            "sha256": jet_hash,
            "matches_archived_independent_derivative_division": True,
        },
        "hp": {
            "max_n": args.max_n,
            "records": hp_records,
            "all_records_match_archived_probe": True,
            "endpoint_decades": [
                item["independent_endpoint_certificate"]["decade"]
                for item in hp_records
            ],
        },
        "search_diagnostics": audit_search(archived_search),
        "conclusion": (
            "The exact endpoint, derivative jets, 12 Schur gaps, 3^4 "
            "neighbor classification, composed G jets, and all HP records "
            "through n=15 independently match the frozen artifacts. "
            "The search orderings and roots remain diagnostics."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
