#!/usr/bin/env python3
"""Deterministic certificate for work Item 415.

The uniform proofs are in the companion report.  This checker pins the
dependencies, evaluates the two exact residue integers, verifies the
compulsory prime strip on transparent finite normalization rows, and checks
the tied q == 1 (mod 6) Frobenius bookkeeping.  No finite row is promoted to
a zero-density or noncollision theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STEM = "item415_marked_selector_compulsory_strip"
MAX_M = 160
SELECTED_M = {1, 2, 3, 4, 10, 20, 40, 80, 120, 160}

DEPENDENCIES = {
    "sources/item200_common_log_gcd_report.md":
        "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "results/item200_common_log_gcd_certificate.json":
        "5fd9f62b82d92dde6755919ef0e44d5d42a3c9452acfc3bbe3d3ee96f7326f82",
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "sources/item393_mixed_cubic_small_prime_strata_ceiling_report.md":
        "5e2c92f87075cbe3ac8af3191d8df7485ac6efd13609ede5f82819e355ae5f96",
    "sources/item396_fixed_gap_resultant_3adic_report.md":
        "7355b6909994357583f799e627e1ff19edb230a6a9002ee845be585057726aca",
    "sources/item406_mixed_cubic_actual_adjacent_recurrence_report.md":
        "a9c33967b42f5ae09c2c0c71de1b956ca240e49c367be46f3af2878cd96cbb83",
    "sources/item411_mixed_primitive_boundary_transport_report.md":
        "9061f8088ea2bb403065a9192bc947c1a36299ee0ab6893caa0fd134a2f72f4f",
    "sources/item412_marked_cubic_frobenius_selector_boundary_report.md":
        "cbf2fa9216c2037e54fe6ac440039b3a8773ed2e173a6576f75070b6e0512299",
    "results/item412_marked_cubic_frobenius_selector_boundary_certificate.json":
        "50231958f02f7fcf3401ded1a5ca60a5ebe563eadf57e320fb08a4625ca5057a",
    "manifests/item412_marked_cubic_frobenius_selector_boundary_manifest.json":
        "e95b2505b097df5ce3267bc92ac3c79c758f2a33153bdd5b7b9c4fa85a437143",
}

TIED_ROWS = (
    (1, 13),
    (1, 19),
    (2, 19),
    (2, 31),
    (3, 37),
    (10, 67),
    (10, 73),
    (20, 127),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_dependencies() -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        digest = sha256_bytes((ROOT / relative).read_bytes())
        assert digest == expected, (relative, expected, digest)
        observed[relative] = digest
    return observed


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


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


ALL_PRIMES = primes_up_to(6 * MAX_M)


def numerator_zero(m_value: int, degree: int) -> int:
    first = (
        (-1) ** degree * math.comb(6 * m_value, degree)
        if 0 <= degree <= 6 * m_value
        else 0
    )
    second = (
        (-1) ** (degree - 1) * math.comb(6 * m_value, degree - 1)
        if 1 <= degree <= 6 * m_value + 1
        else 0
    )
    return first + second


def numerator_one(m_value: int, degree: int) -> int:
    total = 0
    for shift in range(5):
        source = degree - shift
        if 0 <= source <= 6 * m_value:
            total += (
                math.comb(4, shift)
                * (-1) ** source
                * math.comb(6 * m_value, source)
            )
    return total


def residue_integers(m_value: int) -> tuple[int, int]:
    """The exact Item-390 integers lambda_0,m and lambda_1,m."""
    target_zero = 4 * m_value
    lambda_zero = 0
    for numerator_degree in range(target_zero + 1):
        remainder = target_zero - numerator_degree
        if remainder % 2 == 0:
            half = remainder // 2
            lambda_zero += (
                numerator_zero(m_value, numerator_degree)
                * (-1) ** half
                * math.comb(4 * m_value + half, half)
            )

    target_one = 4 * m_value + 1
    lambda_one = 0
    for numerator_degree in range(target_one + 1):
        remainder = target_one - numerator_degree
        if remainder % 2 == 0:
            half = remainder // 2
            lambda_one += (
                numerator_one(m_value, numerator_degree)
                * (-1) ** half
                * math.comb(4 * m_value + 1 + half, half)
            )
    return lambda_zero, lambda_one


def compulsory_primes(m_value: int) -> list[int]:
    return [
        prime for prime in ALL_PRIMES
        if 4 * m_value + 1 < prime < 6 * m_value
    ]


def compulsory_product(m_value: int) -> int:
    return math.prod(compulsory_primes(m_value))


def cartier_defect(modulus: int, numerator_degree: int, pole_order: int) -> int:
    remainder = numerator_degree % modulus
    target = pole_order % modulus
    if target == 0:
        return 2 * remainder
    return 2 * remainder + 3 * (modulus - target)


def full_rank_zero_primes(m_value: int) -> list[int]:
    """Canonical Item-200 rank-zero set P_m."""
    answer = []
    for prime in ALL_PRIMES:
        if prime == 2:
            continue
        if (
            cartier_defect(prime, 6 * m_value, 4 * m_value + 1) <= prime - 2
            and cartier_defect(prime, 6 * m_value, 4 * m_value + 2) <= prime - 2
        ):
            answer.append(prime)
    return answer


def tied_selector_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for m_value, prime in TIED_ROWS:
        assert is_prime(prime) and prime > 6 * m_value
        q_value = prime - 6 * m_value
        assert q_value >= 7 and q_value % 6 == 1
        d_value = (q_value - 1) // 2
        assert d_value % 3 == 0
        h_value = d_value // 3
        n_value = 2 * d_value
        phase = n_value % 4
        assert phase == 2 * (h_value % 2)
        assert prime == 6 * (m_value + h_value) + 1
        assert prime % 18 == (1, 7, 13)[(m_value + h_value) % 3]

        t_value = (prime - 1) // 3
        x_value = pow(16, h_value, prime)
        chi_two = pow(2, t_value, prime)
        selected = pow(2, 2 * m_value + q_value - 1, prime)
        assert selected == x_value * chi_two % prime
        assert pow(chi_two, 3, prime) == 1
        rows.append({
            "m": m_value,
            "p": prime,
            "q=2d+1": q_value,
            "d": d_value,
            "h=d/3": h_value,
            "phase_n_mod_4": phase,
            "p_mod_18": prime % 18,
            "chi_p(2)": chi_two,
            "selected_root": selected,
            "selected_rational_stratum": (
                "linear" if chi_two == 1 else "quadratic"
            ),
            "normalization_only_not_support_evidence": True,
        })
    return rows


def strip_normalization() -> dict[str, object]:
    selected_rows: list[dict[str, object]] = []
    stream: list[str] = []
    total_interval_primes = 0

    for m_value in range(1, MAX_M + 1):
        lambda_zero, lambda_one = residue_integers(m_value)
        strip_primes = compulsory_primes(m_value)
        strip_product = math.prod(strip_primes)
        full_primes = full_rank_zero_primes(m_value)
        full_product = math.prod(full_primes)
        assert set(strip_primes) <= set(full_primes)
        assert lambda_zero % strip_product == 0
        assert lambda_one % strip_product == 0
        # The uniform full-product theorem is inherited from canonical
        # Item 200; these rows are an independent finite normalization.
        assert lambda_zero % full_product == 0
        assert lambda_one % full_product == 0
        mu_zero = lambda_zero // full_product
        mu_one = lambda_one // full_product

        # The displayed polynomial-degree proof, normalized prime by prime.
        for prime in strip_primes:
            a_value = 6 * m_value - prime
            b_value = prime - 4 * m_value - 1
            assert 0 < a_value < 2 * m_value - 1
            assert b_value >= 2
            degree_zero = a_value + 1 + 2 * b_value
            degree_one = a_value + 4 + 2 * (b_value - 1)
            assert degree_zero == prime - 2 * m_value - 1 < 4 * m_value
            assert degree_one == prime - 2 * m_value < 4 * m_value + 1
            assert lambda_zero % prime == 0
            assert lambda_one % prime == 0
            total_interval_primes += 1

        # An integral marked-basis transform.  Its determinant is
        # -2(4m+1), hence it is p-adically invertible for every p>6m.
        marked_zero = (
            2 * (5 * m_value + 1) * lambda_zero
            - (4 * m_value + 1) * lambda_one
        )
        marked_one = (
            (4 * m_value + 1) * lambda_one
            - 2 * (5 * m_value + 2) * lambda_zero
        )
        assert marked_zero + marked_one == -2 * lambda_zero
        determinant = -2 * (4 * m_value + 1)
        assert abs(determinant) < 2 * (6 * m_value + 1)
        assert marked_zero % full_product == 0
        assert marked_one % full_product == 0

        stream.append(
            ":".join(map(str, (
                m_value,
                lambda_zero,
                lambda_one,
                strip_product,
                full_product,
                mu_zero,
                mu_one,
                marked_zero,
                marked_one,
            )))
        )
        if m_value in SELECTED_M:
            selected_rows.append({
                "m": m_value,
                "interval_prime_count": len(strip_primes),
                "interval_primes": strip_primes,
                "interval_subproduct_D_m": str(strip_product),
                "full_rank_zero_prime_count": len(full_primes),
                "full_Item200_product_F_m": str(full_product),
                "lambda_0_bit_length": abs(lambda_zero).bit_length(),
                "lambda_1_bit_length": abs(lambda_one).bit_length(),
                "mu_0_bit_length": abs(mu_zero).bit_length(),
                "mu_1_bit_length": abs(mu_one).bit_length(),
                "divisibility_verified": True,
                "finite_normalization_only": True,
            })

    return {
        "range": f"1<=m<={MAX_M}",
        "rows": MAX_M,
        "interval_prime_incidents_checked": total_interval_primes,
        "selected_rows": selected_rows,
        "strip_stream_sha256": sha256_bytes("\n".join(stream).encode("ascii")),
        "uniform_proof_location": "companion report, polynomial truncation theorem",
    }


def capacity_record() -> dict[str, object]:
    getcontext().prec = 60
    old_ceiling = Decimal(136).ln() / Decimal(6)
    pi_value = Decimal(
        "3.14159265358979323846264338327950288419716939937510582097494"
    )
    forced_rate_per_m = (
        -Decimal(4) * Decimal(2).ln()
        + pi_value / Decimal(3).sqrt()
        + Decimal(3) * Decimal(3).ln()
    )
    new_ceiling = (Decimal(136).ln() - forced_rate_per_m) / Decimal(6)
    improvement = old_ceiling - new_ceiling
    assert abs(improvement - forced_rate_per_m / Decimal(6)) < Decimal("1e-58")
    return {
        "old_strictly_large_component_ceiling": str(old_ceiling),
        "interval_subproduct_rate_in_log_D_m_per_m": "2",
        "full_Item200_forced_rate_in_log_F_m_per_m": str(forced_rate_per_m),
        "new_strictly_large_component_ceiling": str(new_ceiling),
        "component_ceiling_improvement": str(improvement),
        "booking_delta": 0,
        "global_total_content_ceiling_delta": 0,
        "weighted_zero_density_proved": False,
    }


def build_certificate() -> dict[str, object]:
    dependencies = verify_dependencies()
    tied_rows = tied_selector_rows()
    strip = strip_normalization()
    capacity = capacity_record()
    witness = json.dumps(
        {"tied_rows": tied_rows, "strip": strip, "capacity": capacity},
        sort_keys=True,
        separators=(",", ":"),
    ).encode("ascii")
    return {
        "schema": "item415-marked-selector-compulsory-strip-v2",
        "item": 415,
        "status": "CANONICAL_ROOT_AUDITED_COMPONENT_CEILING_REDUCED_NO_BOOKING",
        "dependency_sha256": dependencies,
        "tied_q_equals_1_mod_6_selector_rows": tied_rows,
        "compulsory_interval_strip_normalization": strip,
        "capacity": capacity,
        "theorems_proved_in_report": {
            "tied_congruences": (
                "q=2d+1 is 1 mod 6 iff d=3h; then p=6(m+h)+1, "
                "n mod 4=2(h mod 2), and the mark is 16^h*2^((p-1)/3)"
            ),
            "compulsory_strip": (
                "canonical Item200 proves its full F_m=G_m divides both exact "
                "residue integers; the report independently rederives the "
                "interval subproduct 4m+1<ell<6m"
            ),
            "all_depth_reduction": (
                "dividing both residues by the full Item200 F_m preserves every p>6m "
                "valuation and hence the exact strictly-large carrier"
            ),
            "capacity": (
                "the strictly-large component ceiling is at most "
                "(log(136)-C_F)/6, where C_F=-4log2+pi/sqrt3+3log3"
            ),
        },
        "labels": {
            "PROVED": [
                "exact tied congruence and Frobenius-mark bookkeeping",
                "independent interval-prime proof of the j=0 part of canonical Item200",
                "new synthesis of the full Item200 normalization with Item390 all-depth height",
                "all-depth stripped residue carrier for p>6m",
                "strictly-large component ceiling improvement by C_F/6",
                "zero booking and no global total-ceiling subtraction",
            ],
            "OPEN": [
                "valuation-weighted o(m) for the stripped carrier",
                "selected-branch zero density inside p=1 mod 6",
                "uniform noncollision and c_m^>=1",
                "Route 1 and irrationality of e+pi",
            ],
            "NOT_CLAIMED": [
                "Chebotarev distribution for moving carrier divisors",
                "an actual wrong-branch prime",
                "finite normalization implies noncollision",
                "a positive Route-1 divisor booking",
            ],
        },
        "witness_sha256": sha256_bytes(witness),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=HERE / f"{STEM}_certificate.json"
    )
    parser.add_argument(
        "--replay",
        type=Path,
        help="Optional certificate whose bytes must equal the generated payload.",
    )
    args = parser.parse_args()
    certificate = build_certificate()
    payload = (json.dumps(certificate, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if args.replay is not None:
        assert args.replay.read_bytes() == payload
    args.output.write_bytes(payload)


if __name__ == "__main__":
    main()
