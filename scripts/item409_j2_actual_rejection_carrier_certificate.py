#!/usr/bin/env python3
"""Deterministic certificate for Item 409.

This checker reconstructs the *actual* ordinary-j=2 connection sequences,
the safely saturated degenerate gate and target carriers, and

    J_(r,s) = (Pi_sat_(r,s))_(Gamma_sat_(r,s)).

It also replays the algebraic/holonomic formulae used in the report, gives an
actual counterexample to the proposed all-row good-reduction identities, and
checks exact capacity arithmetic.  Declared rows are formula witnesses only;
there is no prime census and no finite-data extrapolation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
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
RESULT_NAME = "item409_j2_actual_rejection_carrier_certificate.json"


DEPENDENCIES = {
    "sources/item334_j2_coupled_cartier_carrier_report.md":
        "a9a1b42652e5157b850014758c321ffd8a5734e4f9ea3586510ae0549822357c",
    "scripts/item334_j2_coupled_cartier_carrier_certificate.py":
        "b9cab6a6ddc4a0817bae5852e78473ab3144ed9a3b8985c7eacaf27629c90cce",
    "results/item334_j2_coupled_cartier_carrier_certificate.json":
        "238046186f90bdffb2e9b4c72994bac4f0c2ba7e377b42f04753b5502ea861e2",
    "manifests/item334_j2_coupled_cartier_carrier_manifest.json":
        "518176b7e7cf5908e350bb857063bae47658050ca63c4a0e1976554efac87bc9",
    "sources/item338_j2_secondary_cartier_saturation_report.md":
        "14aa87b718b4bb83dd3e5371412fd231829f809b853d1a52eabba6181650ac33",
    "scripts/item338_j2_secondary_cartier_saturation_certificate.py":
        "5209d57fee32a6bad74e8f5b933116aa4d62448b1f9ca44e539cadf7f95fe6bd",
    "results/item338_j2_secondary_cartier_saturation_certificate.json":
        "accf5bf87b148c73117f05b8d9f7eee92af1d59611871498593cc992c758450d",
    "manifests/item338_j2_secondary_cartier_saturation_manifest.json":
        "d3ecc6c74e3dbd3b921a3f5c3aa363eac10e68322536c88ced5e6972785a6573",
    "sources/item349_j2_degenerate_triple_minor_carrier_report.md":
        "ca3141156cb5034012a174377c3596e22d22cae924625649b6d620d510f4790c",
    "scripts/item349_j2_degenerate_triple_minor_carrier_certificate.py":
        "b72b1ee335f243ae6a2761c417e27640f443183ec625027a14d5b7e06b91cf9b",
    "results/item349_j2_degenerate_triple_minor_carrier_certificate.json":
        "b26294d51b1844aeee04146004b2ecec9b6e1ff81aa271a3167e5d86c11bce44",
    "manifests/item349_j2_degenerate_triple_minor_carrier_manifest.json":
        "1c1dec25ac00ea5adb2befe885c9c96ba805564651b6e90c73ef2506d30e7f4f",
    "sources/item397_j2_matched_aggregate_factor_localization_report.md":
        "4f30aab79be7039866bbad7e71cc545bd0e553d51d1166b77cb3d5f5371476ee",
    "scripts/item397_j2_matched_aggregate_factor_localization_certificate.py":
        "f7fe2d81b31ce31fb41e77c551119ac66fa7b62fadda2691ae06036ef4426186",
    "results/item397_j2_matched_aggregate_factor_localization_certificate.json":
        "45df777a3a93c0c7e4b62dadd75da7d7231d4235b2e9efde1b5204fee43254d3",
    "manifests/item397_j2_matched_aggregate_factor_localization_manifest.json":
        "a6aa125bcc12f5b258ea02fb2e552b2a658c6b8ca9bd56386297530891ef5044",
    "sources/item399_j2_raywise_chosen_prime_invariant_report.md":
        "6c7aec34049d0ed74676166d746eeb5b256f2ff45fb8409671688abd4b4fbf26",
    "scripts/item399_j2_raywise_chosen_prime_invariant_certificate.py":
        "ab58b05023329805e06e66a4c20430943fc17cda33133cace0b83d79f7e67d90",
    "results/item399_j2_raywise_chosen_prime_invariant_certificate.json":
        "967cb7effb6bf2f3f2d255c4eec6418b5ae65244888026f2e6cbc0c20ad94a35",
    "manifests/item399_j2_raywise_chosen_prime_invariant_manifest.json":
        "3f2ae65892fa23a2b5ca0c12be81eda5d924daf2c78f2442662e43293d3f326d",
    "sources/item402_j2_marked_frobenius_descent_no_go_report.md":
        "c6ba6147dfe835a2f01654e71131ee4e7df4c54aae91811ad7fbb3c30ba1f720",
    "scripts/item402_j2_marked_frobenius_descent_no_go_certificate.py":
        "9c4404518a85396c29578a04998f19577bafce4f4aecf167c0102f8d0aed6997",
    "results/item402_j2_marked_frobenius_descent_no_go_certificate.json":
        "1ca82cfc211a97961ad615d931f09d97df074596caff61741f434e64eb0fe3b7",
    "manifests/item402_j2_marked_frobenius_descent_no_go_manifest.json":
        "25d66b0e60b21b397e7dbfd9fb399551f1d9e406432b981f5a4b73847b27e08f",
    "sources/item404_j2_degenerate_target_rejection_capacity_report.md":
        "e691d2118611781aee2a3e851afa9b26495b75b142d9f40f6b75234334df4de2",
    "scripts/item404_j2_degenerate_target_rejection_capacity_certificate.py":
        "8d74c388dbfa9aee5762a99243000a791e0d93b8d9bacb7ef6b3485e230e9694",
    "results/item404_j2_degenerate_target_rejection_capacity_certificate.json":
        "e40b09431077bb8a432dfe8acb2678cd563f323e0ceab06f3da611bdba6a6636",
    "manifests/item404_j2_degenerate_target_rejection_capacity_manifest.json":
        "8e47fe49f8237662ec7e5c58029ef674a37fcc9a753e319097c31fbe83b13c36",
    "sources/item407_j2_rejection_density_boundary_report.md":
        "1894dd0b9951c54f23705380fdc5c88c3fd0b6847293f91be985914cceb42208",
    "scripts/item407_j2_rejection_density_boundary_certificate.py":
        "4e71d8fc83a1df3c438de804ac0c77ac1803d530a6c1e6a1de8a32eb665c1c10",
    "results/item407_j2_rejection_density_boundary_certificate.json":
        "9dbf1069aedbc245ff986410529d26f96de6b6259c1e196fd4b42dffac964580",
    "manifests/item407_j2_rejection_density_boundary_manifest.json":
        "fbd0a9fc2689ed523729f1ccd4e72cd00613beb632f86358025d01a160c58972",
    "results/item407_j2_rejection_density_boundary_root_audit.json":
        "ee155a6b2fa3efc1b751fb4586a4a07e559bc1b243514fc622461576076b8dd6",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_dependencies() -> dict[str, str]:
    actuals: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))
        actuals[relative] = actual
    return actuals


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def gcd_many(values: Iterable[int]) -> int:
    answer = 0
    for value in values:
        answer = math.gcd(answer, abs(value))
    return answer


def largest_divisor_coprime_to(value: int, support: int) -> int:
    answer = abs(value)
    while True:
        common = math.gcd(answer, abs(support))
        if common == 1:
            return answer
        answer //= common


def support_product(values: Iterable[F], extra: int) -> int:
    answer = abs(extra)
    for value in values:
        answer *= value.denominator
    return answer


def digest_rows(rows: Iterable[Any]) -> str:
    stream = json.dumps(list(rows), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(stream.encode("utf-8")).hexdigest()


def actual_carrier_row(
    i334: Any,
    i331: Any,
    i318: Any,
    i319: Any,
    prime: int,
    r: int,
    s: int,
) -> dict[str, Any]:
    if not is_prime(prime) or prime != 2 * r + 6 * s + 3:
        raise AssertionError((prime, r, s, "actual prime row"))
    if r < 1 or r % 2 != 1 or r % 3 == 0 or s < 1:
        raise AssertionError((prime, r, s, "ordinary-j2 range"))

    m = s - 1
    d_tied = r + 4
    n_exp = 3 * m + d_tied
    q_exp = 2 * m + d_tied
    data = i318.i250.phase_data(r)
    coeff = i318.coefficients(data)
    period = i318.actual_period(r, s, data)
    factorization = i319.canonical_factorization(r, data)

    f = coeff["f"]
    b = coeff["b"]
    v = coeff["d"]
    ell = coeff["ell"]
    minor_mu = coeff["m"]
    C = coeff["C"]
    residue = r % 6
    index = (r - residue) // 6
    sigma = (
        i319.i314.gauge_value(residue, index)
        * i319.i314.KAPPA[residue]
        / F(16 ** index)
    )
    beta = i319.beta_closed(r)
    a_value = ell / (2 * sigma)
    b_value = -minor_mu / sigma
    K_value = factorization["K"]
    Pi = gcd_many((a_value.numerator, b_value.numerator, K_value.numerator))
    if Pi <= 0:
        raise AssertionError((prime, r, s, "positive Pi"))

    c_p = i331.coefficient(n_exp, q_exp, prime)
    epsilon = i331.legendre_two(prime)
    h_m = i334.h_value(m)
    correction = i334.p_correction(r + 2, m)
    base = F(9, 2) * period["kappa"] * (F(c_p) + epsilon * h_m * correction)
    c_value = F(4 ** s)
    T = tuple(
        f[nu] * period["B"] * base
        + (-1) ** m * (
            f[nu] * period["B"] * period["tau"]
            - 9 * c_value * b[nu]
            + 11 * v[nu]
        )
        for nu in (0, 1)
    )

    Gamma = gcd_many((Pi, T[0].numerator, T[1].numerator))
    support = support_product(
        (
            *f, *b, *v,
            period["B"], period["kappa"], period["tau"],
            h_m, correction,
        ),
        extra=6 * math.comb(2 * m, m),
    )
    if support % prime == 0:
        raise AssertionError((prime, r, s, "unsafe saturation"))
    Pi_sat = largest_divisor_coprime_to(Pi, support)
    Gamma_sat = largest_divisor_coprime_to(Gamma, support)
    if Pi_sat % Gamma_sat != 0:
        raise AssertionError((prime, r, s, "Gamma_sat divides Pi_sat"))
    J = largest_divisor_coprime_to(Pi_sat, Gamma_sat)

    # The period formula is an exact tied-prime replacement for the
    # Cartier representative, not an equality of foreign-prime carriers.
    period_residual = tuple(
        f[nu] * period["Z"] + 9 * c_value * b[nu] - 11 * v[nu]
        for nu in (0, 1)
    )
    sign = (-1) ** (m + 1)
    T_mod = tuple(i334.fmod(value, prime) for value in T)
    R_mod = tuple(i334.fmod(value, prime) for value in period_residual)
    if T_mod != tuple(sign * value % prime for value in R_mod):
        raise AssertionError((prime, r, s, T_mod, R_mod, "period substitution"))

    triple_gate = all(i334.fmod(value, prime) == 0 for value in (ell, minor_mu, C))
    normalized_gate = Pi_sat % prime == 0
    target_hit = Gamma_sat % prime == 0
    rejection = J % prime == 0
    if triple_gate != normalized_gate:
        raise AssertionError((prime, r, s, "actual Pi equivalence"))
    if target_hit and not triple_gate:
        raise AssertionError((prime, r, s, "Gamma outside Pi"))
    if rejection != (triple_gate and not target_hit):
        raise AssertionError((prime, r, s, "actual J equivalence"))

    f_zero = all(i334.fmod(value, prime) == 0 for value in f)
    if triple_gate:
        if not f_zero:
            nu = 0 if i334.fmod(f[0], prime) != 0 else 1
            if target_hit != (T_mod[nu] == 0):
                raise AssertionError((prime, r, s, "f-nonzero scalar target"))
        elif target_hit != (T_mod == (0, 0)):
            raise AssertionError((prime, r, s, "f-zero vector target"))

    return {
        "p": prime,
        "r": r,
        "s": s,
        "M": (5 * r + 14 * s + 7) // 2,
        "Pi": Pi,
        "Pi_sat": Pi_sat,
        "Gamma": Gamma,
        "Gamma_sat": Gamma_sat,
        "J": J,
        "support_gcd_Pi": math.gcd(Pi, support),
        "p_divides_J": rejection,
        "actual_triple_gate": triple_gate,
        "actual_degenerate_target_hit": target_hit,
        "f_zero_mod_p": f_zero,
        "T_mod_p": T_mod,
        "period_residual_mod_p": R_mod,
        "T_numerator_bits": [abs(value.numerator).bit_length() for value in T],
        "a_b_K_numerator_bits": [
            abs(a_value.numerator).bit_length(),
            abs(b_value.numerator).bit_length(),
            abs(K_value.numerator).bit_length(),
        ],
        "support_sha256": hashlib.sha256(str(support).encode("ascii")).hexdigest(),
    }


def actual_rows_replay(i334: Any, i331: Any, i318: Any, i319: Any) -> dict[str, Any]:
    declared = [
        (17, 1, 2),
        (251, 121, 1),
        (313, 149, 2),
        (347, 157, 5),
        (709, 347, 2),
    ]
    rows = [actual_carrier_row(i334, i331, i318, i319, *row) for row in declared]
    witness = next(row for row in rows if row["p"] == 709)
    expected = {
        "Pi": 79,
        "Pi_sat": 79,
        "Gamma": 1,
        "Gamma_sat": 1,
        "J": 79,
        "p_divides_J": False,
    }
    for key, value in expected.items():
        if witness[key] != value:
            raise AssertionError(("actual good-reduction witness", key, witness[key], value))
    return {
        "classification": (
            "EXACT DECLARED ACTUAL-FORMULA ROWS ONLY / NO PRIME CENSUS / "
            "NO DENSITY EXTRAPOLATION"
        ),
        "rows": rows,
        "row_digest_sha256": digest_rows(rows),
        "actual_counterexample": {
            "row": [709, 347, 2],
            "statement_refuted": "Pi_sat_(r,s)=1 and J_(r,s)=1 on every actual row",
            "values": expected,
            "scope_warning": (
                "79 is foreign to the tied characteristic 709; this does not "
                "refute tied-prime good reduction p not dividing Pi_sat and "
                "does not prove positive J-support density"
            ),
        },
    }


def cartier_coefficient_formula(i331: Any) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for d_value in (5, 9, 11):
        for m in range(0, 6):
            n_exp = 3 * m + d_value
            q_exp = 2 * m + d_value
            k = 6 * m + 2 * d_value + 1
            direct = i331.coefficient(n_exp, q_exp, k)
            convolution = 0
            for j in range(0, n_exp + 1):
                other = k - j
                if 0 <= other <= n_exp + q_exp:
                    convolution += ((-1) ** j) * math.comb(n_exp, j) * math.comb(n_exp + q_exp, other)
            if direct != convolution:
                raise AssertionError((d_value, m, direct, convolution))
            rows.append({
                "d": d_value,
                "m": m,
                "coefficient_bits": abs(direct).bit_length(),
                "coefficient_sha256": hashlib.sha256(str(direct).encode("ascii")).hexdigest(),
            })
    return {
        "classification": "EXACT FINITE EXPANSION REPLAY OF A SYMBOLIC CONSTANT-TERM IDENTITY",
        "bivariate_constant_term": (
            "sum_(m,d>=0)c_(m,d)t^m u^d = CT_x x^(-1)/"
            "[(1-t(1-x)^3(1+x)^5/x^6)(1-u(1-x)(1+x)^2/x^2)]"
        ),
        "coefficient": (
            "c_(m,d)=[x^(6m+2d+1)](1-x)^(3m+d)(1+x)^(5m+2d)"
        ),
        "consequence": "the raw Cartier digit is a rational diagonal and hence holonomic",
        "rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
    }


def period_recurrence_replay(i251: Any) -> dict[str, Any]:
    values = {s: i251.a_direct(s) for s in range(1, 23)}
    if values[1] != 3 or values[2] != 49:
        raise AssertionError((values[1], values[2], "period initials"))
    rows = []
    for s in range(1, 21):
        residual = (
            (s + 1) * (2 * s + 3) * (28 * s + 11) * values[s + 2]
            - (1456 * s**3 + 3456 * s**2 + 2303 * s + 435) * values[s + 1]
            - 6 * (3 * s + 1) * (3 * s + 2) * (28 * s + 39) * values[s]
        )
        if residual != 0:
            raise AssertionError((s, residual, "A_s recurrence"))
        rows.append((s, len(str(abs(values[s]))), len(str(abs(values[s + 1])))))
    return {
        "classification": "EXACT FINITE REPLAY OF THE PROVED ITEM-251 ACTUAL PERIOD RECURRENCE",
        "generating_function": (
            "sum_(s>=1)A_s t^(s-1)=(2+w)^3/[2(1-w^2)]-1/(1+t), "
            "where w=t(2+w)^3"
        ),
        "recurrence_rows": len(rows),
        "row_digest_sha256": digest_rows(rows),
        "moving_characteristic_warning": (
            "at fixed r, s->s+1 changes the tied modulus p to p+6; "
            "the recurrence is an integer identity, not a map F_p->F_(p+6)"
        ),
    }


def known_operator_separation(i319: Any) -> dict[str, Any]:
    result = i319.operator_reuse_counterexamples({})
    for row in result["rows"]:
        for residual in row["residuals"].values():
            if not residual["nonzero"]:
                raise AssertionError((row, "operator separation"))
    return {
        "classification": (
            "PROVED EXACT COUNTEREXAMPLES TO FIVE SPECIFIED COMMON-OPERATOR "
            "IDENTITIES / NOT A NO-GO FOR EVERY POSSIBLE RECURRENCE"
        ),
        "rays": result["rows"],
        "conclusion": (
            "the actual K_r chain is not annihilated by the known a_r,b_r "
            "operator in the five natural gauges tested, so its Abel/Casoratian "
            "cannot be used as a proved moving-row resultant for Pi"
        ),
    }


def atomic_matched_rejection_theorem() -> dict[str, Any]:
    declared = []
    for M in (20, 35, 100, 335, 1000):
        lower = -(-(4 * M + 3) // 5)
        upper = (6 * M - 1) // 7
        if not upper < 2 * lower:
            raise AssertionError((M, lower, upper))
        for q in range(lower, upper + 1):
            for prime in range(lower, upper + 1):
                if is_prime(prime) and q % prime == 0 and q != prime:
                    raise AssertionError((M, lower, upper, q, prime))
        declared.append((M, lower, upper, upper < 2 * lower))
    return {
        "classification": (
            "PROVED ALL-M ATOMIC LOCALIZATION; DECLARED BOUNDS ARE "
            "EXACT FINITE IMPLEMENTATION REPLAY"
        ),
        "definition": (
            "j_(M,q)^sharp=(rad gcd(q,J_(6M-7q,(5q-4M-1)/2)))_((L_M-1)!)"
        ),
        "theorem": (
            "j_(M,q)^sharp=q exactly when q is prime and its actual row is "
            "degenerate-target-rejected; otherwise it is 1"
        ),
        "pairwise": "gcd(j_(M,q)^sharp,j_(M,q')^sharp)=1 for q!=q'",
        "proof_key": "U_M<2L_M, so a prime lambda>=L_M dividing q in [L_M,U_M] forces q=lambda",
        "declared_bounds": declared,
        "scope_warning": (
            "this closes only common-divisor reuse among matched factors; a "
            "formula-specific theorem using unmatched values remains open"
        ),
    }


def frac(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def capacity_replay() -> dict[str, Any]:
    R = F(1, 35)
    scenarios = []
    for name, j, g, n in (
        ("no_actual_margin", F(0), R, R),
        ("J_half_ray_only", F(1, 70), R, R),
        ("two_chart_upper_bounds", F(0), F(1, 140), F(1, 140)),
        ("both_routes", F(1, 140), F(1, 140), F(1, 140)),
        ("full_J_ray", R, R, R),
    ):
        excluded = max(F(0), j, R - g - n)
        scenarios.append({
            "name": name,
            "J_lower_per_M": frac(j),
            "G_upper_per_M": frac(g),
            "N_upper_per_M": frac(n),
            "excluded_lower_per_M": frac(excluded),
            "normalized_saving": frac(excluded / 6),
        })
    if scenarios[1]["normalized_saving"] != "1/420":
        raise AssertionError(scenarios[1])
    if scenarios[2]["normalized_saving"] != "1/420":
        raise AssertionError(scenarios[2])
    if scenarios[-1]["normalized_saving"] != "1/210":
        raise AssertionError(scenarios[-1])
    return {
        "one_ray_mass_per_M": "1/35",
        "one_ray_normalized_capacity": "1/210",
        "actual_J_coupling": (
            "J_e(M)>=jM, G_e(M)<=gM, N_e(M)<=nM imply excluded mass "
            ">=max(0,j,1/35-g-n)M+o(M)"
        ),
        "normalized_saving": "max(0,j,1/35-g-n)/6",
        "good_reduction_direction": (
            "Pi_sat=1 makes j=0 and books zero without a nondegenerate bound; "
            "relative target good reduction Gamma_sat=1 still needs positive "
            "degenerate occupancy"
        ),
        "scenarios": scenarios,
        "proved_j_lower_per_M": 0,
        "proved_eta_per_M": 0,
        "new_booking": 0,
        "new_capacity_reduction": 0,
        "retained_ordinary_j2_ceiling_per_6M": "1/105",
    }


def build_payload() -> dict[str, Any]:
    dependencies = verify_dependencies()
    i334 = load("item409_i334", "scripts/item334_j2_coupled_cartier_carrier_certificate.py")
    i349 = load("item409_i349", "scripts/item349_j2_degenerate_triple_minor_carrier_certificate.py")
    i318 = i334.load("item409_i318", "scripts/item318_j2_actual_period_plucker_certificate.py")
    i331 = i334.load("item409_i331", "scripts/item331_j2_global_cartier_concentration_certificate.py")
    i319 = i349.load("item409_i319", "scripts/item319_j2_third_minor_elimination_certificate.py")

    return {
        "item": 409,
        "schema": "item409-j2-actual-rejection-carrier-v1",
        "title": "actual formula, recurrence, and resultant audit for the degenerate rejection carrier",
        "checked_date_beijing": "2026-09-01",
        "status": "PROVED_EXACT_WITNESS_AND_SCREENED_MECHANISM_OBSTRUCTIONS_ETA_ZERO",
        "dependency_hashes_verified": dependencies,
        "actual_formula": {
            "gate": "Pi_r=gcd(abs(num(a_r)),abs(num(b_r)),abs(num(K_r)))",
            "target": "Gamma_(r,s)=gcd(Pi_r,abs(num(T_0)),abs(num(T_1)))",
            "rejection": "J_(r,s)=(Pi_sat_(r,s))_(Gamma_sat_(r,s))",
            "tied_equivalence": (
                "p divides J iff p divides the actual normalized minors a_r,b_r,K_r "
                "and at least one actual target residual T_0,T_1 is nonzero mod p"
            ),
            "actual_period_replacement": (
                "T_nu=(-1)^(m+1)[f_nu Z_(r,s)+9*4^s*b_nu-11*v_nu] mod p, "
                "with Z=B_s(9*kappa_r*A_s/2-tau_(r,s))"
            ),
            "foreign_support_warning": (
                "the period replacement preserves tied-p support only; it is not "
                "an equality of the full foreign-prime integer carriers"
            ),
            "branch_split": {
                "f_nonzero": (
                    "on p|Pi, choose f_nu!=0; rejection is the nonvanishing of "
                    "one scalar residual containing the actual incomplete period A_s"
                ),
                "f_zero": (
                    "on p|Pi, the period disappears; rejection is "
                    "9*4^s*b-11*v != 0"
                ),
            },
        },
        "actual_rows_replay": actual_rows_replay(i334, i331, i318, i319),
        "cartier_rational_diagonal": cartier_coefficient_formula(i331),
        "actual_period_recurrence": period_recurrence_replay(i318.i251),
        "known_operator_separation": known_operator_separation(i319),
        "atomic_matched_rejection": atomic_matched_rejection_theorem(),
        "capacity": capacity_replay(),
        "screened_mechanism_audit": {
            "classification": "PROVED ONLY FOR THE EXPLICITLY NAMED MECHANISMS; NOT AN EXHAUSTIVE INFORMATION-CLASS NO-GO",
            "failed_mechanisms": [
                "an all-row identity Pi_sat=1 or J=1 (refuted by the actual row (709,347,2))",
                "a Casoratian/resultant built by putting K_r into the known a_r,b_r recurrence in any of five natural gauges",
                "high-prime overlap or lcm compression among distinct matched J row atoms",
                "using the fixed-r A_s recurrence as if it transported selected divisibility between p and p+6",
                "pointwise height as a lower bound for J-support",
            ],
            "not_closed": [
                "tied-prime good reduction p not dividing Pi_sat on every actual row",
                "an unmatched moving-row resultant with a proved bridge back to the selected row",
                "a cross-characteristic reciprocity law for the actual formulas",
                "a new formula-specific use of the displayed exact sequences",
                "a weighted large-prime anti-gcd theorem for Pi versus the two T residuals",
            ],
        },
        "smallest_missing_lemma": {
            "name": "actual tied large-prime Smith anti-gcd lemma",
            "statement": (
                "for some ray e and delta>0, sum log p over fixed-M actual rows "
                "with r=6M-7p congruent to e mod 6, p|Pi_r, and "
                "(T_0,T_1)!=(0,0) mod p is >=delta*M+o(M)"
            ),
            "equivalent": "J_e(M)>=delta*M+o(M)",
            "reward": "normalized saving delta/6, coupled as max(delta,1/35-g-n)/6",
            "status": "OPEN",
        },
        "strict_labels": {
            "PROVED": [
                "exact actual-formula reconstruction of Pi, Gamma, and J on tied rows",
                "tied-support period normal form and internal branch split",
                "rational-diagonal formula for the raw Cartier coefficient",
                "actual counterexample to Pi_sat=1 and J=1 as all-row integer identities",
                "failure of five specified common-operator resultants",
                "atomic matched-J factor localization and exact capacity coupling",
                "proved eta and booking are zero",
            ],
            "EXACT_DECLARED_ACTUAL_FORMULA_ROWS_ONLY": [
                "the five row replays and the witness (709,347,2); no census or extrapolation"
            ],
            "EXACT_FINITE_IMPLEMENTATION_REPLAY": [
                "constant-term coefficient comparisons, period recurrence rows, and declared interval bounds"
            ],
            "CONDITIONAL": [
                "positive capacity implications whose actual weighted antecedents are explicit"
            ],
            "OPEN": [
                "the tied large-prime Smith anti-gcd lemma",
                "tied-prime good reduction, unmatched resultants, or cross-characteristic reciprocity",
                "any positive J-support lower bound or selected-prime collision upper bound",
                "Route 1 and every conclusion about e+pi",
            ],
        },
        "evidence_policy": {
            "actual_values_only_in_row_replay": True,
            "no_ambient_packet_claimed_actual": True,
            "no_prime_or_collision_census": True,
            "no_finite_extrapolation": True,
            "no_pointwise_height_booking": True,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results" / RESULT_NAME)
    parser.add_argument("--replay", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = json.loads(json.dumps(build_payload(), sort_keys=True))
    if args.replay is not None:
        frozen = json.loads(args.replay.read_text(encoding="utf-8"))
        if frozen != payload:
            raise AssertionError("replay payload differs from frozen certificate")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "item": 409,
        "output": str(args.output),
        "replay": args.replay is not None,
        "sha256": sha256(args.output),
        "new_booking": payload["capacity"]["new_booking"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
