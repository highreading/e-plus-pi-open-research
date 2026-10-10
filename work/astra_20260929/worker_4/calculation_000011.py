import sys, json, math
sys.path.insert(0, '[private local path removed]')
import sympy as s

# Universal determinant identities, without assuming the Wronskian prematurely.
a,b,wp,wu,G,TU,TP,a0,a1,a2,r1,r2 = s.symbols('a b wp wu G TU TP a0 a1 a2 r1 r2')
av=s.Matrix([a0,a1,a2]); ev=s.ones(3,1)
tuv=s.Matrix([TU,TU-a1,TU-a1-a2])
tpv=s.Matrix([TP,TP-r1,TP-r1-r2])
S0=a1*a1-a0*a2
C0=(a1-a0)*r2-(a2-a1)*r1
W0=a1*r2-a2*r1
Z0=a0*W0+TU*C0-TP*S0
assert s.expand(s.Matrix.hstack(av,ev,tuv).det()-S0)==0
assert s.expand(s.Matrix.hstack(av,ev,tpv).det()-C0)==0
assert s.expand(s.Matrix.hstack(av,tuv,tpv).det()-Z0)==0
tv=(a*tuv-b*tpv)/G
xv=(wp*tuv-wu*tpv)/G
beta=av.cross(ev+tv)
Yr=beta.dot(ev); Xr=beta.dot(xv)
N0=(wp+TP)*S0-(wu+TU)*C0-a0*W0
assert s.factor(G*Yr-(b*C0-a*S0))==0
assert s.factor(G**2*Xr-G*N0-(G-a*wu+b*wp)*Z0)==0

# Independent scaling and chart checks.
f,g,k,eta,S,C,W,Ps,Us=s.symbols('f g k eta S C W Ps Us')
D=k*b*C-2*a*S
X=2*Ps*S-k*Us*C-2*f*eta*W
V=b*Ps-a*Us
alpha=g*f/(G*k)
ys=(b*g*f*C-a*g*g*S)/G
xs=(Ps*g*g*S-Us*g*f*C-g*g*f*eta*W)/G
assert s.factor((ys-alpha*D).subs(g,2*f/k))==0
assert s.factor((xs-alpha*X).subs(g,2*f/k))==0
Hb=V*S-b*f*eta*W
Ha=k*V*C-2*a*f*eta*W
assert s.expand(b*X+Us*D-2*Hb)==0
assert s.expand(a*X+Ps*D-Ha)==0
assert s.expand(2*a*Hb-b*Ha+V*D)==0

# Exact finite checks from polynomial definitions and moment equations.
t,x=s.symbols('t x')
def Lpoly(m):
    return s.Poly(s.expand(sum(s.Rational(math.factorial(2*m-2*j), math.factorial(j)*math.factorial(m-j)*math.factorial(m-2*j))*(2*t-1)**(m-2*j) for j in range(m//2+1))),t)
def Hpoly(m):
    expr=0
    for c in range(m//2+1):
        for bb in range(m-2*c+1):
            coeff=(-1)**bb*s.binomial(m,bb+c)*s.binomial(bb+c,c)*s.Rational(math.factorial(m),math.factorial(m-bb-2*c)*2**c)
            expr += coeff*x**(m-bb-2*c)
    return s.Poly(expr,x)
def mu(d):
    return s.Rational(2,2**d)*sum((-1)**j*s.binomial(d,2*j)*s.Rational(1,2*j+1) for j in range(d//2+1))
def moment(poly):
    pp=s.Poly(poly,t)
    return sum(cc*mu(mon[0]) for mon,cc in pp.terms())
def wvalue(poly):
    quotient,remainder=s.div(poly.as_expr()-poly.eval(1),t-1,t)
    assert remainder==0
    return moment(quotient)
records=[]
for n in (2,3,4,5,6):
    P=Lpoly(n); U=Lpoly(n+1)
    aa=P.eval(1); bb=U.eval(1)
    wwP=wvalue(P); wwU=wvalue(U)
    GG=s.Rational((-1)**n*2**(2*n+3),n+1)
    assert aa*wwU-bb*wwP==GG
    assert moment(P.as_expr()*U.as_expr())==0
    assert moment(P.as_expr()**2)==s.Rational((-1)**n*2**(2*n+1),2*n+1)
    E=[sum(s.Rational(1,math.factorial(v)) for v in range(m+1)) for m in range(2*n+2)]
    def ell(poly,j):
        return sum(cc/s.factorial(n+mon[0]+1-j) for mon,cc in poly.terms())
    def T(poly,j):
        return sum(cc*E[n+mon[0]-j] for mon,cc in poly.terms())
    aa_vec=s.Matrix([ell(U,j) for j in range(3)])
    tt_vec=s.Matrix([(aa*T(U,j)-bb*T(P,j))/GG for j in range(3)])
    xx_vec=s.Matrix([(wwP*T(U,j)-wwU*T(P,j))/GG for j in range(3)])
    bet=aa_vec.cross(s.ones(3,1)+tt_vec)
    Yraw=sum(bet); Xraw=bet.dot(xx_vec)
    transforms={}
    for m,poly in ((n,P),(n+1,U)):
        HH=Hpoly(m)
        lhs=sum(cc*x**(m+mon[0])/s.factorial(m+mon[0]) for mon,cc in poly.terms())
        rhs=s.Rational(2**m,math.factorial(m)**2)*x**m*HH.as_expr()
        assert s.expand(lhs-rhs)==0
        hh=HH.eval(1)
        jj=m*hh+HH.diff().eval(1)
        kk=m*(m-1)*hh+2*m*HH.diff().eval(1)+HH.diff((x,2)).eval(1)
        assert all(value.q==1 for value in (hh,jj,kk))
        transforms[m]=(hh,jj,kk)
    hn,jn,kn=transforms[n]
    hn1,jn1,kn1=transforms[n+1]
    ff=s.Rational(2**n,math.factorial(n)**2)
    gg=s.Rational(2**(n+1),math.factorial(n+1)**2)
    kval=(n+1)**2
    assert s.Matrix([ell(P,1),ell(P,2)])==ff*s.Matrix([hn,jn])
    assert aa_vec==gg*s.Matrix([hn1,jn1,kn1])
    SS=jn1**2-hn1*kn1
    CC=(jn1-hn1)*jn-(kn1-jn1)*hn
    WW=jn1*jn-kn1*hn
    pstar=wwP+T(P,0); ustar=wwU+T(U,0)
    DD=kval*bb*CC-2*aa*SS
    XX=2*pstar*SS-kval*ustar*CC-2*ff*hn1*WW
    al=gg*ff/(GG*kval)
    assert Yraw==al*DD and Xraw==al*XX
    vv=bb*pstar-aa*ustar
    assert vv==bb*T(P,0)-aa*T(U,0)-GG
    assert bb*XX+ustar*DD==2*(vv*SS-bb*ff*hn1*WW)
    assert aa*XX+pstar*DD==kval*vv*CC-2*aa*ff*hn1*WW

    # Recover C using only the high Taylor moment equations.
    Hmat=s.Matrix(n+1,n+1,lambda rr,ss: mu(rr+ss))
    rhs=s.Matrix([-sum(bet[j]/s.factorial(n+1+rr-j) for j in range(3)) for rr in range(n+1)])
    qcoeff=Hmat.inv()*rhs
    ccoeff=list(reversed(list(qcoeff)))
    def be_coeff(m):
        return sum(bet[j]/s.factorial(m-j) for j in range(min(2,m)+1))
    def cf_coeff(m):
        return sum(ccoeff[d]*mu(m-d-1) for d in range(min(n,m-1)+1)) if m>=1 else s.Integer(0)
    acoeff=[-be_coeff(m)-cf_coeff(m) for m in range(n+1)]
    for m in range(2*n+3):
        residue=(acoeff[m] if m<=n else 0)+be_coeff(m)+cf_coeff(m)
        assert residue==0, (n,m,residue)
    assert sum(acoeff)==Xraw
    assert sum(ccoeff)==Yraw
    Lambda=2**(n+1)*math.factorial(2*n+2)*math.factorial(n)**2
    assert (Lambda*XX).q==1
    assert DD.q==1
    record={'n':n,'D':str(DD),'X':str(XX),'raw_vector_nonzero':any(v!=0 for v in bet),'order_and_endpoints_pass':True}
    if DD!=0:
        ratio=s.cancel(XX/DD)
        integral_den=int(Lambda*DD); integral_num=int(Lambda*XX)
        recovered_q=abs(integral_den)//math.gcd(abs(integral_den),abs(integral_num))
        assert recovered_q==int(ratio.q)
        record['q']=str(ratio.q)
    else:
        record['q']='undefined: D=0'
    records.append(record)
print(json.dumps({'universal_determinants_pass':True,'common_scaling_pass':True,'both_chart_identities_pass':True,'chart_compatibility_pass':True,'finite_reconstruction_checks':records,'scope':'Exact algebra and bounded finite reconstruction checks only; no formal registry verdict or denominator estimate.'},indent=2))