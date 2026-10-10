"""Independent coefficient, Frobenius-ambiguity and rank checks."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent/'math_packages'))
import sympy as S
from sympy.polys.matrices import DomainMatrix
BASE=Path(__file__).resolve().parent
x,r=S.symbols('x r');u=x*(1-x);Q=(1+x)*(1+x*x)


def poly_mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]=(out[i+j]+v*w)%p
    return out


def poly_pow(a,n,p):
    out=[1]
    while n:
        if n%2:out=poly_mul(out,a,p)
        a=poly_mul(a,a,p);n//=2
    return out


def primitive(p,s,nu):
    rr=(p-6*s-3)//2
    P=poly_mul(poly_pow([0,1,-1],rr,p),poly_pow([1,1,1,1],2*s-nu,p),p)
    assert len(P)-1<p-1
    return [0]+[v*pow(k+1,-1,p)%p for k,v in enumerate(P)]


def h_vector(T,p,j):
    D=[3*j+1,-5*j-2,-5*j-2,-5*j-2,1]
    N=poly_mul(T,D,p);H=[0]*5
    invp=pow(p,-1,4)
    for k in range(1,len(N)):
        n=(k*invp-1)%4+1
        H[n]=(H[n]+N[k])%p
    return H


def evaluate_rat(a,rr,p):
    num,den=S.fraction(S.cancel(a.subs(r,rr)))
    return int(num)*pow(int(den),-1,p)%p


def endpoint0(H,p):
    return ((H[2]-H[3])*pow(4,-1,p)%p,(-H[1]+H[3]-2*H[4])*pow(2,-1,p)%p)


def run():
    data=json.loads((BASE/'witt_period_operator_symbolic.json').read_text())
    cont=json.loads((BASE/'witt_period_contiguity_symbolic.json').read_text())
    ids=[]; rows=[]
    p,s=59,1;rr=(p-6*s-3)//2
    for nu in (0,1):
        entry=data[str(nu)]; A=sum(S.sympify(v)*x**k for k,v in enumerate(entry['A_coefficients']))
        cc=list(map(S.sympify,entry['recurrence_coefficients']))
        bracket=(-S.Rational(2,3)*r-nu)*u*S.diff(Q,x)+(r-17)*Q*S.diff(u,x)
        residual=S.Poly(S.expand(u*Q*S.diff(A,x)+bracket*A-sum(cc[k]*Q**(4*k)*u**(18-6*k) for k in range(4))),x,r)
        assert residual.is_zero;ids.append('operator_nu'+str(nu))
        coeffs=[evaluate_rat(v,rr,p) for v in cc]
        Ts=[primitive(p,s+2*k,nu) for k in range(4)]
        raw=sum(c*sum(T) for c,T in zip(coeffs,Ts))%p
        beta=(-1)**(rr-17)*evaluate_rat(S.Poly(A,x).LC(),rr,p)%p
        assert raw==(-beta)%p and raw!=0
        Hs=[h_vector(T,p,0) for T in Ts]
        summed=[sum(c*H[k] for c,H in zip(coeffs,Hs))%p for k in range(5)]
        G=[0,2,-2,-2,-2]
        assert summed==[(-beta*v)%p for v in G]
        assert endpoint0(summed,p)==(0,0)
        rows.append(dict(kind='recurrence',nu=nu,p=p,s=s,r=rr,raw_at_one=raw,Frobenius_beta=beta,projected_RL=[0,0]))
    A=sum(S.sympify(v)*x**k for k,v in enumerate(cont['A_coefficients']))
    aa=list(map(S.sympify,cont['period_coefficients']))
    bracket=(r-11)*Q*S.diff(u,x)+(-S.Rational(2,3)*r-1)*u*S.diff(Q,x)
    residual=S.cancel(u*Q*S.diff(A,x)+bracket*A+sum(aa[k]*u**(12-6*k)*Q**(4*k+1) for k in range(3))-u**12)
    assert residual==0;ids.append('contiguity')
    aa_mod=[evaluate_rat(v,rr,p) for v in aa]
    T1=primitive(p,s,1);Ts=[primitive(p,s+2*k,0) for k in range(3)]
    raw=(sum(T1)-sum(c*sum(T) for c,T in zip(aa_mod,Ts)))%p
    beta=(-1)**(rr-11)*evaluate_rat(S.Poly(A,x).LC(),rr,p)%p
    assert raw==(-beta)%p and raw!=0
    H1=h_vector(T1,p,0);Hs=[h_vector(T,p,0) for T in Ts]
    Hdiff=[(H1[k]-sum(c*H[k] for c,H in zip(aa_mod,Hs)))%p for k in range(5)]
    assert Hdiff==[(-beta*v)%p for v in [0,2,-2,-2,-2]]
    assert endpoint0(Hdiff,p)==(0,0)
    rows.append(dict(kind='contiguity',p=p,s=s,r=rr,raw_at_one=raw,Frobenius_beta=beta,projected_RL=[0,0]))
    # Construct the square rank matrix from its expanded five-diagonal stencil.
    mat=S.zeros(26,26)
    for h in range(23):
        vals=[3*r-33+3*h,33-5*r,33-5*r,33-5*r,66-3*h]
        for shift,val in enumerate(vals):
            if h+shift<26:mat[h+shift,h]=val
            else:assert val==0
    for k in range(3):
        pol=S.Poly(-3*u**(12-6*k)*Q**(4*k),x)
        for i in range(26):mat[i,23+k]=pol.nth(i)
    stored=json.loads((BASE/'witt_actual_exterior_rank_certificate.json').read_text())
    assert mat==S.Matrix([[S.sympify(v) for v in row] for row in stored['matrix']])
    det=DomainMatrix.from_Matrix(mat).det().as_expr()
    assert S.expand(det-S.sympify(stored['determinant_factored']))==0
    return dict(status='PASS',coefficient_identities=ids,actual_Frobenius_correction_checks=rows,
                rank_matrix_independently_reconstructed=True,rank_determinant_recomputed_exactly=True,
                rank_determinant_degree=int(S.degree(det,r)),
                scope='Raw T identities are inhomogeneous; the projected identities survive because the correction is in the complete endpoint kernel.')


if __name__=='__main__':
    result=run();Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='actual_Frobenius_correction_checks'}))
