#!/usr/bin/env python3
"""Exact certificate for the quadratic Euler-gcd Kummer obstruction.

The companion source contains the all-parameter proofs.  This replay checks
finite algebraic identities and the advertised counterexamples without using
the grid as a classification theorem.  It checks

* the secant-Euler recurrence through N=1000;
* G_N = H_N*gcd(A_N,E_{2N+2}/H_N) and the exact sandwich;
* the prime-power Kummer formula on an explicit grid;
* reduction to the positive fundamental Kummer representative;
* the complete mod-p endpoint criterion;
* the recurring factors 149 and 241;
* the S_N,J_N split and the lcm divisibility on the exact grid; and
* the centered Euler-polynomial/resultant normalization for small N.

The JSON is deterministic.  Elapsed time and peak RSS are printed but are not
stored.  No finite computation is used to classify e+pi or all Euler-irregular
pairs.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from pathlib import Path

import sympy as sp


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "root_unity_quadratic_euler_gcd_kummer_certificate.json"
RSS_LIMIT_KIB = 2 * 1024 * 1024
N_MAX = 1000
TABLE_MAX = 1100


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def peak_rss_kib() -> int:
    """Read this process's high-water RSS, avoiding pre-exec rusage history."""
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def digest_rows(rows: list[list[int]]) -> str:
    payload = "".join(
        f"{len(row)}:" + ",".join(str(value) for value in row) + "\n"
        for row in rows
    )
    return sha256_bytes(payload.encode())


def euler_half_table(max_half_index: int) -> list[int]:
    """Return [E_0,E_2,...,E_{2*max_half_index}] exactly."""
    values = [1]
    for n in range(1, max_half_index + 1):
        total = 0
        choose = 1
        for k in range(n):
            total += choose * values[k]
            choose = (
                choose
                * (2 * n - 2 * k)
                * (2 * n - 2 * k - 1)
                // ((2 * k + 1) * (2 * k + 2))
            )
        values.append(-total)
        assert values[-1] % 2
        assert (values[-1] > 0) == (n % 2 == 0)
    return values


def factor_dict(value: int) -> dict[str, int]:
    return {str(int(p)): int(a) for p, a in sp.factorint(abs(value)).items()}


def fundamental_even(index: int, modulus: int) -> int:
    assert index > 0 and index % 2 == 0
    assert modulus > 0 and modulus % 2 == 0
    residue = index % modulus
    return modulus if residue == 0 else residue


def kummer_depth_bound(p: int, X: int) -> int:
    assert p >= 3 and sp.isprime(p)
    a = 0
    phi = p - 1
    while phi <= X:
        a += 1
        phi *= p
    return a


def lcm_upto(limit: int) -> int:
    value = 1
    for p in sp.primerange(2, limit + 1):
        power = int(p)
        while power * p <= limit:
            power *= int(p)
        value *= power
    return value


def split_h(H: int, N: int) -> tuple[int, int, list[dict]]:
    X = 2 * N + 2
    S = 1
    layers: list[dict] = []
    for p_sp, valuation in sp.factorint(H).items():
        p = int(p_sp)
        depth = kummer_depth_bound(p, X)
        small_valuation = min(int(valuation), depth)
        S *= p**small_valuation
        layers.append(
            {
                "p": p,
                "valuation": int(valuation),
                "period_depth": depth,
                "small_valuation": small_valuation,
                "excess_valuation": int(valuation) - small_valuation,
            }
        )
    assert H % S == 0
    return S, H // S, layers


def centered_euler_polynomial(m: int, T: sp.Symbol, half: list[int]) -> sp.Poly:
    assert m % 2 == 0
    expression = sum(
        sp.binomial(m, j) * (half[j // 2] if j % 2 == 0 else 0) * T ** (m - j)
        for j in range(m + 1)
    )
    polynomial = sp.Poly(expression, T, domain=sp.ZZ)
    assert polynomial.eval(0) == half[m // 2]
    assert polynomial.eval(1) == 0
    assert polynomial.eval(-1) == 0
    return polynomial


def resultant_rows(half: list[int]) -> list[dict]:
    T = sp.symbols("T")
    rows: list[dict] = []
    for N in range(1, 9):
        low = centered_euler_polynomial(2 * N, T, half)
        high = centered_euler_polynomial(2 * N + 2, T, half)
        divisor = sp.Poly(T * T - 1, T, domain=sp.ZZ)
        low_q, low_r = sp.div(low, divisor, domain=sp.ZZ)
        high_q, high_r = sp.div(high, divisor, domain=sp.ZZ)
        assert low_r.is_zero and high_r.is_zero
        assert int(low_q.eval(0)) == -half[N]
        assert int(high_q.eval(0)) == -half[N + 1]
        resultant = abs(int(sp.resultant(low_q.as_expr(), high_q.as_expr(), T)))
        assert resultant > 0
        v2 = 0
        odd_part = resultant
        while odd_part % 2 == 0:
            odd_part //= 2
            v2 += 1
        odd_root = math.isqrt(odd_part)
        assert odd_root * odd_root == odd_part
        assert v2 == 4 * N * (N - 1)
        H = math.gcd(abs(half[N]), abs(half[N + 1]))
        assert resultant % H == 0
        rows.append(
            {
                "N": N,
                "resultant_bits": resultant.bit_length(),
                "v2_resultant": v2,
                "odd_square_root": str(odd_root),
                "sha256_decimal_resultant": sha256_bytes(str(resultant).encode()),
            }
        )
    return rows


def main() -> None:
    started = time.perf_counter()
    half = euler_half_table(TABLE_MAX)

    exact_rows: list[list[int]] = []
    nontrivial_H: list[dict] = []
    easy_quotient_primes: set[int] = set()
    split_rows: list[dict] = []
    maximum_lcm_limit = 3 * N_MAX + 3
    global_lcm = lcm_upto(maximum_lcm_limit)

    for N in range(1, N_MAX + 1):
        e0 = abs(half[N])
        e1 = abs(half[N + 1])
        A = (2 * N + 2) * (2 * N + 1)
        H = math.gcd(e0, e1)
        G = math.gcd(A * e0, e1)
        quotient = math.gcd(A, e1 // H)
        assert G == H * quotient
        assert G % H == 0 and A * H % G == 0
        S, J, layers = split_h(H, N)
        assert H == S * J
        assert global_lcm % S == 0
        # Stronger pointwise check, without constructing every pointwise lcm.
        for layer in layers:
            if layer["small_valuation"]:
                assert (
                    layer["p"] ** layer["small_valuation"] <= 3 * N + 3
                )
        if H > 1:
            nontrivial_H.append(
                {
                    "N": N,
                    "H_factorization": factor_dict(H),
                    "G_factorization": factor_dict(G),
                    "S": S,
                    "J": J,
                    "layers": layers,
                }
            )
            split_rows.append(
                {
                    "N": N,
                    "H": H,
                    "S": S,
                    "J": J,
                }
            )
        easy_quotient_primes.update(int(p) for p in sp.factorint(quotient))
        exact_rows.append([N, H, G, quotient, S, J])

    assert nontrivial_H
    assert {int(p) for row in nontrivial_H for p in row["H_factorization"]} == {
        149,
        241,
    }
    assert all(row["J"] == 1 for row in nontrivial_H)

    # Explicit counterexamples and periodic repeats.
    expected_H = {
        73: 149,
        119: 241,
        147: 149,
        221: 149,
        239: 241,
        295: 149,
        359: 241,
    }
    for N, expected in expected_H.items():
        assert math.gcd(abs(half[N]), abs(half[N + 1])) == expected
    assert (147 - 73) == (149 - 1) // 2
    assert (239 - 119) == (241 - 1) // 2

    # Prime-power Kummer formula (13) on a declared finite grid.
    kummer_rows: list[list[int]] = []
    for p in [3, 5, 7, 11, 13]:
        epsilon = (-1) ** ((p - 1) // 2)
        for a in [1, 2, 3]:
            modulus = p**a
            phi = int(sp.totient(modulus))
            for k in range(1, 13):
                target_half = (phi + 2 * k) // 2
                assert target_half < len(half)
                lhs = half[target_half] % modulus
                rhs = ((1 - epsilon * p ** (2 * k)) * half[k]) % modulus
                assert lhs == rhs
                assert math.gcd(1 - epsilon * p ** (2 * k), p) == 1
                assert (lhs == 0) == (half[k] % modulus == 0)
                kummer_rows.append([p, a, k, lhs, rhs])

    # Exact fundamental-representative criterion over a broader finite grid.
    representative_rows: list[list[int]] = []
    for p_sp in list(sp.primerange(3, 50)):
        p = int(p_sp)
        for a in [1, 2]:
            modulus = p**a
            phi = int(sp.totient(modulus))
            if phi > 2 * N_MAX:
                continue
            for N in range(1, min(N_MAX, 3 * phi) + 1):
                r = fundamental_even(2 * N, phi)
                common_actual = half[N] % modulus == 0 and half[N + 1] % modulus == 0
                if r == phi:
                    common_seed = False
                else:
                    common_seed = (
                        half[r // 2] % modulus == 0
                        and half[(r + 2) // 2] % modulus == 0
                    )
                assert common_actual == common_seed
                representative_rows.append(
                    [p, a, N, r, int(common_actual), int(common_seed)]
                )

    # Boundary formula E_{p-1} = 1-(-1)^((p-1)/2) mod p, and endpoint seeds.
    endpoint_seeds: list[dict] = []
    interior_adjacent_pairs: list[dict] = []
    for p_sp in sp.primerange(3, 1000):
        p = int(p_sp)
        assert half[(p - 1) // 2] % p == (1 - (-1) ** ((p - 1) // 2)) % p
        if p % 4 == 1 and half[(p - 3) // 2] % p == 0:
            endpoint_seeds.append({"p": p, "N": (p - 3) // 2})
        for r in range(2, p - 3, 2):
            if half[r // 2] % p == 0 and half[(r + 2) // 2] % p == 0:
                interior_adjacent_pairs.append({"p": p, "r": r})
    assert endpoint_seeds == [{"p": 149, "N": 73}, {"p": 241, "N": 119}]
    # A finite null result is recorded only as a diagnostic, never extrapolated.
    assert interior_adjacent_pairs == []

    resultants = resultant_rows(half)

    payload = {
        "schema": "root_unity_quadratic_euler_gcd_kummer_certificate_v1",
        "logical_scope": (
            "Exact finite replay of recurrence, factor separation, Kummer formula, "
            "representative reduction, endpoint examples, lcm split, and small "
            "resultants. Finite grids do not classify adjacent Euler-irregular pairs "
            "or e+pi."
        ),
        "grid": {
            "N_max": N_MAX,
            "Euler_half_table_max": TABLE_MAX,
            "kummer_primes": [3, 5, 7, 11, 13],
            "kummer_prime_power_exponents": [1, 2, 3],
            "kummer_k_max": 12,
            "representative_primes_below": 50,
            "endpoint_and_interior_scan_primes_below": 1000,
            "resultant_N_max": 8,
        },
        "theorem_identity": {
            "factor_separation": "G_N=H_N*gcd(A_N,abs(E_{2N+2})/H_N)",
            "sandwich": "H_N divides G_N divides A_N*H_N",
            "periodic_split": "H_N=S_N*J_N and S_N divides lcm(1,...,3N+3)",
            "asymptotic_reduction": "log(G_N)=log(J_N)+O(N)",
        },
        "exact_grid_digest": digest_rows(exact_rows),
        "kummer_grid_digest": digest_rows(kummer_rows),
        "representative_grid_digest": digest_rows(representative_rows),
        "nontrivial_H_rows": nontrivial_H,
        "split_rows": split_rows,
        "easy_quotient_primes_seen": sorted(easy_quotient_primes),
        "explicit_counterexamples": {
            str(N): expected for N, expected in expected_H.items()
        },
        "endpoint_seeds_below_1000": endpoint_seeds,
        "interior_adjacent_pairs_below_1000": interior_adjacent_pairs,
        "small_centered_resultants": resultants,
        "euler_table_digest": digest_rows(
            [[n, half[n]] for n in range(len(half))]
        ),
    }

    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    measured_peak_rss_kib = peak_rss_kib()
    assert measured_peak_rss_kib < RSS_LIMIT_KIB
    OUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUT}")
    print(f"sha256 {sha256_bytes(encoded)}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak_rss_kib}")


if __name__ == "__main__":
    main()
