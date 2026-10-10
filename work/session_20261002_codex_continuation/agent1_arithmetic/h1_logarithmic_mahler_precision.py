"""L17: bounded supporting checks for the proved h1 Mahler/carry law.

Only the already used primes 11 and 13 occur.  This does not scan Gram
unit criteria, recompute an atlas, or establish any theorem experimentally.
"""
from pathlib import Path
from fractions import Fraction
from math import comb, factorial
import json

BASE=Path(__file__).resolve().parent


def jets_mod(limit, modulus):
    a=[1];s=[1];d=[1];t=[0,1]
    for n in range(1,limit+1):
        a.append((n*a[-1]-(comb(n,2)*a[-2] if n>=2 else 0))%modulus)
        s.append((n*s[-1]-(comb(n,2)*s[-2] if n>=2 else 0)+1)%modulus)
        d.append((n*d[-1]+1)%modulus)
        if n<limit:t.append(((n+2)*t[-1]-n*t[-2]+s[n])%modulus)
    return a,s,d,t


def vp(n,p):
    if not n:return None
    ans=0
    while n%p==0:n//=p;ans+=1
    return ans


def floor_log(j,p):
    ans=0
    while j>=p:j//=p;ans+=1
    return ans


def exact_mahler(limit):
    alpha=[Fraction(1),Fraction(1)]
    for j in range(2,limit):alpha.append(alpha[-1]-alpha[-2]/2)
    prefix=Fraction(0);out=[0]
    for j in range(1,limit+1):
        prefix+=alpha[j-1]/j
        val=factorial(j)*prefix
        assert val.denominator==1
        out.append(val.numerator)
    return out


def run():
    out=[]
    for p in (11,13):
        chi=1 if p%4==1 else -1
        modulus=p**3
        limit=2*p+2*p**3
        a,s,d,t=jets_mod(limit,modulus)
        coeff=exact_mahler(4*p)
        for j,c in enumerate(coeff):
            direct=sum((-1)**(j-i)*comb(j,i)*t[i] for i in range(j+1))%modulus
            assert c%modulus==direct
            if j:
                actual=vp(c,p)
                bound=vp(factorial(j),p)-floor_log(j,p)
                assert actual is None or actual>=bound
                assert actual is None or actual+1>=floor_log(j,p)
                if j>=2*p:assert actual is None or actual>=floor_log(j,p)
        block=[coeff[p+r]%p for r in range(p)]
        assert block==[-chi*factorial(r)%p for r in range(p)]
        assert t[p]%p==-chi%p and t[0]==0
        rows=[];unit=0;zero=0
        for k in range(1,4):
            for n in range(2*p+1):
                for step in (1,2):
                    nn=n+p**k*step;pk=p**k
                    diff=(t[nn]-t[n])%pk
                    expected=(-p**(k-1)*step*chi*d[n])%pk
                    assert diff==expected
                    assert (s[nn]-s[n])%pk==(d[nn]-d[n])%pk==0
                    if d[n]%p:
                        unit+=1
                        assert vp(diff,p)==k-1
                    else:
                        zero+=1
                        assert diff==0
                    rows.append(dict(depth=k,index=n,step=step,D_mod_p=d[n]%p,
                                     difference_mod_pk=diff,expected_mod_pk=expected))
        # In a unit-D cell the next base-p digit is a bijection, not a
        # claim about the primes or about actual Gram endpoint content.
        cell=next(r for r in range(p) if d[r]%p)
        image=[t[cell+p*z]%p for z in range(p)]
        assert sorted(image)==list(range(p))
        out.append(dict(p=p,chi=chi,mahler_checked_through=4*p,
                        exceptional_block_mod_p=block,unit_difference_checks=unit,
                        zero_difference_checks=zero,cell=cell,cell_digit_image=image,
                        carry_rows=rows))
    dest=BASE/'H1_LOGARITHMIC_MAHLER_PRECISION_RECEIPT.json'
    dest.write_text(json.dumps(dict(
        status='AUTHOR bounded support for an all-depth proof; no new prime atlas or actual-q inference',
        primes_are_existing_receipt_primes=True,
        sequence='T_n=(e^z integral_0^z(1-z+z^2/2)^(-1)/(1-z))^(n)(0)',
        rows=out),indent=2)+'\n')
    print(json.dumps([dict(p=r['p'],mahler_through=r['mahler_checked_through'],
                           unit_checks=r['unit_difference_checks'],zero_checks=r['zero_difference_checks'],
                           cell=r['cell'],image=r['cell_digit_image']) for r in out],indent=2))


if __name__=='__main__':run()
