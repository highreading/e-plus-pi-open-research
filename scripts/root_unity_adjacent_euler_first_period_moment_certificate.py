#!/usr/bin/env python3
"""Replay the adjacent first-period Euler moment obstruction.

The companion source contains the all-parameter proofs.  This script checks
their normalizations on a declared prime grid and independently replays the
full p=151483 adjacent seed by the primary power sum, its paired moment, and
the secant recurrence modulo p.  Finite checks are not extrapolated to a
product estimate or a classification of e+pi.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "sources/root_unity_adjacent_euler_first_period_moment_obstruction.md"
)
OUTPUT = (
    ROOT
    / "results/root_unity_adjacent_euler_first_period_moment_certificate.json"
)

# This is a failure guard, not a memory allocation and not a Colab RAM cap.
RSS_GUARD_KIB = 8 * 1024 * 1024

DEPENDENCIES = {
    "results/root_unity_adjacent_euler_irregular_seed_hashes.sha256":
        "c4e0b694a4f57130370e1f66869f5d862536e21708a78a0fa1c8655463525f0f",
}

PRIME_GRID = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 43, 61, 101]
SEED_P = 151_483
SEED_N = 1_643


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_u32(values: list[int]) -> str:
    digest = hashlib.sha256()
    for value in values:
        digest.update(int(value).to_bytes(4, "little"))
    return digest.hexdigest()


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    forbidden = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte != 10
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": forbidden,
        "clean": not forbidden,
    }


def peak_rss_kib() -> int:
    for line in Path("/proc/self/status").read_text().splitlines():
        if line.startswith("VmHWM:"):
            fields = line.split()
            assert fields[2] == "kB"
            return int(fields[1])
    raise RuntimeError("VmHWM is unavailable")


def trial_prime(number: int) -> tuple[bool, int]:
    """Deterministic trial-division primality test."""
    if number < 2:
        return False, 1
    if number % 2 == 0:
        return number == 2, 2
    last = 1
    for divisor in range(3, math.isqrt(number) + 1, 2):
        last = divisor
        if number % divisor == 0:
            return False, divisor
    return True, last


def secant_even_exact(max_n: int) -> list[int]:
    """Return E_0,E_2,...,E_{2 max_n} from cosh(t) sech(t)=1."""
    values = [1]
    for n in range(1, max_n + 1):
        values.append(
            -sum(math.comb(2 * n, 2 * k) * values[k] for k in range(n))
        )
    return values


def secant_even_mod(max_n: int, modulus: int) -> list[int]:
    """Modular secant recurrence, valid here because 2 max_n < modulus."""
    assert 2 * max_n < modulus
    factorial = [1] * (2 * max_n + 1)
    for k in range(1, len(factorial)):
        factorial[k] = factorial[k - 1] * k % modulus
    inverse_factorial = [1] * len(factorial)
    inverse_factorial[-1] = pow(factorial[-1], -1, modulus)
    for k in range(len(factorial) - 1, 0, -1):
        inverse_factorial[k - 1] = inverse_factorial[k] * k % modulus

    values = [1]
    for n in range(1, max_n + 1):
        factorial_2n = factorial[2 * n]
        total = 0
        for k in range(n):
            choose = (
                factorial_2n
                * inverse_factorial[2 * k]
                % modulus
                * inverse_factorial[2 * n - 2 * k]
                % modulus
            )
            total = (total + choose * values[k]) % modulus
        values.append((-total) % modulus)
    return values


def support_and_weights(p: int) -> tuple[list[int], list[int]]:
    r = (p - 1) // 2
    support = [pow(2 * j + 1, 2, p) for j in range(r)]
    weights = [(2 if j % 2 == 0 else -2) % p for j in range(r)]
    return support, weights


def paired_moment(
    p: int,
    exponent: int,
    support: list[int] | None = None,
    weights: list[int] | None = None,
) -> int:
    if support is None or weights is None:
        support, weights = support_and_weights(p)
    return sum(
        weight * pow(point, exponent, p)
        for point, weight in zip(support, weights)
    ) % p


def primary_power_sum(p: int, even_half_exponent: int) -> int:
    exponent = 2 * even_half_exponent
    return sum(
        (1 if j % 2 == 0 else -1) * pow(2 * j + 1, exponent, p)
        for j in range(p)
    ) % p


def polynomial_from_roots(roots: list[int], p: int) -> list[int]:
    """Ascending coefficients of the monic polynomial on roots."""
    coefficients = [1]
    for root in roots:
        updated = [0] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            updated[degree] = (
                updated[degree] - root * coefficient
            ) % p
            updated[degree + 1] = (
                updated[degree + 1] + coefficient
            ) % p
        coefficients = updated
    return coefficients


def interpolant_coefficients(
    p: int,
    support: list[int],
    weights: list[int],
) -> list[int]:
    """Fourier inversion on the order-r quadratic-residue group."""
    r = len(support)
    inverse_r = pow(r, -1, p)
    coefficients = []
    for degree in range(r):
        exponent = (-degree) % r
        coefficient = sum(
            weight * pow(point, exponent, p)
            for point, weight in zip(support, weights)
        )
        coefficients.append(inverse_r * coefficient % p)
    return coefficients


def evaluate_polynomial(coefficients: list[int], value: int, p: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % p
    return result


def cyclic_product(
    left: list[int],
    right: list[int],
    p: int,
) -> list[int]:
    """Product modulo X^r-1 in ascending coordinates."""
    assert len(left) == len(right)
    r = len(left)
    output = [0] * r
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[(i + j) % r] = (
                output[(i + j) % r] + a * b
            ) % p
    return output


def determinant_mod(matrix: list[list[int]], p: int) -> int:
    work = [row[:] for row in matrix]
    dimension = len(work)
    determinant = 1
    for column in range(dimension):
        pivot = next(
            (row for row in range(column, dimension)
             if work[row][column] % p),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column] % p
        determinant = determinant * pivot_value % p
        inverse_pivot = pow(pivot_value, -1, p)
        for row in range(column + 1, dimension):
            multiplier = work[row][column] * inverse_pivot % p
            if multiplier:
                for j in range(column, dimension):
                    work[row][j] = (
                        work[row][j] - multiplier * work[column][j]
                    ) % p
    return determinant % p


def vandermonde_product(points: list[int], p: int) -> int:
    result = 1
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            result = result * (points[j] - points[i]) % p
    return result


def audit_prime(p: int) -> dict[str, object]:
    prime, _ = trial_prime(p)
    assert prime and p % 2 == 1
    r = (p - 1) // 2
    support, weights = support_and_weights(p)

    assert len(set(support)) == r
    quadratic_residues = {pow(value, 2, p) for value in range(1, p)}
    assert set(support) == quadratic_residues
    assert all(weight for weight in weights)

    root_polynomial = polynomial_from_roots(support, p)
    expected_root_polynomial = [p - 1] + [0] * (r - 1) + [1]
    assert root_polynomial == expected_root_polynomial

    euler_period = secant_even_mod(r, p) if 2 * r < p else None
    # Here 2r=p-1, so the modular recurrence is valid.
    assert euler_period is not None
    max_test_exponent = min(r + 3, 14)
    euler_short = secant_even_exact(max_test_exponent)
    normalization_rows = []
    for n in range(1, max_test_exponent + 1):
        paired = paired_moment(p, n, support, weights)
        unpaired = primary_power_sum(p, n)
        recurrence_value = euler_short[n] % p
        assert paired == unpaired == recurrence_value
        assert paired_moment(p, n + r, support, weights) == paired
        normalization_rows.append(
            {
                "n": n,
                "E_2n_mod_p": recurrence_value,
                "paired_moment": paired,
                "primary_full_sum": unpaired,
            }
        )

    coefficients = interpolant_coefficients(p, support, weights)
    assert all(
        evaluate_polynomial(coefficients, point, p) == weight
        for point, weight in zip(support, weights)
    )
    square = cyclic_product(coefficients, coefficients, p)
    assert square == [4 % p] + [0] * (r - 1)
    assert coefficients[-1] == 2 % p
    assert max(index for index, value in enumerate(coefficients) if value) == r - 1

    explicit_from_euler = [0] * r
    for k in range(1, r + 1):
        explicit_from_euler[r - k] = -2 * euler_period[k] % p
    assert coefficients == explicit_from_euler

    determinant_rows = []
    if p <= 31:
        for shift in (0, 1, 3):
            hankel = [
                [
                    paired_moment(p, shift + a + b, support, weights)
                    for b in range(r)
                ]
                for a in range(r)
            ]
            direct_determinant = determinant_mod(hankel, p)
            vandermonde = vandermonde_product(support, p)
            diagonal_product = math.prod(
                weight * pow(point, shift, p)
                for point, weight in zip(support, weights)
            ) % p
            factored_determinant = (
                diagonal_product * vandermonde * vandermonde
            ) % p
            assert direct_determinant == factored_determinant != 0
            determinant_rows.append(
                {
                    "shift": shift,
                    "direct": direct_determinant,
                    "factored": factored_determinant,
                    "nonzero": True,
                }
            )

    return {
        "p": p,
        "r": r,
        "support_is_exactly_QR": True,
        "all_weights_nonzero": True,
        "root_polynomial": f"Z^{r}-1",
        "minimal_constant_coefficient_recurrence_order": r,
        "interpolant_degree": r - 1,
        "half_degree_lower_bound": (r + 1) // 2,
        "interpolant_leading_coefficient": coefficients[-1],
        "interpolant_sha256_u32le": sha256_u32(coefficients),
        "cyclic_square_is_4": True,
        "normalization_rows": normalization_rows,
        "hankel_determinants": determinant_rows,
    }


def endpoint_audit(max_n: int) -> list[dict[str, object]]:
    rows = []
    for n in range(1, max_n + 1):
        p = 2 * n + 3
        prime, _ = trial_prime(p)
        if not prime:
            continue
        r = n + 1
        euler = secant_even_mod(r, p)
        actual_pair = euler[n] == 0 and euler[n + 1] == 0
        criterion = p % 4 == 1 and euler[n] == 0
        assert euler[r] == (1 - (-1) ** r) % p
        assert actual_pair == criterion
        rows.append(
            {
                "N": n,
                "p": p,
                "p_mod_4": p % 4,
                "E_p_minus_3_mod_p": euler[n],
                "E_p_minus_1_mod_p": euler[r],
                "simultaneous_divisibility": actual_pair,
                "endpoint_criterion": criterion,
            }
        )
    return rows


def seed_audit() -> dict[str, object]:
    p = SEED_P
    n = SEED_N
    prime, last_trial_divisor = trial_prime(p)
    assert prime
    r = (p - 1) // 2
    assert p > 2 * n + 3
    assert r >= n + 2

    support, weights = support_and_weights(p)
    assert len(set(support)) == r
    assert all(weights)

    moments = {
        str(exponent): paired_moment(p, exponent, support, weights)
        for exponent in (1, n, n + 1)
    }
    full_sums = {
        str(exponent): primary_power_sum(p, exponent)
        for exponent in (n, n + 1)
    }
    assert moments["1"] == p - 1
    assert moments[str(n)] == moments[str(n + 1)] == 0
    assert full_sums[str(n)] == full_sums[str(n + 1)] == 0

    recurrence = secant_even_mod(n + 1, p)
    assert recurrence[1] == p - 1
    assert recurrence[n] == recurrence[n + 1] == 0
    assert moments[str(n)] == recurrence[n]
    assert moments[str(n + 1)] == recurrence[n + 1]

    inverse_r = pow(r, -1, p)
    top_coefficient = inverse_r * moments["1"] % p
    assert inverse_r == p - 2
    assert top_coefficient == 2
    assert p % 4 == 3 and r % 2 == 1

    return {
        "N": n,
        "p": p,
        "p_is_prime_by_trial_division": True,
        "last_odd_trial_divisor": last_trial_divisor,
        "r": r,
        "p_greater_than_2N_plus_3": True,
        "support_size": len(support),
        "distinct_support_size": len(set(support)),
        "support_sha256_u32le": sha256_u32(support),
        "weights_sha256_u32le": sha256_u32(weights),
        "paired_moments": moments,
        "primary_full_power_sums": full_sums,
        "secant_recurrence": {
            "E_2_mod_p": recurrence[1],
            "E_3286_mod_p": recurrence[n],
            "E_3288_mod_p": recurrence[n + 1],
        },
        "interpolant": {
            "exact_degree_from_all_parameter_theorem": r - 1,
            "half_degree_lower_bound": (r + 1) // 2,
            "leading_coefficient": top_coefficient,
            "zero_coefficient_exponents": [r - n, r - n - 1],
        },
        "minimal_constant_coefficient_recurrence_order": r,
        "full_hankel_dimension": r,
        "p_mod_4": p % 4,
        "QR_group_order_is_odd": True,
        "normalized_alternating_weights_are_not_a_multiplicative_character":
            True,
    }


def main() -> None:
    started = time.perf_counter()

    dependency_checks = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependency_checks[relative] = {
            "expected": expected,
            "actual": actual,
        }

    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__))
    assert source_control["clean"] and script_control["clean"]

    grid_rows = [audit_prime(p) for p in PRIME_GRID]
    endpoint_rows = endpoint_audit(80)
    seed = seed_audit()

    payload = {
        "schema":
            "root_unity_adjacent_euler_first_period_moment_certificate_v1",
        "logical_scope": (
            "Exact finite replay for the normalization and the p=151483 seed "
            "of an all-prime moment-complexity obstruction. It proves no "
            "upper bound for the adjacent first-period prime product and "
            "does not classify e+pi."
        ),
        "all_parameter_theorem": {
            "paired_power_sum": (
                "E_(2n) = sum_{j=0}^{r-1} 2(-1)^j "
                "((2j+1)^2)^n mod p for n>=1 and r=(p-1)/2"
            ),
            "support": (
                "The points (2j+1)^2 are exactly the r distinct nonzero "
                "quadratic residues and all weights are nonzero."
            ),
            "minimal_recurrence": (
                "The minimal constant-coefficient recurrence has order r "
                "and characteristic polynomial Z^r-1."
            ),
            "interpolant": (
                "W_p=-2 sum_{k=1}^r E_(2k) X^(r-k), "
                "deg W_p=r-1, and W_p^2=4 mod X^r-1."
            ),
            "hankel": (
                "Every full r by r moment Hankel determinant factors as a "
                "nonzero weighted Vandermonde square."
            ),
            "scope_boundary": (
                "These statements obstruct the canonical bounded-degree "
                "linear-recurrence, interpolation, and rank routes only; "
                "they do not exclude nonlinear or other arithmetic coupling."
            ),
        },
        "primary_reference": {
            "authors": "J. B. Cosgrave and K. Dilcher",
            "title": "On a congruence of Emma Lehmer related to Euler numbers",
            "journal": "Acta Arith. 161 (2013), 47-67",
            "url":
                "https://www.impan.pl/shop/publication/transaction/download/product/82378",
            "equation": "2.3",
        },
        "prime_grid": PRIME_GRID,
        "grid_rows": grid_rows,
        "endpoint_rows_through_N_80": endpoint_rows,
        "seed": seed,
        "dependency_checks": dependency_checks,
        "source_sha256": sha256(SOURCE),
        "control_audit": {
            "source": source_control,
            "script": script_control,
        },
        "resource_policy": {
            "RSS_guard_kib": RSS_GUARD_KIB,
            "meaning": (
                "Failure guard only; it neither allocates nor limits the "
                "approximately 50 GiB available Colab RAM."
            ),
            "hardware_accelerator": (
                "Not used: exact modular scalar arithmetic is CPU-suitable, "
                "and the replay is small."
            ),
        },
        "missing_lemma": (
            "A global coupling across the deterministic W_p as p varies, "
            "strong enough to prove sum log p=o(N log N) over strict "
            "adjacent first-period primes; none of the certified identities "
            "supplies such a bound."
        ),
    }

    measured_peak = peak_rss_kib()
    assert measured_peak < RSS_GUARD_KIB

    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUTPUT.write_bytes(encoded)
    elapsed = time.perf_counter() - started
    print(f"wrote {OUTPUT}")
    print(f"sha256 {hashlib.sha256(encoded).hexdigest()}")
    print(f"elapsed_seconds {elapsed:.6f}")
    print(f"peak_rss_kib {measured_peak}")


if __name__ == "__main__":
    main()
