#!/usr/bin/env python3
"""Exact replay for Item 169.

The finite prime scan is explicitly diagnostic.  The algebraic fixtures
verify the divided Newton/Taylor implications without pretending that a
singular all-lift orbit was found for the actual Bessel seed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for d in range(2, math.isqrt(limit) + 1):
        if sieve[d]:
            sieve[d * d : limit + 1 : d] = b"\x00" * (
                (limit - d * d) // d + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def recurrence(initial0: int, initial1: int, stop: int, modulus: int) -> list[int]:
    values = [initial0 % modulus]
    if stop == 0:
        return values
    values.append(initial1 % modulus)
    for n in range(2, stop + 1):
        values.append(((4 * n - 2) * values[-1] + values[-2]) % modulus)
    return values


def forward_difference(values: list[int], order: int, modulus: int) -> int:
    return sum(
        (-1) ** (order - j) * math.comb(order, j) * values[j]
        for j in range(order + 1)
    ) % modulus


def binomial_basis_poly(order: int, p: int) -> list[int]:
    """Coefficients of binom(T, order), low degree first, in F_p[T]."""
    poly = [1]
    for root in range(order):
        nxt = [0] * (len(poly) + 1)
        for degree, coefficient in enumerate(poly):
            nxt[degree] = (nxt[degree] - root * coefficient) % p
            nxt[degree + 1] = (nxt[degree + 1] + coefficient) % p
        poly = nxt
    scale = pow(math.factorial(order), -1, p)
    return [(scale * coefficient) % p for coefficient in poly]


def binomial_sum_poly(coefficients: list[int], p: int) -> list[int]:
    out = [0] * len(coefficients)
    for order, coefficient in enumerate(coefficients):
        basis = binomial_basis_poly(order, p)
        for degree, value in enumerate(basis):
            out[degree] = (out[degree] + coefficient * value) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_eval(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def poly_derivative(poly: list[int], p: int) -> list[int]:
    if len(poly) == 1:
        return [0]
    return [(degree * poly[degree]) % p for degree in range(1, len(poly))]


def integer_binomial_sum(coefficients: list[int], x: int) -> int:
    return sum(coefficient * math.comb(x, j) for j, coefficient in enumerate(coefficients))


def scan_actual_seed(prime_limit: int) -> dict:
    singular = []
    all_lift = []
    noncentral_singular = []
    root_count = 0
    anti_checks = 0
    numerator_checks = 0

    for p in primes_upto(prime_limit):
        if p < 3:
            continue
        p2 = p * p
        q = recurrence(1, 1, 2 * p - 1, p2)
        numerator = recurrence(1, 3, 2 * p - 1, p)
        for n in range(p):
            assert (q[n + p] + q[n]) % p == 0
            anti_checks += 1
            assert (numerator[n + p] - numerator[n]) % p == 0
            numerator_checks += 1
        for r in range(p):
            if q[r] % p:
                continue
            root_count += 1
            lam = (q[r] // p) % p
            delta = ((-q[r + p] - q[r]) % p2) // p
            if delta == 0:
                row = {
                    "p": p,
                    "r": r,
                    "central": r == (p - 1) // 2,
                    "lambda": lam,
                    "delta": delta,
                }
                singular.append(row)
                if not row["central"]:
                    noncentral_singular.append(row)
                if lam == 0:
                    all_lift.append(row)

    return {
        "prime_limit": prime_limit,
        "odd_prime_count": sum(1 for p in primes_upto(prime_limit) if p >= 3),
        "root_count": root_count,
        "anti_period_value_checks": anti_checks,
        "numerator_period_value_checks": numerator_checks,
        "singular_roots": singular,
        "noncentral_singular_roots": noncentral_singular,
        "all_lift_roots": all_lift,
        "status": "EXPERIMENTAL_FINITE",
    }


def verify_newton_grid(limit: int = 101) -> dict:
    root_fibres = 0
    evaluations = 0
    difference_checks = 0
    for p in primes_upto(limit):
        if p < 7:
            continue
        p4 = p**4
        test_x = list(range(13)) + [p - 1, p, p + 1, 2 * p + 3]
        stop = (p - 1) + max(test_x) * p
        q = recurrence(1, 1, stop, p4)
        for r in range(p):
            if q[r] % p:
                continue
            root_fibres += 1
            a = [((-1) ** j * q[r + j * p]) % p4 for j in range(7)]
            differences = [forward_difference(a, j, p4) for j in range(7)]
            assert differences[4] % (p**3) == 0
            assert differences[5] % (p**3) == 0
            assert differences[6] % p4 == 0
            difference_checks += 3
            for x in test_x:
                rhs = sum(math.comb(x, j) * differences[j] for j in range(6)) % p4
                lhs = ((-1) ** x * q[r + x * p]) % p4
                assert lhs == rhs
                evaluations += 1
    return {
        "prime_limit": limit,
        "root_fibres": root_fibres,
        "newton_evaluations": evaluations,
        "difference_valuation_checks": difference_checks,
        "status": "EXACT_REPLAY_OF_PROVED_CONGRUENCES",
    }


def formal_fixture(p: int, name: str, b_coefficients: list[int]) -> dict:
    """Here B(T)=sum b_j binom(T,j); D_j=p^2 b_j."""
    assert p >= 7
    assert len(b_coefficients) == 6
    assert b_coefficients[4] % p == 0
    assert b_coefficients[5] % p == 0
    p2 = p * p
    p_coefficients = [value % p for value in b_coefficients[:4]]
    p_poly = binomial_sum_poly(p_coefficients, p)
    p_derivative = poly_derivative(p_poly, p)
    roots = []
    taylor_checks = 0

    for t in range(p):
        p_value = poly_eval(p_poly, t, p)
        direct_p_value = integer_binomial_sum(b_coefficients, t) % p
        assert p_value == direct_p_value
        if p_value:
            continue
        b_at_t = integer_binomial_sum(b_coefficients, t)
        assert b_at_t % p == 0
        kappa = (b_at_t // p) % p
        tau = poly_eval(p_derivative, t, p)
        passing_u = []
        for u in range(p):
            pass_values = []
            for v in (0, 1, p - 1):
                x = t + p * u + p2 * v
                b_at_x = integer_binomial_sum(b_coefficients, x)
                assert b_at_x % p == 0
                lhs = (b_at_x // p) % p
                rhs = (kappa + u * tau) % p
                assert lhs == rhs
                pass_values.append(lhs == 0)
                taylor_checks += 1
            assert len(set(pass_values)) == 1
            if pass_values[0]:
                passing_u.append(u)

        if tau:
            assert len(passing_u) == 1
            branch_type = "unique_u_then_all_v"
        elif kappa:
            assert len(passing_u) == 0
            branch_type = "dead"
        else:
            assert len(passing_u) == p
            branch_type = "all_u_all_v"
        roots.append(
            {
                "t": t,
                "kappa": kappa,
                "tau": tau,
                "passing_u": passing_u,
                "branch_type": branch_type,
            }
        )

    if len(p_poly) > 1 or p_poly[0] != 0:
        assert len(roots) <= 3
    return {
        "p": p,
        "name": name,
        "B_binomial_coefficients": b_coefficients,
        "P_power_basis_coefficients_mod_p": p_poly,
        "P_roots": roots,
        "taylor_checks": taylor_checks,
    }


def formal_fixtures() -> dict:
    rows = []
    for p in (7, 11, 13):
        rows.append(formal_fixture(p, "three_simple_roots", [0, 0, 0, 6, 2 * p, 3 * p]))
        rows.append(formal_fixture(p, "double_root_full", [0, 1, 2, 0, 0, 0]))
        rows.append(formal_fixture(p, "double_root_dead", [p, 1, 2, 0, 0, 0]))
        rows.append(formal_fixture(p, "P_identically_zero", [p, 2 * p, 3 * p, 4 * p, 5 * p, 6 * p]))

    matching_checks = 0
    matching_rows = []
    level_three_matching_rows = []
    for row in rows:
        p = row["p"]
        b_coefficients = row["B_binomial_coefficients"]
        p_poly = row["P_power_basis_coefficients_mod_p"]
        beta = 2
        numerator_value = 3
        a_value = 5
        sign = -1
        target = beta * numerator_value % p
        roots = []
        for t in range(p):
            p_value = poly_eval(p_poly, t, p)
            match_value = (target - sign * a_value * p_value) % p
            if match_value == 0:
                assert p_value != 0
                roots.append(t)
            matching_checks += 1
        # Unless the matching polynomial is identically zero, degree <= 3.
        matching_poly = p_poly[:]
        matching_poly = [(-sign * a_value * c) % p for c in matching_poly]
        matching_poly[0] = (matching_poly[0] + target) % p
        while len(matching_poly) > 1 and matching_poly[-1] == 0:
            matching_poly.pop()
        identity = len(matching_poly) == 1 and matching_poly[0] == 0
        if not identity:
            assert len(roots) <= 3
        matching_rows.append(
            {
                "p": p,
                "fixture": row["name"],
                "matching_polynomial_identity": identity,
                "matching_t_roots": roots,
            }
        )

        beta3 = 2
        numerator3 = 3
        a3 = 5
        sign3 = -1
        target3 = beta3 * numerator3 % p
        for root in row["P_roots"]:
            t = root["t"]
            kappa = root["kappa"]
            tau = root["tau"]
            passing_u = []
            for u in range(p):
                divided_q = (kappa + u * tau) % p
                match_value = (target3 - sign3 * a3 * divided_q) % p
                if match_value == 0:
                    assert divided_q != 0
                    passing_u.append(u)
                matching_checks += 1
            if tau:
                assert len(passing_u) == 1
            else:
                assert len(passing_u) in (0, p)
                if kappa == 0:
                    assert len(passing_u) == 0
            level_three_matching_rows.append(
                {
                    "p": p,
                    "fixture": row["name"],
                    "t": t,
                    "kappa": kappa,
                    "tau": tau,
                    "matching_u": passing_u,
                }
            )

    # Separate exact identity fixture: constant P and matching constant agree.
    identity_checks = []
    for p in (7, 11, 13):
        sign = -1
        a_value = 5
        numerator_value = 3
        constant_p = 2
        beta = (sign * a_value * constant_p * pow(numerator_value, -1, p)) % p
        assert beta != 0
        values = [
            (beta * numerator_value - sign * a_value * constant_p) % p
            for _ in range(p)
        ]
        assert values == [0] * p
        identity_checks.append({"p": p, "constant_P": constant_p, "beta": beta})

    return {
        "fixtures": rows,
        "matching_rows": matching_rows,
        "level_three_matching_rows": level_three_matching_rows,
        "matching_value_checks": matching_checks,
        "matching_identity_fixtures": identity_checks,
        "status": "FORMAL_ALGEBRA_REPLAY_NOT_RECURRENCE_EXAMPLES",
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=20_000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("work/item169_deeper_all_lift_certificate.json"),
    )
    args = parser.parse_args()
    if args.prime_limit < 101:
        raise SystemExit("--prime-limit must be at least 101")

    script_path = Path(__file__)
    result = {
        "item": 169,
        "sequence": "q_0=q_1=1; q_n=(4n-2)q_{n-1}+q_{n-2}",
        "actual_seed_scan": scan_actual_seed(args.prime_limit),
        "newton_grid": verify_newton_grid(),
        "formal_divided_law_fixtures": formal_fixtures(),
        "scope": {
            "proved": [
                "replayed recurrence congruences and finite-difference valuations",
                "formal p^3/p^4 divided Taylor implications",
                "formal cubic matching root bound and identity alternative",
            ],
            "experimental": [
                "finite actual-seed absence or occurrence of singular/all-lift roots",
            ],
            "open": [
                "existence of any actual-seed noncentral singular all-lift orbit",
                "positive-rate abundance and synchronization with the actual coefficient b_m",
            ],
            "modified_seed_examples_used": False,
        },
        "script_sha256": sha256(script_path),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded, encoding="utf-8", newline="\n")
    print(encoded, end="")


if __name__ == "__main__":
    main()
