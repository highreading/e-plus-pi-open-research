"""Exact controls of the actual normalized Gram quotient, not asymptotic evidence."""
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as s
x=s.symbols('x')
def integrate(f):
    f=s.Poly(s.expand(f),x)
    return sum(c/s.Integer(k[0]+1) for k,c in f.terms())
def coeffvec(f,n):
    return s.Matrix([s.expand(f).coeff(x,j) for j in range(n+1)])
def beta(f,n):
    return sum((-1)**j*s.diff(f,x,j).subs(x,1) for j in range(n+1))
def check(n):
    Q=[s.expand(s.factorial(k)/s.factorial(2*k)*s.diff((1+x*x)**k,x,k))
       for k in range(2*n+1)]
    F=[sum(q.coeff(x,d)*x**d/s.factorial(d) for d in range(k+1))
       for k,q in enumerate(Q)]
    h=[s.Rational((-1)**k*2**(2*k),(2*k+1)*s.binomial(2*k,k)**2) for k in range(n+1)]
    T=s.expand(sum(Q[k].subs(x,1)*F[k]/h[k] for k in range(n+1)))
    G=s.Matrix(n+1,n+1,lambda i,j:s.Rational(1,i+j+1))
    bv=s.Matrix([beta(x**j,n) for j in range(n+1)])
    zv=G.inv()*bv
    Z=sum(zv[j]*x**j for j in range(n+1))
    rows=[s.Matrix([[integrate(x**j*F[k]) for j in range(n+1)]])
          for k in range(n+1,2*n)]
    tv=s.Matrix([integrate(x**j*T) for j in range(n+1)])
    wrow=(tv+4*bv).T
    A=s.Matrix.vstack(*rows,wrow,bv.T)
    pv=A.inv()*s.Matrix([0]*n+[1])
    P=sum(pv[j]*x**j for j in range(n+1))
    S=s.Matrix.vstack(*rows,wrow)
    gramS=S*G.inv()*S.T
    gramAll=A*G.inv()*A.T
    norm2=(pv.T*G*pv)[0]
    assert s.factor(norm2-gramS.det()/gramAll.det())==0
    assert beta(P,n)==1 and integrate(P*T)==-4
    # Original B and C, followed by original high Taylor coefficients.
    B=[(-1)**(n-j)*s.diff(P,x,n-j).subs(x,1) for j in range(n+1)]
    ell=lambda f:sum(B[j]*f.coeff(x,d)/s.factorial(n+d+1-j)
                     for j in range(n+1) for d in range(n+1))
    Cstar=s.expand(-sum(ell(Q[k])*Q[k]/h[k] for k in range(n+1)))
    C=[Cstar.coeff(x,n-j) for j in range(n+1)]
    assert sum(B)==1 and sum(C)==4
    def atan(k):
        return s.Rational((-1)**((k-1)//2),k) if k>0 and k%2 else s.S.Zero
    for k in range(n+1,3*n+1):
        assert sum(B[j]/s.factorial(k-j)+C[j]*atan(k-j) for j in range(n+1))==0
    return {'n':n,'actual_normalization':True,'original_high_jets':True,
            'positive_gram_quotient':True,'norm_squared':str(norm2)}
out={'status':'PASS','checks':[check(n) for n in (1,2,4)],
     'scope':'Finite exact identity checks; no asymptotic upper bound claimed.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
