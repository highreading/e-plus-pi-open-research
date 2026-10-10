#!/usr/bin/env python3
"""Exact replay for the native output moment and congruence-isolation barrier.

The replay proves/checks algebraic identities over exact polynomial rings,
factorial beta responses, the coefficientwise C^3 error constant, and the
Farey normalization.  The PNT statement and the general Bernstein
approximation theorem used in the companion proof are analytic theorems, not
finite extrapolations from this replay.
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
    / "sources/common_kernel_native_output_bernstein_congruence_isolation.md"
)
OUTPUT = (
    ROOT
    / "results/common_kernel_native_output_bernstein_congruence_certificate.json"
)
RSS_GUARD_KIB = 40 * 1024 * 1024

DEPENDENCIES = {
    "results/common_kernel_native_sign_integer_bernstein_hashes.sha256":
        "337f9276d17304927c34427277fbc62f8bb99642cf525a69aa01c6eed818a2f9",
}

x, t = sp.symbols("x t")


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


def gaussian_power_one_minus_i(exponent: int) -> tuple[int, int]:
    real, imaginary = 1, 0
    for _ in range(exponent):
        real, imaginary = real + imaginary, imaginary - real
    return real, imaginary


def native_parameters(exponent: int) -> tuple[int, int, int, int, int]:
    real, imaginary = gaussian_power_one_minus_i(exponent)
    difference = math.factorial(exponent) - real
    assert difference > 0 and difference % 2 == 0
    a_value = -imaginary
    b_value = difference // 2
    return real, imaginary, a_value, b_value, a_value + b_value


def operator(poly: sp.Expr, variable: sp.Symbol = x) -> sp.Expr:
    return sp.expand((1 - variable) * sp.diff(poly, variable) - variable * poly)


def polynomial_integral(poly: sp.Expr, variable: sp.Symbol = x) -> sp.Rational:
    value = sp.integrate(sp.Poly(sp.expand(poly), variable).as_expr(), (variable, 0, 1))
    assert value.is_Rational
    return sp.Rational(value)


def lcm_through(bound: int) -> int:
    value = 1
    for integer in range(1, bound + 1):
        value = math.lcm(value, integer)
    return value


def symbolic_integration_checks() -> dict[str, str]:
    a, b = sp.symbols("a b")
    q_function = sp.Function("q")
    q = q_function(x)
    u = 1 + x**2
    K = -a - b * (1 - x)
    Y = u**2 * q * K
    TY = (1 - x) * sp.diff(Y, x) - x * Y

    exponential_difference = sp.simplify(
        sp.exp(x) * TY - sp.diff(sp.exp(x) * (1 - x) * Y, x)
    )
    assert exponential_difference == 0

    rational_difference = sp.simplify(
        TY / u
        - sp.diff((1 - x) * Y / u, x)
        - (1 - x) * (1 + x) ** 2 * q * K
    )
    assert rational_difference == 0

    W = sp.expand((a + b * t) * t * (2 - t) ** 2)
    expected_W = (
        4 * a * t
        + (4 * b - 4 * a) * t**2
        + (a - 4 * b) * t**3
        + b * t**4
    )
    assert sp.expand(W - expected_W) == 0

    return {
        "exponential_pointwise_difference": str(exponential_difference),
        "rational_pointwise_difference": str(rational_difference),
        "W_expansion": str(W),
        "boundary_values": (
            "Y(0)=-K(0), so the exponential boundary is K(0) and "
            "four times the rational boundary is 4*K(0)"
        ),
    }


def taylor_inverse(exponent: int) -> sp.Poly:
    coefficients = sp.symbols(f"c0:{exponent}")
    candidate = sum(
        coefficients[index] * x**index for index in range(exponent)
    )
    target = sp.expand((1 - x) ** exponent - math.factorial(exponent))
    equations = sp.Poly(operator(candidate) - target, x).all_coeffs()
    solution = sp.solve(equations, coefficients, dict=True)
    assert len(solution) == 1
    result = sp.Poly(sp.expand(candidate.subs(solution[0])), x, domain=sp.ZZ)
    assert operator(result.as_expr()) == target
    return result


def reference_coordinate(exponent: int) -> dict[str, object]:
    real, imaginary, a_value, b_value, A_value = native_parameters(exponent)
    assert imaginary <= 0
    factorial = math.factorial(exponent)
    u = 1 + x**2
    t_x = 1 - x
    K = sp.expand(imaginary - b_value * t_x)
    P0 = taylor_inverse(exponent).as_expr()

    base_numerator = sp.expand(t_x**exponent + operator(K) - factorial)
    base_quotient, base_remainder = sp.div(base_numerator, u, domain=sp.ZZ)
    assert base_remainder == 0
    assert sp.Poly(base_quotient, x).degree() <= exponent - 2
    rho_base = sp.Rational(
        -factorial - (P0 + K).subs(x, 0)
        + 4 * polynomial_integral(base_quotient)
    )

    # This q is used only for exact algebraic replay.  It obeys q(0)=-1;
    # positivity and sign control are not inferred from this sample.
    q = -1 + 2 * x - 3 * x**2 + x**3
    h = sp.expand(1 + u**2 * q)
    assert h.subs(x, 0) == 0
    Y = sp.expand((h - 1) * K)

    changed_numerator = sp.expand(
        t_x**exponent + operator(h * K) - factorial
    )
    changed_quotient, changed_remainder = sp.div(
        changed_numerator, u, domain=sp.ZZ
    )
    assert changed_remainder == 0
    rho_changed = sp.Rational(
        -factorial - (P0 + h * K).subs(x, 0)
        + 4 * polynomial_integral(changed_quotient)
    )

    rational_integral = polynomial_integral(
        sp.cancel(operator(Y) / u)
    )
    moment_x = polynomial_integral(
        (1 - x) * (1 + x) ** 2 * q * K
    )
    assert rational_integral == -A_value + moment_x

    Q = sp.expand(q.subs(x, 1 - t))
    W = sp.expand((a_value + b_value * t) * t * (2 - t) ** 2)
    predicted = sp.Rational(
        rho_base - 5 * A_value - 4 * sp.integrate(W * Q, (t, 0, 1))
    )
    assert predicted == rho_changed
    assert sp.expand(Y - u**2 * q * K) == 0

    base_denominator_divisor = lcm_through(max(1, exponent - 1))
    assert base_denominator_divisor % int(rho_base.q) == 0

    return {
        "N": exponent,
        "R_N": real,
        "I_N": imaginary,
        "a": a_value,
        "b": b_value,
        "A": A_value,
        "degree_P0": str(sp.Poly(P0, x).degree()),
        "degree_base_quotient": str(sp.Poly(base_quotient, x).degree()),
        "rho_reference": str(rho_base),
        "rho_changed_direct": str(rho_changed),
        "rho_changed_single_moment": str(predicted),
        "rational_boundary_plus_moment": str(rational_integral),
    }


def beta_response(
    a_value: int, b_value: int, n: int, k: int
) -> Fraction:
    weights = (
        4 * a_value,
        4 * b_value - 4 * a_value,
        a_value - 4 * b_value,
        b_value,
    )
    value = Fraction(0)
    for j, weight in enumerate(weights, start=1):
        value += (
            4
            * weight
            * Fraction(
                math.factorial(k + j) * math.factorial(n - k),
                math.factorial(n + j + 1),
            )
        )
    return value


def bernstein_ledger_checks() -> dict[str, object]:
    rows = []
    for exponent, n in [(2, 8), (3, 9), (4, 10), (8, 12)]:
        _, imaginary, a_value, b_value, A_value = native_parameters(exponent)
        assert imaginary <= 0
        L = lcm_through(n + 5)
        W = sp.expand((a_value + b_value * t) * t * (2 - t) ** 2)
        responses: list[Fraction] = []
        scaled: list[int] = []
        for k in range(n + 1):
            direct = sp.Rational(
                4
                * sp.integrate(
                    W * t**k * (1 - t) ** (n - k), (t, 0, 1)
                )
            )
            formula = beta_response(a_value, b_value, n, k)
            assert direct == sp.Rational(formula.numerator, formula.denominator)
            assert (L * formula.numerator) % formula.denominator == 0
            responses.append(formula)
            scaled.append(L * formula.numerator // formula.denominator)

        P = -1 + t - t**2
        z = [((3 * k + 1) % 7) - 3 for k in range(n)] + [0]
        Q = sp.expand(P + sum(
            z[k] * t**k * (1 - t) ** (n - k)
            for k in range(n + 1)
        ))
        assert Q.subs(t, 1) == -1

        reference = reference_coordinate(exponent)
        rho_reference = sp.Rational(reference["rho_reference"])
        C = sp.Rational(
            rho_reference
            - 5 * A_value
            - 4 * sp.integrate(W * P, (t, 0, 1))
        )
        assert (L * C).q == 1
        Z = int(L * C) - sum(
            scaled[k] * z[k] for k in range(n + 1)
        )
        rho_ledger = Fraction(Z, L)
        rho_moment = sp.Rational(
            rho_reference
            - 5 * A_value
            - 4 * sp.integrate(W * Q, (t, 0, 1))
        )
        assert rho_moment == sp.Rational(
            rho_ledger.numerator, rho_ledger.denominator
        )

        d0 = math.gcd(abs(Z), L)
        c = Z // d0
        D = L // d0
        assert math.gcd(abs(c), D) == 1
        assert Fraction(c, D) == rho_ledger
        g = math.gcd(math.factorial(exponent), abs(c))
        p = -c // g
        q_denominator = math.factorial(exponent) * D // g
        assert math.gcd(abs(p), q_denominator) == 1

        rows.append({
            "N": exponent,
            "n": n,
            "L_n_plus_5": L,
            "response_count": len(responses),
            "scaled_response_gcd_diagnostic": math.gcd(
                L, *[abs(value) for value in scaled]
            ),
            "Z": Z,
            "d0": d0,
            "c": c,
            "D": D,
            "g": g,
            "reduced_rational_coordinate": f"{c}/{D}",
            "primitive_approximant_coefficients": [p, q_denominator],
        })

    return {
        "representative_rows": rows,
        "scope": (
            "The finite scaled-response gcd entries are diagnostics only; "
            "no all-n gcd claim is inferred from them."
        ),
    }


def falling(value: int, count: int) -> int:
    product = 1
    for offset in range(count):
        product *= value - offset
    return product


def derivative_and_sharpness_checks() -> dict[str, object]:
    checked = 0
    for n_value in range(8, 61):
        minimum = min(
            math.comb(n_value, k_value)
            for k_value in range(4, n_value - 3)
        )
        assert minimum == math.comb(n_value, 4)
        for k_value in range(4, n_value - 3):
            for j_value in range(4):
                lhs = Fraction(
                    falling(k_value, j_value)
                    * falling(n_value - k_value, 3 - j_value),
                    math.comb(n_value - 3, k_value - j_value),
                )
                rhs = Fraction(
                    n_value * (n_value - 1) * (n_value - 2),
                    math.comb(n_value, k_value),
                )
                assert lhs == rhs
                checked += 1

    n_symbol = sp.symbols("n", positive=True)
    basis = t**4 * (1 - t) ** (n_symbol - 4)
    scaled_third = sp.factor(
        n_symbol * sp.diff(basis, t, 3).subs(t, 1 / n_symbol)
    )
    expected_scaled = (
        -n_symbol ** (5 - n_symbol)
        * (n_symbol - 1) ** (n_symbol - 7)
        * (n_symbol**2 - 39 * n_symbol - 22)
    )
    assert sp.simplify(scaled_third - expected_scaled) == 0
    sharp_limit = sp.limit(scaled_third, n_symbol, sp.oo)
    assert sharp_limit == -sp.exp(-1)

    n_bound = sp.symbols("n_bound", integer=True, positive=True)
    simplified_bound = sp.simplify(
        4
        * n_bound
        * (n_bound - 1)
        * (n_bound - 2)
        / sp.binomial(n_bound, 4)
    )
    assert simplified_bound == 96 / (n_bound - 3)

    return {
        "finite_identity_instances_checked": checked,
        "third_derivative_error_multiplier": "96*m_n/(n-3)",
        "scaled_k4_third_derivative": str(scaled_third),
        "scaled_k4_limit": str(sharp_limit),
        "logical_scope": (
            "m_n=o(n) is sharp for a guarantee uniform over arbitrary "
            "coefficientwise residue patterns, not for adaptive sparse choices"
        ),
    }


def farey_isolation_checks() -> dict[str, object]:
    checks = []
    for exponent in [14, 15, 16, 20, 50, 100]:
        # e<3 gives 5e-1<14, and this exact rational comparison finishes
        # Delta_N < 1/N!.
        rational_factor = Fraction(14, exponent + 1)
        assert rational_factor < 1
        checks.append({
            "N": exponent,
            "upper_factor_after_e_lt_3": str(rational_factor),
            "strictly_below_one": True,
        })

    normalization_rows = []
    for exponent, c, D in [
        (14, 37, 19),
        (15, -44, 27),
        (20, 105, 64),
        (50, -1001, 243),
    ]:
        assert math.gcd(abs(c), D) == 1
        g = math.gcd(math.factorial(exponent), abs(c))
        p = -c // g
        q = math.factorial(exponent) * D // g
        assert math.gcd(abs(p), q) == 1
        normalization_rows.append({
            "N": exponent,
            "c": c,
            "D": D,
            "g": g,
            "p": p,
            "q": q,
        })

    return {
        "exact_N_ge_14_checks": checks,
        "normalization_rows": normalization_rows,
        "separation": (
            "distinct reduced rationals with denominators <=sqrt(N!) "
            "are separated by at least 1/N!"
        ),
        "equivalence": (
            "q=N!*D/g <= (N!)^(1/2) iff g/D >= (N!)^(1/2)"
        ),
    }


def main() -> None:
    dependency_audit = {}
    for relative, expected in DEPENDENCIES.items():
        path = ROOT / relative
        observed = sha256(path)
        assert observed == expected, (relative, observed, expected)
        dependency_audit[relative] = observed

    controls = [
        control_audit(SOURCE),
        control_audit(Path(__file__)),
    ]
    assert all(item["clean"] for item in controls)

    result = {
        "theorem": (
            "exact native single-moment ledger; sharp coefficientwise "
            "full-residue rounding scale; sqrt-factorial Farey isolation"
        ),
        "dependency_audit": dependency_audit,
        "control_audit": controls,
        "symbolic_integration": symbolic_integration_checks(),
        "reference_coordinate_checks": [
            reference_coordinate(exponent)
            for exponent in [2, 3, 4, 8, 9, 10, 11, 12]
            if gaussian_power_one_minus_i(exponent)[1] <= 0
        ],
        "bernstein_ledger": bernstein_ledger_checks(),
        "derivative_and_sharpness": derivative_and_sharpness_checks(),
        "farey_isolation": farey_isolation_checks(),
        "scope": {
            "all_parameter_claims": [
                "integration-by-parts and beta-response identities",
                "m_n=o(n) suffices uniformly over arbitrary residue patterns",
                "that scale is necessary for such a uniform guarantee",
                "for N>=14 there is at most one sqrt-factorial candidate",
            ],
            "not_claimed": [
                "adaptive sparse central-channel impossibility",
                "existence or nonexistence of the isolated candidate",
                "the primitive-decay or Roth threshold",
                "any arithmetic classification of e+pi",
            ],
        },
    }
    observed_peak_rss_kib = peak_rss_kib()
    assert observed_peak_rss_kib < RSS_GUARD_KIB
    # Keep the generated certificate byte-deterministic across allocator
    # variations; the exact observed peak is printed by every replay.
    result["rss_guard_kib"] = RSS_GUARD_KIB
    result["rss_guard_passed"] = True

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "peak_rss_kib": observed_peak_rss_kib,
        "status": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
