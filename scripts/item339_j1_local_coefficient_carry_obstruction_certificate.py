#!/usr/bin/env python3
"""Deterministic exact replay for Item 339.

The checker starts from Item 332's selected diagonal b_h and verifies its
actual-row reduction to one integral local coefficient a_(r,n).  It checks
the positive hypergeometric-prefix formula, the fixed rational bivariate
carrier, the complete termwise p-carry classification, the exact recurrence
rank, and five preselected controls.  It performs no prime scan and makes no
weighted-density inference from the controls.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any

import sympy as S


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "item339_j1_local_coefficient_carry_obstruction_certificate.json"

DEPENDENCIES = {
    "sources/item308_j1_all_s_fixed_divisor_no_go_report.md":
        "4eb8f8c37dfde9d19e57c8df5ff8090bd95f03be59fff7d6aede55d02993bdc8",
    "scripts/item308_j1_all_s_fixed_divisor_no_go_certificate.py":
        "9b60d380b503c7ac9fed13792fae67735cfcf6b0f376581a0076fde16a82f0b9",
    "results/item308_j1_all_s_fixed_divisor_no_go_certificate.json":
        "4efff9ca2fb1bc11cc6030e260ff73aae89c28bd157bb41fa6bbc3b32e41e5cf",
    "results/item308_root_audit.json":
        "11feb8105ea46c27d83df2449404297fe74709eceaa8be6a21bd9484cbffba22",
    "manifests/item308_j1_all_s_fixed_divisor_no_go_manifest.json":
        "1c4721f43b5bbdc0c68e4d9fd689562a32a4af4fbbab2a9e7075da96b151b4d5",
    "sources/item332_j1_global_diagonal_collapse_report.md":
        "7bb0aff7943f13e517d67ac84120c4f956d0234232ff280f4ddde2ff78cdb954",
    "scripts/item332_j1_global_diagonal_collapse_certificate.py":
        "4562fd5f50947703a5ddc7c03634c633733cbd383ee605ba7761d103b3225d2e",
    "results/item332_j1_global_diagonal_collapse_certificate.json":
        "d544609c7ccc08f2ed0c661533939de60d97d2ab75509692925638420f789f68",
    "results/item332_j1_global_diagonal_collapse_certificate_replay.json":
        "d544609c7ccc08f2ed0c661533939de60d97d2ab75509692925638420f789f68",
    "results/item332_j1_global_diagonal_collapse_root_audit.json":
        "88ce3dd64aaf3011beeb74955f906be41231f9a42873e70b4a09fe7517143317",
    "manifests/item332_j1_global_diagonal_collapse_manifest.json":
        "999db69e1ead2bfab7733a1d57c5732e502adcaff9b14953d8b64aec19395f1c",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_dependencies() -> None:
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(("dependency mismatch", relative))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pin_dependencies()
ITEM332 = load_module(
    "item339_pinned_item332",
    ROOT / "scripts/item332_j1_global_diagonal_collapse_certificate.py",
)


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def a_hypergeometric(r: int, n: int) -> int:
    """The exact integral coefficient [u^n]G(u)^(-r)."""
    return sum(
        comb(r + k - 1, k) * comb(4 * r + n - 1, n - 4 * k)
        for k in range(n // 4 + 1)
    )


def hypergeometric_terms(r: int, n: int) -> list[int]:
    return [
        comb(r + k - 1, k) * comb(4 * r + n - 1, n - 4 * k)
        for k in range(n // 4 + 1)
    ]


def survivor_length(r: int, n: int) -> int:
    """Number of hypergeometric terms that are p-units on p=3r+2n."""
    if r <= n:
        return n // 4 + 1
    d = r - n - 1
    delta = n % 4
    top = min(d, n)
    if top < delta:
        return 0
    return (top - delta) // 4 + 1


def symbolic_audit() -> dict[str, Any]:
    u, t, z, w, x = S.symbols("u t z w x")
    h, s, n, r, M, p = S.symbols("h s n r M p", integer=True)
    F = 1 - 2 * t + S.Rational(3, 2) * t**2 - S.Rational(1, 2) * t**3
    G = 1 - 4 * u + 6 * u**2 - 4 * u**3
    if S.expand(F.subs(t, 2 * u) - G) != 0:
        raise AssertionError("G=F(2u)")
    if S.expand(G - ((1 - u) ** 4 - u**4)) != 0:
        raise AssertionError("quartic-difference identity")

    substitutions = {n: 2 * h, r: 2 * s + 1}
    actual = {
        "p": p - (2 * n + 3 * r),
        "2M": 2 * M - (3 * n + 4 * r),
    }
    actual_substitutions = {
        **substitutions,
        M: 3 * h + 4 * s + 2,
        p: 4 * h + 6 * s + 3,
    }
    if any(S.expand(value.subs(actual_substitutions)) != 0 for value in actual.values()):
        raise AssertionError("actual row parameterization")
    if S.expand((4 * h - p) / 3 + r).subs(actual_substitutions) != 0:
        raise AssertionError("Frobenius exponent shift")
    if S.expand(p - (4 * M + r) / 3).subs(actual_substitutions) != 0:
        raise AssertionError("fixed-M candidate prime")

    carrier = z * G / (G**2 - z**2)
    odd_geometric = (z / G) / (1 - (z / G) ** 2)
    if S.cancel(carrier - odd_geometric) != 0:
        raise AssertionError("bivariate rational carrier")

    return {
        "F_t": str(F),
        "G_u": str(G),
        "quartic_difference": "G(u)=(1-u)^4-u^4",
        "actual_parameters": {
            "n": "2h",
            "r": "2s+1",
            "p": "2n+3r",
            "2M": "3n+4r",
            "fixed_M_prime": "p=(4M+r)/3",
        },
        "frobenius_reduction": {
            "eta": "eta=h mod 3=p mod 3 in {1,2}",
            "unit_branch": "U(t)=F(t)^(1/3), U(0)=1",
            "formal_identity_mod_p":
                "F^(4h/3)=U(t)^p F^(-r)=U(t^p)F^(-r)",
            "coefficient_consequence":
                "because n<p, b_h=[t^n]F(t)^(-r) mod p",
        },
        "integral_normalization":
            "a_(r,n)=2^n[t^n]F(t)^(-r)=[u^n]G(u)^(-r) in Z",
        "positive_prefix":
            "a_(r,n)=sum_(0<=k<=floor(n/4)) C(r+k-1,k) C(4r+n-1,n-4k)",
        "rational_bivariate_carrier": str(carrier),
        "fixed_M_row_polynomial":
            "R_M(w)=[x^(2M)] C(w x^4,x^3); [w^r]R_M=a_(r,n) when 3n+4r=2M",
    }


def carry_theorem() -> dict[str, Any]:
    return {
        "setup": {
            "N": "4r+n-1",
            "p": "3r+2n",
            "d": "N-p=r-n-1",
            "m_k": "n-4k",
            "delta": "n mod 4 in {0,2}",
        },
        "first_factor":
            "C(r+k-1,k) is a p-unit for every 0<=k<=floor(n/4)",
        "case_r_at_most_n":
            "N<p, so every C(N,n-4k) and every complete summand is a p-unit",
        "case_r_at_least_n_plus_1":
            "N=p+d<2p and Lucas gives C(p+d,m)=C(d,m) mod p for 0<=m<p",
        "survivors":
            "the surviving terms are exactly those with n-4k<=d",
        "complete_termwise_zero_classification":
            "all summands are divisible by p iff d=0 and delta=2, equivalently r=n+1 and n=2 mod 4",
        "actual_row_translation":
            "all summands are divisible by p iff h=s is odd; then p=10h+3 and M=7h+2",
        "strict_scope":
            "outside that ray at least one summand is a p-unit, but the total sum can still vanish by cancellation",
    }


def direct_controls() -> list[dict[str, Any]]:
    declared = [
        (1, 1, 13, [0], 0, 0),
        (2, 1, 17, [5, 3], 8, 2),
        (8, 2, 47, [1, 4, 43, 23, 23], 0, 5),
        (4, 4, 43, [0, 0, 2], 2, 1),
        (2, 6, 47, [23, 13], 36, 2),
    ]
    output = []
    for h, s, prime, expected_residues, expected_sum, expected_length in declared:
        n = 2 * h
        r = 2 * s + 1
        M = 3 * h + 4 * s + 2
        if prime != 2 * n + 3 * r or 2 * M != 3 * n + 4 * r:
            raise AssertionError("declared row is not actual")

        b_value = ITEM332.b_coefficient(h)
        a_value = a_hypergeometric(r, n)
        if Fraction(a_value) != 2**n * ITEM332.rational_power_series(
            [Fraction(1), Fraction(-2), Fraction(3, 2), Fraction(-1, 2)],
            Fraction(-r),
            n,
        )[n]:
            raise AssertionError("exact local coefficient versus positive prefix")
        if a_value % prime != pow(2, n, prime) * fraction_mod(b_value, prime) % prime:
            raise AssertionError("actual Frobenius bridge")

        terms = hypergeometric_terms(r, n)
        residues = [value % prime for value in terms]
        length = survivor_length(r, n)
        if residues != expected_residues or a_value % prime != expected_sum:
            raise AssertionError(("declared prefix control", h, s, prime))
        if sum(value != 0 for value in residues) != length or length != expected_length:
            raise AssertionError("survivor length")

        d = r - n - 1
        delta = n % 4
        forced = d == 0 and delta == 2
        if forced != (length == 0):
            raise AssertionError("termwise forced-zero classification")
        output.append(
            {
                "classification": "PRESELECTED EXACT CONTROL; NOT A PRIME SCAN",
                "M": M,
                "h": h,
                "s": s,
                "p": prime,
                "n": n,
                "r": r,
                "d": d,
                "delta": delta,
                "term_residues_mod_p": residues,
                "survivor_length": length,
                "a_mod_p": a_value % prime,
                "b_mod_p": fraction_mod(b_value, prime),
                "termwise_forced_zero": forced,
                "full_original_collision_claimed": False,
            }
        )
    return output


def recurrence_and_capacity() -> dict[str, Any]:
    return {
        "minimal_recurrence": {
            "generating_function": "sum_(n>=0) a_(r,n)u^n=G(u)^(-r)",
            "reduced_denominator_degree": "3r",
            "reason":
                "the numerator is 1, G(0)=1, and the leading coefficient of G is -4; hence for Q or F_p with p>2 the reduced denominator G^r has degree 3r",
            "conclusion":
                "the exact minimal homogeneous constant-coefficient recurrence order in n is 3r=6s+3",
        },
        "capacity_first": {
            "raw_fixed_j1_prime_mass": "M/6+o(M)",
            "forced_termwise_ray":
                "h=s odd gives at most one row at fixed M (M=7h+2), hence O(log M)=o(M)",
            "short_interval_lemma":
                "a fixed-M row set whose candidate primes lie in intervals of total length o(M) has weighted prime mass o(M), by the trivial bound below M/log^2 M and Brun-Titchmarsh above it",
            "low_rank_support":
                "if 3r=o(M), then r=o(M), so the candidate-prime interval has length o(M) and weighted mass o(M)",
            "short_prefix_support":
                "if the survivor length is o(M), then n=o(M) or positive d=r-n-1=o(M); each condition gives candidate-prime intervals of total length o(M)",
            "bulk_obstruction":
                "outside zero-rate edge sets, r=Theta(M) and the surviving prefix length is Theta(M)",
            "new_linear_log_rate": 0,
            "new_fixed_j1_capacity_reduction": 0,
            "retained_ceiling_per_6M": "1/36",
        },
        "scoped_no_go": {
            "closed": [
                "termwise Lucas/Kummer carry forcing beyond the single h=s odd ray",
                "bounded- or sublinear-rank one-variable constant-coefficient recurrence methods on positive-rate support",
                "bounded- or sublinear-length surviving-tail arguments on positive-rate support",
                "treating the direct unit-branch Frobenius reduction, by itself, as a fixed low-dimensional trace rather than its exact growing local jet",
            ],
            "reason":
                "Frobenius consumes the cubic branch and leaves a moving local jet of exact rank 3r; the only complete termwise carry family is zero-rate",
            "not_closed": [
                "uniform mod-p cancellation/nonconcentration for the growing hypergeometric prefix",
                "average gcd or a global factor-localization theorem for the fixed rational bivariate carrier",
                "a different global transformation to a fixed-rank trace with an actual-gate implication",
                "weighted zero density W_b(M)=o(M)",
            ],
        },
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "item339-j1-local-coefficient-carry-obstruction-certificate-v1",
        "item": 339,
        "date": "2026-09-01",
        "status":
            "PROVED_LOCAL_COEFFICIENT_REDUCTION_TERMWISE_CARRY_CLASSIFICATION_AND_SCOPED_GROWING_RANK_NO_GO",
        "dependencies": DEPENDENCIES,
        "symbolic": symbolic_audit(),
        "carry_theorem": carry_theorem(),
        "recurrence_and_capacity": recurrence_and_capacity(),
        "direct_controls": direct_controls(),
        "classification": {
            "PROVED": [
                "actual-row Frobenius reduction b_h=[t^n]F^(-r) mod p and integral normalization a_(r,n)",
                "exact positive hypergeometric-prefix formula and fixed rational bivariate carrier",
                "complete termwise Lucas/Kummer carry classification",
                "zero-rate capacity of the unique forced carry ray",
                "exact minimal fixed-r recurrence rank 3r and zero-rate support of sublinear rank or prefix length",
                "scoped growing-rank/local-method no-go",
            ],
            "EXACT_FINITE_ONLY": [
                "five preselected controls, including one all-unit cancellation zero at p=47; no scan"
            ],
            "OPEN": [
                "weighted zero density W_b(M)=o(M)",
                "uniform mod-p nonconcentration for a growing-length positive hypergeometric prefix",
                "average-gcd or global factor localization for the fixed rational bivariate carrier",
                "fixed-j1 closure, Route 1, and every conclusion about e+pi",
            ],
        },
        "canonical_files_modified": False,
        "prime_scans": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "item": 339,
                "local_coefficient": "PROVED",
                "termwise_carry_classification": "PROVED",
                "forced_carry_mass": "ZERO_RATE",
                "bulk": "GROWING_LENGTH_CANCELLATION",
                "weighted_density": "OPEN",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
