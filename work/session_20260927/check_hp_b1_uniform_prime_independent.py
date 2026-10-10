"""Independent exact scalar seeds on the assigned six primes and two germs."""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
PRIMES = (5, 7, 11, 13, 17, 19)

def phi_coefficient(k, degree):
    ans = F(0)
    for c in range(degree//2+1):
        b = degree-2*c
        if b+c <= k:
            ans += F((-1)**b * factorial(k),
                     factorial(k-b-c)*factorial(b)*factorial(c)*2**c)
    return ans

def H_derivative(k, d):
    return sum((F(factorial(k), factorial(k-d-r))*phi_coefficient(k,r)
                for r in range(k-d+1)), F(0)) if d <= k else F(0)

def legendre_integer_coefficients(k):
    # Explicit ordinary Legendre binomial formula after its complex change
    # of variable; neither the author's recurrence nor Rodrigues code is used.
    coefficients = [0]*(k+1)
    for j in range(k//2+1):
        e = k-2*j
        a = factorial(2*k-2*j)//(
            factorial(j)*factorial(k-j)*factorial(k-2*j))
        for r in range(e+1):
            coefficients[r] += a*comb(e,r)*2**r*(-1)**(e-r)
    return coefficients

def seed(n):
    H = H_derivative(n,0)
    K = H_derivative(n+1,0)+H_derivative(n+1,1)/(n+1)
    partials = [sum((F(1,factorial(j)) for j in range(k+1)), F(0))
                for k in range(2*n+2)]
    ts, rs = [], []
    for k in (n,n+1):
        coefficients = legendre_integer_coefficients(k)
        ts.append(sum((v*partials[n+r] for r,v in enumerate(coefficients)),F(0)))
        rs.append(sum((F(v,factorial(n+r)) for r,v in enumerate(coefficients)),F(0)))
    scale = F(factorial(n)**2,2**n)
    assert H == scale*rs[0]
    assert K == scale*F(n+1,2)*rs[1]
    A = scale*ts[0]
    B = scale*F(n+1,2)*ts[1]
    return H,K,A,B,K*A-H*B

def mod(x,p):
    x=F(x)
    assert x.denominator%p
    return x.numerator*pow(x.denominator,-1,p)%p

def valuation_integer(n,p):
    v=0
    while n and n%p==0:
        v+=1
        n//=p
    return v

def germ(p):
    # The previously proved Gauss bound kills R>=2p modulo p^2.
    # For R<2p, the only possible denominator loss is one power of p.
    # Compute numerators modulo p^3, retaining Y degrees 0,1,2.
    q=p**3
    def add(a,b):
        return [(x+y)%q for x,y in zip(a,b)]
    def mul(a,b):
        return [sum(a[j]*b[r-j] for j in range(r+1))%q for r in range(3)]
    def falls(offset):
        values=[[1,0,0]]
        for r in range(1,2*p):
            values.append(mul(values[-1],[offset-r+1,p,0]))
        return values
    fall1,fall2=falls(1),falls(2)
    H=[0,0,0]; KP=[0,0,0]
    q2=p*p
    for R in range(2*p):
        for c in range(R//2+1):
            b=R-2*c; s=b+c
            denominator=2**c*factorial(b)*factorial(c)
            loss=valuation_integer(denominator,p)
            assert loss<=1
            power=p**loss
            unit=denominator//power
            factor=(-1)**b*pow(unit,-1,q2)
            nums=[mul(fall1[R],fall1[s]),
                  mul(mul(fall2[R],fall2[s]),[4-R,2*p,0])]
            for target,num in zip((H,KP),nums):
                for j in range(3):
                    assert num[j]%power==0
                    target[j]=(target[j]+num[j]//power*factor)%q2
    inverse=[pow(2,-1,q2),-p*pow(4,-1,q2),0]
    K=[x%q2 for x in mul(KP,inverse)]
    expectedH=[0,mod(F(-3*p,2),q2),0]
    expectedK=[0,4*p%q2,0]
    assert H==expectedH,(p,H,expectedH)
    assert K==expectedK,(p,K,expectedK)
    # A=3, B=10 modulo p; H and K are multiples of p.
    C=[(3*k-10*h)%q2 for k,h in zip(K,H)]
    assert C==[0,27*p%q2,0]
    return dict(p=p,modulus=q2,H=H,K=K,C=C,
                exact_coefficient_cutoff="R<2p; numerator modulus p^3; all Y degrees>=3 vanish")

results=[]
for p in PRIMES:
    rows=[]
    for n in range(p):
        rational=seed(n)
        coordinates=[mod(x,p) for x in rational]
        rows.append(dict(r=n,values=dict(zip(("H","K","A","B","C"),coordinates))))
    results.append(dict(p=p,zero_residues=[x["r"] for x in rows if not x["values"]["C"]],
                        rows=rows))
germs=[germ(p) for p in (5,13)]
output=dict(scope="Assigned primes only; exact scalar definitions and coefficientwise germs, no HP solve",
            primes=list(PRIMES),seeds=results,residue_one_germs=germs,
            all_checks_pass=True)
(BASE/"hp_b1_uniform_prime_independent_certificate.json").write_text(
    json.dumps(output,indent=2)+"\n")
print(json.dumps({"all_checks_pass":True,
                  "zero_residues":{str(x["p"]):x["zero_residues"] for x in results},
                  "residue_one_germs":germs},indent=2))
