"""Independent, finite, exact main checks; no original code is executed."""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial as fac, gcd
from functools import reduce
import json
import time

BASE = Path(__file__).resolve().parent


def bareiss(matrix):
    a = [list(r) for r in matrix]
    n = len(a)
    if not n:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = a[i][j] * pivot - a[i][k] * a[k][j]
                assert value % prev == 0
                a[i][j] = value // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def derivative(a, n):
    return [x * fac(j) // fac(j - n) for j, x in enumerate(a) if j >= n]


def div_monic(a, b):
    rem = list(a)
    q = [0] * (len(a) - len(b) + 1)
    for j in range(len(q) - 1, -1, -1):
        q[j] = rem[j + len(b) - 1]
        for k, x in enumerate(b):
            rem[j + k] -= q[j] * x
    return q, rem


def valuation(x, p):
    assert x
    x = abs(x)
    out = 0
    while x % p == 0:
        out += 1
        x //= p
    return out


def inverse_column(a):
    n = len(a)
    aug = [list(row) + [F(int(i == 0))] for i, row in enumerate(a)]
    for k in range(n):
        r = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[r] = aug[r], aug[k]
        pivot = aug[k][k]
        aug[k] = [x / pivot for x in aug[k]]
        for i in range(n):
            if i != k:
                coefficient = aug[i][k]
                aug[i] = [x - coefficient * y for x, y in zip(aug[i], aug[k])]
    return [row[-1] for row in aug]


def tau(k):
    return F((-1) ** ((k - 1) // 2), k) if k > 0 and k % 2 else F(0)


def one_degree(n):
    x = []
    for k in range(n, 3 * n + 1):
        row = [fac(k) // fac(k - j) for j in range(n)]
        for j in range(n):
            value = fac(k) * tau(k - j)
            assert value.denominator == 1
            row.append(value.numerator)
        x.append(row)
    cofactors = [(-1) ** i * bareiss(x[:i] + x[i + 1:]) for i in range(len(x))]
    content = reduce(gcd, cofactors)
    assert content > 0
    w = [0] * n + [a // content for a in cofactors]
    assert reduce(gcd, w) == 1
    assert all(sum(w[n + i] * x[i][j] for i in range(2 * n + 1)) == 0 for j in range(2 * n))
    divisor = [0] * n + [(-1) ** (n - j) * comb(n, j) for j in range(n + 1)]
    v, rem = div_monic(w, divisor)
    assert not any(rem) and reduce(gcd, v) == 1
    b = []
    for j in range(n + 1):
        b.append(sum((-1) ** h * comb(n + h - 1, h) * fac(n + j + 2 * h) // fac(n + j) * w[2 * n + j + 2 * h]
                     for h in range((n - j) // 2 + 1)))
    assert reduce(gcd, b) == 1
    u = [b[j] * fac(n + j) for j in range(n + 1)]
    d = [comb(n, j // 2) if j % 2 == 0 else 0 for j in range(2 * n + 1)]
    s = mul(d, u)
    t = derivative(s, n)
    t_direct = [fac(n + r) * w[n + r] for r in range(2 * n + 1)]
    assert t == t_direct
    assert [F(a, fac(r)) for r, a in enumerate(t)] == derivative(w, n)
    qhat = [F(a, fac(n)) for a in t[::-1]]
    assert all(a.denominator == 1 for a in qhat)
    qhat = [a.numerator for a in qhat]
    pe = [sum(F(qhat[j], fac(k - j)) for j in range(k + 1)) for k in range(2 * n + 1)]
    pa = [sum(qhat[j] * tau(k - j) for j in range(k + 1)) for k in range(2 * n + 1)]
    assert all(a.denominator == 1 for a in pe + pa)
    pe, pa = [a.numerator for a in pe], [a.numerator for a in pa]
    z, numer = sum(qhat), sum(pe) + 4 * sum(pa)
    assert z
    g = gcd(z, numer)
    q_reduced = abs(z) // g
    p_reduced = numer * (1 if z > 0 else -1) // g
    border = sum(v[r] * sum(comb(n + j, j) * fac(n + r) // fac(n + r - j)
                           for j in range(n + r + 1)) for r in range(n + 1))
    assert border == sum(pe)
    acoeff = [sum(F(comb(n, h), fac(k - 2 * h)) for h in range(min(n, k // 2) + 1))
              for k in range(2 * n + 1)]
    a = [[acoeff[n + i - j] if n + i >= j else F(0) for j in range(n + 1)] for i in range(n + 1)]
    inv = inverse_column(a)
    qr = u[::-1]
    vend = sum(v)
    assert vend and v[-1]
    assert qr == [fac(n) * vend * t0 for t0 in inv]
    assert all(sum(a[i][j] * qr[j] for j in range(n + 1)) == (fac(n) * vend if i == 0 else 0)
               for i in range(n + 1))
    for j, t0 in enumerate(inv):
        hook_ratio = fac(2 * n - j) // (fac(j) * fac(n - j))
        difference = t0 / ((-1) ** j * hook_ratio) - 1
        assert gcd(difference.denominator, 2 * n) == 1 and difference.numerator % (2 * n) == 0
    assert gcd(vend, 2 * n) == 1
    assert all(v[j] % (2 * n) == 0 for j in range(n))
    assert (v[-1] - vend) % (2 * n) == 0
    assert (sum(pe) - vend) % (2 * n) == 0
    uc = reduce(gcd, u)
    for p in [2, 3, 5]:
        if (2 * n) % p == 0:
            assert valuation(uc, p) == valuation(fac(n), p)
            assert valuation(z, p) >= valuation(fac(n), p)
    if n == 1:
        assert w[n:] == [-2, 3, -1] and v == [2, -1]
        assert u == [3, -2] and qhat == [-6, 6, -2]
        assert (p_reduced, q_reduced) == (5, 2)
    if n == 2:
        assert content == 4 and w[n:] == [940, -1944, 1117, -162, 49]
        assert v == [940, -64, 49] and u == [-118, -972, 1176]
        assert qhat == [17640, -9720, 13404, -5832, 940]
        assert (z, sum(pe), sum(pa), numer) == (16432, 44641, 12852, 96049)
        assert (p_reduced, q_reduced) == (96049, 16432)
        moments = [F(49, 24), F(13, 6), F(5, 2), F(1), F(1)]
        assert sum(F(qr[i] * qr[j]) * moments[i + j] for i in range(3) for j in range(3)) == -218300
        assert 49 * 940 * 4 > 64 ** 2 and 2438 ** 2 > 2 * 1380 ** 2
        assert 4704 // 2 - 1380 - 2266 == -1294
    return {'n': n, 'cofactor_content': content, 'primitive_w': w[n:], 'V': v, 'U': u,
            'Z': z, 'N': numer, 'actual_reduced_pair': [p_reduced, q_reduced], 'controls_passed': True}


start = time.monotonic()
rows = [one_degree(n) for n in range(1, 7)]
out = {'reviewer': 'main Codex', 'degree_range': [1, 6], 'finite_control_only': True,
       'arithmetic': 'integers and exact rational numbers; Bareiss exact divisions asserted',
       'source_code_from_archive_executed': False, 'original_data_written': False,
       'all_index_theorems_proved_by_this_control': False, 'all_controls_passed': True,
       'elapsed_seconds': time.monotonic() - start, 'rows': rows}
(BASE / 'RAW_PRIMITIVE_DUAL_NORMALIZATION_MAIN_CONTROL.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in out.items() if k != 'rows'}, ensure_ascii=False))
