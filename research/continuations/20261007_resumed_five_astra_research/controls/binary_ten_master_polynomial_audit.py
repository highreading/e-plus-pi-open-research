"""Parent-authored exact polynomial and finite-sum audit, independent of remote code."""
from pathlib import Path
from math import comb
from fractions import Fraction
import json, time
import sympy as sp
ROOT=Path(__file__).resolve().parent
j,b=sp.symbols('j b');n=4002*b

def reduction(P,u,v,sigma,degree):
    rest=sp.Poly(sp.expand(P),j)
    Q=sp.Integer(0)
    for k in range(degree,2,-1):
        leading=rest.nth(k)
        if leading==0 or k-3+sigma==0:continue
        coefficient=leading/(k-3+sigma)
        Q+=coefficient*j**(k-3)
        image=u*(j+1)**(k-3)-v*j**(k-3)
        rest=sp.Poly(sp.expand(rest.as_expr()-coefficient*image),j)
    return sp.expand(Q),rest.as_expr()

start=time.monotonic()
u=(n+2-j)**2*(b+1-j)**2
v=j**2*(n+b-j)**2
P=j*(j-1)*((n+b-j)*(n+b+1-j)*(b+1-j)*(b-j))**2
Q,R=reduction(P,u,v,-6,10)
Q720=sp.expand(720*Q);R720=sp.Poly(sp.expand(720*R),j)
identity=sp.expand(720*P-R720.as_expr()-u*Q720.subs(j,j+1)+v*Q720)
expected=720*(-8004*b*b+8000*b+3)
symbolic={'D':1,'n':'4002*b','identity_difference':str(identity),
          'exceptional_coefficient_difference':str(sp.expand(R720.nth(9)-expected)),
          'remainder_degrees':[monomial[0] for monomial,_ in R720.terms()],
          'Q_degree_j':sp.Poly(Q720,j).degree(),
          'Q_integral_in_b_j':all(c.q==1 for c in sp.Poly(Q720,j,b,domain=sp.QQ).coeffs()),
          'R_integral_in_b_j':all(c.q==1 for c in sp.Poly(R720.as_expr(),j,b,domain=sp.QQ).coeffs()),
          'Q':str(Q720),'C':{str(k):str(R720.nth(k)) for k in (0,1,2,9)},
          'scope':'Polynomial identity for symbolic b. Not a master-moment value or primitive-error proof.'}

cases=[]
for bb,D in ((5,1),(7,1),(5,2),(7,2)):
 for aa,ab in ((1,1),(1,2),(2,2)):
    nn=4002*bb;N=nn+2;B=bb+D;A=aa*nn+bb-D;Aprime=ab*nn+bb-D
    U=(N-j)**2*(B-j)**2
    V=j*j*(A+1-j)*(Aprime+1-j)
    sigma=(aa+ab-2)*nn-4*D-2
    # Extreme allowed offsets realize maximal polynomial degree 10D.
    degree=10*D
    PP=sp.prod(j-r for r in range(2*D))*sp.prod(A+1-j+r for r in range(2*D))*sp.prod(B-j-r for r in range(2*D))*sp.prod(Aprime+1-j+r for r in range(2*D))*sp.prod(B-j-r for r in range(2*D))
    q,rr=reduction(PP,U,V,sigma,degree)
    pi=1
    for s in range(degree-2):
        if s+sigma:pi*=s+sigma
    qpaid=sp.Poly(sp.expand(pi*q),j,domain=sp.QQ)
    rpaid=sp.Poly(sp.expand(pi*rr),j,domain=sp.QQ)
    imagecheck=sp.expand(pi*PP-rpaid.as_expr()-U*qpaid.as_expr().subs(j,j+1)+V*qpaid.as_expr())
    def t(k):return comb(N,k)**2*comb(A-k,B-k)*comb(Aprime-k,B-k)
    adjoint_sum=sum(t(k)*(int(U.subs(j,k))*int(qpaid.as_expr().subs(j,k+1))-int(V.subs(j,k))*int(qpaid.as_expr().subs(j,k))) for k in range(bb))
    terminal=int(V.subs(j,bb))*t(bb)*int(qpaid.as_expr().subs(j,bb))
    h=l=hp=lp=2*D;r=2*D
    c=sp.factorial(r)*sp.prod(A-B+1+k for k in range(h+l))*sp.prod(Aprime-B+1+k for k in range(hp+lp))
    kernel=sum(comb(N,k)**2*comb(k,r)*comb(A+h-k,B-l-k)*comb(Aprime+hp-k,B-lp-k) if k>=r and B-l-k>=0 else 0 for k in range(bb))
    polynomial_sum=sum(t(k)*int(PP.subs(j,k)) for k in range(bb))
    cases.append({'b':bb,'D':D,'type':[aa,ab],'degree':degree,
                  'polynomial_identity_zero':imagecheck==0,
                  'paid_Q_integral':all(x.q==1 for x in qpaid.all_coeffs()),
                  'paid_R_integral':all(x.q==1 for x in rpaid.all_coeffs()),
                  'adjoint_terminal_equal':adjoint_sum==terminal,
                  'offset_kernel_identity_equal':int(c)*kernel==polynomial_sum,
                  'scope':'Auxiliary finite sums, not original approximation indices.'})
report={'personally_authored':True,'network_and_credential_reads_denied':True,
        'symbolic':symbolic,'finite_checks':cases,
        'all_passed':identity==0 and sp.expand(R720.nth(9)-expected)==0 and all(all(row[k] for k in ('polynomial_identity_zero','paid_Q_integral','paid_R_integral','adjoint_terminal_equal','offset_kernel_identity_equal')) for row in cases),
        'elapsed_seconds':round(time.monotonic()-start,3)}
(ROOT/'binary_ten_master_polynomial_certificate.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_passed':report['all_passed'],'symbolic_identity_zero':identity==0,
                  'finite_cases':len(cases),'seconds':report['elapsed_seconds']}))
