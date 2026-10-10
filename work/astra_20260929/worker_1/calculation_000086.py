from pathlib import Path
from fractions import Fraction as F
from math import factorial, inf
import hashlib, json

root = Path('[private local path removed]')
paths = list((root / 'work/astra_review_registry/candidates').glob('worker2-b2-ternary-residue-two-*.md'))
assert len(paths) == 1, [str(p) for p in paths]
data = paths[0].read_bytes()
file_hash = hashlib.sha256(data).hexdigest()
assert file_hash == '2ce6f3898cad017fe32a406a1eafc2e677370643e34c2ce8db41aadf14415e55'
start = data.index(b'STATUS: Unverified author derivation submitted for independent review.')
expected = 'ba51fc9529c4fe1ea78ad46225229d224dc4c5ac36b4b80e067017230642ce38'
variants = [data[start:], data[start:].rstrip(b'\r\n'), data[start:].rstrip(b'\r\n') + b'\n']
matched = [p for p in variants if hashlib.sha256(p).hexdigest() == expected]
assert matched, 'Candidate payload hash did not match'
print(json.dumps({'file_sha256': file_hash, 'payload_sha256': expected, 'payload_offset': start, 'payload_bytes': len(matched[0])}))

def vp(x):
    x = F(x)
    if not x:
        return inf
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % 3 == 0:
        a //= 3
        v += 1
    while b % 3 == 0:
        b //= 3
        v -= 1
    return v

def residue(x):
    x = F(x)
    assert x.denominator % 3
    return x.numerator * pow(x.denominator, -1, 3) % 3

def power_coefficients(h):
    out = [1]
    for unused in range(h):
        new = [0] * (len(out) + 2)
        for j, c in enumerate(out):
            new[j] += c
            new[j + 1] -= 2 * c
            new[j + 2] += 2 * c
        out = new
    return out

def polynomials(h, fac):
    u = power_coefficients(h)
    leg = [F(fac[h + d] * u[h + d], fac[h] * fac[d]) for d in range(h + 1)]
    aux = [F(fac[h] * u[h - d], fac[d] * (1 << (h - d))) for d in range(h + 1)]
    assert all(c.denominator == 1 for c in leg + aux)
    return u, [int(c) for c in leg], [int(c) for c in aux]

def auxiliary_values(poly):
    h = sum(poly)
    hp = sum(j * c for j, c in enumerate(poly))
    hpp = sum(j * (j - 1) * c for j, c in enumerate(poly))
    degree = len(poly) - 1
    return h, hp, hpp, degree * h + hp, degree * (degree - 1) * h + 2 * degree * hp + hpp

def quotient_moment(poly, moments):
    tail = 0
    total = F(0)
    for d in range(len(poly) - 2, -1, -1):
        tail += poly[d + 1]
        total += tail * moments[d]
    return total

def endpoint_digit_residue(j):
    out = 1
    while j:
        if j % 3:
            out = 2 * out % 3
        j //= 3
    return out

samples = [5, 8, 11, 26, 80]
results = []
term_checks = 0
coefficient_checks = 0
for n in samples:
    m = n + 1
    fac = [factorial(j) for j in range(2 * m + 1)]
    t, r = vp(m), vp(fac[n])
    un, pn, hnpoly = polynomials(n, fac)
    um, pm, hmpoly = polynomials(m, fac)
    hn, hnp, hnpp, jn, kn = auxiliary_values(hnpoly)
    hm, hmp, hmpp, jm, km = auxiliary_values(hmpoly)

    for j, c in enumerate(hnpoly):
        target = {n: 1, n - 1: -1, n - 2: 1}.get(j, 0)
        assert (c - target) % 3 == 0
        coefficient_checks += 1
    assert hn % 3 == 1 and jn % 3 == 0
    assert vp(hm - 1) >= 2 * t - 1
    assert vp(hmp - m) >= 2 * t
    assert vp(hmpp - m * (m - 1)) >= 2 * t
    assert vp(jm - 2 * m) >= 2 * t
    assert vp(km - 2 * m * (m - 1)) >= 2 * t
    assert residue(F(jm, m)) == 2 and residue(F(km, m)) == 1

    # Independently reconstruct derivatives from the original double sum.
    direct = [F(fac[m], fac[m - j]) for j in range(3)]
    for B in range(m + 1):
        for Cc in range((m - B) // 2 + 1):
            ell, k = B + Cc, B + 2 * Cc
            if ell == 0:
                continue
            for j in range(3):
                if k + j > m:
                    continue
                term = F((-1) ** B * (fac[m] // fac[m - k - j]) * (fac[m] // fac[m - ell]), (1 << Cc) * fac[B] * fac[Cc])
                bound = 2 * t + (k + j - 1) // 3 - vp(ell)
                assert vp(term) >= bound, (n, B, Cc, j, vp(term), bound)
                direct[j] += term
                term_checks += 1
    assert direct == [hm, hmp, hmpp]

    a, b = sum(pn), sum(pm)
    assert a % 3 == endpoint_digit_residue(n)
    assert b % 3 == endpoint_digit_residue(m)
    assert vp(a) == vp(b) == 0
    S = jm * jm - hm * km
    C = (jm - hm) * jn - (km - jm) * hn
    W = jm * jn - km * hn
    assert vp(C) >= 1
    assert vp(S) == vp(W) == t
    assert residue(F(S, m)) == residue(F(W, m)) == 2
    D = m * m * b * C - 2 * a * S
    assert D and vp(D) == t
    assert residue(F(D, m)) == 2 * a % 3

    e = [1]
    for j in range(1, 2 * m):
        e.append(j * e[-1] + 1)
    assert all(e[j] % 3 == (1 if j % 3 == 0 else 2) for j in range(len(e)))
    Tn = sum((F(c * e[n + d], fac[n + d]) for d, c in enumerate(pn)), F(0))
    Tm = sum((F(c * e[n + d], fac[n + d]) for d, c in enumerate(pm)), F(0))
    f = F(1 << n, fac[n] ** 2)
    normalized_n = sum((F(fac[n] * un[n + d] * e[n + d], fac[d] * (1 << n)) for d in range(n + 1)), F(0))
    normalized_m = sum((F(fac[n] * (m + d) * um[m + d] * e[n + d], fac[d] * (1 << n) * m) for d in range(m + 1)), F(0))
    assert Tn / f == normalized_n and Tm / f == normalized_m
    assert un[2 * n] == 1 << n
    assert un[2 * n - 1] == -n * (1 << n)
    assert un[2 * n - 2] == n * n * (1 << (n - 1))
    assert vp(normalized_n) >= 1
    assert vp(m * m * normalized_m) >= t
    boundary = F(m * fac[n] * (2 * m) * um[2 * m] * e[2 * n + 1], (1 << n) * fac[m])
    assert boundary == 4 * m * e[2 * n + 1]
    for d in range(n + 1):
        term = F(m * fac[n] * (m + d) * um[m + d] * e[n + d], (1 << n) * fac[d])
        assert vp(term) >= t

    # Exact monomial moments via integer real and imaginary parts of (1+i)^k.
    moments = []
    real, imag = 1, 0
    for d in range(n + 1):
        real, imag = real - imag, real + imag
        moments.append(F(2 * imag, (1 << d) * (d + 1)))
    wn = quotient_moment(pn, moments)
    wm = quotient_moment(pm, moments)
    L, power = 0, 1
    while 3 * power <= m:
        power *= 3
        L += 1
    assert r >= L >= 1
    assert vp(wn) >= -L and vp(wm) >= -L
    assert vp(wn / f) >= 2 * r - L
    assert vp(m * m * wm / f) >= 2 * t + 2 * r - L
    Pstar, Ustar = wn + Tn, wm + Tm
    assert vp(Pstar / f) >= 1
    assert vp(m * m * Ustar / f) >= t

    numerator_terms = [2 * Pstar * S, -m * m * Ustar * C, -2 * f * hm * W]
    X = sum(numerator_terms, F(0))
    N = X / f
    assert vp(numerator_terms[0] / f) >= t + 1
    assert vp(numerator_terms[1] / f) >= t + 1
    assert vp(numerator_terms[2] / f) == t
    assert X and N and vp(N) == t
    assert residue(N / m) == 2
    ratio = X / D
    q = ratio.denominator
    assert vp(X) == t - 2 * r
    assert vp(q) == 2 * r
    assert residue(N / m) * pow(residue(F(D, m)), -1, 3) % 3 == pow(a % 3, -1, 3)
    results.append({'n': n, 't': t, 'r': r, 'v3_D': vp(D), 'v3_N': vp(N), 'v3_X': vp(X), 'v3_q': vp(q), 'D_over_m_mod3': residue(F(D, m)), 'N_over_m_mod3': residue(N / m)})

# Independent endpoint recurrence checks the digit rule over the full bounded range.
endpoints = [1, 2]
for j in range(1, max(samples) + 1):
    num = (4 * j + 2) * endpoints[j] + 4 * j * endpoints[j - 1]
    assert num % (j + 1) == 0
    endpoints.append(num // (j + 1))
assert all(a % 3 == endpoint_digit_residue(j) for j, a in enumerate(endpoints))
print(json.dumps({'samples': results, 'individual_auxiliary_term_checks': term_checks, 'auxiliary_coefficient_checks': coefficient_checks, 'endpoint_digit_checks': len(endpoints), 'all_assertions_passed': True}))