#!/usr/bin/env python3
"""Exact Smith/prime diagnostics for a unit ray in the unresolved cone.

The companion note proves the general rational-ray Smith reduction and the
sharp primitive threshold.  This script certifies the particularly simple
interior ray theta_d=u_7^d through d=200 by default.  The finite gcd sizes
are diagnostics, not an all-degree gcd theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

import algebraic_unit_two_log_n5_ideal_content as base
import cyclotomic_unit_trace_probe as prior


sys.set_int_max_str_digits(0)

Pair = base.Pair
TRACE_GRAM = sp.Matrix(
    [
        [4, -2, 0, 0],
        [-2, 6, 0, 0],
        [0, 0, 10, 0],
        [0, 0, 0, 10],
    ]
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trace_product(a: Pair, b: Pair) -> int:
    x = sp.Matrix(base.plus_coordinates(a))
    y = sp.Matrix(base.plus_coordinates(b))
    return int((x.T * TRACE_GRAM * y)[0])


def trace_matrix(u: Pair, v: Pair) -> sp.Matrix:
    u_column = sp.Matrix(base.plus_coordinates(u))
    v_column = sp.Matrix(base.plus_coordinates(v))
    return sp.Matrix.vstack(
        (TRACE_GRAM * u_column).T,
        (TRACE_GRAM * v_column).T,
    )


def pair_linear_combination(a: int, x: Pair, b: int, y: Pair) -> Pair:
    return prior.padd(prior.pscale(a, x), prior.pscale(b, y))


def exact_fourth_root_ceiling(value: int) -> int:
    root, exact = sp.integer_nthroot(value, 4)
    return int(root if exact else root + 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/cyclotomic_unit_cone_selected_gcd_d200.json"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("sources/cyclotomic_unit_cone_selected_gcd.md"),
    )
    args = parser.parse_args()
    if args.max_d < 200:
        raise ValueError("max-d must be at least 200")

    eta: base.Kelt = (0, -1, 0, -1)
    eta_bar = base.ksub(base.ONE, eta)
    w: Pair = (base.ZERO, base.kpow(base.ZETA, 4))
    u7 = prior.cyclotomic_unit(w, 7)
    if base.plus_coordinates(u7) != (2, 1, -1, -1):
        raise AssertionError("u_7 coordinates changed")

    multiplication = base.plus_multiplication_matrix(u7)
    expected_multiplication = sp.Matrix(
        [
            [2, 1, -4, -3],
            [1, 1, -3, -1],
            [-1, -1, 2, 1],
            [-1, 0, 1, 1],
        ]
    )
    if multiplication != expected_multiplication:
        raise AssertionError("u_7 multiplication matrix changed")
    characteristic = sp.Poly(
        multiplication.charpoly().as_expr(), multiplication.charpoly().gen
    )
    expected_characteristic = sp.Poly(
        characteristic.gen**4
        - 6 * characteristic.gen**3
        + characteristic.gen**2
        + 4 * characteristic.gen
        + 1,
        characteristic.gen,
    )
    if characteristic != expected_characteristic or multiplication.det() != 1:
        raise AssertionError("u_7 recurrence certificate failed")

    # Exact rational isolating intervals.  These imply that the two negative
    # conjugates have modulus <1/2 and that the smaller positive conjugate is
    # in (1,6/5).  The elementary sine quotient for the distinguished
    # embedding gives sigma_1(u_7)>5, as proved in the source note.
    root_intervals = sp.intervals(characteristic.as_expr(), eps=sp.Rational(1, 1000))
    intervals = [(sp.Rational(a), sp.Rational(b), int(mult)) for (a, b), mult in root_intervals]
    if len(intervals) != 4 or any(mult != 1 for _, _, mult in intervals):
        raise AssertionError("u_7 did not have four simple real roots")
    if not (
        -sp.Rational(1, 2) < intervals[0][0] < intervals[0][1] < 0
        and -sp.Rational(1, 2) < intervals[1][0] < intervals[1][1] < 0
        and 1 < intervals[2][0] < intervals[2][1] < sp.Rational(6, 5)
        and 5 < intervals[3][0] < intervals[3][1]
    ):
        raise AssertionError("root intervals did not certify the cone bounds")

    selected_degrees = {
        2,
        3,
        5,
        8,
        12,
        20,
        50,
        90,
        100,
        150,
        188,
        191,
        199,
        args.max_d,
    }
    selected_records = []
    compact_rows = []
    selected_prime_support: set[int] = set()
    maximum_gcd = (0, 0)
    maximum_extra = (0, 0)
    maximum_normalized_log_after_20 = (0.0, 0)
    all_smith_checks = True
    all_kernel_checks = True
    all_orbit_vectors_primitive = True
    all_safe_pair_checks = True
    all_C_E_integrality_checks = True
    all_denominator_transfer_checks = True
    transfer_exception_records = []

    theta = u7
    for d in range(2, args.max_d + 1):
        theta = base.pmul(theta, u7)
        edge = base.edge_integer_data(d, eta, eta_bar)
        u = edge["u_plus"]
        v = edge["v_plus"]
        matrix = trace_matrix(u, v)
        if d >= 2 and matrix.rank() != 2:
            raise AssertionError(f"trace matrix lost rank at d={d}")

        theta_column = sp.Matrix(base.plus_coordinates(theta))
        if math.gcd(*(abs(int(value)) for value in theta_column)) != 1:
            all_orbit_vectors_primitive = False
            raise AssertionError("a unit orbit vector was not primitive")
        direct_pair = matrix * theta_column
        direct_a, direct_b = int(direct_pair[0]), int(direct_pair[1])
        if direct_a != trace_product(theta, u) or direct_b != trace_product(theta, v):
            raise AssertionError("direct trace pair disagreed with matrix product")
        common = math.gcd(abs(direct_a), abs(direct_b))
        if common == 0:
            raise AssertionError("unit ray produced the zero pair")
        primitive_a = direct_a // common
        primitive_b = direct_b // common

        # Exact safe-pair reduction.  With P_d=d!*A_d, D=!d, h=d!, and
        # ell=lcm(1,...,d), the safe coefficient is (-1)^d*D*C, where
        # C=2*ell*Tr(theta*P_d(eta)*P_d(etabar)).  The safe constant has
        # the form (-1)^d*(-h*C+D*E), E integral.  Dividing gcd(D,h)
        # gives a rationally equivalent pair with coprime D0,h0.
        factorial = math.factorial(d)
        derangement = prior.derangement(d)
        delta = math.gcd(factorial, derangement)
        d0 = derangement // delta
        h0 = factorial // delta
        ell = base.lcm_through(d)
        p_product = base.kmul(edge["p_eta"], edge["p_bar"])
        x_trace = trace_product(theta, (p_product, base.ZERO))
        c_value = 2 * ell * x_trace

        # Reconstruct Q_d=d!*ell*B_d independently and verify that the
        # second integral coordinate is exactly E=5*Tr(theta*(0,-R)),
        # R=P(eta)Q(etabar)-P(etabar)Q(eta).  This checks the integrality
        # input to the denominator-transfer lemma, not just divisibility of
        # the already-cleared output pair.
        p_coefficients = edge["p_coefficients"]
        q_coefficients = [0] * (d + 1)
        for degree in range(d + 1):
            q_coefficients[degree] = -sum(
                p_coefficients[j] * (ell // (degree - j))
                for j in range(degree)
            )
        q_eta = base.keval(q_coefficients, eta)
        q_bar = base.keval(q_coefficients, eta_bar)
        r_value = base.ksub(
            base.kmul(edge["p_eta"], q_bar),
            base.kmul(edge["p_bar"], q_eta),
        )
        z_trace = trace_product(theta, (base.ZERO, base.kneg(r_value)))
        direct_e_value = 5 * z_trace

        safe_scale = int(edge["safe_coordinate_gcd"])
        safe_a = safe_scale * direct_a
        safe_b = safe_scale * direct_b
        signed_safe_a = ((-1) ** d) * safe_a
        signed_safe_b = ((-1) ** d) * safe_b
        safe_ok = signed_safe_a == derangement * c_value
        e_numerator = signed_safe_b + factorial * c_value
        safe_ok &= e_numerator % derangement == 0
        e_value = e_numerator // derangement
        c_e_integrality_ok = (
            isinstance(c_value, int)
            and isinstance(direct_e_value, int)
            and e_value == direct_e_value
        )
        all_C_E_integrality_checks &= c_e_integrality_ok
        safe_ok &= c_e_integrality_ok
        reduced_safe_a = d0 * c_value
        reduced_safe_b = -h0 * c_value + d0 * e_value
        reduced_safe_gcd = math.gcd(abs(reduced_safe_a), abs(reduced_safe_b))
        reduced_safe_pair = (
            reduced_safe_a // reduced_safe_gcd,
            reduced_safe_b // reduced_safe_gcd,
        )
        safe_ok &= reduced_safe_pair in (
            (primitive_a, primitive_b),
            (-primitive_a, -primitive_b),
        )
        all_safe_pair_checks &= safe_ok
        if not safe_ok:
            raise AssertionError("safe-pair reduction failed")

        transfer_common = math.gcd(d0, abs(c_value))
        transfer_divisor = d0 // transfer_common
        transfer_ok = primitive_a % transfer_divisor == 0
        all_denominator_transfer_checks &= transfer_ok
        if not transfer_ok:
            raise AssertionError("denominator-transfer divisor failed")
        if transfer_common != 1:
            transfer_exception_records.append(
                {
                    "d": d,
                    "gcd_D0_C": str(transfer_common),
                    "gcd_D0_C_factorization": {
                        str(prime): exponent
                        for prime, exponent in sorted(
                            (int(p), int(e))
                            for p, e in sp.factorint(transfer_common).items()
                        )
                    },
                    "D0_digits": len(str(d0)),
                    "proved_transfer_divisor_digits": len(str(transfer_divisor)),
                }
            )

        diagonal, left, right = smith_normal_decomp(matrix, domain=sp.ZZ)
        if left * matrix * right != diagonal:
            raise AssertionError("Smith decomposition identity failed")
        alpha = abs(int(diagonal[0, 0]))
        beta = abs(int(diagonal[1, 1]))
        if alpha == 0 or beta == 0 or beta % alpha:
            raise AssertionError("invalid Smith invariant ordering")
        transformed = right.inv() * theta_column
        if any(value.q != 1 for value in transformed):
            raise AssertionError("unimodular Smith coordinates were not integral")
        transformed = sp.Matrix([int(value) for value in transformed])
        if math.gcd(*(abs(int(value)) for value in transformed)) != 1:
            raise AssertionError("Smith coordinate vector lost primitivity")
        transformed_pair = left * direct_pair
        expected_transformed_pair = sp.Matrix(
            [alpha * transformed[0], beta * transformed[1]]
        )
        smith_ok = transformed_pair == expected_transformed_pair
        formula_common = alpha * math.gcd(
            abs(int(transformed[0])),
            (beta // alpha) * abs(int(transformed[1])),
        )
        smith_ok = smith_ok and formula_common == common
        all_smith_checks &= smith_ok
        if not smith_ok:
            raise AssertionError("selected Smith gcd formula failed")

        factors = {int(p): int(e) for p, e in sp.factorint(common).items()}
        selected_prime_support.update(factors)
        kernel_ok = True
        for prime, exponent in factors.items():
            modulus = prime**exponent
            kernel_ok &= all(int(value) % modulus == 0 for value in direct_pair)
            vp_alpha = 0
            alpha_temp = alpha
            while alpha_temp % prime == 0:
                vp_alpha += 1
                alpha_temp //= prime
            vp_beta = 0
            beta_temp = beta
            while beta_temp % prime == 0:
                vp_beta += 1
                beta_temp //= prime
            vp_y1 = 0
            y1_temp = abs(int(transformed[0]))
            while y1_temp and y1_temp % prime == 0:
                vp_y1 += 1
                y1_temp //= prime
            vp_y2 = 0
            y2_temp = abs(int(transformed[1]))
            while y2_temp and y2_temp % prime == 0:
                vp_y2 += 1
                y2_temp //= prime
            kernel_ok &= exponent == min(vp_alpha + vp_y1, vp_beta + vp_y2)
        all_kernel_checks &= kernel_ok
        if not kernel_ok:
            raise AssertionError("prime-adic Smith/kernel formula failed")

        extra = common // alpha
        if common > maximum_gcd[0]:
            maximum_gcd = (common, d)
        if extra > maximum_extra[0]:
            maximum_extra = (extra, d)
        if d >= 20:
            normalized = math.log(extra + 1) / d
            if normalized > maximum_normalized_log_after_20[0]:
                maximum_normalized_log_after_20 = (normalized, d)

        compact_rows.append(
            (
                d,
                direct_a,
                direct_b,
                common,
                alpha,
                beta,
                tuple(int(value) for value in transformed),
            )
        )
        if d in selected_degrees:
            # The canonical determinant element proves g^4 | N(A v-B u).
            wedge = pair_linear_combination(direct_a, v, -direct_b, u)
            wedge_norm = abs(int(base.plus_multiplication_matrix(wedge).det()))
            if wedge_norm == 0 or wedge_norm % common**4:
                raise AssertionError("determinant-norm divisibility failed")
            norm_bound = exact_fourth_root_ceiling(wedge_norm)
            selected_records.append(
                {
                    "d": d,
                    "cleared_pair_gcd": str(common),
                    "cleared_pair_gcd_factorization": {
                        str(prime): exponent for prime, exponent in sorted(factors.items())
                    },
                    "primitive_coefficient_digits": len(str(abs(primitive_a))),
                    "primitive_constant_digits": len(str(abs(primitive_b))),
                    "q_min_digits": len(str(edge["q_min"])),
                    "smith_invariants": [str(alpha), str(beta)],
                    "selected_extra_content": str(extra),
                    "reduced_exponential_denominator_D0_digits": len(str(d0)),
                    "gcd_D0_C": str(transfer_common),
                    "proved_denominator_transfer_divisor_digits": len(
                        str(transfer_divisor)
                    ),
                    "denominator_transfer_divides_primitive_coefficient": (
                        transfer_ok
                    ),
                    "smith_coordinates_first_two": [
                        str(int(transformed[0])),
                        str(int(transformed[1])),
                    ],
                    "smith_coordinates_all_four_are_primitive": True,
                    "wedge_norm_digits": len(str(wedge_norm)),
                    "wedge_norm_fourth_root_bound_digits": len(str(norm_bound)),
                    "wedge_bound_is_weaker_than_trivial_integer_bound": (
                        norm_bound >= abs(direct_a)
                    ),
                    "smith_formula_matches": smith_ok,
                    "prime_kernel_formula_matches": kernel_ok,
                }
            )

    # Same edge data, different powers of the same unit.  This finite exact
    # comparison demonstrates that the fixed coefficient ideal alone does
    # not determine a selected trace gcd.
    edge_two = base.edge_integer_data(2, eta, eta_bar)
    fixed_degree_records = []
    for exponent in (2, 1275):
        multiplier = prior.ppow_unit(u7, exponent)
        aa = trace_product(multiplier, edge_two["u_plus"])
        bb = trace_product(multiplier, edge_two["v_plus"])
        gg = math.gcd(abs(aa), abs(bb))
        fixed_degree_records.append(
            {
                "d": 2,
                "unit_exponent": exponent,
                "selected_trace_gcd": str(gg),
                "primitive_coefficient_digits": len(str(abs(aa // gg))),
            }
        )
    if [int(row["selected_trace_gcd"]) for row in fixed_degree_records] != [50, 994110]:
        raise AssertionError("fixed-degree selected-gcd witnesses changed")

    script_path = Path(__file__).resolve()
    source_path = args.source.resolve()
    dependency_paths = [
        Path(base.__file__).resolve(),
        Path(prior.__file__).resolve(),
        Path("sources/cyclotomic_unit_rational_primitive_chambers.md").resolve(),
        Path("sources/arbitrary_integer_trace_lattice.md").resolve(),
    ]
    if not source_path.exists() or not all(path.exists() for path in dependency_paths):
        raise FileNotFoundError("source or theorem dependency was missing")
    result = {
        "description": (
            "Exact rational-ray recurrence, Smith-coordinate, prime-kernel, "
            "and finite selected-gcd certificate for theta_d=u_7^d."
        ),
        "scope_warning": (
            "The d<=max_d gcd sizes are diagnostics only.  No all-degree "
            "selected-gcd bound, and hence no primitive theorem inside the "
            "open cone, is asserted."
        ),
        "script_sha256": file_sha256(script_path),
        "source_path": str(source_path),
        "source_sha256": file_sha256(source_path),
        "dependencies": [
            {"path": str(path), "sha256": file_sha256(path)}
            for path in dependency_paths
        ],
        "field_and_ray": {
            "field": "K=Q(zeta_20)^+",
            "integral_basis_trace_gram": [
                [int(value) for value in row] for row in TRACE_GRAM.tolist()
            ],
            "u_7_coordinates": list(base.plus_coordinates(u7)),
            "u_7_multiplication_matrix": [
                [int(value) for value in row] for row in multiplication.tolist()
            ],
            "u_7_characteristic_polynomial": str(characteristic.as_expr()),
            "u_7_norm": int(multiplication.det()),
            "exact_real_root_intervals": [
                [str(a), str(b)] for a, b, _ in intervals
            ],
            "cone_certificate": (
                "sigma_1(u_7)>5; both negative conjugates have modulus<1/2; "
                "1<sigma_7(u_7)<6/5; phi<2 and phi^2<3.  Hence the three "
                "cone inequalities hold and lambda_1=mu_1-log(phi) is the "
                "unique raw-value maximum."
            ),
            "sharp_primitive_threshold": (
                "|primitive form| asymp |primitive coefficient|/(d*phi^d)"
            ),
        },
        "smith_reduction": {
            "identity": "S_d*M_d*V_d=[diag(alpha_d,beta_d) 0]",
            "transformed_orbit": "y_d=V_d^(-1)*x_d",
            "selected_gcd_formula": (
                "g_d=alpha_d*gcd(y_1,d,(beta_d/alpha_d)*y_2,d)"
            ),
            "prime_valuation_formula": (
                "v_p(g_d)=min(v_p(alpha_d)+v_p(y_1,d), "
                "v_p(beta_d)+v_p(y_2,d))"
            ),
            "all_smith_checks": all_smith_checks,
            "all_prime_kernel_checks": all_kernel_checks,
            "all_unit_orbit_vectors_primitive": all_orbit_vectors_primitive,
        },
        "denominator_transfer": {
            "safe_pair": "(D*C,-h*C+D*E), with C,E integral",
            "reduced_pair": (
                "(D0*C,-h0*C+D0*E), D0=D/gcd(D,h), "
                "h0=h/gcd(D,h)"
            ),
            "proved_divisor": "D0/gcd(D0,C) divides the primitive coefficient",
            "C_on_this_ray": (
                "2*lcm(1,...,d)*Tr(u_7^d*P_d(eta)*P_d(etabar))"
            ),
            "all_safe_pair_checks": all_safe_pair_checks,
            "all_C_E_integrality_and_reconstruction_checks": (
                all_C_E_integrality_checks
            ),
            "all_transfer_divisibility_checks": all_denominator_transfer_checks,
            "finite_nontrivial_gcd_D0_C_records": transfer_exception_records,
            "scope_warning": (
                "The sparse finite exception list is not extrapolated beyond max_d."
            ),
        },
        "finite_diagnostics": {
            "range": f"2<=d<={args.max_d}",
            "maximum_selected_gcd": str(maximum_gcd[0]),
            "maximum_selected_gcd_degree": maximum_gcd[1],
            "maximum_extra_content_after_alpha": str(maximum_extra[0]),
            "maximum_extra_content_degree": maximum_extra[1],
            "maximum_log_extra_plus_one_over_d_for_d_at_least_20": format(
                maximum_normalized_log_after_20[0], ".17g"
            ),
            "degree_attaining_previous_maximum": maximum_normalized_log_after_20[1],
            "selected_gcd_prime_support": sorted(selected_prime_support),
            "all_rows_sha256": hashlib.sha256(repr(compact_rows).encode()).hexdigest(),
            "selected_records": selected_records,
        },
        "fixed_degree_same_ideal_witnesses": fixed_degree_records,
        "all_exact_checks_pass": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
