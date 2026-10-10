#!/usr/bin/env python3
"""Independent root audit for Item 245 (does not import its checker)."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


def trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    out = [0] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = ((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) % p
    return trim(out, p)


def scale(a, c, p):
    return trim([(c * x) % p for x in a], p)


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out, p)


def divmod_poly(a, b, p):
    rem = trim(a[:], p)
    b = trim(b[:], p)
    if b == [0]:
        raise ZeroDivisionError
    quo = [0] * max(1, len(rem) - len(b) + 1)
    lead_inv = pow(b[-1], -1, p)
    while rem != [0] and len(rem) >= len(b):
        shift = len(rem) - len(b)
        c = rem[-1] * lead_inv % p
        quo[shift] = c
        for j, y in enumerate(b):
            rem[shift + j] = (rem[shift + j] - c * y) % p
        rem = trim(rem, p)
    return trim(quo, p), rem


def power(a, n, p):
    out = [1]
    base = a
    while n:
        if n & 1:
            out = mul(out, base, p)
        base = mul(base, base, p)
        n //= 2
    return out


def binomial_poly(sign, exponent, spacing, p):
    out = [0] * (spacing * exponent + 1)
    for j in range(exponent + 1):
        out[spacing * j] = math.comb(exponent, j) * (sign ** j) % p
    return trim(out, p)


def harmonic_digits(p):
    a0 = [0] * p
    a1 = [0] * p
    b0 = [0] * (2 * p - 1)
    b1 = [0] * (2 * p - 1)
    harmonic = 0
    for k in range(1, p):
        inv = pow(k, -1, p)
        a0[k] = -inv % p
        a1[k] = harmonic * inv % p
        sign = 1 if k % 2 else -1
        b0[2 * k] = sign * inv % p
        b1[2 * k] = -sign * harmonic * inv % p
        harmonic = (harmonic + inv) % p
    return a0, a1, b0, b1


def kernel_numerator(p):
    a0, a1, b0, b1 = harmonic_digits(p)
    aa, ab, bb = mul(a0, a0, p), mul(a0, b0, p), mul(b0, b0, p)
    u2 = binomial_poly(-1, 2, p, p)
    u3 = binomial_poly(-1, 3, p, p)
    u4 = binomial_poly(-1, 4, p, p)
    v1 = binomial_poly(1, 1, 2 * p, p)
    v2 = binomial_poly(1, 2, 2 * p, p)
    terms = [
        scale(mul(mul(u3, v2, p), a1, p), 4, p),
        scale(mul(mul(u4, v1, p), b1, p), -3, p),
        scale(mul(mul(u2, v2, p), aa, p), 6, p),
        scale(mul(mul(u3, v1, p), ab, p), -12, p),
        scale(mul(u4, bb, p), 6, p),
    ]
    out = [0]
    for term in terms:
        out = add(out, term, p)
    return out, b0, bb


def p_poly(h, s, nu, p):
    r = 2 * h
    q = 2 * s - nu
    return mul(mul(binomial_poly(-1, r, 1, p),
                   binomial_poly(1, 1 + 3 * nu, 1, p), p),
               binomial_poly(1, q, 2, p), p)


def section(poly, p, a):
    if a >= len(poly):
        return [0]
    return trim([poly[a + j * p] for j in range((len(poly) - 1 - a) // p + 1)], p)


def remainder_q(poly, exponent, p):
    return divmod_poly(poly, power([1, 0, 1], exponent, p), p)[1]


def det_mod(matrix, p):
    a = [row[:] for row in matrix]
    answer = 1
    for c in range(len(a)):
        pivot = next((r for r in range(c, len(a)) if a[r][c] % p), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            answer = -answer
        pivot_value = a[c][c] % p
        answer = answer * pivot_value % p
        inv = pow(pivot_value, -1, p)
        for r in range(c + 1, len(a)):
            factor = a[r][c] * inv % p
            for j in range(c, len(a)):
                a[r][j] = (a[r][j] - factor * a[c][j]) % p
    return answer % p


def rank_mod(matrix, p):
    a = [row[:] for row in matrix]
    rank = 0
    for c in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][c] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][c], -1, p)
        a[rank] = [x * inv % p for x in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][c] % p:
                f = a[r][c] % p
                a[r] = [(x - f * y) % p for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def multiplication_matrix(state, p):
    modulus = power([1, 0, 1], 4, p)
    columns = []
    for j in range(8):
        rem = remainder_q([0] * j + state, 4, p)
        columns.append(rem + [0] * (8 - len(rem)))
    return [[columns[c][r] for c in range(8)] for r in range(8)]


def observation_matrix(p):
    out = []
    for m in range(8):
        row = []
        for j in range(8):
            d = m - j
            row.append(0 if d < 0 or d % 2 else
                       ((-1) ** (d // 2) * math.comb(d // 2 + 3, 3)) % p)
        out.append(row)
    return out


def matmul(a, b, p):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def primes(n):
    answer = []
    for x in range(2, n + 1):
        if all(x % q for q in range(2, math.isqrt(x) + 1)):
            answer.append(x)
    return answer


def rows(limit):
    for p in primes(limit):
        if p < 13:
            continue
        for s in range(1, (p - 7) // 6 + 1):
            rem = p - 6 * s - 3
            if rem > 0 and rem % 4 == 0:
                yield p, rem // 4, s


def main():
    checked = 0
    coordinates = 0
    rank_counts = {str(k): 0 for k in range(9)}
    samples = []
    cache = {}
    for p, h, s in rows(151):
        if p not in cache:
            cache[p] = kernel_numerator(p)
        rnum, b0, bb = cache[p]
        assert len(rnum) - 1 <= 8 * p - 1
        q4 = power([1, 0, 1], 4, p)
        obs = observation_matrix(p)
        assert det_mod(obs, p) == 1
        states = []
        for nu in (0, 1):
            q = 2 * s - nu
            a = p - q - 1
            poly = p_poly(h, s, nu, p)
            d = 2 * h + 4 * s + 1 + nu
            assert len(poly) - 1 == d
            assert d + q == p - 2 * h - 2 < p
            full = mul(rnum, poly, p)
            target = section(full, p, a)
            assert len(target) - 1 <= 7
            # c4 is the quotient after four divisions by Q, reduced mod Q.
            after_four = divmod_poly(target, q4, p)[0]
            assert remainder_q(after_four, 1, p) == [0]
            state = remainder_q(target, 4, p)
            state8 = state + [0] * (8 - len(state))
            alpha_beta = remainder_q(target, 1, p) + [0, 0]
            alpha, beta = alpha_beta[:2]
            short_product = mul(bb, poly, p)
            short_section = section(short_product, p, a)
            fast_alpha = sum(((-1) ** j) *
                             (short_section[2 * j] if 2 * j < len(short_section) else 0)
                             for j in range((len(short_section) + 1) // 2)) * -24 % p
            fast_beta = sum(((-1) ** j) *
                            (short_section[2 * j + 1] if 2 * j + 1 < len(short_section) else 0)
                            for j in range(len(short_section) // 2)) * -24 % p
            assert (alpha, beta) == (fast_alpha, fast_beta)
            b = p - 2 * h - 1
            reflected = section(short_product, p, b)
            left4 = short_section + [0] * (4 - len(short_section))
            right4 = reflected + [0] * (4 - len(reflected))
            assert left4 == list(reversed(right4))
            mult = multiplication_matrix(state8, p)
            terminal = matmul(obs, mult, p)
            norm = (alpha * alpha + beta * beta) % p
            assert det_mod(terminal, p) == pow(norm, 4, p)
            rank = rank_mod(terminal, p)
            rank_counts[str(rank)] += 1
            states.append((state8, rank, alpha, beta))
            coordinates += 1
        joint_rank = rank_mod(multiplication_matrix(states[0][0], p) +
                              multiplication_matrix(states[1][0], p), p)
        if joint_rank < 8:
            raise AssertionError((p, h, s, joint_rank))
        if (p, h, s) in {(29, 5, 1), (59, 2, 8), (149, 2, 23)}:
            samples.append({"row": [p, h, s], "states": states,
                            "joint_rank": joint_rank})
        checked += 1

    # Exhaustively test the universal determinant identity over three fields.
    universal_pairs = 0
    for p in (5, 7, 11):
        for alpha in range(p):
            for beta in range(p):
                state = [alpha, beta] + [0] * 6
                observed = matmul(observation_matrix(p), multiplication_matrix(state, p), p)
                assert det_mod(observed, p) == pow((alpha * alpha + beta * beta) % p, 4, p)
                universal_pairs += 1

    output = {
        "item": 245,
        "audit": "root-independent construction without importing Item245",
        "rows_through_151": checked,
        "coordinates": coordinates,
        "rank_counts": rank_counts,
        "universal_alpha_beta_pairs": universal_pairs,
        "samples": samples,
        "proved_checks": [
            "degree bound and c4=0",
            "full-numerator and B0^2P leading-pair equality",
            "section reciprocity",
            "observation determinant and joint rank",
        ],
    }
    path = Path(__file__).with_suffix(".json")
    payload = json.dumps(output, indent=2, sort_keys=True) + "\n"
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    print(json.dumps({"output": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                      "rows": checked, "coordinates": coordinates,
                      "universal_pairs": universal_pairs}, sort_keys=True))


if __name__ == "__main__":
    main()
