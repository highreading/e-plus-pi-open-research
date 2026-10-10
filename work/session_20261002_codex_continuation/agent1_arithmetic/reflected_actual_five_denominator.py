"""L19: exact five-residue certificate plus bounded COMPLETE center gcds.

No prime atlas.  No numerical error estimate is asserted.  The theorem uses
the finite residue reduction and strict valuation comparison in its note.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial,comb,gcd
from hashlib import sha256
import json

BASE=Path(__file__).resolve().parent


def valuation(x,p):
    if x==0:return None
    if isinstance(x,Fraction):
        return valuation(x.numerator,p)-valuation(x.denominator,p)
    ans=0
    while x%p==0:x//=p;ans+=1
    return ans


def fall(a,j):
    ans=1
    for k in range(j):ans*=a-k
    return ans


def coeff0(N,h,limit):
    d=[1]
    for j in range(limit):
        val=(h-2*N+3*j)*d[j]
        if j>=1:val+=(6*N-2*h-4*(j-1))*d[j-1]
        if j>=2:val+=(2*h-4*N+2*(j-2))*d[j-2]
        assert val%(j+1)==0
        d.append(val//(j+1))
    return d


def coeff1(N,limit):
    c=[1]
    for j in range(limit):
        val=(N-1-3*j)*c[j]
        if j>=1:val+=(4*N-2-4*(j-1))*c[j-1]
        if j>=2:val+=(2*N-2-2*(j-2))*c[j-2]
        assert val%(j+1)==0
        c.append(val//(j+1))
    return c


def residue_row(R):
    # Representatives N=h=R+5 keep h positive and preserve all coefficients
    # through degree4, while L mod5 is R-1 and T is divisible5.
    N=h=R+10;L=h-1
    d=coeff0(N,h,4);c=coeff1(N,4)
    M0=sum(c[j]*fall(L,j) for j in range(5))%5
    M1=sum((c[j]+(c[j-1] if j else 0))*fall(L,j) for j in range(5))%5
    E0=sum(d[j]*fall(N,j) for j in range(5))%5
    E1=sum(d[j-1]*fall(N,j) for j in range(1,5))%5
    E=(M1*E0-M0*E1)%5
    assert E==(1-2*R*R)%5 and E!=0
    return dict(N_mod5=R,h_mod5=R,L_mod5=(R-1)%5,
                d_low_mod5=[x%5 for x in d],c_low_mod5=[x%5 for x in c],
                M0_over_sign=M0,M1_over_sign=M1,E0=E0,E1=E1,E_over_sign=E)


def imag_powers(real,imag,limit):
    a,b=1,0;out=[0]
    for _ in range(limit):a,b=a*real-b*imag,a*imag+b*real;out.append(b)
    return out


def actual_center(n,N,include_integer_state=False):
    h=N-n;L=h-1;eps=(-1)**h;T=factorial(L)
    d=coeff0(N,h,N);c=coeff1(N,L)
    assert d[0]==c[0]==1
    # Exact finite binomial formula checks at just selected small indices.
    for j in sorted({0,1,2,3,4,N-1,N}):
        value=(-1)**j*sum(comb(N,ell)*comb(N+n-2*ell,j-2*ell)
                         for ell in range(j//2+1))
        assert d[j]==value
    for j in sorted({0,1,2,3,4,L-1,L}):
        value=sum(comb(N,ell)*comb(N-1-2*ell,j-2*ell)
                  for ell in range(j//2+1))
        assert c[j]==value
    R0=d[N]-eps*c[L]
    R1=d[N-1]-eps*(c[L]+(c[L-1] if L else 0))
    M0=eps*sum(c[j]*fall(L,j) for j in range(L+1))
    M1=eps*sum((c[j]+(c[j-1] if j else 0))*fall(L,j) for j in range(L+1))
    m0=M0-T*R0;m1=M1-T*R1;U=M1*R0-M0*R1
    assert U>0
    E0=sum(d[j]*fall(N,j) for j in range(N+1))
    E1=sum(d[j-1]*fall(N,j) for j in range(1,N+1))
    E=m1*E0-m0*E1
    assert E%2==1 and E%5!=0
    k=[]
    for j in range(n+1):
        k.append((-1)**j*sum(Fraction(comb(N,b)*comb(n-b,j-2*b),2**b)
                            for b in range(j//2+1)))
    pp=[]
    for ell in range(n+1):
        val=eps*2**N*(m1*(k[n-1-ell] if ell<n else 0)-m0*k[n-ell])
        assert val.denominator==1
        pp.append(val.numerator)
    pos=imag_powers(1,1,n+1)
    neg0=imag_powers(1,-1,N)
    neg1=imag_powers(-1,-1,L)
    Pi=4*sum((Fraction(pp[ell]*pos[ell+1],2**(ell+1)*(ell+1))
              for ell in range(n+1)),Fraction(0))
    for t in range(1,N+1):
        z=m1*d[N-t]-m0*(d[N-t-1] if t<N else 0)
        Pi-=Fraction(4*z*neg0[t],t)
    for t in range(1,L+1):
        j=L-t
        z=eps*(m1*c[j]-m0*(c[j]+(c[j-1] if j else 0)))
        Pi-=Fraction(4*z*neg1[t],t)
    numerator=Fraction(E,factorial(N))+Pi
    center=-numerator/U
    q=center.denominator
    # Retain and independently compare the FINAL cleared gcd identity.
    ON=1
    for j in range(1,N+1,2):ON=ON*j//gcd(ON,j)
    assert (ON*Pi).denominator==1
    full_den=factorial(N)*ON*U
    full_num=ON*E+factorial(N)*(ON*Pi).numerator
    content=gcd(full_den,full_num)
    assert q==full_den//content
    vf=valuation(factorial(N),5);vu=valuation(U,5)
    log5=0;power=5
    while power<=N:log5+=1;power*=5
    assert valuation(Pi,5)>=-log5
    assert valuation(numerator,5)==-vf
    assert valuation(q,5)==vf+vu
    assert valuation(q,2)==N and valuation(U,2)==1
    result=dict(n=n,N=N,h=h,N_factorial_v5=vf,U_v5=vu,E_mod5=E%5,
                Pi_v5=valuation(Pi,5),complete_numerator_v5=valuation(numerator,5),
                actual_q_v5=valuation(q,5),actual_q_v2=valuation(q,2),U_v2=valuation(U,2),
                final_q_bit_length=q.bit_length(),final_content_bit_length=content.bit_length(),
                final_cleared_gcd_verified=True,
                q_sha256=sha256(str(q).encode()).hexdigest(),
                coefficient_prefix_sign='epsilon=(-1)^h retained',
                no_approximation_error_inferred=True)
    if include_integer_state:
        result['integer_state']=dict(U=U,E=E,Pi=Pi,q=q,center=center,
                                     full_den=full_den,full_num=full_num,content=content)
    return result


def run():
    table=[residue_row(R) for R in range(5)]
    examples=[actual_center(n,N) for n,N in ((20,64),(20,128),(40,512))]
    out=dict(status='AUTHOR finite5-residue proof certificate and three bounded COMPLETE-q checks; no experiment is an infinite theorem',
             residue_rows=table,complete_center_examples=examples,
             target='n divisible20,h>=6 actual q5; power2 N dyadic/correction compatibility')
    (BASE/'REFLECTED_ACTUAL_FIVE_DENOMINATOR_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':run()
