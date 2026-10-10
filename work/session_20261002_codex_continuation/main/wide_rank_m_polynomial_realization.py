"""M33 new widened-stack exact author receipts; full primitive content retained."""
from pathlib import Path
from math import factorial, comb, prod, gcd, lcm
import sympy as sp
import json

ROOT=Path(__file__).resolve().parent
y,w,T=sp.symbols('y w T')
D=[1]
for n in range(1,100):
    D.append(n*D[-1]+(-1)**n)
def df(d): return prod(range(1,2*d,2))
def cm(m): return sp.Rational(2**(m+1)*factorial(m-1),df(m-1))
def cj(m,j): return sp.Rational(2**j*comb(m-1,j)*df(m-1-j),df(m-1))
def nu(m,r): return (-1)**r*sp.rf(sp.Rational(1,2)-r,m-1)/sp.rf(sp.Rational(1,2),m-1)
def oldmass(m): return sum((sp.Rational(2*factorial(h-2),df(h-1)) for h in range(2,m+1)),sp.Integer(0))
def moment(m,r):
    quotient,rem=sp.div(y**r,(1+y)**m)
    remw=sp.expand(rem.subs(y,w-1))
    coeff=[remw.coeff(w,m-h) for h in range(1,m+1)]
    rational=sum((quotient.coeff(y,j)/sp.Integer(2*j+1) for j in range(int(sp.degree(quotient,y))+1)),sp.Integer(0)) if quotient else 0
    aa=cm(m)*(rational+sum((coeff[h-1]*oldmass(h)/cm(h) for h in range(1,m+1)),sp.Integer(0)))
    period=cm(m)*sum((coeff[h-1]/cm(h) for h in range(1,m+1)),sp.Integer(0))
    assert period==nu(m,r)
    return aa
def companion(coeff):
    d=len(coeff)-1
    a=coeff[-1]
    H=sp.zeros(d)
    for j in range(d-1): H[j+1,j]=1
    for i in range(d): H[i,d-1]=-sp.Rational(coeff[i],a)
    assert sp.Poly((T*sp.eye(d)-H).det(),T)==sp.Poly(sum(sp.Rational(v,a)*T**i for i,v in enumerate(coeff)),T)
    return H

rows=[]
for m,k in [(1,2),(2,2),(2,4),(3,3),(3,5),(4,4),(4,6),(5,5)]:
    N=2*k+m
    alpha=[moment(m,r) for r in range(k+N-1)]
    C=sp.Matrix(k,N,lambda i,j:D[2*(i+j)]-nu(m,i+j))
    R=sp.Matrix(k,N,lambda i,j:alpha[i+j]-factorial(2*(i+j)))
    E=sp.Matrix(m,N,lambda a,j:comb(j,a)*(-1)**(j-a) if j>=a else 0)
    J=sp.Matrix(m,m,lambda a,b:factorial(a+b)*cj(m,a+b) if a+b<m else 0)
    EL=E[:,:k].T
    V=sp.Matrix(k,N,lambda i,j:nu(m,i+j))
    assert V==EL*J*E and J.det()!=0
    # Left polynomials: (y+1)^m y^i, then (y+1)^a.
    polys=[y**i*(y+1)**m for i in range(k-m)]+[(y+1)**a for a in range(m)]
    F0=sp.Matrix(k,k,lambda i,j:sp.expand(polys[i]).coeff(y,j))
    F=sp.diag(sp.eye(k-m),J.inv())*F0
    U=sp.zeros(k,m)
    U[k-m:k,:]=sp.eye(m)
    assert F.det()!=0 and F*EL*J==U
    border=C.col_join(F*R).col_join(E)
    bd=border.det()
    assert bd!=0
    inv=border.inv()
    delta=lcm(*(int(a.q) for a in R))
    assert all((delta*a).q==1 for a in V)
    targets=[[ -41,7 ],[i*(-1)**i+2 for i in range(m)]+[3]] if m>1 else [[-41,7],[-23,5]]
    if m>=2: targets.append([1,0,1])
    for coeff in targets:
        d=len(coeff)-1
        assert gcd(*coeff)==1 and coeff[-1]>0 and d<=m
        A=sp.diag(sp.eye(k-d),-companion(coeff))
        B=sp.zeros(m,k)
        B[m-d:m,k-d:k]=sp.eye(d)
        rhs=sp.zeros(k,k).col_join(A).col_join(B)
        Q=inv*rhs
        assert C*Q==sp.zeros(k,k) and F*R*Q==A and E*Q==B and Q.rank()==k
        den=[lcm(*(int(Q[i,j].q) for i in range(N))) for j in range(k)]
        Z=Q*sp.diag(*den)
        assert all(a.q==1 for a in Z) and C*Z==sp.zeros(k,k)
        val=[(delta*(R+t*V)*Z).det() for t in range(m+2)]
        poly=sp.Poly(sp.interpolate(list(enumerate(val[:m+1])),T),T)
        assert poly.eval(m+1)==val[m+1] and poly.degree()==d
        ic=[int(poly.nth(j)) for j in range(m+1)]
        scalar=sp.Rational(delta**k*prod(den),coeff[-1]*F.det())
        assert scalar.q==1
        assert all(ic[j]==scalar*(coeff[j] if j<=d else 0) for j in range(m+1))
        g=gcd(*ic)
        primitive=[v//g for v in ic]
        if primitive[d]<0: primitive=[-v for v in primitive]
        assert primitive==coeff+[0]*(m-d)
        rows.append({'m':m,'k':k,'width':N,'target_primitive_coefficients':coeff,
                     'complete_border_determinant':str(bd),'left_basis_determinant':str(F.det()),
                     'right_column_minimum_denominators':list(map(str,den)),
                     'full_entry_clearer':str(delta),'complete_integer_coefficient_content':str(g),
                     'actual_primitive_coefficients':primitive,
                     'right_integer_coefficient_height_bits':max(abs(int(z)).bit_length() for z in Z),
                     'exact_complete_matching_jet_response_content_checks':True})
        print('WIDE',m,k,'degree',d,'rightbits',rows[-1]['right_integer_coefficient_height_bits'],flush=True)
(ROOT/'WIDE_RANK_M_POLYNOMIAL_REALIZATION_CERTIFICATE.json').write_text(json.dumps({'status':'PASS_NEW_WIDENED_RANK_M_REALIZATION','rows':rows,'scope':'New widened actual matching stacks. Arbitrary direction encoding, not controlled approximation or an irrationality proof.'},indent=2)+'\n')
