"""Two preselected generic accessory/endpoint updates; no polynomiality rows."""
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
z=s.symbols('z');D=1+z*z
def Kmat(A,B,C):
    return s.Matrix([[D*D*A,B,C],
        [D*D*s.diff(A,z)+D*C,B+s.diff(B,z),s.diff(C,z)],
        [D*D*s.diff(A,z,2)+2*D*s.diff(C,z)-s.diff(D,z)*C,
         B+2*s.diff(B,z)+s.diff(B,z,2),s.diff(C,z,2)]])
archive=json.loads((HERE/'raw_rational_transfer_checks.json').read_text())['steps']
seed=[7-s.Rational(19,2)*z,-7+8*z,s.Rational(17,2)-s.Rational(9,2)*z]
triples=[seed]+[[s.sympify(a) for a in row['next_triple']] for row in archive]
out={'scope':'Generic state only in the new solve; two exact comparison controls','steps':[]}
for n,old,new in zip((1,2),triples,triples[1:]):
    K=Kmat(*old);Kp=Kmat(*new)
    Q=s.cancel(K.det()/z**(3*n-1));q=s.Poly(Q,z)
    assert q.degree()==3 and s.degree(s.gcd(Q,s.diff(Q,z)),z)==0
    assert s.degree(s.gcd(Q,z*D),z)==0
    base=s.Matrix([[-2*s.diff(D,z)/D,0,0],[0,1,0],[D,0,0]])
    conn=((K.diff(z)+K*base)*K.inv()).applyfunc(s.cancel)
    A3=s.expand(z*D*Q)
    coeff=[s.cancel(-conn[2,j]*A3) for j in range(3)]+[A3]
    assert all(not s.denom(a).has(z) for a in coeff)
    A0,A1,A2,A3=coeff
    # Fixed four-step Frobenius reconstruction using only the accessories.
    M=3*n+1;f=z**M;us=[s.Integer(1)]
    for r in range(1,5):
        residual=s.expand(sum(coeff[j]*s.diff(f,z,j) for j in range(4)))
        u=-residual.coeff(z,M+r-2)/(Q.subs(z,0)*(M+r)*(M+r-1)*r)
        us.append(s.cancel(u));f+=u*z**(M+r)
    B,C=old[1:]
    uj=[sum(s.binomial(j,r)*s.diff(B,z,r).subs(z,1) for r in range(j+1)) for j in range(6)]
    cj=[s.diff(C,z,j).subs(z,1) for j in range(6)]
    monomials=[(j,d) for j,maxd in enumerate((5,6,6)) for d in range(maxd+1)]
    columns=[]
    for j,d in monomials:
        Ns=[s.Integer(0)]*3;Ns[j]=z**d;N0,N1,N2=Ns
        col=[]
        for P in (s.diff(A3,z)*N0+A0*N2,s.diff(A3,z)*N1+A1*N2):
            rem=s.rem(s.Poly(P,z),s.Poly(Q,z)).as_expr()
            col.extend(rem.coeff(z,k) for k in range(3))
        for P in (N2,N1-s.diff(N2,z)):
            rem=s.rem(s.Poly(P,z),s.Poly(D,z)).as_expr()
            col.extend(rem.coeff(z,k) for k in range(2))
        origin=s.expand(sum(Ns[r]*s.diff(f,z,r) for r in range(3)))
        col.extend(origin.coeff(z,k) for k in range(M-2,M+3))
        a05=N0.coeff(z,5);a15=N1.coeff(z,5);a16=N1.coeff(z,6)
        a25=N2.coeff(z,5);a26=N2.coeff(z,6)
        col.extend([a05+n*a16,a16+a26,a05+a15+a25+n*a16+2*n*a26])
        if Q.subs(z,1)!=0:
            col.extend([sum(Ns[r].subs(z,1)*uj[r] for r in range(3)),
                        sum(Ns[r].subs(z,1)*cj[r] for r in range(3))])
            endpoint_den=Q.subs(z,1)
        else:
            col.extend([sum(s.diff(Ns[r],z).subs(z,1)*uj[r]+Ns[r].subs(z,1)*uj[r+1] for r in range(3)),
                        sum(s.diff(Ns[r],z).subs(z,1)*cj[r]+Ns[r].subs(z,1)*cj[r+1] for r in range(3))])
            endpoint_den=s.diff(Q,z).subs(z,1)
        columns.append(col)
    mat=s.Matrix.hstack(*map(s.Matrix,columns));assert mat.shape==(20,20)
    rhs=s.zeros(20,1);rhs[-2]=endpoint_den;rhs[-1]=4*endpoint_den
    sol,params=mat.gauss_jordan_solve(rhs);assert params.rows==0
    Ns=[s.expand(sum(sol[i]*z**d for i,(jj,d) in enumerate(monomials) if jj==j)) for j in range(3)]
    true=(Kp*K.inv()).applyfunc(s.cancel)
    assert all(s.cancel(Ns[j]/Q-true[0,j])==0 for j in range(3))
    out['steps'].append({'from_n':n,'shape':[20,20],'rank':20,
        'generic_hypotheses_verified':True,'frobenius_relative_coefficients':list(map(str,us)),
        'Q_at_1_nonzero':bool(Q.subs(z,1)!=0),
        'matches_independent_polynomial_transfer':True})
out['status']='passed'
(HERE/'raw_generic_accessory_update_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Generic 20x20 accessory/endpoint solves n=1 and n=2 passed and match the independent polynomial transfer.')
