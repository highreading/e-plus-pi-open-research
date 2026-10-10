"""Frozen exact controls for the all-index moment proof; no canonical solve."""
from pathlib import Path
import sys, json, math
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
z,t=s.symbols('z t')

def val(q):
    q=s.Rational(q)
    if not q:return None
    a,b=abs(int(q.p)),int(q.q)
    return (a&-a).bit_length()-(b&-b).bit_length()

def lower(q,k):
    return not q or val(q)>=k

def phi(j):
    return j-j.bit_count()

def mu(k):
    return s.Rational((-1)**(k//2),k+1) if k%2==0 else s.S.Zero

def moment(f):
    p=s.Poly(s.expand(f),t)
    return sum(c*mu(i[0]) for i,c in p.terms())

def poly(co):
    return sum(s.Rational(c)*z**(len(co)-1-i) for i,c in enumerate(co))

Q=[s.S.One,t]
for j in range(1,16):
    Q.append(s.expand(t*Q[-1]+s.Rational(j*j,4*j*j-1)*Q[-2]))

rows=json.loads((HERE/'raw_accessory_scaling_probe.json').read_text())['cases']
out=[]
for row in rows:
    n=row['n']; inp=row['exact_polynomial_input']
    A,B,C=(poly(inp[key]) for key in ('A','B','C'))
    common=B.subs(z,1)
    A,B,C=(s.expand(f/common) for f in (A,B,C))
    assert B.subs(z,1)==1 and C.subs(z,1)==4
    U=s.expand(t**n*C.subs(z,1/t))
    V=s.expand(t**n*A.subs(z,1/t))
    b=s.Poly(B,z)
    hs=[s.Rational((-1)**j*4**j,(2*j+1)*math.comb(2*j,j)**2) for j in range(n+1)]
    us=[s.cancel(moment(U*Q[j])/hs[j]) for j in range(n+1)]
    assert s.expand(sum(us[j]*Q[j] for j in range(n+1))-U)==0
    eps=int(n%4==2)
    M=-n-2*phi(n-1)-2*eps
    K=M-n
    for j in range(n):
        assert lower(us[j],phi(n)-phi(n+1+j)-2*phi(j))
    assert all(lower(u,M) for u in us)
    for k in range(n):
        N=n+1+k
        coeff=sum(b.nth(j)/math.factorial(N-j) for j in range(n+1))
        assert s.cancel(moment(t**k*U)+coeff)==0
    up=s.Poly(U,t)
    SU=sum(up.nth(j)*sum(t**(j-1-k)*mu(k) for k in range(j)) for j in range(1,n+1))
    EB=sum(sum(b.nth(j)/math.factorial(N-j) for j in range(N+1))*t**(n-N) for N in range(n+1))
    assert s.expand(V+SU+EB)==0
    TU=s.expand(U*U+(1+t*t)*(U*s.diff(SU,t)-s.diff(U,t)*SU))
    corr=s.expand((1+t*t)*(s.diff(EB,t)*U-EB*s.diff(U,t)))
    P=s.Poly((1+z*z)*(s.diff(A,z)*C-A*s.diff(C,z))+C*C,z)
    assert s.expand(t**(2*n)*P.as_expr().subs(z,1/t)-TU-corr)==0
    p0,p1,p2=(P.nth(2*n-j) for j in range(3))
    vn=val(n)
    assert val(p0)==K
    for d in (1,2):
        assert lower(s.Poly(TU,t).nth(d),K+vn+1)
        assert lower(s.Poly(corr,t).nth(d),M)
        assert lower(P.nth(2*n-d),K+min(n,vn+1))
    out.append({'n':n,'normalization':'B(1)=1, C(1)=4',
        'moment_and_reconstruction_identities':'pass',
        'all_orthogonal_coefficient_bounds':'pass',
        'v2_p0':K,'v2_p1_over_p0':val(p1/p0),'v2_p2_over_p0':val(p2/p0),
        'proved_relative_lower_bound':min(n,vn+1),
        'pure_second_kind_relative_valuations':[val(s.Poly(TU,t).nth(d)/p0) for d in (1,2)],
        'exponential_correction_relative_valuations':[val(s.Poly(corr,t).nth(d)/p0) for d in (1,2)]})

record={'status':'pass','scope':'Only frozen n=2,4,8,16 triples; no canonical solve or new degree scan.', 'cases':out}
(HERE/'raw_even_P_moment_gates_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
