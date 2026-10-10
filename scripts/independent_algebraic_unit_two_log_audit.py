#!/usr/bin/env python3
"""Independent audit of the paired-log algebraic-unit Rivoal family.

This program deliberately reconstructs the branch, phase, embedding, and
n=5 norm diagnostics rather than importing the candidate certificate.  Exact
symbolic checks are separated from high-precision asymptotic diagnostics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


W20 = tuple[int, int, int, int, int, int, int, int]
W20_ZERO: W20 = (0, 0, 0, 0, 0, 0, 0, 0)
W20_ONE: W20 = (1, 0, 0, 0, 0, 0, 0, 0)
W20_GEN: W20 = (0, 1, 0, 0, 0, 0, 0, 0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def w20_add(a: W20, b: W20) -> W20:
    return tuple(x+y for x, y in zip(a, b))  # type: ignore[return-value]


def w20_scale(n: int, a: W20) -> W20:
    return tuple(n*x for x in a)  # type: ignore[return-value]


def w20_sub(a: W20, b: W20) -> W20:
    return w20_add(a, w20_scale(-1, b))


def w20_mul(a: W20, b: W20) -> W20:
    """Multiply in Z[w]/(Phi_20), independently of the candidate basis."""
    raw = [0]*15
    for j, aj in enumerate(a):
        for k, bk in enumerate(b):
            raw[j+k] += aj*bk
    # Phi_20(X)=X^8-X^6+X^4-X^2+1.
    for degree in range(14, 7, -1):
        value = raw[degree]
        if value:
            raw[degree-2] += value
            raw[degree-4] -= value
            raw[degree-6] += value
            raw[degree-8] -= value
            raw[degree] = 0
    return tuple(raw[:8])  # type: ignore[return-value]


def w20_pow(a: W20, exponent: int) -> W20:
    answer = W20_ONE
    base = a
    while exponent:
        if exponent & 1:
            answer = w20_mul(answer, base)
        base = w20_mul(base, base)
        exponent //= 2
    return answer


def w20_evaluate(coefficients: list[int], x: W20) -> W20:
    answer = W20_ZERO
    for coefficient in reversed(coefficients):
        answer = w20_add(
            w20_mul(answer, x), w20_scale(coefficient, W20_ONE)
        )
    return answer


def lcm_through(n: int) -> int:
    answer = 1
    for value in range(1, n+1):
        answer = math.lcm(answer, value)
    return answer


def independent_n5_content_checks(candidate_content: dict) -> dict:
    """Recompute selected content ideals in the unrelated zeta_20 basis.

    The candidate works in the tensor basis Z[zeta_5,i].  Here w=zeta_20,
    zeta_5=w^4, and i=w^5, so arithmetic is instead performed directly in
    Z[w]/(Phi_20).  This gives an independent representation of O_L.
    """
    w = W20_GEN
    ii = w20_pow(w, 5)
    eta = w20_sub(w20_pow(w, 2), w20_pow(w, 4))
    eta_bar = w20_sub(W20_ONE, eta)
    if w20_mul(w20_add(W20_ONE, w20_pow(w, 4)), eta) != W20_ONE:
        raise AssertionError("independent eta inverse failed")

    # The displayed O_K basis, reduced in the power basis of zeta_20.
    basis = (
        W20_ONE,
        w20_sub(w20_pow(w, 4), w20_pow(w, 6)),
        w20_add(
            w20_add(
                w20_sub(w20_pow(w, 7), w20_pow(w, 5)),
                w20_pow(w, 3),
            ),
            w20_scale(-2, w20_pow(w, 1)),
        ),
        w20_sub(w20_pow(w, 7), w20_pow(w, 3)),
    )
    basis_matrix = sp.Matrix.hstack(*(sp.Matrix(x) for x in basis))

    def plus_coordinates(x: W20) -> tuple[int, int, int, int]:
        solutions = list(sp.linsolve((basis_matrix, sp.Matrix(x))))
        if len(solutions) != 1:
            raise AssertionError("real-subfield coordinate solution not unique")
        vector = tuple(solutions[0])
        if any(value.q != 1 for value in vector):
            raise AssertionError("nonintegral coordinate in displayed O_K basis")
        return tuple(int(value) for value in vector)  # type: ignore[return-value]

    def plus_multiplication_matrix(x: W20) -> sp.Matrix:
        return sp.Matrix.hstack(
            *(sp.Matrix(plus_coordinates(w20_mul(x, element))) for element in basis)
        )

    # Exact trace discriminant of the proposed basis.  This also checks its
    # multiplication closure in this independent field representation.
    trace_gram = sp.Matrix(
        4, 4,
        lambda j, k: sp.trace(plus_multiplication_matrix(w20_mul(basis[j], basis[k]))),
    )
    basis_discriminant = int(trace_gram.det())
    if basis_discriminant != 2000:
        raise AssertionError("unexpected maximal-real-subfield discriminant")

    records_by_d = {record["d"]: record for record in candidate_content["records"]}
    selected_degrees = (1, 2, 3, 7, 15, 72, 167, 200)
    selected_records = []
    for d in selected_degrees:
        h = math.factorial(d)
        ell = lcm_through(d)
        p_coefficients = [
            (-1)**(d-j)*h//math.factorial(j) for j in range(d+1)
        ]
        q_coefficients = [
            -sum(
                p_coefficients[j]*(ell//(degree-j))
                for j in range(degree)
            )
            for degree in range(d+1)
        ]
        a_one = sum(p_coefficients)
        p_eta = w20_evaluate(p_coefficients, eta)
        p_bar = w20_evaluate(p_coefficients, eta_bar)
        q_eta = w20_evaluate(q_coefficients, eta)
        q_bar = w20_evaluate(q_coefficients, eta_bar)
        p_product = w20_mul(p_eta, p_bar)

        safe_u = w20_scale(2*ell*a_one, p_product)
        safe_w = w20_scale(-2*((-1)**d)*h*ell, p_product)
        safe_v = w20_add(
            w20_scale(-5*a_one, w20_mul(p_bar, q_eta)),
            w20_scale(5*a_one, w20_mul(p_eta, q_bar)),
        )
        # D*(-i Lambda)=U*s+W-i*V in the zeta_20 power basis.
        safe_constant = w20_sub(safe_w, w20_mul(ii, safe_v))
        safe_denominator = h**3*ell
        common = safe_denominator
        for coordinate in safe_u+safe_constant:
            common = math.gcd(common, abs(coordinate))
        u = tuple(value//common for value in safe_u)
        v = tuple(value//common for value in safe_constant)
        u_coordinates = plus_coordinates(u)  # type: ignore[arg-type]
        v_coordinates = plus_coordinates(v)  # type: ignore[arg-type]

        ideal_matrix = plus_multiplication_matrix(u).row_join(  # type: ignore[arg-type]
            plus_multiplication_matrix(v)  # type: ignore[arg-type]
        )
        smith = smith_normal_form(ideal_matrix, domain=sp.ZZ)
        diagonal = [abs(int(smith[j, j])) for j in range(4)]
        norm = math.prod(diagonal)
        archived = records_by_d[d]
        if diagonal != archived["smith_diagonal_Lplus"]:
            raise AssertionError(f"independent Smith diagonal mismatch at d={d}")
        if norm != int(archived["content_ideal_norm_Lplus"]):
            raise AssertionError(f"independent ideal norm mismatch at d={d}")
        if len(str(safe_denominator//common)) != archived["q_min_digits"]:
            raise AssertionError(f"independent clearing mismatch at d={d}")
        selected_records.append(
            {
                "d": d,
                "q_min_digits": len(str(safe_denominator//common)),
                "u_coordinates_Lplus": list(u_coordinates),
                "v_coordinates_Lplus": list(v_coordinates),
                "smith_diagonal_Lplus": diagonal,
                "content_ideal_norm_Lplus": str(norm),
            }
        )

    return {
        "arithmetic_model": "Z[w]/(Phi_20), w=zeta_20",
        "integral_basis_trace_gram": [list(map(int, row)) for row in trace_gram.tolist()],
        "integral_basis_discriminant": basis_discriminant,
        "selected_exact_recomputations": selected_records,
    }


def edge_polynomials(d: int) -> tuple[list[Fraction], list[Fraction]]:
    a = [Fraction((-1) ** (d-j), math.factorial(j)) for j in range(d+1)]
    b: list[Fraction] = []
    for n in range(d+1):
        b.append(-sum((a[m] / (n-m) for m in range(n)), Fraction()))
    return a, b


def evaluate(poly: list[Fraction], z: mp.mpc) -> mp.mpc:
    value = mp.mpc(0)
    for coefficient in reversed(poly):
        value = value*z + mp.mpf(coefficient.numerator)/coefficient.denominator
    return value


def symbolic_isolation_check() -> dict:
    a, b = sp.symbols("a b", nonzero=True)
    A1, Ax, Ay, Bx, By, E1, ee, pp, Ly = sp.symbols(
        "A1 Ax Ay Bx By E1 e pi Ly"
    )
    ii = sp.I
    Lx = Ly + ii*pp*a/b
    rexp = A1*ee-E1
    rlogx = Ax*Lx-Bx
    rlogy = Ay*Ly-By
    expression = ii*a*Ax*Ay*rexp + b*A1*(Ay*rlogx-Ax*rlogy)
    expected = (
        ii*a*A1*Ax*Ay*(ee+pp)
        - ii*a*Ax*Ay*E1
        - b*A1*Ay*Bx
        + b*A1*Ax*By
    )
    residual = sp.expand(expression-expected)
    if residual != 0:
        raise AssertionError("paired isolation identity failed")
    return {"exact_symbolic_residual": str(residual)}


def cyclotomic_and_branch_checks(max_n: int) -> tuple[list[dict], dict]:
    z = sp.Symbol("z")
    exact_phi = {}
    records = []
    for n in range(5, max_n+1, 2):
        phi_minus_one = int(sp.cyclotomic_poly(n, z).subs(z, -1))
        if phi_minus_one != 1:
            raise AssertionError(f"Phi_{n}(-1) is not one")
        exact_phi[str(n)] = phi_minus_one

        representatives = [
            k for k in range(-(n//2), n//2+1)
            if k and math.gcd(k, n) == 1
        ]
        rho_product = mp.mpf(1)
        small: list[int] = []
        large: list[int] = []
        max_branch_residual = mp.mpf(0)
        xi = mp.e**(2j*mp.pi/n)
        for k in representatives:
            x = 1/(1+xi**k)
            y = 1-x
            rho = abs(x)
            rho_product *= rho
            if rho < 1:
                small.append(k)
            elif rho > 1:
                large.append(k)
            else:
                raise AssertionError("unexpected unit-circle equality")
            branch_residual = abs(mp.log(y)-mp.log(x)-2j*mp.pi*k/n)
            max_branch_residual = max(max_branch_residual, branch_residual)
            if abs(mp.re(x)-mp.mpf("0.5")) > mp.mpf("1e-80"):
                raise AssertionError("evaluation point has wrong real part")
        base = (1/(2*mp.cos(mp.pi/n)))**2
        for k in large:
            base *= (1/(2*mp.cos(mp.pi*k/n)))**2
        if not (base > 1):
            raise AssertionError("global exponential base is not greater than one")
        if abs(rho_product-1) > mp.mpf("1e-70"):
            raise AssertionError("unit product failed")
        records.append(
            {
                "n": n,
                "small_representatives": small,
                "large_representatives": large,
                "rho_product_minus_one": mp.nstr(rho_product-1, 8),
                "maximum_principal_branch_residual": mp.nstr(
                    max_branch_residual, 8
                ),
                "global_base_diagnostic": mp.nstr(base, 40),
                "predicted_d_power": -2*(1+len(large)),
            }
        )
    return records, exact_phi


def n5_edge_diagnostic(d: int) -> dict:
    n = 5
    xi = mp.e**(2j*mp.pi/n)
    a_poly, b_poly = edge_polynomials(d)
    a_one = evaluate(a_poly, mp.mpc(1))
    e_one = mp.mpf((-1)**d)
    ee = mp.e
    target = mp.e+mp.pi
    representatives = [1, 2, -2, -1]
    embedding_values: list[mp.mpf] = []
    phase_ratios: dict[str, str] = {}
    maximum_mismatch_residual = mp.mpf(0)
    for k in representatives:
        x = 1/(1+xi**k)
        y = 1-x
        ax = evaluate(a_poly, x)
        ay = evaluate(a_poly, y)
        bx = evaluate(b_poly, x)
        by = evaluate(b_poly, y)
        rlogx = ax*mp.log(1-x)-bx
        rlogy = ay*mp.log(1-y)-by
        d_pair = ay*rlogx-ax*rlogy
        rho = abs(x)
        theta = mp.pi*k/n
        phase = (d+2)*theta+mp.tan(theta)/2
        leading = (
            2j*mp.e**(-mp.mpf(3)/2)*rho**d*mp.sin(phase)/d
        )
        phase_ratios[str(k)] = mp.nstr(d_pair/leading, 40)
        rexp = a_one*ee-e_one
        for epsilon in (1, -1):
            algebraic = (
                2*epsilon*1j*a_one*ax*ay*target
                - 2*epsilon*1j*ax*ay*e_one
                - n*a_one*ay*bx
                + n*a_one*ax*by
            )
            tilde = 2*epsilon*1j*ax*ay*rexp+n*a_one*d_pair
            corrected = tilde+2j*(epsilon-k)*mp.pi*a_one*ax*ay
            maximum_mismatch_residual = max(
                maximum_mismatch_residual, abs(algebraic-corrected)
            )
            embedding_values.append(abs(algebraic))
    product = mp.fprod(embedding_values)
    golden = (1+mp.sqrt(5))/2
    scaled = product*d**6*golden**(-2*d)
    return {
        "d": d,
        "D_pair_over_phase_leading_by_k": phase_ratios,
        "maximum_exact_mismatch_residual": mp.nstr(
            maximum_mismatch_residual, 12
        ),
        "raw_eight_embedding_product": mp.nstr(product, 45),
        "product_times_d6_phi_minus_2d": mp.nstr(scaled, 45),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", type=Path,
        default=Path("sources/algebraic_unit_global_norm_rivoal.md")
    )
    parser.add_argument(
        "--candidate-script", type=Path,
        default=Path("scripts/algebraic_unit_two_log_rivoal_certificate.py")
    )
    parser.add_argument(
        "--candidate-result", type=Path,
        default=Path("results/algebraic_unit_two_log_rivoal_certificate.json")
    )
    parser.add_argument(
        "--content-script", type=Path,
        default=Path("scripts/algebraic_unit_two_log_n5_ideal_content.py")
    )
    parser.add_argument(
        "--content-result", type=Path,
        default=Path("results/algebraic_unit_two_log_n5_ideal_content_d200.json")
    )
    parser.add_argument(
        "--output", type=Path,
        default=Path("results/independent_algebraic_unit_two_log_audit.json")
    )
    args = parser.parse_args()
    mp.mp.dps = 120

    candidate = json.loads(args.candidate_result.read_text())
    actual_source_hash = sha256(args.source)
    actual_script_hash = sha256(args.candidate_script)
    if candidate["source_sha256"] != actual_source_hash:
        raise AssertionError("candidate result/source hash mismatch")
    if candidate["script_sha256"] != actual_script_hash:
        raise AssertionError("candidate result/script hash mismatch")

    candidate_content = json.loads(args.content_result.read_text())
    actual_content_script_hash = sha256(args.content_script)
    if candidate_content["source_sha256"] != actual_source_hash:
        raise AssertionError("content result/source hash mismatch")
    if candidate_content["script_sha256"] != actual_content_script_hash:
        raise AssertionError("content result/script hash mismatch")

    isolation = symbolic_isolation_check()
    branch_records, phi_checks = cyclotomic_and_branch_checks(31)

    phi = (1+sp.sqrt(5))/2
    base = sp.expand(phi**2)
    minimal_residual = sp.expand(base**2-3*base+1)
    if minimal_residual != 0:
        raise AssertionError("n=5 base polynomial failed")
    content_checks = independent_n5_content_checks(candidate_content)

    result = {
        "description": (
            "Independent exact/diagnostic audit of the paired-log algebraic-unit "
            "Rivoal family; asymptotic decimal records are not proofs."
        ),
        "audited_source_sha256": actual_source_hash,
        "audited_candidate_script_sha256": actual_script_hash,
        "audited_candidate_result_sha256": sha256(args.candidate_result),
        "audited_content_script_sha256": actual_content_script_hash,
        "audited_content_result_sha256": sha256(args.content_result),
        "independent_script_sha256": sha256(Path(__file__).resolve()),
        "symbolic_isolation": isolation,
        "odd_cyclotomic_exact_checks": phi_checks,
        "branch_and_embedding_set_checks": branch_records,
        "n5_exact_base": {
            "base": str(base),
            "minimal_polynomial_residual": str(minimal_residual),
            "eight_embedding_order": "phi^(2*d)*d^(-6)",
            "minimal_real_coefficient_field_order_after_common_i_unit": (
                "phi^d*d^(-3)"
            ),
        },
        "n5_high_precision_edge_diagnostics": [
            n5_edge_diagnostic(d) for d in (20, 40, 80)
        ],
        "n5_independent_exact_ideal_content_checks": content_checks,
        "scope_warning": (
            "The coefficient-field product does not control common algebraic "
            "coordinate content beyond the finite exact checks, or the blocks at "
            "other conjugates of a hypothetical algebraic e+pi."
        ),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")


if __name__ == "__main__":
    main()
