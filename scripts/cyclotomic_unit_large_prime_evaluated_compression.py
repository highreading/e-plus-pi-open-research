#!/usr/bin/env python3
"""Exact certificate for the evaluated large-prime compression.

The script verifies the Wilson-evaluation identities at every frozen
large-prime witness, the fixed bilinear trace curve, the u7 relative-trace
recurrence, and the all-degree order-four recurrence for Z_d by a symbolic
tensor-transition calculation. Witness records are finite checks only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp

import algebraic_unit_two_log_n5_ideal_content as base
import cyclotomic_unit_large_prime_boundary_resultant as boundary
import cyclotomic_unit_large_prime_norm_one_certificate as normone
import cyclotomic_unit_trace_probe as prior


sys.set_int_max_str_digits(0)

Kelt = base.Kelt
Pair = base.Pair


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def p_coefficients(degree: int) -> list[int]:
    factorial = 1
    for value in range(2, degree + 1):
        factorial *= value
    answer = []
    current = factorial
    for j in range(degree + 1):
        answer.append((-1) ** (degree - j) * current)
        if j < degree:
            current //= j + 1
    return answer


def pair_add(a: Pair, b: Pair) -> Pair:
    return base.kadd(a[0], b[0]), base.kadd(a[1], b[1])


def pair_tau(a: Pair) -> Pair:
    return a[0], base.kneg(a[1])


def f_coordinates_exact(a: Kelt) -> tuple[int, int]:
    if a[1] != 0 or a[2] != a[3]:
        raise AssertionError("element did not lie in F")
    return a[0] - a[2], -a[2]


def symbolic_z_recurrence_check() -> dict[str, object]:
    """Verify the order-four recurrence as a tensor-state identity."""
    n = sp.symbols("n")
    eta = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    t = (-1, 0, -1, -1)
    zero = base.ZERO

    def kadd(a, b):
        return tuple(sp.expand(x + y) for x, y in zip(a, b))

    def kscale(coefficient, a):
        return tuple(sp.expand(coefficient * x) for x in a)

    def kmul(a, b):
        return tuple(sp.expand(x) for x in base.kmul(a, b))

    def ksum(values):
        answer = zero
        for value in values:
            answer = kadd(answer, value)
        return answer

    def transition(index):
        alpha = kadd(eta, kscale(-(index + 1), base.ONE))
        beta = kscale(index, eta)
        gamma = kadd(eta_bar, kscale(-(index + 1), base.ONE))
        delta = kscale(index, eta_bar)
        return [
            [
                kmul(alpha, gamma),
                kmul(alpha, delta),
                kmul(beta, gamma),
                kmul(beta, delta),
            ],
            [alpha, zero, beta, zero],
            [gamma, delta, zero, zero],
            [base.ONE, zero, zero, zero],
        ]

    def matrix_multiply(a, b):
        return [
            [
                ksum(kmul(a[i][k], b[k][j]) for k in range(4))
                for j in range(4)
            ]
            for i in range(4)
        ]

    identity = [
        [base.ONE if i == j else zero for j in range(4)]
        for i in range(4)
    ]
    product = identity
    rows = [[base.ONE, zero, zero, zero]]
    for shift in range(4):
        product = matrix_multiply(transition(n + shift), product)
        rows.append(product[0])

    a_polynomials = [
        (n + 1) ** 2 * (n + 2) * (n + 3) * (2 * n**2 + 14 * n + 19),
        -(n + 2) * (n + 3)
        * (n**4 + 10 * n**3 + 35 * n**2 + 54 * n + 31),
        -(n + 3) ** 2 * (n**3 + 7 * n**2 + 13 * n + 8),
        -(n**2 + 6 * n + 7) * (n**2 + 6 * n + 10),
        n**2 + 5 * n + 5,
    ]
    b_polynomials = [
        -(n + 1) ** 2 * (n + 2) * (n + 3)
        * (3 * n**2 + 21 * n + 28),
        (n + 2) * (n + 3)
        * (n**4 + 10 * n**3 + 35 * n**2 + 56 * n + 34),
        -(n + 3) ** 2 * (2 * n**2 + 13 * n + 14),
        -3,
        1,
    ]
    coefficients = [
        kadd(
            kscale(a_polynomials[j], base.ONE),
            kscale(b_polynomials[j], t),
        )
        for j in range(5)
    ]
    residuals = []
    for column in range(4):
        residual = ksum(
            kmul(coefficients[j], rows[j][column]) for j in range(5)
        )
        factored = tuple(sp.factor(value) for value in residual)
        if factored != zero:
            raise AssertionError("symbolic tensor recurrence failed")
        residuals.append([str(value) for value in factored])
    return {
        "coefficient_A": [
            str(sp.factor(value)) for value in a_polynomials
        ],
        "coefficient_B": [
            str(sp.factor(value)) for value in b_polynomials
        ],
        "four_tensor_state_residuals": residuals,
        "symbolic_identity_passes": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "results/cyclotomic_unit_large_prime_evaluated_compression.json"
        ),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "sources/cyclotomic_unit_large_prime_evaluated_compression.md"
        ),
    )
    parser.add_argument(
        "--boundary-result",
        type=Path,
        default=Path(
            "results/cyclotomic_unit_large_prime_boundary_resultant_p2000.json"
        ),
    )
    args = parser.parse_args()

    eta: Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    a: Kelt = (1, 1, 0, 0)
    b: Kelt = (0, -1, -1, -1)
    q = base.kmul(eta, eta_bar)
    z = base.kmul(a, b)
    if base.kadd(eta, eta_bar) != base.ONE:
        raise AssertionError("eta+eta_bar identity failed")
    if base.kmul(q, z) != base.ONE:
        raise AssertionError("q inverse identity failed")
    if (
        base.kmul(
            base.ksub(a, base.ONE), base.ksub(b, base.ONE)
        )
        != base.ONE
    ):
        raise AssertionError("forced-factor product failed")

    w: Pair = (base.ZERO, base.kpow(base.ZETA, 4))
    u7 = prior.cyclotomic_unit(w, 7)
    tau_u7 = pair_tau(u7)
    relative_trace = pair_add(u7, tau_u7)
    relative_norm = base.pmul(u7, tau_u7)
    if base.plus_coordinates(relative_trace) != (4, 2, 0, 0):
        raise AssertionError("relative u7 trace changed")
    if base.plus_coordinates(relative_norm) != (-2, -1, 0, 0):
        raise AssertionError("relative u7 norm changed")
    trace_pairing = sp.Matrix([[2, -1], [-1, 3]])
    if trace_pairing.det() != 5:
        raise AssertionError("quadratic trace pairing changed")

    # Exact all-degree sequence checks supplement the symbolic tensor proof.
    p_eta = base.ONE
    p_bar = base.ONE
    eta_power = base.ONE
    bar_power = base.ONE
    theta_powers = [(base.ONE, base.ZERO)]
    z_sequence = []
    for degree in range(41):
        z_sequence.append(f_coordinates_exact(base.kmul(p_eta, p_bar)))
        if degree < 40:
            theta_powers.append(base.pmul(theta_powers[-1], u7))
        eta_power = base.kmul(eta_power, eta)
        bar_power = base.kmul(bar_power, eta_bar)
        p_eta = base.kadd(
            eta_power, base.kscale(-(degree + 1), p_eta)
        )
        p_bar = base.kadd(
            bar_power, base.kscale(-(degree + 1), p_bar)
        )

    trace_multiplier = prior.plus_from_coordinates((4, 2, 0, 0))
    norm_negative = prior.plus_from_coordinates((2, 1, 0, 0))
    for degree in range(39):
        predicted = pair_add(
            base.pmul(trace_multiplier, theta_powers[degree + 1]),
            base.pmul(norm_negative, theta_powers[degree]),
        )
        if theta_powers[degree + 2] != predicted:
            raise AssertionError("u7 power recurrence failed")

    symbolic_record = symbolic_z_recurrence_check()
    n_symbol = sp.symbols("n")
    a_expr = [
        sp.sympify(value)
        for value in symbolic_record["coefficient_A"]
    ]
    b_expr = [
        sp.sympify(value)
        for value in symbolic_record["coefficient_B"]
    ]

    def f_multiply(
        x: tuple[int, int], y: tuple[int, int]
    ) -> tuple[int, int]:
        x0, x1 = x
        y0, y1 = y
        return (
            x0 * y0 + x1 * y1,
            x0 * y1 + x1 * y0 - x1 * y1,
        )

    for n_value in range(37):
        total = (0, 0)
        for j in range(5):
            coefficient = (
                int(a_expr[j].subs(n_symbol, n_value)),
                int(b_expr[j].subs(n_symbol, n_value)),
            )
            term = f_multiply(
                coefficient, z_sequence[n_value + j]
            )
            total = total[0] + term[0], total[1] + term[1]
        if total != (0, 0):
            raise AssertionError("exact Z sequence recurrence failed")

    boundary_data = json.loads(args.boundary_result.read_text())
    witnesses = boundary_data["finite_diagnostics"]["witness_records"]
    witness_records = []
    for witness in witnesses:
        prime = int(witness["p"])
        degree = int(witness["d"])
        r = int(witness["r=p-1-d"])
        r_coeffs = normone.r_coefficients(prime, r)
        r_at_a = boundary.polynomial_eval_k_mod(
            r_coeffs, a, prime
        )
        r_at_b = boundary.polynomial_eval_k_mod(
            r_coeffs, b, prime
        )
        coefficients_p = p_coefficients(degree)
        p_at_eta = boundary.polynomial_eval_k_mod(
            coefficients_p, eta, prime
        )
        p_at_bar = boundary.polynomial_eval_k_mod(
            coefficients_p, eta_bar, prime
        )

        a_minus_one = boundary.kadd_mod(
            a, boundary.kneg_mod(base.ONE, prime), prime
        )
        b_minus_one = boundary.kadd_mod(
            b, boundary.kneg_mod(base.ONE, prime), prime
        )
        left_a = boundary.kmul_mod(
            a_minus_one, r_at_a, prime
        )
        right_a = boundary.kmul_mod(
            boundary.kpow_mod(a, prime - 1, prime),
            p_at_eta,
            prime,
        )
        left_b = boundary.kmul_mod(
            b_minus_one, r_at_b, prime
        )
        right_b = boundary.kmul_mod(
            boundary.kpow_mod(b, prime - 1, prime),
            p_at_bar,
            prime,
        )
        if left_a != right_a or left_b != right_b:
            raise AssertionError("Wilson evaluated compression failed")

        resultant_r = boundary.kmul_mod(r_at_a, r_at_b, prime)
        z_degree = boundary.kmul_mod(
            p_at_eta, p_at_bar, prime
        )
        chi = boundary.kpow_mod(q, prime - 1, prime)
        if (
            boundary.kmul_mod(chi, resultant_r, prime)
            != z_degree
        ):
            raise AssertionError("M=chi^-1*Z failed")

        theta_d = boundary.ppow_mod(u7, degree, prime)
        trace_pair = boundary.padd_mod(
            theta_d, boundary.tau_mod(theta_d, prime), prime
        )
        trace_k = trace_pair[0]
        trace_product = boundary.kmul_mod(
            z_degree, trace_k, prime
        )
        if boundary.f_trace_mod(trace_product, prime) != 0:
            raise AssertionError("fixed bilinear trace equation failed")
        z_coordinates = boundary.f_coordinates_mod(
            z_degree, prime
        )
        t_coordinates = boundary.f_coordinates_mod(
            trace_k, prime
        )
        curve_value = (
            2 * z_coordinates[0] * t_coordinates[0]
            - z_coordinates[0] * t_coordinates[1]
            - z_coordinates[1] * t_coordinates[0]
            + 3 * z_coordinates[1] * t_coordinates[1]
        ) % prime
        if curve_value:
            raise AssertionError("coordinate curve equation failed")
        witness_records.append(
            {
                "p": prime,
                "d": degree,
                "r": r,
                "R_evaluation_identities": True,
                "M_equals_chi_inverse_Z": True,
                "Z_coordinates_mod_p": list(z_coordinates),
                "T_coordinates_mod_p": list(t_coordinates),
                "bilinear_curve_value_mod_p": curve_value,
            }
        )

    source_path = args.source.resolve()
    script_path = Path(__file__).resolve()
    dependency_paths = [
        Path(base.__file__).resolve(),
        Path(boundary.__file__).resolve(),
        Path(normone.__file__).resolve(),
        Path(prior.__file__).resolve(),
        args.boundary_result.resolve(),
        Path(
            "sources/cyclotomic_unit_large_prime_boundary_resultant.md"
        ).resolve(),
        Path(
            "sources/cyclotomic_unit_large_prime_norm_one_obstruction.md"
        ).resolve(),
    ]
    if (
        not source_path.exists()
        or not all(path.exists() for path in dependency_paths)
    ):
        raise FileNotFoundError("source or dependency missing")

    result = {
        "description": (
            "Exact Wilson-evaluated compression, fixed bilinear curve, "
            "and symbolic recurrence certificate."
        ),
        "scope_warning": (
            "All algebraic identities and recurrences are proved exactly. "
            "The four witness records are finite checks only. No uniform "
            "large-prime gcd bound is claimed."
        ),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "script_sha256": file_sha256(script_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependency_paths
        ],
        "proved_compression": {
            "evaluated_resultant": (
                "M_(p,r)=chi_p^(-1)*Z_d mod p"
            ),
            "Z_d": "P_d(eta)*P_d(eta_bar)",
            "T_d": "Tr_(K/F)(u_7^d)",
            "fixed_curve": (
                "2*z0*w0-z0*w1-z1*w0+3*z1*w1=0 mod p"
            ),
            "trace_pairing_determinant": 5,
            "Z_recurrence_order": 4,
            "T_recurrence": (
                "T_(n+2)=(4+2*t)T_(n+1)+(2+t)T_n"
            ),
        },
        "symbolic_Z_recurrence": symbolic_record,
        "exact_sequence_check_range": {
            "Z_n": [0, 40],
            "recurrence_n": [0, 36],
        },
        "witness_reconstructions": witness_records,
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
