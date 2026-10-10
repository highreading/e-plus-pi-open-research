#!/usr/bin/env python3
"""Exact replay for the symmetric-transfer/base-carry Bessel barrier."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import resource
import time
from pathlib import Path
from types import ModuleType


DEPENDENCIES = {
    "sources/bessel_ordinary_first_three_layer_wilson_carry.md": (
        "af171d428ac26019c3d98af3cd46a72cfa64db5a305857f369b05a6cfd5fa44f"
    ),
    "scripts/bessel_ordinary_first_three_layer_wilson_carry_certificate.py": (
        "6284b8afcbfed1349df814a7be0f4e507c59a9202308684ab7f706fbb366ad2a"
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def check_dependencies(repo: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(repo / relative)
        assert actual == expected, (relative, expected, actual)
        observed[relative] = actual
    return observed


def import_old_certificate(repo: Path) -> ModuleType:
    path = repo / "scripts/bessel_ordinary_first_three_layer_wilson_carry_certificate.py"
    spec = importlib.util.spec_from_file_location("frozen_wilson_carry", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    if limit:
        sieve[0] = 0
    if limit > 1:
        sieve[1] = 0
    for candidate in range(2, int((limit - 1) ** 0.5) + 1):
        if not sieve[candidate]:
            continue
        start = candidate * candidate
        count = (limit - 1 - start) // candidate + 1
        sieve[start:limit:candidate] = b"\x00" * count
    return [value for value, flag in enumerate(sieve) if flag]


def matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def continuant(values: list[int]) -> int:
    previous_previous = 1
    if not values:
        return previous_previous
    previous = values[0]
    for value in values[1:]:
        previous_previous, previous = previous, value * previous + previous_previous
    return previous


def symmetric_continuant_value_derivative(h: int) -> tuple[int, int]:
    """Return K_h(0), K_h'(0) by exact dual-number recurrence."""
    offsets = list(range(-4 * h, 4 * h + 1, 4))
    value_previous_previous, derivative_previous_previous = 1, 0
    value_previous, derivative_previous = offsets[0], 1
    for offset in offsets[1:]:
        value = offset * value_previous + value_previous_previous
        derivative = (
            value_previous
            + offset * derivative_previous
            + derivative_previous_previous
        )
        value_previous_previous, derivative_previous_previous = (
            value_previous,
            derivative_previous,
        )
        value_previous, derivative_previous = value, derivative
    return value_previous, derivative_previous


def q_values(limit: int, modulus: int | None = None) -> list[int]:
    values = [1, 1]
    for n in range(2, limit + 1):
        value = (4 * n - 2) * values[-1] + values[-2]
        if modulus is not None:
            value %= modulus
        values.append(value)
    return values[: limit + 1]


def u_values(limit: int, modulus: int | None = None) -> list[int]:
    values = [1, 3]
    for n in range(2, limit + 1):
        value = (4 * n - 2) * values[-1] + values[-2]
        if modulus is not None:
            value %= modulus
        values.append(value)
    return values[: limit + 1]


def falling(a: int, j: int) -> int:
    result = 1
    for offset in range(j):
        result *= a - offset
    return result


def charlier(n: int, a: int) -> int:
    return sum(math.comb(n, j) * falling(a, j) for j in range(n + 1))


def charlier_lift(n: int) -> int:
    total = 0
    for j in range(1, n + 1):
        quotient, remainder = divmod(falling(n, j), j)
        assert remainder == 0
        total += (-1) ** (j - 1) * quotient * charlier(n - j, -n - 1)
    return total


def transfer_and_slope_grid(prime_bound: int) -> dict[str, object]:
    matrix_checks = 0
    interior_checks = 0
    derivative_checks = 0
    root_slope_checks = 0
    derivative_samples: list[dict[str, int]] = []
    for prime in primes_below(prime_bound):
        if prime < 5:
            continue
        q = q_values(prime + (prime - 1) // 2, prime * prime)
        for root in range((prime - 1) // 2):
            reflected = prime - 1 - root
            h = (prime - 3) // 2 - root
            transfer = [[1, 0], [0, 1]]
            for n in range(root + 1, reflected + 1):
                transfer = matrix_multiply([[4 * n - 2, 1], [1, 0]], transfer)
            assert [
                [entry % prime for entry in row] for row in transfer
            ] == [[1, 0], [(4 * root + 2) % prime, 1]]
            matrix_checks += 1

            interior = list(range(4 * (root + 2) - 2, 4 * reflected - 1, 4))
            symmetric = list(range(2 * prime - 4 * h, 2 * prime + 4 * h + 1, 4))
            assert interior == symmetric
            exact_b = continuant(interior)
            assert transfer[0][1] == exact_b
            interior_checks += 1

            value_zero, derivative_zero = symmetric_continuant_value_derivative(h)
            assert value_zero == 0
            assert exact_b // prime % prime == 2 * derivative_zero % prime
            derivative_checks += 1
            if len(derivative_samples) < 12:
                derivative_samples.append(
                    {
                        "prime": prime,
                        "root": root,
                        "h": h,
                        "K_derivative_at_zero": derivative_zero,
                    }
                )

            if q[root] % prime == 0:
                assert q[root - 1] % prime != 0
                delta = ((q[root] - q[reflected]) // prime) % prime
                predicted = -2 * derivative_zero * q[root - 1] % prime
                assert delta == predicted
                root_slope_checks += 1
    return {
        "prime_bound_exclusive": prime_bound,
        "matrix_checks": matrix_checks,
        "interior_continuant_checks": interior_checks,
        "odd_derivative_checks": derivative_checks,
        "root_slope_checks": root_slope_checks,
        "derivative_samples": derivative_samples,
    }


def charlier_grid(prime_bound: int) -> dict[str, int]:
    evaluation_checks = 0
    symmetry_checks = 0
    connection_checks = 0
    root_digit_checks = 0
    slope_checks = 0
    for prime in primes_below(prime_bound):
        if prime < 5:
            continue
        modulus = prime * prime
        q = q_values(prime - 1)
        for root in range((prime - 1) // 2 + 1):
            reflected = prime - 1 - root
            assert charlier(root, -root - 1) == (-1) ** root * q[root]
            evaluation_checks += 1
            positive = charlier(root, reflected)
            assert positive == charlier(reflected, root)
            symmetry_checks += 1
            lift_root = charlier_lift(root)
            lift_reflected = charlier_lift(reflected)
            assert (
                positive - ((-1) ** root * q[root] + prime * lift_root)
            ) % modulus == 0
            assert (
                positive - ((-1) ** root * q[reflected] + prime * lift_reflected)
            ) % modulus == 0
            connection_checks += 2
            if q[root] % prime == 0:
                assert positive % prime == 0
                base_square = q[root] % modulus == 0
                charlier_condition = positive // prime % prime == lift_root % prime
                assert base_square == charlier_condition
                root_digit_checks += 1
                delta = (q[root] - q[reflected]) // prime % prime
                assert delta == ((-1) ** root * (lift_reflected - lift_root)) % prime
                slope_checks += 1
    return {
        "prime_bound_exclusive": prime_bound,
        "evaluation_checks": evaluation_checks,
        "partial_injection_symmetry_checks": symmetry_checks,
        "connection_congruence_checks": connection_checks,
        "root_square_digit_checks": root_digit_checks,
        "root_slope_checks": slope_checks,
    }


def recurrence_value_at(limit: int, initial: tuple[int, int]) -> list[int]:
    values = [initial[0], initial[1]]
    for n in range(2, limit + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def countermodel_checks() -> dict[str, object]:
    q = q_values(15)
    u = u_values(15)

    prime = 13
    index = 8
    coefficient = 7
    altered_cube = q[index] + prime**2 * coefficient * u[index]
    assert altered_cube == 1004035995248
    assert altered_cube % prime**3 == 0
    assert altered_cube // prime**3 == 457003184
    altered_sequence = recurrence_value_at(
        index,
        (q[0] + prime**2 * coefficient * u[0], q[1] + prime**2 * coefficient * u[1]),
    )
    assert altered_sequence[index] == altered_cube
    for n in range(index + 1):
        assert altered_sequence[n] % prime**2 == q[n] % prime**2

    prime = 11
    root = 4
    coefficient = 2
    altered_base = [q[n] + prime * coefficient * u[n] for n in range(16)]
    assert altered_base == recurrence_value_at(15, (23, 67))
    assert altered_base[root] == 60863 == prime**2 * 503
    altered_delta = (-(altered_base[root + prime] + altered_base[root]) // prime) % prime
    assert altered_delta == 7

    return {
        "cube_countermodel": {
            "prime": 13,
            "index": 8,
            "coefficient": 7,
            "altered_value": altered_cube,
            "altered_over_p3": altered_cube // 13**3,
        },
        "ordinary_base_square_countermodel": {
            "prime": 11,
            "root": 4,
            "coefficient_in_p_times_companion": 2,
            "altered_initial_values": [23, 67],
            "altered_root_value": altered_base[root],
            "altered_slope_mod_p": altered_delta,
        },
    }


def q_at_modulus(index: int, modulus: int) -> int:
    if index <= 1:
        return 1
    previous, current = 1, 1
    for n in range(2, index + 1):
        previous, current = current, ((4 * n - 2) * current + previous) % modulus
    return current


def affine_carry_checks(old: ModuleType) -> list[dict[str, int]]:
    specifications = [
        (13, 4, -1, 8, 1),
        (52453, 14378, 1, 66831, -1),
    ]
    records: list[dict[str, int]] = []
    for prime, root, endpoint, index, f_sign in specifications:
        witness = old.witness(prime, root, endpoint, index, f_sign)
        q_root = q_at_modulus(root, prime**3)
        c = q_root // prime % prime
        d = ((q_root // prime - c) // prime) % prime
        low = witness["unreduced_low_P_mod_p2"]
        delta = low % prime
        rho = ((low - delta) // prime) % prime
        assert (c + endpoint * delta) % prime == 0
        lam = ((c + endpoint * delta) // prime) % prime
        psi = (
            lam
            + endpoint * rho
            + endpoint * (endpoint + 1) * (c + witness["R"])
            + witness["second_layer"]
        ) % prime
        assert (d + psi) % prime == witness["carried_F_over_p2_mod_p"]
        records.append(
            {
                "prime": prime,
                "root": root,
                "endpoint": endpoint,
                "index": index,
                "base_first_digit_c": c,
                "base_second_digit_d": d,
                "slope_delta": delta,
                "low_lift_rho": rho,
                "first_digit_integer_carry_lambda": lam,
                "psi": psi,
                "carried_digit": witness["carried_F_over_p2_mod_p"],
            }
        )
    return records


def main() -> None:
    started = time.perf_counter()
    repo = Path(__file__).resolve().parents[1]
    dependencies = check_dependencies(repo)
    old = import_old_certificate(repo)
    result = {
        "description": (
            "Deterministic exact replay for the ordinary Bessel symmetric-transfer "
            "separation and unavoidable base-carry barrier."
        ),
        "frozen_dependencies": dependencies,
        "transfer_and_slope_grid": transfer_and_slope_grid(100),
        "charlier_grid": charlier_grid(55),
        "affine_carry_witnesses": affine_carry_checks(old),
        "recurrence_countermodels": countermodel_checks(),
        "scope_warning": (
            "The matrix, continuant, Charlier, affine-carry, and perturbation statements "
            "are symbolically proved in the source. Finite grids are regression checks. "
            "No all-prime square or cube exclusion for the original Bessel initial values "
            "is proved."
        ),
    }
    output = repo / "results/bessel_ordinary_symmetric_transfer_base_carry_certificate.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    elapsed = time.perf_counter() - started
    rss_mib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"live_metrics: elapsed_seconds={elapsed:.6f}, peak_rss_mib={rss_mib:.3f}")


if __name__ == "__main__":
    main()

