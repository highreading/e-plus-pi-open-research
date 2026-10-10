#!/usr/bin/env python3
"""Portable exact certificate for Item 289.

The checker exercises only universal integer identities and one declared
lattice witness.  It performs no actual fixed-j=1 collision census.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = ROOT / "results" / "item289_j1_crt_norm_balancing_certificate.json"

DEPENDENCIES = {
    "sources/item264_j1_weighted_gate_report.md": "767005f8fad07b1fa633bfdd23436e36c7cdef346d032030390c437f207c9344",
    "sources/item281_j1_isolated_fitting_norm_report.md": "fcd8f91426edf31a8de5b90dbc986ae04c08865ddfe448fc9e240410c5c1fd80",
    "sources/item284_j1_parameter_norm_report.md": "bc8b84ab59f2e8aed790237d8e57191c78e4c5811d198137ab5ceb6d68a23889",
    "scripts/item284_j1_parameter_norm_certificate.py": "992a13836c1a0736b464630feb24f6e79a65f2423bdd82fa181150f801460451",
    "sources/item200_common_log_gcd_report.md": "06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68",
    "scripts/item200_common_log_gcd_certificate.py": "26ef60a6f89d569d7f22fdd504dd76f5b3b6a2c11d9b99f2c56a0be645c1396b",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def dependency_audit() -> dict[str, Any]:
    checked: dict[str, str] = {}
    for relative, expected in DEPENDENCIES.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            raise AssertionError((relative, expected, actual))
        checked[relative] = actual
    return {"count": len(checked), "sha256": checked}


def primes_of(number: int) -> list[int]:
    result = []
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            result.append(divisor)
            while number % divisor == 0:
                number //= divisor
        divisor += 1
    if number > 1:
        result.append(number)
    return result


def is_nonsquare(value: int, prime: int) -> bool:
    return value % prime != 0 and pow(value % prime, (prime - 1) // 2, prime) == prime - 1


def nearest_norm(x: int, y: int, b: int, d0: int) -> tuple[int, int, int]:
    if y == 0:
        return x * x, 0, x * x
    t = x * x - d0 * y * y
    q = b * y * y
    r = t % q
    if r < q - r:
        k = (t - r) // q
        value = r
    elif r > q - r:
        k = (t + q - r) // q
        value = -(q - r)
    else:
        raise AssertionError((x, y, b, d0, "unexpected nearest tie"))
    if value != x * x - (d0 + k * b) * y * y:
        raise AssertionError((x, y, b, d0, k, value))
    return abs(value), k, value


def algebra_replay() -> tuple[dict[str, Any], str]:
    classes = [
        (3, 2),
        (5, 2),
        (7, 3),
        (15, 2),
        (21, 5),
        (35, 3),
    ]
    digest = hashlib.sha256()
    rows = 0
    products = 0
    for b, d0 in classes:
        primes = primes_of(b)
        if math.prod(primes) != b or not all(is_nonsquare(d0, p) for p in primes):
            raise AssertionError((b, d0, primes))
        for x in range(-18, 19):
            for y in range(-18, 19):
                if x == y == 0:
                    continue
                c = math.gcd(abs(x), abs(y))
                minimum, k_star, signed = nearest_norm(x, y, b, d0)
                if minimum <= 0 or minimum % (c * c):
                    raise AssertionError((b, d0, x, y, minimum, c))
                n0 = x * x - d0 * y * y
                n1 = x * x - (d0 + b) * y * y
                if math.gcd(abs(n0), abs(n1)) != c * c:
                    raise AssertionError((b, d0, x, y, n0, n1, c))
                if y:
                    q = b * y * y
                    candidates = []
                    quotient = (x * x - d0 * y * y) // q
                    for k in range(quotient - 3, quotient + 5):
                        candidates.append(abs(x * x - (d0 + k * b) * y * y))
                    if minimum != min(candidates):
                        raise AssertionError((b, d0, x, y, minimum, min(candidates)))
                for p in primes:
                    for k in (k_star - 2, k_star - 1, k_star, k_star + 1, k_star + 2):
                        norm = x * x - (d0 + k * b) * y * y
                        collision = x % p == 0 and y % p == 0
                        if (norm % p == 0) != collision:
                            raise AssertionError((b, d0, x, y, p, k, norm))
                        expected = 2 * min(v_p(x, p), v_p(y, p))
                        if v_p(norm, p) != expected:
                            raise AssertionError((b, d0, x, y, p, k, norm, expected))
                # Natural degree-two product: independent minima multiply.
                product_minimum = minimum * minimum
                local_values = []
                for k1 in range(k_star - 1, k_star + 2):
                    for k2 in range(k_star - 1, k_star + 2):
                        local_values.append(abs(
                            (x * x - (d0 + k1 * b) * y * y)
                            * (x * x - (d0 + k2 * b) * y * y)
                        ))
                if product_minimum != min(local_values):
                    raise AssertionError((b, d0, x, y, product_minimum, min(local_values)))
                digest.update(
                    f"{b},{d0},{x},{y},{c},{minimum},{k_star},{signed}\n".encode("ascii")
                )
                rows += 1
                products += 1
    return {
        "CRT_classes": len(classes),
        "nonzero_integer_pairs": rows,
        "degree_two_product_rows": products,
        "actual_collision_rows_sampled": 0,
        "label": "EXACT FINITE ONLY universal algebra replay",
    }, digest.hexdigest()


def v_p(number: int, prime: int) -> int:
    if number == 0:
        return 10**9
    number = abs(number)
    value = 0
    while number % prime == 0:
        number //= prime
        value += 1
    return value


def boundary_audit() -> dict[str, Any]:
    cases = [
        {"x": 7, "y": 0, "B": 35, "d0": 3, "minimum": 49},
        {"x": 0, "y": 6, "B": 35, "d0": 3, "minimum": 108},
    ]
    for case in cases:
        minimum, _, _ = nearest_norm(case["x"], case["y"], case["B"], case["d0"])
        if minimum != case["minimum"]:
            raise AssertionError((case, minimum))
    return {
        "nonzero_coordinate_cases": cases,
        "both_zero": "all representative norms are zero; height route degenerate",
        "B_equals_one": "candidate set empty; zero prime-log mass",
    }


def covering_witness() -> dict[str, Any]:
    b, d0, x, y = 35, 3, 163, 36
    if not all(is_nonsquare(d0, p) for p in primes_of(b)):
        raise AssertionError("declared d0 is not simultaneous nonsquare")
    t = x * x - d0 * y * y
    q = b * y * y
    minimum, k, signed = nearest_norm(x, y, b, d0)
    if (t, q, minimum, k, signed) != (22681, 45360, 22679, 1, -22679):
        raise AssertionError((t, q, minimum, k, signed))
    if minimum != q // 2 - 1 or math.gcd(t, q) != 1:
        raise AssertionError((t, q, minimum))
    return {
        "B": b,
        "d0": d0,
        "X": x,
        "Y": y,
        "T": t,
        "Q": q,
        "minimum": minimum,
        "minimizing_k": k,
        "signed_norm": signed,
        "distance_from_half_Q": 1,
        "label": "declared exact lattice witness; not an actual-family row",
    }


def height_audit() -> dict[str, Any]:
    h_constant = 6.327627545440858
    kappa = -4 * math.log(2) + math.pi / math.sqrt(3) + 3 * math.log(3)
    normalized = h_constant - kappa + 1 / 12
    raw = h_constant / 2 + 1 / 24
    if not (normalized > 1 / 6 and raw > 1 / 6):
        raise AssertionError((normalized, raw))
    return {
        "H": h_constant,
        "kappa": kappa,
        "balanced_normalized_ratio": normalized,
        "balanced_raw_ratio": raw,
        "raw_candidate_mass_per_M": 1 / 6,
        "useful_normalized_norm_exponent_needed": "strictly less than 1/3",
        "height_admission_passed": False,
    }


def certificate() -> dict[str, Any]:
    replay, replay_hash = algebra_replay()
    body: dict[str, Any] = {
        "schema": "item289-j1-crt-norm-balancing-certificate-v1",
        "labels": {
            "nearest_representative": "PROVED exact global optimum",
            "primitive_cofactor": "PROVED coprime to full candidate product",
            "candidate_valuation_invariant": "PROVED for every representative",
            "all_representative_ideal": "PROVED equal to gcd(x,y)^2 Z",
            "algebra_replay": "EXACT FINITE ONLY",
            "actual_collision_census_performed": False,
            "new_route1_rate": 0,
        },
        "dependencies": dependency_audit(),
        "theorem": {
            "scope": "nonempty candidate set B>1; B=1 is a zero-capacity boundary",
            "minimum": "dist(x^2-d0*y^2, B*y^2*Z)",
            "factorization": "N_k=c^2*(X^2-d0*Y^2-k*B*Y^2)",
            "primitive_gcd": "gcd(X^2-d0*Y^2,B*Y^2)=1",
            "candidate_valuation": "v_p(N_k)=2*v_p(c) for every p|B and every k",
            "adjacent_gcd": "gcd(N_0,N_1)=c^2",
            "covering_bound": "0<minimum<B*y^2/2 for a nonzero pair with y!=0",
            "natural_degree_e_product": "minimum product=minimum^e and ratio unchanged",
        },
        "algebra_replay": {**replay, "sha256": replay_hash},
        "boundaries": boundary_audit(),
        "covering_witness": covering_witness(),
        "height": height_audit(),
        "scope": {
            "fixed_CRT_class": "d0 modulo B is frozen before representative balancing",
            "excluded": "an improvement from changing the integer representative or taking natural products/powers while using only the same fixed-class lattice and inherited component heights",
            "not_excluded": [
                "optimization across distinct simultaneous-nonresidue CRT classes",
                "an actual-family exponential phase-cancellation theorem",
                "a moving-prime bound on gcd(Cbar0,Cbar1)",
                "a different bounded-degree scalar with separately proved low height",
            ],
        },
        "capacity": {
            "raw_j1_capacity_per_6M": "1/36",
            "new_capacity_reduction": 0,
            "new_route1_rate": 0,
        },
    }
    payload = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    body["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "payload_sha256": result["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
