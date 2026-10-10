#!/usr/bin/env python3
"""Exact checks for Item 220's twisted de Rham fixed-cell reduction.

The all-phase arguments are in the companion report.  This checker verifies
the Euler primitive, endpoint formulas, minimal endpoint basis, bounded
contiguity/Bezout no-go ranks, and a finite actual-row replay.  It deliberately
contains no clock, host path, or external numerical backend in its output.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from decimal import Decimal, getcontext
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item220_twisted_derham_fixed_cells_certificate.json"
AUXILIARY_PRIME = 1_000_000_007

DEPENDENCIES = {
    "sources/item197_common_log_locus_report.md":
        "2241656ac9c47e81b5026449a97c15bed7d35290bf2b6a91cdfed4bb3fe3683c",
    "sources/item217_common_log_invariant_report.md":
        "89e8f8f7f9fabdafa8d9330171eb388e854df835c10ee50be4f4f5b43e028466",
    "scripts/item217_common_log_invariant_certificate.py":
        "b84a97d2d0d62ca950a7f7e8907baed7623879739ed78f04bbd8bc642e4c4d83",
}


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def load_item217():
    path = resolve("item217_common_log_invariant_certificate.py")
    spec = importlib.util.spec_from_file_location("item220_item217", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


item217 = load_item217()


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def phase_data(r: int, s: int, nu: int) -> tuple[int, int, int, int]:
    p_formal = 2 * r + 6 * s + 3
    q = 2 * s - nu
    degree = r + 1 + nu + 4 * s
    target = 2 * p_formal - 2 * s + nu - 1
    return p_formal, q, degree, target


def moving_polynomial(r: int, s: int, nu: int, modulus: int) -> list[int]:
    _, q, _, _ = phase_data(r, s, nu)
    left = item217.power_mod([1, -1], r, modulus)
    middle = item217.power_mod([1, 1], 1 + 3 * nu, modulus)
    right = item217.power_mod([1, 0, 1], q, modulus)
    return item217.convolution_mod(
        item217.convolution_mod(left, middle, modulus), right, modulus
    )


def endpoint_coordinates(
    r: int, s: int, nu: int, modulus: int
) -> tuple[int, int, int]:
    """Return (E,C,S) for the Euler resolvent V_nu modulo modulus."""
    _, _, degree, target = phase_data(r, s, nu)
    poly = moving_polynomial(r, s, nu, modulus)
    if len(poly) - 1 != degree:
        raise AssertionError((r, s, nu, len(poly) - 1, degree))
    endpoint_one = 0
    endpoint_even_i = 0
    endpoint_odd_i = 0
    for k, coefficient in enumerate(poly):
        denominator = (target - k) % modulus
        if not denominator:
            raise AssertionError((r, s, nu, modulus, k, target, "resonance"))
        term = coefficient * pow(denominator, -1, modulus) % modulus
        endpoint_one = (endpoint_one + term) % modulus
        if k & 1:
            sign = -1 if ((k - 1) // 2) & 1 else 1
            endpoint_odd_i = (endpoint_odd_i + sign * term) % modulus
        else:
            sign = -1 if (k // 2) & 1 else 1
            endpoint_even_i = (endpoint_even_i + sign * term) % modulus
    return endpoint_one, endpoint_even_i, endpoint_odd_i


def primitive_functionals(
    cell: int, r: int, s: int, modulus: int
) -> tuple[int, int]:
    epsilon = -1 if (r + s + 1) & 1 else 1
    e0, c0, t0 = endpoint_coordinates(r, s, 0, modulus)
    e1, c1, t1 = endpoint_coordinates(r, s, 1, modulus)
    if cell == 1:
        return (c0 - 2 * epsilon * t0) % modulus, (2 * c1 + epsilon * t1) % modulus
    if cell == 2:
        return (
            20 * c0 - 2 * epsilon * t0 - 9 * e0
        ) % modulus, (
            2 * epsilon * c1 + 20 * t1 - 9 * e1
        ) % modulus
    raise ValueError(cell)


def raw_endpoint_functionals(
    cell: int, r: int, s: int, modulus: int
) -> tuple[int, int]:
    """The H_(j,nu) values before removing their harmless phase scalars."""
    delta = -1 if s & 1 else 1
    epsilon = -1 if (r + s + 1) & 1 else 1
    e0, c0, t0 = endpoint_coordinates(r, s, 0, modulus)
    e1, c1, t1 = endpoint_coordinates(r, s, 1, modulus)
    if cell == 1:
        return (
            2 * delta * (epsilon * c0 - 2 * t0) % modulus,
            2 * delta * (2 * c1 + epsilon * t1) % modulus,
        )
    return (
        (-9 * e0 + 2 * delta * (10 * epsilon * c0 - t0)) % modulus,
        (-9 * e1 + 2 * delta * (c1 + 10 * epsilon * t1)) % modulus,
    )


def euler_primitive_check(limit: int = 10) -> dict:
    modulus = AUXILIARY_PRIME
    rows = []
    for r in range(1, limit + 1):
        for s in range(1, limit + 1):
            for nu in (0, 1):
                _, _, degree, target = phase_data(r, s, nu)
                poly = moving_polynomial(r, s, nu, modulus)
                resolvent = [
                    coefficient * pow((target - k) % modulus, -1, modulus) % modulus
                    for k, coefficient in enumerate(poly)
                ]
                # (N-z d/dz)V=P.
                recovered = [
                    (target - k) * coefficient % modulus
                    for k, coefficient in enumerate(resolvent)
                ]
                if recovered != poly:
                    raise AssertionError((r, s, nu))
                p_formal, _, _, _ = phase_data(r, s, nu)
                if target - p_formal != degree + r + 1:
                    raise AssertionError((r, s, nu, "nonresonance identity"))
                rows.append((r, s, nu, degree, target))
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "formal_r_s_max": limit,
        "rows": len(rows),
        "identity": "(N_nu-z*d/dz)V_nu=P_nu",
        "nonresonance": "N_nu-p=deg(P_nu)+r+1>deg(P_nu)",
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
    }


def rank_mod(matrix: list[list[int]], modulus: int) -> int:
    matrix = [row[:] for row in matrix]
    rows = len(matrix)
    columns = len(matrix[0])
    rank = 0
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, rows) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], modulus - 2, modulus)
        matrix[rank] = [value * inverse % modulus for value in matrix[rank]]
        for index in range(rank + 1, rows):
            factor = matrix[index][column]
            if factor:
                matrix[index] = [
                    (left - factor * right) % modulus
                    for left, right in zip(matrix[index], matrix[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def monomials(total_degree: int) -> list[tuple[int, int]]:
    return [
        (a, b)
        for a in range(total_degree + 1)
        for b in range(total_degree + 1 - a)
    ]


def denominator_audit(
    phase_pairs: list[tuple[int, int]], modulus: int
) -> dict:
    """Inspect every Euler-resolvent denominator used by a rank sample."""
    count = 0
    minimum = None
    maximum = None
    zero_modulus_count = 0
    for r, s in phase_pairs:
        for nu in (0, 1):
            _, _, degree, target = phase_data(r, s, nu)
            for k in range(degree + 1):
                denominator = target - k
                count += 1
                minimum = denominator if minimum is None else min(minimum, denominator)
                maximum = denominator if maximum is None else max(maximum, denominator)
                zero_modulus_count += denominator % modulus == 0
    if zero_modulus_count:
        raise AssertionError((modulus, zero_modulus_count, "rank denominator"))
    return {
        "division_count": count,
        "integer_denominator_min": minimum,
        "integer_denominator_max": maximum,
        "zero_mod_auxiliary_modulus": zero_modulus_count,
        "all_reductions_defined": True,
    }


def bounded_contiguity_no_go(total_degree: int = 8) -> dict:
    modulus = AUXILIARY_PRIME
    mons = monomials(total_degree)
    rows = []
    phase_pairs = [(r, s) for r in range(1, 19) for s in range(1, 19)]
    for r, s in phase_pairs:
        values = endpoint_coordinates(r, s, 0, modulus) + endpoint_coordinates(
            r, s, 1, modulus
        )
        rows.append([
            value * pow(r, a, modulus) * pow(s, b, modulus) % modulus
            for value in values
            for a, b in mons
        ])
    columns = 6 * len(mons)
    rank = rank_mod(rows, modulus)
    if (len(rows), columns, rank) != (324, 270, 270):
        raise AssertionError((len(rows), columns, rank))
    return {
        "ansatz": (
            "sum over the six E/C/S endpoint coordinates of a polynomial "
            "in (r,s) of total degree <=8"
        ),
        "auxiliary_modulus": modulus,
        "sample_grid": "1<=r,s<=18",
        "rows": len(rows),
        "columns": columns,
        "rank": rank,
        "nullity_over_Q": 0,
        "denominator_audit": denominator_audit(phase_pairs, modulus),
        "one_good_prime_argument": (
            "a rational identity gives, after clearing coefficient denominators, "
            "a nonzero primitive integer null vector; because every sampled entry "
            "denominator is invertible modulo the auxiliary prime, reduction gives "
            "a nonzero modular null vector, contradicting full column rank"
        ),
        "scope": (
            "rules out a universal linear contiguity covector in this bounded "
            "ansatz; it does not rule out nonlinear, higher-degree, or prime-only identities"
        ),
    }


def bounded_affine_bezout_no_go(total_degree: int = 8) -> dict:
    modulus = AUXILIARY_PRIME
    mons = monomials(total_degree)
    results = {}
    for cell in (1, 2):
        required_r_parity = 0 if cell == 1 else 1
        for s_parity in (0, 1):
            rows = []
            phase_pairs = []
            for r in range(1, 34):
                if r % 2 != required_r_parity:
                    continue
                for s in range(1, 34):
                    if s % 2 != s_parity:
                        continue
                    phase_pairs.append((r, s))
                    h0, h1 = primitive_functionals(cell, r, s, modulus)
                    rows.append([
                        value * pow(r, a, modulus) * pow(s, b, modulus) % modulus
                        for value in (h0, h1, 1)
                        for a, b in mons
                    ])
            columns = 3 * len(mons)
            rank = rank_mod(rows, modulus)
            if rank != columns:
                raise AssertionError((cell, s_parity, len(rows), columns, rank))
            results[f"j{cell}_s_parity_{s_parity}"] = {
                "rows": len(rows),
                "columns": columns,
                "rank": rank,
                "nullity_over_Q": 0,
                "denominator_audit": denominator_audit(phase_pairs, modulus),
            }
    return {
        "ansatz": "A(r,s)H_0+B(r,s)H_1+C(r,s)=0 with total degrees <=8",
        "auxiliary_modulus": modulus,
        "phase_grid": "1<=r,s<=33, split by the actual r parity and by s parity",
        "blocks": results,
        "one_good_prime_argument": (
            "on each fixed parity block epsilon is constant; clearing rational "
            "coefficient denominators would produce a primitive integer null vector, "
            "but all endpoint denominators are units modulo the auxiliary prime and "
            "the reduced matrix has full column rank"
        ),
        "scope": (
            "rules out a bounded-degree universal affine Bezout boundary on each "
            "parity component; it does not exclude a higher-degree or arithmetic boundary"
        ),
    }


def minimal_basis_check() -> dict:
    # Columns are the endpoint triples of V=1,z,z^2:
    # (E,C,S)=(1,1,0),(1,0,1),(1,-1,0).
    matrix = [[1, 1, 0], [1, 0, 1], [1, -1, 0]]
    determinant = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    if determinant != 2:
        raise AssertionError(determinant)
    return {
        "common_endpoint_basis": ["E=V(1)", "C=even part of V(i)", "S=odd part of V(i)/i"],
        "test_polynomials": ["1", "z", "z^2"],
        "evaluation_matrix_determinant": determinant,
        "conclusion": "three endpoint coordinates are minimal for a universal odd-prime reduction",
    }


def finite_actual_replay(prime_max: int) -> dict:
    counts = {
        1: {"rows": 0, "H0_zero": 0, "H1_zero": 0, "paired_zero": 0},
        2: {"rows": 0, "H0_zero": 0, "H1_zero": 0, "paired_zero": 0},
    }
    endpoint_zero_counts = {"E": 0, "C": 0, "S": 0}
    rows = []
    for p in item217.primes_upto(prime_max):
        if p <= 7:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            numerator = p - 6 * s - 3
            if numerator < 0 or numerator % 2:
                raise AssertionError((p, s, numerator))
            r = numerator // 2
            if r < 1:
                raise AssertionError((p, s, r, "admissible r must be positive"))
            cell = 1 if r % 2 == 0 else 2
            h0, h1 = primitive_functionals(cell, r, s, p)
            raw0, raw1 = raw_endpoint_functionals(cell, r, s, p)
            direct = []
            for nu in (0, 1):
                x, y, y_high = item217.moments(p, s, nu)
                direct.append(
                    (2 * y_high - y) % p
                    if cell == 1
                    else (9 * x - 10 * y + y_high) % p
                )
            if (raw0, raw1) != tuple(direct):
                raise AssertionError((p, s, r, cell, raw0, raw1, direct))
            # The raw and primitive pairs differ only by nonzero phase scalars.
            if (h0 == 0, h1 == 0) != (raw0 == 0, raw1 == 0):
                raise AssertionError((p, s, r, cell, h0, h1, raw0, raw1))
            q0, q1 = item217.quotient_digits(p, cell, s)
            predicted_q = (
                (6 * raw0 % p, 6 * raw1 % p)
                if cell == 1
                else (-35 * raw0 % p, -35 * raw1 % p)
            )
            if (q0, q1) != predicted_q:
                raise AssertionError((p, s, r, cell, q0, q1, predicted_q))
            counts[cell]["rows"] += 1
            counts[cell]["H0_zero"] += h0 == 0
            counts[cell]["H1_zero"] += h1 == 0
            counts[cell]["paired_zero"] += h0 == h1 == 0
            for nu in (0, 1):
                e, c, t = endpoint_coordinates(r, s, nu, p)
                endpoint_zero_counts["E"] += e == 0
                endpoint_zero_counts["C"] += c == 0
                endpoint_zero_counts["S"] += t == 0
            rows.append((p, s, r, cell, h0, h1, q0, q1))
    if counts[1]["paired_zero"] or counts[2]["paired_zero"]:
        raise AssertionError(counts)
    stream = json.dumps(rows, separators=(",", ":")).encode("ascii")
    return {
        "classification": "EXACT_FINITE_ONLY",
        "prime_max": prime_max,
        "j1": counts[1],
        "j2": counts[2],
        "endpoint_coordinate_zero_counts": endpoint_zero_counts,
        "row_stream_sha256": hashlib.sha256(stream).hexdigest(),
        "scope_warning": "bounded nonoccurrence is not an all-prime or rate theorem",
    }


def rate_ledger() -> dict:
    getcontext().prec = 50
    raw_per_m = Decimal("0.3370475079987658")
    gap = Decimal("0.01963298366943179388")
    remaining_per_m = raw_per_m - Decimal(1) / Decimal(6) - Decimal(2) / Decimal(35)
    remaining_per_6m = remaining_per_m / Decimal(6)
    return {
        "raw_per_m_displayed_input": str(raw_per_m),
        "raw_per_m_source": "displayed numerical ceiling inherited from Item 217",
        "decimal_status": (
            "conditional bookkeeping at the displayed precision; the cell masses "
            "1/6 and 2/35 are the exact proof inputs"
        ),
        "j1_mass_per_m": "1/6",
        "j2_mass_per_m": "2/35",
        "conditional_remaining_per_m": str(remaining_per_m),
        "conditional_remaining_per_6m": str(remaining_per_6m),
        "gap_per_6m": str(gap),
        "conditional_margin_below_gap": str(gap - remaining_per_6m),
        "all_prime_paired_cell_exclusion": "OPEN",
        "new_unconditional_linear_log_rate": 0,
        "new_divisibility_exponent": 0,
    }


def certificate(prime_max: int) -> dict:
    return {
        "item": 220,
        "classification": {
            "PROVED": [
                "p=2r+6s+3 with r>=1; the j=1 rows are exactly even r and j=2 rows exactly odd r",
                "both logarithmic moment forms are exact under the nonresonant Euler primitive",
                "the j=1 pair reduces to two C/S endpoint functionals",
                "the j=2 pair reduces to two E/C/S endpoint functionals",
                "the three-coordinate common endpoint basis is minimal in the universal odd-prime reduction",
                "no degree-at-most-eight universal linear contiguity or affine Bezout identity exists in the certified ansatz",
            ],
            "OPEN": [
                "all-prime nonvanishing of either paired fixed-cell functional",
                "a higher-degree, nonlinear, or genuinely arithmetic endpoint boundary",
                "any positive linear-rate or radical saving",
            ],
            "EXACT_FINITE_ONLY": [f"actual-row paired nonoccurrence through p<={prime_max}"],
        },
        "phase_parameterization": {
            "prime": "p=2r+6s+3",
            "r_minimum": 1,
            "j1_admissibility": "r even",
            "j2_admissibility": "r odd",
            "epsilon": "(-1)^((p-1)/2)=(-1)^(r+s+1)",
        },
        "exact_differential_reduction": {
            "P_nu": "(1-z)^r(1+z)^(1+3nu)(1+z^2)^(2s-nu)",
            "N_nu": "2p-2s+nu-1",
            "V_nu": "sum_k [z^k]P_nu*z^k/(N_nu-k)",
            "euler_identity": "(N_nu-z*d/dz)V_nu=P_nu",
            "exact_form": "P_nu*z^(-N_nu-1)dz=-d(z^(-N_nu)V_nu)",
            "j1_kernel": "L_1=(2-z^p)B_p",
            "j2_kernel": "L_2=9z^p A_p+(1-10z^p)B_p",
            "moment_reduction": "H_(j,nu)=Res_0 L'_j z^(-N_nu)V_nu dz",
            "finite_log_coordinate_remaining": "NONE_IN_THE_INTERIOR_NONRESONANT_REDUCTION",
            "remaining_coordinate": "the incomplete Euler-resolvent endpoint vector (E_nu,C_nu,S_nu)",
            "regression": euler_primitive_check(),
        },
        "endpoint_formulas": {
            "definitions": {
                "E_nu": "V_nu(1)",
                "C_nu": "sum_h (-1)^h [z^(2h)]P_nu/(N_nu-2h)",
                "S_nu": "sum_h (-1)^h [z^(2h+1)]P_nu/(N_nu-2h-1)",
            },
            "j1_actual_row": ["C_0-2epsilon*S_0", "2C_1+epsilon*S_1"],
            "j2_actual_row": [
                "20C_0-2epsilon*S_0-9E_0",
                "2epsilon*C_1+20S_1-9E_1",
            ],
            "cross_cell_coupling": {
                "nu0_covectors_in_E_C_S": [
                    [0, 1, "-2epsilon"],
                    [-9, 20, "-2epsilon"],
                ],
                "nu1_covectors_in_E_C_S": [
                    [0, 2, "epsilon"],
                    [-9, "2epsilon", 20],
                ],
                "nonzero_E_C_minors": [9, 18],
                "scoped_obstruction": (
                    "the two formal cell covectors are independent for p>3, but the "
                    "actual j1 and j2 rows lie on disjoint r-parity components, so "
                    "their minors cannot be used as a same-phase Bezout contradiction"
                ),
            },
            "minimality": minimal_basis_check(),
        },
        "bounded_ansatz_no_go": {
            "linear_contiguity": bounded_contiguity_no_go(),
            "affine_bezout": bounded_affine_bezout_no_go(),
            "interpretation": (
                "inhomogeneous contiguity leaves genuine endpoint periods; general "
                "holonomicity alone supplies no nonvanishing boundary"
            ),
        },
        "finite_actual_replay": finite_actual_replay(prime_max),
        "rate_ledger": rate_ledger(),
        "dependency_sha256": DEPENDENCIES,
        "runtime": {"external_numeric_backend": None},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-max", type=int, default=251)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    result = certificate(args.prime_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "output": str(args.output),
        "prime_max": args.prime_max,
        "j1_rows": result["finite_actual_replay"]["j1"]["rows"],
        "j2_rows": result["finite_actual_replay"]["j2"]["rows"],
        "paired_zeros": (
            result["finite_actual_replay"]["j1"]["paired_zero"]
            + result["finite_actual_replay"]["j2"]["paired_zero"]
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
