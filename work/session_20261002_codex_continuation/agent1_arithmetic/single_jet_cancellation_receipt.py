"""Bounded exact examples; no radius claim is inferred from these checks."""
import hashlib
import json
from fractions import Fraction
from math import comb, factorial, gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent/'main'/'EXPLICIT_DEGREE61_RADIUS198_CERTIFICATE.json'


def compose_jets(pj, maxn):
    h = [0]*maxn
    h[0] = 2
    for j in range(1,min(len(pj),maxn)):
        h[j] -= 2*pj[j]
    nz = [j for j in range(1,min(len(pj),maxn)) if pj[j]]
    for i in nz:
        for j in nz:
            if i+j < maxn:
                h[i+j] += comb(i+j,i)*pj[i]*pj[j]
    g = [0]
    for n in range(1,maxn+1):
        z = (4*pj[n] if n<len(pj) else 0)-sum(
            comb(n-1,k)*h[k]*g[n-k] for k in range(1,n)
        )
        assert z%2 == 0
        g.append(z//2)
    return g


def main():
    raw = SRC.read_bytes()
    cert = json.loads(raw)
    kj = [int(k) for k in cert['endpoint_basis_integers']]
    pj = [0]*(len(kj)+2)
    pj[1] = 1
    for j,k in enumerate(kj,1):
        pj[j] += k
        pj[j+1] -= (j+1)*k
    g = compose_jets(pj,240)
    records = []
    for n in (80,120,180,240):
        fact = factorial(n)
        f = n-n.bit_count()
        O = fact>>f
        old = sum((Fraction(1+g[j],factorial(j))
                   for j in range(1,n+1)),Fraction(1))
        Z = old*fact
        assert Z.denominator==1
        Z = Z.numerator
        assert Z%2==1
        K = (-Z*pow(2,-1,O))%O if O>1 else 0
        if 2*K>O:
            K -= O
        assert 2*abs(K)<O
        newpj = pj+[0]*max(0,n+2-len(pj))
        newpj[n] += K
        newpj[n+1] -= (n+1)*K
        assert sum((Fraction(newpj[j],factorial(j))
                    for j in range(len(newpj))),Fraction(0))==1
        newg = compose_jets(newpj,n)
        assert newg[:-1]==g[:n]
        assert newg[n]-g[n]==2*K
        new = sum((Fraction(1+newg[j],factorial(j))
                   for j in range(1,n+1)),Fraction(1))
        assert new==old+Fraction(2*K,fact)
        L = (Z+2*K)//O
        assert (Z+2*K)%O==0 and L%2==1
        assert new==Fraction(L,1<<f)
        assert new.denominator==1<<f
        assert gcd(Z+2*K,fact)==O
        alpha = Fraction(abs(K),O)
        norms = {}
        for r in (Fraction(19,10),Fraction(21,10)):
            a = Fraction(abs(K),fact)*r**n*(1+r)
            b = (1+r)*alpha*(1<<n.bit_count())*(r/2)**n
            assert a==b
            norms[str(r)] = str(a)
        records.append(dict(N=n, K=str(K), alpha=str(alpha),
                            old_q=str(old.denominator), new_p=str(new.numerator),
                            new_q=str(new.denominator), odd_factorial=str(O),
                            full_endpoint_gcd=str(gcd(Z+2*K,fact)),
                            perturbation_norms=norms,
                            new_P_jets_sha256=hashlib.sha256(str(newpj).encode()).hexdigest()))
    out = HERE/'SINGLE_JET_CANCELLATION_RECEIPT.json'
    result = dict(status='PASS_FOUR_BOUNDED_EXACT_CANCELLATIONS',
                  scope='Arithmetic checks only; no finite modified-polynomial radius certification',
                  source=str(SRC), source_sha256=hashlib.sha256(raw).hexdigest(),records=records)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'])
    print([(r['N'],len(r['old_q']),len(r['new_q'])) for r in records])


if __name__=='__main__':
    main()
