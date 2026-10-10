#!/usr/bin/env python3
"""Exact boundary/resultant certificate for the large-prime u_7^d branch.

The all-degree theorem is in the companion source note.  This script
certifies the algebraic identities at every simultaneous root with p<2000
and records one nonzero trace-cancellation witness in each Frobenius class
of Gal(Q(zeta_20)^+/Q).  The bounded prime scan is diagnostic only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import sympy as sp

import algebraic_unit_two_log_n5_ideal_content as base
import cyclotomic_unit_linear_ray_padic_reduction as prior_reduction
import cyclotomic_unit_trace_probe as prior


sys.set_int_max_str_digits(0)

Kelt = base.Kelt
Pair = base.Pair
ZERO_PAIR: Pair = (base.ZERO, base.ZERO)
ONE_PAIR: Pair = (base.ONE, base.ZERO)

TRACE_GRAM = (
    (4, -2, 0, 0),
    (-2, 6, 0, 0),
    (0, 0, 10, 0),
    (0, 0, 0, 10),
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reduce_k(a: Kelt, modulus: int) -> Kelt:
    return tuple(value % modulus for value in a)  # type: ignore[return-value]


def reduce_pair(a: Pair, modulus: int) -> Pair:
    return (reduce_k(a[0], modulus), reduce_k(a[1], modulus))


def kadd_mod(a: Kelt, b: Kelt, modulus: int) -> Kelt:
    return tuple((a[j] + b[j]) % modulus for j in range(4))  # type: ignore[return-value]


def kneg_mod(a: Kelt, modulus: int) -> Kelt:
    return tuple(-value % modulus for value in a)  # type: ignore[return-value]


def kscale_mod(coefficient: int, a: Kelt, modulus: int) -> Kelt:
    return tuple(coefficient * value % modulus for value in a)  # type: ignore[return-value]


def kmul_mod(a: Kelt, b: Kelt, modulus: int) -> Kelt:
    return reduce_k(base.kmul(a, b), modulus)


def kpow_mod(a: Kelt, exponent: int, modulus: int) -> Kelt:
    answer = base.ONE
    current = reduce_k(a, modulus)
    while exponent:
        if exponent & 1:
            answer = kmul_mod(answer, current, modulus)
        current = kmul_mod(current, current, modulus)
        exponent //= 2
    return answer


def pmul_mod(a: Pair, b: Pair, modulus: int) -> Pair:
    return reduce_pair(base.pmul(a, b), modulus)


def ppow_mod(a: Pair, exponent: int, modulus: int) -> Pair:
    answer = ONE_PAIR
    current = reduce_pair(a, modulus)
    while exponent:
        if exponent & 1:
            answer = pmul_mod(answer, current, modulus)
        current = pmul_mod(current, current, modulus)
        exponent //= 2
    return answer


def padd_mod(a: Pair, b: Pair, modulus: int) -> Pair:
    return (
        kadd_mod(a[0], b[0], modulus),
        kadd_mod(a[1], b[1], modulus),
    )


def plus_coordinates_mod(a: Pair, modulus: int) -> tuple[int, int, int, int]:
    real, imaginary = a
    return (
        (real[0] - real[2]) % modulus,
        (-real[2]) % modulus,
        imaginary[0] % modulus,
        (imaginary[2] - imaginary[0]) % modulus,
    )


def plus_from_coordinates_mod(
    coordinates: tuple[int, int, int, int], modulus: int
) -> Pair:
    answer = ZERO_PAIR
    for coefficient, basis in zip(coordinates, base.BPLUS):
        scaled = (
            kscale_mod(coefficient, basis[0], modulus),
            kscale_mod(coefficient, basis[1], modulus),
        )
        answer = padd_mod(answer, scaled, modulus)
    return answer


def tau_mod(a: Pair, modulus: int) -> Pair:
    return (reduce_k(a[0], modulus), kneg_mod(a[1], modulus))


def f_from_coordinates_mod(c0: int, c1: int, modulus: int) -> Kelt:
    real_basis = base.BPLUS[1][0]
    return kadd_mod(
        kscale_mod(c0, base.ONE, modulus),
        kscale_mod(c1, real_basis, modulus),
        modulus,
    )


def f_coordinates_mod(a: Kelt, modulus: int) -> tuple[int, int]:
    # An element fixed by zeta_5 -> zeta_5^-1 has coordinates c0+c1*t,
    # t=zeta_5+zeta_5^-1, with c0=a0-a2 and c1=-a2.
    return ((a[0] - a[2]) % modulus, (-a[2]) % modulus)


def f_trace_mod(a: Kelt, modulus: int) -> int:
    c0, c1 = f_coordinates_mod(a, modulus)
    return (2 * c0 - c1) % modulus


def k_multiplication_matrix(a: Kelt) -> tuple[tuple[int, ...], ...]:
    columns = [
        base.kmul(a, tuple(1 if i == j else 0 for i in range(4)))
        for j in range(4)
    ]
    return tuple(
        tuple(columns[column][row] for column in range(4))
        for row in range(4)
    )


def matvec4_mod(
    matrix: tuple[tuple[int, ...], ...],
    vector: tuple[int, int, int, int],
    modulus: int,
) -> tuple[int, int, int, int]:
    a, b, c, d = vector
    return tuple(
        (
            row[0] * a
            + row[1] * b
            + row[2] * c
            + row[3] * d
        )
        % modulus
        for row in matrix
    )  # type: ignore[return-value]


def recurrence_subtract_mod(
    power: tuple[int, int, int, int],
    previous: tuple[int, int, int, int],
    degree: int,
    modulus: int,
) -> tuple[int, int, int, int]:
    return tuple(
        (power[j] - degree * previous[j]) % modulus for j in range(4)
    )  # type: ignore[return-value]


def trace_theta_h_mod(
    theta_coordinates: tuple[int, int, int, int],
    h_value: Kelt,
    modulus: int,
) -> int:
    h0, h1 = f_coordinates_mod(h_value, modulus)
    x0, x1, _, _ = theta_coordinates
    return (
        x0 * (4 * h0 - 2 * h1) + x1 * (-2 * h0 + 6 * h1)
    ) % modulus


def galois_k(a: Kelt, exponent: int) -> Kelt:
    answer = base.ZERO
    for degree, coefficient in enumerate(a):
        if coefficient:
            power = base.kpow(base.ZETA, exponent * degree % 5)
            answer = base.kadd(answer, base.kscale(coefficient, power))
    return answer


def galois_pair(a: Pair, exponent: int) -> Pair:
    sign_i = 1 if exponent % 4 == 1 else -1
    return (
        galois_k(a[0], exponent),
        base.kscale(sign_i, galois_k(a[1], exponent)),
    )


def quotient_frobenius_class(prime: int) -> int:
    residue = prime % 20
    representative = min(residue, (-residue) % 20)
    if representative not in (1, 3, 7, 9):
        raise AssertionError("unexpected unramified residue class")
    return representative


def polynomial_eval_k_mod(
    coefficients: list[int], x: Kelt, modulus: int
) -> Kelt:
    answer = base.ZERO
    for coefficient in reversed(coefficients):
        answer = kmul_mod(answer, x, modulus)
        answer = kadd_mod(
            answer, kscale_mod(coefficient, base.ONE, modulus), modulus
        )
    return answer


def divide_by_y_minus_one(
    coefficients: list[int], modulus: int
) -> list[int]:
    """Divide S(Y) by Y-1, asserting S(1)=0."""
    if sum(coefficients) % modulus:
        raise AssertionError("S(1) was nonzero")
    degree = len(coefficients) - 1
    quotient = [0] * degree
    quotient[degree - 1] = coefficients[degree] % modulus
    for k in range(degree - 1, 0, -1):
        quotient[k - 1] = (
            coefficients[k] + quotient[k]
        ) % modulus
    if (-quotient[0] - coefficients[0]) % modulus:
        raise AssertionError("synthetic division remainder was nonzero")
    return quotient


def differential_identity_check(
    coefficients: list[int], r: int, factorial_r: int, prime: int
) -> bool:
    # Y^2*S'(Y)+(Y-1)*S(Y) = -r!*Y^r modulo p.
    left = [0] * (len(coefficients) + 1)
    for k, coefficient in enumerate(coefficients):
        left[k] = (left[k] - coefficient) % prime
        left[k + 1] = (left[k + 1] + coefficient) % prime
        if k:
            left[k + 1] = (left[k + 1] + k * coefficient) % prime
    expected = [0] * len(left)
    expected[r] = -factorial_r % prime
    return left == expected


def quadratic_resultant_mod(
    quotient: list[int], z_value: Kelt, prime: int
) -> tuple[Kelt, Kelt, Kelt]:
    """Return Res(Y^2-zY+z,Q) and the linear remainder A+B*Y."""
    a_value = base.ZERO
    b_value = base.ZERO
    for coefficient in reversed(quotient):
        new_a = kneg_mod(kmul_mod(b_value, z_value, prime), prime)
        new_b = kadd_mod(
            a_value, kmul_mod(b_value, z_value, prime), prime
        )
        a_value = kadd_mod(
            new_a, kscale_mod(coefficient, base.ONE, prime), prime
        )
        b_value = new_b
    aa = kmul_mod(a_value, a_value, prime)
    ab = kmul_mod(a_value, b_value, prime)
    bb = kmul_mod(b_value, b_value, prime)
    resultant = kadd_mod(
        aa,
        kadd_mod(
            kmul_mod(z_value, ab, prime),
            kmul_mod(z_value, bb, prime),
            prime,
        ),
        prime,
    )
    return resultant, a_value, b_value


def is_zero_k(a: Kelt, modulus: int) -> bool:
    return all(value % modulus == 0 for value in a)


def witness_certificate(
    prime: int,
    degree: int,
    p_eta: Kelt,
    p_bar: Kelt,
    theta_coordinates: tuple[int, int, int, int],
    eta: Kelt,
    eta_bar: Kelt,
    q_value: Kelt,
    z_value: Kelt,
    u7: Pair,
    u7_inverse: Pair,
) -> dict[str, object]:
    r = prime - 1 - degree
    factorials = [1]
    for k in range(1, prime):
        factorials.append(factorials[-1] * k % prime)
    coefficients = [
        factorials[k] if k >= r else 0 for k in range(prime)
    ]
    if sum(coefficients) % prime:
        raise AssertionError("large-prime derangement root did not give S(1)=0")
    quotient = divide_by_y_minus_one(coefficients, prime)
    if sum(quotient) % prime != -factorials[r] % prime:
        raise AssertionError("Q(1)=-r! failed")
    if not differential_identity_check(
        coefficients, r, factorials[r], prime
    ):
        raise AssertionError("factorial-tail differential identity failed")

    eta_inverse: Kelt = (1, 1, 0, 0)
    bar_inverse: Kelt = (0, -1, -1, -1)
    if (
        kmul_mod(eta, eta_inverse, prime) != base.ONE
        or kmul_mod(eta_bar, bar_inverse, prime) != base.ONE
    ):
        raise AssertionError("eta inverse identities failed")
    if kmul_mod(
        base.ksub(eta_inverse, base.ONE),
        base.ksub(bar_inverse, base.ONE),
        prime,
    ) != base.ONE:
        raise AssertionError("(eta^-1-1)(etabar^-1-1)=1 failed")

    q_eta = polynomial_eval_k_mod(quotient, eta_inverse, prime)
    q_bar = polynomial_eval_k_mod(quotient, bar_inverse, prime)
    direct_resultant = kmul_mod(q_eta, q_bar, prime)
    resultant, remainder_a, remainder_b = quadratic_resultant_mod(
        quotient, z_value, prime
    )
    if resultant != direct_resultant:
        raise AssertionError("quadratic resultant reconstruction failed")

    h_mod = factorials[degree]
    h_inverse_squared = pow(h_mod * h_mod % prime, -1, prime)
    p_product = kmul_mod(p_eta, p_bar, prime)
    normalized_h_from_p = kscale_mod(
        h_inverse_squared, p_product, prime
    )
    chi = kpow_mod(q_value, prime - 1, prime)
    normalized_h_boundary = kmul_mod(chi, resultant, prime)
    if normalized_h_from_p != normalized_h_boundary:
        raise AssertionError("boundary H/resultant identity failed")

    residue = prime % 20
    sigma_u = galois_pair(u7, residue)
    if ppow_mod(u7, prime, prime) != reduce_pair(sigma_u, prime):
        raise AssertionError("Frobenius action on u_7 failed")
    boundary_theta = pmul_mod(
        sigma_u, ppow_mod(u7_inverse, r + 1, prime), prime
    )
    theta_pair = plus_from_coordinates_mod(theta_coordinates, prime)
    if boundary_theta != theta_pair:
        raise AssertionError("boundary unit identity failed")

    relative_trace_pair = padd_mod(
        boundary_theta, tau_mod(boundary_theta, prime), prime
    )
    relative_coordinates = plus_coordinates_mod(
        relative_trace_pair, prime
    )
    if relative_coordinates[2:] != (0, 0):
        raise AssertionError("relative trace did not land in F")
    w_value = f_from_coordinates_mod(
        relative_coordinates[0], relative_coordinates[1], prime
    )
    final_f_element = kmul_mod(
        normalized_h_boundary, w_value, prime
    )
    final_trace = f_trace_mod(final_f_element, prime)
    normalized_direct_trace = (
        trace_theta_h_mod(theta_coordinates, p_product, prime)
        * h_inverse_squared
    ) % prime
    if final_trace != normalized_direct_trace or final_trace:
        raise AssertionError("boundary trace decomposition failed")

    split = sp.legendre_symbol(5, prime) == 1
    final_coordinates = f_coordinates_mod(final_f_element, prime)
    component_record: dict[str, object]
    if split:
        square_root_5 = int(sp.sqrt_mod(5, prime, all_roots=True)[0])
        inv_two = pow(2, -1, prime)
        t_roots = [
            (-1 + square_root_5) * inv_two % prime,
            (-1 - square_root_5) * inv_two % prime,
        ]
        components = [
            (final_coordinates[0] + final_coordinates[1] * root) % prime
            for root in t_roots
        ]
        if sum(components) % prime or any(value == 0 for value in components):
            raise AssertionError("split nonzero trace cancellation failed")
        component_record = {
            "F_mod_p": "F_p x F_p",
            "t_roots": t_roots,
            "final_two_components": components,
            "relation": "y_plus+y_minus=0 with both components nonzero",
        }
    else:
        conjugate_coordinates = (
            (final_coordinates[0] - final_coordinates[1]) % prime,
            (-final_coordinates[1]) % prime,
        )
        negative_coordinates = tuple(
            -value % prime for value in final_coordinates
        )
        if conjugate_coordinates != negative_coordinates:
            raise AssertionError("inert nonzero trace cancellation failed")
        component_record = {
            "F_mod_p": "F_(p^2)",
            "final_coordinates_in_1_t_basis": list(final_coordinates),
            "Frobenius_conjugate_coordinates": list(conjugate_coordinates),
            "relation": "y^p=-y with y nonzero",
        }

    if is_zero_k(resultant, prime) or is_zero_k(w_value, prime):
        raise AssertionError("the witness was not a genuine trace cancellation")

    expected_chi = (
        base.ONE
        if split
        else kpow_mod(z_value, 2, prime)
    )
    if chi != expected_chi:
        raise AssertionError("q^(p-1) Frobenius-class factor failed")

    return {
        "p": prime,
        "d": degree,
        "r=p-1-d": r,
        "p_mod_20": residue,
        "quotient_frobenius_class": quotient_frobenius_class(prime),
        "F_split": split,
        "S_1_mod_p": sum(coefficients) % prime,
        "Q_1_mod_p": sum(quotient) % prime,
        "minus_r_factorial_mod_p": -factorials[r] % prime,
        "factorial_tail_differential_identity": True,
        "Q_coefficients_sha256": hashlib.sha256(
            repr(quotient).encode()
        ).hexdigest(),
        "quadratic_remainder_A_coordinates": list(
            f_coordinates_mod(remainder_a, prime)
        ),
        "quadratic_remainder_B_coordinates": list(
            f_coordinates_mod(remainder_b, prime)
        ),
        "resultant_F_coordinates": list(
            f_coordinates_mod(resultant, prime)
        ),
        "resultant_nonzero": not is_zero_k(resultant, prime),
        "W_class_r_F_coordinates": list(
            f_coordinates_mod(w_value, prime)
        ),
        "W_class_r_nonzero": not is_zero_k(w_value, prime),
        "chi=q^(p-1)_F_coordinates": list(
            f_coordinates_mod(chi, prime)
        ),
        "normalized_final_F_coordinates": list(final_coordinates),
        "normalized_trace_mod_p": final_trace,
        "component_cancellation": component_record,
        "all_boundary_resultant_checks": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-bound", type=int, default=2000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/cyclotomic_unit_large_prime_boundary_resultant_p2000.json"
        ),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "sources/cyclotomic_unit_large_prime_boundary_resultant.md"
        ),
    )
    args = parser.parse_args()
    if args.prime_bound != 2000:
        raise ValueError("the frozen certificate uses prime-bound=2000")

    eta: Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    q_value = base.kmul(eta, eta_bar)
    eta_inverse: Kelt = (1, 1, 0, 0)
    bar_inverse: Kelt = (0, -1, -1, -1)
    z_value = base.kmul(eta_inverse, bar_inverse)
    if (
        q_value != (2, 0, 1, 1)
        or base.kmul(q_value, z_value) != base.ONE
        or base.kadd(eta_inverse, bar_inverse) != z_value
    ):
        raise AssertionError("quadratic eta identities changed")

    w: Pair = (base.ZERO, base.kpow(base.ZETA, 4))
    u7 = prior.cyclotomic_unit(w, 7)
    u7_inverse = prior.pinverse_unit(u7)
    if base.plus_coordinates(u7) != (2, 1, -1, -1):
        raise AssertionError("u_7 coordinates changed")

    eta_matrix = k_multiplication_matrix(eta)
    bar_matrix = k_multiplication_matrix(eta_bar)
    u7_matrix = tuple(
        tuple(int(value) for value in row)
        for row in base.plus_multiplication_matrix(u7).tolist()
    )

    class_counts = {
        str(class_value): {
            "prime_count": 0,
            "E_d(-1)_root_count_for_1<=d<p": 0,
            "simultaneous_trace_root_count": 0,
        }
        for class_value in (1, 3, 7, 9)
    }
    simultaneous_data: list[
        tuple[int, int, Kelt, Kelt, tuple[int, int, int, int]]
    ] = []
    prime_compact_rows = []

    for prime_object in sp.primerange(3, args.prime_bound):
        prime = int(prime_object)
        if prime == 5:
            continue
        class_value = quotient_frobenius_class(prime)
        class_counts[str(class_value)]["prime_count"] += 1
        a_value = 1
        eta_power = base.ONE
        bar_power = base.ONE
        p_eta = base.ONE
        p_bar = base.ONE
        theta_coordinates = (1, 0, 0, 0)
        root_count = 0
        common_count = 0
        for degree in range(1, prime):
            a_value = (1 - degree * a_value) % prime
            eta_power = matvec4_mod(eta_matrix, eta_power, prime)
            bar_power = matvec4_mod(bar_matrix, bar_power, prime)
            p_eta = recurrence_subtract_mod(
                eta_power, p_eta, degree, prime
            )
            p_bar = recurrence_subtract_mod(
                bar_power, p_bar, degree, prime
            )
            theta_coordinates = matvec4_mod(
                u7_matrix, theta_coordinates, prime
            )
            if a_value:
                continue
            root_count += 1
            p_product = reduce_k(base.kmul(p_eta, p_bar), prime)
            trace_value = trace_theta_h_mod(
                theta_coordinates, p_product, prime
            )
            if trace_value == 0:
                common_count += 1
                simultaneous_data.append(
                    (
                        prime,
                        degree,
                        p_eta,
                        p_bar,
                        theta_coordinates,
                    )
                )
        class_counts[str(class_value)][
            "E_d(-1)_root_count_for_1<=d<p"
        ] += root_count
        class_counts[str(class_value)][
            "simultaneous_trace_root_count"
        ] += common_count
        prime_compact_rows.append((prime, class_value, root_count, common_count))

    expected_pairs = [(13, 8), (31, 28), (277, 199), (1879, 1427)]
    actual_pairs = [(row[0], row[1]) for row in simultaneous_data]
    if actual_pairs != expected_pairs:
        raise AssertionError("finite simultaneous-root list changed")
    if {
        quotient_frobenius_class(prime) for prime, _ in expected_pairs
    } != {1, 3, 7, 9}:
        raise AssertionError("finite witnesses no longer cover every class")

    witness_records = [
        witness_certificate(
            prime,
            degree,
            p_eta,
            p_bar,
            theta_coordinates,
            eta,
            eta_bar,
            q_value,
            z_value,
            u7,
            u7_inverse,
        )
        for prime, degree, p_eta, p_bar, theta_coordinates in simultaneous_data
    ]

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependencies = [
        Path(base.__file__).resolve(),
        Path(prior.__file__).resolve(),
        Path(prior_reduction.__file__).resolve(),
        Path("sources/cyclotomic_unit_linear_ray_padic_reduction.md").resolve(),
    ]
    if not source_path.exists() or not all(path.exists() for path in dependencies):
        raise FileNotFoundError("source or dependency was missing")

    result = {
        "description": (
            "Exact factorial-tail, quadratic-resultant, Frobenius-class, "
            "and nonzero trace-cancellation certificate for the p>d branch."
        ),
        "scope_warning": (
            "The boundary/resultant identities are all-degree theorems for "
            "p not dividing 20.  The p<2000 root list is diagnostic only and "
            "is not extrapolated to larger primes."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependencies
        ],
        "field_data": {
            "K": "Q(zeta_20)^+",
            "F": "Q(sqrt(5))",
            "Gal_K_Q_quotient_classes": [[1, 19], [3, 17], [7, 13], [9, 11]],
            "q=eta*etabar_coordinates": list(q_value),
            "z=q^-1=eta^-1+etabar^-1_coordinates": list(z_value),
            "eta_inverse_coordinates": list(eta_inverse),
            "etabar_inverse_coordinates": list(bar_inverse),
            "u7_plus_coordinates": list(base.plus_coordinates(u7)),
        },
        "proved_boundary_identities": {
            "r": "p-1-d",
            "S_p_r": "sum_(k=r)^(p-1) k!*Y^k mod p",
            "truncation": "E_d(-x)=-x^(p-1)*S_p_r(x^-1)",
            "derangement_root": "E_d(-1)=0 iff S_p_r(1)=0",
            "simple_factor": (
                "S=(Y-1)Q, Q(1)=S'(1)=-r! != 0 mod p"
            ),
            "differential_identity": (
                "Y^2*S'(Y)+(Y-1)*S(Y)=-r!*Y^r mod p"
            ),
            "quadratic_resultant": (
                "E_d(-eta)E_d(-etabar)=q^(p-1)*"
                "Res_Y(Y^2-q^-1*Y+q^-1,Q)"
            ),
            "unit_boundary": (
                "u7^d=sigma_p(u7)*u7^(-r-1) mod p"
            ),
            "trace_condition": (
                "tr_(O_F/p over F_p)(q^(p-1)*resultant*"
                "Tr_(K/F)(sigma_p(u7)*u7^(-r-1)))=0"
            ),
        },
        "trace_does_not_factor": {
            "split_classes": (
                "For p mod 20 in {1,9,11,19}, O_F/p=F_p x F_p and "
                "the condition is y_plus+y_minus=0, not y_plus=y_minus=0."
            ),
            "inert_classes": (
                "For p mod 20 in {3,7,13,17}, O_F/p=F_(p^2) and "
                "the condition is y+y^p=0, not y=0."
            ),
            "finite_exact_witnesses_cover_all_four_classes": True,
            "all_witnesses_have_nonzero_resultant_and_nonzero_unit_factor": True,
        },
        "finite_diagnostics": {
            "prime_range": "3<=p<2000, p!=5",
            "class_counts": class_counts,
            "simultaneous_root_pairs": [
                {"p": prime, "d": degree} for prime, degree in expected_pairs
            ],
            "prime_rows_sha256": hashlib.sha256(
                repr(prime_compact_rows).encode()
            ).hexdigest(),
            "witness_records": witness_records,
            "warning": "No finite pattern is extrapolated beyond p<2000.",
        },
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
