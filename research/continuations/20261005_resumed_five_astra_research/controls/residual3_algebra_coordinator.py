"""Bounded exact certificate for the new residual operator's building blocks.

This does not evaluate any original-size residual rank or actual unknown force.
"""
from math import factorial,comb
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).resolve().parent;MOD=243
PRE=[1]
for r in range(1,MOD):PRE.append(PRE[-1]*(r if r%3 else 1)%MOD)

def valuation_fact(n):
    v=0
    while n:n//=3;v+=n
    return v

def unit_fact(n):
    ans=1
    while n:
        ans=ans*(-1 if (n//MOD)%2 else 1)*PRE[n%MOD]%MOD
        n//=3
    return ans

def main():
    for n in range(1001):
        exact=factorial(n)//3**valuation_fact(n)%MOD
        assert exact==unit_fact(n),n
    betacount=0
    for p in range(41):
        for s in range(41):
            den=1
            for a in range(p+1):den*=2*s+2*a+1
            beta=Q((-1)**p*2**p*factorial(p),den)
            other=Q((-1)**p*2**(2*p+1)*factorial(p)*factorial(s+p+1)*factorial(2*s),
                    factorial(2*s+2*p+2)*factorial(s))
            assert beta==other,(p,s)
            numargs=[p,s+p+1,2*s];denargs=[2*s+2*p+2,s]
            depth=sum(map(valuation_fact,numargs))-sum(map(valuation_fact,denargs))
            scale=max(0,-depth)
            numerator=(-1)**p*pow(2,2*p+1,MOD)
            denominator=1
            for nn in numargs:numerator=numerator*unit_fact(nn)%MOD
            for nn in denargs:denominator=denominator*unit_fact(nn)%MOD
            got=numerator*pow(denominator,-1,MOD)*pow(3,depth+scale,MOD)%MOD
            scaled=beta*3**scale
            assert scaled.denominator%3
            exp=scaled.numerator*pow(scaled.denominator,-1,MOD)%MOD
            assert got==exp,(p,s,got,exp)
            betacount+=1
    low=0;high=0
    for D in range(1,9):
        for r1 in range(20,29):
            L=sp.Matrix(D,D,lambda a,b: (-1)**(D-1-a-b)*comb(r1+D-1-a-b,D-1-a-b) if a+b<=D-1 else 0)
            R=sp.Matrix(D,D,lambda a,b:comb(r1+1,a+b-D+1) if a+b>=D-1 else 0)
            assert L*R==sp.eye(D)
            low+=1
    for A in range(1,13):
        for d in range(5):
            for extra in range(9):
                m=d+extra;rstar=A+d+m
                def ec(a,b):
                    k=rstar-a-b
                    return (-1)**(A-k)*comb(A,k) if 0<=k<=A else 0
                def rc(a,b):
                    k=d+m-a-b
                    return comb(A+k-1,k) if k>=0 else 0
                E=sp.Matrix(extra+1,extra+1,lambda i,j:ec(i+d,j+d))
                R=sp.Matrix(extra+1,extra+1,lambda i,j:rc(i+d,j+d))
                assert E*R==sp.eye(extra+1),(A,d,m)
                # Test the finite inverse words on a synthetic integral perturbation.
                T=sp.Matrix(extra+1,extra+1,lambda i,j:3*(i+j+1))
                for length,mod in ((4,81),(5,243)):
                    S=sp.zeros(extra+1);term=R.copy()
                    for _ in range(length):
                        S+=term;term=-R*T*term
                    rem=(E+T)*S-sp.eye(extra+1)
                    assert all(int(value)%mod==0 for value in rem),(A,d,m,length)
                high+=1
    report={'status':'EXACT_RESIDUAL_BUILDING_BLOCK_PASS','factorial_unit_arguments_checked':1001,
            'beta_exact_and_scaled_residue_checks':betacount,'low_integral_inverse_checks':low,
            'high_integral_inverse_and_neumann_checks':high,
            'scope':'Bounded algebra and implementation checks only. New Schur/degree transfer requires mathematical review; original-family D6 rank, endpoint coupling and q-depth not evaluated.'}
    (OUT/'residual3_algebra_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

if __name__=='__main__':main()
