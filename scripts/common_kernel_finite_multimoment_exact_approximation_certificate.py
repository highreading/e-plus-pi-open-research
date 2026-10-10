#!/usr/bin/env python3
"""Exact replay for finite moment images and two-native exact approximation.

Finite examples replay the Wronskian formal-adjoint identities, the native
double kernel, weighted Bernstein normalization, endpoint sign algebra, and
factorial elimination.  The source proves the all-parameter statements; no
finite row is extrapolated.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/common_kernel_finite_multimoment_exact_approximation.md"
OUTPUT = (
    ROOT
    / "results/common_kernel_finite_multimoment_exact_approximation_certificate.json"
)
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_native_exact_moment_integer_approximation_hashes.sha256":
        "aa35956007909d980f86d43909eaad180d56b9c80a654059425513a1debbb6b9",
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


def integral(poly: sp.Expr) -> sp.Rational:
    return sp.Rational(
        sp.integrate(sp.Poly(sp.expand(poly), t).as_expr(), (t, 0, 1))
    )


def D(weight: sp.Expr, poly: sp.Expr) -> sp.Expr:
    return sp.expand(2 * sp.diff(weight, t) * poly + weight * sp.diff(poly, t))


def formal_adjoint_coordinate_checks() -> dict[str, object]:
    weights = [
        1 + t,
        1 + t + t**2,
        2 - t + t**3,
    ]
    full_wronskian = sp.wronskian(weights, t)
    assert full_wronskian != 0

    y = sp.Function("y")(t)
    rows = []
    for j in range(3):
        others = [weights[index] for index in range(3) if index != j]
        star_expression = sp.expand(sp.wronskian(others + [y], t))
        coefficients = []
        remainder = star_expression
        for order in range(3):
            derivative = sp.diff(y, t, order)
            coefficient = sp.expand(star_expression.coeff(derivative))
            coefficients.append(coefficient)
            remainder = sp.expand(remainder - coefficient * derivative)
        assert remainder == 0

        Q = t**8 * (1 - t) ** 8 * (1 + 2 * t)
        adjoint_Q = sp.expand(sum(
            (-1) ** order * sp.diff(coefficients[order] * Q, t, order)
            for order in range(3)
        ))
        coordinate = []
        for index, weight in enumerate(weights):
            observed = integral(weight * adjoint_Q)
            expected = integral(
                sp.expand(star_expression.subs({
                    y: weight,
                    sp.diff(y, t): sp.diff(weight, t),
                    sp.diff(y, t, 2): sp.diff(weight, t, 2),
                })) * Q
            )
            assert observed == expected
            if index != j:
                assert observed == 0
            else:
                assert observed != 0
            coordinate.append(str(observed))
        assert sp.rem(adjoint_Q, t**6, t) == 0
        assert sp.rem(adjoint_Q, (t - 1) ** 6, t) == 0
        rows.append({
            "isolated_coordinate": j,
            "star_coefficients": [str(value) for value in coefficients],
            "moment_vector": coordinate,
            "degree_adjoint_Q": sp.Poly(adjoint_Q, t).degree(),
        })

    dependent = [weights[0], weights[1], 2 * weights[0] - 3 * weights[1]]
    P = 3 - 2 * t + 5 * t**4
    dependent_moments = [integral(weight * P) for weight in dependent]
    assert dependent_moments[2] == 2 * dependent_moments[0] - 3 * dependent_moments[1]

    return {
        "independent_weights": [str(value) for value in weights],
        "full_wronskian": str(full_wronskian),
        "coordinate_rows": rows,
        "dependent_example_moments": [str(value) for value in dependent_moments],
        "dependent_relation": "coordinate_3=2*coordinate_1-3*coordinate_2",
    }


def native_symbolic_checks() -> dict[str, object]:
    a1, b1, a2, b2 = sp.symbols("a1 b1 a2 b2")
    base = t * (2 - t) ** 2
    V1 = sp.expand((a1 + b1 * t) * base)
    V2 = sp.expand((a2 + b2 * t) * base)
    delta = a1 * b2 - a2 * b1
    K = sp.expand(V2 * sp.diff(V1, t) - V1 * sp.diff(V2, t))
    expected_K = sp.expand(-delta * t**2 * (2 - t) ** 4)
    assert sp.expand(K - expected_K) == 0

    U = sp.Function("U")(t)
    cross_left = sp.expand(
        V2 * (2 * sp.diff(V1, t) * U + V1 * sp.diff(U, t))
    )
    cross_boundary = sp.diff(V1 * V2 * U, t)
    assert sp.simplify(cross_left - cross_boundary - K * U) == 0

    A0 = sp.expand(4 * sp.diff(V1, t) * sp.diff(K, t) + 2 * V1 * sp.diff(K, t, 2))
    A1 = sp.expand(2 * sp.diff(V1, t) * K + 3 * V1 * sp.diff(K, t))
    A2 = sp.expand(V1 * K)
    composed = sp.expand(D(V1, D(K, U)))
    expected_composed = sp.expand(
        A0 * U + A1 * sp.diff(U, t) + A2 * sp.diff(U, t, 2)
    )
    assert sp.simplify(composed - expected_composed) == 0

    examples = []
    for case in ["nu_one", "nu_two"]:
        if case == "nu_one":
            native_V1 = sp.expand((2 + t) * base)
            native_V2 = sp.expand((1 + 3 * t) * base)
            nu = 1
        else:
            native_V1 = sp.expand(t * base)
            native_V2 = sp.expand((1 + t) * base)
            nu = 2
        native_K = sp.expand(
            native_V2 * sp.diff(native_V1, t)
            - native_V1 * sp.diff(native_V2, t)
        )
        assert native_K != 0
        r = 4 - nu
        polynomial_U = sp.expand(t**r * (1 - t) ** 6 * (1 + t))
        common = sp.Poly(D(native_V1, D(native_K, polynomial_U)), t, domain=sp.ZZ)
        assert sp.rem(common.as_expr(), t**4, t) == 0
        assert sp.rem(common.as_expr(), (t - 1) ** 4, t) == 0
        assert integral(native_V1 * common.as_expr()) == 0
        assert integral(native_V2 * common.as_expr()) == 0
        examples.append({
            "case": case,
            "nu": nu,
            "r": r,
            "K": str(native_K),
            "degree_common_kernel": common.degree(),
            "coefficient_sha256": hashlib.sha256(
                str(common.all_coeffs()).encode()
            ).hexdigest(),
        })

    return {
        "symbolic_cross_weight": str(K),
        "symbolic_expected_cross_weight": str(expected_K),
        "double_operator_coefficients": [str(A0), str(A1), str(A2)],
        "exact_common_kernel_examples": examples,
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


def weighted_bernstein_checks() -> dict[str, object]:
    identities = 0
    maxima: dict[str, Fraction] = {}
    for nu in [1, 2]:
        r = 4 - nu
        for n in range(14, 101):
            for q in range(6):
                lam = max(0, nu + q - 3)
                for alpha in range(q + 1):
                    for k in range(max(r, alpha), n - 5):
                        if n - k < q - alpha:
                            continue
                        first = Fraction(
                            falling(k, alpha) * falling(n - k, q - alpha),
                            math.comb(n - q, k - alpha),
                        )
                        target_first = Fraction(
                            falling(n, q), math.comb(n, k)
                        )
                        assert first == target_first
                        second = Fraction(
                            math.comb(n - q, k - alpha),
                            math.comb(n - q + lam, k - alpha + lam),
                        )
                        target_second = Fraction(
                            rising(k - alpha + 1, lam),
                            rising(n - q + 1, lam),
                        )
                        assert second == target_second
                        identities += 1

                central_sum = Fraction(0)
                for alpha in range(q + 1):
                    candidates = [
                        Fraction(
                            rising(k - alpha + 1, lam),
                            math.comb(n, k),
                        )
                        for k in range(r, n - 5)
                        if k >= alpha and n - k >= q - alpha
                    ]
                    central_sum += math.comb(q, alpha) * max(candidates)
                bound = Fraction(
                    falling(n, q),
                    2 * rising(n - q + 1, lam),
                ) * central_sum
                scaled = n * bound
                key = f"nu_{nu}_q_{q}_lambda_{lam}"
                maxima[key] = max(maxima.get(key, Fraction(0)), scaled)

    return {
        "exact_identity_instances": identities,
        "finite_n_times_bound_maxima": {
            key: str(value) for key, value in sorted(maxima.items())
        },
        "scope": (
            "The exact endpoint-ratio proof gives O(1/n); n<=100 rows "
            "are diagnostics only."
        ),
    }


def nearest_integer(value: Fraction) -> int:
    if value >= 0:
        return (2 * value.numerator + value.denominator) // (
            2 * value.denominator
        )
    return -nearest_integer(-value)


def rounded_common_kernel_checks() -> dict[str, object]:
    base = t * (2 - t) ** 2
    rows = []
    for case in ["nu_one", "nu_two"]:
        if case == "nu_one":
            V1 = sp.expand((2 + t) * base)
            V2 = sp.expand((1 + 3 * t) * base)
            nu = 1
        else:
            V1 = sp.expand(t * base)
            V2 = sp.expand((1 + t) * base)
            nu = 2
        K = sp.expand(V2 * sp.diff(V1, t) - V1 * sp.diff(V2, t))
        r = 4 - nu
        target_U = sp.expand(t**r * (1 - t) ** 6 * (1 + t) / 16)
        for n in [18, 28, 40]:
            z = []
            for k in range(n + 1):
                value = sp.Rational(target_U.subs(t, sp.Rational(k, n)))
                target = Fraction(
                    int(value.p) * math.comb(n, k), int(value.q)
                )
                z.append(nearest_integer(target))
            assert all(z[k] == 0 for k in range(r))
            assert all(z[k] == 0 for k in range(n - 5, n + 1))
            U_n = sp.Poly(sp.expand(sum(
                z[k] * t**k * (1 - t) ** (n - k)
                for k in range(n + 1)
            )), t, domain=sp.ZZ)
            G_n = sp.Poly(D(V1, D(K, U_n.as_expr())), t, domain=sp.ZZ)
            assert sp.rem(G_n.as_expr(), t**4, t) == 0
            assert sp.rem(G_n.as_expr(), (t - 1) ** 4, t) == 0
            assert integral(V1 * G_n.as_expr()) == 0
            assert integral(V2 * G_n.as_expr()) == 0
            rows.append({
                "case": case,
                "n": n,
                "nonzero_raw_channels": sum(value != 0 for value in z),
                "degree_G_n": str(G_n.degree()),
                "coefficient_sha256": hashlib.sha256(
                    str(G_n.all_coeffs()).encode()
                ).hexdigest(),
            })
    return {
        "rows": rows,
        "scope": "Exact moment/divisibility replay only; convergence is all-n.",
    }


def sign_and_output_checks() -> dict[str, object]:
    a, b, N = sp.symbols("a b N", positive=True)
    H = sp.Function("H")(t)
    alpha = (
        a * (1 - t) + b * t * (2 - t)
    ) / (t * (a + b * t))
    beta = t ** (N - 1) / (a + b * t)
    residual = (
        t**N
        + t * (a + b * t) * sp.diff(H, t)
        + (a * (1 - t) + b * t * (2 - t)) * H
    )
    factorized = sp.expand(
        t * (a + b * t) * (sp.diff(H, t) + alpha * H + beta)
    )
    assert sp.simplify(residual - factorized) == 0
    assert sp.limit(t * alpha, t, 0) == 1

    alpha_a_zero = sp.simplify(alpha.subs(a, 0))
    assert sp.limit(t * alpha_a_zero, t, 0) == 2

    v = t**2 - 2 * t + 2
    q_left = sp.series(((1 - 4 * t**2) - 1) / v**2, t, 0, 4)
    s = sp.symbols("s")
    v_right = 1 + s**2
    q_right = sp.series((s**2 - 1) / v_right**2, s, 0, 4)
    assert q_left.removeO().expand() == -t**2 - 2 * t**3
    assert q_right.removeO().expand() == -1 + 3 * s**2

    symbol = sp.symbols("symbol")
    N_small, M_large, D_common, cN, cM = sp.symbols(
        "N_small M_large D_common cN cM",
        integer=True, positive=True,
    )
    LN = sp.factorial(N_small) * symbol + cN / D_common
    LM = sp.factorial(M_large) * symbol + cM / D_common
    # Replay with concrete indices because symbolic factorial divisibility
    # does not simplify under an inequality assumption.
    elimination_rows = []
    for n_value, m_value in [(2, 3), (4, 8), (8, 12)]:
        ratio = math.factorial(m_value) // math.factorial(n_value)
        left = sp.expand(
            D_common
            * (
                LM.subs(M_large, m_value)
                - ratio * LN.subs(N_small, n_value)
            )
        )
        expected = cM - ratio * cN
        assert sp.simplify(left - expected) == 0
        elimination_rows.append({
            "N": n_value,
            "M": m_value,
            "factorial_ratio": ratio,
        })

    return {
        "residual_factorization_difference": "0",
        "t_alpha_limit_a_positive": "1",
        "t_alpha_limit_a_zero": "2",
        "left_q_jet": str(q_left),
        "right_q_jet": str(q_right),
        "factorial_elimination_rows": elimination_rows,
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
            "finite rational moment image and simultaneous two-native exact "
            "integer C3 approximation"
        ),
        "dependency_audit": dependency_audit,
        "control_audit": controls,
        "formal_adjoint_coordinates": formal_adjoint_coordinate_checks(),
        "native_double_kernel": native_symbolic_checks(),
        "weighted_bernstein": weighted_bernstein_checks(),
        "rounded_common_kernel": rounded_common_kernel_checks(),
        "sign_and_output": sign_and_output_checks(),
        "scope": {
            "proved_all_parameter": [
                "integer image equals rational linear image for finite weights",
                "independent weights have full Q^m image",
                "two independent native moments can be preserved exactly in C3",
                "finite sign-possible native systems admit a common strict profile",
            ],
            "not_claimed": [
                "arbitrary-m exact approximation across Wronskian zeros",
                "effective degree, denominator, or primitive-content gain",
                "irrationality or transcendence of e+pi",
            ],
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
