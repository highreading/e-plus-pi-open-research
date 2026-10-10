#!/usr/bin/env python3
"""Replay the pointed-Euler bounded-eliminant audit.

The all-parameter arguments are in the companion source.  Finite exact
grids below audit identities and bounds.  The degree-1644 computation is
an exact counterexample to a universal higher-subdiscriminant implication;
it is not extrapolated to an asymptotic gcd theorem.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import resource
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "sources/root_unity_adjacent_euler_bounded_eliminant_no_go.md"
)
OUTPUT = (
    ROOT
    / "results/root_unity_adjacent_euler_bounded_eliminant_certificate.json"
)

# This is a failure guard, not a memory allocation or a Colab RAM cap.
RSS_GUARD_KIB = 8 * 1024 * 1024

DEPENDENCIES = {
    "results/root_unity_adjacent_euler_descent_discriminant_hashes.sha256":
        "57de6b30c8efc92532d3d7c8292e2467d176983baeb20443d7f17cfecf4f7f14",
    "results/root_unity_adjacent_euler_irregular_seed_hashes.sha256":
        "c4e0b694a4f57130370e1f66869f5d862536e21708a78a0fa1c8655463525f0f",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def control_audit(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    bad = [
        {"offset": index, "byte": byte}
        for index, byte in enumerate(data)
        if byte < 32 and byte != 10
    ]
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "forbidden_control_bytes": bad,
        "clean": not bad,
    }


def secant_even_exact(max_m: int) -> list[int]:
    """Return E_0,E_2,...,E_{2 max_m} in the sech convention."""
    values = [1]
    for n in range(1, max_m + 1):
        values.append(
            -sum(
                math.comb(2 * n, 2 * j) * values[j]
                for j in range(n)
            )
        )
    return values


def trial_prime(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    for divisor in range(3, math.isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def seed_modular_gcd() -> dict[str, object]:
    """Compute the complete M=3288 polynomial gcd over F_151483."""
    prime = 151483
    degree = 3288
    m = degree // 2
    assert trial_prime(prime)
    assert degree < prime

    factorial = [1] * (degree + 1)
    for index in range(1, degree + 1):
        factorial[index] = factorial[index - 1] * index % prime
    inverse_factorial = [1] * (degree + 1)
    inverse_factorial[degree] = pow(factorial[degree], -1, prime)
    for index in range(degree, 0, -1):
        inverse_factorial[index - 1] = (
            inverse_factorial[index] * index % prime
        )

    # Exact O(m^2) inversion of cosh in exponential-generating
    # coordinates.  There is no floating-point or probabilistic step.
    euler = [1]
    for n in range(1, m + 1):
        factorial_2n = factorial[2 * n]
        total = 0
        for j in range(n):
            choose = (
                factorial_2n
                * inverse_factorial[2 * j]
                % prime
                * inverse_factorial[2 * n - 2 * j]
                % prime
            )
            total += choose * euler[j]
        euler.append((-total) % prime)

    assert euler[m - 1] == 0
    assert euler[m] == 0

    coefficients = []
    for k in range(m + 1):
        choose = (
            factorial[degree]
            * inverse_factorial[2 * k]
            % prime
            * inverse_factorial[degree - 2 * k]
            % prime
        )
        coefficients.append(choose * euler[m - k] % prime)

    coefficient_digest = hashlib.sha256(
        b"".join(value.to_bytes(4, "little") for value in coefficients)
    ).hexdigest()

    Y = sp.symbols("Y")
    polynomial = sp.Poly.from_list(
        list(reversed(coefficients)),
        gens=Y,
        modulus=prime,
    )
    assert polynomial.degree() == m
    assert polynomial.LC() == 1
    assert polynomial.nth(0) == 0
    assert polynomial.nth(1) == 0
    assert polynomial.nth(2) != 0
    assert polynomial.eval(1) == 0

    gcd_full = sp.gcd(polynomial, polynomial.diff()).monic()
    assert gcd_full.as_expr() == Y

    permanent = sp.Poly(Y - 1, Y, modulus=prime)
    quotient = sp.exquo(polynomial, permanent)
    gcd_quotient = sp.gcd(quotient, quotient.diff()).monic()
    assert quotient.degree() == m - 1
    assert gcd_quotient.as_expr() == Y

    inverse_four = pow(4, -1, prime)
    normalized_scale = pow(pow(4, m - 1, prime), -1, prime)
    p_at_zero = int(quotient.eval(1)) % prime
    p_at_zero = p_at_zero * normalized_scale % prime
    p_at_two = int(quotient.eval(9)) % prime
    p_at_two = p_at_two * normalized_scale % prime
    p_at_six = int(quotient.eval(25)) % prime
    p_at_six = p_at_six * normalized_scale % prime

    assert inverse_four == 37871
    assert (-inverse_four) % prime == 113612
    assert p_at_zero == 22227
    assert p_at_zero
    assert p_at_two == 1
    assert p_at_six == 131225

    return {
        "p": prime,
        "M": degree,
        "m": m,
        "p_is_prime_by_trial_division": True,
        "coefficient_count": len(coefficients),
        "coefficient_sha256_u32le": coefficient_digest,
        "E_M_minus_2_mod_p": euler[m - 1],
        "E_M_mod_p": euler[m],
        "degree_f_M": polynomial.degree(),
        "constant_coefficient_mod_p": int(polynomial.nth(0)),
        "linear_coefficient_mod_p": int(polynomial.nth(1)),
        "quadratic_coefficient_nonzero": True,
        "gcd_f_with_derivative": str(gcd_full.as_expr()),
        "degree_after_removing_Y_minus_1": quotient.degree(),
        "gcd_quotient_with_derivative": str(gcd_quotient.as_expr()),
        "normalized_gcd": f"U + {inverse_four}",
        "normalized_double_root": (-inverse_four) % prime,
        "normalized_gcd_degree": 1,
        "next_principal_subresultant_nonzero": True,
        "special_values_mod_p": {
            "P_m_at_0": p_at_zero,
            "P_m_at_2": p_at_two,
            "P_m_at_6": p_at_six,
        },
    }


def main() -> None:
    dependency_checks = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        assert actual == expected, (relative, expected, actual)
        dependency_checks[relative] = {
            "expected": expected,
            "actual": actual,
        }

    X, U, Y, T = sp.symbols("X U Y T")
    grid_max_m = 12
    secant = secant_even_exact(grid_max_m)
    rows = []
    h_polynomials: dict[int, sp.Poly] = {}
    p_polynomials: dict[int, sp.Poly] = {}

    for m in range(1, grid_max_m + 1):
        degree = 2 * m
        square = sp.Poly(
            sum(
                sp.binomial(degree, 2 * k)
                * secant[m - k]
                * Y**k
                for k in range(m + 1)
            ),
            Y,
            domain=sp.ZZ,
        )
        centered = sp.Poly(square.as_expr().subs(Y, T**2), T)
        ordinary = sp.Poly(sp.euler(degree, X), X, domain=sp.ZZ)
        ordinary_from_genocchi = X**degree
        for r_index in range(1, m + 1):
            genocchi_index = (
                sp.Integer(2)
                * (1 - 2 ** (2 * r_index))
                * sp.bernoulli(2 * r_index)
            )
            coefficient = (
                sp.binomial(degree, 2 * r_index - 1)
                * genocchi_index
                / (2 * r_index)
            )
            assert coefficient.is_Integer
            ordinary_from_genocchi += (
                coefficient * X ** (degree - 2 * r_index + 1)
            )
        assert sp.expand(ordinary_from_genocchi) == ordinary.as_expr()
        invariant = sp.Poly(
            sp.expand(square.as_expr().subs(Y, 1 + 4 * U) / 4**m),
            U,
            domain=sp.ZZ,
        )

        assert ordinary.monic()
        assert ordinary.as_expr() == sp.expand(
            invariant.as_expr().subs(U, X * (X - 1))
        )
        assert square.as_expr() == sp.expand(
            4**m * invariant.as_expr().subs(U, (Y - 1) / 4)
        )
        assert centered.as_expr() == sp.expand(
            4**m * invariant.as_expr().subs(U, (T**2 - 1) / 4)
        )
        assert invariant.eval(0) == 0
        quotient = sp.exquo(invariant, sp.Poly(U, U))
        assert quotient.degree() == m - 1
        assert quotient.LC() == 1
        assert quotient.eval(2) == 1

        genocchi = sp.Integer(2) * (1 - 2**degree) * sp.bernoulli(degree)
        assert genocchi.is_Integer
        assert quotient.eval(0) == -genocchi

        coefficient_bound = 2 ** (m + 1) * math.factorial(degree)
        assert max(abs(int(c)) for c in invariant.all_coeffs()) <= (
            coefficient_bound
        )
        assert max(abs(int(c)) for c in quotient.all_coeffs()) <= (
            coefficient_bound
        )

        h_polynomials[m] = invariant
        p_polynomials[m] = quotient
        if m >= 2:
            left = sp.Poly(
                (4 * U + 1) * sp.diff(invariant.as_expr(), U, 2)
                + 2 * sp.diff(invariant.as_expr(), U),
                U,
            )
            right = sp.Poly(
                degree * (degree - 1) * h_polynomials[m - 1].as_expr(),
                U,
            )
            assert left == right

            common = math.gcd(abs(secant[m]), abs(secant[m - 1]))
            disc = int(sp.discriminant(quotient.as_expr(), U))
            assert disc
            assert disc % common == 0

            r = m - 1
            hadamard_squared = (
                ((r + 1) * coefficient_bound**2) ** (r - 1)
                * (r**3 * coefficient_bound**2) ** r
            )
            assert disc**2 <= hadamard_squared

            recurrence_resultant = int(
                sp.resultant(
                    quotient.as_expr(),
                    p_polynomials[m - 1].as_expr(),
                    U,
                )
            )
            rows.append({
                "M": degree,
                "degree_P_m": quotient.degree(),
                "P_m_at_0": str(quotient.eval(0)),
                "P_m_at_2": str(quotient.eval(2)),
                "coefficient_height": max(
                    abs(int(c)) for c in quotient.all_coeffs()
                ),
                "declared_coefficient_bound": str(coefficient_bound),
                "gcd_E_M_E_M_minus_2": str(common),
                "disc_P_m_bits": abs(disc).bit_length(),
                "disc_divisible_by_common_gcd": True,
                "hadamard_squared_bound": True,
                "recurrence_resultant_nonzero": bool(
                    recurrence_resultant
                ),
                "recurrence_resultant_bits": (
                    abs(recurrence_resultant).bit_length()
                    if recurrence_resultant
                    else 0
                ),
            })

    # Direct symbolic checks of the centered shift and its derivative
    # jets on the same finite grid.
    shift_rows = []
    for m in range(2, grid_max_m + 1):
        degree = 2 * m
        centered = sp.Poly(
            sum(
                sp.binomial(degree, 2 * k)
                * secant[k]
                * T ** (degree - 2 * k)
                for k in range(m + 1)
            ),
            T,
        )
        shift = sp.expand(
            centered.as_expr().subs(T, T + 1)
            + centered.as_expr().subs(T, T - 1)
        )
        assert shift == 2 * T**degree
        for derivative_order in range(degree):
            jet = sp.diff(
                centered.as_expr(), T, derivative_order
            )
            assert sp.expand(jet.subs(T, 1) + jet.subs(T, -1)) == 0
            if derivative_order % 2 == 0:
                assert jet.subs(T, 1) == 0
        shift_rows.append({
            "M": degree,
            "jets_checked": degree,
            "shift_identity": True,
            "parity_or_permanent_root": True,
        })

    seed = seed_modular_gcd()

    source_text = SOURCE.read_text(encoding="utf-8")
    tags = [int(value) for value in re.findall(r"\\tag\{(\d+)\}", source_text)]
    assert tags == list(range(1, 36)), tags
    source_control = control_audit(SOURCE)
    script_control = control_audit(Path(__file__).resolve())
    assert source_control["clean"] and script_control["clean"]
    assert source_text.count(r"\(") == source_text.count(r"\)")
    displays_open = sum(
        line.strip() == r"\[" for line in source_text.splitlines()
    )
    displays_close = sum(
        line.strip() == r"\]" for line in source_text.splitlines()
    )
    assert displays_open == displays_close == 35
    assert "conceivable eliminant" in source_text
    assert "does not prove or disprove its transcendence" in source_text

    peak_rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss_kib < RSS_GUARD_KIB, peak_rss_kib

    result = {
        "schema": (
            "root_unity_adjacent_euler_bounded_eliminant_certificate/v1"
        ),
        "checked_utc": "2026-08-27",
        "claim_scope": {
            "all_parameter_proofs_in_source": True,
            "finite_grids_are_formula_audits_only": True,
            "seed_refutes_universal_higher_subdiscriminant_implication":
                True,
            "rules_out_every_conceivable_eliminant": False,
            "bounds_J_N_by_exp_o_N_log_N": False,
            "classification_of_e_plus_pi": False,
        },
        "dependencies": dependency_checks,
        "integral_invariant_grid": {
            "m_min": 1,
            "m_max": grid_max_m,
            "ordinary_E_2m_equals_H_m_of_X_X_minus_1": True,
            "genocchi_integral_coefficient_formula": True,
            "H_m_equals_U_P_m_integrally": True,
            "affine_centering_identity": True,
            "P_m_at_2_is_one": True,
            "appell_differential_recurrence": True,
            "coefficient_height_bound": True,
            "rows_m_at_least_2": rows,
        },
        "centered_shift_grid": {
            "m_min": 2,
            "m_max": grid_max_m,
            "rows": shift_rows,
        },
        "exact_seed_modular_gcd": seed,
        "source_audit": {
            "equation_tags": tags,
            "equation_tags_contiguous_1_through_35": True,
            "inline_math_balanced": True,
            "display_math_pairs": displays_open,
            "source_control": source_control,
            "script_control": script_control,
        },
        "resource_audit": {
            "guard_kib": RSS_GUARD_KIB,
            "guard_is_not_an_allocation_or_colab_limit": True,
            "peak_rss_kib_omitted_from_deterministic_payload": True,
            "guard_passed": True,
            "hardware_accelerator_used": False,
            "accelerator_reason": (
                "Exact modular and symbolic polynomial arithmetic is "
                "CPU-bound at this degree and the replay is already "
                "memory-light."
            ),
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "ok",
        "output": str(OUTPUT.relative_to(ROOT)),
        "grid_rows": len(rows),
        "seed_degree": seed["degree_f_M"],
        "seed_gcd": seed["gcd_f_with_derivative"],
        "seed_quotient_gcd": seed["gcd_quotient_with_derivative"],
        "peak_rss_kib": peak_rss_kib,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
