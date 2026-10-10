"""L20: integer determinant terms, one counterexample, one complete-q node.

The proof is symbolic and all-prime. This is deliberately not a prime atlas.
The bounded examples neither imply a distribution law nor an error estimate.
"""
from pathlib import Path
from math import factorial
from hashlib import sha256
import json
from reflected_actual_five_denominator import coeff0,coeff1,fall,valuation,actual_center

BASE=Path(__file__).resolve().parent


def integer_determinant(r):
    if r==0:return dict(r=0,Z=1,special_zero_residue=True)
    d=coeff0(r,r,r);c=coeff1(r,r-1)
    A=sum(c[j]*fall(r-1,j) for j in range(r))
    B=sum((c[j]+(c[j-1] if j else 0))*fall(r-1,j) for j in range(r))
    X=sum(d[j]*fall(r,j) for j in range(r+1))
    Y=sum(d[j-1]*fall(r,j) for j in range(1,r+1))
    return dict(r=r,Z=B*X-A*Y,A=A,B=B,X=X,Y=Y,
                d=d,c=c,prime_independent_integer_definition=True)


def counterexample():
    p=13;n=156;h=28;N=n+h;L=h-1;eps=(-1)**h
    assert n%(p*(p-1))==0 and h>=p+1 and N%p==2
    d=coeff0(N,h,N);c=coeff1(N,L);T=factorial(L)
    R0=d[N]-eps*c[L]
    R1=d[N-1]-eps*(c[L]+c[L-1])
    M0=eps*sum(c[j]*fall(L,j) for j in range(L+1))
    M1=eps*sum((c[j]+(c[j-1] if j else 0))*fall(L,j) for j in range(L+1))
    m0=M0-T*R0;m1=M1-T*R1
    E0=sum(d[j]*fall(N,j) for j in range(N+1))
    E1=sum(d[j-1]*fall(N,j) for j in range(1,N+1))
    E=m1*E0-m0*E1
    assert E%p==integer_determinant(2)['Z']%p==0
    assert (1-2*(N%p)**2)%p!=0
    return dict(p=p,n=n,h=h,N=N,N_modp=N%p,E_modp=E%p,
                exact_full_E_vp=valuation(E,p),
                alleged_p5_formula_modp=(1-2*(N%p)**2)%p,
                character_minus_one=1,
                full_integer_E_sha256=sha256(str(E).encode()).hexdigest(),
                no_actual_q_inferred_from_E_zero=True)


def complete_simultaneous_node():
    # n divisible lcm(4,3*2,5*4)=60; N=2^8 is1 at both primes.
    raw=actual_center(60,256,include_integer_state=True)
    st=raw.pop('integer_state');N=raw['N'];h=raw['h'];n=raw['n']
    rows=[]
    for p in (3,5):
        assert n%(p*(p-1))==0 and N%p==1 and h>=p+1
        assert st['E']*((-1)**h)%p==p-1
        vf=valuation(factorial(N),p);vu=valuation(st['U'],p)
        logp=0;power=p
        while power<=N:logp+=1;power*=p
        assert valuation(st['Pi'],p)>=-logp
        assert valuation(st['center'],p)==-vf-vu
        assert valuation(st['q'],p)==vf+vu
        rows.append(dict(p=p,E_over_sign_modp=st['E']*((-1)**h)%p,
                         N_factorial_vp=vf,U_vp=vu,Pi_vp=valuation(st['Pi'],p),
                         actual_q_vp=valuation(st['q'],p),
                         exact_full_final_gcd_retained=True))
    raw['simultaneous_odd_prime_rows']=rows
    raw['fixed_modulus']=60
    raw['final_num_sha256']=sha256(str(st['full_num']).encode()).hexdigest()
    raw['final_den_sha256']=sha256(str(st['full_den']).encode()).hexdigest()
    return raw


def run():
    terms=[integer_determinant(r) for r in range(5)]
    assert [x['Z'] for x in terms]==[1,-1,13,-197,19289]
    out=dict(status='AUTHOR bounded exact support for symbolic all-p theorem; no atlas',
             integer_determinants=terms,
             p13_counterexample=counterexample(),
             complete_simultaneous_node=complete_simultaneous_node(),
             proof_scope='p|n,h>=p+1; residue unit and N>=2p imply complete actual q equality',
             no_error_or_distribution_inferred_from_experiments=True)
    (BASE/'REFLECTED_UNIVERSAL_PRIME_RESIDUE_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':run()
