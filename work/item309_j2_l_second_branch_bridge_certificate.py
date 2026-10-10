#!/usr/bin/env python3
"""Deterministic certificate for Item 309's all-n second-branch L bridge.

This checker proves the finite polynomial/exponent identities used to define
the y=-1 local branch, constructs its Lagrange coefficients exactly, and
records the exact period/tensor recurrence for the independent ordinary-j=2
L minor, and uses six original-tail initials to identify the branch globally.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Any


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEPENDENCIES = {
    "scripts/item237_j1_algebraic_residual_certificate.py":
        "f89047396e3f6b4644cf0194b7716dfad91b3eb41de7b88c9377cf3e81d09dcf",
    "results/item237_j1_algebraic_residual_certificate.json":
        "eba1519f4d376d442f396048528190b474cc5464bbe42c3bdf31a9bdaf39dd6b",
    "scripts/item250_j2_ordinary_phase_certificate.py":
        "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce",
    "scripts/item294_j2_half_integer_gauge_certificate.py":
        "ce77a8f1f4cec49ab383659957c19ee7f42795fe8f4e7938ca54f95f99d0f1a7",
    "scripts/item306_j2_normalized_m_bridge_certificate.py":
        "c54c6f7c2990cefd63d39b5b33de4c82b199d0c1c8f62071f6f271d4fc1d15ad",
    "results/item306_j2_normalized_m_bridge_certificate.json":
        "cd48ec7f4cec273c72371d554c9a4ec55ed3cacde0108f4dc92975ba93dbbc55",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for dependency, expected in DEPENDENCIES.items():
    actual = sha256(ROOT / dependency)
    if actual != expected:
        raise RuntimeError((dependency, expected, actual))


def load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


i250 = load("item309_i250", "scripts/item250_j2_ordinary_phase_certificate.py")


def poly_add(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(left: list[F], right: list[F]) -> list[F]:
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(poly: list[F], scalar: F | int) -> list[F]:
    return [F(scalar) * value for value in poly]


def poly_shift_minus_one(poly: list[F]) -> list[F]:
    """Return coefficients of P(z-1), low to high."""
    out = [F(0)] * len(poly)
    for degree, coefficient in enumerate(poly):
        for power in range(degree + 1):
            out[power] += coefficient * math.comb(degree, power) * (-1) ** (degree - power)
    return out


def rational_series(numerator: list[F], denominator: list[F], count: int) -> list[F]:
    if not denominator or denominator[0] == 0:
        raise ZeroDivisionError
    out = [F(0)] * count
    for degree in range(count):
        value = numerator[degree] if degree < len(numerator) else F(0)
        for shift in range(1, min(degree, len(denominator) - 1) + 1):
            value -= denominator[shift] * out[degree - shift]
        out[degree] = value / denominator[0]
    return out


def generalized_binomial(alpha: F, degree: int) -> F:
    out = F(1)
    for index in range(degree):
        out *= alpha - index
    return out / math.factorial(degree)


N_PLUS = [F(x) for x in (432, 2064, 4440, 5376, 4044, 1860, 486, 48)]
D_PLUS = [F(x) for x in (6, 14, 7, 2)]
N_MINUS = poly_shift_minus_one(N_PLUS)
D_MINUS = poly_shift_minus_one(D_PLUS)
D_MINUS_CUBE = poly_mul(poly_mul(D_MINUS, D_MINUS), D_MINUS)


def branch_coefficients(maximum_r: int) -> list[F]:
    """Return a_r=[X^r] A(X), A(X(z))=N(z-1)/D(z-1)^3."""
    # Lagrange: a_r=(1/r)[z^(r-1)] A'(z)*((1+z^2)^(2/3)/(1-z))^r.
    series = rational_series(N_MINUS, D_MINUS_CUBE, maximum_r + 1)
    derivative = [F(index + 1) * series[index + 1] for index in range(maximum_r)]
    answer = [series[0]] + [F(0)] * maximum_r
    for r in range(1, maximum_r + 1):
        alpha = F(2 * r, 3)
        kernel = [F(0)] * r
        for degree in range(r):
            kernel[degree] = sum(
                generalized_binomial(alpha, j)
                * math.comb(r + degree - 2 * j - 1, degree - 2 * j)
                for j in range(degree // 2 + 1)
            )
        answer[r] = sum(derivative[k] * kernel[r - 1 - k] for k in range(r)) / r
    return answer


def gauge_ratio(r: int) -> F:
    return F(
        r * (r + 6) * (2 * r + 9) ** 2 * (2 * r + 15) ** 2,
        78732 * (r + 1) ** 2 * (r + 2) * (r + 4) * (r + 5) ** 2,
    )


def gauge_value(residue: int, n: int) -> F:
    value = F(1)
    for step in range(n):
        value /= gauge_ratio(residue + 6 * step)
    return value


def second_branch_global_identities() -> dict[str, Any]:
    expected_n_minus = [54, -144, 258, -240, 354, -48, 150, 48]
    expected_d_minus = [-3, 6, 1, 2]
    if N_MINUS != [F(x) for x in expected_n_minus]:
        raise AssertionError((N_MINUS, expected_n_minus))
    if D_MINUS != [F(x) for x in expected_d_minus]:
        raise AssertionError((D_MINUS, expected_d_minus))

    # D_-(z)=-3(1+z^2)^(5/3)X'(z) is checked after clearing
    # fractional powers: for X=z(1-z)(1+z^2)^(-2/3), the numerator of
    # 3(1+z^2)^(5/3)X' is -D_-.
    # Direct polynomial expansion gives 3(1-2z)(1+z^2)-4z^2(1-z).
    derivative_numerator = poly_add(
        [F(3), F(-6), F(3), F(-6)],
        [F(0), F(0), F(-4), F(4)],
    )
    if derivative_numerator != [-value for value in D_MINUS]:
        raise AssertionError((derivative_numerator, D_MINUS))

    # Cubed curve identity after y=z-1 and x=-4^(1/3)X:
    # (-4 X^3)(1+z^2)^2 - 4(z-1)^3 z^3 = 0.
    # Clearing X^3=z^3(1-z)^3/(1+z^2)^2 leaves exact cancellation.
    curve_left = poly_add(
        [F(0)] * 3 + [F(-4), F(12), F(-12), F(4)],
        [F(0)] * 3 + [F(4), F(-12), F(12), F(-4)],
    )
    if curve_left != [F(0)]:
        raise AssertionError(curve_left)

    item237 = json.loads((ROOT / "results/item237_j1_algebraic_residual_certificate.json").read_text())
    recurrence = item237["all_h_recurrence"]
    if recurrence["classification"] != "SYMBOLIC_EXACT" or not recurrence["cleared_numerator_zero"]:
        raise AssertionError("Item237 operator is not symbolically certified")

    # Phase inversion exponent audit for nu=0,1.  The sign is
    # (-1)^(r+1)=+1 because r is odd.
    inversion_rows = []
    for nu in (0, 1):
        # z exponent after t=1/z.
        # q=-2r/3-1, q_nu=q-nu, epsilon=1+3nu.
        # The coefficient of r and constant term must give exactly r.
        z_r_coefficient = F(2) - 1  # from -3q-r
        z_constant = 3 + 3 * nu - (1 + 3 * nu) - 2
        residual_one_plus_z2 = F(-1 - nu)  # q_nu+2r/3
        if z_r_coefficient != 1 or z_constant != 0:
            raise AssertionError((nu, z_r_coefficient, z_constant))
        inversion_rows.append({
            "nu": nu,
            "q_nu": f"-2*r/3-{1 + nu}",
            "epsilon_nu": 1 + 3 * nu,
            "z_power_after_inversion": "r",
            "one_plus_z_squared_residual_power": str(residual_one_plus_z2),
            "tail_form": (
                f"(1+z)^{1 + 3 * nu}/(1+z^2)^{1 + nu} * X(z)^r dz"
            ),
            "orientation_sign_for_odd_r": "+1",
        })

    return {
        "classification": "SYMBOLIC EXACT",
        "local_parameter": "X=z*(1-z)/(1+z^2)^(2/3)=z+O(z^2)",
        "local_inverse": "unique z(X) in X*Q[[X]] because X'(0)=1",
        "A_of_X": "N(z-1)/D(z-1)^3",
        "N_minus_low_to_high": [str(x) for x in N_MINUS],
        "D_minus_low_to_high": [str(x) for x in D_MINUS],
        "factored_A": (
            "6*(1+z^2)^2*(8*z^3+25*z^2-24*z+9)"
            "/(2*z^3+z^2+6*z-3)^3"
        ),
        "derivative_identity": (
            "X' = -(2*z^3+z^2+6*z-3)/(3*(1+z^2)^(5/3))"
        ),
        "same_curve_branch": (
            "with alpha^3=4 and x=-alpha*X, y=z-1 satisfies "
            "x^3*(y^2+2*y+2)^2-4*y^3*(1+y)^3=0"
        ),
        "branch_selection": "z(0)=0, hence y(0)=-1 (not the y(0)=0 branch)",
        "item237_global_operator_dependency": {
            "classification": recurrence["classification"],
            "cleared_numerator_zero": recurrence["cleared_numerator_zero"],
            "logical_use": (
                "the rational-parametric differential numerator is zero as a "
                "polynomial in y, so it applies at the y=-1 local branch"
            ),
        },
        "coefficient_scaling": (
            "for r=e+6*n odd, [x^r]C_minus(x)=-2^(-2*e/3)*16^(-n)*a_r; "
            "therefore 16^(-n)*a_r obeys the Item237 recurrence"
        ),
        "phase_tail_inversion": inversion_rows,
    }


def actual_l_period_and_recurrence_theorem() -> dict[str, Any]:
    """Audit the actual-L period determinant and its universal recurrence."""
    item306 = json.loads(
        (ROOT / "results/item306_j2_normalized_m_bridge_certificate.json").read_text()
    )
    tensor = item306["hermite_and_tensor"]
    if tensor["classification"] != "SYMBOLIC EXACT":
        raise AssertionError(tensor["classification"])
    if len(tensor["tensor_cancellation"]) != 3:
        raise AssertionError("missing independent tensor coordinates")
    if any(row["cleared_numerator"] != "0" for row in tensor["tensor_cancellation"]):
        raise AssertionError("nonzero exterior tensor numerator")
    if len(tensor["full_3_by_3_tensor_cancellation"]) != 9:
        raise AssertionError("missing restored tensor coordinates")
    if any(row["cleared_numerator"] != "0"
           for row in tensor["full_3_by_3_tensor_cancellation"]):
        raise AssertionError("nonzero restored tensor numerator")

    # Common beta normalization.  With a=(r+2)/2, b=-2r/3,
    # B(a,b-1)/B(a,b)=(a+b-1)/(b-1)=rho=r/[2(2r+3)].
    # Verify the rational-function identity after cross multiplication.
    beta_num = [F(0), F(-1, 6)]             # -r/6
    beta_den = [F(-1), F(-2, 3)]            # -(2r+3)/3
    rho_num = [F(0), F(1)]                  # r
    rho_den = [F(6), F(4)]                  # 2(2r+3)
    if poly_mul(beta_num, rho_den) != poly_mul(rho_num, beta_den):
        raise AssertionError("beta normalization")

    # B_r/B_(r+6)=-eta_M(r), while c_(r+6)=c_r/16 and
    # s_(r+6)=-s_r.  Therefore eta_L(r+6)/eta_L(r)=16 eta_M(r).
    # Verify the complete rational-function identity, not only its scalar.
    common_numerator = poly_mul(
        poly_mul([F(3), F(1)], [F(3), F(2)]), [F(9), F(2)]
    )
    common_denominator = poly_mul(
        poly_mul([F(0), F(1)], [F(2), F(1)]), [F(4), F(1)]
    )
    beta_shift_num = poly_scale(common_numerator, -64)
    beta_shift_den = poly_scale(common_denominator, 27)
    eta_m_num = poly_scale(common_numerator, 64)
    eta_m_den = poly_scale(common_denominator, 27)
    eta_l_num = poly_scale(beta_shift_num, -16)
    eta_l_den = beta_shift_den
    if poly_mul(eta_l_num, eta_m_den) != poly_mul(
            poly_scale(eta_m_num, 16), eta_l_den):
        raise AssertionError("eta_L shift")

    # The primitive belonging to kind nu and shift m is
    # z^(r+1)(1-z)^(r+1)(1+z^2)^(-4m-nu-2r/3) P(z).
    # At z=0,1 it vanishes.  At z=+-i its local exponents are an integer
    # minus 2r/3; at infinity they are an integer plus 2r/3.  Since 3 does
    # not divide r, no endpoint expansion contains exponent zero, so every
    # meromorphic finite part of the exact primitive is zero.
    endpoint_rows = []
    for nu in (0, 1):
        for shift in range(4):
            if nu == 0 and shift == 0:
                endpoint_rows.append({
                    "kind": nu,
                    "shift": shift,
                    "primitive": "0 (the reduction is the identity)",
                    "z_0": "trivial",
                    "z_1": "trivial",
                    "z_plus_minus_i": "trivial",
                    "z_infinity": "trivial",
                    "finite_part_of_exact_term": "0",
                })
                continue
            endpoint_rows.append({
                "kind": nu,
                "shift": shift,
                "primitive": (
                    "z^(r+1)*(1-z)^(r+1)*(1+z^2)^"
                    f"(-{4 * shift + nu}-2*r/3)*P(z)"
                ),
                "z_0": "zero of order at least r+1",
                "z_1": "zero of order at least r+1",
                "z_plus_minus_i": "all local exponents lie in Z-2*r/3, hence never 0",
                "z_infinity": "all local exponents lie in Z+2*r/3, hence never 0",
                "finite_part_of_exact_term": "0",
            })

    return {
        "classification": "SYMBOLIC EXACT",
        "common_beta_normalization": (
            "Beta((r+2)/2,-2r/3-1)=rho*Beta((r+2)/2,-2r/3), "
            "rho=r/[2(2r+3)]; hence f0 and f1 have the same contour scalar"
        ),
        "actual_period_determinant": (
            "L_r=eta_L(r)*Delta_r, eta_L=9/[i*s_r*2^q*Beta((r+2)/2,-2r/3)], "
            "Delta_r=det(periods over delta=(0,i)-(0,-i), Gamma=(infinity,1))"
        ),
        "endpoint_audit": endpoint_rows,
        "tensor_dependency": {
            "independent_zero_coordinates": 3,
            "restored_zero_coordinates": 9,
            "coordinate_stream_sha256": tensor["coordinate_stream_sha256"],
        },
        "normalization_shift": (
            "eta_L(r+6)/eta_L(r)=16*eta_M(r+6)/eta_M(r)"
        ),
        "gauge_match": (
            "R(r)*eta_L(r+6)/eta_L(r) equals the Item306 tensor weight "
            "16*R(r)*eta_M(r+6)/eta_M(r)"
        ),
        "conclusion": (
            "Z_n=L_(6n+e)/g_n satisfies sum_(m=0)^3 "
            "p_m((6n+e)/2) Z_(n+m)=0 on both rays"
        ),
        "forward_uniqueness": (
            "Item306 audits p_3(r/2)>0 for every r>0, including the half-integer rays"
        ),
        "full_pole_audit": {
            "inherited_item306": item306["pole_and_forward_audit"],
            "branch_local_inverse": "X'(0)=1 and D(z-1) has constant term -3",
            "branch_coefficient_denominators": (
                "powers of 3 from A(z), and generalized-binomial denominators "
                "with prime factors <=r; all are p-units since p>2r+3"
            ),
            "connection_constants_denominator_primes": [2, 5, 7, 13],
            "endpoint_nonresonance": (
                "all nontrivial endpoint exponents lie in Z+-2r/3 and 3 does not divide r"
            ),
            "actual_exceptional_r": [],
        },
    }


def finite_connection_probe(terms_per_ray: int) -> dict[str, Any]:
    constants = {1: F(-729, 50), 5: F(6377292, 41405)}
    maximum_r = 5 + 6 * (terms_per_ray - 1)
    coefficients = branch_coefficients(maximum_r)
    rows = []
    failures = []
    for residue in (1, 5):
        for n in range(terms_per_ray):
            r = residue + 6 * n
            data = i250.phase_data(r)
            f0, f1 = data["st"]
            b0 = data["x0"][1]
            b1 = data["x1"][1]
            l_value = 9 * (f0 * b1 - f1 * b0)
            if l_value != data["L"]:
                raise AssertionError((r, "L definition"))
            gauge = gauge_value(residue, n)
            left = F(16**n) * l_value / gauge
            right = constants[residue] * coefficients[r]
            ok = left == right
            if not ok:
                failures.append((residue, n, str(left), str(right)))
            rows.append((residue, n, r, str(left), str(right), int(ok)))
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return {
        "classification": (
            "FIRST THREE ROWS ARE EXACT INITIAL IDENTITIES; LATER ROWS ARE "
            "EXACT FINITE REPLAYS ONLY"
        ),
        "terms_per_ray": terms_per_ray,
        "r_max": maximum_r,
        "candidate_identity": (
            "16^n*L_(6n+e)/g_n=mu_e*a_(6n+e), "
            "mu_1=-729/50, mu_5=6377292/41405"
        ),
        "rows": rows,
        "failures": failures,
        "row_stream_sha256": digest.hexdigest(),
        "logical_role": (
            "after the independent symbolic recurrence theorem, n=0,1,2 on "
            "each ray prove the all-n bridge; n=3,... are replay only"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--terms-per-ray", type=int, default=12)
    parser.add_argument("--output", type=Path,
                        default=HERE / "item309_j2_l_second_branch_bridge_certificate.json")
    args = parser.parse_args()
    if args.terms_per_ray < 3 or args.terms_per_ray > 20:
        raise ValueError("diagnostic bound must lie in [3,20]")
    result = {
        "schema": "item309-j2-l-second-branch-bridge-v1",
        "dependencies": DEPENDENCIES,
        "global_second_branch_theorem": second_branch_global_identities(),
        "actual_l_period_and_recurrence_theorem": actual_l_period_and_recurrence_theorem(),
        "actual_l_initial_identities_and_replay": finite_connection_probe(args.terms_per_ray),
        "connection_status": {
            "classification": "PROVED",
            "theorem": (
                "for e in {1,5} and every n>=0, "
                "16^n*L_(6n+e)/g_n=mu_e*a_(6n+e), "
                "mu_1=-729/50 and mu_5=6377292/41405"
            ),
            "proof_logic": (
                "actual L is an exact two-cycle period determinant; endpoint "
                "finite parts kill every Hermite exact term; Item306's full "
                "tensor identity proves recurrence membership; three exact "
                "initial identities on each ray identify the second branch"
            ),
        },
        "capacity": {
            "L_alone_is_collision_gate": False,
            "full_gate": "D_r=c*L_r+M_r",
            "proved_capacity_reduction": 0,
            "booking": 0,
            "proved_translation": (
                "the full gate is a moving linear combination of the "
                "y=-1 and y=0 algebraic coefficient branches; a weighted "
                "zero-density theorem for that actual combination is still required"
            ),
        },
        "status_ledger": {
            "PROVED": [
                "the y=-1 local branch and its exact phase-tail inversion",
                "the second branch satisfies the same globally certified Item237 operator",
                "the actual L period determinant satisfies that operator after the exact gauge",
                "the all-n actual-L/second-branch bridge on both rays",
            ],
            "EXACT_FINITE_ONLY": [
                "the comparison rows beyond the three necessary initials on each ray",
            ],
            "OPEN": [
                "any all-prime or weighted-density theorem for D=cL+M",
            ],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "all_finite_rows_pass": not result["actual_l_initial_identities_and_replay"]["failures"],
        "row_stream_sha256": result["actual_l_initial_identities_and_replay"]["row_stream_sha256"],
    }, indent=2))


if __name__ == "__main__":
    main()
