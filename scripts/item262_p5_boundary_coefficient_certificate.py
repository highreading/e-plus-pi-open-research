#!/usr/bin/env python3
"""Deterministic certificate for Item 262's p=5 mod 6 boundary coefficient.

The checker proves and replays exact rational recurrences and valuation
identities for K_delta=B_delta^(5), verifies its localization inside the
Item-251 period, and keeps every bounded prime census explicitly finite-only.
Only Python's standard library is used.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item262_p5_boundary_coefficient_certificate.json"
ITEM251_NAME = "item251_j2_exceptional_period_certificate.py"
ITEM251_SHA256 = "a255ebeef0d73ef82bc6197a1f3f88c9522b6d8408f449971911702842c92f61"
ITEM260_REPORT = "item260_p5_punctured_cohomology_report.md"
ITEM260_REPORT_SHA256 = "e9f055bae0a3a85392aa31faba1b7dbeb383375f6d81f241e678f5f855d8576a"


def resolve(name: str, source: bool = False) -> Path:
    bases = [HERE]
    if HERE.name.lower() == "scripts":
        bases.append(HERE.parent / ("sources" if source else "scripts"))
    else:
        bases.append(HERE.parent / ("sources" if source else "scripts"))
    for base in bases:
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM251_PATH = resolve(ITEM251_NAME)
ITEM260_PATH = resolve(ITEM260_REPORT, source=True)
if sha256(ITEM251_PATH) != ITEM251_SHA256:
    raise RuntimeError("Item251 checker hash mismatch")
if sha256(ITEM260_PATH) != ITEM260_REPORT_SHA256:
    raise RuntimeError("Item260 report hash mismatch")
item251 = load_module("item262_item251", ITEM251_PATH)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def v2_int(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0)")
    n = abs(n)
    return (n & -n).bit_length() - 1


def v2_fraction(x: F) -> int:
    return v2_int(x.numerator) - v2_int(x.denominator)


def fmod(x: F, p: int) -> int:
    if x.denominator % p == 0:
        raise AssertionError(("nonunit", x, p))
    return x.numerator * pow(x.denominator, -1, p) % p


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for a in range(2, math.isqrt(n) + 1):
        if sieve[a]:
            sieve[a * a : n + 1 : a] = b"\x00" * (((n - a * a) // a) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def coefficient_data(delta: int) -> tuple[list[F], F, F]:
    """Return c_0,...,c_(delta-1), K_delta, and c_delta."""
    if delta < 1:
        raise ValueError(delta)
    c = F(1)
    terms: list[F] = []
    total = F(0)
    for j in range(delta):
        terms.append(c)
        total += c
        c *= F(6 * j + 5, 3 * j + 4)
    return terms, total, c


def reverse_ratio(j: int) -> F:
    """R_j=K_(j+1)/c_j, with an odd denominator."""
    r = F(1)
    for i in range(j):
        r = 1 + F(3 * i + 4, 6 * i + 5) * r
    return r


def a_two(n: int) -> int:
    """-v_2(c_(2n))."""
    return n + sum(v2_int(3 * u + 2) for u in range(n))


def pi_delta(delta: int) -> F:
    """Fixed p=5 mod 6 localization of Item-251's P_(3delta)."""
    term = F(1)
    total = F(0)
    for t in range(3 * delta):
        term *= F(3 * t - 3 * delta - 1, 3 * (2 * t + 1))
        total += term
    return total


def prefix_mod(p: int, q: int) -> tuple[list[int], list[int]]:
    h_values = [1]
    h_sums = [1]
    h = 1
    total = 1
    for j in range(q):
        h = h * (2 * j + 1) * pow(4 * (j + 1), -1, p) % p
        total = (total + h) % p
        h_values.append(h)
        h_sums.append(total)
    return h_values, h_sums


def p_correction_mod(p: int, m: int, d: int) -> int:
    term = 1
    total = 0
    for k in range(1, d + 1):
        term = term * (2 * m + 2 * k - 1) * pow(2 * (2 * k - 1), -1, p) % p
        total = (total + term) % p
    return total


def recurrence_and_valuations(delta_max: int) -> dict[str, Any]:
    k_values = [F(0)]
    c = F(1)
    total = F(0)
    digest = hashlib.sha256()
    valuation_samples: list[dict[str, Any]] = []
    for delta in range(1, delta_max + 3):
        total += c
        k_values.append(total)
        c *= F(6 * (delta - 1) + 5, 3 * (delta - 1) + 4)

    recurrence_checks = 0
    for delta in range(delta_max):
        lhs = (
            (3 * delta + 4) * k_values[delta + 2]
            - 9 * (delta + 1) * k_values[delta + 1]
            + (6 * delta + 5) * k_values[delta]
        )
        if lhs:
            raise AssertionError(("order-two recurrence", delta, lhs))
        recurrence_checks += 1

    odd_section_checks = 0
    for n in range(1, (delta_max - 1) // 2):
        a = (12 * n - 1) * (12 * n + 5) * (n + 1)
        b = (6 * n + 4) * (6 * n + 7) * n
        lhs = b * k_values[2 * n + 3] - (a + b) * k_values[2 * n + 1] + a * k_values[2 * n - 1]
        if lhs:
            raise AssertionError(("odd-section recurrence", n, lhs))
        odd_section_checks += 1

    two_checks = 0
    three_checks = 0
    for delta in range(1, delta_max + 1):
        terms, kval, _ = coefficient_data(delta)
        digest.update(f"{delta},{kval.numerator},{kval.denominator}\n".encode("ascii"))
        if delta % 2 == 0:
            n = delta // 2
            expected = -a_two(n)
            if v2_fraction(kval) != expected:
                raise AssertionError(("even-delta v2", delta, kval, expected))
            two_checks += 1
        else:
            n = (delta - 1) // 2
            r = reverse_ratio(2 * n)
            if r.denominator % 2 == 0 or kval != terms[-1] * r:
                raise AssertionError(("reverse ratio", delta))
            exact = -a_two(n) + v2_int(r.numerator)
            if v2_fraction(kval) != exact:
                raise AssertionError(("odd-delta v2", delta, exact))
            if n % 2 == 1 and v2_int(r.numerator) != 1:
                raise AssertionError(("n odd stratum", n))
            if n > 0 and n % 4 == 0 and v2_int(r.numerator) != 2:
                raise AssertionError(("n=0 mod 4 stratum", n))
            if n % 4 == 2 and v2_int(r.numerator) < 3:
                raise AssertionError(("n=2 mod 4 stratum", n))
            if kval.denominator % 3 == 0 or kval.numerator % 3 == 0:
                raise AssertionError(("actual v3 unit", delta))
            if fmod(kval, 3) != 1:
                raise AssertionError(("actual mod 3", delta))
            two_checks += 1
            three_checks += 1
            if delta in {1, 3, 5, 7, 9, 11, delta_max if delta_max % 2 else delta_max - 1}:
                valuation_samples.append(
                    {
                        "delta": delta,
                        "K": f"{kval.numerator}/{kval.denominator}",
                        "v2_K": v2_fraction(kval),
                        "v2_reverse_numerator": v2_int(r.numerator),
                        "v3_K": 0,
                    }
                )

    return {
        "delta_max": delta_max,
        "order_two_recurrence_checks": recurrence_checks,
        "actual_odd_section_recurrence_checks": odd_section_checks,
        "valuation_checks": two_checks,
        "actual_v3_unit_checks": three_checks,
        "K_digest_sha256": digest.hexdigest(),
        "samples": valuation_samples,
        "K_values": k_values,
    }


def denominator_height_replay(delta_max: int, k_values: list[F]) -> dict[str, Any]:
    common = 1
    c = F(1)
    terms: list[F] = []
    checks = 0
    samples: list[dict[str, Any]] = []
    for j in range(delta_max):
        terms.append(c)
        c *= F(6 * j + 5, 3 * j + 4)
    for delta in range(1, delta_max + 1):
        common = math.lcm(common, terms[delta - 1].denominator)
        n = 6 * delta
        lcm_all = 1
        for a in range(1, n + 1):
            lcm_all = math.lcm(lcm_all, a)
        odd_lcm = lcm_all >> v2_int(lcm_all)
        j = delta - 1
        a_exp = sum(v2_int(3 * i + 4) for i in range(j))
        container = (1 << a_exp) * odd_lcm
        if container % common:
            raise AssertionError(("denominator container", delta))
        kval = k_values[delta]
        if common % kval.denominator:
            raise AssertionError(("K denominator", delta))
        if kval.numerator >= (1 << delta) * common:
            raise AssertionError(("positive height inequality", delta))
        checks += 1
        if delta in {3, 7, 31, delta_max}:
            samples.append(
                {
                    "delta": delta,
                    "common_denominator_bits": common.bit_length(),
                    "reduced_numerator_bits": kval.numerator.bit_length(),
                    "reduced_denominator_bits": kval.denominator.bit_length(),
                }
            )
    return {
        "checks": checks,
        "samples": samples,
        "proved_bound": (
            "log num(K_delta), log den(K_delta) <= "
            "(B_(delta-1)+delta)log2+psi(6delta)=O(delta), "
            "B_j=sum_(i<j)v2(3i+4)"
        ),
    }


def strip_primes_at_most(n: int, bound: int) -> int:
    n = abs(n)
    for p in primes_upto(bound):
        while n % p == 0 and n > 1:
            n //= p
    return n


def gcd_replay(delta_max: int, k_values: list[F]) -> dict[str, Any]:
    consecutive = 0
    odd_distance_two = 0
    samples: list[dict[str, Any]] = []
    for delta in range(1, delta_max):
        g = math.gcd(k_values[delta].numerator, k_values[delta + 1].numerator)
        if strip_primes_at_most(g, 6 * delta + 5) != 1:
            raise AssertionError(("consecutive numerator gcd", delta, g))
        consecutive += 1
    for delta in range(1, delta_max - 1, 2):
        g = math.gcd(k_values[delta].numerator, k_values[delta + 2].numerator)
        if strip_primes_at_most(g, 6 * delta + 5) != 1:
            raise AssertionError(("odd distance-two numerator gcd", delta, g))
        odd_distance_two += 1
        if delta in {1, 3, 7, 31}:
            samples.append({"delta": delta, "gcd_num_K_delta_num_K_delta_plus_2": g})
    return {
        "consecutive_checks": consecutive,
        "actual_odd_distance_two_checks": odd_distance_two,
        "samples": samples,
        "proved_scope": (
            "a common prime divisor of num(K_delta) and num(K_(delta+2)) "
            "is at most 6delta+5"
        ),
    }


def actual_rows_replay(prime_max: int) -> dict[str, Any]:
    primes = [p for p in primes_upto(prime_max) if p >= 11 and p % 6 == 5]
    max_s = max((p - 3) // 6 for p in primes) + 2
    a_values = item251.a_sequence(max_s)
    cache_251: dict[int, dict[str, Any]] = {}
    cache_coeff: dict[int, tuple[list[F], F, F]] = {}
    rows = 0
    localization_checks = 0
    h_zeros: list[dict[str, Any]] = []
    k_numerator_zeros: list[dict[str, Any]] = []
    linear_rows: list[dict[str, Any]] = []
    common_gate_rows: list[dict[str, Any]] = []
    digest = hashlib.sha256()
    witnesses: dict[str, Any] = {}

    for p in primes:
        q = (p - 5) // 6
        h_values, h_sums = prefix_mod(p, q)
        epsilon = 1 if pow(2, (p - 1) // 2, p) == 1 else -1
        for s in range(1, (p - 3) // 6 + 1):
            r = (p - 6 * s - 3) // 2
            if r < 1 or r % 2 == 0:
                continue
            delta = (r + 2) // 3
            if r != 3 * delta - 2 or delta % 2 == 0:
                raise AssertionError(("phase", p, s, r, delta))
            m = s - 1
            if m != q - delta:
                raise AssertionError(("cutoff", p, s, r))
            terms, kval, cdelta = cache_coeff.setdefault(delta, coefficient_data(delta))
            kmod = fmod(kval, p)
            cmod = fmod(cdelta, p)
            pimod = fmod(pi_delta(delta), p)
            dmod = (kmod + cmod * pimod) % p
            pmod = p_correction_mod(p, m, 3 * delta)
            if h_values[m] != cmod * h_values[q] % p or pmod != pimod:
                raise AssertionError(("fixed localization", p, s, r))
            if h_sums[m] != (h_sums[q] - kmod * h_values[q]) % p:
                raise AssertionError(("K coupling", p, s, r))
            original_period = ((-1) ** m) * (
                epsilon * ((h_sums[m] - h_values[m] * pmod) % p) - 1
            )
            localized_period = ((-1) ** m) * (
                epsilon * ((h_sums[q] - dmod * h_values[q]) % p) - 1
            )
            a_mod = a_values[s] % p
            if original_period % p != a_mod or localized_period % p != a_mod:
                raise AssertionError(("Item251 period localization", p, s, r))

            data = cache_251.get(r)
            if data is None:
                data = item251.item250.phase_data(r)
                cache_251[r] = data
            gate = item251.row_invariant(p, s, r, a_values, data)
            hm = h_sums[m]
            row = {
                "p": p,
                "s": s,
                "r": r,
                "m": m,
                "delta": delta,
                "H_m": hm,
                "K_delta": kmod,
                "linear": gate["linear"],
                "g0": gate["g0"],
                "g1": gate["g1"],
            }
            rows += 1
            localization_checks += 4
            digest.update(
                f"{p},{s},{r},{m},{delta},{hm},{kmod},{gate['linear']},{gate['g0']},{gate['g1']}\n".encode(
                    "ascii"
                )
            )
            if hm == 0:
                h_zeros.append(row)
            if kval.numerator % p == 0:
                k_numerator_zeros.append(row)
            if gate["linear"] == 0:
                linear_rows.append(row)
            if gate["g0"] == gate["g1"] == 0:
                common_gate_rows.append(row)
            if (p, s, r) == (47, 5, 7):
                witnesses["H_zero_but_K_numerator_unit"] = row
            if (p, s, r) == (59, 7, 7):
                witnesses["K_numerator_zero_but_H_nonzero"] = row

    if witnesses.get("H_zero_but_K_numerator_unit", {}).get("H_m") != 0:
        raise AssertionError("missing p=47 witness")
    if witnesses.get("K_numerator_zero_but_H_nonzero", {}).get("H_m") == 0:
        raise AssertionError("missing p=59 witness")
    return {
        "prime_max_inclusive": prime_max,
        "actual_p5_rows": rows,
        "localization_equalities": localization_checks,
        "H_zero_count": len(h_zeros),
        "K_numerator_zero_count": len(k_numerator_zeros),
        "linear_affine_locus_count": len(linear_rows),
        "common_gate_count": len(common_gate_rows),
        "H_zero_rows": h_zeros,
        "K_numerator_zero_rows": k_numerator_zeros,
        "linear_rows": linear_rows,
        "common_gate_rows": common_gate_rows,
        "independence_witnesses": witnesses,
        "row_digest_sha256": digest.hexdigest(),
        "role": "EXACT FINITE ONLY",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delta-max", type=int, default=127)
    parser.add_argument("--prime-max", type=int, default=401)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.delta_max < 31 or args.prime_max < 59:
        raise ValueError("bounds too small")

    recurrence = recurrence_and_valuations(args.delta_max)
    k_values = recurrence.pop("K_values")
    height = denominator_height_replay(args.delta_max, k_values)
    gcd_data = gcd_replay(args.delta_max, k_values)
    actual = actual_rows_replay(args.prime_max)

    k3 = k_values[3]
    k7 = k_values[7]
    if k3 != F(59, 14) or k7.numerator != 521 * 9323:
        raise AssertionError("fixed divisor witnesses")

    payload: dict[str, Any] = {
        "schema": "item262-p5-boundary-coefficient-certificate-v1",
        "dependencies": {
            ITEM251_NAME: ITEM251_SHA256,
            ITEM260_REPORT: ITEM260_REPORT_SHA256,
        },
        "proved": {
            "term": "c_j=2^j(5/6)_j/(4/3)_j, c_(j+1)/c_j=(6j+5)/(3j+4)",
            "prefix": "K_delta=sum_(j<delta)c_j, K_0=0, K_1=1",
            "recurrence": (
                "(3delta+4)K_(delta+2)-9(delta+1)K_(delta+1)"
                "+(6delta+5)K_delta=0"
            ),
            "generating_function": (
                "sum_(delta>=0)K_delta z^delta = z/(1-z) "
                "* 2F1(1,5/6;4/3;2z)"
            ),
            "actual_odd_generating_function": (
                "L(t)=[G(sqrt(t))-G(-sqrt(t))]/(2sqrt(t)), L_N=K_(2N+1)"
            ),
            "minimality": (
                "both the full and actual-odd scalar order-two recurrences are minimal: "
                "their Gosper rational equations have no rational solution"
            ),
            "actual_v3": "v3(K_delta)=0 and K_delta=1 mod 3 for every odd delta",
            "denominator_support": (
                "every prime dividing den(K_delta) is at most 3delta-2; "
                "on an actual row p>=6delta+5 the denominator is a p-unit"
            ),
            "fixed_divisor_weight": (
                "for fixed delta, sum_(p|num K_delta) log p <= log|num K_delta|=O(delta)"
            ),
            "localized_Item251_period": (
                "A_s=(-1)^m{epsilon[H_q-D_delta h_q]-1}, "
                "D_delta=K_delta+c_delta Pi_delta, "
                "Pi_delta=sum_(k=1)^(3delta)2^-k(-delta-1/3)_k/(1/2)_k"
            ),
        },
        "minimality_certificate": {
            "full_pole_endpoints": {
                "left": ["1/6"],
                "right": ["-4/3"],
                "integer_separation": False,
            },
            "actual_odd_pole_endpoints": {
                "left": ["13/12", "7/12", "0"],
                "right": ["-2/3", "-7/6", "0"],
                "only_possible_pole": "simple at 0",
                "remaining_ansatz": "R=a/x+b; x^3 and constant force b=1/3,a=-5/99; x^2 contradicts",
            },
        },
        "fixed_prime_divisor_witnesses": {
            "K_3": "59/14",
            "K_7": f"{k7.numerator}/{k7.denominator}",
            "factor_num_K_7": [521, 9323],
        },
        "recurrence_and_valuations": recurrence,
        "denominator_height_replay": height,
        "gcd_replay": gcd_data,
        "actual_rows_replay": actual,
        "booking": {
            "new_unconditional_Route1_rate": 0,
            "new_j2_capacity_reduction": 0,
            "positive_linear_capacity_admission": "FAIL",
            "reason": (
                "K-numerator divisibility is neither necessary nor sufficient for H_m=0; "
                "the fixed-delta O(delta) height sums to O(M^2) over moving delta, above "
                "the raw O(M) cell scale; and the full affine gate retains h_q and row data"
            ),
        },
        "strict_labels": {
            "identities_recurrences_valuation_strata_height_and_gcd_bounds": "PROVED",
            "bounded_counts_samples_and_digests": "EXACT FINITE ONLY",
            "all_prime_H_or_gate_exclusion": "OPEN",
            "new_bookable_rate": 0,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
