#!/usr/bin/env python3
"""Deterministic certificate for Item 221's j=2 twisted-cohomology step.

The companion report supplies the proofs and scope.  This checker uses
only the Python standard library plus the frozen Item 219 checker beside
it.  It verifies the rational contiguity identity symbolically, expands
the exact cohomology minor, and replays the finite period identities.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item221_j2_twisted_cohomology_certificate.json"


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


ITEM219_PATH = resolve("item219_common_log_j2_certificate.py")
item219 = load("item221_item219", ITEM219_PATH)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_digest(rows: list[tuple[int, ...]]) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in rows).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


# Bivariate polynomials in (z,s), represented by (z_degree,s_degree)->Fraction.
BP = dict[tuple[int, int], Fraction]


def bp_clean(value: BP) -> BP:
    return {key: coefficient for key, coefficient in value.items() if coefficient}


def bp_const(value: int | Fraction) -> BP:
    coefficient = Fraction(value)
    return {} if not coefficient else {(0, 0): coefficient}


def bp_add(left: BP, right: BP) -> BP:
    answer = dict(left)
    for key, coefficient in right.items():
        answer[key] = answer.get(key, Fraction(0)) + coefficient
    return bp_clean(answer)


def bp_neg(value: BP) -> BP:
    return {key: -coefficient for key, coefficient in value.items()}


def bp_sub(left: BP, right: BP) -> BP:
    return bp_add(left, bp_neg(right))


def bp_mul(left: BP, right: BP) -> BP:
    answer: BP = {}
    for (zi, si), x in left.items():
        for (zj, sj), y in right.items():
            key = (zi + zj, si + sj)
            answer[key] = answer.get(key, Fraction(0)) + x * y
    return bp_clean(answer)


def bp_scale(value: BP, scalar: int | Fraction) -> BP:
    return bp_mul(value, bp_const(scalar))


def bp_pow(value: BP, exponent: int) -> BP:
    answer = bp_const(1)
    power = value
    e = exponent
    while e:
        if e & 1:
            answer = bp_mul(answer, power)
        e >>= 1
        if e:
            power = bp_mul(power, power)
    return answer


def bp_derivative_z(value: BP) -> BP:
    return bp_clean(
        {(z_degree - 1, s_degree): coefficient * z_degree
         for (z_degree, s_degree), coefficient in value.items() if z_degree}
    )


Rat = tuple[BP, BP]


def rat(value: BP) -> Rat:
    return value, bp_const(1)


def rat_add(left: Rat, right: Rat) -> Rat:
    return (
        bp_add(bp_mul(left[0], right[1]), bp_mul(right[0], left[1])),
        bp_mul(left[1], right[1]),
    )


def rat_neg(value: Rat) -> Rat:
    return bp_neg(value[0]), value[1]


def rat_sub(left: Rat, right: Rat) -> Rat:
    return rat_add(left, rat_neg(right))


def rat_mul(left: Rat, right: Rat) -> Rat:
    return bp_mul(left[0], right[0]), bp_mul(left[1], right[1])


def rat_div(left: Rat, right: Rat) -> Rat:
    return bp_mul(left[0], right[1]), bp_mul(left[1], right[0])


def rat_derivative_z(value: Rat) -> Rat:
    numerator, denominator = value
    return (
        bp_sub(bp_mul(bp_derivative_z(numerator), denominator),
               bp_mul(numerator, bp_derivative_z(denominator))),
        bp_mul(denominator, denominator),
    )


def verify_contiguity_identity() -> dict[str, object]:
    one = bp_const(1)
    z: BP = {(1, 0): Fraction(1)}
    s: BP = {(0, 1): Fraction(1)}
    one_plus_z = bp_add(one, z)
    one_minus_z = bp_sub(one, z)
    one_plus_z2 = bp_add(one, bp_pow(z, 2))
    delta = bp_mul(s, bp_sub(bp_scale(s, 10), one))
    r_parameter = bp_add(bp_scale(s, -3), bp_const(Fraction(-3, 2)))

    h = rat_div(rat(r_parameter), rat(z))
    h = rat_add(h, rat_neg(rat_div(rat(r_parameter), rat(one_minus_z))))
    h = rat_add(h, rat_div(rat(one), rat(one_plus_z)))
    h = rat_add(
        h,
        rat_div(rat(bp_scale(bp_mul(s, z), 4)), rat(one_plus_z2)),
    )

    n_num = bp_add(bp_mul(bp_sub(bp_scale(s, 10), bp_const(3)), z), bp_scale(bp_pow(z, 2), 2))
    n_num = bp_sub(n_num, bp_mul(bp_add(bp_scale(s, 10), one), bp_pow(z, 3)))
    n_num = bp_add(n_num, bp_scale(bp_pow(z, 4), 2))
    h_reduction = rat_div(rat(n_num), rat(bp_scale(bp_mul(delta, one_plus_z), 2)))

    q_num = bp_add(bp_sub(bp_scale(bp_pow(s, 2), 100), bp_scale(s, 12)), bp_const(-3))
    q_num = bp_add(q_num, bp_mul(bp_sub(bp_const(10), bp_scale(s, 4)), z))
    q_num = bp_add(q_num, bp_mul(bp_sub(bp_scale(s, 8), bp_const(4)), bp_pow(z, 2)))
    q_remainder = rat_div(rat(q_num), rat(bp_scale(delta, 4)))
    g = rat_div(rat(bp_pow(one_plus_z, 3)), rat(one_plus_z2))

    expression = rat_add(rat_derivative_z(h_reduction), rat_mul(h, h_reduction))
    expression = rat_add(rat_sub(expression, g), q_remainder)
    if bp_clean(expression[0]):
        raise AssertionError(expression[0])
    return {
        "H_numerator": "(10s-3)z+2z^2-(10s+1)z^3+2z^4",
        "H_denominator": "2s(10s-1)(1+z)",
        "Q_numerator": "100s^2-12s-3+(10-4s)z+(8s-4)z^2",
        "Q_denominator": "4s(10s-1)",
        "symbolic_numerator_terms_after_cancellation": 0,
    }


def sp_add(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        answer[i] += value
    for i, value in enumerate(right):
        answer[i] += value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def sp_mul(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] += x * y
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def cohomology_minor() -> list[int]:
    # First eight rows of the 9x8 coefficient matrix for
    # H'+(f0'/f0)H=Q0+Q1*z+Q2*z^2, H=N_4/(1+z).
    zero = (0, 0)
    matrix = [
        [(-3, -6), zero, zero, zero, zero, zero, zero, zero],
        [(3, 6), (-1, -6), zero, zero, zero, (-2, 0), zero, zero],
        [(3, 14), (3, 6), (1, -6), zero, zero, (-2, 0), (-2, 0), zero],
        [(3, 6), (3, 14), (3, 6), (3, -6), zero, zero, (-2, 0), (-2, 0)],
        [(6, 4), (3, 6), (3, 14), (3, 6), (5, -6), zero, zero, (-2, 0)],
        [zero, (4, 4), (3, 6), (3, 14), (3, 6), (2, 0), zero, zero],
        [zero, zero, (2, 4), (3, 6), (3, 14), (2, 0), (2, 0), zero],
        [zero, zero, zero, (0, 4), (3, 6), zero, (2, 0), (2, 0)],
    ]
    determinant = [0]
    for permutation in itertools.permutations(range(8)):
        term = [permutation_sign(permutation)]
        for row, column in enumerate(permutation):
            term = sp_mul(term, list(matrix[row][column]))
        determinant = sp_add(determinant, term)
    # 36864*s^2*(2s+1)^2*(10s-1)
    expected = sp_mul(
        [0, 0, 36864],
        sp_mul([1, 4, 4], [-1, 10]),
    )
    if determinant != expected:
        raise AssertionError((determinant, expected))
    return determinant


def gaussian_mul(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def gaussian_add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def frobenius_phase_values() -> dict[str, list[int]]:
    output: dict[str, list[int]] = {}
    for chi in (-1, 1):
        value = (9, 0)
        value = gaussian_add(value, gaussian_mul((-10, chi), (0, chi)))
        value = gaussian_add(value, gaussian_mul((-10, -chi), (0, -chi)))
        if value != (7, 0):
            raise AssertionError((chi, value))
        output[str(chi)] = list(value)
    return output


def shifted_period(p: int, s: int, shift: int) -> int:
    r, _, _, polynomial = item219.pnu_poly(p, s, 0)
    chi = 1 if p % 4 == 1 else -1
    total = 0
    for ell, coefficient in enumerate(polynomial):
        n = r + ell + shift + 1
        if not (1 <= n < p):
            raise AssertionError((p, s, shift, ell, n))
        total += coefficient * item219.residue_weight(n, chi) * pow(n, -1, p)
    return total % p


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime-max", type=int, default=401)
    ap.add_argument("--output", type=Path, default=default_output())
    args = ap.parse_args()
    if args.prime_max < 11:
        raise ValueError("prime maximum must be at least 11")

    identity = verify_contiguity_identity()
    minor = cohomology_minor()
    phase = frobenius_phase_values()
    if item219.hermite_minor() != [0, 2304, 9216, 9216]:
        raise AssertionError("Item 219 scalar minor changed")

    rows: list[tuple[int, ...]] = []
    separate: list[dict[str, int | str]] = []
    common: list[dict[str, int]] = []
    counts = {"rows": 0, "T0_zero": 0, "S1_zero": 0, "common_zero": 0}
    for p in item219.primes_upto(args.prime_max):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (5 * p - 2 * s - 1) % 4:
                continue
            delta = s * (10 * s - 1) % p
            if delta == 0:
                raise AssertionError((p, s, "non-unit contiguity denominator"))
            t0 = shifted_period(p, s, 0)
            t1 = shifted_period(p, s, 1)
            t2 = shifted_period(p, s, 2)
            s1 = item219.period_sum(p, s, 1)
            lhs = 4 * delta * s1 % p
            rhs = (
                (100 * s * s - 12 * s - 3) * t0
                + (10 - 4 * s) * t1
                + (8 * s - 4) * t2
            ) % p
            if lhs != rhs:
                raise AssertionError((p, s, lhs, rhs))
            reduced = ((5 - 2 * s) * t1 + 2 * (2 * s - 1) * t2) % p
            if t0 == 0 and (s1 == 0) != (reduced == 0):
                raise AssertionError((p, s, t0, s1, reduced))
            m = (5 * p - 2 * s - 1) // 4
            counts["rows"] += 1
            counts["T0_zero"] += t0 == 0
            counts["S1_zero"] += s1 == 0
            counts["common_zero"] += t0 == s1 == 0
            rows.append((p, s, m, t0, t1, t2, s1, reduced))
            if t0 == 0 or s1 == 0:
                separate.append(
                    {
                        "p": p,
                        "s": s,
                        "m": m,
                        "zero": "both" if t0 == s1 == 0 else ("T0" if t0 == 0 else "S1"),
                        "T0": t0,
                        "S1": s1,
                    }
                )
            if t0 == s1 == 0:
                common.append({"p": p, "s": s, "m": m})

    result = {
        "schema": "item221-j2-twisted-cohomology-v1",
        "parameters": {
            "j": 2,
            "prime_max_inclusive": args.prime_max,
            "cell": "4m+1=5p-2s, 1<=s<=(p-3)/6, p>=11, s=(p-1)/2 mod 2",
        },
        "dependency": {
            "item219_checker": ITEM219_PATH.name,
            "item219_checker_sha256": file_sha256(ITEM219_PATH),
        },
        "frobenius_resonance": {
            "phase_functional_on_z^p": phase,
            "value": 7,
            "theorem": "under S0=S1=0, a boundary-free first-resonant scalar primitive F1-RF0+c*z^p forces c=0",
            "consequence": "Item219's scalar minor then excludes the reduction on every admissible row",
            "scope": "first z^p resonance only; arbitrary higher polynomials in z^p are not claimed impossible",
        },
        "non_scalar_reduction": identity,
        "cohomology_independence": {
            "basis": ["f0 dz", "z f0 dz", "z^2 f0 dz"],
            "minor_coefficients_in_s": minor,
            "minor_factorization": "36864*s^2*(2s+1)^2*(10s-1)",
            "unit_audit": "s, 2s+1, and 10s-1 are nonzero mod p on every admissible row",
            "conclusion": "no nonzero quadratic remainder is boundary-free sub-Frobenius exact",
        },
        "reduced_common_gate": {
            "T_k": "L_chi integral_0^(1,i,-i) z^k f0 dz, equivalently the shifted four-residue sum",
            "identity": "4s(10s-1)S1=(100s^2-12s-3)T0+(10-4s)T1+(8s-4)T2",
            "common_equivalence": "T0=0 and (5-2s)T1+2(2s-1)T2=0",
        },
        "finite_replay": {
            "status": "EXACT FINITE ONLY",
            "counts": counts,
            "separate_zero_rows": separate,
            "common_zero_rows": common,
            "row_digest_sha256": row_digest(rows),
        },
        "status_ledger": {
            "PROVED": [
                "first z^p resonance collapses to the excluded nonresonant scalar ansatz under the common gate",
                "exact all-row quadratic-remainder contiguity identity",
                "three quadratic cohomology classes are independent for every admissible row",
                "exact one-polynomial reduced common gate",
            ],
            "EXACT_FINITE": [
                "all admissible rows through the recorded bound; no common zero in this finite set"
            ],
            "OPEN": [
                "all-prime nonvanishing of the reduced two-period gate",
                "higher polynomials in z^p and higher/non-polynomial cohomology mechanisms",
                "any common-log capacity reduction or conclusion about e+pi",
            ],
        },
    }
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(payload.decode("utf-8"), end="")


if __name__ == "__main__":
    main()
