#!/usr/bin/env python3
"""Exact replay for rational-moment-preserving integer C^3 approximation.

The all-parameter approximation theorem is proved symbolically in the
companion source.  This replay checks the algebraic kernel, endpoint orders,
Bernstein normalization identities, representative exact constructions, and
the Farey obstruction.  Finite rows are diagnostics, not extrapolations.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "sources/common_kernel_native_exact_moment_integer_approximation.md"
)
OUTPUT = (
    ROOT
    / "results/common_kernel_native_exact_moment_integer_approximation_certificate.json"
)
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_native_output_bernstein_congruence_hashes.sha256":
        "559cc412db81ed449d4255654ad370f44a8ceb4d8acdce234a7f607d448ffcb7",
}

t = sp.symbols("t")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
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


def valuation(integer: int, prime: int) -> int:
    assert integer
    value = abs(integer)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def rational_valuation(value: Fraction, prime: int) -> int:
    return valuation(value.numerator, prime) - valuation(value.denominator, prime)


def polynomial_integral(poly: sp.Expr) -> Fraction:
    value = sp.Rational(sp.integrate(sp.Poly(sp.expand(poly), t).as_expr(), (t, 0, 1)))
    return Fraction(int(value.p), int(value.q))


def moment(poly: sp.Expr, W: sp.Expr) -> Fraction:
    return 4 * polynomial_integral(sp.expand(W * poly))


def moment_image_checks() -> dict[str, object]:
    n = sp.symbols("n", integer=True, nonnegative=True)
    v0, v1, v2, v3 = sp.symbols("v0 v1 v2 v3", integer=True)
    denominator = sp.prod(n + j + 1 for j in range(4))
    rational = sum(
        coefficient / (n + j + 1)
        for j, coefficient in enumerate([v0, v1, v2, v3])
    )
    numerator = sp.Poly(
        sp.cancel(rational * denominator), n,
        domain=sp.ZZ[v0, v1, v2, v3],
    )
    assert numerator.degree() <= 3
    for j, coefficient in enumerate([v0, v1, v2, v3], start=1):
        residue = sp.expand(numerator.as_expr().subs(n, -j))
        expected = sp.expand(
            coefficient
            * sp.prod(-j + offset for offset in range(1, 5) if offset != j)
        )
        assert residue == expected

    rows = []
    representative_weights = [
        4 * (2 + t) * t * (2 - t) ** 2,
        4 * t**2 * (2 - t) ** 2 * t**4 * (1 - t) ** 4,
    ]
    for index, V in enumerate(representative_weights):
        V_poly = sp.Poly(V, t, domain=sp.ZZ)
        degree = V_poly.degree()

        def closed_moment(exponent: int) -> Fraction:
            return sum(
                (
                    Fraction(int(V_poly.nth(j)), exponent + j + 1)
                    for j in range(degree + 1)
                ),
                Fraction(0),
            )

        prime_rows = []
        for prime in [2, 3, 5, 7, 11, 13]:
            samples = []
            # Search the finitely many denominator branches for a nonzero
            # limiting numerator and record exact valuation descent.
            common_denominator = sp.prod(n + j + 1 for j in range(degree + 1))
            expression = sum(
                V_poly.nth(j) / (n + j + 1)
                for j in range(degree + 1)
            )
            F = sp.Poly(
                sp.cancel(expression * common_denominator), n, domain=sp.ZZ
            )
            branch = next(
                c for c in range(1, degree + 2)
                if F.eval(-c) != 0
            )
            base_valuation = valuation(int(F.eval(-branch)), prime)
            for exponent in range(max(4, base_valuation + 1), 9):
                m = prime**exponent - branch
                value = closed_moment(m)
                samples.append({
                    "exponent": exponent,
                    "n": m,
                    "v_p_moment": rational_valuation(value, prime),
                })
            assert all(
                samples[offset + 1]["v_p_moment"]
                < samples[offset]["v_p_moment"]
                for offset in range(len(samples) - 1)
            )
            prime_rows.append({
                "prime": prime,
                "branch_c": branch,
                "v_p_F_minus_c": base_valuation,
                "samples": samples,
            })
        rows.append({
            "weight_index": index,
            "degree": degree,
            "prime_descent": prime_rows,
        })

    return {
        "generic_degree_three_numerator": str(numerator.as_expr()),
        "representative_p_adic_descent": rows,
        "scope": (
            "The displayed finite descents replay examples; the all-prime "
            "proof uses n=p^k-c and F(-c) nonzero."
        ),
    }


def crt_and_kernel_checks() -> dict[str, object]:
    inverse_left = -20 * t**3 + 70 * t**2 - 84 * t + 35
    inverse_right = 20 * t**3 + 10 * t**2 + 4 * t + 1
    bezout = sp.expand(
        inverse_left * t**4 + inverse_right * (t - 1) ** 4
    )
    assert bezout == 1

    W_function = sp.Function("W")(t)
    U_function = sp.Function("U")(t)
    differential = 2 * sp.diff(W_function, t) * U_function + W_function * sp.diff(U_function, t)
    kernel_difference = sp.simplify(
        W_function * differential
        - sp.diff(W_function**2 * U_function, t)
    )
    assert kernel_difference == 0

    E_function = sp.Function("E")(t)
    third = sp.expand(sp.diff(
        2 * sp.diff(W_function, t) * E_function
        + W_function * sp.diff(E_function, t),
        t,
        3,
    ))
    expected = (
        2 * sp.diff(W_function, t, 4) * E_function
        + 7 * sp.diff(W_function, t, 3) * sp.diff(E_function, t)
        + 9 * sp.diff(W_function, t, 2) * sp.diff(E_function, t, 2)
        + 5 * sp.diff(W_function, t) * sp.diff(E_function, t, 3)
        + W_function * sp.diff(E_function, t, 4)
    )
    assert sp.simplify(third - expected) == 0

    examples = []
    for case in ["order_one", "order_two"]:
        if case == "order_one":
            W = sp.expand((2 + t) * t * (2 - t) ** 2)
            S = sp.expand(t**4 * (1 - t) ** 5 * (1 + t))
            origin_order = 1
        else:
            W = sp.expand(t**2 * (2 - t) ** 2)
            S = sp.expand(t**3 * (1 - t) ** 5 * (1 + t))
            origin_order = 2
        g = sp.expand(2 * sp.diff(W, t) * S + W * sp.diff(S, t))
        assert sp.rem(g, t**4, t) == 0
        assert sp.rem(g, (t - 1) ** 4, t) == 0
        assert moment(g, W) == 0
        J = sp.integrate(sp.expand(W * g), (t, 0, t))
        assert sp.expand(J - W**2 * S) == 0
        examples.append({
            "case": case,
            "ord_0_W": origin_order,
            "ord_0_S": sp.Poly(S, t).terms()[-1][0][0],
            "degree_S": sp.Poly(S, t).degree(),
            "degree_g": sp.Poly(g, t).degree(),
            "moment_g": "0",
        })

    return {
        "crt_bezout": str(bezout),
        "kernel_pointwise_difference": str(kernel_difference),
        "third_derivative_term_count": len(sp.Add.make_args(third)),
        "polynomial_examples": examples,
    }


def falling(value: int, count: int) -> int:
    answer = 1
    for offset in range(count):
        answer *= value - offset
    return answer


def rising(value: int, count: int) -> int:
    answer = 1
    for offset in range(count):
        answer *= value + offset
    return answer


def bernstein_identity_checks() -> dict[str, object]:
    identity_count = 0
    weighted_count = 0
    maxima = {
        "nu1_t_D4_scaled_n": Fraction(0),
        "nu2_t_D3_scaled_n": Fraction(0),
        "nu2_t2_D4_scaled_n": Fraction(0),
    }
    for n in range(12, 121):
        for j in range(5):
            for alpha in range(j + 1):
                for k in range(max(4, alpha), n - 4):
                    if n - k < j - alpha:
                        continue
                    left = Fraction(
                        falling(k, alpha) * falling(n - k, j - alpha),
                        math.comb(n - j, k - alpha),
                    )
                    right = Fraction(
                        falling(n, j), math.comb(n, k)
                    )
                    assert left == right
                    identity_count += 1
                    for lam in range(3):
                        ratio = Fraction(
                            math.comb(n - j, k - alpha),
                            math.comb(
                                n - j + lam, k - alpha + lam
                            ),
                        )
                        expected = Fraction(
                            rising(k - alpha + 1, lam),
                            rising(n - j + 1, lam),
                        )
                        assert ratio == expected
                        weighted_count += 1

        def normalized_bound(r: int, j: int, lam: int) -> Fraction:
            total = Fraction(0)
            denominator_rising = rising(n - j + 1, lam)
            for alpha in range(j + 1):
                candidates = []
                for k in range(r, n - 4):
                    if k < alpha or n - k < j - alpha:
                        continue
                    candidates.append(Fraction(
                        rising(k - alpha + 1, lam),
                        math.comb(n, k),
                    ))
                total += math.comb(j, alpha) * max(candidates)
            return (
                Fraction(falling(n, j), 2 * denominator_rising) * total
            )

        b1 = normalized_bound(4, 4, 1)
        b2 = normalized_bound(3, 3, 1)
        b3 = normalized_bound(3, 4, 2)
        maxima["nu1_t_D4_scaled_n"] = max(
            maxima["nu1_t_D4_scaled_n"], n * b1
        )
        maxima["nu2_t_D3_scaled_n"] = max(
            maxima["nu2_t_D3_scaled_n"], n * b2
        )
        maxima["nu2_t2_D4_scaled_n"] = max(
            maxima["nu2_t2_D4_scaled_n"], n * b3
        )

    return {
        "factorial_identity_instances": identity_count,
        "weighted_identity_instances": weighted_count,
        "finite_scaled_bound_maxima": {
            key: str(value) for key, value in maxima.items()
        },
        "scope": (
            "The O(1/n) theorem follows from exact endpoint-ratio formulas; "
            "the n<=120 maxima are diagnostics only."
        ),
    }


def nearest_integer(value: Fraction) -> int:
    if value >= 0:
        return (2 * value.numerator + value.denominator) // (
            2 * value.denominator
        )
    return -nearest_integer(-value)


def exact_rounded_examples() -> dict[str, object]:
    rows = []
    for case in ["order_one", "order_two"]:
        if case == "order_one":
            W = sp.expand((2 + t) * t * (2 - t) ** 2)
            S = sp.expand(t**4 * (1 - t) ** 5 * (1 + t) / 4)
            r = 4
        else:
            W = sp.expand(t**2 * (2 - t) ** 2)
            S = sp.expand(t**3 * (1 - t) ** 5 * (1 + t) / 4)
            r = 3
        for n in [16, 24, 36]:
            z = []
            for k in range(n + 1):
                value = sp.Rational(S.subs(t, sp.Rational(k, n)))
                target = Fraction(
                    int(value.p) * math.comb(n, k), int(value.q)
                )
                z.append(nearest_integer(target))
            S_n = sp.Poly(sp.expand(sum(
                z[k] * t**k * (1 - t) ** (n - k)
                for k in range(n + 1)
            )), t, domain=sp.ZZ)
            assert all(z[k] == 0 for k in range(r))
            assert all(z[k] == 0 for k in range(n - 4, n + 1))
            G_n = sp.Poly(sp.expand(
                2 * sp.diff(W, t) * S_n.as_expr()
                + W * sp.diff(S_n.as_expr(), t)
            ), t, domain=sp.ZZ)
            assert sp.rem(G_n.as_expr(), t**4, t) == 0
            assert sp.rem(G_n.as_expr(), (t - 1) ** 4, t) == 0
            assert moment(G_n.as_expr(), W) == 0
            rows.append({
                "case": case,
                "n": n,
                "degree_S_n": str(S_n.degree()),
                "degree_G_n": str(G_n.degree()),
                "nonzero_raw_channels": sum(value != 0 for value in z),
                "coefficient_sha256": hashlib.sha256(
                    str(G_n.all_coeffs()).encode()
                ).hexdigest(),
            })
    return {
        "rows": rows,
        "scope": (
            "These rows verify exact divisibility and zero moment; convergence "
            "is proved by the all-n weighted estimates, not by this table."
        ),
    }


def farey_checks() -> dict[str, object]:
    grid_rows = []
    for left, width in [
        (Fraction(7, 13), Fraction(1, 20)),
        (Fraction(-11, 7), Fraction(3, 101)),
        (Fraction(1001, 997), Fraction(1, 997)),
    ]:
        D = width.denominator // width.numerator + 1
        assert Fraction(1, D) < width
        first = math.floor(left * D) + 1
        rational = Fraction(first, D)
        assert left < rational < left + width
        grid_rows.append({
            "left": str(left),
            "width": str(width),
            "D": D,
            "rational": str(rational),
        })

    gap_rows = []
    c_value = 3
    C_value = 4
    for m in [100, 250, 1000]:
        N = m * m
        Q = C_value * m
        lower = Fraction(1, 2) + Fraction(c_value, 4 * N)
        upper = Fraction(1, 2) + Fraction(5 * c_value, 4 * N)
        assert upper - lower == Fraction(c_value, N)
        assert upper - Fraction(1, 2) < Fraction(1, 2 * Q)
        # Any p/q above 1/2 has distance at least 1/(2q).
        for q in range(1, Q + 1):
            p = q // 2 + 1
            candidate = Fraction(p, q)
            if candidate > Fraction(1, 2):
                assert candidate - Fraction(1, 2) >= Fraction(1, 2 * Q)
                assert not (lower < candidate < upper)
        gap_rows.append({
            "N": N,
            "Q": Q,
            "interval": [str(lower), str(upper)],
            "width": str(upper - lower),
        })
    return {
        "grid_rows": grid_rows,
        "farey_gap_rows": gap_rows,
        "general_gap_identity": (
            "p/q-1/2=(2p-q)/(2q)>=1/(2Q) for p/q>1/2 and q<=Q"
        ),
    }


def main() -> None:
    dependency_audit = {}
    for relative, expected in DEPENDENCIES.items():
        observed = sha256(ROOT / relative)
        assert observed == expected, (relative, observed, expected)
        dependency_audit[relative] = observed

    controls = [control_audit(SOURCE), control_audit(Path(__file__))]
    assert all(item["clean"] for item in controls)

    result = {
        "theorem": (
            "exact rational-moment preservation under integer C3 "
            "approximation for native weights"
        ),
        "dependency_audit": dependency_audit,
        "control_audit": controls,
        "moment_image": moment_image_checks(),
        "crt_and_kernel": crt_and_kernel_checks(),
        "bernstein_identities": bernstein_identity_checks(),
        "exact_rounded_examples": exact_rounded_examples(),
        "farey": farey_checks(),
        "scope": {
            "proved_all_parameter": [
                "the integral moment image of every nonzero integral weight is Q",
                "exact rational-moment integer C3 approximation",
                "N*w_N tending to infinity conditionally implies irrationality",
                "width c/N alone does not force a square-root denominator",
            ],
            "not_claimed": [
                "effective degree or coefficient-height bounds",
                "existence of real sign intervals with N*w_N tending to infinity",
                "irrationality or transcendence of e+pi",
            ],
            "native_context": (
                "The global native positive-output range has width O(1/N), "
                "so N*w_N tending to infinity is unavailable in that family."
            ),
        },
    }
    observed_peak = peak_rss_kib()
    assert observed_peak < RSS_GUARD_KIB
    result["rss_guard_kib"] = RSS_GUARD_KIB
    result["rss_guard_passed"] = True

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "peak_rss_kib": observed_peak,
        "status": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
