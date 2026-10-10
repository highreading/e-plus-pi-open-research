#!/usr/bin/env python3
"""Exact p-adic reduction for the fixed cyclotomic-unit ray theta_d=u_7^d.

This certificate deliberately separates proved all-degree identities from a
finite diagnostic scan.  It verifies:

* the derangement state A_d=(-1)^d !d has period m modulo every tested m;
* the complete algebraic state which produces
  X_d=Tr(u_7^d P_d(eta)P_d(etabar)) resets at the proved unit-order period;
* the universal unramified period p^k(p^f-1), f=ord_20(p), is valid;
* the exact valuation/separation identities for gcd(D0,C);
* the finite exception lists through max_d (diagnostics only);
* selected first levels of the nested simultaneous-root tree.

No finite record is extrapolated to an all-degree gcd bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Callable, TypeVar

import sympy as sp

import algebraic_unit_two_log_n5_ideal_content as base
import cyclotomic_unit_trace_probe as prior


sys.set_int_max_str_digits(0)

Kelt = base.Kelt
Pair = base.Pair
T = TypeVar("T")

TRACE_GRAM = (
    (4, -2, 0, 0),
    (-2, 6, 0, 0),
    (0, 0, 10, 0),
    (0, 0, 0, 10),
)
ONE_PAIR: Pair = (base.ONE, base.ZERO)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trace_product(a: Pair, b: Pair) -> int:
    x = base.plus_coordinates(a)
    y = base.plus_coordinates(b)
    return sum(
        x[j] * TRACE_GRAM[j][k] * y[k]
        for j in range(4)
        for k in range(4)
    )


def kord20(prime: int) -> int:
    if math.gcd(prime, 20) != 1:
        raise ValueError("ord_20 is used only at primes not dividing 20")
    value = prime % 20
    order = 1
    while value != 1:
        value = value * prime % 20
        order += 1
    return order


def reduce_k(a: Kelt, modulus: int) -> Kelt:
    return tuple(value % modulus for value in a)  # type: ignore[return-value]


def reduce_pair(a: Pair, modulus: int) -> Pair:
    return (reduce_k(a[0], modulus), reduce_k(a[1], modulus))


def kadd_mod(a: Kelt, b: Kelt, modulus: int) -> Kelt:
    return tuple((a[j] + b[j]) % modulus for j in range(4))  # type: ignore[return-value]


def kscale_mod(coefficient: int, a: Kelt, modulus: int) -> Kelt:
    return tuple(coefficient * value % modulus for value in a)  # type: ignore[return-value]


def kmul_mod(a: Kelt, b: Kelt, modulus: int) -> Kelt:
    return reduce_k(base.kmul(a, b), modulus)


def pmul_mod(a: Pair, b: Pair, modulus: int) -> Pair:
    return reduce_pair(base.pmul(a, b), modulus)


def kpow_mod(a: Kelt, exponent: int, modulus: int) -> Kelt:
    answer = base.ONE
    current = reduce_k(a, modulus)
    while exponent:
        if exponent & 1:
            answer = kmul_mod(answer, current, modulus)
        current = kmul_mod(current, current, modulus)
        exponent //= 2
    return answer


def ppow_mod(a: Pair, exponent: int, modulus: int) -> Pair:
    answer = ONE_PAIR
    current = reduce_pair(a, modulus)
    while exponent:
        if exponent & 1:
            answer = pmul_mod(answer, current, modulus)
        current = pmul_mod(current, current, modulus)
        exponent //= 2
    return answer


def plus_coordinates_mod(a: Pair, modulus: int) -> tuple[int, int, int, int]:
    """Fixed-field coordinates modulo m, without integer equality checks."""
    real, imaginary = a
    return (
        (real[0] - real[2]) % modulus,
        (-real[2]) % modulus,
        imaginary[0] % modulus,
        (imaginary[2] - imaginary[0]) % modulus,
    )


def trace_product_mod(a: Pair, b: Pair, modulus: int) -> int:
    x = plus_coordinates_mod(a, modulus)
    y = plus_coordinates_mod(b, modulus)
    return sum(
        x[j] * TRACE_GRAM[j][k] * y[k]
        for j in range(4)
        for k in range(4)
    ) % modulus


def multiplicative_order(
    element: T,
    one: T,
    multiply: Callable[[T, T, int], T],
    power: Callable[[T, int, int], T],
    modulus: int,
    exponent_bound: int,
) -> int:
    if power(element, exponent_bound, modulus) != one:
        raise AssertionError("the proposed unit exponent was invalid")
    order = exponent_bound
    for prime, exponent in sp.factorint(exponent_bound).items():
        for _ in range(int(exponent)):
            candidate = order // int(prime)
            if power(element, candidate, modulus) != one:
                break
            order = candidate
    # Keep multiply in the signature to make the ring operation explicit and
    # catch accidental mismatches between the two supplied operations.
    if power(element, order, modulus) != one or multiply(one, element, modulus) != reduce_like(
        element, modulus
    ):
        raise AssertionError("multiplicative-order reconstruction failed")
    return order


def reduce_like(value: T, modulus: int) -> T:
    if len(value) == 2 and isinstance(value[0], tuple):  # type: ignore[arg-type,index]
        return reduce_pair(value, modulus)  # type: ignore[arg-type,return-value]
    return reduce_k(value, modulus)  # type: ignore[arg-type,return-value]


def modular_state_records(
    length: int,
    modulus: int,
    eta: Kelt,
    eta_bar: Kelt,
    u7: Pair,
) -> tuple[list[int], list[int], dict[str, object]]:
    """Return A_d and X_d modulo modulus for 0<=d<length."""
    a_value = 1
    eta_power = base.ONE
    bar_power = base.ONE
    p_eta = base.ONE
    p_bar = base.ONE
    theta = ONE_PAIR
    a_values = [1 % modulus]
    x_values = [4 % modulus]
    for d in range(1, length):
        a_value = (1 - d * a_value) % modulus
        eta_power = kmul_mod(eta_power, eta, modulus)
        bar_power = kmul_mod(bar_power, eta_bar, modulus)
        p_eta = kadd_mod(
            eta_power, kscale_mod(-d, p_eta, modulus), modulus
        )
        p_bar = kadd_mod(
            bar_power, kscale_mod(-d, p_bar, modulus), modulus
        )
        theta = pmul_mod(theta, u7, modulus)
        p_product = kmul_mod(p_eta, p_bar, modulus)
        x_value = trace_product_mod(theta, (p_product, base.ZERO), modulus)
        a_values.append(a_value)
        x_values.append(x_value)
    state = {
        "A": a_value,
        "eta_power": list(eta_power),
        "etabar_power": list(bar_power),
        "P_eta": list(p_eta),
        "P_etabar": list(p_bar),
        "theta_coordinates": list(plus_coordinates_mod(theta, modulus)),
        "X": x_values[-1],
    }
    return a_values, x_values, state


def state_at(
    degree: int,
    modulus: int,
    eta: Kelt,
    eta_bar: Kelt,
    u7: Pair,
) -> dict[str, object]:
    a_values, x_values, state = modular_state_records(
        degree + 1, modulus, eta, eta_bar, u7
    )
    state["A"] = a_values[-1]
    state["X"] = x_values[-1]
    return state


def expected_reset_state(modulus: int) -> dict[str, object]:
    return {
        "A": 1 % modulus,
        "eta_power": list(base.ONE),
        "etabar_power": list(base.ONE),
        "P_eta": list(base.ONE),
        "P_etabar": list(base.ONE),
        "theta_coordinates": [1, 0, 0, 0],
        "X": 4 % modulus,
    }


def valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("the certificate does not request v_p(0)")
    answer = 0
    value = abs(value)
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def factor_record(value: int) -> dict[str, int]:
    return {
        str(int(prime)): int(exponent)
        for prime, exponent in sorted(sp.factorint(abs(value)).items())
    }


def truncated_exp_k_mod(x: Kelt, degree: int, prime: int) -> Kelt:
    """sum_{j=0}^degree (-x)^j/j! in O_Q(zeta5)/p, prime>degree."""
    answer = base.ONE
    term = base.ONE
    minus_x = kscale_mod(-1, x, prime)
    for j in range(1, degree + 1):
        term = kmul_mod(term, minus_x, prime)
        term = kscale_mod(pow(j, -1, prime), term, prime)
        answer = kadd_mod(answer, term, prime)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=1000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/cyclotomic_unit_linear_ray_padic_reduction.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/cyclotomic_unit_linear_ray_padic_reduction.md"),
    )
    args = parser.parse_args()
    if args.max_d < 1000:
        raise ValueError("max-d must be at least 1000")

    eta: Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    w: Pair = (base.ZERO, base.kpow(base.ZETA, 4))
    u7 = prior.cyclotomic_unit(w, 7)
    if base.plus_coordinates(u7) != (2, 1, -1, -1):
        raise AssertionError("u_7 coordinates changed")
    if base.kmul(eta, eta_bar) != (2, 0, 1, 1):
        raise AssertionError("eta*etabar identity changed")

    # Exact recurrence scan.  The exception lists are finite diagnostics;
    # the recurrence and the gcd-separation divisibilities are all-degree
    # identities proved in the companion source.
    derangement = 1
    factorial = 1
    ell = 1
    eta_power = base.ONE
    bar_power = base.ONE
    p_eta = base.ONE
    p_bar = base.ONE
    theta = ONE_PAIR
    c_exceptions = []
    x_exceptions = []
    compact_rows = []
    selected_degrees = {2, 4, 8, 12, 28, 100, 199, 500, args.max_d}
    recurrence_cross_check_degrees = {2, 4, 8, 12, 28, 100, 199}
    selected_records = []
    valuation_checks = True
    separation_checks = True
    recurrence_cross_checks = True

    for d in range(1, args.max_d + 1):
        derangement = d * derangement + (-1) ** d
        factorial *= d
        ell = math.lcm(ell, d)
        eta_power = base.kmul(eta_power, eta)
        bar_power = base.kmul(bar_power, eta_bar)
        p_eta = base.ksub(eta_power, base.kscale(d, p_eta))
        p_bar = base.ksub(bar_power, base.kscale(d, p_bar))
        theta = base.pmul(theta, u7)
        p_product = base.kmul(p_eta, p_bar)
        x_value = trace_product(theta, (p_product, base.ZERO))
        delta = math.gcd(derangement, factorial)
        d0 = derangement // delta
        c_value = 2 * ell * x_value
        gcd_x = math.gcd(abs(d0), abs(x_value))
        gcd_c = math.gcd(abs(d0), abs(c_value))

        if d >= 2:
            separation_checks &= gcd_x != 0 and gcd_c % gcd_x == 0
            separation_checks &= (2 * ell * gcd_x) % gcd_c == 0
            if not separation_checks:
                raise AssertionError("gcd separation failed")

        if gcd_c > 1 and d >= 2:
            c_exceptions.append(
                {
                    "d": d,
                    "gcd_D0_C": str(gcd_c),
                    "factorization": factor_record(gcd_c),
                }
            )
        if gcd_x > 1 and d >= 2:
            x_exceptions.append(
                {
                    "d": d,
                    "gcd_D0_X": str(gcd_x),
                    "factorization": factor_record(gcd_x),
                }
            )

        # Factoring D0 itself is neither needed nor attempted.  At primes not
        # dividing C both sides of the gcd-valuation formula are zero.  Thus
        # it is enough to check every prime dividing the (usually tiny) gcd.
        primes_to_check = set(sp.factorint(gcd_c)) if d >= 2 else set()
        for prime_object in primes_to_check:
            prime = int(prime_object)
            vp_d0 = max(
                valuation(derangement, prime) - valuation(factorial, prime), 0
            )
            vp_ell = 0
            power = prime
            while power <= d:
                vp_ell += 1
                power *= prime
            predicted = min(
                vp_d0,
                (1 if prime == 2 else 0) + vp_ell + valuation(x_value, prime),
            )
            actual = valuation(gcd_c, prime) if gcd_c % prime == 0 else 0
            valuation_checks &= predicted == actual
        if not valuation_checks:
            raise AssertionError("valuation formula failed")

        compact_rows.append((d, gcd_c, gcd_x))
        if d in recurrence_cross_check_degrees:
            edge = base.edge_integer_data(d, eta, eta_bar)
            recurrence_cross_checks &= edge["p_eta"] == p_eta
            recurrence_cross_checks &= edge["p_bar"] == p_bar
            recurrence_cross_checks &= prior.derangement(d) == derangement
            if not recurrence_cross_checks:
                raise AssertionError("edge recurrence cross-check failed")
        if d in selected_degrees:
            selected_records.append(
                {
                    "d": d,
                    "D0_digits": len(str(abs(d0))),
                    "X_digits": len(str(abs(x_value))),
                    "gcd_D0_X": str(gcd_x),
                    "gcd_D0_C": str(gcd_c),
                    "log_gcd_C_over_gcd_X": format(
                        math.log(gcd_c / gcd_x), ".17g"
                    ),
                    "log_2lcm_upper_bound": format(math.log(2 * ell), ".17g"),
                }
            )

    expected_c_exceptions = [(4, 3), (8, 13), (12, 11), (28, 31), (199, 277)]
    expected_x_exceptions = [(8, 13), (28, 31), (199, 277)]
    if [(row["d"], int(row["gcd_D0_C"])) for row in c_exceptions] != expected_c_exceptions:
        raise AssertionError("finite C-exception list changed")
    if [(row["d"], int(row["gcd_D0_X"])) for row in x_exceptions] != expected_x_exceptions:
        raise AssertionError("finite X-exception list changed")

    # A_d=1-d*A_{d-1} is exactly periodic modulo m with period m.
    period_moduli = [2, 3, 4, 5, 7, 8, 9, 16, 25, 27, 49, 121]
    derangement_period_records = []
    for modulus in period_moduli:
        values = [1]
        for d in range(1, 2 * modulus):
            values.append((1 - d * values[-1]) % modulus)
        passed = all(values[d + modulus] == values[d] for d in range(modulus))
        if not passed:
            raise AssertionError("derangement A-state period failed")
        derangement_period_records.append(
            {"modulus": modulus, "proved_period": modulus, "check": passed}
        )

    # Actual mod-p unit orders and the resulting smaller state-reset periods.
    order_primes = [3, 7, 11, 13, 31, 277]
    order_records = []
    root_count_primes = {3, 7, 11, 13, 31}
    for prime in order_primes:
        residue_degree = kord20(prime)
        exponent_bound = prime**residue_degree - 1
        eta_order = multiplicative_order(
            eta,
            base.ONE,
            kmul_mod,
            kpow_mod,
            prime,
            exponent_bound,
        )
        bar_order = multiplicative_order(
            eta_bar,
            base.ONE,
            kmul_mod,
            kpow_mod,
            prime,
            exponent_bound,
        )
        u7_order = multiplicative_order(
            u7,
            ONE_PAIR,
            pmul_mod,
            ppow_mod,
            prime,
            exponent_bound,
        )
        reset_period = math.lcm(prime, eta_order, bar_order, u7_order)
        algebraic_reset_check = (
            reset_period % prime == 0
            and kpow_mod(eta, reset_period, prime) == base.ONE
            and kpow_mod(eta_bar, reset_period, prime) == base.ONE
            and ppow_mod(u7, reset_period, prime) == ONE_PAIR
        )
        if not algebraic_reset_check:
            raise AssertionError("actual-order algebraic reset conditions failed")
        direct_reset_check: bool | None = None
        if reset_period <= 50_000:
            reset = state_at(reset_period, prime, eta, eta_bar, u7)
            direct_reset_check = reset == expected_reset_state(prime)
            if not direct_reset_check:
                raise AssertionError("actual-order state reset failed")
        record: dict[str, object] = {
            "p": prime,
            "ord_20_p": residue_degree,
            "orders_eta_etabar_u7": [eta_order, bar_order, u7_order],
            "actual_order_reset_period": reset_period,
            "universal_period_k1": prime * exponent_bound,
            "algebraic_state_reset_conditions": algebraic_reset_check,
            "direct_iterated_state_reset_if_feasible": direct_reset_check,
        }
        if prime in root_count_primes:
            a_values, x_values, _ = modular_state_records(
                reset_period, prime, eta, eta_bar, u7
            )
            a_roots = sum(value == 0 for value in a_values)
            common_roots = sum(
                aa == 0 and xx == 0 for aa, xx in zip(a_values, x_values)
            )
            record["A_roots_in_actual_period"] = a_roots
            record["simultaneous_A_X_roots_in_actual_period"] = common_roots
        order_records.append(record)

    # Nested universal periods T_{p,k}=p^k(p^f-1).  We record exact root
    # counts at small levels.  This is a diagnostic view of the proved finite
    # root tree, not evidence that a branch must or must not continue.
    tree_specs = [(3, 1), (3, 2), (11, 1)]
    root_tree_records = []
    for prime, level in tree_specs:
        residue_degree = kord20(prime)
        base_factor = prime**residue_degree - 1
        period_level = prime**level * base_factor
        period_next = prime * period_level
        modulus_next = prime ** (level + 1)
        reset_level = state_at(
            period_level, modulus_level := prime**level, eta, eta_bar, u7
        )
        if reset_level != expected_reset_state(modulus_level):
            raise AssertionError("universal period failed at level k")
        a_values, x_values, reset_next = modular_state_records(
            period_next + 1, modulus_next, eta, eta_bar, u7
        )
        if reset_next != expected_reset_state(modulus_next):
            raise AssertionError("universal period failed at level k+1")
        roots_level = [
            r
            for r in range(period_level)
            if a_values[r] % modulus_level == 0
            and x_values[r] % modulus_level == 0
        ]
        roots_next = [
            r
            for r in range(period_next)
            if a_values[r] == 0 and x_values[r] == 0
        ]
        projection_ok = all(
            (root % period_level) in set(roots_level) for root in roots_next
        )
        lift_enumeration_ok = set(roots_next) == {
            root + digit * period_level
            for root in roots_level
            for digit in range(prime)
            if a_values[root + digit * period_level] == 0
            and x_values[root + digit * period_level] == 0
        }
        if not projection_ok or not lift_enumeration_ok:
            raise AssertionError("nested simultaneous-root tree failed")
        root_tree_records.append(
            {
                "p": prime,
                "level_k": level,
                "T_p_k": period_level,
                "roots_mod_p_to_k": len(roots_level),
                "T_p_k_plus_1": period_next,
                "roots_mod_p_to_k_plus_1": len(roots_next),
                "universal_state_resets_at_both_levels": True,
                "projection_and_p_ary_lift_enumeration": True,
                "next_root_residues_sha256": hashlib.sha256(
                    repr(roots_next).encode()
                ).hexdigest(),
            }
        )

    # For p>d, h and ell are p-adic units.  The three finite exceptions from
    # gcd(D0,X) therefore have the normalized truncated-exponential criterion.
    normalized_large_prime_records = []
    for degree, prime in expected_x_exceptions:
        if prime <= degree:
            raise AssertionError("expected large-prime diagnostic changed")
        e_eta = truncated_exp_k_mod(eta, degree, prime)
        e_bar = truncated_exp_k_mod(eta_bar, degree, prime)
        e_one = sum(
            (-1) ** j * pow(math.factorial(j), -1, prime)
            for j in range(degree + 1)
        ) % prime
        theta_mod = ppow_mod(u7, degree, prime)
        normalized_x = trace_product_mod(
            theta_mod,
            (kmul_mod(e_eta, e_bar, prime), base.ZERO),
            prime,
        )
        if e_one != 0 or normalized_x != 0:
            raise AssertionError("large-prime normalized criterion failed")
        normalized_large_prime_records.append(
            {
                "d": degree,
                "p": prime,
                "p>d": True,
                "E_d_minus_1_mod_p": e_one,
                "trace_u7d_Eeta_Eetabar_mod_p": normalized_x,
            }
        )

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependencies = [
        Path(base.__file__).resolve(),
        Path(prior.__file__).resolve(),
        Path("sources/cyclotomic_unit_cone_selected_gcd.md").resolve(),
    ]
    if not source_path.exists() or not all(path.exists() for path in dependencies):
        raise FileNotFoundError("source or dependency missing")

    result = {
        "description": (
            "Exact all-prime finite-state and unramified p-adic root-tree "
            "reduction for gcd(D0_d,C_d(u_7^d)), plus diagnostics through d=1000."
        ),
        "scope_warning": (
            "The periodicity, valuation, separation, and root-tree reductions "
            "are proved all-degree statements.  The sparse exception lists and "
            "root counts are finite diagnostics only; no exp(o(d log d)) gcd "
            "bound is claimed."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependencies
        ],
        "exact_identities": {
            "derangement_state": "A_0=1, A_d=1-d*A_(d-1), A_d=(-1)^d*!d",
            "derangement_period": "A_(d+m)=A_d mod m",
            "P_recurrence": "P_0(x)=1, P_d(x)=x^d-d*P_(d-1)(x)",
            "X": "Tr_K/Q(u_7^d*P_d(eta)*P_d(etabar))",
            "C": "2*lcm(1,...,d)*X",
            "valuation_formula": (
                "v_p gcd(D0,C)=min(max(v_p(!d)-v_p(d!),0), "
                "v_p(2)+floor(log_p d)+v_p(X))"
            ),
            "gcd_separation": (
                "gcd(D0,X) | gcd(D0,C) | "
                "2*lcm(1,...,d)*gcd(D0,X)"
            ),
            "unramified_universal_period": (
                "T_(p,k)=p^k*(p^ord_20(p)-1), for p not dividing 20"
            ),
        },
        "all_exact_checks": {
            "valuation_formula": valuation_checks,
            "gcd_separation": separation_checks,
            "edge_recurrence_cross_checks": recurrence_cross_checks,
            "derangement_periods": True,
            "actual_unit_order_state_resets": True,
            "universal_root_tree_projection": True,
            "large_prime_normalization": True,
        },
        "derangement_period_records": derangement_period_records,
        "unit_order_and_state_reset_records": order_records,
        "nested_root_tree_records": root_tree_records,
        "finite_diagnostics": {
            "range": f"2<=d<={args.max_d}",
            "gcd_D0_C_nontrivial": c_exceptions,
            "gcd_D0_X_nontrivial": x_exceptions,
            "selected_records": selected_records,
            "all_gcd_rows_sha256": hashlib.sha256(
                repr(compact_rows).encode()
            ).hexdigest(),
            "normalized_p_greater_than_d_records": normalized_large_prime_records,
            "warning": "No finite pattern is extrapolated beyond max_d.",
        },
        "moving_target_warning": (
            "On t_d=d, the normalized Padé coefficient targets have height "
            "O(d log d), not o(t_d).  The accelerated moving-target S-unit "
            "theorem therefore does not apply to this fixed linear ray."
        ),
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
