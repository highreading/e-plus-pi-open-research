#!/usr/bin/env python3
"""Exact certificate for the n=5 p-boundary and complementary-sum identities.

The companion Markdown file contains the all-prime proofs.  Every prime scan
below is finite and diagnostic; it is not used as a proof of zero avoidance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


Pair = tuple[int, int]  # a+b*A, A^2=3*A-1
Elt = tuple[int, int, int, int]  # power basis of Z[zeta_5]
QElt = tuple[Pair, Pair]  # c+d*z modulo z^2+z+(3-A)

PZERO: Pair = (0, 0)
PONE: Pair = (1, 0)
A: Pair = (0, 1)
AINV: Pair = (3, -1)
KAPPA: Pair = (-2, 5)

EZERO: Elt = (0, 0, 0, 0)
EONE: Elt = (1, 0, 0, 0)
ZETA: Elt = (0, 1, 0, 0)
ETA: Elt = (0, -1, 0, -1)
ETABAR: Elt = (1, 1, 0, 1)
U: Elt = (1, 1, 0, 0)
V: Elt = (0, -1, -1, -1)
A_IN_E: Elt = (1, 0, -1, -1)


def padd(x: Pair, y: Pair) -> Pair:
    return (x[0] + y[0], x[1] + y[1])


def pneg(x: Pair) -> Pair:
    return (-x[0], -x[1])


def pscale(c: int, x: Pair) -> Pair:
    return (c * x[0], c * x[1])


def pmul(x: Pair, y: Pair) -> Pair:
    return (
        x[0] * y[0] - x[1] * y[1],
        x[0] * y[1] + x[1] * y[0] + 3 * x[1] * y[1],
    )


def pmod(x: Pair, prime: int) -> Pair:
    return (x[0] % prime, x[1] % prime)


def paddm(x: Pair, y: Pair, prime: int) -> Pair:
    return ((x[0] + y[0]) % prime, (x[1] + y[1]) % prime)


def pscalem(c: int, x: Pair, prime: int) -> Pair:
    return (c * x[0] % prime, c * x[1] % prime)


def pmulm(x: Pair, y: Pair, prime: int) -> Pair:
    return pmod(pmul(x, y), prime)


def eadd(x: Elt, y: Elt) -> Elt:
    return tuple(x[j] + y[j] for j in range(4))  # type: ignore[return-value]


def escale(c: int, x: Elt) -> Elt:
    return tuple(c * value for value in x)  # type: ignore[return-value]


def emul(x: Elt, y: Elt) -> Elt:
    raw = [0] * 7
    for j, xj in enumerate(x):
        for k, yk in enumerate(y):
            raw[j + k] += xj * yk
    # zeta^4=-(1+zeta+zeta^2+zeta^3).
    for degree in range(6, 3, -1):
        value = raw[degree]
        for target in range(degree - 4, degree):
            raw[target] -= value
    return tuple(raw[:4])  # type: ignore[return-value]


def emod(x: Elt, prime: int) -> Elt:
    return tuple(value % prime for value in x)  # type: ignore[return-value]


def eaddm(x: Elt, y: Elt, prime: int) -> Elt:
    return emod(eadd(x, y), prime)


def escalem(c: int, x: Elt, prime: int) -> Elt:
    return emod(escale(c, x), prime)


def emulm(x: Elt, y: Elt, prime: int) -> Elt:
    return emod(emul(x, y), prime)


def epowm(x: Elt, exponent: int, prime: int) -> Elt:
    answer = EONE
    base = emod(x, prime)
    while exponent:
        if exponent & 1:
            answer = emulm(answer, base, prime)
        base = emulm(base, base, prime)
        exponent //= 2
    return answer


def qadd(x: QElt, y: QElt, prime: int) -> QElt:
    return (paddm(x[0], y[0], prime), paddm(x[1], y[1], prime))


def qneg(x: QElt, prime: int) -> QElt:
    return (pscalem(-1, x[0], prime), pscalem(-1, x[1], prime))


def qscale(c: Pair, x: QElt, prime: int) -> QElt:
    return (pmulm(c, x[0], prime), pmulm(c, x[1], prime))


def qmul(x: QElt, y: QElt, prime: int) -> QElt:
    # z^2=-z-(3-A)=-z-A^{-1}.
    df = pmulm(x[1], y[1], prime)
    constant = paddm(
        pmulm(x[0], y[0], prime),
        pscalem(-1, pmulm(AINV, df, prime), prime),
        prime,
    )
    linear = paddm(
        paddm(pmulm(x[0], y[1], prime), pmulm(x[1], y[0], prime), prime),
        pscalem(-1, df, prime),
        prime,
    )
    return (constant, linear)


def qpow_z(exponent: int, prime: int) -> QElt:
    answer: QElt = (PONE, PZERO)
    base: QElt = (PZERO, PONE)
    while exponent:
        if exponent & 1:
            answer = qmul(answer, base, prime)
        base = qmul(base, base, prime)
        exponent //= 2
    return answer


def qmonomial(coefficient: Pair, exponent: int, prime: int) -> QElt:
    return qscale(coefficient, qpow_z(exponent, prime), prime)


def falling(n: int, length: int) -> int:
    answer = 1
    for j in range(length):
        answer *= n - j
    return answer


def t_value(n: int) -> Pair:
    return padd(
        PONE,
        padd(
            pscale(-n, A),
            padd(
                pscale(n * (n - 1), (-1, 2)),
                pscale(n * (n - 1) * (n - 2), (1, -2)),
            ),
        ),
    )


def h_pair_is_proper_mod_p(current: Pair, previous: Pair, prime: int) -> bool:
    """Whether (current,previous) is proper in F_p[A]/(A^2-3A+1)."""

    a, b = current
    c, d = previous
    norm_current = (a * a + 3 * a * b + b * b) % prime
    norm_previous = (c * c + 3 * c * d + d * d) % prime
    cross = (a * d - b * c) % prime
    return norm_current == norm_previous == cross == 0


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_checks(max_degree: int) -> None:
    if max_degree < 5:
        raise ValueError("exact-degree must be at least 5")

    q_values: list[Pair] = [PONE, pneg(A)]
    for _ in range(2, max_degree + 1):
        q_values.append(pscale(-1, pmul(A, padd(q_values[-1], q_values[-2]))))

    expected = [PONE, (0, -1), (-1, 2), (1, -2), PZERO]
    if q_values[:5] != expected:
        raise AssertionError(f"wrong reciprocal initial values: {q_values[:5]}")
    for j in range(max_degree - 4):
        if q_values[j + 5] != pmul(KAPPA, q_values[j]):
            raise AssertionError(f"q five-step identity failed at j={j}")

    h_values: list[Pair] = [PONE, (1, -1)]
    for n in range(2, max_degree + 1):
        h_values.append(
            padd(
                PONE,
                padd(
                    pscale(-n, pmul(A, h_values[-1])),
                    pscale(-n * (n - 1), pmul(A, h_values[-2])),
                ),
            )
        )
    for n in range(max_degree + 1):
        convolution = PZERO
        for j in range(n + 1):
            convolution = padd(convolution, pscale(falling(n, j), q_values[j]))
        if convolution != h_values[n]:
            raise AssertionError(f"exact convolution failed at n={n}")
        if n >= 5:
            left = padd(
                h_values[n],
                pscale(-falling(n, 5), pmul(KAPPA, h_values[n - 5])),
            )
            if left != t_value(n):
                raise AssertionError(f"exact five-step law failed at n={n}")


def prime_checks(prime: int) -> list[dict[str, int]]:
    if prime == 5 or prime < 3:
        raise ValueError("prime must be odd and different from 5")

    # Factorials and inverse factorials below p.
    factorial = [1]
    for n in range(1, prime):
        factorial.append(factorial[-1] * n % prime)
    inverse_factorial = [pow(value, -1, prime) for value in factorial]

    # Scalar recurrence through one full boundary and enough terms to compare.
    h: list[Pair] = [PONE, pmod((1, -1), prime)]
    for n in range(2, 2 * prime + 5):
        h.append(
            paddm(
                PONE,
                paddm(
                    pscalem(-n, pmulm(A, h[-1], prime), prime),
                    pscalem(-n * (n - 1), pmulm(A, h[-2], prime), prime),
                    prime,
                ),
                prime,
            )
        )
    for n in range(prime + 5):
        if h[n + prime] != h[n]:
            raise AssertionError(f"period failed at p={prime}, n={n}")
    for n in range(5, 2 * prime + 5):
        left = paddm(
            h[n],
            pscalem(-falling(n, 5), pmulm(KAPPA, h[n - 5], prime), prime),
            prime,
        )
        if left != pmod(t_value(n), prime):
            raise AssertionError(f"five-step law failed at p={prime}, n={n}")
    for s in range(5):
        if h[prime + s] != pmod(t_value(s), prime) or h[prime + s] != h[s]:
            raise AssertionError(f"boundary reset failed at p={prime}, s={s}")

    # Reciprocal q-values and the two Wilson endpoint formulas.
    q_values: list[Pair] = [PONE, pmod((0, -1), prime)]
    for _ in range(2, prime):
        q_values.append(
            pscalem(-1, pmulm(A, paddm(q_values[-1], q_values[-2], prime), prime), prime)
        )
    endpoint_1 = PZERO
    for j in range(prime):
        endpoint_1 = paddm(
            endpoint_1,
            pscalem((-1) ** j * factorial[j], q_values[j], prime),
            prime,
        )
    endpoint_2 = PZERO
    for j in range(prime - 1):
        endpoint_2 = paddm(
            endpoint_2,
            pscalem((-1) ** j * factorial[j + 1], q_values[j], prime),
            prime,
        )
    if endpoint_1 != h[prime - 1] or endpoint_2 != h[prime - 2]:
        raise AssertionError(f"Wilson endpoint formula failed at p={prime}")

    # Cyclotomic unit identities and all complementary-degree formulas.
    if emul(U, ETA) != EONE or emul(V, ETABAR) != EONE:
        raise AssertionError("incorrect exact cyclotomic units")
    x_powers = [EONE]
    y_powers = [EONE]
    u_powers = [EONE]
    v_powers = [EONE]
    p_x = [EONE]
    p_y = [EONE]
    for d in range(1, prime):
        x_powers.append(emulm(x_powers[-1], ETA, prime))
        y_powers.append(emulm(y_powers[-1], ETABAR, prime))
        u_powers.append(emulm(u_powers[-1], U, prime))
        v_powers.append(emulm(v_powers[-1], V, prime))
        p_x.append(eaddm(x_powers[d], escalem(-d, p_x[-1], prime), prime))
        p_y.append(eaddm(y_powers[d], escalem(-d, p_y[-1], prime), prime))
    for d in range(prime):
        m = prime - 1 - d
        left_u = EZERO
        left_v = EZERO
        for j in range(d + 1):
            coefficient = factorial[m + j]
            left_u = eaddm(left_u, escalem(coefficient, u_powers[j], prime), prime)
            left_v = eaddm(left_v, escalem(coefficient, v_powers[j], prime), prime)
        factor = inverse_factorial[m]
        rhs_x = emulm(x_powers[d], escalem(factor, left_u, prime), prime)
        rhs_y = emulm(y_powers[d], escalem(factor, left_v, prime), prime)
        if rhs_x != p_x[d] or rhs_y != p_y[d]:
            raise AssertionError(f"complementary formula failed at p={prime}, d={d}")

    # Frobenius in every residue class modulo five.
    target_u = eaddm(EONE, epowm(ZETA, prime % 5, prime), prime)
    target_v = eaddm(EONE, epowm(ZETA, (-prime) % 5, prime), prime)
    if epowm(U, prime, prime) != target_u or epowm(V, prime, prime) != target_v:
        raise AssertionError(f"cyclotomic Frobenius failed at p={prime}")
    a_frobenius = epowm(A_IN_E, prime, prime)
    if prime % 5 in (1, 4):
        expected_a = emod(A_IN_E, prime)
    else:
        expected_a = eaddm(escalem(3, EONE, prime), escalem(-1, A_IN_E, prime), prime)
    if a_frobenius != expected_a:
        raise AssertionError(f"quadratic Frobenius failed at p={prime}")

    # Remainders modulo Q.  Because A is a unit, Q=0 is z^2+z+(3-A)=0.
    e_remainders: list[QElt] = []
    current: QElt = (PZERO, PZERO)
    z_power: QElt = (PONE, PZERO)
    for n in range(prime):
        current = qadd(current, qscale((inverse_factorial[n], 0), z_power, prime), prime)
        e_remainders.append(current)
        if n >= 1:
            coefficient_1 = pscalem(
                -1,
                pmulm(
                    A,
                    paddm(
                        pscalem(inverse_factorial[n], h[n], prime),
                        pscalem(inverse_factorial[n - 1], h[n - 1], prime),
                        prime,
                    ),
                    prime,
                ),
                prime,
            )
            coefficient_2 = pscalem(
                -1,
                pmulm(A, pscalem(inverse_factorial[n], h[n], prime), prime),
                prime,
            )
            rhs = qadd(
                qmonomial(coefficient_1, n + 1, prime),
                qmonomial(coefficient_2, n + 2, prime),
                prime,
            )
            if current != rhs:
                raise AssertionError(f"remainder formula failed at p={prime}, n={n}")
        z_power = qmul(z_power, (PZERO, PONE), prime)

    endpoint_rhs = qadd(
        qmonomial(
            pmulm(A, paddm(h[prime - 1], pscalem(-1, h[prime - 2], prime), prime), prime),
            prime,
            prime,
        ),
        qmonomial(pmulm(A, h[prime - 1], prime), prime + 1, prime),
        prime,
    )
    if e_remainders[prime - 1] != endpoint_rhs:
        raise AssertionError(f"boundary endpoint remainder failed at p={prime}")

    for d in range(prime):
        m = prime - 1 - d
        reverse_tail: QElt = (PZERO, PZERO)
        z_j: QElt = (PONE, PZERO)
        for j in range(m):
            coefficient = (-1) ** j * factorial[m - 1 - j]
            reverse_tail = qadd(
                reverse_tail,
                qscale((coefficient % prime, 0), z_j, prime),
                prime,
            )
            z_j = qmul(z_j, (PZERO, PONE), prime)
        tail_rhs = qscale(
            (((-1) ** d) % prime, 0),
            qmul(qpow_z(d + 1, prime), reverse_tail, prime),
            prime,
        )
        actual_tail = qadd(e_remainders[prime - 1], qneg(e_remainders[d], prime), prime)
        if actual_tail != tail_rhs:
            raise AssertionError(f"reverse-tail remainder failed at p={prime}, d={d}")

    return [
        {"p": prime, "d": d}
        for d in range(1, prime)
        if h_pair_is_proper_mod_p(h[d], h[d - 1], prime)
    ]


def run(exact_degree: int, max_prime: int) -> dict[str, object]:
    if max_prime < 19:
        raise ValueError("max-prime must be at least 19")
    exact_checks(exact_degree)
    hits: list[dict[str, int]] = []
    residues_seen: set[int] = set()
    prime_count = 0
    for prime_value in sp.primerange(3, max_prime + 1):
        prime = int(prime_value)
        if prime == 5:
            continue
        prime_count += 1
        residues_seen.add(prime % 5)
        hits.extend(prime_checks(prime))

    return {
        "description": "Exact p-boundary, Wilson endpoint, Frobenius, and complementary weighted-factorial checks.",
        "bounds": {
            "exact_integer_degree": exact_degree,
            "odd_primes_other_than_5_max": max_prime,
            "prime_count": prime_count,
            "degrees_for_each_prime": "0<=d<p",
        },
        "identity_checks": {
            "reciprocal_q_initial_values_and_five_step": True,
            "h_convolution_and_five_step": True,
            "period_p_and_five_boundary_resets": True,
            "two_Wilson_endpoint_sums": True,
            "precise_complementary_unit_factors_at_u_and_v": True,
            "Frobenius_cases_modulo_5": sorted(residues_seen) == [1, 2, 3, 4],
            "quadratic_remainder_and_reverse_tail_formulas": True,
        },
        "finite_diagnostic": {
            "simultaneous_h_ideal_hits": hits,
            "interpretation": "A hit means a prime of F above p contains both h_d and h_(d-1).",
        },
        "scope_warning": (
            "The scans are finite diagnostics only.  The exact identities hold for every odd "
            "p != 5 by the companion proof, but they do not classify all zero pairs, prove "
            "support only over 19, or prove anything about the arithmetic nature of e+pi."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-degree", type=int, default=200)
    parser.add_argument("--max-prime", type=int, default=200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/algebraic_unit_two_log_n5_p_boundary_obstruction.json"),
    )
    args = parser.parse_args()
    result = run(args.exact_degree, args.max_prime)
    script = Path(__file__).resolve()
    source = script.parent.parent / "sources" / "algebraic_unit_two_log_n5_p_boundary_obstruction.md"
    result["script_sha256"] = file_sha256(script)
    result["source_sha256"] = file_sha256(source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
