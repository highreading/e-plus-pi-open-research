#!/usr/bin/env python3
"""Deterministic certificate for Item 244's actual-family Abel reduction.

Starting from Item 241's character-harmonic coefficient state, this
checker projects the actual reciprocal-binomial P_nu onto the odd
denominators, performs exact summation by parts, and isolates one
canonically normalized residual bulk moment.  Bounded scans are labelled
finite; the identities themselves are proved algebraically in the report.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item244_j2_actual_character_bulk_certificate.json"
ITEM241_SHA256 = "0a9e3e665d272f6a2a016d1f394d4d95356c7a3b433846f593491c4819ec9baa"


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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


ITEM241_PATH = resolve("item241_j2_character_harmonic_collapse_certificate.py")
if sha256(ITEM241_PATH) != ITEM241_SHA256:
    raise RuntimeError("Item241 checker hash mismatch")
item241 = load("item244_item241", ITEM241_PATH)
item239 = item241.item239


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def trim(polynomial: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    result = list(polynomial)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def parity_factor(p: int, s: int, nu: int, r: int) -> tuple[int, ...]:
    """Exact projected factor, reduced modulo p."""
    a = 1 + 3 * nu
    q = 2 * s - nu
    delta = r % 2
    common = min(r, a)
    gap = abs(r - a)
    if gap < delta:
        parity_binomial: tuple[int, ...] = ()
    else:
        values = [
            math.comb(gap, 2 * j + delta) % p
            for j in range((gap - delta) // 2 + 1)
        ]
        if r >= a and delta:
            values = [(-value) % p for value in values]
        parity_binomial = tuple(values)
    if not parity_binomial:
        return ()
    result = item239.power_mod((1, -1), common, p)
    result = item239.convolution_mod(result, item239.power_mod((1, 1), q, p), p)
    result = item239.convolution_mod(result, parity_binomial, p)
    return trim(result)


def actual_coordinate(p: int, s: int, nu: int) -> dict[str, int]:
    r, polynomial = item239.p_polynomial(p, s, nu, p)
    delta = r % 2
    lower = (r + 1) // 2
    selected = trim(polynomial[delta::2])
    factored = parity_factor(p, s, nu, r)
    if selected != factored:
        raise AssertionError((p, s, nu, "actual parity factor", selected, factored))

    projection_zero = not selected
    classified_zero = nu == 0 and r == 1
    if projection_zero != classified_zero:
        raise AssertionError((p, s, nu, r, "zero-projection classification"))

    tables = item241.prefix_tables(p)
    character_prefix = tables["O"]
    chi = -1 if ((p - 1) // 2) % 2 else 1

    full_aggregate = 0
    base_aggregate = 0
    direct_character = 0
    for ell, coefficient in enumerate(polynomial):
        n = r + ell + 1
        if not (1 <= n < p):
            raise AssertionError((p, s, nu, ell, n, "denominator range"))
        kernel = item241.full_kernel_closed(p, n, tables)
        variable = 0
        if n % 2:
            u = (n - 1) // 2
            epsilon = -1 if u % 2 else 1
            variable = 90 * epsilon * character_prefix[u] * pow(n, -1, p) % p
        full_aggregate += coefficient * kernel
        base_aggregate += coefficient * (kernel - variable)
        direct_character += coefficient * variable
    full_aggregate %= p
    base_aggregate %= p
    direct_character %= p
    if full_aggregate != (base_aggregate + direct_character) % p:
        raise AssertionError((p, s, nu, "aggregate split"))

    if projection_zero:
        if direct_character:
            raise AssertionError((p, s, nu, "zero projection character"))
        return {
            "r": r,
            "lower_u": lower,
            "projected_degree": -1,
            "projection_zero": 1,
            "old_sine_endpoint": 0,
            "tail_q_0": 0,
            "bulk_b_0": 0,
            "direct_character": 0,
            "abel_character": 0,
            "base_aggregate": base_aggregate,
            "full_aggregate": full_aggregate,
        }

    degree = len(selected) - 1
    q_tail = [0] * (degree + 2)
    bulk = [0] * (degree + 1)
    weights = [0] * (degree + 1)
    for k in range(degree, -1, -1):
        u = lower + k
        n = 2 * u + 1
        if not (1 <= n < p):
            raise AssertionError((p, s, nu, k, n, "projected range"))
        weights[k] = selected[k] * pow(n, -1, p) % p
        q_tail[k] = (weights[k] - q_tail[k + 1]) % p
        if k < degree:
            bulk[k] = (bulk[k + 1] + q_tail[k + 1] * pow(n, -1, p)) % p

    # Check the unique terminally normalized tail and bulk states directly.
    for k in range(degree + 1):
        expected_q = sum(
            ((-1) ** (v - k)) * weights[v] for v in range(k, degree + 1)
        ) % p
        if q_tail[k] != expected_q:
            raise AssertionError((p, s, nu, k, "tail state"))
    expected_bulk = sum(
        q_tail[k + 1] * pow(2 * (lower + k) + 1, -1, p)
        for k in range(degree)
    ) % p
    if bulk[0] != expected_bulk:
        raise AssertionError((p, s, nu, "bulk state"))

    old_sine = sum(
        selected[k]
        * (-1 if (lower + k) % 2 else 1)
        * pow(2 * (lower + k) + 1, -1, p)
        for k in range(degree + 1)
    ) % p
    if q_tail[0] != ((-1) ** lower) * old_sine % p:
        raise AssertionError((p, s, nu, "tail/sine boundary"))

    # Relate the rational sign period to Item 219's old J endpoint weight.
    j_endpoint = 0
    for ell, coefficient in enumerate(polynomial):
        n = r + ell + 1
        _, j_weight, _ = item239.phase_weights(p, n)
        j_endpoint += coefficient * j_weight * pow(n, -1, p)
    j_endpoint %= p
    sine_from_j = -j_endpoint * pow((2 * chi) % p, -1, p) % p
    if old_sine != sine_from_j:
        raise AssertionError((p, s, nu, "old sine endpoint normalization"))

    abel_character = (
        90 * (character_prefix[lower] * old_sine - bulk[0])
    ) % p
    if direct_character != abel_character:
        raise AssertionError((p, s, nu, "Abel aggregate identity"))

    return {
        "r": r,
        "lower_u": lower,
        "projected_degree": degree,
        "projection_zero": 0,
        "old_sine_endpoint": old_sine,
        "tail_q_0": q_tail[0],
        "bulk_b_0": bulk[0],
        "direct_character": direct_character,
        "abel_character": abel_character,
        "base_aggregate": base_aggregate,
        "full_aggregate": full_aggregate,
    }


def verify_counterexamples() -> dict[str, Any]:
    zero_line = actual_coordinate(17, 2, 0)
    nonzero_bulk = actual_coordinate(17, 2, 1)
    first = actual_coordinate(19, 2, 0)
    second = actual_coordinate(19, 2, 1)
    if not zero_line["projection_zero"]:
        raise AssertionError("r=1, nu=0 line must have zero projection")
    if nonzero_bulk["bulk_b_0"] != 9 or nonzero_bulk["direct_character"] != 7:
        raise AssertionError((nonzero_bulk, "p=17 actual bulk witness"))
    ratio_first = first["bulk_b_0"] * pow(first["old_sine_endpoint"], -1, 19) % 19
    ratio_second = second["bulk_b_0"] * pow(second["old_sine_endpoint"], -1, 19) % 19
    if (ratio_first, ratio_second) != (5, 12):
        raise AssertionError((ratio_first, ratio_second, "p=19 ratio witness"))
    return {
        "automatic_zero_projection": {"p": 17, "s": 2, "nu": 0, **zero_line},
        "nonzero_bulk_actual_row": {"p": 17, "s": 2, "nu": 1, **nonzero_bulk},
        "not_common_scalar_multiple_of_old_sine": {
            "p": 19,
            "s": 2,
            "nu_0_bulk_over_sine": ratio_first,
            "nu_1_bulk_over_sine": ratio_second,
        },
    }


def finite_census(bound: int) -> dict[str, Any]:
    rows = 0
    coordinates = 0
    zero_projections = 0
    nonempty_bulk_zeros = 0
    nonempty_character_zeros = 0
    digest_rows: list[tuple[int, ...]] = []
    for p, s in item239.admissible_rows(bound):
        rows += 1
        for nu in (0, 1):
            coordinates += 1
            data = actual_coordinate(p, s, nu)
            zero_projections += data["projection_zero"]
            if not data["projection_zero"]:
                nonempty_bulk_zeros += data["bulk_b_0"] == 0
                nonempty_character_zeros += data["direct_character"] == 0
            digest_rows.append(
                (
                    p,
                    s,
                    nu,
                    data["r"],
                    data["lower_u"],
                    data["projected_degree"],
                    data["old_sine_endpoint"],
                    data["bulk_b_0"],
                    data["direct_character"],
                    data["base_aggregate"],
                    data["full_aggregate"],
                )
            )
    return {
        "status": "EXACT FINITE ONLY",
        "prime_max_inclusive": bound,
        "admissible_row_count": rows,
        "coordinate_count": coordinates,
        "zero_projection_count": zero_projections,
        "nonempty_bulk_zero_count": nonempty_bulk_zeros,
        "nonempty_character_zero_count": nonempty_character_zeros,
        "row_digest_sha256": row_digest(digest_rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=401)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.prime_max < 19:
        raise ValueError("prime-max must be at least 19")

    witnesses = verify_counterexamples()
    finite = finite_census(args.prime_max)
    result = {
        "schema": "item244-j2-actual-character-bulk-v1",
        "item": 244,
        "route": "Route 1A",
        "cell": "normalized common-log j=2 fixed cell, actual P_nu family, s>=2",
        "proved": {
            "actual_parity_projection": "if delta=r mod 2, L=ceil(r/2), a=1+3nu, q=2s-nu, b=min(r,a), and R=abs(r-a), then the odd-denominator coefficient polynomial is sigma*(1-t)^b*(1+t)^q*sum_j binom(R,2j+delta)t^j, with sigma=(-1)^delta for r>=a and sigma=1 for r<a",
            "zero_projection_classification": "the projection vanishes exactly for nu=0 and r=1; equivalently P_0 is even on the actual line p=6s+5",
            "old_endpoint": "S_old=sum d_k*(-1)^(L+k)/(2(L+k)+1) equals -1/(2chi) times the old Item219 J-endpoint period",
            "tail_recurrence": "Q_(D+1)=0 and Q_k=d_k/(2(L+k)+1)-Q_(k+1)",
            "bulk_recurrence": "B_D=0 and B_k=B_(k+1)+Q_(k+1)/(2(L+k)+1)",
            "actual_aggregate_identity": "K_nu=K_nu_base+90*O_L*S_old-90*B_0",
            "canonical_residual": "the terminal normalizations uniquely define one residual scalar B_0 after one exact Abel summation",
            "unit_audit": "all projected denominators are in 1,...,p-1 and hence are p-units",
        },
        "exact_counterexamples": witnesses,
        "finite_census": finite,
        "scoped_consequence": {
            "proved": "the Item241 variable character aggregate collapses to one old endpoint boundary term plus one canonically normalized scalar bulk moment",
            "not_proved": "B_0 is not proved independent of every larger known harmonic state, and no all-row telescoper or nonvanishing theorem is known",
            "simple_no_go": "the p=17 actual row has B_0=9 nonzero, and at p=19 the two coordinate ratios B_0/S_old are 5 and 12, so B_0 neither vanishes identically nor is a common coordinate-independent scalar multiple of S_old",
        },
        "status_ledger": {
            "PROVED": [
                "the exact actual-family parity projection and its zero classification",
                "the old-sine endpoint normalization",
                "the unique terminally normalized Q,B recurrence",
                "the aggregate identity K_nu=K_base+90 O_L S_old-90 B_0",
                "the two exact scoped counterexamples and full range/unit audit",
            ],
            "EXACT_FINITE": [
                "the bounded actual-row census through the stated prime bound",
            ],
            "OPEN": [
                "collapse B_0 to already-known aggregate states or prove that no such actual-family collapse exists",
                "derive an all-prime zero or nonzero classification for B_0",
                "classify simultaneous j=2 common-log zeros",
                "obtain any Route-1 rate or capacity reduction",
            ],
        },
        "global_interface": "the identity simplifies Item239's stronger p^3 carry only; it does not strengthen the ordinary p^2 common-log gate",
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "none",
        },
        "dependencies": {
            "item241_checker": ITEM241_PATH.name,
            "item241_checker_sha256": ITEM241_SHA256,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
