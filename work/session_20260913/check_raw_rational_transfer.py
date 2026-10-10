"""Recover two successive raw triples through a fixed-size rational-transfer solve."""
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
def rcoeff(A,B,C,limit):
    ans=[]
    for k in range(limit+1):
        ans.append(A.coeff(z,k)+sum(B.coeff(z,j)/s.factorial(k-j)
            for j in range(min(s.degree(B,z),k)+1))+sum(C.coeff(z,j)*
            (s.Rational((-1)**((k-j-1)//2),k-j) if (k-j)>0 and (k-j)%2 else 0)
            for j in range(min(s.degree(C,z),k)+1)))
    return ans
def divide(poly,den):
    q,r=s.div(s.Poly(poly,z),s.Poly(den,z));return q.as_expr(),r.as_expr()
def step(n,A,B,C):
    K=Kmat(A,B,C)
    Q=s.cancel(K.det()/z**(3*n-1))
    assert s.denom(Q)==1 or not s.denom(Q).has(z)
    Q=s.Poly(Q,z).as_expr();q=s.degree(Q,z)
    h=min(j for (j,),a in s.Poly(Q,z).terms())
    jets=rcoeff(A,B,C,3*n+5+q)
    Rs=sum(a*z**j for j,a in enumerate(jets))
    columns=[];outputs=[]
    for j in range(3):
        for d in range(7):
            pB=z**d*K[j,1];pC=z**d*K[j,2];pA=z**d*K[j,0]
            Bq,Br=divide(pB,Q);Cq,Cr=divide(pC,Q);Aq,Ar=divide(pA,D*D*Q)
            col=[]
            for quotient,remainder,den_degree in [(Bq,Br,q),(Cq,Cr,q),(Aq,Ar,q+4)]:
                col.extend(s.expand(remainder).coeff(z,k) for k in range(den_degree))
                col.extend(s.expand(quotient).coeff(z,k) for k in range(n+2,n+7-q))
            poly=s.expand(z**d*s.diff(Rs,z,j))
            col.extend(poly.coeff(z,k) for k in range(3*n-1,3*n+4+h))
            col.extend([Bq.subs(z,1),Cq.subs(z,1)])
            columns.append(col);outputs.append((Aq,Bq,Cq))
    M=s.Matrix.hstack(*[s.Matrix(col) for col in columns])
    target=s.zeros(M.rows,1);target[-2]=1;target[-1]=4
    sol,params=M.gauss_jordan_solve(target)
    assert params.rows==0 and M.cols==21 and M.rows<=29
    new=[s.expand(sum(sol[i]*outputs[i][j] for i in range(21))) for j in range(3)]
    Ap,Bp,Cp=new
    assert max(s.degree(p,z) for p in new)<=n+1
    assert Bp.subs(z,1)==1 and Cp.subs(z,1)==4
    actual=rcoeff(Ap,Bp,Cp,3*(n+1))
    assert all(a==0 for a in actual)
    Kp=Kmat(*new)
    T=(Kp*K.inv()).applyfunc(s.cancel)
    N=(Q*T).applyfunc(s.cancel)
    bounds=[[5,6,6],[4,5,5],[3,4,4]]
    degrees=[]
    for i in range(3):
        degrees.append([])
        for j in range(3):
            assert not s.denom(N[i,j]).has(z)
            deg=s.degree(N[i,j],z)
            assert deg<=bounds[i][j]
            degrees[i].append(int(deg) if deg!=-s.oo else None)
        assert N[i,2].subs(z,0)==0
    Qp=s.cancel(Kp.det()/z**(3*n+2))
    assert s.cancel(T.det()-z**3*Qp/Q)==0
    assert all(s.cancel(T[0,j]-sum(sol[7*j+d]*z**d for d in range(7))/Q)==0 for j in range(3))
    # Rational companion matrices retain the universal gauge derivative.
    base=s.Matrix([[-2*s.diff(D,z)/D,0,0],[0,1,0],[D,0,0]])
    conn=((K.diff(z)+K*base)*K.inv()).applyfunc(s.cancel)
    connp=((Kp.diff(z)+Kp*base)*Kp.inv()).applyfunc(s.cancel)
    assert conn[:2,:]==s.Matrix([[0,1,0],[0,0,1]])
    assert (T.diff(z)-connp*T+T*conn).applyfunc(s.cancel)==s.zeros(3)
    return new,{'from_n':n,'linear_system_shape':list(M.shape),'rank':21,
                'Q':str(Q),'Q_next':str(Qp),'transfer_numerator_degrees':degrees,
                'next_endpoint_A':str(Ap.subs(z,1)),
                'next_triple':list(map(str,new))}

A=s.Integer(7)-s.Rational(19,2)*z;B=-7+8*z;C=s.Rational(17,2)-s.Rational(9,2)*z
out={'scope':'Two fixed-size transfer steps, original Taylor and normalization checks','steps':[]}
archive=json.loads((HERE.parent.parent/'results/mixed_hermite_pade_n18.json').read_text())['models']['direct']
for n in (1,2):
    (A,B,C),cert=step(n,A,B,C)
    old=next(row for row in archive if row['n']==n+1)
    expected=s.Rational(old['raw_endpoint_A_from_primitive_integer_polynomials'],
                        old['raw_endpoint_B_from_primitive_integer_polynomials'])
    assert A.subs(z,1)==expected
    cert['frozen_archive_endpoint_match']=True
    out['steps'].append(cert)
out['status']='passed'
(HERE/'raw_rational_transfer_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Fixed 21-unknown transfer steps n=1→2 and n=2→3, original equations, degrees, determinant, and zero curvature passed.')
