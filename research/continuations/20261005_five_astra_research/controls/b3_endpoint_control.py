"""Independent direct contact matrix vs full scalar endpoint quotient."""
import json
import math
import resource
from pathlib import Path
import sympy as s

resource.setrlimit(resource.RLIMIT_CPU, (60,60))
OUT=Path(__file__).resolve().parent
y=s.Symbol('y')
x=s.Symbol('x')
z=s.Symbol('z')


def H(n):
    phi=s.Poly((1-z+z*z/2)**n,z)
    return sum(math.factorial(n)//math.factorial(n-j)*phi.nth(j)*x**(n-j) for j in range(n+1))


def I(expr):
    degree=s.degree(expr,x)
    return sum(s.diff(expr,x,j).subs(x,1) for j in range(degree+1))


def vprime(num,p):
    num=abs(int(num))
    assert num
    depth=0
    while num%p==0:
        num//=p;depth+=1
    return depth


records=[]
for n in range(3,13):
    size=2*n+4
    deriv=[s.Rational(2),s.Rational(2)]
    while len(deriv)<size:
        deriv.append(deriv[-1]-deriv[-2]/2)
    fc=[s.Rational(0)]+[deriv[j-1]/j for j in range(1,size+1)]
    rows=[]
    for r in range(n+1,size):
        rows.append([s.Rational(1,math.factorial(r-j)) for j in range(4)]+[fc[r-j] for j in range(n+1)])
    rows.append([1]*4+[-1]*(n+1))
    M=s.Matrix(rows)
    kernel=M.nullspace()
    assert len(kernel)==1,(n,len(kernel))
    vec=kernel[0]
    B=list(vec[:4]);C=list(vec[4:])
    Y=sum(B)
    assert Y!=0,n
    X=-sum(sum(B[j]/math.factorial(r-j) for j in range(min(3,r)+1))+
           sum(C[j]*fc[r-j] for j in range(r+1)) for r in range(n+1))
    direct=s.cancel(-X/Y)
    # Reconstruct all derivative contraction rows from defining polynomials.
    Hn=H(n);Ht=H(n+1);Ht1=H(n+2)
    pr=x**n*Hn;pr1=x**(n+1)*Ht;pr2=x**(n+2)*Ht1
    e=[1]*4
    row_r=[s.diff(pr1,x,j).subs(x,1) for j in range(4)]
    row_s=[s.diff(pr2,x,j+1).subs(x,1)/(n+2) for j in range(4)]
    row_p=[0]+[sum(s.diff(pr,x,j).subs(x,1) for j in range(k)) for k in range(1,4)]
    row_u=[0]+[sum(s.diff(pr1,x,j).subs(x,1)/(n+1) for j in range(1,k+1)) for k in range(1,4)]
    sig=-s.Matrix([row_r,row_s,e,row_u]).det()
    chi=-s.Matrix([row_r,row_s,e,row_p]).det()
    kap=s.Matrix([row_r,row_s,row_u,row_p]).det()
    Ac=I(pr);Bc=I(s.diff(pr1,x))/(n+1)
    V=sig*Ac-chi*Bc-kap
    L=[s.Integer(1),4*y-2]
    for k in range(1,n+1):
        L.append(s.expand((2*(2*k+1)*(2*y-1)*L[-1]+4*k*L[-2])/(k+1)))
    P=[p.subs(y,1) for p in L]
    def second(p,Pval):
        quotient=s.Poly(s.div(p-Pval,y-1,y)[0],y)
        return sum(quotient.nth(j)*fc[j+1] for j in range(quotient.degree()+1)) if quotient.as_expr()!=0 else s.Rational(0)
    wn=second(L[n],P[n]);wn1=second(L[n+1],P[n+1])
    D=(n+1)*P[n+1]*chi-2*P[n]*sig
    Q=2*wn*sig-(n+1)*wn1*chi
    cofactor=s.cancel(-(Q+s.Rational(2**(n+1),math.factorial(n)**2)*V)/D)
    assert direct==cofactor,(n,direct,cofactor)
    gcd=math.gcd(int(sig),int(chi),int(kap))
    assert int(V)%gcd==0
    if n>=7:
        assert vprime(direct.q,7)==2*vprime(math.factorial(n),7)+vprime(D,7)
    records.append({'n':n,'normality_dimension':len(kernel),'p':str(direct.p),'q':str(direct.q),
                    'complete_center_agreement':True,'contraction_content':str(gcd),
                    'D':str(D),'V':str(V),'v7_q':vprime(direct.q,7),
                    'finite_only':True})

(OUT/'b3_endpoint_control.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'direct_contact_and_full_quotient':'PASS, n=3..12',
                  'actual_7adic_control':'PASS, n=7..12','finite_only':True}))
