#!/usr/bin/env python3
"""Deterministic exact certificate for Item 228.

This checker continues Item 223's j=1 Pearson transfer through the next
Frobenius pole.  It verifies the regularized forcing, the exact 3p source,
the finite support of the first free mode, the resulting second necessary
invariant, and a declared finite survivor census.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterator


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item228_j1_second_frobenius_certificate.json"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM223_PATH = resolve("item223_j1_frobenius_transfer_certificate.py")
ITEM218_PATH = resolve("item218_j1_common_log_certificate.py")
item223 = load("item228_item223", ITEM223_PATH)
item218 = item223.item218


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def actual_rows(prime_max: int) -> Iterator[tuple[int, int, int, int]]:
    """Yield (p,h,r,s) for every actual j=1 row through prime_max."""
    for prime in item218.primes_upto(prime_max):
        if prime < 13:
            continue
        for s_value in range(1, (prime - 7) // 6 + 1):
            numerator = prime - 6 * s_value - 3
            if numerator % 4:
                continue
            h_value = numerator // 4
            if h_value >= 1:
                yield prime, h_value, 2 * h_value, s_value


def weight_polynomials(r_value: int, s_value: int) -> tuple[list[int], list[int]]:
    weight = item223.convolution(
        item223.polynomial_power([1, -1], r_value),
        item223.polynomial_power([1, 0, 1], 2 * s_value - 1),
    )
    sigma_weight = item223.convolution([1, -1, 1, -1], weight)
    return weight, sigma_weight


def epsilon_for(prime: int) -> int:
    return 1 if ((prime - 1) // 2) % 2 == 0 else -1


def coefficient(poly: list[int], degree: int) -> int:
    return poly[degree] if 0 <= degree < len(poly) else 0


def recurrence_coefficients(
    prime: int, r_value: int, s_value: int, t_value: int
) -> tuple[int, int, int, int]:
    """Exact (B,-C,D,-A) coefficients in B*u_t-C*u_(t+1)+D*u_(t+2)-A*u_(t+3)."""
    return (
        prime + r_value + t_value + 1,
        -(prime + 2 * r_value + t_value + 2),
        prime + r_value + 4 * s_value + t_value + 1,
        -(prime + 2 * r_value + 4 * s_value + t_value + 2),
    )


def regularized_rhs(
    prime: int,
    r_value: int,
    t_value: int,
    epsilon: int,
    sigma_weight: list[int],
) -> int:
    """The omitted-derivative forcing, reduced modulo p.

    If K_t=z^(p+r+t+1)*sigma*W, then the value is
    -sum_[a>=1] [z^(ap)]K_t * ell_(ap-1).
    """
    base_degree = prime + r_value + t_value + 1
    minimum_multiple = max(1, (base_degree + prime - 1) // prime)
    maximum_multiple = (base_degree + len(sigma_weight) - 1) // prime
    total = 0
    for multiple in range(minimum_multiple, maximum_multiple + 1):
        local_degree = multiple * prime - base_degree
        total -= coefficient(sigma_weight, local_degree) * item223.ell_numerator(
            multiple * prime - 1, epsilon
        )
    return total % prime


def boundary_moment_from_weight(
    prime: int,
    r_value: int,
    epsilon: int,
    shift: int,
    weight: list[int],
) -> Fraction:
    base_exponent = prime + r_value + shift
    return sum(
        Fraction(
            value * item223.ell_numerator(base_exponent + degree, epsilon),
            base_exponent + degree + 1,
        )
        for degree, value in enumerate(weight)
    )


Vector = tuple[int, int, int]  # fixed forcing, initial lambda, first-pole freedom


def vector_add(left: Vector, right: Vector, prime: int) -> Vector:
    return tuple((left[index] + right[index]) % prime for index in range(3))  # type: ignore[return-value]


def vector_scale(value: Vector, scalar: int, prime: int) -> Vector:
    return tuple((scalar * value[index]) % prime for index in range(3))  # type: ignore[return-value]


def lower_combination(
    values: dict[int, Vector],
    prime: int,
    r_value: int,
    s_value: int,
    t_value: int,
) -> Vector:
    exact = recurrence_coefficients(prime, r_value, s_value, t_value)
    result: Vector = (0, 0, 0)
    for offset in range(3):
        result = vector_add(
            result,
            vector_scale(values[t_value + offset], exact[offset] % prime, prime),
            prime,
        )
    return result


def second_transfer_components(prime: int, r_value: int, s_value: int) -> dict[str, int]:
    if prime != 2 * r_value + 6 * s_value + 3 or r_value < 2 or r_value % 2:
        raise ValueError((prime, r_value, s_value))
    epsilon = epsilon_for(prime)
    weight, sigma_weight = weight_polynomials(r_value, s_value)
    first_terminal = 2 * s_value + 1
    second_terminal = first_terminal + prime

    values: dict[int, Vector] = {
        0: (0, 1, 0),
        1: (0, 1, 0),
        2: (0, -1, 0),
    }

    for t_value in range(first_terminal):
        rhs = regularized_rhs(
            prime, r_value, t_value, epsilon, sigma_weight
        )
        if rhs:
            raise AssertionError((prime, r_value, s_value, t_value, "early forcing", rhs))
        exact = recurrence_coefficients(prime, r_value, s_value, t_value)
        positive_pivot = -exact[3] % prime
        if positive_pivot == 0:
            raise AssertionError((prime, r_value, s_value, t_value, "early pole"))
        lower = lower_combination(values, prime, r_value, s_value, t_value)
        values[t_value + 3] = vector_scale(lower, pow(positive_pivot, -1, prime), prime)

    first_vector = lower_combination(
        values, prime, r_value, s_value, first_terminal
    )
    first_rhs = regularized_rhs(
        prime, r_value, first_terminal, epsilon, sigma_weight
    )
    if first_vector[0] or first_vector[2]:
        raise AssertionError((prime, r_value, s_value, "first vector", first_vector))
    if first_rhs != (-4 * epsilon) % prime:
        raise AssertionError((prime, r_value, s_value, "first source", first_rhs))
    delta_plus, delta_minus = item223.transfer_mod(r_value, s_value, prime)
    if first_vector[1] != delta_plus:
        raise AssertionError((prime, r_value, s_value, first_vector[1], delta_plus))

    # The first pole leaves u_(T+3) free.  Its coefficient is tracked in
    # the third vector component.
    values[first_terminal + 3] = (0, 0, 1)
    for t_value in range(first_terminal + 1, second_terminal):
        exact = recurrence_coefficients(prime, r_value, s_value, t_value)
        positive_pivot = -exact[3] % prime
        if positive_pivot == 0:
            raise AssertionError((prime, r_value, s_value, t_value, "intermediate pole"))
        lower = lower_combination(values, prime, r_value, s_value, t_value)
        rhs = regularized_rhs(
            prime, r_value, t_value, epsilon, sigma_weight
        )
        numerator = vector_add(lower, ((-rhs) % prime, 0, 0), prime)
        values[t_value + 3] = vector_scale(
            numerator, pow(positive_pivot, -1, prime), prime
        )

    second_vector = lower_combination(
        values, prime, r_value, s_value, second_terminal
    )
    second_rhs = regularized_rhs(
        prime, r_value, second_terminal, epsilon, sigma_weight
    )
    if second_rhs != (2 * epsilon) % prime:
        raise AssertionError((prime, r_value, s_value, "second source", second_rhs))

    free_degree = len(weight) - 1
    support_gap = prime - 3 - free_degree
    if support_gap <= 0:
        raise AssertionError((prime, r_value, s_value, free_degree, support_gap))
    for local_degree, expected in enumerate(weight):
        actual = values[first_terminal + 3 + local_degree][2]
        if actual != expected % prime:
            raise AssertionError(
                (prime, r_value, s_value, local_degree, "free mode", actual, expected)
            )
    if second_vector[2] != 0:
        raise AssertionError((prime, r_value, s_value, "free mode at second pole", second_vector))

    rho_constant, rho_lambda, rho_free = second_vector
    psi = (
        delta_plus * (rho_constant - second_rhs) + first_rhs * rho_lambda
    ) % prime
    theta = (delta_plus - 2 * delta_minus) % prime
    return {
        "epsilon": epsilon,
        "first_terminal": first_terminal,
        "second_terminal": second_terminal,
        "first_rhs": first_rhs,
        "second_rhs": second_rhs,
        "delta_plus": delta_plus,
        "delta_minus": delta_minus,
        "theta": theta,
        "rho_constant": rho_constant,
        "rho_lambda": rho_lambda,
        "rho_free": rho_free,
        "psi": psi,
        "free_mode_degree": free_degree,
        "free_mode_support_gap": support_gap,
    }


def terminal_source_grid(prime_max: int) -> dict[str, Any]:
    rows: list[tuple[int, ...]] = []
    forcing_steps = 0
    for prime, _h_value, r_value, s_value in actual_rows(prime_max):
        epsilon = epsilon_for(prime)
        weight, sigma_weight = weight_polynomials(r_value, s_value)
        first_terminal = 2 * s_value + 1
        second_terminal = first_terminal + prime
        second_pole_shift = second_terminal + 3

        # Before regularization, u_(T+p+3) contains the unique term
        # ell_(3p-1)/(3p), from the leading coefficient W_d=1.
        pole_moment = boundary_moment_from_weight(
            prime, r_value, epsilon, second_pole_shift, weight
        )
        pole_residue = item223.fraction_mod(prime * pole_moment, prime)
        expected_residue = 2 * epsilon * pow(3, -1, prime) % prime
        if pole_residue != expected_residue:
            raise AssertionError(
                (prime, r_value, s_value, pole_residue, expected_residue)
            )

        exact = recurrence_coefficients(
            prime, r_value, s_value, second_terminal
        )
        if exact[3] != -3 * prime:
            raise AssertionError((prime, r_value, s_value, "3p multiplier", exact[3]))
        exact_lower = sum(
            exact[offset]
            * boundary_moment_from_weight(
                prime, r_value, epsilon, second_terminal + offset, weight
            )
            for offset in range(3)
        )
        exact_pole_term = -exact[3] * pole_moment
        if exact_lower != exact_pole_term:
            raise AssertionError(
                (prime, r_value, s_value, "unreduced recurrence", exact_lower, exact_pole_term)
            )
        terminal_source = item223.fraction_mod(exact_pole_term, prime)
        if terminal_source != (2 * epsilon) % prime:
            raise AssertionError(
                (prime, r_value, s_value, terminal_source, 2 * epsilon)
            )

        base_degree = prime + r_value + second_terminal + 1
        top_local_degree = 3 * prime - base_degree
        omitted_coefficient = coefficient(sigma_weight, top_local_degree)
        omitted_weight = item223.ell_numerator(3 * prime - 1, epsilon)
        signed_regularized_rhs = (-omitted_coefficient * omitted_weight) % prime
        if (
            top_local_degree != len(sigma_weight) - 1
            or omitted_coefficient != -1
            or omitted_weight != 2 * epsilon
            or signed_regularized_rhs != (2 * epsilon) % prime
        ):
            raise AssertionError(
                (
                    prime,
                    r_value,
                    s_value,
                    top_local_degree,
                    omitted_coefficient,
                    omitted_weight,
                    signed_regularized_rhs,
                )
            )

        # Audit the sign obtained by subtracting the unreduced 2p pole
        # parts u_t=uhat_t+R_t/p throughout the band before the 3p pole.
        degree = len(weight) - 1

        def singular_numerator(t_value: int) -> int:
            local_degree = prime - r_value - t_value - 1
            return -2 * epsilon * coefficient(weight, local_degree)

        for t_value in range(first_terminal, second_terminal):
            b_value, minus_c, d_value, minus_a = recurrence_coefficients(
                prime, r_value, s_value, t_value
            )
            bracket = (
                b_value * singular_numerator(t_value)
                + minus_c * singular_numerator(t_value + 1)
                + d_value * singular_numerator(t_value + 2)
                + minus_a * singular_numerator(t_value + 3)
            )
            if bracket % prime:
                raise AssertionError(
                    (prime, r_value, s_value, t_value, "nonintegral forcing quotient")
                )
            rhs_from_unreduced = (-bracket // prime) % prime
            rhs_from_deleted_derivative = regularized_rhs(
                prime, r_value, t_value, epsilon, sigma_weight
            )
            if rhs_from_unreduced != rhs_from_deleted_derivative:
                raise AssertionError(
                    (
                        prime,
                        r_value,
                        s_value,
                        t_value,
                        rhs_from_unreduced,
                        rhs_from_deleted_derivative,
                    )
                )
            forcing_steps += 1

        rows.append(
            (
                prime,
                r_value,
                s_value,
                epsilon,
                pole_residue,
                -exact[3],
                terminal_source,
                omitted_coefficient,
                signed_regularized_rhs,
                degree,
            )
        )

    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_REPLAY_OF_PROVED_IDENTITIES",
        "prime_max": prime_max,
        "actual_rows": len(rows),
        "forcing_steps": forcing_steps,
        "unreduced_pole_residue": "p*u_(T+p+3)=ell_(3p-1)/3=2epsilon/3 mod p",
        "regularization_timing": "the residue statement is before regularization; the pole monomial is deleted from uhat",
        "exact_terminal_multiplier": "3p",
        "terminal_source": "+2epsilon",
        "forcing_sign": "Lhat(K_t')=-sum_a [z^(ap)]K_t*ell_(ap-1)",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def finite_survivor_census(prime_max: int) -> dict[str, Any]:
    counts = {
        "actual_rows": 0,
        "item223_transfer_survivors": 0,
        "psi_nonzero_on_item223_survivors": 0,
        "joint_theta_psi_zero": 0,
        "direct_paired_zero_among_joint_survivors": 0,
    }
    survivor_rows: list[tuple[int, ...]] = []
    for prime, h_value, r_value, s_value in actual_rows(prime_max):
        counts["actual_rows"] += 1
        delta_plus, delta_minus = item223.transfer_mod(r_value, s_value, prime)
        theta = (delta_plus - 2 * delta_minus) % prime
        if theta or not delta_plus or not delta_minus:
            continue
        counts["item223_transfer_survivors"] += 1
        data = second_transfer_components(prime, r_value, s_value)
        if data["theta"] != 0:
            raise AssertionError((prime, r_value, s_value, "theta disagreement"))
        psi = data["psi"]
        counts["psi_nonzero_on_item223_survivors"] += psi != 0
        q0, q1 = item218.candidate_conditions(prime, h_value, s_value)
        if psi == 0:
            counts["joint_theta_psi_zero"] += 1
            counts["direct_paired_zero_among_joint_survivors"] += q0 == q1 == 0
        survivor_rows.append(
            (
                prime,
                r_value,
                s_value,
                delta_plus,
                delta_minus,
                data["rho_constant"],
                data["rho_lambda"],
                psi,
                q0,
                q1,
            )
        )

    expected = {
        "actual_rows": 22934,
        "item223_transfer_survivors": 22,
        "psi_nonzero_on_item223_survivors": 22,
        "joint_theta_psi_zero": 0,
        "direct_paired_zero_among_joint_survivors": 0,
    }
    if prime_max == 2000 and counts != expected:
        raise AssertionError((counts, expected))
    stream = json.dumps(survivor_rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_ONLY",
        "prime_max": prime_max,
        **counts,
        "first_item223_survivors": [list(row) for row in survivor_rows[:8]],
        "item223_survivor_with_psi_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "scope_warning": "the finite disappearance of joint survivors is not an all-prime theorem or density estimate",
    }


def certificate(prime_max: int, source_prime_max: int) -> dict[str, Any]:
    source_grid = terminal_source_grid(source_prime_max)
    finite = finite_survivor_census(prime_max)
    return {
        "item": 228,
        "schema": "item228-j1-second-frobenius-v1",
        "dependencies": {
            "item223_checker": ITEM223_PATH.name,
            "item223_checker_sha256": sha256(ITEM223_PATH),
            "item218_checker": ITEM218_PATH.name,
            "item218_checker_sha256": sha256(ITEM218_PATH),
        },
        "parameters": {
            "cell": "p=2r+6s+3, r=2h, h>=1, s>=1",
            "finite_prime_max_inclusive": prime_max,
            "source_replay_prime_max_inclusive": source_prime_max,
        },
        "regularized_recurrence": {
            "weight": "W=(1-z)^r*(1+z^2)^(2s-1)",
            "sigma": "(1-z)*(1+z^2)",
            "moment": "uhat_t deletes from L_epsilon(z^(p+r+t)W) every monomial whose primitive denominator is divisible by p",
            "exact_coefficients": "B*u_t-C*u_(t+1)+D*u_(t+2)-A*u_(t+3), A=p+2r+4s+t+2, B=p+r+t+1, C=p+2r+t+2, D=p+r+4s+t+1",
            "forcing": "B*uhat_t-C*uhat_(t+1)+D*uhat_(t+2)-A*uhat_(t+3)=-sum_(a>=1)[z^(ap)]z^(p+r+t+1)*sigma*W*ell_(ap-1)",
            "ell_multiples_mod_4": ["ell_(p-1)=-2epsilon", "ell_(2p-1)=-4epsilon", "ell_(3p-1)=2epsilon", "ell_(4p-1)=4epsilon"],
        },
        "second_terminal_theorem": {
            "first_terminal": "T=2s+1, exact multiplier 2p and source -4epsilon",
            "second_terminal": "T+p, exact multiplier 3p and source +2epsilon",
            "unreduced_residue": "before regularization, p*u_(T+p+3)=ell_(3p-1)/3=2epsilon/3 mod p",
            "deleted_term_sign": "the top coefficient of sigma*W is -1, so deleting its derivative contribution gives -(-1)*(2epsilon)=+2epsilon",
            "free_mode": "the free coefficient after the first terminal is W itself",
            "free_mode_degree": "r+4s-2<p-3",
            "free_mode_consequence": "its three entries at the second terminal vanish identically",
            "terminal_vector": "rho_constant+lambda*rho_lambda; rho_free=0",
            "psi": "Delta_plus*(rho_constant-2epsilon)-4epsilon*rho_lambda",
            "necessary": "a collision requires Delta_plus=2Delta_minus!=0 and Psi=0 mod p",
            "sufficiency": "not claimed; Psi is only an additional necessary condition",
        },
        "terminal_source_replay": source_grid,
        "finite_survivor_census": finite,
        "rate_ledger": {
            "j1_cell_mass_per_m_if_fully_excluded": "1/6",
            "full_cell_exclusion": "OPEN",
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "reason": "no all-prime or weighted bound for simultaneous Theta=Psi zeros is proved",
        },
        "status_ledger": {
            "PROVED": [
                "the exact regularized recurrence and its forcing sign",
                "the direct unreduced 3p residue and +2epsilon terminal source",
                "the first-pole free mode equals W and vanishes before the second terminal",
                "every collision satisfies Delta_plus=2Delta_minus!=0 and Psi=0",
            ],
            "EXACT_FINITE": [
                "the direct source replay through the declared source bound",
                "Psi eliminates every Item223 transfer survivor through the declared finite bound",
            ],
            "OPEN": [
                "all-prime exclusion or a weighted bound for simultaneous Theta=Psi zeros",
                "sufficiency of the transfer conditions",
                "any positive Route-1 rate or radical saving from the j=1 cell",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=2000)
    parser.add_argument("--source-prime-max", type=int, default=251)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.prime_max < 251 or not (13 <= args.source_prime_max <= args.prime_max):
        raise ValueError("require prime-max>=251 and 13<=source-prime-max<=prime-max")
    result = certificate(args.prime_max, args.source_prime_max)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "source_rows": result["terminal_source_replay"]["actual_rows"],
                "item223_survivors": result["finite_survivor_census"]["item223_transfer_survivors"],
                "joint_theta_psi_zero": result["finite_survivor_census"]["joint_theta_psi_zero"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
