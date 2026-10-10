#!/usr/bin/env python3
"""Deterministic exact replay for Item 373.

Checks the symmetric singleton saturation formula, exact first quotient,
declared polynomial-dominance boxes, and raw height scales.  No actual prime,
target, factorization, or half-bound census is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any


DEPENDENCY_HASHES = {
    "sources/item316_beta_intermediate_ostrowski_no_go_report.md": (
        "8d6dce8354f08e94a252a2120cf677d9a374df95507a9297dcb064a1982fb6b0"
    ),
    "results/item316_beta_intermediate_ostrowski_no_go_certificate.json": (
        "5167e9d160fcecac86791944e41a176d3400f2a6856090de7cf78d55984e7aa4"
    ),
    "results/item316_root_audit.json": (
        "6cad978132f5f09c687aa8fcf8dcd92a7d917cf9411a69f679c7757139229175"
    ),
    "manifests/item316_beta_intermediate_ostrowski_no_go_manifest.json": (
        "aac741658430fb661de078adfeafdbc3a9d20312a8fd8725cb4244d406d9bcf6"
    ),
    "sources/item346_beta_t_avoiding_radical_localization_report.md": (
        "2ad742c14d0adbc74da6c46394ed89f68cec8888a3c9d22ee4f230a4e16548a5"
    ),
    "scripts/item346_beta_t_avoiding_radical_localization_certificate.py": (
        "76c020b07d199a7283d7373a3ef677643d3be01adfe7480628f92ccdad7498c0"
    ),
    "results/item346_beta_t_avoiding_radical_localization_certificate.json": (
        "29a20d6ede62db23658d66db8e57af4a2982c9b66fd12d104f0070b3280aefab"
    ),
    "results/item346_beta_t_avoiding_radical_localization_root_audit.json": (
        "c9273d7e187ee2c9b4b91bffc65769f1a29f937613c36960e4ed5871c5782089"
    ),
    "manifests/item346_beta_t_avoiding_radical_localization_manifest.json": (
        "5029cf3483fdf6cce4bbc0d454bca362bb2796104ca36b353d0161e374915530"
    ),
    "sources/item358_beta_actual_low_incidence_saturation_barrier_report.md": (
        "681c9f9cbe926978c78f632084c8be83439c2ac3f5e50f2c2697a49f2f0da68d"
    ),
    "scripts/item358_beta_actual_low_incidence_saturation_barrier_certificate.py": (
        "c997c7f3739fe5dc98ee2e48c3ebfd1a67e74289e175d52bc8d5adfb1f9565bf"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_certificate.json": (
        "4da88e55dec36f3c130def549007c8ae1509ff0a029dfed9ff25f67a78c2ffa3"
    ),
    "results/item358_beta_actual_low_incidence_saturation_barrier_root_audit.json": (
        "a1a48f7d7080834ebf3be56b47d8056733e88e1913e8f6ea784f97a5eb2d9172"
    ),
    "manifests/item358_beta_actual_low_incidence_saturation_barrier_manifest.json": (
        "4ba799fe2fc8cb6063034d844f91bcaec6c3fc84d043b1f46c675fce400acfb1"
    ),
    "sources/item367_beta_uniform_affine_carrier_no_go_report.md": (
        "3827c4e9d9532135fdb2e338397523ce8b2936483b09cf5accbc974002023798"
    ),
    "scripts/item367_beta_uniform_affine_carrier_no_go_certificate.py": (
        "6c9322838eccbca1ac257f7526fbae1a11f77937679b00fc4824aa40006f3a19"
    ),
    "results/item367_beta_uniform_affine_carrier_no_go_certificate.json": (
        "b6fc66168a18237a67e43d75c13dc36666bd5c0fbb444d98fdc0a928bb186d93"
    ),
    "results/item367_beta_uniform_affine_carrier_no_go_root_audit.json": (
        "40dd78454cd16a16581e3fd1f3d1c89c61b4c1e70465f4688f8298c59fa2c843"
    ),
    "manifests/item367_beta_uniform_affine_carrier_no_go_manifest.json": (
        "3d3d7db889f0b39fab5b1e1792bf2332aa8d57a1718c6681dc1cbd5c915c20b1"
    ),
    "sources/item370_beta_q_free_residual_saturation_no_go_report.md": (
        "760767813ab0bbd56114f6a6c264ce396ccc2ec8eb9e7a3139e56b155051fef4"
    ),
    "scripts/item370_beta_q_free_residual_saturation_no_go_certificate.py": (
        "df51c792f64c945ceade3ae01ef24fab3ed87d8eed232088e36db43332b61edd"
    ),
    "results/item370_beta_q_free_residual_saturation_no_go_certificate.json": (
        "78703c11fee6715189fc8c0c7a513bef5eda1d973ab27b3e1f486d0b908008fb"
    ),
    "results/item370_beta_q_free_residual_saturation_no_go_root_audit.json": (
        "264c64d6495c2d1a20eff67b270379adb95ffc5f5711269dc325f11988c12ea2"
    ),
    "manifests/item370_beta_q_free_residual_saturation_no_go_manifest.json": (
        "53147f04c406d69c67f3b53b7032d6c90db20380583ebb79238f84505cd6d6d2"
    ),
}


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def dependency_audit() -> dict[str, Any]:
    root = Path(__file__).resolve().parent.parent
    rows = []
    for relative_path, expected in DEPENDENCY_HASHES.items():
        payload = (root / relative_path).read_bytes()
        actual = hashlib.sha256(payload).hexdigest()
        assert actual == expected, (relative_path, actual, expected)
        rows.append(
            {"path": relative_path, "bytes": len(payload), "sha256": actual}
        )
    return {"count": len(rows), "rows": rows, "rows_digest": digest(rows)}


def valuation(value: int, prime: int) -> int:
    assert value != 0 and prime > 1
    result = 0
    value = abs(value)
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def symmetric_data(loads: list[int], t_value: int) -> dict[str, int]:
    assert loads and all(load > 0 for load in loads)
    product = math.prod(loads)
    top_derivative = sum(product // load for load in loads)
    exponent = len(loads)
    saturated = product // math.gcd(product, abs(t_value * top_derivative) ** exponent)
    return {
        "P": product,
        "E": top_derivative,
        "N": exponent,
        "S_sym": saturated,
    }


def singleton_saturation_controls() -> dict[str, Any]:
    A = 10
    base_loads = [2, 3, 5, 7]
    t_zero_data = symmetric_data(base_loads, 0)
    assert t_zero_data["S_sym"] == 1
    rows = []
    for prime in [11, 13]:
        for hit_count in range(0, len(base_loads) + 1):
            for hit_indices in itertools.combinations(range(len(base_loads)), hit_count):
                loads = list(base_loads)
                for index in hit_indices:
                    loads[index] *= prime
                assert all(load < A * A for load in loads)
                for t_has_prime in [False, True]:
                    t_value = prime if t_has_prime else 1
                    data = symmetric_data(loads, t_value)
                    product_valuation = valuation(data["P"], prime) if data["P"] % prime == 0 else 0
                    e_is_unit = data["E"] % prime != 0
                    saturated_valuation = (
                        valuation(data["S_sym"], prime)
                        if data["S_sym"] % prime == 0
                        else 0
                    )
                    assert product_valuation == hit_count
                    if hit_count == 1:
                        assert e_is_unit
                    if hit_count >= 2:
                        assert not e_is_unit
                    expected = int(hit_count == 1 and not t_has_prime)
                    assert saturated_valuation == expected
                    quotient_bridge = None
                    if hit_count == 1 and not t_has_prime:
                        hit = hit_indices[0]
                        quotient_bridge = (
                            (data["P"] // prime) * pow(data["E"], -1, prime)
                        ) % prime
                        hit_quotient = loads[hit] // prime
                        assert 1 <= hit_quotient < A
                        assert quotient_bridge == hit_quotient % prime
                        assert product_valuation == 1
                    rows.append(
                        {
                            "declared_prime": prime,
                            "hit_indices": list(hit_indices),
                            "t_has_prime": t_has_prime,
                            "P_valuation": product_valuation,
                            "E_is_unit": e_is_unit,
                            "S_sym_valuation": saturated_valuation,
                            "first_quotient_bridge": quotient_bridge,
                        }
                    )
    return {
        "capital_A": A,
        "t_zero_symmetric_carrier": t_zero_data["S_sym"],
        "rows": rows,
        "rows_digest": digest(rows),
        "declared_algebra_controls_only": True,
        "actual_prime_or_target_census_performed": False,
    }


def evaluate_polynomial(coefficients: tuple[int, ...], value: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def polynomial_dominance_controls() -> dict[str, Any]:
    rows = []
    for degree, coefficient_bound, value in [(1, 5, 50), (2, 4, 100), (3, 3, 120)]:
        assert value >= 2 * degree * coefficient_bound + 2
        checked = 0
        minimum_absolute = None
        for lower_coefficients in itertools.product(
            range(-coefficient_bound, coefficient_bound + 1), repeat=degree
        ):
            for leading in range(-coefficient_bound, coefficient_bound + 1):
                if leading == 0:
                    continue
                coefficients = lower_coefficients + (leading,)
                result = abs(evaluate_polynomial(coefficients, value))
                assert result * 2 >= value**degree
                minimum_absolute = (
                    result if minimum_absolute is None else min(minimum_absolute, result)
                )
                checked += 1
        rows.append(
            {
                "degree": degree,
                "coefficient_bound": coefficient_bound,
                "E_value": value,
                "polynomials_checked": checked,
                "minimum_absolute_value": minimum_absolute,
                "dominance_bound": "2*|C(E)|>=E^degree",
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def q_sequence(n_max: int) -> list[int]:
    values = [1, 1]
    for n in range(2, n_max + 1):
        values.append((4 * n - 2) * values[-1] + values[-2])
    return values


def height_scale_controls() -> dict[str, Any]:
    q_values = q_sequence(14)
    rows = []
    for n in range(6, 15):
        A = 4 * n - 2
        b = q_values[n]
        N_max = n - 4
        product_log_ceiling = 2 * N_max * math.log(A)
        rows.append(
            {
                "n": n,
                "capital_A": A,
                "b": str(b),
                "N_max": N_max,
                "two_N_log_A_over_log_b": product_log_ceiling / math.log(b),
                "symmetric_carrier_raw_ceiling": "log S_sym<=log P<2N log A",
            }
        )
    return {"rows": rows, "rows_digest": digest(rows)}


def proof_object() -> dict[str, Any]:
    return {
        "symmetric_carrier": (
            "For positive actual loads set P=product Z_j, "
            "E=sum_j P/Z_j, and S_sym=P/gcd(P,(|t|E)^N). Since p>A and "
            "Z_j<A^2 imply v_p(Z_j)<=1, S_sym has valuation one exactly "
            "at t-away singleton incidences and zero at all other p>A."
        ),
        "actual_U": (
            "Therefore U_11=gcd(Q^[1],rad_{>A}(S_sym)) exactly. This is a "
            "prime-independent actual-family formula, but log S_sym is at "
            "most 2N log A=(2+o(1))log b and gives no new capacity bound."
        ),
        "first_quotient": (
            "At a singleton hit j, v_p(P)=1, E is a unit, and "
            "(P/p)E^{-1}=Z_j/p mod p with 1<=Z_j/p<A. Thus P, P*E^r, "
            "and their p-unit monomial quotients have exact valuation one."
        ),
        "bounded_degree": (
            "For F=P*C(E)/V with V a p-unit, an extra p is equivalent to "
            "p|C(E). For a first-quotient residual H=C(E)/D with D and the "
            "coefficients bounded by b^o, positive beta mass gives "
            "E>A^(r-1) with r=Omega(n). A nonconstant fixed-degree C then "
            "satisfies |H|>=E^d/(2D), so it is not sub-beta. The "
            "constant/content branch needs a new actual divisibility theorem."
        ),
        "scope": (
            "The theorem closes top-symmetric monomial/unit first quotients "
            "and sub-beta bounded-degree univariate C(E) portfolios. It does "
            "not close multivariate elementary-symmetric cancellations, "
            "gcd/radical height, or beta-height full-support states."
        ),
    }


def build_certificate() -> dict[str, Any]:
    dependencies = dependency_audit()
    saturation = singleton_saturation_controls()
    dominance = polynomial_dominance_controls()
    heights = height_scale_controls()
    proof = proof_object()
    controls = {"saturation": saturation, "dominance": dominance, "heights": heights}
    return {
        "schema": "item373-beta-symmetric-singleton-first-quotient-certificate-v1",
        "item": 373,
        "date": "2026-09-01",
        "status": "PROVED_SYMMETRIC_SINGLETON_CARRIER_AND_FIRST_QUOTIENT_NO_GO",
        "dependencies": dependencies,
        "theorem": {
            "exact_symmetric_actual_singleton_carrier": "PROVED",
            "singleton_product_valuation_exactly_one": "PROVED",
            "top_symmetric_first_quotient_bridge": "PROVED",
            "monomial_unit_first_quotient_lift": "PROVED_IMPOSSIBLE",
            "bounded_degree_univariate_sub_beta_residual": "PROVED_SCOPED_NO_GO",
            "nonzero_sub_beta_actual_carrier": "OPEN",
            "multivariate_symmetric_correlation": "OPEN",
        },
        "proof_object": proof,
        "proof_object_digest": digest(proof),
        "declared_controls": {
            **controls,
            "controls_digest": digest(controls),
            "finite_rows_promoted": False,
            "actual_prime_or_target_census_performed": False,
        },
        "strict_scope": {
            "actual_item316_claim_from_declared_rows": False,
            "closes": [
                "top symmetric product P as a source of a second p-adic digit at singleton primes",
                "P times powers of E and p-unit monomial quotients as extra-digit mechanisms",
                "nonconstant fixed-degree C(E) with sub-beta coefficient height as a sub-beta residual on a positive-mass branch",
            ],
            "does_not_close": [
                "multivariate elementary-symmetric cancellations",
                "height of the exact gcd/radical symmetric carrier",
                "full-support beta-height recurrence states",
                "quotients with beta-height denominators or new gcd cancellation",
                "a constant/content residual with actual U_11 divisibility",
                "beta capacity, Route 1, or e+pi",
            ],
            "zero_residual_admissible": False,
            "candidate_dependent_constants_admissible": False,
            "canonical_files_modified": False,
        },
        "capacity": {
            "raw_symmetric_carrier_ceiling": "log S_sym<2N log A=(2+o(1))*log b",
            "post_intersection_ceiling": "log U_11<=log Q<=log b",
            "first_quotient_increment": 0,
            "constructed_sub_beta_actual_carrier": False,
            "new_beta_capacity_reduction": 0,
            "new_route1_rate": 0,
            "booking": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="work/item373_beta_symmetric_singleton_first_quotient_certificate.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate()
    output = Path(arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "item": certificate["item"],
                "status": certificate["status"],
                "booking": certificate["capacity"]["booking"],
                "sub_beta_actual_carrier": certificate["theorem"][
                    "nonzero_sub_beta_actual_carrier"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
