"""Independent controls of the dual content theorem.
Only the frozen n=1,2 triples: no new HP system is solved.
"""
import json, math
from pathlib import Path
import sympy as s
z,u=s.symbols("z u")
D=1+z*z
data={
1: (-2*z*z+6*z-6, z*z-6, 6*z*z-6*z),
2: (940*z**4-5832*z**3+13404*z*z-9720*z+17640,
    925*z**4+5652*z**3+12504*z*z+7920*z+17640,
    -2592*z**4+7524*z**3-9720*z*z+17640*z)
}
def content(f):
    return math.gcd(*(int(x) for x in s.Poly(f,z).all_coeffs()))
def v2q(v):
    v=s.Rational(v)
    if not v: return s.oo
    def vv(a):
        a=abs(int(a)); r=0
        while a%2==0: a//=2; r+=1
        return r
    return vv(v.p)-vv(v.q)
out={"scope":"Only frozen n=1,2 triples. Exact identity controls, not a new degree or prime scan.","checks":{}}
for n,(Q,P,T) in data.items():
    m=2*n
    E=s.expand(D*(Q*s.diff(T,z)-s.diff(Q,z)*T)-Q**2)
    F=s.expand(Q*s.diff(P,z)-s.diff(Q,z)*P-Q*P)
    W=s.cancel((D*(F*s.diff(E,z)-s.diff(F,z)*E+F*E)-s.diff(D,z)*F*E)/Q)
    K=s.cancel(W/z**(6*n))
    assert s.denom(K)==1
    p=[s.expand(P).coeff(z,m-j) for j in range(3)]
    e=[E.coeff(z,2*m-j) for j in range(3)]
    predicted=-p[0]*e[0]*z*z+((2*p[0]-p[1])*e[0]-p[0]*e[1])*z-(p[0]+p[2])*e[0]+(3*p[0]-p[1])*e[1]-p[0]*e[2]
    assert s.expand(K-predicted)==0
    cQ,cP,cE,cK=map(content,(Q,P,E,K))
    assert cK==cP*cE
    R=math.factorial(2*n)//math.factorial(n)
    assert R%cQ==R%cP==0
    assert (2**(4*n)*cQ*cQ)%cE==0
    assert (2**(4*n)*R**3)%cK==0
    Qstar=s.Poly(s.expand((Q/cQ).subs(z,s.I+2*s.I*u)),u)
    sigmas=[]
    for c in Qstar.all_coeffs():
        if c:
            norm=s.expand(c*s.conjugate(c))
            sigmas.append(s.Rational(v2q(norm),2))
    sigma=min(sigmas)
    assert v2q(cE)<=2*v2q(cQ)+2*sigma
    endpointg=math.gcd(int(Q.subs(z,1)),int(P.subs(z,1)),int(T.subs(z,1)))
    assert cK%endpointg==0
    out["checks"][str(n)]={
        "p_top":list(map(int,p)),"e_top":list(map(int,e)),
        "K":str(s.expand(K)),
        "content_Q":cQ,"content_P":cP,"content_E":cE,"content_K":cK,
        "sigma":str(sigma),"dyadic_bound_attained":v2q(cE)==2*v2q(cQ)+2*sigma,
        "six_coefficient_identity":True,"gauss_content_identity":True,
        "factorial_content_divisors":True,"global_endpoint_divisor":True
    }
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

