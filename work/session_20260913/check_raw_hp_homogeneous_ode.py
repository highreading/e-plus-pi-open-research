"""Exact controls for the cofactor ODE, using original high-jet equations."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as s
z=s.symbols('z'); D=1+z*z
def atan(k):
    return s.Rational((-1)**((k-1)//2),k) if k>0 and k%2 else s.S.Zero
def raw_row(n):
    rows=[[s.S.One/s.factorial(k-j) for j in range(n+1)]+
          [atan(k-j) for j in range(n+1)] for k in range(n+1,3*n+1)]
    rows+=[[-4]*(n+1)+[1]*(n+1),[1]*(n+1)+[0]*(n+1)]
    v=s.Matrix(rows).inv()*s.Matrix([0]*(2*n+1)+[1])
    B=sum(v[j]*z**j for j in range(n+1)); C=sum(v[n+1+j]*z**j for j in range(n+1))
    A=-sum(sum(v[j]/s.factorial(k-j)+v[n+1+j]*atan(k-j) for j in range(k+1))*z**k
           for k in range(n+1))
    scale=s.ilcm(*[c.q for f in (A,B,C) for c in s.Poly(f,z).all_coeffs()])
    return [s.expand(scale*f) for f in (A,B,C)]
def check(n):
    A,B,C=raw_row(n)
    fj={1:1/D,2:s.diff(1/D,z),3:s.diff(1/D,z,2)}
    Ej=[s.diff(A,z,r)+sum(s.binomial(r,j)*s.diff(C,z,r-j)*fj[j] for j in range(1,r+1))
        for r in range(4)]
    Bj=[sum(s.binomial(r,j)*s.diff(B,z,j) for j in range(r+1)) for r in range(4)]
    Cj=[s.diff(C,z,r) for r in range(4)]
    mat=s.Matrix([[Ej[r],Bj[r],Cj[r]] for r in range(4)])
    wr=lambda I:s.cancel(mat.extract(I,[0,1,2]).det())
    Q=s.cancel(D*D*wr([0,1,2])/z**(3*n-1))
    assert Q.is_polynomial(z) and Q!=0
    A3=s.expand(z*D*Q)
    A2=s.expand(-(((z+3*n-1)*D-2*z*s.diff(D,z))*Q+z*D*s.diff(Q,z)))
    A1=s.cancel(D**3*wr([0,2,3])/z**(3*n-2))
    A0=s.cancel(-D**3*wr([1,2,3])/z**(3*n-2))
    assert A1.is_polynomial(z) and A0.is_polynomial(z)
    q=s.degree(Q,z)
    assert s.degree(A1,z)<=q+2 and s.degree(A0,z)<=q+1
    assert s.cancel(A2+D**3*wr([0,1,3])/z**(3*n-2))==0
    Aj=[A0,A1,A2,A3]
    for jets in (Ej,Bj,Cj):
        assert s.cancel(sum(Aj[r]*jets[r] for r in range(4)))==0
    # Congruences are checked only after verifying their hypotheses.
    good=s.degree(s.gcd(Q,s.diff(Q,z)),z)==0 and s.degree(s.gcd(Q,z*D),z)==0
    if good:
        e1=A1*(s.diff(A2,z)+A1)+s.diff(A3,z)*(s.diff(A1,z)+A0)
        e2=A0*(s.diff(A2,z)+A1)+s.diff(A3,z)*s.diff(A0,z)
        assert s.rem(e1,Q,z)==0 and s.rem(e2,Q,z)==0
    # Independent local logarithmic-line identity at both raw poles.
    logpole_good=s.degree(s.gcd(Q,D),z)==0
    if logpole_good:
        lp=s.diff(A3,z)*s.diff(C,z)-(s.diff(A2,z)-s.diff(A3,z,2)-A1)*C
        assert s.rem(lp,D,z)==0
    # For these rows, exact Laurent cancellation establishes the two powers.
    w=s.symbols('w')
    # F(z)-F_infinity=-atan(1/z) near infinity.
    H=s.series(A.subs(z,1/w)-C.subs(z,1/w)*s.atan(w),w,0,2*n+5).removeO().expand()
    c=int(s.degree(C,z)); b=int(s.degree(B,z))
    if H.coeff(w,-c)!=0:
        H=s.expand(H-H.coeff(w,-c)/s.LC(s.Poly(C,z))*C.subs(z,1/w))
    powers=[term.as_powers_dict().get(w,s.S.Zero) for term in s.Add.make_args(H) if term!=0]
    d=-int(min(powers))
    assert c!=d and b+c+d==3*n+q-4
    lead=s.LC(s.Poly(Q,z))
    assert s.expand(A1).coeff(z,q+2)==(c+d-1)*lead
    assert s.expand(A0).coeff(z,q+1)==-c*d*lead
    return {'n':n,'degrees':[int(s.degree(a,z)) for a in (Q,A3,A2,A1,A0)],
            'infinity_powers':[b,c,d],'direct_three_solution_check':True,
            'simple_apparent_hypotheses':bool(good),'apparent_congruences_pass':bool(good),
            'logarithmic_pole_C_jet_identity':bool(logpole_good)}
if __name__=='__main__':
    out={'status':'PASS','checks':[check(n) for n in (1,2,4)],
         'scope':'Exact finite controls of all-degree derivations, not an asymptotic scan.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
