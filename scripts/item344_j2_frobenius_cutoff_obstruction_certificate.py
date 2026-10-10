#!/usr/bin/env python3
"""Deterministic certificate for Item 344.

The checker verifies the exact half-binomial recurrence, the tied-prime
Frobenius coefficient formula, the all-mode additive completion
mechanism, the maximal-degree finite-field cutoff, and the fixed-M
parameter identities.  Finite rows validate formulas only; the global
method-class and weighted-edge proofs are in the companion report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULT_NAME = "item344_j2_frobenius_cutoff_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item341_j2_diagonal_affine_state_report.md":
        "42f6ccd326e385f8034abe322756517a30a93d7468b3e6f85cbca3dba8080cb4",
    "results/item341_j2_diagonal_affine_state_certificate.json":
        "75c05cb486e5a5a6f9af5dda2e62f2a4b81cb888a15eb19ecabd10a382625cb4",
    "results/item341_j2_diagonal_affine_state_root_audit.json":
        "d5c810346f9181f10d38e9f5ae2e250a8c880e32f97cbc5bef91f6bd37f61a27",
    "manifests/item341_j2_diagonal_affine_state_manifest.json":
        "fc073e4c11a2d9ab519f0b5babae6f9f95e2e8cf9e8cbcf05c4c8ca8ba155000",
}


def default_output() -> Path:
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))


def fmod(value: F, prime: int) -> int:
    if value.denominator % prime == 0:
        raise ZeroDivisionError((value, prime))
    return value.numerator % prime * pow(value.denominator, -1, prime) % prime


def digest_rows(rows: Iterable[Iterable[Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


def h_term(index: int) -> F:
    return F(math.comb(2 * index, index), 8 ** index)


def h_prefix(index: int) -> F:
    return sum((h_term(j) for j in range(index + 1)), F(0))


def recurrence_replay(m_max: int) -> dict[str, Any]:
    values = [h_prefix(m) for m in range(m_max + 2)]
    rows = []
    for m in range(1, m_max + 1):
        lhs = (
            4 * (m + 1) * values[m + 1]
            - (6 * m + 5) * values[m]
            + (2 * m + 1) * values[m - 1]
        )
        if lhs != 0:
            raise AssertionError((m, lhs, "order-two recurrence"))
        determinant = F(2 * m + 1, 4 * (m + 1))
        if determinant == 0:
            raise AssertionError((m, "singular transfer"))
        rows.append(
            (
                m,
                values[m].numerator,
                values[m].denominator,
                determinant.numerator,
                determinant.denominator,
            )
        )
    return {
        "classification": "EXACT FINITE REPLAY ONLY",
        "m_max_inclusive": m_max,
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
    }


def cutoff_polynomial(prime: int, m: int) -> list[int]:
    """Reduced coefficients of sum_(u=0)^m (1-(X-u)^(p-1))."""
    coefficients = [0] * prime
    for u in range(m + 1):
        coefficients[0] = (coefficients[0] + 1) % prime
        for degree in range(prime):
            term = math.comb(prime - 1, degree)
            term *= pow((-u) % prime, prime - 1 - degree, prime)
            coefficients[degree] = (coefficients[degree] - term) % prime
    return coefficients


def evaluate_polynomial(coefficients: list[int], value: int, prime: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = (answer * value + coefficient) % prime
    return answer


def actual_row_replay(prime: int, r: int, s: int) -> tuple[Any, ...]:
    m = s - 1
    d = r + 4
    n = (prime - 1) // 2
    if prime != 2 * r + 6 * s + 3:
        raise AssertionError((prime, r, s, "tied prime"))
    if n != 3 * m + d:
        raise AssertionError((prime, r, s, n, "Frobenius exponent"))
    if not (0 <= m < prime and 0 < m + 1 < prime):
        raise AssertionError((prime, m, "prefix range"))

    inverse_two = pow(2, -1, prime)
    inverse_eight = pow(8, -1, prime)
    G_mod = 0
    H_mod = 0
    g_values = []
    for j in range(prime):
        if j <= n:
            g_mod = math.comb(n, j) % prime
            g_mod = g_mod * pow((-inverse_two) % prime, j, prime) % prime
            g_exact = F(math.comb(n, j) * ((-1) ** j), 2 ** j)
        else:
            g_mod = 0
            g_exact = F(0)
        g_values.append(g_exact)
        if j <= m:
            G_mod = (G_mod + g_mod) % prime
            H_mod = (
                H_mod
                + (math.comb(2 * j, j) % prime) * pow(inverse_eight, j, prime)
            ) % prime
    if G_mod != H_mod or H_mod != fmod(h_prefix(m), prime):
        raise AssertionError((prime, r, s, G_mod, H_mod, "Frobenius prefix"))

    # On an actual endpoint every coefficient in the reversible recurrence is a unit.
    endpoint_units = (4 * (m + 1), 6 * m + 5, 2 * m + 1)
    if not all(0 < value < prime and value % prime for value in endpoint_units):
        raise AssertionError((prime, m, endpoint_units, "recurrence units"))

    # Every additive Fourier coefficient of the interval is nonzero:
    # for a != 0 this is equivalent to a*(m+1) != 0 mod p.
    nonzero_modes = 1
    exponent_digest_rows = [(0, m + 1, 0)]
    for a in range(1, prime):
        numerator_exponent = a * (m + 1) % prime
        denominator_exponent = a % prime
        if numerator_exponent == 0 or denominator_exponent == 0:
            raise AssertionError((prime, m, a, "zero Fourier coefficient"))
        nonzero_modes += 1
        exponent_digest_rows.append((a, numerator_exponent, denominator_exponent))
    if nonzero_modes != prime:
        raise AssertionError((prime, nonzero_modes, "mode count"))

    # Orthogonality leaves exactly j=u because both ranges lie in [0,p-1].
    completion_numerator = F(0)
    matching_pairs = 0
    for u in range(m + 1):
        for j, g_exact in enumerate(g_values):
            if (j - u) % prime == 0:
                completion_numerator += prime * g_exact
                matching_pairs += 1
    G_exact = sum(g_values[:m + 1], F(0))
    if completion_numerator != prime * G_exact or matching_pairs != m + 1:
        raise AssertionError((prime, matching_pairs, "orthogonality completion"))

    coefficients = cutoff_polynomial(prime, m)
    degree = max(index for index, value in enumerate(coefficients) if value)
    if degree != prime - 1:
        raise AssertionError((prime, m, degree, "cutoff degree"))
    if coefficients[-1] != (-(m + 1)) % prime:
        raise AssertionError((prime, m, coefficients[-1], "leading coefficient"))
    for value in range(prime):
        expected = 1 if value <= m else 0
        if evaluate_polynomial(coefficients, value, prime) != expected:
            raise AssertionError((prime, m, value, "cutoff interpolation"))

    M_numerator = 5 * r + 14 * s + 7
    if M_numerator % 2:
        raise AssertionError((prime, r, s, "nonintegral M"))
    M = M_numerator // 2
    if 5 * prime != 4 * M + 2 * m + 3 or r != 6 * M - 7 * prime:
        raise AssertionError((prime, r, s, M, "fixed-M relation"))

    boundary_degree = r + 2
    last_odd = 2 * boundary_degree - 1
    if not (0 < last_odd < prime):
        raise AssertionError((prime, r, boundary_degree, "boundary unit range"))
    odd_product_mod = 1
    for odd in range(1, last_odd + 1, 2):
        odd_product_mod = odd_product_mod * odd % prime
    if odd_product_mod == 0:
        raise AssertionError((prime, r, "boundary leading coefficient pole"))

    return (
        prime,
        r,
        s,
        m,
        n,
        M,
        H_mod,
        nonzero_modes,
        degree,
        coefficients[-1],
        matching_pairs,
        boundary_degree,
        last_odd,
        odd_product_mod,
        hashlib.sha256(
            (",".join(map(str, coefficients)) + "\n").encode("ascii")
        ).hexdigest(),
        digest_rows(exponent_digest_rows),
    )


def actual_rows_replay() -> dict[str, Any]:
    declared = [
        (11, 1, 1),
        (17, 1, 2),
        (29, 1, 4),
        (271, 113, 7),
        (367, 65, 39),
        (383, 109, 27),
        (599, 7, 97),
    ]
    rows = [actual_row_replay(*row) for row in declared]
    return {
        "classification": "EXACT FINITE REPLAY ONLY - NO ZERO CENSUS",
        "declared_rows": len(rows),
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
    }


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    if not args.skip_dependency_check:
        verify_dependencies()
    return {
        "schema": "item344-j2-frobenius-cutoff-obstruction-v1",
        "classification": "PROVED_MAXIMAL_MOVING_CUTOFF_COMPLEXITY_AND_BOUNDED_COMPLETION_NO_GO",
        "dependency_hashes_verified": not args.skip_dependency_check,
        "dependencies": DEPENDENCIES,
        "proved_formulae": {
            "generating_function": "sum H_m*z^m=1/((1-z)*sqrt(1-z/2))",
            "recurrence": "4(m+1)H_(m+1)-(6m+5)H_m+(2m+1)H_(m-1)=0",
            "Frobenius_coefficient": "H_m=[z^m](1-z/2)^((p-1)/2)/(1-z) mod p",
            "quadratic_carrier": "(1-z/2)^((p-1)/2)=U(z^p)/U(z), U^2=1-z/2",
            "character_completion": "p*G_(p,m)=sum_a Ihat_m(a)*(1-zeta^a/2)^((p-1)/2)",
            "Fourier_support": "all p additive modes are nonzero because 1<=m+1<p",
            "cutoff_degree": "deg sum_(u=0)^m(1-(X-u)^(p-1))=p-1",
            "sublinear_edge_mass": "m=o(M) or r=o(M) contributes o(M) logarithmic mass",
        },
        "recurrence_replay": recurrence_replay(args.m_max),
        "actual_rows_replay": actual_rows_replay(),
        "capacity": {
            "raw_ordinary_j2_chebyshev_mass": "(2/35)M+o(M)",
            "raw_ordinary_j2_ceiling_per_6M": "1/105",
            "new_capacity_reduction": 0,
            "new_booking": 0,
        },
        "closed_method_class": [
            "exact pre-summand cutoff replacement by bounded-degree or o(p)-degree F_p polynomials",
            "exact pre-summand additive completion with a bounded or o(p) number of modes",
            "the fixed quadratic Frobenius carrier or state recurrence used without an arithmetic law for the moving target",
            "direct bounded or sublinear prefix/boundary analysis as a positive-rate mechanism",
        ],
        "open": [
            "target-specific cancellation among the full p completed modes",
            "a bounded-conductor joint model retaining (4^(m+1)-c_star,H_m-Theta)",
            "weighted nonconcentration for the actual moving target",
            "weighted support of the degenerate triple-minor carrier",
        ],
        "scope_warning": (
            "The no-go concerns exact cutoff-first bounded-complexity methods. "
            "It does not exclude summand-specific cancellation, a moving Frobenius sheaf, "
            "or a joint weighted-density theorem. Finite rows are formula replay only."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m-max", type=int, default=120)
    parser.add_argument("--output", type=Path, default=default_output())
    parser.add_argument("--skip-dependency-check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.m_max < 10:
        raise ValueError("m_max must be at least 10")
    result = build_result(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
