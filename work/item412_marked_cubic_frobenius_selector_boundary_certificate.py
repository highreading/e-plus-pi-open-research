#!/usr/bin/env python3
"""Deterministic certificate for Item 412.

The certificate checks the exact Frobenius marking identity in the
q == 1 (mod 6) mixed-cubic branch, the rational linear/quadratic split,
the complete finite-field branch decomposition on transparent exhaustive
normalization fields, and the two ordinary cubic-residue selector formulas.
Finite rows normalize identities only; the uniform proofs are in the report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STEM = "item412_marked_cubic_frobenius_selector_boundary"

DEPENDENCIES = {
    "sources/mixed_cubic_cube_smith_reduction.md":
        "b44cc15d1a846d5298d61b9e53539116b31bbab0338dbc6e320fb0a875b0d0a0",
    "sources/item390_mixed_cubic_fresh_primitive_saturation_report.md":
        "5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46",
    "sources/item396_fixed_gap_resultant_3adic_report.md":
        "7355b6909994357583f799e627e1ff19edb230a6a9002ee845be585057726aca",
    "sources/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_report.md":
        "245bf2e557dd81ac88c94e9d0adc8990f203e3ab40680d23bd50f8e435240c48",
    "sources/item406_mixed_cubic_actual_adjacent_recurrence_report.md":
        "a9c33967b42f5ae09c2c0c71de1b956ca240e49c367be46f3af2878cd96cbb83",
    "work/item411_mixed_primitive_boundary_transport_report.md":
        "1399357c4dbbf49ea685c356e34efde4fa5566fe31db14f7dd0ce252a3f35168",
    "work/item411_mixed_primitive_boundary_transport_certificate.json":
        "5f7c48924d650dc5b5078ef86eaef9a0ea5ce32b3de3268229218d50f7eb7407",
    "work/item411_mixed_primitive_boundary_transport_manifest.json":
        "0d1cdbc73a4b6d0570af6d00895250e76f4d1d3ba7a590aa0c0209b2450ee96d",
}

FROBENIUS_ROWS = (
    (7, 13),
    (7, 31),
    (7, 43),
    (13, 19),
    (13, 31),
    (19, 31),
    (25, 31),
    (25, 43),
    (37, 43),
    (37, 61),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_dependencies() -> dict[str, str]:
    observed: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        digest = sha256_bytes((ROOT / relative).read_bytes())
        assert digest == expected, (relative, expected, digest)
        observed[relative] = digest
    return observed


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def mu3(prime: int) -> list[int]:
    return [value for value in range(1, prime) if pow(value, 3, prime) == 1]


def clean_polynomial(poly: dict[tuple[int, ...], int]) -> dict[tuple[int, ...], int]:
    return {monomial: coefficient for monomial, coefficient in poly.items()
            if coefficient}


def poly_add(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
    scale: int = 1,
) -> dict[tuple[int, ...], int]:
    answer = dict(left)
    for monomial, coefficient in right.items():
        answer[monomial] = answer.get(monomial, 0) + scale * coefficient
    return clean_polynomial(answer)


def poly_mul(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], int]:
    answer: dict[tuple[int, ...], int] = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            answer[monomial] = answer.get(monomial, 0) + (
                left_coefficient * right_coefficient
            )
    return clean_polynomial(answer)


def poly_pow(poly: dict[tuple[int, ...], int], exponent: int) -> dict[tuple[int, ...], int]:
    variables = len(next(iter(poly)))
    answer = {(0,) * variables: 1}
    for _ in range(exponent):
        answer = poly_mul(answer, poly)
    return answer


def symbolic_factorization() -> dict[str, object]:
    # Variables are ordered (S, X, U).  XU denotes x*u.
    s_poly = {(1, 0, 0): 1}
    xu_poly = {(0, 1, 1): 1}
    linear = poly_add(s_poly, xu_poly, -1)
    quadratic = poly_add(
        poly_add(poly_pow(s_poly, 2), poly_mul(s_poly, xu_poly)),
        poly_pow(xu_poly, 2),
    )
    product = poly_mul(linear, quadratic)
    expected = poly_add(poly_pow(s_poly, 3), poly_pow(xu_poly, 3), -1)
    assert product == expected
    return {
        "identity": "(S-XU)*(S^2+S*XU+(XU)^2)=S^3-(XU)^3",
        "expanded_sparse_coefficients": [
            {"exponents_S_X_U": list(monomial), "coefficient": coefficient}
            for monomial, coefficient in sorted(product.items())
        ],
        "applies_to_both_V0_and_V1": True,
    }


def frobenius_mark_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for q_value, prime in FROBENIUS_ROWS:
        assert q_value % 6 == 1 and prime > q_value and is_prime(prime)
        assert (prime - q_value) % 6 == 0
        m_value = (prime - q_value) // 6
        n_value = q_value - 1
        t_value = (prime - 1) // 3
        e_value = 2 * m_value + q_value - 1
        assert e_value == t_value + 2 * n_value // 3

        x_integer = pow(4, n_value // 3)
        k_integer = pow(4, n_value)
        assert pow(x_integer, 3) == k_integer
        x_mod = x_integer % prime
        cubic_character_two = pow(2, t_value, prime)
        selected_root = pow(2, e_value, prime)
        assert pow(cubic_character_two, 3, prime) == 1
        assert selected_root == x_mod * cubic_character_two % prime
        assert pow(selected_root, 3, prime) == k_integer % prime

        linear_value = (selected_root - x_mod) % prime
        quadratic_value = (
            selected_root * selected_root
            + x_mod * selected_root
            + x_mod * x_mod
        ) % prime
        assert (linear_value == 0) != (quadratic_value == 0)

        rows.append({
            "q": q_value,
            "p": prime,
            "m": m_value,
            "n": n_value,
            "t=(p-1)/3": t_value,
            "E": e_value,
            "x=4^(n/3)_mod_p": x_mod,
            "chi_p(2)=2^t_mod_p": cubic_character_two,
            "X_p=2^E_mod_p": selected_root,
            "selected_rational_stratum": (
                "linear" if cubic_character_two == 1 else "quadratic"
            ),
            "X_equals_x_times_chi": True,
        })
    return rows


def exhaustive_branch_decomposition() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for prime in (7, 13):
        q_value = 7
        n_value = q_value - 1
        x_value = pow(4, n_value // 3, prime)
        k_value = pow(x_value, 3, prime)
        roots = mu3(prime)
        assert len(roots) == 3
        omega = next(root for root in roots if root != 1)
        checked = 0
        unmarked_count = 0
        branch_counts = {str(root): 0 for root in roots}
        stream: list[str] = []
        for u_value in range(prime):
            for v_value in range(prime):
                second_a = (u_value + v_value) % prime
                for r_value in range(prime):
                    for s_value in range(prime):
                        determinant = (
                            u_value * r_value - s_value * second_a
                        ) % prime
                        v_zero = (
                            pow(s_value, 3, prime)
                            - k_value * pow(u_value, 3, prime)
                        ) % prime
                        v_one = (
                            pow(r_value, 3, prime)
                            - k_value * pow(second_a, 3, prime)
                        ) % prime
                        unmarked = determinant == v_zero == v_one == 0
                        branches = [
                            root for root in roots
                            if s_value == root * x_value * u_value % prime
                            and r_value == root * x_value * second_a % prime
                        ]
                        assert unmarked == bool(branches)
                        if unmarked:
                            unmarked_count += 1
                            for root in branches:
                                branch_counts[str(root)] += 1

                        twisted_s = omega * s_value % prime
                        twisted_r = omega * r_value % prime
                        twisted_determinant = (
                            u_value * twisted_r - twisted_s * second_a
                        ) % prime
                        twisted_v_zero = (
                            pow(twisted_s, 3, prime)
                            - k_value * pow(u_value, 3, prime)
                        ) % prime
                        twisted_v_one = (
                            pow(twisted_r, 3, prime)
                            - k_value * pow(second_a, 3, prime)
                        ) % prime
                        assert twisted_determinant == omega * determinant % prime
                        assert twisted_v_zero == v_zero
                        assert twisted_v_one == v_one
                        twisted_branches = [
                            root for root in roots
                            if twisted_s == root * x_value * u_value % prime
                            and twisted_r == root * x_value * second_a % prime
                        ]
                        assert sorted(twisted_branches) == sorted(
                            omega * root % prime for root in branches
                        )
                        checked += 1
                        if unmarked:
                            stream.append(
                                f"{u_value}:{v_value}:{r_value}:{s_value}:"
                                + ",".join(map(str, branches))
                            )
        rows.append({
            "p": prime,
            "q_normalization": q_value,
            "x": x_value,
            "mu3": roots,
            "tuples_exhaustively_checked": checked,
            "unmarked_tuples": unmarked_count,
            "branch_incidence_counts_including_origin_overlap": branch_counts,
            "cyclic_branch_action_verified_exhaustively": True,
            "normalization_only_not_uniform_proof": True,
            "unmarked_stream_sha256": sha256_bytes("\n".join(stream).encode("ascii")),
        })
    return rows


def cubic_residue_selector_rows() -> dict[str, object]:
    primes = [
        value for value in range(7, 250)
        if value % 3 == 1 and is_prime(value)
    ]
    class_counts = {"1": 0, "7": 0, "13": 0}
    checks = 0
    exceptional_kernel_checks = 0
    stream: list[str] = []
    for prime in primes:
        residue = str(prime % 18)
        assert residue in class_counts
        class_counts[residue] += 1
        t_value = (prime - 1) // 3
        chi_two = pow(2, t_value, prime)
        roots = mu3(prime)
        assert len(roots) == 3 and chi_two in roots
        for zeta in roots:
            selected = zeta == chi_two
            if prime % 18 == 7:
                exponent = 2
                test_value = 2 * pow(pow(zeta, exponent, prime), -1, prime) % prime
                cubic_residue = pow(test_value, t_value, prime) == 1
                assert cubic_residue == selected
                formula = "2*zeta^(-2) is a cube"
            elif prime % 18 == 13:
                exponent = 1
                test_value = 2 * pow(zeta, -1, prime) % prime
                cubic_residue = pow(test_value, t_value, prime) == 1
                assert cubic_residue == selected
                formula = "2*zeta^(-1) is a cube"
            else:
                assert prime % 18 == 1 and t_value % 3 == 0
                assert pow(zeta, t_value, prime) == 1
                for exponent in range(3):
                    assert (
                        pow(2 * pow(zeta, -exponent, prime), t_value, prime)
                        == chi_two
                    )
                    exceptional_kernel_checks += 1
                formula = "direct zeta=chi_p(2); multiplying by mu3 cannot change chi"
            checks += 1
            stream.append(f"{prime}:{zeta}:{chi_two}:{selected}:{formula}")
    return {
        "primes_used_for_normalization": primes,
        "prime_class_counts": class_counts,
        "zeta_cases_checked": checks,
        "p_equals_1_mod_18_kernel_checks": exceptional_kernel_checks,
        "formulas": {
            "p_mod_18_7": "marked iff 2*zeta^(-2) is a cubic residue",
            "p_mod_18_13": "marked iff 2*zeta^(-1) is a cubic residue",
            "p_mod_18_1": "ordinary cubic character kills mu3; retain direct Frobenius equality",
        },
        "normalization_only_not_density_evidence": True,
        "selector_stream_sha256": sha256_bytes("\n".join(stream).encode("ascii")),
    }


def fixed_rational_branch_witness() -> dict[str, object]:
    q_value = 7
    witnesses = []
    for prime in (13, 31):
        m_value = (prime - q_value) // 6
        n_value = q_value - 1
        t_value = (prime - 1) // 3
        x_value = pow(4, n_value // 3, prime)
        chi_two = pow(2, t_value, prime)
        selected_root = pow(2, 2 * m_value + q_value - 1, prime)
        linear = selected_root == x_value
        quadratic = (
            selected_root * selected_root
            + x_value * selected_root
            + x_value * x_value
        ) % prime == 0
        assert linear != quadratic
        witnesses.append({
            "q": q_value,
            "p": prime,
            "m": m_value,
            "chi_p(2)": chi_two,
            "x": x_value,
            "selected_root": selected_root,
            "rational_factor_containing_selected_root": (
                "Z-x" if linear else "Z^2+xZ+x^2"
            ),
        })
    assert witnesses[0]["rational_factor_containing_selected_root"] != (
        witnesses[1]["rational_factor_containing_selected_root"]
    )
    return {
        "same_q_compatible_prime_witnesses": witnesses,
        "conclusion": (
            "No one proper q-only rational factor of Z^3-x^3 contains "
            "the distinguished root for every compatible prime."
        ),
        "does_not_assert_actual_unmarked_support_at_either_prime": True,
    }


def build_certificate() -> dict[str, object]:
    dependencies = verify_dependencies()
    factorization = symbolic_factorization()
    frobenius = frobenius_mark_rows()
    decomposition = exhaustive_branch_decomposition()
    residue_selector = cubic_residue_selector_rows()
    rational_no_go = fixed_rational_branch_witness()
    witness_payload = json.dumps(
        {
            "factorization": factorization,
            "frobenius": frobenius,
            "decomposition": decomposition,
            "residue_selector": residue_selector,
            "rational_no_go": rational_no_go,
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("ascii")
    return {
        "schema": "item412-marked-cubic-frobenius-selector-boundary-v1",
        "item": 412,
        "status": "WORK_ONLY_UNAUDITED_NO_CENTRAL_EDIT_NO_BOOKING",
        "dependency_sha256": dependencies,
        "exact_linear_quadratic_factorization": factorization,
        "frobenius_mark_normalization_rows": frobenius,
        "exhaustive_unmarked_branch_normalizations": decomposition,
        "ordinary_cubic_residue_selector": residue_selector,
        "fixed_rational_branch_no_go": rational_no_go,
        "theorems": {
            "actual_frobenius_mark": (
                "For q=1 mod 6, x=4^((q-1)/3) and "
                "X_p=x*2^((p-1)/3) mod p."
            ),
            "eisenstein_diagonal_incidence": (
                "The actual collision is the branch ideal whose mu3 label "
                "equals the cubic Frobenius value of 2; the Smith carrier is "
                "the unmarked union of all three branch ideals."
            ),
            "symmetric_information_no_go": (
                "The unmarked ideal is stable under cyclic branch rotation, "
                "so Smith data and other mu3-symmetric invariants cannot select "
                "the marked branch without nonsymmetric p-local input."
            ),
            "rational_fixed_branch_no_go": (
                "Already at q=7 the selected root lies in the quadratic factor "
                "for p=13 and the linear factor for p=31."
            ),
        },
        "capacity": {
            "strictly_large_component_ceiling_unchanged":
                "log(136)/6 = 0.8187758142893420014168718304...",
            "frozen_booked_deficit_unchanged":
                "1.0196329836694317938803064012...",
            "proved_total_capacity_ceiling_delta": 0,
            "booking_delta": 0,
            "fixed_branch_exclusion_ceiling_delta_without_weighted_distribution": 0,
            "reason": (
                "Nonnegative carrier-weighted mass may concentrate entirely in "
                "uncontrolled Frobenius bins; ambient prime density is not a "
                "carrier-weighted distribution theorem."
            ),
        },
        "labels": {
            "PROVED": [
                "exact all-parameter Frobenius mark identity in q=1 mod 6",
                "exact marked Eisenstein branch incidence and rational linear/quadratic split",
                "ordinary cubic-residue selector in p=7,13 mod 18",
                "mu3-symmetric invariant no-go and fixed rational branch no-go",
                "zero booking and zero proved capacity reduction",
            ],
            "OPEN": [
                "nonoccurrence of the marked branch in the actual coefficient family",
                "carrier-weighted distribution across Frobenius-marked branch ideals",
                "a p=1 mod 18 selector beyond the direct Frobenius equality",
                "valuation-weighted o(m) control of strictly large common content",
                "Route 1 and irrationality of e+pi",
            ],
            "NOT_CLAIMED": [
                "an actual wrong-root support prime",
                "Chebotarev equidistribution for divisors of moving carriers",
                "radical control of all p-adic valuation depth",
                "any positive divisor or capacity booking",
            ],
        },
        "witness_sha256": sha256_bytes(witness_payload),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / f"{STEM}_certificate.json",
    )
    parser.add_argument(
        "--replay",
        type=Path,
        help="Optional certificate whose bytes must equal the generated payload.",
    )
    args = parser.parse_args()
    certificate = build_certificate()
    payload = (json.dumps(certificate, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if args.replay is not None:
        assert args.replay.read_bytes() == payload
    args.output.write_bytes(payload)


if __name__ == "__main__":
    main()
