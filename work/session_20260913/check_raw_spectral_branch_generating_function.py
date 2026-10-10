"""Closed symbolic coefficient checks, k=0,...,6, no canonical HP solve."""
import sys,json
from pathlib import Path
from math import comb
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
z,w,xi=s.symbols('z w xi')
K=6
def V_coeff(seed):
    v=[s.Rational(seed[0]),s.Rational(seed[1])]
    for j in range(K-1):
        vm=v[j-1] if j else 0
        v.append(s.expand(((j+1)*v[j+1]+(xi-j*(j+1)-1)*v[j]+j*vm)/((j+2)*(j+1))))
    return v
def row_branch(seed):
    r=[s.Rational(seed[0]),s.Rational(seed[1])]
    for k in range(K-1):
        up2=s.Rational((k+1)**2*(k+2)**2,(2*k+1)*(2*k+3))
        up1=s.Rational((k+1)**2,2*k+1)
        down1=s.Rational(k*k,2*k+1)
        down2=s.Rational(k*k*(k-1)**2,(2*k+1)*(2*k-1))
        diag=s.Rational((k+1)**4,(2*k+1)*(2*k+3))+s.Rational(k**4,(2*k+1)*(2*k-1))-k*(k+1)
        r.append(s.expand(((xi-diag)*r[k]+up1*r[k+1]+(down1*r[k-1] if k else 0)-(down2*r[k-2] if k>=2 else 0))/up2))
    return r
records=[]
for sigma,seed in enumerate(((1,s.Rational(1,2)),(0,1))):
    v=V_coeff(seed)
    cc=[s.Rational(comb(2*j,j),2**j) for j in range(K+1)]
    eta=z/(1-z*z)
    gen=s.series(sum(cc[j]*v[j]*eta**j for j in range(K+1))/s.sqrt(1-z*z),z,0,K+1).removeO().expand()
    r=row_branch(seed)
    assert all(s.expand(gen.coeff(z,k)-r[k])==0 for k in range(K+1))
    vp=sum(v[j]*w**j for j in range(K+1))
    residual=s.expand((1+w*w)*s.diff(vp,w,2)-(w-1)**2*s.diff(vp,w)+(1-w-xi)*vp)
    assert all(residual.coeff(w,j)==0 for j in range(K-1))
    ap=sum(cc[j]*v[j]*w**j for j in range(K+1))
    def theta(p):return s.expand(w*s.diff(p,w))
    def factors(p,fs):
        for a,b in fs:p=s.expand(a*theta(p)+b*p)
        return p
    ode=factors(ap,[(1,0),(1,0),(1,-1),(1,-1)])
    ode-=w*factors(ap,[(1,0),(1,0),(2,1)])
    q=theta(theta(ap))+theta(ap)+(1-xi)*ap
    ode+=w*w*factors(q,[(2,1),(2,3)])
    ode-=w**3*factors(ap,[(2,1),(2,3),(2,5)])
    ode=s.expand(ode)
    assert all(ode.coeff(w,j)==0 for j in range(K+1))
    records.append({'sigma':sigma,'normalized_branch_coefficients':[str(p) for p in r],
        'second_order_V_equation':'pass','Abel_fourth_order_equation':'pass','row_recurrence_match':'pass'})
out={'scope':'Only formal coefficients0..6 in the symbolic spectral parameter; no spectral eigenvalues sampled and no canonical HP degree solve.',
     'status':'pass','branches':records}
(HERE/'raw_spectral_branch_generating_function_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
