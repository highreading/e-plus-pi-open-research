"""Exact original-row checks of the second-order/Volterra transfer, n=3,5."""
import sys,json
from pathlib import Path
from math import factorial
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
z,t=s.symbols('z t');D=1+z*z
clean=s.cancel
def ff(k):return s.Rational(1,factorial(k)) if k>=0 else s.S.Zero
def tau(k):return s.Rational((-1)**((k-1)//2),k) if k>0 and k%2 else s.S.Zero
def original(n):
    rows=[[ff(k-j) for j in range(n+1)]+[tau(k-j) for j in range(n+1)] for k in range(n+1,3*n+1)]
    rows += [[-4]*(n+1)+[1]*(n+1),[1]*(n+1)+[0]*(n+1)]
    sol=s.Matrix(rows).inv()*s.Matrix([0]*(2*n+1)+[1])
    B=sum(sol[j]*z**j for j in range(n+1));C=sum(sol[n+1+j]*z**j for j in range(n+1))
    A=-sum(sum(sol[j]*ff(k-j)+sol[n+1+j]*tau(k-j) for j in range(n+1))*z**k for k in range(n+1))
    return list(map(s.expand,(A,B,C)))
def gauge(A,B,C):
    return s.Matrix([[D**2*A,B,C],
        [D**2*s.diff(A,z)+D*C,B+s.diff(B,z),s.diff(C,z)],
        [D**2*s.diff(A,z,2)+2*D*s.diff(C,z)-s.diff(D,z)*C,B+2*s.diff(B,z)+s.diff(B,z,2),s.diff(C,z,2)]])
def J(f,k=1):
    for r in range(k):
        f=s.integrate(f,t);f=s.expand(f-f.subs(t,0))
    return f
def reverse(B,n):return sum(B.coeff(z,k)*t**(n-k)/factorial(n-k) for k in range(n+1))
def euler(f,n,j):
    for a in range(j):f=s.expand((n-a)*f-t*s.diff(f,t))
    return f
out=[]
for n in (3,5):
    old=original(n);new=original(n+1)
    K=gauge(*old);Kn=gauge(*new)
    Q=clean(K.det()/z**(3*n-1));assert s.degree(Q,z)==3
    row=Kn[0,:]*K.inv();N=[clean(row[j]*Q) for j in range(3)]
    assert all(not s.denom(v).has(z) for v in N)
    AA=s.expand(sum(N));BB=s.expand(N[1]+2*N[2]);CC=s.expand(N[2])
    coef=lambda f,k:f.coeff(z,k) if 0<=k<=6 else s.S.Zero
    gam=coef(CC,6);delta=coef(CC,5);beta=coef(BB,5)
    assert coef(AA,6)==0 and coef(BB,6)==gam and coef(AA,5)==-n*gam
    def V(k):
        return s.expand(coef(AA,4-k)+(n+k)*coef(BB,5-k)+(n+k)*(n+k-1)*coef(CC,6-k)
            -t*(coef(BB,4-k)+2*(n+k)*coef(CC,5-k))+t*t*coef(CC,4-k))
    def fullop(P):
        return s.expand(gam*t*(t-1)*s.diff(P,t,2)+(delta*t*t-((2*n-2)*gam+beta)*t-gam)*s.diff(P,t)
                        +sum(V(k)*J(P,k) for k in range(7)))
    def primitive(P):
        return s.expand(sum(coef(f,d)*J(euler(P,n,j),6+j-d) for j,f in enumerate((AA,BB,CC)) for d in range(7) if coef(f,d)!=0))
    # The primitive expression has no negative integral powers here,
    # because A_6=0 and j>=1 in every remaining degree6 term.
    for k in range(n+1):
        P=t**k;W=primitive(P)
        assert W.subs(t,0)==0 and s.diff(W,t).subs(t,0)==0
        assert s.expand(s.diff(W,t,2)-fullop(P))==0
    P=reverse(old[1],n);Pn=reverse(new[1],n+1)
    lhs=sum(coef(Q,d)*J(Pn,3-d) for d in range(4))
    assert s.expand(lhs-fullop(P))==0
    # Independent weighted-Legendre rewriting.
    eps=delta-2*n*gam-beta
    Leg=t*(t-1)*s.diff(P,t,2)+(2*t-1)*s.diff(P,t)
    alt=gam*Leg+delta*t*(t-1)*s.diff(P,t)+eps*t*s.diff(P,t)+sum(V(k)*J(P,k) for k in range(7))
    assert s.expand(alt-fullop(P))==0
    # Root controls are exact bounded observations, not all-index claims.
    intervals=s.Poly(Q,z).intervals(eps=s.Rational(1,1000))
    real_count=sum(mult for interval,mult in intervals)
    pos_sum=sum(max(s.S.Zero,interval[1])*mult for interval,mult in intervals)
    q3=coef(Q,3)
    polynomial_sup_bound=lambda f:sum(abs(c) for c in s.Poly(f,t).all_coeffs())
    # A rational safe bound for the differential/Volterra numerator norm,
    # using sqrt(n(n+1))<=n+1 and K_n<=(n+1)^2.
    normbound=(abs(gam)*n*(n+1)+abs(delta)*(n+1)/2+abs(eps)*(n+1)**2
               +sum(polynomial_sup_bound(V(k))/factorial(k) for k in range(7)))/abs(q3)
    out.append({'n':n,'full_operator_identity_all_monomials':True,'primitive_boundary_cancellation':True,
                'actual_next_polynomial_matches':True,'weighted_legendre_rewriting':True,
                'real_roots_count':real_count,'isolating_intervals':[[str(v) for v in interval]+[mult] for interval,mult in intervals],
                'positive_root_upper_sum':str(pos_sum),
                'safe_rational_numerator_norm_bound':str(normbound),
                'gamma_over_Q3':str(gam/q3),'delta_over_Q3':str(delta/q3),'epsilon_over_Q3':str(eps/q3)})
result={'status':'PASS','scope':'Two selected exact rows from original Taylor/endpoint systems; no uniform coefficient or root bound inferred.','rows':out}
(HERE/'raw_integral_transfer_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
