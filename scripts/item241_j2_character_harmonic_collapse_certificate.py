#!/usr/bin/env python3
"""Deterministic certificate for Item 241's j=2 harmonic collapse.

The checker eliminates the A^2, B^2, and AB convolution tables from the
Item 239 corrected kernel.  It verifies the resulting all-index harmonic
formulas, the simplified full kernel, and two exact seven-coordinate
parity-state updates.  Bounded replay data are explicitly finite only.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item241_j2_character_harmonic_collapse_certificate.json"
ITEM239_SHA256 = "3715e70670befb3dff0f16e6d7056750acd230b771a28b5ced47bae53ea94dc5"


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


ITEM239_PATH = resolve("item239_j2_actual_witt_bridge_certificate.py")
if sha256(ITEM239_PATH) != ITEM239_SHA256:
    raise RuntimeError("Item239 checker hash mismatch")
item239 = load("item241_item239", ITEM239_PATH)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def coefficient(polynomial: tuple[int, ...], degree: int) -> int:
    return polynomial[degree] if 0 <= degree < len(polynomial) else 0


def prefix_tables(p: int) -> dict[str, tuple[int, ...]]:
    """Return H_N, A_N=sum(-1)^j/j, and O_N=sum(-1)^j/(2j+1)."""
    h = (p - 1) // 2
    harmonic = item239.harmonic_table(p)
    alternating = [0] * p
    for j in range(1, p):
        alternating[j] = (
            alternating[j - 1] + (-1 if j % 2 else 1) * pow(j, -1, p)
        ) % p
        expected = (harmonic[j // 2] - harmonic[j]) % p
        if alternating[j] != expected:
            raise AssertionError((p, j, "alternating/ordinary harmonic identity"))
    character = [0] * (h + 1)
    for j in range(h):
        character[j + 1] = (
            character[j] + (-1 if j % 2 else 1) * pow(2 * j + 1, -1, p)
        ) % p
    return {
        "H": harmonic,
        "A": tuple(alternating),
        "O": tuple(character),
    }


def square_closed(p: int, n: int, tables: dict[str, tuple[int, ...]]) -> tuple[int, int]:
    """Closed AA and BB contributions to K^(2)."""
    harmonic = tables["H"]
    inverse_n = pow(n, -1, p)
    aa = (-54 * harmonic[n - 1] * inverse_n - 18 * inverse_n * inverse_n) % p
    if n % 2 == 0:
        u = n // 2
        epsilon = -1 if u % 2 else 1
        c_weight = 2 * epsilon
        inverse_u = pow(u, -1, p)
        bb = c_weight * (
            -30 * harmonic[u - 1] * inverse_u + 6 * inverse_u * inverse_u
        )
    else:
        half = (p + n) // 2
        j_weight = 2 * (-1 if half % 2 else 1)
        inverse_half = pow(half, -1, p)
        bb = j_weight * (
            3 * harmonic[half - 1] * inverse_half
            - 3 * inverse_half * inverse_half
        )
    return aa, bb % p


def mixed_sections_closed(
    p: int, n: int, tables: dict[str, tuple[int, ...]]
) -> tuple[int, int, int]:
    """Closed c(n), c(p+n), c(2p+n) for c=[z^t]A_p B_p."""
    h = (p - 1) // 2
    alternating = tables["A"]
    character = tables["O"]
    inverse_n = pow(n, -1, p)
    if n % 2 == 0:
        u = n // 2
        epsilon = -1 if u % 2 else 1
        c0 = (1 + epsilon) * alternating[u - 1]
        c1 = (
            alternating[h + u]
            - alternating[u]
            + 2 * ((-1) ** (h + u)) * character[h]
        )
        c2 = (
            alternating[p - 1]
            - alternating[h + u]
            - epsilon * (alternating[h] - alternating[u])
        )
    else:
        u = (n - 1) // 2
        epsilon = -1 if u % 2 else 1
        c0 = alternating[u] + 2 * epsilon * character[u]
        c1 = (
            alternating[h + u]
            - alternating[u]
            + ((-1) ** (h + u + 1)) * alternating[h]
        )
        c2 = (
            alternating[p - 1]
            - alternating[h + u + 1]
            - 2 * epsilon * (character[h] - character[u + 1])
        )
    return tuple(value * inverse_n % p for value in (c0, c1, c2))


def full_kernel_closed(p: int, n: int, tables: dict[str, tuple[int, ...]]) -> int:
    """Parity-simplified formula for K_p^(1)(n)+K_p^(2)(n)."""
    h = (p - 1) // 2
    chi = -1 if h % 2 else 1
    harmonic = tables["H"]
    alternating = tables["A"]
    character = tables["O"]
    inverse_n = pow(n, -1, p)
    if n % 2 == 0:
        u = n // 2
        epsilon = -1 if u % 2 else 1
        bracket = (
            -63 * harmonic[2 * u - 1]
            - 100 * epsilon * harmonic[u - 1]
            - 9 * alternating[p - 1]
            - 7 * alternating[h + u]
            + 9 * epsilon * alternating[h]
            - 32 * chi * epsilon * character[h]
            + 70 * alternating[u - 1]
            + 45 * epsilon * alternating[u - 1]
        )
        pole_two = 80 * epsilon - 36
    else:
        u = (n - 1) // 2
        epsilon = -1 if u % 2 else 1
        bracket = (
            -63 * harmonic[2 * u]
            - 10 * chi * epsilon * harmonic[h + u]
            - 9 * alternating[p - 1]
            - 7 * alternating[h + u]
            + 70 * alternating[u]
            + 16 * chi * epsilon * alternating[h]
            + 18 * epsilon * character[h]
            + 90 * epsilon * character[u]
        )
        pole_two = 8 * chi * epsilon - 36
    return (bracket * inverse_n + pole_two * inverse_n * inverse_n) % p


def raw_components(p: int, n: int) -> tuple[int, int, int, int]:
    data = item239.kernel_data(p)
    aa = (
        9 * coefficient(data["AA"], p + n)
        - 18 * coefficient(data["AA"], n)
    ) % p
    bb = (
        -3 * coefficient(data["BB"], 3 * p + n)
        + 6 * coefficient(data["BB"], 2 * p + n)
        + 6 * coefficient(data["BB"], p + n)
        - 36 * coefficient(data["BB"], n)
    ) % p
    ab = (
        -9 * coefficient(data["AB"], 2 * p + n)
        - 16 * coefficient(data["AB"], p + n)
        + 54 * coefficient(data["AB"], n)
    ) % p
    return aa, bb, ab, data["total"][n]


def verify_even_state(p: int, tables: dict[str, tuple[int, ...]]) -> int:
    """Verify the seven-coordinate even state for u=1,...,(p-1)/2."""
    h = (p - 1) // 2
    chi = -1 if h % 2 else 1
    harmonic = tables["H"]
    alternating = tables["A"]
    character = tables["O"]
    checks = 0
    for u in range(1, h + 1):
        epsilon = -1 if u % 2 else 1
        state = (
            1,
            epsilon,
            harmonic[2 * u - 1],
            epsilon * harmonic[u - 1] % p,
            alternating[h + u],
            alternating[u - 1],
            epsilon * alternating[u - 1] % p,
        )
        one, e, h2, eh, ahu, au, eau = state
        n = 2 * u
        inverse_n = pow(n, -1, p)
        output = (
            (
                -63 * h2
                - 100 * eh
                - 9 * alternating[p - 1]
                - 7 * ahu
                + 9 * e * alternating[h]
                - 32 * chi * e * character[h]
                + 70 * au
                + 45 * eau
            )
            * inverse_n
            + (80 * e - 36) * inverse_n * inverse_n
        ) % p
        if output != full_kernel_closed(p, n, tables):
            raise AssertionError((p, u, "even output map"))
        if u < h:
            inverse_u = pow(u, -1, p)
            predicted = (
                one,
                -e % p,
                (h2 + pow(2 * u, -1, p) + pow(2 * u + 1, -1, p)) % p,
                (-eh - e * inverse_u) % p,
                (ahu - chi * e * pow(h + u + 1, -1, p)) % p,
                (au + e * inverse_u) % p,
                (-eau - inverse_u) % p,
            )
            next_e = -1 if (u + 1) % 2 else 1
            actual = (
                1,
                next_e % p,
                harmonic[2 * u + 1],
                next_e * harmonic[u] % p,
                alternating[h + u + 1],
                alternating[u],
                next_e * alternating[u] % p,
            )
            if predicted != actual:
                raise AssertionError((p, u, "even state transition", predicted, actual))
            checks += 1
    return checks


def verify_odd_state(p: int, tables: dict[str, tuple[int, ...]]) -> tuple[int, int]:
    """Verify the seven-coordinate odd state and the forced O-state update."""
    h = (p - 1) // 2
    chi = -1 if h % 2 else 1
    harmonic = tables["H"]
    alternating = tables["A"]
    character = tables["O"]
    transition_checks = 0
    forced_checks = 0
    for u in range(h):
        epsilon = -1 if u % 2 else 1
        state = (
            1,
            epsilon,
            harmonic[2 * u],
            epsilon * harmonic[h + u] % p,
            alternating[h + u],
            alternating[u],
            epsilon * character[u] % p,
        )
        one, e, h2, eh, ahu, au, eo = state
        n = 2 * u + 1
        inverse_n = pow(n, -1, p)
        output = (
            (
                -63 * h2
                - 10 * chi * eh
                - 9 * alternating[p - 1]
                - 7 * ahu
                + 70 * au
                + 16 * chi * e * alternating[h]
                + 18 * e * character[h]
                + 90 * eo
            )
            * inverse_n
            + (8 * chi * e - 36) * inverse_n * inverse_n
        ) % p
        if output != full_kernel_closed(p, n, tables):
            raise AssertionError((p, u, "odd output map"))
        if u < h - 1:
            predicted = (
                one,
                -e % p,
                (h2 + pow(2 * u + 1, -1, p) + pow(2 * u + 2, -1, p)) % p,
                (-eh - e * pow(h + u + 1, -1, p)) % p,
                (ahu - chi * e * pow(h + u + 1, -1, p)) % p,
                (au - e * pow(u + 1, -1, p)) % p,
                (-eo - pow(2 * u + 1, -1, p)) % p,
            )
            next_e = -1 if (u + 1) % 2 else 1
            actual = (
                1,
                next_e % p,
                harmonic[2 * u + 2],
                next_e * harmonic[h + u + 1] % p,
                alternating[h + u + 1],
                alternating[u + 1],
                next_e * character[u + 1] % p,
            )
            if predicted != actual:
                raise AssertionError((p, u, "odd state transition", predicted, actual))
            z_value = 90 * eo * inverse_n % p
            next_n = n + 2
            next_z = (
                90 * actual[-1] * pow(next_n, -1, p)
            ) % p
            predicted_z = (
                -n * pow(next_n, -1, p) * z_value
                - 90 * pow(n * next_n % p, -1, p)
            ) % p
            if next_z != predicted_z:
                raise AssertionError((p, u, "forced character state"))
            transition_checks += 1
            forced_checks += 1
    return transition_checks, forced_checks


def verify_all(bound: int) -> dict[str, Any]:
    rows: list[tuple[int, ...]] = []
    prime_count = 0
    even_state_checks = 0
    odd_state_checks = 0
    forced_state_checks = 0
    character_nonzero_coefficients = 0
    for p in item239.item219.primes_upto(bound):
        if p < 17:
            continue
        prime_count += 1
        if 90 % p == 0:
            raise AssertionError((p, "90 must be a unit"))
        tables = prefix_tables(p)
        data = item239.kernel_data(p)
        for n in range(1, p):
            aa_raw, bb_raw, ab_raw, total_raw = raw_components(p, n)
            aa_closed, bb_closed = square_closed(p, n, tables)
            c0, c1, c2 = mixed_sections_closed(p, n, tables)
            ab_closed = (-9 * c2 - 16 * c1 + 54 * c0) % p
            total_closed = full_kernel_closed(p, n, tables)
            if aa_raw != aa_closed:
                raise AssertionError((p, n, "AA collapse"))
            if bb_raw != bb_closed:
                raise AssertionError((p, n, "BB collapse"))
            if (c0, c1, c2) != (
                coefficient(data["AB"], n),
                coefficient(data["AB"], p + n),
                coefficient(data["AB"], 2 * p + n),
            ):
                raise AssertionError((p, n, "AB section collapse"))
            if ab_raw != ab_closed or total_raw != total_closed:
                raise AssertionError((p, n, "full kernel collapse"))
            if n % 2:
                character_nonzero_coefficients += 1
            rows.append(
                (
                    p,
                    n,
                    aa_closed,
                    bb_closed,
                    ab_closed,
                    total_closed,
                    c0,
                    c1,
                    c2,
                )
            )
        even_state_checks += verify_even_state(p, tables)
        odd_checks, forced_checks = verify_odd_state(p, tables)
        odd_state_checks += odd_checks
        forced_state_checks += forced_checks
    return {
        "status": "EXACT FINITE REPLAY OF ALL-ROW IDENTITIES",
        "prime_max_inclusive": bound,
        "prime_count": prime_count,
        "prime_denominator_pair_count": len(rows),
        "even_state_transition_checks": even_state_checks,
        "odd_state_transition_checks": odd_state_checks,
        "forced_character_state_checks": forced_state_checks,
        "odd_indices_with_unit_90_coefficient": character_nonzero_coefficients,
        "row_digest_sha256": row_digest(rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=401)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.prime_max < 17:
        raise ValueError("prime-max must be at least 17")

    replay = verify_all(args.prime_max)
    result = {
        "schema": "item241-j2-character-harmonic-collapse-v1",
        "item": 241,
        "route": "Route 1A",
        "cell": "normalized common-log j=2 fixed cell, p>=17, s>=2",
        "proved": {
            "alternating_prefix": "A_N=sum_{j=1}^N (-1)^j/j=H_floor(N/2)-H_N modulo p",
            "AA_collapse": "9a(p+n)-18a(n)=-54H_(n-1)/n-18/n^2",
            "BB_even_collapse": "for n=2u: C(n)*(-30H_(u-1)/u+6/u^2)",
            "BB_odd_collapse": "for odd n and h_n=(p+n)/2: J(n)*(3H_(h_n-1)/h_n-3/h_n^2)",
            "AB_collapse": "the three needed AB sections are the explicit A_N,O_N formulas in the report; no convolution table remains",
            "full_kernel": "K_p^(1)+K_p^(2) is the explicit parity formula and output map of two seven-coordinate first-order states",
            "character_state": "R_u=(-1)^u O_u obeys R_(u+1)=-R_u-1/(2u+1); Z_u=90R_u/(2u+1) obeys Z_(u+1)=-(2u+1)/(2u+3) Z_u-90/((2u+1)(2u+3))",
            "unit_audit": "for p>=17, every displayed in-range denominator and 90 are p-units",
        },
        "scoped_consequence": {
            "proved": "the depth-two convolution coordinate can be replaced by a finite affine coefficient state with one explicit mod-4 character prefix",
            "not_proved": "the coefficient-state update is not a boundary-only terminal recurrence for sums against P_nu; restricted-row cancellation or a telescoper may still exist",
            "bulk_forcing": "the character state has a nonzero inhomogeneous source at every interior odd index, with unit output coefficient 90",
        },
        "global_interface": "K_nu enters only the stronger Item239 p^3 condition; Item241 does not strengthen the ordinary p^2 common-log gate and books no fixed-cell capacity",
        "finite_replay": replay,
        "status_ledger": {
            "PROVED": [
                "all-index harmonic collapse of AA, BB, and all three AB sections",
                "the simplified full corrected kernel for both parities",
                "two exact seven-coordinate rational first-order coefficient states",
                "the inhomogeneous mod-4 character-prefix update and complete range/unit audit",
            ],
            "EXACT_FINITE": [
                "the bounded exhaustive replay of the all-row formulas and state transitions",
            ],
            "OPEN": [
                "turn the coefficient state into a boundary-only terminal recurrence after summation against P_nu",
                "exclude aggregate cancellation of the forced bulk coordinate on the restricted row family",
                "classify simultaneous j=2 common-log zeros over all primes",
                "obtain any Route-1 rate or capacity reduction",
            ],
        },
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
            "conclusion_about_e_plus_pi": "none",
        },
        "dependencies": {
            "item239_checker": ITEM239_PATH.name,
            "item239_checker_sha256": ITEM239_SHA256,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
