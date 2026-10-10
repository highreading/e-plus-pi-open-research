#!/usr/bin/env python3
"""Deterministic certificate for Item 251's exceptional j=2 period.

This checker isolates the period left after Item 250's rank-one elimination.
It proves an exact beta normalization, a diagonal/algebraic generating
function, and a telescoping recurrence for the resulting integer sequence.
It also replays the rank-aware exceptional-row implication against Item 250.

Only Python's standard library is used.  Bounded prime scans are recorded as
finite evidence and are not used as all-prime theorems.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
RESULT_NAME = "item251_j2_exceptional_period_certificate.json"
ITEM250_NAME = "item250_j2_ordinary_phase_certificate.py"
ITEM250_SHA256 = "2364a9e9c9be0ea0827c2b12137883ad326d77017a53bb4f242be300335e90ce"


def resolve(name: str) -> Path:
    for base in (HERE, HERE.parent / "scripts"):
        candidate = base / name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM250_PATH = resolve(ITEM250_NAME)
if sha256(ITEM250_PATH) != ITEM250_SHA256:
    raise RuntimeError("Item250 checker hash mismatch")
item250 = load("item251_item250", ITEM250_PATH)


def default_output() -> Path:
    if HERE.name.lower() == "scripts":
        return HERE.parent / "results" / RESULT_NAME
    return HERE / RESULT_NAME


def fmod(value: F, p: int) -> int:
    if value.denominator % p == 0:
        raise AssertionError(("nonunit fraction", value, p))
    return value.numerator * pow(value.denominator, -1, p) % p


def rising_int(start: int, count: int) -> int:
    out = 1
    for j in range(count):
        out *= start + j
    return out


def beta_fraction(s: int) -> F:
    return F(math.factorial(2 * s - 1) * math.factorial(s - 1), math.factorial(3 * s - 1))


def tail_fraction(r: int, s: int) -> F:
    h = (r - 1) // 2
    return F(
        ((-1) ** (s + h)) * math.factorial(2 * s) * math.factorial(s + h),
        math.factorial(3 * s + h + 1),
    )


def tau_fraction(r: int, s: int) -> F:
    h = (r - 1) // 2
    return F(((-1) ** (s + h)) * 2 * rising_int(s, h + 1), 3 * rising_int(3 * s + 1, h + 1))


def a_direct(s: int) -> int:
    return sum(
        math.comb(3 * s - 1, s + j) * math.comb(s + j - 1, j)
        for j in range(2 * s)
    )


def a_diagonal(s: int) -> int:
    # [x^(s-1)] (((2+x)^(3s-1)-1)/(1+x)).
    n = s - 1
    first = sum(
        ((-1) ** (n - k)) * math.comb(3 * s - 1, k) * (2 ** (3 * s - 1 - k))
        for k in range(n + 1)
    )
    return first - ((-1) ** n)


def recurrence_coefficients(s: int) -> tuple[int, int, int]:
    c0 = -6 * (3 * s + 1) * (3 * s + 2) * (28 * s + 39)
    c1 = -(1456 * s**3 + 3456 * s**2 + 2303 * s + 435)
    c2 = (s + 1) * (2 * s + 3) * (28 * s + 11)
    return c0, c1, c2


def a_sequence(max_s: int) -> list[int]:
    if max_s < 2:
        raise ValueError(max_s)
    values = [0] * (max_s + 1)
    values[1], values[2] = 3, 49
    for s in range(1, max_s - 1):
        c0, c1, c2 = recurrence_coefficients(s)
        quotient, remainder = divmod(-(c0 * values[s] + c1 * values[s + 1]), c2)
        if remainder:
            raise AssertionError(("nonintegral recurrence", s, remainder))
        values[s + 2] = quotient
    return values


# Sparse bivariate integer polynomials: key=(degree in s, degree in u).
Poly = dict[tuple[int, int], int]


def pclean(poly: Poly) -> Poly:
    return {key: value for key, value in poly.items() if value}


def padd(*polys: Poly) -> Poly:
    out: Poly = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, 0) + value
    return pclean(out)


def pscale(value: int, poly: Poly) -> Poly:
    return pclean({key: value * coefficient for key, coefficient in poly.items()})


def pmul(*polys: Poly) -> Poly:
    out: Poly = {(0, 0): 1}
    for poly in polys:
        product: Poly = {}
        for (si, ui), x in out.items():
            for (sj, uj), y in poly.items():
                key = (si + sj, ui + uj)
                product[key] = product.get(key, 0) + x * y
        out = pclean(product)
    return out


def ppow(poly: Poly, exponent: int) -> Poly:
    out: Poly = {(0, 0): 1}
    for _ in range(exponent):
        out = pmul(out, poly)
    return out


def pdu(poly: Poly) -> Poly:
    return pclean({(si, ui - 1): ui * value for (si, ui), value in poly.items() if ui})


ONE: Poly = {(0, 0): 1}
S: Poly = {(1, 0): 1}
U: Poly = {(0, 1): 1}


def lin_s(a: int, b: int) -> Poly:
    return pclean({(1, 0): a, (0, 0): b})


def lin_u(a: int, b: int) -> Poly:
    return pclean({(0, 1): a, (0, 0): b})


def telescoping_identity() -> dict[str, int]:
    # P(s,u), in the notation of the report's certificate H.
    p_inner: Poly = {}
    coefficient_rows = {
        4: (252, 435, 132),
        3: (1176, 2058, 627),
        2: (2380, 4211, 1287),
        1: (2016, 3648, 1182),
        0: (448, 848, 312),
    }
    for u_degree, (s2, s1, s0) in coefficient_rows.items():
        p_inner[(2, u_degree)] = s2
        p_inner[(1, u_degree)] = s1
        p_inner[(0, u_degree)] = s0

    common = pscale(3, pmul(lin_s(3, 1), lin_s(3, 2)))
    n_over_u = pmul(common, lin_u(1, -1), lin_u(1, 1), p_inner)
    n_over_u_plus_1 = pmul(common, U, lin_u(1, -1), p_inner)
    numerator = pmul(n_over_u, U)
    lhs = padd(
        pdu(numerator),
        pmul(lin_s(1, -1), n_over_u),
        pmul(lin_s(2, -1), n_over_u_plus_1),
    )

    # Multiply the desired identity by q=4s(2s+1).  The beta-ratio
    # denominators then cancel exactly.
    qd0 = pscale(-24, pmul(S, lin_s(2, 1), lin_s(3, 1), lin_s(3, 2), lin_s(28, 39)))
    cubic = padd(
        {(3, 0): 1456}, {(2, 0): 3456}, {(1, 0): 2303}, {(0, 0): 435}
    )
    qd1 = pscale(-6, pmul(lin_s(3, 1), lin_s(3, 2), cubic))
    qd2 = pscale(
        9,
        pmul(lin_s(3, 1), lin_s(3, 2), lin_s(3, 4), lin_s(3, 5), lin_s(28, 11)),
    )
    rpoly = pmul(U, ppow(lin_u(1, 1), 2))
    rhs = padd(qd0, pmul(qd1, rpoly), pmul(qd2, ppow(rpoly, 2)))
    if lhs != rhs:
        missing = padd(lhs, pscale(-1, rhs))
        raise AssertionError(("telescoping polynomial", missing))
    return {
        "nonzero_monomials": len(lhs),
        "max_s_degree": max(si for si, _ in lhs),
        "max_u_degree": max(ui for _, ui in lhs),
    }


def conv(left: list[int], right: list[int], length: int) -> list[int]:
    out = [0] * length
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right[: length - i]):
            out[i + j] += x * y
    return out


def fps_add(left: list[int], right: list[int]) -> list[int]:
    return [x + y for x, y in zip(left, right)]


def generating_function_prefix(length: int) -> list[int]:
    # The unique w in t Z[[t]] with w=t(2+w)^3, followed by
    # (2+w)^3/(2(1-w^2))-1/(1+t).
    w = [0] * length
    two = [2] + [0] * (length - 1)
    for _ in range(length):
        cube = conv(conv(fps_add(two, w), fps_add(two, w), length), fps_add(two, w), length)
        w = [0] + cube[:-1]
    w2 = conv(w, w, length)
    inverse = [0] * length
    inverse[0] = 1
    power = [0] * length
    power[0] = 1
    for _ in range(1, length):
        power = conv(power, w2, length)
        inverse = fps_add(inverse, power)
    numerator = conv(conv(fps_add(two, w), fps_add(two, w), length), fps_add(two, w), length)
    product = conv(numerator, inverse, length)
    if any(value % 2 for value in product):
        raise AssertionError("unexpected half-integral generating coefficient")
    return [product[n] // 2 - ((-1) ** n) for n in range(length)]


def factorial_beta_mod(p: int, s: int) -> int:
    numerator = 1
    denominator = 1
    for j in range(1, 2 * s):
        numerator = numerator * j % p
    for j in range(1, s):
        numerator = numerator * j % p
    for j in range(1, 3 * s):
        denominator = denominator * j % p
    return numerator * pow(denominator, -1, p) % p


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\1") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\0" * (((limit - start) // prime) + 1)
    return [value for value in range(2, limit + 1) if sieve[value]]


def digest_rows(rows: Iterable[tuple[int, ...]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update((",".join(map(str, row)) + "\n").encode("ascii"))
    return digest.hexdigest()


TARGET_LINEAR = (
    (953, 158, 1),
    (2281, 378, 5),
    (5711, 941, 31),
    (1279, 199, 41),
    (3929, 636, 55),
    (1657, 256, 59),
    (367, 39, 65),
)


def row_invariant(p: int, s: int, r: int, a_values: list[int], data: dict[str, Any]) -> dict[str, Any]:
    phase = item250.evaluate_phase_row(p, s, data)
    beta = factorial_beta_mod(p, s)
    tau = fmod(tau_fraction(r, s), p)
    if fmod(beta_fraction(s), p) != beta:
        raise AssertionError(("beta fraction", p, s))
    if fmod(tail_fraction(r, s), p) != phase["f"]:
        raise AssertionError(("tail fraction", p, s))
    if beta * tau % p != phase["f"]:
        raise AssertionError(("tail ratio", p, s))

    a_value = a_values[s] % p
    e_from_a = beta * a_value * pow(2, -1, p) % p
    if e_from_a != phase["e"]:
        raise AssertionError(("beta-normalized period", p, s, e_from_a, phase["e"]))

    kappa, _ = item250.reversal_certificate(r, data)
    kappa_mod = fmod(kappa, p)
    w_value = ((9 * kappa_mod * a_value * pow(2, -1, p)) - tau) % p
    z_from_a = beta * w_value % p
    z_direct = (9 * kappa_mod * phase["e"] - phase["f"]) % p
    if z_from_a != z_direct:
        raise AssertionError(("Z normalization", p, s))

    gates: list[int] = []
    f_vector: list[int] = []
    u_vector: list[int] = []
    for nu in (0, 1):
        f_nu = fmod(data["st"][nu], p)
        _, b_nu, d_nu = data[f"x{nu}"]
        u_nu = (9 * fmod(b_nu, p) * phase["c"] + 9 * fmod(d_nu, p) - 10 * fmod(data["ba"][nu], p)) % p
        gate = (f_nu * z_from_a + u_nu) % p
        if gate != phase[f"g{nu}"]:
            raise AssertionError(("gate reconstruction", p, s, nu, gate, phase[f"g{nu}"]))
        f_vector.append(f_nu)
        u_vector.append(u_nu)
        gates.append(gate)

    compatibility = (f_vector[0] * u_vector[1] - f_vector[1] * u_vector[0]) % p
    if compatibility != phase["linear"]:
        raise AssertionError(("compatibility", p, s))
    return {
        "p": p,
        "s": s,
        "r": r,
        "A": a_value,
        "beta": beta,
        "tau": tau,
        "W": w_value,
        "Z": z_from_a,
        "f0": f_vector[0],
        "f1": f_vector[1],
        "u0": u_vector[0],
        "u1": u_vector[1],
        "g0": gates[0],
        "g1": gates[1],
        "linear": compatibility,
        "rank_zero": f_vector == [0, 0],
    }


def scalar_zero_scan(prime_max: int, a_values: list[int]) -> dict[str, Any]:
    rows = 0
    a_zeros: list[tuple[int, int, int]] = []
    increment_zeros: list[tuple[int, int, int]] = []
    digest = hashlib.sha256()
    for p in primes_upto(prime_max):
        if p < 11:
            continue
        for s in range(1, (p - 3) // 6 + 1):
            if (s - (p - 1) // 2) % 2:
                continue
            r = (p - 6 * s - 3) // 2
            az = a_values[s] % p == 0
            bz = (a_values[s] + a_values[s + 1]) % p == 0
            rows += 1
            digest.update(f"{p},{s},{r},{int(az)},{int(bz)}\n".encode("ascii"))
            if az:
                a_zeros.append((p, s, r))
            if bz:
                increment_zeros.append((p, s, r))
    return {
        "prime_max_inclusive": prime_max,
        "rows": rows,
        "A_zero_count": len(a_zeros),
        "increment_zero_count": len(increment_zeros),
        "first_A_zeros": a_zeros[:20],
        "first_increment_zeros": increment_zeros[:20],
        "row_digest_sha256": digest.hexdigest(),
        "role": "bounded exact replay only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase-prime-max", type=int, default=401)
    parser.add_argument("--scalar-prime-max", type=int, default=20000)
    parser.add_argument("--identity-s-max", type=int, default=1000)
    parser.add_argument("--output", type=Path, default=default_output())
    args = parser.parse_args()
    if args.phase_prime_max < 23 or args.scalar_prime_max < 100 or args.identity_s_max < 50:
        raise ValueError("bounds too small")

    max_target_s = max(s for _, s, _ in TARGET_LINEAR)
    max_scalar_s = (args.scalar_prime_max - 3) // 6 + 1
    max_s = max(args.identity_s_max + 2, max_target_s, max_scalar_s + 1)
    a_values = a_sequence(max_s)

    direct_checks = 0
    for s in range(1, min(args.identity_s_max, 100) + 1):
        if a_values[s] != a_direct(s) or a_values[s] != a_diagonal(s):
            raise AssertionError(("A identity", s))
        if beta_fraction(s) * a_values[s] != F(1, 1) * sum(
            F(math.comb(2 * s - 1, j), s + j) for j in range(2 * s)
        ):
            raise AssertionError(("integral normalization", s))
        direct_checks += 3

    telescoping = telescoping_identity()
    recurrence_checks = 0
    increment_checks = 0
    alternating = 3
    for s in range(1, args.identity_s_max):
        c0, c1, c2 = recurrence_coefficients(s)
        if c0 - c1 + c2 != 0:
            raise AssertionError(("known alternating solution", s))
        if c0 * a_values[s] + c1 * a_values[s + 1] + c2 * a_values[s + 2] != 0:
            raise AssertionError(("recurrence", s))
        recurrence_checks += 1
        increment = a_values[s] + a_values[s + 1]
        next_increment = a_values[s + 1] + a_values[s + 2]
        numerator = 6 * (3 * s + 1) * (3 * s + 2) * (28 * s + 39)
        denominator = (s + 1) * (2 * s + 3) * (28 * s + 11)
        if denominator * next_increment != numerator * increment:
            raise AssertionError(("increment ratio", s))
        increment_checks += 1
        if s < args.identity_s_max - 1:
            alternating += ((-1) ** s) * increment
            if ((-1) ** s) * alternating != a_values[s + 1]:
                raise AssertionError(("alternating reconstruction", s))

    gf_length = 30
    gf_values = generating_function_prefix(gf_length)
    if gf_values != [a_values[s] for s in range(1, gf_length + 1)]:
        raise AssertionError("generating function prefix")

    cache: dict[int, dict[str, Any]] = {}
    phase_counts = {
        "rows": 0,
        "period_identity_rows": 0,
        "linear_exceptional_rows": 0,
        "common_gate_zeros": 0,
        "rank_zero_rows": 0,
    }
    phase_rows: list[tuple[int, ...]] = []
    linear_hits: list[dict[str, Any]] = []
    for p, s, r in item250.actual_rows(args.phase_prime_max):
        data = cache.get(r)
        if data is None:
            data = item250.phase_data(r)
            cache[r] = data
        row = row_invariant(p, s, r, a_values, data)
        phase_counts["rows"] += 1
        phase_counts["period_identity_rows"] += 1
        phase_counts["linear_exceptional_rows"] += row["linear"] == 0
        phase_counts["common_gate_zeros"] += row["g0"] == row["g1"] == 0
        phase_counts["rank_zero_rows"] += row["rank_zero"]
        phase_rows.append((p, s, r, row["A"], row["Z"], row["linear"], row["g0"], row["g1"]))
        if row["linear"] == 0:
            linear_hits.append(row)

    target_rows: list[dict[str, Any]] = []
    for p, s, r in TARGET_LINEAR:
        data = cache.get(r)
        if data is None:
            data = item250.phase_data(r)
            cache[r] = data
        row = row_invariant(p, s, r, a_values, data)
        if row["linear"] != 0 or row["g0"] == row["g1"] == 0:
            raise AssertionError(("target linear false positive", p, s, row))
        target_rows.append(row)

    scalar_scan = scalar_zero_scan(args.scalar_prime_max, a_values)
    if scalar_scan["first_A_zeros"][0] != (31, 3, 5):
        raise AssertionError("first A zero changed")
    if scalar_scan["first_increment_zeros"][0] != (41, 4, 7):
        raise AssertionError("first increment zero changed")

    result = {
        "schema": "item251-j2-exceptional-period-v1",
        "parameters": {
            "phase_prime_max_inclusive": args.phase_prime_max,
            "scalar_prime_max_inclusive": args.scalar_prime_max,
            "identity_s_max_inclusive": args.identity_s_max,
            "cell": "p=2r+6s+3, r odd, Q=2s",
        },
        "exact_formulas": {
            "beta": "B_s=(2s-1)!(s-1)!/(3s-1)!",
            "integer_period": "A_s=sum_(j=0)^(2s-1) C(3s-1,s+j)C(s+j-1,j)",
            "period": "e=J_0=B_s*A_s/2",
            "tail_ratio": "mathfrak_f=B_s*tau_(r,s), tau=(-1)^(s+h)*(2/3)*(s)_(h+1)/(3s+1)_(h+1)",
            "surviving_period": "Z=B_s*((9*kappa_r/2)*A_s-tau_(r,s))",
            "diagonal": "A_s=[x^(s-1)](((2+x)^(3s-1)-1)/(1+x))",
            "generating_function": "w=t(2+w)^3; sum_(s>=1)A_s*t^(s-1)=(2+w)^3/(2(1-w^2))-1/(1+t)",
            "recurrence": "(s+1)(2s+3)(28s+11)A_(s+2)-(1456s^3+3456s^2+2303s+435)A_(s+1)-6(3s+1)(3s+2)(28s+39)A_s=0",
            "initial_values": "A_1=3, A_2=49",
            "increment": "Delta_s=A_(s+1)+A_s; Delta_(s+1)/Delta_s=6(3s+1)(3s+2)(28s+39)/((s+1)(2s+3)(28s+11)) over Q",
            "exceptional_rank_one": "if f0*U1-f1*U0=0 and (f0,f1)!=(0,0) mod p, collision iff f_nu*B_s*((9*kappa/2)A_s-tau)+U_nu=0 for one/every nonzero f_nu",
            "rank_zero_branch": "if f0=f1=0 mod p, collision requires U0=U1=0 and Z is irrelevant",
        },
        "symbolic_replay": {
            "telescoping": telescoping,
            "direct_sum_diagonal_integral_checks": direct_checks,
            "recurrence_checks": recurrence_checks,
            "increment_ratio_checks": increment_checks,
            "generating_function_coefficients": gf_length,
        },
        "phase_replay": {
            "counts": phase_counts,
            "linear_hits": linear_hits,
            "row_digest_sha256": digest_rows(phase_rows),
            "role": "bounded exact replay only",
        },
        "explicit_affine_false_positives": target_rows,
        "scalar_zero_scan": scalar_scan,
        "unit_audit": {
            "beta_factorials": "all arguments <=3s-1<p",
            "tail_factorials": "all arguments <=3s+h+1<p",
            "tau_denominators": "3 and 3s+j (1<=j<=h+1) are in [1,p-1]",
            "telescoper_denominators": "4s(2s+1) is a p-unit because 1<=2s+1<p",
            "recurrence_reduction_warning": "28s+11 and other displayed recurrence factors are not asserted p-units; the recurrence is used integrally",
            "division_by_f_vector": False,
        },
        "status": {
            "PROVED": [
                "the exact beta normalization e=B_s*A_s/2 and tail ratio mathfrak_f=B_s*tau",
                "the exact rank-aware formula for the surviving period Z on Item250's exceptional locus",
                "the coefficient, diagonal, algebraic generating-function, and telescoping-recurrence descriptions of A_s",
                "the first-order hypergeometric recurrence for A_(s+1)+A_s and the resulting alternating incomplete-sum structure",
                "the complete denominator audit stated in this certificate",
            ],
            "EXACT_FINITE": [
                "the phase identity and exceptional-row replay through the recorded phase prime bound",
                "the recorded larger affine false positives",
                "the separate scalar zero census through the recorded scalar prime bound",
            ],
            "OPEN": [
                "all-prime nonvanishing or zero-density control of the second residual on affine-exceptional rows",
                "all-prime classification of the rank-zero branch",
                "a rowwise theorem for the incomplete hypergeometric sum A_s modulo p",
                "any capacity reduction, Route-1 gain, or conclusion about e+pi",
            ],
        },
        "booking": {
            "new_unconditional_linear_log_rate": 0,
            "new_divisibility_exponent": 0,
            "capacity_reduction": 0,
        },
        "dependency": {ITEM250_NAME: ITEM250_SHA256},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
