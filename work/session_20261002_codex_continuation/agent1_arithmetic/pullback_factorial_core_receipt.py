"""Bounded exact author examples of the proved support/core normalization.

Read the root's endpoint-basis integers; do not modify its certificate or
independently audit its analytic radius. This script checks our new arithmetic
identities on the same fixed polynomial for N<=240. Finite examples are not
used as proof of the all-order theorem.
"""
import hashlib
import json
from fractions import Fraction
from math import comb, factorial, gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT_CERT = HERE.parent / 'main' / 'EXPLICIT_DEGREE61_RADIUS198_CERTIFICATE.json'


def primes(n):
    a = [True] * (n+1)
    a[:2] = [False, False]
    for j in range(2, n+1):
        if a[j]:
            yield j
            for k in range(j*j, n+1, j):
                a[k] = False


def val(a, p):
    if not a:
        return None
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def vp_fact(n, p):
    v = 0
    while n:
        n //= p
        v += n
    return v


def digest(a):
    return hashlib.sha256(str(a).encode()).hexdigest()


def main():
    src = ROOT_CERT.read_bytes()
    cert = json.loads(src)
    K = [int(k) for k in cert['endpoint_basis_integers']]
    d = len(K)+1
    P = [Fraction(0) for _ in range(d+1)]
    P[1] = Fraction(1)
    for j, k in enumerate(K, 1):
        P[j] += Fraction(k, factorial(j))
        P[j+1] -= Fraction(k, factorial(j))
    assert sum(P) == 1
    pj = [int(P[j]*factorial(j)) for j in range(d+1)]
    assert all(P[j]*factorial(j) == pj[j] for j in range(d+1))
    den = lcm(*(x.denominator for x in P))
    support = {2} | {p for p in primes(d) if den % p == 0}
    h = [2] + [
        sum(comb(j,k)*pj[k]*pj[j-k]
            for k in range(max(0,j-d), min(d,j)+1))
        - (2*pj[j] if j <= d else 0)
        for j in range(1, 2*d+1)
    ]
    gj = [0]
    gamma = Fraction(0)
    A = 1
    fact = 1
    records = []
    all_primes = list(primes(240))
    for n in range(1, 241):
        order = n-1
        num = (4*pj[n] if n <= d else 0) - sum(
            comb(order,k)*h[k]*gj[n-k]
            for k in range(1, min(2*d,order)+1)
        )
        assert num % 2 == 0
        gj.append(num//2)
        assert gj[n] % 2 == 0
        fact *= n
        A = n*A+1
        gamma += Fraction(gj[n], fact)
        B = gamma*fact
        assert B.denominator == 1
        B = B.numerator
        assert B % 2 == 0
        E = Fraction(A, fact)
        total = E+gamma
        q = total.denominator
        Q = E.denominator
        M = 1
        for p in all_primes:
            if p > n:
                break
            v = vp_fact(n,p) if p in support else 0
            if p not in support:
                u = p
                while u <= n:
                    v += 1
                    u *= p
            M *= p**v
        assert fact % M == 0
        F = fact//M
        assert M % gamma.denominator == 0
        assert B % F == 0
        assert gcd(A+B,F) == gcd(A,F)
        core = F//gcd(A,F)
        assert q % core == 0
        assert q*M % Q == 0 and Q*M % q == 0
        if n % 2 == 0:
            assert val(q,2) == vp_fact(n,2)
        for p in all_primes:
            if p > n:
                break
            if p in support:
                continue
            f = vp_fact(n,p)
            ell = 0
            u = p
            while u <= n:
                ell += 1
                u *= p
            a = val(A,p)
            if a < f-ell:
                assert val(q,p) == f-a
            else:
                assert val(q,p) <= ell
        if n in (20,61,80,120,180,240):
            records.append(dict(
                N=n, q=str(q), q_e=str(Q), q_log=str(gamma.denominator),
                M=str(M), F=str(F), surviving_core=str(core),
                actual_gcd=str(gcd(A+B,fact)), exponential_gcd=str(gcd(A,fact)),
                A_sha256=digest(A), B_sha256=digest(B), Z_sha256=digest(A+B),
                v2_q=val(q,2), v2_factorial=vp_fact(n,2),
            ))
    receipt = dict(
        status='PASS_BOUNDED_AUTHOR_ARITHMETIC_IDENTITIES',
        scope='N=1..240 of fixed degree61 P; no analytic radius audit; no infinite theorem from examples',
        source_path=str(ROOT_CERT), source_sha256=hashlib.sha256(src).hexdigest(),
        degree=d, monomial_common_denominator=str(den),
        denominator_prime_support=sorted(support),
        P_jets_sha256=digest(pj), G_jets_0_240_sha256=digest(gj),
        identities=['den(G_N)|M_N','F_N|B_N','gcd(Z_N,F_N)=gcd(A_N,F_N)',
                    'core_N|q_N','Q_N|q_N M_N','q_N|Q_N M_N',
                    'all good-prime local alternatives','even N: v2(q_N)=v2(N!)'],
        records=records,
    )
    out = HERE/'POLYNOMIAL_PULLBACK_FACTORIAL_CORE_RECEIPT.json'
    out.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','degree','denominator_prime_support')},indent=2))
    print('Saved', out)


if __name__ == '__main__':
    main()
