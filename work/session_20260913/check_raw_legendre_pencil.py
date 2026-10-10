"""Synthetic structural controls for the exact banded Legendre pencil."""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
t=s.symbols('t')
def integ(f,k=1):
    for j in range(k):
        f=s.integrate(f,t);f=s.expand(f-f.subs(t,0))
    return f
out=[]
for n in (3,6):
    size=n+10
    jj=s.zeros(size);tt=s.zeros(size);lam=s.diag(*(l*(l+1) for l in range(size)))
    jj[0,0]=s.Rational(1,2)
    for l in range(size):
        tt[l,l]=s.Rational(1,2)
        if l+1<size:
            jj[l+1,l]=s.Rational(1,2*(2*l+1))
            tt[l+1,l]=s.Rational(l+1,2*(2*l+1))
        if l:
            jj[l-1,l]=-s.Rational(1,2*(2*l+1))
            tt[l-1,l]=s.Rational(l,2*(2*l+1))
    E=s.diag(*(s.sqrt(2*l+1) for l in range(size)))
    jo=E.inv()*jj*E;to=E.inv()*tt*E
    assert (jo+jo.T)==s.diag(1,*([0]*(size-1))) and to==to.T
    # Synthetic numerator coefficients satisfying the three exact cubic
    # infinity identities and c0=0. They are not a canonical HP row.
    cc=[0,1,-2,3,2,-3,2]
    bb=[2,-1,4,3,-2,cc[5]-2*n*cc[6],cc[6]]
    aa=[-1,3,2,-2,4,-n*cc[6],0]
    cf=lambda a,k:s.Integer(a[k]) if 0<=k<=6 else s.S.Zero
    vs=[s.expand(cf(aa,4-k)+(n+k)*cf(bb,5-k)+(n+k)*(n+k-1)*cf(cc,6-k)
            -t*(cf(bb,4-k)+2*(n+k)*cf(cc,5-k))+t*t*cf(cc,4-k)) for k in range(7)]
    gamma=s.Integer(cc[6]);delta=s.Integer(cc[5])
    dm=gamma*lam+delta*jj*lam
    for k in range(7):
        mult=vs[k].coeff(t,0)*s.eye(size)+vs[k].coeff(t,1)*tt+vs[k].coeff(t,2)*tt**2
        dm+=mult*jj**k
    dm=dm.applyfunc(s.cancel)
    assert vs[6]==0 and s.degree(vs[5],t)<=0 and s.degree(vs[4],t)<=1
    assert all(dm[r,l]==0 for r in range(size) for l in range(size) if abs(r-l)>5)
    assert dm[n+5:,0:n+1]==s.zeros(size-n-5,n+1)
    for l in range(n+1):
        P=s.legendre(l,2*t-1)
        direct=s.expand(gamma*(-s.diff(t*(1-t)*s.diff(P,t),t))+delta*t*(t-1)*s.diff(P,t)+sum(vs[k]*integ(P,k) for k in range(7)))
        via=s.expand(sum(dm[r,l]*s.legendre(r,2*t-1) for r in range(n+5)))
        assert direct==via
    # Left cubic H has bandwidth3 and is represented through output n+4.
    hm=s.eye(size)-2*jj**2+jj**3
    assert all(hm[r,l]==0 for r in range(size) for l in range(size) if abs(r-l)>3)
    assert hm[n+5:,0:n+2]==s.zeros(size-n-5,n+2)
    # Exact endpoint quotient for one arbitrary degree-n control polynomial.
    pc=[s.Integer((-1)**l*(l+1)) for l in range(n+1)]
    P=sum(pc[l]*s.legendre(l,2*t-1) for l in range(n+1))
    den=sum((-1)**l*pc[l] for l in range(n+1))
    beta=s.diff(P,t).subs(t,0)/P.subs(t,0)
    rhs=-sum((-1)**l*l*(l+1)*pc[l] for l in range(n+1))/den
    assert beta==rhs
    out.append({'n':n,'scope':'synthetic coefficient row, not actual canonical HP transfer',
        'orthonormal_J_and_t_scaling':True,'right_bandwidth_at_most':5,
        'top_output_above_n_plus_4_cancels':True,'left_bandwidth':3,
        'full_polynomial_operator_identity':True,'finite_shapes':[[n+5,n+2],[n+5,n+1]],
        'endpoint_beta_quotient':True})
result={'status':'PASS','controls':out}
(HERE/'raw_legendre_pencil_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
