#!/usr/bin/env python3
"""Deterministic checks for Item 195's two-point moment reduction.

The companion report contains the proofs.  This script checks the finite-field
Hermite inversion, the rational jet formula, agreement with the frozen
Item180 determinant, the natural interpolation tail factor, and the bounded-
conductor Jacobi-sum counterexample.  Finite checks are not extrapolated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item195_twopoint_moment_certificate.json"
DEPENDENCIES = (
    "item180_moving_residual_report.md",
    "item185_moving_root_count_report.md",
    "item189_collision_route_report.md",
)
RESIDUE_OFFSETS = (0, 1, -1, -2, -3)
JET_ORDER = 3


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            return False
        q += 2
    return True


def primes_upto(limit: int) -> list[int]:
    return [p for p in range(17, limit + 1) if is_prime(p)]


def poly_mul_trunc(left: list[int], right: list[int], p: int, cap: int = 3) -> list[int]:
    out = [0] * (cap + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= cap:
                out[i + j] = (out[i + j] + a * b) % p
    return out


def generalized_binomial(exponent: int, k: int, p: int) -> int:
    value = 1
    for j in range(k):
        value = value * (exponent - j) % p
    return value * pow(math.factorial(k), -1, p) % p


def one_plus_power(series: list[int], exponent: int, p: int, cap: int = 3) -> list[int]:
    """(1+u)^exponent for a truncated series with series[0]=1."""
    u = series[:]
    u[0] = 0
    out = [0] * (cap + 1)
    out[0] = 1
    power = [0] * (cap + 1)
    power[0] = 1
    for k in range(1, cap + 1):
        power = poly_mul_trunc(power, u, p, cap)
        coefficient = generalized_binomial(exponent, k, p)
        for j in range(cap + 1):
            out[j] = (out[j] + coefficient * power[j]) % p
    return out


def psi_series(p: int, s: int, t: int) -> list[int]:
    """The p-free order-three logarithmic Hasse jet Psi_j(t,s)."""
    inv_t = pow(t, -1, p)
    inv_one_minus_t = pow((1 - t) % p, -1, p)
    first = [
        math.comb(3 * s, k) * pow(inv_t, k, p) % p
        for k in range(JET_ORDER + 1)
    ]
    second = [
        ((-1) ** k) * math.comb(5 * s + 2, k) * pow(inv_one_minus_t, k, p) % p
        for k in range(JET_ORDER + 1)
    ]
    g0 = (1 - pow(t, 4, p)) % p
    inv_g0 = pow(g0, -1, p)
    ratio = [
        1,
        -4 * pow(t, 3, p) * inv_g0 % p,
        -6 * pow(t, 2, p) * inv_g0 % p,
        -4 * t * inv_g0 % p,
    ]
    third = one_plus_power(ratio, -2 * s - 2, p, JET_ORDER)
    return poly_mul_trunc(poly_mul_trunc(first, second, p), third, p)


def w_polynomial(p: int, s: int) -> list[int]:
    """Coefficients of x^(3s)(1-x)^(5s+2)(1-x^4)^(p-2s-2)."""
    b = 5 * s + 2
    c = p - 2 * s - 2
    degree = 4 * p - 6
    out = [0] * (degree + 1)
    for a in range(b + 1):
        left = ((-1) ** a) * math.comb(b, a)
        for q in range(c + 1):
            n = 3 * s + a + 4 * q
            out[n] = (out[n] + left * ((-1) ** q) * math.comb(c, q)) % p
    if out[-1] == 0:
        raise AssertionError((p, s, "lost leading coefficient"))
    return out


def hasse_derivative(coefficients: list[int], order: int, p: int) -> list[int]:
    return [
        math.comb(n + order, order) * coefficients[n + order] % p
        for n in range(len(coefficients) - order)
    ]


def evaluate_polynomial(coefficients: list[int], t: int, p: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * t + coefficient) % p
    return value


def invert_matrix(matrix: list[list[int]], p: int) -> list[list[int]]:
    size = len(matrix)
    augmented = [
        [entry % p for entry in row]
        + [1 if i == j else 0 for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next((i for i in range(column, size) if augmented[i][column]), None)
        if pivot is None:
            raise AssertionError("singular Hermite matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = pow(augmented[column][column], -1, p)
        augmented[column] = [entry * scale % p for entry in augmented[column]]
        for i in range(size):
            if i == column:
                continue
            scale = augmented[i][column]
            if scale:
                augmented[i] = [
                    (a - scale * b) % p
                    for a, b in zip(augmented[i], augmented[column])
                ]
    return [row[size:] for row in augmented]


def matrix_vector(matrix: list[list[int]], vector: list[int], p: int) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) % p for row in matrix]


def recurrence_coefficients(p: int, s: int) -> list[int]:
    a = [0] * p
    a[0] = 1
    for n in range(p - 1):
        rhs = (n - 5 * s - 2) * a[n]
        if n >= 3:
            rhs += (n + 8 * s + 5) * a[n - 3]
        if n >= 4:
            rhs -= (n + 3 * s + 2) * a[n - 4]
        a[n + 1] = rhs * pow(n + 1, -1, p) % p
    return a


def item180_determinant(p: int, s: int) -> int:
    a = recurrence_coefficients(p, s)
    d = p - 3 * s

    def get(n: int) -> int:
        return a[n] if 0 <= n < len(a) else 0

    value = (
        (get(d - 2) + get(d - 3) + get(d - 4)) * get(p - 5)
        - (get(p - 4) + get(p - 3) + get(p - 2)) * get(d - 1)
    )
    return ((-1 if s & 1 else 1) * value) % p


def verify_pair(p: int, s: int) -> dict:
    coefficients = w_polynomial(p, s)
    derivatives = [
        hasse_derivative(coefficients, j, p) for j in range(JET_ORDER + 1)
    ]
    derivative_values = [
        [evaluate_polynomial(derivative, t, p) for t in range(1, p)]
        for derivative in derivatives
    ]

    rational_jet_checks = 0
    excluded_jet_checks = 0
    for t in range(1, p):
        g = (1 - pow(t, 4, p)) % p
        if g == 0:
            for j in range(JET_ORDER + 1):
                if derivative_values[j][t - 1] != 0:
                    raise AssertionError((p, s, t, j, "nonzero excluded jet"))
                excluded_jet_checks += 1
            continue
        psi = psi_series(p, s, t)
        q = (1 + t + t * t + t * t * t) % p
        rational_map = (
            pow(t * (1 - t) % p, 3, p) * pow(q * q % p, -1, p)
        ) % p
        base = (1 - t) * pow(q, -1, p) % p
        f_value = base * pow(rational_map, s, p) % p
        if f_value != derivative_values[0][t - 1]:
            raise AssertionError((p, s, t, "rational-map value mismatch"))
        for j in range(JET_ORDER + 1):
            if derivative_values[j][t - 1] != f_value * psi[j] % p:
                raise AssertionError((p, s, t, j, "rational jet mismatch"))
            rational_jet_checks += 1

    recovered: dict[tuple[int, int], int] = {}
    moment_count = 0
    alias_count = 0
    for offset in RESIDUE_OFFSETS:
        residue = offset % (p - 1)
        moments = []
        for j in range(JET_ORDER + 1):
            total = 0
            exponent = (j - residue) % (p - 1)
            for t in range(1, p):
                total += pow(t, exponent, p) * derivative_values[j][t - 1]
            moments.append(-total % p)
            moment_count += 1
        matrix = [
            [math.comb(residue + ell * (p - 1), j) % p for ell in range(4)]
            for j in range(4)
        ]
        aliases = matrix_vector(invert_matrix(matrix, p), moments, p)
        for ell, value in enumerate(aliases):
            n = residue + ell * (p - 1)
            expected = coefficients[n] if n < len(coefficients) else 0
            if value != expected:
                raise AssertionError((p, s, offset, ell, value, expected))
            recovered[(offset, ell)] = value
            alias_count += 1

    w_p1 = recovered[(0, 1)]
    z_p1 = (
        w_p1
        + recovered[(-1, 0)]
        + recovered[(-2, 0)]
        + recovered[(-3, 0)]
    ) % p
    w_2p1 = recovered[(1, 2)]
    z_2p1 = (
        w_2p1
        + recovered[(0, 2)]
        + recovered[(-1, 1)]
        + recovered[(-2, 1)]
    ) % p
    determinant = (z_p1 * w_2p1 - z_2p1 * w_p1) % p
    frozen = item180_determinant(p, s)
    if determinant != frozen:
        raise AssertionError((p, s, determinant, frozen))
    return {
        "rational_jet_checks": rational_jet_checks,
        "excluded_jet_checks": excluded_jet_checks,
        "moment_checks": moment_count,
        "alias_checks": alias_count,
        "determinant": determinant,
    }


def trim_polynomial(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def polynomial_add(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i in range(len(out)):
        out[i] = ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)) % p
    return trim_polynomial(out)


def polynomial_scale(poly: list[int], scale: int, p: int) -> list[int]:
    return trim_polynomial([scale * value % p for value in poly])


def polynomial_multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim_polynomial(out)


def interpolate_consecutive(values: list[int], p: int) -> list[int]:
    """Interpolate values at 0,...,p-1 in the Newton binomial basis."""
    differences = [value % p for value in values]
    newton = []
    while differences:
        newton.append(differences[0])
        differences = [
            (differences[i + 1] - differences[i]) % p
            for i in range(len(differences) - 1)
        ]
    result = [0]
    basis = [1]
    for k, coefficient in enumerate(newton):
        if k:
            basis = polynomial_multiply(basis, [-(k - 1) % p, 1], p)
            basis = polynomial_scale(basis, pow(k, -1, p), p)
        result = polynomial_add(result, polynomial_scale(basis, coefficient, p), p)
    return trim_polynomial(result)


def divide_linear(poly: list[int], root: int, p: int) -> tuple[list[int], int]:
    if len(poly) <= 1:
        return [0], poly[0]
    quotient = [0] * (len(poly) - 1)
    quotient[-1] = poly[-1]
    for i in range(len(poly) - 2, 0, -1):
        quotient[i - 1] = (poly[i] + root * quotient[i]) % p
    remainder = (poly[0] + root * quotient[0]) % p
    return trim_polynomial(quotient), remainder


def natural_entry_sequence(p: int) -> list[int]:
    values = []
    for s in range(p):
        a = recurrence_coefficients(p, s)

        def u(r: int) -> int:
            n = p - r - 3 * s
            return a[n] if 0 <= n < p else 0

        def v(r: int) -> int:
            return a[p - r]

        value = ((u(2) + u(3) + u(4)) * v(5) - (v(4) + v(3) + v(2)) * u(1)) % p
        values.append(value)
    return values


def interpolation_tail_check(p: int) -> dict:
    values = natural_entry_sequence(p)
    n = (p - 1) // 3
    tail_start = n + 1
    if not all(value == 0 for value in values[tail_start:]):
        raise AssertionError((p, "natural tail is not zero"))
    if values[0] == 0:
        raise AssertionError((p, "nonzero anchor lost"))
    polynomial = interpolate_consecutive(values, p)
    quotient = polynomial
    for root in range(tail_start, p):
        quotient, remainder = divide_linear(quotient, root, p)
        if remainder:
            raise AssertionError((p, root, "tail factor division failed"))
    lower_bound = p - 1 - n
    if len(polynomial) - 1 < lower_bound:
        raise AssertionError((p, len(polynomial) - 1, lower_bound))
    return {
        "p": p,
        "N_p": n,
        "tail_start": tail_start,
        "tail_root_count": lower_bound,
        "proved_degree_lower_bound": lower_bound,
        "actual_interpolation_degree_finite_check": len(polynomial) - 1,
        "residual_quotient_degree_finite_check": len(quotient) - 1,
        "value_at_zero": values[0],
    }


def jacobi_counterexample(p: int) -> dict:
    checked = []
    for s in range(1, (p - 3) // 2 + 1):
        value = sum(pow(t * (1 - t) % p, s, p) for t in range(p)) % p
        if value:
            raise AssertionError((p, s, value, "Jacobi reduction should vanish"))
        checked.append(s)
    return {
        "p": p,
        "zero_parameter_interval": [1, (p - 3) // 2],
        "zero_count": len(checked),
    }


def locate_dependencies() -> dict:
    # Resolution is deliberately local-layout aware, while the serialized
    # identity is archive-relative.  This makes work/ and archived scripts/
    # replays byte-identical and avoids embedding a machine-specific path.
    candidates = [HERE, HERE.parent / "sources"]
    if HERE.name.lower() == "scripts":
        candidates = [HERE.parent / "sources"]
    candidates.append((Path(__file__).resolve().parents[1] / "sources"))
    found = {}
    for name in DEPENDENCIES:
        logical_path = f"sources/{name}"
        for directory in candidates:
            path = directory / name
            if path.exists():
                found[logical_path] = {"sha256": sha256_file(path)}
                break
        else:
            raise FileNotFoundError(f"missing frozen dependency: {logical_path}")
    return found


def run(prime_limit: int) -> dict:
    primes = primes_upto(prime_limit)
    if not primes:
        raise ValueError("prime limit must include a prime at least 17")
    totals = {
        "prime_count": len(primes),
        "admissible_pair_count": 0,
        "rational_jet_checks": 0,
        "excluded_jet_checks": 0,
        "moment_checks": 0,
        "alias_checks": 0,
        "determinant_checks": 0,
    }
    zero_pairs = []
    for p in primes:
        for s in range((p - 1) // 3 + 1):
            row = verify_pair(p, s)
            totals["admissible_pair_count"] += 1
            for key in ("rational_jet_checks", "excluded_jet_checks", "moment_checks", "alias_checks"):
                totals[key] += row[key]
            totals["determinant_checks"] += 1
            if row["determinant"] == 0:
                zero_pairs.append([p, s])

    tail_rows = [interpolation_tail_check(p) for p in primes]
    jacobi_rows = [jacobi_counterexample(p) for p in primes]
    encoded = json.dumps(zero_pairs, separators=(",", ":")).encode("ascii")
    return {
        "item": 195,
        "title": "two-point Hermite moments and conductor obstruction",
        "status": {
            "proved": [
                "four Hasse moments invert each relevant coefficient residue class",
                "the moving determinant and its h-shift use one fixed six-puncture rational map",
                "the natural coefficient extension has at least p-1-floor((p-1)/3) interpolation degree",
                "bounded tame Kummer conductor alone does not control mod-p zeros",
            ],
            "finite_only": "all numerical checks in this JSON",
            "open": "C_p(h)=O(h), the Sidon assertion, and every unconditional sublinear root count",
        },
        "scope": {"prime_min": 17, "prime_max": prime_limit, "jet_order": JET_ORDER},
        "hermite_matrix": {
            "size": 4,
            "entries": "binomial(r+ell*(p-1),j), 0<=j,ell<=3",
            "determinant_mod_p": 1,
            "residue_offsets": list(RESIDUE_OFFSETS),
        },
        "totals": totals,
        "zero_pairs": zero_pairs,
        "zero_pairs_sha256": hashlib.sha256(encoded).hexdigest(),
        "interpolation_tail_checks": tail_rows,
        "jacobi_bounded_conductor_counterexample_checks": jacobi_rows,
        "dependencies": locate_dependencies(),
        "runtime": {"python": platform.python_version(), "implementation": platform.python_implementation()},
        "warning": "Finite verification is not an asymptotic collision theorem.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=47)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    result = run(args.prime_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "sha256": sha256_file(args.output), "totals": result["totals"]}, sort_keys=True))


if __name__ == "__main__":
    main()
