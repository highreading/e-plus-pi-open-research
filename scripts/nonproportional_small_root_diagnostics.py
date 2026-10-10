#!/usr/bin/env python3
"""Independent numerical diagnostics for the nonproportional theorem.

This script does not prove any asymptotic assertion.  It evaluates the
factored Rodrigues integral directly, checks the endpoint logarithmic
formula on deliberately nonproportional triples, checks the compact-slope
f-dominant saddle formula, and samples the zero-balanced hypergeometric
factor covered rigorously by Runckel's theorem.

It does not import either implementation used by the earlier exact scans.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp


def zeta_eta(N: int) -> tuple[mp.mpc, mp.mpc]:
    zeta = mp.e ** (2j * mp.pi / N)
    return zeta, 1 - zeta


def falling_ratios(d: int, f: int) -> list[mp.mpf]:
    """Return d^(under q)/(d+f)^(under q), q=0,...,d."""
    ratios = [mp.mpf(1)]
    for q in range(1, d + 1):
        ratios.append(ratios[-1] * mp.mpf(d - q + 1) / (d + f - q + 1))
    return ratios


def t_value(u: mp.mpc, ratios: list[mp.mpf]) -> mp.mpc:
    """Evaluate T(u) from the factorially convergent reversed sum."""
    answer = mp.mpc(0)
    inverse_power = mp.mpc(1)
    for q, ratio in enumerate(ratios):
        if q:
            inverse_power /= u
        answer += (-1) ** q * ratio * inverse_power / mp.factorial(q)
    return answer


def u_power_t_coefficients(ratios: list[mp.mpf]) -> list[mp.mpf]:
    """Descending coefficients of the polynomial u^d T(u)."""
    return [
        (-1) ** q * ratio / mp.factorial(q)
        for q, ratio in enumerate(ratios)
    ]


def u_power_t_value(u: mp.mpf, coefficients: list[mp.mpf]) -> mp.mpf:
    """Evaluate u^d T(u) without the apparent singularity at u=0."""
    # The list is ordered by q=0,...,d, hence by powers u^d,...,u^0.
    # Horner evaluation remains finite at u=0 and is stable at the high
    # precision used below.
    answer = mp.mpf(0)
    for coefficient in coefficients:
        answer = answer * u + coefficient
    return answer


def integral_j(c: int, d: int, f: int, N: int) -> mp.mpc:
    """Evaluate J in equation (39) after t=d(1-u)."""
    _, eta = zeta_eta(N)
    ratios = falling_ratios(d, f)
    coefficients = u_power_t_coefficients(ratios)

    def integrand(t: mp.mpf) -> mp.mpc:
        u = 1 - t / d
        k_value = u_power_t_value(u, coefficients)
        return (
            t**c
            * u**c
            * k_value
            / (1 - eta * u) ** (c + 1)
        )

    # The gamma-like mass is near t=c.  Extra breakpoints prevent the
    # adaptive quadrature from overlooking it when d is large.
    candidates = [
        mp.mpf(0),
        mp.mpf(1),
        mp.mpf(max(2, c // 2)),
        mp.mpf(max(3, c)),
        mp.mpf(max(5, 2 * c + 4)),
        mp.mpf(max(10, c + 12 * math.sqrt(c + 1) + 24)),
        mp.mpf(d) / 2,
        mp.mpf(d),
    ]
    points = sorted({value for value in candidates if 0 <= value <= d})
    if points[0] != 0:
        points.insert(0, mp.mpf(0))
    if points[-1] != d:
        points.append(mp.mpf(d))
    value = mp.quad(integrand, points, method="gauss-legendre")
    return value / mp.mpf(d) ** (c + 1)


def principal_log(c: int, d: int, f: int, N: int) -> mp.mpf:
    """Log of N|A(1)R_log|, the asymptotically dominant summand."""
    _, eta = zeta_eta(N)
    ratios = falling_ratios(d, f)
    beta = mp.mpf(d) / (d + f)
    del beta  # Recorded implicitly by the exact ratios.
    t_one = mp.fsum(
        (-1) ** q * ratio / mp.factorial(q)
        for q, ratio in enumerate(ratios)
    )
    log_binomial = mp.loggamma(d + f + 1) - mp.loggamma(d + 1) - mp.loggamma(f + 1)
    log_a_one = log_binomial + mp.log(abs(t_one))
    j_value = integral_j(c, d, f, N)
    log_r_log = (
        log_binomial
        + (d + 2 * c + 1) * mp.log(abs(eta))
        + mp.log(abs(j_value))
    )
    return mp.log(N) + log_a_one + log_r_log


def endpoint_prediction(c: int, d: int, f: int, N: int) -> mp.mpf:
    _, eta = zeta_eta(N)
    log_binomial = mp.loggamma(d + f + 1) - mp.loggamma(d + 1) - mp.loggamma(f + 1)
    beta = mp.mpf(d) / (d + f)
    return (
        mp.log(N)
        + 2 * log_binomial
        + (d + 2 * c + 1) * mp.log(abs(eta))
        + mp.loggamma(c + 1)
        - (c + 1) * mp.log(d)
        - 2 * beta
    )


def chi_value(c: int, d: int, N: int) -> mp.mpf:
    zeta, eta = zeta_eta(N)
    lam = mp.mpf(d) / c
    radicand = lam**2 + 4 * (lam + 1) * mp.conj(zeta)
    r_star = (lam + mp.sqrt(radicand)) / 2
    u_star = r_star / (1 + r_star)
    return (
        (lam + 2) * mp.log(abs(eta))
        + (lam + 1) * mp.log(abs(u_star))
        + mp.log(abs(1 - u_star))
        - mp.log(abs(1 - eta * u_star))
    )


def compact_saddle_prediction(c: int, d: int, f: int, N: int) -> mp.mpf:
    log_binomial = mp.loggamma(d + f + 1) - mp.loggamma(d + 1) - mp.loggamma(f + 1)
    return 2 * log_binomial + c * chi_value(c, d, N) - mp.log(c) / 2


def endpoint_records() -> list[dict]:
    triples = [
        (0, 30, 0),
        (0, 30, 1),
        (1, 30, 1),
        (2, 40, 2),
        (3, 60, 3),
        (3, 60, 60),
        (8, 160, 8),
        (8, 160, 800),
    ]
    records = []
    for N in (3, 4, 6):
        for c, d, f in triples:
            observed = principal_log(c, d, f, N)
            predicted = endpoint_prediction(c, d, f, N)
            records.append(
                {
                    "N": N,
                    "c": c,
                    "d": d,
                    "f": f,
                    "log_principal_summand": mp.nstr(observed, 30),
                    "endpoint_log_prediction": mp.nstr(predicted, 30),
                    "log_residual": mp.nstr(observed - predicted, 20),
                }
            )
    return records


def f_dominant_records() -> list[dict]:
    triples = [(8, 16, 8), (8, 16, 80), (8, 16, 800),
               (12, 36, 12), (12, 36, 360), (12, 36, 3600)]
    records = []
    for N in (3, 4, 6):
        for c, d, f in triples:
            observed = principal_log(c, d, f, N)
            predicted = compact_saddle_prediction(c, d, f, N)
            records.append(
                {
                    "N": N,
                    "c": c,
                    "d": d,
                    "f": f,
                    "log_principal_summand": mp.nstr(observed, 30),
                    "saddle_log_without_constant": mp.nstr(predicted, 30),
                    "bounded_log_residual": mp.nstr(observed - predicted, 20),
                }
            )
    return records


def hypergeometric_records() -> dict:
    def euler_factor(c: int, d: int, eta: mp.mpc, method: str) -> mp.mpc:
        """Evaluate 2F1 through its nonsingular Euler integral divided by B."""
        integral = mp.quad(
            lambda u: u ** (c + d) * (1 - u) ** c
            / (1 - eta * u) ** (c + 1),
            [0, 1],
            method=method,
        )
        return integral / mp.beta(c + d + 1, c + 1)

    minima: dict[str, dict] = {}
    quadrature_checks = []
    for N in (3, 4, 6):
        _, eta = zeta_eta(N)
        best_value = mp.inf
        best_parameters = None
        for c in range(7):
            for offset in range(7):
                d = 2 * c + offset
                value = euler_factor(c, d, eta, "gauss-legendre")
                modulus = abs(value)
                if modulus < best_value:
                    best_value = modulus
                    best_parameters = [c, d]
        minima[str(N)] = {
            "sampled_c_range": [0, 6],
            "sampled_offset_range": [0, 6],
            "minimum_modulus": mp.nstr(best_value, 30),
            "at_c_d": best_parameters,
            "evaluation": (
                "Gauss-Legendre Euler integral divided by the beta factor; "
                "this quotient equals the sampled 2F1"
            ),
            "status": "diagnostic only; nonvanishing is proved by Runckel",
        }

        for c, d in ((0, 0), (1, 2), (3, 7)):
            gauss_value = euler_factor(c, d, eta, "gauss-legendre")
            tanh_sinh_value = euler_factor(c, d, eta, "tanh-sinh")
            quadrature_checks.append(
                {
                    "N": N,
                    "c": c,
                    "d": d,
                    "methods": ["gauss-legendre", "tanh-sinh"],
                    "relative_difference": mp.nstr(
                        abs(gauss_value - tanh_sinh_value)
                        / abs(tanh_sinh_value),
                        12,
                    ),
                }
            )
    return {
        "sampled_minima": minima,
        "euler_quadrature_cross_checks": quadrature_checks,
    }


def h_uniformity_records() -> list[dict]:
    points = [mp.mpc(1), mp.mpc("0.8", "-0.1"), mp.mpc("1.05", "-0.05")]
    records = []
    for d, f in ((30, 0), (30, 1), (30, 30), (30, 3000),
                 (120, 0), (120, 120), (120, 12000)):
        ratios = falling_ratios(d, f)
        beta = mp.mpf(d) / (d + f)
        errors = []
        for u in points:
            exact = t_value(u, ratios)
            limiting = mp.e ** (-beta / u)
            errors.append(abs(exact / limiting - 1))
        records.append(
            {
                "d": d,
                "f": f,
                "beta": mp.nstr(beta, 20),
                "max_relative_error_at_test_points": mp.nstr(max(errors), 20),
            }
        )
    return records


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/nonproportional_small_root_diagnostics.json"),
    )
    parser.add_argument("--dps", type=int, default=100)
    args = parser.parse_args()
    mp.mp.dps = args.dps

    theorem = Path("sources/nonproportional_small_root_classification.md")
    script = Path(__file__)
    payload = {
        "status": "numerical diagnostics only",
        "mpmath_decimal_precision": args.dps,
        "theorem_sha256_at_run": sha256(theorem),
        "script_sha256_at_run": sha256(script),
        "H_uniformity": h_uniformity_records(),
        "endpoint_checks": endpoint_records(),
        "f_dominant_checks": f_dominant_records(),
        "runckel_factor_checks": hypergeometric_records(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
